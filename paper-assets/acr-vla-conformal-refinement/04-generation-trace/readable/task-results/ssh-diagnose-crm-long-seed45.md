# ssh diagnose crm long seed45

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_diagnose-crm-long-seed45_20260519T221351_result.json`
- **Structured JSON:** [`b857f525421d51a27e26.json`](../../sessions/b8/b857f525421d51a27e26.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

eval-crm-long-seed45 **成功完成**，注册表已更正（之前被自动标记为 failed，实际有完整输出）。

**结果**: overall_success_rate = **18%** (18/100)

CRM-Long 四个 seed 汇总：

| seed | success rate |
|------|-------------|
| 42 | 17% |
| 43 | 15% |
| 44 | 20% |
| 45 | 18% |
| **mean** | **17.5%** |

Per-task 分布（seed45）：KITCHEN_SCENE3 最高 80%，KITCHEN_SCENE6 40%，其余多数 0-30%。与其他 seed 趋势一致。

---
