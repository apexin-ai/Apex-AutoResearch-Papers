# ssh harvest seed45 fisher test

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_harvest-seed45-fisher-test_20260516T185120_result.json`
- **Structured JSON:** [`3fac67fd4576db1ad1c9.json`](../../sessions/3f/3fac67fd4576db1ad1c9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两边都在运行中，尚未完成。

## 当前状态

**bjb1-32546 (obs_only seed45)**: 8/10 tasks 完成
- 中间统计: 10/80 successes so far (0+0+1+4+1+1+1+2)
- 最后修改: 02:49 CST，正在跑 task 9
- 预估 ETA: ~2-3 小时 (约 05:00-06:00 CST)

**bjb2-28827 (argmin seed45)**: 6.5/10 tasks 完成 (task 7 butter 在 rollout 5/10)
- 中间统计: 5/60 successes so far (0+0+1+4+0+0)
- 最后修改: 02:51 CST，正在跑 task 7 的后半
- 预估 ETA: ~5-6 小时 (约 08:00-09:00 CST)

## 初步趋势观察

obs_only seed45 当前: 10/80 = 12.5% (8 tasks done)
argmin seed45 当前: 5/60 = 8.3% (6 tasks done)

差异方向与前 3 seeds 一致 (obs > argmin)，但绝对值比前几个 seed 偏低。

---

两实验均未完成，无法计算 4-seed Fisher test。建议数小时后再查收。需要我设置定时轮询吗？

---
