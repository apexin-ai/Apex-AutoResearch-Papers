# analysis diverse prompt accuracy and scatter fix

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_diverse-prompt-accuracy-and-scatter-fix_20260520T025854_result.json`
- **Structured JSON:** [`27ffe40cd0eb47e52538.json`](../../sessions/27/27ffe40cd0eb47e52538.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**子任务 1 结果**：
| Method | Majority-Vote Accuracy | 来源 |
|--------|----------------------|------|
| Diverse-Prompt | **54.41%** (111/204) | exp-077 per-question 数据，12 traces majority vote |
| SC | 54.41% (111/204) | exp-077 交叉验证（vs 原始 56.86%，因 n_raters 6-12 不一致） |
| Debate | 49.02% (100/204) | exp-077 交叉验证（vs 原始 38.24%，不同实验参数） |

27 个 diverse answers 无法归一化为 True/False/Unknown（如 "Partially True"、实体陈述句等），但 fuzzy normalization 后结果不变（仍 54.41%）。

**子任务 2 完成**：
- Diverse-Prompt accuracy: 55.0% → **54.41%**
- X 轴标签: "Trace Correlation" → **"Output Correlation"**
- 生成文件：
  - `docs/paper/figures/f6_kappa_accuracy_scatter.pdf`
  - `docs/paper/figures/f6_kappa_accuracy_scatter.png`

---
