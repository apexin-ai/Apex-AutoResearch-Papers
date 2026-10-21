# paper trace length ablation narrative

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_trace_length_ablation_narrative_20260516T022748_result.json`
- **Structured JSON:** [`c7efc063ee35e9c9eac2.json`](../../sessions/c7/c7efc063ee35e9c9eac2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

5 个 `\begin{table}` 和 5 个 `\end{table}` 匹配。

已完成。新增 `\subsection{Trace Length Ablation}`（§5.5，位于 Information Density Decomposition 和 Calibration Analysis 之间），包含：

- **Table 5** (`tab:trace_length`)：4 个 token budget 的精度和 CI，加 exception_only 和 no_trace 参照
- **叙事**：所有 full_trace 变体聚集在 77–82% 窄带内；非单调性（1024 < 512）排除 truncation 作为瓶颈；no_limit 仍留 18.07pp gap 到 exception_only；结论是 signal quality 问题而非 signal quantity 问题；反向引用 §5.3 的 information overload 机制

---
