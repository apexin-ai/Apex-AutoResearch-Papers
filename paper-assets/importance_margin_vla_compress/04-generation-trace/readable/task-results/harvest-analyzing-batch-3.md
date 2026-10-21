# harvest analyzing batch 3

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_analyzing_batch_3_20260528T061646_result.json`
- **Structured JSON:** [`bfdf5804d8ec2aa597a9.json`](../../sessions/bf/bfdf5804d8ec2aa597a9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 registry 更新完成。汇总报告：

---

## [Part A — ANALYZING 收割]

| # | exp_id | SR | per_task |
|---|--------|-----|----------|
| 1 | eval_pi05_l2norm_k095_long_seed45_strict_w38 | **87.8%** (439/500) | [96, 98, 94, 96, 98, 94, 52, 94, 58, 98] |
| 2 | eval_pi05_attn_k09_long_seed44_strict_w38 | **未找到** | w38 上无此日志。最接近: attn_k09_**seed45** SR=65.0% |
| 3 | eval_pi05_random_k085_long_seed44_strict_w41 | **44.2%** (221/500) | [34, 52, 54, 72, 12, 34, 50, 48, 20, 66] |

**Part A #2 说明**：w38 上搜索所有 `*attn_k09*` 日志，只有 seed45 (SR=65.0%)，无 seed44。同时有 `attn_k085_seed44` 和 `attn_k05_seed44`。请确认 exp_id 是否有误。

## [Part B — 无 cron RUNNING 检查]

| # | exp_id | 状态 | SR |
|---|--------|------|-----|
| 1 | eval_pi05_l2norm_k09_long_seed43_strict_cqa1 | ✅ 已完成 → DONE | **81.2%** (406/500) |
| 2 | eval_pi05_l2norm_k095_long_seed43_strict_w38 | ✅ 已完成 → DONE | **87.4%** (437/500) |
| 3 | eval_openvla_attn_k075_long_seed42 (w41) | ❌ 超时失败 → DONE(failed) | EXIT_CODE=124, 8/10 tasks |
| 4 | eval_pi05_l2norm_k085_long_seed42 (cqa1) | ✅ 已完成 → DONE | **78.8%** (394/500) |
| 5 | eval_openvla_random_k095_object_seed42 (w41) | ✅ 已完成 → DONE | **67.4%** (337/500) |
| 6 | eval_pi05_random_k07_long_seed42 (cqa1) | ✅ 已完成 → DONE | **66.0%** (330/500) |
| 7 | eval_openvla_random_k075_goal_seed42 (w38) | ✅ 已完成 → DONE | **72.0%** (360/500) |
| 8 | eval_openvla_attn_k075_goal_seed42 (w27) | ✅ 已完成 → DONE | **67.4%** (337/500) |

## [当前 GPU 占用]

所有旧实验 GPU 已被新实验重用，无实际空闲释放：

| 服务器 | 当前占用 | 空闲 GPU |
|--------|---------|----------|
| w38 | GPU 0,2,3 (3个新实验) + tmux on GPU0 | GPU 1 |
| w41 | GPU 0,1,2,3 (4个新实验) | 无 |
| cqa1 | GPU 0,2 (2个实验) | **GPU 1, 3** |
| w27 | GPU 0 (1个实验) | **GPU 0 以外空闲** |

---
