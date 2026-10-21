# verify ced s42 s44 checkpoints

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_ced_s42_s44_checkpoints_20260516T023959_result.json`
- **Structured JSON:** [`aa90bfb49d44e571aee1.json`](../../sessions/aa/aa90bfb49d44e571aee1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

## Checkpoint 路径验证

### 标准化路径
- `rsft_output_ced_s42/` — **不存在**
- `rsft_output_ced_s44/` — **不存在**
- `rsft_output_ced_s43/checkpoint-510` — 存在 ✓
- `rsft_output_ced_s45/checkpoint-510` — 存在 ✓

### 旧路径分析

| 目录 | 最大 checkpoint | lora_alpha | 完整训练? |
|------|----------------|------------|----------|
| `rsft_output/` | **510** | 128 | ✓ |
| `rsft_output_s44/` | **510** | 128 | ✓ |
| `rsft_output_r2b/` | 160 | **32** | ✗ |
| `rsft_output_r2a/` | 160 | 128 | ✗ |

### 结论

**CED s42 正确路径：`/root/autodl-tmp/rsft_output/checkpoint-510`**
- seed 42（脚本默认值），lora_alpha=128，完整 510 步训练
- 旧 eval 用的 `rsft_output_r2b` **是错的**：lora_alpha=32 且只训了 160 步，是不同超参的 round 2 实验

**CED s44 正确路径：`/root/autodl-tmp/rsft_output_s44/checkpoint-510`**
- lora_alpha=128，完整 510 步训练，与 ced_s43/ced_s45 配置一致
- 旧 eval 用的路径和这个一致，只是缺 `checkpoint-510` 后缀（用的是根目录 adapter）

### 四个 seed 的完整路径

| Seed | Checkpoint 路径 |
|------|----------------|
| 42 | `/root/autodl-tmp/rsft_output/checkpoint-510` |
| 43 | `/root/autodl-tmp/rsft_output_ced_s43/checkpoint-510` |
| 44 | `/root/autodl-tmp/rsft_output_s44/checkpoint-510` |
| 45 | `/root/autodl-tmp/rsft_output_ced_s45/checkpoint-510` |

---
