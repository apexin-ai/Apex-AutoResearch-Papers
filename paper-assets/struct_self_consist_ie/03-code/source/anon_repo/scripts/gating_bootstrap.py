import json
import numpy as np
from scipy.stats import spearmanr
from pathlib import Path
import warnings
warnings.filterwarnings("ignore")

DATA_DIR = Path("/root/autodl-tmp/struct_self_consist_ie/output/dev_set_lp_probe")
OUT_DIR = Path("/root/autodl-tmp/struct_self_consist_ie/output/gating_bootstrap")
OUT_DIR.mkdir(parents=True, exist_ok=True)

DATASETS = ["scierc", "conll2003", "fewnerd"]
B = 1000
THRESHOLDS = [0.2, 0.25, 0.3, 0.35, 0.4]
np.random.seed(42)

def compute_entity_f1(pred_entities, gold_entities):
    """Compute entity-level F1 (strict match: text + type + span)."""
    def to_set(ents):
        return set((e["text"], e["type"], e["start"], e["end"]) for e in ents)
    pred_set = to_set(pred_entities)
    gold_set = to_set(gold_entities)
    if len(pred_set) == 0 and len(gold_set) == 0:
        return 1.0
    if len(pred_set) == 0 or len(gold_set) == 0:
        return 0.0
    tp = len(pred_set & gold_set)
    prec = tp / len(pred_set) if pred_set else 0.0
    rec = tp / len(gold_set) if gold_set else 0.0
    if prec + rec == 0:
        return 0.0
    return 2 * prec * rec / (prec + rec)

def load_dataset(name):
    """Load dataset and compute per-instance (logprobs, f1s, spearman_rho)."""
    fpath = DATA_DIR / f"{name}_dev_samples.jsonl"
    instances = []
    with open(fpath) as f:
        for line in f:
            rec = json.loads(line)
            gold_ents = rec["gold"]["entities"]
            samples = rec["samples"]
            lps = [s["mean_logprob"] for s in samples]
            f1s = [compute_entity_f1(s["entities"], gold_ents) for s in samples]
            
            # Check degeneracy: all samples identical output
            unique_f1s = set(f1s)
            unique_lps = set(lps)
            is_degenerate = len(unique_f1s) <= 1 or len(unique_lps) <= 1
            
            rho = np.nan
            if not is_degenerate and len(lps) >= 3:
                rho_val, _ = spearmanr(lps, f1s)
                if not np.isnan(rho_val):
                    rho = rho_val
            
            instances.append({
                "id": rec["id"],
                "rho": rho,
                "is_valid": not np.isnan(rho),
                "is_degenerate": is_degenerate,
                "n_unique_f1": len(unique_f1s),
                "n_unique_lp": len(unique_lps),
                "mean_f1": np.mean(f1s),
                "greedy_f1": compute_entity_f1(rec["greedy"]["entities"], gold_ents),
                "f1s": f1s,
                "lps": lps,
            })
    return instances

def bootstrap_spearman(instances, B=1000):
    """Bootstrap resample instances, compute mean rho per resample."""
    valid_rhos = np.array([inst["rho"] for inst in instances if inst["is_valid"]])
    n_valid = len(valid_rhos)
    n_total = len(instances)
    
    if n_valid < 3:
        return {
            "mean_rho": float(np.mean(valid_rhos)) if n_valid > 0 else None,
            "ci_lower": None, "ci_upper": None,
            "n_valid": n_valid, "n_total": n_total,
            "bootstrap_means": []
        }
    
    # Bootstrap on ALL instances (including invalid -> contribute 0 to adjusted score)
    all_rhos = np.array([inst["rho"] if inst["is_valid"] else 0.0 for inst in instances])
    bootstrap_means = []
    for _ in range(B):
        idx = np.random.randint(0, n_total, size=n_total)
        resampled = all_rhos[idx]
        # Adjusted score = mean of resampled (invalid instances contribute 0)
        bootstrap_means.append(float(np.mean(resampled)))
    
    bootstrap_means = np.array(bootstrap_means)
    ci_lower = float(np.percentile(bootstrap_means, 2.5))
    ci_upper = float(np.percentile(bootstrap_means, 97.5))
    
    # Also bootstrap just valid rhos for mean_rho CI
    valid_bootstrap = []
    for _ in range(B):
        idx = np.random.randint(0, n_valid, size=n_valid)
        valid_bootstrap.append(float(np.mean(valid_rhos[idx])))
    valid_bootstrap = np.array(valid_bootstrap)
    
    return {
        "mean_rho": float(np.mean(valid_rhos)),
        "adjusted_score": float(np.mean(all_rhos)),
        "ci_lower_adjusted": ci_lower,
        "ci_upper_adjusted": ci_upper,
        "ci_lower_rho": float(np.percentile(valid_bootstrap, 2.5)),
        "ci_upper_rho": float(np.percentile(valid_bootstrap, 97.5)),
        "n_valid": n_valid,
        "n_total": n_total,
        "valid_ratio": n_valid / n_total,
        "degeneracy_rate": sum(1 for i in instances if i["is_degenerate"]) / n_total,
    }

def threshold_sensitivity(instances, thresholds):
    """For each threshold, determine routing decision using bootstrap."""
    valid_rhos = np.array([inst["rho"] for inst in instances if inst["is_valid"]])
    n_total = len(instances)
    all_rhos = np.array([inst["rho"] if inst["is_valid"] else 0.0 for inst in instances])
    
    results = {}
    for th in thresholds:
        # Point estimate
        adjusted = float(np.mean(all_rhos))
        point_decision = "LP" if adjusted > th else "greedy"
        
        # Bootstrap stability: how often does the decision flip?
        lp_count = 0
        for _ in range(B):
            idx = np.random.randint(0, n_total, size=n_total)
            boot_adj = float(np.mean(all_rhos[idx]))
            if boot_adj > th:
                lp_count += 1
        
        stability = max(lp_count, B - lp_count) / B
        
        results[str(th)] = {
            "adjusted_score": adjusted,
            "point_decision": point_decision,
            "lp_fraction": lp_count / B,
            "greedy_fraction": (B - lp_count) / B,
            "routing_stability": stability,
        }
    return results

def analyze_greedy_fallback(instances):
    """Analyze when construction fails and greedy is the fallback."""
    degenerate_instances = [i for i in instances if i["is_degenerate"]]
    valid_instances = [i for i in instances if i["is_valid"]]
    
    # For degenerate instances: check if all samples produce same output
    all_zero_f1 = [i for i in degenerate_instances if i["mean_f1"] == 0.0]
    all_perfect_f1 = [i for i in degenerate_instances if i["mean_f1"] == 1.0]
    
    # Greedy vs sample mean F1 comparison
    greedy_wins = sum(1 for i in instances if i["greedy_f1"] > i["mean_f1"])
    sample_wins = sum(1 for i in instances if i["mean_f1"] > i["greedy_f1"])
    ties = sum(1 for i in instances if i["greedy_f1"] == i["mean_f1"])
    
    # For valid instances: negative rho means LP would pick wrong answer
    if valid_instances:
        negative_rho = [i for i in valid_instances if i["rho"] < 0]
        negative_frac = len(negative_rho) / len(valid_instances)
    else:
        negative_frac = 0.0
    
    return {
        "n_degenerate": len(degenerate_instances),
        "n_total": len(instances),
        "degeneracy_rate": len(degenerate_instances) / len(instances),
        "degenerate_all_zero_f1": len(all_zero_f1),
        "degenerate_all_perfect_f1": len(all_perfect_f1),
        "greedy_vs_sample_mean": {
            "greedy_wins": greedy_wins,
            "sample_wins": sample_wins,
            "ties": ties,
        },
        "negative_rho_fraction": negative_frac,
        "mean_greedy_f1": float(np.mean([i["greedy_f1"] for i in instances])),
        "mean_sample_f1": float(np.mean([i["mean_f1"] for i in instances])),
    }

# Main analysis
results = {}
for ds in DATASETS:
    print(f"\n{'='*60}")
    print(f"Dataset: {ds}")
    print(f"{'='*60}")
    
    instances = load_dataset(ds)
    
    # Bootstrap CI
    boot = bootstrap_spearman(instances, B=B)
    print(f"  mean_rho = {boot['mean_rho']:.4f}, "
          f"CI(rho) = [{boot['ci_lower_rho']:.4f}, {boot['ci_upper_rho']:.4f}]")
    print(f"  adjusted_score = {boot['adjusted_score']:.4f}, "
          f"CI(adj) = [{boot['ci_lower_adjusted']:.4f}, {boot['ci_upper_adjusted']:.4f}]")
    print(f"  valid_ratio = {boot['valid_ratio']:.4f}, degeneracy = {boot['degeneracy_rate']:.4f}")
    
    # Threshold sensitivity
    thresh = threshold_sensitivity(instances, THRESHOLDS)
    print(f"\n  Threshold sensitivity:")
    for th, v in thresh.items():
        print(f"    τ={th}: decision={v['point_decision']}, "
              f"LP%={v['lp_fraction']:.3f}, stability={v['routing_stability']:.3f}")
    
    # Greedy fallback
    fallback = analyze_greedy_fallback(instances)
    print(f"\n  Greedy fallback:")
    print(f"    degeneracy_rate = {fallback['degeneracy_rate']:.4f}")
    print(f"    greedy_f1 = {fallback['mean_greedy_f1']:.4f}, sample_f1 = {fallback['mean_sample_f1']:.4f}")
    print(f"    greedy_wins={fallback['greedy_vs_sample_mean']['greedy_wins']}, "
          f"sample_wins={fallback['greedy_vs_sample_mean']['sample_wins']}, "
          f"ties={fallback['greedy_vs_sample_mean']['ties']}")
    print(f"    negative_rho_fraction = {fallback['negative_rho_fraction']:.4f}")
    
    results[ds] = {
        "bootstrap": boot,
        "threshold_sensitivity": thresh,
        "greedy_fallback": fallback,
    }

# Routing stability summary across thresholds
print(f"\n{'='*60}")
print("ROUTING STABILITY SUMMARY")
print(f"{'='*60}")
for th in THRESHOLDS:
    decisions = {ds: results[ds]["threshold_sensitivity"][str(th)]["point_decision"] for ds in DATASETS}
    stabilities = {ds: results[ds]["threshold_sensitivity"][str(th)]["routing_stability"] for ds in DATASETS}
    print(f"τ={th}: {decisions}  stability={stabilities}")

# Find robust threshold range
print(f"\nRobust range analysis:")
for th in THRESHOLDS:
    all_stable = all(
        results[ds]["threshold_sensitivity"][str(th)]["routing_stability"] >= 0.95 
        for ds in DATASETS
    )
    print(f"  τ={th}: all_stable_95%={all_stable}")

# Save
with open(OUT_DIR / "gating_analysis.json", "w") as f:
    json.dump(results, f, indent=2)
print(f"\nSaved to {OUT_DIR / 'gating_analysis.json'}")
