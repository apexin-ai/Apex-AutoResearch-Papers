"""
Feature Group Ablation: single-group, leave-one-group-out, and full-model
1v2 AUC across C4 / arXiv / Wiki domains.
CPU only.
"""
import csv
import json
import os
import sys
from pathlib import Path

import numpy as np
from sklearn.model_selection import GroupKFold
from sklearn.metrics import roc_auc_score
import lightgbm as lgb

os.environ["CUDA_VISIBLE_DEVICES"] = ""

DOMAINS = {
    "C4":    Path("/root/autodl-tmp/gen-depth-contamination/data/exp_018_llama8b/features.csv"),
    "arXiv": Path("/root/autodl-tmp/gen-depth-contamination/data/exp_024_arxiv/features.csv"),
    "Wiki":  Path("/root/autodl-tmp/gen-depth-contamination/data/exp_023_wiki/features.csv"),
}

FEATURE_GROUPS = {
    "surprisal_base":  ["surp_mean", "surp_std", "surp_skew", "surp_kurt"],
    "surprisal_deriv": ["surp_d1_mean", "surp_d1_std", "surp_d1_skew", "surp_d2_mean", "surp_d2_std"],
    "lexical_diversity": ["ttr", "hapax_ratio", "self_bleu"],
    "freq_distribution": ["freq_kurtosis", "freq_entropy", "low_freq_ratio"],
}

ALL_FEATURES = []
for feats in FEATURE_GROUPS.values():
    ALL_FEATURES.extend(feats)

GROUP_ORDER = ["surprisal_base", "surprisal_deriv", "lexical_diversity", "freq_distribution"]

LGB_PARAMS = dict(
    n_estimators=200, max_depth=6, learning_rate=0.05,
    num_leaves=31, verbose=-1, n_jobs=-1,
)


def load_1v2(csv_path):
    rows = []
    with open(csv_path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            d = int(row["depth"])
            if d in (1, 2):
                rows.append(row)
    if not rows:
        raise ValueError(f"No depth 1 or 2 rows in {csv_path}")

    doc_ids = np.array([int(r["doc_id"]) for r in rows])
    depths = np.array([int(r["depth"]) for r in rows])
    y = (depths == 2).astype(int)

    feat_dict = {}
    for col in ALL_FEATURES:
        feat_dict[col] = np.array([float(r[col]) for r in rows])

    print(f"  Loaded {len(rows)} rows (depth1={np.sum(depths==1)}, depth2={np.sum(depths==2)})", flush=True)
    return doc_ids, y, feat_dict


def run_cv(X, y, groups):
    gkf = GroupKFold(n_splits=5)
    fold_aucs = []
    for train_idx, test_idx in gkf.split(X, y, groups=groups):
        clf = lgb.LGBMClassifier(**LGB_PARAMS)
        clf.fit(X[train_idx], y[train_idx])
        proba = clf.predict_proba(X[test_idx])[:, 1]
        fold_aucs.append(roc_auc_score(y[test_idx], proba))
    return float(np.mean(fold_aucs)), float(np.std(fold_aucs))


def build_X(feat_dict, cols):
    return np.column_stack([feat_dict[c] for c in cols])


def main():
    results = []
    results_json = {}

    for domain, csv_path in DOMAINS.items():
        print(f"\n{'='*50}", flush=True)
        print(f"Domain: {domain} ({csv_path})", flush=True)
        print(f"{'='*50}", flush=True)

        doc_ids, y, feat_dict = load_1v2(csv_path)
        domain_results = {}

        # Full model baseline
        X_full = build_X(feat_dict, ALL_FEATURES)
        auc_full, std_full = run_cv(X_full, y, doc_ids)
        print(f"  Full (15D): AUC = {auc_full:.4f} +/- {std_full:.4f}", flush=True)
        results.append({
            "domain": domain, "ablation_type": "full",
            "feature_group": "all_15d", "1v2_auc": round(auc_full, 4),
            "1v2_auc_std": round(std_full, 4),
        })
        domain_results["full"] = {"auc": round(auc_full, 4), "std": round(std_full, 4)}

        # Single-group ablation
        print(f"\n  --- Single-group ablation ---", flush=True)
        domain_results["single"] = {}
        for gname in GROUP_ORDER:
            cols = FEATURE_GROUPS[gname]
            X = build_X(feat_dict, cols)
            auc, std = run_cv(X, y, doc_ids)
            print(f"  {gname} ({len(cols)}D): AUC = {auc:.4f} +/- {std:.4f}", flush=True)
            results.append({
                "domain": domain, "ablation_type": "single",
                "feature_group": gname, "1v2_auc": round(auc, 4),
                "1v2_auc_std": round(std, 4),
            })
            domain_results["single"][gname] = {"auc": round(auc, 4), "std": round(std, 4)}

        # Leave-one-group-out ablation
        print(f"\n  --- Leave-one-group-out ablation ---", flush=True)
        domain_results["leave_one_out"] = {}
        for gname in GROUP_ORDER:
            remaining_cols = []
            for other_gname in GROUP_ORDER:
                if other_gname != gname:
                    remaining_cols.extend(FEATURE_GROUPS[other_gname])
            X = build_X(feat_dict, remaining_cols)
            auc, std = run_cv(X, y, doc_ids)
            drop = auc_full - auc
            print(f"  w/o {gname} ({len(remaining_cols)}D): AUC = {auc:.4f} +/- {std:.4f}  (drop={drop:+.4f})", flush=True)
            results.append({
                "domain": domain, "ablation_type": "leave_one_out",
                "feature_group": gname, "1v2_auc": round(auc, 4),
                "1v2_auc_std": round(std, 4),
                "auc_drop": round(drop, 4),
            })
            domain_results["leave_one_out"][gname] = {
                "auc": round(auc, 4), "std": round(std, 4), "drop": round(drop, 4),
            }

        results_json[domain] = domain_results

    # Save CSV
    out_dir = Path("/root/autodl-tmp/gen-depth-contamination/results/feature_ablation")
    out_dir.mkdir(parents=True, exist_ok=True)

    csv_path = out_dir / "ablation_results.csv"
    with open(csv_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["domain", "ablation_type", "feature_group", "1v2_auc", "1v2_auc_std", "auc_drop"])
        writer.writeheader()
        for r in results:
            row = {k: r.get(k, "") for k in writer.fieldnames}
            writer.writerow(row)
    print(f"\nCSV saved: {csv_path}", flush=True)

    # Save JSON
    json_path = out_dir / "ablation_results.json"
    with open(json_path, "w") as f:
        json.dump(results_json, f, indent=2)
    print(f"JSON saved: {json_path}", flush=True)

    # Generate LaTeX table
    latex = generate_latex_table(results_json)
    latex_path = out_dir / "latex_table.tex"
    with open(latex_path, "w") as f:
        f.write(latex)
    print(f"LaTeX saved: {latex_path}", flush=True)

    # Generate heatmap
    fig_path = out_dir / "fig_feature_ablation"
    generate_heatmap(results_json, fig_path)

    print("\nDone.", flush=True)
    print(json.dumps(results_json, indent=2), flush=True)


def generate_latex_table(results_json):
    domains = ["C4", "arXiv", "Wiki"]
    lines = []
    lines.append(r"\begin{table}[t]")
    lines.append(r"\centering")
    lines.append(r"\small")
    lines.append(r"\caption{Feature group ablation for 1\,vs.\,2 classification (AUC). "
                 r"\textbf{Single}: using only features from one group. "
                 r"\textbf{Leave-one-out}: removing one group from the full 15D feature set. "
                 r"$\Delta$ denotes the AUC drop from the full model.}")
    lines.append(r"\label{tab:feature_ablation}")
    lines.append(r"\begin{tabular}{l ccc ccc}")
    lines.append(r"\toprule")
    lines.append(r"& \multicolumn{3}{c}{\textbf{Single Group}} & \multicolumn{3}{c}{\textbf{Leave-One-Out ($\Delta$)}} \\")
    lines.append(r"\cmidrule(lr){2-4} \cmidrule(lr){5-7}")
    lines.append(r"Feature Group & C4 & arXiv & Wiki & C4 & arXiv & Wiki \\")
    lines.append(r"\midrule")

    group_labels = {
        "surprisal_base": r"Surprisal (base)",
        "surprisal_deriv": r"Surprisal (deriv.)",
        "lexical_diversity": r"Lexical diversity",
        "freq_distribution": r"Freq. distribution",
    }

    for gname in GROUP_ORDER:
        label = group_labels[gname]
        single_vals = []
        loo_vals = []
        for dom in domains:
            s = results_json[dom]["single"][gname]["auc"]
            single_vals.append(f"{s:.3f}")
            d = results_json[dom]["leave_one_out"][gname]
            drop = d["drop"]
            sign = "+" if drop < 0 else r"$-$" if drop > 0 else ""
            if drop > 0:
                loo_vals.append(f"{d['auc']:.3f} ({sign}{abs(drop):.3f})")
            elif drop < 0:
                loo_vals.append(f"{d['auc']:.3f} ({sign}{abs(drop):.3f})")
            else:
                loo_vals.append(f"{d['auc']:.3f} (0.000)")
        row = f"{label} & {' & '.join(single_vals)} & {' & '.join(loo_vals)} \\\\"
        lines.append(row)

    lines.append(r"\midrule")
    full_vals = []
    for dom in domains:
        full_vals.append(f"{results_json[dom]['full']['auc']:.3f}")
    lines.append(f"Full (15D) & {' & '.join(full_vals)} & \\multicolumn{{3}}{{c}}{{---}} \\\\")
    lines.append(r"\bottomrule")
    lines.append(r"\end{tabular}")
    lines.append(r"\end{table}")
    return "\n".join(lines)


def generate_heatmap(results_json, out_path):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import matplotlib.colors as mcolors

    domains = ["C4", "arXiv", "Wiki"]
    groups = GROUP_ORDER
    group_labels = ["Surp. (base)", "Surp. (deriv.)", "Lex. diversity", "Freq. dist."]

    single_matrix = np.zeros((len(domains), len(groups)))
    loo_matrix = np.zeros((len(domains), len(groups)))

    for i, dom in enumerate(domains):
        for j, gname in enumerate(groups):
            single_matrix[i, j] = results_json[dom]["single"][gname]["auc"]
            loo_matrix[i, j] = results_json[dom]["leave_one_out"][gname]["auc"]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 2.8), gridspec_kw={"wspace": 0.35})

    all_vals = np.concatenate([single_matrix.ravel(), loo_matrix.ravel()])
    vmin = max(0.45, np.min(all_vals) - 0.02)
    vmax = min(1.0, np.max(all_vals) + 0.02)

    cmap = plt.cm.YlOrRd

    for ax, matrix, title in [
        (ax1, single_matrix, "Single Group"),
        (ax2, loo_matrix, "Leave-One-Out"),
    ]:
        im = ax.imshow(matrix, cmap=cmap, aspect="auto", vmin=vmin, vmax=vmax)
        ax.set_xticks(range(len(groups)))
        ax.set_xticklabels(group_labels, rotation=30, ha="right", fontsize=8)
        ax.set_yticks(range(len(domains)))
        ax.set_yticklabels(domains, fontsize=9)
        ax.set_title(title, fontsize=10, fontweight="bold", pad=6)

        for i in range(len(domains)):
            for j in range(len(groups)):
                val = matrix[i, j]
                color = "white" if val > (vmin + vmax) / 2 else "black"
                ax.text(j, i, f"{val:.3f}", ha="center", va="center",
                        fontsize=8, fontweight="bold", color=color)

    cbar = fig.colorbar(im, ax=[ax1, ax2], shrink=0.8, pad=0.02)
    cbar.set_label("1 vs. 2 AUC", fontsize=9)
    cbar.ax.tick_params(labelsize=8)

    # Add full-model reference lines as text
    for i, dom in enumerate(domains):
        full_auc = results_json[dom]["full"]["auc"]
        ax2.annotate(f"Full: {full_auc:.3f}", xy=(len(groups) - 0.5, i),
                     xytext=(len(groups) + 0.1, i),
                     fontsize=7, va="center", color="gray",
                     annotation_clip=False)

    plt.tight_layout()
    for ext in ["pdf", "png"]:
        fig.savefig(f"{out_path}.{ext}", dpi=300, bbox_inches="tight")
        print(f"Figure saved: {out_path}.{ext}", flush=True)
    plt.close()


if __name__ == "__main__":
    main()
