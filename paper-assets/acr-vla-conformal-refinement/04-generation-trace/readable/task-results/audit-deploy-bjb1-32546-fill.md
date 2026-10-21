# audit deploy bjb1 32546 fill

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit-deploy_bjb1-32546-fill_20260520T152929_result.json`
- **Structured JSON:** [`8064c9236c36b2cad967.json`](../../sessions/80/8064c9236c36b2cad967.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。bjb1-32546 现在 6/6 GPU 全满：

| GPU | 实验 | 状态 |
|-----|------|------|
| 0 | eval-random-selection-spatial-seed44 | RUNNING (新部署) |
| 1 | eval-k5-obs-only-object-seed43 | RUNNING (新部署) |
| 2 | eval-perdof-object-norm02-seed49 | RUNNING (已有) |
| 3 | eval-k20-obs-only-object-seed43 | RUNNING (新部署) |
| 4 | eval-obs-only-object-norm005-seed43 | RUNNING (新部署) |
| 5 | eval-random-selection-object-seed45 | RUNNING (已有) |

第 5 个实验 (eval-obs-only-object-norm003-seed43) 没有空闲 GPU，未部署。最近完成的 JSON 文件已在 registry 中正确标记为 DONE。

---
