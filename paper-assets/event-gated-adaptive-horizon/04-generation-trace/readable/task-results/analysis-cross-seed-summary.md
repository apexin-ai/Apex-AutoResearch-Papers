# analysis cross seed summary

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cross_seed_summary_20260529T005629_result.json`
- **Structured JSON:** [`1d380ecd7196afea8be6.json`](../../sessions/1d/1d380ecd7196afea8be6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。文件写入 `artifacts/cross_seed_summary.md` 并注册为 `art_20260529_012b3e`。

9 组配置覆盖情况：

| 组 | Seeds | eval mean±std | CIVO rate |
|---|---|---|---|
| Walker baseline | 4 | 787.7±230.8 | — |
| Walker 008d | 4 eval / 5 NVE | 190.6±90.2 | 5/5 |
| Walker 008f | 4 | 302.4±134.8 | 0/4 |
| Walker 008a | 4 | 820.9±68.8 | 0/4 |
| Walker 008e_v3 | 4 | 689.8±369.1 | 0/4* |
| Cheetah baseline | 2 | 446.1±2.9 | — |
| Cheetah 008d | 4 | 123.2±132.9 | 3/4 |
| Cartpole baseline | 3 | 673.3±142.0 | — |
| Cartpole 008d | 3 | 236.3±29.7 | 0/3 |

Cartpole control (008f/008a) 在 registry 中无数据，已标注"无数据"。

---
