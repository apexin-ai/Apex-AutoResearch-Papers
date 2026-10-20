# submit seed456 cuda1 cvd

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_seed456_cuda1_cvd_20260513T173149_result.json`
- **Structured JSON:** [`7c4be19c81ccf63d1fc4.json`](../../sessions/7c/7c4be19c81ccf63d1fc4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
Thu May 14 01:32:34 2026       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 595.58.03              Driver Version: 595.58.03      CUDA Version: 13.2     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|=========================================+========================+======================|
|   0  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:38:00.0 Off |                  Off |
| N/A   47C    P0             86W /  600W |   79986MiB /  97887MiB |      0%      Default |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:5A:00.0 Off |                  Off |
| N/A   28C    P8             35W /  600W |       0MiB /  97887MiB |      0%      Default |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|=========================================================================================|
|    0   N/A  N/A          250452      C   python3                               15400MiB |
|    0   N/A  N/A          250453      C   python3                               15400MiB |
+-----------------------------------------------------------------------------------------+
===
random_50_seed123: 1 windows (created Thu May 14 01:08:06 2026)
random_50_seed456: 1 windows (created Thu May 14 01:08:06 2026)
seed456_methods: 1 windows (created Thu May 14 01:32:15 2026)
```

GPU 1 当前 0MiB 占用、0% 利用率 — `seed456_methods` session 已创建但尚未开始使用 GPU。GPU 0 被其他两个 session 的进程占用（~80GB/98GB）。

---
