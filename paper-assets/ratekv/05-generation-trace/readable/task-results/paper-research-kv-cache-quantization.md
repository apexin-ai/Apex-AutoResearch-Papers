# paper research kv cache quantization

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_research_kv_cache_quantization_20260514T075325_result.json`
- **Structured JSON:** [`bff8a28678b7d8d092ef.json`](../../sessions/bf/bff8a28678b7d8d092ef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。literature_map.yaml 已添加 6 篇 KV Cache Quantization 论文，全部 verified=true：

| # | bibtex_key | 论文 | venue | role |
|---|---|---|---|---|
| 1 | liu2024kivi | **KIVI** — asymmetric per-channel key / per-token value 2-bit | ICML 2024 | direct-competitor |
| 2 | hooper2024kvquant | **KVQuant** — pre-RoPE + non-uniform + dense-and-sparse outlier | NeurIPS 2024 | direct-competitor |
| 3 | lin2024qserve | **QServe** — W4A8KV4 + SmoothAttention co-design | MLSys 2025 | foundation |
| 4 | he2024zipcache | **ZipCache** — channel-separable tokenwise + saliency-based mixed-precision | NeurIPS 2024 | direct-competitor |
| 5 | kang2024gear | **GEAR** — quantization + low-rank + sparse residual correction | arXiv 2024 | direct-competitor |
| 6 | duanmu2024skvq | **SKVQ** — channel rearrangement + sliding-window 2-bit/1.5-bit | arXiv 2024 | direct-competitor |

Must-cite KIVI 和 KVQuant 均已包含。

---
