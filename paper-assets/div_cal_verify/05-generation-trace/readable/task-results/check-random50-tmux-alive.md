# check random50 tmux alive

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_random50_tmux_alive_20260513T170658_result.json`
- **Structured JSON:** [`3cdaf58b5635612a0366.json`](../../sessions/3c/3cdaf58b5635612a0366.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**两个 random_50 实验都在正常运行。**

| 项目 | seed123 | seed456 |
|------|---------|---------|
| tmux session | `random_50_seed123` ✅ | `random_50_seed456` ✅ |
| PID | 248465 (176% CPU) | 248464 (172% CPU) |
| GPU | GPU 0, 12216MiB / 97887MiB, 98% util | GPU 1, 12216MiB / 97887MiB, 98% util |
| 启动时间 | 01:05 | 01:05 |
| 当前阶段 | gen_0（刚开始，目录已创建但还没产出文件） | gen_0（同上） |

**状态：刚启动约 2 分钟，两个实验都在 generation 0 阶段做初始数据生成，GPU 满负荷运行，无错误。** gen_0 目录已创建但尚未写出结果文件，属于正常的初始阶段。

---
