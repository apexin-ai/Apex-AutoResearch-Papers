# fix p2b data bug steps0 2

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_p2b_data_bug_steps0-2_20260512T193908_result.json`
- **Structured JSON:** [`3af128a17d7b95f96f6c.json`](../../sessions/3a/3af128a17d7b95f96f6c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两处修改都正确完成。汇报如下：

---

## Step 0: 清理 GPU

cuda:4 已空闲（3MiB / 0% 利用率）。PID 318345、318733 已不存在，无需 kill。

## Step 1: 清理磁盘

删除了 6 个目录：
- `/root/autodl-tmp/structfuse/checkpoints/p2b_dataflow_aware_s42/`
- `/root/autodl-tmp/structfuse/checkpoints/p2b_dataflow_aware_s123/`
- `/root/autodl-tmp/structfuse/checkpoints/p2b_dataflow_aware_s456/`
- `/root/autodl-tmp/structfuse/checkpoints/p2b_embedding_distance_s123/`
- `/root/autodl-tmp/structfuse/checkpoints/p2b_embedding_distance_s456/`
- `/root/autodl-tmp/structfuse/eval_results_p50/`

剩余 checkpoint：`p2b_embedding_distance_s42`, `p2b_random_s42`, `p2b_random_s123`, `p2b_random_s456`

磁盘：91G 可用 / 169G 总量（47% 使用）

## Step 2: build_p2b_data.py 完整 Diff

文件路径：`/root/structfuse/scripts/build_p2b_data.py`

**改动 B — 第 18 行，pool_size：**
```diff
- CANDIDATE_POOL_SIZE = 25
+ CANDIDATE_POOL_SIZE = 50
```

**改动 A — 第 134 行，候选池 bug：**
```diff
- non_pos = [f for f in all_py if f != buggy_file and f not in connected_all]
+ non_pos = [f for f in all_py if f != buggy_file and f not in connected_files]
```

**逻辑效果：**
- `connected_files` = gold 正例文件（来自 report）
- `connected_all` = gold + dataflow 连接文件（第 120-121 行构造）
- 修改前：`non_pos` 排除了 gold 和 dataflow-connected 文件 → embedding 和 dataflow 策略候选池相同（都缺 connected 文件）
- 修改后：`non_pos` 只排除 gold 文件 → 包含 dataflow-connected 文件
  - `embedding` 策略：从完整 `non_pos`（含 connected）按 BM25 排序取 top-50
  - `dataflow` 策略：`build_candidate_pools` 内部用 `connected_all` 过滤，从 `non_pos` 中排除 connected → 只从 disconnected 子集按 BM25 取 top-50
- 第 135 行 `build_candidate_pools(non_pos, bm25, connected_all, ...)` 保持不变，确保 dataflow 策略正确排除 connected 文件

**未运行脚本，等待确认。**

---
