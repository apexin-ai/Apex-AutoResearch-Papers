# code check paraphrase coverage

**afford invar** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_check-paraphrase-coverage_20260519T215930_result.json`
- **Structured JSON:** [`2b05d2958c46442fc65a.json`](../../sessions/2b/2b05d2958c46442fc65a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**判定：ACCEPTABLE — 无需补生成。**

paraphrases.json 覆盖情况：

| Suite | 任务数 | 有 paraphrase | 每任务 paraphrase 数 |
|-------|--------|---------------|---------------------|
| libero_10 | 10 | 10 | 5 |
| libero_90 | 90 | 90 | 5 |
| libero_goal | 10 | 10 | 5 |
| libero_object | 10 | 10 | 5 |
| libero_spatial | 10 | 10 | 5 |
| **合计** | **130** | **130** | **均为 5** |

全部 130 个任务都有 paraphrase，每个任务恰好 5 条。不存在缺失。之前"112/130 缺 18 个"的信息已过时，可能之后已补齐。

---
