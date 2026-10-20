# code grpo v5 step50 check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_grpo-v5-step50-check_20260515T123228_result.json`
- **Structured JSON:** [`ff93ab775667733a7de2.json`](../../sessions/ff/ff93ab775667733a7de2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据完整了。汇总如下：

## GRPO v5 训练状态报告

### 1. 进度
- **当前**: step 89 / 250 (36%)
- **进程**: PID 498474，运行 2h59m，存活
- **ETA**: 约 5h10m 后完成（~115s/step × 161 steps remaining）

### 2. Metrics 趋势

| Step | Reward | Grad Norm | Clipped Ratio | Loss | frac_zero_std |
|------|--------|-----------|---------------|------|---------------|
| 10 | 0.014 | 2.609 | 94.4% | 0.0050 | 95% |
| 20 | 0.026 | 1.328 | 95.6% | 0.0048 | 87.5% |
| 30 | 0.020 | 0.027 | 95.0% | 0.0064 | 87.5% |
| 40 | **0.033** | 0.018 | 95.0% | 0.0109 | 87.5% |
| 50 | 0.025 | 0.027 | 93.1% | 0.0117 | 90% |
| 60 | 0.019 | 0.008 | 96.3% | 0.0063 | 92.5% |
| 70 | 0.014 | 0.016 | 96.3% | 0.0097 | 90% |
| 80 | **0.000** | 0.010 | **97.5%** | 0.00002 | **100%** |

### 3. 诊断

**训练已实质性崩溃，建议立即停止。** 三个致命信号：

1. **Reward 归零**: step 40 达到峰值 0.033 后持续下降，step 80 直接归零。`frac_reward_zero_std=1.0` 说明 **100% 的样本 reward 都是 0**，完全没有正向信号。

2. **Grad norm 坍塌**: step 10 的 2.6 → step 30 骤降到 0.027 → step 80 仅 0.01。模型已经停止学习，梯度本质上是噪声。

3. **Clipped ratio 居高不下（93-97.5%）**: 平均生成长度 ~500/512，几乎所有 completion 都被截断。模型根本无法在 512 token 内完成推理 → 无法产生正确答案 → 无 reward → 无梯度。

### 4. 根因

**max_completion_length=512 是瓶颈。** 模型需要更长的推理链来解题，但 512 的上限导致生成被截断，正确率极低。从样本看，模型在尝试详细解题但总是被截断在中间。

### 5. 建议

**应该切 v6（max_completion_length=1024）。** 当前 v5 继续跑下去没有意义——reward 已归零、梯度已坍塌，不会恢复。剩余 5 小时的 GPU 时间会浪费。

是否现在就 kill PID 498474 并启动 v6？

---
