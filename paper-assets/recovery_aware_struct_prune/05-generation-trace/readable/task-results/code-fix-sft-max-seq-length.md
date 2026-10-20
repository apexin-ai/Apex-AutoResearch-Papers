# code fix sft max seq length

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_sft_max_seq_length_20260521T181040_result.json`
- **Structured JSON:** [`950c67c74a99a57e5b77.json`](../../sessions/95/950c67c74a99a57e5b77.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。总结：

### 报告

| | westd-29022 | westb-23072 |
|---|---|---|
| TRL 版本 | 1.4.0 | 1.1.0 |
| 修复前 | 已修正（`max_length`） | **有 bug**（`max_seq_length`） |
| 修复后 | 无需改动 | `max_length=args.max_seq_length` ✓ |

**修改内容**：`westb-23072:/root/recovery_aware_struct_prune/src/train_sft_warmup.py` line 94，`max_seq_length=args.max_seq_length` → `max_length=args.max_seq_length`

**验证**：两台服务器 SFTConfig 实例化均通过（`SFTConfig OK, max_length=2048`）。

**`sft_recovery.py`**：两台服务器均已正确使用 `max_length`，无需修改。

**`run_alpha4_pipeline.sh`**：调用 `train_sft_warmup.py` 的 CLI 参数 `--max_seq_length` 未被传入（使用默认值 2048），不受此 bug 影响——但修复后即使显式传入也不会报错了。

---
