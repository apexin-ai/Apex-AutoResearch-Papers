# analyze llama31 random s42

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_llama31-random-s42_20260516T083419_result.json`
- **Structured JSON:** [`ea362816e415838b872a.json`](../../sessions/ea/ea362816e415838b872a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
METRICS:
- train_loss: 0.33664
- token_acc: 0.93636
- train_steps: 3387
- train_duration_s: 7622
- epochs_completed: 3.0

CHECKPOINT_PATH: /root/autodl-tmp/tax_error_inject_agent/output/llama31-random-s42/v0-20260516-142300/checkpoint-3387
LOG_PATH: /root/runs/tax_error_inject_agent/llama31-random-s42.log
WANDB_RUN_ID: NONE

COMPARISON_VS_VANILLA:
- loss_diff: -0.0636 (random lower)
- acc_diff: +0.0297 (random higher)

CONCLUSION: success
NOTES: Random condition 训练步数(3387)是 vanilla(1635)的 2.07 倍，训练时长(7622s)也约为 vanilla(4157s)的 1.83 倍，说明 random 数据集样本量显著更大。Random 的 loss 更低、acc 更高，可能与数据量差异有关，对比时需控制数据量因素。每步 epoch 保存了 checkpoint（1129/2258/3387）。
```

---
