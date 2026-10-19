# Plan 005: 分层分析报告

**日期**: 2026-05-14
**状态**: 脚本已完成全部 5 维度，dry-run 通过。真实数据分析受阻于 GPU 占用和缺少跨策略 checkpoint。

## 1. 脚本路径与参数

**脚本**: `/root/structfuse/evaluation/analyze_stratified.py` (910 行，已修改)

### 参数

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--m1-data` | M1 all.jsonl 路径 (必须) | — |
| `--val-data-dir` | val_*.jsonl 目录 | — |
| `--output-dir` | 输出目录 (必须) | — |
| `--predictions-dir` | 预计算预测 JSON 目录 (CPU) | None |
| `--checkpoints-dir` | Checkpoint 目录 (需 GPU) | None |
| `--dry-run` | Mock 预测，用于测试管道 (CPU) | False |
| `--seeds` | 逗号分隔的种子 | 42,43,44 |
| `--device` | 推理设备 | cuda |
| `--n-bootstrap` | Bootstrap 迭代数 | 1000 |
| `--dataflow-graph` | dataflow_graph.json 路径 (新增) | None |
| `--repo-size-bins` | 自定义 repo size 分组 | None |
| `--pool-size-bins` | 自定义 pool size 分组 | None |
| `--sim-bins` | 自定义 similarity 分组 | None |

### 运行命令 (完整)

```bash
cd /root/structfuse && python3 evaluation/analyze_stratified.py \
  --m1-data /root/autodl-tmp/structfuse/full_m1_data/all.jsonl \
  --val-data-dir /root/autodl-tmp/structfuse/full_m2_training_data \
  --dataflow-graph /root/autodl-tmp/structfuse/full_m2_training_data/dataflow_graph.json \
  --output-dir /root/autodl-tmp/structfuse/artifacts/stratified_analysis \
  --predictions-dir <predictions_dir> \  # 或 --checkpoints-dir 或 --dry-run
  --seeds 42,43,44 \
  --n-bootstrap 1000
```

### 输出
- `stratified_results.json`: 完整 per-stratum 指标 + bootstrap CI (5 维度)
- `stratified_summary.csv`: 紧凑表格
- `stratified_plots.pdf`: 分组柱状图 + heatmap + delta 趋势 (5 维度)

## 2. 维度覆盖 — 全部 5/5 ✅

| # | 维度 | 状态 | 分层 | 说明 |
|---|------|------|------|------|
| 1 | **Repo size** | ✅ | small/medium/large/xlarge | M1 instance count per repo |
| 2 | **Pool size** | ✅ | small/medium/large | neg_candidates 数量 |
| 3 | **Query-positive similarity** | ✅ | low/medium/high | cosine sim 或 text overlap |
| 4 | **Structural data availability** | ✅ 新增 | sparse/moderate/rich | dataflow graph 边数 |
| 5 | **neg_difficulty quartile** | ✅ 新增 | Q1_easy/Q2/Q3/Q4_hard | text overlap proxy margin |

### 新增维度实现细节

**Structural data availability**: 从 `dataflow_graph.json` 统计每个 query_id 的边数，按 DATAFLOW_BINS 分层：
- sparse (0-1 边): 1546 instances (51.9%)
- moderate (2-9 边): 498 instances (16.7%)
- rich (10+ 边): 936 instances (31.4%)

**neg_difficulty quartile**: CPU 友好的 text-overlap proxy。计算 margin = (query-pos Jaccard overlap) - max(query-neg Jaccard overlap)，按 quartile 分四等分，margin 越小 → negative 越难。每个 quartile ~745 instances。

## 3. 已完成的修改

1. **新增 `DATAFLOW_BINS` 和 `NEG_DIFFICULTY_QUARTILE_LABELS` 常量**
2. **新增 `load_dataflow_edges()` 函数** — 加载 dataflow graph 并返回 {file_key: edge_count}
3. **新增 `assign_neg_difficulty_quartiles()` 函数** — 基于 text overlap proxy 计算 margin 并按 quartile 分配
4. **扩展 `assign_strata()`** — 增加 `dataflow_edges` 参数，分配 `dataflow_bin`
5. **新增 `--dataflow-graph` 参数**
6. **修复 checkpoint 路径解析** — 依次查找 `best/`, `best_by_recall_at_1/`, `best_by_val_loss/`，需 model.pt 存在
7. **扩展 `write_summary_csv()` 和 `make_plots()`** — 接受新维度数据，自动生成对应图表

## 4. 阻塞点（真实数据分析）

### 4.1 缺少 embedding_distance / dataflow_aware checkpoints
`m2_full_qwen/` 只有 `random_s42/43/44`。跨策略对比需要这些策略的训练 checkpoint。

### 4.2 无预计算预测文件
`--predictions-dir` 模式需要 `eval_retrieval.py` 产出的 per-instance JSON。

### 4.3 GPU 占用
model inference 需要 GPU，当前被训练占用。

## 5. Dry-run 验证

运行 `--dry-run --seeds 42 --n-bootstrap 200 --dataflow-graph ...`，全部 5 维度成功产出：

```
/root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v2/
├── stratified_results.json  (5 维度，含 by_dataflow + by_neg_difficulty)
├── stratified_summary.csv   (dataflow + neg_difficulty 行已加入)
└── stratified_plots.pdf     (113KB，含新维度的 bar chart + heatmap + delta)
```

## 6. 下一步行动

| 优先级 | 任务 | 依赖 |
|--------|------|------|
| P1 | 用现有 random checkpoints 生成 per-instance predictions (eval_retrieval.py) | GPU 空闲后 |
| P1 | 用 predictions 跑 5 维度分层分析 (random only) | P1 上一步 |
| P2 | 训练 embedding_distance / dataflow_aware checkpoints | GPU + 训练时间 |
| P2 | 跨策略全 5 维度完整分析 | P2 上一步 |

## 7. 相关文件清单

```
脚本 (已修改):
  /root/structfuse/evaluation/analyze_stratified.py        # 910 行，5 维度完整

数据:
  /root/autodl-tmp/structfuse/full_m1_data/all.jsonl
  /root/autodl-tmp/structfuse/full_m2_training_data/val_*.jsonl
  /root/autodl-tmp/structfuse/full_m2_training_data/dataflow_graph.json

Checkpoints (仅 random):
  /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s{42,43,44}/best_by_recall_at_1/
  /root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_recall_at_1/

Dry-run 输出:
  /root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v2/
```
