#!/usr/bin/env python3
"""AWR LoRA fine-tuning for OpenVLA on LIBERO tasks.

Pipeline:
  1. Load OpenVLA-OFT checkpoint + apply LoRA adapters to LLM attention layers
  2. Load per-task IQL checkpoints → compute advantage A(s,a) = min(Q1,Q2) - V
  3. AWR weights = exp(A / temperature), clipped and normalized to mean 1
  4. Train with weighted BC loss on action prediction

Modes:
  --mode awr   : AWR-weighted training (default)
  --mode bc    : Vanilla BC (uniform weights = 1)
  --lite       : Train simple MLP on VIP features instead of full VLA
                 (validates AWR pipeline without requiring OpenVLA model)

Inputs:
  - OpenVLA-OFT checkpoint (HF format, local path)
  - IQL checkpoints per task (from train_pertask_iql.py)
  - VIP features per task (from extract_all_vip_features.py)
  - LIBERO demo HDF5 files (images + actions)

Outputs:
  - Checkpoints in --checkpoint-dir (per epoch + best)
  - Optional WandB logging

Related scripts:
  - phase2_bc_baseline.py: thin wrapper calling this with --mode bc
  - phase2_evaluation.py: evaluate fine-tuned model on LIBERO
  - train_pertask_iql.py: trains IQL checkpoints used here
"""

import argparse
import copy
import glob
import json
import os
import time

import h5py
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader


# ---------------------------------------------------------------------------
# IQL Networks (same architecture as train_pertask_iql.py)
# ---------------------------------------------------------------------------

class QNetwork(nn.Module):
    def __init__(self, state_dim, action_dim, hidden_dims=(256, 256)):
        super().__init__()
        dims = [state_dim + action_dim] + list(hidden_dims) + [1]
        layers = []
        for i in range(len(dims) - 1):
            layers.append(nn.Linear(dims[i], dims[i + 1]))
            if i < len(dims) - 2:
                layers.append(nn.ReLU())
        self.net = nn.Sequential(*layers)

    def forward(self, state, action):
        return self.net(torch.cat([state, action], dim=-1)).squeeze(-1)


class VNetwork(nn.Module):
    def __init__(self, state_dim, hidden_dims=(256, 256)):
        super().__init__()
        dims = [state_dim] + list(hidden_dims) + [1]
        layers = []
        for i in range(len(dims) - 1):
            layers.append(nn.Linear(dims[i], dims[i + 1]))
            if i < len(dims) - 2:
                layers.append(nn.ReLU())
        self.net = nn.Sequential(*layers)

    def forward(self, state):
        return self.net(state).squeeze(-1)


# ---------------------------------------------------------------------------
# AWR Weight Computation
# ---------------------------------------------------------------------------

def compute_awr_weights(iql_path, features, actions, temperature=1.0,
                        clip_max=20.0):
    """Compute AWR weights from IQL advantage for one task.

    Returns:
        weights: (N,) tensor, normalized to mean ~1
        advantages: (N,) raw advantage values
    """
    ckpt = torch.load(iql_path, map_location="cpu", weights_only=False)

    Q1 = QNetwork(ckpt["state_dim"], ckpt["action_dim"])
    Q2 = QNetwork(ckpt["state_dim"], ckpt["action_dim"])
    V = VNetwork(ckpt["state_dim"])
    Q1.load_state_dict(ckpt["Q1"]); Q1.eval()
    Q2.load_state_dict(ckpt["Q2"]); Q2.eval()
    V.load_state_dict(ckpt["V"]); V.eval()

    with torch.no_grad():
        q1 = Q1(features, actions)
        q2 = Q2(features, actions)
        q_min = torch.min(q1, q2)
        v = V(features)
        advantages = q_min - v

    weights = torch.exp(advantages / temperature)
    weights = torch.clamp(weights, max=clip_max)
    weights = weights / weights.mean()
    return weights, advantages


# ---------------------------------------------------------------------------
# Action Discretization (OpenVLA convention)
# ---------------------------------------------------------------------------

def discretize_action(action, norm_stats, n_bins=256):
    """Continuous action → bin indices [0, n_bins-1].

    OpenVLA convention: normalize by dataset stats, clip to [-1,1], map to bins.
    """
    mean = torch.tensor(norm_stats["action"]["mean"], dtype=torch.float32)
    std = torch.tensor(norm_stats["action"]["std"], dtype=torch.float32)
    std = torch.clamp(std, min=1e-6)

    normalized = (action - mean) / std
    normalized = torch.clamp(normalized, -1.0, 1.0)
    bins = ((normalized + 1.0) / 2.0 * (n_bins - 1)).long()
    return torch.clamp(bins, 0, n_bins - 1)


def undiscretize_action(bin_idx, norm_stats, n_bins=256):
    """Bin indices → continuous action (inverse of discretize_action)."""
    mean = torch.tensor(norm_stats["action"]["mean"], dtype=torch.float32)
    std = torch.tensor(norm_stats["action"]["std"], dtype=torch.float32)
    normalized = (bin_idx.float() / (n_bins - 1)) * 2.0 - 1.0
    return normalized * std + mean


# ---------------------------------------------------------------------------
# Datasets
# ---------------------------------------------------------------------------

class LiberoLiteDataset(Dataset):
    """VIP features + actions for lite mode training."""

    def __init__(self, features_path, data_dir, task_name, weights=None):
        feat_data = torch.load(features_path, map_location="cpu",
                               weights_only=False)
        self.features = feat_data["features"]        # (N, 1024)
        self.traj_ids = feat_data["traj_ids"]         # (N,)

        hdf5_path = os.path.join(data_dir, f"{task_name}_demo.hdf5")
        all_actions = []
        with h5py.File(hdf5_path, "r") as hf:
            demo_keys = sorted(
                [k for k in hf["data"].keys() if k.startswith("demo_")],
                key=lambda x: int(x.split("_")[1]),
            )
            for dk in demo_keys:
                acts = hf[f"data/{dk}/actions"][:]
                all_actions.append(torch.from_numpy(acts).float())
        self.actions = torch.cat(all_actions, dim=0)   # (N, 7)

        min_len = min(len(self.features), len(self.actions))
        self.features = self.features[:min_len]
        self.actions = self.actions[:min_len]

        if weights is not None:
            self.weights = weights[:min_len].float()
        else:
            self.weights = torch.ones(min_len)

    def __len__(self):
        return len(self.features)

    def __getitem__(self, idx):
        return (self.features[idx], self.actions[idx], self.weights[idx])


class LiberoVLADataset(Dataset):
    """Images + actions for full VLA mode training."""

    def __init__(self, data_dir, task_name, weights=None, subsample=1):
        self.task_name = task_name
        self.instruction = self._task_to_instruction(task_name)

        hdf5_path = os.path.join(data_dir, f"{task_name}_demo.hdf5")
        self.images = []
        self.actions = []

        with h5py.File(hdf5_path, "r") as hf:
            demo_keys = sorted(
                [k for k in hf["data"].keys() if k.startswith("demo_")],
                key=lambda x: int(x.split("_")[1]),
            )
            for dk in demo_keys:
                imgs = hf[f"data/{dk}/obs/agentview_rgb"][:]
                acts = hf[f"data/{dk}/actions"][:]
                for t in range(0, len(imgs), subsample):
                    self.images.append(imgs[t])
                    self.actions.append(acts[t])

        self.actions = np.array(self.actions, dtype=np.float32)
        n = len(self.images)

        if weights is not None:
            self.weights = weights[:n].float().numpy()
        else:
            self.weights = np.ones(n, dtype=np.float32)

        print(f"  VLADataset {task_name}: {n} samples", flush=True)

    @staticmethod
    def _task_to_instruction(task_name):
        return "In: What action should the robot take to " + \
               task_name.replace("_", " ") + "?\nOut:"

    def __len__(self):
        return len(self.images)

    def __getitem__(self, idx):
        return {
            "image": self.images[idx],          # (H, W, 3) uint8
            "action": self.actions[idx],         # (7,) float32
            "weight": self.weights[idx],         # scalar
            "instruction": self.instruction,
        }


# ---------------------------------------------------------------------------
# Lite-mode Action Head
# ---------------------------------------------------------------------------

class LiteActionHead(nn.Module):
    """MLP: VIP features (1024) → continuous actions (7)."""

    def __init__(self, input_dim=1024, hidden_dim=512, action_dim=7):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.LayerNorm(hidden_dim),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.LayerNorm(hidden_dim),
            nn.Linear(hidden_dim, action_dim),
        )

    def forward(self, x):
        return self.net(x)


# ---------------------------------------------------------------------------
# Training: Lite Mode
# ---------------------------------------------------------------------------

def train_lite(args):
    device = torch.device(args.device if torch.cuda.is_available() else "cpu")
    print(f"=== Lite Mode ({args.mode.upper()}) on {device} ===", flush=True)

    task_names = _get_task_names(args)
    os.makedirs(args.checkpoint_dir, exist_ok=True)

    if args.wandb:
        _init_wandb(args, mode="lite")

    for task_name in task_names:
        short = task_name.replace("pick_up_the_", "").replace(
            "_and_place_it_in_the_basket", "")
        print(f"\n{'=' * 50}\nTask: {short}\n{'=' * 50}", flush=True)

        feat_path = os.path.join(args.features_dir, f"{task_name}.pt")
        if not os.path.exists(feat_path):
            print(f"  SKIP: no features at {feat_path}", flush=True)
            continue

        # --- AWR weights ---
        weights = None
        if args.mode == "awr":
            iql_path = os.path.join(args.iql_checkpoint_dir,
                                    f"{task_name}_iql.pt")
            if not os.path.exists(iql_path):
                print(f"  SKIP: no IQL checkpoint at {iql_path}", flush=True)
                continue

            feat_data = torch.load(feat_path, map_location="cpu",
                                   weights_only=False)
            features_for_iql = feat_data["features"]
            hdf5_path = os.path.join(args.data_dir,
                                     f"{task_name}_demo.hdf5")
            all_act = []
            with h5py.File(hdf5_path, "r") as hf:
                for dk in sorted(hf["data"].keys()):
                    if dk.startswith("demo_"):
                        all_act.append(
                            torch.from_numpy(hf[f"data/{dk}/actions"][:]).float()
                        )
            actions_for_iql = torch.cat(all_act, 0)
            min_len = min(len(features_for_iql), len(actions_for_iql))
            features_for_iql = features_for_iql[:min_len]
            actions_for_iql = actions_for_iql[:min_len]

            weights, advantages = compute_awr_weights(
                iql_path, features_for_iql, actions_for_iql,
                temperature=args.temperature, clip_max=args.clip_max,
            )
            print(f"  AWR weights: mean={weights.mean():.3f} "
                  f"std={weights.std():.3f} "
                  f"min={weights.min():.3f} max={weights.max():.3f}",
                  flush=True)
            print(f"  Advantages: mean={advantages.mean():.4f} "
                  f"std={advantages.std():.4f} "
                  f"IQR={_iqr(advantages):.4f}", flush=True)

        # --- Dataset ---
        dataset = LiberoLiteDataset(
            feat_path, args.data_dir, task_name, weights=weights,
        )
        loader = DataLoader(dataset, batch_size=args.batch_size,
                            shuffle=True, num_workers=0, drop_last=True)

        # --- Model ---
        model = LiteActionHead(input_dim=1024, action_dim=7).to(device)
        optimizer = optim.AdamW(model.parameters(), lr=args.lr,
                                weight_decay=1e-4)
        scheduler = optim.lr_scheduler.CosineAnnealingLR(
            optimizer, T_max=args.epochs * len(loader))

        # --- Train ---
        best_loss = float("inf")
        for epoch in range(1, args.epochs + 1):
            model.train()
            total_loss = 0.0
            n_steps = 0

            for step, (feats, actions, w) in enumerate(loader):
                if args.max_steps and step >= args.max_steps:
                    break
                feats = feats.to(device)
                actions = actions.to(device)
                w = w.to(device)

                pred = model(feats)
                per_sample_loss = ((pred - actions) ** 2).mean(dim=1)
                loss = (per_sample_loss * w).mean()

                optimizer.zero_grad()
                loss.backward()
                torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
                optimizer.step()
                scheduler.step()

                total_loss += loss.item()
                n_steps += 1

            avg_loss = total_loss / max(n_steps, 1)
            print(f"  Epoch {epoch}/{args.epochs}: loss={avg_loss:.6f}",
                  flush=True)

            if args.wandb:
                _log_wandb({"train/loss": avg_loss, "train/epoch": epoch,
                            "task": short})

            if avg_loss < best_loss:
                best_loss = avg_loss
                _save_checkpoint(model, optimizer, epoch, avg_loss,
                                 args.checkpoint_dir, task_name, tag="best")

            if args.dry_run:
                print("  [dry-run] stopping after 1 epoch", flush=True)
                break

        _save_checkpoint(model, optimizer, epoch, avg_loss,
                         args.checkpoint_dir, task_name, tag="last")
        print(f"  Done: {short}, best_loss={best_loss:.6f}", flush=True)


# ---------------------------------------------------------------------------
# Training: Full VLA Mode
# ---------------------------------------------------------------------------

def train_full(args):
    device = torch.device(args.device if torch.cuda.is_available() else "cpu")
    print(f"=== Full VLA Mode ({args.mode.upper()}) on {device} ===",
          flush=True)

    try:
        from peft import LoraConfig, get_peft_model, TaskType
    except ImportError:
        raise RuntimeError("peft not installed: pip install peft")
    try:
        from transformers import AutoModelForVision2Seq, AutoProcessor
    except ImportError:
        raise RuntimeError("transformers not installed")

    # --- Load model ---
    print(f"Loading OpenVLA from {args.model_path} ...", flush=True)
    model = AutoModelForVision2Seq.from_pretrained(
        args.model_path,
        torch_dtype=torch.bfloat16,
        trust_remote_code=True,
        low_cpu_mem_usage=True,
    )
    processor = AutoProcessor.from_pretrained(
        args.model_path, trust_remote_code=True,
    )

    # --- Norm stats ---
    dataset_name = args.dataset_name
    if hasattr(model.config, "norm_stats"):
        norm_stats = model.config.norm_stats.get(dataset_name)
        if norm_stats is None:
            avail = list(model.config.norm_stats.keys())
            print(f"  WARNING: no norm_stats for '{dataset_name}', "
                  f"available: {avail}. Using first.", flush=True)
            norm_stats = model.config.norm_stats[avail[0]]
    else:
        stats_path = os.path.join(args.model_path, "dataset_statistics.json")
        with open(stats_path) as f:
            all_stats = json.load(f)
        norm_stats = all_stats.get(dataset_name, list(all_stats.values())[0])
    n_bins = getattr(model.config, "n_action_bins", 256)

    # --- LoRA ---
    lora_config = LoraConfig(
        r=args.lora_rank,
        lora_alpha=args.lora_alpha,
        lora_dropout=args.lora_dropout,
        target_modules=["q_proj", "k_proj", "v_proj", "o_proj"],
        task_type=TaskType.CAUSAL_LM,
        bias="none",
    )
    model = get_peft_model(model, lora_config)
    model.print_trainable_parameters()
    model = model.to(device)

    if args.wandb:
        _init_wandb(args, mode="full")

    task_names = _get_task_names(args)
    os.makedirs(args.checkpoint_dir, exist_ok=True)

    for task_name in task_names:
        short = task_name.replace("pick_up_the_", "").replace(
            "_and_place_it_in_the_basket", "")
        print(f"\n{'=' * 50}\nTask: {short}\n{'=' * 50}", flush=True)

        # --- AWR weights ---
        weights = None
        if args.mode == "awr":
            weights = _compute_task_awr_weights(
                task_name, args.iql_checkpoint_dir, args.features_dir,
                args.data_dir, args.temperature, args.clip_max,
            )
            if weights is None:
                print(f"  SKIP: AWR weights unavailable", flush=True)
                continue

        # --- Dataset ---
        dataset = LiberoVLADataset(
            args.data_dir, task_name, weights=weights,
        )
        loader = DataLoader(dataset, batch_size=args.batch_size,
                            shuffle=True, num_workers=2,
                            collate_fn=lambda b: b, drop_last=True)

        # --- Optimizer (reset per task) ---
        trainable = [p for p in model.parameters() if p.requires_grad]
        optimizer = optim.AdamW(trainable, lr=args.lr, weight_decay=1e-4)
        total_steps = args.epochs * len(loader)
        scheduler = optim.lr_scheduler.CosineAnnealingLR(
            optimizer, T_max=max(total_steps, 1))

        best_loss = float("inf")
        for epoch in range(1, args.epochs + 1):
            model.train()
            epoch_loss = 0.0
            n_steps = 0

            for step, batch in enumerate(loader):
                if args.max_steps and step >= args.max_steps:
                    break

                loss = _vla_train_step(
                    model, processor, batch, norm_stats, n_bins, device,
                )

                optimizer.zero_grad()
                loss.backward()
                torch.nn.utils.clip_grad_norm_(trainable, 1.0)
                optimizer.step()
                scheduler.step()

                epoch_loss += loss.item()
                n_steps += 1

                if (step + 1) % 10 == 0:
                    print(f"  E{epoch} S{step + 1}: "
                          f"loss={epoch_loss / n_steps:.6f}", flush=True)

            avg = epoch_loss / max(n_steps, 1)
            print(f"  Epoch {epoch}/{args.epochs}: loss={avg:.6f}",
                  flush=True)

            if args.wandb:
                _log_wandb({"train/loss": avg, "train/epoch": epoch,
                            "task": short})

            if avg < best_loss:
                best_loss = avg
                adapter_dir = os.path.join(
                    args.checkpoint_dir, f"{task_name}_best")
                model.save_pretrained(adapter_dir)
                print(f"  Saved best adapter → {adapter_dir}", flush=True)

            if args.dry_run:
                print("  [dry-run] stopping after 1 epoch", flush=True)
                break

        adapter_dir = os.path.join(args.checkpoint_dir, f"{task_name}_last")
        model.save_pretrained(adapter_dir)
        print(f"  Done: {short}, best_loss={best_loss:.6f}", flush=True)


def _vla_train_step(model, processor, batch, norm_stats, n_bins, device):
    """One gradient step for full VLA mode.

    Handles per-sample AWR weighting via manual CE from logits.
    """
    from PIL import Image as PILImage

    images = [PILImage.fromarray(b["image"]) for b in batch]
    instructions = [b["instruction"] for b in batch]
    actions = torch.tensor(
        np.stack([b["action"] for b in batch]), dtype=torch.float32)
    weights = torch.tensor(
        [b["weight"] for b in batch], dtype=torch.float32).to(device)

    # Discretize target actions
    target_bins = discretize_action(actions, norm_stats, n_bins)  # (B, 7)

    # Process inputs through the model's processor
    inputs = processor(
        text=instructions,
        images=images,
        return_tensors="pt",
        padding=True,
    )
    inputs = {k: v.to(device) if isinstance(v, torch.Tensor) else v
              for k, v in inputs.items()}

    # Forward pass
    outputs = model(**inputs)
    logits = outputs.logits  # (B, seq_len, vocab_size)

    # The action tokens are the last 7 tokens in the sequence.
    # Extract logits at those positions and compute per-sample CE.
    action_logits = logits[:, -7:, :]   # (B, 7, vocab_size)

    # Determine action token ID offset
    # OpenVLA maps bin k → token (vocab_size - n_bins + k) by convention
    vocab_size = logits.shape[-1]
    token_offset = vocab_size - n_bins
    target_token_ids = target_bins.to(device) + token_offset  # (B, 7)

    ce = nn.functional.cross_entropy(
        action_logits.reshape(-1, vocab_size),
        target_token_ids.reshape(-1),
        reduction="none",
    )
    per_sample = ce.view(len(batch), 7).mean(dim=1)    # (B,)
    loss = (per_sample * weights).mean()
    return loss


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _get_task_names(args):
    if args.task:
        return [args.task]
    feat_files = sorted(glob.glob(os.path.join(args.features_dir, "*.pt")))
    return [os.path.basename(f).replace(".pt", "") for f in feat_files]


def _compute_task_awr_weights(task_name, iql_dir, features_dir, data_dir,
                              temperature, clip_max):
    iql_path = os.path.join(iql_dir, f"{task_name}_iql.pt")
    feat_path = os.path.join(features_dir, f"{task_name}.pt")
    if not os.path.exists(iql_path) or not os.path.exists(feat_path):
        return None

    feat_data = torch.load(feat_path, map_location="cpu", weights_only=False)
    features = feat_data["features"]
    hdf5_path = os.path.join(data_dir, f"{task_name}_demo.hdf5")
    all_act = []
    with h5py.File(hdf5_path, "r") as hf:
        for dk in sorted(hf["data"].keys()):
            if dk.startswith("demo_"):
                all_act.append(
                    torch.from_numpy(hf[f"data/{dk}/actions"][:]).float())
    actions = torch.cat(all_act, 0)
    min_len = min(len(features), len(actions))

    weights, adv = compute_awr_weights(
        iql_path, features[:min_len], actions[:min_len],
        temperature=temperature, clip_max=clip_max,
    )
    print(f"  AWR: mean_w={weights.mean():.3f} std_w={weights.std():.3f} "
          f"adv_iqr={_iqr(adv):.4f}", flush=True)
    return weights


def _iqr(t):
    q75 = torch.quantile(t.float(), 0.75)
    q25 = torch.quantile(t.float(), 0.25)
    return (q75 - q25).item()


def _save_checkpoint(model, optimizer, epoch, loss, ckpt_dir, task_name,
                     tag="last"):
    path = os.path.join(ckpt_dir, f"{task_name}_{tag}.pt")
    torch.save({
        "model": model.state_dict(),
        "optimizer": optimizer.state_dict(),
        "epoch": epoch,
        "loss": loss,
    }, path)
    print(f"  Saved {tag} checkpoint → {path}", flush=True)


def _init_wandb(args, mode="lite"):
    try:
        import wandb
        name = args.wandb_run_name or f"phase2_{args.mode}_{mode}"
        wandb.init(project=args.wandb_project, name=name,
                   config=vars(args))
    except Exception as e:
        print(f"  WandB init failed: {e}", flush=True)


def _log_wandb(metrics):
    try:
        import wandb
        if wandb.run is not None:
            wandb.log(metrics)
    except Exception:
        pass


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args():
    p = argparse.ArgumentParser(
        description="AWR LoRA fine-tuning for OpenVLA on LIBERO")

    # Mode
    p.add_argument("--mode", choices=["awr", "bc"], default="awr")
    p.add_argument("--lite", action="store_true",
                   help="Train MLP on VIP features instead of full VLA")

    # Model (full mode)
    p.add_argument("--model-path", type=str,
                   default="/root/autodl-tmp/models/"
                           "openvla-7b-finetuned-libero-spatial")
    p.add_argument("--dataset-name", type=str, default="libero_spatial",
                   help="Key in norm_stats for action normalization")

    # Task selection
    p.add_argument("--task", type=str, default=None,
                   help="Single task name (without _demo.hdf5)")

    # Data paths
    p.add_argument("--data-dir", type=str,
                   default="./data/libero/libero_object")
    p.add_argument("--features-dir", type=str,
                   default="./artifacts/vip_features_all")
    p.add_argument("--iql-checkpoint-dir", type=str,
                   default="./artifacts/iql_checkpoints_scaled")

    # AWR hyperparams
    p.add_argument("--temperature", type=float, default=1.0,
                   help="AWR temperature (lower → more peaked weights)")
    p.add_argument("--clip-max", type=float, default=20.0,
                   help="Max AWR weight before normalization")

    # LoRA (full mode)
    p.add_argument("--lora-rank", type=int, default=16)
    p.add_argument("--lora-alpha", type=int, default=32)
    p.add_argument("--lora-dropout", type=float, default=0.05)

    # Training
    p.add_argument("--epochs", type=int, default=10)
    p.add_argument("--lr", type=float, default=2e-4)
    p.add_argument("--batch-size", type=int, default=4)
    p.add_argument("--max-steps", type=int, default=None,
                   help="Max steps per epoch (for testing)")

    # Output
    p.add_argument("--checkpoint-dir", type=str,
                   default="./artifacts/phase2_checkpoints")
    p.add_argument("--device", type=str, default="cuda:0")

    # WandB
    p.add_argument("--wandb", action="store_true")
    p.add_argument("--wandb-project", type=str, default="tad-phase2")
    p.add_argument("--wandb-run-name", type=str, default=None)

    # Debug
    p.add_argument("--dry-run", action="store_true",
                   help="1 epoch, 2 steps, no full save")
    return p.parse_args()


def main():
    args = parse_args()
    if args.dry_run:
        args.max_steps = args.max_steps or 2

    print(f"Phase 2 {'AWR' if args.mode == 'awr' else 'BC'} "
          f"({'lite' if args.lite else 'full VLA'})", flush=True)
    print(f"Config: lr={args.lr} epochs={args.epochs} "
          f"batch={args.batch_size} temp={args.temperature}", flush=True)

    if args.lite:
        train_lite(args)
    else:
        train_full(args)

    print("\nDone.", flush=True)


if __name__ == "__main__":
    main()
