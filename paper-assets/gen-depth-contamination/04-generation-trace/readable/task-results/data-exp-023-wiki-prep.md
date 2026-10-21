# data exp 023 wiki prep

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_exp_023_wiki_prep_20260516T080040_result.json`
- **Structured JSON:** [`07a3b873a06e19e588c2.json`](../../sessions/07/07a3b873a06e19e588c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. Wikipedia 数据
- **路径**: `/root/autodl-tmp/gen-depth-contamination/data/exp_023_wiki/depth_0.jsonl`
- **行数**: 5000
- **来源**: `wikimedia/wikipedia` 20231101.en，streaming 前 ~5300 篇，跳过 282 篇短文（<500 字符）

### 2. 格式验证
- 字段: `text`, `doc_id` — 与 C4 seed data 完全一致
- 文本长度: min=502, max=1701, avg=1070 chars
- doc_id: 0-4999 连续
- 已用 Qwen2.5-1.5B tokenizer 截断到 256 tokens

### 3. 运行脚本
- **路径**: `/root/autodl-tmp/gen-depth-contamination/scripts/exp023_wiki_domain.sh`
- 配置: Qwen2.5-1.5B base, continuation, 5K docs, depth 0-5, batch=16, cuda:3
- 设置 `HF_DATASETS_OFFLINE=1` + `TRANSFORMERS_OFFLINE=1` 阻断网络
- 包含 seed data 存在性检查

### 4. Dry-run
- `bash -n` 语法检查: PASS
- 模型路径 `/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B`: 存在
- Seed data 文件: 存在，5000 行

### 5. 注意事项
- cuda:3 当前跑 exp-021 (PID 20982)，等完成后直接执行 `bash scripts/exp023_wiki_domain.sh`
- 下载时出现 GIL 退出警告，但数据完整无损（datasets 库已知问题）
- 预计运行时间 ~2-3h（5K docs × 6 depths，与 exp-016 类似）

---
