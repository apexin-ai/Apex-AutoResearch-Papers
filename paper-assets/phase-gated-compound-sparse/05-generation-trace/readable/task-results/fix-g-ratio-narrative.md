# fix g ratio narrative

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_g_ratio_narrative_20260515T091722_result.json`
- **Structured JSON:** [`8c56c2cc4bdccafa59c0.json`](../../sessions/8c/8c56c2cc4bdccafa59c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

远程服务器上不存在 `supplementary_stats.md` 文件，`n500_full_statistics.md` 和 `supplementary_stats.json` 也不包含错误叙事。

本地两份关键文件的状态：

- **`artifacts/n500_analysis/supplementary_stats.md`** 第106行和第130行**已经是修正后的文本**：
  - L106: "Random masking G ranges 0.5–1.3; while statistically significant in 6/8 conditions, the magnitude is trivial (< 1.4×) compared to importance masking (22–148×), indicating that phase asymmetry under random masking is negligible in practical terms."
  - L130: "Random masking G 0.5–1.3, statistically significant in 6/8 conditions but practically negligible (< 1.4×)."
- **`artifacts/_project/report/n500_full_statistics.md`** 和 **`artifacts/n500_analysis/n500_full_statistics.md`** 不包含相关叙事。

旧的错误文本（"most CIs near or overlapping 1, confirming no meaningful phase asymmetry"）仅残留在 `logs/` 目录的聊天记录和 worker 日志中，这些是历史记录不需要修改。

从 worker 日志 `worker_fix_g_ratio_narrative_20260515T091722.log` 的命名看，这个修正已经被之前的 worker 执行过了。**无需额外修改。**

---
