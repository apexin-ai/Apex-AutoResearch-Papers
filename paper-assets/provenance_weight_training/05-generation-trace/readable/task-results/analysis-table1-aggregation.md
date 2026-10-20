# analysis table1 aggregation

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_table1_aggregation_20260515T123940_result.json`
- **Structured JSON:** [`741076f3f6b7ce97d514.json`](../../sessions/74/741076f3f6b7ce97d514.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 artifact 已生成并注册：

**`table1_data.md`** — 核心结果：
| Method | Mean PPL | ΔPPL | Δ% |
|--------|----------|------|-----|
| Uniform | 17.693 ± 0.006 | — | — |
| Grid b=0.5 | 17.646 ± 0.007 | −0.047 | −0.3% |
| Grid b=1.0 | 17.682 ± 0.009 | −0.011 | −0.1% |
| Grid b=1.5 | 17.710 ± 0.009 | +0.016 | +0.1% |
| Grid b=2.0 | 17.733 ± 0.011 | +0.040 | +0.2% |
| Grid b=3.0 | 17.767 ± 0.010 | +0.074 | +0.4% |
| Grid b=5.0 | 17.811 ± 0.010 | +0.118 | +0.7% |
| Adaptive (n_min=3) | 17.653 ± 0.032 | −0.040 | −0.2% |
| Adaptive-fix (n_min=2) | 17.651 ± 0.009 | −0.042 | −0.2% |

- b=2.0/3.0/5.0 只用 2 seeds（seed456 invalidated, D026）
- ΔPPL 符号：负=优于 uniform

**`experiment_status_summary.md`** — 39 实验，22 success，~96.7 GPU hours（已完成部分）。

---
