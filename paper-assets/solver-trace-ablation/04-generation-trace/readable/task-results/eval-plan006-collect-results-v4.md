# eval plan006 collect results v4

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_plan006-collect-results-v4_20260514T161210_result.json`
- **Structured JSON:** [`4ba703224496860236be.json`](../../sessions/4b/4ba703224496860236be.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 均已完成并更新 registry。汇总：

## Prolog exec-only 3-seed eval 结果 (eval_sta.py full STA)

| Seed | PR | Mean ISR | Proved-only ISR | n_proved |
|------|-----|----------|-----------------|----------|
| s42 | **83%** | 0.031 | 0.037 | 83 |
| s43 | **56%** | 0.008 | 0.015 | 56 |
| s44 | **21%** | 0.081 | 0.387 | 21 |
| **Mean±Std** | **53.3%±31.1%** | **0.040±0.037** | **0.146±0.210** | — |

关键发现：
- PR 跨 seed 极不稳定（std=31pp），与 FOL exec-only 一致
- Mean ISR 始终极低（<0.1），确认 Prolog exec-only 不产生 genuine reasoning traces（参考 C006: 低 ISR = 冗余编码，非无推理）
- s44 异常：PR 最低（21%）但 proved_only_ISR 最高（0.387, max=1.0），可能因少量 proved 样本中有几个碰巧 ISR 较高

---
