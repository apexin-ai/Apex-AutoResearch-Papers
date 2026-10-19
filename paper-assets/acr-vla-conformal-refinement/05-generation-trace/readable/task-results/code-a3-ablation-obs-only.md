# code a3 ablation obs only

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_a3-ablation-obs-only_20260513T225233_result.json`
- **Structured JSON:** [`2cb8d7eab9ed917820cc.json`](../../sessions/2c/2cb8d7eab9ed917820cc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Epoch 1 完成，train_loss=0.059092, val_loss=0.018489。训练正常运行，没有任何维度错误。

总结：

**已完成的修改：**
1. **`src/crm.py`** — `forward()` 支持 `uncertainty_features=None`，此时只拼接 `mean_action + obs_features`
2. **`src/train_crm.py`** — 新增 `--input_mode` 参数（full/obs_only/scalar_unc），CRM 实例化时根据 mode 设置 `uncertainty_dim`（0 for obs_only），3 处 forward 调用处条件传 `None`

**训练状态：**
- 实验 `crm-train-a3-obs-only` 已注册并 RUNNING
- bjb1-18228 cuda:3，PID 104611
- Epoch 1/50 已完成：val_loss=0.018489
- 每 epoch 约 3-4 分钟（CGS CPU 计算密集），预计 ~15-20 分钟内完成全部 50 epochs
- 日志：`/root/autodl-tmp/checkpoints/crm/obs_only/train.log`

---
