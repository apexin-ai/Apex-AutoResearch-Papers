#!/usr/bin/env python3
"""B5 Cross-Model Self-Consistency: Qwen3-8B FT + LLaMA-3.1-8B FT.

Compares pure-model vs mixed-model entity construction.
Usage:
    python cross_model_construction.py --qwen <path> --llama <path> --output <path> [--dataset <name>] [--skip-m030]
"""

import argparse
import json
from collections import defaultdict

import numpy as np

B = 10000
SEED = 42


def compute_entity_f1(pred_entities, gold_entities):
    pred = {(e["start"], e["end"], e["type"]) for e in pred_entities}
    gold = {(e["start"], e["end"], e["type"]) for e in gold_entities}
    if not gold and not pred:
        return 1.0
    if not gold or not pred:
        return 0.0
    tp = len(pred & gold)
    if tp == 0:
        return 0.0
    p = tp / len(pred)
    r = tp / len(gold)
    return 2 * p * r / (p + r)


def compute_vc(samples):
    N = len(samples)
    entity_sets = []
    for s in samples:
        es = frozenset((e["start"], e["end"], e["type"]) for e in s.get("entities", []))
        entity_sets.append(es)
    return [sum(1 for j in range(N) if entity_sets[j] == entity_sets[i]) / N for i in range(N)]


def uniform_construct(samples, threshold):
    N = len(samples)
    entity_vote = defaultdict(int)
    for s in samples:
        seen = set()
        for e in s.get("entities", []):
            key = (e["start"], e["end"], e["type"])
            if key not in seen:
                entity_vote[key] += 1
                seen.add(key)
    consensus = []
    for key, count in entity_vote.items():
        if count / N > threshold:
            consensus.append(key)
    return [{"start": s, "end": e, "type": t} for s, e, t in consensus]


def vc_weighted_construct(samples, threshold):
    vc = compute_vc(samples)
    total_vc = sum(vc)
    entity_vc_vote = defaultdict(float)
    for i, s in enumerate(samples):
        seen = set()
        for e in s.get("entities", []):
            key = (e["start"], e["end"], e["type"])
            if key not in seen:
                entity_vc_vote[key] += vc[i]
                seen.add(key)
    consensus = []
    for key, vote in entity_vc_vote.items():
        normalized = vote / total_vc if total_vc > 0 else 0
        if normalized > threshold:
            consensus.append(key)
    return [{"start": s, "end": e, "type": t} for s, e, t in consensus]


def is_degenerate(samples):
    key_sets = set()
    for s in samples:
        ks = frozenset((e["start"], e["end"], e["type"]) for e in s.get("entities", []))
        key_sets.add(ks)
    return len(key_sets) == 1


def load_data(path):
    instances = {}
    with open(path) as f:
        for line in f:
            if not line.strip():
                continue
            obj = json.loads(line)
            instances[obj["id"]] = obj
    return instances


def run_bootstrap(baseline_f1s, method_f1s, label=""):
    rng = np.random.RandomState(SEED)
    base = np.array(baseline_f1s)
    method = np.array(method_f1s)
    n = len(base)
    diffs = method - base
    obs_diff = float(diffs.mean())
    boot = np.zeros(B)
    for b in range(B):
        idx = rng.randint(0, n, n)
        boot[b] = diffs[idx].mean()
    boot.sort()
    ci_lo = float(boot[int(0.025 * B)])
    ci_hi = float(boot[int(0.975 * B)])
    p_value = float(np.mean(boot <= 0))
    return {
        "label": label,
        "n": n,
        "baseline_f1": float(base.mean()),
        "method_f1": float(method.mean()),
        "delta_pp": round(obs_diff * 100, 4),
        "ci_95_pp": [round(ci_lo * 100, 4), round(ci_hi * 100, 4)],
        "p_value": round(p_value, 4),
    }


def main():
    parser = argparse.ArgumentParser(description="Cross-model entity construction")
    parser.add_argument("--qwen", required=True, help="Qwen samples.jsonl path")
    parser.add_argument("--llama", required=True, help="LLaMA samples.jsonl path")
    parser.add_argument("--output", required=True, help="Output JSON path")
    parser.add_argument("--dataset", default="unknown", help="Dataset label")
    parser.add_argument("--skip-m030", action="store_true", help="Skip M030 greedy F1 sanity check")
    args = parser.parse_args()

    print(f"=== Cross-Model Construction: {args.dataset} ===", file=__import__('sys').stderr)

    print("Loading Qwen data...", file=__import__('sys').stderr)
    qwen_data = load_data(args.qwen)
    print(f"  {len(qwen_data)} instances", file=__import__('sys').stderr)

    print("Loading LLaMA data...", file=__import__('sys').stderr)
    llama_data = load_data(args.llama)
    print(f"  {len(llama_data)} instances", file=__import__('sys').stderr)

    common_ids = sorted(set(qwen_data.keys()) & set(llama_data.keys()))
    print(f"Common: {len(common_ids)}", file=__import__('sys').stderr)

    filtered_ids = [id_ for id_ in common_ids if qwen_data[id_]["gold"].get("entities", [])]
    print(f"After gold filter: {len(filtered_ids)}", file=__import__('sys').stderr)

    qwen_greedy_f1s = []
    llama_greedy_f1s = []
    for id_ in filtered_ids:
        gold = qwen_data[id_]["gold"]["entities"]
        qg = qwen_data[id_].get("greedy", qwen_data[id_]["samples"][0])
        lg = llama_data[id_].get("greedy", llama_data[id_]["samples"][0])
        qwen_greedy_f1s.append(compute_entity_f1(qg.get("entities", []), gold))
        llama_greedy_f1s.append(compute_entity_f1(lg.get("entities", []), gold))

    qwen_greedy_mean = float(np.mean(qwen_greedy_f1s))
    llama_greedy_mean = float(np.mean(llama_greedy_f1s))
    print(f"Qwen greedy F1: {qwen_greedy_mean:.4f}", file=__import__('sys').stderr)
    print(f"LLaMA greedy F1: {llama_greedy_mean:.4f}", file=__import__('sys').stderr)

    m030_pass = True
    if not args.skip_m030:
        if abs(qwen_greedy_mean - 0.748) > 0.01:
            print(f"M030 FAIL: Qwen greedy={qwen_greedy_mean:.4f}", file=__import__('sys').stderr)
            __import__('sys').exit(1)
        if abs(llama_greedy_mean - 0.745) > 0.01:
            print(f"M030 FAIL: LLaMA greedy={llama_greedy_mean:.4f}", file=__import__('sys').stderr)
            __import__('sys').exit(1)
        print("M030 passed.", file=__import__('sys').stderr)
    else:
        print("M030 check skipped.", file=__import__('sys').stderr)
        m030_pass = "skipped"

    theta = 0.25

    groups = {
        "pure_qwen_uniform": [], "pure_qwen_vc": [],
        "pure_llama_uniform": [], "pure_llama_vc": [],
        "mixed_uniform": [], "mixed_vc": [],
    }
    degen = {"pure_qwen": 0, "pure_llama": 0, "mixed": 0}

    for i, id_ in enumerate(filtered_ids):
        if i % 5000 == 0:
            print(f"  Processing {i}/{len(filtered_ids)}...", file=__import__('sys').stderr)
        gold = qwen_data[id_]["gold"]["entities"]
        qs = qwen_data[id_]["samples"][:8]
        ls = llama_data[id_]["samples"][:8]
        ms = qs[:4] + ls[:4]

        if is_degenerate(qs):
            degen["pure_qwen"] += 1
        if is_degenerate(ls):
            degen["pure_llama"] += 1
        if is_degenerate(ms):
            degen["mixed"] += 1

        groups["pure_qwen_uniform"].append(compute_entity_f1(uniform_construct(qs, theta), gold))
        groups["pure_qwen_vc"].append(compute_entity_f1(vc_weighted_construct(qs, theta), gold))
        groups["pure_llama_uniform"].append(compute_entity_f1(uniform_construct(ls, theta), gold))
        groups["pure_llama_vc"].append(compute_entity_f1(vc_weighted_construct(ls, theta), gold))
        groups["mixed_uniform"].append(compute_entity_f1(uniform_construct(ms, theta), gold))
        groups["mixed_vc"].append(compute_entity_f1(vc_weighted_construct(ms, theta), gold))

    n_total = len(filtered_ids)

    bs = {}
    bs["pure_qwen_uniform"] = run_bootstrap(qwen_greedy_f1s, groups["pure_qwen_uniform"], "pure_qwen_uniform_vs_greedy")
    bs["pure_qwen_vc"] = run_bootstrap(qwen_greedy_f1s, groups["pure_qwen_vc"], "pure_qwen_vc_vs_greedy")
    bs["pure_llama_uniform"] = run_bootstrap(llama_greedy_f1s, groups["pure_llama_uniform"], "pure_llama_uniform_vs_greedy")
    bs["pure_llama_vc"] = run_bootstrap(llama_greedy_f1s, groups["pure_llama_vc"], "pure_llama_vc_vs_greedy")
    bs["mixed_uniform_vs_qwen"] = run_bootstrap(qwen_greedy_f1s, groups["mixed_uniform"], "mixed_uniform_vs_qwen_greedy")
    bs["mixed_vc_vs_qwen"] = run_bootstrap(qwen_greedy_f1s, groups["mixed_vc"], "mixed_vc_vs_qwen_greedy")
    bs["mixed_uniform_vs_llama"] = run_bootstrap(llama_greedy_f1s, groups["mixed_uniform"], "mixed_uniform_vs_llama_greedy")
    bs["mixed_vc_vs_llama"] = run_bootstrap(llama_greedy_f1s, groups["mixed_vc"], "mixed_vc_vs_llama_greedy")

    bs["mixed_uni_vs_pure_qwen_uni"] = run_bootstrap(groups["pure_qwen_uniform"], groups["mixed_uniform"], "mixed_uni_vs_pure_qwen_uni")
    bs["mixed_vc_vs_pure_qwen_vc"] = run_bootstrap(groups["pure_qwen_vc"], groups["mixed_vc"], "mixed_vc_vs_pure_qwen_vc")
    bs["mixed_uni_vs_pure_llama_uni"] = run_bootstrap(groups["pure_llama_uniform"], groups["mixed_uniform"], "mixed_uni_vs_pure_llama_uni")
    bs["mixed_vc_vs_pure_llama_vc"] = run_bootstrap(groups["pure_llama_vc"], groups["mixed_vc"], "mixed_vc_vs_pure_llama_vc")

    summary = {
        "meta": {
            "dataset": args.dataset,
            "qwen_path": args.qwen,
            "llama_path": args.llama,
            "n_common": len(common_ids),
            "n_filtered": n_total,
            "threshold": theta,
            "n_bootstrap": B,
        },
        "m030": {
            "qwen_greedy_f1": round(qwen_greedy_mean, 4),
            "llama_greedy_f1": round(llama_greedy_mean, 4),
            "pass": m030_pass,
        },
        "degeneracy": {k: round(v / n_total, 4) for k, v in degen.items()},
        "construction_f1": {k: round(float(np.mean(v)), 4) for k, v in groups.items()},
        "bootstrap": bs,
    }

    with open(args.output, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\nResults -> {args.output}", file=__import__('sys').stderr)

    fmt = "{:<25} {:>8} {:>8} {:>8} {:>10} {:>10} {:>8} {:>8}"
    print("\n" + fmt.format("Group", "Degen%", "Uni F1", "VC F1", "Uni dF1", "VC dF1", "Uni p", "VC p"), file=__import__('sys').stderr)
    print("-" * 95, file=__import__('sys').stderr)

    d = summary["degeneracy"]
    c = summary["construction_f1"]
    print(fmt.format(
        "Pure Qwen (N=8)", f"{d['pure_qwen']*100:.1f}%", f"{c['pure_qwen_uniform']:.4f}", f"{c['pure_qwen_vc']:.4f}",
        f"{bs['pure_qwen_uniform']['delta_pp']:+.2f}pp", f"{bs['pure_qwen_vc']['delta_pp']:+.2f}pp",
        f"{bs['pure_qwen_uniform']['p_value']:.4f}", f"{bs['pure_qwen_vc']['p_value']:.4f}"), file=__import__('sys').stderr)

    print(fmt.format(
        "Pure LLaMA (N=8)", f"{d['pure_llama']*100:.1f}%", f"{c['pure_llama_uniform']:.4f}", f"{c['pure_llama_vc']:.4f}",
        f"{bs['pure_llama_uniform']['delta_pp']:+.2f}pp", f"{bs['pure_llama_vc']['delta_pp']:+.2f}pp",
        f"{bs['pure_llama_uniform']['p_value']:.4f}", f"{bs['pure_llama_vc']['p_value']:.4f}"), file=__import__('sys').stderr)

    print(fmt.format(
        "Mixed (4Q+4L)", f"{d['mixed']*100:.1f}%", f"{c['mixed_uniform']:.4f}", f"{c['mixed_vc']:.4f}",
        f"{bs['mixed_uniform_vs_qwen']['delta_pp']:+.2f}pp", f"{bs['mixed_vc_vs_qwen']['delta_pp']:+.2f}pp",
        f"{bs['mixed_uniform_vs_qwen']['p_value']:.4f}", f"{bs['mixed_vc_vs_qwen']['p_value']:.4f}"), file=__import__('sys').stderr)

    print("\n(dF1 vs respective greedy; mixed vs Qwen greedy)", file=__import__('sys').stderr)


if __name__ == "__main__":
    main()
