# analysis exp002 full pipeline

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp002_full_pipeline_20260521T134340_result.json`
- **Structured JSON:** [`b3cce0a65ea5348d95cd.json`](../../sessions/b3/b3cce0a65ea5348d95cd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 执行状态

| # | 脚本 | 状态 | 输出文件 |
|---|------|------|----------|
| 1 | per_benchmark_gstudy | **OK** (14.8s) | 12K |
| 2 | gradient_permutation_test | **OK** (15.0s) | 2.4K |
| 3 | leave_one_benchmark_out | **OK** (15.1s) | 3.1K |
| 4 | within_format_gradient | **OK** (15.2s) | 3.3K |
| 5 | gsm8k_answer_reextract | **FAILED** | 无输出 |
| 6 | cross_benchmark_dstudy | **OK** (15.0s) | 2.5K |

**Script 5 错误**：`gsm8k_answer_reextract.py:70` — `original_predicted` 列含 NaN（float），`normalize_numeric` 未处理。修复：在函数开头加 `if pd.isna(answer): return None`。

---

## per_benchmark_gstudy 核心结果

| Benchmark | item_id% | model:item_id% | G_item | min_n(G≥0.80) |
|-----------|----------|----------------|--------|---------------|
| **arc** | **48.90%** | 38.20% | 0.8307 | 164 |
| hellaswag | 44.47% | 32.31% | 0.8324 | 162 |
| mmlu | 41.55% | 32.81% | 0.8159 | 181 |
| gsm8k | 11.99% | 12.09% | 0.7289 | 298 |

MATH（来自 gradient_permutation_test 输出）：item_id% = **4.78%**，model:item% = **46.07%**

梯度方向符合预期：MC 题 item_id% 高（arc 49% → mmlu 42%），自由格式低（gsm8k 12% → math 5%）。model:item% 反向梯度在 MATH 上最突出（46%），说明模型间在 MATH 难题上的差异交互最大。

---

## gradient_permutation_test

- item_id 递减：**p = 0.0083**（显著）
- model:item 递增：**p = 0.0083**（显著）
- 联合检验：**p = 0.0000**
- 单调性：均为 False（arc > hellaswag > mmlu 的排序不完美，但整体趋势显著）

---

## cross_benchmark_dstudy — G≥0.80 所需 items

| Benchmark | 当前 G | G≥0.80 | G≥0.90 | G≥0.95 |
|-----------|--------|--------|--------|--------|
| hellaswag | 0.8324 | **162** | 363 | 766 |
| arc | 0.8307 | **164** | 367 | 775 |
| mmlu | 0.8159 | **181** | 407 | 858 |
| gsm8k | 0.7289 | **298** | 670 | 1413 |

GSM8K 需要近 300 题才能达 G≥0.80，是 MC 类 benchmark 的 ~1.8 倍。要达 G≥0.95，GSM8K 需 1413 题——当前 200 题远远不够。

---

**待修复**：`gsm8k_answer_reextract.py` 第 70 行的 NaN 处理。需要我现在修吗？

---
