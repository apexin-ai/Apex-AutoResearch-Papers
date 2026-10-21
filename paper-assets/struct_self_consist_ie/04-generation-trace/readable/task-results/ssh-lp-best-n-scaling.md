# ssh lp best n scaling

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_lp_best_n_scaling_20260522T050848_result.json`
- **Structured JSON:** [`75414b1fb013d79e5e72.json`](../../sessions/75/75414b1fb013d79e5e72.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果出来了。

## LP-best F1 N-scaling 结果

| Dataset | N | LP-best F1 | Greedy F1 | LP Δ (pp) | #inst | seed |
|---------|---|-----------|-----------|-----------|-------|------|
| SciERC | 8 | 66.51% | 63.48% | +3.03 | 529 | 42 |
| SciERC | 16 | 66.35% | 64.07% | +2.28 | 529 | 42 |
| SciERC | 32 | 67.08% | 63.60% | +3.48 | 529 | 42 |
| SciERC | 64 | 67.12% | 63.79% | +3.33 | 529 | 42 |
| CoNLL | 8 | 89.57% | 89.47% | +0.09 | 2756 | 123 |
| CoNLL | 16 | 90.01% | 88.57% | +1.44 | 2756 | 456 |
| CoNLL | 32 | 89.23% | 88.62% | +0.61 | 2756 | 42 |
| CoNLL | 64 | 88.89% | 88.66% | +0.23 | 2756 | 42 |
| FewNERD | 8 | 79.27% | 71.23% | +8.04 | 32565 | 42 |
| FewNERD | 16 | 79.46% | 71.23% | +8.23 | 32565 | 42 |

**关键发现：**
- **FewNERD LP Δ 最大**（+8pp），Greedy 基线较弱，LP 选择收益显著
- **SciERC LP Δ 稳定在 +2.3–3.5pp**，N 从 8 到 64 几乎没有进一步增长（饱和）
- **CoNLL LP Δ 最小**（+0.1–1.4pp），但注意 N=8 和 N=16 用了不同 seed，不可直接比较 scaling 趋势
- CoNLL 的 Greedy F1 跨 seed 有波动（88.57–89.47%），说明不同 seed 之间有 ~1pp 差异

**缺失数据：** CoNLL N=8/N=16 没有 seed42 文件（分别用 seed123/seed456 替代），FewNERD N=32 数据不存在。

结果已保存到服务器 `output/lp_best_n_scaling_results.txt`。

---
