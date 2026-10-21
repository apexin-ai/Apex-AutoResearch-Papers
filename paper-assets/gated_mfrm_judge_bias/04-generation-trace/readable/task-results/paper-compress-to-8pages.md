# paper compress to 8pages

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_compress-to-8pages_20260525T080852_result.json`
- **Structured JSON:** [`7d0d8c1ab1370bddffa4.json`](../../sessions/7d/7d0d8c1ab1370bddffa4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Sections layout:
- Page 1: Abstract, Introduction (starts ~43%)
- Page 2: Introduction cont., Related Work (starts ~56%)
- Page 3: Confounding/Background (starts ~37%)
- Page 4: G-MFRM Method (starts ~62%)
- Page 5-6: Method cont. (Identifiability, Error Propagation)
- Page 6-7: Experiments (starts ~93% of p6)
- Page 8: Experiments cont., Conclusion (~55%), Limitations (~69%)
- Page 9: Limitations cont., References (~23%)
- Pages 10+: References cont., Appendix

---

**Summary:**

**Final page count:** Main text (Abstract through Conclusion) = ~7.6 pages (Conclusion ends near top of page 8 at ~69%). Total PDF = 17 pages.

**Section layout (approximate):**
| Section | Pages |
|---------|-------|
| Abstract + Introduction | ~1.5 |
| Related Work | ~0.8 |
| Background (Confounding) | ~1.3 |
| Method (G-MFRM) | ~2.0 |
| Experiments | ~1.7 |
| Conclusion | ~0.3 |

**Content moved to appendix:**
- Proposition 1 and 2 proofs → new `\ref{app:prop_proofs}` section in appendix

**Compressed in place (not moved):**
- experiments.tex: Main results paragraph (deleted discretization artifact discussion, structural confounding cross-reference, CyclicJudge+discard interpretation), convergence diagnostics (compressed to 1 sentence), contamination/prior robustness/judge count details (1 sentence each), error propagation subsection (3 sentences), predictive fit/ranking accuracy paragraphs
- method.tex: DG-IRT comparison (2 sentences), Stage 2 exposure (removed LogProber sentence, merged non-circularity), Theorem 1 explanation, error propagation numerical details, Murphy-Topel paragraph
- background.tex: Last two paragraphs (linear approximation caveat + sequential estimation failure) merged and compressed
- related_work.tex: All three paragraphs compressed, detailed per-citation descriptions → grouped citations

**N=17 data filled in:** Raw Average, CyclicJudge, CyclicJudge+discard, DCR Factor, Pref. Leakage columns populated. MFRM-only/Sequential/G-MFRM remain TBD (awaiting MCMC).

**LaTeX warnings:** No undefined references. Only benign `h→ht` float specifier changes in appendix.

---
