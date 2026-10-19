# ops training checkpoint inventory

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_training-checkpoint-inventory_20260513T104748_result.json`
- **Structured JSON:** [`c4eb1972f0e5af5b8871.json`](../../sessions/c4/c4eb1972f0e5af5b8871.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Checkpoint 盘点结果

### 磁盘总览

| 目录 | 大小 |
|------|------|
| `m2_embed_verify_output/` | 18G |
| `m2_starcoder_output/` | 23G |
| 数据盘 `/root/autodl-tmp/` | 60G / 250G (24%) |

---

### m2_embed_verify_output（Qwen2.5-Coder-3B, GPU 1）

| 子实验 | best | final | 大小 | 状态 |
|--------|------|-------|------|------|
| **random_s42** | ✅ | ✅ | 5.8G + 5.8G | ✅ 完成 |
| **embedding_s42** | ✅ | ❌ | 5.8G | 🔄 训练中（PID 37880, step ~1450） |
| **dataflow_s42** | ❌ 空目录 | ❌ | 0 | ❌ 失败（日志仅到 epoch 1 加载，无训练 step） |

### m2_starcoder_output（StarCoder2-3B, GPU 0）

| 子实验 | best | final | 大小 | 状态 |
|--------|------|-------|------|------|
| **random_s42** | ✅ | ❌ | 5.8G | ⚠️ 仅 best，日志 812B（可能 early stop 或只跑了 500 步） |
| **embedding_s42** | ✅ | ✅ | 5.8G + 5.8G | ✅ 完成 |
| **dataflow_s42** | ✅ | ❌ | 5.8G | 🔄 训练中（PID 43172, step ~800, epoch 2） |

---

### Checkpoint 内容

所有 checkpoint 保存的是**合并后的完整模型**（`model.pt` ~5.8G），不是 LoRA adapter。文件列表：

- **Qwen 系列**: `model.pt`, `training_config.json`, `tokenizer.json`, `tokenizer_config.json`, `vocab.json`, `merges.txt`, `special_tokens_map.json`, `added_tokens.json`, `chat_template.jinja`
- **StarCoder2 系列**: 同上但无 `added_tokens.json` 和 `chat_template.jinja`

---

### 问题项

1. **`m2_embed_verify/dataflow_s42`** — 训练失败，输出目录为空，需重跑
2. **`m2_starcoder/random_s42`** — 无 `final/` 目录，日志极短，需确认是否 early stop 正常结束
3. **无 plan013 独立输出目录** — `plan_013_starcoder.sh` 的产出实际写入了 `m2_starcoder_output/`

---
