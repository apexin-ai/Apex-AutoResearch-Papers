# status gpu scan all servers

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_gpu-scan-all-servers_20260522T135208_result.json`
- **Structured JSON:** [`befd94350e41ced459e7.json`](../../sessions/be/befd94350e41ced459e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## bjb1-32546 (6× RTX 4090)
| GPU | 状态 | PID | 显存 | GPU利用率 |
|-----|------|-----|------|----------|
| cuda:0 | **占用** | 218144 (python) | 11316/24564 MiB | 28% |
| cuda:1 | **占用** | 218433 (python) | 11316/24564 MiB | 27% |
| cuda:2 | **占用** | 218713 (python) | 11783/24564 MiB | 25% |
| cuda:3 | **占用** | 322367 (python) | 532/24564 MiB | 10% |
| cuda:4 | **占用** | 326387 (python) | 546/24564 MiB | 9% |
| cuda:5 | **空闲** | — | 2 MiB | 0% |

**重点：cuda:0-2 仍有 python 进程在跑（各占 ~11GB，GPU util 25-28%），旧 CRM Object eval 尚未结束。** cuda:3-4 有轻量进程（~500MB，可能是 unified CRM r4 相关）。cuda:5 完全空闲。

## bjb1-18228 (4× RTX 4090)
| GPU | 状态 | PID | 显存 | GPU利用率 |
|-----|------|-----|------|----------|
| cuda:0 | **占用** | 883211 (python) | 9874/24564 MiB | 27% |
| cuda:1 | **空闲** | — | 0 MiB | 0% |
| cuda:2 | **空闲** | — | 0 MiB | 0% |
| cuda:3 | **空闲** | — | 0 MiB | 0% |

**异常：预期 cuda:1-3 跑 π0.5 Spatial r4 baseline，实际只有 cuda:0 有进程。cuda:1-3 全部空闲。** 可能训练已结束或异常退出。

## bjb2-28827 (6× RTX 4090)
| GPU | 状态 | PID | 显存 | GPU利用率 |
|-----|------|-----|------|----------|
| cuda:0 | **空闲** | — | 0 MiB | 0% |
| cuda:1 | **空闲** | — | 0 MiB | 0% |
| cuda:2 | **空闲** | — | 0 MiB | 0% |
| cuda:3 | **占用** | 206132 (python) | 9874/24564 MiB | 22% |
| cuda:4 | **占用** | 206279 (python) | 9874/24564 MiB | 20% |
| cuda:5 | **占用** | 206558 (python) | 9874/24564 MiB | 20% |

cuda:3-5 在跑任务（可能是 SmolVLA Long eval），cuda:0-2 完全空闲。

## bjb2-40593 (1× RTX 4090 D)
| GPU | 状态 | PID | 显存 | GPU利用率 |
|-----|------|-----|------|----------|
| cuda:0 | **空闲** | — | 0 MiB | 0% |

OFT eval 已结束，完全空闲。

---

**总结可用卡：** bjb1-32546 cuda:5、bjb1-18228 cuda:1-3、bjb2-28827 cuda:0-2、bjb2-40593 cuda:0 — 共 **8 张空闲 4090**。bjb1-18228 情况需关注，π0.5 Spatial r4 baseline 可能已异常退出。

---
