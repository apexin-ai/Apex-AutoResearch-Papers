# eval dr epoch matched seed123

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_dr_epoch_matched_seed123_20260521T233903_result.json`
- **Structured JSON:** [`9f6e99160c124b6d4d9f.json`](../../sessions/9f/9f6e99160c124b6d4d9f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。Registry 已更新为 DONE。

**结果汇总：**

| Dataset | Loss | PPL |
|---------|------|-----|
| Holdout | 2.9087 | **18.332** |
| OWT | 2.9099 | 18.354 |
| Wiki | 2.7050 | 14.955 |

**注意：** holdout_ppl = 18.332，比预期的 ~17.65（seed42 epoch-matched 的结果）高 0.68。这说明 seed 间方差较大，seed123 在 epoch-matched 条件下表现明显更差。需要结合 `detect_remove_q05_v2_seed123`（full D&R）的结果一起分析，才能判断 epoch confound 在 seed123 上的占比。

---
