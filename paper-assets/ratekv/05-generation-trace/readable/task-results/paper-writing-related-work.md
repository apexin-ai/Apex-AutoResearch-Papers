# paper writing related work

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_related_work_20260514T102130_result.json`
- **Structured JSON:** [`d3cd7e52b344507a7be7.json`](../../sessions/d3/d3cd7e52b344507a7be7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Related Work 已写入 `docs/paper/related_work.tex`，约 580 words，4 个子主题：

1. **KV Cache Quantization** — 6 篇 uniform 方法，定位我们为 per-head non-uniform + hardware-aligned
2. **KV Cache Eviction** — 6 篇 token eviction 方法，明确正交互补关系
3. **Mixed-Precision Rate-Distortion Allocation** — RateQuant 为核心对比（polymatroid 在 {2,4,8,16} 上失效 + compounding failure），加 SqueezeLLM/ARKV/KVmix/MixKVQ 各自差异化
4. **Attention Head Analysis** — Voita 和 Michel 用 `[UNVERIFIED: ...]` 占位，区分 head pruning vs quantization sensitivity

所有 17 个已验证 `\cite{}` 均使用，无新增定量 claim。

---
