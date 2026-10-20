---
dream_id: dream_20260515T132059
tier: median
overall_score: 2.5/5 — Leaning Reject (Main); Recommend Findings
timestamp: 2026-05-15T14:25:43.822210+00:00
---

# DREAM Review Report: FREIGE

**Paper**: FREIGE: Faithful Evidence Generation for Document-Level Relation Extraction via Rejection Sampling Fine-Tuning  
**Venue**: EMNLP 2026 Main (via ACL Rolling Review)  
**Review Mode**: Full (2 Reviewers + Roundtable)  
**Date**: 2026-05-15

---

## 1. Paper Summary

FREIGE proposes the first LLM-based document-level relation extraction (DocRE) system that jointly generates relation triples and sentence-level evidence citations. The method uses Rejection Sampling Fine-Tuning (RSFT): an SFT-trained Qwen3-4B generates N=8 candidate outputs per document, a Contrastive Evidence Discrimination (CED) scorer based on DeBERTa-v3-base NLI ranks candidates by evidence quality using document-internal hard negatives, and only the top-1 candidate is retained for further fine-tuning. On DocRED test, FREIGE achieves rel_F1=43.2% (+3.2pp over SFT, p<0.01) and joint Evi-F1=32.2%. The paper also documents "evidence-extraction decoupling" under GRPO+QLoRA (evidence quality rises while extraction collapses), shows this worsens with larger group sizes (G=8 vs G=4), and introduces EDCR (Evidence Distractor Citation Rate) as a diagnostic metric validated through human annotation (r=0.44, method-level rank concordance=1.0).

---

## 2. Strengths

### S1: Credible and well-scoped "first" claim (R1+R2 consensus)
No prior LLM-based DocRE system jointly generates (head, relation, tail, [evidence sentences]). Encoder methods (DREEAM, SAIS) derive evidence from attention weights (implicit, not directly auditable). LLM methods (LMRC, AutoRE) produce triples only. The task definition fills a genuine gap relevant to KB population, biomedical curation, and RAG provenance. The claim is appropriately scoped to DocRED.

### S2: Thorough training paradigm comparison (R1+R2 consensus)
The systematic GRPO → DPO → SFT → RSFT spectrum (Table 5) is more insightful than typical ablation studies. The ordering (GRPO collapse < DPO degradation < SFT baseline < RSFT improvement) leads to the nuanced insight that the problem is contrastive/reward-based losses in general, not the online/offline distinction. This is a genuinely useful empirical contribution.

### S3: Evidence-extraction decoupling is the paper's strongest empirical finding (R1+R2 consensus)
The observation that GRPO drives evi_F1 to 0.835–0.862 while rel_F1 collapses to <0.08 is striking. The G=4 vs G=8 comparison is particularly valuable: G=8 peaks earlier (step 40) and collapses faster, ruling out the "insufficient exploration" counter-argument and connecting to reward overoptimization theory (Gao et al. 2023). The full checkpoint trajectory (Table 4) with monotonically increasing reward alongside collapsing extraction is a compelling empirical demonstration.

### S4: Well-designed ablation structure (R1)
The paper includes ablations along multiple axes: CED vs flat-NLI scoring (Table 2), top-k filtering strictness (Table 8), NLI model capacity (Table 12), CED as training vs inference reranker (Section 5.6), model size (Table 9, 1.7B/4B/8B), and dataset variant (Table 10, Re-DocRED). Each isolates a specific design choice. The CED-reranker experiment is a particularly clever control separating the value of CED as a signal from RSFT as a paradigm.

### S5: Intellectual honesty throughout (R2)
The paper is transparent about CED's non-significant advantage over flat-NLI (p=0.12/0.28/0.09), the absolute performance gap to encoder methods (43.2% vs 62.8%), EDCR's moderate sample-level correlation (r=0.44), and dev-to-test degradation (3.6pp vs 0.6pp for SFT). This level of self-assessment substantially increases credibility.

### S6: EDCR captures a real evaluation blind spot (R1+R2 consensus)
The demonstration that GRPO achieves high evi_F1 (~0.835–0.862) but EDCR >0.92 illustrates a clear failure mode invisible to standard Evi-F1. The metric is simple, interpretable, and the cross-method diagnostic zones (collapse >85%, baseline ~71%, filtered 64–67%) provide actionable diagnostic information.

---

## 3. Weaknesses

### W1 [Major]: CED is not a novel method and does not significantly outperform the simpler alternative (R2 primary, R1 concurs after correction)
The contrastive margin (p_entail(cited) − max p_entail(distractor)) is a standard pattern in retrieval, reranking, and faithfulness evaluation. More critically, CED does NOT significantly outperform flat-NLI scoring on any metric: evi_F1 p=0.12, rel_F1 p=0.28, EDCR p=0.09 (Table 2). The 78% candidate overlap between the two scorers indicates minimal differentiation. Despite being named in the title, acronym (FREIGE), and 6 of 12 tables, CED's actual contribution is marginal. The paper's Discussion reframes CED as "one possible scoring function," but the rest of the paper reads as CED-centric, creating a title-contribution mismatch.

**Impact**: This means the primary methodological contribution reduces to "RSFT applied to DocRE," which is also not architecturally novel (see W2). The contribution budget shifts to task definition + negative findings + diagnostic metric.

### W2 [Major]: RSFT is existing methodology applied to a new domain (R2 primary)
Rejection sampling fine-tuning / ReST is well-established for math reasoning (Dong et al. 2024, RAFT), code generation (Singh et al. 2024, ReST-EM), and dialogue (Gulcehre et al. 2023). The paper's title centers "Rejection Sampling Fine-Tuning" as the solution, but there is no architectural or algorithmic innovation in the RSFT pipeline — it is a straightforward generate → score → filter → retrain loop. Applying it to DocRE is a valid application contribution, but it should not be framed as a methodological advance.

### W3 [Major]: Evidence-extraction decoupling is confounded by QLoRA (R1+R2 consensus)
All GRPO experiments use 4-bit QLoRA (rank=64). The paper claims "structural incompatibility" between online RL and document-level IE, but never tests full fine-tuning or even higher-rank/bf16 LoRA as controls. The Limitations section appropriately scopes to "GRPO+QLoRA," but the abstract and introduction use unqualified language like "online reward optimization (GRPO) with evidence-quality rewards causes catastrophic evidence-extraction decoupling." A full fine-tuning or bf16 LoRA experiment would be needed to determine whether this is a QLoRA artifact or a genuine RL-for-IE phenomenon. Without this control, the claim's generalizability is limited.

### W4 [Major]: Significant related work gaps (R2 primary)
The "RL for Information Extraction" paragraph (Section 2) states "Prior work has applied RL to IE tasks with mixed results" without citing a single specific paper. Critical omissions include:
- **R1-RE** (arXiv 2507.04642): GRPO for sentence-level RE that *succeeds* — creates a natural foil (why does GRPO work for sentence-level but fail for document-level?), which would actually strengthen the paper's argument
- **Recent LLM-based DocRE methods**: RelPrior (arXiv 2511.08143), Ru-LLM (NLPCC 2025), AutoRE (arXiv 2403.14888), GLiDRE (arXiv 2508.00757) — while none produce evidence (strengthening the "first" claim), their omission leaves the extraction gap (43.2% vs LMRC's 60.7%) undercontextualized
- **GRPO stability literature**: DAPO (NeurIPS 2025), Dr. GRPO (COLM 2025) — mechanisms that may explain document-level IE failures
- **NLI-based faithfulness evaluation**: INFUSE (EACL 2024), TRUE benchmark — CED's methodological antecedents

### W5 [Moderate]: "Evidence-extraction decoupling" may be a special case of well-known reward hacking (R2 primary, R1 concurs)
Reward hacking/overoptimization — where optimizing a proxy reward degrades the true objective — is extensively documented (Gao et al. 2023, Skalse et al. 2022). The specific manifestation in DocRE is a domain-specific instance of this general phenomenon. The paper should acknowledge this lineage more explicitly rather than presenting it as a wholly novel discovery. Additionally, the paper mentions (in the GRPO analysis) that the decoupling occurs across all reward types including extraction-only rewards — if even extraction-only reward fails under GRPO+QLoRA, the issue may be GRPO+QLoRA instability for structured generation broadly, not specifically evidence-vs-extraction misalignment. This partially undermines the "decoupling" framing.

### W6 [Moderate]: EDCR human validation is underpowered (R1 primary)
The human validation uses only 100 samples with 2 annotators (κ=0.62). With only 3–4 methods at the method level, "perfect method-level rank concordance" is not statistically remarkable (random chance ≈ 1/24 for 4 methods, 1/6 for 3 methods). The sample-level correlation r=0.44 has a wide confidence interval at n=100. EDCR systematically overestimates the distractor rate by 8.5pp, attributed to incomplete DocRED gold annotations (~14% false distractors). While the paper honestly reports these limitations, the validation falls short of establishing EDCR as a reliable metric beyond directional diagnostics.

### W7 [Moderate]: Large extraction gap limits practical impact (R1+R2 consensus)
FREIGE achieves rel_F1=43.2% (test) vs DREEAM 62.8% and LMRC 60.7%. Even the 8B variant (rel_F1=48.8% dev) falls well short. The paper correctly decomposes the Evi-F1 gap into extraction recall vs evidence quality (conditional Evi-F1: 80% vs ~93%), but the extraction gap itself is underexplained. LMRC uses a similar paradigm (LLaMA3.1-8B) and achieves 60.7% without evidence generation — a direct comparison or ablation (same model, with vs without evidence output) would clarify how much of the gap is due to the evidence generation burden vs other factors.

### W8 [Moderate]: Dev-to-test degradation asymmetry (R1 primary)
RSFT shows 3.6pp dev-to-test degradation in rel_F1 (46.8→43.2 dev→test) vs only 0.6pp for SFT (40.6→40.0). This suggests indirect overfitting through the CED scoring pathway — RSFT candidates are generated from training documents, and CED scoring may implicitly favor patterns that correlate with dev-set characteristics. While the test improvement remains significant (p<0.01), this 6x relative degradation ratio warrants investigation and is not adequately analyzed.

### W9 [Minor]: Single-seed reporting for main results (R1)
The paper reports results for "best RSFT configuration (3 epochs, alpha=128, seed=43)" based on dev-set selection. Table 2 shows three different configs with CED (rel_F1: 44.49, 46.83, 44.93), indicating meaningful variance across seeds/configs. Mean ± std across seeds should be reported for the main RSFT results to avoid the appearance of cherry-picking.

---

## 4. Claims-Evidence Alignment

| # | Claim | Evidence in Paper | Verdict |
|---|-------|-------------------|---------|
| C1 | First LLM-based DocRE with verifiable evidence | No prior work cited/found; results across 3 scales and 2 datasets | **Supported** — genuine novelty in task definition |
| C2 | RSFT +3.2pp test rel_F1 over SFT (p<0.01) | Table 1 (test), p-value reported | **Supported** — but single seed, 3.6pp dev-to-test degradation noted |
| C3 | CED scoring as key component | Table 2: CED vs flat-NLI NOT significant (p=0.12/0.28/0.09); 78% candidate overlap | **Weakly supported** — consistent direction (+0.49/+0.75pp) but no statistical significance; CED's value may lie only in ranking (top-k selection) rather than scoring precision |
| C4 | Evidence-extraction decoupling in GRPO | Tables 3–4: comprehensive trajectory data; G=4 vs G=8 comparison; reward-rel_F1 negative correlation r=−0.68 | **Partially supported** — convincing within GRPO+QLoRA scope, but generalizability beyond QLoRA is uncertain; all reward types fail (including extraction-only), which suggests broader GRPO+QLoRA instability rather than evidence-specific decoupling |
| C5 | EDCR as validated diagnostic metric | Table 7: r=0.44, κ=0.62, method-level concordance=1.0; Table 6: clear zone separation | **Partially supported** — directionally useful, but modest sample-level correlation, systematic overestimate (+8.5pp), and underpowered validation (n=100) |
| C6 | Data curation > reward/preference learning for structured IE | Table 5: RSFT > SFT > DPO > GRPO; Section 5.4 analysis | **Supported** — well-demonstrated for this task/model combination |

---

## 5. Experiment Coverage Assessment

Comparing paper content against the full experiment design (review_context.yaml, 13 planned experiments):

| Experiment | Plan ID | In Paper? | Coverage Quality |
|-----------|---------|-----------|-----------------|
| CED vs flat-NLI RSFT ablation | plan_001 | ✓ Table 2 | Full — 3 configs, bootstrap p-values |
| Test set evaluation | plan_002 | ✓ Table 1 | Full — 3 methods on CodaLab |
| EDCR cross-method diagnostic | plan_003 | ✓ Table 6 | Full — 7 methods, zone classification |
| DREEAM baseline reproduction | plan_004 | ✓ Table 11 | Full — <1pp gap, validates protocol |
| CED-as-reranker | plan_005 | ✓ Section 5.6 | Adequate — results reported but no table |
| Model size ablation (1.7B/8B) | plan_006 | ✓ Table 9 | Full — 3 sizes with consistent gains |
| Re-DocRED extension | plan_007 | ✓ Table 10 | Full — ceiling effect correctly noted |
| Top-k ablation | plan_008 | ✓ Table 8 | Full — quality > quantity confirmed |
| GRPO forgetting analysis | plan_009 | ✓ Tables 3–4, Section 5.3 | Good — trajectory data shown, but figures described in context not in paper |
| NLI model ablation | plan_010 | ✓ Table 12 | Full — base vs large, bottleneck identified |
| GRPO G=8 experiment | plan_011 | ✓ Tables 3–4 | Full — decisive for ruling out "G too small" |
| DPO+CED experiment | plan_012 | ✓ Table 5 | Full — fills spectrum |
| EDCR human validation | plan_013 | ✓ Table 7 | Full — all statistics reported |

**Coverage**: 13/13 experiments covered. All planned experiments are represented in the paper. The paper demonstrates comprehensive experimental coverage.

---

## 6. Novelty Assessment

| Component | Novelty | Rationale |
|-----------|---------|-----------|
| Evidence-grounded DocRE task definition | **Medium-High** | Genuine gap; first to combine extraction + evidence in LLM-based DocRE |
| CED scoring function | **Low** | Standard contrastive NLI; not significantly better than flat-NLI |
| RSFT for DocRE | **Low** | Existing methodology (RAFT/ReST, mature since 2023) applied to new domain |
| Evidence-extraction decoupling finding | **Medium-High** | Novel empirical observation in IE, with good G=4/G=8 evidence; weakened by QLoRA confound and being a domain instance of reward hacking |
| EDCR metric | **Medium** | Identifies real blind spot; formula is trivial but observation is valuable |
| GRPO/DPO/RSFT spectrum analysis | **Medium** | Well-designed comparison; contrastive-loss insight is useful for the community |

**Overall novelty**: The paper's novelty is concentrated in the task definition and negative findings rather than in the method. The method-level contributions (CED, RSFT) are applications of existing techniques with limited differentiation.

---

## 7. Actionable Revision Suggestions

### Must-fix for resubmission:
1. **Add QLoRA qualifier to all GRPO claims** in abstract and introduction, not just Limitations
2. **Expand "RL for IE" related work** substantially — cite R1-RE (GRPO for sentence-RE), REAR, and other RL-for-IE papers; discuss why sentence-level succeeds where document-level fails
3. **Add recent LLM-based DocRE baselines** (RelPrior, Ru-LLM, AutoRE) to contextualize the extraction gap
4. **Run GRPO without QLoRA** (full FT or bf16 LoRA) to determine if decoupling is a QLoRA artifact or a genuine phenomenon
5. **Report multi-seed mean±std** for main RSFT results (at least 3 seeds)
6. **Reframe CED honestly throughout** — either strengthen differentiation or pivot the narrative to "RSFT pipeline (scorer-agnostic) + decoupling finding + EDCR"

### Should-fix:
7. **Add SFT-without-evidence ablation** to measure the evidence generation tax on extraction
8. **Analyze dev-to-test degradation** — does CED filtering create implicit data leakage?
9. **Discuss CED's dependence on gold evidence labels** (Eq. 1 uses gold evidence set for hard negatives)
10. **Acknowledge reward hacking lineage** more explicitly in Section 5.3/6
11. **Expand EDCR human validation** to ≥200 samples if possible

### Nice-to-have:
12. Per-relation-type analysis of CED vs flat-NLI
13. Discussion of CED in the context of citation precision evaluation (FactScore, attributed QA)
14. Engagement with GRPO stability literature (DAPO, Dr. GRPO)

---

## 8. Consolidated Scores

| Dimension | R1 | R2 | Converged | Rationale |
|-----------|----|----|-----------|-----------|
| Soundness | 3 | 3 | **3/5** | Experiments are thorough but QLoRA confound limits the GRPO claim; CED non-significance weakens the method; dev-to-test degradation insufficiently analyzed |
| Excitement | 3 | 3 | **3/5** | Task definition is valuable; decoupling finding is interesting; but limited method novelty and large extraction gap dampen excitement |
| Overall Assessment | 3.0 | 2.5 | **2.5/5** | After cross-sharing, R1 concurs with R2's novelty concerns and the related work gaps are substantial; contribution package (task + negative finding + diagnostic metric) is suitable for Findings but falls short of Main at ~22-25% acceptance rate |
| Confidence | 4 | 4 | **4/5** | Both reviewers well-calibrated on the task area |

---

## 9. Overall Assessment

**Recommendation: 2.5/5 — Leaning Reject for EMNLP 2026 Main; recommend Findings track**

### Justification

FREIGE makes a credible "first" claim for evidence-grounded LLM-based DocRE and documents a genuinely interesting negative finding about GRPO+QLoRA for document-level structured IE. The experimental coverage is comprehensive (13 experiments, ablations across scoring function, filtering strictness, NLI model, training paradigm, model size, and dataset). The honest reporting of CED's non-significance, the extraction gap, and EDCR's limitations is commendable.

However, the paper faces three interconnected problems that prevent recommendation for Main:

1. **Limited method novelty**: CED is a standard contrastive NLI scorer that does not significantly outperform flat-NLI (p>0.05 on all metrics). RSFT is existing methodology with no architectural innovation. The contribution is the application to a new task, not the method.

2. **Under-scoped key claim**: The evidence-extraction decoupling finding is established only for GRPO+QLoRA but presented more broadly in the abstract/introduction. Without a full-FT or bf16 LoRA control, the claim cannot be distinguished from a QLoRA-specific artifact. The finding that extraction-only rewards also fail further complicates the "decoupling" narrative — it may be GRPO+QLoRA instability for structured generation generally.

3. **Significant related work gaps**: The "RL for IE" section cites no specific papers. Critical omissions include R1-RE (GRPO for sentence-level RE — a direct foil) and multiple recent LLM-based DocRE methods. This weakens the paper's positioning and suggests incomplete literature coverage.

The paper's contribution package — task definition, thorough negative findings, EDCR metric — represents solid empirical work appropriate for the EMNLP Findings track. With the revisions outlined above (especially the QLoRA control experiment, expanded related work, and honest CED reframing), this could be strengthened to Main quality.

---

*Review conducted by: R1 (Methods + Experiments) and R2 (Novelty + Related Work)*  
*Roundtable: 4-step protocol (Independent → Cross-share → Convergence → Consolidated)*