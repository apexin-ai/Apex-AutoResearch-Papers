# ssh status check and spatial submit

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_status_check_and_spatial_submit_20260522T010155_result.json`
- **Structured JSON:** [`c02c5e42e53850408e61.json`](../../sessions/c0/c02c5e42e53850408e61.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇报

### cf_batch_missing_v1 (PID 584349, cuda:0) — 运行 2h18m

5 个子任务中已完成 4 个，正在执行最后一个：

| # | 子任务 | 耗时 | 状态 |
|---|--------|------|------|
| 1 | openvla object untrained | 27.6 min | Done |
| 2 | tracvla spatial untrained | 29.9 min | Done |
| 3 | tracvla object untrained | 28.5 min | Done |
| 4 | tracvla goal untrained | 28.9 min | Done |
| 5 | tracvla long untrained | — | **进行中**: "wrong" condition 4400/5000 |

"wrong" condition 剩余 600 iterations (~1 min)，之后还有 "paraphrased" condition (5000 iterations, ~15-20 min)。**预计 ~15-20 分钟后完成。**

### openvla_goal_standardized_v1 (PID 591230, cuda:1) — 运行 29m

目前在第一个 condition（可能是 trained），Phase 6 (counterfactual analysis) 的 "wrong" condition at 600/5000。Phases 1-5 耗时 ~26 min。Phase 6 剩余量较大，之后还要跑第二个 condition（untrained），**预计还需 1.5-2 小时。**

### GPU 状态
- cuda:0: 58% utilization, 9.5/95.6 GB — cf_batch 占用
- cuda:1: 90% utilization, 15.3/95.6 GB — goal pipeline 占用

### 结论

**cf_batch 仍在 cuda:0 上运行，不提交 Spatial pipeline。** 预计 cf_batch ~15-20 分钟后完成，届时可提交。

---
