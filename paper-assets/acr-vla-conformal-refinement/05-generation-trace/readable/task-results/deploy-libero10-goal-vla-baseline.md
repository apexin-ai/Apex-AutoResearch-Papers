# deploy libero10 goal vla baseline

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_libero10-goal-vla-baseline_20260519T163640_result.json`
- **Structured JSON:** [`cf611dfbe754b988245b.json`](../../sessions/cf/cf611dfbe754b988245b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

## 执行总结

### Step 1: evaluate.py benchmark 支持
- `--benchmark long` → `libero_10` (LIBERO-10)
- `--benchmark goal` → `libero_goal` (LIBERO-Goal)
- 无需代码修改

### Step 4: 6 个实验已部署并启动

| exp_id | benchmark | seed | server | GPU | 状态 |
|--------|-----------|------|--------|-----|------|
| eval-vla-only-long-seed42 | LIBERO-10 | 42 | bjb1-32546 | cuda:0 | RUNNING |
| eval-vla-only-long-seed43 | LIBERO-10 | 43 | bjb1-32546 | cuda:2 | RUNNING |
| eval-vla-only-long-seed44 | LIBERO-10 | 44 | bjb1-32546 | cuda:3 | RUNNING |
| eval-vla-only-goal-seed42 | LIBERO-Goal | 42 | bjb1-32546 | cuda:4 | RUNNING |
| eval-vla-only-goal-seed43 | LIBERO-Goal | 43 | bjb1-32546 | cuda:5 | RUNNING |
| eval-vla-only-goal-seed44 | LIBERO-Goal | 44 | bjb2-28827 | cuda:0 | RUNNING |

### Step 5: CRM 覆盖分析
- CRM v3 norm 仅在 **Object + Spatial** (20 tasks) 上训练
- **LIBERO-10 和 LIBERO-Goal 不在 CRM 训练集中**
- CRM eval 需要 zero-shot transfer；建议先跑 zero-shot CRM eval 测泛化性，效果差再 retrain

---
