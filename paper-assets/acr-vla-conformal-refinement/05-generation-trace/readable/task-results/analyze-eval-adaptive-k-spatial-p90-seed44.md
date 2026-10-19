# analyze eval adaptive k spatial p90 seed44

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-adaptive-k-spatial-p90-seed44_20260520T145720_result.json`
- **Structured JSON:** [`43c455caedc989319f32.json`](../../sessions/43/43c455caedc989319f32.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。结果摘要：

| 指标 | 值 |
|------|-----|
| **Overall SR** | **36.0%** (36/100) |
| **avg_K** | 3.56 |
| **fast_path_ratio** | 80.5% |
| **adaptive_trigger_rate** | 19.5% |
| **mean_l2_distance** | 0.090 |
| **threshold (τ=P90)** | 0.12587 |

Per-task 分布：next_to_ramekin 100%, next_to_cookie_box 90%, between_plate_and_ramekin 80% 领先；from_table_center / on_ramekin / on_stove / on_wooden_cabinet 均 0%。

对比 Object P90 参考（SR ~13.3%, avg_K ~2.6, fast_path ~93%），Spatial P90 seed44 的 SR 显著更高（36% vs 13.3%），但 avg_K 也更高（3.56 vs 2.6），fast_path 更低（80.5% vs 93%），说明 Spatial 任务触发更多 full refinement。

---
