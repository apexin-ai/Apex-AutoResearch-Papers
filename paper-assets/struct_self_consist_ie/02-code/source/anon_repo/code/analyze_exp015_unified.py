"""exp-015: Unified cross-signal comparison with bootstrap CI, LOO-SJ, and calibration.

Computes all 5 confidence signals on the same dataset (pilot_005, T=0.7 with logprobs),
produces a unified 5-signal x 4-metric x 2-task comparison table, bootstrap CI,
leave-one-out SJ analysis, and calibration bins.
"""

import json
import os
import sys
from collections import Counter

import numpy as np
from scipy.stats import spearmanr, kendalltau

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from consistency import (
    compute_all_consistency_scores,
    structural_consistency_soft_jaccard,
)
from evaluation import per_instance_f1

DATA_PATH = "/root/autodl-tmp/struct_self_consist_ie/output/exp_012_logprob/samples_with_logprobs.jsonl"
OUTPUT_DIR = "/root/autodl-tmp/struct_self_consist_ie/output/exp_015_unified"


def load_data(path):
    instances = []
    with open(path) as f:
        for line in f:
            if line.strip():
                instances.append(json.loads(line))
    return instances


def auroc_simple(scores, labels):
    scores = np.array(scores, dtype=float)
    labels = np.array(labels, dtype=int)
    if len(set(labels)) < 2:
        return float('nan')
    pos = scores[labels == 1]
    neg = scores[labels == 0]
    n_pos, n_neg = len(pos), len(neg)
    if n_pos == 0 or n_neg == 0:
        return float('nan')
    count = 0.0
    for p in pos:
        count += np.sum(p > neg) + 0.5 * np.sum(p == neg)
    return count / (n_pos * n_neg)


# ---- Signal computation ----

def compute_exact_match_rate(samples, subtask):
    if subtask == "ner":
        keys = [frozenset((e["text"], e["type"]) for e in s.get("entities", [])) for s in samples]
    else:
        keys = [frozenset((r["head"], r["tail"], r["type"]) for r in s.get("relations", [])) for s in samples]
    counter = Counter(keys)
    return counter.most_common(1)[0][1] / len(samples)


def compute_voting_confidence(samples, subtask):
    N = len(samples)
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


def compute_mean_logprob(samples):
    logprobs = [s.get("mean_logprob") for s in samples if s.get("mean_logprob") is not None]
    logprobs = [lp for lp in logprobs if np.isfinite(lp)]
    if not logprobs:
        return float("nan")
    return float(np.mean(logprobs))


def compute_all_signals(instances, subtask):
    consistency = compute_all_consistency_scores(instances, subtask=subtask)
    signals = {
        "soft_jaccard": consistency["soft_jaccard"],
        "fleiss_kappa": consistency["fleiss_kappa"],
        "mean_logprob": [],
        "exact_match": [],
        "entity_voting": [],
    }
    f1_scores = []
    for inst in instances:
        samples = inst["samples"]
        gold = inst["gold"]
        greedy = inst.get("greedy")
        if greedy is not None:
            f1 = per_instance_f1(greedy, gold, subtask=subtask)
        else:
            f1 = per_instance_f1(samples[0], gold, subtask=subtask)
        f1_scores.append(f1)
        signals["mean_logprob"].append(compute_mean_logprob(samples))
        signals["exact_match"].append(compute_exact_match_rate(samples, subtask))
        signals["entity_voting"].append(compute_voting_confidence(samples, subtask))
    return signals, f1_scores


def compute_metrics(signal_values, f1_values, median_f1):
    x = np.array(signal_values, dtype=float)
    y = np.array(f1_values, dtype=float)
    mask = np.isfinite(x) & np.isfinite(y)
    x, y = x[mask], y[mask]
    if len(x) < 3:
        return {"rho": float("nan"), "p_rho": float("nan"),
                "tau": float("nan"), "p_tau": float("nan"),
                "auroc": float("nan"), "n": int(len(x))}
    rho_r = spearmanr(x, y)
    tau_r = kendalltau(x, y)
    labels = (y >= median_f1).astype(int)
    auroc = auroc_simple(x, labels)
    return {
        "rho": float(rho_r.statistic), "p_rho": float(rho_r.pvalue),
        "tau": float(tau_r.statistic), "p_tau": float(tau_r.pvalue),
        "auroc": float(auroc), "n": int(len(x)),
    }


def bootstrap_rho_diff(signal_a, signal_b, f1_values, n_boot=10000, seed=42):
    rng = np.random.RandomState(seed)
    a = np.array(signal_a, dtype=float)
    b = np.array(signal_b, dtype=float)
    y = np.array(f1_values, dtype=float)
    mask = np.isfinite(a) & np.isfinite(b) & np.isfinite(y)
    a, b, y = a[mask], b[mask], y[mask]
    n = len(y)
    diffs = np.empty(n_boot)
    for i in range(n_boot):
        idx = rng.randint(0, n, size=n)
        rho_a = spearmanr(a[idx], y[idx]).statistic
        rho_b = spearmanr(b[idx], y[idx]).statistic
        diffs[i] = rho_a - rho_b
    ci_low = float(np.percentile(diffs, 2.5))
    ci_high = float(np.percentile(diffs, 97.5))
    return {
        "mean_diff": float(np.mean(diffs)),
        "ci_95_low": ci_low,
        "ci_95_high": ci_high,
        "significant": (ci_low > 0) or (ci_high < 0),
    }


def loo_sj_analysis(instances, f1_scores, subtask):
    standard_sj = []
    loo_sj_list = []
    for inst in instances:
        samples = inst["samples"]
        sj_full = structural_consistency_soft_jaccard(samples, subtask=subtask)
        standard_sj.append(sj_full)
        loo_vals = []
        for i in range(len(samples)):
            subset = samples[:i] + samples[i+1:]
            loo_vals.append(structural_consistency_soft_jaccard(subset, subtask=subtask))
        loo_sj_list.append(float(np.mean(loo_vals)))
    std_rho = float(spearmanr(standard_sj, f1_scores).statistic)
    loo_rho = float(spearmanr(loo_sj_list, f1_scores).statistic)
    rho_diff = abs(loo_rho - std_rho)
    loo_vs_std_rho = float(spearmanr(standard_sj, loo_sj_list).statistic)
    return {
        "standard_f1_rho": std_rho,
        "loo_f1_rho": loo_rho,
        "rho_difference": rho_diff,
        "loo_vs_standard_rho": loo_vs_std_rho,
        "circularity_ok": rho_diff < 0.02,
    }


def calibration_analysis(signal_values, f1_values, n_bins=5):
    x = np.array(signal_values, dtype=float)
    y = np.array(f1_values, dtype=float)
    mask = np.isfinite(x) & np.isfinite(y)
    x, y = x[mask], y[mask]
    if len(x) < n_bins:
        return []
    bin_edges = np.percentile(x, np.linspace(0, 100, n_bins + 1))
    bin_edges[0] -= 1e-10
    bin_edges[-1] += 1e-10
    bins = []
    for i in range(n_bins):
        m = (x > bin_edges[i]) & (x <= bin_edges[i+1])
        if m.sum() == 0:
            continue
        bins.append({
            "bin": i + 1,
            "conf_range": [float(bin_edges[i]), float(bin_edges[i+1])],
            "mean_conf": float(np.mean(x[m])),
            "mean_f1": float(np.mean(y[m])),
            "n": int(m.sum()),
        })
    return bins


def generate_markdown(results):
    lines = ["# exp-015: Unified Cross-Signal Comparison", ""]
    lines.append("**Data**: pilot_005 (T=0.7, N=8 samples/instance)")
    lines.append(f"**Total instances**: {results['ner']['n_total']}")
    lines.append("")

    signal_order = ["soft_jaccard", "fleiss_kappa", "mean_logprob", "exact_match", "entity_voting"]
    signal_labels = {
        "soft_jaccard": "Soft Jaccard (SJ)",
        "fleiss_kappa": "Fleiss' Kappa (FK)",
        "mean_logprob": "Mean Log-prob",
        "exact_match": "Exact Match Rate",
        "entity_voting": "Entity Voting",
    }

    for subtask in ["ner", "re"]:
        r = results[subtask]
        label = "NER" if subtask == "ner" else "RE"
        lines.append(f"## {label}")
        lines.append(f"Valid (gold non-empty): {r['n_valid']} | Conditional: {r['n_conditional']}")
        lines.append("")

        for setting, setting_label in [("full", "Full"), ("cond", "Conditional")]:
            n = r['n_valid'] if setting == "full" else r['n_conditional']
            lines.append(f"### {setting_label} (n={n})")
            lines.append("")
            lines.append("| Signal | Spearman ρ | Kendall τ | AUROC | p-value |")
            lines.append("|--------|-----------|----------|-------|---------|")
            for sig in signal_order:
                m = r["signals"][sig][setting]
                lines.append(f"| {signal_labels[sig]} | {m['rho']:.4f} | {m['tau']:.4f} | {m['auroc']:.4f} | {m['p_rho']:.2e} |")
            lines.append("")

        lines.append("### Bootstrap 95% CI (SJ ρ − Other ρ, full set)")
        lines.append("")
        lines.append("| Comparison | Mean Δρ | 95% CI | Significant |")
        lines.append("|-----------|---------|--------|-------------|")
        for key, boot in r["bootstrap_ci"].items():
            other = key.replace("sj_vs_", "")
            sig = "Yes" if boot["significant"] else "No"
            lines.append(f"| SJ vs {signal_labels.get(other, other)} | {boot['mean_diff']:+.4f} | [{boot['ci_95_low']:+.4f}, {boot['ci_95_high']:+.4f}] | {sig} |")
        lines.append("")

        loo = r["loo_sj"]
        lines.append("### LOO-SJ Analysis")
        lines.append(f"- Standard SJ→F1 ρ: {loo['standard_f1_rho']:.4f}")
        lines.append(f"- LOO-SJ→F1 ρ: {loo['loo_f1_rho']:.4f}")
        lines.append(f"- |Δρ|: {loo['rho_difference']:.4f}")
        lines.append(f"- LOO vs Standard SJ correlation: {loo['loo_vs_standard_rho']:.4f}")
        lines.append(f"- Circularity concern: {'No (< 0.02)' if loo['circularity_ok'] else 'Yes (>= 0.02)'}")
        lines.append("")

        lines.append("### Calibration (5 quintile bins)")
        lines.append("")
        for sig in signal_order:
            lines.append(f"**{signal_labels[sig]}**")
            lines.append("")
            lines.append("| Bin | Mean Conf | Mean F1 | n |")
            lines.append("|-----|-----------|---------|---|")
            for b in r["calibration"].get(sig, []):
                lines.append(f"| {b['bin']} | {b['mean_conf']:.4f} | {b['mean_f1']:.4f} | {b['n']} |")
            lines.append("")
        lines.append("---")
        lines.append("")
    return "\n".join(lines)


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    instances = load_data(DATA_PATH)
    print(f"Loaded {len(instances)} instances")

    results = {}
    for subtask in ["ner", "re"]:
        print(f"\n{'='*60}")
        print(f"Subtask: {subtask.upper()}")

        field = "entities" if subtask == "ner" else "relations"
        valid = [inst for inst in instances if len(inst["gold"].get(field, [])) > 0]
        print(f"  Valid (gold non-empty): {len(valid)}")

        signals, f1_scores = compute_all_signals(valid, subtask)

        # Conditional: exclude greedy_F1=0 instances (knowledge-gap)
        cond_mask = [f1_scores[i] > 0 for i in range(len(valid))]
        cond_idx = [i for i, m in enumerate(cond_mask) if m]
        print(f"  Conditional: {len(cond_idx)}")

        median_full = float(np.median(f1_scores))
        cond_f1 = [f1_scores[i] for i in cond_idx]
        median_cond = float(np.median(cond_f1))

        sr = {
            "n_total": len(instances),
            "n_valid": len(valid),
            "n_conditional": len(cond_idx),
            "median_f1_full": median_full,
            "median_f1_cond": median_cond,
            "signals": {},
        }

        for sname, svals in signals.items():
            full_m = compute_metrics(svals, f1_scores, median_full)
            cond_svals = [svals[i] for i in cond_idx]
            cond_m = compute_metrics(cond_svals, cond_f1, median_cond)
            sr["signals"][sname] = {"full": full_m, "cond": cond_m}
            print(f"  {sname:<16} full ρ={full_m['rho']:+.4f}  cond ρ={cond_m['rho']:+.4f}")

        # Bootstrap CI (SJ vs others, on full set)
        print("  Bootstrap CI...")
        sj = signals["soft_jaccard"]
        bootstrap = {}
        for other in ["fleiss_kappa", "mean_logprob", "exact_match", "entity_voting"]:
            boot = bootstrap_rho_diff(sj, signals[other], f1_scores)
            bootstrap[f"sj_vs_{other}"] = boot
            print(f"    SJ vs {other}: Δ={boot['mean_diff']:+.4f} CI=[{boot['ci_95_low']:+.4f},{boot['ci_95_high']:+.4f}] sig={boot['significant']}")
        sr["bootstrap_ci"] = bootstrap

        # LOO-SJ
        print("  LOO-SJ analysis...")
        loo = loo_sj_analysis(valid, f1_scores, subtask)
        sr["loo_sj"] = loo
        print(f"    std_rho={loo['standard_f1_rho']:.4f} loo_rho={loo['loo_f1_rho']:.4f} diff={loo['rho_difference']:.4f} ok={loo['circularity_ok']}")

        # Calibration
        cal = {}
        for sname, svals in signals.items():
            cal[sname] = calibration_analysis(svals, f1_scores)
        sr["calibration"] = cal

        results[subtask] = sr

    # Save JSON
    json_path = os.path.join(OUTPUT_DIR, "exp015_unified_report.json")
    with open(json_path, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\nJSON report: {json_path}")

    # Save markdown
    md = generate_markdown(results)
    md_path = os.path.join(OUTPUT_DIR, "exp015_summary.md")
    with open(md_path, "w") as f:
        f.write(md)
    print(f"Markdown: {md_path}")


if __name__ == "__main__":
    main()
