# ops gpu check 10894

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_check_10894_20260524T233631_result.json`
- **Structured JSON:** [`c6cf565d879cd1740c97.json`](../../sessions/c6/c6cf565d879cd1740c97.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 4 张卡的任务确认完毕。汇总：

```
cuda:0 - 运行中 - PID 775953 - 99%  - ablation_occ_detach_s0_retrain（训练，resume from step 20000, max_steps=50005）
cuda:1 - 运行中 - PID 797141 - 53%  - full_occ_ln_s0_eval（evaluate_safelibero.py, 50 rollouts, libero_spatial）
cuda:2 - 运行中 - PID 777222 - 93%  - full_occ_ln_s1（训练，resume from step 20000, max_steps=50005, seed=43）
cuda:3 - 运行中 - PID 777428 - 55%  - full_occ_ln_s2（训练，resume from step 20000, max_steps=50005, seed=44）
```

4 张卡全部在正常工作，与预期一致。没有空闲卡，没有崩溃。

---
