# code fix fallback fields

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-fallback-fields_20260515T141820_result.json`
- **Structured JSON:** [`cac335f99fe08c1026ad.json`](../../sessions/ca/cac335f99fe08c1026ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两处修复完成，验证全部通过。

### 修复总结

**pipeline.py** (L139-169) — except 分支的 `result` dict 从只有 `error`+`domain` 扩展为包含所有正常路径的 key：
- 新增 `answer`(空串)、`scores`({})、`answer_counts`({})、`traces`([])
- 新增 `constraints_stats`（三个字段全部为 0）
- 新增 `maxsat_stats`（四个字段：satisfied/excluded/total_weight/solve_time_ms 全部为 0）
- 有 `cached_traces` 时仍覆盖 answer/answer_counts/traces

**run_full_mvp.py** (L112-114) — `compute_summary` 中三行直接下标访问改为 `.get()` 链式安全访问：
- `r["constraints_stats"]["total_extracted"]` → `r.get("constraints_stats", {}).get("total_extracted", 0)`
- `r["maxsat_stats"]["excluded"]` → 同上
- `r["constraints_stats"]["unique_after_dedup"]` → 同上

### 验证结果
- 两个文件 import 无语法错误 ✓
- fallback result 包含所有 required keys ✓
- compute_summary 对空 dict / 完全缺失字段 / 正常+fallback 混合数据均正确计算 ✓

---
