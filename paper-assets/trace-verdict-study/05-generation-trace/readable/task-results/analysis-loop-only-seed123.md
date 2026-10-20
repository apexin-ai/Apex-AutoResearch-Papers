# analysis loop only seed123

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_loop_only_seed123_20260516T112955_result.json`
- **Structured JSON:** [`5ae21f73c6c937e892ca.json`](../../sessions/5a/5ae21f73c6c937e892ca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## loop_only_seed123 实验结果

**训练状态**: 正常完成 (EXIT_CODE=0)

**Checkpoint 路径**: `/root/autodl-tmp/trace-verdict-study-checkpoints/loop_only_seed123/final`

### 核心指标

| Metric | Value | 95% CI |
|--------|-------|--------|
| **Accuracy** | 85.9% | [84.0%, 87.7%] |
| Majority baseline | 71.5% | — |
| **Lift over baseline** | +14.4pp | [+11.4pp, +17.3pp] |

### Per-class 指标

| Class | Precision | Recall | F1 |
|-------|-----------|--------|----|
| **pass** | 0.913 | 0.887 | **0.900** |
| **fail** | 0.736 | 0.788 | **0.761** |

测试集 n=1190，bootstrap 1000 次重采样。Predictions 保存在同目录 `predictions.jsonl`。

---
