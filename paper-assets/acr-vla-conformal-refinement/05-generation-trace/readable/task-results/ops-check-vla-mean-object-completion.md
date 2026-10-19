# ops check vla mean object completion

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-vla-mean-object-completion_20260515T170014_result.json`
- **Structured JSON:** [`8650e166821c02b305dd.json`](../../sessions/86/8650e166821c02b305dd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**eval-vla-mean-object 已完成，registry 已更新为 DONE。**

结果汇总：
- **Overall SR: 12.0% (12/100)**
- 10/10 tasks 全部完成

| Task | SR |
|------|-----|
| alphabet_soup | 0% |
| cream_cheese | 0% |
| salad_dressing | 10% |
| bbq_sauce | 30% |
| ketchup | 10% |
| tomato_sauce | 10% |
| butter | 0% |
| milk | 20% |
| chocolate_pudding | 30% |
| orange_juice | 10% |

与 reconvla-object（也是 12% SR）完全一致——VLA mean 和 ReconVLA argmin 在 object benchmark 上表现相同。

cuda:5 已释放（2 MiB, 0% 利用率）。JSON 输出已保存在 `logs/eval_object_vla_mean.json`。

---
