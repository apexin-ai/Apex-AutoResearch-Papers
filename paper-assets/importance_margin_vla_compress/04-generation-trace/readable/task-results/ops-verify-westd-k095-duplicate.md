# ops verify westd k095 duplicate

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-westd-k095-duplicate_20260520T215023_result.json`
- **Structured JSON:** [`db444a69eb1014390681.json`](../../sessions/db/db444a69eb1014390681.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论：确认重复

### 重复实验：`random_prune k_ratio=0.95 seed=43`

| | westd-41074 GPU 0 | westd-38929 GPU 0 |
|---|---|---|
| PID | 564806 | 975878 |
| 启动时间 | 02:20:16 | 03:11:17（晚 51 分钟）|
| 进度 | Task 9/10, Ep 10/50 | Task 1/10, Ep 10/50 |
| 输出文件 | `openvla_random_k095_seed43.json` | `openvla_prune_random_k095_seed43.json` |
| 完整命令 | `CUDA_VISIBLE_DEVICES=0 python -u eval_openvla_libero.py --mode random_prune --k_ratio 0.95 --suite libero_object --seed 43` | `CUDA_VISIBLE_DEVICES=0 python -u eval_openvla_libero.py --mode random_prune --k_ratio 0.95 --suite libero_object --num_episodes 50 --seed 43` |

**westd-41074 启动更早、进度远超（9/10 vs 1/10），westd-38929 上的是浪费。**

### 两台服务器完整 GPU 占用

**westd-41074:**
| GPU | 实验 | seed |
|---|---|---|
| 0 | random_prune k=0.95 | 43 |
| 1 | random_prune k=0.9 (tmux eval_random_k09_s42) | 42 |
| 2 | train_openvla_smart_compress m96 | 42 |
| 3 | train_openvla_smart_compress m64 | 42 |

**westd-38929:**
| GPU | 实验 | seed |
|---|---|---|
| 0 | **random_prune k=0.95 (重复!)** | 43 |
| 0 | random_prune k=0.95 | 42 |
| 1 | random_prune k=0.7 | 42 |
| 2 | random_prune k=0.3 | 43 |
| 3 | l2norm_prune k=0.9 | 43 |

westd-38929 GPU 0 上跑了两个实验（k095 seed43 + k095 seed42），互相抢显存，建议 kill 掉重复的 seed43（PID 975878 / tmux session `eval_random_k095_s43`）。

---
