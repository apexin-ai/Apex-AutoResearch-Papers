# train binary seed42 full pipeline

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_binary-seed42-full-pipeline_20260518T124014_result.json`
- **Structured JSON:** [`cc25729e38d4e45dd655.json`](../../sessions/cc/cc25729e38d4e45dd655.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果汇总：

**Stage 1 DeBERTa (seed=42)**: val_persuasion_acc=1.0, val_intent_acc=1.0, best_epoch=4

**binary_seed42 ActorAttack OOD (F1 macro)**:

| K | seed42 | seed123 | seed456 | mean±std |
|---|--------|---------|---------|----------|
| 1 | 0.636 | 0.808 | 0.767 | 0.737±0.074 |
| 2 | 0.800 | 0.917 | 0.953 | 0.890±0.065 |
| 3 | 0.900 | 0.971 | 0.981 | 0.951±0.036 |
| 5 | 0.971 | 0.990 | 1.000 | 0.987±0.012 |
| Full | 0.981 | 0.990 | 1.000 | 0.990±0.008 |

结果已保存至：
- `/root/persuasion_turn_jailbreak_detect/results/exp2_binary_seed42_actorattack.json`（seed42 详细结果 + 3-seed 统计）
- `exp2_actorattack_ood.json` 已同步更新（binary variant 加入 seed42，mean_std 重算为 3-seed）

seed42 的 k1 偏低（0.636 vs 其他两个 0.77-0.81），拉高了 k1 的 std。k3 以上三个 seed 趋于一致。

---
