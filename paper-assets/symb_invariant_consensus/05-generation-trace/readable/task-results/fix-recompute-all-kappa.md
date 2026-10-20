# fix recompute all kappa

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_recompute-all-kappa_20260524T065118_result.json`
- **Structured JSON:** [`a975288fbb1abf74d5dd.json`](../../sessions/a9/a975288fbb1abf74d5dd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits applied and compiled. Summary of changes:

**appendix.tex `tab:independence` (15 rows)** — 8 rows changed κ/K_eff, 7 unchanged:

| Row | Old κ → New κ | Old K_eff → New K_eff | Note |
|-----|----------|----------|------|
| Qwen3 | 0.77 → **0.79** | 1.26 → **1.24** | recomputed |
| Qwen2.5-14B FOLIO | 0.74 → 0.74 | 1.30 → **1.31** | K_eff rounding |
| Mistral-7B FOLIO | 0.50 → **0.46** | 1.84 → **1.98** | unified normalization |
| Mistral-7B s123 | 0.49 → **0.46** | 1.88 → **1.99** | unified normalization |
| Mistral-7B s456 | 0.51 → **0.46** | 1.82 → **1.99** | unified normalization |
| Mistral-7B multi-T | 0.48 → **0.43** | 1.91 → **2.11** | unified normalization |
| Mistral-7B PW-D5 | 0.21 → **0.19** | 3.62 → **3.94** | unified normalization |
| Row order | — | — | reordered by κ desc (T=0.5 moved up, LogiQA moved down) |

**experiments.tex line 50**: κ range 0.21→**0.19** to 0.82; K_eff 3.62→**3.94**; seed κ range [0.45, 0.51]→**[0.45, 0.46]**

**discussion.tex**: K_eff ≤ 3.62 → **3.94**

**appendix.tex** (two additional locations): PW-D5 cross-model table κ 0.21→**0.19**, K_eff 3.62→**3.94**; prose K_eff 3.62→**3.94**

**5 rows not recomputable** (data on decommissioned westd-25068): Qwen3-think, Qwen2.5-7B, T=0.3, T=0.5, T=1.0. Of these, Qwen2.5-7B κ=0.66 is confirmed correct via `fleiss_kappa_batch2.json`. The other 4 retain their old values.

---
