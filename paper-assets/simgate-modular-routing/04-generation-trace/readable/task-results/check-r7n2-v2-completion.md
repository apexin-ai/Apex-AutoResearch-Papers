# check r7n2 v2 completion

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_r7n2-v2-completion_20260516T033508_result.json`
- **Structured JSON:** [`0401c96b3573d871c591.json`](../../sessions/04/0401c96b3573d871c591.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## r7n2-data-size-ablation-v2 结果

**状态**: KILLED (SIGHUP, EXIT_CODE=129)

**结果文件**: 无。results/ablation_data_size/ 为空，无 checkpoint。

### 运行时间线

| 阶段 | Scale | Seeds | 状态 |
|------|-------|-------|------|
| 第一次启动 | 25pct/seed42 | 1 | wandb login error → EXIT_CODE=1 |
| 第二次启动 | 25pct | 42, 43, 44 | 训练完成 |
| | 50pct | 42, 43, 44 | 训练完成 |
| | 75pct | 42, 43, 44 | 训练完成 |
| | 100pct | 42 | **step 162/165 (98%) 被 SIGHUP 终止** |
| | 100pct | 43, 44 | 未开始 |

### 关键问题

脚本在所有 scale×seed 全部完成后才一次性写入结果文件。100pct/seed42 在 98% 时被 kill，导致 **全部 9 个已完成的训练结果丢失**（25pct×3 + 50pct×3 + 75pct×3）。

### Registry / Cron

- Registry 已更新：conclusion=killed, status=DONE
- Cron 已删除

### 下一步

需要完整重跑。建议改进脚本，每完成一个 scale×seed 就增量写入结果，避免再次全损。

---
