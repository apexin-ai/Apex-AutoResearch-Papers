"""
llama_filter_and_extract.py — Llama rp=1.0 soft filter + 3-ref feature extraction

Phase 1: Filter degenerate samples (repeated_4gram_ratio > 0.5)
Phase 2: Extract features with 3 reference models (Pythia-410M, OLMo-2-1B, Qwen3-0.6B)
"""

import argparse
import json
import sys
import time
from collections import Counter
from pathlib import Path

import numpy as np
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

DATA_DIR = Path("/root/gen-depth-fingerprint/data/mistral-7b-v0.3")
INPUT_FILE = DATA_DIR / "generations_shard0.jsonl"
FILTERED_FILE = DATA_DIR / "generations_filtered.jsonl"

REF_MODELS = {
    "pythia410m": "/root/autodl-tmp/models/pythia-410m/models--EleutherAI--pythia-410m/snapshots/9879c9b5f8bea9051dcb0e68dff21493d67e9d4f",
    "olmo2-1b": "/root/autodl-tmp/models/olmo-2-1b-hf/allenai/OLMo-2-0425-1B",
    "qwen3-06b": "/root/autodl-tmp/models/Qwen/Qwen3-0.6B-Base",
}


def compute_repeated_4gram_ratio(text: str) -> float:
    words = text.split()
    if len(words) < 4:
        return 0.0
    ngrams = [tuple(words[i:i+4]) for i in range(len(words) - 3)]
    total = len(ngrams)
    counter = Counter(ngrams)
    repeated = sum(count for count in counter.values() if count > 1)
    return repeated / total


def phase1_filter():
    print("=" * 60)
    print("PHASE 1: Soft Degenerate Filter (repeated_4gram_ratio > 0.5)")
    print("=" * 60)

    records = []
    with open(INPUT_FILE) as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))

    print(f"Loaded {len(records)} records from {INPUT_FILE.name}")

    depth_stats = {}
    filtered_records = []

    for rec in records:
        d = rec["depth"]
        if d not in depth_stats:
            depth_stats[d] = {"total": 0, "kept": 0}
        depth_stats[d]["total"] += 1

        ratio = compute_repeated_4gram_ratio(rec["text"])
        if ratio <= 0.5:
            filtered_records.append(rec)
            depth_stats[d]["kept"] += 1

    print("\nFilter Results:")
    total_orig, total_kept = 0, 0
    for d in sorted(depth_stats.keys()):
        s = depth_stats[d]
        removed = s["total"] - s["kept"]
        pct = 100.0 * removed / s["total"] if s["total"] > 0 else 0
        print(f"  Depth {d}: {s['total']} → {s['kept']} (filtered {removed}, {pct:.1f}%)")
        total_orig += s["total"]
        total_kept += s["kept"]

    removed_total = total_orig - total_kept
    pct_total = 100.0 * removed_total / total_orig if total_orig > 0 else 0
    print(f"  Total: {total_orig} → {total_kept} (filtered {removed_total}, {pct_total:.1f}%)")

    with open(FILTERED_FILE, "w") as f:
        for rec in filtered_records:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    print(f"\nFiltered data saved to {FILTERED_FILE}")
    return filtered_records


def load_model(model_path: str, device: str):
    print(f"  Loading model from {model_path}")
    tokenizer = AutoTokenizer.from_pretrained(model_path, local_files_only=True, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        model_path, local_files_only=True, torch_dtype=torch.float16, trust_remote_code=True,
    ).to(device).eval()
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    print(f"  Model loaded on {device}")
    return tokenizer, model


def compute_per_token_nll(texts, tokenizer, model, device, batch_size=8):
    """Compute per-token NLL for each text. Returns list of numpy arrays."""
    all_nlls = []
    for start in range(0, len(texts), batch_size):
        batch_texts = texts[start:start + batch_size]
        encodings = tokenizer(
            batch_texts, return_tensors="pt", padding=True,
            truncation=True, max_length=512,
        ).to(device)

        with torch.no_grad():
            logits = model(**encodings).logits

        for i in range(len(batch_texts)):
            mask = encodings["attention_mask"][i].bool()
            seq_len = mask.sum().item()
            if seq_len < 2:
                all_nlls.append(np.array([0.0]))
                continue

            token_logits = logits[i, :seq_len - 1, :]
            target_ids = encodings["input_ids"][i, 1:seq_len]
            log_probs = torch.log_softmax(token_logits, dim=-1)
            token_log_probs = log_probs.gather(1, target_ids.unsqueeze(1)).squeeze(1)
            nll = -token_log_probs.float().cpu().numpy()
            all_nlls.append(nll)

        if (start // batch_size) % 20 == 0:
            print(f"    [{min(start + batch_size, len(texts))}/{len(texts)}]")

    return all_nlls


def compute_entropy_features(texts, tokenizer, model, device, batch_size=8):
    """Compute entropy stats per text."""
    results = []
    for start in range(0, len(texts), batch_size):
        batch_texts = texts[start:start + batch_size]
        encodings = tokenizer(
            batch_texts, return_tensors="pt", padding=True,
            truncation=True, max_length=512,
        ).to(device)

        with torch.no_grad():
            logits = model(**encodings).logits

        for i in range(len(batch_texts)):
            mask = encodings["attention_mask"][i].bool()
            seq_len = mask.sum().item()
            if seq_len < 2:
                results.append({
                    "entropy_mean": 0.0, "entropy_std": 0.0,
                    "entropy_min": 0.0, "entropy_max": 0.0,
                })
                continue

            token_logits = logits[i, :seq_len - 1, :]
            log_probs = torch.log_softmax(token_logits, dim=-1)
            probs = torch.exp(log_probs)
            entropy = -(probs * log_probs).sum(dim=-1)
            entropy_np = entropy.float().cpu().numpy()

            results.append({
                "entropy_mean": float(np.mean(entropy_np)),
                "entropy_std": float(np.std(entropy_np)),
                "entropy_min": float(np.min(entropy_np)),
                "entropy_max": float(np.max(entropy_np)),
            })

        if (start // batch_size) % 20 == 0:
            print(f"    [{min(start + batch_size, len(texts))}/{len(texts)}]")

    return results


def phase2_extract(records, device="cuda:0", batch_size=8):
    print("\n" + "=" * 60)
    print("PHASE 2: 3-Reference Model Feature Extraction")
    print("=" * 60)

    texts = [r["text"] for r in records]
    depths = [r["depth"] for r in records]

    # Surface features (computed once)
    print("\nComputing surface features (TTR, hapax_ratio)...")
    surface_features = []
    for text in texts:
        words = text.lower().split()
        n = len(words)
        if n == 0:
            surface_features.append({"ttr": 0.0, "hapax_ratio": 0.0})
            continue
        counter = Counter(words)
        surface_features.append({
            "ttr": len(counter) / n,
            "hapax_ratio": sum(1 for c in counter.values() if c == 1) / n,
        })
    print(f"  Done: {len(surface_features)} records")

    # Depth-0 indices for threshold computation
    depth0_indices = [i for i, d in enumerate(depths) if d == 0]
    depth0_texts = [texts[i] for i in depth0_indices]
    print(f"\n  Depth-0 samples for threshold: {len(depth0_texts)}")

    for ref_name, ref_path in REF_MODELS.items():
        print(f"\n{'─' * 50}")
        print(f"Reference model: {ref_name}")
        print(f"{'─' * 50}")
        t0 = time.time()

        tokenizer, model = load_model(ref_path, device)

        # Step 1: Compute NLL threshold from depth-0 data
        print("  Computing NLL threshold from depth-0 data...")
        depth0_nlls = compute_per_token_nll(depth0_texts, tokenizer, model, device, batch_size)
        all_depth0_nll_values = np.concatenate(depth0_nlls)
        threshold_90 = float(np.percentile(all_depth0_nll_values, 90))
        print(f"  90th percentile NLL threshold: {threshold_90:.4f}")

        # Step 2: Compute entropy features + tail_decay for all texts
        print("  Computing entropy features...")
        entropy_feats = compute_entropy_features(texts, tokenizer, model, device, batch_size)

        print("  Computing tail_decay (NLL > threshold proportion)...")
        all_nlls = compute_per_token_nll(texts, tokenizer, model, device, batch_size)
        tail_decays = []
        for nll_arr in all_nlls:
            if len(nll_arr) == 0:
                tail_decays.append(0.0)
            else:
                tail_decays.append(float(np.mean(nll_arr > threshold_90)))

        # Free GPU memory
        del model, tokenizer
        torch.cuda.empty_cache()

        # Assemble and save
        output_path = DATA_DIR / f"features_{ref_name}.jsonl"
        with open(output_path, "w") as f:
            for i, rec in enumerate(records):
                row = {
                    "seed_id": rec["seed_id"],
                    "depth": rec["depth"],
                    **entropy_feats[i],
                    "tail_decay": tail_decays[i],
                    **surface_features[i],
                }
                f.write(json.dumps(row) + "\n")

        elapsed = time.time() - t0
        print(f"  Saved to {output_path} ({elapsed:.0f}s)")

    print("\n" + "=" * 60)
    print("ALL DONE")
    print("=" * 60)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--phase", choices=["1", "2", "both"], default="both")
    parser.add_argument("--device", default="cuda:0")
    parser.add_argument("--batch-size", type=int, default=8)
    parser.add_argument("--dry-run", action="store_true", help="Process only 20 records")
    args = parser.parse_args()

    if args.phase in ("1", "both"):
        records = phase1_filter()
    else:
        records = []
        with open(FILTERED_FILE) as f:
            for line in f:
                line = line.strip()
                if line:
                    records.append(json.loads(line))
        print(f"Loaded {len(records)} filtered records")

    if args.dry_run:
        records = records[:20]
        print(f"[dry-run] Using first 20 records")

    if args.phase in ("2", "both"):
        phase2_extract(records, device=args.device, batch_size=args.batch_size)


if __name__ == "__main__":
    main()
