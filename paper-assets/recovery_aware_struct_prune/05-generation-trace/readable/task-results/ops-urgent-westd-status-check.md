# ops urgent westd status check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent_westd_status_check_20260517T171129_result.json`
- **Structured JSON:** [`99b13ec2d8e92be1657d.json`](../../sessions/99/99b13ec2d8e92be1657d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-11672 状态报告

| GPU | 实验 | PID | 显存 | GPU Util | 进度 | 当前指标 |
|-----|------|-----|------|----------|------|----------|
| cuda:0 | eval_humaneval_sft_standard_20_2048_v2 | 36729 | 12,780 MiB | 88% | **115/164** (70%) | Pass@1: 0.0900 (at 100) |
| cuda:1 | eval_math500_grpo_standard_20 | 14556 | 34,560 MiB | 98% | **169/500** (34%) | Acc: 0.3267 (at 150) |
| cuda:2 | eval_humaneval_grpo_standard_20_2048 | 27199 | 17,802 MiB | 96% | **140/164** (85%) | Pass@1: 0.1000 (at 140) |
| cuda:3 | eval_math500_grpo_rasp_20_v3 | 31706 | 30,078 MiB | 99% | **84/500** (17%) | Acc: 0.3400 (at 50) |

**结果文件**：4 个 json 均未生成，全部仍在运行中。

**预估完成时间**：
- cuda:0 (HumanEval SFT): 剩 49 题，~20s/题 → **~16 min**
- cuda:1 (MATH500 GRPO standard): 剩 331 题，~3-4 min/题 → **~15-20 h**
- cuda:2 (HumanEval GRPO): 剩 24 题，~100s/题 → **~40 min**
- cuda:3 (MATH500 GRPO RASP): 剩 416 题，~3-4 min/题 → **~20+ h**

**空闲 GPU**：无。四卡全满载。cuda:0 和 cuda:2 将在 1 小时内先后完成，届时可复用。

---
