# code mvp critical fix

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp-critical-fix_20260514T170956_result.json`
- **Structured JSON:** [`9a7fe892d93a4b074eed.json`](../../sessions/9a/9a7fe892d93a4b074eed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

results/ 目录已清空，dry-run 产物已清理。

---

## 报告

### 1. 虚假结果删除
已删除：`results/mvp_results.json`、`data/generations_shard0.jsonl`、`data/features.csv`。results/ 目录现为空。

### 2. wiki_seed_1000.jsonl 格式
- **JSON keys**: `{"id": str, "title": str, "text": str}`
- **行数**: 1000 行（经过滤后有效 seeds: 995 条）

### 3. Dry-run 结果
| 脚本 | 状态 |
|------|------|
| generate_chain.py | **PASS** — 10 records (2 seeds × 5 depths), 0 skipped, 21.4s |
| extract_features.py | **PASS** — 10 rows, shape (10, 10) |
| classify_and_eval.py | **PASS** — 无 MARGINAL，无 mock 数据，dry-run 未写文件 |

### 4. 模型路径
**Pythia-2.8B**: `/root/autodl-tmp/.hf_cache/EleutherAI/pythia-2___8b`

### 5. 4 shard 完整运行命令
```
shard 0: python generate_chain.py --input data/wiki_seed_1000.jsonl --shard-id 0 --num-shards 4 --device cuda:0
shard 1: python generate_chain.py --input data/wiki_seed_1000.jsonl --shard-id 1 --num-shards 4 --device cuda:1
shard 2: python generate_chain.py --input data/wiki_seed_1000.jsonl --shard-id 2 --num-shards 4 --device cuda:2
shard 3: python generate_chain.py --input data/wiki_seed_1000.jsonl --shard-id 3 --num-shards 4 --device cuda:3
```

### 6. 预估运行时间
- 每个 seed ~10.7s（含 4 次 256-token 生成）
- 每 shard: 248-249 seeds
- **单 shard 预估: ~44 分钟**
- 4 shard 并行运行，总耗时 ~44 分钟

### 修复总结
| 修改 | 详情 |
|------|------|
| generate_chain.py | `--input` 替代 `--seed-file`；`--output-dir` 新增；删除 HF 下载回退；`temperature=0.7, top_p=0.9`；空输入防护；ID 公式 `shard_id * shard_size * 5 + local_idx`；`dtype=torch.float16` |
| classify_and_eval.py | 删除 `generate_mock_features`；verdict 改为二元 PASS/FAIL（无 MARGINAL）；dry-run 只输出到 stdout；小数据集自适应处理 |
| merge_shards.py | 已存在且逻辑正确，无需修改 |

---
