#!/usr/bin/env python3
"""Entity-Level Self-Judgment (ESJ) for structured self-consistency IE.

For each unique entity across N=8 samples, uses the FT model to do a
yes/no verification forward pass. P(yes) serves as entity-level confidence
for weighted construction.
"""

import argparse
import json
import os
import sys
import time
from collections import defaultdict

import numpy as np
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel
from scipy.stats import spearmanr
from sklearn.metrics import roc_auc_score


# ---------------------------------------------------------------------------
# Data
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


def extract_unique_entities(instance):
    """Return {(start, end, type, text): count_across_samples}."""
    emap = defaultdict(int)
    for sample in instance["samples"]:
        for e in sample.get("entities", []):
            emap[(e["start"], e["end"], e["type"], e["text"])] += 1
    return emap


# ---------------------------------------------------------------------------
# Prompt
# ---------------------------------------------------------------------------

def build_verification_prompt(sentence, entity_text, entity_type):
    return (
        f'In the following sentence, is "{entity_text}" a {entity_type} entity? '
        f'Answer only yes or no.\n\n'
        f'Sentence: {sentence}\n'
        f'Answer:'
    )


# ---------------------------------------------------------------------------
# Model
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


# ---------------------------------------------------------------------------
# Batch verification
# ---------------------------------------------------------------------------

@torch.no_grad()
def batch_verify(model, tokenizer, prompts, yes_ids, no_ids,
                 batch_size=16, device="cuda"):
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

        logits = model(**inputs).logits  # (B, L, V)

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
# Eval helpers
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


def esj_construction(instance, esj_scores, threshold):
    counts = defaultdict(int)
    N = len(instance["samples"])
    for s in instance["samples"]:
        for e in s.get("entities", []):
            counts[(e["start"], e["end"], e["type"])] += 1
    out = set()
    for key, c in counts.items():
        p_yes = esj_scores.get(key, 0.0)
        if p_yes * (c / N) >= threshold:
            out.add(key)
    return out


def safe_spearman(a, b):
    mask = np.isfinite(a) & np.isfinite(b)
    if mask.sum() < 3:
        return float("nan"), float("nan")
    return spearmanr(a[mask], b[mask])


def safe_auroc(scores, labels):
    mask = np.isfinite(scores)
    s, l = scores[mask], labels[mask]
    if len(set(l)) < 2:
        return float("nan")
    try:
        return roc_auc_score(l, s)
    except Exception:
        return float("nan")


# ---------------------------------------------------------------------------
# Within-instance sample ranking (ESJ can rank samples, LP cannot for entity-level)
# ---------------------------------------------------------------------------

def compute_sample_esj_scores(instance, esj_scores):
    """Mean P(yes) across entities in each sample."""
    per_sample = []
    for s in instance["samples"]:
        ents = s.get("entities", [])
        if not ents:
            per_sample.append(0.0)
            continue
        pyes_vals = []
        for e in ents:
            key = (e["start"], e["end"], e["type"])
            pyes_vals.append(esj_scores.get(key, 0.0))
        per_sample.append(float(np.mean(pyes_vals)))
    return per_sample


def compute_sample_lp_scores(instance):
    out = []
    for s in instance["samples"]:
        lp = s.get("mean_logprob")
        if lp is None:
            lp = s.get("cumulative_logprob", -999) / max(s.get("n_tokens", 1), 1)
        out.append(lp)
    return out


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base_model_path", type=str, required=True)
    ap.add_argument("--adapter_path", type=str, default=None)
    ap.add_argument("--data_path", type=str, required=True)
    ap.add_argument("--output_dir", type=str, required=True)
    ap.add_argument("--max_instances", type=int, default=0)
    ap.add_argument("--batch_size", type=int, default=16)
    args = ap.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    device = "cuda"

    # ---- 1. Load data ----
    print(f"Loading data from {args.data_path} ...")
    data = load_samples(args.data_path, args.max_instances)
    print(f"  {len(data)} instances loaded")

    # ---- 2. Collect unique entities ----
    print("Extracting unique entities ...")
    inst_emaps = []
    total_occ, total_uniq = 0, 0
    for inst in data:
        em = extract_unique_entities(inst)
        inst_emaps.append(em)
        total_occ += sum(em.values())
        total_uniq += len(em)
    print(f"  {total_uniq} unique entities to verify ({total_occ} total occurrences)")
    print(f"  avg {total_uniq/len(data):.1f} unique / {total_occ/len(data):.1f} total per instance")

    # ---- 3. Build prompts ----
    all_prompts = []
    prompt_idx = []  # (instance_i, (start, end, type))
    for i, inst in enumerate(data):
        for (s, e, t, txt), _ in inst_emaps[i].items():
            all_prompts.append(build_verification_prompt(inst["text"], txt, t))
            prompt_idx.append((i, (s, e, t)))
    print(f"  {len(all_prompts)} verification prompts built")

    # ---- 4. Load model ----
    model, tokenizer = load_model(args.base_model_path, args.adapter_path, device)
    yes_ids, no_ids = get_yes_no_ids(tokenizer)

    # ---- 5. Run verification ----
    print(f"Running batch verification (batch_size={args.batch_size}) ...")
    t0 = time.time()
    p_yes_all = batch_verify(model, tokenizer, all_prompts, yes_ids, no_ids,
                             args.batch_size, device)
    elapsed = time.time() - t0
    print(f"  Done in {elapsed:.1f}s ({len(all_prompts)/elapsed:.0f} prompts/s)")

    del model
    import gc; gc.collect(); torch.cuda.empty_cache()

    # ---- 6. Map P(yes) back ----
    inst_esj = [dict() for _ in range(len(data))]
    for idx, (ii, key) in enumerate(prompt_idx):
        inst_esj[ii][key] = p_yes_all[idx]

    # ---- 7. Baselines ----
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
        for i, inst in enumerate(data):
            gold = entity_set(inst["gold"]["entities"])
            fs.append(compute_prf(majority_vote(inst, th), gold)[2])
        mv_res[str(th)] = float(np.mean(fs))
    best_mv_th = max(mv_res, key=mv_res.get)
    best_mv_f1 = mv_res[best_mv_th]

    # ---- 8. ESJ construction ----
    print("Evaluating ESJ construction ...")
    esj_ths = [0.02, 0.05, 0.08, 0.1, 0.12, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]
    esj_res = {}
    for th in esj_ths:
        fs = []
        for i, inst in enumerate(data):
            gold = entity_set(inst["gold"]["entities"])
            fs.append(compute_prf(esj_construction(inst, inst_esj[i], th), gold)[2])
        esj_res[str(th)] = float(np.mean(fs))
    best_esj_th = max(esj_res, key=esj_res.get)
    best_esj_f1 = esj_res[best_esj_th]

    # ---- 9. Entity-level signal quality ----
    print("Entity-level analysis ...")
    ent_correct, ent_esj, ent_agree = [], [], []
    for i, inst in enumerate(data):
        gold = entity_set(inst["gold"]["entities"])
        N = len(inst["samples"])
        counts = defaultdict(int)
        for s in inst["samples"]:
            for e in s.get("entities", []):
                counts[(e["start"], e["end"], e["type"])] += 1
        for key, c in counts.items():
            ent_correct.append(1 if key in gold else 0)
            ent_esj.append(inst_esj[i].get(key, 0.0))
            ent_agree.append(c / N)

    ent_correct = np.array(ent_correct)
    ent_esj_arr = np.array(ent_esj)
    ent_agree_arr = np.array(ent_agree)
    ent_combined = ent_esj_arr * ent_agree_arr

    rho_esj, p_rho_esj = safe_spearman(ent_esj_arr, ent_correct.astype(float))
    rho_agree, _ = safe_spearman(ent_agree_arr, ent_correct.astype(float))
    rho_comb, _ = safe_spearman(ent_combined, ent_correct.astype(float))
    auroc_esj = safe_auroc(ent_esj_arr, ent_correct)
    auroc_agree = safe_auroc(ent_agree_arr, ent_correct)
    auroc_comb = safe_auroc(ent_combined, ent_correct)

    # ---- 10. Breakdown by agreement ----
    disputed = ent_agree_arr < 0.5
    consensus = ent_agree_arr >= 0.75
    mid = (~disputed) & (~consensus)

    def group_stats(mask, label):
        n = int(mask.sum())
        if n < 3:
            return {"n": n}
        return {
            "n": n,
            "correct_rate": round(float(ent_correct[mask].mean()), 4),
            "esj_mean": round(float(ent_esj_arr[mask].mean()), 4),
            "esj_std": round(float(ent_esj_arr[mask].std()), 4),
            "rho_esj_correct": round(float(safe_spearman(ent_esj_arr[mask], ent_correct[mask].astype(float))[0]), 4),
            "auroc_esj": round(safe_auroc(ent_esj_arr[mask], ent_correct[mask]), 4),
        }

    # ---- 11. Within-instance sample ranking ----
    print("Within-instance sample ranking ...")
    esj_rank_corrs, lp_rank_corrs = [], []
    for i, inst in enumerate(data):
        gold = entity_set(inst["gold"]["entities"])
        sample_f1s = [compute_prf(entity_set(s.get("entities", [])), gold)[2]
                      for s in inst["samples"]]
        if len(set(sample_f1s)) < 2:
            continue
        esj_sample = compute_sample_esj_scores(inst, inst_esj[i])
        lp_sample = compute_sample_lp_scores(inst)
        r_esj, _ = spearmanr(esj_sample, sample_f1s)
        r_lp, _ = spearmanr(lp_sample, sample_f1s)
        if np.isfinite(r_esj):
            esj_rank_corrs.append(r_esj)
        if np.isfinite(r_lp):
            lp_rank_corrs.append(r_lp)

    # ESJ-based selection F1 (pick best sample by ESJ score)
    esj_sel_f1s, lp_sel_f1s = [], []
    for i, inst in enumerate(data):
        gold = entity_set(inst["gold"]["entities"])
        sample_f1s = [compute_prf(entity_set(s.get("entities", [])), gold)[2]
                      for s in inst["samples"]]
        esj_sample = compute_sample_esj_scores(inst, inst_esj[i])
        lp_sample = compute_sample_lp_scores(inst)
        esj_sel_f1s.append(sample_f1s[int(np.argmax(esj_sample))])
        lp_sel_f1s.append(sample_f1s[int(np.argmax(lp_sample))])

    # ---- 12. P(yes) distribution ----
    pya = np.array(p_yes_all)
    p_yes_dist = {
        "mean": round(float(pya.mean()), 4),
        "std": round(float(pya.std()), 4),
        "median": round(float(np.median(pya)), 4),
        "q25": round(float(np.percentile(pya, 25)), 4),
        "q75": round(float(np.percentile(pya, 75)), 4),
    }

    # ---- Build result ----
    result = {
        "experiment": "ESJ_entity_self_judgment",
        "model_base": args.base_model_path,
        "adapter": args.adapter_path,
        "data": args.data_path,
        "n_instances": len(data),
        "n_unique_entities": total_uniq,
        "n_entity_occurrences": total_occ,
        "avg_unique_per_instance": round(total_uniq / len(data), 2),
        "verification_seconds": round(elapsed, 1),
        "prompts_per_second": round(len(all_prompts) / elapsed, 1),
        "p_yes_distribution": p_yes_dist,
        "construction_f1": {
            "greedy": round(greedy_f1, 4),
            "oracle": round(oracle_f1, 4),
            "majority_vote": {k: round(v, 4) for k, v in mv_res.items()},
            "best_mv": {"threshold": best_mv_th, "f1": round(best_mv_f1, 4)},
            "esj_weighted": {k: round(v, 4) for k, v in esj_res.items()},
            "best_esj": {"threshold": best_esj_th, "f1": round(best_esj_f1, 4)},
        },
        "deltas": {
            "esj_vs_greedy": round(best_esj_f1 - greedy_f1, 4),
            "esj_vs_mv": round(best_esj_f1 - best_mv_f1, 4),
            "mv_vs_greedy": round(best_mv_f1 - greedy_f1, 4),
        },
        "entity_signal_quality": {
            "n_entities": len(ent_correct),
            "overall_correct_rate": round(float(ent_correct.mean()), 4),
            "esj": {"rho": round(float(rho_esj), 4), "auroc": round(float(auroc_esj), 4)},
            "agreement": {"rho": round(float(rho_agree), 4), "auroc": round(float(auroc_agree), 4)},
            "esj_x_agreement": {"rho": round(float(rho_comb), 4), "auroc": round(float(auroc_comb), 4)},
        },
        "agreement_breakdown": {
            "disputed_lt0.5": group_stats(disputed, "disputed"),
            "mid_0.5_0.75": group_stats(mid, "mid"),
            "consensus_gte0.75": group_stats(consensus, "consensus"),
        },
        "within_instance_ranking": {
            "esj_mean_rho": round(float(np.mean(esj_rank_corrs)), 4) if esj_rank_corrs else None,
            "lp_mean_rho": round(float(np.mean(lp_rank_corrs)), 4) if lp_rank_corrs else None,
            "n_rankable_instances": len(esj_rank_corrs),
            "esj_selection_f1": round(float(np.mean(esj_sel_f1s)), 4),
            "lp_selection_f1": round(float(np.mean(lp_sel_f1s)), 4),
        },
    }

    out_path = os.path.join(args.output_dir, "esj_results.json")
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)
    print(f"\nSaved: {out_path}")

    # ---- Print summary ----
    print(f"\n{'='*60}")
    print("ESJ Entity-Level Self-Judgment Results")
    print(f"{'='*60}")
    print(f"Instances: {len(data)}  Unique entities verified: {total_uniq}")
    print(f"P(yes): mean={p_yes_dist['mean']}, std={p_yes_dist['std']}, median={p_yes_dist['median']}")
    print(f"\nConstruction F1 (macro):")
    print(f"  Greedy:              {greedy_f1:.4f}")
    print(f"  Best MV (θ={best_mv_th}):  {best_mv_f1:.4f}  (Δ={best_mv_f1-greedy_f1:+.4f})")
    print(f"  Best ESJ (θ={best_esj_th}): {best_esj_f1:.4f}  (Δ={best_esj_f1-greedy_f1:+.4f})")
    print(f"  Oracle:              {oracle_f1:.4f}")
    print(f"  ESJ vs MV: {best_esj_f1-best_mv_f1:+.4f}")
    print(f"\nEntity-level signal:")
    print(f"  ESJ         ρ={rho_esj:+.4f}  AUROC={auroc_esj:.4f}")
    print(f"  Agreement   ρ={rho_agree:+.4f}  AUROC={auroc_agree:.4f}")
    print(f"  ESJ×Agree   ρ={rho_comb:+.4f}  AUROC={auroc_comb:.4f}")
    print(f"\nWithin-instance ranking (rho with sample F1):")
    if esj_rank_corrs:
        print(f"  ESJ: {np.mean(esj_rank_corrs):+.4f} ({len(esj_rank_corrs)} instances)")
    if lp_rank_corrs:
        print(f"  LP:  {np.mean(lp_rank_corrs):+.4f} ({len(lp_rank_corrs)} instances)")
    print(f"\nSelection F1 (pick best sample):")
    print(f"  ESJ: {np.mean(esj_sel_f1s):.4f}  LP: {np.mean(lp_sel_f1s):.4f}  Greedy: {greedy_f1:.4f}")
    print(f"\nBreakdown by agreement:")
    for label, mask in [("Disputed (<0.5)", disputed), ("Mid [0.5,0.75)", mid), ("Consensus (≥0.75)", consensus)]:
        n = mask.sum()
        if n >= 3:
            print(f"  {label}: n={n}, correct={ent_correct[mask].mean():.3f}, "
                  f"ESJ_mean={ent_esj_arr[mask].mean():.3f}, "
                  f"AUROC={safe_auroc(ent_esj_arr[mask], ent_correct[mask]):.4f}")


if __name__ == "__main__":
    main()
