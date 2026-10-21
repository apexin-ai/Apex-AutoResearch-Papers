import pandas as pd
import numpy as np
import json
from pathlib import Path
from xgboost import XGBClassifier
from sklearn.metrics import f1_score, confusion_matrix, classification_report

FEATURES = ['entropy_mean', 'entropy_std', 'entropy_max', 'entropy_min', 'tail_decay', 'ttr', 'hapax_ratio']

def load_csv_train(path):
    df = pd.read_csv(path)
    # Only rp=1.0 (original 6 generators)
    return df[FEATURES + ['depth']].copy()

def load_jsonl(path):
    records = []
    with open(path) as f:
        for line in f:
            records.append(json.loads(line))
    df = pd.DataFrame(records)
    return df[FEATURES + ['depth']].copy()

def make_label(depth):
    if depth == 0:
        return 0
    elif depth == 1:
        return 1
    else:
        return 2

def evaluate(model, X_test, y_test):
    y_pred = model.predict(X_test)
    
    # 3-class F1
    f1_3class = f1_score(y_test, y_pred, average='macro')
    
    # Binary F1: gen-1 vs gen-2+
    mask_binary = y_test >= 1
    if mask_binary.sum() > 0:
        y_bin_true = (y_test[mask_binary] >= 2).astype(int)
        y_bin_pred = (y_pred[mask_binary] >= 2).astype(int)
        f1_binary = f1_score(y_bin_true, y_bin_pred, average='binary')
    else:
        f1_binary = None
    
    # Per-class F1
    per_class = f1_score(y_test, y_pred, average=None)
    per_class_dict = {f"gen-{i}" if i < 2 else "gen-2+": float(per_class[i]) for i in range(len(per_class))}
    
    # Confusion matrix
    cm = confusion_matrix(y_test, y_pred, labels=[0, 1, 2]).tolist()
    
    return {
        "3class_f1": round(float(f1_3class), 4),
        "binary_f1": round(float(f1_binary), 4) if f1_binary is not None else None,
        "per_class": per_class_dict,
        "confusion_matrix": cm,
        "n_samples": len(y_test),
        "class_distribution": {f"gen-{i}" if i < 2 else "gen-2+": int((y_test == i).sum()) for i in range(3)}
    }

# Load train data
print("Loading train data...")
train_csv = load_csv_train('/root/gen-depth-fingerprint/data/features_all_models.csv')
print(f"  CSV (6 generators): {len(train_csv)} samples")

train_mistral = load_jsonl('/root/gen-depth-fingerprint/data/mistral-7b-v0.3/features_pythia410m.jsonl')
print(f"  Mistral rp=1.0: {len(train_mistral)} samples")

train_all = pd.concat([train_csv, train_mistral], ignore_index=True)
train_all['label'] = train_all['depth'].apply(make_label)
print(f"  Total train: {len(train_all)} samples")
print(f"  Label distribution: {train_all['label'].value_counts().sort_index().to_dict()}")

X_train = train_all[FEATURES].values
y_train = train_all['label'].values

# Train XGBoost
print("\nTraining XGBoost...")
model = XGBClassifier(
    n_estimators=200,
    max_depth=6,
    learning_rate=0.1,
    use_label_encoder=False,
    eval_metric='mlogloss',
    random_state=42
)
model.fit(X_train, y_train)

# Test on Gemma rp=1.0
print("\n--- Test: Gemma-2-2B rp=1.0 (unfiltered) ---")
test_gemma = load_jsonl('/root/gen-depth-fingerprint/data/gemma-2-2b/features_pythia410m.jsonl')
test_gemma['label'] = test_gemma['depth'].apply(make_label)
print(f"  Samples: {len(test_gemma)}")
print(f"  Label distribution: {test_gemma['label'].value_counts().sort_index().to_dict()}")

X_test_gemma = test_gemma[FEATURES].values
y_test_gemma = test_gemma['label'].values
results_gemma = evaluate(model, X_test_gemma, y_test_gemma)
print(f"  3-class F1: {results_gemma['3class_f1']}")
print(f"  Binary F1 (gen-1 vs gen-2+): {results_gemma['binary_f1']}")
print(f"  Per-class: {results_gemma['per_class']}")
print(f"  Confusion matrix:\n    {results_gemma['confusion_matrix']}")

# Test on Llama rp=1.1
print("\n--- Test: Llama-3.2-3B rp=1.1 ---")
test_llama = load_jsonl('/root/gen-depth-fingerprint/data/llama-3.2-3b-rp11/features_pythia410m.jsonl')
test_llama['label'] = test_llama['depth'].apply(make_label)
print(f"  Samples: {len(test_llama)}")
print(f"  Label distribution: {test_llama['label'].value_counts().sort_index().to_dict()}")

X_test_llama = test_llama[FEATURES].values
y_test_llama = test_llama['label'].values
results_llama = evaluate(model, X_test_llama, y_test_llama)
print(f"  3-class F1: {results_llama['3class_f1']}")
print(f"  Binary F1 (gen-1 vs gen-2+): {results_llama['binary_f1']}")
print(f"  Per-class: {results_llama['per_class']}")
print(f"  Confusion matrix:\n    {results_llama['confusion_matrix']}")

# Save results
output = {
    "test_gemma_rp10": results_gemma,
    "test_llama_rp11": results_llama
}

out_path = Path('/root/gen-depth-fingerprint/results/rp_lofo_corrected.json')
out_path.parent.mkdir(parents=True, exist_ok=True)
with open(out_path, 'w') as f:
    json.dump(output, f, indent=2)
print(f"\nResults saved to {out_path}")
