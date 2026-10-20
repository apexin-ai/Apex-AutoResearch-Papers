# infra diagnose env

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_diagnose_env_20260520T180238_result.json`
- **Structured JSON:** [`c693e5052b08c5806524.json`](../../sessions/c6/c693e5052b08c5806524.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整诊断结果：

```
=== TORCH ===
torch=2.7.0+cu128, cuda=True, gpus=4

=== VLLM ===
ModuleNotFoundError: No module named 'vllm'

=== PIP LIST ===
nvidia-cublas-cu12                       12.8.3.14
nvidia-cuda-cupti-cu12                   12.8.57
nvidia-cuda-nvrtc-cu12                   12.8.61
nvidia-cuda-runtime-cu12                 12.8.57
nvidia-cudnn-cu12                        9.7.1.26
nvidia-cufft-cu12                        11.3.3.41
nvidia-cufile-cu12                       1.13.0.11
nvidia-curand-cu12                       10.3.9.55
nvidia-cusolver-cu12                     11.7.2.55
nvidia-cusparse-cu12                     12.5.7.53
nvidia-cusparselt-cu12                   0.6.3
nvidia-ml-py                             13.595.45
nvidia-nccl-cu12                         2.26.2
nvidia-nvjitlink-cu12                    12.8.61
nvidia-nvtx-cu12                         12.8.55
torch                                    2.7.0+cu128
torchaudio                               2.11.0+cu128
torchvision                              0.22.0+cu128

=== DISK ===
Filesystem      Size  Used Avail Use% Mounted on
overlay          30G   24G  6.5G  79% /
/dev/md0        350G  8.4G  342G   3% /root/autodl-tmp

=== RUNNING ===
(无正在运行的下载/安装进程)
```

摘要：
- **PyTorch 2.7.0+cu128**，4 GPU，CUDA 可用
- **vLLM 未安装**，flash-attn 未安装
- **根分区 79% 已用（剩 6.5G）**，数据盘 342G 空闲
- 无后台安装进程

---
