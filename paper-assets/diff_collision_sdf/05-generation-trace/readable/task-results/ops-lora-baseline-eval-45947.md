# ops lora baseline eval 45947

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_lora_baseline_eval_45947_20260526T013633_result.json`
- **Structured JSON:** [`56486e97919f7bcd9a6e.json`](../../sessions/56/56486e97919f7bcd9a6e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Episode 已经在跑了！Seed 0 已经完成了 Episode 10/50。之前 tail -5 没看到是因为输出缓冲。两个 eval 都在正常运行。

## 最终确认

| 项目 | Seed 0 | Seed 1 |
|------|--------|--------|
| PID | 30237 | 30636 |
| GPU | 0 (8399 MiB) | 1 (9018 MiB) |
| 状态 | 正在跑 episodes（已到 10/50） | 正在跑（同样进入 episode 阶段） |
| 报错 | 无 | 无 |

两个 eval 正常运行中。中间修复了：
1. 缺 `peft` 包
2. libero 包需要从 LIBERO/ 做 editable install 才能被 safelibero benchmark 覆盖

---
