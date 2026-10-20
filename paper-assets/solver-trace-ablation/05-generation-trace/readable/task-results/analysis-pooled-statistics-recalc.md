# analysis pooled statistics recalc

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_pooled-statistics-recalc_20260515T192941_result.json`
- **Structured JSON:** [`b3c17f39a42e972334bc.json`](../../sessions/b3/b3c17f39a42e972334bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总报告：

---

## Pooled Statistics — ISR β=0.1 vs Random β=0.1 (FINAL)

### Genuine rate
- **ISR**: 14/231 = **6.06%** [Wilson 95% CI: 3.64–9.91%]
- **Random**: 25/262 = **9.54%** [Wilson 95% CI: 6.55–13.71%]
- **Fisher exact**: OR=0.61, **p=0.182 (n.s.)**, ISR < Random
- **Bootstrap diff**: −4.44pp [−17.44%, +8.57%] — 跨零，无显著差异

### H7 rate
- **ISR**: 163/231 = **70.56%** [Wilson 95% CI: 64.39–76.07%]
- **Random**: 36/262 = **13.74%** [Wilson 95% CI: 10.09–18.44%]
- **Fisher exact**: OR=15.05, **p=1.33×10⁻³⁹ (\*\*\*)**
- **Bootstrap diff**: +59.25pp [+5.74%, +100.00%]

### Per-seed genuine rates
| | s42 | s43 | s44 | Mean±SD |
|--|--|--|--|--|
| ISR | 17.28% | 0% | 0% | 5.76±9.98% |
| Random | 22.78% | 1.06% | 6.74% | 10.20±11.27% |

### H7b specificity
ISR=2, Random=0, Exec-only=0 — H7b 仍为 ISR-specific。

### Claim 2 结论
ISR reward 不提升 genuine reasoning（6.06% vs 9.54%, p=0.18），但将 H7 tautological gaming 放大 5.1 倍（70.56% vs 13.74%, p<10⁻³⁹）。ISR 信号是 Goodhart 效应放大器，非 reasoning 改善器。

---

JSON 已保存至 `westd-39279:/root/solver-trace-ablation/outputs/pooled_statistics_2026-05-15.json`，memory.md 已更新（DEPRECATED 部分已替换为 FINAL 数据），artifact 已注册。

---
