# code plan 008 router size

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan-008-router-size_20260515T131841_result.json`
- **Structured JSON:** [`5b36220f7f6bc4a01ef5.json`](../../sessions/5b/5b36220f7f6bc4a01ef5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常运行中。关键信息：

- **Qwen3-1.7B**: 165 steps/epoch (bs=4, ga=8), ~1.04 it/s, 当前 30/165 (epoch 1)
- 3 epochs × 165 steps = 495 total steps，约 8 分钟/epoch，共 ~25 分钟
- trainable params: 6.4M / 1.7B (0.37%)

估算总训练时间：
- Qwen3-1.7B: ~25 min + eval ~2 min
- Qwen2.5-1.5B: ~20 min + eval ~2 min（参数更少，更快）
- Qwen2.5-3B: ~35 min + eval ~3 min
- **总计约 90 分钟**

训练已在 GPU0 上后台运行，PID 476627。日志路径：
- 主日志：`logs/plan008_training.log`
- 各模型日志：`checkpoints/plan-008-{model}/logs/train.log`

Registry 已更新为 RUNNING (exp_id: `plan-008-router-size`)。

训练完成后 summary 自动保存到 `results/plan-008/summary.json`。

---
