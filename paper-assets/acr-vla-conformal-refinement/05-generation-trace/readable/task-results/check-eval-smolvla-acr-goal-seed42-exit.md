# check eval smolvla acr goal seed42 exit

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_eval-smolvla-acr-goal-seed42-exit_20260522T055240_result.json`
- **Structured JSON:** [`d8f67bd7cd52ed360025.json`](../../sessions/d8/d8f67bd7cd52ed360025.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 已不存在（可能在进程退出时已被清理）。

**总结：**

- **退出原因**：`RuntimeError` — CRM checkpoint (`crm_v3_norm/obs_only/crm_best.pt`) 输入维度 990 与当前模型期望的 1030 不匹配（差 40 维，涉及 `input_mean`、`input_std`、`net.0.weight`）。
- **状态**：已更新 registry → `DONE / failed`
- **无 output json**，进程在加载 checkpoint 阶段就崩溃了

根因：`obs_dim=960` 时模型总输入维度应为 990（960+30 action），但代码当前构建的模型期望 1030。需要检查 CRM 模型定义中 `obs_dim` 与实际输入拼接逻辑是否在最近被修改过。

---
