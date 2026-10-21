# train plan001 exec only s44

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_plan001-exec-only-s44_20260514T022911_result.json`
- **Structured JSON:** [`5414e00c8b64fd75f226.json`](../../sessions/54/5414e00c8b64fd75f226.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

cuda:0 上有一个**活跃训练任务**（不是僵尸进程）：

- **PID 161819**: `plan002_additive_beta03_s42`，运行 3 分 37 秒，使用 `configs/grpo_additive_bonus.yaml`
- 占用 ~80GB 显存，GPU 利用率 91%

这是一个正在运行的 plan002 实验，不是僵尸进程。杀掉它会丢失训练进度。

**cuda:0 当前不可用。** 需要你决定：
1. **等 plan002 跑完**再提交 s44（plan002 500 steps 大概需要几小时）
2. **杀掉 plan002** 优先跑 plan001-s44（会丢失 plan002 进度）

怎么处理？

---
