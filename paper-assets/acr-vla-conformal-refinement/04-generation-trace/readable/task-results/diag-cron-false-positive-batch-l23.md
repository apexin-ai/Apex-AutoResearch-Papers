# diag cron false positive batch L23

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_cron-false-positive-batch-L23_20260521T025221_result.json`
- **Structured JSON:** [`50849c68faafdc79988e.json`](../../sessions/50/50849c68faafdc79988e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

| 实验 | 服务器 | 实际状态 | 详情 |
|------|--------|---------|------|
| **eval-obs-only-object-norm005-seed65** | bjb1-18228 | **completed** | SR=14.0% (14/100)，输出 JSON 存在（1490B），日志完整到 "Results saved" |
| **eval-obs-only-object-norm005-seed62** | bjb2-28827 | **truly failed** | 日志仅到 task1 rollout 5/10 就中断，无输出 JSON。SIGHUP 导致进程被杀 |
| **eval-obs-only-object-norm005-seed63** | bjb2-28827 | **truly failed** | 同上，task1 rollout 5/10 处中断，SIGHUP |
| **eval-obs-only-object-norm01-seed61** | bjb2-28827 | **truly failed** | 同上，task1 rollout 5/10 处中断，SIGHUP |

**Registry 更新：**
- seed65：已补录 metrics `{success_rate: 0.14, total_rollouts: 100, successful_rollouts: 14}`。conclusion 已是 "success"，无需改。
- seed62/seed63/seed61：conclusion="failed" 正确，notes 已记录 SIGHUP 根因且已被 seed71-75 替代，无需修改。

只有 seed65 是 cron false positive（1/4）。bjb2-28827 上的 3 个是真实失败——该服务器有 SIGHUP 批量故障历史。

---
