# diagnose exp 004 fisher heatmap w4

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_004_fisher_heatmap_w4_20260516T204303_result.json`
- **Structured JSON:** [`9c209293a5f1994ed091.json`](../../sessions/9c/9c209293a5f1994ed091.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：exp_004_fisher_heatmap_w4 失败（部分完成）。**

- **完成数**：7/18 conditions
- **失败点**：`arc_N16` 的 200 次 rep 全部跑完，但写结果文件时报 `OSError: [Errno 28] No space left on device`
- **根因**：磁盘满（写入时刻满，现在已恢复到 79% / 37GB 可用——可能有临时文件被清理了）

**已完成的 conditions**：
| Benchmark | N=5 | N=10 | N=16 |
|-----------|-----|------|------|
| mmlu | ✓ | ✓ | ✓ |
| gsm8k | ✓ | ✓ | ✗ |
| arc | ✓ | ✓ | ✗ |

**缺失 11 个**：gsm8k_N16, arc_N16, 以及所有 N=20/N=30/N=50（如果预期 6 个 N 值的话）。

实际看代码预期的 N 值列表才能确认是 18 还是其他数目，但至少 gsm8k_N16 和 arc_N16 未产出，且 N>16 的全部未运行。进程已终止，当前磁盘空间恢复，可以安全重跑缺失 conditions。

---
