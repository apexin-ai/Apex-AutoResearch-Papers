# plan_001b_analysis.py
# Matched-Ability DIF: temporal DIF within accuracy quintiles to isolate contamination from ability gain.
# Input:  response_matrix.npz, response_matrix_index.npz, model_metadata.csv, item_metadata.csv, mmlu_li2024_proxy_labels.csv
# Output: quintile_cohort_sizes.csv, dif_results_per_quintile.csv, dif_results_merged.csv, enrichment_summary.csv, plan_001b_report.md

import numpy as np
import pandas as pd
import scipy.sparse as sp
from scipy.stats import chi2
from pathlib import Path
import time

BASE = Path("/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts")
OUT = BASE / "plan_001b"
OUT.mkdir(exist_ok=True)

# ── Load data ──────────────────────────────────────────────────────────────────
print("Loading data...")
idx = np.load(BASE / "response_matrix_index.npz", allow_pickle=True)
model_names = idx["model_names"]
item_ids = idx["item_ids"]

resp = sp.load_npz(BASE / "response_matrix.npz").toarray()  # (5227, 12508) uint8
model_meta = pd.read_csv(BASE / "model_metadata.csv")
item_meta = pd.read_csv(BASE / "item_metadata.csv")
li_labels = pd.read_csv(BASE / "mmlu_li2024_proxy_labels.csv")

assert (model_names == model_meta["model_name"].values).all()
assert (item_ids == item_meta["item_id"].values).all()
n_models, n_items = resp.shape
print(f"Matrix: {n_models}×{n_items}  |  2023={int((model_meta.cohort_temporal=='2023').sum())}  2024={int((model_meta.cohort_temporal=='2024').sum())}")


# ── MH-DIF engine ─────────────────────────────────────────────────────────────
def mh_dif_all_items(resp_ref, resp_foc, n_strata=5):
    """Purified MH-DIF for every item. Returns (n_items, 5) array: alpha, delta, chi2, pval, ets_code."""
    nr = resp_ref.shape[0]
    nf = resp_foc.shape[0]
    ni = resp_ref.shape[1]

    total_ref = resp_ref.sum(axis=1).astype(np.float64)
    total_foc = resp_foc.sum(axis=1).astype(np.float64)

    alphas = np.full(ni, np.nan)
    deltas = np.full(ni, np.nan)
    chi2s = np.full(ni, np.nan)
    pvals = np.full(ni, np.nan)
    ets = np.full(ni, 0, dtype=np.int8)  # 0=A, 1=B, 2=C

    pct_edges = np.linspace(0, 100, n_strata + 1)

    for j in range(ni):
        yr = resp_ref[:, j].astype(np.float64)
        yf = resp_foc[:, j].astype(np.float64)
        sr = total_ref - yr
        sf = total_foc - yf

        all_s = np.concatenate([sr, sf])
        edges = np.unique(np.percentile(all_s, pct_edges))
        if len(edges) < 3:
            continue

        br = np.digitize(sr, edges[1:-1])
        bf = np.digitize(sf, edges[1:-1])

        num = den = mh_n = mh_v = 0.0
        for k in range(len(edges) - 1):
            rm = br == k
            fm = bf == k
            A = float(yr[rm].sum())
            n1 = float(rm.sum())
            B = n1 - A
            C = float(yf[fm].sum())
            n2 = float(fm.sum())
            D = n2 - C
            N = n1 + n2
            if N < 2:
                continue
            num += A * D / N
            den += B * C / N
            m1 = A + C
            m0 = B + D
            mh_n += A - n1 * m1 / N
            mh_v += n1 * n2 * m1 * m0 / (N * N * (N - 1))

        if num == 0 or den == 0:
            continue

        a = num / den
        d = -2.35 * np.log(a)
        alphas[j] = a
        deltas[j] = d

        if mh_v > 0:
            c2 = (abs(mh_n) - 0.5) ** 2 / mh_v
            p = 1.0 - chi2.cdf(c2, 1)
            chi2s[j] = c2
            pvals[j] = p
        else:
            p = np.nan

        ad = abs(d)
        if ad < 1.0:
            ets[j] = 0
        elif ad < 1.5:
            ets[j] = 1
        elif np.isnan(p) or p >= 0.05:
            ets[j] = 1
        else:
            ets[j] = 2

    return alphas, deltas, chi2s, pvals, ets

ETS_MAP = {0: "A", 1: "B", 2: "C"}


# ── Step 1: Quintile × temporal cross-tab ──────────────────────────────────────
print("\n─── Step 1: Quintile cohort sizes ───")
cohort_rows = []
quintile_data = {}  # q -> (resp_ref, resp_foc, n_strata)

for q in range(1, 6):
    qm = model_meta["cohort_accuracy_quintile"].values == q
    ref = qm & (model_meta["cohort_temporal"].values == "2023")
    foc = qm & (model_meta["cohort_temporal"].values == "2024")
    nr, nf = int(ref.sum()), int(foc.sum())
    up = nr < 40 or nf < 40
    cohort_rows.append(dict(quintile=q, n_2023=nr, n_2024=nf, n_total=nr + nf, underpowered=up))
    print(f"  Q{q}: 2023={nr}  2024={nf}  {'UNDERPOWERED' if up else ''}")
    if nr >= 10 and nf >= 10:
        ns = 5 if (nr + nf) >= 200 else 3
        quintile_data[q] = (resp[ref], resp[foc], ns)

cohort_df = pd.DataFrame(cohort_rows)
cohort_df.to_csv(OUT / "quintile_cohort_sizes.csv", index=False)


# ── Step 2: Per-quintile MH-DIF ───────────────────────────────────────────────
print("\n─── Step 2: MH-DIF per quintile ───")
per_q_results = {}  # q -> (alphas, deltas, chi2s, pvals, ets)

for q in sorted(quintile_data):
    rr, rf, ns = quintile_data[q]
    t0 = time.time()
    res = mh_dif_all_items(rr, rf, ns)
    dt = time.time() - t0
    per_q_results[q] = res
    ets_counts = {v: int((res[4] == k).sum()) for k, v in ETS_MAP.items()}
    print(f"  Q{q}: A={ets_counts['A']}  B={ets_counts['B']}  C={ets_counts['C']}  ({dt:.1f}s)")

# Save per-quintile detail
rows = []
for q, (alphas, deltas, chi2s, pvals, ets_arr) in per_q_results.items():
    info = cohort_rows[q - 1]
    for j in range(n_items):
        rows.append(dict(
            item_id=item_ids[j], quintile=q,
            n_ref=info["n_2023"], n_foc=info["n_2024"], n_strata=quintile_data[q][2],
            alpha_mh=alphas[j], delta_mh=deltas[j],
            chi2_mh=chi2s[j], p_value=pvals[j],
            ets_class=ETS_MAP[ets_arr[j]],
        ))
per_q_df = pd.DataFrame(rows)
per_q_df.to_csv(OUT / "dif_results_per_quintile.csv", index=False)
print(f"  Saved {len(per_q_df)} rows")


# ── Step 3: Merge across quintiles ─────────────────────────────────────────────
print("\n─── Step 3: Merge across quintiles ───")
tested_qs = sorted(per_q_results.keys())

merged = pd.DataFrame({"item_id": item_ids})
for q in tested_qs:
    alphas, deltas, chi2s, pvals, ets_arr = per_q_results[q]
    merged[f"ets_q{q}"] = [ETS_MAP[e] for e in ets_arr]
    merged[f"delta_q{q}"] = deltas

merged["n_quintiles_c"] = sum((merged[f"ets_q{q}"] == "C").astype(int) for q in tested_qs)
merged["n_quintiles_tested"] = len(tested_qs)
merged["overall_c"] = merged["n_quintiles_c"] >= 2

merged = merged.merge(item_meta[["item_id", "subject", "ctt_difficulty", "ctt_discrimination"]], on="item_id", how="left")
merged = merged.merge(li_labels[["item_id", "is_contaminated", "contamination_type", "similarity_score"]], on="item_id", how="left")

print(f"  overall_c (≥2 quintiles): {merged['overall_c'].sum()} / {len(merged)} ({merged['overall_c'].mean()*100:.1f}%)")


# ── Step 4: Li et al. proxy validation ─────────────────────────────────────────
print("\n─── Step 4: Li et al. proxy validation ───")
clean = merged["contamination_type"] == "clean"
contam = merged["contamination_type"].isin(["input_only", "input_and_label"])
unlabeled = merged["contamination_type"] == "no_annotation"

fpr = merged.loc[clean, "overall_c"].mean()
rate_contam = merged.loc[contam, "overall_c"].mean()
rate_unlabeled = merged.loc[unlabeled, "overall_c"].mean()
enrichment = rate_contam / fpr if fpr > 0 else np.nan

print(f"  FPR (clean):        {fpr:.4f}  ({int(merged.loc[clean, 'overall_c'].sum())}/{int(clean.sum())})")
print(f"  Rate (contaminated):{rate_contam:.4f}  ({int(merged.loc[contam, 'overall_c'].sum())}/{int(contam.sum())})")
print(f"  Rate (unlabeled):   {rate_unlabeled:.4f}  ({int(merged.loc[unlabeled, 'overall_c'].sum())}/{int(unlabeled.sum())})")
print(f"  Enrichment:         {enrichment:.2f}")

per_q_enrichment = []
print("\n  Per-quintile:")
for q in tested_qs:
    col = f"ets_q{q}"
    is_c = merged[col] == "C"
    fpr_q = merged.loc[clean, col].eq("C").mean()
    rate_q = merged.loc[contam, col].eq("C").mean()
    enr_q = rate_q / fpr_q if fpr_q > 0 else np.nan
    per_q_enrichment.append(dict(quintile=q, n_c=int(is_c.sum()), pct_c=is_c.mean() * 100, fpr=fpr_q, rate_contaminated=rate_q, enrichment=enr_q))
    print(f"    Q{q}: C={int(is_c.sum())} ({is_c.mean()*100:.1f}%)  FPR={fpr_q:.4f}  enrichment={enr_q:.2f}")


# ── Step 5: Compare with plan_001 ─────────────────────────────────────────────
print("\n─── Step 5: Comparison with plan_001 ───")
print(f"  plan_001 (raw temporal):    C%=31.3%  enrichment=0.96")
print(f"  plan_001b (matched-ability):C%={merged['overall_c'].mean()*100:.1f}%  enrichment={enrichment:.2f}")
print(f"  Improvement factor: {enrichment / 0.96:.2f}x")


# ── Step 6: Sensitivity + CMH ─────────────────────────────────────────────────
print("\n─── Step 6: Sensitivity analysis ───")
sensitivity = []
for thresh in [1, 2, 3]:
    flag = merged["n_quintiles_c"] >= thresh
    n_c = int(flag.sum())
    pct_c = flag.mean() * 100
    fpr_t = merged.loc[clean, "n_quintiles_c"].ge(thresh).mean()
    rate_t = merged.loc[contam, "n_quintiles_c"].ge(thresh).mean()
    enr_t = rate_t / fpr_t if fpr_t > 0 else np.nan
    sensitivity.append(dict(threshold=f">=  {thresh}", n_c=n_c, pct_c=pct_c, fpr=fpr_t, rate_contaminated=rate_t, enrichment=enr_t))
    print(f"  ≥{thresh}: C={n_c} ({pct_c:.1f}%)  FPR={fpr_t:.4f}  enrichment={enr_t:.2f}")

# CMH: pool strata across quintiles
print("\n  CMH (pooled across quintiles)...")
t0 = time.time()

cmh_alphas = np.full(n_items, np.nan)
cmh_deltas = np.full(n_items, np.nan)
cmh_chi2s = np.full(n_items, np.nan)
cmh_pvals = np.full(n_items, np.nan)
cmh_ets = np.full(n_items, 0, dtype=np.int8)

# Precompute totals per quintile
q_totals = {}
for q, (rr, rf, ns) in quintile_data.items():
    q_totals[q] = (rr.sum(axis=1).astype(np.float64), rf.sum(axis=1).astype(np.float64))

for j in range(n_items):
    num = den = mh_n = mh_v = 0.0

    for q, (rr, rf, ns) in quintile_data.items():
        tr, tf = q_totals[q]
        yr = rr[:, j].astype(np.float64)
        yf = rf[:, j].astype(np.float64)
        sr = tr - yr
        sf = tf - yf

        all_s = np.concatenate([sr, sf])
        edges = np.unique(np.percentile(all_s, np.linspace(0, 100, ns + 1)))
        if len(edges) < 3:
            continue
        br = np.digitize(sr, edges[1:-1])
        bf = np.digitize(sf, edges[1:-1])

        for k in range(len(edges) - 1):
            rm = br == k
            fm = bf == k
            A = float(yr[rm].sum())
            n1 = float(rm.sum())
            B = n1 - A
            C = float(yf[fm].sum())
            n2 = float(fm.sum())
            D = n2 - C
            N = n1 + n2
            if N < 2:
                continue
            num += A * D / N
            den += B * C / N
            m1 = A + C
            m0 = B + D
            mh_n += A - n1 * m1 / N
            mh_v += n1 * n2 * m1 * m0 / (N * N * (N - 1))

    if num == 0 or den == 0:
        continue
    a = num / den
    d = -2.35 * np.log(a)
    cmh_alphas[j] = a
    cmh_deltas[j] = d
    if mh_v > 0:
        c2 = (abs(mh_n) - 0.5) ** 2 / mh_v
        p = 1.0 - chi2.cdf(c2, 1)
        cmh_chi2s[j] = c2
        cmh_pvals[j] = p
    else:
        p = np.nan
    ad = abs(d)
    if ad < 1.0:
        cmh_ets[j] = 0
    elif ad < 1.5:
        cmh_ets[j] = 1
    elif np.isnan(p) or p >= 0.05:
        cmh_ets[j] = 1
    else:
        cmh_ets[j] = 2

    if (j + 1) % 3000 == 0:
        print(f"    CMH {j+1}/{n_items}...")

dt = time.time() - t0
cmh_labels = np.array([ETS_MAP[e] for e in cmh_ets])
cmh_counts = {v: int((cmh_ets == k).sum()) for k, v in ETS_MAP.items()}
print(f"  CMH: A={cmh_counts['A']}  B={cmh_counts['B']}  C={cmh_counts['C']}  ({dt:.1f}s)")

merged["cmh_alpha"] = cmh_alphas
merged["cmh_delta"] = cmh_deltas
merged["cmh_chi2"] = cmh_chi2s
merged["cmh_pvalue"] = cmh_pvals
merged["cmh_ets"] = cmh_labels

cmh_fpr = merged.loc[clean, "cmh_ets"].eq("C").mean()
cmh_rate = merged.loc[contam, "cmh_ets"].eq("C").mean()
cmh_enr = cmh_rate / cmh_fpr if cmh_fpr > 0 else np.nan
print(f"  CMH enrichment: FPR={cmh_fpr:.4f}  rate={cmh_rate:.4f}  enrichment={cmh_enr:.2f}")

sensitivity.append(dict(threshold="CMH", n_c=cmh_counts["C"], pct_c=cmh_counts["C"] / n_items * 100,
                        fpr=cmh_fpr, rate_contaminated=cmh_rate, enrichment=cmh_enr))

for pqe in per_q_enrichment:
    sensitivity.append(dict(threshold=f"Q{pqe['quintile']}_only", **{k: pqe[k] for k in ["n_c", "pct_c", "fpr", "rate_contaminated", "enrichment"]}))

sens_df = pd.DataFrame(sensitivity)
sens_df.to_csv(OUT / "enrichment_summary.csv", index=False)
merged.to_csv(OUT / "dif_results_merged.csv", index=False)


# ── Report ─────────────────────────────────────────────────────────────────────
print("\n─── Generating report ───")

report_lines = [
    "# Plan 001b: Matched-Ability DIF Analysis",
    "",
    "## Background",
    "plan_001 found temporal cohort MH-DIF (2023 vs 2024) produced 31.3% ETS C items but enrichment=0.96,",
    "indicating DIF captured ability improvement rather than contamination. This analysis controls for",
    "ability by running temporal DIF within each accuracy quintile.",
    "",
    "## Quintile Cohort Sizes",
    "",
    "| Quintile | N(2023) | N(2024) | Total | Underpowered |",
    "|----------|---------|---------|-------|--------------|",
]
for _, r in cohort_df.iterrows():
    report_lines.append(f"| {int(r['quintile'])} | {int(r['n_2023'])} | {int(r['n_2024'])} | {int(r['n_total'])} | {'YES' if r['underpowered'] else 'no'} |")

report_lines += ["", "## Per-Quintile DIF Results", ""]
for pqe in per_q_enrichment:
    report_lines.append(f"- **Q{pqe['quintile']}**: {pqe['n_c']} C items ({pqe['pct_c']:.1f}%), FPR={pqe['fpr']:.4f}, enrichment={pqe['enrichment']:.2f}")

report_lines += [
    "",
    "## Merged Results (threshold: ≥2 quintiles flagged C)",
    "",
    f"- Items flagged: {merged['overall_c'].sum()} / {len(merged)} ({merged['overall_c'].mean()*100:.1f}%)",
    f"- FPR (clean items): {fpr:.4f}",
    f"- Detection rate (contaminated): {rate_contam:.4f}",
    f"- Detection rate (unlabeled): {rate_unlabeled:.4f}",
    f"- **Enrichment: {enrichment:.2f}**",
    "",
    "## Comparison with plan_001",
    "",
    "| Metric | plan_001 (raw temporal) | plan_001b (matched-ability) |",
    "|--------|------------------------|-----------------------------|",
    f"| C% | 31.3% | {merged['overall_c'].mean()*100:.1f}% |",
    f"| Enrichment | 0.96 | {enrichment:.2f} |",
    f"| FPR | ~0.31 | {fpr:.4f} |",
    "",
    "## Sensitivity Analysis",
    "",
    "| Method | N(C) | C% | FPR | Rate(contam) | Enrichment |",
    "|--------|------|----|-----|-------------|------------|",
]
for _, r in sens_df.iterrows():
    report_lines.append(f"| {r['threshold']} | {int(r['n_c'])} | {r['pct_c']:.1f}% | {r['fpr']:.4f} | {r['rate_contaminated']:.4f} | {r['enrichment']:.2f} |")

success = enrichment > 1.5 and fpr < 0.10
report_lines += [
    "",
    "## Verdict",
    "",
    f"- Enrichment {'>' if enrichment > 1.5 else '≤'} 1.5: {'PASS' if enrichment > 1.5 else 'FAIL'}",
    f"- FPR {'<' if fpr < 0.10 else '≥'} 0.10: {'PASS' if fpr < 0.10 else 'FAIL'}",
    f"- **Overall: {'SUCCESS' if success else 'FAILURE'}**",
]

report = "\n".join(report_lines) + "\n"
(OUT / "plan_001b_report.md").write_text(report)
print(report)

# ── Sanity checks ──────────────────────────────────────────────────────────────
print("\n─── Sanity checks ───")
print(f"  Response matrix density: {resp.sum() / resp.size:.3f}")
print(f"  Items with any NaN delta across quintiles: {merged[[f'delta_q{q}' for q in tested_qs]].isna().any(axis=1).sum()}")
print(f"  CMH NaN deltas: {np.isnan(cmh_deltas).sum()}")
for q in tested_qs:
    col = f"delta_q{q}"
    vals = merged[col].dropna()
    print(f"  Q{q} delta range: [{vals.min():.2f}, {vals.max():.2f}], median={vals.median():.2f}")

print(f"\nOutput: {OUT}")
for f in sorted(OUT.iterdir()):
    if f.name != "__pycache__":
        print(f"  {f.name}  ({f.stat().st_size / 1024:.0f} KB)")
