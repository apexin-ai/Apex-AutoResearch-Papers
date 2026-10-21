# check bjb1 exp089 090

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_bjb1_exp089_090_20260525T220822_result.json`
- **Structured JSON:** [`30224ca00c24d5f0f08d.json`](../../sessions/30/30224ca00c24d5f0f08d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**exp_089 和 exp_090 均启动失败**，没有进行任何训练。

**失败原因**：启动命令使用了 `--dt_embed_dim 0`（不存在的参数），正确参数名是 `--gate_dt_embed_dim 0`。两个实验都在 argparse 阶段 EXIT_CODE=2 退出。

**服务器状态**：bjb1-45299 两块 GPU 当前空闲（无计算进程）。

**需要操作**：
1. 用修正后的命令（`--gate_dt_embed_dim 0` 替代 `--dt_embed_dim 0`）重新启动两个实验
2. exp_089 → cuda:0, seed=1；exp_090 → cuda:1, seed=2

是否现在重新启动？

---
