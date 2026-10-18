# gpu status scan all servers

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu-status-scan-all-servers_20260524T005448_result.json`
- **Structured JSON:** [`3120702e477d6df544ce.json`](../../sessions/31/3120702e477d6df544ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

tmux 不在 read-only 白名单中，跳过。已有完整 GPU 数据，汇总如下：

## 14 GPU 实际状态表

| 服务器 | GPU | 显存 (已用/总计) | GPU利用率 | PID | 状态 |
|--------|-----|-----------------|-----------|-----|------|
| **cqa1-33015** (4× RTX 4090) | GPU 0 | 10314 / 24564 MiB | 37% | 459609 | **占用** |
| | GPU 1 | 10321 / 24564 MiB | 22% | 541798 | **占用** |
| | GPU 2 | 10261 / 24564 MiB | 9% | 467663 | **占用** |
| | GPU 3 | 1 / 24564 MiB | 0% | — | **空闲** |
| **westd-41074** (4× H800) | GPU 0 | 0 / 97887 MiB | 0% | — | **空闲** |
| | GPU 1 | 0 / 97887 MiB | 0% | — | **空闲** |
| | GPU 2 | 0 / 97887 MiB | 0% | — | **空闲** |
| | GPU 3 | 0 / 97887 MiB | 0% | — | **空闲** |
| **westd-38929** (4× H800) | GPU 0 | 1 / 97887 MiB | 0% | — | **空闲** |
| | GPU 1 | 4672 / 97887 MiB | 1% | 432791 | **占用** (低负载) |
| | GPU 2 | 1 / 97887 MiB | 0% | — | **空闲** |
| | GPU 3 | 1 / 97887 MiB | 0% | — | **空闲** |
| **westd-27271** (2× H800) | GPU 0 | 15964 / 97887 MiB | 81% | 486402 | **占用** (活跃) |
| | GPU 1 | 1 / 97887 MiB | 0% | — | **空闲** |

## 汇总

- **总计 14 GPU**：5 占用，9 空闲
- **空闲可用**：
  - cqa1-33015 GPU 3 (24GB RTX 4090)
  - westd-41074 GPU 0-3 (4× 98GB H800) — 整机空闲
  - westd-38929 GPU 0/2/3 (3× 98GB H800)
  - westd-27271 GPU 1 (98GB H800)
- **注意**：westd-38929 GPU 1 有进程但利用率仅 1%，可能是残留进程或 idle 推理服务

---
