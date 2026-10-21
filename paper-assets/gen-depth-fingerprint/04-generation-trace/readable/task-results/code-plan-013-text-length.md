# code plan 013 text length

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan-013-text-length_20260514T234122_result.json`
- **Structured JSON:** [`0fd75a268833e664b572.json`](../../sessions/0f/0fd75a268833e664b572.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。输出文件已生成：
- `data/text_length_analysis.json` (13KB)
- `data/text_length_boxplot.png` (102KB)

### 结果摘要

**1. 长度分布**：depth 0 的文本最长（~175-181 词），随深度增加略有下降，但方差增大（std 从 ~27 增至 ~55-65）。olmo-2-1b 是例外，深度越大反而越长。

**2. Spearman 相关性**（word_count vs depth）：

| Model | ρ | p-value | Sig |
|---|---|---|---|
| pythia-2.8b | -0.057 | 9.9e-05 | Yes |
| pythia-1b | -0.066 | 9.6e-06 | Yes |
| olmo-2-1b | +0.134 | 2.7e-20 | Yes |
| qwen3-0.6b | +0.012 | 0.43 | No |
| qwen3-1.7b | +0.085 | 6.7e-09 | Yes |

相关性虽统计显著但绝对值很小（|ρ| < 0.14），长度与深度弱相关。

**3. 归一化特征**（窗口200词）：所有 5 个模型的 TTR/hapax 深度趋势在归一化后**完全保留**，且 Spearman ρ 绝对值反而增大（如 pythia-2.8b: -0.633 → -0.715）。**长度不是 TTR/hapax 深度趋势的混淆因素。**

**4. 长度匹配分类器**：匹配后 macro-F1 反而**上升**（avg Δ = +0.041），说明移除长度变异后分类更纯净。**长度不是主要混淆因素**。

**5. Dropout**：20/20 个深度转换中，dropout 样本的平均词数都低于保留样本（如 pythia-1b depth 3→4: lost=41词 vs kept=158词）。**短文本显著更容易 dropout。**

---
