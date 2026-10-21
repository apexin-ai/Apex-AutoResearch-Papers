# eval grid b05 seed42

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_grid-b05-seed42_20260514T072916_result.json`
- **Structured JSON:** [`0be5e6784432aaeadf35.json`](../../sessions/0b/0be5e6784432aaeadf35.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**grid_b b=0.5 seed42 eval perplexity = 17.65**

| 方法 | Eval PPL |
|------|---------|
| uniform 均值 | 17.694 |
| **grid_b b=0.5 seed42** | **17.651** |
| adaptive 均值 | 17.639 |

b=0.5 的 PPL (17.651) 位于 uniform (17.694) 和 adaptive (17.639) 之间，比 uniform 好 0.043，比 adaptive 差 0.012。结果已保存到 `output/eval_grid_b0_5_seed42.json`。

---
