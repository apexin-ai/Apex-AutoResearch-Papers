# analyze eval metrics batch 15B 3B

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_metrics_batch_15B_3B_20260515T230026_result.json`
- **Structured JSON:** [`17d692c5a83b5d63bca7.json`](../../sessions/17/17d692c5a83b5d63bca7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验 metrics 已更新成功。Registry 显示 conclusion=success, status=DONE, checkpoint_path 和 log_path 均已设置。

## 汇总

```
exp_001_eval_15B_s123_para_aligned_batch (paraphrased):
  d000: {mmlu: 0.6111, gsm8k: 0.5921, arc_challenge: 0.7547, humaneval: 0.1538}
  d005: {mmlu: 0.6140, gsm8k: 0.5439, arc_challenge: 0.7475, humaneval: 0.0769}
  d025: {mmlu: 0.6145, gsm8k: 0.5482, arc_challenge: 0.7504, humaneval: 0.1923}
  d100: {mmlu: 0.6290, gsm8k: 0.5307, arc_challenge: 0.7834, humaneval: 0.2308}

exp_001_eval_3B_d005_s123_gsm8k (aligned, original):
  gsm8k: 0.6308
```

趋势：1.5B para_aligned 随 dose 增加，mmlu/arc_challenge 上升（0.611→0.629, 0.755→0.783），gsm8k 下降（0.592→0.531），humaneval 波动但 d100 最高（0.231）。

---
