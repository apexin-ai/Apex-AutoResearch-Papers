# code remove s3 from rrf

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_remove-s3-from-rrf_20260516T023317_result.json`
- **Structured JSON:** [`8ea4e401a2d9c6197524.json`](../../sessions/8e/8ea4e401a2d9c6197524.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。输出确认只包含 3 个信号列：`s1_embedding`、`s2_minkpp`、`s4_selfcritique`，无 s3/constat 引用。

修改汇总（4 处）：
- **docstring** (L11): CSV columns 描述移除 `s3_constat`
- **SIGNAL_KEYS** (L26): `["s1_embedding", "s2_minkpp", "s4_selfcritique"]`
- **SIGNAL_NAMES** (L30): 移除 `"s3_constat": "ConStat"` 条目
- **sig_name_map** (L75): 移除 `"s3_constat": "constat"` 条目

备份在 `rrf_aggregation.py.bak2`。

---
