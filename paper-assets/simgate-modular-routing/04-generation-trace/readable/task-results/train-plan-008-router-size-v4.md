# train plan 008 router size v4

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_plan-008-router-size-v4_20260515T194652_result.json`
- **Structured JSON:** [`32fe41ff44580c697291.json`](../../sessions/32/32fe41ff44580c697291.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练确认正常。

**0.6B Loss 曲线（epoch 1）：** 3.14 → 2.08 → 0.96 → 0.63 → 0.51（快速收敛，符合预期）

4B 还没有 loss 输出（进度还在前 37/165 步），稍后再看。

**执行报告：**

| 任务 | GPU | PID | VRAM | 速度 | 状态 |
|------|-----|-----|------|------|------|
| Qwen3-0.6B (seed42→43) | cuda:0 | 893681 | 8.7/32 GB | ~1.02 it/s | Epoch 1 进行中，loss 0.51 |
| Qwen3-4B (seed42→43) | cuda:1 | 893825 | 17.5/32 GB | ~1.10 s/it | Epoch 1 进行中 |

**预计时间：**
- 每个 seed: 165 steps × 3 epochs = 495 steps
- 0.6B: ~495s/seed ≈ 8.3 min/seed → 2 seeds ~17 min
- 4B: ~545s/seed ≈ 9.1 min/seed → 2 seeds ~18 min
- 两个 GPU 约 **18-20 分钟**后全部完成

Registry 已更新为 RUNNING，plan-id 已关联。

---
