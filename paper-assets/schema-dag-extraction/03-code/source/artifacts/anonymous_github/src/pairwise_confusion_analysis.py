# Pairwise type confusion analysis for exp2:
# Computes confusion matrix from predictions vs gold, correlates with BCS (pairwise cosine similarity).
import json
import logging
import sys
from collections import defaultdict
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import torch
from scipy import stats

sys.path.insert(0, str(Path(__file__).parent))
from few_nerd_utils import load_few_nerd

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

PREDICTIONS_PATH = "./artifacts/predictions_exp2.json"
EMBEDDINGS_PATH = "./data/type_embeddings.pt"
OUTPUT_DIR = Path("./results")
MAX_SAMPLES = 1000


def load_predictions():
    with open(PREDICTIONS_PATH) as f:
        return json.load(f)


def build_confusion_matrix(pred_entries, samples, count_filter=None):
    """Build pairwise confusion counts: C[gold_type][pred_type] = count.

    For each prediction, find matching gold entity by text (exact match).
    If pred.type != gold.type, record confusion.
    Also track gold counts per type for normalization.
    """
    confusion = defaultdict(lambda: defaultdict(int))
    gold_counts = defaultdict(int)

    by_batch_sample = defaultdict(list)
    for p in pred_entries:
        if count_filter and p["count_key"] != count_filter:
            continue
        by_batch_sample[(p["batch_id"], p["sample_id"])].append(p)

    for (batch_id, sid), entries in by_batch_sample.items():
        if sid >= len(samples):
            continue

        entry = entries[0]
        batch_types = set(entry["batch_types"])
        source_text = samples[sid]["text"]
        gold_entities = [e for e in samples[sid]["entities"] if e["type"] in batch_types]
        preds = [p for p in entry.get("predictions", []) if p.get("type") in batch_types]

        for g in gold_entities:
            gold_counts[g["type"]] += 1

        # For each pred, try to find a gold entity with same text but possibly different type
        gold_available = [[g["text"], g["type"], False] for g in gold_entities]

        for pred in preds:
            pt = pred.get("text", "")
            ptype = pred.get("type", "")
            if pt not in source_text:
                continue

            # First try exact match (text + type) - this is a correct prediction, skip
            exact_matched = False
            for g in gold_available:
                if not g[2] and g[0] == pt and g[1] == ptype:
                    g[2] = True
                    exact_matched = True
                    break

            if exact_matched:
                continue

            # Text matches but type differs -> confusion
            for g in gold_available:
                if not g[2] and g[0] == pt and g[1] != ptype:
                    confusion[g[1]][ptype] += 1
                    g[2] = True
                    break

    return confusion, gold_counts


def compute_pairwise_bcs(embeddings_path):
    """Compute pairwise cosine similarity between all type embeddings."""
    emb_dict = torch.load(embeddings_path, map_location="cpu")
    type_names = sorted(emb_dict.keys())
    emb_matrix = torch.stack([emb_dict[t] for t in type_names])
    emb_norm = emb_matrix / emb_matrix.norm(dim=1, keepdim=True)
    sim_matrix = emb_norm @ emb_norm.T
    return type_names, sim_matrix.float().numpy()


def analyze_correlation(confusion, gold_counts, type_names, sim_matrix, label="all"):
    """Compute correlation between pairwise BCS and confusion rate."""
    type_to_idx = {t: i for i, t in enumerate(type_names)}

    bcs_vals = []
    confusion_vals = []
    pair_labels = []

    all_types = sorted(set(list(gold_counts.keys())))

    for i, t1 in enumerate(all_types):
        for j, t2 in enumerate(all_types):
            if t1 == t2:
                continue
            if t1 not in type_to_idx or t2 not in type_to_idx:
                continue

            idx1 = type_to_idx[t1]
            idx2 = type_to_idx[t2]
            bcs = sim_matrix[idx1, idx2]

            # Bidirectional confusion rate
            c_ij = confusion.get(t1, {}).get(t2, 0)
            c_ji = confusion.get(t2, {}).get(t1, 0)
            denom_i = gold_counts.get(t1, 0)
            denom_j = gold_counts.get(t2, 0)

            if denom_i + denom_j == 0:
                continue

            rate = (c_ij + c_ji) / (denom_i + denom_j)

            bcs_vals.append(bcs)
            confusion_vals.append(rate)
            pair_labels.append((t1, t2))

    bcs_arr = np.array(bcs_vals)
    conf_arr = np.array(confusion_vals)

    # Deduplicate symmetric pairs for correlation (keep (A,B) not (B,A))
    seen = set()
    unique_bcs = []
    unique_conf = []
    unique_labels = []
    for bcs, conf, (t1, t2) in zip(bcs_arr, conf_arr, pair_labels):
        key = tuple(sorted([t1, t2]))
        if key not in seen:
            seen.add(key)
            unique_bcs.append(bcs)
            unique_conf.append(conf)
            unique_labels.append((t1, t2))

    bcs_arr = np.array(unique_bcs)
    conf_arr = np.array(unique_conf)

    pearson_r, pearson_p = stats.pearsonr(bcs_arr, conf_arr)
    spearman_r, spearman_p = stats.spearmanr(bcs_arr, conf_arr)

    # Only non-zero confusion pairs for additional stats
    nonzero_mask = conf_arr > 0
    n_nonzero = nonzero_mask.sum()

    result = {
        "label": label,
        "n_pairs": len(bcs_arr),
        "n_nonzero_confusion": int(n_nonzero),
        "pearson_r": float(pearson_r),
        "pearson_p": float(pearson_p),
        "spearman_rho": float(spearman_r),
        "spearman_p": float(spearman_p),
    }

    if n_nonzero > 10:
        sp_nz_r, sp_nz_p = stats.spearmanr(bcs_arr[nonzero_mask], conf_arr[nonzero_mask])
        pe_nz_r, pe_nz_p = stats.pearsonr(bcs_arr[nonzero_mask], conf_arr[nonzero_mask])
        result["pearson_r_nonzero"] = float(pe_nz_r)
        result["pearson_p_nonzero"] = float(pe_nz_p)
        result["spearman_rho_nonzero"] = float(sp_nz_r)
        result["spearman_p_nonzero"] = float(sp_nz_p)

    return result, bcs_arr, conf_arr, unique_labels


def plot_scatter(bcs_arr, conf_arr, pair_labels, corr_result, output_path):
    """Scatter plot of pairwise BCS vs confusion rate with top-10 annotations."""
    fig, ax = plt.subplots(1, 1, figsize=(10, 8))

    nonzero = conf_arr > 0
    zero = ~nonzero

    ax.scatter(bcs_arr[zero], conf_arr[zero], alpha=0.15, s=15, color="gray", label=f"zero confusion (n={zero.sum()})")
    ax.scatter(bcs_arr[nonzero], conf_arr[nonzero], alpha=0.6, s=30, color="tab:red", label=f"nonzero confusion (n={nonzero.sum()})")

    # Annotate top-10
    top_idx = np.argsort(conf_arr)[-10:]
    for idx in top_idx:
        t1, t2 = pair_labels[idx]
        short1 = t1.split("-", 1)[-1][:12]
        short2 = t2.split("-", 1)[-1][:12]
        ax.annotate(f"{short1}↔{short2}", (bcs_arr[idx], conf_arr[idx]),
                     fontsize=7, alpha=0.8, textcoords="offset points", xytext=(5, 5))

    label = corr_result["label"]
    r_str = f"r={corr_result['pearson_r']:.3f} (p={corr_result['pearson_p']:.2e})"
    rho_str = f"ρ={corr_result['spearman_rho']:.3f} (p={corr_result['spearman_p']:.2e})"
    ax.set_title(f"Pairwise BCS vs Confusion Rate [{label}]\n{r_str}, {rho_str}", fontsize=12)
    ax.set_xlabel("Pairwise BCS (cosine similarity)", fontsize=11)
    ax.set_ylabel("Pairwise Confusion Rate (bidirectional)", fontsize=11)
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)

    fig.tight_layout()
    fig.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    logger.info("Saved scatter plot to %s", output_path)


def print_top_confused(confusion, gold_counts, type_names, sim_matrix, n=20):
    """Print top-N most confused type pairs with their BCS."""
    type_to_idx = {t: i for i, t in enumerate(type_names)}

    pair_data = []
    seen = set()
    for gt in confusion:
        for pt in confusion[gt]:
            key = tuple(sorted([gt, pt]))
            if key in seen:
                continue
            seen.add(key)
            c_ij = confusion.get(gt, {}).get(pt, 0)
            c_ji = confusion.get(pt, {}).get(gt, 0)
            total_conf = c_ij + c_ji
            denom = gold_counts.get(gt, 0) + gold_counts.get(pt, 0)
            rate = total_conf / denom if denom > 0 else 0

            if gt in type_to_idx and pt in type_to_idx:
                bcs = sim_matrix[type_to_idx[gt], type_to_idx[pt]]
            else:
                bcs = float("nan")

            pair_data.append((gt, pt, total_conf, rate, bcs, c_ij, c_ji))

    pair_data.sort(key=lambda x: x[2], reverse=True)

    print(f"\n{'Rank':<5} {'Type A':<35} {'Type B':<35} {'Conf':<6} {'Rate':<8} {'BCS':<7} {'A→B':<5} {'B→A':<5}")
    print("-" * 110)
    for i, (t1, t2, total, rate, bcs, c12, c21) in enumerate(pair_data[:n]):
        print(f"{i+1:<5} {t1:<35} {t2:<35} {total:<6} {rate:<8.4f} {bcs:<7.4f} {c12:<5} {c21:<5}")

    return pair_data[:n]


def main():
    logger.info("Loading gold data...")
    samples = load_few_nerd(split="test", max_samples=MAX_SAMPLES)
    logger.info("Loading predictions...")
    preds = load_predictions()
    logger.info("Computing pairwise BCS...")
    type_names, sim_matrix = compute_pairwise_bcs(EMBEDDINGS_PATH)

    results = {}

    for count_filter, label in [(None, "all"), ("count_6", "count_6"), ("count_12", "count_12")]:
        logger.info("=== Analyzing: %s ===", label)
        confusion, gold_counts = build_confusion_matrix(preds, samples, count_filter)

        total_confusions = sum(v for d in confusion.values() for v in d.values())
        logger.info("Total confusion events (%s): %d", label, total_confusions)
        logger.info("Types with gold entities: %d", len(gold_counts))

        corr, bcs_arr, conf_arr, pair_labels = analyze_correlation(
            confusion, gold_counts, type_names, sim_matrix, label
        )
        results[label] = corr

        print(f"\n{'='*60}")
        print(f"  {label.upper()}")
        print(f"{'='*60}")
        print(f"  Total unique type pairs:     {corr['n_pairs']}")
        print(f"  Pairs with nonzero confusion: {corr['n_nonzero_confusion']}")
        print(f"  Pearson  r = {corr['pearson_r']:.4f}  (p = {corr['pearson_p']:.2e})")
        print(f"  Spearman ρ = {corr['spearman_rho']:.4f}  (p = {corr['spearman_p']:.2e})")
        if "pearson_r_nonzero" in corr:
            print(f"  [nonzero only] Pearson  r = {corr['pearson_r_nonzero']:.4f}  (p = {corr['pearson_p_nonzero']:.2e})")
            print(f"  [nonzero only] Spearman ρ = {corr['spearman_rho_nonzero']:.4f}  (p = {corr['spearman_p_nonzero']:.2e})")

        if label == "all":
            plot_scatter(bcs_arr, conf_arr, pair_labels, corr,
                         OUTPUT_DIR / "pairwise_confusion_analysis.png")
            print("\n  Top-20 most confused type pairs (ALL):")
            top_pairs = print_top_confused(confusion, gold_counts, type_names, sim_matrix, n=20)

        elif label == "count_6":
            plot_scatter(bcs_arr, conf_arr, pair_labels, corr,
                         OUTPUT_DIR / "pairwise_confusion_count6.png")
        elif label == "count_12":
            plot_scatter(bcs_arr, conf_arr, pair_labels, corr,
                         OUTPUT_DIR / "pairwise_confusion_count12.png")

    # Save JSON results
    output_json = OUTPUT_DIR / "pairwise_confusion_correlation.json"
    with open(output_json, "w") as f:
        json.dump(results, f, indent=2)
    logger.info("Saved correlation results to %s", output_json)


if __name__ == "__main__":
    main()
