# eval plan013 dd crossattack

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_plan013-dd-crossattack_20260518T011543_result.json`
- **Structured JSON:** [`12beef5f884a49d7d4d9.json`](../../sessions/12/12beef5f884a49d7d4d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

评估完成。结果：

## Plan 013 Binary Model DD Cross-Attack Results

| K | Binary (plan_013) | 9-class (plan_006) | Scrambled | Baseline |
|---|---|---|---|---|
| full | 0.9904 | 1.0000 | 0.9809 | 0.2845 |
| 1 | 0.9809 | 1.0000 | 0.9904 | 0.5752 |
| 2 | 0.9809 | 0.9904 | 0.9350 | 0.4381 |
| 3 | 0.9715 | 0.9904 | 0.9350 | 0.3596 |
| 5 | 1.0000 | 1.0000 | 0.9904 | 0.3105 |

**结论**：
- Binary model (plan_013) 在 DD 上 F1 = 0.97-1.0，远超 baseline (0.28-0.58)
- 与 9-class treatment 相比仅有微小差距（~0.01-0.02 lower at K=1-3），K=5 时完美
- Binary 在 K=2,3 时略优于 Scrambled（0.98 vs 0.935）
- Binary collapse 几乎不损失泛化能力，cross-attack 性能依然很强

结果已保存到 `results/plan_013_dd_crossattack_eval.json`。

---
