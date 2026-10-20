# analyze cls seed0

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_cls-seed0_20260512T123026_result.json`
- **Structured JSON:** [`b2ba766200d57875ff19.json`](../../sessions/b2/b2ba766200d57875ff19.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

cls-seed0 已完成，registry 已更新为 DONE。

**结果汇总：**

| Metric | Value |
|--------|-------|
| accuracy | 87.94% |
| fail_f1 / pass_f1 | 88.08 / 87.79 |
| fail_precision / recall | 84.2% / 92.3% |
| pass_precision / recall | 92.1% / 83.8% |
| train_loss / eval_loss | 0.2347 / 0.0963 |
| train_runtime | 4977s (~83min) |
| unparseable | 0 |

**5-seed cls 对比：**

| Seed | Accuracy |
|------|----------|
| 0 | 87.94 |
| 42 | 87.83 |
| 123 | 89.52 |
| 456 | 87.88 |
| 789 | 89.00 |
| **mean ± std** | **88.43 ± 0.78** |

**Cls vs Traj：** cls 88.43±0.78 vs traj 86.30±0.97，cls 高 +2.13pp 且方差更小。5-paired comparison 全部完成。

---
