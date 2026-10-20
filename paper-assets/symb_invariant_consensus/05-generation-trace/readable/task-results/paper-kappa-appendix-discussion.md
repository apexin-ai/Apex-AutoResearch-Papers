# paper kappa appendix discussion

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_kappa-appendix-discussion_20260524T112336_result.json`
- **Structured JSON:** [`fcc5b22e7e8de7bf0b62.json`](../../sessions/fc/fcc5b22e7e8de7bf0b62.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits complete. Summary:

### Modified files

**1. `docs/paper/diagnosis.tex`** — two changes:
- **Line 51**: condition count updated from "15 conditions" → "16 conditions"
- **Line 69** (new): added `Qwen3 & PW-D5 & 0.78 & 1.25 & 85.83 & $-$0.17 \\` between Qwen3 FOLIO (κ=0.79) and Qwen2.5-14B FOLIO (κ=0.74), preserving κ-descending sort order

**2. `docs/paper/discussion.tex`** — line 9: inserted one sentence in the ensemble diversity paragraph:
> "The effect is capability-modulated: Qwen3-14B on ProofWriter produces the most redundant non-thinking traces (κ = 0.78, K_eff = 1.25) yet shows negligible Δ (−0.17 pp, n.s.), because its high SC baseline (85.83%) already minimizes correctable errors."

### Consistency checks
- κ range [0.19, 0.82]: 0.78 is within range — **no change needed**
- K_eff range [1.20, 3.94]: 1.25 is within range — **no change needed**
- "$K_{\text{eff}} \leq 1.30$ never improves" claim: K_eff=1.25 with Δ=−0.17 confirms this — **still valid**

### `tab:independence` complete table (post-edit)

| Model | Condition | κ | K_eff | SC (%) | Δ (pp) |
|---|---|---|---|---|---|
| Qwen3 (think) | FOLIO | 0.91 | 1.09 | ~84 | ~0 |
| Qwen2.5-14B | LogiQA | 0.82 | 1.20 | 79.00 | −1.00 |
| Qwen3 | FOLIO | 0.79 | 1.24 | 83.33 | +1.47 |
| **Qwen3** | **PW-D5** | **0.78** | **1.25** | **85.83** | **−0.17** |
| Qwen2.5-14B | FOLIO | 0.74 | 1.31 | 75.98 | −0.49 |
| Qwen2.5-7B | FOLIO | 0.66 | 1.46 | 75.98 | +0.49 |
| Mistral-7B (T=0.3) | FOLIO | 0.53 | 1.77 | 58.33 | −1.47 |
| Mistral-7B (T=0.5) | FOLIO | 0.52 | 1.80 | 58.33 | −0.98 |
| Mistral-7B | LogiQA | 0.51 | 1.81 | 50.00 | +1.50 |
| Mistral-7B (T=1.0) | FOLIO | 0.48 | 1.91 | 55.39 | 0.00 |
| Mistral-7B | FOLIO | 0.46 | 1.98 | 55.88 | +3.43 |
| Mistral-7B (s123) | FOLIO | 0.46 | 1.99 | 54.41 | +2.94 |
| Mistral-7B (s456) | FOLIO | 0.46 | 1.99 | 55.88 | 0.00 |
| Mistral-7B (s789) | FOLIO | 0.45 | 2.03 | 59.31 | −2.45 |
| Mistral-7B (multi-T) | FOLIO | 0.43 | 2.11 | 57.84 | 0.00 |
| Mistral-7B | PW-D5 | 0.19 | 3.94 | 39.33 | **−2.83*** |

---
