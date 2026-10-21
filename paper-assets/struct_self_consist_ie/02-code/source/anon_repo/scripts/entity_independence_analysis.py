import json
import numpy as np
from itertools import combinations
from collections import defaultdict
from scipy import stats
import os
import sys
import random

def load_samples(path):
    data = []
    with open(path) as f:
        for line in f:
            data.append(json.loads(line))
    return data

def entity_key(e):
    return (e['start'], e['end'], e['type'])

def entity_key_text(e):
    return (e['text'].lower().strip(), e['type'])

def check_gold_in_sample(gold_ent, sample_entities):
    gk = entity_key(gold_ent)
    for se in sample_entities:
        if entity_key(se) == gk:
            return True
    gt = entity_key_text(gold_ent)
    for se in sample_entities:
        if entity_key_text(se) == gt:
            return True
    return False

def analyze_dataset(data, dataset_name):
    n_total = len(data)
    pair_ratios = []
    pair_chi2_pvals = []
    pair_positive_dep = 0
    pair_negative_dep = 0
    pair_independent = 0
    n_pairs_total = 0
    n_instances_used = 0
    
    all_or_nothing_obs_all = []
    all_or_nothing_exp_all = []
    none_obs_all = []
    none_exp_all = []
    individual_probs = []
    
    for idx, inst in enumerate(data):
        if idx % 2000 == 0:
            print(f"  [{dataset_name}] {idx}/{n_total}...", flush=True)
        
        gold_entities = inst['gold']['entities']
        samples = inst['samples']
        N = len(samples)
        
        if len(gold_entities) < 2:
            continue
        
        n_instances_used += 1
        
        presence = np.zeros((len(gold_entities), N), dtype=bool)
        for j, sample in enumerate(samples):
            sample_ents = sample['entities']
            for i, ge in enumerate(gold_entities):
                presence[i, j] = check_gold_in_sample(ge, sample_ents)
        
        probs = presence.mean(axis=1)
        for p in probs:
            individual_probs.append(p)
        
        for i, j in combinations(range(len(gold_entities)), 2):
            pi = probs[i]
            pj = probs[j]
            pij = (presence[i] & presence[j]).mean()
            expected = pi * pj
            
            n_pairs_total += 1
            
            if expected > 0 and pi > 0 and pi < 1 and pj > 0 and pj < 1:
                ratio = pij / expected
                pair_ratios.append(ratio)
                
                a11 = int((presence[i] & presence[j]).sum())
                a10 = int((presence[i] & ~presence[j]).sum())
                a01 = int((~presence[i] & presence[j]).sum())
                a00 = int((~presence[i] & ~presence[j]).sum())
                table = np.array([[a11, a10], [a01, a00]])
                
                try:
                    _, pval = stats.fisher_exact(table)
                    pair_chi2_pvals.append(pval)
                    if pval < 0.05:
                        if ratio > 1:
                            pair_positive_dep += 1
                        else:
                            pair_negative_dep += 1
                    else:
                        pair_independent += 1
                except:
                    pair_independent += 1
            else:
                pair_independent += 1
        
        all_present_obs = (presence.all(axis=0)).mean()
        none_present_obs = (~presence.any(axis=0)).mean()
        all_present_exp = np.prod(probs) if all(probs > 0) else 0
        none_present_exp = np.prod(1 - probs)
        
        all_or_nothing_obs_all.append(all_present_obs)
        all_or_nothing_exp_all.append(all_present_exp)
        none_obs_all.append(none_present_obs)
        none_exp_all.append(none_present_exp)
    
    pair_ratios = np.array(pair_ratios)
    pair_chi2_pvals = np.array(pair_chi2_pvals)
    
    n_tested = pair_positive_dep + pair_negative_dep + pair_independent
    n_sig = pair_positive_dep + pair_negative_dep
    
    all_obs = np.array(all_or_nothing_obs_all)
    all_exp = np.array(all_or_nothing_exp_all)
    none_obs = np.array(none_obs_all)
    none_exp = np.array(none_exp_all)
    
    result = {
        "dataset": dataset_name,
        "n_instances_total": n_total,
        "n_instances_with_ge2_entities": n_instances_used,
        "n_entity_pairs_total": n_pairs_total,
        "n_entity_pairs_testable": int(len(pair_ratios)),
        "mean_cooccurrence_ratio": round(float(np.mean(pair_ratios)), 4) if len(pair_ratios) > 0 else None,
        "median_cooccurrence_ratio": round(float(np.median(pair_ratios)), 4) if len(pair_ratios) > 0 else None,
        "std_cooccurrence_ratio": round(float(np.std(pair_ratios)), 4) if len(pair_ratios) > 0 else None,
        "pct_ratio_in_0.9_1.1": round(float((np.abs(pair_ratios - 1.0) < 0.1).mean() * 100), 1) if len(pair_ratios) > 0 else None,
        "pct_ratio_in_0.8_1.2": round(float((np.abs(pair_ratios - 1.0) < 0.2).mean() * 100), 1) if len(pair_ratios) > 0 else None,
        "n_fisher_tests": n_tested,
        "n_significant_p05": int(n_sig),
        "pct_significant_p05": round(float(n_sig / n_tested * 100), 1) if n_tested > 0 else None,
        "pct_positive_dependent": round(float(pair_positive_dep / n_tested * 100), 1) if n_tested > 0 else None,
        "pct_negative_dependent": round(float(pair_negative_dep / n_tested * 100), 1) if n_tested > 0 else None,
        "pct_independent_p05": round(float(pair_independent / n_tested * 100), 1) if n_tested > 0 else None,
        "all_present_observed_mean": round(float(all_obs.mean()), 4) if len(all_obs) > 0 else None,
        "all_present_expected_mean": round(float(all_exp.mean()), 4) if len(all_exp) > 0 else None,
        "all_present_ratio": round(float(all_obs.mean() / all_exp.mean()), 4) if len(all_exp) > 0 and all_exp.mean() > 0 else None,
        "none_present_observed_mean": round(float(none_obs.mean()), 4) if len(none_obs) > 0 else None,
        "none_present_expected_mean": round(float(none_exp.mean()), 4) if len(none_exp) > 0 else None,
        "none_present_ratio": round(float(none_obs.mean() / none_exp.mean()), 4) if len(none_exp) > 0 and none_exp.mean() > 0 else None,
        "individual_entity_prob_mean": round(float(np.mean(individual_probs)), 4),
        "individual_entity_prob_median": round(float(np.median(individual_probs)), 4),
        "ratio_percentiles": {
            "p5": round(float(np.percentile(pair_ratios, 5)), 4) if len(pair_ratios) > 0 else None,
            "p25": round(float(np.percentile(pair_ratios, 25)), 4) if len(pair_ratios) > 0 else None,
            "p50": round(float(np.percentile(pair_ratios, 50)), 4) if len(pair_ratios) > 0 else None,
            "p75": round(float(np.percentile(pair_ratios, 75)), 4) if len(pair_ratios) > 0 else None,
            "p95": round(float(np.percentile(pair_ratios, 95)), 4) if len(pair_ratios) > 0 else None,
        }
    }
    
    return result

def main():
    datasets = {
        "FewNERD": "/root/autodl-tmp/struct_self_consist_ie/output/exp_021_fewnerd_n8_seed123/samples.jsonl",
        "CoNLL2003": "/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n8_seed123/samples.jsonl",
        "SciERC": "/root/autodl-tmp/struct_self_consist_ie/output/exp_018_qwen_scierc_seed123/samples.jsonl",
    }
    
    results = {}
    for name, path in datasets.items():
        if not os.path.exists(path):
            print(f"SKIP {name}: {path} not found")
            continue
        print(f"Loading {name}...")
        data = load_samples(path)
        N_samples = len(data[0]['samples'])
        print(f"  {len(data)} instances, N={N_samples} samples each")
        
        # Subsample large datasets for tractability
        if len(data) > 5000:
            random.seed(42)
            data = random.sample(data, 5000)
            print(f"  Subsampled to {len(data)} instances")
        
        result = analyze_dataset(data, name)
        results[name] = result
        
        print(f"\n=== {name} ===")
        print(f"  Instances with >=2 entities: {result['n_instances_with_ge2_entities']}")
        print(f"  Entity pairs testable: {result['n_entity_pairs_testable']}")
        print(f"  Mean co-occ ratio: {result['mean_cooccurrence_ratio']}")
        print(f"  Median co-occ ratio: {result['median_cooccurrence_ratio']}")
        print(f"  Fisher sig (p<0.05): {result['pct_significant_p05']}%")
        print(f"    +dep: {result['pct_positive_dependent']}% | -dep: {result['pct_negative_dependent']}%")
        print(f"  All-present obs/exp: {result['all_present_ratio']}")
        print(f"  None-present obs/exp: {result['none_present_ratio']}")
        print(f"  Ratio percentiles: {result['ratio_percentiles']}")
        print()
    
    out_dir = "/root/autodl-tmp/struct_self_consist_ie/output/entity_independence_analysis"
    os.makedirs(out_dir, exist_ok=True)
    
    with open(f"{out_dir}/entity_independence.json", "w") as f:
        json.dump(results, f, indent=2)
    
    print(f"\nAll results saved to {out_dir}/entity_independence.json")

if __name__ == "__main__":
    main()
