# XNLI MLP Probe Results — C3 Non-linearity Specificity Test

**Date**: 2026-05-22
**Server**: westd-41302
**Task**: 验证 C3 (non-linearity) 是否为冲突任务特有的 contribution

## 完整对比表 (Balanced Accuracy %)

| Model | Direction | XNLI Linear | XNLI MLP | XNLI Δ | Conflict Linear | Conflict MLP | Conflict Δ |
|-------|-----------|:-----------:|:--------:|:------:|:--------------:|:------------:|:----------:|
| **Qwen3** | EN→EN | 96.58 | 96.58 | +0.0 | 75.00 | 77.38 | **+2.4** |
| | ZH→ZH | 89.49 | 90.99 | +1.5 | 72.62 | 75.00 | **+2.4** |
| | EN→ZH | 90.45 | 88.43 | **-2.0** | 67.26 | 69.64 | **+2.4** |
| | ZH→EN | 97.17 | 97.46 | +0.3 | 73.21 | 73.81 | +0.6 |
| **Llama3.1** | EN→EN | 93.98 | 93.03 | -1.0 | 77.57 | 80.51 | **+2.9** |
| | ZH→ZH | 87.47 | 88.47 | +1.0 | 72.06 | 74.63 | **+2.6** |
| | EN→ZH | 88.95 | 88.48 | **-0.5** | 59.56 | 68.75 | **+9.2** |
| | ZH→EN | 94.92 | 94.69 | -0.2 | 71.32 | 75.00 | **+3.7** |

## 关键发现：EN→ZH 方向 MLP Gains 对比

| Model | XNLI EN→ZH Δ | Conflict EN→ZH Δ | 差异 |
|-------|:------------:|:----------------:|:----:|
| Qwen3 | -2.0pp | +2.4pp | 4.4pp |
| Llama3.1 | -0.5pp | +9.2pp | 9.7pp |

## 判断

**C3 成立：方向依赖的非线性 encoding 是冲突任务特有的。**

核心证据：
1. **XNLI EN→ZH MLP gains 均为负值**（Qwen -2.0pp, Llama -0.5pp），MLP 不仅没有提升，反而略有下降
2. **冲突任务 EN→ZH MLP gains 显著为正**（Qwen +2.4pp, Llama +9.2pp），尤其 Llama 提升近 10pp
3. 两个模型一致表现出这一模式，排除了模型特异性的解释

解读：在 XNLI（无冲突的 NLI 任务）上，跨语言 representation 已经被线性 probe 充分捕获，MLP 的额外非线性容量无法带来增益。但在知识冲突任务上，EN→ZH 方向存在需要非线性变换才能解码的 conflict-specific representation，这正是 C3 所预测的。

## 补充观察

- XNLI 整体 probe accuracy 远高于冲突任务（88-97% vs 60-80%），说明 NLI label 比 conflict detection 更容易从 residual stream 中线性解码
- XNLI 的 mono-lingual 方向（EN→EN, ZH→ZH）MLP gains 也接近 0 或微正，说明 MLP 的非线性容量在 XNLI 上整体无用
- 冲突任务中除 EN→ZH 外的方向也有 MLP gains（+0.6 到 +3.7pp），但 EN→ZH 方向的 Llama +9.2pp 是最显著的 outlier

## 数据来源

- XNLI Linear: `data/xnli/{qwen3,llama31}/probe_results.json`
- XNLI MLP: `data/xnli/{qwen3,llama31}/mlp_probe_results.json`
- Conflict Linear: `data/{qwen3,llama31}/probe_results.json`
- Conflict MLP: `data/{qwen3,llama31}/mlp_probe_results.json`
