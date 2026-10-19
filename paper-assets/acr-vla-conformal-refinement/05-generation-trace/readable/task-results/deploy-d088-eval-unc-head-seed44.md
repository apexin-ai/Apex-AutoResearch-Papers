# deploy d088 eval unc head seed44

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_d088-eval-unc-head-seed44_20260520T165125_result.json`
- **Structured JSON:** [`1f7059db85c7b874cca3.json`](../../sessions/1f/1f7059db85c7b874cca3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。汇总：

**eval-adaptive-unc-head-object-seed44** 已在 bjb2-28827 cuda:5 启动 (PID 728278)
- Mode: `adaptive_unc_head` (新增模式，已 patch 到 evaluate.py)
- UncertaintyHead: 15,665 params, τ=0.42 (F1=0.767)
- CRM: obs_only, 327,198 params, max_correction_norm=0.2
- K=1, 10 tasks × 10 rollouts = 100 episodes
- Registry: RUNNING

**seed42 (PID 401372) 和 seed43 (PID 401666) 状态**：两个进程均已终止，cuda:0 和 cuda:1 空闲。但 logs 目录中没有 `adaptive-unc-head` 相关的日志文件——这两个 PID 可能是其他实验（最近的日志是 `eval-obs-only-spatial-norm02-seed42-r2.log` 和 `eval-crm-k1-object-seed43-plan702.log`）。

---
