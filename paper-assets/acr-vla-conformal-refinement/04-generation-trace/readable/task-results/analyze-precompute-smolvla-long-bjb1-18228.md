# analyze precompute smolvla long bjb1 18228

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_precompute-smolvla-long-bjb1-18228_20260522T085455_result.json`
- **Structured JSON:** [`3d805d4eb75d148d8b6f.json`](../../sessions/3d/3d805d4eb75d148d8b6f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Precompute 任务 **成功完成**，已标记 DONE(success)。

**结果摘要：**

| 指标 | 值 |
|------|-----|
| n_samples | 136,090 |
| obs_features | [136090, 960] float32 (499MB) |
| k_samples | [136090, 10, 5, 6] float32 (156MB) |
| expert_actions | [136090, 5, 6] float32 (16MB) |
| K | 10 |
| obs_dim | 960 |
| action_dim | 6 |
| h_eff | 5 |
| 总耗时 | 8021s (~2.2h), 0.06s/sample |
| cache 路径 | `/root/autodl-tmp/crm_cache_v5/long/` |

与 Goal precompute (61728 samples) 结构一致，obs_dim/K/action_dim/h_eff 参数匹配。4-suite cache 现已完成 spatial、object、goal、long 四个 benchmark。

---
