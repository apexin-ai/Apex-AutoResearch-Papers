# diagnose crm train v3 norm result

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_crm-train-v3-norm-result_20260514T200316_result.json`
- **Structured JSON:** [`50fe6cf37f2177289a16.json`](../../sessions/50/50fe6cf37f2177289a16.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。结果汇总：

**crm-train-v3-norm: SUCCESS**

| 指标 | 值 |
|------|-----|
| 总 epochs | 50/50 完成 |
| best_epoch | 47 |
| best_val_loss | 0.03578 |
| final_train_loss | 0.04992 |
| final_val_loss | 0.03578 |
| checkpoint | `/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt` |

从 epoch 1 的 val_loss=0.0726 降到 0.0358，降幅 50.7%。最后几个 epoch 收敛稳定（epoch 46-50 的 val_loss 在 0.03578-0.03583 间波动），best 出现在 epoch 47。归一化参数（input_mean/input_std）已嵌入 `crm_best.pt`。

---
