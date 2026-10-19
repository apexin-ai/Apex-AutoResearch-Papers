# ops server check v2

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_server-check-v2_20260516T053608_result.json`
- **Structured JSON:** [`7e21115412bdeddfdaba.json`](../../sessions/7e/7e21115412bdeddfdaba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Server Status
- **cuda:0**: bench_dense running (PID 209887, child PID 209892, 44105/97887 MiB used, GPU util 100%, elapsed 12m23s)
- **cuda:1**: IDLE (0 MiB used, 0% util)

## bce_v3 Status
- **Log found**: yes, `/root/distill_sparse_swiglu/logs/bce_isocompute_v3_s42.log`
- **Last step reached**: 2700/2700
- **Completed**: YES — cron 误判，训练正常完成
- **Final metrics** (step 2700):
  - loss = 0.6382
  - bce = 0.6371
  - reg = 0.0010
  - sparsity = 0.510
- **Checkpoint exists**: yes, `/root/distill_sparse_swiglu/checkpoints/bce_isocompute_v3_s42/predictor_bce.pt` (145 MB)
- **Evaluation done**: NO — 日志在 "Saved checkpoint" 后结束，没有 evaluation 阶段输出

**总结**: bce_isocompute_v3_s42 训练 2700 steps 全部完成（耗时 2828s，1.05s/step），sparsity 收敛到 ~51%。但没有跑 downstream evaluation。bench_dense 正在 cuda:0 上跑 benchmark eval，cuda:1 空闲可用。

---
