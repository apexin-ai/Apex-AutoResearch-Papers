"""D127 Track F: Wasserstein Distance Tail Canary Analysis.

Computes token-frequency W-1 distance per generation vs gen_0,
then runs PermG to test whether W-1 detects collapse earlier than entropy
in the blind zone (α≤0.45).
"""

import json
import os
import sys
import numpy as np
from collections import Counter
from pathlib import Path

sys.path.insert(0, "/root/autodl-tmp/distrib_canary_collapse")
from permutation_granger import permutation_granger_test

BASE = "/root/autodl-tmp/distrib_canary_collapse"
N_PERM = 5000

EXPERIMENTS = {
    "a010": "results/alpha_sweep/a010_s42_fp32",
    "a025": "results/alpha_sweep/a025_s42_fp32",
    "a030": "results/alpha_sweep/a030_s42_fp32",
    "a035": "results/alpha_sweep/a035_s42_fp32",
    "a040": "results/alpha_sweep/a040_s42_fp32",
    "a045": "results/alpha_sweep/a045_s42_fp32",
    "a050": "results/alpha_sweep/a050_s42_fp32",
    "a075": "results/alpha_sweep/a075_s42_fp32",
}

DOWNSTREAMS = ["distinct_1", "distinct_2", "distinct_3", "mauve"]


def load_token_freqs(data_dir):
    """Load per-generation token frequency Counters from synthetic_data."""
    from datasets import load_from_disk
    gen_dirs = sorted(
        [d for d in Path(data_dir).iterdir() if d.name.startswith("gen_")],
        key=lambda d: int(d.name.split("_")[1])
    )
    freqs = []
    for gd in gen_dirs:
        sd_path = gd / "synthetic_data"
        if not sd_path.exists():
            freqs.append(Counter())
            continue
        ds = load_from_disk(str(sd_path))
        counter = Counter()
        for row in ds:
            counter.update(row["text"].split())
        freqs.append(counter)
    return freqs


def compute_wasserstein_series(freqs):
    """Compute W-1 distance between each gen's token freq dist and gen_0's.

    Tokens are ordered by gen_0 frequency rank (descending).
    W-1 is computed over this 1D rank space, measuring how probability mass
    shifts between frequent and rare tokens across generations.
    """
    from scipy.stats import wasserstein_distance

    vocab = set()
    for c in freqs:
        vocab.update(c.keys())
    vocab = sorted(vocab, key=lambda t: -freqs[0].get(t, 0))

    total_0 = sum(freqs[0].values()) or 1
    p0 = np.array([freqs[0].get(t, 0) / total_0 for t in vocab])
    ranks = np.arange(1, len(vocab) + 1, dtype=float)

    w1_series = [0.0]
    for i in range(1, len(freqs)):
        total_i = sum(freqs[i].values()) or 1
        pi = np.array([freqs[i].get(t, 0) / total_i for t in vocab])
        w1 = wasserstein_distance(ranks, ranks, p0, pi)
        w1_series.append(float(w1))

    return w1_series


def load_metric_series(data_dir):
    all_path = os.path.join(data_dir, "all_metrics.json")
    with open(all_path) as f:
        data = json.load(f)
    data.sort(key=lambda x: x["generation"])
    series = {}
    for k in ["token_entropy", "effective_rank"] + DOWNSTREAMS:
        series[k] = np.array([d[k] for d in data])
    return series


def bh_fdr(pvals, q=0.05):
    pvals = np.array(pvals, dtype=float)
    n = len(pvals)
    valid = ~np.isnan(pvals)
    adjusted = np.full(n, np.nan)
    significant = np.full(n, False)
    if valid.sum() == 0:
        return adjusted, significant
    idx = np.where(valid)[0]
    p_sub = pvals[idx]
    order = np.argsort(p_sub)
    ranks = np.empty_like(order)
    ranks[order] = np.arange(1, len(p_sub) + 1)
    adj = p_sub * len(p_sub) / ranks
    adj = np.minimum.accumulate(adj[np.argsort(-ranks)])[np.argsort(np.argsort(-ranks))]
    adj = np.clip(adj, 0, 1)
    adjusted[idx] = adj
    significant[idx] = adj < q
    return adjusted, significant


def run_permg_battery(canary_series, metric_series, downstreams):
    """Run PermG fwd+rev for canary vs each downstream."""
    results = []
    for dn in downstreams:
        ds = metric_series[dn]
        fwd = permutation_granger_test(canary_series, ds, max_lag=1, n_perm=N_PERM, seed=42)
        rev = permutation_granger_test(ds, canary_series, max_lag=1, n_perm=N_PERM, seed=42)
        results.append({
            "downstream": dn,
            "fwd_f": fwd["f_stat"], "fwd_p": fwd["p_value"], "fwd_f2": fwd["effect_size_f2"],
            "rev_f": rev["f_stat"], "rev_p": rev["p_value"], "rev_f2": rev["effect_size_f2"],
        })
    return results


def main():
    out_dir = os.path.join(BASE, "artifacts", "d127_wasserstein")
    os.makedirs(out_dir, exist_ok=True)

    all_results = {}
    w1_all = {}

    for alpha_label, rel_path in sorted(EXPERIMENTS.items()):
        data_dir = os.path.join(BASE, rel_path)
        alpha_val = int(alpha_label[1:]) / 100.0
        print(f"\n{'='*60}")
        print(f"α={alpha_val:.2f} ({alpha_label})")
        print(f"{'='*60}")

        print("  Loading token frequencies...")
        freqs = load_token_freqs(data_dir)
        print(f"  Loaded {len(freqs)} generations, vocab sizes: {[len(c) for c in freqs]}")

        print("  Computing W-1 series...")
        w1_series = compute_wasserstein_series(freqs)
        w1_all[alpha_label] = w1_series
        print(f"  W-1: {[round(v, 4) for v in w1_series]}")

        print("  Loading metric series...")
        metrics = load_metric_series(data_dir)

        w1_arr = np.array(w1_series)

        print("  Running PermG: W-1 → downstream...")
        w1_permg = run_permg_battery(w1_arr, metrics, DOWNSTREAMS)

        print("  Running PermG: entropy → downstream...")
        ent_permg = run_permg_battery(metrics["token_entropy"], metrics, DOWNSTREAMS)

        print("  Running PermG: effective_rank → downstream...")
        erank_permg = run_permg_battery(metrics["effective_rank"], metrics, DOWNSTREAMS)

        # FDR across all pairs for this alpha
        all_pvals = []
        all_pairs = []
        for label, pairs in [("w1", w1_permg), ("entropy", ent_permg), ("erank", erank_permg)]:
            for p in pairs:
                all_pvals.append(p["fwd_p"] if p["fwd_p"] is not None else float('nan'))
                all_pairs.append((label, p))

        adj_pvals, sig_fdr = bh_fdr(all_pvals)
        for i, (label, p) in enumerate(all_pairs):
            p["fwd_p_fdr"] = round(float(adj_pvals[i]), 6) if not np.isnan(adj_pvals[i]) else None
            p["fwd_sig_fdr"] = bool(sig_fdr[i])

        all_results[alpha_label] = {
            "alpha": alpha_val,
            "w1_series": w1_series,
            "entropy_series": metrics["token_entropy"].tolist(),
            "erank_series": metrics["effective_rank"].tolist(),
            "permg_w1": w1_permg,
            "permg_entropy": ent_permg,
            "permg_erank": erank_permg,
        }

        # Print summary table
        print(f"\n  {'Canary':<14} {'Downstream':<12} {'fwd_F':>8} {'fwd_p':>8} {'p_FDR':>8} {'Sig':>4}")
        print(f"  {'-'*56}")
        for label, pairs in [("W-1", w1_permg), ("entropy", ent_permg), ("eff_rank", erank_permg)]:
            for p in pairs:
                f_s = f"{p['fwd_f']:.3f}" if p['fwd_f'] is not None else "N/A"
                p_s = f"{p['fwd_p']:.4f}" if p['fwd_p'] is not None else "N/A"
                pf_s = f"{p['fwd_p_fdr']:.4f}" if p['fwd_p_fdr'] is not None else "N/A"
                sig = "*" if p.get('fwd_sig_fdr') else ""
                print(f"  {label:<14} {p['downstream']:<12} {f_s:>8} {p_s:>8} {pf_s:>8} {sig:>4}")

    # ===================== SUMMARY =====================
    print(f"\n\n{'='*80}")
    print("BLIND ZONE ANALYSIS: FDR-significant pairs per canary x alpha")
    print(f"{'='*80}")

    alphas = sorted(all_results.keys())
    header = f"  {'Canary':<14}" + "".join(f"  α={int(a[1:])/100:.2f}" for a in alphas)
    print(header)
    print(f"  {'-'*len(header)}")

    for canary_label, key in [("W-1", "permg_w1"), ("entropy", "permg_entropy"), ("eff_rank", "permg_erank")]:
        counts = []
        for a in alphas:
            pairs = all_results[a][key]
            n_sig = sum(1 for p in pairs if p.get("fwd_sig_fdr"))
            counts.append(f"{n_sig}/{len(pairs)}")
        print(f"  {canary_label:<14}" + "".join(f"  {c:>6}" for c in counts))

    # Blind zone detection summary
    blind_zone = [a for a in alphas if int(a[1:]) <= 45]
    print(f"\nBLIND ZONE (α≤0.45) detection count (FDR-sig pairs):")
    for canary_label, key in [("W-1", "permg_w1"), ("entropy", "permg_entropy"), ("eff_rank", "permg_erank")]:
        total_sig = 0
        total_pairs = 0
        for a in blind_zone:
            pairs = all_results[a][key]
            total_sig += sum(1 for p in pairs if p.get("fwd_sig_fdr"))
            total_pairs += len(pairs)
        print(f"  {canary_label:<14}: {total_sig}/{total_pairs}")

    # Save JSON
    json_path = os.path.join(out_dir, "d127_wasserstein.json")
    with open(json_path, "w") as f:
        json.dump(all_results, f, indent=2, default=str)
    print(f"\nJSON saved: {json_path}")

    # ===================== PLOT =====================
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Panel 1: W-1 time series across alpha regimes
    ax = axes[0, 0]
    cmap = plt.cm.RdYlGn_r
    for i, a in enumerate(alphas):
        alpha_val = int(a[1:]) / 100.0
        color = cmap(alpha_val)
        ax.plot(range(len(w1_all[a])), w1_all[a], 'o-', color=color, label=f"α={alpha_val:.2f}", markersize=4)
    ax.set_xlabel("Generation")
    ax.set_ylabel("W-1 Distance (vs gen_0)")
    ax.set_title("Token-Frequency W-1 Across α Regimes")
    ax.legend(fontsize=7, ncol=2)
    ax.grid(True, alpha=0.3)

    # Panel 2: W-1 final value vs alpha
    ax = axes[0, 1]
    alpha_vals = [int(a[1:]) / 100 for a in alphas]
    w1_finals = [w1_all[a][-1] for a in alphas]
    ax.plot(alpha_vals, w1_finals, 'ko-', markersize=6)
    ax.set_xlabel("α")
    ax.set_ylabel("W-1 at Final Generation")
    ax.set_title("W-1 Magnitude vs α")
    ax.axvspan(0, 0.45, alpha=0.15, color='red', label='Blind zone')
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Panel 3: PermG p-values comparison (W-1 vs entropy vs erank) across alphas
    ax = axes[1, 0]
    for canary_label, key, marker, color in [
        ("W-1", "permg_w1", "s", "tab:blue"),
        ("entropy", "permg_entropy", "o", "tab:orange"),
        ("eff_rank", "permg_erank", "^", "tab:green"),
    ]:
        min_pvals = []
        for a in alphas:
            pairs = all_results[a][key]
            pvals = [p["fwd_p"] for p in pairs if p["fwd_p"] is not None]
            min_pvals.append(min(pvals) if pvals else 1.0)
        ax.plot(alpha_vals, min_pvals, f'{marker}-', color=color, label=canary_label, markersize=6)
    ax.axhline(0.05, color='gray', ls='--', alpha=0.5, label='p=0.05')
    ax.axvspan(0, 0.45, alpha=0.15, color='red')
    ax.set_xlabel("α")
    ax.set_ylabel("min(fwd p-value) across downstreams")
    ax.set_title("PermG Sensitivity: W-1 vs Entropy vs Eff.Rank")
    ax.set_yscale('log')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel 4: FDR-sig count heatmap
    ax = axes[1, 1]
    canary_labels = ["W-1", "entropy", "eff_rank"]
    canary_keys = ["permg_w1", "permg_entropy", "permg_erank"]
    heatmap = np.zeros((len(canary_labels), len(alphas)))
    for ci, key in enumerate(canary_keys):
        for ai, a in enumerate(alphas):
            pairs = all_results[a][key]
            heatmap[ci, ai] = sum(1 for p in pairs if p.get("fwd_sig_fdr"))

    im = ax.imshow(heatmap, aspect='auto', cmap='YlOrRd', vmin=0, vmax=4)
    ax.set_xticks(range(len(alphas)))
    ax.set_xticklabels([f"{int(a[1:])/100:.2f}" for a in alphas], fontsize=8)
    ax.set_yticks(range(len(canary_labels)))
    ax.set_yticklabels(canary_labels)
    ax.set_xlabel("α")
    ax.set_title("FDR-Significant Pairs (out of 4 downstreams)")
    for ci in range(len(canary_labels)):
        for ai in range(len(alphas)):
            ax.text(ai, ci, f"{int(heatmap[ci, ai])}", ha='center', va='center', fontsize=9,
                    color='white' if heatmap[ci, ai] > 2 else 'black')
    plt.colorbar(im, ax=ax)

    plt.tight_layout()
    png_path = os.path.join(out_dir, "wasserstein_canary.png")
    fig.savefig(png_path, dpi=150, bbox_inches='tight')
    print(f"PNG saved: {png_path}")
    plt.close()

    return all_results


if __name__ == "__main__":
    main()
