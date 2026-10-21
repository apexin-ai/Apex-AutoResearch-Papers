# analyze unified crm training check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_unified-crm-training-check_20260522T111651_result.json`
- **Structured JSON:** [`bcea4e887e75e9b1767a.json`](../../sessions/bc/bcea4e887e75e9b1767a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。总结：

**train-crm-unified-4suite → DONE (failed)**

- **失败原因**：EXIT_CODE=124（timeout），仅完成 4/50 epochs 后被系统级 timeout 终止
- **224,555 samples，6316 batches/epoch**，每 epoch 约 25 分钟，4 epochs 共约 2.3 GPU 小时
- **val_loss 仍在持续下降**（0.0108 → 0.0096），远未收敛
- **Checkpoints 已保存**：`/root/autodl-tmp/checkpoints/crm_unified_4suite/` 下有 epoch 1-4 + `crm_best.pt`（best val_loss=0.009633 @ epoch 4）

需要重新提交训练，移除 timeout 限制或增大 timeout 阈值，让它跑完 50 epochs。按当前速度估算完整训练需约 26 小时。

---
