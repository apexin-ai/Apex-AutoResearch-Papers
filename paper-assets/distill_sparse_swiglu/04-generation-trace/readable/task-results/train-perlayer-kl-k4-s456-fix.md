# train perlayer kl k4 s456 fix

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_perlayer_kl_k4_s456_fix_20260522T133926_result.json`
- **Structured JSON:** [`bec26489c54147b028b0.json`](../../sessions/be/bec26489c54147b028b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**无需修复，训练已经在正常运行。**

两个 pipeline 都已经由 `submit_training_job` 正确启动，进程已被 reparent 到 init (PPID=1)，不会因 SSH 断连而死：

| 实验 | GPU | PID | 进度 | 速度 |
|------|-----|-----|------|------|
| s123 | cuda:0 | 59565→59575 | Step 1/2700 | ~2.3s/step |
| s456 | cuda:1 | 59879→59889 | Step 1/2700 | ~2.3s/step |

关键事实：
- `WANDB_MODE=disabled` 已生效，wandb 问题已修复
- 日志重定向到 `~/runs/distill_sparse_swiglu/perlayer_kl_k4_s{123,456}.log`
- 6 小时 timeout 保护
- `save_every=500`，首个 checkpoint 约 19 分钟后产生
- Phase 1 训练预计 ~1.7 小时完成（2700 steps × 2.3s）

不需要任何操作，等训练跑完即可。

---
