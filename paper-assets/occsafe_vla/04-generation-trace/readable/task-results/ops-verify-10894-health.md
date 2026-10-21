# ops verify 10894 health

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-10894-health_20260526T035723_result.json`
- **Structured JSON:** [`4b17ed50fdf885cd89f3.json`](../../sessions/4b/4b17ed50fdf885cd89f3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已保存。汇总：

**磁盘**: 从满盘恢复到 87% (35G 可用)，但存在瞬时满盘风险（4 个实验同时写 checkpoint 时需 60G 临时空间）。

**4 个实验全部正常运行**:
- cutoff_45k_s2_v2: 73% (step 36345), ETA ~14:00 UTC
- mvp_occ_s3_v2: 50% (step 25152), ETA ~16:40 UTC
- full_occ_ln_s3_v2: 50% (step 25061), ETA ~16:50 UTC
- ablation_occ_detach_s3_v2: 50% (step 25000), ETA ~16:50 UTC

**建议清理** full_occ_ln_s1 + full_occ_ln_s2 (各 15G，共 30G)，无任何 RUNNING/PREPARING 依赖，清理后可用空间达 65G，消除磁盘风险。如需更大缓冲可再清 vanilla_retrain_s0 + ablation_occ_detach_s0_retrain (+30G)。

---
