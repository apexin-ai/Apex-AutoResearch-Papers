# ssh comprehensive gpu status

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_comprehensive-gpu-status_20260520T012703_result.json`
- **Structured JSON:** [`7e37f7654ad88d7bcd92.json`](../../sessions/7e/7e37f7654ad88d7bcd92.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态总览

### GPU 状态

| GPU | Util | VRAM | 状态 |
|-----|------|------|------|
| 0 | 98% | 21253/32607 MiB | 活跃训练 |
| 1 | 100% | **0 MiB** / 32607 MiB | **仍 hung** — 100% 利用率但 0 VRAM，温度 40°C |
| 2 | 82% | 16051/32607 MiB | 活跃训练 |
| 3 | 99% | 31259/32607 MiB | 活跃训练 |

### 训练任务

| 任务 | GPU | PID | 状态 | 进度 |
|------|-----|-----|------|------|
| **Qwen3-8B CWM s123** | 0 或 3 | 881323 | **OOM 崩溃** (EXIT_CODE=1) | v3 日志显示 CUDA OOM，进程 20.75 GiB 时爆显存 |
| **Qwen3-8B CWM s456** | 0 或 3 | 881465 | **OOM 崩溃** (EXIT_CODE=1) | v2 日志显示 CUDA OOM，进程 30.52 GiB 时爆显存 |
| **DeepSeek CWM s123** | 2 | 885624 | **运行中** | step 13/2865 (0.5%), ~1.8s/it, ETA ~1h25m |

### 关键问题

1. **Qwen s123 + s456 双双 OOM**：两个 8B 模型都挤在 `--device cuda:0`（共享同一张卡），互相抢显存导致 OOM。进程虽然在 ps 中仍显示，但日志已报 EXIT_CODE=1，实际已死。GPU 0 和 GPU 3 上残留的 21 GiB / 31 GiB 显存是僵尸进程占用。

2. **GPU 1 仍然 hung**：100% utilization + 0 MiB VRAM 是典型的 GPU 硬件 hang 状态，未恢复。

3. **DeepSeek CWM s123 正常**：刚启动 1 分钟，在 GPU 2 上跑得很稳，16 GiB 显存占用。

### RAM
754 GB total, 51 GB used — 充裕。

### 建议操作
- Qwen 两个 OOM 进程需要 kill 掉释放 GPU 0/3 显存，然后分别指定 `CUDA_VISIBLE_DEVICES=0` 和 `CUDA_VISIBLE_DEVICES=3` 重新启动
- GPU 1 需要 `nvidia-smi -r` 或实例重启才能恢复

---
