# research literature vota

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature-vota_20260514T215130_result.json`
- **Structured JSON:** [`fd7373b24bb500e857a2.json`](../../sessions/fd/fd7373b24bb500e857a2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入 `artifacts/literature_map.yaml`，12 篇论文覆盖 4 个方向。

关键发现：

- **最重要的负面结果**：Wang et al. (EMNLP 2025 Findings) 发现原始 execution trace 对 SFT 帮助有限——这恰好支持 VOTA 的核心动机：需要针对性的 trace 压缩/抽象，而非直接喂原始 trace
- **最接近的 competitor**：APPT (TSE 2024) 做 patch 正确性二分类达 79.7% accuracy，但用 BERT 而非 decoder LLM，且不用 trace 信息
- **文献空白**：没有工作将 compressed execution trace + SFT 用于 binary verdict 分类——这正是 VOTA 的差异化定位

---
