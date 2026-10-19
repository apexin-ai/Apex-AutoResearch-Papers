# code d062 analysis script

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d062_analysis_script_20260516T110856_result.json`
- **Structured JSON:** [`e04a71c266cd0703079c.json`](../../sessions/e0/e04a71c266cd0703079c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

### 产出

**脚本**：`/root/structfuse/scripts/d062_analysis.py`

功能：
1. **Summary Table** — 读取所有 `selection_*.json`，按 strategy × criterion × seed 生成交叉表（终端打印 + CSV）
2. **Stratified Analysis** — criterion main effect / strategy main effect / interaction 分析 → JSON
3. **Bootstrap CI** — binomial bootstrap（n_queries 次 Bernoulli），95% CI + pairwise P(alt > random) → JSON

**dry-run 结果**（5 个文件，`--partial` 模式）：

| Config | R@1 | 95% CI |
|--------|-----|--------|
| random_s42_best_by_val_loss | 23.02% | [19.25, 26.39] |
| random_s42_best_by_recall_at_1 | 23.02% | [19.25, 26.59] |
| random_s43_best_by_val_loss | 34.13% | [30.15, 38.49] |
| random_s43_best_by_recall_at_1 | 50.40% | [46.42, 54.56] |
| random_s44_best_by_val_loss | 35.32% | [31.15, 39.09] |

Criterion main effect (random only): **+5.89 pp**（by_recall_at_1 优于 by_val_loss）

**3 个输出文件**均生成成功并可正常 `json.load()` 读取。Pairwise comparisons 待 embedding_distance / dataflow_aware 结果就绪后自动填充。

---
