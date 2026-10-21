import json
import numpy as np
import pandas as pd
from pathlib import Path
from xgboost import XGBClassifier
from sklearn.metrics import f1_score

SEED = 42
ROOT = Path("/root/gen-depth-fingerprint")
FEATURES = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max",
            "tail_decay", "ttr", "hapax_ratio"]
CLASS_MAP = {0: 0, 1: 1, 2: 2, 3: 2, 4: 2}
XGB_PARAMS = dict(n_estimators=200, max_depth=6, learning_rate=0.1,
                  random_state=SEED, eval_metric="mlogloss",
                  use_label_encoder=False)


def downsample(df, rng):
    min_n = df["label"].value_counts().min()
    parts = [df[df["label"] == lbl].sample(n=min_n, random_state=rng, replace=False)
             for lbl in sorted(df["label"].unique())]
    return pd.concat(parts, ignore_index=True)


def load_7gen():
    base = pd.read_csv(ROOT / "data" / "features_all_models.csv")
    base["label"] = base["depth"].map(CLASS_MAP)

    inst = pd.read_csv(ROOT / "data" / "features_qwen3-1.7b-instruct.csv")
    inst["model_name"] = "qwen3-1.7b-instruct"
    inst["label"] = inst["depth"].map(CLASS_MAP)

    df = pd.concat([base, inst], ignore_index=True)
    print(f"7-gen dataset: {len(df)} rows, generators: {sorted(df['model_name'].unique())}")
    print(df["model_name"].value_counts().sort_index())
    return df


def logo_3class(df):
    generators = sorted(df["model_name"].unique())
    results = {}
    rng = np.random.RandomState(SEED)

    for gen in generators:
        test_df = df[df["model_name"] == gen]
        train_df = df[df["model_name"] != gen]
        train_ds = downsample(train_df, rng)

        clf = XGBClassifier(**XGB_PARAMS)
        clf.fit(train_ds[FEATURES].values, train_ds["label"].values)
        y_pred = clf.predict(test_df[FEATURES].values)
        y_test = test_df["label"].values

        macro_f1 = f1_score(y_test, y_pred, average="macro")
        per_class = f1_score(y_test, y_pred, average=None, labels=[0, 1, 2])
        results[gen] = {
            "3class_f1": round(float(macro_f1), 4),
            "gen0_f1": round(float(per_class[0]), 4),
            "gen1_f1": round(float(per_class[1]), 4),
            "gen2p_f1": round(float(per_class[2]), 4),
        }
        print(f"  {gen:25s}  macro-F1={macro_f1:.4f}  g0={per_class[0]:.4f}  g1={per_class[1]:.4f}  g2+={per_class[2]:.4f}")

    avg = np.mean([r["3class_f1"] for r in results.values()])
    print(f"  {'AVERAGE':25s}  macro-F1={avg:.4f}")
    return results, round(float(avg), 4)


def logo_binary(df):
    df_bin = df[df["label"] > 0].copy()
    df_bin["bin_label"] = (df_bin["label"] >= 2).astype(int)  # 0=gen-1, 1=gen-2+

    generators = sorted(df_bin["model_name"].unique())
    results = {}
    rng = np.random.RandomState(SEED)

    xgb_bin = dict(n_estimators=200, max_depth=6, learning_rate=0.1,
                   random_state=SEED, eval_metric="logloss",
                   use_label_encoder=False)

    for gen in generators:
        test_df = df_bin[df_bin["model_name"] == gen]
        train_df = df_bin[df_bin["model_name"] != gen]

        min_n = train_df["bin_label"].value_counts().min()
        train_ds = pd.concat([
            train_df[train_df["bin_label"] == 0].sample(n=min_n, random_state=rng, replace=False),
            train_df[train_df["bin_label"] == 1].sample(n=min_n, random_state=rng, replace=False),
        ], ignore_index=True)

        clf = XGBClassifier(**xgb_bin)
        clf.fit(train_ds[FEATURES].values, train_ds["bin_label"].values)
        y_pred = clf.predict(test_df[FEATURES].values)
        y_test = test_df["bin_label"].values

        bin_f1 = f1_score(y_test, y_pred, average="binary", pos_label=1)
        macro_f1 = f1_score(y_test, y_pred, average="macro")
        results[gen] = {
            "binary_f1": round(float(bin_f1), 4),
            "binary_macro_f1": round(float(macro_f1), 4),
        }
        print(f"  {gen:25s}  binary-F1={bin_f1:.4f}  macro={macro_f1:.4f}")

    avg = np.mean([r["binary_f1"] for r in results.values()])
    print(f"  {'AVERAGE':25s}  binary-F1={avg:.4f}")
    return results, round(float(avg), 4)


def main():
    df = load_7gen()

    print("\n=== 7-gen LOGO 3-class ===")
    per_gen_3c, avg_3c = logo_3class(df)

    print("\n=== 7-gen LOGO binary (gen-1 vs gen-2+) ===")
    per_gen_bin, avg_bin = logo_binary(df)

    per_generator = {}
    for gen in sorted(df["model_name"].unique()):
        per_generator[gen] = {
            "3class_f1": per_gen_3c[gen]["3class_f1"],
            "gen0_f1": per_gen_3c[gen]["gen0_f1"],
            "gen1_f1": per_gen_3c[gen]["gen1_f1"],
            "gen2p_f1": per_gen_3c[gen]["gen2p_f1"],
            "binary_f1": per_gen_bin[gen]["binary_f1"],
        }

    instruct_3c = per_gen_3c["qwen3-1.7b-instruct"]["3class_f1"]
    base_3c = per_gen_3c["qwen3-1.7b"]["3class_f1"]

    output = {
        "7gen_logo_avg_f1": avg_3c,
        "7gen_binary_f1": avg_bin,
        "per_generator": per_generator,
        "vs_base_comparison": {
            "instruct_held_out_f1": instruct_3c,
            "base_held_out_f1": base_3c,
            "delta": round(instruct_3c - base_3c, 4),
            "reference_6gen_base_held_out_f1": 0.805,
        },
        "note": "instruct depth-response direction is reversed (diversity increases with depth) vs base (decreases). XGBoost handles both directions.",
    }

    out_path = ROOT / "results" / "p1c_instruct_logo_f1.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"\nSaved: {out_path}")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
