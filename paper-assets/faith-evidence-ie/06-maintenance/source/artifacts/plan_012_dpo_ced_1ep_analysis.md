# plan_012_dpo_ced_1ep 训练指标分析

## 训练概要

| 项目 | 值 |
|------|-----|
| 模型 | Qwen3-4B + SFT adapter (merged) |
| 数据 | 2666 DPO pairs |
| 总步数 | 167 steps (1 epoch) |
| 训练时间 | 33 min 49 sec (2029.9s) |
| 速度 | 1.313 samples/s, 0.082 steps/s |
| 状态 | 正常结束 (EXIT_CODE=0) |

## 训练指标轨迹

| Epoch | Step | Loss | Rewards Acc | Margins | Chosen Reward | Rejected Reward |
|-------|------|------|-------------|---------|---------------|-----------------|
| 0.06 | 10 | 0.6930 | 0.4125 | 0.0007 | 0.0022 | 0.0015 |
| 0.12 | 20 | 0.6923 | 0.5500 | 0.0022 | -0.0017 | -0.0039 |
| 0.18 | 30 | 0.6871 | 0.6438 | 0.0127 | 0.0026 | -0.0101 |
| 0.84 | 140 | 0.4844 | 0.8000 | 0.7504 | -0.9638 | -1.7143 |
| 0.90 | 150 | 0.5373 | 0.7438 | 0.6518 | -0.9173 | -1.5691 |
| 0.96 | 160 | 0.5036 | 0.7813 | 0.7423 | -0.9637 | -1.7059 |
| **1.00** | **167** | **0.5933** | **0.8208** | **0.8593** | **-0.9328** | **-1.7921** |

## 1ep vs 3ep 对比

| 指标 | 1ep (本次) | 3ep (过拟合) | 判断 |
|------|-----------|-------------|------|
| rewards/accuracies | **0.8208** | 1.0000 | 1ep 未饱和，健康 |
| rewards/margins | **0.8593** | 9.01 | 1ep 差距合理 (~10x 小) |
| train_loss | **0.5933** | ~0.1 (推测) | 1ep loss 仍有余量 |
| logps/chosen | -42.02 | — | 偏移适中 |
| logps/rejected | -58.02 | — | 偏移适中 |
| mean_token_accuracy | 0.9677 | — | — |

## 过拟合信号检查

- **rewards/accuracies = 0.82**：训练末期在 0.74–0.82 间波动，未锁死 1.0。健康。
- **rewards/margins = 0.86**：相比 3ep 的 9.01 下降了一个数量级。chosen/rejected 没有被极端拉开。
- **Loss 轨迹**：从 0.693 (接近 ln2，随机水平) 稳步下降到 0.49–0.54 区间，最终报告 0.5933 (含 warmup 平均)。没有塌缩到接近 0。
- **Accuracy 轨迹**：0.41 → 0.55 → 0.64 → ... → 0.78–0.82，渐进上升，未跳变到 1.0。

**结论：过拟合信号已消除。**

## Checkpoint 产出

路径: `/root/autodl-tmp/dpo_output_1ep/`

```
adapter_model.safetensors   528 MB
adapter_config.json
checkpoint-100/
checkpoint-167/             (final)
tokenizer files (vocab.json, merges.txt, tokenizer.json, etc.)
training_args.bin
ref/                        (reference model)
```

关键文件 `adapter_model.safetensors` (528MB) 已生成，checkpoint-167 为最终 checkpoint。

## 结论

1. **过拟合已消除**：rewards_accuracy 0.82 (vs 1.0), margins 0.86 (vs 9.01)，均在健康范围
2. **训练学到了有效信号**：accuracy 从随机水平 (0.41) 提升到 0.82，模型确实学会了区分 chosen/rejected
3. **值得跑 eval**：指标健康，应该立即用 eval pipeline 测 rel_f1，看是否超过 SFT baseline (0.4057)
