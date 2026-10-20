# fix oracle doc trace source

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_oracle-doc-trace-source_20260517T171013_result.json`
- **Structured JSON:** [`0e30e6895602114eb5f1.json`](../../sessions/0e/0e30e6895602114eb5f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个修复完成，汇总：

### 修复 1: 设计文档 trace 来源
- `results/exp020_folio_200/exp020_results.json` → `results/sica_expanded_14b.json`
- 明确标注 "Qwen2.5-14B-Instruct traces from exp-001, FOLIO subset"
- 三方对比表的 Source 列同步更新为 `exp-001 (sica_expanded_14b)`
- SC=79.41% 与 sica_expanded_14b folio_sc=0.7941 一致 ✓

### 修复 2: 答案解析 LaTeX 残留
- **受影响问题**: `folio_141`（非 folio_142），traces 4 和 8 的 answer 为 `\text{True}`
- **Bug 机制**: `check_consistency_for_answer` 的 else 分支返回 -1，maxsat 给 0.5 权重，导致 `\text{True}` 以 1.0 总权重赢过 "Unknown"(权重 0.0)
- **修复**: 在 `run_exp021_oracle_folio.py` 添加 `normalize_answer()` 函数，用 `re.sub` 清理 `\text{...}` 包装
- **重跑结果**: solver_errors 从 2 → 0，folio_141 的 oracle_answer 从 `\text{True}` → `Unknown`
- **Accuracy 不变**: 仍为 **180/204 = 88.24%**。原因：folio_141 的 gold 是 "False"，修复后 oracle 答 "Unknown" 仍是错的，不产生 +1

---
