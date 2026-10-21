# prep no evi test eval commands

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_no_evi_test_eval_commands_20260521T225528_result.json`
- **Structured JSON:** [`133316ade48617f6c4b2.json`](../../sessions/13/133316ade48617f6c4b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

命令已写入 `artifacts/no_evi_test_commands.md`。

关键点：
- `--base_model` 必须显式指定（默认是 Qwen3-4B，不适用于 14B/1.7B）
- 提交时把 `CUDA_VISIBLE_DEVICES=X` 的 X 替换为空闲 GPU 编号
- 提交前先 `nvidia-smi` 确认目标 GPU 显存 < 2GB（C001）

---
