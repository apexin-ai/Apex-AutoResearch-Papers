# code data format fix

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_data_format_fix_20260514T113420_result.json`
- **Structured JSON:** [`2c741118b31fea95ffb2.json`](../../sessions/2c/2c741118b31fea95ffb2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。总结：

| 任务 | 结果 |
|------|------|
| WNUT-17 → JSONL | train=3394, dev=1009, test=1287 已转换 |
| dataset_info.json | 添加 `conll2003_uie_train` 和 `wnut17_uie_train` |
| data_utils.py | 添加 `load_conll2003()` 和 `load_wnut17()` |
| sampling.py | 添加 `CONLL2003_SCHEMA_HINT` 和 `WNUT17_SCHEMA_HINT` |

数据格式统一为 JSONL，字段结构与 SciERC 一致：`id, text, entities, relations, events`。CoNLL-2003 共 20744 条，WNUT-17 共 5690 条。

---
