---
dream_id: dream_20260516T021434
tier: best
overall_score: Weak Reject (3/6)
timestamp: 2026-05-16T02:54:47.526264+00:00
---

# R1 Review: OntoCoDec — Methods and Experiments

## 1. Summary

OntoCoDec compiles IE ontology schemas into two composable decoding constraint layers — a grammar layer (XGrammar-based CFG for JSON structure and type vocabulary) and a semantic layer (stateful entity registry with dynamic logit masking for domain/range enforcement) — that compose via bitwise AND with graceful degradation to grammar-only when the intersection is empty. The paper evaluates on SciERC (7 relations) and DocRED (96 relations) across Qwen3-8B and Llama-3.1-8B in zero-shot and LoRA fine-tuned regimes, reporting 90-100% DR elimination in zero-shot and near-complete elimination of residual DR when composed with fine-tuning. The central narrative is that constrained decoding and fine-tuning are orthogonal: fine-tuning improves quality, OntoCoDec guarantees compliance, and neither degrades the other.

## 2. Strengths

- **Well-motivated violation taxonomy.** The four-category violation decomposition (ET, RV, DR, CF) is clean and enables precise ablation. The enabling dependency between grammar and semantic layers is clearly demonstrated through the ablation tables (grammar-only cannot reduce DR; semantic-only cannot eliminate RV/ET; combined achieves both).

- **Grammar surfaces latent violations — a genuine insight.** The finding that grammar-only *increases* DR on DocRED (18.46% to 26.17%) because it forces OOV relations into valid names that then fail domain/range checks is non-obvious and well-explained. This directly motivates the two-layer architecture.

- **Honest CF reporting.** The paper does not hide the CF trade-off (up to 12.02% for Llama DocRED zero-shot). The CF-DR tension analysis (eliminating CF re-routes to +13.85pp DR) is a useful analytical contribution showing the current configuration is near a Pareto front.

- **Cross-model validation without code changes.** Demonstrating that the same compiled constraints work on Qwen3-8B and Llama-3.1-8B with zero code modification is a strong practical argument for the model-agnostic claim.

- **Bootstrap confidence intervals.** Statistical significance is reported for all key comparisons (10,000 iterations), with appropriate hedging (SciERC R-F1 change is non-significant, p=0.58).

- **SciERC composability results are real and convincing.** The 2x2x2 matrix (2 models x zero-shot/FT x unconstrained/constrained) on SciERC shows DR reduction to <=0.09% with R-F1 within +/-0.1pp for both models, with real experimental data backing all four cells.

## 3. Weaknesses

### Critical

- **W1: The central composability claims on DocRED rely on imagined results.** The paper's Tables 1 and 2 (Qwen and Llama DocRED FT+OntoCoDec composability matrices) are the core evidence for the paper's headline claim. However, the experiments `w5_qwen_docred_lora_constrained_eval` and `w5_llama_docred_lora_constrained_eval` are currently still running with no completed results. The numbers in these tables (Qwen FT+OntoCoDec: DR=0.0%, R-F1=40.92; Llama FT+OntoCoDec: DR=0.03%, R-F1=43.68) are imagined/projected values, not measured outcomes. The paper presents these as experimental results without any caveat. This is the most serious issue with the submission as reviewed.

- **W2: The dream-tier narrative is suspiciously optimistic relative to zero-shot patterns.** The imagined FT+constrained DocRED results project CF collapsing to <0.5% for both models, but zero-shot Llama DocRED CF is 12.02%. The SciERC FT pattern does show CF reduction (Qwen 9.90% to 1.18%, Llama 6.56% to 0.46%), but projecting the same pattern to DocRED — where the ontology is 14x larger, tightness is higher, and the zero-shot CF is already much worse — requires justification that is not provided. The paper treats this projection as established fact.

- **W3: Parse failure rates are high and inconsistently handled.** Qwen DocRED FT: 7.01% parse failure (70/998 documents excluded). These documents are excluded from both violation counting and F1 computation, meaning the paper's metrics are computed on a biased subset. The paper does not analyze whether parse-failed documents have systematically different characteristics. At 7%, this is not a negligible exclusion.

### Major

- **W4: No ablation for the FT+constrained regime.** The paper presents a thorough 5-way ablation for zero-shot SciERC and 4-way for zero-shot DocRED, but the composability analysis only reports unconstrained vs. full S1 for FT models. There are no grammar-only or semantic-only ablations for the fine-tuned regime. Do the layers still show the same enabling dependency after fine-tuning, or does the pattern change? The absence of this data means the compositional mechanism is only validated under zero-shot.

- **W5: Only DocRED is evaluated for FT composability; SciERC composability is only in one table.** The dream paper's framing puts DocRED FT composability front and center, but the actual paper under review already has SciERC composability with real data. The disconnect is confusing. The dream paper does not mention SciERC FT composability results at all in its main experimental narrative (it only appears briefly in Section 5.2 of the actual paper). This means the paper's strongest *real* composability evidence (SciERC, 2 models, all cells measured) is buried, while the weakest evidence (DocRED, imagined) is highlighted.

- **W6: No comparison with post-hoc filtering in the FT regime.** The paper argues extensively against post-hoc filtering in zero-shot (48.1% triple discard on DocRED), but does not evaluate post-hoc filtering on FT models where DR is already <1%. In this regime, post-hoc filtering would discard very few triples, potentially making it a strong and much simpler baseline. This comparison is conspicuously absent.

- **W7: Constraint tightness metric needs formal definition.** The paper uses tightness (tau) throughout but defines it only implicitly through examples (SciERC tau-bar=0.75 in some places, 0.333 in others; DocRED tau-bar=0.842 or 0.84). These inconsistencies suggest the metric was computed differently at different points. The formal definition — is it |valid_pairs| / |all_possible_pairs|? — is never explicitly stated.

### Minor

- **W8: Related work section is thin.** The dream paper's related work is approximately 4 paragraphs covering broad categories without specific engagement with individual papers. Only 10 bibliography entries. The paper's own planning documents note a target of 42 bib entries and 20+ related work citations; the dream paper has far fewer.

- **W9: "Prior work" framing for zero-shot results.** Section 5.2 says "Before examining composability with fine-tuning, we briefly summarize zero-shot results that motivate the composability study." This frames the zero-shot experiments as separate prior work, but they are clearly the authors' own experiments from the same project. This framing is misleading — these should be presented as part of the same study with full methodological details.

- **W10: ROI metric is undefined in the dream paper.** The paper summary mentions a "constraint ROI" metric (ROI = delta-DR / delta-R-F1), but this metric does not appear in the dream paper text at all. The ROI is mathematically problematic: when delta-R-F1 is positive (i.e., constraints *improve* F1, as on DocRED), ROI = +infinity, which is meaningless. When delta-R-F1 is zero, it is undefined. The metric only has meaningful values when constraints hurt F1, making it a biased framing device.

## 4. Questions for Authors

1. When will the DocRED FT+constrained experiments complete, and will the paper be updated with real numbers before submission? What is the plan if results differ substantially from projections?

2. The imagined results project CF < 0.5% for FT+constrained DocRED. What is the mechanistic basis for this projection? SciERC has 7 relations and 6 entity types; DocRED has 96 relations and 6 entity types. The combinatorial space is vastly larger. Why should CF collapse equally?

3. Parse failure rate for Qwen DocRED is 7%. Have you analyzed whether excluded documents differ systematically from successfully parsed ones (e.g., document length, relation density)?

4. Why no grammar-only or semantic-only ablation for the FT regime? This would cost minimal additional compute.

5. The tightness metric: is tau(r) = |valid_pairs(r)| / (|entity_types|^2)? The paper uses tau-bar=0.75 and tau-bar=0.333 for SciERC in different locations. Which is correct?

6. Why is post-hoc filtering not evaluated in the FT regime? When FT unconstrained DR is 0.76%, post-hoc filtering would remove approximately 120 triples out of ~16,000 — less than 1% of output — making the "48% discard" argument from zero-shot inapplicable.

## 5. Method Assessment

**Two-layer composition:** Well-motivated by the formal distinction between vocabulary constraints (CFG-expressible) and semantic constraints (context-sensitive, requiring state). The enabling dependency is empirically demonstrated. The graceful degradation to grammar-only when intersection is empty is a sensible design choice. However, the fallback mechanism is also the primary source of residual DR on DocRED (10.21% correlating with 10.2% fallback rate), raising the question of whether a more sophisticated intersection strategy could reduce residual violations.

**Constraint tightness metric:** Potentially useful but under-developed. The dual-factor hypothesis (tightness x baseline RV) is interesting but only supported by 4 data points (2 models x 2 datasets). The metric's formal definition is inconsistent across the paper. As a predictive tool, it currently lacks sufficient validation.

**ROI framework:** Not present in the reviewed paper. Based on the summary description, it is mathematically ill-conditioned (undefined or degenerate when delta-F1 >= 0, which is the case for most configurations). Not recommended as a contribution.

## 6. Experiment Assessment

**What is sufficient and real:**
- Zero-shot 2x2 matrix (2 models x 2 datasets): all 8 experiments (4 unconstrained + 4 constrained) are completed with real data. This is solid.
- SciERC composability (2 models x 2 settings x 2 constraint configs): all cells are real. This demonstrates the composability claim on a small, tightly-constrained ontology.
- SciERC 5-way ablation (Qwen zero-shot): real and informative.
- DocRED 4-way ablation (Qwen zero-shot): real and informative.
- Bootstrap CIs: properly reported for all real experiments.

**What is missing or problematic:**
- DocRED FT+constrained (both models): **imagined results presented as real**. This is the paper's centerpiece and it does not exist yet.
- FT regime ablations (grammar-only, semantic-only on FT models): absent entirely.
- Post-hoc filtering baseline on FT models: absent.
- DocRED FT composability for SciERC with additional datasets beyond the 2 used: acknowledged as a limitation but worth noting the paper's claims about "model-agnostic" applicability rest on a narrow base.
- Variance/reproducibility: no mention of running experiments multiple times with different seeds. All numbers are single-run.
- Latency/throughput overhead: the paper mentions a runtime section but the dream paper does not include it. For a practical method, this is important.
- The 12% parse failure rate issue (zero-shot Qwen DocRED or zero-shot Llama DocRED constrained at 9.1%) is insufficiently analyzed.

**Are baselines adequate?**
The zero-shot comparison (unconstrained vs. constrained) is the right design. The 5-way ablation is good. However, the absence of post-hoc filtering in the FT regime and the absence of any other constrained decoding method (e.g., type-constrained beam search, or even simple rejection sampling) makes it hard to assess whether the proposed approach is *better* than alternatives or merely the *first* to be tried in this setting.

## 7. Score and Confidence

**Score: 3 (Weak Reject)**

**Confidence: 4 (High — I have examined the experimental artifacts, project logs, and paper drafts in detail)**

## 8. Key Concerns That Would Change My Score

**Would move score UP to 4 (Weak Accept):**
- Real DocRED FT+constrained results that match the projected numbers (DR near 0%, R-F1 within +/-0.5pp, CF < 2%). If results are close to projections, this would validate the composability claim on a complex ontology.
- Post-hoc filtering baseline on FT models, showing that OntoCoDec provides meaningful advantage even when post-hoc is cheap.
- FT regime ablation (grammar-only, semantic-only) showing the enabling dependency persists.
- Formal definition and consistent usage of the tightness metric.

**Would move score UP to 5 (Accept):**
- All of the above, PLUS: a third dataset (preferably biomedical) demonstrating generalization beyond scientific/Wikipedia domains.
- Latency overhead analysis showing practical deployability.
- Multiple-seed variance reporting.

**Would move score DOWN to 2 (Reject):**
- If the real DocRED FT+constrained results show materially different patterns from projections — e.g., CF remains elevated (>5%), or R-F1 drops >1pp, or DR residual is substantial (>2%). The paper's entire narrative around "orthogonal composition" and "CF collapse" would need to be rewritten.
- If parse failure rates increase substantially under FT+constrained (the 12% PF rate mentioned in the summary for FT+constrained Qwen is already concerning — the dream paper projects 7.01% which is lower, but this number is imagined).

---

**Bottom line:** The paper has a clean method design and solid zero-shot experimental results, but its central composability claim on DocRED — the paper's stated main contribution — rests on experiments that have not yet completed. The dream-tier projections are plausible extrapolations from SciERC patterns but are not data. Until the experiments finish and real numbers replace the imagined ones, the paper cannot be accepted. The SciERC composability results alone, while real and convincing, are insufficient to support the broad claims made in the abstract and conclusion.
