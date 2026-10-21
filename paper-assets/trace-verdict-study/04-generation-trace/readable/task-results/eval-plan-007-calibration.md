# eval plan 007 calibration

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_plan_007_calibration_20260515T121655_result.json`
- **Structured JSON:** [`e40df5bff7263fe386e5.json`](../../sessions/e4/e40df5bff7263fe386e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总结果：

## Calibration Analysis 汇总（5 条件 × 1190 测试样本）

| Condition | Accuracy | ECE ↓ | Brier ↓ |
|-----------|----------|-------|---------|
| **exception_only** | 99.83% | **0.0024** | **0.0013** |
| **VOTA** | 99.41% | 0.0054 | 0.0052 |
| **loop_only** | 85.63% | 0.0833 | 0.1183 |
| **full_trace** | 81.76% | 0.0946 | 0.1438 |
| **no_trace** | 75.13% | 0.1715 | 0.1972 |

关键发现：
- **exception_only** 和 **VOTA** calibration 极优（ECE < 0.01），模型置信度与实际准确率高度一致
- **no_trace** calibration 最差（ECE=0.17），模型过度自信
- **loop_only** 和 **full_trace** 处于中间水平
- Calibration 排序与 accuracy 排序一致：trace 信息越丰富，模型越"知道自己知道什么"

JSON 结果保存在 `/root/autodl-tmp/trace-verdict-study-checkpoints/calibration/` 下，每个条件一个文件。

---
