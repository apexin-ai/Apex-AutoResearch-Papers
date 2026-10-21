# eval uniform epoch matched ood

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_uniform_epoch_matched_ood_20260521T134728_result.json`
- **Structured JSON:** [`84123593e07ae55fc127.json`](../../sessions/84/84123593e07ae55fc127.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 OOD eval 完成。汇总结果：

```
uniform_epoch_matched_indep_lr_seed42:
  holdout_ppl:  18.062061    loss: 2.893814
  ood_owt_ppl:  18.649663    loss: 2.925828
  ood_wiki_ppl: 15.510996    loss: 2.741549
```

与 D&R 对照对比：

| 指标 | D&R | Uniform | Δ |
|------|-----|---------|---|
| Holdout PPL | — | 18.062 | — |
| OOD OWT PPL | 19.235 | 18.650 | **-0.585** (uniform 更好) |
| OOD Wiki PPL | 15.960 | 15.511 | **-0.449** (uniform 更好) |

Uniform 在两个 OOD 数据集上 PPL 均低于 D&R 对照。

---
