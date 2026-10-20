# analysis deepseek func summary

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_deepseek-func-summary_20260516T120840_result.json`
- **Structured JSON:** [`56a569ef25c2077b6a4b.json`](../../sessions/56/56a569ef25c2077b6a4b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总完成。核心结果：

| 实验 | Seed 42 | Seed 123 | Mean±Std |
|------|---------|----------|----------|
| CLS acc | 86.93 | 86.77 | **86.85±0.11%** |
| CWM acc | 85.77 | 87.88 | **86.83±1.49%** |

**ROADMAP 数字验证通过**：CLS 86.85±0.11%、CWM 86.83±1.49% 均正确。

**Registry 有误**：`deepseek-cls-func-s123` 记录 acc=87.88 是错的，实际为 86.77。87.88 属于 `deepseek-cwm-func-s123`。

其他观察：
- 所有实验 unparseable=0%
- CLS 在 epoch 1 即达 best，CWM 在 epoch 2
- CWM 跨 seed 方差大（std 1.49 vs 0.11），呈现高 precision_pass + 高 recall_fail 的非对称模式

JSON 已写入 `artifacts/deepseek_func_summary.json`。

---
