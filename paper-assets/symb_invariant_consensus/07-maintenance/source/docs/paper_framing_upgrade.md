# Paper Framing Upgrade — Two Frameworks for EMNLP 2026 ARR May 25

Prepared: 2026-05-18. Based on current paper state + 3 new extraction methods in progress.

---

## Framework A: "Diagnosis + Method" (at least one method works)

### Trigger Condition
disc_rate improves from ~8% to 20%+ AND accuracy gain >= +2pp (significant or near-significant) for at least one of: Contrastive Extraction, Z3 Feedback Refinement, Cross-Model Extraction.

### Title Options
1. "Breaking the Capability Trap: Contrastive Constraint Extraction for LLM Self-Verification"
2. "From Diagnosis to Remedy: Overcoming Non-Discriminative Constraints in LLM Self-Verification"
3. "Discriminative by Design: Targeted Extraction Methods for Symbolic LLM Consensus"

### Abstract Framework (~220 words)
1. **Problem** (2 sent): Neuro-symbolic methods extract FOL constraints from LLM reasoning traces for answer aggregation, but whether self-extraction produces useful constraints has not been evaluated. If it works, no trained verifier or external prover is needed.
2. **Gap** (1 sent): We show standard self-extraction falls into a capability trap: constraints are semantically coupled to source answers and carry no discriminative signal (only [X]% evaluate differently across candidates).
3. **Method** (2-3 sent): We diagnose the trap across [N] models and [N] domains, then design three targeted interventions: contrastive extraction (forcing answer-discriminative constraints), Z3 feedback refinement (iterative solver-guided re-extraction), and cross-model extraction (breaking self-reference). [BEST_METHOD] achieves [PLACEHOLDER_DISC_RATE]% discriminative rate (vs. [BASELINE]% baseline).
4. **Result** (2 sent): [BEST_METHOD]-SICA improves over SC by +[PLACEHOLDER]pp on [DATASET] (p=[PLACEHOLDER]). The oracle ceiling (+8.82pp) remains partially unreached, but [BEST_METHOD] recovers [X]% of the gap, demonstrating that targeted extraction design can partially break the capability trap.

### Introduction Narrative (5 paragraphs)

**P1 — Background**: Neuro-symbolic methods (Logic-LM, LINC, DyLoS, Aristotle, FoVer) augment LLM reasoning with symbolic solvers and report gains on logical benchmarks. A critical commonality: all introduce capabilities beyond the reasoning model itself. Self-extraction would provide a lightweight, portable alternative.

**P2 — Problem importance**: Self-Consistency remains the dominant aggregation method but treats traces as black boxes, discarding intermediate reasoning structure. SC's known scaling plateau (Loo et al. 2025) motivates methods that extract richer signal. Yet no work has systematically evaluated whether self-extraction produces useful constraints.

**P3 — Capability trap diagnosis**: We evaluate SICA (MAX-SAT over self-extracted FOL) across six models, three domains, N>1,300 instances. Result: zero significant improvement. Manual analysis reveals only [X]% of constraints discriminate between candidates. Oracle control (+8.82pp, p<0.001) confirms the aggregation mechanism works; the bottleneck is extraction quality. We term this the capability trap.

**P4 — Our interventions**: The trap has a specific mechanism: constraints mirror their source answers because the same model generates both. We design three interventions targeting this mechanism: (1) contrastive extraction forces the model to generate constraints that distinguish between competing answers, (2) Z3 feedback refinement uses solver results to iteratively improve constraint quality, (3) cross-model extraction breaks self-reference by using a different model. [BEST_METHOD] raises discriminative rate from [X]% to [Y]% and yields +[Z]pp accuracy gain.

**P5 — Contributions**:
- C1: Characterize the capability trap in same-model constraint extraction (six models, three domains, N>1,300)
- C2: Design three targeted interventions grounded in the diagnosed failure mechanism
- C3: Show [BEST_METHOD] partially breaks the trap: disc_rate [X]->[Y]%, accuracy +[Z]pp, recovering [W]% of the oracle ceiling
- C4: Provide C0 diagnostic and practical guidelines for when symbolic aggregation is worth pursuing

### Method Section Additions

Current S3 (SICA Pipeline) stays as-is. Add:

**S3.5 Contrastive Extraction**
- Input: K traces with candidate answers, the set of distinct answers A(q)
- Key change: extraction prompt includes ALL candidate answers and explicitly asks "what constraint would distinguish answer X from answer Y?"
- Template structure: "The following traces disagree on the answer. Traces 1,3,5 say True. Traces 2,4,6 say False. Extract a FOL constraint that evaluates differently for True vs False."
- Rationale: forces the model to attend to inter-answer differences rather than intra-trace facts
- Cost: same number of LLM calls (one per trace), but prompt is longer (includes answer distribution)

**S3.6 Z3 Feedback Refinement**
- Iterative loop: extract -> Z3 evaluate against all candidates -> identify non-discriminative constraints -> feedback to model -> re-extract
- Feedback prompt: "The following constraints you extracted evaluate identically for all candidate answers: [list]. These are not useful. Extract constraints that evaluate differently for True vs False."
- Max iterations: 3 (diminishing returns expected)
- Inspired by Logic-LM's self-refinement but applied to constraint quality rather than parse correctness
- Cost: up to 3x extraction calls per trace

**S3.7 Cross-Model Extraction**
- Model A generates traces, Model B extracts constraints from Model A's traces
- Breaks the self-reference: Model B's extraction biases are independent of Model A's generation biases
- Tested pairs: Mistral-7B extracts from Qwen-14B traces, Qwen-14B extracts from LLaMA-8B traces
- Cost: same as baseline (one extraction call per trace), but requires two models

### Results Section Additions

**New Table 5: Extraction Method Comparison**
| Method | disc_rate (%) | Acc (%) | Delta vs SC (pp) | Delta vs baseline SICA (pp) |
|--------|-------------|---------|------------------|---------------------------|
| SC (majority vote) | --- | [X] | --- | --- |
| SICA (baseline) | [X] | [X] | [X] | --- |
| SICA + Contrastive | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |
| SICA + Z3 Refinement | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |
| SICA + Cross-Model | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |
| Oracle (gold FOL) | ~100 | 88.24 | +8.82 | +8.82 |

Primary: Qwen2.5-14B on FOLIO (n=204) + ProofWriter (n=600).

**New Table 6: Qwen3-14B Generational Comparison**
| Model | Mode | SC (%) | SICA (%) | disc_rate (%) | Delta (pp) |
|-------|------|--------|----------|--------------|--------|
| Qwen2.5-14B | standard | [X] | [X] | [X] | [X] |
| Qwen3-14B | non-thinking | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |
| Qwen3-14B | thinking | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |

**New Figure: disc_rate vs Accuracy Improvement**
- Scatter: x = disc_rate (%), y = Delta(SICA-SC) in pp
- Points: all conditions (baseline + 3 methods x datasets)
- Narrative intent: "disc_rate is the binding bottleneck; improving it translates to accuracy gains"

### Discussion Key Paragraphs (Framework A)

1. **Why [BEST_METHOD] works**: Mechanism explanation connecting back to capability trap diagnosis.
2. **Remaining gap to oracle**: Even best method recovers only [W]% of +8.82pp. What the gap represents.
3. **Cost-benefit**: [BEST_METHOD] overhead vs accuracy gain. Compare to SC baseline cost.
4. **Updated practical recommendation**: C0 -> if high, try [BEST_METHOD] -> pilot disc_rate check -> deploy.

---

## Framework B: "Systematic Diagnosis + Strong Negative" (all methods fail)

### Trigger Condition
All three methods produce disc_rate < 15% OR accuracy gain < +1.5pp (n.s.) across all tested conditions.

### Title Options
1. "The Capability Trap: Why LLMs Cannot Verify Their Own Reasoning Through Self-Extracted Constraints"
2. "Beyond Prompt Engineering: The Fundamental Limits of Self-Extracted Constraint Verification in LLMs"
3. "Three Roads to Nowhere: Systematic Evidence That Self-Extraction Cannot Break the Capability Trap"

### Abstract Framework (~220 words)
1. **Problem** (2 sent): Same as Framework A.
2. **Gap** (1 sent): Same capability trap diagnosis.
3. **Method** (2-3 sent): We diagnose the trap, then test three targeted interventions designed to break it: contrastive extraction, Z3 feedback refinement, and cross-model extraction. Each targets a specific hypothesized cause.
4. **Result** (2-3 sent): None of the three interventions significantly improves discriminative rate or accuracy. This rules out prompt-engineering explanations and establishes the capability trap as a fundamental limitation. The +8.82pp oracle ceiling remains achievable only with external formal knowledge.

### Introduction Narrative (5 paragraphs)

**P1-P3**: Same as Framework A (background, SC limitations, capability trap diagnosis).

**P4 — Systematic interventions**: The capability trap could stem from (a) prompt design (fixable with contrastive prompts), (b) solver feedback blindness (fixable with iterative refinement), or (c) self-reference circularity (fixable with cross-model). We test one intervention per hypothesis. If any succeeds, the trap is contingent; if all fail, it is fundamental to current LLM capabilities.

**P5 — Contributions**:
- C1: Characterize the capability trap across six models, three domains, N>1,300 instances
- C2: Test three targeted interventions, each addressing a specific hypothesized cause; all three fail
- C3: Rule out prompt-engineering and provide causal evidence (oracle +8.82pp) that external formal knowledge is required
- C4: C0 as zero-cost diagnostic; establish that trained verifiers are necessary for symbolic LLM verification

### Results Section Additions (Framework B)

Same table structure as Framework A, but narrative shifts:

"Despite targeting three distinct hypothesized causes, none of the interventions raise disc_rate above [X]% or achieve significant accuracy gain. The oracle ceiling (+8.82pp) remains exclusively accessible through external formal knowledge."

**Additional analysis unique to Framework B**:
- Per-intervention failure analysis: WHY each fails
  - Contrastive: model still generates constraints consistent with its own answer bias even when explicitly asked to discriminate
  - Refinement: re-extraction produces different but equally non-discriminative constraints (constraints are correct but vacuous)
  - Cross-model: Model B's extraction inherits Model A's trace structure, not truly independent
- Table: disc_rate per refinement iteration (showing plateau)

### Discussion Key Paragraphs (Framework B)

1. **Why all three fail**: Each intervention targets a surface symptom, not the root cause. Traces encode conclusions before justifications; extraction from conclusion-laden traces inevitably produces conclusion-coupled constraints.
2. **Implications**: Self-extraction pipelines cannot improve over SC without external knowledge. Trained extractors (FoVer), external provers (Logic-LM, LINC), and multi-paradigm solvers (DyLoS) succeed because they introduce knowledge the model lacks.
3. **What "fundamental" means**: Not that symbolic reasoning is useless, but that the formal knowledge must originate outside the reasoning model's own traces.
4. **Practical recommendation**: C0 screening stands, but stronger: if C0 > threshold, invest in trained extractors, not prompt engineering.

---

## Shared Elements (Both Frameworks)

### Current Structure Reuse (~80%)
- S1 Introduction: P1-P3 reusable, P4-P5 rewritten
- S2 Related Work: current text reusable, add 3-5 new citations
- S3 Method: S3.1-3.4 unchanged, add S3.5-3.7
- S4 Experiments: S4.1-4.4 unchanged, add S4.5 (new methods) + S4.6 (Qwen3)
- S5 Discussion: partially rewritten depending on framework
- S6 Conclusion: rewritten
- Abstract: rewritten

### Page Budget (8pp main limit)
Current: 8pp main. Adding 3 methods + new results + discussion = ~1.5pp extra.
Must cut ~1.5pp:
- Move temperature ablation detail to appendix (saves ~0.3pp)
- Compress ablation S4.4 table + text (saves ~0.2pp)
- Tighten Related Work (saves ~0.3pp)
- Move degeneration proof S3.4 to appendix (saves ~0.3pp)
- Merge current discussion into expanded discussion (saves ~0.3pp)

### Related Work Additions Needed (Both Frameworks)
- **Contrastive methods**: Contrastive Decoding (Li et al. 2023)
- **Self-refinement**: Self-Refine (Madaan et al. 2023), Logic-LM refinement (already cited)
- **Cross-model verification**: LLM-as-Judge, cross-model debate literature
- **CISC**: already cited (taubenfeld2025cisc)
- **RASC**: already cited (wan2024rasc)
- All new citations need verify_references before inclusion

---

## Experiment Suggestions and Insights

1. **Lead with disc_rate, not accuracy**: disc_rate is the mechanism-level metric. Accuracy is downstream consequence. Both needed, but disc_rate tells you whether the intervention is working at the right level.

2. **Contrastive prompt design is critical**: Must include actual answer distribution AND explicitly request distinguishing constraints. Test 2-3 prompt variants. A weak contrastive prompt ("extract important constraints") will fail just like baseline.

3. **Z3 Refinement: track disc_rate per iteration**: If disc_rate plateaus after round 1, further rounds are wasteful. This data is informative regardless of which framework we use.

4. **Cross-model: test BOTH directions**: Mistral->Qwen AND Qwen->Mistral. If direction matters (stronger extracting from weaker vs. vice versa), that reveals whether the issue is extraction capability or trace structure.

5. **Qwen3 thinking mode**: Most exciting condition. Extended internal CoT may produce qualitatively different traces. Measure trace length distribution alongside disc_rate. If thinking mode traces have more explicit intermediate steps, extraction might capture genuinely different constraints.

6. **Statistical power**: Run new methods on FOLIO (n=204) + ProofWriter (n=600) minimum. Combined n=804 gives MDE ~1.9pp. Running only n=204 gives MDE ~4.8pp, which may miss moderate effects.

7. **Cost tracking**: Record wall-clock time and token usage for each method. Framework A needs cost-benefit; Framework B needs "expensive interventions still fail."

8. **Define recovery metric**: recovery_rate = Delta_method / Delta_oracle x 100%. E.g., +2pp method / +8.82pp oracle = 22.7% recovery. Clean communication of progress toward ceiling.

9. **Contrastive may help Framework B too**: Even if contrastive extraction fails on accuracy, if it raises disc_rate from 8% to 15% but accuracy stays flat, that's evidence that higher disc_rate alone is insufficient (constraints are discriminative but wrong). This would strengthen the "fundamental" narrative.

10. **Cross-model with Qwen3**: If Qwen3 (thinking mode) extracts from Qwen2.5 traces, we get the strongest cross-model condition: generationally different model with extended reasoning capabilities doing extraction. Worth prioritizing.
