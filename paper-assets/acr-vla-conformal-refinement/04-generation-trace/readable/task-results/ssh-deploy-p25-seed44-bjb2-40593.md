# ssh deploy p25 seed44 bjb2 40593

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_deploy-p25-seed44-bjb2-40593_20260520T002327_result.json`
- **Structured JSON:** [`5331a7ed8bbe7d30d2f0.json`](../../sessions/53/5331a7ed8bbe7d30d2f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署就绪，全部检查通过：

- **Checkpoint**: `/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt` 已存在（1.3MB，May 15）
- **代码版本**: `evaluate.py` 593 行，含 19 处 `adaptive_k` 引用，确认是新版

bjb2-40593 上 checkpoint 和代码均已就绪，可以直接启动 eval-adaptive-k-p25-seed44 实验。

---
