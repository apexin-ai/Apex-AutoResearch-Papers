import json
import numpy as np
import pandas as pd
from xgboost import XGBClassifier
from sklearn.metrics import f1_score, classification_report, confusion_matrix
from pathlib import Path

DATA_DIR = Path("/root/gen-depth-fingerprint/data")
OUT_DIR = Path("/root/gen-depth-fingerprint/results")
OUT_DIR.mkdir(exist_ok=True)

FEATURES = ["entropy_mean", "entropy_std", "entropy_max", "entropy_min", "tail_decay", "ttr", "hapax_ratio"]
CLASS_MAP = {0: 0, 1: 1, 2: 2, 3: 2, 4: 2}

XGB_PARAMS = dict(n_estimators=200, max_depth=6, learning_rate=0.1,
                  random_state=42, eval_metric="mlogloss", verbosity=0)

# Load 6 original generators from CSV
df_csv = pd.read_csv(DATA_DIR / "features_all_models.csv")
df_csv["label"] = df_csv["depth"].map(CLASS_MAP)
df_csv = df_csv.dropna(subset=FEATURES + ["label"])
print(f"CSV (6 generators): {len(df_csv)} rows")

# Load Mistral from JSONL
mistral_rows = []
with open(DATA_DIR / "mistral-7b-v0.3" / "features_pythia410m.jsonl") as f:
    for line in f:
        mistral_rows.append(json.loads(line))
df_mistral = pd.DataFrame(mistral_rows)
df_mistral["label"] = df_mistral["depth"].map(CLASS_MAP)
df_mistral["model_name"] = "mistral-7b-v0.3"
df_mistral = df_mistral.dropna(subset=FEATURES + ["label"])
print(f"Mistral (filtered): {len(df_mistral)} rows")

# Combine train
df_train = pd.concat([df_csv, df_mistral], ignore_index=True)
print(f"Total train: {len(df_train)} rows")
print(f"Train label distribution:\n{df_train['label'].value_counts().sort_index()}")

# Load test: Llama rp=1.1
test_rows = []
with open(DATA_DIR / "llama-3.2-3b-rp11" / "features_pythia410m.jsonl") as f:
    for line in f:
        test_rows.append(json.loads(line))
df_test = pd.DataFrame(test_rows)
df_test["label"] = df_test["depth"].map(CLASS_MAP)
df_test = df_test.dropna(subset=FEATURES + ["label"])
print(f"\nTest (Llama rp=1.1): {len(df_test)} rows")
print(f"Test label distribution:\n{df_test['label'].value_counts().sort_index()}")

# Train XGBoost
X_train = df_train[FEATURES].values
y_train = df_train["label"].values.astype(int)
X_test = df_test[FEATURES].values
y_test = df_test["label"].values.astype(int)

clf = XGBClassifier(**XGB_PARAMS)
clf.fit(X_train, y_train)

# Predict
y_pred = clf.predict(X_test)

# 3-class metrics
f1_3class_macro = f1_score(y_test, y_pred, average="macro")
f1_3class_weighted = f1_score(y_test, y_pred, average="weighted")
f1_per_class = f1_score(y_test, y_pred, average=None).tolist()
cm = confusion_matrix(y_test, y_pred).tolist()

print(f"\n=== 3-class Results ===")
print(f"Macro F1: {f1_3class_macro:.4f}")
print(f"Weighted F1: {f1_3class_weighted:.4f}")
print(f"Per-class F1: gen-0={f1_per_class[0]:.4f}, gen-1={f1_per_class[1]:.4f}, gen-2+={f1_per_class[2]:.4f}")
print(f"Confusion matrix:\n{np.array(cm)}")
print(classification_report(y_test, y_pred, target_names=["gen-0", "gen-1", "gen-2+"]))

# Binary: gen-1 vs gen-2+
mask_binary = y_test > 0
y_test_bin = (y_test[mask_binary] >= 2).astype(int)  # 0=gen-1, 1=gen-2+
y_pred_bin = (y_pred[mask_binary] >= 2).astype(int)
f1_binary = f1_score(y_test_bin, y_pred_bin, average="macro")
f1_binary_per = f1_score(y_test_bin, y_pred_bin, average=None).tolist()
cm_binary = confusion_matrix(y_test_bin, y_pred_bin).tolist()

print(f"\n=== Binary (gen-1 vs gen-2+) ===")
print(f"Macro F1: {f1_binary:.4f}")
print(f"Per-class F1: gen-1={f1_binary_per[0]:.4f}, gen-2+={f1_binary_per[1]:.4f}")
print(f"Confusion matrix:\n{np.array(cm_binary)}")

# Save results
results = {
    "experiment": "rp_lofo_preliminary",
    "description": "Train on 7 generators (rp=1.0), test on Llama rp=1.1",
    "train_generators": ["pythia-2.8b", "pythia-1b", "olmo-2-1b", "qwen3-0.6b", "qwen3-1.7b", "qwen3-8b", "mistral-7b-v0.3"],
    "test_generator": "llama-3.2-3b-rp11",
    "train_size": len(df_train),
    "test_size": len(df_test),
    "three_class": {
        "macro_f1": round(f1_3class_macro, 4),
        "weighted_f1": round(f1_3class_weighted, 4),
        "per_class_f1": {"gen-0": round(f1_per_class[0], 4), "gen-1": round(f1_per_class[1], 4), "gen-2+": round(f1_per_class[2], 4)},
        "confusion_matrix": cm,
        "labels": ["gen-0", "gen-1", "gen-2+"]
    },
    "binary_gen1_vs_gen2plus": {
        "macro_f1": round(f1_binary, 4),
        "per_class_f1": {"gen-1": round(f1_binary_per[0], 4), "gen-2+": round(f1_binary_per[1], 4)},
        "confusion_matrix": cm_binary,
        "labels": ["gen-1", "gen-2+"]
    },
    "gate_d036": {
        "criterion": "binary_f1 > 0.70",
        "binary_f1": round(f1_binary, 4),
        "pass": f1_binary > 0.70
    },
    "xgb_params": XGB_PARAMS,
    "features": FEATURES
}

with open(OUT_DIR / "rp_lofo_preliminary.json", "w") as f:
    json.dump(results, f, indent=2)

print(f"\nResults saved to {OUT_DIR / 'rp_lofo_preliminary.json'}")
print(f"\n=== Gate D036: binary F1={f1_binary:.4f}, pass={'YES' if f1_binary > 0.70 else 'NO'} ===")
