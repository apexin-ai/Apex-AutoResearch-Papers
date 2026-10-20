#!/usr/bin/env python3
"""Latent Self-Consistency (LSC) for structured self-consistency IE.

Uses entity-level hidden-state representations for latent aggregation,
bypassing the LP compression proven by F4 diagnostic (median range 0.041 nats).

Methods:
  A) Centroid Selection — pick sample whose entity centroid is closest to grand centroid
  B) Latent Confidence — intra-entity cosine agreement in hidden-state space
  C) Clustering — k-means (k=2) on entity hidden states, check separation by correctness

Pipeline:
  1. Load N=8 inference samples (JSONL, same format as ESJ)
  2. Forward pass to extract last-layer hidden states for each sample's output
  3. Locate entity text spans in the token sequence (offset_mapping + subsequence fallback)
  4. Mean-pool entity token hidden states → entity vector
  5. Apply latent aggregation methods A/B/C
  6. Evaluate: F1, selection F1, entity-level ρ/AUROC
"""

import argparse
import gc
import json
import os
import time
from collections import defaultdict

import numpy as np
import torch
import torch.nn.functional as F
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel
from scipy.stats import spearmanr
from sklearn.metrics import roc_auc_score
from sklearn.cluster import KMeans


# ---------------------------------------------------------------------------
# Prompt templates (must match inference-time prompts exactly)
# ---------------------------------------------------------------------------

_TRAIN_ALIGNED_TEMPLATE = (
    "Extract all structured information (entities and relations) from the following text. "
    "Output a JSON object.\n\n"
    "Text: {text}\n"
    "{schema_line}"
    "\nOutput format: "
    '{{"entities": [{{"text": "...", "type": "...", "start": <int>, "end": <int>}}], '
    '"relations": [{{"head": "...", "tail": "...", "type": "...", '
    '"head_start": <int>, "head_end": <int>, "tail_start": <int>, "tail_end": <int>}}], '
    '"events": []}}'
)

_NER_TEMPLATE = (
    "Extract named entities from the following text. "
    "Output a JSON object with the fields: entities, relations, events.\n\n"
    "Text: {text}\n"
    "{schema_line}"
    "\nOutput format: "
    '{{"entities": [{{"text": "...", "type": "...", "start": <int>, "end": <int>}}], '
    '"relations": [], "events": []}}'
)


# ---------------------------------------------------------------------------
# Data helpers (shared interface with ESJ)
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


def compute_sample_lp_scores(instance):
    out = []
    for s in instance["samples"]:
        lp = s.get("mean_logprob")
        if lp is None:
            lp = s.get("cumulative_logprob", -999) / max(s.get("n_tokens", 1), 1)
        out.append(lp)
    return out


# ---------------------------------------------------------------------------
# Model
# ---------------------------------------------------------------------------

def load_model(base_path, adapter_path, device="cuda"):
    tok_path = adapter_path if adapter_path else base_path
    print(f"Loading tokenizer from {tok_path} ...")
    tokenizer = AutoTokenizer.from_pretrained(
        tok_path, trust_remote_code=True, padding_side="right",
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


# ---------------------------------------------------------------------------
# Prompt & output reconstruction
# ---------------------------------------------------------------------------

def build_prompt(text, subtask="ner", schema_hint="", use_train_format=True):
    """Build the extraction prompt matching inference-time format."""
    if use_train_format:
        schema_line = f"{schema_hint}\n" if schema_hint else ""
        return _TRAIN_ALIGNED_TEMPLATE.format(text=text, schema_line=schema_line)
    schema_line = f"Schema: {schema_hint}\n" if schema_hint else ""
    if subtask == "ner":
        return _NER_TEMPLATE.format(text=text, schema_line=schema_line)
    return _TRAIN_ALIGNED_TEMPLATE.format(text=text, schema_line=schema_line)


def format_chat_prompt(tokenizer, content):
    """Wrap content with chat template, return formatted string."""
    msgs = [{"role": "user", "content": content}]
    try:
        return tokenizer.apply_chat_template(
            msgs, tokenize=False, add_generation_prompt=True,
            enable_thinking=False,
        )
    except TypeError:
        return tokenizer.apply_chat_template(
            msgs, tokenize=False, add_generation_prompt=True,
        )


def reconstruct_output(sample):
    """Reconstruct the JSON output text from parsed fields (raw_output not stored)."""
    for key in ("raw_output", "output", "response", "generated_text"):
        if key in sample:
            return sample[key]
    obj = {
        "entities": sample.get("entities", []),
        "relations": sample.get("relations", []),
        "events": sample.get("events", []),
    }
    return json.dumps(obj, ensure_ascii=False)


# ---------------------------------------------------------------------------
# Entity span finding
# ---------------------------------------------------------------------------

def _find_entity_span(entity_text, output_text, output_ids, output_offsets, tokenizer):
    """Find entity token span using offset_mapping (primary) or subsequence match (fallback).

    output_offsets: list of (char_start, char_end) already adjusted to be relative to output_text.
    """
    # Strategy 1: character position → token span via offset_mapping
    if output_offsets is not None:
        char_idx = output_text.find(entity_text)
        if char_idx != -1:
            char_end = char_idx + len(entity_text)
            t_start, t_end = None, None
            for ti, (cs, ce) in enumerate(output_offsets):
                if cs == ce:
                    continue
                if t_start is None and cs <= char_idx < ce:
                    t_start = ti
                if cs < char_end <= ce:
                    t_end = ti + 1
                    break
            if t_start is not None and t_end is not None:
                return (t_start, t_end)

    # Strategy 2: token subsequence matching
    entity_ids = tokenizer.encode(entity_text, add_special_tokens=False)
    if entity_ids:
        n = len(entity_ids)
        for i in range(len(output_ids) - n + 1):
            if output_ids[i:i + n] == entity_ids:
                return (i, i + n)

    # Strategy 3: with leading space (some tokenizers prepend space)
    entity_ids_sp = tokenizer.encode(" " + entity_text, add_special_tokens=False)
    if entity_ids_sp and entity_ids_sp != (entity_ids or []):
        n = len(entity_ids_sp)
        for i in range(len(output_ids) - n + 1):
            if output_ids[i:i + n] == entity_ids_sp:
                return (i, i + n)

    return None


# ---------------------------------------------------------------------------
# Hidden state extraction
# ---------------------------------------------------------------------------

@torch.no_grad()
def extract_instance_hidden_states(model, tokenizer, instance, hidden_layer=-1,
                                   batch_size=4, device="cuda",
                                   subtask="ner", schema_hint="",
                                   use_train_format=True):
    """Extract entity-level hidden state vectors for all samples in one instance.

    Returns:
        sample_entity_vectors: list of dicts (one per sample),
            each mapping entity_key (start,end,type) -> numpy vector (D,)
        sample_centroids: list of numpy vectors (D,) or None per sample
        n_matched: total entities with found spans
        n_total: total entities attempted
    """
    raw_prompt = build_prompt(instance["text"], subtask, schema_hint, use_train_format)
    prompt_text = format_chat_prompt(tokenizer, raw_prompt)
    prompt_char_len = len(prompt_text)

    samples = instance["samples"]
    sample_entity_vectors = []
    sample_centroids = []
    n_matched, n_total = 0, 0

    for bi in range(0, len(samples), batch_size):
        batch_samples = samples[bi:bi + batch_size]

        # Tokenize each sample individually to get offset_mapping
        full_encodings = []
        output_metas = []
        for s in batch_samples:
            out_text = reconstruct_output(s)
            full_text = prompt_text + out_text

            try:
                enc = tokenizer(full_text, add_special_tokens=False,
                                return_offsets_mapping=True)
                has_offsets = "offset_mapping" in enc and enc["offset_mapping"] is not None
            except Exception:
                enc = tokenizer(full_text, add_special_tokens=False)
                has_offsets = False

            # Find prompt/output boundary
            if has_offsets:
                offsets = enc["offset_mapping"]
                p_len = len(enc["input_ids"])
                for ti, (cs, _ce) in enumerate(offsets):
                    if cs >= prompt_char_len:
                        p_len = ti
                        break
                # Adjust output offsets to be relative to output_text
                output_offsets_raw = offsets[p_len:]
                output_offsets_adj = [
                    (cs - prompt_char_len, ce - prompt_char_len)
                    for cs, ce in output_offsets_raw
                ]
            else:
                prompt_enc = tokenizer(prompt_text, add_special_tokens=False)
                p_len = len(prompt_enc["input_ids"])
                output_offsets_adj = None

            full_encodings.append(enc)
            output_metas.append({
                "prompt_len": p_len,
                "output_text": out_text,
                "output_offsets": output_offsets_adj,
            })

        # Build padded batch
        max_len = max(len(e["input_ids"]) for e in full_encodings)
        pad_id = tokenizer.pad_token_id if tokenizer.pad_token_id is not None else 0

        batch_ids = []
        batch_mask = []
        for e in full_encodings:
            seq_len = len(e["input_ids"])
            pad_len = max_len - seq_len
            batch_ids.append(e["input_ids"] + [pad_id] * pad_len)
            batch_mask.append([1] * seq_len + [0] * pad_len)

        inputs = {
            "input_ids": torch.tensor(batch_ids, dtype=torch.long, device=device),
            "attention_mask": torch.tensor(batch_mask, dtype=torch.long, device=device),
        }

        model_outputs = model(**inputs, output_hidden_states=True)
        hs = model_outputs.hidden_states[hidden_layer]  # (B, L, D)

        for i, s in enumerate(batch_samples):
            meta = output_metas[i]
            p_len = meta["prompt_len"]
            total_tok = len(full_encodings[i]["input_ids"])
            out_len = total_tok - p_len

            if out_len <= 0:
                sample_entity_vectors.append({})
                sample_centroids.append(None)
                continue

            output_hs = hs[i, p_len:p_len + out_len].float().cpu()  # (n_out, D)
            output_ids = full_encodings[i]["input_ids"][p_len:p_len + out_len]

            entities = s.get("entities", [])
            evecs = {}
            for e in entities:
                key = (e["start"], e["end"], e["type"])
                if key in evecs:
                    continue
                n_total += 1
                span = _find_entity_span(
                    e["text"], meta["output_text"], output_ids,
                    meta["output_offsets"], tokenizer,
                )
                if span is None:
                    continue
                t_start, t_end = span
                if t_end > output_hs.shape[0]:
                    continue
                evecs[key] = output_hs[t_start:t_end].mean(dim=0).numpy()
                n_matched += 1

            sample_entity_vectors.append(evecs)
            centroid = np.mean(list(evecs.values()), axis=0) if evecs else None
            sample_centroids.append(centroid)

        del model_outputs, hs
        torch.cuda.empty_cache()

    return sample_entity_vectors, sample_centroids, n_matched, n_total


# ---------------------------------------------------------------------------
# Method A: Centroid Selection
# ---------------------------------------------------------------------------

def centroid_selection(instance, sample_centroids):
    """Select the sample whose entity centroid is closest to the grand centroid."""
    valid = [(i, c) for i, c in enumerate(sample_centroids) if c is not None]
    if not valid:
        return entity_set(instance["samples"][0].get("entities", []))

    indices, centroids = zip(*valid)
    centroids = np.stack(centroids)  # (K, D)
    grand = centroids.mean(axis=0)  # (D,)

    # Cosine similarity to grand centroid
    norms = np.linalg.norm(centroids, axis=1)
    norms = np.maximum(norms, 1e-8)
    grand_norm = max(np.linalg.norm(grand), 1e-8)
    sims = (centroids @ grand) / (norms * grand_norm)

    best_idx = indices[int(np.argmax(sims))]
    return entity_set(instance["samples"][best_idx].get("entities", []))


def centroid_selection_idx(sample_centroids):
    """Return the index of the centroid-selected sample."""
    valid = [(i, c) for i, c in enumerate(sample_centroids) if c is not None]
    if not valid:
        return 0
    indices, centroids = zip(*valid)
    centroids = np.stack(centroids)
    grand = centroids.mean(axis=0)
    norms = np.maximum(np.linalg.norm(centroids, axis=1), 1e-8)
    grand_norm = max(np.linalg.norm(grand), 1e-8)
    sims = (centroids @ grand) / (norms * grand_norm)
    return indices[int(np.argmax(sims))]


# ---------------------------------------------------------------------------
# Method B: Latent Confidence Scoring
# ---------------------------------------------------------------------------

def latent_confidence_scoring(instance, sample_entity_vectors, threshold):
    """Entity-level latent agreement as confidence, combined with frequency."""
    N = len(instance["samples"])

    entity_counts = defaultdict(int)
    entity_vecs_map = defaultdict(list)
    for si, s in enumerate(instance["samples"]):
        for e in s.get("entities", []):
            key = (e["start"], e["end"], e["type"])
            entity_counts[key] += 1
            if key in sample_entity_vectors[si]:
                entity_vecs_map[key].append(sample_entity_vectors[si][key])

    out = set()
    entity_latent_data = {}
    for key, count in entity_counts.items():
        freq = count / N
        vecs = entity_vecs_map.get(key, [])

        if len(vecs) >= 2:
            vecs_t = torch.from_numpy(np.stack(vecs)).float()
            vecs_norm = F.normalize(vecs_t, dim=1)
            sim_mat = vecs_norm @ vecs_norm.T
            n = len(vecs)
            mask = torch.triu(torch.ones(n, n, dtype=torch.bool), diagonal=1)
            latent_agree = sim_mat[mask].mean().item()
        elif len(vecs) == 1:
            latent_agree = 0.0
        else:
            latent_agree = 0.0

        score = latent_agree * freq
        entity_latent_data[key] = {
            "latent_agree": latent_agree,
            "freq": freq,
            "score": score,
            "n_vectors": len(vecs),
        }

        if score >= threshold:
            out.add(key)

    return out, entity_latent_data


# ---------------------------------------------------------------------------
# Method C: Clustering Analysis
# ---------------------------------------------------------------------------

def cluster_analysis(instance, sample_entity_vectors, gold_set):
    """K-means (k=2) on entity hidden states. Check cluster-correctness separation."""
    all_vecs, all_keys, all_correct = [], [], []

    for si, s in enumerate(instance["samples"]):
        for e in s.get("entities", []):
            key = (e["start"], e["end"], e["type"])
            if key in sample_entity_vectors[si]:
                all_vecs.append(sample_entity_vectors[si][key])
                all_keys.append(key)
                all_correct.append(1 if key in gold_set else 0)

    if len(all_vecs) < 4:
        return None

    X = np.stack(all_vecs)
    labels_true = np.array(all_correct)

    try:
        km = KMeans(n_clusters=2, random_state=42, n_init=10)
        cluster_labels = km.fit_predict(X)
    except Exception:
        return None

    c0_mask = cluster_labels == 0
    c1_mask = cluster_labels == 1
    c0_correct = float(labels_true[c0_mask].mean()) if c0_mask.sum() > 0 else 0.0
    c1_correct = float(labels_true[c1_mask].mean()) if c1_mask.sum() > 0 else 0.0

    return {
        "n_entities": len(all_vecs),
        "cluster_sizes": [int(c0_mask.sum()), int(c1_mask.sum())],
        "cluster_correct_rates": [round(c0_correct, 4), round(c1_correct, 4)],
        "separation": round(abs(c0_correct - c1_correct), 4),
    }


# ---------------------------------------------------------------------------
# Within-instance sample ranking via latent centroids
# ---------------------------------------------------------------------------

def rank_samples_by_centroid(sample_centroids):
    """Score each sample by cosine similarity of its centroid to the grand centroid."""
    valid = [(i, c) for i, c in enumerate(sample_centroids) if c is not None]
    if not valid:
        return [0.0] * len(sample_centroids)

    indices, centroids = zip(*valid)
    centroids = np.stack(centroids)
    grand = centroids.mean(axis=0)
    norms = np.maximum(np.linalg.norm(centroids, axis=1), 1e-8)
    grand_norm = max(np.linalg.norm(grand), 1e-8)
    sims = (centroids @ grand) / (norms * grand_norm)

    scores = [0.0] * len(sample_centroids)
    for idx, sim in zip(indices, sims):
        scores[idx] = float(sim)
    return scores


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description="Latent Self-Consistency (LSC)")
    ap.add_argument("--base_model_path", type=str, required=True)
    ap.add_argument("--adapter_path", type=str, default=None)
    ap.add_argument("--data_path", type=str, required=True)
    ap.add_argument("--output_dir", type=str, required=True)
    ap.add_argument("--hidden_layer", type=int, default=-1,
                    help="Which hidden layer to extract (-1 = last)")
    ap.add_argument("--batch_size", type=int, default=4,
                    help="Forward-pass batch size (smaller than ESJ — stores hidden states)")
    ap.add_argument("--max_instances", type=int, default=0)
    ap.add_argument("--subtask", type=str, default="ner",
                    choices=["ner", "re", "full"])
    ap.add_argument("--schema_hint", type=str, default="",
                    help="Schema description (e.g. entity types) matching inference")
    ap.add_argument("--use_train_format", action="store_true", default=True,
                    help="Use train-aligned prompt template (default)")
    ap.add_argument("--no_train_format", dest="use_train_format", action="store_false",
                    help="Use subtask-specific prompt template instead")
    args = ap.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    device = "cuda"

    # ---- 1. Load data ----
    print(f"Loading data from {args.data_path} ...")
    data = load_samples(args.data_path, args.max_instances)
    print(f"  {len(data)} instances loaded")
    N_samples = len(data[0]["samples"]) if data else 0
    print(f"  {N_samples} samples per instance")

    # Entity stats
    total_occ, total_uniq = 0, 0
    for inst in data:
        em = extract_unique_entities(inst)
        total_occ += sum(em.values())
        total_uniq += len(em)
    print(f"  {total_uniq} unique entities ({total_occ} total occurrences)")

    # ---- 2. Load model ----
    model, tokenizer = load_model(args.base_model_path, args.adapter_path, device)

    # ---- 3. Extract hidden states & entity vectors ----
    print(f"\nExtracting hidden states (layer={args.hidden_layer}, "
          f"batch_size={args.batch_size}) ...")
    t0 = time.time()

    all_sample_evecs = []   # per instance: list of 8 dicts
    all_sample_cents = []   # per instance: list of 8 vectors/None
    total_matched, total_entities = 0, 0

    for idx, inst in enumerate(data):
        evecs, cents, n_m, n_t = extract_instance_hidden_states(
            model, tokenizer, inst,
            hidden_layer=args.hidden_layer,
            batch_size=args.batch_size,
            device=device,
            subtask=args.subtask,
            schema_hint=args.schema_hint,
            use_train_format=args.use_train_format,
        )
        all_sample_evecs.append(evecs)
        all_sample_cents.append(cents)
        total_matched += n_m
        total_entities += n_t

        if (idx + 1) % 50 == 0:
            print(f"  {idx+1}/{len(data)} instances")

    elapsed = time.time() - t0
    match_rate = total_matched / max(total_entities, 1)
    print(f"  Done in {elapsed:.1f}s  "
          f"({len(data) * N_samples / elapsed:.0f} samples/s)")
    print(f"  Entity span match rate: {match_rate:.1%} "
          f"({total_matched}/{total_entities})")

    # Free model
    del model
    gc.collect()
    torch.cuda.empty_cache()

    # ---- 4. Method A: Centroid Selection ----
    print("\nMethod A: Centroid Selection ...")
    centroid_f1s = []
    for i, inst in enumerate(data):
        gold = entity_set(inst["gold"]["entities"])
        pred = centroid_selection(inst, all_sample_cents[i])
        centroid_f1s.append(compute_prf(pred, gold)[2])
    centroid_f1 = float(np.mean(centroid_f1s))

    # ---- 5. Method B: Latent Confidence Scoring ----
    print("Method B: Latent Confidence Scoring ...")
    lc_thresholds = [0.02, 0.05, 0.08, 0.1, 0.12, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.5]
    lc_res = {}
    all_entity_latent_data = []  # collected once at first threshold

    for th in lc_thresholds:
        fs = []
        for i, inst in enumerate(data):
            gold = entity_set(inst["gold"]["entities"])
            pred, latent_data = latent_confidence_scoring(
                inst, all_sample_evecs[i], th)
            fs.append(compute_prf(pred, gold)[2])
            if th == lc_thresholds[0]:
                all_entity_latent_data.append(latent_data)
        lc_res[str(th)] = float(np.mean(fs))

    best_lc_th = max(lc_res, key=lc_res.get)
    best_lc_f1 = lc_res[best_lc_th]

    # ---- 6. Method C: Clustering ----
    print("Method C: Clustering Analysis ...")
    cluster_results_per_inst = []  # indexed by instance, None if not analyzable
    for i, inst in enumerate(data):
        gold = entity_set(inst["gold"]["entities"])
        cr = cluster_analysis(inst, all_sample_evecs[i], gold)
        cluster_results_per_inst.append(cr)

    valid_clusters = [c for c in cluster_results_per_inst if c is not None]
    if valid_clusters:
        avg_sep = float(np.mean([c["separation"] for c in valid_clusters]))
        high_sep = sum(1 for c in valid_clusters if c["separation"] > 0.1)
    else:
        avg_sep, high_sep = 0.0, 0

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

    # LP-based selection (baseline from parent experiment)
    lp_sel_f1s = []
    for i, inst in enumerate(data):
        gold = entity_set(inst["gold"]["entities"])
        sample_f1s = [compute_prf(entity_set(s.get("entities", [])), gold)[2]
                      for s in inst["samples"]]
        lp_scores = compute_sample_lp_scores(inst)
        lp_sel_f1s.append(sample_f1s[int(np.argmax(lp_scores))])
    lp_sel_f1 = float(np.mean(lp_sel_f1s))

    # ---- 8. Entity-level signal quality ----
    print("Entity-level signal analysis ...")
    ent_correct, ent_latent_agree, ent_freq, ent_latent_score = [], [], [], []
    for i, inst in enumerate(data):
        gold = entity_set(inst["gold"]["entities"])
        if i < len(all_entity_latent_data):
            for key, info in all_entity_latent_data[i].items():
                ent_correct.append(1 if key in gold else 0)
                ent_latent_agree.append(info["latent_agree"])
                ent_freq.append(info["freq"])
                ent_latent_score.append(info["score"])

    ent_correct = np.array(ent_correct, dtype=float)
    ent_latent_agree = np.array(ent_latent_agree)
    ent_freq = np.array(ent_freq)
    ent_latent_score = np.array(ent_latent_score)

    rho_latent, _ = safe_spearman(ent_latent_agree, ent_correct)
    rho_freq, _ = safe_spearman(ent_freq, ent_correct)
    rho_score, _ = safe_spearman(ent_latent_score, ent_correct)
    auroc_latent = safe_auroc(ent_latent_agree, ent_correct)
    auroc_freq = safe_auroc(ent_freq, ent_correct)
    auroc_score = safe_auroc(ent_latent_score, ent_correct)

    # Breakdown by agreement level
    disputed = ent_freq < 0.5
    consensus = ent_freq >= 0.75
    mid = (~disputed) & (~consensus)

    def group_stats(mask, label):
        n = int(mask.sum())
        if n < 3:
            return {"n": n}
        return {
            "n": n,
            "correct_rate": round(float(ent_correct[mask].mean()), 4),
            "latent_agree_mean": round(float(ent_latent_agree[mask].mean()), 4),
            "latent_agree_std": round(float(ent_latent_agree[mask].std()), 4),
            "rho_latent_correct": round(float(safe_spearman(
                ent_latent_agree[mask], ent_correct[mask])[0]), 4),
            "auroc_latent": round(safe_auroc(ent_latent_agree[mask], ent_correct[mask]), 4),
        }

    # ---- 9. Within-instance sample ranking ----
    print("Within-instance sample ranking ...")
    cent_rank_corrs, lp_rank_corrs = [], []
    cent_sel_f1s = []

    for i, inst in enumerate(data):
        gold = entity_set(inst["gold"]["entities"])
        sample_f1s = [compute_prf(entity_set(s.get("entities", [])), gold)[2]
                      for s in inst["samples"]]

        cent_scores = rank_samples_by_centroid(all_sample_cents[i])
        lp_scores = compute_sample_lp_scores(inst)

        # Selection F1
        cent_sel_f1s.append(sample_f1s[int(np.argmax(cent_scores))])

        # Rank correlation (only if variance in F1)
        if len(set(sample_f1s)) >= 2:
            r_c, _ = spearmanr(cent_scores, sample_f1s)
            r_lp, _ = spearmanr(lp_scores, sample_f1s)
            if np.isfinite(r_c):
                cent_rank_corrs.append(r_c)
            if np.isfinite(r_lp):
                lp_rank_corrs.append(r_lp)

    cent_sel_f1 = float(np.mean(cent_sel_f1s))

    # ---- 10. Build result ----
    result = {
        "experiment": "LSC_latent_self_consistency",
        "model_base": args.base_model_path,
        "adapter": args.adapter_path,
        "data": args.data_path,
        "hidden_layer": args.hidden_layer,
        "n_instances": len(data),
        "n_samples_per_instance": N_samples,
        "n_unique_entities": total_uniq,
        "entity_span_match_rate": round(match_rate, 4),
        "extraction_seconds": round(elapsed, 1),
        "construction_f1": {
            "greedy": round(greedy_f1, 4),
            "oracle": round(oracle_f1, 4),
            "majority_vote": {k: round(v, 4) for k, v in mv_res.items()},
            "best_mv": {"threshold": best_mv_th, "f1": round(best_mv_f1, 4)},
            "centroid_selection": round(centroid_f1, 4),
            "latent_confidence": {k: round(v, 4) for k, v in lc_res.items()},
            "best_latent_confidence": {"threshold": best_lc_th, "f1": round(best_lc_f1, 4)},
        },
        "deltas": {
            "centroid_vs_greedy": round(centroid_f1 - greedy_f1, 4),
            "centroid_vs_mv": round(centroid_f1 - best_mv_f1, 4),
            "latent_conf_vs_greedy": round(best_lc_f1 - greedy_f1, 4),
            "latent_conf_vs_mv": round(best_lc_f1 - best_mv_f1, 4),
        },
        "entity_signal_quality": {
            "n_entities": len(ent_correct),
            "latent_agree": {
                "rho": round(float(rho_latent), 4),
                "auroc": round(float(auroc_latent), 4),
            },
            "frequency": {
                "rho": round(float(rho_freq), 4),
                "auroc": round(float(auroc_freq), 4),
            },
            "latent_x_freq": {
                "rho": round(float(rho_score), 4),
                "auroc": round(float(auroc_score), 4),
            },
        },
        "agreement_breakdown": {
            "disputed_lt0.5": group_stats(disputed, "disputed"),
            "mid_0.5_0.75": group_stats(mid, "mid"),
            "consensus_gte0.75": group_stats(consensus, "consensus"),
        },
        "clustering": {
            "n_analyzable_instances": len(valid_clusters),
            "avg_separation": round(avg_sep, 4),
            "high_separation_instances": high_sep,
        },
        "within_instance_ranking": {
            "centroid_mean_rho": round(float(np.mean(cent_rank_corrs)), 4) if cent_rank_corrs else None,
            "lp_mean_rho": round(float(np.mean(lp_rank_corrs)), 4) if lp_rank_corrs else None,
            "n_rankable_instances": len(cent_rank_corrs),
            "centroid_selection_f1": round(cent_sel_f1, 4),
            "lp_selection_f1": round(lp_sel_f1, 4),
        },
    }

    out_path = os.path.join(args.output_dir, "lsc_results.json")
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)
    print(f"\nSaved: {out_path}")

    # Per-instance details
    details = []
    for i, inst in enumerate(data):
        d = {
            "instance_idx": i,
            "instance_id": inst.get("id", str(i)),
            "n_gold": len(entity_set(inst["gold"]["entities"])),
            "centroid_f1": round(centroid_f1s[i], 4),
            "greedy_f1": round(greedy_f1s[i], 4),
            "centroid_selected_sample": centroid_selection_idx(all_sample_cents[i]),
        }
        if cluster_results_per_inst[i] is not None:
            d["clustering"] = cluster_results_per_inst[i]
        details.append(d)

    details_path = os.path.join(args.output_dir, "lsc_details.jsonl")
    with open(details_path, "w") as f:
        for d in details:
            f.write(json.dumps(d) + "\n")
    print(f"Saved: {details_path}")

    # ---- Print summary ----
    print(f"\n{'='*60}")
    print("LSC Latent Self-Consistency Results")
    print(f"{'='*60}")
    print(f"Instances: {len(data)}  Samples/instance: {N_samples}")
    print(f"Entity span match rate: {match_rate:.1%}")

    print(f"\nConstruction F1 (macro):")
    print(f"  Greedy:                      {greedy_f1:.4f}")
    print(f"  Best MV (θ={best_mv_th}):         {best_mv_f1:.4f}  "
          f"(Δ={best_mv_f1-greedy_f1:+.4f})")
    print(f"  Centroid Selection:          {centroid_f1:.4f}  "
          f"(Δ={centroid_f1-greedy_f1:+.4f})")
    print(f"  Best Latent Conf (θ={best_lc_th}): {best_lc_f1:.4f}  "
          f"(Δ={best_lc_f1-greedy_f1:+.4f})")
    print(f"  Oracle:                      {oracle_f1:.4f}")
    print(f"  Centroid vs MV: {centroid_f1-best_mv_f1:+.4f}  "
          f"Latent Conf vs MV: {best_lc_f1-best_mv_f1:+.4f}")

    print(f"\nEntity-level signal:")
    print(f"  Latent agree  ρ={rho_latent:+.4f}  AUROC={auroc_latent:.4f}")
    print(f"  Frequency     ρ={rho_freq:+.4f}  AUROC={auroc_freq:.4f}")
    print(f"  Latent×Freq   ρ={rho_score:+.4f}  AUROC={auroc_score:.4f}")

    print(f"\nBreakdown by agreement:")
    for label, mask in [("Disputed (<0.5)", disputed),
                        ("Mid [0.5,0.75)", mid),
                        ("Consensus (≥0.75)", consensus)]:
        n = mask.sum()
        if n >= 3:
            print(f"  {label}: n={n}, correct={ent_correct[mask].mean():.3f}, "
                  f"latent_agree={ent_latent_agree[mask].mean():.3f}, "
                  f"AUROC={safe_auroc(ent_latent_agree[mask], ent_correct[mask]):.4f}")

    print(f"\nClustering (k=2):")
    print(f"  Analyzable: {len(valid_clusters)}/{len(data)} instances")
    print(f"  Avg separation: {avg_sep:.4f}  "
          f"High separation (>0.1): {high_sep}")

    print(f"\nWithin-instance ranking (ρ with sample F1):")
    if cent_rank_corrs:
        print(f"  Centroid: {np.mean(cent_rank_corrs):+.4f} "
              f"({len(cent_rank_corrs)} instances)")
    if lp_rank_corrs:
        print(f"  LP:       {np.mean(lp_rank_corrs):+.4f} "
              f"({len(lp_rank_corrs)} instances)")

    print(f"\nSelection F1 (pick best sample):")
    print(f"  Centroid: {cent_sel_f1:.4f}  LP: {lp_sel_f1:.4f}  "
          f"Greedy: {greedy_f1:.4f}")


if __name__ == "__main__":
    main()
