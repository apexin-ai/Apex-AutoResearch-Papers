# analysis alpha sweep a000 s44

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_alpha_sweep_a000_s44_20260516T185105_result.json`
- **Structured JSON:** [`4f850d9afa5788ef2387.json`](../../sessions/4f/4f850d9afa5788ef2387.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。`alpha_sweep_a000_s44` 分析结果：

**FPR 控制：成功** — 所有检测方法在 null 条件下均不产生 false positive。

| 指标 | Perm Granger FDR | TY Granger | Robust pairs (≥3/5) |
|------|-----------------|-----------|---------------------|
| 显著数 | 0/8 | 0/8 | 0/8 |

**Drift (gen0→gen10)**:
| Metric | gen0 | gen10 | drift% |
|--------|------|-------|--------|
| token_entropy | 3.234 | 3.096 | -4.3% |
| perplexity | 26.95 | 21.62 | -19.8% |
| distinct_1 | 0.098 | 0.084 | -14.6% |
| effective_rank | 46.61 | 44.50 | -4.5% |

与 s43 高度一致，drift 模式相同（自然漂移，无合成污染信号）。Registry 已更新为 DONE/success，artifacts 已注册。

---
