#!/usr/bin/env python3
"""Task 6: Oracle-Improvable Fraction + Task 7: TOST Equivalence Test."""
import json, os, sys
import numpy as np
from scipy import stats
from collections import Counter

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code/')
from consistency import _ner_soft_jaccard_pair, _re_soft_jaccard_pair
from evaluation import per_instance_f1

CONFIGS = {
    "qwen_scierc_ner": {
        "path": "/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples.jsonl",
        "subtask": "ner",
    },
    "qwen_scierc_re": {
        "path": "/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples.jsonl",
        "subtask": "re",
    },
    "llama_scierc_ner": {
        "path": "/root/autodl-tmp/struct_self_consist_ie/output/exp007_llama_inference/samples.jsonl",
        "subtask": "ner",
    },
    "qwen_conll_ner": {
        "path": "/root/autodl-tmp/struct_self_consist_ie/output/exp002_conll2003/samples.jsonl",
        "subtask": "ner",
    },
    "llama_conll_ner": {
        "path": "/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_infer/samples.jsonl",
        "subtask": "ner",
    },
}

OUTPUT_PATH = "/root/autodl-tmp/struct_self_consist_ie/output/review_round2/oracle_improvable_tost.json"

def load_instances(path):
    with open(path) as f:
        return [json.loads(line.strip()) for line in f if line.strip()]

def filter_gold_nonempty(instances, subtask):
    key = "entities" if subtask == "ner" else "relations"
    return [inst for inst in instances if len(inst["gold"].get(key, [])) > 0]

# ─── Per-sample signal functions (subtask-aware) ───

def per_sample_sj(inst, subtask):
    samples = inst["samples"]
    n = len(samples)
    if n <= 1:
        return [1.0] * n
    pair_fn = _ner_soft_jaccard_pair if subtask == "ner" else _re_soft_jaccard_pair
    item_key = "entities" if subtask == "ner" else "relations"
    scores = []
    for k in range(n):
        sims = []
        for j in range(n):
            if j == k:
                continue
            sims.append(pair_fn(
                samples[k].get(item_key, []),
                samples[j].get(item_key, []),
            ))
        scores.append(float(np.mean(sims)))
    return scores

def per_sample_fk(inst, subtask):
    samples = inst["samples"]
    n = len(samples)
    if n <= 1:
        return [1.0] * n
    if subtask == "ner":
        sample_keys = [{(e["text"], e["type"]) for e in s.get("entities", [])} for s in samples]
    else:
        sample_keys = [{(r["head"], r["tail"], r["type"]) for r in s.get("relations", [])} for s in samples]
    scores = []
    for k in range(n):
        if not sample_keys[k]:
            scores.append(0.0)
            continue
        ent_agr = []
        for ent_key in sample_keys[k]:
            cnt = sum(1 for j in range(n) if j != k and ent_key in sample_keys[j])
            ent_agr.append(cnt / (n - 1))
        scores.append(float(np.mean(ent_agr)))
    return scores

def per_sample_em(inst, subtask):
    samples = inst["samples"]
    n = len(samples)
    if n <= 1:
        return [1.0] * n
    if subtask == "ner":
        sample_sets = [frozenset((e["text"], e["type"], e["start"], e["end"]) for e in s.get("entities", [])) for s in samples]
    else:
        sample_sets = [frozenset((r["head"], r["tail"], r["type"]) for r in s.get("relations", [])) for s in samples]
    return [sum(1 for j in range(n) if j != k and sample_sets[j] == sample_sets[k]) / (n - 1) for k in range(n)]

def per_sample_logprob(inst, subtask):
    lp = inst.get("logprobs")
    if lp is not None:
        return list(lp)
    return [s.get("mean_logprob", 0.0) for s in inst["samples"]]

def per_sample_voting_conf(inst, subtask):
    samples = inst["samples"]
    n = len(samples)
    if n <= 1:
        return [1.0] * n
    counter = Counter()
    if subtask == "ner":
        for s in samples:
            for e in s.get("entities", []):
                counter[(e["text"], e["type"])] += 1
    else:
        for s in samples:
            for r in s.get("relations", []):
                counter[(r["head"], r["tail"], r["type"])] += 1
    majority_set = {k for k, v in counter.items() if v > n / 2}
    scores = []
    for s in samples:
        if subtask == "ner":
            s_keys = {(e["text"], e["type"]) for e in s.get("entities", [])}
        else:
            s_keys = {(r["head"], r["tail"], r["type"]) for r in s.get("relations", [])}
        overlap = len(s_keys & majority_set)
        penalty = len(s_keys - majority_set)
        scores.append(overlap - 0.5 * penalty)
    return scores

SIGNAL_FNS = {
    "sj": per_sample_sj,
    "fk": per_sample_fk,
    "em": per_sample_em,
    "logprob": per_sample_logprob,
    "vc": per_sample_voting_conf,
}

def tost_test(diffs, delta):
    n = len(diffs)
    mean_diff = np.mean(diffs)
    se = np.std(diffs, ddof=1) / np.sqrt(n)
    if se < 1e-15:
        equivalent = abs(mean_diff) < delta
        return {"p_value": 0.0 if equivalent else 1.0, "equivalent": equivalent}
    t_upper = (mean_diff - delta) / se
    p_upper = stats.t.cdf(t_upper, df=n-1)
    t_lower = (mean_diff + delta) / se
    p_lower = 1 - stats.t.cdf(t_lower, df=n-1)
    p_tost = max(p_upper, p_lower)
    return {"p_value": round(float(p_tost), 6), "equivalent": bool(p_tost < 0.05)}

def run_config(name, cfg):
    subtask = cfg["subtask"]
    instances = load_instances(cfg["path"])
    filtered = filter_gold_nonempty(instances, subtask)
    n_valid = len(filtered)
    print(f"\n{'='*60}")
    print(f"  {name} (subtask={subtask}, n_valid={n_valid})")
    print(f"{'='*60}")

    greedy_f1s = []
    oracle_f1s = []
    all_sample_f1s = []
    for inst in filtered:
        gf = per_instance_f1(inst["greedy"], inst["gold"], subtask=subtask)
        greedy_f1s.append(gf)
        sf = [per_instance_f1(s, inst["gold"], subtask=subtask) for s in inst["samples"]]
        all_sample_f1s.append(sf)
        oracle_f1s.append(max(sf) if sf else 0.0)

    greedy_f1s = np.array(greedy_f1s)
    oracle_f1s = np.array(oracle_f1s)

    # Task 6: Oracle-Improvable Fraction
    improvable_mask = oracle_f1s > greedy_f1s + 1e-9
    n_improvable = int(improvable_mask.sum())
    improvable_fraction = float(n_improvable / n_valid) if n_valid > 0 else 0.0
    gains = oracle_f1s[improvable_mask] - greedy_f1s[improvable_mask]
    mean_oracle_gain = float(np.mean(gains)) if len(gains) > 0 else 0.0

    task6 = {
        "n_valid": n_valid,
        "n_improvable": n_improvable,
        "improvable_fraction": round(improvable_fraction, 6),
        "mean_oracle_gain_when_improvable": round(mean_oracle_gain, 6),
        "greedy_f1_mean": round(float(greedy_f1s.mean()), 6),
        "oracle_f1_mean": round(float(oracle_f1s.mean()), 6),
    }
    print(f"  Greedy={greedy_f1s.mean():.4f}  Oracle={oracle_f1s.mean():.4f}")
    print(f"  Improvable: {n_improvable}/{n_valid} = {improvable_fraction:.4f}")
    print(f"  Mean oracle gain (when improvable): {mean_oracle_gain:.4f}")

    # Task 7: TOST for each signal
    task7 = {}
    for sig_name, sig_fn in SIGNAL_FNS.items():
        sel_f1s = []
        for i, inst in enumerate(filtered):
            scores = sig_fn(inst, subtask)
            best_k = int(np.argmax(scores))
            sel_f1s.append(all_sample_f1s[i][best_k])

        sel_f1s = np.array(sel_f1s)
        diffs = sel_f1s - greedy_f1s
        mean_diff = float(np.mean(diffs))

        tost_01 = tost_test(diffs, 0.01)
        tost_02 = tost_test(diffs, 0.02)

        task7[sig_name] = {
            "selection_f1_mean": round(float(sel_f1s.mean()), 6),
            "mean_diff": round(mean_diff, 6),
            "tost_delta_0.01": tost_01,
            "tost_delta_0.02": tost_02,
        }
        eq01 = "YES" if tost_01["equivalent"] else "no"
        eq02 = "YES" if tost_02["equivalent"] else "no"
        print(f"  {sig_name:>8}: sel_F1={sel_f1s.mean():.4f} Δ={mean_diff:+.4f}  "
              f"TOST(δ=.01) p={tost_01['p_value']:.4f} [{eq01}]  "
              f"TOST(δ=.02) p={tost_02['p_value']:.4f} [{eq02}]")

    return task6, task7

def main():
    results = {"task6_oracle_improvable": {}, "task7_tost": {}}
    for name, cfg in CONFIGS.items():
        t6, t7 = run_config(name, cfg)
        results["task6_oracle_improvable"][name] = t6
        results["task7_tost"][name] = t7

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\n\nSaved -> {OUTPUT_PATH}")

    # Summary table
    print(f"\n{'='*100}")
    print("Task 6: Oracle-Improvable Fraction")
    print(f"{'Config':<22} {'n_valid':>8} {'n_impr':>8} {'frac':>8} {'mean_gain':>10} {'greedy':>8} {'oracle':>8}")
    print("-"*100)
    for name, t6 in results["task6_oracle_improvable"].items():
        print(f"{name:<22} {t6['n_valid']:>8} {t6['n_improvable']:>8} "
              f"{t6['improvable_fraction']:>8.4f} {t6['mean_oracle_gain_when_improvable']:>10.4f} "
              f"{t6['greedy_f1_mean']:>8.4f} {t6['oracle_f1_mean']:>8.4f}")

    print(f"\n{'='*100}")
    print("Task 7: TOST Equivalence Test (selection vs greedy)")
    print(f"{'Config':<22} {'signal':>8} {'sel_F1':>8} {'Δ':>8} {'δ=.01 p':>8} {'eq?':>4} {'δ=.02 p':>8} {'eq?':>4}")
    print("-"*100)
    for name, t7 in results["task7_tost"].items():
        for sig, res in t7.items():
            eq01 = "Y" if res["tost_delta_0.01"]["equivalent"] else ""
            eq02 = "Y" if res["tost_delta_0.02"]["equivalent"] else ""
            print(f"{name:<22} {sig:>8} {res['selection_f1_mean']:>8.4f} {res['mean_diff']:>+8.4f} "
                  f"{res['tost_delta_0.01']['p_value']:>8.4f} {eq01:>4} "
                  f"{res['tost_delta_0.02']['p_value']:>8.4f} {eq02:>4}")

if __name__ == "__main__":
    main()
