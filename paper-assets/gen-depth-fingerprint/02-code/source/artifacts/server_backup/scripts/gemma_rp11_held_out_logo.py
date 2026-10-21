import json
import pandas as pd
import numpy as np
from xgboost import XGBClassifier
from sklearn.metrics import f1_score, confusion_matrix

FEATURES = ["entropy_mean", "entropy_std", "entropy_max", "entropy_min", "ttr", "hapax_ratio", "tail_decay"]

def depth_to_3class(d):
    if d == 0: return 0
    elif d == 1: return 1
    else: return 2

# --- Load training data ---
# 1) 6-gen CSV
csv_df = pd.read_csv("/root/gen-depth-fingerprint/data/features_all_models.csv")
csv_df = csv_df[FEATURES + ["depth"]].copy()

# 2) Llama-3.2-3B jsonl
llama_rows = []
with open("/root/gen-depth-fingerprint/data/llama-3.2-3b/features_pythia410m.jsonl") as f:
    for line in f:
        llama_rows.append(json.loads(line))
llama_df = pd.DataFrame(llama_rows)[FEATURES + ["depth"]]

# 3) Mistral-7B jsonl
mistral_rows = []
with open("/root/gen-depth-fingerprint/data/mistral-7b-v0.3/features_pythia410m.jsonl") as f:
    for line in f:
        mistral_rows.append(json.loads(line))
mistral_df = pd.DataFrame(mistral_rows)[FEATURES + ["depth"]]

train_df = pd.concat([csv_df, llama_df, mistral_df], ignore_index=True)
print(f"Training set: {len(train_df)} rows")

# --- Load test data ---
test_rows = []
with open("/root/gen-depth-fingerprint/data/gemma-2-2b-rp11/features_pythia410m.jsonl") as f:
    for line in f:
        test_rows.append(json.loads(line))
test_df = pd.DataFrame(test_rows)[FEATURES + ["depth"]]
print(f"Test set: {len(test_df)} rows")

# --- 3-class eval ---
train_df["label3"] = train_df["depth"].apply(depth_to_3class)
test_df["label3"] = test_df["depth"].apply(depth_to_3class)

X_train = train_df[FEATURES].values
y_train_3 = train_df["label3"].values
X_test = test_df[FEATURES].values
y_test_3 = test_df["label3"].values

clf3 = XGBClassifier(n_estimators=200, max_depth=6, random_state=42, use_label_encoder=False, eval_metric="mlogloss")
clf3.fit(X_train, y_train_3)
pred3 = clf3.predict(X_test)

f1_3 = f1_score(y_test_3, pred3, average="macro")
f1_per_3 = f1_score(y_test_3, pred3, average=None)
cm3 = confusion_matrix(y_test_3, pred3, labels=[0,1,2]).tolist()
print(f"3-class macro F1: {f1_3:.4f}, per-class: {f1_per_3}")

# --- Binary eval (gen-1 vs gen-2+) ---
train_bin = train_df[train_df["depth"] >= 1].copy()
test_bin = test_df[test_df["depth"] >= 1].copy()
train_bin["label_bin"] = (train_bin["depth"] >= 2).astype(int)
test_bin["label_bin"] = (test_bin["depth"] >= 2).astype(int)

X_train_b = train_bin[FEATURES].values
y_train_b = train_bin["label_bin"].values
X_test_b = test_bin[FEATURES].values
y_test_b = test_bin["label_bin"].values

clf_b = XGBClassifier(n_estimators=200, max_depth=6, random_state=42, use_label_encoder=False, eval_metric="logloss")
clf_b.fit(X_train_b, y_train_b)
pred_b = clf_b.predict(X_test_b)

f1_b = f1_score(y_test_b, pred_b, average="macro")
f1_per_b = f1_score(y_test_b, pred_b, average=None)
cm_b = confusion_matrix(y_test_b, pred_b, labels=[0,1]).tolist()
print(f"Binary macro F1: {f1_b:.4f}, per-class: {f1_per_b}")

# --- Save results ---
results = {
    "3class": {
        "f1": round(float(f1_3), 4),
        "per_class_f1": {
            "gen0": round(float(f1_per_3[0]), 4),
            "gen1": round(float(f1_per_3[1]), 4),
            "gen2plus": round(float(f1_per_3[2]), 4)
        },
        "confusion_matrix": cm3,
        "n_train": int(len(train_df)),
        "n_test": int(len(test_df))
    },
    "binary": {
        "f1": round(float(f1_b), 4),
        "per_class_f1": {
            "gen1": round(float(f1_per_b[0]), 4),
            "gen2plus": round(float(f1_per_b[1]), 4)
        },
        "confusion_matrix": cm_b,
        "n_train": int(len(train_bin)),
        "n_test": int(len(test_bin))
    },
    "config": {
        "train_generators": 8,
        "test_generator": "gemma-2-2b-rp11",
        "classifier": "XGBoost",
        "n_estimators": 200,
        "max_depth": 6
    }
}

import os
os.makedirs("/root/gen-depth-fingerprint/results", exist_ok=True)
with open("/root/gen-depth-fingerprint/results/gemma_rp11_held_out_logo.json", "w") as f:
    json.dump(results, f, indent=2)

print("\nSaved to results/gemma_rp11_held_out_logo.json")
print(json.dumps(results, indent=2))
