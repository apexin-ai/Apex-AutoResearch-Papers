# diagnosis gpu conflict check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_gpu-conflict-check_20260519T133705_result.json`
- **Structured JSON:** [`ae0b5d53862ac4656a7b.json`](../../sessions/ae/ae0b5d53862ac4656a7b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已更新 `eval-perdof-object-norm01-seed43` 从 ANALYZING → DONE (sr=12%)。

---

## 总结

| 服务器 | GPU | 冲突 | 严重性 | 建议 |
|--------|-----|------|--------|------|
| bjb2-40593 | cuda:0 | random_selection_seed46 + spatial_norm02_seed43 | 中等（速度减半，无OOM风险） | 可接受共存，或 kill random_selection 优先跑 spatial 三连 |
| bjb1-32546 | cuda:4 | perdof_norm005_seed45 + obs_only_default_seed48 | 低（都快完了） | 等完成即可，预计 1-2 小时内结束 |

**已执行的修复：** `eval-perdof-object-norm01-seed43` ANALYZING → DONE

**待你决定：** bjb2-40593 上是否 kill random_selection_seed46 来让 spatial 系列（3个seed串行）加速？

---
