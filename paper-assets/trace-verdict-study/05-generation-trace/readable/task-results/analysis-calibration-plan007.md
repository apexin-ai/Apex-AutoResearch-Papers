# analysis calibration plan007

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_calibration_plan007_20260515T122737_result.json`
- **Structured JSON:** [`94d51b2496272ee017ec.json`](../../sessions/94/94d51b2496272ee017ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果汇总：

| Condition | Accuracy | ECE | MCE | Brier |
|-----------|----------|-----|-----|-------|
| No Trace | 0.7513 | 0.1715 | 0.4754 | 0.1972 |
| Full Trace | 0.8176 | 0.0946 | 0.2490 | 0.1438 |
| Exception Only | **0.9983** | **0.0024** | 0.8359* | **0.0013** |
| VOTA | 0.9941 | 0.0054 | 0.6211* | 0.0052 |

\* MCE 高是因为极少样本（1-2个）落在低置信度 bin 导致的离群值，不影响整体 calibration 质量。

**产出文件**（westd-11235 服务器）：
- `calibration_metrics.json`: `/root/autodl-tmp/trace-verdict-study-checkpoints/calibration/calibration_metrics.json`
- `reliability_diagram.pdf`: `/root/autodl-tmp/trace-verdict-study-checkpoints/calibration/reliability_diagram.pdf`
- `reliability_diagram.png`: `/root/autodl-tmp/trace-verdict-study-checkpoints/calibration/reliability_diagram.png`
- 4 个条件的详细 calibration JSON 也在同目录下

两个 artifact 已注册（`art_20260515_f778e0`, `art_20260515_aec352`）。

---
