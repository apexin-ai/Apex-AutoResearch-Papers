# ops exp002 benchmark data

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp002_benchmark_data_20260520T232219_result.json`
- **Structured JSON:** [`61727421dec463448d30.json`](../../sessions/61/61727421dec463448d30.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据准备完成。

### 产出报告

| 数据集 | 状态 | 条数 | Response 长度 (min/mean/max) | 文件大小 |
|--------|------|------|------------------------------|----------|
| `benchmark_alpacaeval.jsonl` | 成功 | 100 | 2 / 519 / 3104 | 75.3KB |
| `benchmark_mtbench.jsonl` | 成功 | 80 | 5 / 1176 / 3736 | 122.9KB |

**数据来源：**
- **AlpacaEval**: HF Hub `tatsu-lab/alpaca_eval` (805 条中随机采样 100 条，seed=42)
- **MT-Bench**: HF `lmsys/mt_bench_human_judgments` parquet，提取 80 个 question 的 GPT-4 first-turn response（每题一条，全部来自 GPT-4）

**格式**：`id`, `instruction`, `response`, `source` — 与 LLMBar 的 `mvp_samples.jsonl` 对齐（后者额外有 `label` 字段）。

**路径**：
- `/root/causal_style_decomp_judge/data/benchmark_alpacaeval.jsonl`
- `/root/causal_style_decomp_judge/data/benchmark_mtbench.jsonl`

---
