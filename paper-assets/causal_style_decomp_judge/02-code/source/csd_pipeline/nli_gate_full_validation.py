"""NLI Gate Full GPT-4o Validation (W-MF1)

Evaluates all ~200 counterfactual pairs (formality + verbosity) with GPT-4o
to validate NLI gate pass/fail decisions.

Usage:
    cd /root/causal_style_decomp_judge
    python3 csd_pipeline/nli_gate_full_validation.py
"""

import json
import os
import sys
import time
from collections import Counter

import numpy as np
from openai import OpenAI

NLI_THRESHOLD = 0.90
API_BASE = "http://47.94.22.126/v1"
API_KEY = "[REDACTED]"
MODEL = "gpt-4o"

ROOT = "/root/causal_style_decomp_judge"
DATA_FILES = {
    "formality": f"{ROOT}/data/verified_32b.jsonl",
    "verbosity": f"{ROOT}/data/verified_verbosity.jsonl",
}
OUTPUT_PATH = f"{ROOT}/data/nli_gate_full_validation.json"
SPOTCHECK_PATH = f"{ROOT}/artifacts/reanalysis_outputs/nli_gate_gpt4o_spotcheck.json"

PROMPT_TEMPLATE = """\
Given the original text and a rewritten version, does the rewritten text \
preserve the same meaning and factual content? Only the writing style should \
differ.

## Original text
{original}

## Rewritten text
{rewritten}

First, state your verdict: **Preserved** or **Not Preserved**.
Then give a confidence score from 1 (very uncertain) to 5 (very certain).
Finally, explain in 1-2 sentences.

Format your answer exactly as:
Verdict: <Preserved or Not Preserved>
Confidence: <1-5>
Explanation: <your explanation>"""


def load_pairs(path, axis):
    pairs = []
    with open(path) as f:
        for line in f:
            if not line.strip():
                continue
            rec = json.loads(line)
            rid = rec.get("id", "unknown")
            if "nli_cf" not in rec or "counterfactual_text" not in rec:
                continue
            pairs.append({
                "id": f"{rid}_cf",
                "axis": axis,
                "original_text": rec["original_text"],
                "rewritten_text": rec["counterfactual_text"],
                "nli_score": rec["nli_cf"],
                "nli_pass": rec["nli_cf"] >= NLI_THRESHOLD,
            })
    return pairs


def parse_response(text):
    verdict = None
    confidence = None
    explanation = ""
    for line in text.strip().split("\n"):
        line_lower = line.strip().lower()
        if line_lower.startswith("verdict:"):
            v = line.split(":", 1)[1].strip().lower()
            if "not preserved" in v:
                verdict = "Not Preserved"
            elif "preserved" in v:
                verdict = "Preserved"
        elif line_lower.startswith("confidence:"):
            try:
                confidence = int(line.split(":", 1)[1].strip().split()[0])
            except (ValueError, IndexError):
                confidence = None
        elif line_lower.startswith("explanation:"):
            explanation = line.split(":", 1)[1].strip()
    if verdict is None:
        t = text.lower()
        if "not preserved" in t:
            verdict = "Not Preserved"
        elif "preserved" in t:
            verdict = "Preserved"
    return verdict, confidence, explanation


def evaluate_pair(client, pair):
    prompt = PROMPT_TEMPLATE.format(
        original=pair["original_text"],
        rewritten=pair["rewritten_text"],
    )
    try:
        resp = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300,
            temperature=0.0,
        )
        answer = resp.choices[0].message.content.strip()
    except Exception as e:
        print(f"  API ERROR {pair['id']}: {e}")
        return None, None, str(e)
    verdict, confidence, explanation = parse_response(answer)
    return verdict, confidence, answer


def cohens_kappa(y1, y2):
    n = len(y1)
    if n == 0:
        return float("nan")
    agree = sum(a == b for a, b in zip(y1, y2))
    p_o = agree / n
    c1 = Counter(y1)
    c2 = Counter(y2)
    labels = set(y1) | set(y2)
    p_e = sum((c1[l] / n) * (c2[l] / n) for l in labels)
    if p_e == 1.0:
        return 1.0 if p_o == 1.0 else 0.0
    return (p_o - p_e) / (1.0 - p_e)


def compute_metrics(results):
    valid = [r for r in results if r["gpt4o_pass"] is not None]
    n = len(valid)
    if n == 0:
        return None

    nli_labels = [1 if r["nli_pass"] else 0 for r in valid]
    gpt_labels = [1 if r["gpt4o_pass"] else 0 for r in valid]

    agreement = sum(a == b for a, b in zip(nli_labels, gpt_labels)) / n
    kappa = cohens_kappa(nli_labels, gpt_labels)

    tp = sum(1 for r in valid if r["nli_pass"] and r["gpt4o_pass"])
    fp = sum(1 for r in valid if r["nli_pass"] and not r["gpt4o_pass"])
    fn = sum(1 for r in valid if not r["nli_pass"] and r["gpt4o_pass"])
    tn = sum(1 for r in valid if not r["nli_pass"] and not r["gpt4o_pass"])

    n_pass = tp + fp
    n_fail = tn + fn
    pass_precision = tp / n_pass if n_pass > 0 else None
    fail_recall = tn / n_fail if n_fail > 0 else None
    base_rate_pass = n_pass / n

    return {
        "n": n,
        "agreement": round(agreement, 4),
        "kappa": round(kappa, 4),
        "base_rate_pass": round(base_rate_pass, 4),
        "pass_precision": round(pass_precision, 4) if pass_precision is not None else None,
        "fail_recall": round(fail_recall, 4) if fail_recall is not None else None,
        "confusion": {"tp": tp, "fp": fp, "tn": tn, "fn": fn},
    }


def load_spotcheck_cache():
    """Load spot-check results that can be reused (same file + same pair ID)."""
    if not os.path.exists(SPOTCHECK_PATH):
        return {}
    with open(SPOTCHECK_PATH) as f:
        data = json.load(f)
    cache = {}
    for r in data.get("results", []):
        if r.get("gpt4o_verdict") and r.get("axis") in ("formality", "verbosity"):
            cache[r["id"]] = r
    return cache


def main():
    all_pairs = []
    for axis, path in DATA_FILES.items():
        if not os.path.exists(path):
            print(f"WARNING: {path} not found, skipping")
            continue
        pairs = load_pairs(path, axis)
        n_pass = sum(1 for p in pairs if p["nli_pass"])
        print(f"{axis}: {len(pairs)} pairs ({n_pass} pass, {len(pairs) - n_pass} fail)")
        all_pairs.extend(pairs)

    print(f"Total: {len(all_pairs)} pairs\n")

    # Load spot-check cache (verbosity pairs from same file may overlap)
    sc_cache = load_spotcheck_cache()
    reused = 0

    client = OpenAI(base_url=API_BASE, api_key=[REDACTED]
    results = []
    t0 = time.time()

    for i, pair in enumerate(all_pairs):
        # Check spot-check cache
        if pair["id"] in sc_cache:
            cached = sc_cache[pair["id"]]
            verdict = cached["gpt4o_verdict"]
            confidence = cached.get("gpt4o_confidence")
            raw = cached.get("gpt4o_raw", "")
            reused += 1
            src = "cache"
        else:
            verdict, confidence, raw = evaluate_pair(client, pair)
            src = "api"
            time.sleep(1.0)

        gpt4o_pass = verdict == "Preserved" if verdict else None
        entry = {
            "id": pair["id"],
            "axis": pair["axis"],
            "nli_score": pair["nli_score"],
            "nli_pass": pair["nli_pass"],
            "gpt4o_verdict": verdict,
            "gpt4o_confidence": confidence,
            "gpt4o_pass": gpt4o_pass,
            "agree": (pair["nli_pass"] == gpt4o_pass) if gpt4o_pass is not None else None,
            "gpt4o_raw": raw,
        }
        results.append(entry)

        tag = "AGREE" if entry["agree"] else ("DISAGREE" if entry["agree"] is not None else "ERROR")
        print(f"  [{i+1}/{len(all_pairs)}] {pair['id']} "
              f"nli={pair['nli_score']:.4f}({'P' if pair['nli_pass'] else 'F'}) "
              f"gpt4o={verdict} [{tag}] ({src})")

    elapsed = time.time() - t0
    print(f"\nDone in {elapsed:.0f}s. Reused {reused} from spot-check cache.")

    # Compute per-axis and overall metrics
    per_axis = {}
    for axis in DATA_FILES:
        axis_results = [r for r in results if r["axis"] == axis]
        metrics = compute_metrics(axis_results)
        if metrics:
            per_axis[axis] = metrics
            print(f"\n{axis} (n={metrics['n']}): "
                  f"agreement={metrics['agreement']}, kappa={metrics['kappa']}, "
                  f"pass_prec={metrics['pass_precision']}, fail_recall={metrics['fail_recall']}, "
                  f"confusion={metrics['confusion']}")

    overall = compute_metrics(results)
    print(f"\nOverall (n={overall['n']}): "
          f"agreement={overall['agreement']}, kappa={overall['kappa']}, "
          f"pass_prec={overall['pass_precision']}, fail_recall={overall['fail_recall']}")

    # Compare with spot-check
    vs_spotcheck = {
        "spotcheck_agreement": 0.65,
        "full_agreement": overall["agreement"],
        "note": (
            f"Full validation agreement ({overall['agreement']:.4f}) vs "
            f"spot-check (0.6500): delta={overall['agreement'] - 0.65:+.4f}. "
            f"Spot-check sampled 50 pass + 50 fail (balanced); full validation "
            f"uses natural prevalence (~87% pass)."
        ),
    }

    output = {
        "total_evaluated": overall["n"],
        "per_axis": per_axis,
        "overall": {k: v for k, v in overall.items() if k != "confusion"},
        "vs_spotcheck": vs_spotcheck,
    }
    # Add confusion to overall
    output["overall"]["confusion"] = overall.get("confusion")
    # Remove individual results from top-level output (keep it clean)
    # but save full results in a separate key
    output["individual_results"] = results

    with open(OUTPUT_PATH, "w") as f:
        json.dump(output, f, indent=2, default=str)
    print(f"\nSaved to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
