"""OLMo-Instruct length confound analysis — same method as Qwen instruct."""
import json, os, sys
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
                  random_state=SEED, eval_metric="logloss",
                  use_label_encoder=False)
PROJECT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_jsonl(path):
    records = []
    with open(path) as f:
        for line in f:
            if line.strip():
                records.append(json.loads(line))
    return pd.DataFrame(records)


def spearman(x, y):
    rho, p = stats.spearmanr(x, y)
    return round(float(rho), 4), float(p)


def bootstrap_se(values, n_boot=N_BOOT, seed=SEED):
    rng = np.random.RandomState(seed)
    n = len(values)
    means = [np.mean(values[rng.randint(0, n, size=n)]) for _ in range(n_boot)]
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
    feat_df = pd.read_csv(feat_path)
    merged = feat_df.merge(gen_df[["id", "token_count"]], on="id", how="left")
    print(f"Records: {len(merged)}, with token_count: {merged['token_count'].notna().sum()}")

    # Part 1: Length distribution
    length_per_depth = {}
    for d in sorted(merged["depth"].unique()):
        tc = merged[merged["depth"] == d]["token_count"]
        length_per_depth[str(int(d))] = {
            "mean": round(float(tc.mean()), 1),
            "median": int(tc.median()),
            "std": round(float(tc.std()), 1),
            "min": int(tc.min()),
            "max": int(tc.max()),
            "n": int(len(tc)),
        }
        print(f"  depth {d}: mean={tc.mean():.1f}, median={tc.median():.0f}, std={tc.std():.1f}")

    rho_len, p_len = spearman(merged["depth"], merged["token_count"])
    print(f"  length-depth Spearman rho = {rho_len}, p = {p_len:.2e}")

    # Part 1b: Original Spearman rho
    original_rho = {}
    for feat in ["ttr", "hapax_ratio", "entropy_mean", "entropy_std", "entropy_min"]:
        if feat in merged.columns:
            r, p = spearman(merged["depth"], merged[feat])
            original_rho[feat] = r
            print(f"  {feat}: rho = {r}")

    # Part 2: Length-matched subset
    depth_ranges = {}
    for d in sorted(merged["depth"].unique()):
        sub = merged[merged["depth"] == d]["token_count"]
        depth_ranges[d] = (sub.quantile(0.1), sub.quantile(0.9))
        print(f"  depth {d}: 10-90 pctile = [{depth_ranges[d][0]:.0f}, {depth_ranges[d][1]:.0f}]")

    lo = max(r[0] for r in depth_ranges.values())
    hi = min(r[1] for r in depth_ranges.values())
    print(f"  Overlapping range: [{lo:.0f}, {hi:.0f}]")

    if lo >= hi:
        lo = merged[merged["depth"] > 0]["token_count"].quantile(0.25)
        hi = merged[merged["depth"] > 0]["token_count"].quantile(0.75)
        print(f"  Relaxed range (gen-1+ 25-75th): [{lo:.0f}, {hi:.0f}]")

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
                print(f"  length-matched {feat}: rho = {r} (was {original_rho.get(feat)})")

    # Part 2b: Partial correlation
    partial_rho = {}
    for feat in ["ttr", "hapax_ratio", "entropy_mean", "entropy_std", "entropy_min"]:
        if feat in merged.columns:
            depth_r = stats.rankdata(merged["depth"])
            feat_r = stats.rankdata(merged[feat])
            len_r = stats.rankdata(merged["token_count"])
            d_res = depth_r - np.polyval(np.polyfit(len_r, depth_r, 1), len_r)
            f_res = feat_r - np.polyval(np.polyfit(len_r, feat_r, 1), len_r)
            r_partial, _ = stats.pearsonr(d_res, f_res)
            partial_rho[feat] = round(float(r_partial), 4)
            print(f"  {feat}: partial rho = {r_partial:.4f} (original = {original_rho.get(feat)})")

    # Part 3: Short text reliability
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
    print(f"\n--- Binary gen-1 vs gen-2+ LOGO for {model_key} ---")
    df_all = pd.read_csv(feat_all_path)
    df_inst = pd.read_csv(feat_instruct_path)
    df_inst["model_name"] = model_key

    df_combined = pd.concat([df_all, df_inst], ignore_index=True)
    df_combined = df_combined[df_combined["depth"] > 0].copy()
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
        clf = XGBClassifier(**XGB_PARAMS)
        clf.fit(train_ds[FEATURES].values, train_ds["label"].values)
        y_pred = clf.predict(test_df[FEATURES].values)
        f1 = f1_score(test_df["label"].values, y_pred, average="macro")
        results[gen] = round(float(f1), 4)
        print(f"  {gen:30s} F1 = {f1:.4f}")

    avg_f1 = round(float(np.mean(list(results.values()))), 4) if results else 0
    print(f"  Average: {avg_f1}")
    return results, avg_f1


def make_conclusion(res):
    len_rho = abs(res["length_depth_spearman"]["rho"])
    confound = len_rho > 0.3
    partial_ttr = res["partial_corr_rho"].get("ttr", 0)
    partial_hapax = res["partial_corr_rho"].get("hapax_ratio", 0)
    surface_survives = (partial_ttr > 0.05) and (partial_hapax > 0.05)
    partial_ent = res["partial_corr_rho"].get("entropy_mean", 0)
    entropy_survives = (partial_ent > 0.05)

    if not confound:
        depth_signal = "strong_independent"
    elif surface_survives and entropy_survives:
        depth_signal = "survives_length_control"
    elif surface_survives or entropy_survives:
        depth_signal = "partially_survives"
    else:
        depth_signal = "dominated_by_length"

    return {
        "length_confound_confirmed": confound,
        "length_depth_abs_rho": len_rho,
        "surface_reversal_survives_control": surface_survives,
        "surface_partial_rho": {"ttr": partial_ttr, "hapax_ratio": partial_hapax},
        "entropy_reversal_survives_control": entropy_survives,
        "entropy_partial_rho": partial_ent,
        "length_confound_dominates": not (surface_survives or entropy_survives),
        "depth_signal_after_control": depth_signal,
    }


def main():
    data_dir = os.path.join(PROJECT, "data")

    # Analyze OLMo-Instruct
    res = analyze_model(
        "OLMo-2-0425-1B-Instruct",
        os.path.join(data_dir, "olmo-2-0425-1b-instruct", "generations_shard0.jsonl"),
        os.path.join(data_dir, "features_olmo-2-0425-1b-instruct.csv"),
    )

    # Binary LOGO
    feat_all = os.path.join(data_dir, "features_all_models.csv")
    bin_res, avg_f1 = binary_logo_gen1_vs_gen2plus(
        "olmo-2-0425-1b-instruct",
        os.path.join(data_dir, "features_olmo-2-0425-1b-instruct.csv"),
        feat_all,
    )
    res["binary_f1_gen1_vs_gen2plus"] = {
        "per_generator": bin_res,
        "average_f1": avg_f1,
        "instruct_held_out_f1": bin_res.get("olmo-2-0425-1b-instruct"),
    }

    # Conclusion
    conclusion = make_conclusion(res)
    res["conclusion"] = conclusion

    # Load existing JSON and append
    out_path = os.path.join(PROJECT, "results", "instruct_length_confound.json")
    with open(out_path) as f:
        existing = json.load(f)

    existing["olmo_2_0425_1b_instruct"] = res

    # Update overall conclusion
    all_conclusions = []
    for k, v in existing.items():
        if k == "conclusion":
            continue
        if isinstance(v, dict) and "conclusion" in v:
            all_conclusions.append(v["conclusion"])

    existing["conclusion"] = {
        "length_confound_confirmed": any(c.get("length_confound_confirmed", False) for c in all_conclusions),
        "surface_reversal_survives_control": all(c.get("surface_reversal_survives_control", False) for c in all_conclusions),
        "entropy_reversal_survives_control": all(c.get("entropy_reversal_survives_control", False) for c in all_conclusions),
    }

    with open(out_path, "w") as f:
        json.dump(existing, f, indent=2, ensure_ascii=False)

    # Print summary
    print(f"\n{'='*60}")
    print("OLMo-Instruct Length Confound Summary")
    print(f"{'='*60}")
    print(f"  Length-depth |rho| = {conclusion['length_depth_abs_rho']}")
    print(f"  Length confound: {'YES' if conclusion['length_confound_confirmed'] else 'NO'}")
    print(f"  Surface reversal survives: {'YES' if conclusion['surface_reversal_survives_control'] else 'NO'}")
    print(f"  Entropy reversal survives: {'YES' if conclusion['entropy_reversal_survives_control'] else 'NO'}")
    print(f"  Length confound dominates: {'YES' if conclusion['length_confound_dominates'] else 'NO'}")
    print(f"  Depth signal after control: {conclusion['depth_signal_after_control']}")
    print(f"  Binary LOGO F1 (held-out): {res['binary_f1_gen1_vs_gen2plus']['instruct_held_out_f1']}")
    print(f"\nResults saved to {out_path}")


if __name__ == "__main__":
    main()
