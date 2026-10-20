# ops gpu status monitor

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-status-monitor_20260516T104439_result.json`
- **Structured JSON:** [`712bb7c2d5b48ca8095f.json`](../../sessions/71/712bb7c2d5b48ca8095f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

| 实验 | GPU | 进程状态 | 当前进度 | 预计剩余 | 风险 |
|------|-----|---------|---------|---------|------|
| llama31-taxei-s0 | cuda:1 (26.0/32.6 GB, 99%) | **ALIVE** PID 262833, 运行27min | 685/3387 (20%), ~2.3s/it | **~1h43min** | ⚠️ 高: 交互式终端, SSH断连即死 |
| llama31-random-s0 | cuda:2 (26.0/32.6 GB, 99%) | **ALIVE** PID **257765**, 运行1h29m | 2365/3387 (70%), ~2.25s/it | **~38min** | 低: agent-ml wrapper管理 |
| llama31-vanilla-s0-eval | cuda:3 (16.8/32.6 GB, 88%) | **ALIVE** PID 265940, 运行5min | 15/47 episodes (32%) | **~11min** | 低 |

**重要修正：**

1. **PID 260936 已死**，但 random-s0 实际训练进程是 PID 257765（通过 agent-ml wrapper PID 257429 管理）。训练正常推进，无问题。

2. **vanilla-s0-eval 不在 tmux 中**——是通过 `bash -c` 直接启动的（PID 265938→265940），有 tee 输出到 `eval_results/llama31_vanilla_s0_eval.log`。

3. **cuda:0 完全空闲**（0 MiB, 0%）。

**eval 初步结果**（vanilla-s0, 15/47 done）：10 OK / 5 FAIL，成功率 67%，检测率偏低（大部分 det=-）。

---
