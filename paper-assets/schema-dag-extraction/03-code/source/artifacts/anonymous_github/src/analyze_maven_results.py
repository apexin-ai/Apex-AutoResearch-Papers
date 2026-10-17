"""Three-layer MAVEN analysis: pairwise SCS-confusion, per-type F1 vs BCS, batch percentile BCS.

Designed for MAVEN exp-004 where Qwen3 BCS range is extremely compressed
(max pairwise sim >=0.90, batch-level BCS delta ~ 0.014).
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

DEFAULT_DATA_PATH = "./data/maven_parquet/valid.parquet"


# ─────────────────────────────────────────────────────
# Data loading
# ─────────────────────────────────────────────────────

def load_bcs_matrix(path: str) -> Tuple[List[str], np.ndarray]:
    data = torch.load(path, map_location="cpu", weights_only=True)
    type_names = data["type_names"]
    if isinstance(type_names, torch.Tensor):
        type_names = type_names.tolist()
    if isinstance(type_names[0], bytes):
        type_names = [t.decode() for t in type_names]
    sim_matrix = data["similarity_matrix"].float().numpy()
    return list(type_names), sim_matrix


def load_maven_samples(data_path: str = DEFAULT_DATA_PATH,
                       max_samples: Optional[int] = None) -> List[Dict]:
    import pandas as pd
    df = pd.read_parquet(data_path)
    if max_samples:
        df = df.head(max_samples)
    samples = []
    for _, row in df.iterrows():
        entities = row["entities"]
        if isinstance(entities, str):
            entities = json.loads(entities)
        samples.append({"text": row["text"], "entities": list(entities)})
    return samples


def load_type_descriptions(path: str) -> Dict[str, str]:
    with open(path) as f:
        return json.load(f)


def load_predictions(results_dir: Path) -> List[Dict]:
    for name in ["predictions_exp2.json", "predictions_exp1.json"]:
        p = results_dir / name
        if p.exists():
            logger.info("Loading predictions from %s", p)
            with open(p) as f:
                return json.load(f)
    raise FileNotFoundError(f"No predictions JSON in {results_dir}")


def load_eval_results(results_dir: Path, exp: str = "exp2") -> Dict:
    p = results_dir / f"eval_{exp}.json"
    if p.exists():
        with open(p) as f:
            return json.load(f)
    return {}


# ─────────────────────────────────────────────────────
# Text match helpers
# ─────────────────────────────────────────────────────

def text_match(pred_text: str, gold_text: str, source_text: str = "") -> bool:
    pt = pred_text.strip().lower()
    gt = gold_text.strip().lower()
    if not pt or not gt:
        return False
    if source_text and pt not in source_text.lower():
        return False
    return pt == gt or pt in gt or gt in pt


# ─────────────────────────────────────────────────────
# Layer 1: Pairwise SCS-Confusion
# ─────────────────────────────────────────────────────

def build_confusion_counts(predictions: List[Dict],
                           samples: List[Dict]) -> Tuple[Dict, Dict]:
    confusion = defaultdict(lambda: defaultdict(int))
    gold_counts = defaultdict(int)

    by_batch_sample = defaultdict(list)
    for p in predictions:
        by_batch_sample[(p["batch_id"], p["sample_id"])].append(p)

    for (batch_id, sid), entries in by_batch_sample.items():
        if sid >= len(samples):
            continue
        entry = entries[0]
        batch_types = set(entry.get("batch_types", []))
        source_text = samples[sid]["text"]
        gold_entities = [e for e in samples[sid]["entities"] if e["type"] in batch_types]
        preds = [p for p in entry.get("predictions", []) if p.get("type") in batch_types]

        for g in gold_entities:
            gold_counts[g["type"]] += 1

        gold_available = [[g["text"], g["type"], False] for g in gold_entities]

        for pred in preds:
            pt = pred.get("text", "")
            ptype = pred.get("type", "")
            if not text_match(pt, pt, source_text):
                continue

            exact_matched = False
            for g in gold_available:
                if not g[2] and text_match(pt, g[0], source_text) and g[1] == ptype:
                    g[2] = True
                    exact_matched = True
                    break

            if exact_matched:
                continue

            for g in gold_available:
                if not g[2] and text_match(pt, g[0], source_text) and g[1] != ptype:
                    confusion[g[1]][ptype] += 1
                    g[2] = True
                    break

    return dict(confusion), dict(gold_counts)


def layer1_pairwise(predictions: List[Dict], samples: List[Dict],
                    type_names: List[str], sim_matrix: np.ndarray) -> Dict:
    confusion, gold_counts = build_confusion_counts(predictions, samples)
    type_to_idx = {t: i for i, t in enumerate(type_names)}

    all_types = sorted(set(gold_counts.keys()) & set(type_names))
    bcs_vals, conf_vals, pair_labels = [], [], []

    seen = set()
    for t1 in all_types:
        for t2 in all_types:
            if t1 >= t2:
                continue
            key = (t1, t2)
            if key in seen:
                continue
            seen.add(key)
            if t1 not in type_to_idx or t2 not in type_to_idx:
                continue

            scs = float(sim_matrix[type_to_idx[t1], type_to_idx[t2]])
            c_ij = confusion.get(t1, {}).get(t2, 0)
            c_ji = confusion.get(t2, {}).get(t1, 0)
            total_conf = c_ij + c_ji

            bcs_vals.append(scs)
            conf_vals.append(total_conf)
            pair_labels.append((t1, t2, total_conf, scs))

    bcs_arr = np.array(bcs_vals)
    conf_arr = np.array(conf_vals)

    result = {"n_pairs": len(bcs_arr)}

    if len(bcs_arr) < 3:
        return result

    pr, pp = stats.pearsonr(bcs_arr, conf_arr)
    sr, sp = stats.spearmanr(bcs_arr, conf_arr)
    result.update({
        "pearson_r": _f(pr), "pearson_p": _f(pp),
        "spearman_rho": _f(sr), "spearman_p": _f(sp),
    })

    nz_mask = conf_arr > 0
    nz_n = int(nz_mask.sum())
    if nz_n >= 3:
        nz_sr, nz_sp = stats.spearmanr(bcs_arr[nz_mask], conf_arr[nz_mask])
        result["nonzero_only"] = {
            "spearman_rho": _f(nz_sr), "spearman_p": _f(nz_sp), "n": nz_n
        }

    pair_labels.sort(key=lambda x: x[2], reverse=True)
    result["top_confused_pairs"] = [
        {"type_a": t1, "type_b": t2, "scs": _f(scs), "confusion": c}
        for t1, t2, c, scs in pair_labels[:20]
    ]

    return result


# ─────────────────────────────────────────────────────
# Layer 2: Per-type F1 vs Mean BCS
# ─────────────────────────────────────────────────────

def compute_per_type_metrics(predictions: List[Dict],
                             samples: List[Dict]) -> Dict[str, Dict]:
    type_stats = defaultdict(lambda: {"tp": 0, "fp": 0, "fn": 0})

    by_batch_sample = defaultdict(list)
    for p in predictions:
        by_batch_sample[(p["batch_id"], p["sample_id"])].append(p)

    for (batch_id, sid), entries in by_batch_sample.items():
        if sid >= len(samples):
            continue
        entry = entries[0]
        batch_types = set(entry.get("batch_types", []))
        source_text = samples[sid]["text"]
        gold_entities = [e for e in samples[sid]["entities"] if e["type"] in batch_types]
        pred_entities = [p for p in entry.get("predictions", []) if p.get("type") in batch_types]

        matched_gold = set()
        matched_pred = set()

        for pi, pred in enumerate(pred_entities):
            for gi, gold in enumerate(gold_entities):
                if gi in matched_gold:
                    continue
                if pred.get("type") == gold["type"] and text_match(
                        pred.get("text", ""), gold["text"], source_text):
                    matched_gold.add(gi)
                    matched_pred.add(pi)
                    type_stats[gold["type"]]["tp"] += 1
                    break

        for pi, pred in enumerate(pred_entities):
            if pi not in matched_pred:
                t = pred.get("type")
                if t in batch_types:
                    type_stats[t]["fp"] += 1

        for gi, gold in enumerate(gold_entities):
            if gi not in matched_gold:
                type_stats[gold["type"]]["fn"] += 1

    result = {}
    for t, s in type_stats.items():
        tp, fp, fn = s["tp"], s["fp"], s["fn"]
        p = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        r = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        f1 = 2 * p * r / (p + r) if (p + r) > 0 else 0.0
        result[t] = {"precision": p, "recall": r, "f1": f1,
                      "tp": tp, "fp": fp, "fn": fn, "freq": tp + fn}
    return result


def partial_corr(x, y, z):
    x, y, z = np.array(x), np.array(y), np.array(z)
    if len(x) < 4:
        return float("nan"), float("nan")

    def _resid(a, b):
        slope, intercept = np.polyfit(b, a, 1)
        return a - (slope * b + intercept)

    return stats.pearsonr(_resid(x, z), _resid(y, z))


def layer2_per_type(predictions: List[Dict], samples: List[Dict],
                    type_names: List[str], sim_matrix: np.ndarray,
                    min_freq: int = 5) -> Dict:
    per_type = compute_per_type_metrics(predictions, samples)
    type_to_idx = {t: i for i, t in enumerate(type_names)}

    n = len(type_names)
    mean_bcs = {}
    for i, t in enumerate(type_names):
        sims = [float(sim_matrix[i, j]) for j in range(n) if j != i]
        mean_bcs[t] = np.mean(sims)

    rows = []
    for t, m in per_type.items():
        if t not in mean_bcs:
            continue
        if m["freq"] < min_freq:
            continue
        rows.append({
            "type": t,
            "f1": m["f1"],
            "precision": m["precision"],
            "recall": m["recall"],
            "mean_bcs": mean_bcs[t],
            "freq": m["freq"],
            "log_freq": math.log(m["freq"] + 1),
        })

    if len(rows) < 5:
        return {"n_types": len(rows), "filter": f"freq>={min_freq}",
                "note": "too few types for analysis"}

    f1_arr = np.array([r["f1"] for r in rows])
    bcs_arr = np.array([r["mean_bcs"] for r in rows])
    log_freq = np.array([r["log_freq"] for r in rows])

    pr, pp = stats.pearsonr(bcs_arr, f1_arr)
    sr, sp = stats.spearmanr(bcs_arr, f1_arr)
    part_r, part_p = partial_corr(bcs_arr, f1_arr, log_freq)

    q25 = float(np.percentile(bcs_arr, 25))
    q75 = float(np.percentile(bcs_arr, 75))
    low_f1 = [r["f1"] for r in rows if r["mean_bcs"] <= q25]
    high_f1 = [r["f1"] for r in rows if r["mean_bcs"] >= q75]

    confound_r, confound_p = stats.pearsonr(bcs_arr, log_freq)

    return {
        "n_types": len(rows),
        "filter": f"freq>={min_freq}",
        "f1_vs_mean_bcs": {
            "pearson_r": _f(pr), "pearson_p": _f(pp),
            "spearman_rho": _f(sr), "spearman_p": _f(sp),
            "partial_r_controlling_logfreq": _f(part_r),
            "partial_p": _f(part_p),
        },
        "quartile": {
            "q25_threshold": _f(q25),
            "q75_threshold": _f(q75),
            "low_bcs_f1": _f(np.mean(low_f1)) if low_f1 else None,
            "high_bcs_f1": _f(np.mean(high_f1)) if high_f1 else None,
            "delta": _f(np.mean(high_f1) - np.mean(low_f1)) if low_f1 and high_f1 else None,
            "n_low": len(low_f1),
            "n_high": len(high_f1),
        },
        "confound_check": {
            "bcs_vs_logfreq_r": _f(confound_r),
            "bcs_vs_logfreq_p": _f(confound_p),
        },
    }


# ─────────────────────────────────────────────────────
# Layer 3: Batch-level Percentile Rank BCS
# ─────────────────────────────────────────────────────

def layer3_batch_percentile(eval_results: Dict) -> Dict:
    count_groups = defaultdict(list)
    for bid, batch in eval_results.items():
        count_key = batch.get("count_key", "")
        bcs = batch.get("bcs")
        metrics = batch.get("text_match", batch.get("relaxed", batch.get("exact", {})))
        f1 = metrics.get("f1")
        recall = metrics.get("recall")
        if bcs is not None and f1 is not None:
            count_groups[count_key].append({"bcs": bcs, "f1": f1, "recall": recall or 0})

    result = {}
    for ck, batches in sorted(count_groups.items()):
        if len(batches) < 5:
            result[ck] = {"n": len(batches), "note": "too few batches"}
            continue

        bcs_arr = np.array([b["bcs"] for b in batches])
        f1_arr = np.array([b["f1"] for b in batches])
        recall_arr = np.array([b["recall"] for b in batches])

        pct_bcs = stats.rankdata(bcs_arr) / len(bcs_arr) * 100

        r_f1, p_f1 = stats.pearsonr(pct_bcs, f1_arr)
        r_rec, p_rec = stats.pearsonr(pct_bcs, recall_arr)

        bcs_range = float(bcs_arr.max() - bcs_arr.min())

        result[ck] = {
            "n": len(batches),
            "bcs_range": _f(bcs_range),
            "r_f1_pctBCS": _f(r_f1), "p_f1": _f(p_f1),
            "r_recall_pctBCS": _f(r_rec), "p_recall": _f(p_rec),
        }

    all_significant = all(
        r.get("p_f1", 1) < 0.05
        for r in result.values()
        if isinstance(r.get("p_f1"), (int, float))
    )
    if not all_significant:
        result["note"] = "BCS compression limitation: batch-level BCS range too narrow for significance"

    return result


# ─────────────────────────────────────────────────────
# Mock data for dry-run
# ─────────────────────────────────────────────────────

def generate_mock_data(type_names: List[str], sim_matrix: np.ndarray,
                       n_samples: int = 200) -> Tuple[List[Dict], List[Dict], Dict]:
    rng = np.random.RandomState(42)
    active_types = type_names[:40]

    samples = []
    for i in range(n_samples):
        n_ent = rng.randint(0, 5)
        entities = []
        for _ in range(n_ent):
            t = active_types[rng.randint(0, len(active_types))]
            word = f"entity_{rng.randint(0, 1000)}"
            entities.append({"text": word, "type": t})
        text = " ".join(["word"] * 10 + [e["text"] for e in entities] + ["word"] * 5)
        samples.append({"text": text, "entities": entities})

    predictions = []
    type_to_idx = {t: i for i, t in enumerate(type_names)}
    count_levels = [12, 24]
    batch_id_counter = 0

    for count in count_levels:
        n_batches = 25
        for b in range(n_batches):
            batch_types = list(rng.choice(active_types, size=min(count, len(active_types)),
                                         replace=False))
            idxs = [type_to_idx[t] for t in batch_types if t in type_to_idx]
            if len(idxs) >= 2:
                sims = [float(sim_matrix[i, j]) for i in idxs for j in idxs if i != j]
                bcs = float(np.mean(sims))
            else:
                bcs = 0.9

            batch_id = f"count_{count}_random_{b}"
            for sid in range(n_samples):
                sample = samples[sid]
                gold_in_batch = [e for e in sample["entities"] if e["type"] in batch_types]
                preds = []
                for g in gold_in_batch:
                    if rng.random() < 0.6:
                        preds.append({"text": g["text"], "type": g["type"]})
                    elif rng.random() < 0.3:
                        wrong_type = batch_types[rng.randint(0, len(batch_types))]
                        preds.append({"text": g["text"], "type": wrong_type})

                predictions.append({
                    "sample_id": sid,
                    "batch_id": batch_id,
                    "count_key": f"count_{count}",
                    "batch_types": batch_types,
                    "batch_bcs": bcs,
                    "predictions": preds,
                })
            batch_id_counter += 1

    eval_results = {}
    by_batch = defaultdict(list)
    for p in predictions:
        by_batch[p["batch_id"]].append(p)

    for bid, batch_preds in by_batch.items():
        entry = batch_preds[0]
        batch_types = set(entry["batch_types"])
        tp = fp = fn = 0
        for p in batch_preds:
            sid = p["sample_id"]
            if sid >= len(samples):
                continue
            gold = [e for e in samples[sid]["entities"] if e["type"] in batch_types]
            pred = p.get("predictions", [])
            matched = set()
            for pr in pred:
                found = False
                for gi, g in enumerate(gold):
                    if gi not in matched and pr.get("type") == g["type"] and pr.get("text") == g["text"]:
                        matched.add(gi)
                        tp += 1
                        found = True
                        break
                if not found:
                    fp += 1
            fn += len(gold) - len(matched)

        precision = tp / (tp + fp) if (tp + fp) > 0 else 0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0
        f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0

        eval_results[bid] = {
            "bcs": entry["batch_bcs"],
            "count_key": entry["count_key"],
            "num_types": len(entry["batch_types"]),
            "text_match": {"precision": precision, "recall": recall, "f1": f1,
                           "tp": tp, "total_pred": tp + fp, "total_gold": tp + fn},
        }

    return predictions, samples, eval_results


# ─────────────────────────────────────────────────────
# Utilities
# ─────────────────────────────────────────────────────

def _f(x):
    if x is None or (isinstance(x, float) and math.isnan(x)):
        return None
    return round(float(x), 6)


# ─────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Three-layer MAVEN analysis: pairwise SCS-confusion, "
                    "per-type F1 vs BCS, batch percentile BCS")
    parser.add_argument("--results_dir", type=str, default=None,
                        help="Directory with predictions and eval JSONs")
    parser.add_argument("--bcs_matrix", type=str, required=True,
                        help="Path to maven_bcs_matrix_qwen3.pt")
    parser.add_argument("--types_file", type=str, default=None,
                        help="Path to maven_event_types.json (optional)")
    parser.add_argument("--data_path", type=str, default=DEFAULT_DATA_PATH,
                        help="Path to MAVEN parquet for gold labels")
    parser.add_argument("--max_samples", type=int, default=500,
                        help="Max samples to load from dataset")
    parser.add_argument("--output", type=str, default="results/maven_analysis.json",
                        help="Output JSON path")
    parser.add_argument("--min_freq", type=int, default=5,
                        help="Min frequency threshold for per-type analysis")
    parser.add_argument("--dry-run", action="store_true",
                        help="Run with mock data to test script logic")
    args = parser.parse_args()

    type_names, sim_matrix = load_bcs_matrix(args.bcs_matrix)
    logger.info("Loaded BCS matrix: %d types, shape %s", len(type_names), sim_matrix.shape)

    if args.dry_run:
        logger.info("=== DRY RUN with mock data ===")
        predictions, samples, eval_results = generate_mock_data(type_names, sim_matrix)
    else:
        if not args.results_dir:
            parser.error("--results_dir is required when not using --dry-run")
        results_dir = Path(args.results_dir)
        predictions = load_predictions(results_dir)
        samples = load_maven_samples(args.data_path, args.max_samples)
        eval_results = load_eval_results(results_dir, "exp2")
        if not eval_results:
            eval_results = load_eval_results(results_dir, "exp1")

    logger.info("=== Layer 1: Pairwise SCS-Confusion ===")
    l1 = layer1_pairwise(predictions, samples, type_names, sim_matrix)
    logger.info("  Pairs: %d, Pearson r=%s, Spearman rho=%s",
                l1.get("n_pairs", 0), l1.get("pearson_r"), l1.get("spearman_rho"))
    if "nonzero_only" in l1:
        nz = l1["nonzero_only"]
        logger.info("  Nonzero-only: n=%d, Spearman rho=%s (p=%s)",
                    nz["n"], nz["spearman_rho"], nz["spearman_p"])

    logger.info("=== Layer 2: Per-type F1 vs Mean BCS ===")
    l2 = layer2_per_type(predictions, samples, type_names, sim_matrix,
                         min_freq=args.min_freq)
    if "f1_vs_mean_bcs" in l2:
        corr = l2["f1_vs_mean_bcs"]
        logger.info("  Types: %d, Pearson r=%s, Partial r=%s",
                    l2["n_types"], corr["pearson_r"],
                    corr["partial_r_controlling_logfreq"])
    if "quartile" in l2:
        q = l2["quartile"]
        logger.info("  Quartile: low_bcs_f1=%s, high_bcs_f1=%s, delta=%s",
                    q.get("low_bcs_f1"), q.get("high_bcs_f1"), q.get("delta"))

    logger.info("=== Layer 3: Batch-level Percentile Rank BCS ===")
    l3 = layer3_batch_percentile(eval_results)
    for ck, v in l3.items():
        if ck == "note":
            logger.info("  Note: %s", v)
        elif isinstance(v, dict):
            logger.info("  %s: n=%s, r(F1,pctBCS)=%s (p=%s)",
                        ck, v.get("n"), v.get("r_f1_pctBCS"), v.get("p_f1"))

    output = {
        "layer1_pairwise": l1,
        "layer2_per_type": l2,
        "layer3_batch_percentile": l3,
    }

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(output, f, indent=2, default=lambda x: None if isinstance(x, float) and math.isnan(x) else x)
    logger.info("Saved analysis to %s", output_path)


if __name__ == "__main__":
    main()
