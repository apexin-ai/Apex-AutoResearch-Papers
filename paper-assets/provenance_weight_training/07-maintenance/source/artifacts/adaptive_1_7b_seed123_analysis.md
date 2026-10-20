# adaptive_1_7b_seed123 训练结果分析

**服务器**: westd-41312  
**分析日期**: 2026-05-19

## 训练状态: 成功完成

- EXIT_CODE=0, 进度 100% (6103/6103 steps)
- 训练时间: 18540s (约 5h 09m), ~3.04 s/step
- 模型已保存

## 关键指标

| 指标 | seed123 | seed42 (参考) | 备注 |
|------|---------|-------------|------|
| train_loss | **9.144** | 5.36 | seed123 显著偏高 |
| total_steps | 6103 | 6103 | 一致 |
| epoch | 0.2629 | - | - |
| 最终 lr | 3.45e-08 | - | cosine decay 到尾部 |

## Loss 差异分析

seed123 的 train_loss (9.144) 显著高于 seed42 (5.36)。整个训练过程中 trainer 报告的 loss 在 8.0~10.5 范围波动, 未见明显下降趋势。

注意: trainer 报告的 `loss` 是 weighted loss (经过 adaptive weighting 后的值)。step_metrics.jsonl 中最后几步的 per-example 数据显示:
- weighted_loss: 1.08 ~ 3.14
- unweighted_loss: 1.34 ~ 2.31

可能的解释:
1. seed 改变数据顺序, adaptive weighting 在不同数据分布下表现不同, 导致 weighted loss 整体偏高
2. seed42 的 train_loss 可能是 unweighted_loss, 而 seed123 是 weighted_loss (需确认两者口径)
3. 如果两者都是同口径 loss, 则 seed123 结果异常, 需排查

**建议**: 对比两个 seed 的日志格式, 确认 train_loss 口径是否一致。

## Checkpoints

```
/root/autodl-tmp/provenance_weight_training/output/models/adaptive_1_7b_seed123/
├── checkpoint-5500/
├── checkpoint-6000/
├── checkpoint-6103/
├── final/           ← 最终模型 (model.safetensors 3.4GB)
├── config.json
└── step_metrics.jsonl
```

## 训练配置

- model: Qwen3-1.7B
- weighting_method: adaptive
- tau: 0.8, n_min: 2, contamination_ratio: 0.4
- batch_size: 4, lr: 5e-05
- num_train_tokens: 200M, num_examples: 371499
- seed: 123

## Eval 状态

训练日志中无 eval_loss / eval_ppl。**需要独立 eval** (holdout set PPL), 与 seed42 的 PPL 13.27 对比。

## 下一步

1. 确认 seed42 和 seed123 的 train_loss 口径是否一致 (weighted vs unweighted)
2. 在 holdout set 上运行独立 eval, 获取 PPL
3. 如果 PPL 与 seed42 相近, 则 train_loss 差异仅为 weighted loss 的 seed 方差; 如果 PPL 也显著偏高, 需要排查原因
