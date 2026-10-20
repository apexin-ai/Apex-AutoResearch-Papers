# analysis alpha sweep a075 s42 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_alpha_sweep_a075_s42_fp32_20260519T142135_result.json`
- **Structured JSON:** [`411a9389c66fc95934e7.json`](../../sessions/41/411a9389c66fc95934e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。汇总：

## alpha_sweep_a075_s42_fp32 — SUCCESS

**Drift (gen_0→gen_10):**
| Metric | Drift |
|--------|-------|
| token_entropy | −29.4% |
| ECE | +1885% |
| perplexity | +188% |
| distinct_1/2/3 | −25~31% |
| effective_rank | +67.5% |
| mauve | −3.7% (near-flat) |

**Lead-Lag:**
- **PermG: 6/8 fwd, 0/8 rev** — perfect asymmetry
- **K≥4 consensus: 6/8** — 6 pairs with 5/5 unanimous agreement (all canary→distinct-n)
- **MMCT detection: 75%**
- TY Granger: 8/8 (C003 compliant, α=0.75 > 0.50)

**Dose-response:** α=0.75 fits high regime。PermG=75% 略低于预期的 ~83% 但在单 seed 方差范围内。唯二未通过 K≥4 的 pair 都是 →mauve（MAUVE 仅 −3.73% drift，信号不足）。

Registry 已更新为 DONE/success，artifact 已注册 (`art_20260519_7d0a70`)。

---
