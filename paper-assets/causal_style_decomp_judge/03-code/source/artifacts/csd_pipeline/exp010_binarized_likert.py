"""exp-010: Binarized Likert Sign Test — C2 Critical Control.

Isolates whether the Likert-vs-Pairwise sensitivity gap (C2) is due to
measurement structure (forced choice vs rating scale) or statistical test
choice (paired t-test vs sign test).

Binarizes Likert scores per pair: formal_score > casual_score → formal_wins.
Applies sign test (binomial) on non-tie pairs, matching the pairwise protocol.

Input:  scored_32b.jsonl (with score_original, score_counterfactual, original_formality)
Output: Console report + optional CSV
"""

import argparse
import json
import os
import sys

from scipy import stats


def load_scored(path: str) -> list[dict]:
    records = []
    with open(path) as f:
        for line in f:
            if line.strip():
                rec = json.loads(line)
                if rec.get("score_original") is not None and rec.get("score_counterfactual") is not None:
                    records.append(rec)
    return records


def binarized_analysis(records: list[dict], axis: str = "formality", nli_threshold: float | None = None):
    axis_config = {
        "formality": {"poles": ("formal", "casual"), "field": "original_formality"},
        "verbosity": {"poles": ("verbose", "concise"), "field": "original_verbosity"},
        "tone": {"poles": ("assertive", "hedging"), "field": "original_tone"},
        "register": {"poles": ("academic", "conversational"), "field": "original_register"},
    }
    cfg = axis_config[axis]
    pole_a, pole_b = cfg["poles"]
    field = cfg["field"]

    if nli_threshold is not None:
        records = [r for r in records if r.get("nli_cf", 0) >= nli_threshold]

    formal_wins = 0
    casual_wins = 0
    ties = 0

    for rec in records:
        s_orig = float(rec["score_original"])
        s_cf = float(rec["score_counterfactual"])
        is_pole_b = rec[field] == pole_b

        if is_pole_b:
            score_a = s_cf
            score_b = s_orig
        else:
            score_a = s_orig
            score_b = s_cf

        if score_a > score_b:
            formal_wins += 1
        elif score_b > score_a:
            casual_wins += 1
        else:
            ties += 1

    n_total = len(records)
    n_non_tie = formal_wins + casual_wins

    print(f"\n{'='*60}")
    label = f"NLI≥{nli_threshold}" if nli_threshold else "all"
    print(f"  Binarized Likert Sign Test ({label}, n={n_total})")
    print(f"{'='*60}")
    print(f"  {pole_a} > {pole_b}: {formal_wins}")
    print(f"  {pole_b} > {pole_a}: {casual_wins}")
    print(f"  Ties (equal):    {ties} ({ties/n_total*100:.1f}%)")
    print(f"  Non-tie pairs:   {n_non_tie}")

    if n_non_tie < 2:
        print("  Too few non-tie pairs for sign test")
        return None

    win_rate = formal_wins / n_non_tie
    sign_p = stats.binomtest(formal_wins, n_non_tie, 0.5).pvalue

    z = 1.96
    denom = 1 + z**2 / n_non_tie
    center = (win_rate + z**2 / (2 * n_non_tie)) / denom
    spread = z * (win_rate * (1 - win_rate) / n_non_tie + z**2 / (4 * n_non_tie**2))**0.5 / denom
    ci_lo, ci_hi = max(0, center - spread), min(1, center + spread)

    print(f"\n  {pole_a} win rate (non-tie): {win_rate:.4f} ({formal_wins}/{n_non_tie})")
    print(f"  95% CI (Wilson):  [{ci_lo:.4f}, {ci_hi:.4f}]")
    print(f"  Sign test p:      {sign_p:.6f}")
    print(f"  Significant:      {'YES' if sign_p < 0.05 else 'NO'} (α=0.05)")

    print(f"\n  --- Comparison with Pairwise ---")
    print(f"  Pairwise (reference): 69.1% win rate, p=0.006")
    print(f"  Binarized Likert:     {win_rate*100:.1f}% win rate, p={sign_p:.4f}")
    if sign_p < 0.05:
        print(f"  → Binarized Likert ALSO significant: gap may be test choice, not measurement structure")
        print(f"  → C2 (Likert Blindspot) needs reframing")
    else:
        print(f"  → Binarized Likert NOT significant: confirms pairwise structural advantage")
        print(f"  → C2 (Likert Blindspot) validated — forced choice matters, not just test choice")

    return {
        "group": label,
        "n": n_total,
        "n_non_tie": n_non_tie,
        f"{pole_a}_wins": formal_wins,
        f"{pole_b}_wins": casual_wins,
        "ties": ties,
        "tie_rate": ties / n_total,
        "win_rate": win_rate,
        "ci_lo": ci_lo,
        "ci_hi": ci_hi,
        "sign_p": sign_p,
    }


def main():
    parser = argparse.ArgumentParser(description="exp-010: Binarized Likert Sign Test")
    parser.add_argument("--input-file", required=True, help="scored_32b.jsonl path")
    parser.add_argument("--output-dir", default=None, help="Optional output dir for CSV")
    parser.add_argument("--axis", default="formality", help="Style axis (default: formality)")
    args = parser.parse_args()

    records = load_scored(args.input_file)
    print(f"Loaded {len(records)} scored records")

    results = []

    r_all = binarized_analysis(records, axis=args.axis)
    if r_all:
        results.append(r_all)

    for thresh in [0.90, 0.85, 0.80]:
        r = binarized_analysis(records, axis=args.axis, nli_threshold=thresh)
        if r:
            results.append(r)

    cfg = {
        "formality": {"field": "original_formality", "poles": ("formal", "casual")},
        "verbosity": {"field": "original_verbosity", "poles": ("verbose", "concise")},
    }
    if args.axis in cfg:
        pole_a, pole_b = cfg[args.axis]["poles"]
        field = cfg[args.axis]["field"]
        print(f"\n{'='*60}")
        print(f"  Directional Breakdown (all records)")
        print(f"{'='*60}")
        for direction in [pole_a, pole_b]:
            sub = [r for r in records if r.get(field) == direction]
            if len(sub) < 3:
                continue
            target = pole_b if direction == pole_a else pole_a
            print(f"\n  --- {direction}→{target} (n={len(sub)}) ---")
            binarized_analysis(sub, axis=args.axis)

    if args.output_dir and results:
        import csv
        os.makedirs(args.output_dir, exist_ok=True)
        csv_path = os.path.join(args.output_dir, "exp010_binarized_likert.csv")
        with open(csv_path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=results[0].keys())
            writer.writeheader()
            for r in results:
                writer.writerow(r)
        print(f"\nSaved CSV to {csv_path}")


if __name__ == "__main__":
    main()
