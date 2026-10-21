"""B7 Adaptive Sampling Budget Analysis — memory-efficient version."""
import json, os, sys
import numpy as np
from collections import defaultdict

BASE = "/root/autodl-tmp/struct_self_consist_ie/output"
OUTPUT_DIR = f"{BASE}/b7_adaptive_budget"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def entity_set(entities):
    return {(e["start"], e["end"], e["type"]) for e in entities}

def entity_mv(samples, threshold=0.5):
    counts = defaultdict(int)
    N = len(samples)
    if N == 0:
        return set()
    for s in samples:
        for e in s.get("entities", []):
            counts[(e["start"], e["end"], e["type"])] += 1
    return {k for k, c in counts.items() if c / N >= threshold}

def micro_prf(tp, fp, fn):
    if tp == 0:
        return 0.0, 0.0, 0.0
    p = tp / (tp + fp)
    r = tp / (tp + fn)
    f = 2 * p * r / (p + r)
    return p, r, f

def inst_f1(pred, gold):
    if not gold and not pred:
        return 1.0
    tp = len(pred & gold)
    if tp == 0:
        return 0.0
    p = tp / len(pred)
    r = tp / len(gold)
    return 2 * p * r / (p + r)

def load_slim(path):
    """Load only needed fields to save memory."""
    data = []
    with open(path) as f:
        for line in f:
            raw = json.loads(line)
            slim = {
                "id": raw["id"],
                "gold_ents": raw["gold"]["entities"],
                "greedy_ents": raw["greedy"]["entities"],
                "greedy_mlp": raw["greedy"]["mean_logprob"],
                "sample_ents": [
                    s.get("entities", []) for s in raw["samples"][:8]
                ],
            }
            data.append(slim)
    return data

def analyze(name, data):
    M = len(data)
    print(f"\n{'='*60}")
    print(f"{name}: {M} instances")
    
    glps = np.array([d["greedy_mlp"] for d in data])
    median_lp = float(np.median(glps))
    print(f"Greedy LP: mean={glps.mean():.4f}, median={median_lp:.4f}, "
          f"std={glps.std():.4f}")
    
    hi = set(i for i in range(M) if glps[i] >= median_lp)
    lo = set(range(M)) - hi
    print(f"High-conf: {len(hi)}, Low-conf: {len(lo)}")

    strategies = {}
    
    # Define strategies: name -> (n_samples_high, n_samples_low)
    # n=0 means use greedy
    strat_defs = {
        "greedy": (0, 0),
        "uniform_n2": (2, 2),
        "uniform_n4": (4, 4),
        "uniform_n8": (8, 8),
        "adaptive_h1_l8": (0, 8),
        "adaptive_h2_l8": (2, 8),
        "adaptive_h3_l8": (3, 8),
        "adaptive_h4_l8": (4, 8),
    }
    
    for sname, (nh, nl) in strat_defs.items():
        tp_t, fp_t, fn_t = 0, 0, 0
        f1s, f1h, f1l = [], [], []
        
        for i, d in enumerate(data):
            gold = entity_set(d["gold_ents"])
            is_hi = i in hi
            n = nh if is_hi else nl
            
            if n == 0:
                pred = entity_set(d["greedy_ents"])
            else:
                samples_e = [{"entities": e} for e in d["sample_ents"][:n]]
                pred = entity_mv(samples_e)
            
            tp = len(pred & gold)
            fp_t += len(pred - gold)
            fn_t += len(gold - pred)
            tp_t += tp
            
            f = inst_f1(pred, gold)
            f1s.append(f)
            (f1h if is_hi else f1l).append(f)
        
        p, r, f = micro_prf(tp_t, fp_t, fn_t)
        total_s = len(hi) * max(nh, 1) + len(lo) * max(nl, 1)
        if sname.startswith("uniform"):
            ns = nh if nh > 0 else 1
            total_s = M * ns
        elif sname == "greedy":
            total_s = M
        
        strategies[sname] = {
            "micro_p": round(p*100, 2),
            "micro_r": round(r*100, 2),
            "micro_f1": round(f*100, 2),
            "macro_f1": round(np.mean(f1s)*100, 2),
            "macro_f1_high": round(np.mean(f1h)*100, 2) if f1h else 0,
            "macro_f1_low": round(np.mean(f1l)*100, 2) if f1l else 0,
            "total_samples": total_s,
            "pct_of_uniform8": round(total_s/(M*8)*100, 1),
        }
    
    u8f1 = strategies["uniform_n8"]["micro_f1"]
    for sn, sv in strategies.items():
        sv["f1_delta_vs_u8"] = round(sv["micro_f1"] - u8f1, 2)
        print(f"  {sn:20s}: F1={sv['micro_f1']:.2f} (Δ={sv['f1_delta_vs_u8']:+.2f}), "
              f"samples={sv['total_samples']} ({sv['pct_of_uniform8']:.1f}%)")

    # Percentile sweep
    pct_sweep = {}
    for pct in [25, 33, 50, 67, 75]:
        thr = np.percentile(glps, 100 - pct)
        hi_p = set(i for i in range(M) if glps[i] >= thr)
        lo_p = set(range(M)) - hi_p
        tp_t, fp_t, fn_t = 0, 0, 0
        for i, d in enumerate(data):
            gold = entity_set(d["gold_ents"])
            if i in hi_p:
                samples_e = [{"entities": e} for e in d["sample_ents"][:2]]
                pred = entity_mv(samples_e)
            else:
                samples_e = [{"entities": e} for e in d["sample_ents"][:8]]
                pred = entity_mv(samples_e)
            tp = len(pred & gold)
            fp_t += len(pred - gold)
            fn_t += len(gold - pred)
            tp_t += tp
        _, _, f = micro_prf(tp_t, fp_t, fn_t)
        total_s = len(hi_p) * 2 + len(lo_p) * 8
        pct_sweep[f"top{pct}pct_h2l8"] = {
            "high_pct": pct,
            "n_high": len(hi_p), "n_low": len(lo_p),
            "micro_f1": round(f*100, 2),
            "f1_delta": round(f*100 - u8f1, 2),
            "total_samples": total_s,
            "savings_pct": round((1 - total_s/(M*8))*100, 1),
        }

    print(f"\n  Percentile sweep (h=2, l=8):")
    for k, v in pct_sweep.items():
        print(f"    {k}: F1={v['micro_f1']:.2f} (Δ={v['f1_delta']:+.2f}), "
              f"save={v['savings_pct']:.1f}%")

    return {
        "n_instances": M,
        "greedy_lp_stats": {
            "mean": round(float(glps.mean()), 6),
            "median": round(float(median_lp), 6),
            "std": round(float(glps.std()), 6),
            "min": round(float(glps.min()), 6),
            "max": round(float(glps.max()), 6),
        },
        "n_high_conf": len(hi),
        "n_low_conf": len(lo),
        "strategies": strategies,
        "percentile_sweep": pct_sweep,
    }

# Main
results = {}
datasets = {
    "fewnerd_qwen3_8b": f"{BASE}/exp_021_inference/samples.jsonl",
    "scierc_qwen3_8b": f"{BASE}/exp_029b_scierc_10epoch/samples.jsonl",
}

for name, path in datasets.items():
    print(f"\nLoading {name}...", flush=True)
    data = load_slim(path)
    print(f"Loaded {len(data)} instances", flush=True)
    results[name] = analyze(name, data)
    del data

# Summary
print("\n" + "="*60)
print("RECOMMENDATION")
print("="*60)
for name, res in results.items():
    u8 = res["strategies"]["uniform_n8"]
    a28 = res["strategies"]["adaptive_h2_l8"]
    savings = 100 - a28["pct_of_uniform8"]
    loss = u8["micro_f1"] - a28["micro_f1"]
    print(f"{name}:")
    print(f"  Uniform N=8: F1={u8['micro_f1']:.2f}")
    print(f"  Adaptive h2/l8: F1={a28['micro_f1']:.2f} (saves {savings:.1f}%, loss={loss:.2f})")
    
    # Best strategy: max savings with <=0.5 F1 loss
    candidates = [(k, v) for k, v in res["strategies"].items() 
                  if abs(v["f1_delta_vs_u8"]) <= 0.5 and v["pct_of_uniform8"] < 100]
    if candidates:
        best = min(candidates, key=lambda x: x[1]["pct_of_uniform8"])
        print(f"  Best (<=0.5 loss): {best[0]} → saves {100-best[1]['pct_of_uniform8']:.1f}%, "
              f"F1={best[1]['micro_f1']:.2f}")

output = {
    "experiment": "B7_adaptive_sampling_budget",
    "description": "Compare uniform N=8 vs adaptive allocation based on greedy LP confidence",
    "method": "Split instances by median greedy mean_logprob; high-conf uses fewer samples, low-conf uses N=8. Entity construction via majority vote (threshold=0.5).",
    "datasets": results,
}
out_path = os.path.join(OUTPUT_DIR, "adaptive_analysis.json")
with open(out_path, "w") as f:
    json.dump(output, f, indent=2, ensure_ascii=False)
print(f"\nSaved to {out_path}")
