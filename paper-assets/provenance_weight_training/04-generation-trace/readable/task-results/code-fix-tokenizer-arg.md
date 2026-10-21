# code fix tokenizer arg

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_tokenizer_arg_20260517T111930_result.json`
- **Structured JSON:** [`c3e8f6ae2d6379801779.json`](../../sessions/c3/c3e8f6ae2d6379801779.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：bug 已经被修复了。**

服务器上 `pretrain_weighted.py` 第415行已经使用 `processing_class=tokenizer` 而非废弃的 `tokenizer=tokenizer`。transformers 4.57.6 下 import 正常，dry-run 1 step 训练成功完成，无 TypeError。

4 个实验不再被此 bug 阻塞，可以正常启动。

---
