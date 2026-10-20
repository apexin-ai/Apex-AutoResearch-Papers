#!/usr/bin/env python3
"""Latent Self-Consistency: entity-level hidden state aggregation for IE.

Hypothesis: Hidden states contain richer per-sample information than scalar LP.
Entity-level mean-pooled hidden representations enable latent aggregation
(centroid selection, latent confidence scoring) that bypasses LP compression.
"""

import argparse
import json
import os
import random
import time
from collections import defaultdict

import torch
import torch.nn.functional as F
from scipy.stats import spearmanr
from transformers import AutoModelForCausalLM, AutoTokenizer

SCHEMA_HINT = (
    "Entity types: person, organization, location, building, "
    "art, product, event, other"
)

PROMPT_TPL = (
    "Extract all structured information (entities and relations) from the "
    "following text. Output a JSON object.\n\n"
    "Text: {text}\n"
    "{schema}\n\n"
    'Output format: {{"entities": [...], "relations": [...], "events": []}}\n'
    "For relations, head is the subject entity and tail is the object entity."
)


def build_prompt(text):
    return PROMPT_TPL.format(text=text, schema=SCHEMA_HINT)


def apply_chat(tokenizer, prompt):
    msgs = [{"role": "user", "content": prompt}]
    try:
        return tokenizer.apply_chat_template(
            msgs, tokenize=False, add_generation_prompt=True,
            enable_thinking=False,
        )
    except TypeError:
        return tokenizer.apply_chat_template(
            msgs, tokenize=False, add_generation_prompt=True,
        )


def get_output_text(sample):
    """Reconstruct model output from token_texts (preserves original generation)."""
    if "token_texts" in sample and sample["token_texts"]:
        return "".join(
            t for t in sample["token_texts"]
            if not (t.startswith("<|") and t.endswith("|>"))
        )
    return json.dumps({
        "entities": sample.get("entities", []),
        "relations": sample.get("relations", []),
        "events": sample.get("events", []),
    }, ensure_ascii=False)


def eset(entities):
    return {(e["start"], e["end"], e["type"]) for e in entities}


def prf(pred, gold):
    if not gold and not pred:
        return 1.0, 1.0, 1.0
    if not pred or not gold:
        return 0.0, 0.0, 0.0
    tp = len(pred & gold)
    if tp == 0:
        return 0.0, 0.0, 0.0
    p, r = tp / len(pred), tp / len(gold)
    return p, r, 2 * p * r / (p + r)


def find_entity_spans(tokenizer, output_text, entities):
    """Map entity text to token index ranges within output_text."""
    enc = tokenizer(output_text, return_offsets_mapping=True, add_special_tokens=False)
    offsets = enc["offset_mapping"]
    result = {}
    search_from = 0

    for e in entities:
        key = (e["start"], e["end"], e["type"])
        if key in result:
            continue
        pattern = '"text": "' + e["text"] + '"'
        pos = output_text.find(pattern, search_from)
        if pos == -1:
            pos = output_text.find(pattern)
        if pos == -1:
            char_s = output_text.find(e["text"])
            if char_s == -1:
                continue
        else:
            char_s = pos + len('"text": "')
            search_from = pos + len(pattern)
        char_e = char_s + len(e["text"])

        tok_s, tok_e = None, None
        for ti, (cs, ce) in enumerate(offsets):
            if cs == ce:
                continue
            if tok_s is None and ce > char_s:
                tok_s = ti
            if cs < char_e:
                tok_e = ti + 1
        if tok_s is not None and tok_e is not None and tok_s < tok_e:
            result[key] = (tok_s, tok_e)

    return result


@torch.no_grad()
def process_sample(model, tokenizer, chat_prompt, prompt_len, sample, layer, device):
    """Forward pass + entity-level mean pooling for one sample."""
    output_text = get_output_text(sample)
    full_text = chat_prompt + output_text
    input_ids = tokenizer.encode(full_text, add_special_tokens=False)
    if len(input_ids) > 2048:
        input_ids = input_ids[:2048]

    tensor = torch.tensor([input_ids], device=device)
    outputs = model(tensor, output_hidden_states=True)
    hidden = outputs.hidden_states[layer][0]  # (seq_len, hidden_size)
    output_hidden = hidden[prompt_len:].cpu().float()
    del outputs, hidden, tensor
    torch.cuda.empty_cache()

    entities = sample.get("entities", [])
    spans = find_entity_spans(tokenizer, output_text, entities)

    entity_vecs = {}
    for e in entities:
        key = (e["start"], e["end"], e["type"])
        if key in spans:
            ts, te = spans[key]
            if te <= output_hidden.shape[0]:
                entity_vecs[key] = output_hidden[ts:te].mean(dim=0)

    fingerprint = torch.stack(list(entity_vecs.values())).mean(dim=0) if entity_vecs else None
    return entity_vecs, fingerprint, len(entities), len(entity_vecs)


# ---------------------------------------------------------------------------
# Aggregation methods
# ---------------------------------------------------------------------------

def centroid_selection(fingerprints, samples, gold_set):
    """A) Pick sample whose entity fingerprint is closest to centroid."""
    valid = [(i, fp) for i, fp in enumerate(fingerprints) if fp is not None]
    if len(valid) < 2:
        return None, None
    centroid = torch.stack([fp for _, fp in valid]).mean(dim=0)
    best_i = max(valid, key=lambda x: F.cosine_similarity(
        x[1].unsqueeze(0), centroid.unsqueeze(0)).item())[0]
    _, _, f1 = prf(eset(samples[best_i]["entities"]), gold_set)
    return f1, best_i


def latent_entity_confidence(vecs_by_key, n_samples, gold_set, thresholds):
    """B) Entity inclusion based on hidden state consistency × frequency."""
    confidence = {}
    for key, vecs in vecs_by_key.items():
        freq = len(vecs) / n_samples
        if len(vecs) < 2:
            confidence[key] = freq
            continue
        stacked = torch.stack(vecs)
        normed = F.normalize(stacked, dim=1)
        sim = normed @ normed.T
        n = len(vecs)
        mask = torch.triu(torch.ones(n, n, dtype=torch.bool), diagonal=1)
        mean_sim = sim[mask].mean().item()
        confidence[key] = mean_sim * freq

    best_f1, best_t = 0.0, 0.0
    for t in thresholds:
        pred = {k for k, c in confidence.items() if c >= t}
        _, _, f1 = prf(pred, gold_set)
        if f1 > best_f1:
            best_f1, best_t = f1, t
    return best_f1, best_t


def majority_vote(samples, gold_set, thresholds):
    counts = defaultdict(int)
    for s in samples:
        for e in s["entities"]:
            counts[(e["start"], e["end"], e["type"])] += 1
    n = len(samples)
    best_f1, best_t = 0.0, 0.0
    for t in thresholds:
        pred = {k for k, c in counts.items() if c / n >= t}
        _, _, f1 = prf(pred, gold_set)
        if f1 > best_f1:
            best_f1, best_t = f1, t
    return best_f1, best_t


def lp_selection(samples, gold_set):
    best_i = max(range(len(samples)), key=lambda i: samples[i].get("mean_logprob", -999))
    _, _, f1 = prf(eset(samples[best_i]["entities"]), gold_set)
    return f1, best_i


def oracle_selection(samples, gold_set):
    best_f1, best_i = 0.0, 0
    for i, s in enumerate(samples):
        _, _, f1 = prf(eset(s["entities"]), gold_set)
        if f1 > best_f1:
            best_f1, best_i = f1, i
    return best_f1, best_i


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base_model_path", required=True)
    ap.add_argument("--adapter_path", default=None)
    ap.add_argument("--data_path", required=True)
    ap.add_argument("--output_dir", required=True)
    ap.add_argument("--hidden_layer", type=int, default=-1)
    ap.add_argument("--batch_size", type=int, default=2, help="reserved (individual forward passes used)")
    ap.add_argument("--max_instances", type=int, default=0)
    ap.add_argument("--subsample_seed", type=int, default=42)
    args = ap.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)

    # --- Data ---
    print("Loading data...")
    with open(args.data_path) as f:
        data = [json.loads(line) for line in f if line.strip()]
    print(f"  Total: {len(data)}")

    data = [d for d in data if d["gold"].get("entities")]
    print(f"  Gold-filtered: {len(data)}")

    if 0 < args.max_instances < len(data):
        random.seed(args.subsample_seed)
        data = random.sample(data, args.max_instances)
        print(f"  Subsampled: {len(data)}")

    n_samples = len(data[0]["samples"])
    print(f"  {n_samples} samples/instance, {len(data)} instances")

    # --- Model ---
    print("Loading model...")
    tokenizer = AutoTokenizer.from_pretrained(args.base_model_path, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        args.base_model_path,
        torch_dtype=torch.bfloat16,
        device_map="cuda:0",
        trust_remote_code=True,
    )
    if args.adapter_path:
        from peft import PeftModel
        model = PeftModel.from_pretrained(model, args.adapter_path)
        model = model.merge_and_unload()
    model.eval()
    print(f"  hidden_size={model.config.hidden_size}")

    thresholds = [i * 0.05 for i in range(1, 21)]
    R = defaultdict(list)
    t0 = time.time()

    for idx, inst in enumerate(data):
        gold_set = eset(inst["gold"]["entities"])
        samples = inst["samples"]
        greedy = inst.get("greedy", samples[0])

        # --- Baselines (no forward pass) ---
        _, _, greedy_f1 = prf(eset(greedy["entities"]), gold_set)
        mv_f1, _ = majority_vote(samples, gold_set, thresholds)
        lp_f1, lp_idx = lp_selection(samples, gold_set)
        orc_f1, _ = oracle_selection(samples, gold_set)

        # --- Forward pass: extract entity hidden vectors ---
        prompt = build_prompt(inst["text"])
        chat_prompt = apply_chat(tokenizer, prompt)
        prompt_len = len(tokenizer.encode(chat_prompt, add_special_tokens=False))

        fingerprints = []
        vecs_by_key = defaultdict(list)
        total_ent, matched_ent = 0, 0

        for si, s in enumerate(samples):
            evecs, fp, n_ent, n_matched = process_sample(
                model, tokenizer, chat_prompt, prompt_len, s,
                args.hidden_layer, "cuda:0",
            )
            fingerprints.append(fp)
            total_ent += n_ent
            matched_ent += n_matched
            for k, v in evecs.items():
                vecs_by_key[k].append(v)

        match_rate = matched_ent / max(total_ent, 1)

        # --- Method A: Centroid Selection ---
        cent_f1, cent_idx = centroid_selection(fingerprints, samples, gold_set)

        # --- Method B: Latent Entity Confidence ---
        lat_f1, lat_t = latent_entity_confidence(vecs_by_key, n_samples, gold_set, thresholds)

        # --- Method C: LP vs Latent ranking ---
        lp_scores = [s.get("mean_logprob", -999) for s in samples]
        valid_fps = [(i, fp) for i, fp in enumerate(fingerprints) if fp is not None]
        rho = None
        if len(valid_fps) >= 3:
            centroid = torch.stack([fp for _, fp in valid_fps]).mean(dim=0)
            lat_scores = [
                F.cosine_similarity(fp.unsqueeze(0), centroid.unsqueeze(0)).item()
                for _, fp in valid_fps
            ]
            lp_sub = [lp_scores[i] for i, _ in valid_fps]
            rho_val, _ = spearmanr(lp_sub, lat_scores)
            if rho_val == rho_val:  # NaN guard
                rho = float(rho_val)

        # --- Record ---
        R["id"].append(inst.get("id", str(idx)))
        R["greedy_f1"].append(greedy_f1)
        R["mv_f1"].append(mv_f1)
        R["lp_f1"].append(lp_f1)
        R["cent_f1"].append(cent_f1)
        R["lat_f1"].append(lat_f1)
        R["oracle_f1"].append(orc_f1)
        R["rho"].append(rho)
        R["match_rate"].append(match_rate)

        del fingerprints, vecs_by_key
        torch.cuda.empty_cache()

        if (idx + 1) % 50 == 0:
            elapsed = time.time() - t0
            eta = elapsed / (idx + 1) * (len(data) - idx - 1)
            avg_mr = sum(R["match_rate"]) / len(R["match_rate"])
            print(f"  [{idx+1}/{len(data)}] {elapsed:.0f}s ETA {eta:.0f}s match={avg_mr:.3f}")

    elapsed = time.time() - t0

    # --- Summary ---
    def avg(lst):
        v = [x for x in lst if x is not None]
        return sum(v) / len(v) if v else 0.0

    # Head-to-head: centroid vs LP
    cent_wins = sum(1 for c, l in zip(R["cent_f1"], R["lp_f1"])
                    if c is not None and c > l)
    cent_losses = sum(1 for c, l in zip(R["cent_f1"], R["lp_f1"])
                      if c is not None and c < l)
    cent_ties = sum(1 for c, l in zip(R["cent_f1"], R["lp_f1"])
                    if c is not None and c == l)
    cent_coverage = sum(1 for c in R["cent_f1"] if c is not None)

    summary = {
        "n_instances": len(data),
        "n_samples": n_samples,
        "elapsed_s": round(elapsed, 1),
        "entity_match_rate": round(avg(R["match_rate"]), 4),
        "metrics": {
            "greedy_f1": round(avg(R["greedy_f1"]), 4),
            "majority_vote_f1": round(avg(R["mv_f1"]), 4),
            "lp_selection_f1": round(avg(R["lp_f1"]), 4),
            "centroid_selection_f1": round(avg(R["cent_f1"]), 4),
            "latent_entity_conf_f1": round(avg(R["lat_f1"]), 4),
            "oracle_f1": round(avg(R["oracle_f1"]), 4),
        },
        "centroid_vs_lp": {
            "wins": cent_wins,
            "losses": cent_losses,
            "ties": cent_ties,
            "coverage": cent_coverage,
        },
        "lp_vs_latent_rho": {
            "mean": round(avg(R["rho"]), 4),
            "n_valid": sum(1 for x in R["rho"] if x is not None),
        },
        "config": vars(args),
    }

    print(f"\n{'='*60}")
    for k, v in summary["metrics"].items():
        print(f"  {k}: {v}")
    rho_info = summary["lp_vs_latent_rho"]
    print(f"  lp_vs_latent_rho: {rho_info['mean']} (n={rho_info['n_valid']})")
    print(f"  centroid_vs_lp: W{cent_wins}/L{cent_losses}/T{cent_ties} "
          f"(coverage={cent_coverage}/{len(data)})")
    print(f"  entity_match_rate: {summary['entity_match_rate']}")
    print(f"  elapsed: {elapsed:.1f}s")

    out_results = os.path.join(args.output_dir, "lsc_results.json")
    out_summary = os.path.join(args.output_dir, "lsc_summary.json")
    with open(out_results, "w") as f:
        json.dump(dict(R), f, indent=2, default=str)
    with open(out_summary, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\nSaved to {args.output_dir}")


if __name__ == "__main__":
    main()
