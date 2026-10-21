#!/usr/bin/env python3
"""4-baseline ensemble + unified hyperparams LOGO comparison for reviewer response.

Groups:
  (a) 4-baseline:         [avg_logprob, ld_score, fastdetectgpt, binoculars]
  (b) 4-baseline+surface: above + ttr, hapax_ratio
  (c) 7-feature unified:  7 depth features, unified XGB params (n_est=200,md=6)
  (d) 7-feature original: 7 depth features, original XGB params (n_est=200,md=6, sanity ≈0.789)

All groups use identical LOGO folds with downsample.
LD score recomputed per fold (train depth-0 reference only) to avoid leakage.
"""

import argparse, json, time
import numpy as np
import pandas as pd
from collections import Counter
from pathlib import Path
from scipy.spatial.distance import jensenshannon
from sklearn.metrics import f1_score
from xgboost import XGBClassifier

ROOT = Path("/root/gen-depth-fingerprint")
DATA = ROOT / "data"
RESULTS = ROOT / "results"
RESULTS.mkdir(exist_ok=True)

DEVICE = "cuda:0"
MAX_LEN = 512
HF_CACHE = "/root/autodl-tmp/.hf_cache"
N_BOOT = 1000
LOGO_SEED = 789
BOOT_SEED = 42

JSONL_PATHS = {
    "olmo-2-1b":   DATA / "olmo-2-1b" / "generations.jsonl",
    "pythia-1b":   DATA / "pythia-1b" / "generations.jsonl",
    "pythia-2.8b": DATA / "generations.jsonl",
    "qwen3-0.6b":  DATA / "qwen3-0.6b" / "generations.jsonl",
    "qwen3-1.7b":  DATA / "qwen3-1.7b" / "generations.jsonl",
    "qwen3-8b":    DATA / "qwen3-8b" / "generations.jsonl",
}

FEAT_7 = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max",
           "tail_decay", "ttr", "hapax_ratio"]
CLASS_MAP = {0: 0, 1: 1, 2: 2, 3: 2, 4: 2}

# Unified hyperparams — matches Table 1 / bootstrap_ci_v2
UNIFIED_XGB = dict(n_estimators=200, max_depth=6, learning_rate=0.1,
                   random_state=789, eval_metric="mlogloss", verbosity=0)
# Original = same as unified (bootstrap_ci_v2 produced the 0.789 reference)
ORIGINAL_XGB = dict(n_estimators=200, max_depth=6, learning_rate=0.1,
                    random_state=789, eval_metric="mlogloss", verbosity=0)

SCORES_CSV = DATA / "detector_scores_all.csv"


# ================================================================
# Detector score computation
# ================================================================

def compute_fdg_logprob(texts, model, tokenizer, device, bs=16):
    import torch
    import torch.nn.functional as F
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
        if (i // bs) % 400 == 0:
            print(f"  FDG+LP: {min(i+bs,len(texts))}/{len(texts)}", flush=True)
    return fdg, lp


def compute_binoculars(texts, observer, performer, tokenizer, device, bs=16):
    import torch
    import torch.nn.functional as F
    scores = []
    for i in range(0, len(texts), bs):
        batch = texts[i:i+bs]
        enc = tokenizer(batch, return_tensors="pt", truncation=True,
                        max_length=MAX_LEN, padding=True).to(device)
        with torch.no_grad():
            o = observer(**enc).logits[:, :-1].contiguous()
            p = performer(**enc).logits[:, :-1].contiguous()
        ids = enc["input_ids"][:, 1:].contiguous()
        mask = enc["attention_mask"][:, 1:].float()
        B, T, V = o.shape
        ppl = (F.cross_entropy(o.view(-1, V), ids.view(-1), reduction="none")
               .view(B, T) * mask).sum(1) / mask.sum(1).clamp(min=1)
        ce = (F.cross_entropy(p.view(-1, V), ids.view(-1), reduction="none")
              .view(B, T) * mask).sum(1) / mask.sum(1).clamp(min=1)
        scores.extend((ppl / ce.clamp(min=1e-8)).cpu().float().tolist())
        if (i // bs) % 400 == 0:
            print(f"  Bino: {min(i+bs,len(texts))}/{len(texts)}", flush=True)
    return scores


# ================================================================
# LD Score (trigram JSD, per-fold reference)
# ================================================================

def build_trigram_counts(texts, n=3):
    cl, vocab = [], set()
    for t in texts:
        c = Counter(t.lower()[j:j+n] for j in range(len(t) - n + 1))
        cl.append(c)
        vocab.update(c)
    vocab = sorted(vocab)
    return cl, {ng: i for i, ng in enumerate(vocab)}, len(vocab)


def ld_scores_from_ref(cl, ref_idx, ng2i, V):
    ref = Counter()
    for i in ref_idx:
        ref.update(cl[i])
    s = sum(ref.values())
    if s == 0:
        return np.zeros(len(cl))
    rv = np.zeros(V)
    for ng, c in ref.items():
        if ng in ng2i:
            rv[ng2i[ng]] = c / s
    out = np.empty(len(cl))
    for i, c in enumerate(cl):
        t = sum(c.values())
        if t == 0:
            out[i] = 0.0
            continue
        v = np.zeros(V)
        for ng, cnt in c.items():
            if ng in ng2i:
                v[ng2i[ng]] = cnt / t
        js = jensenshannon(rv, v)
        out[i] = float(js) if not np.isnan(js) else 0.0
    return out


# ================================================================
# LOGO evaluation
# ================================================================

def downsample(df, rng):
    vc = df["label"].value_counts()
    mn = vc.min()
    return pd.concat(
        [df[df["label"] == l].sample(n=mn, random_state=rng, replace=False)
         for l in sorted(vc.index)], ignore_index=True)


def logo_simple(df, feat_cols, params, gens):
    """Standard LOGO for pre-computed features."""
    rng = np.random.RandomState(LOGO_SEED)
    preds = np.full(len(df), -1, dtype=int)
    pg = {}
    for g in sorted(gens):
        tr = downsample(df[df["model_name"] != g].copy(), rng)
        tm = df["model_name"] == g
        clf = XGBClassifier(**params)
        clf.fit(tr[feat_cols].values, tr["label"].values)
        p = clf.predict(df.loc[tm, feat_cols].values)
        preds[tm.values] = p
        pg[g] = round(f1_score(df.loc[tm, "label"], p, average="macro"), 4)
    return round(np.mean(list(pg.values())), 4), pg, df["label"].values.copy(), preds


def logo_with_ld(df, feat_cols, params, gens, tri):
    """LOGO where ld_score is recomputed per fold from training depth-0 only."""
    cl, ng2i, V = tri
    rng = np.random.RandomState(LOGO_SEED)
    preds = np.full(len(df), -1, dtype=int)
    pg = {}
    cols = [("_ld_fold" if c == "ld_score" else c) for c in feat_cols]
    for g in sorted(gens):
        tr_mask = df["model_name"] != g
        tm = df["model_name"] == g
        ref = df.index[tr_mask & (df["label"] == 0)].tolist()
        df["_ld_fold"] = ld_scores_from_ref(cl, ref, ng2i, V)
        tr = downsample(df[tr_mask].copy(), rng)
        clf = XGBClassifier(**params)
        clf.fit(tr[cols].values, tr["label"].values)
        p = clf.predict(df.loc[tm, cols].values)
        preds[tm.values] = p
        pg[g] = round(f1_score(df.loc[tm, "label"], p, average="macro"), 4)
        print(f"    LOGO hold={g}: F1={pg[g]}", flush=True)
    return round(np.mean(list(pg.values())), 4), pg, df["label"].values.copy(), preds


# ================================================================
# Bootstrap CI
# ================================================================

def boot_ci(y, p, groups, gens, n=N_BOOT, seed=BOOT_SEED):
    rng = np.random.RandomState(seed)
    pg = {}
    for g in sorted(gens):
        m = groups == g
        yt, yp = y[m], p[m]
        nn = len(yt)
        boots = np.empty(n)
        for b in range(n):
            idx = rng.randint(0, nn, nn)
            boots[b] = f1_score(yt[idx], yp[idx], average="macro")
        pg[g] = {"f1": round(f1_score(yt, yp, average="macro"), 4),
                 "ci_lower": round(float(np.percentile(boots, 2.5)), 4),
                 "ci_upper": round(float(np.percentile(boots, 97.5)), 4)}

    rng2 = np.random.RandomState(seed + 1)
    ab = np.empty(n)
    for b in range(n):
        bf = []
        for g in sorted(gens):
            m = groups == g
            yt, yp = y[m], p[m]
            nn = len(yt)
            idx = rng2.randint(0, nn, nn)
            bf.append(f1_score(yt[idx], yp[idx], average="macro"))
        ab[b] = np.mean(bf)

    avg = round(np.mean([pg[g]["f1"] for g in sorted(gens)]), 4)
    ci = [round(float(np.percentile(ab, 2.5)), 4),
          round(float(np.percentile(ab, 97.5)), 4)]
    return avg, ci, pg


# ================================================================
# Main
# ================================================================

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--skip-inference", action="store_true",
                    help="Skip model inference, use saved detector_scores_all.csv")
    args = ap.parse_args()
    t0 = time.time()

    # --- 1. Load features ---
    print("Loading features_all_models.csv...")
    df_feat = pd.read_csv(DATA / "features_all_models.csv")
    df_feat["label"] = df_feat["depth"].map(CLASS_MAP)
    print(f"  {len(df_feat)} rows, gens={sorted(df_feat.model_name.unique())}")

    # --- 2. Load texts ---
    print("Loading texts from JSONL...")
    recs = []
    for mn, p in sorted(JSONL_PATHS.items()):
        if not p.exists():
            print(f"  SKIP {mn}"); continue
        ct = 0
        with open(p) as f:
            for line in f:
                r = json.loads(line)
                recs.append({"model_name": mn, "seed_id": r["seed_id"],
                             "depth": r["depth"], "text": r["text"]})
                ct += 1
        print(f"  {mn}: {ct}")
    df_txt = pd.DataFrame(recs)

    # --- 3. Merge ---
    df = df_feat.merge(df_txt, on=["model_name", "seed_id", "depth"], how="inner")
    print(f"  Merged: {len(df)} rows")
    gens = sorted(df["model_name"].unique())
    print(f"  Generators ({len(gens)}): {gens}")

    # --- 4. Detector scores ---
    if args.skip_inference and SCORES_CSV.exists():
        print(f"\nLoading saved scores from {SCORES_CSV}...")
        sc = pd.read_csv(SCORES_CSV)
        df = df.merge(sc[["model_name", "seed_id", "depth",
                          "avg_logprob", "fastdetectgpt", "binoculars"]],
                      on=["model_name", "seed_id", "depth"], how="left")
    else:
        print("\n=== Computing detector scores ===")
        import torch
        from transformers import AutoModelForCausalLM, AutoTokenizer

        texts = df["text"].tolist()

        print("Loading EleutherAI/pythia-410m (observer)...")
        tok = AutoTokenizer.from_pretrained("EleutherAI/pythia-410m", cache_dir=HF_CACHE, local_files_only=True)
        tok.pad_token = tok.eos_token
        obs = AutoModelForCausalLM.from_pretrained(
            "EleutherAI/pythia-410m", cache_dir=HF_CACHE, local_files_only=True).eval().to(DEVICE)

        print(f"Computing AvgLogProb + FastDetectGPT ({len(texts)} texts)...")
        t1 = time.time()
        fdg, lp = compute_fdg_logprob(texts, obs, tok, DEVICE)
        print(f"  Done: {time.time()-t1:.0f}s")

        print("Loading EleutherAI/pythia-160m (performer)...")
        prf = AutoModelForCausalLM.from_pretrained(
            "EleutherAI/pythia-160m", cache_dir=HF_CACHE, local_files_only=True).eval().to(DEVICE)

        print(f"Computing Binoculars ({len(texts)} texts)...")
        t1 = time.time()
        bino = compute_binoculars(texts, obs, prf, tok, DEVICE)
        print(f"  Done: {time.time()-t1:.0f}s")

        del obs, prf
        torch.cuda.empty_cache()

        df["avg_logprob"] = lp
        df["fastdetectgpt"] = fdg
        df["binoculars"] = bino

        df[["model_name", "seed_id", "depth", "label",
            "avg_logprob", "fastdetectgpt", "binoculars"]
        ].to_csv(SCORES_CSV, index=False)
        print(f"  Saved: {SCORES_CSV}")

    # --- Filter to generators with complete scores ---
    baseline_df = df.dropna(subset=["avg_logprob", "fastdetectgpt", "binoculars"]).copy()
    baseline_df = baseline_df.reset_index(drop=True)
    det_gens = sorted(baseline_df.model_name.unique())
    print(f"\nBaseline groups: {det_gens} ({len(baseline_df)} samples)")
    print(f"Feature groups:  {gens} ({len(df)} samples)")

    # --- 5. Trigram data for LD score ---
    print("\nBuilding trigram data...")
    tri = build_trigram_counts(baseline_df["text"].tolist())
    print(f"  Vocab size: {tri[2]}")

    # --- 6. LOGO Evaluation ---
    print("\n" + "=" * 60)
    print("LOGO Evaluation (4 groups)")
    print("=" * 60)

    results = {
        "n_generators_baseline": len(det_gens),
        "n_generators_feature": len(gens),
        "baseline_generators": det_gens,
        "feature_generators": gens,
        "unified_hyperparams": {k: v for k, v in UNIFIED_XGB.items() if k != "verbosity"},
        "groups": {},
    }

    # (a) 4-baseline
    print("\n(a) 4-baseline [avg_logprob, ld_score, fastdetectgpt, binoculars]")
    feat_a = ["avg_logprob", "ld_score", "fastdetectgpt", "binoculars"]
    f1_a, pg_a, y_a, p_a = logo_with_ld(baseline_df, feat_a, UNIFIED_XGB, det_gens, tri)
    avg_a, ci_a, pga = boot_ci(y_a, p_a, baseline_df["model_name"].values, det_gens)
    results["groups"]["4_baseline"] = {
        "features": feat_a, "avg_f1": f1_a, "ci95": ci_a, "per_generator": pga}
    print(f"  => Avg F1={f1_a}, CI={ci_a}")

    # (b) 4-baseline + surface
    print("\n(b) 4-baseline + surface [+ ttr, hapax_ratio]")
    feat_b = ["avg_logprob", "ld_score", "fastdetectgpt", "binoculars", "ttr", "hapax_ratio"]
    f1_b, pg_b, y_b, p_b = logo_with_ld(baseline_df, feat_b, UNIFIED_XGB, det_gens, tri)
    avg_b, ci_b, pgb = boot_ci(y_b, p_b, baseline_df["model_name"].values, det_gens)
    results["groups"]["4_baseline_plus_surface"] = {
        "features": feat_b, "avg_f1": f1_b, "ci95": ci_b, "per_generator": pgb}
    print(f"  => Avg F1={f1_b}, CI={ci_b}")

    # (c) 7-feature unified
    df_full = df.copy().reset_index(drop=True)
    print(f"\n(c) 7-feature unified [n_est=200, md=6]")
    f1_c, pg_c, y_c, p_c = logo_simple(df_full, FEAT_7, UNIFIED_XGB, gens)
    avg_c, ci_c, pgc = boot_ci(y_c, p_c, df_full["model_name"].values, gens)
    results["groups"]["7_feature_unified"] = {
        "features": FEAT_7, "avg_f1": f1_c, "ci95": ci_c, "per_generator": pgc}
    print(f"  => Avg F1={f1_c}, CI={ci_c}")

    # (d) 7-feature original (sanity check)
    print(f"\n(d) 7-feature original [sanity check, expect ≈0.789 for 6-gen]")
    f1_d, pg_d, y_d, p_d = logo_simple(df_full, FEAT_7, ORIGINAL_XGB, gens)
    avg_d, ci_d, pgd = boot_ci(y_d, p_d, df_full["model_name"].values, gens)
    results["groups"]["7_feature_original"] = {
        "features": FEAT_7, "avg_f1": f1_d, "ci95": ci_d, "per_generator": pgd}
    print(f"  => Avg F1={f1_d}, CI={ci_d}")

    # --- Summary ---
    print("\n" + "=" * 70)
    print(f"{'Group':<28} {'N-gen':>5} {'Avg F1':>8} {'95% CI':>22}")
    print("-" * 70)
    ng_map = {"4_baseline": len(det_gens), "4_baseline_plus_surface": len(det_gens),
              "7_feature_unified": len(gens), "7_feature_original": len(gens)}
    for name, g in results["groups"].items():
        print(f"{name:<28} {ng_map[name]:>5} {g['avg_f1']:>8.4f} "
              f"[{g['ci95'][0]:.4f}, {g['ci95'][1]:.4f}]")

    # --- Save ---
    out = RESULTS / "review_baseline_ensemble_results.json"
    with open(out, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved: {out}")
    print(f"Total: {time.time()-t0:.0f}s")


if __name__ == "__main__":
    main()
