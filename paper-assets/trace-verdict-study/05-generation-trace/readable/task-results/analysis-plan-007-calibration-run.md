# analysis plan 007 calibration run

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan_007_calibration_run_20260515T122803_result.json`
- **Structured JSON:** [`10d9dc930f8047c464fa.json`](../../sessions/10/10d9dc930f8047c464fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

6 个条件的 calibration 分析全部完成。结果汇总：

| 条件 | Accuracy | ECE | Brier Score |
|------|----------|-----|-------------|
| **ae_only** | 99.92% | **0.0004** | 0.0008 |
| **exception_only** | 99.83% | **0.0024** | 0.0013 |
| **vota** | 99.41% | **0.0054** | 0.0052 |
| **full_trace** | 81.76% | **0.0946** | 0.1438 |
| **label_only** | 86.22% | **0.1108** | 0.1202 |
| **no_trace** | 75.13% | **0.1715** | 0.1972 |

关键发现：
- **ae_only 校准最好**（ECE=0.0004），所有 1190 样本 confidence 都在 [0.95, 1.0] 区间，几乎完美校准
- **exception_only 和 vota** 也极好（ECE < 0.01），高置信度且高准确率
- **full_trace 和 label_only** 中等（ECE ~0.10），存在明显过度自信——高 confidence bin 中准确率低于 confidence
- **no_trace 最差**（ECE=0.1715），模型在高 confidence bin（0.95-1.0）中准确率仅 85.7%，严重过度自信

结果已保存到 `/root/autodl-tmp/trace-verdict-study-checkpoints/calibration/` 目录下各 `{condition}_calibration.json` 文件。

---
