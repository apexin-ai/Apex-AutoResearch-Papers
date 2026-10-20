#!/usr/bin/env python3
"""Compute 5 confidence signals + entity construction pipeline for NER.

Signals: LP (Log Probability), SJ (Soft Jaccard), FK (Fleiss Kappa),
         VC (Vote Count), EM (Exact Match Rate)
Construction: greedy, LP selection, majority vote, consensus θ=2/N,
              LP-weighted construction (high=0.5, medium=2/N), oracle

Usage:
    # Process all datasets under a model output directory
    python compute_signals.py --input-dir /path/to/output/72b_zeroshot

    # Process specific dataset with model metadata
    python compute_signals.py --input-dir /path/to/output/7b_ft \
        --dataset scierc --model-size 7 --regime ft

    # Custom output directory
    python compute_signals.py --input-dir /path/to/output/72b_zeroshot \
        --output-dir /path/to/results

Expected input: <input-dir>/<dataset>/samples.jsonl  (or <input-dir>/samples.jsonl)
Output: full_signal_report.json + <dataset>_per_instance.json per dataset
"""

import argparse
import json
import math
import os
import statistics
import sys
from collections import Counter, defaultdict

import numpy as np
from scipy.stats import spearmanr

CODE_DIR = os.environ.get(
    "STRUCT_CODE_DIR",
    "/root/autodl-tmp/struct_self_consist_ie/code",
)
if os.path.isdir(CODE_DIR):
    sys.path.insert(0, CODE_DIR)

try:
    from consistency import fleiss_kappa_surface, structural_consistency_soft_jaccard
    HAS_CONSISTENCY = True
except ImportError:
    HAS_CONSISTENCY = False
    print("WARNING: consistency module not found; SJ/FK signals will be skipped")


# ---------------------------------------------------------------------------
# Core metrics
# ---------------------------------------------------------------------------

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


def compute_degeneracy_f1(inst):
    """Constant-F1 degeneracy: all N samples have identical F1 against gold."""
    gold_ents = inst["gold"]["entities"]
    f1s = [compute_entity_f1(s.get("entities", []), gold_ents)
           for s in inst["samples"]]
    return len(set(round(f, 10) for f in f1s)) <= 1


def compute_degeneracy_set(inst):
    """Entity-set degeneracy: all N samples produce identical entity sets."""
    key_sets = set()
    for s in inst["samples"]:
        ks = frozenset((e["start"], e["end"], e["type"])
                       for e in s.get("entities", []))
        key_sets.add(ks)
    return len(key_sets) == 1


# ---------------------------------------------------------------------------
# Signal computation
# ---------------------------------------------------------------------------

def compute_mean_logprob(samples, inst):
    lps = []
    for i, s in enumerate(samples):
        lp = s.get("mean_logprob")
        if lp is None and "logprobs" in inst and i < len(inst["logprobs"]):
            lp = inst["logprobs"][i]
        if lp is not None and np.isfinite(lp):
            lps.append(lp)
    return float(np.mean(lps)) if lps else float("nan")


def compute_exact_match_rate(samples):
    keys = [frozenset((e["text"], e["type"]) for e in s.get("entities", []))
            for s in samples]
    if not keys:
        return 0.0
    counter = Counter(keys)
    return counter.most_common(1)[0][1] / len(samples)


def compute_voting_confidence(samples):
    N = len(samples)
    if N == 0:
        return 0.0
    counter = Counter()
    for s in samples:
        for e in s.get("entities", []):
            counter[(e["text"], e["type"])] += 1
    if not counter:
        return 0.0
    return float(np.mean([v / N for v in counter.values()]))


def safe_spearman(x, y):
    x, y = np.asarray(x, dtype=float), np.asarray(y, dtype=float)
    mask = np.isfinite(x) & np.isfinite(y)
    x, y = x[mask], y[mask]
    if len(x) < 3:
        return float("nan")
    return float(spearmanr(x, y).statistic)


# ---------------------------------------------------------------------------
# Construction pipeline
# ---------------------------------------------------------------------------

def consensus_construct(inst, high_thresh=0.5, medium_thresh=0.25):
    """LP-weighted entity construction with two-tier thresholding.

    Entities with freq > high_thresh are auto-included.
    Entities with freq in (medium_thresh, high_thresh] are included only if
    their contributing samples' mean LP exceeds the instance median LP.
    """
    samples = inst["samples"]
    N = len(samples)

    entity_counts = Counter()
    entity_sample_indices = defaultdict(list)
    for i, s in enumerate(samples):
        seen = set()
        for e in s.get("entities", []):
            key = (e["start"], e["end"], e["type"])
            if key not in seen:
                entity_counts[key] += 1
                entity_sample_indices[key].append(i)
                seen.add(key)

    sample_lps = []
    for i, s in enumerate(samples):
        lp = s.get("mean_logprob")
        if lp is None and "logprobs" in inst and i < len(inst["logprobs"]):
            lp = inst["logprobs"][i]
        if lp is not None:
            sample_lps.append(lp)
    instance_median_lp = statistics.median(sample_lps) if sample_lps else 0.0

    consensus = []
    for entity_key, count in entity_counts.items():
        freq = count / N
        if freq > high_thresh:
            consensus.append(entity_key)
        elif freq > medium_thresh:
            contributing_lps = []
            for i in entity_sample_indices[entity_key]:
                lp = samples[i].get("mean_logprob")
                if lp is None and "logprobs" in inst and i < len(inst["logprobs"]):
                    lp = inst["logprobs"][i]
                if lp is not None:
                    contributing_lps.append(lp)
            if contributing_lps:
                mean_lp = statistics.mean(contributing_lps)
                if mean_lp > instance_median_lp:
                    consensus.append(entity_key)

    return [{"start": s, "end": e, "type": t} for s, e, t in consensus]


def majority_vote_span(inst, threshold=0.5):
    samples = inst["samples"]
    N = len(samples)
    entity_counts = Counter()
    for s in samples:
        seen = set()
        for e in s.get("entities", []):
            key = (e["start"], e["end"], e["type"])
            if key not in seen:
                entity_counts[key] += 1
                seen.add(key)
    return [{"start": k[0], "end": k[1], "type": k[2]}
            for k, c in entity_counts.items() if c / N > threshold]


# ---------------------------------------------------------------------------
# Data loading & helpers
# ---------------------------------------------------------------------------

def load_data(path, gold_filter=True):
    instances = []
    with open(path) as f:
        for line in f:
            if not line.strip():
                continue
            obj = json.loads(line)
            if gold_filter and not obj["gold"].get("entities", []):
                continue
            instances.append(obj)
    return instances


def bootstrap_ci(values, n_boot=2000, seed=42):
    arr = np.array(values)
    n = len(arr)
    if n == 0:
        return {"mean": 0.0, "ci_lo": 0.0, "ci_hi": 0.0}
    rng = np.random.RandomState(seed)
    boot_means = np.array([arr[rng.randint(0, n, n)].mean() for _ in range(n_boot)])
    boot_means.sort()
    return {
        "mean": float(arr.mean()),
        "ci_lo": float(boot_means[int(0.025 * n_boot)]),
        "ci_hi": float(boot_means[int(0.975 * n_boot)]),
    }


# ---------------------------------------------------------------------------
# Main evaluation
# ---------------------------------------------------------------------------

def evaluate_dataset(name, path, subtask="ner"):
    """Full signal + construction analysis on one dataset."""
    print(f"\n{'='*60}")
    print(f"  {name}")
    print(f"{'='*60}")

    instances = load_data(path, gold_filter=True)
    print(f"  Loaded {len(instances)} instances (gold-filtered)")
    if not instances:
        return None

    N_samples = len(instances[0]["samples"])

    # --- 5 signals ---
    sj_vals, fk_vals = [], []
    if HAS_CONSISTENCY:
        for inst in instances:
            sj_vals.append(structural_consistency_soft_jaccard(
                inst["samples"], subtask=subtask))
            fk_vals.append(fleiss_kappa_surface(
                inst["samples"], subtask=subtask))

    lp_vals, em_vals, vc_vals, f1_vals = [], [], [], []
    for inst in instances:
        samples = inst["samples"]
        gold = inst["gold"]
        greedy = inst.get("greedy", samples[0])
        lp_vals.append(compute_mean_logprob(samples, inst))
        em_vals.append(compute_exact_match_rate(samples))
        vc_vals.append(compute_voting_confidence(samples))
        f1_vals.append(compute_entity_f1(
            greedy.get("entities", []), gold["entities"]))

    signals = {
        "LP": np.array(lp_vals, dtype=float),
        "EM": np.array(em_vals, dtype=float),
        "VC": np.array(vc_vals, dtype=float),
    }
    if HAS_CONSISTENCY:
        signals["SJ"] = np.array(sj_vals, dtype=float)
        signals["FK"] = np.array(fk_vals, dtype=float)

    f1_arr = np.array(f1_vals, dtype=float)

    signal_results = {}
    for sig_name in ["SJ", "FK", "LP", "EM", "VC"]:
        if sig_name in signals:
            signal_results[sig_name] = {
                "rho": safe_spearman(signals[sig_name], f1_arr)
            }

    # --- Baselines & construction ---
    greedy_f1s = f1_vals
    oracle_f1s, lp_selection_f1s = [], []

    for inst in instances:
        gold_ents = inst["gold"]["entities"]
        sample_f1s = [compute_entity_f1(s.get("entities", []), gold_ents)
                      for s in inst["samples"]]
        oracle_f1s.append(max(sample_f1s))

        best_lp_idx, best_lp = 0, float("-inf")
        for i, s in enumerate(inst["samples"]):
            lp = s.get("mean_logprob")
            if lp is None and "logprobs" in inst and i < len(inst["logprobs"]):
                lp = inst["logprobs"][i]
            if lp is not None and lp > best_lp:
                best_lp = lp
                best_lp_idx = i
        lp_selection_f1s.append(compute_entity_f1(
            inst["samples"][best_lp_idx].get("entities", []), gold_ents))

    mv_f1s = [compute_entity_f1(majority_vote_span(inst),
              inst["gold"]["entities"]) for inst in instances]

    theta = 2 / N_samples
    consensus_2n_f1s = [compute_entity_f1(
        consensus_construct(inst, high_thresh=theta, medium_thresh=0.0),
        inst["gold"]["entities"]) for inst in instances]

    consensus_lp_f1s = [compute_entity_f1(
        consensus_construct(inst, high_thresh=0.5, medium_thresh=theta),
        inst["gold"]["entities"]) for inst in instances]

    # --- Degeneracy (constant-F1 definition for scaling curve) ---
    degen_f1_flags = [compute_degeneracy_f1(inst) for inst in instances]
    n_degen_f1 = sum(degen_f1_flags)
    degen_rate = n_degen_f1 / len(instances) if instances else 0.0

    # Entity-set degeneracy (for bootstrap stratification)
    degen_set_flags = [compute_degeneracy_set(inst) for inst in instances]
    n_degen_set = sum(degen_set_flags)

    result = {
        "name": name,
        "n_instances": len(instances),
        "n_samples": N_samples,
        "signals": signal_results,
        "baselines": {
            "greedy": bootstrap_ci(greedy_f1s),
            "lp_selection": bootstrap_ci(lp_selection_f1s),
            "majority_vote": bootstrap_ci(mv_f1s),
            "oracle": bootstrap_ci(oracle_f1s),
            "consensus_theta2n": bootstrap_ci(consensus_2n_f1s),
            "consensus_lp_weighted": bootstrap_ci(consensus_lp_f1s),
        },
        "consensus_variants": {},
        "degeneracy_rate": degen_rate,
        "degeneracy_count": n_degen_f1,
        "degeneracy_set_count": n_degen_set,
        "lp_selection_delta": float(np.mean(lp_selection_f1s) - np.mean(greedy_f1s)),
    }

    # Additional threshold configs
    for cfg in [{"high": 0.5, "medium": 0.1},
                {"high": 0.6, "medium": 0.2},
                {"high": 0.7, "medium": 0.3}]:
        key = f"high={cfg['high']}_medium={cfg['medium']}"
        cc_f1s = [compute_entity_f1(
            consensus_construct(inst, high_thresh=cfg["high"],
                                medium_thresh=cfg["medium"]),
            inst["gold"]["entities"]) for inst in instances]
        result["consensus_variants"][key] = bootstrap_ci(cc_f1s)

    # --- Print summary ---
    print(f"  N={N_samples}")
    print(f"\n  Signal correlations (Spearman rho vs greedy F1):")
    for sig in ["LP", "SJ", "FK", "VC", "EM"]:
        if sig in signal_results:
            print(f"    {sig:4s}: rho={signal_results[sig]['rho']:.4f}")

    print(f"\n  Entity F1 (mean [95% CI]):")
    for label, key in [("Greedy", "greedy"), ("LP Selection", "lp_selection"),
                       ("Majority Vote", "majority_vote"),
                       ("Consensus theta=2/N", "consensus_theta2n"),
                       ("Consensus LP-wt", "consensus_lp_weighted"),
                       ("Oracle", "oracle")]:
        ci = result["baselines"][key]
        print(f"    {label:25s} {ci['mean']:.4f}  "
              f"[{ci['ci_lo']:.4f}, {ci['ci_hi']:.4f}]")

    print(f"\n  Degeneracy (constant-F1): {n_degen_f1}/{len(instances)} "
          f"({degen_rate*100:.1f}%)")
    print(f"  Degeneracy (entity-set):  {n_degen_set}/{len(instances)} "
          f"({n_degen_set/len(instances)*100:.1f}%)")

    # Attach per-instance arrays (for bootstrap script)
    result["_per_instance"] = {
        "greedy_f1": greedy_f1s,
        "construction_lp_f1": consensus_lp_f1s,
        "oracle_f1": oracle_f1s,
        "degenerate": degen_set_flags,
    }

    return result


def find_datasets(input_dir):
    """Auto-detect dataset directories under input_dir."""
    datasets = {}
    for name in ["scierc", "conll2003", "fewnerd"]:
        path = os.path.join(input_dir, name, "samples.jsonl")
        if os.path.exists(path):
            datasets[name] = path
    top_path = os.path.join(input_dir, "samples.jsonl")
    if os.path.exists(top_path) and not datasets:
        ds_name = os.path.basename(input_dir)
        for known in ["scierc", "conll", "fewnerd"]:
            if known in ds_name.lower():
                ds_name = known
                break
        datasets[ds_name] = top_path
    return datasets


def main():
    parser = argparse.ArgumentParser(
        description="Compute 5 signals + construction pipeline")
    parser.add_argument("--input-dir", required=True,
                        help="Model output directory")
    parser.add_argument("--output-dir", default=None,
                        help="Output directory (default: input-dir)")
    parser.add_argument("--dataset", default=None, nargs="+",
                        help="Dataset(s) to process (default: auto-detect)")
    parser.add_argument("--model-size", default=None,
                        help="Model size label (e.g. 7, 14, 32, 72)")
    parser.add_argument("--regime", default=None, choices=["ft", "zs", "fs"],
                        help="Training regime")
    args = parser.parse_args()

    output_dir = args.output_dir or args.input_dir
    os.makedirs(output_dir, exist_ok=True)

    datasets = find_datasets(args.input_dir)
    if args.dataset:
        datasets = {k: v for k, v in datasets.items() if k in args.dataset}

    if not datasets:
        print(f"ERROR: No samples.jsonl found under {args.input_dir}")
        sys.exit(1)

    all_results = {}
    for ds_name, path in sorted(datasets.items()):
        result = evaluate_dataset(ds_name, path)
        if result:
            if args.model_size:
                result["model_size"] = args.model_size
            if args.regime:
                result["regime"] = args.regime
            all_results[ds_name] = result

    # Save report (without bulky per-instance arrays)
    report = {}
    for ds_name, r in all_results.items():
        report[ds_name] = {k: v for k, v in r.items() if k != "_per_instance"}

    report_path = os.path.join(output_dir, "full_signal_report.json")
    with open(report_path, "w") as f:
        json.dump(report, f, indent=2, default=str)
    print(f"\nReport saved to {report_path}")

    # Save per-instance arrays for downstream bootstrap analysis
    for ds_name, r in all_results.items():
        pi = r.get("_per_instance")
        if pi:
            pi_path = os.path.join(output_dir,
                                   f"{ds_name}_per_instance.json")
            with open(pi_path, "w") as f:
                json.dump(pi, f)
            print(f"Per-instance data: {pi_path}")


if __name__ == "__main__":
    main()
