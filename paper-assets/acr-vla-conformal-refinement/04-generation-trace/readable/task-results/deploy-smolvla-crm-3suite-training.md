# deploy smolvla crm 3suite training

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_smolvla-crm-3suite-training_20260522T165259_result.json`
- **Structured JSON:** [`9575b73e5fbe1bf50bd1.json`](../../sessions/95/9575b73e5fbe1bf50bd1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常进行，loss 在下降：

| Batch | Loss |
|-------|------|
| 50/2190 | 0.0218 |
| 100/2190 | 0.0234 |
| 150/2190 | 0.0199 |

**训练启动总结：**
- **PID**: 344454 (bash) → 344463 (python)
- **tmux session**: `train-crm-smolvla-3suite-v1`
- **GPU**: cuda:0 @ bjb2-28827
- **日志**: `~/runs/acr-vla-conformal-refinement/train-crm-smolvla-3suite-v1.log`
- **数据**: 77,835 样本 (object:28,950 + spatial:24,133 + goal:24,752), K=10, obs_dim=960
- **模型**: CRM 327,198 参数, obs_only 模式
- **初始 loss**: ~0.020 (MSE)
- **每 epoch**: 2190 batches (bs=32)，每 epoch ~15-20 min（CGS 密集）
- **预计总时间**: ~15-20h (50 epochs)

---
