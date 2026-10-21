# check restart health

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_restart_health_20260523T032000_result.json`
- **Structured JSON:** [`fc7225807c8b4fadb133.json`](../../sessions/fc/fc7225807c8b4fadb133.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**严重问题：4 个实验中 3 个已崩溃，仅 1 个存活。**

| 实验 | 状态 | 详情 |
|------|------|------|
| `rho03_adaptive_seed456` | **崩溃** | `FileNotFoundError`: checkpoint-1000/trainer_state.json 不存在 |
| `rho03_uniform_seed456` | **运行中** | step 1022/6103 (17%), 已运行 1h10m, PID 833051 |
| `bs8_nmin4_adaptive_seed123` | **崩溃** | `SafetensorError`: incomplete metadata, file not fully covered（checkpoint 损坏） |
| `bs8_nmin4_uniform_seed123` | **崩溃** | `SafetensorError`: 同上，checkpoint 损坏 |

**资源状态：**
- 磁盘：153G/250G (62%)，剩余 98G — 正常
- GPU：仅 GPU 2 在用 (100%, 26GB)，GPU 0/1/3 空闲

**存活实验预估：**
- `rho03_uniform_seed456`：step 1022/6103，从 checkpoint-1000 恢复后仅走了 22 步，速度 ~10.77 it/s，剩余 ~5081 步，预计还需 **~7 分 52 秒**（进度条显示）。但已运行 1h10m，说明大部分时间花在加载 checkpoint 上。

**需要处理：**
1. 3 个崩溃实验的 checkpoint-1000 文件有问题（2 个 safetensors 损坏、1 个缺 trainer_state.json）。需要检查这些 checkpoint 是否可修复，或者从头重跑/从更早的 checkpoint 恢复。
2. 3 张空闲 GPU 可以立即用于重启失败的实验。

是否要我排查 checkpoint 文件状态并重启失败的实验？

---
