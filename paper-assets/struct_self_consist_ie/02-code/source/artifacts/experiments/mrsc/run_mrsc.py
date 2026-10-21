#!/usr/bin/env python3
"""Multi-Round Structured Self-Consistency (MRSC) for IE.

Reads existing N-sample inference JSONL, identifies disputed entities
(agreement < threshold), re-prompts the model on those entities in Round 2,
and aggregates with weighted voting. Compares against greedy / majority vote
/ oracle baselines.

Input:  samples.jsonl — one JSON object per line with keys:
        text, gold.entities, samples[].entities, (optional) greedy.entities
        Each entity: {text, type, start, end}

Output: mrsc_results.json — full metrics including per-threshold F1,
        disputed-entity breakdown, and baseline comparisons.

Requires: torch, transformers, peft (optional), scipy, sklearn
"""

import argparse
import json
import os
import time
from collections import defaultdict

import numpy as np
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_samples(path, max_instances=0):
    data = []
    with open(path) as f:
        for line in f:
            if line.strip():
                data.append(json.loads(line))
                if 0 < max_instances <= len(data):
                    break
    return data


# ---------------------------------------------------------------------------
# Round 1: entity agreement analysis
# ---------------------------------------------------------------------------

def compute_entity_agreement(instance):
    """Return {(start, end, type, text): agreement_ratio} across N samples."""
    counts = defaultdict(int)
    N = len(instance["samples"])
    for sample in instance["samples"]:
        for e in sample.get("entities", []):
            counts[(e["start"], e["end"], e["type"], e["text"])] += 1
    return {k: c / N for k, c in counts.items()}, counts, N


def split_entities(agreement_map, dispute_threshold):
    """Split entities into disputed (< threshold) and non-disputed (>= threshold)."""
    disputed = {}
    non_disputed = {}
    for key, agree in agreement_map.items():
        if agree < dispute_threshold:
            disputed[key] = agree
        else:
            non_disputed[key] = agree
    return disputed, non_disputed


# ---------------------------------------------------------------------------
# Round 2: focused re-prompting
# ---------------------------------------------------------------------------

def build_round2_prompt(sentence, entity_text, entity_type, count, N):
    """Verification prompt that includes disagreement context."""
    return (
        f'In the sentence below, multiple attempts at entity extraction '
        f'disagreed on whether "{entity_text}" is a {entity_type} entity '
        f'(appeared in {count}/{N} samples). '
        f'Please re-examine and determine: is "{entity_text}" a {entity_type} '
        f'entity in this context? Answer yes or no.\n\n'
        f'Sentence: {sentence}\n'
        f'Answer:'
    )


# ---------------------------------------------------------------------------
# Model loading & batch verification (shared with ESJ pattern)
# ---------------------------------------------------------------------------

def load_model(base_path, adapter_path, device="cuda"):
    tok_path = adapter_path if adapter_path else base_path
    print(f"Loading tokenizer from {tok_path} ...")
    tokenizer = AutoTokenizer.from_pretrained(
        tok_path, trust_remote_code=True, padding_side="left",
    )
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    print(f"Loading base model from {base_path} ...")
    model = AutoModelForCausalLM.from_pretrained(
        base_path,
        torch_dtype=torch.bfloat16,
        device_map=device,
        trust_remote_code=True,
    )

    if adapter_path:
        print(f"Loading LoRA adapter from {adapter_path} ...")
        model = PeftModel.from_pretrained(model, adapter_path)
        model = model.merge_and_unload()
        print("LoRA merged.")

    model.eval()
    return model, tokenizer


def get_yes_no_ids(tokenizer):
    yes_ids, no_ids = [], []
    for w in ["yes", "Yes", "YES"]:
        ids = tokenizer.encode(w, add_special_tokens=False)
        if len(ids) == 1:
            yes_ids.append(ids[0])
    for w in ["no", "No", "NO"]:
        ids = tokenizer.encode(w, add_special_tokens=False)
        if len(ids) == 1:
            no_ids.append(ids[0])
    yes_ids = list(set(yes_ids))
    no_ids = list(set(no_ids))
    print(f"yes token IDs: {yes_ids}  no token IDs: {no_ids}")
    assert yes_ids and no_ids, "Could not find yes/no token IDs"
    return yes_ids, no_ids


@torch.no_grad()
def batch_verify(model, tokenizer, prompts, yes_ids, no_ids,
                 batch_size=16, device="cuda"):
    """Run batched yes/no verification. Returns list of P(yes) per prompt."""
    yes_t = torch.tensor(yes_ids, device=device)
    no_t = torch.tensor(no_ids, device=device)
    all_p_yes = []

    n_batches = (len(prompts) + batch_size - 1) // batch_size
    for bi in range(n_batches):
        start = bi * batch_size
        batch = prompts[start:start + batch_size]

        formatted = []
        for p in batch:
            msgs = [{"role": "user", "content": p}]
            try:
                fp = tokenizer.apply_chat_template(
                    msgs, tokenize=False, add_generation_prompt=True,
                    enable_thinking=False,
                )
            except TypeError:
                fp = tokenizer.apply_chat_template(
                    msgs, tokenize=False, add_generation_prompt=True,
                )
            formatted.append(fp)

        inputs = tokenizer(
            formatted, return_tensors="pt", padding=True,
            truncation=True, max_length=512,
        ).to(device)

        logits = model(**inputs).logits

        for i in range(len(batch)):
            last_pos = inputs.attention_mask[i].sum() - 1
            next_logits = logits[i, last_pos]
            y_logits = next_logits[yes_t]
            n_logits = next_logits[no_t]
            combined = torch.cat([y_logits, n_logits])
            probs = torch.softmax(combined, dim=0)
            p_yes = probs[:len(yes_ids)].sum().item()
            all_p_yes.append(p_yes)

        if bi % 100 == 0:
            print(f"  batch {bi}/{n_batches}  avg_p_yes={np.mean(all_p_yes[-len(batch):]):.3f}")

    return all_p_yes


# ---------------------------------------------------------------------------
# Evaluation helpers
# ---------------------------------------------------------------------------

def entity_set(entities):
    return {(e["start"], e["end"], e["type"]) for e in entities}


def compute_prf(pred, gold):
    if not gold and not pred:
        return 1.0, 1.0, 1.0
    if not pred or not gold:
        return 0.0, 0.0, 0.0
    tp = len(pred & gold)
    if tp == 0:
        return 0.0, 0.0, 0.0
    p = tp / len(pred)
    r = tp / len(gold)
    return p, r, 2 * p * r / (p + r)


def majority_vote(instance, threshold=0.5):
    counts = defaultdict(int)
    N = len(instance["samples"])
    for s in instance["samples"]:
        for e in s.get("entities", []):
            counts[(e["start"], e["end"], e["type"])] += 1
    return {k for k, c in counts.items() if c / N >= threshold}


# ---------------------------------------------------------------------------
# MRSC aggregation
# ---------------------------------------------------------------------------

def mrsc_construction(instance, round2_scores, dispute_threshold,
                      round2_weight, final_threshold):
    """Weighted aggregation of Round 1 agreement + Round 2 P(yes).

    Non-disputed entities (agreement >= dispute_threshold):
        included if agreement >= final_threshold (standard majority vote).
    Disputed entities (agreement < dispute_threshold):
        score = (P_yes_round2 * round2_weight + agreement * 1.0)
                / (round2_weight + 1.0)
        included if score >= final_threshold.
    """
    agreement_map, counts, N = compute_entity_agreement(instance)
    out = set()

    for (s, e, t, txt), agree in agreement_map.items():
        key = (s, e, t)
        if agree >= dispute_threshold:
            if agree >= final_threshold:
                out.add(key)
        else:
            p_yes = round2_scores.get((s, e, t), 0.0)
            # Weighted combination: Round 2 gets higher weight
            score = (p_yes * round2_weight + agree * 1.0) / (round2_weight + 1.0)
            if score >= final_threshold:
                out.add(key)

    return out


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(
        description="Multi-Round Structured Self-Consistency (MRSC)")
    ap.add_argument("--base_model_path", type=str, required=True)
    ap.add_argument("--adapter_path", type=str, default=None)
    ap.add_argument("--data_path", type=str, required=True,
                    help="Path to N-sample inference JSONL")
    ap.add_argument("--output_dir", type=str, required=True)
    ap.add_argument("--dispute_threshold", type=float, default=0.6,
                    help="Agreement below this triggers Round 2 (default: 0.6)")
    ap.add_argument("--round2_weight", type=float, default=2.0,
                    help="Weight for Round 2 P(yes) in aggregation (default: 2.0)")
    ap.add_argument("--batch_size", type=int, default=16)
    ap.add_argument("--max_instances", type=int, default=0,
                    help="Limit instances for debugging (0 = all)")
    args = ap.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    device = "cuda"

    # ---- 1. Load data ----
    print(f"Loading data from {args.data_path} ...")
    data = load_samples(args.data_path, args.max_instances)
    print(f"  {len(data)} instances loaded")

    # ---- 2. Round 1: compute agreement & identify disputed entities ----
    print(f"Round 1: analyzing entity agreement (dispute_threshold={args.dispute_threshold}) ...")
    inst_agreements = []
    inst_counts = []
    inst_Ns = []
    total_entities = 0
    total_disputed = 0
    total_non_disputed = 0

    for inst in data:
        agree_map, counts, N = compute_entity_agreement(inst)
        inst_agreements.append(agree_map)
        inst_counts.append(counts)
        inst_Ns.append(N)
        disputed, non_disputed = split_entities(agree_map, args.dispute_threshold)
        total_entities += len(agree_map)
        total_disputed += len(disputed)
        total_non_disputed += len(non_disputed)

    print(f"  Total unique entities: {total_entities}")
    print(f"  Disputed (agreement < {args.dispute_threshold}): {total_disputed} "
          f"({100*total_disputed/max(total_entities,1):.1f}%)")
    print(f"  Non-disputed: {total_non_disputed}")

    # ---- 3. Build Round 2 prompts for disputed entities only ----
    all_prompts = []
    prompt_idx = []  # (instance_i, (start, end, type))
    for i, inst in enumerate(data):
        disputed, _ = split_entities(inst_agreements[i], args.dispute_threshold)
        for (s, e, t, txt), agree in disputed.items():
            count = inst_counts[i][(s, e, t, txt)]
            N = inst_Ns[i]
            all_prompts.append(build_round2_prompt(inst["text"], txt, t, count, N))
            prompt_idx.append((i, (s, e, t)))

    print(f"  {len(all_prompts)} Round 2 verification prompts built")

    if len(all_prompts) == 0:
        print("No disputed entities found — MRSC reduces to majority vote.")

    # ---- 4. Load model & run Round 2 verification ----
    inst_round2 = [dict() for _ in range(len(data))]

    if len(all_prompts) > 0:
        model, tokenizer = load_model(args.base_model_path, args.adapter_path, device)
        yes_ids, no_ids = get_yes_no_ids(tokenizer)

        print(f"Round 2: batch verification (batch_size={args.batch_size}) ...")
        t0 = time.time()
        p_yes_all = batch_verify(model, tokenizer, all_prompts, yes_ids, no_ids,
                                 args.batch_size, device)
        elapsed = time.time() - t0
        print(f"  Done in {elapsed:.1f}s ({len(all_prompts)/elapsed:.0f} prompts/s)")

        del model
        import gc; gc.collect(); torch.cuda.empty_cache()

        for idx, (ii, key) in enumerate(prompt_idx):
            inst_round2[ii][key] = p_yes_all[idx]
    else:
        elapsed = 0.0
        p_yes_all = []

    # ---- 5. Baselines ----
    print("Computing baselines ...")
    greedy_f1s, oracle_f1s = [], []
    for inst in data:
        gold = entity_set(inst["gold"]["entities"])
        g = entity_set(inst.get("greedy", inst["samples"][0]).get("entities", []))
        greedy_f1s.append(compute_prf(g, gold)[2])
        oracle_f1s.append(max(
            compute_prf(entity_set(s.get("entities", [])), gold)[2]
            for s in inst["samples"]
        ))
    greedy_f1 = float(np.mean(greedy_f1s))
    oracle_f1 = float(np.mean(oracle_f1s))

    mv_ths = [0.125, 0.25, 0.375, 0.5, 0.625, 0.75]
    mv_res = {}
    for th in mv_ths:
        fs = []
        for inst in data:
            gold = entity_set(inst["gold"]["entities"])
            fs.append(compute_prf(majority_vote(inst, th), gold)[2])
        mv_res[str(th)] = float(np.mean(fs))
    best_mv_th = max(mv_res, key=mv_res.get)
    best_mv_f1 = mv_res[best_mv_th]

    # ---- 6. MRSC construction at various final thresholds ----
    print("Evaluating MRSC construction ...")
    mrsc_ths = [0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6]
    mrsc_res = {}
    for th in mrsc_ths:
        fs = []
        for i, inst in enumerate(data):
            gold = entity_set(inst["gold"]["entities"])
            pred = mrsc_construction(inst, inst_round2[i],
                                     args.dispute_threshold,
                                     args.round2_weight, th)
            fs.append(compute_prf(pred, gold)[2])
        mrsc_res[str(th)] = float(np.mean(fs))
    best_mrsc_th = max(mrsc_res, key=mrsc_res.get)
    best_mrsc_f1 = mrsc_res[best_mrsc_th]

    # ---- 7. Disputed vs non-disputed entity breakdown ----
    print("Disputed entity breakdown ...")
    disp_tp, disp_fp, disp_fn = 0, 0, 0
    nondisp_tp, nondisp_fp, nondisp_fn = 0, 0, 0

    # Use best MRSC threshold for breakdown
    for i, inst in enumerate(data):
        gold = entity_set(inst["gold"]["entities"])
        pred = mrsc_construction(inst, inst_round2[i],
                                 args.dispute_threshold,
                                 args.round2_weight, float(best_mrsc_th))
        agree_map = inst_agreements[i]

        for (s, e, t, txt), agree in agree_map.items():
            key = (s, e, t)
            in_pred = key in pred
            in_gold = key in gold
            if agree < args.dispute_threshold:
                if in_pred and in_gold:
                    disp_tp += 1
                elif in_pred and not in_gold:
                    disp_fp += 1
                elif not in_pred and in_gold:
                    disp_fn += 1
            else:
                if in_pred and in_gold:
                    nondisp_tp += 1
                elif in_pred and not in_gold:
                    nondisp_fp += 1
                elif not in_pred and in_gold:
                    nondisp_fn += 1

        # Gold entities not in any sample are missed by both categories;
        # count them as non-disputed FN
        all_sample_keys = {(s, e, t) for (s, e, t, _) in agree_map}
        for gkey in gold:
            if gkey not in all_sample_keys:
                nondisp_fn += 1

    def safe_prf(tp, fp, fn):
        p = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        r = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        f1 = 2 * p * r / (p + r) if (p + r) > 0 else 0.0
        return {"tp": tp, "fp": fp, "fn": fn,
                "precision": round(p, 4), "recall": round(r, 4), "f1": round(f1, 4)}

    # Same breakdown for best MV baseline
    mv_disp_tp, mv_disp_fp, mv_disp_fn = 0, 0, 0
    mv_nondisp_tp, mv_nondisp_fp, mv_nondisp_fn = 0, 0, 0
    for i, inst in enumerate(data):
        gold = entity_set(inst["gold"]["entities"])
        mv_pred = majority_vote(inst, float(best_mv_th))
        agree_map = inst_agreements[i]

        for (s, e, t, txt), agree in agree_map.items():
            key = (s, e, t)
            in_pred = key in mv_pred
            in_gold = key in gold
            if agree < args.dispute_threshold:
                if in_pred and in_gold:
                    mv_disp_tp += 1
                elif in_pred and not in_gold:
                    mv_disp_fp += 1
                elif not in_pred and in_gold:
                    mv_disp_fn += 1
            else:
                if in_pred and in_gold:
                    mv_nondisp_tp += 1
                elif in_pred and not in_gold:
                    mv_nondisp_fp += 1
                elif not in_pred and in_gold:
                    mv_nondisp_fn += 1

        all_sample_keys = {(s, e, t) for (s, e, t, _) in agree_map}
        for gkey in gold:
            if gkey not in all_sample_keys:
                mv_nondisp_fn += 1

    # ---- 8. Round 2 P(yes) distribution for disputed entities ----
    r2_dist = {}
    if p_yes_all:
        pya = np.array(p_yes_all)
        r2_dist = {
            "mean": round(float(pya.mean()), 4),
            "std": round(float(pya.std()), 4),
            "median": round(float(np.median(pya)), 4),
            "q25": round(float(np.percentile(pya, 25)), 4),
            "q75": round(float(np.percentile(pya, 75)), 4),
        }

    # ---- Build result ----
    result = {
        "experiment": "MRSC_multi_round_self_consistency",
        "config": {
            "model_base": args.base_model_path,
            "adapter": args.adapter_path,
            "data": args.data_path,
            "dispute_threshold": args.dispute_threshold,
            "round2_weight": args.round2_weight,
        },
        "data_stats": {
            "n_instances": len(data),
            "n_unique_entities": total_entities,
            "n_disputed": total_disputed,
            "n_non_disputed": total_non_disputed,
            "disputed_pct": round(100 * total_disputed / max(total_entities, 1), 2),
        },
        "round2_stats": {
            "n_prompts": len(all_prompts),
            "verification_seconds": round(elapsed, 1),
            "prompts_per_second": round(len(all_prompts) / max(elapsed, 0.001), 1),
            "p_yes_distribution": r2_dist,
        },
        "construction_f1": {
            "greedy": round(greedy_f1, 4),
            "oracle": round(oracle_f1, 4),
            "majority_vote": {k: round(v, 4) for k, v in mv_res.items()},
            "best_mv": {"threshold": best_mv_th, "f1": round(best_mv_f1, 4)},
            "mrsc": {k: round(v, 4) for k, v in mrsc_res.items()},
            "best_mrsc": {"threshold": best_mrsc_th, "f1": round(best_mrsc_f1, 4)},
        },
        "deltas": {
            "mrsc_vs_greedy": round(best_mrsc_f1 - greedy_f1, 4),
            "mrsc_vs_mv": round(best_mrsc_f1 - best_mv_f1, 4),
            "mv_vs_greedy": round(best_mv_f1 - greedy_f1, 4),
        },
        "disputed_entity_breakdown": {
            "mrsc": {
                "disputed": safe_prf(disp_tp, disp_fp, disp_fn),
                "non_disputed": safe_prf(nondisp_tp, nondisp_fp, nondisp_fn),
            },
            "majority_vote": {
                "disputed": safe_prf(mv_disp_tp, mv_disp_fp, mv_disp_fn),
                "non_disputed": safe_prf(mv_nondisp_tp, mv_nondisp_fp, mv_nondisp_fn),
            },
        },
    }

    out_path = os.path.join(args.output_dir, "mrsc_results.json")
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)
    print(f"\nSaved: {out_path}")

    # ---- Print summary ----
    print(f"\n{'='*60}")
    print("MRSC Multi-Round Self-Consistency Results")
    print(f"{'='*60}")
    print(f"Instances: {len(data)}  "
          f"Entities: {total_entities} (disputed: {total_disputed}, "
          f"non-disputed: {total_non_disputed})")
    if r2_dist:
        print(f"Round 2 P(yes): mean={r2_dist['mean']}, "
              f"std={r2_dist['std']}, median={r2_dist['median']}")

    print(f"\nConstruction F1 (macro):")
    print(f"  Greedy:                  {greedy_f1:.4f}")
    print(f"  Best MV (θ={best_mv_th}):     {best_mv_f1:.4f}  "
          f"(Δ={best_mv_f1-greedy_f1:+.4f})")
    print(f"  Best MRSC (θ={best_mrsc_th}):  {best_mrsc_f1:.4f}  "
          f"(Δ={best_mrsc_f1-greedy_f1:+.4f})")
    print(f"  Oracle:                  {oracle_f1:.4f}")
    print(f"  MRSC vs MV: {best_mrsc_f1-best_mv_f1:+.4f}")

    print(f"\nDisputed entity breakdown (at best thresholds):")
    print(f"  MRSC disputed:     {safe_prf(disp_tp, disp_fp, disp_fn)}")
    print(f"  MV   disputed:     {safe_prf(mv_disp_tp, mv_disp_fp, mv_disp_fn)}")
    print(f"  MRSC non-disputed: {safe_prf(nondisp_tp, nondisp_fp, nondisp_fn)}")
    print(f"  MV   non-disputed: {safe_prf(mv_nondisp_tp, mv_nondisp_fp, mv_nondisp_fn)}")

    print(f"\nAll MV thresholds:  {mv_res}")
    print(f"All MRSC thresholds: {mrsc_res}")


if __name__ == "__main__":
    main()
