# ssh d062 cf majority voting

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d062_cf_majority_voting_20260519T031718_result.json`
- **Structured JSON:** [`f4ce52cdcaf595a61cb6.json`](../../sessions/f4/f4ce52cdcaf595a61cb6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

d062 完成。**结论: negative。**

| | CF 变化 | DR 变化 |
|---|---|---|
| **ZS 条件** | 减少 18-96% | 增加 43-3300% |
| **FT 条件** | 减少 43-95% | 增加 145-3300% |

Majority voting 在所有 8 个条件上都降低了 CF，但同时大幅增加了 DR。原因：统一 entity type 时不考虑 domain/range 约束，"赢"的 type 在特定 relation 中违反了允许的 (head_type, tail_type) 组合。DocRED 尤为严重（Llama ZS 的 DR 从 2.55% 飙升到 16.65%）。FT 模型本身 CF 就很低（8-48），majority voting 意义不大。

产出已全部就绪：脚本、8 组修正后 JSONL、8 组 correction report、8 组 violation report、summary artifact，registry 已标记 DONE(negative)。

---
