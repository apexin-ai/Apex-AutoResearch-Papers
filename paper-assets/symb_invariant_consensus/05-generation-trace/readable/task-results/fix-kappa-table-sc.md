# fix kappa table sc

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_kappa-table-sc_20260522T220738_result.json`
- **Structured JSON:** [`162f7605ca7c69492e5a.json`](../../sessions/16/162f7605ca7c69492e5a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成。

**修改对比：**
- L718: `39.17` → `39.33`（kappa 分析表，within-model）
- L743: `39.17` → `39.33`（cross-model kappa 表）

**验证：** 其余 4 处 `39.17`（L875, L892, L948, L965, L1001）均为 DRC 表 / multi-NLI 表 / capability gap 标注，使用 seed42 traces，未被改动。

---
