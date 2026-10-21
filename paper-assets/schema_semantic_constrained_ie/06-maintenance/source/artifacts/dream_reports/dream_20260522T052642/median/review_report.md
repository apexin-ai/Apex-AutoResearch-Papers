---
dream_id: dream_20260522T052642
tier: median
overall_score: 3.0 Findings
timestamp: 2026-05-22T06:40:57.646481+00:00
---

# Dream Review Report: OntoCoDec: Type-Valid Information Extraction via Compiled Ontology Constraints

**dream_id:** 20260522T052642
**Review Mode:** full (2 Reviewers, 4-step roundtable)
**Target Venue:** EMNLP 2026 (ARR)

---

## Consolidated Scores

| Dimension | R1 (Post-discussion) | R2 (Post-discussion) | Consensus |
|-----------|---------------------|---------------------|-----------|
| Soundness | 3.5 | 3.5 | **3.5** |
| Excitement | 2.5 | 2.5 | **2.5** |
| Reproducibility | 4.0 | 4.0 | **4.0** |
| **Overall Assessment** | 3.0 | 3.0 | **3.0 (Findings)** |

---

## Paper Summary

OntoCoDec compiles IE ontology schemas into two composable constraint layers for autoregressive decoding: (1) a grammar layer via XGrammar enforcing JSON structure and type vocabulary membership, and (2) a semantic layer maintaining a stateful entity registry with dynamic logit masking for domain/range constraints. Evaluated on SciERC, DocRED (RE), and WikiEvents (EE) across 4 models (7B–70B), it reduces domain/range violations by up to 99.4% with F1-neutral impact. Fine-tuning composability with LoRA achieves R-F1 of 43–46% with near-zero violations.

---

## Key Strengths (Consensus)

1. **Thorough experimental methodology.** Five-way ablation, causal tracing of residual violations, bootstrap CIs (10K iterations), seed variance analysis, constraint tightness analysis across datasets. Both reviewers rated reproducibility at 4/5 — the paper provides LoRA hyperparameters, hardware specs, verbatim prompts, and data split details.

2. **Principled architecture design.** The decidability taxonomy (context-free / prefix-decidable with state / non-local) cleanly motivates the two-layer decomposition. Proposition 1 (domain/range constraints are not context-free, proved via pumping lemma) is rigorous. The graceful degradation mechanism (fallback to grammar-only when mask intersection is empty) is well-justified.

3. **Fine-tuning composability is the strongest practical contribution.** LoRA + OntoCoDec achieves R-F1 40–46% with DR ≤0.09% (8B) and CF ≤1.2%. This demonstrates the method's value in the deployment-relevant regime where extraction quality is meaningful.

4. **Empirical enabling dependency is informative.** Grammar-only yields only ~3% DR reduction on RE, while grammar+semantic yields 94%. This non-obvious empirical finding justifies the two-layer architecture in the zero-shot regime.

5. **Post-hoc filtering non-viability on EE is compelling.** The 99.6–100% rejection rate on WikiEvents provides strong differentiation from the "just filter" alternative, particularly since RE post-hoc is merely costly (16–48% rejection) while EE post-hoc is completely non-viable.

6. **Honest treatment of limitations.** The paper clearly acknowledges CF tradeoff, ZS F1 limitations, Mistral boundary case, forward coreference scope, and frames zero-shot as diagnostic rather than deployment-ready.

---

## Key Weaknesses (Consensus)

### Critical

1. **Incomplete 70B LoRA results (XX.XX placeholders).** Both reviewers flagged this as the single most consequential issue. Section 4.2 (or corresponding appendix/runtime section) contains placeholder values for 70B LoRA fine-tuning numbers. The abstract and introduction claim "scale generalization to 70B parameters and composability with LoRA fine-tuning" — this claim is not substantiated without the 70B LoRA data. This is disqualifying for a complete submission and directly undermines the "scale-independent composability" contribution.

### Major

2. **CF tradeoff converts violations rather than eliminates them.** R2's sharpest observation, endorsed by R1: on SciERC ZS, total violations (DR+CF) drop from 15.45% to 10.83% — only a 32% reduction when both violation types are counted, not the headline 94% DR reduction. On DocRED ZS, total violations go from 18.56% to 12.78% (31%). The method partially converts one violation type into another. Under fine-tuning CF drops to ≤1.2%, which is practical, but the zero-shot violation-conversion pattern limits the framework's value precisely where it is most needed.

3. **Zero-shot F1 too low for practical significance.** ZS R-F1 of 2–8% (RE) and Arg-F1 ≈ 0% (EE) means models fundamentally fail at extraction. Enforcing type constraints on overwhelmingly incorrect extractions has limited practical value. The paper devotes considerable space to zero-shot results that are diagnostic but not deployment-relevant. The "inverted utility curve" (method works best where least needed, and where most needed, extraction fails) weakens the overall narrative.

4. **Novelty is primarily engineering integration.** Both reviewers converged: the grammar layer is XGrammar off-the-shelf, the semantic layer is a dictionary-based state tracker with logit masking, and composition is bitwise AND with fallback. Each component is straightforward; the contribution is assembling them for IE. The "first systematic integration" claim is technically accurate but narrow in significance. The delta over "XGrammar for JSON + post-hoc validation" is real but incremental — particularly in the fine-tuned regime where post-hoc rejection rates are only 0.6–2%.

5. **Grammar layer becomes no-op under fine-tuning.** The ablation shows the grammar layer contributes nothing additional when models are fine-tuned (violations are already structurally valid). This means the "two-layer enabling dependency" — the paper's core architectural insight — is validated only in the zero-shot regime where extraction quality is too low to matter practically. For the deployment-relevant FT setting, only the semantic layer matters.

### Minor

6. **Narrow dataset diversity.** All English, two of three datasets are RE (SciERC, DocRED). WikiEvents EE is preliminary (20 FT test docs with high per-document variance). No TACRED, ACE05, or biomedical IE benchmarks. Constraint tightness analysis spans only n=3 schemas.

7. **Missing experimental baselines.** No comparison with IterGen (backtracking-based semantic constraint enforcement), BoostCD (boosting-based constrained/unconstrained alternation), or a "constrained re-generation" baseline (detect violations → regenerate only type tokens under constraints, potentially avoiding CF tradeoff). GoLLIE comparison is asymmetric (ZS GoLLIE vs FT OntoCoDec).

8. **Mistral residual DR (13.4% SciERC, 33.2% DocRED)** shows method effectiveness degrades substantially for poorly calibrated models. The dual-factor analysis excludes Mistral with a post-hoc criterion (ET>5%), limiting the "universality" claim.

9. **WikiEvents EE evaluation is preliminary.** FT evaluation uses only 20 test documents. Per-document variance is high (Arg-F1 std/mean > 0.5). Bootstrap CIs for EE are reported as p-values in text but no full CI table is provided.

---

## Questions for Authors (Consolidated)

1. **70B LoRA completeness:** When will the 70B LoRA numbers be available? Can you either provide these results or remove the scale-composability claim from the abstract?

2. **Total violation burden:** Have you computed a unified "type violation rate" (DR+CF) across all settings? Does OntoCoDec still show a clear win over unconstrained decoding on this combined metric in zero-shot?

3. **Constrained re-generation alternative:** Have you considered a detect-and-regenerate approach that identifies DR violations after generation and re-generates only the type-bearing tokens under constraints? This could potentially avoid the CF tradeoff while achieving similar DR reduction.

4. **Grammar layer under FT:** Given that the grammar layer is a no-op for fine-tuned models, would a deployment using LoRA + semantic-layer-only (without grammar) achieve identical results? If so, how does this affect the "two-layer architecture is necessary" claim?

5. **IterGen comparison:** IterGen (Ugare et al. 2025) addresses semantic constraints beyond grammar via backtracking. Is there a technical reason this was not experimentally compared? Even a qualitative analysis of enforcement mechanism differences would strengthen positioning.

---

## Roundtable Discussion Summary

### Step 1 (Independent Reviews)
- R1 (Methods+Experiments): Overall 3.0. Flagged 70B placeholders as critical, CF tradeoff as most significant limitation, and core novelty as systems engineering. Found statistical rigor generally good.
- R2 (Novelty+Related Work): Overall 3.0. Characterized novelty as "solid applied contribution," found excitement low (results largely expected given correct implementation), and identified CF as "converting violations rather than eliminating them."

### Step 2 (Cross-Sharing)
- R1 adopted R2's "violation conversion" framing as the sharpest characterization of the CF problem. Adjusted Excitement down from 3.0 to 2.5. Disagreed with R2's Soundness of 4.0 given the placeholders.
- R2 adopted R1's stronger stance on 70B placeholders being "disqualifying." Adjusted Soundness down from 4.0 to 3.5. Maintained Excitement at 2.5, arguing the "inverted utility curve" limits practical impact.

### Step 3 (Convergence)
Full consensus on:
- Overall: 3.0 (Findings) — both reviewers independently arrived at this score and maintained it after discussion
- The 70B LoRA incompleteness is the most actionable issue
- CF tradeoff is the deepest methodological concern
- Fine-tuning composability is the strongest practical contribution
- Paper is honest and thorough but engineering-dominant in novelty

### Disagreements resolved:
- Soundness converged to 3.5 (R2 adopted R1's position on placeholder severity)
- Excitement converged to 2.5 (R1 adopted R2's "expected results" and "inverted utility" framing)
- No unresolved disagreements remain

---

## Final Recommendation

**Overall Assessment: 3.0 — Findings**

OntoCoDec addresses a genuine problem (ontology type violations in LLM-based IE, 13–57% DR rates) with a well-engineered, thoroughly evaluated solution. The fine-tuning composability results (R-F1 43–46%, DR ≤0.09%) and the empirical enabling dependency between grammar and semantic layers are useful contributions to the community. The evaluation breadth (5 models, 3 datasets, 2 tasks, 3 decoding strategies) exceeds the norm.

However, four factors prevent a Conference recommendation: (1) incomplete 70B LoRA results with visible placeholders undermine a stated contribution; (2) the CF tradeoff means total violations are only partially reduced in zero-shot, converting one violation type into another; (3) the novelty is engineering integration of existing components (XGrammar + stateful logit masking) rather than a methodological advance; (4) the framework's practical value is strongest under fine-tuning, where the grammar layer is unnecessary and baseline violation rates are already low (0.5–2%).

**Path to 3.5 (borderline Conference):** Complete the 70B LoRA results, add IterGen or constrained-re-generation baseline comparison, and reframe the narrative to foreground the FT composability results rather than the ZS violation reduction. Discuss the total violation burden (DR+CF) more prominently in the main text.

**Path to 4.0 (Conference):** Additionally resolve the CF tradeoff within the framework (e.g., global entity consensus mechanism), demonstrate on a broader dataset set (biomedical, ACE05), and include a formal comparison with concurrent constrained decoding methods (IterGen, BoostCD).

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