# qwen15b_full_trace_seed42 实验结果

## eval_results.json

```json
{
  "condition": "full_trace",
  "checkpoint_dir": "/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_seed42/final",
  "metrics": {
    "accuracy": 0.7705882352941177,
    "majority_baseline": 0.7151260504201681,
    "lift": 0.055462184873949605,
    "majority_class": "pass",
    "n": 1190,
    "pass_precision": 0.8232662192393736,
    "pass_recall": 0.8648648648648649,
    "pass_f1": 0.8435530085959886,
    "fail_precision": 0.6114864864864865,
    "fail_recall": 0.5339233038348082,
    "fail_f1": 0.5700787401574803
  },
  "confidence_intervals": {
    "accuracy_ci_lower": 0.7478781512605042,
    "accuracy_ci_upper": 0.795798319327731,
    "majority_baseline_ci_lower": 0.6915966386554622,
    "majority_baseline_ci_upper": 0.738655462184874,
    "lift_ci_lower": 0.02689075630252102,
    "lift_ci_upper": 0.08237394957983195,
    "pass_precision_ci_lower": 0.7993235625704622,
    "pass_precision_ci_upper": 0.8474208755155376,
    "pass_recall_ci_lower": 0.8402307692307692,
    "pass_recall_ci_upper": 0.887734180276794,
    "pass_f1_ci_lower": 0.8252868134999797,
    "pass_f1_ci_upper": 0.8625304573475305,
    "fail_precision_ci_lower": 0.5559119152046784,
    "fail_precision_ci_upper": 0.6677318870452438,
    "fail_recall_ci_lower": 0.48104956268221577,
    "fail_recall_ci_upper": 0.5828767889087656,
    "fail_f1_ci_lower": 0.5240254706533777,
    "fail_f1_ci_upper": 0.6137442809752248
  }
}
```

## 训练日志（最后 50 行）

```
{'train_runtime': 2808.6793, 'train_samples_per_second': 5.042, 'train_steps_per_second': 0.158, 'train_loss': 0.04993047436011267, 'epoch': 3.0}
Training complete. Model saved to /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_seed42/final
Condition: full_trace
Checkpoint: /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_seed42/final
Test samples: 1190
Loading base model from /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct
Loading LoRA adapter from /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_seed42/final
Running inference...
  [50/1190] running accuracy: 0.9000
  [100/1190] running accuracy: 0.8800
  ...
  [1150/1190] running accuracy: 0.7722

=== Evaluation Results (condition: full_trace) ===
Accuracy:           77.1% (95% CI: [74.8%, 79.6%])
Majority baseline:  71.5% (always predict 'pass')
Lift over majority: +5.5pp (95% CI: [+2.7pp, +8.2pp])

Per-class metrics:
  pass:  P=0.82  R=0.86  F1=0.84
  fail:  P=0.61  R=0.53  F1=0.57
```

## Checkpoint 文件列表

```
adapter_config.json          1.1 KB
adapter_model.safetensors   70.5 MB
eval_results.json            1.4 KB
predictions.jsonl           75.6 KB
tokenizer.json              10.9 MB
training_args.bin            6.3 KB
+ README.md, added_tokens.json, chat_template.jinja, merges.txt, special_tokens_map.json, tokenizer_config.json, vocab.json
```

W&B summary: 不存在。

## 关键指标摘要

| 指标 | 值 |
|------|-----|
| Accuracy | 77.06% |
| Accuracy 95% CI | [74.8%, 79.6%] |
| Majority baseline | 71.5% |
| Lift over baseline | +5.5pp |
| Pass F1 | 0.844 |
| Fail F1 | 0.570 |
| Train loss | 0.0499 |
| Epochs | 3 |
| Train runtime | 2808.7s (~47 min) |

## 对比分析

### vs 同模型（Qwen-1.5B）其他 trace 条件

| Condition | Accuracy | Fail F1 | Pass F1 | Lift |
|-----------|----------|---------|---------|------|
| **full_trace (本实验)** | **77.06%** | **0.570** | **0.844** | **+5.5pp** |
| exception_only | 99.83% | ~1.00 | ~1.00 | +28.3pp |
| VOTA | 99.58% | ~1.00 | ~1.00 | +28.1pp |
| no_trace | 67.31% | — | — | -4.2pp |

**发现**：full_trace 在 Qwen-1.5B 上表现远不如 exception_only 和 VOTA。exception_only 和 VOTA 几乎达到完美准确率（99.8%+），而 full_trace 仅比 majority baseline 高 5.5pp。完整 trace 对 1.5B 小模型信息过于复杂，反而不如精简格式。

### vs 7B 模型 full_trace 条件

| Model | Accuracy | Fail F1 | Pass F1 | Lift |
|-------|----------|---------|---------|------|
| **Qwen-1.5B (本实验)** | **77.06%** | **0.570** | **0.844** | **+5.5pp** |
| DeepSeek-Coder-7B v3 | 79.16% | 0.637 | 0.854 | +7.7pp |
| DeepSeek-Coder-7B v5 | 81.76% | 0.685 | 0.872 | +10.3pp |
| DeepSeek-7B 512tok | 80.42% | 0.665 | 0.862 | +8.9pp |
| DeepSeek-7B label_only | 86.22% | 0.740 | 0.906 | +14.7pp |

**发现**：
- Qwen-1.5B full_trace (77.1%) 比 7B full_trace 最佳版本 (81.8%) 低约 4.7pp
- 7B 的 fail_recall 明显更好（0.64-0.70 vs 0.53），1.5B 对 fail 类检测能力较弱
- 7B label_only (86.2%) 远超 1.5B full_trace (77.1%)

### 核心结论

1. **Trace 格式 > 模型大小**：Qwen-1.5B + exception_only (99.8%) >> DeepSeek-7B + full_trace (81.8%)
2. **Full trace 对小模型不友好**：1.5B 处理完整 trace 时 lift 仅 5.5pp，用精简格式可达 28pp+
3. **Fail 检测是瓶颈**：1.5B full_trace 的 fail_recall 仅 0.53，近半数 fail 样本被误判为 pass
