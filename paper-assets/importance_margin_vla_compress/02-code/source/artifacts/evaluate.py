"""IMM Evaluation Pipeline.

Evaluates trained models under:
  - Clean vs perturbed inputs (Gaussian noise eps in {0.01, 0.02, 0.05})
  - With/without ACIS-based 50% token pruning
  - Metrics: margin stats, top-k preservation rate, L*eps/Delta_k, Kendall tau, certified bound

Usage:
    python evaluate.py --checkpoint path/to/ckpt --config configs/imm_anchor.yaml --gpu 0
    python evaluate.py --checkpoint path/to/baseline --config configs/baseline.yaml --output results/baseline.json

Depends: lerobot, torch, imm.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import logging
import sys
from pathlib import Path
from typing import Any, Dict, List

import torch
import torch.nn.functional as F
import yaml

ARTIFACTS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(ARTIFACTS_DIR))

from imm.metrics import (
    certified_bound,
    compute_empirical_lipschitz,
    compute_margin,
    kendall_tau_distance,
    l_eps_delta_ratio,
    margin_statistics,
    topk_preservation_rate,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger(__name__)


def parse_args():
    parser = argparse.ArgumentParser(description="IMM evaluation for SmolVLA on LIBERO")
    parser.add_argument("--checkpoint", type=str, required=True, help="Path to checkpoint file or directory")
    parser.add_argument("--config", type=str, required=True, help="Path to YAML config file")
    parser.add_argument("--gpu", type=int, default=0, help="GPU index")
    parser.add_argument("--output", type=str, default=None, help="Path to save results JSON (default: results/<run>.json)")
    parser.add_argument("--max_batches", type=int, default=100, help="Max batches to evaluate")
    parser.add_argument("--lipschitz_samples", type=int, default=100, help="Samples for empirical Lipschitz estimation")
    parser.add_argument("--seed", type=int, default=42, help="Random seed")
    return parser.parse_args()


def load_config(config_path: str) -> Dict[str, Any]:
    """Load YAML config with _base_ inheritance."""
    import copy
    config_path = Path(config_path)
    with open(config_path) as f:
        config = yaml.safe_load(f)
    if "_base_" in config:
        base_path = config_path.parent / config.pop("_base_")
        base_config = load_config(str(base_path))
        for k, v in config.items():
            if k in base_config and isinstance(base_config[k], dict) and isinstance(v, dict):
                base_config[k].update(v)
            else:
                base_config[k] = v
        return base_config
    return config


def load_model_and_checkpoint(config: Dict[str, Any], checkpoint_path: str, device: torch.device):
    """Load SmolVLA policy, optionally wrap with IMM, then load checkpoint weights."""
    from train import load_smolvla_policy, wrap_with_imm

    policy = load_smolvla_policy(config, device)
    imm_enabled = config.get("imm", {}).get("enabled", False)

    if imm_enabled:
        model = wrap_with_imm(policy, config)
        model.to(device)
    else:
        model = policy

    ckpt_path = Path(checkpoint_path)
    if ckpt_path.is_dir():
        ckpt_path = ckpt_path / "checkpoint.pt"

    log.info("Loading checkpoint from %s", ckpt_path)
    state = torch.load(ckpt_path, map_location=device, weights_only=False)
    model.load_state_dict(state["model_state_dict"], strict=False)

    model.eval()
    return model, imm_enabled


def compute_importance_scores(
    model, batch: Dict[str, torch.Tensor], imm_enabled: bool,
    noise: torch.Tensor = None, time: torch.Tensor = None,
):
    """Extract ACIS importance scores from the model.

    Returns (scores, k) or (None, None) for baseline models.
    Pass noise/time to ensure deterministic scoring across clean vs perturbed.
    """
    if not imm_enabled:
        return None, None

    return model.compute_importance_scores(batch, noise=noise, time=time)


def perturb_images(batch: Dict[str, torch.Tensor], epsilon: float) -> Dict[str, torch.Tensor]:
    """Add Gaussian noise to image tensors in batch."""
    batch_noisy = {}
    for key, val in batch.items():
        if isinstance(val, torch.Tensor) and "image" in key.lower() and val.is_floating_point():
            batch_noisy[key] = (val + epsilon * torch.randn_like(val)).clamp(0, 1)
        else:
            batch_noisy[key] = val
    return batch_noisy


def baseline_forward(policy, batch: Dict[str, torch.Tensor]):
    """Baseline forward: flow matching loss without action_is_pad masking.

    Bypasses SmolVLAPolicy.forward() which dilutes loss via pad masking.
    Uses the same approach as IMMSmolVLAWrapper.forward() for consistency.
    """
    from lerobot.utils.constants import OBS_LANGUAGE_TOKENS, OBS_LANGUAGE_ATTENTION_MASK

    images, img_masks = policy.prepare_images(batch)
    state = policy.prepare_state(batch)
    lang_tokens = batch[OBS_LANGUAGE_TOKENS]
    lang_masks = batch[OBS_LANGUAGE_ATTENTION_MASK]
    actions = policy.prepare_action(batch)

    losses = policy.model.forward(
        images, img_masks, lang_tokens, lang_masks, state, actions, None, None
    )

    action_dim = policy.config.action_feature.shape[0]
    loss = losses[:, :, :action_dim].mean()
    return loss, {"action_loss": loss.detach()}


def _find_connector(model):
    """Find the visual connector module in SmolVLA (multi_modal_projector or connector)."""
    for name, module in model.named_modules():
        if name.endswith(".connector") or "multi_modal_projector" in name:
            return module
    return None


def _apply_random_pruning_hook(model, pruning_ratio: float, seed: int, batch_idx: int):
    """Register a forward hook on the visual connector for random token pruning.

    The hook targets multi_modal_projector output which contains only visual
    tokens (B, N_vis, D). Mask is scoped to the first n_visual positions to
    avoid accidentally zeroing non-visual tokens if the connector output
    ever includes extra dimensions.
    """
    n_visual = 64
    k_keep = int(n_visual * (1 - pruning_ratio))

    def hook_fn(module, input, output):
        if isinstance(output, tuple):
            tokens = output[0]
        else:
            tokens = output
        if tokens.dim() != 3 or tokens.shape[1] < n_visual:
            return output
        B = tokens.shape[0]
        N = tokens.shape[1]
        g = torch.Generator(device="cpu")
        g.manual_seed(seed + batch_idx)
        mask = torch.ones(B, N, device=tokens.device)
        for b in range(B):
            perm = torch.randperm(n_visual, generator=g, device="cpu")
            prune_idx = perm[k_keep:]
            mask[b, prune_idx] = 0.0
        masked = tokens * mask.unsqueeze(-1)
        if isinstance(output, tuple):
            return (masked,) + output[1:]
        return masked

    connector = _find_connector(model)
    if connector is None:
        log.warning("Could not find multi_modal_projector for random pruning")
        return None
    return connector.register_forward_hook(hook_fn)


def estimate_lipschitz(model, dataloader, device: torch.device, max_batches: int = 10, num_samples: int = 100) -> float:
    """Estimate empirical Lipschitz constant of ACIS scorer.

    Uses the wrapper's policy.prepare_* methods and base_model for correct
    visual token extraction and suffix embedding.
    """
    if not hasattr(model, "acis"):
        return 0.0

    bm = model.base_model

    L_max = 0.0
    for batch_idx, batch in enumerate(dataloader):
        if batch_idx >= max_batches:
            break
        batch = {k: v.to(device) if isinstance(v, torch.Tensor) else v for k, v in batch.items()}

        images, _ = model.policy.prepare_images(batch)
        vis_tokens, _ = model._get_visual_tokens(images)

        actions = model.policy.prepare_action(batch)
        B = actions.shape[0]
        noise = bm.sample_noise(actions.shape, actions.device)
        time = bm.sample_time(B, actions.device)
        time_expanded = time[:, None, None]
        x_t = time_expanded * noise + (1 - time_expanded) * actions

        a_query, _, _ = bm.embed_suffix(x_t, time)

        L = compute_empirical_lipschitz(
            model.acis, vis_tokens, a_query,
            num_samples=num_samples, epsilon=0.001,
        )
        L_max = max(L_max, L)

    log.info("Empirical Lipschitz constant: %.4f", L_max)
    return L_max


@torch.no_grad()
def evaluate_full(
    model,
    dataloader,
    config: Dict[str, Any],
    device: torch.device,
    imm_enabled: bool,
    lipschitz_const: float,
    max_batches: int = 100,
    seed: int = 42,
    tokenizer=None,
):
    """Full evaluation matrix: 4 noise levels x 2 pruning modes = 8 conditions."""
    eval_cfg = config.get("evaluation", {})
    epsilons = eval_cfg.get("perturbations", [0.0, 0.01, 0.02, 0.05])
    pruning_ratio = eval_cfg.get("pruning_ratio", 0.5)

    results = {}
    action_losses = []

    for epsilon in epsilons:
        for pruning in [False, True]:
            condition = f"eps{epsilon}_prune{pruning}"
            log.info("Evaluating condition: %s", condition)

            # D011: RNG isolation per condition (deterministic across PYTHONHASHSEED)
            condition_offset = int(hashlib.md5(condition.encode()).hexdigest()[:8], 16) % 10000
            torch.manual_seed(seed + condition_offset)

            all_margins = []
            all_preservation = []
            all_kendall = []
            all_certified = []
            all_led_ratio = []
            all_action_loss = []

            for batch_idx, batch in enumerate(dataloader):
                if batch_idx >= max_batches:
                    break
                batch = {k: v.to(device) if isinstance(v, torch.Tensor) else v for k, v in batch.items()}

                if tokenizer is not None:
                    from train import preprocess_batch
                    batch = preprocess_batch(batch, tokenizer, device=device)

                # D011: Baseline path — apply perturbation + random pruning
                if not imm_enabled:
                    eval_batch = perturb_images(batch, epsilon) if epsilon > 0 else batch

                    hook_handle = None
                    if pruning:
                        hook_handle = _apply_random_pruning_hook(
                            model, pruning_ratio, seed, batch_idx
                        )

                    loss, _ = baseline_forward(model, eval_batch)
                    all_action_loss.append(loss.item())

                    if hook_handle is not None:
                        hook_handle.remove()
                    continue

                # IMM path: generate deterministic noise/time for this batch
                actions = model.policy.prepare_action(batch)
                bm = model.base_model if hasattr(model, 'base_model') else model._unwrap_to_vla(model.policy.model)
                det_noise = bm.sample_noise(actions.shape, actions.device)
                det_time = bm.sample_time(actions.shape[0], actions.device)

                scores_clean, k = compute_importance_scores(model, batch, imm_enabled, noise=det_noise, time=det_time)

                # Perturbed batch (reuse same noise/time for fair comparison)
                if epsilon > 0:
                    batch_noisy = perturb_images(batch, epsilon)
                    scores_pert, _ = compute_importance_scores(model, batch_noisy, imm_enabled, noise=det_noise, time=det_time)
                else:
                    scores_pert = scores_clean

                # Metrics
                margin = compute_margin(scores_clean, k)
                pres = topk_preservation_rate(scores_clean, scores_pert, k)
                kendall = kendall_tau_distance(scores_clean, scores_pert, k)
                cert = certified_bound(margin, lipschitz_const, max(epsilon, 0.01), k)
                led = l_eps_delta_ratio(lipschitz_const, max(epsilon, 0.01), margin, k)

                all_margins.append(margin.cpu())
                all_preservation.append(pres.cpu())
                all_kendall.append(kendall.cpu())
                all_certified.append(cert.cpu())
                all_led_ratio.append(led.cpu())

                # Action loss under this condition
                if pruning:
                    model.train(False)
                    eval_batch = batch_noisy if epsilon > 0 else batch
                    _, info = model(eval_batch, step=0)
                    all_action_loss.append(info["action_loss"].item())
                else:
                    _, info = model(batch if epsilon == 0 else perturb_images(batch, epsilon), step=0)
                    all_action_loss.append(info["action_loss"].item())

            cond_results = {
                "action_loss": sum(all_action_loss) / max(len(all_action_loss), 1),
            }

            if imm_enabled and all_margins:
                margins_cat = torch.cat(all_margins)
                pres_cat = torch.cat(all_preservation)
                kendall_cat = torch.cat(all_kendall)
                cert_cat = torch.cat(all_certified)
                led_cat = torch.cat(all_led_ratio)

                cond_results.update({
                    "margin_mean": margins_cat.mean().item(),
                    "margin_median": margins_cat.median().item(),
                    "margin_std": margins_cat.std().item(),
                    "margin_min": margins_cat.min().item(),
                    "margin_max": margins_cat.max().item(),
                    "preservation_rate": pres_cat.mean().item(),
                    "kendall_tau": kendall_cat.mean().item(),
                    "certified_bound_mean": cert_cat.mean().item(),
                    "certified_bound_max": cert_cat.max().item(),
                    "l_eps_delta_ratio_mean": led_cat.mean().item(),
                    "l_eps_delta_ratio_median": led_cat.median().item(),
                })

            results[condition] = cond_results
            log.info("  %s: %s", condition, {k: f"{v:.4f}" for k, v in cond_results.items()})

    return results


def main():
    args = parse_args()

    import numpy as np
    import random
    random.seed(args.seed)
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)

    config = load_config(args.config)
    device = torch.device(f"cuda:{args.gpu}" if torch.cuda.is_available() else "cpu")

    model, imm_enabled = load_model_and_checkpoint(config, args.checkpoint, device)

    from train import load_dataset, make_dataloader, get_tokenizer_from_policy
    dataset = load_dataset(config)
    dataloader = make_dataloader(dataset, {
        **config,
        "training": {**config.get("training", {}), "batch_size": config.get("training", {}).get("eval_batch_size", 4)},
    })

    tokenizer = get_tokenizer_from_policy(model)

    # Lipschitz estimation
    lipschitz_const = 0.0
    spectral_lipschitz = 0.0
    if imm_enabled and hasattr(model, "acis"):
        spectral_lipschitz = model.acis.get_lipschitz_estimate()
        log.info("Spectral Lipschitz estimate: %.4f", spectral_lipschitz)
        lipschitz_const = estimate_lipschitz(model, dataloader, device, max_batches=10, num_samples=args.lipschitz_samples)

    results = evaluate_full(model, dataloader, config, device, imm_enabled, lipschitz_const, max_batches=args.max_batches, seed=args.seed, tokenizer=tokenizer)

    results["_meta"] = {
        "checkpoint": args.checkpoint,
        "config": args.config,
        "imm_enabled": imm_enabled,
        "lipschitz_empirical": lipschitz_const,
        "lipschitz_spectral": spectral_lipschitz,
        "max_batches": args.max_batches,
        "seed": args.seed,
    }

    # Summary: compare clean vs perturbed L*eps/Delta_k ratio
    if imm_enabled:
        clean_key = "eps0.0_pruneFalse"
        if clean_key in results and "l_eps_delta_ratio_mean" in results.get(clean_key, {}):
            log.info("=== Gate Metric Summary ===")
            for cond, data in results.items():
                if cond.startswith("_"):
                    continue
                led = data.get("l_eps_delta_ratio_mean", float("nan"))
                pres = data.get("preservation_rate", float("nan"))
                log.info("  %s: L*eps*k/Delta_k=%.4f, preservation=%.4f", cond, led, pres)

    # Save results
    output_path = args.output
    if output_path is None:
        results_dir = Path("results")
        results_dir.mkdir(exist_ok=True)
        ckpt_name = Path(args.checkpoint).stem
        output_path = results_dir / f"eval_{ckpt_name}.json"
    else:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w") as f:
        json.dump(results, f, indent=2, default=str)
    log.info("Results saved to %s", output_path)


if __name__ == "__main__":
    main()
