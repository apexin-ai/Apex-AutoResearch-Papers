# diag 41312 hostname verify

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_41312_hostname_verify_20260518T145527_result.json`
- **Structured JSON:** [`8ca8d34926cdc67f7c50.json`](../../sessions/8c/8ca8d34926cdc67f7c50.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告 — westd-41312

### 服务器状态
- **GPU**: 4x NVIDIA RTX PRO 6000 Blackwell (98GB VRAM each), 全部空闲
- **PyTorch**: 2.10.0+cu128, CUDA 可用
- **数据/代码**: 全部就位

### 磁盘：100% 满，无法启动训练
```
/root/autodl-tmp: 250G / 250G used (68K free)
```

**空间明细 (224G 在 output/models/):**

| 目录 | 大小 | 状态 |
|------|------|------|
| uniform_1_7b_seed42 | 39G (4 checkpoints × ~9.7G) | 需 resume from checkpoint-3000 |
| adaptive_1_7b_seed42 | 29G (3 checkpoints × ~9.7G) | 需 resume from checkpoint-2500 |
| llama3b_uniform_seed42 | 25G | 已完成 (checkpoint-6103) |
| llama3b_adaptive_seed42 | 25G | 已完成 (checkpoint-6103) |
| contamination_60_* (6个) | ~57G | 已完成 (checkpoint-6103) |
| 0.6B 模型 (grid/ess/hybrid 等 ~10个) | ~46G | 已完成 |
| 其他 (uniform_seed42, adaptive_fix) | ~5G | 已完成 |

### Checkpoint 路径（resume 用）
- **uniform_1_7b**: `/root/autodl-tmp/provenance_weight_training/output/models/uniform_1_7b_seed42/checkpoint-3000`
- **adaptive_1_7b**: `/root/autodl-tmp/provenance_weight_training/output/models/adaptive_1_7b_seed42/checkpoint-2500`

### 可安全删除释放空间的方案

**方案 A — 最小清理 (~39G)：** 删除活跃训练目录中的旧 checkpoint（只保留最新的用于 resume）
- uniform_1_7b: 删 checkpoint-1500, 2000 → ~19.4G
- adaptive_1_7b: 删 checkpoint-1500, 2000 → ~19.4G

**方案 B — 大幅清理：** 在方案 A 基础上，删除已完成实验的模型（需你确认哪些可删）
- llama3b_* → +50G
- contamination_60_* → +57G
- 0.6B grid/ess/hybrid → +46G

**请指示：** 清理哪些模型？我可以立即执行并启动训练。

---
