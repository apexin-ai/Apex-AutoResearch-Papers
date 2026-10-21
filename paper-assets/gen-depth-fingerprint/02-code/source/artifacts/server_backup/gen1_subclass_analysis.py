"""
Gen-1 subclass error analysis by generator.
Binary LOGO (gen-1 vs gen-2+), reporting per-generator gen-1 error metrics.
Uses sklearn HistGradientBoosting to avoid xgboost CUDA dependency.
"""

import json
import os
import numpy as np
import pandas as pd
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.metrics import f1_score, confusion_matrix
from scipy.stats import spearmanr

SEED = 42
FEATURES = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max",
            "tail_decay", "ttr", "hapax_ratio"]

CLASS_MAP_3 = {0: 0, 1: 1, 2: 2, 3: 2, 4: 2}

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(ROOT, "data")
RESULTS_DIR = os.path.join(ROOT, "results")

MODEL_SIZES = {
    "qwen3-0.6b": 0.6,
    "pythia-1b": 1.0,
    "olmo-2-1b": 1.0,
    "qwen3-1.7b": 1.7,
    "pythia-2.8b": 2.8,
    "llama-3.2-3b": 3.0,
    "mistral-7b-v0.3": 7.0,
    "qwen3-8b": 8.0,
}


def load_data():
    df_base = pd.read_csv(os.path.join(DATA_DIR, "features_all_models.csv"))
    new_gens = [
        ("llama-3.2-3b", os.path.join(DATA_DIR, "llama-3.2-3b", "features_pythia410m.jsonl")),
        ("mistral-7b-v0.3", os.path.join(DATA_DIR, "mistral-7b-v0.3", "features_pythia410m.jsonl")),
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


def downsample(df, label_col, rng):
    counts = df[label_col].value_counts()
    min_n = counts.min()
    parts = []
    for lbl in sorted(counts.index):
        sub = df[df[label_col] == lbl]
        parts.append(sub.sample(n=min_n, random_state=rng, replace=False))
    return pd.concat(parts, ignore_index=True)


def main():
    df = load_data()
    df["label3"] = df["depth"].map(CLASS_MAP_3)
    df_binary = df[df["label3"] >= 1].copy()
    df_binary["binary_label"] = (df_binary["label3"] >= 2).astype(int)  # gen-1=0, gen-2+=1

    generators = sorted(df_binary["model_name"].unique())
    rng = np.random.RandomState(SEED)
    results = {}

    print("=== Gen-1 Subclass Error Analysis (Binary LOGO) ===\n")

    for gen in generators:
        test_df = df_binary[df_binary["model_name"] == gen].copy()
        train_df = df_binary[df_binary["model_name"] != gen]

        if test_df["binary_label"].nunique() < 2:
            print(f"  {gen:20s}  SKIPPED (single class in test)")
            continue

        train_ds = downsample(train_df, "binary_label", rng)

        clf = HistGradientBoostingClassifier(
            max_iter=200, max_depth=6, learning_rate=0.1, random_state=SEED
        )
        clf.fit(train_ds[FEATURES].values, train_ds["binary_label"].values)
        y_pred = clf.predict(test_df[FEATURES].values)
        y_test = test_df["binary_label"].values

        # gen-1 = class 0, gen-2+ = class 1
        cm = confusion_matrix(y_test, y_pred, labels=[0, 1])
        # Treating gen-1 as positive class:
        # cm[0,0] = gen-1 correctly classified as gen-1
        # cm[0,1] = gen-1 misclassified as gen-2+ (false negative for gen-1)
        # cm[1,0] = gen-2+ misclassified as gen-1 (false positive for gen-1)
        # cm[1,1] = gen-2+ correctly classified as gen-2+

        n_gen1 = int(cm[0, 0] + cm[0, 1])
        n_gen2p = int(cm[1, 0] + cm[1, 1])

        gen1_f1 = f1_score(y_test, y_pred, pos_label=0)
        fnr = cm[0, 1] / n_gen1 if n_gen1 > 0 else 0
        fpr = cm[1, 0] / n_gen2p if n_gen2p > 0 else 0

        binary_macro_f1 = f1_score(y_test, y_pred, average="macro")

        results[gen] = {
            "size_B": MODEL_SIZES.get(gen, None),
            "n_gen1": n_gen1,
            "n_gen2p": n_gen2p,
            "gen1_f1": round(float(gen1_f1), 4),
            "binary_macro_f1": round(float(binary_macro_f1), 4),
            "fnr": round(float(fnr), 4),
            "fpr": round(float(fpr), 4),
            "confusion_matrix": cm.tolist(),
        }

        print(f"  {gen:20s}  gen1_f1={gen1_f1:.4f}  FNR={fnr:.4f}  FPR={fpr:.4f}  n_gen1={n_gen1}")

    sorted_gens = sorted(results.keys(), key=lambda g: MODEL_SIZES.get(g, 99))

    print(f"\n{'Generator':<20s} {'Size':>6s} {'gen1-N':>7s} {'gen1-F1':>8s} {'FNR':>7s} {'FPR':>7s} {'Macro-F1':>9s}")
    print("-" * 70)
    for gen in sorted_gens:
        r = results[gen]
        print(f"{gen:<20s} {r['size_B']:>5.1f}B {r['n_gen1']:>7d} {r['gen1_f1']:>8.4f} {r['fnr']:>7.4f} {r['fpr']:>7.4f} {r['binary_macro_f1']:>9.4f}")

    sizes = [results[g]["size_B"] for g in sorted_gens]
    fnrs = [results[g]["fnr"] for g in sorted_gens]
    gen1_f1s = [results[g]["gen1_f1"] for g in sorted_gens]
    fprs = [results[g]["fpr"] for g in sorted_gens]

    rho_fnr, p_fnr = spearmanr(sizes, fnrs)
    rho_f1, p_f1 = spearmanr(sizes, gen1_f1s)
    rho_fpr, p_fpr = spearmanr(sizes, fprs)

    print(f"\nSpearman correlations (model_size vs metric):")
    print(f"  size vs FNR:     rho={rho_fnr:+.4f}, p={p_fnr:.4f}")
    print(f"  size vs gen1-F1: rho={rho_f1:+.4f}, p={p_f1:.4f}")
    print(f"  size vs FPR:     rho={rho_fpr:+.4f}, p={p_fpr:.4f}")

    output = {
        "experiment": "gen1_subclass_error_analysis",
        "classifier": "HistGradientBoostingClassifier(max_iter=200, max_depth=6, lr=0.1)",
        "per_generator": {g: results[g] for g in sorted_gens},
        "correlations": {
            "size_vs_fnr": {"rho": round(rho_fnr, 4), "p": round(p_fnr, 4)},
            "size_vs_gen1_f1": {"rho": round(rho_f1, 4), "p": round(p_f1, 4)},
            "size_vs_fpr": {"rho": round(rho_fpr, 4), "p": round(p_fpr, 4)},
        },
        "size_ordering": [g for g in sorted_gens],
    }

    os.makedirs(RESULTS_DIR, exist_ok=True)
    out_path = os.path.join(RESULTS_DIR, "gen1_subclass_analysis.json")
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"\nResults saved to {out_path}")


if __name__ == "__main__":
    main()
