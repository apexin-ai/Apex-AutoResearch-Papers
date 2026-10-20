# Plan018 Random Control Group — Prep Report

**Date**: 2026-05-14 ~17:00 server time

---

## Part A: Running Experiments Progress

### plan002-additive-b01-s43 (cuda:0)
- **PID**: 466128 (alive, etime=15:07)
- **Step**: 107/500 (21.4%)
- **Elapsed**: 16m28s, avg ~9.2s/step
- **tqdm ETA**: ~1h01m remaining → **~18:03 server time**
- **Recent metrics** (step 107): reward=0.768, PR=0.750, ISR=0.175

### plan002-additive-b01-s44 (cuda:1)
- **PID**: 466540 (alive, etime=14:38)
- **Step**: 99/500 (19.8%)
- **Elapsed**: 14m08s, avg ~8.6s/step
- **tqdm ETA**: ~48m remaining → **~17:48 server time**
- **Recent metrics** (step 99): reward=0.542, PR=0.500, ISR=0.417

### GPU Status
| GPU | Used | Total | Util |
|-----|------|-------|------|
| 0 | 80291 MiB | 97887 MiB | 93% |
| 1 | 80327 MiB | 97887 MiB | 0% |

### Disk
- `/root/autodl-tmp`: 139G/250G used (56%), 112G free — sufficient for 2 more runs

---

## Part B: Plan018 Launch Commands

**Prerequisite**: Wait for plan002 runs to finish. cuda:1 frees first (~17:48), cuda:0 frees ~18:03.

### plan018-additive-random-b01-s43 (cuda:1, launch after plan002-s44 finishes)

```bash
tmux new-session -d -s plan018-additive-random-b01-s43 \
  "bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
  export CUDA_VISIBLE_DEVICES=1 && \
  cd /root/solver-trace-ablation && \
  python scripts/train_grpo.py \
    --config configs/grpo_additive_bonus.yaml \
    --reward_mode additive_random \
    --beta 0.1 \
    --seed 43 \
    --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s43 \
    --no_wandb \
  2>&1 | tee /root/runs/solver-trace-ablation/plan018-additive-random-b01-s43.log'"
```

### plan018-additive-random-b01-s44 (cuda:0, launch after plan002-s43 finishes)

```bash
tmux new-session -d -s plan018-additive-random-b01-s44 \
  "bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
  export CUDA_VISIBLE_DEVICES=0 && \
  cd /root/solver-trace-ablation && \
  python scripts/train_grpo.py \
    --config configs/grpo_additive_bonus.yaml \
    --reward_mode additive_random \
    --beta 0.1 \
    --seed 44 \
    --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s44 \
    --no_wandb \
  2>&1 | tee /root/runs/solver-trace-ablation/plan018-additive-random-b01-s44.log'"
```

### Launch verification (run after each tmux command)

```bash
# Verify GPU assignment (C002)
nvidia-smi --query-compute-apps=pid,gpu_uuid,used_memory --format=csv,noheader

# Verify process alive
ps aux | grep train_grpo | grep -v grep

# Verify log starts
tail -5 /root/runs/solver-trace-ablation/plan018-additive-random-b01-s43.log
```

---

## Notes

1. **Config reuse**: Commands use `--config configs/grpo_additive_bonus.yaml` as base (provides model_path, data_path, num_steps=500, etc.), then override reward_mode/beta/seed/output_dir via CLI. This matches the pattern used for plan018-s42 and plan002 runs.
2. **C001**: data_path comes from config → `data/train_500_seed42.jsonl` ✓
3. **C002**: `export CUDA_VISIBLE_DEVICES=N` inside bash -c, not inline ✓
4. **C003**: `save_total_limit=1` hardcoded in train_grpo.py ✓
5. **C005**: CUDA_VISIBLE_DEVICES explicitly set ✓
6. **plan018-s42 reference**: Completed in 1h10m, PR=0.645, ISR=0.131 (eval: PR=0.79, ISR=0.098). Expected ~70min per run for s43/s44.
7. **Staggered launch**: cuda:1 frees ~15min before cuda:0. Can launch s43 first on cuda:1, then s44 on cuda:0 when available. Or wait for both to free and launch simultaneously.
