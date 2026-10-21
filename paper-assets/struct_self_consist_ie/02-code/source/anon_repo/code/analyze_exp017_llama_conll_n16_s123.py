#!/usr/bin/env python3
"""exp_017_llama_conll_n16: 5-signal evaluation + N=8 vs N=16 delta + Best-of-N selection."""

import json, sys, os
import numpy as np
from scipy.stats import spearmanr, kendalltau, rankdata
from collections import Counter

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from consistency import compute_all_consistency_scores, _ner_soft_jaccard_pair
from evaluation import per_instance_f1

N16_PATH = "/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_n16_s123/samples.jsonl"
N8_PATH = "/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_infer/samples.jsonl"
N8_REPORT = "/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_infer/all_signals_report.json"
OUTPUT_DIR = "/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_n16_s123"
SUBTASK = "ner"


def load_data(path):
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]


def compute_exact_match_rate(samples, subtask):
    keys = [frozenset((e["text"], e["type"]) for e in s.get("entities", [])) for s in samples]
    if not keys: return 0.0
    c = Counter(keys)
    return c.most_common(1)[0][1] / len(samples)


def compute_voting_confidence(samples, subtask):
    N = len(samples)
    if N == 0: return 0.0
    counter = Counter()
    for s in samples:
        for e in s.get("entities", []):
            counter[(e["text"], e["type"])] += 1
    if not counter: return 0.0
    return float(np.mean([v / N for v in counter.values()]))


def compute_mean_logprob(samples):
    lps = [s.get("mean_logprob") for s in samples if s.get("mean_logprob") is not None]
    lps = [lp for lp in lps if np.isfinite(lp)]
    return float(np.mean(lps)) if lps else float("nan")


def safe_spearman(x, y):
    x, y = np.asarray(x, float), np.asarray(y, float)
    m = np.isfinite(x) & np.isfinite(y)
    x, y = x[m], y[m]
    if len(x) < 3: return float("nan"), float("nan")
    r = spearmanr(x, y)
    return float(r.statistic), float(r.pvalue)


def safe_auroc(scores, labels):
    scores, labels = np.asarray(scores, float), np.asarray(labels, int)
    if len(np.unique(labels)) < 2: return float("nan")
    n_pos, n_neg = (labels==1).sum(), (labels==0).sum()
    if n_pos == 0 or n_neg == 0: return float("nan")
    ranks = rankdata(scores)
    u = ranks[labels==1].sum() - n_pos*(n_pos+1)/2
    return float(u / (n_pos * n_neg))


def normalize_for_ece(sig_name, values):
    v = np.asarray(values, dtype=float)
    if sig_name in ("SJ", "EM", "voting_conf"):
        return np.clip(v, 0, 1)
    elif sig_name == "FK":
        return np.clip((v + 1) / 2, 0, 1)
    elif sig_name == "logprob":
        return np.clip(np.exp(v), 0, 1)
    return v


def compute_ece(confidences, correctness, n_bins=10):
    conf = np.asarray(confidences, dtype=float)
    corr = np.asarray(correctness, dtype=float)
    mask = np.isfinite(conf)
    conf, corr = conf[mask], corr[mask]
    if len(conf) == 0: return float("nan")
    bin_edges = np.linspace(0, 1, n_bins + 1)
    ece = 0.0
    for i in range(n_bins):
        lo, hi = bin_edges[i], bin_edges[i + 1]
        in_bin = (conf >= lo) & (conf <= hi if i == n_bins - 1 else conf < hi)
        if in_bin.sum() == 0: continue
        ece += in_bin.sum() / len(conf) * abs(conf[in_bin].mean() - corr[in_bin].mean())
    return float(ece)


def bootstrap_metric(metric_fn, signals, targets, n_boot=1000, seed=42):
    rng = np.random.RandomState(seed)
    signals, targets = np.asarray(signals, float), np.asarray(targets, float)
    n = len(signals)
    vals = []
    for _ in range(n_boot):
        idx = rng.randint(0, n, size=n)
        v = metric_fn(signals[idx], targets[idx])
        if isinstance(v, tuple): v = v[0]
        if np.isfinite(v): vals.append(v)
    if not vals: return [float("nan"), float("nan")]
    return [float(np.percentile(vals, 2.5)), float(np.percentile(vals, 97.5))]


def analyze_split(instances, split_name):
    consistency = compute_all_consistency_scores(instances, subtask=SUBTASK)
    sj_vals = consistency["soft_jaccard"]
    fk_vals = consistency["fleiss_kappa"]

    lp_vals, em_vals, vc_vals, f1_vals = [], [], [], []
    for inst in instances:
        samples = inst["samples"]
        greedy = inst.get("greedy", samples[0])
        lp_vals.append(compute_mean_logprob(samples))
        em_vals.append(compute_exact_match_rate(samples, SUBTASK))
        vc_vals.append(compute_voting_confidence(samples, SUBTASK))
        f1_vals.append(per_instance_f1(greedy, inst["gold"], subtask=SUBTASK))

    signals = {"SJ": np.array(sj_vals), "FK": np.array(fk_vals),
               "logprob": np.array(lp_vals), "EM": np.array(em_vals),
               "voting_conf": np.array(vc_vals)}
    f1_arr = np.array(f1_vals)
    binary = (f1_arr >= 1.0).astype(int)

    result = {"n": len(instances), "pct_perfect": float(binary.mean()),
              "greedy_f1_mean": round(float(np.mean(f1_vals)), 4)}
    metrics = {}
    for name, vals in signals.items():
        rho, p = safe_spearman(vals, f1_arr)
        rho_ci = bootstrap_metric(lambda x,y: safe_spearman(x,y)[0], vals, f1_arr)
        auroc = safe_auroc(vals, binary)
        auroc_ci = bootstrap_metric(safe_auroc, vals, binary.astype(float))
        ece_conf = normalize_for_ece(name, vals)
        ece = compute_ece(ece_conf, binary)
        metrics[name] = {
            "rho": round(rho, 4), "rho_ci95": [round(v, 4) for v in rho_ci], "p_rho": p,
            "auroc": round(auroc, 4), "auroc_ci95": [round(v, 4) for v in auroc_ci],
            "ece": round(ece, 4)
        }
        print(f"  {name:>12}: rho={rho:.4f} [{rho_ci[0]:.4f},{rho_ci[1]:.4f}]  AUROC={auroc:.4f}  ECE={ece:.4f}")
    result["metrics"] = metrics
    return result, signals, f1_arr


def best_of_n_selection(instances, signals_dict, f1_arr):
    per_sample_f1s = []
    for inst in instances:
        sf = [per_instance_f1(s, inst["gold"], subtask=SUBTASK) for s in inst["samples"]]
        per_sample_f1s.append(sf)

    greedy_f1s = [per_instance_f1(inst.get("greedy", inst["samples"][0]), inst["gold"], subtask=SUBTASK) for inst in instances]
    greedy_mean = float(np.mean(greedy_f1s))

    random_f1s = [float(np.mean(sf)) if sf else 0.0 for sf in per_sample_f1s]
    random_mean = float(np.mean(random_f1s))

    oracle_f1s = [max(sf) if sf else 0.0 for sf in per_sample_f1s]
    oracle_mean = float(np.mean(oracle_f1s))

    # SJ-best: pick sample with highest mean pairwise SJ
    sj_selected = []
    for idx, inst in enumerate(instances):
        samples = inst["samples"]
        n = len(samples)
        if n <= 1:
            sj_selected.append(per_sample_f1s[idx][0] if per_sample_f1s[idx] else 0.0)
            continue
        best_k, best_score = 0, -1
        for k in range(n):
            pw = []
            for j in range(n):
                if j == k: continue
                sim = _ner_soft_jaccard_pair(samples[k].get("entities", []), samples[j].get("entities", []))
                pw.append(sim)
            score = float(np.mean(pw))
            if score > best_score:
                best_score = score
                best_k = k
        sj_selected.append(per_sample_f1s[idx][best_k])
    sj_mean = float(np.mean(sj_selected))

    # Logprob-best: pick sample with highest mean_logprob
    lp_selected = []
    for idx, inst in enumerate(instances):
        samples = inst["samples"]
        lps = [s.get("mean_logprob", float("-inf")) for s in samples]
        best_k = int(np.argmax(lps))
        lp_selected.append(per_sample_f1s[idx][best_k])
    lp_mean = float(np.mean(lp_selected))

    # Voting-conf-best: pick sample with highest entity voting agreement
    vc_selected = []
    for idx, inst in enumerate(instances):
        samples = inst["samples"]
        n = len(samples)
        entity_counter = Counter()
        for s in samples:
            for e in s.get("entities", []):
                entity_counter[(e["text"], e["type"])] += 1
        best_k, best_score = 0, -1
        for k, s in enumerate(samples):
            ents = [(e["text"], e["type"]) for e in s.get("entities", [])]
            if not ents:
                score = 0.0
            else:
                score = float(np.mean([entity_counter[e] / n for e in ents]))
            if score > best_score:
                best_score = score
                best_k = k
        vc_selected.append(per_sample_f1s[idx][best_k])
    vc_mean = float(np.mean(vc_selected))

    methods = {
        "greedy": round(greedy_mean, 4),
        "random_avg": round(random_mean, 4),
        "sj_best": round(sj_mean, 4),
        "logprob_best": round(lp_mean, 4),
        "voting_conf_best": round(vc_mean, 4),
        "oracle": round(oracle_mean, 4),
    }
    return methods


def compute_n8_delta(n8_report, n16_results):
    delta = {}
    for split in ["full", "conditional"]:
        if split not in n8_report or split not in n16_results:
            continue
        n8_m = n8_report[split]["metrics"]
        n16_m = n16_results[split]["metrics"]
        d = {}
        for sig in ["SJ", "FK", "logprob", "EM", "voting_conf"]:
            if sig in n8_m and sig in n16_m:
                n8_rho = n8_m[sig]["rho"]["value"] if isinstance(n8_m[sig]["rho"], dict) else n8_m[sig]["rho"]
                n16_rho = n16_m[sig]["rho"]
                n8_auroc = n8_m[sig]["AUROC"]["value"] if isinstance(n8_m[sig]["AUROC"], dict) else n8_m[sig].get("auroc", n8_m[sig].get("AUROC", 0))
                n16_auroc = n16_m[sig]["auroc"]
                d[sig] = {
                    "rho_n8": round(n8_rho, 4), "rho_n16": round(n16_rho, 4),
                    "rho_delta": round(n16_rho - n8_rho, 4),
                    "auroc_n8": round(n8_auroc, 4), "auroc_n16": round(n16_auroc, 4),
                    "auroc_delta": round(n16_auroc - n8_auroc, 4),
                }
        delta[split] = d
    return delta


def main():
    print("Loading N=16 data...")
    instances = load_data(N16_PATH)
    print(f"Loaded {len(instances)} instances, N={len(instances[0]['samples'])}")

    valid = [inst for inst in instances if len(inst["gold"].get("entities", [])) > 0]
    print(f"Valid (non-empty gold): {len(valid)}")

    greedy_f1s_all = []
    for inst in valid:
        greedy = inst.get("greedy", inst["samples"][0])
        greedy_f1s_all.append(per_instance_f1(greedy, inst["gold"], subtask=SUBTASK))
    conditional = [inst for inst, f1 in zip(valid, greedy_f1s_all) if f1 > 0]
    print(f"Conditional (greedy F1 > 0): {len(conditional)}")

    results = {}

    # 5-signal evaluation
    for split_name, split_insts in [("full", valid), ("conditional", conditional)]:
        print(f"\n--- {split_name} ({len(split_insts)} instances) ---")
        res, signals, f1_arr = analyze_split(split_insts, split_name)
        results[split_name] = res

    # Best-of-N selection
    print("\n--- Best-of-N Selection (full split) ---")
    bon = best_of_n_selection(valid, None, None)
    for method, f1_val in bon.items():
        print(f"  {method:>20}: {f1_val:.4f}")
    results["best_of_n"] = bon

    # N=8 vs N=16 delta
    if os.path.exists(N8_REPORT):
        print("\n--- N=8 vs N=16 Delta ---")
        with open(N8_REPORT) as f:
            n8_report = json.load(f)
        delta = compute_n8_delta(n8_report, results)
        for split, sigs in delta.items():
            print(f"  [{split}]")
            for sig, d in sigs.items():
                print(f"    {sig:>12}: rho {d['rho_n8']:.4f} -> {d['rho_n16']:.4f} (Δ={d['rho_delta']:+.4f})  "
                      f"AUROC {d['auroc_n8']:.4f} -> {d['auroc_n16']:.4f} (Δ={d['auroc_delta']:+.4f})")
        results["n8_vs_n16_delta"] = delta
    else:
        print(f"N=8 report not found at {N8_REPORT}, skipping delta")

    # Save
    def json_default(obj):
        if isinstance(obj, (np.floating, np.float64, np.float32)): return float(obj)
        if isinstance(obj, (np.integer, np.int64, np.int32)): return int(obj)
        if isinstance(obj, np.ndarray): return obj.tolist()
        if isinstance(obj, np.bool_): return bool(obj)
        return str(obj)

    out_path = os.path.join(OUTPUT_DIR, "all_signals_report.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2, default=json_default)
    print(f"\nSaved to {out_path}")


if __name__ == "__main__":
    main()
