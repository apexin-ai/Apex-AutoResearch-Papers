# check n32 and run

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_n32_and_run_20260523T112013_result.json`
- **Structured JSON:** [`cd4e24307076e920d56a.json`](../../sessions/cd/cd4e24307076e920d56a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果：

### N=32 Pretrained FewNERD 分析（32565 instances）

| 指标 | 值 |
|------|-----|
| **Greedy F1** | 0.539 |
| **MV F1** | 0.577 (**MV Δ = +3.9 pp**) |
| **MV Δ 95% CI** | [+2.6, +2.9] pp |
| **Oracle F1** | 0.705 (**Oracle Δ = +16.6 pp**) |
| **Degeneracy %** | 5.4% |
| **Capture %** | 19% |
| **SJ ρ** | 0.456 |
| **LP F1** | 0.529 (Δ = -1.0 pp) |

### N-scaling 对比

| N | Greedy | MV Δ(pp) | Degen% | Oracle Δ | Capture | ρ_SJ |
|---|--------|----------|--------|----------|---------|------|
| 8 | .538 | +3.9 | 11.7 | +11.2 | 36% | .436 |
| 16 | .537 | +4.1 | 7.6 | +14.1 | 29% | .453 |
| **32** | **.539** | **+3.9** | **5.4** | **+16.6** | **19%** | **.456** |

**判定：Scenario A (plateau)** — MV Δ 在 +3.9 pp，N=8→16→32 无显著增长。Degeneracy 从 11.7%→5.4% 持续下降，Oracle headroom 从 +11.2→+16.6 持续增长（更多样本覆盖更多正确答案），但 capture rate 从 36%→19% 持续下降（MV 无法利用这些多样性）。SJ ρ=0.456 基本稳定。

---
