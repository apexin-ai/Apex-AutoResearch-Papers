# ops check norm003 seed45 r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-norm003-seed45-r2_20260519T051433_result.json`
- **Structured JSON:** [`7272faa23135d19a3397.json`](../../sessions/72/7272faa23135d19a3397.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

| 字段 | 值 |
|---|---|
| **exp_id** | `eval-obs-only-object-norm003-seed45-r2` |
| **SR** | 不完整，仅完成 5/10 tasks |
| **conclusion** | `killed` |
| **理由** | 进程在 task 6 (tomato_sauce) rollout 5/10 处被静默终止，无错误信息，无 JSON 输出。与当天 kill bjb1-18228 上 norm003 实验腾 GPU 的操作一致。 |

**已完成 tasks 的部分 SR：**
- alphabet_soup: 0% (0/10)
- cream_cheese: 0% (0/10)  
- salad_dressing: 20% (2/10)
- bbq_sauce: 30% (3/10)
- ketchup: 0% (0/10)
- 部分平均: 10%

如需补跑此 seed，需要重新启动完整 eval。

---
