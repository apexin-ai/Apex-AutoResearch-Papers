# Research conversation: <project_context> # 项目: structfuse-context ## 运行环境 - 服务器名: bjb1-42106 - SSH 账户: root（调用 ssh_execute / submit_training_jo — Part 2 of 2

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../research-conversation-project-context-structfuse-context-bjb1-42106-ssh-root-ssh-execute-submit-trai-copy-135.md) · [Structured JSON](../../../sessions/f3/f355ceed7ed477eaa7a4.json)

## Round 1

### Tool result

_source line 244 · 2026-05-14T20:25:25.311Z_

<details><summary>↩ Tool result · `toolu_01SNfMLywNd4ryiNBKjnbF4Z`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/plan005_stratified_analysis_report.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "0e3a2853-ff69-4b3f-afce-5a355d7a5677",
  "isSidechain": false,
  "promptId": "9e9b674e-9fc3-475b-a334-fc014d0bb425",
  "type": "user",
  "uuid": "35865531-75a4-482d-a498-82ae5a08ff4f",
  "toolUseResult": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/plan005_stratified_analysis_report.md",
    "content": "# Plan 005: 分层分析报告\n\n**日期**: 2026-05-14\n**状态**: 脚本已完成全部 5 维度，dry-run 通过。真实数据分析受阻于 GPU 占用和缺少跨策略 checkpoint。\n\n## 1. 脚本路径与参数\n\n**脚本**: `/root/structfuse/evaluation/analyze_stratified.py` (910 行，已修改)\n\n### 参数\n\n| 参数 | 说明 | 默认值 |\n|------|------|--------|\n| `--m1-data` | M1 all.jsonl 路径 (必须) | — |\n| `--val-data-dir` | val_*.jsonl 目录 | — |\n| `--output-dir` | 输出目录 (必须) | — |\n| `--predictions-dir` | 预计算预测 JSON 目录 (CPU) | None |\n| `--checkpoints-dir` | Checkpoint 目录 (需 GPU) | None |\n| `--dry-run` | Mock 预测，用于测试管道 (CPU) | False |\n| `--seeds` | 逗号分隔的种子 | 42,43,44 |\n| `--device` | 推理设备 | cuda |\n| `--n-bootstrap` | Bootstrap 迭代数 | 1000 |\n| `--dataflow-graph` | dataflow_graph.json 路径 (新增) | None |\n| `--repo-size-bins` | 自定义 repo size 分组 | None |\n| `--pool-size-bins` | 自定义 pool size 分组 | None |\n| `--sim-bins` | 自定义 similarity 分组 | None |\n\n### 运行命令 (完整)\n\n```bash\ncd /root/structfuse && python3 evaluation/analyze_stratified.py \\\n  --m1-data /root/autodl-tmp/structfuse/full_m1_data/all.jsonl \\\n  --val-data-dir /root/autodl-tmp/structfuse/full_m2_training_data \\\n  --dataflow-graph /root/autodl-tmp/structfuse/full_m2_training_data/dataflow_graph.json \\\n  --output-dir /root/autodl-tmp/structfuse/artifacts/stratified_analysis \\\n  --predictions-dir &lt;predictions_dir> \\  # 或 --checkpoints-dir 或 --dry-run\n  --seeds 42,43,44 \\\n  --n-bootstrap 1000\n```\n\n### 输出\n- `stratified_results.json`: 完整 per-stratum 指标 + bootstrap CI (5 维度)\n- `stratified_summary.csv`: 紧凑表格\n- `stratified_plots.pdf`: 分组柱状图 + heatmap + delta 趋势 (5 维度)\n\n## 2. 维度覆盖 — 全部 5/5 ✅\n\n| # | 维度 | 状态 | 分层 | 说明 |\n|---|------|------|------|------|\n| 1 | **Repo size** | ✅ | small/medium/large/xlarge | M1 instance count per repo |\n| 2 | **Pool size** | ✅ | small/medium/large | neg_candidates 数量 |\n| 3 | **Query-positive similarity** | ✅ | low/medium/high | cosine sim 或 text overlap |\n| 4 | **Structural data availability** | ✅ 新增 | sparse/moderate/rich | dataflow graph 边数 |\n| 5 | **neg_difficulty quartile** | ✅ 新增 | Q1_easy/Q2/Q3/Q4_hard | text overlap proxy margin |\n\n### 新增维度实现细节\n\n**Structural data availability**: 从 `dataflow_graph.json` 统计每个 query_id 的边数，按 DATAFLOW_BINS 分层：\n- sparse (0-1 边): 1546 instances (51.9%)\n- moderate (2-9 边): 498 instances (16.7%)\n- rich (10+ 边): 936 instances (31.4%)\n\n**neg_difficulty quartile**: CPU 友好的 text-overlap proxy。计算 margin = (query-pos Jaccard overlap) - max(query-neg Jaccard overlap)，按 quartile 分四等分，margin 越小 → negative 越难。每个 quartile ~745 instances。\n\n## 3. 已完成的修改\n\n1. **新增 `DATAFLOW_BINS` 和 `NEG_DIFFICULTY_QUARTILE_LABELS` 常量**\n2. **新增 `load_dataflow_edges()` 函数** — 加载 dataflow graph 并返回 {file_key: edge_count}\n3. **新增 `assign_neg_difficulty_quartiles()` 函数** — 基于 text overlap proxy 计算 margin 并按 quartile 分配\n4. **扩展 `assign_strata()`** — 增加 `dataflow_edges` 参数，分配 `dataflow_bin`\n5. **新增 `--dataflow-graph` 参数**\n6. **修复 checkpoint 路径解析** — 依次查找 `best/`, `best_by_recall_at_1/`, `best_by_val_loss/`，需 model.pt 存在\n7. **扩展 `write_summary_csv()` 和 `make_plots()`** — 接受新维度数据，自动生成对应图表\n\n## 4. 阻塞点（真实数据分析）\n\n### 4.1 缺少 embedding_distance / dataflow_aware checkpoints\n`m2_full_qwen/` 只有 `random_s42/43/44`。跨策略对比需要这些策略的训练 checkpoint。\n\n### 4.2 无预计算预测文件\n`--predictions-dir` 模式需要 `eval_retrieval.py` 产出的 per-instance JSON。\n\n### 4.3 GPU 占用\nmodel inference 需要 GPU，当前被训练占用。\n\n## 5. Dry-run 验证\n\n运行 `--dry-run --seeds 42 --n-bootstrap 200 --dataflow-graph ...`，全部 5 维度成功产出：\n\n```\n/root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v2/\n├── stratified_results.json  (5 维度，含 by_dataflow + by_neg_difficulty)\n├── stratified_summary.csv   (dataflow + neg_difficulty 行已加入)\n└── stratified_plots.pdf     (113KB，含新维度的 bar chart + heatmap + delta)\n```\n\n## 6. 下一步行动\n\n| 优先级 | 任务 | 依赖 |\n|--------|------|------|\n| P1 | 用现有 random checkpoints 生成 per-instance predictions (eval_retrieval.py) | GPU 空闲后 |\n| P1 | 用 predictions 跑 5 维度分层分析 (random only) | P1 上一步 |\n| P2 | 训练 embedding_distance / dataflow_aware checkpoints | GPU + 训练时间 |\n| P2 | 跨策略全 5 维度完整分析 | P2 上一步 |\n\n## 7. 相关文件清单\n\n```\n脚本 (已修改):\n  /root/structfuse/evaluation/analyze_stratified.py        # 910 行，5 维度完整\n\n数据:\n  /root/autodl-tmp/structfuse/full_m1_data/all.jsonl\n  /root/autodl-tmp/structfuse/full_m2_training_data/val_*.jsonl\n  /root/autodl-tmp/structfuse/full_m2_training_data/dataflow_graph.json\n\nCheckpoints (仅 random):\n  /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s{42,43,44}/best_by_recall_at_1/\n  /root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_recall_at_1/\n\nDry-run 输出:\n  /root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v2/\n```\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 11,
        "newStart": 1,
        "newLines": 11,
        "lines": [
          " # Plan 005: 分层分析报告",
          " ",
          " **日期**: 2026-05-14",
          "-**状态**: 部分完成 — 管道验证通过，真实分析有阻塞",
          "+**状态**: 脚本已完成全部 5 维度，dry-run 通过。真实数据分析受阻于 GPU 占用和缺少跨策略 checkpoint。",
          " ",
          " ## 1. 脚本路径与参数",
          " ",
          "-**脚本**: `/root/structfuse/evaluation/analyze_stratified.py` (781 行)",
          "+**脚本**: `/root/structfuse/evaluation/analyze_stratified.py` (910 行，已修改)",
          " ",
          " ### 参数",
          " "
        ]
      },
      {
        "oldStart": 20,
        "oldLines": 134,
        "newStart": 20,
        "newLines": 104,
        "lines": [
          " | `--seeds` | 逗号分隔的种子 | 42,43,44 |",
          " | `--device` | 推理设备 | cuda |",
          " | `--n-bootstrap` | Bootstrap 迭代数 | 1000 |",
          "+| `--dataflow-graph` | dataflow_graph.json 路径 (新增) | None |",
          " | `--repo-size-bins` | 自定义 repo size 分组 | None |",
          " | `--pool-size-bins` | 自定义 pool size 分组 | None |",
          " | `--sim-bins` | 自定义 similarity 分组 | None |",
          " ",
          "-### 输入模式 (三选一)",
          "-1. `--dry-run`: Mock 数据，CPU，用于管道验证 ✅ 已验证通过",
          "-2. `--predictions-dir`: 加载已有预测结果，CPU ⛔ 无数据",
          "-3. `--checkpoints-dir`: 从 checkpoint 做 forward pass，GPU ⛔ GPU 占用中",
          "+### 运行命令 (完整)",
          " ",
          "+```bash",
          "+cd /root/structfuse && python3 evaluation/analyze_stratified.py \\",
          "+  --m1-data /root/autodl-tmp/structfuse/full_m1_data/all.jsonl \\",
          "+  --val-data-dir /root/autodl-tmp/structfuse/full_m2_training_data \\",
          "+  --dataflow-graph /root/autodl-tmp/structfuse/full_m2_training_data/dataflow_graph.json \\",
          "+  --output-dir /root/autodl-tmp/structfuse/artifacts/stratified_analysis \\",
          "+  --predictions-dir &lt;predictions_dir> \\  # 或 --checkpoints-dir 或 --dry-run",
          "+  --seeds 42,43,44 \\",
          "+  --n-bootstrap 1000",
          "+```",
          "+",
          " ### 输出",
          "-- `stratified_results.json`: 完整 per-stratum 指标 + bootstrap CI",
          "+- `stratified_results.json`: 完整 per-stratum 指标 + bootstrap CI (5 维度)",
          " - `stratified_summary.csv`: 紧凑表格",
          "-- `stratified_plots.pdf`: 分组柱状图 + heatmap + delta 趋势",
          "+- `stratified_plots.pdf`: 分组柱状图 + heatmap + delta 趋势 (5 维度)",
          " ",
          "-## 2. 维度覆盖",
          "+## 2. 维度覆盖 — 全部 5/5 ✅",
          " ",
          "-| # | 维度 | 状态 | 说明 |",
          "-|---|------|------|------|",
          "-| 1 | **Repo size** | ✅ 已实现 | small(<50), medium(50-200), large(200-500), xlarge(500+) — M1 instance count per repo |",
          "-| 2 | **Pool size** | ✅ 已实现 | small(<20), medium(20-40), large(40-51) — neg_candidates 数量 |",
          "-| 3 | **Query-positive similarity** | ✅ 已实现 | low(0-0.3), medium(0.3-0.6), high(0.6-1.0) — cosine sim 或 text overlap |",
          "-| 4 | **Structural data availability** | ❌ 未实现 | 需新增：按 dataflow graph 边数分层 |",
          "-| 5 | **neg_difficulty quartile** | ❌ 未实现 | 需新增：按 negative difficulty (margin) 分四等分 |",
          "+| # | 维度 | 状态 | 分层 | 说明 |",
          "+|---|------|------|------|------|",
          "+| 1 | **Repo size** | ✅ | small/medium/large/xlarge | M1 instance count per repo |",
          "+| 2 | **Pool size** | ✅ | small/medium/large | neg_candidates 数量 |",
          "+| 3 | **Query-positive similarity** | ✅ | low/medium/high | cosine sim 或 text overlap |",
          "+| 4 | **Structural data availability** | ✅ 新增 | sparse/moderate/rich | dataflow graph 边数 |",
          "+| 5 | **neg_difficulty quartile** | ✅ 新增 | Q1_easy/Q2/Q3/Q4_hard | text overlap proxy margin |",
          " ",
          "-## 3. 阻塞点",
          "+### 新增维度实现细节",
          " ",
          "-### 3.1 Checkpoint 路径不匹配",
          "-脚本查找 `{strategy}_s{seed}/best/`，但实际路径是 `{strategy}_s{seed}/best_by_recall_at_1/`。",
          "+**Structural data availability**: 从 `dataflow_graph.json` 统计每个 query_id 的边数，按 DATAFLOW_BINS 分层：",
          "+- sparse (0-1 边): 1546 instances (51.9%)",
          "+- moderate (2-9 边): 498 instances (16.7%)",
          "+- rich (10+ 边): 936 instances (31.4%)",
          " ",
          "-**修复方案**: 在 `main()` 中 checkpoint 路径解析处增加对 `best_by_recall_at_1` 和 `best_by_val_loss` 的查找逻辑。",
          "+**neg_difficulty quartile**: CPU 友好的 text-overlap proxy。计算 margin = (query-pos Jaccard overlap) - max(query-neg Jaccard overlap)，按 quartile 分四等分，margin 越小 → negative 越难。每个 quartile ~745 instances。",
          " ",
          "-### 3.2 缺少 embedding_distance / dataflow_aware checkpoints",
          "-`/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/` 只有 `random_s42/43/44`，无 `embedding_distance` 和 `dataflow_aware` checkpoint。",
          "+## 3. 已完成的修改",
          " ",
          "-跨策略对比需要等这些策略的训练完成。",
          "+1. **新增 `DATAFLOW_BINS` 和 `NEG_DIFFICULTY_QUARTILE_LABELS` 常量**",
          "+2. **新增 `load_dataflow_edges()` 函数** — 加载 dataflow graph 并返回 {file_key: edge_count}",
          "+3. **新增 `assign_neg_difficulty_quartiles()` 函数** — 基于 text overlap proxy 计算 margin 并按 quartile 分配",
          "+4. **扩展 `assign_strata()`** — 增加 `dataflow_edges` 参数，分配 `dataflow_bin`",
          "+5. **新增 `--dataflow-graph` 参数**",
          "+6. **修复 checkpoint 路径解析** — 依次查找 `best/`, `best_by_recall_at_1/`, `best_by_val_loss/`，需 model.pt 存在",
          "+7. **扩展 `write_summary_csv()` 和 `make_plots()`** — 接受新维度数据，自动生成对应图表",
          " ",
          "-### 3.3 GPU 占用",
          "-两块 GPU 正在训练，无法用 `--checkpoints-dir` 做 model inference。",
          "+## 4. 阻塞点（真实数据分析）",
          " ",
          "-### 3.4 无预计算预测文件",
          "-没有 `eval_retrieval.py` 产出的 per-instance prediction JSON，`--predictions-dir` 模式无法使用。",
          "+### 4.1 缺少 embedding_distance / dataflow_aware checkpoints",
          "+`m2_full_qwen/` 只有 `random_s42/43/44`。跨策略对比需要这些策略的训练 checkpoint。",
          " ",
          "-## 4. 缺失维度的实现方案",
          "+### 4.2 无预计算预测文件",
          "+`--predictions-dir` 模式需要 `eval_retrieval.py` 产出的 per-instance JSON。",
          " ",
          "-### 4.1 Structural data availability",
          "+### 4.3 GPU 占用",
          "+model inference 需要 GPU，当前被训练占用。",
          " ",
          "-**数据源**: `/root/autodl-tmp/structfuse/full_m2_training_data/dataflow_graph.json`",
          "-- 376,069 条 file→edges 映射，覆盖 11,205 个 instance",
          "-- Val 数据中所有 2,980 个 query 都有 graph 条目",
          "-- 但 51.9% (1,546/2,980) 的 query 仅有 1 条边",
          "+## 5. Dry-run 验证",
          " ",
          "-**分层方案**:",
          "-```python",
          "-DATAFLOW_BINS = {",
          "-    \"sparse\": (0, 2),      # 0-1 条边 — 无/极少 dataflow 信息",
          "-    \"moderate\": (2, 10),    # 2-9 条边",
          "-    \"rich\": (10, float(\"inf\")),  # 10+ 条边 — 丰富 dataflow 信息",
          "-}",
          "-```",
          "+运行 `--dry-run --seeds 42 --n-bootstrap 200 --dataflow-graph ...`，全部 5 维度成功产出：",
          " ",
          "-**实现**: 在 `assign_strata()` 中加载 graph，统计每个 query_id 的边数，分配 `dataflow_bin`。在 `main()` 中增加 `run_stratified_analysis(all_results, \"dataflow_bin\", ...)`。",
          "-",
          "-### 4.2 neg_difficulty quartile",
          "-",
          "-**定义**: margin = pos_sim - max(neg_sims)。margin 越小，negative 越难。",
          "-",
          "-**问题**: 需要 model forward pass 计算 embedding 相似度 → 需 GPU。",
          "-",
          "-**替代方案 (CPU)**:",
          "-- 用 text overlap (Jaccard token similarity) 代替 embedding similarity 作为 proxy",
          "-- 从 val data 中计算 query-neg 的 text overlap，取 max，得到 proxy margin",
          "-- 按 quartile 分四等分",
          "-",
          "-**实现**:",
          "-```python",
          "-def compute_neg_difficulty_proxy(sample):",
          "-    q_tokens = set(sample[\"query_tokens\"][:1000].split())",
          "-    p_tokens = set(sample[\"pos_tokens\"][:1000].split())",
          "-    pos_overlap = len(q_tokens & p_tokens) / max(len(q_tokens | p_tokens), 1)",
          "-    max_neg_overlap = 0",
          "-    for neg_id in sample[\"neg_candidates\"][:7]:",
          "-        neg_text = sample[\"candidate_tokens\"].get(neg_id, \"\")",
          "-        if neg_text:",
          "-            n_tokens = set(neg_text[:1000].split())",
          "-            overlap = len(q_tokens & n_tokens) / max(len(q_tokens | n_tokens), 1)",
          "-            max_neg_overlap = max(max_neg_overlap, overlap)",
          "-    return pos_overlap - max_neg_overlap  # margin proxy",
          " ```",
          "+/root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v2/",
          "+├── stratified_results.json  (5 维度，含 by_dataflow + by_neg_difficulty)",
          "+├── stratified_summary.csv   (dataflow + neg_difficulty 行已加入)",
          "+└── stratified_plots.pdf     (113KB，含新维度的 bar chart + heatmap + delta)",
          "+```",
          " ",
          "-然后按 quartile 分成 Q1(easiest) - Q4(hardest)。",
          "-",
          "-## 5. Dry-run 验证结果",
          "-",
          "-成功运行 `--dry-run --seeds 42 --n-bootstrap 200`，产出:",
          "-- `/root/autodl-tmp/structfuse/artifacts/stratified_dryrun/stratified_results.json` ✅",
          "-- `/root/autodl-tmp/structfuse/artifacts/stratified_dryrun/stratified_summary.csv` ✅",
          "-- `/root/autodl-tmp/structfuse/artifacts/stratified_dryrun/stratified_plots.pdf` ✅",
          "-",
          "-数据规模: 2,980 val instances, 123 repos, 44,173 M1 instances。",
          "-",
          " ## 6. 下一步行动",
          " ",
          " | 优先级 | 任务 | 依赖 |",
          " |--------|------|------|",
          "-| P0 | 修复 checkpoint 路径解析 (best_by_recall_at_1) | 无 |",
          "-| P0 | 添加 structural data availability 维度 | 无 (CPU) |",
          "-| P0 | 添加 neg_difficulty quartile 维度 (text proxy) | 无 (CPU) |",
          "-| P1 | 用现有 random checkpoints 生成 per-instance predictions | GPU 空闲后 |",
          "-| P1 | 用 predictions 跑真实 3 维度分层分析 | P1 上一步 |",
          "+| P1 | 用现有 random checkpoints 生成 per-instance predictions (eval_retrieval.py) | GPU 空闲后 |",
          "+| P1 | 用 predictions 跑 5 维度分层分析 (random only) | P1 上一步 |",
          " | P2 | 训练 embedding_distance / dataflow_aware checkpoints | GPU + 训练时间 |",
          " | P2 | 跨策略全 5 维度完整分析 | P2 上一步 |",
          " ",
          " ## 7. 相关文件清单",
          " ",
          " ```",
          "-脚本:",
          "-  /root/structfuse/evaluation/analyze_stratified.py        # 主分析脚本",
          "-  /root/structfuse/scripts/analyze_bm25_overlap_stratified.py  # BM25 overlap 分层 (独立)",
          "+脚本 (已修改):",
          "+  /root/structfuse/evaluation/analyze_stratified.py        # 910 行，5 维度完整",
          " ",
          " 数据:",
          "-  /root/autodl-tmp/structfuse/full_m1_data/all.jsonl       # M1 元数据 (44,173 instances)",
          "-  /root/autodl-tmp/structfuse/full_m2_training_data/       # Val/Train JSONL (3 strategies × 3 seeds)",
          "-  /root/autodl-tmp/structfuse/full_m2_training_data/dataflow_graph.json  # Dataflow 图 (376K edges)",
          "+  /root/autodl-tmp/structfuse/full_m1_data/all.jsonl",
          "+  /root/autodl-tmp/structfuse/full_m2_training_data/val_*.jsonl",
          "+  /root/autodl-tmp/structfuse/full_m2_training_data/dataflow_graph.json",
          " ",
          " Checkpoints (仅 random):",
          "   /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s{42,43,44}/best_by_recall_at_1/",
          "   /root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_recall_at_1/",
          " ",
          " Dry-run 输出:",
          "-  /root/autodl-tmp/structfuse/artifacts/stratified_dryrun/",
          "+  /root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v2/",
          " ```"
        ]
      }
    ],
    "originalFile": "# Plan 005: 分层分析报告\n\n**日期**: 2026-05-14\n**状态**: 部分完成 — 管道验证通过，真实分析有阻塞\n\n## 1. 脚本路径与参数\n\n**脚本**: `/root/structfuse/evaluation/analyze_stratified.py` (781 行)\n\n### 参数\n\n| 参数 | 说明 | 默认值 |\n|------|------|--------|\n| `--m1-data` | M1 all.jsonl 路径 (必须) | — |\n| `--val-data-dir` | val_*.jsonl 目录 | — |\n| `--output-dir` | 输出目录 (必须) | — |\n| `--predictions-dir` | 预计算预测 JSON 目录 (CPU) | None |\n| `--checkpoints-dir` | Checkpoint 目录 (需 GPU) | None |\n| `--dry-run` | Mock 预测，用于测试管道 (CPU) | False |\n| `--seeds` | 逗号分隔的种子 | 42,43,44 |\n| `--device` | 推理设备 | cuda |\n| `--n-bootstrap` | Bootstrap 迭代数 | 1000 |\n| `--repo-size-bins` | 自定义 repo size 分组 | None |\n| `--pool-size-bins` | 自定义 pool size 分组 | None |\n| `--sim-bins` | 自定义 similarity 分组 | None |\n\n### 输入模式 (三选一)\n1. `--dry-run`: Mock 数据，CPU，用于管道验证 ✅ 已验证通过\n2. `--predictions-dir`: 加载已有预测结果，CPU ⛔ 无数据\n3. `--checkpoints-dir`: 从 checkpoint 做 forward pass，GPU ⛔ GPU 占用中\n\n### 输出\n- `stratified_results.json`: 完整 per-stratum 指标 + bootstrap CI\n- `stratified_summary.csv`: 紧凑表格\n- `stratified_plots.pdf`: 分组柱状图 + heatmap + delta 趋势\n\n## 2. 维度覆盖\n\n| # | 维度 | 状态 | 说明 |\n|---|------|------|------|\n| 1 | **Repo size** | ✅ 已实现 | small(<50), medium(50-200), large(200-500), xlarge(500+) — M1 instance count per repo |\n| 2 | **Pool size** | ✅ 已实现 | small(<20), medium(20-40), large(40-51) — neg_candidates 数量 |\n| 3 | **Query-positive similarity** | ✅ 已实现 | low(0-0.3), medium(0.3-0.6), high(0.6-1.0) — cosine sim 或 text overlap |\n| 4 | **Structural data availability** | ❌ 未实现 | 需新增：按 dataflow graph 边数分层 |\n| 5 | **neg_difficulty quartile** | ❌ 未实现 | 需新增：按 negative difficulty (margin) 分四等分 |\n\n## 3. 阻塞点\n\n### 3.1 Checkpoint 路径不匹配\n脚本查找 `{strategy}_s{seed}/best/`，但实际路径是 `{strategy}_s{seed}/best_by_recall_at_1/`。\n\n**修复方案**: 在 `main()` 中 checkpoint 路径解析处增加对 `best_by_recall_at_1` 和 `best_by_val_loss` 的查找逻辑。\n\n### 3.2 缺少 embedding_distance / dataflow_aware checkpoints\n`/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/` 只有 `random_s42/43/44`，无 `embedding_distance` 和 `dataflow_aware` checkpoint。\n\n跨策略对比需要等这些策略的训练完成。\n\n### 3.3 GPU 占用\n两块 GPU 正在训练，无法用 `--checkpoints-dir` 做 model inference。\n\n### 3.4 无预计算预测文件\n没有 `eval_retrieval.py` 产出的 per-instance prediction JSON，`--predictions-dir` 模式无法使用。\n\n## 4. 缺失维度的实现方案\n\n### 4.1 Structural data availability\n\n**数据源**: `/root/autodl-tmp/structfuse/full_m2_training_data/dataflow_graph.json`\n- 376,069 条 file→edges 映射，覆盖 11,205 个 instance\n- Val 数据中所有 2,980 个 query 都有 graph 条目\n- 但 51.9% (1,546/2,980) 的 query 仅有 1 条边\n\n**分层方案**:\n```python\nDATAFLOW_BINS = {\n    \"sparse\": (0, 2),      # 0-1 条边 — 无/极少 dataflow 信息\n    \"moderate\": (2, 10),    # 2-9 条边\n    \"rich\": (10, float(\"inf\")),  # 10+ 条边 — 丰富 dataflow 信息\n}\n```\n\n**实现**: 在 `assign_strata()` 中加载 graph，统计每个 query_id 的边数，分配 `dataflow_bin`。在 `main()` 中增加 `run_stratified_analysis(all_results, \"dataflow_bin\", ...)`。\n\n### 4.2 neg_difficulty quartile\n\n**定义**: margin = pos_sim - max(neg_sims)。margin 越小，negative 越难。\n\n**问题**: 需要 model forward pass 计算 embedding 相似度 → 需 GPU。\n\n**替代方案 (CPU)**:\n- 用 text overlap (Jaccard token similarity) 代替 embedding similarity 作为 proxy\n- 从 val data 中计算 query-neg 的 text overlap，取 max，得到 proxy margin\n- 按 quartile 分四等分\n\n**实现**:\n```python\ndef compute_neg_difficulty_proxy(sample):\n    q_tokens = set(sample[\"query_tokens\"][:1000].split())\n    p_tokens = set(sample[\"pos_tokens\"][:1000].split())\n    pos_overlap = len(q_tokens & p_tokens) / max(len(q_tokens | p_tokens), 1)\n    max_neg_overlap = 0\n    for neg_id in sample[\"neg_candidates\"][:7]:\n        neg_text = sample[\"candidate_tokens\"].get(neg_id, \"\")\n        if neg_text:\n            n_tokens = set(neg_text[:1000].split())\n            overlap = len(q_tokens & n_tokens) / max(len(q_tokens | n_tokens), 1)\n            max_neg_overlap = max(max_neg_overlap, overlap)\n    return pos_overlap - max_neg_overlap  # margin proxy\n```\n\n然后按 quartile 分成 Q1(easiest) - Q4(hardest)。\n\n## 5. Dry-run 验证结果\n\n成功运行 `--dry-run --seeds 42 --n-bootstrap 200`，产出:\n- `/root/autodl-tmp/structfuse/artifacts/stratified_dryrun/stratified_results.json` ✅\n- `/root/autodl-tmp/structfuse/artifacts/stratified_dryrun/stratified_summary.csv` ✅\n- `/root/autodl-tmp/structfuse/artifacts/stratified_dryrun/stratified_plots.pdf` ✅\n\n数据规模: 2,980 val instances, 123 repos, 44,173 M1 instances。\n\n## 6. 下一步行动\n\n| 优先级 | 任务 | 依赖 |\n|--------|------|------|\n| P0 | 修复 checkpoint 路径解析 (best_by_recall_at_1) | 无 |\n| P0 | 添加 structural data availability 维度 | 无 (CPU) |\n| P0 | 添加 neg_difficulty quartile 维度 (text proxy) | 无 (CPU) |\n| P1 | 用现有 random checkpoints 生成 per-instance predictions | GPU 空闲后 |\n| P1 | 用 predictions 跑真实 3 维度分层分析 | P1 上一步 |\n| P2 | 训练 embedding_distance / dataflow_aware checkpoints | GPU + 训练时间 |\n| P2 | 跨策略全 5 维度完整分析 | P2 上一步 |\n\n## 7. 相关文件清单\n\n```\n脚本:\n  /root/structfuse/evaluation/analyze_stratified.py        # 主分析脚本\n  /root/structfuse/scripts/analyze_bm25_overlap_stratified.py  # BM25 overlap 分层 (独立)\n\n数据:\n  /root/autodl-tmp/structfuse/full_m1_data/all.jsonl       # M1 元数据 (44,173 instances)\n  /root/autodl-tmp/structfuse/full_m2_training_data/       # Val/Train JSONL (3 strategies × 3 seeds)\n  /root/autodl-tmp/structfuse/full_m2_training_data/dataflow_graph.json  # Dataflow 图 (376K edges)\n\nCheckpoints (仅 random):\n  /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s{42,43,44}/best_by_recall_at_1/\n  /root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_recall_at_1/\n\nDry-run 输出:\n  /root/autodl-tmp/structfuse/artifacts/stratified_dryrun/\n```\n",
    "userModified": false
  },
  "sourceToolAssistantUUID": "0e3a2853-ff69-4b3f-afce-5a355d7a5677",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---


### Assistant

_source line 245 · 2026-05-14T20:25:28.355Z_

Now let me register this artifact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35865531-75a4-482d-a498-82ae5a08ff4f",
  "isSidechain": false,
  "requestId": "req_011Cb365omYTM3ieUtvaKe7o",
  "type": "assistant",
  "uuid": "ba537026-258a-402b-ab7b-13bab25fd3af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FGEvejxnyfM8Xh5Edj96m1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2418,
      "cache_read_input_tokens": 104743,
      "output_tokens": 82,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2418,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 82,
          "cache_read_input_tokens": 104743,
          "cache_creation_input_tokens": 2418,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2418
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 246 · 2026-05-14T20:25:28.435Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Qzt48ccZANXTihRibJKX16`</summary>

```json
{
  "query": "register_artifact",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba537026-258a-402b-ab7b-13bab25fd3af",
  "isSidechain": false,
  "requestId": "req_011Cb365omYTM3ieUtvaKe7o",
  "type": "assistant",
  "uuid": "0fec26a2-35b5-4656-8cf5-531fa97fc40d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FGEvejxnyfM8Xh5Edj96m1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2418,
      "cache_read_input_tokens": 104743,
      "output_tokens": 82,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2418,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 82,
          "cache_read_input_tokens": 104743,
          "cache_creation_input_tokens": 2418,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2418
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 247 · 2026-05-14T20:25:28.443Z_

<details><summary>↩ Tool result · `toolu_01Qzt48ccZANXTihRibJKX16`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0fec26a2-35b5-4656-8cf5-531fa97fc40d",
  "isSidechain": false,
  "promptId": "9e9b674e-9fc3-475b-a334-fc014d0bb425",
  "type": "user",
  "uuid": "645bfebb-730c-4b01-9c4a-c2a24a03c397",
  "toolUseResult": {
    "matches": [],
    "query": "register_artifact",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "0fec26a2-35b5-4656-8cf5-531fa97fc40d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 248 · 2026-05-14T20:25:28.499Z_

```json
{
  "parentUuid": "645bfebb-730c-4b01-9c4a-c2a24a03c397",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "f95db227-7161-4176-ab46-42ad05960cd7",
  "timestamp": "2026-05-14T20:25:28.499Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Runtime record

_source line 249_

```json
{
  "type": "last-prompt",
  "leafUuid": "f95db227-7161-4176-ab46-42ad05960cd7",
  "sessionId": "cd11087d-991b-47e1-b3c6-f81e960f8388"
}
```

---


### Runtime record

_source line 250_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze stratified embedding vs random effectiveness",
  "sessionId": "cd11087d-991b-47e1-b3c6-f81e960f8388"
}
```

---


### Assistant

_source line 251 · 2026-05-14T20:25:39.350Z_

完成。总结：

## 结果

**`analyze_stratified.py` 已修改 (781→910 行)，全部 5 个分层维度实现完毕，dry-run 验证通过。**

### 已完成
1. **找到脚本** — `/root/structfuse/evaluation/analyze_stratified.py`
2. **补齐 2 个缺失维度**：
   - **Structural data availability** — 基于 dataflow_graph.json 边数分 sparse/moderate/rich (分布: 52%/17%/31%)
   - **neg_difficulty quartile** — CPU 友好的 text-overlap proxy，按 margin 分 Q1-Q4
3. **修复 checkpoint 路径** — 支持 `best_by_recall_at_1/` 和 `best_by_val_loss/`
4. **新增 `--dataflow-graph` 参数**
5. **CSV 和 PDF 图表** 均已扩展覆盖 5 个维度

### 阻塞（真实数据分析）
- **只有 random 策略 checkpoint**，无 embedding_distance / dataflow_aware → 无法做跨策略对比
- **无 per-instance prediction JSON** → `--predictions-dir` 模式不可用
- **GPU 被训练占用** → `--checkpoints-dir` 模式不可用

### 下一步
GPU 空闲后用 `eval_retrieval.py` 对现有 random checkpoint 生成 per-instance predictions，再用 `--predictions-dir` 跑真实分析。完整跨策略分析需等 embedding/dataflow checkpoint 训练完成。

报告已写入 `artifacts/plan005_stratified_analysis_report.md`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f95db227-7161-4176-ab46-42ad05960cd7",
  "isSidechain": false,
  "requestId": "req_011Cb3663LrrkExPuUxUfxk6",
  "type": "assistant",
  "uuid": "d80bc453-8ea0-4da4-bc91-533eae775c55",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016wYBKj1R1stERKSkEBPZiH",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 203,
      "cache_read_input_tokens": 107161,
      "output_tokens": 479,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 203,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 479,
          "cache_read_input_tokens": 107161,
          "cache_creation_input_tokens": 203,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 203
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Runtime record

_source line 252_

```json
{
  "type": "last-prompt",
  "leafUuid": "d80bc453-8ea0-4da4-bc91-533eae775c55",
  "sessionId": "cd11087d-991b-47e1-b3c6-f81e960f8388"
}
```

---


### Runtime record

_source line 253_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze stratified embedding vs random effectiveness",
  "sessionId": "cd11087d-991b-47e1-b3c6-f81e960f8388"
}
```

---
