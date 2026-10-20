# setup nora spatial ckpt and verify v2

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_setup_nora_spatial_ckpt_and_verify_v2_20260521T032819_result.json`
- **Structured JSON:** [`dc7c43cb8fe8a365d5f5.json`](../../sessions/dc/dc7c43cb8fe8a365d5f5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Spatial 下载进程存活（PID 527351, 101秒）。

---

## 产出汇总

### 1. NORA Goal v2 运行状态：**ALIVE**

- PID 526939，CUDA:1，`nora_goal_full_pipeline.py --conditions trained untrained`
- 模型加载成功 (12.1s, 2 shards)
- Phase 1 representation extraction 进行中：**Task 2/10** (push_the_plate...), sample 1400/5000
- 预计速度：~21s/100 samples, 每 task 500 samples → 10 tasks × ~105s ≈ 17.5 分钟完成 Phase 1 trained
- 注意：CUDA:1 同时还跑着 `tracvla_spatial_full_pipeline.py --conditions trained` (PID 521842, CPU 1587%)，可能互相抢 GPU 显存

### 2. NORA Spatial checkpoint 下载：**已启动**

- 模型：`declare-lab/nora-long-finetuned-libero-spatial`
- 下载方式：`huggingface-cli download` via hf-mirror
- 当前进度：175MB / ~7.5GB (小文件完成，两个大 safetensors 分片下载中)
- PID 527351，后台运行
- 日志：`/tmp/download_nora_spatial.log`

### 3. NORA Goal checkpoint 完整性：**完整**

- shard 1: 4,959,940,464 bytes (4.6GB) ✓
- shard 2: 2,556,676,080 bytes (2.4GB) ✓
- 合计 7.52GB ≈ index total_size 7,516,524,544 + headers overhead
- Pipeline 已成功加载并正常使用
- aria2c (PID 523735) 仍在运行但文件大小不再增长，属残留进程，可安全 kill

---
