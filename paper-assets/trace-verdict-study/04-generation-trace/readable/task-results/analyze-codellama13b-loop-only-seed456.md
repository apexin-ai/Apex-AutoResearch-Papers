# analyze codellama13b loop only seed456

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_codellama13b_loop_only_seed456_20260520T125604_result.json`
- **Structured JSON:** [`a8ad081b26848f046613.json`](../../sessions/a8/a8ad081b26848f046613.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE (success)。cuda:0 无残留进程。

## CodeLlama-13B loop_only 跨 seed 汇总

| Seed | Accuracy |
|------|----------|
| 42 | 77.06% |
| 123 | 76.05% |
| 456 | **79.08%** |
| **Mean ± Std** | **77.40% ± 1.25pp** |

seed456 = 79.08%，落在假设区间内。3-seed 标准差仅 1.25pp，loop_only condition 在 CodeLlama-13B 上表现稳定。

---
