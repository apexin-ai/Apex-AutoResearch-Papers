# train plan013 none collapse

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_plan013-none-collapse_20260518T005249_result.json`
- **Structured JSON:** [`79a45a657d11da518c7e.json`](../../sessions/79/79a45a657d11da518c7e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Plan 013 完成 — 结果总结

| K | Binary collapse (plan_013) | 9-class (plan_002) | Baseline (vanilla) |
|---|---|---|---|
| 1 | F1=1.000 | F1=1.000 | F1=0.987 |
| 2 | F1=1.000 | F1=1.000 | F1=0.987 |
| 3 | F1=1.000 | F1=1.000 | F1=0.987 |
| 5 | F1=1.000 | F1=1.000 | F1=1.000 |
| full | F1=1.000 | F1=1.000 | F1=1.000 |

**结论：binary ≈ 8-class**（两者在所有 K 值上完全相同，均为 F1=1.0）。模型本质上是 **persuasion-presence detector**，不依赖细粒度策略区分。8 种策略的额外分类信号对下游 jailbreak detection 没有提供增量价值。

**产出文件：**
- DeBERTa checkpoint: `checkpoints/plan_013_none_collapse/deberta_multitask/best/`
- GRU checkpoint: `checkpoints/plan_013_none_collapse/gru/treatment/best.pt`
- 评估结果: `results/plan_013_none_collapse_eval.json`
- 训练脚本: `src/train_deberta_binary.py`, `src/train_classifier_binary.py`

---
