# hotfix eval reset order bjb2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_hotfix_eval-reset-order-bjb2_20260513T233447_result.json`
- **Structured JSON:** [`79babca712972cddac3c.json`](../../sessions/79/79babca712972cddac3c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**修复完成。总结：**

- **修改**: `evaluate.py:201` — 在 `set_init_state` 前插入 `env.reset()`，顺序为 `reset() → set_init_state() → 5步零动作`
- **旧进程**: PID 115623/115624/115629 已 kill，tmux session 已清理
- **新进程**: PID 117697，运行 3 分 49 秒，CPU 292%，内存 ~9.4GB
- **ValueError**: 日志中出现 0 次，无报错
- **状态**: 已完成环境加载，正在执行第一个 task 的 rollout（每 5 个 rollout 打印一次进度，所以暂无新输出）

---
