# scan all servers p4 sync

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_scan_all-servers-p4-sync_20260520T124556_result.json`
- **Structured JSON:** [`12c44b8175192add048d.json`](../../sessions/12/12c44b8175192add048d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整 GPU 地图如下：

## GPU 状态全景表

### bjb2-28827 (6× RTX 4090)

| GPU | 状态 | PID | 显存占用 | 实验 |
|-----|------|-----|---------|------|
| cuda:0 | **运行中** | 307491 | 1470/24564 MiB | `adaptive_k` / spatial / p75 / seed44 |
| cuda:1 | **运行中** | 307767 | 2536/24564 MiB | `adaptive_k` / spatial / p25 / seed44 |
| cuda:2 | **运行中** | 308043 | 2007/24564 MiB | `adaptive_k` / spatial / p90 / seed42 |
| cuda:3 | 空闲 | — | 1/24564 MiB | — |
| cuda:4 | 空闲 | — | 1/24564 MiB | — |
| cuda:5 | 空闲 | — | 1/24564 MiB | — |

### bjb1-18228 (4× RTX 4090)

| GPU | 状态 | PID | 显存占用 | 实验 |
|-----|------|-----|---------|------|
| cuda:0 | 空闲 | — | 0/24564 MiB | — |
| cuda:1 | 空闲 | — | 0/24564 MiB | — |
| cuda:2 | 空闲 | — | 0/24564 MiB | — |
| cuda:3 | 空闲 | — | 0/24564 MiB | — |

### bjb1-32546 (6× RTX 4090)

| GPU | 状态 | PID | 显存占用 | 实验 |
|-----|------|-----|---------|------|
| cuda:0 | 空闲 | — | 2/24564 MiB | — |
| cuda:1 | **运行中** | 401661 | 3785/24564 MiB | `crm_obs_only` / goal / norm02 / seed51 |
| cuda:2 | **运行中** | 401735 | 4316/24564 MiB | `crm_obs_only` / object / norm02 / seed43 (r3) |
| cuda:3 | 空闲 | — | 2/24564 MiB | — |
| cuda:4 | 空闲 | — | 2/24564 MiB | — |
| cuda:5 | 空闲 | — | 2/24564 MiB | — |

### bjb2-40593 (1× RTX 4090)

| GPU | 状态 | PID | 显存占用 | 实验 |
|-----|------|-----|---------|------|
| cuda:0 | 空闲 | — | 0/24564 MiB | — |

## 汇总

- **活跃进程**: 5 个（bjb2-28827 上 3 个，bjb1-32546 上 2 个）
- **空闲 GPU**: 12 块（bjb2-28827×3, bjb1-18228×4, bjb1-32546×4, bjb2-40593×1）
- bjb2-28827 跑的是 **adaptive_k 评估**（spatial benchmark, 不同 percentile/seed 组合）
- bjb1-32546 跑的是 **crm_obs_only 评估**（goal 和 object benchmark, norm0.2）
- bjb1-18228 **全部空闲**，4 块 GPU 可用

---
