# analysis permutation equivalence test

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_permutation_equivalence_test_20260522T015431_result.json`
- **Structured JSON:** [`e35d537a58d8fdc3573e.json`](../../sessions/e3/e35d537a58d8fdc3573e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果摘要：

| 指标 | 值 |
|------|-----|
| Observed interaction | -0.48 pp |
| Permutation p (H0: interaction=0) | 0.914 |
| Permutation TOST p (equivalence) | 0.285 |
| Null distribution SD | 4.26 pp |
| Equivalence supported | **No** |

**核心问题**：每个 cell 只有 12-13 个 batch（25 batches per count level → median split），导致 permutation null distribution 的 SD (4.26 pp) 远大于 ±3pp equivalence margin。Permutation TOST 没有足够统计功效来建立等价性。

这与 logit 尺度 TOST p=0.209 一致——都是功效不足的问题，不是效应量的问题。

**LaTeX 段落的策略**：我写了一段 "complementary evidence" 风格的文字，强调：
1. Point estimate 极小 (0.48 pp ≪ 3 pp margin)
2. p=0.914 说明 interaction 与零无法区分
3. 承认 TOST 不显著是因为 cell size 限制
4. 将其定位为"corroborates"parametric TOST 而非独立证明

如果你想要更强的结果，有两个可能的方向：
- **使用所有 7 个 count level** 做回归型 permutation test（permute BCS 在所有 175 batches 内），power 会大很多
- **使用连续 BCS**（不做 median split）做 permutation regression，避免信息损失

要我尝试其中一种方案？

---
