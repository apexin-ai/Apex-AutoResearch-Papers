# ssh harvest standard 15 seed123 v3

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_harvest_standard_15_seed123_v3_20260521T005657_result.json`
- **Structured JSON:** [`02c02ec75999d4d38878.json`](../../sessions/02/02c02ec75999d4d38878.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE。

**Standard 15% seed123 结果**: accuracy = **65.13%** (859/1319)

**Standard 15% 全部三个 seed 汇总**:

| Seed | Accuracy |
|------|----------|
| seed42 | 待查 |
| seed123 | 65.13% |
| seed456 | 65.43% |

注意 seed42 的结果不在本次任务范围内，已有的两个 seed 均值为 **65.28%**。

**CKA-only 15% vs Standard 15% 对比**（已完成 seed）:
- CKA-only 15%: mean **72.76%** (73.09 / 73.09 / 72.10)
- Standard 15%: seed123=65.13%, seed456=65.43%

CKA-only 在 15% 剪枝率下领先 Standard 约 **7.5 个百分点**。

---
