# diagnose gpu audit 34685

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_gpu_audit_34685_20260527T174051_result.json`
- **Structured JSON:** [`1844013ca10b7f4b15f6.json`](../../sessions/18/1844013ca10b7f4b15f6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

westd-34685 **全部 4 张 GPU 正常运行**，无 crash。

### 状态汇总

| GPU | 实验 | 进度 | 速度 | 状态 |
|-----|------|------|------|------|
| cuda:0 | detach_ln_v2_s2 | 8588/50005 (17%) | ~1.08 it/s | 正常 |
| cuda:1 | vanilla_object_s0 | 3409/50005 (7%) | ~1.10 it/s | 正常 |
| cuda:2 | full_occ_ln_v2_s3 | 3825/50005 (8%) | ~1.09 it/s | 正常 |
| cuda:3 | detach_ln_v2_s3 | 3819/50005 (8%) | ~1.08 it/s | 正常 |

所有 GPU 利用率 99%，显存 ~62GB/98GB。System 的 "3/8 活跃" 报告是误报——4/4 全满。

---
