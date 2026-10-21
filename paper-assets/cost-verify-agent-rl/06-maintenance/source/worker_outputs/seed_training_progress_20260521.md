# Seed Training Progress Report — 2026-05-21 19:20 UTC

## Overview

| Experiment | Server | Step | Progress | Train Success | Val Success (step 5) | ETA |
|---|---|---|---|---|---|---|
| seed4_v2 | bjb1-17606 (cuda:0,1) | 5/15 | 33% | 0.148 (step 3) | 0.094 (step 0 only) | ~00:30 May 22 |
| seed5_v2 | westd-47453 (cuda:0,1) | 9/15 | 60% | 0.438 (step 9) | 0.063 (step 5) | ~21:00 May 21 |
| seed6_v3 | westd-47453 (cuda:2,3) | 8/15 | 53% | 0.422 (step 6) | 0.219 (step 5) | ~21:30 May 21 |

All 3 experiments running normally. All GPUs at 100% utilization.

---

## Detailed Per-Seed Status

### exp029_seed4_v2 (bjb1-17606)
- **W&B**: https://wandb.ai/xiaoyucorynne-/cost-verify-agent-rl/runs/fb1o765g
- **Progress**: 5/15 steps (33%), ~1804s/step (~30 min/step)
- **Elapsed**: 2h23m, ETA ~5h remaining
- **Checkpoint**: global_step_5 saved (21GB)

**Train metrics trajectory**:
| Step | success | pass@8 | response_length |
|------|---------|--------|-----------------|
| 1 | 0.133 | 0.563 | 3798 |
| 3 | 0.148 | 0.438 | 6817 |

**Val metrics** (step 0 initial only, step 5 eval not yet completed):
- val-env/AlfworldSG/success: 0.094 (3/32)
- val-core/unknown/reward/mean@32: 0.938

**Note**: seed4 train success (0.13-0.15) is significantly lower than seed5/seed6 (~0.42-0.47). Also the slowest of the 3 seeds (~30min/step vs ~17-20min/step on westd).

### exp029_seed5_v2 (westd-47453, cuda:0,1)
- **W&B**: https://wandb.ai/xiaoyucorynne-/cost-verify-agent-rl/runs/yyoghk1f
- **Progress**: 9/15 steps (60%), ~1083-1187s/step (~18-20 min/step)
- **Elapsed**: 2h42m, ETA ~2h remaining
- **Checkpoint**: global_step_5 saved (21GB)

**Train metrics trajectory**:
| Step | success | pass@8 | response_length |
|------|---------|--------|-----------------|
| 1 | 0.469 | 1.0 | 1746 |
| 5 | 0.422 | 1.0 | 2066 |
| 9 | 0.438 | 1.0 | 5697 |

**Val metrics**:
| Step | val success | val reward@32 |
|------|-------------|---------------|
| 0 | 0.031 | 0.313 |
| 5 | 0.063 | 0.625 |

**Note**: Train success stable at ~0.42-0.47 but val success still very low (0.063). Large train-val gap — possible overfitting or distribution mismatch. Response length growing (1746 → 5697).

### exp029_seed6_v3 (westd-47453, cuda:2,3)
- **W&B**: https://wandb.ai/xiaoyucorynne-/cost-verify-agent-rl/runs/2bbyvsdr
- **Progress**: 8/15 steps (53%), ~1011-1423s/step (~17-24 min/step)
- **Elapsed**: 2h48m, ETA ~2h remaining
- **Checkpoint**: global_step_5 saved (21GB)

**Train metrics trajectory**:
| Step | success | pass@8 | response_length |
|------|---------|--------|-----------------|
| 1 | 0.070 | 0.313 | 8083 |
| 6 | 0.422 | 0.875 | 2199 |

**Val metrics**:
| Step | val success | val reward@32 |
|------|-------------|---------------|
| 0 | 0.094 | 0.938 |
| 5 | 0.219 | 2.188 |

**Note**: Strong recovery from very low step-1 (0.07 → 0.42). Best val success among all 3 seeds (0.219). Response length decreased (8083 → 2199), suggesting the model is learning more efficient action sequences.

---

## GPU Utilization

| Server | GPU | Utilization | Memory Used | Memory Total | Usage % |
|--------|-----|-------------|-------------|--------------|---------|
| bjb1-17606 | cuda:0 | 100% | 44,457 MiB | 97,887 MiB | 45% |
| bjb1-17606 | cuda:1 | 100% | 44,821 MiB | 97,887 MiB | 46% |
| westd-47453 | cuda:0 | 100% | 97,247 MiB | 97,887 MiB | 99% |
| westd-47453 | cuda:1 | 100% | 97,247 MiB | 97,887 MiB | 99% |
| westd-47453 | cuda:2 | 100% | 93,437 MiB | 97,887 MiB | 95% |
| westd-47453 | cuda:3 | 100% | 93,437 MiB | 97,887 MiB | 95% |

**Notable**: bjb1 only uses ~45% GPU memory vs westd's 95-99%. bjb1 also trains ~1.5x slower per step. The memory and speed difference may be due to different vLLM/generation configurations or GPU architecture differences between the two servers.

---

## Disk Space

| Server | Partition | Used | Available | Usage % |
|--------|-----------|------|-----------|---------|
| bjb1-17606 | / (root) | 8.3G | 22G | 28% |
| bjb1-17606 | /root/autodl-tmp | 196G | 55G | 79% |
| westd-47453 | / (root) | 14G | 17G | 46% |
| westd-47453 | /root/autodl-tmp | 170G | 81G | 68% |

**Checkpoint sizes**: All 3 seeds have 1 checkpoint (global_step_5), each 21GB.
- bjb1: 55GB free, next checkpoint at step 10 + step 15 = ~8.4GB additional needed. **OK**.
- westd: 81GB free, 2 experiments × 2 more checkpoints each × ~4.2GB = ~17GB additional needed. **OK**.

---

## Risks & Observations

1. **seed4 train success significantly lower** (0.13-0.15) than seed5/seed6 (~0.42). May indicate this seed is stuck in a suboptimal region. Monitor closely at step 5 eval.

2. **seed5 train-val gap**: Train success ~0.44 but val success only 0.063. Possible overfitting or distribution shift between train/val environments.

3. **seed6 is the best performer**: Both highest val success (0.219) and strong train recovery. Response length decreasing is a positive signal.

4. **bjb1 disk at 79%**: Not critical now but monitor — 55GB free with ~8.4GB more checkpoints expected.

5. **westd GPU memory near capacity** (95-99%): No immediate risk but no headroom for unexpected memory spikes during longer rollouts.

6. **Speed disparity**: bjb1 at ~30min/step vs westd at ~18-20min/step. seed4 will finish ~3h after seed5/seed6. All configs appear identical except seed values, so the speed difference is server-level.
