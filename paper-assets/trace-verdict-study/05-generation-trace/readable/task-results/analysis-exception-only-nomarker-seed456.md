# analysis exception only nomarker seed456

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exception_only_nomarker_seed456_20260516T194538_result.json`
- **Structured JSON:** [`0a6f38e5ff8e77daaf5e.json`](../../sessions/0a/0a6f38e5ff8e77daaf5e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exception_only_nomarker_seed456 评估结果

### 总体指标

| 指标 | 值 |
|------|-----|
| **Accuracy** | **98.07%** (1167/1190) |
| Wilson 95% CI | [97.12%, 98.71%] |
| n | 1190 |
| Errors | 23 |
| Majority baseline | 71.5% (always "pass") |
| Lift | +26.6pp |

### Per-class Metrics

| Class | Precision | Recall | F1 | Correct |
|-------|-----------|--------|-----|---------|
| **pass** | 0.9836 | 0.9894 | 0.9865 | 842/851 |
| **fail** | 0.9731 | 0.9587 | 0.9658 | 325/339 |

### Error Breakdown (23 errors)

- fail→pass (miss): 14
- pass→fail (false alarm): 9

### Seed Robustness (3 seeds, exception_only_nomarker)

| Seed | Accuracy |
|------|----------|
| 42 | 96.55% |
| 123 | 98.32% |
| **456** | **98.07%** |
| **Mean ± Std** | **97.65% ± 0.96%** |

### 对比：有标记 vs 无标记

| Condition | Mean (3 seeds) | Std |
|-----------|---------------|-----|
| exception_only (有 [ERROR] 标记) | 99.83% | ~0% |
| exception_only_nomarker (无标记) | 97.65% | 0.96% |
| **差异** | **−2.18pp** | |

去掉格式标记后 accuracy 下降约 2.2pp，且 seed 间方差从接近零升至 ~1%。模型对格式标记有一定依赖，但即使无标记仍能达到 97.65% 的平均准确率，说明模型主要依赖内容理解而非表面标记。

---
