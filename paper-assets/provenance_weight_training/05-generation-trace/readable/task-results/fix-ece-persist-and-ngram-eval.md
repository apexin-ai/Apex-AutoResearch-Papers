# fix ece persist and ngram eval

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_ece_persist_and_ngram_eval_20260521T103127_result.json`
- **Structured JSON:** [`2af069bca3e9fa7f05bd.json`](../../sessions/2a/2af069bca3e9fa7f05bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
ECE 持久化: OK — 文件路径: /root/autodl-tmp/provenance_weight_training/output/ece_results.txt
  TF-IDF ECE = 0.0478
  GPT-2 ECE = 0.1314
  N-gram ECE = 0.0685

ngram_seed42 eval (FP32):
  holdout_ppl: 17.820214 (source: /root/autodl-tmp/provenance_weight_training/output/eval_results/ngram_adaptive_seed42_eval_fp32.json)
  holdout_loss: 2.880333
  num_tokens: 4,077,068
  eval_time: 561.8s (GPU contention with concurrent eval on same GPU)
```

---
