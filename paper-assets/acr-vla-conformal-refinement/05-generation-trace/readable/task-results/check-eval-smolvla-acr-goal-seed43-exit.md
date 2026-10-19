# check eval smolvla acr goal seed43 exit

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_eval-smolvla-acr-goal-seed43-exit_20260522T055347_result.json`
- **Structured JSON:** [`2faf04a8f2bcda4b5205.json`](../../sessions/2f/2faf04a8f2bcda4b5205.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/failed，cron 不存在（可能已被删除）。

**故障原因**：`crm_best.pt` checkpoint 的输入维度（990）与 evaluate.py 构建的 CRM 模型输入维度（1030）不匹配。差值 40 说明 `obs_dim` 参数传的是 960，但模型架构代码期望的 obs 维度更大（可能近期代码改动了 obs 拼接逻辑，增加了额外特征）。需要用匹配的 `obs_dim` 重新训练 CRM 或修正 evaluate.py 的模型构建参数。

---
