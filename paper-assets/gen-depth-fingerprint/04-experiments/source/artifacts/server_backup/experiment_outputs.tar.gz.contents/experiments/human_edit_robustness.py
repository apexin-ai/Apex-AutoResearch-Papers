#!/usr/bin/env python3
"""
plan-010-human-edit: Human Edit Robustness — Depth Signal Survival Test
"""

import argparse
import json
import os
import random
import sys
import time
import warnings
from collections import Counter
from pathlib import Path

import numpy as np
import pandas as pd
import torch
from sklearn.metrics import f1_score
from transformers import AutoModelForCausalLM, AutoTokenizer
from xgboost import XGBClassifier

warnings.filterwarnings("ignore", message=".*right-padding.*")
warnings.filterwarnings("ignore", message=".*torch_dtype.*")

SEED = 42
FEATURES = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max",
            "tail_decay", "ttr", "hapax_ratio"]

ALL_6 = ["pythia-2.8b", "pythia-1b", "olmo-2-1b", "qwen3-0.6b", "qwen3-1.7b", "qwen3-8b"]

JSONL_PATHS = {
    "pythia-2.8b": "data/generations.jsonl",
    "pythia-1b":   "data/pythia-1b/generations.jsonl",
    "olmo-2-1b":   "data/olmo-2-1b/generations.jsonl",
    "qwen3-0.6b":  "data/qwen3-0.6b/generations.jsonl",
    "qwen3-1.7b":  "data/qwen3-1.7b/generations.jsonl",
    "qwen3-8b":    "data/qwen3-8b/generations.jsonl",
}

PYTHIA_410M = "/root/autodl-tmp/models/pythia-410m/models--EleutherAI--pythia-410m/snapshots/9879c9b5f8bea9051dcb0e68dff21493d67e9d4f"
QWEN3_INSTRUCT = "/root/autodl-tmp/models/qwen3-0.6b-instruct/Qwen/Qwen3-0.6B"

XGB_PARAMS = dict(n_estimators=200, max_depth=6, learning_rate=0.1,
                  random_state=SEED, eval_metric="mlogloss", verbosity=0)

CLASS_MAP_3 = {0: 0, 1: 1, 2: 2, 3: 2, 4: 2}


# -- Text editing --

def random_replace(text, rate, vocab_list, rng):
    words = text.split()
    n_replace = int(len(words) * rate)
    if n_replace == 0 or len(words) == 0:
        return text
    indices = rng.sample(range(len(words)), min(n_replace, len(words)))
    for i in indices:
        words[i] = rng.choice(vocab_list)
    return " ".join(words)


def build_vocab(all_texts, min_len=2, max_vocab=50000):
    counter = Counter()
    for t in all_texts:
        for w in t.split():
            if len(w) >= min_len:
                counter[w.lower()] += 1
    return [w for w, _ in counter.most_common(max_vocab)]


def llm_rephrase_batch(texts, tokenizer, model, device, batch_size=16):
    rephrased = []
    rephrase_instruction = "Lightly rephrase the following text, keeping the meaning and most of the structure. Output ONLY the rephrased text, nothing else.\n\n{text}"

    for start in range(0, len(texts), batch_size):
        batch = texts[start:start + batch_size]
        messages_batch = [[{"role": "user", "content": rephrase_instruction.format(text=t[:600])}] for t in batch]
        prompts = [tokenizer.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True, enable_thinking=False) for msgs in messages_batch]

        inputs = tokenizer(prompts, return_tensors="pt", padding=True,
                           truncation=True, max_length=768).to(device)

        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=200,
                do_sample=True,
                temperature=1.0,
                top_p=0.95,
                pad_token_id=tokenizer.eos_token_id,
            )

        for i, out in enumerate(outputs):
            input_len = inputs["input_ids"].shape[1]
            generated = tokenizer.decode(out[input_len:], skip_special_tokens=True).strip()
            if len(generated.split()) < 10:
                rephrased.append(batch[i])
            else:
                rephrased.append(generated)

        done = min(start + batch_size, len(texts))
        if done % 320 == 0 or done == len(texts):
            elapsed = time.time() - llm_rephrase_batch._t0
            rate = done / elapsed if elapsed > 0 else 0
            eta = (len(texts) - done) / rate if rate > 0 else 0
            print(f"  Rephrased {done}/{len(texts)} ({rate:.1f} texts/s, ETA {eta/60:.1f}m)", flush=True)

    return rephrased


# -- Feature extraction --

def compute_reference_features(texts, tokenizer, model, device, batch_size=16):
    results = []
    for start in range(0, len(texts), batch_size):
        batch_texts = texts[start:start + batch_size]
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
                results.append(dict(entropy_mean=0., entropy_std=0.,
                                    entropy_min=0., entropy_max=0., tail_decay=0.))
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

            results.append({
                "entropy_mean": float(np.mean(entropy_np)),
                "entropy_std":  float(np.std(entropy_np)),
                "entropy_min":  float(np.min(entropy_np)),
                "entropy_max":  float(np.max(entropy_np)),
                "tail_decay":   tail_decay,
            })

        done = min(start + batch_size, len(texts))
        if done % 800 == 0 or done == len(texts):
            print(f"    features: {done}/{len(texts)}", flush=True)

    return results


def compute_surface_features(texts):
    results = []
    for text in texts:
        words = text.lower().split()
        n_tokens = len(words)
        if n_tokens == 0:
            results.append({"ttr": 0.0, "hapax_ratio": 0.0})
            continue
        counter = Counter(words)
        results.append({
            "ttr": len(counter) / n_tokens,
            "hapax_ratio": sum(1 for c in counter.values() if c == 1) / n_tokens,
        })
    return results


def extract_all_features(texts, tokenizer, model, device, batch_size=16):
    ref_feats = compute_reference_features(texts, tokenizer, model, device, batch_size)
    surf_feats = compute_surface_features(texts)
    rows = []
    for r, s in zip(ref_feats, surf_feats):
        row = {}
        row.update(r)
        row.update(s)
        rows.append(row)
    return rows


# -- LOGO evaluation --

def downsample(df, label_col, rng):
    counts = df[label_col].value_counts()
    min_n = counts.min()
    parts = []
    for lbl in sorted(counts.index):
        sub = df[df[label_col] == lbl]
        parts.append(sub.sample(n=min_n, random_state=rng, replace=False))
    return pd.concat(parts, ignore_index=True)


def logo_3class(df):
    df = df.copy()
    df["label"] = df["depth"].map(CLASS_MAP_3)
    generators = sorted(df["model_name"].unique())
    rng = np.random.RandomState(SEED)
    all_f1s = []
    for gen in generators:
        test_df = df[df["model_name"] == gen]
        train_df = df[df["model_name"] != gen]
        train_ds = downsample(train_df, "label", rng)
        clf = XGBClassifier(**XGB_PARAMS)
        clf.fit(train_ds[FEATURES].values, train_ds["label"].values)
        y_pred = clf.predict(test_df[FEATURES].values)
        f1 = f1_score(test_df["label"].values, y_pred, average="macro", zero_division=0)
        all_f1s.append(f1)
    return round(float(np.mean(all_f1s)), 4)


def logo_binary(df):
    df = df.copy()
    df["label"] = (df["depth"] >= 2).astype(int)
    df = df[df["depth"] != 0].copy().reset_index(drop=True)
    generators = sorted(df["model_name"].unique())
    rng = np.random.RandomState(SEED)
    all_f1s = []
    for gen in generators:
        test_df = df[df["model_name"] == gen]
        train_df = df[df["model_name"] != gen]
        train_ds = downsample(train_df, "label", rng)
        clf = XGBClassifier(**XGB_PARAMS)
        clf.fit(train_ds[FEATURES].values, train_ds["label"].values)
        y_pred = clf.predict(test_df[FEATURES].values)
        f1 = f1_score(test_df["label"].values, y_pred, average="macro", zero_division=0)
        all_f1s.append(f1)
    return round(float(np.mean(all_f1s)), 4)


def bootstrap_f1(df, eval_fn, n_boot=200):
    rng = np.random.RandomState(SEED)
    seeds = sorted(df["seed_id"].unique())
    scores = []
    for _ in range(n_boot):
        sampled_seeds = rng.choice(seeds, size=len(seeds), replace=True)
        parts = [df[df["seed_id"] == s] for s in sampled_seeds]
        boot_df = pd.concat(parts, ignore_index=True)
        if boot_df["depth"].nunique() < 2:
            continue
        scores.append(eval_fn(boot_df))
    arr = np.array(scores)
    return {"mean": round(float(np.mean(arr)), 4),
            "ci_lo": round(float(np.percentile(arr, 2.5)), 4),
            "ci_hi": round(float(np.percentile(arr, 97.5)), 4)}


# -- Main --

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--device", default="cuda:1")
    parser.add_argument("--batch-size", type=int, default=16)
    parser.add_argument("--rephrase-batch-size", type=int, default=16)
    parser.add_argument("--skip-rephrase", action="store_true")
    args = parser.parse_args()

    root = Path("/root/gen-depth-fingerprint")
    os.makedirs(root / "results", exist_ok=True)

    t0 = time.time()
    random.seed(SEED)
    rng = random.Random(SEED)

    # Phase 1: Load texts
    print("=" * 60)
    print("Phase 1: Loading texts from 6 generators")
    print("=" * 60)

    records = []
    for model_name, rel_path in sorted(JSONL_PATHS.items()):
        path = root / rel_path
        if not path.exists():
            print(f"  SKIP {model_name}: {path}")
            continue
        ct = 0
        with open(path) as f:
            for line in f:
                r = json.loads(line.strip())
                records.append({
                    "model_name": model_name,
                    "seed_id": r["seed_id"],
                    "depth": r["depth"],
                    "text": r["text"],
                })
                ct += 1
        print(f"  {model_name}: {ct} records")

    df_text = pd.DataFrame(records)
    print(f"Total: {len(df_text)} texts, {df_text['model_name'].nunique()} generators")

    all_texts = df_text["text"].tolist()
    vocab = build_vocab(all_texts)
    print(f"Vocab size for replacement: {len(vocab)}")

    # Phase 2: Apply edits
    print("\n" + "=" * 60)
    print("Phase 2: Applying edits")
    print("=" * 60)

    conditions = {"baseline": all_texts}

    for rate_pct in [5, 10, 20]:
        rate = rate_pct / 100.0
        print(f"  Random replace {rate_pct}%...")
        edited = [random_replace(t, rate, vocab, rng) for t in all_texts]
        conditions[f"random_{rate_pct}pct"] = edited
        print(f"    Done ({len(edited)} texts)")

    if not args.skip_rephrase:
        print("  Loading Qwen3-0.6B-Instruct for rephrasing...")
        reph_tokenizer = AutoTokenizer.from_pretrained(QWEN3_INSTRUCT, local_files_only=True,
                                                       padding_side="left")
        reph_model = AutoModelForCausalLM.from_pretrained(
            QWEN3_INSTRUCT, local_files_only=True, torch_dtype=torch.float16,
        ).to(args.device).eval()
        if reph_tokenizer.pad_token is None:
            reph_tokenizer.pad_token = reph_tokenizer.eos_token

        gen0_mask = (df_text["depth"] == 0).tolist()
        texts_to_rephrase = [t for t, is_g0 in zip(all_texts, gen0_mask) if not is_g0]
        print(f"  Rephrasing {len(texts_to_rephrase)} non-gen-0 texts...")

        llm_rephrase_batch._t0 = time.time()
        rephrased_nongen0 = llm_rephrase_batch(
            texts_to_rephrase, reph_tokenizer, reph_model,
            args.device, batch_size=args.rephrase_batch_size,
        )

        rephrased_all = []
        reph_idx = 0
        for is_g0, orig_text in zip(gen0_mask, all_texts):
            if is_g0:
                rephrased_all.append(orig_text)
            else:
                rephrased_all.append(rephrased_nongen0[reph_idx])
                reph_idx += 1
        conditions["llm_rephrase"] = rephrased_all

        del reph_model, reph_tokenizer
        torch.cuda.empty_cache()
        reph_time = time.time() - llm_rephrase_batch._t0
        print(f"  LLM rephrasing done in {reph_time/60:.1f}m")
    else:
        print("  Skipping LLM rephrasing")

    # Phase 3: Extract features
    print("\n" + "=" * 60)
    print("Phase 3: Extracting features (Pythia-410M)")
    print("=" * 60)

    print("Loading Pythia-410M...")
    feat_tokenizer = AutoTokenizer.from_pretrained(PYTHIA_410M, local_files_only=True)
    feat_model = AutoModelForCausalLM.from_pretrained(
        PYTHIA_410M, local_files_only=True, torch_dtype=torch.float16,
    ).to(args.device).eval()
    if feat_tokenizer.pad_token is None:
        feat_tokenizer.pad_token = feat_tokenizer.eos_token

    condition_dfs = {}
    for cond_name, texts in conditions.items():
        print(f"\n--- {cond_name} ---")
        feat_rows = extract_all_features(texts, feat_tokenizer, feat_model,
                                         args.device, args.batch_size)
        df_cond = df_text[["model_name", "seed_id", "depth"]].copy()
        feat_df = pd.DataFrame(feat_rows)
        for col in FEATURES:
            df_cond[col] = feat_df[col].values
        condition_dfs[cond_name] = df_cond
        print(f"  {cond_name}: {len(df_cond)} rows, done")

    del feat_model, feat_tokenizer
    torch.cuda.empty_cache()

    # Phase 4: LOGO evaluation
    print("\n" + "=" * 60)
    print("Phase 4: LOGO evaluation")
    print("=" * 60)

    results = {"experiment": "plan-010-human-edit", "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S")}

    for cond_name, df_cond in condition_dfs.items():
        print(f"\n--- {cond_name} ---")
        logo_f1 = logo_3class(df_cond)
        binary_f1 = logo_binary(df_cond)
        boot_logo = bootstrap_f1(df_cond, logo_3class, n_boot=200)
        boot_binary = bootstrap_f1(df_cond, logo_binary, n_boot=200)
        print(f"  3-class LOGO F1: {logo_f1}  [{boot_logo['ci_lo']}, {boot_logo['ci_hi']}]")
        print(f"  Binary LOGO F1:  {binary_f1}  [{boot_binary['ci_lo']}, {boot_binary['ci_hi']}]")

        results[cond_name] = {
            "logo_f1": logo_f1,
            "logo_f1_ci": [boot_logo["ci_lo"], boot_logo["ci_hi"]],
            "binary_f1": binary_f1,
            "binary_f1_ci": [boot_binary["ci_lo"], boot_binary["ci_hi"]],
        }

    # Phase 5: Compile results
    print("\n" + "=" * 60)
    print("Phase 5: Compiling results")
    print("=" * 60)

    baseline_logo = results["baseline"]["logo_f1"]
    baseline_binary = results["baseline"]["binary_f1"]

    output = {
        "experiment": "plan-010-human-edit",
        "timestamp": results["timestamp"],
        "n_generators": 6,
        "generators": ALL_6,
        "n_texts": len(df_text),
        "baseline_logo_f1": baseline_logo,
        "baseline_binary_f1": baseline_binary,
        "baseline_logo_ci": results["baseline"]["logo_f1_ci"],
        "baseline_binary_ci": results["baseline"]["binary_f1_ci"],
        "random_replace": {},
        "degradation_curve": None,
    }

    for rate_pct in [5, 10, 20]:
        key = f"random_{rate_pct}pct"
        if key in results:
            r = results[key]
            output["random_replace"][f"{rate_pct}pct"] = {
                "logo_f1": r["logo_f1"],
                "logo_f1_ci": r["logo_f1_ci"],
                "binary_f1": r["binary_f1"],
                "binary_f1_ci": r["binary_f1_ci"],
                "delta_logo_f1": round(r["logo_f1"] - baseline_logo, 4),
                "delta_binary_f1": round(r["binary_f1"] - baseline_binary, 4),
            }

    if "llm_rephrase" in results:
        r = results["llm_rephrase"]
        output["llm_rephrase"] = {
            "logo_f1": r["logo_f1"],
            "logo_f1_ci": r["logo_f1_ci"],
            "binary_f1": r["binary_f1"],
            "binary_f1_ci": r["binary_f1_ci"],
            "delta_logo_f1": round(r["logo_f1"] - baseline_logo, 4),
            "delta_binary_f1": round(r["binary_f1"] - baseline_binary, 4),
        }

    rr = output["random_replace"]
    if "20pct" in rr:
        f1_20 = rr["20pct"]["logo_f1"]
        f1_10 = rr.get("10pct", {}).get("logo_f1", 0)
        if f1_20 > 0.70:
            output["degradation_curve"] = "robust"
        elif f1_10 < 0.65:
            output["degradation_curve"] = "fragile"
        else:
            output["degradation_curve"] = "graceful"

    if "llm_rephrase" in output:
        delta = abs(output["llm_rephrase"]["delta_logo_f1"])
        output["llm_rephrase_robust"] = delta < 0.05

    out_path = root / "results" / "human_edit_robustness.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved to {out_path}")

    elapsed = time.time() - t0
    print(f"Total time: {elapsed:.1f}s ({elapsed/60:.1f}m)")

    print("\n" + "=" * 70)
    print(f"{'Condition':<20} {'LOGO F1':>10} {'Binary F1':>10} {'delta LOGO':>10}")
    print("-" * 70)
    print(f"{'baseline':<20} {baseline_logo:>10.4f} {baseline_binary:>10.4f} {'---':>10}")
    for rate_pct in [5, 10, 20]:
        key = f"{rate_pct}pct"
        if key in rr:
            r = rr[key]
            print(f"{'random_' + key:<20} {r['logo_f1']:>10.4f} {r['binary_f1']:>10.4f} {r['delta_logo_f1']:>+10.4f}")
    if "llm_rephrase" in output:
        r = output["llm_rephrase"]
        print(f"{'llm_rephrase':<20} {r['logo_f1']:>10.4f} {r['binary_f1']:>10.4f} {r['delta_logo_f1']:>+10.4f}")
    print("=" * 70)
    print(f"Degradation: {output['degradation_curve']}")
    if "llm_rephrase_robust" in output:
        print(f"LLM rephrase robust: {output['llm_rephrase_robust']}")


if __name__ == "__main__":
    main()
