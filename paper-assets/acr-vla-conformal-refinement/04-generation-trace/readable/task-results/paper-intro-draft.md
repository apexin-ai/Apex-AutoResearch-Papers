# paper intro draft

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_intro-draft_20260515T192303_result.json`
- **Structured JSON:** [`32c534ea98d1c91ff200.json`](../../sessions/32/32c534ea98d1c91ff200.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Introduction 初稿已写到 `artifacts/_project/paper/sections/introduction.tex`。

结构：5 段落 + 贡献列表。
- Para 1: VLA 成就 + 分布偏移脆弱性
- Para 2: 现有方法（training-time vs inference-time）+ gap
- Para 3: ACR-VLA sample-then-correct pipeline 概述
- Para 4: 三个核心发现，每个附 exp_id 注释和具体数字
- Para 5: 三条贡献

关键处理：
- Spatial null result 诚实 framed（"targeted improvements on object-centric manipulation rather than universal gains"）
- 所有定量 claim 用 seed=42 confirmed 数据，标注 `% TODO: update with pooled seed results`
- 每个数字附 `% exp_id:` 注释可追溯
- 引用全部使用 references.bib 中已有的 key，无虚构引用
- 强度词匹配 evidence（只在 object benchmark 上说 "outperforms"，不用 "consistently"）

---
