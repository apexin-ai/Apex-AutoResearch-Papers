# ops kill gpu5 duplicate

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-gpu5-duplicate_20260516T182821_result.json`
- **Structured JSON:** [`3432faaeb2568e1b069c.json`](../../sessions/34/3432faaeb2568e1b069c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

PID 831490 已不存在（进程已自行退出或被别处 kill）。GPU 5 现在只剩 PID 831033。

以下是完整原始输出：

```
Sun May 17 02:28:52 2026       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 580.76.05              Driver Version: 580.76.05      CUDA Version: 13.0     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GeForce RTX 4090 D      On  |   00000000:16:00.0 Off |                  Off |
| 30%   46C    P2            220W /  425W |    8081MiB /  24564MiB |     74%      Default |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA GeForce RTX 4090 D      On  |   00000000:39:00.0 Off |                  Off |
| 47%   65C    P2            405W /  425W |    8281MiB /  24564MiB |     88%      Default |
+-----------------------------------------+------------------------+----------------------+
|   2  NVIDIA GeForce RTX 4090 D      On  |   00000000:5A:00.0 Off |                  Off |
| 30%   38C    P2             89W /  425W |    1176MiB /  24564MiB |     10%      Default |
+-----------------------------------------+------------------------+----------------------+
|   3  NVIDIA GeForce RTX 4090 D      On  |   00000000:99:00.0 Off |                  Off |
| 38%   57C    P2            235W /  425W |    8313MiB /  24564MiB |     78%      Default |
+-----------------------------------------+------------------------+----------------------+
|   4  NVIDIA GeForce RTX 4090 D      On  |   00000000:A8:00.0 Off |                  Off |
| 30%   56C    P2            169W /  425W |    7205MiB /  24564MiB |     62%      Default |
+-----------------------------------------+------------------------+----------------------+
|   5  NVIDIA GeForce RTX 4090 D      On  |   00000000:B8:00.0 Off |                  Off |
| 30%   55C    P2            393W /  425W |    7257MiB /  24564MiB |     90%      Default |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|    0   N/A  N/A          825638      C   python                                 8072MiB |
|    1   N/A  N/A          830115      C   python                                 8272MiB |
|    2   N/A  N/A          823710      C   python                                  586MiB |
|    2   N/A  N/A          826502      C   python                                  576MiB |
|    3   N/A  N/A          822390      C   python                                 8304MiB |
|    4   N/A  N/A          831353      C   python                                 7196MiB |
|    5   N/A  N/A          831033      C   python                                 7248MiB |
+-----------------------------------------------------------------------------------------+
---PROCESS_MAP---
=== GPU 0 ===
825638, 8072 MiB
PID 825638: python exp001/evaluate.py --model-path /root/autodl-tmp/models/LLM-Research/Llama-3___2-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Llama-3.2-3B_d005_s42/lora_adapter --benchmarks mmlu gsm8k
=== GPU 1 ===
830115, 8272 MiB
PID 830115: python compute_signals.py --model-path /root/autodl-tmp/exp001/checkpoints/Llama-3.2-3B_d000_s42/merged --benchmark mmlu --signal all --output-dir /root/autodl-tmp/exp002/signals/Llama-3.2-3B_d000_s42
=== GPU 2 ===
823710, 586 MiB
826502, 576 MiB
PID 823710: python compute_signals.py --model-path /root/autodl-tmp/models/Qwen2.5-1.5B-Instruct --benchmark arc_challenge --signal all --output-dir /root/autodl-tmp/exp002/signals/Qwen2.5-1.5B-Instruct/ --batch-
PID 826502: python compute_signals.py --model-path /root/autodl-tmp/models/Qwen2.5-1.5B-Instruct --benchmark arc_challenge --signal all --output-dir /root/autodl-tmp/exp002/signals/Qwen2.5-1.5B-Instruct/ --batch-
=== GPU 3 ===
822390, 8304 MiB
PID 822390: python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/exp001/checkpoints/Llama-3.2-3B_d025_s42/merged --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format alig
=== GPU 4 ===
831353, 7196 MiB
PID 831353: python compute_signals.py --model-path /root/autodl-tmp/exp001/checkpoints/Llama-3.2-3B_d000_s42/merged --benchmark arc_challenge --signal all --output-dir /root/autodl-tmp/exp002/signals/Llama-3.2-3B
=== GPU 5 ===
831033, 7356 MiB
PID 831033: python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/exp001/checkpoints/Llama-3.2-3B_d100_s42/merged --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format alig
```

**注意：GPU 2 有两个进程（PID 823710 和 826502）写同一个 output-dir `Qwen2.5-1.5B-Instruct/`，疑似重复。**

---
