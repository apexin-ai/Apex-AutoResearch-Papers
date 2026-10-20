# analysis v4 random fixed inject50

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_v4-random-fixed-inject50_20260515T014029_result.json`
- **Structured JSON:** [`0c362d946b7e00746784.json`](../../sessions/0c/0c362d946b7e00746784.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常完成，checkpoint 完整。无 W&B 集成。

```
STATUS: success (EXIT_CODE=0, epoch 3.0/3.0)
FINAL_LOSS: 0.4338 (train_loss)
LAST_STEP_LOSS: 0.2618 (step 1635/1635)
TOTAL_STEPS: 1635
TRAINING_TIME: 53m 8s (3188s)
TRAIN_SPEED: 1.95 s/it, 4.1 samples/s
CHECKPOINT_PATH: /root/autodl-tmp/tax_error_inject_agent/checkpoints/random_fixed_inject50/v0-20260515-084528/checkpoint-1635
WANDB_RUN_ID: N/A (未启用 W&B)
NOTES:
  - adapter_config.json + adapter_model.safetensors (167MB) 确认为 LoRA checkpoint
  - 每 epoch 保存一次 checkpoint (545, 1090, 1635)
  - 末期 loss 稳定在 0.23-0.29 范围，token_acc ~0.90-0.92
  - GPU 内存峰值 18 GiB
  - 与 TaxEI 50% 对比：train_loss 0.4338 略低于 TaxEI 50% 典型的 0.82-0.90 范围，说明 random injection 的错误模式可能比 taxonomy-guided injection 更容易学习（模型更容易拟合随机错误 pattern）
```

---
