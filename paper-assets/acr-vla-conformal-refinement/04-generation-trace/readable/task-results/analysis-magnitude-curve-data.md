# analysis magnitude curve data

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_magnitude-curve-data_20260516T185620_result.json`
- **Structured JSON:** [`7ef35f762714ad8a5c21.json`](../../sessions/7e/7ef35f762714ad8a5c21.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个产出已完成并注册：

**1. `magnitude_curve_data.json`** — 包含：
- Object benchmark magnitude curve（seed42，6 norm 级别 × obs_only + perdof）
- Spatial benchmark magnitude curve（seed42）
- 所有 baselines（argmin / vla_only / vla_mean）
- `seed_comparison` 区段：obs_only_norm02 (3 seeds), obs_only_norm01 (2 seeds), argmin (3 seeds), perdof_norm01/02 (2 seeds), vla_only (3 seeds), vla_mean (3 seeds)
- 每个数据点含 exp_id 追溯

**2. `pooled_fisher_test_v2.py`** — 修正版脚本：
- 从 JSON 读 `successes`/`total`（不硬编码）
- `--seeds 42 43 44` 指定包含哪些 seeds
- 输出 pooled Fisher p-value（双边 + 单边）
- 用法示例：`python pooled_fisher_test_v2.py --data magnitude_curve_data.json --method1 obs_only_norm02 --method2 argmin --seeds 42 43 44`

seed45/46 完成后只需在 JSON 的 `seed_comparison` 各 method 下追加条目即可直接跑 5-seed pooled test。

---
