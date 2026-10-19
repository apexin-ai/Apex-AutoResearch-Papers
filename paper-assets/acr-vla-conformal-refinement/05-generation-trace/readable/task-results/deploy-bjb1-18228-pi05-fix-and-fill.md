# deploy bjb1 18228 pi05 fix and fill

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb1-18228-pi05-fix-and-fill_20260525T072537_result.json`
- **Structured JSON:** [`f76a02a6a75fc64ccf40.json`](../../sessions/f7/f76a02a6a75fc64ccf40.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 jobs running on bjb1-18228:

**修复 Adaptive Spatial s42 crash (cuda:0, PID 484286)**
- 根因: CRM checkpoint 由 `unified_obs_dim=2088` 训练而成（PI05 2048D 特征 zero-pad +40），但默认 `obs_dim=960`，导致 `input_mean` 形状不匹配 (2118 vs 990)
- 修复: `--obs_dim 2048 --unified_obs_dim 2088`，crm.input_dim = `H_EFF*CORRECTION_DIM + 0 + 2088 = 30 + 2088 = 2118` ✓
- 日志已确认: `[eval] CRM loaded from ... (615,966 params)` + `PI05 features (2048D) passed directly to CRM (no projection)`，已进入 rollout，GPU 14.6 GB / 59% util

**VLA-only Object s42 (cuda:1, PID 484670)** — GPU 14.1 GB
**VLA-only Spatial s43 (cuda:2, PID 485043)** — GPU 14.6 GB

| GPU | mem | util | job |
|---|---|---|---|
| 0 | 14663 MiB | 20% | adaptive-spatial-s42-r2 |
| 1 | 14060 MiB | 7% | vla-only-object-s42 |
| 2 | 14663 MiB | 16% | vla-only-spatial-s43 |
| 3 | 9883 MiB | 24% | (其他) |

**注意**: registry 显示 `eval-pi05-vla-only-object-s42` 和 `eval-pi05-vla-only-spatial-s43` 已于 2026-05-25 00:37 在 bjb1-32546 完成（success rates 0.965 / 0.96），output_file 路径同名将被覆盖。已用 `-r2` 后缀注册新 exp_id 保留历史。

---
