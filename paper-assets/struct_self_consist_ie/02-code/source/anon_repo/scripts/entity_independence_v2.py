"""
Entity independence analysis v2: 
- Separate testable vs non-testable reporting
- Monte Carlo null baseline for N=8 discretization
- Cramér's V for effect size
"""
import json
import numpy as np
from itertools import combinations
from scipy import stats
import os, random

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

def cramers_v(table):
    chi2 = stats.chi2_contingency(table, correction=False)[0]
    n = table.sum()
    return np.sqrt(chi2 / n) if n > 0 else 0

def mc_null_baseline(n_trials=50000, N=8):
    """What fraction of truly independent pairs show significant Fisher p<0.05 with N=8?"""
    rng = np.random.RandomState(42)
    sig_count = 0
    ratios = []
    for _ in range(n_trials):
        pi = rng.randint(1, N) / N  # exclude 0 and 1
        pj = rng.randint(1, N) / N
        xi = rng.binomial(1, pi, N)
        xj = rng.binomial(1, pj, N)
        
        a11 = int((xi & xj).sum())
        a10 = int((xi & ~xj.astype(bool)).sum())
        a01 = int((~xi.astype(bool) & xj).sum())
        a00 = int((~xi.astype(bool) & ~xj.astype(bool)).sum())
        table = np.array([[a11, a10], [a01, a00]])
        
        obs_pi = xi.mean()
        obs_pj = xj.mean()
        obs_pij = (xi & xj).mean()
        exp = obs_pi * obs_pj
        if exp > 0 and obs_pi > 0 and obs_pi < 1 and obs_pj > 0 and obs_pj < 1:
            ratios.append(obs_pij / exp)
        
        try:
            _, pval = stats.fisher_exact(table)
            if pval < 0.05:
                sig_count += 1
        except:
            pass
    
    return {
        "n_trials": n_trials,
        "pct_significant_null": round(sig_count / n_trials * 100, 2),
        "mean_ratio_null": round(np.mean(ratios), 4),
        "median_ratio_null": round(np.median(ratios), 4),
    }

def analyze_dataset(data, dataset_name):
    n_total = len(data)
    
    # Separate tracking for testable vs all
    testable_ratios = []
    testable_cramers = []
    testable_sig_pos = 0
    testable_sig_neg = 0
    testable_nonsig = 0
    
    n_trivial_both1 = 0  # both always present
    n_trivial_one01 = 0  # at least one always/never present
    
    n_instances_used = 0
    all_obs_list = []
    all_exp_list = []
    none_obs_list = []
    none_exp_list = []
    indiv_probs = []
    
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
            for i, ge in enumerate(gold_entities):
                presence[i, j] = check_gold_in_sample(ge, sample['entities'])
        
        probs = presence.mean(axis=1)
        for p in probs:
            indiv_probs.append(p)
        
        for i, j in combinations(range(len(gold_entities)), 2):
            pi, pj = probs[i], probs[j]
            
            if (pi == 1.0 and pj == 1.0):
                n_trivial_both1 += 1
                continue
            if pi == 0 or pi == 1 or pj == 0 or pj == 1:
                n_trivial_one01 += 1
                continue
            
            pij = (presence[i] & presence[j]).mean()
            expected = pi * pj
            ratio = pij / expected if expected > 0 else float('inf')
            testable_ratios.append(ratio)
            
            a11 = int((presence[i] & presence[j]).sum())
            a10 = int((presence[i] & ~presence[j]).sum())
            a01 = int((~presence[i] & presence[j]).sum())
            a00 = int((~presence[i] & ~presence[j]).sum())
            table = np.array([[a11, a10], [a01, a00]])
            
            if table.min() >= 0:
                try:
                    cv = cramers_v(table)
                    testable_cramers.append(cv)
                except:
                    testable_cramers.append(0)
            
            try:
                _, pval = stats.fisher_exact(table)
                if pval < 0.05:
                    if ratio > 1:
                        testable_sig_pos += 1
                    else:
                        testable_sig_neg += 1
                else:
                    testable_nonsig += 1
            except:
                testable_nonsig += 1
        
        all_obs = (presence.all(axis=0)).mean()
        none_obs = (~presence.any(axis=0)).mean()
        all_exp = np.prod(probs) if all(probs > 0) else 0
        none_exp = np.prod(1 - probs)
        
        all_obs_list.append(all_obs)
        all_exp_list.append(all_exp)
        none_obs_list.append(none_obs)
        none_exp_list.append(none_exp)
    
    testable_ratios = np.array(testable_ratios)
    testable_cramers = np.array(testable_cramers)
    n_testable = len(testable_ratios)
    n_total_pairs = n_testable + n_trivial_both1 + n_trivial_one01
    n_sig = testable_sig_pos + testable_sig_neg
    
    all_obs_arr = np.array(all_obs_list)
    all_exp_arr = np.array(all_exp_list)
    none_obs_arr = np.array(none_obs_list)
    none_exp_arr = np.array(none_exp_list)
    
    result = {
        "dataset": dataset_name,
        "n_instances_total": n_total,
        "n_instances_ge2_entities": n_instances_used,
        "n_pairs_total": n_total_pairs,
        "n_pairs_trivial_both_always": n_trivial_both1,
        "n_pairs_trivial_one_deterministic": n_trivial_one01,
        "n_pairs_testable": n_testable,
        "pct_pairs_testable": round(n_testable / n_total_pairs * 100, 1) if n_total_pairs > 0 else 0,
        
        "testable_mean_ratio": round(float(np.mean(testable_ratios)), 4) if n_testable > 0 else None,
        "testable_median_ratio": round(float(np.median(testable_ratios)), 4) if n_testable > 0 else None,
        "testable_std_ratio": round(float(np.std(testable_ratios)), 4) if n_testable > 0 else None,
        "testable_mean_cramers_v": round(float(np.mean(testable_cramers)), 4) if len(testable_cramers) > 0 else None,
        "testable_median_cramers_v": round(float(np.median(testable_cramers)), 4) if len(testable_cramers) > 0 else None,
        
        "testable_pct_sig_p05": round(n_sig / n_testable * 100, 1) if n_testable > 0 else None,
        "testable_pct_sig_positive": round(testable_sig_pos / n_testable * 100, 1) if n_testable > 0 else None,
        "testable_pct_sig_negative": round(testable_sig_neg / n_testable * 100, 1) if n_testable > 0 else None,
        "testable_n_sig_positive": testable_sig_pos,
        "testable_n_sig_negative": testable_sig_neg,
        "testable_n_nonsig": testable_nonsig,
        
        "overall_pct_sig_p05": round(n_sig / n_total_pairs * 100, 1) if n_total_pairs > 0 else None,
        
        "ratio_percentiles": {
            "p5": round(float(np.percentile(testable_ratios, 5)), 4),
            "p25": round(float(np.percentile(testable_ratios, 25)), 4),
            "p50": round(float(np.percentile(testable_ratios, 50)), 4),
            "p75": round(float(np.percentile(testable_ratios, 75)), 4),
            "p95": round(float(np.percentile(testable_ratios, 95)), 4),
        } if n_testable > 0 else None,
        
        "all_present_obs_mean": round(float(all_obs_arr.mean()), 4),
        "all_present_exp_mean": round(float(all_exp_arr.mean()), 4),
        "all_present_ratio": round(float(all_obs_arr.mean() / all_exp_arr.mean()), 4) if all_exp_arr.mean() > 0 else None,
        "none_present_obs_mean": round(float(none_obs_arr.mean()), 4),
        "none_present_exp_mean": round(float(none_exp_arr.mean()), 4),
        "none_present_ratio": round(float(none_obs_arr.mean() / none_exp_arr.mean()), 4) if none_exp_arr.mean() > 0 else None,
        
        "individual_prob_mean": round(float(np.mean(indiv_probs)), 4),
        "individual_prob_median": round(float(np.median(indiv_probs)), 4),
    }
    
    return result

def main():
    print("=== Monte Carlo null baseline (true independence, N=8) ===")
    mc = mc_null_baseline(50000, 8)
    print(f"  Under true independence with N=8:")
    print(f"    Fisher p<0.05 rate: {mc['pct_significant_null']}% (expected ~5%)")
    print(f"    Mean ratio: {mc['mean_ratio_null']}")
    print(f"    Median ratio: {mc['median_ratio_null']}")
    print()
    
    datasets = {
        "FewNERD": "/root/autodl-tmp/struct_self_consist_ie/output/exp_021_fewnerd_n8_seed123/samples.jsonl",
        "CoNLL2003": "/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n8_seed123/samples.jsonl",
        "SciERC": "/root/autodl-tmp/struct_self_consist_ie/output/exp_018_qwen_scierc_seed123/samples.jsonl",
    }
    
    results = {"mc_null_baseline": mc}
    for name, path in datasets.items():
        if not os.path.exists(path):
            print(f"SKIP {name}: {path} not found")
            continue
        print(f"Loading {name}...")
        data = load_samples(path)
        print(f"  {len(data)} instances, N={len(data[0]['samples'])} samples")
        
        if len(data) > 5000:
            random.seed(42)
            data = random.sample(data, 5000)
            print(f"  Subsampled to {len(data)}")
        
        r = analyze_dataset(data, name)
        results[name] = r
        
        print(f"\n=== {name} ===")
        print(f"  Instances >=2 ent: {r['n_instances_ge2_entities']}")
        print(f"  Total pairs: {r['n_pairs_total']}")
        print(f"    Trivial (both always): {r['n_pairs_trivial_both_always']}")
        print(f"    Trivial (one determ.): {r['n_pairs_trivial_one_deterministic']}")
        print(f"    Testable: {r['n_pairs_testable']} ({r['pct_pairs_testable']}%)")
        print(f"  Among testable pairs:")
        print(f"    Mean ratio: {r['testable_mean_ratio']}")
        print(f"    Median ratio: {r['testable_median_ratio']}")
        print(f"    Mean Cramér's V: {r['testable_mean_cramers_v']}")
        print(f"    Sig p<0.05: {r['testable_pct_sig_p05']}% (+:{r['testable_pct_sig_positive']}%, -:{r['testable_pct_sig_negative']}%)")
        print(f"  Overall sig rate: {r['overall_pct_sig_p05']}%")
        print(f"  All-present obs/exp: {r['all_present_ratio']}")
        print(f"  None-present obs/exp: {r['none_present_ratio']}")
        print(f"  Ratio percentiles: {r['ratio_percentiles']}")
        print()
    
    out_dir = "/root/autodl-tmp/struct_self_consist_ie/output/entity_independence_analysis"
    os.makedirs(out_dir, exist_ok=True)
    with open(f"{out_dir}/entity_independence_v2.json", "w") as f:
        json.dump(results, f, indent=2)
    print(f"Saved to {out_dir}/entity_independence_v2.json")

if __name__ == "__main__":
    main()
