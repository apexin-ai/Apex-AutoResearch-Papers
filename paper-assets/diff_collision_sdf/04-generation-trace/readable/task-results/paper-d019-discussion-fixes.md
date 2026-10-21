# paper d019 discussion fixes

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_d019_discussion_fixes_20260525T080714_result.json`
- **Structured JSON:** [`278d992671371e7ede24.json`](../../sessions/27/278d992671371e7ede24.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个修正完成：

1. **Fix 1** (line 15): `oracle_true_gt_feature_object_v11` → `oracle_true_gt_feature_v11`。被 killed 的实验改为实际有 metrics (CAR=76.9%) 的正确实验 ID。

2. **Fix 2** (line 27): Boundary 2 开头添加了数据溯源——标注 seed 0 evaluation、两个 training exp_id (`train_pi05_a1_obj_s0_l005`, `train_pi05_a1_obj_s0_l01`) 和 baseline 来源 (`eval_pi05_safelibero_object_v11`, 3-seed average)。Registry 中无独立的 10K eval 实验条目，数据来自 D012 mid-eval artifacts。

3. **Fix 3** (line 36): "baseline CAR = 10%" → "3-seed average baseline CAR = 10%"。Registry 显示 seed 0 Task 0 CAR = 6%，D012 报告的 10.0% 是 3-seed 平均值，已标注来源。49pp = avg(62−10, 56−10) 验证一致。

---
