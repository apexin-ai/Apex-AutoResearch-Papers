#!/usr/bin/env python3
"""Evaluate verifier-selected candidates against gold annotations."""
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


def load_results(results_dir):
    results = defaultdict(dict)
    for rf in sorted(Path(results_dir).glob("test_shard_*_n*.jsonl")):
        with open(rf) as f:
            for line in f:
                r = json.loads(line.strip())
                key = (r["n_candidates"], r["seed"])
                results[key][r["doc_key"]] = r["candidates"]
    return results


def load_verify_results(verify_dir):
    verify = defaultdict(dict)
    for vf in sorted(Path(verify_dir).glob("verify_test_shard_*.jsonl")):
        with open(vf) as f:
            for line in f:
                r = json.loads(line.strip())
                key = (r["n_candidates"], r["seed"])
                verify[key][r["doc_key"]] = r
    return verify


def compute_micro_f1(predictions, gold):
    total_tp = total_pred = total_gold = 0
    for doc_key, pred_entities in predictions.items():
        gold_ents = gold.get(doc_key, set())
        pred_set = set((e["text"], e["type"]) for e in pred_entities)
        tp = len(pred_set & gold_ents)
        total_tp += tp
        total_pred += len(pred_set)
        total_gold += len(gold_ents)
    micro_p = total_tp / max(total_pred, 1)
    micro_r = total_tp / max(total_gold, 1)
    micro_f1 = 2 * micro_p * micro_r / (micro_p + micro_r) if (micro_p + micro_r) > 0 else 0
    return {"micro_p": round(micro_p, 4), "micro_r": round(micro_r, 4), "micro_f1": round(micro_f1, 4)}


def candidate_f1(entities, gold_ents):
    pred_set = set((e["text"], e["type"]) for e in entities)
    if not pred_set and not gold_ents:
        return 1.0
    if not pred_set or not gold_ents:
        return 0.0
    tp = len(pred_set & gold_ents)
    p = tp / len(pred_set)
    r = tp / len(gold_ents)
    return 2 * p * r / (p + r) if (p + r) > 0 else 0.0


def pearson(x, y):
    n = len(x)
    if n < 2:
        return 0.0
    mx = sum(x) / n
    my = sum(y) / n
    cov = sum((a - mx) * (b - my) for a, b in zip(x, y)) / n
    sx = (sum((a - mx) ** 2 for a in x) / n) ** 0.5
    sy = (sum((b - my) ** 2 for b in y) / n) ** 0.5
    return cov / (sx * sy) if sx * sy > 0 else 0.0


def spearman(x, y):
    def rank(arr):
        indexed = sorted(range(len(arr)), key=lambda i: arr[i])
        ranks = [0.0] * len(arr)
        i = 0
        while i < len(indexed):
            j = i
            while j < len(indexed) and arr[indexed[j]] == arr[indexed[i]]:
                j += 1
            avg_rank = (i + j - 1) / 2.0
            for k in range(i, j):
                ranks[indexed[k]] = avg_rank
            i = j
        return ranks
    return pearson(rank(x), rank(y))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify_dir", required=True)
    parser.add_argument("--results_dir", required=True)
    parser.add_argument("--gold_file", required=True)
    parser.add_argument("--output_file", required=True)
    args = parser.parse_args()

    gold = load_gold(args.gold_file)
    all_results = load_results(args.results_dir)
    all_verify = load_verify_results(args.verify_dir)

    print(f"Gold: {len(gold)} docs")
    print(f"Results: {len(all_results)} (n, seed) settings")
    print(f"Verify: {len(all_verify)} (n, seed) settings")

    output = {"per_seed": {}, "aggregated": {}, "score_distribution": {}}

    for key in sorted(all_verify.keys()):
        n, seed = key
        if n == 1:
            continue
        verify_data = all_verify[key]
        result_data = all_results.get(key, {})

        predictions = {}
        score_f1_pairs = []
        parse_ok = parse_total = all_same = 0
        all_overall_scores = []

        for doc_key, vr in verify_data.items():
            best_idx = vr["best_candidate_idx"]
            cands = result_data.get(doc_key, [])
            if not cands or best_idx >= len(cands):
                continue
            predictions[doc_key] = cands[best_idx].get("entities", [])

            for vs in vr["verify_scores"]:
                parse_total += 1
                if vs.get("parse_success"):
                    parse_ok += 1

            overall_scores = [vs.get("overall_score", 0) for vs in vr["verify_scores"]]
            all_overall_scores.extend(overall_scores)
            if len(set(overall_scores)) == 1:
                all_same += 1

            gold_ents = gold.get(doc_key, set())
            for ci, cand in enumerate(cands):
                if ci < len(vr["verify_scores"]):
                    vs = vr["verify_scores"][ci]
                    cf1 = candidate_f1(cand.get("entities", []), gold_ents)
                    score_f1_pairs.append((vs.get("overall_score", 0), cf1))

        metrics = compute_micro_f1(predictions, gold)
        scores_arr = [p[0] for p in score_f1_pairs]
        f1_arr = [p[1] for p in score_f1_pairs]
        pr = pearson(scores_arr, f1_arr) if len(set(scores_arr)) > 1 else 0.0
        sr = spearman(scores_arr, f1_arr) if len(set(scores_arr)) > 1 else 0.0

        sk = f"n{n}_seed{seed}"
        output["per_seed"][sk] = {
            "n": n, "seed": seed, **metrics,
            "parse_rate": round(parse_ok / max(parse_total, 1), 4),
            "all_same_score_docs": all_same, "total_docs": len(verify_data),
            "pearson_r": round(pr, 4), "spearman_r": round(sr, 4),
        }
        if all_overall_scores:
            mean_s = sum(all_overall_scores) / len(all_overall_scores)
            std_s = (sum((x - mean_s) ** 2 for x in all_overall_scores) / len(all_overall_scores)) ** 0.5
            output["score_distribution"][sk] = {
                "mean": round(mean_s, 2), "std": round(std_s, 2),
                "min": min(all_overall_scores), "max": max(all_overall_scores),
            }
        print(f"N={n:2d} seed={seed:3d}: F1={metrics['micro_f1']*100:.2f} "
              f"parse={parse_ok}/{parse_total} same_score={all_same}/{len(verify_data)} "
              f"pearson={pr:.3f} spearman={sr:.3f}")

    # Aggregate across seeds
    print("\n=== Aggregated ===")
    n_values = sorted(set(k[0] for k in all_verify.keys() if k[0] > 1))
    for n in n_values:
        seed_f1s, seed_pr, seed_sr, seed_parse = [], [], [], []
        for seed in [42, 123, 456]:
            sk = f"n{n}_seed{seed}"
            if sk in output["per_seed"]:
                d = output["per_seed"][sk]
                seed_f1s.append(d["micro_f1"])
                seed_pr.append(d["pearson_r"])
                seed_sr.append(d["spearman_r"])
                seed_parse.append(d["parse_rate"])
        if seed_f1s:
            mean_f1 = sum(seed_f1s) / len(seed_f1s)
            std_f1 = (sum((x - mean_f1) ** 2 for x in seed_f1s) / max(len(seed_f1s) - 1, 1)) ** 0.5
            output["aggregated"][f"n{n}"] = {
                "mean_micro_f1": round(mean_f1 * 100, 2),
                "std_micro_f1": round(std_f1 * 100, 2),
                "mean_pearson": round(sum(seed_pr) / len(seed_pr), 4),
                "mean_spearman": round(sum(seed_sr) / len(seed_sr), 4),
                "mean_parse_rate": round(sum(seed_parse) / len(seed_parse), 4),
            }
            print(f"N={n:2d}: verify_selected={mean_f1*100:.2f}+/-{std_f1*100:.2f} "
                  f"pearson={sum(seed_pr)/len(seed_pr):.3f} spearman={sum(seed_sr)/len(seed_sr):.3f}")

    # Print comparison table
    print("\n=== Comparison Table ===")
    baselines = {
        4: {"greedy": 42.05, "self_consistency": "41.88+/-0.37", "oracle": "45.92+/-0.42", "random": "41.29+/-0.72"},
        8: {"greedy": 42.05, "self_consistency": "42.22+/-0.63", "oracle": "47.45+/-0.25", "random": "41.79+/-0.58"},
        16: {"greedy": 42.05, "self_consistency": "41.34+/-0.32", "oracle": "48.54+/-0.36", "random": "41.83+/-0.86"},
    }
    print(f"{'N':>3} | {'greedy':>8} | {'exact_sc':>12} | {'verify_sel':>14} | {'oracle':>12} | {'random':>12}")
    print("-" * 75)
    for n in n_values:
        bl = baselines.get(n, {})
        agg = output["aggregated"].get(f"n{n}", {})
        vs = f"{agg.get('mean_micro_f1', 0):.2f}+/-{agg.get('std_micro_f1', 0):.2f}" if agg else "—"
        print(f"{n:3d} | {bl.get('greedy', '—'):>8} | {bl.get('self_consistency', '—'):>12} | {vs:>14} | {bl.get('oracle', '—'):>12} | {bl.get('random', '—'):>12}")

    out_path = Path(args.output_file)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, 'w') as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved to {out_path}")


if __name__ == "__main__":
    main()
