# code m2 data pipeline prep

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_m2_data_pipeline_prep_20260513T013038_result.json`
- **Structured JSON:** [`9876020fb01502a7aa32.json`](../../sessions/98/9876020fb01502a7aa32.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据收集完毕，以下是汇总报告。

---

## Part 1: M2 数据构建脚本预检

### `build_m1_training_data.py` — 就绪，有 1 个依赖需确认

**CLI 参数：**
| 参数 | 说明 | 对应值 |
|------|------|--------|
| `--extraction-dir` (必填) | M1 提取结果 | `/root/autodl-tmp/structfuse/m1_extraction/` |
| `--repos-dir` (必填) | 源码目录 | `/root/structfuse/m1_repos/` |
| `--output-dir` (必填) | 输出 JSONL | 建议 `/root/autodl-tmp/structfuse/m2_training_data/` |
| `--embedding-mining-mode` | static / dynamic | static 产出 3 个策略文件，dynamic 产出 1 个 |
| `--pool-size` | 候选池大小 | 默认 50 |
| `--max-per-repo` | 每 repo 最多样本数 | 默认 200 |

**3 种策略实现：**
- **random**: 从 repo 内非 positive 文件随机采样 negatives
- **embedding** (实际用 BM25): 用 `rank_bm25.BM25Okapi` 对 query 文件做相似度排序，取最相似的非 positive 文件作为 hard negatives（call graph 邻居**不排除**）
- **dataflow**: 同 embedding，但 `full_connected`（positive + call graph 邻居）全部从 negative pool 排除

**两级连通性设计：**
- `positive_files`: 直接跨文件 dataflow 连接（训练 positive）
- `full_connected`: positive_files ∪ call graph 邻居（dataflow 策略的排除集）

**输出文件（static 模式）：** `train_random.jsonl`, `train_embedding.jsonl`, `train_dataflow.jsonl`, `val.jsonl`, `dataflow_graph.json`

**依赖状态：**
- `rank_bm25` ✅ 已安装（`/root/miniconda3/lib/python3.12/site-packages/rank_bm25.py`）
- `sentence_transformers` ✅ 已安装
- 标准库 ✅

**问题：** 无阻塞问题，脚本就绪可运行。

---

### `train.py` — 关键参数汇总

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--model-name` | Qwen/Qwen2.5-Coder-3B | 基座模型 |
| `--train-file` | 必填 | JSONL 训练数据 |
| `--val-file` | 必填 | JSONL 验证数据 |
| `--output-dir` | 必填 | checkpoint 保存路径 |
| `--hard-negative-strategy` | dataflow_aware | random / embedding_distance / dataflow_aware |
| `--learning-rate` | 2e-5 | |
| `--temperature` | 0.07 | InfoNCE 温度 |
| `--batch-size` | 8 | |
| `--num-epochs` | 3 | |
| `--num-negatives` | 7 | |
| `--hard-negative-ratio` | 0.5 | |
| `--use-lora` | flag | 启用 LoRA (r=16) |
| `--gradient-checkpointing` | flag | |
| `--max-seq-length` | 2048 | |
| `--dynamic-mining` | flag | 每 epoch 重新挖负样本 |
| `--dataflow-graph-file` | 可选 | 传入 dataflow_graph.json |
| `--candidate-pool-file` | 可选 | dynamic 模式的候选池 |
| `--eval-steps` | 500 | |
| `--save-steps` | 1000 | |
| `--wandb-project` | structfuse | |

**⚠️ 问题：** `train.py` 第 2 行硬编码 `os.environ["CUDA_VISIBLE_DEVICES"] = "4"` — 训练前需要改掉或删除。

**checkpoint 保存：** `_save_checkpoint()` 保存到 `--output-dir`，需确保设为 `/root/autodl-tmp/` 下路径。

---

### M1 数据格式样例

```json
{
  "instance_id": "Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh",
  "repo": "swesmith/Cog-Creators__Red-DiscordBot.33e0eac7",
  "github_repo": "Cog-Creators/Red-DiscordBot",
  "base_commit": "33e0eac7",
  "buggy_file": "redbot/cogs/audio/managed_node/ll_version.py",
  "buggy_function": "LavalinkOldVersion",
  "gold_patch_files": ["redbot/cogs/audio/managed_node/ll_version.py"],
  "call_graph": [{"target_func": "...", "hop_distance": N, "direction": "caller/callee", "file_path": "...", ...}],
  "dataflow_paths": [{"source_file": "...", "source_line": N, "sink_file": "...", "sink_line": N}],
  "inter_procedural": true,
  "extraction_method": "codeql",  // 或 "beniget"（无 call_graph/dataflow）
  "extraction_time_s": 37.36,
  "error": null
}
```

**M1 当前状态：**
- 目录大小：2.2 GB
- 已提取 23 个 repo（`m1_repos/` 下 23 个源码目录 + 8 个 codeql_db）
- skip_log.jsonl: 660 条 `clone_failed` 记录
- 两种提取方法共存：`beniget`（call_graph/dataflow_paths 为空）和 `codeql`（有丰富数据）

---

## Part 2: M3a 评估框架状态

### 已有代码 — 比预期完善得多

`/root/structfuse/evaluation/eval_swebench.py` **已经是完整的 E2E 评估脚本**：

- **Pipeline**: issue description → StructFuse context retrieval → vLLM (Qwen3.6-27B) patch generation → 评估
- 支持 `--swebench-split` (lite/verified/pro)
- 支持 `--bm25-only` baseline
- 支持 `--use-fusion` 融合头
- 断点续传（`load_completed_instances`）
- 依赖 `eval_retrieval.py` 中的 `StructFuseRetriever`, `FusionRanker`, `bm25_retrieve`
- 输出 per-instance 结果 + summary.json (Pass@1, avg recall, avg tokens)

**关键参数：** `--model-path`（StructFuse checkpoint）、`--llm-endpoint`（默认 localhost:8000）、`--llm-model`（Qwen3.6-27B）、`--max-context-tokens`（16000）

### 已有 eval 结果

`/root/structfuse/eval_results/` 下有 P2B 评估结果（3 策略 × 3 seed），说明 P2B 评估已跑完。

### M3a 待做

1. **vLLM 部署 Qwen3.6-27B** — 脚本假设 localhost:8000 有 vLLM 端点
2. **SWE-bench 数据集下载** — 需 `datasets` 库从 HuggingFace 下载（需 network_turbo + HF_HUB_DISABLE_XET=1）
3. 验证 `eval_retrieval.py` 中的 `StructFuseRetriever` 能正确加载 M2 训练后的 checkpoint

### 依赖状态

- `datasets` — 需确认是否已安装
- `rank_bm25` ✅
- `requests` / `tqdm` / `numpy` ✅（conda base 基础包）
- 不需要安装 `swebench` 包（脚本自实现评估逻辑）

---

## 预估

| 项目 | 预估 |
|------|------|
| M2 数据构建时间 | 10-30 分钟（取决于 23 repos 的文件数量，embedding 策略需 BM25 计算） |
| M2 输出空间 | ~2-5 GB（3 策略 JSONL + val + graph） |
| ⚠️ 磁盘空间 | `/root/autodl-tmp/` 仅剩 **16 GB (91%)**，需注意 |

**关键行动项：**
1. M1 全量完成后 → 直接运行 `build_m1_training_data.py`，参数就绪
2. 训练前删除 `train.py` 第 2 行的 `CUDA_VISIBLE_DEVICES=4` 硬编码
3. 确保 `--output-dir` 指向 `/root/autodl-tmp/structfuse/` 下
4. 磁盘紧张，可能需要清理旧数据或 codeql_db 目录

---
