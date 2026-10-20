# deploy 10894 verify and fix

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_10894_verify_and_fix_20260525T174500_result.json`
- **Structured JSON:** [`f5093c1cc5625eda0d92.json`](../../sessions/f5/f5093c1cc5625eda0d92.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**全部 4 个实验正常运行，无冲突。**

| GPU | 实验 | 当前 step | 速度 | 状态 |
|-----|------|-----------|------|------|
| cuda:0 | cutoff_45k_s2_v2 | ~373/50005 | ~1.07 it/s | ✅ 从头训练中 |
| cuda:1 | mvp_occ_s3_v2 | 训练中 | ~1.08 it/s | ✅ resume from 20K |
| cuda:2 | full_occ_ln_s3_v2 | 训练中 | ~1.06 it/s | ✅ resume from 20K |
| cuda:3 | ablation_occ_detach_s3_v2 | ~336/50005 | ~1.06 it/s | ✅ 训练中 |

`full_occ_bn_v2_s1` 冲突 session 已不存在，无需额外操作。所有实验约 6 分钟前启动，进度正常。

---
