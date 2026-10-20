import json
import math
import os
import numpy as np
from collections import defaultdict

THRESHOLDS = [0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.7, 0.8, 0.9]

DATASETS = {
    "fewnerd_5epoch": "/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_5epoch_lp_seed42/samples.jsonl",
    "fewnerd_3epoch_mf4v2": "/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_mf4v2_seed42/samples.jsonl",
    "fewnerd_3epoch_exp021": "/root/autodl-tmp/struct_self_consist_ie/output/exp_021_inference/samples.jsonl",
}

def load_data(path):
    instances = []
    with open(path) as f:
        for line in f:
            if not line.strip():
                continue
            obj = json.loads(line)
            if not obj["gold"].get("entities", []):
                continue
            instances.append(obj)
    return instances

def entity_set(entities):
    return {(e["start"], e["end"], e["type"]) for e in entities}

def get_lp_weights(inst):
    samples = inst["samples"]
    logprobs = inst.get("logprobs", None)
    lps = []
    for i, s in enumerate(samples):
        lp = s.get("mean_logprob", None)
        if lp is None and logprobs is not None and i < len(logprobs):
            lp = logprobs[i]
        if lp is None or not math.isfinite(lp):
            lp = -100.0
        lps.append(lp)
    max_lp = max(lps)
    ws = [math.exp(lp - max_lp) for lp in lps]
    total = sum(ws)
    return [w / total for w in ws]

def entity_majority_vote(samples, threshold, weights=None):
    entity_counts = defaultdict(float)
    N = len(samples)
    for i, sample in enumerate(samples):
        w = weights[i] if weights is not None else 1.0
        for e in sample.get("entities", []):
            key = (e["start"], e["end"], e["type"])
            entity_counts[key] += w
    total_weight = sum(weights) if weights is not None else N
    constructed = set()
    for key, count in entity_counts.items():
        if count / total_weight >= threshold:
            constructed.add(key)
    return constructed

def compute_prf(pred_set, gold_set):
    if not gold_set and not pred_set:
        return 1.0, 1.0, 1.0
    if not pred_set:
        return 0.0, 0.0, 0.0
    if not gold_set:
        return 0.0, 0.0, 0.0
    tp = len(pred_set & gold_set)
    if tp == 0:
        return 0.0, 0.0, 0.0
    p = tp / len(pred_set)
    r = tp / len(gold_set)
    f = 2 * p * r / (p + r)
    return p, r, f

def compute_micro(pred_sets, gold_sets):
    tp_total, fp_total, fn_total = 0, 0, 0
    for pred, gold in zip(pred_sets, gold_sets):
        tp = len(pred & gold)
        fp = len(pred - gold)
        fn = len(gold - pred)
        tp_total += tp
        fp_total += fp
        fn_total += fn
    if tp_total == 0:
        return 0.0, 0.0, 0.0
    p = tp_total / (tp_total + fp_total)
    r = tp_total / (tp_total + fn_total)
    f = 2 * p * r / (p + r)
    return p, r, f

def evaluate(path, name):
    if not os.path.exists(path):
        print(f"SKIP {name}: {path} not found")
        return None

    data = load_data(path)
    N_inst = len(data)

    gold_sets = []
    greedy_sets = []
    greedy_f1s = []
    degen_count = 0

    # Precompute weights
    all_lp_weights = []
    sample_entity_sets_per_inst = []

    for inst in data:
        gold = entity_set(inst["gold"]["entities"])
        gold_sets.append(gold)

        greedy_ents = inst.get("greedy", inst["samples"][0])
        g_set = entity_set(greedy_ents.get("entities", []))
        greedy_sets.append(g_set)
        _, _, gf = compute_prf(g_set, gold)
        greedy_f1s.append(gf)

        samples = inst["samples"]
        sample_ent_sets = [frozenset(entity_set(s.get("entities", []))) for s in samples]
        sample_entity_sets_per_inst.append(sample_ent_sets)
        if len(set(sample_ent_sets)) == 1:
            degen_count += 1

        all_lp_weights.append(get_lp_weights(inst))

    # Greedy metrics
    greedy_macro_f1 = np.mean(greedy_f1s)
    gp_micro, gr_micro, gf_micro = compute_micro(greedy_sets, gold_sets)

    print(f"\n{'='*70}")
    print(f"{name} (N=8, seed=42, n_instances={N_inst})")
    print(f"{'='*70}")
    print(f"  Greedy:  macro-F1={greedy_macro_f1:.6f}  micro-F1={gf_micro:.6f}")
    print(f"  Degeneracy rate: {degen_count/N_inst*100:.1f}% ({degen_count}/{N_inst})")

    # Threshold sweep
    print(f"\n  {'θ':>5} | {'Uniform macro':>14} {'Uniform micro':>14} | {'LP-w macro':>14} {'LP-w micro':>14} | {'Δ_unif_macro':>13} {'Δ_lp_macro':>13} {'Δ_unif_micro':>13} {'Δ_lp_micro':>13}")
    print(f"  {'-'*5}-+-{'-'*14}-{'-'*14}-+-{'-'*14}-{'-'*14}-+-{'-'*13}-{'-'*13}-{'-'*13}-{'-'*13}")

    best_lp_macro = {"f1": 0, "theta": 0}
    best_lp_micro = {"f1": 0, "theta": 0}
    best_unif_macro = {"f1": 0, "theta": 0}
    best_unif_micro = {"f1": 0, "theta": 0}

    results_by_theta = {}

    for theta in THRESHOLDS:
        uniform_sets = []
        uniform_f1s = []
        lp_sets = []
        lp_f1s = []

        for idx, inst in enumerate(data):
            gold = gold_sets[idx]
            samples = inst["samples"]
            weights = all_lp_weights[idx]

            u_set = entity_majority_vote(samples, theta)
            uniform_sets.append(u_set)
            _, _, uf = compute_prf(u_set, gold)
            uniform_f1s.append(uf)

            lp_set = entity_majority_vote(samples, theta, weights=weights)
            lp_sets.append(lp_set)
            _, _, lpf = compute_prf(lp_set, gold)
            lp_f1s.append(lpf)

        u_macro = np.mean(uniform_f1s)
        lp_macro = np.mean(lp_f1s)
        _, _, u_micro = compute_micro(uniform_sets, gold_sets)
        _, _, lp_micro = compute_micro(lp_sets, gold_sets)

        du_macro = (u_macro - greedy_macro_f1) * 100
        dlp_macro = (lp_macro - greedy_macro_f1) * 100
        du_micro = (u_micro - gf_micro) * 100
        dlp_micro = (lp_micro - gf_micro) * 100

        marker = ""
        if theta == 0.25:
            marker = " <-- θ=2/N"

        print(f"  {theta:5.2f} | {u_macro:14.6f} {u_micro:14.6f} | {lp_macro:14.6f} {lp_micro:14.6f} | {du_macro:+13.2f} {dlp_macro:+13.2f} {du_micro:+13.2f} {dlp_micro:+13.2f}{marker}")

        results_by_theta[theta] = {
            "uniform_macro": u_macro, "uniform_micro": u_micro,
            "lp_macro": lp_macro, "lp_micro": lp_micro,
        }

        if lp_macro > best_lp_macro["f1"]:
            best_lp_macro = {"f1": lp_macro, "theta": theta}
        if lp_micro > best_lp_micro["f1"]:
            best_lp_micro = {"f1": lp_micro, "theta": theta}
        if u_macro > best_unif_macro["f1"]:
            best_unif_macro = {"f1": u_macro, "theta": theta}
        if u_micro > best_unif_micro["f1"]:
            best_unif_micro = {"f1": u_micro, "theta": theta}

    print(f"\n  Best LP-weighted (macro):  θ={best_lp_macro['theta']:.2f}  F1={best_lp_macro['f1']:.6f}  Δ={+(best_lp_macro['f1']-greedy_macro_f1)*100:+.2f}pp")
    print(f"  Best LP-weighted (micro):  θ={best_lp_micro['theta']:.2f}  F1={best_lp_micro['f1']:.6f}  Δ={(best_lp_micro['f1']-gf_micro)*100:+.2f}pp")
    print(f"  Best Uniform (macro):      θ={best_unif_macro['theta']:.2f}  F1={best_unif_macro['f1']:.6f}  Δ={(best_unif_macro['f1']-greedy_macro_f1)*100:+.2f}pp")
    print(f"  Best Uniform (micro):      θ={best_unif_micro['theta']:.2f}  F1={best_unif_micro['f1']:.6f}  Δ={(best_unif_micro['f1']-gf_micro)*100:+.2f}pp")

    # At θ=0.25 specifically
    t025 = results_by_theta[0.25]
    print(f"\n  At θ=0.25 (confirmation threshold):")
    print(f"    LP-weighted:  macro-F1={t025['lp_macro']:.6f} ({(t025['lp_macro']-greedy_macro_f1)*100:+.2f}pp)  micro-F1={t025['lp_micro']:.6f} ({(t025['lp_micro']-gf_micro)*100:+.2f}pp)")
    print(f"    Uniform:      macro-F1={t025['uniform_macro']:.6f} ({(t025['uniform_macro']-greedy_macro_f1)*100:+.2f}pp)  micro-F1={t025['uniform_micro']:.6f} ({(t025['uniform_micro']-gf_micro)*100:+.2f}pp)")

    return {
        "greedy_macro": greedy_macro_f1, "greedy_micro": gf_micro,
        "degen_rate": degen_count / N_inst * 100, "n_instances": N_inst,
        "best_lp_macro": best_lp_macro, "best_lp_micro": best_lp_micro,
        "best_unif_macro": best_unif_macro, "best_unif_micro": best_unif_micro,
        "theta_025": t025,
    }

if __name__ == "__main__":
    for name, path in DATASETS.items():
        evaluate(path, name)
