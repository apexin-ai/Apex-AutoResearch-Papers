# analysis scierc mv sign flip

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_scierc-mv-sign-flip_20260522T182049_result.json`
- **Structured JSON:** [`406cee0f4d6c4cef588b.json`](../../sessions/40/406cee0f4d6c4cef588b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。核心结论：

**不存在真正的符号翻转。** 注册表中 s123=+0.34pp 来自混用了两次独立的 pipeline 运行（N8 re-run vs MF4v2）。统一的 MF4v2 recompute（3 个 seed 用同一 pipeline、同一数据源）显示 **MV delta 全为负**：

| Seed | MV Δ (pp) |
|------|-----------|
| 42 | −1.25 |
| 123 | −0.11 |
| 456 | −0.86 |
| **Mean±σ** | **−0.74 ± 0.46** |

论文可直接写 "MV consistently hurts on SciERC"，无需对符号不稳定性做 hedge。

报告已注册为 `art_20260522_c57a9e`。

---
