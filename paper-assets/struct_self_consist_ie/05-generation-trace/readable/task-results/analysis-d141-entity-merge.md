# analysis d141 entity merge

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d141_entity_merge_20260518T132334_result.json`
- **Structured JSON:** [`12e8f91b52e56fab3b3e.json`](../../sessions/12/12e8f91b52e56fab3b3e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

D141 分析完成。总结:

**Entity-level majority voting merge 无法突破 instance-level selection ceiling。**

| Dataset | Greedy | Best Merge | Oracle | Gap Recovered |
|---------|--------|------------|--------|---------------|
| SciERC | 0.6182 | 0.6333 (k=3) | 0.7448 | 11.9% |
| CoNLL | 0.7239 | 0.7223 (k=5) | 0.7639 | -4.0% |
| FewNERD | 0.6507 | 0.6571 (k=4) | 0.7850 | 4.8% |

关键发现:
1. 所有 3 个数据集上 merge vs oracle 差异均统计显著 (bootstrap CI 不含 0)
2. LP-weighted merge 与简单频率投票无明显差异
3. 在 degenerate instances 上 merge 反而略损 (Δ 均为负)
4. 最优阈值低 (k=3-5/N=8-16)，说明 inclusive merge 优于 conservative，但仍不够

**对论文的意义**: 论文应定位为 diagnostic + selection (而非 diagnostic + method)。Oracle gap 很大 (4-13 points)，但简单 voting merge 无法弥补，进一步验证了 instance-level quality estimation 的必要性。

产出文件:
- 脚本: `analysis_d141_entity_merge.py`
- 结果: `output/d141_entity_merge/results.json`
- 报告: `output/d141_entity_merge/report.md`
- 图表: `output/d141_entity_merge/threshold_curve.png`

---
