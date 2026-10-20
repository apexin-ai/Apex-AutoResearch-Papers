"""Supplement rp_lofo_results.json with Test B per_class and confusion_matrix."""
import json
from collections import Counter
from pathlib import Path
import numpy as np
import pandas as pd
from xgboost import XGBClassifier
from sklearn.metrics import f1_score, confusion_matrix

DATA_DIR = Path("/root/gen-depth-fingerprint/data")
RESULTS = Path("/root/gen-depth-fingerprint/results")

FEATURES = ["entropy_mean", "entropy_std", "entropy_max", "entropy_min", "tail_decay", "ttr", "hapax_ratio"]
CLASS_MAP = {0: 0, 1: 1, 2: 2, 3: 2, 4: 2}
XGB_PARAMS = dict(n_estimators=200, max_depth=6, learning_rate=0.1,
                  random_state=42, eval_metric="mlogloss", verbosity=0)


def compute_repeated_4gram_ratio(text):
    words = text.lower().split()
    if len(words) < 4:
        return 0.0
    ngrams = [tuple(words[i:i+4]) for i in range(len(words) - 3)]
    counter = Counter(ngrams)
    repeated = sum(c - 1 for c in counter.values() if c > 1)
    return repeated / len(ngrams)


# Load train data (7 generators, same as rp_lofo)
df_csv = pd.read_csv(DATA_DIR / "features_all_models.csv")
df_csv["label"] = df_csv["depth"].map(CLASS_MAP)

mistral_rows = []
with open(DATA_DIR / "mistral-7b-v0.3" / "features_pythia410m.jsonl") as f:
    for line in f:
        mistral_rows.append(json.loads(line))
df_mistral = pd.DataFrame(mistral_rows)
df_mistral["label"] = df_mistral["depth"].map(CLASS_MAP)
df_mistral["model_name"] = "mistral-7b-v0.3"

df_train = pd.concat([df_csv, df_mistral], ignore_index=True)
print(f"Train: {len(df_train)} rows")

# Load test: Llama rp=1.0 (unfiltered features)
llama_feat_rows = []
with open(DATA_DIR / "llama-3.2-3b" / "features_pythia410m.jsonl") as f:
    for line in f:
        llama_feat_rows.append(json.loads(line))
df_llama = pd.DataFrame(llama_feat_rows)
df_llama["label"] = df_llama["depth"].map(CLASS_MAP)
df_llama["model_name"] = "llama-3.2-3b"
print(f"Llama rp=1.0 total: {len(df_llama)} rows")

# Filter: repeated_4gram_ratio <= 0.5
llama_gens = []
with open(DATA_DIR / "llama-3.2-3b" / "generations_shard0.jsonl") as f:
    for line in f:
        if line.strip():
            llama_gens.append(json.loads(line))

keep_mask = np.array([compute_repeated_4gram_ratio(r["text"]) <= 0.5 for r in llama_gens])
df_llama_filtered = df_llama[keep_mask].copy()
print(f"Llama rp=1.0 filtered: {len(df_llama_filtered)} rows (kept {keep_mask.sum()}/{len(keep_mask)})")

# Train
X_train = df_train[FEATURES].values
y_train = df_train["label"].values.astype(int)

clf = XGBClassifier(**XGB_PARAMS)
clf.fit(X_train, y_train)

# Predict on filtered Llama rp=1.0
X_test = df_llama_filtered[FEATURES].values
y_test = df_llama_filtered["label"].values.astype(int)
y_pred = clf.predict(X_test)

# 3-class
f1_3class = f1_score(y_test, y_pred, average="macro")
f1_per_class = f1_score(y_test, y_pred, average=None, labels=[0, 1, 2])
cm = confusion_matrix(y_test, y_pred, labels=[0, 1, 2]).tolist()

per_class = {}
for i, lbl in enumerate(["gen-0", "gen-1", "gen-2+"]):
    mask = y_test == i
    n = mask.sum()
    acc = (y_pred[mask] == i).sum() / n if n > 0 else 0
    per_class[lbl] = {"f1": round(float(f1_per_class[i]), 4), "accuracy": round(float(acc), 4), "n": int(n)}

# Binary
mask_bin = y_test > 0
y_test_bin = (y_test[mask_bin] >= 2).astype(int)
y_pred_bin = (y_pred[mask_bin] >= 2).astype(int)
f1_binary = f1_score(y_test_bin, y_pred_bin, average="macro")
f1_bin_per = f1_score(y_test_bin, y_pred_bin, average=None)
cm_bin = confusion_matrix(y_test_bin, y_pred_bin).tolist()

print(f"\nTest B (Llama rp=1.0 filtered):")
print(f"  3-class macro F1: {f1_3class:.4f}")
print(f"  Per-class F1: gen-0={f1_per_class[0]:.4f}, gen-1={f1_per_class[1]:.4f}, gen-2+={f1_per_class[2]:.4f}")
print(f"  Binary macro F1: {f1_binary:.4f}")
print(f"  Confusion matrix (3-class): {cm}")

# Update rp_lofo_results.json
existing = json.load(open(RESULTS / "rp_lofo_results.json"))
existing["test_B_llama_rp10_filtered"]["per_class"] = per_class
existing["test_B_llama_rp10_filtered"]["confusion_matrix"] = cm
existing["test_B_llama_rp10_filtered"]["3class_f1"] = round(float(f1_3class), 4)
existing["test_B_llama_rp10_filtered"]["binary_f1"] = round(float(f1_binary), 4)
existing["test_B_llama_rp10_filtered"]["binary_per_class"] = {
    "gen-1": round(float(f1_bin_per[0]), 4),
    "gen-2+": round(float(f1_bin_per[1]), 4),
}
existing["test_B_llama_rp10_filtered"]["binary_confusion_matrix"] = cm_bin

# Also add labels to Test A confusion matrix
existing["test_A_llama_rp11"]["labels"] = ["gen-0", "gen-1", "gen-2+"]
existing["test_B_llama_rp10_filtered"]["labels"] = ["gen-0", "gen-1", "gen-2+"]

with open(RESULTS / "rp_lofo_results.json", "w") as f:
    json.dump(existing, f, indent=2, ensure_ascii=False)
print(f"\nUpdated: {RESULTS / 'rp_lofo_results.json'}")
