# deploy pi05 unified crm 3suite r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_pi05-unified-crm-3suite-r2_20260524T101200_result.json`
- **Structured JSON:** [`19cce78380196454417e.json`](../../sessions/19/19cce78380196454417e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Summary:

1. **训练脚本**: `train_crm.py`（已支持 `--benchmark object spatial goal` 多 suite 统一训练）
2. **数据集**: 194,485 samples（Object 72,507 + Spatial 60,250 + Goal 61,728），obs_dim=2048
3. **训练状态**: 已成功启动 ✅
   - PID: 319672，GPU 0（558 MiB）
   - 当前进度: epoch 1, batch ~850/5470
   - Loss: ~0.01–0.03 范围，正常下降中
   - CRM 参数量: 615,966
4. **Best checkpoint**: `crm_best.pt`，保存在 `/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt`
5. **预计训练时长**: 5,470 batches/epoch × 50 epochs = 273,500 batches，以当前速度（~80 batches/min）估算约 **55–60 小时**

---
