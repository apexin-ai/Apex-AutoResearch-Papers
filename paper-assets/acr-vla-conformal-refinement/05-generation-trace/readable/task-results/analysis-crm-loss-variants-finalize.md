# analysis crm loss variants finalize

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_crm-loss-variants-finalize_20260522T063402_result.json`
- **Structured JSON:** [`b5de98d2fb3eda19cac6.json`](../../sessions/b5/b5de98d2fb3eda19cac6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**实际状态**：3 个实验中只有 `crm-loss-perdof` 还在 ANALYZING，已推到 DONE。`crm-loss-mse-baseline` 和 `crm-loss-conformal` 此前已是 DONE 状态，checkpoint_path / log_path 均已设置，无需操作。

**checkpoint 路径**（均在 bjb1-18228）：
- mse-baseline: `/root/autodl-tmp/checkpoints/crm_loss_variants/mse/crm_best.pt`
- perdof: `/root/autodl-tmp/checkpoints/crm_loss_variants/perdof_weighted/crm_best.pt`
- conformal: `/root/autodl-tmp/checkpoints/crm_loss_variants/conformal_guided/crm_best.pt`

附带发现：`crm-loss-combined` 也在 ANALYZING 且具备 checkpoint + conclusion=success，不在本次任务范围，未处理。

---
