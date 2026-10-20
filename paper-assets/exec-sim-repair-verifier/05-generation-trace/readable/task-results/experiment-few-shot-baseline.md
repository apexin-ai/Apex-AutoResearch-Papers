# experiment few shot baseline

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_few-shot-baseline_20260517T115423_result.json`
- **Structured JSON:** [`8650aa08c4ad4dca2e25.json`](../../sessions/86/8650aa08c4ad4dca2e25.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存到 `artifacts/few_shot_baseline.json`。

## 3-shot Baseline 结果汇总

| Model | Accuracy | Pass F1 | Fail F1 | Unparseable |
|---|---|---|---|---|
| DeepSeek-coder-6.7B-instruct | 59.95% | 44.13% | 68.78% | 0% |
| Qwen3-8B | 68.78% | 64.46% | 72.17% | 0% |

**对比参考**:
- Zero-shot: 64.4%
- Fine-tuned CLS: 86.85%

**关键观察**:
- DeepSeek 3-shot (59.95%) 反而低于 zero-shot (64.4%)，且严重偏向预测 fail (tn=834, fn=679)，pass 召回极低 (299/978 = 30.6%)
- Qwen3-8B 3-shot (68.78%) 优于 DeepSeek 零/少样本，但仍远低于 fine-tuned CLS (86.85%)，验证了 fine-tuning 的必要性
- 两个模型 unparseable rate 均为 0%，输出格式遵循良好

---
