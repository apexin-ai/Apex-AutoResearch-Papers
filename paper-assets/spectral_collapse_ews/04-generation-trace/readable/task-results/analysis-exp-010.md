# analysis exp 010

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_010_20260520T074817_result.json`
- **Structured JSON:** [`94dd77a4fb848586c69a.json`](../../sessions/94/94dd77a4fb848586c69a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。exp_010 → DONE (success)。

**结论：三阶段 pattern 跨 seed 完全复现。**

关键数字：
- Phase boundaries 完全一致：peak Gen 2, onset Gen 3, sustained collapse Gen 2→10
- Gen 10 SLV: **2194.86 ± 22.50**（decline from peak: -11.07% ± 1.00%）
- Gen 10 PPL: **73.64 ± 4.44**（+670.7% from Gen 0）
- Gen 10 eff_rank: **440.62 ± 2.60**
- 跨 seed SLV 差异全程 <1.5%，eff_rank <1%

报告已写入 `artifacts/exp_010/report/exp_010_analysis.md`，`seed_comparison.json` 已更新为完整 11 代数据，registry 已更新。

---
