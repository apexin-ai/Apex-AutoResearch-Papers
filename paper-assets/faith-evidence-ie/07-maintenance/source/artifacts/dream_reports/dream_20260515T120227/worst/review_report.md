---
dream_id: dream_20260515T120227
tier: worst
overall_score: 2.5 — Leaning Reject
timestamp: 2026-05-15T12:53:29.722003+00:00
---

# Dream Review Report — EMNLP 2026 Main

**Paper**: "Why Online RL Catastrophically Fails for Structured Information Extraction, and What Works Instead"

**Review Mode**: Full (2-Reviewer Roundtable)
**Venue**: EMNLP 2026 Main (via ACL Rolling Review)
**Scoring Scale**: ARR 2025+ (Soundness 1-5, Excitement 1-5, Overall 1-5 with half-points)

---

## Step 1: Independent Reviews

### Reviewer 1 (R1): Methods + Experiments

**Summary**: The paper studies online RL (GRPO) for document-level relation extraction with evidence generation, finding universal failure across 3 reward functions. It proposes RSFT with NLI-based filtering as an alternative (+3.7 F1 on test) and introduces EDCR, a diagnostic metric for entity-sharing distractor citations.

**Strengths**:
- Comprehensive GRPO failure analysis with 3 fundamentally different reward functions × multiple learning rates — this breadth convincingly rules out "just tune harder" objections
- The evidence–extraction decoupling phenomenon (evi_F1 → 0.850 while rel_F1 < 0.02 under lr=5e-6) is a genuinely striking finding that reveals how compositional structured outputs can be differentially optimized by RL
- Thorough ablation suite: model size (3 scales), NLI model capacity, top-k filtering, Re-DocRED extension, CED-as-reranker — the paper leaves few stones unturned
- Commendable honesty in reporting negative results: CED vs flat-NLI not statistically significant (p=0.08/0.38/0.12), large dev→test degradation, cross-protocol comparison caveats
- EDCR is cleanly defined (Eq. 2) and the cross-method diagnostic table (Table 7) effectively demonstrates its orthogonality to Evi-F1

**Weaknesses**:

**W1 (Major): CED is not validated as a contribution.** The paper's method section devotes significant space to Contrastive Evidence Discrimination (CED), and "CED" appears in the method name throughout (RSFT+CED). Yet the paper's own ablation (Table 4) shows CED vs flat-NLI is not statistically significant on any metric (p = 0.08, 0.38, 0.12). The candidates selected by CED and flat-NLI overlap at Jaccard ~0.75. The paper itself concludes "the benefit comes from rejection sampling itself" — but then why is CED presented as a method contribution? This creates a disconnect between the method presentation and the empirical findings.

**W2 (Major): GRPO configuration may be undertested.** Group size G=4 is unusually small for GRPO. Standard practice in reasoning tasks uses G=8–16+. The paper's own theoretical argument (§5.2) is that GRPO advantage estimation degrades with high structural variance across rollouts — but with only 4 rollouts, the advantage estimate is inherently noisy regardless of structural variance. The paper should test G=8 or G=16 to disentangle "GRPO fundamentally fails for structured IE" from "G=4 is insufficient for this task."

**W3 (Major): Severe dev→test degradation undermines RSFT's practical value.** The 7.4pp rel_F1 drop (dev 0.466 → test 0.392) is roughly double the typical encoder method degradation (DREEAM ~3.5pp). The paper attributes this to "shared distributional characteristics" between train/dev splits but does not investigate or mitigate. This suggests RSFT+CED may be overfitting to the training distribution. The 15.8% relative degradation rate raises serious questions about whether the dev set improvements would transfer to real-world deployments.

**W4 (Moderate): Cross-protocol Evi-F1 comparison is fundamentally misleading.** While the paper adds caveats (Table 6 caption), it still prominently reports a ~20pp Evi-F1 advantage over DREEAM. The generative approach (explicit sentence index generation) vs. attention-based extraction are incommensurable evaluation protocols. The reproduced DREEAM dev Evi-F1 (60.8) exceeding its reported test value (57.34) by 3.5pp further suggests evaluation pipeline differences. This comparison should be demoted or removed entirely.

**W5 (Moderate): Extraction F1 trails encoder SOTA by ~24pp.** RSFT+CED achieves rel_F1 = 0.392 on test vs. DREEAM's 0.630. The paper frames this as "the extraction–evidence trade-off inherent in the generative paradigm," but this is a massive gap. The paper essentially demonstrates that generative evidence-grounded DocRE works much worse at extraction than encoder methods, while achieving higher Evi-F1 under an incomparable evaluation protocol.

**W6 (Minor): Model size ablation reveals non-robust gains.** RSFT gain is +2.6pp (1.7B), +6.0pp (4B), +1.7pp (8B) — non-monotonic with 4B as a coincidental sweet spot. This undermines claims of methodological robustness. The paper suggests "LoRA rank/lr should be tuned per model size," which means the 4B results may reflect lucky hyperparameter alignment rather than method strength.

**W7 (Minor): Only LoRA training evaluated.** All experiments use LoRA (α=128, r=64). GRPO failure might be LoRA-specific (gradient noise from low-rank approximation compounding with advantage estimation noise). A full fine-tuning control would strengthen the "structural incompatibility" claim.

**Questions for Authors**:
1. What happens with GRPO at G=8 or G=16? Does the failure pattern persist?
2. Can you provide learning curves showing the training dynamics of RSFT to verify it's not also showing early signs of the same degradation?
3. Have you considered held-out validation during RSFT training to detect overfitting?
4. What is the inference latency of your generative approach vs. DREEAM/SAIS?

**R1 Scores**:
- Soundness: 3 (Acceptable — conclusions generally follow from evidence, but CED claim is unsupported and GRPO undertested)
- Excitement: 3 (Ambivalent — decoupling finding is interesting, but overall practical contribution is limited)
- Overall: 2.5 (Leaning reject)
- Confidence: 4/5

---

### Reviewer 2 (R2): Novelty + Related Work

**Summary**: The paper makes a negative finding about GRPO for structured IE, proposes RSFT as an alternative, and introduces EDCR as a diagnostic metric. The framing emphasizes the failure analysis as the core contribution, with RSFT and EDCR as secondary contributions.

**Strengths**:
- Timely and relevant: the NLP community is enthusiastically adopting GRPO/RL for reasoning tasks, and a systematic negative result for structured IE fills an important gap
- The evidence–extraction decoupling phenomenon is genuinely novel — I'm not aware of prior work documenting this specific failure mode where one output component improves while another collapses under RL
- Writing is clear, well-structured, and refreshingly honest. The limitations section is substantive and the paper doesn't try to hide its weaknesses
- The reframing from "CED as method innovation" to "why does GRPO fail, and what works instead" is the right narrative choice given the empirical results
- EDCR provides a useful conceptual lens even if the metric itself needs further validation

**Weaknesses**:

**W1 (Major): Title claims "Online RL" but only tests GRPO.** The title says "Why Online RL Catastrophically Fails" but the paper only evaluates one online RL algorithm (GRPO). PPO, REINFORCE, and other on-policy methods are not tested. The failure might be GRPO-specific (e.g., group-relative advantage estimation) rather than fundamental to online RL. The generalization from "GRPO fails" to "online RL fails" is unwarranted without broader algorithmic coverage.

**W2 (Major): RSFT is not methodologically novel.** Rejection sampling fine-tuning (ReST/RSFT) is well-established in the literature (Yuan et al., Singh et al., Gulcehre et al.). Applying it to DocRE with NLI filtering is a straightforward application. The paper's own ablations show that the specific scoring function doesn't matter — any reasonable filter works. This reduces the RSFT contribution to "we tried RSFT on a new task and it worked," which has limited novelty.

**W3 (Major): Missing critical baselines.** The paper compares GRPO (online) vs. RSFT (offline) but omits important intermediate approaches:
- **DPO/KTO**: offline preference-based methods that avoid GRPO's advantage estimation issues but still do reward-based training. These would help locate where exactly online RL breaks.
- **PPO with value network**: the most established RL algorithm for NLP. GRPO's elimination of the value network might be the problem, not online RL per se.
- **Iterative RSFT / online RSFT**: multi-round rejection sampling from an updated policy, bridging online and offline.
- **Best-of-N at inference time**: a stronger version of the reranker baseline with larger N.
Without these baselines, the paper's narrative of "online RL fails → use offline RL" has a gap in the middle.

**W4 (Moderate): Theoretical connection to LongRLVR is informal.** Section 5.2 claims to "connect" the failure to LongRLVR's gradient vanishing analysis, but the connection is purely verbal — the paper doesn't verify that the specific conditions for gradient vanishing (as formalized in LongRLVR) actually hold in this setting. It's plausible but unverified speculation. A formal analysis (e.g., measuring advantage variance across rollouts, comparing structural diversity metrics) would strengthen this significantly.

**W5 (Moderate): EDCR lacks human validation.** EDCR is defined as an automatic metric but never validated against human judgments of evidence quality. The weak correlation with Evi-F1 (r=-0.42) could indicate that EDCR captures a genuine orthogonal dimension, or it could indicate noise. Without human annotation study, we can't distinguish. A small-scale human evaluation (100 examples, annotators judge whether each cited evidence sentence genuinely supports the relation) would be sufficient.

**W6 (Moderate): Related work gaps.** 
- No discussion of RL for other structured prediction tasks (NER, parsing, structured summarization). Are there similar negative results?
- No mention of reward hacking / reward over-optimization literature, which is directly relevant to the reward↑ + F1↓ pattern
- No comparison with recent structured generation approaches (constrained decoding, grammar-based generation) that might address the evidence quality issue differently
- Missing citation of R1-RE (EMNLP 2025) or similar recent generative DocRE work

**W7 (Minor): Single dataset family limits generalizability.** All experiments use DocRED/Re-DocRED. TACRED, SciERC, DWIE, or BioRED would test whether findings generalize beyond WikiData-style relations. The GRPO failure could be DocRED-specific (e.g., related to its annotation noise or entity density).

**Questions for Authors**:
1. Have you tried PPO or DPO? Even a small-scale experiment would substantially strengthen the "online RL fails" claim.
2. What does the advantage variance look like across GRPO rollouts? You hypothesize high structural variance — can you measure it?
3. Does EDCR correlate with human judgments of evidence quality? Even a small study (50-100 examples) would help.
4. How does the GRPO failure interact with generation length? Do collapsed models produce shorter/longer outputs?

**R2 Scores**:
- Soundness: 3 (Acceptable — GRPO analysis is sound within its scope, but overclaims in generalization)
- Excitement: 3 (Ambivalent — decoupling finding is interesting but overall novelty is limited)
- Overall: 2.5 (Leaning reject)
- Confidence: 4/5

---

## Step 2: Cross-Sharing

**R1 → R2**: R1 highlights that GRPO uses only G=4, which directly undermines the paper's own theoretical argument about advantage estimation noise. R1 also notes the LoRA-only confound — GRPO failure might be amplified by low-rank gradient approximation rather than being fundamental to online RL. R2 agrees this strengthens W1 (title overclaims) and adds it as supporting evidence.

**R2 → R1**: R2 points out the missing DPO/PPO baselines, which R1 agrees would help diagnose whether the failure is GRPO-specific or online-RL-general. R2's observation about reward hacking literature being missing is relevant to R1's experimental analysis — the reward↑ + F1↓ pattern in Table 1 is a textbook case of reward over-optimization, and the paper doesn't connect to that literature.

**Joint observation**: Both reviewers note that the paper's strongest contribution (GRPO failure + decoupling) is undermined by overclaiming in the title and insufficient algorithmic breadth, while the two positive contributions (RSFT, EDCR) are either not novel (RSFT) or not validated (EDCR). The paper would be significantly stronger if it narrowed its claims to "GRPO fails for DocRE" and provided deeper analysis (advantage variance measurements, formal connection to gradient vanishing conditions).

---

## Step 3: Convergence

**Consensus Strengths**:
1. **Evidence–extraction decoupling** under slow-lr GRPO is a genuinely novel and striking finding (evi_F1 → 0.850 while rel_F1 < 0.02). This alone has community value.
2. **Systematic negative result** across 3 reward types × multiple lr is a thorough failure analysis within the tested scope.
3. **Honest, transparent reporting** — the paper does not hide its weaknesses (CED not significant, large dev-test gap, cross-protocol comparison caveats).
4. **EDCR** as a concept identifies a real blind spot in Evi-F1, even if the metric needs further validation.
5. **Ablation thoroughness** — model size, NLI model, top-k, Re-DocRED, reranker — covers many axes.

**Consensus Weaknesses** (ranked by severity):

1. **(Critical) Title and claims overclaim the scope of evidence.** "Online RL" → only GRPO tested. "What Works Instead" → standard RSFT, not novel. The paper should claim "GRPO fails for DocRE" and present RSFT as a known fallback, not a contribution.

2. **(Major) Missing intermediate baselines (DPO, PPO) create a narrative gap.** The paper positions a binary online/offline dichotomy but doesn't test methods that lie between GRPO and RSFT. Without these, the diagnosis of *why* online RL fails remains speculative.

3. **(Major) CED is not a validated contribution.** p=0.08/0.38/0.12 across all metrics; Jaccard overlap ~0.75 with flat-NLI. The paper should either (a) drop CED as a contribution and reframe around generic RSFT, or (b) provide additional evidence for CED's value (e.g., on harder datasets with more ambiguous distractors).

4. **(Major) GRPO undertested: G=4 is too small; LoRA-only is a confound.** The paper's own theory (§5.2) argues advantage estimation fails with high structural variance — G=4 makes this trivially true. Larger group sizes might partially mitigate. LoRA's low-rank gradient approximation adds another confound.

5. **(Moderate) Severe dev→test degradation (-7.4pp rel_F1).** Nearly double the typical encoder method degradation. Suggests distributional overfitting. Not investigated or mitigated.

6. **(Moderate) Cross-protocol Evi-F1 comparison with DREEAM/SAIS.** Despite caveats, the ~20pp gap is prominently displayed. This comparison is unreliable and misleads about actual progress.

7. **(Moderate) EDCR not validated by human evaluation.** Without human annotation, the metric's value is uncertain.

8. **(Minor) Single dataset family; single model family.** Limits generalizability of all findings.

**Score Convergence**:
Both reviewers converge on Overall 2.5 (Leaning Reject). The paper has a genuinely interesting core finding (decoupling phenomenon) but overclaims its scope, presents a non-novel method (RSFT) as a contribution, and fails to validate its proposed scoring mechanism (CED). The gap between what the paper promises in the title/abstract and what it delivers in the experiments is too large for acceptance at a top venue.

---

## Step 4: Consolidated Assessment

### Overall Recommendation: **2.5 — Leaning Reject**

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Soundness | 3 | Core GRPO experiments are competently executed within scope. Statistical testing is appropriate. But G=4 and LoRA-only confounds weaken the "fundamental failure" claim. CED contribution is empirically unsupported. |
| Excitement | 3 | Evidence–extraction decoupling is a striking finding worthy of publication. But RSFT is not novel, EDCR needs validation, and overall the paper's positive contributions don't match the ambition of its framing. |
| Overall | 2.5 | Leaning reject. The paper has one strong contribution (decoupling phenomenon) wrapped in two weak ones (RSFT as "what works," EDCR without validation) and overclaims its scope. |
| Confidence | 4/5 | Both reviewers are knowledgeable about RL for NLP and document-level IE. |

### Key Reasons for Score

**Why not accept (3.5+)**:
- The title promises "why online RL fails" but only tests one algorithm (GRPO) with small group size (G=4) and LoRA-only training
- The "what works instead" (RSFT) is a known technique; the proposed scoring function (CED) is not validated
- 24pp extraction gap vs. encoder SOTA and 7.4pp dev-test degradation limit practical impact
- Missing intermediate baselines (DPO, PPO) leave the online/offline analysis incomplete

**Why not strong reject (1.5)**:
- The evidence–extraction decoupling finding is genuinely novel and valuable
- The systematic negative result across multiple reward functions is thorough within its scope
- The paper is well-written and refreshingly honest about its limitations
- EDCR identifies a real problem even if the metric needs more validation

### Actionable Revision Priorities

1. **Narrow the title and claims** to "GRPO fails for DocRE" rather than "online RL fails for structured IE." Present RSFT as a known practical fallback, not a core contribution.
2. **Add PPO and/or DPO experiments**, even small-scale, to support generalization beyond GRPO.
3. **Test GRPO with larger group sizes** (G=8, G=16) and ideally full fine-tuning to isolate the failure cause.
4. **Either drop CED as a contribution** (reframe around generic RSFT) or provide stronger evidence for its value (more challenging datasets, larger sample size for significance).
5. **Add human validation for EDCR** — even 100 annotated examples would suffice.
6. **Investigate dev-test degradation** — is it RSFT-specific or does SFT also degrade? What drives it?
7. **Measure advantage variance across GRPO rollouts** to empirically verify the theoretical connection to LongRLVR.

### Experiment Coverage vs. Design

All 10 planned experiments appear in the paper: (1) CED vs flat-NLI ablation ✓, (2) test set evaluation ✓, (3) EDCR cross-method diagnostic ✓, (4) DREEAM reproduction ✓, (5) CED-as-reranker ✓, (6) model size ablation ✓, (7) Re-DocRED extension ✓, (8) top-k ablation ✓, (9) GRPO forgetting analysis ✓, (10) NLI model ablation ✓. Coverage is complete. The issue is not missing planned experiments but missing *additional* experiments needed to support the paper's claims (larger GRPO group sizes, PPO/DPO baselines, human evaluation of EDCR).
