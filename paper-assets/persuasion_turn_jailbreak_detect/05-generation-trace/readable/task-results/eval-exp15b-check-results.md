# eval exp15b check results

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_exp15b-check-results_20260519T092026_result.json`
- **Structured JSON:** [`6312edff967b94643a0b.json`](../../sessions/63/6312edff967b94643a0b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp15b 训练成功完成。3 seeds (42/123/456) 的 DAPT + GRU checkpoints 均完整。

## exp15b 结果

### DD OOD (Macro F1, mean±std, 3 seeds)
| Variant | K=1 | K=3 | Full |
|---------|-----|-----|------|
| 9class LR=1e-5 (exp15b) | .899±.066 | .851±.094 | .948±.034 |
| 9class LR=2e-5 (exp15) | .965 | .960 | .987 |
| vanilla (exp15) | .878 | .915 | .927 |

### ActorAttack (Macro F1, mean±std, 3 seeds)
| Variant | K=1 | K=3 | Full |
|---------|-----|-----|------|
| 9class LR=1e-5 (exp15b) | .459±.077 | .676±.077 | .781±.054 |
| 9class LR=2e-5 (exp15) | .718 | .881 | .946 |
| vanilla (exp15) | .977 | .990 | 1.000 |

**结论：LR=1e-5 在两个数据集上均大幅低于 LR=2e-5。** DD OOD Full 从 .987 降到 .948，K=1 从 .965 降到 .899；ActorAttack 更严重，Full 从 .946 降到 .781，K=1 从 .718 降到 .459。降低学习率没有带来改善，LR=2e-5 仍是 9class DAPT 的更优选择。

---
