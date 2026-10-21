"""Degeneracy Filtering + Entity Construction analysis."""

import json
import sys
from collections import defaultdict

def entity_set_from_list(entities):
    return frozenset((e["start"], e["end"], e["type"]) for e in entities)

def is_degenerate(samples):
    sets = [entity_set_from_list(s.get("entities", [])) for s in samples]
    return all(s == sets[0] for s in sets[1:])

def entity_construction(samples, threshold=0.5):
    entity_counts = defaultdict(int)
    N = len(samples)
    for s in samples:
        for e in s.get("entities", []):
            entity_counts[(e["start"], e["end"], e["type"])] += 1
    return frozenset(k for k, c in entity_counts.items() if c / N >= threshold)

def micro_f1(pred_sets, gold_sets):
    tp_total, pred_total, gold_total = 0, 0, 0
    for pred, gold in zip(pred_sets, gold_sets):
        tp_total += len(pred & gold)
        pred_total += len(pred)
        gold_total += len(gold)
    if pred_total == 0 and gold_total == 0:
        return 1.0
    if pred_total == 0 or gold_total == 0:
        return 0.0
    p = tp_total / pred_total
    r = tp_total / gold_total
    if p + r == 0:
        return 0.0
    return 2 * p * r / (p + r)

def analyze_dataset(path, name):
    instances = []
    with open(path) as f:
        for line in f:
            if not line.strip():
                continue
            instances.append(json.loads(line))

    n_total = len(instances)
    deg_idx, nondeg_idx = [], []

    for i, inst in enumerate(instances):
        if is_degenerate(inst["samples"]):
            deg_idx.append(i)
        else:
            nondeg_idx.append(i)

    n_deg = len(deg_idx)
    n_nondeg = len(nondeg_idx)

    golds, greedys, constructions = [], [], []
    for inst in instances:
        gold = entity_set_from_list(inst["gold"].get("entities", []))
        greedy = entity_set_from_list(inst["samples"][0].get("entities", []))
        constr = entity_construction(inst["samples"], threshold=0.5)
        golds.append(gold)
        greedys.append(greedy)
        constructions.append(constr)

    deg_consistent = True
    for i in deg_idx:
        if constructions[i] != greedys[i]:
            deg_consistent = False
            break

    full_greedy_f1 = micro_f1(greedys, golds)
    full_constr_f1 = micro_f1(constructions, golds)
    full_delta = (full_constr_f1 - full_greedy_f1) * 100

    if nondeg_idx:
        nd_golds = [golds[i] for i in nondeg_idx]
        nd_greedys = [greedys[i] for i in nondeg_idx]
        nd_constrs = [constructions[i] for i in nondeg_idx]
        nd_greedy_f1 = micro_f1(nd_greedys, nd_golds)
        nd_constr_f1 = micro_f1(nd_constrs, nd_golds)
        nd_delta = (nd_constr_f1 - nd_greedy_f1) * 100
    else:
        nd_greedy_f1 = nd_constr_f1 = nd_delta = 0.0

    if deg_idx:
        d_golds = [golds[i] for i in deg_idx]
        d_greedys = [greedys[i] for i in deg_idx]
        d_constrs = [constructions[i] for i in deg_idx]
        d_greedy_f1 = micro_f1(d_greedys, d_golds)
        d_constr_f1 = micro_f1(d_constrs, d_golds)
        d_delta = (d_constr_f1 - d_greedy_f1) * 100
    else:
        d_greedy_f1 = d_constr_f1 = d_delta = 0.0

    return {
        "dataset": name,
        "n_total": n_total,
        "n_deg": n_deg,
        "n_nondeg": n_nondeg,
        "full_greedy_f1": full_greedy_f1,
        "full_constr_f1": full_constr_f1,
        "full_delta_pp": full_delta,
        "nondeg_greedy_f1": nd_greedy_f1,
        "nondeg_constr_f1": nd_constr_f1,
        "nondeg_delta_pp": nd_delta,
        "deg_greedy_f1": d_greedy_f1,
        "deg_constr_f1": d_constr_f1,
        "deg_delta_pp": d_delta,
        "deg_consistent": deg_consistent,
    }

def main():
    datasets = {
        "SciERC": "output/scierc_mf4v2_seed42/samples.jsonl",
        "CoNLL": "output/conll_mf4v2_seed42/samples.jsonl",
        "FewNERD": "output/fewnerd_mf4v2_seed42_v3/samples.jsonl",
    }

    results = []
    for name, path in datasets.items():
        try:
            r = analyze_dataset(path, name)
            results.append(r)
        except FileNotFoundError:
            print(f"SKIP {name}: {path} not found")

    if not results:
        print("No datasets found")
        sys.exit(1)

    print()
    hdr = f"{'Dataset':<10} {'n_total':>7} {'n_nondeg':>8} {'n_deg':>6} {'Full_d(pp)':>10} {'NonDeg_d(pp)':>12} {'Deg_d(pp)':>10} {'Consistent':>10}"
    print(hdr)
    print("-" * len(hdr))
    for r in results:
        print(f"{r['dataset']:<10} {r['n_total']:>7} {r['n_nondeg']:>8} {r['n_deg']:>6} "
              f"{r['full_delta_pp']:>+10.2f} {r['nondeg_delta_pp']:>+12.2f} "
              f"{r['deg_delta_pp']:>+10.2f} {'Yes' if r['deg_consistent'] else 'NO':>10}")

    print()
    for r in results:
        print(f"\n--- {r['dataset']} ---")
        print(f"  Total: {r['n_total']}  NonDeg: {r['n_nondeg']}  Deg: {r['n_deg']} ({r['n_deg']/r['n_total']*100:.1f}%)")
        print(f"  Full:   Greedy={r['full_greedy_f1']:.4f}  Constr={r['full_constr_f1']:.4f}  d={r['full_delta_pp']:+.2f}pp")
        print(f"  NonDeg: Greedy={r['nondeg_greedy_f1']:.4f}  Constr={r['nondeg_constr_f1']:.4f}  d={r['nondeg_delta_pp']:+.2f}pp")
        print(f"  Deg:    Greedy={r['deg_greedy_f1']:.4f}  Constr={r['deg_constr_f1']:.4f}  d={r['deg_delta_pp']:+.2f}pp")
        print(f"  Deg construction == greedy: {'Yes' if r['deg_consistent'] else 'NO'}")

    print("\n\n--- JSON ---")
    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    main()
