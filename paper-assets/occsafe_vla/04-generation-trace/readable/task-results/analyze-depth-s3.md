# analyze depth s3

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_depth_s3_20260522T215816_result.json`
- **Structured JSON:** [`ef7efbcc35b164ba0ad4.json`](../../sessions/ef/ef7efbcc35b164ba0ad4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完毕。depth_s3 分析结果：

| 指标 | depth_s3 (seed 45) | depth_s2 (seed 44) |
|------|-------|-------|
| final_depth_loss | 0.0628 | 0.0468 |
| final_action_loss | 0.0698 | 0.0498 |
| init_depth_loss | 0.6877 | — |
| init_action_loss | 0.5938 | — |
| training_hours | 14.84 | 14.8 |
| checkpoint_step | 50000 | 50000 |
| checkpoint_size | 15GB | — |

训练正常完成，无NaN/异常。depth_s3 的 final loss 比 depth_s2 高（depth +34%, action +40%），种子间有一定方差，后续eval会更直接反映性能差异。

---
