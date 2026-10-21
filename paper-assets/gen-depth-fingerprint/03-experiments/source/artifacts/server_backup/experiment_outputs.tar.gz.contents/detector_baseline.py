"""
detector_baseline.py — plan-015
Test whether existing detector scores provide ordinal depth signal.
Detectors: log-likelihood, FastDetectGPT (perturbation-free), entropy_mean
"""

import json, os, time
import numpy as np
import pandas as pd
import torch
from scipy.stats import spearmanr
from xgboost import XGBClassifier
from sklearn.metrics import f1_score
from sklearn.model_selection import StratifiedKFold

SEED = 42
N_BOOT = 1000
DEVICE = "cuda:0"
MODEL_PATH = "/root/autodl-tmp/models/pythia-410m/models--EleutherAI--pythia-410m/snapshots/9879c9b5f8bea9051dcb0e68dff21493d67e9d4f/"
DATA_DIR = "/root/gen-depth-fingerprint/data"

CLASS_MAP = {0: 0, 1: 1, 2: 2, 3: 2, 4: 2}
CLASS_NAMES = ["gen-0", "gen-1", "gen-2+"]
XGB_PARAMS = dict(n_estimators=200, max_depth=6, learning_rate=0.1,
                  random_state=SEED, eval_metric="mlogloss",
                  use_label_encoder=False)

GENERATION_FILES = {
    "pythia-2.8b": f"{DATA_DIR}/generations.jsonl",
    "pythia-1b": f"{DATA_DIR}/pythia-1b/generations.jsonl",
    "olmo-2-1b": f"{DATA_DIR}/olmo-2-1b/generations.jsonl",
    "qwen3-0.6b": f"{DATA_DIR}/qwen3-0.6b/generations.jsonl",
    "qwen3-1.7b": f"{DATA_DIR}/qwen3-1.7b/generations.jsonl",
}


def load_all_texts():
    rows = []
    for model_name, path in GENERATION_FILES.items():
        with open(path) as f:
            for line in f:
                obj = json.loads(line)
                rows.append({
                    "model_name": model_name,
                    "seed_id": obj["seed_id"],
                    "depth": obj["depth"],
                    "text": obj["text"],
                })
    df = pd.DataFrame(rows)
    df["label"] = df["depth"].map(CLASS_MAP)
    return df


@torch.no_grad()
def compute_scores(df, model, tokenizer, batch_size=16):
    texts = df["text"].tolist()
    log_lls = np.zeros(len(texts), dtype=np.float64)
    fdg_scores = np.zeros(len(texts), dtype=np.float64)

    t0 = time.time()
    for i in range(0, len(texts), batch_size):
        batch = texts[i:i + batch_size]
        enc = tokenizer(batch, return_tensors="pt", padding=True,
                        truncation=True, max_length=512)
        input_ids = enc["input_ids"].to(DEVICE)
        attn_mask = enc["attention_mask"].to(DEVICE)

        logits = model(input_ids=input_ids, attention_mask=attn_mask).logits

        for j in range(len(batch)):
            mask = attn_mask[j].bool()
            ids = input_ids[j][mask]
            lgt = logits[j][mask]

            if len(ids) < 2:
                continue

            shift_logits = lgt[:-1].float()
            shift_labels = ids[1:]

            log_probs = torch.log_softmax(shift_logits, dim=-1)
            probs = torch.softmax(shift_logits, dim=-1)

            obs = log_probs.gather(1, shift_labels.unsqueeze(1)).squeeze(1)
            log_lls[i + j] = obs.mean().item()

            # FastDetectGPT: conditional probability curvature (perturbation-free)
            # mu_t = E_{X~p(·|ctx)}[log p(X|ctx)] = sum_v p(v) log p(v)
            mu = (probs * log_probs).sum(dim=-1)
            # var_t = E[log^2 p] - mu^2
            var = (probs * log_probs ** 2).sum(dim=-1) - mu ** 2
            sigma = torch.sqrt(var.clamp(min=1e-10))
            z = (obs - mu) / sigma
            fdg_scores[i + j] = z.mean().item()

        done = min(i + batch_size, len(texts))
        if done % (batch_size * 50) == 0 or done == len(texts):
            elapsed = time.time() - t0
            rate = done / elapsed if elapsed > 0 else 0
            print(f"  {done}/{len(texts)}  ({elapsed:.0f}s, {rate:.0f} texts/s)")

    df = df.copy()
    df["log_likelihood"] = log_lls
    df["fast_detect_gpt"] = fdg_scores
    return df


# ─── Evaluation helpers ───

def downsample(df, rng):
    min_n = df["label"].value_counts().min()
    parts = [df[df["label"] == lbl].sample(n=min_n, random_state=rng, replace=False)
             for lbl in sorted(df["label"].unique())]
    return pd.concat(parts, ignore_index=True)


def _safe_macro_f1(yt, yp):
    if len(np.unique(yt)) < 3:
        return np.nan
    return f1_score(yt, yp, average="macro")


def bootstrap_f1(yt, yp, n_boot=N_BOOT, seed=SEED):
    rng = np.random.RandomState(seed)
    n = len(yt)
    vals = [v for _ in range(n_boot)
            if not np.isnan(v := _safe_macro_f1(yt[(idx := rng.randint(0, n, n))], yp[idx]))]
    arr = np.array(vals)
    return float(np.mean(arr)), float(np.percentile(arr, 2.5)), float(np.percentile(arr, 97.5))


def bootstrap_corr(x, y, n_boot=N_BOOT, seed=SEED):
    rng = np.random.RandomState(seed)
    n = len(x)
    vals = []
    for _ in range(n_boot):
        idx = rng.randint(0, n, size=n)
        rho, _ = spearmanr(x[idx], y[idx])
        if not np.isnan(rho):
            vals.append(rho)
    arr = np.array(vals)
    return float(np.mean(arr)), float(np.percentile(arr, 2.5)), float(np.percentile(arr, 97.5))


def eval_5fold(df, feature):
    X = df[[feature]].values
    y = df["label"].values
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=SEED)
    yt_all, yp_all = [], []

    for fold, (tr, te) in enumerate(skf.split(X, y)):
        tr_ds = downsample(df.iloc[tr], np.random.RandomState(SEED + fold))
        clf = XGBClassifier(**XGB_PARAMS)
        clf.fit(tr_ds[[feature]].values, tr_ds["label"].values)
        yp_all.append(clf.predict(X[te]))
        yt_all.append(y[te])

    yt = np.concatenate(yt_all)
    yp = np.concatenate(yp_all)
    macro_f1 = f1_score(yt, yp, average="macro")
    per_cls = f1_score(yt, yp, average=None, labels=[0, 1, 2])
    _, f1_lo, f1_hi = bootstrap_f1(yt, yp)

    rho, pval = spearmanr(df[feature].values, df["depth"].values)
    _, rho_lo, rho_hi = bootstrap_corr(df[feature].values, df["depth"].values)

    return {
        "5fold_macro_f1": round(macro_f1, 4),
        "5fold_f1_ci": [round(f1_lo, 4), round(f1_hi, 4)],
        "gen-0_f1": round(float(per_cls[0]), 4),
        "gen-1_f1": round(float(per_cls[1]), 4),
        "gen-2+_f1": round(float(per_cls[2]), 4),
        "spearman_rho": round(float(rho), 4),
        "spearman_p": float(pval),
        "spearman_ci": [round(rho_lo, 4), round(rho_hi, 4)],
    }


def eval_logo(df, feature):
    generators = sorted(df["model_name"].unique())
    yt_all, yp_all = [], []
    per_gen = {}

    for gen in generators:
        te = df[df["model_name"] == gen]
        tr = downsample(df[df["model_name"] != gen], np.random.RandomState(SEED))
        clf = XGBClassifier(**XGB_PARAMS)
        clf.fit(tr[[feature]].values, tr["label"].values)
        yp = clf.predict(te[[feature]].values)
        per_gen[gen] = round(float(f1_score(te["label"].values, yp, average="macro")), 4)
        yt_all.append(te["label"].values)
        yp_all.append(yp)

    yt = np.concatenate(yt_all)
    yp = np.concatenate(yp_all)
    macro_f1 = f1_score(yt, yp, average="macro")
    per_cls = f1_score(yt, yp, average=None, labels=[0, 1, 2])
    _, f1_lo, f1_hi = bootstrap_f1(yt, yp)

    return {
        "logo_macro_f1": round(macro_f1, 4),
        "logo_f1_ci": [round(f1_lo, 4), round(f1_hi, 4)],
        "logo_gen-0_f1": round(float(per_cls[0]), 4),
        "logo_gen-1_f1": round(float(per_cls[1]), 4),
        "logo_gen-2+_f1": round(float(per_cls[2]), 4),
        "per_generator": per_gen,
    }


def main():
    print("=" * 60)
    print("Plan-015: Detector Baseline Evaluation")
    print("=" * 60)

    # --- Load model ---
    from transformers import AutoTokenizer, AutoModelForCausalLM
    print("\nLoading Pythia-410M...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    model = AutoModelForCausalLM.from_pretrained(MODEL_PATH, torch_dtype=torch.float16)
    model.to(DEVICE).eval()
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    print(f"Model on {DEVICE}")

    # --- Load texts ---
    print("\nLoading texts...")
    df = load_all_texts()
    print(f"Total: {len(df)}  Labels: {df['label'].value_counts().sort_index().to_dict()}")

    # --- Compute scores ---
    print("\nComputing log-likelihood & FastDetectGPT scores...")
    df = compute_scores(df, model, tokenizer, batch_size=16)
    del model
    torch.cuda.empty_cache()

    # --- Merge entropy_mean ---
    print("\nMerging entropy_mean from features_all_models.csv...")
    feat_df = pd.read_csv(f"{DATA_DIR}/features_all_models.csv")
    df = df.merge(feat_df[["model_name", "seed_id", "depth", "entropy_mean"]],
                  on=["model_name", "seed_id", "depth"], how="left")

    # Save intermediate scores
    score_cols = ["model_name", "seed_id", "depth", "label",
                  "log_likelihood", "fast_detect_gpt", "entropy_mean"]
    df[score_cols].to_csv(f"{DATA_DIR}/detector_scores.csv", index=False)
    print(f"Saved detector scores → {DATA_DIR}/detector_scores.csv")

    # --- Evaluate ---
    detectors = ["log_likelihood", "fast_detect_gpt", "entropy_mean"]
    results = {}

    print("\n" + "=" * 60)
    print("5-Fold Stratified CV (1:1:1 downsampled)")
    print("=" * 60)
    for det in detectors:
        r = eval_5fold(df, det)
        results[det] = r
        print(f"\n  {det}:")
        print(f"    macro-F1 = {r['5fold_macro_f1']:.4f}  "
              f"[{r['5fold_f1_ci'][0]:.4f}, {r['5fold_f1_ci'][1]:.4f}]")
        print(f"    per-class: g0={r['gen-0_f1']:.4f}  g1={r['gen-1_f1']:.4f}  "
              f"g2+={r['gen-2+_f1']:.4f}")
        print(f"    Spearman ρ = {r['spearman_rho']:.4f}  "
              f"[{r['spearman_ci'][0]:.4f}, {r['spearman_ci'][1]:.4f}]")

    print("\n" + "=" * 60)
    print("LOGO (Leave-One-Generator-Out)")
    print("=" * 60)
    for det in detectors:
        r = eval_logo(df, det)
        results[det].update(r)
        print(f"\n  {det}:")
        print(f"    LOGO macro-F1 = {r['logo_macro_f1']:.4f}  "
              f"[{r['logo_f1_ci'][0]:.4f}, {r['logo_f1_ci'][1]:.4f}]")
        print(f"    per-gen: {r['per_generator']}")

    # Reference
    results["7_feature_model_reference"] = {
        "logo_macro_f1": 0.8037,
        "note": "plan-002-eval LOGO, 7 features, XGBoost"
    }
    results["skipped_detectors"] = {
        "ld_score": "arXiv:2605.01647 -- no public implementation; "
                    "character-distribution method not trivially reproducible",
        "binoculars": "requires two models (observer+performer); "
                      "skipped to conserve GPU memory on shared device"
    }

    # --- Comparison table ---
    print("\n" + "=" * 70)
    print("COMPARISON TABLE")
    print("=" * 70)
    print(f"{'Detector':<20s} {'5fold-F1':>9s} {'LOGO-F1':>9s} "
          f"{'Spearman':>9s} {'rho 95% CI':>20s}")
    print("-" * 70)
    for det in detectors:
        r = results[det]
        print(f"{det:<20s} {r['5fold_macro_f1']:>9.4f} {r['logo_macro_f1']:>9.4f} "
              f"{r['spearman_rho']:>9.4f} "
              f"[{r['spearman_ci'][0]:.4f}, {r['spearman_ci'][1]:.4f}]")
    print(f"{'7-feature (ref)':<20s} {'\u2014':>9s} {'0.8037':>9s} {'\u2014':>9s}")

    # --- Save ---
    out_path = f"{DATA_DIR}/detector_baseline_results.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\nSaved: {out_path}")


if __name__ == "__main__":
    main()
