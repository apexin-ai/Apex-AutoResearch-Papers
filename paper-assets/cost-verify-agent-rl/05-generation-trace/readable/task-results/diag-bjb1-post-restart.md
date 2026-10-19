# diag bjb1 post restart

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_bjb1-post-restart_20260519T124528_result.json`
- **Structured JSON:** [`e49890f8f4b49db1495f.json`](../../sessions/e4/e49890f8f4b49db1495f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 服务器状态报告

### 1. Per-task-type eval 进程 — **存活，正在运行**

- tmux 会话 `exp029_per_task_breakdown` 存在
- `python eval_per_task_type.py` (PID 166489) 正在运行，CPU 25.3%
- `VLLM::EngineCore` (PID 166766) 正在运行，CPU 86.7%
- 进度：**67/134 tasks 已完成**（重启后从头重新开始了，不是从 30 续跑）
  - OK: 16 | FAIL: 51 | 成功率: 23.9% (16/67)
- 模型：`/root/autodl-tmp/checkpoints/exp029_hf`，vLLM v0.18.1，bf16，max_seq_len=20480
- 启动时间：20:26（约 19 分钟前），预计还需 ~20 分钟完成剩余 67 tasks

### 2. GPU 状态

| GPU | 利用率 | 显存占用 |
|-----|--------|----------|
| cuda:0 | 47% | 39,605 / 97,887 MiB |
| cuda:1 | 0% | 3 / 97,887 MiB |

仅 GPU 0 在用（tensor_parallel_size=1）。

### 3. exp029 checkpoint — **存在**

- `/root/autodl-tmp/checkpoints/exp029/global_step_15/actor/` — 存在
- `/root/autodl-tmp/checkpoints/exp029_hf` — eval 正在使用的 HF 格式 checkpoint

### 4. 磁盘状态

| 分区 | 大小 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| / (根) | 30G | 14G | 17G | 47% |
| /usr/bin/nvidia-smi (数据盘) | 879G | 18G | 817G | 3% |

磁盘充裕，无风险。

### 总结

eval 进程在服务器重启后被重新启动（今天 20:26），已完成 67/134，正在正常推进。当前成功率 23.9%（之前 30 tasks 时是 33.3%，随着更多 hard tasks 进入有所下降）。无需干预，等待完成即可。

---
