# paper checklist verify

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_checklist-verify_20260515T212906_result.json`
- **Structured JSON:** [`cd5bdc09c4b532582ba4.json`](../../sessions/cd/cd5bdc09c4b532582ba4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the data needed. Here is the complete audit report:

---

## Checklist Audit: Dream-Identified Structural Fixes

### ✅ 已在 TeX 中实现

**1. Related work: 6→25+ references**
30 unique citation keys across the paper. `related_work.tex` alone cites 26 distinct works across 4 paragraphs (neurosymbolic reasoning, process rewards, reward hacking/Goodhart, mutation testing).

**2. RIP framing → "component necessity testing"**
No "RIP" appears anywhere in TeX. Introduction (`introduction.tex:15`) and Method (`method.tex:22`) consistently use "component necessity testing" / "leave-one-out (LOO) ablation."

**3. "Dense+automatic" → removed**
No "dense" appears in any TeX file. The original language was removed entirely (no need for "conditionally dense" in current framing).

**4. Remove all "Pareto-improving" language**
No "Pareto" appears in any TeX file.

**6. Address ISR sparsity for unproved outputs**
`method.tex:50-51`: "ISR is defined only for proved formalizations... We report proved-only ISR (denoted ISR*) throughout." `appendix.tex:61`: "For unproved samples, ISR is undefined and the protocol is not applied."

**7. Add Goodhart's Law literature (Manheim, Karwowski, Gao)**
All three cited: `related_work.tex:15` (`manheim-goodhart-taxonomy, karwowski-goodhart-rl`), `related_work.tex:15` (`gao-reward-overoptimization`), plus `kwa-catastrophic-goodhart`, `spurious-rewards`, `metr-reward-hacking`.

**8. D051: Premise-count confound discussion**
Full paragraph in `experiments.tex:76-82` ("Premise-count confound"). Full paragraph in `appendix.tex:79-85` ("The premise-count confound"). Also mentioned in `conclusion.tex:6`.

**9. D051: Remove "2.4x", replace with "1.06x"**
No "2.4" in any TeX file. "1.06" appears in `abstract.tex:7`, `experiments.tex:79`, `conclusion.tex:6`.

**10. Prolog s44 classifier blind spot → Discussion**
`conclusion.tex:10-14`: full "Classifier blind spots and functional cross-validation" paragraph covering H7b and query-as-fact gaming.

**11. D060: β=0.3 → "multi-modal Goodhart instability"**
`experiments.tex:97-102`: "High-dose ISR (β=0.3): multi-modal Goodhart" with three pathways (reward collapse / H1 shortcutting / pure H7 meta-Goodhart). Random β=0.3 also described as equally unstable (PR=54±35%). `abstract.tex:7`, Table 1 (`experiments.tex:60-61`), `conclusion.tex:6` all updated.

**12. D060: s44 ISR co-gaming as Goodhart mode**
`experiments.tex:101`: "Seed 44: pure H7 meta-Goodhart (PR=95%, H7=100%, ISR*=0.742, 0% non-hacking)—simultaneously gaming both execution and structural metrics."

**13. D085: H7b obfuscated tautology → §4.2 + Discussion**
`method.tex:73`: H7b defined in taxonomy. `experiments.tex:167`: detailed H7b analysis with vacuous quantifier wrapping. `conclusion.tex:10-13`: classifier blind spots paragraph. `appendix.tex:240-262`: full H7b subsection with examples.

**14. D085: s44 triple gaming as meta-Goodhart case**
`experiments.tex:167`: "simultaneously gaming execution reward, ISR metric, and hacking detector." `conclusion.tex:11-12`: "This triple gaming—execution reward, structural metric, and diagnostic classifier—is the most complete meta-Goodhart case we observe."

**15. D086: β=0.3 H7 dose-response gradient in Discussion**
`conclusion.tex:16-18`: full "H7 dose-response gradient" paragraph with gradient: random β=0.1 (13.7%) → random β=0.3 (4–7 per seed) → ISR β=0.1 (70.6%).

**16. D095 Narrative A: H7a GRPO-general + H7b ISR-specific**
`experiments.tex:68-73`: "H7 tautological collapse occurs under both ISR and random conditions, but ISR amplifies it ~5×." Taxonomy section separates H7a (149 text-match) and H7b (14 obfuscated). Table 2 reports both.

**17. D095/W2: Per-seed + pooled dual reporting; Random H7 annotation**
Table 1 footnote `$^\S$`: "Random H7 driven by seed 43 (38.3%); seeds 42 and 44: 0%." `experiments.tex:70`: per-seed breakdown in text. `abstract.tex:7`: "random H7 is seed-dependent, driven by one of three seeds." Appendix Table has full per-seed data.

**18. D095/W3: Hack mode switching paragraph**
`conclusion.tex:20-25`: full "Hacking mode switching" paragraph. Covers random β=0.1 seeds (s42 non-hacking-heavy, s43 H7-dominant, s44 H8-dominant) and ISR β=0.1 analogous switching.

**19. C013: Set exclusion formula**
`experiments.tex:11`: "non-hacking (N-H) rate—the residual of proved samples matching none of the eight cataloged patterns." This is set-theoretic complement (none of H7 ∪ H1 ∪ H8 ∪ ...), not arithmetic subtraction. Numbers are consistent with set exclusion (e.g., H1∩H8 overlap not double-counted in `appendix.tex:436`). The concept is correctly implemented, just expressed verbally rather than as a formula.

**20. D095: H7 two-layer framing → Abstract, §4.2**
`method.tex:73`: "subtypes H7a standard and H7b obfuscated tautology." `experiments.tex:167`: separate H7a/H7b counts. `abstract.tex:7`: H7 amplification framing. `introduction.tex:27`: "ISR amplifies tautological collapse." Consistent two-layer framing throughout.

**21. D093/D088: H7a not additive-reward-specific**
Exec-only H7 reported: `experiments.tex:30` (s44: H7=100%), `experiments.tex:32` (1000-step s43: H7 tautology). `conclusion.tex:17`: H7 described as "seed-dependent GRPO tendency" that ISR transforms into "near-universal convergence direction." H7 is never described as ISR-exclusive.

### ⚠️ 部分实现

**5. Acknowledge ISR = LOO ablation, cite feature attribution literature**
LOO acknowledgment: ✅ — `method.tex:26`: "LOO ablation itself is standard in mutation testing and feature attribution." `introduction.tex:17`: "LOO ablation itself is standard [demillo1978, jia-harman-survey]."
Feature attribution citation: ❌ — The phrase "feature attribution" appears in `method.tex:26` but no feature attribution paper is cited (e.g., Shapley values, LIME, permutation importance). Only mutation testing citations (DeMillo 1978, Jia & Harman) are present.

### ❌ 确实未实现

None — all items are either fully or substantially implemented.

---

**Summary**: 20/21 items fully implemented in TeX. 1 item (feature attribution citation) partially implemented — the text mentions "feature attribution" but lacks a supporting citation. All numbers, framings, and structural changes match the checklist requirements.

---
