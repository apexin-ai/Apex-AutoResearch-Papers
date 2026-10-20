# collect westd ckpt6633 val final

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_collect_westd-ckpt6633-val-final_20260515T085504_result.json`
- **Structured JSON:** [`4254a33de8f4394ccfe1.json`](../../sessions/42/4254a33de8f4394ccfe1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。ckpt-6633 val eval 结果：

| 指标 | 值 |
|------|-----|
| **Accuracy** | **87.10%** |
| Majority baseline | 75.88% |
| **Gap vs majority** | **+11.23pp** |
| **F1 macro** | **78.79%** |
| F1 fail | 65.52% (P=92.26%, R=50.80%) |
| F1 pass | 92.07% (P=86.31%, R=98.64%) |
| Unparseable | 9 / 9335 |
| Wall clock | ~57 min (0.95 GPU-hr) |

特点：fail 类 precision 很高（92.3%）但 recall 偏低（50.8%），模型对 fail 的判断保守——说 fail 时大概率对，但漏掉了近一半的 fail 样本。

---
