# audit gpu status all servers

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_gpu-status-all-servers_20260526T145300_result.json`
- **Structured JSON:** [`4574b26c6bf5dc34e610.json`](../../sessions/45/4574b26c6bf5dc34e610.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

tmux 被 ssh_read_only 白名单拦截，跳过。nvidia-smi 数据已全部拿到，汇总如下：

---

## GPU 状态审计报告 (2026-05-26 22:56 UTC)

### 1. cqa1-32758 (6×4090D, 24GB each)

| GPU | 显存占用 | 状态 | 进程 |
|-----|---------|------|------|
| cuda:0 | 10317/24564 MiB | **占用** | python PID 216649 |
| cuda:1 | 1/24564 MiB | **空闲** | — |
| cuda:2 | 10788/24564 MiB | **占用** | python PID 364803 |
| cuda:3 | 10319/24564 MiB | **占用** | python PID 350486 |
| cuda:4 | 11860/24564 MiB | **占用** | python PID 350882 |
| cuda:5 | 11860/24564 MiB | **占用** | python PID 351448 |

**5 占用 / 1 空闲**

### 2. bjb1-32546 (6×4090, 24GB each)

| GPU | 显存占用 | 状态 | 进程 |
|-----|---------|------|------|
| cuda:0 | 2/24564 MiB | **空闲** | — |
| cuda:1 | 2/24564 MiB | **空闲** | — |
| cuda:2 | 2/24564 MiB | **空闲** | — |
| cuda:3 | 13063/24564 MiB | **占用** | python PID 872081 |
| cuda:4 | 2/24564 MiB | **空闲** | — |
| cuda:5 | 12446/24564 MiB | **占用** | python PID 872370 |

**2 占用 / 4 空闲**

### 3. bjb2-28827 (6×4090, 24GB each)

| GPU | 显存占用 | 状态 | 进程 |
|-----|---------|------|------|
| cuda:0 | 13606/24564 MiB | **占用** | python PID 443692 |
| cuda:1 | 13606/24564 MiB | **占用** | python PID 444363 |
| cuda:2 | 13516/24564 MiB | **占用** | python PID 445988 |
| cuda:3 | 13516/24564 MiB | **占用** | python PID 448295 |
| cuda:4 | 14741/24564 MiB | **占用** | python PID 450041 |
| cuda:5 | 14741/24564 MiB | **占用** | python PID 451711 |

**6 占用 / 0 空闲**

### 4. bjb1-18228 (4×4090, 24GB each)

| GPU | 显存占用 | 状态 | 进程 |
|-----|---------|------|------|
| cuda:0 | 14062/24564 MiB | **占用** | python PID 338026 |
| cuda:1 | 14062/24564 MiB | **占用** | python PID 338487 |
| cuda:2 | 1/24564 MiB | **空闲** | — |
| cuda:3 | 14062/24564 MiB | **占用** | python PID 339344 |

**3 占用 / 1 空闲**

### 5. westd-49937 (6×RTX PRO 6000, 96GB each)

| GPU | 显存占用 | 状态 | 进程 |
|-----|---------|------|------|
| cuda:0 | 13030/97887 MiB | **占用** | python PID 491271 |
| cuda:1 | 13030/97887 MiB | **占用** | python PID 491696 |
| cuda:2 | 13509/97887 MiB | **占用** | python PID 492088 |
| cuda:3 | 13443/97887 MiB | **占用** | python PID 492479 |
| cuda:4 | 12964/97887 MiB | **占用** | python PID 492867 |
| cuda:5 | 13443/97887 MiB | **占用** | python PID 493251 |

**6 占用 / 0 空闲**（但每卡仅用 ~13GB/96GB，剩余 ~84GB 显存可共享）

### 6. bjb2-24035 (1×4090D, 24GB)

| GPU | 显存占用 | 状态 | 进程 |
|-----|---------|------|------|
| cuda:0 | 11432/24564 MiB | **占用** | python PID 63656 |

**1 占用 / 0 空闲**

---

## 全集群汇总

| 指标 | 数值 |
|------|------|
| 总 GPU 数 | 29 |
| 占用 | 23 |
| 空闲 | **6** |

### 空闲 GPU 清单

```
cqa1-32758:cuda:1      (4090D, 24GB)
bjb1-32546:cuda:0      (4090, 24GB)
bjb1-32546:cuda:1      (4090, 24GB)
bjb1-32546:cuda:2      (4090, 24GB)
bjb1-32546:cuda:4      (4090, 24GB)
bjb1-18228:cuda:2      (4090, 24GB)
```

备注：tmux ls 不在 ssh_read_only 白名单内，无法查询。westd-49937 全部 6 卡虽有进程但每卡仅占 ~13%显存（13GB/96GB），如需可共享使用。

---
