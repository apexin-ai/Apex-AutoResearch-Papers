# analysis d073 s2 new lf design

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d073-s2-new-lf-design_20260516T025932_result.json`
- **Structured JSON:** [`79dd2a49447c9883f259.json`](../../sessions/79/79dd2a49447c9883f259.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

## 新 LF 设计结果

### 4 个候选 LF（gold set N=601 上验证）

| LF | Threshold | Gold Coverage | Stag Precision | Full Coverage |
|---|---|---|---|---|
| **error_repetition** | ≥4次相同error | 4.2% | **84.0%** | 2.8% |
| **low_file_diversity** | files/actions ≤ 0.1 | 40.3% | 70.3% | **24.1%** |
| **action_entropy** | norm_entropy < 0.3 | 24.5% | 74.1% | 11.8% |
| **output_stagnation** | obs sim ≥ 0.8, run≥3 | 20.8% | **80.0%** | 9.8% |

### 选定的 3 个新 LF
`low_file_diversity`, `action_entropy`, `output_stagnation`（error_repetition 因 coverage 仅 2.8% 排名最低，但用 7-LF 时仍有边际贡献）

### MV 对比（vs gold set）

| 配置 | Macro F1 | F1(stag) | F1(prog) | Accuracy | Coverage |
|---|---|---|---|---|---|
| Old 3-LF MV | 0.682 | 0.559 | 0.805 | 0.730 | 97.2% |
| **New 6-LF MV** | **0.719** | **0.622** | **0.817** | **0.753** | 98.3% |
| All 7-LF MV | 0.724 | 0.629 | 0.819 | 0.756 | 98.3% |

**6-LF vs 3-LF 改进：macro_f1 +3.7pp, f1_stag +6.3pp, stag_recall +10.6pp**

### Label 翻转（214K windows）
- 总变化：16,702 (7.8%)
- 净方向：偏向 stagnation（+8,795 stag vs +4,877 prog）
- 3,030 窗口从 abstain 变为 labeled

### 关键发现
- **Overall pairwise conflict rate = 42.2%** → 远超 15% 阈值，**建议重跑 TWV/TLM**
- 3 个新 stagnation-only LF 之间 conflict rate = 0%（互补信号）
- 高 conflict 主要来自 `command_repetition`（偏好 progress）与新 LF（偏好 stagnation）的分歧

### 产出文件
- 分析报告：`artifacts/d073/new_lf_analysis.json`（服务器）
- LF 代码：追加到 `labeling_functions.py`（`ALL_LFS_EXTENDED` = 7 个 LF）
- 实现脚本：`new_lf_design.py`

---
