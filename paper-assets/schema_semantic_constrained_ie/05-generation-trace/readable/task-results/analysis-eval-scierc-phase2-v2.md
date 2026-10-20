# analysis eval scierc phase2 v2

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_scierc_phase2_v2_20260514T014906_result.json`
- **Structured JSON:** [`0c93df9d10b3fa4a33db.json`](../../sessions/0c/0c93df9d10b3fa4a33db.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇总结果：

## SciERC Phase 2 实验结果汇总

| Mode | Samples | R-F1 | E-F1 | DR% | RV% | ET% | DR delta |
|------|---------|------|------|-----|-----|-----|----------|
| unconstrained | 551 | 0.0823 | 0.3101 | 15.37% | 1.39% | 0.4% | baseline |
| grammar_only | 551 | 0.0823 | 0.3098 | 14.84% | 0% | 0% | -0.53pp |
| semantic_only | 551 | 0.0815 | 0.3101 | 11.65% | 1.51% | 0.4% | **-3.72pp** |
| full_s1 | 551 | 0.0836 | 0.3098 | 0.93% | 0% | 0% | **-14.44pp** |
| full_s2 | 415/551 | — | — | — | — | — | 未完成 |

### 关键发现

**full_s1（Grammar + Semantic 双层约束）** 是论文核心结果：
- DR violation 从 15.37% 降至 **0.93%**（降幅 14.44pp，消除 94%）
- ET=0%, RV=0%（完全消除）
- R-F1 **微升** 0.0013（0.0823→0.0836），E-F1 基本持平（-0.0003）
- F1 无损甚至略升 + violations 近乎清零 → 完美 trade-off

**semantic_only** 仅靠语义约束：
- DR 只降到 11.65%（-3.72pp），远不如双层
- RV=1.51%、ET=0.4% 未消除（因为没有 grammar 层）
- R-F1 略降 0.0008

**Per-relation DR（full_s1）**：Used-for/Hyponym-of/Part-of/Conjunction = 0%，Evaluate-for 5.76% 和 Compare 2.82% 残留最多，Feature-of 1.21%。

**full_s2** 仅完成 415/551，跳过评估。

---
