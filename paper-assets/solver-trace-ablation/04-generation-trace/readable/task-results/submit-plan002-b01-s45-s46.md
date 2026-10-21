# submit plan002 b01 s45 s46

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_plan002-b01-s45-s46_20260517T034747_result.json`
- **Structured JSON:** [`bac1bf25e4f593c89fd8.json`](../../sessions/ba/bac1bf25e4f593c89fd8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。两个实验均已启动并确认运行中：

| 实验 | GPU | PID | Registry |
|------|-----|-----|----------|
| plan002-additive-b01-s45 | cuda:0 | 115767 | RUNNING |
| plan002-additive-b01-s46 | cuda:1 | 115914 | RUNNING |

两个 python3 进程均在活跃消耗 CPU（130%+），GPU 尚在模型加载阶段（nvidia-smi 暂未显示显存占用，约 1-2 分钟后会出现）。500 步训练预计 2-3 小时完成。

---
