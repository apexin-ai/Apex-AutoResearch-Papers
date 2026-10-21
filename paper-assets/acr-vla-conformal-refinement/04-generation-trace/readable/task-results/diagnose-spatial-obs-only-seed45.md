# diagnose spatial obs only seed45

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_spatial-obs-only-seed45_20260521T114948_result.json`
- **Structured JSON:** [`243a50c5bbebc16bafc4.json`](../../sessions/24/243a50c5bbebc16bafc4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已修正。总结：

- **状态**：实验正常完成，cron 误判（eval 脚本不写 sentinel/W&B，进程退出后 cron 无法确认）
- **结果**：LIBERO-Spatial crm_obs_only seed45, **SR = 34.0%** (34/100)
- **Per-task**：between_plate_ramekin 90%, next_to_ramekin 90%, next_to_cookie_box 80%, on_cookie_box 40%, next_to_plate 30%, in_top_drawer 10%, table_center/on_ramekin/on_stove/on_wooden_cabinet 均 0%
- **Registry**：conclusion 从 "failed" 修正为 "success"，metrics/log_path/checkpoint_path 此前已正确设置

---
