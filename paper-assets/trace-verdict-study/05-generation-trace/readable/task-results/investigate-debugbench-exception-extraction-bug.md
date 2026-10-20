# investigate debugbench exception extraction bug

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_debugbench_exception_extraction_bug_20260515T230714_result.json`
- **Structured JSON:** [`5c3a13c333ee40b8984a.json`](../../sessions/5c/5c3a13c333ee40b8984a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 完成总结

### Bug 根因
`debugbench_format_data.py` 的 `compress_exception_only()` 仅从 `trace_raw` 事件中提取 `event=="exception"`，但：
- **625/1006** fail 样本 `trace_raw` 为空（syntax error/multiple error 无法产生 trace）
- **5/1006** fail 样本 trace 达 2000 事件上限，异常在上限之后
- 所有 1006 fail 样本的异常信息都在 `test_results.error` 中，但从未被使用

### 修复（2 处）
1. `compress_exception_only()` (L96): 增加 `test_results` 参数，当 trace 无 exception 事件时 fallback 到 `test_results.error`
2. `format_sample()` (L127-129): 去掉 `if trace_raw` 短路，传入 `test_results`

### 修复效果
| 指标 | 修复前 | 修复后 |
|------|--------|--------|
| Fail 有异常信号 | 376/1006 (37.4%) | **1006/1006 (100%)** |
| Pass 有异常信号 | 0/1042 | 0/1042 (不变) |
| 理论上限 | 69.2% | **100.0%** |
| exception_only empty trace | 1668/2048 | 1042/2048 (仅 pass) |

### 产出
- 修复后的 `debugbench_format_data.py` (服务器)
- 重新格式化的 `debugbench_exception_only_{train,test}.jsonl`
- Bug 分析报告 artifact: `debugbench_exception_bug_analysis.md`
- Registry: `debugbench_exception_bug_fix` (DONE/success)
- memory.md 已更新

---
