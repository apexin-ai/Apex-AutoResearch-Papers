# analysis plan 001 flat nli seed43 metrics

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan_001_flat_nli_seed43_metrics_20260515T202713_result.json`
- **Structured JSON:** [`4db66cfc7064ba01d134.json`](../../sessions/4d/4db66cfc7064ba01d134.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集。汇总如下：

```
训练完成状态: 正常结束 (EXIT_CODE=0)
训练类型: RSFT (非 GRPO)
基座模型: Qwen3-4B + SFT adapter
训练数据: 2691 samples (flatNLI filtered, CED mean=0.725)
总步数: 507 (3 epochs)
训练耗时: 1h54m40s

最终 train_loss: 0.6248
最终 eval_loss: 0.7567
最终 eval_mean_token_accuracy: 0.8298
最终 eval_entropy: 0.6778

Task Eval (DocRE, 50 docs):
  Step 169 (epoch ~1): F1=0.4825, Ign-F1=0.4825, Evi-F1=0.7596, EDCR=0.6278 (771 preds)
  Step 338 (epoch ~2): F1=0.4542, Ign-F1=0.4542, Evi-F1=0.7661, EDCR=0.6354 (964 preds)
  Step 507 (epoch  3): F1=0.4866, Ign-F1=0.4866, Evi-F1=0.7834, EDCR=0.6402 (782 preds)

RSFT Checkpoints: checkpoint-350, 400, 450, 500, 507
GRPO Checkpoints (grpo_flatnli_r3/): checkpoint-20, 40, 60, 80, 100

输出目录: /root/autodl-tmp/rsft_output_flat_nli_s43/
W&B: 未启用（日志中无 wandb 记录）
```

关键观察：epoch 2 时 F1 下降到 0.4542，epoch 3 回升到 **0.4866**（最佳），Evi-F1 持续上升到 **0.7834**，EDCR 也持续改善到 **0.6402**。

---
