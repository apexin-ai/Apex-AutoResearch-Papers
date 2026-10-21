# monitor factorial step5plus

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_factorial_step5plus_20260518T011316_result.json`
- **Structured JSON:** [`47ba148cd014a899203e.json`](../../sessions/47/47ba148cd014a899203e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Process still alive. Step 5 is the latest completed; step 6 rollout is likely in progress.

## 完整 Step-by-Step Metrics 表格

| Metric | Step 0 (val) | Step 1 | Step 2 | Step 3 | Step 4 | Step 5 |
|---|---|---|---|---|---|---|
| **train success** | — | **20.31%** | **6.25%** | **5.47%** | **3.13%** | **15.63%** |
| train pass@8 | — | 68.75% | 31.25% | 31.25% | 18.75% | 62.50% |
| train action_valid | — | 85.64% | 83.96% | 79.54% | 83.70% | 79.92% |
| train action_effective | — | 97.04% | 97.32% | 94.87% | 94.29% | 91.28% |
| entropy | — | 0.359 | 0.569 | 0.567 | 0.617 | 0.699 |
| kl_loss | — | 0.238 | 0.208 | **1.077** | 0.638 | 0.735 |
| pg_loss | — | 0.0121 | 0.0118 | 0.0126 | 0.0114 | 0.0100 |
| grad_norm | — | 18.27 | 14.73 | 12.73 | 11.33 | 9.59 |
| critic score mean | — | 1.367 | 0.419 | 0.385 | 0.182 | 0.768 |
| **val success** | **2.24%** | — | — | — | — | **5.97%** |
| val action_valid | 37.80% | — | — | — | — | 57.65% |
| val action_effective | 71.94% | — | — | — | — | 66.63% |
| val manager_invalid | 28.06% | — | — | — | — | 33.37% |

## 判断：场景 A（回升）

**Step 5 train success 从 3.13% 反弹至 15.63%**，pass@8 从 18.75% 回到 62.50%，critic score 也从 0.182 回升至 0.768。这是明确的回升信号。

关键观察：
1. **Train success 呈 V 型曲线**：20.3% → 6.25% → 5.47% → 3.13% → **15.63%**。Step 1-4 的下降可能是 policy 探索新策略空间的过程（entropy 单调上升 0.36→0.70 支持此解读）。
2. **Val success 5.97%**（step 0 初始 2.24% → step 5 5.97%）：改善有限，但注意 val 用的是 AlfworldOOD（域外），train 用的是 AlfworldSG，分布不同。Val action_valid 从 37.8% 提升到 57.6% 是实质性改善。
3. **Entropy 单调上升**（0.36→0.70）：模型持续增加探索性，step 5 的回升可能正是探索收益开始兑现。
4. **Grad norm 持续下降**（18.3→9.6）：训练趋于稳定。
5. **kl_loss 在 step 3 有个 spike（1.077）**，之后回落，表明 policy 经历了较大更新后稳定下来。

进程仍在运行，step 6 rollout 中。

---
