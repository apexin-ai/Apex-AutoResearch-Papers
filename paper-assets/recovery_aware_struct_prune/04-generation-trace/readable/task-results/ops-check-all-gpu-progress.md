# ops check all gpu progress

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_all_gpu_progress_20260519T041508_result.json`
- **Structured JSON:** [`702049976e1b6228b47f.json`](../../sessions/70/702049976e1b6228b47f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 6-GPU 进度表

### westd-29022 (4× RTX PRO 6000)

| GPU | 实验 | 进度 | 状态 | 备注 |
|-----|------|------|------|------|
| cuda:0 | eval_math500_sft_standard_20_2048_v2 | **180/500** (36%) | 运行中 99% GPU | ~66s/it, ETA ~5.8h |
| cuda:1 | eval_humaneval_grpo_cka_only_20_2048 | **1/164** (1%) | 运行中 97% GPU | 刚启动 (12:13), ~104s/it |
| cuda:2 | eval_humaneval_sft_cka_only_20_2048 | **43/164** (26%) | 运行中 98% GPU | Pass@1=0.0000 (截至40题), ~60s/it |
| cuda:3 | eval_gsm8k_grpo_standard_20_extended_300 | **731/1319** (55%) | 运行中 99% GPU | acc=0.6000, ETA ~1.5h |

### westb-23072 (2× RTX PRO 6000)

| GPU | 实验 | 进度 | 状态 | 备注 |
|-----|------|------|------|------|
| cuda:0 | grpo_unstructured_20 | **68/100** (68%) | 运行中 95% GPU | ~28.5s/step, ETA ~15min |
| cuda:1 | grpo_cka_only_20_seed123 | **5/100** (5%) | 运行中 99% GPU | ~7min/step, ETA ~11h, W&B已连接 |

**注意**: cuda:2 的 HumanEval SFT 评测 Pass@1 在前 40 题都是 0.0000，可能有问题。

---
