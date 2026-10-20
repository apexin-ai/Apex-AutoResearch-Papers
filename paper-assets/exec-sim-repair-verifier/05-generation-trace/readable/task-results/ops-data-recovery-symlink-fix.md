# ops data recovery symlink fix

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_data-recovery-symlink-fix_20260519T135535_result.json`
- **Structured JSON:** [`167483ae626fc3bf290d.json`](../../sessions/16/167483ae626fc3bf290d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过：

| 文件 | 行数 | md5 |
|------|------|-----|
| train 源 → 目标 | 70748 → 70748 | `e25e2c88f86bdd9dabdb5d77394f5e0c` 一致 |
| val 源 → 目标 | 9335 → 9335 | `bab83e17cbed30b2e5eef13f16d1be36` 一致 |

数据文件已正确覆盖到 `data/swebench_full/`，训练脚本现在会读到正确数据。

---
