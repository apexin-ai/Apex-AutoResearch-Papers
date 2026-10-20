# analysis cross model comparison 20260515

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cross_model_comparison_20260515_20260515T155523_result.json`
- **Structured JSON:** [`52459638601ae36b71de.json`](../../sessions/52/52459638601ae36b71de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文档已生成并注册 (`art_20260515_be691e`)。

**核心结论：**

1. **exception_only 是 primary claim** — 两个模型 peak accuracy 完全一致 (99.83%)，per-class 指标精确到小数点后三位相同
2. **VOTA 应降级为 secondary result** — Qwen 99.41% vs DeepSeek 84.45%，gap 14.96pp，根因是 DeepSeek fail_recall 仅 45.4%
3. **Baseline 一致** — no_trace 差异仅 1.77pp，CI 重叠
4. **DeepSeek exception_only 轻微过拟合** — epoch1→epoch3 退化 0.50pp，early stopping 可恢复

产出文件：`artifacts/cross_model_analysis/cross_model_comparison.md`

---
