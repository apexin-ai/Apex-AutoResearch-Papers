# fix seed comparison ign f1 compat

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_seed_comparison_ign_f1_compat_20260516T052418_result.json`
- **Structured JSON:** [`b3093a28f963159c8722.json`](../../sessions/b3/b3093a28f963159c8722.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

seed_comparison.py 已正确读取 CED s43/s45 的 ign_f1：

| Seed | CED Ign-F1 | fNLI Ign-F1 |
|------|-----------|------------|
| s43 | 0.4512 | — |
| s45 | 0.4416 | 0.4462 |

汇总统计也正常：CED ign_f1 = 0.4464 ± 0.0068 (n=2), fNLI = 0.4492 ± 0.0042 (n=2)。当前只有 s45 一个 matched seed，paired t-test 需等更多 seed 完成。

---
