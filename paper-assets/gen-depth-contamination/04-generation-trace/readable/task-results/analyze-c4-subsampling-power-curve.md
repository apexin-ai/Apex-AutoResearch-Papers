# analyze c4 subsampling power curve

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_c4_subsampling_power_curve_20260518T102108_result.json`
- **Structured JSON:** [`e0e6c3ac9f6767e4d69f.json`](../../sessions/e0/e0e6c3ac9f6767e4d69f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

## 结果摘要

| n | Mean AUC | Std | P(AUC > 0.60) |
|---:|---:|---:|---:|
| 1000 | 0.608 | 0.012 | 90% |
| 1500 | 0.612 | 0.011 | 90% |
| 2000 | 0.610 | 0.011 | 80% |
| 2500 | 0.618 | 0.006 | **100%** |
| 3000 | 0.615 | 0.009 | 100% |
| 3500 | 0.623 | 0.005 | 100% |
| 4000 | 0.620 | 0.003 | 100% |
| 4500 | 0.627 | 0.007 | 100% |
| 5000 | 0.629 | 0.000 | 100% |

**结论**: n=1000 即可达 90% 检测概率；n=2500 起 10/10 trials 全部超过 theta=0.60，达到 100% 可靠检测。K\*=2 信号很强，不是大样本量的伪信号。

**产出文件**:
- 服务器: `results/c4_power_curve/{power_curve_results.json, fig_power_curve.pdf, fig_power_curve.png}`
- 本地: `artifacts/c4_power_curve/{results.json, fig_power_curve.png, summary.md}`

---
