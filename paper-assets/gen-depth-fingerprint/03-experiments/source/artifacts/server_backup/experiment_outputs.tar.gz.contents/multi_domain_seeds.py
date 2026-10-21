"""
multi_domain_seeds.py — Multi-domain seed experiment (plan_008)

Validates depth signal consistency across 4 text domains:
  wikipedia (existing baseline), news, scientific, creative

Pipeline: prepare seeds -> generate chains -> extract features -> evaluate
"""

import argparse
import json
import os
import re
import time
from collections import Counter
from pathlib import Path

import numpy as np
import pandas as pd
import torch
from scipy.stats import spearmanr
from tqdm import tqdm
from transformers import AutoModelForCausalLM, AutoTokenizer
from xgboost import XGBClassifier
from sklearn.metrics import f1_score
from sklearn.model_selection import StratifiedKFold

import signal
signal.signal(signal.SIGHUP, signal.SIG_IGN)

SEED = 42
GENERATOR_MODEL = "/root/autodl-tmp/models/pythia-2.8b"
GENERATOR_NAME = "EleutherAI/pythia-2.8b"
REFERENCE_MODEL = "/root/autodl-tmp/models/pythia-410m/models--EleutherAI--pythia-410m/snapshots/9879c9b5f8bea9051dcb0e68dff21493d67e9d4f"
DATA_DIR = Path("/root/gen-depth-fingerprint/data")
SEEDS_DIR = DATA_DIR / "seeds"
RESULTS_DIR = Path("/root/gen-depth-fingerprint/results")

NUM_SEEDS = 500
MAX_DEPTH = 4
NUM_DEPTHS = MAX_DEPTH + 1
MAX_TOKENS = 256
PROMPT_TOKENS = 128
MAX_NEW_TOKENS = 256

FEATURES = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max",
            "tail_decay", "ttr", "hapax_ratio"]
CLASS_MAP = {0: 0, 1: 1, 2: 2, 3: 2, 4: 2}
XGB_PARAMS = dict(n_estimators=200, max_depth=6, learning_rate=0.1,
                  random_state=SEED, eval_metric="mlogloss",
                  use_label_encoder=False)

DOMAINS = {
    "news": {
        "dataset": "abisee/cnn_dailymail",
        "config": "3.0.0",
        "split": "test",
        "text_field": "article",
    },
    "scientific": {
        "dataset": "ccdv/arxiv-summarization",
        "config": None,
        "split": "test",
        "text_field": "abstract",
    },
    "creative": {
        "dataset": "euclaise/writingprompts",
        "config": None,
        "split": "test",
        "text_field": "story",
    },
}


# ================================================================
# Phase 1: Seed Preparation
# ================================================================

def prepare_seeds_for_domain(domain_name, domain_cfg, tokenizer):
    """Download dataset and prepare 500 seeds as JSONL."""
    from datasets import load_dataset

    seed_path = SEEDS_DIR / f"{domain_name}_seed_{NUM_SEEDS}.jsonl"
    if seed_path.exists():
        count = sum(1 for _ in open(seed_path))
        print(f"  [{domain_name}] Seeds exist: {seed_path} ({count} seeds)")
        return seed_path, count

    print(f"  [{domain_name}] Loading dataset: {domain_cfg['dataset']}")

    load_kwargs = dict(
        split=domain_cfg["split"],
        cache_dir="/root/autodl-tmp/.hf_cache",
    )
    if domain_cfg["config"]:
        load_kwargs["name"] = domain_cfg["config"]

    try:
        ds = load_dataset(domain_cfg["dataset"], **load_kwargs, streaming=True)
    except Exception as e1:
        # Retry without trust_remote_code
        try:
            load_kwargs.pop("trust_remote_code", None)
            ds = load_dataset(domain_cfg["dataset"], **load_kwargs, streaming=True)
        except Exception as e2:
            print(f"  [{domain_name}] Primary dataset failed: {e2}")
            ds = _fallback_dataset(domain_name)
            if ds is None:
                print(f"  [{domain_name}] FAILED: no fallback available")
                return None, 0

    text_field = domain_cfg["text_field"]
    seeds = []

    for item in ds:
        text = item.get(text_field, "")
        if not text or len(text.strip()) < 100:
            continue
        # Clean text
        text = re.sub(r'\s+', ' ', text.strip())
        # Truncate to MAX_TOKENS tokens (align with Wikipedia seeds)
        token_ids = tokenizer.encode(text, add_special_tokens=False)[:MAX_TOKENS]
        if len(token_ids) < 64:
            continue
        truncated = tokenizer.decode(token_ids)
        seeds.append({"text": truncated, "seed_id": len(seeds), "domain": domain_name})
        if len(seeds) >= NUM_SEEDS:
            break

    SEEDS_DIR.mkdir(parents=True, exist_ok=True)
    with open(seed_path, "w") as f:
        for s in seeds:
            f.write(json.dumps(s, ensure_ascii=False) + "\n")

    print(f"  [{domain_name}] Saved {len(seeds)} seeds to {seed_path}")
    return seed_path, len(seeds)


def _fallback_dataset(domain_name):
    from datasets import load_dataset

    if domain_name == "scientific":
        for fallback_ds, fallback_split, fallback_field in [
            ("ccdv/arxiv-summarization", "test", "abstract"),
            ("multi_news", "test", "document"),
        ]:
            try:
                print(f"  [scientific] Trying fallback: {fallback_ds}")
                ds = load_dataset(fallback_ds, split=fallback_split, streaming=True,
                                  cache_dir="/root/autodl-tmp/.hf_cache")
                DOMAINS["scientific"]["text_field"] = fallback_field
                return ds
            except Exception:
                continue

    if domain_name == "creative":
        for fallback_ds, fallback_split, fallback_field in [
            ("reddit/writingprompts", "test", "story"),
            ("bookcorpus/bookcorpus", "train", "text"),
        ]:
            try:
                print(f"  [creative] Trying fallback: {fallback_ds}")
                ds = load_dataset(fallback_ds, split=fallback_split, streaming=True,
                                  cache_dir="/root/autodl-tmp/.hf_cache")
                DOMAINS["creative"]["text_field"] = fallback_field
                return ds
            except Exception:
                continue

    return None


def phase_seeds(tokenizer):
    print("=" * 60)
    print("PHASE 1: Seed Preparation")
    print("=" * 60)

    results = {}
    for domain_name, domain_cfg in DOMAINS.items():
        seed_path, count = prepare_seeds_for_domain(domain_name, domain_cfg, tokenizer)
        results[domain_name] = {"path": str(seed_path) if seed_path else None, "count": count}

    print(f"\nSeed summary:")
    for d, r in results.items():
        print(f"  {d}: {r['count']} seeds")
    return results


# ================================================================
# Phase 2: Chain Generation
# ================================================================

def load_seeds_from_file(path, tokenizer):
    seeds = []
    with open(path) as f:
        for line in f:
            item = json.loads(line.strip())
            text = item.get("text", "")
            if len(text.strip()) < 100:
                continue
            token_ids = tokenizer.encode(text, add_special_tokens=False)[:MAX_TOKENS]
            if len(token_ids) < 64:
                continue
            seeds.append({"seed_id": item.get("seed_id", len(seeds)),
                          "text": tokenizer.decode(token_ids)})
    return seeds


def generate_continuation(model, tokenizer, text, device):
    input_ids = tokenizer.encode(text, add_special_tokens=False)
    if len(input_ids) == 0:
        return ""
    input_ids = input_ids[-PROMPT_TOKENS:]
    input_tensor = torch.tensor([input_ids], device=device)

    with torch.no_grad():
        output = model.generate(
            input_tensor,
            max_new_tokens=MAX_NEW_TOKENS,
            temperature=1.0,
            top_p=0.95,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id,
        )

    new_tokens = output[0][len(input_ids):]
    return tokenizer.decode(new_tokens, skip_special_tokens=True)


def load_done_seeds(path):
    done = set()
    if not os.path.exists(path):
        return done
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                done.add(json.loads(line)["seed_id"])
            except (json.JSONDecodeError, KeyError):
                pass
    return done


def generate_for_domain(domain_name, seeds, model, tokenizer, device):
    output_dir = DATA_DIR / f"pythia-2.8b-{domain_name}"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "generations_shard0.jsonl"

    done_seeds = load_done_seeds(output_path)
    remaining = [s for s in seeds if s["seed_id"] not in done_seeds]

    if not remaining:
        total = sum(1 for _ in open(output_path))
        print(f"  [{domain_name}] All {len(seeds)} seeds done ({total} records)")
        return

    print(f"  [{domain_name}] {len(done_seeds)} done, {len(remaining)} remaining")
    t0 = time.time()
    record_count = 0

    with open(output_path, "a") as f:
        for i, seed_info in enumerate(tqdm(remaining, desc=domain_name)):
            seed_id = seed_info["seed_id"]
            seed_text = seed_info["text"]
            base_id = seed_id * NUM_DEPTHS

            gen0_tokens = tokenizer.encode(seed_text, add_special_tokens=False)
            f.write(json.dumps({
                "id": base_id, "depth": 0, "text": seed_text,
                "seed_id": seed_id, "token_count": len(gen0_tokens),
                "model": "pythia-2.8b", "domain": domain_name,
            }, ensure_ascii=False) + "\n")
            f.flush()
            record_count += 1

            prev_text = seed_text
            for depth in range(1, NUM_DEPTHS):
                check_ids = tokenizer.encode(prev_text, add_special_tokens=False)
                if len(check_ids) == 0 or len(prev_text.strip()) < 10:
                    print(f"  WARN: {domain_name} seed {seed_id} depth {depth}: empty, skipping")
                    break

                continuation = generate_continuation(model, tokenizer, prev_text, device)
                if not continuation or len(continuation.strip()) == 0:
                    print(f"  WARN: {domain_name} seed {seed_id} depth {depth}: empty output, skipping")
                    break

                cont_tokens = tokenizer.encode(continuation, add_special_tokens=False)
                f.write(json.dumps({
                    "id": base_id + depth, "depth": depth, "text": continuation,
                    "seed_id": seed_id, "token_count": len(cont_tokens),
                    "model": "pythia-2.8b", "domain": domain_name,
                }, ensure_ascii=False) + "\n")
                f.flush()
                record_count += 1
                prev_text = continuation

            if (i + 1) % 50 == 0:
                elapsed = time.time() - t0
                rate = (i + 1) / elapsed
                print(f"  [{domain_name}] [{i+1}/{len(remaining)}] {elapsed:.0f}s, {rate:.2f} seeds/s")

    elapsed = time.time() - t0
    print(f"  [{domain_name}] {record_count} new records in {elapsed:.1f}s")


def phase_generate(device):
    print("=" * 60)
    print("PHASE 2: Chain Generation (Pythia-2.8B)")
    print("=" * 60)

    print("Loading Pythia-2.8B...")
    tokenizer = AutoTokenizer.from_pretrained(
        GENERATOR_NAME, cache_dir=GENERATOR_MODEL, local_files_only=True)
    model = AutoModelForCausalLM.from_pretrained(
        GENERATOR_NAME, cache_dir=GENERATOR_MODEL, local_files_only=True,
        dtype=torch.float16,
    ).to(device)
    model.eval()
    print(f"Model on {device}")

    for domain_name in DOMAINS:
        seed_path = SEEDS_DIR / f"{domain_name}_seed_{NUM_SEEDS}.jsonl"
        if not seed_path.exists():
            print(f"  [{domain_name}] No seed file, skipping")
            continue

        seeds = load_seeds_from_file(seed_path, tokenizer)
        print(f"\n--- {domain_name}: {len(seeds)} seeds ---")
        torch.manual_seed(SEED)
        torch.cuda.manual_seed(SEED)
        generate_for_domain(domain_name, seeds, model, tokenizer, device)

    del model, tokenizer
    torch.cuda.empty_cache()
    print("\nGeneration complete\n")


# ================================================================
# Phase 3: Feature Extraction
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

        done = min(start + batch_size, len(texts))
        if done % (batch_size * 20) == 0 or done == len(texts):
            print(f"    ref features: [{done}/{len(texts)}]")

    return results


def compute_surface_features(texts):
    results = []
    for text in texts:
        words = text.lower().split()
        n = len(words)
        if n == 0:
            results.append({"ttr": 0.0, "hapax_ratio": 0.0})
            continue
        counter = Counter(words)
        results.append({
            "ttr": len(counter) / n,
            "hapax_ratio": sum(1 for c in counter.values() if c == 1) / n,
        })
    return results


def load_generation_records(data_dir):
    records = []
    seen = set()
    paths = sorted(data_dir.glob("generations*.jsonl"))
    for p in paths:
        with open(p) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                rec = json.loads(line)
                key = (rec["seed_id"], rec["depth"])
                if key not in seen:
                    seen.add(key)
                    records.append(rec)
    return records


def extract_features_for_domain(domain_name, ref_tokenizer, ref_model, device):
    feat_path = DATA_DIR / f"features_pythia-2.8b-{domain_name}.csv"

    if feat_path.exists():
        df = pd.read_csv(feat_path)
        print(f"  [{domain_name}] Features exist: {len(df)} rows")
        return df

    data_dir = DATA_DIR / f"pythia-2.8b-{domain_name}"
    if not data_dir.exists():
        print(f"  [{domain_name}] No generation data, skipping")
        return None

    records = load_generation_records(data_dir)
    print(f"  [{domain_name}] {len(records)} records loaded")

    texts = [r["text"] for r in records]
    print(f"  [{domain_name}] Computing reference features...")
    ref_feats = compute_reference_features(texts, ref_tokenizer, ref_model, device)
    surf_feats = compute_surface_features(texts)

    rows = []
    for rec, ref, surf in zip(records, ref_feats, surf_feats):
        rows.append({
            "model_name": "pythia-2.8b",
            "domain": domain_name,
            "seed_id": rec["seed_id"],
            "depth": rec["depth"],
            **ref, **surf,
        })

    df = pd.DataFrame(rows)
    df.to_csv(feat_path, index=False)
    print(f"  [{domain_name}] Saved: {feat_path} ({len(df)} rows)")
    return df


def phase_features(device):
    print("=" * 60)
    print("PHASE 3: Feature Extraction (Pythia-410M)")
    print("=" * 60)

    print("Loading Pythia-410M reference model...")
    ref_tokenizer = AutoTokenizer.from_pretrained(REFERENCE_MODEL, local_files_only=True)
    ref_model = AutoModelForCausalLM.from_pretrained(
        REFERENCE_MODEL, local_files_only=True, torch_dtype=torch.float16
    ).to(device).eval()
    if ref_tokenizer.pad_token is None:
        ref_tokenizer.pad_token = ref_tokenizer.eos_token
    print(f"Reference model on {device}")

    domain_features = {}
    for domain_name in DOMAINS:
        print(f"\n--- {domain_name} ---")
        df = extract_features_for_domain(domain_name, ref_tokenizer, ref_model, device)
        if df is not None:
            domain_features[domain_name] = df

    del ref_model, ref_tokenizer
    torch.cuda.empty_cache()
    print("\nFeature extraction complete\n")
    return domain_features


# ================================================================
# Phase 4: Evaluation
# ================================================================

def downsample(df, rng):
    min_n = df["label"].value_counts().min()
    parts = [df[df["label"] == lbl].sample(n=min_n, random_state=rng, replace=False)
             for lbl in sorted(df["label"].unique())]
    return pd.concat(parts, ignore_index=True)


def cv_evaluate(df, n_folds=5):
    """Stratified k-fold CV for single-domain evaluation."""
    X = df[FEATURES].values
    y = df["label"].values
    skf = StratifiedKFold(n_splits=n_folds, shuffle=True, random_state=SEED)

    yt_all, yp_all = [], []
    for train_idx, test_idx in skf.split(X, y):
        tr_df = df.iloc[train_idx]
        tr_balanced = downsample(tr_df, np.random.RandomState(SEED))
        clf = XGBClassifier(**XGB_PARAMS)
        clf.fit(tr_balanced[FEATURES].values, tr_balanced["label"].values)
        yp = clf.predict(X[test_idx])
        yt_all.append(y[test_idx])
        yp_all.append(yp)

    yt = np.concatenate(yt_all)
    yp = np.concatenate(yp_all)
    macro_f1 = f1_score(yt, yp, average="macro")
    per_cls = f1_score(yt, yp, average=None, labels=[0, 1, 2])

    mask = yt > 0
    binary_f1 = 0.0
    if mask.sum() > 0:
        binary_f1 = f1_score((yt[mask] > 1).astype(int), (yp[mask] > 1).astype(int), average="binary")

    return {
        "3class_f1": round(float(macro_f1), 4),
        "binary_f1": round(float(binary_f1), 4),
        "per_class_f1": {
            "gen-0": round(float(per_cls[0]), 4),
            "gen-1": round(float(per_cls[1]), 4),
            "gen-2+": round(float(per_cls[2]), 4),
        },
    }


def cross_domain_evaluate(domain_features):
    """Leave-one-domain-out evaluation."""
    all_df = pd.concat(domain_features.values(), ignore_index=True)
    all_df["label"] = all_df["depth"].map(CLASS_MAP)
    domains = sorted(all_df["domain"].unique())

    yt_all, yp_all = [], []
    per_domain = {}

    for held_out in domains:
        te = all_df[all_df["domain"] == held_out]
        tr = downsample(all_df[all_df["domain"] != held_out], np.random.RandomState(SEED))
        clf = XGBClassifier(**XGB_PARAMS)
        clf.fit(tr[FEATURES].values, tr["label"].values)
        yp = clf.predict(te[FEATURES].values)
        per_domain[held_out] = round(float(f1_score(te["label"].values, yp, average="macro")), 4)
        yt_all.append(te["label"].values)
        yp_all.append(yp)

    yt = np.concatenate(yt_all)
    yp = np.concatenate(yp_all)
    macro_f1 = f1_score(yt, yp, average="macro")
    per_cls = f1_score(yt, yp, average=None, labels=[0, 1, 2])

    mask = yt > 0
    binary_f1 = 0.0
    if mask.sum() > 0:
        binary_f1 = f1_score((yt[mask] > 1).astype(int), (yp[mask] > 1).astype(int), average="binary")

    return {
        "3class_f1": round(float(macro_f1), 4),
        "binary_f1": round(float(binary_f1), 4),
        "per_class_f1": {
            "gen-0": round(float(per_cls[0]), 4),
            "gen-1": round(float(per_cls[1]), 4),
            "gen-2+": round(float(per_cls[2]), 4),
        },
        "per_domain": per_domain,
    }


def wiki_transfer_evaluate(domain_features):
    """Train on Wikipedia (Pythia-2.8B features), test on each new domain."""
    wiki_feat_path = DATA_DIR / "features_pythia-2.8b.csv"
    if not wiki_feat_path.exists():
        print("  Wikipedia features not found, skipping transfer eval")
        return {}

    wiki_df = pd.read_csv(wiki_feat_path)
    wiki_df["label"] = wiki_df["depth"].map(CLASS_MAP)
    wiki_df["domain"] = "wikipedia"

    wiki_balanced = downsample(wiki_df, np.random.RandomState(SEED))
    clf = XGBClassifier(**XGB_PARAMS)
    clf.fit(wiki_balanced[FEATURES].values, wiki_balanced["label"].values)

    results = {}
    for domain_name, df in domain_features.items():
        df = df.copy()
        df["label"] = df["depth"].map(CLASS_MAP)
        yp = clf.predict(df[FEATURES].values)
        yt = df["label"].values
        macro_f1 = f1_score(yt, yp, average="macro")
        per_cls = f1_score(yt, yp, average=None, labels=[0, 1, 2])
        results[domain_name] = {
            "3class_f1": round(float(macro_f1), 4),
            "per_class_f1": {
                "gen-0": round(float(per_cls[0]), 4),
                "gen-1": round(float(per_cls[1]), 4),
                "gen-2+": round(float(per_cls[2]), 4),
            },
        }

    return results


def compute_spearman(df):
    corrs = {}
    for feat in FEATURES:
        rho, _ = spearmanr(df[feat].values, df["depth"].values)
        corrs[f"spearman_{feat}"] = round(float(rho), 4)
    return corrs


def phase_evaluate(domain_features=None):
    print("=" * 60)
    print("PHASE 4: Evaluation")
    print("=" * 60)

    if domain_features is None:
        domain_features = {}
        for domain_name in DOMAINS:
            feat_path = DATA_DIR / f"features_pythia-2.8b-{domain_name}.csv"
            if feat_path.exists():
                df = pd.read_csv(feat_path)
                df["domain"] = domain_name
                domain_features[domain_name] = df

    results = {"per_domain": {}, "cross_domain": {}, "wiki_transfer": {}}

    # Per-domain CV
    print("\n--- Per-domain 5-fold CV ---")
    for domain_name, df in domain_features.items():
        df = df.copy()
        df["label"] = df["depth"].map(CLASS_MAP)
        cv_res = cv_evaluate(df)
        spearman = compute_spearman(df)
        results["per_domain"][domain_name] = {**cv_res, **spearman}
        print(f"  {domain_name}: 3class_f1={cv_res['3class_f1']:.4f}, "
              f"binary_f1={cv_res['binary_f1']:.4f}")

    # Add Wikipedia features for cross-domain analysis
    wiki_feat_path = DATA_DIR / "features_pythia-2.8b.csv"
    all_domain_features = dict(domain_features)
    if wiki_feat_path.exists():
        wiki_df = pd.read_csv(wiki_feat_path)
        wiki_df["domain"] = "wikipedia"
        all_domain_features["wikipedia"] = wiki_df

        # Per-domain CV for wikipedia too (for comparison)
        wiki_df_eval = wiki_df.copy()
        wiki_df_eval["label"] = wiki_df_eval["depth"].map(CLASS_MAP)
        cv_res = cv_evaluate(wiki_df_eval)
        spearman = compute_spearman(wiki_df_eval)
        results["per_domain"]["wikipedia"] = {**cv_res, **spearman}
        print(f"  wikipedia: 3class_f1={cv_res['3class_f1']:.4f}, "
              f"binary_f1={cv_res['binary_f1']:.4f}")

    # Cross-domain leave-one-domain-out
    if len(all_domain_features) >= 2:
        print("\n--- Cross-domain (leave-one-domain-out) ---")
        cross_res = cross_domain_evaluate(all_domain_features)
        results["cross_domain"] = cross_res
        print(f"  Overall: 3class_f1={cross_res['3class_f1']:.4f}")
        for d, f1 in cross_res.get("per_domain", {}).items():
            print(f"    held-out {d}: {f1:.4f}")

    # Wikipedia transfer
    print("\n--- Wikipedia transfer (train wiki, test others) ---")
    transfer_res = wiki_transfer_evaluate(domain_features)
    results["wiki_transfer"] = transfer_res
    for d, r in transfer_res.items():
        print(f"  wiki -> {d}: 3class_f1={r['3class_f1']:.4f}")

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    out_path = RESULTS_DIR / "multi_domain_results.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\nSaved: {out_path}")
    return results


# ================================================================
# Main
# ================================================================

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--device", default="cuda:0")
    parser.add_argument("--phase", choices=["all", "seeds", "generate", "features", "evaluate"],
                        default="all")
    args = parser.parse_args()

    device = torch.device(args.device)
    print(f"Device: {device}")
    print(f"Phase: {args.phase}")
    print()

    domain_features = {}

    if args.phase in ("all", "seeds"):
        tokenizer = AutoTokenizer.from_pretrained(
            GENERATOR_NAME, cache_dir=GENERATOR_MODEL, local_files_only=True)
        phase_seeds(tokenizer)
        del tokenizer

    if args.phase in ("all", "generate"):
        phase_generate(device)

    if args.phase in ("all", "features"):
        domain_features = phase_features(device)

    if args.phase in ("all", "evaluate"):
        phase_evaluate(domain_features if domain_features else None)


if __name__ == "__main__":
    main()
