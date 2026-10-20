import json
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

BASE = "/root/entrainment_gated_ft"
OUT = f"{BASE}/results/a3_complementarity"
os.makedirs(OUT, exist_ok=True)

ARCHS = ["GDN", "RetNet", "HGRN2"]
RATIOS = ["pure", "h24-1", "h12-1", "h6-1", "h3-1"]
RATIO_LABELS = {"pure": "0%", "h24-1": "4%", "h12-1": "7.7%", "h6-1": "14.3%", "h3-1": "25%"}
BENCHMARKS = ["lambada", "hellaswag", "piqa", "arc_easy"]
BENCH_LABELS = {"lambada": "LAMBADA", "hellaswag": "HellaSwag", "piqa": "PIQA", "arc_easy": "ARC-Easy"}

ARCH_FILE_MAP = {"GDN": "GatedDeltaNet", "RetNet": "RetNet", "HGRN2": "HGRN2"}
RATIO_FILE_MAP = {"pure": "pure", "h24-1": "hybrid-24-1", "h12-1": "hybrid-12-1", "h6-1": "hybrid-6-1", "h3-1": "hybrid-3-1"}

BENCH_KEY_METRIC = {
    "lambada": ("lambada_openai", "acc,none"),
    "hellaswag": ("hellaswag", "acc_norm,none"),
    "piqa": ("piqa", "acc,none"),
    "arc_easy": ("arc_easy", "acc,none"),
}

def load_lm_eval_result(model_name, bench_key, metric_key):
    """Try multiple file locations and formats to find a result."""
    lm = f"{BASE}/lm_eval_clean"
    
    # Candidate paths
    candidates = [
        f"{lm}/{model_name}.json",
        f"{lm}/{model_name}_results.json",
        f"{lm}/{bench_key}/{model_name}/{model_name}.json",
        f"{lm}/{'arc_easy' if bench_key == 'arc_easy' else bench_key}/{model_name}/{model_name}.json",
    ]
    
    for fpath in candidates:
        if not os.path.exists(fpath):
            continue
        with open(fpath) as f:
            data = json.load(f)
        # Format 1: {"results": {"bench_key": {...}}}
        if "results" in data and bench_key in data["results"]:
            if metric_key in data["results"][bench_key]:
                return data["results"][bench_key][metric_key]
        # Format 2: {"bench_key": {...}} (flat)
        if bench_key in data and metric_key in data[bench_key]:
            return data[bench_key][metric_key]
    
    return None

def load_individual_accs():
    accs = {}
    for bench in BENCHMARKS:
        accs[bench] = {}
        bench_key, metric_key = BENCH_KEY_METRIC[bench]
        for ratio in RATIOS:
            accs[bench][ratio] = {}
            for arch in ARCHS:
                model_name = f"1.3B-100B-{ARCH_FILE_MAP[arch]}-{RATIO_FILE_MAP[ratio]}"
                val = load_lm_eval_result(model_name, bench_key, metric_key)
                if val is None:
                    print(f"  MISSING: {arch}-{ratio}-{bench}")
                accs[bench][ratio][arch] = val
    return accs

def load_disagreement_distributions():
    dd = {}
    with open(f"{BASE}/formal_multiplicity_metrics.json") as f:
        fmm = json.load(f)
    for bk in ["arc_easy", "lambada"]:
        dd[bk] = {}
        for ratio in RATIOS:
            dd[bk][ratio] = fmm[bk]["metrics"][ratio]["disagreement_distribution"]
    
    for bk, fp in [
        ("hellaswag", f"{BASE}/analysis_output/hellaswag_per_example.json"),
        ("boolq", f"{BASE}/analysis_output/boolq_per_example.json"),
    ]:
        with open(fp) as f:
            data = json.load(f)
        dd[bk] = {}
        for ratio in RATIOS:
            dd[bk][ratio] = data["ambiguity"][ratio]["disagreement_distribution"]
    
    with open(f"{BASE}/lm_eval_clean/analysis/piqa_per_example.json") as f:
        data = json.load(f)
    dd["piqa"] = {}
    for ratio in RATIOS:
        dd["piqa"][ratio] = data["ambiguity"][ratio]["disagreement_distribution"]
    
    return dd

def compute_decomposition(dd, individual_accs):
    results = {}
    for bench in BENCHMARKS:
        results[bench] = {}
        for ratio in RATIOS:
            d = dd[bench][ratio]
            uw = d["0_of_3"]
            mC = d["1_of_3"]
            MC = d["2_of_3"]
            uc = d["3_of_3"]
            N = uw + mC + MC + uc
            
            mean_ind_acc = (1 * mC + 2 * MC + 3 * uc) / (3 * N)
            mv_acc = (MC + uc) / N
            oracle_acc = (mC + MC + uc) / N
            
            arch_accs = individual_accs[bench][ratio]
            valid_accs = {k: v for k, v in arch_accs.items() if v is not None}
            best_single = max(valid_accs.values()) if valid_accs else None
            best_arch = max(valid_accs, key=valid_accs.get) if valid_accs else None
            
            contested = (mC + MC) / N
            
            ci = None
            if contested > 0 and best_single is not None:
                ci = (oracle_acc - best_single) / contested
            
            mv_eff = None
            if best_single is not None and (oracle_acc - best_single) > 1e-10:
                mv_eff = (mv_acc - best_single) / (oracle_acc - best_single)
            
            wasted = mC / N
            
            results[bench][ratio] = {
                "N": N,
                "UC": uc, "UW": uw, "MC": MC, "mC": mC,
                "UC_pct": uc / N * 100, "UW_pct": uw / N * 100,
                "MC_pct": MC / N * 100, "mC_pct": mC / N * 100,
                "mean_individual_acc": round(mean_ind_acc * 100, 2),
                "best_single_acc": round(best_single * 100, 2) if best_single else None,
                "best_single_arch": best_arch,
                "mv_acc": round(mv_acc * 100, 2),
                "oracle_acc": round(oracle_acc * 100, 2),
                "contested_fraction": round(contested * 100, 2),
                "complementarity_index": round(ci, 4) if ci is not None else None,
                "mv_efficiency": round(mv_eff, 4) if mv_eff is not None else None,
                "wasted_complementarity": round(wasted * 100, 2),
                "individual_accs": {k: round(v * 100, 2) if v else None for k, v in arch_accs.items()},
            }
    return results

# ── Visualization ──────────────────────────────────────────────────────────

def plot_stacked_bars(results):
    plt.rcParams.update({
        'font.size': 13, 'axes.labelsize': 14,
        'xtick.labelsize': 12, 'ytick.labelsize': 12,
        'legend.fontsize': 11, 'font.family': 'serif',
    })
    fig, axes = plt.subplots(1, 4, figsize=(16, 4.5), sharey=True)
    colors = {'UC': '#2ecc71', 'MC': '#3498db', 'mC': '#f39c12', 'UW': '#e74c3c'}
    bw = 0.6
    
    for idx, bench in enumerate(BENCHMARKS):
        ax = axes[idx]
        xp = np.arange(len(RATIOS))
        uc = [results[bench][r]["UC_pct"] for r in RATIOS]
        mc = [results[bench][r]["MC_pct"] for r in RATIOS]
        mc_min = [results[bench][r]["mC_pct"] for r in RATIOS]
        uw = [results[bench][r]["UW_pct"] for r in RATIOS]
        
        ax.bar(xp, uw, bw, label='UW (all wrong)', color=colors['UW'])
        ax.bar(xp, mc_min, bw, bottom=uw, label='mC (1/3 right)', color=colors['mC'])
        b2 = [a+b for a,b in zip(uw, mc_min)]
        ax.bar(xp, mc, bw, bottom=b2, label='MC (2/3 right)', color=colors['MC'])
        b3 = [a+b for a,b in zip(b2, mc)]
        ax.bar(xp, uc, bw, bottom=b3, label='UC (all right)', color=colors['UC'])
        
        mv = [results[bench][r]["mv_acc"] for r in RATIOS]
        orc = [results[bench][r]["oracle_acc"] for r in RATIOS]
        ax.plot(xp, mv, 'k^-', ms=6, lw=1.5, label='MV acc', zorder=5)
        ax.plot(xp, orc, 'kD--', ms=5, lw=1.5, label='Oracle acc', zorder=5)
        
        ax.set_title(BENCH_LABELS[bench], fontsize=14, fontweight='bold')
        ax.set_xticks(xp)
        ax.set_xticklabels([RATIO_LABELS[r] for r in RATIOS])
        ax.set_xlabel("Attention Ratio")
        if idx == 0:
            ax.set_ylabel("Proportion (%)")
        ax.set_ylim(0, 105)
    
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc='upper center', ncol=6, bbox_to_anchor=(0.5, 1.08), frameon=False)
    plt.tight_layout()
    fig.savefig(f"{OUT}/fig_complementarity_stacked.pdf", bbox_inches='tight', dpi=300)
    fig.savefig(f"{OUT}/fig_complementarity_stacked.png", bbox_inches='tight', dpi=200)
    plt.close()
    print("Saved stacked bar chart")


def plot_metrics_lines(results):
    plt.rcParams.update({
        'font.size': 13, 'axes.labelsize': 14,
        'xtick.labelsize': 12, 'ytick.labelsize': 12,
        'legend.fontsize': 12, 'font.family': 'serif',
    })
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.5))
    attn = [0, 4, 7.7, 14.3, 25]
    mk = ['o', 's', '^', 'D']
    cl = ['#e74c3c', '#3498db', '#2ecc71', '#9b59b6']
    
    for i, bench in enumerate(BENCHMARKS):
        ci = [results[bench][r]["complementarity_index"] for r in RATIOS]
        eff = [results[bench][r]["mv_efficiency"] for r in RATIOS]
        
        vci = [(x,y) for x,y in zip(attn, ci) if y is not None]
        if vci:
            xs, ys = zip(*vci)
            ax1.plot(xs, ys, marker=mk[i], color=cl[i], label=BENCH_LABELS[bench], lw=2, ms=8)
        
        veff = [(x,y) for x,y in zip(attn, eff) if y is not None]
        if veff:
            xs, ys = zip(*veff)
            ax2.plot(xs, ys, marker=mk[i], color=cl[i], label=BENCH_LABELS[bench], lw=2, ms=8)
    
    ax1.set_xlabel("Attention Ratio (%)")
    ax1.set_ylabel("Complementarity Index")
    ax1.set_title("Complementarity Index", fontweight='bold')
    ax1.legend(frameon=False)
    ax1.grid(alpha=0.3)
    
    ax2.set_xlabel("Attention Ratio (%)")
    ax2.set_ylabel("MV Efficiency")
    ax2.set_title("Majority Vote Efficiency", fontweight='bold')
    ax2.legend(frameon=False)
    ax2.grid(alpha=0.3)
    ax2.axhline(y=1.0, color='gray', ls=':', alpha=0.5)
    ax2.axhline(y=0.0, color='gray', ls=':', alpha=0.5)
    
    plt.tight_layout()
    fig.savefig(f"{OUT}/fig_complementarity_metrics.pdf", bbox_inches='tight', dpi=300)
    fig.savefig(f"{OUT}/fig_complementarity_metrics.png", bbox_inches='tight', dpi=200)
    plt.close()
    print("Saved metrics line plots")


def plot_wasted_contested(results):
    plt.rcParams.update({
        'font.size': 13, 'axes.labelsize': 14,
        'xtick.labelsize': 12, 'ytick.labelsize': 12,
        'legend.fontsize': 12, 'font.family': 'serif',
    })
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.5))
    attn = [0, 4, 7.7, 14.3, 25]
    mk = ['o', 's', '^', 'D']
    cl = ['#e74c3c', '#3498db', '#2ecc71', '#9b59b6']
    
    for i, bench in enumerate(BENCHMARKS):
        w = [results[bench][r]["wasted_complementarity"] for r in RATIOS]
        c = [results[bench][r]["contested_fraction"] for r in RATIOS]
        ax1.plot(attn, w, marker=mk[i], color=cl[i], label=BENCH_LABELS[bench], lw=2, ms=8)
        ax2.plot(attn, c, marker=mk[i], color=cl[i], label=BENCH_LABELS[bench], lw=2, ms=8)
    
    ax1.set_xlabel("Attention Ratio (%)")
    ax1.set_ylabel("Wasted Complementarity (%)")
    ax1.set_title("Wasted Complementarity (mC)", fontweight='bold')
    ax1.legend(frameon=False)
    ax1.grid(alpha=0.3)
    
    ax2.set_xlabel("Attention Ratio (%)")
    ax2.set_ylabel("Contested Fraction (%)")
    ax2.set_title("Contested Samples (mC + MC)", fontweight='bold')
    ax2.legend(frameon=False)
    ax2.grid(alpha=0.3)
    
    plt.tight_layout()
    fig.savefig(f"{OUT}/fig_complementarity_trends.pdf", bbox_inches='tight', dpi=300)
    fig.savefig(f"{OUT}/fig_complementarity_trends.png", bbox_inches='tight', dpi=200)
    plt.close()
    print("Saved trend plots")


# ── Main ───────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("Loading individual architecture accuracies...")
    individual_accs = load_individual_accs()
    
    print("\nLoading disagreement distributions...")
    dd = load_disagreement_distributions()
    
    print("\nComputing decomposition...")
    results = compute_decomposition(dd, individual_accs)
    
    print("\n" + "="*110)
    print("COMPLEMENTARITY DECOMPOSITION SUMMARY")
    print("="*110)
    
    for bench in BENCHMARKS:
        N = results[bench]['pure']['N']
        print(f"\n--- {BENCH_LABELS[bench]} (N={N}) ---")
        hdr = f"{'Ratio':<8} {'UC%':>6} {'MC%':>6} {'mC%':>6} {'UW%':>6} | {'MeanAcc':>8} {'Best':>8} {'MV':>8} {'Oracle':>8} | {'CI':>8} {'MVEff':>8} {'Waste%':>8}"
        print(hdr)
        print("-" * len(hdr))
        for ratio in RATIOS:
            r = results[bench][ratio]
            ci_s = f"{r['complementarity_index']:.4f}" if r['complementarity_index'] is not None else "N/A"
            eff_s = f"{r['mv_efficiency']:.4f}" if r['mv_efficiency'] is not None else "N/A"
            bs = f"{r['best_single_acc']:.2f}%" if r['best_single_acc'] is not None else "N/A"
            print(f"{ratio:<8} {r['UC_pct']:>6.1f} {r['MC_pct']:>6.1f} {r['mC_pct']:>6.1f} {r['UW_pct']:>6.1f} | "
                  f"{r['mean_individual_acc']:>7.2f}% {bs:>8} {r['mv_acc']:>7.2f}% {r['oracle_acc']:>7.2f}% | "
                  f"{ci_s:>8} {eff_s:>8} {r['wasted_complementarity']:>7.2f}%")
    
    output_data = {
        "description": "A3 Complementarity Decomposition",
        "scale": "1.3B parameters",
        "architectures": ARCHS,
        "ratios": RATIOS,
        "ratio_attention_pct": RATIO_LABELS,
        "categories": {
            "UC": "Universal Correct (3/3 correct)",
            "MC": "Majority Correct (2/3 correct)",
            "mC": "Minority Correct (1/3 correct, wasted complementarity)",
            "UW": "Universal Wrong (0/3 correct)"
        },
        "metrics_definition": {
            "complementarity_index": "(Oracle_acc - Best_single_acc) / Contested_fraction",
            "mv_efficiency": "(MV_acc - Best_single_acc) / (Oracle_acc - Best_single_acc)",
            "wasted_complementarity": "mC / N"
        },
        "results": results
    }
    
    with open(f"{OUT}/complementarity_decomposition.json", "w") as f:
        json.dump(output_data, f, indent=2)
    print(f"\nSaved: {OUT}/complementarity_decomposition.json")
    
    print("\nGenerating visualizations...")
    plot_stacked_bars(results)
    plot_metrics_lines(results)
    plot_wasted_contested(results)
    
    print("\nAll outputs:")
    for fn in sorted(os.listdir(OUT)):
        fsize = os.path.getsize(f"{OUT}/{fn}")
        print(f"  {fn} ({fsize} bytes)")
