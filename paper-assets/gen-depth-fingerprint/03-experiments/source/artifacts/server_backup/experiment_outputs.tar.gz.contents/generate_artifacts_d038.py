"""
D038: Generate all 5 paper data artifacts.
Pure CPU, no GPU needed.
"""
import json
import os
from collections import Counter
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import spearmanr

ROOT = Path("/root/gen-depth-fingerprint")
DATA = ROOT / "data"
RESULTS = ROOT / "results"

FEATURES = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max",
            "tail_decay", "ttr", "hapax_ratio"]
ALL_6 = ["pythia-2.8b", "pythia-1b", "olmo-2-1b", "qwen3-0.6b", "qwen3-1.7b", "qwen3-8b"]
ALL_8 = ALL_6 + ["llama-3.2-3b", "mistral-7b-v0.3"]


def load_8gen_data():
    """Load all 8 generators' feature data."""
    df_base = pd.read_csv(DATA / "features_all_models.csv")
    new_gens = [
        ("llama-3.2-3b", DATA / "llama-3.2-3b" / "features_pythia410m.jsonl"),
        ("mistral-7b-v0.3", DATA / "mistral-7b-v0.3" / "features_pythia410m.jsonl"),
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
    return df


# ============================================================
# Artifact 1: 8gen_logo_results.json — reformat
# ============================================================
def artifact1_logo_results():
    print("=" * 60)
    print("Artifact 1: 8gen_logo_results.json")
    existing = json.load(open(RESULTS / "8gen_logo_results.json"))

    output = {
        "overall": {
            "3class_f1": existing["overall_3class_f1"],
            "binary_f1": existing["overall_binary_f1"],
        },
        "per_generator": {},
        "metadata": {
            "n_generators": existing["n_generators"],
            "n_total_rows": existing["n_total_rows"],
            "xgb_params": "n_estimators=200, max_depth=6, lr=0.1, 7 features",
            "binary_definition": "gen-1 vs gen-2+ only (gen-0 excluded)",
            "baseline_6gen_3class_f1": existing["baseline_6gen_3class_f1"],
            "delta_8gen_vs_6gen": existing["delta_8gen_vs_6gen"],
        },
    }

    for gen in ALL_8:
        r3 = existing["per_generator_3class"].get(gen, {})
        rb = existing["per_generator_binary"].get(gen, {})
        output["per_generator"][gen] = {
            "3class_f1": r3.get("macro_f1"),
            "3class_ci": [r3.get("ci_lower"), r3.get("ci_upper")],
            "binary_f1": rb.get("binary_f1"),
            "binary_ci": [rb.get("ci_lower"), rb.get("ci_upper")],
            "per_class_f1": {
                "gen-0": r3.get("gen-0_f1"),
                "gen-1": r3.get("gen-1_f1"),
                "gen-2+": r3.get("gen-2+_f1"),
            },
        }

    out_path = RESULTS / "8gen_logo_results.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"  Saved: {out_path}")
    return output


# ============================================================
# Artifact 2: 8gen_pooled_rho.json
# ============================================================
def artifact2_pooled_rho(df):
    print("=" * 60)
    print("Artifact 2: 8gen_pooled_rho.json")

    pooled = {}
    for feat in FEATURES:
        rho, _ = spearmanr(df[feat].values, df["depth"].values)
        pooled[feat] = round(float(rho), 4)

    # balanced version: equal samples per depth
    depths = sorted(df["depth"].unique())
    min_count = min(len(df[df["depth"] == d]) for d in depths)
    rng = np.random.RandomState(42)
    balanced_parts = []
    for d in depths:
        sub = df[df["depth"] == d]
        balanced_parts.append(sub.sample(n=min_count, random_state=rng, replace=False))
    df_bal = pd.concat(balanced_parts, ignore_index=True)

    pooled_balanced = {}
    for feat in FEATURES:
        rho, _ = spearmanr(df_bal[feat].values, df_bal["depth"].values)
        pooled_balanced[feat] = round(float(rho), 4)

    output = {
        "pooled": pooled,
        "pooled_balanced": pooled_balanced,
        "n_samples_pooled": len(df),
        "n_samples_balanced": len(df_bal),
        "n_per_depth_balanced": int(min_count),
        "generators": ALL_8,
    }

    out_path = RESULTS / "8gen_pooled_rho.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"  Saved: {out_path}")
    return output


# ============================================================
# Artifact 3: 8gen_per_gen_spearman.json
# ============================================================
def artifact3_per_gen_spearman(df):
    print("=" * 60)
    print("Artifact 3: 8gen_per_gen_spearman.json")

    per_gen = {}
    for gen in ALL_8:
        sub = df[df["model_name"] == gen]
        gen_rhos = {}
        for feat in FEATURES:
            rho, _ = spearmanr(sub[feat].values, sub["depth"].values)
            gen_rhos[feat] = round(float(rho), 4)
        per_gen[gen] = gen_rhos

    # Median across generators
    median_rhos = {}
    for feat in FEATURES:
        vals = [per_gen[g][feat] for g in ALL_8]
        median_rhos[feat] = round(float(np.median(vals)), 4)

    output = dict(per_gen)
    output["_median"] = median_rhos
    output["_generators"] = ALL_8

    out_path = RESULTS / "8gen_per_gen_spearman.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"  Saved: {out_path}")
    return output


# ============================================================
# Artifact 4: degeneration_rates.json
# ============================================================
def compute_repeated_4gram_ratio(text):
    words = text.lower().split()
    if len(words) < 4:
        return 0.0
    ngrams = [tuple(words[i:i+4]) for i in range(len(words) - 3)]
    counter = Counter(ngrams)
    repeated = sum(c - 1 for c in counter.values() if c > 1)
    return repeated / len(ngrams)


def compute_degen_rates_from_generations(gen_dir, gen_name):
    """Compute per-depth degeneration rate from generation files."""
    gen_file = gen_dir / "generations_shard0.jsonl"
    if not gen_file.exists():
        print(f"  WARNING: {gen_file} not found")
        return None

    by_depth = {}
    with open(gen_file) as f:
        for line in f:
            if not line.strip():
                continue
            rec = json.loads(line)
            d = rec.get("depth", rec.get("gen_depth", -1))
            text = rec["text"]
            ratio = compute_repeated_4gram_ratio(text)
            if d not in by_depth:
                by_depth[d] = {"total": 0, "degen": 0}
            by_depth[d]["total"] += 1
            if ratio > 0.5:
                by_depth[d]["degen"] += 1

    result = {}
    total_all = 0
    degen_all = 0
    for d in sorted(by_depth.keys()):
        t = by_depth[d]["total"]
        dg = by_depth[d]["degen"]
        result[f"d{d}"] = round(dg / t * 100, 1) if t > 0 else 0.0
        total_all += t
        degen_all += dg
    result["total"] = round(degen_all / total_all * 100, 1) if total_all > 0 else 0.0
    return result


def artifact4_degeneration_rates():
    print("=" * 60)
    print("Artifact 4: degeneration_rates.json")

    output = {}

    # 6 original generators from filter stats
    filter_stats = json.load(open(RESULTS / "original_6gen_filter_stats.json"))
    gen_name_map = {
        "Pythia-2.8B": "pythia-2.8b",
        "Pythia-1B": "pythia-1b",
        "OLMo-2-1B": "olmo-2-1b",
        "Qwen3-0.6B": "qwen3-0.6b",
        "Qwen3-1.7B": "qwen3-1.7b",
        "Qwen3-8B": "qwen3-8b",
    }

    for display_name, key in gen_name_map.items():
        stats = filter_stats[display_name]
        result = {}
        for d_str, d_info in stats["by_depth"].items():
            t = d_info["total"]
            fg = d_info["filtered"]
            result[f"d{d_str}"] = round(fg / t * 100, 1) if t > 0 else 0.0
        result["total"] = round(stats["filtered"] / stats["total"] * 100, 1)
        output[key] = result

    # Llama and Mistral from generation files
    for gen_name in ["llama-3.2-3b", "mistral-7b-v0.3"]:
        gen_dir = DATA / gen_name
        rates = compute_degen_rates_from_generations(gen_dir, gen_name)
        if rates:
            output[gen_name] = rates

    out_path = RESULTS / "degeneration_rates.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"  Saved: {out_path}")
    return output


# ============================================================
# Artifact 5: rp_lofo_results.json — check and supplement
# ============================================================
def artifact5_rp_lofo():
    print("=" * 60)
    print("Artifact 5: rp_lofo_results.json — checking completeness")

    existing = json.load(open(RESULTS / "rp_lofo_results.json"))

    required_keys = ["test_A_llama_rp11", "test_B_llama_rp10_filtered", "train_info"]
    missing = [k for k in required_keys if k not in existing]

    if missing:
        print(f"  MISSING keys: {missing}")
        # Try to merge from preliminary
        prelim = json.load(open(RESULTS / "rp_lofo_preliminary.json"))
        for k in missing:
            if k in prelim:
                existing[k] = prelim[k]

    # Check Test A has per_class and confusion matrix
    test_a = existing.get("test_A_llama_rp11", {})
    has_per_class_a = "per_class" in test_a or "per_class_f1" in test_a
    has_cm_a = "confusion_matrix" in test_a

    # Check Test B
    test_b = existing.get("test_B_llama_rp10_filtered", {})
    has_per_class_b = "per_class" in test_b or "per_class_f1" in test_b
    has_cm_b = "confusion_matrix" in test_b

    print(f"  Test A: 3class_f1={test_a.get('3class_f1')}, binary_f1={test_a.get('binary_f1')}")
    print(f"    per_class: {'YES' if has_per_class_a else 'NO'}, confusion_matrix: {'YES' if has_cm_a else 'NO'}")
    print(f"  Test B: 3class_f1={test_b.get('3class_f1')}, binary_f1={test_b.get('binary_f1')}")
    print(f"    per_class: {'YES' if has_per_class_b else 'NO'}, confusion_matrix: {'YES' if has_cm_b else 'NO'}")

    # If incomplete, supplement from preliminary
    if not has_per_class_a or not has_cm_a:
        prelim = json.load(open(RESULTS / "rp_lofo_preliminary.json"))
        prelim_3c = prelim.get("three_class", {})
        if not has_per_class_a and "per_class_f1" in prelim_3c:
            existing["test_A_llama_rp11"]["per_class"] = prelim_3c["per_class_f1"]
        if not has_cm_a and "confusion_matrix" in prelim_3c:
            existing["test_A_llama_rp11"]["confusion_matrix"] = prelim_3c["confusion_matrix"]

    out_path = RESULTS / "rp_lofo_results.json"
    with open(out_path, "w") as f:
        json.dump(existing, f, indent=2, ensure_ascii=False)
    print(f"  Saved: {out_path}")
    return existing


# ============================================================
# Main
# ============================================================
def main():
    print("Loading 8-gen data...")
    df = load_8gen_data()
    print(f"  Loaded {len(df)} rows, generators: {sorted(df['model_name'].unique())}")
    print(f"  Per-gen counts:")
    for gen in ALL_8:
        n = len(df[df["model_name"] == gen])
        print(f"    {gen}: {n}")

    a1 = artifact1_logo_results()
    a2 = artifact2_pooled_rho(df)
    a3 = artifact3_per_gen_spearman(df)
    a4 = artifact4_degeneration_rates()
    a5 = artifact5_rp_lofo()

    # ========== SUMMARY ==========
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)

    # 1. Per-generator binary F1 table
    print("\n--- Per-Generator Binary F1 ---")
    print(f"{'Generator':20s} {'Binary F1':>10s} {'95% CI':>22s} {'3class F1':>10s}")
    print("-" * 65)
    for gen in ALL_8:
        pg = a1["per_generator"][gen]
        bf1 = pg["binary_f1"]
        bci = pg["binary_ci"]
        cf1 = pg["3class_f1"]
        bf_str = f"{bf1:.4f}" if bf1 else "N/A"
        ci_str = f"[{bci[0]:.4f}, {bci[1]:.4f}]" if bci[0] else "N/A"
        cf_str = f"{cf1:.4f}" if cf1 else "N/A"
        print(f"{gen:20s} {bf_str:>10s} {ci_str:>22s} {cf_str:>10s}")
    print(f"{'OVERALL':20s} {a1['overall']['binary_f1']:10.4f} {'':22s} {a1['overall']['3class_f1']:10.4f}")

    # 2. Pooled ρ ranking
    print("\n--- 7 Features Pooled Spearman ρ (sorted by |ρ|) ---")
    sorted_feats = sorted(a2["pooled"].items(), key=lambda x: abs(x[1]), reverse=True)
    for feat, rho in sorted_feats:
        bal_rho = a2["pooled_balanced"][feat]
        print(f"  {feat:16s}  ρ={rho:+.4f}  (balanced: {bal_rho:+.4f})")

    # 3. Per-gen Spearman median
    print("\n--- Per-Gen Spearman Median ---")
    med = a3["_median"]
    sorted_med = sorted(med.items(), key=lambda x: abs(x[1]), reverse=True)
    for feat, rho in sorted_med:
        print(f"  {feat:16s}  median ρ={rho:+.4f}")

    # 4. Degeneration rates summary
    print("\n--- Degeneration Rates (%) ---")
    print(f"{'Generator':20s} {'d0':>6s} {'d1':>6s} {'d2':>6s} {'d3':>6s} {'d4':>6s} {'total':>6s}")
    print("-" * 60)
    for gen in ALL_8:
        if gen in a4:
            r = a4[gen]
            print(f"{gen:20s} {r.get('d0',0):6.1f} {r.get('d1',0):6.1f} {r.get('d2',0):6.1f} {r.get('d3',0):6.1f} {r.get('d4',0):6.1f} {r.get('total',0):6.1f}")

    print("\nAll 5 artifacts saved to /root/gen-depth-fingerprint/results/")


if __name__ == "__main__":
    main()
