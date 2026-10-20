# analyze deepseek loop only seed123

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_deepseek_loop_only_seed123_20260520T001212_result.json`
- **Structured JSON:** [`be1b6194b36027549639.json`](../../sessions/be/be1b6194b36027549639.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

| Metric | seed123 | seed42 | Δ |
|--------|---------|--------|---|
| **Accuracy** | **81.26%** | **81.26%** | **0.00pp** |
| Accuracy 95% CI | [79.2%, 83.4%] | — | — |
| pass_recall | 0.856 | 0.883 | −2.7pp |
| fail_recall | 0.705 | 0.637 | +6.8pp |

**结论：✅ Seed robust.** Accuracy 与 seed42 完全一致（81.26%），在 78–84% 接受范围内。per-class recall 有轻微 tradeoff 偏移（seed123 更偏向 fail 检出），但总体性能无差异。无需额外 seed sweep。

报告已注册：`art_20260520_01050f`。

---
