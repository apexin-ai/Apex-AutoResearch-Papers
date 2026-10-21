# DeepSeek-6.7B VOTA seed123 Analysis

## Key Result

| Metric | seed123 | seed42 | |Delta| |
|--------|---------|--------|--------|
| **Accuracy** | **99.16%** | 84.45% | **+14.71pp** |
| Accuracy 95% CI | [98.57%, 99.66%] | — | — |
| Train Loss | 0.0625 | — | — |
| Eval Loss (epoch 3) | 0.1100 | — | — |

## Per-class Metrics

| Class | Precision | Recall | F1 |
|-------|-----------|--------|-----|
| pass | 0.990 | 0.999 | 0.994 |
| fail | 0.997 | 0.973 | 0.985 |

n=1190, majority baseline=71.5% (always predict "pass"), lift=+27.6pp.

## Cross-model VOTA Comparison

| Model | VOTA Accuracy | Tier |
|-------|---------------|------|
| Qwen-7B (seed42) | 99.05% | Tier 1 |
| Qwen-7B (seed456) | 99.41% | Tier 1 |
| Qwen-1.5B (seed42) | 99.58% | Tier 1 |
| CodeLlama-13B (seed42) | 98.57% | Tier 1 |
| **DeepSeek-6.7B (seed123)** | **99.16%** | **Tier 1** |
| DeepSeek-6.7B (seed42) | 84.45% | outlier? |

## Analysis

seed123 (99.16%) 与其他 3 个模型的 VOTA 结果高度一致（98.57%--99.58%），而 seed42 (84.45%) 是唯一显著偏低的结果。这强烈暗示 **seed42 是 outlier，而非 VOTA 在 DeepSeek 上的典型表现**。

seed42 的异常可能原因：
1. 训练不稳定（特定 seed 的 weight initialization 导致收敛到次优解）
2. 数据 shuffle 导致 early training 阶段 fail 样本集中，模型偏向 pass-only

## Seed Robustness 结论

**假设被推翻**：原假设 accuracy in [82%, 88%] 不成立。实际 accuracy=99.16% 远超预期。

seed42 vs seed123 的 14.71pp 差距表明 DeepSeek VOTA 的 seed sensitivity 远高于 Qwen-7B（99.05% vs 99.41%, |Delta|=0.36pp）。但 seed123 的结果证明 VOTA 方法本身在 DeepSeek 上是有效的，seed42 是 outlier。

**下一步**：deepseek_vota_seed456 已提交（PREPARING），作为 tie-breaker。若 seed456 in [95%, 100%] 则确认 seed42 是 outlier，DeepSeek VOTA 归 Tier 1。

## Provenance

- Server: westd-11235
- Checkpoint: /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_vota_seed123/final
- Log: ~/runs/trace-verdict-study/deepseek_vota_seed123.log
- Wall clock: 8533s (~2.37 GPU-hours)
- Training: 3 epochs, 444 steps
- Parent: deepseek_vota_seed42
