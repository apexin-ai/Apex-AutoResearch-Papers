#!/usr/bin/env python3
"""Entity-level frequency merging for structured IE candidates."""
import json
import sys
from pathlib import Path
from collections import defaultdict, Counter


def load_gold(gold_file):
    gold = {}
    doc_tokens = {}
    with open(gold_file) as f:
        for line in f:
            doc = json.loads(line.strip())
            entities = set()
            for ent in doc["entities"]:
                entities.add((ent["text"], ent["type"]))
            gold[doc["doc_key"]] = entities
            doc_tokens[doc["doc_key"]] = doc["tokens"]
    return gold, doc_tokens


def load_results(results_dir):
    results = defaultdict(dict)
    for rf in sorted(Path(results_dir).glob("test_shard_*_n*.jsonl")):
        with open(rf) as f:
            for line in f:
                r = json.loads(line.strip())
                key = (r["n_candidates"], r["seed"])
                results[key][r["doc_key"]] = r["candidates"]
    return results


def frequency_merge(candidates, threshold_k):
    freq = Counter()
    for cand in candidates:
        if not cand.get("parse_success", True):
            continue
        unique = set((e["text"], e["type"]) for e in cand["entities"])
        for key in unique:
            freq[key] += 1
    return [{"text": t, "type": tp} for (t, tp), c in freq.items() if c >= threshold_k]


def locate_spans(entities, tokens):
    if not tokens:
        for ent in entities:
            ent["spans"] = []
        return
    token_text = " ".join(tokens)
    char_to_token = {}
    pos = 0
    for i, tok in enumerate(tokens):
        for j in range(len(tok)):
            char_to_token[pos + j] = i
        pos += len(tok) + 1
    for ent in entities:
        text = ent["text"]
        spans = []
        search_pos = 0
        while True:
            idx = token_text.find(text, search_pos)
            if idx < 0:
                break
            s = char_to_token.get(idx)
            ec = idx + len(text) - 1
            e = char_to_token.get(ec)
            if s is not None and e is not None:
                spans.append((s, e + 1))
            search_pos = idx + 1
        ent["spans"] = spans


def span_iou(s1, e1, s2, e2):
    inter = max(0, min(e1, e2) - max(s1, s2))
    union = (e1 - s1) + (e2 - s2) - inter
    return inter / union if union > 0 else 0.0


def weighted_frequency_merge(candidates, tokens, threshold_k, iou_threshold=0.5):
    all_ents_by_type = defaultdict(list)

    for cand_idx, cand in enumerate(candidates):
        if not cand.get("parse_success", True):
            continue
        ents = [{"text": e["text"], "type": e["type"]} for e in cand["entities"]]
        locate_spans(ents, tokens)
        for ent in ents:
            all_ents_by_type[ent["type"]].append({
                "text": ent["text"],
                "spans": ent["spans"],
                "cand_idx": cand_idx,
            })

    merged = []

    for etype, ents in all_ents_by_type.items():
        clusters = []
        cluster_spans = []

        for ent in ents:
            best_cluster = -1
            best_iou = 0.0

            if ent["spans"]:
                for ci, cspans in enumerate(cluster_spans):
                    if not cspans:
                        continue
                    for s1, e1 in ent["spans"]:
                        for s2, e2 in cspans:
                            iou = span_iou(s1, e1, s2, e2)
                            if iou > best_iou:
                                best_iou = iou
                                best_cluster = ci

            if best_iou >= iou_threshold and best_cluster >= 0:
                clusters[best_cluster].append({"text": ent["text"], "cand_idx": ent["cand_idx"]})
                for sp in ent["spans"]:
                    if sp not in cluster_spans[best_cluster]:
                        cluster_spans[best_cluster].append(sp)
            else:
                if not ent["spans"]:
                    found = False
                    for ci, cluster in enumerate(clusters):
                        if any(m["text"] == ent["text"] for m in cluster):
                            cluster.append({"text": ent["text"], "cand_idx": ent["cand_idx"]})
                            found = True
                            break
                    if not found:
                        clusters.append([{"text": ent["text"], "cand_idx": ent["cand_idx"]}])
                        cluster_spans.append(list(ent["spans"]))
                else:
                    clusters.append([{"text": ent["text"], "cand_idx": ent["cand_idx"]}])
                    cluster_spans.append(list(ent["spans"]))

        for cluster in clusters:
            unique_cands = set(m["cand_idx"] for m in cluster)
            freq = len(unique_cands)
            if freq >= threshold_k:
                text_counts = Counter(m["text"] for m in cluster)
                best_text = text_counts.most_common(1)[0][0]
                merged.append({"text": best_text, "type": etype})

    return merged


def evaluate_merge(all_results, gold, doc_tokens, n, seed, threshold_k, use_weighted=False):
    key = (n, seed)
    if key not in all_results:
        return None

    total_tp, total_pred, total_gold = 0, 0, 0

    for doc_key, gold_ents in gold.items():
        if doc_key not in all_results[key]:
            continue

        candidates = all_results[key][doc_key]

        if use_weighted:
            tokens = doc_tokens.get(doc_key, [])
            merged = weighted_frequency_merge(candidates, tokens, threshold_k)
        else:
            merged = frequency_merge(candidates, threshold_k)

        pred_set = set((e["text"], e["type"]) for e in merged)
        tp = len(pred_set & gold_ents)
        total_tp += tp
        total_pred += len(pred_set)
        total_gold += len(gold_ents)

    p = total_tp / max(total_pred, 1)
    r = total_tp / max(total_gold, 1)
    f1 = 2 * p * r / (p + r) if (p + r) > 0 else 0.0
    return {"p": p, "r": r, "f1": f1, "tp": total_tp, "pred": total_pred, "gold": total_gold}


def mean_std(vals):
    m = sum(vals) / len(vals)
    if len(vals) > 1:
        s = (sum((x - m) ** 2 for x in vals) / (len(vals) - 1)) ** 0.5
    else:
        s = 0.0
    return m, s


def main():
    results_dir = "/root/projects/verifier-tts-struct-ie/results"
    gold_file = "/root/projects/verifier-tts-struct-ie/data/test_gold.jsonl"
    output_file = "/root/projects/verifier-tts-struct-ie/results/frequency_merge_results.json"

    gold, doc_tokens = load_gold(gold_file)
    print(f"Loaded {len(gold)} gold documents")

    all_results = load_results(results_dir)
    print(f"Found {len(all_results)} (n, seed) settings")

    n_seeds = defaultdict(list)
    for n, seed in all_results.keys():
        n_seeds[n].append(seed)
    for n in n_seeds:
        n_seeds[n] = sorted(set(n_seeds[n]))

    threshold_map = {
        1: [1],
        4: [1, 2, 3, 4],
        8: [1, 2, 3, 4, 5, 6, 7, 8],
        16: [1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 14, 16],
    }

    full_results = {}

    for method_name, use_weighted in [("binary", False), ("weighted_iou", True)]:
        header = "Binary Frequency Merging" if not use_weighted else "Weighted IoU Frequency Merging"
        print(f"\n{'=' * 60}")
        print(f"=== {header} ===")
        print(f"{'=' * 60}")

        method_results = {}

        for n in sorted(n_seeds.keys()):
            seeds = n_seeds[n]
            thresholds = threshold_map.get(n, list(range(1, n + 1)))

            if n > 1:
                print(f"\nN={n}, seeds={seeds}")

            for k in thresholds:
                seed_metrics = []
                for seed in seeds:
                    m = evaluate_merge(all_results, gold, doc_tokens, n, seed, k, use_weighted)
                    if m:
                        seed_metrics.append(m)

                if not seed_metrics:
                    continue

                f1s = [m["f1"] for m in seed_metrics]
                ps = [m["p"] for m in seed_metrics]
                rs = [m["r"] for m in seed_metrics]
                mf1, sf1 = mean_std(f1s)
                mp, sp = mean_std(ps)
                mr, sr = mean_std(rs)

                if n == 1:
                    print(f"\nN=1 (greedy):     P={mp*100:.1f}       R={mr*100:.1f}       F1={mf1*100:.2f}")
                else:
                    label = "union" if k == 1 else ("intersect" if k == n else "")
                    label_str = f" ({label})" if label else ""
                    print(
                        f"  k={k:2d}{label_str:12s}: "
                        f"P={mp*100:.1f}±{sp*100:.1f}  "
                        f"R={mr*100:.1f}±{sr*100:.1f}  "
                        f"F1={mf1*100:.2f}±{sf1*100:.2f}"
                    )

                method_results[f"n{n}_k{k}"] = {
                    "n": n, "k": k,
                    "mean_p": round(mp * 100, 2), "std_p": round(sp * 100, 2),
                    "mean_r": round(mr * 100, 2), "std_r": round(sr * 100, 2),
                    "mean_f1": round(mf1 * 100, 2), "std_f1": round(sf1 * 100, 2),
                    "per_seed": [
                        {"seed": s, "p": round(m["p"] * 100, 2), "r": round(m["r"] * 100, 2),
                         "f1": round(m["f1"] * 100, 2), "tp": m["tp"], "pred": m["pred"], "gold": m["gold"]}
                        for s, m in zip(seeds, seed_metrics)
                    ],
                }

        full_results[method_name] = method_results

    # Best configs
    print(f"\n{'=' * 60}")
    print("=== Best Configs ===")
    print(f"{'=' * 60}")

    greedy_f1 = full_results["binary"].get("n1_k1", {}).get("mean_f1", 0.0)

    for method_name, label in [("binary", "Binary"), ("weighted_iou", "Weighted")]:
        best_key, best_f1, best_std = None, 0.0, 0.0
        for k, v in full_results[method_name].items():
            if v["mean_f1"] > best_f1:
                best_f1 = v["mean_f1"]
                best_std = v.get("std_f1", 0.0)
                best_key = k
        if best_key:
            v = full_results[method_name][best_key]
            print(f"{label:10s}: best = N={v['n']}, k={v['k']}, F1={best_f1:.2f}±{best_std:.2f}")

    print(f"Greedy baseline: F1={greedy_f1:.2f}")

    # Pass/fail
    print(f"\n=== Pass/Fail ===")
    pass_result = False
    for method_name in ["binary", "weighted_iou"]:
        for k, v in full_results[method_name].items():
            if v["n"] >= 8 and v["mean_f1"] >= greedy_f1 + 1.0:
                pass_result = True
                break
        if pass_result:
            break
    print(f"merging@N>=8 > greedy >= 1.0pt? {'YES' if pass_result else 'NO'}")

    output = {"results": full_results, "greedy_f1": greedy_f1, "pass_result": pass_result}
    with open(output_file, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved to {output_file}")


if __name__ == "__main__":
    main()
