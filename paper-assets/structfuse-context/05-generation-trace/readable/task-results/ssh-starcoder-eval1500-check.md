# ssh starcoder eval1500 check

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_starcoder_eval1500_check_20260514T053507_result.json`
- **Structured JSON:** [`8f4b99b16719a2a0dba1.json`](../../sessions/8f/8f4b99b16719a2a0dba1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

eval@1500 已出，且 **eval@2000 马上要来了**（当前 step 2000）。

## StarCoder random_s42 eval 进度

| step | val_loss | R@1 | R@5 | 趋势 |
|------|----------|-----|-----|------|
| 500 | 0.6194 | 0.4352 | 0.9054 | baseline |
| 1000 | **0.6134** | **0.4537** | 0.9201 | best |
| 1500 | 0.6528 | 0.4490 | 0.9057 | 下降 |

**结论：StarCoder 也过拟合了。**

- eval@1500 val_loss 从 0.6134 升到 0.6528（+6.4%），R@1 从 0.4537 降到 0.4490（-1.0%），R@5 从 0.9201 降到 0.9057
- best 仍在 eval@1000：val_loss=0.6134, R@1=0.4537
- 进入 epoch 2 后 val_loss 明显反弹，early_stopping 计数器已触发（"val_loss not improved (1/0)"）
- 当前 step 2000，eval@2000 即将出。如果继续恶化，patience=3 的话还有 2 次机会

训练 loss 在持续下降（step 1950 loss=0.0509），但 val_loss 反升，典型的过拟合模式，和 Qwen 一致。

---
