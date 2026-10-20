# diagnosis 70b scierc failure

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_70b_scierc_failure_20260518T133349_result.json`
- **Structured JSON:** [`8ab91267f7c32fe20147.json`](../../sessions/8a/8ab91267f7c32fe20147.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：两个 70B SciERC 实验都没有失败，均已正常完成。**

| 实验 | 处理样本 | 成功 | 失败 | 输出行数 |
|---|---|---|---|---|
| 70b_scierc_constrained | 551/551 | 551 | 0 | 551 |
| 70b_scierc_unconstrained | 551/551 | 551 | 0 | 551 |

进程退出和 GPU 释放是因为任务跑完了，不是崩溃。心跳 miss 是因为进程已经正常结束。输出文件完整，可直接用于后续评估。

---
