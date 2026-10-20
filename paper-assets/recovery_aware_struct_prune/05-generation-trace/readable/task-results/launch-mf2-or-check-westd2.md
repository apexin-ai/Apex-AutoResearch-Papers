# launch mf2 or check westd2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_launch_mf2_or_check_westd2_20260522T102854_result.json`
- **Structured JSON:** [`762d4ad22e1741ae2508.json`](../../sessions/76/762d4ad22e1741ae2508.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 2 已占用 25174MiB（94% 利用率），训练已开始。PID 36832 + 37026（ref model）在 GPU 2 上。

```
MF2 模型检查:
  SFT RASP: MISSING
  SFT Random: OK (12GB)
  GRPO RASP seed123: 不存在（且 SFT RASP 缺失无法跑）
  GRPO RASP seed456: 目录存在但无 model.safetensors（仅有 checkpoint-100）
  GRPO Random seed123: 需要跑 → 已启动
  GRPO Random seed456: 不存在

启动: Random seed123 GRPO（回退方案，因 SFT RASP 不存在）
PID: 36832 (python) / 36825 (bash wrapper)

=== nvidia-smi 完整输出 ===
Fri May 22 18:32:46 2026       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 580.82.09              Driver Version: 580.82.09      CUDA Version: 13.0     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|=========================================+========================+======================|
|   0  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:49:00.0 Off |                  Off |
| N/A   75C    P0            578W /  600W |   19251MiB /  97887MiB |     98%      Default |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:5A:00.0 Off |                  Off |
| N/A   78C    P0            601W /  600W |   17651MiB /  97887MiB |     98%      Default |
+-----------------------------------------+------------------------+----------------------+
|   2  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:98:00.0 Off |                  Off |
| N/A   54C    P0            476W /  600W |   25174MiB /  97887MiB |     94%      Default |
+-----------------------------------------+------------------------+----------------------+
|   3  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:C8:00.0 Off |                  Off |
| N/A   66C    P0            413W /  600W |   54119MiB /  97887MiB |     95%      Default |
+-----------------------------------------+------------------------+----------------------+
| Processes:                                                                              |
|    0   N/A  N/A            2234      C   python                                19242MiB |
|    1   N/A  N/A            5241      C   python                                17642MiB |
|    2   N/A  N/A           36832      C   python                                12326MiB |
|    2   N/A  N/A           37026      C   python                                12834MiB |
|    3   N/A  N/A           36167      C   python                                54110MiB |
+-----------------------------------------------------------------------------------------+

=== ps 输出 ===
PID 36832: python src/train_grpo_v5.py (State: R, 234 threads)
PID 37026: python ref_model process

GPU 2 占用确认: 是（25174MiB, 94% util, 2 个 python 进程）
```

---
