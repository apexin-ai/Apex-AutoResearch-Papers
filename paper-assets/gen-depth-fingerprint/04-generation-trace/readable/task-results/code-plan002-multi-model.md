# code plan002 multi model

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan002-multi-model_20260514T185438_result.json`
- **Structured JSON:** [`9b7bb2cecd94cbd39e46.json`](../../sessions/9b/9b7bb2cecd94cbd39e46.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 报告

### 1. Qwen 模型确认

| 模型 | Repo ID | 参数量 | 本地路径 |
|------|---------|--------|---------|
| Qwen3-1.7B-Base | `Qwen/Qwen3-1.7B-Base` | 1721M | `/root/autodl-tmp/models/Qwen/Qwen3-1___7B-Base` |
| Qwen3-0.6B-Base | `Qwen/Qwen3-0.6B-Base` | 596M | `/root/autodl-tmp/models/Qwen/Qwen3-0___6B-Base` |

### 2. Dry-run 结果

| 模型 | 状态 | Records | Skipped | 耗时 |
|------|------|---------|---------|------|
| pythia-1b | **PASS** | 10 | 0 | 12.0s |
| olmo-2-1b | **PASS** | 10 | 0 | 19.3s |
| qwen3-1.7b | **PASS** | 10 | 0 | 29.6s |
| qwen3-0.6b | **PASS** | 7 | 1 | 13.1s |

qwen3-0.6b 在 seed 0 depth 2 生成了空输出，属小模型正常行为，代码已正确处理（skip + continue）。

### 3. 完整运行命令（4 shard）

```bash
cd /root/gen-depth-fingerprint
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

# pythia-1b
python generate_chain.py --model-name pythia-1b --model-path /root/autodl-tmp/models/pythia-1b/EleutherAI/pythia-1b --shard-id 0 --num-shards 4 --device cuda:0
python generate_chain.py --model-name pythia-1b --model-path /root/autodl-tmp/models/pythia-1b/EleutherAI/pythia-1b --shard-id 1 --num-shards 4 --device cuda:1
python generate_chain.py --model-name pythia-1b --model-path /root/autodl-tmp/models/pythia-1b/EleutherAI/pythia-1b --shard-id 2 --num-shards 4 --device cuda:2
python generate_chain.py --model-name pythia-1b --model-path /root/autodl-tmp/models/pythia-1b/EleutherAI/pythia-1b --shard-id 3 --num-shards 4 --device cuda:3

# olmo-2-1b
python generate_chain.py --model-name olmo-2-1b --model-path /root/autodl-tmp/models/olmo-2-1b-hf/allenai/OLMo-2-0425-1B --shard-id 0 --num-shards 4 --device cuda:0
python generate_chain.py --model-name olmo-2-1b --model-path /root/autodl-tmp/models/olmo-2-1b-hf/allenai/OLMo-2-0425-1B --shard-id 1 --num-shards 4 --device cuda:1
python generate_chain.py --model-name olmo-2-1b --model-path /root/autodl-tmp/models/olmo-2-1b-hf/allenai/OLMo-2-0425-1B --shard-id 2 --num-shards 4 --device cuda:2
python generate_chain.py --model-name olmo-2-1b --model-path /root/autodl-tmp/models/olmo-2-1b-hf/allenai/OLMo-2-0425-1B --shard-id 3 --num-shards 4 --device cuda:3

# qwen3-1.7b
python generate_chain.py --model-name qwen3-1.7b --model-path /root/autodl-tmp/models/Qwen/Qwen3-1___7B-Base --shard-id 0 --num-shards 4 --device cuda:0
python generate_chain.py --model-name qwen3-1.7b --model-path /root/autodl-tmp/models/Qwen/Qwen3-1___7B-Base --shard-id 1 --num-shards 4 --device cuda:1
python generate_chain.py --model-name qwen3-1.7b --model-path /root/autodl-tmp/models/Qwen/Qwen3-1___7B-Base --shard-id 2 --num-shards 4 --device cuda:2
python generate_chain.py --model-name qwen3-1.7b --model-path /root/autodl-tmp/models/Qwen/Qwen3-1___7B-Base --shard-id 3 --num-shards 4 --device cuda:3

# qwen3-0.6b
python generate_chain.py --model-name qwen3-0.6b --model-path /root/autodl-tmp/models/Qwen/Qwen3-0___6B-Base --shard-id 0 --num-shards 4 --device cuda:0
python generate_chain.py --model-name qwen3-0.6b --model-path /root/autodl-tmp/models/Qwen/Qwen3-0___6B-Base --shard-id 1 --num-shards 4 --device cuda:1
python generate_chain.py --model-name qwen3-0.6b --model-path /root/autodl-tmp/models/Qwen/Qwen3-0___6B-Base --shard-id 2 --num-shards 4 --device cuda:2
python generate_chain.py --model-name qwen3-0.6b --model-path /root/autodl-tmp/models/Qwen/Qwen3-0___6B-Base --shard-id 3 --num-shards 4 --device cuda:3

# 合并（每个模型跑完后）
python merge_shards.py --model-name pythia-1b --num-shards 4
python merge_shards.py --model-name olmo-2-1b --num-shards 4
python merge_shards.py --model-name qwen3-1.7b --num-shards 4
python merge_shards.py --model-name qwen3-0.6b --num-shards 4
```

### 4. 代码改动摘要

**generate_chain.py**：新增 `--model-name`（默认 pythia-2.8b）和 `--model-path`（默认 None → 回退 Pythia-2.8B）。输出路径改为 `data/{model_name}/`。添加 `trust_remote_code=True`、pad_token 兼容处理、输出记录含 `"model"` 字段。不指定新参数时行为与原版一致。

**merge_shards.py**：新增 `--model-name`。指定时从 `data/{model_name}/` 读取 shard，不指定时行为不变。

---
