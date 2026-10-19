# write introduction draft

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_write_introduction-draft_20260514T224556_result.json`
- **Structured JSON:** [`85fb0567efbfcc8be550.json`](../../sessions/85/85fb0567efbfcc8be550.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Introduction v1 已写入并注册。结构概要：

- **P1** — Code retrieval 重要性 + lexical ≠ structural relevance 问题（引用 SWE-bench, SweRank, SWE-Fixer, SWE-agent, Agentless）
- **P2** — 两个 gap：(a) graph-guided 方法仅 inference-time 用结构信号，encoder 训练无结构；(b) code domain 缺乏 negative mining 系统研究，CoCoHaNeRe 主张 gradient-based 优于 non-differentiable embedding negatives 但未测试 static embedding-distance mining
- **P3** — 我们的 systematic study：static embedding mining +1.6–2.0pp R@1（标注 pilot evidence），counter CoCoHaNeRe 前提但限定在 structural code retrieval 场景；dataflow negatives 与 encoder geometry 交互的 mechanistic 分析
- **P4** — 3 contributions：Claim 1（embedding mining suffices），Claim 2（exploratory observation，dataflow × geometry 交互），Claim 3（CodeQL pipeline scalability）

全文 ~730 words，所有引用均来自 literature_map.yaml，强度词已加 "(pilot evidence; pending M2 full confirmation)" 标注。

---
