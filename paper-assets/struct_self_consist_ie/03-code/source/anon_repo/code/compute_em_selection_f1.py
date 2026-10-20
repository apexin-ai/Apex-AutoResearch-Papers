"""Compute EM (Exact Match) selection F1 for Qwen SciERC N=8."""

import json
import sys
from collections import Counter

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from evaluation import per_instance_f1

DATA_PATH = "/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples.jsonl"
COMPARISON_PATH = "/root/autodl-tmp/struct_self_consist_ie/output/exp_016_rerun_1024/selection_f1_comparison.json"
FULL_PATH = "/root/autodl-tmp/struct_self_consist_ie/output/exp_016_rerun_1024/selection_f1_full.json"


def load_data(path):
    instances = []
    with open(path) as f:
        for line in f:
            if line.strip():
                instances.append(json.loads(line))
    return instances


def entity_set_key(sample):
    return frozenset((e["text"], e["type"]) for e in sample.get("entities", []))


def relation_set_key(sample):
    return frozenset((r["head"], r["tail"], r["type"]) for r in sample.get("relations", []))


def em_select(samples, key_fn):
    """Select sample by exact-match plurality vote. Tie-break: first occurrence."""
    if not samples:
        return None
    keys = [key_fn(s) for s in samples]
    counter = Counter(keys)
    max_count = counter.most_common(1)[0][1]
    for i, k in enumerate(keys):
        if counter[k] == max_count:
            return samples[i]
    return samples[0]


def compute_em_selection_f1(instances, subtask):
    key_fn = entity_set_key if subtask == "ner" else relation_set_key
    
    em_f1s = []
    greedy_f1s = []
    oracle_f1s = []
    
    for inst in instances:
        gold = inst["gold"]
        samples = inst.get("samples", [])
        greedy = inst.get("greedy")
        
        selected = em_select(samples, key_fn)
        if selected is not None:
            em_f1 = per_instance_f1(selected, gold, subtask)
        else:
            em_f1 = 0.0
        em_f1s.append(em_f1)
        
        if greedy is not None:
            greedy_f1s.append(per_instance_f1(greedy, gold, subtask))
        else:
            greedy_f1s.append(0.0)
        
        if samples:
            best_f1 = max(per_instance_f1(s, gold, subtask) for s in samples)
            oracle_f1s.append(best_f1)
        else:
            oracle_f1s.append(0.0)
    
    return em_f1s, greedy_f1s, oracle_f1s


def sign_test(a_f1s, b_f1s):
    wins = losses = ties = 0
    for a, b in zip(a_f1s, b_f1s):
        if abs(a - b) < 1e-9:
            ties += 1
        elif a > b:
            wins += 1
        else:
            losses += 1
    return wins, losses, ties


def main():
    instances = load_data(DATA_PATH)
    
    # Filter: gold-nonempty (same as exp_016)
    ner_instances = [inst for inst in instances if len(inst["gold"].get("entities", [])) > 0]
    re_instances = [inst for inst in instances if len(inst["gold"].get("relations", [])) > 0]
    
    with open(COMPARISON_PATH) as f:
        comparison = json.load(f)
    with open(FULL_PATH) as f:
        full_data = json.load(f)
    
    print("=" * 70)
    print("Qwen SciERC N=8 — EM Selection F1 (gold-nonempty filter)")
    print("=" * 70)
    
    for subtask, insts in [("ner", ner_instances), ("re", re_instances)]:
        em_f1s, greedy_f1s, oracle_f1s = compute_em_selection_f1(insts, subtask)
        n = len(insts)
        em_mean = sum(em_f1s) / n
        
        comp = comparison[subtask]["summary"]
        comp_n = comparison[subtask]["n"]
        
        print(f"\n{'─' * 50}")
        print(f"{subtask.upper()} (n={n}, expected={comp_n})")
        print(f"{'─' * 50}")
        print(f"{'Method':<20} {'Selection F1':>12}")
        print(f"{'─' * 32}")
        print(f"{'Greedy':<20} {comp['greedy']:>12.4f}")
        print(f"{'Oracle':<20} {comp['oracle']:>12.4f}")
        print(f"{'SJ-Best':<20} {comp['sj_best']:>12.4f}")
        print(f"{'EM-Best':<20} {em_mean:>12.4f}  ← NEW")
        print(f"{'LP-Best':<20} {comp['logprob_best']:>12.4f}")
        print(f"{'Voting-Best':<20} {comp['voting_conf_best']:>12.4f}")
        print(f"{'Ensemble-Best':<20} {comp['ensemble_best']:>12.4f}")
        print(f"{'Random-Avg':<20} {comp['random_avg']:>12.4f}")
        
        # Sign test vs greedy
        wins, losses, ties = sign_test(em_f1s, greedy_f1s)
        print(f"\nSign test (EM vs Greedy):")
        print(f"  Wins={wins}, Losses={losses}, Ties={ties}")
        if (wins + losses) > 0:
            print(f"  Win rate (excl. ties): {wins/(wins+losses)*100:.1f}%")
        
        # Sign test vs other methods
        for method_name, method_key in [("SJ-Best", "sj_best"), ("LP-Best", "logprob_best"), ("Voting-Best", "voting_conf_best")]:
            if method_key in full_data[subtask]["methods"]:
                other_f1s = full_data[subtask]["methods"][method_key]["per_instance"]
                w, l, t = sign_test(em_f1s, other_f1s)
                print(f"\nSign test (EM vs {method_name}):")
                print(f"  Wins={w}, Losses={l}, Ties={t}")
        
        delta = em_mean - comp['greedy']
        print(f"\nΔ(EM - Greedy) = {delta:+.4f}")


if __name__ == "__main__":
    main()
