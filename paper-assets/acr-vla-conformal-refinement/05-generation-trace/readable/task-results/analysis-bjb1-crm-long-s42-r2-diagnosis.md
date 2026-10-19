# analysis bjb1 crm long s42 r2 diagnosis

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bjb1-crm-long-s42-r2-diagnosis_20260526T121737_result.json`
- **Structured JSON:** [`ca996570cb843058ee01.json`](../../sessions/ca/ca996570cb843058ee01.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both experiments diagnosed and registry updated.

## 诊断结果

**两个实验都已成功完成，cron 误报为 failed（实际是 tmux session 在 eval 自然退出后结束）。**

### pi05-crm-k2-long-s42-r2 ✅ success
- 模式: `crm_obs_only`, K=2, max_correction_norm=0.05
- **Overall success rate: 82.0% (164/200)** on LIBERO-Long s42
- 日志: `/root/acr-vla-conformal-refinement/logs/eval_long_crm_obs_only_norm0.05_seed42_pi05_K2.log`
- JSON: `eval_long_crm_obs_only_norm0.05_seed42_pi05_K2.json`（已写盘）
- 之前被 cron 自动标 failed（"process dead 5× with no sentinel/W&B"），已修正 conclusion=success 并记录原因到 failure_reason 字段

### pi05-adaptive-long-s42-r2 ✅ success
- 模式: `adaptive_conformal_crm`, K=2, τ=0.25, max_correction_norm=0.2
- **Overall success rate: 80.5% (161/200)** on LIBERO-Long s42
- 触发率 trigger_rate=3.9%, mean_uncertainty=0.087
- 日志: `/root/acr-vla-conformal-refinement/logs/eval_long_adaptive_pi05_seed42.log`
- JSON: `eval_long_adaptive_pi05_seed42.json`（已写盘）
- 注册表已从 RUNNING → DONE/success

### 关键观察
- CRM K=2 (82.0%) **微优于** Adaptive (80.5%) on Long s42，触发率仅 3.9%（adaptive 几乎从不修正）
- 两个进程都跑了 ~6000+ 秒（wall_clock），正常退出
- **cron 误报根因**：tmux session 在 Python 进程退出后随之消失，cron 检测 pid 时已没了 → 误判 dead。建议未来 eval 任务写 sentinel 文件标识正常完成

---
