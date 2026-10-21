# harvest cqa1 analyzing 3

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_cqa1-analyzing-3_20260526T195904_result.json`
- **Structured JSON:** [`e4a35487c69e21121b3f.json`](../../sessions/e4/e4a35487c69e21121b3f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 3 ANALYZING experiments harvested and marked DONE. Here's the summary:

## ANALYZING 收割结果

| exp_id | SR | trigger_rate | correction_norm | conclusion |
|--------|-----|-------------|-----------------|------------|
| pi05-adaptive-long-s44-cqa1-r3 | **83%** | 4.48% | 0.20 | success |
| pi05-adaptive-object-s43-cqa1-r3 | **85%** | 4.02% | 0.20 | success |
| pi05-adaptive-object-s44-cqa1-r3 | **88%** | 3.48% | 0.20 | success |

日志检查：3 个实验均 EXIT_CODE=0，无 OOM/CUDA error（long-s44 的 25 个 grep 命中全是 "LIVING_ROOM" 中 "OOM" 子串的误匹配）。

## RUNNING 状态检查

| exp_id | 状态 | 进度/详情 |
|--------|------|-----------|
| **pi05-adaptive-long-s43-cqa1-r3** | alive (PID 350877, 9h+) | 9/10 tasks done, 最后一个 KITCHEN_SCENE6 跑到 15/20 rollout，即将完成 |
| smolvla-crm-norm005-k10-object-s44-cqa1 | alive (PID 492013, cuda:3) | chocolate_pudding 15/20 (task 9/10) |
| smolvla-adapt-tau015-object-s42-cqa1 | alive (PID 488512, cuda:0) | chocolate_pudding 15/20 (task 9/10) |
| smolvla-adapt-tau015-object-s43-cqa1 | alive (PID 489509, cuda:1) | chocolate_pudding 15/20 (task 9/10) |
| smolvla-adapt-tau015-object-s44-cqa1 | alive (PID 491099, cuda:2) | chocolate_pudding 15/20 (task 9/10) |

**所有 5 个 RUNNING 实验均存活，且都接近完成**（剩最后 1-2 个 task）。pi05-adaptive-long-s43（Table 2 最后缺失格）预计 ~30 分钟内完成。SmolVLA 4 个实验也只剩最后 1 个 task 的尾巴。

---
