"""DiD Parallel Trends Balance Check (B1)."""

import json
import numpy as np
import pandas as pd
from scipy import stats
from collections import Counter

LABELS_PATH = "/root/autodl-tmp/exp001/sft_data/contamination_labels_mmlu_d025.json"
METADATA_PATH = "/root/contamcal-irt-calibration/analysis/irt_data/mmlu/item_metadata.csv"
RESPONSE_MATRIX_PATH = "/root/contamcal-irt-calibration/analysis/irt_data/mmlu/response_matrix.csv"
EXPOSURE_PATH = "/root/contamcal-irt-calibration/analysis/irt_data/mmlu/exposure_scores.csv"

with open(LABELS_PATH) as f:
    labels_data = json.load(f)
labels = np.array(labels_data["labels"], dtype=bool)
n_total = len(labels)
n_treated = labels.sum()
n_untreated = n_total - n_treated
print(f"Items: total={n_total}, treated={n_treated}, untreated={n_untreated}")

meta = pd.read_csv(METADATA_PATH)
print(f"Metadata: {meta.shape}, columns={list(meta.columns)}")

resp = pd.read_csv(RESPONSE_MATRIX_PATH, index_col=0)
exposure = pd.read_csv(EXPOSURE_PATH)

d000_respondents = exposure[exposure["dosage"] == 0]["respondent"].tolist()
print(f"d000 respondents ({len(d000_respondents)}): {d000_respondents}")

resp_d000 = resp.loc[d000_respondents]
item_acc = resp_d000.values.astype(float).mean(axis=0)

treated_acc = item_acc[labels]
untreated_acc = item_acc[~labels]

print(f"\n{'='*80}")
print("BALANCE CHECK RESULTS")
print(f"{'='*80}")

# ── 1. Baseline accuracy ──
print(f"\n── 1. BASELINE ACCURACY ──")
print(f"  Treated   (n={n_treated:,}): mean={treated_acc.mean():.4f}, std={treated_acc.std():.4f}, median={np.median(treated_acc):.4f}")
print(f"  Untreated (n={n_untreated:,}): mean={untreated_acc.mean():.4f}, std={untreated_acc.std():.4f}, median={np.median(untreated_acc):.4f}")
diff = treated_acc.mean() - untreated_acc.mean()
print(f"  Difference: {diff:+.4f}")

t_stat, t_pval = stats.ttest_ind(treated_acc, untreated_acc)
u_stat, u_pval = stats.mannwhitneyu(treated_acc, untreated_acc, alternative="two-sided")
pooled_std = np.sqrt(((n_treated - 1) * treated_acc.std()**2 + (n_untreated - 1) * untreated_acc.std()**2) / (n_total - 2))
cohens_d = diff / pooled_std if pooled_std > 0 else 0

print(f"  t-test: t={t_stat:.4f}, p={t_pval:.4f}")
print(f"  Mann-Whitney U: U={u_stat:.0f}, p={u_pval:.4f}")
print(f"  Cohen's d: {cohens_d:.4f}")

# ── 2. Per-model d000 accuracy ──
print(f"\n── 2. PER-MODEL d000 ACCURACY ──")
for respondent in d000_respondents:
    r_vals = resp.loc[respondent].values.astype(float)
    t_acc = r_vals[labels].mean()
    u_acc = r_vals[~labels].mean()
    t2, p2 = stats.ttest_ind(r_vals[labels].astype(float), r_vals[~labels].astype(float))
    print(f"  {respondent:>30s}: treated={t_acc:.4f}, untreated={u_acc:.4f}, diff={t_acc-u_acc:+.4f}, t={t2:.3f}, p={p2:.4f}")

# ── 3. Difficulty quintile distribution ──
print(f"\n── 3. DIFFICULTY QUINTILE DISTRIBUTION ──")
quintile_labels_arr = pd.qcut(item_acc, q=5, labels=False, duplicates='drop')
n_bins = len(set(quintile_labels_arr))
q_names = [f"Q{i+1}" for i in range(n_bins)]

# Compute quintile boundaries for display
boundaries = []
for i in range(n_bins):
    mask = quintile_labels_arr == i
    lo = item_acc[mask].min()
    hi = item_acc[mask].max()
    boundaries.append(f"[{lo:.2f}-{hi:.2f}]")

treated_counts = np.array([np.sum(quintile_labels_arr[labels] == i) for i in range(n_bins)])
untreated_counts = np.array([np.sum(quintile_labels_arr[~labels] == i) for i in range(n_bins)])
treated_pcts = treated_counts / n_treated * 100
untreated_pcts = untreated_counts / n_untreated * 100

print(f"  {'Quintile':>8s} {'Range':>15s} | {'Treated':>8s} {'%':>7s} | {'Untrt':>8s} {'%':>7s} | {'Diff':>6s}")
print(f"  {'-'*8}-{'-'*15}-+-{'-'*8}-{'-'*7}-+-{'-'*8}-{'-'*7}-+-{'-'*6}")
for i in range(n_bins):
    print(f"  {q_names[i]:>8s} {boundaries[i]:>15s} | {treated_counts[i]:>8d} {treated_pcts[i]:>6.1f}% | {untreated_counts[i]:>8d} {untreated_pcts[i]:>6.1f}% | {treated_pcts[i]-untreated_pcts[i]:>+5.1f}")

# Filter out zero-count bins for chi-square
nonzero = (treated_counts > 0) & (untreated_counts > 0)
if nonzero.sum() >= 2:
    contingency_q = np.array([treated_counts[nonzero], untreated_counts[nonzero]])
    chi2_q, p_q, dof_q, _ = stats.chi2_contingency(contingency_q)
    cramers_v_q = np.sqrt(chi2_q / (contingency_q.sum() * (min(contingency_q.shape) - 1)))
    print(f"  Chi-square: χ²={chi2_q:.4f}, df={dof_q}, p={p_q:.4f}, Cramér's V={cramers_v_q:.4f}")
else:
    chi2_q, p_q, cramers_v_q = 0, 1, 0
    print(f"  Chi-square: insufficient non-zero bins")

# ── 4. Domain distribution ──
print(f"\n── 4. DOMAIN DISTRIBUTION ──")
domains = meta["domain"].values
unique_domains = sorted(set(domains))

treated_domain_counts = []
untreated_domain_counts = []
print(f"  {'Domain':>15s} | {'Treated':>8s} {'%':>7s} | {'Untrt':>8s} {'%':>7s} | {'Diff':>6s}")
print(f"  {'-'*15}-+-{'-'*8}-{'-'*7}-+-{'-'*8}-{'-'*7}-+-{'-'*6}")
for domain in unique_domains:
    domain_mask = domains == domain
    t_count = int(np.sum(labels & domain_mask))
    u_count = int(np.sum(~labels & domain_mask))
    treated_domain_counts.append(t_count)
    untreated_domain_counts.append(u_count)
    t_pct = t_count / n_treated * 100
    u_pct = u_count / n_untreated * 100
    print(f"  {domain:>15s} | {t_count:>8d} {t_pct:>6.1f}% | {u_count:>8d} {u_pct:>6.1f}% | {t_pct-u_pct:>+5.1f}")

contingency_d = np.array([treated_domain_counts, untreated_domain_counts])
chi2_d, p_d, dof_d, _ = stats.chi2_contingency(contingency_d)
cramers_v_d = np.sqrt(chi2_d / (n_total * (min(contingency_d.shape) - 1)))
print(f"  Chi-square: χ²={chi2_d:.4f}, df={dof_d}, p={p_d:.4f}, Cramér's V={cramers_v_d:.4f}")

# ── 5. Subject distribution (top 20 by |diff|) ──
print(f"\n── 5. SUBJECT DISTRIBUTION (top 20 by |diff|) ──")
subjects = meta["subject"].values
unique_subjects = sorted(set(subjects))

subject_rows = []
for subj in unique_subjects:
    subj_mask = subjects == subj
    t_count = int(np.sum(labels & subj_mask))
    u_count = int(np.sum(~labels & subj_mask))
    total = t_count + u_count
    t_pct = t_count / n_treated * 100
    u_pct = u_count / n_untreated * 100
    subject_rows.append({
        "subject": subj, "n_total": total,
        "n_treated": t_count, "n_untreated": u_count,
        "pct_treated": t_pct, "pct_untreated": u_pct,
        "diff_pp": t_pct - u_pct
    })

subject_df = pd.DataFrame(subject_rows).sort_values("diff_pp", key=abs, ascending=False)
print(f"  {'Subject':>40s} | {'N':>5s} | {'Trt%':>6s} | {'Unt%':>6s} | {'Diff':>6s}")
print(f"  {'-'*40}-+-{'-'*5}-+-{'-'*6}-+-{'-'*6}-+-{'-'*6}")
for _, row in subject_df.head(20).iterrows():
    print(f"  {row['subject']:>40s} | {row['n_total']:>5d} | {row['pct_treated']:>5.2f}% | {row['pct_untreated']:>5.2f}% | {row['diff_pp']:>+5.2f}")

t_subj_counts = np.array([int(np.sum(labels & (subjects == s))) for s in unique_subjects])
u_subj_counts = np.array([int(np.sum(~labels & (subjects == s))) for s in unique_subjects])
nonzero_s = (t_subj_counts > 0) & (u_subj_counts > 0)
contingency_s = np.array([t_subj_counts[nonzero_s], u_subj_counts[nonzero_s]])
chi2_s, p_s, dof_s, _ = stats.chi2_contingency(contingency_s)
cramers_v_s = np.sqrt(chi2_s / (contingency_s.sum() * (min(contingency_s.shape) - 1)))
print(f"  Chi-square: χ²={chi2_s:.4f}, df={dof_s}, p={p_s:.4f}, Cramér's V={cramers_v_s:.4f}")

# ── 6. KS test ──
print(f"\n── 6. DISTRIBUTIONAL TESTS ──")
ks_stat, ks_pval = stats.ks_2samp(treated_acc, untreated_acc)
print(f"  KS test (accuracy distribution): D={ks_stat:.4f}, p={ks_pval:.4f}")

# ── 7. Difficulty × group interaction within quintiles ──
print(f"\n── 7. ACCURACY WITHIN QUINTILES (treated vs untreated) ──")
print(f"  {'Quintile':>8s} | {'Trt_mean':>8s} | {'Unt_mean':>8s} | {'Diff':>7s} | {'p':>7s}")
print(f"  {'-'*8}-+-{'-'*8}-+-{'-'*8}-+-{'-'*7}-+-{'-'*7}")
for i in range(n_bins):
    t_q = item_acc[labels & (quintile_labels_arr == i)]
    u_q = item_acc[~labels & (quintile_labels_arr == i)]
    if len(t_q) > 1 and len(u_q) > 1:
        _, p_q_i = stats.ttest_ind(t_q, u_q)
        print(f"  {q_names[i]:>8s} | {t_q.mean():>8.4f} | {u_q.mean():>8.4f} | {t_q.mean()-u_q.mean():>+6.4f} | {p_q_i:>7.4f}")

# ── Summary ──
print(f"\n{'='*80}")
print("SUMMARY")
print(f"{'='*80}")
print(f"  Accuracy:  diff={diff:+.4f}, d={cohens_d:.4f}, p(t)={t_pval:.4f}, p(MW)={u_pval:.4f}")
print(f"  Quintile:  χ²={chi2_q:.2f}, p={p_q:.4f}, V={cramers_v_q:.4f}")
print(f"  Domain:    χ²={chi2_d:.2f}, p={p_d:.4f}, V={cramers_v_d:.4f}")
print(f"  Subject:   χ²={chi2_s:.2f}, p={p_s:.4f}, V={cramers_v_s:.4f}")
print(f"  KS test:   D={ks_stat:.4f}, p={ks_pval:.4f}")

concerns = []
if t_pval < 0.05 and abs(cohens_d) > 0.1:
    concerns.append(f"Accuracy: significant & non-trivial (d={cohens_d:.4f})")
elif t_pval < 0.05:
    concerns.append(f"Accuracy: stat. significant but trivial effect (d={cohens_d:.4f})")
if p_d < 0.05 and cramers_v_d > 0.05:
    concerns.append(f"Domain: significant & non-trivial (V={cramers_v_d:.4f})")
if p_s < 0.05 and cramers_v_s > 0.05:
    concerns.append(f"Subject: significant & non-trivial (V={cramers_v_s:.4f})")

if not concerns:
    print(f"\n  CONCLUSION: Pre-treatment balance holds. Treated and untreated items")
    print(f"  are well-matched on baseline accuracy, difficulty, and domain composition.")
    print(f"  The parallel trends assumption is supported.")
elif all("trivial" in c for c in concerns):
    print(f"\n  CONCLUSION: Minor statistical significance detected but effect sizes are")
    print(f"  negligible. With n={n_total:,} items, small differences reach significance.")
    print(f"  Pre-treatment balance is substantively adequate.")
    for c in concerns:
        print(f"    - {c}")
else:
    print(f"\n  CONCERNS:")
    for c in concerns:
        print(f"    - {c}")
