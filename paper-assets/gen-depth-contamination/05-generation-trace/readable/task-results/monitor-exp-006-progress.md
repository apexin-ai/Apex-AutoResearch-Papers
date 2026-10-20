# monitor exp 006 progress

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_exp_006_progress_20260514T025636_result.json`
- **Structured JSON:** [`fe949e15fc5bcbfb1681.json`](../../sessions/fe/fe949e15fc5bcbfb1681.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**exp-006 进度汇报：**

| 指标 | 状态 |
|------|------|
| **已完成** | **8 / 50 runs**（+ 1 正在 eval） |
| **当前 run** | `binary-ours_s456` — 训练已完成 (2814/2814 steps, loss=2.794)，正在用 lm-eval 评估 |
| **已完成列表** | `base_model`, `no-filter_s42/s123/s456/s789/s1024`, `binary-ours_s42/s123` |
| **GPU VRAM** | RTX 4090 D — 3861 MiB / 24564 MiB（eval 阶段，占用较低） |
| **GPU 利用率** | 0%（eval 间歇性使用 GPU） |

**时间估算：**
- 已运行 ~14h（05-13 21:02 → 05-14 10:57 UTC）
- 完成 ~8.5 runs → 平均 ~99 min/run（训练 ~41min + 评估 ~58min）
- 剩余 ~41.5 runs × 99 min ≈ **68.5h**
- **预估完成：~05-17 07:30 UTC**

注意：实际每 run 耗时（~99 min）远超预估的 46 min，主要是 lm-eval 评估时间比预期长。总耗时将从预估的 38h 膨胀到 ~82h。PID 已从 46129 变为 57675（子进程）。

---
