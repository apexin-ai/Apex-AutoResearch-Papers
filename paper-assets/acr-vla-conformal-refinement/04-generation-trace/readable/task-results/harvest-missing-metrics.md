# harvest missing metrics

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_missing-metrics_20260521T032058_result.json`
- **Structured JSON:** [`b0e6843ea92745c755f2.json`](../../sessions/b0/b0e6843ea92745c755f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

25/25 更新全部成功。

## 汇总表

| exp_id | ε | seed | SR | server | JSON 文件 |
|--------|---|------|----|--------|-----------|
| eval-obs-only-object-norm003-seed43 | 0.03 | 43 | 0.14 | bjb2-28827 | eval_obs_only_object_norm003_seed43.json |
| eval-obs-only-object-norm003-seed43-r2 | 0.03 | 43 | 0.14 | bjb1-32546 | eval_object_obs_only_norm003_seed43_r2.json |
| eval-obs-only-object-norm003-seed44 | 0.03 | 44 | 0.15 | bjb1-18228 | eval_obs_only_object_norm003_seed44.json |
| eval-obs-only-object-norm003-seed44-bjb2 | 0.03 | 44 | 0.15 | bjb2-28827 | eval_object_obs_only_norm003_seed44.json |
| eval-obs-only-object-norm003-seed45 | 0.03 | 45 | 0.15 | bjb2-28827 | eval_obs_only_object_norm003_seed45.json |
| eval-obs-only-object-norm003-seed46 | 0.03 | 46 | 0.15 | bjb2-28827 | eval_obs_only_object_norm003_seed46.json |
| eval-obs-only-object-norm003-seed47-r2 | 0.03 | 47 | 0.15 | bjb1-32546 | eval_object_obs_only_norm003_seed47.json |
| eval-obs-only-object-norm003-seed48 | 0.03 | 48 | 0.15 | bjb1-18228 | eval_object_obs_only_norm003_seed48.json |
| eval-obs-only-object-norm005-seed43 | 0.05 | 43 | 0.13 | bjb1-32546 | eval_obs_only_object_norm005_seed43.json |
| eval-obs-only-object-norm005-seed43-r2 | 0.05 | 43 | 0.14 | bjb1-32546 | eval_object_obs_only_norm005_seed43_r2.json |
| eval-obs-only-object-norm005-seed44 | 0.05 | 44 | 0.12 | bjb1-18228 | eval_obs_only_object_norm005_seed44.json |
| eval-obs-only-object-norm005-seed47 | 0.05 | 47 | 0.13 | bjb2-28827 | eval_obs_only_object_norm005_seed47.json |
| eval-obs-only-object-norm005-seed48 | 0.05 | 48 | 0.13 | bjb1-32546 | eval_obs_only_object_norm005_seed48.json |
| eval-obs-only-object-norm005-seed49 | 0.05 | 49 | 0.15 | bjb1-32546 | eval_obs_only_object_norm005_seed49.json |
| eval-obs-only-object-norm005-seed50 | 0.05 | 50 | 0.13 | bjb2-28827 | eval_obs_only_object_norm005_seed50.json |
| eval-obs-only-object-norm005-seed55 | 0.05 | 55 | 0.15 | bjb1-18228 | eval_obs_only_object_norm005_seed55.json |
| eval-obs-only-object-norm01-seed44 | 0.1 | 44 | 0.16 | bjb1-32546 | eval_object_obs_only_norm01_seed44.json |
| eval-obs-only-object-norm01-seed45-r2 | 0.1 | 45 | 0.17 | bjb2-28827 | eval_object_obs_only_norm01_seed45_r2.json |
| eval-obs-only-object-norm01-seed47 | 0.1 | 47 | 0.17 | bjb1-32546 | eval_object_obs_only_norm01_seed47.json |
| eval-obs-only-object-norm01-seed48 | 0.1 | 48 | **0.13** | bjb2-28827 | eval_obs_only_object_norm01_seed48.json |
| eval-obs-only-object-norm01-seed49 | 0.1 | 49 | 0.16 | bjb1-32546 | eval_obs_only_object_norm01_seed49.json |
| eval-obs-only-object-norm01-seed50 | 0.1 | 50 | 0.14 | bjb1-18228 | eval_obs_only_object_norm01_seed50.json |
| eval-obs-only-object-norm01-seed52 | 0.1 | 52 | 0.15 | bjb1-32546 | eval_obs_only_object_norm01_seed52.json |
| eval-obs-only-object-norm01-seed53 | 0.1 | 53 | 0.19 | bjb2-28827 | eval_obs_only_object_norm01_seed53.json |
| eval-obs-only-object-norm01-seed54 | 0.1 | 54 | 0.15 | bjb2-28827 | eval_obs_only_object_norm01_seed54.json |

## 需确认的 2 个 discrepancy

1. **eval-obs-only-object-norm003-seed44-bjb2** — registry notes 记录 "overall SR=17%"，但 `logs/` 下的 JSON 文件读出 0.15。notes 提到实际 JSON 在 `/root/logs/`（非标准路径），可能读到的是不同 run 的文件。

2. **eval-obs-only-object-norm01-seed48** — 旧 metrics 记录 success_rate=0.18（与 bjb1-18228 上的文件 0.18 一致），但 spec.server=bjb2-28827 上的文件只有 0.13。可能是被后续实验覆盖，或 spec.server 不准确。已按 bjb2-28827 上的 JSON 写入 0.13。

如果这两个值需要修正，可以重新 update。

---
