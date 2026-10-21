# analysis gradient masking seed123 eval

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gradient_masking_seed123_eval_20260522T145428_result.json`
- **Structured JSON:** [`7cf9fb80b63298454c1b.json`](../../sessions/7c/7cf9fb80b63298454c1b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新至 DONE。

## 评估结果汇总

### gradient_masking_qwen7b_seed123

| 指标 | 值 |
|------|-----|
| **accuracy** | **99.33%** [CI: 98.82%–99.75%] |
| pass_precision | 1.000 |
| pass_recall | 0.991 |
| pass_f1 | 0.995 |
| fail_precision | 0.977 |
| fail_recall | 1.000 |
| fail_f1 | 0.988 |
| n | 1190 |
| majority_baseline | 71.51% |
| lift | +27.82pp |

### 与 seed42 对比

| | seed123 | seed42 |
|--|---------|--------|
| accuracy | **99.33%** | 98.99% |
| 差异 | +0.34pp | baseline |

seed123 的 accuracy (99.33%) 略高于 seed42 (98.99%)，两者 CI 重叠，无统计显著差异。**Hypothesis 成立**：gradient masking 在不同 seed 下均达到近乎完美的准确率，确认 content quality 解释绝大部分性能，gradient dilution 的影响 ≤5%。

### 文件路径
- checkpoint: `/root/autodl-tmp/trace-verdict-study-checkpoints/gradient_masking_qwen7b_seed123/final`
- log: `/root/runs/trace-verdict-study/gradient_masking_qwen7b_seed123.log`
- eval results: `/root/trace-verdict-study/results/gradient_masking_qwen7b_seed123_eval.json`

注：seed42 的评估结果 JSON 文件不在磁盘上（`gradient_masking_qwen7b_seed42_eval.json` 不存在），seed42 的 98.99% accuracy 来自此前记录。

---
