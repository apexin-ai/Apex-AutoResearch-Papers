# deploy bjb2 28827 p0b 5exp

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb2-28827-p0b-5exp_20260520T134556_result.json`
- **Structured JSON:** [`c920b74492d74c5aca2f.json`](../../sessions/c9/c920b74492d74c5aca2f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

5 个实验全部提交成功。

| # | exp_id | GPU | PID | plan |
|---|--------|-----|-----|------|
| 1 | `eval-crm-k1-object-seed42-plan702` | cuda:0 | 365485 | plan_702 |
| 2 | `eval-crm-k1-object-seed43-plan702` | cuda:3 | 365759 | plan_702 |
| 3 | `eval-crm-k1-object-seed44-plan702` | cuda:4 | 366294 | plan_702 |
| 4 | `eval-latency-profiling-v1` | cuda:1 | 367510 | plan_602 |
| 5 | `eval-adaptive-k-spatial-p90-seed44-bjb2` | cuda:5 | 367984 | plan_602 |

额外操作：
- **evaluate.py** 已 patch，恢复了 `crm_k1_accg` mode（从 .bak 移植 `MultiScaleCRM` 加载 + `select_action_crm_k1_accg` 函数）
- **profile_latency.py** 新建于 `src/`，测量 prefix encode / VLA sampling (K=1,5,10,20) / CGS scoring / CRM inference 各组件独立延迟
- 实验 5 因原 exp_id 已被 bjb1-18228 占用，改用 `eval-adaptive-k-spatial-p90-seed44-bjb2`
- cuda:2 未触碰

---
