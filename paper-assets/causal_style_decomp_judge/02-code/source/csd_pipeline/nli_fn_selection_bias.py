"""NLI gate false-negative selection bias analysis.

Compares style-change magnitude between NLI-pass and NLI-fail pairs
to test whether the gate systematically filters pairs with larger
style changes, which would bias measured effects downward.
"""

import json
from collections import defaultdict
from pathlib import Path

import Levenshtein
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
from scipy import stats
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

SEED = 42
NLI_THRESHOLD = 0.90
DATA_DIR = Path("/root/causal_style_decomp_judge/data")
OUT_DIR = Path("/root/causal_style_decomp_judge/artifacts/nli_fn_bias")

AXES = {
    "formality": {
        "file": DATA_DIR / "verified_scaled_formality.jsonl",
    },
    "verbosity": {
        "file": DATA_DIR / "verified_verbosity.jsonl",
    },
    "register": {
        "file": DATA_DIR / "verified_register.jsonl",
    },
}

METRICS = [
    ("norm_edit_dist", "Norm. Edit Distance", True),
    ("char_diff_abs", "Char Count Diff (abs)", True),
    ("char_diff_rel", "Char Count Diff (rel)", True),
    ("token_diff_abs", "Token Count Diff (abs)", True),
    ("token_diff_rel", "Token Count Diff (rel)", True),
    ("bleu", "BLEU Score", False),
    ("tfidf_cosine", "TF-IDF Cosine Sim", False),
]


def load_records(path):
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]


def tokenize(text):
    return text.lower().split()


def compute_bleu(reference, hypothesis):
    """Sentence-level BLEU with smoothing."""
    ref_tokens = tokenize(reference)
    hyp_tokens = tokenize(hypothesis)
    if len(ref_tokens) == 0 or len(hyp_tokens) == 0:
        return 0.0
    smoothing = SmoothingFunction().method1
    return sentence_bleu([ref_tokens], hyp_tokens, smoothing_function=smoothing)


def compute_tfidf_cosine(text_a, text_b):
    """TF-IDF cosine similarity between two texts."""
    vectorizer = TfidfVectorizer()
    try:
        tfidf = vectorizer.fit_transform([text_a, text_b])
        return cosine_similarity(tfidf[0:1], tfidf[1:2])[0, 0]
    except ValueError:
        return float("nan")


def compute_metrics(original, rewrite):
    """Compute style-change magnitude metrics between original and rewrite."""
    max_len = max(len(original), len(rewrite), 1)
    norm_edit = Levenshtein.distance(original, rewrite) / max_len

    char_diff_abs = abs(len(rewrite) - len(original))
    char_diff_rel = char_diff_abs / max(len(original), 1)

    orig_tokens = tokenize(original)
    rew_tokens = tokenize(rewrite)
    token_diff_abs = abs(len(rew_tokens) - len(orig_tokens))
    token_diff_rel = token_diff_abs / max(len(orig_tokens), 1)

    bleu = compute_bleu(original, rewrite)
    tfidf_cos = compute_tfidf_cosine(original, rewrite)

    return {
        "norm_edit_dist": norm_edit,
        "char_diff_abs": float(char_diff_abs),
        "char_diff_rel": char_diff_rel,
        "token_diff_abs": float(token_diff_abs),
        "token_diff_rel": token_diff_rel,
        "bleu": bleu,
        "tfidf_cosine": tfidf_cos,
    }


def cohens_d(x, y):
    """Cohen's d effect size."""
    nx, ny = len(x), len(y)
    if nx < 2 or ny < 2:
        return float("nan")
    pooled_std = np.sqrt(
        ((nx - 1) * np.var(x, ddof=1) + (ny - 1) * np.var(y, ddof=1))
        / (nx + ny - 2)
    )
    if pooled_std == 0:
        return float("nan")
    return (np.mean(x) - np.mean(y)) / pooled_std


def interpret_d(d):
    d = abs(d)
    if d < 0.2:
        return "negligible"
    elif d < 0.5:
        return "small"
    elif d < 0.8:
        return "medium"
    return "large"


def analyze_axis(axis_name, config):
    """Run selection bias analysis for one style axis."""
    records = load_records(config["file"])
    n_total = len(records)

    pass_recs = [r for r in records if r["passed_cf"] and r["passed_dr"]]
    fail_recs = [r for r in records if not (r["passed_cf"] and r["passed_dr"])]
    n_pass, n_fail = len(pass_recs), len(fail_recs)

    print(f"\n{'='*78}")
    print(f"  AXIS: {axis_name.upper()}")
    print(f"  File: {config['file'].name}")
    print(f"  N total={n_total}  pass={n_pass} ({100*n_pass/max(n_total,1):.1f}%)"
          f"  fail={n_fail} ({100*n_fail/max(n_total,1):.1f}%)")
    print(f"{'='*78}")

    cf_fail = sum(1 for r in records if not r["passed_cf"])
    dr_fail = sum(1 for r in records if not r["passed_dr"])
    print(f"  Failure breakdown: cf_fail={cf_fail}, dr_fail={dr_fail}")

    if n_fail == 0:
        print("  No fail samples — skipping.")
        return None

    pass_metrics = defaultdict(list)
    fail_metrics = defaultdict(list)

    for r in pass_recs:
        m = compute_metrics(r["original_text"], r["counterfactual_text"])
        for k, v in m.items():
            pass_metrics[k].append(v)

    for r in fail_recs:
        m = compute_metrics(r["original_text"], r["counterfactual_text"])
        for k, v in m.items():
            fail_metrics[k].append(v)

    hdr = (f"  {'Metric':<24} {'Pass (mean±std)':<22} {'Fail (mean±std)':<22}"
           f" {'U p-val':<10} {'Cohen d':<10} {'Size':<12} {'Direction'}")
    print(f"\n{hdr}")
    print(f"  {'-'*110}")

    results = []
    for key, label, higher_means_larger in METRICS:
        p_vals = np.array(pass_metrics[key], dtype=float)
        f_vals = np.array(fail_metrics[key], dtype=float)
        p_vals = p_vals[~np.isnan(p_vals)]
        f_vals = f_vals[~np.isnan(f_vals)]
        if len(p_vals) == 0 or len(f_vals) == 0:
            continue

        p_mean, p_std = np.mean(p_vals), np.std(p_vals, ddof=1)
        f_mean, f_std = np.mean(f_vals), np.std(f_vals, ddof=1)

        try:
            _, p_value = stats.mannwhitneyu(p_vals, f_vals, alternative="two-sided")
        except ValueError:
            p_value = float("nan")

        d = cohens_d(f_vals, p_vals)
        d_interp = interpret_d(d)

        if higher_means_larger:
            direction = "fail>pass" if f_mean > p_mean else "pass>fail"
        else:
            direction = "fail<pass" if f_mean < p_mean else "pass<fail"

        sig = " *" if p_value < 0.05 else ""
        print(f"  {label:<24} {p_mean:.4f}±{p_std:.4f}      "
              f"{f_mean:.4f}±{f_std:.4f}      "
              f"{p_value:<10.4f} {d:<+10.3f} {d_interp:<12} {direction}{sig}")

        results.append({
            "metric": label,
            "key": key,
            "pass_vals": p_vals,
            "fail_vals": f_vals,
            "p_value": p_value,
            "cohens_d": d,
            "direction": direction,
            "higher_means_larger": higher_means_larger,
        })

    sig_count = sum(1 for r in results if r["p_value"] < 0.05)
    conservative = any(
        r["p_value"] < 0.05
        and (
            (r["higher_means_larger"] and np.mean(r["fail_vals"]) > np.mean(r["pass_vals"]))
            or (not r["higher_means_larger"] and np.mean(r["fail_vals"]) < np.mean(r["pass_vals"]))
        )
        for r in results
    )

    print(f"\n  Significant metrics: {sig_count}/{len(results)}")
    if n_fail < 20:
        print(f"  ⚠ Low fail sample size (n={n_fail}): limited statistical power.")
    if conservative:
        print("  → CONSERVATIVE bias: gate filters larger style changes → measured effects are lower bounds.")
    elif sig_count == 0:
        print("  → No significant selection bias on style change magnitude.")
    else:
        print("  → Mixed or anti-conservative pattern — inspect individual metrics.")

    return results


def make_violin_plots(all_results):
    """Generate violin plots comparing pass vs fail distributions per axis."""
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    plot_keys = ["norm_edit_dist", "bleu", "tfidf_cosine", "token_diff_rel"]

    for axis_name, results in all_results.items():
        if results is None:
            continue

        plot_results = [r for r in results if r["key"] in plot_keys]
        if not plot_results:
            continue

        n_metrics = len(plot_results)
        fig, axes = plt.subplots(1, n_metrics, figsize=(4 * n_metrics, 5))
        if n_metrics == 1:
            axes = [axes]

        for ax, r in zip(axes, plot_results):
            data = [r["pass_vals"], r["fail_vals"]]
            parts = ax.violinplot(data, positions=[0, 1], showmeans=True,
                                  showmedians=True, showextrema=True)
            for pc in parts["bodies"]:
                pc.set_alpha(0.7)

            ax.set_xticks([0, 1])
            ax.set_xticklabels([f"Pass\n(n={len(r['pass_vals'])})",
                                f"Fail\n(n={len(r['fail_vals'])})"])
            ax.set_title(r["metric"], fontsize=10)

            sig_str = f"p={r['p_value']:.3f}"
            if r["p_value"] < 0.05:
                sig_str += " *"
            d_str = f"d={r['cohens_d']:+.2f}"
            ax.text(0.5, 0.02, f"{sig_str}\n{d_str}",
                    transform=ax.transAxes, ha="center", fontsize=8,
                    bbox=dict(boxstyle="round,pad=0.3", facecolor="lightyellow",
                              edgecolor="gray", alpha=0.8))

        fig.suptitle(f"NLI Gate Selection Bias — {axis_name.title()}", fontsize=13)
        fig.tight_layout()
        out_path = OUT_DIR / f"nli_fn_bias_{axis_name}.png"
        fig.savefig(out_path, dpi=150, bbox_inches="tight")
        plt.close(fig)
        print(f"  Saved: {out_path}")


def main():
    np.random.seed(SEED)
    print("NLI Gate False-Negative Selection Bias Analysis")
    print(f"NLI threshold: {NLI_THRESHOLD}")
    print(f"Gate: passed_cf AND passed_dr")

    all_results = {}
    for axis_name, config in AXES.items():
        all_results[axis_name] = analyze_axis(axis_name, config)

    make_violin_plots(all_results)

    print(f"\n{'='*78}")
    print("  OVERALL CONCLUSION")
    print(f"{'='*78}")
    any_bias = any(
        results is not None and any(r["p_value"] < 0.05 for r in results)
        for results in all_results.values()
    )
    if any_bias:
        print("  Some metrics show significant pass/fail differences.")
        print("  If fail group has LARGER style changes → bias is conservative (lower bounds).")
    else:
        print("  No significant selection bias across any axis.")
        print("  NLI gate does not systematically filter by style change magnitude.")


if __name__ == "__main__":
    main()
