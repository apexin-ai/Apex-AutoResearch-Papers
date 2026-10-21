# code add save predictions

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_add_save_predictions_20260515T141334_result.json`
- **Structured JSON:** [`aec81dd9ae9da38558d2.json`](../../sessions/ae/aec81dd9ae9da38558d2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`--save_predictions` 参数已添加，`--help` 输出确认新参数正常显示。保存逻辑会在 `eval_results.json` 同目录下写入 `predictions.jsonl`，每行一个 `{id, label, pred, raw_pred}` JSON 对象。

---
