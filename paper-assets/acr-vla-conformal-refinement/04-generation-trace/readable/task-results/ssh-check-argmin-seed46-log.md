# ssh check argmin seed46 log

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-argmin-seed46-log_20260517T084155_result.json`
- **Structured JSON:** [`749aa238417a383da36f.json`](../../sessions/74/749aa238417a383da36f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 已不存在，无需删除。

**实验结果汇总：eval-argmin-object-seed46**

| 指标 | 值 |
|---|---|
| **Overall SR** | **10.0% (10/100)** |
| 状态 | 成功完成 |
| 服务器 | bjb1-32546, cuda:1 |

**Per-task SR：**

| Task | SR |
|---|---|
| alphabet_soup | 0% |
| cream_cheese | 0% |
| salad_dressing | 10% |
| **bbq_sauce** | **40%** |
| ketchup | 0% |
| tomato_sauce | 10% |
| butter | 10% |
| milk | 10% |
| chocolate_pudding | 10% |
| orange_juice | 10% |

Overall 10.0% 略低于预期的 12-17% 范围。bbq_sauce 是唯一明显高于平均的 task (40%)，alphabet_soup/cream_cheese/ketchup 三个 task 完全失败。Registry 已更新 metrics + conclusion=success。

---
