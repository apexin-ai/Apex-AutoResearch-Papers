# analysis fk excess agreement

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_fk_excess_agreement_20260515T121311_result.json`
- **Structured JSON:** [`5a6c6070cc9d59858ea1.json`](../../sessions/5a/5a6c6070cc9d59858ea1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/fk_excess_agreement_all_configs.md` 并注册。

核心结论：
- **P_e 由数据集决定**：SciERC P_e 高（0.45–0.51），CoNLL P_e 低（0.07–0.31）
- **LLaMA CoNLL excess 最高**（~0.90），SciERC excess 最低（0.24–0.31）——SciERC 的大量观察一致性来自 chance
- RE 的 FK 系统性低于同数据集的 NER
- N=8→16 对 FK 几乎无影响，但 P_e 随 N 增大而上升

---
