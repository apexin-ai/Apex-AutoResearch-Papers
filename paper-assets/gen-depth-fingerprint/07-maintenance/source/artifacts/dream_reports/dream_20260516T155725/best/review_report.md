---
dream_id: dream_20260516T155725
tier: best
overall_score: weak accept
timestamp: 2026-05-16T16:23:07.829178+00:00
---

# Review Report: Distributional Depth Profiling

**Paper:** Distributional Depth Profiling: Ordinal Estimation of Recursive LLM Generation Depth via Differential Feature Response

**Venue standard:** Top ML venue, ~25% acceptance rate, 6-point scale

---

## 1. Summary

This paper introduces ordinal depth estimation as a new task: given a text, predict how many recursive LLM generation steps it has undergone (generation depth 0–4). The authors characterize "differential depth response" — central-tendency/diversity features (entropy mean, TTR, hapax ratio) drift monotonically with depth while distributional shape features (entropy std, tail decay) remain stationary. A 7-feature XGBoost ensemble achieves 0.83 macro-F1 within-generator and 0.81 under leave-one-generator-out (LOGO) cross-validation across 5 generators from 3 model families. Additional experiments cover paraphrastic vs. continuation chains, finer-grained 5-class ordinal classification (F1=0.51, concordance=0.82), and end-to-end QLoRA classifiers that achieve higher within-generator accuracy (0.91) but degrade under LOGO (0.72), validating the robustness advantage of interpretable features.

---

## 2. Strengths

- **Genuinely novel task formulation.** No prior work attempts ordinal depth estimation. The move beyond binary real/synthetic detection is well-motivated by the reality of recursive generation chains in web-scale corpora. The framing as an ordinal classification problem with formal LOGO evaluation protocol is a meaningful contribution to the research agenda (§1, §3.1).

- **Clean empirical characterization.** The differential depth response — drift vs. stationary feature partition — is demonstrated convincingly. Table 2 shows a sharp bifurcation: drift features have R² > 0.88 while stationary features have R² < 0.20. The location-shift interpretation is mechanistically coherent and well-supported by the perplexity validation (13.5 → 1.72 across depths, Spearman ρ = −0.92).

- **Strong cross-generator generalization.** LOGO macro-F1 = 0.81 with per-generator std = 0.032 across 5 generators from 3 distinct families (Tables 3–4) is a strong result. The leave-one-family-out evaluation showing only −1.5pp additional degradation beyond generator-level holdout is particularly convincing for architecture-invariance claims.

- **Comprehensive experimental coverage.** The paper covers five distinct experimental dimensions: feature ablation (§4.1), cross-generator evaluation (§4.2), chain-type comparison (§4.3), granularity analysis (§4.4), and end-to-end neural classifiers (§4.5). Each addresses a natural question about the phenomenon.

- **Informative negative/bounded results.** The 5-class result (F1=0.51, concordance=0.82) is honestly reported as establishing a practical ceiling. The gen-2/gen-3 confusion (42%) is well-explained by diminishing drift returns. The E2E generalization gap (−19pp under LOGO) provides genuine insight about the interpretability–robustness tradeoff.

- **Well-designed evaluation protocol.** LOGO is the right evaluation for generalization claims. Feature ablation confirms complementarity rather than redundancy. The paraphrastic comparison provides theoretical validation via attractor convergence predictions.

- **Clear writing.** The paper is well-organized, with clean logical flow from motivation through characterization to practical implications. Each experiment section states the question, presents results, and interprets findings concisely.

---

## 3. Weaknesses

- **(Major) Limited model scale.** All 5 generators are ≤2.8B parameters, and all are base (pretrained) models. Real-world recursive generation chains are more likely to involve instruction-tuned models at larger scales (7B–70B+). The model collapse literature suggests that distributional drift attenuates with model capacity. Without testing on larger or instruction-tuned models, the practical applicability of the findings to realistic contamination scenarios is uncertain. The paper acknowledges this in Limitations (§6), but this is a fundamental gap between the motivating scenario and experimental scope.

- **(Major) Synthetic chain construction.** All chains use single-model continuation where the same generator produces all depths. Real-world contamination involves heterogeneous generators, diverse prompts, varying decoding parameters, and human editing at each step. The paper tests only a single continuation prompt and fixed sampling parameters (though these details are not fully specified in the method section). The practical relevance of the controlled experimental setup to the motivating real-world problem is unclear.

- **(Major) Limited methodological novelty.** The features (NLL entropy statistics, TTR, hapax ratio) are entirely standard stylometric and detection features. The classifier (XGBoost) is off-the-shelf. The observation that recursive generation reduces lexical diversity and increases predictability is well-established in the model collapse literature (Shumailov et al., 2024). The paper's contribution is primarily in (a) formulating the ordinal task and (b) empirically characterizing the drift/stationary partition — the methodology itself is not novel.

- **(Minor) Reference model dependency underexplored.** All experiments use Pythia-410M as the reference model. The paper lists this as a limitation but does not ablate reference model choice. Given that Pythia-410M shares architecture with two of the five generators (Pythia-1B, Pythia-2.8B), within-family feature extraction could inflate performance for Pythia generators. The higher F1 for Pythia-1B (0.86, highest in Table 3) is consistent with this concern.

- **(Minor) Narrow domain and language.** Seed texts presumably come from a single domain (not specified in the paper). No cross-domain or cross-language experiments are reported. Depth drift dynamics could vary substantially across registers (news, social media, creative writing, code).

- **(Minor) Feature ablation labeling is confusing.** In Table 1, "Surface only (2 features)" refers to TTR and hapax_ratio, while "Reference only (5 features)" refers to the 5 entropy-based features requiring the reference model. But Section 3.3 categorizes features into "Drifting" (4 features including TTR and hapax) and "Stationary" (3 features). These are two different partitions that are not clearly distinguished, potentially confusing readers about what "surface" vs "reference" means relative to "drifting" vs "stationary."

- **(Minor) Some references appear placeholder.** "Brokentel et al., 2025" and "Attractor Authors, 2025" in the Related Work section look like anonymized placeholder citations. If these are real papers, the citation format should match standard conventions; if they are the authors' own work, this compromises anonymity.

- **(Minor) Missing figures.** The paper contains 10 tables but no figures in the main text. A visualization of the differential depth response (feature values × depth, as described in the experiment design) would greatly strengthen the core empirical contribution. The strip plot / feature trend visualization seems planned but absent from the submitted PDF.

---

## 4. Questions for Authors

1. **Reference model ablation:** How sensitive are results to reference model choice? Specifically, does using a non-Pythia reference model (e.g., OLMo or Qwen-family) change the LOGO results, and does it eliminate the potential inflation for Pythia generators?

2. **Instruction-tuned models:** Have you tested any instruction-tuned variants (e.g., Qwen3-1.7B-Instruct)? The motivating scenario (web contamination) primarily involves instruct model outputs. If the depth signal collapses for instruct models, this would fundamentally limit practical impact.

3. **Convergence behavior:** The perplexity drops from 13.5 (depth-0) to 1.72 (depth-4), suggesting rapid convergence. At what depth would you expect features to reach a fixed point? Is the gen-2/gen-3 confusion (42%) evidence that convergence has effectively occurred, making the 3-class formulation an inherent ceiling rather than a practical one?

4. **Real-world validation path:** Is there any way to validate the method on naturally-occurring recursive generation (e.g., detecting depth in web-crawled text where some ground truth is available)? The gap between controlled chains and real contamination seems large.

5. **Seed text diversity:** How many seed texts were used, from what source, and what is the average text length at each depth? The paper does not specify dataset statistics (total of 22,920 records is mentioned in §4.2 but without breakdown).

---

## 5. Missing Experiments or Analysis

Comparing against the 5 planned experiments:

1. **Feature ablation and trend (plan_001):** ✅ Fully covered in §4.1. Tables 1–2 report ablation and per-feature trends. Perplexity validation included.

2. **Cross-generator evaluation (plan_002):** ✅ Fully covered in §4.2. Tables 3–4 report LOGO and leave-one-family-out. Feature importance reported.

3. **Paraphrastic comparison (plan_006):** ✅ Covered in §4.3. Tables 5–6 report classification comparison and feature-level drift. Cross-transfer F1 reported.

4. **Finer-grained ordinal (plan_009):** ✅ Covered in §4.4. Tables 7–8 report granularity comparison and per-depth F1. Ordinal methods (CORAL, Frank-Hall) compared.

5. **End-to-end classifier (plan_012):** ✅ Covered in §4.5. Tables 9–10 report E2E vs feature-based comparison. LOGO generalization gap quantified.

**All 5 planned experiments are reported.** Coverage is comprehensive relative to the design document.

**Notable gaps beyond planned experiments:**
- No figures/visualizations in the main text (despite figure descriptions in the design)
- No confusion matrix visualization (mentioned in design as Fig 6)
- No dataset statistics table (number of samples per generator × depth)
- No error analysis or qualitative examples
- Cross-model chains (different generator at each depth) not tested
- No domain/prompt diversity analysis

---

## 6. Soundness: 4/5

Claims are well-supported within the experimental scope. Statistical methodology is appropriate (bootstrap CIs, significance tests). The LOGO evaluation protocol is the right choice for generalization claims. The main soundness concern is whether conclusions generalize beyond the controlled small-model setting — but the paper does not overclaim. The feature complementarity claim (Table 1) and architecture invariance claim (Tables 3–4) are convincingly demonstrated.

## 7. Significance: 3/5

The task formulation is a genuine contribution to the research agenda. However, practical significance is limited by: (1) restriction to small base models, (2) controlled chain construction far from real-world contamination, (3) the 3-class ceiling limits fine-grained provenance tracking. The differential depth response characterization is interesting but largely predictable from model collapse literature. The paper opens a research direction rather than providing a deployable solution.

## 8. Novelty: 3/5

The ordinal depth estimation task is novel — no prior work formulates this problem. The drift/stationary feature partition is a useful empirical characterization. However, the features are standard stylometric measures, the classifier is off-the-shelf, and the core observation (recursive generation reduces diversity and increases predictability) is well-established. The novelty is primarily conceptual (task formulation + empirical characterization) rather than methodological.

## 9. Clarity: 4/5

Well-written and logically organized. Each experiment section has clear structure (question → results → interpretation). The Discussion section provides good synthesis. Minor issues: the surface/reference vs drift/stationary feature partition overlap is confusing; dataset construction details are sparse; placeholder-looking citations; no figures despite being a characterization paper where visualization would be highly valuable.

## 10. Overall Score: 4/6 (Weak Accept)

A well-executed empirical study that introduces a genuinely novel task formulation with solid cross-generator evidence, but limited by small model scale, controlled experimental setup, and modest methodological novelty.

## 11. Confidence: 4/5

High confidence in this assessment. The methodology and claims are straightforward to evaluate. Minor uncertainty about whether frontier-scale or instruct-model experiments would substantially change the picture.

## 12. Recommendation

**Weak Accept.** The paper makes a clear conceptual contribution by formulating ordinal depth estimation as a task and providing the first systematic empirical characterization across multiple generators and model families. The LOGO results (0.81 F1, std=0.032) convincingly demonstrate cross-generator generalization, and the granularity ceiling and E2E comparison add genuine insight. The main concerns — limited model scale, controlled chain construction, and standard features/classifiers — are real but do not invalidate the core empirical findings. For a top venue, this is borderline: the task novelty and thorough execution argue for acceptance, while the limited practical impact and modest methodological novelty argue against. The paper would be strengthened significantly by (a) testing instruction-tuned models, (b) ablating reference model choice, and (c) adding visualizations of the core differential response phenomenon.
