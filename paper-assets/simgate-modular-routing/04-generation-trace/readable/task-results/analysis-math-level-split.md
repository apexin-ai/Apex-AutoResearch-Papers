# analysis math level split

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_math-level-split_20260517T055900_result.json`
- **Structured JSON:** [`0bdf6182fec78bd84e08.json`](../../sessions/0b/0bdf6182fec78bd84e08.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

| | Level 4 (N=458) | Level 5 (N=502) | All (N=960) |
|---|---|---|---|
| internal_acc | 0.7576 (347/458) | 0.6474 (325/502) | 0.7000 (672/960) |
| code_acc | 0.7576 (347/458) | 0.6474 (325/502) | 0.7000 (672/960) |
| diff (int-code) | +0.00pp | +0.00pp | +0.00pp |
| McNemar chi2 | 0.0000 | 0.0000 | 0.0000 |
| p-value | 1.000000 | 1.000000 | 1.000000 |
| discordant (int_only / code_only) | 39 / 39 | 61 / 61 | 100 / 100 |

两个 level 的 internal 和 deterministic(code) 准确率完全相同，且 discordant pairs 对称（b=c），McNemar 统计量为 0，p=1。Level 5 的整体准确率比 Level 4 低约 11pp（0.6474 vs 0.7576），符合难度预期。数据集总量 960（不是文件名暗示的 800），Level 4/5 接近对半分（458/502）。

---
