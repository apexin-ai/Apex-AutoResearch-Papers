# eval plan017 status check

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_plan017-status-check_20260514T052725_result.json`
- **Structured JSON:** [`09a308f855ab2d0fe85c.json`](../../sessions/09/09a308f855ab2d0fe85c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Here's the final analysis:

## plan017-additive-random-s42 评估结果

| 指标 | plan017 (additive random) | plan001-s42-r2 (exec-only) | plan013-r4 (pure random) | plan001-s44 (exec-only) |
|------|:---:|:---:|:---:|:---:|
| **Prove Rate** | 0.48 | 0.93 | 1.00 | 0.98 |
| **Mean ISR** | 0.0453 | 0.1232 | 0.535 | 0.57 |
| **Proved-only ISR** | 0.0943 | 0.1324 | 0.535 | 0.5816 |
| **Mean Components** | 9.56 | 6.58 | ≈2 | 2.04 |
| **2-comp %** | 0% | — | ~100% | 94% |
| **Collapse?** | **No** | **No** | **Yes** | **Yes** |

**核心发现：**

1. **No tautological collapse** — 0% 2-component, mean 9.56 components. Additive random noise prevents the collapse seen in plan013/plan001-s44.

2. **但 PR 和 ISR 都严重下降** — PR=0.48（远低于 exec-only 的 0.93），ISR=0.045（低于 exec-only 的 0.123）。Random noise 破坏了 exec reward signal。

3. **不同的 failure mode** — 模型生成复杂 formalization（9-18 components），但 33% proved 样本 n_necessary=0（conclusion 不依赖任何 premise），说明生成了大量无用 premises。

4. **对假设的回答** — random << exec-only，排除了"variance regularization alone is beneficial"假设。ISR（如果有效）的价值来自结构信号，不是 noise/variance。

Registry 已更新为 DONE/negative。

---
