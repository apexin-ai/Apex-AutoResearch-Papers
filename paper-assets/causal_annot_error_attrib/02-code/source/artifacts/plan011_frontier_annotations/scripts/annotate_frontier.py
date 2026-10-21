#!/usr/bin/env python3
"""
plan011: Frontier-model zero-shot annotation of VAST (K=3) + CivilComments (K=2).

Sends each test record to 3 frontier models via an OpenAI-compatible chat
completions endpoint. Supports streaming JSONL writes + resume (re-runs only
skip records whose idx already appears in the output JSONL).

Models (--model):
  llama4   -> meta-llama/llama-4-maverick
  qwen3    -> qwen/qwen3-235b-a22b
  deepseek -> deepseek/deepseek-chat-v3-0324

Usage:
  python annotate_frontier.py --dataset vast --model llama4
  python annotate_frontier.py --all

Output: results/{dataset}/{model}_zero-shot.jsonl
"""
import argparse
import json
import os
import re
import sys
import time
from difflib import SequenceMatcher
from pathlib import Path

import requests

# ── Config ──────────────────────────────────────────────────────────────────

PLAN_ROOT = Path("/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan011_frontier_annotations")
DATA_DIR = PLAN_ROOT / "data"
RESULTS_DIR = PLAN_ROOT / "results"

API_BASE = os.environ.get("OPENROUTER_API_BASE", "https://openrouter.ai/api/v1")
API_KEY = [REDACTED]"OPENROUTER_API_KEY", "tum_XXB3sZILRCg8llb3NjxVbbRNzFpsYVFdiogFkavpGn8")

MODELS = {
    "llama4": "meta-llama/llama-4-maverick",
    "qwen3": "qwen/qwen3-235b-a22b",
    "deepseek": "deepseek/deepseek-chat-v3-0324",
}

DATASETS = {
    "vast": {
        "classes": ["Con", "Pro", "Neutral"],
        "task": "Determine the stance expressed in this text toward the given topic.",
        "has_topic": True,
    },
    "civil_comments": {
        "classes": ["non-toxic", "toxic"],
        "task": "Classify whether this comment is toxic or non-toxic.",
        "has_topic": False,
    },
}


# ── Prompt ──────────────────────────────────────────────────────────────────

def build_prompt(text, topic, classes, task):
    """Build a zero-shot classification prompt with strict JSON output schema."""
    classes_str = ", ".join(f'"{c}"' for c in classes)
    topic_line = f"\nTopic: {topic}" if topic else ""
    return (
        f"{task}\n"
        f"\nCategories: {classes_str}"
        f"{topic_line}"
        f"\n\nText: \"{text}\""
        f"\n\nRespond with ONLY a JSON object in this exact format:"
        f"\n{{\"label\": \"<category_name>\"}}"
    )


# ── Label Parsing ────────────────────────────────────────────────────────────

def parse_label(raw_response, classes):
    """Extract predicted class from LLM raw response: JSON -> pattern -> fuzzy."""
    if not raw_response:
        return None
    text = raw_response.strip()

    # JSON match
    m = re.search(r'\{[^{}]*"label"\s*:\s*"([^"]+)"[^{}]*\}', text)
    if m:
        c = _match_to_class(m.group(1).strip(), classes)
        if c:
            return c

    # "label: X" pattern
    m = re.search(r'(?:label|category|class|answer)\s*[:=]\s*["\']?([^"\'\n,}]+)', text, re.IGNORECASE)
    if m:
        c = _match_to_class(m.group(1).strip().rstrip("."), classes)
        if c:
            return c

    # Unique class substring
    tl = text.lower()
    found = [c for c in classes if c.lower() in tl]
    if len(found) == 1:
        return found[0]

    # Fuzzy whole-response
    best, best_s = None, 0.0
    for c in classes:
        s = SequenceMatcher(None, tl, c.lower()).ratio()
        if s > best_s:
            best_s, best = s, c
    return best if best_s > 0.5 else None


def _match_to_class(candidate, classes):
    cl = candidate.lower().strip()
    for c in classes:
        if c.lower() == cl:
            return c
    for c in classes:
        if c.lower() in cl or cl in c.lower():
            return c
    best, best_s = None, 0.0
    for c in classes:
        s = max(
            SequenceMatcher(None, cl, c.lower()).ratio(),
            SequenceMatcher(None, cl, c.lower().replace("-", " ").replace("_", " ")).ratio(),
        )
        if s > best_s:
            best_s, best = s, c
    return best if best_s > 0.6 else None


# ── Annotation Pipeline ──────────────────────────────────────────────────────

class Pipeline:

    def __init__(self, api_base, api_key, model_id, max_retries=5, timeout=90):
        self.url = api_base.rstrip("/") + "/chat/completions"
        self.model_id = model_id
        self.max_retries = max_retries
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": [REDACTED]"Bearer {api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/causal-annot-error-attrib",
            "X-Title": "plan011_frontier",
        })

    def annotate_one(self, text, topic, classes, task):
        """Returns (pred_label_or_None, raw_response, error_or_None, n_retries)."""
        prompt = build_prompt(text, topic, classes, task)
        payload = {
            "model": self.model_id,
            "messages": [
                {"role": "system", "content": (
                    "You are a precise text classifier. "
                    "Always respond with ONLY a JSON object containing the label. "
                    "Do not include any explanation or extra text.")},
                {"role": "user", "content": prompt},
            ],
            "temperature": 0.0,
            "max_tokens": 32,
        }
        n_retries = 0
        for attempt in range(1, self.max_retries + 1):
            try:
                resp = self.session.post(self.url, json=payload, timeout=self.timeout)
                if resp.status_code in (402, 429) or resp.status_code >= 500:
                    n_retries += 1
                    wait = 30
                    print(f"    HTTP {resp.status_code} body={resp.text[:120]} — wait {wait}s "
                          f"(attempt {attempt}/{self.max_retries})", flush=True)
                    time.sleep(wait)
                    continue
                if resp.status_code != 200:
                    return None, "", f"HTTP {resp.status_code}: {resp.text[:200]}", n_retries
                data = resp.json()
                raw = data["choices"][0]["message"]["content"]
                pred = parse_label(raw, classes)
                return pred, raw, None, n_retries
            except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
                n_retries += 1
                err_t = "Timeout" if isinstance(e, requests.exceptions.Timeout) else "ConnError"
                print(f"    {err_t} — wait 30s (attempt {attempt}/{self.max_retries})", flush=True)
                if attempt < self.max_retries:
                    time.sleep(30)
                    continue
                return None, "", f"{err_t}: {e}", n_retries
            except Exception as e:
                return None, "", f"Unexpected: {type(e).__name__}: {e}", n_retries
        return None, "", "Max retries exceeded", n_retries


# ── I/O ──────────────────────────────────────────────────────────────────────

def load_samples(dataset):
    path = DATA_DIR / dataset / "test.jsonl"
    if not path.exists():
        sys.exit(f"ERROR: data file missing: {path}. Run prepare_data.py first.")
    out = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                out.append(json.loads(line))
    return out


def load_completed_idx(output_path):
    """Return set of idx values already in the JSONL file (for resume)."""
    if not output_path.exists():
        return set()
    done = set()
    with open(output_path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                r = json.loads(line)
                done.add(r["idx"])
            except Exception:
                pass
    return done


# ── Runner ──────────────────────────────────────────────────────────────────

def run_config(dataset, model_key, delay=0.3, hard_stop_on_repeated_failure=True):
    cfg = DATASETS[dataset]
    model_id = MODELS[model_key]
    samples = load_samples(dataset)

    out_dir = RESULTS_DIR / dataset
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{model_key}_zero-shot.jsonl"

    done = load_completed_idx(out_path)
    remaining = [s for s in samples if s["idx"] not in done]

    print(f"\n{'='*60}\nConfig: {dataset} / {model_key} ({model_id})\n"
          f"  Samples: {len(samples)} | Done: {len(done)} | Remaining: {len(remaining)}\n"
          f"  Output: {out_path}\n{'='*60}", flush=True)

    if not remaining:
        return {"status": "complete", "n_done": len(done), "n_failed": 0}

    pipe = Pipeline(API_BASE, API_KEY, model_id)
    consecutive_failures = 0
    n_failed = 0
    n_done = len(done)
    t0 = time.time()

    with open(out_path, "a") as fout:
        for i, s in enumerate(remaining):
            text = s["text"]
            topic = s.get("topic", "") if cfg["has_topic"] else ""
            pred, raw, err, retries = pipe.annotate_one(text, topic, cfg["classes"], cfg["task"])

            rec = {
                "idx": s["idx"],
                "text": text,
                "gold_label": s["label_name"],
                "gold_label_id": s["label"],
                "pred_label": pred,
                "raw_response": raw,
                "model_key": model_key,
                "model_id": model_id,
                "prompt_type": "zero-shot",
                "n_retries": retries,
                "error": err,
            }
            if cfg["has_topic"]:
                rec["topic"] = s.get("topic", "")
            fout.write(json.dumps(rec, ensure_ascii=False) + "\n")
            fout.flush()

            if err:
                n_failed += 1
                consecutive_failures += 1
                if hard_stop_on_repeated_failure and consecutive_failures >= 20:
                    print(f"  ABORT: {consecutive_failures} consecutive failures. Last err: {err}",
                          flush=True)
                    return {"status": "aborted", "n_done": n_done,
                            "n_failed": n_failed, "last_error": err}
            else:
                consecutive_failures = 0
            n_done += 1

            if (i + 1) % 50 == 0:
                elapsed = time.time() - t0
                rate = (i + 1) / max(elapsed, 1e-9)
                eta = (len(remaining) - i - 1) / max(rate, 1e-9)
                n_parsed = i + 1 - n_failed
                print(f"  [{i+1}/{len(remaining)}] parsed={n_parsed} failed={n_failed} "
                      f"rate={rate:.2f}/s eta={eta/60:.1f}m", flush=True)

            if i < len(remaining) - 1:
                time.sleep(delay)

    return {"status": "complete", "n_done": n_done, "n_failed": n_failed}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dataset", choices=list(DATASETS) + ["all"], default="all")
    ap.add_argument("--model", choices=list(MODELS) + ["all"], default="all")
    ap.add_argument("--delay", type=float, default=0.3)
    ap.add_argument("--smoke", action="store_true",
                    help="Just send 1 test request to verify auth, don't iterate dataset")
    args = ap.parse_args()

    if args.smoke:
        pipe = Pipeline(API_BASE, API_KEY, MODELS["deepseek"])
        pred, raw, err, n = pipe.annotate_one(
            "I really hate this policy.", "Gun Control",
            DATASETS["vast"]["classes"], DATASETS["vast"]["task"])
        print(f"SMOKE: pred={pred} raw={raw!r} err={err} retries={n}")
        return

    ds_list = list(DATASETS) if args.dataset == "all" else [args.dataset]
    m_list = list(MODELS) if args.model == "all" else [args.model]

    summary = []
    for ds in ds_list:
        for m in m_list:
            r = run_config(ds, m, delay=args.delay)
            r.update({"dataset": ds, "model": m})
            summary.append(r)

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    for r in summary:
        print(f"  {r['dataset']}/{r['model']}: status={r['status']} "
              f"done={r['n_done']} failed={r['n_failed']}")


if __name__ == "__main__":
    main()
