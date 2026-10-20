# analysis humaneval overlap

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_humaneval_overlap_20260519T112242_result.json`
- **Structured JSON:** [`7f25776e56246e8ae82a.json`](../../sessions/7f/7f25776e56246e8ae82a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成，报告已保存并注册 (`art_20260519_26eadf`)。核心发现：

**Finding 1: GRPO Standard vs RASP 重合度极低**
- 仅 5/31 题重合 (Jaccard 16.1%)，各有 13 题独占
- 虽然总分相同 (18/164)，但解的是**几乎完全不同的题**

**Finding 2: CKA-only 不是 Standard/RASP 的超集**
- CKA union 49 题 vs Standard/RASP union 31 题
- 交集仅 18 题；CKA 独占 31 题，但丢了 13 题 Standard/RASP 能解的
- 三种 pruning 策略保留的代码能力有显著分化

**Finding 3: SFT CKA → GRPO CKA 是纯 redistribution**
- 总分不变 (33/164)，但 16 题丢失、16 题新增，仅 17 题稳定
- GRPO 没有扩展能力，只是重新分配了哪些题能解

---
