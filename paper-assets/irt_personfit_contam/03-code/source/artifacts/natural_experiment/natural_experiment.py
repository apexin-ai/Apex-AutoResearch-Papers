#!/usr/bin/env python3
"""
Base→Chat Natural Experiment: Δlz* Cross-Benchmark Analysis

Hypothesis: Instruction-tuning produces a consistent cross-benchmark Δlz* shift,
but contamination on specific benchmarks manifests as outlier Δlz* on those
benchmarks relative to the pair's mean Δlz* across benchmarks.

Uses v1 Open LLM Leaderboard data with 21 base/chat model pairs across
4 benchmarks: MMLU, HellaSwag, ARC-Challenge, GSM8K.
"""

import os
import sys
import json
import time
import warnings
import numpy as np
import pandas as pd
from scipy.special import expit
from scipy.stats import ttest_1samp

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

warnings.filterwarnings('ignore')

PROJECT_ROOT = "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam"
OUT_DIR = os.path.join(PROJECT_ROOT, "artifacts/natural_experiment")
PILOT_DIR = os.path.join(PROJECT_ROOT, "artifacts/v1_irt_refit_pilot")
CACHE_DIR = os.path.join(OUT_DIR, ".hf_cache")

sys.path.insert(0, os.path.join(PROJECT_ROOT, "src"))
from person_fit import prob_4pl, estimate_theta_mle, compute_lz_star

os.makedirs(OUT_DIR, exist_ok=True)

# ─── 21 Pairs ───────────────────────────────────────────────────────────

PAIRS = [
    ("mistralai__Mistral-7B-v0.1", "mistralai__Mistral-7B-Instruct-v0.1", "Mistral-7B"),
    ("mosaicml__mpt-7b", "mosaicml__mpt-7b-instruct", "MPT-7B→Inst"),
    ("mosaicml__mpt-7b", "mosaicml__mpt-7b-chat", "MPT-7B→Chat"),
    ("mosaicml__mpt-30b", "mosaicml__mpt-30b-chat", "MPT-30B→Chat"),
    ("tiiuae__falcon-7b", "tiiuae__falcon-7b-instruct", "Falcon-7B"),
    ("togethercomputer__RedPajama-INCITE-7B-Base", "togethercomputer__RedPajama-INCITE-7B-Instruct", "RedPajama-7B"),
    ("huggyllama__llama-7b", "lmsys__vicuna-7b-v1.3", "LLaMA-7B→Vicuna"),
    ("huggyllama__llama-13b", "lmsys__vicuna-13b-v1.5", "LLaMA-13B→Vicuna"),
    ("huggyllama__llama-7b", "TheBloke__guanaco-7B-HF", "LLaMA-7B→Guanaco"),
    ("huggyllama__llama-13b", "TheBloke__guanaco-13B-HF", "LLaMA-13B→Guanaco"),
    ("huggyllama__llama-65b", "TheBloke__guanaco-65B-HF", "LLaMA-65B→Guanaco"),
    ("meta-llama__Llama-2-7b-hf", "jondurbin__airoboros-l2-7b-2.1", "L2-7B→Airoboros"),
    ("meta-llama__Llama-2-13b-hf", "jondurbin__airoboros-l2-13b-2.1", "L2-13B→Airoboros"),
    ("meta-llama__Llama-2-70b-hf", "jondurbin__airoboros-l2-70b-2.1", "L2-70B→Airoboros"),
    ("EleutherAI__pythia-12b-deduped", "OpenAssistant__oasst-sft-4-pythia-12b-epoch-3.5", "Pythia-12B→OASST"),
    ("huggyllama__llama-13b", "NousResearch__Nous-Hermes-13b", "LLaMA-13B→Hermes"),
    ("huggyllama__llama-13b", "teknium__OpenHermes-13B", "LLaMA-13B→OpenHermes"),
    ("huggyllama__llama-13b", "WizardLM__WizardLM-13B-V1.2", "LLaMA-13B→WizardLM"),
    ("huggyllama__llama-13b", "ehartford__dolphin-llama-13b", "LLaMA-13B→Dolphin"),
    ("huggyllama__llama-7b", "psmathur__orca_mini_v3_7b", "LLaMA-7B→Orca"),
    ("huggyllama__llama-13b", "psmathur__orca_mini_v3_13b", "LLaMA-13B→Orca"),
]

BENCHMARK_CONFIGS = {
    "HellaSwag": {
        "file_pattern": "harness|hellaswag|10_",
        "acc_col": "acc_norm",
        "c_param": 0.25,
    },
    "ARC-Challenge": {
        "file_pattern": "harness|arc:challenge|25_",
        "acc_col": "acc_norm",
        "c_param": 0.25,
    },
    "GSM8K": {
        "file_pattern": "harness|gsm8k|5_",
        "acc_col": "acc",
        "c_param": 0.0,
    },
}


# ─── MML-EM IRT Fitting ────────────────────────────────────────────────

def _gauss_hermite_quadrature(n_points=41, bounds=(-4, 4)):
    theta = np.linspace(bounds[0], bounds[1], n_points)
    weights = np.exp(-0.5 * theta**2) / np.sqrt(2 * np.pi)
    weights /= weights.sum()
    return theta, weights


def _e_step(X, a, b, c, theta_q, w_q):
    P = c + (1 - c) * expit(a[None, :] * (theta_q[:, None] - b[None, :]))
    P = np.clip(P, 1e-15, 1 - 1e-15)
    logP = np.log(P)
    log1mP = np.log(1 - P)
    log_lik = X @ logP.T + (1 - X) @ log1mP.T
    log_lik += np.log(w_q)[None, :]
    log_lik -= log_lik.max(axis=1, keepdims=True)
    posterior = np.exp(log_lik)
    posterior /= posterior.sum(axis=1, keepdims=True)
    return X.T @ posterior, posterior.sum(axis=0)


def _m_step(r_j, f_q, a, b, c, theta_q, n_newton=5):
    for _ in range(n_newton):
        z = a[:, None] * (theta_q[None, :] - b[:, None])
        sig = expit(z)
        P = np.clip(c + (1 - c) * sig, 1e-15, 1 - 1e-15)

        dP_db = -a[:, None] * (1 - c) * sig * (1 - sig)
        w = r_j / P - (f_q[None, :] - r_j) / (1 - P)
        grad_b = (w * dP_db).sum(axis=1)
        hess_b = -(f_q[None, :] * dP_db ** 2 / (P * (1 - P))).sum(axis=1)
        hess_b = np.where(np.abs(hess_b) > 1e-10, hess_b, -1e-10)
        b = np.clip(b + np.clip(-grad_b / hess_b, -1.0, 1.0), -6.0, 6.0)

        z = a[:, None] * (theta_q[None, :] - b[:, None])
        sig = expit(z)
        P = np.clip(c + (1 - c) * sig, 1e-15, 1 - 1e-15)
        dP_da = (1 - c) * (theta_q[None, :] - b[:, None]) * sig * (1 - sig)
        w = r_j / P - (f_q[None, :] - r_j) / (1 - P)
        grad_a = (w * dP_da).sum(axis=1)
        hess_a = -(f_q[None, :] * dP_da ** 2 / (P * (1 - P))).sum(axis=1)
        hess_a = np.where(np.abs(hess_a) > 1e-10, hess_a, -1e-10)
        a = np.clip(a + np.clip(-grad_a / hess_a, -0.5, 0.5), 0.01, 5.0)
    return a, b


def fit_irt_mml_em(X, c_fixed=0.0, n_quad=31, max_iter=50, tol=1e-3):
    N, J = X.shape
    theta_q, w_q = _gauss_hermite_quadrature(n_quad)
    p_adj = np.clip((X.mean(axis=0) - c_fixed) / max(1 - c_fixed, 1e-10), 0.01, 0.99)
    b = -np.log(p_adj / (1 - p_adj))
    a = np.ones(J)

    for it in range(max_iter):
        a_old = a.copy()
        r_j, f_q = _e_step(X, a, b, c_fixed, theta_q, w_q)
        a, b = _m_step(r_j, f_q, a, b, c_fixed, theta_q, n_newton=3)
        change = np.max(np.abs(a - a_old))
        if it % 10 == 0:
            print(f"    Iter {it}: max Δa = {change:.6f}")
        if change < tol:
            print(f"    Converged at iter {it}")
            break
    return a, b, c_fixed


# ─── Data Download ──────────────────────────────────────────────────────

def download_benchmarks_for_model(model_name, cache_dir=None):
    os.environ['HF_HUB_DISABLE_XET'] = '1'
    from huggingface_hub import HfApi, hf_hub_download
    import pyarrow.parquet as pq

    repo_id = f"open-llm-leaderboard-old/details_{model_name}"
    api = HfApi()

    try:
        files = api.list_repo_files(repo_id, repo_type="dataset")
    except Exception:
        return {}

    results = {}
    for bench_key, config in BENCHMARK_CONFIGS.items():
        pattern = config["file_pattern"]
        acc_col = config["acc_col"]

        matching = sorted(
            [f for f in files if pattern in f and f.endswith('.parquet')],
            reverse=True
        )
        if not matching:
            continue

        try:
            local = hf_hub_download(repo_id, matching[0], repo_type="dataset",
                                     cache_dir=cache_dir)
            table = pq.read_table(local)

            if acc_col in table.column_names:
                vals = table[acc_col].to_pylist()
            elif 'acc' in table.column_names:
                vals = table['acc'].to_pylist()
            else:
                continue

            results[bench_key] = np.array([int(v) for v in vals], dtype=np.float64)
        except Exception:
            continue

    return results


# ─── lz* Computation ───────────────────────────────────────────────────

def compute_lz_stars_for_benchmark(X, a, b, c_val):
    N, J = X.shape
    c = np.full(J, c_val)
    d = np.ones(J)
    thetas = np.zeros(N)
    lz_stars = np.zeros(N)
    for i in range(N):
        x_i = X[i].astype(np.float64)
        thetas[i] = estimate_theta_mle(x_i, a, b, c, d)
        lz_stars[i] = compute_lz_star(x_i, thetas[i], a, b, c, d)
    return thetas, lz_stars


# ─── Visualization ──────────────────────────────────────────────────────

def plot_heatmap(matrix, row_labels, col_labels, title, out_path,
                 cmap='RdBu_r', center=0, fmt='.2f', figsize=None):
    n_rows, n_cols = matrix.shape
    if figsize is None:
        figsize = (max(6, n_cols * 1.5 + 2), max(6, n_rows * 0.35 + 2))
    fig, ax = plt.subplots(figsize=figsize)

    mask = np.isnan(matrix)
    vmax = np.nanmax(np.abs(matrix - center)) if not np.all(mask) else 1
    im = ax.imshow(matrix, cmap=cmap, aspect='auto',
                   vmin=center - vmax, vmax=center + vmax)

    for i in range(n_rows):
        for j in range(n_cols):
            if not mask[i, j]:
                val = matrix[i, j]
                color = 'white' if abs(val - center) > vmax * 0.6 else 'black'
                ax.text(j, i, f'{val:{fmt}}', ha='center', va='center',
                        fontsize=8, color=color)

    ax.set_xticks(range(n_cols))
    ax.set_xticklabels(col_labels, fontsize=10, rotation=30, ha='right')
    ax.set_yticks(range(n_rows))
    ax.set_yticklabels(row_labels, fontsize=8)
    ax.set_title(title, fontsize=12, pad=10)
    plt.colorbar(im, ax=ax, shrink=0.8)
    plt.tight_layout()
    plt.savefig(out_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Saved: {out_path}")


def plot_boxplot(dev_df, benchmarks, out_path):
    fig, ax = plt.subplots(figsize=(8, 5))
    data = [dev_df[dev_df['benchmark'] == b]['deviation'].dropna().values
            for b in benchmarks]
    bp = ax.boxplot(data, labels=benchmarks, patch_artist=True, widths=0.5)
    colors = ['#4C72B0', '#DD8452', '#55A868', '#C44E52']
    for patch, color in zip(bp['boxes'], colors[:len(benchmarks)]):
        patch.set_facecolor(color)
        patch.set_alpha(0.6)
    ax.axhline(y=0, color='gray', linestyle='--', alpha=0.5)
    ax.set_ylabel('Deviation from pair mean Δlz*')
    ax.set_title('Benchmark-Specific Δlz* Deviation Across Pairs')
    for i, (bench, d) in enumerate(zip(benchmarks, data)):
        if len(d) > 0:
            ax.text(i + 1, ax.get_ylim()[1] * 0.95,
                    f'n={len(d)}', ha='center', va='top', fontsize=8)
    plt.tight_layout()
    plt.savefig(out_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Saved: {out_path}")


def plot_scatter_delta_acc_vs_lz(pairs_df, out_path):
    fig, ax = plt.subplots(figsize=(8, 6))
    colors = {'MMLU': '#4C72B0', 'HellaSwag': '#DD8452',
              'ARC-Challenge': '#55A868', 'GSM8K': '#C44E52'}
    for bench in pairs_df['benchmark'].unique():
        sub = pairs_df[pairs_df['benchmark'] == bench]
        ax.scatter(sub['delta_acc'], sub['delta_lz_star'],
                   label=bench, color=colors.get(bench, 'gray'),
                   alpha=0.7, s=50, edgecolors='white', linewidth=0.5)
    ax.axhline(y=0, color='gray', linestyle='--', alpha=0.3)
    ax.axvline(x=0, color='gray', linestyle='--', alpha=0.3)
    ax.set_xlabel('Δ Accuracy (chat - base)')
    ax.set_ylabel('Δlz* (chat - base)')
    ax.set_title('Δ Accuracy vs Δlz* by Benchmark')
    ax.legend(fontsize=9)
    plt.tight_layout()
    plt.savefig(out_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Saved: {out_path}")


# ─── Main Pipeline ──────────────────────────────────────────────────────

def main():
    np.random.seed(42)
    t_start = time.time()

    # === Step 0: Load MMLU from pilot ===
    print("=" * 60)
    print("Step 0: Loading MMLU from pilot")
    print("=" * 60)

    pilot_data = np.load(os.path.join(PILOT_DIR, "pilot_response_matrix.npz"),
                         allow_pickle=True)
    mmlu_X = pilot_data['X'].astype(np.float64)
    pilot_models = list(pilot_data['model_names'])
    N_pilot, J_mmlu = mmlu_X.shape
    print(f"  {N_pilot} models × {J_mmlu} MMLU items")

    params_df = pd.read_csv(os.path.join(PILOT_DIR, "v1_fitted_params.csv"))
    mmlu_a = params_df['a_3pl'].values
    mmlu_b = params_df['b_3pl'].values

    with open(os.path.join(PILOT_DIR, "pilot_results.json")) as f:
        pilot_results = json.load(f)

    pilot_stats = {}
    for entry in pilot_results['per_model']:
        pilot_stats[entry['model']] = {
            'lz_star': entry['lz_star'],
            'theta': entry['theta'],
            'accuracy': entry['accuracy'],
        }

    # === Step 1: Download non-MMLU benchmarks ===
    print("\n" + "=" * 60)
    print("Step 1: Downloading HellaSwag, ARC-Challenge, GSM8K")
    print("=" * 60)

    bench_responses = {b: {} for b in BENCHMARK_CONFIGS}

    for i, model_name in enumerate(pilot_models):
        print(f"  [{i+1}/{len(pilot_models)}] {model_name}...", end=" ", flush=True)
        t0 = time.time()
        results = download_benchmarks_for_model(model_name, cache_dir=CACHE_DIR)
        dt = time.time() - t0

        found = []
        for bench, resp in results.items():
            bench_responses[bench][model_name] = resp
            found.append(f"{bench}({len(resp)})")

        print(f"{'OK' if found else 'NONE'} ({dt:.1f}s)" +
              (f" [{', '.join(found)}]" if found else ""))

    print("\nData availability:")
    bench_item_counts = {}
    for bench in BENCHMARK_CONFIGS:
        n = len(bench_responses[bench])
        if n > 0:
            sample = next(iter(bench_responses[bench].values()))
            bench_item_counts[bench] = len(sample)
            print(f"  {bench}: {n} models × {len(sample)} items")
        else:
            print(f"  {bench}: NO DATA")

    # === Step 2: IRT Fitting ===
    print("\n" + "=" * 60)
    print("Step 2: IRT fitting per benchmark")
    print("=" * 60)

    irt_params = {"MMLU": (mmlu_a, mmlu_b, 0.25)}
    bench_model_lists = {"MMLU": pilot_models}
    print(f"  MMLU: reusing pilot 3PL (c=0.25), {J_mmlu} items")

    for bench, config in BENCHMARK_CONFIGS.items():
        data = bench_responses[bench]
        if len(data) < 10:
            print(f"  {bench}: SKIPPED ({len(data)} models < 10)")
            continue

        expected_n = bench_item_counts.get(bench, 0)
        models = [m for m in sorted(data.keys()) if len(data[m]) == expected_n]

        if len(models) < 10:
            print(f"  {bench}: SKIPPED (only {len(models)} consistent models)")
            continue

        X = np.vstack([data[m] for m in models]).astype(np.float64)
        N, J = X.shape

        n_zero_var = (X.var(axis=0) == 0).sum()
        c_fixed = config["c_param"]
        label = "3PL" if c_fixed > 0 else "2PL"
        print(f"  {bench}: {label} (c={c_fixed}), {N}×{J}, {n_zero_var} zero-var items")

        t0 = time.time()
        a, b, c = fit_irt_mml_em(X, c_fixed=c_fixed, n_quad=31, max_iter=50, tol=1e-3)
        print(f"    Done in {time.time()-t0:.1f}s, a∈[{a.min():.2f},{a.max():.2f}], b∈[{b.min():.2f},{b.max():.2f}]")

        irt_params[bench] = (a, b, c)
        bench_model_lists[bench] = models

    # === Step 3: Compute lz* ===
    print("\n" + "=" * 60)
    print("Step 3: Computing lz* per benchmark")
    print("=" * 60)

    benchmark_stats = {"MMLU": pilot_stats}

    for bench in ["HellaSwag", "ARC-Challenge", "GSM8K"]:
        if bench not in irt_params:
            continue

        a, b, c = irt_params[bench]
        models = bench_model_lists[bench]
        X = np.vstack([bench_responses[bench][m] for m in models]).astype(np.float64)

        print(f"  {bench}: {len(models)} models...", end=" ", flush=True)
        t0 = time.time()
        thetas, lz_stars = compute_lz_stars_for_benchmark(X, a, b, c)
        print(f"done ({time.time()-t0:.1f}s)")
        print(f"    lz* ∈ [{lz_stars.min():.2f}, {lz_stars.max():.2f}], "
              f"mean={lz_stars.mean():.2f}, std={lz_stars.std():.2f}")

        benchmark_stats[bench] = {}
        for i, m in enumerate(models):
            benchmark_stats[bench][m] = {
                'lz_star': float(lz_stars[i]),
                'theta': float(thetas[i]),
                'accuracy': float(X[i].mean()),
            }

    # === Step 4: Δlz* Analysis ===
    print("\n" + "=" * 60)
    print("Step 4: Δlz* analysis")
    print("=" * 60)

    benchmarks_avail = [b for b in ["MMLU", "HellaSwag", "ARC-Challenge", "GSM8K"]
                        if b in benchmark_stats]
    print(f"  Benchmarks: {benchmarks_avail}")

    # Build pairs data
    rows = []
    for base_m, chat_m, label in PAIRS:
        for bench in benchmarks_avail:
            stats = benchmark_stats[bench]
            if base_m not in stats or chat_m not in stats:
                continue
            rows.append({
                "pair": label,
                "base_model": base_m,
                "chat_model": chat_m,
                "benchmark": bench,
                "lz_star_base": stats[base_m]["lz_star"],
                "lz_star_chat": stats[chat_m]["lz_star"],
                "delta_lz_star": stats[chat_m]["lz_star"] - stats[base_m]["lz_star"],
                "acc_base": stats[base_m]["accuracy"],
                "acc_chat": stats[chat_m]["accuracy"],
                "delta_acc": stats[chat_m]["accuracy"] - stats[base_m]["accuracy"],
            })

    pairs_df = pd.DataFrame(rows)
    print(f"  {len(pairs_df)} (pair, benchmark) data points")

    # Check which pairs have data for all available benchmarks
    pair_bench_counts = pairs_df.groupby('pair')['benchmark'].nunique()
    complete_pairs = pair_bench_counts[pair_bench_counts == len(benchmarks_avail)].index.tolist()
    print(f"  {len(complete_pairs)}/{len(PAIRS)} pairs have all {len(benchmarks_avail)} benchmarks")

    # Compute deviations (within-pair normalization)
    dev_rows = []
    for label in pairs_df['pair'].unique():
        pdata = pairs_df[pairs_df['pair'] == label]
        if len(pdata) < 2:
            continue
        mean_dlz = pdata['delta_lz_star'].mean()
        std_dlz = pdata['delta_lz_star'].std(ddof=1) if len(pdata) > 2 else pdata['delta_lz_star'].std()

        for _, r in pdata.iterrows():
            dev = r['delta_lz_star'] - mean_dlz
            z = dev / std_dlz if std_dlz > 1e-10 else 0.0
            dev_rows.append({
                "pair": r['pair'],
                "benchmark": r['benchmark'],
                "delta_lz_star": r['delta_lz_star'],
                "mean_delta_lz_pair": mean_dlz,
                "deviation": dev,
                "within_pair_zscore": z,
                "delta_acc": r['delta_acc'],
            })

    dev_df = pd.DataFrame(dev_rows)

    # Per-benchmark deviation statistics
    print("\n  Per-benchmark deviation from pair mean:")
    bench_dev_stats = {}
    for bench in benchmarks_avail:
        devs = dev_df[dev_df['benchmark'] == bench]['deviation'].values
        if len(devs) < 3:
            continue
        t_stat, p_val = ttest_1samp(devs, 0)
        s = {
            "n_pairs": int(len(devs)),
            "mean_deviation": float(devs.mean()),
            "std_deviation": float(devs.std()),
            "median_deviation": float(np.median(devs)),
            "t_statistic": float(t_stat),
            "p_value": float(p_val),
            "mean_delta_lz_star": float(
                pairs_df[pairs_df['benchmark'] == bench]['delta_lz_star'].mean()),
        }
        bench_dev_stats[bench] = s
        sig = " *" if p_val < 0.05 else ""
        print(f"    {bench:15s}: mean_dev={s['mean_deviation']:+.3f}, "
              f"std={s['std_deviation']:.3f}, t={t_stat:+.2f}, p={p_val:.4f}{sig}")

    # Outlier detection
    print("\n  Outlier (pair, benchmark) with |z| > 1.5:")
    outliers = dev_df[dev_df['within_pair_zscore'].abs() > 1.5].sort_values(
        'within_pair_zscore', key=abs, ascending=False)
    if len(outliers) > 0:
        for _, r in outliers.iterrows():
            print(f"    {r['pair']:25s} × {r['benchmark']:15s}: "
                  f"Δlz*={r['delta_lz_star']:+.2f}, dev={r['deviation']:+.2f}, z={r['within_pair_zscore']:+.2f}")
    else:
        print("    None")

    # Cross-pair Δlz* summary per benchmark
    print("\n  Mean Δlz* per benchmark:")
    for bench in benchmarks_avail:
        sub = pairs_df[pairs_df['benchmark'] == bench]
        print(f"    {bench:15s}: Δlz*={sub['delta_lz_star'].mean():+.2f} ± {sub['delta_lz_star'].std():.2f}, "
              f"Δacc={sub['delta_acc'].mean():+.4f} ± {sub['delta_acc'].std():.4f}")

    # === Step 5: Visualizations ===
    print("\n" + "=" * 60)
    print("Step 5: Visualizations")
    print("=" * 60)

    pair_labels = [p[2] for p in PAIRS]

    # --- Δlz* Heatmap ---
    delta_matrix = np.full((len(PAIRS), len(benchmarks_avail)), np.nan)
    for i, (_, _, label) in enumerate(PAIRS):
        for j, bench in enumerate(benchmarks_avail):
            sub = pairs_df[(pairs_df['pair'] == label) & (pairs_df['benchmark'] == bench)]
            if len(sub) == 1:
                delta_matrix[i, j] = sub['delta_lz_star'].values[0]

    plot_heatmap(delta_matrix, pair_labels, benchmarks_avail,
                 'Δlz* = lz*(chat) − lz*(base)',
                 os.path.join(OUT_DIR, "delta_lz_heatmap.png"))

    # --- Deviation Heatmap ---
    dev_matrix = np.full((len(PAIRS), len(benchmarks_avail)), np.nan)
    for i, (_, _, label) in enumerate(PAIRS):
        for j, bench in enumerate(benchmarks_avail):
            sub = dev_df[(dev_df['pair'] == label) & (dev_df['benchmark'] == bench)]
            if len(sub) == 1:
                dev_matrix[i, j] = sub['deviation'].values[0]

    plot_heatmap(dev_matrix, pair_labels, benchmarks_avail,
                 'Benchmark-Specific Deviation (Δlz* − pair mean)',
                 os.path.join(OUT_DIR, "deviation_heatmap.png"))

    # --- Boxplot ---
    plot_boxplot(dev_df, benchmarks_avail,
                 os.path.join(OUT_DIR, "benchmark_boxplot.png"))

    # --- Scatter: Δacc vs Δlz* ---
    plot_scatter_delta_acc_vs_lz(pairs_df,
                                 os.path.join(OUT_DIR, "delta_acc_vs_lz.png"))

    # === Step 6: Save ===
    print("\n" + "=" * 60)
    print("Step 6: Saving results")
    print("=" * 60)

    pairs_df.to_csv(os.path.join(OUT_DIR, "pairs_data.csv"), index=False)
    dev_df.to_csv(os.path.join(OUT_DIR, "deviation_analysis.csv"), index=False)

    summary = {
        "n_pairs": len(PAIRS),
        "benchmarks": benchmarks_avail,
        "n_pair_benchmark_combinations": len(pairs_df),
        "n_complete_pairs": len(complete_pairs),
        "irt_fitting": {
            bench: {
                "n_models": len(bench_model_lists.get(bench, [])),
                "n_items": int(irt_params[bench][0].shape[0]) if bench in irt_params else 0,
                "c_param": float(irt_params[bench][2]) if bench in irt_params else None,
                "a_range": [float(irt_params[bench][0].min()), float(irt_params[bench][0].max())]
                    if bench in irt_params else None,
                "b_range": [float(irt_params[bench][1].min()), float(irt_params[bench][1].max())]
                    if bench in irt_params else None,
            }
            for bench in benchmarks_avail
        },
        "lz_star_per_benchmark": {
            bench: {
                "mean": float(np.mean([s['lz_star'] for s in benchmark_stats[bench].values()])),
                "std": float(np.std([s['lz_star'] for s in benchmark_stats[bench].values()])),
                "min": float(min(s['lz_star'] for s in benchmark_stats[bench].values())),
                "max": float(max(s['lz_star'] for s in benchmark_stats[bench].values())),
            }
            for bench in benchmarks_avail
        },
        "delta_lz_star_per_benchmark": {
            bench: {
                "mean": float(pairs_df[pairs_df['benchmark'] == bench]['delta_lz_star'].mean()),
                "std": float(pairs_df[pairs_df['benchmark'] == bench]['delta_lz_star'].std()),
            }
            for bench in benchmarks_avail
        },
        "deviation_tests": bench_dev_stats,
        "outlier_pairs": [
            {"pair": r['pair'], "benchmark": r['benchmark'],
             "delta_lz_star": r['delta_lz_star'],
             "deviation": r['deviation'], "zscore": r['within_pair_zscore']}
            for _, r in outliers.iterrows()
        ] if len(outliers) > 0 else [],
        "runtime_sec": time.time() - t_start,
    }

    with open(os.path.join(OUT_DIR, "natural_experiment_summary.json"), 'w') as f:
        json.dump(summary, f, indent=2)

    print(f"  pairs_data.csv: {len(pairs_df)} rows")
    print(f"  deviation_analysis.csv: {len(dev_df)} rows")
    print(f"  natural_experiment_summary.json")

    # === Generate Report ===
    print("\n" + "=" * 60)
    print("Generating report")
    print("=" * 60)

    report_lines = [
        "# Natural Experiment: Base→Chat Δlz* Cross-Benchmark Analysis",
        "",
        "## Overview",
        f"- **Pairs**: {len(PAIRS)} base/chat model pairs",
        f"- **Benchmarks**: {', '.join(benchmarks_avail)}",
        f"- **Complete pairs** (all benchmarks): {len(complete_pairs)}/{len(PAIRS)}",
        "",
        "## Hypothesis",
        "Instruction-tuning produces a consistent cross-benchmark Δlz* shift.",
        "Contamination on specific benchmarks manifests as outlier Δlz* on those",
        "benchmarks relative to the pair's mean Δlz* across benchmarks.",
        "",
        "## IRT Fitting Summary",
    ]
    for bench in benchmarks_avail:
        if bench in irt_params:
            a_arr = irt_params[bench][0]
            b_arr = irt_params[bench][1]
            c_val = irt_params[bench][2]
            n_m = len(bench_model_lists.get(bench, []))
            report_lines.append(
                f"- **{bench}**: {n_m} models × {len(a_arr)} items, "
                f"{'3PL' if c_val > 0 else '2PL'} (c={c_val}), "
                f"a∈[{a_arr.min():.2f}, {a_arr.max():.2f}], "
                f"b∈[{b_arr.min():.2f}, {b_arr.max():.2f}]"
            )

    report_lines += [
        "",
        "## lz* Distribution Per Benchmark",
    ]
    for bench in benchmarks_avail:
        vals = [s['lz_star'] for s in benchmark_stats[bench].values()]
        report_lines.append(
            f"- **{bench}**: mean={np.mean(vals):.2f}, std={np.std(vals):.2f}, "
            f"range=[{min(vals):.2f}, {max(vals):.2f}]"
        )

    report_lines += [
        "",
        "## Δlz* Across Benchmarks",
    ]
    for bench in benchmarks_avail:
        sub = pairs_df[pairs_df['benchmark'] == bench]
        report_lines.append(
            f"- **{bench}**: mean Δlz*={sub['delta_lz_star'].mean():+.2f} ± "
            f"{sub['delta_lz_star'].std():.2f}, "
            f"mean Δacc={sub['delta_acc'].mean():+.4f}"
        )

    report_lines += [
        "",
        "## Deviation Analysis",
        "For each pair, Δlz* deviation = Δlz*(benchmark) − mean Δlz*(pair).",
        "A positive deviation means lz* increased more on this benchmark than average.",
        "",
        "### Per-Benchmark Deviation (one-sample t-test, H0: mean=0)",
    ]
    for bench in benchmarks_avail:
        if bench in bench_dev_stats:
            s = bench_dev_stats[bench]
            sig = " **significant at p<0.05**" if s['p_value'] < 0.05 else ""
            report_lines.append(
                f"- **{bench}**: mean_dev={s['mean_deviation']:+.3f}, "
                f"t({s['n_pairs']-1})={s['t_statistic']:+.2f}, "
                f"p={s['p_value']:.4f}{sig}"
            )

    report_lines += [
        "",
        "### Outlier Pairs (|within-pair z| > 1.5)",
    ]
    if len(outliers) > 0:
        for _, r in outliers.iterrows():
            report_lines.append(
                f"- **{r['pair']}** × {r['benchmark']}: "
                f"Δlz*={r['delta_lz_star']:+.2f}, z={r['within_pair_zscore']:+.2f}"
            )
    else:
        report_lines.append("- None detected")

    report_lines += [
        "",
        "## Interpretation",
        "",
        "### Key Findings",
    ]

    # Auto-generate findings
    sig_benches = [b for b in benchmarks_avail
                   if b in bench_dev_stats and bench_dev_stats[b]['p_value'] < 0.05]
    if sig_benches:
        report_lines.append(
            f"1. Benchmarks with significant systematic deviation: **{', '.join(sig_benches)}**"
        )
    else:
        report_lines.append(
            "1. No benchmark shows a significant systematic deviation from the pair mean Δlz*."
        )

    n_out = len(outliers) if len(outliers) > 0 else 0
    report_lines.append(
        f"2. {n_out} (pair, benchmark) combinations flagged as outliers (|z| > 1.5)."
    )

    report_lines += [
        "",
        "### Caveats",
        "- lz* values are systematically miscalibrated (mean >> 0) due to model violations",
        "  of IRT assumptions. However, Δlz* deviations within pairs should be interpretable",
        "  since systematic bias cancels.",
        "- With only 4 benchmarks per pair, within-pair z-scores have very few degrees of freedom.",
        "- IRT parameters fitted on ~60 models may not generalize perfectly.",
        f"- Runtime: {time.time() - t_start:.0f}s",
        "",
        "## Files",
        "- `pairs_data.csv`: Per (pair, benchmark) raw data",
        "- `deviation_analysis.csv`: Deviation analysis",
        "- `delta_lz_heatmap.png`: Δlz* heatmap",
        "- `deviation_heatmap.png`: Deviation heatmap",
        "- `benchmark_boxplot.png`: Per-benchmark deviation boxplot",
        "- `delta_acc_vs_lz.png`: Δacc vs Δlz* scatter",
        "- `natural_experiment_summary.json`: Full statistics",
    ]

    report_path = os.path.join(OUT_DIR, "natural_experiment_report.md")
    with open(report_path, 'w') as f:
        f.write('\n'.join(report_lines))
    print(f"  Saved: {report_path}")

    total_time = time.time() - t_start
    print(f"\n{'=' * 60}")
    print(f"DONE in {total_time:.0f}s")
    print(f"  Pairs: {len(PAIRS)}, Benchmarks: {len(benchmarks_avail)}")
    print(f"  Data points: {len(pairs_df)}")
    if sig_benches:
        print(f"  Significant deviations: {', '.join(sig_benches)}")
    else:
        print("  No significant systematic deviations detected")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
