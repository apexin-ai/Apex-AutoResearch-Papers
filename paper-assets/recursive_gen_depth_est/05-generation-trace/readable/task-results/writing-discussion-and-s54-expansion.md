# writing discussion and s54 expansion

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_discussion-and-s54-expansion_20260515T200231_result.json`
- **Structured JSON:** [`65bbeb3a2b27b36830b8.json`](../../sessions/65/65bbeb3a2b27b36830b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

No other files reference `sec:discussion` or `sec:conclusion` — labels are clean.

Summary of changes:

**`discussion.tex`** — expanded from 2 lines to full §6 Discussion + §7 Conclusion (~450 words):
- §6.1 Implications: depth-graduated curation (cites dsir2023, qurating2024, sugiyama2007), feature evolution tracking collapse dynamics (cites shumailov2024_nature, marchi2024_heat_death), provenance toolkit positioning (cites kirchenbauer2023_watermark, uchendu2020_attribution)
- §7 Conclusion: task definition summary, dual-layer signal structure, key numbers (69.6–85.4%, EDD=4, cross-model 66.4%, cross-strategy 59.1%), future work (wild-data, 7B+, cross-domain, cites pudasaini2026_detection_fails)

**`generalization.tex` §5.4** — enhanced with:
- Table 6 (`tab:e2e_detail`): per-backbone F1 breakdown (DeBERTa 58.3%±4.7, RoBERTa 59.5%±3.2, RF d2 recall 0.596)
- "Feature space divergence" paragraph: negative Spearman correlations (DeBERTa ρ=−0.484, RoBERTa ρ=−0.456), zero top-5 overlap, both backbones converge to same anti-correlated subspace
- Fixed `\textsc` → `\texttt` for feature names

**`conclusion.tex`** — unchanged; already covers all 5 required Limitations points (cross-strategy constraint, controlled setting, reference model circularity, feature domain fragility via Pudasaini, EDD monotonicity via Bakshi).

---
