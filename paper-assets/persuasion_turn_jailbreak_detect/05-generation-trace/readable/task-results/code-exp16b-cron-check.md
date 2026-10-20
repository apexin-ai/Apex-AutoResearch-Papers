# code exp16b cron check

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp16b-cron-check_20260520T001430_result.json`
- **Structured JSON:** [`a62bf5cb7013a0c1f018.json`](../../sessions/a6/a62bf5cb7013a0c1f018.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
exp16b Llama-only MLM: SUCCESS (正常完成)
- S1 MLM checkpoint: ✅ exists (checkpoints/exp16_llama_only_mlm/mlm_seed42/best/)
- S2 GRU checkpoint: ✅ exists (checkpoints/exp16_llama_only_mlm/mlm_gru_seed42/baseline/)
- S1 best val_loss: 5.1489 (epoch 4/4)
- S2 best val_loss: 0.3776, val_acc: 0.8514 (epoch 19/20)

exp17 MLM fix: BOTH DONE
- GPU0: ✅ 完成 (07:50:20), best val_loss=0.0492, val_acc=0.9933
- GPU1: ✅ 完成 (07:50:00), best val_loss=0.0524, val_acc=0.9867

GPU 0-3: 全部空闲 (0% util, 0 MiB)
```

---
