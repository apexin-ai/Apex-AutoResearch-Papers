# analysis plan018 error analysis v2

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan018_error_analysis_v2_20260519T034156_result.json`
- **Structured JSON:** [`0340974f1be54d510335.json`](../../sessions/03/0340974f1be54d510335.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Plan 018 完成。核心发现：

1. **Tier1 (exception/ae/vota) 仅 9 个错误（union）**，全部为 FN，准确率 >99.4%。exception trace 是最关键信号。
2. **FP/FN 模式随 trace 信息量系统变化**：Tier1=纯 FN（保守），Tier2=平衡，Tier3=FN 主导（无 trace 时默认判 fail）。
3. **full_trace_tail 的 FP 问题**：65.6% 错误为 FP，错误样本 input 显著更长（median 2025 vs 425），截断丢失 failure 证据 → 支持"选择性 trace > 完整 trace"。
4. **跨模型一致性**：4 个模型在 exception_only 下共享完全相同的 2 个错误（HumanEval/95），性能上限由数据决定。
5. **48.7% 的 problems 零错误**，难题集中在少数 MBPP problems。

报告已注册为 `error_analysis_v2`。

---
