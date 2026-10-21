"""
Human Edit Robustness Experiment (plan_010 RC5)

Tests depth fingerprint robustness under random word replacement.
- Perturbation rates: 0%, 5%, 10%, 20%
- LOGO evaluation: train on original features, test on perturbed features
- 7 features: entropy_mean/std/min/max, tail_decay, ttr, hapax_ratio
- Reference model: Pythia-410M
- Classifier: XGBoost (200 trees, max_depth=6)
"""

import json
import os
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
FEATURES = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max",
            "tail_decay", "ttr", "hapax_ratio"]
XGB_PARAMS = dict(n_estimators=200, max_depth=6, learning_rate=0.1,
                  random_state=SEED, eval_metric="mlogloss",
                  use_label_encoder=False)
CLASS_MAP_3 = {0: 0, 1: 1, 2: 2, 3: 2, 4: 2}
MODEL_SNAPSHOT = "/root/autodl-tmp/models/pythia-410m/models--EleutherAI--pythia-410m/snapshots/9879c9b5f8bea9051dcb0e68dff21493d67e9d4f"
PROJECT_ROOT = Path("/root/gen-depth-fingerprint")
DATA_DIR = PROJECT_ROOT / "data"
OUTPUT_DIR = PROJECT_ROOT / "experiments" / "human_edit_robustness"


def load_all_texts():
    """Load texts from all 8 generators, return DataFrame with model_name, seed_id, depth, text."""
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
    """Load features from features_all_models.csv + llama/mistral JSONL."""
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

    cols = ["model_name", "seed_id", "depth"] + FEATURES
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
    """Extract all 7 features for a list of texts."""
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
                results.append({f: 0.0 for f in FEATURES})
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


def logo_eval(df_original, df_perturbed):
    """
    LOGO evaluation: train on original features of 7 generators,
    test on perturbed features of held-out generator.
    Returns binary F1 (gen-1 vs gen-2+) and multiclass F1 (3-class).
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

        # 3-class
        train_ds = downsample(train_df, "label_3", rng)
        clf = XGBClassifier(**XGB_PARAMS)
        clf.fit(train_ds[FEATURES].values, train_ds["label_3"].values)
        preds_3 = clf.predict(test_df[FEATURES].values)
        all_multi_true.extend(test_df["label_3"].values.tolist())
        all_multi_pred.extend(preds_3.tolist())

        # Binary (gen-1 vs gen-2+): only test samples with depth >= 1
        test_bin = test_df[test_df["depth"] >= 1].copy()
        train_bin = train_df[train_df["depth"] >= 1].copy()
        if len(test_bin) == 0 or len(train_bin) == 0:
            continue
        test_bin["label_bin"] = (test_bin["depth"] >= 2).astype(int)
        train_bin["label_bin"] = (train_bin["depth"] >= 2).astype(int)

        train_bin_ds = downsample(train_bin, "label_bin", rng)
        clf_bin = XGBClassifier(**XGB_PARAMS)
        clf_bin.fit(train_bin_ds[FEATURES].values, train_bin_ds["label_bin"].values)
        preds_bin = clf_bin.predict(test_bin[FEATURES].values)
        all_binary_true.extend(test_bin["label_bin"].values.tolist())
        all_binary_pred.extend(preds_bin.tolist())

    y_bin_true = np.array(all_binary_true)
    y_bin_pred = np.array(all_binary_pred)
    y_multi_true = np.array(all_multi_true)
    y_multi_pred = np.array(all_multi_pred)

    binary_f1 = float(f1_score(y_bin_true, y_bin_pred, average="macro"))
    multi_f1 = float(f1_score(y_multi_true, y_multi_pred, average="macro"))
    ci_lo, ci_hi = bootstrap_f1(y_bin_true, y_bin_pred)

    return binary_f1, multi_f1, [ci_lo, ci_hi]


def main():
    print("=" * 60)
    print("Human Edit Robustness Experiment")
    print("=" * 60)

    # Step 1: Load texts and features
    print("\n[1/5] Loading texts...")
    df_texts = load_all_texts()
    print(f"  Total texts: {len(df_texts)}")

    print("\n[2/5] Loading original features...")
    df_features = load_all_features()
    print(f"  Total features: {len(df_features)}")

    # Merge texts with features
    df = df_features.merge(df_texts, on=["model_name", "seed_id", "depth"], how="inner")
    print(f"  Merged (features+text): {len(df)}")

    # Subsample stratified by model
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
    for gen in generators:
        n = len(df_sample[df_sample["model_name"] == gen])
        print(f"    {gen}: {n}")

    # Step 2: Load model for feature extraction
    print("\n[4/5] Loading Pythia-410M...")
    device = "cuda:0"
    tokenizer = AutoTokenizer.from_pretrained(MODEL_SNAPSHOT, local_files_only=True)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_SNAPSHOT, local_files_only=True, torch_dtype=torch.float16,
    ).to(device).eval()
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    print("  Model loaded on cuda:0")

    # Step 3: For each perturbation rate, perturb + extract + evaluate
    print("\n[5/5] Running perturbation experiments...")
    results = {}
    original_features_df = df_sample[["model_name", "seed_id", "depth"] + FEATURES].copy()

    for rate in PERTURBATION_RATES:
        rate_key = f"{rate:.2f}"
        print(f"\n--- Rate: {rate_key} ---")

        if rate == 0.0:
            # Baseline: use original features directly
            perturbed_df = original_features_df.copy()
        else:
            # Perturb texts and re-extract features
            perturb_rng = np.random.RandomState(SEED)
            texts = df_sample["text"].tolist()
            perturbed_texts = [perturb_text(t, rate, perturb_rng) for t in texts]
            print(f"  Perturbed {len(perturbed_texts)} texts at rate {rate}")

            print(f"  Extracting features...")
            feat_list = extract_features_batch(perturbed_texts, tokenizer, model, device)
            perturbed_df = df_sample[["model_name", "seed_id", "depth"]].copy()
            for feat_name in FEATURES:
                perturbed_df[feat_name] = [f[feat_name] for f in feat_list]

        # LOGO evaluation
        print(f"  Running LOGO evaluation...")
        binary_f1, multi_f1, binary_ci = logo_eval(original_features_df, perturbed_df)
        results[rate_key] = {
            "binary_f1": round(binary_f1, 4),
            "multiclass_f1": round(multi_f1, 4),
            "binary_ci": [round(binary_ci[0], 4), round(binary_ci[1], 4)],
        }
        print(f"  Binary F1: {binary_f1:.4f} [{binary_ci[0]:.4f}, {binary_ci[1]:.4f}]")
        print(f"  Multiclass F1: {multi_f1:.4f}")

    # Compute degradation
    baseline_bin = results["0.00"]["binary_f1"]
    degradation = {}
    for rate in [0.05, 0.10, 0.20]:
        rate_key = f"{rate:.2f}"
        drop = results[rate_key]["binary_f1"] - baseline_bin
        degradation[f"{rate_key}_drop_binary"] = round(drop, 4)

    # Save results
    output = {
        "results": results,
        "degradation": degradation,
        "meta": {
            "n_samples": len(df_sample),
            "n_per_generator": {gen: int(len(df_sample[df_sample["model_name"] == gen]))
                                for gen in generators},
            "perturbation_method": "random word replacement from same-text vocabulary",
            "feature_extraction": "Pythia-410M",
            "classifier": "XGBoost 200/6, class-balanced LOGO",
            "seed": SEED,
            "batch_size": BATCH_SIZE,
        }
    }

    output_path = OUTPUT_DIR / "robustness_results.json"
    with open(output_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved to {output_path}")
    print(json.dumps(output, indent=2))

    # Cleanup
    del model, tokenizer
    torch.cuda.empty_cache()


if __name__ == "__main__":
    main()
