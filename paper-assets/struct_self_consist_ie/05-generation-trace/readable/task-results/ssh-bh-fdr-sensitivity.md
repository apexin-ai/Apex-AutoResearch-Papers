# ssh bh fdr sensitivity

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_bh_fdr_sensitivity_20260522T033313_result.json`
- **Structured JSON:** [`cfbb2fb067071dd7de96.json`](../../sessions/cf/cfbb2fb067071dd7de96.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果已保存到 `output/bh_fdr_sensitivity_results.txt`。

核心结论：

**BH-FDR 比论文当前的 Holm-Bonferroni 更宽松，不会削弱任何结论：**

| 方法 | Rejected / 57 | Selection tests surviving |
|------|---------------|---------------------------|
| Holm-Bonferroni (论文现用) | 10 | 0 |
| BH-FDR α=0.01 | 10 | #6, #19, #21 (3个) |
| BH-FDR α=0.05 | 19 | #6, #18, #19, #20, #21 (5个) |
| BH-FDR α=0.10 | 21 | 同上 |
| BH-FDR α=0.20 | 26 | +#8, #13 (7个) |

关键逻辑：
- 15/21 个 selection tests 的 uncorrected p > 0.05，任何校正方法都不可能让它们变显著
- Few-NERD LP selection (p<0.001) 在 BH α=0.01 下仍显著 (BH-adj=0.0029)，但在 Holm 下不显著 (Holm-adj=0.055)
- BH 额外保留了 9 个 Holm 不保留的显著结果（non-tied LP subset、SciERC LP-wt construction 等）
- 论文的核心结论 "no signal reliably beats greedy" 基于大量 non-significant p-values，与校正方法无关

Rebuttal 可以直接引用：换用 BH-FDR 只会让更多正面发现通过校正，不会改变 null findings。

---
