"""
Multi-domain seeds experiment with temperature=0.7, top_p=0.9.
Reuses existing seeds, regenerates chains with new params.
"""

import json
import os
import signal
import sys
import time
import multiprocessing as mp
from collections import Counter
from pathlib import Path

import numpy as np
import pandas as pd
import torch
from scipy.stats import spearmanr
from sklearn.metrics import f1_score
from xgboost import XGBClassifier

signal.signal(signal.SIGHUP, signal.SIG_IGN)

SEED = 42
np.random.seed(SEED)
torch.manual_seed(SEED)

BASE_DIR = Path("/root/gen-depth-fingerprint")
DATA_DIR = BASE_DIR / "data"
EXP_DIR = BASE_DIR / "experiments" / "multi_domain"
GEN_DIR = EXP_DIR / "generations_t07"
GEN_DIR.mkdir(parents=True, exist_ok=True)

# Generation parameters - KEY CHANGE
TEMPERATURE = 0.7
TOP_P = 0.9

REFERENCE_MODEL = "/root/autodl-tmp/models/pythia-410m/models--EleutherAI--pythia-410m/snapshots/9879c9b5f8bea9051dcb0e68dff21493d67e9d4f"

GENERATORS = {
    "pythia-1b": {
        "path": "/root/autodl-tmp/models/pythia-1b/EleutherAI/pythia-1b",
        "device": "cuda:0",
    },
    "qwen3-1.7b": {
        "path": "/root/autodl-tmp/models/Qwen/Qwen3-1___7B-Base",
        "device": "cuda:1",
    },
    "mistral-7b": {
        "path": "/root/autodl-tmp/models/mistral-7b-v0.3",
        "device": "cuda:2",
    },
}

DOMAINS = ["news", "academic", "code"]
NUM_SEEDS = 200
MAX_DEPTH = 3
MAX_NEW_TOKENS = 200
FEATURES = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max",
            "tail_decay", "ttr", "hapax_ratio"]

XGB_PARAMS = dict(n_estimators=200, max_depth=6, learning_rate=0.1,
                  random_state=SEED, eval_metric="mlogloss",
                  use_label_encoder=False)

# t=1.0 baseline results for comparison
T10_RESULTS = {
    "news": {"binary_f1": 0.7459},
    "academic": {"binary_f1": 0.7386},
    "code": {"binary_f1": 0.7535},
}


# ================================================================
# Phase 2: Generation (parallel across GPUs)
# ================================================================

def _generate_for_model(gen_name, gen_cfg, seed_paths):
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer

    signal.signal(signal.SIGHUP, signal.SIG_IGN)
    torch.manual_seed(SEED + hash(gen_name) % 1000)

    device = gen_cfg["device"]

    print(f"  [{gen_name}] Loading model on {device}...")
    print(f"  [{gen_name}] Generation params: temperature={TEMPERATURE}, top_p={TOP_P}")
    tokenizer = AutoTokenizer.from_pretrained(gen_cfg["path"], local_files_only=True)
    model = AutoModelForCausalLM.from_pretrained(
        gen_cfg["path"], local_files_only=True, torch_dtype=torch.float16
    ).to(device).eval()
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    print(f"  [{gen_name}] Model loaded")

    for domain in DOMAINS:
        out_path = GEN_DIR / f"{gen_name}_{domain}.jsonl"
        expected = NUM_SEEDS * (MAX_DEPTH + 1)

        done_seeds = set()
        if out_path.exists():
            with open(out_path) as f:
                for line in f:
                    rec = json.loads(line)
                    done_seeds.add(rec["seed_id"])
            if len(done_seeds) >= NUM_SEEDS:
                print(f"  [{gen_name}][{domain}] Already complete ({len(done_seeds)} seeds)")
                continue

        print(f"  [{gen_name}][{domain}] Generating (done: {len(done_seeds)}/{NUM_SEEDS})...")

        seeds = []
        with open(seed_paths[domain]) as f:
            for line in f:
                seeds.append(json.loads(line))

        with open(out_path, "a") as fout:
            for seed_idx, seed_item in enumerate(seeds):
                if seed_idx in done_seeds:
                    continue

                current_text = seed_item["text"]

                rec = {
                    "seed_id": seed_idx,
                    "depth": 0,
                    "text": current_text,
                    "generator": gen_name,
                    "domain": domain,
                }
                fout.write(json.dumps(rec, ensure_ascii=False) + "\n")

                for d in range(1, MAX_DEPTH + 1):
                    prompt = f"Continue the following text:\n\n{current_text}"
                    input_ids = tokenizer.encode(prompt, add_special_tokens=False)
                    input_ids = input_ids[-512:]
                    input_tensor = torch.tensor([input_ids], device=device)

                    with torch.no_grad():
                        output = model.generate(
                            input_tensor,
                            max_new_tokens=MAX_NEW_TOKENS,
                            temperature=TEMPERATURE,
                            top_p=TOP_P,
                            do_sample=True,
                            pad_token_id=tokenizer.pad_token_id,
                        )

                    new_tokens = output[0][len(input_ids):]
                    generated = tokenizer.decode(new_tokens, skip_special_tokens=True)

                    rec = {
                        "seed_id": seed_idx,
                        "depth": d,
                        "text": generated,
                        "generator": gen_name,
                        "domain": domain,
                    }
                    fout.write(json.dumps(rec, ensure_ascii=False) + "\n")
                    current_text = generated

                if (seed_idx + 1) % 20 == 0:
                    fout.flush()
                    print(f"  [{gen_name}][{domain}] {seed_idx + 1}/{len(seeds)} seeds")

        total = sum(1 for _ in open(out_path))
        print(f"  [{gen_name}][{domain}] Done: {total} records")

    del model, tokenizer
    torch.cuda.empty_cache()
    print(f"  [{gen_name}] Complete, GPU freed")


def generate_chains_parallel(seed_paths):
    print("\n" + "=" * 60)
    print(f"PHASE 2: Generating Depth Chains (temperature={TEMPERATURE}, top_p={TOP_P})")
    print("=" * 60)

    all_done = all(
        (GEN_DIR / f"{gn}_{d}.jsonl").exists() and
        sum(1 for _ in open(GEN_DIR / f"{gn}_{d}.jsonl")) >= NUM_SEEDS * (MAX_DEPTH + 1)
        for gn in GENERATORS for d in DOMAINS
    )
    if all_done:
        print("  All generations already complete!")
        return

    processes = []
    mp.set_start_method("spawn", force=True)
    for gen_name, gen_cfg in GENERATORS.items():
        p = mp.Process(target=_generate_for_model,
                       args=(gen_name, gen_cfg, seed_paths))
        p.start()
        processes.append((gen_name, p))
        print(f"  Started {gen_name} (PID {p.pid})")

    for gen_name, p in processes:
        p.join()
        print(f"  {gen_name} finished (exit code: {p.exitcode})")


# ================================================================
# Phase 3: Feature Extraction
# ================================================================

def extract_features():
    print("\n" + "=" * 60)
    print("PHASE 3: Feature Extraction (Pythia-410M)")
    print("=" * 60)

    feat_path = EXP_DIR / "features_t07.csv"
    if feat_path.exists():
        df = pd.read_csv(feat_path)
        print(f"  Features already extracted: {len(df)} records")
        return df

    from transformers import AutoModelForCausalLM, AutoTokenizer

    print(f"  Loading reference model...")
    ref_tokenizer = AutoTokenizer.from_pretrained(REFERENCE_MODEL, local_files_only=True)
    ref_model = AutoModelForCausalLM.from_pretrained(
        REFERENCE_MODEL, local_files_only=True, torch_dtype=torch.float16
    ).to("cuda:0").eval()
    if ref_tokenizer.pad_token is None:
        ref_tokenizer.pad_token = ref_tokenizer.eos_token
    print(f"  Reference model loaded on cuda:0")

    all_records = []
    for gen_name in GENERATORS:
        for domain in DOMAINS:
            fpath = GEN_DIR / f"{gen_name}_{domain}.jsonl"
            if not fpath.exists():
                print(f"  WARNING: Missing {fpath}")
                continue
            with open(fpath) as f:
                for line in f:
                    line = line.strip()
                    if line:
                        all_records.append(json.loads(line))

    print(f"  Total records to process: {len(all_records)}")

    batch_size = 16
    all_features = []

    for start in range(0, len(all_records), batch_size):
        batch = all_records[start:start + batch_size]
        texts = [r["text"] for r in batch]

        valid_mask = [len(t.strip()) > 0 for t in texts]
        valid_texts = [t for t, v in zip(texts, valid_mask) if v]

        if valid_texts:
            ref_feats = _compute_ref_features(valid_texts, ref_tokenizer, ref_model, "cuda:0")
        else:
            ref_feats = []

        surf_feats = _compute_surface_features(texts)

        ref_idx = 0
        for i, rec in enumerate(batch):
            if valid_mask[i]:
                feat_row = {
                    "seed_id": rec["seed_id"],
                    "depth": rec["depth"],
                    "generator": rec["generator"],
                    "domain": rec["domain"],
                    **ref_feats[ref_idx],
                    **surf_feats[i],
                }
                ref_idx += 1
            else:
                feat_row = {
                    "seed_id": rec["seed_id"],
                    "depth": rec["depth"],
                    "generator": rec["generator"],
                    "domain": rec["domain"],
                    "entropy_mean": 0.0, "entropy_std": 0.0,
                    "entropy_min": 0.0, "entropy_max": 0.0,
                    "tail_decay": 0.0,
                    **surf_feats[i],
                }
            all_features.append(feat_row)

        if (start + batch_size) % 640 == 0 or start + batch_size >= len(all_records):
            print(f"    Processed {min(start + batch_size, len(all_records))}/{len(all_records)}")

    df = pd.DataFrame(all_features)
    df.to_csv(feat_path, index=False)
    print(f"  Saved features: {feat_path} ({len(df)} rows)")

    del ref_model, ref_tokenizer
    torch.cuda.empty_cache()
    return df


def _compute_ref_features(texts, tokenizer, model, device):
    results = []
    encodings = tokenizer(
        texts, return_tensors="pt", padding=True, truncation=True, max_length=512
    ).to(device)

    with torch.no_grad():
        outputs = model(**encodings)
        logits = outputs.logits

    for i in range(len(texts)):
        mask = encodings["attention_mask"][i].bool()
        seq_len = mask.sum().item()
        if seq_len < 2:
            results.append({
                "entropy_mean": 0.0, "entropy_std": 0.0,
                "entropy_min": 0.0, "entropy_max": 0.0,
                "tail_decay": 0.0,
            })
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

    return results


def _compute_surface_features(texts):
    results = []
    for text in texts:
        words = text.lower().split()
        n = len(words)
        if n == 0:
            results.append({"ttr": 0.0, "hapax_ratio": 0.0})
            continue
        counter = Counter(words)
        types = len(counter)
        hapax = sum(1 for w, c in counter.items() if c == 1)
        results.append({
            "ttr": types / n,
            "hapax_ratio": hapax / n,
        })
    return results


# ================================================================
# Phase 4: Evaluation (LOGO)
# ================================================================

def evaluate(df):
    print("\n" + "=" * 60)
    print("PHASE 4: LOGO Evaluation")
    print("=" * 60)

    generators_list = sorted(df["generator"].unique())
    print(f"  Generators: {generators_list}")
    print(f"  Domains: {sorted(df['domain'].unique())}")

    per_domain = {}
    for domain in DOMAINS:
        domain_df = df[df["domain"] == domain].copy()
        if len(domain_df) == 0:
            print(f"  [{domain}] No data, skipping")
            continue

        print(f"\n  --- {domain} (n={len(domain_df)}) ---")
        domain_results = _logo_eval_domain(domain_df, generators_list)
        domain_results["n_samples"] = len(domain_df)
        per_domain[domain] = domain_results

    # Overall averages
    binary_f1s = [per_domain[d]["binary_f1"] for d in DOMAINS if d in per_domain]
    threeclass_f1s = [per_domain[d]["3class_f1"] for d in DOMAINS if d in per_domain]
    overall = {
        "binary_f1": round(np.mean(binary_f1s), 4) if binary_f1s else 0.0,
        "3class_f1": round(np.mean(threeclass_f1s), 4) if threeclass_f1s else 0.0,
    }

    # Comparison with t=1.0
    comparison = {}
    for domain in DOMAINS:
        if domain in per_domain and domain.lower() in T10_RESULTS:
            t07_val = per_domain[domain]["binary_f1"]
            t10_val = T10_RESULTS[domain.lower()]["binary_f1"]
            comparison[domain] = {
                "t07": t07_val,
                "t10": t10_val,
                "delta": round(t07_val - t10_val, 4),
            }

    results = {
        "experiment": "multi_domain_t07",
        "generation_params": {"temperature": TEMPERATURE, "top_p": TOP_P},
        "per_domain": per_domain,
        "overall": overall,
        "comparison_with_t10": comparison,
    }

    out_path = EXP_DIR / "multi_domain_results_t07.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\n  Results saved: {out_path}")
    print(f"\n=== COMPARISON t=0.7 vs t=1.0 ===")
    for domain, comp in comparison.items():
        print(f"  {domain}: t07={comp['t07']:.4f}, t10={comp['t10']:.4f}, delta={comp['delta']:+.4f}")
    print(f"  Overall binary F1: {overall['binary_f1']:.4f}")

    return results


def _logo_eval_domain(domain_df, generators_list):
    domain_df = domain_df.copy()
    domain_df["label_3c"] = domain_df["depth"].map({0: 0, 1: 1, 2: 2, 3: 2})

    binary_df = domain_df[domain_df["depth"] > 0].copy()
    binary_df["label_bin"] = (binary_df["depth"] >= 2).astype(int)

    # LOGO 3-class
    yt_3c_all, yp_3c_all = [], []
    per_gen_3c = {}
    for held_out in generators_list:
        tr = domain_df[domain_df["generator"] != held_out]
        te = domain_df[domain_df["generator"] == held_out]
        if len(te) == 0 or len(tr) == 0:
            continue

        # Class-balanced downsampling
        tr_balanced = _balance_classes(tr, "label_3c")

        clf = XGBClassifier(**XGB_PARAMS)
        clf.fit(tr_balanced[FEATURES].values, tr_balanced["label_3c"].values)
        yp = clf.predict(te[FEATURES].values)
        yt = te["label_3c"].values
        per_gen_3c[held_out] = round(float(f1_score(yt, yp, average="macro")), 4)
        yt_3c_all.append(yt)
        yp_3c_all.append(yp)

    yt_3c = np.concatenate(yt_3c_all) if yt_3c_all else np.array([])
    yp_3c = np.concatenate(yp_3c_all) if yp_3c_all else np.array([])
    multiclass_f1 = float(f1_score(yt_3c, yp_3c, average="macro")) if len(yt_3c) > 0 else 0.0

    # LOGO binary
    yt_bin_all, yp_bin_all = [], []
    per_gen_bin = {}
    for held_out in generators_list:
        tr = binary_df[binary_df["generator"] != held_out]
        te = binary_df[binary_df["generator"] == held_out]
        if len(te) == 0 or len(tr) == 0:
            continue

        # Class-balanced downsampling
        tr_balanced = _balance_classes(tr, "label_bin")

        clf = XGBClassifier(**XGB_PARAMS)
        clf.fit(tr_balanced[FEATURES].values, tr_balanced["label_bin"].values)
        yp = clf.predict(te[FEATURES].values)
        yt = te["label_bin"].values
        per_gen_bin[held_out] = round(float(f1_score(yt, yp, average="binary")), 4)
        yt_bin_all.append(yt)
        yp_bin_all.append(yp)

    yt_bin = np.concatenate(yt_bin_all) if yt_bin_all else np.array([])
    yp_bin = np.concatenate(yp_bin_all) if yp_bin_all else np.array([])
    binary_f1 = float(f1_score(yt_bin, yp_bin, average="binary")) if len(yt_bin) > 0 else 0.0

    binary_ci = _bootstrap_ci(yt_bin, yp_bin, metric="binary")
    multiclass_ci = _bootstrap_ci(yt_3c, yp_3c, metric="macro")

    print(f"    Binary F1: {binary_f1:.4f} CI: {binary_ci}")
    print(f"    3-class F1: {multiclass_f1:.4f} CI: {multiclass_ci}")
    print(f"    Per-generator (bin): {per_gen_bin}")
    print(f"    Per-generator (3c): {per_gen_3c}")

    return {
        "binary_f1": round(binary_f1, 4),
        "binary_ci": binary_ci,
        "3class_f1": round(multiclass_f1, 4),
        "3class_ci": multiclass_ci,
        "per_generator_binary": per_gen_bin,
        "per_generator_3class": per_gen_3c,
    }


def _balance_classes(df, label_col):
    counts = df[label_col].value_counts()
    min_count = counts.min()
    balanced = pd.concat([
        group.sample(n=min_count, random_state=SEED)
        for _, group in df.groupby(label_col)
    ])
    return balanced.sample(frac=1, random_state=SEED).reset_index(drop=True)


def _bootstrap_ci(y_true, y_pred, metric="binary", n_boot=1000, alpha=0.05):
    if len(y_true) == 0:
        return [0.0, 0.0]
    rng = np.random.RandomState(SEED)
    scores = []
    n = len(y_true)
    for _ in range(n_boot):
        idx = rng.randint(0, n, size=n)
        yt_b = y_true[idx]
        yp_b = y_pred[idx]
        if len(np.unique(yt_b)) < 2:
            continue
        scores.append(f1_score(yt_b, yp_b, average=metric))
    if not scores:
        return [0.0, 0.0]
    lo = float(np.percentile(scores, 100 * alpha / 2))
    hi = float(np.percentile(scores, 100 * (1 - alpha / 2)))
    return [round(lo, 4), round(hi, 4)]


# ================================================================
# Main
# ================================================================

def main():
    t0 = time.time()
    print(f"Multi-domain seeds experiment (t={TEMPERATURE}, top_p={TOP_P})")
    print(f"Generators: {list(GENERATORS.keys())}")
    print(f"Domains: {DOMAINS}")
    print(f"Seeds/domain: {NUM_SEEDS}, Max depth: {MAX_DEPTH}")
    print(f"Output dir: {GEN_DIR}")
    print()

    seed_paths = {
        "news": EXP_DIR / "seeds_news.jsonl",
        "academic": EXP_DIR / "seeds_academic.jsonl",
        "code": EXP_DIR / "seeds_code.jsonl",
    }

    for domain, path in seed_paths.items():
        assert path.exists(), f"Seed file missing: {path}"
        n = sum(1 for _ in open(path))
        print(f"  [{domain}] {n} seeds available")

    generate_chains_parallel(seed_paths)
    df = extract_features()
    results = evaluate(df)

    elapsed = time.time() - t0
    print(f"\n{'=' * 60}")
    print(f"COMPLETE in {elapsed/3600:.1f}h ({elapsed/60:.0f}min)")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
