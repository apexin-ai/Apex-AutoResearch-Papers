# ssh gpu status check

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gpu_status_check_20260515T040004_result.json`
- **Structured JSON:** [`826fc13a18fcc479a2bd.json`](../../sessions/82/826fc13a18fcc479a2bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇报

### 1. nvidia-smi

```
GPU 0: NVIDIA RTX PRO 6000 Blackwell | 0MiB / 97887MiB | 0% util | 31°C | P8 36W/600W
GPU 1: NVIDIA RTX PRO 6000 Blackwell | 0MiB / 97887MiB | 0% util | 32°C | P8 36W/600W
Driver: 595.58.03 | CUDA: 13.2
No running GPU processes.
```

### 2. GPU 计算进程

无。

### 3. Python 进程

| PID | CPU% | 命令 | 备注 |
|-----|------|------|------|
| 297806 | 4759% | `python3 run_9cell_battery.py` | 启动于 11:57，`CUDA_VISIBLE_DEVICES=""`（纯 CPU），RSS ~950MB |
| 914 | 0.0% | jupyter-lab | 系统服务 |
| 912 | 0.0% | tensorboard (port 6007) | 系统服务 |
| 916 | 0.2% | autopanel serve | 系统服务 |

### 4. tmux sessions

`tmux` 命令被 read-only 白名单拦截，无法执行。

### 5. 磁盘

| 挂载点 | 大小 | 已用 | 可用 | 使用率 |
|--------|------|------|------|--------|
| `/` | 30G | 7.5G | 23G | 25% |
| `/root/autodl-tmp` | 250G | 86G | 165G | 35% |

---
