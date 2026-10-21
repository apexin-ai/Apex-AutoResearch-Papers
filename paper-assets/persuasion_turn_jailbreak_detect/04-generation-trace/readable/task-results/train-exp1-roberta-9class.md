# train exp1 roberta 9class

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_exp1-roberta-9class_20260518T100247_result.json`
- **Structured JSON:** [`27fe9476d582b401ddfd.json`](../../sessions/27/27fe9476d582b401ddfd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。RoBERTa-base 9-class 多任务微调 + GRU + DD OOD 评估，3 seeds 结果汇总：

**Stage 1 (RoBERTa 9-class fine-tuning)**

| Seed | Best Epoch | P_Acc | I_Acc |
|------|-----------|-------|-------|
| 42   | 2         | 0.830 | 1.000 |
| 123  | 3         | 0.849 | 1.000 |
| 456  | 3         | 0.842 | 1.000 |

**DD OOD F1 (macro)**

| K    | Mean   | Std    |
|------|--------|--------|
| K=1  | 0.9873 | 0.0119 |
| K=2  | 0.9505 | 0.0284 |
| K=3  | 0.9563 | 0.0189 |
| K=5  | 0.9872 | 0.0090 |
| Full | 0.9936 | 0.0045 |

IID test F1 = 1.0 across all seeds. 所有 Stage 2 GRU 也达到了 val_acc=1.0。

结果已保存到:
- 服务器: `results/exp1_roberta_9class.json`
- 本地 artifact: `exp1_roberta_9class_results.json` (已注册)

---
