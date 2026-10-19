# code pipeline alignment

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_pipeline_alignment_20260521T124913_result.json`
- **Structured JSON:** [`1595ef63c9ad8da46ff8.json`](../../sessions/15/1595ef63c9ad8da46ff8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个文件参数解析均正确，无语法错误。

总结：
1. **`translate_to_zh.py`** — 已经使用 `_verified` 后缀，无需修改
2. **`collect_activations.py`** — 默认文件名改为 EN 读 `_verified`、ZH 读 `_validated`；新增 `--train_file`/`--test_file` 可直接指定路径
3. **`run_mvp.sh`** — 从 3 步扩展为完整 5 步 pipeline（verify → translate → COMET gate → collect activations → train probes）

---
