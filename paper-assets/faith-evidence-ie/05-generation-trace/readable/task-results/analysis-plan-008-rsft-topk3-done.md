# analysis plan 008 rsft topk3 done

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan_008_rsft_topk3_done_20260515T210915_result.json`
- **Structured JSON:** [`d8e3a60ab236a0b31417.json`](../../sessions/d8/d8e3a60ab236a0b31417.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇报如下：

```
训练完成状态: 正常 (EXIT_CODE=0)
总步数: 1509 (3 epochs)
训练时长: 3h02m
最终 train_loss: 0.5543
最终 eval_loss: 0.8297
Token accuracy: 82.28%

Task eval (50-doc subset):
  Epoch 1 (step 503):  F1=0.4848, Evi-F1=0.7450, EDCR=0.6525
  Epoch 2 (step 1006): F1=0.4824, Evi-F1=0.6997, EDCR=0.6529
  Epoch 3 (step 1509): F1=0.5012, Evi-F1=0.6816, EDCR=0.5963

Checkpoints: 1350, 1400, 1450, 1500, 1509
cuda:3 状态: 空闲 (0 MiB, 0%)
W&B: 无（训练未配置 wandb logging）
```

**关键发现：** F1 随 epoch 上升（0.4848→0.5012），但 Evi-F1 持续下降（0.745→0.6816），EDCR 也在降（0.6525→0.5963）。呈现 **relation extraction 改善 vs 证据质量退化** 的 trade-off。

与 CED RSFT top_k=5 baseline (rel_f1=0.4596) 对比：subset F1=0.5012 表面更高，但注意这是 50-doc subset 而非 full dev，需要 full dev eval（eval_plan_008_rsft_topk3，已在 ALLOCATED 状态）才能做可靠对比。

---
