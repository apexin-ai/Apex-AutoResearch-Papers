"""Smart Compress Training: VisionTokenCompressor + OpenVLA on LIBERO.

Usage:
    python train_openvla_smart_compress.py --config configs/openvla_smart_compress_m32.yaml
    python train_openvla_smart_compress.py --config configs/openvla_smart_compress_m32.yaml --dry-run
    python train_openvla_smart_compress.py --config configs/openvla_smart_compress_m32.yaml --resume checkpoints/openvla_sc_m32/latest

Trainable: VisionTokenCompressor only.
Frozen: DINOv2 + SigLIP + projector + Llama-2 7B.

OpenVLA uses autoregressive action prediction: continuous actions are discretized
to 256-bin tokens, and the LLM generates them via cross-entropy loss.
"""

from __future__ import annotations

import faulthandler
faulthandler.enable()
import argparse
import copy
import json
import logging
import os
import signal
import sys
import time as time_module
from pathlib import Path
from typing import Any, Dict, List, Optional

import numpy as np
import torch
import torch.nn.functional as F
import yaml

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger(__name__)

ARTIFACTS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(ARTIFACTS_DIR))

from openvla_vtc_adapter import (
    OpenVLAActionTokenizer,
    OpenVLASmartCompressWrapper,
    VisionTokenCompressor,
)


# ---- config loading ----

def load_config(config_path: str) -> Dict[str, Any]:
    config_path = Path(config_path)
    with open(config_path) as f:
        config = yaml.safe_load(f)
    if "_base_" in config:
        base_path = config_path.parent / config.pop("_base_")
        base_config = load_config(str(base_path))
        base_config = deep_merge(base_config, config)
        return base_config
    return config


def deep_merge(base: Dict, override: Dict) -> Dict:
    result = copy.deepcopy(base)
    for k, v in override.items():
        if k in result and isinstance(result[k], dict) and isinstance(v, dict):
            result[k] = deep_merge(result[k], v)
        else:
            result[k] = copy.deepcopy(v)
    return result


def set_seed(seed: int):
    import random
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


# ---- model loading ----

def load_openvla_model(config: Dict[str, Any], device: torch.device):
    """Load OpenVLA model and processor from HuggingFace."""
    from transformers import AutoModelForVision2Seq, AutoProcessor

    model_cfg = config["model"]
    pretrained = model_cfg.get("pretrained", "openvla/openvla-7b")
    dtype_str = model_cfg.get("dtype", "float32")
    dtype_map = {"float32": torch.float32, "bfloat16": torch.bfloat16, "float16": torch.float16}
    torch_dtype = dtype_map.get(dtype_str, torch.float32)

    log.info("Loading OpenVLA from %s (dtype=%s)", pretrained, dtype_str)

    model = AutoModelForVision2Seq.from_pretrained(
        pretrained,
        torch_dtype=torch_dtype,
        trust_remote_code=True,
        low_cpu_mem_usage=True,
    )
    processor = AutoProcessor.from_pretrained(
        pretrained,
        trust_remote_code=True,
    )

    model.to(device)
    log.info("OpenVLA loaded: %d params", sum(p.numel() for p in model.parameters()))
    return model, processor


def wrap_with_compressor(
    model, processor, config: Dict[str, Any]
) -> OpenVLASmartCompressWrapper:
    """Create SmartCompressWrapper around OpenVLA."""
    compress_cfg = config.get("compressor", {})
    wrapper = OpenVLASmartCompressWrapper(
        model, processor, compress_config=compress_cfg
    )
    return wrapper


def freeze_for_compress_training(wrapper: OpenVLASmartCompressWrapper, config=None):
    """Freeze all OpenVLA parameters. Trainable: VTC compressor + LoRA (if enabled)."""
    for param in wrapper.model.parameters():
        param.requires_grad = False

    for param in wrapper.compressor.parameters():
        param.requires_grad = True

    if config and config.get("lora", {}).get("enabled", False):
        for name, param in wrapper.model.named_parameters():
            if "lora_" in name:
                param.requires_grad = True

    trainable = sum(p.numel() for p in wrapper.parameters() if p.requires_grad)
    total = sum(p.numel() for p in wrapper.parameters())
    comp_params = sum(p.numel() for p in wrapper.compressor.parameters())
    lora_params = sum(
        p.numel() for n, p in wrapper.model.named_parameters()
        if p.requires_grad and "lora_" in n
    )
    log.info(
        "Freeze config: trainable=%d / total=%d (%.4f%%)",
        trainable, total, 100 * trainable / total,
    )
    log.info("  Compressor params: %d", comp_params)
    if lora_params > 0:
        log.info("  LoRA params: %d", lora_params)


def apply_lora(model, config):
    """Apply LoRA adapters to the language model if configured."""
    lora_cfg = config.get("lora", {})
    if not lora_cfg.get("enabled", False):
        return
    from peft import LoraConfig, get_peft_model
    lc = LoraConfig(
        r=lora_cfg.get("r", 16),
        lora_alpha=lora_cfg.get("alpha", 32),
        target_modules=lora_cfg.get("target_modules", ["q_proj", "v_proj"]),
        lora_dropout=lora_cfg.get("dropout", 0.05),
        bias="none",
        task_type="CAUSAL_LM",
    )
    model.language_model = get_peft_model(model.language_model, lc)
    lora_params = sum(p.numel() for p in model.language_model.parameters() if p.requires_grad)
    log.info("LoRA applied: %d trainable params in LLM", lora_params)


# ---- dataset ----

def load_dataset(config: Dict[str, Any]):
    """Load LIBERO dataset via LeRobotDataset."""
    from lerobot.datasets.lerobot_dataset import LeRobotDataset
    from lerobot.datasets.dataset_metadata import LeRobotDatasetMetadata

    ds_cfg = config["dataset"]
    repo_id = ds_cfg["repo_id"]
    chunk_size = ds_cfg.get("action_chunk_size", 1)

    meta = LeRobotDatasetMetadata(repo_id)
    delta_timestamps = {"action": [i / meta.fps for i in range(chunk_size)]}

    dataset = LeRobotDataset(
        repo_id=repo_id,
        episodes=ds_cfg.get("episodes", None),
        delta_timestamps=delta_timestamps,
    )
    return dataset


def make_dataloader(dataset, config: Dict[str, Any]):
    from torch.utils.data import DataLoader
    train_cfg = config["training"]
    return DataLoader(
        dataset,
        batch_size=train_cfg.get("batch_size", 4),
        shuffle=True,
        num_workers=train_cfg.get("num_workers", 4),
        pin_memory=True,
        drop_last=True,
    )


# ---- action normalization stats ----

def compute_action_stats(dataset, config: Dict[str, Any]) -> Dict[str, Tensor]:
    """Compute per-dimension min/max action statistics from dataset.

    Returns dict with 'min' and 'max' tensors of shape (action_dim,).
    """
    ds_cfg = config["dataset"]
    action_dim = ds_cfg["features"]["action_dim"]

    if "action_stats" in ds_cfg:
        return {
            "min": torch.tensor(ds_cfg["action_stats"]["min"], dtype=torch.float32),
            "max": torch.tensor(ds_cfg["action_stats"]["max"], dtype=torch.float32),
        }

    log.info("Computing action statistics from dataset...")
    all_actions = []
    for i in range(min(len(dataset), 10000)):
        sample = dataset[i]
        action = sample["action"]
        if isinstance(action, torch.Tensor):
            action = action.numpy()
        if action.ndim == 2:
            action = action[0]
        all_actions.append(action[:action_dim])

    all_actions = np.stack(all_actions, axis=0)
    lo = np.percentile(all_actions, 1, axis=0)
    hi = np.percentile(all_actions, 99, axis=0)
    # Ensure non-zero range
    margin = np.maximum(hi - lo, 0.01) * 0.05
    lo -= margin
    hi += margin

    log.info("  Action min: %s", lo)
    log.info("  Action max: %s", hi)
    return {
        "min": torch.tensor(lo, dtype=torch.float32),
        "max": torch.tensor(hi, dtype=torch.float32),
    }


# ---- batch preprocessing ----

OPENVLA_PROMPT_TEMPLATE = "In: What action should the robot take to {task}?\nOut:"


def preprocess_batch(
    batch: Dict[str, Any],
    processor,
    action_tokenizer: OpenVLAActionTokenizer,
    config: Dict[str, Any],
    device: torch.device,
) -> Dict[str, Tensor]:
    """Convert LeRobot batch to OpenVLA training format.

    Returns dict with: pixel_values (list of tensors per camera),
    input_ids, attention_mask, labels.
    """
    ds_cfg = config["dataset"]
    cameras = ds_cfg["features"].get("cameras", ["observation.images.image"])
    action_dim = ds_cfg["features"]["action_dim"]

    # Tasks
    tasks = batch.get("task", batch.get("language_instruction", None))
    if tasks is None:
        tasks = ["pick up the object"] * batch["action"].shape[0]
    elif isinstance(tasks, str):
        tasks = [tasks]

    B = len(tasks)

    # Actions: (B, chunk_size, action_dim) or (B, action_dim)
    actions = batch["action"]
    if isinstance(actions, torch.Tensor):
        if actions.ndim == 3:
            actions = actions[:, 0, :action_dim]
        else:
            actions = actions[:, :action_dim]
    actions = actions.float()

    # Process images per camera
    pixel_values_list = []
    for cam_key in cameras:
        imgs = batch[cam_key]
        if isinstance(imgs, torch.Tensor):
            # (B, C, H, W) float [0,1] -> PIL -> processor
            img_list = []
            for b in range(B):
                img = imgs[b]
                if img.dtype == torch.float32 or img.dtype == torch.float16:
                    img = (img.clamp(0, 1) * 255).byte()
                if img.shape[0] in (1, 3):
                    img = img.permute(1, 2, 0)
                img_np = img.cpu().numpy()
                from PIL import Image
                pil_img = Image.fromarray(img_np)
                img_list.append(pil_img)

            # Use processor's image_processor to get pixel_values
            proc_out = processor.image_processor(
                images=img_list, return_tensors="pt"
            )
            pv = proc_out["pixel_values"].to(device)
            pixel_values_list.append(pv)

    # Tokenize prompts
    prompts = [OPENVLA_PROMPT_TEMPLATE.format(task=t) for t in tasks]
    text_out = processor.tokenizer(
        prompts,
        padding="longest",
        return_tensors="pt",
        add_special_tokens=True,
    )
    prompt_ids = text_out["input_ids"]  # (B, prompt_len) -- may NOT include image tokens
    prompt_mask = text_out["attention_mask"]

    # If the tokenizer didn't insert image tokens, we add them manually
    # Prismatic processors often handle this in __call__ not in tokenizer alone
    image_token_id = OpenVLASmartCompressWrapper(
        None, processor, {}
    ).image_token_id if hasattr(processor, "tokenizer") else 32000

    # Check if image tokens present
    has_img_tokens = (prompt_ids == image_token_id).any()
    if not has_img_tokens:
        # Insert 256 image tokens after the first token (BOS)
        n_img = 256 * len(cameras)
        img_ids = torch.full((B, n_img), image_token_id, dtype=torch.long)
        prompt_ids = torch.cat([prompt_ids[:, :1], img_ids, prompt_ids[:, 1:]], dim=1)
        img_mask = torch.ones(B, n_img, dtype=torch.long)
        prompt_mask = torch.cat([prompt_mask[:, :1], img_mask, prompt_mask[:, 1:]], dim=1)

    # Tokenize actions
    action_token_ids = action_tokenizer.encode(actions)  # (B, action_dim)

    # Build full input_ids: [prompt, action_tokens, eos]
    eos_id = processor.tokenizer.eos_token_id
    if eos_id is None:
        eos_id = processor.tokenizer.pad_token_id or 2
    eos_ids = torch.full((B, 1), eos_id, dtype=torch.long)

    full_ids = torch.cat([prompt_ids, action_token_ids.cpu(), eos_ids], dim=1)
    full_mask = torch.cat([
        prompt_mask,
        torch.ones(B, action_dim + 1, dtype=torch.long),
    ], dim=1)

    # Labels: -100 for prompt, action_token_ids for action positions, eos at end
    labels = torch.full_like(full_ids, -100)
    prompt_len = prompt_ids.shape[1]
    labels[:, prompt_len:prompt_len + action_dim] = action_token_ids.cpu()
    labels[:, prompt_len + action_dim] = eos_id

    return {
        "pixel_values": pixel_values_list if len(pixel_values_list) > 1 else pixel_values_list[0],
        "input_ids": full_ids.to(device),
        "attention_mask": full_mask.to(device),
        "labels": labels.to(device),
    }


# ---- optimizer + scheduler ----

def make_optimizer(model, config: Dict[str, Any]):
    train_cfg = config["training"]
    params = [p for p in model.parameters() if p.requires_grad]
    return torch.optim.AdamW(
        params,
        lr=train_cfg.get("lr", 1e-4),
        betas=tuple(train_cfg.get("betas", [0.9, 0.95])),
        weight_decay=train_cfg.get("weight_decay", 1e-10),
    )


def make_scheduler(optimizer, config: Dict[str, Any]):
    from torch.optim.lr_scheduler import CosineAnnealingLR, LinearLR, SequentialLR

    train_cfg = config["training"]
    total_steps = train_cfg.get("total_steps", 100000)
    warmup_steps = train_cfg.get("warmup_steps", 1000)

    warmup = LinearLR(optimizer, start_factor=0.01, end_factor=1.0, total_iters=warmup_steps)
    cosine = CosineAnnealingLR(
        optimizer,
        T_max=total_steps - warmup_steps,
        eta_min=train_cfg.get("decay_lr", 2.5e-6),
    )
    return SequentialLR(optimizer, schedulers=[warmup, cosine], milestones=[warmup_steps])


# ---- checkpointing ----

def save_checkpoint(model, optimizer, scheduler, step, config, info, output_dir,
                    final=False, max_keep_ckpt=3):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    info_dict = {
        k: v.item() if isinstance(v, torch.Tensor) else v
        for k, v in info.items()
        if not isinstance(v, torch.Tensor) or v.dim() == 0
    }

    if final:
        ckpt = {
            "step": step,
            "model_state_dict": model.state_dict(),
            "optimizer_state_dict": optimizer.state_dict(),
            "scheduler_state_dict": scheduler.state_dict(),
            "config": config,
            "info": info_dict,
        }
    else:
        compressor_state = {
            k: v for k, v in model.state_dict().items()
            if "compressor" in k
        }
        ckpt = {
            "step": step,
            "compressor_state_dict": compressor_state,
            "optimizer_state_dict": optimizer.state_dict(),
            "scheduler_state_dict": scheduler.state_dict(),
            "config": config,
            "info": info_dict,
        }

    ckpt_path = output_dir / f"checkpoint_step{step}.pt"
    torch.save(ckpt, ckpt_path)
    size_mb = ckpt_path.stat().st_size / 1024**2
    log.info("Saved %s checkpoint at step %d -> %s (%.1f MB)",
             "full" if final else "compressor-only", step, ckpt_path, size_mb)

    if final:
        latest_path = output_dir / "checkpoint.pt"
        torch.save(ckpt, latest_path)

    if not final and max_keep_ckpt > 0:
        step_ckpts = sorted(
            output_dir.glob("checkpoint_step*.pt"),
            key=lambda p: p.stat().st_mtime,
        )
        while len(step_ckpts) > max_keep_ckpt:
            old = step_ckpts.pop(0)
            old.unlink()
            log.info("Removed old checkpoint: %s", old.name)


# ---- dry run ----

def dry_run(model, dataloader, device, config, processor, action_tokenizer):
    """Single forward/backward pass to verify everything works."""
    log.info("=== DRY RUN ===")
    model.train()

    batch = next(iter(dataloader))
    batch = {k: v.to(device) if isinstance(v, torch.Tensor) else v for k, v in batch.items()}
    inputs = preprocess_batch(batch, processor, action_tokenizer, config, device)

    log.info("Input shapes:")
    for k, v in inputs.items():
        if isinstance(v, torch.Tensor):
            log.info("  %s: %s %s", k, v.shape, v.dtype)
        elif isinstance(v, list):
            log.info("  %s: list of %d tensors, each %s", k, len(v), v[0].shape)

    loss, info = model.forward(**inputs)
    log.info("Forward OK: loss=%.4f", loss.item())

    loss.backward()
    grad_norm = torch.nn.utils.clip_grad_norm_(
        [p for p in model.parameters() if p.requires_grad], 10.0
    ).item()
    log.info("Backward OK: grad_norm=%.4f", grad_norm)

    for k, v in info.items():
        val = v.item() if isinstance(v, torch.Tensor) else v
        log.info("  %s: %s", k, val)

    trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
    log.info("Trainable params: %d", trainable)
    log.info("=== DRY RUN PASSED ===")


# ---- evaluation ----

def evaluate(model, dataloader, step, config, device, processor, action_tokenizer):
    """Evaluate action prediction loss on a few batches."""
    model.eval()
    max_batches = config.get("evaluation", {}).get("max_eval_batches", 50)

    losses = []
    data_iter = iter(dataloader)
    with torch.no_grad():
        for _ in range(max_batches):
            try:
                batch = next(data_iter)
            except StopIteration:
                break
            batch = {k: v.to(device) if isinstance(v, torch.Tensor) else v for k, v in batch.items()}
            inputs = preprocess_batch(batch, processor, action_tokenizer, config, device)
            loss, _ = model.forward(**inputs)
            losses.append(loss.item())

    model.train()
    avg_loss = sum(losses) / len(losses) if losses else 0.0
    return {"eval/action_loss": avg_loss, "eval/step": step}


# ---- graceful exit ----

class GracefulExit:
    def __init__(self):
        self.should_exit = False
        signal.signal(signal.SIGTERM, self._handler)
        signal.signal(signal.SIGINT, self._handler)

    def _handler(self, signum, frame):
        log.info("Caught signal %d, will exit after current step", signum)
        self.should_exit = True


# ---- main ----

def parse_args():
    p = argparse.ArgumentParser(description="Train VTC for OpenVLA")
    p.add_argument("--config", type=str, required=True)
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--resume", type=str, default=None)
    p.add_argument("--max-steps", type=int, default=None)
    p.add_argument("--wandb-project", type=str, default="openvla-smart-compress")
    p.add_argument("--wandb-run", type=str, default=None)
    return p.parse_args()


def main():
    args = parse_args()
    config = load_config(args.config)
    train_cfg = config["training"]

    set_seed(train_cfg.get("seed", 42))

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    log.info("Device: %s", device)

    # Load model
    model_base, processor = load_openvla_model(config, device)
    apply_lora(model_base, config)
    model = wrap_with_compressor(model_base, processor, config)
    model.to(device)
    freeze_for_compress_training(model, config)

    # Dataset + dataloader
    dataset = load_dataset(config)
    dataloader = make_dataloader(dataset, config)
    log.info("Dataset: %d samples, %d batches/epoch", len(dataset), len(dataloader))

    # Action tokenizer
    action_stats = compute_action_stats(dataset, config)
    action_tokenizer = OpenVLAActionTokenizer(
        processor.tokenizer,
        min_action=action_stats["min"],
        max_action=action_stats["max"],
    )
    log.info("Action tokenizer: begin_id=%d", action_tokenizer.action_token_begin_id)

    # Dry run
    if args.dry_run:
        dry_run(model, dataloader, device, config, processor, action_tokenizer)
        return

    # Optimizer + scheduler
    optimizer = make_optimizer(model, config)
    scheduler = make_scheduler(optimizer, config)

    total_steps = args.max_steps or train_cfg.get("total_steps", 100000)
    log_every = train_cfg.get("log_every", 50)
    eval_every = train_cfg.get("eval_every", 5000)
    save_every = train_cfg.get("save_every", 10000)
    grad_clip = train_cfg.get("grad_clip", 10.0)
    output_dir = train_cfg.get("output_dir", "checkpoints/openvla_sc_m32")

    start_step = 0

    # Resume
    if args.resume:
        ckpt_path = Path(args.resume)
        if ckpt_path.is_dir():
            ckpt_path = ckpt_path / "checkpoint.pt"
        log.info("Resuming from %s", ckpt_path)
        ckpt = torch.load(ckpt_path, map_location=device, weights_only=False)
        if "compressor_state_dict" in ckpt:
            model.load_state_dict(ckpt["compressor_state_dict"], strict=False)
        else:
            model.load_state_dict(ckpt["model_state_dict"], strict=False)
        optimizer.load_state_dict(ckpt["optimizer_state_dict"])
        scheduler.load_state_dict(ckpt["scheduler_state_dict"])
        start_step = ckpt["step"] + 1
        log.info("Resumed at step %d", start_step)

    # W&B
    import wandb
    compress_cfg = config.get("compressor", {})
    run_name = args.wandb_run or f"openvla_sc_m{compress_cfg.get('num_queries', 32)}"
    wandb.init(
        project=args.wandb_project,
        name=run_name,
        config=config,
        resume="allow",
    )

    # Eval dataloader
    eval_dataloader = make_dataloader(dataset, {
        **config,
        "training": {**train_cfg, "batch_size": train_cfg.get("eval_batch_size", 1)},
    })

    # Training loop
    graceful = GracefulExit()
    model.train()
    data_iter = iter(dataloader)
    t0 = time_module.time()
    last_info: Dict[str, Any] = {}

    log.info("Starting training: %d -> %d steps", start_step, total_steps)

    for step in range(start_step, total_steps):
        try:
            batch = next(data_iter)
        except StopIteration:
            data_iter = iter(dataloader)
            batch = next(data_iter)

        batch = {k: v.to(device) if isinstance(v, torch.Tensor) else v for k, v in batch.items()}
        inputs = preprocess_batch(batch, processor, action_tokenizer, config, device)

        loss, info = model.forward(**inputs)
        loss.backward()

        grad_norm = torch.nn.utils.clip_grad_norm_(
            [p for p in model.parameters() if p.requires_grad],
            grad_clip,
        ).item()

        optimizer.step()
        scheduler.step()
        optimizer.zero_grad()

        last_info = info

        if step % log_every == 0:
            action_l = info["action_loss"].item() if isinstance(info["action_loss"], torch.Tensor) else info["action_loss"]
            log_dict = {
                "train/action_loss": action_l,
                "train/lr": optimizer.param_groups[0]["lr"],
                "train/grad_norm": grad_norm,
            }
            wandb.log(log_dict, step=step)

            elapsed = time_module.time() - t0
            sps = (step - start_step + 1) / elapsed if elapsed > 0 else 0
            log.info(
                "step=%d/%d  loss=%.4f  lr=%.2e  grad=%.2f  sps=%.1f",
                step, total_steps, action_l,
                optimizer.param_groups[0]["lr"], grad_norm, sps,
            )

        if step > 0 and step % eval_every == 0:
            eval_metrics = evaluate(
                model, eval_dataloader, step, config, device,
                processor, action_tokenizer,
            )
            wandb.log(eval_metrics, step=step)
            for k, v in eval_metrics.items():
                log.info("  %s: %.4f", k, v)

        if step > 0 and step % save_every == 0:
            save_checkpoint(model, optimizer, scheduler, step, config, last_info, output_dir)

        if graceful.should_exit:
            log.info("Graceful exit at step %d", step)
            save_checkpoint(model, optimizer, scheduler, step, config, last_info, output_dir, final=True)
            break

    if not graceful.should_exit:
        save_checkpoint(model, optimizer, scheduler, total_steps - 1, config, last_info, output_dir, final=True)

    wandb.finish()
    log.info("Training complete.")


if __name__ == "__main__":
    main()
