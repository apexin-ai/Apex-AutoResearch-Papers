"""Case Study: ASV diagnosis applied to Sushkov et al. (2025), arXiv:2509.15510
"The (Short-Term) Effects of Large Language Models on Unemployment and Earnings."

Setting:
- Claude (Anthropic Economic Index, Handa et al. 2025) classifies each O*NET task
  into K=3 categories: automative / augmentative / neither.
- Task-level proportions are aggregated to occupation-level exposure shares.
- Authors run synthetic difference-in-differences (SDiD) with binary treatment
  (above-median exposure), recovering +$89 weekly earnings for exposed
  occupations after ChatGPT (Nov 2022).

Our framework projects this onto the K=3 exposure DAG topology:
    A in {automative, augmentative, neither}, A -> Y (earnings outcome).
The Claude task classification is the A* (mismeasured A); the regression
coefficient on the task type is the structural primitive that the SDiD effect
aggregates.

We construct three plausible confusion matrices for the Claude task classifier:
  best     : diag ~ 0.90 (high agreement with held-out human labels)
  realistic: diag ~ 0.80 (typical LLM coding accuracy on O*NET tasks)
  weak     : diag ~ 0.70 (lower bound for zero-shot LLM coding)
Each is constructed with a mild asymmetry between automation and augmentation
classes (LLMs in the Anthropic Index report systematic over-classification of
augmentation; see Handa et al. 2025 Nov report: 52%/45% split).

For each C, we compute:
  (1) bias_pct  : %-bias of the OLS coefficient on the "automative" dummy
                  (the primary contrast of substantive interest)
  (2) magnitude ASV with 10% threshold
  (3) sign-flip ASV (catastrophic-failure threshold for exposure topology)
We also Monte-Carlo over Dirichlet(diag, 1, 1) confusion matrices anchored at
each diagonal level to bound the distribution of bias and ASV.
"""
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from annot_sensitivity.bias import compute_bias  # noqa: E402
from annot_sensitivity.asv import compute_asv  # noqa: E402
from annot_sensitivity.confusion import random_confusion_matrix  # noqa: E402

OUTDIR = os.path.dirname(__file__)
os.makedirs(OUTDIR, exist_ok=True)


def make_realistic_matrix(diag, asymmetry=0.05):
    """Build a K=3 confusion matrix with given diagonal mass.

    Off-diagonal mass is spread asymmetrically so that the augmentative class
    (column 1) leaks slightly more probability to automative (row 0) than the
    reverse — reflecting that Claude self-reports more "augment" labels but
    annotators audit a subset as automation.
    """
    off = 1.0 - diag
    C = np.full((3, 3), off / 2.0)
    for k in range(3):
        C[k, k] = diag
    # asymmetry: column 1 (augmentative) leaks more to row 0 (automative)
    C[0, 1] = off / 2.0 + asymmetry
    C[2, 1] = off / 2.0 - asymmetry
    # column 0 (automative) leaks slightly more to row 2 (neither)
    C[2, 0] = off / 2.0 + asymmetry
    C[1, 0] = off / 2.0 - asymmetry
    # renormalize columns
    C = C / C.sum(axis=0, keepdims=True)
    return C


def analyze_matrix(C, label):
    bias = compute_bias("exposure", C)
    asv_mag = compute_asv("exposure", C, threshold_type="magnitude", threshold_value=0.10)
    asv_sf = compute_asv("exposure", C, threshold_type="sign_flip", threshold_value=0.0)
    return {
        "label": label,
        "diag": [float(C[i, i]) for i in range(C.shape[0])],
        "min_diag": float(np.min(np.diag(C))),
        "tau_true_auto": bias["tau_true"],
        "tau_biased_auto": bias["tau_biased"],
        "bias_pct_auto": bias["bias_pct"],
        "magnitude_ASV": asv_mag["asv"],
        "signflip_ASV": asv_sf["asv"],
    }


def monte_carlo_at_diag(diag, n=500, seed=0, n_grid=400):
    """Sample n random K=3 matrices with diagonal dominance approx `diag`
    and report distribution of bias%, mag ASV, sign-flip rate.
    """
    rng = np.random.default_rng(seed)
    biases = []
    mags = []
    sf_count = 0
    sf_asvs = []
    for _ in range(n):
        C = random_confusion_matrix(3, diag_dominance=diag, rng=rng)
        b = compute_bias("exposure", C)
        biases.append(b["bias_pct"])
        a_mag = compute_asv("exposure", C, threshold_type="magnitude",
                            threshold_value=0.10, n_grid=n_grid)
        if a_mag["asv"] is not None:
            mags.append(a_mag["asv"])
        a_sf = compute_asv("exposure", C, threshold_type="sign_flip",
                           threshold_value=0.0, n_grid=n_grid)
        if a_sf["asv"] is not None and a_sf["asv"] <= 1.0:
            sf_count += 1
            sf_asvs.append(a_sf["asv"])
    biases = np.array(biases)
    mags = np.array(mags) if mags else np.array([np.inf])
    return {
        "diag_dominance": diag,
        "n_samples": n,
        "bias_pct_mean": float(biases.mean()),
        "bias_pct_median": float(np.median(biases)),
        "bias_pct_p5": float(np.percentile(biases, 5)),
        "bias_pct_p95": float(np.percentile(biases, 95)),
        "abs_bias_pct_mean": float(np.abs(biases).mean()),
        "abs_bias_pct_p95": float(np.percentile(np.abs(biases), 95)),
        "magnitude_ASV_p5": float(np.percentile(mags, 5)) if len(mags) > 1 else None,
        "magnitude_ASV_median": float(np.median(mags)) if len(mags) > 1 else None,
        "fraction_signflip_within_delta1": sf_count / n,
        "signflip_ASV_median": float(np.median(sf_asvs)) if sf_asvs else None,
    }


def main():
    point_results = []
    for diag, label in [(0.90, "best"), (0.80, "realistic"), (0.70, "weak")]:
        C = make_realistic_matrix(diag)
        point_results.append(analyze_matrix(C, label))

    mc_results = [monte_carlo_at_diag(d) for d in [0.90, 0.80, 0.70]]

    paper_facts = {
        "title": "The (Short-Term) Effects of Large Language Models on Unemployment and Earnings",
        "arxiv": "2509.15510",
        "year": 2025,
        "llm_used": "Claude (Anthropic Economic Index; Handa et al. 2025)",
        "annotation_task": "Classify each O*NET task as automative / augmentative / neither",
        "K": 3,
        "estimator": "Synthetic difference-in-differences (SDiD)",
        "primary_estimand_USD": 89.0,
        "primary_estimand_se_USD": 20.0,
        "outcome": "Weekly earnings (2010 USD), occupation-level CPS data",
        "treatment": "Above-median LLM exposure (binary) x post-Nov-2022",
        "sample": "188 months Jan 2010-Aug 2025, US occupation-level panel",
    }

    summary = {
        "paper": paper_facts,
        "topology_assignment": "exposure (A -> Y, A is Claude-classified task type)",
        "framework_note": (
            "We apply the K=3 exposure-topology bias/ASV machinery to the "
            "task-level primitive that the paper aggregates to occupation level. "
            "The structural coefficient of interest is the earnings differential "
            "between the automative class and the 'neither' baseline (tau_auto)."
        ),
        "point_estimates": point_results,
        "monte_carlo": mc_results,
    }

    out_path = os.path.join(OUTDIR, "case_study_results.json")
    with open(out_path, "w") as f:
        json.dump(summary, f, indent=2, default=lambda o: None if isinstance(o, float) and np.isnan(o) else o)
    print(f"Wrote {out_path}")

    print("\n=== Point-estimate scenarios ===")
    for r in point_results:
        print(
            f"[{r['label']:>9}] diag~{r['min_diag']:.2f}  "
            f"bias_auto={r['bias_pct_auto']:+.1f}%  "
            f"mag_ASV={r['magnitude_ASV']}  "
            f"sf_ASV={r['signflip_ASV']}"
        )

    print("\n=== Monte-Carlo over Dirichlet(diag) anchored matrices ===")
    for r in mc_results:
        print(
            f"diag={r['diag_dominance']:.2f}  "
            f"|bias|_mean={r['abs_bias_pct_mean']:.1f}%  "
            f"|bias|_p95={r['abs_bias_pct_p95']:.1f}%  "
            f"sign-flip rate (delta<=1) = {r['fraction_signflip_within_delta1']:.1%}  "
            f"median sf_ASV={r['signflip_ASV_median']}"
        )


if __name__ == "__main__":
    main()
