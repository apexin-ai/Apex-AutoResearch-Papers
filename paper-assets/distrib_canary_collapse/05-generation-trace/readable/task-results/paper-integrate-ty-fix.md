# paper integrate ty fix

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_integrate_ty_fix_20260516T002030_result.json`
- **Structured JSON:** [`3cbc1db46a307ac6446a.json`](../../sessions/3c/3cbc1db46a307ac6446a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Edit confirmed. Now let me verify consistency with paper_framing.md constraints.

## Summary of analysis

**Modified files:**
- `docs/paper/discussion.tex` line 31 — Replaced incorrect claim that TY returns `insufficient_df` for all pairs at T≤7 with the corrected window sensitivity results (TY produces valid statistics at all T∈{5,...,10}, 3/6 to 6/6 pairs significant).

**No changes needed in the following (verified):**

| Item | Location | Why unchanged |
|------|----------|--------------|
| TY 4/16 (25%) | experiments.tex:54, method.tex:15, intro:24 | From method_ablation.py (canonical impl), not window_sensitivity |
| TY 59.4% at α=1.0 | experiments.tex:97 (method_comparison table) | Same — canonical impl |
| TY FNR 33.3% (2/6) | experiments.tex:178, method.tex:103, discussion.tex:27 | Still correct: ECE→d2 and ECE→d3 still miss at 3/4 seed threshold (2/4 seeds) even with the fix |
| TY FNR 25% in FPR/FNR table | experiments.tex:196 | Correct (33.3%) |
| Tier 4 FNR 50% | method.tex:67,81 | Still correct: ECE→d1 at 3/4 seeds still fails 4/4 |
| 4/5 consensus = 6/6 robust | discussion.tex:30, experiments passim | Confirmed unchanged: fix report Table 2 shows 6/6 robust at every T∈{5,...,10} |
| Spurious-signal rate 75%/62.5% | experiments.tex:56, method.tex:16 | Unaffected — based on pair-level method_ablation results |
| ECE "conditional secondary" | experiments.tex:150-153 | Still correct: TY Type II errors still drive the "secondary" label |

**Consistency with paper_framing.md:**
- Constraint #15 (TY 降级为辅助指标): ✓ No claim strength change
- Constraint #8 (TY 在 N=11 下不可靠): ✓ Narrative preserved — "limited residual degrees of freedom"
- Constraint #11 (统计效力须显式论证): ✓ The updated line still explicitly acknowledges TY's power limitation

**Pre-existing issue flagged (not related to this fix):** `artifacts/_project/paper/experiments.tex:173,191` reports TY FNR as 25% instead of 33.3% (inconsistent with its own discussion.tex:27 and with the `docs/paper/` version). This predates the window_sensitivity fix.

---
