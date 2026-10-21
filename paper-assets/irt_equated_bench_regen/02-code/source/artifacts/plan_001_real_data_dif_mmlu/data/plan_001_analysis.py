#!/usr/bin/env python3
"""
plan_001_analysis.py — METABENCH real-data MH-DIF analysis

Runs purified Mantel-Haenszel DIF detection on MMLU binary response data with
two cohort definitions (temporal 2023-vs-2024, ability Q1-2 vs Q4-5), validates
against Li et al. contamination proxy labels, and performs within-family,
domain-specificity, and negative-discrimination sensitivity analyses.

Inputs  (all in ../):
  response_matrix.npz          — (5227, 12508) CSR sparse, int8 binary
  response_matrix_index.npz    — model_names, item_ids
  model_metadata.csv           — cohort_temporal, cohort_accuracy_quintile, family
  item_metadata.csv            — subject, is_negative_disc
  mmlu_li2024_proxy_labels.csv — contamination_type proxy labels

Outputs (all in ./):
  dif_results_temporal.csv, dif_results_ability.csv, dif_summary.csv,
  within_family_dif.csv, cross_analysis.csv, domain_specificity.csv,
  neg_disc_sensitivity.csv, plan_001_report.md

Dependencies: numpy, scipy, pandas
"""

import numpy as np
import pandas as pd
from scipy.sparse import load_npz
from scipy.stats import chi2 as chi2_dist, spearmanr
from pathlib import Path
import time
import warnings

warnings.filterwarnings("ignore", category=RuntimeWarning)

BASE = Path("/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts")
OUT = BASE / "plan_001"
OUT.mkdir(exist_ok=True)


# ════════════════════════════════════════════════════════════════════════════
#  DATA LOADING
# ════════════════════════════════════════════════════════════════════════════
print("=== Loading data ===")
mat = load_npz(BASE / "response_matrix.npz")
X = mat.toarray().astype(np.int16)          # (5227, 12508)
del mat

idx = np.load(BASE / "response_matrix_index.npz", allow_pickle=True)
MODEL_NAMES = idx["model_names"]             # (5227,)
ITEM_IDS    = idx["item_ids"]                # (12508,)

model_meta = pd.read_csv(BASE / "model_metadata.csv")
item_meta  = pd.read_csv(BASE / "item_metadata.csv")
li_labels  = pd.read_csv(BASE / "mmlu_li2024_proxy_labels.csv")

NAME2ROW = {n: i for i, n in enumerate(MODEL_NAMES)}
N_MODELS, J = X.shape
print(f"  Matrix {N_MODELS}×{J}")
print(f"  Li annotated: {(li_labels.contamination_type != 'no_annotation').sum()}, "
      f"no_annotation: {(li_labels.contamination_type == 'no_annotation').sum()}")


# ════════════════════════════════════════════════════════════════════════════
#  MH-DIF CORE
# ════════════════════════════════════════════════════════════════════════════
def mh_dif(X_ref, X_foc, n_strata=5, col_mask=None):
    """
    Purified Mantel-Haenszel DIF for all items (or a column subset).

    For item j the matching variable is:
        purified_score = total_score_across_all_columns - response_to_item_j

    Parameters
    ----------
    X_ref, X_foc : ndarray (N_ref, J) and (N_foc, J), int, binary 0/1
    n_strata     : number of quantile-based score strata
    col_mask     : bool array (J,); True = analyse this column.  None = all.

    Returns
    -------
    DataFrame with cols: col_idx, alpha_mh, delta_mh, se, chi2, p_value, ets_class
    """
    _Nr, Jc = X_ref.shape

    # row-wise total scores (used for purified matching)
    tot_ref = X_ref.sum(axis=1).astype(np.float64)   # (N_ref,)
    tot_foc = X_foc.sum(axis=1).astype(np.float64)   # (N_foc,)

    cols = np.where(col_mask)[0] if col_mask is not None else np.arange(Jc)
    rows = []
    t0 = time.time()

    for pos, j in enumerate(cols):
        if pos % 2500 == 0 and pos > 0:
            print(f"    {pos}/{len(cols)}  ({time.time()-t0:.0f}s)")

        # ── purified scores: exclude item j from matching variable ──
        s_ref = tot_ref - X_ref[:, j].astype(np.float64)
        s_foc = tot_foc - X_foc[:, j].astype(np.float64)

        # ── quantile-based strata on pooled purified scores ──
        s_all = np.concatenate([s_ref, s_foc])
        edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))
        if len(edges) < 2:
            rows.append(_nan_row(j))
            continue
        n_bins = len(edges) - 1

        k_ref = np.digitize(s_ref, edges[1:-1])      # values in [0, n_bins-1]
        k_foc = np.digitize(s_foc, edges[1:-1])

        # ── accumulate MH statistics across strata ──
        #   α_MH = R / S  where  R = Σ A_k D_k / N_k,  S = Σ B_k C_k / N_k
        #   Δ_MH = −2.35 · ln(α_MH)
        R = S = 0.0
        sum_diff = 0.0       # Σ (A_k − E[A_k])
        sum_var  = 0.0       # Σ Var(A_k)
        # Robins-Breslow-Greenland variance components for ln(α_MH)
        pr = ps_qr = qs = 0.0
        n_ok = 0

        for k in range(n_bins):
            mr = (k_ref == k)
            mf = (k_foc == k)
            n1 = int(mr.sum())           # ref count in stratum
            n0 = int(mf.sum())           # foc count in stratum
            if n1 == 0 or n0 == 0:
                continue

            A = float(X_ref[mr, j].sum())   # ref correct
            B = float(n1 - A)               # ref incorrect
            C = float(X_foc[mf, j].sum())   # foc correct
            D = float(n0 - C)               # foc incorrect
            Nk = float(n1 + n0)
            m1 = A + C                       # total correct
            m0 = B + D                       # total incorrect

            if m1 == 0 or m0 == 0 or Nk <= 1:
                continue
            n_ok += 1

            Rk = A * D / Nk
            Sk = B * C / Nk
            R += Rk
            S += Sk

            # E[A_k] = n1·m1 / N_k
            EA = n1 * m1 / Nk
            sum_diff += A - EA
            # Var(A_k) = n1·n0·m1·m0 / (N_k²·(N_k−1))
            sum_var += n1 * n0 * m1 * m0 / (Nk * Nk * (Nk - 1))

            # RBG components: P_k = (A+D)/N, Q_k = (B+C)/N
            Pk = (A + D) / Nk
            Qk = (B + C) / Nk
            pr    += Pk * Rk
            ps_qr += Pk * Sk + Qk * Rk
            qs    += Qk * Sk

        if n_ok == 0 or (R == 0 and S == 0):
            rows.append(_nan_row(j))
            continue

        # ── MH odds ratio ──
        if S == 0:
            alpha, delta, se = np.inf, -np.inf, np.nan
        elif R == 0:
            alpha, delta, se = 0.0, np.inf, np.nan
        else:
            alpha = R / S
            delta = -2.35 * np.log(alpha)
            # SE via Robins-Breslow-Greenland:
            #   Var(ln α) = pr/(2R²) + ps_qr/(2RS) + qs/(2S²)
            v = pr / (2 * R * R) + ps_qr / (2 * R * S) + qs / (2 * S * S)
            se = 2.35 * np.sqrt(v) if v > 0 else np.nan

        # ── MH χ² with continuity correction (df=1) ──
        if sum_var > 0:
            chi2_stat = max(abs(sum_diff) - 0.5, 0) ** 2 / sum_var
            pval = 1 - chi2_dist.cdf(chi2_stat, df=1)
        else:
            chi2_stat = pval = np.nan

        # ── ETS classification ──
        #   A: |Δ| < 1.0
        #   C: |Δ| ≥ 1.5 AND p < 0.05
        #   B: everything else
        ad = abs(delta) if np.isfinite(delta) else 0.0
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


def _nan_row(j):
    return dict(col_idx=j, alpha_mh=np.nan, delta_mh=np.nan,
                se=np.nan, chi2=np.nan, p_value=np.nan, ets_class="A")


# ════════════════════════════════════════════════════════════════════════════
#  HELPERS
# ════════════════════════════════════════════════════════════════════════════
def rows_for(col, values):
    """Row indices into X for models matching model_meta[col] ∈ values."""
    names = model_meta.loc[model_meta[col].isin(values), "model_name"]
    return np.array([NAME2ROW[n] for n in names if n in NAME2ROW])


def enrich(df):
    """Attach item_id, subject, Li labels to DIF results (col_idx → item_id)."""
    df = df.copy()
    df["item_id"] = [ITEM_IDS[i] for i in df["col_idx"]]
    df = df.merge(item_meta[["item_id", "subject"]], on="item_id", how="left")
    df = df.merge(
        li_labels[["item_id", "is_contaminated", "contamination_type"]].rename(
            columns={"is_contaminated": "li_label",
                     "contamination_type": "li_contamination_type"}),
        on="item_id", how="left",
    )
    return df


def li_metrics(df):
    """FPR, contaminated rate, enrichment from enriched DIF results."""
    is_c   = df["ets_class"] == "C"
    clean  = df["li_contamination_type"] == "clean"
    contam = df["li_contamination_type"].isin(["input_only", "input_and_label"])
    unlab  = df["li_contamination_type"] == "no_annotation"

    r_clean  = is_c[clean].mean()  if clean.any()  else np.nan
    r_contam = is_c[contam].mean() if contam.any() else np.nan
    r_unlab  = is_c[unlab].mean()  if unlab.any()  else np.nan
    enrich   = r_contam / r_clean  if r_clean > 0  else np.nan

    return dict(fpr_vs_li_clean=r_clean, rate_contaminated=r_contam,
                rate_clean=r_clean, rate_unlabeled=r_unlab,
                enrichment_ratio=enrich)


def summary_row(cohort, filt, df):
    vc = df["ets_class"].value_counts()
    n  = len(df)
    lm = li_metrics(df)
    return dict(
        cohort_type=cohort, item_filter=filt, n_items=n,
        n_ets_a=vc.get("A", 0), n_ets_b=vc.get("B", 0), n_ets_c=vc.get("C", 0),
        pct_c=vc.get("C", 0) / n * 100 if n > 0 else 0,
        fpr_vs_li_clean=lm["fpr_vs_li_clean"],
        enrichment_ratio=lm["enrichment_ratio"],
    )


# ════════════════════════════════════════════════════════════════════════════
#  MAIN
# ════════════════════════════════════════════════════════════════════════════
def main():
    summary_rows = []

    # ── Step 1-2: MH-DIF — Temporal cohort ─────────────────────────────────
    print("\n=== Step 1-2a: Temporal cohort DIF (2023 vs 2024, 5 strata) ===")
    ref_t = rows_for("cohort_temporal", ["2023"])
    foc_t = rows_for("cohort_temporal", ["2024"])
    print(f"  N_ref={len(ref_t)}, N_foc={len(foc_t)}")

    dif_temp = mh_dif(X[ref_t], X[foc_t], n_strata=5)
    dif_temp = enrich(dif_temp)
    print(f"  ETS: {dif_temp.ets_class.value_counts().to_dict()}")
    summary_rows.append(summary_row("temporal", "all", dif_temp))

    # ── Step 1-2: MH-DIF — Ability cohort ──────────────────────────────────
    print("\n=== Step 1-2b: Ability cohort DIF (Q1-2 vs Q4-5, 10 strata) ===")
    ref_a = rows_for("cohort_accuracy_quintile", [1, 2])
    foc_a = rows_for("cohort_accuracy_quintile", [4, 5])
    print(f"  N_ref={len(ref_a)}, N_foc={len(foc_a)}")

    dif_abil = mh_dif(X[ref_a], X[foc_a], n_strata=10)
    dif_abil = enrich(dif_abil)
    print(f"  ETS: {dif_abil.ets_class.value_counts().to_dict()}")
    summary_rows.append(summary_row("ability", "all", dif_abil))

    # ── Step 3: Li et al. proxy validation ─────────────────────────────────
    print("\n=== Step 3: Li et al. proxy validation ===")
    li_t = li_metrics(dif_temp)
    li_a = li_metrics(dif_abil)
    print(f"  Temporal — FPR={li_t['fpr_vs_li_clean']:.4f}, "
          f"enrichment={li_t['enrichment_ratio']:.2f}")
    print(f"  Ability  — FPR={li_a['fpr_vs_li_clean']:.4f}, "
          f"enrichment={li_a['enrichment_ratio']:.2f}")

    # ── Step 4: Within-family analysis ─────────────────────────────────────
    print("\n=== Step 4: Within-family DIF ===")

    # Show family × temporal distribution
    fam_temp = (model_meta.groupby(["family", "cohort_temporal"])
                .size().unstack(fill_value=0))
    print("  Family × temporal counts:")
    for fam in ["llama-2", "llama-3", "mistral", "mixtral", "solar", "zephyr"]:
        if fam in fam_temp.index:
            print(f"    {fam}: {fam_temp.loc[fam].to_dict()}")

    family_pairs = []

    # (A) Cross-family comparisons (related families)
    llama2_idx = rows_for("family", ["llama-2"])
    llama3_idx = rows_for("family", ["llama-3"])
    if len(llama2_idx) >= 80 and len(llama3_idx) >= 80:
        family_pairs.append(("llama-2", "llama-3", llama2_idx, llama3_idx))

    mistral_idx = rows_for("family", ["mistral"])
    mixtral_idx = rows_for("family", ["mixtral"])
    if len(mistral_idx) >= 80 and len(mixtral_idx) >= 80:
        family_pairs.append(("mistral", "mixtral", mistral_idx, mixtral_idx))

    # (B) Within single family, temporal split (where both groups >= 40)
    for fam in ["unknown", "mistral", "llama-3", "llama-2"]:
        fam_df = model_meta[model_meta["family"] == fam]
        r_names = fam_df.loc[fam_df.cohort_temporal == "2023", "model_name"]
        f_names = fam_df.loc[fam_df.cohort_temporal == "2024", "model_name"]
        ri = np.array([NAME2ROW[n] for n in r_names if n in NAME2ROW])
        fi = np.array([NAME2ROW[n] for n in f_names if n in NAME2ROW])
        if len(ri) >= 40 and len(fi) >= 40:
            family_pairs.append((f"{fam}_2023", f"{fam}_2024", ri, fi))

    wf_parts = []
    for rname, fname, ri, fi in family_pairs:
        ns = 5 if min(len(ri), len(fi)) < 200 else 10
        print(f"  {rname} (N={len(ri)}) vs {fname} (N={len(fi)}), {ns} strata")
        wf = mh_dif(X[ri], X[fi], n_strata=ns)
        wf = enrich(wf)
        wf["ref_group"] = rname
        wf["foc_group"] = fname
        wf_parts.append(wf)
        print(f"    ETS: {wf.ets_class.value_counts().to_dict()}")

    wf_all = pd.concat(wf_parts, ignore_index=True) if wf_parts else pd.DataFrame()

    # Cross-cohort vs within-family comparison
    print("\n=== Step 4 cont: Cross analysis ===")
    cross_rows = []
    for rname, fname, _, _ in family_pairs:
        wf_sub = wf_all[(wf_all.ref_group == rname) & (wf_all.foc_group == fname)]
        for _, wr in wf_sub.iterrows():
            iid = wr["item_id"]
            tr = dif_temp.loc[dif_temp.item_id == iid]
            if tr.empty:
                continue
            tr = tr.iloc[0]
            cross_rows.append(dict(
                item_id=iid, subject=wr["subject"],
                temporal_ets=tr["ets_class"], temporal_delta=tr["delta_mh"],
                wf_pair=f"{rname}_vs_{fname}",
                wf_ets=wr["ets_class"], wf_delta=wr["delta_mh"],
                li_contamination_type=wr.get("li_contamination_type", np.nan),
            ))
    cross_df = pd.DataFrame(cross_rows)

    if not cross_df.empty:
        for pair in cross_df["wf_pair"].unique():
            sub = cross_df[cross_df.wf_pair == pair]
            tc = sub.temporal_ets == "C"
            wc = sub.wf_ets == "C"
            print(f"  {pair}: both_C={int((tc & wc).sum())}, "
                  f"temp_only_C={int((tc & ~wc).sum())}, "
                  f"wf_only_C={int((~tc & wc).sum())}, "
                  f"neither={int((~tc & ~wc).sum())}")

    # ── Step 5: Domain specificity ─────────────────────────────────────────
    print("\n=== Step 5: Domain specificity ===")

    # C rate per subject (temporal cohort)
    subj_c = (dif_temp.groupby("subject")["ets_class"]
              .agg(n_items="size", n_ets_c=lambda x: (x == "C").sum()))
    subj_c["pct_c"] = subj_c["n_ets_c"] / subj_c["n_items"] * 100

    # Per-item accuracy for 2023 and 2024 models
    acc_2023 = X[ref_t].mean(axis=0).astype(np.float64)   # (J,)
    acc_2024 = X[foc_t].mean(axis=0).astype(np.float64)

    item_acc = pd.DataFrame({"item_id": ITEM_IDS, "acc_2023": acc_2023, "acc_2024": acc_2024})
    item_acc = item_acc.merge(item_meta[["item_id", "subject"]], on="item_id")
    subj_acc = item_acc.groupby("subject")[["acc_2023", "acc_2024"]].mean()
    subj_acc["acc_change"] = subj_acc["acc_2024"] - subj_acc["acc_2023"]

    domain_df = subj_c.join(subj_acc, how="inner")
    rho, rho_p = spearmanr(domain_df["pct_c"], domain_df["acc_change"])
    print(f"  Spearman(pct_C, acc_change) = {rho:.3f}, p = {rho_p:.4f}")
    print("  Top 5 by C rate:")
    for subj, row in domain_df.nlargest(5, "pct_c").iterrows():
        print(f"    {subj}: {row.pct_c:.1f}% C ({int(row.n_ets_c)}/{int(row.n_items)}), "
              f"Δacc={row.acc_change:+.3f}")

    # ── Step 6: Negative-discrimination sensitivity ────────────────────────
    print("\n=== Step 6: Negative-disc sensitivity ===")
    neg_mask = item_meta.set_index("item_id").reindex(ITEM_IDS)["is_negative_disc"].values
    pos_mask = ~neg_mask
    n_neg = int(neg_mask.sum())
    n_pos = int(pos_mask.sum())
    print(f"  All={J}, neg_disc={n_neg}, non_neg={n_pos}")

    # Re-run temporal DIF on non-negative-disc items only
    # (total scores also computed only on non-neg items)
    pos_cols = np.where(pos_mask)[0]
    dif_temp_nn = mh_dif(X[np.ix_(ref_t, pos_cols)],
                         X[np.ix_(foc_t, pos_cols)], n_strata=5)

    # Map col_idx back to original item space
    dif_temp_nn["col_idx_orig"] = [pos_cols[c] for c in dif_temp_nn["col_idx"]]
    dif_temp_nn["item_id"] = [ITEM_IDS[pos_cols[c]] for c in dif_temp_nn["col_idx"]]
    dif_temp_nn = dif_temp_nn.merge(
        li_labels[["item_id", "is_contaminated", "contamination_type"]].rename(
            columns={"is_contaminated": "li_label",
                     "contamination_type": "li_contamination_type"}),
        on="item_id", how="left",
    )

    n_c_all = int((dif_temp["ets_class"] == "C").sum())
    n_c_nn  = int((dif_temp_nn["ets_class"] == "C").sum())
    # C count among neg-disc items in the full run
    neg_col_set = set(np.where(neg_mask)[0])
    n_c_neg = int((dif_temp.loc[dif_temp.col_idx.isin(neg_col_set), "ets_class"] == "C").sum())

    neg_disc_df = pd.DataFrame([
        dict(item_set="all",               n_items=J,     n_ets_c=n_c_all,
             pct_c=n_c_all / J * 100),
        dict(item_set="non_negative_disc",  n_items=n_pos, n_ets_c=n_c_nn,
             pct_c=n_c_nn / n_pos * 100),
        dict(item_set="negative_disc_only", n_items=n_neg, n_ets_c=n_c_neg,
             pct_c=n_c_neg / n_neg * 100 if n_neg > 0 else 0),
    ])
    print(neg_disc_df.to_string(index=False))

    summary_rows.append(summary_row("temporal", "non_neg_disc", dif_temp_nn))

    # ── Sanity check: random half-split of 2023 cohort ─────────────────────
    print("\n=== Sanity check: random half-split of 2023 cohort ===")
    rng = np.random.RandomState(42)
    perm = rng.permutation(len(ref_t))
    half = len(perm) // 2
    san_ref = ref_t[perm[:half]]
    san_foc = ref_t[perm[half:]]
    print(f"  Split: {len(san_ref)} vs {len(san_foc)}")
    dif_san = mh_dif(X[san_ref], X[san_foc], n_strata=5)
    vc_san = dif_san["ets_class"].value_counts()
    n_c_san = vc_san.get("C", 0)
    pct_c_san = n_c_san / len(dif_san) * 100
    print(f"  ETS C: {n_c_san}/{len(dif_san)} = {pct_c_san:.2f}% (expect <5%)")

    # ── Save all outputs ───────────────────────────────────────────────────
    print("\n=== Saving outputs ===")

    out_cols = ["item_id", "subject", "alpha_mh", "delta_mh", "se",
                "p_value", "ets_class", "li_label", "li_contamination_type"]
    dif_temp[out_cols].to_csv(OUT / "dif_results_temporal.csv", index=False)
    dif_abil[out_cols].to_csv(OUT / "dif_results_ability.csv", index=False)

    summary_df = pd.DataFrame(summary_rows)
    summary_df.to_csv(OUT / "dif_summary.csv", index=False)

    if not wf_all.empty:
        wf_cols = ["item_id", "subject", "ref_group", "foc_group",
                   "alpha_mh", "delta_mh", "se", "p_value", "ets_class",
                   "li_label", "li_contamination_type"]
        wf_all[[c for c in wf_cols if c in wf_all.columns]].to_csv(
            OUT / "within_family_dif.csv", index=False)

    if not cross_df.empty:
        cross_df.to_csv(OUT / "cross_analysis.csv", index=False)

    domain_df.reset_index().to_csv(OUT / "domain_specificity.csv", index=False)
    neg_disc_df.to_csv(OUT / "neg_disc_sensitivity.csv", index=False)

    # ── Cohort overlap ─────────────────────────────────────────────────────
    temp_c = set(dif_temp.loc[dif_temp.ets_class == "C", "item_id"])
    abil_c = set(dif_abil.loc[dif_abil.ets_class == "C", "item_id"])
    overlap = temp_c & abil_c
    union   = temp_c | abil_c
    jaccard = len(overlap) / len(union) if union else 0

    # ── Console summary ────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"\nTemporal (2023 vs 2024, 5 strata):")
    print(f"  ETS: {dif_temp.ets_class.value_counts().to_dict()}")
    print(f"  FPR vs Li clean = {li_t['fpr_vs_li_clean']:.4f}")
    print(f"  Enrichment = {li_t['enrichment_ratio']:.2f}")
    print(f"\nAbility (Q1-2 vs Q4-5, 10 strata):")
    print(f"  ETS: {dif_abil.ets_class.value_counts().to_dict()}")
    print(f"  FPR vs Li clean = {li_a['fpr_vs_li_clean']:.4f}")
    print(f"  Enrichment = {li_a['enrichment_ratio']:.2f}")
    print(f"\nSanity check (random split): {pct_c_san:.2f}% C")
    print(f"Domain ρ(C_rate, Δacc) = {rho:.3f}, p = {rho_p:.4f}")
    print(f"Cohort overlap: temp_C={len(temp_c)}, abil_C={len(abil_c)}, "
          f"both={len(overlap)}, Jaccard={jaccard:.3f}")

    # ── Generate report ────────────────────────────────────────────────────
    _write_report(dif_temp, dif_abil, li_t, li_a, summary_df,
                  domain_df, rho, rho_p, neg_disc_df, pct_c_san,
                  wf_all, cross_df, temp_c, abil_c, overlap, jaccard,
                  ref_t, foc_t, ref_a, foc_a)

    print(f"\nAll outputs saved to {OUT}")


# ════════════════════════════════════════════════════════════════════════════
#  REPORT
# ════════════════════════════════════════════════════════════════════════════
def _write_report(dif_temp, dif_abil, li_t, li_a, summary_df,
                  domain_df, rho, rho_p, neg_disc_df, pct_san,
                  wf_all, cross_df, temp_c, abil_c, overlap, jaccard,
                  ref_t, foc_t, ref_a, foc_a):
    L = []
    def w(s=""):
        L.append(s)

    w("# Plan 001: METABENCH Real-Data MH-DIF Analysis")
    w()
    w("## 1. Data & Setup")
    w()
    w(f"- Response matrix: **{N_MODELS} models × {J} items** (binary, MMLU)")
    w(f"- Temporal cohort: ref = 2023 (N={len(ref_t)}), foc = 2024 (N={len(foc_t)}), 5 strata")
    w(f"- Ability cohort: ref = Q1-2 (N={len(ref_a)}), foc = Q4-5 (N={len(foc_a)}), 10 strata")
    w(f"- Li et al. annotations: {(li_labels.contamination_type != 'no_annotation').sum()} annotated items")
    w()

    w("## 2. ETS Classification")
    w()
    w("| Cohort | Filter | Items | A | B | C | %C | FPR (clean) | Enrichment |")
    w("|--------|--------|-------|---|---|---|----|-------------|------------|")
    for _, r in summary_df.iterrows():
        w(f"| {r.cohort_type} | {r.item_filter} | {r.n_items} | "
          f"{r.n_ets_a} | {r.n_ets_b} | {r.n_ets_c} | {r.pct_c:.2f}% | "
          f"{r.fpr_vs_li_clean:.4f} | {r.enrichment_ratio:.2f} |")
    w()

    w("## 3. Li et al. Proxy Validation")
    w()
    w("| Cohort | FPR (clean) | Rate (contam) | Rate (clean) | Rate (unlabeled) | Enrichment |")
    w("|--------|-------------|---------------|--------------|------------------|------------|")
    for name, lm in [("temporal", li_t), ("ability", li_a)]:
        w(f"| {name} | {lm['fpr_vs_li_clean']:.4f} | "
          f"{lm['rate_contaminated']:.4f} | {lm['rate_clean']:.4f} | "
          f"{lm['rate_unlabeled']:.4f} | {lm['enrichment_ratio']:.2f} |")
    w()

    w("## 4. Within-Family Analysis")
    w()
    if not wf_all.empty:
        for (rn, fn), sub in wf_all.groupby(["ref_group", "foc_group"]):
            vc = sub.ets_class.value_counts()
            nc = vc.get("C", 0)
            w(f"- **{rn} vs {fn}**: A={vc.get('A',0)}, B={vc.get('B',0)}, "
              f"C={nc} ({nc/len(sub)*100:.2f}%)")
        w()
        if not cross_df.empty:
            w("### Cross-cohort vs within-family overlap")
            w()
            for pair in cross_df.wf_pair.unique():
                s = cross_df[cross_df.wf_pair == pair]
                tc = s.temporal_ets == "C"
                wc = s.wf_ets == "C"
                w(f"- **{pair}**: both_C={int((tc&wc).sum())}, "
                  f"temp_only_C={int((tc&~wc).sum())}, "
                  f"wf_only_C={int((~tc&wc).sum())}")
            w()
    else:
        w("No within-family pairs with sufficient N found.")
        w()

    w("## 5. Domain Specificity")
    w()
    w(f"Spearman ρ(C_rate, Δacc) = **{rho:.3f}** (p = {rho_p:.4f})")
    w()
    w("Top 15 subjects by C rate (temporal cohort):")
    w()
    w("| Subject | Items | C | %C | Acc 2023 | Acc 2024 | ΔAcc |")
    w("|---------|-------|---|-----|----------|----------|------|")
    for subj, row in domain_df.nlargest(15, "pct_c").iterrows():
        w(f"| {subj} | {int(row.n_items)} | {int(row.n_ets_c)} | "
          f"{row.pct_c:.1f}% | {row.acc_2023:.3f} | {row.acc_2024:.3f} | "
          f"{row.acc_change:+.3f} |")
    w()

    w("## 6. Negative-Discrimination Sensitivity")
    w()
    w("| Item Set | Items | C | %C |")
    w("|----------|-------|---|----|")
    for _, r in neg_disc_df.iterrows():
        w(f"| {r.item_set} | {int(r.n_items)} | {int(r.n_ets_c)} | {r.pct_c:.2f}% |")
    w()

    w("## 7. Sanity Check")
    w()
    w(f"Random half-split of 2023 cohort: **{pct_san:.2f}% C** (expect < 5%)")
    w()

    w("## 8. Cohort Overlap")
    w()
    w(f"- Temporal C: {len(temp_c)} items")
    w(f"- Ability C: {len(abil_c)} items")
    w(f"- Both C: {len(overlap)} items")
    w(f"- Jaccard index: {jaccard:.3f}")

    (OUT / "plan_001_report.md").write_text("\n".join(L) + "\n")
    print("  Report written.")


if __name__ == "__main__":
    main()
