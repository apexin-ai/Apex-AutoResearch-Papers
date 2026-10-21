#!/usr/bin/env python3
"""FK per-instance bootstrap & permutation test: FK vs {SJ, VC, EM} + FK excess agreement CI."""
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
    "scierc_ner_n8_seed42": {
        "path": f"{BASE}/exp_012_rerun_1024/samples_with_logprobs.jsonl",
        "subtask": "ner",
        "n_samples": 8,
    },
    "conll_ner_n16_seed42": {
        "path": f"{BASE}/exp_002_conll_n16_r1024/samples.jsonl",
        "subtask": "ner",
        "n_samples": 16,
    },
}


def load_data(path):
    records = []
    with open(path) as f:
        for line in f:
            if line.strip():
                records.append(json.loads(line))
    return records


def extract_surface_keys(sample, subtask):
    if subtask == "ner":
        return {(e["text"], e["type"]) for e in sample.get("entities", [])}
    elif subtask == "re":
        return {(r["head"], r["tail"], r["type"]) for r in sample.get("relations", [])}
    else:
        raise ValueError(f"Unknown subtask: {subtask}")


def fleiss_kappa_decomposed(samples, subtask="ner"):
    """Returns (P_o, P_e, excess, kappa) for one instance."""
    n_raters = len(samples)
    if n_raters <= 1:
        return (1.0, 0.0, 1.0, 1.0)

    entity_sets = []
    all_keys = set()
    for sample in samples:
        keys = extract_surface_keys(sample, subtask)
        entity_sets.append(keys)
        all_keys |= keys

    n_subjects = len(all_keys)
    if n_subjects <= 0:
        return (1.0, 0.0, 1.0, 1.0)

    key_list = sorted(all_keys)
    rating = np.zeros((n_subjects, 2), dtype=np.int64)
    for es in entity_sets:
        for idx, key in enumerate(key_list):
            if key in es:
                rating[idx, 1] += 1
            else:
                rating[idx, 0] += 1

    n = n_raters
    if np.all(np.max(rating, axis=1) == n):
        return (1.0, 0.0, 1.0, 1.0)

    P_i = (np.sum(rating ** 2, axis=1) - n) / (n * (n - 1))
    P_bar = float(np.mean(P_i))
    p_j = np.sum(rating, axis=0) / (n_subjects * n)
    P_e = float(np.sum(p_j ** 2))
    excess = P_bar - P_e
    if abs(1.0 - P_e) < 1e-12:
        return (P_bar, P_e, excess, 1.0)
    kappa = excess / (1.0 - P_e)
    return (P_bar, P_e, excess, kappa)


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


def compute_instance_signals(records, subtask, n_samples=None):
    """Compute per-instance signal values, greedy F1, and FK decomposition."""
    sj, fk, vc, em, f1 = [], [], [], [], []
    po_list, pe_list, excess_list = [], [], []
    gold_key = "entities" if subtask == "ner" else "relations"
    valid_ids = []

    for inst in records:
        gold = inst["gold"]
        if len(gold.get(gold_key, [])) == 0:
            continue
        samples = inst["samples"]
        if n_samples is not None:
            samples = samples[:n_samples]

        greedy = inst.get("greedy", samples[0])

        sj.append(structural_consistency_soft_jaccard(samples, subtask=subtask))
        fk.append(fleiss_kappa_surface(samples, subtask=subtask))
        vc.append(compute_voting_confidence(samples, subtask))
        em.append(compute_exact_match_rate(samples, subtask))
        f1.append(per_instance_f1(greedy, gold, subtask=subtask))

        P_o, P_e, excess, _ = fleiss_kappa_decomposed(samples, subtask=subtask)
        po_list.append(P_o)
        pe_list.append(P_e)
        excess_list.append(excess)
        valid_ids.append(inst["id"])

    signals = {
        "SJ": np.array(sj),
        "FK": np.array(fk),
        "VC": np.array(vc),
        "EM": np.array(em),
    }
    fk_decomp = {
        "P_o": np.array(po_list),
        "P_e": np.array(pe_list),
        "excess": np.array(excess_list),
    }
    return signals, np.array(f1), fk_decomp, valid_ids


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
    # two-sided p: fraction of bootstrap where sign differs from observed
    if point_delta >= 0:
        p_boot = float(np.mean(deltas <= 0)) * 2
    else:
        p_boot = float(np.mean(deltas >= 0)) * 2
    p_boot = min(p_boot, 1.0)

    return {
        "rho_a": round(rho_a, 4),
        "rho_b": round(rho_b, 4),
        "mean_diff": round(point_delta, 4),
        "ci_lower": round(ci_lo, 4),
        "ci_upper": round(ci_hi, 4),
        "p_bootstrap": round(p_boot, 6),
        "n_boot_valid": count,
        "n_instances": n,
    }


def permutation_test_delta(sig_a, sig_b, quality, n_perm=10000, seed=42):
    """Two-sided permutation test: H0: rho(A,q) - rho(B,q) = 0."""
    rng = np.random.default_rng(seed)
    mask = np.isfinite(sig_a) & np.isfinite(sig_b) & np.isfinite(quality)
    sa, sb, q = sig_a[mask], sig_b[mask], quality[mask]
    n = len(sa)

    rho_a = float(spearmanr(sa, q).statistic)
    rho_b = float(spearmanr(sb, q).statistic)
    obs_delta = abs(rho_a - rho_b)

    count_ge = 0
    for _ in range(n_perm):
        swap = rng.random(n) < 0.5
        pa = np.where(swap, sb, sa)
        pb = np.where(swap, sa, sb)
        ra = spearmanr(pa, q).statistic
        rb = spearmanr(pb, q).statistic
        perm_delta = abs(float(ra) - float(rb))
        if perm_delta >= obs_delta:
            count_ge += 1

    p_perm = (count_ge + 1) / (n_perm + 1)
    return {
        "observed_abs_delta": round(obs_delta, 4),
        "p_permutation": round(p_perm, 6),
        "n_perm": n_perm,
    }


def bootstrap_excess_agreement(fk_decomp, n_boot=10000, seed=42):
    """Bootstrap 95% CI for mean FK excess agreement (P_o - P_e)."""
    rng = np.random.default_rng(seed)
    excess = fk_decomp["excess"]
    po = fk_decomp["P_o"]
    pe = fk_decomp["P_e"]
    n = len(excess)

    obs_mean_excess = float(np.mean(excess))
    obs_mean_po = float(np.mean(po))
    obs_mean_pe = float(np.mean(pe))

    boot_excess = np.empty(n_boot)
    boot_po = np.empty(n_boot)
    boot_pe = np.empty(n_boot)
    boot_fk = np.empty(n_boot)

    for i in range(n_boot):
        idx = rng.integers(0, n, size=n)
        boot_excess[i] = np.mean(excess[idx])
        boot_po[i] = np.mean(po[idx])
        boot_pe[i] = np.mean(pe[idx])
        mean_excess_i = boot_excess[i]
        mean_1_minus_pe = np.mean(1.0 - pe[idx])
        boot_fk[i] = mean_excess_i / mean_1_minus_pe if abs(mean_1_minus_pe) > 1e-12 else 1.0

    return {
        "mean_excess": round(obs_mean_excess, 4),
        "excess_ci_lower": round(float(np.percentile(boot_excess, 2.5)), 4),
        "excess_ci_upper": round(float(np.percentile(boot_excess, 97.5)), 4),
        "mean_P_o": round(obs_mean_po, 4),
        "P_o_ci_lower": round(float(np.percentile(boot_po, 2.5)), 4),
        "P_o_ci_upper": round(float(np.percentile(boot_po, 97.5)), 4),
        "mean_P_e": round(obs_mean_pe, 4),
        "P_e_ci_lower": round(float(np.percentile(boot_pe, 2.5)), 4),
        "P_e_ci_upper": round(float(np.percentile(boot_pe, 97.5)), 4),
        "mean_FK_ratio": round(float(np.mean(boot_fk)), 4),
        "FK_ratio_ci_lower": round(float(np.percentile(boot_fk, 2.5)), 4),
        "FK_ratio_ci_upper": round(float(np.percentile(boot_fk, 97.5)), 4),
        "n_instances": n,
        "n_boot": n_boot,
    }


def bootstrap_rho_single(signal, quality, n_boot=10000, seed=42):
    """Bootstrap 95% CI for a single Spearman rho."""
    rng = np.random.default_rng(seed)
    mask = np.isfinite(signal) & np.isfinite(quality)
    s, q = signal[mask], quality[mask]
    n = len(s)
    obs_rho = float(spearmanr(s, q).statistic)

    rhos = np.empty(n_boot)
    count = 0
    for i in range(n_boot):
        idx = rng.integers(0, n, size=n)
        r = spearmanr(s[idx], q[idx]).statistic
        if np.isfinite(r):
            rhos[count] = float(r)
            count += 1
    rhos = np.sort(rhos[:count])

    return {
        "rho": round(obs_rho, 4),
        "ci_lower": round(float(np.percentile(rhos, 2.5)), 4),
        "ci_upper": round(float(np.percentile(rhos, 97.5)), 4),
        "n_boot_valid": count,
        "n_instances": n,
    }


def analyze_dataset(name, config):
    print(f"\n{'='*60}")
    print(f"Dataset: {name}")

    records = load_data(config["path"])
    n_samples = config.get("n_samples")
    print(f"  total records: {len(records)}, using first {n_samples} samples")

    signals, f1, fk_decomp, valid_ids = compute_instance_signals(
        records, config["subtask"], n_samples=n_samples
    )
    n = len(f1)
    print(f"  valid instances (non-empty gold): {n}")

    # Per-signal bootstrap rho
    signal_rhos = {}
    for sig_name in ["FK", "SJ", "VC", "EM"]:
        rho_result = bootstrap_rho_single(signals[sig_name], f1)
        signal_rhos[sig_name] = rho_result
        print(f"  rho({sig_name})={rho_result['rho']:.4f} [{rho_result['ci_lower']:.4f}, {rho_result['ci_upper']:.4f}]")

    # Pairwise comparisons: FK vs each other signal
    comparisons = {}
    for other in ["SJ", "VC", "EM"]:
        label = f"FK_vs_{other}"
        print(f"\n  --- FK vs {other} ---")
        boot = paired_bootstrap_delta(signals["FK"], signals[other], f1)
        perm = permutation_test_delta(signals["FK"], signals[other], f1)

        result = {**boot, **perm}
        comparisons[label] = result
        print(f"    rho(FK)={boot['rho_a']:.4f}, rho({other})={boot['rho_b']:.4f}")
        print(f"    delta(FK-{other})={boot['mean_diff']:+.4f}, 95% CI=[{boot['ci_lower']:+.4f}, {boot['ci_upper']:+.4f}]")
        print(f"    p_bootstrap={boot['p_bootstrap']:.6f}, p_permutation={perm['p_permutation']:.6f}")

    # FK excess agreement bootstrap
    print(f"\n  --- FK Excess Agreement Bootstrap ---")
    excess_result = bootstrap_excess_agreement(fk_decomp)
    print(f"    mean excess={excess_result['mean_excess']:.4f} [{excess_result['excess_ci_lower']:.4f}, {excess_result['excess_ci_upper']:.4f}]")
    print(f"    mean P_o={excess_result['mean_P_o']:.4f}, mean P_e={excess_result['mean_P_e']:.4f}")
    print(f"    FK ratio={excess_result['mean_FK_ratio']:.4f} [{excess_result['FK_ratio_ci_lower']:.4f}, {excess_result['FK_ratio_ci_upper']:.4f}]")

    # Signal summary stats
    signal_stats = {}
    for sig_name in ["FK", "SJ", "VC", "EM"]:
        arr = signals[sig_name]
        signal_stats[sig_name] = {
            "mean": round(float(np.mean(arr)), 4),
            "std": round(float(np.std(arr)), 4),
            "median": round(float(np.median(arr)), 4),
            "p5": round(float(np.percentile(arr, 5)), 4),
            "p95": round(float(np.percentile(arr, 95)), 4),
        }

    return {
        "n_total_records": len(records),
        "n_valid": n,
        "n_samples_per_instance": n_samples,
        "subtask": config["subtask"],
        "signal_rhos": signal_rhos,
        "signal_stats": signal_stats,
        "comparisons": comparisons,
        "fk_excess_agreement": excess_result,
    }


if __name__ == "__main__":
    results = {}
    for name, config in DATASETS.items():
        results[name] = analyze_dataset(name, config)

    out_path = f"{BASE}/analysis_fk_bootstrap_per_instance.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\n\nSaved to {out_path}")

    # Summary table
    print("\n\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    for ds_name, ds_res in results.items():
        print(f"\n{ds_name} (n={ds_res['n_valid']}, N={ds_res['n_samples_per_instance']}):")
        print(f"  Signal rhos:")
        for sig, r in ds_res["signal_rhos"].items():
            print(f"    {sig}: {r['rho']:.4f} [{r['ci_lower']:.4f}, {r['ci_upper']:.4f}]")
        print(f"  FK vs others (delta = rho_FK - rho_other):")
        for comp_name, comp in ds_res["comparisons"].items():
            sig_star = "***" if comp["p_permutation"] < 0.001 else "**" if comp["p_permutation"] < 0.01 else "*" if comp["p_permutation"] < 0.05 else "n.s."
            print(f"    {comp_name}: delta={comp['mean_diff']:+.4f} CI=[{comp['ci_lower']:+.4f},{comp['ci_upper']:+.4f}] p_perm={comp['p_permutation']:.4f} {sig_star}")
        ea = ds_res["fk_excess_agreement"]
        print(f"  FK excess agreement: {ea['mean_excess']:.4f} [{ea['excess_ci_lower']:.4f}, {ea['excess_ci_upper']:.4f}]")
