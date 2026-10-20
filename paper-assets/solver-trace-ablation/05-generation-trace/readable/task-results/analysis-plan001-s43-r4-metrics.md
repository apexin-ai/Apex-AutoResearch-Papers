# analysis plan001 s43 r4 metrics

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan001-s43-r4-metrics_20260514T031420_result.json`
- **Structured JSON:** [`bfa393ac3e09fb78d413.json`](../../sessions/bf/bfa393ac3e09fb78d413.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完毕。

**plan001-exec-only-s43-r4 指标汇总：**

| 指标 | 值 |
|------|-----|
| total_steps | 500 |
| duration_min | 91.6 |
| overall_prove_rate | 0.66675 |
| first20_prove_rate | 0.0625 |
| last50_prove_rate | 0.9225 |
| last100_prove_rate | 0.8825 |
| parse_rate | 1.0 |
| mean_loss | 0.014022 |
| last100_loss | 0.014724 |

**窗口 prove_rate 趋势：** 0.15 → 0.30 → 0.63 → 0.78 → 0.81 → 0.88

**Conclusion: success**（last100_pr=0.8825 > 0.5）

**GPU 1 状态：** 16329 MiB / 97887 MiB 占用，训练进程已结束（EXIT_CODE=0），残余显存可能是缓存或其他进程。

**注意：** 日志中的 ISR (overall=0.089) 为 binary 近似 (_fast_fn)，需通过 eval_sta.py 统一评估获取真实 ISR。

---
