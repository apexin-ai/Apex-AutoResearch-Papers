# ssh 10894 emergency disk clean

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_10894_emergency_disk_clean_20260526T040108_result.json`
- **Structured JSON:** [`d5c8f531d77e316da9de.json`](../../sessions/d5/d5c8f531d77e316da9de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
清理前: 87% (35G free)
清理后: 63% (95G free)
删除: full_occ_ln_s1 (15G) + full_occ_ln_s2 (15G) + vanilla_retrain_s0 (15G) + ablation_occ_detach_s0_retrain (15G) = 60G
训练进程: 4/4 存活 (cutoff_45k_s2_v2, full_occ_ln_s3_v2, ablation_occ_detach_s3_v2, mvp_occ_s3_v2)
```

30K checkpoint 写入空间充足（需 ~60G，可用 95G）。

---
