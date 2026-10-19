# check eval smolvla acr long seed42 exit

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_eval-smolvla-acr-long-seed42-exit_20260522T055312_result.json`
- **Structured JSON:** [`22a8704b10debb4ec36f.json`](../../sessions/22/22a8704b10debb4ec36f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 已不存在（可能已被清理）。Registry 已更新完毕。

**结果汇总：**

- **状态**: DONE / failed
- **原因**: CRM checkpoint (`crm_v3_norm/obs_only/crm_best.pt`) 的输入维度与当前模型不匹配。Checkpoint 训练时 obs_dim=960（总输入 990=960+30），但当前模型期望 obs_dim=1000（总输入 1030=1000+30）。需要用匹配的 obs_dim 重新训练 CRM 或调整 evaluate.py 中的 obs_dim 参数。

---
