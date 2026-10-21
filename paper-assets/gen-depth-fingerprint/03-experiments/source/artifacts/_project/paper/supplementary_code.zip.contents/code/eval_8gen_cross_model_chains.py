# Anonymous submission — EMNLP 2026 ARR
"""
eval_8gen_cross_model_chains.py -- Cross-model chain experiment

RQ3: Do depth fingerprints persist when each generation step uses a different model?
Cross-model chains randomly select a generator at each depth, simulating realistic
recursive generation where different LLMs contribute at different steps.

Pipeline:
  Phase 1 (generate): Depth-by-depth generation with random model selection.
    At each depth, group seeds by assigned generator, load one model at a time.
  Phase 2 (extract):  7-feature extraction using Pythia-410M reference model.
  Phase 3 (evaluate): 5-fold CV + comparison with single-model baselines.

Input:  data/wiki_seed_1000.jsonl
Output: data/cross-model-chains/generations_shard{X}.jsonl
        data/cross-model-chains/chain_assignments_shard{X}.json
        data/cross-model-chains/features.csv
        results/cross_model_chains_results.json

Usage:
  # Parallel generation on 2 GPUs:
  python eval_8gen_cross_model_chains.py --phase generate --shard-id 0 --num-shards 2 --device cuda:0
  python eval_8gen_cross_model_chains.py --phase generate --shard-id 1 --num-shards 2 --device cuda:1
  # After both complete:
  python eval_8gen_cross_model_chains.py --phase extract --device cuda:0
  python eval_8gen_cross_model_chains.py --phase evaluate
"""

import argparse
import gc
import json
import os
import random
import time
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np
import pandas as pd
import torch
from tqdm import tqdm
from transformers import AutoModelForCausalLM, AutoTokenizer
from scipy.stats import kruskal
from xgboost import XGBClassifier
from sklearn.metrics import f1_score, classification_report, confusion_matrix
from sklearn.model_selection import StratifiedKFold

SEED = 42
MAX_DEPTH = 4
NUM_DEPTHS = MAX_DEPTH + 1
MAX_TOKENS = 256
PROMPT_TOKENS = 128
MAX_NEW_TOKENS = 256

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = Path(os.path.join(ROOT, "..", "data"))
RESULTS_DIR = Path(os.path.join(ROOT, "results"))
OUTPUT_DIR = DATA_DIR / "cross-model-chains"

# Generator pool: set these to local model paths or HuggingFace model IDs.
# For generation phases, all models must be accessible.
GENERATOR_POOL = {
    "pythia-2.8b": os.environ.get("MODEL_PYTHIA_2_8B", "EleutherAI/pythia-2.8b"),
    "pythia-1b": os.environ.get("MODEL_PYTHIA_1B", "EleutherAI/pythia-1b"),
    "olmo-2-1b": os.environ.get("MODEL_OLMO_2_1B", "allenai/OLMo-2-0425-1B"),
    "qwen3-0.6b": os.environ.get("MODEL_QWEN3_0_6B", "Qwen/Qwen3-0.6B-Base"),
    "qwen3-1.7b": os.environ.get("MODEL_QWEN3_1_7B", "Qwen/Qwen3-1.7B-Base"),
}

REFERENCE_MODEL = os.environ.get("REFERENCE_MODEL", "EleutherAI/pythia-410m")

FEATURES = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max",
            "tail_decay", "ttr", "hapax_ratio"]

CLASS_MAP = {0: 0, 1: 1, 2: 2, 3: 2, 4: 2}
XGB_PARAMS = dict(n_estimators=200, max_depth=6, learning_rate=0.1,
                  random_state=SEED, eval_metric="mlogloss",
                  use_label_encoder=False)


# ================================================================
# Shared utilities
# ================================================================

def load_seeds(path, max_tokens=256):
    """Load seeds, truncate with pythia-2.8b tokenizer for consistency."""
    tok = AutoTokenizer.from_pretrained(GENERATOR_POOL["pythia-2.8b"])
    seeds = []
    with open(path, "r") as f:
        for line_num, line in enumerate(f):
            item = json.loads(line)
            text = item.get("text", "")
            if len(text.strip()) < 100:
                continue
            token_ids = tok.encode(text, add_special_tokens=False)[:max_tokens]
            if len(token_ids) < 64:
                continue
            seeds.append({"seed_id": line_num, "text": tok.decode(token_ids)})
    print(f"Loaded {len(seeds)} seeds from {path}")
    return seeds


def assign_generators(seed_ids, max_depth, generator_names, rng_seed=42):
    """Pre-assign a random generator for each (seed_id, depth) pair.
    Deterministic: same rng_seed always produces same assignments."""
    rng = random.Random(rng_seed)
    assignments = {}
    for sid in sorted(seed_ids):
        for depth in range(1, max_depth + 1):
            assignments[(sid, depth)] = rng.choice(generator_names)
    return assignments


def generate_continuation(model, tokenizer, text, device,
                          max_new_tokens=256, prompt_tokens=128):
    input_ids = tokenizer.encode(text, add_special_tokens=False)
    if len(input_ids) == 0:
        return ""
    input_ids = input_ids[-prompt_tokens:]
    input_tensor = torch.tensor([input_ids], device=device)
    with torch.no_grad():
        output = model.generate(
            input_tensor,
            max_new_tokens=max_new_tokens,
            temperature=0.7,
            top_p=0.9,
            do_sample=True,
            pad_token_id=tokenizer.pad_token_id,
        )
    new_tokens = output[0][len(input_ids):]
    return tokenizer.decode(new_tokens, skip_special_tokens=True)


def load_generator(model_name, model_path, device):
    print(f"Loading generator {model_name} on {device}")
    tokenizer = AutoTokenizer.from_pretrained(
        model_path, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        model_path, torch_dtype=torch.float16,
        trust_remote_code=True,
    ).to(device).eval()
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    print(f"  Loaded {model_name}, vocab={model.config.vocab_size}")
    return model, tokenizer


def unload_model(model, tokenizer):
    del model, tokenizer
    gc.collect()
    torch.cuda.empty_cache()


# ================================================================
# Phase 1: Generate cross-model chains
# ================================================================

def load_existing_records(output_path):
    records = {}
    if not os.path.exists(output_path):
        return records
    with open(output_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
                records[(rec["seed_id"], rec["depth"])] = rec
            except (json.JSONDecodeError, KeyError):
                pass
    return records


def phase_generate(args):
    torch.manual_seed(SEED)
    torch.cuda.manual_seed(SEED)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    seed_path = DATA_DIR / "wiki_seed_1000.jsonl"
    all_seeds = load_seeds(str(seed_path))

    total = len(all_seeds)
    shard_size = total // args.num_shards
    start = args.shard_id * shard_size
    end = start + shard_size if args.shard_id < args.num_shards - 1 else total
    seeds = all_seeds[start:end]
    print(f"Shard {args.shard_id}/{args.num_shards}: seeds [{start}:{end}] ({len(seeds)} seeds)")

    if args.dry_run:
        seeds = seeds[:3]
        print(f"[DRY-RUN] Processing only {len(seeds)} seeds")

    seed_ids = [s["seed_id"] for s in seeds]
    generator_names = list(GENERATOR_POOL.keys())
    assignments = assign_generators(seed_ids, MAX_DEPTH, generator_names, rng_seed=SEED)

    assign_path = OUTPUT_DIR / f"chain_assignments_shard{args.shard_id}.json"
    assign_serializable = {f"{sid}_{d}": gen for (sid, d), gen in assignments.items()}
    with open(str(assign_path), "w") as f:
        json.dump(assign_serializable, f, indent=2)
    print(f"Assignments saved to {assign_path}")

    output_path = OUTPUT_DIR / f"generations_shard{args.shard_id}.jsonl"
    existing = load_existing_records(str(output_path))
    print(f"Found {len(existing)} existing records for resume")

    # Build current_texts from seeds + existing records
    current_texts = {}
    for s in seeds:
        current_texts[s["seed_id"]] = s["text"]

    # Replay existing records to get latest text per seed
    for (sid, d), rec in sorted(existing.items(), key=lambda x: (x[0][0], x[0][1])):
        if sid in current_texts:
            current_texts[sid] = rec["text"]

    t0 = time.time()

    # Write depth=0 records
    with open(str(output_path), "a") as f:
        for s in seeds:
            sid = s["seed_id"]
            if (sid, 0) in existing:
                continue
            rec = {
                "id": sid * NUM_DEPTHS,
                "depth": 0,
                "text": s["text"],
                "seed_id": sid,
                "token_count": len(s["text"].split()),
                "generator_at_depth": "wikipedia",
                "chain_generators": ["wikipedia"],
            }
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            f.flush()
            existing[(sid, 0)] = rec

    # Depth-by-depth generation
    for depth in range(1, NUM_DEPTHS):
        todo_seeds = [s for s in seeds if (s["seed_id"], depth) not in existing]
        if not todo_seeds:
            print(f"Depth {depth}: all {len(seeds)} seeds complete, skipping")
            continue

        # Check prerequisite: all todo seeds must have depth-1 completed
        missing_prev = [s for s in todo_seeds if (s["seed_id"], depth - 1) not in existing]
        if missing_prev:
            print(f"WARNING: {len(missing_prev)} seeds missing depth {depth-1}, skipping them")
            todo_seeds = [s for s in todo_seeds if s not in missing_prev]

        gen_groups = defaultdict(list)
        for s in todo_seeds:
            gen_name = assignments[(s["seed_id"], depth)]
            gen_groups[gen_name].append(s)

        print(f"\nDepth {depth}: {len(todo_seeds)} seeds across {len(gen_groups)} generators")
        for gn, gs in gen_groups.items():
            print(f"  {gn}: {len(gs)} seeds")

        for gen_name, gen_seeds in gen_groups.items():
            model_path = GENERATOR_POOL[gen_name]
            model, tokenizer = load_generator(gen_name, model_path, args.device)

            skipped = 0
            with open(str(output_path), "a") as f:
                for s in tqdm(gen_seeds, desc=f"d{depth}/{gen_name}"):
                    sid = s["seed_id"]
                    prev_text = current_texts.get(sid, "")

                    if len(prev_text.strip()) < 10:
                        print(f"WARNING: seed {sid} depth {depth}: input too short, skipping")
                        skipped += 1
                        continue

                    continuation = generate_continuation(
                        model, tokenizer, prev_text, args.device,
                        max_new_tokens=MAX_NEW_TOKENS, prompt_tokens=PROMPT_TOKENS,
                    )
                    if not continuation or len(continuation.strip()) == 0:
                        print(f"WARNING: seed {sid} depth {depth}: empty output, skipping")
                        skipped += 1
                        continue

                    chain_gens = ["wikipedia"]
                    for dd in range(1, depth + 1):
                        chain_gens.append(assignments[(sid, dd)])

                    cont_tokens = tokenizer.encode(continuation, add_special_tokens=False)
                    rec = {
                        "id": sid * NUM_DEPTHS + depth,
                        "depth": depth,
                        "text": continuation,
                        "seed_id": sid,
                        "token_count": len(cont_tokens),
                        "generator_at_depth": gen_name,
                        "chain_generators": chain_gens,
                    }
                    f.write(json.dumps(rec, ensure_ascii=False) + "\n")
                    f.flush()

                    current_texts[sid] = continuation
                    existing[(sid, depth)] = rec

            if skipped:
                print(f"  {gen_name}: skipped {skipped} seeds")
            unload_model(model, tokenizer)

        elapsed = time.time() - t0
        done_at_depth = sum(1 for s in seeds if (s["seed_id"], depth) in existing)
        print(f"Depth {depth} done: {done_at_depth}/{len(seeds)} seeds, {elapsed:.0f}s elapsed")

    elapsed = time.time() - t0
    print(f"\nGeneration complete. {len(existing)} total records in {elapsed:.1f}s")


# ================================================================
# Phase 2: Feature extraction
# ================================================================

def compute_reference_features(texts, tokenizer, model, device, batch_size=8):
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
                results.append({k: 0.0 for k in
                    ["entropy_mean", "entropy_std", "entropy_min", "entropy_max", "tail_decay"]})
                continue

            token_logits = logits[i, :seq_len - 1, :]
            log_probs = torch.log_softmax(token_logits, dim=-1)
            probs = torch.exp(log_probs)
            entropy = -(probs * log_probs).sum(dim=-1)
            entropy_np = entropy.float().cpu().numpy()

            avg_log_probs = log_probs.float().mean(dim=0)
            sorted_lp, _ = torch.sort(avg_log_probs, descending=True)
            sorted_lp_np = sorted_lp.cpu().numpy()
            vocab_size = sorted_lp_np.shape[0]
            hi = min(1000, vocab_size)
            lo = min(100, hi)
            if hi - lo >= 2:
                x = np.arange(lo, hi, dtype=np.float64)
                y = sorted_lp_np[lo:hi].astype(np.float64)
                coeffs = np.polyfit(x, y, 1)
                tail_decay = float(coeffs[0])
            else:
                tail_decay = 0.0

            results.append({
                "entropy_mean": float(np.mean(entropy_np)),
                "entropy_std": float(np.std(entropy_np)),
                "entropy_min": float(np.min(entropy_np)),
                "entropy_max": float(np.max(entropy_np)),
                "tail_decay": tail_decay,
            })

        if (start + batch_size) % 200 == 0 or start + batch_size >= len(texts):
            print(f"  Ref features: {min(start + batch_size, len(texts))}/{len(texts)}")

    return results


def compute_surface_features(texts):
    results = []
    for text in texts:
        words = text.lower().split()
        n_tokens = len(words)
        if n_tokens == 0:
            results.append({"ttr": 0.0, "hapax_ratio": 0.0})
            continue
        counter = Counter(words)
        results.append({
            "ttr": len(counter) / n_tokens,
            "hapax_ratio": sum(1 for c in counter.values() if c == 1) / n_tokens,
        })
    return results


def phase_extract(args):
    records = []
    for shard_file in sorted(OUTPUT_DIR.glob("generations_shard*.jsonl")):
        with open(shard_file) as f:
            for line in f:
                line = line.strip()
                if line:
                    records.append(json.loads(line))
    print(f"Loaded {len(records)} records from {OUTPUT_DIR}")

    if not records:
        print("ERROR: No records found. Run --phase generate first.")
        return

    texts = [r["text"] for r in records]

    print(f"Loading reference model...")
    tokenizer = AutoTokenizer.from_pretrained(REFERENCE_MODEL)
    model = AutoModelForCausalLM.from_pretrained(
        REFERENCE_MODEL, torch_dtype=torch.float16,
    ).to(args.device).eval()
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    ref_feats = compute_reference_features(
        texts, tokenizer, model, args.device, batch_size=args.batch_size)
    del model, tokenizer
    torch.cuda.empty_cache()

    surf_feats = compute_surface_features(texts)

    rows = []
    for rec, ref, surf in zip(records, ref_feats, surf_feats):
        rows.append({
            "id": rec["id"],
            "depth": rec["depth"],
            "seed_id": rec["seed_id"],
            "generator_at_depth": rec.get("generator_at_depth", ""),
            "chain_generators": json.dumps(rec.get("chain_generators", [])),
            **ref,
            **surf,
        })

    df = pd.DataFrame(rows)
    output_path = OUTPUT_DIR / "features.csv"
    df.to_csv(output_path, index=False)
    print(f"Features saved to {output_path}, shape={df.shape}")
    print(df.groupby("depth")[FEATURES].mean().round(4))


# ================================================================
# Phase 3: Evaluate
# ================================================================

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (np.bool_,)):
            return bool(obj)
        if isinstance(obj, (np.integer,)):
            return int(obj)
        if isinstance(obj, (np.floating,)):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super().default(obj)


def run_cv(X, y, n_splits=5):
    """Run stratified k-fold CV, return per-fold F1 scores and OOF predictions."""
    skf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=SEED)
    fold_f1s = []
    oof_preds = np.zeros_like(y)

    for fold, (train_idx, test_idx) in enumerate(skf.split(X, y)):
        clf = XGBClassifier(**XGB_PARAMS)
        clf.fit(X[train_idx], y[train_idx])
        preds = clf.predict(X[test_idx])
        f1 = f1_score(y[test_idx], preds, average="macro", zero_division=0)
        fold_f1s.append(f1)
        oof_preds[test_idx] = preds

    return fold_f1s, oof_preds


def balance_dataset(df):
    gen0 = df[df["label"] == 0]
    gen1 = df[df["label"] == 1]
    gen2plus = df[df["label"] == 2]
    gen2_parts = []
    for d in [2, 3, 4]:
        subset = gen2plus[gen2plus["depth"] == d]
        n = min(333, len(subset))
        if n > 0:
            gen2_parts.append(subset.sample(n=n, random_state=SEED))
    gen2_sampled = pd.concat(gen2_parts, ignore_index=True) if gen2_parts else gen2plus
    min_size = min(len(gen0), len(gen1), len(gen2_sampled))
    return pd.concat([
        gen0.sample(n=min_size, random_state=SEED),
        gen1.sample(n=min_size, random_state=SEED),
        gen2_sampled.sample(n=min(min_size, len(gen2_sampled)), random_state=SEED),
    ], ignore_index=True)


def evaluate_single_model(feat_path):
    """Evaluate a single-model feature file with same pipeline."""
    df = pd.read_csv(feat_path)
    if "depth" not in df.columns or not all(f in df.columns for f in FEATURES):
        return None
    df["label"] = df["depth"].map(CLASS_MAP)
    balanced = balance_dataset(df)
    if len(balanced) < 30:
        return None
    X = balanced[FEATURES].values
    y = balanced["label"].values
    fold_f1s, _ = run_cv(X, y)
    return {
        "macro_f1_mean": round(float(np.mean(fold_f1s)), 4),
        "macro_f1_std": round(float(np.std(fold_f1s)), 4),
        "n_samples": len(balanced),
    }


def phase_evaluate(args):
    feat_path = OUTPUT_DIR / "features.csv"
    if not feat_path.exists():
        print("ERROR: Features not found. Run --phase extract first.")
        return

    df = pd.read_csv(feat_path)
    print(f"Loaded {len(df)} records, depths: {sorted(df['depth'].unique())}")

    df["label"] = df["depth"].map(CLASS_MAP)
    balanced = balance_dataset(df)
    print(f"Balanced: {len(balanced)} samples, {balanced['label'].value_counts().to_dict()}")

    X = balanced[FEATURES].values
    y = balanced["label"].values

    fold_f1s, oof_preds = run_cv(X, y)
    cross_model_f1 = np.mean(fold_f1s)
    cross_model_std = np.std(fold_f1s)
    print(f"\nCross-model chains: macro-F1 = {cross_model_f1:.4f} +/- {cross_model_std:.4f}")

    for i, f1 in enumerate(fold_f1s):
        print(f"  Fold {i}: {f1:.4f}")

    cm = confusion_matrix(y, oof_preds).tolist()
    report = classification_report(y, oof_preds, output_dict=True, zero_division=0)

    # Binary F1: gen-0 vs gen-2+
    mask_bin = np.isin(y, [0, 2])
    if mask_bin.sum() > 0:
        y_bt = (y[mask_bin] == 2).astype(int)
        y_bp = (oof_preds[mask_bin] == 2).astype(int)
        binary_f1 = f1_score(y_bt, y_bp, zero_division=0)
    else:
        binary_f1 = 0.0

    # Feature importance (full retrain)
    clf_full = XGBClassifier(**XGB_PARAMS)
    clf_full.fit(X, y)
    importance = dict(zip(FEATURES, [round(float(x), 4) for x in clf_full.feature_importances_]))

    # Generator diversity analysis
    if "chain_generators" in df.columns:
        chain_data = df[df["depth"] == MAX_DEPTH].copy()
        if len(chain_data) > 0:
            chain_data["chain_list"] = chain_data["chain_generators"].apply(
                lambda x: json.loads(x) if isinstance(x, str) else x)
            chain_data["n_unique_gens"] = chain_data["chain_list"].apply(
                lambda x: len(set(x[1:])))  # exclude "wikipedia"
            diversity_stats = {
                "mean_unique_generators": round(float(chain_data["n_unique_gens"].mean()), 2),
                "std_unique_generators": round(float(chain_data["n_unique_gens"].std()), 2),
                "distribution": chain_data["n_unique_gens"].value_counts().to_dict(),
            }
        else:
            diversity_stats = {}
    else:
        diversity_stats = {}

    # Single-model baselines
    print("\n--- Single-model baselines ---")
    single_model_results = {}
    candidate_paths = [
        ("pythia-2.8b", DATA_DIR / "pythia-2.8b-continuation" / "features.csv"),
        ("pythia-2.8b", DATA_DIR / "features_pythia-2.8b.csv"),
        ("pythia-1b", DATA_DIR / "pythia-1b" / "features.csv"),
        ("pythia-1b", DATA_DIR / "features_pythia-1b.csv"),
        ("olmo-2-1b", DATA_DIR / "olmo-2-1b" / "features.csv"),
        ("olmo-2-1b", DATA_DIR / "features_olmo-2-1b.csv"),
        ("qwen3-0.6b", DATA_DIR / "qwen3-0.6b" / "features.csv"),
        ("qwen3-0.6b", DATA_DIR / "features_qwen3-0.6b.csv"),
        ("qwen3-1.7b", DATA_DIR / "qwen3-1.7b" / "features.csv"),
        ("qwen3-1.7b", DATA_DIR / "features_qwen3-1.7b.csv"),
    ]
    for model_name, fpath in candidate_paths:
        if model_name in single_model_results:
            continue
        if not fpath.exists():
            continue
        result = evaluate_single_model(fpath)
        if result:
            single_model_results[model_name] = result
            print(f"  {model_name}: macro-F1 = {result['macro_f1_mean']:.4f} +/- {result['macro_f1_std']:.4f}")

    # Kruskal-Wallis tests
    stat_tests = []
    n_features = len(FEATURES)
    alpha_corrected = 0.05 / n_features
    groups = [balanced[balanced["label"] == lbl] for lbl in [0, 1, 2]]
    for feat in FEATURES:
        group_vals = [g[feat].dropna().values for g in groups]
        if any(len(g) < 2 for g in group_vals):
            stat_tests.append({"feature": feat, "H": None, "p": None, "sig": False})
            continue
        h_stat, p_val = kruskal(*group_vals)
        stat_tests.append({
            "feature": feat,
            "H": round(float(h_stat), 4),
            "p": float(p_val),
            "sig": p_val < alpha_corrected,
        })

    results = {
        "experiment": "cross_model_chains",
        "cross_model": {
            "macro_f1_mean": round(cross_model_f1, 4),
            "macro_f1_std": round(cross_model_std, 4),
            "binary_f1_gen0_vs_gen2plus": round(binary_f1, 4),
            "fold_f1s": [round(f, 4) for f in fold_f1s],
            "n_samples": len(balanced),
            "confusion_matrix": cm,
            "per_class": {
                cls_name: {
                    "precision": round(report[str(cls_label)]["precision"], 4),
                    "recall": round(report[str(cls_label)]["recall"], 4),
                    "f1": round(report[str(cls_label)]["f1-score"], 4),
                }
                for cls_label, cls_name in [(0, "gen-0"), (1, "gen-1"), (2, "gen-2+")]
                if str(cls_label) in report
            },
            "feature_importance": importance,
            "statistical_tests": stat_tests,
        },
        "generator_diversity": diversity_stats,
        "single_model_baselines": single_model_results,
        "generator_pool": list(GENERATOR_POOL.keys()),
    }

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    result_path = RESULTS_DIR / "cross_model_chains_results.json"
    with open(result_path, "w") as f:
        json.dump(results, f, indent=2, cls=NumpyEncoder)
    print(f"\nResults saved to {result_path}")
    print(json.dumps(results, indent=2, cls=NumpyEncoder))


# ================================================================
# Main
# ================================================================

def main():
    parser = argparse.ArgumentParser(description="Cross-model chain experiment")
    parser.add_argument("--phase", choices=["generate", "extract", "evaluate", "all"],
                        default="all")
    parser.add_argument("--device", default="cuda:0")
    parser.add_argument("--shard-id", type=int, default=0)
    parser.add_argument("--num-shards", type=int, default=1)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--batch-size", type=int, default=8)
    args = parser.parse_args()

    if args.phase in ("generate", "all"):
        phase_generate(args)
    if args.phase in ("extract", "all"):
        phase_extract(args)
    if args.phase in ("evaluate", "all"):
        phase_evaluate(args)


if __name__ == "__main__":
    main()
