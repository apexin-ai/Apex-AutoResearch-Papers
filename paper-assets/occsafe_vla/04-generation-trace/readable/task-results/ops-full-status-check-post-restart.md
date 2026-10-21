# ops full status check post restart

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_full_status_check_post_restart_20260524T111609_result.json`
- **Structured JSON:** [`67e965a9f2d6fcb88052.json`](../../sessions/67/67e965a9f2d6fcb88052.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
[westd-10894]
GPU 0: util 99%, mem 61/96GB — ablation_occ_detach_s0_retrain PID alive, step 7334/50005 (15%)
GPU 1: util 99%, mem 61/96GB — full_occ_ln_s0 PID alive, step 7702/50005 (15%)
GPU 2: util 99%, mem 61/96GB — full_occ_ln_s1 PID alive, step 7698/50005 (15%)
GPU 3: util 99%, mem 62/96GB — full_occ_ln_s2 PID alive, step 7677/50005 (15%)

[westd-34685]
GPU 0: util 0%, mem 16/96GB — cutoff_45k_s0_eval: 运行中 (Task 7/10, 94%)
GPU 1: util 0%, mem 0/96GB — cutoff_15k_s0_eval: ✓ 已完成
GPU 2: util 99%, mem 61/96GB — cutoff_25k_s1 PID alive, step 39423/50005 (79%)
GPU 3: util 99%, mem 61/96GB — reverse_cutoff_s1 PID alive, step 39481/50005 (79%)

[Eval 结果]
- cutoff_15k_s0_eval: TSR=0.912, CAR=0.804 → /root/occsafe_vla/artifacts/safelibero_libero_spatial_20260524_182606.json
- cutoff_45k_s0_eval: 进行中，预计 ~15 分钟完成

[需要行动]
- GPU 1 (westd-34685) 已空闲，可安排新任务
- cutoff_45k_s0_eval 即将完成，完成后 GPU 0 也将空闲
- westd-10894 四个训练均正常，运行 ~2h，ETA ~11h
- cutoff_25k_s1 / reverse_cutoff_s1 运行 ~12.7h，ETA ~2.7h
```

---
