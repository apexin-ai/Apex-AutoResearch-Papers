# ssh unified lp best recompute

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_unified_lp_best_recompute_20260522T064332_result.json`
- **Structured JSON:** [`9ebb884d3f0867945e4c.json`](../../sessions/9e/9ebb884d3f0867945e4c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已完成。汇总如下：

## 统一 Instance 集 LP-best F1 结果

### SciERC (529 gold-nonempty instances, unified baseline from N=8 greedy)

| N | LP-best F1 | LP Δ(pp) |
|---|-----------|----------|
| 8 | 0.6651 | -0.32 |
| 16 | 0.6635 | -0.48 |
| 32 | 0.6708 | +0.25 |
| 64 | 0.6712 | +0.29 |

LP baseline (greedy F1): **0.6683**

### CoNLL (2756 gold-nonempty instances, unified baseline from N=8 greedy)

| N | LP-best F1 | LP Δ(pp) |
|---|-----------|----------|
| 8 | 0.8961 | -1.62 |
| 16 | 0.8887 | -2.36 |
| 32 | 0.8923 | -2.00 |
| 64 | 0.8889 | -2.34 |

LP baseline (greedy F1): **0.9123**

**关键发现**：LP-best 在两个数据集上均未超越 greedy baseline，CoNLL 上甚至有 -1.6 到 -2.4pp 的下降。这说明 mean log-probability 不是一个有效的样本选择器——即使选了模型自评"最确信"的样本，entity extraction 质量依然不如 greedy 解码。SciERC 在 N=32/64 时 LP-best 略微回正（+0.25/+0.29pp），但幅度很小。

脚本已保存至服务器 `code/lp_best_unified.py`，结果保存至 `output/unified_lp_best_results.txt`。

---
