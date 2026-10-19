# check seed4 seed8 status and westd gpu

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_seed4_seed8_status_and_westd_gpu_20260521T161256_result.json`
- **Structured JSON:** [`e1c3805ab65c0dacd063.json`](../../sessions/e1/e1c3805ab65c0dacd063.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
Seed 4 (bjb1): ✅ 完成  step 15/15, EXIT_CODE=0
  - train_success=38.28% (step 13), response_length=10625 (mean)
  - val: pass@1=43.75%, pass@8=98.8%, response_length=4459
  - checkpoint: /root/autodl-tmp/checkpoints/exp029-seed4/global_step_15/actor/ (21GB)

Seed 8 (westd): 🔄 进行中  step 0/15 (首轮 rollout 中)
  - PID 462991 alive, elapsed=20min, 正在 compute_policy_loss
  - GPU 2,3: 91.6/97.9 GB, 100% util
  - 尚无 step 指标，刚启动属正常

westd GPU 0,1: ✅ 已释放  (0 MiB, 0% util, 无计算进程)
```

---
