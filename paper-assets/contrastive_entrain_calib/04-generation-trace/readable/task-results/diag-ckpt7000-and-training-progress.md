# diag ckpt7000 and training progress

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_ckpt7000-and-training-progress_20260521T081207_result.json`
- **Structured JSON:** [`c74e46f0f6bfc8bf4ed8.json`](../../sessions/c7/c74e46f0f6bfc8bf4ed8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已经齐了。以下是诊断报告：

---

## 诊断报告

### 1. ckpt-7000 eval 失败根因

**两次都是被 SIGTERM (EXIT_CODE=143) 外部杀死，不是自身崩溃。**

- **v1**: 模型加载成功，推理跑到 80/362 (~22分钟)后被杀
- **v2**: 模型加载时 accelerate 报 GPU 内存不足警告（"no modules could be assigned to device 0 due to insufficient memory: 2489319424 bytes required"），LoRA adapter 被 offload 到 CPU。加载 362 条数据后刚开始推理就被杀

根因判断：**GPU 显存不足导致 accelerate 将部分权重 offload 到 CPU → 推理变慢 → 被 job monitoring 系统判定超时后 SIGTERM 杀死**。v2 显存压力比 v1 更大（连 LoRA 都装不下），可能 westd-28034 当时有其他进程占用 GPU。

### 2. Checkpoint 完整性

**checkpoint-7000 完整，可以重试。**
- `adapter_model.safetensors`: 245,405,936 bytes（与 checkpoint-6000 完全一致）
- 所有文件齐全（adapter_config, tokenizer, optimizer, scheduler 等）
- 磁盘空间充足：262GB 可用

### 3. exp-003 训练进度

westd-29046 上有两个 seed 在并行训练：

| Run | 当前 step | 总 steps | 进度 | 最新 checkpoint |
|-----|-----------|----------|------|-----------------|
| **seed1** | 已过 7500 | 8000 | ~94% | checkpoint-7500 (May 21 14:10) |
| **seed2** (exp-003-s2.log) | 3641 | 8000 | 45.5% | checkpoint-3500 (May 21 15:00) |

seed1 checkpoint 列表：500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, **7500**
seed2 checkpoint 列表：500, 1000, 1500, 2000, 2500, 3000, **3500**

**seed1 预计再 ~3-4 小时完成（8000 step）。seed2 预计还需 ~35 小时。**

westd-28034 上的 eval 用 checkpoint 目录 `/root/autodl-tmp/checkpoints/exp003/` 只到 checkpoint-7000（无 7500/8000）。

### 4. 建议下一步

1. **ckpt-7000 重试**：确保 westd-28034 GPU 无其他进程占用后重跑。如果 GPU 显存太小（单张放不下 Qwen3-8B + LoRA），考虑加 `--max_memory` 参数或用 `dtype=float16` 减少显存占用
2. **同步新 checkpoint**：seed1 已产出 7500，需从 westd-29046 同步到 westd-28034 的 eval checkpoint 目录
3. **等 seed1 完成**：约 3-4 小时后产出 checkpoint-8000，届时全部 checkpoint 可一次性 eval

---
