# analysis gradient masking seed456

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gradient_masking_seed456_20260522T161827_result.json`
- **Structured JSON:** [`e7669ef28d3c5ef4b8b0.json`](../../sessions/e7/e7669ef28d3c5ef4b8b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## gradient_masking_qwen7b_seed456 分析结果

**训练状态**: completed (EXIT_CODE=0), 444 steps, 3 epochs, 75min

### Eval Metrics (n=1190)

| 指标 | 值 |
|------|-----|
| accuracy | **99.33%** |
| pass_precision | 1.0000 |
| pass_recall | 0.9906 |
| pass_f1 | 0.9953 |
| fail_precision | 0.9769 |
| fail_recall | 1.0000 |
| fail_f1 | 0.9883 |

### Baseline 对比

| 对比项 | accuracy | diff |
|--------|----------|------|
| exception_only_seed456 | 99.83% | **-0.50pp** |
| gradient_masking seed42 | 98.99% | +0.34pp |
| gradient_masking seed123 | 99.33% | ±0.00pp |

### 3-seed gradient_masking 统计

**mean: 99.22% ± 0.20%** (seeds: 98.99 / 99.33 / 99.33)

vs exception_only baseline 99.83%: **-0.61pp**

### 关键观察
- fail_recall = 1.0（零漏检），pass_precision = 1.0（零误判）
- 主要误差来源是 pass_recall < 1.0，部分 pass 被误判为 fail
- W&B 查询因 entity 未配置失败，指标从 checkpoint 的 eval_results.json 获取

---
