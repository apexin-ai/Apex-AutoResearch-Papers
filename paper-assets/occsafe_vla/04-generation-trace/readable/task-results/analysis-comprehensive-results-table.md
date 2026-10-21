# analysis comprehensive results table

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_comprehensive_results_table_20260524T223512_result.json`
- **Structured JSON:** [`2646a6d52e70a162bc45.json`](../../sessions/26/2646a6d52e70a162bc45.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

CSV 已生成并注册：`artifacts/comprehensive_results.csv` (art_20260524_d8c934)

**39 行，覆盖 15 个 condition：**

| 状态 | 数量 | 说明 |
|------|------|------|
| 有 eval 数据 | 30 行 | TSR/CAR/collisions 完整 |
| training | 6 行 | full_occ_ln ×3, cutoff_15k_s1, cutoff_25k_s2, cutoff_45k_s1, reverse_cutoff_s2 |
| eval_pending | 1 行 | full_occ_retrain_s0（训练完无 eval） |

注意事项：
- 早期 mvp 实验用 20 rollouts (200 episodes)，后续实验用 50 rollouts (500 episodes)
- cutoff_s2_v2_eval 缺 collisions 数据（原始 metrics 中未记录）
- occ_s1_fresh 包含 47500 和 50000 两个 checkpoint 的 eval，分列两行

---
