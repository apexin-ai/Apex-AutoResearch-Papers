# analysis a048 s43 5method

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_a048_s43_5method_20260521T072703_result.json`
- **Structured JSON:** [`c1c37db40e10f3a98af2.json`](../../sessions/c1/c1c37db40e10f3a98af2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

| Metric | Value |
|--------|-------|
| PermG_fwd (FDR) | **0/8** |
| PermG_rev (FDR) | 0/8 |
| DiffXCorr_fwd (FDR) | 5/8 |
| DiffXCorr_rev (FDR) | 5/8 |
| Threshold onset (3σ) | 0/8 |
| TY_fwd | 2/8 (C003: 不可引用) |
| **K≥3** | **0/8** |
| **K≥4** | **0/8** |

**Drift**: token_entropy -19%, distinct_1/2/3 -35~48%, ece +835%, perplexity +18%, mauve -16%

**结论**: α=0.48 s43 PermG=0/8，与 s42 完全一致，**blind zone cross-seed confirmed**。Registry 已更新为 DONE/success，artifact 已注册。

---
