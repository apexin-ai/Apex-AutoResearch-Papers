# code dgs gold filter rerun

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_dgs_gold_filter_rerun_20260518T173617_result.json`
- **Structured JSON:** [`9c301abc9a145739d2b5.json`](../../sessions/9c/9c301abc9a145739d2b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。`gold_filter=True` 结果已写入 `output/dgs_selection_results.json`（metadata 中标记 `gold_filter: true`）。

### 结果汇总

| Dataset | Total | Used | Filtered | Degen% | Greedy | LP-all | DGS | Oracle | DGS-Greedy |
|---------|-------|------|----------|--------|--------|--------|-----|--------|------------|
| SciERC  | 551   | 529  | 22       | 18.5%  | 0.6417 | 0.6403 | 0.6400 | 0.7785 | -0.17pp |
| CoNLL   | 3453  | 2756 | 697      | 57.9%  | 0.9070 | 0.8989 | 0.8989 | 0.9494 | -0.81pp |
| FewNERD | 5000  | 4351 | 649      | 14.4%  | 0.7478 | 0.7610 | 0.7615 | 0.8686 | +1.37pp |

### Bootstrap 95% CI (DGS vs Greedy)
- **SciERC**: -0.0017 [-0.0154, +0.0122] (not significant)
- **CoNLL**: -0.0081 [-0.0122, -0.0040] (significant negative)
- **FewNERD**: +0.0137 [+0.0091, +0.0186] (significant positive)

### 与旧结果差异（无 gold filter → gold_filter=True）
- **SciERC**: 过滤 22 条，DGS 从 0.6507 降至 0.6400（-1.07pp），主要因为 LP-all 下降
- **CoNLL**: 过滤 697 条（均为 gold 为空的句子），退化率从 62.0% 降至 57.9%，DGS 微升 +0.04pp
- **FewNERD**: 过滤 649 条，退化率从 23.1% 大幅降至 14.4%，DGS gain 从 +0.92pp 增至 +1.37pp

FewNERD 变化最大：大量 gold 为空的 instance 之前被算作退化（所有 sample F1=0），过滤后退化率显著降低，DGS 的正向增益更突出。

---
