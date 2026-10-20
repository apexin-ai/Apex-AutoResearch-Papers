# ops check eval and grpo speed

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_eval_and_grpo_speed_20260516T124409_result.json`
- **Structured JSON:** [`3a38fb0f0ee9cb20c23a.json`](../../sessions/3a/3a38fb0f0ee9cb20c23a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 1. Eval 已完成

| Model | Accuracy | Correct/Total | EOS Rate |
|-------|----------|---------------|----------|
| **RASP 25%** | **64.0%** | 128/200 | 99.5% |
| **Standard 25%** | **63.0%** | 126/200 | 100% |

两个 eval 文件分别在 20:20 和 20:16 写入完毕。EOS 问题已修复（Standard 100%, RASP 99.5%）。

### 2. GRPO 仍在初始化，无法测步速

两个 GRPO 进程都活着（PID 9291 RASP, PID 9375 Standard），但日志显示仍在加载模型/准备数据阶段：

- **RASP log** (4行)：最后一行 `20:44:35 Preparing GSM8K training dataset...`
- **Standard log** (2行)：最后一行 `20:43:11 Non-uniform MLP detected`

尚未产出任何训练 step，无法测量步速。

### 3. GPU 状态异常

```
GPU 0:   0% util,   3 MiB / 97887 MiB   ← RASP GRPO 分配但未加载到显存
GPU 1: 100% util,   3 MiB / 97887 MiB   ← Standard GRPO，100% util 但 3 MiB 显存很奇怪
GPU 2:   0% util,   0 MiB / 97887 MiB   ← 空闲
GPU 3:   0% util,   0 MiB / 97887 MiB   ← 空闲
```

GPU 1 显示 100% utilization 但只有 3 MiB 显存，可能是初始化 CUDA context 的开销。模型尚未加载到 GPU。

**建议**：等 3-5 分钟后再查一次日志，确认模型是否成功加载到 GPU 并开始出 step。如果 5 分钟后日志仍无训练输出，需要排查是否卡住。

---
