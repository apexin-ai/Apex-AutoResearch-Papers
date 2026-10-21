# DeepSeek VOTA Seed42 实验分析

## 实验配置
- Model: deepseek-ai/deepseek-coder-6.7b-instruct
- Condition: vota
- Data: 4720 train / 1190 test
- Seed: 42
- Training: 3 epochs, 444 steps, ~2h12m on cuda:0

## 核心指标

| Metric | Value | 95% CI |
|--------|-------|--------|
| Accuracy | 84.45% | [82.60%, 86.39%] |
| Majority baseline | 71.51% | [69.16%, 73.87%] |
| Lift | +12.94pp | [+11.09pp, +14.87pp] |

### Per-class metrics

| Class | Precision | Recall | F1 |
|-------|-----------|--------|-----|
| pass | 0.821 [0.800, 0.843] | 1.000 [1.000, 1.000] | 0.902 [0.889, 0.915] |
| fail | 1.000 [1.000, 1.000] | 0.454 [0.405, 0.505] | 0.625 [0.576, 0.671] |

Bootstrap: 1000 resamples

## 训练 Loss 曲线

**Train loss（第一个 epoch 采样）：**
- epoch 0.07: 0.4668 → epoch 0.27: 0.1057 → epoch 0.95: 0.0522
- 快速收敛，0.3 epoch 内 loss 从 0.47 降到 0.09

**Eval loss & classification accuracy by epoch：**
| Epoch | Eval Loss | Eval Mean Token Acc | Verdict Accuracy | Fail Recall |
|-------|-----------|---------------------|-----------------|-------------|
| 1.0 | 0.0679 | 0.9802 | 78.15% | 23.3% |
| 2.0 | 0.0950 | 0.9794 | — | — |
| 3.0 | 0.1121 | 0.9791 | 84.45% | 45.4% |

**eval_loss 与 classification accuracy 解耦**：eval_loss 单调递增 (+65%) 但 verdict accuracy 从 78.15% 提升到 84.45% (+6.3pp)，fail recall 从 23.3% 提升到 45.4% (+22.1pp)。continued training 改善了分类能力（尤其是 fail 识别），eval_loss 上升反映 token-level calibration 退化而非分类能力下降。eval_loss 不是 verdict task 的可靠 checkpoint selection criterion。

### Epoch-level Classification Performance
| Epoch | Eval Loss | Accuracy | Fail Recall | Fail Precision |
|-------|-----------|----------|-------------|----------------|
| 1 | 0.0679 | 78.15% | 23.3% | — |
| 3 (final) | 0.1121 | 84.45% | 45.4% | 100% |

Continued training improves verdict classification (+6.3pp accuracy, +22.1pp fail recall) despite increasing eval_loss. This validates using the final checkpoint rather than the lowest-loss checkpoint for verdict classification.

## Within-Model 对比（DeepSeek-Coder-6.7B）

| Condition | Accuracy | 95% CI |
|-----------|----------|--------|
| DeepSeek no_trace | 73.4% | [70.8%, 75.7%] |
| **DeepSeek VOTA** | **84.5%** | **[82.6%, 86.4%]** |
| **Within-model lift** | **+11.09pp** | CI 不重叠，显著 |

- deepseek_no_trace conclusion = **negative**（lift +1.85pp over majority, CI [-0.93, +4.63] 跨 0，不显著）
- DeepSeek VOTA within-model lift: 84.45% − 73.36% = **+11.09pp**，统计显著

### Cross-Model Comparison (Qwen-2.5-Coder-7B vs DeepSeek-Coder-6.7B)

| Condition | Qwen-2.5-Coder-7B | DeepSeek-Coder-6.7B | Δ |
|-----------|-------------------|---------------------|---|
| no_trace | 75.1% [72.8, 77.5] | 73.4% [70.8, 75.7] | −1.7pp（CI 重叠，不显著）|
| VOTA | 99.2% [98.6, 99.7] | 84.5% [82.6, 86.4] | −14.7pp（显著）|
| VOTA within-model lift | +24.0pp | +11.1pp | — |

**核心发现**：两模型 no_trace 基线接近（Δ = −1.7pp，不显著）→ VOTA 效果差距 (−14.7pp) 完全来自 trace 利用效率差异，而非基础代码理解能力差距。

## 关键发现

1. **Pass 偏向严重**：模型对 pass 有 100% recall 但对 fail 只有 45.4% recall，说明模型倾向于预测 pass。Fail precision 为 1.0 表示当模型预测 fail 时总是对的，但它漏掉了超过一半的 fail 样本。
2. **eval_loss 与 verdict accuracy 解耦**：eval loss 从 epoch 1 的 0.068 增加到 epoch 3 的 0.112 (+65%)，但 verdict accuracy 从 78.15% 提升到 84.45% (+6.3pp)，fail recall 从 23.3% 提升到 45.4% (+22.1pp)。eval_loss 上升反映 token-level calibration 退化，不是分类能力下降。这验证了 revert load_best_model_at_end 的决策正确性——用 eval_loss 选 checkpoint 会选到分类能力更差的 epoch 1。
3. **VOTA 对 DeepSeek 有效但 trace 利用效率远低于 Qwen**：DeepSeek VOTA within-model lift +11.09pp（vs DeepSeek no_trace 73.4%），而 Qwen VOTA lift +24.0pp。两模型 no_trace 基线接近（Δ=1.7pp，不显著），VOTA 效果差距完全来自 trace 利用效率差异。

## 结论

**Success** — accuracy 84.5% 显著高于 DeepSeek no_trace baseline 73.4%（within-model lift +11.09pp，95% CI 不重叠），VOTA 条件对 DeepSeek 模型同样有效。但 within-model lift (+11.1pp) 远低于 Qwen (+24.0pp)，且两模型 no_trace 基线接近（Δ=1.7pp，不显著），说明 trace 利用效率是跨模型效果差异的主因。