# ops gpu audit westd41074 v3

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-audit-westd41074-v3_20260520T154438_result.json`
- **Structured JSON:** [`56a2289968120e4fdc2a.json`](../../sessions/56/56a2289968120e4fdc2a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

原始 nvidia-smi 输出：

```
Wed May 20 23:45:03 2026       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 580.82.09              Driver Version: 580.82.09      CUDA Version: 13.0     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:38:00.0 Off |                  Off |
| N/A   52C    P0            307W /  600W |   15980MiB /  97887MiB |     78%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:49:00.0 Off |                  Off |
| N/A   49C    P0            275W /  600W |   15980MiB /  97887MiB |     67%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   2  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:5A:00.0 Off |                  Off |
| N/A   36C    P0            177W /  600W |   28555MiB /  97887MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   3  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:A8:00.0 Off |                  Off |
| N/A   44C    P0            175W /  600W |   27535MiB /  97887MiB |     94%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|    0   N/A  N/A          468330    C+G   python                                15961MiB |
|    1   N/A  N/A          468864    C+G   python                                15961MiB |
|    2   N/A  N/A           68539      C   python                                28546MiB |
|    3   N/A  N/A           68852      C   python                                27526MiB |
+-----------------------------------------------------------------------------------------+
```

**GPU 进程映射：**

| GPU | PID | 任务 | 显存 | GPU-Util | 运行时间 |
|-----|-----|------|------|----------|----------|
| 0 | 468330 | eval random_prune k=0.7 seed43 v2 | 15961MiB / 97887MiB | 78% | 02:09:19 |
| 1 | 468864 | eval random_prune k=0.5 seed43 v2 | 15961MiB / 97887MiB | 67% | 02:08:47 |
| 2 | 68539 | train smart_compress M96 | 28546MiB / 97887MiB | 0% | 12:04:45 |
| 3 | 68852 | train smart_compress M64 | 27526MiB / 97887MiB | 94% | 12:04:14 |

4 个进程全部存活（状态 `Rl`），4 张 GPU 全部占用。GPU2 (M96) util 为 0% 但进程在跑，可能处于数据加载/checkpoint 阶段。tmux 无活跃 session（exit code 1）。

---
