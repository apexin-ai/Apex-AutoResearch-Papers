# exp dpo train cuda3

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_dpo-train-cuda3_20260512T150843_result.json`
- **Structured JSON:** [`0388853155207271d939.json`](../../sessions/03/0388853155207271d939.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常进行，所有产出汇总：

## 结果

| 项目 | 状态 |
|------|------|
| **cuda:3 释放** | 已确认，无残留进程 |
| **DPO 训练 PID** | 170853 |
| **tmux session** | `dpo_train` |
| **GPU 3 显存** | 23094 MiB |
| **cuda:2 mvp-004** | 未受影响（PID 110596, 22096 MiB） |

## 训练指标（前 ~17 步）

- **loss**: 0.693 → 0.677~0.701 范围波动（初始阶段正常，lr warmup 中）
- **rewards/margins**: 从 0.0 开始缓慢上升，部分 step 已到 0.03+
- **rewards/accuracies**: 0.25~1.0 波动，尚未稳定

## 预估训练时长

- 总步数：**1077 steps**（1434 samples × 3 epochs / grad_accum=4）
- 平均速度：**~4.5 s/step**
- 预估总时长：**~1.3 小时**（1077 × 4.5s ≈ 4847s ≈ 81 min）
- 预计完成时间：约 **UTC 00:35**

日志路径：`/root/democalib/results/dpo_train.log`

---
