# analysis exp 012

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_012_20260520T222011_result.json`
- **Structured JSON:** [`e66aa3e53c7533a2984e.json`](../../sessions/e6/e66aa3e53c7533a2984e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结论：

**Type III 复现确认。** seed43 与 seed42 的 SLV 轨迹高度一致（max divergence < 0.5%），均呈 ~6% 渐进上升。

**Table 3 可升级为 2-seed mean±std：**
- SLV: 2509.7 ± 2.0 (+6.0% ± 0.1%)
- eff_rank: 521.2 ± 0.0
- ppl: 13.34 ± 0.05

**注意 d4 divergence 较大**：seed43 在 gen10 降至 0.12（seed42 为 0.34），std=0.156。建议 Table 3 中 d4 列加脚注或报告单独 seed 值。

报告已注册：`art_20260520_ed2cc7`

---
