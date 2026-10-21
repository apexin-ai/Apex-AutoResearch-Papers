# analysis qwen14b kappa from exp001

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen14b-kappa-from-exp001_20260520T031016_result.json`
- **Structured JSON:** [`ae2e98988212b801a6c7.json`](../../sessions/ae/ae2e98988212b801a6c7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Artifact 已写入。结果汇总：

### Qwen2.5-14B-Instruct Fleiss' κ（K=12 SC traces）

| 子集 | N | K (mean) | κ | Eff-K | 类别分布 |
|------|---|----------|------|-------|---------|
| **FOLIO-204** | 204 | 12.0 | **0.738** | 1.32 | True 42.4%, False 37.4%, Unknown 20.2% |
| **PW-600** | 600 | 11.97 | **0.617** | 1.54 | True 32.9%, False 28.8%, Unknown 38.4% |
| **Combined** | 804 | 11.98 | **0.656** | 1.46 | — |

关键发现：Qwen2.5-14B 的 κ（0.62–0.74）**显著高于** Mistral-7B（~0.40–0.50），对应的 Eff-K 更低（1.3–1.5 vs Mistral 的 ~1.8）。更大的模型 same-model 一致性更高，SC traces 的有效多样性更低——强化了 "same-model ceiling" 跨模型成立的结论。

---
