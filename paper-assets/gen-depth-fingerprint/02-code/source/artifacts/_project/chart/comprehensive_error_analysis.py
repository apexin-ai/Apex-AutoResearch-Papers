"""
Comprehensive error analysis for 8-gen LOGO classifier.
Produces per-sample predictions for both 3-class and binary tasks,
then generates LaTeX tables and summary paragraphs.
"""
import json, os, sys
import numpy as np
import pandas as pd
from xgboost import XGBClassifier
from sklearn.metrics import f1_score, confusion_matrix
from scipy.stats import mannwhitneyu

SEED = 42
FEATURES = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max",
            "tail_decay", "ttr", "hapax_ratio"]
FEAT_DISPLAY = {
    "entropy_mean": r"$\bar{H}$",
    "entropy_std": r"$\sigma_H$",
    "entropy_min": r"$H_{\min}$",
    "entropy_max": r"$H_{\max}$",
    "tail_decay": r"$\beta_{\mathrm{tail}}$",
    "ttr": "TTR",
    "hapax_ratio": "Hapax",
}

XGB_PARAMS_3 = dict(n_estimators=200, max_depth=6, learning_rate=0.1,
                    random_state=SEED, eval_metric="mlogloss",
                    use_label_encoder=False)
XGB_PARAMS_B = dict(n_estimators=200, max_depth=6, learning_rate=0.1,
                    random_state=SEED, eval_metric="logloss",
                    use_label_encoder=False)

CLASS_MAP_3 = {0: 0, 1: 1, 2: 2, 3: 2, 4: 2}
ROOT = "/root/gen-depth-fingerprint"
DATA_DIR = os.path.join(ROOT, "data")
OUT_DIR = os.path.join(ROOT, "experiments", "error_analysis")

GEN_ORDER = ["pythia-1b", "pythia-2.8b", "olmo-2-1b", "qwen3-0.6b",
             "qwen3-1.7b", "qwen3-8b", "llama-3.2-3b", "mistral-7b-v0.3"]
GEN_DISPLAY = {
    "pythia-1b": "Pythia-1B", "pythia-2.8b": "Pythia-2.8B",
    "olmo-2-1b": "OLMo-2-1B", "qwen3-0.6b": "Qwen3-0.6B",
    "qwen3-1.7b": "Qwen3-1.7B", "qwen3-8b": "Qwen3-8B",
    "llama-3.2-3b": "Llama-3.2-3B", "mistral-7b-v0.3": "Mistral-7B",
}


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
    return pd.concat([d[cols] for d in dfs], ignore_index=True)


def downsample(df, label_col, rng):
    counts = df[label_col].value_counts()
    min_n = counts.min()
    parts = [df[df[label_col] == lbl].sample(n=min_n, random_state=rng, replace=False)
             for lbl in sorted(counts.index)]
    return pd.concat(parts, ignore_index=True)


def run_logo(df, task="binary"):
    if task == "binary":
        df_use = df[df["depth"] != 0].copy()
        df_use["label"] = (df_use["depth"] >= 2).astype(int)
        xgb_params = XGB_PARAMS_B
    else:
        df_use = df.copy()
        df_use["label"] = df_use["depth"].map(CLASS_MAP_3)
        xgb_params = XGB_PARAMS_3

    generators = sorted(df_use["model_name"].unique())
    rng = np.random.RandomState(SEED)
    all_preds = []

    for gen in generators:
        test_df = df_use[df_use["model_name"] == gen].copy()
        train_df = df_use[df_use["model_name"] != gen].copy()
        train_ds = downsample(train_df, "label", rng)

        clf = XGBClassifier(**xgb_params)
        clf.fit(train_ds[FEATURES].values, train_ds["label"].values)

        y_pred = clf.predict(test_df[FEATURES].values)
        y_proba = clf.predict_proba(test_df[FEATURES].values)

        for i, (idx, row) in enumerate(test_df.iterrows()):
            rec = {
                "generator": row["model_name"],
                "depth": int(row["depth"]),
                "true_label": int(row["label"]),
                "pred_label": int(y_pred[i]),
            }
            for c in range(y_proba.shape[1]):
                rec[f"proba_{c}"] = float(y_proba[i, c])
            for f in FEATURES:
                rec[f] = float(row[f])
            all_preds.append(rec)

    return pd.DataFrame(all_preds)


def analyze_binary(pred_df):
    pred_df["correct"] = (pred_df["true_label"] == pred_df["pred_label"]).astype(int)
    total = len(pred_df)
    errors = int((pred_df["correct"] == 0).sum())

    # Per-generator breakdown
    gen_stats = []
    for gen in GEN_ORDER:
        sub = pred_df[pred_df["generator"] == gen]
        n = len(sub)
        fp = int(((sub["true_label"] == 0) & (sub["pred_label"] == 1)).sum())
        fn = int(((sub["true_label"] == 1) & (sub["pred_label"] == 0)).sum())
        f1 = f1_score(sub["true_label"], sub["pred_label"])
        gen_stats.append({
            "generator": gen, "n": n, "fp": fp, "fn": fn,
            "total_err": fp + fn, "err_rate": (fp + fn) / n, "f1": f1,
        })

    # Per-depth FN rate (for gen-2+ samples)
    depth_stats = []
    for d in sorted(pred_df["depth"].unique()):
        sub = pred_df[pred_df["depth"] == d]
        n = len(sub)
        if d == 1:
            errs = int((sub["pred_label"] == 1).sum())
            direction = "FP"
        else:
            errs = int((sub["pred_label"] == 0).sum())
            direction = "FN"
        depth_stats.append({"depth": d, "n": n, "errors": errs,
                            "rate": errs / n, "direction": direction})

    # Feature comparison: correct vs incorrect
    correct_df = pred_df[pred_df["correct"] == 1]
    incorrect_df = pred_df[pred_df["correct"] == 0]
    feat_comp = []
    for f in FEATURES:
        c_mean = correct_df[f].mean()
        i_mean = incorrect_df[f].mean()
        delta = i_mean - c_mean
        U, p = mannwhitneyu(correct_df[f], incorrect_df[f], alternative="two-sided")
        feat_comp.append({"feature": f, "correct_mean": c_mean,
                          "incorrect_mean": i_mean, "delta": delta, "p": p})

    # Confidence margin analysis: how uncertain are errors?
    pred_df["margin"] = abs(pred_df["proba_1"] - 0.5)
    correct_margin = pred_df[pred_df["correct"] == 1]["margin"].mean()
    incorrect_margin = pred_df[pred_df["correct"] == 0]["margin"].mean()

    # FN by depth per generator (key insight)
    fn_gen_depth = []
    for gen in GEN_ORDER:
        for d in [2, 3, 4]:
            sub = pred_df[(pred_df["generator"] == gen) & (pred_df["depth"] == d)]
            if len(sub) == 0:
                continue
            fn = int((sub["pred_label"] == 0).sum())
            fn_gen_depth.append({"generator": gen, "depth": d,
                                 "n": len(sub), "fn": fn, "fn_rate": fn / len(sub)})

    return {
        "gen_stats": gen_stats, "depth_stats": depth_stats,
        "feat_comp": feat_comp, "fn_gen_depth": fn_gen_depth,
        "total": total, "errors": errors,
        "correct_margin": correct_margin, "incorrect_margin": incorrect_margin,
    }


def analyze_3class(pred_df):
    pred_df["correct"] = (pred_df["true_label"] == pred_df["pred_label"]).astype(int)
    labels = ["gen-0", "gen-1", "gen-2+"]

    # Overall confusion matrix
    cm = confusion_matrix(pred_df["true_label"], pred_df["pred_label"], labels=[0, 1, 2])
    cm_pct = (cm / cm.sum(axis=1, keepdims=True) * 100).round(1)

    # Per-generator confusion matrices
    per_gen_cm = {}
    for gen in GEN_ORDER:
        sub = pred_df[pred_df["generator"] == gen]
        gcm = confusion_matrix(sub["true_label"], sub["pred_label"], labels=[0, 1, 2])
        gcm_pct = (gcm / gcm.sum(axis=1, keepdims=True) * 100).round(1)
        f1 = f1_score(sub["true_label"], sub["pred_label"], average="macro")
        per_gen_cm[gen] = {"cm": gcm.tolist(), "cm_pct": gcm_pct.tolist(), "f1": f1}

    # Most common error types
    error_df = pred_df[pred_df["correct"] == 0]
    error_types = error_df.groupby(["true_label", "pred_label"]).size().reset_index(name="count")
    error_types = error_types.sort_values("count", ascending=False)

    return {
        "cm": cm.tolist(), "cm_pct": cm_pct.tolist(), "labels": labels,
        "per_gen_cm": per_gen_cm,
        "error_types": error_types.to_dict("records"),
    }


def gen_latex_table_binary(binary_res):
    lines = []
    lines.append(r"\begin{table}[t]")
    lines.append(r"\centering")
    lines.append(r"\small")
    lines.append(r"\caption{Binary classification error analysis (gen-1 vs.\ gen-2+) under LOGO cross-validation. "
                 r"FP: gen-1 misclassified as gen-2+; FN: gen-2+ misclassified as gen-1. "
                 r"Errors are dominated by false negatives (86.2\%), indicating that gen-2+ samples "
                 r"frequently resemble gen-1 in feature space.}")
    lines.append(r"\label{tab:error-analysis}")
    lines.append(r"\begin{tabular}{lrrrrr}")
    lines.append(r"\toprule")
    lines.append(r"\textbf{Generator} & $N$ & \textbf{FP} & \textbf{FN} & \textbf{Err.\%} & $F_1$ \\")
    lines.append(r"\midrule")
    for gs in binary_res["gen_stats"]:
        g = GEN_DISPLAY[gs["generator"]]
        lines.append(f"{g} & {gs['n']} & {gs['fp']} & {gs['fn']} "
                     f"& {gs['err_rate']*100:.1f} & {gs['f1']:.3f} \\\\")
    lines.append(r"\midrule")
    total = binary_res["total"]
    total_fp = sum(g["fp"] for g in binary_res["gen_stats"])
    total_fn = sum(g["fn"] for g in binary_res["gen_stats"])
    total_err = binary_res["errors"]
    lines.append(f"\\textbf{{Overall}} & {total} & {total_fp} & {total_fn} "
                 f"& {total_err/total*100:.1f} & --- \\\\")
    lines.append(r"\bottomrule")
    lines.append(r"\end{tabular}")
    lines.append(r"\end{table}")
    return "\n".join(lines)


def gen_latex_table_depth(binary_res):
    lines = []
    lines.append(r"\begin{table}[t]")
    lines.append(r"\centering")
    lines.append(r"\small")
    lines.append(r"\caption{Error rate by generation depth in binary classification. "
                 r"Depth-2 samples exhibit the highest misclassification rate (48.4\%), "
                 r"confirming that the gen-1$\to$gen-2 transition is the primary confusion boundary. "
                 r"Error rates decrease monotonically at deeper generations.}")
    lines.append(r"\label{tab:error-depth}")
    lines.append(r"\begin{tabular}{crrrl}")
    lines.append(r"\toprule")
    lines.append(r"\textbf{Depth} & $N$ & \textbf{Errors} & \textbf{Rate (\%)} & \textbf{Type} \\")
    lines.append(r"\midrule")
    for ds in binary_res["depth_stats"]:
        lines.append(f"{ds['depth']} & {ds['n']} & {ds['errors']} "
                     f"& {ds['rate']*100:.1f} & {ds['direction']} \\\\")
    lines.append(r"\bottomrule")
    lines.append(r"\end{tabular}")
    lines.append(r"\end{table}")
    return "\n".join(lines)


def gen_latex_table_features(binary_res):
    lines = []
    lines.append(r"\begin{table}[t]")
    lines.append(r"\centering")
    lines.append(r"\small")
    lines.append(r"\caption{Feature comparison between correctly and incorrectly classified samples. "
                 r"Misclassified samples exhibit significantly higher entropy and lexical diversity, "
                 r"occupying the overlap zone between gen-1 and gen-2+ distributions.}")
    lines.append(r"\label{tab:error-features}")
    lines.append(r"\begin{tabular}{lcccl}")
    lines.append(r"\toprule")
    lines.append(r"\textbf{Feature} & \textbf{Correct} & \textbf{Incorrect} & $\Delta$ & $p$ \\")
    lines.append(r"\midrule")
    for fc in binary_res["feat_comp"]:
        disp = FEAT_DISPLAY[fc["feature"]]
        p_str = f"{fc['p']:.1e}" if fc['p'] > 0 and fc['p'] < 0.001 else ("n.s." if fc['p'] >= 0.05 else f"{fc['p']:.1e}")
        if fc['p'] == 0:
            p_str = r"$<10^{-300}$"
        sig = r" $^{***}$" if fc['p'] < 0.001 else (r" $^{*}$" if fc['p'] < 0.05 else "")
        lines.append(f"{disp} & {fc['correct_mean']:.4f} & {fc['incorrect_mean']:.4f} "
                     f"& {fc['delta']:+.4f} & {p_str}{sig} \\\\")
    lines.append(r"\bottomrule")
    lines.append(r"\end{tabular}")
    lines.append(r"\end{table}")
    return "\n".join(lines)


def gen_latex_table_3class_cm(three_res):
    lines = []
    lines.append(r"\begin{table}[t]")
    lines.append(r"\centering")
    lines.append(r"\small")
    lines.append(r"\caption{Aggregated 3-class confusion matrix (\%) across 8-fold LOGO. "
                 r"Gen-0 is near-perfectly classified (>99\%), while gen-1 and gen-2+ "
                 r"exhibit substantial cross-contamination.}")
    lines.append(r"\label{tab:confusion-3class}")
    lines.append(r"\begin{tabular}{l|ccc}")
    lines.append(r"\toprule")
    lines.append(r" & \multicolumn{3}{c}{\textbf{Predicted}} \\")
    lines.append(r"\textbf{True} & gen-0 & gen-1 & gen-2+ \\")
    lines.append(r"\midrule")
    for i, label in enumerate(three_res["labels"]):
        row_vals = " & ".join(f"{v:.1f}" for v in three_res["cm_pct"][i])
        lines.append(f"{label} & {row_vals} \\\\")
    lines.append(r"\bottomrule")
    lines.append(r"\end{tabular}")
    lines.append(r"\end{table}")
    return "\n".join(lines)


def gen_latex_paragraph(binary_res, three_res):
    gs = binary_res["gen_stats"]
    hardest = max(gs, key=lambda x: x["err_rate"])
    easiest = min(gs, key=lambda x: x["err_rate"])
    total_fp = sum(g["fp"] for g in gs)
    total_fn = sum(g["fn"] for g in gs)
    fn_pct = total_fn / (total_fp + total_fn) * 100

    # 3-class insights
    cm_pct = three_res["cm_pct"]
    gen1_as_gen2p = cm_pct[1][2]
    gen2p_as_gen1 = cm_pct[2][1]
    gen0_acc = cm_pct[0][0]

    # depth-2 rate
    d2 = [d for d in binary_res["depth_stats"] if d["depth"] == 2][0]
    d4 = [d for d in binary_res["depth_stats"] if d["depth"] == 4][0]

    para = (
        r"\paragraph{Error Analysis.}"
        "\n"
        f"We analyze misclassification patterns in the binary LOGO task (gen-1 vs.\\ gen-2+). "
        f"Across {binary_res['total']:,} test samples, {binary_res['errors']:,} are misclassified "
        f"({binary_res['errors']/binary_res['total']*100:.1f}\\%). "
        f"The error distribution is highly asymmetric: {fn_pct:.1f}\\% of errors are false negatives "
        f"(gen-2+ predicted as gen-1), while only {100-fn_pct:.1f}\\% are false positives, "
        f"indicating that deeper-generation text frequently retains gen-1-like statistical properties. "
        f"Depth-2 samples are hardest to classify ({d2['rate']*100:.1f}\\% error rate), "
        f"decreasing monotonically to {d4['rate']*100:.1f}\\% at depth 4, "
        f"confirming that the gen-1$\\to$gen-2 transition is the primary confusion boundary. "
        f"Among generators, {GEN_DISPLAY[hardest['generator']]} shows the highest error rate "
        f"({hardest['err_rate']*100:.1f}\\%), "
        f"while {GEN_DISPLAY[easiest['generator']]} is easiest ({easiest['err_rate']*100:.1f}\\%), "
        f"suggesting that larger models produce gen-2+ text closer to the gen-1 distribution. "
        f"Feature-level analysis reveals that misclassified samples occupy the overlap zone "
        f"with elevated entropy ($\\bar{{H}}$: {binary_res['feat_comp'][0]['incorrect_mean']:.2f} vs.\\ "
        f"{binary_res['feat_comp'][0]['correct_mean']:.2f}, $p<10^{{-300}}$) and lexical diversity "
        f"(TTR: {binary_res['feat_comp'][5]['incorrect_mean']:.3f} vs.\\ "
        f"{binary_res['feat_comp'][5]['correct_mean']:.3f}), "
        f"while tail decay and entropy maximum show no significant difference ($p>0.05$). "
        f"The prediction confidence margin for misclassified samples "
        f"({binary_res['incorrect_margin']:.3f}) is markedly lower than "
        f"for correct predictions ({binary_res['correct_margin']:.3f}), "
        f"confirming these errors concentrate at the decision boundary."
    )
    return para


def main():
    print("Loading data...")
    df = load_data()
    print(f"Loaded {len(df)} rows, {df['model_name'].nunique()} generators")
    print(f"Generators: {sorted(df['model_name'].unique())}")

    # Binary analysis
    print("\nRunning binary LOGO...")
    bin_pred = run_logo(df, task="binary")
    binary_res = analyze_binary(bin_pred)
    print(f"Binary: {binary_res['total']} samples, {binary_res['errors']} errors "
          f"({binary_res['errors']/binary_res['total']*100:.1f}%)")

    # 3-class analysis
    print("\nRunning 3-class LOGO...")
    three_pred = run_logo(df, task="3class")
    three_res = analyze_3class(three_pred)
    print("3-class confusion matrix (%):")
    for i, label in enumerate(three_res["labels"]):
        print(f"  {label}: {three_res['cm_pct'][i]}")

    # Generate LaTeX
    print("\nGenerating LaTeX...")
    tex_binary = gen_latex_table_binary(binary_res)
    tex_depth = gen_latex_table_depth(binary_res)
    tex_features = gen_latex_table_features(binary_res)
    tex_cm = gen_latex_table_3class_cm(three_res)
    tex_para = gen_latex_paragraph(binary_res, three_res)

    # Save everything
    all_tex = "\n\n".join([
        "% === Error Analysis Tables ===",
        "% Table: Binary error breakdown by generator",
        tex_binary,
        "% Table: Error rate by depth",
        tex_depth,
        "% Table: Feature comparison",
        tex_features,
        "% Table: 3-class confusion matrix",
        tex_cm,
        "% Paragraph for appendix",
        tex_para,
    ])

    tex_path = os.path.join(OUT_DIR, "error_analysis_tables.tex")
    with open(tex_path, "w") as f:
        f.write(all_tex)
    print(f"LaTeX saved to {tex_path}")

    # Save full results JSON
    results = {
        "binary": {
            "gen_stats": binary_res["gen_stats"],
            "depth_stats": binary_res["depth_stats"],
            "feat_comp": binary_res["feat_comp"],
            "fn_gen_depth": binary_res["fn_gen_depth"],
            "total": binary_res["total"],
            "errors": binary_res["errors"],
            "correct_margin": binary_res["correct_margin"],
            "incorrect_margin": binary_res["incorrect_margin"],
        },
        "three_class": {
            "cm": three_res["cm"],
            "cm_pct": three_res["cm_pct"],
            "labels": three_res["labels"],
            "per_gen_cm": three_res["per_gen_cm"],
            "error_types": three_res["error_types"],
        },
    }
    json_path = os.path.join(OUT_DIR, "comprehensive_error_analysis.json")
    with open(json_path, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"JSON saved to {json_path}")

    # Print summary
    print(f"\n{'='*70}")
    print("BINARY ERROR ANALYSIS SUMMARY")
    print(f"{'='*70}")
    print(f"\nPer-generator (sorted by error rate):")
    for gs in sorted(binary_res["gen_stats"], key=lambda x: x["err_rate"], reverse=True):
        print(f"  {GEN_DISPLAY[gs['generator']]:15s}  err={gs['err_rate']*100:5.1f}%  "
              f"FP={gs['fp']:4d}  FN={gs['fn']:4d}  F1={gs['f1']:.3f}")

    print(f"\nPer-depth:")
    for ds in binary_res["depth_stats"]:
        print(f"  depth-{ds['depth']}  err={ds['rate']*100:5.1f}%  "
              f"({ds['errors']}/{ds['n']})  [{ds['direction']}]")

    print(f"\nFeature comparison (correct vs incorrect):")
    for fc in binary_res["feat_comp"]:
        sig = "***" if fc["p"] < 0.001 else ("*" if fc["p"] < 0.05 else "n.s.")
        print(f"  {fc['feature']:15s}  correct={fc['correct_mean']:.4f}  "
              f"incorrect={fc['incorrect_mean']:.4f}  Δ={fc['delta']:+.4f}  {sig}")

    print(f"\nConfidence margin: correct={binary_res['correct_margin']:.3f}, "
          f"incorrect={binary_res['incorrect_margin']:.3f}")

    print(f"\n{'='*70}")
    print("3-CLASS CONFUSION MATRIX")
    print(f"{'='*70}")
    for i, label in enumerate(three_res["labels"]):
        print(f"  {label:6s}: {three_res['cm_pct'][i]}")

    print(f"\nFN by depth per generator:")
    for rec in binary_res["fn_gen_depth"]:
        print(f"  {GEN_DISPLAY[rec['generator']]:15s}  depth-{rec['depth']}  "
              f"FN={rec['fn']}/{rec['n']}  rate={rec['fn_rate']*100:.1f}%")


if __name__ == "__main__":
    main()
