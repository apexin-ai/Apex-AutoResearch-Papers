# check crm 4suite training done

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_crm-4suite-training-done_20260523T013151_result.json`
- **Structured JSON:** [`a1add1e453611338ac42.json`](../../sessions/a1/a1add1e453611338ac42.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**train-crm-unified-4suite-r5：killed**

- 完成 32/50 epochs，两次在 epoch 33 中途被外部 kill（无 traceback，怀疑 OOM 或实例中断）
- Best val_loss = **0.006075**（epoch 32），对比 3-suite 的 0.005878 略高
- val_loss 在 32 epochs 内仍持续下降，未收敛
- Checkpoint 可用：`/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt`（1.3MB）+ `checkpoint_epoch0032.pt`（3.9MB，可恢复训练）

Registry 已更新为 DONE/killed，cron 已删除。

---
