# ssh d062 beam latency collect

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d062_beam_latency_collect_20260519T035059_result.json`
- **Structured JSON:** [`7007b50b4dd9c1af9bcb.json`](../../sessions/70/7007b50b4dd9c1af9bcb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**d062_beam_latency 实验结果汇总**：

| Condition | s/doc | vs Greedy Unc |
|-----------|-------|---------------|
| Greedy unconstrained | 2.612 | 1.00x |
| Greedy constrained | 2.873 | 1.10x |
| Beam-4 unconstrained | 3.446 | 1.32x |
| Beam-4 constrained | 4.013 | 1.54x |

- Beam search 增加 ~32-40% 延迟
- Constraint overhead 在 beam 下为 16.5%（greedy 下为 10.0%），因为 constraint checker 需在每步对所有 4 个 beam 独立检查
- Registry 已更新为 DONE/success，artifact 已注册

---
