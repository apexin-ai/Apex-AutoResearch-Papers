#!/usr/bin/env python3
"""FK Bootstrap CI & Permutation Test: FK vs {SJ, VC, EM} across datasets."""
import json
import sys
import numpy as np
from collections import Counter
from scipy.stats import spearmanr

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from consistency import structural_consistency_soft_jaccard, fleiss_kappa_surface
from evaluation import per_instance_f1

BASE = "/root/autodl-tmp/struct_self_consist_ie/output"

DATASETS = {
    "scierc_ner_seed42_n16": {
        "path": f"{BASE}/exp_001_seed42_v2/samples.jsonl",
        "subtask": "ner",
    },
    "scierc_ner_seed123_n16": {
        "path": f"{BASE}/exp_001_seed123_v2/samples.jsonl",
        "subtask": "ner",
    },
    "scierc_ner_seed456_n16": {
        "path": f"{BASE}/exp_001_seed456_v2_ner/samples.jsonl",
        "subtask": "ner",
    },
    "scierc_re_seed42_n16": {
        "path": f"{BASE}/exp_001_seed42_v2/samples.jsonl",
        "subtask": "re",
    },
    "conll_ner_seed42_n16": {
        "path": f"{BASE}/exp_002_conll_n16_r1024/samples.jsonl",
        "subtask": "ner",
    },
    "llama_conll_ner_seed42_n16": {
        "path": f"{BASE}/exp_017_llama_conll_n16_r1024/samples.jsonl",
        "subtask": "ner",
    },
    "llama_scierc_ner_seed42": {
        "path": f"{BASE}/exp_018_llama_scierc_seed42_r1024/samples.jsonl",
        "subtask": "ner",
    },
}


def load_data(path):
    records = []
    with open(path) as f:
        for line in f:
            if line.strip():
                records.append(json.loads(line))
    return records


def compute_exact_match_rate(samples, subtask):
    if subtask == "ner":
        keys = [frozenset((e["text"], e["type"]) for e in s.get("entities", [])) for s in samples]
    else:
        keys = [frozenset((r["head"], r["tail"], r["type"]) for r in s.get("relations", [])) for s in samples]
    if not keys:
        return 0.0
    counter = Counter(keys)
    return counter.most_common(1)[0][1] / len(samples)


def compute_voting_confidence(samples, subtask):
    N = len(samples)
    if N == 0:
        return 0.0
    counter = Counter()
    if subtask == "ner":
        for s in samples:
            for e in s.get("entities", []):
                counter[(e["text"], e["type"])] += 1
    else:
        for s in samples:
            for r in s.get("relations", []):
                counter[(r["head"], r["tail"], r["type"])] += 1
    if not counter:
        return 0.0
    rates = [v / N for v in counter.values()]
    return float(np.mean(rates))


def compute_instance_signals(records, subtask):
    """Compute per-instance signal values and greedy F1."""
    sj, fk, vc, em, f1 = [], [], [], [], []
    gold_key = "entities" if subtask == "ner" else "relations"
    for inst in records:
        gold = inst["gold"]
        if len(gold.get(gold_key, [])) == 0:
            continue
        samples = inst["samples"]
        greedy = inst.get("greedy", samples[0])
        sj.append(structural_consistency_soft_jaccard(samples, subtask=subtask))
        fk.append(fleiss_kappa_surface(samples, subtask=subtask))
        vc.append(compute_voting_confidence(samples, subtask))
        em.append(compute_exact_match_rate(samples, subtask))
        f1.append(per_instance_f1(greedy, gold, subtask=subtask))
    return {
        "SJ": np.array(sj),
        "FK": np.array(fk),
        "VC": np.array(vc),
        "EM": np.array(em),
    }, np.array(f1)


def paired_bootstrap_delta(sig_a, sig_b, quality, n_boot=10000, seed=42):
    """Bootstrap CI for rho(sig_a, quality) - rho(sig_b, quality)."""
    rng = np.random.default_rng(seed)
    mask = np.isfinite(sig_a) & np.isfinite(sig_b) & np.isfinite(quality)
    sa, sb, q = sig_a[mask], sig_b[mask], quality[mask]
    n = len(sa)

    rho_a = float(spearmanr(sa, q).statistic)
    rho_b = float(spearmanr(sb, q).statistic)
    point_delta = rho_a - rho_b

    deltas = np.empty(n_boot)
    count = 0
    for i in range(n_boot):
        idx = rng.integers(0, n, size=n)
        ra = spearmanr(sa[idx], q[idx]).statistic
        rb = spearmanr(sb[idx], q[idx]).statistic
        d = float(ra) - float(rb)
        if np.isfinite(d):
            deltas[count] = d
            count += 1
    deltas = np.sort(deltas[:count])

    ci_lo = float(np.percentile(deltas, 2.5))
    ci_hi = float(np.percentile(deltas, 97.5))
    p_boot = float(np.mean(deltas <= 0))  # one-sided: P(delta <= 0)

    return {
        "rho_a": round(rho_a, 4),
        "rho_b": round(rho_b, 4),
        "mean_diff": round(point_delta, 4),
        "ci_lower": round(ci_lo, 4),
        "ci_upper": round(ci_hi, 4),
        "p_bootstrap": round(p_boot, 6),
        "n_boot": count,
        "n_instances": n,
    }


def permutation_test_delta(sig_a, sig_b, quality, n_perm=10000, seed=42):
    """Permutation test: under H0, rho(A,q) - rho(B,q) = 0.
    Shuffle signal assignment within each instance."""
    rng = np.random.default_rng(seed)
    mask = np.isfinite(sig_a) & np.isfinite(sig_b) & np.isfinite(quality)
    sa, sb, q = sig_a[mask], sig_b[mask], quality[mask]
    n = len(sa)

    rho_a = float(spearmanr(sa, q).statistic)
    rho_b = float(spearmanr(sb, q).statistic)
    obs_delta = rho_a - rho_b

    count_ge = 0
    for _ in range(n_perm):
        swap = rng.random(n) < 0.5
        pa = np.where(swap, sb, sa)
        pb = np.where(swap, sa, sb)
        ra = spearmanr(pa, q).statistic
        rb = spearmanr(pb, q).statistic
        perm_delta = float(ra) - float(rb)
        if perm_delta >= obs_delta:
            count_ge += 1

    p_perm = (count_ge + 1) / (n_perm + 1)
    return {
        "observed_delta": round(obs_delta, 4),
        "p_permutation": round(p_perm, 6),
        "n_perm": n_perm,
    }


def analyze_dataset(name, config):
    print(f"\n{'='*60}")
    print(f"Dataset: {name}")
    print(f"  path: {config['path']}")
    print(f"  subtask: {config['subtask']}")

    records = load_data(config["path"])
    print(f"  total records: {len(records)}")

    signals, f1 = compute_instance_signals(records, config["subtask"])
    n = len(f1)
    print(f"  valid instances: {n}")

    comparisons = {}
    for other in ["SJ", "VC", "EM"]:
        label = f"{other}_minus_FK"
        print(f"\n  --- {other} vs FK (rho) ---")
        boot = paired_bootstrap_delta(signals[other], signals["FK"], f1)
        perm = permutation_test_delta(signals[other], signals["FK"], f1)

        result = {**boot, **perm}
        comparisons[label] = result
        print(f"    rho({other})={boot['rho_a']:.4f}, rho(FK)={boot['rho_b']:.4f}")
        print(f"    delta={boot['mean_diff']:+.4f}, 95% CI=[{boot['ci_lower']:+.4f}, {boot['ci_upper']:+.4f}]")
        print(f"    p_bootstrap={boot['p_bootstrap']:.6f}, p_permutation={perm['p_permutation']:.6f}")

    return {
        "n_valid": n,
        "subtask": config["subtask"],
        "comparisons": comparisons,
    }


if __name__ == "__main__":
    results = {}
    for name, config in DATASETS.items():
        results[name] = analyze_dataset(name, config)

    out_path = f"{BASE}/analysis_fk_bootstrap_ci.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\n\nSaved to {out_path}")

    print("\n\n=== SUMMARY ===")
    for ds_name, ds_res in results.items():
        print(f"\n{ds_name} (n={ds_res['n_valid']}):")
        for comp_name, comp in ds_res["comparisons"].items():
            sig_star = "***" if comp["p_permutation"] < 0.001 else "**" if comp["p_permutation"] < 0.01 else "*" if comp["p_permutation"] < 0.05 else "n.s."
            print(f"  {comp_name}: delta={comp['mean_diff']:+.4f} CI=[{comp['ci_lower']:+.4f},{comp['ci_upper']:+.4f}] p_boot={comp['p_bootstrap']:.4f} p_perm={comp['p_permutation']:.4f} {sig_star}")
