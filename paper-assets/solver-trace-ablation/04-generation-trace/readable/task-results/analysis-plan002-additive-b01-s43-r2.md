# analysis plan002 additive b01 s43 r2

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan002-additive-b01-s43-r2_20260515T173259_result.json`
- **Structured JSON:** [`e1caab25c62d0efc8f96.json`](../../sessions/e1/e1caab25c62d0efc8f96.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

## plan002-additive-b01-s43-r2 结果

| 指标 | 值 |
|------|-----|
| eval_prove_rate | 61/100 (61%) |
| eval_mean_isr | 0.5063 |
| proved_only_isr | 0.8301 |
| H7 (tautology) | 61/61 (100%) |
| H1 | 0 |
| H8 | 0 |
| **genuine** | **0/61 (0.0%)** |
| single_premise | 61/61 (100%) |

**Conclusion: negative** — 重训确认了原始 s43 的负面结果，且更差（genuine 从 2→0）。

### ISR β=0.1 三 seed 汇总

| seed | proved | H7 | genuine | genuine_rate | conclusion |
|------|--------|-----|---------|-------------|------------|
| s42 | 61 | 29 | 14 | 23% | success |
| s43-r2 | 61 | 61 | 0 | 0% | negative |
| s44 | 53 | 51 | 2 | 3.8% | negative |

s42 是唯一成功的 seed，s43 和 s44 均完全坍缩为 tautology hacking。种子间 genuine_rate 方差极大（0%~23%）。

---
