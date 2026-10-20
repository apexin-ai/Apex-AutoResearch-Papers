#!/usr/bin/env python3
"""exp_023 LoRA rank=8 ablation: full 5-signal analysis + selection F1 + degeneracy."""

import json
import sys
from collections import Counter

import numpy as np
from scipy.stats import spearmanr, kendalltau, rankdata

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from consistency import (
    compute_all_consistency_scores,
    _ner_soft_jaccard_pair,
    _re_soft_jaccard_pair,
    _extract_surface_keys,
)
from evaluation import per_instance_f1

DATA_PATH = "/root/autodl-tmp/struct_self_consist_ie/output/exp_023_rank8_inference/samples.jsonl"
OUTPUT_DIR = "/root/autodl-tmp/struct_self_consist_ie/output/exp_023_rank8_inference"
SUBTASKS = ["ner", "re"]

# rank=32 (r16 actually, ft_002_v2 baseline) from exp_012_rerun_1024
BASELINE_R32 = {
    "ner": {
        "full": {"SJ": 0.3599, "FK": 0.2665, "LP": 0.2052, "EM": 0.2945, "VC": 0.3792,
                 "greedy_f1": 0.643, "oracle_f1": 0.7845,
                 "sel_SJ": 0.6438, "sel_FK": 0.6458, "sel_VC": 0.6436, "sel_EM": 0.6291, "sel_LP": 0.6465},
        "cond": {"SJ": 0.3113, "FK": 0.1761, "LP": 0.1538, "EM": 0.3596, "VC": 0.3},
    },
    "re": {
        "full": {"SJ": 0.2503, "FK": 0.2752, "LP": 0.2662, "EM": 0.1344, "VC": 0.3498,
                 "greedy_f1": 0.3906},
        "cond": {"SJ": 0.2457, "FK": 0.1139, "LP": 0.0112, "EM": 0.4165, "VC": 0.2409},
    },
}


def load_data(path):
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]


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


def compute_mean_logprob(samples):
    logprobs = [s.get("mean_logprob") for s in samples if s.get("mean_logprob") is not None]
    logprobs = [lp for lp in logprobs if np.isfinite(lp)]
    if not logprobs:
        return float("nan")
    return float(np.mean(logprobs))


def safe_auroc(scores, labels):
    scores = np.asarray(scores, dtype=float)
    labels = np.asarray(labels, dtype=int)
    if len(np.unique(labels)) < 2:
        return float("nan")
    n_pos = np.sum(labels == 1)
    n_neg = np.sum(labels == 0)
    if n_pos == 0 or n_neg == 0:
        return float("nan")
    ranks = rankdata(scores)
    u = ranks[labels == 1].sum() - n_pos * (n_pos + 1) / 2
    return float(u / (n_pos * n_neg))


def safe_spearman(x, y):
    x, y = np.asarray(x, dtype=float), np.asarray(y, dtype=float)
    mask = np.isfinite(x) & np.isfinite(y)
    x, y = x[mask], y[mask]
    if len(x) < 3:
        return float("nan")
    return float(spearmanr(x, y).statistic)


def safe_kendall(x, y):
    x, y = np.asarray(x, dtype=float), np.asarray(y, dtype=float)
    mask = np.isfinite(x) & np.isfinite(y)
    x, y = x[mask], y[mask]
    if len(x) < 3:
        return float("nan")
    return float(kendalltau(x, y).statistic)


def compute_sample_sj_scores(instance, subtask):
    samples = instance["samples"]
    N = len(samples)
    field = "entities" if subtask == "ner" else "relations"
    pair_fn = _ner_soft_jaccard_pair if subtask == "ner" else _re_soft_jaccard_pair
    matrix = np.zeros((N, N))
    for i in range(N):
        for j in range(i + 1, N):
            s = pair_fn(samples[i].get(field, []), samples[j].get(field, []))
            matrix[i][j] = s
            matrix[j][i] = s
    np.fill_diagonal(matrix, 1.0)
    return [float(np.mean([matrix[k][j] for j in range(N) if j != k])) for k in range(N)]


def compute_sample_surface_scores(instance, subtask):
    samples = instance["samples"]
    N = len(samples)
    key_sets = [frozenset(_extract_surface_keys(s, subtask)) for s in samples]
    matrix = np.zeros((N, N))
    for i in range(N):
        for j in range(i + 1, N):
            union = len(key_sets[i] | key_sets[j])
            inter = len(key_sets[i] & key_sets[j])
            s = inter / union if union > 0 else 1.0
            matrix[i][j] = s
            matrix[j][i] = s
    np.fill_diagonal(matrix, 1.0)
    fk_scores = [float(np.mean([matrix[k][j] for j in range(N) if j != k])) for k in range(N)]
    vc_scores = []
    all_keys = Counter()
    for ks in key_sets:
        for k in ks:
            all_keys[k] += 1
    for i, ks in enumerate(key_sets):
        if not ks:
            vc_scores.append(0.0)
        else:
            vc_scores.append(float(np.mean([all_keys[k] / N for k in ks])))
    em_scores = []
    for i in range(N):
        em_scores.append(sum(1 for j in range(N) if key_sets[j] == key_sets[i]) / N)
    return fk_scores, vc_scores, em_scores


def compute_selection_f1_all(instances, subtask):
    greedy_f1s, oracle_f1s = [], []
    sel_f1 = {"SJ": [], "FK": [], "VC": [], "EM": [], "LP": []}
    n_degenerate = 0
    n_total = 0

    for inst in instances:
        samples = inst["samples"]
        gold = inst["gold"]
        greedy = inst.get("greedy", samples[0])
        g_f1 = per_instance_f1(greedy, gold, subtask=subtask)
        greedy_f1s.append(g_f1)

        sample_f1s = [per_instance_f1(s, gold, subtask=subtask) for s in samples]
        oracle_f1s.append(max(sample_f1s))

        # Degeneracy: all samples have same F1
        if len(set(round(f, 6) for f in sample_f1s)) == 1:
            n_degenerate += 1
        n_total += 1

        # Per-sample signals
        sj_scores = compute_sample_sj_scores(inst, subtask)
        fk_scores, vc_scores, em_scores = compute_sample_surface_scores(inst, subtask)
        lp_scores = [s.get("mean_logprob", float("-inf")) for s in samples]
        lp_scores = [lp if np.isfinite(lp) else float("-inf") for lp in lp_scores]

        for sig_name, sig_scores in [("SJ", sj_scores), ("FK", fk_scores),
                                      ("VC", vc_scores), ("EM", em_scores), ("LP", lp_scores)]:
            best_idx = int(np.argmax(sig_scores))
            sel_f1[sig_name].append(sample_f1s[best_idx])

    return {
        "greedy_f1": float(np.mean(greedy_f1s)),
        "oracle_f1": float(np.mean(oracle_f1s)),
        "oracle_headroom": float(np.mean(oracle_f1s) - np.mean(greedy_f1s)),
        "degeneracy_rate": n_degenerate / n_total if n_total > 0 else 0,
        "n_degenerate": n_degenerate,
        "n_total": n_total,
        "selection_f1": {k: float(np.mean(v)) for k, v in sel_f1.items()},
    }


def evaluate_subtask(instances, subtask):
    entity_key = "entities" if subtask == "ner" else "relations"
    valid = [inst for inst in instances if len(inst["gold"].get(entity_key, [])) > 0]

    greedy_f1s_all = []
    for inst in valid:
        greedy = inst.get("greedy", inst["samples"][0])
        greedy_f1s_all.append(per_instance_f1(greedy, inst["gold"], subtask=subtask))
    conditional = [inst for inst, f1 in zip(valid, greedy_f1s_all) if f1 > 0]
    print(f"\n=== {subtask.upper()} === Valid: {len(valid)}, Conditional: {len(conditional)}")

    results = {}
    for split_name, split_instances in [("full", valid), ("conditional", conditional)]:
        print(f"\n--- {split_name} ({len(split_instances)} instances) ---")
        consistency = compute_all_consistency_scores(split_instances, subtask=subtask)
        sj_vals = consistency["soft_jaccard"]
        fk_vals = consistency["fleiss_kappa"]

        lp_vals, em_vals, vc_vals, f1_vals = [], [], [], []
        for inst in split_instances:
            samples = inst["samples"]
            gold = inst["gold"]
            greedy = inst.get("greedy", samples[0])
            lp_vals.append(compute_mean_logprob(samples))
            em_vals.append(compute_exact_match_rate(samples, subtask))
            vc_vals.append(compute_voting_confidence(samples, subtask))
            f1_vals.append(per_instance_f1(greedy, gold, subtask=subtask))

        signals = {
            "SJ": np.array(sj_vals, dtype=float),
            "FK": np.array(fk_vals, dtype=float),
            "LP": np.array(lp_vals, dtype=float),
            "EM": np.array(em_vals, dtype=float),
            "VC": np.array(vc_vals, dtype=float),
        }
        f1_arr = np.array(f1_vals, dtype=float)
        binary_correct = (f1_arr >= 1.0).astype(int)

        baseline = BASELINE_R32.get(subtask, {}).get(split_name if split_name == "full" else "cond", {})

        split_results = {"n": len(split_instances), "greedy_f1_mean": float(np.mean(f1_vals))}
        metrics = {}
        for sig_name, sig_vals in signals.items():
            rho = safe_spearman(sig_vals, f1_arr)
            tau = safe_kendall(sig_vals, f1_arr)
            auroc = safe_auroc(sig_vals, binary_correct)
            baseline_rho = baseline.get(sig_name, float("nan"))
            delta = rho - baseline_rho if np.isfinite(baseline_rho) else float("nan")
            metrics[sig_name] = {"rho": round(rho, 4), "tau": round(tau, 4),
                                  "AUROC": round(auroc, 4), "delta_vs_r16": round(delta, 4)}
            print(f"  {sig_name:>5}: rho={rho:.4f}  tau={tau:.4f}  AUROC={auroc:.4f}  Δr16={delta:+.4f}")

        split_results["metrics"] = metrics

        # Selection F1 (only for full split)
        if split_name == "full":
            sel = compute_selection_f1_all(split_instances, subtask)
            split_results["selection"] = sel
            print(f"\n  Greedy F1:   {sel['greedy_f1']:.4f}")
            print(f"  Oracle F1:   {sel['oracle_f1']:.4f}  (headroom={sel['oracle_headroom']:.4f})")
            print(f"  Degeneracy:  {sel['degeneracy_rate']:.3f} ({sel['n_degenerate']}/{sel['n_total']})")
            for sig in ["SJ", "FK", "VC", "EM", "LP"]:
                sf1 = sel["selection_f1"][sig]
                delta_g = sf1 - sel["greedy_f1"]
                bl_key = f"sel_{sig}"
                bl_val = baseline.get(bl_key, float("nan"))
                delta_bl = sf1 - bl_val if np.isfinite(bl_val) else float("nan")
                print(f"  Sel {sig:>3}: {sf1:.4f}  Δgreedy={delta_g:+.4f}  Δr16={delta_bl:+.4f}" if np.isfinite(delta_bl) else f"  Sel {sig:>3}: {sf1:.4f}  Δgreedy={delta_g:+.4f}")

        results[split_name] = split_results

    return results


def generate_comparison_report(all_results):
    lines = ["# exp_023 LoRA rank=8 Analysis Report", ""]
    lines.append("## Configuration")
    lines.append("- Model: Qwen3-8B, LoRA r=8, α=16")
    lines.append("- Training: 5 epochs, 585 steps, train_loss=0.1018")
    lines.append("- Inference: N=8, T=1.0, seed=42, joint NER+RE")
    lines.append("- Baseline: rank=16 (ft_002_v2 / exp_012_rerun_1024)")
    lines.append("")

    for subtask in SUBTASKS:
        if subtask not in all_results:
            continue
        res = all_results[subtask]
        lines.append(f"## {subtask.upper()}")
        lines.append("")

        # Correlation table
        lines.append("### Correlation (ρ) & AUROC")
        lines.append("")
        lines.append("| Signal | ρ (full) | AUROC (full) | Δρ vs r16 | ρ (cond) | AUROC (cond) | Δρ cond |")
        lines.append("|--------|----------|-------------|-----------|----------|-------------|---------|")
        for sig in ["SJ", "FK", "VC", "EM", "LP"]:
            fm = res["full"]["metrics"][sig]
            cm = res["conditional"]["metrics"][sig]
            lines.append(f"| {sig} | {fm['rho']:.4f} | {fm['AUROC']:.4f} | {fm['delta_vs_r16']:+.4f} | {cm['rho']:.4f} | {cm['AUROC']:.4f} | {cm['delta_vs_r16']:+.4f} |")
        lines.append("")

        # Selection F1 table
        if "selection" in res["full"]:
            sel = res["full"]["selection"]
            lines.append("### Selection F1")
            lines.append("")
            lines.append(f"- Greedy F1: {sel['greedy_f1']:.4f}")
            lines.append(f"- Oracle F1: {sel['oracle_f1']:.4f} (headroom: {sel['oracle_headroom']:.4f})")
            lines.append(f"- Degeneracy: {sel['degeneracy_rate']:.1%} ({sel['n_degenerate']}/{sel['n_total']})")
            lines.append("")
            lines.append("| Signal | Selection F1 | Δ greedy |")
            lines.append("|--------|-------------|----------|")
            for sig in ["SJ", "FK", "VC", "EM", "LP"]:
                sf1 = sel["selection_f1"][sig]
                delta = sf1 - sel["greedy_f1"]
                lines.append(f"| {sig} | {sf1:.4f} | {delta:+.4f} |")
            lines.append("")

        lines.append(f"n_full={res['full']['n']}, n_cond={res['conditional']['n']}")
        lines.append("")

    return "\n".join(lines)


def main():
    instances = load_data(DATA_PATH)
    print(f"Loaded {len(instances)} instances, N={len(instances[0]['samples'])}")

    all_results = {}
    for subtask in SUBTASKS:
        all_results[subtask] = evaluate_subtask(instances, subtask)

    def json_default(obj):
        if isinstance(obj, (np.floating, np.float64, np.float32)):
            return float(obj)
        if isinstance(obj, (np.integer, np.int64, np.int32)):
            return int(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, np.bool_):
            return bool(obj)
        return str(obj)

    out_json = f"{OUTPUT_DIR}/all_signals_5signal.json"
    with open(out_json, "w") as f:
        json.dump(all_results, f, indent=2, default=json_default)
    print(f"\nSaved JSON: {out_json}")

    report = generate_comparison_report(all_results)
    out_md = f"{OUTPUT_DIR}/comparison.md"
    with open(out_md, "w") as f:
        f.write(report)
    print(f"Saved report: {out_md}")


if __name__ == "__main__":
    main()
