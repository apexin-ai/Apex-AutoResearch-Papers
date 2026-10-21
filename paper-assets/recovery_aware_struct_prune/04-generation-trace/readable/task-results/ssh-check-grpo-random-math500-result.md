# ssh check grpo random math500 result

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_grpo_random_math500_result_20260523T110059_result.json`
- **Structured JSON:** [`7fcf02069712bd44c601.json`](../../sessions/7f/7fcf02069712bd44c601.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE。Cron ID 不存在（可能已被删除或名称不同）。

**结果汇报**：

| 指标 | 值 |
|------|-----|
| **Accuracy** | **13.4%** |
| **Correct/Total** | 67 / 500 |
| SE | ±0.0152 |
| Natural EOS | 167 (33.4%) |
| Truncated | 333 (66.6%) |
| Avg response length | 1479.2 tokens |

**GPU 状态**（westd-32935）：

| GPU | Utilization | Memory |
|-----|------------|--------|
| 0 | 99% | 29593 MiB |
| 1 | 91% | 19251 MiB |
| **2** | **0%** | **0 MiB** ← 已释放 |
| 3 | 99% | 29173 MiB |

GPU 2 已完全释放，eval 进程已退出。66.6% 的样本被截断（达到 2048 max tokens），truncation 严重影响了准确率。

---
