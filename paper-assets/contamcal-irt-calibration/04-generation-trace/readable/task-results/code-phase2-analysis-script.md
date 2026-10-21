# code phase2 analysis script

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_phase2-analysis-script_20260519T120028_result.json`
- **Structured JSON:** [`56e27bb6bb356db49273.json`](../../sessions/56/56e27bb6bb356db49273.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

运行成功。结果摘要：

**已完成**: gemma2 全 5 dosage, phi4 d000-d050 (缺 d100), qwen14b d000-d050 (缺 d100), qwen7b 全 5 dosage, olmo2 全部缺失。

**MMLU 趋势**:
- **gemma2**: +3.76pp (d000→d100), 非单调, Spearman r=0.90 (p=0.037, 显著)
- **qwen14b**: 严格递减 (r=-1.0), d000 0.694 → d050 0.594, 下降 10pp
- **qwen7b**: -1.78pp, 非单调, r=-0.60 (不显著)
- **phi4**: 基本持平, 非单调

**ARC 趋势**:
- **gemma2 ARC**: 大幅振荡 (0.86→0.78→0.87→0.71→0.85), r=-0.30, 符合预期的不可靠标注
- **qwen14b/qwen7b ARC**: 均递减

三个输出文件已生成：
- `phase2_summary.csv`
- `phase2_mmlu_dose_response.pdf`
- `phase2_arc_dose_response.pdf`

---
