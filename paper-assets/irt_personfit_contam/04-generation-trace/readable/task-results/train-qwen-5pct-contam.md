# train qwen 5pct contam

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_qwen-5pct-contam_20260522T091954_result.json`
- **Structured JSON:** [`8c24c0561290fc921208.json`](../../sessions/8c/8c24c0561290fc921208.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。以下是完整结果汇总：

---

## exp-ctrl-contam-qwen-5pct 结果

**磁盘**: 165GB 可用，充裕

**数据**: `train.jsonl` = 5702 行（5000 Alpaca + 702 MMLU 5%），已复用之前生成的数据

**训练**: 已完成（之前的运行），3 epochs, 1071 steps, train_loss=1.39, 耗时 ~19 分钟

**评估结果**:

| 指标 | 值 |
|------|-----|
| θ_MLE (free) | +0.0879 |
| lz* (free-θ) | 5.6309 |
| lz* (fixed-θ, θ=-0.1022) | 11.0900 |
| accuracy_overall | 0.7141 |
| accuracy_seen (702 items) | 0.8291 |
| accuracy_unseen (13340 items) | 0.7080 |

**Cohen's d**:

| 方法 | d | 95% CI |
|------|---|--------|
| Free-θ | **-4.15** | [-9.85, -2.74] |
| Fixed-θ | **+3.52** | [+2.90, +5.71] |

**跨条件对比** (fixed-θ Cohen's d):

| 条件 | d (fixed-θ) |
|------|-------------|
| 5% (702 items) | +3.52 |
| 15% (2106 items) | +4.77 |
| 50% (7021 items) | +14.52 |

5% 污染的 fixed-θ Cohen's d = 3.52，效应量依然很大（远超常规阈值 0.8），表明即使 5% 的 MMLU 污染也能被 lz* person-fit 统计量检测到。

---
