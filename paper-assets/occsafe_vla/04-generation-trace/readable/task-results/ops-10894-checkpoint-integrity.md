# ops 10894 checkpoint integrity

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_10894_checkpoint_integrity_20260524T175256_result.json`
- **Structured JSON:** [`3d1130b21b72b20d7f56.json`](../../sessions/3d/3d1130b21b72b20d7f56.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Checkpoint 完整性报告

### 1. full_occ_ln_s1

| 步数 | 状态 | 详情 |
|------|------|------|
| **30000** | **不完整** | .pt 文件 OK (action_head 288MB/16keys, occ_head 2.3MB/12keys, proprio_projector 64MB/4keys)；lora_adapter OK (462MB/879keys)；**model shard 2/4 CORRUPT** (52MB 截断，应~4.7GB)，shard 3-4 缺失，index.json 缺失 |
| **20000** | **完整** | 全部 .pt OK，lora_adapter OK，4/4 model shards，index.json 存在 |
| **10000** | 已删除 | — |

### 2. full_occ_ln_s2

| 步数 | 状态 | 详情 |
|------|------|------|
| **30000** | **严重不完整** | 仅有 tokenizer/config 文件 + 部分 lora_adapter（无 adapter_config.json）；**无 .pt 文件，无 model shards** |
| **20000** | **完整** | 全部 .pt OK，lora_adapter OK，4/4 model shards，index.json 存在 |
| **10000** | 已删除 | — |

### 3. ablation_occ_detach_s0_retrain

| 步数 | 状态 | 详情 |
|------|------|------|
| **30000** | **严重不完整** | 仅有 tokenizer/config 文件；**无 lora_adapter，无 .pt 文件，无 model shards** |
| **20000** | **完整** | 全部 .pt OK (occ_head 18keys vs 其他实验12keys)，lora_adapter OK，4/4 model shards，index.json 存在 |
| **10000** | 已删除 | — |

### 4. full_occ_ln_s0（参考，仍在运行）

| 步数 | 状态 | 详情 |
|------|------|------|
| **30000** | **完整** | 全部 .pt OK，4/4 model shards，index.json 存在 |
| **20000** | 已删除 | — |
| **10000** | 已删除 | — |

### 结论

- **3 个崩溃实验的 30000 步 checkpoint 均不可用**，磁盘满导致保存中途中断
- **3 个实验的 20000 步 checkpoint 均完整可用**，可从 20000 步恢复训练
- s1 的 30000 步 .pt 文件（action_head / occ_head / proprio_projector）和 lora_adapter 单独完整，但缺基座模型分片，无法直接用于推理
- 磁盘当前 102G/250G (41%)，空间已恢复充足
- 所有实验的 10000 步 checkpoint 已被训练进程自动清理

---
