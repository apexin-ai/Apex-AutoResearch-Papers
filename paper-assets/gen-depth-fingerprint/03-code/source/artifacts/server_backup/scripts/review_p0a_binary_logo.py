#!/usr/bin/env python3
"""P0-A: Binary LOGO (gen-1 vs gen-2+), gen-0 excluded.
Addresses reviewer concern about gen-0 data leakage across generators.
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
RESULTS.mkdir(exist_ok=True)

N_BOOT = 1000
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
    pg = {}
    for g in sorted(gens):
        tr = downsample(df[df["model_name"] != g].copy(), rng)
        tm = df["model_name"] == g
        clf = XGBClassifier(**params)
        clf.fit(tr[feat_cols].values, tr["label"].values)
        p = clf.predict(df.loc[tm, feat_cols].values)
        preds[tm.values] = p
        pg[g] = round(f1_score(df.loc[tm, "label"], p, average="macro"), 4)
        print(f"    hold={g}: F1={pg[g]}", flush=True)
    return round(np.mean(list(pg.values())), 4), pg, df["label"].values.copy(), preds


def logo_with_ld(df, feat_cols, params, gens, tri):
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
        print(f"    hold={g}: F1={pg[g]}", flush=True)
    return round(np.mean(list(pg.values())), 4), pg, df["label"].values.copy(), preds


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


def main():
    t0 = time.time()

    print("Loading features...")
    df_feat = pd.read_csv(DATA / "features_all_models.csv")
    df_feat = df_feat[df_feat["model_name"].isin(ALL_6)].copy()
    print(f"  features: {len(df_feat)} rows")

    print("Loading detector scores...")
    df_scores = pd.read_csv(DATA / "detector_scores_all.csv")
    df_scores = df_scores[df_scores["model_name"].isin(ALL_6)].copy()
    print(f"  scores: {len(df_scores)} rows")

    print("Loading texts...")
    recs = []
    for mn, p in sorted(JSONL_PATHS.items()):
        if not p.exists():
            print(f"  SKIP {mn}")
            continue
        ct = 0
        with open(p) as f:
            for line in f:
                r = json.loads(line)
                recs.append({"model_name": mn, "seed_id": r["seed_id"],
                             "depth": r["depth"], "text": r["text"]})
                ct += 1
        print(f"  {mn}: {ct}")
    df_txt = pd.DataFrame(recs)

    df = df_feat.merge(
        df_scores[["model_name", "seed_id", "depth", "avg_logprob", "fastdetectgpt", "binoculars"]],
        on=["model_name", "seed_id", "depth"], how="inner")
    df = df.merge(df_txt, on=["model_name", "seed_id", "depth"], how="inner")
    print(f"  Merged: {len(df)} rows, gens={sorted(df.model_name.unique())}")

    # Exclude gen-0
    df = df[df["depth"] >= 1].copy().reset_index(drop=True)
    print(f"  After gen-0 exclusion: {len(df)} rows")
    print(f"  Depths remaining: {sorted(df.depth.unique())}")

    # Binary label: gen-1 -> 0, gen-2+ -> 1
    df["label"] = (df["depth"] >= 2).astype(int)
    print(f"  Label dist: {df['label'].value_counts().to_dict()}")

    gens = sorted(df["model_name"].unique())
    print(f"  Generators ({len(gens)}): {gens}")

    print("\nBuilding trigrams...")
    tri = build_trigram_counts(df["text"].tolist())
    print(f"  Vocab size: {tri[2]}")

    print("\n" + "=" * 60)
    print("Binary LOGO: gen-1 vs gen-2+ (gen-0 excluded)")
    print("=" * 60)

    results = {
        "task": "binary (gen-1 vs gen-2+), gen-0 excluded",
        "n_generators": len(gens),
        "generators": gens,
        "n_samples": len(df),
        "methods": {}
    }

    def eval_method(name, feat_cols, params, use_ld=False):
        print(f"\n--- {name} ---")
        if use_ld:
            f1, pg, y, p = logo_with_ld(df, feat_cols, params, gens, tri)
        else:
            f1, pg, y, p = logo_simple(df, feat_cols, params, gens)
        avg, ci, pg_boot = boot_ci(y, p, df["model_name"].values, gens)
        per_gen_f1s = [pg_boot[g]["f1"] for g in sorted(gens)]
        std_val = round(float(np.std(per_gen_f1s)), 4)
        range_val = round(max(per_gen_f1s) - min(per_gen_f1s), 4)
        results["methods"][name] = {
            "f1": avg, "ci95": ci, "per_gen": pg_boot,
            "per_gen_std": std_val, "per_gen_range": range_val,
        }
        print(f"  => F1={avg}, CI={ci}, std={std_val}, range={range_val}")

    eval_method("7_feature", FEAT_7, XGB_ENSEMBLE)
    eval_method("avg_logprob", ["avg_logprob"], XGB_SINGLE)
    eval_method("ld_score", ["ld_score"], XGB_SINGLE, use_ld=True)
    eval_method("fastdetectgpt", ["fastdetectgpt"], XGB_SINGLE)
    eval_method("binoculars", ["binoculars"], XGB_SINGLE)
    eval_method("4_baseline",
                ["avg_logprob", "ld_score", "fastdetectgpt", "binoculars"],
                XGB_ENSEMBLE, use_ld=True)
    eval_method("4_baseline_surface",
                ["avg_logprob", "ld_score", "fastdetectgpt", "binoculars", "ttr", "hapax_ratio"],
                XGB_ENSEMBLE, use_ld=True)

    print("\n" + "=" * 80)
    print(f"{'Method':<22} {'F1':>6} {'95% CI':>22} {'Std':>6} {'Range':>6}")
    print("-" * 80)
    for name, m in results["methods"].items():
        print(f"{name:<22} {m['f1']:>6.4f} [{m['ci95'][0]:.4f}, {m['ci95'][1]:.4f}] "
              f"{m['per_gen_std']:>6.4f} {m['per_gen_range']:>6.4f}")

    out = RESULTS / "review_p0a_binary_logo.json"
    with open(out, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved: {out}")
    print(f"Total: {time.time()-t0:.1f}s")


if __name__ == "__main__":
    main()
