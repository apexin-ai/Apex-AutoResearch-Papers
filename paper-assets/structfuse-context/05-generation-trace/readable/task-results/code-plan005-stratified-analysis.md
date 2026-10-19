# code plan005 stratified analysis

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan005_stratified_analysis_20260514T092057_result.json`
- **Structured JSON:** [`fd82a49916b13e87f63d.json`](../../sessions/fd/fd82a49916b13e87f63d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 完成总结

### 1. 脚本路径与核心逻辑

**`/root/structfuse-context/evaluation/analyze_stratified.py`** (781 行)

三种数据获取模式：
- `--dry-run`: 生成 mock predictions 验证管线
- `--predictions-dir`: 加载 eval_retrieval.py 的 JSON 输出
- `--checkpoints-dir`: 加载 checkpoint，逐实例 re-eval（因为 train.py evaluate 不输出 per-instance predictions）

三个分层维度：
- **Repo size**: small(<50) / medium(50-200) / large(200-500) / xlarge(500+)
- **Candidate pool size**: small(<20) / medium(20-40) / large(40-51)
- **Query-positive similarity**: low(<0.3) / medium(0.3-0.6) / high(0.6-1.0)

### 2. Dry-run 结果（mock 数据）

| 维度 | 层 | Random R@1 | Embedding R@1 | Dataflow R@1 | Emb-Rand Delta |
|------|------|-----------|---------------|--------------|----------------|
| repo_size | small | 0.104 | 0.216 | 0.432 | +0.113 (+109%) |
| repo_size | medium | 0.098 | 0.232 | 0.335 | +0.134 (+136%) |
| repo_size | large | 0.027 | 0.070 | 0.130 | +0.042 (+155%) |
| repo_size | xlarge | 0.027 | 0.060 | 0.103 | +0.034 (+127%) |
| pool_size | small | 0.121 | 0.273 | 0.421 | +0.152 (+126%) |
| pool_size | large | 0.024 | 0.057 | 0.095 | +0.033 (+140%) |

### 3. 生成的图表

`stratified_plots.pdf` (78KB) 含 9 页：
- 3 × 分组柱状图（每维度一页，含 R@1/R@5/MRR + error bars）
- 3 × R@1 热力图（stratum × strategy）
- 3 × Delta 趋势折线图（embedding/dataflow vs random 随层变化）

### 4. M2 正式运行所需文件

- **M1 metadata**: `/root/autodl-tmp/structfuse/full_m1_data/all.jsonl` ✅ 已存在
- **Val 数据**: `/root/autodl-tmp/structfuse/full_m2_training_data/val_{strategy}_s{seed}.jsonl` ✅ 已存在
- **Checkpoints**: `/root/autodl-tmp/structfuse/checkpoints/{strategy}_s{seed}/best/model.pt` + `training_config.json` + tokenizer 文件 ⏳ 待 M2 训练产生

正式运行命令：
```bash
python3 analyze_stratified.py \
    --checkpoints-dir /root/autodl-tmp/structfuse/checkpoints \
    --m1-data /root/autodl-tmp/structfuse/full_m1_data/all.jsonl \
    --val-data-dir /root/autodl-tmp/structfuse/full_m2_training_data \
    --output-dir /root/autodl-tmp/structfuse/artifacts/stratified_analysis
```

### 5. 注意事项

- `pos_dataflow_distance` 所有策略/seed 均为 1，无法用于相似度分层。改用 text Jaccard（dry-run）或 model cosine similarity（re-eval）
- M1 文件 44k 行，每行含大量 call_graph/dataflow_paths，已用 regex 快速提取 instance_id/repo，避免全量 JSON 解析
- Val 文件每行含完整 candidate_tokens（50 个文件内容），lite 模式下截断到 1000 字符用于相似度计算
- Re-eval 模式逐实例编码，2980 × 51 次 forward pass，预计需 GPU 约 30-60 分钟

---
