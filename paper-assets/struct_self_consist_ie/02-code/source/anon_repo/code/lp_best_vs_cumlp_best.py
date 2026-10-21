"""Compare entity-level F1 between mean-LP-best and cumulative-LP-best sample selection."""
import json
import argparse
import numpy as np
from scipy import stats


def extract_entities(output_dict):
    entities = set()
    for e in output_dict.get("entities", []):
        entities.add((e["text"], e["type"], e["start"], e["end"]))
    return frozenset(entities)


def instance_f1(pred, gold):
    tp = len(pred & gold)
    fp = len(pred - gold)
    fn = len(gold - pred)
    if tp == 0:
        return 0.0
    p = tp / (tp + fp)
    r = tp / (tp + fn)
    return 2 * p * r / (p + r)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--samples_file", required=True)
    args = parser.parse_args()

    with open(args.samples_file) as f:
        instances = [json.loads(line) for line in f]

    lp_f1s = []
    cum_f1s = []
    token_cvs = []
    disagree_lp_f1s = []
    disagree_cum_f1s = []
    n_skipped = 0

    for inst in instances:
        gold_entities = extract_entities(inst["gold"])
        if len(gold_entities) == 0:
            n_skipped += 1
            continue

        samples = inst["samples"]
        if len(samples) < 2:
            n_skipped += 1
            continue

        mean_lps = [s["mean_logprob"] for s in samples]
        cum_lps = [s["cumulative_logprob"] for s in samples]
        n_tokens_list = [s["n_tokens"] for s in samples]

        best_mean_idx = int(np.argmax(mean_lps))
        best_cum_idx = int(np.argmax(cum_lps))

        pred_mean = extract_entities(samples[best_mean_idx])
        pred_cum = extract_entities(samples[best_cum_idx])

        f1_mean = instance_f1(pred_mean, gold_entities)
        f1_cum = instance_f1(pred_cum, gold_entities)

        lp_f1s.append(f1_mean)
        cum_f1s.append(f1_cum)

        cv = np.std(n_tokens_list) / np.mean(n_tokens_list) if np.mean(n_tokens_list) > 0 else 0
        token_cvs.append(cv)

        if best_mean_idx != best_cum_idx:
            disagree_lp_f1s.append(f1_mean)
            disagree_cum_f1s.append(f1_cum)

    lp_f1s = np.array(lp_f1s)
    cum_f1s = np.array(cum_f1s)
    token_cvs = np.array(token_cvs)

    print(f"Instances evaluated: {len(lp_f1s)} (skipped {n_skipped} gold-empty or <2 samples)")
    print()

    # Overall
    mean_lp_f1 = np.mean(lp_f1s)
    mean_cum_f1 = np.mean(cum_f1s)
    diff = (mean_lp_f1 - mean_cum_f1) * 100
    print(f"Overall: LP-best mean F1 = {mean_lp_f1:.4f}, cumLP-best mean F1 = {mean_cum_f1:.4f} (差 {diff:+.2f}pp)")

    # Disagreement subset
    n_disagree = len(disagree_lp_f1s)
    if n_disagree > 0:
        d_lp = np.array(disagree_lp_f1s)
        d_cum = np.array(disagree_cum_f1s)
        print(f"Disagreement subset (n={n_disagree}): LP-best = {np.mean(d_lp):.4f}, cumLP-best = {np.mean(d_cum):.4f} (差 {(np.mean(d_lp)-np.mean(d_cum))*100:+.2f}pp)")
    else:
        print("Disagreement subset: n=0")

    # Wilcoxon
    diffs_all = lp_f1s - cum_f1s
    nonzero = diffs_all[diffs_all != 0]
    if len(nonzero) > 0:
        stat_all, p_all = stats.wilcoxon(nonzero)
        print(f"Wilcoxon p-value (overall): {p_all:.6f}")
    else:
        p_all = 1.0
        print("Wilcoxon p-value (overall): N/A (all diffs = 0)")

    if n_disagree > 0:
        diffs_dis = d_lp - d_cum
        nonzero_dis = diffs_dis[diffs_dis != 0]
        if len(nonzero_dis) > 0:
            stat_dis, p_dis = stats.wilcoxon(nonzero_dis)
            print(f"Wilcoxon p-value (disagreement): {p_dis:.6f}")
        else:
            p_dis = 1.0
            print("Wilcoxon p-value (disagreement): N/A (all diffs = 0)")
    else:
        p_dis = 1.0
        print("Wilcoxon p-value (disagreement): N/A")

    # Winner
    if p_all < 0.05:
        winner = "mean_LP" if mean_lp_f1 > mean_cum_f1 else "cumulative_LP"
    else:
        winner = "no significant difference"
    print(f"Winner: {winner}")

    # Token CV stratified
    print("\n--- Token CV stratified F1 ---")
    buckets = [
        ("low (CV<=0.05)", token_cvs <= 0.05),
        ("mid (0.05<CV<=0.10)", (token_cvs > 0.05) & (token_cvs <= 0.10)),
        ("high-mid (0.10<CV<=0.20)", (token_cvs > 0.10) & (token_cvs <= 0.20)),
        ("high (CV>0.20)", token_cvs > 0.20),
    ]
    print(f"{'Bucket':<25} {'n':>6} {'LP-best F1':>12} {'cumLP-best F1':>14} {'diff (pp)':>10} {'p-value':>10}")
    print("-" * 80)
    for name, mask in buckets:
        n = mask.sum()
        if n == 0:
            print(f"{name:<25} {n:>6} {'---':>12} {'---':>14} {'---':>10} {'---':>10}")
            continue
        lp_b = lp_f1s[mask]
        cum_b = cum_f1s[mask]
        d = lp_b - cum_b
        nz = d[d != 0]
        if len(nz) > 0:
            _, p = stats.wilcoxon(nz)
            p_str = f"{p:.4f}"
        else:
            p_str = "N/A"
        print(f"{name:<25} {n:>6} {np.mean(lp_b):>12.4f} {np.mean(cum_b):>14.4f} {(np.mean(lp_b)-np.mean(cum_b))*100:>+10.2f} {p_str:>10}")

    # Extra: win/loss/tie counts
    print("\n--- Win/Loss/Tie counts ---")
    lp_wins = int(np.sum(lp_f1s > cum_f1s))
    cum_wins = int(np.sum(cum_f1s > lp_f1s))
    ties = int(np.sum(lp_f1s == cum_f1s))
    print(f"LP-best wins: {lp_wins}, cumLP-best wins: {cum_wins}, ties: {ties}")


if __name__ == "__main__":
    main()
