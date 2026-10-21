# ssh check math500 progress all

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_math500_progress_all_20260521T153317_result.json`
- **Structured JSON:** [`35cf3a1fffbd845b3c9c.json`](../../sessions/35/35cf3a1fffbd845b3c9c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集完毕。

## MATH-500 Eval 进度汇总

| exp_id | Server:GPU | PID | 状态 | 进度 | 当前 Acc | 平均速度 | 预估完成时间 |
|--------|-----------|-----|------|------|----------|---------|-------------|
| eval_math500_grpo_cka_only_25_v2 | westd:0 | 379999 | **运行中** | **246/500** (49%) | 20.5%@200 | ~29s/题 | ~01:35 (≈2h) |
| eval_math500_grpo_random_20_v2 | westd:1 | 382472* | **运行中** | **74/500** (15%) | 8.0%@50 | ~75s/题 | ~08:30 (≈9h) |
| eval_math500_sft_cka_only_25_v2 | westd:2 | 380074 | **运行中** | **278/500** (56%) | 20.8%@250 | ~26s/题 | ~01:10 (≈1.5h) |
| eval_math500_sft_random_20 | westd:3 | 385685 | **运行中** | **41/500** (8%) | — | ~69s/题 | ~08:20 (≈9h) |
| eval_math500_grpo_standard_25_v2 | westb:0 | 99426 | **运行中** | **105/500** (21%) | — | ~57s/题 | ~06:00 (≈6.5h) |
| eval_math500_sft_standard_25_v2 | westb:1 | 104592 | **运行中** | **11/500** (2%) | — | ~65s/题 | ~08:30 (≈9h) |

**\*PID 382470 是 wrapper，实际子进程 382472。**

### 补充说明

- **eval_math500_sft_standard_25 v1 已完成**：westb 上 `results/eval_math500_sft_standard_25.json` 已有完整结果（n_total=500, accuracy=**13.0%**），Director 已采用。当前 westb:1 上 PID 104592 是 v2 重跑（刚启动约16分钟）。
- **速度差异**：random 剪枝模型（grpo_random_20、sft_random_20）每题 65-75s，比 CKA/standard 剪枝（25-30s/题）慢 2-3x，推测是剪枝后模型生成更长的无效 token。
- **GPU 利用率**：westd 4卡 95-97%，westb 2卡 99%，均满载运行。
- **最早完成**：sft_cka_only_25_v2（~01:10）和 grpo_cka_only_25_v2（~01:35）。**最晚完成**：4个 random/standard 模型约 06:00-08:30。

---
