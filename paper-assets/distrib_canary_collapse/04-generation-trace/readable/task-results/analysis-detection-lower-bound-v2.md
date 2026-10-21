# analysis detection lower bound v2

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_detection_lower_bound_v2_20260521T091810_result.json`
- **Structured JSON:** [`a84e5e0f3bd64130c5f4.json`](../../sessions/a8/a84e5e0f3bd64130c5f4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

### 修复结果

**v1 错误** → **v2 修正**（全部从 JSON 实时读取）:

| α | v1 (硬编码) | v2 (JSON) | 来源 |
|---|---|---|---|
| 0.50 | 0/8 | **6/8** | a050_s42/s43/s44_fp32 |
| 0.52 | 0/8 | **3/8** | a052_s42_fp32 |
| 0.10 s43 | 0/8 | **3/8** | a010_s43_fp32 |

**Spot-check 全部通过**：α=0.50→6/8, α=0.52→3/8, α=0.00→0/8, α=0.75≥6/8

### Proposition 1 重拟合

- **Joint model**: `rate(α,T) = 0.70 / (1 + exp(-100·(α - α_c(T))))`, R²=0.883
- **α_c(T) = 0.193 + 75.68·T^(-2.41)**
  - α_c(10) = **0.487**（旧版 ~0.67）
  - α_c(20) = **0.248**
- Sigmoid k=100 反映数据中 α=0.48→0.50 的 sharp phase transition

### 产出文件（westd-17855）
- 脚本: `scripts/detection_lower_bound_v2.py`
- 输出目录: `artifacts/detection_bound_v2/`
  - `detection_bound_results_v2.json`
  - `fig_delta_min_vs_T.pdf/png`
  - `fig_signal_strength.pdf/png`
  - `fig_phase_boundary.pdf/png`
  - `proposition.tex`

---
