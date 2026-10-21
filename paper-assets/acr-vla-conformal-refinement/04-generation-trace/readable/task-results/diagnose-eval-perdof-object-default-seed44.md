# diagnose eval perdof object default seed44

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-perdof-object-default-seed44_20260517T072242_result.json`
- **Structured JSON:** [`62e92b80f9f9bb7ea8a6.json`](../../sessions/62/62e92b80f9f9bb7ea8a6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

确认完毕。无 partial JSON output（进程在写 JSON 前被 timeout kill 了）。

## 诊断结果

| 指标 | 值 |
|------|-----|
| **tasks_completed** | 9/10 |
| **rollouts_completed** | 90/100 |
| **partial_success_rate** | **0.0%** (0/90) |
| **partial JSON output** | 不存在（timeout 在第 10 个 task 执行期间 kill 了进程，JSON 未写入） |
| **OOM/error** | 无 OOM，无 Python error |

**失败模式确认**: Catastrophic collapse confirmed。所有 9 个已完成 task（90 个 rollouts）成功率为 0%。超时原因是每个 rollout 都跑满 max_steps=300（因为 agent 永远无法完成任务），导致总时间超过 24h 限制。第 10 个 task (`pick_up_the_orange_juice_and_place_it_in_the_basket`) 未开始即被 kill。

**结论**: 数据已足够判定 perdof+default 配置在 object benchmark 上完全失效（0% success rate），不需要重跑。缺失的第 10 个 task 不会改变结论。

---
