"""EXP-A: Alternative Scorer Validation (Reviewer FR-2)

Re-score existing depth-chain data with Pythia-1.4B or OLMo-1B,
extract 9 surprisal features, merge with 6 text-based features from
existing features.csv, retrain OBD-LightGBM, and compute K* / pairwise AUC.
"""

import argparse
import csv
import json
import logging
import os
import sys
from collections import Counter
from pathlib import Path

import numpy as np
import torch
from scipy import stats
from tqdm import tqdm

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)

SURPRISAL_COLS = [
    "surp_mean", "surp_std", "surp_skew", "surp_kurt",
    "surp_d1_mean", "surp_d1_std", "surp_d1_skew",
    "surp_d2_mean", "surp_d2_std",
]
NON_SURP_COLS = ["ttr", "hapax_ratio", "self_bleu", "freq_kurtosis", "freq_entropy", "low_freq_ratio"]
ALL_FEAT_COLS = SURPRISAL_COLS + NON_SURP_COLS


def load_jsonl(path: Path):
    with open(path) as f:
        return [json.loads(line) for line in f]


def compute_surprisal_features(model, tokenizer, texts, batch_size=8):
    """Compute 9-dim surprisal statistics per text using batched inference."""
    all_features = []
    for start in tqdm(range(0, len(texts), batch_size), desc="Surprisal"):
        batch_texts = texts[start : start + batch_size]
        inputs = tokenizer(
            batch_texts,
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=512,
        ).to(model.device)

        with torch.no_grad():
            logits = model(**inputs).logits

        log_probs = torch.log_softmax(logits, dim=-1)
        input_ids = inputs["input_ids"]

        for i in range(len(batch_texts)):
            mask = inputs["attention_mask"][i].bool()
            seq_len = mask.sum().item()
            if seq_len < 3:
                all_features.append([0.0] * 9)
                continue

            offset = input_ids.shape[1] - seq_len
            token_ids = input_ids[i, offset:]
            token_log_probs = []
            for t in range(1, seq_len):
                lp = log_probs[i, offset + t - 1, token_ids[t]].item()
                token_log_probs.append(-lp)

            arr = np.array(token_log_probs)
            if len(arr) < 3:
                all_features.append([0.0] * 9)
                continue

            d1 = np.diff(arr)
            d2 = np.diff(d1) if len(d1) > 1 else np.array([0.0])

            feats = [
                float(np.mean(arr)),
                float(np.std(arr)),
                float(stats.skew(arr)),
                float(stats.kurtosis(arr)),
                float(np.mean(d1)),
                float(np.std(d1)),
                float(stats.skew(d1)) if len(d1) >= 3 else 0.0,
                float(np.mean(d2)),
                float(np.std(d2)),
            ]
            all_features.append(feats)

        torch.cuda.empty_cache()

    return all_features


def load_non_surprisal_features(features_csv: Path):
    """Load non-surprisal columns from existing features.csv keyed by (doc_id, depth)."""
    lookup = {}
    with open(features_csv) as f:
        reader = csv.DictReader(f)
        for row in reader:
            key = (int(row["doc_id"]), int(row["depth"]))
            vals = []
            for col in NON_SURP_COLS:
                v = row[col]
                vals.append(float(v) if v != "" and v != "nan" else np.nan)
            lookup[key] = vals
    return lookup


def run_pairwise_auc(feat_matrix, depths, doc_ids, max_depth):
    """Pairwise AUC with 5-fold GroupKFold LightGBM."""
    import lightgbm as lgb
    from sklearn.metrics import roc_auc_score
    from sklearn.model_selection import GroupKFold

    pairwise_auc = {}
    pairwise_auc_folds = {}

    for k in range(1, max_depth + 1):
        mask = (depths == k - 1) | (depths == k)
        X = feat_matrix[mask]
        y = (depths[mask] == k).astype(int)
        if len(np.unique(y)) < 2:
            pairwise_auc[f"{k-1}v{k}"] = float("nan")
            continue

        gkf = GroupKFold(n_splits=5)
        groups = doc_ids[mask]
        fold_aucs = []
        for train_idx, test_idx in gkf.split(X, y, groups=groups):
            clf = lgb.LGBMClassifier(
                n_estimators=200, max_depth=6, learning_rate=0.05,
                num_leaves=31, verbose=-1, n_jobs=-1,
            )
            clf.fit(X[train_idx], y[train_idx])
            proba = clf.predict_proba(X[test_idx])[:, 1]
            fold_aucs.append(roc_auc_score(y[test_idx], proba))
        auc_mean = float(np.mean(fold_aucs))
        pairwise_auc[f"{k-1}v{k}"] = round(auc_mean, 4)
        pairwise_auc_folds[f"{k-1}v{k}"] = [round(a, 4) for a in fold_aucs]
        log.info(f"  AUC({k-1} vs {k}) = {auc_mean:.4f} ± {np.std(fold_aucs):.4f}")

    return pairwise_auc, pairwise_auc_folds


def run_ordinal_and_importance(feat_matrix, depths, doc_ids, max_depth):
    """Ordinal 6-class LightGBM → feature importance."""
    import lightgbm as lgb
    from sklearn.metrics import accuracy_score, mean_absolute_error
    from sklearn.model_selection import GroupKFold

    gkf = GroupKFold(n_splits=5)
    all_preds = np.zeros_like(depths, dtype=float)
    importances = np.zeros(len(ALL_FEAT_COLS))

    for train_idx, test_idx in gkf.split(feat_matrix, depths, groups=doc_ids):
        clf = lgb.LGBMClassifier(
            n_estimators=300, max_depth=8, learning_rate=0.05,
            num_leaves=63, verbose=-1, n_jobs=-1,
            num_class=max_depth + 1,
            objective="multiclass",
        )
        clf.fit(feat_matrix[train_idx], depths[train_idx])
        preds = clf.predict(feat_matrix[test_idx])
        all_preds[test_idx] = preds
        importances += clf.feature_importances_

    importances /= 5.0
    mae = float(mean_absolute_error(depths, all_preds))
    accuracy = float(accuracy_score(depths, all_preds.astype(int)))

    feat_imp = sorted(
        [{"feature": ALL_FEAT_COLS[i], "importance": float(importances[i])}
         for i in range(len(ALL_FEAT_COLS))],
        key=lambda x: x["importance"], reverse=True,
    )

    return mae, accuracy, feat_imp, importances


def compute_spearman_rho(new_importances, baseline_importances_json):
    """Spearman ρ between two feature importance rankings (all 15 features)."""
    baseline_rank = {}
    for rank, item in enumerate(baseline_importances_json):
        baseline_rank[item["feature"]] = rank

    new_sorted = sorted(
        [{"feature": ALL_FEAT_COLS[i], "importance": float(new_importances[i])}
         for i in range(len(ALL_FEAT_COLS))],
        key=lambda x: x["importance"], reverse=True,
    )
    new_rank = {}
    for rank, item in enumerate(new_sorted):
        new_rank[item["feature"]] = rank

    # All 15 features ranked
    features = ALL_FEAT_COLS
    ranks_new = [new_rank[f] for f in features]
    ranks_base = [baseline_rank.get(f, len(features)) for f in features]

    rho, pval = stats.spearmanr(ranks_new, ranks_base)
    return float(rho), float(pval)


def main():
    parser = argparse.ArgumentParser(description="EXP-A: Alternative Scorer Validation")
    parser.add_argument("--scorer_model_path", type=str, required=True)
    parser.add_argument("--data_dir", type=str, required=True)
    parser.add_argument("--output_dir", type=str, required=True)
    parser.add_argument("--baseline_importance_json", type=str, default=None,
                        help="Path to baseline feature_importance.json for Spearman ρ")
    parser.add_argument("--device", type=str, default="cuda:0")
    parser.add_argument("--batch_size", type=int, default=8)
    parser.add_argument("--max_depth", type=int, default=5)
    args = parser.parse_args()

    data_dir = Path(args.data_dir)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    scorer_name = Path(args.scorer_model_path).name
    log.info(f"Scorer: {scorer_name}")
    log.info(f"Data: {data_dir}")

    # --- Load scorer model ---
    from transformers import AutoModelForCausalLM, AutoTokenizer

    log.info("Loading scorer tokenizer ...")
    tokenizer = AutoTokenizer.from_pretrained(args.scorer_model_path, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
        tokenizer.pad_token_id = tokenizer.eos_token_id
    tokenizer.padding_side = "left"

    log.info("Loading scorer model ...")
    model = AutoModelForCausalLM.from_pretrained(
        args.scorer_model_path,
        torch_dtype=torch.float16,
        device_map=args.device,
        trust_remote_code=True,
    )
    model.eval()
    log.info(f"Model loaded on {model.device}")

    # --- Load non-surprisal features from existing features.csv ---
    features_csv = data_dir / "features.csv"
    log.info(f"Loading non-surprisal features from {features_csv} ...")
    non_surp_lookup = load_non_surprisal_features(features_csv)

    # --- Compute surprisal features per depth ---
    all_rows = []
    for d in range(args.max_depth + 1):
        jsonl_path = data_dir / f"depth_{d}.jsonl"
        records = load_jsonl(jsonl_path)
        texts = [r["text"] for r in records]
        doc_ids = [r["doc_id"] for r in records]
        log.info(f"  depth {d}: {len(texts)} texts")

        surp_feats = compute_surprisal_features(model, tokenizer, texts, batch_size=args.batch_size)

        for i in range(len(texts)):
            row = {"doc_id": doc_ids[i], "depth": d}
            for j, col in enumerate(SURPRISAL_COLS):
                row[col] = surp_feats[i][j]
            non_surp = non_surp_lookup.get((doc_ids[i], d))
            if non_surp is not None:
                for j, col in enumerate(NON_SURP_COLS):
                    row[col] = non_surp[j]
            else:
                for col in NON_SURP_COLS:
                    row[col] = 0.0
            all_rows.append(row)

    # --- Free GPU memory ---
    del model
    torch.cuda.empty_cache()
    log.info("Scorer model unloaded, GPU memory freed")

    # --- Build feature matrix ---
    depths = np.array([r["depth"] for r in all_rows])
    doc_ids_arr = np.array([r["doc_id"] for r in all_rows])
    feat_matrix = np.array(
        [[float(r[c]) if not np.isnan(float(r[c])) else 0.0 for c in ALL_FEAT_COLS] for r in all_rows]
    )
    col_means = np.nanmean(feat_matrix, axis=0)
    for j in range(feat_matrix.shape[1]):
        mask = np.isnan(feat_matrix[:, j])
        if mask.any():
            feat_matrix[mask, j] = col_means[j]

    # --- Save new features.csv ---
    feat_csv_out = output_dir / "features.csv"
    with open(feat_csv_out, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["doc_id", "depth"] + ALL_FEAT_COLS)
        writer.writeheader()
        writer.writerows(all_rows)
    log.info(f"Saved {len(all_rows)} rows to {feat_csv_out}")

    # --- Pairwise AUC ---
    log.info("Computing pairwise AUC ...")
    pairwise_auc, pairwise_auc_folds = run_pairwise_auc(
        feat_matrix, depths, doc_ids_arr, args.max_depth
    )

    # --- K* ---
    k_star = 0
    for k in range(1, args.max_depth + 1):
        key = f"{k-1}v{k}"
        if pairwise_auc.get(key, 0) > 0.60:
            k_star = k
    log.info(f"K* = {k_star}")

    # --- Ordinal + Feature Importance ---
    log.info("Running ordinal classification ...")
    mae, accuracy, feat_imp, raw_importances = run_ordinal_and_importance(
        feat_matrix, depths, doc_ids_arr, args.max_depth
    )
    log.info(f"Ordinal MAE={mae:.4f}, Accuracy={accuracy:.4f}")

    # --- Spearman ρ with baseline ---
    spearman_rho = None
    spearman_pval = None
    if args.baseline_importance_json and os.path.exists(args.baseline_importance_json):
        with open(args.baseline_importance_json) as f:
            baseline_imp = json.load(f)
        spearman_rho, spearman_pval = compute_spearman_rho(raw_importances, baseline_imp)
        log.info(f"Spearman ρ vs baseline = {spearman_rho:.4f} (p={spearman_pval:.4f})")

    # --- Save results ---
    results = {
        "scorer": scorer_name,
        "data_dir": str(data_dir),
        "k_star": k_star,
        "pairwise_auc": pairwise_auc,
        "pairwise_auc_folds": pairwise_auc_folds,
        "ordinal_mae": round(mae, 4),
        "ordinal_accuracy": round(accuracy, 4),
        "feature_importance": feat_imp[:10],
        "feature_importance_all": feat_imp,
        "spearman_rho_vs_baseline": round(spearman_rho, 4) if spearman_rho is not None else None,
        "spearman_pval": round(spearman_pval, 4) if spearman_pval is not None else None,
    }

    out_json = output_dir / "results.json"
    with open(out_json, "w") as f:
        json.dump(results, f, indent=2)
    log.info(f"Results saved to {out_json}")

    # --- Print summary ---
    print("\n" + "=" * 60)
    print(f"EXP-A Alternative Scorer: {scorer_name}")
    print(f"Dataset: {data_dir.name}")
    print("=" * 60)
    print(f"\nK* = {k_star}  (threshold θ=0.60)")
    print("\nPairwise AUC:")
    for k in range(1, args.max_depth + 1):
        key = f"{k-1}v{k}"
        folds = pairwise_auc_folds.get(key, [])
        std = float(np.std(folds)) if folds else 0.0
        print(f"  {key}: {pairwise_auc.get(key, 'N/A'):.4f} ± {std:.4f}")
    print(f"\nOrdinal: MAE={mae:.4f}, Acc={accuracy:.4f}")
    print("\nTop-5 Feature Importance:")
    for fi in feat_imp[:5]:
        print(f"  {fi['feature']:20s} {fi['importance']:.1f}")
    if spearman_rho is not None:
        print(f"\nSpearman ρ vs Qwen-scored baseline: {spearman_rho:.4f} (p={spearman_pval:.4f})")
    print("=" * 60)


if __name__ == "__main__":
    main()
