# eval kill and resubmit seed123 8b val 8192

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_kill-and-resubmit-seed123-8b-val-8192_20260514T211013_result.json`
- **Structured JSON:** [`166d95c4aac12cc77fc4.json`](../../sessions/16/166d95c4aac12cc77fc4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成：

- **旧实验** `cls8b-seed123-ckpt3000-val-eval`：已 kill，registry 标记 conclusion=killed，notes 说明原因
- **新实验** `cls8b-seed123-ckpt3000-val8192-eval`：已在 cuda:1 上运行（17891 MiB），推理已开始
  - 修复：添加 `--max_seq_length 8192` + `--batch_size 1`（原 batch_size=16 在 8192 seq_len 下 OOM）
  - Registry 状态 RUNNING，hypothesis/parent/spec 已更新

---
