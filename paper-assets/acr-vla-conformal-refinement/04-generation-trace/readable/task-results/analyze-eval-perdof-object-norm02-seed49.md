# analyze eval perdof object norm02 seed49

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-perdof-object-norm02-seed49_20260520T155840_result.json`
- **Structured JSON:** [`a9842db6f398776416b5.json`](../../sessions/a9/a9842db6f398776416b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated to DONE/success.

## 分析结论

**实验状态：正常完成**（EXIT_CODE=0，全部 100 rollouts 跑完，无错误）

**Overall SR：12.0%**（12/100）

**Per-task breakdown：**

| Task | SR | Successes |
|------|----|-----------|
| alphabet_soup | 0% | 0/10 |
| cream_cheese | 0% | 0/10 |
| salad_dressing | 10% | 1/10 |
| bbq_sauce | 20% | 2/10 |
| ketchup | 0% | 0/10 |
| tomato_sauce | 0% | 0/10 |
| butter | 10% | 1/10 |
| milk | 20% | 2/10 |
| chocolate_pudding | 40% | 4/10 |
| orange_juice | 20% | 2/10 |

**判定：conclusion = success**（正常完成的 eval run）

- 之前的 `killed` 标记是误标——进程正常退出，EXIT_CODE=0，所有 rollout 完整运行
- SR=12% 略低于同系列 seed43-48 的 14-18% 范围，但在 seed variance 合理区间内（10 rollouts/task 的方差较大）
- Registry 已更新：status=DONE, conclusion=success, metrics 和 log_path/checkpoint_path 已填入

---
