---
dream_id: dream_20260516T153939
tier: best
overall_score: weak reject
timestamp: 2026-05-16T16:15:18.239628+00:00
---

# Dream Review Report — Structured Error Injection for Embodied Planning

**Dream ID**: 20260516T153939 | **Review Mode**: full | **Reviewers**: R1 (Methods+Experiments), R2 (Novelty+Related Work)

---

## Roundtable Summary

| Reviewer | Focus | Score | Confidence | Post-Discussion Score |
|----------|-------|-------|------------|----------------------|
| R1 | Methods + Experiments | 3/6 (Weak Reject) | 4/5 | 3/6 (Weak Reject) |
| R2 | Novelty + Related Work | 3/6 (Weak Reject) | 4/5 | 3/6 (Weak Reject) |
| **Consensus** | | **3/6 (Weak Reject)** | **4/5** | |

Both reviewers converged independently on the same score with high confidence. The roundtable discussion reinforced rather than shifted positions — no disagreements required resolution.

---

## Consolidated Assessment

### Paper Contribution in Brief

The paper investigates whether taxonomy-guided error injection (PALADIN's +57pp on ToolBench) transfers to embodied planning via TaxEI on ALFWorld. Across 5 seeds (Qwen3-8B) and 3 seeds (LLaMA-3.1-8B), it finds: (1) structured injection degrades by 9pp with zero taxonomy-label benefit; (2) 4:1 SD ratio on LLaMA; (3) inverted-U dose-response; (4) recovery ≈ resilience (r=0.96). The paper frames these as task-structural boundary conditions for error injection.

---

### Consensus Strengths

**S1: TaxEI = Random = 58.3% is a clean, strong finding.** Both reviewers highlight this as the paper's strongest result. The experimental design isolating the taxonomy label as the sole variable (same operators, same injection points, same data volume) makes this highly credible. This cleanly falsifies the hypothesis that structured labeling improves training signal for embodied planning. [R1, R2]

**S2: Recovery ≈ resilience is a genuine conceptual contribution.** The observation that recovery rates track clean competence with r=0.96 (p<0.001, N=15) and 0% detection rate across all conditions reframes what "recovery" means in agent evaluation. Models passively ignore perturbations rather than actively recovering. This has implications beyond this specific paper. [R1, R2]

**S3: Exceptional experimental thoroughness for a negative-result paper.** Five-seed main experiment, complete 5-dose × 5-seed dose-response ablation (50+ training runs), cross-model replication, recovery-paired injection ablation, per-operator analysis, data scaling, and recovery prompting ablation. The pre-registered decision gates and transparent pivot to negative-result framing demonstrate scientific integrity. [R1, R2]

**S4: Recovery-paired injection experiment is methodologically strong.** TaxEI-RP at ~50% (worse than unpaired TaxEI at 58.3%) definitively rules out recovery pairing as the explanation for PALADIN's success. This would not be obvious to predict a priori and is a valuable experimental contribution. [R1, R2]

**S5: Statistical honesty throughout.** The authors report Bonferroni-corrected NS results, power analyses (45% at n=5), bootstrap CIs, and explicitly note when findings are exploratory. The Limitations section is unusually thorough. [R1, R2]

**S6: Inverted-U dose-response is a non-trivial empirical pattern.** The taxonomy penalty peaking at 25% and vanishing at full dose resists simple narrative explanations and suggests real structure in how structured vs. random noise interacts with training dynamics. [R2]

---

### Consensus Weaknesses

**W1 (Critical): "Fundamentally destabilizing" overclaims the evidence.** Both reviewers independently flagged the title. The primary Vanilla-vs-TaxEI comparison is Bonferroni NS (p=0.039 uncorrected, α=0.017 after correction). Power is 45%. The cross-model replication yields p=0.52. "Fundamentally" implies either formal analysis or broad empirical coverage; the paper has neither. The word should be replaced with "empirically" or removed. The paper body is appropriately hedged, but the title/abstract systematically overstate confidence. [R1, R2]

**W2 (Critical): Cross-model replication is underpowered and has confounds.** The entire "cross-architecture evidence" narrative on LLaMA rests on 3 seeds, with the catastrophic s123 result potentially confounded by a different eval seed (eval_seed=123 vs. 42 for the other seeds). Additionally, R2 identifies a cross-model inconsistency: on LLaMA, Random injection is *beneficial* (+3.5pp over Vanilla), directly contradicting the Qwen pattern where Random degrades by 9pp. This inconsistency undermines the "cross-architecture" framing. The 4:1 SD ratio claim from n=3 is statistically untestable. [R1, R2]

**W3 (Major): Data volume confound is inadequately resolved.** Vanilla trains on 4,358 samples; TaxEI/Random on 9,029 (2.07×). The dose-response ablation at fixed 4,358 partially addresses this but changes two variables simultaneously. A volume-matched Vanilla control (9,029 upsampled clean samples) is missing and would be straightforward to run. Without it, the -9.0pp result could partially reflect signal-to-noise ratio degradation at higher volume. [R1]

**W4 (Major): Scale ablation data provenance is questionable.** R1 identifies that project logs show data collection was incomplete (~405/1000 trajectories at latest update), yet the paper reports specific means and SDs for 1,000 and 2,500 trajectory conditions. If these numbers are projected rather than measured, this must be transparently labeled. Presenting extrapolated data as empirical results with specific statistics is a serious integrity concern. [R1]

**W5 (Major): Single-benchmark scope limits generalizability.** ALFWorld (47 test tasks, 6 task types, text-only observations) is one specific instantiation of embodied planning. The generalization from "ALFWorld" to "embodied planning" is overreach. Other environments (VirtualHome, Habitat, BEHAVIOR) have different error structures. The paper should say "ALFWorld" when describing empirical findings and reserve "embodied planning" for hypothesized generalizations. [R2]

**W6 (Major): Task-structural boundary conditions are hypothesized, not validated.** The 4-dimension comparison (Table 10: error observability, recovery action space, error locality, feedback granularity) is post-hoc rationalization of a single-benchmark result. No dimension is independently operationalized or tested. The framework has an empty cell (negative signal in tool-use), making it unfalsifiable. A stronger paper would test at least one dimension in isolation (e.g., adding explicit error signals to ALFWorld). [R1, R2]

**W7 (Moderate): Related work is far too sparse.** Only 9 references in the draft. Both reviewers note this is well below venue standards (30-50 typical). Critical omissions include: AgentTuning (Zeng et al., 2023), FireAct (Chen et al., 2023), Agent-FLAN (Chen et al., 2024), NAT/Learning from Mistakes (Wang et al., 2024), SayCan, Inner Monologue, domain randomization literature, noise injection theory (Mixup, NoisyStudent, label smoothing), and modern curriculum learning. [R2]

**W8 (Moderate): Per-operator analysis is underpowered and misleadingly presented.** With N=55-60 per operator, all Fisher exact tests are NS (p>0.18). The "monotonic local-to-global gradient" narrative, while theoretically motivated, rests on effects within noise margins. A single task flip changes deltas by 8-9pp. This should be more clearly flagged as exploratory or relegated to an appendix. [R1, R2]

**W9 (Minor): LLaMA 27% detection rate is a known false positive.** Project logs acknowledge this results from keyword matching ("back" in navigation phrases), not genuine error detection. Reporting it in a results table is misleading. [R1]

---

### Questions for Authors (Prioritized)

1. Were the scale ablation results (1,000 and 2,500 trajectory conditions) actually trained and evaluated, or projected? Provide experiment IDs and training logs. [R1 — integrity question]
2. For LLaMA s123, have you verified the catastrophic result is not an eval-seed artifact? Run TaxEI s123 with eval_seed=42. [R1]
3. On LLaMA, Random is *beneficial* (+3.5pp over Vanilla) while on Qwen it degrades by 9pp. How do you reconcile this? Does this not undermine the generic "injection harms embodied planning" claim? [R2]
4. Why not include a volume-matched Vanilla control (9,029 upsampled clean samples)? [R1]
5. The r=0.96 correlation (N=15) pools across conditions and seeds. What is the within-condition correlation? Non-independence across seeds may inflate the cross-condition estimate. [R1]
6. Have you considered that the taxonomy design itself may be suboptimal for ALFWorld (vs. error injection being fundamentally incompatible)? [R2]

---

### Experiment Coverage Assessment

| Planned Experiment | Status in Paper | Assessment |
|---|---|---|
| Recovery Eval Multi-Seed (5-seed × 3 conditions) | Present | Adequate |
| LLaMA Cross-Model Replication | Present (3 seeds) | Underpowered; eval-seed confound |
| Scale-Up Data (500→2500 traj) | Claimed | Provenance questionable |
| Scale Ablation (25K-50K traj) | Extrapolation table only | Appropriately labeled |
| Recovery Prompting (Few-Shot) | Present (single seed) | Limited evidential value |
| Per-Operator Deep Dive | Present (5-seed pooled) | Underpowered, all NS |

**Missing experiments that would strengthen the paper:**
- Volume-matched Vanilla control (critical)
- LLaMA with 5+ seeds (important)
- LLaMA s123 eval-seed verification (important)
- Second environment (would transform the paper)
- Empirical test of at least one boundary condition dimension (important)

---

### Actionable Revision Recommendations

1. **Downgrade framing**: Replace "fundamentally destabilizing" with "empirically destabilizing on ALFWorld." Remove "cross-architecture evidence" from the title; say "with preliminary cross-model replication."
2. **Add volume-matched Vanilla control**: Train Vanilla on 9,029 upsampled samples. This is cheap and resolves a critical confound.
3. **Verify scale ablation data**: If projected, label transparently. If incomplete, either complete or remove.
4. **Expand LLaMA replication**: Run 5 seeds minimum, all with consistent eval_seed. Address the Random-beneficial inconsistency.
5. **Expand related work**: Add 20+ missing references covering agent training, embodied agents, noise injection theory, domain randomization.
6. **Reframe boundary conditions as hypotheses**: Currently presented as findings; they are untested explanations. Explicitly label them as "proposed boundary conditions" requiring future validation.
7. **Fix LLaMA detection rate**: Either correct to 0% or remove the 27% figure with a note about the keyword-matching artifact.
8. **Clarify per-operator analysis**: Move to supplementary or explicitly label as "exploratory, hypothesis-generating" with appropriate caveats about power.

---

### Overall Verdict

**Score: 3/6 — Weak Reject**

The paper addresses a genuinely important question (when does error injection help vs. harm agent training?) with commendable experimental thoroughness and statistical honesty. The TaxEI=Random identity, recovery≈resilience finding, and recovery-paired ablation are real contributions. However, the evidence does not support the strength of the framing: the primary effect is Bonferroni NS, the cross-model replication is underpowered with concerning confounds, the single-benchmark scope cannot support "embodied planning" generalizations, and the boundary conditions are hypothesized rather than validated. The scale ablation data provenance is a potential integrity concern that must be resolved.

For a top ML venue (~25% acceptance), the paper needs either (a) a second environment confirming the pattern, (b) empirical validation of at least one boundary condition, (c) substantially stronger statistics (more seeds, volume-matched controls), or (d) formal modeling of the destabilization mechanism. The recovery-paired ablation and resilience-vs-recovery distinction are the strongest contributions and should be elevated in a revision. With the recommended revisions — particularly framing adjustments, volume-matched controls, and expanded LLaMA replication — this could reach Weak Accept territory at a findings track.