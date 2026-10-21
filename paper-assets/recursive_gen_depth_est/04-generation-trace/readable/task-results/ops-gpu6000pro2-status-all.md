# ops gpu6000pro2 status all

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu6000pro2-status-all_20260518T114505_result.json`
- **Structured JSON:** [`fb768484935e154fd139.json`](../../sessions/fb/fb768484935e154fd139.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇总

### 实验 1: gpt2xl_seed43_001 (PID 857779) — 运行中

- **进程**: 存活
- **当前阶段**: Step 6 — 生成 depth_3 (加载 gpt2-xl + LoRA adapters)
- **已完成**:
  - depth_0/1/2 各 5000 samples ✓
  - depth_2 LoRA 训练完成 (final loss: 1.3255, 3 epochs, 681s)
  - LoRA adapter 保存至 `checkpoints/gpt2xl_seed43/lora_depth_2` ✓
- **depth_3 生成进度**: 2718/5000 samples (~54%)
- **无 summary.json** — 尚未跑完全部 pipeline

### 实验 2: qwen25_14b_scale_002 (PID 806751) — 失败/卡住

- **进程**: 存活，但**模型下载失败**
- **数据**: depth_0/1/2 各 5000 samples (这些可能是之前生成的)
- **失败原因**: 从 hf-mirror.com 下载 `model-00005-of-00008.safetensors` 时 SSL/TLS handshake failure，aria2 返回 EXIT_CODE=1
- **无 results 目录** — pipeline 未进入评估阶段

实验 2 需要重新下载模型 shard 5/8 或换下载方式后重启。

---
