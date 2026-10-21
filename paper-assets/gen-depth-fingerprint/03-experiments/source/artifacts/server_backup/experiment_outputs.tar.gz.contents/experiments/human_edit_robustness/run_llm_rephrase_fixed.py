"""
LLM Rephrase Evaluation - Fixed version
Fixes: (1) binary = gen1 vs gen2+, (2) 3-class mapping, (3) tail_decay rank 100-1000
"""
import json
import time
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
BATCH_SIZE = 32
FEATURES = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max",
            "tail_decay", "ttr", "hapax_ratio"]
XGB_PARAMS = dict(n_estimators=200, max_depth=6, learning_rate=0.1,
                  random_state=SEED, eval_metric="mlogloss",
                  use_label_encoder=False)
CLASS_MAP_3 = {0: 0, 1: 1, 2: 2, 3: 2, 4: 2}

PYTHIA_MODEL_PATH = "/root/autodl-tmp/models/pythia-410m/models--EleutherAI--pythia-410m/snapshots/9879c9b5f8bea9051dcb0e68dff21493d67e9d4f"
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
    cols = ["model_name", "seed_id", "depth"] + FEATURES
    df = pd.concat([d[cols] for d in dfs], ignore_index=True)
    return df


def extract_features_batch(texts, tokenizer, model, device, batch_size=BATCH_SIZE):
    """Fixed: tail_decay uses rank 100-1000 of avg log-probs (matching main pipeline)."""
    all_features = []
    for start in range(0, len(texts), batch_size):
        batch_texts = texts[start:start + batch_size]
        encodings = tokenizer(
            batch_texts, return_tensors="pt", padding=True,
            truncation=True, max_length=512,
        )
        input_ids = encodings["input_ids"].to(device)
        attention_mask = encodings["attention_mask"].to(device)

        with torch.no_grad():
            logits = model(input_ids=input_ids, attention_mask=attention_mask).logits

        for j in range(len(batch_texts)):
            mask = attention_mask[j].bool()
            seq_len = mask.sum().item()
            if seq_len < 3:
                all_features.append({f: 0.0 for f in FEATURES})
                continue

            token_logits = logits[j, :seq_len - 1, :]
            log_probs = torch.log_softmax(token_logits, dim=-1)
            probs = torch.exp(log_probs)
            entropy = -(probs * log_probs).sum(dim=-1)
            ent_np = entropy.float().cpu().numpy()

            # tail_decay: avg log-probs across positions, sort descending, fit rank 100-1000
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

            # ttr and hapax on words (matching reference)
            words = batch_texts[j].lower().split()
            n_tokens = len(words)
            if n_tokens == 0:
                ttr, hapax_ratio = 0.0, 0.0
            else:
                counter = Counter(words)
                ttr = len(counter) / n_tokens
                hapax_ratio = sum(1 for c in counter.values() if c == 1) / n_tokens

            all_features.append({
                "entropy_mean": float(np.mean(ent_np)),
                "entropy_std": float(np.std(ent_np)),
                "entropy_min": float(np.min(ent_np)),
                "entropy_max": float(np.max(ent_np)),
                "tail_decay": tail_decay,
                "ttr": ttr,
                "hapax_ratio": hapax_ratio,
            })

        done = min(start + batch_size, len(texts))
        if done % (batch_size * 10) == 0 or done == len(texts):
            print(f"    Features extracted: {done}/{len(texts)}", flush=True)

    return all_features


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


def logo_eval(train_df, test_df):
    """
    Fixed LOGO evaluation:
    - Binary: filter depth>=1, then y = (depth >= 2) → gen-1 vs gen-2+
    - Multiclass: 3-class via CLASS_MAP_3
    """
    df_tr = train_df.copy()
    df_te = test_df.copy()
    df_tr["label_3"] = df_tr["depth"].map(CLASS_MAP_3)
    df_te["label_3"] = df_te["depth"].map(CLASS_MAP_3)

    generators = sorted(df_tr["model_name"].unique())
    rng = np.random.RandomState(SEED)

    all_binary_true, all_binary_pred = [], []
    all_multi_true, all_multi_pred = [], []

    for gen in generators:
        tr = df_tr[df_tr["model_name"] != gen].copy()
        te = df_te[df_te["model_name"] == gen].copy()
        if len(te) == 0:
            continue

        # 3-class evaluation
        train_ds = downsample(tr, "label_3", rng)
        clf = XGBClassifier(**XGB_PARAMS)
        clf.fit(train_ds[FEATURES].values, train_ds["label_3"].values)
        preds_3 = clf.predict(te[FEATURES].values)
        all_multi_true.extend(te["label_3"].values.tolist())
        all_multi_pred.extend(preds_3.tolist())

        # Binary: gen-1 vs gen-2+ (filter depth==0)
        test_bin = te[te["depth"] >= 1].copy()
        train_bin = tr[tr["depth"] >= 1].copy()
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
    ci_bin = bootstrap_f1(y_bin_true, y_bin_pred)
    ci_multi = bootstrap_f1(y_multi_true, y_multi_pred)

    return binary_f1, multi_f1, ci_bin, ci_multi


def compute_edit_distance_ratio(original_texts, rephrased_texts):
    ratios = []
    for orig, reph in zip(original_texts, rephrased_texts):
        orig_words = orig.split()
        reph_words = reph.split()
        if not orig_words:
            continue
        max_len = max(len(orig_words), len(reph_words))
        matching = sum(1 for i, w in enumerate(orig_words)
                       if i < len(reph_words) and reph_words[i] == w)
        ratio = 1.0 - (matching / max_len) if max_len > 0 else 0.0
        ratios.append(ratio)
    return float(np.mean(ratios)) if ratios else 0.0


def main():
    import os
    os.environ["CUDA_VISIBLE_DEVICES"] = "0"
    device = "cuda:0"
    t0 = time.time()

    print("[1/5] Loading texts and features...", flush=True)
    df_texts = load_all_texts()
    df_features = load_all_features()
    df = df_texts.merge(df_features, on=["model_name", "seed_id", "depth"], how="inner")
    print(f"  Merged: {len(df)} samples", flush=True)

    print(f"\n[2/5] Subsampling to {SUBSAMPLE_N}...", flush=True)
    rng = np.random.RandomState(SEED)
    generators = sorted(df["model_name"].unique())
    n_per_gen = SUBSAMPLE_N // len(generators)
    parts = []
    for gen in generators:
        sub = df[df["model_name"] == gen]
        n = min(n_per_gen, len(sub))
        parts.append(sub.sample(n=n, random_state=rng, replace=False))
    df_sample = pd.concat(parts, ignore_index=True)
    print(f"  Sampled: {len(df_sample)} ({len(generators)} generators, ~{n_per_gen} each)", flush=True)

    # Load cached rephrased texts
    intermediate_path = OUTPUT_DIR / "rephrased_texts.jsonl"
    print(f"\n[3/5] Loading cached rephrased texts...", flush=True)
    rephrased_texts = []
    n_replaced = []
    with open(intermediate_path) as f:
        for line in f:
            rec = json.loads(line)
            rephrased_texts.append(rec["rephrased"])
            n_replaced.append(rec["n_sentences_replaced"])
    assert len(rephrased_texts) == len(df_sample), \
        f"Cache mismatch: {len(rephrased_texts)} vs {len(df_sample)}"
    print(f"  Loaded {len(rephrased_texts)} rephrased texts", flush=True)

    texts = df_sample["text"].tolist()

    # Extract features with fixed tail_decay
    print(f"\n[4/5] Extracting features (fixed tail_decay)...", flush=True)
    print("  Loading Pythia-410M...", flush=True)
    tokenizer = AutoTokenizer.from_pretrained(PYTHIA_MODEL_PATH, local_files_only=True)
    model = AutoModelForCausalLM.from_pretrained(
        PYTHIA_MODEL_PATH, local_files_only=True, torch_dtype=torch.float16,
    ).to(device).eval()
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    print("  Extracting original text features...", flush=True)
    orig_feat_list = extract_features_batch(texts, tokenizer, model, device)
    print("  Extracting rephrased text features...", flush=True)
    reph_feat_list = extract_features_batch(rephrased_texts, tokenizer, model, device)

    original_df = df_sample[["model_name", "seed_id", "depth"]].copy()
    for feat_name in FEATURES:
        original_df[feat_name] = [f[feat_name] for f in orig_feat_list]

    rephrased_df = df_sample[["model_name", "seed_id", "depth"]].copy()
    for feat_name in FEATURES:
        rephrased_df[feat_name] = [f[feat_name] for f in reph_feat_list]

    del model, tokenizer
    torch.cuda.empty_cache()

    # LOGO evaluation
    print(f"\n[5/5] Running LOGO evaluation...", flush=True)
    print("  Evaluating original...", flush=True)
    orig_bin_f1, orig_multi_f1, orig_bin_ci, orig_multi_ci = logo_eval(original_df, original_df)
    print(f"  Original: binary={orig_bin_f1:.4f} [{orig_bin_ci[0]:.4f}, {orig_bin_ci[1]:.4f}], "
          f"multi={orig_multi_f1:.4f} [{orig_multi_ci[0]:.4f}, {orig_multi_ci[1]:.4f}]", flush=True)

    print("  Evaluating rephrased...", flush=True)
    reph_bin_f1, reph_multi_f1, reph_bin_ci, reph_multi_ci = logo_eval(original_df, rephrased_df)
    print(f"  Rephrased: binary={reph_bin_f1:.4f} [{reph_bin_ci[0]:.4f}, {reph_bin_ci[1]:.4f}], "
          f"multi={reph_multi_f1:.4f} [{reph_multi_ci[0]:.4f}, {reph_multi_ci[1]:.4f}]", flush=True)

    # Save results
    edit_ratio = compute_edit_distance_ratio(texts, rephrased_texts)
    binary_drop = reph_bin_f1 - orig_bin_f1
    multi_drop = reph_multi_f1 - orig_multi_f1

    output = {
        "original": {
            "binary_f1": round(orig_bin_f1, 4),
            "binary_ci": [round(orig_bin_ci[0], 4), round(orig_bin_ci[1], 4)],
            "multiclass_f1": round(orig_multi_f1, 4),
            "multiclass_ci": [round(orig_multi_ci[0], 4), round(orig_multi_ci[1], 4)],
        },
        "rephrased": {
            "binary_f1": round(reph_bin_f1, 4),
            "binary_ci": [round(reph_bin_ci[0], 4), round(reph_bin_ci[1], 4)],
            "multiclass_f1": round(reph_multi_f1, 4),
            "multiclass_ci": [round(reph_multi_ci[0], 4), round(reph_multi_ci[1], 4)],
        },
        "drop": {
            "binary": round(binary_drop, 4),
            "multiclass": round(multi_drop, 4),
        },
        "edit_distance_ratio": round(edit_ratio, 4),
        "n_samples": len(df_sample),
        "method": "7feature LOGO-CV, binary=gen1-vs-gen2+, 3class=gen0/gen1/gen2+",
        "meta": {
            "avg_sentences_replaced": round(float(np.mean(n_replaced)), 2),
            "rephrase_model": "Qwen3-0.6B-Base",
            "reference_model": "Pythia-410M",
            "elapsed_seconds": round(time.time() - t0, 1),
        },
    }

    output_path = OUTPUT_DIR / "llm_rephrase_results.json"
    with open(output_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved to {output_path}", flush=True)
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
