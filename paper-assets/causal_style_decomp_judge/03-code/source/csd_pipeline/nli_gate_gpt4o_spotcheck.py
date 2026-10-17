"""GPT-4o independent spot-check of NLI gate pass/fail decisions.

Samples 50 NLI-pass and 50 NLI-fail pairs across formality/verbosity/register
axes, asks GPT-4o whether meaning is preserved, then computes inter-annotator
agreement (Cohen's kappa with bootstrap 95% CI).

Usage:
    source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
    cd /root/causal_style_decomp_judge
    python3 csd_pipeline/nli_gate_gpt4o_spotcheck.py

API: http://47.94.22.126/v1 (GPT-4o compatible)
"""

import json
import os
import random
import sys
import time
from collections import Counter, defaultdict

import numpy as np
from openai import OpenAI

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
SEED = 42
N_PASS = 50
N_FAIL = 50
NLI_THRESHOLD = 0.90

API_BASE = "http://47.94.22.126/v1"
API_KEY = "[REDACTED]"
MODEL = "gpt-4o"

ROOT = "/root/causal_style_decomp_judge"
DATA_FILES = {
    "formality": f"{ROOT}/data/verified_scaled_formality.jsonl",
    "verbosity": f"{ROOT}/data/verified_verbosity.jsonl",
    "register": f"{ROOT}/data/verified_register.jsonl",
}
OUTPUT_PATH = f"{ROOT}/artifacts/reanalysis_outputs/nli_gate_gpt4o_spotcheck.json"

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


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------
def load_pairs(path, axis):
    """Load a verified JSONL file and flatten into individual (orig, rewrite) pairs."""
    pairs = []
    with open(path) as f:
        for line in f:
            if not line.strip():
                continue
            rec = json.loads(line)
            rid = rec.get("id", "unknown")
            orig = rec["original_text"]

            # counterfactual pair
            if "nli_cf" in rec:
                pairs.append({
                    "id": f"{rid}_cf",
                    "axis": axis,
                    "pair_type": "cf",
                    "original_text": orig,
                    "rewritten_text": rec["counterfactual_text"],
                    "nli_score": rec["nli_cf"],
                    "nli_pass": rec["nli_cf"] >= NLI_THRESHOLD,
                })

            # double-rewrite pair
            if "nli_dr" in rec:
                pairs.append({
                    "id": f"{rid}_dr",
                    "axis": axis,
                    "pair_type": "dr",
                    "original_text": orig,
                    "rewritten_text": rec["double_rewrite_text"],
                    "nli_score": rec["nli_dr"],
                    "nli_pass": rec["nli_dr"] >= NLI_THRESHOLD,
                })
    return pairs


def load_all_pairs():
    """Load pairs from all axes and split into pass/fail."""
    all_pairs = []
    for axis, path in DATA_FILES.items():
        if not os.path.exists(path):
            print(f"WARNING: {path} not found, skipping")
            continue
        pairs = load_pairs(path, axis)
        print(f"  {axis}: {len(pairs)} pairs "
              f"(pass={sum(1 for p in pairs if p['nli_pass'])}, "
              f"fail={sum(1 for p in pairs if not p['nli_pass'])})")
        all_pairs.extend(pairs)

    pass_pairs = [p for p in all_pairs if p["nli_pass"]]
    fail_pairs = [p for p in all_pairs if not p["nli_pass"]]
    return pass_pairs, fail_pairs


# ---------------------------------------------------------------------------
# GPT-4o evaluation
# ---------------------------------------------------------------------------
def parse_response(text):
    """Parse GPT-4o response into verdict and confidence."""
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

    # fallback: scan entire text
    if verdict is None:
        t = text.lower()
        if "not preserved" in t:
            verdict = "Not Preserved"
        elif "preserved" in t:
            verdict = "Preserved"

    return verdict, confidence, explanation


def evaluate_pair(client, pair):
    """Send a single pair to GPT-4o for evaluation."""
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
        print(f"    API ERROR for {pair['id']}: {e}")
        return None, None, str(e)

    verdict, confidence, explanation = parse_response(answer)
    return verdict, confidence, f"{answer}"


# ---------------------------------------------------------------------------
# Cohen's kappa
# ---------------------------------------------------------------------------
def cohens_kappa(y1, y2):
    """Compute Cohen's kappa for two binary label lists."""
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


def bootstrap_kappa_ci(y1, y2, n_boot=10000, alpha=0.05):
    """Bootstrap 95% CI for Cohen's kappa."""
    rng = np.random.RandomState(SEED)
    n = len(y1)
    y1 = np.array(y1)
    y2 = np.array(y2)
    kappas = []
    for _ in range(n_boot):
        idx = rng.randint(0, n, size=n)
        k = cohens_kappa(y1[idx].tolist(), y2[idx].tolist())
        if not np.isnan(k):
            kappas.append(k)
    if not kappas:
        return float("nan"), float("nan")
    lo = np.percentile(kappas, 100 * alpha / 2)
    hi = np.percentile(kappas, 100 * (1 - alpha / 2))
    return float(lo), float(hi)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print("=" * 60)
    print("  NLI Gate GPT-4o Independent Spot-Check")
    print("=" * 60)

    # Load data
    print("\nLoading data...")
    pass_pairs, fail_pairs = load_all_pairs()
    print(f"\nTotal: {len(pass_pairs)} pass pairs, {len(fail_pairs)} fail pairs")

    # Sample
    random.seed(SEED)
    n_pass_sample = min(N_PASS, len(pass_pairs))
    n_fail_sample = min(N_FAIL, len(fail_pairs))
    pass_sample = random.sample(pass_pairs, n_pass_sample)
    fail_sample = random.sample(fail_pairs, n_fail_sample)
    samples = pass_sample + fail_sample
    random.shuffle(samples)

    print(f"Sampled: {n_pass_sample} pass + {n_fail_sample} fail = {len(samples)} total")

    # Evaluate
    client = OpenAI(base_url=API_BASE, api_key=[REDACTED]
    results = []
    for i, pair in enumerate(samples):
        verdict, confidence, raw = evaluate_pair(client, pair)
        gpt4o_pass = verdict == "Preserved" if verdict else None

        entry = {
            "id": pair["id"],
            "axis": pair["axis"],
            "pair_type": pair["pair_type"],
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
        print(f"  [{i+1}/{len(samples)}] {pair['id']} "
              f"nli={pair['nli_score']:.4f}({'P' if pair['nli_pass'] else 'F'}) "
              f"gpt4o={verdict} conf={confidence} [{tag}]")

        if (i + 1) % 20 == 0:
            time.sleep(1)

    # Filter valid results
    valid = [r for r in results if r["agree"] is not None]
    n_valid = len(valid)
    if n_valid == 0:
        print("\nERROR: No valid results")
        sys.exit(1)

    # ---- Overall metrics ----
    overall_agree = sum(1 for r in valid if r["agree"])
    nli_labels = [1 if r["nli_pass"] else 0 for r in valid]
    gpt_labels = [1 if r["gpt4o_pass"] else 0 for r in valid]
    kappa = cohens_kappa(nli_labels, gpt_labels)
    ci_lo, ci_hi = bootstrap_kappa_ci(nli_labels, gpt_labels)

    # ---- Per-group metrics ----
    pass_valid = [r for r in valid if r["nli_pass"]]
    fail_valid = [r for r in valid if not r["nli_pass"]]
    pass_agree = sum(1 for r in pass_valid if r["agree"])
    fail_agree = sum(1 for r in fail_valid if r["agree"])

    # ---- Per-axis metrics ----
    axis_stats = {}
    for axis in ["formality", "verbosity", "register"]:
        ax = [r for r in valid if r["axis"] == axis]
        if ax:
            ax_agree = sum(1 for r in ax if r["agree"])
            ax_nli = [1 if r["nli_pass"] else 0 for r in ax]
            ax_gpt = [1 if r["gpt4o_pass"] else 0 for r in ax]
            ax_kappa = cohens_kappa(ax_nli, ax_gpt)
            axis_stats[axis] = {
                "n": len(ax),
                "agreement": ax_agree / len(ax),
                "kappa": ax_kappa,
            }

    # ---- Disagreement analysis ----
    disagree = [r for r in valid if not r["agree"]]
    disagree_patterns = defaultdict(list)
    for r in disagree:
        pattern = f"NLI={'pass' if r['nli_pass'] else 'fail'}_GPT={'pass' if r['gpt4o_pass'] else 'fail'}"
        disagree_patterns[pattern].append({
            "id": r["id"],
            "axis": r["axis"],
            "nli_score": r["nli_score"],
            "gpt4o_confidence": r["gpt4o_confidence"],
        })

    # ---- Print summary ----
    print(f"\n{'=' * 60}")
    print(f"  RESULTS (N={n_valid})")
    print(f"{'=' * 60}")
    print(f"  Total samples: {n_valid} (pass: {len(pass_valid)}, fail: {len(fail_valid)})")
    print(f"  Overall agreement: {overall_agree}/{n_valid} ({overall_agree/n_valid*100:.1f}%)")
    print(f"  Cohen's kappa: {kappa:.4f} (95% CI: [{ci_lo:.4f}, {ci_hi:.4f}])")
    print(f"  Pass group agreement: {pass_agree}/{len(pass_valid)} "
          f"({pass_agree/len(pass_valid)*100:.1f}%)" if pass_valid else "")
    print(f"  Fail group agreement: {fail_agree}/{len(fail_valid)} "
          f"({fail_agree/len(fail_valid)*100:.1f}%)" if fail_valid else "")

    print(f"\n  Per-axis breakdown:")
    for axis, stats in axis_stats.items():
        print(f"    {axis}: agreement={stats['agreement']*100:.1f}% "
              f"kappa={stats['kappa']:.4f} (n={stats['n']})")

    if disagree_patterns:
        print(f"\n  Disagreement patterns ({len(disagree)} total):")
        for pattern, items in sorted(disagree_patterns.items()):
            print(f"    {pattern}: {len(items)} cases")
            for item in items[:3]:
                print(f"      - {item['id']} nli={item['nli_score']:.4f} "
                      f"gpt_conf={item['gpt4o_confidence']}")

    # ---- Confidence distribution ----
    confs = [r["gpt4o_confidence"] for r in valid if r["gpt4o_confidence"] is not None]
    if confs:
        print(f"\n  GPT-4o confidence: mean={np.mean(confs):.2f}, "
              f"median={np.median(confs):.0f}, "
              f"distribution={dict(Counter(confs))}")

    # ---- Save ----
    summary = {
        "n_total": n_valid,
        "n_pass": len(pass_valid),
        "n_fail": len(fail_valid),
        "overall_agreement": overall_agree / n_valid,
        "cohens_kappa": kappa,
        "kappa_ci_95": [ci_lo, ci_hi],
        "pass_group_agreement": pass_agree / len(pass_valid) if pass_valid else None,
        "fail_group_agreement": fail_agree / len(fail_valid) if fail_valid else None,
        "per_axis": axis_stats,
        "disagreement_patterns": {k: len(v) for k, v in disagree_patterns.items()},
        "gpt4o_confidence_mean": float(np.mean(confs)) if confs else None,
    }

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        json.dump({"summary": summary, "results": results}, f, indent=2, default=str)
    print(f"\n  Saved to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
