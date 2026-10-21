"""
Correlation Analysis: rho(CKA overlap, RLVR recoverability).

Tests the MVP hypothesis: pruned heads with higher CKA overlap F(h) are more
effectively compensated by RLVR through their most similar retained head.

Metric: for each pruned head h_p, find the most CKA-similar retained head h_r,
then measure h_r's activation shift between pruned model and RLVR-recovered model.
"""

import argparse
import json
import logging
import os
import random

import numpy as np
import scipy.stats as stats
import torch
import torch.nn.functional as F
from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)


def set_seed(seed: int):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


def load_calibration_data(tokenizer, n_samples: int, max_length: int = 512, seed: int = 42):
    ds = load_dataset("openai/gsm8k", "main", split="train")
    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))
    encodings = []
    for example in ds:
        prompt = f"Question: {example['question']}\nAnswer: Let me think step by step.\n"
        ids = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=max_length)
        encodings.append(ids)
    return encodings


def load_pruned_model(base_model_path, saved_model_path, pruning_meta, torch_dtype, device):
    """Load a structurally pruned model by reconstructing from base model + saved weights."""
    logging.getLogger("prune").setLevel(logging.WARNING)
    from prune import prune_attention_heads, prune_mlp_channels

    model = AutoModelForCausalLM.from_pretrained(
        base_model_path, torch_dtype=torch_dtype, device_map="cpu", trust_remote_code=True
    )
    prune_attention_heads(model, pruning_meta["attn_keep_masks"])
    prune_mlp_channels(model, pruning_meta["mlp_keep_masks"])

    safetensor_files = sorted(
        [f for f in os.listdir(saved_model_path) if f.endswith(".safetensors")]
    )
    if safetensor_files:
        from safetensors.torch import load_file
        state_dict = {}
        for f in safetensor_files:
            state_dict.update(load_file(os.path.join(saved_model_path, f)))
    else:
        state_dict = torch.load(
            os.path.join(saved_model_path, "pytorch_model.bin"),
            map_location="cpu", weights_only=True,
        )

    model.load_state_dict(state_dict)
    model.to(device)
    return model


def collect_retained_head_activations(model, calibration_data, keep_masks, device):
    """Collect per-head q_proj activations (mean-pooled over seq_len).

    Returns dict[layer_idx] -> tensor[n_samples, n_retained_heads, head_dim]
    """
    n_layers = model.config.num_hidden_layers
    head_dim = model.config.hidden_size // model.config.num_attention_heads

    q_outputs = {i: [] for i in range(n_layers)}
    hooks = []

    def make_hook(layer_idx):
        def fn(module, inp, out):
            q_outputs[layer_idx].append(out.detach().cpu())
        return fn

    for i in range(n_layers):
        h = model.model.layers[i].self_attn.q_proj.register_forward_hook(make_hook(i))
        hooks.append(h)

    model.eval()
    with torch.no_grad():
        for idx, enc in enumerate(calibration_data):
            input_ids = enc["input_ids"].to(device)
            attention_mask = enc["attention_mask"].to(device)
            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)
            if (idx + 1) % 50 == 0:
                logger.info(f"  Processed {idx + 1}/{len(calibration_data)} samples")

    for h in hooks:
        h.remove()

    activations = {}
    for layer_idx in range(n_layers):
        n_retained = len(keep_masks[layer_idx])
        per_head = []
        for t in q_outputs[layer_idx]:
            t = t.squeeze(0)  # [seq, n_retained * head_dim]
            t = t.view(t.shape[0], n_retained, head_dim)  # [seq, n_retained, head_dim]
            t = t.mean(dim=0)  # [n_retained, head_dim]
            per_head.append(t)
        activations[layer_idx] = torch.stack(per_head, dim=0).float()
        q_outputs[layer_idx] = None

    return activations


def compute_recoverability(pruned_acts, recovered_acts, cka_data, keep_masks,
                           n_heads_original=28):
    """Compute per-pruned-head recoverability as activation shift of best retained head."""
    attn_overlap = cka_data["attn_overlap"]
    attn_cka_matrix = cka_data["attn_cka_matrix"]
    results = []

    for layer_idx in range(len(keep_masks)):
        retained = keep_masks[layer_idx]
        pruned_heads = sorted(set(range(n_heads_original)) - set(retained))
        if not pruned_heads:
            continue

        cka_matrix = attn_cka_matrix[layer_idx]

        for h_p in pruned_heads:
            sims = torch.tensor([cka_matrix[h_p, h_r].item() for h_r in retained])
            best_idx = sims.argmax().item()
            h_r = retained[best_idx]
            h_r_local = retained.index(h_r)

            act_p = pruned_acts[layer_idx][:, h_r_local, :]
            act_r = recovered_acts[layer_idx][:, h_r_local, :]
            cos_sim = F.cosine_similarity(act_p, act_r, dim=-1)
            activation_shift = 1.0 - cos_sim.mean().item()

            results.append({
                "layer": layer_idx,
                "pruned_head": h_p,
                "best_retained_head": h_r,
                "cka_overlap": attn_overlap[layer_idx][h_p].item(),
                "recoverability": activation_shift,
                "cka_similarity_to_retained": sims[best_idx].item(),
            })

    return results


def bootstrap_spearman(x, y, n_bootstrap=10000, seed=42):
    rng = np.random.RandomState(seed)
    x, y = np.array(x), np.array(y)
    n = len(x)
    rhos = []
    for _ in range(n_bootstrap):
        idx = rng.choice(n, n, replace=True)
        r, _ = stats.spearmanr(x[idx], y[idx])
        if not np.isnan(r):
            rhos.append(r)
    return np.percentile(rhos, [2.5, 97.5]).tolist()


def permutation_test(x, y, n_perm=10000, seed=42):
    rng = np.random.RandomState(seed)
    x, y = np.array(x), np.array(y)
    observed, _ = stats.spearmanr(x, y)
    count = 0
    for _ in range(n_perm):
        r, _ = stats.spearmanr(x, rng.permutation(y))
        if abs(r) >= abs(observed):
            count += 1
    return count / n_perm


def make_scatter_plot(results, rho, p_value, ci, perm_p, output_path):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        logger.warning("matplotlib not available, skipping scatter plot")
        return

    fh = [r["cka_overlap"] for r in results]
    rec = [r["recoverability"] for r in results]
    layers = [r["layer"] for r in results]

    fig, ax = plt.subplots(figsize=(8, 6))
    sc = ax.scatter(fh, rec, c=layers, cmap="viridis", alpha=0.7,
                    edgecolors="k", linewidths=0.3, s=30)
    plt.colorbar(sc, ax=ax, label="Layer index")
    ax.set_xlabel("F(h_p) — CKA overlap of pruned head")
    ax.set_ylabel("Recoverability — activation shift of best retained head")

    verdict = "PASS" if rho >= 0.4 else ("WARNING" if rho >= 0.3 else "FAIL")
    ax.set_title(
        f"CKA Overlap vs RLVR Recoverability\n"
        f"ρ={rho:.3f}, 95% CI=[{ci[0]:.3f}, {ci[1]:.3f}], "
        f"p={p_value:.1e}, perm_p={perm_p:.1e} — {verdict}"
    )
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()
    logger.info(f"Scatter plot saved to {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Correlation analysis: rho(CKA overlap, RLVR recoverability)"
    )
    parser.add_argument("--base_model_path", required=True,
                        help="Path to original unpruned model")
    parser.add_argument("--pruned_model_path", required=True,
                        help="Path to pruned model (before RLVR)")
    parser.add_argument("--recovered_model_path", required=True,
                        help="Path to RLVR-recovered model")
    parser.add_argument("--cka_scores_path", required=True,
                        help="CKA overlap scores (cka_scores.pt, must contain attn_cka_matrix)")
    parser.add_argument("--pruning_mask_path", required=True,
                        help="Pruning metadata (pruning_metadata.pt with attn_keep_masks)")
    parser.add_argument("--n_samples", type=int, default=256,
                        help="Number of calibration samples")
    parser.add_argument("--output_dir", default="results/analysis/",
                        help="Output directory")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--dtype", type=str, default="bfloat16",
                        choices=["float16", "bfloat16", "float32"])
    args = parser.parse_args()

    set_seed(args.seed)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    torch_dtype = {"float16": torch.float16, "bfloat16": torch.bfloat16,
                   "float32": torch.float32}[args.dtype]

    logger.info("Loading CKA scores...")
    cka_data = torch.load(args.cka_scores_path, map_location="cpu", weights_only=True)
    if "attn_cka_matrix" not in cka_data:
        raise ValueError(
            "CKA scores missing 'attn_cka_matrix'. "
            "Re-run cka_overlap.py to generate pairwise CKA matrices."
        )

    logger.info("Loading pruning metadata...")
    pruning_meta = torch.load(args.pruning_mask_path, map_location="cpu",
                              weights_only=True)
    keep_masks = pruning_meta["attn_keep_masks"]

    tokenizer = AutoTokenizer.from_pretrained(args.base_model_path, trust_remote_code=True)
    calibration_data = load_calibration_data(tokenizer, args.n_samples, seed=args.seed)
    logger.info(f"Loaded {len(calibration_data)} calibration samples")

    logger.info(f"Loading pruned model from {args.pruned_model_path}")
    pruned_model = load_pruned_model(
        args.base_model_path, args.pruned_model_path, pruning_meta, torch_dtype, device
    )
    logger.info("Collecting activations from pruned model...")
    pruned_acts = collect_retained_head_activations(
        pruned_model, calibration_data, keep_masks, device
    )
    del pruned_model
    torch.cuda.empty_cache()

    logger.info(f"Loading recovered model from {args.recovered_model_path}")
    recovered_model = load_pruned_model(
        args.base_model_path, args.recovered_model_path, pruning_meta, torch_dtype, device
    )
    logger.info("Collecting activations from recovered model...")
    recovered_acts = collect_retained_head_activations(
        recovered_model, calibration_data, keep_masks, device
    )
    del recovered_model
    torch.cuda.empty_cache()

    logger.info("Computing recoverability scores...")
    n_heads = 28
    results = compute_recoverability(
        pruned_acts, recovered_acts, cka_data, keep_masks, n_heads
    )
    del pruned_acts, recovered_acts
    logger.info(f"Computed recoverability for {len(results)} pruned heads")

    fh = [r["cka_overlap"] for r in results]
    rec = [r["recoverability"] for r in results]
    rho, p_value = stats.spearmanr(fh, rec)
    ci = bootstrap_spearman(fh, rec, seed=args.seed)
    perm_p = permutation_test(fh, rec, seed=args.seed)

    verdict = "PASS" if rho >= 0.4 else ("WARNING" if rho >= 0.3 else "FAIL")

    os.makedirs(args.output_dir, exist_ok=True)
    output = {
        "spearman_rho": rho,
        "p_value": p_value,
        "bootstrap_ci_95": ci,
        "permutation_p_value": perm_p,
        "n_pruned_heads": len(results),
        "mvp_verdict": verdict,
        "per_head_data": results,
    }
    json_path = os.path.join(args.output_dir, "correlation_results.json")
    with open(json_path, "w") as f:
        json.dump(output, f, indent=2)
    logger.info(f"Results saved to {json_path}")

    plot_path = os.path.join(args.output_dir, "fh_vs_recoverability.png")
    make_scatter_plot(results, rho, p_value, ci, perm_p, plot_path)

    print(f"\n{'='*50}")
    print("MVP Correlation Analysis Results")
    print(f"{'='*50}")
    print(f"Spearman rho:      {rho:.4f}")
    print(f"p-value:           {p_value:.2e}")
    print(f"95% CI:            [{ci[0]:.4f}, {ci[1]:.4f}]")
    print(f"Permutation p:     {perm_p:.4f}")
    print(f"N pruned heads:    {len(results)}")
    print(f"MVP Verdict:       {verdict}")
    print(f"{'='*50}")


if __name__ == "__main__":
    main()
