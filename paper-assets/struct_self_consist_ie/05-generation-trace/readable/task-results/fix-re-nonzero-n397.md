# fix re nonzero n397

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_re_nonzero_n397_20260515T073520_result.json`
- **Structured JSON:** [`805ce51199344a06971d.json`](../../sessions/80/805ce51199344a06971d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。核心结果：

**n=397 确认**，其中 238 个 greedy 非零，159 个 greedy 为零。

**非零子集 (n=238)：所有 5 个信号都劣于 greedy**，损失 7-10 个 F1 点（p=1.0）。信号无法在 greedy 已有效的 instance 上做出更好的选择。

**全集 n=397：同样全部为负增益**。零子集的正增益（trivially greedy=0）不足以抵消非零子集的损失。

**Oracle gap 很大**（0.4042 → 0.5850），说明 N=8 pool 中确实存在更好的 sample，但当前 5 个一致性信号无法为 RE 选出它们。LP 是损失最小的信号。

产出已注册：`art_20260515_14dd31`

---
