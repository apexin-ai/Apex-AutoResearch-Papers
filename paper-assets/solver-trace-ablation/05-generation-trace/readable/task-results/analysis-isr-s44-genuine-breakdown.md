# analysis isr s44 genuine breakdown

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_isr-s44-genuine-breakdown_20260514T154254_result.json`
- **Structured JSON:** [`0d3a41889c7c6f81b201.json`](../../sessions/0d/0d3a41889c7c6f81b201.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
ISR β=0.1 s44:
- Total proved: 89
- H7 (1 premise == conclusion): n=77 (86.5%), mean ISR=0.9260
- H1 (≥2 premises, one == conclusion): n=0 (0.0%), mean ISR=N/A
- Genuine (no premise == conclusion): n=12 (13.5%), mean ISR=0.7500
```

**Caveat：** s44 的 12 个 "genuine" 全部是 n_prems=1（不是真正的多前提推理），premise 与 conclusion 不等是因为 conclusion 多套了一层 `∃x` 量词（例如 premise `∃x (Mary(x) → Advocate(x))`，conclusion `∃x (∃y (Mary(y) → Advocate(y)))`）。这与 s42 的 26 genuine 在性质上可能不同——s42 的 genuine 是否也是同类 1-prem 量词包装？建议核对 s42 的 genuine 是否包含真正多前提样本，再决定能否 mean±std 报告。

数据源：`/root/runs/solver-trace-ablation/plan002-additive-b01-s44-eval.json`（100 problems, 89 proved，使用 `eval_sta.py` 输出的 details.premises/conclusion + ISR）。

---
