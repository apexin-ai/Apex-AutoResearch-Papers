# knowledge literature map update

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_knowledge_literature-map-update_20260514T190537_result.json`
- **Structured JSON:** [`be44e0d15e55406eab3f.json`](../../sessions/be/be44e0d15e55406eab3f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。添加了 6 篇缺失论文：

| 条目 | 论文 | Cluster | Role |
|------|------|---------|------|
| `li2025kvtuner` | KVTuner (ICML 2025) | Mixed-Precision R-D | direct-competitor |
| `chen2025pmkvq` | PM-KVQ (arXiv 2025) | Mixed-Precision R-D | method-component |
| `li2025kitty` | KITTY (arXiv 2025) | KV Cache Quantization | background |
| `fu2025headkv` | HeadKV (ICLR 2025) | KV Cache Eviction | background |
| `feng2025adakv` | AdaKV (NeurIPS 2025) | KV Cache Eviction | background |
| `chen2026muxq` | MUXQ (arXiv 2026) | Model Compression | background |

另外修正了 KVmix 的 venue（arXiv 2025 → AAAI 2026）和 role（method-component → direct-competitor）。RateQuant、KVmix、MixKVQ 已在 map 中，未重复添加。total_papers 更新为 41。

---
