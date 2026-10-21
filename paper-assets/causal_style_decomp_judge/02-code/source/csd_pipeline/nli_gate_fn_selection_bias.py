"""NLI Gate False-Negative Selection Bias Analysis.

Tests whether the NLI gate (threshold=0.90) systematically filters pairs
with larger style changes, which would bias measured effect estimates
downward. Compares style-change magnitude metrics between pass/fail groups.
"""

import json
from collections import defaultdict
from pathlib import Path

import Levenshtein
import numpy as np
import textstat
from scipy import stats

SEED = 42
NLI_THRESHOLD = 0.90
DATA_DIR = Path("/root/causal_style_decomp_judge/data")

AXES = {
    "formality": {
        "file": DATA_DIR / "verified_scaled_formality.jsonl",
        "style_field": "original_formality",
    },
    "verbosity": {
        "file": DATA_DIR / "verified_verbosity.jsonl",
        "style_field": "original_verbosity",
    },
}


def load_records(path):
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]


def tokenize(text):
    return text.lower().split()


def compute_style_metrics(original, rewrite):
    """Compute surface-level style change magnitude metrics between two texts."""
    max_len = max(len(original), len(rewrite), 1)
    norm_lev = Levenshtein.distance(original, rewrite) / max_len

    char_diff = abs(len(rewrite) - len(original))
    char_ratio = len(rewrite) / max(len(original), 1)

    orig_tokens = tokenize(original)
    rew_tokens = tokenize(rewrite)
    token_diff = abs(len(rew_tokens) - len(orig_tokens))
    token_ratio = len(rew_tokens) / max(len(orig_tokens), 1)

    orig_set = set(orig_tokens)
    rew_set = set(rew_tokens)
    union = orig_set | rew_set
    jaccard = len(orig_set & rew_set) / max(len(union), 1)

    lev_ratio = Levenshtein.ratio(original, rewrite)

    try:
        fre_diff = abs(textstat.flesch_reading_ease(rewrite) - textstat.flesch_reading_ease(original))
    except Exception:
        fre_diff = float('nan')

    try:
        sent_diff = abs(textstat.sentence_count(rewrite) - textstat.sentence_count(original))
    except Exception:
        sent_diff = float('nan')

    return {
        "norm_levenshtein": norm_lev,
        "char_diff": char_diff,
        "char_ratio": char_ratio,
        "token_diff": token_diff,
        "token_ratio": token_ratio,
        "jaccard_overlap": jaccard,
        "levenshtein_ratio": lev_ratio,
        "flesch_diff": fre_diff,
        "sentence_diff": sent_diff,
    }


def cliffs_delta(x, y):
    """Cliff's delta effect size (non-parametric)."""
    nx, ny = len(x), len(y)
    if nx == 0 or ny == 0:
        return float('nan')
    more = less = 0
    for xi in x:
        for yi in y:
            if xi > yi:
                more += 1
            elif xi < yi:
                less += 1
    return (more - less) / (nx * ny)


def interpret_cliffs_delta(d):
    d = abs(d)
    if d < 0.147:
        return "negligible"
    elif d < 0.33:
        return "small"
    elif d < 0.474:
        return "medium"
    return "large"


def analyze_axis(axis_name, config):
    """Run selection bias analysis for one style axis."""
    records = load_records(config["file"])
    n_total = len(records)

    for r in records:
        r["gate_pass"] = r["passed_cf"] and r["passed_dr"]

    pass_recs = [r for r in records if r["gate_pass"]]
    fail_recs = [r for r in records if not r["gate_pass"]]
    n_pass, n_fail = len(pass_recs), len(fail_recs)

    print(f"\n{'='*70}")
    print(f"  AXIS: {axis_name.upper()}")
    print(f"  File: {config['file'].name}")
    print(f"  N total={n_total}  pass={n_pass} ({100*n_pass/n_total:.1f}%)  fail={n_fail} ({100*n_fail/n_total:.1f}%)")
    print(f"{'='*70}")

    cf_fail = sum(1 for r in records if not r["passed_cf"])
    dr_fail = sum(1 for r in records if not r["passed_dr"])
    print(f"  Failure breakdown: cf_fail={cf_fail}, dr_fail={dr_fail}")

    print(f"\n  NLI scores (cf): pass={np.mean([r['nli_cf'] for r in pass_recs]):.4f}  fail={np.mean([r['nli_cf'] for r in fail_recs]):.4f}")
    print(f"  NLI scores (dr): pass={np.mean([r['nli_dr'] for r in pass_recs]):.4f}  fail={np.mean([r['nli_dr'] for r in fail_recs]):.4f}")

    pass_metrics = defaultdict(list)
    fail_metrics = defaultdict(list)

    for r in pass_recs:
        m = compute_style_metrics(r["original_text"], r["counterfactual_text"])
        for k, v in m.items():
            pass_metrics[k].append(v)

    for r in fail_recs:
        m = compute_style_metrics(r["original_text"], r["counterfactual_text"])
        for k, v in m.items():
            fail_metrics[k].append(v)

    metric_names = list(compute_style_metrics("a", "b").keys())

    hdr = f"  {'Metric':<22} {'Pass (mean+/-std)':<22} {'Fail (mean+/-std)':<22} {'U p-val':<12} {'Cliff d':<12} {'Size':<12}"
    print(f"\n{hdr}")
    print(f"  {'-'*100}")

    bias_detected = False
    for metric in metric_names:
        p_vals = np.array(pass_metrics[metric], dtype=float)
        f_vals = np.array(fail_metrics[metric], dtype=float)
        p_vals = p_vals[~np.isnan(p_vals)]
        f_vals = f_vals[~np.isnan(f_vals)]
        if len(p_vals) == 0 or len(f_vals) == 0:
            continue

        p_mean, p_std = np.mean(p_vals), np.std(p_vals)
        f_mean, f_std = np.mean(f_vals), np.std(f_vals)

        try:
            _, p_value = stats.mannwhitneyu(p_vals, f_vals, alternative="two-sided")
        except ValueError:
            p_value = float('nan')

        cd = cliffs_delta(f_vals.tolist(), p_vals.tolist())
        cd_interp = interpret_cliffs_delta(cd)
        if p_value < 0.05:
            bias_detected = True

        sig = " *" if p_value < 0.05 else ""
        print(f"  {metric:<22} {p_mean:.4f}+/-{p_std:.4f}     {f_mean:.4f}+/-{f_std:.4f}     {p_value:<12.4f} {cd:<+12.4f} {cd_interp}{sig}")

    lev_p = np.array(pass_metrics["norm_levenshtein"])
    lev_f = np.array(fail_metrics["norm_levenshtein"])
    direction = "LARGER" if np.mean(lev_f) > np.mean(lev_p) else "SMALLER"

    try:
        _, p_lev = stats.mannwhitneyu(lev_p, lev_f, alternative="two-sided")
    except ValueError:
        p_lev = 1.0

    print(f"\n  --- Direction ---")
    print(f"  Fail group edit distance is {direction} than pass group (p={p_lev:.4f})")
    if direction == "LARGER" and p_lev < 0.05:
        print(f"  -> CONSERVATIVE bias: gate filters larger changes -> measured effects are lower bounds")
    elif p_lev >= 0.05:
        print(f"  -> No significant selection bias on style change magnitude")
    else:
        print(f"  -> Gate filters SMALLER changes -> could inflate measured effects")

    print(f"\n  --- Double-Rewrite (original vs double_rewrite) ---")
    dr_p_lev = [Levenshtein.distance(r["original_text"], r["double_rewrite_text"]) / max(len(r["original_text"]), len(r["double_rewrite_text"]), 1) for r in pass_recs]
    dr_f_lev = [Levenshtein.distance(r["original_text"], r["double_rewrite_text"]) / max(len(r["original_text"]), len(r["double_rewrite_text"]), 1) for r in fail_recs]
    dr_p_arr = np.array(dr_p_lev)
    dr_f_arr = np.array(dr_f_lev)
    try:
        _, dr_p = stats.mannwhitneyu(dr_p_arr, dr_f_arr, alternative="two-sided")
    except ValueError:
        dr_p = float('nan')
    dr_cd = cliffs_delta(dr_f_arr.tolist(), dr_p_arr.tolist())
    print(f"  Pass: {np.mean(dr_p_arr):.4f}+/-{np.std(dr_p_arr):.4f}  Fail: {np.mean(dr_f_arr):.4f}+/-{np.std(dr_f_arr):.4f}")
    print(f"  Mann-Whitney p={dr_p:.4f}, Cliff's d={dr_cd:+.4f} ({interpret_cliffs_delta(dr_cd)})")

    return bias_detected


def main():
    np.random.seed(SEED)
    print("NLI Gate Selection Bias Analysis")
    print(f"NLI threshold: {NLI_THRESHOLD}")
    print(f"Gate: passed_cf AND passed_dr")

    any_bias = False
    for axis_name, config in AXES.items():
        any_bias |= analyze_axis(axis_name, config)

    print(f"\n{'='*70}")
    print(f"  OVERALL CONCLUSION")
    print(f"{'='*70}")
    if any_bias:
        print("  Some metrics show significant pass/fail differences.")
        print("  If fail group has LARGER changes -> conservative (lower bounds).")
    else:
        print("  No significant selection bias across either axis.")
        print("  NLI gate does not systematically filter by style change magnitude.")


if __name__ == "__main__":
    main()
