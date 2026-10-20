#!/usr/bin/env python3
"""Paired bootstrap significance test for binary LOGO F1.
Re-runs LOGO to collect per-sample predictions, then does paired bootstrap
comparing 7-feature vs each baseline.
"""

import json, time
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

N_BOOT = 10000
LOGO_SEED = 789
BOOT_SEED = 42

FEAT_7 = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max",
           "tail_decay", "ttr", "hapax_ratio"]

ALL_6 = ["pythia-2.8b", "pythia-1b", "olmo-2-1b", "qwen3-0.6b", "qwen3-1.7b", "qwen3-8b"]

JSONL_PATHS = {
    "olmo-2-1b":   DATA / "olmo-2-1b" / "generations.jsonl",
    "pythia-1b":   DATA / "pythia-1b" / "generations.jsonl",
    "pythia-2.8b": DATA / "generations.jsonl",
    "qwen3-0.6b":  DATA / "qwen3-0.6b" / "generations.jsonl",
    "qwen3-1.7b":  DATA / "qwen3-1.7b" / "generations.jsonl",
    "qwen3-8b":    DATA / "qwen3-8b" / "generations.jsonl",
}

XGB_ENSEMBLE = dict(n_estimators=200, max_depth=6, learning_rate=0.1,
                    random_state=789, eval_metric="logloss", verbosity=0)
XGB_SINGLE = dict(n_estimators=100, max_depth=3, learning_rate=0.1,
                  random_state=789, eval_metric="logloss", verbosity=0)


def downsample(df, rng):
    vc = df["label"].value_counts()
    mn = vc.min()
    return pd.concat(
        [df[df["label"] == l].sample(n=mn, random_state=rng, replace=False)
         for l in sorted(vc.index)], ignore_index=True)


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


def logo_simple(df, feat_cols, params, gens):
    rng = np.random.RandomState(LOGO_SEED)
    preds = np.full(len(df), -1, dtype=int)
    for g in sorted(gens):
        tr = downsample(df[df["model_name"] != g].copy(), rng)
        tm = df["model_name"] == g
        clf = XGBClassifier(**params)
        clf.fit(tr[feat_cols].values, tr["label"].values)
        p = clf.predict(df.loc[tm, feat_cols].values)
        preds[tm.values] = p
    return preds


def logo_with_ld(df, feat_cols, params, gens, tri):
    cl, ng2i, V = tri
    rng = np.random.RandomState(LOGO_SEED)
    preds = np.full(len(df), -1, dtype=int)
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
    return preds


def compute_logo_f1(y_true, y_pred, groups, gens):
    """Compute LOGO macro F1: average of per-generator macro F1."""
    f1s = []
    for g in sorted(gens):
        m = groups == g
        f1s.append(f1_score(y_true[m], y_pred[m], average="macro"))
    return np.mean(f1s)


def paired_bootstrap(y_true, pred_a, pred_b, groups, gens, n_boot=N_BOOT, seed=BOOT_SEED):
    """Stratified paired bootstrap: resample within each generator."""
    rng = np.random.RandomState(seed)
    gen_indices = {g: np.where(groups == g)[0] for g in sorted(gens)}

    deltas = np.empty(n_boot)
    for b in range(n_boot):
        f1s_a, f1s_b = [], []
        for g in sorted(gens):
            idx = gen_indices[g]
            boot_idx = rng.choice(idx, size=len(idx), replace=True)
            yt = y_true[boot_idx]
            pa = pred_a[boot_idx]
            pb = pred_b[boot_idx]
            f1s_a.append(f1_score(yt, pa, average="macro"))
            f1s_b.append(f1_score(yt, pb, average="macro"))
        deltas[b] = np.mean(f1s_a) - np.mean(f1s_b)

    observed_delta = compute_logo_f1(y_true, pred_a, groups, gens) - \
                     compute_logo_f1(y_true, pred_b, groups, gens)

    p_value = float(np.mean(deltas <= 0))
    ci_lower = float(np.percentile(deltas, 2.5))
    ci_upper = float(np.percentile(deltas, 97.5))

    return {
        "delta": round(observed_delta, 4),
        "p_value": round(p_value, 6),
        "ci95": [round(ci_lower, 4), round(ci_upper, 4)],
        "bootstrap_mean_delta": round(float(np.mean(deltas)), 4),
    }


def main():
    t0 = time.time()

    print("Loading data...")
    df_feat = pd.read_csv(DATA / "features_all_models.csv")
    df_feat = df_feat[df_feat["model_name"].isin(ALL_6)].copy()

    df_scores = pd.read_csv(DATA / "detector_scores_all.csv")
    df_scores = df_scores[df_scores["model_name"].isin(ALL_6)].copy()

    recs = []
    for mn, p in sorted(JSONL_PATHS.items()):
        if not p.exists():
            print(f"  SKIP {mn}")
            continue
        with open(p) as f:
            for line in f:
                r = json.loads(line)
                recs.append({"model_name": mn, "seed_id": r["seed_id"],
                             "depth": r["depth"], "text": r["text"]})
    df_txt = pd.DataFrame(recs)

    df = df_feat.merge(
        df_scores[["model_name", "seed_id", "depth", "avg_logprob", "fastdetectgpt", "binoculars"]],
        on=["model_name", "seed_id", "depth"], how="inner")
    df = df.merge(df_txt, on=["model_name", "seed_id", "depth"], how="inner")

    df = df[df["depth"] >= 1].copy().reset_index(drop=True)
    df["label"] = (df["depth"] >= 2).astype(int)
    gens = sorted(df["model_name"].unique())
    print(f"Data: {len(df)} samples, {len(gens)} generators")
    print(f"Label dist: {df['label'].value_counts().to_dict()}")

    print("\nBuilding trigrams...")
    tri = build_trigram_counts(df["text"].tolist())
    print(f"Vocab size: {tri[2]}")

    # Run LOGO for each method
    methods = {}

    print("\n--- 7_feature LOGO ---")
    methods["7_feature"] = logo_simple(df, FEAT_7, XGB_ENSEMBLE, gens)
    f1_7 = compute_logo_f1(df["label"].values, methods["7_feature"], df["model_name"].values, gens)
    print(f"  F1 = {f1_7:.4f}")

    print("--- avg_logprob LOGO ---")
    methods["avg_logprob"] = logo_simple(df, ["avg_logprob"], XGB_SINGLE, gens)
    f1_alp = compute_logo_f1(df["label"].values, methods["avg_logprob"], df["model_name"].values, gens)
    print(f"  F1 = {f1_alp:.4f}")

    print("--- ld_score LOGO ---")
    methods["ld_score"] = logo_with_ld(df, ["ld_score"], XGB_SINGLE, gens, tri)
    f1_ld = compute_logo_f1(df["label"].values, methods["ld_score"], df["model_name"].values, gens)
    print(f"  F1 = {f1_ld:.4f}")

    print("--- fastdetectgpt LOGO ---")
    methods["fastdetectgpt"] = logo_simple(df, ["fastdetectgpt"], XGB_SINGLE, gens)
    f1_fdg = compute_logo_f1(df["label"].values, methods["fastdetectgpt"], df["model_name"].values, gens)
    print(f"  F1 = {f1_fdg:.4f}")

    print("--- binoculars LOGO ---")
    methods["binoculars"] = logo_simple(df, ["binoculars"], XGB_SINGLE, gens)
    f1_bin = compute_logo_f1(df["label"].values, methods["binoculars"], df["model_name"].values, gens)
    print(f"  F1 = {f1_bin:.4f}")

    print("--- 4_baseline (4-detector ensemble) LOGO ---")
    methods["4_baseline"] = logo_with_ld(
        df, ["avg_logprob", "ld_score", "fastdetectgpt", "binoculars"],
        XGB_ENSEMBLE, gens, tri)
    f1_4b = compute_logo_f1(df["label"].values, methods["4_baseline"], df["model_name"].values, gens)
    print(f"  F1 = {f1_4b:.4f}")

    print(f"\nLOGO complete in {time.time()-t0:.1f}s")

    # Paired bootstrap tests
    y_true = df["label"].values
    groups = df["model_name"].values

    comparisons = {
        "7feat_vs_avglogprob": ("7_feature", "avg_logprob"),
        "7feat_vs_ldscore": ("7_feature", "ld_score"),
        "7feat_vs_fastdetectgpt": ("7_feature", "fastdetectgpt"),
        "7feat_vs_binoculars": ("7_feature", "binoculars"),
        "7feat_vs_4det_ensemble": ("7_feature", "4_baseline"),
    }

    print("\n" + "=" * 70)
    print("PAIRED BOOTSTRAP SIGNIFICANCE TESTS (n=10000)")
    print("=" * 70)

    results = {}
    for name, (method_a, method_b) in comparisons.items():
        print(f"\n--- {name} ---")
        r = paired_bootstrap(y_true, methods[method_a], methods[method_b],
                           groups, gens, n_boot=N_BOOT, seed=BOOT_SEED)
        results[name] = r

        sig = "***" if r["p_value"] < 0.001 else ("**" if r["p_value"] < 0.01 else ("*" if r["p_value"] < 0.05 else "n.s."))
        warn = ""
        if r["p_value"] >= 0.05 and name in ("7feat_vs_avglogprob", "7feat_vs_4det_ensemble"):
            warn = " ⚠️ NOT SIGNIFICANT"
        elif r["p_value"] >= 0.001:
            warn = f" (paper claims p<0.001 but actual p={r['p_value']:.4f})"

        print(f"  delta = {r['delta']:.4f}")
        print(f"  p-value = {r['p_value']:.6f} {sig}{warn}")
        print(f"  95% CI of delta = [{r['ci95'][0]:.4f}, {r['ci95'][1]:.4f}]")

    # Summary table
    print("\n" + "=" * 90)
    print(f"{'Comparison':<28} {'Delta':>7} {'p-value':>10} {'95% CI':>22} {'Sig':>6}")
    print("-" * 90)
    for name, r in results.items():
        sig = "***" if r["p_value"] < 0.001 else ("**" if r["p_value"] < 0.01 else ("*" if r["p_value"] < 0.05 else "n.s."))
        warn = ""
        if r["p_value"] >= 0.05 and name in ("7feat_vs_avglogprob", "7feat_vs_4det_ensemble"):
            warn = " ⚠️ NOT SIGNIFICANT"
        elif r["p_value"] >= 0.001 and r["p_value"] < 0.05:
            warn = " ⚠️ NOT p<0.001"
        elif r["p_value"] >= 0.05:
            warn = " ⚠️ NOT SIGNIFICANT"
        print(f"{name:<28} {r['delta']:>+7.4f} {r['p_value']:>10.6f} [{r['ci95'][0]:>+.4f}, {r['ci95'][1]:>+.4f}] {sig:>6}{warn}")

    # Save
    out = RESULTS / "binary_bootstrap_pvalue.json"
    with open(out, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved: {out}")
    print(f"Total: {time.time()-t0:.1f}s")


if __name__ == "__main__":
    main()
