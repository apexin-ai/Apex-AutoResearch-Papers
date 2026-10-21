# code mvp pipeline

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp-pipeline_20260514T161549_result.json`
- **Structured JSON:** [`4ef0a2c8a48265db7020.json`](../../sessions/4e/4ef0a2c8a48265db7020.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

`/root/schema-dag-extraction/src/` 下创建了 8 个文件，全部语法和 CLI 验证通过：

| 文件 | 功能 |
|------|------|
| `few_nerd_utils.py` | Few-NERD 数据加载，token-level BIO → span-level 转换 |
| `compute_type_embeddings.py` | 用 Qwen3 causal LM 计算 66 个 type 的 mean-pooled last-layer embeddings |
| `compute_bcs.py` | 计算 pairwise cosine similarity 矩阵和 BCS 分数，输出 heatmap |
| `select_type_batches.py` | 贪心选择 low/high BCS type batch + 随机采样，输出 JSON 配置 |
| `run_extraction.py` | vLLM constrained JSON decoding NER extraction，批量推理 |
| `evaluate.py` | exact/relaxed span matching，计算 micro P/R/F1 |
| `run_experiment.py` | 主入口，串联全流程，支持 dry_run / exp1 / exp2 三种模式 |
| `analyze_results.py` | Pearson correlation、t-test、Cohen's d 统计分析 + 学术图表输出 |

运行前需准备：
1. `configs/few_nerd_types.json` — 66 个 type 的 name→definition 映射
2. 先跑 `compute_type_embeddings.py` 生成 embeddings，再跑 `run_experiment.py`（避免同时加载两个模型 OOM）

---
