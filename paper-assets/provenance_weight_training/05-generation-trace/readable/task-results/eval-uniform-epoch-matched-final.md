# eval uniform epoch matched final

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_uniform_epoch_matched_final_20260521T134506_result.json`
- **Structured JSON:** [`18fbe301657284c92d83.json`](../../sessions/18/18fbe301657284c92d83.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果汇总：

```
uniform_epoch_matched_indep_lr_seed42:
  holdout_ppl: 18.06206
  holdout_loss: 2.89381
  ood_owt_ppl: 18.64966
  ood_wiki_ppl: 15.51100
```

与 D&R 对照比较：

| Metric | D&R | Uniform | Δ |
|--------|-----|---------|---|
| Holdout PPL | 18.78174 | 18.06206 | -0.720 (uniform更好) |
| OOD OWT PPL | 19.23533 | 18.64966 | -0.586 (uniform更好) |
| OOD Wiki PPL | 15.95958 | 15.51100 | -0.449 (uniform更好) |

Uniform baseline 在所有三个指标上都优于 D&R epoch-matched 模型。

---
