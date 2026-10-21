# code baseline embeddings gru

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_baseline-embeddings-gru_20260517T074816_result.json`
- **Structured JSON:** [`2cee2c72379d7a4b1b17.json`](../../sessions/2c/2cee2c72379d7a4b1b17.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both steps completed successfully.

**Results:**

| Metric | Value |
|--------|-------|
| Test F1 | 0.9870 |
| Test Accuracy | 0.9868 |
| FPR@95TPR | 0.0000 |
| Test Loss | 0.0954 |
| Best Val F1 | 0.9730 (epoch 15) |

The baseline GRU achieves very strong performance. Training converged well: loss dropped from 0.70 to 0.03 over 20 epochs, with best validation F1 of 0.973 at epoch 15.

Outputs on server:
- Embeddings: `/root/persuasion_turn_jailbreak_detect/data/embeddings/baseline_{train,val,test}.pt`
- Best model: `/root/persuasion_turn_jailbreak_detect/checkpoints/baseline_gru/best.pt`
- Results JSON: `/root/persuasion_turn_jailbreak_detect/checkpoints/baseline_gru/results.json`

---
