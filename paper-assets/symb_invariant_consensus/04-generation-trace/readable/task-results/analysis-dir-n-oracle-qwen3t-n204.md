# analysis dir n oracle qwen3t n204

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_dir-n-oracle-qwen3t-n204_20260520T213804_result.json`
- **Structured JSON:** [`1039e1e5d474b88e1dd8.json`](../../sessions/10/1039e1e5d474b88e1dd8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。N=204 重算结果：

| | Dir-N (n=166) | N=204 (本次) |
|---|---|---|
| SC@12 | 83.7% | **86.27%** |
| Oracle@12 | 89.8% | **91.18%** |
| Oracle Gap | 6.0pp | **4.90pp** |

Oracle curve (N=204):
- Oracle@1: 85.48% ± 1.05%
- Oracle@2: 87.99% ± 0.82%
- Oracle@3: 88.81% ± 0.68%
- Oracle@4: 89.38% ± 0.68%
- Oracle@6: 90.16% ± 0.52%
- Oracle@8: 90.53% ± 0.47%
- Oracle@12: 91.18% ± 0.00%

结果写入 `/root/symb_invariant_consensus/results/dir_n_oracle_qwen3t_n204/results.json`。

补充的 38 题整体偏简单（多数 12 traces 全部一致），SC 和 Oracle 都涨，但 Oracle Gap 从 6.0pp 缩小到 4.90pp。

---
