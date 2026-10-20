# eval exp2 actorattack mcnemar

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_exp2-actorattack-mcnemar_20260518T135753_result.json`
- **Structured JSON:** [`645b27a35d543d5661d1.json`](../../sessions/64/645b27a35d543d5661d1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总：

## McNemar Test 结果：9-class vs Vanilla on ActorAttack OOD (118 samples)

| K | Seed | p-value | 9class_right | vanilla_right | total_discord |
|---|------|---------|-------------|---------------|---------------|
| k1 | 42 | 3.4e-10 | 52 | 4 | 56 |
| k1 | 123 | 1.5e-08 | 42 | 3 | 45 |
| k1 | 456 | 9.1e-13 | 53 | 0 | 53 |
| k2 | 42 | 1.9e-13 | 59 | 1 | 60 |
| k2 | 123 | 6.5e-12 | 52 | 1 | 53 |
| k2 | 456 | 4.4e-16 | 68 | 0 | 68 |
| k3 | 42 | 1.1e-16 | 70 | 0 | 70 |
| k3 | 123 | 1.6e-14 | 61 | 0 | 61 |
| k3 | 456 | ~0 | 74 | 0 | 74 |
| k5 | 42 | ~0 | 77 | 0 | 77 |
| k5 | 123 | 1.1e-16 | 71 | 0 | 71 |
| k5 | 456 | ~0 | 77 | 0 | 77 |
| full | 42 | ~0 | 78 | 0 | 78 |
| full | 123 | 1.1e-16 | 72 | 0 | 72 |
| full | 456 | ~0 | 78 | 0 | 78 |

**所有 15 组 McNemar test 均 p<0.001**，方向全部 9class > vanilla。K≥3 时 discordant 样本 100% 偏向 9-class（vanilla_right=0）。

产出文件：
- `results/exp2_actorattack_mcnemar.json` — McNemar 统计结果
- `results/exp2_actorattack_per_sample_preds.json` — per-sample predictions 备查
- Registry `exp2_actorattack_mcnemar` 已更新为 DONE/success

---
