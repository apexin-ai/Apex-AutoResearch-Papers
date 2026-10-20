"""
Correlation Analysis: rho(CKA overlap, RLVR recoverability).

Tests the hypothesis: pruned structures (GQA groups or MLP channel groups) with
higher CKA overlap F(g) are more effectively compensated by RLVR through their
most similar retained structure.

Metric: for each pruned structure g_p, find the most CKA-similar retained
structure g_r, then measure g_r's activation shift between pruned and
RLVR-recovered models.
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


def collect_all_activations(model, calibration_data, attn_keep_masks, mlp_keep_masks, device):
    """Collect both GQA-group and MLP-group activations in a single forward pass.

    Returns:
        attn_acts: dict[layer_idx] -> tensor[n_samples, n_retained_gqa, heads_per_kv * head_dim]
        mlp_acts:  dict[layer_idx] -> tensor[n_samples, n_retained_mlp, group_size]
    """
    config = model.config
    n_layers = config.num_hidden_layers
    n_heads = config.num_attention_heads
    n_kv_heads = config.num_key_value_heads
    head_dim = config.hidden_size // n_heads
    heads_per_kv = n_heads // n_kv_heads

    q_outputs = {i: [] for i in range(n_layers)}
    gate_outputs = {i: [] for i in range(n_layers)}
    hooks = []

    def make_q_hook(layer_idx):
        def fn(module, inp, out):
            q_outputs[layer_idx].append(out.detach().cpu())
        return fn

    def make_gate_hook(layer_idx):
        def fn(module, inp, out):
            gate_outputs[layer_idx].append(out.detach().cpu())
        return fn

    for i in range(n_layers):
        h1 = model.model.layers[i].self_attn.q_proj.register_forward_hook(make_q_hook(i))
        h2 = model.model.layers[i].mlp.gate_proj.register_forward_hook(make_gate_hook(i))
        hooks.extend([h1, h2])

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

    attn_activations = {}
    for layer_idx in range(n_layers):
        n_retained_gqa = len(attn_keep_masks[layer_idx])
        per_group = []
        for t in q_outputs[layer_idx]:
            t = t.squeeze(0)  # [seq, n_retained_gqa * heads_per_kv * head_dim]
            t = t.view(t.shape[0], n_retained_gqa, heads_per_kv, head_dim)
            t = t.view(t.shape[0], n_retained_gqa, heads_per_kv * head_dim)
            t = t.mean(dim=0)  # [n_retained_gqa, heads_per_kv * head_dim]
            per_group.append(t)
        attn_activations[layer_idx] = torch.stack(per_group, dim=0).float()
        q_outputs[layer_idx] = None

    mlp_activations = {}
    for layer_idx in range(n_layers):
        n_retained = len(mlp_keep_masks[layer_idx])
        per_group = []
        for t in gate_outputs[layer_idx]:
            t = t.squeeze(0)  # [seq, n_retained * group_size]
            total_channels = t.shape[-1]
            group_size = total_channels // n_retained
            usable = n_retained * group_size
            t = t[:, :usable].view(t.shape[0], n_retained, group_size)
            t = t.mean(dim=0)  # [n_retained, group_size]
            per_group.append(t)
        mlp_activations[layer_idx] = torch.stack(per_group, dim=0).float()
        gate_outputs[layer_idx] = None

    return attn_activations, mlp_activations


def compute_attn_recoverability(pruned_acts, recovered_acts, cka_data, attn_keep_masks,
                                n_gqa_groups_original):
    attn_overlap = cka_data["attn_overlap"]
    attn_cka_matrix = cka_data["attn_cka_matrix"]
    results = []

    for layer_idx in sorted(attn_keep_masks.keys()):
        retained = attn_keep_masks[layer_idx]
        pruned_groups = sorted(set(range(n_gqa_groups_original)) - set(retained))
        if not pruned_groups:
            continue

        cka_matrix = attn_cka_matrix[layer_idx]

        for g_p in pruned_groups:
            sims = torch.tensor([cka_matrix[g_p, g_r].item() for g_r in retained])
            best_idx = sims.argmax().item()
            g_r = retained[best_idx]
            g_r_local = retained.index(g_r)

            act_p = pruned_acts[layer_idx][:, g_r_local, :]
            act_r = recovered_acts[layer_idx][:, g_r_local, :]
            cos_sim = F.cosine_similarity(act_p, act_r, dim=-1)
            activation_shift = 1.0 - cos_sim.mean().item()

            results.append({
                "layer": layer_idx,
                "type": "attention",
                "pruned_group": g_p,
                "best_retained_group": g_r,
                "cka_overlap": attn_overlap[layer_idx][g_p].item(),
                "recoverability": activation_shift,
                "cka_similarity_to_retained": sims[best_idx].item(),
            })

    return results


def compute_mlp_recoverability(pruned_acts, recovered_acts, cka_data, mlp_keep_masks,
                               n_mlp_groups_original):
    mlp_overlap = cka_data["mlp_overlap"]
    mlp_cka_matrix = cka_data["mlp_cka_matrix"]
    results = []

    for layer_idx in sorted(mlp_keep_masks.keys()):
        retained = mlp_keep_masks[layer_idx]
        pruned_groups = sorted(set(range(n_mlp_groups_original)) - set(retained))
        if not pruned_groups:
            continue

        cka_matrix = mlp_cka_matrix[layer_idx]

        for m_p in pruned_groups:
            sims = torch.tensor([cka_matrix[m_p, m_r].item() for m_r in retained])
            best_idx = sims.argmax().item()
            m_r = retained[best_idx]
            m_r_local = retained.index(m_r)

            act_p = pruned_acts[layer_idx][:, m_r_local, :]
            act_r = recovered_acts[layer_idx][:, m_r_local, :]
            cos_sim = F.cosine_similarity(act_p, act_r, dim=-1)
            activation_shift = 1.0 - cos_sim.mean().item()

            results.append({
                "layer": layer_idx,
                "type": "mlp",
                "pruned_group": m_p,
                "best_retained_group": m_r,
                "cka_overlap": mlp_overlap[layer_idx][m_p].item(),
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


def compute_correlation_stats(fh, rec, seed=42):
    if len(fh) < 3:
        return {
            "spearman_rho": float("nan"), "p_value": float("nan"),
            "bootstrap_ci_95": [float("nan"), float("nan")],
            "permutation_p_value": float("nan"),
            "n_pruned_groups": len(fh),
        }
    rho, p_value = stats.spearmanr(fh, rec)
    ci = bootstrap_spearman(fh, rec, seed=seed)
    perm_p = permutation_test(fh, rec, seed=seed)
    return {
        "spearman_rho": rho, "p_value": p_value,
        "bootstrap_ci_95": ci, "permutation_p_value": perm_p,
        "n_pruned_groups": len(fh),
    }


def make_scatter_plot(results, stat, output_path, title_prefix="", color_by_type=False):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        logger.warning("matplotlib not available, skipping scatter plot")
        return

    fh = [r["cka_overlap"] for r in results]
    rec = [r["recoverability"] for r in results]
    rho = stat["spearman_rho"]
    p_value = stat["p_value"]
    ci = stat["bootstrap_ci_95"]
    perm_p = stat.get("permutation_p_value", float("nan"))

    fig, ax = plt.subplots(figsize=(8, 6))

    if color_by_type:
        type_colors = {"attention": "#1f77b4", "mlp": "#ff7f0e"}
        for stype, color in type_colors.items():
            mask = [r["type"] == stype for r in results]
            x = [f for f, m in zip(fh, mask) if m]
            y = [r for r, m in zip(rec, mask) if m]
            if x:
                ax.scatter(x, y, c=color, alpha=0.7, edgecolors="k",
                           linewidths=0.3, s=30, label=stype)
        ax.legend()
    else:
        layers = [r["layer"] for r in results]
        sc = ax.scatter(fh, rec, c=layers, cmap="viridis", alpha=0.7,
                        edgecolors="k", linewidths=0.3, s=30)
        plt.colorbar(sc, ax=ax, label="Layer index")

    ax.set_xlabel("F(g) — CKA overlap of pruned structure")
    ax.set_ylabel("Recoverability — activation shift of best retained structure")

    verdict = "PASS" if rho >= 0.4 else ("WARNING" if rho >= 0.3 else "FAIL")
    ax.set_title(
        f"{title_prefix}CKA Overlap vs RLVR Recoverability\n"
        f"ρ={rho:.3f}, 95% CI=[{ci[0]:.3f}, {ci[1]:.3f}], "
        f"p={p_value:.1e}, perm_p={perm_p:.1e} — {verdict}"
    )
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()
    logger.info(f"Scatter plot saved to {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Correlation analysis: rho(CKA overlap, RLVR recoverability) "
                    "for attention GQA groups and MLP channel groups"
    )
    parser.add_argument("--base_model_path", required=True,
                        help="Path to original unpruned model")
    parser.add_argument("--pruned_model_path", required=True,
                        help="Path to pruned model (before RLVR)")
    parser.add_argument("--recovered_model_path", required=True,
                        help="Path to RLVR-recovered model")
    parser.add_argument("--cka_scores_path", required=True,
                        help="Path to CKA overlap .pt file")
    parser.add_argument("--pruning_mask_path", required=True,
                        help="Path to pruning_metadata.pt")
    parser.add_argument("--n_samples", type=int, default=128,
                        help="Number of calibration samples")
    parser.add_argument("--n_gqa_groups", type=int, default=4,
                        help="Number of original GQA groups (KV heads) per layer")
    parser.add_argument("--n_mlp_groups", type=int, default=28,
                        help="Number of original MLP channel groups per layer")
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
    for key in ("attn_cka_matrix", "mlp_cka_matrix"):
        if key not in cka_data:
            raise ValueError(f"CKA scores missing '{key}'. Re-run cka_overlap.py.")

    logger.info("Loading pruning metadata...")
    pruning_meta = torch.load(args.pruning_mask_path, map_location="cpu",
                              weights_only=True)
    attn_keep_masks = pruning_meta["attn_keep_masks"]
    mlp_keep_masks = pruning_meta["mlp_keep_masks"]

    tokenizer = AutoTokenizer.from_pretrained(args.base_model_path, trust_remote_code=True)
    calibration_data = load_calibration_data(tokenizer, args.n_samples, seed=args.seed)
    logger.info(f"Loaded {len(calibration_data)} calibration samples")

    # --- Pruned model ---
    logger.info(f"Loading pruned model from {args.pruned_model_path}")
    pruned_model = load_pruned_model(
        args.base_model_path, args.pruned_model_path, pruning_meta, torch_dtype, device
    )
    logger.info("Collecting activations from pruned model...")
    pruned_attn_acts, pruned_mlp_acts = collect_all_activations(
        pruned_model, calibration_data, attn_keep_masks, mlp_keep_masks, device
    )
    del pruned_model
    torch.cuda.empty_cache()

    # --- Recovered model ---
    logger.info(f"Loading recovered model from {args.recovered_model_path}")
    recovered_model = load_pruned_model(
        args.base_model_path, args.recovered_model_path, pruning_meta, torch_dtype, device
    )
    logger.info("Collecting activations from recovered model...")
    recovered_attn_acts, recovered_mlp_acts = collect_all_activations(
        recovered_model, calibration_data, attn_keep_masks, mlp_keep_masks, device
    )
    del recovered_model
    torch.cuda.empty_cache()

    # --- Attention recoverability ---
    logger.info("Computing attention recoverability...")
    attn_results = compute_attn_recoverability(
        pruned_attn_acts, recovered_attn_acts, cka_data,
        attn_keep_masks, args.n_gqa_groups,
    )
    del pruned_attn_acts, recovered_attn_acts
    logger.info(f"Computed recoverability for {len(attn_results)} pruned GQA groups")

    # --- MLP recoverability ---
    logger.info("Computing MLP recoverability...")
    mlp_results = compute_mlp_recoverability(
        pruned_mlp_acts, recovered_mlp_acts, cka_data,
        mlp_keep_masks, args.n_mlp_groups,
    )
    del pruned_mlp_acts, recovered_mlp_acts
    logger.info(f"Computed recoverability for {len(mlp_results)} pruned MLP groups")

    # --- Statistics ---
    attn_fh = [r["cka_overlap"] for r in attn_results]
    attn_rec = [r["recoverability"] for r in attn_results]
    attn_stats = compute_correlation_stats(attn_fh, attn_rec, seed=args.seed)

    mlp_fh = [r["cka_overlap"] for r in mlp_results]
    mlp_rec = [r["recoverability"] for r in mlp_results]
    mlp_stats = compute_correlation_stats(mlp_fh, mlp_rec, seed=args.seed)

    combined_results = attn_results + mlp_results
    combined_fh = [r["cka_overlap"] for r in combined_results]
    combined_rec = [r["recoverability"] for r in combined_results]
    combined_stats = compute_correlation_stats(combined_fh, combined_rec, seed=args.seed)
    combined_stats["n_total_pruned"] = len(combined_results)

    combined_rho = combined_stats["spearman_rho"]
    verdict = "PASS" if combined_rho >= 0.4 else (
        "WARNING" if combined_rho >= 0.3 else "FAIL")

    # --- Save results ---
    os.makedirs(args.output_dir, exist_ok=True)

    output = {
        "attention": {**attn_stats, "per_group_data": attn_results},
        "mlp": {**mlp_stats, "per_group_data": mlp_results},
        "combined": combined_stats,
        "mvp_verdict": verdict,
    }
    json_path = os.path.join(args.output_dir, "correlation_results.json")
    with open(json_path, "w") as f:
        json.dump(output, f, indent=2)
    logger.info(f"Results saved to {json_path}")

    # --- Scatter plots ---
    if attn_results:
        make_scatter_plot(
            attn_results, attn_stats,
            os.path.join(args.output_dir, "fh_vs_recoverability_attention.png"),
            title_prefix="Attention: ",
        )
    if mlp_results:
        make_scatter_plot(
            mlp_results, mlp_stats,
            os.path.join(args.output_dir, "fh_vs_recoverability_mlp.png"),
            title_prefix="MLP: ",
        )
    if combined_results:
        make_scatter_plot(
            combined_results, combined_stats,
            os.path.join(args.output_dir, "fh_vs_recoverability_combined.png"),
            title_prefix="Combined: ",
            color_by_type=True,
        )

    # --- Summary ---
    print(f"\n{'='*60}")
    print("Correlation Analysis Results (Attention + MLP)")
    print(f"{'='*60}")
    if attn_results:
        print(f"  ATTENTION: rho={attn_stats['spearman_rho']:.4f}, "
              f"p={attn_stats['p_value']:.2e}, N={len(attn_results)}")
    else:
        print("  ATTENTION: no pruned groups")
    if mlp_results:
        print(f"  MLP:       rho={mlp_stats['spearman_rho']:.4f}, "
              f"p={mlp_stats['p_value']:.2e}, N={len(mlp_results)}")
    else:
        print("  MLP:       no pruned groups")
    print(f"  COMBINED:  rho={combined_rho:.4f}, "
          f"p={combined_stats['p_value']:.2e}, N={len(combined_results)}")
    print(f"  95% CI:    [{combined_stats['bootstrap_ci_95'][0]:.4f}, "
          f"{combined_stats['bootstrap_ci_95'][1]:.4f}]")
    print(f"  MVP Verdict: {verdict}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
