#!/usr/bin/env python3
"""
plan_004_step1 — GSM8K Temporal MH-DIF Analysis

Replicates plan_001 methodology on GSM8K data from METABENCH.
Two matching strategies:
  - standard: purified GSM8K total score
  - external: total scores from ARC + HellaSwag + TruthfulQA + Winogrande

Inputs:
  metabench_data/benchmark-data/gsm8k.csv  — (source, item, correct) long format
  model_metadata.csv                        — cohort_temporal, etc.
  metabench_data/benchmark-data/{arc,hellaswag,truthfulqa,winogrande}.csv

Outputs (in plan_004/):
  gsm8k_dif_results.csv, gsm8k_ets_summary.csv, plan_004_step1_report.md
"""

import numpy as np
import pandas as pd
from scipy.stats import chi2 as chi2_dist
from pathlib import Path
import time
import warnings
import csv

warnings.filterwarnings("ignore", category=RuntimeWarning)

BASE = Path("/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts")
BENCH_DIR = BASE / "metabench_data" / "benchmark-data"
OUT = BASE / "plan_004"
OUT.mkdir(exist_ok=True)


# ════════════════════════════════════════════════════════════════════════════
#  DATA LOADING
# ════════════════════════════════════════════════════════════════════════════
print("=== Loading GSM8K data ===")
t0_load = time.time()
gsm = pd.read_csv(BENCH_DIR / "gsm8k.csv")
print(f"  Raw rows: {len(gsm):,}")

gsm["correct"] = gsm["correct"].map({"True": 1, "False": 0, True: 1, False: 0}).astype(np.int8)
gsm_pivot = gsm.pivot(index="source", columns="item", values="correct")
gsm_pivot = gsm_pivot.fillna(0).astype(np.int8)

MODEL_NAMES = np.array(gsm_pivot.index.tolist())
ITEM_IDS = np.array(gsm_pivot.columns.tolist())
X = gsm_pivot.values  # (N_models, J)
N_MODELS, J = X.shape
print(f"  Response matrix: {N_MODELS} models × {J} items")
del gsm, gsm_pivot

NAME2ROW = {n: i for i, n in enumerate(MODEL_NAMES)}

# Load model metadata
model_meta = pd.read_csv(BASE / "model_metadata.csv")
print(f"  Model metadata: {len(model_meta)} models")
print(f"  Cohort distribution: {model_meta.cohort_temporal.value_counts().to_dict()}")

# Intersection: GSM8K models ∩ metadata models
meta_names = set(model_meta["model_name"])
gsm_names = set(MODEL_NAMES)
common_names = meta_names & gsm_names
print(f"  GSM8K ∩ metadata: {len(common_names)} models")

elapsed_load = time.time() - t0_load
print(f"  Load time: {elapsed_load:.1f}s")


# ════════════════════════════════════════════════════════════════════════════
#  EXTERNAL MATCHING SCORES
# ════════════════════════════════════════════════════════════════════════════
def compute_benchmark_scores(filepath, benchmark_name):
    """Compute per-model total scores from a benchmark CSV (chunked for large files)."""
    print(f"  Loading {benchmark_name}...")
    t0 = time.time()
    scores = {}
    counts = {}
    chunk_size = 500_000
    for chunk in pd.read_csv(filepath, chunksize=chunk_size):
        chunk["correct"] = chunk["correct"].map({"True": 1, "False": 0, True: 1, False: 0})
        grouped = chunk.groupby("source")["correct"].agg(["sum", "count"])
        for model, row in grouped.iterrows():
            if model in scores:
                scores[model] += row["sum"]
                counts[model] += row["count"]
            else:
                scores[model] = row["sum"]
                counts[model] = row["count"]
    # Normalize: proportion correct
    result = {m: scores[m] / counts[m] for m in scores if counts[m] > 0}
    print(f"    {benchmark_name}: {len(result)} models, {time.time()-t0:.1f}s")
    return result


print("\n=== Computing external matching scores ===")
ext_benchmarks = ["arc", "hellaswag", "truthfulqa", "winogrande"]
ext_scores_raw = {}
for bm in ext_benchmarks:
    ext_scores_raw[bm] = compute_benchmark_scores(BENCH_DIR / f"{bm}.csv", bm)

# Combine: for each model, average across available benchmarks
# Only include models that appear in GSM8K AND have at least 2 external benchmarks
ext_combined = {}
for model in MODEL_NAMES:
    bm_scores = []
    for bm in ext_benchmarks:
        if model in ext_scores_raw[bm]:
            bm_scores.append(ext_scores_raw[bm][model])
    if len(bm_scores) >= 2:
        ext_combined[model] = np.mean(bm_scores)

print(f"  Models with external scores (≥2 benchmarks): {len(ext_combined)}")
del ext_scores_raw


# ════════════════════════════════════════════════════════════════════════════
#  COHORT CONSTRUCTION
# ════════════════════════════════════════════════════════════════════════════
print("\n=== Cohort construction ===")


def rows_for(col, values):
    names = model_meta.loc[model_meta[col].isin(values), "model_name"]
    return np.array([NAME2ROW[n] for n in names if n in NAME2ROW])


ref_idx = rows_for("cohort_temporal", ["2023"])
foc_idx = rows_for("cohort_temporal", ["2024"])
print(f"  Temporal cohort: ref=2023 (N={len(ref_idx)}), foc=2024 (N={len(foc_idx)})")

# For external matching, further restrict to models with external scores
ref_names_ext = [MODEL_NAMES[i] for i in ref_idx if MODEL_NAMES[i] in ext_combined]
foc_names_ext = [MODEL_NAMES[i] for i in foc_idx if MODEL_NAMES[i] in ext_combined]
ref_idx_ext = np.array([NAME2ROW[n] for n in ref_names_ext])
foc_idx_ext = np.array([NAME2ROW[n] for n in foc_names_ext])
print(f"  External cohort: ref=2023 (N={len(ref_idx_ext)}), foc=2024 (N={len(foc_idx_ext)})")


# ════════════════════════════════════════════════════════════════════════════
#  MH-DIF CORE
# ════════════════════════════════════════════════════════════════════════════
def _nan_row(j):
    return dict(col_idx=j, alpha_mh=np.nan, delta_mh=np.nan,
                se=np.nan, chi2=np.nan, p_value=np.nan, ets_class="A")


def mh_dif(X_ref, X_foc, n_strata=5, external_scores_ref=None, external_scores_foc=None):
    """
    Purified Mantel-Haenszel DIF.

    If external_scores_{ref,foc} are provided, use them as the matching
    variable instead of purified total scores.
    """
    _Nr, Jc = X_ref.shape
    use_external = external_scores_ref is not None

    if not use_external:
        tot_ref = X_ref.sum(axis=1).astype(np.float64)
        tot_foc = X_foc.sum(axis=1).astype(np.float64)
    else:
        ext_ref = external_scores_ref.astype(np.float64)
        ext_foc = external_scores_foc.astype(np.float64)

    cols = np.arange(Jc)
    rows = []
    t0 = time.time()

    for pos, j in enumerate(cols):
        if pos % 200 == 0 and pos > 0:
            print(f"    {pos}/{len(cols)}  ({time.time()-t0:.0f}s)")

        if use_external:
            s_ref = ext_ref
            s_foc = ext_foc
        else:
            # Purified: exclude item j
            s_ref = tot_ref - X_ref[:, j].astype(np.float64)
            s_foc = tot_foc - X_foc[:, j].astype(np.float64)

        s_all = np.concatenate([s_ref, s_foc])
        edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))
        if len(edges) < 2:
            rows.append(_nan_row(j))
            continue
        n_bins = len(edges) - 1

        k_ref = np.digitize(s_ref, edges[1:-1])
        k_foc = np.digitize(s_foc, edges[1:-1])

        R = S = 0.0
        sum_diff = 0.0
        sum_var = 0.0
        pr = ps_qr = qs = 0.0
        n_ok = 0

        for k in range(n_bins):
            mr = (k_ref == k)
            mf = (k_foc == k)
            n1 = int(mr.sum())
            n0 = int(mf.sum())
            if n1 == 0 or n0 == 0:
                continue

            A = float(X_ref[mr, j].sum())
            B = float(n1 - A)
            C = float(X_foc[mf, j].sum())
            D = float(n0 - C)
            Nk = float(n1 + n0)
            m1 = A + C
            m0 = B + D

            if m1 == 0 or m0 == 0 or Nk <= 1:
                continue
            n_ok += 1

            Rk = A * D / Nk
            Sk = B * C / Nk
            R += Rk
            S += Sk

            EA = n1 * m1 / Nk
            sum_diff += A - EA
            sum_var += n1 * n0 * m1 * m0 / (Nk * Nk * (Nk - 1))

            Pk = (A + D) / Nk
            Qk = (B + C) / Nk
            pr += Pk * Rk
            ps_qr += Pk * Sk + Qk * Rk
            qs += Qk * Sk

        if n_ok == 0 or (R == 0 and S == 0):
            rows.append(_nan_row(j))
            continue

        # MH odds ratio — handle inf properly
        if S == 0:
            alpha, delta, se = np.inf, -np.inf, np.nan
        elif R == 0:
            alpha, delta, se = 0.0, np.inf, np.nan
        else:
            alpha = R / S
            delta = -2.35 * np.log(alpha)
            v = pr / (2 * R * R) + ps_qr / (2 * R * S) + qs / (2 * S * S)
            se = 2.35 * np.sqrt(v) if v > 0 else np.nan

        # MH chi2 with continuity correction
        if sum_var > 0:
            chi2_stat = max(abs(sum_diff) - 0.5, 0) ** 2 / sum_var
            pval = 1 - chi2_dist.cdf(chi2_stat, df=1)
        else:
            chi2_stat = pval = np.nan

        # ETS classification — inf delta → extreme DIF (C if significant)
        ad = abs(delta) if np.isfinite(delta) else 999.0
        if ad < 1.0:
            ets = "A"
        elif ad >= 1.5 and (not np.isnan(pval)) and pval < 0.05:
            ets = "C"
        else:
            ets = "B"

        rows.append(dict(col_idx=j, alpha_mh=alpha, delta_mh=delta,
                         se=se, chi2=chi2_stat, p_value=pval, ets_class=ets))

    elapsed = time.time() - t0
    print(f"    done — {len(cols)} items in {elapsed:.1f}s")
    return pd.DataFrame(rows)


# ════════════════════════════════════════════════════════════════════════════
#  MAIN ANALYSIS
# ════════════════════════════════════════════════════════════════════════════
def main():
    results_parts = []

    # ── Standard MH-DIF (purified GSM8K total score) ──────────────────────
    print("\n=== Standard MH-DIF (purified GSM8K total, 5 strata) ===")
    print(f"  ref=2023 (N={len(ref_idx)}), foc=2024 (N={len(foc_idx)})")

    dif_std = mh_dif(X[ref_idx], X[foc_idx], n_strata=5)
    dif_std["item_id"] = [ITEM_IDS[i] for i in dif_std["col_idx"]]
    dif_std["matching_type"] = "standard"
    print(f"  ETS: {dif_std.ets_class.value_counts().to_dict()}")

    delta_finite = dif_std.loc[np.isfinite(dif_std.delta_mh), "delta_mh"]
    print(f"  Δ_MH stats: mean={delta_finite.mean():.3f}, median={delta_finite.median():.3f}, "
          f"std={delta_finite.std():.3f}, range=[{delta_finite.min():.3f}, {delta_finite.max():.3f}]")
    results_parts.append(dif_std)

    # ── External MH-DIF (other benchmarks total score) ────────────────────
    print("\n=== External MH-DIF (ARC+HellaSwag+TruthfulQA+Winogrande, 5 strata) ===")
    print(f"  ref=2023 (N={len(ref_idx_ext)}), foc=2024 (N={len(foc_idx_ext)})")

    ext_ref_scores = np.array([ext_combined[MODEL_NAMES[i]] for i in ref_idx_ext])
    ext_foc_scores = np.array([ext_combined[MODEL_NAMES[i]] for i in foc_idx_ext])

    dif_ext = mh_dif(X[ref_idx_ext], X[foc_idx_ext], n_strata=5,
                     external_scores_ref=ext_ref_scores,
                     external_scores_foc=ext_foc_scores)
    dif_ext["item_id"] = [ITEM_IDS[i] for i in dif_ext["col_idx"]]
    dif_ext["matching_type"] = "external"
    print(f"  ETS: {dif_ext.ets_class.value_counts().to_dict()}")

    delta_finite_ext = dif_ext.loc[np.isfinite(dif_ext.delta_mh), "delta_mh"]
    print(f"  Δ_MH stats: mean={delta_finite_ext.mean():.3f}, median={delta_finite_ext.median():.3f}, "
          f"std={delta_finite_ext.std():.3f}, range=[{delta_finite_ext.min():.3f}, {delta_finite_ext.max():.3f}]")
    results_parts.append(dif_ext)

    # ── Sanity check: random split ────────────────────────────────────────
    print("\n=== Sanity check: random half-split of 2023 cohort ===")
    rng = np.random.RandomState(42)
    perm = rng.permutation(len(ref_idx))
    half = len(perm) // 2
    san_ref = ref_idx[perm[:half]]
    san_foc = ref_idx[perm[half:]]
    print(f"  Split: {len(san_ref)} vs {len(san_foc)}")
    dif_san = mh_dif(X[san_ref], X[san_foc], n_strata=5)
    vc_san = dif_san["ets_class"].value_counts()
    n_c_san = vc_san.get("C", 0)
    pct_c_san = n_c_san / len(dif_san) * 100
    print(f"  ETS C: {n_c_san}/{len(dif_san)} = {pct_c_san:.2f}% (expect <5%)")

    # ── Agreement between standard and external ───────────────────────────
    print("\n=== Agreement: standard vs external ===")
    merged = dif_std[["item_id", "ets_class", "delta_mh"]].merge(
        dif_ext[["item_id", "ets_class", "delta_mh"]],
        on="item_id", suffixes=("_std", "_ext"))

    both_c = ((merged.ets_class_std == "C") & (merged.ets_class_ext == "C")).sum()
    std_only_c = ((merged.ets_class_std == "C") & (merged.ets_class_ext != "C")).sum()
    ext_only_c = ((merged.ets_class_std != "C") & (merged.ets_class_ext == "C")).sum()
    neither_c = ((merged.ets_class_std != "C") & (merged.ets_class_ext != "C")).sum()
    print(f"  both_C={both_c}, std_only_C={std_only_c}, ext_only_C={ext_only_c}, neither={neither_c}")

    # Correlation of delta_mh between standard and external
    finite_mask = np.isfinite(merged.delta_mh_std) & np.isfinite(merged.delta_mh_ext)
    if finite_mask.sum() > 10:
        from scipy.stats import spearmanr, pearsonr
        rho_s, p_s = spearmanr(merged.loc[finite_mask, "delta_mh_std"],
                                merged.loc[finite_mask, "delta_mh_ext"])
        r_p, p_p = pearsonr(merged.loc[finite_mask, "delta_mh_std"],
                            merged.loc[finite_mask, "delta_mh_ext"])
        print(f"  Δ_MH correlation: Spearman ρ={rho_s:.3f} (p={p_s:.2e}), Pearson r={r_p:.3f} (p={p_p:.2e})")

    # ── Save results ──────────────────────────────────────────────────────
    print("\n=== Saving outputs ===")

    # Combined DIF results
    all_results = pd.concat(results_parts, ignore_index=True)
    out_cols = ["item_id", "matching_type", "alpha_mh", "delta_mh", "se",
                "chi2", "p_value", "ets_class"]
    all_results[out_cols].to_csv(OUT / "gsm8k_dif_results.csv", index=False)

    # ETS summary
    summary_rows = []
    for mt in ["standard", "external"]:
        sub = all_results[all_results.matching_type == mt]
        vc = sub.ets_class.value_counts()
        n = len(sub)
        d_fin = sub.loc[np.isfinite(sub.delta_mh), "delta_mh"]
        summary_rows.append(dict(
            matching_type=mt,
            n_ref=len(ref_idx) if mt == "standard" else len(ref_idx_ext),
            n_foc=len(foc_idx) if mt == "standard" else len(foc_idx_ext),
            n_items=n,
            n_ets_a=vc.get("A", 0), n_ets_b=vc.get("B", 0), n_ets_c=vc.get("C", 0),
            pct_a=vc.get("A", 0) / n * 100,
            pct_b=vc.get("B", 0) / n * 100,
            pct_c=vc.get("C", 0) / n * 100,
            delta_mean=d_fin.mean(), delta_median=d_fin.median(),
            delta_std=d_fin.std(), delta_min=d_fin.min(), delta_max=d_fin.max(),
        ))
    summary_rows.append(dict(
        matching_type="sanity_random",
        n_ref=len(san_ref), n_foc=len(san_foc),
        n_items=len(dif_san),
        n_ets_a=vc_san.get("A", 0), n_ets_b=vc_san.get("B", 0), n_ets_c=vc_san.get("C", 0),
        pct_a=vc_san.get("A", 0) / len(dif_san) * 100,
        pct_b=vc_san.get("B", 0) / len(dif_san) * 100,
        pct_c=pct_c_san,
        delta_mean=np.nan, delta_median=np.nan,
        delta_std=np.nan, delta_min=np.nan, delta_max=np.nan,
    ))
    summary_df = pd.DataFrame(summary_rows)
    summary_df.to_csv(OUT / "gsm8k_ets_summary.csv", index=False)

    # ── Generate report ───────────────────────────────────────────────────
    L = []
    def w(s=""):
        L.append(s)

    w("# Plan 004 Step 1: GSM8K Temporal MH-DIF Analysis")
    w()
    w("## 1. Data & Setup")
    w()
    w(f"- **Benchmark**: GSM8K (grade-school math, single domain)")
    w(f"- **Response matrix**: {N_MODELS} models × {J} items")
    w(f"- **GSM8K ∩ metadata**: {len(common_names)} models")
    w(f"- **Temporal cohort (standard)**: ref=2023 (N={len(ref_idx)}), foc=2024 (N={len(foc_idx)})")
    w(f"- **Temporal cohort (external)**: ref=2023 (N={len(ref_idx_ext)}), foc=2024 (N={len(foc_idx_ext)})")
    w(f"- **External matching**: average proportion correct across ARC, HellaSwag, TruthfulQA, Winogrande")
    w(f"- **Models with external scores**: {len(ext_combined)} (require ≥2 benchmarks)")
    w()

    w("## 2. ETS Classification")
    w()
    w("| Matching | N_ref | N_foc | Items | A | B | C | %A | %B | %C |")
    w("|----------|-------|-------|-------|---|---|---|-----|-----|-----|")
    for _, r in summary_df.iterrows():
        w(f"| {r.matching_type} | {r.n_ref} | {r.n_foc} | {r.n_items} | "
          f"{r.n_ets_a} | {r.n_ets_b} | {r.n_ets_c} | "
          f"{r.pct_a:.1f}% | {r.pct_b:.1f}% | {r.pct_c:.1f}% |")
    w()

    w("## 3. Δ_MH Distribution (finite values)")
    w()
    w("| Matching | Mean | Median | Std | Min | Max |")
    w("|----------|------|--------|-----|-----|-----|")
    for _, r in summary_df[summary_df.matching_type != "sanity_random"].iterrows():
        w(f"| {r.matching_type} | {r.delta_mean:.3f} | {r.delta_median:.3f} | "
          f"{r.delta_std:.3f} | {r.delta_min:.3f} | {r.delta_max:.3f} |")
    w()

    # Inf delta items
    n_inf_std = (~np.isfinite(dif_std.delta_mh)).sum()
    n_inf_ext = (~np.isfinite(dif_ext.delta_mh)).sum()
    w(f"- Non-finite Δ_MH: standard={n_inf_std}, external={n_inf_ext}")
    w()

    w("## 4. Standard vs External Agreement")
    w()
    w(f"- Both C: {both_c}")
    w(f"- Standard-only C: {std_only_c}")
    w(f"- External-only C: {ext_only_c}")
    w(f"- Neither C: {neither_c}")
    if finite_mask.sum() > 10:
        w(f"- Δ_MH Spearman ρ = {rho_s:.3f} (p = {p_s:.2e})")
        w(f"- Δ_MH Pearson r = {r_p:.3f} (p = {p_p:.2e})")
    w()

    w("## 5. Sanity Check")
    w()
    w(f"Random half-split of 2023 cohort: **{pct_c_san:.2f}% C** (expect < 5%)")
    w()

    w("## 6. Comparison with MMLU (plan_001)")
    w()
    w("| | MMLU (plan_001) | GSM8K (this) |")
    w("|--|----------------|--------------|")
    w(f"| Items | 12,508 | {J} |")
    w(f"| Models (temporal) | 1,080 vs 807 | {len(ref_idx)} vs {len(foc_idx)} |")
    w(f"| Standard %C | (see plan_001_report) | {summary_df.loc[summary_df.matching_type=='standard','pct_c'].iloc[0]:.1f}% |")
    w(f"| Sanity %C | (see plan_001_report) | {pct_c_san:.1f}% |")
    w()

    # Top DIF items
    w("## 7. Top 20 DIF Items (standard matching, by |Δ_MH|)")
    w()
    dif_std_sorted = dif_std.loc[np.isfinite(dif_std.delta_mh)].copy()
    dif_std_sorted["abs_delta"] = dif_std_sorted.delta_mh.abs()
    top20 = dif_std_sorted.nlargest(20, "abs_delta")
    w("| Item | Δ_MH | SE | p-value | ETS |")
    w("|------|------|----|---------|-----|")
    for _, r in top20.iterrows():
        p_str = f"{r.p_value:.2e}" if not np.isnan(r.p_value) else "NaN"
        w(f"| {r.item_id} | {r.delta_mh:+.3f} | {r.se:.3f} | {p_str} | {r.ets_class} |")
    w()

    # Direction analysis
    w("## 8. DIF Direction Analysis")
    w()
    n_pos = (dif_std_sorted.delta_mh > 0).sum()
    n_neg = (dif_std_sorted.delta_mh < 0).sum()
    n_zero = (dif_std_sorted.delta_mh == 0).sum()
    w(f"- Positive Δ (favoring 2024): {n_pos} items ({n_pos/len(dif_std_sorted)*100:.1f}%)")
    w(f"- Negative Δ (favoring 2023): {n_neg} items ({n_neg/len(dif_std_sorted)*100:.1f}%)")
    w(f"- Zero Δ: {n_zero} items")
    w()

    c_items = dif_std[dif_std.ets_class == "C"]
    if len(c_items) > 0:
        c_pos = (c_items.delta_mh > 0).sum()
        c_neg = (c_items.delta_mh < 0).sum()
        w(f"Among ETS-C items: {c_pos} favor 2024, {c_neg} favor 2023")
    w()

    report_text = "\n".join(L) + "\n"
    (OUT / "plan_004_step1_report.md").write_text(report_text)

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    for _, r in summary_df.iterrows():
        print(f"  {r.matching_type}: A={r.n_ets_a}, B={r.n_ets_b}, C={r.n_ets_c} ({r.pct_c:.1f}%)")
    print(f"  Sanity random: {pct_c_san:.2f}% C")
    print(f"\nAll outputs saved to {OUT}")


if __name__ == "__main__":
    main()
