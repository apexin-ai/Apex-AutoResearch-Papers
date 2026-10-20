# audit ece investigation

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_ece-investigation_20260523T112743_result.json`
- **Structured JSON:** [`120c1bd1578f46bc9166.json`](../../sessions/12/120c1bd1578f46bc9166.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完成。以下是完整结论。

---

## 根因：两个表使用了不同的 ECE 分箱范围

| | `calibration_model_level` | `calibration_cross` |
|---|---|---|
| **脚本** | `eval/calibration_eval.py` | `eval/cross_model_calibration.py` |
| **原始数据** | `outputs/calibration_results.json` | `cross_model_calibration_results.json` |
| **ECE bin 范围** | `np.linspace(0, 1, 11)` — **[0, 1]** | `np.linspace(0.5, 1.0, 11)` — **[0.5, 1.0]** |
| **所在 appendix 位置** | ~L820, subsection "Calibration Analysis" | ~L586, section "Calibration Analysis" (calibration_full) |
| **实验设定** | exception_only, seed 42, N=1190, 4 models | **完全相同** |

两个表测量的是**同一个实验**，但 ECE 分箱粒度不同。[0.5, 1.0] 的 10 个 bin（宽 0.05）在高置信度区域分辨率更高，会捕捉到更多 miscalibration，因此 ECE 偏大。

## 4 个模型的 ECE 对照

| Model | `model_level` [0,1] bins | `cross` [0.5,1.0] bins | 原始精确值 (cross) |
|---|---|---|---|
| Qwen-1.5B | 0.0014 | 0.0020 | 0.001976 |
| Qwen-7B | 0.0017 | 0.0027 | 0.002717 |
| CodeLlama-13B | 0.0020 | 0.0020 | 0.002039 |
| **DeepSeek-6.7B** | **0.0048** | **0.0064** | **0.006411** |

## 正文 claim 分析

experiments.tex L197:
> "all four models (1.5B–13B) achieve ECE < 0.005 under exception_only (Table calibration_model_level)"

- 对 `calibration_model_level` 表（[0,1] bins）：成立（最大 0.0048）
- 对 `calibration_cross` 表（[0.5,1] bins）：**不成立**（DeepSeek = 0.0064）
- `calibration_cross` 表的 caption 自己说的是 "ECE < 0.007"，与正文矛盾

## 核心问题

论文同一个 appendix 中有**两个冗余表**报告同一实验的不同 ECE 值，且未说明方法差异。Reviewer 如果注意到两个 DeepSeek ECE 值 (0.0048 vs 0.0064) 不一致，会质疑数据可靠性。

## 建议修复方案

**方案 A（推荐）**：删除 `calibration_model_level` 表，保留 `calibration_cross`（位置更自然、含 MCE、分辨率更高）。将正文 claim 改为 "ECE < 0.007"。

**方案 B**：统一两个表的 bin 范围为 [0, 1]（文献标准），重新计算 `calibration_cross` 的 ECE。保留 "ECE < 0.005" claim。

**方案 C**：保留两个表，但加脚注说明 bin 范围差异，正文 claim 改为保守值 "ECE < 0.007"。

---
