---
dream_id: dream_20260515T132059
tier: worst
overall_score: leaning reject
timestamp: 2026-05-15T14:34:04.053727+00:00
---

# Dream Review Report: "How Should LLMs Generate Evidence for Document-Level Relation Extraction?"

**Venue:** EMNLP 2026 Main (via ACL Rolling Review)
**Review Mode:** Full (2 Reviewers + Roundtable)
**Date:** 2026-05-15

---

## Meta-Review (Roundtable Synthesis)

Both reviewers independently scored this paper at **Overall 2.5/5 (Leaning Reject)**. The roundtable converged on the assessment that this paper makes genuine empirical contributions suitable for the **Findings track** but does not meet the bar for Main conference acceptance at EMNLP 2026 (~22% acceptance rate).

### Points of Agreement (Both Reviewers)

1. **The task definition (evidence-grounded LLM DocRE) fills a genuine gap.** No prior work has LLMs jointly generate (h, r, t, evidence sentences) for document-level RE. This is a credible "first."
2. **Evidence-extraction decoupling under GRPO is the paper's strongest finding.** The scissors pattern (reward↑, Rel-F1↓) and the extreme lr=5e-6 case (Evi-F1=85.0, Rel-F1=1.4) are empirically compelling.
3. **CED's non-significance vs. flat-NLI is a fatal title-contribution mismatch.** CED is prominently featured but fails to significantly outperform the simpler baseline on any metric (p>0.10). The paper's primary method contribution effectively reduces to "RSFT applied to DocRE."
4. **The GRPO decoupling claim is confounded by QLoRA.** All GRPO experiments use 4-bit QLoRA. Without a full-FT or bf16 control, the claim cannot distinguish QLoRA artifacts from genuine RL-for-IE phenomena. The abstract/intro use unqualified language while Limitations correctly scopes to "GRPO+QLoRA."
5. **Dev-to-test degradation is concerning.** RSFT drops 5.75pp (46.55→40.80) vs. SFT's 1.27pp (40.57→39.30). The 6x relative ratio suggests indirect overfitting through the CED scoring pathway.
6. **DPO experiment is underspecified.** Insufficient detail for reproducibility.
7. **Single-seed test reporting** with ~2pp dev variance across seeds risks cherry-picking appearance.

### Points of Divergence

| Issue | R1 | R2 |
|-------|----|----|
| Soundness | 2/5 (code-description mismatches found) | 3/5 (claims supported within narrow scope) |
| Excitement | 3/5 (decoupling finding interesting enough) | 2/5 (limited method novelty, large extraction gap limits impact) |
| Related work | Notes missing RL-for-IE citations | Extensive gaps identified: R1-RE, recent LLM DocRE methods, GRPO stability literature, NLI faithfulness literature |
| EDCR assessment | Flags implementation vs. definition mismatch | Flags underpowered human validation (n=100) |

**Resolution:** R2's related work concerns are well-founded and substantive. R1's code-level findings (CED formula discrepancy, EDCR implementation mismatch) are severe if confirmed. The meta-review adopts R1's lower Soundness score as the more conservative assessment.

### Final Consensus Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| **Soundness** | **2.5/5** | Multiple implementation-description mismatches erode trust; QLoRA confound limits GRPO claim generalizability; RSFT-over-SFT result solid but marginal on test (p=0.08) |
| **Excitement** | **2.5/5** | Task definition is valuable; decoupling finding is interesting; but CED≈flat-NLI eliminates method novelty; RSFT is existing technique; large extraction gap (40.8 vs DREEAM 63.0) limits practical appeal |
| **Overall** | **2.5/5 (Leaning Reject)** | Suitable for Findings, not Main |
| **Confidence** | **4/5** | Both reviewers have domain expertise in DocRE, RL fine-tuning, and NLI-based evaluation |

### Recommendation

**Reject for Main; redirect to Findings.** Three conditions for Main acceptance:
1. Resolve CED formula/code alignment and EDCR implementation vs. definition mismatch
2. Complete a non-QLoRA GRPO control (bf16 LoRA or full FT) to scope the decoupling claim
3. Honestly reframe: downgrade CED from headline method to "one scoring option"; retitle to emphasize the systematic study rather than CED

---

## Reviewer 1: Methods and Experiments

### Summary
This paper presents a systematic study of LLM-based evidence generation for document-level relation extraction. The core finding is that RSFT (rejection sampling fine-tuning) consistently improves evidence quality regardless of scoring function, while GRPO exhibits catastrophic evidence-extraction decoupling. The paper introduces EDCR as a diagnostic metric and provides thorough ablations across scoring functions, model sizes, and datasets.

### Strengths

- **Comprehensive training paradigm comparison.** The GRPO→DPO→SFT→RSFT spectrum (Table 11) is more insightful than a typical ablation. The ordering reveals that data curation (not just avoiding policy gradients) is key—DPO avoids forgetting but yields no gain, proving the distinction is about training data quality, not loss function.

- **Evidence-extraction decoupling is well-documented.** The lr=5e-6 extreme case (Evi-F1=85.0 exceeding SFT's 79.8, while Rel-F1 collapses to 1.4) is a clean, striking demonstration. The G=4 vs G=8 comparison (Table 9) with partial recovery (+1.8pp Rel-F1) implicates advantage estimation noise. The full G=8 trajectory (Table 10) showing reward peaking at step 80 while Rel-F1 already declines is compelling.

- **Well-designed ablation structure across multiple axes.** CED vs flat-NLI (Table 4), DeBERTa-base vs large (Table 5), top-k=1 vs k=3 (Table 7), CED-as-reranker (Table 6), model size 1.7B/4B/8B (Table 16), DocRED vs Re-DocRED (Table 17). The CED-reranker experiment is a particularly clever control separating CED's value as a training signal from inference-time application.

- **Intellectual honesty.** The paper transparently reports CED's non-significance over flat-NLI (p>0.10 all metrics), the extraction gap to encoder methods (40.8% vs 63.0%), EDCR's weak human correlation (r=0.28), and the dev-to-test asymmetry. This is unusual and credibility-enhancing.

- **Statistical testing present for key claims.** Paired bootstrap with 10,000 resamples. Non-significance correctly reported rather than hidden.

- **EDCR captures a real evaluation blind spot.** GRPO lr=5e-6 achieves Evi-F1_cond=85.0 but EDCR=98.8—nearly all citations are entity-sharing distractors. This pathology is completely invisible to standard Evi-F1.

### Weaknesses

- **(Major) GRPO decoupling claims confounded by QLoRA.** All GRPO experiments use 4-bit QLoRA (rank=64). QLoRA's discretized gradients introduce their own instabilities for RL training. The abstract states "online reward optimization (GRPO) causes catastrophic evidence-extraction decoupling" without qualification. The Limitations section correctly scopes to "GRPO+QLoRA," but the abstract and introduction do not. A bf16 LoRA or full fine-tuning GRPO control is essential to determine whether decoupling is a QLoRA artifact or a genuine RL-for-structured-IE phenomenon.

- **(Major) CED does not significantly outperform flat-NLI, undermining the method contribution.** CED is prominently featured throughout (title area, all main tables), yet Table 4 shows no statistically significant advantage (rel_F1: p=0.11; evi_F1: p=0.42; EDCR: p=0.15). Jaccard candidate overlap of 0.76 confirms minimal differentiation. The paper's primary method contribution effectively reduces to "RSFT applied to DocRE with any NLI-based scoring," which is less novel than the framing suggests.

- **(Major) Test set result is not significant at α=0.05.** RSFT+CED achieves +1.5pp Rel-F1 over SFT on test (p=0.08). While this is borderline, at a top venue the primary result should clear the standard significance threshold. Combined with the 5.75pp dev-to-test drop (vs SFT's 1.27pp), reviewers can reasonably argue the dev-set gains contain an overfitting component.

- **(Major) DPO experiment underspecified.** No training details: learning rate, LoRA configuration, number of epochs, preference pair construction methodology. DPO is a key data point in the paradigm spectrum (Table 11) but cannot be reproduced or evaluated as presented.

- **(Moderate) Dev-to-test degradation asymmetry insufficiently analyzed.** The 6x relative degradation ratio (RSFT 5.75pp vs SFT 1.27pp) is concerning. RSFT candidates are generated from train-split documents and CED scoring uses gold evidence labels—this creates an indirect overfitting pathway. A diagnostic (e.g., RSFT performance on held-out documents not used for candidate generation) would clarify.

- **(Moderate) Single-seed test reporting.** Dev rel_F1 varies from 44.49 (s42) to 46.55 (s44) across seeds. Test results from a single best-dev configuration risks cherry-picking. Mean ± std across seeds should be reported.

- **(Moderate) Extraction-only reward also fails under GRPO.** Table 8 shows flat-NLI and extract-only G=4 both collapse. If even an extraction-only reward (no evidence component) causes failure, the phenomenon may be GRPO+QLoRA instability for structured generation broadly, not specifically evidence-extraction tension. This undermines the "decoupling" narrative.

- **(Minor) Missing GRPO trajectory figure.** The decoupling phenomenon is the paper's strongest finding but is presented only in tables. A training dynamics plot (rel_F1, evi_F1, reward vs. step) would be far more compelling and should be the centerpiece figure.

- **(Minor) No error analysis of RSFT improvements.** What types of relations or documents benefit most from RSFT? A per-relation-type or per-document-complexity breakdown would add depth.

### Questions for Authors

1. How were joint Evi-F1 numbers (Tables 2, 3, 12) computed? Does the evaluation code implement both conditional and joint protocols?
2. Given extraction-only reward also fails under GRPO+QLoRA, how do you distinguish "evidence-extraction decoupling" from general GRPO+QLoRA instability for structured generation?
3. For DPO: what learning rate, LoRA rank/alpha, epochs, and preference pair construction were used?
4. Have you tested GRPO with bf16 LoRA (no 4-bit quantization)?
5. What is the per-seed variance on test set results?

### Scores
- **Soundness:** 2/5
- **Excitement:** 3/5
- **Overall:** 2.5/5
- **Confidence:** 4/5

---

## Reviewer 2: Novelty and Related Work

### Summary
This paper claims to present the first systematic study of LLM-based evidence generation for DocRE, introducing CED scoring, EDCR metric, and a training paradigm comparison (RSFT/GRPO/DPO). While the task definition fills a genuine gap and the negative RL findings are interesting, method-level novelty is thin (CED ≈ flat-NLI; RSFT is established), related work coverage has substantial omissions, and several novelty claims are overscoped.

### Strengths

- **The "first" claim for evidence-grounded LLM DocRE is credible.** No prior work has LLMs jointly produce (h, r, t, evidence sentences) for document-level RE. Encoder methods (DREEAM, SAIS) derive evidence implicitly from attention weights. All prior LLM DocRE methods produce triples only. This is a genuine task-level contribution.

- **Evidence-extraction decoupling is the strongest and most novel empirical finding.** GRPO driving Evi-F1 to 85.0 while Rel-F1 collapses to 1.4 is striking. The G=4→G=8 comparison is valuable: partial recovery implicates advantage estimation noise. This finding has independent value for the RL-for-NLP community.

- **Training paradigm spectrum is insightful.** GRPO ≪ DPO ≈ SFT < RSFT, with the analysis that the fundamental distinction is data curation vs. loss function modification, is a nuanced empirical takeaway.

- **Intellectual honesty throughout.** Transparent about CED non-significance, extraction gap, EDCR limitations, and dev-to-test degradation. Unusual and credibility-enhancing.

- **EDCR captures a real blind spot.** Simple, interpretable metric that identifies a failure mode (GRPO decoupling) invisible to Evi-F1.

### Weaknesses

- **(Major) CED is not novel and fails to differentiate.** The contrastive margin (p_entail(gold) − max p_entail(distractor)) is standard in retrieval, reranking, and faithfulness evaluation literature (contrastive rewards in RLHF, INFUSE, TRUE benchmark). More critically, CED does NOT outperform flat-NLI (p>0.10 all metrics, 76% candidate overlap). Despite being named prominently, CED's contribution is marginal. The paper effectively reduces to "RSFT applied to DocRE."

- **(Major) RSFT is existing methodology applied to a new domain.** Rejection sampling fine-tuning (RAFT/ReST) is well-established since 2023 for math, code, and dialogue. The theoretical PPO equivalence has been shown. The paper's RSFT pipeline (generate→score→filter→retrain) involves no architectural or algorithmic innovation. Applying it to DocRE is a valid application, but the framing positions it as a methodological advance.

- **(Major) Significant related work gaps:**
  - **R1-RE** (GRPO for sentence-level RE that succeeds) — the most critical missing citation. Why does GRPO work sentence-level but fail document-level? Discussing this would strengthen the paper.
  - **Recent LLM-based DocRE methods** (RelPrior, AutoRE, GLiDRE, Ru-LLM) — needed to contextualize the extraction gap.
  - **GRPO stability literature** (DAPO, Dr. GRPO, REINFORCE++) — identifies mechanisms (entropy collapse, std normalization bias) that may explain the observed failures.
  - **NLI faithfulness evaluation** (INFUSE, TRUE) — CED's methodological antecedents.
  - **Contrastive reward methods** — broader context for CED's design.

- **(Major) "Decoupling" may be domain-specific reward hacking, and claims are overscoped.** Reward overoptimization is extensively documented (Gao et al., Goodhart's Law). The paper cites Gao et al. once but doesn't engage substantively. The decoupling finding should be positioned as a domain-specific manifestation, not a wholly novel discovery. Additionally, the QLoRA confound (all GRPO uses 4-bit QLoRA) means the claim cannot be generalized beyond this specific configuration.

- **(Moderate) Large extraction gap inadequately analyzed.** Rel-F1 40.8% vs DREEAM 63.0%. Even 8B achieves only 47.5 (dev). No ablation of extraction with vs. without evidence output, leaving unclear how much of the gap is the evidence generation burden. This limits practical appeal—users face a 17+pp accuracy penalty for evidence.

- **(Moderate) EDCR human validation underpowered.** 100 samples with κ=0.58 is thin. Pearson r=0.28 (weak) with wide confidence interval at n=100. The 45% false positive rate from incomplete DocRED annotations is honestly reported but reduces confidence in EDCR as a standalone metric.

- **(Minor) Single-seed test reporting.** Same concern as R1.

### Questions for Authors

1. R1-RE applies GRPO successfully to sentence-level RE. What is your hypothesis for why GRPO fails at document-level but not sentence-level? Output length? Multi-triple credit assignment?
2. Have you tested GRPO with full-rank FT or bf16 LoRA?
3. Have you considered an SFT-without-evidence ablation to quantify the extraction cost of evidence generation?
4. Does CED use gold evidence labels at scoring time? If so, this limits applicability to training scenarios only.
5. What fraction of triples have empty hard-negative sets (no entity-sharing non-gold sentences)?

### Scores
- **Soundness:** 3/5
- **Excitement:** 2/5
- **Overall:** 2.5/5
- **Confidence:** 4/5

---

## Experiment Coverage Assessment

Comparing the paper against the full experiment design:

| Experiment | Status | Notes |
|------------|--------|-------|
| CED vs flat-NLI ablation | ✅ Covered (Table 4) | Negative result: no significant difference |
| Test set evaluation | ✅ Covered (Table 2) | Marginal significance (p=0.08) |
| EDCR cross-method diagnostic | ✅ Covered (Table 13) | Captures GRPO pathology well |
| DREEAM reproduction | ✅ Covered (Table 12) | Evaluation protocol challenge documented |
| CED-as-reranker | ✅ Covered (Table 6) | Limited benefit, good control |
| Model size ablation | ✅ Covered (Table 16) | Non-monotonic gains documented |
| Re-DocRED extension | ✅ Covered (Table 17) | RSFT gain shrinks with cleaner annotations |
| top_k ablation | ✅ Covered (Table 7) | Small effect, supports "filtering itself is key" |
| GRPO forgetting analysis | ✅ Covered (Tables 8-10) | Comprehensive; missing trajectory figure |
| NLI model ablation | ✅ Covered (Table 5) | No difference, supports saturation claim |
| GRPO G=8 | ✅ Covered (Table 9) | Partial recovery documented |
| DPO experiment | ⚠️ Partially covered (Table 11) | Results present but training details missing |
| EDCR human validation | ✅ Covered (Tables 14-15) | Weak correlation honestly reported |

**Coverage: 12/13 fully covered, 1 partially.** The experimental breadth is a strength; the main gaps are in reporting detail (DPO) and scope qualification (QLoRA confound).

---

## Key Actionable Items for Revision

1. **Retitle/reframe** to emphasize the systematic study, not CED. CED should be presented as one explored scoring function, not the headline contribution.
2. **Run GRPO with bf16 LoRA** to scope the decoupling claim. If it persists → genuine finding about RL+structured IE. If it resolves → QLoRA artifact, still publishable but differently framed.
3. **Report multi-seed test results** (mean ± std across ≥3 seeds).
4. **Specify DPO training details** fully for reproducibility.
5. **Add GRPO training dynamics figure** — this is the paper's strongest visual argument and is currently absent.
6. **Expand related work**: cite R1-RE (GRPO for sentence-level RE), recent LLM DocRE methods, GRPO stability literature. The R1-RE comparison especially would strengthen the decoupling analysis.
7. **Add SFT-without-evidence ablation** to quantify the extraction cost of joint evidence generation.
8. **Scope abstract/intro claims** to match Limitations section's "GRPO+QLoRA" qualification.
