# analysis eval acr object v4 scalar

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval-acr-object-v4-scalar_20260515T160921_result.json`
- **Structured JSON:** [`a7f2c178de85d2cf9423.json`](../../sessions/a7/a7f2c178de85d2cf9423.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**结果：scalar_unc CRM v3-norm on LIBERO Object = 9.0% SR (9/100)**

- 4/10 tasks 完全失败 (0%)，最好的 chocolate_pudding 30%
- 略高于 argmin baseline (6.7%)，但低于 obs_only (13.3%) 和 vla_mean (10.0%)
- 结论：**negative** — scalar uncertainty 信号不足以提供有效的 correction 方向信息，obs_only 的全观测 embedding 明显更优

Registry 已更新 (status=DONE, conclusion=negative)，报告已注册。

---
