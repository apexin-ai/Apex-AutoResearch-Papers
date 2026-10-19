# deploy bjb1 32546 cuda5 fill

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb1-32546-cuda5-fill_20260520T143627_result.json`
- **Structured JSON:** [`ba6251c7aef4004ebc44.json`](../../sessions/ba/ba6251c7aef4004ebc44.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

注册表中已有同名实验（DONE, success_rate=0.1, 之前在 bjb2-28827 上跑的，无 CRM checkpoint）。DONE→RUNNING 转换被拒绝。但进程已在运行中。

**部署完成：**
- **exp_id**: eval-random-selection-object-seed45
- **PID**: 468175
- **GPU**: bjb1-32546 cuda:5
- **tmux**: `eval-random-selection-object-seed45`
- **输出**: `logs/eval_random_selection_object_seed45.json`

注意：该 exp_id 在 registry 中已有一条 DONE 记录（旧跑：bjb2-28827, 10% success rate, 无 CRM checkpoint, 输出文件名不同）。当前这次跑法加了 `--crm_checkpoint`，配置不同。如需区分，可用新 exp_id 重新注册。

---
