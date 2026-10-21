# diagnose v2 rasp humaneval harvest

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_v2_rasp_humaneval_harvest_20260519T143546_result.json`
- **Structured JSON:** [`e7f777bc2d751ce89441.json`](../../sessions/e7/e7f777bc2d751ce89441.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE (negative)。

**结果汇总：**

| 模型 | HumanEval pass@1 |
|------|------------------|
| SFT Standard | 13.41% |
| SFT CKA-only | 20.12% |
| **SFT RASP 20%** | **10.37% (17/164)** |
| GRPO RASP | 10.98% |

SFT RASP 20% v2 重跑结果与 v1 一致（10.37%），确认非 truncation 问题。RASP 在 HumanEval 上表现最差，低于 Standard 和 CKA-only，与 GRPO RASP 接近。median_response_length=2048 说明大量生成被截断，模型在代码生成上存在冗长输出问题。

**westd-29022 GPU 状态：** cuda:1 已空闲（0MiB, 0%），可用于下一个任务。cuda:0/2/3 均有进程占用。

---
