# check v6 cuda verify

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_v6_cuda_verify_20260512T221619_result.json`
- **Structured JSON:** [`046f7989aab9dcbbf765.json`](../../sessions/04/046f7989aab9dcbbf765.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## v6 ICL 进程状态报告

### 进程信息

| | cuda0 | cuda1 |
|---|---|---|
| **PID** | 631287 | 633173 |
| **GPU** | GPU 0 (10005 MiB, 0% util) | GPU 1 (11489 MiB, 34% util) |
| **num_tasks** | 300 | 300 |
| **seed** | 42 | 42 |
| **part_num/part_idx** | 2/0 | 2/1 |
| **模型** | Qwen3-14B-AWQ | Qwen3-14B-AWQ |
| **进度** | 16/300 (SR 11/16 = 68.8%) | 20/300 (SR 17/20 = 85.0%) |
| **最后日志** | 06:16:41 | 06:15:10 |
| **启动时间** | ~05:55:54 | ~05:55:59 |

### CUDA_VISIBLE_DEVICES 状态：**未设置**

进程环境中 **没有** `CUDA_VISIBLE_DEVICES`。脚本仅通过 `device_map=f"cuda:{gpu}"` (line 213) 将模型放到指定卡上，但进程对全部 6 张 GPU 可见。

**当前无越界**——nvidia-smi 确认 PID 631287 仅在 GPU 0、PID 633173 仅在 GPU 1。但这是软约束（`device_map`），不是硬隔离。`torch.cuda.empty_cache()` (line 551) 等操作理论上可以影响其他卡。

### GPU 全局占用

| GPU | 显存占用 | 利用率 | PID |
|-----|---------|--------|-----|
| 0 | 10005 MiB | 0% | 631287 (v6 ICL) |
| 1 | 11489 MiB | 34% | 633173 (v6 ICL) |
| 2 | 22123 MiB | 38% | 55024 (其他) |
| 3 | 22123 MiB | 37% | 311950 (其他) |
| 4 | 3 MiB | 0% | — |
| 5 | 9311 MiB | 99% | 279220 (其他) |

### 风险评估

**中等风险**。`device_map` 是软绑定，没有 `CUDA_VISIBLE_DEVICES` 硬隔离。若脚本中任何代码路径（如异常处理、GC）触发非指定卡操作，可能重现 D019 越界。建议后续启动时在 tmux 中加 `CUDA_VISIBLE_DEVICES=0` / `CUDA_VISIBLE_DEVICES=1` 前缀。当前进程已在跑，不建议中断。

---
