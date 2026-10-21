---
dream_id: dream_20260522T052642
tier: worst
overall_score: 2.5 - Borderline Findings
timestamp: 2026-05-22T06:49:00.642535+00:00
---

# Dream Review Report: "How Do LLMs Violate Ontology Constraints? A Systematic Study with Mitigation"

**Review Mode:** Full (2 Reviewers, 4-Step Roundtable)
**Target Venue:** EMNLP 2026 (ARR October cycle)
**Reviewers:** R1 (Methods + Experiments), R2 (Novelty + Related Work)

---

## Consolidated Scores

| Dimension | R1 | R2 | Final |
|-----------|----|----|-------|
| Soundness | 3.0 | — | 3.0 |
| Excitement | 2.0 | 2.5 | 2.0 |
| Novelty | — | 3.0 | 2.5 |
| Reproducibility | 3.0 | — | 3.0 |
| Related Work | — | 2.0 | 2.0 |
| **Overall** | **2.5** | **3.0** | **2.5** |

**Overall Assessment: 2.5/5 — Borderline Findings**

---

## R1 Review: Methods and Experiments

### Soundness: 3.0/5

The violation taxonomy is well-defined and the five categories (ET, RV/EV, RoV, DR/AC, CF) follow logically from ontology constraint types. The decidability classification (local, prefix-decidable, non-local) adds useful theoretical grounding. However, several experimental rigor concerns reduce confidence:

(1) **Predicted data mixed with actual data.** Table 4 (grammar-only ablation) presents Qwen and Llama results marked "(predicted)" alongside actual Mistral data, yet the paper discusses these as findings without adequate caveat. Tables 9-10 (70B LoRA) mark entries as "(pred.)" but the main text Finding 8 draws strong conclusions ("does not generalize reliably to quantized large models") partly from predicted data. This is a significant transparency issue — readers may not register the "(pred.)" notation, and findings should not be anchored on predictions.

(2) **Incomplete statistical testing.** Bootstrap CIs are provided for EE (Table 11) but not for RE, despite RE being the primary task where constrained decoding claims positive F1 impact. The DocRED R-F1 delta of +0.50pp (Qwen-8B) and +0.29pp (Llama-8B) are presented without significance testing.

(3) **DocRED 70B LoRA uses only 200 documents** (of 998) without justification for the subset selection or analysis of whether this is representative.

(4) **Missing control:** No 8B FT RE constrained results are shown — only EE FT (Table 8) and 70B LoRA RE (Tables 9-10). The FT RE story for 8B models is absent from the paper.

### Excitement: 2.0/5

The key empirical findings are largely confirmatory rather than surprising: (a) LLMs violate ontology constraints — practitioners already know this; (b) prompt-based mitigation is unreliable — this is the motivating premise of the entire constrained decoding literature; (c) grammar can't do semantic constraints — trivially expected (a CFG cannot condition on dynamically determined state); (d) larger models are more compliant but not perfect — consistent with general scaling literature.

The most interesting finding — that post-hoc filtering beats constrained decoding in 5/6 ZS RE configs — actually undermines the paper's own method. The paper handles this transparently, which is commendable, but the practical implication is that OntoCoDec is not the right tool for the majority evaluation setting (ZS RE).

### Reproducibility: 3.0/5

The paper claims to release a "violation analysis toolkit and constraint compiler" but provides no URL or anonymous repository link. The method description (Section 4) is conceptually clear but lacks implementation details: XGrammar integration specifics, logit masking implementation, fallback threshold, entity registry data structure. Prompts and LoRA hyperparameters are not provided. The 10-page format is tight, but an appendix with these details would be expected.

### Strengths

- **[S1] Comprehensive evaluation matrix.** 3 datasets × 5 models × multiple configurations (unconstrained, grammar-only, full constrained, post-hoc, FT) with cross-scale analysis (8B vs 70B). This breadth is genuinely above average for the subfield.
- **[S2] Honest reporting of negative results.** Post-hoc beating constrained decoding in 5/6 ZS RE configs, CF trade-off (3.7-21.1%), Trigger-F1 degradation in FT EE, 70B LoRA failures — all reported transparently with mechanistic explanations.
- **[S3] The grammar-only ablation (Table 5) demonstrates enabling dependency.** The three-way comparison (unconstrained → grammar-only → full S1) cleanly shows that grammar eliminates vocabulary violations while surfacing latent semantic violations, providing empirical justification for the two-layer architecture.
- **[S4] Post-hoc filtering analysis for EE (Table 2).** The 99.6-100% discard rate is a striking result that clearly demonstrates post-hoc is non-viable for event extraction — a useful empirical contribution.

### Weaknesses

- **[W1] No significant improvement on any semantically meaningful metric in EE.** Bootstrap testing (Table 11) shows Trigger-F1 and Arg-F1 improvements are not significant across all three models. Entity-F1 is significant but is explicitly format compliance recovery (0%→11-17%), not semantic extraction improvement. The paper's own statistical analysis demonstrates OntoCoDec does not improve extraction quality in EE.
- **[W2] Post-hoc filtering superiority in ZS RE (Table 3) undermines the method's practical value.** In the setting that constitutes roughly 60% of the evaluation (6 ZS RE configs), a trivial post-hoc baseline outperforms OntoCoDec on the metric that matters (R-F1). The paper's counter-arguments (information coverage, FT regime, EE) are valid but narrow.
- **[W3] CF trade-off is severe and incompletely analyzed.** CF=3.7-21.1% across configurations means the method introduces a new violation category while eliminating others. The error analysis (Section 5.9, 15 cases) is qualitative and small-scale. The paper frames CF as "inherent to per-relation enforcement" — but this means the method has a fundamental architectural limitation that is not resolved.
- **[W4] Predicted/incomplete data presented as findings.** Grammar-only results for Qwen and Llama (Table 4) are predicted, not experimental. 70B LoRA results (Tables 9-10) are partially predicted. The paper draws strong conclusions (Finding 8) from these predicted results. This is below the evidential standard expected for EMNLP.
- **[W5] Near-zero F1 baselines.** ZS RE R-F1 ranges from 2.54% to 11.24%; ZS EE Trigger-F1 ranges from 2.4% to 11.8%, Arg-F1 ≈ 0%. Improvements of +0.3-0.5pp on sub-10% F1 are within noise regardless of statistical significance. The practical interpretability of any improvement claim in this regime is severely limited.

### Questions for Authors

- **[Q1]** Table 4 presents Qwen and Llama grammar-only results as "(predicted)". What is the basis for these predictions? Are they from a regression model, extrapolation from Mistral, or another method? Why were these experiments not run?
- **[Q2]** Bootstrap CIs are provided for EE but not RE. The R-F1 improvements on DocRED (+0.50pp, +0.29pp) are small — are they statistically significant?
- **[Q3]** The 70B LoRA DocRED experiment uses 200 documents. What motivated this subset? How were documents selected? Is there evidence this subset is representative?

### Missing Experiments

- **[M1] Prompt-based mitigation experiments.** The paper claims "prompt-based mitigation is fundamentally unreliable" as Contribution (2), but provides no controlled experiment comparing explicit constraint prompting (e.g., "only use the following relation types: ...") across models. This claim is stated but not experimentally supported.
- **[M2] Structured IE baselines.** GoLLIE (code-generation IE), KnowCoder, and other schema-aware IE methods are not compared. These methods address the same problem (schema compliance in LLM-based IE) through different mechanisms and are the natural baselines.
- **[M3] Few-shot evaluation.** Only zero-shot and full fine-tuning are evaluated. Few-shot (1-5 examples) is the most common practical setting for LLM-based IE and would substantially strengthen the evaluation.
- **[M4] 8B FT RE constrained results.** The paper evaluates FT EE composability (Table 8) and 70B LoRA RE (Tables 9-10) but omits 8B FT RE constrained results — the most directly relevant comparison for practical use.

---

## R2 Review: Novelty and Related Work

### Novelty: 2.5/5

The paper's novelty distributes across three components:

**Violation taxonomy:** The five categories (ET, RV/EV, RoV, DR/AC, CF) are natural and complete given the ontology constraint formalism — they are essentially the only categories that *can* exist. Formalizing the obvious has some utility (standardized vocabulary, quantification framework), but the taxonomy itself is not a creative contribution. The decidability classification (local, prefix-decidable, non-local) adds modest theoretical value but is straightforward for anyone familiar with automata theory — a CFG (pushdown automaton with LIFO stack) cannot do the random access required for cross-field consistency.

**OntoCoDec method:** The grammar layer is a direct application of XGrammar with IE-specific JSON Schema. The paper explicitly states it is "implemented atop XGrammar." The semantic layer implements stateful logit masking with an entity registry — a lookup table that, given relation type R, restricts entity types to those satisfying domain/range constraints. The statefulness (entity-to-type mappings) is minimal. The conceptual distance from "compile type constraints into logit masks" (prior work in code generation) to "compile ontology constraints into logit masks" (this work) is not large. The engineering is competent but the contribution is incremental: it is, at its core, XGrammar + a domain/range lookup table with a fallback mechanism.

**Empirical study:** The "first large-scale empirical analysis" claim has value but needs qualification. Prior work has studied LLM IE output validity (Wadhwa et al. 2023), constrained decoding quality trade-offs (BoostCD), and schema compliance gaps (GoLLIE) — though not with this specific taxonomy or at this scale. The finding that "constraint tightness drives violations" is the most novel empirical insight, but the paper does not formalize "tightness" with a quantitative metric.

### Related Work Completeness: 2.0/5

The related work section is severely underdeveloped: approximately 15 lines across 3 paragraphs with ~14 total references. This is far below EMNLP expectations (typically 30-50+ references with substantive discussion of positioning).

**Critical missing citations and comparisons:**
- **GoLLIE (Sainz et al., 2024):** Code-generation approach to schema-constrained IE that enforces type constraints through Python dataclass definitions. This is the most directly comparable approach — it addresses the same problem through a fundamentally different mechanism (prompt-level schema encoding vs. decoding-time constraint enforcement). Not cited.
- **Structure Snowballing (Tam et al., 2024):** Documented the trade-off between constrained decoding and extraction quality in IE — directly relevant to the CF trade-off observed in this paper. Not cited.
- **KnowCoder (Li et al., 2024):** Schema-aware code-generation IE with explicit ontology grounding. Not cited.
- **REBEL (Cabot & Navigli, 2021), GenIE (Josifoski et al., 2022):** Structured generation methods for RE with implicit schema constraints. Not cited.
- **TANL (Paolini et al., 2021), UIE (Lu et al., 2022), InstructUIE:** Unified IE frameworks addressing schema compliance through linearization and instruction tuning. Not cited.
- **Broader constrained generation literature:** PICARD (Scholak et al., 2021) for SQL, NeuroLogic Decoding (Lu et al., 2021), and other constrained generation methods that could contextualize the approach. Not cited.

The paper positions itself against only three strands (LLM-based IE, grammar-constrained decoding, training-time ontology enforcement) with minimal depth. A reader cannot assess the paper's positioning relative to the field from Section 2 alone.

### Excitement: 2.0/5

The paper is thorough but does not generate substantial intellectual excitement. The core question — "do LLMs violate ontology constraints, and can constrained decoding help?" — has expected answers: yes and partially. The most interesting finding (post-hoc beats constrained in 5/6 ZS RE) actually undermines the method. The CF trade-off is thought-provoking as a fundamental tension, but the paper does not resolve it or propose a clear path forward beyond acknowledging it. The practical deployment story is muddled by the 70B LoRA failures and the near-zero ZS F1 scores. The contribution feels like careful measurement of a known problem with an incremental solution that trades one violation type for another.

### Strengths

- **[S1] Comprehensive evaluation breadth.** 3 datasets, 5 models, multiple configurations per setting, cross-scale analysis, ablation studies, latency benchmarks, and statistical testing. The evaluation matrix is above average for the subfield.
- **[S2] Transparent negative-result reporting.** Post-hoc superiority, CF trade-off, Trigger-F1 degradation, 70B LoRA failures — all reported honestly with mechanistic explanations rather than hidden or spun.
- **[S3] Post-hoc filtering analysis for EE.** The 99.6-100% discard rate is a clean, striking result demonstrating post-hoc non-viability for event extraction.
- **[S4] Three-way ablation (Table 5).** The unconstrained → grammar-only → full comparison cleanly demonstrates the enabling dependency between layers and the latent violation surfacing phenomenon.

### Weaknesses

- **[W1] Limited conceptual novelty.** OntoCoDec = XGrammar + entity-type lookup table with fallback. The engineering is sound but the gap from prior constrained decoding work is narrow. The paper does not introduce a new decoding paradigm, constraint formalism, or theoretical framework.
- **[W2] Severely incomplete related work.** ~14 references and ~15 lines of related work for an EMNLP submission is inadequate. GoLLIE, Structure Snowballing, KnowCoder, REBEL, GenIE, TANL, UIE, PICARD — all directly relevant and uncited. The paper cannot be properly evaluated without positioning against these works.
- **[W3] "First systematic study" claim is overclaimed.** Prior work has studied LLM IE output validity and constrained decoding trade-offs. The novelty is in the specific taxonomy and evaluation scale, not in the research question.
- **[W4] Method works best when least needed.** Under FT (where the method works well), baseline violations are already low (DR=0.5-2%). Under ZS (where violations are high, DR=15-57%), the method introduces CF=2-21% and post-hoc filtering often outperforms on F1.
- **[W5] Single EE dataset.** WikiEvents is the only event extraction evaluation. With one dataset, the "cross-task generalization" to EE rests on a single data point.

### Questions for Authors

- **[Q1]** How does OntoCoDec compare to GoLLIE's code-generation approach to schema enforcement? GoLLIE encodes type constraints through Python dataclass definitions — this achieves structural compliance through a fundamentally different mechanism. A head-to-head comparison is essential for positioning.
- **[Q2]** You claim "constraint tightness" drives violations rather than ontology size. Can you formalize tightness with a quantitative metric (e.g., average valid types per constraint position / total types) and show correlation with violation rates?
- **[Q3]** The "first systematic study" claim — are you aware of BoostCD's analysis of constrained decoding quality trade-offs, or GoLLIE's implicit schema compliance evaluation? How does your study differ in scope or depth?

---

## Roundtable Discussion

### Step 2: Cross-sharing

**Points of agreement (both reviewers):**
1. CF trade-off (3.7-21.1%) is the central weakness — the method introduces a new violation type while eliminating others
2. Limited novelty — XGrammar + lookup table is competent engineering but not a conceptual advance
3. Post-hoc superiority in 5/6 ZS RE configs is damaging to the practical narrative
4. Near-zero F1 baselines undermine the significance of improvement claims
5. Missing critical baselines (GoLLIE, structured IE methods, few-shot)
6. Paper is commendably honest about negative results

**Points of disagreement:**
- R1 (2.5) vs R2 (3.0) on overall score. R1 weighted the predicted data issue and missing experiments more heavily; R2 credited the evaluation breadth more. After discussion, the very thin related work (~14 references) and missing key baselines push the consensus toward 2.5.

### Step 3: Convergence

**The core tension:** The paper has genuine strengths in evaluation thoroughness and transparent reporting, but faces a compounding problem: (a) limited novelty + (b) the method's own results often argue against its utility (post-hoc wins in ZS RE, CF trade-off, no significant EE metric improvement, 70B LoRA failures) + (c) severely incomplete related work.

The paper is most convincing as a diagnostic study — the violation taxonomy and landscape analysis have standalone value. But the method contribution (OntoCoDec) is incremental and its results are mixed at best. For Findings acceptance, the paper would need either (a) stronger novelty in the method or findings, or (b) complete positioning against the field via adequate related work.

**Converged score: 2.5 (Borderline Findings)**

### Step 4: Synthesis

**Verdict: 2.5/5 — Borderline Findings**

The paper presents a systematic empirical study of ontology constraint violations in LLM-based IE with commendable evaluation breadth and transparent reporting. The violation taxonomy is useful and the finding that post-hoc filtering destroys 99.6-100% of EE arguments is compelling. However, the work faces four compounding problems: (1) OntoCoDec is an incremental engineering contribution over XGrammar with limited conceptual novelty; (2) the method's own results often argue against its utility — post-hoc filtering outperforms in 5/6 ZS RE configs, no significant improvement on semantically meaningful EE metrics, CF trade-off of 3.7-21.1%, and failure on quantized 70B models; (3) the related work is severely underdeveloped (~14 references) with critical missing comparisons (GoLLIE, Structure Snowballing, KnowCoder, REBEL, TANL); (4) some results are predicted rather than experimental without adequate disclosure. The paper would benefit from: completing all experiments, expanding related work substantially, adding GoLLIE and few-shot comparisons, formalizing the "constraint tightness" metric, and reconsidering whether the violation landscape study (rather than OntoCoDec) should be the primary contribution.

---

## Actionable Revision Priorities

1. **[Critical] Expand related work.** Add 20-30 references minimum. GoLLIE, Structure Snowballing, KnowCoder, REBEL, GenIE, TANL, UIE, PICARD must be cited and discussed.
2. **[Critical] Complete all experiments.** Remove all "(predicted)" results. Run Qwen/Llama grammar-only, complete 70B LoRA evaluations, add bootstrap CIs for RE.
3. **[Critical] Add GoLLIE comparison.** Head-to-head on at least SciERC RE — this is the most natural baseline.
4. **[High] Formalize constraint tightness.** Define a quantitative metric (e.g., |valid_types_per_position| / |total_types|) and correlate with violation rates across datasets.
5. **[High] Add few-shot evaluation.** 1-shot and 5-shot on all datasets would substantially strengthen the practical relevance.
6. **[High] Strengthen CF analysis.** Expand error analysis beyond 15 cases. Measure downstream KG impact of CF vs DR violations to support the "hard vs soft" severity argument.
7. **[Medium] Add prompt-based mitigation experiment.** The paper claims prompt unreliability as a contribution but provides no controlled experiment.
8. **[Medium] Add 8B FT RE constrained results.** This is the most practically relevant configuration and is missing.

---

## Auto-Reject Signal Check

| Signal | Status |
|--------|--------|
| Anonymity violation | ✅ No violation detected |
| Page limit (8pp main) | ⚠️ 8 pages main text + 2 pages refs/tables — verify formatting |
| Limitations section | ✅ Present, covers 3 points |
| Hallucinated citations | ⚠️ Not checked — only 14 refs, all appear standard |
| Responsible NLP Checklist | ⚠️ Not in PDF (should be in OpenReview form per EMNLP 2026 rules) |


---

## 引用验证结果

**统计**: 60 篇文献 / 101 处引用 / 在线验证 60/60 篇

### 问题 (6)

- ⚠️ `pldi2025_type_constrained_codegen` — 元数据不匹配: first_author: bib=m\"undler vs api=mündler
- ⚠️ `eberts2020spert` — 元数据不匹配: first_author: bib=eberts vs api=eberts markus
- ⚠️ `decao2021genre` — 元数据不匹配: first_author: bib=de cao vs api=cao
- ❌ `regino2025kgcurator` — 在线验证未找到匹配（疑似虚假引用）: best match similarity 0.48 below threshold 0.82
- ⚠️ `schall2025hiddencost` — 元数据不匹配: first_author: bib=schall vs api=
- ⚠️ `qwen2025qwen3` — 元数据不匹配: first_author: bib=team vs api=yang

### ✅ 通过 (54)