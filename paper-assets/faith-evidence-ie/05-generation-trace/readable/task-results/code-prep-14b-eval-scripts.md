# code prep 14b eval scripts

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep_14b_eval_scripts_20260519T072129_result.json`
- **Structured JSON:** [`457afbfb04982dba3de4.json`](../../sessions/45/457afbfb04982dba3de4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**脚本路径:**
- `/root/autodl-tmp/scripts/14b/eval_14b_sft.sh`
- `/root/autodl-tmp/scripts/14b/eval_14b_sft_no_evidence.sh`

**Dry-run:** 两个脚本参数解析均通过（`--help` 正常退出，无 unrecognized arguments 错误）。

**GPU 状态:**

| GPU | 已用 | 总量 | 可用于 eval |
|-----|------|------|-------------|
| 0 | 29639 MiB | 32607 MiB | 否（被占用） |
| 1 | 0 MiB | 32607 MiB | 是 |
| 2 | 0 MiB | 32607 MiB | 是 |
| 3 | 5415 MiB | 32607 MiB | 否（>2GB，C001） |

cuda:1 和 cuda:2 空闲可用。运行时需按 C002 在脚本前加 `CUDA_VISIBLE_DEVICES=1`（或 2）。

---
