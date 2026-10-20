# ssh gpu check

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gpu_check_20260521T190220_result.json`
- **Structured JSON:** [`64b666ecf34e2b8a4907.json`](../../sessions/64/64b666ecf34e2b8a4907.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 1. GPU 占用

| GPU | 型号 | 显存占用 | 利用率 | 计算进程 |
|-----|------|---------|--------|---------|
| cuda:0 | RTX PRO 6000 Blackwell (96GB) | 0 MiB | 0% | 无 |
| **cuda:1** | RTX PRO 6000 Blackwell (96GB) | **0 MiB** | **100%** | **无** |
| cuda:2 | RTX PRO 6000 Blackwell (96GB) | 0 MiB | 0% | 无 |
| **cuda:3** | RTX PRO 6000 Blackwell (96GB) | **0 MiB** | **100%** | **无** |

**异常：cuda:1 和 cuda:3 显示 100% 利用率，但显存占用为 0 且无任何计算进程。** 这是 phantom GPU utilization——可能是驱动级别的残留状态或硬件异常，没有实际用户进程在用这两块卡。

### 2. 后台任务状态

| 任务 | PID | 状态 | 说明 |
|------|-----|------|------|
| `run_mvp_002.py` | 15291 | **运行中** (seed 12/20) | CPU 459%, 已跑 82 min |
| `bias_scatter.py` | 18203 | **运行中** (seed 1/20) | CPU 568%, 刚启动 |
| `diag_a` | — | **失败** | `nohup: failed to run command 'python3': No such file or directory` |
| `diag_b` | — | **失败** | 同上 |
| `diag_c` | — | **失败** | 同上 |

### 3. 关键问题

**两个运行中的任务都在用 CPU，没用 GPU：**
> "An NVIDIA GPU may be present on this machine, but a CUDA-enabled jaxlib is not installed. Falling back to cpu."

三个 diag 任务全部因 `python3` 路径未找到而失败——nohup 启动时 PATH 中没有 `/root/miniconda3/bin/`。

tmux 状态无法通过 ssh_read_only 查询（命令被白名单拦截）。

---
