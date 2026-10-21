# status plan 002 progress

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_plan-002-progress_20260514T210725_result.json`
- **Structured JSON:** [`a416ba5633c5d452e36b.json`](../../sessions/a4/a416ba5633c5d452e36b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Plan-002 进度汇报

### 1. 运行中实验进度

| 实验 | 进度 | 速度 | 预估剩余时间 |
|------|------|------|-------------|
| OLMo-2 shard0 (PID 108242) | **442/497 (89%)** | ~8.5s/it | ~8 min |
| OLMo-2 shard1 (PID 108452) | **423/498 (85%)** | ~9.2s/it | ~12 min |
| Qwen3-1.7B shard0 (PID 111533) | **72/498 (14%)** | ~13s/it | ~92 min (~1.5h) |
| Qwen3-1.7B shard1 (PID 111646) | **66/498 (13%)** | ~13s/it | ~94 min (~1.6h) |

4 个进程全部存活，运行正常。OLMo-2 两个 shard 约 10 分钟内完成；Qwen3-1.7B 约 1.5 小时后完成。

### 2. Pythia-1B 数据完整性

- `generations_shard0.jsonl`: 2,286 行
- `generations_shard1.jsonl`: 2,269 行
- **已合并**: `generations.jsonl` (4.9MB)，无 `generations_merged.jsonl`（合并文件命名为 `generations.jsonl`）
- 数据格式正确：包含 id, depth, text, seed_id, token_count, model 字段

### 3. 评估脚本就绪状态

| 脚本 | 状态 | 用途 |
|------|------|------|
| `extract_features_multi.py` | 就绪 | 多生成器特征提取，支持增量模式 |
| `cross_generator_eval.py` | 就绪 | Leave-one-generator-out CV + Leave-one-family-out |
| `classify_multi.py` | 就绪 | 多生成器分类 |
| `ablation_analysis.py` | 就绪 | 消融分析 |
| `merge_shards.py` | 就绪 | shard 合并 |

所有评估脚本已就绪，等数据生成完成即可运行。

### 4. Qwen3-0.6B 模型

**已下载完成**。`model.safetensors` = 1.19GB，配置文件齐全（config.json, tokenizer.json, generation_config.json 等）。

### 5. GPU 利用率

| GPU | 型号 | 利用率 | 显存 |
|-----|------|--------|------|
| 0 | RTX 5090 | 42% | 3,977 / 32,607 MiB |
| 1 | RTX 5090 | 43% | 3,977 / 32,607 MiB |
| 2 | RTX 5090 | 49% | 3,623 / 32,607 MiB |
| 3 | RTX 5090 | 44% | 3,623 / 32,607 MiB |

4 卡均在使用中，显存占用较低（~12%），利用率中等（42-49%）。OLMo-2 完成后 GPU 2/3 将释放，可立即启动 Qwen3-0.6B 的数据生成。

---
