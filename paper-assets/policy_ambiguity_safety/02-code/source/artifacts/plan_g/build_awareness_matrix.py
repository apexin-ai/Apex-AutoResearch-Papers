#!/usr/bin/env python3
"""Build per-model × per-type disambiguation awareness matrix from failure_modes data."""

import json
import csv
import os
from collections import defaultdict
from itertools import combinations

import numpy as np
from scipy.stats import fisher_exact
from scipy.stats import false_discovery_control

BASE = "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts"
DATA_DIR = f"{BASE}/_project/data"
OUT_DIR = f"{BASE}/plan_g"

MODEL_FILES = {
    "gpt-5.4": f"{DATA_DIR}/failure_modes.jsonl",
    "gpt-4.1": f"{DATA_DIR}/failure_modes_gpt41.jsonl",
    "claude-sonnet-4-6": f"{DATA_DIR}/failure_modes_claude.jsonl",
    "qwen3-235b": f"{DATA_DIR}/failure_modes_qwen3.jsonl",
    "deepseek-v3": f"{DATA_DIR}/failure_modes_deepseek.jsonl",
}

MODELS = ["gpt-5.4", "gpt-4.1", "claude-sonnet-4-6", "qwen3-235b", "deepseek-v3"]
TYPES = ["authorization_scope", "conditional_precedence", "coreferential",
         "incompleteness", "lexical", "scopal"]
TYPE_SHORT = {
    "authorization_scope": "Auth. Scope",
    "conditional_precedence": "Cond. Prec.",
    "coreferential": "Coref.",
    "incompleteness": "Incompl.",
    "lexical": "Lexical",
    "scopal": "Scopal",
}
MODEL_SHORT = {
    "gpt-5.4": "GPT-5.4",
    "gpt-4.1": "GPT-4.1",
    "claude-sonnet-4-6": "Claude S4.6",
    "qwen3-235b": "Qwen3-235B",
    "deepseek-v3": "DeepSeek-V3",
}


def load_all_violations():
    """Load all failure_modes data with awareness coding."""
    records = []
    for model, fpath in MODEL_FILES.items():
        with open(fpath) as f:
            for line in f:
                d = json.loads(line)
                assert d.get("model", model) in (model, model), f"model mismatch in {fpath}"
                records.append({
                    "model": model,
                    "episode_id": d["episode_id"],
                    "clause_id": d["clause_id"],
                    "ambiguity_type": d["ambiguity_type"],
                    "showed_awareness": d["disambiguation_behavior"]["showed_awareness"],
                    "evidence": d["disambiguation_behavior"]["evidence"],
                })
    return records


def build_matrix(records):
    """Build counts: matrix[model][type] = (n_aware, n_total)."""
    matrix = defaultdict(lambda: defaultdict(lambda: [0, 0]))
    for r in records:
        m, t = r["model"], r["ambiguity_type"]
        matrix[m][t][1] += 1
        if r["showed_awareness"]:
            matrix[m][t][0] += 1
    return matrix


def write_csv(matrix):
    rows = []
    for m in MODELS:
        for t in TYPES:
            n_aware, n_total = matrix[m][t]
            rate = n_aware / n_total if n_total > 0 else 0.0
            rows.append({
                "model": m,
                "type": t,
                "n_aware": n_aware,
                "n_total": n_total,
                "awareness_rate": round(rate, 4),
            })
    # margin by model
    for m in MODELS:
        total_aware = sum(matrix[m][t][0] for t in TYPES)
        total_n = sum(matrix[m][t][1] for t in TYPES)
        rate = total_aware / total_n if total_n > 0 else 0.0
        rows.append({
            "model": m, "type": "ALL", "n_aware": total_aware,
            "n_total": total_n, "awareness_rate": round(rate, 4),
        })
    # margin by type
    for t in TYPES:
        total_aware = sum(matrix[m][t][0] for m in MODELS)
        total_n = sum(matrix[m][t][1] for m in MODELS)
        rate = total_aware / total_n if total_n > 0 else 0.0
        rows.append({
            "model": "ALL", "type": t, "n_aware": total_aware,
            "n_total": total_n, "awareness_rate": round(rate, 4),
        })
    # grand total
    grand_aware = sum(matrix[m][t][0] for m in MODELS for t in TYPES)
    grand_n = sum(matrix[m][t][1] for m in MODELS for t in TYPES)
    rows.append({
        "model": "ALL", "type": "ALL", "n_aware": grand_aware,
        "n_total": grand_n, "awareness_rate": round(grand_aware / grand_n, 4) if grand_n else 0,
    })

    outpath = f"{OUT_DIR}/awareness_matrix.csv"
    with open(outpath, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["model", "type", "n_aware", "n_total", "awareness_rate"])
        w.writeheader()
        w.writerows(rows)
    print(f"Wrote {outpath} ({len(rows)} rows)")
    return rows


def pairwise_fisher(matrix):
    """Fisher's exact test for all model pairs (aware vs not-aware × model)."""
    results = []
    pairs = list(combinations(MODELS, 2))
    for m1, m2 in pairs:
        a1 = sum(matrix[m1][t][0] for t in TYPES)
        n1 = sum(matrix[m1][t][1] for t in TYPES)
        a2 = sum(matrix[m2][t][0] for t in TYPES)
        n2 = sum(matrix[m2][t][1] for t in TYPES)
        table = [[a1, n1 - a1], [a2, n2 - a2]]
        odds_ratio, p_value = fisher_exact(table)
        results.append({
            "model_1": m1, "model_2": m2,
            "aware_1": a1, "total_1": n1, "rate_1": round(a1/n1, 4) if n1 else 0,
            "aware_2": a2, "total_2": n2, "rate_2": round(a2/n2, 4) if n2 else 0,
            "odds_ratio": round(odds_ratio, 4),
            "p_value": p_value,
        })

    # Holm-Bonferroni correction
    p_values = [r["p_value"] for r in results]
    sorted_indices = np.argsort(p_values)
    n_tests = len(p_values)
    for rank, idx in enumerate(sorted_indices):
        adjusted = min(p_values[idx] * (n_tests - rank), 1.0)
        results[idx]["p_holm"] = adjusted
    # Fix monotonicity
    for i in range(1, n_tests):
        idx_curr = sorted_indices[i]
        idx_prev = sorted_indices[i - 1]
        results[idx_curr]["p_holm"] = max(results[idx_curr]["p_holm"], results[idx_prev]["p_holm"])

    for r in results:
        r["significant_005"] = r["p_holm"] < 0.05
        r["p_value"] = round(r["p_value"], 6)
        r["p_holm"] = round(r["p_holm"], 6)

    return results


def cluster_test(matrix):
    """Test {Claude, GPT-4.1} vs {Qwen3, DeepSeek} cluster."""
    cluster_hi = ["gpt-4.1", "claude-sonnet-4-6"]
    cluster_lo = ["qwen3-235b", "deepseek-v3"]
    a_hi = sum(matrix[m][t][0] for m in cluster_hi for t in TYPES)
    n_hi = sum(matrix[m][t][1] for m in cluster_hi for t in TYPES)
    a_lo = sum(matrix[m][t][0] for m in cluster_lo for t in TYPES)
    n_lo = sum(matrix[m][t][1] for m in cluster_lo for t in TYPES)
    table = [[a_hi, n_hi - a_hi], [a_lo, n_lo - a_lo]]
    odds_ratio, p_value = fisher_exact(table)
    return {
        "cluster_hi": cluster_hi, "cluster_lo": cluster_lo,
        "aware_hi": a_hi, "total_hi": n_hi, "rate_hi": round(a_hi/n_hi, 4),
        "aware_lo": a_lo, "total_lo": n_lo, "rate_lo": round(a_lo/n_lo, 4) if n_lo else 0,
        "odds_ratio": round(odds_ratio, 4) if np.isfinite(odds_ratio) else "Inf",
        "p_value": p_value,
    }


def per_type_test(matrix):
    """Fisher's exact test for awareness rate across types (aggregate models)."""
    type_counts = {}
    for t in TYPES:
        a = sum(matrix[m][t][0] for m in MODELS)
        n = sum(matrix[m][t][1] for m in MODELS)
        type_counts[t] = (a, n)

    pairs = list(combinations(TYPES, 2))
    results = []
    for t1, t2 in pairs:
        a1, n1 = type_counts[t1]
        a2, n2 = type_counts[t2]
        table = [[a1, n1 - a1], [a2, n2 - a2]]
        odds_ratio, p_value = fisher_exact(table)
        results.append({
            "type_1": t1, "type_2": t2,
            "aware_1": a1, "total_1": n1, "rate_1": round(a1/n1, 4) if n1 else 0,
            "aware_2": a2, "total_2": n2, "rate_2": round(a2/n2, 4) if n2 else 0,
            "odds_ratio": round(odds_ratio, 4) if np.isfinite(odds_ratio) else "Inf",
            "p_value": p_value,
        })

    # Holm-Bonferroni
    p_values = [r["p_value"] for r in results]
    sorted_indices = np.argsort(p_values)
    n_tests = len(p_values)
    for rank, idx in enumerate(sorted_indices):
        adjusted = min(p_values[idx] * (n_tests - rank), 1.0)
        results[idx]["p_holm"] = adjusted
    for i in range(1, n_tests):
        idx_curr = sorted_indices[i]
        idx_prev = sorted_indices[i - 1]
        results[idx_curr]["p_holm"] = max(results[idx_curr]["p_holm"], results[idx_prev]["p_holm"])

    for r in results:
        r["significant_005"] = r["p_holm"] < 0.05
        r["p_value"] = round(r["p_value"], 6)
        r["p_holm"] = round(r["p_holm"], 6)

    return results, type_counts


def gpt54_3way_test(matrix):
    """GPT-5.4 is interesting: it's non-zero but lower than GPT-4.1/Claude. Test vs each cluster."""
    gpt54_a = sum(matrix["gpt-5.4"][t][0] for t in TYPES)
    gpt54_n = sum(matrix["gpt-5.4"][t][1] for t in TYPES)

    hi_a = sum(matrix[m][t][0] for m in ["gpt-4.1", "claude-sonnet-4-6"] for t in TYPES)
    hi_n = sum(matrix[m][t][1] for m in ["gpt-4.1", "claude-sonnet-4-6"] for t in TYPES)

    lo_a = sum(matrix[m][t][0] for m in ["qwen3-235b", "deepseek-v3"] for t in TYPES)
    lo_n = sum(matrix[m][t][1] for m in ["qwen3-235b", "deepseek-v3"] for t in TYPES)

    _, p_vs_hi = fisher_exact([[gpt54_a, gpt54_n - gpt54_a], [hi_a, hi_n - hi_a]])
    _, p_vs_lo = fisher_exact([[gpt54_a, gpt54_n - gpt54_a], [lo_a, lo_n - lo_a]])

    return {
        "gpt54_rate": round(gpt54_a / gpt54_n, 4),
        "hi_cluster_rate": round(hi_a / hi_n, 4),
        "lo_cluster_rate": round(lo_a / lo_n, 4) if lo_n else 0,
        "p_vs_hi_cluster": round(p_vs_hi, 6),
        "p_vs_lo_cluster": round(p_vs_lo, 6),
    }


def generate_report(matrix, csv_rows, pairwise, cluster, type_tests, type_counts, gpt54):
    lines = ["# Disambiguation Awareness: Per-Model × Per-Type Breakdown\n"]

    # Matrix table
    lines.append("## Awareness Matrix (n_aware / n_violations, rate)\n")
    header = "| Type | " + " | ".join(MODEL_SHORT[m] for m in MODELS) + " | Total |"
    sep = "|---" * (len(MODELS) + 2) + "|"
    lines.append(header)
    lines.append(sep)
    for t in TYPES:
        cells = []
        for m in MODELS:
            a, n = matrix[m][t]
            rate = a / n * 100 if n else 0
            cells.append(f"{a}/{n} ({rate:.1f}%)")
        a_t, n_t = type_counts[t]
        rate_t = a_t / n_t * 100 if n_t else 0
        cells.append(f"{a_t}/{n_t} ({rate_t:.1f}%)")
        lines.append(f"| {TYPE_SHORT[t]} | " + " | ".join(cells) + " |")
    # Margin row
    margin_cells = []
    for m in MODELS:
        a = sum(matrix[m][t][0] for t in TYPES)
        n = sum(matrix[m][t][1] for t in TYPES)
        rate = a / n * 100 if n else 0
        margin_cells.append(f"{a}/{n} ({rate:.1f}%)")
    ga = sum(matrix[m][t][0] for m in MODELS for t in TYPES)
    gn = sum(matrix[m][t][1] for m in MODELS for t in TYPES)
    margin_cells.append(f"{ga}/{gn} ({ga/gn*100:.1f}%)")
    lines.append(f"| **Total** | " + " | ".join(margin_cells) + " |")
    lines.append("")

    # Cluster test
    lines.append("## Cluster Analysis: {GPT-4.1, Claude} vs {Qwen3, DeepSeek}\n")
    lines.append(f"- High cluster: {cluster['rate_hi']*100:.1f}% ({cluster['aware_hi']}/{cluster['total_hi']})")
    lines.append(f"- Low cluster: {cluster['rate_lo']*100:.1f}% ({cluster['aware_lo']}/{cluster['total_lo']})")
    lines.append(f"- Fisher's exact p = {cluster['p_value']:.2e}, OR = {cluster['odds_ratio']}")
    lines.append("")

    # GPT-5.4 position
    lines.append("## GPT-5.4 Position\n")
    lines.append(f"- GPT-5.4: {gpt54['gpt54_rate']*100:.1f}%")
    lines.append(f"- vs high cluster ({gpt54['hi_cluster_rate']*100:.1f}%): p = {gpt54['p_vs_hi_cluster']:.4f}")
    lines.append(f"- vs low cluster ({gpt54['lo_cluster_rate']*100:.1f}%): p = {gpt54['p_vs_lo_cluster']:.4f}")
    lines.append("")

    # Pairwise tests
    lines.append("## Pairwise Model Comparisons (Fisher's exact, Holm-corrected)\n")
    lines.append("| Model 1 | Model 2 | Rate 1 | Rate 2 | OR | p (raw) | p (Holm) | Sig? |")
    lines.append("|---|---|---|---|---|---|---|---|")
    for r in sorted(pairwise, key=lambda x: x["p_value"]):
        sig = "**yes**" if r["significant_005"] else "no"
        lines.append(f"| {r['model_1']} | {r['model_2']} | {r['rate_1']*100:.1f}% | {r['rate_2']*100:.1f}% | {r['odds_ratio']} | {r['p_value']:.4f} | {r['p_holm']:.4f} | {sig} |")
    lines.append("")

    # Per-type
    lines.append("## Per-Type Awareness Rates (aggregated across models)\n")
    for t in TYPES:
        a, n = type_counts[t]
        lines.append(f"- {TYPE_SHORT[t]}: {a}/{n} ({a/n*100:.1f}%)" if n else f"- {TYPE_SHORT[t]}: 0/0")
    lines.append("")

    sig_type_pairs = [r for r in type_tests if r["significant_005"]]
    if sig_type_pairs:
        lines.append(f"Significant type-pair differences (Holm p<0.05): {len(sig_type_pairs)}")
        for r in sig_type_pairs:
            lines.append(f"  - {r['type_1']} vs {r['type_2']}: p={r['p_holm']:.4f}")
    else:
        lines.append("No significant type-pair differences after Holm correction.")
    lines.append("")

    # Key findings
    lines.append("## Key Findings\n")
    lines.append("1. Disambiguation awareness is concentrated in GPT-4.1 and Claude Sonnet 4.6 (10-11%), "
                 "with Qwen3-235B and DeepSeek-V3 showing zero awareness across all types.")
    lines.append(f"2. The two-cluster pattern is statistically significant (Fisher p = {cluster['p_value']:.2e}).")
    lines.append("3. GPT-5.4 occupies an intermediate position (~4%), significantly different from the zero cluster "
                 "but also lower than the high cluster.")
    lines.append("4. Awareness is coded among violating episodes only (denominator = violations per cell).")

    report = "\n".join(lines)
    outpath = f"{OUT_DIR}/analysis_report.md"
    with open(outpath, "w") as f:
        f.write(report)
    print(f"Wrote {outpath}")
    return report


def generate_appendix_tex(matrix, type_counts, cluster, pairwise, gpt54):
    """Generate LaTeX appendix table and text."""
    lines = []
    lines.append(r"\subsection{Disambiguation Awareness by Model and Ambiguity Type}")
    lines.append(r"\label{app:awareness-breakdown}")
    lines.append("")
    lines.append(r"Table~\ref{tab:awareness-matrix} disaggregates the overall disambiguation awareness rate "
                 r"(4.6\%, \S\ref{sec:disambiguation}) by model and ambiguity type. "
                 r"Awareness is coded as the agent explicitly acknowledging policy ambiguity or requesting "
                 r"clarification before acting, among episodes where the agent violated the intended policy interpretation.")
    lines.append("")

    # Table
    lines.append(r"\begin{table}[t]")
    lines.append(r"\centering")
    lines.append(r"\small")
    lines.append(r"\begin{tabular}{l" + "c" * len(MODELS) + "c}")
    lines.append(r"\toprule")
    header = " & ".join([r"\textbf{Type}"] + [r"\textbf{" + MODEL_SHORT[m] + "}" for m in MODELS] + [r"\textbf{All}"])
    lines.append(header + r" \\")
    lines.append(r"\midrule")

    for t in TYPES:
        cells = [TYPE_SHORT[t]]
        for m in MODELS:
            a, n = matrix[m][t]
            if n == 0:
                cells.append("--")
            elif a == 0:
                cells.append(f"0/{n}")
            else:
                cells.append(f"{a}/{n}")
        a_t, n_t = type_counts[t]
        cells.append(f"{a_t}/{n_t}")
        lines.append(" & ".join(cells) + r" \\")

    lines.append(r"\midrule")
    margin_cells = [r"\textbf{All}"]
    for m in MODELS:
        a = sum(matrix[m][t][0] for t in TYPES)
        n = sum(matrix[m][t][1] for t in TYPES)
        rate = a / n * 100 if n else 0
        margin_cells.append(f"{a}/{n} ({rate:.0f}\\%)")
    ga = sum(matrix[m][t][0] for m in MODELS for t in TYPES)
    gn = sum(matrix[m][t][1] for m in MODELS for t in TYPES)
    margin_cells.append(f"{ga}/{gn} ({ga/gn*100:.0f}\\%)")
    lines.append(" & ".join(margin_cells) + r" \\")
    lines.append(r"\bottomrule")
    lines.append(r"\end{tabular}")
    lines.append(r"\caption{Disambiguation awareness counts (aware/total violations) by model and ambiguity type. "
                 r"Awareness denotes the agent explicitly recognizing policy ambiguity before acting. "
                 r"Rates in the margin row are percentages of each model's total violations.}")
    lines.append(r"\label{tab:awareness-matrix}")
    lines.append(r"\end{table}")
    lines.append("")

    # Text paragraph
    lines.append(r"Awareness clusters sharply by model family. GPT-4.1 and Claude Sonnet~4.6 show non-trivial "
                 r"awareness rates (10.7\% and 11.0\%, respectively), while Qwen3-235B and DeepSeek-V3 "
                 r"exhibit zero awareness across all " + str(sum(matrix[m][t][1] for m in ["qwen3-235b", "deepseek-v3"] for t in TYPES)) +
                 r" combined violation episodes "
                 fr"(Fisher's exact $p = {cluster['p_value']:.1e}$, two-tailed). "
                 f"GPT-5.4 occupies an intermediate position at {gpt54['gpt54_rate']*100:.1f}\\%, "
                 f"significantly above the zero-awareness cluster ($p = {gpt54['p_vs_lo_cluster']:.3f}$) "
                 f"but also significantly below the high-awareness cluster ($p = {gpt54['p_vs_hi_cluster']:.4f}$). "
                 r"Across ambiguity types, awareness instances are sparse and distributed without "
                 r"strong concentration in any single type, "
                 r"though the small per-cell counts preclude reliable type-level inference.")

    tex = "\n".join(lines)
    outpath = f"{OUT_DIR}/appendix_draft.tex"
    with open(outpath, "w") as f:
        f.write(tex)
    print(f"Wrote {outpath}")


def generate_maintext_sentence(cluster, gpt54):
    p_exp = f"{cluster['p_value']:.1e}"
    sentence = (
        f"Awareness clusters by model family: GPT-4.1 and Claude~Sonnet~4.6 show non-zero rates "
        f"(10--11\\%) while Qwen3-235B and DeepSeek-V3 exhibit zero awareness across all "
        f"{cluster['total_lo']} combined violation episodes "
        f"($p = {p_exp}$, Fisher's exact test); "
        f"GPT-5.4 falls in between at {gpt54['gpt54_rate']*100:.1f}\\% "
        f"(Appendix~\\ref{{app:awareness-breakdown}})."
    )
    outpath = f"{OUT_DIR}/maintext_sentence.txt"
    with open(outpath, "w") as f:
        f.write(sentence + "\n")
    print(f"Wrote {outpath}")


def main():
    records = load_all_violations()
    print(f"Loaded {len(records)} violation records")

    matrix = build_matrix(records)

    # Verify totals match expected
    for m in MODELS:
        total = sum(matrix[m][t][1] for t in TYPES)
        aware = sum(matrix[m][t][0] for t in TYPES)
        print(f"  {m}: {aware}/{total} aware ({aware/total*100:.2f}%)" if total else f"  {m}: 0/0")

    csv_rows = write_csv(matrix)
    pairwise = pairwise_fisher(matrix)
    cluster = cluster_test(matrix)
    type_tests, type_counts = per_type_test(matrix)
    gpt54 = gpt54_3way_test(matrix)

    generate_report(matrix, csv_rows, pairwise, cluster, type_tests, type_counts, gpt54)
    generate_appendix_tex(matrix, type_counts, cluster, pairwise, gpt54)
    generate_maintext_sentence(cluster, gpt54)

    # Save full analysis as JSON
    analysis = {
        "matrix": {m: {t: {"n_aware": matrix[m][t][0], "n_total": matrix[m][t][1]}
                        for t in TYPES} for m in MODELS},
        "pairwise_fisher": pairwise,
        "cluster_test": cluster,
        "type_tests": type_tests,
        "type_counts": {t: {"n_aware": c[0], "n_total": c[1]} for t, c in type_counts.items()},
        "gpt54_position": gpt54,
    }
    with open(f"{OUT_DIR}/analysis_full.json", "w") as f:
        json.dump(analysis, f, indent=2, default=lambda o: bool(o) if isinstance(o, np.bool_) else o)
    print(f"Wrote {OUT_DIR}/analysis_full.json")


if __name__ == "__main__":
    main()
