#!/usr/bin/env python3
"""Bootstrap 95% CI for all key correlation/effect-size metrics.

Metrics:
1. Few-NERD pairwise BCS→confusion: Pearson r (n=1953 pairs)
2. MAVEN MiniLM pairwise SCS→confusion: Pearson r (n=14028 pairs)
3. FewRel 80-rel BCS-controlled accuracy Δ (count_8 and count_16)
4. Few-NERD per-type F1 vs BCS: Spearman ρ (n=63 types)
5. exp-002 confusion ratio: extreme batches
"""

import json
import sys
import argparse
import logging
from pathlib import Path
from collections import defaultdict

import numpy as np
import torch
from scipy import stats

ROOT = Path("/root/schema-dag-extraction")

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")
logger = logging.getLogger(__name__)


def bootstrap_corr(x, y, corr_func, n_boot, seed):
    rng = np.random.RandomState(seed)
    n = len(x)
    point_est = float(corr_func(x, y))
    boot_vals = np.empty(n_boot)
    for i in range(n_boot):
        idx = rng.randint(0, n, size=n)
        try:
            boot_vals[i] = float(corr_func(x[idx], y[idx]))
        except Exception:
            boot_vals[i] = np.nan
    finite = boot_vals[~np.isnan(boot_vals)]
    return {
        "point_estimate": point_est,
        "ci_lower": float(np.percentile(finite, 2.5)),
        "ci_upper": float(np.percentile(finite, 97.5)),
        "n_samples": n,
        "n_bootstrap": n_boot,
        "n_valid_bootstrap": len(finite),
    }


def pearson_r(x, y):
    return stats.pearsonr(x, y)[0]

def spearman_rho(x, y):
    return stats.spearmanr(x, y)[0]


# ===== Metric 1: Few-NERD pairwise BCS → confusion =====

def metric1_fewnerd_pairwise():
    sys.path.insert(0, str(ROOT / "src"))
    from few_nerd_utils import load_few_nerd

    logger.info("[1] Loading Few-NERD test data + predictions_exp2...")
    samples = load_few_nerd(split="test", max_samples=1000)
    with open(ROOT / "artifacts" / "predictions_exp2.json") as f:
        preds = json.load(f)

    emb_dict = torch.load(ROOT / "data" / "type_embeddings.pt",
                           map_location="cpu", weights_only=False)
    type_names = sorted(emb_dict.keys())
    emb_matrix = torch.stack([emb_dict[t] for t in type_names])
    emb_norm = emb_matrix / emb_matrix.norm(dim=1, keepdim=True)
    sim_matrix = (emb_norm @ emb_norm.T).float().numpy()
    type_to_idx = {t: i for i, t in enumerate(type_names)}

    confusion = defaultdict(lambda: defaultdict(int))
    gold_counts = defaultdict(int)

    by_batch_sample = defaultdict(list)
    for p in preds:
        by_batch_sample[(p["batch_id"], p["sample_id"])].append(p)

    for (batch_id, sid), entries in by_batch_sample.items():
        if sid >= len(samples):
            continue
        entry = entries[0]
        batch_types = set(entry["batch_types"])
        source_text = samples[sid]["text"]
        gold_entities = [e for e in samples[sid]["entities"]
                         if e["type"] in batch_types]
        pred_entities = [p for p in entry.get("predictions", [])
                         if p.get("type") in batch_types]

        for g in gold_entities:
            gold_counts[g["type"]] += 1

        gold_available = [[g["text"], g["type"], False] for g in gold_entities]

        for pred in pred_entities:
            pt = pred.get("text", "")
            ptype = pred.get("type", "")
            if pt not in source_text:
                continue

            exact_matched = False
            for g in gold_available:
                if not g[2] and g[0] == pt and g[1] == ptype:
                    g[2] = True
                    exact_matched = True
                    break
            if exact_matched:
                continue

            for g in gold_available:
                if not g[2] and g[0] == pt and g[1] != ptype:
                    confusion[g[1]][ptype] += 1
                    g[2] = True
                    break

    all_types = sorted(set(gold_counts.keys()))
    bcs_vals, conf_vals = [], []
    seen = set()
    for t1 in all_types:
        for t2 in all_types:
            if t1 == t2:
                continue
            pair = tuple(sorted([t1, t2]))
            if pair in seen:
                continue
            seen.add(pair)
            if t1 not in type_to_idx or t2 not in type_to_idx:
                continue
            bcs = sim_matrix[type_to_idx[t1], type_to_idx[t2]]
            c12 = confusion.get(t1, {}).get(t2, 0)
            c21 = confusion.get(t2, {}).get(t1, 0)
            denom = gold_counts.get(t1, 0) + gold_counts.get(t2, 0)
            rate = (c12 + c21) / denom if denom > 0 else 0
            bcs_vals.append(float(bcs))
            conf_vals.append(float(rate))

    bcs_arr = np.array(bcs_vals)
    conf_arr = np.array(conf_vals)
    logger.info("[1] n_pairs=%d, Pearson r=%.4f", len(bcs_arr),
                pearson_r(bcs_arr, conf_arr))
    return bcs_arr, conf_arr


# ===== Metric 2: MAVEN MiniLM pairwise SCS → confusion =====

def metric2_maven_pairwise():
    import pandas as pd

    logger.info("[2] Loading MAVEN data + predictions...")
    df = pd.read_parquet(ROOT / "data" / "maven_parquet" / "valid.parquet")
    samples = []
    for _, row in df.iterrows():
        entities = row["entities"]
        if isinstance(entities, str):
            entities = json.loads(entities)
        samples.append({"text": row["text"], "entities": list(entities)})

    with open(ROOT / "artifacts" / "exp004" / "predictions_maven_exp1.json") as f:
        preds = json.load(f)

    sim_data = torch.load(ROOT / "artifacts" / "maven_minilm_sim_matrix.pt",
                           map_location="cpu", weights_only=True)
    type_names_sim = sim_data["type_names"]
    if isinstance(type_names_sim, torch.Tensor):
        type_names_sim = type_names_sim.tolist()
    if isinstance(type_names_sim[0], bytes):
        type_names_sim = [t.decode() for t in type_names_sim]
    sim_matrix = sim_data["similarity_matrix"].float().numpy()
    type_to_idx = {t: i for i, t in enumerate(type_names_sim)}

    def text_match(pred_text, gold_text, source_text=""):
        pt = pred_text.strip().lower()
        gt = gold_text.strip().lower()
        if not pt or not gt:
            return False
        if source_text and pt not in source_text.lower():
            return False
        return pt == gt or pt in gt or gt in pt

    confusion = defaultdict(lambda: defaultdict(int))
    gold_counts = defaultdict(int)

    by_batch_sample = defaultdict(list)
    for p in preds:
        by_batch_sample[(p["batch_id"], p["sample_id"])].append(p)

    for (batch_id, sid), entries in by_batch_sample.items():
        if sid >= len(samples):
            continue
        entry = entries[0]
        batch_types = set(entry.get("batch_types", []))
        source_text = samples[sid]["text"]
        gold_entities = [e for e in samples[sid]["entities"]
                         if e["type"] in batch_types]
        pred_entities = [p for p in entry.get("predictions", [])
                         if p.get("type") in batch_types]

        for g in gold_entities:
            gold_counts[g["type"]] += 1

        gold_available = [[g["text"], g["type"], False] for g in gold_entities]

        for pred in pred_entities:
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

    all_types = sorted(set(gold_counts.keys()) & set(type_names_sim))
    bcs_vals, conf_vals = [], []
    for i, t1 in enumerate(all_types):
        for t2 in all_types[i+1:]:
            scs = float(sim_matrix[type_to_idx[t1], type_to_idx[t2]])
            c_ij = confusion.get(t1, {}).get(t2, 0)
            c_ji = confusion.get(t2, {}).get(t1, 0)
            total_conf = c_ij + c_ji
            bcs_vals.append(scs)
            conf_vals.append(float(total_conf))

    bcs_arr = np.array(bcs_vals)
    conf_arr = np.array(conf_vals)
    logger.info("[2] n_pairs=%d, Pearson r=%.4f", len(bcs_arr),
                pearson_r(bcs_arr, conf_arr))
    return bcs_arr, conf_arr


# ===== Metric 3: FewRel accuracy Δ =====

def metric3_fewrel_delta(n_boot, seed):
    logger.info("[3] Loading FewRel exp2 data...")
    with open(ROOT / "artifacts" / "fewrel_formal_full" / "eval_exp2.json") as f:
        data = json.load(f)

    results = {}
    for count_key in ["count_8", "count_16"]:
        low = data[f"{count_key}_low_bcs"]
        high = data[f"{count_key}_high_bcs"]
        n_low, c_low = low["total"], low["correct"]
        n_high, c_high = high["total"], high["correct"]
        acc_low = c_low / n_low
        acc_high = c_high / n_high
        delta = acc_low - acc_high

        low_arr = np.array([1] * c_low + [0] * (n_low - c_low))
        high_arr = np.array([1] * c_high + [0] * (n_high - c_high))

        rng = np.random.RandomState(seed)
        boot_deltas = np.empty(n_boot)
        for i in range(n_boot):
            bl = low_arr[rng.randint(0, n_low, size=n_low)]
            bh = high_arr[rng.randint(0, n_high, size=n_high)]
            boot_deltas[i] = bl.mean() - bh.mean()

        results[count_key] = {
            "point_estimate_delta_pp": round(float(delta * 100), 2),
            "ci_lower_pp": round(float(np.percentile(boot_deltas, 2.5) * 100), 2),
            "ci_upper_pp": round(float(np.percentile(boot_deltas, 97.5) * 100), 2),
            "acc_low_bcs": round(float(acc_low), 4),
            "acc_high_bcs": round(float(acc_high), 4),
            "n_low": n_low,
            "n_high": n_high,
            "bcs_low": round(float(low["bcs"]), 4),
            "bcs_high": round(float(high["bcs"]), 4),
            "n_bootstrap": n_boot,
        }
        logger.info("[3] FewRel %s: Δ=%.1fpp, 95%% CI [%.1f, %.1f]pp",
                     count_key, delta * 100,
                     np.percentile(boot_deltas, 2.5) * 100,
                     np.percentile(boot_deltas, 97.5) * 100)

    return results


# ===== Metric 4: Few-NERD per-type F1 vs BCS =====

def metric4_fewnerd_pertype():
    logger.info("[4] Loading per-type analysis data...")
    with open(ROOT / "results" / "per_type_analysis.json") as f:
        data = json.load(f)

    rows = data["per_type_table"]
    f1_arr = np.array([r["micro_f1"] for r in rows])
    bcs_arr = np.array([r["mean_bcs"] for r in rows])
    logger.info("[4] n_types=%d, Spearman ρ=%.4f", len(f1_arr),
                spearman_rho(bcs_arr, f1_arr))
    return bcs_arr, f1_arr


# ===== Metric 5: exp-002 confusion ratio =====

def metric5_confusion_ratio(n_boot, seed):
    logger.info("[5] Loading exp-002 reeval results...")
    with open(ROOT / "results" / "exp2_reeval_results.json") as f:
        data = json.load(f)

    results = {}
    for count_key in ["count_6", "count_12"]:
        low = data[f"{count_key}_low_bcs"]
        high = data[f"{count_key}_high_bcs"]

        low_wt = low["fp_breakdown"]["wrong_type"]
        low_gold = low["text_match"]["total_gold"]
        high_wt = high["fp_breakdown"]["wrong_type"]
        high_gold = high["text_match"]["total_gold"]

        low_rate = low_wt / low_gold
        high_rate = high_wt / high_gold
        ratio = high_rate / low_rate if low_rate > 0 else float("inf")

        rng = np.random.RandomState(seed)
        boot_ratios = np.empty(n_boot)
        for i in range(n_boot):
            bl_wt = rng.binomial(low_gold, low_wt / low_gold)
            bh_wt = rng.binomial(high_gold, high_wt / high_gold)
            bl_rate = (bl_wt + 0.5) / (low_gold + 1)
            bh_rate = (bh_wt + 0.5) / (high_gold + 1)
            boot_ratios[i] = bh_rate / bl_rate

        results[count_key] = {
            "point_estimate_ratio": round(float(ratio), 1),
            "ci_lower": round(float(np.percentile(boot_ratios, 2.5)), 1),
            "ci_upper": round(float(np.percentile(boot_ratios, 97.5)), 1),
            "high_bcs_wrong_type": high_wt,
            "high_bcs_total_gold": high_gold,
            "high_bcs_rate": round(float(high_rate), 5),
            "low_bcs_wrong_type": low_wt,
            "low_bcs_total_gold": low_gold,
            "low_bcs_rate": round(float(low_rate), 5),
            "n_bootstrap": n_boot,
            "note": "Haldane-Anscombe correction (+0.5/+1) for zero-count stability",
        }
        logger.info("[5] %s: ratio=%.1fx, 95%% CI [%.1f, %.1f]x",
                     count_key, ratio,
                     np.percentile(boot_ratios, 2.5),
                     np.percentile(boot_ratios, 97.5))

    return results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default=str(ROOT / "artifacts" / "bootstrap_ci.json"))
    parser.add_argument("--n-bootstrap", type=int, default=1000)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    n_boot = args.n_bootstrap
    seed = args.seed
    results = {}

    # Metric 1
    bcs1, conf1 = metric1_fewnerd_pairwise()
    results["fewnerd_pairwise_bcs_confusion_pearson"] = bootstrap_corr(
        bcs1, conf1, pearson_r, n_boot, seed)

    # Metric 2
    bcs2, conf2 = metric2_maven_pairwise()
    results["maven_minilm_pairwise_scs_confusion_pearson"] = bootstrap_corr(
        bcs2, conf2, pearson_r, n_boot, seed)

    # Metric 3
    results["fewrel_bcs_controlled_accuracy_delta"] = metric3_fewrel_delta(n_boot, seed)

    # Metric 4
    bcs4, f14 = metric4_fewnerd_pertype()
    results["fewnerd_pertype_f1_vs_bcs_spearman"] = bootstrap_corr(
        bcs4, f14, spearman_rho, n_boot, seed)

    # Metric 5
    results["exp002_confusion_ratio"] = metric5_confusion_ratio(n_boot, seed)

    with open(args.output, "w") as f:
        json.dump(results, f, indent=2)
    logger.info("Saved → %s", args.output)

    # Summary
    print("\n" + "=" * 70)
    print("BOOTSTRAP 95% CI RESULTS (B=%d, seed=%d)" % (n_boot, seed))
    print("=" * 70)

    r = results["fewnerd_pairwise_bcs_confusion_pearson"]
    print(f"\n1. Few-NERD pairwise BCS→confusion (Pearson r, n={r['n_samples']})")
    print(f"   r = {r['point_estimate']:.4f}  [{r['ci_lower']:.4f}, {r['ci_upper']:.4f}]")

    r = results["maven_minilm_pairwise_scs_confusion_pearson"]
    print(f"\n2. MAVEN MiniLM pairwise SCS→confusion (Pearson r, n={r['n_samples']})")
    print(f"   r = {r['point_estimate']:.4f}  [{r['ci_lower']:.4f}, {r['ci_upper']:.4f}]")

    d = results["fewrel_bcs_controlled_accuracy_delta"]
    for ck in ["count_8", "count_16"]:
        r = d[ck]
        print(f"\n3. FewRel {ck} accuracy Δ (low−high BCS)")
        print(f"   Δ = {r['point_estimate_delta_pp']:+.1f}pp  [{r['ci_lower_pp']:+.1f}, {r['ci_upper_pp']:+.1f}]pp")

    r = results["fewnerd_pertype_f1_vs_bcs_spearman"]
    print(f"\n4. Few-NERD per-type F1 vs BCS (Spearman ρ, n={r['n_samples']})")
    print(f"   ρ = {r['point_estimate']:.4f}  [{r['ci_lower']:.4f}, {r['ci_upper']:.4f}]")

    d = results["exp002_confusion_ratio"]
    for ck in ["count_6", "count_12"]:
        r = d[ck]
        print(f"\n5. exp-002 {ck} confusion ratio (high/low BCS)")
        print(f"   ratio = {r['point_estimate_ratio']:.1f}x  [{r['ci_lower']:.1f}, {r['ci_upper']:.1f}]x")

    print("\n" + "=" * 70)


if __name__ == "__main__":
    main()
