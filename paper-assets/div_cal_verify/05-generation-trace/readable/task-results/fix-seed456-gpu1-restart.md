# fix seed456 gpu1 restart

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_seed456_gpu1_restart_20260513T175149_result.json`
- **Structured JSON:** [`8fd4be40357f042837a5.json`](../../sessions/8f/8fd4be40357f042837a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
Thu May 14 01:52:27 2026       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 595.58.03              Driver Version: 595.58.03      CUDA Version: 13.2     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|=========================================+========================+======================|
|   0  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:38:00.0 Off |                  Off |
| N/A   51C    P0            200W /  600W |   79986MiB /  97887MiB |    100%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:5A:00.0 Off |                  Off |
| N/A   28C    P8             35W /  600W |       0MiB /  97887MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|    0   N/A  N/A          250452      C   python3                               15400MiB |
|    0   N/A  N/A          250453      C   python3                               15400MiB |
+-----------------------------------------------------------------------------------------+
===
random_50_seed123: 1 windows (created Thu May 14 01:08:06 2026)
random_50_seed456: 1 windows (created Thu May 14 01:08:06 2026)
seed456_methods: 1 windows (created Thu May 14 01:52:08 2026)
```

GPU 0 正在被其他 session 占用（100% util, ~80GB/98GB），GPU 1 空闲。`seed456_methods` session 已创建，但当前 GPU 0 满载，任务可能在排队等待。

---
