# check multiscale train status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_multiscale-train-status_20260517T182355_result.json`
- **Structured JSON:** [`3bdbca11e87c3ee12596.json`](../../sessions/3b/3bdbca11e87c3ee12596.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
进程状态: dead (训练已完成)
当前 epoch: 50/50 ✓ 完成
最终 train_loss: 0.024104
最终 val_loss: 0.007199 (best)
  - l2: 0.0068
  - dir: 0.0787
  - tri: 0.0010
  - mag: 0.0013
Checkpoint 路径: /root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt (1.3M)
```

训练正常收敛完成，val_loss 从 epoch 44 到 50 持续小幅下降（0.007204 → 0.007199），最后几个 epoch lr 接近 0 说明 cosine schedule 已走完。GPU 已释放，无进程占用。

---
