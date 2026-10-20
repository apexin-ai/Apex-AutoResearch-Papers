## full_trace_seed456 分析报告

### 单 seed 指标
- accuracy: 0.8050 (95% CI: [0.7824, 0.8269])
- fail_f1: 0.6578 (95% CI: [0.6174, 0.6977])
- lift vs majority: +8.99pp (95% CI: [+6.05pp, +12.10pp])
- pass: P=0.8637 R=0.8637 F1=0.8637
- fail: P=0.6578 R=0.6578 F1=0.6578
- train_loss: 0.0416, eval_loss: 0.0820
- n=1190, majority_baseline=0.7151

### 训练细节
- 模型: Qwen2.5-Coder-7B-Instruct + LoRA
- 训练时长: 2h11m (7862s), 3 epochs, 444 steps
- Epoch 2 eval_loss: 0.0728, Epoch 3 eval_loss: 0.0820 (轻微过拟合)
- Checkpoint: /root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_seed456/final

### 3-seed 统计 (full_trace condition)

| Metric | seed42 | seed123 | seed456 | Mean ± Std |
|--------|--------|---------|---------|------------|
| accuracy | 0.8176 | 0.7958 | 0.8050 | 0.8061 ± 0.0109 |
| fail_f1 | 0.6851 | 0.6620 | 0.6578 | 0.6683 ± 0.0147 |
| lift | 0.1025 | 0.0807 | 0.0899 | 0.0910 ± 0.0109 |
| pass_f1 | — | 0.8537 | 0.8637 | — |
| fail_precision | — | 0.6263 | 0.6578 | — |
| fail_recall | — | 0.7021 | 0.6578 | — |

### 观察
1. seed456 的 precision 和 recall 完全相等（0.6578），说明 pass→fail 和 fail→pass 的误分类数量恰好相同
2. 3 个 seed 的 accuracy std=0.0109，表明 full_trace 条件下训练稳定
3. 所有 3 个 seed 的 lift 都显著为正（>8pp），CI 下界均 >5pp
4. Epoch 2→3 eval_loss 略增（0.0728→0.0820），与 seed123 模式一致

### 结论
**SUCCESS** — seed456 accuracy=0.8050 在 seed42(0.8176) 和 seed123(0.7958) 的 ±5pp 范围内。3-seed 统计完成：full_trace condition mean accuracy=80.61%±1.09pp，mean lift=+9.10±1.09pp over majority baseline。结果可用于 rebuttal。
