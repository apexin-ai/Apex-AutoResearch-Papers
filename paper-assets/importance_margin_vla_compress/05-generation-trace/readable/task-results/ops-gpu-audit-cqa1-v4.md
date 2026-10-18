# ops gpu audit cqa1 v4

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-audit-cqa1-v4_20260520T162918_result.json`
- **Structured JSON:** [`70f8b16f9e24e0841801.json`](../../sessions/70/70f8b16f9e24e0841801.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 1. 原始 nvidia-smi 输出

```
0, 3 %, 5024 MiB, 24564 MiB
1, 1 %, 4537 MiB, 24564 MiB
2, 0 %, 4055 MiB, 24564 MiB
3, 0 %, 4064 MiB, 24564 MiB
```

## 2. 原始 ps 输出（python 进程）

```
root     344867  333  0.7 44112128 8088964 ?    Rl   May20 384:44 python -u eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_object --keep_ratio 0.3 --num_episodes 50 --seed 43 --domain_id 3 --gpu 0 --output eval_results/xvla_prune_k0.3_libero_object_seed43.json
root     346216  329  0.7 42814576 8037276 ?    Rl   May20 378:25 python -u eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_object --keep_ratio 0.3 --num_episodes 50 --seed 44 --domain_id 3 --gpu 0 --output eval_results/xvla_prune_k0.3_libero_object_seed44.json
root     443004  313  0.7 55364576 7866204 ?    Rl   May20 242:04 python -u eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_object --keep_ratio 0.2 --num_episodes 50 --seed 43 --domain_id 3 --gpu 0 --output eval_results/xvla_prune_k0.2_libero_object_seed43.json
root     518362  297  0.7 55495788 7751064 ?    Rl   May20 125:03 python -u eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_object --keep_ratio 0.2 --num_episodes 50 --seed 44 --domain_id 3 --gpu 2 --output eval_results/xvla_prune_k0.2_libero_object_seed44.json
```

## 3. PID Detail

```
PID 443004: Rl  01:17:09  keep_ratio=0.2 seed=43 --gpu 0
PID 346216: Rl  01:54:53  keep_ratio=0.3 seed=44 --gpu 0 (实际 CUDA_VISIBLE_DEVICES=1)
PID 518362: Rl  00:42:07  keep_ratio=0.2 seed=44 --gpu 2
PID 344867: Rl  01:55:24  keep_ratio=0.3 seed=43 --gpu 0 (实际 CUDA_VISIBLE_DEVICES=3)
```

## 4. GPU → PID → 任务映射

| GPU | 显存占用 | PID | 任务 | 运行时间 |
|-----|---------|-----|------|---------|
| 0 | 5024 MiB | 443004 | k=0.2 seed=43 | 1h17m |
| 1 | 4537 MiB | 346216 | k=0.3 seed=44 | 1h55m |
| 2 | 4055 MiB | 518362 | k=0.2 seed=44 | 42m |
| 3 | 4064 MiB | 344867 | k=0.3 seed=43 | 1h55m |

4 个进程全部 `Rl` 状态（Running），4 块 GPU 全部在用。

## 5. 已完成的实验结果

已有 JSON 文件（k=0.9/0.7/0.5 的 seed43 和 seed44 均已完成）：

| 文件 | 完成时间 |
|------|---------|
| xvla_prune_k0.9_libero_object_seed43.json | May 20 20:44 |
| xvla_prune_k0.9_libero_object_seed44.json | May 20 22:16 |
| xvla_prune_k0.7_libero_object_seed43.json | May 20 21:22 |
| xvla_prune_k0.7_libero_object_seed44.json | May 20 22:54 |
| xvla_prune_k0.5_libero_object_seed43.json | May 20 21:43 |
| xvla_prune_k0.5_libero_object_seed44.json | May 20 23:12 |

k=0.3 和 k=0.2 的结果 JSON 尚未生成（4 个进程仍在跑）。

## 6. 空闲 GPU

**无空闲 GPU。** 4 块 GPU 全部被占用，分别跑 k=0.3 (seed43/44) 和 k=0.2 (seed43/44) 的 eval。

---
