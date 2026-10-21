# diag gpu status all servers 0527

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_gpu_status_all_servers_0527_20260526T233240_result.json`
- **Structured JSON:** [`dbf83910ab12de2b7baa.json`](../../sessions/db/dbf83910ab12de2b7baa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 诊断结果 (2026-05-27 07:33 UTC)

### cqa1-33015 (4× RTX 4090 D 24GB)
| GPU | Status | Experiment |
|-----|--------|-----------|
| **0** | **IDLE** | — |
| **1** | **IDLE** | — |
| 2 | Running 44% | π0.5 attn k=0.5 Long s42 |
| 3 | Running 16% | π0.5 random k=0.7 Long s42 |

eval_pi05_attn_k095_long_seed42 已完成 (**SR=77.0%**, 04:20 UTC)，已更新 registry → DONE。

### westd-38929 (4× RTX PRO 6000 98GB)
| GPU | Status | Experiment |
|-----|--------|-----------|
| 0 | Running 43% | OV L2norm k=0.5 Long s42 |
| 1 | Running 70% | OV Random k=0.85 Long s42 v3 |
| 2 | Running 48% | OV L2norm k=0.75 Long s42 |
| 3 | Running 89% | OV Random k=0.75 Goal s42 (不在 registry) |

### westd-41074 (4× RTX PRO 6000 98GB)
| GPU | Status | Experiment |
|-----|--------|-----------|
| 0 | Running 0%* | OV Random k=0.75 Object s42 (不在 registry; 进程活跃，瞬时0%) |
| 1 | Running 82% | OV Random k=0.75 Long s42 |
| 2 | Running 84% | OV Random k=0.95 Object s42 (不在 registry) |
| 3 | Running 80% | OV Attn k=0.75 Long s42 |

### westd-27271 (2× RTX PRO 6000 98GB)
| GPU | Status | Experiment |
|-----|--------|-----------|
| 0 | Running 70% | OV Attn k=0.75 Goal s42 |
| 1 | Running 74% | OV Attn k=0.5 Long s42 |

### 汇总
- **12/14 GPU 在跑，2 张空闲** (cqa1 GPU 0 + GPU 1, RTX 4090D 24GB)
- Cron 悬疑已解决：L2norm k=0.5 在 westd-38929 GPU 0，Attn k=0.5 在 westd-27271 GPU 1
- 5 个实验在跑但不在 registry 中（3个 OV Random 系列 + 2个 π0.5）
- eval_pi05_attn_k095_long_seed42 已完成，registry 已更新

---
