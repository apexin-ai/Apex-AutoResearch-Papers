# ssh fix connector only lr

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix-connector-only-lr_20260517T151824_result.json`
- **Structured JSON:** [`8a4a80d2076c5e3bf509.json`](../../sessions/8a/8a4a80d2076c5e3bf509.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本的 lr 都已经是 `5e-5`，完全一致。训练日志也确认 v7.2 实际使用的就是这个值。

**结果：**
- v7.2 (`run_v7.2_connector_scorer.sh`) lr = `5e-5`
- connector-only (`run_connector_only.sh`) lr = `5e-5`

两者 lr 已经相同，无需修改。其他关键参数对比也一致：steps=20000, batch_size=64, warmup_steps=1000, grad_clip=1.0。区别仅在预期的消融变量上：`freeze_mode` (connector_scorer vs connector_only)、`lambda_contrastive` (0.1 vs 0.0)、`diversity_lambda` (0.1 vs 0.0)、`lambda_drift` (0.1 vs 0.0)。

这是一个公平的消融对比，不需要任何修改。

---
