# research panel analysis feasibility

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_panel_analysis_feasibility_20260515T085153_result.json`
- **Structured JSON:** [`fca9b290f4e67e13d1e2.json`](../../sessions/fc/fca9b290f4e67e13d1e2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出已写入 `artifacts/panel_analysis_feasibility.md`。

**核心结论：现在做 panel Granger 分析统计上不成立，不能作为发表级结论。**

三个致命问题：
1. **N=4–5, T=11 处于 DH 检验的 power floor 之下**——即使假设全部满足，检出中等效应的 power 仅 15–25%
2. **单 seed/α 无法分离 regime effect 与 seed noise**——这是实验设计缺陷，不是样本量问题
3. **不同 α 不是 exchangeable units**——违反 panel 模型的基本假设

**现在可以做的**：descriptive cross-α comparison + Fisher's method pool per-α p-values，定位为 preliminary/suggestive evidence。

**正式 panel 分析最低要求**：3 seeds × 5 α = N=15, T=11。推荐 4 seeds × 5 α = N=20。优先补跑 α=0.00 和 α=0.50 的额外 seeds。

---
