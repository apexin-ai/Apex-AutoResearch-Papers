# train acis stage1 k07 k03

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_acis_stage1_k07_k03_20260517T071117_result.json`
- **Structured JSON:** [`9d29f72e2258e3994b9f.json`](../../sessions/9d/9d29f72e2258e3994b9f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。两个 ACIS Stage1-only 训练已成功启动：

| 实验 | GPU | k_ratio | 状态 | sps |
|------|-----|---------|------|-----|
| `train_acis_stage1only_k07` | cuda:2 | 0.7 | RUNNING, step 50/10000 | ~3.7 |
| `train_acis_stage1only_k03` | cuda:3 | 0.3 | RUNNING, step 50/10000 | ~3.3 |

关键确认：
- Expert 冻结 (0 trainable)，只训 ACIS (3.46M params)
- `stage2_steps: 0` → Stage2 被跳过
- baseline checkpoint: Full FT 100K step
- 预计 ~45min 完成（按 3.5 sps 估算，比预期 2h 快）

---
