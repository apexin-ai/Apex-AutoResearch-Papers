"""
K=1 CRM training script.

Two-phase approach:
  Phase 1 (--precompute): Run frozen SmolVLA on LIBERO demos with multi-scale
      feature extraction hooks. Cache (multi_scale_obs, vla_action_k1,
      expert_action) to disk.
  Phase 2 (default): Load cached features, train MultiScaleCRM with
      multi-loss (L2 + direction + triplet + magnitude).

Usage:
  # Phase 1: precompute K=1 features with multi-scale extraction
  python train_crm_k1.py --precompute --benchmark object

  # Phase 2: train K=1 CRM
  python train_crm_k1.py --benchmark object --epochs 50

  # Use existing K=10 cache (fallback: single obs feature, sample[0] as K=1)
  python train_crm_k1.py --benchmark object --epochs 50 --reuse_k10_cache

  # End-to-end
  python train_crm_k1.py --benchmark object --epochs 50 --auto
"""
import argparse
import os
os.environ.setdefault("HF_HUB_OFFLINE", "1")
os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")
import sys
import json
import time
import signal
import traceback
from pathlib import Path

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from crm_k1_model import MultiScaleCRM, MultiScaleFeatureExtractor, CRMMultiLoss, EXTRACT_LAYERS
from utils import (
    set_seed, load_libero_demos, build_training_samples,
    CheckpointManager, CORRECTION_DIM, H_EFF, OBS_DIM, CHUNK_SIZE,
)


def parse_args():
    p = argparse.ArgumentParser(description="Train K=1 MultiScaleCRM on LIBERO demos")
    p.add_argument("--benchmark", type=str, nargs='+', default=["spatial"],
                   choices=["object", "spatial", "goal", "long", "90"])
    p.add_argument("--epochs", type=int, default=50)
    p.add_argument("--batch_size", type=int, default=512)
    p.add_argument("--lr", type=float, default=1e-3)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--output_dir", type=str,
                   default="/root/autodl-tmp/checkpoints/crm_k1/")
    p.add_argument("--cache_dir", type=str,
                   default="/root/autodl-tmp/crm_cache_k1/")
    p.add_argument("--k10_cache_dir", type=str,
                   default="/root/autodl-tmp/crm_cache/")
    p.add_argument("--obs_dim", type=int, default=OBS_DIM)
    p.add_argument("--hidden_dim", type=int, default=256)
    p.add_argument("--bottleneck_dim", type=int, default=192)
    p.add_argument("--max_correction_norm", type=float, default=1.42)
    p.add_argument("--aug_noise_min", type=float, default=0.02)
    p.add_argument("--aug_noise_max", type=float, default=0.1)
    p.add_argument("--aug_ratio", type=float, default=0.5)
    p.add_argument("--precompute", action="store_true")
    p.add_argument("--auto", action="store_true")
    p.add_argument("--reuse_k10_cache", action="store_true",
                   help="Use existing K=10 cache (single obs, sample[0] as K=1)")
    p.add_argument("--smolvla_path", type=str,
                   default="/root/autodl-tmp/models/smolvla_libero/")
    p.add_argument("--max_demos_per_task", type=int, default=50)
    p.add_argument("--val_split", type=float, default=0.1)
    p.add_argument("--log_every", type=int, default=50)
    p.add_argument("--precompute_batch_size", type=int, default=4)
    p.add_argument("--save_every", type=int, default=500)
    # Loss weights
    p.add_argument("--lambda_dir", type=float, default=0.1)
    p.add_argument("--lambda_tri", type=float, default=0.05)
    p.add_argument("--lambda_mag", type=float, default=0.01)
    p.add_argument("--loss_mode", type=str, default="multi",
                   choices=["mse", "multi"],
                   help="mse=L2 only (baseline), multi=L2+dir+tri+mag")
    return p.parse_args()


# ── Precomputation ──────────────────────────────────────────────────

def precompute_features_k1(args):
    """Run frozen SmolVLA on all demo timesteps with multi-scale hooks, K=1."""
    from smolvla_wrapper import SmolVLAWrapper

    benchmarks_to_run = []
    for bm in args.benchmark:
        cache_dir = Path(args.cache_dir) / bm
        if (cache_dir / "manifest.json").exists():
            print(f"[precompute] {bm}: cache already exists, skipping")
        else:
            benchmarks_to_run.append(bm)

    if not benchmarks_to_run:
        print("[precompute] All benchmarks cached, nothing to do")
        return

    print("[precompute] Loading SmolVLA...")
    wrapper = SmolVLAWrapper(args.smolvla_path)
    text_model = wrapper.flow.vlm_with_expert.vlm.model.text_model
    extractor = MultiScaleFeatureExtractor(text_model, EXTRACT_LAYERS)

    for bm in benchmarks_to_run:
        print(f"\n[precompute] Processing benchmark: {bm}")
        cache_dir = Path(args.cache_dir) / bm
        cache_dir.mkdir(parents=True, exist_ok=True)

        trajectories = load_libero_demos(bm, max_demos_per_task=args.max_demos_per_task)
        samples = build_training_samples(trajectories, h_eff=H_EFF, action_dim=CORRECTION_DIM)
        print(f"[precompute] {len(samples)} training samples from {len(trajectories)} trajectories")

        extractor.register()
        saved_count = 0
        t0 = time.time()

        try:
            for i, sample in enumerate(samples):
                imgs, img_masks, lt, lm, state = wrapper.preprocess_obs(
                    agentview_rgb=sample["agentview_rgb"],
                    task_name=sample["task_name"],
                    robot_state=sample["ee_states"],
                    eye_in_hand_rgb=sample["eye_in_hand_rgb"],
                )

                # Forward with hooks
                extractor.captured = {}
                obs_feat, kv_cache, pad_masks = wrapper.encode_prefix(
                    imgs, img_masks, lt, lm, state
                )
                multi_scale_feats = extractor.get_features(pad_masks)

                # K=1 sample
                vla_sample = wrapper.generate_k_samples(kv_cache, pad_masks, K=1)
                # vla_sample: (1, 1, chunk_size, 7) -> (chunk_size, 7)
                vla_action = vla_sample[0, 0, :H_EFF, :CORRECTION_DIM]

                sample_path = cache_dir / f"sample_{i:06d}.pt"
                torch.save({
                    "multi_scale_obs": torch.stack(
                        [f.squeeze(0).cpu() for f in multi_scale_feats]
                    ),  # (4, 960)
                    "obs_features": obs_feat.squeeze(0).cpu(),  # (960,) for fallback
                    "vla_action": vla_action.cpu(),  # (H_EFF, CORRECTION_DIM)
                    "expert_action": torch.tensor(
                        sample["expert_action"], dtype=torch.float32
                    ),  # (H_EFF, CORRECTION_DIM)
                    "task_name": sample["task_name"],
                }, sample_path)

                saved_count += 1
                if (saved_count % args.save_every == 0) or (i == len(samples) - 1):
                    elapsed = time.time() - t0
                    rate = saved_count / elapsed
                    print(f"  [{bm}] {saved_count}/{len(samples)} samples "
                          f"({rate:.1f} samples/s)")

        finally:
            extractor.remove()

        manifest = {
            "benchmark": bm,
            "n_samples": saved_count,
            "K": 1,
            "multi_scale": True,
            "extract_layers": EXTRACT_LAYERS,
            "obs_dim": OBS_DIM,
            "h_eff": H_EFF,
            "correction_dim": CORRECTION_DIM,
        }
        (cache_dir / "manifest.json").write_text(json.dumps(manifest, indent=2))
        print(f"[precompute] {bm}: saved {saved_count} samples in {time.time()-t0:.1f}s")


# ── Dataset ─────────────────────────────────────────────────────────

class CRMK1Dataset(Dataset):
    """Load precomputed K=1 multi-scale features."""

    def __init__(self, cache_dir, benchmarks, multi_scale=True):
        self.samples = []
        self.multi_scale = multi_scale

        for bm in benchmarks:
            bm_dir = Path(cache_dir) / bm
            if not bm_dir.exists():
                raise FileNotFoundError(f"Cache not found: {bm_dir}")
            sample_files = sorted(bm_dir.glob("sample_*.pt"))
            print(f"  [{bm}] {len(sample_files)} cached samples")
            self.samples.extend(sample_files)

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        data = torch.load(self.samples[idx], map_location="cpu", weights_only=True)
        return {
            "multi_scale_obs": data["multi_scale_obs"],  # (4, 960) or (960,)
            "obs_features": data.get("obs_features", data["multi_scale_obs"][-1]
                                     if data["multi_scale_obs"].dim() == 2
                                     else data["multi_scale_obs"]),
            "vla_action": data["vla_action"],       # (H_EFF, CORRECTION_DIM)
            "expert_action": data["expert_action"],  # (H_EFF, CORRECTION_DIM)
        }


class CRMK1FromK10Dataset(Dataset):
    """Load existing K=10 cache, use sample[0] as K=1 and obs_features as fallback."""

    def __init__(self, cache_dir, benchmarks):
        self.samples = []
        for bm in benchmarks:
            bm_dir = Path(cache_dir) / bm
            if not bm_dir.exists():
                raise FileNotFoundError(f"K=10 cache not found: {bm_dir}")
            sample_files = sorted(bm_dir.glob("sample_*.pt"))
            print(f"  [{bm}] {len(sample_files)} K=10 cached samples (reuse mode)")
            self.samples.extend(sample_files)

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        data = torch.load(self.samples[idx], map_location="cpu", weights_only=False)
        obs_feat = data["obs_features"]  # (960,)
        k_samples = data["k_samples"]    # (K, chunk_size, 7)
        expert = data["expert_action"]   # (H_EFF, 6)
        # Use first sample as K=1 action
        vla_action = k_samples[0, :H_EFF, :CORRECTION_DIM]
        return {
            "multi_scale_obs": obs_feat,  # single (960,) -> fallback mode
            "obs_features": obs_feat,
            "vla_action": vla_action,
            "expert_action": expert,
        }


# ── Training ────────────────────────────────────────────────────────

def compute_normalization_stats(dataset, num_scale_layers=4):
    """Compute mean/std for actions and multi-scale obs features."""
    all_actions = []
    all_obs = {i: [] for i in range(num_scale_layers)}
    is_multi_scale = None

    n = min(len(dataset), 10000)
    indices = np.random.choice(len(dataset), n, replace=False)

    for idx in indices:
        sample = dataset[idx]
        vla = sample["vla_action"].reshape(-1)  # (30,)
        all_actions.append(vla)

        ms = sample["multi_scale_obs"]
        if ms.dim() == 2 and ms.shape[0] == num_scale_layers:
            is_multi_scale = True
            for i in range(num_scale_layers):
                all_obs[i].append(ms[i])
        else:
            is_multi_scale = False
            all_obs[0].append(ms if ms.dim() == 1 else ms.squeeze())

    action_all = torch.stack(all_actions)
    action_mean = action_all.mean(0)
    action_std = action_all.std(0).clamp(min=1e-6)

    if is_multi_scale:
        obs_mean = torch.stack([torch.stack(all_obs[i]).mean(0) for i in range(num_scale_layers)])
        obs_std = torch.stack([torch.stack(all_obs[i]).std(0).clamp(min=1e-6) for i in range(num_scale_layers)])
    else:
        single_obs = torch.stack(all_obs[0])
        obs_mean = single_obs.mean(0)
        obs_std = single_obs.std(0).clamp(min=1e-6)

    return action_mean, action_std, obs_mean, obs_std


def train(args):
    """Train K=1 MultiScaleCRM."""
    set_seed(args.seed)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # Load dataset
    print("[train] Loading cached features...")
    if args.reuse_k10_cache:
        dataset = CRMK1FromK10Dataset(args.k10_cache_dir, args.benchmark)
        multi_scale = False
    else:
        dataset = CRMK1Dataset(args.cache_dir, args.benchmark, multi_scale=True)
        # Detect if multi-scale
        sample0 = dataset[0]
        multi_scale = (sample0["multi_scale_obs"].dim() == 2
                       and sample0["multi_scale_obs"].shape[0] == 4)

    print(f"[train] {len(dataset)} total samples, multi_scale={multi_scale}")

    # Train/val split
    n_val = int(len(dataset) * args.val_split)
    n_train = len(dataset) - n_val
    train_dataset, val_dataset = torch.utils.data.random_split(
        dataset, [n_train, n_val],
        generator=torch.Generator().manual_seed(args.seed)
    )

    train_loader = DataLoader(train_dataset, batch_size=args.batch_size,
                              shuffle=True, num_workers=2, pin_memory=True)
    val_loader = DataLoader(val_dataset, batch_size=args.batch_size,
                            shuffle=False, num_workers=2, pin_memory=True)

    print(f"[train] train={n_train}, val={n_val}, "
          f"batch_size={args.batch_size}, batches/epoch={len(train_loader)}")

    # Normalization stats
    print("[train] Computing normalization stats...")
    action_mean, action_std, obs_mean, obs_std = compute_normalization_stats(dataset)

    # Model
    num_scale = 4 if multi_scale else 4  # keep architecture same, fallback handles single
    crm = MultiScaleCRM(
        action_dim=H_EFF * CORRECTION_DIM,
        obs_dim=args.obs_dim,
        hidden_dim=args.hidden_dim,
        bottleneck_dim=args.bottleneck_dim,
        num_scale_layers=num_scale,
        max_correction_norm=args.max_correction_norm,
    ).to(device)

    crm.set_normalization_stats(action_mean.to(device), action_std.to(device),
                                obs_mean.to(device), obs_std.to(device))

    print(f"[train] MultiScaleCRM: {crm.count_parameters():,} params")

    # Loss
    if args.loss_mode == "multi":
        loss_fn = CRMMultiLoss(
            lambda_dir=args.lambda_dir,
            lambda_tri=args.lambda_tri,
            lambda_mag=args.lambda_mag,
        )
        print(f"[train] Multi-loss: lambda_dir={args.lambda_dir}, "
              f"lambda_tri={args.lambda_tri}, lambda_mag={args.lambda_mag}")
    else:
        loss_fn = None
        print("[train] MSE loss only")

    # Optimizer
    optimizer = torch.optim.AdamW(crm.parameters(), lr=args.lr, weight_decay=1e-4)
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=args.epochs)

    # Checkpoint
    Path(args.output_dir).mkdir(parents=True, exist_ok=True)
    ckpt_mgr = CheckpointManager(args.output_dir)

    # Noise scale for augmentation
    noise_scale = torch.linspace(args.aug_noise_min, args.aug_noise_max,
                                 CORRECTION_DIM).to(device)

    best_val_loss = float("inf")

    for epoch in range(1, args.epochs + 1):
        crm.train()
        epoch_loss = 0.0
        epoch_losses = {"l2": 0, "dir": 0, "tri": 0, "mag": 0}
        n_batches = 0

        for batch_idx, batch in enumerate(train_loader):
            ms_obs = batch["multi_scale_obs"].to(device)
            vla_action = batch["vla_action"].to(device)
            expert = batch["expert_action"].to(device)

            # Flatten actions
            ba_flat = vla_action.reshape(vla_action.shape[0], -1)  # (B, 30)
            expert_flat = expert.reshape(expert.shape[0], -1)      # (B, 30)

            # Prepare multi-scale obs
            if ms_obs.dim() == 3 and ms_obs.shape[1] == 4:
                obs_input = [ms_obs[:, i] for i in range(4)]
            else:
                obs_input = ms_obs  # (B, 960) fallback

            # Forward
            refined = crm(ba_flat, obs_input)

            # Loss
            if args.loss_mode == "multi":
                loss, ld = loss_fn(refined, expert_flat, ba_flat)
                for k in epoch_losses:
                    epoch_losses[k] += ld.get(k, 0)
            else:
                loss = nn.functional.mse_loss(refined, expert_flat)

            # Augmentation: perturb VLA action, keep expert target
            n_aug = int(ba_flat.shape[0] * args.aug_ratio)
            if n_aug > 0:
                aug_noise = noise_scale.repeat(H_EFF)
                aug_ba = ba_flat[:n_aug] + torch.randn_like(ba_flat[:n_aug]) * aug_noise
                if isinstance(obs_input, list):
                    aug_obs = [o[:n_aug] for o in obs_input]
                else:
                    aug_obs = obs_input[:n_aug]
                aug_refined = crm(aug_ba, aug_obs)
                if args.loss_mode == "multi":
                    aug_loss, _ = loss_fn(aug_refined, expert_flat[:n_aug], aug_ba)
                else:
                    aug_loss = nn.functional.mse_loss(aug_refined, expert_flat[:n_aug])
                loss = loss + 0.5 * aug_loss

            optimizer.zero_grad()
            loss.backward()
            torch.nn.utils.clip_grad_norm_(crm.parameters(), 1.0)
            optimizer.step()

            epoch_loss += loss.item()
            n_batches += 1

            if (batch_idx + 1) % args.log_every == 0:
                print(f"  epoch {epoch} batch {batch_idx+1}/{len(train_loader)} "
                      f"loss={loss.item():.6f}")

        scheduler.step()
        avg_train_loss = epoch_loss / max(n_batches, 1)

        # Validate
        crm.eval()
        val_loss = 0.0
        n_val = 0
        with torch.no_grad():
            for batch in val_loader:
                ms_obs = batch["multi_scale_obs"].to(device)
                vla_action = batch["vla_action"].to(device)
                expert = batch["expert_action"].to(device)
                ba_flat = vla_action.reshape(vla_action.shape[0], -1)
                expert_flat = expert.reshape(expert.shape[0], -1)

                if ms_obs.dim() == 3 and ms_obs.shape[1] == 4:
                    obs_input = [ms_obs[:, i] for i in range(4)]
                else:
                    obs_input = ms_obs

                refined = crm(ba_flat, obs_input)
                val_loss += nn.functional.mse_loss(refined, expert_flat).item()
                n_val += 1

        avg_val_loss = val_loss / max(n_val, 1)

        loss_str = f"train_loss={avg_train_loss:.6f}  val_loss={avg_val_loss:.6f}"
        if args.loss_mode == "multi":
            avg_ld = {k: v / max(n_batches, 1) for k, v in epoch_losses.items()}
            loss_str += f"  [l2={avg_ld['l2']:.4f} dir={avg_ld['dir']:.4f} " \
                        f"tri={avg_ld['tri']:.4f} mag={avg_ld['mag']:.4f}]"

        print(f"Epoch {epoch}/{args.epochs}  {loss_str}  "
              f"lr={scheduler.get_last_lr()[0]:.2e}")

        metrics = {"train_loss": avg_train_loss, "val_loss": avg_val_loss}
        ckpt_mgr.save(crm, optimizer, epoch, metrics)

        if avg_val_loss < best_val_loss:
            best_val_loss = avg_val_loss
            torch.save(crm.state_dict(), Path(args.output_dir) / "crm_k1_best.pt")
            print(f"  -> New best val_loss: {best_val_loss:.6f}")

    print(f"\n[train] Done. Best val_loss={best_val_loss:.6f}")
    print(f"[train] Checkpoints at {args.output_dir}")


def main():
    def _segfault_handler(signum, frame):
        print(f"[train_crm_k1] FATAL: caught signal {signum}", flush=True)
        traceback.print_stack(frame)
        sys.exit(139)

    signal.signal(signal.SIGSEGV, _segfault_handler)

    args = parse_args()
    print(f"[train_crm_k1] args: {vars(args)}")
    print(f"[train_crm_k1] device: {'cuda' if torch.cuda.is_available() else 'cpu'}")

    if args.precompute:
        precompute_features_k1(args)
        return

    if args.auto:
        needs_precompute = any(
            not (Path(args.cache_dir) / bm / "manifest.json").exists()
            for bm in args.benchmark
        )
        if needs_precompute:
            print("[auto] Cache not found, precomputing K=1 features...")
            precompute_features_k1(args)

    train(args)


if __name__ == "__main__":
    main()
