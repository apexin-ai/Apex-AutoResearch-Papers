# eval mvp kl s42

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_mvp_kl_s42_20260515T131552_result.json`
- **Structured JSON:** [`5deb526f947b461c5486.json`](../../sessions/5d/5deb526f947b461c5486.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

```json
{
  "eval_results": {
    "wikitext2_ppl_dense": 6.12,
    "wikitext2_ppl_sparse": 455.93,
    "ppl_increase_pct": "+7349%",
    "model_level_sparsity": 0.372
  },
  "sparsity_collapse_analysis": {
    "root_cause": "KL loss (~556) vs reg loss (~0.017), 比值 32700:1，正则化完全失效",
    "reg_loss_weight": "0.1 (--sparsity_reg_weight 默认值)",
    "tau_schedule": "线性 1.0→0.1, 1000 steps",
    "fix_suggestions": [
      "1. --sparsity_reg_weight 提到 1000-5000",
      "2. 两阶段：BCE 预训练 → KL 微调",
      "3. KL loss 归一化（per-token 而非 batchmean）",
      "4. 延迟 tau annealing：warmup 期间保持 τ=1.0",
      "5. 自适应 λ：动态维持 KL:reg ≈ 10:1"
    ]
  },
  "comparison_with_bce": {
    "bce_sparse_ppl": 44.21,
    "kl_sparse_ppl": 455.93,
    "kl_better": false,
    "delta": -411.72
  },
  "missing_eval_reason": "train_kl() 和 train_bce() 都不调 evaluate.py，只存 checkpoint + wandb.finish()。BCE eval 是手动单独跑的。"
}
```

**Per-layer sparsity 分布**：前半层 (0-13) 高 sparsity 0.47-0.72，后半层 (14-31) 极低 0.10-0.27。Predictor 学到了"后层更重要"但没学到神经元级选择，所以后层几乎全保留，前层被过度剪枝 → PPL 崩坏。

**关键代码位置**：
- `losses.py:48` — SparsityRegularizer weight=0.1，max output 仅 0.05
- `train.py:76` — `reg_fn = SparsityRegularizer(target, 0.1)`，未 scale
- `train.py:97` — `tau = tau_start + (tau_end - tau_start) * (step/num_steps)` 线性递减
- `train.py:107` — `loss = (kl + reg) / ga`，KL 和 reg 直接相加无权重调节

**Dense PPL 差异**：本次 6.12 vs BCE baseline 报告 27.96 待查。可能 BCE eval 时环境/参数不同。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "eval_results": {
      "wikitext2_ppl_dense": 6.12,
      "wikitext2_ppl_sparse": 455.93,
      "ppl_increase_pct": "+7349%",
      "model_level_sparsity": 0.372
    },
    "sparsity_collapse_analysis": {
      "root_cause": "KL loss (~556) vs reg loss (~0.017), 比值 32700:1，正则化完全失效",
      "reg_loss_weight": "0.1 (--sparsity_reg_weight 默认值)",
      "tau_schedule": "线性 1.0→0.1, 1000 steps",
      "fix_suggestions": [
        "1. --sparsity_reg_weight 提到 1000-5000",
        "2. 两阶段：BCE 预训练 → KL 微调",
        "3. KL loss 归一化（per-token 而非 batchmean）",
        "4. 延迟 tau annealing：warmup 期间保持 τ=1.0",
        "5. 自适应 λ：动态维持 KL:reg ≈ 10:1"
      ]
    },
    "comparison_with_bce": {
      "bce_sparse_ppl": 44.21,
      "kl_sparse_ppl": 455.93,
      "kl_better": false,
      "delta": -411.72
    },
    "missing_eval_reason": "train_kl() 和 train_bce() 都不调 evaluate.py，只存 checkpoint + wandb.finish()。BCE eval 是手动单独跑的。"
  }
}
```

</details>

---
