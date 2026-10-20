# train mf1 binary seed123

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_mf1-binary-seed123_20260518T093440_result.json`
- **Structured JSON:** [`f053af552184fbaaa9b3.json`](../../sessions/f0/f053af552184fbaaa9b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Pipeline 完成。结果汇总：

**DeBERTa Stage 1 (seed=123)**
- Best epoch: 3 (val_loss=0.0006)
- Val Persuasion Acc: 1.0, Val Intent Acc: 1.0

**GRU Stage 2 (seed=123)**
- Val Acc: 1.0 from epoch 1

**DD OOD F1 (macro)**

| K | F1 |
|---|-----|
| 1 | 1.0000 |
| 2 | 1.0000 |
| 3 | 0.9904 |
| 5 | 1.0000 |
| Full | 1.0000 |

**IID F1 (macro)**

| K | F1 |
|---|-----|
| 1 | 1.0000 |
| 2 | 1.0000 |
| 3 | 1.0000 |
| 5 | 1.0000 |
| Full | 1.0000 |

结果与 seed=456 几乎一致，K=3 的 DD OOD 同样是 0.9904（1 个 DD 样本在截断到 3 turns 时被漏掉）。Artifact 已注册为 `art_20260518_9f4f78`。

---
