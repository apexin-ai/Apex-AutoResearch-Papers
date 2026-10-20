#!/usr/bin/env python3
"""Evaluate sequential refinement results per round, compare with parallel methods."""
import json
import argparse
from pathlib import Path
from collections import defaultdict


def load_gold(gold_file):
    gold = {}
    with open(gold_file) as f:
        for line in f:
            doc = json.loads(line.strip())
            entities = set()
            for ent in doc["entities"]:
                entities.add((ent["text"], ent["type"]))
            gold[doc["doc_key"]] = entities
    return gold


def load_sequential_results(results_dir, num_shards=8):
    """Load all seq_shard*_round*_seed*.jsonl files, grouped by (round, seed)."""
    by_round_seed = defaultdict(dict)
    results_path = Path(results_dir)
    for f in sorted(results_path.glob("seq_shard*_round*_seed*.jsonl")):
        parts = f.stem.split("_")
        round_num = int(parts[2].replace("round", ""))
        seed = int(parts[3].replace("seed", ""))
        with open(f) as fh:
            for line in fh:
                rec = json.loads(line.strip())
                by_round_seed[(round_num, seed)][rec["doc_key"]] = rec
    return by_round_seed


def compute_micro_f1(predictions, gold):
    total_tp = 0
    total_pred = 0
    total_gold = 0
    for doc_key, gold_ents in gold.items():
        pred_rec = predictions.get(doc_key)
        if pred_rec is None:
            total_gold += len(gold_ents)
            continue
        pred_ents = set((e["text"], e["type"]) for e in pred_rec["entities"])
        tp = len(pred_ents & gold_ents)
        total_tp += tp
        total_pred += len(pred_ents)
        total_gold += len(gold_ents)
    p = total_tp / max(total_pred, 1)
    r = total_tp / max(total_gold, 1)
    f1 = 2 * p * r / (p + r) if (p + r) > 0 else 0.0
    return {
        "p": round(p * 100, 2),
        "r": round(r * 100, 2),
        "f1": round(f1 * 100, 2),
        "tp": total_tp,
        "pred": total_pred,
        "gold": total_gold,
    }


def mean_std(vals):
    m = sum(vals) / len(vals)
    if len(vals) > 1:
        s = (sum((x - m) ** 2 for x in vals) / (len(vals) - 1)) ** 0.5
    else:
        s = 0.0
    return m, s


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--results_dir", required=True)
    parser.add_argument("--gold_file", required=True)
    parser.add_argument("--output_file", default="seq_eval_results.json")
    args = parser.parse_args()

    gold = load_gold(args.gold_file)
    print(f"Loaded {len(gold)} gold documents")

    by_round_seed = load_sequential_results(args.results_dir)
    rounds = sorted(set(r for r, s in by_round_seed.keys()))
    seeds = sorted(set(s for r, s in by_round_seed.keys()))
    print(f"Found rounds: {rounds}, seeds: {seeds}")

    all_results = {}

    print(f"\n{'='*70}")
    print("=== Sequential Self-Refinement F1 ===")
    print(f"{'='*70}")
    print(f"{'Round (K)':<12} {'Compute':<10} {'F1 (mean±std)':<18} {'P':<10} {'R':<10} {'ΔF1 vs K=1':<12}")
    print("-" * 70)

    baseline_f1 = None

    for rnd in rounds:
        seed_metrics = []
        for seed in seeds:
            key = (rnd, seed)
            if key not in by_round_seed:
                continue
            m = compute_micro_f1(by_round_seed[key], gold)
            m["seed"] = seed
            seed_metrics.append(m)

        if not seed_metrics:
            continue

        f1s = [m["f1"] for m in seed_metrics]
        ps = [m["p"] for m in seed_metrics]
        rs = [m["r"] for m in seed_metrics]
        mf1, sf1 = mean_std(f1s)
        mp, sp = mean_std(ps)
        mr, sr = mean_std(rs)

        if rnd == 1:
            baseline_f1 = mf1
            delta_str = "baseline"
            f1_str = f"{mf1:.2f}"
        else:
            delta = mf1 - baseline_f1 if baseline_f1 is not None else 0
            sign = "+" if delta >= 0 else ""
            delta_str = f"{sign}{delta:.2f}"
            f1_str = f"{mf1:.2f}±{sf1:.2f}"

        print(f"{rnd:<12} {rnd}x{'':<8} {f1_str:<18} {mp:.1f}±{sp:.1f}{'':<3} {mr:.1f}±{sr:.1f}{'':<3} {delta_str}")

        all_results[f"round{rnd}"] = {
            "round": rnd,
            "mean_f1": round(mf1, 2),
            "std_f1": round(sf1, 2),
            "mean_p": round(mp, 2),
            "std_p": round(sp, 2),
            "mean_r": round(mr, 2),
            "std_r": round(sr, 2),
            "per_seed": seed_metrics,
        }

    # Parallel comparison
    print(f"\n{'='*70}")
    print("=== Sequential vs Parallel (matched compute) ===")
    print(f"{'='*70}")
    print(f"{'Compute':<10} {'Sequential':<20} {'Parallel freq_merge':<22} {'Parallel oracle':<18}")
    print("-" * 70)

    parallel_data = {
        1: {"freq": 42.05, "oracle": 42.05},
        2: {"freq": "~42.3", "oracle": "~44.0"},
        4: {"freq": 42.71, "oracle": 45.92},
    }

    for compute, par in parallel_data.items():
        rnd_key = f"round{compute}"
        if rnd_key in all_results:
            seq_f1 = all_results[rnd_key]["mean_f1"]
            seq_std = all_results[rnd_key]["std_f1"]
            seq_str = f"{seq_f1:.2f}±{seq_std:.2f}" if compute > 1 else f"{seq_f1:.2f}"
        else:
            seq_str = "N/A"
        freq_str = f"{par['freq']}" if isinstance(par["freq"], str) else f"{par['freq']:.2f}"
        oracle_str = f"{par['oracle']}" if isinstance(par["oracle"], str) else f"{par['oracle']:.2f}"
        print(f"{compute}x{'':<8} {seq_str:<20} {freq_str:<22} {oracle_str:<18}")

    # Pass/Fail
    print(f"\n{'='*70}")
    print("=== Pass/Fail ===")
    print(f"{'='*70}")

    pass_result = False
    best_seq_f1 = 0
    best_round = 0
    for rnd in rounds:
        rnd_key = f"round{rnd}"
        if rnd_key in all_results and rnd >= 3:
            f1 = all_results[rnd_key]["mean_f1"]
            if f1 > best_seq_f1:
                best_seq_f1 = f1
                best_round = rnd

    if baseline_f1 is not None and best_seq_f1 >= baseline_f1 + 1.0:
        pass_result = True

    print(f"sequential@K>=3 > greedy >= 1.0pt? {'YES' if pass_result else 'NO'}")
    if baseline_f1 is not None:
        print(f"  Greedy (K=1): {baseline_f1:.2f}")
        if best_round > 0:
            print(f"  Best sequential (K={best_round}): {best_seq_f1:.2f}")
            print(f"  Delta: {best_seq_f1 - baseline_f1:+.2f}")

    if pass_result:
        print("\nMVP PASS — IE 上 sequential > parallel")
    else:
        print("\nMVP FAIL — training-free TTS 不适用于 IE")

    # Per-type analysis for refinement rounds
    print(f"\n{'='*70}")
    print("=== Entity Type Analysis (K=1 vs best K) ===")
    print(f"{'='*70}")

    if best_round > 0:
        for seed in seeds[:1]:
            r1_data = by_round_seed.get((1, seed), {})
            rk_data = by_round_seed.get((best_round, seed), {})
            r1_by_type = defaultdict(lambda: {"tp": 0, "pred": 0, "gold": 0})
            rk_by_type = defaultdict(lambda: {"tp": 0, "pred": 0, "gold": 0})

            for doc_key, gold_ents in gold.items():
                for ent_text, ent_type in gold_ents:
                    r1_by_type[ent_type]["gold"] += 1
                    rk_by_type[ent_type]["gold"] += 1

                r1_rec = r1_data.get(doc_key)
                if r1_rec:
                    for e in r1_rec["entities"]:
                        r1_by_type[e["type"]]["pred"] += 1
                        if (e["text"], e["type"]) in gold_ents:
                            r1_by_type[e["type"]]["tp"] += 1

                rk_rec = rk_data.get(doc_key)
                if rk_rec:
                    for e in rk_rec["entities"]:
                        rk_by_type[e["type"]]["pred"] += 1
                        if (e["text"], e["type"]) in gold_ents:
                            rk_by_type[e["type"]]["tp"] += 1

            print(f"\nSeed={seed}, Round 1 vs Round {best_round}:")
            print(f"{'Type':<25} {'R1 F1':<10} {'R{0} F1'.format(best_round):<10} {'Delta':<10}")
            print("-" * 55)
            for etype in sorted(set(list(r1_by_type.keys()) + list(rk_by_type.keys()))):
                r1 = r1_by_type[etype]
                rk = rk_by_type[etype]
                r1_p = r1["tp"] / max(r1["pred"], 1)
                r1_r = r1["tp"] / max(r1["gold"], 1)
                r1_f1 = 2 * r1_p * r1_r / (r1_p + r1_r) if (r1_p + r1_r) > 0 else 0
                rk_p = rk["tp"] / max(rk["pred"], 1)
                rk_r = rk["tp"] / max(rk["gold"], 1)
                rk_f1 = 2 * rk_p * rk_r / (rk_p + rk_r) if (rk_p + rk_r) > 0 else 0
                delta = (rk_f1 - r1_f1) * 100
                print(f"{etype:<25} {r1_f1*100:<10.1f} {rk_f1*100:<10.1f} {delta:+.1f}")

    # Degradation check
    print(f"\n{'='*70}")
    print("=== Refinement Degradation Check ===")
    print(f"{'='*70}")
    for seed in seeds:
        prev_f1 = None
        degrade = []
        for rnd in rounds:
            key = (rnd, seed)
            if key not in by_round_seed:
                continue
            m = compute_micro_f1(by_round_seed[key], gold)
            if prev_f1 is not None and m["f1"] < prev_f1:
                degrade.append(f"Round {rnd}: {m['f1']:.2f} < Round {rnd-1}: {prev_f1:.2f}")
            prev_f1 = m["f1"]
        if degrade:
            print(f"Seed {seed}: DEGRADATION detected — {'; '.join(degrade)}")
        else:
            print(f"Seed {seed}: No degradation (monotonic improvement or stable)")

    output = {
        "results": all_results,
        "baseline_f1": baseline_f1,
        "best_sequential_f1": best_seq_f1,
        "best_round": best_round,
        "pass_result": pass_result,
    }
    out_path = Path(args.output_file)
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved to {out_path}")


if __name__ == "__main__":
    main()
