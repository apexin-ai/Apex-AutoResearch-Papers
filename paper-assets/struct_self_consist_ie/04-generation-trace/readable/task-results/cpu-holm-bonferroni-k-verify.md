# cpu holm bonferroni k verify

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cpu_holm_bonferroni_k_verify_20260521T115959_result.json`
- **Structured JSON:** [`e740835c70607be92f21.json`](../../sessions/e7/e740835c70607be92f21.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结论：

**k=19 与 Table 13 一致**，表中 Selection 家族确实只有 19 行。但差异来源是 **tests #56 和 #57**（SciERC/CoNLL LP favorable subset）——它们是条件 LP **选择**测试，却被分类到了 "Other" 而非 "Selection"。同类型的 test #18（non-tied subset LP selection）反而在 Selection 家族里，形成分类不一致。

如果将 #56、#57 移入 Selection 使 k=21：
- Few-NERD LP 的 Holm-adjusted p 从 **0.019 → ~0.021**，仍显著（< 0.05）
- **无任何显著性结论翻转**
- 需更新 4 处引用（abstract、introduction、single_signal、experiments_main footnote）

建议采用 **Option A**：将 #56/#57 重新归入 Selection 家族，更新 k=21 和 p_adj 数值，消除审稿人质疑。具体修改位置和新值均已记录在 artifact `k_value_verification.md` 中。

---
