# analysis exp 017

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_017_20260523T040027_result.json`
- **Structured JSON:** [`e45812a5fb22d1073723.json`](../../sessions/e4/e45812a5fb22d1073723.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp_017 分析完成

**结论: SUCCESS** — seed43 高保真复现 Type II trajectory。

### 核心发现

| 指标 | Gen0 | Gen2 (dip) | Gen5 | Gen10 |
|------|------|-----------|------|-------|
| SLV | 2366.68 | **2358.84** (Δ=-7.84) | 2395.98 | 2455.78 |
| eff_rank | 417.55 | 480.44 | 492.09 | 505.98 |
| PPL | 9.55 | 10.74 | 11.83 | 13.40 |
| D-4 | 0.7415 | 0.4988 | 0.4435 | 0.2453 |

### Cross-seed 一致性 (seed42 vs seed43)

- **SLV Gen2 dip**: Δ = −8.11 ± 0.27，两个 seed 几乎完全一致
- **Gen0-5 谱指标**: SLV std < 1.6, eff_rank std < 0.7, PPL std < 0.02
- **Gen6-10 分化**: SLV 两者均持续上升，但 seed 间 std 增至 ~12；D-4 分化最大 — seed42 恢复到 0.52 而 seed43 持续下降到 0.25

### 延伸趋势 (Gen5→10)
SLV 持续单调上升，无二次坍缩。但 PPL (+40%) 和 D-4 (-67%) 的持续退化表明 20% real data 能稳定谱结构，但不足以阻止逐代质量下降。

报告已写入 `artifacts/exp_017/report/analysis.md`，registry 已更新 metrics/notes/conclusion/paths。

---
