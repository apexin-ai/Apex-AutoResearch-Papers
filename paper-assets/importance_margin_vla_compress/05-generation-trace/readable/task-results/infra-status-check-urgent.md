# infra status check urgent

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_status-check-urgent_20260515T144626_result.json`
- **Structured JSON:** [`c7fb27f35e6a83732fb6.json`](../../sessions/c7/c7fb27f35e6a83732fb6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== TMUX ===
mvp_baseline: 1 windows (created Fri May 15 22:44:21 2026)
mvp_imm_anchor: 1 windows (created Fri May 15 22:44:22 2026)
=== NVIDIA-SMI ===
Fri May 15 22:46:52 2026       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 580.95.05              Driver Version: 580.95.05      CUDA Version: 13.0     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:B8:00.0 Off |                  Off |
| N/A   31C    P8             35W /  600W |       3MiB /  97887MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:C8:00.0 Off |                  Off |
| N/A   31C    P8             35W /  600W |       3MiB /  97887MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+
=== TRAIN PROCESSES ===
root      24513  0.0  0.0   6080  3808 ?        Ss   22:44   0:00 tmux new-session -d -s mvp_baseline ...
root      24514  0.0  0.0   4364  3236 pts/0    Ss+  22:44   0:00 bash -c ...
root      24520 92.3  0.2 31216436 2149588 pts/0 Sl+ 22:44   2:18 python train.py --config configs/baseline.yaml --gpu 0 --seed 42 --wandb_run baseline_seed42
root      24587  0.0  0.0   4364  3264 pts/1    Ss+  22:44   0:00 bash -c ...
root      24593 82.0  0.2 31235620 2169012 pts/1 Sl+ 22:44   2:02 python train.py --config configs/imm_anchor.yaml --gpu 0 --seed 42 --wandb_run imm_d03_l05_seed42
=== BASELINE LOG (last 20) ===
2026-05-15 22:44:23 [INFO] Device: cuda:0
2026-05-15 22:44:23 [INFO] Loading SmolVLA policy...
=== IMM LOG (last 20) ===
2026-05-15 22:44:24 [INFO] Device: cuda:0
2026-05-15 22:44:24 [INFO] Loading SmolVLA policy...
```

两个 tmux session 都在运行，train.py 进程存在（CPU 占用 92%/82%），但 GPU 显存 0MB、GPU-Util 0%——目前还在加载模型阶段，尚未开始 GPU 训练。日志也只到 "Loading SmolVLA policy..."。

---
