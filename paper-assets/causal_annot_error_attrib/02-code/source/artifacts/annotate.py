#!/usr/bin/env python3
"""
LLM Annotation Pipeline for Causal Annotation Error Attribution

Annotates text classification datasets using multiple LLMs via OpenRouter-compatible API.
Produces confusion matrices C comparing LLM labels vs gold labels.

Usage:
  python annotate.py --dataset humaid --model llama4 --prompt zero-shot --sample 500
  python annotate.py --dataset vast --model all --prompt all --sample 1000
  python annotate.py --all --sample 500  # run all combinations

Input: data/{dataset}/{split}.jsonl (from preprocess.py)
Output: results/{dataset}/{model}_{prompt}.jsonl + confusion_matrix.npz
"""

import argparse
import json
import os
import re
import sys
import time
import traceback
from pathlib import Path
from difflib import SequenceMatcher

import numpy as np
import requests

# ── API Configuration ────────────────────────────────────────────────────────

API_BASE = os.environ.get("OPENROUTER_API_BASE", "https://openrouter.ai/api/v1")

MODELS = {
    "llama4": "meta-llama/llama-4-maverick",
    "qwen3": "qwen/qwen3-235b-a22b",
    "deepseek": "deepseek/deepseek-chat",
}

PROJECT_ROOT = Path(__file__).resolve().parent
DATA_DIR = PROJECT_ROOT / "data"
RESULTS_DIR = PROJECT_ROOT / "results"


# ── Dataset Configurations ───────────────────────────────────────────────────

DATASET_CONFIGS = {
    "humaid": {
        "classes": [
            "caution_and_advice",
            "displaced_people_and_evacuations",
            "donation_and_volunteering",
            "infrastructure_and_utility_damage",
            "injured_or_dead_people",
            "missing_or_found_people",
            "not_humanitarian",
            "other_relevant_information",
            "requests_or_urgent_needs",
            "rescue_volunteering_or_donation_effort",
            "sympathy_and_support",
        ],
        "task": "Classify this tweet into one of the following crisis event categories.",
        "text_field": "text",
        "label_field": "label",
        "few_shot_examples": [
            {"text": "Please stay away from the coastal areas. Tsunami warning issued.", "label": "caution_and_advice"},
            {"text": "Over 500 families displaced from their homes due to flooding.", "label": "displaced_people_and_evacuations"},
            {"text": "We are collecting blankets and food for the victims. Please donate.", "label": "donation_and_volunteering"},
            {"text": "The main bridge on Highway 5 has completely collapsed.", "label": "infrastructure_and_utility_damage"},
            {"text": "Sadly, 12 people confirmed dead after the earthquake.", "label": "injured_or_dead_people"},
        ],
    },
    "vast": {
        "classes": [
            "Pro",
            "Con",
            "Neutral",
        ],
        "task": "Determine the stance expressed in this text toward the given topic.",
        "text_field": "text",
        "label_field": "label",
        "topic_field": "topic",
        "few_shot_examples": [
            {"text": "Gun control is essential for public safety.", "topic": "Gun Control", "label": "Pro"},
            {"text": "More regulations will not stop criminals from getting guns.", "topic": "Gun Control", "label": "Con"},
            {"text": "The debate on gun control continues across the country.", "topic": "Gun Control", "label": "Neutral"},
            {"text": "Immigration brings valuable diversity to our communities.", "topic": "Immigration", "label": "Pro"},
            {"text": "Open borders threaten national security and jobs.", "topic": "Immigration", "label": "Con"},
        ],
    },
    "civil_comments": {
        "classes": [
            "non-toxic",
            "toxic",
        ],
        "task": "Classify whether this comment is toxic or non-toxic.",
        "text_field": "text",
        "label_field": "label",
        "few_shot_examples": [
            {"text": "I think we should consider all perspectives before making a decision.", "label": "non-toxic"},
            {"text": "You are an absolute idiot and should never speak again.", "label": "toxic"},
            {"text": "This policy change could have both positive and negative effects.", "label": "non-toxic"},
            {"text": "People like you are what's wrong with this country, just shut up.", "label": "toxic"},
            {"text": "I respectfully disagree with the author's conclusions.", "label": "non-toxic"},
        ],
    },
}


# ── Prompt Templates ─────────────────────────────────────────────────────────

class PromptTemplates:

    @staticmethod
    def _format_classes(classes):
        return ", ".join(f'"{c}"' for c in classes)

    @staticmethod
    def zero_shot(text, config):
        classes_str = PromptTemplates._format_classes(config["classes"])
        task = config["task"]
        topic_line = ""
        if "topic_field" in config and "__topic__" in text:
            parts = text.split("__topic__:", 1)
            actual_text = parts[0].strip()
            topic = parts[1].strip()
            topic_line = f"\nTopic: {topic}"
            text = actual_text
        prompt = (
            f"{task}\n"
            f"\nCategories: {classes_str}"
            f"{topic_line}"
            f"\n\nText: \"{text}\""
            f"\n\nRespond with ONLY a JSON object in this exact format:"
            f"\n{{\"label\": \"<category_name>\"}}"
        )
        return prompt

    @staticmethod
    def few_shot(text, config, n_examples):
        classes_str = PromptTemplates._format_classes(config["classes"])
        task = config["task"]
        examples = config["few_shot_examples"][:n_examples]
        has_topic = "topic_field" in config

        topic_line = ""
        if has_topic and "__topic__:" in text:
            parts = text.split("__topic__:", 1)
            actual_text = parts[0].strip()
            topic = parts[1].strip()
            topic_line = f"\nTopic: {topic}"
            text = actual_text

        prompt = (
            f"{task}\n"
            f"\nCategories: {classes_str}\n"
            f"\nHere are some examples:\n"
        )
        for i, ex in enumerate(examples, 1):
            ex_topic = ""
            if has_topic and "topic" in ex:
                ex_topic = f"\nTopic: {ex['topic']}"
            prompt += (
                f"\nExample {i}:"
                f"{ex_topic}"
                f"\nText: \"{ex['text']}\""
                f"\nAnswer: {{\"label\": \"{ex['label']}\"}}\n"
            )

        prompt += (
            f"\nNow classify the following:"
            f"{topic_line}"
            f"\nText: \"{text}\""
            f"\n\nRespond with ONLY a JSON object in this exact format:"
            f"\n{{\"label\": \"<category_name>\"}}"
        )
        return prompt


# ── Label Parsing ────────────────────────────────────────────────────────────

def parse_label(raw_response, classes):
    """Extract predicted label from LLM response via JSON parsing + fuzzy matching."""
    text = raw_response.strip()

    # Try JSON extraction
    json_match = re.search(r'\{[^}]*"label"\s*:\s*"([^"]+)"[^}]*\}', text)
    if json_match:
        candidate = json_match.group(1).strip()
        matched = _match_to_class(candidate, classes)
        if matched:
            return matched

    # Try "Category: X" or "Label: X" pattern
    pattern_match = re.search(r'(?:category|label|class|answer)\s*[:=]\s*["\']?([^"\'\n,}]+)', text, re.IGNORECASE)
    if pattern_match:
        candidate = pattern_match.group(1).strip().rstrip(".")
        matched = _match_to_class(candidate, classes)
        if matched:
            return matched

    # Try to find any class name appearing in the response
    text_lower = text.lower()
    found = []
    for cls in classes:
        if cls.lower() in text_lower:
            found.append(cls)
    if len(found) == 1:
        return found[0]

    # Fuzzy match the entire response against class names
    best_match = None
    best_score = 0.0
    for cls in classes:
        score = SequenceMatcher(None, text_lower, cls.lower()).ratio()
        if score > best_score:
            best_score = score
            best_match = cls
    if best_score > 0.5:
        return best_match

    return None


def _match_to_class(candidate, classes):
    """Match a candidate string to one of the valid classes."""
    candidate_lower = candidate.lower().strip()

    # Exact match (case-insensitive)
    for cls in classes:
        if cls.lower() == candidate_lower:
            return cls

    # Substring match
    for cls in classes:
        if cls.lower() in candidate_lower or candidate_lower in cls.lower():
            return cls

    # Fuzzy match
    best_match = None
    best_score = 0.0
    for cls in classes:
        # Also try with underscores replaced by spaces
        score = max(
            SequenceMatcher(None, candidate_lower, cls.lower()).ratio(),
            SequenceMatcher(None, candidate_lower, cls.lower().replace("_", " ")).ratio(),
        )
        if score > best_score:
            best_score = score
            best_match = cls
    if best_score > 0.6:
        return best_match

    return None


# ── Annotation Pipeline ─────────────────────────────────────────────────────

class AnnotationPipeline:

    def __init__(self, api_base, api_key, model_id, max_retries=5, timeout=60):
        self.api_base = api_base.rstrip("/")
        self.api_key = [REDACTED]
        self.model_id = model_id
        self.max_retries = max_retries
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": [REDACTED]"Bearer {self.api_key}",
            "Content-Type": "application/json",
        })

    def annotate_single(self, text, config, prompt_type, n_examples=0):
        """Send one text to LLM, parse response to class label.

        Returns (pred_label_or_None, raw_response, error_msg_or_None, n_retries).
        """
        if prompt_type == "zero-shot":
            user_prompt = PromptTemplates.zero_shot(text, config)
        else:
            user_prompt = PromptTemplates.few_shot(text, config, n_examples)

        payload = {
            "model": self.model_id,
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You are a precise text classifier. "
                        "Always respond with ONLY a JSON object containing the label. "
                        "Do not include any explanation or extra text."
                    ),
                },
                {"role": "user", "content": user_prompt},
            ],
            "temperature": 0.0,
            "max_tokens": 64,
        }

        n_retries = 0
        for attempt in range(1, self.max_retries + 1):
            try:
                resp = self.session.post(
                    f"{self.api_base}/chat/completions",
                    json=payload,
                    timeout=self.timeout,
                )
                resp.raise_for_status()
                data = resp.json()
                raw = data["choices"][0]["message"]["content"]
                pred = parse_label(raw, config["classes"])
                return pred, raw, None, n_retries
            except requests.exceptions.HTTPError as e:
                status = e.response.status_code if e.response is not None else None
                if status == 429 or (status and status >= 500):
                    n_retries += 1
                    wait = min(2 * (2 ** (attempt - 1)), 60)
                    label = "Rate limited (429)" if status == 429 else f"Server error ({status})"
                    print(f"  {label}, waiting {wait}s (attempt {attempt}/{self.max_retries})")
                    time.sleep(wait)
                    continue
                return None, "", f"HTTP {status}: {e}", n_retries
            except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
                n_retries += 1
                wait = min(2 * (2 ** (attempt - 1)), 60)
                err_type = "Timeout" if isinstance(e, requests.exceptions.Timeout) else "ConnectionError"
                print(f"  {err_type}, waiting {wait}s (attempt {attempt}/{self.max_retries})")
                if attempt < self.max_retries:
                    time.sleep(wait)
                    continue
                return None, "", f"{err_type}: {e}", n_retries
            except Exception as e:
                return None, "", f"Unexpected error: {e}", n_retries

        return None, "", "Max retries exceeded", n_retries

    def annotate_batch(self, samples, config, prompt_type, batch_delay=0.5, output_dir=None):
        """Annotate a list of samples with rate limiting.

        Each sample is a dict with at least text_field and label_field.
        Returns list of result dicts.
        """
        n_examples = 0
        if prompt_type == "few-shot-3":
            n_examples = 3
        elif prompt_type == "few-shot-5":
            n_examples = 5

        text_field = config["text_field"]
        topic_field = config.get("topic_field")

        results = []
        total_retries = 0
        failed_samples = []

        for i, sample in enumerate(samples):
            text = sample[text_field]
            if topic_field and topic_field in sample:
                text = f"{text} __topic__:{sample[topic_field]}"

            pred, raw, err, n_retries = self.annotate_single(text, config, prompt_type, n_examples)
            total_retries += n_retries

            result = {
                "idx": sample.get("idx", i),
                "text": sample[text_field],
                "gold_label": sample[config["label_field"]],
                "pred_label": pred,
                "raw_response": raw,
                "model": self.model_id,
                "prompt_type": prompt_type,
                "error": err,
            }
            if topic_field and topic_field in sample:
                result["topic"] = sample[topic_field]

            results.append(result)

            if err and pred is None:
                failed_samples.append({
                    "sample_id": sample.get("idx", i),
                    "error_type": err.split(":")[0] if ":" in err else err,
                    "error_msg": err,
                })

            if (i + 1) % 50 == 0:
                n_parsed = sum(1 for r in results if r["pred_label"] is not None)
                print(f"  [{i+1}/{len(samples)}] parsed: {n_parsed}/{i+1}")

            if i < len(samples) - 1:
                time.sleep(batch_delay)

        if failed_samples and output_dir:
            output_dir.mkdir(parents=True, exist_ok=True)
            failed_path = output_dir / "failed_samples.jsonl"
            with open(failed_path, "a") as f:
                for fs in failed_samples:
                    f.write(json.dumps(fs, ensure_ascii=False) + "\n")
            print(f"  {len(failed_samples)} failed samples saved to {failed_path}")

        print(f"  Retry stats: {total_retries} total retries, {len(failed_samples)} final failures")
        return results


# ── Confusion Matrix ─────────────────────────────────────────────────────────

def compute_confusion_matrix(gold_labels, pred_labels, classes):
    """Compute column-stochastic confusion matrix C[j,i] = P(pred=j|gold=i).

    Args:
        gold_labels: list of gold label strings
        pred_labels: list of predicted label strings (may contain None)
        classes: ordered list of class names

    Returns:
        C: (K, K) column-stochastic numpy array
        class_to_idx: dict mapping class name to index
        stats: dict with coverage info
    """
    K = len(classes)
    class_to_idx = {c: i for i, c in enumerate(classes)}
    C = np.zeros((K, K))

    n_valid = 0
    n_skipped = 0
    for g, p in zip(gold_labels, pred_labels):
        if p is None or g not in class_to_idx or p not in class_to_idx:
            n_skipped += 1
            continue
        C[class_to_idx[p], class_to_idx[g]] += 1
        n_valid += 1

    col_sums = C.sum(axis=0)
    col_sums[col_sums == 0] = 1
    C_norm = C / col_sums

    stats = {
        "n_total": len(gold_labels),
        "n_valid": n_valid,
        "n_skipped": n_skipped,
        "coverage": n_valid / len(gold_labels) if gold_labels else 0,
        "raw_counts": C.tolist(),
    }

    return C_norm, class_to_idx, stats


# ── I/O ──────────────────────────────────────────────────────────────────────

def load_data(dataset_name, split, sample_size, seed=42):
    """Load dataset from data/{dataset}/{split}.jsonl, optionally sample."""
    path = DATA_DIR / dataset_name / f"{split}.jsonl"
    if not path.exists():
        print(f"ERROR: Data file not found: {path}")
        print(f"Run preprocess.py first to prepare the datasets.")
        sys.exit(1)

    samples = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                samples.append(json.loads(line))

    if dataset_name == "vast":
        seen = set()
        deduped = []
        for s in samples:
            key = (s.get("text", ""), s.get("topic", ""), s.get("label_name", s.get("label", "")))
            if key not in seen:
                seen.add(key)
                deduped.append(s)
        n_removed = len(samples) - len(deduped)
        if n_removed > 0:
            print(f"VAST dedup: removed {n_removed} duplicates ({len(samples)} -> {len(deduped)})")
        samples = deduped

    if sample_size and sample_size < len(samples):
        rng = np.random.default_rng(seed)
        indices = rng.choice(len(samples), size=sample_size, replace=False)
        indices.sort()
        samples = [samples[i] for i in indices]

    for i, s in enumerate(samples):
        if "idx" not in s:
            s["idx"] = i

    return samples


def load_existing_results(output_path):
    """Load already-completed results for resume support."""
    if not output_path.exists():
        return {}
    existing = {}
    with open(output_path) as f:
        for line in f:
            line = line.strip()
            if line:
                r = json.loads(line)
                existing[r["idx"]] = r
    return existing


def save_results(results, confusion_matrix, class_to_idx, stats, output_dir, model_key, prompt_type):
    """Save annotations as JSONL and confusion matrix as npz."""
    output_dir.mkdir(parents=True, exist_ok=True)

    jsonl_path = output_dir / f"{model_key}_{prompt_type}.jsonl"
    with open(jsonl_path, "w") as f:
        for r in results:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    npz_path = output_dir / f"{model_key}_{prompt_type}_confusion_matrix.npz"
    np.savez(
        npz_path,
        C=confusion_matrix,
        classes=list(class_to_idx.keys()),
        **{f"stat_{k}": v for k, v in stats.items() if not isinstance(v, (list, dict))},
        raw_counts=np.array(stats["raw_counts"]),
    )

    print(f"  Saved: {jsonl_path}")
    print(f"  Saved: {npz_path}")
    return jsonl_path, npz_path


# ── Main ─────────────────────────────────────────────────────────────────────

def run_single(dataset_name, model_key, prompt_type, sample_size, split, api_key):
    """Run annotation for one (dataset, model, prompt) combination."""
    config = DATASET_CONFIGS[dataset_name]
    model_id = MODELS[model_key]

    output_dir = RESULTS_DIR / dataset_name
    output_path = output_dir / f"{model_key}_{prompt_type}.jsonl"

    print(f"\n{'='*60}")
    print(f"Dataset: {dataset_name} | Model: {model_key} ({model_id})")
    print(f"Prompt: {prompt_type} | Sample: {sample_size} | Split: {split}")
    print(f"{'='*60}")

    samples = load_data(dataset_name, split, sample_size)
    print(f"Loaded {len(samples)} samples")

    # Resume support
    existing = load_existing_results(output_path)
    if existing:
        remaining = [s for s in samples if s["idx"] not in existing]
        print(f"Resuming: {len(existing)} done, {len(remaining)} remaining")
    else:
        remaining = samples

    if not remaining:
        print("All samples already annotated. Recomputing confusion matrix...")
        all_results = [existing[s["idx"]] for s in samples if s["idx"] in existing]
    else:
        pipeline = AnnotationPipeline(API_BASE, api_key, model_id)
        new_results = pipeline.annotate_batch(remaining, config, prompt_type, output_dir=output_dir)

        merged = dict(existing)
        for r in new_results:
            merged[r["idx"]] = r
        all_results = [merged[s["idx"]] for s in samples if s["idx"] in merged]

    # Compute confusion matrix
    gold = [r["gold_label"] for r in all_results]
    pred = [r["pred_label"] for r in all_results]
    C, class_to_idx, stats = compute_confusion_matrix(gold, pred, config["classes"])

    raw_counts = np.array(stats["raw_counts"])
    col_counts = raw_counts.sum(axis=0).astype(int)
    stats["per_column_counts"] = {cls: int(col_counts[i]) for i, cls in enumerate(config["classes"])}

    if dataset_name == "humaid":
        low_cols = [(cls, int(col_counts[i])) for i, cls in enumerate(config["classes"]) if col_counts[i] < 20]
        if low_cols:
            print(f"\n  WARNING: HumAID columns with < 20 samples:")
            for cls, cnt in low_cols:
                print(f"    {cls}: {cnt}")
            stats["low_column_warning"] = [{"class": cls, "count": cnt} for cls, cnt in low_cols]

    print(f"\n  Per-column sample counts:")
    for cls in config["classes"]:
        print(f"    {cls}: {stats['per_column_counts'][cls]}")

    save_results(all_results, C, class_to_idx, stats, output_dir, model_key, prompt_type)

    n_parsed = sum(1 for r in all_results if r["pred_label"] is not None)
    n_correct = sum(1 for r in all_results if r["pred_label"] == r["gold_label"])
    print(f"\nResults: {n_parsed}/{len(all_results)} parsed, "
          f"{n_correct}/{n_parsed} correct ({n_correct/max(n_parsed,1)*100:.1f}%)")
    print(f"Confusion matrix coverage: {stats['coverage']:.1%}")
    print(f"Confusion matrix C (column-stochastic):\n{np.array2string(C, precision=3)}")


def main():
    parser = argparse.ArgumentParser(
        description="LLM Annotation Pipeline for Causal Annotation Error Attribution"
    )
    parser.add_argument(
        "--dataset",
        choices=["humaid", "vast", "civil_comments", "all"],
        help="Dataset to annotate",
    )
    parser.add_argument(
        "--model",
        choices=["llama4", "qwen3", "deepseek", "all"],
        help="Model to use",
    )
    parser.add_argument(
        "--prompt",
        choices=["zero-shot", "few-shot-3", "few-shot-5", "all"],
        help="Prompt variant",
    )
    parser.add_argument(
        "--sample", type=int, default=500, help="Sample size per dataset (default: 500)"
    )
    parser.add_argument(
        "--split", default="test", help="Which split to annotate (default: test)"
    )
    parser.add_argument(
        "--all", action="store_true", dest="run_all", help="Run all (dataset x model x prompt) combinations"
    )
    parser.add_argument(
        "--delay", type=float, default=0.5, help="Delay between API calls in seconds (default: 0.5)"
    )
    parser.add_argument(
        "--api-base", default=None,
        help="Override API base URL (default: env OPENROUTER_API_BASE or https://openrouter.ai/api/v1)"
    )

    args = parser.parse_args()

    if args.run_all:
        args.dataset = "all"
        args.model = "all"
        args.prompt = "all"

    if not args.run_all and not (args.dataset and args.model and args.prompt):
        parser.error("Specify --dataset, --model, --prompt (or use --all)")

    api_key = [REDACTED]"OPENROUTER_API_KEY")
    if not api_key:
        print("ERROR: OPENROUTER_API_KEY environment variable not set.")
        sys.exit(1)

    global API_BASE
    if args.api_base:
        API_BASE = args.api_base

    datasets = list(DATASET_CONFIGS.keys()) if args.dataset == "all" else [args.dataset]
    models = list(MODELS.keys()) if args.model == "all" else [args.model]
    prompts = ["zero-shot", "few-shot-3", "few-shot-5"] if args.prompt == "all" else [args.prompt]

    total = len(datasets) * len(models) * len(prompts)
    done = 0

    for ds in datasets:
        for mdl in models:
            for pt in prompts:
                done += 1
                print(f"\n[{done}/{total}] Running {ds} / {mdl} / {pt}")
                try:
                    run_single(ds, mdl, pt, args.sample, args.split, api_key)
                except Exception as e:
                    print(f"FAILED: {e}")
                    traceback.print_exc()

    print(f"\nDone. {done}/{total} combinations processed.")


if __name__ == "__main__":
    main()
