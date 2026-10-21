# diag gpu idle deploy 0527b

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_gpu_idle_deploy_0527b_20260527T002559_result.json`
- **Structured JSON:** [`75dcd7b6702ba61cf2ea.json`](../../sessions/75/75dcd7b6702ba61cf2ea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### westd-27271
| GPU | 状态 | 详情 |
|-----|------|------|
| **GPU 0** | **已部署** | PID 499267 已死。已部署 `eval_openvla_l2norm_k095_goal_seed42`，PID 609726，L2norm pruning 256→243 tokens，Task 1/10 开始推理 |
| GPU 1 | 忙碌 | 15938 MiB, 67%，`eval_attn_k05_long` 在跑 Task 10/10（即将完成） |

### westd-41074
| GPU | 状态 | 详情 |
|-----|------|------|
| **GPU 0** | **已部署** | 已部署 `eval_openvla_random_k095_long_seed42`，PID 32175，16188 MiB/72%，Random pruning 256→243 tokens，Task 1/10 开始推理 |
| GPU 1-3 | 忙碌 | 各 ~16GB, 69-84%，跑 OpenVLA 其他实验 |

### cqa1-33015
| GPU | 状态 | 详情 |
|-----|------|------|
| GPU 0-1 | 忙碌 | ~15.3GB, 70-82%，正常运行 |
| **GPU 2** | 正常运行 | PID 790017, 10.5GB/24% — `pi05_l2norm_k085_long` (libero_10), Task 6/10 ep10, 当前 SR=90.3%。低利用率正常（eval 在环境 step 间歇推理） |
| **GPU 3** | 正常运行 | PID 732826, 10GB/18% — `pi05_random_k07_long` (libero_10), Task 8/10 ep30, 当前 SR=68.0%。同理，正常运行中 |

### 总结
- 2 张空闲卡已部署：Goal L2norm k=0.95 (westd-27271) + Long Random k=0.95 (westd-41074)
- cqa1 GPU 2+3 无异常，pi05 eval 正常推进，预计 2-3h 内完成

---
