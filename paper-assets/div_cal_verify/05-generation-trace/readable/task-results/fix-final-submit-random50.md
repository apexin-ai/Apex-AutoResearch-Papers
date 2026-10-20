# fix final submit random50

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_final_submit_random50_20260513T170748_result.json`
- **Structured JSON:** [`4020202bac8a02eaf256.json`](../../sessions/40/4020202bac8a02eaf256.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**nvidia-smi:**
```
Thu May 14 01:08:24 2026       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 595.58.03              Driver Version: 595.58.03      CUDA Version: 13.2     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|=========================================+========================+======================|
|   0  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:38:00.0 Off |                  Off |
| N/A   37C    P8             37W /  600W |   49175MiB /  97887MiB |      0%      Default |
|   1  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:5A:00.0 Off |                  Off |
| N/A   36C    P8             38W /  600W |       0MiB /  97887MiB |      0%      Default |
+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+
```

**tmux ls:**
```
random_50_seed123: 1 windows (created Thu May 14 01:08:06 2026)
random_50_seed456: 1 windows (created Thu May 14 01:08:06 2026)
```

两个 tmux session 已启动。GPU 0 有 ~49GB 显存占用但无进程显示（可能刚启动还在加载），GPU 1 空闲。

---
