# Narrative Review: End-to-End Audit

Paper: "When the Most Disruptive Messages Are Predictably Safe to Prune"  
Date: 2026-04-26  
Reviewer scope: logical coherence, consistency, redundancy, claim-evidence alignment, terminology, transitions

---

## Abstract

### 🟡 A1. "ongoing 72B probes" vs. body text with results
**Line**: abstract.tex:1 ("ongoing 72B probes")  
The abstract says "ongoing 72B" but the appendix power analysis body (`appendix_power_72b_body.tex`) already reports N=500 with zero discordant pairs, and `main.tex:39–42` defines macros with concrete 72B values (e.g., `\qwenSevenTwoBDiscordant{0}`). The abstract undersells the result. Update once 72B data is finalized.  
**Fix**: Replace "ongoing 72B probes" with the actual 72B finding.

### 🟢 A2. Dense TOST parenthetical
**Line**: abstract.tex:1 ("oracle p = 0.048, heuristic p = 0.007; 10 seeds each")  
Both p-values are for Qwen only, but a reader could mistake them as covering different backbones. Low risk since the body clarifies.  
**Fix**: Consider "Qwen oracle p = 0.048, Qwen heuristic p = 0.007" if space permits.

---

## Introduction

### 🟡 I1. "15 configurations" implies full factorial but isn't
**Line**: introduction.tex:7 ("three backbone models...three task domains...three communication topologies across 15 configurations")  
The phrasing "three × three × three" implies 27 cells, but only GSM8K uses all three topologies; ARC and StratQA use RR only (3×1×3 + 3×2×1 = 15). Clarified in methodology (§4.5) but the intro misleads.  
**Fix**: Add "(GSM8K under three topologies; ARC, StratQA under round-robin)" inline.

### 🟡 I2. "Cross-generational failure (Qwen3)" appears without setup
**Line**: introduction.tex:14 (Contribution 3)  
Qwen3 has not been mentioned before this line. The reader encounters "cross-generational failure" as a cold reference. The intro paragraph mentions only Qwen, Llama, and Gemma as the three backbones.  
**Fix**: Add one clause earlier (e.g., in the "gap" paragraph or scope statement) noting that generational transfer is tested.

### 🟢 I3. "Predictably" in title overstates the method
**Line**: main.tex:45  
"Predictably safe to prune" implies a predictive framework, but the paper performs retrospective analysis + heuristic detection. The heuristic predicts acks, not safety per se. Minor framing issue.  
**Fix**: Acceptable as-is if the paper's scope statement is clear. Alternatively, "Reliably" might be more precise.

---

## Related Work

### 🟢 R1. Contribution claim embedded in Related Work
**Line**: related_work.tex:10 ("To our knowledge, no prior work has examined whether communication pruning safety is invariant to model scale")  
This "first evidence" claim is a contribution statement better placed in the Introduction, where it already partially appears. Having it in Related Work weakens the rhetorical impact and creates minor redundancy with intro.  
**Fix**: Consider moving to Introduction contributions list or keeping only a gap statement here ("Scale invariance of pruning has not been studied") without the "we provide" clause.

---

## Taxonomy (§3)

### 🟡 T1. Ack example contains task-relevant information
**Line**: taxonomy.tex:20 ("I agree with your solution. The answer is 42.")  
The example acknowledgment explicitly states the answer ("42"). This contradicts the taxonomy definition of "no new content." A reader could reasonably argue this message carries task-relevant information (the final answer). The MATH ack analysis in Appendix D acknowledges exactly this problem for harder domains, but the taxonomy table example itself sets a confusing precedent.  
**Fix**: Use a purer ack example: "Your solution is correct." or "I agree with your calculation."

### 🟢 T2. \label inside \paragraph is non-standard
**Line**: taxonomy.tex:28 (`\label{sec:annotation_protocol}` inside `\paragraph{Annotation protocol.}`)  
`\paragraph` doesn't create a numbered section, so `\label` won't produce a useful reference. Not referenced elsewhere in the paper, so harmless.  
**Fix**: Remove the label or promote to `\subsection` if referencing is needed.

---

## Methodology (§4)

### 🟡 M1. Two different κ values without disambiguation
**Lines**: methodology.tex:4 (κ=0.721), discussion.tex:39 (κ=0.76)  
κ=0.721 is cross-model (LLM-LLM) agreement; κ=0.76 is human-human validation. Both are correct, but the paper doesn't consistently label which is which. The pipeline figure caption uses 0.721 without specifying it's cross-model. A reviewer may see 0.721 and 0.76 and think they contradict.  
**Fix**: Always qualify: "cross-model κ=0.721" vs. "human inter-rater κ=0.76."

### 🟡 M2. Correctness evaluation only mentions GSM8K
**Line**: experiments.tex:1 ("Solution correctness is evaluated by comparing extracted numerical answers against GSM8K ground truth")  
The paper tests on ARC-Challenge (multiple-choice) and StrategyQA (yes/no) as well, but doesn't specify how correctness is evaluated for those domains. Trivial for multiple-choice, but should be stated.  
**Fix**: Add "ARC-Challenge by exact letter match; StrategyQA by yes/no match."

### 🟢 M3. "Informational importance" defined but not used until later
**Line**: methodology.tex:29 (operational definition via bigram novelty, token length, etc.)  
The term is defined in §4.2 but the metrics aren't used until §5.1 (impact gradient) and Appendix C. The gap is expected in a methods-first paper but the list of metrics reads like a forward reference.  
**Fix**: Acceptable as-is; consider a brief parenthetical "(detailed in §5.1)."

---

## Results (§5)

### 🔴 R-1. Missing transition between individual perturbation and aggregate pruning
**Lines**: results.tex:6–16 → results.tex:19–24  
§5.1 (Impact Gradient) shows acks are individually most disruptive. §5.2 (E2E Pruning) immediately shows they're safely removable in aggregate. The paper jumps from "91% high disruption" to "Δ ≈ 0pp" without any bridging text explaining why aggregate behavior might differ from individual perturbation. The resolution (cascade dissolution) is deferred to Discussion (§6). This is the paper's central paradox and the reader is left hanging for two full sections.  
**Fix**: Add a 2-sentence transition at the start of §5.2: "The individual perturbation results suggest acknowledgments should be critical to preserve. The following aggregate pruning tests reveal the opposite — a dissociation we analyze in Section 6."

### 🟡 R-2. "One-directional error channel" introduced without motivation
**Line**: results.tex:24 ("consistent with a one-directional error channel: 0% error correction...")  
The error channel concept appears with data but no prior framing. The reader hasn't been told to expect that acks might inject errors, so "0% error correction but non-zero injection" needs context. The term "error channel" isn't defined anywhere.  
**Fix**: Add a sentence before the data: "Acknowledgments can either correct or propagate errors in downstream reasoning. We find an asymmetric pattern:" Then present the data.

### 🟡 R-3. FG comparison is unfair in suppression rate
**Lines**: results.tex:77 ("FG degrades by −5.0pp while ack-only improves by +1.0pp")  
FG removes ~84–91% of messages vs. ack-only's ~48%. The comparison is confounded by vastly different suppression volumes. The paper notes "Online FG is confounded by cascading suppression (~90% removal)" but only for the online case. The offline comparison (p=0.031) also operates at different suppression rates, which isn't flagged.  
**Fix**: Explicitly state the offline suppression rates in the FG comparison sentence, and note the comparison is at unmatched volumes.

### 🟡 R-4. 72B placeholder macros still in text
**Lines**: results.tex:84–95, discussion.tex:10–16, appendix_scaling.tex:31–71  
Multiple `\qwenSevenTwoBDelta{}` etc. render as "XX.X" or "X.X". The power analysis body already has results (zero discordant, N=500). These need to be reconciled.  
**Fix**: Fill macros from completed experiment data. The `72b_power_macros` input (main.tex:43) should override the default placeholder values.

### 🟡 R-5. "Backbone Communication Typology" section title is opaque
**Line**: results.tex:98 (§5.3 header)  
The term "typology" suggests a classification system, but this section presents ANCOVA/ME results showing that backbone identity determines communication structure. "Backbone Communication Profiles" or "Backbone-Dependent Communication Structure" would be clearer.  
**Fix**: Consider renaming to "Backbone Communication Profiles" for clarity.

---

## Discussion (§6)

### 🟡 D1. Cascade dissolution is presented as a finding but is a hypothesis
**Line**: discussion.tex:1–2 ("We attribute the dissociation to LLM-specific cascade dynamics")  
The paper frames cascade dissolution as an explanation but never directly tests it. The dose-response curve (Appendix E) is consistent with the hypothesis, and the cascade transition probabilities (Appendix A) show sequential dependency. But consistency is not confirmation. The abstract says "we propose that self-reinforcing ack cascades create structural redundancy that dissolves under aggregate removal...requiring causal verification." The Discussion is less cautious.  
**Fix**: In Discussion, use hedging language: "We hypothesize that..." or "The most parsimonious explanation is..." rather than "We attribute."

### 🟡 D2. Dense limitations paragraph covers too many topics
**Lines**: discussion.tex:23–39  
A single paragraph spanning backbone specificity, domain mismatch, stochastic decoding, topology, quantization, single-seed 72B, heuristic transferability, and human evaluation. At 17 lines, this is hard to parse. Key limitations (e.g., "all evaluations measure task accuracy; human judgments are not assessed") are buried at the end.  
**Fix**: Break into 2–3 sub-paragraphs by theme: (1) scope boundaries (backbone/domain/scale), (2) methodological constraints (single-seed 72B, quantization, no human eval), (3) heuristic transferability.

### 🟡 D3. Contingency-B comment bleeds into text
**Line**: discussion.tex:39  
The line `% END CONTINGENCY-B The 5-class taxonomy achieves κ = 0.76...` has text after the comment marker on the same line. Currently the LaTeX renders correctly (comment is to EOL only), but the continuation text ("The 5-class taxonomy...") runs on from a line that starts with a comment, making editing error-prone. The visual layout is confusing.  
**Fix**: Move "The 5-class taxonomy achieves..." to its own line.

### 🔴 D4. "κ = 0.76 (two human annotators, N = 225)" — where is this study reported?
**Line**: discussion.tex:39  
The human validation study is mentioned in Discussion and referenced as "Section 6" in methodology.tex:11. But the actual methodology and results of this study (how annotators were selected, inter-rater protocol, disagreement resolution) never appear in the main text. There is no subsection in Discussion dedicated to it. A reviewer asking "where is the human validation?" would have to hunt through the appendix. The checklist item 15 says "Section 6" but Section 6 doesn't have a clearly labeled paragraph about it.  
**Fix**: Add a dedicated paragraph in Discussion: "Human validation. Two annotators independently classified 225 messages..." with protocol details. Or add a subsection.

---

## Conclusion (§7)

### 🟢 C1. Appropriate brevity
The conclusion accurately summarizes without overclaiming. No issues found.

---

## Cross-Cutting Issues

### 🔴 X1. Terminology inconsistency: "perturbation sensitivity" vs. "perturbation impact" vs. "individual perturbation"
**Locations**:
- methodology.tex:29: "Perturbation sensitivity: 1 − sim_remove(m_i)"
- introduction.tex:3: "perturbation sensitivity"
- results.tex:6: "impact gradient"  
- discussion.tex:1: "perturbation--sensitivity dissociation"
- abstract.tex:1: "perturbation sensitivity"

The paper defines "perturbation sensitivity" formally (§4.2) but uses "impact" and "perturbation" loosely elsewhere. The section heading is "Impact Gradient" (§5.1) but the Discussion calls it "perturbation–sensitivity dissociation." A reader might wonder whether "impact" and "perturbation sensitivity" are the same measure.  
**Fix**: Standardize on "perturbation sensitivity" for the quantity (1-sim) and "impact gradient" for the ordering across types. Use consistently throughout.

### 🟡 X2. Redundant repetition of 10-seed replication numbers
The exact string "Δ=+0.40±1.02pp" or close variants appears in:
- abstract.tex:1
- results.tex:24 (§5.2)
- discussion.tex:5 (§6)
- discussion.tex:9 (scale invariance)
- appendix_statistical.tex:352 (online validation)

Similarly, "non-inferiority at δ=-3pp (p<0.001)" appears 4 times. Some repetition is expected (abstract restates key results) but the Discussion re-quoting identical numbers from Results adds no new information.  
**Fix**: In Discussion, refer to "the 10-seed result (Table 2, §5.2)" rather than re-quoting exact numbers. Save space.

### 🟡 X3. Llama heuristic over-suppression explained 3+ times
The issue of Llama heuristic over-suppression (74.4% vs. ~45% true rate) is explained in:
- results.tex:25–26
- discussion.tex:5
- appendix_statistical.tex:226–300

Each instance partially re-derives the explanation. The appendix coverage is appropriate (detailed evidence), but the main text could point to it rather than repeating.  
**Fix**: In Results, state the finding once with a pointer: "Llama heuristic over-suppresses (74.4% vs. ~45% true ack rate), so Llama equivalence claims use oracle labels (details in Appendix F)."

### 🟡 X4. "Information content" vs. "informational importance" vs. "information-sparse"
**Locations**: 
- methodology.tex:29: "informational importance" (defined)
- results.tex:6: "information content"
- results.tex:17: "information-sparse"
- introduction.tex:3: "informational importance"

The formally defined term is "informational importance," but the paper frequently uses the informal "information content" and "information-sparse." These likely mean the same thing but the inconsistency could confuse a careful reader.  
**Fix**: Use "informational importance" or "information content" consistently; define whichever you choose.

### 🟡 X5. Non-inferiority p<0.001 for Llama is partly driven by improvement, not just harmlessness
**Lines**: abstract.tex:1, results.tex:24  
Llama 10-seed Δ=+2.1±2.4pp yields non-inferiority at δ=-3pp with p<0.001. The strong p-value reflects the positive direction (improvement), not just absence of harm. A reader might interpret "p<0.001" as strong evidence of harmlessness, when it's actually strong evidence that the effect is >-3pp (which it trivially is, since it's positive). This is statistically correct but rhetorically misleading.  
**Fix**: Add a parenthetical: "non-inferiority at δ=-3pp (p<0.001; driven by positive direction)."

### 🟡 X6. 72B "dissociation" is only half-validated
**Lines**: discussion.tex:21 ("individual-message perturbation sensitivity at 72B scale remains unmeasured")  
The paper claims "scale-invariant dissociation" but at 72B only the pruning-safety half is tested. The perturbation-sensitivity half (individual acks are most disruptive) is extrapolated from 7B. The Discussion honestly acknowledges this (line 21), but the abstract and intro don't hedge when referencing scale.  
**Fix**: In the abstract/intro, qualify: "pruning safety is scale-invariant (7B–72B); the full perturbation-sensitivity dissociation is validated at 7B with pruning-only confirmation at larger scales."

---

## Appendices (Quick Scan)

### 🟡 AP1. Appendix A (examples): Llama footnote reveals annotation ambiguity
**Line**: appendix_examples.tex:83  
The Llama "reasoning guidance" example ("I'm glad the solution was accurate...") is acknowledged as resembling an ack. The footnote explains Llama's undifferentiated mode makes annotation difficult. This is honest but undermines confidence in Llama annotations — the reader may wonder how many other Llama messages are similarly ambiguous.  
**Fix**: Acceptable as-is; the paper is transparent. But consider adding a sentence in the main text (§5.3 or §6) referencing this ambiguity.

### 🟢 AP2. Appendix B (HumanEval pilot): Appropriately scoped
Well-flagged as exploratory with explicit statistical limitations.

### 🟢 AP3. Appendix D (MATH): Good qualitative analysis
The MATH ack comparison (16.6 vs. 5.6 tokens) clearly explains why pruning fails in this domain. Strong section.

### 🟡 AP4. Appendix E (scaling): 14B results are confusing
**Lines**: appendix_scaling.tex:22–24  
Two 14B online runs (char_threshold=80 and =30) yield Δ=+3 and +4pp respectively, but only ~6% of messages are suppressed. The text correctly says this tests "partial heuristic coverage rather than a full pruning safety test," but the table (Table 8) lists these alongside the 7B and 72B results without this caveat visible, making cross-scale comparison misleading.  
**Fix**: Add a footnote to Table 8 noting the 14B result reflects partial coverage only.

### 🟡 AP5. Appendix F (statistical): "efficiency_paragraph" input file not checked
**Line**: appendix_efficiency.tex:4 (`\input{sections/efficiency_paragraph}`)  
This file is referenced but I did not verify its existence. If missing, LaTeX will silently skip it or error.  
**Fix**: Verify `sections/efficiency_paragraph.tex` exists and renders correctly.

---

## Priority Summary

| Severity | Count | Key Items |
|----------|-------|-----------|
| 🔴 Must fix | 3 | R-1 (missing transition at paper's core paradox), X1 (terminology inconsistency), D4 (human validation study unreported in main text) |
| 🟡 Should fix | 16 | A1, I1, I2, T1, M1, M2, R-2, R-3, R-4, R-5, D1, D2, D3, X2–X6, AP1, AP4, AP5 |
| 🟢 Optional | 7 | A2, I3, R1, T2, M3, C1, AP2 |

### Top 5 Fixes by Impact

1. **R-1**: Add transition between §5.1 and §5.2 bridging the individual-vs-aggregate paradox. This is the paper's central contribution and the narrative gap is jarring.
2. **D4**: Report the human validation study (κ=0.76, N=225) in a dedicated Discussion paragraph with protocol details. Currently it's a dangling reference.
3. **X1**: Standardize "perturbation sensitivity" terminology throughout. The concept is clear but the vocabulary drifts.
4. **R-4**: Fill all 72B placeholder macros. The data exists in the power analysis.
5. **A1/X6**: Update abstract and intro to reflect finalized 72B results, with appropriate hedging about the partial (pruning-only) nature of 72B validation.
