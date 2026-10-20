# eval plan001 exec only s46 r2

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_plan001-exec-only-s46-r2_20260517T022350_result.json`
- **Structured JSON:** [`d6f666652695bdfb7dbc.json`](../../sessions/d6/d6f666652695bdfb7dbc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

**plan001-exec-only-s46 eval 结果：**

| 指标 | 值 |
|------|-----|
| prove_rate | 93/100 = **93.0%** |
| mean_isr | **0.083** |
| H7 | 0/93 = 0.0% |
| H1 | 83/93 = 89.2% |
| H8 | 4/93 = 4.3% |
| Genuine | 9/93 = **9.7%** |

**跨 seed 对比（exec-only）：**

| Seed | PR | Genuine% |
|------|-----|---------|
| s42 | 90% | — |
| s44 | 93% | — |
| **s46** | **93%** | **9.7%** |

s46 prove_rate 与 s44 一致（93%），符合预期。H1 占 89.2% 说明绝大多数证明是 conclusion-in-premise 模式，Genuine 仅 9.7%，ISR 极低（0.083）——典型 exec-only baseline 行为。

---
