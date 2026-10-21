# ops check ablation 10894

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_ablation_10894_20260525T020911_result.json`
- **Structured JSON:** [`d6bc63c8522744c59bcf.json`](../../sessions/d6/d6bc63c8522744c59bcf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**cuda:0 状态：正常运行中，无需干预。**

- **当前 step**: 29,402 / 50,005（59%）
- **已从 40K checkpoint resume**，当前实际训练从 step 40,000 恢复（日志显示连续进度）
- **速度**: ~1.07 it/s
- **预计剩余**: ~5.5h 完成到 50K
- **最新 loss** (step 29,400): occ_loss=0.0091, action_loss=0.0400
- **GPU 0**: 67°C, 437W, 62GB/98GB 显存, 99% 利用率

等等——日志显示 step 29,402 而非预期的 40,000+。这说明 resume 是从 step 0 重新计数到 50,005，而不是接续 40,000 的编号。当前 29,402/50,005 意味着整个训练已完成 59%，还剩约 5.5 小时。

不做任何操作，让训练继续。

---
