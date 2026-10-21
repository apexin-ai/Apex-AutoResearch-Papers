# analysis 3B mmlu gamma crossval

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_3B_mmlu_gamma_crossval_20260515T160046_result.json`
- **Structured JSON:** [`175bd9f8efa084ff779c.json`](../../sessions/17/175bd9f8efa084ff779c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the summary:

## 3B MMLU gamma=-5.70 交叉验证报告

### Raw Accuracy

| Model | MMLU Acc |
|-------|---------|
| d000_v2_s42 | 0.6295 |
| d000_v2_s123 | 0.6314 |
| d100_v2_s42 | 0.6320 |
| d100_v2_s123 | 0.6319 |

d000 均值 0.6304，d100 均值 0.6320，差异仅 **+0.16 pp**——几乎持平。

### MCMC 诊断

| 指标 | 3B | 1.5B |
|------|-----|------|
| max_rhat | 1.008 (OK) | 1.017 (NOT OK) |
| min_ess | 1059 (OK) | 115 (NOT OK) |
| divergences | 0 | 0 |
| **residual_mae** | **0.2168** | 0.0927 |
| obs vs pred acc | 0.627 vs **0.843** | 0.577 vs 0.484 |

3B 的 MCMC 采样本身收敛良好，但 **posterior predictive 严重失败**——模型预测均准 0.843，实际 0.627，系统性高估 22 pp。

### 数据不足

- 3B 只有 **4 个模型、2 个 dosage 水平**（d000, d100），无 d005/d025
- 1.5B 有 6 个模型、4 个 dosage 水平，且呈现清晰的剂量-反应关系

### 结论：**(c) 数据不足 + 模型误配导致的噪声**

gamma=-5.70 **不可信**。原因：
1. Raw accuracy 在 d000→d100 几乎无变化（+0.16 pp），不支持任何方向的强效应
2. 仅 2 个 dosage 水平、4 个模型，自由度不足以约束 IRT 参数
3. posterior predictive residual_mae=0.217 暴露严重模型误配——MCMC 收敛到了错误的解
4. 对比 1.5B（4 个 dosage、6 个模型、MAE=0.093），3B 的数据条件远不够支撑 stratified IRT

**建议**：补充 3B d005/d025 的 eval 数据后重新拟合，或对 3B 该 stratum 标记为 "insufficient data"。

---
