"""RRF Signal Analysis v2: filtered models, cleaner ablation."""
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
NEGATE = {"s1_embedding": False, "s2_minkpp": True, "s4_selfcritique": False}

# C006 blacklist + duplicates
EXCLUDE_PATTERNS = [
    "DEPRECATED", "old_alpha16",
    # alpha=16 blacklist from C006
    "Qwen2.5-3B_d000_s42",  # no _a32 suffix = alpha=16
    "Qwen2.5-3B_d005_s42",  # same
    "Qwen2.5-3B_d025_s42",  # same (not v3)
    "Qwen2.5-3B_d100_s42",  # same
]

def should_exclude(dirname):
    for pat in EXCLUDE_PATTERNS:
        if pat in dirname:
            # But allow _a32 variants
            if pat.startswith("Qwen2.5-3B_d") and "_a32" in dirname:
                continue
            if pat.startswith("Qwen2.5-3B_d") and "_v3" in dirname:
                continue
            if pat.startswith("Qwen2.5-3B_d") and "_s123" in dirname:
                continue
            return True
    return False


def parse_dosage(dirname):
    m = re.search(r'_d(\d{3})', dirname)
    if m:
        return int(m.group(1)) / 100.0
    return None


def parse_scale(dirname):
    if "0.5B" in dirname:
        return "0.5B"
    elif "1.5B" in dirname:
        return "1.5B"
    elif "3B" in dirname:
        return "3B"
    elif "Llama" in dirname:
        return "Llama-3B"
    return "unknown"


def list_model_dirs():
    models = []
    for name in sorted(os.listdir(SIGNALS_DIR)):
        dirpath = os.path.join(SIGNALS_DIR, name)
        if not os.path.isdir(dirpath):
            continue
        dosage = parse_dosage(name)
        if dosage is None:
            continue
        if should_exclude(name):
            continue
        has_merged = any(
            os.path.exists(os.path.join(dirpath, f"signals_merged_{b}.json"))
            for b in BENCHMARKS
        )
        if has_merged:
            models.append({
                "dirname": name, "dosage": dosage,
                "path": dirpath, "scale": parse_scale(name)
            })
    return models


def load_merged(model_path, benchmark):
    fpath = os.path.join(model_path, f"signals_merged_{benchmark}.json")
    if not os.path.exists(fpath):
        return None
    with open(fpath) as f:
        return json.load(f)


def compute_ranks(scores):
    order = np.argsort(-scores)
    ranks = np.empty_like(order, dtype=float)
    ranks[order] = np.arange(1, len(scores) + 1)
    return ranks


def compute_rrf(items, signals, k=RRF_K):
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
    v = np.array([it.get(sig, 0.0) or 0.0 for it in items], dtype=float)
    if NEGATE.get(sig, False):
        v = -v
    return v


def has_all_signals(items):
    for sig in ACTIVE_SIGNALS:
        vals = [it.get(sig) for it in items]
        if all(v is None or v == 0.0 for v in vals):
            return False
    return True


# ═══════════════ C1 ═══════════════

def compute_signal_correlations(models):
    results = {}
    for bench in BENCHMARKS:
        pair_rhos = {f"{a}_vs_{b}": [] for i, a in enumerate(ACTIVE_SIGNALS)
                     for b in ACTIVE_SIGNALS[i+1:]}
        model_details = []
        
        for m in models:
            items = load_merged(m["path"], bench)
            if items is None or not has_all_signals(items):
                continue
            
            sig_arrays = {sig: oriented_scores(items, sig) for sig in ACTIVE_SIGNALS}
            model_rhos = {}
            for i, a in enumerate(ACTIVE_SIGNALS):
                for b in ACTIVE_SIGNALS[i+1:]:
                    key = f"{a}_vs_{b}"
                    rho, _ = spearmanr(sig_arrays[a], sig_arrays[b])
                    pair_rhos[key].append(rho)
                    model_rhos[key] = round(float(rho), 4)
            model_details.append({"model": m["dirname"], "dosage": m["dosage"], "correlations": model_rhos})
        
        n_sig = len(ACTIVE_SIGNALS)
        matrix = np.eye(n_sig)
        pair_summary = {}
        for i, a in enumerate(ACTIVE_SIGNALS):
            for j, b in enumerate(ACTIVE_SIGNALS):
                if i < j:
                    key = f"{a}_vs_{b}"
                    rhos = pair_rhos[key]
                    if rhos:
                        mean_rho = float(np.mean(rhos))
                        matrix[i, j] = mean_rho
                        matrix[j, i] = mean_rho
                        pair_summary[key] = {
                            "mean_rho": round(mean_rho, 4),
                            "std_rho": round(float(np.std(rhos)), 4),
                            "min_rho": round(float(np.min(rhos)), 4),
                            "max_rho": round(float(np.max(rhos)), 4),
                            "n_models": len(rhos),
                        }
        
        results[bench] = {
            "n_models": len(model_details),
            "signals": ACTIVE_SIGNALS,
            "correlation_matrix": [[round(x, 4) for x in row] for row in matrix.tolist()],
            "pair_summary": pair_summary,
            "per_model": model_details,
        }
    return results


# ═══════════════ C2 ═══════════════

def leave_one_out_ablation(models):
    results = {}
    for bench in BENCHMARKS:
        configs = {"full": ACTIVE_SIGNALS}
        for sig in ACTIVE_SIGNALS:
            configs[f"drop_{sig}"] = [s for s in ACTIVE_SIGNALS if s != sig]
        for sig in ACTIVE_SIGNALS:
            configs[f"only_{sig}"] = [sig]
        
        model_exposures = {cfg: [] for cfg in configs}
        # Also store per-item RRF for rank correlation between full and ablated
        item_rrf_full = []
        item_rrf_ablated = {f"drop_{sig}": [] for sig in ACTIVE_SIGNALS}
        dosages = []
        model_names = []
        scales = []
        
        for m in models:
            items = load_merged(m["path"], bench)
            if items is None or not has_all_signals(items):
                continue
            
            dosages.append(m["dosage"])
            model_names.append(m["dirname"])
            scales.append(m["scale"])
            
            for cfg_name, cfg_signals in configs.items():
                mean_exp, item_scores = compute_rrf(items, cfg_signals)
                model_exposures[cfg_name].append(mean_exp)
                if cfg_name == "full":
                    item_rrf_full.append(item_scores)
                elif cfg_name.startswith("drop_"):
                    item_rrf_ablated[cfg_name].append(item_scores)
        
        n_models = len(dosages)
        if n_models < 3:
            continue
        dosages = np.array(dosages)
        
        # Item-level rank correlation between full and ablated (averaged over models)
        item_rank_corr = {}
        for drop_key in item_rrf_ablated:
            rhos = []
            for i in range(n_models):
                if len(item_rrf_full[i]) > 0 and len(item_rrf_ablated[drop_key][i]) > 0:
                    rho, _ = spearmanr(item_rrf_full[i], item_rrf_ablated[drop_key][i])
                    rhos.append(rho)
            if rhos:
                item_rank_corr[drop_key] = {
                    "mean_item_rho_vs_full": round(float(np.mean(rhos)), 4),
                    "std": round(float(np.std(rhos)), 4),
                }
        
        config_metrics = {}
        full_exp = np.array(model_exposures["full"])
        
        for cfg_name, exps in model_exposures.items():
            exps = np.array(exps)
            rho_dosage, p_dosage = spearmanr(exps, dosages)
            tau_dosage, p_tau = kendalltau(exps, dosages)
            
            if cfg_name != "full":
                rho_full, _ = spearmanr(exps, full_exp)
            else:
                rho_full = 1.0
            
            if exps.max() > exps.min():
                exps_scaled = (exps - exps.min()) / (exps.max() - exps.min())
            else:
                exps_scaled = exps
            mae_dosage = float(np.mean(np.abs(exps_scaled - dosages)))
            
            entry = {
                "signals_used": configs[cfg_name],
                "n_signals": len(configs[cfg_name]),
                "spearman_rho_vs_dosage": round(float(rho_dosage), 4),
                "kendall_tau_vs_dosage": round(float(tau_dosage), 4),
                "spearman_rho_vs_full_rrf": round(float(rho_full), 4),
                "mae_vs_dosage_scaled": round(mae_dosage, 4),
            }
            if cfg_name in item_rank_corr:
                entry["item_level_rho_vs_full"] = item_rank_corr[cfg_name]
            config_metrics[cfg_name] = entry
        
        full_mae = config_metrics["full"]["mae_vs_dosage_scaled"]
        full_rho = config_metrics["full"]["spearman_rho_vs_dosage"]
        
        importance = []
        for sig in ACTIVE_SIGNALS:
            dk = f"drop_{sig}"
            if dk in config_metrics:
                d_mae = config_metrics[dk]["mae_vs_dosage_scaled"] - full_mae
                d_rho = config_metrics[dk]["spearman_rho_vs_dosage"] - full_rho
                config_metrics[dk]["delta_mae"] = round(d_mae, 4)
                config_metrics[dk]["delta_rho"] = round(d_rho, 4)
                importance.append({
                    "signal": sig,
                    "delta_mae_when_dropped": round(d_mae, 4),
                    "delta_rho_when_dropped": round(d_rho, 4),
                })
        importance.sort(key=lambda x: -x["delta_mae_when_dropped"])
        
        # Per-model detail
        per_model = []
        for i, mname in enumerate(model_names):
            entry = {
                "model": mname,
                "scale": scales[i],
                "dosage": round(dosages[i], 4),
            }
            for cfg_name in configs:
                entry[f"exposure_{cfg_name}"] = round(model_exposures[cfg_name][i], 6)
            per_model.append(entry)
        
        results[bench] = {
            "n_models": n_models,
            "configs": config_metrics,
            "signal_importance_by_delta_mae": importance,
            "per_model": per_model,
        }
    return results


def main():
    models = list_model_dirs()
    print(f"Found {len(models)} model directories (after filtering)")
    for m in models:
        print(f"  {m['dirname']} ({m['scale']}, d={m['dosage']})")
    
    print("\n=== C1: Signal Rank Correlation ===")
    corr = compute_signal_correlations(models)
    for bench, data in corr.items():
        print(f"\n{bench} (n={data['n_models']}):")
        sigs = data["signals"]
        mx = np.array(data["correlation_matrix"])
        print("    " + "  ".join(f"{s:>16s}" for s in sigs))
        for i, s in enumerate(sigs):
            print(f"{s:>16s}" + "  ".join(f"{mx[i,j]:>16.4f}" for j in range(len(sigs))))
        for k, v in data["pair_summary"].items():
            print(f"  {k}: ρ={v['mean_rho']:.4f}±{v['std_rho']:.4f} [{v['min_rho']:.4f}, {v['max_rho']:.4f}]")
    
    print("\n=== C2: Leave-One-Out Ablation ===")
    ablation = leave_one_out_ablation(models)
    for bench, data in ablation.items():
        print(f"\n{bench} (n={data['n_models']}):")
        print(f"{'Config':<25s} {'#Sig':<5s} {'ρ_dose':<9s} {'τ_dose':<9s} {'MAE':<8s} {'ΔMAE':<8s} {'ρ_full':<8s} {'item_ρ':<8s}")
        for cfg, m in data["configs"].items():
            dm = m.get("delta_mae", "")
            dm_s = f"{dm:+.4f}" if isinstance(dm, float) else ""
            ir = m.get("item_level_rho_vs_full", {}).get("mean_item_rho_vs_full", "")
            ir_s = f"{ir:.4f}" if isinstance(ir, float) else ""
            print(f"{cfg:<25s} {m['n_signals']:<5d} {m['spearman_rho_vs_dosage']:<9.4f} "
                  f"{m['kendall_tau_vs_dosage']:<9.4f} {m['mae_vs_dosage_scaled']:<8.4f} "
                  f"{dm_s:<8s} {m['spearman_rho_vs_full_rrf']:<8.4f} {ir_s:<8s}")
        print("Importance:")
        for r, e in enumerate(data["signal_importance_by_delta_mae"], 1):
            print(f"  #{r} {e['signal']}: ΔMAE={e['delta_mae_when_dropped']:+.4f}")
    
    output = {
        "c1_signal_correlation": corr,
        "c2_leave_one_out_ablation": ablation,
        "metadata": {
            "signals": ACTIVE_SIGNALS,
            "signal_descriptions": {
                "s1_embedding": "Embedding similarity between benchmark item and SFT training data (higher = more similar to training)",
                "s2_minkpp": "Min-K%++ memorization score (negated: lower raw value = more memorized)",
                "s4_selfcritique": "Self-critique consistency (higher = model more confident, suggesting memorization)",
            },
            "rrf_k": RRF_K,
            "negate_rules": NEGATE,
            "benchmarks": BENCHMARKS,
            "excluded_patterns": EXCLUDE_PATTERNS,
        }
    }
    
    outpath = "/root/contamcal-irt-calibration/analysis/rrf_signal_analysis_v2.json"
    with open(outpath, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved to {outpath}")


if __name__ == "__main__":
    main()
