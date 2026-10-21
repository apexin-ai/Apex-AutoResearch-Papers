# ablation-b 多种子复现报告

## 配置确认
ablation-b 实际训练配置: gradient_accumulation_steps=8
- 证据: 总步数 165 = ceil(1735/(4×8)) × 3 = 55 × 3
- train_config.json 未记录 ga（旧版脚本），但步数反推确凿

## 复现结果 (generation-level eval, val set: seed=42 random split, n=306)

| seed | accuracy | balanced_acc | int_recall | det_recall | pred int/det |
|------|----------|-------------|------------|-----------|-------------|
| 42 (原始) | 0.6536 | 0.5927 | 0.5152 | 0.6703 | 107/199 |
| 123 | 0.5719 | 0.5736 | 0.5758 | 0.5714 | 136/170 |
| 456 | 0.4314 | 0.5748 | 0.7576 | 0.3919 | 191/115 |
| 789 | 0.3987 | 0.5831 | 0.8182 | 0.3480 | 205/101 |

## 结论
- 成功率: 3/3 非退化 generation-level router
- balanced_acc 稳定: 57.4-58.3% (原始 59.3%)
- internal_recall 均 >50%, 但新 seed 偏高 (recall tradeoff 偏移)
- 注意: 训练脚本更新 (episode-level stratified split vs 原始 random shuffle)
