# train mf1 binary seed456

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_mf1-binary-seed456_20260518T091234_result.json`
- **Structured JSON:** [`63e6a955882192534ff6.json`](../../sessions/63/63e6a955882192534ff6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

MF1 Binary Persuasion DeBERTa+GRU+DD OOD Eval (seed=456) 全部完成。

**结果摘要：**

| 阶段 | 指标 |
|------|------|
| Stage 1 DeBERTa | val_persuasion_acc=1.0, val_intent_acc=1.0 |
| Stage 2 GRU | val_acc=1.0 |
| Stage 3 DD OOD | F1@K1=1.0, K2=1.0, K3=0.9904, K5=1.0, Full=1.0 |

**产出文件：**
- DeBERTa checkpoint: `checkpoints/mf1_binary_seed456/deberta_multitask/best/`
- GRU checkpoint: `checkpoints/mf1_binary_seed456/gru/treatment/best.pt`
- 评估结果: `results/mf1_binary_seed456.json`
- Registry: `mf1_binary_seed456` → DONE (success)

---
