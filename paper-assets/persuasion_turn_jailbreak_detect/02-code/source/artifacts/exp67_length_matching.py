"""exp67: Length-matched control experiment for DD/AA OOD evaluation.

Reviewer concern: OOD detection might be driven by turn-count differences
between jailbreak and benign conversations (shortcut).

Approach:
  1. Count user turns per conversation in DD/AA jailbreak and test benign
  2. Find overlapping turn-count range
  3. Construct length-matched subsets (only keep overlapping range)
  4. Run inference with trained DeBERTa+BiGRU models
  5. Compare full-set F1 vs length-matched F1

If length-matched F1 ≈ full-set F1 → model doesn't rely on turn count.
"""

import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

import sys
import json
import random
import numpy as np
import torch
from pathlib import Path
from collections import Counter
from sklearn.metrics import f1_score, precision_score, recall_score

sys.path.insert(0, "/root/persuasion_turn_jailbreak_detect")
from src.models.gru_classifier import GRUClassifier
from src.models.deberta_multitask import DeBERTaMultiTask
from transformers import AutoTokenizer

PROJ = Path("/root/persuasion_turn_jailbreak_detect")
MODEL_NAME = "microsoft/deberta-v3-base"
MAX_LENGTH = 256
GRU_HIDDEN = 256
GRU_LAYERS = 2
GRU_DROPOUT = 0.3
SEEDS = [42, 123, 456]
EVAL_SEED = 42
DEVICE = torch.device("cuda:0")

DD_PATH = PROJ / "data/generated/deceptive_delight_all.jsonl"
AA_PATH = PROJ / "data/actorattack_ood/actorattack_all.jsonl"

random.seed(EVAL_SEED)
np.random.seed(EVAL_SEED)
torch.manual_seed(EVAL_SEED)


def load_jsonl(path):
    with open(path) as f:
        return [json.loads(l) for l in f if l.strip()]


def count_user_turns(conv):
    return len([t for t in conv["turns"] if t["role"] == "user"])


def extract_user_turns(conv):
    return [t["content"] for t in conv["turns"] if t["role"] == "user"]


def get_label(conv):
    return 1 if conv["label"] == "jailbreak" else 0


def load_encoder(seed):
    ckpt = PROJ / f"checkpoints/exp59_seed{seed}/deberta_multitask/best/model.pt"
    model = DeBERTaMultiTask(model_name=MODEL_NAME)
    sd = torch.load(ckpt, map_location="cpu", weights_only=False)
    model.load_state_dict(sd)
    encoder = model.deberta.float().to(DEVICE).eval()
    for p in encoder.parameters():
        p.requires_grad = False
    return encoder


def load_gru(seed):
    gru_path = PROJ / f"checkpoints/exp59_seed{seed}/gru_treatment/treatment/best.pt"
    gru = GRUClassifier(
        input_dim=768, hidden_dim=GRU_HIDDEN,
        num_layers=GRU_LAYERS, dropout=GRU_DROPOUT,
    )
    gru.load_state_dict(torch.load(gru_path, map_location="cpu", weights_only=True))
    return gru.float().to(DEVICE).eval()


def predict(encoder, gru, tokenizer, convs):
    preds, probs = [], []
    for c in convs:
        turns = extract_user_turns(c)
        if not turns:
            turns = [""]
        enc = tokenizer(
            turns, max_length=MAX_LENGTH, padding=True,
            truncation=True, return_tensors="pt",
        ).to(DEVICE)
        with torch.no_grad():
            out = encoder(input_ids=enc["input_ids"], attention_mask=enc["attention_mask"])
            embs = out.last_hidden_state[:, 0, :].unsqueeze(0)
            lengths = torch.tensor([embs.size(1)], dtype=torch.long).to(DEVICE)
            logits = gru(embs, lengths)
            prob = torch.softmax(logits, dim=1)[0, 1].item()
            pred = logits.argmax(dim=1).item()
        preds.append(pred)
        probs.append(prob)
    return preds, probs


def compute_metrics(labels, preds):
    labels, preds = np.array(labels), np.array(preds)
    return {
        "f1_macro": float(f1_score(labels, preds, average="macro")),
        "precision_macro": float(precision_score(labels, preds, average="macro", zero_division=0)),
        "recall_macro": float(recall_score(labels, preds, average="macro", zero_division=0)),
        "accuracy": float((labels == preds).mean()),
        "n": int(len(labels)),
        "n_jailbreak": int(labels.sum()),
        "n_benign": int((labels == 0).sum()),
    }


def length_match(jailbreak_convs, benign_convs):
    """Return length-matched subsets: only keep conversations within overlapping turn-count range."""
    jb_counts = [count_user_turns(c) for c in jailbreak_convs]
    bn_counts = [count_user_turns(c) for c in benign_convs]

    jb_min, jb_max = min(jb_counts), max(jb_counts)
    bn_min, bn_max = min(bn_counts), max(bn_counts)
    overlap_min = max(jb_min, bn_min)
    overlap_max = min(jb_max, bn_max)

    jb_matched = [c for c, tc in zip(jailbreak_convs, jb_counts) if overlap_min <= tc <= overlap_max]
    bn_matched = [c for c, tc in zip(benign_convs, bn_counts) if overlap_min <= tc <= overlap_max]

    return jb_matched, bn_matched, {
        "jailbreak_range": [jb_min, jb_max],
        "benign_range": [bn_min, bn_max],
        "overlap_range": [overlap_min, overlap_max],
        "jailbreak_original": len(jailbreak_convs),
        "jailbreak_matched": len(jb_matched),
        "benign_original": len(benign_convs),
        "benign_matched": len(bn_matched),
    }


def length_match_per_bucket(jailbreak_convs, benign_convs):
    """Finer-grained: match per turn-count bucket, subsample majority class."""
    jb_by_tc = {}
    for c in jailbreak_convs:
        tc = count_user_turns(c)
        jb_by_tc.setdefault(tc, []).append(c)

    bn_by_tc = {}
    for c in benign_convs:
        tc = count_user_turns(c)
        bn_by_tc.setdefault(tc, []).append(c)

    shared_tcs = set(jb_by_tc.keys()) & set(bn_by_tc.keys())

    jb_matched, bn_matched = [], []
    bucket_info = {}
    for tc in sorted(shared_tcs):
        jb_bucket = jb_by_tc[tc]
        bn_bucket = bn_by_tc[tc]
        n_min = min(len(jb_bucket), len(bn_bucket))
        random.seed(EVAL_SEED + tc)
        jb_sampled = random.sample(jb_bucket, n_min) if len(jb_bucket) > n_min else jb_bucket
        bn_sampled = random.sample(bn_bucket, n_min) if len(bn_bucket) > n_min else bn_bucket
        jb_matched.extend(jb_sampled)
        bn_matched.extend(bn_sampled)
        bucket_info[tc] = {"jb": len(jb_bucket), "bn": len(bn_bucket), "matched": n_min}

    return jb_matched, bn_matched, bucket_info


def print_distribution(name, convs):
    counts = [count_user_turns(c) for c in convs]
    counter = Counter(counts)
    print(f"\n  {name}: n={len(convs)}, turns range [{min(counts)}, {max(counts)}], mean={np.mean(counts):.1f}")
    for tc in sorted(counter):
        print(f"    turns={tc}: {counter[tc]}")


def eval_one_setting(encoder, gru, tokenizer, jailbreak_convs, benign_convs, setting_name):
    """Evaluate full-set and length-matched subsets."""
    print(f"\n--- {setting_name} ---")
    print_distribution(f"{setting_name} jailbreak", jailbreak_convs)
    print_distribution(f"{setting_name} benign", benign_convs)

    # Full set
    full_convs = jailbreak_convs + benign_convs
    full_labels = [get_label(c) for c in full_convs]
    full_preds, _ = predict(encoder, gru, tokenizer, full_convs)
    full_metrics = compute_metrics(full_labels, full_preds)
    print(f"  Full-set F1: {full_metrics['f1_macro']:.4f} (n={full_metrics['n']})")

    # Range-matched
    jb_m, bn_m, match_info = length_match(jailbreak_convs, benign_convs)
    if jb_m and bn_m:
        matched_convs = jb_m + bn_m
        matched_labels = [get_label(c) for c in matched_convs]
        matched_preds, _ = predict(encoder, gru, tokenizer, matched_convs)
        matched_metrics = compute_metrics(matched_labels, matched_preds)
        print(f"  Range-matched F1: {matched_metrics['f1_macro']:.4f} "
              f"(n={matched_metrics['n']}, overlap={match_info['overlap_range']})")
    else:
        matched_metrics = None
        print(f"  Range-matched: NO OVERLAP (jb={match_info['jailbreak_range']}, bn={match_info['benign_range']})")

    # Per-bucket matched
    jb_pb, bn_pb, bucket_info = length_match_per_bucket(jailbreak_convs, benign_convs)
    if jb_pb and bn_pb:
        pb_convs = jb_pb + bn_pb
        pb_labels = [get_label(c) for c in pb_convs]
        pb_preds, _ = predict(encoder, gru, tokenizer, pb_convs)
        pb_metrics = compute_metrics(pb_labels, pb_preds)
        print(f"  Bucket-matched F1: {pb_metrics['f1_macro']:.4f} "
              f"(n={pb_metrics['n']}, buckets={len(bucket_info)})")
    else:
        pb_metrics = None
        print("  Bucket-matched: NO SHARED BUCKETS")

    delta_range = None
    delta_bucket = None
    if matched_metrics:
        delta_range = matched_metrics["f1_macro"] - full_metrics["f1_macro"]
    if pb_metrics:
        delta_bucket = pb_metrics["f1_macro"] - full_metrics["f1_macro"]

    return {
        "full": full_metrics,
        "range_matched": matched_metrics,
        "bucket_matched": pb_metrics,
        "match_info": match_info,
        "bucket_info": bucket_info,
        "delta_range_matched": delta_range,
        "delta_bucket_matched": delta_bucket,
    }


def main():
    print("=" * 70)
    print("EXP67: Length-Matched Control Experiment")
    print("=" * 70)

    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    dd_jailbreak = load_jsonl(DD_PATH)
    aa_jailbreak = load_jsonl(AA_PATH)

    print(f"\nDD jailbreak: {len(dd_jailbreak)} conversations")
    print(f"AA jailbreak: {len(aa_jailbreak)} conversations")

    all_results = {}
    for seed in SEEDS:
        print(f"\n{'='*70}")
        print(f"SEED {seed}")
        print(f"{'='*70}")

        test_data = load_jsonl(PROJ / f"data/exp59_resample/seed{seed}/test.jsonl")
        test_benign = [c for c in test_data if c["label"] == "benign"]
        print(f"Test benign: {len(test_benign)} conversations")

        encoder = load_encoder(seed)
        gru = load_gru(seed)

        dd_result = eval_one_setting(encoder, gru, tokenizer, dd_jailbreak, test_benign, f"DD OOD (seed={seed})")
        aa_result = eval_one_setting(encoder, gru, tokenizer, aa_jailbreak, test_benign, f"AA OOD (seed={seed})")

        all_results[f"seed{seed}"] = {"dd_ood": dd_result, "aa_ood": aa_result}

        del encoder, gru
        torch.cuda.empty_cache()

    # Aggregate across seeds
    print(f"\n{'='*70}")
    print("AGGREGATE RESULTS (mean ± std across 3 seeds)")
    print(f"{'='*70}")

    summary = {}
    for setting in ["dd_ood", "aa_ood"]:
        full_f1s = [all_results[f"seed{s}"][setting]["full"]["f1_macro"] for s in SEEDS]
        range_f1s = [all_results[f"seed{s}"][setting]["range_matched"]["f1_macro"]
                     for s in SEEDS if all_results[f"seed{s}"][setting]["range_matched"]]
        bucket_f1s = [all_results[f"seed{s}"][setting]["bucket_matched"]["f1_macro"]
                      for s in SEEDS if all_results[f"seed{s}"][setting]["bucket_matched"]]

        deltas_range = [all_results[f"seed{s}"][setting]["delta_range_matched"]
                        for s in SEEDS if all_results[f"seed{s}"][setting]["delta_range_matched"] is not None]
        deltas_bucket = [all_results[f"seed{s}"][setting]["delta_bucket_matched"]
                         for s in SEEDS if all_results[f"seed{s}"][setting]["delta_bucket_matched"] is not None]

        summary[setting] = {
            "full_f1_mean": float(np.mean(full_f1s)),
            "full_f1_std": float(np.std(full_f1s)),
            "full_f1_per_seed": {f"seed{s}": all_results[f"seed{s}"][setting]["full"]["f1_macro"] for s in SEEDS},
        }

        if range_f1s:
            summary[setting].update({
                "range_matched_f1_mean": float(np.mean(range_f1s)),
                "range_matched_f1_std": float(np.std(range_f1s)),
                "range_matched_f1_per_seed": {f"seed{s}": all_results[f"seed{s}"][setting]["range_matched"]["f1_macro"]
                                               for s in SEEDS if all_results[f"seed{s}"][setting]["range_matched"]},
                "delta_range_mean": float(np.mean(deltas_range)),
                "delta_range_std": float(np.std(deltas_range)),
            })

        if bucket_f1s:
            summary[setting].update({
                "bucket_matched_f1_mean": float(np.mean(bucket_f1s)),
                "bucket_matched_f1_std": float(np.std(bucket_f1s)),
                "bucket_matched_f1_per_seed": {f"seed{s}": all_results[f"seed{s}"][setting]["bucket_matched"]["f1_macro"]
                                                for s in SEEDS if all_results[f"seed{s}"][setting]["bucket_matched"]},
                "delta_bucket_mean": float(np.mean(deltas_bucket)),
                "delta_bucket_std": float(np.std(deltas_bucket)),
            })

        print(f"\n{setting.upper()}:")
        print(f"  Full-set F1:     {summary[setting]['full_f1_mean']:.4f} ± {summary[setting]['full_f1_std']:.4f}")
        if range_f1s:
            print(f"  Range-matched:   {summary[setting]['range_matched_f1_mean']:.4f} ± {summary[setting]['range_matched_f1_std']:.4f}"
                  f"  (Δ = {summary[setting]['delta_range_mean']:+.4f})")
        if bucket_f1s:
            print(f"  Bucket-matched:  {summary[setting]['bucket_matched_f1_mean']:.4f} ± {summary[setting]['bucket_matched_f1_std']:.4f}"
                  f"  (Δ = {summary[setting]['delta_bucket_mean']:+.4f})")

    conclusion = []
    for setting in ["dd_ood", "aa_ood"]:
        s = summary[setting]
        if "delta_range_mean" in s:
            delta = abs(s["delta_range_mean"])
            if delta < 0.03:
                conclusion.append(f"{setting}: F1 stable under length matching (Δ={s['delta_range_mean']:+.4f})")
            else:
                conclusion.append(f"{setting}: F1 changed under length matching (Δ={s['delta_range_mean']:+.4f})")

    print(f"\n--- Conclusion ---")
    for c in conclusion:
        print(f"  {c}")

    output = {
        "experiment": "exp67_length_matching",
        "description": "Length-matched control: verify OOD detection is not driven by turn-count shortcut",
        "model": "exp59 DeBERTa 9-class + BiGRU (3 seeds)",
        "seeds": SEEDS,
        "per_seed": all_results,
        "summary": summary,
        "conclusion": conclusion,
    }

    out_path = PROJ / "results/exp67_length_matching.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved to {out_path}")


if __name__ == "__main__":
    main()
