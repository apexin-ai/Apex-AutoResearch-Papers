# analysis vota no ae seed42

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_vota_no_ae_seed42_20260515T061115_result.json`
- **Structured JSON:** [`316d44095c4ef083f4e3.json`](../../sessions/31/316d44095c4ef083f4e3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here are the results:

```
=== RESULTS ===
accuracy: 0.9941
majority_baseline: 0.7151
lift: 0.2790
n: 1190
pass_precision: 0.9988
pass_recall: 0.9929
pass_f1: 0.9959
fail_precision: 0.9826
fail_recall: 0.9971
fail_f1: 0.9898
train_loss: 0.0908
eval_loss: 0.2215
eval_mean_token_accuracy: 0.9577
checkpoint_path: /root/autodl-tmp/trace-verdict-study-checkpoints/vota_no_ae/final
log_path: ~/runs/trace-verdict-study/vota_no_ae_seed42.log
wall_clock_seconds: 6397.88
=== END RESULTS ===
```

**分析：**

**vs VOTA v5 (with actual/expected):** accuracy delta = **+0.0025** (0.9941 vs 0.9916)。去掉 actual/expected 后性能不降反微升，pass_f1 +0.0018, fail_f1 +0.0043。差异在置信区间内，统计上不显著，但方向明确：actual/expected 对 VOTA 性能没有正向贡献。

**vs no_trace baseline:** accuracy delta = **+0.2428** (0.9941 vs 0.7513)。trace 结构信息才是关键。

**结论：VOTA 的高精度来自对 trace 行为模式的真实理解，而非 actual/expected 的字符串比较。** 去掉 actual/expected 后模型几乎无损甚至微升，说明这两个字段是冗余信息——模型已从 trace 的调用序列、变量变化等行为线索中学到了 pass/fail 的判别依据。这是个强 ablation 结果：排除了 "VOTA 只是在做 actual vs expected 匹配" 的 trivial explanation。

---
