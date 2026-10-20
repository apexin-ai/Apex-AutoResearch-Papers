import json
import numpy as np
import pandas as pd
from sklearn.ensemble import HistGradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import f1_score, confusion_matrix, accuracy_score
import warnings, os, sys
warnings.filterwarnings("ignore")
sys.stdout.reconfigure(line_buffering=True)

DATA_PATH = "data/features_all_models.csv"
FEATURES = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max",
            "tail_decay", "ttr", "hapax_ratio"]
OUT_PATH = "results/finer_ordinal_results.json"

def frank_hall_predict(X_train, y_train, X_test, n_classes=5):
    probs = np.zeros((len(X_test), n_classes))
    cum_probs = []
    for k in range(n_classes - 1):
        y_bin = (y_train > k).astype(int)
        clf = LogisticRegression(max_iter=1000, C=1.0)
        clf.fit(X_train, y_bin)
        p = clf.predict_proba(X_test)[:, 1]
        cum_probs.append(p)
    for k in range(n_classes):
        if k == 0:
            probs[:, k] = 1 - cum_probs[0]
        elif k == n_classes - 1:
            probs[:, k] = cum_probs[k - 1]
        else:
            probs[:, k] = cum_probs[k - 1] - cum_probs[k]
    probs = np.clip(probs, 0, 1)
    row_sums = probs.sum(axis=1, keepdims=True)
    row_sums[row_sums == 0] = 1
    probs /= row_sums
    return np.argmax(probs, axis=1)

def mae_ordinal(y_true, y_pred):
    return np.mean(np.abs(y_true - y_pred))

def bootstrap_ci(y_true, y_pred, metric_fn, n_boot=2000, ci=0.95):
    rng = np.random.RandomState(42)
    scores = []
    n = len(y_true)
    for _ in range(n_boot):
        idx = rng.randint(0, n, n)
        scores.append(metric_fn(y_true[idx], y_pred[idx]))
    lo = np.percentile(scores, (1 - ci) / 2 * 100)
    hi = np.percentile(scores, (1 + ci) / 2 * 100)
    return float(np.mean(scores)), float(lo), float(hi)

def logo_cv(df, model_name, n_classes=5, use_frank_hall=False):
    generators = df["model_name"].unique()
    all_y_true, all_y_pred = [], []
    per_gen_results = {}
    for gen in generators:
        test_mask = df["model_name"] == gen
        train_mask = ~test_mask
        X_train = df.loc[train_mask, FEATURES].values
        y_train = df.loc[train_mask, "depth"].values
        X_test = df.loc[test_mask, FEATURES].values
        y_test = df.loc[test_mask, "depth"].values
        scaler = StandardScaler()
        X_train_s = scaler.fit_transform(X_train)
        X_test_s = scaler.transform(X_test)
        if use_frank_hall:
            y_pred = frank_hall_predict(X_train_s, y_train, X_test_s, n_classes)
        else:
            if model_name == "HGBT":
                clf = HistGradientBoostingClassifier(
                    max_iter=200, max_depth=4, learning_rate=0.1, random_state=42
                )
                clf.fit(X_train, y_train)
            elif model_name == "RF":
                clf = RandomForestClassifier(
                    n_estimators=200, max_depth=8, random_state=42, n_jobs=-1
                )
                clf.fit(X_train, y_train)
            elif model_name == "LR":
                clf = LogisticRegression(max_iter=1000, C=1.0, random_state=42)
                clf.fit(X_train_s, y_train)
            else:
                raise ValueError(f"Unknown model: {model_name}")
            if model_name == "LR":
                y_pred = clf.predict(X_test_s)
            else:
                y_pred = clf.predict(X_test)
        all_y_true.extend(y_test)
        all_y_pred.extend(y_pred)
        per_gen_results[gen] = {
            "f1_macro": round(float(f1_score(y_test, y_pred, average="macro", zero_division=0)), 4),
            "accuracy": round(float(accuracy_score(y_test, y_pred)), 4),
            "mae": round(float(mae_ordinal(y_test, y_pred)), 4),
            "n_test": int(len(y_test)),
        }
        print(f"  fold {gen}: F1={per_gen_results[gen]['f1_macro']:.4f} acc={per_gen_results[gen]['accuracy']:.4f}")
    all_y_true = np.array(all_y_true)
    all_y_pred = np.array(all_y_pred)
    macro_f1 = float(f1_score(all_y_true, all_y_pred, average="macro", zero_division=0))
    _, f1_lo, f1_hi = bootstrap_ci(
        all_y_true, all_y_pred,
        lambda yt, yp: f1_score(yt, yp, average="macro", zero_division=0)
    )
    per_class_f1 = f1_score(all_y_true, all_y_pred, average=None, zero_division=0)
    cm = confusion_matrix(all_y_true, all_y_pred, labels=list(range(n_classes)))
    return {
        "macro_f1": round(macro_f1, 4),
        "macro_f1_95ci": [round(f1_lo, 4), round(f1_hi, 4)],
        "accuracy": round(float(accuracy_score(all_y_true, all_y_pred)), 4),
        "mae": round(float(mae_ordinal(all_y_true, all_y_pred)), 4),
        "per_class_f1": {f"depth_{i}": round(float(per_class_f1[i]), 4) for i in range(n_classes)},
        "confusion_matrix": cm.tolist(),
        "per_generator": per_gen_results,
    }

def run_3class(df):
    df3 = df.copy()
    df3["depth_3class"] = df3["depth"].clip(upper=2)
    generators = df3["model_name"].unique()
    all_y_true, all_y_pred = [], []
    for gen in generators:
        test_mask = df3["model_name"] == gen
        train_mask = ~test_mask
        X_train = df3.loc[train_mask, FEATURES].values
        y_train = df3.loc[train_mask, "depth_3class"].values
        X_test = df3.loc[test_mask, FEATURES].values
        y_test = df3.loc[test_mask, "depth_3class"].values
        clf = HistGradientBoostingClassifier(
            max_iter=200, max_depth=4, learning_rate=0.1, random_state=42
        )
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        all_y_true.extend(y_test)
        all_y_pred.extend(y_pred)
    all_y_true = np.array(all_y_true)
    all_y_pred = np.array(all_y_pred)
    macro_f1 = float(f1_score(all_y_true, all_y_pred, average="macro", zero_division=0))
    _, f1_lo, f1_hi = bootstrap_ci(
        all_y_true, all_y_pred,
        lambda yt, yp: f1_score(yt, yp, average="macro", zero_division=0)
    )
    per_class_f1 = f1_score(all_y_true, all_y_pred, average=None, zero_division=0)
    return {
        "macro_f1": round(macro_f1, 4),
        "macro_f1_95ci": [round(f1_lo, 4), round(f1_hi, 4)],
        "accuracy": round(float(accuracy_score(all_y_true, all_y_pred)), 4),
        "per_class_f1": {
            "gen-0": round(float(per_class_f1[0]), 4),
            "gen-1": round(float(per_class_f1[1]), 4),
            "gen-2+": round(float(per_class_f1[2]), 4),
        },
    }

def main():
    os.makedirs("results", exist_ok=True)
    df = pd.read_csv(DATA_PATH)
    print(f"Data: {len(df)} samples, {df['model_name'].nunique()} generators")
    print(f"Depth distribution:\n{df['depth'].value_counts().sort_index()}\n")
    results = {}
    models_5class = [
        ("HGBT_5class", "HGBT", False),
        ("RF_5class", "RF", False),
        ("LR_5class", "LR", False),
        ("FrankHall_5class", None, True),
    ]
    for name, model_name, use_fh in models_5class:
        print(f"Running {name}...")
        r = logo_cv(df, model_name, n_classes=5, use_frank_hall=use_fh)
        results[name] = r
        print(f"  => macro-F1: {r['macro_f1']:.4f} [{r['macro_f1_95ci'][0]:.4f}, {r['macro_f1_95ci'][1]:.4f}]")
        print(f"     accuracy: {r['accuracy']:.4f}, MAE: {r['mae']:.4f}")
        print(f"     per-class F1: {r['per_class_f1']}\n")
    print("Running 3-class HGBT comparison...")
    results["HGBT_3class"] = run_3class(df)
    r3 = results["HGBT_3class"]
    print(f"  => macro-F1: {r3['macro_f1']:.4f} [{r3['macro_f1_95ci'][0]:.4f}, {r3['macro_f1_95ci'][1]:.4f}]")
    print(f"     per-class F1: {r3['per_class_f1']}\n")
    print("=" * 60)
    print("SUMMARY: 5-class vs 3-class")
    print(f"  HGBT 5-class macro-F1: {results['HGBT_5class']['macro_f1']:.4f}")
    print(f"  HGBT 3-class macro-F1: {results['HGBT_3class']['macro_f1']:.4f}")
    delta = results['HGBT_5class']['macro_f1'] - results['HGBT_3class']['macro_f1']
    print(f"  Delta: {delta:+.4f}")
    best_5class = max(
        [(k, v["macro_f1"]) for k, v in results.items() if "5class" in k],
        key=lambda x: x[1]
    )
    print(f"  Best 5-class model: {best_5class[0]} (F1={best_5class[1]:.4f})")
    with open(OUT_PATH, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {OUT_PATH}")

if __name__ == "__main__":
    main()
