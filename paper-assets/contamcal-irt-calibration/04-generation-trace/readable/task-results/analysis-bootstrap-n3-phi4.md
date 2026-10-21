# analysis bootstrap n3 phi4

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bootstrap-n3-phi4_20260520T165116_result.json`
- **Structured JSON:** [`de1f6718ad5dcc180493.json`](../../sessions/de/de1f6718ad5dcc180493.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Bootstrap 完成。Phi-4 升级到 n=3 的关键变化：

### Phi-4 n=2 → n=3 变化

| 指标 | n=2 (旧) | n=3 (新) |
|------|----------|----------|
| CI 方法 | t-distribution (df=1) | BCa bootstrap (10k) |
| Δ(d100) mean | — | **+0.72pp** |
| 95% CI | 极宽 (t, df=1) | **[-0.17, +1.39]** (很窄) |
| Pattern | — | Immune†（不一致：s42=Immune, s123=Benefit-sat, s0=Immune） |
| Direction | — | 0 (均值+0.72 < 1pp threshold) |
| Dir-Con | — | ✗（s123 方向与 s42/s0 不同） |
| ρ_mean | — | 0.31（低稳定性） |

### 全局概览（5 家族）

- **Phi-4** (n=3): +0.72pp [-0.17,+1.39] — CI 不含 0（p=0.039），但效应小，方向分类为 Immune
- **OLMo-2-7B** (n=3): +1.35pp [-0.55,+2.60] — 也升到了 BCa，CI 含 0
- **Qwen14B/7B/Gemma** (n=2): 仍用 t-distribution，CI 极宽，信息量有限

LaTeX 表已写入 `analysis/bootstrap_table.tex`，文本结果在 `analysis/bootstrap_results.txt`。

---
