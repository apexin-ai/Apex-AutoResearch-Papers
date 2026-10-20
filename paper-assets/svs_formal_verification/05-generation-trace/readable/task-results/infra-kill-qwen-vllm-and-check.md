# infra kill qwen vllm and check

**svs formal verification** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_kill_qwen_vllm_and_check_20260514T120228_result.json`
- **Structured JSON:** [`0f18d5ba674450ea6010.json`](../../sessions/0f/0f18d5ba674450ea6010.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

- **Qwen vLLM（PID 41815/41816）**：已不存在，无需手动杀
- **GPU 2+3 当前状态**：已释放，各 3MiB 占用，0% 利用率
- **注意**：GPU 0+1 上有新的 vLLM 进程（PID 33642/33643），各占 31450MiB，99% 利用率
- **mvp_003 gold_label 计数**：**24**（路径 `/root/outputs/results_partial.json`）

完整 nvidia-smi：
```
Thu May 14 20:02:55 2026
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 580.76.05              Driver Version: 580.76.05      CUDA Version: 13.0     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
|=========================================+========================+======================|
|   0  NVIDIA GeForce RTX 5090        On  | 00000000:50:00.0  Off |                  N/A |
| 59%   66C    P1            467W / 575W  |   31459MiB / 32607MiB |     99%      Default |
|   1  NVIDIA GeForce RTX 5090        On  | 00000000:99:00.0  Off |                  N/A |
| 64%   70C    P1            516W / 575W  |   31459MiB / 32607MiB |     99%      Default |
|   2  NVIDIA GeForce RTX 5090        On  | 00000000:AB:00.0  Off |                  N/A |
| 42%   28C    P8             15W / 575W  |       3MiB / 32607MiB |      0%      Default |
|   3  NVIDIA GeForce RTX 5090        On  | 00000000:CF:00.0  Off |                  N/A |
| 40%   28C    P8              9W / 575W  |       3MiB / 32607MiB |      0%      Default |
+-----------------------------------------+------------------------+----------------------+
| Processes:                                                                              |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory Usage       |
|=========================================================================================|
|    0   N/A  N/A     33642      C   VLLM::Worker_TP0                31450MiB             |
|    1   N/A  N/A     33643      C   VLLM::Worker_TP1                31450MiB             |
+-----------------------------------------------------------------------------------------+
```

---
