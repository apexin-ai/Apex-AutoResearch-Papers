"""
fix_tail_decay_and_eval.py — Re-extract features (unfiltered) with correct tail_decay + evaluate.
"""

import json
import time
from collections import Counter
from pathlib import Path

import numpy as np
import pandas as pd
import torch
from sklearn.metrics import f1_score
from transformers import AutoModelForCausalLM, AutoTokenizer
from xgboost import XGBClassifier

ROOT = Path("/root/gen-depth-fingerprint")
DATA = ROOT / "data"
RESULTS = ROOT / "results"
RESULTS.mkdir(exist_ok=True)

MODEL_SNAPSHOT = "/root/autodl-tmp/models/pythia-410m/models--EleutherAI--pythia-410m/snapshots/9879c9b5f8bea9051dcb0e68dff21493d67e9d4f"

FEAT_COLS = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max",
             "tail_decay", "ttr", "hapax_ratio"]
CLASS_MAP = {0: 0, 1: 1, 2: 2, 3: 2, 4: 2}
XGB_PARAMS = dict(n_estimators=200, max_depth=6, learning_rate=0.1,
                  random_state=42, eval_metric="mlogloss",
                  use_label_encoder=False)

ALL_6 = ["pythia-2.8b", "pythia-1b", "olmo-2-1b", "qwen3-0.6b", "qwen3-1.7b", "qwen3-8b"]
ALL_8 = ALL_6 + ["llama-3.2-3b", "mistral-7b-v0.3"]

N_BOOT = 1000
SEED = 42


def compute_surface_features(texts):
    results = []
    for text in texts:
        words = text.lower().split()
        n = len(words)
        if n == 0:
            results.append({"ttr": 0.0, "hapax_ratio": 0.0})
            continue
        counter = Counter(words)
        results.append({
            "ttr": len(counter) / n,
            "hapax_ratio": sum(1 for c in counter.values() if c == 1) / n,
        })
    return results


def extract_all_features(texts, tokenizer, model, device, batch_size=16):
    """Extract entropy + tail_decay (slope formula) for all texts."""
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
                results.append({
                    "entropy_mean": 0.0, "entropy_std": 0.0,
                    "entropy_min": 0.0, "entropy_max": 0.0,
                    "tail_decay": 0.0,
                })
                continue

            token_logits = logits[i, :seq_len - 1, :]
            log_probs = torch.log_softmax(token_logits, dim=-1)
            probs = torch.exp(log_probs)
            entropy = -(probs * log_probs).sum(dim=-1)
            entropy_np = entropy.float().cpu().numpy()

            # tail_decay: slope of sorted avg log-probs (ranks 100-1000)
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
                "entropy_std": float(np.std(entropy_np)),
                "entropy_min": float(np.min(entropy_np)),
                "entropy_max": float(np.max(entropy_np)),
                "tail_decay": tail_decay,
            })

        processed = min(start + batch_size, len(texts))
        if (start // batch_size) % 50 == 0:
            print(f"    [{processed}/{len(texts)}]")

    return results


def step1_extract_features():
    print("=" * 70)
    print("STEP 1: Extract features (unfiltered) with correct tail_decay")
    print("=" * 70)
    t0 = time.time()

    device = "cuda:0"
    print(f"Loading Pythia-410M on {device}...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_SNAPSHOT, local_files_only=True)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_SNAPSHOT, local_files_only=True, torch_dtype=torch.float16
    ).to(device).eval()
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    print("  Model loaded.")

    datasets = [
        ("llama-3.2-3b", DATA / "llama-3.2-3b" / "generations_shard0.jsonl"),
        ("mistral-7b-v0.3", DATA / "mistral-7b-v0.3" / "generations_shard0.jsonl"),
        ("llama-3.2-3b-rp11", DATA / "llama-3.2-3b-rp11" / "generations_shard0.jsonl"),
    ]

    for name, gen_path in datasets:
        print(f"\n  Processing {name} ({gen_path})...")
        records = []
        with open(gen_path) as f:
            for line in f:
                if line.strip():
                    records.append(json.loads(line.strip()))
        texts = [r["text"] for r in records]
        print(f"    {len(texts)} texts loaded")

        # Surface features
        surface = compute_surface_features(texts)

        # Model features (entropy + tail_decay)
        print(f"    Extracting model features...")
        model_feats = extract_all_features(texts, tokenizer, model, device, batch_size=16)

        # Save
        output_path = gen_path.parent / "features_pythia410m.jsonl"
        with open(output_path, "w") as f:
            for i, rec in enumerate(records):
                row = {
                    "seed_id": rec["seed_id"],
                    "depth": rec["depth"],
                    **model_feats[i],
                    **surface[i],
                }
                f.write(json.dumps(row) + "\n")
        print(f"    Saved {len(records)} rows to {output_path}")

    del model, tokenizer
    torch.cuda.empty_cache()
    print(f"\nStep 1 done in {time.time()-t0:.0f}s")


# ============================================================
# STEP 2-4: Evaluation functions
# ============================================================

def load_6gen_data():
    df = pd.read_csv(DATA / "features_all_models.csv")
    df["label"] = df["depth"].map(CLASS_MAP)
    return df


def load_new_gen_features(name, data_dir):
    feat_path = data_dir / "features_pythia410m.jsonl"
    rows = []
    with open(feat_path) as f:
        for line in f:
            row = json.loads(line.strip())
            row["model_name"] = name
            rows.append(row)
    df = pd.DataFrame(rows)
    df["label"] = df["depth"].map(CLASS_MAP)
    return df


def logo_predictions(X, y, groups):
    preds = np.full(len(y), -1, dtype=int)
    for hold in sorted(set(groups)):
        tr = groups != hold
        te = groups == hold
        clf = XGBClassifier(**XGB_PARAMS)
        clf.fit(X[tr], y[tr])
        preds[te] = clf.predict(X[te])
    return preds


def bootstrap_ci(y_true, y_pred, n_boot=N_BOOT, seed=SEED):
    rng = np.random.RandomState(seed)
    n = len(y_true)
    f1s = np.empty(n_boot)
    for b in range(n_boot):
        idx = rng.randint(0, n, size=n)
        f1s[b] = f1_score(y_true[idx], y_pred[idx], average="macro")
    return float(np.mean(f1s)), float(np.percentile(f1s, 2.5)), float(np.percentile(f1s, 97.5))


def run_logo_eval(df, model_list, task="3class"):
    sub = df[df["model_name"].isin(model_list)].copy()
    X = sub[FEAT_COLS].values
    groups = sub["model_name"].values

    if task == "binary":
        mask = sub["label"] >= 1
        sub_bin = sub[mask].copy()
        X = sub_bin[FEAT_COLS].values
        y = (sub_bin["label"] >= 2).astype(int).values
        groups = sub_bin["model_name"].values
    else:
        y = sub["label"].values

    preds = logo_predictions(X, y, groups)
    f1_obs = round(f1_score(y, preds, average="macro"), 4)

    mean, lo, hi = bootstrap_ci(y, preds)
    per_gen = {}
    for g in sorted(set(groups)):
        mask_g = groups == g
        if mask_g.sum() > 0:
            f1_g = round(f1_score(y[mask_g], preds[mask_g], average="macro"), 4)
            gm, gl, gh = bootstrap_ci(y[mask_g], preds[mask_g])
            per_gen[g] = {"f1": f1_g, "ci_lower": round(gl, 4), "ci_upper": round(gh, 4)}

    return {
        "f1_observed": f1_obs,
        "ci_lower": round(lo, 4),
        "ci_upper": round(hi, 4),
        "n_samples": len(y),
        "per_generator": per_gen,
    }


def step2_8gen_logo():
    print("\n" + "=" * 70)
    print("STEP 2: 8-gen LOGO (unfiltered)")
    print("=" * 70)
    t0 = time.time()

    df_6gen = load_6gen_data()
    df_llama = load_new_gen_features("llama-3.2-3b", DATA / "llama-3.2-3b")
    df_mistral = load_new_gen_features("mistral-7b-v0.3", DATA / "mistral-7b-v0.3")
    df_8gen = pd.concat([df_6gen, df_llama, df_mistral], ignore_index=True)
    print(f"  Total: {len(df_8gen)} samples, generators: {sorted(df_8gen['model_name'].unique())}")

    results = {}
    print("\n  3-class LOGO...")
    results["3class"] = run_logo_eval(df_8gen, ALL_8, "3class")
    print(f"    F1 = {results['3class']['f1_observed']}")
    print("  Binary LOGO...")
    results["binary"] = run_logo_eval(df_8gen, ALL_8, "binary")
    print(f"    F1 = {results['binary']['f1_observed']}")

    out_path = RESULTS / "8gen_logo_unfiltered.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"  Saved: {out_path} ({time.time()-t0:.0f}s)")
    return results


def compute_repeated_4gram_ratio(text):
    words = text.split()
    if len(words) < 4:
        return 0.0
    ngrams = [tuple(words[i:i+4]) for i in range(len(words) - 3)]
    counter = Counter(ngrams)
    repeated = sum(count for count in counter.values() if count > 1)
    return repeated / len(ngrams)


def step3_rp_lofo():
    print("\n" + "=" * 70)
    print("STEP 3: rp-LOFO")
    print("=" * 70)
    t0 = time.time()

    df_6gen = load_6gen_data()
    df_mistral = load_new_gen_features("mistral-7b-v0.3", DATA / "mistral-7b-v0.3")
    df_train = pd.concat([df_6gen, df_mistral], ignore_index=True)
    print(f"  Train: {len(df_train)} samples ({sorted(df_train['model_name'].unique())})")

    X_train_3c = df_train[FEAT_COLS].values
    y_train_3c = df_train["label"].values
    clf_3c = XGBClassifier(**XGB_PARAMS)
    clf_3c.fit(X_train_3c, y_train_3c)

    mask_bin_train = df_train["label"] >= 1
    X_train_bin = df_train[mask_bin_train][FEAT_COLS].values
    y_train_bin = (df_train[mask_bin_train]["label"] >= 2).astype(int).values
    clf_bin = XGBClassifier(**XGB_PARAMS)
    clf_bin.fit(X_train_bin, y_train_bin)

    # Test A: Llama rp=1.1
    print("\n  Test A: Llama rp=1.1")
    df_rp11 = load_new_gen_features("llama-3.2-3b-rp11", DATA / "llama-3.2-3b-rp11")
    X_a = df_rp11[FEAT_COLS].values
    y_a_3c = df_rp11["label"].values
    pred_a_3c = clf_3c.predict(X_a)
    f1_a_3c = round(f1_score(y_a_3c, pred_a_3c, average="macro"), 4)

    mask_a_bin = df_rp11["label"] >= 1
    X_a_bin = df_rp11[mask_a_bin][FEAT_COLS].values
    y_a_bin = (df_rp11[mask_a_bin]["label"] >= 2).astype(int).values
    pred_a_bin = clf_bin.predict(X_a_bin)
    f1_a_bin = round(f1_score(y_a_bin, pred_a_bin, average="macro"), 4)

    per_class_a = {}
    for cls in sorted(set(y_a_3c)):
        mask_cls = y_a_3c == cls
        f1_cls = round(f1_score((y_a_3c == cls).astype(int)[mask_cls],
                                (pred_a_3c == cls).astype(int)[mask_cls],
                                average="binary", zero_division=0), 4)
        # Per-class accuracy
        acc_cls = round(float(np.mean(pred_a_3c[mask_cls] == y_a_3c[mask_cls])), 4)
        per_class_a[f"class_{cls}"] = {"accuracy": acc_cls, "n": int(mask_cls.sum())}

    print(f"    3-class F1 = {f1_a_3c}, binary F1 = {f1_a_bin}")
    print(f"    Per-class: {per_class_a}")

    # Test B: Llama rp=1.0 filtered
    print("\n  Test B: Llama rp=1.0 (soft-filtered)")
    df_llama = load_new_gen_features("llama-3.2-3b", DATA / "llama-3.2-3b")
    llama_records = []
    with open(DATA / "llama-3.2-3b" / "generations_shard0.jsonl") as f:
        for line in f:
            if line.strip():
                llama_records.append(json.loads(line.strip()))
    keep_mask = np.array([compute_repeated_4gram_ratio(r["text"]) <= 0.5 for r in llama_records])
    print(f"    Filter: {keep_mask.sum()}/{len(keep_mask)} kept")

    df_llama_f = df_llama[keep_mask].copy()
    X_b = df_llama_f[FEAT_COLS].values
    y_b_3c = df_llama_f["label"].values
    pred_b_3c = clf_3c.predict(X_b)
    f1_b_3c = round(f1_score(y_b_3c, pred_b_3c, average="macro"), 4)

    mask_b_bin = df_llama_f["label"] >= 1
    X_b_bin = df_llama_f[mask_b_bin][FEAT_COLS].values
    y_b_bin = (df_llama_f[mask_b_bin]["label"] >= 2).astype(int).values
    pred_b_bin = clf_bin.predict(X_b_bin)
    f1_b_bin = round(f1_score(y_b_bin, pred_b_bin, average="macro"), 4)

    print(f"    3-class F1 = {f1_b_3c}, binary F1 = {f1_b_bin}")

    results = {
        "test_A_llama_rp11": {
            "3class_f1": f1_a_3c, "binary_f1": f1_a_bin,
            "per_class": per_class_a, "n_samples": len(df_rp11),
        },
        "test_B_llama_rp10_filtered": {
            "3class_f1": f1_b_3c, "binary_f1": f1_b_bin,
            "n_kept": int(keep_mask.sum()), "n_original": len(keep_mask),
        },
        "train_info": {
            "n_samples": len(df_train),
            "generators": sorted(df_train["model_name"].unique().tolist()),
        }
    }

    out_path = RESULTS / "rp_lofo_results.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"  Saved: {out_path} ({time.time()-t0:.0f}s)")
    return results


def step4_filter_diagnostic():
    print("\n" + "=" * 70)
    print("STEP 4: Filtered vs Unfiltered diagnostics")
    print("=" * 70)
    t0 = time.time()

    df_6gen = load_6gen_data()
    df_llama = load_new_gen_features("llama-3.2-3b", DATA / "llama-3.2-3b")
    df_mistral = load_new_gen_features("mistral-7b-v0.3", DATA / "mistral-7b-v0.3")
    df_8gen = pd.concat([df_6gen, df_llama, df_mistral], ignore_index=True)

    results = {}

    # 6-gen unfiltered
    print("\n  6-gen LOGO unfiltered...")
    r = run_logo_eval(df_6gen, ALL_6, "3class")
    results["6gen_unfiltered_3class"] = r["f1_observed"]
    r_bin = run_logo_eval(df_6gen, ALL_6, "binary")
    results["6gen_unfiltered_binary"] = r_bin["f1_observed"]
    print(f"    3-class={r['f1_observed']}, binary={r_bin['f1_observed']}")

    # 6-gen filtered
    print("\n  6-gen LOGO filtered...")
    gen_files_6 = {
        "pythia-2.8b": DATA / "generations.jsonl",
        "pythia-1b": DATA / "pythia-1b" / "generations.jsonl",
        "olmo-2-1b": DATA / "olmo-2-1b" / "generations.jsonl",
        "qwen3-0.6b": DATA / "qwen3-0.6b" / "generations.jsonl",
        "qwen3-1.7b": DATA / "qwen3-1.7b" / "generations.jsonl",
        "qwen3-8b": DATA / "qwen3-8b" / "generations.jsonl",
    }
    keep_indices = []
    offset = 0
    for model_name in ALL_6:
        gen_path = gen_files_6[model_name]
        records = []
        with open(gen_path) as f:
            for line in f:
                if line.strip():
                    records.append(json.loads(line.strip()))
        for i, rec in enumerate(records):
            ratio = compute_repeated_4gram_ratio(rec["text"])
            if ratio <= 0.5:
                keep_indices.append(offset + i)
        offset += len(records)

    df_6gen_filtered = df_6gen.iloc[keep_indices].copy()
    print(f"    Kept {len(df_6gen_filtered)}/{len(df_6gen)}")
    r = run_logo_eval(df_6gen_filtered, ALL_6, "3class")
    results["6gen_filtered_3class"] = r["f1_observed"]
    r_bin = run_logo_eval(df_6gen_filtered, ALL_6, "binary")
    results["6gen_filtered_binary"] = r_bin["f1_observed"]
    print(f"    3-class={r['f1_observed']}, binary={r_bin['f1_observed']}")

    # 8-gen unfiltered
    print("\n  8-gen LOGO unfiltered...")
    r = run_logo_eval(df_8gen, ALL_8, "3class")
    results["8gen_unfiltered_3class"] = r["f1_observed"]
    r_bin = run_logo_eval(df_8gen, ALL_8, "binary")
    results["8gen_unfiltered_binary"] = r_bin["f1_observed"]
    print(f"    3-class={r['f1_observed']}, binary={r_bin['f1_observed']}")

    # 8-gen filtered
    print("\n  8-gen LOGO filtered...")
    llama_recs = []
    with open(DATA / "llama-3.2-3b" / "generations_shard0.jsonl") as f:
        for line in f:
            if line.strip():
                llama_recs.append(json.loads(line.strip()))
    llama_keep = np.array([compute_repeated_4gram_ratio(r["text"]) <= 0.5 for r in llama_recs])

    mistral_recs = []
    with open(DATA / "mistral-7b-v0.3" / "generations_shard0.jsonl") as f:
        for line in f:
            if line.strip():
                mistral_recs.append(json.loads(line.strip()))
    mistral_keep = np.array([compute_repeated_4gram_ratio(r["text"]) <= 0.5 for r in mistral_recs])

    df_llama_f = df_llama[llama_keep].copy()
    df_mistral_f = df_mistral[mistral_keep].copy()
    df_8gen_filtered = pd.concat([df_6gen_filtered, df_llama_f, df_mistral_f], ignore_index=True)
    print(f"    Kept {len(df_8gen_filtered)}/{len(df_8gen)}")

    r = run_logo_eval(df_8gen_filtered, ALL_8, "3class")
    results["8gen_filtered_3class"] = r["f1_observed"]
    r_bin = run_logo_eval(df_8gen_filtered, ALL_8, "binary")
    results["8gen_filtered_binary"] = r_bin["f1_observed"]
    print(f"    3-class={r['f1_observed']}, binary={r_bin['f1_observed']}")

    out_path = RESULTS / "filter_diagnostic.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"  Saved: {out_path} ({time.time()-t0:.0f}s)")
    return results


def main():
    print("=" * 70)
    print("FULL PIPELINE: Fix tail_decay + Evaluate")
    print("=" * 70)
    t_start = time.time()

    step1_extract_features()
    results_8gen = step2_8gen_logo()
    results_rp = step3_rp_lofo()
    results_filter = step4_filter_diagnostic()

    # Summary
    print("\n" + "=" * 70)
    print("=== RESULTS SUMMARY ===")
    print("=" * 70)
    print(f"\n8-gen LOGO (unfiltered): 3-class F1 = {results_8gen['3class']['f1_observed']}, binary F1 = {results_8gen['binary']['f1_observed']}")
    print("  Per-gen (3-class):")
    for g, v in sorted(results_8gen["3class"]["per_generator"].items()):
        print(f"    {g}: F1={v['f1']} [{v['ci_lower']}, {v['ci_upper']}]")

    print(f"\nrp-LOFO Test A (Llama rp=1.1): 3-class F1 = {results_rp['test_A_llama_rp11']['3class_f1']}, binary F1 = {results_rp['test_A_llama_rp11']['binary_f1']}")
    print(f"rp-LOFO Test B (Llama rp=1.0 filtered): 3-class F1 = {results_rp['test_B_llama_rp10_filtered']['3class_f1']}, binary F1 = {results_rp['test_B_llama_rp10_filtered']['binary_f1']}")

    print(f"\nFilter diagnostic:")
    print(f"  6-gen unfiltered: 3-class={results_filter['6gen_unfiltered_3class']}, binary={results_filter['6gen_unfiltered_binary']}")
    print(f"  6-gen filtered:   3-class={results_filter['6gen_filtered_3class']}, binary={results_filter['6gen_filtered_binary']}")
    print(f"  8-gen unfiltered: 3-class={results_filter['8gen_unfiltered_3class']}, binary={results_filter['8gen_unfiltered_binary']}")
    print(f"  8-gen filtered:   3-class={results_filter['8gen_filtered_3class']}, binary={results_filter['8gen_filtered_binary']}")

    print(f"\nTotal time: {time.time()-t_start:.0f}s")


if __name__ == "__main__":
    main()
