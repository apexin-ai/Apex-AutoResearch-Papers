"""
OLMo-1B C4 cross-scorer experiment.

Cross-scoring OLMo-1B C4 generations with Qwen2.5-1.5B-Instruct scorer.
Uses pre-computed cross-scored features from data/olmo_c4_qwen_scorer/.

Pipeline:
  1. Load cached 15D features (9 surprisal + 6 text-based)
  2. Pairwise LightGBM (GroupKFold 5-fold OOF)
  3. Bootstrap CI (10000 doc-level resamples) + permutation test (10000)
  4. K* with Bonferroni correction (alpha=0.05/5=0.01)
"""
import argparse
import csv
import json
import os
import time
import logging
from pathlib import Path

import numpy as np
import lightgbm as lgb
from sklearn.model_selection import GroupKFold
from sklearn.metrics import roc_auc_score
from scipy import stats as sp_stats

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)

ROOT = Path("/root/autodl-tmp/gen-depth-contamination")
SCORER_PATH = "/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B-Instruct"
DATA_DIR = ROOT / "data" / "olmo1b_c4_10k"
CACHED_FEATURES = ROOT / "data" / "olmo_c4_qwen_scorer" / "features.csv"
OUT_DIR = ROOT / "results" / "olmo_c4_cross_scorer"

SURPRISAL_COLS = [
    "surp_mean", "surp_std", "surp_skew", "surp_kurt",
    "surp_d1_mean", "surp_d1_std", "surp_d1_skew",
    "surp_d2_mean", "surp_d2_std",
]
TEXT_COLS = ["ttr", "hapax_ratio", "self_bleu", "freq_kurtosis", "freq_entropy", "low_freq_ratio"]
ALL_FEAT_COLS = SURPRISAL_COLS + TEXT_COLS

MAX_DEPTH = 5
N_BOOT = 10000
N_PERM = 10000
THETA = 0.60
SEED = 42
N_PAIRS = 5
BONFERRONI_ALPHA = 0.05 / N_PAIRS


def load_jsonl(path):
    with open(path) as f:
        return [json.loads(line) for line in f]


def load_text_features(csv_path):
    with open(csv_path) as f:
        rows = list(csv.DictReader(f))
    result = {}
    for r in rows:
        key = (str(r["doc_id"]), int(r["depth"]))
        result[key] = {col: r[col] for col in TEXT_COLS}
    return result


def compute_surprisal_features(model, tokenizer, texts, batch_size=16):
    import torch
    all_features = []
    for start in range(0, len(texts), batch_size):
        batch_texts = texts[start:start + batch_size]
        inputs = tokenizer(
            batch_texts, return_tensors="pt", padding=True,
            truncation=True, max_length=512,
        )
        inputs = {k: v.to(model.device) for k, v in inputs.items()}
        with torch.no_grad():
            logits = model(**inputs).logits
        log_probs = torch.log_softmax(logits, dim=-1)
        input_ids = inputs["input_ids"]
        for i in range(len(batch_texts)):
            attn_mask = inputs["attention_mask"][i].bool()
            seq_len = attn_mask.sum().item()
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
            if len(arr) < 2:
                all_features.append([0.0] * 9)
                continue
            d1 = np.diff(arr)
            d2 = np.diff(d1) if len(d1) > 1 else np.array([0.0])
            feats = [
                float(np.mean(arr)), float(np.std(arr)),
                float(sp_stats.skew(arr)), float(sp_stats.kurtosis(arr)),
                float(np.mean(d1)), float(np.std(d1)),
                float(sp_stats.skew(d1)) if len(d1) >= 3 else 0.0,
                float(np.mean(d2)), float(np.std(d2)),
            ]
            all_features.append(feats)
        torch.cuda.empty_cache()
    return all_features


def score_all_depths(skip_scoring=False, device="cuda:2"):
    if skip_scoring and CACHED_FEATURES.exists():
        log.info(f"Using cached cross-scored features: {CACHED_FEATURES}")
        with open(CACHED_FEATURES) as f:
            return list(csv.DictReader(f))

    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer

    log.info(f"Loading scorer: {SCORER_PATH}")
    tokenizer = AutoTokenizer.from_pretrained(SCORER_PATH, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        SCORER_PATH, torch_dtype=torch.float16, device_map=device,
        trust_remote_code=True,
    )
    model.eval()
    log.info(f"Scorer loaded on {model.device}")

    text_feats = load_text_features(DATA_DIR / "features.csv")
    log.info(f"Loaded {len(text_feats)} text-based feature rows")

    rows = []
    for d in range(MAX_DEPTH + 1):
        records = load_jsonl(DATA_DIR / f"depth_{d}.jsonl")
        texts = [r["text"] for r in records]
        doc_ids_list = [r["doc_id"] for r in records]
        log.info(f"depth {d}: scoring {len(texts)} texts with Qwen-Instruct")
        surp_feats = compute_surprisal_features(model, tokenizer, texts, batch_size=16)
        for i in range(len(texts)):
            key = (str(doc_ids_list[i]), d)
            tf = text_feats.get(key, {col: "0.0" for col in TEXT_COLS})
            row = {"doc_id": doc_ids_list[i], "depth": d}
            for j, col in enumerate(SURPRISAL_COLS):
                row[col] = surp_feats[i][j]
            for col in TEXT_COLS:
                row[col] = float(tf[col]) if tf[col] not in ("", "nan") else 0.0
            rows.append(row)

    del model
    torch.cuda.empty_cache()
    import gc; gc.collect()
    log.info("Scorer unloaded")

    feat_path = OUT_DIR / "features_cross_scored.csv"
    with open(feat_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["doc_id", "depth"] + ALL_FEAT_COLS)
        writer.writeheader()
        writer.writerows(rows)
    log.info(f"Saved {len(rows)} rows to {feat_path}")
    return rows


def rows_to_arrays(feat_rows):
    doc_ids_raw = [r["doc_id"] for r in feat_rows]
    try:
        doc_ids = np.array([int(d) for d in doc_ids_raw])
    except (ValueError, TypeError):
        uid_map = {d: i for i, d in enumerate(sorted(set(doc_ids_raw)))}
        doc_ids = np.array([uid_map[d] for d in doc_ids_raw])
    depths = np.array([int(r["depth"]) for r in feat_rows])
    X = np.array([
        [float(r[c]) if str(r[c]) not in ("", "nan") else np.nan for c in ALL_FEAT_COLS]
        for r in feat_rows
    ])
    col_means = np.nanmean(X, axis=0)
    for j in range(X.shape[1]):
        mask = np.isnan(X[:, j])
        if mask.any():
            X[mask, j] = col_means[j]
    return X, depths, doc_ids


def get_oof_predictions(X, y, groups):
    gkf = GroupKFold(n_splits=5)
    oof_proba = np.zeros(len(y))
    fold_aucs = []
    for train_idx, test_idx in gkf.split(X, y, groups=groups):
        clf = lgb.LGBMClassifier(
            n_estimators=200, max_depth=6, learning_rate=0.05,
            num_leaves=31, verbose=-1, n_jobs=-1, random_state=SEED,
        )
        clf.fit(X[train_idx], y[train_idx])
        proba = clf.predict_proba(X[test_idx])[:, 1]
        oof_proba[test_idx] = proba
        fold_aucs.append(roc_auc_score(y[test_idx], proba))
    return oof_proba, fold_aucs


def bootstrap_ci(y, oof_proba, doc_ids, n_boot, rng):
    unique_docs = np.unique(doc_ids)
    n_docs = len(unique_docs)
    doc_indices = [np.where(doc_ids == d)[0] for d in unique_docs]
    point_auc = roc_auc_score(y, oof_proba)
    boot_aucs = np.empty(n_boot)
    for b in range(n_boot):
        sampled = rng.randint(0, n_docs, size=n_docs)
        indices = np.concatenate([doc_indices[s] for s in sampled])
        try:
            boot_aucs[b] = roc_auc_score(y[indices], oof_proba[indices])
        except ValueError:
            boot_aucs[b] = np.nan
    boot_aucs = boot_aucs[~np.isnan(boot_aucs)]
    ci_lower = float(np.percentile(boot_aucs, 2.5))
    ci_upper = float(np.percentile(boot_aucs, 97.5))
    return point_auc, ci_lower, ci_upper, boot_aucs


def permutation_test(y, oof_proba, doc_ids, n_perm, rng, observed_auc):
    unique_docs, inverse = np.unique(doc_ids, return_inverse=True)
    n_docs = len(unique_docs)
    count_ge = 0
    for _ in range(n_perm):
        doc_labels = rng.randint(0, 2, size=n_docs)
        perm_y = doc_labels[inverse]
        if perm_y.sum() == 0 or perm_y.sum() == len(perm_y):
            continue
        perm_auc = roc_auc_score(perm_y, oof_proba)
        if perm_auc >= observed_auc:
            count_ge += 1
    return (count_ge + 1) / (n_perm + 1)


def run_pairwise_analysis(X, depths, doc_ids):
    rng = np.random.RandomState(SEED)
    pairs_results = {}

    for k in range(1, MAX_DEPTH + 1):
        pair = f"{k-1}v{k}"
        t0 = time.time()
        print(f"\n  --- {pair} ---", flush=True)

        mask = (depths == k - 1) | (depths == k)
        X_pair = X[mask]
        y_pair = (depths[mask] == k).astype(int)
        groups_pair = doc_ids[mask]

        n0 = (y_pair == 0).sum()
        n1 = (y_pair == 1).sum()
        print(f"  Samples: {len(y_pair)} (class 0: {n0}, class 1: {n1})", flush=True)

        oof_proba, fold_aucs = get_oof_predictions(X_pair, y_pair, groups_pair)
        mean_auc = np.mean(fold_aucs)
        print(f"  Fold AUCs: {[round(a, 4) for a in fold_aucs]}", flush=True)
        print(f"  Mean AUC: {mean_auc:.4f}", flush=True)

        point_auc, ci_lower, ci_upper, boot_aucs = bootstrap_ci(
            y_pair, oof_proba, groups_pair, N_BOOT, rng,
        )
        print(f"  Point AUC (OOF): {point_auc:.4f}", flush=True)
        print(f"  95% CI: [{ci_lower:.4f}, {ci_upper:.4f}]", flush=True)

        perm_p = permutation_test(y_pair, oof_proba, groups_pair, N_PERM, rng, point_auc)
        print(f"  Permutation p-value: {perm_p:.6f}", flush=True)
        print(f"  Bonferroni threshold: {BONFERRONI_ALPHA:.4f}", flush=True)

        significant = perm_p < BONFERRONI_ALPHA
        above_theta = ci_lower > THETA
        print(f"  Significant (Bonferroni): {significant}", flush=True)
        print(f"  CI_lower > theta={THETA}: {above_theta}", flush=True)

        elapsed = time.time() - t0
        print(f"  Done in {elapsed:.1f}s", flush=True)

        pairs_results[pair] = {
            "auc": round(point_auc, 4),
            "auc_mean_folds": round(float(mean_auc), 4),
            "fold_aucs": [round(a, 4) for a in fold_aucs],
            "ci_lower": round(ci_lower, 4),
            "ci_upper": round(ci_upper, 4),
            "perm_p": round(perm_p, 6),
            "perm_significant_bonferroni": significant,
            "ci_lower_above_theta": above_theta,
            "boot_mean": round(float(np.mean(boot_aucs)), 4),
            "boot_std": round(float(np.std(boot_aucs)), 4),
        }

    return pairs_results


def compute_kstar(pairs_results):
    kstar = 0
    for k in range(1, MAX_DEPTH + 1):
        pair = f"{k-1}v{k}"
        r = pairs_results[pair]
        if r["ci_lower_above_theta"] and r["perm_significant_bonferroni"]:
            kstar = k
        else:
            break
    return kstar


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--skip_generation", action="store_true",
                        help="Skip scoring, use cached cross-scored features")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    print("=" * 60, flush=True)
    print("  OLMo-1B C4 Cross-Scorer Experiment", flush=True)
    print("  Scorer: Qwen2.5-1.5B-Instruct", flush=True)
    print(f"  Data: {DATA_DIR}", flush=True)
    print(f"  Cached features: {CACHED_FEATURES}", flush=True)
    print(f"  Output: {OUT_DIR}", flush=True)
    print(f"  Bootstrap: {N_BOOT}, Permutation: {N_PERM}", flush=True)
    print(f"  Theta: {THETA}, Bonferroni alpha: {BONFERRONI_ALPHA:.4f}", flush=True)
    print(f"  Skip scoring: {args.skip_generation}", flush=True)
    print("=" * 60, flush=True)

    if args.dry_run:
        print("DRY RUN — exiting.", flush=True)
        return

    t_start = time.time()

    print("\n[Phase 1] Feature preparation", flush=True)
    feat_rows = score_all_depths(skip_scoring=args.skip_generation)
    for r in feat_rows:
        for col in ALL_FEAT_COLS:
            r[col] = float(r[col]) if str(r[col]) not in ("", "nan") else 0.0
    print(f"  Total feature rows: {len(feat_rows)}", flush=True)

    print("\n[Phase 2] Pairwise classification + bootstrap + permutation", flush=True)
    X, depths, doc_ids = rows_to_arrays(feat_rows)
    print(f"  Array shape: {X.shape}, depths: {np.unique(depths)}", flush=True)
    pairs_results = run_pairwise_analysis(X, depths, doc_ids)

    kstar = compute_kstar(pairs_results)
    total_time = time.time() - t_start

    output = {
        "experiment": "olmo_c4_cross_scorer",
        "generator": "OLMo-1B",
        "scorer": "Qwen2.5-1.5B-Instruct" if not args.skip_generation else "Qwen2.5-1.5B-Instruct (cached)",
        "domain": "C4",
        "docs_per_depth": int(np.sum(depths == 0)),
        "max_depth": MAX_DEPTH,
        "n_bootstrap": N_BOOT,
        "n_permutation": N_PERM,
        "theta": THETA,
        "bonferroni_alpha": BONFERRONI_ALPHA,
        "seed": SEED,
        "kstar": kstar,
        "total_seconds": round(total_time, 1),
        "pairs": pairs_results,
        "comparison": {
            "self_scoring_kstar": 1,
            "self_scoring_0v1_auc": 0.9871,
            "self_scoring_1v2_auc": 0.4984,
            "cross_scoring_old_pipeline_kstar": 1,
            "cross_scoring_old_pipeline_0v1_auc": 0.9861,
            "cross_scoring_old_pipeline_1v2_auc": 0.5001,
            "note": "OLMo-1B C4 shows K*=1 under both self- and cross-scoring (old pipeline without bootstrap CI)",
        },
    }
    out_path = OUT_DIR / "results.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    log.info(f"Results saved to {out_path}")

    print("\n" + "=" * 60, flush=True)
    print("=== SUMMARY ===", flush=True)
    print("=" * 60, flush=True)
    print(f"  Generator: OLMo-1B", flush=True)
    print(f"  Scorer: {output['scorer']}", flush=True)
    print(f"  Domain: C4", flush=True)
    print(f"  Docs/depth: {output['docs_per_depth']}", flush=True)
    print(f"  K* (cross-scorer): {kstar}", flush=True)
    print(f"  K* (self-scoring):  1  (0v1=0.9871, 1v2=0.4984)", flush=True)
    print(f"  K* (cross, old):    1  (0v1=0.9861, 1v2=0.5001)", flush=True)
    print(flush=True)
    for pair, r in pairs_results.items():
        sig = "SIG" if r["perm_significant_bonferroni"] else "n.s."
        ci_flag = "PASS" if r["ci_lower_above_theta"] else "FAIL"
        print(
            f"  {pair}: AUC={r['auc']:.4f}  "
            f"95%CI=[{r['ci_lower']:.4f}, {r['ci_upper']:.4f}]  "
            f"p_perm={r['perm_p']:.6f}  [{sig}]  [{ci_flag}]",
            flush=True,
        )
    print(f"\n  Total time: {total_time:.1f}s", flush=True)


if __name__ == "__main__":
    main()
