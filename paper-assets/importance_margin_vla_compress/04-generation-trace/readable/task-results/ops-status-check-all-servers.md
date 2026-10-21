# ops status check all servers

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_status_check_all_servers_20260517T202544_result.json`
- **Structured JSON:** [`e0808be86ab902484e19.json`](../../sessions/e0/e0808be86ab902484e19.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## cqa1-33015
| 实验 | 状态 | 进度 | 最新 loss | GPU 显存 |
|------|------|------|-----------|----------|
| M=32 | **ALIVE** (PID 342374, 2h48m) | step 43,450 / 100K (43.5%) | ~0.06 | GPU 0: 2,875 MiB |
| M=64 | **ALIVE** (PID 341605, 2h49m) | step 44,750 / 100K (44.8%) | ~0.07 | GPU 1: 2,791 MiB |

GPU 2-3: **空闲** (0 MiB, 0%)

两个训练速度稳定 (4.3-4.4 sps)，预计各剩约 ~3.5h。

## westd-27271
| 实验 | 状态 | 进度 | GPU 显存 |
|------|------|------|----------|
| OpenVLA random prune k=0.5 (object) | **ALIVE** (PID 697608, 55min) | Task 2/10, Ep 40/50 | GPU 0: 15,980 MiB (82%) |

**已完成 task SR:**
- Task 1 (pick up alphabet soup → basket): **0.600** (30/50)
- Task 2 (pick up cream cheese → basket): 进行中，当前 3/40

GPU 1: **空闲** (1 MiB, 0%)

**已完成的历史 pruning 评测结果** (eval_results/ 目录):
- `eval_random_prune_k05_object.json` — 5/17 16:49 完成
- `eval_random_prune_object.json` — 5/17 15:12 完成
- `eval_spatial_prune_k05.json` — 5/17 19:35 完成
- `eval_goal_prune_k05.json` — 5/17 20:50 完成
- 多个 `eval_imm_*_acis_prune.json` — 5/16-5/17 完成

---
