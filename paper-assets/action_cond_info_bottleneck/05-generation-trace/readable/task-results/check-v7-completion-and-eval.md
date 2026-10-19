# check v7 completion and eval

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_v7-completion-and-eval_20260516T135851_result.json`
- **Structured JSON:** [`cab0b7e7e08297840ed4.json`](../../sessions/ca/cab0b7e7e08297840ed4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 seed 都在训练中，未完成。

**Seed1** (PID 21363, GPU 0)
- 当前 step: **7600/20000**
- 速度: ~1.7 steps/s
- 已有 checkpoint: checkpoint-5000
- 剩余: 12400 steps → **ETA ~2h01m**

**Seed2** (PID 27427, GPU 0)
- 当前 step: **1300/20000**
- 速度: ~1.5 steps/s
- 无 checkpoint
- 剩余: 18700 steps → **ETA ~3h28m**

训练指标看起来正常：seed1 的 loss 稳定在 0.15-0.26 区间，scorer_mean ~0.28-0.33；seed2 loss 在持续下降（0.76→0.37），处于早期收敛阶段。

注意：两个 seed 都指定了 `--gpu 0`，但 seed2 也在 GPU 0 上跑——如果服务器只有一块 GPU 这是正常的，如果有多卡可能需要确认是否有意共享。

---
