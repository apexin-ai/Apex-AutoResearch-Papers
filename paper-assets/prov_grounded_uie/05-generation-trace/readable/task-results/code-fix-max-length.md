# code fix max length

**prov grounded uie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-max-length_20260512T200802_result.json`
- **Structured JSON:** [`64c7090b4e8a21aa6a82.json`](../../sessions/64/64c7090b4e8a21aa6a82.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Good — `eval_args` is already in scope where `max_prompt_length` is used. All edits are correct.

**改动摘要：**

| 文件 | 改动 |
|------|------|
| `config.py` | `EvalArgs` 新增 `max_prompt_length=4096` 字段 |
| `evaluate.py` | tokenizer 调用 `max_length=2048` → `eval_args.max_prompt_length`（默认4096）；文件开头加 `PYTHONUNBUFFERED=1` |
| `rerank_nli.py` | tokenizer 调用 `max_length=2048` → `eval_args.max_prompt_length`（默认4096）；文件开头加 `PYTHONUNBUFFERED=1` |

**备注：** `GRPOArgs.max_prompt_length` 仍为 2048（line 70），这是 GRPO 训练的 prompt 长度限制，与本次评估截断修复无关，未改动。

---
