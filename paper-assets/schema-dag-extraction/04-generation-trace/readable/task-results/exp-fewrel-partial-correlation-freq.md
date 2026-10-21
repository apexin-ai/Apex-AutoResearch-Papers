# exp fewrel partial correlation freq

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_fewrel_partial_correlation_freq_20260516T093306_result.json`
- **Structured JSON:** [`ac47b7776327f4f53b4e.json`](../../sessions/ac/ac47b7776327f4f53b4e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果：

**FewRel 是完美平衡数据集**（每种 relation 恰好 700 样本），type frequency 方差为 0，不可能是 BCS-confusion 关系的 confound。

| 指标 | 值 |
|------|-----|
| Raw Pearson r (BCS vs pairwise confusion) | **0.187**, p = 2.56e-26 |
| 95% CI (10k bootstrap) | [0.145, 0.231] |
| Spearman ρ | 0.227, p = 3.63e-38 |
| Partial r (dataset frequency) | = raw r（零方差协变量，undefined） |
| Partial r (eval-level frequency) | 0.189（仅变化 1.2%） |
| n_pairs | 3160 (C(80,2)) |

**Reviewer 回应要点**：FewRel is a balanced dataset with exactly 700 samples per relation type. Type frequency is constant and cannot confound the BCS-accuracy relationship (zero-variance covariate makes partial correlation undefined/equal to raw correlation). Even when using evaluation-level frequency variation as a secondary control, the correlation changes by only 1.2%.

结果保存在服务器 `artifacts/fewrel_partial_correlation_freq/results.json`，registry 已更新为 DONE。

---
