# analysis exception only seed456

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exception_only_seed456_20260515T175730_result.json`
- **Structured JSON:** [`6a42761f7e1522b7cc93.json`](../../sessions/6a/6a42761f7e1522b7cc93.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**exception_only_seed456 分析完成。**

| 指标 | seed42 | seed456 |
|------|--------|---------|
| accuracy | 99.83% | 99.83% |
| 95% CI | — | [99.58%, 100.0%] |
| pass F1 | — | 0.9988 |
| fail F1 | — | 0.9971 |
| lift over majority | — | +28.3pp |

两个 seed 的 accuracy 到小数点后四位完全一致（0.9983），**seed robustness 验证通过**。评估脚本未生成 predictions.jsonl，因此跳过了 paired bootstrap，但 diff=0 已无统计检验必要。

Registry 已更新：status=DONE, conclusion=success。

---
