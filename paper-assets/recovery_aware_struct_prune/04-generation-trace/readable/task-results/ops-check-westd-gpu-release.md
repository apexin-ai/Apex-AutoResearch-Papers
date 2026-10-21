# ops check westd gpu release

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_westd_gpu_release_20260517T174008_result.json`
- **Structured JSON:** [`c7957f7a94a4c4191d42.json`](../../sessions/c7/c7957f7a94a4c4191d42.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-11672 GPU 状态报告

| GPU | 状态 | 进程 |
|-----|------|------|
| cuda:0 | **空闲** (0MiB, 0%) | 无 |
| cuda:1 | **运行中** (34569MiB, 98%) | PID 14556: eval_math500 grpo_standard_20 (checkpoint-50) |
| cuda:2 | **空闲** (0MiB, 0%) | 无 |
| cuda:3 | **运行中** (31527MiB, 99%) | PID 31706: eval_math500 grpo_rasp_20_v9 |

## 已完成实验结果 (HumanEval pass@1)

| 实验 | pass@1 | 正确/总数 | 中位生成长度 |
|------|--------|-----------|-------------|
| **SFT standard_20** (2048 tokens) | **11.59%** | 19/164 | 2048 (截断) |
| **GRPO standard_20** (2048 tokens) | **10.37%** | 17/164 | 2048 (截断) |

两个实验 median response length 都是 2048，说明大量样本被截断。cuda:0 和 cuda:2 已释放，可用于新任务。

---
