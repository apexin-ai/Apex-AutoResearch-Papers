# submit seed456 methods cuda1

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_seed456_methods_cuda1_20260513T171123_result.json`
- **Structured JSON:** [`9f5aa8f1e7a7fd465cb9.json`](../../sessions/9f/9f5aa8f1e7a7fd465cb9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**nvidia-smi:**
```
Thu May 14 01:31:40 2026
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 595.58.03              Driver Version: 595.58.03      CUDA Version: 13.2     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|=========================================+========================+======================|
|   0  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:38:00.0 Off |                  Off |
| N/A   72C    P0            486W /  600W |   79986MiB /  97887MiB |    100%      Default |
|   1  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:5A:00.0 Off |                  Off |
| N/A   27C    P8             35W /  600W |       0MiB /  97887MiB |      0%      Default |
+-----------------------------------------+------------------------+----------------------+
| Processes:                                                                              |
|   0   N/A  N/A   250452   C   python3                               15400MiB            |
|   0   N/A  N/A   250453   C   python3                               15400MiB            |
+-----------------------------------------------------------------------------------------+
```

**tmux ls:**
```
random_50_seed123: 1 windows (created Thu May 14 01:08:06 2026)
random_50_seed456: 1 windows (created Thu May 14 01:08:06 2026)
seed456_methods: 1 windows (created Thu May 14 01:31:22 2026)
```

GPU 0 正在被已有任务占用（100%, 80GB/98GB），GPU 1 空闲。`seed456_methods` tmux session 已创建，但当前 GPU 0 满载，seed456_methods 的任务可能需要等前面的任务完成才能实际开始训练。

---
