# fig dose response

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fig_dose_response_20260517T094623_result.json`
- **Structured JSON:** [`d182c6fda6c742f1bd50.json`](../../sessions/d1/d182c6fda6c742f1bd50.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件生成完毕，验证通过（PDF 15.6KB, PNG 62.7KB，均 > 10KB）。

数据摘要：

| Scale | d000 (0%) | d005 (5%) | d025 (25%) | d100 (100%) |
|-------|-----------|-----------|------------|-------------|
| 0.5B  | 0.410 ± 0.012 | 0.313 ± 0.013 | 0.314 ± 0.034 | 0.270 ± 0.036 |
| 1.5B  | 0.585 ± 0.000 | 0.586 ± 0.001 | 0.589 ± 0.001 | 0.594 ± 0.001 |
| 3B    | 0.632 ± 0.001 | 0.632 ± 0.001 | 0.630 ± 0.006 | 0.635 ± 0.002 |

关键发现：
- **0.5B MMLU accuracy 随 dosage 显著下降**（0.41 → 0.27），SFT contamination 严重损害小模型通用能力
- **1.5B 和 3B 基本不受影响**，MMLU 保持平稳（~0.59 和 ~0.63）
- 图使用等间距 x 轴（0%/5%/25%/100%），Okabe-Ito 色盲友好配色，error bars 表示 seed 间变异

输出路径：
- `/root/contamcal-irt-calibration/figures/fig_dose_response.pdf`
- `/root/contamcal-irt-calibration/figures/fig_dose_response.png`

---
