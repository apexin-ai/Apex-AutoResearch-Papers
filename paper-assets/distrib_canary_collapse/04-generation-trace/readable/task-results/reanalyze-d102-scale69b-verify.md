# reanalyze d102 scale69b verify

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_reanalyze_d102_scale69b_verify_20260519T154954_result.json`
- **Structured JSON:** [`6d9131e25ad7af05c032.json`](../../sessions/6d/6d9131e25ad7af05c032.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

配置已确认是标准的：

- **Canary (2)**: token_entropy, ece
- **Downstream (4)**: distinct_1, distinct_2, distinct_3, mauve
- **共 8 对** — 完全匹配统一 pair 配置，无 perplexity/effective_rank 参与 pair 分析

现有分析指标汇总：

| 指标 | 值 |
|------|-----|
| **PermG fwd** | 7/8 sig (87.5%) |
| **PermG rev** | 0/8 sig |
| **Consensus K≥4** | 6/8 sig (75%) |
| **MMCT detection_rate** | 0.75 |
| **TY Granger** | 4/8 sig |

Consensus K≥4 详情：
- token_entropy→distinct_1: 4 votes (naive, diff, thresh, pg_fwd)
- token_entropy→distinct_2: 5 votes (naive, diff, thresh, pg_fwd, ty)
- token_entropy→distinct_3: 5 votes (naive, diff, thresh, pg_fwd, ty)
- token_entropy→mauve: 3 votes (naive, thresh, ty) — **未达 K≥4**
- ece→distinct_1: 4 votes (naive, diff, thresh, pg_fwd)
- ece→distinct_2: 5+ votes
- ece→distinct_3: 5+ votes
- ece→mauve: 需确认

drift_pct 中虽有 perplexity 和 effective_rank，但这些只是 metrics.json 中计算的漂移量，**未参与 lead-lag pair 分析**。配置标准，无需重跑。

---
