# ops check cqa1 gpu conflict

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-cqa1-gpu-conflict_20260524T140508_result.json`
- **Structured JSON:** [`822b0e87009a1d27c9ab.json`](../../sessions/82/822b0e87009a1d27c9ab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完成。

## cqa1-33015 GPU 状态汇总

| GPU | PID | 显存占用 | 实验 | 追踪状态 |
|-----|-----|---------|------|---------|
| 0 | 392492 | 10.2 GB | l2norm k=0.9 Long (libero_10) | **未追踪，重复** |
| 1 | 326332 | 10.1 GB | random k=0.3 Long (libero_10) | 日志 → `/tmp/eval_pi05_random_k03_long_postfix.log` |
| 2 | 326500 | 10.2 GB | random k=0.3 Spatial | 追踪：`eval_pi05_random_k03_spatial_seed42_postfix_v2` |
| 3 | 431409 | 10.5 GB | l2norm k=0.9 Long (libero_10) | 追踪：`eval_pi05_l2norm_k09_long_seed42_postfix_v2` |

**4 个 GPU 全部占满，0 个空闲。**

## 关键发现

### 1. l2norm k=0.5 Spatial 没有被 GPU 冲突覆盖

`eval_pi05_l2norm_k05_spatial_seed42_postfix` **已完成**（registry 状态 DONE/success，SR=57.4%）。

Worker #3 在 13:29 的部署实际上是一次**重跑尝试**，但它在启动时就崩溃了——网络错误而非 GPU 冲突：
```
ValueError: Failed to instantiate processor step 'tokenizer_processor'
Error: [Errno 99] Cannot assign requested address
```
GPU 3 在 Worker #4 部署 k=0.9 Long 之前就已空闲。**不需要重新部署。**

### 2. GPU 0 和 GPU 3 跑了重复实验

PID 392492 (GPU 0) 和 PID 431409 (GPU 3) 运行**完全相同**的命令：
```
python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.9 --suite libero_10 --n_episodes 50 --seed 42 --gpu 0
```

PID 392492 在旧的 tmux session `eval_pi05_l2norm_k03_goal_seed42` 里启动，且**没有设置 CUDA_VISIBLE_DEVICES**（所以落到了 GPU 0）。这是资源浪费——可以 kill 掉 PID 392492 释放 GPU 0。

### 建议操作
1. Kill PID 392492（GPU 0 上的重复 l2norm k=0.9 Long），释放 GPU 0
2. 无需为 l2norm k=0.5 Spatial 做任何操作——结果已在 registry

---
