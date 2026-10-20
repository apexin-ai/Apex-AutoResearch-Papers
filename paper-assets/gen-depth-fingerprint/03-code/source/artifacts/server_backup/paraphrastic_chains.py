"""
paraphrastic_chains.py — plan_006: Paraphrastic vs continuation chain comparison.

Tests attractor convergence theory: do paraphrastic chains lose depth signal
faster than continuation chains? Builds parallel paraphrasing chains and
directly compares with plan_005 continuation data.

Phases:
  generate  — build paraphrastic chains (Pythia-2.8B, 1000 seeds × depth 0-4)
  extract   — 7-feature extraction with Pythia-410M reference model
  evaluate  — 3-class LOGO CV + head-to-head comparison vs continuation

Input:  data/wiki_seed_1000.jsonl
Output: data/pythia-2.8b-paraphrase/generations_shard0.jsonl
        data/paraphrase_features.csv
        results/plan006_paraphrastic_comparison.json
"""

import argparse
import glob
import json
import os
import signal
import sys
import time
from collections import Counter
from pathlib import Path

import numpy as np
import pandas as pd
import torch
from scipy.stats import spearmanr
from sklearn.metrics import f1_score
from sklearn.model_selection import StratifiedKFold
from transformers import AutoModelForCausalLM, AutoTokenizer
from xgboost import XGBClassifier

signal.signal(signal.SIGHUP, signal.SIG_IGN)

SEED = 42
torch.manual_seed(SEED)
torch.cuda.manual_seed(SEED)

PROJECT_ROOT = Path(__file__).resolve().parent

GENERATOR_PATHS = [
    "/root/autodl-tmp/.hf_cache/EleutherAI/pythia-2___8b",
    "/root/autodl-tmp/models/pythia-2.8b",
]
GENERATOR_NAME = "pythia-2.8b"

REF_MODEL_SNAPSHOT = "/root/autodl-tmp/models/pythia-410m/models--EleutherAI--pythia-410m/snapshots/9879c9b5f8bea9051dcb0e68dff21493d67e9d4f"

MAX_DEPTH = 4
NUM_DEPTHS = MAX_DEPTH + 1

PARAPHRASE_TEMPLATES = [
    "Original: {text}\nRewritten version:",
    "Text: {text}\nThe same information expressed differently:",
    "Source: {text}\nAlternative wording:",
]

FEATURES = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max",
            "tail_decay", "ttr", "hapax_ratio"]

CLASS_MAP = {0: 0, 1: 1, 2: 2, 3: 2, 4: 2}
CLASS_NAMES = ["gen-0", "gen-1", "gen-2+"]

XGB_PARAMS = dict(n_estimators=200, max_depth=6, learning_rate=0.1,
                  random_state=SEED, eval_metric="mlogloss",
                  use_label_encoder=False)


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


# ===========================================================================
# Phase 1: Generate paraphrastic chains
# ===========================================================================

def find_generator_path():
    for p in GENERATOR_PATHS:
        if os.path.isfile(os.path.join(p, "config.json")):
            return p
    raise FileNotFoundError(f"Generator model not found at: {GENERATOR_PATHS}")


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
    print(f"Loaded {len(seeds)} seeds from {path}")
    return seeds


def build_paraphrase_prompt(text, tokenizer, depth, max_text_tokens=200):
    template = PARAPHRASE_TEMPLATES[depth % len(PARAPHRASE_TEMPLATES)]
    text_ids = tokenizer.encode(text, add_special_tokens=False)[:max_text_tokens]
    truncated = tokenizer.decode(text_ids)
    return template.format(text=truncated)


def generate_paraphrase(model, tokenizer, text, device, depth, max_new_tokens=256):
    prompt = build_paraphrase_prompt(text, tokenizer, depth)
    input_ids = tokenizer.encode(prompt, add_special_tokens=False)
    if len(input_ids) == 0:
        return ""
    input_ids = input_ids[-256:]
    input_tensor = torch.tensor([input_ids], device=device)

    with torch.no_grad():
        output = model.generate(
            input_tensor,
            max_new_tokens=max_new_tokens,
            temperature=0.7,
            top_p=0.9,
            do_sample=True,
            repetition_penalty=1.0,
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
                record = json.loads(line)
                done.add(record["seed_id"])
            except (json.JSONDecodeError, KeyError):
                pass
    return done


def phase_generate(args):
    device = torch.device(args.device)
    model_path = find_generator_path()
    print(f"Loading generator from {model_path}")

    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(
        model_path, dtype=torch.float16, trust_remote_code=True,
    ).to(device)
    model.eval()
    print(f"Generator loaded on {device}")

    input_path = PROJECT_ROOT / args.input
    if not input_path.exists():
        raise FileNotFoundError(f"Seed file not found: {input_path}")
    all_seeds = load_seeds(str(input_path), tokenizer)

    total = len(all_seeds)
    shard_size = total // args.num_shards
    start = args.shard_id * shard_size
    end = start + shard_size if args.shard_id < args.num_shards - 1 else total
    seeds = all_seeds[start:end]
    print(f"Shard {args.shard_id}/{args.num_shards}: seeds [{start}:{end}] ({len(seeds)} seeds)")

    if args.max_seeds is not None:
        seeds = seeds[:args.max_seeds]
        print(f"Limiting to {len(seeds)} seeds (--max-seeds)")
    elif args.dry_run:
        seeds = seeds[:5]
        print(f"[DRY-RUN] Processing only {len(seeds)} seeds")

    output_dir = PROJECT_ROOT / "data" / "pythia-2.8b-paraphrase"
    os.makedirs(output_dir, exist_ok=True)
    output_path = output_dir / f"generations_shard{args.shard_id}.jsonl"

    done_seeds = load_done_seeds(str(output_path))
    if done_seeds:
        print(f"Resuming: found {len(done_seeds)} completed seeds, skipping")

    t0 = time.time()
    record_count = 0
    skipped = 0

    with open(output_path, "a") as f:
        for i, seed_info in enumerate(seeds):
            seed_id = seed_info["seed_id"]
            seed_text = seed_info["text"]

            if seed_id in done_seeds:
                continue

            base_id = args.shard_id * shard_size * NUM_DEPTHS + i * NUM_DEPTHS

            gen0_tokens = tokenizer.encode(seed_text, add_special_tokens=False)
            f.write(json.dumps({
                "id": base_id,
                "depth": 0,
                "text": seed_text,
                "seed_id": seed_id,
                "token_count": len(gen0_tokens),
                "model": GENERATOR_NAME,
                "prompt_type": "paraphrase",
            }, ensure_ascii=False) + "\n")
            f.flush()
            record_count += 1

            prev_text = seed_text
            for depth in range(1, NUM_DEPTHS):
                check_ids = tokenizer.encode(prev_text, add_special_tokens=False)
                if len(check_ids) == 0 or len(prev_text.strip()) < 10:
                    print(f"WARNING: Skipping seed {seed_id} at depth {depth}: empty input")
                    skipped += 1
                    break

                paraphrase = generate_paraphrase(model, tokenizer, prev_text, device, depth)
                if not paraphrase or len(paraphrase.strip()) == 0:
                    print(f"WARNING: Skipping seed {seed_id} at depth {depth}: empty output")
                    skipped += 1
                    break

                para_tokens = tokenizer.encode(paraphrase, add_special_tokens=False)
                f.write(json.dumps({
                    "id": base_id + depth,
                    "depth": depth,
                    "text": paraphrase,
                    "seed_id": seed_id,
                    "token_count": len(para_tokens),
                    "model": GENERATOR_NAME,
                    "prompt_type": "paraphrase",
                }, ensure_ascii=False) + "\n")
                f.flush()
                record_count += 1
                prev_text = paraphrase

            if (i + 1) % 50 == 0:
                elapsed = time.time() - t0
                print(f"[{i+1}/{len(seeds)}] {elapsed:.0f}s elapsed, {(i+1)/elapsed:.2f} seeds/s")

    elapsed = time.time() - t0
    print(f"Generate done. {record_count} records written to {output_path} in {elapsed:.1f}s (skipped {skipped})")


# ===========================================================================
# Phase 2: Feature extraction (mirrors extract_features.py)
# ===========================================================================

def load_ref_model(device):
    print(f"Loading reference model from {REF_MODEL_SNAPSHOT} on {device}")
    tokenizer = AutoTokenizer.from_pretrained(REF_MODEL_SNAPSHOT, local_files_only=True)
    model = AutoModelForCausalLM.from_pretrained(
        REF_MODEL_SNAPSHOT, local_files_only=True, torch_dtype=torch.float16,
    ).to(device).eval()
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    return tokenizer, model


def compute_reference_features(texts, tokenizer, model, device, batch_size):
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
                results.append(dict(entropy_mean=0.0, entropy_std=0.0,
                                    entropy_min=0.0, entropy_max=0.0, tail_decay=0.0))
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

            results.append(dict(
                entropy_mean=float(np.mean(entropy_np)),
                entropy_std=float(np.std(entropy_np)),
                entropy_min=float(np.min(entropy_np)),
                entropy_max=float(np.max(entropy_np)),
                tail_decay=tail_decay,
            ))

        print(f"  Ref features: {min(start + batch_size, len(texts))}/{len(texts)}")

    return results


def compute_surface_features(texts):
    results = []
    for text in texts:
        words = text.lower().split()
        n_tokens = len(words)
        if n_tokens == 0:
            results.append(dict(ttr=0.0, hapax_ratio=0.0))
            continue
        counter = Counter(words)
        results.append(dict(
            ttr=len(counter) / n_tokens,
            hapax_ratio=sum(1 for c in counter.values() if c == 1) / n_tokens,
        ))
    return results


def load_generations(data_dir):
    records = []
    merged = data_dir / "generations.jsonl"
    if merged.exists():
        files = [str(merged)]
    else:
        files = sorted(glob.glob(str(data_dir / "generations_shard*.jsonl")))
    for fp in files:
        with open(fp) as f:
            for line in f:
                line = line.strip()
                if line:
                    records.append(json.loads(line))
    return records


def phase_extract(args):
    device = args.device
    data_dir = PROJECT_ROOT / "data" / "pythia-2.8b-paraphrase"
    records = load_generations(data_dir)
    if not records:
        print("ERROR: no paraphrase generation data found")
        sys.exit(1)
    print(f"Loaded {len(records)} paraphrase records")

    if args.dry_run:
        records = records[:50]
        print(f"[dry-run] Using first {len(records)} records")

    texts = [r["text"] for r in records]

    tokenizer, model = load_ref_model(device)
    ref_feats = compute_reference_features(texts, tokenizer, model, device, args.batch_size)
    del model, tokenizer
    torch.cuda.empty_cache()

    surf_feats = compute_surface_features(texts)

    rows = []
    for rec, ref, surf in zip(records, ref_feats, surf_feats):
        rows.append(dict(
            id=rec["id"], depth=rec["depth"], seed_id=rec["seed_id"],
            prompt_type="paraphrase", **ref, **surf,
        ))

    df = pd.DataFrame(rows)
    out_path = PROJECT_ROOT / "data" / "paraphrase_features.csv"
    df.to_csv(out_path, index=False)
    print(f"Features saved to {out_path} ({df.shape})")


# ===========================================================================
# Phase 3: Evaluate — 3-class CV + comparison vs continuation
# ===========================================================================

def load_continuation_features():
    feat_path = PROJECT_ROOT / "data" / "prompt_type_features.csv"
    if feat_path.exists():
        df = pd.read_csv(feat_path)
        cont = df[df["prompt_type"] == "continuation"]
        if len(cont) > 0:
            print(f"Loaded {len(cont)} continuation records from {feat_path}")
            return cont

    feat_path = PROJECT_ROOT / "data" / "features_pythia-2.8b.csv"
    if feat_path.exists():
        df = pd.read_csv(feat_path)
        df["prompt_type"] = "continuation"
        print(f"Loaded {len(df)} continuation records from {feat_path}")
        return df

    return None


def downsample(df, label_col, rng):
    counts = df[label_col].value_counts()
    min_n = counts.min()
    parts = [df[df[label_col] == lbl].sample(n=min_n, random_state=rng, replace=False)
             for lbl in sorted(counts.index)]
    return pd.concat(parts, ignore_index=True)


def bootstrap_f1(y_true, y_pred, n_boot=1000):
    rng = np.random.RandomState(SEED)
    n = len(y_true)
    scores = []
    for _ in range(n_boot):
        idx = rng.randint(0, n, size=n)
        yt, yp = y_true[idx], y_pred[idx]
        if len(np.unique(yt)) < len(CLASS_NAMES):
            continue
        scores.append(f1_score(yt, yp, average="macro"))
    arr = np.array(scores)
    return dict(mean=float(np.mean(arr)),
                ci_lo=float(np.percentile(arr, 2.5)),
                ci_hi=float(np.percentile(arr, 97.5)))


def within_type_cv(df, label_col="label"):
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=SEED)
    fold_f1s = []
    rng = np.random.RandomState(SEED)
    for train_idx, test_idx in skf.split(df, df[label_col]):
        train_fold = df.iloc[train_idx]
        test_fold = df.iloc[test_idx]
        train_ds = downsample(train_fold, label_col, rng)
        clf = XGBClassifier(**XGB_PARAMS)
        clf.fit(train_ds[FEATURES].values, train_ds[label_col].values)
        y_pred = clf.predict(test_fold[FEATURES].values)
        fold_f1s.append(float(f1_score(test_fold[label_col].values, y_pred, average="macro")))
    return dict(mean=float(np.mean(fold_f1s)), std=float(np.std(fold_f1s)), folds=fold_f1s)


def spearman_analysis(df):
    correlations = {}
    for feat in FEATURES:
        rho, p = spearmanr(df[feat], df["depth"])
        correlations[feat] = dict(rho=float(rho), p=float(p))
    return correlations


def depth_retention(df):
    seeds_per_depth = df.groupby("depth")["seed_id"].nunique()
    d0 = seeds_per_depth.get(0, 0)
    d4 = seeds_per_depth.get(4, 0)
    return dict(d0_seeds=int(d0), d4_seeds=int(d4),
                retention=round(d4 / d0, 4) if d0 > 0 else 0.0)


def binary_f1_eval(df, label_col="label"):
    sub = df[df[label_col].isin([1, 2])].copy()
    if len(sub) < 20:
        return dict(status="insufficient_data")
    sub["binary"] = (sub[label_col] == 2).astype(int)
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=SEED)
    fold_f1s = []
    rng = np.random.RandomState(SEED)
    for train_idx, test_idx in skf.split(sub, sub["binary"]):
        train_fold = sub.iloc[train_idx]
        test_fold = sub.iloc[test_idx]
        train_ds = downsample(train_fold, "binary", rng)
        clf = XGBClassifier(**XGB_PARAMS)
        clf.fit(train_ds[FEATURES].values, train_ds["binary"].values)
        y_pred = clf.predict(test_fold[FEATURES].values)
        fold_f1s.append(float(f1_score(test_fold["binary"].values, y_pred, average="macro")))
    return dict(mean=float(np.mean(fold_f1s)), std=float(np.std(fold_f1s)))


def feature_slope_comparison(df_para, df_cont):
    result = {}
    for feat in FEATURES:
        slopes = {}
        for name, df in [("paraphrase", df_para), ("continuation", df_cont)]:
            means = df.groupby("depth")[feat].mean()
            if len(means) < 2:
                slopes[name] = 0.0
                continue
            x = np.array(means.index, dtype=float)
            y = means.values.astype(float)
            coeffs = np.polyfit(x, y, 1)
            slopes[name] = round(float(coeffs[0]), 6)
        slopes["delta"] = round(slopes["paraphrase"] - slopes["continuation"], 6)
        result[feat] = slopes
    return result


def phase_evaluate(args):
    para_path = PROJECT_ROOT / "data" / "paraphrase_features.csv"
    if not para_path.exists():
        print(f"ERROR: {para_path} not found. Run --phase extract first.")
        sys.exit(1)
    df_para = pd.read_csv(para_path)
    df_para["label"] = df_para["depth"].map(CLASS_MAP)
    df_para["prompt_type"] = "paraphrase"
    print(f"Paraphrase features: {len(df_para)} records")

    df_cont = load_continuation_features()
    if df_cont is None:
        print("WARNING: continuation features not found, comparison will be partial")
    else:
        df_cont["label"] = df_cont["depth"].map(CLASS_MAP)

    results = {}

    # 1. Paraphrase within-type depth signal
    print("\n" + "=" * 60)
    print("1. Paraphrase Depth Signal (5-fold CV)")
    print("=" * 60)
    para_cv = within_type_cv(df_para)
    para_spearman = spearman_analysis(df_para)
    para_retention = depth_retention(df_para)
    para_binary = binary_f1_eval(df_para)

    results["paraphrase_signal"] = dict(
        n=len(df_para),
        depth_distribution={str(k): int(v) for k, v in
                            df_para["depth"].value_counts().sort_index().items()},
        cv5_3class_f1=para_cv,
        spearman_correlations=para_spearman,
        depth_retention=para_retention,
        binary_f1_gen1_vs_gen2plus=para_binary,
    )
    print(f"  3-class CV F1: {para_cv['mean']:.4f} +/- {para_cv['std']:.4f}")
    print(f"  Depth retention (d4/d0): {para_retention['retention']:.4f}")
    print(f"  Binary F1 (gen-1 vs gen-2+): {para_binary.get('mean', 'N/A')}")

    # 2. Continuation within-type depth signal (if available)
    if df_cont is not None:
        print("\n" + "=" * 60)
        print("2. Continuation Depth Signal (5-fold CV)")
        print("=" * 60)
        cont_cv = within_type_cv(df_cont)
        cont_spearman = spearman_analysis(df_cont)
        cont_retention = depth_retention(df_cont)
        cont_binary = binary_f1_eval(df_cont)

        results["continuation_signal"] = dict(
            n=len(df_cont),
            cv5_3class_f1=cont_cv,
            spearman_correlations=cont_spearman,
            depth_retention=cont_retention,
            binary_f1_gen1_vs_gen2plus=cont_binary,
        )
        print(f"  3-class CV F1: {cont_cv['mean']:.4f} +/- {cont_cv['std']:.4f}")
        print(f"  Depth retention (d4/d0): {cont_retention['retention']:.4f}")

        # 3. Head-to-head comparison
        print("\n" + "=" * 60)
        print("3. Paraphrase vs Continuation Comparison")
        print("=" * 60)

        f1_delta = round(para_cv["mean"] - cont_cv["mean"], 4)
        retention_delta = round(para_retention["retention"] - cont_retention["retention"], 4)

        spearman_comparison = {}
        for feat in FEATURES:
            pr = para_spearman[feat]["rho"]
            cr = cont_spearman[feat]["rho"]
            spearman_comparison[feat] = dict(
                paraphrase_rho=round(pr, 4),
                continuation_rho=round(cr, 4),
                delta=round(pr - cr, 4),
                para_stronger=abs(pr) > abs(cr),
            )

        slopes = feature_slope_comparison(df_para, df_cont)

        # Cross-type transfer
        rng = np.random.RandomState(SEED)
        train_para = downsample(df_para, "label", rng)
        clf_para = XGBClassifier(**XGB_PARAMS)
        clf_para.fit(train_para[FEATURES].values, train_para["label"].values)
        y_pred_on_cont = clf_para.predict(df_cont[FEATURES].values)
        para_to_cont_f1 = float(f1_score(df_cont["label"].values, y_pred_on_cont, average="macro"))

        train_cont = downsample(df_cont, "label", rng)
        clf_cont = XGBClassifier(**XGB_PARAMS)
        clf_cont.fit(train_cont[FEATURES].values, train_cont["label"].values)
        y_pred_on_para = clf_cont.predict(df_para[FEATURES].values)
        cont_to_para_f1 = float(f1_score(df_para["label"].values, y_pred_on_para, average="macro"))

        results["comparison"] = dict(
            f1_3class_delta=f1_delta,
            retention_delta=retention_delta,
            spearman_comparison=spearman_comparison,
            feature_slopes=slopes,
            cross_transfer=dict(
                para_train_cont_test_f1=round(para_to_cont_f1, 4),
                cont_train_para_test_f1=round(cont_to_para_f1, 4),
            ),
        )

        print(f"  3-class F1 delta (para - cont): {f1_delta:+.4f}")
        print(f"  Retention delta: {retention_delta:+.4f}")
        print(f"  Cross-transfer: para->cont={para_to_cont_f1:.4f}, cont->para={cont_to_para_f1:.4f}")

        if f1_delta < -0.05:
            conclusion = "confirmed: paraphrastic chains lose depth signal faster"
        elif abs(f1_delta) <= 0.05:
            conclusion = "similar: paraphrastic and continuation chains retain comparable depth signal"
        else:
            conclusion = "surprising: paraphrastic chains retain MORE depth signal"

        if retention_delta < -0.05:
            conclusion += "; paraphrase chains have lower seed survival"

        results["conclusion"] = conclusion
        print(f"\n  Conclusion: {conclusion}")
    else:
        results["conclusion"] = "partial: continuation data unavailable for comparison"

    out_path = PROJECT_ROOT / "results" / "plan006_paraphrastic_comparison.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2, cls=NumpyEncoder, ensure_ascii=False)
    print(f"\nResults saved to {out_path}")


# ===========================================================================
# Main
# ===========================================================================

def main():
    parser = argparse.ArgumentParser(description="plan_006: Paraphrastic chain comparison")
    parser.add_argument("--phase", choices=["generate", "extract", "evaluate", "all"],
                        default="all", help="Which phase to run")
    parser.add_argument("--device", default="cuda:1", help="CUDA device")
    parser.add_argument("--input", default="data/wiki_seed_1000.jsonl", help="Seed file")
    parser.add_argument("--shard-id", type=int, default=0)
    parser.add_argument("--num-shards", type=int, default=1)
    parser.add_argument("--max-seeds", type=int, default=None)
    parser.add_argument("--batch-size", type=int, default=8)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    phases = [args.phase] if args.phase != "all" else ["generate", "extract", "evaluate"]

    for phase in phases:
        print(f"\n{'='*60}")
        print(f"Phase: {phase}")
        print(f"{'='*60}")
        if phase == "generate":
            phase_generate(args)
        elif phase == "extract":
            phase_extract(args)
        elif phase == "evaluate":
            phase_evaluate(args)

    print("\nAll phases complete.")


if __name__ == "__main__":
    main()
