"""
eval_8gen_sampling_ablation.py -- Sampling Strategy Ablation for Depth Signal Robustness

Tests whether depth signal is robust across different sampling configurations:
  low:     temperature=0.5, top_p=0.8
  default: temperature=0.7, top_p=0.9  (existing data, skip generation)
  high:    temperature=1.0, top_p=0.95

Pipeline: generate chains -> extract features -> LOGO evaluation
Output:   results/sampling_ablation.json
"""

import argparse
import json
import os
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

SEED = 42

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = Path(os.path.join(ROOT, "..", "data"))
RESULTS_DIR = Path(os.path.join(ROOT, "results"))
SEED_FILE = DATA_DIR / "wiki_seed_1000.jsonl"

# These must be set to local model paths before running generation phases.
# Only the evaluate phase can run without models.
GENERATOR_MODEL = os.environ.get("GENERATOR_MODEL", "Qwen/Qwen3-1.7B-Base")
REFERENCE_MODEL = os.environ.get("REFERENCE_MODEL", "EleutherAI/pythia-410m")

CONFIGS = {
    "low_t05_p08":     {"temperature": 0.5, "top_p": 0.8,  "dir": "qwen3-1.7b-low-temp"},
    "default_t07_p09": {"temperature": 0.7, "top_p": 0.9,  "dir": "qwen3-1.7b"},
    "high_t10_p095":   {"temperature": 1.0, "top_p": 0.95, "dir": "qwen3-1.7b-high-temp"},
}

FEATURES = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max",
            "tail_decay", "ttr", "hapax_ratio"]
CLASS_MAP = {0: 0, 1: 1, 2: 2, 3: 2, 4: 2}
XGB_PARAMS = dict(n_estimators=200, max_depth=6, learning_rate=0.1,
                  random_state=SEED, eval_metric="mlogloss",
                  use_label_encoder=False)
MAX_DEPTH = 4
NUM_DEPTHS = MAX_DEPTH + 1


# ================================================================
# Phase 1: Generation
# ================================================================

def load_seeds(path, tokenizer, max_tokens=256):
    seeds = []
    with open(path) as f:
        for line_num, line in enumerate(f):
            item = json.loads(line)
            text = item.get("text", "")
            if len(text.strip()) < 100:
                continue
            token_ids = tokenizer.encode(text, add_special_tokens=False)[:max_tokens]
            if len(token_ids) < 64:
                continue
            seeds.append({"seed_id": line_num, "text": tokenizer.decode(token_ids)})
    return seeds


def generate_continuation(model, tokenizer, text, device,
                          max_new_tokens=256, prompt_tokens=128,
                          temperature=0.7, top_p=0.9):
    input_ids = tokenizer.encode(text, add_special_tokens=False)
    if len(input_ids) == 0:
        return ""
    input_ids = input_ids[-prompt_tokens:]
    input_tensor = torch.tensor([input_ids], device=device)

    with torch.no_grad():
        output = model.generate(
            input_tensor,
            max_new_tokens=max_new_tokens,
            temperature=temperature,
            top_p=top_p,
            do_sample=True,
            pad_token_id=tokenizer.pad_token_id,
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


def run_generation(config_name, config, seeds, gen_model, gen_tokenizer, device):
    output_dir = DATA_DIR / config["dir"]
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "generations_shard0.jsonl"

    done_seeds = load_done_seeds(output_path)
    remaining = [s for s in seeds if s["seed_id"] not in done_seeds]

    if not remaining:
        print(f"  [{config_name}] All {len(seeds)} seeds done, skipping")
        return

    print(f"  [{config_name}] {len(done_seeds)} done, {len(remaining)} remaining")

    t0 = time.time()
    record_count = 0

    with open(output_path, "a") as f:
        for i, seed_info in enumerate(tqdm(remaining, desc=config_name)):
            seed_id = seed_info["seed_id"]
            seed_text = seed_info["text"]
            base_id = seed_id * NUM_DEPTHS

            gen0_tokens = gen_tokenizer.encode(seed_text, add_special_tokens=False)
            f.write(json.dumps({
                "id": base_id, "depth": 0, "text": seed_text,
                "seed_id": seed_id, "token_count": len(gen0_tokens),
                "model": "qwen3-1.7b",
            }, ensure_ascii=False) + "\n")
            f.flush()
            record_count += 1

            prev_text = seed_text
            for depth in range(1, NUM_DEPTHS):
                check_ids = gen_tokenizer.encode(prev_text, add_special_tokens=False)
                if len(check_ids) == 0 or len(prev_text.strip()) < 10:
                    print(f"  WARN: seed {seed_id} depth {depth}: empty input, skipping rest")
                    break

                continuation = generate_continuation(
                    gen_model, gen_tokenizer, prev_text, device,
                    temperature=config["temperature"], top_p=config["top_p"],
                )
                if not continuation or len(continuation.strip()) == 0:
                    print(f"  WARN: seed {seed_id} depth {depth}: empty output, skipping rest")
                    break

                cont_tokens = gen_tokenizer.encode(continuation, add_special_tokens=False)
                f.write(json.dumps({
                    "id": base_id + depth, "depth": depth, "text": continuation,
                    "seed_id": seed_id, "token_count": len(cont_tokens),
                    "model": "qwen3-1.7b",
                }, ensure_ascii=False) + "\n")
                f.flush()
                record_count += 1
                prev_text = continuation

            if (i + 1) % 50 == 0:
                elapsed = time.time() - t0
                rate = (i + 1) / elapsed
                print(f"  [{i+1}/{len(remaining)}] {elapsed:.0f}s, {rate:.2f} seeds/s")

    elapsed = time.time() - t0
    print(f"  [{config_name}] {record_count} records in {elapsed:.1f}s")


def phase_generate(device):
    print("=" * 60)
    print("PHASE 1: Generation (low + high)")
    print("=" * 60)

    print("Loading generator model...")
    gen_tokenizer = AutoTokenizer.from_pretrained(
        GENERATOR_MODEL, trust_remote_code=True)
    gen_model = AutoModelForCausalLM.from_pretrained(
        GENERATOR_MODEL, dtype=torch.float16, trust_remote_code=True
    ).to(device)
    gen_model.eval()
    if gen_tokenizer.pad_token is None:
        gen_tokenizer.pad_token = gen_tokenizer.eos_token
    print(f"Model on {device}")

    seeds = load_seeds(SEED_FILE, gen_tokenizer)
    print(f"Loaded {len(seeds)} seeds")

    for cfg_name in ["low_t05_p08", "high_t10_p095"]:
        cfg = CONFIGS[cfg_name]
        print(f"\n--- {cfg_name}: T={cfg['temperature']}, p={cfg['top_p']} ---")
        torch.manual_seed(SEED)
        torch.cuda.manual_seed(SEED)
        run_generation(cfg_name, cfg, seeds, gen_model, gen_tokenizer, device)

    del gen_model, gen_tokenizer
    torch.cuda.empty_cache()
    print("\nGeneration complete\n")


# ================================================================
# Phase 2: Feature Extraction
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


def extract_features_for_config(config_name, config, ref_tokenizer, ref_model, device):
    feat_path = DATA_DIR / f"features_{config['dir']}.csv"

    if feat_path.exists():
        df = pd.read_csv(feat_path)
        print(f"  [{config_name}] Features exist: {feat_path} ({len(df)} rows)")
        return df

    data_dir = DATA_DIR / config["dir"]
    records = load_generation_records(data_dir)
    print(f"  [{config_name}] {len(records)} records loaded")

    texts = [r["text"] for r in records]
    print(f"  [{config_name}] Computing reference features...")
    ref_feats = compute_reference_features(texts, ref_tokenizer, ref_model, device)
    surf_feats = compute_surface_features(texts)

    rows = []
    for rec, ref, surf in zip(records, ref_feats, surf_feats):
        rows.append({
            "model_name": "qwen3-1.7b",
            "seed_id": rec["seed_id"],
            "depth": rec["depth"],
            **ref, **surf,
        })

    df = pd.DataFrame(rows)
    df.to_csv(feat_path, index=False)
    print(f"  [{config_name}] Saved: {feat_path} ({len(df)} rows)")
    return df


def phase_features(device):
    print("=" * 60)
    print("PHASE 2: Feature Extraction")
    print("=" * 60)

    print("Loading reference model...")
    ref_tokenizer = AutoTokenizer.from_pretrained(REFERENCE_MODEL)
    ref_model = AutoModelForCausalLM.from_pretrained(
        REFERENCE_MODEL, torch_dtype=torch.float16
    ).to(device).eval()
    if ref_tokenizer.pad_token is None:
        ref_tokenizer.pad_token = ref_tokenizer.eos_token
    print(f"Reference model on {device}")

    config_features = {}
    for cfg_name, cfg in CONFIGS.items():
        print(f"\n--- {cfg_name} ---")
        config_features[cfg_name] = extract_features_for_config(
            cfg_name, cfg, ref_tokenizer, ref_model, device)

    del ref_model, ref_tokenizer
    torch.cuda.empty_cache()
    print("\nFeature extraction complete\n")
    return config_features


# ================================================================
# Phase 3: LOGO Evaluation
# ================================================================

def downsample(df, rng):
    min_n = df["label"].value_counts().min()
    parts = [df[df["label"] == lbl].sample(n=min_n, random_state=rng, replace=False)
             for lbl in sorted(df["label"].unique())]
    return pd.concat(parts, ignore_index=True)


def run_logo(df, features=FEATURES):
    generators = sorted(df["model_name"].unique())
    yt_all, yp_all = [], []
    per_gen = {}

    for gen in generators:
        te = df[df["model_name"] == gen]
        tr = downsample(df[df["model_name"] != gen], np.random.RandomState(SEED))
        clf = XGBClassifier(**XGB_PARAMS)
        clf.fit(tr[features].values, tr["label"].values)
        yp = clf.predict(te[features].values)
        per_gen[gen] = round(float(f1_score(te["label"].values, yp, average="macro")), 4)
        yt_all.append(te["label"].values)
        yp_all.append(yp)

    yt = np.concatenate(yt_all)
    yp = np.concatenate(yp_all)
    macro_f1 = f1_score(yt, yp, average="macro")
    per_cls = f1_score(yt, yp, average=None, labels=[0, 1, 2])

    # Binary F1: gen-1 vs gen-2+ (exclude gen-0)
    mask = yt > 0
    if mask.sum() > 0:
        binary_yt = (yt[mask] > 1).astype(int)
        binary_yp = (yp[mask] > 1).astype(int)
        binary_f1 = f1_score(binary_yt, binary_yp, average="binary")
    else:
        binary_f1 = 0.0

    return {
        "3class_f1": round(float(macro_f1), 4),
        "binary_f1": round(float(binary_f1), 4),
        "per_class_f1": {
            "gen-0": round(float(per_cls[0]), 4),
            "gen-1": round(float(per_cls[1]), 4),
            "gen-2+": round(float(per_cls[2]), 4),
        },
        "per_generator": per_gen,
    }


def compute_spearman(df):
    corrs = {}
    for feat in FEATURES:
        rho, _ = spearmanr(df[feat].values, df["depth"].values)
        corrs[f"spearman_{feat}"] = round(float(rho), 4)
    return corrs


def phase_evaluate(config_features):
    print("=" * 60)
    print("PHASE 3: LOGO Evaluation")
    print("=" * 60)

    # Load base features (all generators except qwen3-1.7b)
    base_csv = DATA_DIR / "features_all_models.csv"
    base_df = pd.read_csv(base_csv)
    base_df["label"] = base_df["depth"].map(CLASS_MAP)
    base_no_qwen = base_df[base_df["model_name"] != "qwen3-1.7b"].copy()
    print(f"Base features: {len(base_no_qwen)} rows "
          f"({base_no_qwen['model_name'].nunique()} generators)")

    results = {"configs": {}}

    for cfg_name, cfg in CONFIGS.items():
        print(f"\n--- {cfg_name} ---")

        if cfg_name in config_features:
            cfg_df = config_features[cfg_name].copy()
        else:
            feat_path = DATA_DIR / f"features_{cfg['dir']}.csv"
            cfg_df = pd.read_csv(feat_path)

        cfg_df["label"] = cfg_df["depth"].map(CLASS_MAP)

        # For default config, use existing features from features_all_models.csv
        if cfg_name == "default_t07_p09":
            cfg_df = base_df[base_df["model_name"] == "qwen3-1.7b"].copy()

        combined = pd.concat([base_no_qwen, cfg_df], ignore_index=True)
        print(f"  Combined: {len(combined)} rows, "
              f"generators: {sorted(combined['model_name'].unique())}")

        logo = run_logo(combined)
        spearman = compute_spearman(cfg_df)

        results["configs"][cfg_name] = {**logo, **spearman}

        print(f"  3-class F1: {logo['3class_f1']:.4f}")
        print(f"  Binary F1:  {logo['binary_f1']:.4f}")
        print(f"  Per-gen:    {logo['per_generator']}")

    # Compute summary
    f1_values = [r["3class_f1"] for r in results["configs"].values()]
    f1_range = max(f1_values) - min(f1_values)
    results["f1_range"] = round(f1_range, 4)
    results["f1_range_pp"] = round(f1_range * 100, 2)
    results["robust"] = f1_range < 0.03

    binary_values = [r["binary_f1"] for r in results["configs"].values()]
    results["binary_f1_range"] = round(max(binary_values) - min(binary_values), 4)

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"{'Config':<20s} {'3class-F1':>10s} {'Binary-F1':>10s}")
    print("-" * 42)
    for cfg_name, r in results["configs"].items():
        print(f"{cfg_name:<20s} {r['3class_f1']:>10.4f} {r['binary_f1']:>10.4f}")
    print(f"\nF1 range: {results['f1_range_pp']:.2f}pp")
    print(f"Robust: {results['robust']}")

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    out_path = RESULTS_DIR / "sampling_ablation.json"
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
    parser.add_argument("--phase", choices=["all", "generate", "features", "evaluate"],
                        default="all")
    args = parser.parse_args()

    device = torch.device(args.device)
    print(f"Device: {device}")
    print(f"Phase: {args.phase}")
    print()

    config_features = {}

    if args.phase in ("all", "generate"):
        phase_generate(device)

    if args.phase in ("all", "features"):
        config_features = phase_features(device)

    if args.phase in ("all", "evaluate"):
        phase_evaluate(config_features)


if __name__ == "__main__":
    main()
