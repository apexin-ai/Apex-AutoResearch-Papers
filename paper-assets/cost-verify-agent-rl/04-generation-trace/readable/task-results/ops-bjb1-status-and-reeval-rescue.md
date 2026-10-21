# ops bjb1 status and reeval rescue

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_bjb1-status-and-reeval-rescue_20260518T040040_result.json`
- **Structured JSON:** [`8905d5785c8c7a43dca1.json`](../../sessions/89/8905d5785c8c7a43dca1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

### 执行结果

**1. exp029 reeval (OOD 134 tasks) — 已完成**
| Metric | Value |
|--------|-------|
| success / pass@1 | **23.88%** |
| action_is_valid | 56.83% |
| action_is_effective | 91.6% |
| manager_invalid_action | 8.39% |
| reward/mean@134 | 2.388 |
| best@8 | 8.88 |

**2. hsweep_h2_seed2 reeval — 已启动**
- tmux: `reeval_hsweep_h2_seed2`，模型已从 `hsweep-h2/global_step_15` 加载成功
- 日志: `/root/runs/cost-verify-agent-rl/hsweep-h2-seed2-reeval-ood.log`
- 预计 ~40-60 min 完成 validation

**3. seed1 checkpoint — 全部丢失**
- `global_step_5`: 不存在
- `global_step_10`: 存在但属于 **seed2**（May 18 06:47）
- `global_step_15`: 存在但属于 **seed2**（May 18 10:47）
- seed2 写入同一目录覆盖了 seed1，不可恢复

**4. 已执行操作**
- Kill 了 exp029 reeval 的无用训练步（validation 已完成，`total_training_steps: 1` 的训练步在浪费 GPU）
- 创建了 `_alfworld_hsweep_h2_seed2_reeval_ood.yaml` 并启动 reeval
- 状态报告已写入 memory.md

---
