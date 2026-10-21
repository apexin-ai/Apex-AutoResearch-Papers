"""exp-012: Binary Detector Confidence vs Generational Depth

Computes Binoculars score (CE ratio) and log-perplexity for each depth level
across all 4 datasets, then measures Spearman rho(score, true_depth).
Low rho supports the claim that binary detection != depth estimation.
"""

import argparse
import gc
import json
import logging
import os
import sys
from pathlib import Path

import numpy as np
import torch
from scipy import stats
from tqdm import tqdm

os.environ.setdefault("HF_HOME", "/root/autodl-tmp/.hf_cache")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)

DATASET_CONFIGS = {
    "qwen_rw": "data",
    "pythia": "data_exp001_pythia",
    "olmo": "data_exp002_olmo",
    "qwen_cont": "data_exp017_qwen_cont",
}


# ── Data loading ──────────────────────────────────────────────────────

def load_depth_texts(data_dir: Path, max_depth: int = 5, num_samples: int = None):
    depth_texts = {}
    for d in range(max_depth + 1):
        path = data_dir / f"depth_{d}.jsonl"
        if not path.exists():
            log.warning(f"Missing {path}, skipping depth {d}")
            continue
        texts = []
        with open(path) as f:
            for line in f:
                if num_samples is not None and len(texts) >= num_samples:
                    break
                texts.append(json.loads(line)["text"])
        depth_texts[d] = texts
        log.info(f"  depth {d}: {len(texts)} samples")
    return depth_texts


# ── Model loading ─────────────────────────────────────────────────────

def load_model_and_tokenizer(model_path, device="cpu", dtype=torch.float32):
    from transformers import AutoModelForCausalLM, AutoTokenizer

    log.info(f"Loading {model_path} → {device} ({dtype})")
    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    kwargs = {"torch_dtype": dtype, "trust_remote_code": True}
    if device == "cuda":
        kwargs["device_map"] = "auto"

    model = AutoModelForCausalLM.from_pretrained(model_path, **kwargs)
    if device == "cpu":
        model = model.to("cpu")
    model.eval()
    return model, tokenizer


# ── Scoring ───────────────────────────────────────────────────────────

@torch.no_grad()
def compute_cross_entropy(model, tokenizer, texts, batch_size=8, max_length=512):
    """Mean per-token cross-entropy for each text."""
    all_ce = []
    device = next(model.parameters()).device

    for start in tqdm(range(0, len(texts), batch_size), desc="CE", leave=False):
        batch = texts[start : start + batch_size]
        inputs = tokenizer(
            batch,
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=max_length,
        ).to(device)

        logits = model(**inputs).logits
        shift_logits = logits[:, :-1, :].contiguous()
        shift_labels = inputs["input_ids"][:, 1:].contiguous()
        shift_mask = inputs["attention_mask"][:, 1:].contiguous()

        loss_fn = torch.nn.CrossEntropyLoss(reduction="none")
        ce = loss_fn(
            shift_logits.view(-1, shift_logits.size(-1)),
            shift_labels.view(-1),
        ).view(shift_labels.shape)

        for i in range(len(batch)):
            mask_i = shift_mask[i].bool()
            if mask_i.sum() == 0:
                all_ce.append(float("nan"))
            else:
                all_ce.append(ce[i][mask_i].mean().item())

        del logits, shift_logits, ce, inputs
        if device.type == "cuda":
            torch.cuda.empty_cache()

    return np.array(all_ce)


def compute_binoculars_scores(
    observer_model, performer_model,
    tokenizer_obs, tokenizer_perf,
    texts, batch_size=8, max_length=512,
):
    """Binoculars score = CE(observer) / CE(performer)."""
    log.info("  → observer CE")
    ce_obs = compute_cross_entropy(observer_model, tokenizer_obs, texts, batch_size, max_length)
    log.info("  → performer CE")
    ce_perf = compute_cross_entropy(performer_model, tokenizer_perf, texts, batch_size, max_length)

    valid = (ce_perf > 0) & ~np.isnan(ce_obs) & ~np.isnan(ce_perf)
    scores = np.full(len(texts), float("nan"))
    scores[valid] = ce_obs[valid] / ce_perf[valid]
    return scores


def compute_log_perplexity(model, tokenizer, texts, batch_size=8, max_length=512):
    """Log-perplexity = mean per-token CE."""
    return compute_cross_entropy(model, tokenizer, texts, batch_size, max_length)


# ── Analysis ──────────────────────────────────────────────────────────

def spearman_from_depth_scores(per_depth_scores):
    depths, scores = [], []
    for d in sorted(per_depth_scores):
        for s in per_depth_scores[d]:
            if not np.isnan(s):
                depths.append(d)
                scores.append(s)
    if len(depths) < 3:
        return float("nan"), float("nan")
    rho, p = stats.spearmanr(depths, scores)
    return float(rho), float(p)


def analyze_dataset(
    ds_name, depth_texts,
    observer_model, performer_model,
    tokenizer_obs, tokenizer_perf,
    batch_size, max_length,
):
    log.info(f"\n{'=' * 60}")
    log.info(f"Dataset: {ds_name}")
    log.info(f"{'=' * 60}")

    bino_by_depth, ppl_by_depth = {}, {}

    for d in sorted(depth_texts):
        texts = depth_texts[d]
        log.info(f"\n--- Depth {d} ({len(texts)} samples) ---")

        bino = compute_binoculars_scores(
            observer_model, performer_model,
            tokenizer_obs, tokenizer_perf,
            texts, batch_size, max_length,
        )
        bino_by_depth[d] = bino

        ppl = compute_log_perplexity(
            performer_model, tokenizer_perf,
            texts, batch_size, max_length,
        )
        ppl_by_depth[d] = ppl

        bv = bino[~np.isnan(bino)]
        pv = ppl[~np.isnan(ppl)]
        log.info(f"  Binoculars: {np.mean(bv):.4f} ± {np.std(bv):.4f}")
        log.info(f"  Log-PPL:    {np.mean(pv):.4f} ± {np.std(pv):.4f}")

    bino_rho, bino_p = spearman_from_depth_scores(bino_by_depth)
    ppl_rho, ppl_p = spearman_from_depth_scores(ppl_by_depth)

    log.info(f"\nSpearman ρ — Binoculars: {bino_rho:.4f} (p={bino_p:.2e})")
    log.info(f"Spearman ρ — Log-PPL:    {ppl_rho:.4f} (p={ppl_p:.2e})")

    result = {
        "binoculars": {
            "spearman_rho": bino_rho,
            "p_value": bino_p,
            "per_depth_mean": [float(np.nanmean(bino_by_depth[d])) for d in sorted(bino_by_depth)],
            "per_depth_std": [float(np.nanstd(bino_by_depth[d])) for d in sorted(bino_by_depth)],
        },
        "log_perplexity": {
            "spearman_rho": ppl_rho,
            "p_value": ppl_p,
            "per_depth_mean": [float(np.nanmean(ppl_by_depth[d])) for d in sorted(ppl_by_depth)],
            "per_depth_std": [float(np.nanstd(ppl_by_depth[d])) for d in sorted(ppl_by_depth)],
        },
    }
    return result, bino_by_depth, ppl_by_depth


# ── Visualization ─────────────────────────────────────────────────────

def plot_boxplots(all_bino, all_ppl, dataset_names, output_path):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    n = len(dataset_names)
    fig, axes = plt.subplots(n, 2, figsize=(14, 4 * n), squeeze=False)

    for row, ds in enumerate(dataset_names):
        depths = sorted(all_bino[ds])

        ax = axes[row][0]
        ax.boxplot(
            [all_bino[ds][d][~np.isnan(all_bino[ds][d])] for d in depths],
            labels=[str(d) for d in depths],
            showfliers=False,
        )
        ax.set_title(f"{ds} — Binoculars")
        ax.set_xlabel("Depth")
        ax.set_ylabel("CE(obs) / CE(perf)")

        ax = axes[row][1]
        ax.boxplot(
            [all_ppl[ds][d][~np.isnan(all_ppl[ds][d])] for d in depths],
            labels=[str(d) for d in depths],
            showfliers=False,
        )
        ax.set_title(f"{ds} — Log-Perplexity")
        ax.set_xlabel("Depth")
        ax.set_ylabel("Mean per-token CE")

    plt.tight_layout()
    plt.savefig(output_path, bbox_inches="tight")
    plt.close()
    log.info(f"Saved boxplot → {output_path}")


# ── Main ──────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="exp-012: binary confidence vs depth")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--batch-size", type=int, default=8)
    parser.add_argument("--max-length", type=int, default=512)
    parser.add_argument("--data-dirs", nargs="+", default=None)
    parser.add_argument("--observer-model", type=str, default=None)
    parser.add_argument("--performer-model", type=str, default=None)
    parser.add_argument("--device", type=str, default=None)
    parser.add_argument("--project-root", type=str, default=".")
    args = parser.parse_args()

    root = Path(args.project_root)
    artifacts_dir = root / "artifacts"
    artifacts_dir.mkdir(exist_ok=True)

    if args.device:
        device = args.device
    elif torch.cuda.is_available():
        device = "cuda"
    else:
        device = "cpu"
    dtype = torch.float16 if device == "cuda" else torch.float32
    log.info(f"Device: {device}, dtype: {dtype}")

    if args.dry_run:
        log.info("*** DRY RUN: 10 samples per depth ***")

    default_model = "Qwen/Qwen2.5-1.5B-Instruct"
    observer_path = args.observer_model or default_model
    performer_path = args.performer_model or default_model
    log.info(f"Observer:  {observer_path}")
    log.info(f"Performer: {performer_path}")

    same_model = observer_path == performer_path
    performer_model, tok_perf = load_model_and_tokenizer(performer_path, device, dtype)
    if same_model:
        log.info("Observer == Performer (Binoculars ratio ≈ 1.0 — use different models for real run)")
        observer_model, tok_obs = performer_model, tok_perf
    else:
        observer_model, tok_obs = load_model_and_tokenizer(observer_path, device, dtype)

    if args.data_dirs:
        ds_configs = {d: d for d in args.data_dirs}
    else:
        ds_configs = DATASET_CONFIGS

    num_samples = 10 if args.dry_run else None

    results = {
        "method": "Binoculars + log-perplexity as binary detection baselines",
        "observer_model": observer_path,
        "performer_model": performer_path,
        "dry_run": args.dry_run,
        "datasets": {},
    }
    all_bino, all_ppl = {}, {}
    output_json = artifacts_dir / "exp012_binary_confidence.json"

    for ds_name, ds_dir_name in ds_configs.items():
        ds_dir = root / ds_dir_name
        if not ds_dir.exists():
            log.warning(f"Data dir {ds_dir} not found, skipping {ds_name}")
            continue

        depth_texts = load_depth_texts(ds_dir, num_samples=num_samples)
        ds_result, bino_data, ppl_data = analyze_dataset(
            ds_name, depth_texts,
            observer_model, performer_model,
            tok_obs, tok_perf,
            args.batch_size, args.max_length,
        )
        results["datasets"][ds_name] = ds_result
        all_bino[ds_name] = bino_data
        all_ppl[ds_name] = ppl_data

        with open(output_json, "w") as f:
            json.dump(results, f, indent=2)
        log.info(f"Checkpoint → {output_json}")

    # Aggregate Spearman
    agg_d_bino, agg_s_bino = [], []
    agg_d_ppl, agg_s_ppl = [], []
    for ds_name in results["datasets"]:
        for d in sorted(all_bino[ds_name]):
            for s in all_bino[ds_name][d]:
                if not np.isnan(s):
                    agg_d_bino.append(d)
                    agg_s_bino.append(s)
            for s in all_ppl[ds_name][d]:
                if not np.isnan(s):
                    agg_d_ppl.append(d)
                    agg_s_ppl.append(s)

    agg_bino = float(stats.spearmanr(agg_d_bino, agg_s_bino).statistic) if len(agg_d_bino) >= 3 else float("nan")
    agg_ppl = float(stats.spearmanr(agg_d_ppl, agg_s_ppl).statistic) if len(agg_d_ppl) >= 3 else float("nan")

    results["aggregate_spearman"] = {
        "binoculars": agg_bino,
        "log_perplexity": agg_ppl,
    }

    with open(output_json, "w") as f:
        json.dump(results, f, indent=2)
    log.info(f"Final results → {output_json}")

    if all_bino:
        plot_path = artifacts_dir / "exp012_binary_confidence_boxplot.pdf"
        plot_boxplots(all_bino, all_ppl, list(all_bino.keys()), plot_path)

    log.info(f"\n{'=' * 60}")
    log.info("SUMMARY")
    log.info(f"{'=' * 60}")
    for ds_name, ds_res in results["datasets"].items():
        log.info(f"  {ds_name}: Bino ρ={ds_res['binoculars']['spearman_rho']:.4f}, PPL ρ={ds_res['log_perplexity']['spearman_rho']:.4f}")
    log.info(f"  Aggregate: Bino ρ={agg_bino:.4f}, PPL ρ={agg_ppl:.4f}")


if __name__ == "__main__":
    main()
