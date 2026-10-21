#!/usr/bin/env python3
"""5-signal + DGS analysis for LLaMA SciERC seed=456."""
import json, sys, os
import numpy as np
from scipy.stats import spearmanr, rankdata
from collections import Counter

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from unified_metrics import compute_entity_f1, compute_degeneracy, bootstrap_ci, bootstrap_delta_ci
from consistency import compute_all_consistency_scores
from evaluation import per_instance_f1

DATA_PATH = "/root/autodl-tmp/struct_self_consist_ie/output/exp_018_llama_scierc_seed456/samples.jsonl"
OUTPUT_DIR = "/root/autodl-tmp/struct_self_consist_ie/output/exp_018_llama_scierc_seed456"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def load_data(path):
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]

def safe_spearman(x, y):
    x, y = np.asarray(x, float), np.asarray(y, float)
    m = np.isfinite(x) & np.isfinite(y)
    x, y = x[m], y[m]
    if len(x) < 3: return float("nan"), float("nan")
    r = spearmanr(x, y)
    return float(r.statistic), float(r.pvalue)

def safe_auroc(scores, labels):
    scores, labels = np.asarray(scores, float), np.asarray(labels, int)
    if len(np.unique(labels)) < 2: return float("nan")
    n_pos, n_neg = (labels==1).sum(), (labels==0).sum()
    if n_pos == 0 or n_neg == 0: return float("nan")
    ranks = rankdata(scores)
    u = ranks[labels==1].sum() - n_pos*(n_pos+1)/2
    return float(u / (n_pos * n_neg))

def compute_exact_match_rate(samples, subtask):
    if subtask == "ner":
        keys = [frozenset((e["text"], e["type"]) for e in s.get("entities", [])) for s in samples]
    else:
        keys = [frozenset((r["head"], r["tail"], r["type"]) for r in s.get("relations", [])) for s in samples]
    if not keys: return 0.0
    c = Counter(keys)
    return c.most_common(1)[0][1] / len(samples)

def compute_voting_confidence(samples, subtask):
    N = len(samples)
    if N == 0: return 0.0
    counter = Counter()
    if subtask == "ner":
        for s in samples:
            for e in s.get("entities", []):
                counter[(e["text"], e["type"])] += 1
    else:
        for s in samples:
            for r in s.get("relations", []):
                counter[(r["head"], r["tail"], r["type"])] += 1
    if not counter: return 0.0
    return float(np.mean([v / N for v in counter.values()]))

def compute_mean_logprob(samples):
    lps = [s.get("mean_logprob") for s in samples if s.get("mean_logprob") is not None]
    lps = [lp for lp in lps if np.isfinite(lp)]
    return float(np.mean(lps)) if lps else float("nan")

print("Loading data...")
instances = load_data(DATA_PATH)
print(f"Total instances: {len(instances)}")

subtask = "ner"
entity_key = "entities"
valid = [inst for inst in instances if len(inst["gold"].get(entity_key, [])) > 0]
print(f"Valid (gold non-empty): {len(valid)}")

greedy_f1s_all = []
for inst in valid:
    greedy = inst.get("greedy", inst["samples"][0])
    greedy_f1s_all.append(per_instance_f1(greedy, inst["gold"], subtask=subtask))
conditional = [inst for inst, f1 in zip(valid, greedy_f1s_all) if f1 > 0]
print(f"Conditional (greedy F1 > 0): {len(conditional)}")

# === 5-Signal Analysis ===
print("\n=== 5-Signal Analysis ===")
report = {"model": "LLaMA-3.1-8B-Instruct", "dataset": "SciERC", "seed": 456,
           "n_samples": 8, "temperature": 1.0, "subtask": "ner",
           "n_total": len(instances), "n_valid": len(valid), "n_conditional": len(conditional)}

for split_name, split_insts in [("full", valid), ("conditional", conditional)]:
    cons = compute_all_consistency_scores(split_insts, subtask=subtask)
    sj = cons["soft_jaccard"]
    fk = cons["fleiss_kappa"]

    lp, em, vc, f1s = [], [], [], []
    sample_f1_lists = []
    for inst in split_insts:
        samples = inst["samples"]
        greedy = inst.get("greedy", samples[0])
        lp.append(compute_mean_logprob(samples))
        em.append(compute_exact_match_rate(samples, subtask))
        vc.append(compute_voting_confidence(samples, subtask))
        gold_ents = inst["gold"]["entities"]
        sample_f1_list = [compute_entity_f1(s.get("entities", []), gold_ents) for s in samples]
        sample_f1_lists.append(sample_f1_list)
        greedy_f1 = compute_entity_f1(greedy.get("entities", []), gold_ents)
        f1s.append(greedy_f1)

    oracle_f1s = [max(sf) for sf in sample_f1_lists]
    headroom = float(np.mean(oracle_f1s) - np.mean(f1s))
    pct_perfect = float(np.mean([1 if f >= 1.0 - 1e-9 else 0 for f in f1s]) * 100)
    n_degen = sum(1 for sf in sample_f1_lists if compute_degeneracy(sf))

    split_res = {
        "n": len(split_insts),
        "greedy_f1_mean": round(float(np.mean(f1s)), 4),
        "oracle_f1_mean": round(float(np.mean(oracle_f1s)), 4),
        "headroom": round(headroom, 4),
        "pct_perfect": round(pct_perfect, 1),
        "n_degenerate": n_degen,
        "pct_degenerate": round(n_degen / len(split_insts) * 100, 1),
    }

    labels = [1 if f >= 1.0 - 1e-9 else 0 for f in f1s]
    for name, scores in [("SJ", sj), ("FK", fk), ("logprob", lp), ("EM", em), ("voting_conf", vc)]:
        rho, p_rho = safe_spearman(scores, f1s)
        auroc = safe_auroc(scores, labels)
        split_res[name] = {"rho": round(rho, 4), "p": round(p_rho, 6), "auroc": round(auroc, 4)}

    report[split_name] = split_res

    print(f"\n--- {split_name} (n={len(split_insts)}) ---")
    print(f"  Greedy F1:  {split_res['greedy_f1_mean']:.4f}")
    print(f"  Oracle F1:  {split_res['oracle_f1_mean']:.4f}")
    print(f"  Headroom:   {split_res['headroom']:.4f}")
    print(f"  % Perfect:  {split_res['pct_perfect']:.1f}%")
    print(f"  {'Signal':<14} {'rho':>8} {'AUROC':>8}")
    print(f"  {'-'*32}")
    for name in ["SJ", "FK", "logprob", "EM", "voting_conf"]:
        s = split_res[name]
        print(f"  {name:<14} {s['rho']:>8.4f} {s['auroc']:>8.4f}")

# === DGS Analysis ===
print("\n=== DGS (Degeneracy-Gated Selection) Analysis ===")
greedy_f1s, lp_f1s, gated_f1s, oracle_f1s_dgs = [], [], [], []
degen_greedy, degen_oracle = [], []
nondegen_greedy, nondegen_lp, nondegen_oracle = [], [], []
n_degen = 0

for inst in valid:
    gold_ents = inst["gold"]["entities"]
    samples = inst["samples"][:8]
    greedy = inst["greedy"]

    sample_f1s = [compute_entity_f1(s.get("entities", []), gold_ents) for s in samples]
    greedy_f1 = compute_entity_f1(greedy.get("entities", []), gold_ents)
    oracle_f1 = max(sample_f1s)

    lp_idx = max(range(len(samples)), key=lambda i: samples[i].get("mean_logprob", -999))
    lp_f1 = sample_f1s[lp_idx]

    is_degen = compute_degeneracy(sample_f1s)
    if is_degen:
        gated_f1 = greedy_f1
        n_degen += 1
        degen_greedy.append(greedy_f1)
        degen_oracle.append(oracle_f1)
    else:
        gated_f1 = lp_f1
        nondegen_greedy.append(greedy_f1)
        nondegen_lp.append(lp_f1)
        nondegen_oracle.append(oracle_f1)

    greedy_f1s.append(greedy_f1)
    lp_f1s.append(lp_f1)
    gated_f1s.append(gated_f1)
    oracle_f1s_dgs.append(oracle_f1)

n_used = len(greedy_f1s)
dgs_report = {
    "n_used": n_used, "n_degen": n_degen, "n_nondegen": n_used - n_degen,
    "degen_pct": round(n_degen / n_used * 100, 1),
    "greedy_f1": bootstrap_ci(greedy_f1s),
    "lp_f1": bootstrap_ci(lp_f1s),
    "dgs_f1": bootstrap_ci(gated_f1s),
    "oracle_f1": bootstrap_ci(oracle_f1s_dgs),
    "delta_dgs_minus_greedy": bootstrap_delta_ci(gated_f1s, greedy_f1s),
    "delta_dgs_minus_lp": bootstrap_delta_ci(gated_f1s, lp_f1s),
}

if nondegen_lp:
    dgs_report["nondegen"] = {
        "greedy": bootstrap_ci(nondegen_greedy),
        "lp": bootstrap_ci(nondegen_lp),
        "oracle": bootstrap_ci(nondegen_oracle),
        "delta_lp_minus_greedy": bootstrap_delta_ci(nondegen_lp, nondegen_greedy),
    }

report["dgs"] = dgs_report

print(f"  Instances:     {n_used}")
print(f"  Degenerate:    {n_degen} ({dgs_report['degen_pct']:.1f}%)")
print(f"  Non-degenerate:{n_used - n_degen}")
print(f"  Greedy F1:     {dgs_report['greedy_f1']['mean']:.4f} [{dgs_report['greedy_f1']['ci_lo']:.4f}, {dgs_report['greedy_f1']['ci_hi']:.4f}]")
print(f"  LP-select F1:  {dgs_report['lp_f1']['mean']:.4f} [{dgs_report['lp_f1']['ci_lo']:.4f}, {dgs_report['lp_f1']['ci_hi']:.4f}]")
print(f"  DGS F1:        {dgs_report['dgs_f1']['mean']:.4f} [{dgs_report['dgs_f1']['ci_lo']:.4f}, {dgs_report['dgs_f1']['ci_hi']:.4f}]")
print(f"  Oracle F1:     {dgs_report['oracle_f1']['mean']:.4f} [{dgs_report['oracle_f1']['ci_lo']:.4f}, {dgs_report['oracle_f1']['ci_hi']:.4f}]")
d = dgs_report["delta_dgs_minus_greedy"]
print(f"  DGS-Greedy:    {d['delta']*100:+.2f}pp [{d['ci_lo']*100:.2f}, {d['ci_hi']*100:.2f}]")
d2 = dgs_report["delta_dgs_minus_lp"]
print(f"  DGS-LP:        {d2['delta']*100:+.2f}pp [{d2['ci_lo']*100:.2f}, {d2['ci_hi']*100:.2f}]")

if nondegen_lp:
    nd = dgs_report["nondegen"]["delta_lp_minus_greedy"]
    print(f"  NonDegen LP-Greedy: {nd['delta']*100:+.2f}pp [{nd['ci_lo']*100:.2f}, {nd['ci_hi']*100:.2f}]")

# Save report
out_path = os.path.join(OUTPUT_DIR, "5signal_dgs_report.json")
with open(out_path, "w") as f:
    json.dump(report, f, indent=2, default=lambda o: float(o) if isinstance(o, (np.floating,)) else str(o))
print(f"\nReport saved to {out_path}")
