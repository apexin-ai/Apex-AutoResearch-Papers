# ssh gpu audit bjb1 18228

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gpu-audit-bjb1-18228_20260520T011717_result.json`
- **Structured JSON:** [`c6f9359e3cd9c0bc6468.json`](../../sessions/c6/c6f9359e3cd9c0bc6468.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 健康审计 — bjb1-18228

| GPU | 利用率 | 显存占用 | 状态 |
|-----|--------|----------|------|
| cuda:0 | 0% | 1 MiB / 24564 MiB | **空闲可用** |
| cuda:1 | 0% | 1 MiB / 24564 MiB | **空闲可用** |
| cuda:2 | 0% | 1 MiB / 24564 MiB | **空闲可用** |
| cuda:3 | 21% | 4755 MiB / 24564 MiB | **占用中** |

### 实验状态

| 实验 | 状态 | 详情 |
|------|------|------|
| eval-adaptive-k-p50-seed43 | **运行中** | PID 196349 (非196344，可能重启过), cuda:3, 已运行 34min, 显存 4737 MiB |
| eval-vla-only-object-seed50 | **已完成** | 无对应进程 |
| eval-vla-only-long-seed48 | **已完成** | 无对应进程 |
| eval-crm-long-seed46 | **已完成** | 无对应进程 |

**结论**：cuda:0/1/2 三张卡完全空闲可用。cuda:3 正在跑 adaptive_k_p50_seed43 评估（object benchmark, seed 43），PID 与之前记录略有偏差（196349 vs 196344），但实验内容一致。

---
