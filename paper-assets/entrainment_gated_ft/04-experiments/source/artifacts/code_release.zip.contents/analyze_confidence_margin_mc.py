import json, os, sys
import numpy as np
from scipy.stats import mannwhitneyu

ARCHS = ["GatedDeltaNet", "RetNet", "HGRN2"]
ARCH_SHORT = {"GatedDeltaNet": "GDN", "RetNet": "RetNet", "HGRN2": "HGRN2"}
HYBRID_CONFIG = {"GatedDeltaNet": "hybrid-12-1", "RetNet": "hybrid-3-1", "HGRN2": "hybrid-3-1"}
BENCHMARKS = ["arc_easy", "hellaswag"]
BASE = "/root/entrainment_gated_ft/lm_eval_clean"

def load_samples(benchmark, arch, config_type):
    dir_name = f"1.3B-100B-{arch}-{config_type}"
    path = f"{BASE}/{benchmark}/{dir_name}/samples/{benchmark}.jsonl"
    if not os.path.exists(path):
        raise FileNotFoundError(f"Not found: {path}")
    samples = {}
    with open(path) as f:
        for line in f:
            s = json.loads(line)
            samples[s["doc_id"]] = s
    return samples

def extract_confidence(sample):
    resps = sample.get("filtered_resps", sample.get("resps", []))
    target = sample.get("target")
    if target is None:
        target = sample.get("doc", {}).get("gold")
    if isinstance(target, str):
        target = int(target)
    logliks = []
    for r in resps:
        if isinstance(r, (list, tuple)):
            logliks.append(float(r[0]))
        else:
            logliks.append(float(r))
    return abs(logliks[target])

def cohens_d(g1, g2):
    n1, n2 = len(g1), len(g2)
    m1, m2 = np.mean(g1), np.mean(g2)
    s1, s2 = np.std(g1, ddof=1), np.std(g2, ddof=1)
    pooled = np.sqrt(((n1-1)*s1**2 + (n2-1)*s2**2) / (n1+n2-2))
    return (m1 - m2) / pooled if pooled > 0 else 0.0

def compute_stats(group_a, group_b, name_a, name_b, hypothesis_desc):
    if len(group_a) < 5 or len(group_b) < 5:
        return {"skip": True, "reason": f"{name_a}_n={len(group_a)}, {name_b}_n={len(group_b)}"}
    a, b = np.array(group_a), np.array(group_b)
    U, p = mannwhitneyu(a, b, alternative='two-sided')
    d = cohens_d(a, b)
    n1, n2 = len(a), len(b)
    r_rb = 1 - 2*U/(n1*n2)
    
    a_lower = np.mean(a) < np.mean(b)
    return {
        f"{name_a}_n": n1,
        f"{name_b}_n": n2,
        f"{name_a}_margin": {
            "mean": round(float(np.mean(a)), 4),
            "median": round(float(np.median(a)), 4),
            "std": round(float(np.std(a, ddof=1)), 4),
            "q25": round(float(np.percentile(a, 25)), 4),
            "q75": round(float(np.percentile(a, 75)), 4),
        },
        f"{name_b}_margin": {
            "mean": round(float(np.mean(b)), 4),
            "median": round(float(np.median(b)), 4),
            "std": round(float(np.std(b, ddof=1)), 4),
            "q25": round(float(np.percentile(b, 25)), 4),
            "q75": round(float(np.percentile(b, 75)), 4),
        },
        "U": float(U),
        "p": float(p),
        "cohens_d": round(d, 4),
        "r_rb": round(r_rb, 4),
        "direction": f"{name_a}_lower" if a_lower else f"{name_b}_lower",
    }

results = {}

for benchmark in BENCHMARKS:
    results[benchmark] = {}
    for arch in ARCHS:
        short = ARCH_SHORT[arch]
        hybrid_type = HYBRID_CONFIG[arch]
        
        print(f"\n=== {benchmark} / {short} (hybrid={hybrid_type}) ===")
        
        pure_samples = load_samples(benchmark, arch, "pure")
        hybrid_samples = load_samples(benchmark, arch, hybrid_type)
        
        doc_ids = sorted(set(pure_samples.keys()) & set(hybrid_samples.keys()))
        print(f"  Matched samples: {len(doc_ids)}")
        
        hurt_conf, stayed_right_conf = [], []
        helped_conf, stayed_wrong_conf = [], []
        
        for did in doc_ids:
            ps = pure_samples[did]
            hs = hybrid_samples[did]
            acc_field = "acc_norm" if benchmark == "hellaswag" else "acc"
            pure_acc = int(ps[acc_field])
            hybrid_acc = int(hs[acc_field])
            conf = extract_confidence(ps)
            
            if pure_acc == 1 and hybrid_acc == 0:
                hurt_conf.append(conf)
            elif pure_acc == 1 and hybrid_acc == 1:
                stayed_right_conf.append(conf)
            elif pure_acc == 0 and hybrid_acc == 1:
                helped_conf.append(conf)
            else:
                stayed_wrong_conf.append(conf)
        
        print(f"  hurt={len(hurt_conf)}, stayed_right={len(stayed_right_conf)}, helped={len(helped_conf)}, stayed_wrong={len(stayed_wrong_conf)}")
        
        c1 = compute_stats(hurt_conf, stayed_right_conf, "hurt", "stayed_right",
                          "hurt has higher |loglik| (less confident correct)")
        c2 = compute_stats(helped_conf, stayed_wrong_conf, "helped", "stayed_wrong",
                          "helped has lower |loglik| (near-miss wrong)")
        
        if "skip" not in c1:
            c1["hypothesis_supported"] = c1["direction"] == "stayed_right_lower"
            c1["interpretation"] = ("Hurt samples had higher abs(loglik) = lower target probability = less confident correct. "
                                   "Supports hypothesis: weakly-correct answers are vulnerable to attention flipping."
                                   if c1["hypothesis_supported"] else
                                   "Direction opposite to hypothesis.")
            print(f"  C1: d={c1['cohens_d']}, p={c1['p']:.2e}, dir={c1['direction']}, supported={c1['hypothesis_supported']}")
        else:
            print(f"  C1: SKIPPED - {c1['reason']}")
            
        if "skip" not in c2:
            c2["hypothesis_supported"] = c2["direction"] == "helped_lower"
            c2["interpretation"] = ("Helped samples had lower abs(loglik) = higher target probability = near-miss wrong. "
                                   "Supports hypothesis: near-miss wrong answers are rescuable by attention."
                                   if c2["hypothesis_supported"] else
                                   "Direction opposite to hypothesis.")
            print(f"  C2: d={c2['cohens_d']}, p={c2['p']:.2e}, dir={c2['direction']}, supported={c2['hypothesis_supported']}")
        else:
            print(f"  C2: SKIPPED - {c2['reason']}")
        
        results[benchmark][short] = {
            "hybrid_config": f"{short}-{hybrid_type.replace('hybrid-','')}",
            "control_1_pure_correct": c1,
            "control_2_pure_wrong": c2,
        }

output = {
    "analysis": "cross_benchmark_confidence_margin",
    "date": "2026-05-20",
    "method": {
        "confidence_proxy": "abs(correct_option_loglikelihood) from pure model",
        "margin_semantics": {
            "pure_correct": "higher |loglik| = lower probability = less confident correct = closer to boundary",
            "pure_wrong": "lower |loglik| = higher probability for target = near-miss = closer to boundary"
        },
        "control_1": "Within pure-correct: hurt (pure-right, hybrid-wrong) vs stayed-right (pure-right, hybrid-right)",
        "control_2": "Within pure-wrong: helped (pure-wrong, hybrid-right) vs stayed-wrong (pure-wrong, hybrid-wrong)",
        "hypotheses": {
            "C1": "hurt has higher |loglik| than stayed-right (less confident correct -> vulnerable)",
            "C2": "helped has lower |loglik| than stayed-wrong (near-miss wrong -> rescuable)"
        },
        "tests": ["Mann-Whitney U (two-sided)", "Cohen's d (pooled std)", "rank-biserial r_rb"],
        "note": "GDN uses h12-1 (consistent with LAMBADA analysis); RetNet/HGRN2 use h3-1",
        "acc_field": "hellaswag: acc_norm (length-normalized); others: acc (raw loglik)"
    },
    "results": results,
}

os.makedirs("/root/entrainment_gated_ft/analysis_output", exist_ok=True)
out_path = "/root/entrainment_gated_ft/analysis_output/cross_benchmark_confidence_margin.json"
with open(out_path, "w") as f:
    json.dump(output, f, indent=2)
print(f"\nSaved to {out_path}")
