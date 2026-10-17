"""exp-015: Validate embedding SCS as proxy for empirical confusion.

Computes rank correlation (Spearman rho, Kendall tau) between
pairwise embedding similarity and pairwise confusion counts
from exp-002 predictions. Compares Qwen3 vs MiniLM embeddings.
"""
import json
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np
import torch
from scipy import stats

sys.path.insert(0, str(Path(__file__).parent))
from few_nerd_utils import load_few_nerd

BASE = Path(".")
PREDICTIONS = BASE / "artifacts" / "predictions_exp2.json"
QWEN3_SIM = BASE / "artifacts" / "sim_matrix.pt"
MINILM_SIM = BASE / "artifacts" / "fewnerd_bcs_matrix_minilm.pt"
OUTPUT = BASE / "artifacts" / "exp015_scs_validation.json"
MAX_SAMPLES = 1000


def load_sim_matrix(path):
    d = torch.load(path, map_location="cpu")
    type_names = d["type_names"]
    sim = d["sim_matrix"].float().numpy()
    idx = {t: i for i, t in enumerate(type_names)}
    return type_names, sim, idx


def build_confusion(predictions, samples):
    confusion = defaultdict(lambda: defaultdict(int))
    gold_counts = defaultdict(int)

    by_key = defaultdict(list)
    for p in predictions:
        by_key[(p["batch_id"], p["sample_id"])].append(p)

    for (batch_id, sid), entries in by_key.items():
        if sid >= len(samples):
            continue
        entry = entries[0]
        batch_types = set(entry["batch_types"])
        source_text = samples[sid]["text"]
        gold_entities = [e for e in samples[sid]["entities"] if e["type"] in batch_types]
        preds = [p for p in entry.get("predictions", []) if p.get("type") in batch_types]

        for g in gold_entities:
            gold_counts[g["type"]] += 1

        gold_available = [[g["text"], g["type"], False] for g in gold_entities]

        for pred in preds:
            pt = pred.get("text", "")
            ptype = pred.get("type", "")
            if pt.lower() not in source_text.lower():
                continue

            exact = False
            for g in gold_available:
                if not g[2] and g[0] == pt and g[1] == ptype:
                    g[2] = True
                    exact = True
                    break
            if exact:
                continue

            for g in gold_available:
                if not g[2] and g[0] == pt and g[1] != ptype:
                    confusion[g[1]][ptype] += 1
                    g[2] = True
                    break

    return confusion, gold_counts


def correlate(confusion, gold_counts, type_names, sim, idx):
    all_types = sorted(set(gold_counts.keys()))
    scs_vals = []
    conf_vals = []

    for t1 in all_types:
        for t2 in all_types:
            if t1 >= t2:
                continue
            if t1 not in idx or t2 not in idx:
                continue
            c12 = confusion.get(t1, {}).get(t2, 0)
            c21 = confusion.get(t2, {}).get(t1, 0)
            total_conf = c12 + c21
            scs = float(sim[idx[t1], idx[t2]])
            scs_vals.append(scs)
            conf_vals.append(total_conf)

    scs_arr = np.array(scs_vals)
    conf_arr = np.array(conf_vals)

    sp = stats.spearmanr(scs_arr, conf_arr)
    kt = stats.kendalltau(scs_arr, conf_arr)

    result = {
        "n_pairs": len(scs_arr),
        "n_nonzero": int((conf_arr > 0).sum()),
        "total_confusions": int(conf_arr.sum()),
        "spearman_rho": round(float(sp.statistic), 5),
        "spearman_p": float(sp.pvalue),
        "kendall_tau": round(float(kt.statistic), 5),
        "kendall_p": float(kt.pvalue),
    }

    # nonzero-only subset
    nz = conf_arr > 0
    if nz.sum() >= 5:
        sp_nz = stats.spearmanr(scs_arr[nz], conf_arr[nz])
        kt_nz = stats.kendalltau(scs_arr[nz], conf_arr[nz])
        result["nonzero_spearman_rho"] = round(float(sp_nz.statistic), 5)
        result["nonzero_spearman_p"] = float(sp_nz.pvalue)
        result["nonzero_kendall_tau"] = round(float(kt_nz.statistic), 5)
        result["nonzero_kendall_p"] = float(kt_nz.pvalue)

    return result


def main():
    print("Loading gold data...")
    samples = load_few_nerd(split="test", max_samples=MAX_SAMPLES)
    print(f"Loaded {len(samples)} samples")

    print("Loading predictions...")
    with open(PREDICTIONS) as f:
        preds = json.load(f)
    print(f"Loaded {len(preds)} prediction entries")

    print("Building confusion matrix...")
    confusion, gold_counts = build_confusion(preds, samples)
    total = sum(v for d in confusion.values() for v in d.values())
    print(f"Total confusion events: {total}, types with gold: {len(gold_counts)}")

    results = {}

    for name, path in [("qwen3", QWEN3_SIM), ("minilm", MINILM_SIM)]:
        print(f"\nProcessing {name}...")
        type_names, sim, idx = load_sim_matrix(path)
        r = correlate(confusion, gold_counts, type_names, sim, idx)
        results[name] = r

        print(f"  {name} — all pairs (n={r['n_pairs']}, nonzero={r['n_nonzero']}):")
        print(f"    Spearman ρ = {r['spearman_rho']:.4f}  (p = {r['spearman_p']:.2e})")
        print(f"    Kendall  τ = {r['kendall_tau']:.4f}  (p = {r['kendall_p']:.2e})")
        if "nonzero_spearman_rho" in r:
            print(f"  {name} — nonzero only (n={r['n_nonzero']}):")
            print(f"    Spearman ρ = {r['nonzero_spearman_rho']:.4f}  (p = {r['nonzero_spearman_p']:.2e})")
            print(f"    Kendall  τ = {r['nonzero_kendall_tau']:.4f}  (p = {r['nonzero_kendall_p']:.2e})")

    with open(OUTPUT, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved to {OUTPUT}")


if __name__ == "__main__":
    main()
