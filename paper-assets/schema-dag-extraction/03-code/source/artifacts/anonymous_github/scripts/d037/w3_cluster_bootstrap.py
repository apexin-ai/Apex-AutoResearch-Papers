"""W3: Type-level cluster bootstrap for pairwise SCS/BCS-confusion correlation.

Input: Few-NERD predictions_exp2.json + type_embeddings.pt; MAVEN predictions + minilm sim matrix
Output: Cluster-robust 95% CIs (B=10,000), comparison with pair-level CIs
Method: Resample types (not pairs) with replacement, reconstruct pairs, compute Pearson r
"""

import json
import sys
import logging
from pathlib import Path
from collections import defaultdict

import numpy as np
import torch
from scipy import stats

ROOT = Path(".")
OUTPUT = ROOT / "scripts" / "d037" / "w3_cluster_bootstrap_results.json"
B = 10_000
SEED = 42

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")
logger = logging.getLogger(__name__)

sys.path.insert(0, str(ROOT / "src"))


def fast_pearsonr(x, y):
    """Pearson r using only numpy — avoids scipy overhead per call."""
    mx, my = x.mean(), y.mean()
    dx, dy = x - mx, y - my
    num = (dx * dy).sum()
    denom = np.sqrt((dx * dx).sum() * (dy * dy).sum())
    if denom == 0:
        return np.nan
    return num / denom


def build_fewnerd_pairwise():
    from few_nerd_utils import load_few_nerd

    logger.info("Loading Few-NERD data...")
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
        gold_entities = [e for e in samples[sid]["entities"] if e["type"] in batch_types]
        pred_entities = [p for p in entry.get("predictions", []) if p.get("type") in batch_types]

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
    n_types = len(all_types)

    pair_bcs, pair_conf, pair_t1, pair_t2 = [], [], [], []
    for i, t1 in enumerate(all_types):
        for j in range(i + 1, n_types):
            t2 = all_types[j]
            if t1 not in type_to_idx or t2 not in type_to_idx:
                continue
            bcs = sim_matrix[type_to_idx[t1], type_to_idx[t2]]
            c12 = confusion.get(t1, {}).get(t2, 0)
            c21 = confusion.get(t2, {}).get(t1, 0)
            denom = gold_counts.get(t1, 0) + gold_counts.get(t2, 0)
            rate = (c12 + c21) / denom if denom > 0 else 0
            pair_bcs.append(float(bcs))
            pair_conf.append(float(rate))
            pair_t1.append(i)
            pair_t2.append(j)

    logger.info("Few-NERD: %d types, %d pairs", n_types, len(pair_bcs))
    return (n_types, np.array(pair_bcs), np.array(pair_conf),
            np.array(pair_t1, dtype=np.int32), np.array(pair_t2, dtype=np.int32))


def build_maven_pairwise():
    import pandas as pd

    logger.info("Loading MAVEN data...")
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
        gold_entities = [e for e in samples[sid]["entities"] if e["type"] in batch_types]
        pred_entities = [p for p in entry.get("predictions", []) if p.get("type") in batch_types]

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

    all_types = sorted(set(gold_counts.keys()))
    n_types = len(all_types)

    pair_scs, pair_conf, pair_t1, pair_t2 = [], [], [], []
    for i, t1 in enumerate(all_types):
        for j in range(i + 1, n_types):
            t2 = all_types[j]
            if t1 not in type_to_idx or t2 not in type_to_idx:
                continue
            scs = sim_matrix[type_to_idx[t1], type_to_idx[t2]]
            c12 = confusion.get(t1, {}).get(t2, 0)
            c21 = confusion.get(t2, {}).get(t1, 0)
            denom = gold_counts.get(t1, 0) + gold_counts.get(t2, 0)
            rate = (c12 + c21) / denom if denom > 0 else 0
            pair_scs.append(float(scs))
            pair_conf.append(float(rate))
            pair_t1.append(i)
            pair_t2.append(j)

    logger.info("MAVEN: %d types, %d pairs", n_types, len(pair_scs))
    return (n_types, np.array(pair_scs), np.array(pair_conf),
            np.array(pair_t1, dtype=np.int32), np.array(pair_t2, dtype=np.int32))


def cluster_bootstrap_fast(n_types, sim_arr, conf_arr, t1_idx, t2_idx, n_boot, seed):
    """Vectorized cluster bootstrap with pure-numpy Pearson r."""
    rng = np.random.RandomState(seed)

    point_r = float(fast_pearsonr(sim_arr, conf_arr))
    logger.info("  Point estimate r=%.6f, starting %d bootstrap iterations...", point_r, n_boot)

    boot_rs = np.empty(n_boot)
    for b in range(n_boot):
        sampled = rng.randint(0, n_types, size=n_types)
        present = np.zeros(n_types, dtype=bool)
        present[sampled] = True
        mask = present[t1_idx] & present[t2_idx]

        if mask.sum() < 3:
            boot_rs[b] = np.nan
            continue

        boot_rs[b] = fast_pearsonr(sim_arr[mask], conf_arr[mask])

        if b % 2000 == 0 and b > 0:
            logger.info("  ... %d/%d iterations done", b, n_boot)

    finite = boot_rs[~np.isnan(boot_rs)]
    ci_lower = float(np.percentile(finite, 2.5))
    ci_upper = float(np.percentile(finite, 97.5))

    return {
        "point_estimate": round(point_r, 6),
        "cluster_ci_lower": round(ci_lower, 6),
        "cluster_ci_upper": round(ci_upper, 6),
        "n_types": int(n_types),
        "n_pairs": int(len(sim_arr)),
        "n_bootstrap": n_boot,
        "n_valid_bootstrap": int(len(finite)),
        "boot_mean": round(float(np.mean(finite)), 6),
        "boot_std": round(float(np.std(finite)), 6),
    }


def main():
    results = {}

    # Few-NERD
    n_fn, bcs_fn, conf_fn, t1_fn, t2_fn = build_fewnerd_pairwise()
    logger.info("Running Few-NERD cluster bootstrap (B=%d)...", B)
    r_fn = cluster_bootstrap_fast(n_fn, bcs_fn, conf_fn, t1_fn, t2_fn, B, SEED)
    r_fn["original_pair_ci"] = {"ci_lower": 0.076, "ci_upper": 0.156}
    results["fewnerd_bcs_confusion"] = r_fn
    logger.info("Few-NERD DONE: r=%.4f, cluster CI [%.4f, %.4f]",
                r_fn["point_estimate"], r_fn["cluster_ci_lower"], r_fn["cluster_ci_upper"])

    # MAVEN
    n_mv, scs_mv, conf_mv, t1_mv, t2_mv = build_maven_pairwise()
    logger.info("Running MAVEN cluster bootstrap (B=%d)...", B)
    r_mv = cluster_bootstrap_fast(n_mv, scs_mv, conf_mv, t1_mv, t2_mv, B, SEED)
    r_mv["original_pair_ci"] = {"ci_lower": 0.104, "ci_upper": 0.156}
    results["maven_minilm_scs_confusion"] = r_mv
    logger.info("MAVEN DONE: r=%.4f, cluster CI [%.4f, %.4f]",
                r_mv["point_estimate"], r_mv["cluster_ci_lower"], r_mv["cluster_ci_upper"])

    for key, r in results.items():
        ci_l, ci_u = r["cluster_ci_lower"], r["cluster_ci_upper"]
        if ci_l > 0:
            r["significance"] = "significant (CI excludes 0)"
        elif ci_u < 0:
            r["significance"] = "significant negative (CI excludes 0)"
        else:
            r["significance"] = "not significant (CI includes 0)"

    with open(OUTPUT, "w") as f:
        json.dump(results, f, indent=2)
    logger.info("Saved -> %s", OUTPUT)

    print("\n" + "=" * 70)
    print("W3: CLUSTER BOOTSTRAP RESULTS (B=%d)" % B)
    print("=" * 70)
    for key, r in results.items():
        print(f"\n{key}:")
        print(f"  r = {r['point_estimate']:.4f}")
        print(f"  Cluster CI (type-level): [{r['cluster_ci_lower']:.4f}, {r['cluster_ci_upper']:.4f}]")
        print(f"  Pair CI (original):      [{r['original_pair_ci']['ci_lower']:.4f}, {r['original_pair_ci']['ci_upper']:.4f}]")
        print(f"  Types: {r['n_types']}, Pairs: {r['n_pairs']}")
        print(f"  Valid: {r['n_valid_bootstrap']}/{r['n_bootstrap']}")
        print(f"  {r['significance']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
