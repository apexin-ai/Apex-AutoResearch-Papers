# audit cqa1 gpu status 20260526c

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_cqa1-gpu-status-20260526c_20260526T195311_result.json`
- **Structured JSON:** [`589219f0d517d23b719e.json`](../../sessions/58/589219f0d517d23b719e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 张 GPU 全满，均在活跃运行 eval。汇总：

```
GPU 0: BUSY  PID=617566  script=eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 42
       VRAM=10145MiB/24564MiB  GPU-Util=25%  运行~1h20m
       log: T3 ep=20 8/20=40%, Total 117/150=78.0% (Task 2完成)

GPU 1: BUSY  PID=617728  script=eval_pi05_pruning_libero.py --prune_mode attention --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 42
       VRAM=10317MiB/24564MiB  GPU-Util=21%  运行~1h20m
       log: T3 ep=10 2/10=20%, Total 100/150=66.7% (Task 2完成)

GPU 2: BUSY  PID=582964  script=eval_pi05_pruning_libero.py --prune_mode attention --keep_ratio 0.5 --suite libero_10 --n_episodes 50 --seed 42
       VRAM=10636MiB/24564MiB  GPU-Util=31%  运行~2h17m
       log: T5完成 SR=52.0%, Total 174/300=58.0% (6/10 tasks done)

GPU 3: BUSY  PID=546287  script=eval_pi05_pruning_libero.py --prune_mode attention --keep_ratio 0.95 --suite libero_10 --n_episodes 50 --seed 42
       VRAM=10234MiB/24564MiB  GPU-Util=19%  运行~3h
       log: T8 ep=30 9/30=30%, Total 321/400=80.2% (8/10 tasks done, 接近完成)
```

**关于之前关注的 PID：**
- PID 199389 (eval_pi05_l2norm_k075_long_seed42) — **已不存在**，进程已结束
- PID 617566 / 617728 / 546287 — 全部活跃运行中

**空闲 GPU：无。** 4 张卡全部在跑实验，GPU 3 进度最快（8/10 tasks），预计最先完成。

---
