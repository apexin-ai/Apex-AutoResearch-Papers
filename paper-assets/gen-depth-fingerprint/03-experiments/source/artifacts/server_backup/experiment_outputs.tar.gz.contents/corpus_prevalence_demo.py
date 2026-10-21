"""
corpus_prevalence_demo.py — Corpus-level depth prevalence estimation.

Build 5 synthetic corpora with known depth-2+ proportions (0%, 25%, 50%, 75%, 100%).
Use LOGO-trained XGBoost with four quantification methods:
  CC  — Classify & Count (hard predictions)
  ACC — Adjusted CC (correct with CV-estimated TPR/FPR)  
  PCC — Probabilistic CC (mean predicted probability)
  EMQ — EM-based quantification (Saerens et al. 2002)
Report calibration MAE for each.
"""

import json
import os
import numpy as np
import pandas as pd
from xgboost import XGBClassifier
from sklearn.metrics import confusion_matrix
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

SEED = 42
FEATURES = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max",
            "tail_decay", "ttr", "hapax_ratio"]

XGB_PARAMS = dict(n_estimators=200, max_depth=6, learning_rate=0.1,
                  random_state=SEED, eval_metric="mlogloss",
                  use_label_encoder=False)

CLASS_MAP_3 = {0: 0, 1: 1, 2: 2, 3: 2, 4: 2}

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(ROOT, "data")
RESULTS_DIR = os.path.join(ROOT, "results")

CORPUS_SIZE = 800
TRUE_PROPORTIONS = [0.0, 0.25, 0.50, 0.75, 1.00]
N_BOOTSTRAP = 200


def load_data():
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
    df["label"] = df["depth"].map(CLASS_MAP_3)
    return df


def downsample(df, label_col, rng):
    counts = df[label_col].value_counts()
    min_n = counts.min()
    parts = []
    for lbl in sorted(counts.index):
        sub = df[df[label_col] == lbl]
        parts.append(sub.sample(n=min_n, random_state=rng, replace=False))
    return pd.concat(parts, ignore_index=True)


def estimate_tpr_fpr_cv(train_df, features, n_folds=5, seed=42):
    rng = np.random.RandomState(seed)
    indices = np.arange(len(train_df))
    rng.shuffle(indices)
    folds = np.array_split(indices, n_folds)
    all_y_true, all_y_pred = [], []
    for i in range(n_folds):
        val_idx = folds[i]
        train_idx = np.concatenate([folds[j] for j in range(n_folds) if j != i])
        tr = train_df.iloc[train_idx]
        va = train_df.iloc[val_idx]
        tr_ds = downsample(tr, "binary", rng)
        clf = XGBClassifier(**XGB_PARAMS)
        clf.fit(tr_ds[features].values, tr_ds["binary"].values)
        preds = clf.predict(va[features].values)
        all_y_true.extend(va["binary"].values)
        all_y_pred.extend(preds)
    tn, fp, fn, tp = confusion_matrix(np.array(all_y_true), np.array(all_y_pred)).ravel()
    return tp / (tp + fn), fp / (fp + tn)


def acc_correct(prev, tpr, fpr):
    d = tpr - fpr
    if abs(d) < 1e-6:
        return prev
    return float(np.clip((prev - fpr) / d, 0, 1))


def emq_prevalence(proba_pos, train_prevalence, max_iter=100, tol=1e-6):
    """EM quantification (Saerens et al. 2002). Returns estimated positive prevalence."""
    n = len(proba_pos)
    proba_neg = 1.0 - proba_pos
    pi_train = np.array([1.0 - train_prevalence, train_prevalence])
    pi = pi_train.copy()

    for _ in range(max_iter):
        # E-step: adjust posteriors with new priors
        ratio = pi / pi_train
        adj_pos = proba_pos * ratio[1]
        adj_neg = proba_neg * ratio[0]
        denom = adj_pos + adj_neg
        denom = np.maximum(denom, 1e-10)
        post_pos = adj_pos / denom

        # M-step: new prevalence = mean adjusted posterior
        new_pi1 = float(np.mean(post_pos))
        new_pi = np.array([1.0 - new_pi1, new_pi1])

        if np.max(np.abs(new_pi - pi)) < tol:
            pi = new_pi
            break
        pi = new_pi

    return float(np.clip(pi[1], 0, 1))


def run_prevalence_estimation(df):
    generators = sorted(df["model_name"].unique())
    rng = np.random.RandomState(SEED)
    all_gen_results = {}

    for gen in generators:
        print(f"\n--- Held-out: {gen} ---")
        test_df = df[df["model_name"] == gen].copy()
        train_df = df[df["model_name"] != gen].copy()

        train_bin = train_df[train_df["label"] >= 1].copy()
        train_bin["binary"] = (train_bin["label"] >= 2).astype(int)
        test_bin = test_df[test_df["label"] >= 1].copy()
        test_bin["binary"] = (test_bin["label"] >= 2).astype(int)

        tpr, fpr = estimate_tpr_fpr_cv(train_bin, FEATURES, n_folds=5, seed=SEED)

        train_ds = downsample(train_bin, "binary", rng)
        train_prev = float(train_ds["binary"].mean())
        clf = XGBClassifier(**XGB_PARAMS)
        clf.fit(train_ds[FEATURES].values, train_ds["binary"].values)

        gen1_pool = test_bin[test_bin["binary"] == 0]
        gen2_pool = test_bin[test_bin["binary"] == 1]
        n_gen1, n_gen2 = len(gen1_pool), len(gen2_pool)

        corpus_results = []
        for true_prop in TRUE_PROPORTIONS:
            n_pos = int(round(CORPUS_SIZE * true_prop))
            n_neg = CORPUS_SIZE - n_pos
            if n_neg > n_gen1 or n_pos > n_gen2:
                continue

            boot_cc, boot_acc, boot_pcc, boot_emq = [], [], [], []
            for b in range(N_BOOTSTRAP):
                brng = np.random.RandomState(SEED + b)
                s_neg = gen1_pool.sample(n=n_neg, random_state=brng, replace=True)
                s_pos = gen2_pool.sample(n=n_pos, random_state=brng, replace=True)
                corpus = pd.concat([s_neg, s_pos], ignore_index=True)
                X = corpus[FEATURES].values

                preds = clf.predict(X)
                proba = clf.predict_proba(X)[:, 1]

                cc = float(preds.sum()) / len(preds)
                acc_v = acc_correct(cc, tpr, fpr)
                pcc = float(proba.mean())
                emq = emq_prevalence(proba, train_prev)

                boot_cc.append(cc)
                boot_acc.append(acc_v)
                boot_pcc.append(pcc)
                boot_emq.append(emq)

            results = {}
            for name, arr in [("cc", boot_cc), ("acc", boot_acc),
                              ("pcc", boot_pcc), ("emq", boot_emq)]:
                m = float(np.mean(arr))
                results[f"{name}_prop"] = round(m, 4)
                results[f"{name}_err"] = round(abs(m - true_prop) * 100, 2)
                results[f"{name}_ci_lo"] = round(float(np.percentile(arr, 2.5)), 4)
                results[f"{name}_ci_hi"] = round(float(np.percentile(arr, 97.5)), 4)
            results["true_prop"] = true_prop

            corpus_results.append(results)
            print(f"  {true_prop:.0%}  CC={results['cc_err']:.1f}  ACC={results['acc_err']:.1f}  "
                  f"PCC={results['pcc_err']:.1f}  EMQ={results['emq_err']:.1f}pp")

        all_gen_results[gen] = {"tpr": round(tpr, 4), "fpr": round(fpr, 4),
                                "corpora": corpus_results}

    return all_gen_results


def aggregate_results(all_gen_results):
    methods = ["cc", "acc", "pcc", "emq"]
    prop_data = {p: {m: {"err": [], "pred": [], "ci_lo": [], "ci_hi": []}
                     for m in methods} for p in TRUE_PROPORTIONS}

    for gen, res in all_gen_results.items():
        for c in res["corpora"]:
            tp = c["true_prop"]
            for m in methods:
                prop_data[tp][m]["err"].append(c[f"{m}_err"])
                prop_data[tp][m]["pred"].append(c[f"{m}_prop"])
                prop_data[tp][m]["ci_lo"].append(c[f"{m}_ci_lo"])
                prop_data[tp][m]["ci_hi"].append(c[f"{m}_ci_hi"])

    agg = []
    for tp in TRUE_PROPORTIONS:
        if not prop_data[tp]["cc"]["err"]:
            continue
        entry = {"true_prop": tp}
        for m in methods:
            d = prop_data[tp][m]
            entry[f"{m}_pred_mean"] = round(float(np.mean(d["pred"])), 4)
            entry[f"{m}_err_mean"] = round(float(np.mean(d["err"])), 2)
            entry[f"{m}_ci_lo_mean"] = round(float(np.mean(d["ci_lo"])), 4)
            entry[f"{m}_ci_hi_mean"] = round(float(np.mean(d["ci_hi"])), 4)
        agg.append(entry)

    maes = {}
    for m in methods:
        maes[m] = round(float(np.mean([a[f"{m}_err_mean"] for a in agg])), 2)
    return agg, maes


def plot_calibration(agg, all_gen_results, maes, out_path):
    methods = [
        ("cc", "Classify & Count"),
        ("acc", "Adjusted CC"),
        ("emq", "EM Quantification"),
    ]
    fig, axes = plt.subplots(1, 3, figsize=(14, 4.5))

    for ax, (key, title) in zip(axes, methods):
        mae = maes[key]
        for gen, res in all_gen_results.items():
            xs = [c["true_prop"] * 100 for c in res["corpora"]]
            ys = [c[f"{key}_prop"] * 100 for c in res["corpora"]]
            ax.scatter(xs, ys, alpha=0.25, s=20, color="steelblue", zorder=2)

        true_pcts = [a["true_prop"] * 100 for a in agg]
        pred_pcts = [a[f"{key}_pred_mean"] * 100 for a in agg]
        ci_lo = [a[f"{key}_ci_lo_mean"] * 100 for a in agg]
        ci_hi = [a[f"{key}_ci_hi_mean"] * 100 for a in agg]
        yerr_lo = [p - lo for p, lo in zip(pred_pcts, ci_lo)]
        yerr_hi = [hi - p for p, hi in zip(pred_pcts, ci_hi)]
        ax.errorbar(true_pcts, pred_pcts, yerr=[yerr_lo, yerr_hi],
                    fmt="o-", color="darkblue", capsize=4, capthick=1.5,
                    markersize=7, zorder=3)

        ax.plot([0, 100], [0, 100], "k--", alpha=0.4, linewidth=1)
        ax.set_xlabel("True depth-2+ (%)", fontsize=10)
        ax.set_ylabel("Predicted depth-2+ (%)", fontsize=10)
        ax.set_xlim(-5, 105)
        ax.set_ylim(-5, 105)
        ax.set_aspect("equal")
        ax.set_title(f"{title}\nMAE = {mae:.1f}pp", fontsize=11)

    plt.tight_layout()
    plt.savefig(out_path, dpi=300, bbox_inches="tight")
    plt.savefig(out_path.replace(".pdf", ".png"), dpi=150, bbox_inches="tight")
    print(f"\nSaved: {out_path}")


def main():
    os.makedirs(RESULTS_DIR, exist_ok=True)
    print("Loading 8-gen data...")
    df = load_data()
    print(f"Loaded {len(df)} rows, {df['model_name'].nunique()} generators")

    all_gen_results = run_prevalence_estimation(df)
    agg, maes = aggregate_results(all_gen_results)

    best_name = min(maes, key=maes.get)
    best_mae = maes[best_name]

    print("\n" + "=" * 85)
    print("AGGREGATED RESULTS (averaged across 8 held-out generators)")
    print("=" * 85)
    header = f"{'True':>6s}"
    for m in ["cc", "acc", "pcc", "emq"]:
        header += f"  {m.upper()+' pred':>9s} {m.upper()+' err':>8s}"
    print(header)
    for a in agg:
        line = f"{a['true_prop']*100:5.0f}%"
        for m in ["cc", "acc", "pcc", "emq"]:
            line += f"  {a[f'{m}_pred_mean']*100:8.1f}% {a[f'{m}_err_mean']:7.2f}pp"
        print(line)

    print()
    for m in ["cc", "acc", "pcc", "emq"]:
        marker = " <-- best" if m == best_name else ""
        print(f"  {m.upper():4s} MAE = {maes[m]:6.2f}pp{marker}")

    viable = best_mae < 5.0
    conclusion = "viable" if viable else "not viable"
    print(f"\nConclusion: corpus-level depth auditing is {conclusion} "
          f"(best MAE = {best_mae:.2f}pp, method={best_name.upper()}, threshold=5pp)")

    out = {
        "corpus_size": CORPUS_SIZE,
        "n_bootstrap": N_BOOTSTRAP,
        "n_generators": len(all_gen_results),
        "per_generator": all_gen_results,
        "aggregated": agg,
        "maes": maes,
        "best_method": best_name.upper(),
        "best_mae_pp": best_mae,
        "conclusion": conclusion,
    }
    json_path = os.path.join(RESULTS_DIR, "corpus_prevalence_demo.json")
    with open(json_path, "w") as f:
        json.dump(out, f, indent=2)
    print(f"Saved: {json_path}")

    pdf_path = os.path.join(RESULTS_DIR, "corpus_prevalence_calibration.pdf")
    plot_calibration(agg, all_gen_results, maes, pdf_path)


if __name__ == "__main__":
    main()
