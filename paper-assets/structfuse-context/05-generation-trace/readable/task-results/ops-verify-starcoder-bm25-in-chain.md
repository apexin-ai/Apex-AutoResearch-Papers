# ops verify starcoder bm25 in chain

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-starcoder-bm25-in-chain_20260515T163232_result.json`
- **Structured JSON:** [`af73676eca6e28667ee5.json`](../../sessions/af/af73676eca6e28667ee5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息收齐，结论如下：

---

## 结果

### 1. StarCoder 主链是否包含 bm25_s42？

**不包含。** StarCoder 主链的调度结构如下：

- `schedule_m2_runs.sh`（主调度器）只跑 Qwen，策略仅限 `random | embedding_distance | dataflow_aware`，无 BM25。
- StarCoder 的主链（PID 519791 所监视的进程）从 `/root/runs/m2_full_starcoder/` 的日志来看只跑了 `random_s42/s43/s44` + `s43plus_all`。
- BM25 StarCoder 有**独立脚本** `scripts/run_m2_full_bm25_starcoder.sh`，跑 3 seeds (42/43/44)，但这不是主链的一部分。
- `full_m2_outputs/` 下只有 `random_s42`，**没有 `bm25_starcoder_s42` 目录**，说明 BM25 StarCoder 脚本**尚未执行**。

### 2. StarCoder s42 supplement watcher 触发后跑哪些策略？

**只跑 `embedding_distance_s42` + `dataflow_aware_s42`。** 

`run_m2_s42_supplement.sh` 硬编码 `STRATEGIES=("embedding_distance" "dataflow_aware")`，**不含 bm25**。

### 3. bm25_s42 状态

**缺失。** bm25_s42 for StarCoder 既不在主链，也不在 supplement watcher 中：

- 训练数据已就绪：`train_bm25_s42.jsonl` 和 `val_bm25_s42.jsonl` 都在 `full_m2_training_data/` 下
- StarCoder 专用数据目录 `full_m2_starcoder_data/` 下**没有** bm25 数据文件
- 独立脚本 `run_m2_full_bm25_starcoder.sh` 存在但**未被执行过**（无输出目录）

### 需要补充

`bm25_s42` (以及 s43/s44) for StarCoder 需要单独安排执行，可以通过 `run_m2_full_bm25_starcoder.sh` 来跑。注意该脚本读取的数据在 `full_m2_training_data/`（通用目录）而非 `full_m2_starcoder_data/`（StarCoder 专用目录）。

---
