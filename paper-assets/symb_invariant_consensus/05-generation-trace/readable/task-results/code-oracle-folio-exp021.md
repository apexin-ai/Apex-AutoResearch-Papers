# code oracle folio exp021

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_oracle-folio-exp021_20260517T163632_result.json`
- **Structured JSON:** [`30c97b923d9b5dd6fe49.json`](../../sessions/30/30c97b923d9b5dd6fe49.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。核心结果：

| Method | Accuracy | 
|--------|----------|
| **Oracle-SICA** (gold FOL + Z3) | **88.24%** (180/204) |
| SC (majority vote) | 79.41% (162/204) |
| SICA (self-extracted) | 79.41% (162/204) |

关键发现：
- **+8.82pp** 增益（Oracle-SICA vs SC/SICA），McNemar p = 6.15e-05
- Z3 solver 与 gold answer 一致率 **94.6%**（193/204）
- FOL parser 全部 204 题 parse 成功，0 错误
- SICA (self-extracted) 在 FOLIO 上与 SC 完全相同（79.41%），说明 LLM 自提取的约束在形式逻辑任务上无有效信号
- 5 题验证阶段 5/5 正确

结论：**约束质量是 SICA 在 formal logic 任务上获得增益的瓶颈**。给定完美 FOL 约束，consistency-weighted voting 能带来显著提升。

---
