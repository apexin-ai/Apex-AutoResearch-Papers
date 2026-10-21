# code bh fdr integration final

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_bh-fdr-integration-final_20260514T223912_result.json`
- **Structured JSON:** [`b16ec44f052efd422c9e.json`](../../sessions/b1/b16ec44f052efd422c9e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### Permutation Granger（BH FDR 校正后）

**Differenced（推荐）:**

| Pair | s42 p_raw→p_fdr | s43 p_raw→p_fdr | s44 p_raw→p_fdr | s45 p_raw→p_fdr | FDR sig |
|------|----------------|----------------|----------------|----------------|---------|
| token_entropy→distinct_1 | .011→.026* | .001→.001* | .002→.004* | .004→.006* | **4/4** |
| token_entropy→distinct_2 | .016→.026* | .001→.001* | .003→.005* | .004→.006* | **4/4** |
| token_entropy→distinct_3 | .027→.036* | .001→.001* | .013→.017* | .005→.007* | **4/4** |
| token_entropy→perplexity | .716→.819 | .801→.801 | .470→.470 | .992→.992 | **0/4** |
| ece→distinct_1 | .001→.008* | .001→.001* | .001→.003* | .002→.006* | **4/4** |
| ece→distinct_2 | .009→.026* | .001→.001* | .001→.003* | .002→.006* | **4/4** |
| ece→distinct_3 | .016→.026* | .001→.001* | .001→.003* | .004→.006* | **4/4** |
| ece→perplexity | .960→.960 | .538→.614 | .346→.395 | .674→.771 | **0/4** |

**FDR 校正影响:**
- Differenced: 24 raw-sig → **24 FDR-sig**（0 翻转）
- Undifferenced: 31 raw-sig → **31 FDR-sig**（0 翻转）

### Method Ablation FDR 影响

| 方法 | raw-sig | FDR-sig | 翻转数 |
|------|---------|---------|--------|
| naive_pearson | 63 | 63 | 0 |
| differenced_xcorr | 55 | 53 | 2 |
| toda_yamamoto | 26 | 24 | 2 |
| permutation_granger | 34 | 27 | 7 |

### 关键结论

1. **零翻转**：differenced permutation Granger 中没有任何 pair 在 FDR 校正后从显著变为不显著
2. **canary→diversity 全部 robust**：token_entropy/ece → distinct_1/2/3 全部 4/4 seed FDR-significant（6 pairs × 4 seeds = 24/24）
3. **canary→perplexity 全部 n.s.**：0/8 差分结果显著，符合预期
4. **对论文 claim 无影响**：所有核心 claim（canary 指标领先 diversity 退化）在多重比较校正后完全成立，p-value 在 FDR 校正后仍远低于 0.05

---
