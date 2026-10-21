# gpu check idle audit 20260526

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu-check_idle-audit-20260526_20260526T163308_result.json`
- **Structured JSON:** [`54a0a2e4bf0a3ad2587b.json`](../../sessions/54/54a0a2e4bf0a3ad2587b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 实际状态

### cqa1-33015 (RTX 4090D × 4)

| GPU | Util | Memory | 进程 | 状态 |
|-----|------|--------|------|------|
| cuda:0 | 0% | 10446/24564 MiB | PID 384775 (python) | **占用中** — util=0% 但有进程占 10GB，可能在等待/加载数据 |
| cuda:1 | 0% | 10448/24564 MiB | PID 416018 (python) | **占用中** — 同上 |
| cuda:2 | 11% | 10162/24564 MiB | PID 467731 (python) | **占用中** — 活跃计算 |
| cuda:3 | 0% | 1/24564 MiB | 无 | **空闲** |

### westd-41074 (RTX PRO 6000 Blackwell × 4, 98GB/卡)

| GPU | Util | Memory | 进程 | 状态 |
|-----|------|--------|------|------|
| cuda:0 | 60% | 15980/97887 MiB | PID 682346 (python) | **占用中** — 活跃训练 |
| cuda:1 | 73% | 15980/97887 MiB | PID 652888 (python) | **占用中** — 活跃训练 |
| cuda:2 | 0% | 1/97887 MiB | 无 | **空闲** |
| cuda:3 | 49% | 15984/97887 MiB | PID 642262 (python) | **占用中** — 活跃训练 |

## 真正空闲的 GPU

- **`cqa1-33015:cuda:3`** — 0% util, 1 MiB memory, 无进程 (24GB RTX 4090D)
- **`westd-41074:cuda:2`** — 0% util, 1 MiB memory, 无进程 (98GB RTX PRO 6000 Blackwell)

注意：cqa1-33015 的 cuda:0 和 cuda:1 虽然 util=0%，但各有 python 进程占用 ~10GB 显存，不是空闲的（可能在做 eval 或数据加载间隙）。

---
