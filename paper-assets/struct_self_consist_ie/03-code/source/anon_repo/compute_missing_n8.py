#!/usr/bin/env python3
"""Compute unified pipeline rho for missing N=8 SciERC experiments."""
import json, sys
import numpy as np
from collections import Counter
from scipy.stats import spearmanr

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from consistency import fleiss_kappa_surface, structural_consistency_soft_jaccard
from evaluation import per_instance_f1

BASE = "/root/autodl-tmp/struct_self_consist_ie/output"

MISSING_EXPS = {
    "qwen_scierc_n8_seed42": {
        "path": f"{BASE}/exp_012_rerun_1024/samples.jsonl",
        "subtask": "joint",
    },
    "qwen_scierc_n8_seed123": {
        "path": f"{BASE}/exp_018_qwen_scierc_seed123/samples.jsonl",
        "subtask": "joint",
    },
    "llama_scierc_n8_seed123": {
        "path": f"{BASE}/exp_018_llama_scierc_seed123/samples.jsonl",
        "subtask": "joint",
    },
}

def load_data(path):
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]

def compute_exact_match_rate(samples, subtask):
    if subtask in ("ner", "joint"):
        keys = [frozenset((e["text"], e["type"]) for e in s.get("entities", [])) for s in samples]
    else:
        keys = [frozenset((r["head"], r["tail"], r["type"]) for r in s.get("relations", [])) for s in samples]
    if not keys: return 0.0
    c = Counter(keys)
    return c.most_common(1)[0][1] / len(samples)

def compute_voting_conf(samples, subtask):
    N = len(samples)
    if N == 0: return 0.0
    counter = Counter()
    if subtask in ("ner", "joint"):
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

def safe_spearman(x, y):
    x, y = np.asarray(x, float), np.asarray(y, float)
    m = np.isfinite(x) & np.isfinite(y)
    x, y = x[m], y[m]
    if len(x) < 3: return float("nan")
    return float(spearmanr(x, y).statistic)

def safe_auroc(scores, labels):
    from scipy.stats import rankdata
    scores, labels = np.asarray(scores, float), np.asarray(labels, int)
    if len(np.unique(labels)) < 2: return float("nan")
    n_pos, n_neg = (labels==1).sum(), (labels==0).sum()
    if n_pos == 0 or n_neg == 0: return float("nan")
    ranks = rankdata(scores)
    u = ranks[labels==1].sum() - n_pos*(n_pos+1)/2
    return float(u / (n_pos * n_neg))

def compute_unified(exp_id, config):
    data = load_data(config["path"])
    n_total = len(data)
    n_gold_empty = sum(1 for d in data if len(d["gold"].get("entities", [])) == 0)
    valid_data = [d for d in data if len(d["gold"].get("entities", [])) > 0]
    n_valid = len(valid_data)

    fk_vals, sj_vals, vc_vals, em_vals, lp_vals, f1_vals = [], [], [], [], [], []
    for d in valid_data:
        samples = d["samples"]
        greedy = d.get("greedy", samples[0])
        fk_vals.append(fleiss_kappa_surface(samples, subtask="ner"))
        sj_vals.append(structural_consistency_soft_jaccard(samples, subtask="ner"))
        vc_vals.append(compute_voting_conf(samples, "ner"))
        em_vals.append(compute_exact_match_rate(samples, "ner"))
        lp_vals.append(compute_mean_logprob(samples))
        f1_vals.append(per_instance_f1(greedy, d["gold"], subtask="ner"))

    rho_fk = safe_spearman(fk_vals, f1_vals)
    rho_sj = safe_spearman(sj_vals, f1_vals)
    rho_vc = safe_spearman(vc_vals, f1_vals)
    rho_em = safe_spearman(em_vals, f1_vals)
    rho_lp = safe_spearman(lp_vals, f1_vals)

    f1_arr = np.array(f1_vals)
    median_f1 = float(np.median(f1_arr))
    binary = (f1_arr >= median_f1).astype(int)
    if median_f1 == 1.0:
        binary = (f1_arr >= 1.0).astype(int)

    auroc_fk = safe_auroc(fk_vals, binary)
    auroc_sj = safe_auroc(sj_vals, binary)
    auroc_vc = safe_auroc(vc_vals, binary)
    auroc_em = safe_auroc(em_vals, binary)
    auroc_lp = safe_auroc(lp_vals, binary)

    result = {
        "n_instances": n_valid,
        "n_total": n_total,
        "n_gold_empty": n_gold_empty,
        "VC": round(rho_vc, 4),
        "SJ": round(rho_sj, 4),
        "FK": round(rho_fk, 4),
        "EM": round(rho_em, 4),
        "LP": round(rho_lp, 4),
        "auroc_VC": round(auroc_vc, 4),
        "auroc_SJ": round(auroc_sj, 4),
        "auroc_FK": round(auroc_fk, 4),
        "auroc_EM": round(auroc_em, 4),
        "auroc_LP": round(auroc_lp, 4),
    }

    # RE metrics for joint subtask
    if config["subtask"] == "joint":
        re_valid = [d for d in data if len(d["gold"].get("relations", [])) > 0]
        re_fk, re_sj, re_f1 = [], [], []
        for d in re_valid:
            samples = d["samples"]
            greedy = d.get("greedy", samples[0])
            re_fk.append(fleiss_kappa_surface(samples, subtask="re"))
            re_sj.append(structural_consistency_soft_jaccard(samples, subtask="re"))
            re_f1.append(per_instance_f1(greedy, d["gold"], subtask="re"))
        result["re_n_valid"] = len(re_valid)
        result["re_FK"] = round(safe_spearman(re_fk, re_f1), 4)
        result["re_SJ"] = round(safe_spearman(re_sj, re_f1), 4)

    return result

# Run
new_results = {}
for exp_id, config in MISSING_EXPS.items():
    print(f"\n=== {exp_id} ===")
    r = compute_unified(exp_id, config)
    new_results[exp_id] = r
    print(f"  n_valid={r['n_instances']}, n_total={r['n_total']}, n_gold_empty={r['n_gold_empty']}")
    print(f"  SJ={r['SJ']}, FK={r['FK']}, VC={r['VC']}, EM={r['EM']}, LP={r['LP']}")
    print(f"  auroc_SJ={r['auroc_SJ']}, auroc_FK={r['auroc_FK']}, auroc_VC={r['auroc_VC']}, auroc_EM={r['auroc_EM']}, auroc_LP={r['auroc_LP']}")
    if "re_n_valid" in r:
        print(f"  RE: n={r['re_n_valid']}, FK={r['re_FK']}, SJ={r['re_SJ']}")

# Load existing JSON and append
json_path = f"{BASE}/analysis_unified_rho_full.json"
with open(json_path) as f:
    existing = json.load(f)

for k, v in new_results.items():
    existing["results"][k] = v

existing["metadata"]["date"] = "2026-05-15"
existing["metadata"]["n8_seed123_added"] = True

with open(json_path, "w") as f:
    json.dump(existing, f, indent=2)

print(f"\n✓ Appended {len(new_results)} entries to {json_path}")
print("\n=== JSON output for registry ===")
print(json.dumps(new_results, indent=2))
