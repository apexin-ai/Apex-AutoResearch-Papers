---
dream_id: dream_20260515T132059
tier: best
overall_score: 3.0 - Findings
timestamp: 2026-05-15T14:16:20.253527+00:00
---

# Dream Review Report: FREIGE

**Paper:** FREIGE: Faithful Evidence Generation for LLM-Based Document-Level Relation Extraction via Contrastive Evidence Discrimination
**Venue:** EMNLP 2026 Main (ACL Rolling Review)
**Review Mode:** Full (2 Reviewers + Roundtable)

---

## Roundtable Summary

| | R1 (Methods+Experiments) | R2 (Novelty+Related Work) | Post-Discussion |
|---|---|---|---|
| Soundness | 3/5 | 3/5 | 3/5 |
| Excitement | 3/5 → 2.5/5 | 3/5 | 3/5 |
| Overall | 3.0 → 2.5 | 3.0 | **3.0 (Findings)** |
| Reproducibility | 3/5 | 4/5 | 3/5 |
| Confidence | 4/5 | 4/5 | 4/5 |

**Consensus outcome: 3.0 — Findings acceptance.** Both reviewers initially scored 3.0. During cross-sharing, R1 dropped to 2.5 after being persuaded by R2's point about CED's non-significance over flat-NLI. R2 held at 3.0, finding R1's QLoRA confound concern reinforcing but not score-changing. The meta-review settles at 3.0: the paper has genuine contributions (task definition, decoupling finding, EDCR metric) that merit Findings publication, but insufficient method novelty and positioning gaps prevent main conference acceptance.

---

## Consolidated Strengths

**S1: Evidence-grounded DocRE as a new task (R1, R2 agree).** The paper credibly claims to be the first LLM-based DocRE system jointly generating relation triples and explicit sentence-level evidence citations. This fills a real gap: encoder methods provide only implicit attention-based evidence, and all prior LLM-based DocRE methods (LMRC, AutoRE, etc.) produce no evidence. The task formulation is well-motivated for KB population, biomedical curation, and RAG provenance.

**S2: Evidence–extraction decoupling is a striking negative finding (R1, R2 strongly agree).** The observation that GRPO drives Evi-F1 to 0.850 while rel_F1 collapses to <0.02 is the paper's most novel empirical contribution. Testing across G=4/G=8, multiple learning rates, and 42 checkpoints with a clear three-phase dynamics description (onset → acceleration → plateau) provides convincing documentation. The G=4 vs G=8 comparison rules out advantage-estimation noise as the root cause. Both reviewers consider this finding independently valuable to the RL-for-NLP community.

**S3: Comprehensive experimental coverage (R1).** 12 tables covering 14 distinct experiments: CED vs flat-NLI ablation, CED usage modes (training vs inference), top-k filtering, NLI model capacity, model scale (1.7B–8B), dataset variant (Re-DocRED), online-offline RL spectrum (GRPO/DPO/SFT/RSFT), cross-method EDCR diagnostic, and human validation. Few ablation gaps remain. Statistical testing (paired bootstrap, p<0.01) is present for key comparisons.

**S4: EDCR fills a genuine evaluation gap (R1, R2 agree).** The demonstration that GRPO achieves Evi-F1=0.850 but EDCR=0.988 illustrates a clear blindspot of standard Evi-F1 to entity-sharing distractors. Human validation (100 samples, 3 annotators, κ=0.72, Pearson r=0.62) provides reasonable support. The metric is simple, interpretable, and captures a failure mode practically relevant to evidence generation.

**S5: Honest self-assessment and transparent limitations (R2).** The paper acknowledges CED's modest advantage, the extraction gap vs encoder methods, and EDCR's proxy nature. This intellectual honesty increases credibility.

**S6: Well-designed GRPO/DPO/RSFT training paradigm comparison (R2).** The full spectrum — GRPO (0.014–0.031) ≪ DPO (0.325) < SFT (0.406) < RSFT (0.468) — adds nuance beyond a binary "RL fails" narrative, showing DPO partially mitigates but does not solve decoupling.

---

## Consolidated Weaknesses

### Major

**W1: CED's advantage over flat-NLI is modest and possibly non-significant (R1 W2, R2 W1 — both agree this is critical).** The paper reports +2.71pp rel_F1 (p=0.007), +2.08pp Evi-F1 (p=0.004), −5.64pp EDCR (p=0.002) for CED vs flat-NLI. R2 raises that in broader experimental context, CED's significance is fragile. The core issue: if CED is positioned as the paper's central contribution (it is in the title and acronym) but provides only marginal improvement over a simpler baseline, the method novelty is thin. The bigger contribution is the RSFT pipeline itself, yet RSFT is existing methodology (Dong et al. 2024). During roundtable, R1 was persuaded this is the paper's most damaging structural weakness.

**W2: GRPO failure analysis is confounded by QLoRA (R1 W1, R2 agrees).** The paper claims "structural incompatibility between on-policy RL and document-level structured IE," but all GRPO experiments use QLoRA (4-bit quantization). QLoRA introduces specific failure modes: KL explosion from quantization noise, rank-limited parameter space. The paper should scope the claim to "GRPO+QLoRA for document-level IE" and prominently discuss the QLoRA confound. A full-rank or bf16 LoRA GRPO experiment would be needed to support the broader claim. Both reviewers agree this scoping is essential.

**W3: Related work has notable gaps (R2 W2, W3 — R1 agrees post-discussion).**
- **R1-RE** (arXiv 2507.04642): GRPO for sentence-level RE — must-cite. Its success at sentence-level creates a natural foil for the document-level failure documented here. Explaining why GRPO works at sentence-level but not document-level would *strengthen* the paper's argument.
- **Recent LLM-based DocRE methods**: RelPrior, Ru-LLM, AutoRE, GLiDRE — missing from related work. Their omission weakens extraction performance positioning.
- **Contrastive reward methods**: (arXiv 2403.07708, EMNLP 2024 contrastive RM) — relevant to CED's design.
- **RSFT theoretical foundations**: "A Minimalist Approach to LLM Reasoning" (arXiv 2504.11343) — directly relevant.
- **DAPO/Dr. GRPO**: Identify entropy collapse and normalization bias in GRPO that may explain document-level failures.

**W4: Large extraction gap with encoder and generative baselines is underexplained (R1 W3).** FREIGE (Qwen3-4B) achieves rel_F1=0.455 vs LMRC (LLaMA-3.1-8B) at 0.607 and DREEAM at ~0.631. The 15pp gap with LMRC deserves quantitative analysis: how much is due to evidence generation burden vs model size (4B vs 8B)? An SFT-without-evidence ablation would isolate the evidence cost. A post-hoc evidence retrieval baseline (extract triples first, retrieve evidence second) would test whether joint generation is necessary.

### Moderate

**W5: CED requires gold evidence at scoring time (R1 W4).** The hard-negative set N(h,t,D) excludes E_gold, requiring gold annotations during CED scoring. This is acceptable for the RSFT pipeline (scoring candidates on training data), but limits applicability to semi-supervised or domain-transfer scenarios. Not discussed in the paper.

**W6: EDCR human validation is small-scale (R1 W5).** 100 samples (25 per method) with a 4-point method-level correlation is statistically thin. Per-sample correlation analysis would be more convincing. The auto-human gap of +6.8pp suggests systematic bias that deserves deeper analysis.

**W7: DPO experiment is underspecified (R1 W8).** No details on preference pair construction, dataset size, or DPO hyperparameters (β, lr, epochs). This makes the DPO result — a key data point in the RL spectrum — hard to evaluate and reproduce.

**W8: Framing tension (R2 W6).** The paper alternates between CED-centric and RSFT-centric narratives. Given CED's modest advantage, the paper should commit to one framing: either "task definition + negative finding (decoupling) + diagnostic metric (EDCR)" as the core contributions, with CED/RSFT as one reasonable instantiation, or strengthen CED's differentiation.

### Minor

**W9: Missing forgetting dynamics visualization (R1 W7, R2 agrees).** Section 4.3 describes a three-phase pattern across 42 checkpoints but provides no figure. A training dynamics plot would be far more convincing than text description alone.

**W10: Connection to reward overoptimization literature is superficial (R2 W5).** CED is framed as "anti-overoptimization" but the paper does not engage with the KL-dependent scaling law framework or Goodhart's Law interpretation.

---

## Key Questions for Authors

1. **Q1 (Critical):** Have you tested GRPO with full-rank fine-tuning (no LoRA) to isolate whether catastrophic forgetting is QLoRA-specific or inherent to on-policy RL for document-level IE?

2. **Q2 (Critical):** R1-RE (arXiv 2507.04642) applies GRPO successfully to sentence-level RE. What is your hypothesis for why GRPO fails at document-level but not sentence-level? Is it output length, multi-triple credit assignment, or something else?

3. **Q3 (Important):** What is the overlap rate between CED-selected and flat-NLI-selected top-1 candidates? If >80%, the marginal signal from the contrastive design is limited to a small subset of documents.

4. **Q4 (Important):** What happens to CED when N(h,t,D) is empty (no entity-sharing non-gold sentences exist)? Does it reduce to flat-NLI? What fraction of triples have empty hard-negative sets?

5. **Q5:** Have you considered training Qwen3-4B SFT without evidence output to quantify the extraction cost of joint evidence generation?

6. **Q6:** What is the inference latency of FREIGE vs DREEAM? Practical deployment considerations are absent.

---

## Missing Experiments / Recommendations

1. **SFT-without-evidence ablation** — isolate the extraction cost of joint evidence generation and contextualize the gap with LMRC.
2. **Post-hoc evidence retrieval baseline** — extract triples with SFT, then retrieve evidence sentences post-hoc (NLI or BM25). Tests whether joint generation is necessary.
3. **Forgetting dynamics figure** — plot rel_F1, Evi-F1, and reward trajectories across training steps for all GRPO configs.
4. **Full-rank GRPO experiment** (even small-scale) — needed to support the "structural incompatibility" claim beyond QLoRA.
5. **Error analysis by relation type/frequency** — determine whether CED's advantage concentrates on specific relation categories.
6. **Confidence intervals across seeds** — Table 1 reports single-number test results; dev set variance (~2pp) is substantial.

---

## Experiment Coverage Assessment

Compared to the full experimental design (review_context.yaml), the paper covers **14/14 planned experiments** across 12 tables. This is comprehensive. However, the paper would benefit from:
- Planned visualization (GRPO forgetting dynamics figure) is described in text but not rendered
- The DREEAM reproduction (plan_004) is present in Table 12 but could include more detail on reproduction fidelity

---

## Final Assessment

| Dimension | Score | Justification |
|-----------|-------|---------------|
| **Soundness** | **3/5** (Acceptable) | Main claims supported but with caveats: CED advantage modest, GRPO analysis confounded by QLoRA |
| **Excitement** | **3/5** (Interesting) | Decoupling finding is genuinely interesting; EDCR is useful. But method novelty (CED) is limited |
| **Overall** | **3.0/5** (Findings) | Genuine contributions in task definition, negative finding, and diagnostic metric. Insufficient method novelty and positioning gaps for main conference |
| **Reproducibility** | **3/5** | Most details provided; DPO setup underspecified; no code/data release mentioned |
| **Confidence** | **4/5** | Both reviewers are familiar with DocRE, RLHF, and evaluation methodology |

### Meta-Review Justification

FREIGE makes three genuine contributions: (1) defining evidence-grounded DocRE as a task and providing the first LLM-based system for it, (2) documenting the evidence–extraction decoupling phenomenon under GRPO+QLoRA — a striking negative finding with implications for the RL-for-NLP community, and (3) proposing EDCR as a diagnostic metric that captures a failure mode invisible to standard Evi-F1. These contributions are sufficient for Findings.

However, the paper falls short of main conference acceptance for three reasons: (a) the core method contribution (CED) provides only modest, potentially fragile improvements over the simpler flat-NLI baseline — the real contribution is the RSFT pipeline, which is existing methodology; (b) the GRPO failure analysis, while thorough, is confounded by QLoRA and the claims need scoping; (c) the related work section has notable gaps (R1-RE, recent LLM DocRE methods, contrastive reward literature) that weaken positioning.

**Path to main conference:** (1) Replicate decoupling under full-rank/bf16 LoRA fine-tuning to support the broader "RL vs structured IE" claim; (2) Either strengthen CED's differentiation from flat-NLI or reframe the paper around the task + negative finding + metric; (3) Expand related work substantially; (4) Add the forgetting dynamics figure and SFT-without-evidence ablation.

---

## Roundtable Process Record

- **Step 1 (Independent):** R1 scored 3.0 (Findings), R2 scored 3.0 (Findings)
- **Step 2 (Cross-sharing):** R1 was persuaded by R2's CED non-significance argument and dropped to 2.5. R2 found R1's QLoRA confound point reinforcing but maintained 3.0.
- **Step 3 (Convergence):** Both reviewers agree on: (i) task contribution genuine, (ii) decoupling finding most novel, (iii) CED advantage modest, (iv) GRPO claims need QLoRA scoping, (v) related work gaps. Divergence: R1 weights CED weakness more heavily (2.5), R2 weighs the package of contributions as sufficient for Findings (3.0).
- **Step 4 (Synthesis):** Final consensus at 3.0 (Findings). The paper's three contributions — task definition, negative finding, diagnostic metric — collectively reach Findings threshold despite limited method novelty. R1's downward revision is partially counterbalanced by the paper's comprehensive experimental coverage and honest self-assessment.
