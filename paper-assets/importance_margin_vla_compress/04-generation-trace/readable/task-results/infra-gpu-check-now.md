# infra gpu check now

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gpu-check-now_20260515T143923_result.json`
- **Structured JSON:** [`b9e28c91920f4be2015a.json`](../../sessions/b9/b9e28c91920f4be2015a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总结果：

---

**1. nvidia-smi**
```
Fri May 15 22:39:51 2026       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 580.95.05              Driver Version: 580.95.05      CUDA Version: 13.0     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|=========================================+========================+======================|
|   0  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:B8:00.0 Off |                  Off |
| N/A   36C    P0             86W /  600W |     559MiB /  97887MiB |      0%      Default |
|   1  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:C8:00.0 Off |                  Off |
| N/A   30C    P8             35W /  600W |       3MiB /  97887MiB |      0%      Default |
+-----------------------------------------+------------------------+----------------------+
| Processes:                                                                              |
|    0   N/A  N/A           18717      C   python3                                 550MiB |
+-----------------------------------------------------------------------------------------+
```

**2. ps aux | grep train.py | grep -v grep**
```
（无输出 — 没有 train.py 进程在运行）
```

**3. tail -30 ~/runs/importance_margin_vla_compress/mvp_baseline.log**
```
OSError: Can't load the model for 'HuggingFaceTB/SmolVLM2-500M-Video-Instruct'. If you were trying to load it from 'https://huggingface.co/models', make sure you don't have a local directory with the same name. Otherwise, make sure 'HuggingFaceTB/SmolVLM2-500M-Video-Instruct' is the correct path to a directory containing a file named pytorch_model.bin.
EXIT_CODE=1
```

**4. tail -30 ~/runs/importance_margin_vla_compress/mvp_imm_anchor.log**
```
（同上，相同的 OSError）
OSError: Can't load the model for 'HuggingFaceTB/SmolVLM2-500M-Video-Instruct'.
EXIT_CODE=1
```

---

两个训练都因模型加载失败而崩溃，没有 train.py 进程在跑。GPU 0 上有个占 550MiB 的 python3 进程（PID 18717），但不是 train.py。根本原因是 `HuggingFaceTB/SmolVLM2-500M-Video-Instruct` 模型文件未下载到本地或路径不对。

---
