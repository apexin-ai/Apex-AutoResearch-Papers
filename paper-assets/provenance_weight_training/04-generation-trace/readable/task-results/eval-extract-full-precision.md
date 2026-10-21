# eval extract full precision

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_extract_full_precision_20260521T102529_result.json`
- **Structured JSON:** [`320550d56be24b847cc5.json`](../../sessions/32/320550d56be24b847cc5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部提取完成。

```
adaptive_tau08_scratch_seed42_v3:
  holdout_ppl: 17.68850 (source: .../adaptive_tau08_scratch_seed42_v2/eval_results/ppl_holdout.json)
  holdout_loss: 2.87291
  ood_owt_ppl: 18.37026 (source: .../adaptive_tau08_scratch_seed42_v2/eval_results/ppl_openwebtext.json)
  ood_owt_loss: 2.91073
  ood_wiki_ppl: 15.34964 (source: .../adaptive_tau08_scratch_seed42_v2/eval_results/ppl_wikipedia.json)
  ood_wiki_loss: 2.73109

gpt2_adaptive_seed123_v3:
  holdout_ppl: 17.78848 (source: .../gpt2_adaptive_seed123_v2/eval_results/ppl_holdout.json)
  holdout_loss: 2.87855

gpt2_adaptive_seed456_v2:
  holdout_ppl: 17.79719 (source: .../gpt2_adaptive_seed456_v2/eval_results/ppl_holdout.json)
  holdout_loss: 2.87904

ngram_adaptive_seed456_v2:
  holdout_ppl: 17.82607 (source: .../ngram_adaptive_seed456_v2/eval_results/ppl_holdout.json)
  holdout_loss: 2.88066
```

Full precision (15 significant digits) values:

| Experiment | Holdout PPL | Holdout Loss | OOD OWT PPL | OOD Wiki PPL |
|---|---|---|---|---|
| adaptive_tau08 | 17.688499785519298 | 2.872914698782336 | 18.370262047524463 | 15.349638691164628 |
| gpt2_seed123 | 17.788479988957246 | 2.878551056147516 | — | — |
| gpt2_seed456 | 17.797192737566270 | 2.879040733487612 | — | — |
| ngram_seed456 | 17.826070212882566 | 2.880662004491443 | — | — |

---
