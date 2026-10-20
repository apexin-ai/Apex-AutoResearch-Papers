# ops diagnose random subset exit

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_diagnose_random_subset_exit_20260524T214331_result.json`
- **Structured JSON:** [`42a3b0889bb2718b590d.json`](../../sessions/42/42a3b0889bb2718b590d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇报如下：

---

## random_subset_epoch_seed42 结果

**训练状态**: 成功完成 6103/6103 steps，`final/` checkpoint 完整。

**Eval PPL**:

| 指标 | Random Subset (multi-epoch) | Uniform (full-data, 1 epoch) | D&R multi-epoch |
|------|---------------------------|------------------------------|-----------------|
| Holdout PPL | **17.694** | ~17.694 | ~17.25 |
| OWT PPL | **18.349** | — | — |
| Wiki PPL | **15.317** | — | — |

**关键发现**: Random subset holdout PPL = 17.694，与 uniform full-data baseline 几乎完全一致。这说明：

1. **多 epoch 训练本身不提供优势** — 在随机数据上多跑几遍 epoch 并不比用全量数据跑一遍好
2. **D&R 的优势来自过滤质量** — D&R multi-epoch (~17.25) 比 random subset multi-epoch (17.694) 好 0.44 PPL，证明 D&R 的质量打分是有效的，不仅仅是 epoch 效应

---
