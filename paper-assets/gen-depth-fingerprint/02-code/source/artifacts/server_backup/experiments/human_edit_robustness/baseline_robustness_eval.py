"""
Baseline Robustness Evaluation: 4 detectors under random word replacement.

Protocol:
- Same 5000 samples as run_robustness.py (seed=42, 625/gen)
- Perturbation rates: 0%, 5%, 10%, 20%
- LOGO: train on ORIGINAL scores (7 gens), test on PERTURBED scores (held-out gen)
- XGBoost: n_estimators=100, max_depth=3
"""

import json
import sys
import time
from collections import Counter
from pathlib import Path

import numpy as np
import pandas as pd
import torch
import torch.nn.functional as F
from transformers import AutoModelForCausalLM, AutoTokenizer
from scipy.sparse import lil_matrix
from sklearn.metrics import f1_score
from xgboost import XGBClassifier

sys.stdout = open(sys.stdout.fileno(), mode='w', buffering=1)

SEED = 42
SUBSAMPLE_N = 5000
BATCH_SIZE = 32
MAX_LEN = 512
PERTURBATION_RATES = [0.0, 0.05, 0.10, 0.20]
N_BOOT = 1000

XGB_PARAMS = dict(n_estimators=100, max_depth=3, learning_rate=0.1,
                  random_state=SEED, eval_metric="mlogloss", verbosity=0)

CLASS_MAP_3 = {0: 0, 1: 1, 2: 2, 3: 2, 4: 2}

PYTHIA_410M = "/root/autodl-tmp/models/pythia-410m/models--EleutherAI--pythia-410m/snapshots/9879c9b5f8bea9051dcb0e68dff21493d67e9d4f/"
PYTHIA_1B = "/root/autodl-tmp/models/pythia-1b/EleutherAI/pythia-1b/"

PROJECT_ROOT = Path("/root/gen-depth-fingerprint")
DATA_DIR = PROJECT_ROOT / "data"
OUTPUT_DIR = PROJECT_ROOT / "experiments" / "human_edit_robustness"

ALL_8 = ["pythia-2.8b", "pythia-1b", "olmo-2-1b", "qwen3-0.6b", "qwen3-1.7b",
         "qwen3-8b", "llama-3.2-3b", "mistral-7b-v0.3"]


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
        print(f"  {model_name}: {len(seen)} texts")
    return pd.DataFrame(all_records)


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


# ================================================================
# Score computation
# ================================================================

def compute_fdg_logprob(texts, model, tokenizer, device, bs=32):
    fdg, lp = [], []
    for i in range(0, len(texts), bs):
        batch = texts[i:i+bs]
        enc = tokenizer(batch, return_tensors="pt", truncation=True,
                        max_length=MAX_LEN, padding=True).to(device)
        with torch.no_grad():
            logits = model(**enc).logits
        log_p = F.log_softmax(logits[:, :-1], dim=-1)
        tgt = enc["input_ids"][:, 1:]
        mask = enc["attention_mask"][:, 1:].bool()
        actual = log_p.gather(2, tgt.unsqueeze(-1)).squeeze(-1)
        expected = (log_p.exp() * log_p).sum(-1)
        curv = actual - expected
        for j in range(len(batch)):
            m = mask[j]
            if m.sum() < 2:
                fdg.append(0.0); lp.append(0.0); continue
            c = curv[j][m]
            mc, sc = c.mean().item(), c.std().item()
            fdg.append(mc / (sc + 1e-8) if sc > 1e-8 else mc)
            lp.append(actual[j][m].mean().item())
        if (i // bs) % 50 == 0:
            print(f"    FDG+LP: {min(i+bs,len(texts))}/{len(texts)}")
    return fdg, lp


def compute_binoculars(texts, observer, performer, tokenizer, device, bs=8):
    scores = []
    for i in range(0, len(texts), bs):
        batch = texts[i:i+bs]
        enc = tokenizer(batch, return_tensors="pt", truncation=True,
                        max_length=MAX_LEN, padding=True).to(device)
        with torch.no_grad():
            o_logits = observer(**enc).logits[:, :-1].contiguous()
            p_logits = performer(**enc).logits[:, :-1].contiguous()
        ids = enc["input_ids"][:, 1:].contiguous()
        mask = enc["attention_mask"][:, 1:].float()
        o_ce = F.cross_entropy(
            o_logits.view(-1, o_logits.size(-1)), ids.view(-1), reduction="none").view(ids.shape)
        p_ce = F.cross_entropy(
            p_logits.view(-1, p_logits.size(-1)), ids.view(-1), reduction="none").view(ids.shape)
        for j in range(len(batch)):
            m = mask[j]
            if m.sum() < 2:
                scores.append(0.0); continue
            o_val = (o_ce[j] * m).sum() / m.sum()
            p_val = (p_ce[j] * m).sum() / m.sum()
            scores.append((o_val / (p_val + 1e-8)).item())
        if (i // bs) % 50 == 0:
            print(f"    Bino: {min(i+bs,len(texts))}/{len(texts)}")
    return scores


# ================================================================
# Vectorized LD score with shared vocabulary
# ================================================================

def build_vocab_from_texts(texts, n=3):
    """Build trigram vocabulary from a set of texts."""
    vocab = {}
    for t in texts:
        t_lower = t.lower()
        for j in range(len(t_lower) - n + 1):
            ng = t_lower[j:j+n]
            if ng not in vocab:
                vocab[ng] = len(vocab)
    return vocab


def texts_to_sparse(texts, vocab, n=3):
    """Convert texts to sparse trigram probability matrix using given vocab."""
    V = len(vocab)
    mat = lil_matrix((len(texts), V), dtype=np.float64)
    for i, t in enumerate(texts):
        t_lower = t.lower()
        c = Counter(t_lower[j:j+n] for j in range(len(t_lower) - n + 1))
        total = sum(c.values())
        if total > 0:
            for ng, cnt in c.items():
                if ng in vocab:
                    mat[i, vocab[ng]] = cnt / total
    return mat.tocsr()


def compute_ld_vectorized(tri_matrix, ref_mask):
    """Vectorized JSD computation. ref_mask selects reference rows from tri_matrix."""
    ref_rows = tri_matrix[ref_mask]
    if ref_rows.shape[0] == 0:
        return np.zeros(tri_matrix.shape[0])
    ref_dist = np.asarray(ref_rows.mean(axis=0)).flatten()
    ref_sum = ref_dist.sum()
    if ref_sum > 0:
        ref_dist = ref_dist / ref_sum
    h_q = -np.sum(ref_dist[ref_dist > 0] * np.log(ref_dist[ref_dist > 0]))
    n = tri_matrix.shape[0]
    scores = np.zeros(n)
    for start in range(0, n, 4000):
        end = min(start + 4000, n)
        batch = tri_matrix[start:end].toarray()
        row_sums = batch.sum(axis=1, keepdims=True)
        row_sums[row_sums == 0] = 1
        batch = batch / row_sums
        safe_batch = np.where(batch > 0, batch, 1.0)
        h_p = -np.sum(batch * np.log(safe_batch), axis=1)
        m_arr = (batch + ref_dist[np.newaxis, :]) / 2.0
        safe_m = np.where(m_arr > 0, m_arr, 1.0)
        h_m = -np.sum(m_arr * np.log(safe_m), axis=1)
        jsd_sq = h_m - (h_p + h_q) / 2.0
        jsd_sq = np.clip(jsd_sq, 0, None)
        scores[start:end] = np.sqrt(jsd_sq)
    return scores


def compute_ld_cross(tri_test, ref_dist, h_q):
    """Compute JSD of test texts against a precomputed reference distribution."""
    n = tri_test.shape[0]
    scores = np.zeros(n)
    for start in range(0, n, 4000):
        end = min(start + 4000, n)
        batch = tri_test[start:end].toarray()
        row_sums = batch.sum(axis=1, keepdims=True)
        row_sums[row_sums == 0] = 1
        batch = batch / row_sums
        safe_batch = np.where(batch > 0, batch, 1.0)
        h_p = -np.sum(batch * np.log(safe_batch), axis=1)
        m_arr = (batch + ref_dist[np.newaxis, :]) / 2.0
        safe_m = np.where(m_arr > 0, m_arr, 1.0)
        h_m = -np.sum(m_arr * np.log(safe_m), axis=1)
        jsd_sq = h_m - (h_p + h_q) / 2.0
        jsd_sq = np.clip(jsd_sq, 0, None)
        scores[start:end] = np.sqrt(jsd_sq)
    return scores


# ================================================================
# LOGO Evaluation
# ================================================================

def downsample(df, label_col, rng):
    counts = df[label_col].value_counts()
    min_n = counts.min()
    parts = [df[df[label_col] == lbl].sample(n=min_n, random_state=rng, replace=False)
             for lbl in sorted(counts.index)]
    return pd.concat(parts, ignore_index=True)


def bootstrap_ci(y_true, y_pred, n_boot=N_BOOT, seed=SEED):
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
    return [round(float(np.percentile(arr, 2.5)), 4),
            round(float(np.percentile(arr, 97.5)), 4)]


def logo_eval_baseline(df_orig, df_pert, baseline,
                        tri_orig=None, tri_pert=None, binary=False):
    """
    LOGO for single baseline: train on original, test on perturbed.
    For ld_score: uses prebuilt sparse matrices in shared vocab.
    Reference distribution comes from ORIGINAL training class-0 texts.
    """
    rng = np.random.RandomState(SEED)
    generators = sorted(df_orig["model_name"].unique())

    if binary:
        mask_bin = df_orig["depth"] >= 1
        df_o = df_orig[mask_bin].reset_index(drop=True)
        df_p = df_pert[mask_bin].reset_index(drop=True)
        df_o["label"] = (df_o["depth"] >= 2).astype(int)
        df_p["label"] = (df_p["depth"] >= 2).astype(int)
        if tri_orig is not None:
            tri_o = tri_orig[mask_bin.values]
            tri_p = tri_pert[mask_bin.values]
        else:
            tri_o, tri_p = None, None
    else:
        df_o = df_orig.copy().reset_index(drop=True)
        df_p = df_pert.copy().reset_index(drop=True)
        df_o["label"] = df_o["depth"].map(CLASS_MAP_3)
        df_p["label"] = df_p["depth"].map(CLASS_MAP_3)
        tri_o, tri_p = tri_orig, tri_pert

    all_true, all_pred = [], []

    for gen in generators:
        tr_mask = (df_o["model_name"] != gen).values
        te_mask = (df_p["model_name"] == gen).values
        if te_mask.sum() == 0:
            continue

        if baseline == "ld_score" and tri_o is not None:
            # Reference: training class-0 from ORIGINAL texts
            ref_mask = tr_mask & (df_o["label"].values == 0)
            ref_rows = tri_o[ref_mask]
            ref_dist = np.asarray(ref_rows.mean(axis=0)).flatten()
            ref_sum = ref_dist.sum()
            if ref_sum > 0:
                ref_dist = ref_dist / ref_sum
            h_q = -np.sum(ref_dist[ref_dist > 0] * np.log(ref_dist[ref_dist > 0]))

            # LD for original training texts
            ld_orig_all = compute_ld_cross(tri_o, ref_dist, h_q)
            df_o["ld_score"] = ld_orig_all
            # LD for perturbed test texts (against SAME original reference)
            ld_pert_all = compute_ld_cross(tri_p, ref_dist, h_q)
            df_p["ld_score"] = ld_pert_all

        train_df = df_o[tr_mask].copy()
        test_df = df_p[te_mask].copy()

        train_ds = downsample(train_df, "label", rng)
        clf = XGBClassifier(**XGB_PARAMS)
        clf.fit(train_ds[[baseline]].values, train_ds["label"].values)
        preds = clf.predict(test_df[[baseline]].values)
        all_true.extend(test_df["label"].values.tolist())
        all_pred.extend(preds.tolist())

    y_true = np.array(all_true)
    y_pred = np.array(all_pred)
    f1 = round(float(f1_score(y_true, y_pred, average="macro")), 4)
    ci = bootstrap_ci(y_true, y_pred)
    return f1, ci


def main():
    t0 = time.time()
    print("=" * 60)
    print("Baseline Robustness Evaluation")
    print("=" * 60)

    # Step 1: Load texts
    print("\n[1] Loading texts...")
    df_texts = load_all_texts()
    print(f"  Total: {len(df_texts)}")

    # Step 2: Subsample
    print(f"\n[2] Subsampling to {SUBSAMPLE_N}...")
    rng = np.random.RandomState(SEED)
    generators = sorted(df_texts["model_name"].unique())
    n_per_gen = SUBSAMPLE_N // len(generators)
    parts = []
    for gen in generators:
        sub = df_texts[df_texts["model_name"] == gen]
        n = min(n_per_gen, len(sub))
        parts.append(sub.sample(n=n, random_state=rng, replace=False))
    df_sample = pd.concat(parts, ignore_index=True)
    print(f"  Sampled: {len(df_sample)}")

    # Step 3: Load models on cuda:1
    print("\n[3] Loading models...")
    device = "cuda:1"
    tokenizer = AutoTokenizer.from_pretrained(PYTHIA_410M, local_files_only=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    model_410m = AutoModelForCausalLM.from_pretrained(
        PYTHIA_410M, local_files_only=True, torch_dtype=torch.float16
    ).to(device).eval()
    print(f"  Pythia-410M on {device}")
    model_1b = AutoModelForCausalLM.from_pretrained(
        PYTHIA_1B, local_files_only=True, torch_dtype=torch.float16
    ).to(device).eval()
    print(f"  Pythia-1B on {device}")

    # Step 4: Build shared trigram vocabulary from original texts
    texts_orig = df_sample["text"].tolist()
    print("\n[4] Building trigram vocabulary...")
    vocab = build_vocab_from_texts(texts_orig)
    print(f"  Vocab size: {len(vocab)}")
    tri_orig = texts_to_sparse(texts_orig, vocab)
    print(f"  Original trigram matrix: {tri_orig.shape}")

    # Step 5: Compute original model-based scores
    print("\n[5] Computing original model scores...")
    print("  FDG + avg_logprob...")
    fdg_orig, lp_orig = compute_fdg_logprob(texts_orig, model_410m, tokenizer, device)
    print("  Binoculars...")
    bino_orig = compute_binoculars(texts_orig, model_410m, model_1b, tokenizer, device)
    print(f"  Done. {time.time()-t0:.0f}s")

    df_orig_scores = df_sample[["model_name", "seed_id", "depth"]].copy()
    df_orig_scores["fastdetectgpt"] = fdg_orig
    df_orig_scores["avg_logprob"] = lp_orig
    df_orig_scores["binoculars"] = bino_orig

    # Step 6: Run perturbation experiments
    print("\n[6] Perturbation experiments...")
    all_results = {}

    for rate in PERTURBATION_RATES:
        rate_key = f"{rate:.2f}"
        print(f"\n{'='*50}")
        print(f"  RATE: {rate_key}")
        print(f"{'='*50}")

        if rate == 0.0:
            df_pert_scores = df_orig_scores.copy()
            tri_pert = tri_orig
        else:
            perturb_rng = np.random.RandomState(SEED)
            texts_pert = [perturb_text(t, rate, perturb_rng) for t in texts_orig]
            print(f"  Perturbed {len(texts_pert)} texts")

            print("  FDG + avg_logprob...")
            fdg_pert, lp_pert = compute_fdg_logprob(texts_pert, model_410m, tokenizer, device)
            print("  Binoculars...")
            bino_pert = compute_binoculars(texts_pert, model_410m, model_1b, tokenizer, device)
            print("  Trigram matrix...")
            tri_pert = texts_to_sparse(texts_pert, vocab)

            df_pert_scores = df_sample[["model_name", "seed_id", "depth"]].copy()
            df_pert_scores["fastdetectgpt"] = fdg_pert
            df_pert_scores["avg_logprob"] = lp_pert
            df_pert_scores["binoculars"] = bino_pert

        # LOGO eval for each baseline
        rate_results = {}
        for baseline in ["fastdetectgpt", "avg_logprob", "binoculars", "ld_score"]:
            print(f"  LOGO: {baseline}...")
            tri_o = tri_orig if baseline == "ld_score" else None
            tri_p = tri_pert if baseline == "ld_score" else None

            bin_f1, bin_ci = logo_eval_baseline(
                df_orig_scores, df_pert_scores, baseline, tri_o, tri_p, binary=True)
            multi_f1, _ = logo_eval_baseline(
                df_orig_scores, df_pert_scores, baseline, tri_o, tri_p, binary=False)

            rate_results[baseline] = {
                "binary_f1": bin_f1,
                "multiclass_f1": multi_f1,
                "binary_ci": bin_ci,
            }
            print(f"    {baseline}: bin={bin_f1:.4f} {bin_ci}, multi={multi_f1:.4f}")

        all_results[rate_key] = rate_results
        print(f"  Rate {rate_key} done. {time.time()-t0:.0f}s")

    # Cleanup
    del model_410m, model_1b
    torch.cuda.empty_cache()

    # Organize output
    print("\n[7] Saving...")
    output = {}
    for baseline in ["fastdetectgpt", "binoculars", "ld_score", "avg_logprob"]:
        output[baseline] = {}
        for rate_key in ["0.00", "0.05", "0.10", "0.20"]:
            output[baseline][rate_key] = all_results[rate_key][baseline]

    ref = json.load(open(OUTPUT_DIR / "robustness_results.json"))
    seven_feat = {k: v["binary_f1"] for k, v in ref["results"].items()}

    degradations = {}
    for baseline in ["fastdetectgpt", "binoculars", "ld_score", "avg_logprob"]:
        base_val = output[baseline]["0.00"]["binary_f1"]
        degradations[baseline] = round(base_val - output[baseline]["0.20"]["binary_f1"], 4)
    degradations["7feature"] = round(seven_feat["0.00"] - seven_feat["0.20"], 4)

    output["comparison_with_7feature"] = {
        "7feature": seven_feat,
        "most_robust": min(degradations, key=degradations.get),
        "least_robust": max(degradations, key=degradations.get),
        "degradation_at_20pct": degradations,
    }

    output["meta"] = {
        "n_samples": len(df_sample),
        "perturbation_rates": PERTURBATION_RATES,
        "xgb_params": {"n_estimators": 100, "max_depth": 3},
        "protocol": "pooled LOGO 8-fold, class-balanced, seed=42",
        "perturbation_method": "random word replacement from same-text vocabulary",
        "models": {"observer": "Pythia-410M", "performer": "Pythia-1B"},
        "total_time_seconds": round(time.time() - t0, 1),
    }

    out_path = OUTPUT_DIR / "baseline_robustness.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved: {out_path}")
    print(json.dumps(output, indent=2))
    print(f"\nTotal: {time.time()-t0:.0f}s")


if __name__ == "__main__":
    main()
