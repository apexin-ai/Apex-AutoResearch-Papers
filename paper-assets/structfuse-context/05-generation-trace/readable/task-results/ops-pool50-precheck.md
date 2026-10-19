# ops pool50 precheck

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_pool50-precheck_20260515T235517_result.json`
- **Structured JSON:** [`b9cb5e65b9ee8ca4cc79.json`](../../sessions/b9/b9cb5e65b9ee8ca4cc79.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Pipeline 验证通过。汇总如下：

---

## 预检结果

### 脚本路径
| 脚本 | 路径 | 用途 |
|------|------|------|
| evaluate_pool50.py | `/root/structfuse/evaluation/evaluate_pool50.py` | 独立 pool=50 R@1/R@5 评估 |
| analyze_stratified.py | `/root/structfuse/evaluation/analyze_stratified.py` | 5+2 维度分层分析 |
| run_eval_p50.sh | `/root/structfuse/scripts/run_eval_p50.sh` | M1 p2b 旧脚本，**不是** M2 用的 |

### 数据路径
- Val 数据: `/root/autodl-tmp/structfuse/full_m2_training_data/val_{strategy}_s{seed}.jsonl` (每份 2980 queries)
- M1 元数据: `/root/autodl-tmp/structfuse/full_m1_data/all.jsonl` ✅
- Dataflow 图: `/root/autodl-tmp/structfuse/full_m2_training_data/dataflow_graph.json` ✅

### Checkpoint 状态 (best_by_recall_at_1)

**Qwen — 6/9 完成:**

| Strategy | s42 | s43 | s44 |
|----------|:---:|:---:|:---:|
| random | ✅ | ✅ | ✅ |
| embedding_distance | ❌ | ✅ | ✅ |
| dataflow_aware | ❌ | ✅ | ❌ |

**StarCoder — 4/9 完成:**

| Strategy | s42 | s43 | s44 |
|----------|:---:|:---:|:---:|
| random | ✅ | ✅ | ✅ |
| embedding_distance | ✅ | ❌ | ❌ |
| dataflow_aware | ❌ | ❌ | ❌ |

### Dry-run 验证
- ✅ Import chain 正常
- ✅ 两个脚本 `--help` 正常
- ✅ 模型加载成功 (StructFuseEncoder, base=Qwen2.5-Coder-3B)
- ✅ 单样本编码: shape `(1, 256)`, norm=1.0000
- ✅ Val 数据格式正确 (keys: query_id, query_tokens, pos_tokens)
- ✅ 上游数据全部存在

### 注意事项
1. **两个脚本是独立 pipeline** — analyze_stratified.py 不消费 evaluate_pool50.py 的输出，它自带 `--checkpoints-dir` 模式直接从 checkpoint re-eval
2. **evaluate_pool50.py 没有 `--max-queries` 参数** — 完整跑需要编码 2980 queries，单 GPU 约 2-5 分钟
3. **两块 GPU 当前 100% 占用**（训练中），eval 需等训练完成或使用空闲 GPU
4. **Qwen 缺 3 个 run, StarCoder 缺 5 个 run** — 还在训练中

### 结论
**Pipeline ready.** 脚本、数据、格式全部验证通过。唯一 blocker 是等待剩余 M2 checkpoint 训练完成。

---
