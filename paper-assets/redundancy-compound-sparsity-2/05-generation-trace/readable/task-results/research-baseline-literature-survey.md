# research baseline literature survey

**redundancy compound sparsity 2** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_baseline-literature-survey_20260512T142807_result.json`
- **Structured JSON:** [`5d6e75be13f65e8dbdcb.json`](../../sessions/5d/5d6e75be13f65e8dbdcb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完成。文件写入 `artifacts/literature_map.yaml`，覆盖 14 个方法：

**核心 baseline（9 个指定方法）：**
- **H2O** (NeurIPS'23) — cumulative attention scoring, O(B)
- **StreamingLLM** (ICLR'24) — sink + window, O(1) 但不做 scoring
- **SnapKV** (NeurIPS'24) — prefill observation window, one-shot
- **R-KV** (NeurIPS'25) — pairwise redundancy scoring, O(B²)，**最直接对比**
- **SkipKV** (arXiv'25) — sentence-level 粗粒度压缩
- **FASA** (ICLR'26) — RoPE 频率域稀疏, O(B·F)
- **LazyEviction** (arXiv'25) — recurrence interval tracking, O(B)，**理念最近**
- **TOVA** (EMNLP'24) — min-attention eviction, O(B)
- **PyramidKV** / **PyramidInfer** — 层级化 budget 分配，正交可组合

**补充方法（5 个）：**
- **NACL** (ACL'24), **Ada-KV** (NeurIPS'25), **KeyDiff** (NeurIPS'25), **ExpectedAttention** (arXiv'25)

**kvpress v0.5.3 可直接跑的 baseline：** H2O, StreamingLLM, SnapKV, TOVA, KeyDiff, ExpectedAttention, ObservedAttention（共 7 个 + KNorm/Threshold/Compactor 等）

**我们方法的定位：** 唯一同时满足 O(1) per-token + redundancy-aware + 不需要 attention matrix 的方法。最直接对比是 R-KV（O(B²)）和 KeyDiff（O(B²)）。

---
