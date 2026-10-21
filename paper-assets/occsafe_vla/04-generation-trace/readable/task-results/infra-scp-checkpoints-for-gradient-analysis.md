# infra scp checkpoints for gradient analysis

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_scp-checkpoints-for-gradient-analysis_20260527T042509_result.json`
- **Structured JSON:** [`49c22c0435789e547baa.json`](../../sessions/49/49c22c0435789e547baa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

5 个 50K checkpoint 全部就绪于 westd-10894，各 15GB：

| 条件 | 目录 | 大小 |
|------|------|------|
| Full OCC BN | `mvp_occ_s3_v2` | 15G |
| Full OCC LN | `full_occ_ln_s3_v2` | 15G |
| Detach BN | `ablation_occ_detach_s3_v2` | 15G |
| Vanilla | `vanilla_v2_s1` | 15G |
| Detach LN | `detach_ln_s3` | 15G |

梯度分析脚本 `run_gradient_analysis_5cond.sh` 可以直接运行。

---
