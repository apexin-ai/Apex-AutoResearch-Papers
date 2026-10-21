# ssh check qwen epoch accuracy

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_qwen_epoch_accuracy_20260515T140516_result.json`
- **Structured JSON:** [`f5b55bd8af55d2e21f8c.json`](../../sessions/f5/f5b55bd8af55d2e21f8c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### Qwen 三个条件的 epoch-level 数据汇总

| 条件 | Epoch 1 eval_loss | Epoch 2 eval_loss | Epoch 3 eval_loss | 趋势 | 中间 checkpoint | epoch-level verdict accuracy |
|------|-------------------|-------------------|-------------------|------|----------------|------------------------------|
| **vota** | 0.0654 | 0.0795 | 0.0867 | 递增 ↑ | ✅ (148, 296, 444) | ❌ 无 |
| **no_trace** | 0.4944 | 0.5886 | 0.6454 | 递增 ↑ | ✅ (148, 296, 444) | ❌ 无 |
| **full_trace** | 0.0619 | 0.0766 | 0.0841 | 递增 ↑ | ✅ (148, 296, 444) | ❌ 无 |

### 关键发现

1. **三个 Qwen 条件的 eval_loss 都是单调递增的**（epoch 1 最低），与 DeepSeek VOTA 行为一致。
2. **中间 checkpoint 存在但未跑 evaluate.py**——eval_results.json 只在 `final/` 目录下，中间 checkpoint 目录内没有。唯一有中间 checkpoint eval_results 的是 `deepseek_vota/checkpoint-148`。
3. **需要派 eval Worker** 对 Qwen 的 6 个中间 checkpoint（3 条件 × checkpoint-148 和 checkpoint-296）跑 evaluate.py，才能获得 epoch-level verdict accuracy，验证 eval_loss 与 accuracy 是否在 Qwen 上也存在解耦现象。

---
