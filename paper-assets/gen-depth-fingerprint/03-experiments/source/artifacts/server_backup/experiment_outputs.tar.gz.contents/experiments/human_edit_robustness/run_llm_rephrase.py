"""
LLM-Simulated Editing (Condition B): Qwen3-0.6B-Base rephrasing

For each text, randomly select 1-3 sentences (not the first), use
Qwen3-0.6B-Base to regenerate them via context continuation.
Then re-extract depth features with Pythia-410M and evaluate with pooled LOGO XGBoost.

Protocol: train on original features, test on rephrased features.
"""

import json
import os
import re
import sys
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

QWEN_MODEL_PATH = "/root/autodl-tmp/models/Qwen/Qwen3-0.6B-Base"
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


def split_sentences(text):
    parts = re.split(r'(?<=[.!?])\s+', text.strip())
    return [p for p in parts if p.strip()]


def rephrase_with_llm(texts, tokenizer, model, device, base_seed=42):
    """
    For each text, randomly pick 1-3 sentences (indices >= 1) and regenerate
    them by providing all preceding text as context.
    """
    rephrased_texts = []
    n_sentences_replaced = []

    for i, text in enumerate(texts):
        rng = np.random.RandomState(base_seed + i)
        sentences = split_sentences(text)

        if len(sentences) < 3:
            rephrased_texts.append(text)
            n_sentences_replaced.append(0)
            continue

        # Only replace sentences at index >= 1 (need preceding context)
        eligible = list(range(1, len(sentences)))
        n_to_replace = rng.randint(1, min(4, len(eligible) + 1))
        indices = sorted(rng.choice(eligible, size=min(n_to_replace, len(eligible)), replace=False))

        new_sentences = list(sentences)
        for idx in indices:
            prefix = ' '.join(sentences[:idx]) + ' '

            inputs = tokenizer(prefix, return_tensors="pt", truncation=True, max_length=384)
            input_ids = inputs["input_ids"].to(device)

            if input_ids.shape[1] == 0:
                continue

            with torch.no_grad():
                outputs = model.generate(
                    input_ids,
                    max_new_tokens=80,
                    temperature=0.7,
                    do_sample=True,
                    top_p=0.9,
                    pad_token_id=tokenizer.eos_token_id,
                )

            generated = tokenizer.decode(outputs[0][input_ids.shape[1]:], skip_special_tokens=True)
            gen_sentences = split_sentences(generated)
            if gen_sentences:
                new_sentences[idx] = gen_sentences[0]

        rephrased_texts.append(' '.join(new_sentences))
        n_sentences_replaced.append(len(indices))

        if (i + 1) % 50 == 0:
            print(f"    Rephrased {i+1}/{len(texts)} texts", flush=True)

    return rephrased_texts, n_sentences_replaced


def extract_features_batch(texts, tokenizer, model, device, batch_size=BATCH_SIZE):
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
            outputs = model(input_ids=input_ids, attention_mask=attention_mask)
            logits = outputs.logits

        for j in range(len(batch_texts)):
            mask = attention_mask[j].bool()
            seq_len = mask.sum().item()
            if seq_len < 3:
                all_features.append({f: 0.0 for f in FEATURES})
                continue

            token_logits = logits[j, :seq_len - 1, :]
            probs = torch.softmax(token_logits, dim=-1)
            log_probs = torch.log(probs + 1e-10)
            entropies = -(probs * log_probs).sum(dim=-1)

            ent_np = entropies.cpu().numpy()
            tokens = input_ids[j, :seq_len].cpu().tolist()

            sorted_probs, _ = probs.sort(dim=-1, descending=True)
            mean_sorted = sorted_probs.mean(dim=0).cpu().numpy()
            top_k = min(50, mean_sorted.shape[0])
            ranks = np.arange(1, top_k + 1)
            log_ranks = np.log(ranks)
            log_probs_tail = np.log(mean_sorted[:top_k] + 1e-10)
            if len(log_ranks) > 1:
                tail_decay = float(np.polyfit(log_ranks, log_probs_tail, 1)[0])
            else:
                tail_decay = 0.0

            unique_tokens = set(tokens)
            ttr = len(unique_tokens) / seq_len if seq_len > 0 else 0
            token_counts = Counter(tokens)
            hapax = sum(1 for c in token_counts.values() if c == 1)
            hapax_ratio = hapax / seq_len if seq_len > 0 else 0

            all_features.append({
                "entropy_mean": float(ent_np.mean()),
                "entropy_std": float(ent_np.std()),
                "entropy_min": float(ent_np.min()),
                "entropy_max": float(ent_np.max()),
                "tail_decay": tail_decay,
                "ttr": ttr,
                "hapax_ratio": hapax_ratio,
            })

        done = min(start + batch_size, len(texts))
        if done % (batch_size * 10) == 0 or done == len(texts):
            print(f"    Features extracted: {done}/{len(texts)}", flush=True)

    return all_features


def logo_eval(train_df, test_df):
    generators = sorted(train_df["model_name"].unique())
    binary_preds_all = []
    binary_true_all = []
    multi_preds_all = []
    multi_true_all = []

    for held_out in generators:
        tr = train_df[train_df["model_name"] != held_out]
        te = test_df[test_df["model_name"] == held_out]

        X_train = tr[FEATURES].values
        y_train_multi = tr["depth"].values
        y_train_bin = (y_train_multi > 0).astype(int)

        X_test = te[FEATURES].values
        y_test_multi = te["depth"].values
        y_test_bin = (y_test_multi > 0).astype(int)

        # Class-balanced binary
        counts = Counter(y_train_bin)
        total = sum(counts.values())
        n_classes = len(counts)
        weights_bin = {c: total / (n_classes * counts[c]) for c in counts}
        sample_weights_bin = np.array([weights_bin[y] for y in y_train_bin])

        clf_bin = XGBClassifier(**XGB_PARAMS)
        clf_bin.fit(X_train, y_train_bin, sample_weight=sample_weights_bin)
        pred_bin = clf_bin.predict(X_test)
        binary_preds_all.extend(pred_bin)
        binary_true_all.extend(y_test_bin)

        # Multiclass
        counts_m = Counter(y_train_multi)
        total_m = sum(counts_m.values())
        n_classes_m = len(counts_m)
        weights_m = {c: total_m / (n_classes_m * counts_m[c]) for c in counts_m}
        sample_weights_m = np.array([weights_m[y] for y in y_train_multi])

        clf_multi = XGBClassifier(**XGB_PARAMS, num_class=len(set(y_train_multi)))
        clf_multi.fit(X_train, y_train_multi, sample_weight=sample_weights_m)
        pred_multi = clf_multi.predict(X_test)
        multi_preds_all.extend(pred_multi)
        multi_true_all.extend(y_test_multi)

    binary_f1 = f1_score(binary_true_all, binary_preds_all, average="macro")
    multi_f1 = f1_score(multi_true_all, multi_preds_all, average="macro")

    # Bootstrap CI
    rng = np.random.RandomState(SEED)
    binary_true_arr = np.array(binary_true_all)
    binary_pred_arr = np.array(binary_preds_all)
    boot_scores = []
    for _ in range(1000):
        idx = rng.choice(len(binary_true_arr), size=len(binary_true_arr), replace=True)
        boot_scores.append(f1_score(binary_true_arr[idx], binary_pred_arr[idx], average="macro"))
    ci = (float(np.percentile(boot_scores, 2.5)), float(np.percentile(boot_scores, 97.5)))

    multi_true_arr = np.array(multi_true_all)
    multi_pred_arr = np.array(multi_preds_all)
    boot_multi = []
    for _ in range(1000):
        idx = rng.choice(len(multi_true_arr), size=len(multi_true_arr), replace=True)
        boot_multi.append(f1_score(multi_true_arr[idx], multi_pred_arr[idx], average="macro"))
    ci_multi = (float(np.percentile(boot_multi, 2.5)), float(np.percentile(boot_multi, 97.5)))

    return binary_f1, multi_f1, ci, ci_multi


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
    os.environ["CUDA_VISIBLE_DEVICES"] = "0"
    device = "cuda:0"
    t0 = time.time()

    print("[1/6] Loading texts and features...", flush=True)
    df_texts = load_all_texts()
    df_features = load_all_features()

    df = df_texts.merge(df_features, on=["model_name", "seed_id", "depth"], how="inner")
    print(f"  Merged: {len(df)} samples", flush=True)

    print(f"\n[2/6] Subsampling to {SUBSAMPLE_N}...", flush=True)
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

    # Check for intermediate results
    intermediate_path = OUTPUT_DIR / "rephrased_texts.jsonl"
    if intermediate_path.exists():
        print(f"\n[3/6] Loading cached rephrased texts from {intermediate_path}...", flush=True)
        rephrased_texts = []
        n_replaced = []
        with open(intermediate_path) as f:
            for line in f:
                rec = json.loads(line)
                rephrased_texts.append(rec["rephrased"])
                n_replaced.append(rec["n_sentences_replaced"])
        if len(rephrased_texts) == len(df_sample):
            print(f"  Loaded {len(rephrased_texts)} cached rephrased texts", flush=True)
        else:
            print(f"  Cache size mismatch ({len(rephrased_texts)} vs {len(df_sample)}), re-running...", flush=True)
            rephrased_texts = None
    else:
        rephrased_texts = None

    texts = df_sample["text"].tolist()

    if rephrased_texts is None:
        print(f"\n[3/6] Loading Qwen3-0.6B-Base for rephrasing...", flush=True)
        qwen_tokenizer = AutoTokenizer.from_pretrained(QWEN_MODEL_PATH, local_files_only=True)
        qwen_model = AutoModelForCausalLM.from_pretrained(
            QWEN_MODEL_PATH, local_files_only=True, dtype=torch.float16
        ).to(device).eval()
        if qwen_tokenizer.pad_token is None:
            qwen_tokenizer.pad_token = qwen_tokenizer.eos_token
        print("  Qwen3-0.6B-Base loaded", flush=True)

        print(f"  Rephrasing {len(texts)} texts...", flush=True)
        rephrased_texts, n_replaced = rephrase_with_llm(texts, qwen_tokenizer, qwen_model, device)
        print(f"  Done. Avg sentences replaced: {np.mean(n_replaced):.2f}", flush=True)

        # Save intermediate
        with open(intermediate_path, "w") as f:
            for i, (orig, reph, n_rep) in enumerate(zip(texts, rephrased_texts, n_replaced)):
                json.dump({"idx": i, "original": orig, "rephrased": reph,
                          "n_sentences_replaced": int(n_rep)}, f)
                f.write("\n")
        print(f"  Saved intermediate to {intermediate_path}", flush=True)

        del qwen_model, qwen_tokenizer
        torch.cuda.empty_cache()

    # Feature extraction with Pythia-410M
    print(f"\n[4/6] Loading Pythia-410M for feature extraction...", flush=True)
    pythia_tokenizer = AutoTokenizer.from_pretrained(PYTHIA_MODEL_PATH, local_files_only=True)
    pythia_model = AutoModelForCausalLM.from_pretrained(
        PYTHIA_MODEL_PATH, local_files_only=True, torch_dtype=torch.float32
    ).to(device).eval()
    if pythia_tokenizer.pad_token is None:
        pythia_tokenizer.pad_token = pythia_tokenizer.eos_token
    print("  Pythia-410M loaded", flush=True)

    print(f"  Extracting features from rephrased texts...", flush=True)
    feat_list = extract_features_batch(rephrased_texts, pythia_tokenizer, pythia_model, device)
    print(f"  Extracted {len(feat_list)} feature vectors", flush=True)

    rephrased_df = df_sample[["model_name", "seed_id", "depth"]].copy()
    for feat_name in FEATURES:
        rephrased_df[feat_name] = [f[feat_name] for f in feat_list]

    original_df = df_sample[["model_name", "seed_id", "depth"] + FEATURES].copy()

    del pythia_model, pythia_tokenizer
    torch.cuda.empty_cache()

    # LOGO evaluation
    print(f"\n[5/6] Running LOGO evaluation...", flush=True)

    print("  Evaluating original (baseline)...", flush=True)
    orig_bin_f1, orig_multi_f1, orig_bin_ci, orig_multi_ci = logo_eval(original_df, original_df)
    print(f"  Original: binary={orig_bin_f1:.4f} [{orig_bin_ci[0]:.4f}, {orig_bin_ci[1]:.4f}], "
          f"multi={orig_multi_f1:.4f} [{orig_multi_ci[0]:.4f}, {orig_multi_ci[1]:.4f}]", flush=True)

    print("  Evaluating LLM rephrased...", flush=True)
    reph_bin_f1, reph_multi_f1, reph_bin_ci, reph_multi_ci = logo_eval(original_df, rephrased_df)
    print(f"  Rephrased: binary={reph_bin_f1:.4f} [{reph_bin_ci[0]:.4f}, {reph_bin_ci[1]:.4f}], "
          f"multi={reph_multi_f1:.4f} [{reph_multi_ci[0]:.4f}, {reph_multi_ci[1]:.4f}]", flush=True)

    # Save results
    print(f"\n[6/6] Saving results...", flush=True)
    edit_ratio = compute_edit_distance_ratio(texts, rephrased_texts)

    binary_drop = reph_bin_f1 - orig_bin_f1
    multi_drop = reph_multi_f1 - orig_multi_f1

    output = {
        "results": {
            "original": {
                "binary_f1": round(orig_bin_f1, 4),
                "binary_ci": [round(orig_bin_ci[0], 4), round(orig_bin_ci[1], 4)],
                "multiclass_f1": round(orig_multi_f1, 4),
                "multiclass_ci": [round(orig_multi_ci[0], 4), round(orig_multi_ci[1], 4)],
            },
            "llm_rephrased": {
                "binary_f1": round(reph_bin_f1, 4),
                "binary_ci": [round(reph_bin_ci[0], 4), round(reph_bin_ci[1], 4)],
                "multiclass_f1": round(reph_multi_f1, 4),
                "multiclass_ci": [round(reph_multi_ci[0], 4), round(reph_multi_ci[1], 4)],
            },
        },
        "degradation": {
            "binary_drop": round(binary_drop, 4),
            "multiclass_drop": round(multi_drop, 4),
            "relative_binary_drop_pct": f"{abs(binary_drop) / orig_bin_f1 * 100:.1f}%",
        },
        "rephrase_stats": {
            "n_samples": len(df_sample),
            "avg_sentences_replaced": round(float(np.mean(n_replaced)), 2),
            "avg_edit_distance_ratio": round(edit_ratio, 4),
            "model": "Qwen3-0.6B-Base",
        },
        "comparison_with_random_replacement": {
            "random_5pct_binary": 0.6496,
            "random_5pct_drop": -0.0457,
            "llm_rephrase_binary": round(reph_bin_f1, 4),
            "llm_rephrase_drop": round(binary_drop, 4),
            "note": ("LLM rephrase degrades less than 5% random replacement"
                     if abs(binary_drop) < 0.0457
                     else "LLM rephrase degrades more than 5% random replacement"),
        },
        "meta": {
            "features": FEATURES,
            "rephrase_model": "Qwen3-0.6B-Base",
            "reference_model": "Pythia-410M",
            "xgb_params": {"n_estimators": 200, "max_depth": 6},
            "class_balanced": True,
            "protocol": "pooled LOGO 8-fold, train=original, test=rephrased",
            "seed": SEED,
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
