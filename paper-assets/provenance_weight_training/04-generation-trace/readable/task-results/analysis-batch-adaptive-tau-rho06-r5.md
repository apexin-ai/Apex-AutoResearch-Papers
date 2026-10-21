# analysis batch adaptive tau rho06 r5

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_batch_adaptive_tau_rho06_r5_20260517T173708_result.json`
- **Structured JSON:** [`7db3257baacc43ef145d.json`](../../sessions/7d/7db3257baacc43ef145d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 完成。结果如下：

```
=== 实验结果 ===
exp_id: batch_adaptive_tau_rho06_r5
train_loss: 9.267
train_runtime: 13903 seconds (~3h51m)
total_steps: 6103
eval_ppl_holdout: 17.73
eval_loss_holdout: 2.8754
eval_holdout_tokens: 4077068
eval_method: sliding window (max_length=2048, stride=1024, 5000 docs, fp16)
checkpoint_path: /root/autodl-tmp/output/models/batch_adaptive_tau_rho06_seed42/final

=== 与 ρ=0.6 baselines 对比 ===
vs uniform (17.766):           -0.036 (略好)
vs adaptive fixed τ=0.8 (17.74): -0.010 (几乎持平)
vs τ=0.7 (17.73):              +0.000 (持平)
vs τ=0.6 (17.7359):            -0.006 (持平)
vs grid-best b=0.5 (17.704):   +0.026 (略差)
vs ESS-only (17.77):           -0.040 (略好)
vs hybrid (17.53):             +0.200 (明显差)

=== 结论 ===
conclusion: NEGATIVE

理由:
1. PPL=17.73 与 adaptive fixed τ=0.8 (17.74) 几乎无差异 (Δ=-0.01)，batch-adaptive τ 没有带来实质性改进
2. 不如 grid-best (17.704) 和 hybrid (17.53)
3. 结合 parent 实验 (ρ=0.4 也是 NEGATIVE，PPL=17.681 vs baseline 17.6527)，batch-adaptive τ 在两个 contamination level 上都未能证明优势
4. **batch-adaptive τ 这条路可以放弃**——per-batch 自适应阈值的额外复杂度没有换来 perplexity 收益，固定 τ 或 grid search b 更简单且效果相当或更好
```

---
