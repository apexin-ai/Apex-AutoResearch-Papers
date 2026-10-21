# Paper Framing — exec-sim-repair-verifier

## Target Venue
- Primary: EMNLP 2026 Main (ARR May 25, 2026)
- Deadline: ARR May 25, 2026

## Framing Evolution
- **D116 (2026-05-16)**: Pivoted from "CLS scales where generation fails" (advocacy) to "The Formulation Design Space for Neural Code Verification" (empirical characterization)
- **D155 (2026-05-20)**: DeepSeek repo-level data confirms CWM collapse is **complexity-dependent** (both models collapse at repo-level), NOT tokenizer-specific. Original D116 claim "Qwen 93% vs DeepSeek 11.8%" was function-level only; repo-level shows DeepSeek CWM also 51-74% unparseable.
- **N4 Reframe**: Function-level equivalence elevated to headline finding; phase transition (func→repo divergence) as differentiating contribution.

## Core Claims (current — post D155/N4 Reframe)

1. **Formulation Equivalence at Function-Level**: CLS, CWM, and TRAJ achieve statistically equivalent accuracy at function-level across two model families (≤1.3pp gap, TOST p=0.007). Per-test CLS provides diagnostic granularity (which tests fail) at comparable accuracy with 217× throughput over CWM, though downstream re-repair benefit is unvalidated (n=44, p=0.42).

2. **Phase Transition: Complexity-Dependent Divergence**: Formulations diverge 19-26pp at repo-level, driven by CWM format collapse (51-74% unparseable outputs, 0% truncation). Direction consistent across both model families; magnitude varies (Qwen3 74% unparseable vs DeepSeek 51% at matched seq_length). This is NOT tokenizer-specific — both models collapse when outputs are long and structured.

3. **Error Complementarity**: CLS and CWM exhibit partial complementarity from different fail-bias degrees (CLS 56.5% FP, CWM 70.3% FP), yielding oracle ensemble 90.63% (+2.80pp over best single model).

## Story Spine (updated)

**Problem**: Execution-free verification for code repair can be formulated as per-test classification (CLS), execution output generation (CWM), or trajectory-level scoring (TRAJ). No controlled comparison exists across these formulations.

**Gap**: Prior work uses different models, data, and compute for each formulation, making comparison impossible. Practitioners lack guidance on when formulation choice matters.

**Our contribution**: First controlled comparison of three formulations across 2 model families, 2 complexity levels, and multiple seeds.

**Headline finding**: Formulation choice is a **phase transition** — irrelevant at function-level (≤1.3pp), critical at repo-level (19-26pp). The mechanism: CWM's O(L) generation tokens become unparseable at repo-level complexity, collapsing to majority-baseline-or-worse accuracy. This pattern is robust across both tested model families.

**Practical implication**: At ≤8B LoRA deployment scale, classification is the safer formulation for repo-level verification. CWM's generation capacity may recover at larger scales (32B+, pre-training on execution traces), but at practical fine-tuning sizes, its format compliance fails.

## Venue Fit Risks

1. **Novelty concern**: "CLS > CWM when outputs are complex" is predictable. Mitigation: (a) function-level equivalence is the surprising null result (proves it's NOT trivially easier), (b) phase transition with mechanistic explanation (format collapse, not capacity), (c) error complementarity, (d) systematic controlled comparison methodology.

2. **EMNLP vs SE venue**: Process vs outcome supervision parallel (Lightman et al., 2023; Uesato et al., 2022). General NLP methodology insight about classification vs generation scaling.

3. **CWM comparison fairness**: 4-8B LoRA vs original 32B. Explicitly scoped as "same-size LoRA comparison." Limitation strengthens practical guidance.

4. **Re-repair null result**: Diagnostic granularity downgraded from core contribution to observation (D155 W3). Efficiency (217× throughput) is the practical benefit; re-repair is future work.

## Anticipated Reviewer Concerns

| Concern | Mitigation |
|---------|------------|
| "Limited novelty — obvious that CLS is easier" | Func-level null result proves it's NOT trivially easier; phase transition with mechanistic explanation is the novel finding |
| "CWM comparison unfair (≤8B LoRA)" | Explicitly scoped; limitation discussed; practical guidance framing |
| "Single-seed repo-level" | Multi-seed replication in progress (3 seeds × 2 models × CLS/TRAJ done, CWM pending) |
| "Model-agnostic overclaim" | Direction consistent, magnitude varies. Claim: "robust across tested families" not "model-agnostic" |
| "No downstream utility" | Efficiency (217×) + diagnostic signal; re-repair honestly framed as future work |
| "Interaction not formally tested" | W5: mixed-effects logistic regression planned after multi-seed data |
| "Synthetic mutation validity" | Relative ranking validity > absolute; Andrews/Just coupling hypothesis supports formulation-agnostic shift |

## Related Work Additions Needed
- Process vs outcome supervision: Lightman et al. 2023, Uesato et al. 2022
- CodeRL, AlphaCode, Reflexion (verification-in-the-loop repair)
- Predictive mutation testing literature
- Aletheia (added per W8)
