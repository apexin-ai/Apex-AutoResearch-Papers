# analysis gpu1 nora diagnosis

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gpu1_nora_diagnosis_20260521T014730_result.json`
- **Structured JSON:** [`11d02a39ed1609310cc1.json`](../../sessions/11/11d02a39ed1609310cc1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告 — westd-19183 (2026-05-21 09:47 UTC)

### GPU 状态

| GPU | 型号 | 显存 | 进程 | 状态 |
|-----|------|------|------|------|
| cuda:0 | RTX PRO 6000 Black (96GB) | 15149MiB / 97887MiB | PID 513523 (python) | LIBERO-Object pipeline 运行中 |
| cuda:1 | RTX PRO 6000 Black (96GB) | 0MiB / 97887MiB | 无 | **空闲** |

### LIBERO-Object Pipeline

- **Phase 1** (数据采集): 完成，5000 samples，耗时 249s
- **Phase 2** (action R2 probing): 进行中
  - L0 结果已出: `img_mean R2=0.6952, last_pre R2=0.5710`
  - L0 耗时 ~24 min (08:50→09:14)，当前时间 09:47，正在计算更深层
  - 如果模型有 32 层，Phase 2 预计还需 **~12 小时**

### NORA 环境 — **未就绪**

- venv 已创建 (3.2GB)，CUDA 依赖包 (cuda_toolkit-12.8, triton-3.6.0, nvidia-* libs, torchaudio-2.11.0+cu128) 已装
- **torch 本体未安装** — site-packages 下无 torch 目录
- 原因: **数据盘已满**，pip install torch 时空间不足

### 下载任务

| 资源 | 大小 | 状态 |
|------|------|------|
| qwen25-vl-3b-base | 7.1GB | 完成 |
| nora-libero-goal | 5.1GB | 完成 |
| openvla-7b-oft-finetuned-libero-10 | 817MB | **不完整** — 有 config/tokenizer/lora_adapter，但 model.safetensors 分片缺失 |

### 磁盘 — **危急**

| 挂载点 | 容量 | 已用 | 可用 | 状态 |
|--------|------|------|------|------|
| / (根分区) | 30GB | 24GB | 6.5GB | 79% |
| /root/autodl-tmp (数据盘) | 250GB | 250GB | **786MB** | **100% 满** |

数据盘主要占用:
- checkpoints: 64GB
- data: 37GB
- results: 18GB
- HF cache: 8.6GB
- NORA env: 3.2GB

### 关键阻塞

**数据盘满是根因**，同时阻塞了:
1. NORA PyTorch 安装（~2.5GB torch wheel 无法写入）
2. LIBERO-Long checkpoint 下载（model safetensors 分片无法下载）

需要释放至少 **20-30GB** 空间才能继续两项工作。可考虑清理 HF cache (8.6GB) 和不再需要的旧 checkpoint。

---
