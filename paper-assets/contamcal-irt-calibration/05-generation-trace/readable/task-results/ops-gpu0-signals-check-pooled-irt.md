# ops gpu0 signals check pooled irt

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu0_signals_check_pooled_irt_20260514T215735_result.json`
- **Structured JSON:** [`96bc1f1201c108a4cee8.json`](../../sessions/96/96bc1f1201c108a4cee8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 3 个 pooled IRT 实验完成。汇总：

## 完成状态

| 实验 | 状态 | 结果路径 |
|------|------|---------|
| exp002-signals-1p5B | DONE | `/root/autodl-tmp/exp002/signals/` |
| exp006-pooled-05B-15B-gsm8k-v2 | DONE | `/root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v2` |
| exp006-pooled-05B-15B-arc-v2 | DONE | `/root/autodl-tmp/exp006/results_pooled_05B_15B_arc_v2` |
| exp006-pooled-05B-15B-mmlu-v2 | DONE | `/root/autodl-tmp/exp006/results_pooled_05B_15B_mmlu_v2` |

## IRT 4PL+gamma 结果 (Table 1 数据)

| Benchmark | MAE | ECE | gamma (main) | gamma (joint-fit) |
|-----------|-----|-----|-------------|-------------------|
| **GSM8K** | 0.0364 | 0.0364 | 0.187 CI[-0.92, 1.33] | 0.120 CI[-0.74, 0.96] |
| **ARC** | 0.0347 | 0.0319 | — | -1.464 CI[-2.51, -0.41] |
| **MMLU** | 0.0990 | 0.0990 | — | -0.210 CI[-1.01, 0.59] |

配置：8 models (0.5B×4 + 1.5B×4 dosages)，`--require-signals --joint-fit --exclude-models 3B_d000`。

---
