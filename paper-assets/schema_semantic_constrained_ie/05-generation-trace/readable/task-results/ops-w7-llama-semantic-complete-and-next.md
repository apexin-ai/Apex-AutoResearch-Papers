# ops w7 llama semantic complete and next

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_w7_llama_semantic_complete_and_next_20260516T083046_result.json`
- **Structured JSON:** [`17eef4d0fc5a77c787fe.json`](../../sessions/17/17eef4d0fc5a77c787fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。Registry 已更新为 DONE/success。

## 结果汇总

**w7_llama_scierc_ft_semantic_only** — 551/551 samples, 0 parse failures

| Metric | Unconstrained | Grammar-only | **Semantic-only** | Full S1 |
|--------|:---:|:---:|:---:|:---:|
| ET% | 0% | 0% | **0%** | 0% |
| RV% | 0% | 0% | **0%** | 0% |
| DR% | 1.11% | 1.11% | **0.65%** | 0.09% |
| CF | 0 | 0 | **2** | - |
| E_F1 | - | 67.76% | **67.76%** | - |
| R_F1 | 45.45% | 45.45% | **45.47%** | - |

**结论**: Semantic-only 约束将 DR 从 1.11% 降至 0.65%（-42%），R_F1 完全持平。说明 semantic 层在 FT Llama 上独立贡献约束效果，但单独不够——需要与 grammar 联合 (full_s1=0.09%) 才能接近消除 DR。Grammar 层对 DR 无直接作用（1.11%→1.11%），它主要保证 ET/RV=0。

---
