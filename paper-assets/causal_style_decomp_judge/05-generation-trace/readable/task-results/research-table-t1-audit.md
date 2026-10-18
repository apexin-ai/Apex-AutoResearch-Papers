# research table t1 audit

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_table_t1_audit_20260524T083003_result.json`
- **Structured JSON:** [`c28c9b8d9212e6c82cf3.json`](../../sessions/c2/c28c9b8d9212e6c82cf3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。以下是完整的排查结论。

---

## 排查结果

### 1. d=1.120 的 provenance chain

| 环节 | 详情 |
|------|------|
| **生成脚本** | `csd_pipeline/cross_benchmark_analysis.py` |
| **输出文件** | `artifacts/r14_fixes/cross_benchmark_local.json`（`likert_d: 1.1597`） |
| **数据文件** | `scored_alpacaeval_llama70b_formality.jsonl`（旧版本，含 pairwise 字段，现已被新实验覆盖） |
| **样本量** | n=48 consistent pairs（旧数据），45-46 formal wins |
| **公式** | **Cohen's h**（arcsine transform）：`h = 2*arcsin(√win_rate) - 2*arcsin(√0.5)` |
| **代码位置** | `likert_from_pairwise()` 函数，因 `likert_file=None` 而走此分支 |

### 2. d=0.211 的 provenance chain

| 环节 | 详情 |
|------|------|
| **生成脚本** | `analysis/llama70b_crossbench_scoring.py` |
| **输出文件** | `data/llama70b_crossbench_summary.json` |
| **数据文件** | `data/scored_alpacaeval_llama70b_formality.jsonl`（新版本，含 score_formal/score_casual） |
| **样本量** | n=86（全部 NLI-pass 记录） |
| **公式** | 真正的 **Cohen's d**：`d = ATE / pooled_SD = 0.186 / 0.882 = 0.211` |

### 3. 根因：两个独立的错误

**错误 A：指标标签错误（d=1.120 is Cohen's h, not Cohen's d）**

旧脚本对 AlpacaEval × Llama-70B 配置了 `likert_file: None`（当时还没做独立 Likert 评分），于是走了 `likert_from_pairwise()` 函数。该函数从 pairwise win/loss 数据计算 **Cohen's h**（arcsine 变换），但输出字段命名为 `likert_d`。论文 Table T1 把它和其他行的真正 Cohen's d 放在同一列中，构成标签错误。

Cohen's h = 1.155 对应的语义是"45/47 的 win rate"——这本身不是错的，但它和 Cohen's d（Likert 均值差/pooled SD）是完全不同的指标，量级不可比。

**错误 B：BT 计算中对 inconsistent pairs 的处理不同（75.6% vs 95.7%）**

| 分析版本 | Inconsistent pairs 处理 | BT P(formal) |
|----------|----------------------|--------------|
| 旧分析 | 包含全部 86 对（含 39 inconsistent），每个 inconsistent 对贡献 1 formal-win + 1 casual-win → 稀释信号 | **75.6%** |
| 新分析 | 仅用 47 consistent 对（45 formal-wins / 2 casual-wins） | **95.7%** |

### 4. 正确的 d 值

基于独立 Likert 评分（1-10 scale，n=86）：

- Mean formal = 8.14, Mean casual = 7.95
- ATE = 0.186, pooled SD = 0.882
- **Cohen's d = 0.211**（Wilcoxon p = 0.012，显著）
- Tie rate = 79.1%

### 5. 建议

论文 Table T1 中该单元格应更正为 **d=0.211**，使用与其他行一致的 Cohen's d（Likert 标准化均值差）。BT 值应使用一致的 inconsistent pairs 处理策略。

---
