# ssh pipeline prep verify

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_pipeline-prep-verify_20260515T020801_result.json`
- **Structured JSON:** [`6aeb10da6bf41d061ef3.json`](../../sessions/6a/6aeb10da6bf41d061ef3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## RSFT 后处理 Pipeline 验证报告

### 组件就绪状态

| 组件 | 状态 | 备注 |
|------|------|------|
| `rsft_generate.py` | ✅ 运行中 | 4 shard 并行，输出格式含所有必要字段 |
| `merge_shards.py` | ✅ 已创建 | 原不存在，已写入服务器 + 本地。按 `(doc_id, generation_idx)` 去重 |
| `rsft_score_filter.py` | ✅ import 正常 | 输入字段与生成输出完全兼容 |
| CED/NLI 模型 | ✅ 离线加载正常 | dry-run 通过，p_pos=0.993 |
| `rsft_trainer.py` | ✅ import 正常 | bf16 ✅ lora_rank=64 ✅ lora_alpha=128 ✅ 无量化 ✅ |
| 字段兼容性 | ✅ 全链路匹配 | generate→score_filter→trainer 三级 I/O 格式一致 |

### 关键注意事项

运行 score_filter 和 trainer 时**必须**设置环境变量（HF 网络不可达）：
```bash
export HF_HOME=/root/autodl-tmp/.hf_cache
export HF_HUB_OFFLINE=1
export TRANSFORMERS_OFFLINE=1
```

Python 路径：`/root/miniconda3/bin/python`（`python3` 不在 PATH）

### 生成完成后执行命令序列

```bash
# Step 1: Merge
cd /root/autodl-tmp && python -m freige.training.merge_shards \
    --shard_dir /root/autodl-tmp/rsft_generations \
    --output /root/autodl-tmp/rsft_generations/generations_merged.jsonl

# Step 2: Score & Filter (用 GPU 加速 NLI)
cd /root/autodl-tmp && python -m freige.training.rsft_score_filter \
    --input_dir /root/autodl-tmp/rsft_generations_merged \
    --output_path /root/autodl-tmp/rsft_filtered \
    --selection_strategy top_pct --top_pct 25

# Step 3: RSFT Training (4 GPU)
cd /root/autodl-tmp && accelerate launch --num_processes 4 \
    -m freige.training.rsft_trainer \
    --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train.jsonl \
    --output_dir /root/autodl-tmp/rsft_output
```

**注意**：Step 2 的 `--input_dir` 需要指向包含 `generations_merged.jsonl` 的目录，但 `load_generations()` 硬编码读 `generations.jsonl`。需要改名或做符号链接：
```bash
mkdir -p /root/autodl-tmp/rsft_generations_merged
ln -s /root/autodl-tmp/rsft_generations/generations_merged.jsonl \
      /root/autodl-tmp/rsft_generations_merged/generations.jsonl
```

### 当前生成进度快照

| 来源 | 已完成 lines | 已完成 docs | 分配范围 | 总 docs | 进度 |
|------|-------------|------------|---------|---------|------|
| top-level (旧) | 2,416 | 302 | idx 0-301 | 302 | 100% |
| shard_0 | 1,048 | ~131 | idx 302-983 | 682 | 19% |
| shard_1 | 1,120 | ~140 | idx 984-1664 | 681 | 21% |
| shard_2 | 1,104 | ~138 | idx 1665-2345 | 681 | 20% |
| shard_3 | 696 | ~87 | idx 2346-3026 | 681 | 13% |
| **合计** | **6,384** | **~791** | | **3,027** | **26%** |

- 去重后: 6,328 条有效记录
- 120 条重复（top-level 与 shard_0 重叠区域）

### 预估完成时间

各 shard 生成速率约 4.1-4.7 docs/min。瓶颈是 shard_3（启动最晚、剩余最多）。

**预计全部完成：约 2-2.5 小时后**（~12:00-12:30 UTC）

---
