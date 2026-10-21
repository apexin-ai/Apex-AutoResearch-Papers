# analyze w3 domain lexical stats

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_w3-domain-lexical-stats_20260518T145650_result.json`
- **Structured JSON:** [`2523059e606366d2aae5.json`](../../sessions/25/2523059e606366d2aae5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。输出文件：

- **LaTeX table**: `artifacts/domain_lexical_stats/domain_ttr_entropy.tex`
- **Summary**: `artifacts/domain_lexical_stats/summary.md`

核心发现：

1. **Depth 0 TTR 符合 K\* 排序**：Wiki (0.665) < C4 (0.720) < arXiv (0.755)，Cohen's d(arXiv vs Wiki) = +1.52（大效应）
2. **Depth 0 entropy 不完全符合 K\***：C4 (6.22) < Wiki (6.41) < arXiv (6.85)，Wiki 和 C4 位置互换。原因可能是 Wikipedia 的百科全书式跨主题覆盖提升了 entropy，尽管其 TTR 较低
3. **TTR 排序在 depth ≥ 3 反转**：arXiv 的 TTR 下降最陡（d0→d5 Δ = −0.137），导致 arXiv < Wiki < C4。这表明模型对专业术语词汇的坍缩速度更快
4. **Entropy 排序在 depth ≥ 3 符合 K\***：Wiki < C4 < arXiv
5. **深度平均后 effect size 大幅衰减**：arXiv vs Wiki 的 d 从 ~1.5 降至 ~0.2，说明迭代生成使域间词汇差异趋同，这本身就是词汇维度 model collapse 的信号

---
