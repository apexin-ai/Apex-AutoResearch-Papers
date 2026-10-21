# analysis r1 w5 temperature seed variance

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r1_w5_temperature_seed_variance_20260521T195424_result.json`
- **Structured JSON:** [`30b84c61917416cd139e.json`](../../sessions/30/30b84c61917416cd139e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果非常清晰。总结如下：

## R1-W5 分析结果

### 核心发现

| 指标 | T=0.0 | T=0.3 | T=0.7 |
|------|-------|-------|-------|
| Accuracy | 0.7131 | 0.7148 | 0.7046 |
| Seed range | **0.000000** | 0.011458 | 0.043958 |
| Seed SD | **0.000000** | 0.004455 | 0.017104 |
| Seed SS% | **0.000000%** | 0.008114% | 0.117137% |
| Within-cell seed var | **≈0** (3e-33) | 1.01e-04 | 3.82e-04 |
| Item perfect agreement | **100.00%** | 84.35% | 70.42% |

### 解读

1. **T=0 下 seed 方差 = 0（完美确定性）**。所有 6 个 seed 在所有 24 个条件组合（6 prompts × 4 orderings）中产生完全相同的 item-level 结果。vLLM greedy decoding 在 bfloat16 下无任何 GPU non-determinism 效应。

2. **T>0 下 seed 方差单调递增**：T=0.7 的 within-cell seed variance 是 T=0.3 的 **3.8×**；seed range 约为 2×。符合 sampling stochasticity 随温度增大的预期。

3. **Seed SS% 占总方差极小**：即使 T=0.7，seed 仅解释 0.12% 的总方差。说明 prompt 和 ordering 的效应远大于 seed。

4. **Item 一致性下降显著**：T=0.3 有 15.65% 的 items 会因 seed 不同而翻转答案；T=0.7 升到 29.58%。

### 论文写法建议

- **T=0 完美确定性是强结论**：可以写 "At T=0, greedy decoding is fully deterministic—random seeds have zero effect on outputs, confirming that GPU non-determinism does not contribute measurable variance in our setup (bfloat16, vLLM)."
- **数据支撑 G-theory分解的正当性**：T=0 作为 baseline 表明所有 T>0 的 seed 方差纯粹来自 sampling noise，无需担心与硬件混淆。
- **建议做一个 Figure**：左边 bar chart 显示 3 个温度下的 seed SS%，右边显示 item-level agreement %，直观展示 deterministic→stochastic 的梯度。

### 产出文件

`/root/nlp_variance_gtheory/results/exp001_analysis/r1_w5_temperature_seed_variance.json`

---
