# analysis d140 oracle gated selection

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d140_oracle_gated_selection_20260518T130246_result.json`
- **Structured JSON:** [`4d14dff8678337c61fc9.json`](../../sessions/4d/4d14dff8678337c61fc9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果汇总：

## D140 Oracle Degeneracy-Gated LP Selection 结果

| | Few-NERD | SciERC | CoNLL |
|---|---|---|---|
| **Instances** | 32,565 | 529 | 2,756 |
| **Degeneracy rate** | 13.8% | 17.8% | **59.1%** |
| **Greedy F1** | 79.11 | 66.63 | 91.23 |
| **Oracle F1** | 88.55 | 78.08 | 95.43 |
| **Ungated LP delta** | +0.07 | -0.31 | -1.62 |
| **Gated delta** | +0.13 | -0.26 | -1.59 |
| **Gated vs Ungated improvement** | +0.06 | +0.06 | +0.03 |
| **NonDegen LP delta** (vs nondeg greedy) | +0.15 | -0.29 | **-3.05** |

### 关键发现

1. **Oracle gating 在所有数据集上都有正向改善**（+0.03 ~ +0.06），验证了 degeneracy 确实引入噪声。

2. **但改善幅度很小**，因为 degeneracy 只是两个必要条件之一。即使 oracle 移除了所有 degenerate instances，LP selection 在 non-degenerate subset 上仍然可能不 work：
   - CoNLL non-degenerate LP delta = **-3.05**（LP 在非退化 instance 上反而更差）
   - SciERC non-degenerate LP delta = **-0.29**

3. **CoNLL degeneracy 极高（59.1%）**，因为模型在 CoNLL 上准确度高，大多数 sample 输出完全一致。

4. 这直接支持论文核心 claim：LP selection 需要 **low degeneracy + LP alignment** 两个条件同时满足。Oracle gating 只解决了 degeneracy 条件，alignment 问题仍在。

**产出文件**：
- 脚本：`code/d140_oracle_gated_analysis.py`
- 结果：`output/d140_oracle_gated/results.json`

---
