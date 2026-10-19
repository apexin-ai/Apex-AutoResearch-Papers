# code fix c1 w3 training pipeline

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-c1-w3-training-pipeline_20260514T074015_result.json`
- **Structured JSON:** [`f0ae2297ae95f5e33ac8.json`](../../sessions/f0/f0ae2297ae95f5e33ac8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 bug 已修复，import 验证通过。

**Fix C1** (`utils.py`):
- `load_libero_demos` 第 80-84 行：`ee_states` 现在拼接 `gripper_states`，从 6D → 8D，与 eval 时 `get_robot_state` 的 8D 一致
- `preprocess_obs_batch` 的 `_normalize_state` 会自动适配 D=8，用 `state_mean[:8]` 归一化

**Fix W3** (`cgs.py`):
- 第 26 行：`alpha` 默认值从 `0.1` 改为 `0.5`
- K=10, alpha=0.5 → `q_idx = ceil(0.5*11)-1 = 5`，取中位数而非最大值

---
