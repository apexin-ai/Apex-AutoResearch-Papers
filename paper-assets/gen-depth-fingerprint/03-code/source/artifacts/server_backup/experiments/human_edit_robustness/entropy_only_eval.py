"""
Entropy-only Robustness Evaluation

Uses only 5 entropy features (entropy_mean/std/min/max, tail_decay) to
eliminate lexical artifact bias from random word replacement.
"""

import json
import sys
from collections import Counter
from pathlib import Path

import numpy as np
import pandas as pd
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from xgboost import XGBClassifier
from sklearn.metrics import f1_score

SEED = 42
SUBSAMPLE_N = 5000
BATCH_SIZE = 48
PERTURBATION_RATES = [0.0, 0.05, 0.10, 0.20]
ALL_FEATURES = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max",
                "tail_decay", "ttr", "hapax_ratio"]
ENTROPY_FEATURES = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max", "tail_decay"]
XGB_PARAMS = dict(n_estimators=200, max_depth=6, learning_rate=0.1,
                  random_state=SEED, eval_metric="mlogloss",
                  use_label_encoder=False)
CLASS_MAP_3 = {0: 0, 1: 1, 2: 2, 3: 2, 4: 2}
MODEL_SNAPSHOT = "/root/autodl-tmp/models/pythia-410m/models--EleutherAI--pythia-410m/snapshots/9879c9b5f8bea9051dcb0e68dff21493d67e9d4f"
PROJECT_ROOT = Path("/root/gen-depth-fingerprint")
DATA_DIR = PROJECT_ROOT / "data"
OUTPUT_DIR = PROJECT_ROOT / "experiments" / "human_edit_robustness"


def load_all_texts():
    generators = {
        "pythia-2.8b": [DATA_DIR / "generations_shard0.jsonl",
                        DATA_DIR / "generations_shard1.jsonl",
                        DATA_DIR / "generations_shard2.jsonl",
                        DATA_DIR / "generations_shard3.jsonl"],
        "pythia-1b": [DATA_DIR / "pythia-1b" / "generations_shard0.jsonl"],
        "olmo-2-1b": [DATA_DIR / "olmo-2-1b" / "generations_shard0.jsonl"],
        "qwen3-0.6b": [DATA_DIR / "qwen3-0.6b" / "generations_shard0.jsonl"],
        "qwen3-1.7b": [DATA_DIR / "qwen3-1.7b" / "generations_shard0.jsonl"],
        "qwen3-8b": [DATA_DIR / "qwen3-8b" / "generations_shard0.jsonl"],
        "llama-3.2-3b": [DATA_DIR / "llama-3.2-3b" / "generations_shard0.jsonl"],
        "mistral-7b-v0.3": [DATA_DIR / "mistral-7b-v0.3" / "generations_shard0.jsonl"],
    }

    all_records = []
    for model_name, paths in generators.items():
        seen = set()
        for p in paths:
            if not p.exists():
                continue
            with open(p) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    rec = json.loads(line)
                    key = (rec.get("seed_id"), rec.get("depth"))
                    if key in seen:
                        continue
                    seen.add(key)
                    all_records.append({
                        "model_name": model_name,
                        "seed_id": rec["seed_id"],
                        "depth": rec["depth"],
                        "text": rec["text"],
                    })
        print(f"  {model_name}: {len(seen)} texts loaded")

    return pd.DataFrame(all_records)


def load_all_features():
    df_base = pd.read_csv(DATA_DIR / "features_all_models.csv")
    new_gens = [
        ("llama-3.2-3b", DATA_DIR / "llama-3.2-3b" / "features_pythia410m.jsonl"),
        ("mistral-7b-v0.3", DATA_DIR / "mistral-7b-v0.3" / "features_pythia410m.jsonl"),
    ]
    dfs = [df_base]
    for gen_name, path in new_gens:
        records = []
        with open(path) as f:
            for line in f:
                rec = json.loads(line)
                rec["model_name"] = gen_name
                records.append(rec)
        dfs.append(pd.DataFrame(records))

    cols = ["model_name", "seed_id", "depth"] + ALL_FEATURES
    df = pd.concat([d[cols] for d in dfs], ignore_index=True)
    return df


def perturb_text(text, replace_rate, rng):
    words = text.split()
    n_replace = int(len(words) * replace_rate)
    if n_replace == 0 or len(words) == 0:
        return text
    positions = rng.choice(len(words), size=n_replace, replace=False)
    vocab = list(set(words))
    for pos in positions:
        words[pos] = vocab[rng.randint(0, len(vocab))]
    return ' '.join(words)


def extract_features_batch(texts, tokenizer, model, device):
    results = []
    for start in range(0, len(texts), BATCH_SIZE):
        batch_texts = texts[start:start + BATCH_SIZE]
        encodings = tokenizer(
            batch_texts, return_tensors="pt", padding=True,
            truncation=True, max_length=512,
        ).to(device)

        with torch.no_grad():
            logits = model(**encodings).logits

        for i in range(len(batch_texts)):
            mask = encodings["attention_mask"][i].bool()
            seq_len = mask.sum().item()
            if seq_len < 2:
                results.append({f: 0.0 for f in ALL_FEATURES})
                continue

            token_logits = logits[i, :seq_len - 1, :]
            log_probs = torch.log_softmax(token_logits, dim=-1)
            probs = torch.exp(log_probs)
            entropy = -(probs * log_probs).sum(dim=-1)
            entropy_np = entropy.float().cpu().numpy()

            avg_log_probs = log_probs.float().mean(dim=0)
            sorted_lp, _ = torch.sort(avg_log_probs, descending=True)
            sorted_lp_np = sorted_lp.cpu().numpy()
            vocab_size = sorted_lp_np.shape[0]
            hi = min(1000, vocab_size)
            lo = min(100, hi)
            if hi - lo >= 2:
                x = np.arange(lo, hi, dtype=np.float64)
                y = sorted_lp_np[lo:hi].astype(np.float64)
                coeffs = np.polyfit(x, y, 1)
                tail_decay = float(coeffs[0])
            else:
                tail_decay = 0.0

            words = batch_texts[i].lower().split()
            n_tokens = len(words)
            if n_tokens == 0:
                ttr, hapax_ratio = 0.0, 0.0
            else:
                counter = Counter(words)
                ttr = len(counter) / n_tokens
                hapax_ratio = sum(1 for c in counter.values() if c == 1) / n_tokens

            results.append({
                "entropy_mean": float(np.mean(entropy_np)),
                "entropy_std": float(np.std(entropy_np)),
                "entropy_min": float(np.min(entropy_np)),
                "entropy_max": float(np.max(entropy_np)),
                "tail_decay": tail_decay,
                "ttr": ttr,
                "hapax_ratio": hapax_ratio,
            })

        if (start // BATCH_SIZE) % 10 == 0:
            print(f"    Extracted {min(start + BATCH_SIZE, len(texts))}/{len(texts)}")

    return results


def downsample(df, label_col, rng):
    counts = df[label_col].value_counts()
    min_n = counts.min()
    parts = []
    for lbl in sorted(counts.index):
        sub = df[df[label_col] == lbl]
        parts.append(sub.sample(n=min_n, random_state=rng, replace=False))
    return pd.concat(parts, ignore_index=True)


def bootstrap_f1(y_true, y_pred, n_boot=1000, seed=SEED):
    rng = np.random.RandomState(seed)
    n = len(y_true)
    scores = []
    for _ in range(n_boot):
        idx = rng.randint(0, n, size=n)
        yt, yp = y_true[idx], y_pred[idx]
        if len(np.unique(yt)) < 2:
            continue
        scores.append(f1_score(yt, yp, average="macro"))
    arr = np.array(scores)
    return float(np.percentile(arr, 2.5)), float(np.percentile(arr, 97.5))


def logo_eval(df_original, df_perturbed, features):
    """
    LOGO evaluation using specified feature subset.
    Train on original features, test on perturbed features.
    """
    df_orig = df_original.copy()
    df_pert = df_perturbed.copy()
    df_orig["label_3"] = df_orig["depth"].map(CLASS_MAP_3)
    df_pert["label_3"] = df_pert["depth"].map(CLASS_MAP_3)

    generators = sorted(df_orig["model_name"].unique())
    rng = np.random.RandomState(SEED)

    all_binary_true, all_binary_pred = [], []
    all_multi_true, all_multi_pred = [], []

    for gen in generators:
        train_df = df_orig[df_orig["model_name"] != gen].copy()
        test_df = df_pert[df_pert["model_name"] == gen].copy()

        if len(test_df) == 0:
            continue

        # Binary: depth 0 vs 1+
        train_df["label_bin"] = (train_df["depth"] > 0).astype(int)
        test_df["label_bin"] = (test_df["depth"] > 0).astype(int)

        train_bal = downsample(train_df, "label_bin", rng)
        clf_bin = XGBClassifier(**XGB_PARAMS)
        clf_bin.fit(train_bal[features].values, train_bal["label_bin"].values)
        pred_bin = clf_bin.predict(test_df[features].values)
        all_binary_true.extend(test_df["label_bin"].values.tolist())
        all_binary_pred.extend(pred_bin.tolist())

        # Multiclass (3-class)
        train_bal_m = downsample(train_df, "label_3", rng)
        clf_multi = XGBClassifier(**XGB_PARAMS)
        clf_multi.fit(train_bal_m[features].values, train_bal_m["label_3"].values)
        pred_multi = clf_multi.predict(test_df[features].values)
        all_multi_true.extend(test_df["label_3"].values.tolist())
        all_multi_pred.extend(pred_multi.tolist())

    y_bin_true = np.array(all_binary_true)
    y_bin_pred = np.array(all_binary_pred)
    y_multi_true = np.array(all_multi_true)
    y_multi_pred = np.array(all_multi_pred)

    binary_f1 = f1_score(y_bin_true, y_bin_pred, average="macro")
    multi_f1 = f1_score(y_multi_true, y_multi_pred, average="macro")
    binary_ci = bootstrap_f1(y_bin_true, y_bin_pred)
    multi_ci = bootstrap_f1(y_multi_true, y_multi_pred)

    return binary_f1, multi_f1, binary_ci, multi_ci


def main():
    print("=" * 60)
    print("Entropy-Only Robustness Evaluation")
    print(f"Features: {ENTROPY_FEATURES}")
    print("=" * 60)

    # Step 1: Load texts and features
    print("\n[1/5] Loading texts...")
    df_texts = load_all_texts()
    print(f"  Total texts: {len(df_texts)}")

    print("\n[2/5] Loading pre-computed features...")
    df_feat = load_all_features()
    df = df_texts.merge(df_feat, on=["model_name", "seed_id", "depth"], how="inner")
    print(f"  Merged: {len(df)} rows")

    # Step 2: Subsample (same seed = same samples as 7-feature run)
    print(f"\n[3/5] Subsampling to {SUBSAMPLE_N}...")
    rng = np.random.RandomState(SEED)
    generators = sorted(df["model_name"].unique())
    n_per_gen = SUBSAMPLE_N // len(generators)
    parts = []
    for gen in generators:
        sub = df[df["model_name"] == gen]
        n = min(n_per_gen, len(sub))
        parts.append(sub.sample(n=n, random_state=rng, replace=False))
    df_sample = pd.concat(parts, ignore_index=True)
    print(f"  Sampled: {len(df_sample)} ({len(generators)} generators, ~{n_per_gen} each)")

    # Step 3: Load model
    print("\n[4/5] Loading Pythia-410M...")
    device = "cuda:0"
    tokenizer = AutoTokenizer.from_pretrained(MODEL_SNAPSHOT, local_files_only=True)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_SNAPSHOT, local_files_only=True, torch_dtype=torch.float16,
    ).to(device).eval()
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    print("  Model loaded on cuda:0")

    # Step 4: Perturbation experiments
    print("\n[5/5] Running perturbation experiments (entropy-only)...")
    results = {}
    original_features_df = df_sample[["model_name", "seed_id", "depth"] + ALL_FEATURES].copy()

    for rate in PERTURBATION_RATES:
        rate_key = f"{rate:.2f}"
        print(f"\n--- Rate: {rate_key} ---")

        if rate == 0.0:
            perturbed_df = original_features_df.copy()
        else:
            perturb_rng = np.random.RandomState(SEED)
            texts = df_sample["text"].tolist()
            perturbed_texts = [perturb_text(t, rate, perturb_rng) for t in texts]
            print(f"  Perturbed {len(perturbed_texts)} texts at rate {rate}")

            print(f"  Extracting features...")
            feat_list = extract_features_batch(perturbed_texts, tokenizer, model, device)
            perturbed_df = df_sample[["model_name", "seed_id", "depth"]].copy()
            for feat_name in ALL_FEATURES:
                perturbed_df[feat_name] = [f[feat_name] for f in feat_list]

        # LOGO evaluation with entropy features only
        print(f"  Running LOGO evaluation (entropy-only)...")
        binary_f1, multi_f1, binary_ci, multi_ci = logo_eval(
            original_features_df, perturbed_df, ENTROPY_FEATURES
        )
        results[rate_key] = {
            "binary_f1": round(binary_f1, 4),
            "binary_ci": [round(binary_ci[0], 4), round(binary_ci[1], 4)],
            "multiclass_f1": round(multi_f1, 4),
            "multiclass_ci": [round(multi_ci[0], 4), round(multi_ci[1], 4)],
        }
        print(f"  Binary F1: {binary_f1:.4f} [{binary_ci[0]:.4f}, {binary_ci[1]:.4f}]")
        print(f"  Multiclass F1: {multi_f1:.4f} [{multi_ci[0]:.4f}, {multi_ci[1]:.4f}]")

    # Compute degradation
    baseline_bin = results["0.00"]["binary_f1"]
    baseline_multi = results["0.00"]["multiclass_f1"]
    degradation_binary = {}
    for rate in [0.05, 0.10, 0.20]:
        rate_key = f"{rate:.2f}"
        drop = results[rate_key]["binary_f1"] - baseline_bin
        degradation_binary[rate_key] = round(drop, 4)

    # Compare with 7-feature results
    seven_feat_drops = {"0.05": -0.0457, "0.10": -0.0814, "0.20": -0.1041}
    entropy_drops = {k: degradation_binary[k] for k in ["0.05", "0.10", "0.20"]}
    entropy_more_robust = all(
        abs(entropy_drops[k]) <= abs(seven_feat_drops[k]) for k in seven_feat_drops
    )

    # Save results
    output = {
        "results": results,
        "degradation_binary": degradation_binary,
        "comparison_with_7feature": {
            "note": "7-feature binary drops: 5%=-0.046, 10%=-0.081, 20%=-0.104",
            "entropy_only_drops": entropy_drops,
            "entropy_only_more_robust": entropy_more_robust,
        },
        "meta": {
            "features": ENTROPY_FEATURES,
            "n_features": len(ENTROPY_FEATURES),
            "xgb_params": {"n_estimators": 200, "max_depth": 6},
            "class_balanced": True,
            "protocol": "pooled LOGO 8-fold",
            "seed": SEED,
            "n_samples": len(df_sample),
        }
    }

    output_path = OUTPUT_DIR / "entropy_only_degradation.json"
    with open(output_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved to {output_path}")
    print(json.dumps(output, indent=2))

    del model, tokenizer
    torch.cuda.empty_cache()


if __name__ == "__main__":
    main()
