"""
Wild-data calibration experiment (plan_015).

Validates RF classifier calibration on real-world web text (RedPajama)
to test external validity of depth classification findings.

Three tests:
  A. d0 False Positive Rate: wild text should be classified as d0
  B. Mixed-domain 4-class accuracy: wild d0 + controlled d1-d3
  C. Feature distribution shift: KS test + MMD between wild d0 and controlled d0

Usage:
  python src/wild_data_calibration.py --mode download --n_samples 10000
  python src/wild_data_calibration.py --mode extract --gpu 0
  python src/wild_data_calibration.py --mode evaluate --controlled_features_dir results/pythia_nucleus095/
  python src/wild_data_calibration.py --mode all --gpu 0 --controlled_features_dir results/pythia_nucleus095/
"""

import argparse
import json
import os
import sys
import numpy as np
from collections import Counter
from scipy.stats import skew, kurtosis, entropy, ks_2samp
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

FEATURE_NAMES = [
    "mean_ppl", "var_ppl", "skewness_ppl", "kurtosis_ppl",
    "p10_ppl", "p25_ppl", "p50_ppl", "p75_ppl", "p90_ppl",
    "mean_surprisal", "var_surprisal", "entropy_of_surprisal",
    "type_token_ratio", "hapax_ratio", "bigram_entropy", "trigram_entropy",
    "rep_2gram", "rep_3gram", "rep_4gram",
]
NUM_FEATURES = len(FEATURE_NAMES)


def parse_args():
    p = argparse.ArgumentParser(description="Wild-data calibration for depth classifier (plan_015)")
    p.add_argument("--mode", choices=["download", "extract", "evaluate", "all"], default="all")
    p.add_argument("--data_source", choices=["redpajama", "dolma"], default="redpajama")
    p.add_argument("--n_samples", type=int, default=10000)
    p.add_argument("--min_tokens", type=int, default=512)
    p.add_argument("--truncate_tokens", type=int, default=512)
    p.add_argument("--reference_model", default="gpt2",
                   help="Reference LM for perplexity/surprisal features")
    p.add_argument("--gpu", type=int, default=0)
    p.add_argument("--batch_size", type=int, default=32)
    p.add_argument("--wild_data_dir", default="data/wild_calibration")
    p.add_argument("--controlled_features_dir", nargs="+",
                   default=["data/features"],
                   help="Directories containing per-cell feature JSONL files")
    p.add_argument("--output_dir", default="results/wild_calibration")
    p.add_argument("--seed", type=int, default=42)
    return p.parse_args()


# ── Data Download ──

def download_redpajama(output_path, n_samples, min_tokens, tokenizer, seed=42):
    from datasets import load_dataset

    print(f"Loading RedPajama-Data-1T-Sample (streaming)...")
    ds = load_dataset(
        "togethercomputer/RedPajama-Data-1T-Sample",
        split="train",
        streaming=True,
    )

    rng = np.random.RandomState(seed)
    collected = []
    skipped_short = 0
    skipped_wiki = 0

    for example in ds:
        meta = example.get("meta", "{}")
        if isinstance(meta, str):
            try:
                meta = json.loads(meta)
            except (json.JSONDecodeError, TypeError):
                meta = {}
        source = meta.get("redpajama_set_name", "")
        if "wikipedia" in source.lower():
            skipped_wiki += 1
            continue

        text = example.get("text", "")
        if not text or len(text) < 100:
            continue
        tokens = tokenizer.encode(text, add_special_tokens=False)
        if len(tokens) < min_tokens:
            skipped_short += 1
            continue

        tokens_trunc = tokens[:min_tokens]
        text_truncated = tokenizer.decode(tokens_trunc)

        collected.append({
            "text": text_truncated,
            "depth": 0,
            "source": "redpajama",
            "token_count": len(tokens_trunc),
            "original_source": source,
        })

        if len(collected) >= n_samples * 2:
            break

        if len(collected) % 5000 == 0 and len(collected) > 0:
            print(f"  Collected {len(collected)} candidates "
                  f"(skipped: {skipped_short} short, {skipped_wiki} wiki)...")

    if len(collected) > n_samples:
        idx = rng.choice(len(collected), n_samples, replace=False)
        collected = [collected[i] for i in sorted(idx)]

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        for rec in collected:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    source_dist = Counter(r["original_source"] for r in collected)
    print(f"Saved {len(collected)} samples to {output_path}")
    print(f"Source distribution: {dict(source_dist)}")
    return collected


def download_dolma(output_path, n_samples, min_tokens, tokenizer, seed=42):
    from datasets import load_dataset

    print("Loading Dolma v1.7 sample (streaming)...")
    ds = load_dataset(
        "allenai/dolma",
        name="v1_7-sample",
        split="train",
        streaming=True,
    )

    collected = []
    skipped = 0

    for example in ds:
        text = example.get("text", "")
        if not text or len(text) < 100:
            continue
        tokens = tokenizer.encode(text, add_special_tokens=False)
        if len(tokens) < min_tokens:
            skipped += 1
            continue

        tokens_trunc = tokens[:min_tokens]
        text_truncated = tokenizer.decode(tokens_trunc)

        collected.append({
            "text": text_truncated,
            "depth": 0,
            "source": "dolma",
            "token_count": len(tokens_trunc),
        })

        if len(collected) >= n_samples:
            break

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        for rec in collected:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    print(f"Saved {len(collected)} samples to {output_path}")
    return collected


# ── Feature Extraction ──

def compute_repetition_rates(token_ids):
    def _rep_rate(ids, n):
        if len(ids) < n:
            return 0.0
        ngrams = [tuple(ids[i:i+n]) for i in range(len(ids) - n + 1)]
        if not ngrams:
            return 0.0
        counts = Counter(ngrams)
        repeated = sum(c - 1 for c in counts.values() if c > 1)
        return repeated / len(ngrams)

    return _rep_rate(token_ids, 2), _rep_rate(token_ids, 3), _rep_rate(token_ids, 4)


def compute_lexical_features(token_ids):
    total = len(token_ids)
    if total == 0:
        return 0.0, 0.0, 0.0, 0.0

    counts = Counter(token_ids)
    unique = len(counts)
    ttr = unique / total
    hapax = sum(1 for c in counts.values() if c == 1)
    hapax_ratio = hapax / unique if unique > 0 else 0.0

    bigrams = [tuple(token_ids[i:i+2]) for i in range(len(token_ids) - 1)]
    if bigrams:
        bg_counts = Counter(bigrams)
        bg_freq = np.array(list(bg_counts.values()), dtype=np.float64)
        bg_freq /= bg_freq.sum()
        bg_ent = float(entropy(bg_freq))
    else:
        bg_ent = 0.0

    trigrams = [tuple(token_ids[i:i+3]) for i in range(len(token_ids) - 2)]
    if trigrams:
        tg_counts = Counter(trigrams)
        tg_freq = np.array(list(tg_counts.values()), dtype=np.float64)
        tg_freq /= tg_freq.sum()
        tg_ent = float(entropy(tg_freq))
    else:
        tg_ent = 0.0

    return ttr, hapax_ratio, bg_ent, tg_ent


def surprisal_entropy_hist(surprisals, n_bins=50):
    if len(surprisals) < 2:
        return 0.0
    hist, _ = np.histogram(surprisals, bins=n_bins, density=True)
    hist = hist[hist > 0]
    if len(hist) == 0:
        return 0.0
    hist = hist / hist.sum()
    return float(entropy(hist))


def extract_features_batch(model, tokenizer, texts, trunc_len, device):
    import torch

    encoded = [tokenizer.encode(t, add_special_tokens=False)[:trunc_len] for t in texts]
    max_len = max(len(e) for e in encoded)
    pad_id = tokenizer.pad_token_id if tokenizer.pad_token_id is not None else tokenizer.eos_token_id

    input_ids_list, attn_mask_list = [], []
    for e in encoded:
        pad_len = max_len - len(e)
        input_ids_list.append(e + [pad_id] * pad_len)
        attn_mask_list.append([1] * len(e) + [0] * pad_len)

    input_ids_t = torch.tensor(input_ids_list, dtype=torch.long, device=device)
    attn_mask_t = torch.tensor(attn_mask_list, dtype=torch.long, device=device)

    with torch.no_grad():
        logits = model(input_ids=input_ids_t, attention_mask=attn_mask_t).logits

    shift_logits = logits[:, :-1, :].contiguous()
    shift_labels = input_ids_t[:, 1:].contiguous()
    loss_fn = torch.nn.CrossEntropyLoss(reduction="none")
    per_token_loss = loss_fn(
        shift_logits.view(-1, shift_logits.size(-1)),
        shift_labels.view(-1),
    ).view(shift_logits.size(0), shift_logits.size(1))

    results = []
    for i in range(len(texts)):
        seq_len = len(encoded[i])
        if seq_len <= 1:
            surprisals = np.array([0.0])
        else:
            surprisals = per_token_loss[i, :seq_len - 1].cpu().numpy().astype(np.float64)

        ppl_per_token = np.exp(np.clip(surprisals, 0, 20))

        ttr, hapax_r, bg_ent, tg_ent = compute_lexical_features(encoded[i])
        rep2, rep3, rep4 = compute_repetition_rates(encoded[i])

        results.append({
            "mean_ppl": float(np.mean(ppl_per_token)),
            "var_ppl": float(np.var(ppl_per_token)),
            "skewness_ppl": float(skew(ppl_per_token)) if len(ppl_per_token) > 2 else 0.0,
            "kurtosis_ppl": float(kurtosis(ppl_per_token)) if len(ppl_per_token) > 3 else 0.0,
            "p10_ppl": float(np.percentile(ppl_per_token, 10)),
            "p25_ppl": float(np.percentile(ppl_per_token, 25)),
            "p50_ppl": float(np.percentile(ppl_per_token, 50)),
            "p75_ppl": float(np.percentile(ppl_per_token, 75)),
            "p90_ppl": float(np.percentile(ppl_per_token, 90)),
            "mean_surprisal": float(np.mean(surprisals)),
            "var_surprisal": float(np.var(surprisals)),
            "entropy_of_surprisal": surprisal_entropy_hist(surprisals),
            "type_token_ratio": ttr,
            "hapax_ratio": hapax_r,
            "bigram_entropy": bg_ent,
            "trigram_entropy": tg_ent,
            "rep_2gram": rep2,
            "rep_3gram": rep3,
            "rep_4gram": rep4,
            "depth": 0,
        })
    return results


def run_feature_extraction(args):
    import torch
    from transformers import AutoTokenizer, AutoModelForCausalLM

    device = torch.device(f"cuda:{args.gpu}" if torch.cuda.is_available() else "cpu")
    print(f"Device: {device}")

    wild_path = os.path.join(args.wild_data_dir, "wild_d0.jsonl")
    records = []
    with open(wild_path) as f:
        for line in f:
            if line.strip():
                records.append(json.loads(line))
    print(f"Loaded {len(records)} wild samples")

    print(f"Loading reference model: {args.reference_model}")
    tokenizer = AutoTokenizer.from_pretrained(args.reference_model)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    model = AutoModelForCausalLM.from_pretrained(
        args.reference_model, torch_dtype=torch.float16,
    ).to(device)
    model.eval()

    texts = [r["text"] for r in records]
    all_features = []
    bs = args.batch_size

    for start in range(0, len(texts), bs):
        end = min(start + bs, len(texts))
        batch_feats = extract_features_batch(
            model, tokenizer, texts[start:end], args.truncate_tokens, device,
        )
        all_features.extend(batch_feats)
        if (start // bs) % 50 == 0 or end == len(texts):
            print(f"  Extracted features: {end}/{len(texts)}")

    output_path = os.path.join(args.wild_data_dir, "wild_d0_features.jsonl")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        for feat in all_features:
            f.write(json.dumps(feat) + "\n")
    print(f"Features saved to {output_path} ({len(all_features)} samples)")
    return all_features


# ── Feature Loading ──

def load_features(path):
    records = []
    with open(path) as f:
        for line in f:
            if line.strip():
                records.append(json.loads(line))
    X = np.array([[r[k] for k in FEATURE_NAMES] for r in records], dtype=np.float64)
    y = np.array([r["depth"] for r in records], dtype=np.int64)
    X = np.nan_to_num(X, nan=0.0, posinf=0.0, neginf=0.0)
    return X, y


def find_feature_files(dirs):
    found = {}
    for d in dirs:
        if not os.path.isdir(d):
            if os.path.isfile(d) and d.endswith(".jsonl"):
                name = os.path.splitext(os.path.basename(d))[0]
                found[name] = d
            continue
        for root, _, files in os.walk(d):
            for f in files:
                if f.endswith(".jsonl") and "feature" in f.lower():
                    cell = os.path.basename(root)
                    if cell in (".", "data", "features"):
                        cell = os.path.splitext(f)[0]
                    found[cell] = os.path.join(root, f)
    return found


# ── Test A: d0 False Positive Rate ──

def test_a_d0_fpr(wild_X, ctrl_X, ctrl_y, output_dir, seed=42):
    print("\n" + "=" * 60)
    print("TEST A: d0 False Positive Rate on Wild Data")
    print("=" * 60)

    scaler = StandardScaler()
    X_train = scaler.fit_transform(ctrl_X)
    rf = RandomForestClassifier(n_estimators=100, random_state=seed, n_jobs=-1)
    rf.fit(X_train, ctrl_y)

    X_wild = scaler.transform(wild_X)
    y_pred = rf.predict(X_wild)
    y_prob = rf.predict_proba(X_wild)

    pred_dist = Counter(int(x) for x in y_pred)
    n_total = len(y_pred)
    d0_rate = pred_dist.get(0, 0) / n_total
    fpr = 1.0 - d0_rate

    d0_col = list(rf.classes_).index(0)
    mean_p_d0 = float(np.mean(y_prob[:, d0_col]))
    std_p_d0 = float(np.std(y_prob[:, d0_col]))

    results = {
        "n_wild_samples": n_total,
        "d0_rate": round(d0_rate, 4),
        "fpr_d_gt_0": round(fpr, 4),
        "prediction_distribution": {str(k): v for k, v in sorted(pred_dist.items())},
        "mean_P_d0": round(mean_p_d0, 4),
        "std_P_d0": round(std_p_d0, 4),
    }

    print(f"  d0 classification rate: {d0_rate:.1%}")
    print(f"  False positive rate (d>0): {fpr:.1%}")
    print(f"  Prediction distribution: {dict(pred_dist)}")
    print(f"  Mean P(d0): {mean_p_d0:.4f} ± {std_p_d0:.4f}")

    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "test_a_d0_fpr.json"), "w") as f:
        json.dump(results, f, indent=2)
    return results


# ── Test B: Mixed-domain 4-class Accuracy ──

def test_b_mixed_accuracy(wild_X, ctrl_X, ctrl_y, output_dir, seed=42):
    print("\n" + "=" * 60)
    print("TEST B: Mixed-domain 4-class Accuracy")
    print("=" * 60)

    ctrl_X_train, ctrl_X_test, ctrl_y_train, ctrl_y_test = train_test_split(
        ctrl_X, ctrl_y, test_size=0.2, random_state=seed, stratify=ctrl_y,
    )

    scaler = StandardScaler()
    X_train = scaler.fit_transform(ctrl_X_train)
    rf = RandomForestClassifier(n_estimators=100, random_state=seed, n_jobs=-1)
    rf.fit(X_train, ctrl_y_train)

    # In-distribution baseline
    y_pred_ctrl = rf.predict(scaler.transform(ctrl_X_test))
    acc_indist = accuracy_score(ctrl_y_test, y_pred_ctrl)

    # Mixed test set: wild d0 + controlled d1-d3 (from test split)
    n_per_class = min(
        len(wild_X),
        *[int(np.sum(ctrl_y_test == d)) for d in [1, 2, 3]],
    )
    n_per_class = min(n_per_class, 2500)

    rng = np.random.RandomState(seed)
    mixed_parts_X, mixed_parts_y = [], []

    wild_idx = rng.choice(len(wild_X), min(n_per_class, len(wild_X)), replace=False)
    mixed_parts_X.append(wild_X[wild_idx])
    mixed_parts_y.append(np.zeros(len(wild_idx), dtype=np.int64))

    for d in [1, 2, 3]:
        d_idx = np.where(ctrl_y_test == d)[0]
        if len(d_idx) > n_per_class:
            d_idx = rng.choice(d_idx, n_per_class, replace=False)
        mixed_parts_X.append(ctrl_X_test[d_idx])
        mixed_parts_y.append(np.full(len(d_idx), d, dtype=np.int64))

    mixed_X = np.vstack(mixed_parts_X)
    mixed_y = np.concatenate(mixed_parts_y)

    y_pred_mixed = rf.predict(scaler.transform(mixed_X))
    acc_mixed = accuracy_score(mixed_y, y_pred_mixed)

    labels = [f"d{d}" for d in range(4)]
    report = classification_report(
        mixed_y, y_pred_mixed, output_dict=True, target_names=labels,
    )

    results = {
        "in_distribution_accuracy": round(acc_indist, 4),
        "mixed_domain_accuracy": round(acc_mixed, 4),
        "accuracy_gap_pp": round((acc_indist - acc_mixed) * 100, 1),
        "n_per_class": n_per_class,
        "per_class_recall": {
            f"d{d}": round(report[f"d{d}"]["recall"], 4) for d in range(4)
        },
        "confusion_matrix": confusion_matrix(mixed_y, y_pred_mixed).tolist(),
    }

    print(f"  In-distribution accuracy: {acc_indist:.1%}")
    print(f"  Mixed-domain accuracy:    {acc_mixed:.1%}")
    print(f"  Gap: {results['accuracy_gap_pp']:.1f} pp")
    print(f"  Per-class recall: {results['per_class_recall']}")

    with open(os.path.join(output_dir, "test_b_mixed_accuracy.json"), "w") as f:
        json.dump(results, f, indent=2)
    return results


# ── Test C: Feature Distribution Shift ──

def compute_mmd_rbf(X, Y, n_subsample=2000, seed=42):
    from sklearn.metrics.pairwise import rbf_kernel
    from scipy.spatial.distance import cdist

    rng = np.random.RandomState(seed)
    n = min(n_subsample, len(X), len(Y))
    Xs = X[rng.choice(len(X), n, replace=False)]
    Ys = Y[rng.choice(len(Y), n, replace=False)]

    scaler = StandardScaler()
    combined = np.vstack([Xs, Ys])
    scaler.fit(combined)
    Xs = scaler.transform(Xs)
    Ys = scaler.transform(Ys)

    dists = cdist(combined[:min(500, len(combined))],
                  combined[:min(500, len(combined))], "sqeuclidean")
    gamma = 1.0 / max(np.median(dists[dists > 0]), 1e-8)

    XX = rbf_kernel(Xs, Xs, gamma=gamma)
    YY = rbf_kernel(Ys, Ys, gamma=gamma)
    XY = rbf_kernel(Xs, Ys, gamma=gamma)
    mmd2 = XX.mean() + YY.mean() - 2 * XY.mean()
    return float(np.sqrt(max(mmd2, 0)))


def test_c_distribution_shift(wild_X, ctrl_X, ctrl_y, output_dir):
    print("\n" + "=" * 60)
    print("TEST C: Feature Distribution Shift (wild d0 vs controlled d0)")
    print("=" * 60)

    d0_mask = ctrl_y == 0
    ctrl_d0_X = ctrl_X[d0_mask]
    print(f"  Wild d0: {len(wild_X)} samples")
    print(f"  Controlled d0: {len(ctrl_d0_X)} samples")

    alpha = 0.05
    bonferroni_alpha = alpha / NUM_FEATURES
    ks_results = {}

    for i, fname in enumerate(FEATURE_NAMES):
        stat, pval = ks_2samp(wild_X[:, i], ctrl_d0_X[:, i])
        ks_results[fname] = {
            "ks_statistic": round(float(stat), 4),
            "p_value": float(pval),
            "significant": pval < bonferroni_alpha,
            "wild_mean": round(float(np.mean(wild_X[:, i])), 4),
            "wild_std": round(float(np.std(wild_X[:, i])), 4),
            "ctrl_mean": round(float(np.mean(ctrl_d0_X[:, i])), 4),
            "ctrl_std": round(float(np.std(ctrl_d0_X[:, i])), 4),
        }

    sorted_feats = sorted(ks_results.items(), key=lambda x: -x[1]["ks_statistic"])

    print(f"\n  KS test (Bonferroni alpha={bonferroni_alpha:.4f}):")
    for fname, res in sorted_feats[:10]:
        sig = "***" if res["significant"] else "   "
        print(f"    {fname:25s}: KS={res['ks_statistic']:.4f}, "
              f"p={res['p_value']:.2e} {sig}")

    n_sig = sum(1 for r in ks_results.values() if r["significant"])
    print(f"\n  {n_sig}/{NUM_FEATURES} features significantly shifted")

    mmd_val = compute_mmd_rbf(wild_X, ctrl_d0_X)
    print(f"  MMD (RBF): {mmd_val:.4f}")

    results = {
        "ks_tests": ks_results,
        "n_significant_bonferroni": n_sig,
        "bonferroni_alpha": bonferroni_alpha,
        "mmd_rbf": round(mmd_val, 4),
        "top_5_shifted": [f for f, _ in sorted_feats[:5]],
    }

    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "test_c_distribution_shift.json"), "w") as f:
        json.dump(results, f, indent=2)
    return results


# ── Evaluation Runner ──

def run_evaluation(args):
    wild_features_path = os.path.join(args.wild_data_dir, "wild_d0_features.jsonl")
    print(f"Loading wild features from {wild_features_path}")
    wild_X, wild_y = load_features(wild_features_path)
    print(f"  Wild: {wild_X.shape[0]} samples, {wild_X.shape[1]} dims")

    feat_files = find_feature_files(args.controlled_features_dir)
    if not feat_files:
        print(f"ERROR: No feature JSONL files found in {args.controlled_features_dir}")
        sys.exit(1)

    print(f"Found {len(feat_files)} controlled feature file(s): {list(feat_files.keys())}")
    os.makedirs(args.output_dir, exist_ok=True)
    all_results = {}

    for cell_name, fpath in sorted(feat_files.items()):
        print(f"\n{'#' * 70}")
        print(f"# Cell: {cell_name}")
        print(f"# File: {fpath}")
        print(f"{'#' * 70}")

        ctrl_X, ctrl_y = load_features(fpath)
        depth_dist = dict(Counter(int(x) for x in ctrl_y))
        print(f"  Controlled: {ctrl_X.shape[0]} samples, depths: {depth_dist}")

        if len(set(ctrl_y)) < 4:
            print(f"  SKIP: fewer than 4 depth classes")
            continue

        cell_dir = os.path.join(args.output_dir, cell_name)

        res_a = test_a_d0_fpr(wild_X, ctrl_X, ctrl_y, cell_dir, args.seed)
        res_b = test_b_mixed_accuracy(wild_X, ctrl_X, ctrl_y, cell_dir, args.seed)
        res_c = test_c_distribution_shift(wild_X, ctrl_X, ctrl_y, cell_dir)

        all_results[cell_name] = {
            "test_a": res_a,
            "test_b": res_b,
            "test_c": {
                "mmd_rbf": res_c["mmd_rbf"],
                "n_significant_ks": res_c["n_significant_bonferroni"],
                "top_5_shifted": res_c["top_5_shifted"],
            },
        }

    # Summary
    print(f"\n{'=' * 80}")
    print("SUMMARY")
    print(f"{'=' * 80}")
    print(f"{'Cell':30s} {'d0%':>6s} {'FPR':>6s} {'Mix':>6s} {'InD':>6s} "
          f"{'Gap':>6s} {'MMD':>6s} {'#KS':>4s}")
    print("-" * 80)

    summary = {}
    for cell, res in sorted(all_results.items()):
        row = {
            "d0_rate": res["test_a"]["d0_rate"],
            "fpr": res["test_a"]["fpr_d_gt_0"],
            "mixed_acc": res["test_b"]["mixed_domain_accuracy"],
            "indist_acc": res["test_b"]["in_distribution_accuracy"],
            "gap_pp": res["test_b"]["accuracy_gap_pp"],
            "mmd": res["test_c"]["mmd_rbf"],
            "n_sig_ks": res["test_c"]["n_significant_ks"],
        }
        summary[cell] = row
        print(f"{cell:30s} {row['d0_rate']:6.1%} {row['fpr']:6.1%} "
              f"{row['mixed_acc']:6.1%} {row['indist_acc']:6.1%} "
              f"{row['gap_pp']:5.1f}pp {row['mmd']:6.4f} {row['n_sig_ks']:4d}")

    with open(os.path.join(args.output_dir, "summary.json"), "w") as f:
        json.dump(summary, f, indent=2)

    print(f"\nAll results saved to {args.output_dir}/")
    return all_results


# ── Main ──

def main():
    args = parse_args()

    if args.mode in ("download", "all"):
        from transformers import AutoTokenizer
        tokenizer = AutoTokenizer.from_pretrained(args.reference_model)
        output_path = os.path.join(args.wild_data_dir, "wild_d0.jsonl")
        if args.data_source == "redpajama":
            download_redpajama(output_path, args.n_samples, args.min_tokens,
                               tokenizer, args.seed)
        else:
            download_dolma(output_path, args.n_samples, args.min_tokens,
                           tokenizer, args.seed)

    if args.mode in ("extract", "all"):
        run_feature_extraction(args)

    if args.mode in ("evaluate", "all"):
        run_evaluation(args)


if __name__ == "__main__":
    main()
