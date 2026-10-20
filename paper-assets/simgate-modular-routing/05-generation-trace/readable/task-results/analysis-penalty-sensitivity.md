# analysis penalty sensitivity

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_penalty-sensitivity_20260514T125431_result.json`
- **Structured JSON:** [`f72b4145b48feb867311.json`](../../sessions/f7/f72b4145b48feb867311.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

C1 Penalty Sensitivity Analysis 完成。

## 核心结果

**死亡分类（245 episodes）**：
- only internal dies: 70, only deterministic dies: 5, both die: 35, neither: 135
- δ = (70 - 5) / 245 = **0.2653**

**分解公式**：`Δ_full(P) = δ·P + Δ_nd`，其中 Δ_nd = **3.07**

**Overall Sensitivity Table**：

| P | Δ_full(P) | DAF(P) |
|---|-----------|--------|
| 10 | 5.72 | 46.4% |
| 25 | 9.70 | 68.4% |
| 50 | 16.33 | **81.2%** |
| 100 | 29.60 | 89.6% |
| 200 | 56.13 | 94.5% |

**与 reviewer 预期对比**：reviewer 预期 P=10→50.4%、P=25→70.7%、P=50→82.6%，实际略低（因 Δ_nd=3.07 > reviewer 假设的 2.84），趋势完全一致。

**关键反驳点**：`find-non-living-thing`（40 episodes）δ=0（零死亡），纯靠 non-death 优势 Δ_nd=9.58，DAF=0%——证明 deterministic 优势不依赖 death penalty。另有 5 个 task 在 P=50 时 DAF>94%。

**产出文件**：
- `artifacts/penalty_sensitivity.json` — 完整数据
- `artifacts/penalty_sensitivity_table.tex` — LaTeX 表格
- Registry: `plan-012-penalty-sensitivity` (DONE/success)

---
