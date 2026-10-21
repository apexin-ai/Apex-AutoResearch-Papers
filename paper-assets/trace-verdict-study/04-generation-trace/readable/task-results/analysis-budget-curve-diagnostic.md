# analysis budget curve diagnostic

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_budget_curve_diagnostic_20260522T043545_result.json`
- **Structured JSON:** [`55369d9c338acdb61472.json`](../../sessions/55/55369d9c338acdb61472.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心发现：

## 结果

| Condition | Mean Trace (chars) | Diag Ratio | has_traceback | trace_content (fail%) | Accuracy |
|---|---|---|---|---|---|
| tail-256 | 305 | 7.53% | 0% | 55.8% | 78.82% |
| tail-384 | 1296 | 1.76% | 0% | 79.4% | N/A |
| tail-512 | 1593 | 1.43% | 0% | 79.4% | 80.42% |
| tail-1024 | 2492 | 0.92% | 0% | 79.4% | 77.23% |
| full(2048) | 6107 | 0.37% | 0% | 79.4% | 81.76% |
| exc_only | 844 | 4.85% | 79.4% | 79.4% | 99.83% |

## 假设验证

**Phase transition 因果解释不成立。**

1. **has_full_traceback = 0%**（所有 tail-X 条件）：full_trace 格式是 `[Line N] var=...` 逐行变量快照，根本没有 `[ERROR]`、异常类型名等 exception 信息。不管截取多长，都不会出现 traceback。

2. **Accuracy 非单调递增**：tail-256(78.8%) → tail-512(80.4%) → tail-1024(77.2%) → full(81.8%)。1024 反而比 512 低，不存在"刚好包含 traceback 时跳升"的 phase transition。

3. **Diagnostic ratio 递减**：唯一匹配的 "diagnostic" 内容是 `[...trace truncated...]` 和 `[No trace available]` 标记（约22.8 chars/样本），随 trace 变长被稀释，与 accuracy 无正相关。

4. **trace_content 可用性与 accuracy 弱相关**：r=0.290, p=0.635。

## 真正的 phase transition 在哪里

accuracy 的巨大跳变（~80% → 99.8%）发生在 full_trace → exception_only 之间，这不是 truncation length 的连续变化，而是 **trace format 的质变**：从无 diagnostic signal 的执行快照切换到包含 `[ERROR] XxxError` 的结构化异常信息。

产出文件：
- `/root/trace-verdict-study/artifacts/budget_curve_diagnostic/budget_curve_diagnostic.json`
- `/root/trace-verdict-study/artifacts/budget_curve_diagnostic/budget_curve_dual_axis.{pdf,png}`
- `/root/trace-verdict-study/artifacts/budget_curve_diagnostic/budget_curve_stacked.{pdf,png}`
- `/root/trace-verdict-study/artifacts/budget_curve_diagnostic/budget_curve_phase_detail.{pdf,png}`

---
