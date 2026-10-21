"""exp-011: NLI Threshold Sensitivity Analysis.

Analyzes how NLI threshold choice affects pass rate and downstream metrics
across style axes. Key question: is the 0.90 threshold well-calibrated,
or are we on a cliff edge?

Input:  verified*.jsonl files (with nli_cf, passed_cf, original_{axis})
Output: Console table + optional CSV
"""

import argparse
import json
import os
import statistics


def load_records(path: str) -> list[dict]:
    records = []
    with open(path) as f:
        for line in f:
            if line.strip():
                records.append(json.loads(line))
    return records


def sensitivity_analysis(records: list[dict], axis: str, thresholds: list[float],
                         pairwise_records: list[dict] | None = None):
    axis_config = {
        "formality": {"field": "original_formality", "poles": ("formal", "casual")},
        "verbosity": {"field": "original_verbosity", "poles": ("verbose", "concise")},
        "tone": {"field": "original_tone", "poles": ("assertive", "hedging")},
        "register": {"field": "original_register", "poles": ("academic", "conversational")},
    }
    cfg = axis_config.get(axis)
    if not cfg:
        print(f"Unknown axis: {axis}")
        return

    field = cfg["field"]
    pole_a, pole_b = cfg["poles"]

    pairwise_map = {}
    if pairwise_records:
        wins_key = f"{pole_a}_wins"
        for pr in pairwise_records:
            if pr.get("consistent") is True and pr.get(wins_key) is not None:
                pairwise_map[pr["id"]] = pr[wins_key]

    print(f"\n{'='*80}")
    print(f"  NLI Threshold Sensitivity — {axis} axis (n={len(records)})")
    print(f"{'='*80}")
    print(f"  {'Threshold':<12} {'N pass':<10} {'Pass%':<10} {'NLI mean':<12} {'BS mean':<12}", end="")
    if pairwise_map:
        print(f" {'PW N':<8} {'PW win%':<10} {'PW p':<10}", end="")
    print()
    print(f"  {'-'*76}")

    rows = []
    for thresh in thresholds:
        passed = [r for r in records if r.get("nli_cf", 0) >= thresh]
        n_pass = len(passed)
        pass_rate = n_pass / len(records) if records else 0

        nli_vals = [r["nli_cf"] for r in passed if r.get("nli_cf") is not None]
        bs_vals = [r["bertscore_cf"] for r in passed if r.get("bertscore_cf") is not None]
        nli_mean = statistics.mean(nli_vals) if nli_vals else 0
        bs_mean = statistics.mean(bs_vals) if bs_vals else 0

        row = {
            "threshold": thresh,
            "n_pass": n_pass,
            "pass_rate": pass_rate,
            "nli_mean": nli_mean,
            "bs_mean": bs_mean,
        }

        print(f"  {thresh:<12.2f} {n_pass:<10} {pass_rate*100:<10.1f} {nli_mean:<12.4f} {bs_mean:<12.4f}", end="")

        if pairwise_map:
            pw_ids = [r["id"] for r in passed if r["id"] in pairwise_map]
            pw_n = len(pw_ids)
            if pw_n > 0:
                pw_wins = sum(1 for rid in pw_ids if pairwise_map[rid] is True)
                pw_rate = pw_wins / pw_n
                from scipy import stats
                pw_p = stats.binomtest(pw_wins, pw_n, 0.5).pvalue
                print(f" {pw_n:<8} {pw_rate*100:<10.1f} {pw_p:<10.4f}", end="")
                row.update({"pw_n": pw_n, "pw_win_rate": pw_rate, "pw_p": pw_p})
            else:
                print(f" {'—':<8} {'—':<10} {'—':<10}", end="")

        print()
        rows.append(row)

    # Distribution summary
    nli_all = [r.get("nli_cf", 0) for r in records]
    print(f"\n  NLI distribution: mean={statistics.mean(nli_all):.4f}, "
          f"std={statistics.stdev(nli_all) if len(nli_all) > 1 else 0:.4f}, "
          f"min={min(nli_all):.4f}, max={max(nli_all):.4f}")

    # By pole
    for pole in [pole_a, pole_b]:
        sub = [r for r in records if r.get(field) == pole]
        if sub:
            nli_sub = [r.get("nli_cf", 0) for r in sub]
            print(f"  {pole} (n={len(sub)}): NLI mean={statistics.mean(nli_sub):.4f}")

    return rows


def main():
    parser = argparse.ArgumentParser(description="exp-011: NLI Threshold Sensitivity")
    parser.add_argument("--input-files", nargs="+", required=True,
                        help="verified*.jsonl files (can pass multiple for multi-axis)")
    parser.add_argument("--axes", nargs="+", required=True,
                        help="Axis name for each input file")
    parser.add_argument("--pairwise-file", default=None,
                        help="Optional pairwise results file for cross-referencing")
    parser.add_argument("--output-dir", default=None)
    args = parser.parse_args()

    thresholds = [0.70, 0.75, 0.80, 0.85, 0.90, 0.95]

    pairwise_records = None
    if args.pairwise_file and os.path.exists(args.pairwise_file):
        pairwise_records = load_records(args.pairwise_file)
        print(f"Loaded {len(pairwise_records)} pairwise records")

    all_rows = []
    for input_file, axis in zip(args.input_files, args.axes):
        if not os.path.exists(input_file):
            print(f"File not found: {input_file}")
            continue
        records = load_records(input_file)
        print(f"\nLoaded {len(records)} records from {input_file}")
        rows = sensitivity_analysis(records, axis, thresholds, pairwise_records)
        if rows:
            for r in rows:
                r["axis"] = axis
            all_rows.extend(rows)

    if args.output_dir and all_rows:
        import csv
        os.makedirs(args.output_dir, exist_ok=True)
        csv_path = os.path.join(args.output_dir, "exp011_nli_sensitivity.csv")
        with open(csv_path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=all_rows[0].keys())
            writer.writeheader()
            for r in all_rows:
                writer.writerow(r)
        print(f"\nSaved CSV to {csv_path}")


if __name__ == "__main__":
    main()
