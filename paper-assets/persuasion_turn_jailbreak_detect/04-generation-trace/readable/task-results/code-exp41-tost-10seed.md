# code exp41 tost 10seed

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp41_tost_10seed_20260522T033057_result.json`
- **Structured JSON:** [`f2b35edc134476cc7f9c.json`](../../sessions/f2/f2b35edc134476cc7f9c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**exp41_tost_10seed 执行完成。**

| | DD OOD | AA OOD | FITD OOD |
|---|---|---|---|
| TOST p | 2.06e-9 | **0.183** | 0.0 |
| Equivalent? | YES | **NO** | YES |
| Cohen's d | -0.14 | **0.44** | 0.0 |

结论：**negative**。增加到 n=10 seeds 后，AA 上的非等价性更加明显（p 从 0.081 升至 0.183，Cohen's d 从 0.08 升至 0.44 中等效应量）。9-class 在 AA 上比 scrambled 高约 3pp（0.979 vs 0.949），scrambled 方差大（seed314: 0.833）。DD 和 FITD 确认等价。

**解读**：persuasion strategy 标签的具体内容对 ActorAttack OOD 泛化有实际影响——打乱标签会降低且不稳定 AA 性能，说明模型确实利用了策略语义信息来泛化到 AA 攻击。

---
