# research missing references

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_missing_references_20260515T081615_result.json`
- **Structured JSON:** [`ef7d068bc92d3decef85.json`](../../sessions/ef/ef7d068bc92d3decef85.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成，文件写入 `artifacts/n500_analysis/missing_references.md`。

三篇论文全部找到：

| 论文 | 实际标题 | Venue | 与本文相关性 |
|------|---------|-------|------------|
| **RLKV** | "Which Heads Matter for Reasoning? RL-Guided KV Cache Compression" (Du et al., arXiv:2510.08525) | ICLR 2026 提交 | 中等——learned importance-based head eviction，但无 compound/phase 分析 |
| **LongFlow** | "LongFlow: Efficient KV Cache Compression for Reasoning Models" (Su et al., arXiv:2603.11504) | ICLR 2026 **已撤稿** | 一般——reasoning-specific importance eviction，纯系统优化 |
| **PM-KVQ** | "PM-KVQ: Progressive Mixed-precision KV Cache Quantization for Long-CoT LLMs" (Liu et al., arXiv:2505.18610) | **ICLR 2026 Poster (Accepted)** | **最高**——progressive quantization 本质上是 temporally-varying multi-axis compression，cumulative error 发现与我们的 compound severity 互补 |

PM-KVQ 必须引用（ICLR 2026 accepted + 与本文核心主题交叉最大）。RLKV 建议引用。LongFlow 可引可不引（已撤稿）。每篇的具体引用位置和建议措辞已写入文件。

---
