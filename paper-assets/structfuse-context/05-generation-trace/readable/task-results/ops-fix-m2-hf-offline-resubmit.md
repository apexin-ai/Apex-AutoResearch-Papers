# ops fix m2 hf offline resubmit

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-m2-hf-offline-resubmit_20260513T015621_result.json`
- **Structured JSON:** [`984b63eed89034b7c8ed.json`](../../sessions/98/984b63eed89034b7c8ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 0 稳定运行在 17 GiB / 100% 利用率，已持续数分钟无 OOM。训练正常运行中，只是尚未到第 50 步（首次打印 loss）。gradient checkpointing + batch_size=2 + 3B 模型，每步约 5-10 秒，50 步约需 5-8 分钟。

---

## 汇报

### 1. 崩溃原因
- **v2 实际崩溃原因**：`wandb.errors.UsageError: No API key configured`（wandb 未设置离线模式）
- **不是** HF tokenizer 下载超时

### 2. 本地缓存状态
- HF cache snapshot `09d9bc5d376b0cfa0100a0694ea7de7232525803`：**shard 1 缺失**（`.incomplete`），shard 2 + tokenizer 完整
- **完整模型副本**存在于 `/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B/`（两个 shards + 所有 tokenizer/config 文件齐全）

### 3. 方案选择
**方案 A**（使用本地完整模型路径），无需额外下载

### 4. 修复内容
| 修改项 | 原值 | 新值 |
|--------|------|------|
| `MODEL` | `Qwen/Qwen2.5-Coder-3B` | `/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B` |
| `WANDB_MODE` | 已有 `offline` | 保留 |
| `HF_HOME` | 无 | `/root/autodl-tmp/.hf_cache` |
| `TRANSFORMERS_OFFLINE` | 无 | `1` |
| `HF_HUB_OFFLINE` | 无 | `1` |
| `PYTORCH_CUDA_ALLOC_CONF` | 无 | `expandable_segments:True` |
| `--batch-size` | `8` | `2`（原值 OOM） |

### 5. 重新提交
- **exp_id**: `m2_early_pilot_v3`
- **PID**: `897651`
- **GPU**: `cuda:0`（原指定 cuda:4 被其他进程占用 9.26 GiB）

### 6. 训练启动状态
- 模型加载成功（2/2 shards）
- 进入 Epoch 1 random 策略训练
- GPU 0 显存 17 GiB / 24.5 GiB，利用率 100%，运行稳定无 OOM
- 尚未到 step 50（首次 loss 打印点），但进程健康

**注意**：batch_size 从 8 降至 2，有效 batch size 下降 4 倍。如果训练效果不理想，后续可考虑在训练代码中添加 gradient accumulation 支持。

---
