# diagnose intervention c final and c prime progress

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_intervention_c_final_and_c_prime_progress_20260521T222518_result.json`
- **Structured JSON:** [`59edae9b9fe782f14358.json`](../../sessions/59/59edae9b9fe782f14358.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Part A: Intervention C 最终结果（westd-47453）— **Negative**

进程已正常退出 (EXIT_CODE=0)，7/7 steps 完成。

### Step 7（最终）关键指标

| 指标 | Train | Val |
|------|-------|-----|
| success | 15.625% | 9.375% |
| response_length (per-episode) | 870.25 | 927.44 |
| response_length/mean (total trajectory) | **7170** | — |
| pass@N | pass@8: 50% | pass@1: 9.375% |
| aborted_ratio | 0.0 | — |
| pg_loss | 6.72e-05 | — |
| kl_loss | 0.0204 | — |
| grad_norm | 1.31 | — |

### 关键对比：Step 6 → Step 7 崩溃

| 指标 | Step 6 | Step 7 |
|------|--------|--------|
| train_success | **38.28%** | 15.625% |
| train_resp_len | 745 | 870 |
| response_length/mean | 4662 | **7170** |
| pass@8 | 93.75% | 50% |

**结论**：Hard cap (512 tokens/turn, 20 turns) **未能阻止 response length 爆炸**。模型通过增加 turn 数绕过了 per-turn 限制——总 trajectory token 数从 4662 飙升到 7170。Train success 在 step 6 达峰 38.28% 后 step 7 崩塌至 15.625%，val_success 仅 9.375%（baseline 6.25%）。三个 intervention (A: len_penalty, B: high_kl, C: hard_cap) 全部 negative。

W&B: `https://wandb.ai/xiaoyucorynne-/cost-verify-agent-rl/runs/hszaa3vc`

Registry 已更新为 DONE / negative。

---

## Part B: C'（bjb1-17606）— 进行中

当前进度：**1/7 steps (14%)**，正在执行 step 2 训练。

### Step 0 (baseline eval)
- val_success: 9.375%
- val_resp_len: 1135.16
- val_pass@1: 9.375%

### Step 1 (train)
- train_success: 28.125%
- train_resp_len: 815.65
- train_pass@8: 62.5%
- kl_loss: 0.000319
- grad_norm: 2.10

C' 刚完成 step 1，训练节奏正常（~17 min/step on bjb1 2xGPU）。预计还需约 1.5-2 小时完成。

---
