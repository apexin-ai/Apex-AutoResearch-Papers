# paper full draft audit

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_full-draft-audit_20260514T144747_result.json`
- **Structured JSON:** [`bdf8b75e87d7528a78d5.json`](../../sessions/bd/bdf8b75e87d7528a78d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计报告已写入并注册。核心结论：

**数字审计：100% 通过** — artifacts/ 目录中所有数字（Table 1、DAF、r/p、tie rate、router accuracy、labeling quality、MATH pilot）均与 registry 一致。trained-router 正确使用 -10.70（非 -12.84），tie rate 正确为 97.4%（非 98.2%）。

**关键问题（P0）**：
1. **两个目录严重分叉** — `docs/paper/` 有大量内容不在 `artifacts/` 中（更完整的 abstract、Rule-Based Baseline 子节、experiments 中 labeling quality 段、更详细的 router 分析）。两者用了不同 CI level（95% vs 90%）。需要合并后废弃 docs/。
2. **discussion.tex 有 2 个 TODO 注释**（pilot-50→math-200-fixed 替换、ALFWorld 结果），math-200-fixed 在 56/200 处崩溃，暂无法替换。

**P1 问题**：
3. plan-013 labeling quality 在 Limitations 里而非 Conclusion（用户意图是"入 conclusion"）
4. MATH pilot 72% 受 sandbox bug 影响（clean accuracy ~89%）

---
