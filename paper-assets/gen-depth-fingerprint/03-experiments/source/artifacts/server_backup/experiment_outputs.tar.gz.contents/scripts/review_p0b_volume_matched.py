#!/usr/bin/env python3
"""P0-B: Volume-matched 5-gen control experiment.

Isolates data-volume effect from generator-diversity effect by bootstrap
upsampling 5-gen LOGO train sets to match 6-gen train sizes.
"""
import json, time
import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.metrics import f1_score
from xgboost import XGBClassifier

ROOT = Path("/root/gen-depth-fingerprint")
DATA = ROOT / "data"
OUT  = ROOT / "results"
OUT.mkdir(exist_ok=True)

FEAT_COLS = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max",
             "tail_decay", "ttr", "hapax_ratio"]
CLASS_MAP = {0: 0, 1: 1, 2: 2, 3: 2, 4: 2}

XGB_PARAMS = dict(n_estimators=200, max_depth=6, learning_rate=0.1,
                  random_state=789, eval_metric="mlogloss", verbosity=0)

ALL_6 = ["pythia-2.8b", "pythia-1b", "olmo-2-1b", "qwen3-0.6b", "qwen3-1.7b", "qwen3-8b"]
ALL_5 = [g for g in ALL_6 if g != "qwen3-8b"]

LOGO_SEED = 789
SEEDS = [42, 123, 456]


def downsample(df, rng):
    counts = df["label"].value_counts()
    min_n = counts.min()
    parts = [df[df["label"] == lbl].sample(n=min_n, random_state=rng, replace=False)
             for lbl in sorted(counts.index)]
    return pd.concat(parts, ignore_index=True)


def logo_5gen_original(df5):
    """Original 5-gen LOGO (reproduces F1=0.800)."""
    preds = np.full(len(df5), -1, dtype=int)
    rng = np.random.RandomState(LOGO_SEED)
    for hold in sorted(ALL_5):
        train_df = downsample(df5[df5["model_name"] != hold], rng)
        test_mask = (df5["model_name"] == hold).values
        clf = XGBClassifier(**XGB_PARAMS)
        clf.fit(train_df[FEAT_COLS].values, train_df["label"].values)
        preds[test_mask] = clf.predict(df5.loc[test_mask, FEAT_COLS].values)
    assert (preds >= 0).all()
    return preds


def compute_6gen_train_sizes(df6):
    """For each 6-gen LOGO fold, compute the post-downsample train size."""
    sizes = {}
    rng = np.random.RandomState(LOGO_SEED)
    for hold in sorted(ALL_6):
        train_raw = df6[df6["model_name"] != hold]
        train_ds = downsample(train_raw, rng)
        sizes[hold] = len(train_ds)
    return sizes


def logo_5gen_volume_matched(df5, df6, seed):
    """5-gen LOGO with train data upsampled to match 6-gen train size."""
    sixgen_train_sizes = compute_6gen_train_sizes(df6)
    avg_6gen_train = int(np.mean(list(sixgen_train_sizes.values())))

    preds = np.full(len(df5), -1, dtype=int)
    rng_logo = np.random.RandomState(LOGO_SEED)
    rng_upsample = np.random.RandomState(seed)

    for hold in sorted(ALL_5):
        train_raw = df5[df5["model_name"] != hold]
        train_ds = downsample(train_raw, rng_logo)
        n_train_orig = len(train_ds)

        # Upsample with replacement to match avg 6-gen train size
        if n_train_orig < avg_6gen_train:
            extra_n = avg_6gen_train - n_train_orig
            extra_idx = rng_upsample.choice(n_train_orig, size=extra_n, replace=True)
            extra = train_ds.iloc[extra_idx]
            train_final = pd.concat([train_ds, extra], ignore_index=True)
        else:
            train_final = train_ds

        test_mask = (df5["model_name"] == hold).values
        clf = XGBClassifier(**XGB_PARAMS)
        clf.fit(train_final[FEAT_COLS].values, train_final["label"].values)
        preds[test_mask] = clf.predict(df5.loc[test_mask, FEAT_COLS].values)

    assert (preds >= 0).all()
    return preds, avg_6gen_train


def per_gen_f1(df, preds, generators):
    y = df["label"].values
    groups = df["model_name"].values
    results = {}
    for g in sorted(generators):
        mask = groups == g
        results[g] = round(f1_score(y[mask], preds[mask], average="macro"), 4)
    results["avg"] = round(np.mean(list(results.values())), 4)
    return results


def main():
    t0 = time.time()
    df = pd.read_csv(DATA / "features_all_models.csv")
    df["label"] = df["depth"].map(CLASS_MAP)

    df6 = df[df["model_name"].isin(ALL_6)].copy().reset_index(drop=True)
    df5 = df[df["model_name"].isin(ALL_5)].copy().reset_index(drop=True)

    print(f"6-gen N={len(df6)}, 5-gen N={len(df5)}")
    print(f"Per-gen counts:")
    for g in sorted(ALL_6):
        n = len(df6[df6["model_name"] == g])
        print(f"  {g}: {n}")

    # --- 5-gen original ---
    print("\n=== 5-gen LOGO (original) ===")
    preds_5orig = logo_5gen_original(df5)
    f1_5orig = per_gen_f1(df5, preds_5orig, ALL_5)
    for g, v in f1_5orig.items():
        print(f"  {g}: {v}")

    # --- 5-gen volume-matched (3 seeds) ---
    print("\n=== 5-gen Volume-Matched LOGO ===")
    seed_results = {}
    for seed in SEEDS:
        preds_vm, avg_train_size = logo_5gen_volume_matched(df5, df6, seed)
        f1_vm = per_gen_f1(df5, preds_vm, ALL_5)
        seed_results[seed] = f1_vm
        print(f"\n  Seed {seed} (train upsampled to ~{avg_train_size}):")
        for g, v in f1_vm.items():
            print(f"    {g}: {v}")

    # Average across seeds
    avg_vm = {}
    for g in sorted(ALL_5) + ["avg"]:
        avg_vm[g] = round(np.mean([seed_results[s][g] for s in SEEDS]), 4)
    print(f"\n  Mean across seeds:")
    for g, v in avg_vm.items():
        print(f"    {g}: {v}")

    # --- 6-gen reference (excl qwen3-8b) ---
    ref_6gen_excl = {"olmo-2-1b": 0.7649, "pythia-1b": 0.8528, "pythia-2.8b": 0.8037,
                     "qwen3-0.6b": 0.8231, "qwen3-1.7b": 0.8064}
    ref_6gen_avg = round(np.mean(list(ref_6gen_excl.values())), 4)
    print(f"\n=== 6-gen LOGO (excl qwen3-8b, from Table 1) ===")
    for g, v in sorted(ref_6gen_excl.items()):
        print(f"  {g}: {v}")
    print(f"  avg: {ref_6gen_avg}")

    # --- Summary ---
    delta_volume = round(avg_vm["avg"] - f1_5orig["avg"], 4)
    delta_total = round(ref_6gen_avg - f1_5orig["avg"], 4)
    delta_diversity = round(delta_total - delta_volume, 4)

    print(f"\n=== Decomposition ===")
    print(f"  5-gen original avg F1:       {f1_5orig['avg']}")
    print(f"  5-gen volume-matched avg F1: {avg_vm['avg']}")
    print(f"  6-gen (excl qwen3-8b) avg:   {ref_6gen_avg}")
    print(f"  Volume effect (VM - orig):   {delta_volume:+.4f}")
    print(f"  Total effect (6gen - orig):  {delta_total:+.4f}")
    print(f"  Diversity residual:          {delta_diversity:+.4f}")

    results = {
        "experiment": "P0-B volume-matched 5-gen control",
        "5gen_original": f1_5orig,
        "5gen_volume_matched_per_seed": {str(s): seed_results[s] for s in SEEDS},
        "5gen_volume_matched_avg": avg_vm,
        "6gen_excl_qwen3_8b": {**ref_6gen_excl, "avg": ref_6gen_avg},
        "decomposition": {
            "volume_effect": delta_volume,
            "total_effect": delta_total,
            "diversity_residual": delta_diversity,
        },
        "seeds": SEEDS,
        "xgb_params": {k: v for k, v in XGB_PARAMS.items() if k != "verbosity"},
    }

    out_path = OUT / "review_p0b_volume_matched.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved: {out_path}")
    print(f"Total: {time.time()-t0:.1f}s")


if __name__ == "__main__":
    main()
