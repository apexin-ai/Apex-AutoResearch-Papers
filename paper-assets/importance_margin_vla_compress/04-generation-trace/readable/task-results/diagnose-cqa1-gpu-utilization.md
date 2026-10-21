# diagnose cqa1 gpu utilization

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_cqa1_gpu_utilization_20260519T042838_result.json`
- **Structured JSON:** [`31b34a50299349447724.json`](../../sessions/31/31b34a50299349447724.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

| GPU | 实验 | Step/Total | Loss | Speed | GPU-Util | 显存 |
|-----|------|-----------|------|-------|----------|------|
| 0 | m32_seed44 | 49250/100K (49.3%) | 0.094 | 4.2 sps | 0%* | 2869/24564 MiB |
| 1 | m64_seed44 | 49250/100K (49.3%) | 0.081 | 4.2 sps | 17% | 2787/24564 MiB |
| 2 | m96_seed44 | 51500/100K (51.5%) | 0.048 | 4.4 sps | 35% | 2787/24564 MiB |
| 3 | m32_official | 33050/100K (33.1%) | 0.114 | 4.1 sps | 39% | 3197/24564 MiB |

**IO 状态**：iowait = 0.0%，无 IO 瓶颈。CPU 利用率 14.1% us，空闲 84.8%。

**注意事项**：
- GPU 0 的 `nvidia-smi` 瞬时 Util 显示 0%，但进程正常运行（PID 737451，CPU 占用 79.9%），log 持续更新，这是 `nvidia-smi` 采样瞬间恰好在 CPU 侧做数据准备，属正常波动。
- m32_seed44 / m64_seed44 进度基本同步（~49.2K），m96_seed44 稍快（51.5K），m32_official 晚启动约 1 小时（10:13 vs 09:12），当前 33K。
- 每个训练都启动了 4 个 dataloader worker 子进程（CPU 占用 ~97% 每个），数据加载充分。
- 按当前速度估算：m32/m64_seed44 剩余约 3.4 小时，m96_seed44 约 3.1 小时，m32_official 约 4.5 小时完成。

---
