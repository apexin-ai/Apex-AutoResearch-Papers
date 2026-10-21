"""MiniLM embedding ablation for Few-NERD: compute BCS matrix + compare with Qwen3."""
import json
import sys
from pathlib import Path
from collections import defaultdict

import numpy as np
import torch
from scipy import stats

sys.path.insert(0, str(Path(__file__).parent))
from few_nerd_utils import load_few_nerd

ROOT = Path(".")


def text_match(pred, gold, source_text=""):
    if pred.get("type") != gold["type"]:
        return False
    pt = pred.get("text", "").strip()
    gt = gold.get("text", "").strip()
    if not pt or not gt:
        return False
    if source_text and pt.lower() not in source_text.lower():
        return False
    pl, gl = pt.lower(), gt.lower()
    return pl == gl or pl in gl or gl in pl


def main():
    # --- Step 1: Load types ---
    with open(ROOT / "configs" / "few_nerd_types.json") as f:
        type_dict = json.load(f)
    type_names_config = list(type_dict.keys())
    print(f"[1] Loaded {len(type_names_config)} types from config")

    # --- Step 2: Compute MiniLM embeddings ---
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer('~/.cache/huggingface/models--sentence-transformers--all-MiniLM-L6-v2/snapshots/c9745ed1d9f207416be6d2e6f8de32d1f16199bf')
    readable_names = [t.replace('-', ' ').replace('/', ' / ') for t in type_names_config]
    embeddings = model.encode(readable_names, convert_to_tensor=True, device='cpu')
    print(f"[2] MiniLM embeddings shape: {embeddings.shape}")

    # Cosine similarity matrix
    embs_norm = embeddings / embeddings.norm(dim=1, keepdim=True)
    sim_minilm = embs_norm @ embs_norm.T
    print(f"[2] MiniLM sim matrix shape: {sim_minilm.shape}")

    # Save - match format of sim_matrix.pt
    type_to_idx = {t: i for i, t in enumerate(type_names_config)}
    torch.save({
        'sim_matrix': sim_minilm.cpu(),
        'type_names': type_names_config,
        'type_to_idx': type_to_idx,
        'model': 'all-MiniLM-L6-v2',
        'embeddings': embeddings.cpu(),
    }, ROOT / "artifacts" / "fewnerd_bcs_matrix_minilm.pt")
    print("[2] Saved artifacts/fewnerd_bcs_matrix_minilm.pt")

    # --- Step 3: Load Qwen3 sim matrix ---
    qwen3_data = torch.load(ROOT / "artifacts" / "sim_matrix.pt", map_location='cpu', weights_only=False)
    sim_qwen3 = qwen3_data['sim_matrix']
    qwen3_types = qwen3_data['type_names']
    print(f"[3] Qwen3 sim matrix: {sim_qwen3.shape}, {len(qwen3_types)} types")

    # Align type ordering: MiniLM uses config order, Qwen3 uses its own order
    # Build aligned MiniLM matrix in Qwen3 type order for comparison
    minilm_idx_map = {t: i for i, t in enumerate(type_names_config)}
    qwen3_to_minilm = [minilm_idx_map[t] for t in qwen3_types]
    sim_minilm_aligned = sim_minilm[qwen3_to_minilm][:, qwen3_to_minilm]

    # --- Step 4: Compare BCS distributions ---
    n = len(qwen3_types)
    mask = ~torch.eye(n, dtype=torch.bool)
    q3_off = sim_qwen3[mask].numpy()
    ml_off = sim_minilm_aligned[mask].numpy()

    print("\n=== BCS Distribution Comparison ===")
    print(f"{'Metric':<20} {'Qwen3':>10} {'MiniLM':>10}")
    print("-" * 42)
    for name, func in [('mean', np.mean), ('std', np.std), ('min', np.min),
                        ('max', np.max), ('median', np.median)]:
        print(f"{name:<20} {func(q3_off):>10.4f} {func(ml_off):>10.4f}")

    # Correlation between the two matrices (off-diagonal)
    matrix_corr, matrix_p = stats.pearsonr(q3_off, ml_off)
    matrix_spearman, matrix_sp = stats.spearmanr(q3_off, ml_off)
    print(f"\nMatrix correlation (off-diag pairs):")
    print(f"  Pearson r={matrix_corr:.4f}, p={matrix_p:.2e}")
    print(f"  Spearman ρ={matrix_spearman:.4f}, p={matrix_sp:.2e}")

    # Top-10 most similar pairs for each
    pairs = []
    for i in range(n):
        for j in range(i+1, n):
            pairs.append((qwen3_types[i], qwen3_types[j], sim_qwen3[i,j].item(), sim_minilm_aligned[i,j].item()))

    top10_q3 = sorted(pairs, key=lambda x: x[2], reverse=True)[:10]
    top10_ml = sorted(pairs, key=lambda x: x[3], reverse=True)[:10]

    print("\n--- Top-10 highest BCS pairs (Qwen3) ---")
    for t1, t2, bq, bm in top10_q3:
        print(f"  {t1} <-> {t2}: Qwen3={bq:.4f}, MiniLM={bm:.4f}")

    print("\n--- Top-10 highest BCS pairs (MiniLM) ---")
    for t1, t2, bq, bm in top10_ml:
        print(f"  {t1} <-> {t2}: MiniLM={bm:.4f}, Qwen3={bq:.4f}")

    # Overlap in top-10
    q3_set = set((p[0], p[1]) for p in top10_q3)
    ml_set = set((p[0], p[1]) for p in top10_ml)
    overlap = q3_set & ml_set
    print(f"\nTop-10 overlap: {len(overlap)}/10 pairs")

    # --- Step 5: Per-type F1 vs mean_BCS (MiniLM) ---
    print("\n=== Per-type F1 vs BCS (MiniLM) ===")

    # Compute mean_BCS for each type (MiniLM)
    mean_bcs_minilm = {}
    for i, t in enumerate(type_names_config):
        sims = [sim_minilm[i, j].item() for j in range(len(type_names_config)) if j != i]
        mean_bcs_minilm[t] = np.mean(sims)

    # Also compute mean_BCS for Qwen3 for comparison
    mean_bcs_qwen3 = {}
    qwen3_idx_map = {t: i for i, t in enumerate(qwen3_types)}
    for t in qwen3_types:
        i = qwen3_idx_map[t]
        sims = [sim_qwen3[i, j].item() for j in range(n) if j != i]
        mean_bcs_qwen3[t] = np.mean(sims)

    # Load predictions and test data
    preds = json.load(open(ROOT / "artifacts" / "predictions_exp2.json"))
    samples = load_few_nerd("test")
    print(f"Loaded {len(preds)} prediction entries, {len(samples)} test samples")

    # Compute per-type TP/FP/FN across all batches
    type_stats = defaultdict(lambda: {"tp": 0, "fp": 0, "fn": 0, "batch_f1s": [], "n_batches": 0})

    for entry in preds:
        batch_types = entry["batch_types"]
        sid = entry["sample_id"]
        if sid >= len(samples):
            continue
        sample = samples[sid]
        source_text = sample.get("text", "")
        gold_entities = [e for e in sample["entities"] if e["type"] in batch_types]
        pred_entities = [p for p in entry.get("predictions", []) if p.get("type") in batch_types]

        matched_gold = set()
        matched_pred = set()
        for pi, pred in enumerate(pred_entities):
            for gi, gold in enumerate(gold_entities):
                if gi not in matched_gold and text_match(pred, gold, source_text):
                    matched_gold.add(gi)
                    matched_pred.add(pi)
                    type_stats[gold["type"]]["tp"] += 1
                    break

        for pi, pred in enumerate(pred_entities):
            if pi not in matched_pred:
                t = pred.get("type")
                if t in type_stats or t in set(batch_types):
                    type_stats[t]["fp"] += 1

        for gi, gold in enumerate(gold_entities):
            if gi not in matched_gold:
                type_stats[gold["type"]]["fn"] += 1

    # Compute per-type F1 and correlations
    rows = []
    for t in type_names_config:
        if t not in type_stats:
            continue
        s = type_stats[t]
        tp, fp, fn = s["tp"], s["fp"], s["fn"]
        freq = tp + fn
        if freq < 5:
            continue
        p = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        r = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        f1 = 2 * p * r / (p + r) if (p + r) > 0 else 0.0
        rows.append({
            "type": t,
            "f1": f1,
            "precision": p,
            "recall": r,
            "freq": freq,
            "mean_bcs_minilm": mean_bcs_minilm.get(t, 0),
            "mean_bcs_qwen3": mean_bcs_qwen3.get(t, 0),
        })

    print(f"Types with freq>=5: {len(rows)}")

    f1_arr = np.array([r["f1"] for r in rows])
    bcs_ml_arr = np.array([r["mean_bcs_minilm"] for r in rows])
    bcs_q3_arr = np.array([r["mean_bcs_qwen3"] for r in rows])
    freq_arr = np.array([r["freq"] for r in rows])
    log_freq = np.log1p(freq_arr)

    # Correlations: MiniLM
    sp_ml, sp_ml_p = stats.spearmanr(bcs_ml_arr, f1_arr)
    pr_ml, pr_ml_p = stats.pearsonr(bcs_ml_arr, f1_arr)
    print(f"\nMiniLM: Spearman ρ(mean_BCS, F1) = {sp_ml:.4f}, p={sp_ml_p:.4f}")
    print(f"MiniLM: Pearson  r(mean_BCS, F1) = {pr_ml:.4f}, p={pr_ml_p:.4f}")

    # Correlations: Qwen3 (re-computed for validation)
    sp_q3, sp_q3_p = stats.spearmanr(bcs_q3_arr, f1_arr)
    pr_q3, pr_q3_p = stats.pearsonr(bcs_q3_arr, f1_arr)
    print(f"\nQwen3:  Spearman ρ(mean_BCS, F1) = {sp_q3:.4f}, p={sp_q3_p:.4f}")
    print(f"Qwen3:  Pearson  r(mean_BCS, F1) = {pr_q3:.4f}, p={pr_q3_p:.4f}")

    # Correlation between MiniLM and Qwen3 mean_BCS per type
    bcs_corr, bcs_corr_p = stats.pearsonr(bcs_ml_arr, bcs_q3_arr)
    bcs_sp, bcs_sp_p = stats.spearmanr(bcs_ml_arr, bcs_q3_arr)
    print(f"\nmean_BCS correlation (MiniLM vs Qwen3):")
    print(f"  Pearson r={bcs_corr:.4f}, p={bcs_corr_p:.2e}")
    print(f"  Spearman ρ={bcs_sp:.4f}, p={bcs_sp_p:.2e}")

    # Partial correlation (controlling log_freq) for MiniLM
    from numpy.linalg import lstsq
    Z = np.column_stack([log_freq, np.ones(len(log_freq))])
    res_bcs_ml = bcs_ml_arr - Z @ lstsq(Z, bcs_ml_arr, rcond=None)[0]
    res_f1 = f1_arr - Z @ lstsq(Z, f1_arr, rcond=None)[0]
    partial_r_ml, partial_p_ml = stats.pearsonr(res_bcs_ml, res_f1)
    print(f"\nMiniLM partial r(BCS, F1 | log_freq) = {partial_r_ml:.4f}, p={partial_p_ml:.4f}")

    res_bcs_q3 = bcs_q3_arr - Z @ lstsq(Z, bcs_q3_arr, rcond=None)[0]
    partial_r_q3, partial_p_q3 = stats.pearsonr(res_bcs_q3, res_f1)
    print(f"Qwen3  partial r(BCS, F1 | log_freq) = {partial_r_q3:.4f}, p={partial_p_q3:.4f}")

    # Confound checks
    r_bcs_freq_ml, _ = stats.pearsonr(bcs_ml_arr, log_freq)
    r_bcs_freq_q3, _ = stats.pearsonr(bcs_q3_arr, log_freq)
    print(f"\nConfound r(mean_BCS, log_freq): MiniLM={r_bcs_freq_ml:.4f}, Qwen3={r_bcs_freq_q3:.4f}")

    # --- Step 6: Save results ---
    output = {
        "n_types_analyzed": len(rows),
        "min_freq_threshold": 5,
        "bcs_distribution": {
            "qwen3": {"mean": float(np.mean(q3_off)), "std": float(np.std(q3_off)),
                       "min": float(np.min(q3_off)), "max": float(np.max(q3_off))},
            "minilm": {"mean": float(np.mean(ml_off)), "std": float(np.std(ml_off)),
                        "min": float(np.min(ml_off)), "max": float(np.max(ml_off))},
            "matrix_pearson_r": float(matrix_corr),
            "matrix_spearman_rho": float(matrix_spearman),
        },
        "top10_overlap": len(overlap),
        "per_type_correlations": {
            "minilm": {
                "spearman": {"rho": float(sp_ml), "p": float(sp_ml_p)},
                "pearson": {"r": float(pr_ml), "p": float(pr_ml_p)},
                "partial_controlling_log_freq": {"r": float(partial_r_ml), "p": float(partial_p_ml)},
            },
            "qwen3": {
                "spearman": {"rho": float(sp_q3), "p": float(sp_q3_p)},
                "pearson": {"r": float(pr_q3), "p": float(pr_q3_p)},
                "partial_controlling_log_freq": {"r": float(partial_r_q3), "p": float(partial_p_q3)},
            },
        },
        "mean_bcs_cross_embedding_corr": {
            "pearson_r": float(bcs_corr),
            "spearman_rho": float(bcs_sp),
        },
        "per_type_table": sorted(
            [{k: (float(v) if isinstance(v, (np.floating, float)) else v) for k, v in r.items()} for r in rows],
            key=lambda x: x["mean_bcs_minilm"], reverse=True
        ),
    }
    out_path = ROOT / "artifacts" / "embedding_ablation_fewnerd.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\n[6] Saved {out_path}")
    print("\nDONE.")


if __name__ == "__main__":
    main()
