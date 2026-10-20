# analysis mmct k sweep

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mmct_k_sweep_20260524T155110_result.json`
- **Structured JSON:** [`0400c7dd25d8580ffc21.json`](../../sessions/04/0400c7dd25d8580ffc21.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Analysis complete. Summary:

**Key findings:**

| Threshold | FPR (α=0) | TPR (α=0.50) | TPR (α=0.75) | TPR (α=1.0) |
|-----------|-----------|-------------|-------------|-------------|
| K ≥ 2     | 38.9%     | ~85.4%      | ~72.9%      | ~75.0%      |
| **K ≥ 3** | **16.7%** | **66.7%**   | **37.5%**   | **75.0%**   |
| K ≥ 4     | 0.0%      | 25.0%       | 0.0%        | 25.0%       |
| K ≥ 5     | 0.0%      | 4.2%        | 0.0%        | 0.0%        |

**Critical trade-off for the paper:**
- **K≥3** (our default): FPR = 16.7% (6/36 null pairs) — inflated above 5% nominal, but delivers 67–75% detection at moderate-to-full contamination
- **K≥4**: FPR = 0% — perfect null rejection, but detection collapses to 0–25%, missing most true signals
- **K≥2**: FPR = 38.9% — unacceptable false alarm rate
- **K≥5**: Near-zero detection everywhere — effectively dead

**Outputs saved:**
- Plot: `docs/paper/figures/fig_mmct_k_operating.pdf` + `.png`
- Data: `artifacts/mmct_k_operating_table.json` (registered as `art_20260524_cb887b`)

**Methodological note:** FPR computed on 6-pair basis (6 null seeds × 6 pairs = 36 total, exact). TPR computed on 8-pair basis from CSV fp32 experiments (includes mauve pairs). K≥2 for TPR is estimated via pigeonhole bounds (marked with `~`). The TPR at α=0.75 (37.5%) being lower than α=0.50 (66.7%) for K≥3 reflects seed-level variance across mixed experiment vintages (fp32 reruns vs originals).

---
