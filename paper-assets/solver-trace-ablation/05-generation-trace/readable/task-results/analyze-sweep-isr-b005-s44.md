# analyze sweep isr b005 s44

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_sweep-isr-b005-s44_20260517T104953_result.json`
- **Structured JSON:** [`2b8a548f78d313edaac3.json`](../../sessions/2b/2b8a548f78d313edaac3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Here's the summary:

## sweep-isr-b005-s44 分析结果

**结论: negative** — 严重 H7 collapse，与 s42/s43 一致。

| 指标 | 值 |
|------|-----|
| prove_rate | 99.0% (99/100) |
| H7 tautology rate | **86.9%** (86/99) |
| H8 degenerate | 2.0% (2/99) |
| H1_exact | 1.0% (1/99) |
| **genuine_rate** | **10.1%** (10/99) |
| mean ISR (proved) | 0.554 |
| median ISR | 0.500 |

**三 seed 对比 (β=0.05 ISR bonus):**

| seed | H7 rate | genuine rate |
|------|---------|-------------|
| s42 | 100% | 0% |
| s43 | 97% | ~3% |
| s44 | 86.9% | 10.1% |

β=0.05 ISR additive bonus 在全部 3 个 seed 上均产生严重 H7 collapse。模型学会了生成 P→P tautology（单一前提 = 结论）来同时最大化 execution reward 和 ISR bonus，训练后期 entropy 接近 0、reward_std=0（完全 mode collapse）。

---
