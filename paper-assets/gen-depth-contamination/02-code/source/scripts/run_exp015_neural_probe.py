"""
exp-015: Neural Probe for Generational Depth Classification

Validates that K*=2 (found with 15D hand-crafted features + LightGBM) is
data-intrinsic, not a feature engineering artifact. Uses frozen Qwen2.5-1.5B
embeddings (last hidden state, avg pool -> 1536-dim) + MLP classifier.

v2 changes: memory-optimized (extract all embeddings then free LLM),
bootstrap CI, permutation test, peak VRAM logging, OOM-safe batch adapt.
"""

import argparse
import gc
import json
import logging
import sys
import time
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import GroupKFold
from tqdm import tqdm

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)


# -- Data loading ------------------------------------------------------

def load_depth_data(data_dir: Path, max_depth: int, num_samples: int = None):
    texts, depths, doc_ids = [], [], []
    for d in range(max_depth + 1):
        path = data_dir / f"depth_{d}.jsonl"
        if not path.exists():
            log.warning(f"Missing {path}, skipping depth {d}")
            continue
        count = 0
        with open(path) as f:
            for line in f:
                if num_samples is not None and count >= num_samples:
                    break
                rec = json.loads(line)
                texts.append(rec["text"])
                depths.append(d)
                doc_ids.append(rec["doc_id"])
                count += 1
        log.info(f"  depth {d}: {count} samples")
    return texts, np.array(depths), np.array(doc_ids)


# -- Embedding extraction with OOM retry ------------------------------

@torch.no_grad()
def extract_embeddings(model, tokenizer, texts, batch_size=16, max_length=512):
    """Auto-halves batch_size on OOM until batch_size=1."""
    all_emb = []
    actual_bs = batch_size
    i = 0
    pbar = tqdm(total=len(texts), desc="Embedding")
    while i < len(texts):
        batch = texts[i : i + actual_bs]
        try:
            inputs = tokenizer(
                batch,
                return_tensors="pt",
                padding=True,
                truncation=True,
                max_length=max_length,
            ).to(model.device)
            out = model(**inputs, output_hidden_states=True)
            hidden = out.hidden_states[-1]
            mask = inputs["attention_mask"].unsqueeze(-1).float()
            pooled = (hidden * mask).sum(dim=1) / mask.sum(dim=1).clamp(min=1)
            all_emb.append(pooled.cpu().float().numpy())
            pbar.update(len(batch))
            i += actual_bs
        except torch.cuda.OutOfMemoryError:
            torch.cuda.empty_cache()
            if actual_bs <= 1:
                pbar.close()
                raise RuntimeError(f"OOM even at batch_size=1 on sample {i}")
            old_bs = actual_bs
            actual_bs = max(1, actual_bs // 2)
            log.warning(f"OOM at batch_size={old_bs}, retrying with {actual_bs}")
    pbar.close()
    log.info(f"Embedding done (effective batch_size={actual_bs})")
    return np.concatenate(all_emb, axis=0), actual_bs


# -- MLP ---------------------------------------------------------------

class DepthMLP(nn.Module):
    def __init__(self, input_dim=1536, num_classes=6):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, 512),
            nn.ReLU(),
            nn.Dropout(0.1),
            nn.Linear(512, 256),
            nn.ReLU(),
            nn.Dropout(0.1),
            nn.Linear(256, num_classes),
        )

    def forward(self, x):
        return self.net(x)


def train_mlp(X_train, y_train, X_val, y_val, input_dim, num_classes,
              epochs=20, lr=1e-3, batch_size=256, patience=5, device="cuda"):
    model = DepthMLP(input_dim=input_dim, num_classes=num_classes).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=lr, weight_decay=1e-4)
    criterion = nn.CrossEntropyLoss()

    ds = TensorDataset(
        torch.tensor(X_train, dtype=torch.float32),
        torch.tensor(y_train, dtype=torch.long),
    )
    loader = DataLoader(ds, batch_size=batch_size, shuffle=True)
    X_val_t = torch.tensor(X_val, dtype=torch.float32).to(device)
    y_val_t = torch.tensor(y_val, dtype=torch.long).to(device)

    best_loss = float("inf")
    best_state = None
    wait = 0

    for epoch in range(epochs):
        model.train()
        for xb, yb in loader:
            xb, yb = xb.to(device), yb.to(device)
            optimizer.zero_grad()
            criterion(model(xb), yb).backward()
            optimizer.step()

        model.eval()
        with torch.no_grad():
            val_loss = criterion(model(X_val_t), y_val_t).item()

        if val_loss < best_loss:
            best_loss = val_loss
            best_state = {k: v.cpu().clone() for k, v in model.state_dict().items()}
            wait = 0
        else:
            wait += 1
            if wait >= patience:
                break

    model.load_state_dict(best_state)
    model.eval()
    return model


# -- Pairwise AUC ------------------------------------------------------

def compute_pairwise_auc(probas, depths, max_depth):
    def _auc_pair(i, j):
        mask = (depths == i) | (depths == j)
        y = (depths[mask] == j).astype(int)
        if len(np.unique(y)) < 2 or mask.sum() < 4:
            return float("nan")
        p_i = probas[mask, i]
        p_j = probas[mask, j]
        score = p_j / (p_i + p_j + 1e-12)
        return round(float(roc_auc_score(y, score)), 4)

    adjacent = {}
    for k in range(1, max_depth + 1):
        adjacent[f"{k-1}v{k}"] = _auc_pair(k - 1, k)

    all_pairs = {}
    for i in range(max_depth + 1):
        for j in range(i + 1, max_depth + 1):
            all_pairs[f"{i}v{j}"] = _auc_pair(i, j)

    return adjacent, all_pairs


# -- Bootstrap CI (doc-level resampling) --------------------------------

def bootstrap_auc_ci(depths, probas, pair_i, pair_j, doc_ids,
                     n_resamples=1000, seed=42):
    """Percentile bootstrap 95% CI, resampling at doc level to respect grouping."""
    mask = (depths == pair_i) | (depths == pair_j)
    y = (depths[mask] == pair_j).astype(int)
    p_i = probas[mask, pair_i]
    p_j = probas[mask, pair_j]
    scores = p_j / (p_i + p_j + 1e-12)
    docs_masked = doc_ids[mask]

    if len(np.unique(y)) < 2:
        return {"auc": float("nan"), "ci_lower": float("nan"),
                "ci_upper": float("nan"), "boot_std": float("nan")}

    obs_auc = float(roc_auc_score(y, scores))

    rng = np.random.default_rng(seed)
    unique_docs = np.unique(docs_masked)
    doc_idx_map = {d: np.where(docs_masked == d)[0] for d in unique_docs}

    boot_aucs = []
    for _ in range(n_resamples):
        sampled = rng.choice(unique_docs, size=len(unique_docs), replace=True)
        idx = np.concatenate([doc_idx_map[d] for d in sampled])
        yb, sb = y[idx], scores[idx]
        if len(np.unique(yb)) < 2:
            continue
        boot_aucs.append(roc_auc_score(yb, sb))

    boot_aucs = np.array(boot_aucs)
    ci_lo, ci_hi = np.percentile(boot_aucs, [2.5, 97.5])

    return {
        "auc": round(obs_auc, 4),
        "ci_lower": round(float(ci_lo), 4),
        "ci_upper": round(float(ci_hi), 4),
        "boot_std": round(float(np.std(boot_aucs)), 4),
        "n_valid_resamples": len(boot_aucs),
    }


# -- Permutation test ---------------------------------------------------

def permutation_test_auc(depths, probas, pair_i, pair_j,
                         n_permutations=500, seed=43):
    """Shuffle binary labels, report fraction of permuted AUC >= observed."""
    mask = (depths == pair_i) | (depths == pair_j)
    y = (depths[mask] == pair_j).astype(int)
    p_i = probas[mask, pair_i]
    p_j = probas[mask, pair_j]
    scores = p_j / (p_i + p_j + 1e-12)

    if len(np.unique(y)) < 2:
        return {"p_value": float("nan"), "obs_auc": float("nan")}

    obs_auc = roc_auc_score(y, scores)
    rng = np.random.default_rng(seed)
    count_ge = 0
    for _ in range(n_permutations):
        yp = rng.permutation(y)
        if len(np.unique(yp)) < 2:
            continue
        count_ge += (roc_auc_score(yp, scores) >= obs_auc)

    return {
        "obs_auc": round(float(obs_auc), 4),
        "p_value": round(count_ge / n_permutations, 4),
        "n_permutations": n_permutations,
    }


# -- Single dataset experiment ------------------------------------------

def run_one_dataset(embeddings, depths, doc_ids, label, data_dir, args, device):
    """MLP 5-fold CV + pairwise AUC + bootstrap CI + permutation test."""
    log.info(f"\n{'='*60}")
    log.info(f"Dataset: {label} ({data_dir})")
    log.info(f"{'='*60}")

    num_classes = int(depths.max()) + 1
    input_dim = embeddings.shape[1]
    log.info(f"Embeddings: {embeddings.shape}, classes: {num_classes}")

    gkf = GroupKFold(n_splits=5)
    all_probas = np.zeros((len(depths), num_classes))
    fold_adj_aucs = {f"{k-1}v{k}": [] for k in range(1, num_classes)}
    peak_vram_mb = []

    for fold, (tr_idx, te_idx) in enumerate(
        gkf.split(embeddings, depths, groups=doc_ids)
    ):
        log.info(f"  Fold {fold+1}/5  train={len(tr_idx)} test={len(te_idx)}")

        if torch.cuda.is_available():
            torch.cuda.reset_peak_memory_stats(device)

        mlp = train_mlp(
            embeddings[tr_idx], depths[tr_idx],
            embeddings[te_idx], depths[te_idx],
            input_dim=input_dim, num_classes=num_classes,
            epochs=args.epochs, lr=args.lr,
            batch_size=args.mlp_batch_size,
            patience=args.patience, device=device,
        )

        with torch.no_grad():
            logits = mlp(torch.tensor(embeddings[te_idx], dtype=torch.float32).to(device))
            probas = torch.softmax(logits, dim=-1).cpu().numpy()

        all_probas[te_idx] = probas

        td = depths[te_idx]
        for k in range(1, num_classes):
            m = (td == k - 1) | (td == k)
            y = (td[m] == k).astype(int)
            if len(np.unique(y)) < 2 or m.sum() < 4:
                continue
            p0 = probas[m, k - 1]
            p1 = probas[m, k]
            s = p1 / (p0 + p1 + 1e-12)
            fold_adj_aucs[f"{k-1}v{k}"].append(round(float(roc_auc_score(y, s)), 4))

        if torch.cuda.is_available():
            peak = torch.cuda.max_memory_allocated(device) / (1024 ** 2)
            peak_vram_mb.append(round(peak, 1))
            log.info(f"    Peak VRAM: {peak:.1f} MB")

        del mlp
        torch.cuda.empty_cache()

    # Overall pairwise AUC
    adj_auc, all_auc = compute_pairwise_auc(all_probas, depths, args.max_depth)

    # K*
    k_star = 0
    for k in range(1, num_classes):
        if adj_auc.get(f"{k-1}v{k}", 0) > 0.60:
            k_star = k

    accuracy = float((all_probas.argmax(axis=1) == depths).mean())

    # Per-fold stats
    fold_stats = {}
    for key, aucs in fold_adj_aucs.items():
        if aucs:
            fold_stats[key] = {
                "mean": round(float(np.mean(aucs)), 4),
                "std": round(float(np.std(aucs)), 4),
                "folds": aucs,
            }

    # Bootstrap CI
    log.info("  Computing bootstrap CI ...")
    bootstrap_results = {}
    for k in range(1, num_classes):
        pair = f"{k-1}v{k}"
        ci = bootstrap_auc_ci(
            depths, all_probas, k - 1, k, doc_ids,
            n_resamples=args.bootstrap_resamples,
        )
        bootstrap_results[pair] = ci
        log.info(f"    {pair}: AUC={ci['auc']}  95%CI=[{ci['ci_lower']}, {ci['ci_upper']}]")

    # Permutation test
    log.info("  Computing permutation tests ...")
    permutation_results = {}
    for k in range(1, num_classes):
        pair = f"{k-1}v{k}"
        pt = permutation_test_auc(
            depths, all_probas, k - 1, k,
            n_permutations=args.permutation_resamples,
        )
        permutation_results[pair] = pt
        pval_s = f"<{1/args.permutation_resamples}" if pt["p_value"] == 0 else f"{pt['p_value']:.4f}"
        log.info(f"    {pair}: p={pval_s}")

    # Load baseline
    baseline = None
    data_name = Path(data_dir).name
    results_name = data_name.replace("data_", "results_")
    baseline_path = Path(data_dir).parent / results_name / "pairwise_auc.json"
    if baseline_path.exists():
        with open(baseline_path) as f:
            baseline = json.load(f)
        log.info(f"  Loaded baseline from {baseline_path}")

    result = {
        "dataset": label,
        "data_dir": str(data_dir),
        "num_samples_per_depth": args.num_samples if args.num_samples else "all",
        "max_depth": args.max_depth,
        "embedding_dim": input_dim,
        "mlp_arch": f"{input_dim}->512->256->{num_classes}",
        "neural_probe": {
            "pairwise_auc_adjacent": adj_auc,
            "pairwise_auc_all": all_auc,
            "fold_stats": fold_stats,
            "k_star": k_star,
            "k_star_threshold": 0.60,
            "classification_accuracy": round(accuracy, 4),
            "bootstrap_ci": bootstrap_results,
            "permutation_test": permutation_results,
        },
        "peak_vram_mb": peak_vram_mb,
        "peak_vram_max_mb": max(peak_vram_mb) if peak_vram_mb else None,
    }
    if baseline:
        result["lgbm_baseline"] = {
            "pairwise_auc_adjacent": baseline["mean"],
            "k_star": max(
                (k for k in range(1, 6) if baseline["mean"].get(f"{k-1}v{k}", 0) > 0.60),
                default=0,
            ),
        }

    # Log summary
    log.info(f"\n  K* (neural probe) = {k_star}")
    log.info(f"  Accuracy = {accuracy:.4f}")
    if peak_vram_mb:
        log.info(f"  Peak VRAM (max across folds) = {max(peak_vram_mb):.1f} MB")
    for k in range(1, num_classes):
        key = f"{k-1}v{k}"
        a = adj_auc.get(key, "N/A")
        ci = bootstrap_results.get(key, {})
        ci_lo = ci.get("ci_lower", "?")
        ci_hi = ci.get("ci_upper", "?")
        pt = permutation_results.get(key, {})
        pv = pt.get("p_value", "?")
        base = baseline["mean"].get(key, "-") if baseline else "-"
        log.info(f"  AUC({key}): neural={a}  95%CI=[{ci_lo},{ci_hi}]  p={pv}  lgbm={base}")

    return result


# -- Main ---------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="exp-015: Neural Probe for depth classification (frozen LLM + MLP)",
    )
    parser.add_argument(
        "--model_path", type=str,
        default="/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B-Instruct/Qwen/Qwen2.5-1.5B-Instruct",
    )
    parser.add_argument("--data_dir", type=str, nargs="+",
                        default=["/root/autodl-tmp/gen-depth-contamination/data_exp017_qwen_cont"])
    parser.add_argument("--label", type=str, nargs="+", default=["Qwen-cont"])
    parser.add_argument(
        "--output", type=str,
        default="/root/autodl-tmp/gen-depth-contamination/artifacts/exp015_neural_probe_results.json",
    )
    parser.add_argument("--num_samples", type=int, default=None,
                        help="Max samples per depth (default: all)")
    parser.add_argument("--max_depth", type=int, default=5)
    parser.add_argument("--embed_batch_size", type=int, default=16)
    parser.add_argument("--max_length", type=int, default=512)
    parser.add_argument("--mlp_batch_size", type=int, default=256)
    parser.add_argument("--epochs", type=int, default=20)
    parser.add_argument("--lr", type=float, default=1e-3)
    parser.add_argument("--patience", type=int, default=5)
    parser.add_argument("--device", type=str, default="cuda:0")
    parser.add_argument("--bootstrap_resamples", type=int, default=1000)
    parser.add_argument("--permutation_resamples", type=int, default=500)
    args = parser.parse_args()

    if len(args.data_dir) != len(args.label):
        log.error("--data_dir and --label must have the same number of entries")
        sys.exit(1)

    device = args.device if torch.cuda.is_available() else "cpu"
    log.info(f"Device: {device}")
    if torch.cuda.is_available():
        props = torch.cuda.get_device_properties(0)
        log.info(f"GPU: {torch.cuda.get_device_name(0)} ({props.total_memory // 1024**3}GB)")

    # Phase 1: Load all text data (cheap, CPU only)
    dataset_info = []
    for dd, lab in zip(args.data_dir, args.label):
        texts, depths, doc_ids = load_depth_data(
            Path(dd), args.max_depth, args.num_samples,
        )
        if len(texts) == 0:
            log.error(f"No data in {dd}")
            continue
        dataset_info.append({
            "data_dir": dd, "label": lab,
            "texts": texts, "depths": depths, "doc_ids": doc_ids,
        })

    if not dataset_info:
        log.error("No valid datasets found")
        sys.exit(1)

    # Phase 2: Load LLM, extract embeddings for ALL datasets, then free LLM
    from transformers import AutoModelForCausalLM, AutoTokenizer

    log.info(f"Loading model from {args.model_path} ...")
    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
        tokenizer.pad_token_id = tokenizer.eos_token_id
    tokenizer.padding_side = "right"

    llm = AutoModelForCausalLM.from_pretrained(
        args.model_path,
        torch_dtype=torch.float16,
        device_map="auto",
        trust_remote_code=True,
    )
    llm.eval()
    log.info("Model loaded.")

    if torch.cuda.is_available():
        torch.cuda.reset_peak_memory_stats(device)

    for ds in dataset_info:
        log.info(f"Extracting embeddings for {ds['label']} ({len(ds['texts'])} samples) ...")
        emb, actual_bs = extract_embeddings(
            llm, tokenizer, ds["texts"],
            batch_size=args.embed_batch_size,
            max_length=args.max_length,
        )
        ds["embeddings"] = emb
        ds["actual_embed_bs"] = actual_bs
        log.info(f"  shape={emb.shape}")

    embed_peak = None
    if torch.cuda.is_available():
        embed_peak = torch.cuda.max_memory_allocated(device) / (1024 ** 2)
        log.info(f"Peak VRAM during embedding extraction: {embed_peak:.1f} MB")

    # Free LLM before MLP training — this is the key memory optimization
    del llm, tokenizer
    gc.collect()
    torch.cuda.empty_cache()
    if torch.cuda.is_available():
        post_free = torch.cuda.memory_allocated(device) / (1024 ** 2)
        log.info(f"VRAM after freeing LLM: {post_free:.1f} MB")

    # Phase 3: Train MLP probes (LLM no longer in memory)
    all_results = []
    for ds in dataset_info:
        r = run_one_dataset(
            ds["embeddings"], ds["depths"], ds["doc_ids"],
            ds["label"], ds["data_dir"], args, device,
        )
        if r:
            r["embed_batch_size_actual"] = ds["actual_embed_bs"]
            r["embed_peak_vram_mb"] = round(embed_peak, 1) if embed_peak else None
            all_results.append(r)

    # Save
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, "w") as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)
    log.info(f"\nResults -> {out}")

    # Final summary
    log.info("\n" + "=" * 60)
    log.info("SUMMARY")
    log.info("=" * 60)
    for r in all_results:
        np_ks = r["neural_probe"]["k_star"]
        base_ks = r.get("lgbm_baseline", {}).get("k_star", "-")
        log.info(f"  {r['dataset']:12s}  K*(neural)={np_ks}  K*(lgbm)={base_ks}  acc={r['neural_probe']['classification_accuracy']}")

        for pair, ci in r["neural_probe"]["bootstrap_ci"].items():
            pt = r["neural_probe"]["permutation_test"].get(pair, {})
            pv = pt.get("p_value", "?")
            pval_s = f"<{1/args.permutation_resamples}" if pv == 0 else f"{pv}"
            log.info(f"    {pair}: AUC={ci['auc']}  95%CI=[{ci['ci_lower']},{ci['ci_upper']}]  p={pval_s}")

    k_stars = [r["neural_probe"]["k_star"] for r in all_results]
    if len(k_stars) > 1:
        if all(k == k_stars[0] for k in k_stars):
            log.info(f"\n  Consistent K* = {k_stars[0]} across all datasets -> boundary is data-intrinsic")
        else:
            log.info(f"\n  K* varies: {k_stars}")


if __name__ == "__main__":
    main()
