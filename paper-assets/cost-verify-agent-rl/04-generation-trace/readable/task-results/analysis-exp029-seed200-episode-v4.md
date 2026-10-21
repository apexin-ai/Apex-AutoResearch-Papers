# analysis exp029 seed200 episode v4

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp029_seed200_episode_v4_20260523T010940_result.json`
- **Structured JSON:** [`56837c4a724a2d9b8853.json`](../../sessions/56/56837c4a724a2d9b8853.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Got all data. Here's the structured analysis:

---

## exp029_seed200_episode_v4 分析报告

### 1. 训练完成状态
- **状态**: 正常完成，EXIT_CODE=0
- **总耗时**: 9016 秒（~2.50 小时）
- **训练步数**: 5 steps 全部完成（W&B 记录了 4 步 train metrics + 1 次 final eval）
- **Checkpoint**: `/root/autodl-tmp/checkpoints/exp029-seed200/global_step_5/`（含 model + optim，rank 0 & 1）

### 2. 每步训练指标（来自 W&B）

| Step | critic/score/mean | success | pass@8 | ppo_kl | kl_loss | response_length |
|------|-------------------|---------|--------|--------|---------|-----------------|
| 1 | **2.891** | 0.289 | 0.688 | -0.000183 | 0.000132 | 3630 |
| 2 | **0.156** | 0.016 | 0.063 | 0.000252 | 0.000528 | 8484 |
| 3 | **0.391** | 0.039 | 0.250 | 0.000198 | 0.002642 | 7340 |
| 4 | **1.953** | 0.195 | 0.500 | 0.000138 | 0.009868 | 4157 |
| 5* | **2.031** | ~0.20 | — | — | — | — |

*Step 5 metrics from log (W&B 未完整记录)

### 3. Eval 结果（step 5 后，32 episodes）
- **val-env/AlfworldSG/pass@1**: 0.125 (12.5%)
- **val-core/unknown/reward/mean@32**: 1.25
- **val-core/unknown/reward/best@32/mean**: 9.81
- **val-env/AlfworldSG/action_is_valid**: 0.643

### 4. KL 趋势
KL 极小，全程 ppo_kl < 0.001，远低于 50 阈值。KL 不是问题。

### 5. Reward 趋势分析
```
Step1: 2.89 ──▼ Step2: 0.16 (暴跌 94%) ──▲ Step3: 0.39 ──▲ Step4: 1.95 ──▲ Step5: 2.03
```
- **Step 2 发生严重 collapse**（reward 从 2.89 暴跌到 0.16，success 从 28.9% 降至 1.6%）
- Step 2 同时 response_length 飙升到 8484（原 3630），模型开始生成冗长无效输出
- **Step 3-5 逐步恢复**，但 step 5 reward (2.03) 仍低于 step 1 (2.89)
- 净方向：**下降**（step5 < step1）

### 6. 判断结论

| 项目 | 结果 |
|------|------|
| 训练完成 | Yes |
| Step5 reward > Step1 reward | **No** (2.03 < 2.89) |
| KL < 50 | Yes |
| ID reward 持续上升 | **No**（step 2 暴跌后恢复） |
| 模式 | **delayed**（中段 collapse + 部分恢复，趋势向上但未恢复到 baseline） |
| **推荐 conclusion** | **negative** |

**理由**: Step 2 发生严重 collapse，虽然后续恢复趋势良好（step 2→5 持续上升），但最终 reward 仍未超过初始值。与 healthy seeds（seed4/5/6 step5 > step1）不符。Eval pass@1 仅 12.5%，表现较弱。如果延长训练步数，恢复趋势可能使其达到 healthy 水平，但当前 5 步结果为 negative。

---
