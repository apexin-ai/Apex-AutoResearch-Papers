# ops wave2 progress check

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_wave2-progress-check_20260517T103719_result.json`
- **Structured JSON:** [`816ce3e63fd3831d3602.json`](../../sessions/81/816ce3e63fd3831d3602.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both experiments fully evaluated and classified. Here's the summary:

---

## 实验: sweep-isr-b005-s44 (ISR β=0.05, seed 44)
```
训练: ✅ COMPLETE (500/500 steps, runtime=2979s, ~6s/step)
PR: 99/100 (99%)
ISR* (proved-only mean): 0.5539
H7: 86/99 (86.9%) [H7a: 86, H7b: 0]
H1: 0/99 (0.0%)
H8: 10/99 (10.1%)
N-H (non-hacking): 3/99 (3.0%)
genuine count: 3
特殊观察: 极端 H7a tautology collapse — 88.9% 单前提，几乎全是 premise=conclusion 的恒真式
```

## 实验: sweep-random-b005-s43 (Random β=0.05, seed 43)
```
训��: ✅ COMPLETE (500/500 steps, runtime=6998s, ~14s/step)
PR: 62/100 (62%)
ISR* (proved-only mean): 0.0058
H7: 0/62 (0.0%) [H7a: 0, H7b: 0]
H1: 48/62 (77.4%)
H8: 7/62 (11.3%)
N-H (non-hacking): 8/62 (12.9%)
genuine count: 8
特殊观察: ISR≈0 但 hacking 模式不同——无 H7（不是单前提恒真），而是 H1 冗余堆砌（大量前提中包含结论，per-clause ablation 全标 unnecessary）
```

---

## 关键对比 (β=0.05)

| 指标 | ISR β=0.05 s44 | Random ��=0.05 s43 |
|------|----------------|-------------------|
| PR | 99% | 62% |
| ISR* | 0.5539 | 0.0058 |
| H7 | 86.9% | 0.0% |
| H1 | 0.0% | 77.4% |
| H8 | 10.1% | 11.3% |
| Genuine | 3 (3.0%) | 8 (12.9%) |

两种奖励信号在极低 β 下都严重 collapse，但走向不同的 hacking 模式：ISR → H7a 恒真式捷径（高 PR、高 ISR、零推理），Random → H1 冗余前提堆砌（低 PR、ISR≈0、结论嵌套在冗余前提中）。

---
