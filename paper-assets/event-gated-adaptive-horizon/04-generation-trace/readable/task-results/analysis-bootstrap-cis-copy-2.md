# analysis bootstrap cis

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bootstrap_cis_20260516T184812_result.json`
- **Structured JSON:** [`21a1eec2f70bac104c9c.json`](../../sessions/21/21a1eec2f70bac104c9c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

**NVE Peak CIs (35K+ window, 10000 bootstraps):**

| Condition | Mean | 95% CI | n |
|-----------|------|--------|---|
| no_dt_emb | 1.06× | [0.97, 1.14] | 2 |
| trained_dt_emb | 3.29× | [1.62, 4.13] | 3* |
| SGS_full (018v2) | 1.66× | — | 1 |
| Cheetah cross-env | 8.65× | — | 1 |
| SGS_partial (016e) | 10.42× | — | 1 |
| dt1_imag | 2.36× | [0.94, 3.78] | 2 |

*trained_dt_emb 注：008d/009e 共享前 55K 数据（NVE peak 在 55K），有效独立 n=2。

**Collapse Rate CIs:**

| Condition | Rate | 95% CI | n |
|-----------|------|--------|---|
| no_dt_emb | 0% | [0, 0] | 2 |
| trained_dt_emb | 67% | [0, 100%] | 3 |
| All CIVO conditions (pooled) | 71% | [43%, 100%] | 7 |
| All control conditions (pooled) | 0% | [0, 0] | 3 |

**Effect Size:**
- trained_dt_emb − no_dt_emb NVE: Δ = +2.24, CI [+0.56, +3.16]（排除 0，显著）

输出文件：`artifacts/bootstrap_cis.json`，已注册 (`art_20260516_8db708`)。

---
