# eval grid b5 0 b3 0 seed456 posthoc

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_grid_b5_0_b3_0_seed456_posthoc_20260515T093323_result.json`
- **Structured JSON:** [`ce00c30f4492374809f8.json`](../../sessions/ce/ce00c30f4492374809f8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。两个实验 registry 已更新为 DONE/success。

**Eval 结果汇总：**

| 实验 | b | seed | eval_ppl | eval_loss | train_loss | tokens |
|------|---|------|----------|-----------|------------|--------|
| grid_b3_0_seed456 | 3.0 | 456 | **17.921** | 2.886 | 5.435 | 4,077,068 |
| grid_b5_0_seed456 | 5.0 | 456 | **17.993** | 2.890 | 5.488 | 4,077,068 |

**Sanity check：** seed456 系列整体偏高（b=2.0 也是 17.99），与其他 seed 的 ~17.7x 有 ~0.2 差距。b=3.0 < b=5.0 的趋势与预期一致（b 越大 PPL 越高）。auto_eval_watcher 已自动完成了 eval，无需手动跑。

---
