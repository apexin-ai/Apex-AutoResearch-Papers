# registry backfill detector baselines

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_registry_backfill_detector_baselines_20260521T041425_result.json`
- **Structured JSON:** [`9144d370da4969b65273.json`](../../sessions/91/9144d370da4969b65273.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

这 4 个实验已经全部录入 registry，状态都是 DONE，metrics 完整：

```
已存在（无需补录）:
- ngram_adaptive_seed42: PPL=17.82, conclusion=negative
- ngram_uniform_seed42: PPL=17.69, conclusion=success
- gpt2_adaptive_seed42: PPL=17.79, conclusion=negative
- gpt2_uniform_seed42: PPL=17.69, conclusion=success
```

部分条目缺少顶层 `checkpoint_path` 和 `log_path` 字段（但 spec 内有）。需要补全这些字段吗？

---
