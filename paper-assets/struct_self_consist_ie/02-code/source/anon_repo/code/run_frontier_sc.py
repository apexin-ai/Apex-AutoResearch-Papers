#!/usr/bin/env python3
"""Frontier model Self-Consistency experiment for structured IE.

Calls a frontier model (e.g. GPT-5.5) via OpenAI-compatible API,
generates N samples per instance, and evaluates SC metrics:
greedy F1, majority-vote F1, oracle F1, degeneracy rate,
agreement-F1 correlation, and failure mode distribution.
"""

import argparse
import json
import os
import random
import sys
import time
from collections import Counter, defaultdict
from itertools import combinations

import numpy as np
from scipy.stats import spearmanr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from evaluation import per_instance_f1, entity_strict_match
from consistency import (
    fleiss_kappa_surface,
    structural_consistency_soft_jaccard,
)

SCHEMA_HINT = (
    "Entity types: person, organization, location, building, "
    "art, product, event, other"
)

PROMPT_TPL = (
    "Extract all named entities from the following text. "
    "Output a JSON object with an \"entities\" key containing a list of entities. "
    "Each entity should have: \"text\" (the entity mention), \"type\" (one of: "
    "person, organization, location, building, art, product, event, other), "
    "\"start\" (character offset), \"end\" (character offset).\n\n"
    "Text: {text}\n\n"
    'Output format: {{"entities": [{{"text": "...", "type": "...", "start": 0, "end": 5}}, ...]}}\n'
    "Output ONLY the JSON object, no explanation."
)


def load_data(path, n_instances=0):
    data = []
    with open(path) as f:
        for line in f:
            if line.strip():
                data.append(json.loads(line))
                if 0 < n_instances <= len(data):
                    break
    return data


def parse_extraction(text):
    """Parse JSON extraction from model output. Returns dict with 'entities' key."""
    text = text.strip()
    if text.startswith("```json"):
        text = text[7:]
    if text.startswith("```"):
        text = text[3:]
    if text.endswith("```"):
        text = text[:-3]
    text = text.strip()

    try:
        obj = json.loads(text)
        if isinstance(obj, dict):
            entities = obj.get("entities", [])
            valid = []
            for e in entities:
                if isinstance(e, dict) and "text" in e and "type" in e:
                    if "start" in e and "end" in e:
                        valid.append({
                            "text": e["text"],
                            "type": e["type"].lower(),
                            "start": int(e["start"]),
                            "end": int(e["end"]),
                        })
            return {"entities": valid, "relations": [], "events": []}
    except (json.JSONDecodeError, ValueError):
        pass

    return {"entities": [], "relations": [], "events": []}


def call_api(client, model, text, temperature=1.0, max_tokens=4096, max_retries=3):
    prompt = PROMPT_TPL.format(text=text)
    for attempt in range(max_retries):
        try:
            resp = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature,
                max_tokens=max_tokens,
            )
            return resp.choices[0].message.content
        except Exception as e:
            if attempt < max_retries - 1:
                wait = 2 ** attempt
                print(f"  API error (attempt {attempt+1}): {e}, retrying in {wait}s...")
                time.sleep(wait)
            else:
                print(f"  API error (final): {e}")
                return ""


def entity_set(extraction):
    return {(e["text"].lower().strip(), e["type"]) for e in extraction.get("entities", []) if e.get("text")}


def majority_vote(samples):
    """Entity-level majority vote: include entity if it appears in > N/2 samples."""
    n = len(samples)
    threshold = n / 2
    entity_counts = Counter()
    entity_info = {}
    for s in samples:
        for e in s.get("entities", []):
            key = (e["text"].lower().strip(), e["type"])
            entity_counts[key] += 1
            if key not in entity_info:
                entity_info[key] = e

    voted = []
    for key, count in entity_counts.items():
        if count > threshold:
            voted.append(entity_info[key])

    return {"entities": voted, "relations": [], "events": []}


def prf(pred_set, gold_set):
    if not gold_set and not pred_set:
        return 1.0, 1.0, 1.0
    if not pred_set or not gold_set:
        return 0.0, 0.0, 0.0
    tp = len(pred_set & gold_set)
    if tp == 0:
        return 0.0, 0.0, 0.0
    p = tp / len(pred_set)
    r = tp / len(gold_set)
    return p, r, 2 * p * r / (p + r)


def compute_agreement(samples):
    """Compute mean pairwise entity overlap as agreement score."""
    n = len(samples)
    if n <= 1:
        return 1.0
    sets = [entity_set(s) for s in samples]
    overlaps = []
    for i in range(n):
        for j in range(i + 1, n):
            union = sets[i] | sets[j]
            if not union:
                overlaps.append(1.0)
            else:
                overlaps.append(len(sets[i] & sets[j]) / len(union))
    return float(np.mean(overlaps))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, required=True)
    parser.add_argument("--base_url", type=str, required=True)
    parser.add_argument("--api_key", type=str, required=True)
    parser.add_argument("--data_dir", type=str, required=True)
    parser.add_argument("--dataset", type=str, default="fewnerd")
    parser.add_argument("--n_instances", type=int, default=200)
    parser.add_argument("--n_samples", type=int, default=8)
    parser.add_argument("--temperature", type=float, default=1.0)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--output_dir", type=str, required=True)
    parser.add_argument("--max_tokens", type=int, default=4096)
    parser.add_argument("--dry_run", type=int, default=0,
                        help="If > 0, only process this many instances")
    parser.add_argument("--resume", action="store_true",
                        help="Resume from checkpoint if exists")
    args = parser.parse_args()

    random.seed(args.seed)
    np.random.seed(args.seed)

    os.makedirs(args.output_dir, exist_ok=True)

    from openai import OpenAI
    client = OpenAI(base_url=args.base_url, api_key=[REDACTED]

    test_path = os.path.join(args.data_dir, "test.json")
    n_load = args.dry_run if args.dry_run > 0 else args.n_instances
    data = load_data(test_path, n_load)
    print(f"Loaded {len(data)} instances from {test_path}")

    checkpoint_path = os.path.join(args.output_dir, "checkpoint.jsonl")
    processed = {}
    if args.resume and os.path.exists(checkpoint_path):
        with open(checkpoint_path) as f:
            for line in f:
                rec = json.loads(line)
                processed[rec["id"]] = rec
        print(f"Resumed: {len(processed)} instances from checkpoint")

    # Per-instance records
    records = []
    t0 = time.time()
    total_api_calls = 0
    parse_failures = 0

    for idx, inst in enumerate(data):
        inst_id = inst.get("id", f"inst_{idx}")
        gold = {
            "entities": inst.get("entities", []),
            "relations": inst.get("relations", []),
            "events": inst.get("events", []),
        }
        gold_set = entity_set(gold)

        if inst_id in processed:
            records.append(processed[inst_id])
            continue

        text = inst["text"]
        samples = []
        raw_outputs = []

        for si in range(args.n_samples):
            raw = call_api(client, args.model, text, args.temperature, args.max_tokens)
            total_api_calls += 1
            raw_outputs.append(raw)
            parsed = parse_extraction(raw)
            if not parsed["entities"] and raw.strip():
                parse_failures += 1
            samples.append(parsed)

        # Greedy = first sample
        greedy = samples[0]
        greedy_set = entity_set(greedy)
        _, _, greedy_f1 = prf(greedy_set, gold_set)

        # Majority vote
        mv = majority_vote(samples)
        mv_set = entity_set(mv)
        _, _, mv_f1 = prf(mv_set, gold_set)

        # Oracle best-of-N
        oracle_f1 = 0.0
        oracle_idx = 0
        for si, s in enumerate(samples):
            s_set = entity_set(s)
            _, _, f1 = prf(s_set, gold_set)
            if f1 > oracle_f1:
                oracle_f1 = f1
                oracle_idx = si

        # Degeneracy: all samples produce identical entity sets
        sample_sets = [entity_set(s) for s in samples]
        is_degenerate = all(ss == sample_sets[0] for ss in sample_sets)

        # Agreement score
        agreement = compute_agreement(samples)

        # Per-sample F1s
        sample_f1s = []
        for s in samples:
            s_set = entity_set(s)
            _, _, f1 = prf(s_set, gold_set)
            sample_f1s.append(f1)

        # Fleiss kappa
        fk = fleiss_kappa_surface(samples, subtask="ner")

        # Soft Jaccard
        sj = structural_consistency_soft_jaccard(samples, subtask="ner")

        # Failure mode classification
        # F1: Greedy correct (F1>=0.5), MV worse → SC hurts
        # F2: Greedy wrong (F1<0.5), MV better → SC helps
        # F3: Both good (both >= 0.5)
        # F4: Both bad (both < 0.5)
        if greedy_f1 >= 0.5 and mv_f1 < greedy_f1 - 0.01:
            failure_mode = "F1_sc_hurts"
        elif greedy_f1 < 0.5 and mv_f1 > greedy_f1 + 0.01:
            failure_mode = "F2_sc_helps"
        elif greedy_f1 >= 0.5 and mv_f1 >= 0.5:
            failure_mode = "F3_both_good"
        else:
            failure_mode = "F4_both_bad"

        record = {
            "id": inst_id,
            "n_gold_entities": len(gold.get("entities", [])),
            "greedy_f1": round(greedy_f1, 4),
            "mv_f1": round(mv_f1, 4),
            "oracle_f1": round(oracle_f1, 4),
            "agreement": round(agreement, 4),
            "fleiss_kappa": round(fk, 4),
            "soft_jaccard": round(sj, 4),
            "is_degenerate": is_degenerate,
            "failure_mode": failure_mode,
            "sample_f1s": [round(f, 4) for f in sample_f1s],
            "n_entities_per_sample": [len(s.get("entities", [])) for s in samples],
        }
        records.append(record)

        # Checkpoint
        with open(checkpoint_path, "a") as f:
            f.write(json.dumps(record) + "\n")

        if (idx + 1) % 10 == 0:
            elapsed = time.time() - t0
            eta = elapsed / (idx + 1) * (len(data) - idx - 1)
            print(f"  [{idx+1}/{len(data)}] elapsed={elapsed:.0f}s ETA={eta:.0f}s "
                  f"greedy={greedy_f1:.3f} mv={mv_f1:.3f} oracle={oracle_f1:.3f}")

    elapsed = time.time() - t0

    # Aggregate metrics
    greedy_f1s = [r["greedy_f1"] for r in records]
    mv_f1s = [r["mv_f1"] for r in records]
    oracle_f1s = [r["oracle_f1"] for r in records]
    agreements = [r["agreement"] for r in records]
    fks = [r["fleiss_kappa"] for r in records]
    sjs = [r["soft_jaccard"] for r in records]

    avg = lambda lst: sum(lst) / len(lst) if lst else 0.0

    # Spearman rho: agreement vs greedy F1
    rho_agree, p_agree = spearmanr(agreements, greedy_f1s)
    rho_fk, p_fk = spearmanr(fks, greedy_f1s)
    rho_sj, p_sj = spearmanr(sjs, greedy_f1s)

    # Degeneracy rate
    n_degen = sum(1 for r in records if r["is_degenerate"])
    degen_rate = n_degen / len(records) if records else 0.0

    # Failure mode distribution
    fm_counts = Counter(r["failure_mode"] for r in records)

    # Selection gap
    selection_gap = avg(oracle_f1s) - avg(mv_f1s)

    # Correlation-selection gap: high agreement correlation but MV doesn't close oracle gap
    corr_sel_gap = {
        "agreement_rho": round(float(rho_agree), 4),
        "fk_rho": round(float(rho_fk), 4),
        "sj_rho": round(float(rho_sj), 4),
        "greedy_f1": round(avg(greedy_f1s), 4),
        "mv_f1": round(avg(mv_f1s), 4),
        "oracle_f1": round(avg(oracle_f1s), 4),
        "mv_gain_over_greedy": round(avg(mv_f1s) - avg(greedy_f1s), 4),
        "selection_gap": round(selection_gap, 4),
    }

    summary = {
        "experiment": f"frontier_sc_{args.model.replace('/', '_')}_{args.dataset}",
        "model": args.model,
        "n_instances": len(records),
        "n_samples": args.n_samples,
        "temperature": args.temperature,
        "seed": args.seed,
        "elapsed_s": round(elapsed, 1),
        "total_api_calls": total_api_calls,
        "parse_failure_count": parse_failures,
        "metrics": {
            "greedy_f1": round(avg(greedy_f1s), 4),
            "mv_f1": round(avg(mv_f1s), 4),
            "oracle_f1": round(avg(oracle_f1s), 4),
            "degeneracy_rate": round(degen_rate, 4),
        },
        "correlations": {
            "agreement_vs_f1": {"rho": round(float(rho_agree), 4), "p": round(float(p_agree), 6)},
            "fleiss_kappa_vs_f1": {"rho": round(float(rho_fk), 4), "p": round(float(p_fk), 6)},
            "soft_jaccard_vs_f1": {"rho": round(float(rho_sj), 4), "p": round(float(p_sj), 6)},
        },
        "failure_modes": {k: v for k, v in sorted(fm_counts.items())},
        "correlation_selection_gap": corr_sel_gap,
    }

    # Save
    results_path = os.path.join(args.output_dir, "results.jsonl")
    with open(results_path, "w") as f:
        for r in records:
            f.write(json.dumps(r) + "\n")

    summary_path = os.path.join(args.output_dir, "summary.json")
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2)

    # Print summary
    print(f"\n{'='*60}")
    print(f"Frontier SC: {args.model} on {args.dataset}")
    print(f"{'='*60}")
    print(f"Instances: {len(records)}, Samples/inst: {args.n_samples}, T={args.temperature}")
    print(f"Elapsed: {elapsed:.1f}s, API calls: {total_api_calls}, Parse failures: {parse_failures}")
    print(f"\nMetrics:")
    print(f"  greedy_f1:       {avg(greedy_f1s):.4f}")
    print(f"  mv_f1:           {avg(mv_f1s):.4f} (Δ={avg(mv_f1s)-avg(greedy_f1s):+.4f})")
    print(f"  oracle_f1:       {avg(oracle_f1s):.4f}")
    print(f"  degeneracy_rate: {degen_rate:.4f} ({n_degen}/{len(records)})")
    print(f"  selection_gap:   {selection_gap:.4f} (oracle - mv)")
    print(f"\nCorrelations (agreement vs greedy F1):")
    print(f"  Jaccard agreement: ρ={rho_agree:.4f} (p={p_agree:.4e})")
    print(f"  Fleiss kappa:      ρ={rho_fk:.4f} (p={p_fk:.4e})")
    print(f"  Soft Jaccard:      ρ={rho_sj:.4f} (p={p_sj:.4e})")
    print(f"\nFailure modes:")
    for fm, count in sorted(fm_counts.items()):
        print(f"  {fm}: {count} ({100*count/len(records):.1f}%)")
    print(f"\nSaved to {args.output_dir}")


if __name__ == "__main__":
    main()
