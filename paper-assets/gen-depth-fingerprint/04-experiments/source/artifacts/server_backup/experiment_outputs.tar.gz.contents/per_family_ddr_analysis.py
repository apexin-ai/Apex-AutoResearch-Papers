import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_csv('/root/gen-depth-fingerprint/data/features_8gen.csv')

FAMILY_MAP = {
    'pythia-2.8b': 'Pythia',
    'pythia-1b': 'Pythia',
    'olmo-2-1b': 'OLMo',
    'qwen3-0.6b': 'Qwen',
    'qwen3-1.7b': 'Qwen',
    'qwen3-8b': 'Qwen',
    'llama-3.2-3b': 'Llama',
    'mistral-7b-v0.3': 'Mistral',
}

FEATURES = ['entropy_mean', 'ttr', 'hapax_ratio', 'entropy_std', 'entropy_max', 'entropy_min', 'tail_decay']
FEAT_LABELS = {
    'entropy_mean': r'$H_{\mathrm{mean}}$',
    'ttr': 'TTR',
    'hapax_ratio': 'Hapax',
    'entropy_std': r'$H_{\mathrm{std}}$',
    'entropy_max': r'$H_{\mathrm{max}}$',
    'entropy_min': r'$H_{\mathrm{min}}$',
    'tail_decay': r'$\beta_{\mathrm{tail}}$',
}

PARTITION = {
    'entropy_mean': 'Drifting',
    'ttr': 'Drifting',
    'hapax_ratio': 'Drifting',
    'entropy_std': 'Intermediate',
    'entropy_max': 'Near-stationary',
    'entropy_min': 'Near-stationary',
    'tail_decay': 'Near-stationary',
}

FAMILY_ORDER = ['Pythia', 'OLMo', 'Qwen', 'Llama', 'Mistral']

df['family'] = df['model_name'].map(FAMILY_MAP)

# --- Compute per-generator Spearman |rho| and Cohen's d ---
records = []
for gen, gdf in df.groupby('model_name'):
    family = FAMILY_MAP[gen]
    for feat in FEATURES:
        rho, p_rho = stats.spearmanr(gdf['depth'], gdf[feat])
        # Cohen's d: depth-0 vs depth >= 1
        d0 = gdf.loc[gdf['depth'] == 0, feat].values
        d1plus = gdf.loc[gdf['depth'] >= 1, feat].values
        if len(d0) > 1 and len(d1plus) > 1:
            pooled_std = np.sqrt(((len(d0)-1)*np.var(d0, ddof=1) + (len(d1plus)-1)*np.var(d1plus, ddof=1)) / (len(d0)+len(d1plus)-2))
            cohens_d = (np.mean(d0) - np.mean(d1plus)) / pooled_std if pooled_std > 0 else 0.0
        else:
            cohens_d = np.nan
        records.append({
            'generator': gen,
            'family': family,
            'feature': feat,
            'abs_rho': abs(rho),
            'abs_cohens_d': abs(cohens_d),
        })

rdf = pd.DataFrame(records)

# --- Aggregate per family ---
family_stats = []
for fam in FAMILY_ORDER:
    fam_df = rdf[rdf['family'] == fam]
    n_gen = fam_df['generator'].nunique()
    for feat in FEATURES:
        ffd = fam_df[fam_df['feature'] == feat]
        rho_mean = ffd['abs_rho'].mean()
        rho_std = ffd['abs_rho'].std(ddof=1) if n_gen > 1 else np.nan
        d_mean = ffd['abs_cohens_d'].mean()
        d_std = ffd['abs_cohens_d'].std(ddof=1) if n_gen > 1 else np.nan
        family_stats.append({
            'family': fam,
            'feature': feat,
            'n_gen': n_gen,
            'rho_mean': rho_mean,
            'rho_std': rho_std,
            'd_mean': d_mean,
            'd_std': d_std,
        })

fst = pd.DataFrame(family_stats)

# --- Print summary table ---
print("="*80)
print("Per-Family DDR Consistency: Spearman |rho|(depth, feature)")
print("="*80)
for fam in FAMILY_ORDER:
    ff = fst[fst['family'] == fam]
    n = ff['n_gen'].iloc[0]
    print(f"\n{fam} (n={n} generators):")
    for _, row in ff.iterrows():
        part = PARTITION[row['feature']]
        if np.isnan(row['rho_std']):
            print(f"  {row['feature']:15s} [{part:15s}]  |rho| = {row['rho_mean']:.3f}  |d| = {row['d_mean']:.3f}")
        else:
            print(f"  {row['feature']:15s} [{part:15s}]  |rho| = {row['rho_mean']:.3f} +/- {row['rho_std']:.3f}  |d| = {row['d_mean']:.3f} +/- {row['d_std']:.3f}")

# --- Generate LaTeX table ---
# Table: rows = families, columns = features grouped by partition
# Show |rho| mean +/- std

drifting = ['entropy_mean', 'ttr', 'hapax_ratio']
intermediate = ['entropy_std']
stationary = ['entropy_max', 'entropy_min', 'tail_decay']

def fmt_val(row):
    if np.isnan(row['rho_std']):
        return f"{row['rho_mean']:.2f}"
    else:
        return f"{row['rho_mean']:.2f}\\tiny{{$\\pm${row['rho_std']:.2f}}}"

lines = []
lines.append(r'\begin{table}[t]')
lines.append(r'\centering')
lines.append(r'\caption{Intra-family consistency of DDR patterns. Each cell shows the mean Spearman $|\rho|$(depth, feature) across generators within a family ($\pm$ SD for multi-generator families). Drifting features exhibit consistently high $|\rho|$ while near-stationary features remain low across all families.}')
lines.append(r'\label{tab:family_ddr_consistency}')
lines.append(r'\small')
lines.append(r'\setlength{\tabcolsep}{3.5pt}')
lines.append(r'\begin{tabular}{l c ccc c ccc}')
lines.append(r'\toprule')
lines.append(r' & & \multicolumn{3}{c}{\textsc{Drifting}} & \textsc{Int.} & \multicolumn{3}{c}{\textsc{Near-Stationary}} \\')
lines.append(r'\cmidrule(lr){3-5} \cmidrule(lr){6-6} \cmidrule(lr){7-9}')

feat_headers = []
for feat in drifting + intermediate + stationary:
    feat_headers.append(FEAT_LABELS[feat])
lines.append(r'Family & $n$ & ' + ' & '.join(feat_headers) + r' \\')
lines.append(r'\midrule')

for fam in FAMILY_ORDER:
    ff = fst[fst['family'] == fam]
    n = int(ff['n_gen'].iloc[0])
    cells = [fam, str(n)]
    for feat in drifting + intermediate + stationary:
        row = ff[ff['feature'] == feat].iloc[0]
        cells.append(fmt_val(row))
    lines.append(' & '.join(cells) + r' \\')

lines.append(r'\midrule')
# Add a "Cross-family" summary row
for feat in drifting + intermediate + stationary:
    pass

# Actually, add a mean row across all 8 generators (not family-aggregated)
all_gen_stats = []
for feat in drifting + intermediate + stationary:
    feat_rdf = rdf[rdf['feature'] == feat]
    all_gen_stats.append(f"{feat_rdf['abs_rho'].mean():.2f}\\tiny{{$\\pm${feat_rdf['abs_rho'].std(ddof=1):.2f}}}")
lines.append(r'\rowcolor{gray!10}')
lines.append(r'All 8 gen. & 8 & ' + ' & '.join(all_gen_stats) + r' \\')

lines.append(r'\bottomrule')
lines.append(r'\end{tabular}')
lines.append(r'\end{table}')

latex = '\n'.join(lines)
print("\n" + "="*80)
print("LaTeX Table:")
print("="*80)
print(latex)

# Save
with open('/root/gen-depth-fingerprint/results/per_family_ddr_table.tex', 'w') as f:
    f.write(latex)
print("\nSaved to /root/gen-depth-fingerprint/results/per_family_ddr_table.tex")

# --- Also generate Cohen's d table ---
lines2 = []
lines2.append(r'\begin{table}[t]')
lines2.append(r'\centering')
lines2.append(r"\caption{Intra-family consistency of Cohen's $d$ (depth-0 vs.\ depth-1+). Format matches Table~\ref{tab:family_ddr_consistency}.}")
lines2.append(r'\label{tab:family_cohens_d}')
lines2.append(r'\small')
lines2.append(r'\setlength{\tabcolsep}{3.5pt}')
lines2.append(r'\begin{tabular}{l c ccc c ccc}')
lines2.append(r'\toprule')
lines2.append(r' & & \multicolumn{3}{c}{\textsc{Drifting}} & \textsc{Int.} & \multicolumn{3}{c}{\textsc{Near-Stationary}} \\')
lines2.append(r'\cmidrule(lr){3-5} \cmidrule(lr){6-6} \cmidrule(lr){7-9}')
lines2.append(r'Family & $n$ & ' + ' & '.join(feat_headers) + r' \\')
lines2.append(r'\midrule')

def fmt_d(row):
    if np.isnan(row['d_std']):
        return f"{row['d_mean']:.2f}"
    else:
        return f"{row['d_mean']:.2f}\\tiny{{$\\pm${row['d_std']:.2f}}}"

for fam in FAMILY_ORDER:
    ff = fst[fst['family'] == fam]
    n = int(ff['n_gen'].iloc[0])
    cells = [fam, str(n)]
    for feat in drifting + intermediate + stationary:
        row = ff[ff['feature'] == feat].iloc[0]
        cells.append(fmt_d(row))
    lines2.append(' & '.join(cells) + r' \\')

lines2.append(r'\midrule')
lines2.append(r'\rowcolor{gray!10}')
all_d = []
for feat in drifting + intermediate + stationary:
    feat_rdf = rdf[rdf['feature'] == feat]
    all_d.append(f"{feat_rdf['abs_cohens_d'].mean():.2f}\\tiny{{$\\pm${feat_rdf['abs_cohens_d'].std(ddof=1):.2f}}}")
lines2.append(r'All 8 gen. & 8 & ' + ' & '.join(all_d) + r' \\')
lines2.append(r'\bottomrule')
lines2.append(r'\end{tabular}')
lines2.append(r'\end{table}')

latex2 = '\n'.join(lines2)
with open('/root/gen-depth-fingerprint/results/per_family_cohens_d_table.tex', 'w') as f:
    f.write(latex2)
print("Saved Cohen's d table to /root/gen-depth-fingerprint/results/per_family_cohens_d_table.tex")

# --- Cross-family variance analysis ---
print("\n" + "="*80)
print("Cross-family variance: which family has highest intra-family variance?")
print("="*80)
for fam in ['Pythia', 'Qwen']:
    ff = fst[fst['family'] == fam]
    print(f"\n{fam}:")
    for _, row in ff.iterrows():
        if not np.isnan(row['rho_std']):
            cv = row['rho_std'] / row['rho_mean'] * 100 if row['rho_mean'] > 0 else float('inf')
            print(f"  {row['feature']:15s}  CV = {cv:.1f}%  (SD/mean)")

