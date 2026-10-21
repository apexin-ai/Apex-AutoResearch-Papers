# analysis docred bcs r2

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_docred_bcs_r2_20260519T140257_result.json`
- **Structured JSON:** [`d87157f75c6207152f3b.json`](../../sessions/d8/d87157f75c6207152f3b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存到 `r2_analysis.json`。汇总：

### Per count level (n=55 each)

| Metric | count_16 | count_32 |
|--------|----------|----------|
| **R²** | **0.6528** | **0.6135** |
| R² 95% CI | [0.5272, 0.7661] | [0.4662, 0.7482] |
| Pearson r | −0.808 (p=8.9e-14) | −0.783 (p=1.6e-12) |
| Spearman ρ | −0.762 (p=1.4e-11) | −0.693 (p=4.6e-09) |
| Slope | −0.7317 | −0.6296 |
| Intercept | 0.9775 | 0.8558 |

### Pooled (n=110)
- R² (BCS only) = 0.5779, CI [0.4629, 0.6838]
- R² (BCS + count covariate) = 0.6784
- Semi-partial R² of BCS = 0.5676

### vs. original
- Original count_16: R² = 0.525, n=35, CI [0.27, 0.73]
- Expanded count_16: R² = **0.6528**, n=55, CI [0.53, 0.77] — 更高且 CI 更窄

### 论文引用
**R² = 0.61–0.65 (61–65%)**，替代原来的 "22–53%"。原来那个范围对应的是旧实验（n=35, R²=0.525 是 count_16 的，其他 count levels 的 R² 更低），expanded 实验两个 count level 都稳定在 61–65%。

---
