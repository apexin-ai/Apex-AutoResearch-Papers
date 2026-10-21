# analysis temperature pilot summary

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_temperature-pilot-summary_20260523T142853_result.json`
- **Structured JSON:** [`e3ae2b6d3e88f95bd833.json`](../../sessions/e3/e3ae2b6d3e88f95bd833.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。从 216 个 checkpoint 聚合的结果：

| 指标 | MMLU | ARC |
|------|------|-----|
| K_eff Δ (max-min) | 0.0332 | 0.0270 |
| K_eff range | 2.564–2.598 | 2.684–2.711 |
| K_eff t=0→t=1 change | +0.008 | −0.014 |

- **216/216 checkpoint 全部加载**，0 失败
- Accuracy 最大变化 0.85pp，instrument_clean = true
- 温度对 K_eff 的影响极小（Δ < 0.034），确认温度不是有效 instrument
- ASR 在各温度下无系统趋势
- 输出已写入 `docs/paper/data/temperature_pilot_summary.json`

---
