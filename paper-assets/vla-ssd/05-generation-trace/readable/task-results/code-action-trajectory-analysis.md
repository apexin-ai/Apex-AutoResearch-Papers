# code action trajectory analysis

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_action_trajectory_analysis_20260518T103905_result.json`
- **Structured JSON:** [`ba30b24796b766bd2caa.json`](../../sessions/ba/ba30b24796b766bd2caa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已提交。

- **exp_id**: `action_trajectory_analysis`
- **tmux session**: `action_trajectory_analysis`
- **GPU**: cuda:0
- **预计时间**: ~20-40 分钟（5000 forward passes）
- **日志**: `/root/autodl-tmp/vla-ssd/results/action_trajectory_analysis.log`
- **结果**: `/root/autodl-tmp/vla-ssd/results/action_trajectory_analysis.json`

Dry-run 验证通过：ablation 使 78.6% action tokens 发生变化，paired MSE=0.14，KL divergence=5.19。gripper 维度受影响最大。

---
