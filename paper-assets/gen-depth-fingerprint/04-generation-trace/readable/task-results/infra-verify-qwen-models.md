# infra verify qwen models

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_verify-qwen-models_20260514T213316_result.json`
- **Structured JSON:** [`f401b617c7ec2fd399dc.json`](../../sessions/f4/f401b617c7ec2fd399dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. Qwen3-1.7B 模型 ✅ 就绪
- 路径: `/root/autodl-tmp/models/Qwen/Qwen3-1___7B-Base/`
- 大小: 3.3G，`model.safetensors` 3.4GB，含 config/tokenizer — 完整

### 2. Qwen3-0.6B 模型 ✅ 就绪
- 路径: `/root/autodl-tmp/models/Qwen/Qwen3-0___6B-Base/`
- 大小: 1.2G，`model.safetensors` 1.2GB，含 config/tokenizer — 完整

### 3. GPU ❌ 非空闲，4 张全在跑

| GPU | 利用率 | 显存占用 |
|-----|--------|----------|
| 0 | 39% | 3977 / 32607 MiB |
| 1 | 39% | 3977 / 32607 MiB |
| 2 | 32% | 1825 / 32607 MiB |
| 3 | 31% | 1823 / 32607 MiB |

### 4. 残留进程 ❌ 有 4 个 generate_chain.py 正在运行

| tmux session | 命令 | GPU | 启动时间 |
|-------------|------|-----|----------|
| plan-002-qwen17b-retry-s0 | `generate_chain.py --model-name qwen3-1.7b --shard-id 0 --num-shards 2` | GPU 0 | 05:25 |
| plan-002-qwen17b-retry-s1 | `generate_chain.py --model-name qwen3-1.7b --shard-id 1 --num-shards 2` | GPU 1 | 05:25 |
| plan-002-qwen06b-s0 | `generate_chain.py --model-name qwen3-0.6b --shard-id 0 --num-shards 2` | GPU 2 | 05:25 |
| plan-002-qwen06b-s1 | `generate_chain.py --model-name qwen3-0.6b --shard-id 1 --num-shards 2` | GPU 3 | 05:25 |

均在 05:25 启动，已运行约 8 分钟。

### 5. qwen3-1.7b 数据目录 — 正在写入
- `generations_shard0.jsonl` — 212KB
- `generations_shard1.jsonl` — 188KB

### 6. qwen3-0.6b 数据目录 — 正在写入
- `generations_shard0.jsonl` — 222KB
- `generations_shard1.jsonl` — 196KB

**结论**: 模型文件均已就绪，但 4 张 GPU 并非空闲 — plan-002 的生成任务（qwen3-1.7b 2 shards + qwen3-0.6b 2 shards）正在全速运行中，数据正在产出。

---
