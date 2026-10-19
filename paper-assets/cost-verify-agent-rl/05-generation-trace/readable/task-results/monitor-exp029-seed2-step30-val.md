# monitor exp029 seed2 step30 val

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_exp029-seed2-step30-val_20260519T004612_result.json`
- **Structured JSON:** [`dae74d05547595ad5039.json`](../../sessions/da/dae74d05547595ad5039.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Step 30 + val eval 数据已获取。

---

## Step 30 监控报告

### Val 指标（step 30，16 episodes）

| 指标 | Step 15 (baseline) | Step 25 | **Step 30** | 趋势 |
|------|:---:|:---:|:---:|:---:|
| **val success** | 25.0% | 15.6% | **31.25%** | ↑ 恢复 |
| **val manager_invalid** | 0.8% | 51.0% | **46.7%** | ↓ 微降 |
| val action_is_valid | 67.8% | 41.0% | 47.7% | ↑ |
| val action_is_effective | 99.2% | 49.0% | 53.3% | ↑ |
| val pass@1 | 25.0% | 15.6% | 31.25% | ↑ |

### Train 指标趋势（step 28→29→30）

| 指标 | Step 28 | Step 29 | Step 30 |
|------|:---:|:---:|:---:|
| train success | 89.1% | 32.8% | 50.0% |
| train manager_invalid | 6.5% | 45.3% | 34.8% |
| KL (ppo_kl) | 0.016 | 0.060 | 0.016 |
| grad_norm | 3.08 | 9.98 | **13.73** |
| kl_loss | 0.065 | 0.101 | **0.162** |

### 判断：**部分恢复，但不稳定**

- **Val success 恢复到 31.25%**，超过 baseline (25%)，从 step 25 的 15.6% 大幅回升
- **manager_invalid_action 仍高企于 46.7%**（baseline 0.8%），说明模型学会了在高 invalid action rate 下"绕着走"来成功，但并没有真正修复 invalid action 问题
- **Train 极度不稳定**：step 28→29 success 从 89%→33% 的暴跌，说明训练方差极大
- **grad_norm 持续攀升**（3.08→9.98→13.73），kl_loss 也在涨（0.065→0.101→0.162），提示训练可能正在发散
- Step 29 的 KL spike (0.060) 回落到 step 30 的 0.016，但 grad_norm 没有回落

**风险**：grad_norm 和 kl_loss 的上升趋势 + train 方差极大，后续 step 有继续恶化的可能。建议关注 step 31-35 的趋势是否稳定。

---
