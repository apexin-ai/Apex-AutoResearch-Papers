# monitor exp028c metrics

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_exp028c_metrics_20260516T033540_result.json`
- **Structured JSON:** [`33b0866492c5f0d356d2.json`](../../sessions/33/33b0866492c5f0d356d2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/exp028c_selfguide_recipe/report/exp028c_full_metrics.md`。

关键发现：

- **PID 824675 在运行**，当前 step 7 rollout 中，预计 ~11:36 完成
- **完成 6/100 步**，预计总完成时间 May 19 ~15:00
- **action_is_valid 稳步提升**：76% → 90%（train），74% → 97%（val）
- **train success 波动大**：6.25%-18.75%，均值 ~12.4%
- **val success 停滞 6.25%**，step 0 到 step 5 无变化
- **kl_loss step 5 飙升到 0.824**（正常 0.01-0.17），step 6 回落到 0.098
- **pass@8 从 step 3 的 68.75% 下降到 step 6 的 31.25%**
- 无 OOM、crash、NaN

**MVP 预判**：当前 val success 6.25%，离 20% 阈值差距很大。模型在学会合法动作（action_is_valid 提升明显），但未转化为任务完成率。

---
