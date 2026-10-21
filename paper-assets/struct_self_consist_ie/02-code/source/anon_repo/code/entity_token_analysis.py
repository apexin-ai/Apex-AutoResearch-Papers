"""Entity-token LP analysis: compare entity-only LP vs full-sequence LP for sample selection."""
import json
import sys
import numpy as np
from pathlib import Path


def load_samples(path):
    with open(path) as f:
        return [json.loads(l) for l in f if l.strip()]


def identify_entity_tokens(sample_dict):
    token_texts = sample_dict.get("token_texts", [])
    token_lps = sample_dict.get("token_logprobs", [])
    if not token_texts or not token_lps:
        return None, None

    full_text = "".join(token_texts)

    entity_mentions = set()
    for ent in sample_dict.get("entities", []):
        if "text" in ent:
            entity_mentions.add(ent["text"])

    char_pos = 0
    token_char_ranges = []
    for t in token_texts:
        token_char_ranges.append((char_pos, char_pos + len(t)))
        char_pos += len(t)

    entity_token_mask = [False] * len(token_texts)
    for mention in entity_mentions:
        search_patterns = [f'"text": "{mention}"', f'"text":"{mention}"']
        for pat in search_patterns:
            start = 0
            while True:
                idx = full_text.find(pat, start)
                if idx == -1:
                    break
                mention_start = idx + pat.index(mention)
                mention_end = mention_start + len(mention)
                for ti, (cs, ce) in enumerate(token_char_ranges):
                    if cs < mention_end and ce > mention_start:
                        entity_token_mask[ti] = True
                start = idx + 1

    entity_lps = [lp for lp, m in zip(token_lps, entity_token_mask) if m]
    schema_lps = [lp for lp, m in zip(token_lps, entity_token_mask) if not m]
    return entity_lps, schema_lps


def compute_ner_f1(pred_entities, gold_entities):
    pred_set = set()
    for e in pred_entities:
        pred_set.add((e.get("text", ""), e.get("type", ""), e.get("start", -1), e.get("end", -1)))
    gold_set = set()
    for e in gold_entities:
        gold_set.add((e.get("text", ""), e.get("type", ""), e.get("start", -1), e.get("end", -1)))
    tp = len(pred_set & gold_set)
    p = tp / max(len(pred_set), 1)
    r = tp / max(len(gold_set), 1)
    return 2 * p * r / max(p + r, 1e-10)


def analyze_dataset(samples_path, dataset_name):
    data = load_samples(samples_path)
    n_total = len(data)

    greedy_f1s = []
    full_sel_f1s = []
    entity_sel_f1s = []
    oracle_f1s = []
    majority_f1s = []

    full_lp_variances = []
    entity_lp_variances = []
    full_lp_ranges = []
    entity_lp_ranges = []
    n_entity_tokens_list = []
    n_total_tokens_list = []

    disagree_count = 0
    entity_wins = 0
    full_wins = 0

    for inst in data:
        gold_entities = inst["gold"].get("entities", [])
        if not gold_entities:
            continue

        samples = inst["samples"]
        n = len(samples)
        if n < 2:
            continue

        full_lps = [s.get("mean_logprob", 0) for s in samples]

        entity_mean_lps = []
        has_entity_tokens = True
        for s in samples:
            e_lps, _ = identify_entity_tokens(s)
            if e_lps and len(e_lps) > 0:
                entity_mean_lps.append(np.mean(e_lps))
                n_entity_tokens_list.append(len(e_lps))
                n_total_tokens_list.append(s.get("n_tokens", len(s.get("token_logprobs", []))))
            else:
                entity_mean_lps.append(s.get("mean_logprob", 0))
                has_entity_tokens = False

        sample_f1s = [compute_ner_f1(s.get("entities", []), gold_entities) for s in samples]
        greedy_f1 = compute_ner_f1(inst["greedy"].get("entities", []), gold_entities)

        full_sel_idx = int(np.argmax(full_lps))
        entity_sel_idx = int(np.argmax(entity_mean_lps))
        oracle_idx = int(np.argmax(sample_f1s))

        greedy_f1s.append(greedy_f1)
        full_sel_f1s.append(sample_f1s[full_sel_idx])
        entity_sel_f1s.append(sample_f1s[entity_sel_idx])
        oracle_f1s.append(sample_f1s[oracle_idx])

        # Majority vote F1
        from collections import Counter
        entity_sets = []
        for s in samples:
            es = frozenset((e.get("text",""), e.get("type",""), e.get("start",-1), e.get("end",-1))
                           for e in s.get("entities",[]))
            entity_sets.append(es)
        all_entities = [e for es in entity_sets for e in es]
        entity_counts = Counter(all_entities)
        majority_entities = {e for e, c in entity_counts.items() if c > n / 2}
        gold_set = {(e.get("text",""), e.get("type",""), e.get("start",-1), e.get("end",-1))
                    for e in gold_entities}
        tp = len(majority_entities & gold_set)
        p = tp / max(len(majority_entities), 1)
        r = tp / max(len(gold_set), 1)
        mv_f1 = 2 * p * r / max(p + r, 1e-10)
        majority_f1s.append(mv_f1)

        if full_sel_idx != entity_sel_idx:
            disagree_count += 1
            if sample_f1s[entity_sel_idx] > sample_f1s[full_sel_idx]:
                entity_wins += 1
            elif sample_f1s[full_sel_idx] > sample_f1s[entity_sel_idx]:
                full_wins += 1

        full_lp_variances.append(np.var(full_lps))
        full_lp_ranges.append(max(full_lps) - min(full_lps))
        if has_entity_tokens:
            entity_lp_variances.append(np.var(entity_mean_lps))
            entity_lp_ranges.append(max(entity_mean_lps) - min(entity_mean_lps))

    n_valid = len(greedy_f1s)

    results = {
        "dataset": dataset_name,
        "n_total": n_total,
        "n_valid": n_valid,
        "greedy_f1": float(np.mean(greedy_f1s)),
        "full_lp_selection_f1": float(np.mean(full_sel_f1s)),
        "entity_lp_selection_f1": float(np.mean(entity_sel_f1s)),
        "majority_vote_f1": float(np.mean(majority_f1s)),
        "oracle_f1": float(np.mean(oracle_f1s)),
        "full_lp_delta": float(np.mean(full_sel_f1s) - np.mean(greedy_f1s)),
        "entity_lp_delta": float(np.mean(entity_sel_f1s) - np.mean(greedy_f1s)),
        "entity_vs_full_delta": float(np.mean(entity_sel_f1s) - np.mean(full_sel_f1s)),
        "disagree_count": disagree_count,
        "entity_wins_when_disagree": entity_wins,
        "full_wins_when_disagree": full_wins,
        "ties_when_disagree": disagree_count - entity_wins - full_wins,
        "full_lp": {
            "median_variance": float(np.median(full_lp_variances)) if full_lp_variances else 0,
            "mean_variance": float(np.mean(full_lp_variances)) if full_lp_variances else 0,
            "median_range": float(np.median(full_lp_ranges)) if full_lp_ranges else 0,
            "mean_range": float(np.mean(full_lp_ranges)) if full_lp_ranges else 0,
            "tied_fraction": float(sum(1 for r in full_lp_ranges if r < 0.01) / max(n_valid, 1)),
        },
        "entity_lp": {
            "median_variance": float(np.median(entity_lp_variances)) if entity_lp_variances else 0,
            "mean_variance": float(np.mean(entity_lp_variances)) if entity_lp_variances else 0,
            "median_range": float(np.median(entity_lp_ranges)) if entity_lp_ranges else 0,
            "mean_range": float(np.mean(entity_lp_ranges)) if entity_lp_ranges else 0,
            "tied_fraction": float(sum(1 for r in entity_lp_ranges if r < 0.01) / max(len(entity_lp_ranges), 1)),
        },
        "entity_token_stats": {
            "median_entity_tokens": float(np.median(n_entity_tokens_list)) if n_entity_tokens_list else 0,
            "mean_entity_tokens": float(np.mean(n_entity_tokens_list)) if n_entity_tokens_list else 0,
            "median_total_tokens": float(np.median(n_total_tokens_list)) if n_total_tokens_list else 0,
            "mean_entity_fraction": float(np.mean(n_entity_tokens_list) / max(np.mean(n_total_tokens_list), 1)) if n_entity_tokens_list else 0,
        },
        "zscore_note": "z-score is a monotonic transform within each instance, so argmax(z_lps) == argmax(raw_lps). Z-score normalization does not change within-instance ranking or selection F1.",
    }
    return results


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--scierc_path", type=str, default=None)
    p.add_argument("--conll_path", type=str, default=None)
    p.add_argument("--output", type=str, default="output/exp_entity_token_lp/results.json")
    args = p.parse_args()

    all_results = {}
    if args.scierc_path:
        print(f"Analyzing SciERC: {args.scierc_path}")
        all_results["scierc"] = analyze_dataset(args.scierc_path, "scierc")
    if args.conll_path:
        print(f"Analyzing CoNLL: {args.conll_path}")
        all_results["conll"] = analyze_dataset(args.conll_path, "conll2003")

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\nResults saved to {args.output}")

    for ds, r in all_results.items():
        print(f"\n{'='*60}")
        print(f"  {ds.upper()} (n={r['n_valid']})")
        print(f"{'='*60}")
        print(f"  Greedy F1:           {r['greedy_f1']:.4f}")
        print(f"  Full-LP Selection:   {r['full_lp_selection_f1']:.4f}  (Δ={r['full_lp_delta']:+.4f})")
        print(f"  Entity-LP Selection: {r['entity_lp_selection_f1']:.4f}  (Δ={r['entity_lp_delta']:+.4f})")
        print(f"  Majority Vote:       {r['majority_vote_f1']:.4f}")
        print(f"  Oracle F1:           {r['oracle_f1']:.4f}")
        print(f"  Entity vs Full Δ:    {r['entity_vs_full_delta']:+.4f}")
        print(f"  Disagree: {r['disagree_count']}  (entity wins: {r['entity_wins_when_disagree']}, full wins: {r['full_wins_when_disagree']})")
        print(f"\n  Variance (within-instance):")
        print(f"    Full-LP:   median={r['full_lp']['median_variance']:.6f}  range={r['full_lp']['median_range']:.4f}  tied(<0.01)={r['full_lp']['tied_fraction']:.1%}")
        print(f"    Entity-LP: median={r['entity_lp']['median_variance']:.6f}  range={r['entity_lp']['median_range']:.4f}  tied(<0.01)={r['entity_lp']['tied_fraction']:.1%}")
        print(f"\n  Token stats:")
        print(f"    Median entity tokens: {r['entity_token_stats']['median_entity_tokens']:.0f}")
        print(f"    Entity fraction:      {r['entity_token_stats']['mean_entity_fraction']:.1%}")
