# analysis pool50 stratified prep

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_pool50_stratified_prep_20260516T055702_result.json`
- **Structured JSON:** [`a56d93ad7dfb061c37c5.json`](../../sessions/a5/a56d93ad7dfb061c37c5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息收集完毕，以下是完整结论：

---

## 1. Pool=50 结果文件结构：**仅有 aggregate metrics，无 instance-level 数据**

两个 JSON 文件结构相同：
```
{checkpoint_path → {config_model_name, pool_size, num_samples, num_queries, metrics: {recall@1_mean/std, recall@5_mean/std}, per_trial: [{recall@1, recall@5}]}}
```
- Qwen: 12 个 checkpoint（6 strategy-seed × 2 selection criteria: best_by_recall_at_1 / best_by_val_loss）
- StarCoder: 8 个 checkpoint（4 × 2，缺 dataflow_aware 和部分 embedding_distance seed）
- `per_trial` 只是 5 次随机采样的 trial-level aggregate，**不包含每个 query 的 rank/score**

## 2. 训练/验证数据中可用的分层字段

**M1 all.jsonl** (`/root/autodl-tmp/structfuse/full_m1_data/all.jsonl`):
- `instance_id`, `repo`, `github_repo`, `base_commit`, `buggy_file`, `buggy_function`, `gold_patch_files`
- `call_graph` (有 hop_distance, direction, file_path)
- `dataflow_paths` (source/sink file+line 对)
- `inter_procedural`, `extraction_method`, `extraction_time_s`

**M2 val JSONL** (`/root/autodl-tmp/structfuse/full_m2_training_data/val_{strategy}_{seed}.jsonl`):
- `query_id`, `query_tokens`, `pos_tokens`（训练数据已截断为 text 对，字段与 evaluate_pool50.py 一致）

**Dataflow graph**: `/root/autodl-tmp/structfuse/full_m2_training_data/dataflow_graph.json` 和 starcoder 版本均存在。

所有 5 个分层维度的数据源都可用：
| 维度 | 数据来源 | 状态 |
|------|----------|------|
| Repo size | M1 all.jsonl → instance_id → repo → count | ✅ |
| Pool size | val JSONL → neg_candidates count | ✅ 需确认 val 文件是否有 neg_candidates |
| Query-pos similarity | 模型推理时计算 cosine sim / text overlap | ✅ |
| Dataflow availability | dataflow_graph.json | ✅ |
| Neg difficulty | pos-neg margin quartiles | ✅ 需模型推理计算 |

## 3. `analyze_stratified.py` 已完整实现，不需要改 `evaluate_pool50.py`

`analyze_stratified.py` 有两种获取 instance-level 数据的路径：
1. **`--predictions-dir`**: 从已保存的预测文件加载（`load_predictions` 函数）
2. **`--checkpoints-dir`**: 直接从 checkpoint 重新推理（`reeval_checkpoint` 函数），自动产出每个 query 的 `{query_id, instance_id, pool_size, rank, pos_sim, total_candidates}`
3. **`--dry-run`**: 用 mock predictions 做验证性运行

所以**不需要修改 `evaluate_pool50.py`**。`analyze_stratified.py` 的 `reeval_checkpoint` 会直接加载 checkpoint，对每个 val query 计算 rank 和 pos_sim，产出完整的 instance-level results。

## 4. Plan_005 分层分析可行性评估与执行方案

**完全可行**。直接运行 `analyze_stratified.py` 即可：

```bash
python3 /root/structfuse/evaluation/analyze_stratified.py \
    --checkpoints-dir /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen \
    --val-data-dir /root/autodl-tmp/structfuse/full_m2_training_data \
    --m1-data /root/autodl-tmp/structfuse/full_m1_data/all.jsonl \
    --dataflow-graph /root/autodl-tmp/structfuse/full_m2_training_data/dataflow_graph.json \
    --output-dir /root/autodl-tmp/structfuse/results/stratified_qwen \
    --seeds 42,43,44 \
    --device cuda
```

StarCoder 同理，换 checkpoints-dir/val-data-dir/dataflow-graph 路径。

脚本会自动产出 `stratified_results.json`、`stratified_summary.csv`、`stratified_plots.pdf`，覆盖全部 5+2 个分析维度（含 pool-size controlled 和 dataflow × pool_size 交叉分析）。

---
