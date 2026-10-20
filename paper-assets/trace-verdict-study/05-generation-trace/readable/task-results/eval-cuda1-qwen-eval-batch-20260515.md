# eval cuda1 qwen eval batch 20260515

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_cuda1_qwen_eval_batch_20260515_20260515T151342_result.json`
- **Structured JSON:** [`8d4429c22c1910b18035.json`](../../sessions/8d/8d4429c22c1910b18035.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部任务完成。汇总所有结果：

---

## 产出汇总

### 1. deepseek_exception_only 完整 metrics
| Metric | Value |
|--------|-------|
| **accuracy** | 0.9933 |
| majority_baseline | 0.7151 |
| lift | +0.2782 |
| n | 1190 |
| pass: P/R/F1 | 1.00 / 0.9906 / 0.9953 |
| fail: P/R/F1 | 0.9769 / 1.00 / 0.9883 |

### 2. VOTA 重跑结果
- **accuracy: 0.9941** (确认不是旧的 0.9916) ✅
- predictions.jsonl: **1190 行**
- eval_results.json 已更新

### 3. 其他 Qwen 条件一致性检查
| 条件 | eval_results.json | registry | 状态 |
|------|------------------|----------|------|
| no_trace | 0.7513 | 0.7513 | ✅ 一致 |
| full_trace | 0.8176 | 0.8176 | ✅ 一致 |
| exception_only | 0.9983 | 0.9983 | ✅ 一致 |
| loop_only | 0.8563 | 0.8563 | ✅ 一致 |

所有条件均已重跑生成 predictions.jsonl（各 1190 行）。

### 4. eval_qwen_epochs.sh epoch-level accuracy

| 条件 | checkpoint-148 (epoch 1) | checkpoint-296 (epoch 2) | final |
|------|-------------------------|-------------------------|-------|
| **vota** | 0.9933 | 0.9941 | 0.9941 |
| **no_trace** | 0.7429 | 0.7630 | 0.7513 |
| **full_trace** | 0.8303 | 0.7630 | 0.8176 |

注意：full_trace 从 epoch 1 (0.8303) 到 epoch 2 (0.7630) 出现了 accuracy 下降，final checkpoint 为 0.8176，说明可能存在过拟合或训练不稳定。no_trace 的 final (0.7513) 也低于 epoch 2 (0.7630)，可能是类似情况。vota 在各阶段保持稳定高性能。

---
