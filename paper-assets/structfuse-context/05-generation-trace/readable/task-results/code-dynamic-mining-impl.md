# code dynamic mining impl

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_dynamic_mining_impl_20260513T002931_result.json`
- **Structured JSON:** [`49f37ed5001ece641098.json`](../../sessions/49/49f37ed5001ece641098.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有修改到位。总结：

**build_m1_training_data.py** (354 → 432 行):
- 新增 `--embedding-mining-mode {static,dynamic}` 参数（默认 `static`）
- `static` 模式：行为完全不变
- `dynamic` 模式：
  - 跳过 BM25 计算和 strategy pool 构建
  - 输出 `candidate_pools.jsonl`（每个 instance 的所有候选文件 + content + dataflow 连通性）
  - 输出 `train_dynamic.jsonl`（全部非正样本文件作为 neg_candidates）
  - 输出 `val.jsonl` + `dataflow_graph.json`

**training/train.py** (477 → 576 行):
- 新增 `--dynamic-mining` flag 和 `--candidate-pool-file` 参数
- 启用时：启动阶段加载 `candidate_pools.jsonl`
- 每 epoch 开始：调用 `_mine_dynamic_negatives()`，用当前 encoder 重新编码所有候选文件，按 cosine similarity 选 top-k hardest negatives，通过 `refresh_negatives()` 更新训练数据
- 未启用时：走原有 pre-mined negatives 路径

---
