"""
instruct_length_confound.py — Length confound analysis for instruct models.

Quantifies how text length varies with depth for instruct models,
determines whether the "direction reversal" in TTR/hapax/entropy
survives length-matching, and computes correct binary F1 (gen-1 vs gen-2+).
"""

import json
import os
import sys

import numpy as np
import pandas as pd
from scipy import stats
from xgboost import XGBClassifier
from sklearn.metrics import f1_score

SEED = 42
N_BOOT = 2000
FEATURES = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max",
            "tail_decay", "ttr", "hapax_ratio"]
XGB_PARAMS = dict(n_estimators=200, max_depth=6, learning_rate=0.1,
                  random_state=SEED, eval_metric="mlogloss",
                  use_label_encoder=False)

PROJECT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_jsonl(path):
    records = []
    with open(path) as f:
        for line in f:
            if line.strip():
                records.append(json.loads(line))
    return pd.DataFrame(records)


def load_features(path):
    return pd.read_csv(path)


def spearman(x, y):
    rho, p = stats.spearmanr(x, y)
    return round(float(rho), 4), float(p)


def bootstrap_se(values, n_boot=N_BOOT, seed=SEED):
    rng = np.random.RandomState(seed)
    n = len(values)
    means = []
    for _ in range(n_boot):
        idx = rng.randint(0, n, size=n)
        means.append(np.mean(values[idx]))
    return float(np.std(means))


def downsample(df, label_col, rng):
    counts = df[label_col].value_counts()
    min_n = counts.min()
    parts = []
    for lbl in sorted(counts.index):
        sub = df[df[label_col] == lbl]
        parts.append(sub.sample(n=min_n, random_state=rng, replace=False))
    return pd.concat(parts, ignore_index=True)


def analyze_model(model_name, gen_path, feat_path):
    print(f"\n{'='*60}")
    print(f"Analyzing: {model_name}")
    print(f"{'='*60}")

    gen_df = load_jsonl(gen_path)
    feat_df = load_features(feat_path)

    # Merge token_count from gen_df into feat_df
    merged = feat_df.merge(gen_df[["id", "token_count"]], on="id", how="left")
    print(f"Records: {len(merged)}, with token_count: {merged['token_count'].notna().sum()}")

    # ---- Part 1: Length distribution ----
    print("\n--- Part 1: Length distribution ---")
    length_per_depth = {}
    for d in sorted(merged["depth"].unique()):
        sub = merged[merged["depth"] == d]
        tc = sub["token_count"]
        length_per_depth[str(int(d))] = {
            "mean": round(float(tc.mean()), 1),
            "median": int(tc.median()),
            "std": round(float(tc.std()), 1),
            "min": int(tc.min()),
            "max": int(tc.max()),
            "n": int(len(tc)),
        }
        print(f"  depth {d}: mean={tc.mean():.1f}, median={tc.median():.0f}, "
              f"std={tc.std():.1f}, range=[{tc.min()}, {tc.max()}]")

    rho_len, p_len = spearman(merged["depth"], merged["token_count"])
    print(f"  length-depth Spearman ρ = {rho_len}, p = {p_len:.2e}")

    # ---- Part 1b: Original Spearman ρ (all data) ----
    print("\n--- Original Spearman ρ (all data) ---")
    original_rho = {}
    for feat in ["ttr", "hapax_ratio", "entropy_mean", "entropy_std", "entropy_min"]:
        if feat in merged.columns:
            r, p = spearman(merged["depth"], merged[feat])
            original_rho[feat] = r
            print(f"  {feat}: ρ = {r}")

    # ---- Part 2: Length-matched subset ----
    print("\n--- Part 2: Length-matched subset ---")

    # Find common length range across all depths
    depth_ranges = {}
    for d in sorted(merged["depth"].unique()):
        sub = merged[merged["depth"] == d]["token_count"]
        depth_ranges[d] = (sub.quantile(0.1), sub.quantile(0.9))
        print(f"  depth {d}: 10th-90th pctile = [{depth_ranges[d][0]:.0f}, {depth_ranges[d][1]:.0f}]")

    # Overlapping range
    lo = max(r[0] for r in depth_ranges.values())
    hi = min(r[1] for r in depth_ranges.values())
    print(f"  Overlapping range: [{lo:.0f}, {hi:.0f}]")

    if lo >= hi:
        print("  WARNING: No overlapping range. Using relaxed bounds.")
        # Use absolute range that at least some samples exist in each depth
        lo = merged[merged["depth"] > 0]["token_count"].quantile(0.25)
        hi = merged[merged["depth"] > 0]["token_count"].quantile(0.75)
        print(f"  Relaxed range (gen-1+ 25th-75th): [{lo:.0f}, {hi:.0f}]")

    matched = merged[(merged["token_count"] >= lo) & (merged["token_count"] <= hi)]
    print(f"  Length-matched samples: {len(matched)} / {len(merged)}")

    matched_n_per_depth = {}
    for d in sorted(matched["depth"].unique()):
        n = len(matched[matched["depth"] == d])
        matched_n_per_depth[str(int(d))] = n
        print(f"    depth {d}: n={n}")

    length_matched_rho = {}
    if len(matched) > 50 and matched["depth"].nunique() >= 2:
        for feat in ["ttr", "hapax_ratio", "entropy_mean", "entropy_std", "entropy_min"]:
            if feat in matched.columns:
                r, p = spearman(matched["depth"], matched[feat])
                length_matched_rho[feat] = r
                print(f"  length-matched {feat}: ρ = {r} (was {original_rho.get(feat, 'N/A')})")
    else:
        print("  Too few matched samples for reliable analysis.")

    # ---- Also: partial correlation (length as covariate) ----
    print("\n--- Partial correlation (controlling for length) ---")
    partial_rho = {}
    for feat in ["ttr", "hapax_ratio", "entropy_mean", "entropy_std", "entropy_min"]:
        if feat in merged.columns:
            # Rank-based partial correlation
            depth_r = stats.rankdata(merged["depth"])
            feat_r = stats.rankdata(merged[feat])
            len_r = stats.rankdata(merged["token_count"])

            # Regress out length from both
            from numpy.polynomial.polynomial import polyfit
            d_res = depth_r - np.polyval(np.polyfit(len_r, depth_r, 1), len_r)
            f_res = feat_r - np.polyval(np.polyfit(len_r, feat_r, 1), len_r)

            r_partial, p_partial = stats.pearsonr(d_res, f_res)
            partial_rho[feat] = round(float(r_partial), 4)
            print(f"  {feat}: partial ρ = {r_partial:.4f} (original = {original_rho.get(feat, 'N/A')})")

    # ---- Part 3: Short text reliability ----
    print("\n--- Part 3: Short text reliability ---")
    short = merged[merged["token_count"] < 50]
    short_stats = {"n_short": int(len(short)), "pct_short": round(100 * len(short) / len(merged), 1)}

    if len(short) > 10:
        for feat in ["ttr", "hapax_ratio", "entropy_mean"]:
            if feat in short.columns:
                vals = short[feat].dropna().values
                se = bootstrap_se(vals)
                short_stats[f"{feat}_mean"] = round(float(vals.mean()), 4)
                short_stats[f"{feat}_se"] = round(se, 4)
                short_stats[f"{feat}_cv"] = round(se / abs(vals.mean()) if vals.mean() != 0 else float("inf"), 4)
                print(f"  {feat} (<50 tok): mean={vals.mean():.4f}, bootstrap SE={se:.4f}, CV={short_stats[f'{feat}_cv']:.4f}")

    # Also check by depth for very short texts
    for d in sorted(merged["depth"].unique()):
        sub_short = merged[(merged["depth"] == d) & (merged["token_count"] < 50)]
        if len(sub_short) > 0:
            print(f"  depth {d}: {len(sub_short)} samples < 50 tokens ({100*len(sub_short)/len(merged[merged['depth']==d]):.1f}%)")

    return {
        "length_per_depth": length_per_depth,
        "length_depth_spearman": {"rho": rho_len, "p": f"{p_len:.2e}"},
        "length_range_used": [float(lo), float(hi)],
        "original_rho": original_rho,
        "length_matched_rho": length_matched_rho,
        "partial_corr_rho": partial_rho,
        "length_matched_n_per_depth": matched_n_per_depth,
        "short_text_stats": short_stats,
    }


def binary_logo_gen1_vs_gen2plus(model_key, feat_instruct_path, feat_all_path):
    """Binary LOGO: gen-1 vs gen-2+ (excluding gen-0)."""
    print(f"\n--- Part 4: Binary gen-1 vs gen-2+ LOGO for {model_key} ---")

    df_all = pd.read_csv(feat_all_path)
    df_inst = pd.read_csv(feat_instruct_path)
    df_inst["model_name"] = model_key

    # Combine
    df_combined = pd.concat([df_all, df_inst], ignore_index=True)

    # Exclude gen-0
    df_combined = df_combined[df_combined["depth"] > 0].copy()

    # Binary label: gen-1 (0) vs gen-2+ (1)
    df_combined["label"] = (df_combined["depth"] >= 2).astype(int)

    generators = sorted(df_combined["model_name"].unique())
    rng = np.random.RandomState(SEED)
    results = {}

    for gen in generators:
        test_df = df_combined[df_combined["model_name"] == gen]
        train_df = df_combined[df_combined["model_name"] != gen]

        if len(test_df) < 10 or test_df["label"].nunique() < 2:
            continue

        train_ds = downsample(train_df, "label", rng)
        clf = XGBClassifier(**{**XGB_PARAMS, "eval_metric": "logloss"})
        clf.fit(train_ds[FEATURES].values, train_ds["label"].values)
        y_pred = clf.predict(test_df[FEATURES].values)
        y_test = test_df["label"].values

        f1 = f1_score(y_test, y_pred, average="macro")
        results[gen] = round(float(f1), 4)
        print(f"  {gen:30s} binary F1 (gen1 vs gen2+) = {f1:.4f}")

    avg_f1 = round(float(np.mean(list(results.values()))), 4) if results else 0
    print(f"  Average: {avg_f1}")

    return results, avg_f1


def main():
    data_dir = os.path.join(PROJECT, "data")

    # ---- Qwen3-0.6B-Instruct ----
    res_06b = analyze_model(
        "Qwen3-0.6B-Instruct",
        os.path.join(data_dir, "qwen3-0.6b-instruct", "generations_shard0.jsonl"),
        os.path.join(data_dir, "features_qwen3-0.6b-instruct.csv"),
    )

    # ---- Qwen3-1.7B-Instruct ----
    res_17b = analyze_model(
        "Qwen3-1.7B-Instruct",
        os.path.join(data_dir, "qwen3-1.7b-instruct", "generations_shard0.jsonl"),
        os.path.join(data_dir, "features_qwen3-1.7b-instruct.csv"),
    )

    # ---- Part 4: Binary LOGO gen-1 vs gen-2+ ----
    feat_all = os.path.join(data_dir, "features_all_models.csv")

    bin_06b, avg_06b = binary_logo_gen1_vs_gen2plus(
        "qwen3-0.6b-instruct",
        os.path.join(data_dir, "features_qwen3-0.6b-instruct.csv"),
        feat_all,
    )
    res_06b["binary_f1_gen1_vs_gen2plus"] = {
        "per_generator": bin_06b,
        "average_f1": avg_06b,
        "instruct_held_out_f1": bin_06b.get("qwen3-0.6b-instruct"),
    }

    bin_17b, avg_17b = binary_logo_gen1_vs_gen2plus(
        "qwen3-1.7b-instruct",
        os.path.join(data_dir, "features_qwen3-1.7b-instruct.csv"),
        feat_all,
    )
    res_17b["binary_f1_gen1_vs_gen2plus"] = {
        "per_generator": bin_17b,
        "average_f1": avg_17b,
        "instruct_held_out_f1": bin_17b.get("qwen3-1.7b-instruct"),
    }

    # ---- Conclusions ----
    def make_conclusion(res):
        len_rho = abs(res["length_depth_spearman"]["rho"])
        confound = len_rho > 0.3

        # Surface reversal: check if original positive ρ survives
        orig_ttr = res["original_rho"].get("ttr", 0)
        orig_hapax = res["original_rho"].get("hapax", res["original_rho"].get("hapax_ratio", 0))
        partial_ttr = res["partial_corr_rho"].get("ttr", orig_ttr)
        partial_hapax = res["partial_corr_rho"].get("hapax_ratio", orig_hapax)

        # "Survives" = partial correlation still positive (same direction as original)
        surface_survives = (partial_ttr > 0.05) and (partial_hapax > 0.05)

        # Entropy reversal
        orig_ent = res["original_rho"].get("entropy_mean", 0)
        partial_ent = res["partial_corr_rho"].get("entropy_mean", orig_ent)
        entropy_survives = (partial_ent > 0.05)

        return {
            "length_confound_confirmed": confound,
            "length_depth_abs_rho": len_rho,
            "surface_reversal_survives_control": surface_survives,
            "surface_partial_rho": {"ttr": partial_ttr, "hapax_ratio": partial_hapax},
            "entropy_reversal_survives_control": entropy_survives,
            "entropy_partial_rho": partial_ent,
        }

    conclusion_06b = make_conclusion(res_06b)
    conclusion_17b = make_conclusion(res_17b)

    # Overall conclusion
    overall = {
        "length_confound_confirmed": conclusion_06b["length_confound_confirmed"] or conclusion_17b["length_confound_confirmed"],
        "surface_reversal_survives_control": conclusion_06b["surface_reversal_survives_control"] and conclusion_17b["surface_reversal_survives_control"],
        "entropy_reversal_survives_control": conclusion_06b["entropy_reversal_survives_control"] and conclusion_17b["entropy_reversal_survives_control"],
    }

    result = {
        "qwen3_06b_instruct": {**res_06b, "conclusion": conclusion_06b},
        "qwen3_17b_instruct": {**res_17b, "conclusion": conclusion_17b},
        "conclusion": overall,
    }

    out_path = os.path.join(PROJECT, "results", "instruct_length_confound.json")
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(f"\n\nResults saved to {out_path}")

    # Print summary
    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    for name, res in [("0.6B-Instruct", res_06b), ("1.7B-Instruct", res_17b)]:
        c = res.get("conclusion", {}) if "conclusion" in res else conclusion_06b if "06b" in name.lower() else conclusion_17b
        print(f"\n{name}:")
        print(f"  Length-depth |ρ| = {c.get('length_depth_abs_rho', 'N/A')}")
        print(f"  Length confound: {'YES' if c['length_confound_confirmed'] else 'NO'}")
        print(f"  Surface reversal survives: {'YES' if c['surface_reversal_survives_control'] else 'NO'}")
        print(f"  Entropy reversal survives: {'YES' if c['entropy_reversal_survives_control'] else 'NO'}")
        bin_info = res.get("binary_f1_gen1_vs_gen2plus", {})
        print(f"  Binary gen1-vs-gen2+ LOGO F1: {bin_info.get('instruct_held_out_f1', 'N/A')}")

    print(f"\nOverall: confound={overall['length_confound_confirmed']}, "
          f"surface_survives={overall['surface_reversal_survives_control']}, "
          f"entropy_survives={overall['entropy_reversal_survives_control']}")


if __name__ == "__main__":
    main()
