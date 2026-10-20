# eval restart cls westd gpu23

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_restart-cls-westd-gpu23_20260514T014747_result.json`
- **Structured JSON:** [`d8d8ba8008b5b4c9379f.json`](../../sessions/d8/d8d8ba8008b5b4c9379f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

指定的 checkpoint 目录不存在，无法启动 eval。具体情况:

**不存在的路径:**
- `checkpoints_repo_cls_v5_conda/` — 不存在
- `checkpoints_repo_cls_8b_conda/` — 不存在
- 整个服务器没有任何 `checkpoint-200`
- `checkpoints_repo_cls/` 和 `checkpoints_repo_cls_seed123/` 是空目录

**可用的 CLS checkpoint:**

| 目录 | Base model | 子目录 |
|------|-----------|--------|
| `checkpoints/best/` | Qwen/Qwen3-4B | best |
| `checkpoints_cls_seed0/best/` | Qwen/Qwen3-4B | best, checkpoint-956, checkpoint-1434 |
| `checkpoints_cls8b/best/` | Qwen/Qwen3-8B | best, checkpoint-478, checkpoint-1434 |
| `checkpoints_cls8b_seed123/best/` | (likely Qwen3-8B) | best, checkpoint-956, checkpoint-1434 |

**测试数据:** `data/swebench_full/swebench_test.jsonl`（不是 `test.jsonl`）

看起来 repo-level CLS 的训练 checkpoint 要么从未生成，要么已被删除。你想用上面哪些 checkpoint 来跑 eval，还是需要先重新训练？

---
