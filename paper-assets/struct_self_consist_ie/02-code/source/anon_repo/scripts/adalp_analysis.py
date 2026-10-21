"""
AdaLP (Adaptive LP Selection) Analysis.
Per-instance degeneracy decides greedy vs LP selection.
Leave-one-dataset-out CV for threshold selection.
"""
import json
import numpy as np
from collections import Counter
from pathlib import Path

N = 8  # number of samples to use

DATA_PATHS = {
    "SciERC": "output/exp_012_logprob/samples_with_logprobs.jsonl",
    "CoNLL": "output/exp_002_conll_n16/samples.jsonl",
    "FewNERD": "output/exp_027_fewnerd_n16/samples.jsonl",
}

TAU_CANDIDATES = [0.25, 0.375, 0.5, 0.625, 0.75]


def compute_ner_f1(pred_entities, gold_entities):
    pred_set = {(e['text'], e['type'], e.get('start', -1), e.get('end', -1))
                for e in pred_entities}
    gold_set = {(e['text'], e['type'], e.get('start', -1), e.get('end', -1))
                for e in gold_entities}
    if not pred_set and not gold_set:
        return 1.0
    if not pred_set or not gold_set:
        return 0.0
    tp = len(pred_set & gold_set)
    prec = tp / len(pred_set)
    rec = tp / len(gold_set)
    if prec + rec == 0:
        return 0.0
    return 2 * prec * rec / (prec + rec)


def load_dataset(path):
    """Load dataset and compute per-instance metrics."""
    instances = []
    with open(path) as f:
        for line in f:
            d = json.loads(line)
            gold_ents = d['gold']['entities']
            samples = d['samples'][:N]
            greedy = d['greedy']

            sample_f1s = [compute_ner_f1(s['entities'], gold_ents) for s in samples]
            sample_lps = [s['mean_logprob'] for s in samples]
            greedy_f1 = compute_ner_f1(greedy['entities'], gold_ents)

            # LP selection: pick sample with highest mean_logprob
            lp_idx = int(np.argmax(sample_lps))
            lp_f1 = sample_f1s[lp_idx]

            # Oracle: best F1 among samples
            oracle_f1 = max(sample_f1s)

            # Degeneracy: max frequency of any F1 value / N
            f1_counts = Counter(sample_f1s)
            degen = max(f1_counts.values()) / len(sample_f1s)

            instances.append({
                'id': d['id'],
                'sample_f1s': sample_f1s,
                'sample_lps': sample_lps,
                'greedy_f1': greedy_f1,
                'lp_f1': lp_f1,
                'oracle_f1': oracle_f1,
                'degen': degen,
            })
    return instances


def adalp_select(instances, tau):
    """Apply AdaLP: if degen > tau, use greedy; else use LP."""
    f1s = []
    for inst in instances:
        if inst['degen'] > tau:
            f1s.append(inst['greedy_f1'])
        else:
            f1s.append(inst['lp_f1'])
    return np.array(f1s)


def mean_f1(instances, key):
    return np.mean([inst[key] for inst in instances])


def paired_bootstrap(scores_a, scores_b, n_iter=1000, seed=42):
    """Paired bootstrap test. Returns delta, 95% CI, p-value."""
    rng = np.random.RandomState(seed)
    n = len(scores_a)
    observed_delta = np.mean(scores_a) - np.mean(scores_b)
    deltas = []
    for _ in range(n_iter):
        idx = rng.randint(0, n, size=n)
        deltas.append(np.mean(scores_a[idx]) - np.mean(scores_b[idx]))
    deltas = np.array(deltas)
    ci_lo = np.percentile(deltas, 2.5)
    ci_hi = np.percentile(deltas, 97.5)
    p_value = np.mean(deltas <= 0) if observed_delta > 0 else np.mean(deltas >= 0)
    return observed_delta, (ci_lo, ci_hi), p_value


def lodo_cv(all_data, tau_candidates):
    """Leave-one-dataset-out cross-validation."""
    dataset_names = list(all_data.keys())
    results = []
    for test_name in dataset_names:
        train_names = [n for n in dataset_names if n != test_name]
        best_tau = None
        best_train_f1 = -1
        for tau in tau_candidates:
            train_f1s = []
            for tn in train_names:
                adalp_scores = adalp_select(all_data[tn], tau)
                train_f1s.append(np.mean(adalp_scores))
            avg_train_f1 = np.mean(train_f1s)
            if avg_train_f1 > best_train_f1:
                best_train_f1 = avg_train_f1
                best_tau = tau
        test_adalp_scores = adalp_select(all_data[test_name], best_tau)
        test_f1 = np.mean(test_adalp_scores)
        results.append({
            'train_sets': train_names,
            'test_set': test_name,
            'best_tau': best_tau,
            'adalp_f1_test': float(test_f1),
        })
    return results


def degeneracy_bin_analysis(instances, tau):
    """Analyze AdaLP behavior by degeneracy bins."""
    bins = [(0, 0, "0"), (0, 0.25, "(0,0.25]"), (0.25, 0.5, "(0.25,0.5]"),
            (0.5, 0.75, "(0.5,0.75]"), (0.75, 1.0, "(0.75,1.0]")]
    results = []
    for lo, hi, label in bins:
        if label == "0":
            subset = [inst for inst in instances if inst['degen'] == 0]
        elif lo == 0 and hi == 0.25:
            subset = [inst for inst in instances if 0 < inst['degen'] <= hi]
        else:
            subset = [inst for inst in instances if lo < inst['degen'] <= hi]
        if not subset:
            results.append({'bin': label, 'count': 0, 'greedy_ratio': 0, 'mean_gain_vs_greedy': 0})
            continue
        n_greedy = sum(1 for inst in subset if inst['degen'] > tau)
        adalp_f1s = []
        greedy_f1s = []
        for inst in subset:
            if inst['degen'] > tau:
                adalp_f1s.append(inst['greedy_f1'])
            else:
                adalp_f1s.append(inst['lp_f1'])
            greedy_f1s.append(inst['greedy_f1'])
        mean_gain = np.mean(np.array(adalp_f1s) - np.array(greedy_f1s))
        results.append({
            'bin': label,
            'count': len(subset),
            'greedy_ratio': n_greedy / len(subset),
            'mean_gain_vs_greedy': float(mean_gain),
        })
    return results


def main():
    base = Path("/root/autodl-tmp/struct_self_consist_ie")

    print("Loading datasets...")
    all_data = {}
    for name, rel_path in DATA_PATHS.items():
        all_data[name] = load_dataset(base / rel_path)
        print(f"  {name}: {len(all_data[name])} instances")

    # Main results per dataset
    print("\n" + "="*90)
    print("MAIN RESULTS (N=8)")
    print("="*90)
    header = f"{'Dataset':<10} {'Greedy F1':>10} {'LP F1':>10} {'AdaLP F1':>10} {'Oracle F1':>10} {'AdaLP-Greedy':>14} {'AdaLP-LP':>10}"
    print(header)
    print("-"*90)

    # First do LODO CV to get per-dataset tau
    cv_results = lodo_cv(all_data, TAU_CANDIDATES)
    cv_tau_map = {r['test_set']: r['best_tau'] for r in cv_results}

    main_results = {}
    for name, instances in all_data.items():
        tau = cv_tau_map[name]
        greedy_scores = np.array([inst['greedy_f1'] for inst in instances])
        lp_scores = np.array([inst['lp_f1'] for inst in instances])
        adalp_scores = adalp_select(instances, tau)
        oracle_scores = np.array([inst['oracle_f1'] for inst in instances])

        g_f1 = np.mean(greedy_scores)
        l_f1 = np.mean(lp_scores)
        a_f1 = np.mean(adalp_scores)
        o_f1 = np.mean(oracle_scores)

        delta_g, ci_g, p_g = paired_bootstrap(adalp_scores, greedy_scores)
        delta_l, ci_l, p_l = paired_bootstrap(adalp_scores, lp_scores)

        print(f"{name:<10} {g_f1:>10.4f} {l_f1:>10.4f} {a_f1:>10.4f} {o_f1:>10.4f} "
              f"{delta_g*100:>+7.2f}pp    {delta_l*100:>+7.2f}pp")

        main_results[name] = {
            'greedy_f1': float(g_f1),
            'lp_f1': float(l_f1),
            'adalp_f1': float(a_f1),
            'oracle_f1': float(o_f1),
            'tau_used': tau,
            'adalp_vs_greedy': {'delta': float(delta_g), 'ci_95': [float(ci_g[0]), float(ci_g[1])], 'p_value': float(p_g)},
            'adalp_vs_lp': {'delta': float(delta_l), 'ci_95': [float(ci_l[0]), float(ci_l[1])], 'p_value': float(p_l)},
        }

    # Cross-validation results
    print("\n" + "="*90)
    print("LEAVE-ONE-DATASET-OUT CROSS-VALIDATION")
    print("="*90)
    print(f"{'Fold':<6} {'Train sets':<25} {'Test set':<10} {'Best tau':>8} {'AdaLP F1 (test)':>16}")
    print("-"*70)
    for i, r in enumerate(cv_results, 1):
        print(f"{i:<6} {str(r['train_sets']):<25} {r['test_set']:<10} {r['best_tau']:>8.3f} {r['adalp_f1_test']:>16.4f}")
    mean_cv_f1 = np.mean([r['adalp_f1_test'] for r in cv_results])
    print(f"\nMean AdaLP F1 across folds: {mean_cv_f1:.4f}")

    # Statistical significance
    print("\n" + "="*90)
    print("STATISTICAL SIGNIFICANCE (paired bootstrap, 1000 iterations)")
    print("="*90)
    for name, instances in all_data.items():
        tau = cv_tau_map[name]
        greedy_scores = np.array([inst['greedy_f1'] for inst in instances])
        lp_scores = np.array([inst['lp_f1'] for inst in instances])
        adalp_scores = adalp_select(instances, tau)

        delta_g, ci_g, p_g = paired_bootstrap(adalp_scores, greedy_scores)
        delta_l, ci_l, p_l = paired_bootstrap(adalp_scores, lp_scores)

        print(f"\n{name} (tau={tau}):")
        print(f"  AdaLP vs Greedy: delta={delta_g*100:+.2f}pp, 95%CI=[{ci_g[0]*100:.2f}, {ci_g[1]*100:.2f}]pp, p={p_g:.4f}")
        print(f"  AdaLP vs LP:     delta={delta_l*100:+.2f}pp, 95%CI=[{ci_l[0]*100:.2f}, {ci_l[1]*100:.2f}]pp, p={p_l:.4f}")

    # Degeneracy bin analysis
    print("\n" + "="*90)
    print("DEGENERACY BIN ANALYSIS")
    print("="*90)
    for name, instances in all_data.items():
        tau = cv_tau_map[name]
        bins = degeneracy_bin_analysis(instances, tau)
        print(f"\n{name} (tau={tau}):")
        print(f"  {'Bin':<12} {'Count':>6} {'Greedy%':>8} {'Gain vs Greedy':>15}")
        for b in bins:
            print(f"  {b['bin']:<12} {b['count']:>6} {b['greedy_ratio']*100:>7.1f}% {b['mean_gain_vs_greedy']*100:>+12.2f}pp")
        main_results[name]['degen_bins'] = bins

    # Save JSON
    output_path = base / "output" / "adalp_analysis_results.json"
    output = {
        'main_results': main_results,
        'cv_results': cv_results,
        'mean_cv_f1': float(mean_cv_f1),
        'tau_candidates': TAU_CANDIDATES,
        'N': N,
    }
    with open(output_path, 'w') as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved to {output_path}")


if __name__ == '__main__':
    main()
