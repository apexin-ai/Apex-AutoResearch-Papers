# analysis qwen15b full trace tail1024 seed42

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen15b_full_trace_tail1024_seed42_20260517T231433_result.json`
- **Structured JSON:** [`94124c6a143db68ccfb9.json`](../../sessions/94/94124c6a143db68ccfb9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结论：

**Hypothesis REJECTED** — tail-1024 (96.6%) 比 tail-512 (95.6%) 高 +1.0pp，1.5B 模型上不存在 non-monotonicity。

关键发现：
1. 1.5B 上下文长度呈单调递增：tail-256 (72.6%) → tail-512 (95.6%) → tail-1024 (96.6%)
2. 1.5B tail-1024 (96.6%) ≈ 7B tail-1024 (96.47%)，说明在充足上下文下模型规模无额外收益
3. CIs 重叠（[95.5%, 97.6%] vs [94.5%, 96.8%]），差异不显著，但方向明确为单调提升

报告已写入 `artifacts/qwen15b_full_trace_tail1024_seed42/report/analysis.md`。

---
