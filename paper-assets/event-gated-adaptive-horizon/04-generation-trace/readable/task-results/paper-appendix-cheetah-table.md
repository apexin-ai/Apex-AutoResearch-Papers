# paper appendix cheetah table

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_appendix_cheetah_table_20260525T155300_result.json`
- **Structured JSON:** [`494546b9848b0cf820c0.json`](../../sessions/49/494546b9848b0cf820c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成。

**修改文件**: `docs/paper/sections/appendix.tex`

**插入内容**（第 72-74 行，在 008a\_ch s1 之后、019b 之前）:

| Exp | Config | dt\_emb | Sub | H | Eval@final | NVE | Outcome |
|-----|--------|---------|-----|---|------------|-----|---------|
| 077 | Cheetah baseline (s0) | --- | --- | 15 | 448.1 @105K | 1.00× | Healthy |
| 078 | Cheetah trigger (s0) | trn | ON | 8 | 119.5 @105K | 4.10× | Onset (self-corr.) |

- exp\_078 行带 `\rowcolor{gray!15}` 标记为 CIVO-positive，与现有格式一致
- 表头说明中实验总数从 43 更新为 45

---
