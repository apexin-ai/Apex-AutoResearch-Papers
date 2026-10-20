import json, os
import numpy as np
import pandas as pd
from sklearn.metrics import f1_score
from xgboost import XGBClassifier

FEATURE_COLS = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max",
                "tail_decay", "ttr", "hapax_ratio"]
SEEDS = [42, 123, 456, 789, 1024]

df = pd.read_csv("/root/gen-depth-fingerprint/data/features_all_models.csv")
df["label"] = df["depth"].apply(lambda d: 0 if d == 0 else (1 if d == 1 else 2))

generators = sorted(df["model_name"].unique())
results = {}

for seed in SEEDS:
    fold_f1s = []
    for held_out in generators:
        train = df[df["model_name"] != held_out]
        test = df[df["model_name"] == held_out]
        clf = XGBClassifier(
            n_estimators=200, max_depth=6, learning_rate=0.1,
            subsample=0.8, colsample_bytree=0.8,
            eval_metric="mlogloss", random_state=seed, verbosity=0,
        )
        clf.fit(train[FEATURE_COLS].values, train["label"].values)
        y_pred = clf.predict(test[FEATURE_COLS].values)
        f1 = f1_score(test["label"].values, y_pred, average="macro", zero_division=0)
        fold_f1s.append(round(float(f1), 4))
    avg = round(float(np.mean(fold_f1s)), 4)
    results[seed] = {"per_generator": dict(zip(generators, fold_f1s)), "avg_macro_f1": avg}
    print(f"Seed {seed:>4d}: avg_macro_f1 = {avg:.4f}  ({fold_f1s})")

all_avgs = [r["avg_macro_f1"] for r in results.values()]
mean_f1 = round(float(np.mean(all_avgs)), 4)
std_f1 = round(float(np.std(all_avgs)), 4)
print(f"\nMean+/-Std: {mean_f1:.4f} +/- {std_f1:.4f}")

output = {"seeds": {str(s): results[s] for s in SEEDS},
          "summary": {"mean_macro_f1": mean_f1, "std_macro_f1": std_f1,
                       "n_seeds": len(SEEDS), "n_generators": len(generators),
                       "generators": generators}}
os.makedirs("/root/gen-depth-fingerprint/results", exist_ok=True)
with open("/root/gen-depth-fingerprint/results/multi_seed_stability.json", "w") as f:
    json.dump(output, f, indent=2)
print("Saved to results/multi_seed_stability.json")
