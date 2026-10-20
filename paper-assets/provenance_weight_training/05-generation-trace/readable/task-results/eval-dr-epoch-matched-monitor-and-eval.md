# eval dr epoch matched monitor and eval

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_dr_epoch_matched_monitor_and_eval_20260521T132152_result.json`
- **Structured JSON:** [`a30acfd4fda82580925e.json`](../../sessions/a3/a30acfd4fda82580925e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

```
dr_epoch_matched_indep_lr_seed42:
  holdout_ppl: 18.78174
  holdout_loss: 2.93288
  ood_owt_ppl: 19.23533
  ood_owt_loss: 2.95675
  ood_wiki_ppl: 15.95958
  ood_wiki_loss: 2.77006
  train_loss_final: 5.833
  total_steps: 2533
```

对比之前的 epoch-matched D&R (adaptive, PPL=17.65 holdout) 和 uniform full (PPL=17.694 holdout)，这次 independent LR 的 D&R holdout PPL=18.78，高出约 1.1。这说明独立 LR schedule 下 D&R 的 holdout perplexity 明显更差，LR confound 验证的初步结论是：之前 D&R 的优势部分来源于 LR schedule 差异，而非 weighting 本身。

---
