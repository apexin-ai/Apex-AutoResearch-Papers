# harvest stale running cleanup

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_stale-running-cleanup_20260527T233143_result.json`
- **Structured JSON:** [`4563b76c4dfc48ed66f8.json`](../../sessions/45/4563b76c4dfc48ed66f8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 8 个实验已处理完毕。实际上这些实验在 registry 中**已经是 DONE 状态**（可能之前的 hook 或 agent 已自动收割）。我补充了缺失的 per_task metrics、log_path 和 checkpoint_path。

## 汇总

| # | exp_id | conclusion | SR% | 备注 |
|---|--------|-----------|-----|------|
| 1 | eval_pi05_l2norm_k09_long_seed43_strict_cqa1 | success | **81.2%** | L2norm k=0.9 seed43, 完整 500ep |
| 2 | eval_pi05_l2norm_k095_long_seed43_strict_w38 | success | **85.8%** | L2norm k=0.95 seed43, 完整 500ep |
| 3 | eval_openvla_attn_k075_long_seed42 | success | **37.4%** | 已是 DONE，partial 430/500ep (timeout) |
| 4 | eval_pi05_l2norm_k085_long_seed42 | killed | **77.8%** | 已是 DONE，标记 CONTAMINATED (lenient condition)，被 v4 supersede |
| 5 | eval_openvla_random_k095_object_seed42 | success | **67.4%** | 完整 500ep |
| 6 | eval_pi05_random_k07_long_seed42 | success | **62.4%** | 已是 DONE，标记 CONTAMINATED |
| 7 | eval_openvla_random_k075_goal_seed42 | success | **72.0%** | 完整 500ep |
| 8 | eval_openvla_attn_k075_goal_seed42 | success | **67.4%** | 完整 500ep，补充了 per_task |

所有 8 个实验在 registry 中均已是 DONE 状态，无需再做状态转换。已补充了缺失的 per_task metrics 数据。当前 RUNNING 实验均为 s44 批次（14 个）。

---
