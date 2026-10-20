#!/usr/bin/env python3
"""J: Calibration (ECE) + Conformal Prediction for entity-level agreement confidence."""

import json, os, math, random
import numpy as np
from collections import Counter, defaultdict

BASE = "/root/autodl-tmp/struct_self_consist_ie"
OUT = f"{BASE}/artifacts/j_calibration"
os.makedirs(OUT, exist_ok=True)

CONFIGS = [
    # SciERC
    dict(name="scierc_qwen8b_s123", path=f"{BASE}/output/exp_018_qwen_scierc_seed123/samples.jsonl", ds="scierc"),
    dict(name="scierc_qwen8b_s456", path=f"{BASE}/output/exp_018_qwen_scierc_seed456/samples.jsonl", ds="scierc"),
    dict(name="scierc_llama8b_s123", path=f"{BASE}/output/exp_018_llama_scierc_seed123/samples.jsonl", ds="scierc"),
    dict(name="scierc_llama8b_s456", path=f"{BASE}/output/exp_018_llama_scierc_seed456/samples.jsonl", ds="scierc"),
    dict(name="scierc_qwen4b", path=f"{BASE}/output/exp_qwen3_4b_scierc_scs_inference/samples.jsonl", ds="scierc"),
    dict(name="scierc_3epoch", path=f"{BASE}/output/exp_029a_scierc_3epoch/samples.jsonl", ds="scierc"),
    # CoNLL
    dict(name="conll_n8_s123", path=f"{BASE}/output/exp_002_conll_n8_seed123/samples.jsonl", ds="conll"),
    dict(name="conll_n8_s456", path=f"{BASE}/output/exp_002_conll_n8_seed456/samples.jsonl", ds="conll"),
    # FewNERD
    dict(name="fewnerd_n8_s123", path=f"{BASE}/output/exp_021_fewnerd_n8_seed123/samples.jsonl", ds="fewnerd"),
    dict(name="fewnerd_n8_s456", path=f"{BASE}/output/exp_021_fewnerd_n8_seed456/samples.jsonl", ds="fewnerd"),
]

FEWNERD_MAX = 5000
N_BINS = 8
ALPHA = 0.1
SEED = 42


def load_data(path, maxn=None):
    out = []
    with open(path) as f:
        for line in f:
            if not line.strip():
                continue
            obj = json.loads(line)
            if not obj["gold"]["entities"]:
                continue
            out.append(obj)
            if maxn and len(out) >= maxn:
                break
    return out


def extract_entities(cfg):
    """Extract per-entity (confidence, is_correct) pairs for one config."""
    maxn = FEWNERD_MAX if cfg["ds"] == "fewnerd" else None
    insts = load_data(cfg["path"], maxn)
    print(f"  {cfg['name']}: {len(insts)} instances", flush=True)

    entities = []
    instance_records = []

    for inst in insts:
        samples = inst["samples"]
        gold = inst["gold"]["entities"]
        N = len(samples)
        if N == 0:
            continue

        gold_set = {(e["start"], e["end"], e["type"]) for e in gold}

        span_cnt = Counter()
        for s in samples:
            seen = set()
            for e in s.get("entities", []):
                k = (e["start"], e["end"], e["type"])
                if k not in seen:
                    span_cnt[k] += 1
                    seen.add(k)

        inst_entities = []
        for k, cnt in span_cnt.items():
            confidence = cnt / N
            is_correct = 1 if k in gold_set else 0
            entities.append({"confidence": confidence, "correct": is_correct,
                             "agreement": cnt, "N": N, "inst_id": inst["id"]})
            inst_entities.append({"key": k, "confidence": confidence,
                                  "correct": is_correct, "agreement": cnt})

        instance_records.append({
            "inst_id": inst["id"],
            "gold_set": gold_set,
            "entities": inst_entities,
            "N": N,
        })

    return entities, instance_records


def compute_ece(entities, n_bins=N_BINS):
    """Compute Expected Calibration Error with uniform bins."""
    if not entities:
        return 0.0, []

    bin_edges = np.linspace(0, 1 + 1e-9, n_bins + 1)
    bins = []
    total = len(entities)

    for i in range(n_bins):
        lo, hi = bin_edges[i], bin_edges[i + 1]
        in_bin = [e for e in entities if lo <= e["confidence"] < hi]
        if not in_bin:
            bins.append({"lo": float(lo), "hi": float(hi), "count": 0,
                         "mean_conf": 0, "mean_acc": 0, "gap": 0})
            continue
        mean_conf = np.mean([e["confidence"] for e in in_bin])
        mean_acc = np.mean([e["correct"] for e in in_bin])
        gap = abs(mean_acc - mean_conf)
        bins.append({
            "lo": float(lo), "hi": float(hi),
            "count": len(in_bin),
            "mean_conf": float(mean_conf),
            "mean_acc": float(mean_acc),
            "gap": float(gap),
        })

    ece = sum(b["count"] / total * b["gap"] for b in bins if b["count"] > 0)
    return float(ece), bins


def compute_conformal(instance_records, alpha=ALPHA, seed=SEED):
    """Conformal prediction at instance level.

    For each instance, the predicted set = {entities with agreement_count/N >= threshold}.
    Coverage = P(all gold entities in predicted set).
    We find threshold via calibration set nonconformity scores.

    Nonconformity score per instance = max over gold entities of (1 - agreement/N),
    or 1.0 if a gold entity is completely missed.
    """
    rng = random.Random(seed)
    indices = list(range(len(instance_records)))
    rng.shuffle(indices)
    split = len(indices) // 2
    cal_idx = indices[:split]
    test_idx = indices[split:]

    cal_scores = []
    for i in cal_idx:
        rec = instance_records[i]
        gold_set = rec["gold_set"]
        ent_map = {e["key"]: e["confidence"] for e in rec["entities"]}

        if not gold_set:
            continue

        max_nonconf = 0.0
        for gk in gold_set:
            if gk in ent_map:
                max_nonconf = max(max_nonconf, 1.0 - ent_map[gk])
            else:
                max_nonconf = 1.0
                break
        cal_scores.append(max_nonconf)

    if not cal_scores:
        return {"coverage": None, "avg_set_size": None, "threshold": None,
                "n_cal": 0, "n_test": 0}

    n = len(cal_scores)
    cal_scores.sort()
    q_idx = min(int(math.ceil((1 - alpha) * (n + 1))) - 1, n - 1)
    q_idx = max(q_idx, 0)
    q_hat = cal_scores[q_idx]
    threshold = 1.0 - q_hat

    covered = 0
    total_test = 0
    set_sizes = []

    for i in test_idx:
        rec = instance_records[i]
        gold_set = rec["gold_set"]
        if not gold_set:
            continue

        predicted_set = {e["key"] for e in rec["entities"] if e["confidence"] >= threshold}
        set_sizes.append(len(predicted_set))

        all_covered = all(gk in predicted_set for gk in gold_set)
        if all_covered:
            covered += 1
        total_test += 1

    coverage = covered / total_test if total_test > 0 else 0.0

    return {
        "coverage": float(coverage),
        "avg_set_size": float(np.mean(set_sizes)) if set_sizes else 0.0,
        "median_set_size": float(np.median(set_sizes)) if set_sizes else 0.0,
        "threshold": float(threshold),
        "quantile_value": float(q_hat),
        "n_cal": n,
        "n_test": total_test,
        "n_covered": covered,
    }


def main():
    print("=" * 60)
    print("J: Calibration + Conformal Prediction Analysis")
    print("=" * 60)

    all_results = {}
    ds_entities = defaultdict(list)
    ds_instances = defaultdict(list)

    for cfg in CONFIGS:
        if not os.path.exists(cfg["path"]):
            print(f"  SKIP {cfg['name']}: file not found")
            continue

        print(f"\nProcessing {cfg['name']}...")
        entities, inst_recs = extract_entities(cfg)

        ece, bins = compute_ece(entities)
        conformal = compute_conformal(inst_recs)

        n_correct = sum(1 for e in entities if e["correct"])
        n_total = len(entities)

        all_results[cfg["name"]] = {
            "dataset": cfg["ds"],
            "n_entities": n_total,
            "n_correct": n_correct,
            "accuracy": n_correct / n_total if n_total else 0,
            "ece": ece,
            "bins": bins,
            "conformal": conformal,
        }

        ds_entities[cfg["ds"]].extend(entities)
        ds_instances[cfg["ds"]].extend(inst_recs)

        print(f"    entities={n_total}, correct={n_correct}, ECE={ece:.4f}")
        print(f"    conformal: coverage={conformal['coverage']:.3f}, "
              f"avg_set={conformal['avg_set_size']:.1f}, "
              f"threshold={conformal['threshold']:.3f}")

    print("\n" + "=" * 60)
    print("Per-dataset aggregated results")
    print("=" * 60)

    ds_results = {}
    for ds in ["scierc", "conll", "fewnerd"]:
        if ds not in ds_entities:
            continue
        ents = ds_entities[ds]
        insts = ds_instances[ds]

        ece, bins = compute_ece(ents)
        conformal = compute_conformal(insts)

        n_correct = sum(1 for e in ents if e["correct"])
        n_total = len(ents)

        ds_results[ds] = {
            "n_entities": n_total,
            "n_correct": n_correct,
            "accuracy": n_correct / n_total if n_total else 0,
            "ece": ece,
            "bins": bins,
            "conformal": conformal,
        }

        print(f"\n{ds.upper()}: {n_total} entities, ECE={ece:.4f}")
        for b in bins:
            if b["count"] > 0:
                print(f"  bin [{b['lo']:.3f}, {b['hi']:.3f}): "
                      f"n={b['count']:5d}, conf={b['mean_conf']:.3f}, "
                      f"acc={b['mean_acc']:.3f}, gap={b['gap']:.3f}")
        print(f"  Conformal (alpha={ALPHA}): "
              f"coverage={conformal['coverage']:.3f}, "
              f"avg_set={conformal['avg_set_size']:.1f}, "
              f"threshold={conformal['threshold']:.3f}")

    calibration_out = {
        "per_config": all_results,
        "per_dataset": ds_results,
        "settings": {"n_bins": N_BINS, "alpha": ALPHA, "seed": SEED},
    }

    cal_path = f"{OUT}/calibration_results.json"
    with open(cal_path, "w") as f:
        json.dump(calibration_out, f, indent=2, default=str)
    print(f"\nSaved: {cal_path}")

    conformal_out = {
        "per_config": {k: v["conformal"] for k, v in all_results.items()},
        "per_dataset": {k: v["conformal"] for k, v in ds_results.items()},
        "settings": {"alpha": ALPHA, "seed": SEED, "split_ratio": 0.5},
    }

    conf_path = f"{OUT}/conformal_results.json"
    with open(conf_path, "w") as f:
        json.dump(conformal_out, f, indent=2, default=str)
    print(f"Saved: {conf_path}")

    print("\n" + "=" * 60)
    print(f"{'Config':<25} {'ECE':>6} {'Cov':>6} {'SetSz':>6} {'Thr':>6}")
    print("-" * 60)
    for name, r in all_results.items():
        c = r["conformal"]
        print(f"{name:<25} {r['ece']:6.4f} {c['coverage']:6.3f} "
              f"{c['avg_set_size']:6.1f} {c['threshold']:6.3f}")
    print("-" * 60)
    for ds, r in ds_results.items():
        c = r["conformal"]
        print(f"{'[AGG] ' + ds.upper():<25} {r['ece']:6.4f} {c['coverage']:6.3f} "
              f"{c['avg_set_size']:6.1f} {c['threshold']:6.3f}")


if __name__ == "__main__":
    main()
