# eval plan017 additive random s42

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_plan017-additive-random-s42_20260514T051831_result.json`
- **Structured JSON:** [`53217a8c61c171acba13.json`](../../sessions/53/53217a8c61c171acba13.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## plan017-additive-random-s42 Eval 结果

| 指标 | plan017 (additive random) | plan001-s42-r2 (exec-only) | plan013-r4 (random reward) | plan001-s44 (exec-only) |
|------|--------------------------|---------------------------|---------------------------|------------------------|
| prove_rate | **0.48** | 0.93 | 1.00 | 0.98 |
| mean_ISR | **0.0453** | 0.1232 | 0.535 | 0.57 |
| proved_only_ISR | 0.0943 | — | — | — |
| mean_components | **9.56** | 6.58 | ~2 | 2.04 |
| 2-comp ratio | **0%** | — | ~100% | ~100% |
| tautological collapse | **否** | 否 | **是** | **是** |

### 关键发现

**plan017 展示了一个全新的 failure mode**：
- **不是 tautological collapse**（0% 两组件比例，mean components = 9.56）
- 但 **prove rate 大幅下降**（0.48 vs 0.93+），且 ISR 极低（0.0453）
- 33% 的 proved 样本 ISR=0（n_necessary=0），即 conclusion 本身就是 tautology，不依赖任何 premise
- 平均只有 0.85 个 premise 是 necessary（9.56 个 components 中）

### 对 hypothesis 的判断

原假设分三种情况：
- ~~ISR > random > exec-only → signal + regularization 均贡献~~
- ~~ISR > random ≈ exec-only → ISR signal 是关键~~
- ~~ISR ≈ random → ISR 无结构价值~~

**实际结果**：plan017 (additive random) 表现远差于所有 baseline，PR 和 ISR 都最低。Additive random bonus 防止了 2-component 坍缩，但模型转向生成冗长但功能无效的 formalization。**Variance regularization 不仅不能替代 ISR structural signal，反而严重损害了模型性能。**

---
