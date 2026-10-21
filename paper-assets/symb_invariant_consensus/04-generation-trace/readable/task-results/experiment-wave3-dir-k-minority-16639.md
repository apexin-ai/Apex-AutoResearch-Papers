# experiment wave3 dir k minority 16639

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_wave3-dir-k-minority-16639_20260520T100637_result.json`
- **Structured JSON:** [`4d3a996f9918f9847bee.json`](../../sessions/4d/4d3a996f9918f9847bee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。Direction K Minority Report 结果：

| Variant | Accuracy | Delta vs SC | Flips (correct/wrong) |
|---------|----------|-------------|----------------------|
| SC baseline | 54.41% | — | — |
| strict | 54.41% | +0.00 | 0 (0/0) |
| moderate | 49.51% | -4.90 | 76 (27/49) |
| combined | 54.41% | +0.00 | 12 (6/6) |

关键发现：minority traces 的 consistency precision 只有 35.53%（76 次 minority 更 consistent，但仅 27 次是对的）。少数派更 consistent 并不意味着更正确——这个 direction 不 work。Minority 只有 33.73% 是 ground truth，而 majority 是 48.80%。

- PID: 307412（已运行完毕，2.1s）
- 结果文件: `/root/symb_invariant_consensus/results/direction_k_minority_report/results.json`

---
