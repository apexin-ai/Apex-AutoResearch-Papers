# code prepare pi05 crm eval scripts

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare-pi05-crm-eval-scripts_20260522T195202_result.json`
- **Structured JSON:** [`384de8ed638ef80db44d.json`](../../sessions/38/384de8ed638ef80db44d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已写入 `artifacts/deploy_pi05_crm_eval.sh`。

**汇总：**

| 项 | 值 |
|---|---|
| 总 evals | 36 (3 modes × 4 suites × 3 seeds) |
| Sessions | 11 (5 on bjb1 + 6 on bjb2) |
| 每 GPU | 链式 3 evals (crm_obs_only → adaptive_conformal_crm → vla_only) |
| 瓶颈 | bjb2 cuda:5 跑 6 evals (goal/43 + goal/44 各 3 modes) |
| Long suite | 全在 bjb1 (cuda:0,1,2)，避开 bjb2 超时限制 |

**需注意的问题：**

`crm_unified_4suite_r4` 训练日志确认使用 **SmolVLA features (obs_dim=960)**，但 π0.5 产生 **2048D features**。当前 `evaluate.py` 在 `--model pi05 --obs_dim 960` + CRM 时会 raise `ValueError`（第 605-613 行）。

部署前需要解决：
- **方案 A**：用 π0.5 caches 重训 CRM（obs_dim=2048）
- **方案 B**：在 evaluate.py 加 2048→960 projection
- **方案 C**：修改 pi05 obs_dim check 逻辑

脚本中 `OBS_DIM=960` 按你的指定设置，改 checkpoint 或 obs_dim 只需修改顶部变量。

---
