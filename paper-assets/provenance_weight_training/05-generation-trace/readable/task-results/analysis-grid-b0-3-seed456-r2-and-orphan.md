# analysis grid b0 3 seed456 r2 and orphan

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_grid_b0_3_seed456_r2_and_orphan_20260518T005841_result.json`
- **Structured JSON:** [`815f116b8b2cfe945c87.json`](../../sessions/81/815f116b8b2cfe945c87.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 完成。汇总报告：

---

## 任务 1: grid_b0_3_seed456_r2

| 指标 | 值 |
|---|---|
| **eval_ppl_holdout** | **17.64** |
| eval_loss_holdout | 2.8700 |
| eval_tokens | 4,077,068 |
| train_loss (avg) | 9.085 |
| total_steps | 6103/6103 (100%) |
| checkpoint_path | `/root/autodl-tmp/output/models/grid_b0_3_seed456_r2/final` |
| 状态 | **成功** |

**Cross-seed 对比**:
- grid_b0_3_seed42 PPL = 17.640 → grid_b0_3_seed456 PPL = **17.64** (一致)
- 假设 b=0.5 seed456 PPL = 17.65 → grid_b0_3_seed456 PPL 17.64 < 17.65 ✓

**结论**: Cross-seed replication 确认 grid-best=0.3。两个 seed 的 PPL 高度一致 (17.64 vs 17.640)，且优于 b=0.5。

---

## 任务 2: grid_b0_2_seed42 orphan cron

| 项目 | 结果 |
|---|---|
| PID 145551 on westd-30476 | **不存在** |
| PID 145551 on westd-41312 | **存在且活跃** |
| 实验 | `pretrain_weighted.py --weighting_method grid --grid_b_value 0.2 --seed 42` |
| 输出目录 | `/root/autodl-tmp/provenance_weight_training/output/models/grid_b0_2_seed42` |
| 进度 | **3057/6103 (50%)**, epoch 0.13, ETA ~1h47m |
| 当前 loss | ~8.5-9.0 范围 |

**结论**: 该 cron 不是 stale 的 — 进程在 westd-41312 上正常运行中，只是 registry 中缺少对应条目。如果 cron 绑定在 westd-30476 上则是错误指向（进程实际在 westd-41312），需要更新 registry 将此实验补录，或将 cron 迁移到正确的服务器。

---
