# ops check topk3 result

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-topk3-result_20260515T083722_result.json`
- **Structured JSON:** [`1e08680f5a729fec429f.json`](../../sessions/1e/1e08680f5a729fec429f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**top_k=3 CED scoring 已完成**，进程已退出，GPU3 已释放。

| 指标 | top_k=3 | top_k=1 |
|------|---------|---------|
| 总 generations | 21,728 | 21,728 |
| **selected samples** | **8,037** | **2,718** |
| unique docs selected | 2,691 | — |
| selection rate | 37.0% | 12.5% |
| selected mean F1 | 0.576 | — |
| selected mean CED | 0.621 | — |
| selected mean combined | 0.679 | — |
| F1 dropped (gens) | 1,299 | — |
| F1 dropped (docs) | 25 | — |

top_k=3 选出 8,037 samples，约为 top_k=1 (2,718) 的 **2.96x**，覆盖 2,691/2,716 个 unique docs（几乎全覆盖）。selected 样本的 mean F1=0.576, mean CED=0.621，质量合理。

---
