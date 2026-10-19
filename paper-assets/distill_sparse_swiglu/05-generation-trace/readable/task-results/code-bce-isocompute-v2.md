# code bce isocompute v2

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_bce_isocompute_v2_20260515T195750_result.json`
- **Structured JSON:** [`61d652d12a872b33ee1e.json`](../../sessions/61/61d652d12a872b33ee1e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已提交并注册完成。总结：

**bce_isocompute_v2_s42** 已在 westd-34887 cuda:0 上启动（PID 125967）

- 修改了 `train.py`：新增 `--save_every` 参数，在 `train_bce` 循环中每 N 步 + 最终步保存 checkpoint
- 终止了旧的 2700 步实验（PID 123989），释放 cuda:0
- 配置：BCE loss, 1000 步, save_every=250 → 将在 step 250/500/750/1000 各保存一个 checkpoint
- 输出目录：`/root/distill_sparse_swiglu/checkpoints/bce_isocompute_v2_s42/`
- 日志：`~/runs/distill_sparse_swiglu/bce_isocompute_v2_s42.log`
- Registry 状态：RUNNING, plan_id=plan_003

---
