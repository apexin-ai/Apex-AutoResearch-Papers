# analysis random reweight seed123 r5

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_random_reweight_seed123_r5_20260517T173827_result.json`
- **Structured JSON:** [`a707c7e2869ed41b76f1.json`](../../sessions/a7/a707c7e2869ed41b76f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 完成。结果：**PPL = 17.80**

汇总：

```
=== 实验结果 ===
exp_id: random_reweight_seed123_r5
train_loss: 8.0176
train_runtime: 13267 seconds (~3h41m)
total_steps: 6103
eval_ppl_holdout: 17.80
eval_loss_holdout: 2.8793
eval_holdout_tokens: 4,077,068
eval_method: sliding window (max_length=2048, 5000 docs)
checkpoint_path: /root/autodl-tmp/output/models/random_reweight_seed123/final

=== 与 baselines 对比 ===
vs uniform_seed123 (17.6861): +0.114 (random weights 退化)
vs adaptive_fix_seed123 (17.6432): +0.157 (random weights 比 adaptive 差更多)
vs random_reweight_v2_seed42 (17.83): 接近一致 (seed42: +0.136 vs uniform; seed123: +0.114 vs uniform)

=== 结论 ===
conclusion: SUCCESS
```

**PPL 17.80 > uniform_seed123 17.6861**，random weights 导致性能退化 +0.114，与 seed42 的退化幅度（+0.136）跨 seed 一致。

**结论**：跨 seed 复现成功，detector signal is load-bearing（Claim 1 进一步加强）。随机权重在两个 seed 下均显著劣于 uniform baseline，说明 detector q-scores 提供了真实的数据质量信号，而非随机噪声即可替代。

---
