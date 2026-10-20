# code sync eval runner fix

**distill kv rag cache** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_sync-eval-runner-fix_20260514T074543_result.json`
- **Structured JSON:** [`1388867c5d4adee4c8b7.json`](../../sessions/13/1388867c5d4adee4c8b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

同步完成，共两处修改：

1. **Prompt 构建重写**（原 172-183 行）：raw text 拼接 `"Context: ...\n\nQuestion: ...\nAnswer:"` → 用 `apply_chat_template` 构建 system+user 消息，按 `"Question:"` 切分 context/query；`max_length` 从 2048 → 4096；context tokenization 加了 `add_special_tokens=False`。

2. **新增 debug 打印**（原 206 行后）：前 5 个样本打印 `pred`、`gold`、`em`、`f1`，方便快速检查模型输出是否合理。

---
