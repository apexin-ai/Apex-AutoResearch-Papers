# check westb eval status

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_westb_eval_status_20260521T195210_result.json`
- **Structured JSON:** [`d2cec2d5aa9846939e4a.json`](../../sessions/d2/d2cec2d5aa9846939e4a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### westb-23072

| PID | 任务 | GPU | 状态 | 运行时间 | 显存 |
|-----|------|-----|------|---------|------|
| 99426 | eval_math500_grpo_standard_25_v2 | cuda:0 | **RUNNING** | 6h02m | 19186MiB |
| 104592 | eval_math500_sft_standard_25_2048 | cuda:1 | **RUNNING** | 4h32m | 18568MiB |
| 118095 | eval_math500_sft_cka_only_20_v6 | cuda:1 | **RUNNING** | 19m | 16546MiB |
| 62714 | eval_math500_sft_standard_25_v2 | cuda:0 | **COMPLETED** | — | — |
| 59663 | eval_humaneval_sft_standard_25 | cuda:1 | **COMPLETED** | — | — |

GPU 利用率：cuda:0 100%, cuda:1 100%

**已完成结果：**
- **eval_humaneval_sft_standard_25** → pass@1 = **1.83%** (3/164)，max_new_tokens=512
- **eval_math500_sft_standard_25** (v2) → accuracy = **13.0%** (65/500)，truncated=318/500，avg_len=1376

注意：PID 62714 的结果文件在 `/root/autodl-tmp/.../results/eval_math500_sft_standard_25.json`（无 `_v2` 后缀），未找到 `_v2.json` 文件。

---

### westd-29022

| PID | 任务 | GPU | 状态 | 运行时间 | 显存 |
|-----|------|-----|------|---------|------|
| 382470 | eval_math500_grpo_random_20_v2 | cuda:1 | **RUNNING** | 5h55m | 17642MiB |
| 385685 | eval_math500_sft_random_20 | cuda:3 | **RUNNING** | 5h07m | 17642MiB |
| 412988 | eval_gsm8k_grpo_alpha4_20 | cuda:0 | **RUNNING** | 24m | 29134MiB |
| 412817 | eval_math500_grpo_alpha4_20 | cuda:2 | **RUNNING** | 24m | 17518MiB |
| 310542 | grpo_cka_only_25 (训练) | cuda:2 | **COMPLETED** | — | — |

GPU 利用率：4 卡全部 96-99%

**已完成结果：**
- **grpo_cka_only_25** — GRPO 训练已完成，模型保存至 `/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_25`，wandb run: `grpo_sft_cka_only_25` (mirgxi5b)

---
