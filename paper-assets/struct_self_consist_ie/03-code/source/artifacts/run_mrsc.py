#!/usr/bin/env python3
"""Multi-Round Iterative Self-Consistency for IE (MRSC).

Round 1: Analyze N inference samples, identify disputed entities (agreement < threshold).
Round 2: Re-prompt model with yes/no verification on disputed entities.
Weighted aggregation: combine round 1 agreement + round 2 P(yes) for final prediction.
"""

import argparse
import json
import os
import sys
import time
from collections import Counter, defaultdict

import torch
import torch.nn.functional as F
from transformers import AutoModelForCausalLM, AutoTokenizer

# ── Entity helpers ──────────────────────────────────────────────────────────

def entity_key(e):
    return (e["start"], e["end"], e["type"])


def entity_set(entities):
    return {entity_key(e) for e in entities}


def compute_prf(pred, gold):
    if not gold and not pred:
        return 1.0, 1.0, 1.0
    if not pred or not gold:
        return 0.0, 0.0, 0.0
    tp = len(pred & gold)
    if tp == 0:
        return 0.0, 0.0, 0.0
    p, r = tp / len(pred), tp / len(gold)
    return p, r, 2 * p * r / (p + r)


# ── Round 1: Agreement analysis ────────────────────────────────────────────

def analyze_agreement(instance, n_samples):
    """Return {entity_key: agreement_ratio} and {entity_key: entity_dict}."""
    samples = instance["samples"][:n_samples]
    N = len(samples)
    if N == 0:
        return {}, {}

    entity_counts = Counter()
    entity_info = {}
    for s in samples:
        seen = set()
        for e in s.get("entities", []):
            k = entity_key(e)
            if k not in seen:
                entity_counts[k] += 1
                seen.add(k)
            if k not in entity_info:
                entity_info[k] = e

    agreement = {k: cnt / N for k, cnt in entity_counts.items()}
    return agreement, entity_info


# ── Yes/No token IDs ───────────────────────────────────────────────────────

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
    return list(set(yes_ids)), list(set(no_ids))


# ── Verification prompt ────────────────────────────────────────────────────

def build_verify_prompt(tokenizer, text, entity_text, entity_type, count, total):
    content = (
        f'In the sentence below, is "{entity_text}" a {entity_type} entity? '
        f"Multiple extraction attempts disagreed ({count}/{total} samples included it). "
        f"Answer only yes or no.\n\n"
        f"Sentence: {text}\n"
        f"Answer:"
    )
    messages = [{"role": "user", "content": content}]
    try:
        return tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True,
            enable_thinking=False,
        )
    except TypeError:
        return tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True,
        )


# ── Batch verification ─────────────────────────────────────────────────────

@torch.no_grad()
def batch_verify(model, tokenizer, prompts, yes_ids, no_ids,
                 batch_size=16, device="cuda"):
    """Return P(yes) for each prompt via single forward pass."""
    all_p_yes = []
    yes_t = torch.tensor(yes_ids, device=device)
    no_t = torch.tensor(no_ids, device=device)

    for i in range(0, len(prompts), batch_size):
        batch = prompts[i:i + batch_size]
        enc = tokenizer(
            batch, return_tensors="pt", padding=True, truncation=True,
            max_length=2048,
        ).to(device)
        out = model(**enc)
        # logits at last non-padding position for each sequence
        for j in range(len(batch)):
            attn = enc["attention_mask"][j]
            last_pos = attn.sum().item() - 1
            logits = out.logits[j, last_pos]
            yes_logits = logits[yes_t]
            no_logits = logits[no_t]
            all_logits = torch.cat([yes_logits, no_logits])
            probs = F.softmax(all_logits, dim=0)
            p_yes = probs[:len(yes_ids)].sum().item()
            all_p_yes.append(p_yes)

    return all_p_yes


# ── Majority vote baseline ─────────────────────────────────────────────────

def majority_vote(agreement, threshold):
    """Return set of entity keys with agreement >= threshold."""
    return {k for k, v in agreement.items() if v >= threshold}


# ── MRSC aggregation ───────────────────────────────────────────────────────

def mrsc_aggregate(agreement, r2_scores, dispute_threshold, r2_weight,
                   decision_threshold):
    """Combine round 1 + round 2 scores for final entity set."""
    result = set()
    for k, agr in agreement.items():
        if agr >= dispute_threshold:
            result.add(k)
        else:
            p_yes = r2_scores.get(k, 0.0)
            combined = (agr * 1.0 + p_yes * r2_weight) / (1.0 + r2_weight)
            if combined >= decision_threshold:
                result.add(k)
    return result


# ── Oracle ──────────────────────────────────────────────────────────────────

def oracle_selection(agreement, gold_set):
    """Per-entity oracle: include iff entity is in gold."""
    return {k for k in agreement if k in gold_set}


# ── Main ────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="MRSC: Multi-Round SC for IE")
    parser.add_argument("--base_model_path", required=True)
    parser.add_argument("--adapter_path", default=None)
    parser.add_argument("--data_path", required=True)
    parser.add_argument("--output_dir", required=True)
    parser.add_argument("--dispute_threshold", type=float, default=0.6)
    parser.add_argument("--round2_weight", type=float, default=2.0)
    parser.add_argument("--batch_size", type=int, default=16)
    parser.add_argument("--max_instances", type=int, default=0)
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    device = "cuda:0"

    # ── Load model ──────────────────────────────────────────────────────
    print(f"[MRSC] Loading model from {args.base_model_path}")
    t0 = time.time()
    tokenizer = AutoTokenizer.from_pretrained(
        args.base_model_path, trust_remote_code=True, padding_side="left",
    )
    if tokenizer.pad_token_id is None:
        tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(
        args.base_model_path, torch_dtype=torch.bfloat16,
        device_map=device, trust_remote_code=True,
    )
    if args.adapter_path:
        from peft import PeftModel
        model = PeftModel.from_pretrained(model, args.adapter_path)
        model = model.merge_and_unload()
    model.eval()
    print(f"[MRSC] Model loaded in {time.time()-t0:.1f}s")

    yes_ids, no_ids = get_yes_no_ids(tokenizer)
    print(f"[MRSC] Yes token IDs: {yes_ids}, No token IDs: {no_ids}")
    if not yes_ids or not no_ids:
        print("[MRSC] WARNING: Could not find yes/no token IDs!")
        sys.exit(1)

    # ── Load data ───────────────────────────────────────────────────────
    print(f"[MRSC] Loading data from {args.data_path}")
    instances = []
    with open(args.data_path) as f:
        for line in f:
            instances.append(json.loads(line))
    if args.max_instances > 0:
        instances = instances[:args.max_instances]
    print(f"[MRSC] Loaded {len(instances)} instances")

    # ── Round 1: Analyze agreement ──────────────────────────────────────
    print("[MRSC] Round 1: Analyzing agreement...")
    r1_data = []
    total_entities = 0
    total_disputed = 0
    all_verify_tasks = []  # (instance_idx, entity_key, prompt)

    for idx, inst in enumerate(instances):
        agreement, entity_info = analyze_agreement(inst, n_samples=len(inst["samples"]))
        N = len(inst["samples"])
        gold_ents = entity_set(inst["gold"]["entities"])

        disputed = {}
        for k, agr in agreement.items():
            if agr < args.dispute_threshold:
                disputed[k] = agr
                e = entity_info[k]
                count = int(agr * N + 0.5)
                prompt = build_verify_prompt(
                    tokenizer, inst["text"], e["text"], e["type"], count, N,
                )
                all_verify_tasks.append((idx, k, prompt))

        total_entities += len(agreement)
        total_disputed += len(disputed)
        r1_data.append({
            "agreement": agreement,
            "entity_info": entity_info,
            "gold": gold_ents,
            "n_samples": N,
        })

    print(f"[MRSC] Total unique entities: {total_entities}, "
          f"Disputed (agr < {args.dispute_threshold}): {total_disputed}")
    print(f"[MRSC] Verification prompts to run: {len(all_verify_tasks)}")

    # ── Round 2: Batch verification ─────────────────────────────────────
    r2_scores = defaultdict(dict)  # idx -> {entity_key: p_yes}

    if all_verify_tasks:
        print(f"[MRSC] Round 2: Running verification ({len(all_verify_tasks)} prompts)...")
        prompts = [t[2] for t in all_verify_tasks]
        t1 = time.time()
        p_yes_list = batch_verify(
            model, tokenizer, prompts, yes_ids, no_ids,
            batch_size=args.batch_size, device=device,
        )
        print(f"[MRSC] Verification done in {time.time()-t1:.1f}s")

        for (inst_idx, ek, _), p_yes in zip(all_verify_tasks, p_yes_list):
            r2_scores[inst_idx][ek] = p_yes
    else:
        print("[MRSC] No disputed entities, skipping round 2")

    # ── Evaluate across thresholds ──────────────────────────────────────
    thresholds = [0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]
    mv_thresholds = [t / 8.0 * i for i in range(1, 9)]
    mv_thresholds = sorted(set(
        [round(k / len(instances[0]["samples"]), 4)
         for inst in instances[:1]
         for k in range(1, len(inst["samples"]) + 1)]
    ))

    results = {
        "config": {
            "dispute_threshold": args.dispute_threshold,
            "round2_weight": args.round2_weight,
            "n_instances": len(instances),
            "total_entities": total_entities,
            "total_disputed": total_disputed,
        },
        "greedy": {},
        "majority_vote": {},
        "mrsc": {},
        "oracle": {},
    }

    # Greedy baseline
    greedy_ps, greedy_rs, greedy_fs = [], [], []
    for idx, inst in enumerate(instances):
        gold = r1_data[idx]["gold"]
        greedy = entity_set(inst["greedy"]["entities"])
        p, r, f = compute_prf(greedy, gold)
        greedy_ps.append(p)
        greedy_rs.append(r)
        greedy_fs.append(f)
    results["greedy"] = {
        "P": sum(greedy_ps) / len(greedy_ps),
        "R": sum(greedy_rs) / len(greedy_rs),
        "F1": sum(greedy_fs) / len(greedy_fs),
    }
    print(f"\n[MRSC] Greedy: P={results['greedy']['P']:.4f} "
          f"R={results['greedy']['R']:.4f} F1={results['greedy']['F1']:.4f}")

    # Oracle
    oracle_ps, oracle_rs, oracle_fs = [], [], []
    for idx in range(len(instances)):
        gold = r1_data[idx]["gold"]
        pred = oracle_selection(r1_data[idx]["agreement"], gold)
        p, r, f = compute_prf(pred, gold)
        oracle_ps.append(p)
        oracle_rs.append(r)
        oracle_fs.append(f)
    results["oracle"] = {
        "P": sum(oracle_ps) / len(oracle_ps),
        "R": sum(oracle_rs) / len(oracle_rs),
        "F1": sum(oracle_fs) / len(oracle_fs),
    }
    print(f"[MRSC] Oracle:  P={results['oracle']['P']:.4f} "
          f"R={results['oracle']['R']:.4f} F1={results['oracle']['F1']:.4f}")

    # Majority vote sweep
    N0 = len(instances[0]["samples"])
    mv_thresholds = sorted(set([round(k / N0, 6) for k in range(1, N0 + 1)]))
    print(f"\n[MRSC] Majority vote sweep (N={N0}):")
    best_mv_f1, best_mv_t = 0, 0
    for t in mv_thresholds:
        ps, rs, fs = [], [], []
        for idx in range(len(instances)):
            gold = r1_data[idx]["gold"]
            pred = majority_vote(r1_data[idx]["agreement"], t)
            p, r, f = compute_prf(pred, gold)
            ps.append(p)
            rs.append(r)
            fs.append(f)
        avg_f1 = sum(fs) / len(fs)
        results["majority_vote"][str(t)] = {
            "P": sum(ps) / len(ps),
            "R": sum(rs) / len(rs),
            "F1": avg_f1,
        }
        marker = ""
        if avg_f1 > best_mv_f1:
            best_mv_f1 = avg_f1
            best_mv_t = t
            marker = " *best*"
        print(f"  θ={t:.4f}: P={sum(ps)/len(ps):.4f} R={sum(rs)/len(rs):.4f} "
              f"F1={avg_f1:.4f}{marker}")

    # MRSC sweep
    print(f"\n[MRSC] MRSC sweep (dispute_thr={args.dispute_threshold}, "
          f"r2_weight={args.round2_weight}):")
    best_mrsc_f1, best_mrsc_t = 0, 0
    for t in thresholds:
        ps, rs, fs = [], [], []
        for idx in range(len(instances)):
            gold = r1_data[idx]["gold"]
            pred = mrsc_aggregate(
                r1_data[idx]["agreement"], r2_scores.get(idx, {}),
                args.dispute_threshold, args.round2_weight, t,
            )
            p, r, f = compute_prf(pred, gold)
            ps.append(p)
            rs.append(r)
            fs.append(f)
        avg_f1 = sum(fs) / len(fs)
        results["mrsc"][str(t)] = {
            "P": sum(ps) / len(ps),
            "R": sum(rs) / len(rs),
            "F1": avg_f1,
        }
        marker = ""
        if avg_f1 > best_mrsc_f1:
            best_mrsc_f1 = avg_f1
            best_mrsc_t = t
            marker = " *best*"
        print(f"  θ={t:.4f}: P={sum(ps)/len(ps):.4f} R={sum(rs)/len(rs):.4f} "
              f"F1={avg_f1:.4f}{marker}")

    # ── Disputed-only analysis ──────────────────────────────────────────
    print("\n[MRSC] Disputed entity analysis:")
    n_disputed_in_gold = 0
    n_disputed_recovered_mv = 0
    n_disputed_recovered_mrsc = 0
    n_disputed_total = 0
    for idx in range(len(instances)):
        gold = r1_data[idx]["gold"]
        agr = r1_data[idx]["agreement"]
        r2 = r2_scores.get(idx, {})
        for k, a in agr.items():
            if a < args.dispute_threshold:
                n_disputed_total += 1
                in_gold = k in gold
                if in_gold:
                    n_disputed_in_gold += 1
                # best MV would include if agr >= best_mv_t
                if a >= best_mv_t and in_gold:
                    n_disputed_recovered_mv += 1
                # MRSC recovery at best threshold
                p_yes = r2.get(k, 0.0)
                combined = (a * 1.0 + p_yes * args.round2_weight) / (1.0 + args.round2_weight)
                if combined >= best_mrsc_t and in_gold:
                    n_disputed_recovered_mrsc += 1

    print(f"  Total disputed: {n_disputed_total}")
    print(f"  Disputed in gold: {n_disputed_in_gold}")
    print(f"  Recovered by MV (θ={best_mv_t:.4f}): {n_disputed_recovered_mv}")
    print(f"  Recovered by MRSC (θ={best_mrsc_t:.4f}): {n_disputed_recovered_mrsc}")

    # ── P(yes) distribution for disputed entities ───────────────────────
    if all_verify_tasks:
        p_yes_in_gold = []
        p_yes_not_in_gold = []
        for (inst_idx, ek, _), p_yes in zip(all_verify_tasks, p_yes_list):
            gold = r1_data[inst_idx]["gold"]
            if ek in gold:
                p_yes_in_gold.append(p_yes)
            else:
                p_yes_not_in_gold.append(p_yes)
        results["r2_pyes_distribution"] = {
            "in_gold_mean": sum(p_yes_in_gold) / len(p_yes_in_gold) if p_yes_in_gold else 0,
            "in_gold_count": len(p_yes_in_gold),
            "not_in_gold_mean": sum(p_yes_not_in_gold) / len(p_yes_not_in_gold) if p_yes_not_in_gold else 0,
            "not_in_gold_count": len(p_yes_not_in_gold),
        }
        print(f"\n[MRSC] P(yes) distribution:")
        print(f"  In gold:     mean={results['r2_pyes_distribution']['in_gold_mean']:.4f} "
              f"(n={results['r2_pyes_distribution']['in_gold_count']})")
        print(f"  Not in gold: mean={results['r2_pyes_distribution']['not_in_gold_mean']:.4f} "
              f"(n={results['r2_pyes_distribution']['not_in_gold_count']})")

    # ── Summary ─────────────────────────────────────────────────────────
    results["summary"] = {
        "greedy_f1": results["greedy"]["F1"],
        "best_mv_f1": best_mv_f1,
        "best_mv_threshold": best_mv_t,
        "best_mrsc_f1": best_mrsc_f1,
        "best_mrsc_threshold": best_mrsc_t,
        "oracle_f1": results["oracle"]["F1"],
        "mrsc_vs_mv_delta": best_mrsc_f1 - best_mv_f1,
    }
    print(f"\n{'='*60}")
    print(f"[MRSC] SUMMARY")
    print(f"  Greedy F1:    {results['greedy']['F1']:.4f}")
    print(f"  Best MV F1:   {best_mv_f1:.4f} (θ={best_mv_t:.4f})")
    print(f"  Best MRSC F1: {best_mrsc_f1:.4f} (θ={best_mrsc_t:.4f})")
    print(f"  Oracle F1:    {results['oracle']['F1']:.4f}")
    print(f"  MRSC vs MV:   {best_mrsc_f1 - best_mv_f1:+.4f}")
    print(f"{'='*60}")

    # ── Save ────────────────────────────────────────────────────────────
    out_path = os.path.join(args.output_dir, "mrsc_results.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\n[MRSC] Results saved to {out_path}")


if __name__ == "__main__":
    main()
