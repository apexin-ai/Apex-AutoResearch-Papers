"""Three-layer FewRel analysis: pairwise SCS-confusion, per-type accuracy vs BCS, batch-level accuracy vs BCS.

Adapted from analyze_maven_results.py for relation extraction (accuracy metric).

Layer 1: Pairwise SCS-Confusion — for each (type_i, type_j) pair, correlate
    pairwise cosine similarity with confusion rate (how often one is predicted
    when the other is the gold label).
Layer 2: Per-type accuracy vs mean_BCS — for each relation type, compute its
    accuracy across all batches it appears in, vs its mean BCS exposure.
Layer 3: Batch-level accuracy vs BCS — correlate batch accuracy with batch BCS.

Usage:
    python3 src/analyze_fewrel_results.py \
        --results_dir artifacts/fewrel_formal \
        --bcs_matrix artifacts/fewrel_formal/relation_sim_matrix.pt \
        --exp exp2
    python3 src/analyze_fewrel_results.py --dry-run \
        --bcs_matrix artifacts/fewrel_formal/relation_sim_matrix.pt
"""
import argparse
import json
import logging
import math
import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import numpy as np
import torch
from scipy import stats

sys.path.insert(0, str(Path(__file__).parent))

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)


# ─────────────────────────────────────────────────────
# Data loading
# ─────────────────────────────────────────────────────

def load_bcs_matrix(path: str) -> Tuple[List[str], np.ndarray]:
    data = torch.load(path, map_location="cpu", weights_only=True)
    type_names = data["type_names"]
    if isinstance(type_names, torch.Tensor):
        type_names = type_names.tolist()
    if type_names and isinstance(type_names[0], bytes):
        type_names = [t.decode() for t in type_names]
    sim_matrix = data["sim_matrix" if "sim_matrix" in data else "similarity_matrix"]
    if isinstance(sim_matrix, torch.Tensor):
        sim_matrix = sim_matrix.float().numpy()
    return list(type_names), sim_matrix


def load_predictions(results_dir: Path, exp: str) -> List[Dict]:
    for name in [f"predictions_{exp}.json", "predictions.json"]:
        p = results_dir / name
        if p.exists():
            logger.info("Loading predictions from %s", p)
            with open(p) as f:
                return json.load(f)
    raise FileNotFoundError(f"No predictions JSON for {exp} in {results_dir}")


def load_eval_results(results_dir: Path, exp: str) -> Dict:
    for name in [f"eval_{exp}.json", "eval_results.json"]:
        p = results_dir / name
        if p.exists():
            with open(p) as f:
                return json.load(f)
    return {}


# ─────────────────────────────────────────────────────
# Layer 1: Pairwise SCS-Confusion
# ─────────────────────────────────────────────────────

def build_confusion_counts(predictions: List[Dict]) -> Tuple[Dict, Dict]:
    """Build confusion matrix from RE predictions.

    For RE, each prediction has a single ground_truth and single prediction.
    Confusion: gold=type_i, predicted=type_j (i≠j).
    """
    confusion = defaultdict(lambda: defaultdict(int))
    gold_counts = defaultdict(int)

    for r in predictions:
        gold = r["ground_truth"]
        pred = r["prediction"]
        gold_counts[gold] += 1
        if pred != gold and pred != "none":
            confusion[gold][pred] += 1

    return dict(confusion), dict(gold_counts)


def layer1_pairwise(predictions: List[Dict],
                    type_names: List[str],
                    sim_matrix: np.ndarray) -> Dict:
    """Correlate pairwise SCS with pairwise confusion rate."""
    name_to_idx = {n: i for i, n in enumerate(type_names)}
    confusion, gold_counts = build_confusion_counts(predictions)

    scs_vals = []
    confusion_rates = []
    pairs = []

    for i, ti in enumerate(type_names):
        for j, tj in enumerate(type_names):
            if i >= j:
                continue
            if ti not in name_to_idx or tj not in name_to_idx:
                continue

            scs = sim_matrix[name_to_idx[ti], name_to_idx[tj]]

            c_ij = confusion.get(ti, {}).get(tj, 0)
            c_ji = confusion.get(tj, {}).get(ti, 0)
            denom_i = gold_counts.get(ti, 0)
            denom_j = gold_counts.get(tj, 0)

            if denom_i + denom_j == 0:
                continue

            rate = (c_ij + c_ji) / (denom_i + denom_j)
            scs_vals.append(float(scs))
            confusion_rates.append(rate)
            pairs.append((ti, tj))

    result = {"n_pairs": len(scs_vals)}
    if len(scs_vals) < 3:
        result["note"] = "too few pairs for correlation"
        return result

    scs_arr = np.array(scs_vals)
    conf_arr = np.array(confusion_rates)

    pr, pp = stats.pearsonr(scs_arr, conf_arr)
    sr, sp = stats.spearmanr(scs_arr, conf_arr)
    result["pearson_r"] = _safe(pr)
    result["pearson_p"] = _safe(pp)
    result["spearman_rho"] = _safe(sr)
    result["spearman_p"] = _safe(sp)

    nonzero = conf_arr > 0
    if nonzero.sum() >= 3:
        sr_nz, sp_nz = stats.spearmanr(scs_arr[nonzero], conf_arr[nonzero])
        result["nonzero_only"] = {
            "n": int(nonzero.sum()),
            "spearman_rho": _safe(sr_nz),
            "spearman_p": _safe(sp_nz),
        }

    top_confused = sorted(zip(pairs, confusion_rates, scs_vals),
                          key=lambda x: -x[1])[:10]
    result["top_confused_pairs"] = [
        {"pair": list(p), "confusion_rate": round(cr, 4), "scs": round(s, 4)}
        for p, cr, s in top_confused
    ]

    return result


# ─────────────────────────────────────────────────────
# Layer 2: Per-type accuracy vs mean BCS
# ─────────────────────────────────────────────────────

def layer2_per_type(predictions: List[Dict],
                    type_names: List[str],
                    sim_matrix: np.ndarray,
                    min_freq: int = 10) -> Dict:
    """Per relation type: accuracy vs mean BCS across batches it appeared in."""
    name_to_idx = {n: i for i, n in enumerate(type_names)}

    type_correct = defaultdict(int)
    type_total = defaultdict(int)
    type_bcs_sum = defaultdict(float)
    type_bcs_count = defaultdict(int)

    for r in predictions:
        gold = r["ground_truth"]
        batch_types = r.get("batch_types", [])
        bcs = r.get("batch_bcs", 0.0)

        type_total[gold] += 1
        if r["prediction"] == gold:
            type_correct[gold] += 1

        for t in batch_types:
            type_bcs_sum[t] += bcs
            type_bcs_count[t] += 1

    accs = []
    mean_bcs_vals = []
    log_freqs = []
    types_used = []

    for t in type_names:
        if type_total.get(t, 0) < min_freq:
            continue
        if type_bcs_count.get(t, 0) == 0:
            continue

        acc = type_correct[t] / type_total[t]
        mean_bcs = type_bcs_sum[t] / type_bcs_count[t]
        accs.append(acc)
        mean_bcs_vals.append(mean_bcs)
        log_freqs.append(math.log(type_total[t]))
        types_used.append(t)

    result = {"n_types": len(accs)}
    if len(accs) < 5:
        result["note"] = "too few types for correlation"
        return result

    acc_arr = np.array(accs)
    bcs_arr = np.array(mean_bcs_vals)
    logf_arr = np.array(log_freqs)

    pr, pp = stats.pearsonr(bcs_arr, acc_arr)
    sr, sp = stats.spearmanr(bcs_arr, acc_arr)

    result["acc_vs_mean_bcs"] = {
        "pearson_r": _safe(pr),
        "pearson_p": _safe(pp),
        "spearman_rho": _safe(sr),
        "spearman_p": _safe(sp),
    }

    # Partial correlation controlling for log-frequency
    if len(accs) >= 10:
        try:
            resid_acc = _residualize(acc_arr, logf_arr)
            resid_bcs = _residualize(bcs_arr, logf_arr)
            partial_r, partial_p = stats.pearsonr(resid_bcs, resid_acc)
            result["acc_vs_mean_bcs"]["partial_r_controlling_logfreq"] = _safe(partial_r)
            result["acc_vs_mean_bcs"]["partial_p"] = _safe(partial_p)
        except Exception:
            pass

    # Quartile analysis
    bcs_sorted_idx = np.argsort(bcs_arr)
    q = len(bcs_sorted_idx) // 4
    if q >= 2:
        low_idx = bcs_sorted_idx[:q]
        high_idx = bcs_sorted_idx[-q:]
        low_acc = float(np.mean(acc_arr[low_idx]))
        high_acc = float(np.mean(acc_arr[high_idx]))
        result["quartile"] = {
            "low_bcs_mean_acc": round(low_acc, 4),
            "high_bcs_mean_acc": round(high_acc, 4),
            "delta": round(low_acc - high_acc, 4),
            "n_per_quartile": int(q),
        }

    # Per-type details
    result["per_type_details"] = [
        {"type": t, "accuracy": round(a, 4), "mean_bcs": round(b, 4),
         "n_samples": type_total[t]}
        for t, a, b in sorted(zip(types_used, accs, mean_bcs_vals), key=lambda x: x[2])
    ]

    return result


# ─────────────────────────────────────────────────────
# Layer 3: Batch-level accuracy vs BCS
# ─────────────────────────────────────────────────────

def layer3_batch_level(eval_results: Dict) -> Dict:
    """Correlate batch accuracy with batch BCS across all batches."""
    result = {}

    by_count = defaultdict(list)
    for bid, m in eval_results.items():
        ck = m.get("count_key", "")
        by_count[ck].append(m)

    all_acc = []
    all_bcs = []

    for ck, batches in sorted(by_count.items()):
        accs = [b["accuracy"] for b in batches]
        bcs_vals = [b["bcs"] for b in batches]
        all_acc.extend(accs)
        all_bcs.extend(bcs_vals)

        if len(accs) < 5:
            result[ck] = {"n": len(accs), "note": "too few batches"}
            continue

        sr, sp = stats.spearmanr(bcs_vals, accs)
        pr, pp = stats.pearsonr(bcs_vals, accs)
        result[ck] = {
            "n": len(accs),
            "pearson_r": _safe(pr),
            "pearson_p": _safe(pp),
            "spearman_rho": _safe(sr),
            "spearman_p": _safe(sp),
            "mean_acc": round(float(np.mean(accs)), 4),
            "std_acc": round(float(np.std(accs)), 4),
            "bcs_range": [round(min(bcs_vals), 4), round(max(bcs_vals), 4)],
        }

    if len(all_acc) >= 5:
        sr, sp = stats.spearmanr(all_bcs, all_acc)
        pr, pp = stats.pearsonr(all_bcs, all_acc)
        result["all_batches"] = {
            "n": len(all_acc),
            "pearson_r": _safe(pr),
            "pearson_p": _safe(pp),
            "spearman_rho": _safe(sr),
            "spearman_p": _safe(sp),
        }

    return result


# ─────────────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────────────

def _safe(val):
    if val is None or (isinstance(val, float) and math.isnan(val)):
        return None
    return round(float(val), 6)


def _residualize(y: np.ndarray, x: np.ndarray) -> np.ndarray:
    slope, intercept, _, _, _ = stats.linregress(x, y)
    return y - (slope * x + intercept)


def generate_mock_data(type_names, sim_matrix):
    """Generate mock RE predictions for dry-run testing."""
    import random
    rng = random.Random(42)
    n_types = len(type_names)

    predictions = []
    batch_configs = [
        ("count_8_low_bcs", 8, 0.3),
        ("count_8_high_bcs", 8, 0.8),
    ]
    for i in range(10):
        batch_configs.append((f"count_8_random_{i}", 8,
                              0.3 + rng.random() * 0.5))

    sample_id = 0
    for bid, count, bcs in batch_configs:
        btypes = rng.sample(type_names, min(count, n_types))
        for _ in range(50):
            gold = rng.choice(btypes)
            if rng.random() < (1.0 - bcs * 0.6):
                pred = gold
            else:
                pred = rng.choice(btypes)
            predictions.append({
                "sample_id": sample_id,
                "batch_id": bid,
                "count_key": f"count_{count}",
                "batch_types": btypes,
                "batch_bcs": bcs,
                "prediction": pred,
                "ground_truth": gold,
                "head_entity": "mock_head",
                "tail_entity": "mock_tail",
            })
            sample_id += 1

    eval_results = {}
    for bid, count, bcs in batch_configs:
        entries = [p for p in predictions if p["batch_id"] == bid]
        correct = sum(1 for e in entries if e["prediction"] == e["ground_truth"])
        eval_results[bid] = {
            "accuracy": correct / len(entries) if entries else 0,
            "correct": correct,
            "total": len(entries),
            "bcs": bcs,
            "count_key": f"count_{count}",
            "num_types": count,
        }

    return predictions, eval_results


def main():
    parser = argparse.ArgumentParser(
        description="Three-layer FewRel analysis")
    parser.add_argument("--results_dir", type=str, default=None)
    parser.add_argument("--bcs_matrix", type=str, required=True)
    parser.add_argument("--exp", type=str, default="exp2",
                        help="Experiment to analyze: exp1 or exp2")
    parser.add_argument("--output", type=str,
                        default="artifacts/fewrel_formal/analysis.json")
    parser.add_argument("--min_freq", type=int, default=5)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    type_names, sim_matrix = load_bcs_matrix(args.bcs_matrix)
    logger.info("Loaded BCS matrix: %d types, shape %s",
                len(type_names), sim_matrix.shape)

    if args.dry_run:
        logger.info("=== DRY RUN with mock data ===")
        predictions, eval_results = generate_mock_data(type_names, sim_matrix)
    else:
        if not args.results_dir:
            parser.error("--results_dir required when not using --dry-run")
        results_dir = Path(args.results_dir)
        predictions = load_predictions(results_dir, args.exp)
        eval_results = load_eval_results(results_dir, args.exp)

    logger.info("=== Layer 1: Pairwise SCS-Confusion ===")
    l1 = layer1_pairwise(predictions, type_names, sim_matrix)
    logger.info("  Pairs: %d, Pearson r=%s, Spearman rho=%s",
                l1.get("n_pairs", 0), l1.get("pearson_r"), l1.get("spearman_rho"))
    if "nonzero_only" in l1:
        nz = l1["nonzero_only"]
        logger.info("  Nonzero-only: n=%d, Spearman rho=%s (p=%s)",
                    nz["n"], nz["spearman_rho"], nz["spearman_p"])

    logger.info("=== Layer 2: Per-type Accuracy vs Mean BCS ===")
    l2 = layer2_per_type(predictions, type_names, sim_matrix,
                         min_freq=args.min_freq)
    if "acc_vs_mean_bcs" in l2:
        corr = l2["acc_vs_mean_bcs"]
        logger.info("  Types: %d, Pearson r=%s, Partial r=%s",
                    l2["n_types"], corr["pearson_r"],
                    corr.get("partial_r_controlling_logfreq"))
    if "quartile" in l2:
        q = l2["quartile"]
        logger.info("  Quartile: low_bcs_acc=%s, high_bcs_acc=%s, delta=%s",
                    q.get("low_bcs_mean_acc"), q.get("high_bcs_mean_acc"),
                    q.get("delta"))

    logger.info("=== Layer 3: Batch-level Accuracy vs BCS ===")
    l3 = layer3_batch_level(eval_results)
    for ck, v in l3.items():
        if isinstance(v, dict) and "n" in v:
            logger.info("  %s: n=%s, r(acc,BCS)=%s (p=%s)",
                        ck, v.get("n"), v.get("pearson_r"), v.get("pearson_p"))

    output = {
        "layer1_pairwise": l1,
        "layer2_per_type": l2,
        "layer3_batch_level": l3,
    }

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(output, f, indent=2,
                  default=lambda x: None if isinstance(x, float) and math.isnan(x) else x)
    logger.info("Saved analysis to %s", output_path)


if __name__ == "__main__":
    main()
