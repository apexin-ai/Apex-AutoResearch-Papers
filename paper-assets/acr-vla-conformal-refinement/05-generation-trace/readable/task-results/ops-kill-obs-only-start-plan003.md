# ops kill obs only start plan003

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-obs-only-start-plan003_20260513T234236_result.json`
- **Structured JSON:** [`85639524250b8ad099dd.json`](../../sessions/85/85639524250b8ad099dd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已启动，确认正常运行。

**汇总：**

| 项目 | 详情 |
|------|------|
| **crm-train-a3-obs-only 最终状态** | Epoch 16/50, best val_loss=0.018312 (Epoch 4), plateau 12 epochs |
| **obs_only checkpoints** | `crm_best.pt` + epoch 12-16, 目录 `/root/autodl-tmp/checkpoints/crm/obs_only/` |
| **已终止进程** | PID 104611 (原始), PID 117206 (重复) |
| **plan_003 scalar_unc** | PID **117487**, tmux session `crm-train-scalar-unc`, cuda:3 (561 MiB), input_mode=scalar_unc |
| **数据加载** | 26737 samples (spatial 12167 + object 14570), CRM params: 327,966 |

---
