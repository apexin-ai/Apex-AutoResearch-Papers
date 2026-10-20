"""RRF Signal Analysis: C1 (rank correlation) + C2 (leave-one-out ablation)."""
import json
import os
import re
import numpy as np
from scipy.stats import spearmanr, kendalltau
from pathlib import Path

SIGNALS_DIR = "/root/autodl-tmp/exp002/signals"
BENCHMARKS = ["mmlu", "gsm8k", "arc_challenge"]
ACTIVE_SIGNALS = ["s1_embedding", "s2_minkpp", "s4_selfcritique"]
RRF_K = 60

# Signal orientation: True = negate before ranking (lower raw = more suspicious)
NEGATE = {"s1_embedding": False, "s2_minkpp": True, "s4_selfcritique": False}


def parse_dosage(dirname):
    """Extract dosage fraction from directory name."""
    m = re.search(r'_d(\d{3})', dirname)
    if m:
        return int(m.group(1)) / 100.0
    return None


def list_model_dirs():
    """List model directories that have merged signal files for all benchmarks."""
    models = []
    for name in sorted(os.listdir(SIGNALS_DIR)):
        dirpath = os.path.join(SIGNALS_DIR, name)
        if not os.path.isdir(dirpath):
            continue
        dosage = parse_dosage(name)
        if dosage is None:
            continue
        # Check merged files exist for at least one benchmark
        has_merged = any(
            os.path.exists(os.path.join(dirpath, f"signals_merged_{b}.json"))
            for b in BENCHMARKS
        )
        if has_merged:
            models.append({"dirname": name, "dosage": dosage, "path": dirpath})
    return models


def load_merged(model_path, benchmark):
    """Load signals_merged_{benchmark}.json, return list of dicts."""
    fpath = os.path.join(model_path, f"signals_merged_{benchmark}.json")
    if not os.path.exists(fpath):
        return None
    with open(fpath) as f:
        return json.load(f)


def compute_ranks(scores):
    """Rank from 1 (highest) to N."""
    order = np.argsort(-scores)
    ranks = np.empty_like(order, dtype=float)
    ranks[order] = np.arange(1, len(scores) + 1)
    return ranks


def compute_rrf(items, signals, k=RRF_K):
    """Compute RRF scores for given signal subset. Returns normalized mean."""
    n = len(items)
    if n == 0:
        return 0.0, np.zeros(0)
    
    rrf = np.zeros(n)
    for sig in signals:
        v = np.array([it.get(sig, 0.0) or 0.0 for it in items], dtype=float)
        if NEGATE.get(sig, False):
            v = -v
        ranks = compute_ranks(v)
        rrf += 1.0 / (k + ranks)
    
    mn, mx = rrf.min(), rrf.max()
    if mx > mn:
        rrf_norm = (rrf - mn) / (mx - mn)
    else:
        rrf_norm = rrf
    return float(rrf_norm.mean()), rrf_norm


def oriented_scores(items, sig):
    """Get signal scores oriented so higher = more suspicious."""
    v = np.array([it.get(sig, 0.0) or 0.0 for it in items], dtype=float)
    if NEGATE.get(sig, False):
        v = -v
    return v


# ════════════════════════════════════════════════════════
# C1: Signal Rank Correlation Matrix
# ════════════════════════════════════════════════════════

def compute_signal_correlations(models):
    """Per-benchmark Spearman rank correlation between signal pairs."""
    results = {}
    for bench in BENCHMARKS:
        pair_rhos = {f"{a}_vs_{b}": [] for i, a in enumerate(ACTIVE_SIGNALS)
                     for b in ACTIVE_SIGNALS[i+1:]}
        
        n_models = 0
        for m in models:
            items = load_merged(m["path"], bench)
            if items is None:
                continue
            
            # Check all 3 signals have non-null values
            sig_arrays = {}
            skip = False
            for sig in ACTIVE_SIGNALS:
                vals = [it.get(sig) for it in items]
                if all(v is None or v == 0.0 for v in vals):
                    skip = True
                    break
                sig_arrays[sig] = oriented_scores(items, sig)
            if skip:
                continue
            
            n_models += 1
            for i, a in enumerate(ACTIVE_SIGNALS):
                for b in ACTIVE_SIGNALS[i+1:]:
                    rho, _ = spearmanr(sig_arrays[a], sig_arrays[b])
                    pair_rhos[f"{a}_vs_{b}"].append(rho)
        
        # Build correlation matrix
        n_sig = len(ACTIVE_SIGNALS)
        matrix = np.eye(n_sig)
        pair_details = {}
        for i, a in enumerate(ACTIVE_SIGNALS):
            for j, b in enumerate(ACTIVE_SIGNALS):
                if i < j:
                    key = f"{a}_vs_{b}"
                    rhos = pair_rhos[key]
                    if rhos:
                        mean_rho = float(np.mean(rhos))
                        std_rho = float(np.std(rhos))
                        matrix[i, j] = mean_rho
                        matrix[j, i] = mean_rho
                        pair_details[key] = {
                            "mean_rho": round(mean_rho, 4),
                            "std_rho": round(std_rho, 4),
                            "n_models": len(rhos),
                            "per_model_rhos": [round(r, 4) for r in rhos]
                        }
        
        results[bench] = {
            "n_models": n_models,
            "signals": ACTIVE_SIGNALS,
            "correlation_matrix": matrix.tolist(),
            "pair_details": pair_details
        }
    
    return results


# ════════════════════════════════════════════════════════
# C2: Leave-One-Signal-Out Ablation
# ════════════════════════════════════════════════════════

def leave_one_out_ablation(models):
    """For each benchmark, compute full RRF and leave-one-out variants."""
    results = {}
    
    for bench in BENCHMARKS:
        # Collect model-level exposures for each signal config
        configs = {
            "full": ACTIVE_SIGNALS,
        }
        for sig in ACTIVE_SIGNALS:
            remaining = [s for s in ACTIVE_SIGNALS if s != sig]
            configs[f"drop_{sig}"] = remaining
        # Also single-signal baselines
        for sig in ACTIVE_SIGNALS:
            configs[f"only_{sig}"] = [sig]
        
        model_exposures = {cfg: [] for cfg in configs}
        dosages = []
        model_names = []
        valid_models = 0
        
        for m in models:
            items = load_merged(m["path"], bench)
            if items is None:
                continue
            
            # Check all signals present
            has_all = True
            for sig in ACTIVE_SIGNALS:
                vals = [it.get(sig) for it in items]
                if all(v is None or v == 0.0 for v in vals):
                    has_all = False
                    break
            if not has_all:
                continue
            
            valid_models += 1
            dosages.append(m["dosage"])
            model_names.append(m["dirname"])
            
            for cfg_name, cfg_signals in configs.items():
                mean_exp, _ = compute_rrf(items, cfg_signals)
                model_exposures[cfg_name].append(mean_exp)
        
        if valid_models < 3:
            continue
        
        dosages = np.array(dosages)
        
        # Compute metrics for each config
        config_metrics = {}
        full_exp = np.array(model_exposures["full"])
        
        for cfg_name, exps in model_exposures.items():
            exps = np.array(exps)
            
            # Spearman correlation with true dosage
            rho_dosage, p_dosage = spearmanr(exps, dosages)
            tau_dosage, p_tau = kendalltau(exps, dosages)
            
            # Rank correlation with full RRF (for ablation configs)
            if cfg_name != "full":
                rho_full, _ = spearmanr(exps, full_exp)
            else:
                rho_full = 1.0
            
            # MAE vs dosage (after linear rescaling to [0,1])
            if exps.max() > exps.min():
                exps_scaled = (exps - exps.min()) / (exps.max() - exps.min())
            else:
                exps_scaled = exps
            mae_dosage = float(np.mean(np.abs(exps_scaled - dosages)))
            
            config_metrics[cfg_name] = {
                "signals_used": configs[cfg_name],
                "spearman_rho_vs_dosage": round(float(rho_dosage), 4),
                "spearman_p_vs_dosage": round(float(p_dosage), 6),
                "kendall_tau_vs_dosage": round(float(tau_dosage), 4),
                "spearman_rho_vs_full_rrf": round(float(rho_full), 4),
                "mae_vs_dosage_scaled": round(mae_dosage, 4),
                "mean_exposure": round(float(exps.mean()), 6),
                "std_exposure": round(float(exps.std()), 6),
            }
        
        # Compute delta MAE (leave-one-out vs full)
        full_mae = config_metrics["full"]["mae_vs_dosage_scaled"]
        for sig in ACTIVE_SIGNALS:
            drop_key = f"drop_{sig}"
            if drop_key in config_metrics:
                config_metrics[drop_key]["delta_mae"] = round(
                    config_metrics[drop_key]["mae_vs_dosage_scaled"] - full_mae, 4)
                config_metrics[drop_key]["delta_rho"] = round(
                    config_metrics[drop_key]["spearman_rho_vs_dosage"] - 
                    config_metrics["full"]["spearman_rho_vs_dosage"], 4)
        
        # Signal importance ranking (by how much MAE increases when dropped)
        importance = []
        for sig in ACTIVE_SIGNALS:
            drop_key = f"drop_{sig}"
            if drop_key in config_metrics:
                importance.append({
                    "signal": sig,
                    "delta_mae_when_dropped": config_metrics[drop_key]["delta_mae"],
                    "delta_rho_when_dropped": config_metrics[drop_key]["delta_rho"],
                })
        importance.sort(key=lambda x: -x["delta_mae_when_dropped"])
        
        results[bench] = {
            "n_models": valid_models,
            "model_names": model_names,
            "dosages": [round(d, 4) for d in dosages.tolist()],
            "configs": config_metrics,
            "signal_importance_by_delta_mae": importance,
        }
    
    return results


# ════════════════════════════════════════════════════════
# Main
# ════════════════════════════════════════════════════════

def main():
    models = list_model_dirs()
    print(f"Found {len(models)} model directories with signal data")
    for m in models:
        print(f"  {m['dirname']} (dosage={m['dosage']})")
    
    # C1
    print("\n" + "="*60)
    print("C1: Signal Rank Correlation Matrix")
    print("="*60)
    corr_results = compute_signal_correlations(models)
    for bench, data in corr_results.items():
        print(f"\n--- {bench} (n_models={data['n_models']}) ---")
        sigs = data["signals"]
        matrix = np.array(data["correlation_matrix"])
        header = "            " + "  ".join(f"{s:>16s}" for s in sigs)
        print(header)
        for i, sig in enumerate(sigs):
            row = f"{sig:>16s}" + "  ".join(f"{matrix[i,j]:>16.4f}" for j in range(len(sigs)))
            print(row)
        for pair, detail in data["pair_details"].items():
            print(f"  {pair}: rho={detail['mean_rho']:.4f} ± {detail['std_rho']:.4f} (n={detail['n_models']})")
    
    # C2
    print("\n" + "="*60)
    print("C2: Leave-One-Signal-Out Ablation")
    print("="*60)
    ablation_results = leave_one_out_ablation(models)
    for bench, data in ablation_results.items():
        print(f"\n--- {bench} (n_models={data['n_models']}) ---")
        print(f"{'Config':<25s} {'Signals':<40s} {'ρ(dosage)':<12s} {'τ(dosage)':<12s} {'MAE':<10s} {'ΔMAE':<10s} {'ρ(full)':<10s}")
        for cfg_name, metrics in data["configs"].items():
            sigs_str = "+".join(s.replace("s1_embedding","S1").replace("s2_minkpp","S2").replace("s4_selfcritique","S4")
                               for s in metrics["signals_used"])
            delta = metrics.get("delta_mae", "")
            delta_str = f"{delta:+.4f}" if isinstance(delta, float) else ""
            print(f"{cfg_name:<25s} {sigs_str:<40s} {metrics['spearman_rho_vs_dosage']:<12.4f} "
                  f"{metrics['kendall_tau_vs_dosage']:<12.4f} {metrics['mae_vs_dosage_scaled']:<10.4f} "
                  f"{delta_str:<10s} {metrics['spearman_rho_vs_full_rrf']:<10.4f}")
        
        print("\nSignal importance (by ΔMAE when dropped, larger = more important):")
        for rank, entry in enumerate(data["signal_importance_by_delta_mae"], 1):
            print(f"  #{rank}: {entry['signal']} — ΔMAE={entry['delta_mae_when_dropped']:+.4f}, Δρ={entry['delta_rho_when_dropped']:+.4f}")
    
    # Save JSON
    output = {
        "c1_signal_correlation": corr_results,
        "c2_leave_one_out_ablation": ablation_results,
        "metadata": {
            "signals": ACTIVE_SIGNALS,
            "rrf_k": RRF_K,
            "negate_rules": NEGATE,
            "benchmarks": BENCHMARKS,
            "signals_dir": SIGNALS_DIR,
        }
    }
    
    outpath = "/root/contamcal-irt-calibration/analysis/rrf_signal_analysis.json"
    with open(outpath, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved to {outpath}")


if __name__ == "__main__":
    main()
