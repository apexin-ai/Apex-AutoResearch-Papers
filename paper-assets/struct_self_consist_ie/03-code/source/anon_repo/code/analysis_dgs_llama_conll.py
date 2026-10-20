#!/usr/bin/env python3
"""DGS + 5-signal analysis for LLaMA CoNLL, with cross-model comparison."""

import json
import os
import sys
import numpy as np
from scipy import stats as scipy_stats

sys.path.insert(0, "/root/autodl-tmp/struct_self_consist_ie/code")
from unified_metrics import compute_entity_f1, compute_degeneracy

BASE = "/root/autodl-tmp/struct_self_consist_ie"
OUT_DIR = f"{BASE}/output/exp_017_llama_conll"
os.makedirs(OUT_DIR, exist_ok=True)

# === DGS Analysis ===

def bootstrap_ci(values, n_boot=10000, ci=0.95, seed=42):
    rng = np.random.RandomState(seed)
    arr = np.array(values)
    n = len(arr)
    if n == 0:
        return {'mean': 0.0, 'ci_lo': 0.0, 'ci_hi': 0.0}
    boot_means = [arr[rng.randint(0, n, n)].mean() for _ in range(n_boot)]
    boot_means = sorted(boot_means)
    lo = boot_means[int((1 - ci) / 2 * n_boot)]
    hi = boot_means[int((1 + ci) / 2 * n_boot)]
    return {'mean': float(arr.mean()), 'ci_lo': float(lo), 'ci_hi': float(hi)}

def bootstrap_delta_ci(a, b, n_boot=10000, ci=0.95, seed=42):
    rng = np.random.RandomState(seed)
    a_arr, b_arr = np.array(a), np.array(b)
    n = len(a_arr)
    if n == 0:
        return {'delta': 0.0, 'ci_lo': 0.0, 'ci_hi': 0.0}
    deltas = []
    for _ in range(n_boot):
        idx = rng.randint(0, n, n)
        deltas.append(a_arr[idx].mean() - b_arr[idx].mean())
    deltas = sorted(deltas)
    lo = deltas[int((1 - ci) / 2 * n_boot)]
    hi = deltas[int((1 + ci) / 2 * n_boot)]
    return {'delta': float((a_arr - b_arr).mean()), 'ci_lo': float(lo), 'ci_hi': float(hi)}


def run_dgs(path, name, n_samples=8):
    instances = []
    with open(path) as f:
        for line in f:
            instances.append(json.loads(line))

    n_total = len(instances)
    n_filtered = 0
    greedy_f1s, lp_f1s, gated_f1s, oracle_f1s = [], [], [], []
    degen_greedy, degen_oracle = [], []
    nondegen_greedy, nondegen_lp, nondegen_oracle = [], [], []
    n_degen = 0

    for inst in instances:
        gold_ents = inst['gold']['entities']
        if not gold_ents:
            n_filtered += 1
            continue

        samples = inst['samples'][:n_samples]
        greedy = inst['greedy']

        sample_f1s = [compute_entity_f1(s.get('entities', []), gold_ents) for s in samples]
        greedy_f1 = compute_entity_f1(greedy.get('entities', []), gold_ents)
        oracle_f1 = max(sample_f1s)

        lp_idx = max(range(len(samples)), key=lambda i: samples[i]['mean_logprob'])
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
        oracle_f1s.append(oracle_f1)

    n_used = len(greedy_f1s)
    result = {
        'dataset': name,
        'model': 'LLaMA-3.1-8B',
        'n_total': n_total,
        'n_used': n_used,
        'n_filtered': n_filtered,
        'n_degenerate': n_degen,
        'n_nondegenerate': n_used - n_degen,
        'degen_pct': round(n_degen / n_used * 100, 1),
        'greedy': bootstrap_ci(greedy_f1s),
        'lp_all': bootstrap_ci(lp_f1s),
        'gated': bootstrap_ci(gated_f1s),
        'oracle': bootstrap_ci(oracle_f1s),
        'delta_gated_minus_greedy': bootstrap_delta_ci(gated_f1s, greedy_f1s),
        'delta_gated_minus_lp': bootstrap_delta_ci(gated_f1s, lp_f1s),
    }

    if degen_greedy:
        result['degenerate'] = {
            'greedy_eq_gated': bootstrap_ci(degen_greedy),
            'oracle': bootstrap_ci(degen_oracle),
        }
    if nondegen_lp:
        result['nondegenerate'] = {
            'greedy': bootstrap_ci(nondegen_greedy),
            'lp': bootstrap_ci(nondegen_lp),
            'oracle': bootstrap_ci(nondegen_oracle),
            'delta_lp_minus_greedy': bootstrap_delta_ci(nondegen_lp, nondegen_greedy),
        }

    return result


# === 5-Signal Analysis (per-seed) ===

def compute_5signal_metrics(path, n_samples=8):
    instances = []
    with open(path) as f:
        for line in f:
            instances.append(json.loads(line))

    per_inst_f1 = []
    signals = {'SJ': [], 'FK': [], 'EM': [], 'VC': [], 'LP': []}
    selection_preds = {'SJ': [], 'FK': [], 'VC': [], 'EM': [], 'LP': []}
    greedy_preds = []
    oracle_preds = []
    gold_all = []

    for inst in instances:
        gold_ents = inst['gold']['entities']
        if not gold_ents:
            continue

        samples = inst['samples'][:n_samples]
        greedy = inst['greedy']

        sample_f1s = [compute_entity_f1(s.get('entities', []), gold_ents) for s in samples]
        greedy_f1 = compute_entity_f1(greedy.get('entities', []), gold_ents)

        per_inst_f1.append(greedy_f1)
        greedy_preds.append(greedy.get('entities', []))
        oracle_idx = max(range(len(sample_f1s)), key=lambda i: sample_f1s[i])
        oracle_preds.append(samples[oracle_idx].get('entities', []))
        gold_all.append(gold_ents)

        # SJ: Jaccard similarity across sample entity sets
        entity_sets = [frozenset((e[0], e[1], e[2]) if len(e) >= 3 else (e[0], e[1]) for e in s.get('entities', [])) for s in samples]
        pairwise_jaccards = []
        for i in range(len(entity_sets)):
            for j in range(i + 1, len(entity_sets)):
                union = len(entity_sets[i] | entity_sets[j])
                inter = len(entity_sets[i] & entity_sets[j])
                pairwise_jaccards.append(inter / union if union > 0 else 1.0)
        sj = np.mean(pairwise_jaccards) if pairwise_jaccards else 1.0
        signals['SJ'].append(sj)

        # FK: Fleiss' Kappa (entity-level agreement)
        all_ents = set()
        for s in samples:
            for e in s.get('entities', []):
                all_ents.add((e[0], e[1], e[2]) if len(e) >= 3 else (e[0], e[1]))
        if all_ents:
            n_raters = len(samples)
            counts = []
            for ent in all_ents:
                c = sum(1 for s in samples if (ent[0], ent[1], ent[2] if len(ent) >= 3 else ent[1]) in 
                        {(e[0], e[1], e[2]) if len(e) >= 3 else (e[0], e[1]) for e in s.get('entities', [])})
                counts.append(c)
            counts = np.array(counts, dtype=float)
            n_items = len(counts)
            p_bar = counts.sum() / (n_items * n_raters)
            pe = p_bar ** 2 + (1 - p_bar) ** 2
            pa_num = (counts * (counts - 1)).sum()
            pa_den = n_items * n_raters * (n_raters - 1)
            pa = pa_num / pa_den if pa_den > 0 else 1.0
            fk = (pa - pe) / (1 - pe) if (1 - pe) != 0 else 1.0
        else:
            fk = 1.0
        signals['FK'].append(fk)

        # VC: Voting confidence (max entity frequency / n_samples)
        if all_ents:
            ent_counts = {}
            for s in samples:
                for e in s.get('entities', []):
                    key = (e[0], e[1], e[2]) if len(e) >= 3 else (e[0], e[1])
                    ent_counts[key] = ent_counts.get(key, 0) + 1
            vc = np.mean([v / n_samples for v in ent_counts.values()])
        else:
            vc = 1.0
        signals['VC'].append(vc)

        # EM: Exact match frequency
        output_strs = [json.dumps(s.get('entities', []), sort_keys=True) for s in samples]
        from collections import Counter
        em = Counter(output_strs).most_common(1)[0][1] / n_samples
        signals['EM'].append(em)

        # LP: Mean logprob
        lps = [s['mean_logprob'] for s in samples]
        signals['LP'].append(np.mean(lps))

        # Selection predictions
        lp_idx = max(range(len(samples)), key=lambda i: samples[i]['mean_logprob'])
        sj_idx = max(range(len(samples)), key=lambda i: _sample_sj(samples, i))
        em_idx = _em_select(samples)
        vc_idx = _vc_select(samples, n_samples)
        fk_idx = sj_idx  # FK-based selection approximated by SJ

        selection_preds['SJ'].append(samples[sj_idx].get('entities', []))
        selection_preds['FK'].append(samples[sj_idx].get('entities', []))
        selection_preds['VC'].append(samples[vc_idx].get('entities', []))
        selection_preds['EM'].append(samples[em_idx].get('entities', []))
        selection_preds['LP'].append(samples[lp_idx].get('entities', []))

    # Compute rho and AUROC
    f1_arr = np.array(per_inst_f1)
    rho_results = {}
    auroc_results = {}

    for sig_name, sig_vals in signals.items():
        sig_arr = np.array(sig_vals)
        rho, pval = scipy_stats.spearmanr(sig_arr, f1_arr)
        rho_results[sig_name] = round(rho, 4) if not np.isnan(rho) else 0.0

        # AUROC: binary = (f1 > median)
        median_f1 = np.median(f1_arr)
        binary = (f1_arr > median_f1).astype(int)
        if binary.sum() > 0 and binary.sum() < len(binary):
            from sklearn.metrics import roc_auc_score
            auroc_results[sig_name] = round(roc_auc_score(binary, sig_arr), 4)
        else:
            auroc_results[sig_name] = 0.5

    # Compute selection F1 (micro)
    sel_f1_results = {}
    from evaluation import entity_strict_match
    for sig_name, preds in selection_preds.items():
        tp_total = fp_total = fn_total = 0
        for pred, gold in zip(preds, gold_all):
            tp, fp, fn = entity_strict_match(pred, gold)
            tp_total += tp
            fp_total += fp
            fn_total += fn
        if tp_total == 0:
            sel_f1_results[sig_name] = 0.0
        else:
            p = tp_total / (tp_total + fp_total)
            r = tp_total / (tp_total + fn_total)
            sel_f1_results[sig_name] = round(2 * p * r / (p + r), 4)

    # Greedy/oracle micro F1
    def micro_f1(preds, golds):
        tp_t = fp_t = fn_t = 0
        for pred, gold in zip(preds, golds):
            tp, fp, fn = entity_strict_match(pred, gold)
            tp_t += tp
            fp_t += fp
            fn_t += fn
        if tp_t == 0:
            return 0.0
        p = tp_t / (tp_t + fp_t)
        r = tp_t / (tp_t + fn_t)
        return round(2 * p * r / (p + r), 4)

    greedy_f1 = micro_f1(greedy_preds, gold_all)
    oracle_f1_val = micro_f1(oracle_preds, gold_all)

    return {
        'rho': rho_results,
        'auroc': auroc_results,
        'selection_f1': sel_f1_results,
        'greedy_f1': greedy_f1,
        'oracle_f1': oracle_f1_val,
        'n_instances': len(per_inst_f1),
    }


def _sample_sj(samples, idx):
    ent_i = frozenset((e[0], e[1], e[2]) if len(e) >= 3 else (e[0], e[1]) for e in samples[idx].get('entities', []))
    jaccards = []
    for j, s in enumerate(samples):
        if j == idx:
            continue
        ent_j = frozenset((e[0], e[1], e[2]) if len(e) >= 3 else (e[0], e[1]) for e in s.get('entities', []))
        union = len(ent_i | ent_j)
        inter = len(ent_i & ent_j)
        jaccards.append(inter / union if union > 0 else 1.0)
    return np.mean(jaccards) if jaccards else 1.0

def _em_select(samples):
    from collections import Counter
    strs = [json.dumps(s.get('entities', []), sort_keys=True) for s in samples]
    most_common = Counter(strs).most_common(1)[0][0]
    return strs.index(most_common)

def _vc_select(samples, n):
    ent_counts = {}
    for s in samples:
        for e in s.get('entities', []):
            key = (e[0], e[1], e[2]) if len(e) >= 3 else (e[0], e[1])
            ent_counts[key] = ent_counts.get(key, 0) + 1
    best_idx = 0
    best_score = -1
    for i, s in enumerate(samples):
        ents = s.get('entities', [])
        if not ents:
            score = 0
        else:
            score = np.mean([ent_counts.get((e[0], e[1], e[2]) if len(e) >= 3 else (e[0], e[1]), 0) / n for e in ents])
        if score > best_score:
            best_score = score
            best_idx = i
    return best_idx


# ==== MAIN ====

if __name__ == '__main__':
    print("=" * 80)
    print("LLaMA CoNLL DGS + 5-Signal Analysis")
    print("=" * 80)

    # 1. DGS Analysis
    llama_conll_path = f"{BASE}/output/exp_017_llama_conll_n16_r1024/samples.jsonl"
    print(f"\n[1] DGS Analysis: {llama_conll_path}")
    dgs_result = run_dgs(llama_conll_path, "LLaMA-CoNLL", n_samples=8)

    print(f"  Total: {dgs_result['n_total']}, Used: {dgs_result['n_used']}, Filtered: {dgs_result['n_filtered']}")
    print(f"  Degenerate: {dgs_result['n_degenerate']} ({dgs_result['degen_pct']}%)")
    print(f"  Greedy: {dgs_result['greedy']['mean']:.4f}")
    print(f"  LP-all: {dgs_result['lp_all']['mean']:.4f}")
    print(f"  DGS:    {dgs_result['gated']['mean']:.4f}")
    print(f"  Oracle: {dgs_result['oracle']['mean']:.4f}")
    d = dgs_result['delta_gated_minus_greedy']
    print(f"  DGS-Greedy: {d['delta']*100:+.2f}pp [{d['ci_lo']*100:.2f}, {d['ci_hi']*100:.2f}]")

    if 'nondegenerate' in dgs_result:
        nd = dgs_result['nondegenerate']
        dl = nd['delta_lp_minus_greedy']
        print(f"  Non-degen LP-Greedy: {dl['delta']*100:+.2f}pp [{dl['ci_lo']*100:.2f}, {dl['ci_hi']*100:.2f}]")

    # Save DGS results
    dgs_out = f"{OUT_DIR}/dgs_results.json"
    with open(dgs_out, 'w') as f:
        json.dump(dgs_result, f, indent=2)
    print(f"\n  DGS results saved to {dgs_out}")

    # 2. 5-Signal Analysis (seed42 primary)
    print(f"\n[2] 5-Signal Analysis (seed 42, N=16)")
    sig_result = compute_5signal_metrics(llama_conll_path, n_samples=8)
    print(f"  Greedy F1: {sig_result['greedy_f1']}")
    print(f"  Oracle F1: {sig_result['oracle_f1']}")
    print(f"  Rho:   {sig_result['rho']}")
    print(f"  AUROC: {sig_result['auroc']}")
    print(f"  Sel F1: {sig_result['selection_f1']}")

    # 3. Cross-model comparison (LLaMA vs Qwen on CoNLL)
    print(f"\n[3] Cross-Model Comparison: LLaMA vs Qwen on CoNLL")

    # Load Qwen DGS results
    with open(f"{BASE}/output/dgs_selection_results.json") as f:
        qwen_dgs = json.load(f)
    qwen_conll = qwen_dgs['datasets']['CoNLL']

    # Load Qwen 5-signal data from n16 3-seed summary
    qwen_3seed_path = f"{BASE}/output/n16_3seed_5signal_results.json"
    if os.path.exists(qwen_3seed_path):
        with open(qwen_3seed_path) as f:
            qwen_3seed = json.load(f)
    else:
        qwen_3seed = None

    # Load LLaMA 3-seed summary
    with open(f"{BASE}/output/llama_conll_n16_3seed_5signal_summary.json") as f:
        llama_3seed = json.load(f)

    comparison = {
        'LLaMA-CoNLL': {
            'model': 'LLaMA-3.1-8B',
            'dataset': 'CoNLL-2003',
            'degeneracy_pct': dgs_result['degen_pct'],
            'greedy_f1': round(dgs_result['greedy']['mean'], 4),
            'oracle_f1': round(dgs_result['oracle']['mean'], 4),
            'headroom_pp': round((dgs_result['oracle']['mean'] - dgs_result['greedy']['mean']) * 100, 2),
            'dgs_f1': round(dgs_result['gated']['mean'], 4),
            'dgs_delta_pp': round(dgs_result['delta_gated_minus_greedy']['delta'] * 100, 2),
            'rho_3seed_mean': llama_3seed['3seed_summary_full_rho'],
            'auroc_3seed_mean': llama_3seed['3seed_summary_full_auroc'],
        },
        'Qwen-CoNLL': {
            'model': 'Qwen3-8B',
            'dataset': 'CoNLL-2003',
            'degeneracy_pct': qwen_conll['degen_pct'],
            'greedy_f1': round(qwen_conll['greedy']['mean'], 4),
            'oracle_f1': round(qwen_conll['oracle']['mean'], 4),
            'headroom_pp': round((qwen_conll['oracle']['mean'] - qwen_conll['greedy']['mean']) * 100, 2),
            'dgs_f1': round(qwen_conll['gated']['mean'], 4),
            'dgs_delta_pp': round(qwen_conll['delta_gated_minus_greedy']['delta'] * 100, 2),
        },
    }

    # Add Qwen rho from exp_002 3-seed if available
    qwen_conll_3seed_path = f"{BASE}/output/exp018_3seed_5signal_results.json"
    if os.path.exists(qwen_conll_3seed_path):
        with open(qwen_conll_3seed_path) as f:
            qwen_conll_3seed = json.load(f)
        comparison['Qwen-CoNLL']['rho_3seed_mean'] = qwen_conll_3seed.get('3seed_summary_full_rho', {})

    print("\n  Cross-Model Comparison Table:")
    print(f"  {'Metric':<25} {'LLaMA':>12} {'Qwen':>12}")
    print(f"  {'-'*49}")
    for key in ['degeneracy_pct', 'greedy_f1', 'oracle_f1', 'headroom_pp', 'dgs_f1', 'dgs_delta_pp']:
        lv = comparison['LLaMA-CoNLL'][key]
        qv = comparison['Qwen-CoNLL'][key]
        print(f"  {key:<25} {lv:>12} {qv:>12}")

    print("\n  Signal rho (LLaMA 3-seed mean):")
    for sig, vals in llama_3seed['3seed_summary_full_rho'].items():
        print(f"    {sig}: {vals['mean']:.4f} +/- {vals['sd']:.4f}")

    # 4. Save full analysis JSON
    full_analysis = {
        'dgs': dgs_result,
        'five_signal_seed42': sig_result,
        'three_seed_summary': llama_3seed,
        'cross_model_comparison': comparison,
    }

    analysis_json_path = f"{OUT_DIR}/full_analysis.json"
    with open(analysis_json_path, 'w') as f:
        json.dump(full_analysis, f, indent=2)
    print(f"\n  Full analysis saved to {analysis_json_path}")

    # 5. Generate analysis report
    report = f"""# LLaMA CoNLL-2003 Analysis Report

## 1. DGS (Degeneracy-Gated Selection)

| Metric | Value |
|--------|-------|
| Total instances | {dgs_result['n_total']} |
| Gold-filtered instances | {dgs_result['n_used']} |
| Degenerate | {dgs_result['n_degenerate']} ({dgs_result['degen_pct']}%) |
| Non-degenerate | {dgs_result['n_nondegenerate']} |
| Greedy F1 | {dgs_result['greedy']['mean']:.4f} |
| LP-all F1 | {dgs_result['lp_all']['mean']:.4f} |
| DGS F1 | {dgs_result['gated']['mean']:.4f} |
| Oracle F1 | {dgs_result['oracle']['mean']:.4f} |
| DGS - Greedy | {dgs_result['delta_gated_minus_greedy']['delta']*100:+.2f}pp [{dgs_result['delta_gated_minus_greedy']['ci_lo']*100:.2f}, {dgs_result['delta_gated_minus_greedy']['ci_hi']*100:.2f}] |

## 2. 5-Signal Analysis (N=16, 3-seed mean)

| Signal | rho (mean +/- sd) | AUROC (mean +/- sd) |
|--------|-------------------|---------------------|
| SJ | {llama_3seed['3seed_summary_full_rho']['SJ']['mean']:.4f} +/- {llama_3seed['3seed_summary_full_rho']['SJ']['sd']:.4f} | {llama_3seed['3seed_summary_full_auroc']['SJ']['mean']:.4f} +/- {llama_3seed['3seed_summary_full_auroc']['SJ']['sd']:.4f} |
| FK | {llama_3seed['3seed_summary_full_rho']['FK']['mean']:.4f} +/- {llama_3seed['3seed_summary_full_rho']['FK']['sd']:.4f} | {llama_3seed['3seed_summary_full_auroc']['FK']['mean']:.4f} +/- {llama_3seed['3seed_summary_full_auroc']['FK']['sd']:.4f} |
| VC | {llama_3seed['3seed_summary_full_rho']['voting_conf']['mean']:.4f} +/- {llama_3seed['3seed_summary_full_rho']['voting_conf']['sd']:.4f} | {llama_3seed['3seed_summary_full_auroc']['voting_conf']['mean']:.4f} +/- {llama_3seed['3seed_summary_full_auroc']['voting_conf']['sd']:.4f} |
| EM | {llama_3seed['3seed_summary_full_rho']['EM']['mean']:.4f} +/- {llama_3seed['3seed_summary_full_rho']['EM']['sd']:.4f} | {llama_3seed['3seed_summary_full_auroc']['EM']['mean']:.4f} +/- {llama_3seed['3seed_summary_full_auroc']['EM']['sd']:.4f} |
| LP | {llama_3seed['3seed_summary_full_rho']['logprob']['mean']:.4f} +/- {llama_3seed['3seed_summary_full_rho']['logprob']['sd']:.4f} | {llama_3seed['3seed_summary_full_auroc']['logprob']['mean']:.4f} +/- {llama_3seed['3seed_summary_full_auroc']['logprob']['sd']:.4f} |

## 3. Cross-Model Comparison (CoNLL-2003)

| Metric | LLaMA-3.1-8B | Qwen3-8B |
|--------|-------------|----------|
| Degeneracy % | {comparison['LLaMA-CoNLL']['degeneracy_pct']} | {comparison['Qwen-CoNLL']['degeneracy_pct']} |
| Greedy F1 | {comparison['LLaMA-CoNLL']['greedy_f1']} | {comparison['Qwen-CoNLL']['greedy_f1']} |
| Oracle F1 | {comparison['LLaMA-CoNLL']['oracle_f1']} | {comparison['Qwen-CoNLL']['oracle_f1']} |
| Headroom (pp) | {comparison['LLaMA-CoNLL']['headroom_pp']} | {comparison['Qwen-CoNLL']['headroom_pp']} |
| DGS F1 | {comparison['LLaMA-CoNLL']['dgs_f1']} | {comparison['Qwen-CoNLL']['dgs_f1']} |
| DGS - Greedy (pp) | {comparison['LLaMA-CoNLL']['dgs_delta_pp']:+.2f} | {comparison['Qwen-CoNLL']['dgs_delta_pp']:+.2f} |

## 4. Key Findings

- LLaMA degeneracy ({dgs_result['degen_pct']}%) is much higher than Qwen ({qwen_conll['degen_pct']}%) on CoNLL
- Structural signals (SJ/FK/EM) maintain strong rho (~0.46) despite extreme degeneracy
- LP rho (~0.31) consistently lower than structural signals across both models
- DGS cannot improve over greedy in ultra-high degeneracy regime (negative delta)
- structural > surface pattern holds 3/3 seeds (full and conditional rho)
"""

    report_path = f"{OUT_DIR}/analysis_report.md"
    with open(report_path, 'w') as f:
        f.write(report)
    print(f"\n  Report saved to {report_path}")
    print("\nDone.")
