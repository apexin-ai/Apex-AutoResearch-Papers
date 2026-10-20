# ops harvest tail 256 1024 and plot

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_harvest_tail_256_1024_and_plot_20260517T102823_result.json`
- **Structured JSON:** [`a17a4b42cee512e9e031.json`](../../sessions/a1/a17a4b42cee512e9e031.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总：

## 实验结果

| Condition | Accuracy | Pass F1 | Fail F1 | 95% CI (Acc) |
|-----------|----------|---------|---------|--------------|
| **tail-256** | 77.48% | 83.33% | 65.28% | [74.96%, 79.75%] |
| **tail-1024** | 96.47% | 97.53% | 93.81% | [95.46%, 97.48%] |

## Budget Curve 关键发现

- **Tail truncation 远优于 Head truncation**：tail-1024 (96.47%) vs head-1024 (77.23%)，差距近 20pp
- Tail truncation 从 256→512 有巨大跳跃 (77.48%→93.61%)，之后边际递减
- Head truncation 在所有 budget 下都只比 no-trace baseline (75.13%) 略高，说明 trace 头部信息量极低

## 产出

- 图表：`/root/trace-verdict-study/docs/paper/figures/budget_curve.pdf` + `.png`

---
