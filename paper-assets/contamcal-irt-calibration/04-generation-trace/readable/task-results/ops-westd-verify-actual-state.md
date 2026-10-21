# ops westd verify actual state

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-verify-actual-state_20260518T100953_result.json`
- **Structured JSON:** [`54d37472715eb87de671.json`](../../sessions/54/54d37472715eb87de671.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

原始输出：

```
===== 1. 下载状态 =====
Qwen2.5-7B: safetensors=4 incomplete=0 size=15G
Qwen2.5-14B: safetensors=5 incomplete=3 size=25G
phi-4: safetensors=0 incomplete=6 size=1.6G
OLMo-2-1124-7B: safetensors=1 incomplete=5 size=13G
gemma-2-9b: safetensors=4 incomplete=4 size=24G

===== 2. GPU 状态 =====
Mon May 18 18:10:30 2026
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 580.82.09              Driver Version: 580.82.09      CUDA Version: 13.0     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|=========================================+========================+======================|
|   0  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:16:00.0 Off |                  Off |
| N/A   71C    P0            452W /  600W |   63281MiB /  97887MiB |     91%      Default |
|   1  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:98:00.0 Off |                  Off |
| N/A   29C    P8             33W /  600W |       0MiB /  97887MiB |      0%      Default |
|   2  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:C8:00.0 Off |                  Off |
| N/A   30C    P8             33W /  600W |       0MiB /  97887MiB |      0%      Default |
|   3  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:D8:00.0 Off |                  Off |
| N/A   36C    P0            200W /  600W |       0MiB /  97887MiB |    100%      Default |
+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|    0   N/A  N/A           17819      C   python                                63272MiB |
+-----------------------------------------------------------------------------------------+

===== 3. 训练进程 =====
- tmux session: exp_001_sft_7b_d000_s42
- 主进程 PID 17819 (GPU 0, 63272MiB, 91% util)
- 命令: python exp001/train_sft.py --model-name Qwen2.5-7B --data-path sft_dosage_000.jsonl --output-dir Qwen2.5-7B_d000_s42 --seed 42 --gpu 0 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 2 --grad-accum 8 --epochs 1 --max-seq-length 2048
- 4个 dataloader worker 子进程 (PID 18265-18268)

===== 4. 7B Pilot checkpoint =====
total 0
drwxr-xr-x 3 root root 34 May 18 18:08 .
drwxr-xr-x 3 root root 41 May 18 18:07 ..
drwxr-xr-x 2 root root 10 May 18 18:08 lora_adapter

===== 5. 下载进程 =====
- download_all.sh (PID 5060) → 正在下载 Qwen2.5-14B (PID 5066, hf download)
- dl_gemma screen session (PID 6378) → 正在下载 gemma-2-9b (PID 6380, hf download)
```

**摘要：**

| 项目 | 状态 |
|---|---|
| **Qwen2.5-7B** | 下载完成 (4 safetensors, 15G, 0 incomplete) |
| **Qwen2.5-14B** | 下载中 (5 safetensors, 3 incomplete, 25G) |
| **phi-4** | 下载中 (0 safetensors, 6 incomplete, 1.6G) |
| **OLMo-2-1124-7B** | 下载中 (1 safetensors, 5 incomplete, 13G) |
| **gemma-2-9b** | 下载中 (4 safetensors, 4 incomplete, 24G) |
| **GPU 0** | 7B SFT 训练中 (PID 17819, 63.3G/97.9G, 91% util, lora_alpha=32) |
| **GPU 1** | 空闲 |
| **GPU 2** | 空闲 |
| **GPU 3** | 空闲 (0MiB 但 100% util — 可能刚释放或有 CPU-bound 进程) |
| **7B checkpoint** | 刚开始，仅有 lora_adapter 空目录 |

注意：GPU 3 显示 0MiB 显存但 100% GPU-Util，异常，可能有残留进程或刚释放。

---
