# ops live status all servers

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_live_status_all_servers_20260520T005811_result.json`
- **Structured JSON:** [`4eb18d91e09cb7881184.json`](../../sessions/4e/4eb18d91e09cb7881184.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== cqa1-33015 (4x RTX 4090D) ===
GPU 0: eval m16_seed44   PID=994858  VRAM=3459MiB  进度=415/500 ep (~83%)
GPU 1: eval m128_seed43  PID=818806  VRAM=3461MiB  进度=124/500 ep (~25%)
GPU 2: eval m16_seed43   PID=819552  VRAM=3427MiB  进度=105/500 ep (~21%)
GPU 3: 空闲 (1MiB)
Eval 结果: 已有大量历史 JSON，当前三个 eval 尚未完成
磁盘: 140/250GB used (111GB free)

=== westd-41074 (4x RTX PRO 6000 Blackwell 96GB) ===
GPU 0: C5 RoboFlamingo v2  PID=26118  VRAM=30108MiB  step=9950 (epoch 2/50)
         loss=0.1464  arm=0.0789  grip=0.7106  LR=9.99e-05
         epoch 1 耗时 7217s → 50 epochs 预计总耗时 ~100h
GPU 1: 空闲 (0MiB)
GPU 2: 空闲 (0MiB)
GPU 3: 空闲 (0MiB)
磁盘: 230/250GB used (21GB free) ⚠️ 紧张

=== westd-27271 (2x RTX PRO 6000 Blackwell 96GB) ===
GPU 0: VTC+LoRA M=128  PID=841334  VRAM=32276MiB  GPU-Util=95%
         运行中 (自 02:38 启动，约6.3h)
         checkpoint_step10000.pt 保存于 07:51 → 当前估计 ~12K steps
         未找到独立 log 文件，wandb run=cl5xi7q3 活跃中
GPU 1: M=32 VTC-only  PID=855140  VRAM=25942MiB
         step=1400/100K  loss=3.54  sps=0.6  lr=1e-4
         启动于 ~08:16，预计总耗时 ~46h
磁盘: 160/250GB used (91GB free) ✓
```

**要点：**
- cqa1 GPU 0 的 eval 即将完成（~10min），GPU 1/2 还需 ~40min
- westd-41074 有 3 块 GPU 空闲，磁盘仅剩 21GB 需关注
- westd-27271 两块 GPU 都在跑长训练，VTC+LoRA M=128 缺少可读 log

---
