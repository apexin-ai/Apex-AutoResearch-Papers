# code llama3 adapt turn utils

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama3_adapt_turn_utils_20260519T041309_result.json`
- **Structured JSON:** [`d1e9ed3ca65b45237e3b.json`](../../sessions/d1/d1e9ed3ca65b45237e3b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`MODEL_NAME` now only appears in the import and as the default value for `--model`. All runtime uses replaced with `args.model`.

---

**改动摘要：**

| 文件 | 改动 |
|---|---|
| `turn_utils.py` | 新增 `get_turn_markers(tokenizer)` 自动检测 ChatML / Llama-3 格式；`_get_special_token_ids()` 返回 dict（含 `start_id`, `end_id`, `format`, 及 Llama-3 的 `end_header_id`）；role parsing 拆为 `_parse_turns_chatml()` 和 `_parse_turns_llama3()` 两个内部函数；`detect_turn_boundaries()` 和 `build_turn_features()` 使用新的 token info dict，不再硬编码 Qwen tokens |
| `train_phase2.py` | 新增 `--model` CLI 参数（默认 `MODEL_NAME`）；所有运行时 `MODEL_NAME` 引用改为 `args.model` |
| `config.py` | 未改动 — `MODEL_NAME` 保留作为默认值，其他文件仍 import 它 |
| `test_turn_utils.py` | 新建，mock-based 测试覆盖 `get_turn_markers`、`_get_special_token_ids`、`detect_turn_boundaries`（Qwen + Llama-3）、`build_turn_features`（Qwen + Llama-3），共 22 个 test case |

---
