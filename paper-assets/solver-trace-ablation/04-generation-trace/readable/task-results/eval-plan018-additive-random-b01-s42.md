# eval plan018 additive random b01 s42

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_plan018-additive-random-b01-s42_20260514T081100_result.json`
- **Structured JSON:** [`9e28ae35a649bd222a5b.json`](../../sessions/9e/9e28ae35a649bd222a5b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## plan018-additive-random-b01-s42 结果总结

**结论：success — ISR 在 β=0.1 下具有结构价值**

### 核心对比

| 实验 | PR | mean_ISR | proved_only_ISR |
|------|-----|----------|-----------------|
| **plan018** random β=0.1 | **0.79** | **0.1038** | **0.1314** |
| plan002 ISR β=0.1 | 0.81 | 0.3365 | 0.4154 |
| plan017 random β=0.3 | 0.48 | 0.0453 | — |
| plan001 exec-only | 0.93 | 0.1232 | — |

### 关键发现

1. **PR 持平** (0.79 vs 0.81, 仅 2pp)：β=0.1 的随机噪声不显著影响证明能力
2. **ISR 差距 3.2 倍** (0.104 vs 0.337)：ISR reward 在低剂量下提供 genuine structural guidance，而非仅仅是 variance regularization
3. plan018 的 ISR (0.104) 接近 exec-only baseline (0.123)，说明 random 控制组的 ISR 仅来自模型自然生成的 proof 结构，ISR reward 将其提升了 3 倍
4. 无 tautological collapse (component_count_2_ratio=0)

---
