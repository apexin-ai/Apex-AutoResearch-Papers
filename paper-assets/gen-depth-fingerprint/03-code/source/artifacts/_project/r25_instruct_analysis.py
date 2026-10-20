"""
r25_instruct_analysis.py — R25 review response: instruct retrain + feature ablation.

Task 1: Instruct model retrain (classification recovery, DDR structure, cross-condition transfer)
Task 2: Feature ablation supplement (3 configurations on 8-gen base data)

All CPU, XGBoost-based, seconds to run.
"""

import numpy as np
import pandas as pd
from scipy import stats
from xgboost import XGBClassifier
from sklearn.metrics import f1_score
from sklearn.model_selection import StratifiedKFold
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from pathlib import Path

SEED = 42
FEATURES = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max",
            "tail_decay", "ttr", "hapax_ratio"]

XGB_PARAMS = dict(n_estimators=200, max_depth=6, learning_rate=0.1,
                  random_state=SEED, eval_metric="mlogloss",
                  use_label_encoder=False)

CLASS_MAP_3 = {0: 0, 1: 1, 2: 2, 3: 2, 4: 2}

DATA_DIR = Path(__file__).parent / "supplement" / "data"

INSTRUCT_MODELS = {
    "olmo-2-0425-1b-instruct": "olmo-2-1b",
    "qwen3-1.7b-instruct": "qwen3-1.7b",
    "qwen3-0.6b-instruct": "qwen3-0.6b",
}


def load_instruct(name):
    df = pd.read_csv(DATA_DIR / f"features_{name}.csv")
    df["model_name"] = name
    df["label3"] = df["depth"].map(CLASS_MAP_3)
    return df


def load_base_all():
    df = pd.read_csv(DATA_DIR / "features_all_models.csv")
    df["label3"] = df["depth"].map(CLASS_MAP_3)
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
        scores.append(f1_score(yt, yp, average="macro"))
    arr = np.array(scores)
    return float(np.percentile(arr, 2.5)), float(np.percentile(arr, 97.5))


def compute_cohens_d(g1, g2):
    n1, n2 = len(g1), len(g2)
    s1, s2 = g1.std(ddof=1), g2.std(ddof=1)
    pooled_std = np.sqrt(((n1 - 1) * s1**2 + (n2 - 1) * s2**2) / (n1 + n2 - 2))
    if pooled_std == 0:
        return 0.0
    return (g1.mean() - g2.mean()) / pooled_std


# ============================================================
# TASK 1: Instruct Model Retrain
# ============================================================

def task1_classification_recovery():
    print("=" * 70)
    print("TASK 1A: Classification Recovery (Within-Model 5-Fold CV)")
    print("=" * 70)

    base_all = load_base_all()
    results = {}

    for inst_name, base_name in INSTRUCT_MODELS.items():
        inst_df = load_instruct(inst_name)
        base_df = base_all[base_all["model_name"] == base_name].copy()

        # --- Within-model 5-fold CV on instruct data (binary) ---
        inst_bin = inst_df[inst_df["label3"] >= 1].copy()
        inst_bin["binary"] = (inst_bin["label3"] >= 2).astype(int)

        skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=SEED)
        y_all_true, y_all_pred = [], []
        rng = np.random.RandomState(SEED)

        for train_idx, test_idx in skf.split(inst_bin[FEATURES], inst_bin["binary"]):
            tr = inst_bin.iloc[train_idx]
            te = inst_bin.iloc[test_idx]
            tr_ds = downsample(tr, "binary", rng)
            clf = XGBClassifier(**XGB_PARAMS)
            clf.fit(tr_ds[FEATURES].values, tr_ds["binary"].values)
            preds = clf.predict(te[FEATURES].values)
            y_all_true.extend(te["binary"].values)
            y_all_pred.extend(preds)

        y_all_true = np.array(y_all_true)
        y_all_pred = np.array(y_all_pred)
        inst_retrain_bin_f1 = f1_score(y_all_true, y_all_pred, average="macro")
        ci_lo, ci_hi = bootstrap_f1(y_all_true, y_all_pred)

        # --- Within-model 5-fold CV on instruct data (3-class) ---
        inst_3c = inst_df.copy()
        skf3 = StratifiedKFold(n_splits=5, shuffle=True, random_state=SEED)
        y3_true, y3_pred = [], []
        rng3 = np.random.RandomState(SEED)

        for train_idx, test_idx in skf3.split(inst_3c[FEATURES], inst_3c["label3"]):
            tr = inst_3c.iloc[train_idx]
            te = inst_3c.iloc[test_idx]
            tr_ds = downsample(tr, "label3", rng3)
            clf = XGBClassifier(**XGB_PARAMS)
            clf.fit(tr_ds[FEATURES].values, tr_ds["label3"].values)
            preds = clf.predict(te[FEATURES].values)
            y3_true.extend(te["label3"].values)
            y3_pred.extend(preds)

        y3_true = np.array(y3_true)
        y3_pred = np.array(y3_pred)
        inst_retrain_3c_f1 = f1_score(y3_true, y3_pred, average="macro")
        ci3_lo, ci3_hi = bootstrap_f1(y3_true, y3_pred)

        # --- Base-trained → instruct-tested (binary) ---
        base_bin = base_df[base_df["label3"] >= 1].copy()
        base_bin["binary"] = (base_bin["label3"] >= 2).astype(int)
        rng_base = np.random.RandomState(SEED)
        base_ds = downsample(base_bin, "binary", rng_base)

        clf_base = XGBClassifier(**XGB_PARAMS)
        clf_base.fit(base_ds[FEATURES].values, base_ds["binary"].values)
        base_on_inst_pred = clf_base.predict(inst_bin[FEATURES].values)
        base_on_inst_f1 = f1_score(inst_bin["binary"].values, base_on_inst_pred, average="macro")
        boi_ci_lo, boi_ci_hi = bootstrap_f1(inst_bin["binary"].values, base_on_inst_pred)

        results[inst_name] = {
            "n_instruct": len(inst_df),
            "n_base": len(base_df),
            "retrain_binary_f1": round(inst_retrain_bin_f1, 3),
            "retrain_binary_ci": [round(ci_lo, 3), round(ci_hi, 3)],
            "retrain_3class_f1": round(inst_retrain_3c_f1, 3),
            "retrain_3class_ci": [round(ci3_lo, 3), round(ci3_hi, 3)],
            "base_on_instruct_f1": round(base_on_inst_f1, 3),
            "base_on_instruct_ci": [round(boi_ci_lo, 3), round(boi_ci_hi, 3)],
        }

    print(f"\n{'Model':<30s} {'Retrain Bin F1':>14s} {'95% CI':>16s} {'Retrain 3cl F1':>14s} {'Base→Inst F1':>14s}")
    print("-" * 92)
    for name, r in results.items():
        print(f"{name:<30s} {r['retrain_binary_f1']:>14.3f} [{r['retrain_binary_ci'][0]:.3f}, {r['retrain_binary_ci'][1]:.3f}] "
              f"{r['retrain_3class_f1']:>14.3f} {r['base_on_instruct_f1']:>14.3f}")

    return results


def task1_logo_instruct():
    print("\n" + "=" * 70)
    print("TASK 1A (cont): 3-Generator LOGO on Merged Instruct Data")
    print("=" * 70)

    frames = []
    for inst_name in INSTRUCT_MODELS:
        df = load_instruct(inst_name)
        frames.append(df)
    merged = pd.concat(frames, ignore_index=True)

    generators = sorted(merged["model_name"].unique())
    print(f"Generators: {generators}, total rows: {len(merged)}")

    # Binary LOGO
    bin_df = merged[merged["label3"] >= 1].copy()
    bin_df["binary"] = (bin_df["label3"] >= 2).astype(int)
    rng = np.random.RandomState(SEED)

    per_gen = {}
    all_true, all_pred = [], []
    for gen in generators:
        test = bin_df[bin_df["model_name"] == gen]
        train = bin_df[bin_df["model_name"] != gen]
        train_ds = downsample(train, "binary", rng)

        clf = XGBClassifier(**XGB_PARAMS)
        clf.fit(train_ds[FEATURES].values, train_ds["binary"].values)
        preds = clf.predict(test[FEATURES].values)
        y_test = test["binary"].values

        f1 = f1_score(y_test, preds, average="macro")
        ci_lo, ci_hi = bootstrap_f1(y_test, preds)
        per_gen[gen] = {"binary_f1": round(f1, 3), "ci": [round(ci_lo, 3), round(ci_hi, 3)]}
        all_true.extend(y_test)
        all_pred.extend(preds)

    all_true, all_pred = np.array(all_true), np.array(all_pred)
    avg_f1 = np.mean([v["binary_f1"] for v in per_gen.values()])
    overall_f1 = f1_score(all_true, all_pred, average="macro")
    ci_lo, ci_hi = bootstrap_f1(all_true, all_pred)

    # 3-class LOGO
    rng3 = np.random.RandomState(SEED)
    per_gen_3c = {}
    for gen in generators:
        test = merged[merged["model_name"] == gen]
        train = merged[merged["model_name"] != gen]
        train_ds = downsample(train, "label3", rng3)
        clf = XGBClassifier(**XGB_PARAMS)
        clf.fit(train_ds[FEATURES].values, train_ds["label3"].values)
        preds = clf.predict(test[FEATURES].values)
        f1_3c = f1_score(test["label3"].values, preds, average="macro")
        per_gen_3c[gen] = round(f1_3c, 3)

    print(f"\n{'Generator':<30s} {'Binary F1':>10s} {'95% CI':>16s} {'3-class F1':>12s}")
    print("-" * 72)
    for gen in generators:
        r = per_gen[gen]
        print(f"{gen:<30s} {r['binary_f1']:>10.3f} [{r['ci'][0]:.3f}, {r['ci'][1]:.3f}] {per_gen_3c[gen]:>12.3f}")
    print("-" * 72)
    print(f"{'Average':30s} {avg_f1:>10.3f}")
    print(f"{'Pooled':30s} {overall_f1:>10.3f} [{ci_lo:.3f}, {ci_hi:.3f}]")

    return {
        "per_generator": per_gen,
        "per_generator_3class": per_gen_3c,
        "average_binary_f1": round(avg_f1, 3),
        "pooled_binary_f1": round(overall_f1, 3),
        "pooled_ci": [round(ci_lo, 3), round(ci_hi, 3)],
    }


def task1_ddr_instruct():
    print("\n" + "=" * 70)
    print("TASK 1B: DDR Structure on Instruct Data")
    print("=" * 70)

    all_results = {}
    for inst_name in INSTRUCT_MODELS:
        df = load_instruct(inst_name)
        bin_df = df[df["label3"] >= 1].copy()
        gen1 = bin_df[bin_df["label3"] == 1]
        gen2p = bin_df[bin_df["label3"] == 2]

        feat_stats = {}
        for feat in FEATURES:
            rho, p_rho = stats.spearmanr(df[feat], df["depth"])
            d = compute_cohens_d(gen2p[feat], gen1[feat])
            feat_stats[feat] = {"rho": round(rho, 3), "d": round(abs(d), 3)}

        all_results[inst_name] = feat_stats

    # Print per-model DDR
    print(f"\n{'Feature':<16s}", end="")
    for name in INSTRUCT_MODELS:
        short = name.replace("-instruct", "").replace("olmo-2-0425-1b", "olmo-inst")
        print(f"  {short:>20s} ρ  {short:>10s} |d|", end="")
    print()
    print("-" * 120)
    for feat in FEATURES:
        print(f"{feat:<16s}", end="")
        for name in INSTRUCT_MODELS:
            s = all_results[name][feat]
            print(f"  {s['rho']:>22.3f}  {s['d']:>12.3f}", end="")
        print()

    # Pooled across instruct models
    frames = [load_instruct(n) for n in INSTRUCT_MODELS]
    pooled = pd.concat(frames, ignore_index=True)
    pooled_bin = pooled[pooled["label3"] >= 1]
    g1 = pooled_bin[pooled_bin["label3"] == 1]
    g2p = pooled_bin[pooled_bin["label3"] == 2]

    pooled_stats = {}
    for feat in FEATURES:
        rho, _ = stats.spearmanr(pooled[feat], pooled["depth"])
        d = compute_cohens_d(g2p[feat], g1[feat])
        pooled_stats[feat] = {"rho": round(rho, 3), "abs_rho": round(abs(rho), 3), "d": round(abs(d), 3)}

    print(f"\n{'Feature':<16s} {'Pooled ρ':>10s} {'|ρ|':>6s} {'|d|':>6s}  Zone (base)")
    print("-" * 55)
    base_zones = {
        "entropy_mean": "drifting", "ttr": "drifting", "hapax_ratio": "drifting",
        "entropy_std": "intermediate",
        "entropy_min": "near-stat", "entropy_max": "near-stat", "tail_decay": "near-stat",
    }
    for feat in FEATURES:
        s = pooled_stats[feat]
        print(f"{feat:<16s} {s['rho']:>10.3f} {s['abs_rho']:>6.3f} {s['d']:>6.3f}  {base_zones[feat]}")

    # k-means on instruct (|ρ|, d) space
    X = np.array([[pooled_stats[f]["abs_rho"], pooled_stats[f]["d"]] for f in FEATURES])
    X_scaled = StandardScaler().fit_transform(X)

    print(f"\nk-means clustering on instruct (|ρ|, d):")
    km_results = {}
    for k in [2, 3]:
        km = KMeans(n_clusters=k, random_state=SEED, n_init=20)
        labels = km.fit_predict(X_scaled)
        sil = silhouette_score(X_scaled, labels)
        clusters = {}
        for i, f in enumerate(FEATURES):
            clusters.setdefault(int(labels[i]), []).append(f)
        km_results[k] = {"silhouette": round(sil, 3), "clusters": clusters}
        print(f"  k={k}: silhouette={sil:.3f}")
        for c in sorted(clusters):
            print(f"    Cluster {c}: {clusters[c]}")

    return {"per_model": all_results, "pooled": pooled_stats, "kmeans": km_results}


def task1_cross_condition():
    print("\n" + "=" * 70)
    print("TASK 1C: Cross-Condition Transfer")
    print("=" * 70)

    base_all = load_base_all()

    # Merge instruct
    inst_frames = [load_instruct(n) for n in INSTRUCT_MODELS]
    inst_merged = pd.concat(inst_frames, ignore_index=True)

    # Corresponding base models only
    base_names = list(INSTRUCT_MODELS.values())
    base_subset = base_all[base_all["model_name"].isin(base_names)].copy()

    # Binary setup
    inst_bin = inst_merged[inst_merged["label3"] >= 1].copy()
    inst_bin["binary"] = (inst_bin["label3"] >= 2).astype(int)

    base_bin = base_subset[base_subset["label3"] >= 1].copy()
    base_bin["binary"] = (base_bin["label3"] >= 2).astype(int)

    rng = np.random.RandomState(SEED)

    # Base-trained → instruct-tested
    base_ds = downsample(base_bin, "binary", rng)
    clf_b2i = XGBClassifier(**XGB_PARAMS)
    clf_b2i.fit(base_ds[FEATURES].values, base_ds["binary"].values)
    pred_b2i = clf_b2i.predict(inst_bin[FEATURES].values)
    f1_b2i = f1_score(inst_bin["binary"].values, pred_b2i, average="macro")
    ci_b2i = bootstrap_f1(inst_bin["binary"].values, pred_b2i)

    # Instruct-trained → base-tested
    inst_ds = downsample(inst_bin, "binary", rng)
    clf_i2b = XGBClassifier(**XGB_PARAMS)
    clf_i2b.fit(inst_ds[FEATURES].values, inst_ds["binary"].values)
    pred_i2b = clf_i2b.predict(base_bin[FEATURES].values)
    f1_i2b = f1_score(base_bin["binary"].values, pred_i2b, average="macro")
    ci_i2b = bootstrap_f1(base_bin["binary"].values, pred_i2b)

    # Instruct-trained within (5-fold CV as reference)
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=SEED)
    y_true_all, y_pred_all = [], []
    for tr_idx, te_idx in skf.split(inst_bin[FEATURES], inst_bin["binary"]):
        tr = inst_bin.iloc[tr_idx]
        te = inst_bin.iloc[te_idx]
        tr_ds = downsample(tr, "binary", rng)
        clf = XGBClassifier(**XGB_PARAMS)
        clf.fit(tr_ds[FEATURES].values, tr_ds["binary"].values)
        preds = clf.predict(te[FEATURES].values)
        y_true_all.extend(te["binary"].values)
        y_pred_all.extend(preds)
    y_true_all, y_pred_all = np.array(y_true_all), np.array(y_pred_all)
    f1_inst_cv = f1_score(y_true_all, y_pred_all, average="macro")
    ci_inst_cv = bootstrap_f1(y_true_all, y_pred_all)

    results = {
        "base_to_instruct": {"f1": round(f1_b2i, 3), "ci": [round(ci_b2i[0], 3), round(ci_b2i[1], 3)]},
        "instruct_to_base": {"f1": round(f1_i2b, 3), "ci": [round(ci_i2b[0], 3), round(ci_i2b[1], 3)]},
        "instruct_within_cv": {"f1": round(f1_inst_cv, 3), "ci": [round(ci_inst_cv[0], 3), round(ci_inst_cv[1], 3)]},
    }

    print(f"\n{'Condition':<30s} {'Binary F1':>10s} {'95% CI':>20s}")
    print("-" * 62)
    print(f"{'Base→Instruct (3-model)':30s} {f1_b2i:>10.3f} [{ci_b2i[0]:.3f}, {ci_b2i[1]:.3f}]")
    print(f"{'Instruct→Base (3-model)':30s} {f1_i2b:>10.3f} [{ci_i2b[0]:.3f}, {ci_i2b[1]:.3f}]")
    print(f"{'Instruct 5-fold CV':30s} {f1_inst_cv:>10.3f} [{ci_inst_cv[0]:.3f}, {ci_inst_cv[1]:.3f}]")
    print(f"\nAsymmetry (inst→base minus base→inst): {f1_i2b - f1_b2i:+.3f}")

    return results


# ============================================================
# TASK 2: Feature Ablation Supplement
# ============================================================

def task2_feature_ablation():
    print("\n" + "=" * 70)
    print("TASK 2: Feature Ablation Supplement (8-gen LOGO)")
    print("=" * 70)

    base_all = load_base_all()
    bin_df = base_all[base_all["label3"] >= 1].copy()
    bin_df["binary"] = (bin_df["label3"] >= 2).astype(int)
    generators = sorted(bin_df["model_name"].unique())

    near_stat = ["entropy_min", "entropy_max", "tail_decay"]

    configs = {
        "hapax+ent_std+3NS (no TTR, no ent_mean)": ["hapax_ratio", "entropy_std"] + near_stat,
        "ent_mean+ent_std+3NS (no TTR, no hapax)": ["entropy_mean", "entropy_std"] + near_stat,
        "Full 7-feature (reference)": FEATURES,
    }

    results = {}

    for config_name, feats in configs.items():
        rng = np.random.RandomState(SEED)
        all_true, all_pred = [], []

        per_gen_f1 = {}
        for gen in generators:
            test = bin_df[bin_df["model_name"] == gen]
            train = bin_df[bin_df["model_name"] != gen]
            train_ds = downsample(train, "binary", rng)

            clf = XGBClassifier(**XGB_PARAMS)
            clf.fit(train_ds[feats].values, train_ds["binary"].values)
            preds = clf.predict(test[feats].values)
            y_test = test["binary"].values

            f1 = f1_score(y_test, preds, average="macro")
            per_gen_f1[gen] = round(f1, 3)
            all_true.extend(y_test)
            all_pred.extend(preds)

        all_true, all_pred = np.array(all_true), np.array(all_pred)
        avg_f1 = np.mean(list(per_gen_f1.values()))
        ci_lo, ci_hi = bootstrap_f1(all_true, all_pred)

        results[config_name] = {
            "features": feats,
            "n_features": len(feats),
            "avg_binary_f1": round(avg_f1, 3),
            "ci": [round(ci_lo, 3), round(ci_hi, 3)],
            "per_generator": per_gen_f1,
        }

    # PC1 ablation
    drifting_feats = ["entropy_mean", "ttr", "hapax_ratio"]
    other_feats = ["entropy_std"] + near_stat

    rng = np.random.RandomState(SEED)
    all_true, all_pred = [], []
    per_gen_f1 = {}

    for gen in generators:
        test = bin_df[bin_df["model_name"] == gen]
        train = bin_df[bin_df["model_name"] != gen]

        # Fit PCA on training drifting features
        pca = PCA(n_components=1, random_state=SEED)
        train_pc1 = pca.fit_transform(train[drifting_feats].values)
        test_pc1 = pca.transform(test[drifting_feats].values)

        train_aug = np.hstack([train_pc1, train[other_feats].values])
        test_aug = np.hstack([test_pc1, test[other_feats].values])

        train_labels = train["binary"].values
        # Downsample
        idx_all = np.arange(len(train_labels))
        classes = np.unique(train_labels)
        min_n = min((train_labels == c).sum() for c in classes)
        ds_idx = []
        for c in classes:
            c_idx = idx_all[train_labels == c]
            ds_idx.extend(rng.choice(c_idx, size=min_n, replace=False))
        ds_idx = np.array(ds_idx)

        clf = XGBClassifier(**XGB_PARAMS)
        clf.fit(train_aug[ds_idx], train_labels[ds_idx])
        preds = clf.predict(test_aug)
        y_test = test["binary"].values

        f1 = f1_score(y_test, preds, average="macro")
        per_gen_f1[gen] = round(f1, 3)
        all_true.extend(y_test)
        all_pred.extend(preds)

    all_true, all_pred = np.array(all_true), np.array(all_pred)
    avg_f1 = np.mean(list(per_gen_f1.values()))
    ci_lo, ci_hi = bootstrap_f1(all_true, all_pred)

    results["PC1(3 drifting)+ent_std+3NS"] = {
        "features": ["PC1(ent_mean,ttr,hapax)"] + other_feats,
        "n_features": 5,
        "avg_binary_f1": round(avg_f1, 3),
        "ci": [round(ci_lo, 3), round(ci_hi, 3)],
        "per_generator": per_gen_f1,
    }

    print(f"\n{'Configuration':<45s} {'#Feat':>5s} {'Bin F1':>8s} {'95% CI':>18s}")
    print("-" * 80)
    for name, r in results.items():
        print(f"{name:<45s} {r['n_features']:>5d} {r['avg_binary_f1']:>8.3f} [{r['ci'][0]:.3f}, {r['ci'][1]:.3f}]")

    return results


# ============================================================
# MAIN
# ============================================================

def main():
    print("R25 Instruct Analysis — All CPU\n")

    # Task 1
    recovery = task1_classification_recovery()
    logo = task1_logo_instruct()
    ddr = task1_ddr_instruct()
    transfer = task1_cross_condition()

    # Task 2
    ablation = task2_feature_ablation()

    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)

    print("\n--- Instruct Retrain Recovery ---")
    for name, r in recovery.items():
        delta = r["retrain_binary_f1"] - r["base_on_instruct_f1"]
        print(f"  {name}: retrain={r['retrain_binary_f1']:.3f}, base→inst={r['base_on_instruct_f1']:.3f}, Δ={delta:+.3f}")

    print(f"\n--- Instruct LOGO ---")
    print(f"  3-gen LOGO binary F1: {logo['average_binary_f1']:.3f} (pooled: {logo['pooled_binary_f1']:.3f})")

    print(f"\n--- DDR on Instruct ---")
    print(f"  k=2 silhouette: {ddr['kmeans'][2]['silhouette']:.3f}")
    print(f"  k=3 silhouette: {ddr['kmeans'][3]['silhouette']:.3f}")
    drifting_rhos = [ddr['pooled'][f]['abs_rho'] for f in ['entropy_mean', 'ttr', 'hapax_ratio']]
    ns_rhos = [ddr['pooled'][f]['abs_rho'] for f in ['entropy_min', 'entropy_max', 'tail_decay']]
    print(f"  Drifting |ρ| range: {min(drifting_rhos):.3f}–{max(drifting_rhos):.3f}")
    print(f"  Near-stat |ρ| range: {min(ns_rhos):.3f}–{max(ns_rhos):.3f}")

    print(f"\n--- Cross-Condition Transfer ---")
    print(f"  Base→Instruct: {transfer['base_to_instruct']['f1']:.3f}")
    print(f"  Instruct→Base: {transfer['instruct_to_base']['f1']:.3f}")
    print(f"  Asymmetry: {transfer['instruct_to_base']['f1'] - transfer['base_to_instruct']['f1']:+.3f}")

    print(f"\n--- Feature Ablation ---")
    for name, r in ablation.items():
        print(f"  {name}: {r['avg_binary_f1']:.3f} [{r['ci'][0]:.3f}, {r['ci'][1]:.3f}]")

    import json
    output = {
        "task1_recovery": recovery,
        "task1_logo": logo,
        "task1_ddr": ddr,
        "task1_transfer": transfer,
        "task2_ablation": ablation,
    }
    out_path = Path(__file__).parent / "rebuttal" / "r25_instruct_results.json"
    out_path.parent.mkdir(exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, default=str)
    print(f"\nFull results saved to {out_path}")


if __name__ == "__main__":
    main()
