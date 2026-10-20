# research literature and framing

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature_and_framing_20260512T124746_result.json`
- **Structured JSON:** [`ed198aa893ea13389e5b.json`](../../sessions/ed/ed198aa893ea13389e5b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三份文档已写入：

**产出 1: `docs/related_work_structure.md`** — 四线交汇结构：
- Thread 1 (Binary Detection → ordinal): DetectGPT, Min-K%++, DivEye, Binoculars
- Thread 2 (Model Collapse → micro forensics): Shumailov Nature'24, Alemohammad, Dohmatob ICLR'25, Schaeffer'25
- Thread 3 (Verification → graduated signal): Feng ICLR'25, Yi'25, Surplexity, Drayson EMNLP'25（最直接前驱）
- Thread 4 (Data Mixing → depth-aware): DoReMi, ConStat, DATAPROPHET

不确定的论文已标 [需验证]。

**产出 2: `docs/claim_routes.md`** — 双路线框架：
- **路线 A (K*≥3)**：depth estimation feasible → graduated filtering > binary，4 个 supporting claims + story arc + 3 个评审攻击面预演
- **路线 B (K*=2)**：K* 本身是 first-of-kind scientific quantity，framing 转换表（避免 hedging 措辞），saturation characterization 5 个卖点 + 3 个攻击面预演
- 底部附决策树

**产出 3: `docs/theory_framework.md`** — 信道级联 + DPI 理论框架：
- 递归生成 = iterated lossy channel Markov chain
- 3 个 proposition 骨架：(1) MI 单调衰减（DPI 直接推论），(2) 不动点收敛 → K* 有限性（contractive mapping），(3) 衰减速率与 decoding strategy 的非单调关系（conjecture）
- JSD 作为 tractable MI proxy 的定位和局限
- 理论预测 ↔ 实验验证对照表

---
