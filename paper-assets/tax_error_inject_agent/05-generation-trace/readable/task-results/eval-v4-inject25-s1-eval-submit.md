# eval v4 inject25 s1 eval submit

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_v4-inject25-s1-eval-submit_20260515T223630_result.json`
- **Structured JSON:** [`9975b2b81f6856aa1d38.json`](../../sessions/99/9975b2b81f6856aa1d38.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

## 1. Checkpoint 路径

| 实验 | Checkpoint |
|------|-----------|
| v4-taxei-fixed-inject25-s1 | `checkpoints/v4_taxei_fixed_inject25_s1/v0-20260516-052917/checkpoint-1635` |
| v4-random-fixed-inject25-s1 | `checkpoints/v4_random_fixed_inject25_s1/v0-20260516-053219/checkpoint-1635` |

## 2. 恢复的 TaxEI 25% eval 结果

| 实验 | Success Rate | Successes/Total |
|------|-------------|----------------|
| v4-taxei-fixed-inject25-s0-eval | **46.8%** | 22/47 |
| v4-taxei-fixed-inject25-s123-eval | **46.8%** | 22/47 |

两个实验的 by_task_type 详细数据已从服务器 JSON 文件恢复写入 registry。

## 3. 已提交的 eval 实验

| Exp ID | GPU | Status |
|--------|-----|--------|
| `v4-taxei-fixed-inject25-s1-eval` | cuda:0 | RUNNING (14.9 GB loaded) |
| `v4-random-fixed-inject25-s1-eval` | cuda:1 | RUNNING (14.9 GB loaded) |

预计每个 eval 约 15-25 分钟完成。cuda:2 空闲，cuda:3 被其他任务占用。

---
