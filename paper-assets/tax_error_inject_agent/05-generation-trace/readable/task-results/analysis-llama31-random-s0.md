# analysis llama31 random s0

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_llama31-random-s0_20260516T112621_result.json`
- **Structured JSON:** [`1d33fdacfb679a079881.json`](../../sessions/1d/1d33fdacfb679a079881.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已成功完成。从日志中提取的 epoch 边界 loss：
- Epoch 1 (step 1130): loss=0.4521
- Epoch 2 (step 2260): loss=0.2380
- Epoch 3 (final step 3387): 最终汇总 train_loss=0.3368

```
CONCLUSION: success
CHECKPOINT_PATH: /root/autodl-tmp/tax_error_inject_agent/output/llama31-random-s0/v0-20260516-171608/checkpoint-3387
TRAIN_LOSS: 0.3368
TOKEN_ACC: 0.9357
TRAIN_STEPS: 3387
TRAIN_DURATION_S: 7622
EPOCH1_LOSS: 0.452 (step 1130, instantaneous)
EPOCH2_LOSS: 0.238 (step 2260, instantaneous)
EPOCH3_LOSS: 0.134 (step 3380, 末尾instantaneous)
PEAK_MEMORY_GIB: 30.74
TRAIN_SAMPLES_PER_SEC: 3.554
```

与 s42 对比：train_loss 几乎一致（0.3368 vs 0.3366），token_acc 持平（0.9357 vs 0.9364），训练时长相同（7622s），步数一致（3387）。两个 seed 的结果高度一致，说明训练稳定。

---
