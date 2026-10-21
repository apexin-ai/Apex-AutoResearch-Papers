"""
Multi-domain seeds experiment.
Validates depth fingerprint is not a Wikipedia artifact by replicating
depth signal across news, academic, and code domains with 3 generators.
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
EXP_DIR.mkdir(parents=True, exist_ok=True)

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


# ================================================================
# Phase 1: Seed Preparation
# ================================================================

def prepare_seeds():
    print("=" * 60)
    print("PHASE 1: Preparing Seeds")
    print("=" * 60)

    seed_paths = {}

    # News
    news_path = EXP_DIR / "seeds_news.jsonl"
    if not news_path.exists():
        src = DATA_DIR / "seeds" / "news_seed_500.jsonl"
        print("  [news] Reusing existing CNN DailyMail seeds (first 200)")
        records = []
        with open(src) as f:
            for i, line in enumerate(f):
                if i >= NUM_SEEDS:
                    break
                item = json.loads(line)
                records.append({"text": item["text"], "source": "cnn_dailymail", "domain": "news"})
        with open(news_path, "w") as f:
            for r in records:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        print(f"    Saved {len(records)} seeds")
    else:
        print(f"  [news] Already exists")
    seed_paths["news"] = news_path

    # Academic
    academic_path = EXP_DIR / "seeds_academic.jsonl"
    if not academic_path.exists():
        src = DATA_DIR / "seeds" / "scientific_seed_500.jsonl"
        print("  [academic] Reusing existing arXiv seeds (first 200)")
        records = []
        with open(src) as f:
            for i, line in enumerate(f):
                if i >= NUM_SEEDS:
                    break
                item = json.loads(line)
                records.append({"text": item["text"], "source": "arxiv", "domain": "academic"})
        with open(academic_path, "w") as f:
            for r in records:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        print(f"    Saved {len(records)} seeds")
    else:
        print(f"  [academic] Already exists")
    seed_paths["academic"] = academic_path

    # Code documentation (from Python stdlib, deduplicated)
    code_path = EXP_DIR / "seeds_code.jsonl"
    if not code_path.exists():
        print("  [code] Generating from Python stdlib docstrings (deduplicated)...")
        records = _prepare_code_seeds_dedup()
        with open(code_path, "w") as f:
            for r in records:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        print(f"    Saved {len(records)} seeds")
    else:
        print(f"  [code] Already exists")
    seed_paths["code"] = code_path

    for domain, path in seed_paths.items():
        count = sum(1 for _ in open(path))
        print(f"  {domain}: {count} seeds")

    return seed_paths


def _prepare_code_seeds_dedup():
    """Generate unique code documentation seeds from Python stdlib."""
    import importlib
    import inspect

    seen_texts = set()
    records = []

    modules_to_try = [
        "os", "sys", "json", "re", "collections", "itertools", "functools",
        "pathlib", "subprocess", "threading", "multiprocessing", "socket",
        "http", "urllib", "email", "logging", "unittest", "typing",
        "dataclasses", "abc", "contextlib", "io", "struct", "hashlib",
        "hmac", "secrets", "os.path", "shutil", "tempfile", "glob",
        "fnmatch", "stat", "filecmp", "sqlite3", "csv", "configparser",
        "argparse", "getopt", "warnings", "traceback", "gc", "inspect",
        "dis", "ast", "compileall", "pdb", "profile", "timeit",
        "pickle", "shelve", "marshal", "copy", "pprint", "textwrap",
        "unicodedata", "string", "difflib", "enum", "numbers", "math",
        "cmath", "decimal", "fractions", "random", "statistics",
        "datetime", "calendar", "time", "array", "queue", "heapq",
        "bisect", "weakref", "types", "operator", "keyword", "token",
        "tokenize", "codecs", "encodings", "html", "xml",
        "urllib.parse", "urllib.request", "http.client", "http.server",
        "ftplib", "smtplib", "imaplib", "poplib", "telnetlib",
        "xmlrpc", "zipfile", "tarfile", "gzip", "bz2", "lzma",
        "zipimport", "pkgutil", "importlib", "platform", "ctypes",
        "select", "selectors", "signal", "mmap", "sysconfig",
    ]

    for mod_name in modules_to_try:
        if len(records) >= NUM_SEEDS:
            break
        try:
            mod = importlib.import_module(mod_name)
        except Exception:
            continue

        # Module docstring
        doc = inspect.getdoc(mod)
        if doc and len(doc.split()) >= 60:
            key = doc[:200]
            if key not in seen_texts:
                seen_texts.add(key)
                words = doc.split()[:180]
                records.append({
                    "text": " ".join(words),
                    "source": f"stdlib_{mod_name}",
                    "domain": "code"
                })

        # Class and function docstrings
        for name, obj in inspect.getmembers(mod):
            if len(records) >= NUM_SEEDS:
                break
            if name.startswith("_"):
                continue
            # Skip basic types whose docstring is generic
            if isinstance(obj, type) and obj in (int, str, float, bytes, list, dict, tuple, set, bool):
                continue
            try:
                doc = inspect.getdoc(obj)
            except Exception:
                continue
            if not doc or len(doc.split()) < 60:
                continue
            key = doc[:200]
            if key in seen_texts:
                continue
            seen_texts.add(key)
            words = doc.split()[:180]
            records.append({
                "text": " ".join(words),
                "source": f"stdlib_{mod_name}.{name}",
                "domain": "code"
            })

    print(f"    Generated {len(records)} unique code documentation seeds")
    return records[:NUM_SEEDS]


# ================================================================
# Phase 2: Generation (parallel across GPUs)
# ================================================================

def _generate_for_model(gen_name, gen_cfg, seed_paths):
    """Generate chains for one model across all domains. Runs in subprocess."""
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer

    signal.signal(signal.SIGHUP, signal.SIG_IGN)
    torch.manual_seed(SEED + hash(gen_name) % 1000)

    device = gen_cfg["device"]
    gen_dir = EXP_DIR / "generations"
    gen_dir.mkdir(exist_ok=True)

    print(f"  [{gen_name}] Loading model on {device}...")
    tokenizer = AutoTokenizer.from_pretrained(gen_cfg["path"], local_files_only=True)
    model = AutoModelForCausalLM.from_pretrained(
        gen_cfg["path"], local_files_only=True, torch_dtype=torch.float16
    ).to(device).eval()
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    print(f"  [{gen_name}] Model loaded")

    for domain in DOMAINS:
        out_path = gen_dir / f"{gen_name}_{domain}.jsonl"
        expected = NUM_SEEDS * (MAX_DEPTH + 1)

        # Check existing progress
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

                # depth 0 = seed
                rec = {
                    "seed_id": seed_idx,
                    "depth": 0,
                    "text": current_text,
                    "generator": gen_name,
                    "domain": domain,
                }
                fout.write(json.dumps(rec, ensure_ascii=False) + "\n")

                # depth 1-3
                for d in range(1, MAX_DEPTH + 1):
                    prompt = f"Continue the following text:\n\n{current_text}"
                    input_ids = tokenizer.encode(prompt, add_special_tokens=False)
                    input_ids = input_ids[-512:]
                    input_tensor = torch.tensor([input_ids], device=device)

                    with torch.no_grad():
                        output = model.generate(
                            input_tensor,
                            max_new_tokens=MAX_NEW_TOKENS,
                            temperature=1.0,
                            top_p=1.0,
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
    print("PHASE 2: Generating Depth Chains (parallel)")
    print("=" * 60)

    gen_dir = EXP_DIR / "generations"
    gen_dir.mkdir(exist_ok=True)

    # Check if all already done
    all_done = all(
        (gen_dir / f"{gn}_{d}.jsonl").exists() and
        sum(1 for _ in open(gen_dir / f"{gn}_{d}.jsonl")) >= NUM_SEEDS * (MAX_DEPTH + 1)
        for gn in GENERATORS for d in DOMAINS
    )
    if all_done:
        print("  All generations already complete!")
        return

    # Launch parallel processes
    processes = []
    mp.set_start_method("spawn", force=True)
    for gen_name, gen_cfg in GENERATORS.items():
        p = mp.Process(target=_generate_for_model,
                       args=(gen_name, gen_cfg, seed_paths))
        p.start()
        processes.append((gen_name, p))
        print(f"  Started {gen_name} (PID {p.pid})")

    # Wait for all
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

    feat_path = EXP_DIR / "features.csv"
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

    gen_dir = EXP_DIR / "generations"
    all_records = []

    for gen_name in GENERATORS:
        for domain in DOMAINS:
            fpath = gen_dir / f"{gen_name}_{domain}.jsonl"
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

        # Filter empty texts
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

    results = {
        "experiment": "multi-domain-seeds",
        "generators": list(GENERATORS.keys()),
        "domains": {},
        "cross_domain_summary": {},
        "feature_analysis": {},
    }

    generators_list = sorted(df["generator"].unique())
    print(f"  Generators: {generators_list}")
    print(f"  Domains: {sorted(df['domain'].unique())}")

    for domain in DOMAINS:
        domain_df = df[df["domain"] == domain].copy()
        if len(domain_df) == 0:
            print(f"  [{domain}] No data, skipping")
            continue

        print(f"\n  --- {domain} (n={len(domain_df)}) ---")
        domain_results = _logo_eval_domain(domain_df, generators_list)
        domain_results["n_seeds"] = NUM_SEEDS
        domain_results["n_samples_total"] = len(domain_df)
        results["domains"][domain] = domain_results

    # Wikipedia baseline
    wiki_baseline = _compute_wiki_baseline()
    if wiki_baseline:
        results["domains"]["wikipedia_baseline"] = wiki_baseline

    # Cross-domain summary
    domain_f1s = {d: results["domains"][d]["binary_f1"]
                  for d in DOMAINS if d in results["domains"]}
    if domain_f1s:
        worst = min(domain_f1s, key=domain_f1s.get)
        best = max(domain_f1s, key=domain_f1s.get)
        wiki_f1 = wiki_baseline.get("binary_f1", 0) if wiki_baseline else 0
        max_gap = max(abs(v - wiki_f1) for v in domain_f1s.values()) if wiki_f1 > 0 else 0

        all_above = all(v >= 0.55 for v in domain_f1s.values())
        gap_small = max_gap < 0.15
        conclusion = "domain_independent" if (all_above and gap_small) else "domain_dependent"

        results["cross_domain_summary"] = {
            "worst_domain": worst,
            "worst_f1": round(domain_f1s[worst], 4),
            "best_domain": best,
            "best_f1": round(domain_f1s[best], 4),
            "max_gap_vs_wiki": round(max_gap, 4),
            "conclusion": conclusion,
        }

    # Feature analysis
    results["feature_analysis"] = _feature_analysis(df)

    out_path = EXP_DIR / "multi_domain_results.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\n  Results saved: {out_path}")
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
        clf = XGBClassifier(**XGB_PARAMS)
        clf.fit(tr[FEATURES].values, tr["label_3c"].values)
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
        clf = XGBClassifier(**XGB_PARAMS)
        clf.fit(tr[FEATURES].values, tr["label_bin"].values)
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
    print(f"    Per-generator (3c): {per_gen_3c}")

    return {
        "binary_f1": round(binary_f1, 4),
        "binary_ci": binary_ci,
        "multiclass_f1": round(multiclass_f1, 4),
        "multiclass_ci": multiclass_ci,
        "per_generator": {
            "binary": per_gen_bin,
            "multiclass": per_gen_3c,
        },
    }


def _bootstrap_ci(yt, yp, metric="binary", n_boot=1000, alpha=0.05):
    if len(yt) == 0:
        return [0.0, 0.0]
    rng = np.random.RandomState(SEED)
    scores = []
    for _ in range(n_boot):
        idx = rng.choice(len(yt), size=len(yt), replace=True)
        if metric == "binary":
            s = f1_score(yt[idx], yp[idx], average="binary", zero_division=0)
        else:
            s = f1_score(yt[idx], yp[idx], average="macro", zero_division=0)
        scores.append(s)
    lo = float(np.percentile(scores, 100 * alpha / 2))
    hi = float(np.percentile(scores, 100 * (1 - alpha / 2)))
    return [round(lo, 4), round(hi, 4)]


def _compute_wiki_baseline():
    feat_path = DATA_DIR / "features_all.csv"
    if not feat_path.exists():
        feat_path = DATA_DIR / "features.csv"
    if not feat_path.exists():
        print("  [wiki baseline] No Wikipedia features found")
        return None

    try:
        wiki_df = pd.read_csv(feat_path)
        if "depth" not in wiki_df.columns:
            return None

        wiki_df["label_3c"] = wiki_df["depth"].map({0: 0, 1: 1, 2: 2, 3: 2, 4: 2})

        from sklearn.model_selection import StratifiedKFold
        skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=SEED)

        X = wiki_df[FEATURES].values
        y3 = wiki_df["label_3c"].values
        yp_3c = np.zeros_like(y3)
        for tr_idx, te_idx in skf.split(X, y3):
            clf = XGBClassifier(**XGB_PARAMS)
            clf.fit(X[tr_idx], y3[tr_idx])
            yp_3c[te_idx] = clf.predict(X[te_idx])
        multiclass_f1 = float(f1_score(y3, yp_3c, average="macro"))

        bin_mask = wiki_df["depth"] > 0
        X_bin = wiki_df.loc[bin_mask, FEATURES].values
        y_bin = (wiki_df.loc[bin_mask, "depth"] >= 2).astype(int).values
        yp_bin = np.zeros_like(y_bin)
        skf2 = StratifiedKFold(n_splits=5, shuffle=True, random_state=SEED)
        for tr_idx, te_idx in skf2.split(X_bin, y_bin):
            clf = XGBClassifier(**XGB_PARAMS)
            clf.fit(X_bin[tr_idx], y_bin[tr_idx])
            yp_bin[te_idx] = clf.predict(X_bin[te_idx])
        binary_f1 = float(f1_score(y_bin, yp_bin, average="binary"))

        print(f"  [wiki baseline] Binary F1: {binary_f1:.4f}, 3-class F1: {multiclass_f1:.4f}")
        n_seeds = wiki_df["seed_id"].nunique() if "seed_id" in wiki_df.columns else len(wiki_df) // 5

        return {
            "n_seeds": int(n_seeds),
            "binary_f1": round(binary_f1, 4),
            "multiclass_f1": round(multiclass_f1, 4),
        }
    except Exception as e:
        print(f"  [wiki baseline] Error: {e}")
        return None


def _feature_analysis(df):
    per_domain_means = {}
    for domain in df["domain"].unique():
        ddf = df[df["domain"] == domain]
        means = {}
        for feat in FEATURES:
            means[feat] = round(float(ddf[feat].mean()), 6)
        per_domain_means[domain] = means

    overall_means = {feat: float(df[feat].mean()) for feat in FEATURES}
    max_shift_domain = None
    max_shift_val = 0
    for domain, means in per_domain_means.items():
        shift = sum(abs(means[f] - overall_means[f]) for f in FEATURES)
        if shift > max_shift_val:
            max_shift_val = shift
            max_shift_domain = domain

    return {
        "per_domain_feature_means": per_domain_means,
        "domain_with_largest_shift": max_shift_domain,
    }


# ================================================================
# Main
# ================================================================

def main():
    t0 = time.time()
    print(f"Multi-domain seeds experiment")
    print(f"Generators: {list(GENERATORS.keys())}")
    print(f"Domains: {DOMAINS}")
    print(f"Seeds/domain: {NUM_SEEDS}, Max depth: {MAX_DEPTH}")
    print()

    seed_paths = prepare_seeds()
    generate_chains_parallel(seed_paths)
    df = extract_features()
    results = evaluate(df)

    elapsed = time.time() - t0
    print(f"\n{'=' * 60}")
    print(f"COMPLETE in {elapsed/3600:.1f}h ({elapsed/60:.0f}min)")
    print(f"{'=' * 60}")

    print("\n=== SUMMARY ===")
    for domain, dres in results.get("domains", {}).items():
        bf1 = dres.get("binary_f1", "N/A")
        mf1 = dres.get("multiclass_f1", "N/A")
        print(f"  {domain}: binary_f1={bf1}, 3class_f1={mf1}")
    cs = results.get("cross_domain_summary", {})
    if cs:
        print(f"  Conclusion: {cs.get('conclusion')}")
        print(f"  Max gap vs wiki: {cs.get('max_gap_vs_wiki')}")


if __name__ == "__main__":
    main()
