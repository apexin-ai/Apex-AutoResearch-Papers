"""exp-012: Consistency Filter Bias Analysis.

Analyzes whether position-consistent vs inconsistent pairwise pairs
have systematic differences, which would indicate selection bias in
the consistency filter (42-52% discard rate).

Input:  pairwise results jsonl (with trial1/trial2 choices, NLI, text fields)
Output: Console report + optional CSV
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


def analyze_consistency_bias(records: list[dict], verified_path: str | None = None):
    from scipy import stats as sp_stats

    valid = [r for r in records if r.get("trial1_choice") and r.get("trial2_choice")]
    consistent = [r for r in valid if r.get("consistent") is True]
    inconsistent = [r for r in valid if r.get("consistent") is False]

    print(f"\n{'='*70}")
    print(f"  Consistency Filter Bias Analysis")
    print(f"{'='*70}")
    print(f"  Total valid: {len(valid)}")
    print(f"  Consistent:   {len(consistent)} ({len(consistent)/len(valid)*100:.1f}%)")
    print(f"  Inconsistent: {len(inconsistent)} ({len(inconsistent)/len(valid)*100:.1f}%)")

    # Load verified data for NLI/BERTScore if available
    verified_map = {}
    if verified_path and os.path.exists(verified_path):
        for line in open(verified_path):
            if line.strip():
                rec = json.loads(line)
                verified_map[rec["id"]] = rec

    # --- NLI Score Distribution ---
    def get_nli(recs):
        if verified_map:
            return [verified_map[r["id"]]["nli_cf"] for r in recs if r["id"] in verified_map and verified_map[r["id"]].get("nli_cf") is not None]
        return [r["nli_cf"] for r in recs if r.get("nli_cf") is not None]

    nli_con = get_nli(consistent)
    nli_inc = get_nli(inconsistent)

    print(f"\n  --- NLI Score ---")
    if nli_con and nli_inc:
        print(f"  Consistent (n={len(nli_con)}):   mean={statistics.mean(nli_con):.4f}, std={statistics.stdev(nli_con) if len(nli_con)>1 else 0:.4f}")
        print(f"  Inconsistent (n={len(nli_inc)}): mean={statistics.mean(nli_inc):.4f}, std={statistics.stdev(nli_inc) if len(nli_inc)>1 else 0:.4f}")
        u_stat, u_p = sp_stats.mannwhitneyu(nli_con, nli_inc, alternative='two-sided')
        print(f"  Mann-Whitney U: U={u_stat:.1f}, p={u_p:.6f}")
        ks_stat, ks_p = sp_stats.ks_2samp(nli_con, nli_inc)
        print(f"  KS test: D={ks_stat:.4f}, p={ks_p:.6f}")
    else:
        print(f"  No NLI data available")

    # --- BERTScore Distribution ---
    def get_bs(recs):
        if verified_map:
            return [verified_map[r["id"]]["bertscore_cf"] for r in recs if r["id"] in verified_map and verified_map[r["id"]].get("bertscore_cf") is not None]
        return [r["bertscore_cf"] for r in recs if r.get("bertscore_cf") is not None]

    bs_con = get_bs(consistent)
    bs_inc = get_bs(inconsistent)

    print(f"\n  --- BERTScore ---")
    if bs_con and bs_inc:
        print(f"  Consistent (n={len(bs_con)}):   mean={statistics.mean(bs_con):.4f}")
        print(f"  Inconsistent (n={len(bs_inc)}): mean={statistics.mean(bs_inc):.4f}")
        u_stat, u_p = sp_stats.mannwhitneyu(bs_con, bs_inc, alternative='two-sided')
        print(f"  Mann-Whitney U: U={u_stat:.1f}, p={u_p:.6f}")
    else:
        print(f"  No BERTScore data available")

    # --- Response Length ---
    def get_lengths(recs):
        lengths = []
        for r in recs:
            rid = r["id"]
            if rid in verified_map:
                v = verified_map[rid]
                orig_len = len(v.get("original_text", ""))
                cf_len = len(v.get("counterfactual_text", ""))
                lengths.append({"orig": orig_len, "cf": cf_len, "diff": abs(orig_len - cf_len)})
        return lengths

    len_con = get_lengths(consistent)
    len_inc = get_lengths(inconsistent)

    print(f"\n  --- Response Length ---")
    if len_con and len_inc:
        orig_con = [l["orig"] for l in len_con]
        orig_inc = [l["orig"] for l in len_inc]
        diff_con = [l["diff"] for l in len_con]
        diff_inc = [l["diff"] for l in len_inc]
        print(f"  Original length — consistent: mean={statistics.mean(orig_con):.0f}, inconsistent: mean={statistics.mean(orig_inc):.0f}")
        u_stat, u_p = sp_stats.mannwhitneyu(orig_con, orig_inc, alternative='two-sided')
        print(f"    Mann-Whitney U: p={u_p:.6f}")
        print(f"  |orig-cf| length diff — consistent: mean={statistics.mean(diff_con):.0f}, inconsistent: mean={statistics.mean(diff_inc):.0f}")
        u_stat, u_p = sp_stats.mannwhitneyu(diff_con, diff_inc, alternative='two-sided')
        print(f"    Mann-Whitney U: p={u_p:.6f}")
    else:
        print(f"  No text length data available (need --verified-file)")

    # --- Position Bias in Each Group ---
    print(f"\n  --- Position Bias ---")
    for label, group in [("Consistent", consistent), ("Inconsistent", inconsistent)]:
        t1_a = sum(1 for r in group if r["trial1_choice"] == "A")
        t2_a = sum(1 for r in group if r["trial2_choice"] == "A")
        n = len(group)
        if n > 0:
            print(f"  {label} (n={n}): Trial1 A rate={t1_a/n*100:.1f}%, Trial2 A rate={t2_a/n*100:.1f}%")

    # --- Summary ---
    print(f"\n  --- Interpretation ---")
    bias_detected = False
    if nli_con and nli_inc:
        _, u_p = sp_stats.mannwhitneyu(nli_con, nli_inc, alternative='two-sided')
        if u_p < 0.05:
            print(f"  ⚠️ NLI differs significantly (p={u_p:.4f}): consistency filter may bias toward higher-quality counterfactuals")
            bias_detected = True
    if not bias_detected:
        print(f"  ✓ No significant systematic bias detected in consistency filter")


def main():
    parser = argparse.ArgumentParser(description="exp-012: Consistency Filter Bias Analysis")
    parser.add_argument("--pairwise-file", required=True, help="Pairwise results jsonl")
    parser.add_argument("--verified-file", default=None, help="Verified jsonl for NLI/text data")
    parser.add_argument("--output-dir", default=None)
    args = parser.parse_args()

    records = load_records(args.pairwise_file)
    print(f"Loaded {len(records)} pairwise records")

    analyze_consistency_bias(records, args.verified_file)


if __name__ == "__main__":
    main()
