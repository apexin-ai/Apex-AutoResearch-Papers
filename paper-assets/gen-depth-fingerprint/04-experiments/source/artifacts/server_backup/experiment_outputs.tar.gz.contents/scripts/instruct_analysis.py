"""Unified instruct vs base analysis: Spearman rho, CV F1, Cohen's d, direction reversals."""
import json, os, sys
import numpy as np
import pandas as pd
from scipy import stats
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import f1_score
from xgboost import XGBClassifier

FEATURES = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max",
            "tail_decay", "ttr", "hapax_ratio"]
SEED = 42
N_BOOT = 1000
N_FOLDS = 5

MODEL_PAIRS = [
    {
        "name": "Qwen3-1.7B",
        "base_csv": "data/features_qwen3-1.7b.csv",
        "instruct_csv": "data/features_qwen3-1.7b-instruct.csv",
        "base_filter": None,
    },
    {
        "name": "OLMo-2-1B",
        "base_csv": "data/features_olmo-2-1b.csv",
        "instruct_csv": "data/features_olmo-2-0425-1b-instruct.csv",
        "base_filter": None,
    },
    {
        "name": "Llama-3.2-3B",
        "base_csv": "data/features_8gen.csv",
        "instruct_csv": "data/features_llama-3.2-3b-instruct.csv",
        "base_filter": "llama-3.2-3b",
    },
]


def load_df(csv_path, model_filter=None):
    df = pd.read_csv(csv_path)
    if model_filter:
        df = df[df["model_name"] == model_filter].copy()
    return df


def compute_spearman(df):
    result = {}
    for feat in FEATURES:
        rho, p = stats.spearmanr(df["depth"], df[feat])
        result[feat] = {"rho": round(float(rho), 4), "p": float(p)}
    return result


def compute_cv_f1(df):
    skf = StratifiedKFold(n_splits=N_FOLDS, shuffle=True, random_state=SEED)
    rng = np.random.RandomState(SEED)

    # 3-class: gen-0 / gen-1 / gen-2+
    df["label_3"] = df["depth"].apply(lambda d: 0 if d == 0 else (1 if d == 1 else 2))
    X3, y3 = df[FEATURES].values, df["label_3"].values
    preds_3 = np.zeros(len(y3), dtype=int)
    for tr, te in skf.split(X3, y3):
        clf = XGBClassifier(n_estimators=200, max_depth=6, learning_rate=0.1,
                            random_state=SEED, eval_metric="mlogloss")
        clf.fit(X3[tr], y3[tr])
        preds_3[te] = clf.predict(X3[te])
    f1_3 = f1_score(y3, preds_3, average="macro")
    boots_3 = [f1_score(y3[idx], preds_3[idx], average="macro")
               for idx in (rng.randint(0, len(y3), len(y3)) for _ in range(N_BOOT))]
    ci3 = [round(np.percentile(boots_3, 2.5), 4), round(np.percentile(boots_3, 97.5), 4)]

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
    boots_b = [f1_score(yb[idx], preds_b[idx], average="binary")
               for idx in (rng.randint(0, len(yb), len(yb)) for _ in range(N_BOOT))]
    ci_b = [round(np.percentile(boots_b, 2.5), 4), round(np.percentile(boots_b, 97.5), 4)]

    return {
        "binary_f1": round(f1_b, 4), "binary_ci95": ci_b,
        "3class_f1": round(f1_3, 4), "3class_ci95": ci3,
    }


def compute_cohens_d(df):
    """Cohen's d for gen-1 vs gen-2+ on each feature."""
    g1 = df[df["depth"] == 1]
    g2 = df[df["depth"] >= 2]
    result = {}
    for feat in FEATURES:
        m1, m2 = g1[feat].mean(), g2[feat].mean()
        s1, s2 = g1[feat].std(ddof=1), g2[feat].std(ddof=1)
        n1, n2 = len(g1), len(g2)
        pooled_std = np.sqrt(((n1 - 1) * s1**2 + (n2 - 1) * s2**2) / (n1 + n2 - 2))
        d = (m1 - m2) / pooled_std if pooled_std > 0 else 0.0
        result[feat] = round(float(d), 4)
    return result


def count_reversals(base_rho, inst_rho):
    reversals = []
    for feat in FEATURES:
        b = base_rho[feat]["rho"]
        i = inst_rho[feat]["rho"]
        if (b > 0) != (i > 0) and abs(b) > 0.05:
            reversals.append(feat)
    return reversals


def analyze_pair(pair):
    name = pair["name"]
    print(f"\n{'='*60}")
    print(f"  {name}")
    print(f"{'='*60}")

    df_base = load_df(pair["base_csv"], pair["base_filter"])
    df_inst = load_df(pair["instruct_csv"])
    print(f"Base: {len(df_base)} records, Instruct: {len(df_inst)} records")

    base_rho = compute_spearman(df_base)
    inst_rho = compute_spearman(df_inst)

    print(f"\nSpearman rho (feature vs depth):")
    print(f"  {'Feature':15s}  {'Base':>8s}  {'Instruct':>8s}  {'Delta':>8s}  Reversed?")
    for feat in FEATURES:
        b, i = base_rho[feat]["rho"], inst_rho[feat]["rho"]
        rev = "YES" if (b > 0) != (i > 0) and abs(b) > 0.05 else ""
        print(f"  {feat:15s}  {b:+8.4f}  {i:+8.4f}  {i-b:+8.4f}  {rev}")

    reversals = count_reversals(base_rho, inst_rho)
    print(f"\nDirection reversals: {len(reversals)}/{len(FEATURES)}: {reversals}")

    print("\nComputing CV F1 (base)...")
    base_cv = compute_cv_f1(df_base.copy())
    print(f"  Binary F1: {base_cv['binary_f1']:.4f} {base_cv['binary_ci95']}")
    print(f"  3-class F1: {base_cv['3class_f1']:.4f} {base_cv['3class_ci95']}")

    print("Computing CV F1 (instruct)...")
    inst_cv = compute_cv_f1(df_inst.copy())
    print(f"  Binary F1: {inst_cv['binary_f1']:.4f} {inst_cv['binary_ci95']}")
    print(f"  3-class F1: {inst_cv['3class_f1']:.4f} {inst_cv['3class_ci95']}")

    base_d = compute_cohens_d(df_base)
    inst_d = compute_cohens_d(df_inst)
    print(f"\nCohen's d (gen-1 vs gen-2+):")
    print(f"  {'Feature':15s}  {'Base':>8s}  {'Instruct':>8s}")
    for feat in FEATURES:
        print(f"  {feat:15s}  {base_d[feat]:+8.4f}  {inst_d[feat]:+8.4f}")

    return {
        "model": name,
        "base": {
            "n_records": len(df_base),
            "spearman": base_rho,
            "cohens_d": base_d,
            **base_cv,
        },
        "instruct": {
            "n_records": len(df_inst),
            "spearman": inst_rho,
            "cohens_d": inst_d,
            **inst_cv,
        },
        "delta": {
            "binary_f1": round(inst_cv["binary_f1"] - base_cv["binary_f1"], 4),
            "3class_f1": round(inst_cv["3class_f1"] - base_cv["3class_f1"], 4),
        },
        "direction_reversals": reversals,
        "n_reversals": len(reversals),
    }


if __name__ == "__main__":
    os.chdir("/root/gen-depth-fingerprint")
    all_results = {}
    for pair in MODEL_PAIRS:
        res = analyze_pair(pair)
        all_results[pair["name"]] = res

    # Summary table
    print(f"\n\n{'='*120}")
    print("SUMMARY TABLE")
    print(f"{'='*120}")
    header = f"{'Model':15s} {'Type':9s} {'Bin F1':>8s} {'3cl F1':>8s} {'ent_mean':>9s} {'ent_std':>9s} {'hapax':>9s} {'ttr':>9s} {'#rev':>5s}"
    print(header)
    print("-" * len(header))
    for name, res in all_results.items():
        for typ, key in [("base", "base"), ("instruct", "instruct")]:
            r = res[key]
            sp = r["spearman"]
            n_rev = res["n_reversals"] if typ == "instruct" else 0
            print(f"{name:15s} {typ:9s} {r['binary_f1']:8.4f} {r['3class_f1']:8.4f} "
                  f"{sp['entropy_mean']['rho']:+9.4f} {sp['entropy_std']['rho']:+9.4f} "
                  f"{sp['hapax_ratio']['rho']:+9.4f} {sp['ttr']['rho']:+9.4f} {n_rev:5d}")

    out_path = "results/instruct_analysis_summary.json"
    os.makedirs("results", exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\nSaved to {out_path}")
