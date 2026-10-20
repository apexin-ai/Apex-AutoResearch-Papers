# code diagnostic calibration

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_diagnostic_calibration_20260518T173407_result.json`
- **Structured JSON:** [`7e9f12dec88e8fb42e64.json`](../../sessions/7e/7e9f12dec88e8fb42e64.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

## 7 个 Dataset-Model Combinations

| Combination | Degen% | ρ(LP,F1) | LP Range | Delta (pp) |
|---|---|---|---|---|
| SciERC-Qwen8B | 17.8 | 0.180 | 0.0401 | **+0.615** |
| CoNLL-Qwen8B | 47.4 | 0.329 | 0.0932 | **-0.921** |
| FewNERD-Qwen8B | 13.8 | 0.511 | 0.0662 | **+1.355** |
| CoNLL-LLaMA | 86.5 | 0.196 | 0.0076 | +0.144 |
| SciERC-LLaMA | 19.1 | 0.167 | 0.0589 | +0.168 |
| SciERC-Qwen4B | 10.4 | 0.189 | 0.0555 | **-2.230** |
| CoNLL-Qwen4B | 90.6 | 0.242 | 0.0000 | +0.089 |

## 核心发现：三指标框架预测能力极弱

- **Individual correlations**: 三个指标与 LP delta 的 Spearman ρ 均 ≈ 0（p > 0.75），无显著相关
- **3-indicator regression**: in-sample R² = 0.39，但 LOO R² = **-3.72**（严重过拟合，7 点 4 参数）
- **LOO sign accuracy**: 2/7 (**28.6%**)，比随机猜测还差
- **Best threshold rule**: `degen<20% & rho>0.15` 仅 57.1% 准确率

**关键 blocker**: SciERC-Qwen4B（degen=10.4%, rho=0.189）看起来满足"低退化+正相关"条件，但 LP selection 反而 -2.23pp。说明模型 logprob 校准质量是一个被三指标忽略的关键因素。

产出文件：
- `output/diagnostic_calibration_results.json`
- `output/diagnostic_calibration/diagnostic_calibration_scatter.png`
- `output/diagnostic_calibration/diagnostic_calibration_report.md`
- `code/diagnostic_calibration.py`

---
