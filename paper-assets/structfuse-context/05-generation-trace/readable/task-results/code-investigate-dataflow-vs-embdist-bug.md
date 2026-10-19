# code investigate dataflow vs embdist bug

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_investigate_dataflow_vs_embdist_bug_20260512T192104_result.json`
- **Structured JSON:** [`3379c5f9a0ff9ceb7912.json`](../../sessions/33/3379c5f9a0ff9ceb7912.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

确认完毕。两个文件的 tail 也完全相同。诊断报告如下：

---

## 诊断报告：dataflow_aware 与 embedding_distance 结果完全一致

### Root Cause

**文件：`/root/structfuse/scripts/build_p2b_data.py`，`main()` 函数中 `non_pos` 的定义。**

```python
# build_p2b_data.py main(), ~line 90
non_pos = [f for f in all_py if f != buggy_file and f not in connected_all]
pools = build_candidate_pools(non_pos, bm25, connected_all, CANDIDATE_POOL_SIZE)
```

`non_pos` 在传入 `build_candidate_pools` 之前已经排除了所有 `connected_all` 中的文件。

而 `build_candidate_pools` 中 dataflow 策略的 "disconnected" 过滤是：

```python
disconnected = [f for f in non_pos_files if f not in connected_set]
```

由于 `non_pos_files` 中的每个元素都已经 `not in connected_set`（因为 `connected_set == connected_all`），**这行过滤是 no-op**。

结果：`disconnected == non_pos_files`，`pools['dataflow'] == pools['embedding']`（都是 `non_pos` 按 BM25 降序取 top-25）。

### Evidence

1. **文件完全一致**：`train_dataflow.jsonl` 和 `train_embedding.jsonl` 大小均为 53,649,714 bytes，行数均为 505，首尾内容相同
2. **代码逻辑证明**：`non_pos` 定义已排除 `connected_all` → `build_candidate_pools` 中 `f not in connected_set` 恒为 True → embedding 和 dataflow pools 完全相同
3. **双重失效**：`train.py` 中虽然构建了 `miner` 对象（根据 `--hard-negative-strategy` 参数），但训练循环中 `refresh_negatives()` 从未被调用（注释 "P2b: negatives pre-mined per strategy in data files"）。`__getitem__` 的 fallback path 直接从数据文件的 `neg_candidates` 字段取 negatives，miner 完全被绕过

### Fix Suggestion

**Fix 1（核心修复）— `build_p2b_data.py`：**

`main()` 中传入更宽的候选集，让各策略自行决定过滤逻辑：

```python
# Before (buggy):
non_pos = [f for f in all_py if f != buggy_file and f not in connected_all]
pools = build_candidate_pools(non_pos, bm25, connected_all, CANDIDATE_POOL_SIZE)

# After (fixed):
all_non_query = [f for f in all_py if f != buggy_file]
pools = build_candidate_pools(all_non_query, bm25, connected_all, CANDIDATE_POOL_SIZE)
```

`build_candidate_pools` 改为：

```python
def build_candidate_pools(all_files, bm25_scores, connected_set, pool_size):
    non_connected = [f for f in all_files if f not in connected_set]

    # random: 从 disconnected 文件中随机抽样
    shuffled = list(non_connected)
    random.shuffle(shuffled)
    pools['random'] = shuffled[:pool_size]

    # embedding: 从 ALL non-query 文件中按 BM25 取 top-K（可能包含 connected 文件）
    scored = sorted(all_files, key=lambda f: -bm25_scores.get(f, 0))
    pools['embedding'] = scored[:pool_size]

    # dataflow: 从 disconnected 文件中按 BM25 取 top-K
    scored_disc = sorted(non_connected, key=lambda f: -bm25_scores.get(f, 0))
    pools['dataflow'] = scored_disc[:pool_size]

    return pools
```

这样 `embedding` 策略的 negatives 会包含一些 dataflow-connected 文件（"有相关性但仍作为 negative"的 hard negatives），而 `dataflow` 策略的 negatives 严格排除 connected 文件——两者产生有意义的差异。

**Fix 2（可选）— `train.py`：** 删除未使用的 miner 构建代码，或者恢复 per-epoch `refresh_negatives()` 调用，使动态 mining 真正生效。

**修复后需要：** 重新运行 `build_p2b_data.py` 生成数据 → 重跑 9 个训练 runs。

---
