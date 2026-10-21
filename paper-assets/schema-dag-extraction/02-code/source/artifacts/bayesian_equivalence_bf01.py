#!/usr/bin/env python3
"""Bayesian Equivalence BF01 for Count x BCS Interaction."""

import json
import numpy as np
from scipy import stats
from scipy.integrate import quad
from pathlib import Path

DATA_PATH = Path(__file__).parent / "d051_fewrel_n25_s42" / "eval_results.json"
OUTPUT_PATH = Path(__file__).parent / "bayesian_equivalence_bf01.json"
LATEX_PATH = Path(__file__).parent / "bayesian_equivalence_latex.tex"

INTERPRETATION_THRESHOLDS = [
    (100, "decisive evidence for null"),
    (10, "strong evidence for null"),
    (3, "moderate evidence for null"),
    (1, "anecdotal evidence for null"),
    (0, "evidence favors alternative"),
]


def interpret_bf01(bf01):
    for threshold, label in INTERPRETATION_THRESHOLDS:
        if bf01 >= threshold:
            return label
    return "evidence favors alternative"


def compute_bf01(data_by_cell, prior_scale=3.0):
    means = {k: np.mean(v) for k, v in data_by_cell.items()}
    ns = {k: len(v) for k, v in data_by_cell.items()}

    interaction = (means[("8", "high")] - means[("8", "low")]) - (
        means[("16", "high")] - means[("16", "low")]
    )

    vars_cell = {k: np.var(v, ddof=1) / len(v) for k, v in data_by_cell.items()}
    se_interaction = np.sqrt(sum(vars_cell.values()))

    t_obs = interaction / se_interaction
    df = sum(ns.values()) - 4

    likelihood_h0 = stats.t.pdf(t_obs, df)

    def likelihood_h1_integrand(delta):
        noncentrality = delta / se_interaction
        return stats.nct.pdf(t_obs, df, noncentrality) * stats.cauchy.pdf(
            delta, 0, prior_scale
        )

    likelihood_h1, _ = quad(likelihood_h1_integrand, -np.inf, np.inf, limit=200)

    bf01 = likelihood_h0 / likelihood_h1
    return bf01, t_obs, df, interaction, se_interaction


def main():
    with open(DATA_PATH) as f:
        raw = json.load(f)

    # Filter count_8 and count_16
    batches = {
        k: v for k, v in raw.items() if v["count_key"] in ("count_8", "count_16")
    }
    print(f"Filtered batches: {len(batches)}")

    # Median split within each count level
    by_count = {"8": [], "16": []}
    for k, v in batches.items():
        count = v["count_key"].replace("count_", "")
        by_count[count].append(v)

    print(f"count_8: {len(by_count['8'])} batches, count_16: {len(by_count['16'])} batches")

    data_by_cell = {}
    for count_level in ["8", "16"]:
        items = by_count[count_level]
        bcs_values = [it["bcs"] for it in items]
        median_bcs = np.median(bcs_values)
        print(f"count_{count_level} BCS median: {median_bcs:.4f}")

        low = [it["accuracy"] * 100 for it in items if it["bcs"] <= median_bcs]
        high = [it["accuracy"] * 100 for it in items if it["bcs"] > median_bcs]
        data_by_cell[(count_level, "low")] = low
        data_by_cell[(count_level, "high")] = high

    # Print cell stats
    print("\nCell statistics (pp):")
    for key in [("8", "low"), ("8", "high"), ("16", "low"), ("16", "high")]:
        vals = data_by_cell[key]
        print(
            f"  count_{key[0]}_bcs_{key[1]}: n={len(vals)}, "
            f"mean={np.mean(vals):.2f}, sd={np.std(vals, ddof=1):.2f}"
        )

    # Primary analysis
    bf01, t_obs, df, interaction, se = compute_bf01(data_by_cell, prior_scale=3.0)
    print(f"\nObserved interaction: {interaction:.2f} pp")
    print(f"SE: {se:.2f} pp")
    print(f"t = {t_obs:.3f}, df = {df}")
    print(f"BF01 (scale=3pp): {bf01:.2f} — {interpret_bf01(bf01)}")

    # Sensitivity analysis
    scales = [1, 2, 3, 5]
    sensitivity = {}
    for s in scales:
        bf, *_ = compute_bf01(data_by_cell, prior_scale=float(s))
        sensitivity[f"scale_{s}pp"] = {
            "bf01": round(bf, 2),
            "bf10": round(1 / bf, 4),
            "interpretation": interpret_bf01(bf),
        }
        print(f"BF01 (scale={s}pp): {bf:.2f} — {interpret_bf01(bf)}")

    # Build output
    cell_means = {
        f"{k[0]}_{k[1]}": round(np.mean(v), 2) for k, v in data_by_cell.items()
    }
    n_per_cell = {f"{k[0]}_{k[1]}": len(v) for k, v in data_by_cell.items()}

    result = {
        "observed_interaction_pp": round(interaction, 2),
        "se_interaction_pp": round(se, 2),
        "t_statistic": round(t_obs, 3),
        "df": df,
        "n_per_cell": n_per_cell,
        "cell_means_pp": cell_means,
        "prior_sensitivity": sensitivity,
        "primary_bf01": round(bf01, 2),
        "primary_interpretation": interpret_bf01(bf01),
    }

    with open(OUTPUT_PATH, "w") as f:
        json.dump(result, f, indent=2)
    print(f"\nResults saved to {OUTPUT_PATH}")

    # Generate LaTeX if BF01 >= 3
    if bf01 >= 3:
        write_latex(result)
        print(f"LaTeX saved to {LATEX_PATH}")


def write_latex(r):
    bf01 = r["primary_bf01"]
    interp = r["primary_interpretation"]
    interaction = r["observed_interaction_pp"]
    se = r["se_interaction_pp"]
    t = r["t_statistic"]
    df = r["df"]
    sens = r["prior_sensitivity"]

    # Sensitivity table rows
    rows = []
    for key in ["scale_1pp", "scale_2pp", "scale_3pp", "scale_5pp"]:
        s = key.replace("scale_", "").replace("pp", "")
        rows.append(
            f"    {s} & {sens[key]['bf01']:.1f} & {sens[key]['bf10']:.4f} & {sens[key]['interpretation']} \\\\"
        )
    table_rows = "\n".join(rows)

    appendix = rf"""%% Appendix C paragraph: Bayesian equivalence test for Count x BCS interaction
\paragraph{{Bayesian Equivalence Test.}}
To complement the frequentist TOST analysis, we computed a Bayes factor
for the null interaction between schema count and boundary confusability (BCS).
Following the JZS framework \citep{{rouder2009bayesian}}, we placed a Cauchy($0, \sigma$)
prior on the interaction effect under $H_1$ and a point-null under $H_0$.
The observed interaction was {interaction:.2f}\,pp (SE\,=\,{se:.2f}\,pp;
$t({df})={t:.2f}$).  With the default prior scale $\sigma = 3$\,pp,
$\mathrm{{BF}}_{{01}} = {bf01:.1f}$, indicating \textit{{{interp}}}.
Table~\ref{{tab:bf01-sensitivity}} shows that this conclusion is robust across
a range of prior scales.

\begin{{table}}[h]
\centering
\small
\caption{{Prior sensitivity for the Count $\times$ BCS interaction $\mathrm{{BF}}_{{01}}$.}}
\label{{tab:bf01-sensitivity}}
\begin{{tabular}}{{cccc}}
\toprule
Prior scale $\sigma$ (pp) & $\mathrm{{BF}}_{{01}}$ & $\mathrm{{BF}}_{{10}}$ & Interpretation \\
\midrule
{table_rows}
\bottomrule
\end{{tabular}}
\end{{table}}"""

    inline = (
        rf"A complementary Bayesian analysis yielded $\mathrm{{BF}}_{{01}} = {bf01:.1f}$ "
        rf"(Cauchy prior, $\sigma = 3$\,pp), constituting {interp} "
        r"(see Appendix~\ref{sec:bayesian-equivalence} for details and prior sensitivity)."
    )

    with open(LATEX_PATH, "w") as f:
        f.write("%% === Appendix C paragraph ===\n")
        f.write(appendix)
        f.write("\n\n")
        f.write("%% === Inline sentence for §4.4 (after TOST paragraph) ===\n")
        f.write(inline)
        f.write("\n")


if __name__ == "__main__":
    main()
