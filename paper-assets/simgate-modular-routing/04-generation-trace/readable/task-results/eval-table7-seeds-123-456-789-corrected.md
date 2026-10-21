# eval table7 seeds 123 456 789 corrected

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_table7-seeds-123-456-789-corrected_20260515T230757_result.json`
- **Structured JSON:** [`a6d7f1bce819f2fdcbb2.json`](../../sessions/a6/a6d7f1bce819f2fdcbb2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个 seed 全部完成。

```
=== Table 7 fixed-split corrected eval ===

Checkpoint 路径：
- seed 123: checkpoints/ablation-b-seed123/final_adapter
- seed 456: checkpoints/ablation-b-seed456/final_adapter
- seed 789: checkpoints/ablation-b-seed789/final_adapter

Data split seed used: per-seed (123/456/789) — 训练代码 load_implicit_sft_data 的 seed 参数直接传入 args.seed

| Seed | Old (INVALIDATED) | Corrected | Δ       |
|------|-------------------|-----------|---------|
| 123  | 57.36%            | 58.10%    | +0.74%  |
| 456  | 57.48%            | 57.00%    | −0.48%  |
| 789  | 58.31%            | 52.70%    | −5.61%  |
```

结果已保存到 `results/table7/seed{123,456,789}_corrected.json`。

注意 seed 789 的 corrected balanced_acc 下降较大（58.31% → 52.70%），该 seed 的 val set 分布不同（deterministic=270, internal=35），模型严重过预测 internal 类（212 vs 93），导致 det recall 仅 31.1%。

---
