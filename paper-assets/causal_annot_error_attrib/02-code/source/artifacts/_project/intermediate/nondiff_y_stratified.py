#!/usr/bin/env python3
"""
MF-2: Y-Stratified Non-Differential Misclassification Test

Tests whether LLM annotation error rates are independent of outcome proxies Y,
i.e. P(A*|A, Y) = P(A*|A). Uses permutation tests on column-stochastic
confusion matrices stratified by three Y proxies.

Phase 1 (annotate): LLM stance classification on VAST test data via OpenRouter.
Phase 2 (test):     Y-stratified permutation tests on annotation results.

Input:  artifacts/plan011_frontier_annotations/data/vast/test.jsonl
Output: artifacts/nondiff_y_stratified_annotations.jsonl  (Phase 1)
        artifacts/nondiff_y_stratified_results.json       (Phase 2)

Usage:
  python3 nondiff_y_stratified.py --phase annotate --api-key <KEY> [--smoke] [--model deepseek/deepseek-chat]
  python3 nondiff_y_stratified.py --phase test [--permutations 10000]
  python3 nondiff_y_stratified.py --phase all --api-key <KEY> [--smoke]

Dependencies: numpy, requests (stdlib otherwise)
"""

import argparse
import json
import os
import re
import sys
import time
from collections import Counter
from difflib import SequenceMatcher
from pathlib import Path

import numpy as np

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_PATH = SCRIPT_DIR / "plan011_frontier_annotations" / "data" / "vast" / "test.jsonl"
ANNOTATION_PATH = SCRIPT_DIR / "nondiff_y_stratified_annotations.jsonl"
RESULTS_PATH = SCRIPT_DIR / "nondiff_y_stratified_results.json"

LABEL_MAP = {"Pro": 1, "Con": 0, "Neutral": 2}
LABEL_NAMES = {v: k for k, v in LABEL_MAP.items()}
CLASS_NAMES = ["Con", "Pro", "Neutral"]
K = 3

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
DEFAULT_MODEL = "deepseek/deepseek-chat"

PROMPT_TEMPLATE = """Determine the stance expressed in this text toward the given topic.

Categories: "Pro", "Con", "Neutral"

Topic: {topic}

Text: "{text}"

Respond with ONLY a JSON object in this exact format:
{{"label": "<category_name>"}}"""

POSITIVE_WORDS = {"good", "great", "best", "love", "right", "support",
                  "agree", "positive", "benefit", "important"}
NEGATIVE_WORDS = {"bad", "worst", "hate", "wrong", "against", "oppose",
                  "negative", "harm", "dangerous", "fail"}


# ── Phase 1: Annotation ─────────────────────────────────────

def parse_label(response_text):
    """Extract predicted label from LLM response. Returns (label_int, label_name) or (None, None)."""
    valid = {"Pro", "Con", "Neutral"}

    # 1) JSON extraction
    m = re.search(r'\{\s*"label"\s*:\s*"([^"]+)"\s*\}', response_text)
    if m and m.group(1) in valid:
        name = m.group(1)
        return LABEL_MAP[name], name

    # 2) "label: X" or "answer: X" pattern
    m = re.search(r'(?:label|answer)\s*[:=]\s*"?(\w+)"?', response_text, re.IGNORECASE)
    if m:
        candidate = m.group(1).capitalize()
        if candidate in valid:
            return LABEL_MAP[candidate], candidate

    # 3) Unique mention
    found = [w for w in valid if w.lower() in response_text.lower()]
    if len(found) == 1:
        name = found[0]
        return LABEL_MAP[name], name

    # 4) Fuzzy match
    best_score, best_name = 0.0, None
    for w in valid:
        for token in re.findall(r'\w+', response_text):
            score = SequenceMatcher(None, token.lower(), w.lower()).ratio()
            if score > best_score:
                best_score = score
                best_name = w
    if best_score > 0.5 and best_name is not None:
        return LABEL_MAP[best_name], best_name

    return None, None


def call_openrouter(api_key, model, topic, text):
    """Single OpenRouter API call with retry on 429."""
    import requests

    prompt = PROMPT_TEMPLATE.format(topic=topic, text=text)
    headers = {
        "Authorization": [REDACTED]"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    body = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0,
    }

    backoff = 1.0
    for attempt in range(6):
        try:
            resp = requests.post(OPENROUTER_URL, headers=headers, json=body, timeout=60)
        except requests.RequestException as e:
            return None, f"request_error: {e}"

        if resp.status_code == 402:
            print(f"\nERROR: 402 Payment Required. Check your OpenRouter balance.", file=sys.stderr)
            sys.exit(1)

        if resp.status_code == 429:
            if attempt < 5:
                time.sleep(backoff)
                backoff *= 2
                continue
            return None, "429_max_retries"

        if resp.status_code != 200:
            return None, f"http_{resp.status_code}: {resp.text[:200]}"

        try:
            data = resp.json()
            content = data["choices"][0]["message"]["content"]
            return content, None
        except (KeyError, IndexError, json.JSONDecodeError) as e:
            return None, f"parse_error: {e}"

    return None, "unknown_error"


def run_annotate(api_key, model, smoke):
    """Phase 1: annotate VAST test data."""
    import requests  # noqa: F811 — validate import early

    if not DATA_PATH.exists():
        print(f"ERROR: VAST data not found at {DATA_PATH}", file=sys.stderr)
        sys.exit(1)

    with open(DATA_PATH) as f:
        samples = [json.loads(line) for line in f]

    if smoke:
        samples = samples[:5]

    done_idxs = set()
    if ANNOTATION_PATH.exists() and not smoke:
        with open(ANNOTATION_PATH) as f:
            for line in f:
                try:
                    rec = json.loads(line)
                    done_idxs.add(rec["idx"])
                except (json.JSONDecodeError, KeyError):
                    pass
        print(f"Resuming: {len(done_idxs)} already annotated")

    todo = [s for s in samples if s["idx"] not in done_idxs]
    if not todo:
        print("All samples already annotated.")
        return

    print(f"Annotating {len(todo)} samples with {model}...")
    mode = "a" if done_idxs else "w"
    with open(ANNOTATION_PATH, mode) as fout:
        for i, sample in enumerate(todo):
            raw, error = call_openrouter(api_key, model, sample["topic"], sample["text"])

            rec = {
                "idx": sample["idx"],
                "text": sample["text"],
                "topic": sample["topic"],
                "gold_label": sample["label"],
                "gold_label_name": sample["label_name"],
            }

            if error:
                rec["predicted_label"] = None
                rec["predicted_label_name"] = None
                rec["raw_response"] = None
                rec["error"] = error
            else:
                pred_label, pred_name = parse_label(raw)
                rec["predicted_label"] = pred_label
                rec["predicted_label_name"] = pred_name
                rec["raw_response"] = raw

            fout.write(json.dumps(rec, ensure_ascii=False) + "\n")
            fout.flush()

            if smoke:
                print(f"  [{sample['idx']}] gold={sample['label_name']}, "
                      f"pred={rec['predicted_label_name']}, raw={raw}")

            if (i + 1) % 50 == 0:
                print(f"  Progress: {i + 1}/{len(todo)}")

            time.sleep(0.3)

    total = len(done_idxs) + len(todo)
    print(f"Done. {total} annotations saved to {ANNOTATION_PATH}")


# ── Phase 2: Testing ─────────────────────────────────────────

def load_annotations():
    """Load annotations, return list of valid records."""
    if not ANNOTATION_PATH.exists():
        print(f"ERROR: Annotation file not found at {ANNOTATION_PATH}", file=sys.stderr)
        sys.exit(1)

    records = []
    parse_failures = 0
    with open(ANNOTATION_PATH) as f:
        for line in f:
            rec = json.loads(line)
            if rec.get("predicted_label") is None:
                parse_failures += 1
            else:
                records.append(rec)
    return records, parse_failures


def compute_confusion_matrix(records, gold_key="gold_label", pred_key="predicted_label"):
    """Column-stochastic K×K confusion matrix. C[j,k] = P(A*=j | A=k)."""
    counts = np.zeros((K, K), dtype=float)
    for r in records:
        g = r[gold_key]
        p = r[pred_key]
        if g is not None and p is not None and 0 <= g < K and 0 <= p < K:
            counts[p, g] += 1

    col_sums = counts.sum(axis=0)
    C = np.full((K, K), np.nan)
    for k in range(K):
        if col_sums[k] > 0:
            C[:, k] = counts[:, k] / col_sums[k]
    return C


def compute_sentiment_proxy(text):
    """Binary sentiment proxy: positive ratio > 0.5."""
    words = set(re.findall(r'\w+', text.lower()))
    pos = len(words & POSITIVE_WORDS)
    neg = len(words & NEGATIVE_WORDS)
    ratio = pos / (pos + neg + 1)
    return 1 if ratio > 0.5 else 0


def max_deviation(C0, C1):
    """Max absolute entry-wise deviation, ignoring NaN."""
    diff = np.abs(C0 - C1)
    valid = ~np.isnan(diff)
    if not valid.any():
        return 0.0
    return float(np.nanmax(diff))


def frobenius_deviation(C0, C1):
    """Frobenius norm of difference, ignoring NaN."""
    diff = C0 - C1
    valid = ~np.isnan(diff)
    if not valid.any():
        return 0.0
    return float(np.sqrt(np.nansum(diff[valid] ** 2)))


def permutation_test_binary(records, y_values, n_perm, rng):
    """Permutation test for binary Y proxy."""
    y_arr = np.array(y_values)
    mask0 = y_arr == 0
    mask1 = y_arr == 1

    recs0 = [r for r, m in zip(records, mask0) if m]
    recs1 = [r for r, m in zip(records, mask1) if m]

    C0 = compute_confusion_matrix(recs0)
    C1 = compute_confusion_matrix(recs1)
    T_obs = max_deviation(C0, C1)
    frob = frobenius_deviation(C0, C1)

    T_perms = np.empty(n_perm)
    n = len(records)
    for b in range(n_perm):
        perm_y = rng.permutation(y_arr)
        pm0 = perm_y == 0
        pm1 = perm_y == 1
        pC0 = compute_confusion_matrix([records[i] for i in range(n) if pm0[i]])
        pC1 = compute_confusion_matrix([records[i] for i in range(n) if pm1[i]])
        T_perms[b] = max_deviation(pC0, pC1)

    p_value = (1 + np.sum(T_perms >= T_obs)) / (1 + n_perm)
    null_95 = float(np.percentile(T_perms, 95))
    null_mean = float(np.mean(T_perms))

    return {
        "n_y0": int(mask0.sum()),
        "n_y1": int(mask1.sum()),
        "C_y0": np.where(np.isnan(C0), None, C0).tolist(),
        "C_y1": np.where(np.isnan(C1), None, C1).tolist(),
        "max_deviation": round(T_obs, 6),
        "frobenius_deviation": round(frob, 6),
        "permutation_p_value": round(float(p_value), 6),
        "null_95pct": round(null_95, 6),
        "null_mean": round(null_mean, 6),
        "conclusion": "non-differential" if p_value > 0.05 else "differential",
    }


def permutation_test_categorical(records, y_values, n_perm, rng):
    """Permutation test for categorical Y proxy (topic)."""
    groups = sorted(set(y_values))
    group_counts = Counter(y_values)
    y_arr = np.array(y_values)

    C_per_group = {}
    for g in groups:
        recs_g = [r for r, yv in zip(records, y_values) if yv == g]
        C_per_group[g] = compute_confusion_matrix(recs_g)

    # Max pairwise deviation
    max_pw = 0.0
    for i, g1 in enumerate(groups):
        for g2 in groups[i + 1:]:
            d = max_deviation(C_per_group[g1], C_per_group[g2])
            if d > max_pw:
                max_pw = d

    # Variance-based statistic: max across (j,k) of var(C[j,k]) across groups
    C_stack = np.array([C_per_group[g] for g in groups])  # (G, K, K)
    with np.errstate(all="ignore"):
        var_per_entry = np.nanvar(C_stack, axis=0)  # (K, K)
    T_obs = float(np.nanmax(var_per_entry)) if not np.all(np.isnan(var_per_entry)) else 0.0

    T_perms = np.empty(n_perm)
    n = len(records)
    for b in range(n_perm):
        perm_y = rng.permutation(y_arr)
        pC_stack = []
        for g in groups:
            mask = perm_y == g
            pC = compute_confusion_matrix([records[i] for i in range(n) if mask[i]])
            pC_stack.append(pC)
        pC_arr = np.array(pC_stack)
        with np.errstate(all="ignore"):
            pvar = np.nanvar(pC_arr, axis=0)
        T_perms[b] = float(np.nanmax(pvar)) if not np.all(np.isnan(pvar)) else 0.0

    p_value = (1 + np.sum(T_perms >= T_obs)) / (1 + n_perm)
    null_95 = float(np.percentile(T_perms, 95))

    C_serializable = {}
    for g in groups:
        C_serializable[g] = np.where(np.isnan(C_per_group[g]), None, C_per_group[g]).tolist()

    return {
        "groups": {g: int(group_counts[g]) for g in groups},
        "C_per_group": C_serializable,
        "max_pairwise_deviation": round(max_pw, 6),
        "max_variance_statistic": round(T_obs, 6),
        "permutation_p_value": round(float(p_value), 6),
        "null_95pct": round(null_95, 6),
        "conclusion": "non-differential" if p_value > 0.05 else "differential",
    }


def run_test(n_perm):
    """Phase 2: Y-stratified permutation tests."""
    records, parse_failures = load_annotations()
    n_valid = len(records)
    n_total = n_valid + parse_failures
    print(f"Loaded {n_valid} valid annotations ({parse_failures} parse failures)")

    # Detect model from first record
    model_used = DEFAULT_MODEL
    if records and "raw_response" in records[0]:
        pass  # model name not stored in annotations; use default

    # Overall confusion matrix and accuracy
    C_overall = compute_confusion_matrix(records)
    correct = sum(1 for r in records if r["gold_label"] == r["predicted_label"])
    accuracy = correct / n_valid if n_valid > 0 else 0.0

    rng = np.random.default_rng(42)

    # Y1: text_length
    print("Testing Y1: text_length ...")
    lengths = [len(r["text"]) for r in records]
    median_len = float(np.median(lengths))
    y1 = [1 if l > median_len else 0 for l in lengths]
    res_y1 = permutation_test_binary(records, y1, n_perm, rng)
    res_y1["description"] = "len(text) > median"
    res_y1["type"] = "binary"

    # Y2: topic
    print("Testing Y2: topic ...")
    topic_counts = Counter(r["topic"] for r in records)
    threshold = 30
    big_topics = {t for t, c in topic_counts.items() if c >= threshold}
    if len(big_topics) <= 2:
        threshold = 20
        big_topics = {t for t, c in topic_counts.items() if c >= threshold}
    y2 = [r["topic"] if r["topic"] in big_topics else "other" for r in records]
    res_y2 = permutation_test_categorical(records, y2, n_perm, rng)
    res_y2["description"] = f"VAST topic field (groups with n>={threshold})"
    res_y2["type"] = "categorical"

    # Y3: sentiment
    print("Testing Y3: sentiment ...")
    y3 = [compute_sentiment_proxy(r["text"]) for r in records]
    res_y3 = permutation_test_binary(records, y3, n_perm, rng)
    res_y3["description"] = "positive/(positive+negative+1) > 0.5"
    res_y3["type"] = "binary"

    # Conclusions
    all_nondiff = all(
        res["conclusion"] == "non-differential"
        for res in [res_y1, res_y2, res_y3]
    )
    if all_nondiff:
        overall = "Non-differential misclassification supported: all three Y-stratified tests show p > 0.05"
    else:
        failing = [name for name, res in [("text_length", res_y1), ("topic", res_y2), ("sentiment", res_y3)]
                   if res["conclusion"] == "differential"]
        overall = f"Differential misclassification detected in: {', '.join(failing)}"

    results = {
        "model": model_used,
        "dataset": "VAST",
        "K": K,
        "classes": CLASS_NAMES,
        "n_samples": n_total,
        "n_valid_predictions": n_valid,
        "n_parse_failures": parse_failures,
        "overall_confusion_matrix": np.where(np.isnan(C_overall), None, C_overall).tolist(),
        "overall_accuracy": round(accuracy, 4),
        "y_proxies": {
            "text_length": res_y1,
            "topic": res_y2,
            "sentiment": res_y3,
        },
        "overall_conclusion": overall,
        "annotation_file": "nondiff_y_stratified_annotations.jsonl",
    }

    with open(RESULTS_PATH, "w") as f:
        json.dump(results, f, indent=2, default=str)

    print(f"\nResults saved to {RESULTS_PATH}")
    print(f"Overall accuracy: {accuracy:.4f}")
    print(f"Y1 text_length: p={res_y1['permutation_p_value']:.4f} → {res_y1['conclusion']}")
    print(f"Y2 topic:       p={res_y2['permutation_p_value']:.4f} → {res_y2['conclusion']}")
    print(f"Y3 sentiment:   p={res_y3['permutation_p_value']:.4f} → {res_y3['conclusion']}")
    print(f"Conclusion: {overall}")


# ── CLI ───────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="MF-2: Y-Stratified Non-Differential Misclassification Test"
    )
    parser.add_argument("--phase", required=True, choices=["annotate", "test", "all"],
                        help="Phase to run: annotate, test, or all")
    parser.add_argument("--api-key", type=str, default=None,
                        help="OpenRouter API key (required for annotate/all)")
    parser.add_argument("--model", type=str, default=DEFAULT_MODEL,
                        help=f"OpenRouter model (default: {DEFAULT_MODEL})")
    parser.add_argument("--smoke", action="store_true",
                        help="Annotate only 5 samples for testing")
    parser.add_argument("--permutations", type=int, default=10000,
                        help="Number of permutations for test phase (default: 10000)")
    args = parser.parse_args()

    if args.phase in ("annotate", "all") and not args.api_key:
        parser.error("--api-key is required for annotate/all phases")

    if args.phase in ("annotate", "all"):
        run_annotate(args.api_key, args.model, args.smoke)

    if args.phase in ("test", "all"):
        run_test(args.permutations)


if __name__ == "__main__":
    main()
