# eval plan002 seed123 dd ood

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_plan002-seed123-dd-ood_20260518T070812_result.json`
- **Structured JSON:** [`9b015a7ac29506f4f636.json`](../../sessions/9b/9b015a7ac29506f4f636.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**结果**：plan_002 seed=123 DD OOD 与 seed=42 **完全一致**：

| K | seed=42 | seed=123 |
|---|---------|----------|
| 1 | 1.0 | 1.0 |
| 2 | 0.9904 | 0.9904 |
| 3 | 0.9904 | 0.9904 |
| 5 | 1.0 | 1.0 |
| full | 1.0 | 1.0 |

9-class persuasion treatment 跨 seed 方差 = 0，与 control variants（MLM std=0.115, topic std=0.207）形成鲜明对比。核心 claim 安全——persuasion treatment 的 DD OOD 泛化是稳定的，不是 seed lottery。

Registry 和 artifact 均已更新。还需要 seed=456 的 DD OOD 来完成 3-seed 全貌。

---
