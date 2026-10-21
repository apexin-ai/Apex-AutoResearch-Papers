# codellama13b_loop_only_seed456 Analysis

## 结果

| Metric | Value | 95% CI |
|--------|-------|--------|
| Accuracy | 79.08% | [76.9%, 81.3%] |
| Majority baseline | 71.5% (always predict 'pass') | [69.2%, 73.9%] |
| Lift over majority | +7.6pp | [+4.3pp, +11.2pp] |
| **Pass** Precision | 0.912 | [0.892, 0.933] |
| **Pass** Recall | 0.783 | [0.756, 0.810] |
| **Pass** F1 | 0.843 | [0.824, 0.861] |
| **Fail** Precision | 0.598 | [0.556, 0.644] |
| **Fail** Recall | 0.811 | [0.770, 0.852] |
| **Fail** F1 | 0.688 | [0.653, 0.723] |

- n = 1190 eval samples
- Training: ~0.95 epochs, final train_loss = 0.076, mean_token_accuracy = 0.977
- Wall clock: 3.91 GPU-hours

## 3-Seed 汇总 (CodeLlama-13B loop_only)

| Metric | seed42 | seed123 | seed456 | Mean±Std |
|--------|--------|---------|---------|----------|
| Accuracy | 77.06% | 76.05% | 79.08% | **77.40±1.54%** |
| Fail F1 | 0.670 | 0.682 | 0.688 | **0.680±0.009** |
| Fail Recall | 0.826 | 0.903 | 0.811 | **0.847±0.049** |
| Lift | +5.6pp | +4.5pp | +7.6pp | **+5.9±1.5pp** |

- seed456 是三个种子中 accuracy 最高的（79.08%），拉高了均值
- Fail recall 在 seed123 上异常高（0.903），导致该指标 std 较大（0.049）
- Fail F1 跨 seed 非常稳定（std=0.009）

## 与其他模型 loop_only 对比

| Model | Accuracy (Mean±Std) | Seeds | Fail F1 |
|-------|-------------------|-------|---------|
| Qwen-7B | 86.05±0.52% | 3 | ~0.79 |
| DeepSeek-6.7B | 81.26±0.00% | 2 | ~0.73 |
| Qwen-1.5B | 78.32% | 1 | ~0.69 |
| **CodeLlama-13B** | **77.40±1.54%** | **3** | **0.680** |

排序：Qwen-7B > DeepSeek-6.7B > Qwen-1.5B > CodeLlama-13B

## 结论

1. **seed456 在预期范围内（79.08% ∈ [74%, 80%]）**，假设验证通过。三个种子均在 76-79% 区间，loop_only 条件下 CodeLlama-13B 表现稳定。

2. **CodeLlama-13B 确认为 Tier 2 loop_only 最弱模型**。尽管参数量最大（13B），其 77.40% 均值低于 Qwen-1.5B（78.32%）和 DeepSeek-6.7B（81.26%），远低于 Qwen-7B（86.05%）。这说明 loop_only 条件下，模型架构/预训练数据的影响大于参数规模。

3. **3-seed 稳定性**：accuracy std=1.54%，略高于 Qwen-7B（0.52%）和 DeepSeek-6.7B（~0.00%），但仍在可接受范围内。Fail F1 的 std=0.009 表明模型对 fail 类别的检测能力跨 seed 一致。

4. **对 C3 (Tier hierarchy) claim 的支撑**：CodeLlama-13B 在 loop_only 下的 3-seed 结果进一步巩固了 tier 排序。参数量与 loop_only 性能的非单调关系（13B < 1.5B < 6.7B < 7B）是一个值得在论文中讨论的发现，暗示代码预训练质量和指令跟随能力可能比模型规模更重要。
