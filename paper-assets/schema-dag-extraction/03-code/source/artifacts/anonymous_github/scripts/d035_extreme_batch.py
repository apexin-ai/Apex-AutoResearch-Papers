"""D035: Extreme-batch Δ for 16-rel and 80-pool-16sub experiments.

Mirrors the 80-rel exp2 approach (single lowest-BCS vs highest-BCS batch)
but for the 100-batch bootstrap experiments, takes top/bottom N batches.
"""
import json
import numpy as np
from pathlib import Path

ARTIFACTS = Path("./artifacts")

def load_jsonl(path):
    pairs = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            d = json.loads(line)
            pairs.append(d)
    return pairs

def load_json_array(path):
    with open(path) as f:
        return json.load(f)

def extreme_delta(records, n_extreme=5, n_boot=1000, seed=42):
    sorted_recs = sorted(records, key=lambda x: x["bcs"])
    low_group = sorted_recs[:n_extreme]
    high_group = sorted_recs[-n_extreme:]

    low_accs = np.array([r["accuracy"] for r in low_group])
    high_accs = np.array([r["accuracy"] for r in high_group])
    low_bcs = np.array([r["bcs"] for r in low_group])
    high_bcs = np.array([r["bcs"] for r in high_group])

    delta_obs = (high_accs.mean() - low_accs.mean()) * 100

    rng = np.random.RandomState(seed)
    all_accs = np.array([r["accuracy"] for r in records])
    all_bcs = np.array([r["bcs"] for r in records])
    n = len(records)
    deltas_boot = []
    for _ in range(n_boot):
        idx = rng.randint(0, n, size=n)
        b_bcs = all_bcs[idx]
        b_acc = all_accs[idx]
        order = np.argsort(b_bcs)
        lo_acc = b_acc[order[:n_extreme]].mean()
        hi_acc = b_acc[order[-n_extreme:]].mean()
        deltas_boot.append((hi_acc - lo_acc) * 100)

    deltas_boot = np.array(deltas_boot)
    ci_lo = float(np.percentile(deltas_boot, 2.5))
    ci_hi = float(np.percentile(deltas_boot, 97.5))

    return {
        "n_extreme": n_extreme,
        "n_total_batches": n,
        "delta_extreme_pp": round(float(delta_obs), 2),
        "ci_95": [round(ci_lo, 2), round(ci_hi, 2)],
        "low_group": {
            "n": n_extreme,
            "mean_bcs": round(float(low_bcs.mean()), 4),
            "bcs_range": [round(float(low_bcs.min()), 4), round(float(low_bcs.max()), 4)],
            "mean_acc": round(float(low_accs.mean()), 4),
            "accs": [round(float(a), 4) for a in low_accs],
        },
        "high_group": {
            "n": n_extreme,
            "mean_bcs": round(float(high_bcs.mean()), 4),
            "bcs_range": [round(float(high_bcs.min()), 4), round(float(high_bcs.max()), 4)],
            "mean_acc": round(float(high_accs.mean()), 4),
            "accs": [round(float(a), 4) for a in high_accs],
        },
    }


def main():
    results = {}

    # 1) 16-rel independent (D033)
    p16 = ARTIFACTS / "fewrel_16rel_bootstrap" / "results.json"
    if p16.exists():
        data16 = load_json_array(p16)
        print(f"[16-rel] Loaded {len(data16)} batches from results.json")
        res16 = extreme_delta(data16, n_extreme=5)
        results["16rel_independent"] = res16
        print(f"  Δ_extreme = {res16['delta_extreme_pp']:.2f}pp, CI {res16['ci_95']}")
        print(f"  Low group: BCS {res16['low_group']['bcs_range']}, mean_acc={res16['low_group']['mean_acc']:.4f}")
        print(f"  High group: BCS {res16['high_group']['bcs_range']}, mean_acc={res16['high_group']['mean_acc']:.4f}")

    # 2) 80-pool-16sub
    p80sub = ARTIFACTS / "fewrel_80pool_16sub" / "results_incremental.jsonl"
    if p80sub.exists():
        data80sub = load_jsonl(p80sub)
        print(f"\n[80pool-16sub] Loaded {len(data80sub)} batches from results_incremental.jsonl")
        res80sub = extreme_delta(data80sub, n_extreme=5)
        results["80pool_16sub"] = res80sub
        print(f"  Δ_extreme = {res80sub['delta_extreme_pp']:.2f}pp, CI {res80sub['ci_95']}")
        print(f"  Low group: BCS {res80sub['low_group']['bcs_range']}, mean_acc={res80sub['low_group']['mean_acc']:.4f}")
        print(f"  High group: BCS {res80sub['high_group']['bcs_range']}, mean_acc={res80sub['high_group']['mean_acc']:.4f}")

    # 3) 80-rel reference
    p80 = ARTIFACTS / "fewrel_formal_full" / "eval_exp2.json"
    if p80.exists():
        with open(p80) as f:
            data80 = json.load(f)
        low8 = data80.get("count_8_low_bcs", {})
        high8 = data80.get("count_8_high_bcs", {})
        if low8 and high8:
            delta80 = (high8["accuracy"] - low8["accuracy"]) * 100
            results["80rel_reference"] = {
                "method": "single_greedy_batch",
                "delta_extreme_pp": round(delta80, 2),
                "low_bcs": round(low8["bcs"], 4),
                "low_acc": round(low8["accuracy"], 4),
                "high_bcs": round(high8["bcs"], 4),
                "high_acc": round(high8["accuracy"], 4),
            }
            print(f"\n[80-rel reference] single low vs high batch")
            print(f"  Δ = {delta80:.2f}pp (BCS {low8['bcs']:.4f} → {high8['bcs']:.4f})")

    # Summary table
    print("\n" + "=" * 80)
    print("D035 EXTREME BATCH COMPARISON")
    print("=" * 80)
    headers = ["Metric", "16-rel (D033)", "80pool-16sub", "80-rel (reference)"]
    rows = []

    r16 = results.get("16rel_independent", {})
    r80s = results.get("80pool_16sub", {})
    r80 = results.get("80rel_reference", {})

    rows.append(("Method", "bottom/top 5 of 100", "bottom/top 5 of 100", "1 greedy low vs 1 greedy high"))
    rows.append(("Δ_extreme (pp)", f"{r16.get('delta_extreme_pp', 'N/A')}", f"{r80s.get('delta_extreme_pp', 'N/A')}", f"{r80.get('delta_extreme_pp', 'N/A')}"))

    ci16 = r16.get("ci_95", ["N/A", "N/A"])
    ci80s = r80s.get("ci_95", ["N/A", "N/A"])
    rows.append(("95% CI", f"[{ci16[0]}, {ci16[1]}]", f"[{ci80s[0]}, {ci80s[1]}]", "N/A (single batch)"))

    lo16 = r16.get("low_group", {})
    hi16 = r16.get("high_group", {})
    lo80s = r80s.get("low_group", {})
    hi80s = r80s.get("high_group", {})
    rows.append(("Low BCS range", f"{lo16.get('bcs_range', 'N/A')}", f"{lo80s.get('bcs_range', 'N/A')}", f"{r80.get('low_bcs', 'N/A')}"))
    rows.append(("High BCS range", f"{hi16.get('bcs_range', 'N/A')}", f"{hi80s.get('bcs_range', 'N/A')}", f"{r80.get('high_bcs', 'N/A')}"))
    rows.append(("Low group mean acc", f"{lo16.get('mean_acc', 'N/A')}", f"{lo80s.get('mean_acc', 'N/A')}", f"{r80.get('low_acc', 'N/A')}"))
    rows.append(("High group mean acc", f"{hi16.get('mean_acc', 'N/A')}", f"{hi80s.get('mean_acc', 'N/A')}", f"{r80.get('high_acc', 'N/A')}"))

    col_widths = [max(len(str(row[i])) for row in [headers] + rows) for i in range(len(headers))]
    def fmt_row(row):
        return "| " + " | ".join(str(c).ljust(w) for c, w in zip(row, col_widths)) + " |"

    print(fmt_row(headers))
    print("|" + "|".join("-" * (w + 2) for w in col_widths) + "|")
    for row in rows:
        print(fmt_row(row))

    # Save results
    out_dir = ARTIFACTS / "d035_extreme_batch"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "results.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {out_path}")

if __name__ == "__main__":
    main()
