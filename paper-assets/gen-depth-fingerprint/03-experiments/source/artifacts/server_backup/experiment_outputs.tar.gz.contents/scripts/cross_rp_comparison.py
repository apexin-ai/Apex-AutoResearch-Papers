import json
import numpy as np
from scipy import stats
from pathlib import Path

FEATURES = ["entropy_mean", "entropy_std", "entropy_max", "entropy_min", "ttr", "hapax_ratio", "tail_decay"]

def load_jsonl(path):
    records = []
    with open(path) as f:
        for line in f:
            records.append(json.loads(line))
    return records

def analyze(records):
    n = len(records)
    depths = [r["depth"] for r in records]
    depth_counts = {}
    for d in depths:
        depth_counts[d] = depth_counts.get(d, 0) + 1
    
    d0 = depth_counts.get(0, 0)
    d4 = depth_counts.get(4, 0)
    retention = d4 / d0 if d0 > 0 else 0.0
    
    feature_stats = {}
    for feat in FEATURES:
        vals = [r[feat] for r in records]
        arr = np.array(vals)
        
        # per-depth means
        per_depth_mean = []
        for d in range(5):
            d_vals = [r[feat] for r in records if r["depth"] == d]
            per_depth_mean.append(float(np.mean(d_vals)) if d_vals else None)
        
        # spearman with depth
        depth_arr = np.array(depths)
        if len(set(depths)) > 1:
            rho, p = stats.spearmanr(depth_arr, arr)
        else:
            rho, p = 0.0, 1.0
        
        feature_stats[feat] = {
            "mean": float(np.mean(arr)),
            "std": float(np.std(arr)),
            "median": float(np.median(arr)),
            "min": float(np.min(arr)),
            "max": float(np.max(arr)),
            "spearman_rho": float(rho),
            "spearman_p": float(p),
            "per_depth_mean": per_depth_mean
        }
    
    return {
        "n_records": n,
        "depth_retention": round(retention, 4),
        "depth_dist": {str(k): v for k, v in sorted(depth_counts.items())},
        "features": feature_stats
    }

def cohens_d(a, b):
    na, nb = len(a), len(b)
    pooled_std = np.sqrt(((na-1)*np.std(a,ddof=1)**2 + (nb-1)*np.std(b,ddof=1)**2) / (na+nb-2))
    if pooled_std == 0:
        return 0.0
    return float((np.mean(a) - np.mean(b)) / pooled_std)

def main():
    rp10_path = Path("/root/gen-depth-fingerprint/data/gemma-2-2b/features_pythia410m.jsonl")
    rp11_path = Path("/root/gen-depth-fingerprint/data/gemma-2-2b-rp11/features_pythia410m.jsonl")
    
    rp10_records = load_jsonl(rp10_path)
    rp11_records = load_jsonl(rp11_path)
    
    rp10_stats = analyze(rp10_records)
    rp11_stats = analyze(rp11_records)
    
    # Comparison
    comparison = {
        "retention_delta": round(rp11_stats["depth_retention"] - rp10_stats["depth_retention"], 4),
        "cohens_d": {},
        "ks_test_p": {},
        "ks_test_stat": {},
        "spearman_delta": {}
    }
    
    for feat in FEATURES:
        a = np.array([r[feat] for r in rp10_records])
        b = np.array([r[feat] for r in rp11_records])
        
        comparison["cohens_d"][feat] = round(cohens_d(a, b), 4)
        ks_stat, ks_p = stats.ks_2samp(a, b)
        comparison["ks_test_stat"][feat] = round(float(ks_stat), 4)
        comparison["ks_test_p"][feat] = float(ks_p)
        comparison["spearman_delta"][feat] = round(
            rp11_stats["features"][feat]["spearman_rho"] - rp10_stats["features"][feat]["spearman_rho"], 4
        )
    
    result = {
        "rp10": rp10_stats,
        "rp11": rp11_stats,
        "comparison": comparison
    }
    
    out_path = Path("/root/gen-depth-fingerprint/results/gemma_cross_rp_comparison.json")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)
    
    print(f"Done. Output: {out_path}")
    print(f"rp10: {rp10_stats['n_records']} records, retention={rp10_stats['depth_retention']}")
    print(f"rp11: {rp11_stats['n_records']} records, retention={rp11_stats['depth_retention']}")
    print(f"Retention delta: {comparison['retention_delta']}")
    print("\nCohen's d (rp10 - rp11):")
    for feat in FEATURES:
        print(f"  {feat}: d={comparison['cohens_d'][feat]}, KS_p={comparison['ks_test_p'][feat]:.2e}")

if __name__ == "__main__":
    main()
