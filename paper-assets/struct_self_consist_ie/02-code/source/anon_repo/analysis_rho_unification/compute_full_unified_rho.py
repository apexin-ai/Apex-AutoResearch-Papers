#!/usr/bin/env python3
"""Compute unified gold-filtered rho for ALL experiments (N=8 + N=16, all seeds)."""
import json, sys
import numpy as np
from collections import Counter
from scipy.stats import spearmanr, rankdata

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from consistency import fleiss_kappa_surface, structural_consistency_soft_jaccard
from evaluation import per_instance_f1

BASE = "/root/autodl-tmp/struct_self_consist_ie/output"

EXPERIMENTS = {
    # === N=16 LLaMA CoNLL (r1024) ===
    "llama_conll_n16_seed42": {
        "path": f"{BASE}/exp_017_llama_conll_n16_r1024/samples.jsonl",
        "subtask": "ner", "model": "llama", "dataset": "conll", "N": 16, "seed": 42,
    },
    "llama_conll_n16_seed123": {
        "path": f"{BASE}/exp_017_llama_conll_n16_s123_r1024/samples.jsonl",
        "subtask": "ner", "model": "llama", "dataset": "conll", "N": 16, "seed": 123,
    },
    "llama_conll_n16_seed456": {
        "path": f"{BASE}/exp_017_llama_conll_n16_s456_r1024/samples.jsonl",
        "subtask": "ner", "model": "llama", "dataset": "conll", "N": 16, "seed": 456,
    },
    # === N=16 Qwen SciERC (joint: NER + RE) ===
    "qwen_scierc_n16_seed42": {
        "path": f"{BASE}/exp001_n16_seed42/samples.jsonl",
        "subtask": "joint", "model": "qwen", "dataset": "scierc", "N": 16, "seed": 42,
    },
    "qwen_scierc_n16_seed123": {
        "path": f"{BASE}/exp001_n16_seed123/samples.jsonl",
        "subtask": "joint", "model": "qwen", "dataset": "scierc", "N": 16, "seed": 123,
    },
    "qwen_scierc_n16_seed456": {
        "path": f"{BASE}/exp001_n16_seed456/samples.jsonl",
        "subtask": "joint", "model": "qwen", "dataset": "scierc", "N": 16, "seed": 456,
    },
    # === N=8 experiments ===
    "llama_conll_n8_seed42": {
        "path": f"{BASE}/exp_017_llama_conll_infer/samples.jsonl",
        "subtask": "ner", "model": "llama", "dataset": "conll", "N": 8, "seed": 42,
    },
    "qwen_conll_n8_seed42": {
        "path": f"{BASE}/exp002_conll2003/samples.jsonl",
        "subtask": "ner", "model": "qwen", "dataset": "conll", "N": 8, "seed": 42,
    },
    "llama_scierc_n8_seed42": {
        "path": f"{BASE}/exp007_llama_inference/samples.jsonl",
        "subtask": "ner", "model": "llama", "dataset": "scierc", "N": 8, "seed": 42,
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
    if not keys:
        return 0.0
    c = Counter(keys)
    return c.most_common(1)[0][1] / len(samples)


def compute_voting_conf(samples, subtask):
    N = len(samples)
    if N == 0:
        return 0.0
    counter = Counter()
    if subtask in ("ner", "joint"):
        for s in samples:
            for e in s.get("entities", []):
                counter[(e["text"], e["type"])] += 1
    else:
        for s in samples:
            for r in s.get("relations", []):
                counter[(r["head"], r["tail"], r["type"])] += 1
    if not counter:
        return 0.0
    return float(np.mean([v / N for v in counter.values()]))


def compute_mean_logprob(samples):
    lps = [s.get("mean_logprob") for s in samples if s.get("mean_logprob") is not None]
    lps = [lp for lp in lps if np.isfinite(lp)]
    return float(np.mean(lps)) if lps else float("nan")


def safe_spearman(x, y):
    x, y = np.asarray(x, float), np.asarray(y, float)
    m = np.isfinite(x) & np.isfinite(y)
    x, y = x[m], y[m]
    if len(x) < 3:
        return float("nan")
    return float(spearmanr(x, y).statistic)


def safe_auroc(scores, labels):
    scores, labels = np.asarray(scores, float), np.asarray(labels, int)
    if len(np.unique(labels)) < 2:
        return float("nan")
    n_pos, n_neg = (labels == 1).sum(), (labels == 0).sum()
    if n_pos == 0 or n_neg == 0:
        return float("nan")
    ranks = rankdata(scores)
    u = ranks[labels == 1].sum() - n_pos * (n_pos + 1) / 2
    return float(u / (n_pos * n_neg))


def analyze_experiment(exp_id, config):
    data = load_data(config["path"])
    subtask = config["subtask"]
    ner_subtask = "ner"  # FK/SJ/F1 always use "ner" even for joint
    entity_key = "entities"

    n_total = len(data)
    valid = [d for d in data if len(d["gold"].get(entity_key, [])) > 0]
    n_gold_empty = n_total - len(valid)
    n_valid = len(valid)

    fk_scores, sj_scores, vc_scores, em_scores, lp_scores, f1_scores = [], [], [], [], [], []

    for d in valid:
        samples = d["samples"]
        greedy = d.get("greedy", samples[0])
        fk_scores.append(fleiss_kappa_surface(samples, subtask=ner_subtask))
        sj_scores.append(structural_consistency_soft_jaccard(samples, subtask=ner_subtask))
        vc_scores.append(compute_voting_conf(samples, ner_subtask))
        em_scores.append(compute_exact_match_rate(samples, ner_subtask))
        lp_scores.append(compute_mean_logprob(samples))
        f1_scores.append(per_instance_f1(greedy, d["gold"], subtask=ner_subtask))

    f1_arr = np.array(f1_scores)
    binary = (f1_arr >= 1.0).astype(int)

    signals = {
        "VC": np.array(vc_scores),
        "SJ": np.array(sj_scores),
        "FK": np.array(fk_scores),
        "EM": np.array(em_scores),
        "LP": np.array(lp_scores),
    }

    result = {
        "n_instances": n_valid,
        "n_total": n_total,
        "n_gold_empty": n_gold_empty,
    }
    for name, vals in signals.items():
        result[name] = round(safe_spearman(vals, f1_arr), 4)
    for name, vals in signals.items():
        result[f"auroc_{name}"] = round(safe_auroc(vals, binary), 4)

    # RE metrics for joint subtask
    if subtask == "joint":
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


if __name__ == "__main__":
    all_results = {}
    for exp_id, config in EXPERIMENTS.items():
        print(f"Processing {exp_id}...")
        try:
            result = analyze_experiment(exp_id, config)
            all_results[exp_id] = result
            rho_str = ", ".join(f"{k}={result[k]}" for k in ["VC","SJ","FK","EM","LP"])
            print(f"  n={result['n_instances']}, {rho_str}")
            if "re_FK" in result:
                print(f"  RE: n={result['re_n_valid']}, FK={result['re_FK']}, SJ={result['re_SJ']}")
        except Exception as e:
            print(f"  ERROR: {e}")
            import traceback; traceback.print_exc()
            all_results[exp_id] = {"error": str(e)}

    # Sanity check against existing rho_audit values
    sanity = {}
    ref = {
        "llama_conll_n16_seed42": {"FK": 0.4752, "SJ": 0.4836, "VC": 0.4746, "EM": 0.4818, "LP": 0.3136},
        "llama_conll_n16_seed456": {"FK": 0.469, "SJ": 0.4734, "VC": 0.4722, "EM": 0.4752, "LP": 0.3099},
        "qwen_scierc_n16_seed456": {"FK": 0.2723, "SJ": 0.4098, "VC": 0.4449, "EM": 0.3363, "LP": 0.2415},
    }
    all_ok = True
    for key, expected in ref.items():
        if key in all_results and "error" not in all_results[key]:
            for sig, exp_val in expected.items():
                got = all_results[key][sig]
                match = abs(got - exp_val) < 0.0005
                if not match:
                    all_ok = False
                sanity[f"{key}.{sig}"] = {"expected": exp_val, "got": got, "match": match}

    # Compare with n8_5signal_results.json
    n8_ref = {}
    try:
        with open(f"{BASE}/n8_5signal_results.json") as f:
            n8_data = json.load(f)
        n8_map = {
            "qwen_conll_n8_seed42": ("exp_002_conll_n8", {"SJ": "SJ", "FK": "FK", "EM": "EM", "LP": "logprob", "VC": "voting_conf"}),
            "llama_scierc_n8_seed42": ("exp_007_llama_n8", {"SJ": "SJ", "FK": "FK", "EM": "EM", "LP": "logprob", "VC": "voting_conf"}),
        }
        for my_key, (n8_key, sig_map) in n8_map.items():
            if n8_key in n8_data and my_key in all_results and "error" not in all_results[my_key]:
                for my_sig, n8_sig in sig_map.items():
                    expected = n8_data[n8_key]["full"][n8_sig]["rho"]
                    got = all_results[my_key][my_sig]
                    match = abs(got - expected) < 0.0005
                    n8_ref[f"{my_key}.{my_sig}"] = {"expected": expected, "got": got, "match": match}
                    if not match:
                        all_ok = False
    except Exception:
        pass

    output = {
        "metadata": {
            "pipeline": "unified_gold_filtered",
            "date": "2026-05-15",
            "fk_empty_fix": True,
            "gold_filter": "exclude instances where len(gold.entities)==0",
            "conll_n_valid": 2756,
            "scierc_n_valid": 529,
        },
        "results": all_results,
        "sanity_check_vs_rho_audit": sanity,
        "sanity_check_vs_n8_5signal": n8_ref,
    }

    out_path = f"{BASE}/analysis_unified_rho_full.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, default=lambda o: None if (isinstance(o, float) and np.isnan(o)) else float(o) if isinstance(o, (np.floating,)) else o)

    import shutil
    shutil.copy(out_path, "/root/autodl-tmp/struct_self_consist_ie/analysis_rho_unification/analysis_unified_rho_full.json")

    print(f"\nSaved to {out_path}")
    print(f"\n=== Sanity check vs rho_audit ===")
    for k, v in sanity.items():
        status = "OK" if v["match"] else "MISMATCH"
        print(f"  {k}: expected={v['expected']}, got={v['got']} [{status}]")
    print(f"\n=== Sanity check vs n8_5signal ===")
    for k, v in n8_ref.items():
        status = "OK" if v["match"] else "MISMATCH"
        print(f"  {k}: expected={v['expected']}, got={v['got']} [{status}]")
