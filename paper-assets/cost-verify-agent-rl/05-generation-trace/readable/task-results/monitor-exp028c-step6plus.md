# monitor exp028c step6plus

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_exp028c_step6plus_20260516T030739_result.json`
- **Structured JSON:** [`4ca8301be9a1ec231e9c.json`](../../sessions/4c/4ca8301be9a1ec231e9c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp028c Step 6 状态摘要

**进程**: PID 824675 存活，运行 5h30m，6/100 steps (6%)

**GPU**: 双卡正常工作，75-80% 利用率，48.4-48.5GB 显存，40-41°C

**关键指标 @ Step 6**:
| 指标 | Step 5 | Step 6 | 趋势 |
|------|--------|--------|------|
| success | 9.38% | 10.94% | 微升，但远低于 step 4 峰值 18.75% |
| kl_loss | **0.824** | **0.098** | 大幅回落，危机解除 |
| action_is_valid | 89.6% | 90.4% | 单调递增，从 74.5% 起步 |
| entropy | 0.236 | 0.234 | 平稳 |
| grad_norm | 13.08 | 12.54 | 稳定 |

**判断**: 训练稳定，kl_loss spike 已自愈。但 success rate 在 6 步内没有建立上升趋势（高方差震荡），这是主要隐忧。action_is_valid 持续改善说明模型在学格式，但还没转化为任务成功率。建议 step 10 再查一次，若 success 仍 <15% 需要考虑干预。

---
