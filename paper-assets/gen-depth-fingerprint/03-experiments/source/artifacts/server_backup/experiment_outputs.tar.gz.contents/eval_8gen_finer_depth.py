"""
8-gen 5-class finer depth LOGO experiment.
Compares 5-class (gen-0/1/2/3/4) vs 3-class (gen-0/1/2+) on all 8 generators.
"""
import json, os, sys
import numpy as np
import pandas as pd
from xgboost import XGBClassifier
from sklearn.metrics import f1_score, confusion_matrix

sys.stdout.reconfigure(line_buffering=True)

SEED = 42
FEATURES = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max",
            "tail_decay", "ttr", "hapax_ratio"]
XGB_PARAMS = dict(n_estimators=200, max_depth=6, learning_rate=0.1,
                  random_state=SEED, eval_metric="mlogloss",
                  use_label_encoder=False)

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(ROOT, "data")
RESULTS_DIR = os.path.join(ROOT, "results")


def load_8gen():
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


def bootstrap_f1(y_true, y_pred, n_boot=1000, seed=SEED):
    rng = np.random.RandomState(seed)
    n = len(y_true)
    scores = []
    for _ in range(n_boot):
        idx = rng.randint(0, n, size=n)
        yt, yp = y_true[idx], y_pred[idx]
        if len(np.unique(yt)) < 2:
            continue
        scores.append(f1_score(yt, yp, average="macro", zero_division=0))
    arr = np.array(scores)
    return float(np.percentile(arr, 2.5)), float(np.percentile(arr, 97.5))


def logo_5class(df):
    generators = sorted(df["model_name"].unique())
    rng = np.random.RandomState(SEED)
    per_gen = {}
    all_y_true, all_y_pred = [], []
    # For per-gen confusion matrices (to average later)
    n_classes = 5
    cm_sum = np.zeros((n_classes, n_classes), dtype=float)

    print("=== 5-class LOGO (gen-0/1/2/3/4) ===")
    for gen in generators:
        test_df = df[df["model_name"] == gen]
        train_df = df[df["model_name"] != gen]
        train_ds = downsample(train_df, "depth", rng)

        clf = XGBClassifier(**XGB_PARAMS)
        clf.fit(train_ds[FEATURES].values, train_ds["depth"].values)
        y_pred = clf.predict(test_df[FEATURES].values)
        y_test = test_df["depth"].values

        macro_f1 = f1_score(y_test, y_pred, average="macro", zero_division=0)
        per_gen[gen] = round(float(macro_f1), 4)
        all_y_true.extend(y_test)
        all_y_pred.extend(y_pred)

        cm = confusion_matrix(y_test, y_pred, labels=list(range(n_classes)))
        # Row-normalize for this fold
        row_sums = cm.sum(axis=1, keepdims=True)
        row_sums[row_sums == 0] = 1
        cm_norm = cm / row_sums
        cm_sum += cm_norm

        print(f"  {gen:20s}  F1={macro_f1:.4f}  n={len(test_df)}")

    all_y_true = np.array(all_y_true)
    all_y_pred = np.array(all_y_pred)

    avg_f1 = round(float(np.mean(list(per_gen.values()))), 4)
    ci_lo, ci_hi = bootstrap_f1(all_y_true, all_y_pred)

    per_class = f1_score(all_y_true, all_y_pred, average=None,
                         labels=list(range(n_classes)), zero_division=0)
    per_class_dict = {f"gen{i}": round(float(per_class[i]), 4) for i in range(n_classes)}

    cm_avg = cm_sum / len(generators)
    cm_avg = np.round(cm_avg, 2).tolist()

    print(f"  {'AVERAGE':20s}  F1={avg_f1:.4f}  95%CI=[{ci_lo:.4f}, {ci_hi:.4f}]")
    print(f"  Per-class F1: {per_class_dict}")

    return {
        "logo_avg_f1": avg_f1,
        "ci95": [round(ci_lo, 4), round(ci_hi, 4)],
        "per_gen": per_gen,
        "per_class_f1": per_class_dict,
        "confusion_matrix_avg": cm_avg,
    }


def logo_3class(df):
    df = df.copy()
    df["label"] = df["depth"].clip(upper=2)
    generators = sorted(df["model_name"].unique())
    rng = np.random.RandomState(SEED)
    per_gen = {}
    all_y_true, all_y_pred = [], []

    print("\n=== 3-class LOGO (gen-0/1/2+) ===")
    for gen in generators:
        test_df = df[df["model_name"] == gen]
        train_df = df[df["model_name"] != gen]
        train_ds = downsample(train_df, "label", rng)

        clf = XGBClassifier(**XGB_PARAMS)
        clf.fit(train_ds[FEATURES].values, train_ds["label"].values)
        y_pred = clf.predict(test_df[FEATURES].values)
        y_test = test_df["label"].values

        macro_f1 = f1_score(y_test, y_pred, average="macro", zero_division=0)
        per_gen[gen] = round(float(macro_f1), 4)
        all_y_true.extend(y_test)
        all_y_pred.extend(y_pred)
        print(f"  {gen:20s}  F1={macro_f1:.4f}  n={len(test_df)}")

    all_y_true = np.array(all_y_true)
    all_y_pred = np.array(all_y_pred)

    avg_f1 = round(float(np.mean(list(per_gen.values()))), 4)
    ci_lo, ci_hi = bootstrap_f1(all_y_true, all_y_pred)
    print(f"  {'AVERAGE':20s}  F1={avg_f1:.4f}  95%CI=[{ci_lo:.4f}, {ci_hi:.4f}]")

    return {
        "logo_avg_f1": avg_f1,
        "ci95": [round(ci_lo, 4), round(ci_hi, 4)],
    }


def main():
    os.makedirs(RESULTS_DIR, exist_ok=True)
    df = load_8gen()
    print(f"Loaded {len(df)} rows, {df['model_name'].nunique()} generators")
    print(f"Depth distribution:\n{df['depth'].value_counts().sort_index()}\n")
    for gen in sorted(df["model_name"].unique()):
        sub = df[df["model_name"] == gen]
        depths = sorted(sub["depth"].unique())
        print(f"  {gen:20s}  n={len(sub):5d}  depths={depths}")
    print()

    res_5 = logo_5class(df)
    res_3 = logo_3class(df)

    delta = round(res_5["logo_avg_f1"] - res_3["logo_avg_f1"], 4)

    output = {
        "5class": res_5,
        "3class_control": res_3,
        "delta_5class_vs_3class": delta,
        "config": {
            "n_generators": int(df["model_name"].nunique()),
            "n_features": len(FEATURES),
            "features": FEATURES,
            "xgb_params": {k: v for k, v in XGB_PARAMS.items() if k != "use_label_encoder"},
            "bootstrap_B": 1000,
            "downsampling": "per-class balance in train set",
        },
    }

    out_path = os.path.join(RESULTS_DIR, "8gen_finer_depth.json")
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"\nResults saved to {out_path}")

    print(f"\n{'='*60}")
    print(f"SUMMARY")
    print(f"  5-class avg F1: {res_5['logo_avg_f1']:.4f}  CI={res_5['ci95']}")
    print(f"  3-class avg F1: {res_3['logo_avg_f1']:.4f}  CI={res_3['ci95']}")
    print(f"  Delta (5c - 3c): {delta:+.4f}")
    print(f"  Per-class F1: {res_5['per_class_f1']}")


if __name__ == "__main__":
    main()
