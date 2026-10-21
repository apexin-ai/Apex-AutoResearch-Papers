"""Patch train_crm_k1.py: add wandb + batch precompute."""
import sys

filepath = "/root/acr-vla-conformal-refinement/src/train_crm_k1.py"
with open(filepath) as f:
    content = f.read()

original = content

# 1. Add wandb import
content = content.replace(
    "import numpy as np\n",
    "import numpy as np\nimport wandb\n",
    1,
)

# 2. Add wandb CLI args before loss_mode
content = content.replace(
    '    p.add_argument("--loss_mode"',
    '    p.add_argument("--wandb_project", type=str, default="acr-vla-conformal-refinement")\n'
    '    p.add_argument("--wandb_run_name", type=str, default="crm-k1-train")\n'
    '    # Loss weights\n'  # keep the existing comment placement
    '    p.add_argument("--loss_mode"',
    1,
)
# Remove duplicate "# Loss weights" comment that was already there
content = content.replace(
    "    # Loss weights\n    # Loss weights\n",
    "    # Loss weights\n",
)

# 3. Replace serial precompute loop with batched version
OLD_PRECOMPUTE = '''        extractor.register()
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
            extractor.remove()'''

NEW_PRECOMPUTE = '''        extractor.register()
        saved_count = 0
        t0 = time.time()
        batch_size = args.precompute_batch_size
        print(f"[precompute] Using batch_size={batch_size}")

        try:
            for batch_start in range(0, len(samples), batch_size):
                batch_end = min(batch_start + batch_size, len(samples))
                batch_samples = samples[batch_start:batch_end]
                cur_bs = len(batch_samples)

                batch_obs = [
                    {
                        "agentview_rgb": s["agentview_rgb"],
                        "task_name": s["task_name"],
                        "ee_states": s["ee_states"],
                        "eye_in_hand_rgb": s.get("eye_in_hand_rgb"),
                    }
                    for s in batch_samples
                ]
                imgs, img_masks, lt, lm, state = wrapper.preprocess_obs_batch(batch_obs)

                extractor.captured = {}
                obs_feat, kv_cache, pad_masks = wrapper.encode_prefix(
                    imgs, img_masks, lt, lm, state
                )
                multi_scale_feats = extractor.get_features(pad_masks)

                vla_batch = wrapper.generate_k_samples(kv_cache, pad_masks, K=1)

                for j in range(cur_bs):
                    global_idx = batch_start + j
                    vla_action = vla_batch[j, 0, :H_EFF, :CORRECTION_DIM]

                    sample_path = cache_dir / f"sample_{global_idx:06d}.pt"
                    torch.save({
                        "multi_scale_obs": torch.stack(
                            [f[j].cpu() for f in multi_scale_feats]
                        ),  # (4, 960)
                        "obs_features": obs_feat[j].cpu(),  # (960,)
                        "vla_action": vla_action.cpu(),  # (H_EFF, CORRECTION_DIM)
                        "expert_action": torch.tensor(
                            batch_samples[j]["expert_action"], dtype=torch.float32
                        ),  # (H_EFF, CORRECTION_DIM)
                        "task_name": batch_samples[j]["task_name"],
                    }, sample_path)
                    saved_count += 1

                if (saved_count % args.save_every == 0) or (batch_end == len(samples)):
                    elapsed = time.time() - t0
                    rate = saved_count / elapsed
                    print(f"  [{bm}] {saved_count}/{len(samples)} samples "
                          f"({rate:.1f} samples/s)")

        finally:
            extractor.remove()'''

if OLD_PRECOMPUTE not in content:
    print("ERROR: Could not find precompute loop to replace")
    sys.exit(1)
content = content.replace(OLD_PRECOMPUTE, NEW_PRECOMPUTE, 1)

# 4. Add wandb.init before training loop
OLD_TRAIN_START = '    best_val_loss = float("inf")\n\n    for epoch in range(1, args.epochs + 1):'

NEW_TRAIN_START = '''    best_val_loss = float("inf")

    wandb.init(
        project=args.wandb_project,
        name=args.wandb_run_name,
        config={
            "epochs": args.epochs,
            "batch_size": args.batch_size,
            "lr": args.lr,
            "seed": args.seed,
            "hidden_dim": args.hidden_dim,
            "bottleneck_dim": args.bottleneck_dim,
            "obs_dim": args.obs_dim,
            "max_correction_norm": args.max_correction_norm,
            "loss_mode": args.loss_mode,
            "lambda_dir": args.lambda_dir,
            "lambda_tri": args.lambda_tri,
            "lambda_mag": args.lambda_mag,
            "aug_ratio": args.aug_ratio,
            "aug_noise_min": args.aug_noise_min,
            "aug_noise_max": args.aug_noise_max,
            "benchmarks": args.benchmark,
            "n_train": n_train,
            "n_val": n_val,
            "model_params": crm.count_parameters(),
            "reuse_k10_cache": args.reuse_k10_cache,
        },
    )

    for epoch in range(1, args.epochs + 1):'''

if OLD_TRAIN_START not in content:
    print("ERROR: Could not find train loop start")
    sys.exit(1)
content = content.replace(OLD_TRAIN_START, NEW_TRAIN_START, 1)

# 5. Add wandb.log after epoch metrics print
OLD_EPOCH_LOG = '''        print(f"Epoch {epoch}/{args.epochs}  {loss_str}  "
              f"lr={scheduler.get_last_lr()[0]:.2e}")

        metrics = {"train_loss": avg_train_loss, "val_loss": avg_val_loss}'''

NEW_EPOCH_LOG = '''        print(f"Epoch {epoch}/{args.epochs}  {loss_str}  "
              f"lr={scheduler.get_last_lr()[0]:.2e}")

        log_dict = {
            "train_loss": avg_train_loss,
            "val_loss": avg_val_loss,
            "lr": scheduler.get_last_lr()[0],
            "epoch": epoch,
        }
        if args.loss_mode == "multi":
            for k, v in avg_ld.items():
                log_dict[f"loss_{k}"] = v
        wandb.log(log_dict)

        metrics = {"train_loss": avg_train_loss, "val_loss": avg_val_loss}'''

if OLD_EPOCH_LOG not in content:
    print("ERROR: Could not find epoch log section")
    sys.exit(1)
content = content.replace(OLD_EPOCH_LOG, NEW_EPOCH_LOG, 1)

# 6. Add wandb.finish at end of train
OLD_TRAIN_END = '    print(f"[train] Checkpoints at {args.output_dir}")'
NEW_TRAIN_END = '    print(f"[train] Checkpoints at {args.output_dir}")\n    wandb.finish()'

if OLD_TRAIN_END not in content:
    print("ERROR: Could not find train end")
    sys.exit(1)
content = content.replace(OLD_TRAIN_END, NEW_TRAIN_END, 1)

# Write
with open(filepath, "w") as f:
    f.write(content)

# Verify
n_changes = sum(1 for a, b in zip(original.splitlines(), content.splitlines()) if a != b)
print(f"Patch applied. Lines changed/added: file went from {len(original.splitlines())} to {len(content.splitlines())} lines")
print("Changes: +wandb import, +wandb args, +batch precompute, +wandb.init, +wandb.log, +wandb.finish")
