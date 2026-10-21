# exp exp 020 fewnerd smoke

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_exp_020_fewnerd_smoke_20260516T102550_result.json`
- **Structured JSON:** [`b5eabcab3cd6a7f62645.json`](../../sessions/b5/b5eabcab3cd6a7f62645.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Training launched successfully on cuda:1 (RTX 5090).

**Status:**
- Config: `train_config_fewnerd.yaml` — Qwen3-8B, LoRA rank=16, 1 epoch, Few-NERD SUPERVISED (131K samples)
- Total steps: 8,236 at ~1.9s/step → ETA ~4.3 hours (~22:50 server time)
- Log: `checkpoints/fewnerd_train.log`
- Registry: `exp_020_fewnerd_smoke` → RUNNING

I'll check back shortly to verify loss at step 50, then periodically until training completes. After that: export merged model → pilot inference (200 instances, N=8) → 5-signal analysis.

---
