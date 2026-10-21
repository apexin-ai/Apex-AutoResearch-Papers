#!/usr/bin/env python3
"""P1-D: 6-gen LOGO single-baseline comparison with two hyperparam sets.

For each of 4 single baselines (avg_logprob, ld_score, fastdetectgpt, binoculars),
run 6-gen LOGO (3-class: gen-0/gen-1/gen-2+) with:
  - Group 1: n_estimators=100, max_depth=3
  - Group 2: n_estimators=200, max_depth=6

Output: results/review_p1d_6gen_baselines.json
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

ALL_6 = ["pythia-2.8b", "pythia-1b", "olmo-2-1b", "qwen3-0.6b", "qwen3-1.7b", "qwen3-8b"]
CLASS_MAP = {0: 0, 1: 1, 2: 2, 3: 2, 4: 2}

JSONL_PATHS = {
    "olmo-2-1b":   DATA / "olmo-2-1b" / "generations.jsonl",
    "pythia-1b":   DATA / "pythia-1b" / "generations.jsonl",
    "pythia-2.8b": DATA / "generations.jsonl",
    "qwen3-0.6b":  DATA / "qwen3-0.6b" / "generations.jsonl",
    "qwen3-1.7b":  DATA / "qwen3-1.7b" / "generations.jsonl",
    "qwen3-8b":    DATA / "qwen3-8b" / "generations.jsonl",
}

HYPERPARAM_SETS = {
    "hyperparams_100_3": dict(n_estimators=100, max_depth=3, learning_rate=0.1,
                              random_state=789, eval_metric="mlogloss", verbosity=0),
    "hyperparams_200_6": dict(n_estimators=200, max_depth=6, learning_rate=0.1,
                              random_state=789, eval_metric="mlogloss", verbosity=0),
}

SINGLE_BASELINES = ["avg_logprob", "ld_score", "fastdetectgpt", "binoculars"]


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


def downsample(df, rng):
    vc = df["label"].value_counts()
    mn = vc.min()
    return pd.concat(
        [df[df["label"] == l].sample(n=mn, random_state=rng, replace=False)
         for l in sorted(vc.index)], ignore_index=True)


def logo_single(df, feat_col, params, gens):
    rng = np.random.RandomState(LOGO_SEED)
    preds = np.full(len(df), -1, dtype=int)
    pg = {}
    for g in sorted(gens):
        tr = downsample(df[df["model_name"] != g].copy(), rng)
        tm = df["model_name"] == g
        clf = XGBClassifier(**params)
        clf.fit(tr[[feat_col]].values, tr["label"].values)
        p = clf.predict(df.loc[tm, [feat_col]].values)
        preds[tm.values] = p
        pg[g] = round(f1_score(df.loc[tm, "label"], p, average="macro"), 4)
    return pg, df["label"].values.copy(), preds


def logo_ld_single(df, params, gens, tri):
    cl, ng2i, V = tri
    rng = np.random.RandomState(LOGO_SEED)
    preds = np.full(len(df), -1, dtype=int)
    pg = {}
    for g in sorted(gens):
        tr_mask = df["model_name"] != g
        tm = df["model_name"] == g
        ref = df.index[tr_mask & (df["label"] == 0)].tolist()
        df["_ld_fold"] = ld_scores_from_ref(cl, ref, ng2i, V)
        tr = downsample(df[tr_mask].copy(), rng)
        clf = XGBClassifier(**params)
        clf.fit(tr[["_ld_fold"]].values, tr["label"].values)
        p = clf.predict(df.loc[tm, ["_ld_fold"]].values)
        preds[tm.values] = p
        pg[g] = round(f1_score(df.loc[tm, "label"], p, average="macro"), 4)
        print(f"    LD LOGO hold={g}: F1={pg[g]}", flush=True)
    return pg, df["label"].values.copy(), preds


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

    # Load detector scores
    print("Loading detector scores...")
    scores_df = pd.read_csv(DATA / "detector_scores_all.csv")
    scores_df = scores_df[scores_df["model_name"].isin(ALL_6)].copy().reset_index(drop=True)
    print(f"  N={len(scores_df)}, gens={sorted(scores_df['model_name'].unique())}")

    # Load texts for LD score
    print("Loading texts for LD score...")
    text_records = []
    for model_name, path in JSONL_PATHS.items():
        count = 0
        with open(path) as f:
            for line in f:
                rec = json.loads(line)
                text_records.append({"model_name": model_name,
                                     "seed_id": rec["seed_id"],
                                     "depth": rec["depth"],
                                     "text": rec["text"]})
                count += 1
        print(f"  {model_name}: {count}")
    text_df = pd.DataFrame(text_records)
    text_df["label"] = text_df["depth"].map(CLASS_MAP)
    text_df = text_df[text_df["model_name"].isin(ALL_6)].copy().reset_index(drop=True)

    # Merge texts into scores_df for LD computation
    merged = scores_df.merge(text_df[["model_name", "seed_id", "depth", "text"]],
                             on=["model_name", "seed_id", "depth"], how="inner")
    merged = merged.reset_index(drop=True)
    print(f"  Merged N={len(merged)}")

    # Build trigram data
    print("Building trigram data...")
    tri = build_trigram_counts(merged["text"].tolist())
    print(f"  Vocab size: {tri[2]}")

    # Run all experiments
    results = {}
    groups = merged["model_name"].values

    for hp_name, params in HYPERPARAM_SETS.items():
        print(f"\n{'='*60}")
        print(f"Hyperparams: {hp_name} (n_est={params['n_estimators']}, md={params['max_depth']})")
        print("="*60)
        results[hp_name] = {}

        for feat in SINGLE_BASELINES:
            print(f"\n  {feat}...")
            if feat == "ld_score":
                pg, y, p = logo_ld_single(merged, params, ALL_6, tri)
            else:
                pg, y, p = logo_single(merged, feat, params, ALL_6)

            avg_f1, ci, per_gen = boot_ci(y, p, groups, ALL_6)
            results[hp_name][feat] = {
                "f1": avg_f1,
                "ci95": ci,
                "per_gen": per_gen,
            }
            print(f"    Avg F1={avg_f1}, CI={ci}")
            for g in sorted(ALL_6):
                print(f"      {g}: {per_gen[g]['f1']} [{per_gen[g]['ci_lower']}, {per_gen[g]['ci_upper']}]")

    # Compute deltas
    print(f"\n{'='*60}")
    print("Delta: 200/6 vs 100/3")
    print("="*60)
    delta = {}
    for feat in SINGLE_BASELINES:
        d = round(results["hyperparams_200_6"][feat]["f1"] - results["hyperparams_100_3"][feat]["f1"], 4)
        delta[feat] = d
        print(f"  {feat}: {d:+.4f}")
    results["delta_200_6_vs_100_3"] = delta

    # Summary table
    print(f"\n{'='*70}")
    print(f"{'Baseline':<16} {'100/3 F1':>10} {'100/3 CI':>22} {'200/6 F1':>10} {'200/6 CI':>22} {'Delta':>8}")
    print("-"*90)
    for feat in SINGLE_BASELINES:
        r1 = results["hyperparams_100_3"][feat]
        r2 = results["hyperparams_200_6"][feat]
        d = delta[feat]
        print(f"{feat:<16} {r1['f1']:>10.4f} [{r1['ci95'][0]:.4f}, {r1['ci95'][1]:.4f}]"
              f" {r2['f1']:>10.4f} [{r2['ci95'][0]:.4f}, {r2['ci95'][1]:.4f}] {d:>+8.4f}")

    # Save
    out_path = RESULTS / "review_p1d_6gen_baselines.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved: {out_path}")
    print(f"Total: {time.time()-t0:.1f}s")


if __name__ == "__main__":
    main()
