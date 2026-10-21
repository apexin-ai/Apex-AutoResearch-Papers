# paper qwen3 multi seed text update

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_qwen3-multi-seed-text-update_20260524T115709_result.json`
- **Structured JSON:** [`cf6b8eaecee4cf871654.json`](../../sessions/cf/cf6b8eaecee4cf871654.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits are verified. Let me confirm the remaining `−0.17` references are intentionally kept:

- **`experiments.tex:37`** (Table 1 row): Correct — single-seed (seed42) value, consistent with other PW rows; footnote `$^\dagger$` now points to multi-seed appendix
- **`diagnosis.tex:69`** (κ table): Correct — shows single-seed metrics for the seed42 experiment
- **`figures/gen_f2_regime_scatter_v2.py`**: Not modified per task instructions (Fig 2 handled separately)
- **`analysis.tex:133`**: States "$\Delta \leq +1.47$\,pp, n.s." which encompasses both FOLIO (+1.47) and PW (−0.17 or mean +0.92) — still valid

Summary of changes:

| File | Change |
|------|--------|
| `experiments.tex` caption | Added `$^\dagger$\,4-seed replication in Table~\ref{tab:multi-seed}` |
| `experiments.tex` Table 1 | Added `$^\dagger$` to Qwen3-14B PW row |
| `experiments.tex` results prose | Added "four Qwen3-14B seeds yield mean Δ = +0.92 ± 1.14 pp (n.s.)" |
| `discussion.tex` | Replaced "negligible Δ (−0.17 pp, n.s.)" with 4-seed framing tied to K_eff prediction |
| `appendix.tex` | No changes needed — already complete |

---
