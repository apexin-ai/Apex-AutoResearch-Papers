# code eval humaneval grpo rasp 20 2048 submit

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval_humaneval_grpo_rasp_20_2048_submit_20260517T135658_result.json`
- **Structured JSON:** [`cc5d6dd2c99dd9ed4678.json`](../../sessions/cc/cc5d6dd2c99dd9ed4678.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

旧 tmux session 已清理（或本身不存在）。

但 **cuda:0 当前不空闲**，4 张 GPU 全部被占用：

| GPU | 显存占用 | GPU 利用率 | 进程 |
|-----|---------|-----------|------|
| cuda:0 | 13,551 / 97,887 MiB | 98% | python (PID 28136) |
| cuda:1 | 31,527 / 97,887 MiB | 99% | python (PID 14556) |
| cuda:2 | 16,521 / 97,887 MiB | 98% | python (PID 27199) |
| cuda:3 | 31,527 / 97,887 MiB | 99% | python (PID 11896) |

所有 GPU 都在高负载运行，不适合强行提交。需要等当前任务完成或手动终止某个进程后再启动 HumanEval eval。

---
