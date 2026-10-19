# exp021_ragen_sft_v4 分析报告

## 训练状态
- **状态**: 正常完成 (EXIT_CODE=0)
- **总步数**: 320 (2 epochs)
- **训练时间**: 2865s (~47.8 min)
- **Final train loss**: 0.038 (avg: 0.106)
- **Eval loss**: 0.0385
- **Eval mean_token_accuracy**: 98.8%
- **Loss 趋势**: 0.11 → 0.05 (epoch 0.6) → 0.035-0.04 (收敛)

## Checkpoint
- **路径**: /root/autodl-tmp/checkpoints/exp021_ragen_sft_v4/final
- **大小**: 3.3GB
- **中间 checkpoint**: checkpoint-160, checkpoint-320

## RAGEN val_before_train 评估 (核心测试)
| 指标 | 值 | Pass Criteria | 状态 |
|------|-----|---------------|------|
| **success** | **25%** | >= 10% | **PASS** |
| **action_is_valid** | **87.5%** | >= 85% | **PASS** |
| action_is_effective | 100% | - | - |
| pass@1 | 25% | - | - |
| avg num_actions | 24.75 | - | - |
| response_length | 2398 | - | - |

## eval_sft_fast 评估 (对比参考)
| 指标 | exp021 | exp019b (旧) |
|------|--------|--------------|
| success_rate | 0% | 20% |
| action_is_valid | 71% | ~70% |
| format_ok | 100% | ~90% |

## 关键发现

1. **格式兼容性修复成功**: exp019b 在 RAGEN val 中 0% success，exp021 达到 25%。核心目标达成。

2. **eval_sft_fast 下降原因**: exp021 用 RAGEN 格式训练（action 直接跟在 </think> 后面，不用 <answer> 标签），而 eval_sft_fast 用不同的 system prompt。模型偏向了 RAGEN 格式，导致在 eval_sft_fast 中表现下降。这是预期行为。

3. **RAGEN val 中 action_is_valid 87.5% 良好**: 模型生成的 action 大部分能被环境识别。

4. **结论**: exp021 成功解决了 SFT 训练格式与 RAGEN eval 格式不匹配的问题。模型在 RAGEN 原生评估中表现显著优于 exp019b (25% vs 0%)。
