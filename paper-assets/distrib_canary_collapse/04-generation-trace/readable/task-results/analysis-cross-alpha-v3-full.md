# analysis cross alpha v3 full

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cross_alpha_v3_full_20260515T054603_result.json`
- **Structured JSON:** [`645beaa543fc89224450.json`](../../sessions/64/645beaa543fc89224450.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**v3 分析结果（gen_0–gen_10, 11 点, 12 对 Granger 检验）：**

| 项目 | 结论 |
|---|---|
| **非单调 dose-response** | 确认。α=0.25 d1 drift -40.34% > α=0.50 -37.28%，d2/d3 同理 |
| **Granger FDR** | 0/12 显著。α=0.00 entropy→d1 p_raw=0.058（v2 是 0.048，不再 borderline sig） |
| **定性模式** | 不变：α=0.25 entropy 主导（p_raw=0.015），α=0.50 ECE 主导（p_raw=0.021） |
| **α=0.25 双向信号** | d1→entropy p_raw=0.023，提示 feedback loop（但 FDR=0.093 n.s.）|
| **Cross-corr** | entropy 一致 lag=+1 领先 d1；α=0.50 ECE lag=+1 r=-0.95 |
| **Velocity** | α=0.25 全程快于 α=0.50，否定"α=0.50 早期快后期饱和"解释 |

**已更新**：registry `alpha_sweep_a050_s42` metrics（含 gen_10 + p_raw/p_fdr 字段）、memory.md、artifact `art_20260515_b979dd`。服务器 JSON: `results/analysis/cross_alpha_v3_full.json`。

---
