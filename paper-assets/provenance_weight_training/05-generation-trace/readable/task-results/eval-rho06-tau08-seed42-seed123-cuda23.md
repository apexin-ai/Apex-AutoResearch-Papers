# eval rho06 tau08 seed42 seed123 cuda23

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_rho06_tau08_seed42_seed123_cuda23_20260520T141334_result.json`
- **Structured JSON:** [`02b5f1f318e9c56ca02e.json`](../../sessions/02/02b5f1f318e9c56ca02e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。两个模型的完整 eval 结果：

### contamination_60_adaptive_seed42_tau08
```
holdout_ppl: 17.74
eval_ppl_openwebtext: 18.42
eval_ppl_wikipedia: 15.37
downstream_arc_easy_acc_norm: 0.6120
downstream_arc_challenge_acc_norm: 0.3439
downstream_hellaswag_acc_norm: 0.4802
downstream_piqa_acc_norm: 0.6850
downstream_winogrande_acc: 0.5777
downstream_mean: 0.5398
```

### contamination_60_adaptive_seed123_tau08
```
holdout_ppl: 17.73
eval_ppl_openwebtext: 18.40
eval_ppl_wikipedia: 15.34
downstream_arc_easy_acc_norm: 0.6014
downstream_arc_challenge_acc_norm: 0.3447
downstream_hellaswag_acc_norm: 0.4804
downstream_piqa_acc_norm: 0.6877
downstream_winogrande_acc: 0.5699
downstream_mean: 0.5368
```

两个 seed 的结果非常接近，与 tau=0.7 的三个 seed (mean 0.5403/0.5361/0.5375) 基本持平。Registry 已更新。

---
