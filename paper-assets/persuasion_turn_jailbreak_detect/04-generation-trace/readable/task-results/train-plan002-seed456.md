# train plan002 seed456

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_plan002-seed456_20260518T005229_result.json`
- **Structured JSON:** [`c336f5bdc5f5d7f76e3d.json`](../../sessions/c3/c336f5bdc5f5d7f76e3d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**plan_002 seed=456 全部完成。** 结果已保存到 `results/plan_002_seed456_eval.json`。

## 汇总

| K | Treatment F1 | Baseline F1 | TF-IDF F1 |
|---|---|---|---|
| 1 | 1.0000 | 0.9296 | 1.0000 |
| 2 | 1.0000 | 0.9589 | 1.0000 |
| 3 | 1.0000 | 0.9867 | 1.0000 |
| 5 | 1.0000 | 0.9867 | 1.0000 |
| full | 1.0000 | 1.0000 | 1.0000 |

**Stage 1**: DeBERTa best at epoch 2 (val_loss=0.4256, persuasion_acc=0.8593, intent_acc=1.0)  
**Treatment GRU**: F1=1.0 across all K values  
**Baseline GRU**: 从 K=1 的 0.93 逐步提升至 full 的 1.0（与 seed=42/123 结果一致）

---
