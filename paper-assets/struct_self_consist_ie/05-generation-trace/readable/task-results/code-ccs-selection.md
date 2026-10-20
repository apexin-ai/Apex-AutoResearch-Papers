# code ccs selection

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ccs_selection_20260518T173312_result.json`
- **Structured JSON:** [`33c2a921aeaa1ae44436.json`](../../sessions/33/33c2a921aeaa1ae44436.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

## CCS 评估结果 (gold_filter=True, N=8)

| Dataset | N | Greedy | LP | DGS | **CCS** | Oracle | CCS-Greedy 95% CI |
|---------|-----|--------|--------|--------|---------|--------|-------------------|
| SciERC  | 529 | 0.6439 | 0.6501 | 0.6513 | 0.6501  | 0.7758 | +0.61pp [-0.70, +2.00] |
| CoNLL   | 2756| 0.9070 | 0.8989 | 0.8989 | 0.8964  | 0.9494 | -1.05pp [-1.49, -0.62] |
| FewNERD | 4351| 0.7478 | 0.7610 | 0.7615 | 0.7277  | 0.8686 | -2.01pp [-2.59, -1.43] |

**Stage 分布：**
| Dataset | Stage1 greedy | Stage2 MV | Stage3 LP |
|---------|---------------|-----------|-----------|
| SciERC  | 94 (17.8%)    | 217 (41.0%) | 218 (41.2%) |
| CoNLL   | 1597 (57.9%)  | 579 (21.0%) | 580 (21.0%) |
| FewNERD | 628 (14.4%)   | 1861 (42.8%)| 1862 (42.8%)|

**关键发现：** CCS 在所有数据集上均未超过 DGS。实体 majority vote（Stage 2）在 low-LP-range 的 non-degenerate instances 上表现不如 LP selection，尤其在 FewNERD 上 CCS 比 DGS 低 3.4pp。span-based `(start, end, type)` majority voting 过于严格，不同 samples 即使语义一致，span 边界也常不同，导致 consensus 质量低。

输出文件：
- JSON: `output/ccs_selection_results.json`
- 报告: `output/ccs_selection_report.md`
- 脚本: `code/ccs_selection.py`

---
