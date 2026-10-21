# code fix stat analysis 3bugs

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-stat-analysis-3bugs_20260515T173636_result.json`
- **Structured JSON:** [`00e5556f2585822d4025.json`](../../sessions/00/00e5556f2585822d4025.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个 bug 全部修复并验证通过：

**Bug 1 — norm parsing**: `parse_norm_from_id` 现在先用 `split("-")` 提取 norm 部分，再用 `"0." + suffix[1:]` 解析。`norm003`→0.03, `norm005`→0.05, `norm0p3`→0.3 全部正确。

**Bug 2 — SR 归一化**: 新增 `normalize_sr()` 函数，统一处理 0-100 整数、0-1 浮点、百分比字符串三种格式。已应用到 `extract_overall_sr`、`extract_partial_sr`、`merge_partial_results` 中所有读取 SR 的位置。同时扩展了 `extract_overall_sr` 的字段名列表（增加 `overall_SR`、`avg_SR_10task`、`overall_sr_10task`）。

**Bug 3 — 硬编码数据**: 删除了 `__main__` 中的 6 组硬编码 dict，替换为 argparse CLI，从 `--comparison-json`（stat_analysis.py 输出）动态读取数据。

---
