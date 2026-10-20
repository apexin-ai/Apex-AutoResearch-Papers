# eval a continued merge and eval

**schema conform ie training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_a_continued_merge_and_eval_20260513T205249_result.json`
- **Structured JSON:** [`d7ec1d0c860ba9e1eb20.json`](../../sessions/d7/d7ec1d0c860ba9e1eb20.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。

## 报告

| 项目 | 状态 |
|------|------|
| **1. 训练完成** | 500/500 步完成，无错误，耗时 3h08m |
| **2. Auto-merge** | 成功 → `formal_A_continued/merged/` (17.9GB model.safetensors) |
| **3. Checkpoint-400 merge** | 手动 merge 完成 → `formal_A_continued/checkpoint-400-merged/` (17.9GB) |
| **4. Eval tmux session** | `eval_a_cont` 已启动，模型加载到 cuda:0 (17639 MiB) |
| **5. 日志** | `eval_A_continued_ckpt400.log` 正常，模型加载完成 |

两个 eval 串行在 cuda:0 上运行：ckpt400 (900 effective steps) → final (1000 effective steps)。eval_B_v3 仍在 cuda:1 上并行运行。

---
