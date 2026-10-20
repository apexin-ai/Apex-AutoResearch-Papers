# Epsilon sensitivity analysis for LP compression threshold.
# Computes how different ε values affect LP-compressed instance ratio,
# LP-F1 correlation, and LP-best vs MV selection F1.
import json
import argparse
import sys
import numpy as np
from collections import Counter
from scipy.stats import spearmanr

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from evaluation import per_instance_f1, entity_strict_match


def load_data(path):
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]


def extract_entities_set(output_dict):
    return frozenset(
        (e["start"], e["end"], e["type"]) for e in output_dict.get("entities", [])
    )


def micro_f1_from_counts(tp, fp, fn):
    if tp == 0:
        return 0.0
    p = tp / (tp + fp)
    r = tp / (tp + fn)
    return 2 * p * r / (p + r)


def mv_entities(samples, threshold):
    counter = Counter()
    for s in samples:
        for e in extract_entities_set(s):
            counter[e] += 1
    return frozenset(e for e, c in counter.items() if c > threshold)


def lp_best_entities(samples, logprobs):
    best_idx = int(np.argmax(logprobs))
    return extract_entities_set(samples[best_idx])


def lp_weighted_mv_entities(samples, logprobs, n_samples):
    weights = np.exp(logprobs - np.max(logprobs))
    weights /= weights.sum()
    counter = {}
    for s, w in zip(samples, weights):
        for e in extract_entities_set(s):
            counter[e] = counter.get(e, 0.0) + w
    threshold = 0.5
    return frozenset(e for e, w in counter.items() if w > threshold)


def entity_f1_counts(pred_set, gold_set):
    tp = len(pred_set & gold_set)
    fp = len(pred_set - gold_set)
    fn = len(gold_set - pred_set)
    return tp, fp, fn


def analyze(data, epsilons):
    n_instances = len(data)
    n_samples = len(data[0]["samples"])
    mv_threshold = n_samples / 2

    inst_lp_ranges = []
    inst_mean_lps = []
    inst_max_lps = []
    inst_sample_f1s = []
    inst_greedy_f1s = []

    # Per-instance precomputed data for selection F1
    inst_data = []

    for inst in data:
        gold = inst["gold"]
        gold_set = extract_entities_set(gold)
        samples = inst["samples"]

        if "logprobs" in inst:
            logprobs = np.array(inst["logprobs"], dtype=float)
        else:
            logprobs = np.array([s["mean_logprob"] for s in samples], dtype=float)

        lp_range = float(np.max(logprobs) - np.min(logprobs))
        inst_lp_ranges.append(lp_range)
        inst_mean_lps.append(float(np.mean(logprobs)))
        inst_max_lps.append(float(np.max(logprobs)))

        sample_f1s = [per_instance_f1(s, gold, "ner") for s in samples]
        inst_sample_f1s.append(sample_f1s)

        greedy_f1 = per_instance_f1(inst["greedy"], gold, "ner") if "greedy" in inst else 0.0
        inst_greedy_f1s.append(greedy_f1)

        inst_data.append({
            "gold_set": gold_set,
            "samples": samples,
            "logprobs": logprobs,
            "lp_range": lp_range,
            "sample_f1s": sample_f1s,
            "greedy_f1": greedy_f1,
        })

    inst_lp_ranges = np.array(inst_lp_ranges)

    # Pooled LP-F1 arrays for correlation
    all_lps_flat = []
    all_f1s_flat = []
    for i, inst in enumerate(inst_data):
        lps = inst["logprobs"].tolist()
        f1s = inst["sample_f1s"]
        all_lps_flat.extend(lps)
        all_f1s_flat.extend(f1s)
    all_lps_flat = np.array(all_lps_flat)
    all_f1s_flat = np.array(all_f1s_flat)

    print(f"Dataset: {n_instances} instances, {n_samples} samples/instance")
    print(f"LP range stats: mean={np.mean(inst_lp_ranges):.4f}, "
          f"median={np.median(inst_lp_ranges):.4f}, "
          f"std={np.std(inst_lp_ranges):.4f}")
    print(f"LP range percentiles: "
          f"P10={np.percentile(inst_lp_ranges, 10):.4f}, "
          f"P25={np.percentile(inst_lp_ranges, 25):.4f}, "
          f"P50={np.percentile(inst_lp_ranges, 50):.4f}, "
          f"P75={np.percentile(inst_lp_ranges, 75):.4f}, "
          f"P90={np.percentile(inst_lp_ranges, 90):.4f}")
    print()

    # Global pooled correlation
    rho_global, p_global = spearmanr(all_lps_flat, all_f1s_flat)
    print(f"Global pooled Spearman rho(LP, F1): {rho_global:.4f} (p={p_global:.2e})")
    print()

    # Table header
    header = (f"{'eps':>6} | {'compressed%':>12} | {'n_comp':>6} | {'n_non':>6} | "
              f"{'rho_non':>8} | {'rho_all':>8} | "
              f"{'MV_F1':>7} | {'LP_F1':>7} | {'wMV_F1':>7} | "
              f"{'MV_comp':>8} | {'LP_comp':>8} | {'MV_non':>8} | {'LP_non':>8}")
    print(header)
    print("-" * len(header))

    results = []
    for eps in epsilons:
        compressed_mask = inst_lp_ranges < eps
        n_compressed = int(compressed_mask.sum())
        n_non = n_instances - n_compressed
        pct_compressed = 100.0 * n_compressed / n_instances

        # Spearman on non-compressed (pooled)
        if n_non >= 3:
            nc_lps = []
            nc_f1s = []
            for i, d in enumerate(inst_data):
                if not compressed_mask[i]:
                    nc_lps.extend(d["logprobs"].tolist())
                    nc_f1s.extend(d["sample_f1s"])
            rho_non, _ = spearmanr(nc_lps, nc_f1s) if len(nc_lps) >= 3 else (float("nan"), 1.0)
        else:
            rho_non = float("nan")

        # Spearman on all
        rho_all = rho_global

        # Selection F1: MV, LP-best, LP-weighted MV (micro-averaged)
        mv_tp = mv_fp = mv_fn = 0
        lp_tp = lp_fp = lp_fn = 0
        wmv_tp = wmv_fp = wmv_fn = 0

        # Split by compressed / non-compressed
        mv_comp_tp = mv_comp_fp = mv_comp_fn = 0
        lp_comp_tp = lp_comp_fp = lp_comp_fn = 0
        mv_non_tp = mv_non_fp = mv_non_fn = 0
        lp_non_tp = lp_non_fp = lp_non_fn = 0

        for i, d in enumerate(inst_data):
            gold_set = d["gold_set"]
            if len(gold_set) == 0:
                continue

            mv_pred = mv_entities(d["samples"], mv_threshold)
            lp_pred = lp_best_entities(d["samples"], d["logprobs"])
            wmv_pred = lp_weighted_mv_entities(d["samples"], d["logprobs"], n_samples)

            t, f_p, f_n = entity_f1_counts(mv_pred, gold_set)
            mv_tp += t; mv_fp += f_p; mv_fn += f_n
            t, f_p, f_n = entity_f1_counts(lp_pred, gold_set)
            lp_tp += t; lp_fp += f_p; lp_fn += f_n
            t, f_p, f_n = entity_f1_counts(wmv_pred, gold_set)
            wmv_tp += t; wmv_fp += f_p; wmv_fn += f_n

            if compressed_mask[i]:
                t, f_p, f_n = entity_f1_counts(mv_pred, gold_set)
                mv_comp_tp += t; mv_comp_fp += f_p; mv_comp_fn += f_n
                t, f_p, f_n = entity_f1_counts(lp_pred, gold_set)
                lp_comp_tp += t; lp_comp_fp += f_p; lp_comp_fn += f_n
            else:
                t, f_p, f_n = entity_f1_counts(mv_pred, gold_set)
                mv_non_tp += t; mv_non_fp += f_p; mv_non_fn += f_n
                t, f_p, f_n = entity_f1_counts(lp_pred, gold_set)
                lp_non_tp += t; lp_non_fp += f_p; lp_non_fn += f_n

        mv_f1 = micro_f1_from_counts(mv_tp, mv_fp, mv_fn)
        lp_f1 = micro_f1_from_counts(lp_tp, lp_fp, lp_fn)
        wmv_f1 = micro_f1_from_counts(wmv_tp, wmv_fp, wmv_fn)

        mv_comp_f1 = micro_f1_from_counts(mv_comp_tp, mv_comp_fp, mv_comp_fn)
        lp_comp_f1 = micro_f1_from_counts(lp_comp_tp, lp_comp_fp, lp_comp_fn)
        mv_non_f1 = micro_f1_from_counts(mv_non_tp, mv_non_fp, mv_non_fn)
        lp_non_f1 = micro_f1_from_counts(lp_non_tp, lp_non_fp, lp_non_fn)

        row = (f"{eps:6.2f} | {pct_compressed:11.1f}% | {n_compressed:6d} | {n_non:6d} | "
               f"{rho_non:8.4f} | {rho_all:8.4f} | "
               f"{mv_f1:7.4f} | {lp_f1:7.4f} | {wmv_f1:7.4f} | "
               f"{mv_comp_f1:8.4f} | {lp_comp_f1:8.4f} | {mv_non_f1:8.4f} | {lp_non_f1:8.4f}")
        print(row)

        results.append({
            "epsilon": eps,
            "pct_compressed": pct_compressed,
            "n_compressed": n_compressed,
            "n_non_compressed": n_non,
            "rho_non_compressed": float(rho_non) if np.isfinite(rho_non) else None,
            "rho_all": float(rho_all),
            "mv_f1": mv_f1,
            "lp_best_f1": lp_f1,
            "wmv_f1": wmv_f1,
            "mv_compressed_f1": mv_comp_f1,
            "lp_compressed_f1": lp_comp_f1,
            "mv_non_compressed_f1": mv_non_f1,
            "lp_non_compressed_f1": lp_non_f1,
        })

    # More epsilon values for elbow detection
    print("\n\n=== Fine-grained epsilon sweep (for elbow detection) ===")
    fine_epsilons = np.arange(0.005, 0.205, 0.005)
    print(f"{'eps':>6} | {'compressed%':>12} | {'delta%':>8}")
    prev_pct = 0.0
    for eps in fine_epsilons:
        pct = 100.0 * np.sum(inst_lp_ranges < eps) / n_instances
        delta = pct - prev_pct
        print(f"{eps:6.3f} | {pct:11.1f}% | {delta:+7.1f}%")
        prev_pct = pct

    # LP-best selection advantage analysis
    print("\n\n=== LP-best selection advantage by LP range bucket ===")
    buckets = [(0, 0.01), (0.01, 0.03), (0.03, 0.05), (0.05, 0.10), (0.10, 0.20), (0.20, float("inf"))]
    print(f"{'bucket':>15} | {'n':>6} | {'MV_F1':>7} | {'LP_F1':>7} | {'LP-MV':>7}")
    for lo, hi in buckets:
        mask = (inst_lp_ranges >= lo) & (inst_lp_ranges < hi)
        n_bucket = int(mask.sum())
        if n_bucket == 0:
            continue
        b_mv_tp = b_mv_fp = b_mv_fn = 0
        b_lp_tp = b_lp_fp = b_lp_fn = 0
        for i, d in enumerate(inst_data):
            if not mask[i]:
                continue
            gold_set = d["gold_set"]
            if len(gold_set) == 0:
                continue
            mv_pred = mv_entities(d["samples"], mv_threshold)
            lp_pred = lp_best_entities(d["samples"], d["logprobs"])
            t, f_p, f_n = entity_f1_counts(mv_pred, gold_set)
            b_mv_tp += t; b_mv_fp += f_p; b_mv_fn += f_n
            t, f_p, f_n = entity_f1_counts(lp_pred, gold_set)
            b_lp_tp += t; b_lp_fp += f_p; b_lp_fn += f_n
        b_mv_f1 = micro_f1_from_counts(b_mv_tp, b_mv_fp, b_mv_fn)
        b_lp_f1 = micro_f1_from_counts(b_lp_tp, b_lp_fp, b_lp_fn)
        hi_str = f"{hi:.2f}" if hi < float("inf") else "inf"
        label = f"[{lo:.2f}, {hi_str})"
        print(f"{label:>15} | {n_bucket:6d} | {b_mv_f1:7.4f} | {b_lp_f1:7.4f} | {b_lp_f1 - b_mv_f1:+7.4f}")

    return results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--samples_file", required=True)
    parser.add_argument("--epsilons", type=float, nargs="+",
                        default=[0.01, 0.03, 0.05, 0.10, 0.15, 0.20])
    parser.add_argument("--gold_filter", action="store_true", default=True,
                        help="Filter to gold-non-empty instances only")
    args = parser.parse_args()

    print(f"Loading {args.samples_file} ...")
    data = load_data(args.samples_file)
    print(f"Loaded {len(data)} instances")

    if args.gold_filter:
        data = [d for d in data if len(d["gold"].get("entities", [])) > 0]
        print(f"After gold-filter: {len(data)} instances")

    results = analyze(data, args.epsilons)

    out_json = args.samples_file.rsplit("/", 1)[0] + "/epsilon_sensitivity.json"
    with open(out_json, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nJSON results saved to {out_json}")


if __name__ == "__main__":
    main()
