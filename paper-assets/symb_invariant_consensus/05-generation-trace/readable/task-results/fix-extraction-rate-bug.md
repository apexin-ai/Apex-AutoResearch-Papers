# fix extraction rate bug

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_extraction-rate-bug_20260517T132009_result.json`
- **Structured JSON:** [`5dc1f638ed66222a69fc.json`](../../sessions/5d/5dc1f638ed66222a69fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。

## 结果

**Bug 原因**: `avg_extraction_rate = Mean(traces_with_constraints / n_traces)` 的分母 `n_traces` 错误地使用了 `boxed + fallback`（成功提取 answer 的 trace 数），而非 `k=12`（总 trace 数）。当 trace 的 answer 提取失败但 constraint 提取成功时，分子 > 分母。

**修复前后对比**:

| Experiment | OLD | NEW |
|---|---|---|
| exp011_llama8b_pw_folio | **1.1018** | 0.9639 |
| exp020_llama8b_folio | **1.0591** | 0.9935 |
| exp019_llama8b_strategyqa | 0.9390 | 0.8008 |

所有实验的 extraction_rate 现在 <= 1.0。

**副作用**: 修正后 c0 与 extraction_rate 的 Pearson 相关从 r=0.675 降至 r=0.116，原来的高相关部分是 bug 造成的伪信号。

**文件变更**:
- `results/exp019_constraint_quality_analysis.json` — 重新生成
- `results/exp019_constraint_quality_summary.csv` — 重新生成
- `scripts/compute_constraint_quality_correlation.py` — 新增可重复运行的分析脚本
- `artifacts/extraction_rate_bugfix.md` — 修复记录

---
