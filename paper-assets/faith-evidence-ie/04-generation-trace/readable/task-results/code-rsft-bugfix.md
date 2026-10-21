# code rsft bugfix

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_rsft-bugfix_20260515T010036_result.json`
- **Structured JSON:** [`95676417980e1107813f.json`](../../sessions/95/95676417980e1107813f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证结果：

1. **Bug 1** — `rsft_generate.py:210`: `--quantize` default 已改为 `False`
2. **Bug 2** — `rsft_score_filter.py:437-448`: 输出改为 JSONL (`rsft_train.jsonl`)，每行含 `input`/`output`/`ced_score` 字段，与 `rsft_trainer.py:62-78` 的 `load_rsft_data` 完全匹配（读 JSONL，取 `s["input"]`、`s["output"]`、`s.get("ced_score", 1.0)`）
3. **Bug 3** — NLI 模型路径逻辑正确，无需修改
4. `rsft_trainer.py` 无需改动

---
