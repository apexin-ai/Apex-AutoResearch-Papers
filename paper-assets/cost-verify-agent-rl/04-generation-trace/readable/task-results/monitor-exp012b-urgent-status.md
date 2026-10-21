# monitor exp012b urgent status

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_exp012b-urgent-status_20260514T073713_result.json`
- **Structured JSON:** [`bc7368fe8ce47f12d94f.json`](../../sessions/bc/bc7368fe8ce47f12d94f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp012b 状态报告

### 1. 进程状态：✅ 存活
- PID 233689 运行中（52 min）
- 两块 RTX PRO 6000 各占用 ~48GB（ray::WorkerDict）
- GPU-Util 0% — 正在执行 step 8 rollout（vLLM 推理间歇期，正常）
- 训练进度：**27% (8/30)**，预计剩余 ~4.5h

### 2. 已完成到 step 7（step 8 进行中）

### 3. 指标表格

| 指标 | Step 5 (val) | Step 6 (train) | Step 7 (train) | exp010 Step 6 |
|------|-------------|----------------|----------------|---------------|
| **success** | 0.0% | **8.59%** | ⚠️ **0.0%** | 3.13% |
| **action_is_valid** | 67.9% | 61.3% | 68.5% | 66.9% |
| action_is_effective | 98.3% | 87.7% | 90.5% | — |
| **pass@16** | — | **50.0%** | ⚠️ **0.0%** | 12.5% (pass@8) |
| pg_loss | — | -0.000286 | 0.0 | — |
| ppo_kl | — | 0.00390 | 0.00439 | — |
| entropy | — | 0.1006 | 0.0904 | — |
| grad_norm | — | **1.477** | **0.094** | — |
| critic/score/mean | — | 0.859 | 0.0 | — |
| critic/rewards/mean | — | 0.859 | 0.0 | — |

### 4. 趋势判断：⚠️ 崩塌复现

Step 6 表现强于 exp010（success 8.6% vs 3.1%, pass@16 50% vs 12.5%），但 **step 7 立即崩塌到 0%**。崩塌标志：

- success 8.6% → 0%
- pass@16 50% → 0%
- critic/rewards 0.859 → 0.0（全批次无 reward）
- grad_norm 1.477 → 0.094（梯度几乎消失）
- pg_loss → 精确 0.0（无梯度更新信号）

模式与 exp010 一致（exp010 在 step 6 崩塌），exp012b 多撑了一步但同样不可逆崩塌。Reward fix 延缓但未解决根因。

### 5. ⚠️ Step 7 起 train success = 0%

当前 step 8 正在执行，但根据 step 7 的完全崩塌（rewards/score 全零、梯度消失），后续 step 大概率维持 0%，继续跑下去价值有限。

---
