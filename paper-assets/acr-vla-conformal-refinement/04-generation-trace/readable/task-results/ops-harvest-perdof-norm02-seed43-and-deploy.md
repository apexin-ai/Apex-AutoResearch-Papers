# ops harvest perdof norm02 seed43 and deploy

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_harvest-perdof-norm02-seed43-and-deploy_20260518T105508_result.json`
- **Structured JSON:** [`8e14c5a9d6c3b93abd48.json`](../../sessions/8e/8e14c5a9d6c3b93abd48.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务完成。

---

## 任务 1：eval-perdof-object-norm02-seed43

- **PID 535595** 已退出
- **Overall SR = 9%** (9/100)，与 magnitude_curve_data.json 中的 9% 一致，已验证
- Per-task 分布：chocolate_pudding 40%、orange_juice 30%、salad_dressing 10%、bbq_sauce 10%，其余 6 个 task 0%
- Registry 已更新为 **DONE (success)**
- Perdof ε=0.2 完整数据现为 n=6: [42=11%, **43=9%**, 44=10%, 45=12%, 46=9%, 47=11%]

## 任务 2：eval-perdof-object-default-seed45

- 已部署到 **bjb1-32546 cuda:4**
- **PID: 626277**
- **tmux session: eval_perdof_default_seed45**
- `max_correction_norm: None`（uncapped）确认正确
- 模型已加载，环境正在初始化，开始跑 10 tasks × 10 rollouts
- Registry 状态：**RUNNING**

---
