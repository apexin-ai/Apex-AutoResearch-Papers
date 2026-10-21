# ssh gpu snapshot urgent

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gpu-snapshot-urgent_20260522T202759_result.json`
- **Structured JSON:** [`6eb6dceefd0add23f2f7.json`](../../sessions/6e/6eb6dceefd0add23f2f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**nvidia-smi:**
```
Sat May 23 04:28:19 2026       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 580.105.08             Driver Version: 580.105.08     CUDA Version: 13.0     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|=========================================+========================+======================|
|   0  NVIDIA GeForce RTX 5090        On  |   00000000:27:00.0 Off |                  N/A |
| 42%   32C    P8             15W /  575W |       0MiB /  32607MiB |      0%      Default |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA GeForce RTX 5090        On  |   00000000:49:00.0 Off |                  N/A |
| 41%   32C    P8             10W /  575W |       0MiB /  32607MiB |      0%      Default |
+-----------------------------------------+------------------------+----------------------+
|   2  NVIDIA GeForce RTX 5090        On  |   00000000:5A:00.0 Off |                  N/A |
| 52%   65C    P1            416W /  575W |   14413MiB /  32607MiB |     86%      Default |
+-----------------------------------------+------------------------+----------------------+
|   3  NVIDIA GeForce RTX 5090        On  |   00000000:A8:00.0 Off |                  N/A |
| 41%   33C    P8             14W /  575W |       0MiB /  32607MiB |      0%      Default |
+-----------------------------------------+------------------------+----------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|    2   N/A  N/A          211098      C   python3                               14404MiB |
+-----------------------------------------------------------------------------------------+
```

**ps aux | grep:**
```
root  211098 124 0.3 ... python3 train_unified.py --data_dir data/ --model_name_or_path /dev/shm/Qwen3-14B --task cwm --output_dir /root/autodl-tmp/checkpoints_cwm14b_func_s42/ --run_name cwm-qwen3-14b-qlora-func-s42 --seed 42 --max_seq_length 2048 --batch_size 1 --grad_accumulation 32 --lr 5e-5 --epochs 3 --quantize_4bit --no_wandb
root  211524  0.2 0.2 ... python3 train_unified.py [same args] (worker process)
root  211525  0.2 0.2 ... python3 train_unified.py [same args] (worker process)
root  211526  0.2 0.2 ... python3 train_unified.py [same args] (worker process)
root  211527  0.2 0.2 ... python3 train_unified.py [same args] (worker process)
```

GPU 2 上正在跑 `train_unified.py`（CWM 14B QLoRA func s42），PID 211098 主进程 + 4 个 worker，占用 14404MiB 显存，GPU 利用率 86%。

---
