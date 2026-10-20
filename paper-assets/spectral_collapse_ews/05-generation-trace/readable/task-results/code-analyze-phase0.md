# code analyze phase0

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_analyze_phase0_20260516T125016_result.json`
- **Structured JSON:** [`cf1038fe1751ebe4b0f9.json`](../../sessions/cf/cf1038fe1751ebe4b0f9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。脚本已部署到 `/root/spectral_collapse_ews/analyze_phase0.py`，dry-run 验证通过。

**Go/No-go 输出格式示例：**

```
============================================================
  PHASE 0 ANALYSIS REPORT — 410M-mock
============================================================

[1] DECLINE RATES (baseline: Gen 1)
    First half  (Gen 1→5): 34.1925 rank/gen
    Second half (Gen 5→10): 58.0000 rank/gen
    Acceleration ratio:     1.6963x

[2] GO/NO-GO DECISION
    Overall: ✓ PASS
    ✓ condition_1_monotonic: rank increases: 0 (allowed: 1)
    ✓ condition_2_acceleration: first_half_rate=34.1925, second_half_rate=58.0000, ratio=1.6963
    ✓ condition_3_perplexity: ppl_gen1=11.3800, ppl_gen10=62.0000, increase=444.82%

[3] τ/k CALIBRATION
    τ (threshold):  0.071171
    k (gain):       9.8354
    max Δ_t:        0.132176
```

产出文件：`results/phase0_analysis_report.json` + `results/phase0_analysis_plots.png`（4 panel 图）。

---
