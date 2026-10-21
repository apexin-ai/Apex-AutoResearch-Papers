"""eval_exp054_instruct_llama.py — Within-model CV + Spearman analysis for Llama-3.2-3B Instruct vs Base."""
import json
import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedKFold
from xgboost import XGBClassifier
from sklearn.metrics import f1_score
from scipy import stats

FEATURES = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max",
            "tail_decay", "ttr", "hapax_ratio"]
SEED = 42
N_BOOT = 1000

LLAMA_BASE_RHO = {
    "entropy_mean": -0.6270,
    "entropy_std": -0.1597,
    "entropy_min": -0.3981,
    "entropy_max": +0.0859,
    "tail_decay": -0.0631,
    "ttr": -0.6856,
    "hapax_ratio": -0.6975,
}


def eval_model(csv_path, model_name):
    df = pd.read_csv(csv_path)
    print(f"\n=== {model_name} ({len(df)} records) ===")
    print(f"Depth distribution: {df['depth'].value_counts().sort_index().to_dict()}")

    # 3-class: gen-0 / gen-1 / gen-2+
    df["label_3"] = df["depth"].apply(lambda d: 0 if d == 0 else (1 if d == 1 else 2))
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=SEED)
    X3, y3 = df[FEATURES].values, df["label_3"].values
    preds_3 = np.zeros(len(y3), dtype=int)
    for tr, te in skf.split(X3, y3):
        clf = XGBClassifier(n_estimators=200, max_depth=6, learning_rate=0.1,
                            random_state=SEED, eval_metric="mlogloss")
        clf.fit(X3[tr], y3[tr])
        preds_3[te] = clf.predict(X3[te])
    f1_3 = f1_score(y3, preds_3, average="macro")
    print(f"3-class macro F1: {f1_3:.4f}")

    for c, name in [(0, "gen-0"), (1, "gen-1"), (2, "gen-2+")]:
        f1_c = f1_score(y3 == c, preds_3 == c, average="binary")
        print(f"  {name} F1: {f1_c:.4f}")

    # Binary: gen-1 vs gen-2+
    df_bin = df[df["depth"] >= 1].copy()
    df_bin["label_bin"] = df_bin["depth"].apply(lambda d: 0 if d == 1 else 1)
    Xb, yb = df_bin[FEATURES].values, df_bin["label_bin"].values
    preds_b = np.zeros(len(yb), dtype=int)
    for tr, te in skf.split(Xb, yb):
        clf = XGBClassifier(n_estimators=200, max_depth=6, learning_rate=0.1,
                            random_state=SEED, eval_metric="logloss")
        clf.fit(Xb[tr], yb[tr])
        preds_b[te] = clf.predict(Xb[te])
    f1_b = f1_score(yb, preds_b, average="binary")

    rng = np.random.RandomState(SEED)
    boots = []
    for _ in range(N_BOOT):
        idx = rng.randint(0, len(yb), size=len(yb))
        boots.append(f1_score(yb[idx], preds_b[idx], average="binary"))
    ci_lo, ci_hi = np.percentile(boots, 2.5), np.percentile(boots, 97.5)
    print(f"Binary F1: {f1_b:.4f}  95% CI: [{ci_lo:.4f}, {ci_hi:.4f}]")

    boots_3 = []
    for _ in range(N_BOOT):
        idx = rng.randint(0, len(y3), size=len(y3))
        boots_3.append(f1_score(y3[idx], preds_3[idx], average="macro"))
    ci3_lo, ci3_hi = np.percentile(boots_3, 2.5), np.percentile(boots_3, 97.5)
    print(f"3-class F1 95% CI: [{ci3_lo:.4f}, {ci3_hi:.4f}]")

    # Spearman rho
    print(f"\nSpearman rho (feature vs depth):")
    spearman = {}
    for feat in FEATURES:
        rho, p = stats.spearmanr(df["depth"], df[feat])
        spearman[feat] = {"rho": round(float(rho), 4), "p": float(p)}
        print(f"  {feat:15s}: rho={rho:+.4f}, p={p:.2e}")

    return {
        "model": model_name,
        "n_records": len(df),
        "binary_f1": round(f1_b, 4),
        "binary_ci95": [round(ci_lo, 4), round(ci_hi, 4)],
        "3class_f1": round(f1_3, 4),
        "3class_ci95": [round(ci3_lo, 4), round(ci3_hi, 4)],
        "spearman": spearman,
    }


instruct_result = eval_model("data/features_llama-3.2-3b-instruct.csv", "Llama-3.2-3B-Instruct")

# Load base from 8gen
df_8gen = pd.read_csv("data/features_8gen.csv")
df_base = df_8gen[df_8gen["model_name"] == "llama-3.2-3b"].copy()
df_base.to_csv("/tmp/features_llama_base_tmp.csv", index=False)
base_result = eval_model("/tmp/features_llama_base_tmp.csv", "Llama-3.2-3B-Base")

# Comparison
print("\n" + "=" * 60)
print("=== Comparison: Instruct vs Base ===")
for metric in ["binary_f1", "3class_f1"]:
    delta = instruct_result[metric] - base_result[metric]
    print(f"{metric}: instruct={instruct_result[metric]:.4f}, base={base_result[metric]:.4f}, delta={delta:+.4f}")

# Spearman comparison
print("\nSpearman rho comparison:")
reversals = 0
for feat in FEATURES:
    inst_rho = instruct_result["spearman"][feat]["rho"]
    base_rho = base_result["spearman"][feat]["rho"]
    delta = inst_rho - base_rho
    reversed_dir = (inst_rho > 0) != (base_rho > 0) and abs(base_rho) > 0.05
    if reversed_dir:
        reversals += 1
    marker = " ** REVERSED **" if reversed_dir else ""
    print(f"  {feat:15s}: instruct={inst_rho:+.4f}  base={base_rho:+.4f}  delta={delta:+.4f}{marker}")

print(f"\nDirection reversals: {reversals}/{len(FEATURES)}")

results = {
    "instruct": instruct_result,
    "base": base_result,
    "delta": {
        "binary_f1": round(instruct_result["binary_f1"] - base_result["binary_f1"], 4),
        "3class_f1": round(instruct_result["3class_f1"] - base_result["3class_f1"], 4),
    },
    "direction_reversals": reversals,
}

import os
os.makedirs("results", exist_ok=True)
with open("results/exp054_instruct_llama_eval.json", "w") as f:
    json.dump(results, f, indent=2)
print("\nSaved to results/exp054_instruct_llama_eval.json")
