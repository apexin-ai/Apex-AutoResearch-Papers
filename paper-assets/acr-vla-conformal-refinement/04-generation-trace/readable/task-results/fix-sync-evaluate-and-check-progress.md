# fix sync evaluate and check progress

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_sync-evaluate-and-check-progress_20260523T010647_result.json`
- **Structured JSON:** [`4ef6c9933c84a5b4dee7.json`](../../sessions/4e/4ef6c9933c84a5b4dee7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

MD5 一致 (`b822bf3fa02895aa5a72ed9843a669ec`)，文件同步完成。

---

## 报告

### 1. bjb2-28827 代码同步：✅ 完成
- `evaluate.py` 已从 bjb1-32546 同步到 bjb2-28827，MD5 校验一致
- `crm_smolvla_3suite_v1` checkpoint 路径已包含在文件中

### 2. bjb1-32546 Eval 进度

**Spatial CRM eval (cuda:0,1,2) — 每个 seed 10 tasks, 20 rollouts/task：**

| Session | 当前 Task | 进度 | 已完成 Tasks |
|---------|----------|------|-------------|
| seed42 | #7 next_to_cookie_box | rollout 5/20 | 6/10 |
| seed43 | #7 next_to_cookie_box | rollout 10/20 | 6/10 |
| seed44 | #7 next_to_cookie_box | rollout 10/20 | 6/10 |

已完成 task 结果 (seed42): between_plate_and_ramekin 80%, next_to_ramekin 75%, from_table_center 75%, on_cookie_box 55%, in_top_drawer 55%, on_ramekin 0%

**Goal CRM eval (cuda:4,5) — 每个 seed 10 tasks：**

| Session | 当前 Task | 进度 | 已完成 Tasks |
|---------|----------|------|-------------|
| seed42 | #6 push_plate_to_stove | rollout 15/20 | 5/10 |
| seed43 | #7 put_cream_cheese_in_bowl | rollout 5/20 | 6/10 |

已完成 task 结果 (seed42): open_middle_drawer 60%, put_bowl_on_stove 85%, put_wine_bottle 60%, open_top_drawer 15%, put_bowl_on_cabinet 60%

**Training (cuda:3):** epoch 33, batch 2400/6316 — 正常运行中

### 3. 预计完成时间
- 所有 GPU 都在正常工作（30% util），没有 eval 完成或退出
- Spatial: 3 个 seed 都在 task 7/10，还剩约 3.5 tasks × 20 rollouts ≈ 剩余 ~35%
- Goal seed42 在 task 6/10 (剩 ~45%)，seed43 在 task 7/10 (剩 ~35%)
- 按当前速度估计还需 **2-4 小时**完成全部 eval

---
