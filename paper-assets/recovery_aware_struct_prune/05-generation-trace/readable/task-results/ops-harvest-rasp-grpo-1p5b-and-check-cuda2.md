# ops harvest rasp grpo 1p5b and check cuda2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_harvest_rasp_grpo_1p5b_and_check_cuda2_20260518T230020_result.json`
- **Structured JSON:** [`6f38868642b3cada8c94.json`](../../sessions/6f/6f38868642b3cada8c94.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总结果：

### Part 1: westb — RASP GRPO 1.5B GSM8K

| 指标 | 值 |
|------|------|
| **Accuracy** | **26.16%** (345/1319) |
| Stderr | ±1.21% |
| EOS rate | 93.78% |
| Avg response length | 392.7 tokens |
| Model | grpo_rasp_20_1p5b/checkpoint-100 |

Registry 已更新为 DONE/success。

**下一个 eval 已启动：** `eval_gsm8k_sft_standard_20_1p5b` on westb cuda:1 (PID 842784)。

### Part 2: westd cuda:2 — SFT Standard 重训

- PID 34346 正在跑 `sft_recovery.py --model_path pruned_standard_20 --output_dir sft_standard_20 --gpu 2`
- 进度：**1249/1870 steps (66.8%)**
- 速度：~1.10 it/s
- Loss：~0.80，mean_token_accuracy：~0.79
- **预计剩余：~9-10 分钟完成**

### 1.5B GSM8K 对比表（截至目前）

| Method | Post-SFT | Post-GRPO | GRPO Δ |
|--------|----------|-----------|--------|
| Standard 20% | (eval 进行中) | 22.29% | — |
| RASP 20% | — | **26.16%** | — |
| CKA-only 20% | — | — | — |

RASP GRPO 1.5B 26.16% 显著优于 Standard GRPO 1.5B 22.29% (+3.87pp)。

---
