# diagnose full gpu status check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_full-gpu-status-check_20260514T212022_result.json`
- **Structured JSON:** [`412a419d100d2c2eef89.json`](../../sessions/41/412a419d100d2c2eef89.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All experiments are still running. Here's the full status report:

---

## GPU 实时状态

### bjb1-18228 (4× RTX 4090)

| GPU | 显存占用 | 利用率 | 进程 | 实验 |
|-----|---------|--------|------|------|
| 0 | 17969/24564 MiB (73%) | 72% | PID 252489 (eval) + PID 256776 (train) | eval-acr-spatial-v4-default + crm-train-obs-only |
| 1 | 1423/24564 MiB (6%) | 21% | PID 231426 (eval) | eval-argmin-only-spatial |
| 2 | 1459/24564 MiB (6%) | 23% | PID 232820 (eval) | eval-tiny-correction-spatial |
| 3 | 2022/24564 MiB (8%) | 71% | PID 253085 (eval) + PID 257091 (train) | eval-acr-spatial-v4-small + crm-train-scalar-unc |

### bjb2-40593 (1× RTX 4090 D)

| GPU | 显存占用 | 利用率 | 进程 | 实验 |
|-----|---------|--------|------|------|
| 0 | 1933/24564 MiB (8%) | 11% | PID 143112 (eval) | eval-vla-mean-spatial |

---

## 实验状态

| 实验 | 服务器/GPU | 状态 | 进度 | 关键信息 |
|------|-----------|------|------|---------|
| eval-acr-spatial-v4-default | bjb1 cuda:0 | RUNNING | Task 1, rollout 5/10 | crm_v3_norm, max_norm=default |
| eval-argmin-only-spatial | bjb1 cuda:1 | RUNNING | Task 3 完成, 进行中 | reconvla baseline (argmin) |
| eval-tiny-correction-spatial | bjb1 cuda:2 | RUNNING | Task 4, rollout 5/10 | crm_v2, max_norm=0.05 |
| eval-acr-spatial-v4-small | bjb1 cuda:3 | RUNNING | Task 1, rollout 5/10 | crm_v3_norm, max_norm=0.1 |
| crm-train-obs-only | bjb1 cuda:0 | RUNNING | Epoch 20/50 | best val_loss=0.016765 |
| crm-train-scalar-unc | bjb1 cuda:3 | RUNNING | Epoch 21/50 | best val_loss=0.041973 |
| eval-vla-mean-spatial | bjb2 cuda:0 | RUNNING | Task 9, rollout 5/10 | vla_only baseline (mean), 接近完成 |

---

## 各实验详细进度

### eval-acr-spatial-v4-default (bjb1 cuda:0)
- 模式: acr_vla, CRM: crm_v3_norm/perdof, max_correction_norm=None
- 刚开始: Task 1 rollout 5/10, 0/5 success

### eval-argmin-only-spatial (bjb1 cuda:1)
- 模式: reconvla (argmin baseline, 无 CRM)
- 已完成 3 个 task:

| Task | Success Rate |
|------|-------------|
| between_plate_and_ramekin | 60% (6/10) |
| next_to_ramekin | 100% (10/10) |
| from_table_center | 0% (0/10) |

### eval-tiny-correction-spatial (bjb1 cuda:2)
- 模式: acr_vla, CRM: crm_v2/perdof, max_correction_norm=0.05
- 已完成 3 个 task, Task 4 进行中:

| Task | Success Rate |
|------|-------------|
| between_plate_and_ramekin | 70% (7/10) |
| next_to_ramekin | 90% (9/10) |
| from_table_center | 0% (0/10) |
| on_cookie_box | 进行中 (1/5 at rollout 5) |

### eval-acr-spatial-v4-small (bjb1 cuda:3)
- 模式: acr_vla, CRM: crm_v3_norm/perdof, max_correction_norm=0.1
- 刚开始: Task 1 rollout 5/10, 3/5 success

### crm-train-obs-only (bjb1 cuda:0, PID 256771)
- Epoch 20/50, best val_loss=0.016765 (epoch 20), 持续改善中
- Checkpoint: `/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt`

### crm-train-scalar-unc (bjb1 cuda:3, PID 257086)
- Epoch 21/50, best val_loss=0.041973 (epoch 20), 仍在收敛
- Checkpoint: `/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt`

### eval-vla-mean-spatial (bjb2 cuda:0) — 最接近完成
- 模式: vla_only, baseline_mode=mean (无 CRM)
- 已完成 8 个 task, Task 9 进行中:

| Task | Success Rate |
|------|-------------|
| between_plate_and_ramekin | 70% (7/10) |
| next_to_ramekin | **100% (10/10)** |
| from_table_center | 0% (0/10) |
| on_cookie_box | 30% (3/10) |
| in_top_drawer | 0% (0/10) |
| on_ramekin | 0% (0/10) |
| next_to_cookie_box | **80% (8/10)** |
| on_stove | 0% (0/10) |
| next_to_plate | 进行中 (1/5 at rollout 5) |
| on_wooden_shelf | 待运行 |

当前累计: 28/80 = 35.0% (前8个task)

---

## Registry 更新记录

无 — 所有 7 个实验仍在运行中，暂无需更新 registry。

**总结**: 所有实验正常运行。bjb2 的 eval-vla-mean-spatial 最接近完成（8/10 tasks done, 当前 ~35% overall）。两个 CRM ablation 训练到 epoch 20-21/50，约 40% 进度。bjb1 的 4 个 eval 实验分布在 task 1-4 不等，预计还需数小时。

---
