#!/usr/bin/env python3
"""Round 3 reviewer response computations — all 4 tasks."""
import json, os, sys
import numpy as np
import pandas as pd
from pathlib import Path
from scipy import stats

ROOT = Path("/root/gen-depth-fingerprint")
DATA = ROOT / "data"
RESULTS = ROOT / "results"
RESULTS.mkdir(exist_ok=True)
FIGURES = ROOT / "figures"
FIGURES.mkdir(exist_ok=True)

# ============================================================
# TASK 1: N2a — Downstream Bootstrap CI + Effect Size
# ============================================================
def task1_downstream_bootstrap():
    print("=" * 60)
    print("TASK 1: Downstream Bootstrap CI + Effect Size")
    print("=" * 60)

    base = Path("/root/autodl-tmp/gen-depth-fingerprint/experiments/downstream")
    
    variants = {
        "all": [],
        "size_matched": [],
        "depth01": [],
        "binary_filtered": [],
        "depth0_only": [],
    }
    seeds = [42, 123, 456]
    
    for var in variants:
        for seed in seeds:
            rpath = base / f"{var}_seed{seed}" / "results.json"
            with open(rpath) as f:
                r = json.load(f)
            variants[var].append(r["eval_perplexity"])
    
    for var, vals in variants.items():
        print(f"  {var}: {[f'{v:.4f}' for v in vals]} mean={np.mean(vals):.4f}")
    
    rng = np.random.RandomState(42)
    n_boot = 10000
    n_perm = 10000
    
    results = {"task": "downstream_bootstrap_ci", "n_seeds": 3, "seeds": seeds,
               "n_bootstrap": n_boot, "n_permutation": n_perm, "variants": {}}
    
    for var, vals in variants.items():
        results["variants"][var] = {
            "perplexities": vals,
            "mean": round(float(np.mean(vals)), 6),
            "std": round(float(np.std(vals, ddof=1)), 6),
        }
    
    # Pairwise comparisons against "all"
    comparisons = {}
    all_vals = np.array(variants["all"])
    
    for var in ["size_matched", "depth01", "binary_filtered", "depth0_only"]:
        var_vals = np.array(variants[var])
        diffs = var_vals - all_vals  # per-seed paired differences
        mean_diff = float(np.mean(diffs))
        
        # Paired bootstrap CI
        boot_diffs = []
        for _ in range(n_boot):
            idx = rng.randint(0, len(diffs), len(diffs))
            boot_diffs.append(np.mean(diffs[idx]))
        boot_diffs = np.array(boot_diffs)
        ci_lower = float(np.percentile(boot_diffs, 2.5))
        ci_upper = float(np.percentile(boot_diffs, 97.5))
        
        # Permutation test (paired)
        observed_diff = abs(mean_diff)
        count_extreme = 0
        for _ in range(n_perm):
            signs = rng.choice([-1, 1], size=len(diffs))
            perm_diff = abs(np.mean(diffs * signs))
            if perm_diff >= observed_diff:
                count_extreme += 1
        p_value = (count_extreme + 1) / (n_perm + 1)
        
        # Cohen's d (paired)
        sd_diff = float(np.std(diffs, ddof=1))
        cohens_d = mean_diff / sd_diff if sd_diff > 0 else float('inf')
        
        # Also do paired t-test for reference
        t_stat, t_pvalue = stats.ttest_rel(var_vals, all_vals)
        
        comparisons[f"{var}_vs_all"] = {
            "paired_diffs": [round(float(d), 6) for d in diffs],
            "mean_diff": round(mean_diff, 6),
            "bootstrap_ci_95": [round(ci_lower, 6), round(ci_upper, 6)],
            "permutation_p_value": round(p_value, 4),
            "cohens_d": round(cohens_d, 4),
            "cohens_d_interpretation": (
                "large" if abs(cohens_d) >= 0.8 else
                "medium" if abs(cohens_d) >= 0.5 else
                "small" if abs(cohens_d) >= 0.2 else "negligible"
            ),
            "paired_t_test": {
                "t_statistic": round(float(t_stat), 4),
                "p_value": round(float(t_pvalue), 4),
            },
            "note": f"n=3 seeds — limited statistical power"
        }
        print(f"\n  {var} vs all:")
        print(f"    mean_diff = {mean_diff:.6f}")
        print(f"    bootstrap 95% CI = [{ci_lower:.6f}, {ci_upper:.6f}]")
        print(f"    permutation p = {p_value:.4f}")
        print(f"    Cohen's d = {cohens_d:.4f} ({comparisons[f'{var}_vs_all']['cohens_d_interpretation']})")
        print(f"    paired t-test p = {t_pvalue:.4f}")
    
    results["comparisons"] = comparisons
    
    out = RESULTS / "n2a_bootstrap_ci.json"
    with open(out, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved: {out}")
    return results

# ============================================================
# TASK 2: Per-Generator Binary F1
# ============================================================
def task2_per_gen_binary_f1():
    print("\n" + "=" * 60)
    print("TASK 2: Per-Generator Binary F1")
    print("=" * 60)
    
    # Read existing LOGO results
    existing = RESULTS / "review_p0a_binary_logo.json"
    with open(existing) as f:
        logo_data = json.load(f)
    
    method_7f = logo_data["methods"]["7_feature"]
    
    result = {
        "task": "per_generator_binary_f1",
        "description": "Binary LOGO F1 (gen-1 vs gen-2+, gen-0 excluded), 7-feature XGBoost ensemble",
        "overall_f1": method_7f["f1"],
        "overall_ci95": method_7f["ci95"],
        "per_generator": {},
    }
    
    gen_order = ["pythia-1b", "pythia-2.8b", "olmo-2-1b", "qwen3-0.6b", "qwen3-1.7b", "qwen3-8b"]
    
    for gen in gen_order:
        pg = method_7f["per_gen"][gen]
        result["per_generator"][gen] = {
            "f1": pg["f1"],
            "ci95": [pg["ci_lower"], pg["ci_upper"]],
        }
        print(f"  {gen}: F1={pg['f1']:.4f} [{pg['ci_lower']:.4f}, {pg['ci_upper']:.4f}]")
    
    # Also include other methods for completeness
    result["all_methods"] = {}
    for method_name, method_data in logo_data["methods"].items():
        result["all_methods"][method_name] = {
            "overall_f1": method_data["f1"],
            "overall_ci95": method_data["ci95"],
            "per_generator": {
                gen: {
                    "f1": method_data["per_gen"][gen]["f1"],
                    "ci95": [method_data["per_gen"][gen]["ci_lower"],
                             method_data["per_gen"][gen]["ci_upper"]],
                }
                for gen in gen_order
            }
        }
    
    out = RESULTS / "per_gen_binary_f1.json"
    with open(out, "w") as f:
        json.dump(result, f, indent=2)
    print(f"\nSaved: {out}")
    return result

# ============================================================
# TASK 3: M4 — Figure 1 Strip Plot (Spearman per generator)
# ============================================================
def task3_strip_plot():
    print("\n" + "=" * 60)
    print("TASK 3: Strip Plot — Spearman correlation per generator")
    print("=" * 60)
    
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    
    plt.rcParams.update({
        'font.family': 'serif',
        'font.serif': ['Times New Roman', 'DejaVu Serif', 'Nimbus Roman'],
        'font.size': 8,
        'axes.labelsize': 9,
        'axes.titlesize': 9,
        'xtick.labelsize': 7.5,
        'ytick.labelsize': 7.5,
        'legend.fontsize': 6.5,
        'figure.dpi': 300,
        'savefig.dpi': 300,
        'savefig.bbox': 'tight',
        'axes.spines.top': False,
        'axes.spines.right': False,
        'axes.grid': False,
        'mathtext.fontset': 'cm',
    })
    
    COLORS = {
        'pythia-1b':   '#E69F00',
        'pythia-2.8b': '#56B4E9',
        'olmo-2-1b':   '#009E73',
        'qwen3-0.6b':  '#0072B2',
        'qwen3-1.7b':  '#D55E00',
        'qwen3-8b':    '#CC79A7',
    }
    MARKERS = {
        'pythia-1b':   'o',
        'pythia-2.8b': 's',
        'olmo-2-1b':   '^',
        'qwen3-0.6b':  'D',
        'qwen3-1.7b':  'v',
        'qwen3-8b':    'P',
    }
    LABELS = {
        'pythia-1b':   'Pythia-1B',
        'pythia-2.8b': 'Pythia-2.8B',
        'olmo-2-1b':   'OLMo-2-1B',
        'qwen3-0.6b':  'Qwen3-0.6B',
        'qwen3-1.7b':  'Qwen3-1.7B',
        'qwen3-8b':    'Qwen3-8B',
    }
    MODEL_ORDER = ['pythia-1b', 'pythia-2.8b', 'olmo-2-1b', 'qwen3-0.6b', 'qwen3-1.7b', 'qwen3-8b']
    
    df = pd.read_csv(DATA / "features_all_models.csv")
    
    features = ['entropy_mean', 'entropy_std', 'entropy_min', 'entropy_max',
                'tail_decay', 'ttr', 'hapax_ratio']
    feat_labels = [r'$\bar{H}$', r'$\sigma_H$', r'$H_{\min}$', r'$H_{\max}$',
                   'Tail Decay', 'TTR', 'Hapax']
    
    # Compute Spearman correlation per generator per feature
    spearman_data = {}
    for model in MODEL_ORDER:
        mdf = df[df['model_name'] == model]
        spearman_data[model] = {}
        for feat in features:
            rho, pval = stats.spearmanr(mdf['depth'], mdf[feat])
            spearman_data[model][feat] = {'rho': rho, 'pval': pval}
    
    # Print results
    print(f"{'Feature':<15}", end="")
    for m in MODEL_ORDER:
        print(f"  {LABELS[m]:>12}", end="")
    print()
    for feat, label in zip(features, feat_labels):
        print(f"{feat:<15}", end="")
        for m in MODEL_ORDER:
            rho = spearman_data[m][feat]['rho']
            print(f"  {rho:>12.4f}", end="")
        print()
    
    # Create strip plot
    fig, ax = plt.subplots(1, 1, figsize=(5.5, 2.8))
    
    x_positions = np.arange(len(features))
    offsets = np.linspace(-0.25, 0.25, len(MODEL_ORDER))
    
    for i, model in enumerate(MODEL_ORDER):
        rhos = [spearman_data[model][feat]['rho'] for feat in features]
        ax.scatter(x_positions + offsets[i], rhos,
                   color=COLORS[model], marker=MARKERS[model],
                   s=35, label=LABELS[model], zorder=3,
                   edgecolors='white', linewidths=0.3)
    
    # Add aggregate mean as horizontal ticks
    for j, feat in enumerate(features):
        all_rhos = [spearman_data[m][feat]['rho'] for m in MODEL_ORDER]
        mean_rho = np.mean(all_rhos)
        ax.plot([j - 0.32, j + 0.32], [mean_rho, mean_rho],
                color='#333333', linewidth=1.2, zorder=2, alpha=0.6)
    
    ax.axhline(y=0, color='#AAAAAA', linewidth=0.5, linestyle='--', zorder=1)
    ax.set_xticks(x_positions)
    ax.set_xticklabels(feat_labels)
    ax.set_ylabel(r'Spearman $\rho$ (feature vs. depth)')
    ax.set_xlim(-0.5, len(features) - 0.5)
    
    ax.legend(loc='upper right', ncol=2, frameon=False, 
              columnspacing=0.8, handletextpad=0.3, borderpad=0.2)
    
    plt.tight_layout()
    
    outdir = FIGURES
    fig.savefig(outdir / 'fig1_differential_response_strip.pdf', facecolor='white')
    fig.savefig(outdir / 'fig1_differential_response_strip.png', dpi=300, facecolor='white')
    print(f"\nSaved: {outdir}/fig1_differential_response_strip.{{pdf,png}}")
    plt.close()
    
    # Also save the correlation data
    corr_out = RESULTS / "spearman_per_generator.json"
    out_data = {}
    for model in MODEL_ORDER:
        out_data[model] = {feat: round(spearman_data[model][feat]['rho'], 4) for feat in features}
    with open(corr_out, "w") as f:
        json.dump(out_data, f, indent=2)
    print(f"Saved: {corr_out}")

# ============================================================
# TASK 4: M6 — Dataset Statistics Table
# ============================================================
def task4_dataset_stats():
    print("\n" + "=" * 60)
    print("TASK 4: Dataset Statistics Table")
    print("=" * 60)
    
    df = pd.read_csv(DATA / "features_all_models.csv")
    
    MODEL_ORDER = ['pythia-1b', 'pythia-2.8b', 'olmo-2-1b', 'qwen3-0.6b', 'qwen3-1.7b', 'qwen3-8b']
    MODEL_LABELS = {
        'pythia-1b':   'Pythia-1B',
        'pythia-2.8b': 'Pythia-2.8B',
        'olmo-2-1b':   'OLMo-2-1B',
        'qwen3-0.6b':  'Qwen3-0.6B',
        'qwen3-1.7b':  'Qwen3-1.7B',
        'qwen3-8b':    'Qwen3-8B',
    }
    
    JSONL_PATHS = {
        "olmo-2-1b":   DATA / "olmo-2-1b" / "generations.jsonl",
        "pythia-1b":   DATA / "pythia-1b" / "generations.jsonl",
        "pythia-2.8b": DATA / "generations.jsonl",
        "qwen3-0.6b":  DATA / "qwen3-0.6b" / "generations.jsonl",
        "qwen3-1.7b":  DATA / "qwen3-1.7b" / "generations.jsonl",
        "qwen3-8b":    DATA / "qwen3-8b" / "generations.jsonl",
    }
    
    # Load text lengths from generation files
    text_lengths = {}
    for model, path in JSONL_PATHS.items():
        if not path.exists():
            print(f"  WARNING: {path} not found")
            continue
        lengths = {}
        with open(path) as f:
            for line in f:
                r = json.loads(line)
                key = (r.get("seed_id", r.get("id")), r["depth"])
                lengths[key] = len(r["text"])
        text_lengths[model] = lengths
        print(f"  {model}: {len(lengths)} texts loaded")
    
    # Count samples per generator per depth
    depths = sorted(df['depth'].unique())
    
    # Build stats
    stats_data = {}
    for model in MODEL_ORDER:
        mdf = df[df['model_name'] == model]
        stats_data[model] = {}
        for d in depths:
            ddf = mdf[mdf['depth'] == d]
            n = len(ddf)
            
            # Get text lengths for this model+depth
            if model in text_lengths:
                lens = []
                for _, row in ddf.iterrows():
                    key = (row['seed_id'], row['depth'])
                    if key in text_lengths[model]:
                        lens.append(text_lengths[model][key])
                if lens:
                    mean_len = np.mean(lens)
                    std_len = np.std(lens, ddof=1) if len(lens) > 1 else 0
                else:
                    mean_len, std_len = 0, 0
            else:
                mean_len, std_len = 0, 0
            
            stats_data[model][d] = {
                'n': n,
                'text_len_mean': round(float(mean_len), 1),
                'text_len_std': round(float(std_len), 1),
            }
            print(f"  {model} depth={d}: n={n}, len={mean_len:.1f}±{std_len:.1f}")
    
    # Generate LaTeX table
    lines = []
    lines.append(r"\begin{table}[t]")
    lines.append(r"\centering")
    lines.append(r"\caption{Per-generator, per-depth sample counts and text lengths (characters, mean$\pm$std).}")
    lines.append(r"\label{tab:dataset_stats}")
    lines.append(r"\small")
    
    depth_cols = " ".join(["c c" for _ in depths])
    lines.append(r"\begin{tabular}{l " + depth_cols + "}")
    lines.append(r"\toprule")
    
    # Header row 1: depth labels spanning 2 cols each
    header1 = r"\multirow{2}{*}{Generator}"
    for d in depths:
        header1 += rf" & \multicolumn{{2}}{{c}}{{Depth {d}}}"
    header1 += r" \\"
    lines.append(header1)
    
    # Header row 2: N and Len subheaders
    header2 = ""
    for d in depths:
        header2 += r" & $N$ & Len."
    header2 += r" \\"
    lines.append(r"\cmidrule(lr){2-" + str(1 + 2*len(depths)) + "}")
    lines.append(header2)
    lines.append(r"\midrule")
    
    for model in MODEL_ORDER:
        row = MODEL_LABELS[model]
        for d in depths:
            s = stats_data[model].get(d, {'n': 0, 'text_len_mean': 0, 'text_len_std': 0})
            n = s['n']
            ml = s['text_len_mean']
            sl = s['text_len_std']
            row += f" & {n} & {ml:.0f}$\\pm${sl:.0f}"
        row += r" \\"
        lines.append(row)
    
    # Total row
    total_row = r"\midrule" + "\n" + "Total"
    for d in depths:
        total_n = sum(stats_data[m].get(d, {'n': 0})['n'] for m in MODEL_ORDER)
        total_row += f" & {total_n} & --"
    total_row += r" \\"
    lines.append(total_row)
    
    lines.append(r"\bottomrule")
    lines.append(r"\end{tabular}")
    lines.append(r"\end{table}")
    
    latex = "\n".join(lines)
    
    out = RESULTS / "dataset_stats_table.tex"
    with open(out, "w") as f:
        f.write(latex)
    print(f"\nSaved: {out}")
    
    # Also save raw data as JSON
    json_out = RESULTS / "dataset_stats.json"
    with open(json_out, "w") as f:
        json.dump(stats_data, f, indent=2)
    print(f"Saved: {json_out}")


if __name__ == "__main__":
    task1_downstream_bootstrap()
    task2_per_gen_binary_f1()
    task3_strip_plot()
    task4_dataset_stats()
    print("\n" + "=" * 60)
    print("ALL TASKS COMPLETE")
    print("=" * 60)
