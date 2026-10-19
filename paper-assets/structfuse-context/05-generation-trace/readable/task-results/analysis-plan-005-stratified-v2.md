# analysis plan 005 stratified v2

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan_005_stratified_v2_20260514T202757_result.json`
- **Structured JSON:** [`35d0d16ebd8c4b28a9ea.json`](../../sessions/35/35d0d16ebd8c4b28a9ea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Pipeline 验证通过，所有输出完整。汇报如下：

---

## 汇报

### 1. 脚本信息

- **路径**: `/root/structfuse/evaluation/analyze_stratified.py` (910 行)
- **关键参数**:
  - `--m1-data` (required): M1 all.jsonl 路径
  - `--output-dir` (required): 输出目录
  - `--predictions-dir` / `--checkpoints-dir` / `--dry-run`: 三选一数据来源
  - `--val-data-dir`: val JSONL 目录（默认 `/root/autodl-tmp/structfuse/full_m2_training_data`）
  - `--dataflow-graph`: dataflow_graph.json 路径（启用 structural data 维度）
  - `--seeds`: 默认 `42,43,44`
  - `--n-bootstrap`: bootstrap CI 次数，默认 1000
  - `--device`: 默认 `cuda`

### 2. 5 个分层维度 — 全部已实现

| 维度 | 状态 | bins |
|------|------|------|
| repo_size | ✅ | small(<50), medium(50-200), large(200-500), xlarge(500+) |
| pool_size | ✅ | small(<20), medium(20-40), large(40-51) |
| query-pos similarity | ✅ | low(<0.3), medium(0.3-0.6), high(0.6+) |
| structural data availability (dataflow) | ✅ | sparse(<2 edges), moderate(2-10), rich(10+) |
| neg_difficulty quartile | ✅ | Q1_easy, Q2, Q3, Q4_hard |

### 3. GPU 需求

- `--dry-run` 模式: **CPU 即可**（mock predictions + text-overlap similarity）
- `--checkpoints-dir` 模式: **需要 GPU**（加载模型做 forward pass） → 当前 GPU 被训练占用，**阻塞**
- `--predictions-dir` 模式: **CPU 即可**，但目前无预计算 predictions 文件

### 4. dry-run 执行结果

已成功运行（seeds=42,43, n_bootstrap=200, CPU, 27秒完成），产出:
- `/root/autodl-tmp/structfuse/stratified_analysis_dryrun/stratified_results.json`
- `/root/autodl-tmp/structfuse/stratified_analysis_dryrun/stratified_summary.csv`
- `/root/autodl-tmp/structfuse/stratified_analysis_dryrun/stratified_plots.pdf`

CSV 覆盖全部 5 维度 × 3 策略，含 bootstrap 95% CI 和 delta 对比。Pipeline 端到端验证通过。

### 5. 真实数据运行阻塞

**阻塞原因**: 只有 `random_s42/43/44` 的 checkpoints 存在（`/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/`），缺少 `embedding_distance_s*` 和 `dataflow_aware_s*` checkpoints。且 checkpoint 模式需要 GPU。

**解决方案**（优先级排序）:
1. 等当前训练完成后，用 `eval_retrieval.py` 对已有 checkpoints 生成 per-instance predictions JSON，然后用 `--predictions-dir` 在 CPU 上跑
2. 如果 embedding_distance / dataflow_aware 策略有训练计划，等 checkpoints 产出后用 `--checkpoints-dir` 跑完整对比
3. 只分析 random 策略的分层特征（不做策略间对比），可用现有 checkpoints + GPU 空闲时段执行

---
