# check gpu health bjb1 45299

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gpu-health-bjb1-45299_20260525T084700_result.json`
- **Structured JSON:** [`35f9bdb94f243f2d7694.json`](../../sessions/35/35f9bdb94f243f2d7694.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 检查结果

| 实验 | 状态 | 详情 |
|------|------|------|
| **exp_070** (PID 260999) | **已结束** | 日志末行 `EXIT_CODE=0` — 正常跑完。logdir 最后更新 16:48，metrics 停在 16:43。PID 260999 已不存在。 |
| **exp_071** (PID 265628) | **存活** | Step 80000/105000，train_return 209.6。GPU 1 占用 2753MiB, util 22%, 42°C。logdir 最后写入 17:06（1分钟前）。实际 python 进程 PID 265633。 |

**GPU 总览**:
- GPU 0: 1% util, 526MiB — exp_070 结束后仅残留少量显存（265633 的 graphics context）
- GPU 1: 22% util, 2753MiB — exp_071 正在跑

exp_070 已正常完成，exp_071 预计还需跑 25000 步。

---
