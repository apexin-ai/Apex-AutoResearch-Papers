#!/usr/bin/env python3
"""Rho consistency audit: diagnose and recompute with unified pipeline."""
import json, sys
import numpy as np
from collections import Counter
from scipy.stats import spearmanr

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from consistency import fleiss_kappa_surface, structural_consistency_soft_jaccard
from evaluation import per_instance_f1

BASE = "/root/autodl-tmp/struct_self_consist_ie/output"

EXPERIMENTS = {
    "exp_017_llama_conll_n16_r1024": {
        "path": f"{BASE}/exp_017_llama_conll_n16_r1024/samples.jsonl",
        "subtask": "ner",
        "registry_rho_fk": 0.8095,
        "registry_rho_sj": 0.1815,
        "registry_n": 3453,
    },
    "exp_017_llama_conll_n16_s456_r1024": {
        "path": f"{BASE}/exp_017_llama_conll_n16_s456_r1024/samples.jsonl",
        "subtask": "ner",
        "registry_rho_fk": 0.8085,
        "registry_rho_sj": 0.1895,
        "registry_n": 3453,
    },
    "exp_001_n16_seed456": {
        "path": f"{BASE}/exp001_n16_seed456/samples.jsonl",
        "subtask": "joint",
        "registry_rho_fk": 0.3448,
        "registry_rho_sj": 0.4134,
        "registry_n": 551,
    },
    "exp_011_ood_conll_to_scierc": {
        "path": f"{BASE}/exp_011_ood_conll_to_scierc/samples.jsonl",
        "subtask": "ner",
        "registry_rho_fk": -0.069,
        "registry_rho_sj": -0.186,
        "registry_n": None,
    },
}


def load_data(path):
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]


# --- OLD pipeline functions (from compute_metrics.py) ---
def old_compute_fk(samples):
    N = len(samples)
    ent_sets = [{(e["text"], e["type"]) for e in s.get("entities", [])} for s in samples]
    all_ents = set().union(*ent_sets)
    if not all_ents:
        return 0.0  # BUG: returns 0.0 for all-empty → should be 1.0
    n_sub = len(all_ents)
    ratings = np.zeros((n_sub, 2))
    for idx, ent in enumerate(all_ents):
        present = sum(1 for es in ent_sets if ent in es)
        ratings[idx] = [N - present, present]
    P_i = (np.sum(ratings**2, axis=1) - N) / (N * (N - 1))
    P_bar = np.mean(P_i)
    p_j = np.sum(ratings, axis=0) / (n_sub * N)
    P_e = np.sum(p_j**2)
    if P_e >= 1.0:
        return 1.0
    return float((P_bar - P_e) / (1 - P_e))


def old_compute_sj(samples):
    from itertools import combinations
    def entity_surface_set(ext):
        return frozenset((e["text"], e["type"]) for e in ext.get("entities", []))
    sets = [entity_surface_set(s) for s in samples]
    if len(sets) < 2:
        return 1.0
    scores = []
    for i, j in combinations(range(len(sets)), 2):
        union = len(sets[i] | sets[j])
        scores.append(len(sets[i] & sets[j]) / union if union else 1.0)
    return float(np.mean(scores))


def old_f1(pred_ext, gold_ext, subtask="ner"):
    if subtask in ("ner", "joint"):
        pred = {(e["start"], e["end"], e["type"]) for e in pred_ext.get("entities", [])}
        gold = {(e["start"], e["end"], e["type"]) for e in gold_ext.get("entities", [])}
    else:
        pred = set()
        gold = set()
    tp = len(pred & gold)
    if tp == 0:
        return 0.0
    fp = len(pred - gold)
    fn = len(gold - pred)
    p, r = tp/(tp+fp), tp/(tp+fn)
    return 2*p*r/(p+r)


# --- NEW pipeline: gold-filtered, uses consistency.py ---
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


def analyze_experiment(exp_id, config):
    data = load_data(config["path"])
    subtask = config["subtask"]
    ner_subtask = "ner"  # for NER metrics specifically
    
    n_total = len(data)
    entity_key = "entities"
    
    # Count gold-empty instances
    n_gold_empty = sum(1 for d in data if len(d["gold"].get(entity_key, [])) == 0)
    
    # --- OLD PIPELINE: all instances ---
    old_fk_vals, old_sj_vals, old_f1_vals = [], [], []
    for d in data:
        samples = d["samples"]
        old_fk_vals.append(old_compute_fk(samples))
        old_sj_vals.append(old_compute_sj(samples))
        old_f1_vals.append(old_f1(d.get("greedy", samples[0]), d["gold"], subtask=ner_subtask))
    
    old_rho_fk = safe_spearman(old_fk_vals, old_f1_vals)
    old_rho_sj = safe_spearman(old_sj_vals, old_f1_vals)
    
    # Show gold-empty instance behavior
    gold_empty_fk = [fk for fk, d in zip(old_fk_vals, data) if len(d["gold"].get(entity_key, [])) == 0]
    gold_empty_sj = [sj for sj, d in zip(old_sj_vals, data) if len(d["gold"].get(entity_key, [])) == 0]
    gold_empty_f1 = [f for f, d in zip(old_f1_vals, data) if len(d["gold"].get(entity_key, [])) == 0]
    
    # --- NEW PIPELINE: gold-filtered ---
    valid_data = [d for d in data if len(d["gold"].get(entity_key, [])) > 0]
    n_valid = len(valid_data)
    
    new_fk_vals, new_sj_vals, new_vc_vals, new_em_vals, new_lp_vals, new_f1_vals = [], [], [], [], [], []
    for d in valid_data:
        samples = d["samples"]
        greedy = d.get("greedy", samples[0])
        new_fk_vals.append(fleiss_kappa_surface(samples, subtask=ner_subtask))
        new_sj_vals.append(structural_consistency_soft_jaccard(samples, subtask=ner_subtask))
        new_vc_vals.append(compute_voting_conf(samples, ner_subtask))
        new_em_vals.append(compute_exact_match_rate(samples, ner_subtask))
        new_lp_vals.append(compute_mean_logprob(samples))
        new_f1_vals.append(per_instance_f1(greedy, d["gold"], subtask=ner_subtask))
    
    new_rho_fk = safe_spearman(new_fk_vals, new_f1_vals)
    new_rho_sj = safe_spearman(new_sj_vals, new_f1_vals)
    new_rho_vc = safe_spearman(new_vc_vals, new_f1_vals)
    new_rho_em = safe_spearman(new_em_vals, new_f1_vals)
    new_rho_lp = safe_spearman(new_lp_vals, new_f1_vals)
    
    # AUROC (binary: F1 >= median)
    f1_arr = np.array(new_f1_vals)
    median_f1 = float(np.median(f1_arr))
    binary = (f1_arr >= median_f1).astype(int)
    if median_f1 == 1.0:
        binary = (f1_arr >= 1.0).astype(int)
    
    new_auroc_fk = safe_auroc(new_fk_vals, binary)
    new_auroc_sj = safe_auroc(new_sj_vals, binary)
    new_auroc_vc = safe_auroc(new_vc_vals, binary)
    new_auroc_em = safe_auroc(new_em_vals, binary)
    new_auroc_lp = safe_auroc(new_lp_vals, binary)
    
    # Conditional (greedy F1 > 0)
    cond_mask = [f > 0 for f in new_f1_vals]
    n_conditional = sum(cond_mask)
    cond_fk = [v for v, m in zip(new_fk_vals, cond_mask) if m]
    cond_sj = [v for v, m in zip(new_sj_vals, cond_mask) if m]
    cond_vc = [v for v, m in zip(new_vc_vals, cond_mask) if m]
    cond_em = [v for v, m in zip(new_em_vals, cond_mask) if m]
    cond_lp = [v for v, m in zip(new_lp_vals, cond_mask) if m]
    cond_f1 = [v for v, m in zip(new_f1_vals, cond_mask) if m]
    
    cond_rho_fk = safe_spearman(cond_fk, cond_f1)
    cond_rho_sj = safe_spearman(cond_sj, cond_f1)
    
    # RE metrics (for joint subtask)
    re_metrics = {}
    if subtask == "joint":
        re_valid = [d for d in data if len(d["gold"].get("relations", [])) > 0]
        re_fk, re_sj, re_f1 = [], [], []
        for d in re_valid:
            samples = d["samples"]
            greedy = d.get("greedy", samples[0])
            re_fk.append(fleiss_kappa_surface(samples, subtask="re"))
            re_sj.append(structural_consistency_soft_jaccard(samples, subtask="re"))
            re_f1.append(per_instance_f1(greedy, d["gold"], subtask="re"))
        re_metrics = {
            "n_re_valid": len(re_valid),
            "rho_fk_re": round(safe_spearman(re_fk, re_f1), 4),
            "rho_sj_re": round(safe_spearman(re_sj, re_f1), 4),
        }
    
    result = {
        "exp_id": exp_id,
        "n_total": n_total,
        "n_gold_empty": n_gold_empty,
        "n_valid": n_valid,
        "n_conditional": n_conditional,
        "gold_empty_analysis": {
            "n": n_gold_empty,
            "fk_mean": round(float(np.mean(gold_empty_fk)), 4) if gold_empty_fk else None,
            "fk_std": round(float(np.std(gold_empty_fk)), 4) if gold_empty_fk else None,
            "sj_mean": round(float(np.mean(gold_empty_sj)), 4) if gold_empty_sj else None,
            "f1_mean": round(float(np.mean(gold_empty_f1)), 4) if gold_empty_f1 else None,
        },
        "old_pipeline": {
            "n": n_total,
            "rho_fk": round(old_rho_fk, 4),
            "rho_sj": round(old_rho_sj, 4),
            "registry_rho_fk": config["registry_rho_fk"],
            "registry_rho_sj": config["registry_rho_sj"],
        },
        "new_pipeline_full": {
            "n": n_valid,
            "rho_fk": round(new_rho_fk, 4),
            "rho_sj": round(new_rho_sj, 4),
            "rho_vc": round(new_rho_vc, 4),
            "rho_em": round(new_rho_em, 4),
            "rho_lp": round(new_rho_lp, 4),
            "auroc_fk": round(new_auroc_fk, 4),
            "auroc_sj": round(new_auroc_sj, 4),
            "auroc_vc": round(new_auroc_vc, 4),
            "auroc_em": round(new_auroc_em, 4),
            "auroc_lp": round(new_auroc_lp, 4),
            "median_f1": round(median_f1, 4),
        },
        "new_pipeline_conditional": {
            "n": n_conditional,
            "rho_fk": round(cond_rho_fk, 4),
            "rho_sj": round(cond_rho_sj, 4),
        },
    }
    if re_metrics:
        result["re_metrics"] = re_metrics
    
    return result


if __name__ == "__main__":
    all_results = {}
    for exp_id, config in EXPERIMENTS.items():
        print(f"\nAnalyzing {exp_id}...")
        result = analyze_experiment(exp_id, config)
        all_results[exp_id] = result
        
        print(f"  Total: {result['n_total']}, Gold-empty: {result['n_gold_empty']}, Valid: {result['n_valid']}")
        ge = result['gold_empty_analysis']
        if ge['n'] > 0:
            print(f"  Gold-empty instances: FK_mean={ge['fk_mean']}, SJ_mean={ge['sj_mean']}, F1_mean={ge['f1_mean']}")
        
        old = result['old_pipeline']
        print(f"  OLD pipeline (n={old['n']}): rho_fk={old['rho_fk']}, rho_sj={old['rho_sj']}")
        print(f"    Registry:               rho_fk={old['registry_rho_fk']}, rho_sj={old['registry_rho_sj']}")
        
        new = result['new_pipeline_full']
        print(f"  NEW pipeline (n={new['n']}): rho_fk={new['rho_fk']}, rho_sj={new['rho_sj']}")
        print(f"    rho_vc={new['rho_vc']}, rho_em={new['rho_em']}, rho_lp={new['rho_lp']}")
        
        cond = result['new_pipeline_conditional']
        print(f"  CONDITIONAL (n={cond['n']}): rho_fk={cond['rho_fk']}, rho_sj={cond['rho_sj']}")
        
        if 're_metrics' in result:
            re = result['re_metrics']
            print(f"  RE (n={re['n_re_valid']}): rho_fk={re['rho_fk_re']}, rho_sj={re['rho_sj_re']}")
    
    out_path = f"{BASE}/rho_audit_results.json"
    with open(out_path, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\nSaved to {out_path}")
