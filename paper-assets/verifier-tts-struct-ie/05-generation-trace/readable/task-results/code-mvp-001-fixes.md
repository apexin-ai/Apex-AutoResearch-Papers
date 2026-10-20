# code mvp 001 fixes

**verifier tts struct ie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp-001-fixes_20260511T165952_result.json`
- **Structured JSON:** [`d4099dcff281f751f0a6.json`](../../sessions/d4/d4099dcff281f751f0a6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

### 产出总结

**修复 1: inference.py parse 统计**
- `parse_entities()` 现在返回 `(entities, success_bool)`
- `call_vllm()` 收集每个 candidate 的 parse 结果
- 输出 JSONL 每条记录包含 `"parse_success": true/false`
- 推理完成后打印 `Parse success: X/Y (Z%)`
- 输出目录写入 `parse_stats.json`（含 shard_id, n_candidates, seed, total, success, fail, success_rate）

**修复 2: check_duplicates.py 重复率分析结果**

| 指标 | 值 |
|------|-----|
| 有重复实体的文档 | 66/100 (66.0%) |
| 重复实体总数 | 272/1685 (16.1%) |
| Generic | 77/241 (32.0%) |
| OtherScientificTerm | 84/522 (16.1%) |
| Method | 59/430 (13.7%) |
| Material | 21/158 (13.3%) |
| Task | 26/263 (9.9%) |
| Metric | 5/71 (7.0%) |

**WARNING 已触发**: 重复率 16.1% > 10%，`text.find()` 定位方式对这些重复实体会不准确，应使用 char offset 匹配。

---
