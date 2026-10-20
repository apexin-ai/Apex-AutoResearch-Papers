---
dream_id: dream_20260516T153939
tier: median
overall_score: 3/6 Borderline Reject
timestamp: 2026-05-16T16:20:43.042437+00:00
---

# Dream Review Report: "Empirical Evidence Toward Boundary Conditions for Error Injection in LLM Agent Training"

**Review mode:** full | **Reviewers:** R1 (Methods+Experiments), R2 (Novelty+Related Work) | **Roundtable:** 4-step

---

## 1. Paper Summary

The paper investigates whether taxonomy-guided error injection — effective for tool-use agents via PALADIN on ToolBench — transfers to embodied planning on ALFWorld. The authors design TaxEI, a 4-operator error injection taxonomy, and train Qwen3-8B under three SFT conditions (Vanilla, TaxEI, Random) across 5 seeds. Both injection methods degrade performance by 9.0pp vs. Vanilla (Cohen's d=1.58, Bonferroni NS at n=5). Taxonomy labels provide zero benefit over random noise. Models exhibit resilience (passively ignoring eval-time errors) rather than recovery (0% detection rate). Preliminary cross-model evidence on LLaMA-3.1-8B (3 seeds) shows directional consistency. A 5× data scale-up narrows but does not eliminate the gap. The paper proposes three boundary conditions (observability, locality, recoverability) to explain the divergence.

---

## 2. Experiment Coverage

All 6 imagined experiments from the design document are reflected in the paper:

| Experiment | Paper Location | Coverage |
|---|---|---|
| Recovery Eval Multi-Seed (5s × 3 conditions) | Table 1 | ✓ Complete |
| LLaMA Cross-Model Replication (3-seed) | Tables 2–3 | ✓ Complete |
| Scale Ablation (500→2500 traj) | Tables 4–5 | ✓ Complete |
| Recovery Prompting (Few-Shot) | Table 6 | ✓ Complete |
| Per-Operator Deep Dive (Multi-Seed) | Table 7, §4.5 | ✓ Complete |
| Scale-Up Data Collection | Appendix B | ✓ Complete |

**Coverage: 6/6.** The paper faithfully reflects the full experimental plan.

---

## 3. Reviewer R1 — Methods & Experiments

### Strengths

1. **Clean controlled design.** TaxEI vs. Random differ only in tag content (taxonomy label vs. generic), isolating taxonomy value. The TaxEI=Random=58.3% identity is strikingly clean and the paper's single most convincing finding.
2. **Honest statistical reporting.** Power analysis (45%), Bonferroni correction, Cohen's d, per-seed disclosure, and the power curve figure (n=9 needed for 80% power) set an exemplary standard for negative-result papers.
3. **Resilience-not-recovery finding (Table 1).** Recovery rates within 1pp of clean rates across all conditions, with 0% detection, is a genuine conceptual contribution that reframes agent evaluation.
4. **Comprehensive ablation suite.** Scale ablation, few-shot prompting, per-operator analysis, and dose-response together provide a multi-angle negative result, not a single failed experiment.
5. **Recovery-paired injection experiment** directly addresses the strongest alternative explanation (that PALADIN's recovery pairing is the "missing ingredient").

### Weaknesses

1. **(Major) Data volume confound.** Vanilla trains on 4,358 samples; TaxEI/Random on 9,029. The headline comparison (Table 1) carries this confound. A "Vanilla-2x" control (9,029 clean samples, upsampled) is missing and would be the most informative single addition.
2. **(Major) Scale ablation undermines the task-structure hypothesis.** The 29% gap reduction at 5× scale, with clear diminishing returns (500→1000: +1.9pp; 1000→2500: +0.7pp), leaves open the possibility that this is primarily a scale problem. Logarithmic extrapolation suggests gap closure at ~15-20K trajectories, well below PALADIN's 50K. The paper needs to engage more honestly with this alternative interpretation.
3. **(Major) Cross-model validation is underpowered (n=3).** Welch t p=0.52 is far from significance. TaxEI SD=8.6pp based on 3 observations is statistically meaningless for formal variance comparison. The 1/3 catastrophic seed fraction has extremely wide CIs (could be 0/10 with more seeds). This section adds narrative weight but near-zero evidential weight.
4. **(Major) Per-operator analysis drives theoretical claims it cannot support.** All Fisher exact p>0.38. The seed=42 C4 pattern (+9.1pp) collapses to +1.8pp at 5-seed. The "locality gradient" hypothesis — the paper's primary theoretical contribution — rests on statistically unsubstantiated per-operator patterns with N≈57/cell.
5. **(Minor) ALFWorld's 47 test tasks create a resolution floor of ~2.1pp per task flip.** Many reported differences are within 1-2 task flips of zero.
6. **(Minor) Detection rate 0% may be trivially expected.** If models were never trained with detection instructions, 0% detection is an artifact of the evaluation protocol, not an informative finding about capability.
7. **(Minor) Few-shot experiment (Table 6) is single-seed (s42).** The ANOVA NS result could be seed-specific.

### R1 Questions for Authors

1. Can you provide a Vanilla-2x baseline (9,029 clean samples) to isolate injection content from volume?
2. What is the projected scale at which the gap reaches zero? How does this compare to PALADIN's training scale?
3. What happens with 2 more LLaMA seeds (reaching n=5)?
4. Could the TaxEI-RP degradation be partly attributable to its larger sample count (14,437 vs 9,029)?
5. How was the gradient cosine similarity (0.28 vs 0.35) computed? Single seed/step or averaged?
6. What is the base rate of "operator replay" behaviors in Random and Vanilla failure cases?

### R1 Score: 3/6 (Borderline Reject) | Confidence: 4/5

---

## 4. Reviewer R2 — Novelty & Related Work

### Strengths

1. **Timely and well-motivated research question.** Testing paradigm transfer across agent domains is exactly what the community needs as error injection methods proliferate.
2. **TaxEI=Random identity is a clear, replicable finding** with immediate practical implications: don't bother with taxonomy design for embodied planning.
3. **Resilience-vs-recovery distinction is a genuine conceptual contribution** that reframes how we interpret "robustness" in agent evaluation.
4. **Cross-model replication attempt** — even at n=3, the effort to test beyond a single architecture shows methodological awareness.

### Weaknesses

1. **(Major) The 2×2 framework is post-hoc and underdetermined.** PALADIN occupies an ambiguous position (it injects errors AND pairs them with recovery demonstrations + retrieval). The axes (positive/negative signal × tool-use/planning) don't cleanly separate the methods. The untested cell ("negative signal in tool-use without recovery") is the critical test, and its absence means the framework cannot distinguish between "signal direction matters" and "domain matters." Moreover, where does TaxEI-RP fit? It includes both positive and negative signal in planning and performs worst, breaking the framework's implicit prediction.
2. **(Major) Boundary condition hypotheses are neither novel nor testable within this paper.** Observability, locality, and recoverability are intuitive post-hoc distinctions any researcher would generate. They are not derived from data (per-operator analysis all NS), not validated across a second domain, and not quantified. Presenting them as a contribution invites scrutiny they cannot withstand.
3. **(Major) Significant gaps in related work.** Only 11 references for a paper at the intersection of agent training, robustness, and domain transfer. Missing areas include:
   - Robustness training in RL/sequential decision-making: domain randomization (Tobin et al. 2017), robust MDPs (Iyengar 2005), RARL (Pinto et al. 2017)
   - Data augmentation transfer failures in NLP (Longpre et al. 2020)
   - Label noise robustness (Rolnick et al. 2017, Arpit et al. 2017) — directly explains training dynamics
   - Agent SFT paradigms: AgentTuning (Zeng et al. 2023), FireAct (Chen et al. 2023), Trial-and-Error/ETO (Song et al. 2024)
   - ALFWorld SOTA context: AgentPRM achieves 91% on ALFWorld, contextualizing baseline performance
4. **(Minor) "Negative transfer" in the title is slightly misleading.** TaxEI is not PALADIN directly applied; it's a new taxonomy. What fails is the paradigm, not a transferred model.
5. **(Minor) The PALADIN comparison has too many confounds** (model, scale, retrieval augmentation) to support strong claims about task structure as the primary explanatory factor.
6. **(Minor) The paper's strongest version would honestly downgrade boundary conditions to "hypotheses for future work"** rather than framing them as contributions. Current framing invites scrutiny the evidence cannot sustain.

### R2 Questions for Authors

1. Have you tested error injection on a tool-use benchmark using your exact recipe (same model, same scale, pure SFT, no retrieval)? This would isolate task structure from all PALADIN confounds.
2. Is the training objective (SFT vs. DPO) a more parsimonious explanation than task structure? SFT on error trajectories trains the model to produce errors; DPO would train it to avoid them.
3. Where does TaxEI-RP fit in the 2×2 framework? It includes both positive and negative signal in planning and performs worst.
4. Would you predict error injection succeeds in a planning domain with 1000+ diverse tasks? If so, is the boundary condition "task diversity" rather than "observability/locality/recoverability"?
5. LLaMA shows 27% detection vs. Qwen 0%. Does detection correlate with recovery on a per-episode basis?

### R2 Score: 3/6 (Borderline Reject) | Confidence: 4/5

---

## 5. Roundtable Synthesis

### Step 2: Cross-Sharing Summary

R1 and R2 independently converged on the same score (3/6) with substantial overlap in identified strengths and weaknesses. R1's distinctive contributions: detailed statistical methodology critique, emphasis on Vanilla-2x control, per-operator power analysis. R2's distinctive contributions: 2×2 framework critique, related work gaps, framing/title issues, SFT-vs-DPO alternative explanation.

### Step 3: Convergence

**Points of strong agreement (both reviewers):**
- TaxEI=Random=58.3% identity is the paper's cleanest and most valuable finding
- Resilience-not-recovery is a genuine conceptual insight
- Honest statistical reporting is exemplary for the sub-field
- Data volume confound (4358 vs 9029) is a major unresolved issue
- Cross-model evidence (n=3) adds narrative but not evidential weight
- Scale ablation partially undermines the task-structure hypothesis
- Boundary condition hypotheses are post-hoc and lack empirical support within the paper
- Per-operator analysis is exploratory only; cannot support theoretical claims
- Paper is appropriate for Findings track, not main conference

**Remaining disagreement:** None substantive. R2 raises the 2×2 framework and related work concerns that R1 did not address, but R1 would likely agree these are valid given the overlap in overall assessment.

### Step 4: Consolidated Assessment

**Overall Score: 3/6 (Borderline Reject)**

**What the paper does well:**
- Clean experimental design with proper controls (same-source dual-formatting)
- Produces a strikingly clear empirical finding (taxonomy labels = zero benefit)
- Introduces a useful distinction (resilience vs. recovery)
- Sets a high bar for statistical honesty in negative-result papers
- Covers all planned experiments comprehensively (6/6)

**What prevents acceptance at a top venue:**
1. The paper cannot statistically confirm its own central claim (Bonferroni NS, power=45%). A negative-result paper at a top venue needs either overwhelming statistical evidence or a compelling mechanistic explanation; this has suggestive evidence of the former and speculative evidence of the latter.
2. The data volume confound in the headline comparison is unresolved without a Vanilla-2x control.
3. The theoretical contribution (boundary conditions) is post-hoc, untestable within the paper, and rests on underpowered per-operator analysis. The 2×2 framework is underdetermined and doesn't cleanly categorize the methods.
4. The scale ablation (29% gap reduction at 5×) opens a credible alternative: this may be primarily a scale/diversity problem, not a structural one.
5. Related work coverage is thin (11 references) for a paper spanning agent training, robustness, and domain transfer.
6. Cross-model evidence (n=3, p=0.52) contributes almost no statistical weight.

**Recommended venue:** EMNLP Findings or workshop (e.g., LangAgents, NeurIPS Agent Workshop). For main conference, the paper would need: (a) n≥9 seeds for 80% power, (b) Vanilla-2x control, (c) a cross-domain direct test (TaxEI recipe on ToolBench), and (d) substantially expanded related work.

**Key revisions to strengthen the paper:**
1. Add Vanilla-2x baseline (9,029 clean samples) — most critical single improvement
2. Run 4 more LLaMA seeds to reach n=7 minimum
3. Run multi-seed scale ablation (current appears single-seed or 3-seed)
4. Expand related work to 25+ references covering RL robustness, data augmentation transfer, noise robustness, agent SFT paradigms
5. Downgrade boundary conditions from "contribution" to "hypotheses for future work"
6. Simplify the 2×2 framework or remove it — it creates more confusion than clarity
7. Consider renaming: "negative transfer" → "failed paradigm transfer" or "negative result"
