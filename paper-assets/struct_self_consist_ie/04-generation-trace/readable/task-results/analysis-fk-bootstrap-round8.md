# analysis fk bootstrap round8

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_fk_bootstrap_round8_20260515T153706_result.json`
- **Structured JSON:** [`06941163f3589bd0be9f.json`](../../sessions/06/06941163f3589bd0be9f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果已保存到 `output/analysis_round8/fk_bootstrap_test.json`。

**核心结果：**

| 指标 | 值 |
|------|-----|
| n_valid | 529 |
| Real FK mean | 0.4015 (std=0.30, median=0.37) |
| FK IQR | [0.206, 0.543] |
| Permuted FK mean (null) | **-0.1406** (std=0.0002) |
| Permutation p-value | **p < 0.0001** (0/10000 permutations ≥ real) |
| Split-half reliability | **r = 0.394 ± 0.028** |
| FK-F1 Spearman ρ | 0.267 (p=4.7e-10) |

**结论**：FK within-instance agreement 远超 random baseline（0.40 vs -0.14，p<0.0001），10000 次 permutation 中没有一次达到真实 FK 均值。Split-half reliability r=0.39 表明即使将 8 个 sample 拆成 4+4，FK 信号仍然稳定。这有力回应了 reviewer 关于 FK independence assumption 的质疑——即使 LLM samples 不是完全独立的 raters，FK 仍捕获了有意义的、显著高于随机的 within-instance agreement 信号。

---
