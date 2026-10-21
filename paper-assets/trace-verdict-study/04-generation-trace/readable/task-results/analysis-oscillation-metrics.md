# analysis oscillation metrics

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_oscillation_metrics_20260522T073914_result.json`
- **Structured JSON:** [`c7719625b0f7b246384e.json`](../../sessions/c7/c7719625b0f7b246384e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

输出文件已生成。汇总如下：

## 数据来源
训练日志（loss/mean_token_accuracy，每50步记录一次，共44个点）+ 硬编码 registry eval accuracy（每50步 checkpoint，9个点）

## 关键指标

| 指标 | exception_only | full_trace | 比率 |
|------|---------------|------------|------|
| **Loss 滚动方差** (window=5) | 0.0036 | 0.1658 | **46x** |
| **Eval accuracy CV** (全程) | 0.0024 | 0.0222 | **9.4x** |
| **Eval accuracy CV** (后半段) | 0.0000 | 0.0172 | **∞** |
| **末尾3 checkpoint std** | 0.0000 | 0.0135 | — |
| **Max drop** | 0.00pp | **5.29pp** (step 50→100) | — |
| **Recovery time** | N/A (无下降) | **150步** (step 100→250) | — |
| **Accuracy方向变化** | 2/8 | **5/8** | 2.5x |
| **首次稳定** (ε=0.005) | step 200 | **从未达到** | — |

## 推荐论文使用的指标

1. **CV of eval accuracy** — 最直观，full_trace 振荡幅度是 exception_only 的 9.4 倍；后半段 exception_only CV=0 而 full_trace 仍为 0.017
2. **Convergence std (最后 3-5 个 checkpoint)** — 干净地表明 exception_only 已收敛 (std=0) 而 full_trace 未收敛 (std=0.0135)

输出路径：
- `/root/autodl-tmp/trace-verdict-study-checkpoints/oscillation_metrics/oscillation_metrics.json`
- `/root/autodl-tmp/trace-verdict-study-checkpoints/oscillation_metrics/oscillation_summary.txt`

---
