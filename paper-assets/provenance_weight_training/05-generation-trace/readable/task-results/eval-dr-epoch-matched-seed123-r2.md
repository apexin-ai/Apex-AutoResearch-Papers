# eval dr epoch matched seed123 r2

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_dr_epoch_matched_seed123_r2_20260522T020907_result.json`
- **Structured JSON:** [`a75e25eb9658be82514f.json`](../../sessions/a7/a75e25eb9658be82514f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 显示 `dr_epoch_matched_seed123_r2` 已经是 DONE 状态，且 metrics 已完整：

| 数据集 | Loss | PPL |
|--------|------|-----|
| holdout | 2.8713 | 17.6591 |
| owt | 2.9069 | 18.2991 |
| wiki | 2.7208 | 15.1918 |

holdout_ppl=17.659 与 baseline seed42 的 17.651 接近，符合预期。

eval 已全部完成并写入 registry，无需重复执行。

---
