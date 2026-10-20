# ops progress check both servers

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_progress_check_both_servers_20260523T214739_result.json`
- **Structured JSON:** [`673fec8cbed244ef19cd.json`](../../sessions/67/673fec8cbed244ef19cd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-34685 (4x H100)

| GPU | Util | VRAM |
|-----|------|------|
| 0 | 97% | 63.0/97.9 GB |
| 1 | 99% | 63.0/97.9 GB |
| 2 | 0% | 16.8/97.9 GB |
| 3 | 1% | 16.8/97.9 GB |

| 实验 | 类型 | 进度 | 速度 | 预估剩余 |
|------|------|------|------|----------|
| **cutoff_45k_s0** | train | 10198/50005 (20%) | ~1.08 it/s | ~10.2h |
| **cutoff_15k_s0** | train | 11102/50005 (22%) | ~1.08 it/s | ~10.0h |
| **reverse_cutoff_s0_eval_v3** | eval | Task 7/10, T7: 2/50 | ~6s/ep | ~20min |
| **cutoff_25k_s0_eval_v3** | eval | Task 7/10, T7: 33/50 | ~6s/ep | ~15min |

cutoff_15k_s0 最新 loss: `occ=0.0106, action=0.0981` (step 11100)

---

## westd-10894 (4x H100)

| GPU | Util | VRAM |
|-----|------|------|
| 0 | 83% | 62.2/97.9 GB |
| 1 | 99% | 62.2/97.9 GB |
| 2 | 99% | 62.2/97.9 GB |
| 3 | 99% | 62.2/97.9 GB |

| 实验 | 类型 | 进度 | 速度 | 预估剩余 |
|------|------|------|------|----------|
| **detach_ln_s0** | train | **50005/50005 ✅ 已完成** | — | 0 |
| **cutoff_s2_v2** | train | 26452/50005 (53%) | ~1.08 it/s | ~6.1h |
| **detach_ln_s1** | train | 15671/50005 (31%) | ~1.08 it/s | ~8.8h |
| **detach_ln_s2** | train | 15552/50005 (31%) | ~1.08 it/s | ~8.9h |

- **detach_ln_s0** 已训练完成 (EXIT_CODE=0)，耗时 14h12m
- **cutoff_s2_v2** 最新 loss: `occ=0.0113, action=0.0791` (step 26400)
- **detach_ln_s1** 最新 loss: `occ=0.0095, action=0.1060` (step 15500)
- **detach_ln_s2** 最新 loss: `occ=0.0121, action=0.1299` (step 15500)

detach_ln_s0 完成后 GPU 仍被占用（62GB），可能进程未完全退出或有新任务接管。

---
