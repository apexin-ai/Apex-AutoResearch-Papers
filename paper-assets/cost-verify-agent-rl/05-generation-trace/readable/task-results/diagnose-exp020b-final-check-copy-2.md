# diagnose exp020b final check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp020b-final-check_20260515T010207_result.json`
- **Structured JSON:** [`ae2904891355b65dbe69.json`](../../sessions/ae/ae2904891355b65dbe69.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp020b 训练状态报告

### 状态：**仍在运行**，当前 step 23/30（77%）

**启动时间**：2026-05-15 06:12，已运行 ~2h53m

**预计剩余**：7 steps × ~450s/step ≈ **~52 分钟**

### Checkpoints
- `global_step_5`, `global_step_10`, `global_step_15`, `global_step_20`

### 关键 Metrics 趋势

| Metric | Step 0 (val) | Step 1 | Step 10 | Step 20 (train/val) | Step 23 |
|--------|-------------|--------|---------|---------------------|---------|
| **val success** | 0.0 | - | - | **0.0** | - |
| **train success** | - | 0.1875 | - | 0.125 | 0.078 |
| **train pass@16** | - | 0.75 | - | 1.0 | 0.25 |
| val action_is_valid | 0.167 | - | - | **0.692** | - |
| val action_is_effective | 0.575 | - | - | **1.0** | - |
| entropy | - | 0.068 | - | 0.045 | 0.036 |
| pg_loss | - | -0.0017 | - | -0.00067 | 0.00019 |
| grad_norm | - | 5.16 | - | 5.58 | 2.89 |
| ppo_kl | - | 0.0011 | - | 0.0092 | 0.0074 |

### 初步判断

**趋势令人担忧**：
- **val success 始终为 0.0**（step 0 和 step 20 都是 0）
- **train success 持续下降**：0.1875 → 0.125 → 0.078 → 0.047
- action_is_valid 和 action_is_effective 有显著提升（模型学会了生成格式正确的动作），但任务完成率反而下降
- entropy 持续下降（0.068 → 0.036），模型趋向确定性输出但没有学到正确策略
- pass@16 波动大且下降（0.75 → 1.0 → 0.25），说明多样性探索不稳定

下一次 validation 在 step 30 完成时。按目前趋势，最终 val success 大概率仍为 0，实验结论可能是 **negative**。建议等训练完成后再做最终判断。

---
