# Research conversation: Formally-Routed Process Reward Models for Sound Miracle Step Detection ## Core Problem No existing PRM exploits the form

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 42
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-3/fe782bfd-21b4-4edc-993e-2743bfd061a7.jsonl`
- **Structured JSON:** [`d25fcd04e626d98cc36f.json`](../../sessions/d2/d25fcd04e626d98cc36f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-29T06:21:41.586Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-29T06:21:41.586Z",
  "sessionId": "fe782bfd-21b4-4edc-993e-2743bfd061a7",
  "content": "# Formally-Routed Process Reward Models for Sound Miracle Step Detection\n\n## Core Problem\n\nNo existing PRM exploits the formalizability structure of reasoning steps. Formal-only PRMs (FoVer, PRoSFI) provide high precision but suffer documented overly-strict behavior on informal steps. Neural-only PRMs (GenPRM, ThinkPRM, R-PRM, ARES) provide broad coverage but no formal derivability guarantees. Hybrid systems use either hand-crafted routing (VERGE) or unlearned try-and-fallback (LogicReward). The critical gap: a learned, context-dependent formalizability router that dispatches each step to the appropriate verifier—with roundtrip-verified formal checking providing sound miracle step detection on formalizable steps while neural verification covers the rest.\n\n## Research Opportunity\n\nThree converging gaps create a unique opening:\n\n(1) VERGE (arXiv:2601.20055) demonstrates 18.7% uplift from routing between Z3 and neural verifiers but uses rule-based routing over static claim types (logical vs. commonsense)—context-free and not learned. The paper explicitly identifies learned routing as the open next step.\n\n(2) LogicReward (ICLR 2026, arXiv:2512.18196) implements Isabelle step verification with token-probability fallback—a \"try-formal-first\" strategy. This cannot distinguish \"step is intrinsically non-formalizable\" from \"autoformalization failed on a formalizable step,\" producing systematic false alarms on non-formalizable steps (the same overly-strict behavior documented in FoVer).\n\n(3) RRM (arXiv:2510.07774, withdrawn from ICLR 2026) defines the miracle step taxonomy and reduces miracle steps by 71% via rubric rewards, but never tested formal derivability from predecessors. FoVer's public codebase (arXiv:2505.15960), GenPRM's open weights (arXiv:2504.00891), and Risk-Controlled Lean-as-Judge (arXiv:2605.28365) with its honest quantification of autoformalization limits (43% faithfulness, 28% coverage for 7B autoformalizer on MATH-500) provide infrastructure and calibration data for a hybrid system at academic compute budgets.\n\n## Key Insight: Conditional Formal Soundness for Miracle Detection\n\nA miracle step is an unjustified logical leap—step S_i that does not follow from predecessors {S_1,...,S_{i-1}}. When a step is faithfully formalized and submitted to Z3 for predecessor-derivability checking, miracle steps produce Z3 UNSAT (not derivable). This is near-definitional: on the faithfully-formalized subset, miracle step detection reduces to Z3 derivability failure.\n\nThe critical qualifier is \"faithfully formalized.\" Autoformalization is unreliable: Risk-Controlled Lean-as-Judge (arXiv:2605.28365) reports only 43% faithfulness, and Do LLMs Game Formalization? (arXiv:2604.19459) identifies two unfaithfulness modes—axiom fabrication and premise mistranslation—that evade compilation-based detection. Therefore, the soundness guarantee is conditional: it holds only for steps that pass both formalizability routing AND roundtrip verification of autoformalization faithfulness (arXiv:2604.25031).\n\nFormalRoute-PRM makes this conditionality explicit and operationalizable through a three-layer pipeline: learned formalizability routing → roundtrip faithfulness verification → formal or neural verification.\n\n## Contributions\n\n1. **Conditional sound miracle detection.** On steps that the router identifies as formalizable AND that pass roundtrip faithfulness verification, Z3 predecessor-derivability checking provides guaranteed miracle step detection. This is the first PRM offering formal soundness guarantees for any subset of reasoning steps, with honest coverage reporting following Risk-Controlled methodology.\n\n2. **Learned context-dependent formalizability routing.** Unlike VERGE's static claim-type routing (context-free) and LogicReward's unlearned try-and-fallback, our Qwen3-8B router predicts formalizability conditioned on the full predecessor chain {S_1,...,S_{i-1}}. Context-dependent formalizability prediction is a non-trivial learning problem because a step's formalizability depends on: (a) the formal context established by predecessors (which definitions and variables are already formalized), (b) the autoformalization tool's capability boundary for this step type, and (c) the step's position in the proof (early declarative steps are more formalizable than later heuristic steps). Rule-based approaches cannot capture these context dependencies. Compared to try-and-fallback, learned routing provides three advantages: (i) avoids systematic false alarms from formal verification on non-formalizable steps (FoVer's documented overly-strict behavior), (ii) produces per-step verification confidence signals distinguishing formally guaranteed vs. neurally estimated scores, and (iii) distinguishes intrinsic step formalizability from extrinsic autoformalization capability.\n\n3. **Asymmetric cost-aware routing threshold.** Router errors have asymmetric costs: routing non-formalizable steps to Z3 produces false alarms (overly strict); routing formalizable steps to neural verification risks missing miracle steps. The router threshold is optimized to favor recall (prefer sending to Z3), with explicit cost-asymmetry analysis. This design is informed by FoVer's documented overly-strict behavior and Risk-Controlled Lean-as-Judge's faithfulness quantification.\n\n## Research Landscape\n\n**Formal-only PRMs.** FoVer (ACL 2026, arXiv:2505.15960) achieves 85.8 AUROC on ProcessBench via Z3/Isabelle-verified training labels, but produces overly-strict scores on informal reasoning steps. PRoSFI (arXiv:2603.29500) generates structured formal intermediaries for prover verification on the generation side.\n\n**Neural PRMs.** GenPRM (AAAI 2026, arXiv:2504.00891): 7B surpasses Qwen2.5-Math-PRM-72B on ProcessBench via generative CoT and code verification. ThinkPRM (arXiv:2504.16828): 14B trained on only 8K process labels outperforms discriminative PRMs trained on 100× more data; establishes token-budget-normalized comparison paradigm (+7.2% over LLM-as-Judge at same budget). R-PRM (EMNLP 2025, arXiv:2503.21295): +13.9 F1 on ProcessBench and +8.5 F1 on PRMBench via three-stage cold-start, DPO, inference-time scaling. ARES (2025): 72.1% Macro-F1 on PRMBench via autoregressive entailment, entirely dependent on LLM calibration.\n\n**Hybrid systems.** VERGE (arXiv:2601.20055): rule-based semantic routing (logical vs. commonsense claim types) to Z3 or LLM ensemble, 18.7% uplift—routing is static, context-free, not learned. LogicReward (ICLR 2026, arXiv:2512.18196): Isabelle step verification with token-probability fallback; 8B model surpasses GPT-4o by 11.6% on logical reasoning but is an RL training framework, not a standalone PRM. FIRMA (MathNLP 2025, ACL Anthology 2025.mathnlp-main.5): bidirectional formal-informal mathematical language alignment with a complexity router—but this routes for translation quality, not verification correctness; the target function and training signal are fundamentally different from formalizability routing for verification.\n\n**Miracle step detection.** RRM (arXiv:2510.07774, withdrawn from ICLR 2026) defines the miracle step taxonomy and reduces miracle steps by 71% via rubric rewards, without formal derivability checking.\n\n**Autoformalization limits.** Risk-Controlled Lean-as-Judge (arXiv:2605.28365): 43% faithfulness, 28% coverage for 7B autoformalizer. Do LLMs Game Formalization? (arXiv:2604.19459): identifies axiom fabrication and premise mistranslation as unfaithfulness modes evading compilation checks. Faithful Autoformalization via Roundtrip Verification (arXiv:2604.25031): provides roundtrip verification methodology for detecting unfaithful formalizations.\n\n## Proposed Approach\n\n**Three-layer pipeline:**\n\n**Layer 1: Formalizability Router.** Qwen3-8B classifier trained on FoVer Z3 verification labels + autoformalization success signals. Labels defined as: formalizable = Z3 compilation success AND roundtrip semantic verification pass; non-formalizable = autoformalization failure OR roundtrip failure OR Z3 timeout. Input: step S_i + predecessor context {S_1,...,S_{i-1}}. Output: formalizability probability. Threshold set via asymmetric cost-aware optimization favoring recall.\n\n**Layer 2: Roundtrip Faithfulness Verification.** Steps routed to formal branch undergo autoformalization (via Qwen2.5-Math-72B-Instruct) → roundtrip verification (arXiv:2604.25031): back-translate the formal statement to natural language and check semantic equivalence with the original step. Steps failing roundtrip verification are redirected to neural branch. This layer gates the soundness guarantee.\n\n**Layer 3: Verification.**\n- Formal branch (roundtrip-verified): Z3 predecessor-derivability checking. Z3 UNSAT → miracle step detected (sound). Z3 SAT → step verified with formal guarantee.\n- Neural branch (non-formalizable or roundtrip-failed): GenPRM-7B scoring with ARES-style calibrated entailment (Platt scaling on held-out validation set). Best-effort verification without formal guarantees.\n\n**Output.** Per-step score with verification confidence tier: (a) roundtrip-verified + Z3-verified (highest confidence), (b) roundtrip-failed but router-formalizable (medium—formal attempt inconclusive), (c) router-non-formalizable + neurally scored (neural confidence), (d) router uncertain (lowest confidence).\n\n## Evaluation Design\n\n**Benchmarks and metrics.**\n- ProcessBench: F1 (aligned with GenPRM, R-PRM) + AUROC (aligned with FoVer)\n- PRMBench (ACL 2025, arXiv:2501.03124): PRMScore + error-type breakdown\n- Best-of-N reranking: MATH-500, AIME24 using Qwen2.5-Math-7B-Instruct as generator; report Pass@1, majority voting, PRM reranking (N=8,16,64)\n- OOD generalization: GPQA-Diamond (scientific reasoning, following ThinkPRM)\n- Miracle step detection: precision/recall/F1 on (a) RRM miracle taxonomy annotations (Yuan et al., 2025) if publicly available, (b) PRMBench error-type categories as primary proxy if RRM data unavailable, (c) self-constructed human-annotated set (200–300 steps, 2–3 annotators, inter-annotator agreement via Cohen's kappa)\n\n**Baseline matrix.**\n- Pure neural: GenPRM-7B, ThinkPRM-14B, R-PRM-7B, Qwen2.5-Math-PRM-72B\n- Pure formal: FoVer-7B\n- Hybrid: VERGE (hand-crafted routing), Naive Hybrid (FoVer Z3 try-and-fallback to GenPRM, no learned router)\n- LLM-as-Judge: GPT-4o, QwQ-32B\n- Compute-matched: GenPRM majority voting under equivalent total token budget (including autoformalization cost)\n- LogicReward (ICLR 2026): conceptual comparison on method design; quantitative comparison where applicable with methodology differences noted (RL framework vs. standalone PRM)\n\n**Ablation studies.**\n1. Formal-only: all steps → Z3 (low coverage penalty)\n2. Neural-only: all steps → GenPRM (miracle step leakage)\n3. Random routing: 50/50 formal/neural (isolates routing from ensemble)\n4. Oracle routing: ground-truth formalizability labels (performance ceiling)\n5. Router threshold sweep: coverage-accuracy trade-off across formalizability thresholds, visualizing asymmetric cost impact\n6. Try-formal-first + neural fallback: no router, attempt Z3 on all steps, fallback on failure (trivial alternative baseline—directly tests whether learned routing outperforms unlearned try-and-fallback)\n7. Router label noise analysis: compare router trained on noisy auto-labels vs. router trained on human-cleaned labels (500–1000 examples); report label precision via human audit of 200–300 \"non-formalizable\" training labels\n\n**Compute fairness.** Report per-step average inference time and total FLOPs for all systems, explicitly including autoformalization cost (Qwen2.5-Math-72B-Instruct inference) in FormalRoute-PRM's compute. Plot accuracy vs. compute Pareto curve. Compute-matched GenPRM majority voting as explicit comparison following ThinkPRM's token-budget-normalized paradigm.\n\n**Router analysis.** Classification accuracy, precision, recall on in-domain (formal reasoning) and out-of-domain (general math, GPQA-Diamond) splits. Few-shot domain adaptation ablation with ProcessBench/PRMBench samples. Oracle formalizability labels (human-annotated, 100–200 examples) to quantify router quality ceiling. Formalizability positive rate, formal branch coverage, roundtrip verification pass rate per benchmark.\n\n**Honest coverage reporting.** Following Risk-Controlled Lean-as-Judge (arXiv:2605.28365) methodology: report autoformalization coverage, roundtrip faithfulness rate, formal branch activation rate, and effective soundness coverage (= steps receiving formal guarantee / total steps) per benchmark.\n\n## Compute Budget\n\n- Router training: Qwen3-8B LoRA fine-tuning on ~80K FoVer-derived labels, ≈4–8 GPU-hours on single H100\n- Autoformalization: Qwen2.5-Math-72B-Instruct inference for formalizable steps (est. 30–50% of total); dominant compute cost\n- Z3 solving: millisecond-scale per formula, negligible\n- GenPRM-7B inference: standard 7B inference for neural branch steps\n- Roundtrip verification: one additional LLM call per formal-branch step for back-translation + semantic equivalence check\n- Total: training <1 day, full evaluation pipeline <5 days on single-node 8×H100 (dominated by autoformalization inference)\n\n## Key References\n\n- FoVer: PRM Data Synthesis via Formal Verification (ACL 2026, arXiv:2505.15960)\n- GenPRM: Scaling Test-Time Compute of PRMs (AAAI 2026, arXiv:2504.00891)\n- LogicReward: Step-Wise Logical Supervision (ICLR 2026, arXiv:2512.18196)\n- VERGE: Formal Refinement and Guidance Engine (arXiv 2026, arXiv:2601.20055)\n- Curing Miracle Steps with Rubric Rewards (arXiv 2025, arXiv:2510.07774)\n- Risk-Controlled Lean-as-Judge (arXiv 2026, arXiv:2605.28365)\n- ARES: Autoregressive Entailment Scoring (2025)\n- ThinkPRM: Process Reward Models That Think (arXiv:2504.16828)\n- R-PRM: Reasoning-Driven Process Reward Modeling (EMNLP 2025, arXiv:2503.21295)\n- PRMBench: Fine-grained PRM Benchmark (ACL 2025, arXiv:2501.03124)\n- PRoSFI: Structured Formal Intermediaries (arXiv:2603.29500)\n- Faithful Autoformalization via Roundtrip Verification (arXiv:2604.25031)\n- FIRMA: Formal-Informal Mathematical Language Alignment (MathNLP 2025, ACL Anthology 2025.mathnlp-main.5)\n- Do LLMs Game Formalization? (arXiv:2604.19459)"
}
```

---

### Runtime record

_source line 2 · 2026-05-29T06:21:41.608Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-29T06:21:41.608Z",
  "sessionId": "fe782bfd-21b4-4edc-993e-2743bfd061a7"
}
```

---

## Round 1

40 recorded events

### User

_source line 3 · 2026-05-29T06:21:41.642Z_

# Formally-Routed Process Reward Models for Sound Miracle Step Detection

## Core Problem

No existing PRM exploits the formalizability structure of reasoning steps. Formal-only PRMs (FoVer, PRoSFI) provide high precision but suffer documented overly-strict behavior on informal steps. Neural-only PRMs (GenPRM, ThinkPRM, R-PRM, ARES) provide broad coverage but no formal derivability guarantees. Hybrid systems use either hand-crafted routing (VERGE) or unlearned try-and-fallback (LogicReward). The critical gap: a learned, context-dependent formalizability router that dispatches each step to the appropriate verifier—with roundtrip-verified formal checking providing sound miracle step detection on formalizable steps while neural verification covers the rest.

## Research Opportunity

Three converging gaps create a unique opening:

(1) VERGE (arXiv:2601.20055) demonstrates 18.7% uplift from routing between Z3 and neural verifiers but uses rule-based routing over static claim types (logical vs. commonsense)—context-free and not learned. The paper explicitly identifies learned routing as the open next step.

(2) LogicReward (ICLR 2026, arXiv:2512.18196) implements Isabelle step verification with token-probability fallback—a "try-formal-first" strategy. This cannot distinguish "step is intrinsically non-formalizable" from "autoformalization failed on a formalizable step," producing systematic false alarms on non-formalizable steps (the same overly-strict behavior documented in FoVer).

(3) RRM (arXiv:2510.07774, withdrawn from ICLR 2026) defines the miracle step taxonomy and reduces miracle steps by 71% via rubric rewards, but never tested formal derivability from predecessors. FoVer's public codebase (arXiv:2505.15960), GenPRM's open weights (arXiv:2504.00891), and Risk-Controlled Lean-as-Judge (arXiv:2605.28365) with its honest quantification of autoformalization limits (43% faithfulness, 28% coverage for 7B autoformalizer on MATH-500) provide infrastructure and calibration data for a hybrid system at academic compute budgets.

## Key Insight: Conditional Formal Soundness for Miracle Detection

A miracle step is an unjustified logical leap—step S_i that does not follow from predecessors {S_1,...,S_{i-1}}. When a step is faithfully formalized and submitted to Z3 for predecessor-derivability checking, miracle steps produce Z3 UNSAT (not derivable). This is near-definitional: on the faithfully-formalized subset, miracle step detection reduces to Z3 derivability failure.

The critical qualifier is "faithfully formalized." Autoformalization is unreliable: Risk-Controlled Lean-as-Judge (arXiv:2605.28365) reports only 43% faithfulness, and Do LLMs Game Formalization? (arXiv:2604.19459) identifies two unfaithfulness modes—axiom fabrication and premise mistranslation—that evade compilation-based detection. Therefore, the soundness guarantee is conditional: it holds only for steps that pass both formalizability routing AND roundtrip verification of autoformalization faithfulness (arXiv:2604.25031).

FormalRoute-PRM makes this conditionality explicit and operationalizable through a three-layer pipeline: learned formalizability routing → roundtrip faithfulness verification → formal or neural verification.

## Contributions

1. **Conditional sound miracle detection.** On steps that the router identifies as formalizable AND that pass roundtrip faithfulness verification, Z3 predecessor-derivability checking provides guaranteed miracle step detection. This is the first PRM offering formal soundness guarantees for any subset of reasoning steps, with honest coverage reporting following Risk-Controlled methodology.

2. **Learned context-dependent formalizability routing.** Unlike VERGE's static claim-type routing (context-free) and LogicReward's unlearned try-and-fallback, our Qwen3-8B router predicts formalizability conditioned on the full predecessor chain {S_1,...,S_{i-1}}. Context-dependent formalizability prediction is a non-trivial learning problem because a step's formalizability depends on: (a) the formal context established by predecessors (which definitions and variables are already formalized), (b) the autoformalization tool's capability boundary for this step type, and (c) the step's position in the proof (early declarative steps are more formalizable than later heuristic steps). Rule-based approaches cannot capture these context dependencies. Compared to try-and-fallback, learned routing provides three advantages: (i) avoids systematic false alarms from formal verification on non-formalizable steps (FoVer's documented overly-strict behavior), (ii) produces per-step verification confidence signals distinguishing formally guaranteed vs. neurally estimated scores, and (iii) distinguishes intrinsic step formalizability from extrinsic autoformalization capability.

3. **Asymmetric cost-aware routing threshold.** Router errors have asymmetric costs: routing non-formalizable steps to Z3 produces false alarms (overly strict); routing formalizable steps to neural verification risks missing miracle steps. The router threshold is optimized to favor recall (prefer sending to Z3), with explicit cost-asymmetry analysis. This design is informed by FoVer's documented overly-strict behavior and Risk-Controlled Lean-as-Judge's faithfulness quantification.

## Research Landscape

**Formal-only PRMs.** FoVer (ACL 2026, arXiv:2505.15960) achieves 85.8 AUROC on ProcessBench via Z3/Isabelle-verified training labels, but produces overly-strict scores on informal reasoning steps. PRoSFI (arXiv:2603.29500) generates structured formal intermediaries for prover verification on the generation side.

**Neural PRMs.** GenPRM (AAAI 2026, arXiv:2504.00891): 7B surpasses Qwen2.5-Math-PRM-72B on ProcessBench via generative CoT and code verification. ThinkPRM (arXiv:2504.16828): 14B trained on only 8K process labels outperforms discriminative PRMs trained on 100× more data; establishes token-budget-normalized comparison paradigm (+7.2% over LLM-as-Judge at same budget). R-PRM (EMNLP 2025, arXiv:2503.21295): +13.9 F1 on ProcessBench and +8.5 F1 on PRMBench via three-stage cold-start, DPO, inference-time scaling. ARES (2025): 72.1% Macro-F1 on PRMBench via autoregressive entailment, entirely dependent on LLM calibration.

**Hybrid systems.** VERGE (arXiv:2601.20055): rule-based semantic routing (logical vs. commonsense claim types) to Z3 or LLM ensemble, 18.7% uplift—routing is static, context-free, not learned. LogicReward (ICLR 2026, arXiv:2512.18196): Isabelle step verification with token-probability fallback; 8B model surpasses GPT-4o by 11.6% on logical reasoning but is an RL training framework, not a standalone PRM. FIRMA (MathNLP 2025, ACL Anthology 2025.mathnlp-main.5): bidirectional formal-informal mathematical language alignment with a complexity router—but this routes for translation quality, not verification correctness; the target function and training signal are fundamentally different from formalizability routing for verification.

**Miracle step detection.** RRM (arXiv:2510.07774, withdrawn from ICLR 2026) defines the miracle step taxonomy and reduces miracle steps by 71% via rubric rewards, without formal derivability checking.

**Autoformalization limits.** Risk-Controlled Lean-as-Judge (arXiv:2605.28365): 43% faithfulness, 28% coverage for 7B autoformalizer. Do LLMs Game Formalization? (arXiv:2604.19459): identifies axiom fabrication and premise mistranslation as unfaithfulness modes evading compilation checks. Faithful Autoformalization via Roundtrip Verification (arXiv:2604.25031): provides roundtrip verification methodology for detecting unfaithful formalizations.

## Proposed Approach

**Three-layer pipeline:**

**Layer 1: Formalizability Router.** Qwen3-8B classifier trained on FoVer Z3 verification labels + autoformalization success signals. Labels defined as: formalizable = Z3 compilation success AND roundtrip semantic verification pass; non-formalizable = autoformalization failure OR roundtrip failure OR Z3 timeout. Input: step S_i + predecessor context {S_1,...,S_{i-1}}. Output: formalizability probability. Threshold set via asymmetric cost-aware optimization favoring recall.

**Layer 2: Roundtrip Faithfulness Verification.** Steps routed to formal branch undergo autoformalization (via Qwen2.5-Math-72B-Instruct) → roundtrip verification (arXiv:2604.25031): back-translate the formal statement to natural language and check semantic equivalence with the original step. Steps failing roundtrip verification are redirected to neural branch. This layer gates the soundness guarantee.

**Layer 3: Verification.**
- Formal branch (roundtrip-verified): Z3 predecessor-derivability checking. Z3 UNSAT → miracle step detected (sound). Z3 SAT → step verified with formal guarantee.
- Neural branch (non-formalizable or roundtrip-failed): GenPRM-7B scoring with ARES-style calibrated entailment (Platt scaling on held-out validation set). Best-effort verification without formal guarantees.

**Output.** Per-step score with verification confidence tier: (a) roundtrip-verified + Z3-verified (highest confidence), (b) roundtrip-failed but router-formalizable (medium—formal attempt inconclusive), (c) router-non-formalizable + neurally scored (neural confidence), (d) router uncertain (lowest confidence).

## Evaluation Design

**Benchmarks and metrics.**
- ProcessBench: F1 (aligned with GenPRM, R-PRM) + AUROC (aligned with FoVer)
- PRMBench (ACL 2025, arXiv:2501.03124): PRMScore + error-type breakdown
- Best-of-N reranking: MATH-500, AIME24 using Qwen2.5-Math-7B-Instruct as generator; report Pass@1, majority voting, PRM reranking (N=8,16,64)
- OOD generalization: GPQA-Diamond (scientific reasoning, following ThinkPRM)
- Miracle step detection: precision/recall/F1 on (a) RRM miracle taxonomy annotations (Yuan et al., 2025) if publicly available, (b) PRMBench error-type categories as primary proxy if RRM data unavailable, (c) self-constructed human-annotated set (200–300 steps, 2–3 annotators, inter-annotator agreement via Cohen's kappa)

**Baseline matrix.**
- Pure neural: GenPRM-7B, ThinkPRM-14B, R-PRM-7B, Qwen2.5-Math-PRM-72B
- Pure formal: FoVer-7B
- Hybrid: VERGE (hand-crafted routing), Naive Hybrid (FoVer Z3 try-and-fallback to GenPRM, no learned router)
- LLM-as-Judge: GPT-4o, QwQ-32B
- Compute-matched: GenPRM majority voting under equivalent total token budget (including autoformalization cost)
- LogicReward (ICLR 2026): conceptual comparison on method design; quantitative comparison where applicable with methodology differences noted (RL framework vs. standalone PRM)

**Ablation studies.**
1. Formal-only: all steps → Z3 (low coverage penalty)
2. Neural-only: all steps → GenPRM (miracle step leakage)
3. Random routing: 50/50 formal/neural (isolates routing from ensemble)
4. Oracle routing: ground-truth formalizability labels (performance ceiling)
5. Router threshold sweep: coverage-accuracy trade-off across formalizability thresholds, visualizing asymmetric cost impact
6. Try-formal-first + neural fallback: no router, attempt Z3 on all steps, fallback on failure (trivial alternative baseline—directly tests whether learned routing outperforms unlearned try-and-fallback)
7. Router label noise analysis: compare router trained on noisy auto-labels vs. router trained on human-cleaned labels (500–1000 examples); report label precision via human audit of 200–300 "non-formalizable" training labels

**Compute fairness.** Report per-step average inference time and total FLOPs for all systems, explicitly including autoformalization cost (Qwen2.5-Math-72B-Instruct inference) in FormalRoute-PRM's compute. Plot accuracy vs. compute Pareto curve. Compute-matched GenPRM majority voting as explicit comparison following ThinkPRM's token-budget-normalized paradigm.

**Router analysis.** Classification accuracy, precision, recall on in-domain (formal reasoning) and out-of-domain (general math, GPQA-Diamond) splits. Few-shot domain adaptation ablation with ProcessBench/PRMBench samples. Oracle formalizability labels (human-annotated, 100–200 examples) to quantify router quality ceiling. Formalizability positive rate, formal branch coverage, roundtrip verification pass rate per benchmark.

**Honest coverage reporting.** Following Risk-Controlled Lean-as-Judge (arXiv:2605.28365) methodology: report autoformalization coverage, roundtrip faithfulness rate, formal branch activation rate, and effective soundness coverage (= steps receiving formal guarantee / total steps) per benchmark.

## Compute Budget

- Router training: Qwen3-8B LoRA fine-tuning on ~80K FoVer-derived labels, ≈4–8 GPU-hours on single H100
- Autoformalization: Qwen2.5-Math-72B-Instruct inference for formalizable steps (est. 30–50% of total); dominant compute cost
- Z3 solving: millisecond-scale per formula, negligible
- GenPRM-7B inference: standard 7B inference for neural branch steps
- Roundtrip verification: one additional LLM call per formal-branch step for back-translation + semantic equivalence check
- Total: training <1 day, full evaluation pipeline <5 days on single-node 8×H100 (dominated by autoformalization inference)

## Key References

- FoVer: PRM Data Synthesis via Formal Verification (ACL 2026, arXiv:2505.15960)
- GenPRM: Scaling Test-Time Compute of PRMs (AAAI 2026, arXiv:2504.00891)
- LogicReward: Step-Wise Logical Supervision (ICLR 2026, arXiv:2512.18196)
- VERGE: Formal Refinement and Guidance Engine (arXiv 2026, arXiv:2601.20055)
- Curing Miracle Steps with Rubric Rewards (arXiv 2025, arXiv:2510.07774)
- Risk-Controlled Lean-as-Judge (arXiv 2026, arXiv:2605.28365)
- ARES: Autoregressive Entailment Scoring (2025)
- ThinkPRM: Process Reward Models That Think (arXiv:2504.16828)
- R-PRM: Reasoning-Driven Process Reward Modeling (EMNLP 2025, arXiv:2503.21295)
- PRMBench: Fine-grained PRM Benchmark (ACL 2025, arXiv:2501.03124)
- PRoSFI: Structured Formal Intermediaries (arXiv:2603.29500)
- Faithful Autoformalization via Roundtrip Verification (arXiv:2604.25031)
- FIRMA: Formal-Informal Mathematical Language Alignment (MathNLP 2025, ACL Anthology 2025.mathnlp-main.5)
- Do LLMs Game Formalization? (arXiv:2604.19459)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "a00e7258-e784-41c0-94ed-69e950d263d7",
  "type": "user",
  "uuid": "83ce2b99-1fa9-4a96-945d-1c4d1d409af0",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "fe782bfd-21b4-4edc-993e-2743bfd061a7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-29T06:21:41.640Z_

```json
{
  "parentUuid": "83ce2b99-1fa9-4a96-945d-1c4d1d409af0",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskOutput",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskOutput",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": [],
    "readdedNames": [],
    "pendingMcpServers": []
  },
  "type": "attachment",
  "uuid": "b6a49b34-f427-4569-a8b9-25af2c7de22a",
  "timestamp": "2026-05-29T06:21:41.640Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "fe782bfd-21b4-4edc-993e-2743bfd061a7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-29T06:21:41.640Z_

```json
{
  "parentUuid": "b6a49b34-f427-4569-a8b9-25af2c7de22a",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "7200c9d9-6592-4bfc-9936-6dc2f8f8e2c2",
  "timestamp": "2026-05-29T06:21:41.640Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "fe782bfd-21b4-4edc-993e-2743bfd061a7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Formally-Routed Process Reward Models for Sound Miracle Step Detection  ## Core Problem  No existing PRM exploits the formalizability structure of reasoning steps. Formal-only PRMs (FoVer, PRoSFI) p…",
  "leafUuid": "7200c9d9-6592-4bfc-9936-6dc2f8f8e2c2",
  "sessionId": "fe782bfd-21b4-4edc-993e-2743bfd061a7"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Learned routing for formal process reward models",
  "sessionId": "fe782bfd-21b4-4edc-993e-2743bfd061a7"
}
```

---

### Assistant

_source line 8 · 2026-05-29T06:21:48.345Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to act as the "发掘 agent" (Discovery Agent) to analyze a research proposal about "Formally-Routed Process Reward Models for Sound Miracle Step Detection" (FormalRoute-PRM). I need to:

1. First do WebSearch-based literature research
2. Then assess the proposal's novelty, significance, and related work differentiation
3. Provide concrete suggestions for strengthening the idea's ceiling

Let me start by loading the WebSearch tool, then conduct thorough literature research.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7200c9d9-6592-4bfc-9936-6dc2f8f8e2c2",
  "isSidechain": false,
  "requestId": "req_011CbWNsrk8YVmGxLUEiJiEK",
  "type": "assistant",
  "uuid": "1ec3a00f-24ee-42ef-bb54-d0e465c955a3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "fe782bfd-21b4-4edc-993e-2743bfd061a7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CuR97CdUwoWmR68UKBmxyN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5382,
      "cache_read_input_tokens": 14184,
      "output_tokens": 207,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5382,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 207,
          "cache_read_input_tokens": 14184,
          "cache_creation_input_tokens": 5382,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5382
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-29T06:21:48.894Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_015ZymV5yNoi5v4oMGi3EEmc`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ec3a00f-24ee-42ef-bb54-d0e465c955a3",
  "isSidechain": false,
  "requestId": "req_011CbWNsrk8YVmGxLUEiJiEK",
  "type": "assistant",
  "uuid": "6ae8115d-e2b7-479a-bfb2-e523b0d82a77",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "fe782bfd-21b4-4edc-993e-2743bfd061a7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CuR97CdUwoWmR68UKBmxyN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5382,
      "cache_read_input_tokens": 14184,
      "output_tokens": 207,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5382,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 207,
          "cache_read_input_tokens": 14184,
          "cache_creation_input_tokens": 5382,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5382
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-29T06:21:48.904Z_

<details><summary>↩ Tool result · `toolu_015ZymV5yNoi5v4oMGi3EEmc`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6ae8115d-e2b7-479a-bfb2-e523b0d82a77",
  "isSidechain": false,
  "promptId": "a00e7258-e784-41c0-94ed-69e950d263d7",
  "type": "user",
  "uuid": "c567aad6-5865-4b81-9561-91619f901c33",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "6ae8115d-e2b7-479a-bfb2-e523b0d82a77",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "fe782bfd-21b4-4edc-993e-2743bfd061a7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-29T06:21:54.734Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me conduct the required pre-research. I need to do 3-5 targeted searches to understand the current landscape before giving any suggestions. Let me search for:

1. Recent work on process reward models (PRMs) and formal verification in math reasoning
2. Learned routing/dispatching in hybrid verification systems
3. Miracle step detection and autoformalization faithfulness
4. FormalRoute-PRM or similar hybrid formal-neural verification approaches
5. Recent advances in formalizability prediction/classification

Let me start with multiple searches in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c567aad6-5865-4b81-9561-91619f901c33",
  "isSidechain": false,
  "requestId": "req_011CbWNtPqeZ8jcRb9aThzB2",
  "type": "assistant",
  "uuid": "96e006e1-9c99-4589-b15b-836b177ac48a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "fe782bfd-21b4-4edc-993e-2743bfd061a7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NpKqSoE9enqq3deGwCnDUE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 735,
      "cache_read_input_tokens": 19566,
      "output_tokens": 352,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 735,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 352,
          "cache_read_input_tokens": 19566,
          "cache_creation_input_tokens": 735,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 735
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-29T06:21:55.736Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AmVksb4m6mB7MtnFrbrDbL`</summary>

```json
{
  "query": "process reward model formal verification hybrid routing 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96e006e1-9c99-4589-b15b-836b177ac48a",
  "isSidechain": false,
  "requestId": "req_011CbWNtPqeZ8jcRb9aThzB2",
  "type": "assistant",
  "uuid": "2ec29510-9a07-45f3-93eb-0b1f31fe8f90",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "fe782bfd-21b4-4edc-993e-2743bfd061a7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NpKqSoE9enqq3deGwCnDUE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 735,
      "cache_read_input_tokens": 19566,
      "output_tokens": 352,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 735,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 352,
          "cache_read_input_tokens": 19566,
          "cache_creation_input_tokens": 735,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 735
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-29T06:21:56.195Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UhuqpT7SybN58TfqhF8QC1`</summary>

```json
{
  "query": "miracle step detection mathematical reasoning LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ec29510-9a07-45f3-93eb-0b1f31fe8f90",
  "isSidechain": false,
  "requestId": "req_011CbWNtPqeZ8jcRb9aThzB2",
  "type": "assistant",
  "uuid": "e9185987-8cfb-44b9-8bad-5d1cf6f1c048",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "fe782bfd-21b4-4edc-993e-2743bfd061a7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NpKqSoE9enqq3deGwCnDUE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 735,
      "cache_read_input_tokens": 19566,
      "output_tokens": 352,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 735,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 352,
          "cache_read_input_tokens": 19566,
          "cache_creation_input_tokens": 735,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 735
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-29T06:21:56.712Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GKd9YAguQCAyEqwhpZajk4`</summary>

```json
{
  "query": "learned formalizability router autoformalization routing 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9185987-8cfb-44b9-8bad-5d1cf6f1c048",
  "isSidechain": false,
  "requestId": "req_011CbWNtPqeZ8jcRb9aThzB2",
  "type": "assistant",
  "uuid": "64ac0860-ad6a-40d4-9299-f55e5adf9485",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "fe782bfd-21b4-4edc-993e-2743bfd061a7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NpKqSoE9enqq3deGwCnDUE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 735,
      "cache_read_input_tokens": 19566,
      "output_tokens": 352,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 735,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 352,
          "cache_read_input_tokens": 19566,
          "cache_creation_input_tokens": 735,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 735
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-29T06:21:57.457Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018Fb2Zt5oFWaRagi1gJtXwp`</summary>

```json
{
  "query": "VERGE formal verification guidance engine Z3 neural routing arXiv 2601.20055"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "64ac0860-ad6a-40d4-9299-f55e5adf9485",
  "isSidechain": false,
  "requestId": "req_011CbWNtPqeZ8jcRb9aThzB2",
  "type": "assistant",
  "uuid": "6a356b31-4ab2-47e0-bd9f-415307a35324",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "fe782bfd-21b4-4edc-993e-2743bfd061a7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NpKqSoE9enqq3deGwCnDUE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 735,
      "cache_read_input_tokens": 19566,
      "output_tokens": 352,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 735,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 352,
          "cache_read_input_tokens": 19566,
          "cache_creation_input_tokens": 735,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 735
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-29T06:22:03.474Z_

<details><summary>↩ Tool result · `toolu_01UhuqpT7SybN58TfqhF8QC1`</summary>

```text
Web search results for query: "miracle step detection mathematical reasoning LLM 2025 2026"

Links: [{"title":"[2510.07774] Curing Miracle Steps in LLM Mathematical Reasoning with Rubric Rewards","url":"https://arxiv.org/abs/2510.07774"},{"title":"Curing \"Miracle Steps'' in LLM Math Reasoning with Rubric Rewards | OpenReview","url":"https://openreview.net/forum?id=FGkknrhv09"},{"title":"(PDF) Curing Miracle Steps in LLM Mathematical Reasoning with Rubric Rewards","url":"https://www.researchgate.net/publication/396372877_Curing_Miracle_Steps_in_LLM_Mathematical_Reasoning_with_Rubric_Rewards"},{"title":"Curing “Miracle Steps” in LLM Mathematical Reasoning with Rubric Rewards","url":"https://arxiv.org/html/2510.07774v3"},{"title":"Curing Miracle Steps in LLM Mathematical Reasoning with Rubric Rewards","url":"https://arxiv.org/pdf/2510.07774"},{"title":"[Literature Review] Curing Miracle Steps in LLM Mathematical Reasoning with Rubric Rewards","url":"https://www.themoonlight.io/en/review/curing-miracle-steps-in-llm-mathematical-reasoning-with-rubric-rewards"}]

Based on the search results, I found relevant information about "Miracle Steps" in LLM mathematical reasoning:

## What are Miracle Steps?

Miracle Steps are abrupt jumps to a correct output without a valid preceding derivation in large language models' mathematical reasoning.

## The Problem

Large language models for mathematical reasoning are typically trained with outcome-based rewards that credit only the final answer, which is highly susceptible to reward hacking, leading to solutions that reach the correct final answer through an unsound reasoning process.

## Root Causes

Probing experiments suggest that these Miracle Steps are linked to answer-recall shortcuts, including memorization from pretraining, where the model accesses the correct answer independently of its reasoning chain.

## Proposed Solution

Researchers have introduced the Rubric Reward Model (RRM) to address this issue. This approach boosts Verified Pass@1024 on AIME2024 from 26.7% to 62.6% and reduces the incidence of Miracle Steps by 71%. Rewarding the solution process is crucial for building models that are not only more accurate but also more reliable.

This research was published in October 2025 with updates through April 2026, representing recent work in improving the reliability of LLMs for mathematical reasoning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e9185987-8cfb-44b9-8bad-5d1cf6f1c048",
  "isSidechain": false,
  "promptId": "a00e7258-e784-41c0-94ed-69e950d263d7",
  "type": "user",
  "uuid": "7761f673-93ea-4eb6-99f3-a6356a1ffef8",
  "toolUseResult": {
    "query": "miracle step detection mathematical reasoning LLM 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01G53K2FfCdFRFnW1C3Qzqo8",
        "content": [
          {
            "title": "[2510.07774] Curing Miracle Steps in LLM Mathematical Reasoning with Rubric Rewards",
            "url": "https://arxiv.org/abs/2510.07774"
          },
          {
            "title": "Curing \"Miracle Steps'' in LLM Math Reasoning with Rubric Rewards | OpenReview",
            "url": "https://openreview.net/forum?id=FGkknrhv09"
          },
          {
            "title": "(PDF) Curing Miracle Steps in LLM Mathematical Reasoning with Rubric Rewards",
            "url": "https://www.researchgate.net/publication/396372877_Curing_Miracle_Steps_in_LLM_Mathematical_Reasoning_with_Rubric_Rewards"
          },
          {
            "title": "Curing “Miracle Steps” in LLM Mathematical Reasoning with Rubric Rewards",
            "url": "https://arxiv.org/html/2510.07774v3"
          },
          {
            "title": "Curing Miracle Steps in LLM Mathematical Reasoning with Rubric Rewards",
            "url": "https://arxiv.org/pdf/2510.07774"
          },
          {
            "title": "[Literature Review] Curing Miracle Steps in LLM Mathematical Reasoning with Rubric Rewards",
            "url": "https://www.themoonlight.io/en/review/curing-miracle-steps-in-llm-mathematical-reasoning-with-rubric-rewards"
          }
        ]
      },
      "Based on the search results, I found relevant information about \"Miracle Steps\" in LLM mathematical reasoning:\n\n## What are Miracle Steps?\n\nMiracle Steps are abrupt jumps to a correct output without a valid preceding derivation in large language models' mathematical reasoning.\n\n## The Problem\n\nLarge language models for mathematical reasoning are typically trained with outcome-based rewards that credit only the final answer, which is highly susceptible to reward hacking, leading to solutions that reach the correct final answer through an unsound reasoning process.\n\n## Root Causes\n\nProbing experiments suggest that these Miracle Steps are linked to answer-recall shortcuts, including memorization from pretraining, where the model accesses the correct answer independently of its reasoning chain.\n\n## Proposed Solution\n\nResearchers have introduced the Rubric Reward Model (RRM) to address this issue. This approach boosts Verified Pass@1024 on AIME2024 from 26.7% to 62.6% and reduces the incidence of Miracle Steps by 71%. Rewarding the solution process is crucial for building models that are not only more accurate but also more reliable.\n\nThis research was published in October 2025 with updates through April 2026, representing recent work in improving the reliability of LLMs for mathematical reasoning."
    ],
    "durationSeconds": 7.275097642,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e9185987-8cfb-44b9-8bad-5d1cf6f1c048",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "fe782bfd-21b4-4edc-993e-2743bfd061a7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-29T06:22:04.062Z_

<details><summary>↩ Tool result · `toolu_01AmVksb4m6mB7MtnFrbrDbL`</summary>

```text
Web search results for query: "process reward model formal verification hybrid routing 2025 2026"

Links: [{"title":"A Survey of Process Reward Models: From Outcome Signals to Process","url":"https://arxiv.org/pdf/2510.08049"},{"title":"FinePRM: Fine-grained Process Reward Model","url":"https://www.emergentmind.com/topics/fine-grained-process-reward-model-fineprm"},{"title":"Generalizable Process Reward Models via Formally Verified Training Data","url":"https://arxiv.org/pdf/2505.15960"},{"title":"Process Reward Models That Think | OpenReview","url":"https://openreview.net/forum?id=V727xqBYIW"},{"title":"AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress | Proceedings of the ACM Web Conference 2026","url":"https://dl.acm.org/doi/10.1145/3774904.3792551"},{"title":"A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models","url":"https://arxiv.org/html/2510.08049v3"},{"title":"Process Reward Models That Think","url":"https://arxiv.org/pdf/2504.16828"}]

Based on the web search results, here's what I found regarding process reward models, formal verification, and hybrid routing in 2025-2026:

## Process Reward Models with Formal Verification

A novel approach called FOVER was proposed to create PRM training data using formal verification tools, such as Z3 and Isabelle. This work advances PRMs in two directions: (1) automatic, accurate creation of training data for PRMs, and (2) generalization of PRMs to diverse reasoning tasks.

## Generative and Hybrid Approaches

ThinkPRM is a generative process reward model that verifies reasoning via long chain-of-thought, fine-tuned on orders of magnitude fewer process labels than required by discriminative PRMs.

Recent approaches combine process-level and outcome-level rewards through hybrid aggregation to ensure alignment and prevent collapse associated with overly fine or sparse rewards, with RL frameworks like PRPO integrating per-segment FinePRM scores with outcome-normalized advantages.

## Hybrid Training Pipelines

Practical task-oriented applications rely on hybrid pipelines, with examples like Web-Shepherd supervising web navigation reasoning traces by mixing human oversight with automatic checks, and GUI-Shepherd building PRM datasets via a dual-pipeline strategy combining diverse trajectories with hybrid human-GPT annotations.

## Agent Applications

Recent work explores constructing process reward models to evaluate each decision and guide agent decision-making processes. This represents an application of PRMs beyond traditional reasoning domains.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2ec29510-9a07-45f3-93eb-0b1f31fe8f90",
  "isSidechain": false,
  "promptId": "a00e7258-e784-41c0-94ed-69e950d263d7",
  "type": "user",
  "uuid": "433f793c-86d9-44af-9dca-def6be8ab956",
  "toolUseResult": {
    "query": "process reward model formal verification hybrid routing 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01R4ZcWRMPGC55UE5V4N3Vva",
        "content": [
          {
            "title": "A Survey of Process Reward Models: From Outcome Signals to Process",
            "url": "https://arxiv.org/pdf/2510.08049"
          },
          {
            "title": "FinePRM: Fine-grained Process Reward Model",
            "url": "https://www.emergentmind.com/topics/fine-grained-process-reward-model-fineprm"
          },
          {
            "title": "Generalizable Process Reward Models via Formally Verified Training Data",
            "url": "https://arxiv.org/pdf/2505.15960"
          },
          {
            "title": "Process Reward Models That Think | OpenReview",
            "url": "https://openreview.net/forum?id=V727xqBYIW"
          },
          {
            "title": "AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress | Proceedings of the ACM Web Conference 2026",
            "url": "https://dl.acm.org/doi/10.1145/3774904.3792551"
          },
          {
            "title": "A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models",
            "url": "https://arxiv.org/html/2510.08049v3"
          },
          {
            "title": "Process Reward Models That Think",
            "url": "https://arxiv.org/pdf/2504.16828"
          }
        ]
      },
      "Based on the web search results, here's what I found regarding process reward models, formal verification, and hybrid routing in 2025-2026:\n\n## Process Reward Models with Formal Verification\n\nA novel approach called FOVER was proposed to create PRM training data using formal verification tools, such as Z3 and Isabelle. This work advances PRMs in two directions: (1) automatic, accurate creation of training data for PRMs, and (2) generalization of PRMs to diverse reasoning tasks.\n\n## Generative and Hybrid Approaches\n\nThinkPRM is a generative process reward model that verifies reasoning via long chain-of-thought, fine-tuned on orders of magnitude fewer process labels than required by discriminative PRMs.\n\nRecent approaches combine process-level and outcome-level rewards through hybrid aggregation to ensure alignment and prevent collapse associated with overly fine or sparse rewards, with RL frameworks like PRPO integrating per-segment FinePRM scores with outcome-normalized advantages.\n\n## Hybrid Training Pipelines\n\nPractical task-oriented applications rely on hybrid pipelines, with examples like Web-Shepherd supervising web navigation reasoning traces by mixing human oversight with automatic checks, and GUI-Shepherd building PRM datasets via a dual-pipeline strategy combining diverse trajectories with hybrid human-GPT annotations.\n\n## Agent Applications\n\nRecent work explores constructing process reward models to evaluate each decision and guide agent decision-making processes. This represents an application of PRMs beyond traditional reasoning domains."
    ],
    "durationSeconds": 8.321191737000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "2ec29510-9a07-45f3-93eb-0b1f31fe8f90",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "fe782bfd-21b4-4edc-993e-2743bfd061a7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-29T06:22:06.105Z_

<details><summary>↩ Tool result · `toolu_018Fb2Zt5oFWaRagi1gJtXwp`</summary>

```text
Web search results for query: "VERGE formal verification guidance engine Z3 neural routing arXiv 2601.20055"

Links: [{"title":"Paper page - VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning","url":"https://huggingface.co/papers/2601.20055"},{"title":"[2601.20055] VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning","url":"https://arxiv.org/abs/2601.20055"},{"title":"VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning","url":"https://arxiv.org/html/2601.20055v1"},{"title":"Using Z3 for Formal Modeling and Verification of FNN ...","url":"https://arxiv.org/pdf/2304.10558"},{"title":"dblp: VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning.","url":"https://dblp.uni-trier.de/rec/journals/corr/abs-2601-20055.html"},{"title":"[2304.10558] Using Z3 for Formal Modeling and Verification of FNN Global Robustness","url":"https://arxiv.org/abs/2304.10558"},{"title":"Neuro-Symbolic Verification on Instruction Following of LLMs","url":"https://arxiv.org/html/2601.17789v1"},{"title":"A NEUROSYMBOLIC APPROACH TO NATURAL LANGUAGE FORMALIZATION AND VERIFICATION","url":"https://arxiv.org/pdf/2511.09008"},{"title":"Out of the Shadows: Exploring a Latent Space for Neural Network Verification","url":"https://arxiv.org/pdf/2505.17854"}]

Based on the search results, here's what I found about VERGE (arXiv 2601.20055):

## VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning

VERGE is a neuro-symbolic framework designed to bridge the semantic gap between LLM fluency and formal correctness by addressing the "all-or-nothing" limitation of traditional solvers.

### Key Features:

**Semantic Routing:** The system dynamically classifies atomic claims to handle non-formalizable natural language; verifiable logic is sent to SMT solvers (Z3) for proof, while ambiguous or commonsense claims are routed to a consensus-based "soft verifier," preventing the system from breaking on vague predicates.

**Core Innovations:** The framework includes three key innovations: (1) multi-model consensus via formal semantic equivalence checking to ensure logic-level alignment between candidates, eliminating the syntactic bias of surface-form metrics, (2) semantic routing that directs different claim types to appropriate verification strategies: symbolic solvers for logical claims and LLM ensembles for commonsense reasoning, and (3) precise logical error localization via Minimal Correction Subsets (MCS), which pinpoint the exact subset of claims to revise.

**Iterative Refinement:** The neurosymbolic framework combines LLMs with SMT solvers to produce verification-guided answers through iterative refinement, decomposing LLM outputs into atomic claims, autoformalizing them into first-order logic, and verifying their logical consistency using automated theorem proving.

**Performance:** The framework achieved an 18.7% performance uplift through iterative refinement from "probabilistic" to "provable."


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6a356b31-4ab2-47e0-bd9f-415307a35324",
  "isSidechain": false,
  "promptId": "a00e7258-e784-41c0-94ed-69e950d263d7",
  "type": "user",
  "uuid": "44f5b1ba-c711-4669-b394-0b69b14a99a3",
  "toolUseResult": {
    "query": "VERGE formal verification guidance engine Z3 neural routing arXiv 2601.20055",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XhAsAQ4VSTgWSvZcwarwgQ",
        "content": [
          {
            "title": "Paper page - VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning",
            "url": "https://huggingface.co/papers/2601.20055"
          },
          {
            "title": "[2601.20055] VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning",
            "url": "https://arxiv.org/abs/2601.20055"
          },
          {
            "title": "VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning",
            "url": "https://arxiv.org/html/2601.20055v1"
          },
          {
            "title": "Using Z3 for Formal Modeling and Verification of FNN ...",
            "url": "https://arxiv.org/pdf/2304.10558"
          },
          {
            "title": "dblp: VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning.",
            "url": "https://dblp.uni-trier.de/rec/journals/corr/abs-2601-20055.html"
          },
          {
            "title": "[2304.10558] Using Z3 for Formal Modeling and Verification of FNN Global Robustness",
            "url": "https://arxiv.org/abs/2304.10558"
          },
          {
            "title": "Neuro-Symbolic Verification on Instruction Following of LLMs",
            "url": "https://arxiv.org/html/2601.17789v1"
          },
          {
            "title": "A NEUROSYMBOLIC APPROACH TO NATURAL LANGUAGE FORMALIZATION AND VERIFICATION",
            "url": "https://arxiv.org/pdf/2511.09008"
          },
          {
            "title": "Out of the Shadows: Exploring a Latent Space for Neural Network Verification",
            "url": "https://arxiv.org/pdf/2505.17854"
          }
        ]
      },
      "Based on the search results, here's what I found about VERGE (arXiv 2601.20055):\n\n## VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning\n\nVERGE is a neuro-symbolic framework designed to bridge the semantic gap between LLM fluency and formal correctness by addressing the \"all-or-nothing\" limitation of traditional solvers.\n\n### Key Features:\n\n**Semantic Routing:** The system dynamically classifies atomic claims to handle non-formalizable natural language; verifiable logic is sent to SMT solvers (Z3) for proof, while ambiguous or commonsense claims are routed to a consensus-based \"soft verifier,\" preventing the system from breaking on vague predicates.\n\n**Core Innovations:** The framework includes three key innovations: (1) multi-model consensus via formal semantic equivalence checking to ensure logic-level alignment between candidates, eliminating the syntactic bias of surface-form metrics, (2) semantic routing that directs different claim types to appropriate verification strategies: symbolic solvers for logical claims and LLM ensembles for commonsense reasoning, and (3) precise logical error localization via Minimal Correction Subsets (MCS), which pinpoint the exact subset of claims to revise.\n\n**Iterative Refinement:** The neurosymbolic framework combines LLMs with SMT solvers to produce verification-guided answers through iterative refinement, decomposing LLM outputs into atomic claims, autoformalizing them into first-order logic, and verifying their logical consistency using automated theorem proving.\n\n**Performance:** The framework achieved an 18.7% performance uplift through iterative refinement from \"probabilistic\" to \"provable.\""
    ],
    "durationSeconds": 8.64463549,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "6a356b31-4ab2-47e0-bd9f-415307a35324",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "fe782bfd-21b4-4edc-993e-2743bfd061a7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-29T06:22:06.289Z_

<details><summary>↩ Tool result · `toolu_01GKd9YAguQCAyEqwhpZajk4`</summary>

```text
Web search results for query: "learned formalizability router autoformalization routing 2025 2026"

Links: [{"title":"Formalization and autoformalization 2026-2027","url":"https://web.math.utk.edu/~yqing/lean.html"},{"title":"130k Lines of Formal Topology in Two Weeks: Simple and Cheap Autoformalization for Everyone?","url":"https://arxiv.org/pdf/2601.03298"},{"title":"Router-R1: Teaching LLMs Multi-Round Routing and Aggregation via Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=DWf4vroKWJ"},{"title":"FormaRL: Enhancing Autoformalization with no Labeled Data","url":"https://arxiv.org/pdf/2508.18914"},{"title":"StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion","url":"https://arxiv.org/pdf/2508.04440"},{"title":"Autoformalizer with Tool Feedback","url":"https://arxiv.org/pdf/2510.06857"},{"title":"Autoformalization in the Era of Large Language Models: A Survey","url":"https://arxiv.org/html/2505.23486v1"},{"title":"MasRouter: Learning to Route LLMs for Multi-Agent System","url":"https://aclanthology.org/2025.acl-long.757.pdf"}]

Based on the search results, I found several relevant papers and projects related to autoformalization and routing in 2025-2026:

## Autoformalization Projects

A major autoformalization project for general topology from the Munkres textbook running since November 21, 2025, produced 160k lines of formalized topology by January 4, 2026, with about 130k lines completed in two weeks from December 22 to January 4 for approximately $100 in LLM subscription costs. The approach uses a feedback loop between an LLM and a proof checker equipped with a core foundational library.

## Research Papers on Autoformalization

Several recent papers address autoformalization challenges:

- Autoformalization is a challenging task for data-driven approaches, and to address the scarcity of informal-formal corpora, researchers have adopted methods to synthesize large-scale datasets for training.

- StepFun-Formalizer-32B achieved state-of-the-art scores of 40.5% on FormalMATH-Lite and 26.7% on ProverBench.

- Goedel-Formalizer-v2, the currently leading formalizer, achieves only 62.31% syntax pass@1 on combibench.

## LLM Routing Research

Router-R1 is a reinforcement learning-based framework that formulates multi-LLM routing and aggregation as a sequential decision process, supporting multi-round reasoning with dynamic LLM selection.

Additionally, MasRouter was presented at ACL 2025 (July 27 - August 1, 2025) as a framework for learning to route LLMs for multi-agent systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "64ac0860-ad6a-40d4-9299-f55e5adf9485",
  "isSidechain": false,
  "promptId": "a00e7258-e784-41c0-94ed-69e950d263d7",
  "type": "user",
  "uuid": "58519084-fb31-4ade-9633-ddb946612f12",
  "toolUseResult": {
    "query": "learned formalizability router autoformalization routing 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KRLf9bPEAyviBChmrEmMmr",
        "content": [
          {
            "title": "Formalization and autoformalization 2026-2027",
            "url": "https://web.math.utk.edu/~yqing/lean.html"
          },
          {
            "title": "130k Lines of Formal Topology in Two Weeks: Simple and Cheap Autoformalization for Everyone?",
            "url": "https://arxiv.org/pdf/2601.03298"
          },
          {
            "title": "Router-R1: Teaching LLMs Multi-Round Routing and Aggregation via Reinforcement Learning | OpenReview",
            "url": "https://openreview.net/forum?id=DWf4vroKWJ"
          },
          {
            "title": "FormaRL: Enhancing Autoformalization with no Labeled Data",
            "url": "https://arxiv.org/pdf/2508.18914"
          },
          {
            "title": "StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion",
            "url": "https://arxiv.org/pdf/2508.04440"
          },
          {
            "title": "Autoformalizer with Tool Feedback",
            "url": "https://arxiv.org/pdf/2510.06857"
          },
          {
            "title": "Autoformalization in the Era of Large Language Models: A Survey",
            "url": "https://arxiv.org/html/2505.23486v1"
          },
          {
            "title": "MasRouter: Learning to Route LLMs for Multi-Agent System",
            "url": "https://aclanthology.org/2025.acl-long.757.pdf"
          }
        ]
      },
      "Based on the search results, I found several relevant papers and projects related to autoformalization and routing in 2025-2026:\n\n## Autoformalization Projects\n\nA major autoformalization project for general topology from the Munkres textbook running since November 21, 2025, produced 160k lines of formalized topology by January 4, 2026, with about 130k lines completed in two weeks from December 22 to January 4 for approximately $100 in LLM subscription costs. The approach uses a feedback loop between an LLM and a proof checker equipped with a core foundational library.\n\n## Research Papers on Autoformalization\n\nSeveral recent papers address autoformalization challenges:\n\n- Autoformalization is a challenging task for data-driven approaches, and to address the scarcity of informal-formal corpora, researchers have adopted methods to synthesize large-scale datasets for training.\n\n- StepFun-Formalizer-32B achieved state-of-the-art scores of 40.5% on FormalMATH-Lite and 26.7% on ProverBench.\n\n- Goedel-Formalizer-v2, the currently leading formalizer, achieves only 62.31% syntax pass@1 on combibench.\n\n## LLM Routing Research\n\nRouter-R1 is a reinforcement learning-based framework that formulates multi-LLM routing and aggregation as a sequential decision process, supporting multi-round reasoning with dynamic LLM selection.\n\nAdditionally, MasRouter was presented at ACL 2025 (July 27 - August 1, 2025) as a framework for learning to route LLMs for multi-agent systems."
    ],
    "durationSeconds": 9.574389082000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "64ac0860-ad6a-40d4-9299-f55e5adf9485",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "fe782bfd-21b4-4edc-993e-2743bfd061a7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Formally-Routed Process Reward Models for Sound Miracle Step Detection  ## Core Problem  No existing PRM exploits the formalizability structure of reasoning steps. Formal-only PRMs (FoVer, PRoSFI) p…",
  "leafUuid": "58519084-fb31-4ade-9633-ddb946612f12",
  "sessionId": "fe782bfd-21b4-4edc-993e-2743bfd061a7"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Learned routing for formal process reward models",
  "sessionId": "fe782bfd-21b4-4edc-993e-2743bfd061a7"
}
```

---

### Assistant

_source line 22 · 2026-05-29T06:22:12.362Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I've gathered some initial research. Let me now do a few more targeted searches to fill in gaps:

1. Risk-Controlled Lean-as-Judge and autoformalization faithfulness limits
2. LogicReward ICLR 2026 details
3. Whether anyone has already proposed a "learned formalizability classifier" or "formalizability prediction"
4. FIRMA bidirectional formal-informal alignment and complexity router
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58519084-fb31-4ade-9633-ddb946612f12",
  "isSidechain": false,
  "requestId": "req_011CbWNufqbdSgtJRhcDv3Fg",
  "type": "assistant",
  "uuid": "be0b47e5-4158-4ccb-88fe-a7e9fabeb2f2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "fe782bfd-21b4-4edc-993e-2743bfd061a7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013S1Q6Bq56izVerjwpbyzBq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 885,
      "cache_creation_input_tokens": 2519,
      "cache_read_input_tokens": 20301,
      "output_tokens": 304,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2519,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 885,
          "output_tokens": 304,
          "cache_read_input_tokens": 20301,
          "cache_creation_input_tokens": 2519,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2519
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-29T06:22:12.676Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0184fqbuLHryVVmB1nMpL4DW`</summary>

```json
{
  "query": "Risk-Controlled Lean-as-Judge autoformalization faithfulness coverage arXiv 2605.28365"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be0b47e5-4158-4ccb-88fe-a7e9fabeb2f2",
  "isSidechain": false,
  "requestId": "req_011CbWNufqbdSgtJRhcDv3Fg",
  "type": "assistant",
  "uuid": "f357b554-8993-42d9-add0-3b8fc74e18f1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "fe782bfd-21b4-4edc-993e-2743bfd061a7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013S1Q6Bq56izVerjwpbyzBq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 885,
      "cache_creation_input_tokens": 2519,
      "cache_read_input_tokens": 20301,
      "output_tokens": 304,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2519,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 885,
          "output_tokens": 304,
          "cache_read_input_tokens": 20301,
          "cache_creation_input_tokens": 2519,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2519
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-29T06:22:13.680Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011Rb2EeTwELoSY3kDyUyr5h`</summary>

```json
{
  "query": "LogicReward ICLR 2026 Isabelle step verification token probability fallback arXiv 2512.18196"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f357b554-8993-42d9-add0-3b8fc74e18f1",
  "isSidechain": false,
  "requestId": "req_011CbWNufqbdSgtJRhcDv3Fg",
  "type": "assistant",
  "uuid": "9b81b578-3df0-4f87-947d-c762496b7a20",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "fe782bfd-21b4-4edc-993e-2743bfd061a7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013S1Q6Bq56izVerjwpbyzBq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 885,
      "cache_creation_input_tokens": 2519,
      "cache_read_input_tokens": 20301,
      "output_tokens": 304,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2519,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 885,
          "output_tokens": 304,
          "cache_read_input_tokens": 20301,
          "cache_creation_input_tokens": 2519,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2519
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-29T06:22:14.857Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01R3qjz5oaXDU1xR748LQ65U`</summary>

```json
{
  "query": "formalizability prediction classification which math steps can be formalized 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b81b578-3df0-4f87-947d-c762496b7a20",
  "isSidechain": false,
  "requestId": "req_011CbWNufqbdSgtJRhcDv3Fg",
  "type": "assistant",
  "uuid": "735d31a9-d409-4337-beba-931dc2b1ae20",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "fe782bfd-21b4-4edc-993e-2743bfd061a7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013S1Q6Bq56izVerjwpbyzBq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 885,
      "cache_creation_input_tokens": 2519,
      "cache_read_input_tokens": 20301,
      "output_tokens": 304,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2519,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 885,
          "output_tokens": 304,
          "cache_read_input_tokens": 20301,
          "cache_creation_input_tokens": 2519,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2519
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-29T06:22:21.680Z_

<details><summary>↩ Tool result · `toolu_0184fqbuLHryVVmB1nMpL4DW`</summary>

```text
Web search results for query: "Risk-Controlled Lean-as-Judge autoformalization faithfulness coverage arXiv 2605.28365"

Links: [{"title":"[2605.28365] Risk-Controlled Lean-as-Judge for Natural-Language Mathematical Reasoning","url":"https://arxiv.org/abs/2605.28365"},{"title":"Risk-Controlled Lean-as-Judge for Natural-Language Mathematical Reasoning","url":"https://arxiv.org/html/2605.28365"},{"title":"MathAtlas: A Benchmark for Autoformalization in the Wild","url":"https://arxiv.org/html/2605.14061"},{"title":"An Evaluation Benchmark for Autoformalization in Lean4","url":"https://arxiv.org/pdf/2406.06555"},{"title":"LeanTutor: A Formally-Verified AI Tutor for Mathematical ...","url":"https://arxiv.org/pdf/2506.08321"},{"title":"Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning","url":"https://arxiv.org/html/2604.19459"},{"title":"ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization","url":"https://arxiv.org/pdf/2510.15981"}]

Based on the search results, here's information about the paper with arXiv ID 2605.28365:

## Risk-Controlled Lean-as-Judge for Natural-Language Mathematical Reasoning

Lean is increasingly used to judge natural-language mathematical answers, but its signal is partial: many answers never formalize, and a failed proof may reflect an ill-typed statement or a missing library fact, not a wrong answer.

**Key Findings on Coverage and Faithfulness:**

On MATH-500, the signal is sharply coverage-dependent—the proof-winning answer is correct 96% of the time at high proved coverage but 20% at low. Additionally, a 7B autoformalizer proves a class for only 28% of problems, and a manual audit finds only approximately 43% of those proofs faithful.

**Proposed Method:**

The paper proposes COVCAL, a selector over Lean-trace diagnostics that certifies a finite-sample selective-risk bound on accepted answers or abstains, under two regimes (a conservative Bonferroni bound and a tighter dev-then-cal rule).

The paper addresses a critical problem in using Lean as a judge for mathematical reasoning: the limited coverage and faithfulness of autoformalization, proposing a risk-controlled approach to make more reliable judgments about mathematical answers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f357b554-8993-42d9-add0-3b8fc74e18f1",
  "isSidechain": false,
  "promptId": "a00e7258-e784-41c0-94ed-69e950d263d7",
  "type": "user",
  "uuid": "c3c21a39-bc9f-4abe-b762-4c9a82c6c179",
  "toolUseResult": {
    "query": "Risk-Controlled Lean-as-Judge autoformalization faithfulness coverage arXiv 2605.28365",
    "results": [
      {
        "tool_use_id": "srvtoolu_018gRTnu6ZJnJayzmAjQEoVT",
        "content": [
          {
            "title": "[2605.28365] Risk-Controlled Lean-as-Judge for Natural-Language Mathematical Reasoning",
            "url": "https://arxiv.org/abs/2605.28365"
          },
          {
            "title": "Risk-Controlled Lean-as-Judge for Natural-Language Mathematical Reasoning",
            "url": "https://arxiv.org/html/2605.28365"
          },
          {
            "title": "MathAtlas: A Benchmark for Autoformalization in the Wild",
            "url": "https://arxiv.org/html/2605.14061"
          },
          {
            "title": "An Evaluation Benchmark for Autoformalization in Lean4",
            "url": "https://arxiv.org/pdf/2406.06555"
          },
          {
            "title": "LeanTutor: A Formally-Verified AI Tutor for Mathematical ...",
            "url": "https://arxiv.org/pdf/2506.08321"
          },
          {
            "title": "Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning",
            "url": "https://arxiv.org/html/2604.19459"
          },
          {
            "title": "ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization",
            "url": "https://arxiv.org/pdf/2510.15981"
          }
        ]
      },
      "Based on the search results, here's information about the paper with arXiv ID 2605.28365:\n\n## Risk-Controlled Lean-as-Judge for Natural-Language Mathematical Reasoning\n\nLean is increasingly used to judge natural-language mathematical answers, but its signal is partial: many answers never formalize, and a failed proof may reflect an ill-typed statement or a missing library fact, not a wrong answer.\n\n**Key Findings on Coverage and Faithfulness:**\n\nOn MATH-500, the signal is sharply coverage-dependent—the proof-winning answer is correct 96% of the time at high proved coverage but 20% at low. Additionally, a 7B autoformalizer proves a class for only 28% of problems, and a manual audit finds only approximately 43% of those proofs faithful.\n\n**Proposed Method:**\n\nThe paper proposes COVCAL, a selector over Lean-trace diagnostics that certifies a finite-sample selective-risk bound on accepted answers or abstains, under two regimes (a conservative Bonferroni bound and a tighter dev-then-cal rule).\n\nThe paper addresses a critical problem in using Lean as a judge for mathematical reasoning: the limited coverage and faithfulness of autoformalization, proposing a risk-controlled approach to make more reliable judgments about mathematical answers."
    ],
    "durationSeconds": 8.996381482,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f357b554-8993-42d9-add0-3b8fc74e18f1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "fe782bfd-21b4-4edc-993e-2743bfd061a7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-29T06:22:22.674Z_

<details><summary>↩ Tool result · `toolu_01R3qjz5oaXDU1xR748LQ65U`</summary>

```text
Web search results for query: "formalizability prediction classification which math steps can be formalized 2025 2026"

Links: [{"title":"Waldemar Lis, HoTT-RO v2 A Mathematical Instrument for Relational Ontology - PhilArchive","url":"https://philarchive.org/rec/LISHVA"},{"title":"FM: Formal Methods 2027 2026 2025 .. ...","url":"http://www.wikicfp.com/cfp/program?id=1050&s=FM&f=Formal+Methods"},{"title":"StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion","url":"https://arxiv.org/pdf/2508.04440"},{"title":"May 2026 Prediction Exam - IB Mathematics AI SL | RV","url":"https://www.revisionvillage.com/ib-math/applications-and-interpretation-sl/practice-exams/prediction-exams/"},{"title":"Formal Reasoning Meets LLMs: Toward AI for Mathematics and Verification – Communications of the ACM","url":"https://cacm.acm.org/research/formal-reasoning-meets-llms-toward-ai-for-mathematics-and-verification/"},{"title":"Frontiers | Formal methods for safety-critical machine learning: a systematic literature review","url":"https://www.frontiersin.org/articles/10.3389/frai.2026.1749956/full"},{"title":"On the Relation between Realizable and Nonrealizable Cases of the   Sequence Prediction Problem","url":"https://arxiv.org/pdf/1005.5603"},{"title":"130k Lines of Formal Topology in Two Weeks: Simple and Cheap Autoformalization for Everyone?","url":"https://arxiv.org/pdf/2601.03298"},{"title":"Explainable AI needs formalization | npj Artificial Intelligence","url":"https://www.nature.com/articles/s44387-026-00095-1"}]

Based on the web search results, here are the most relevant findings about formalizability and mathematical reasoning in 2025-2026:

## Autoformalization of Mathematical Steps

Autoformalization aims to translate natural-language mathematical statements into formally verifiable statements in formal languages such as Lean, Coq, and Isabelle. StepFun-Formalizer-32B achieves state-of-the-art scores of 40.5% on FormalMATH-Lite and 26.7% on ProverBench.

## Recent Progress in AI-Assisted Formalization

A project running since November 21, 2025 has autoformalized a large portion of general topology from the Munkres textbook, producing 160k lines of formalized topology as of January 4, 2026, with about 130k lines completed in two weeks for an LLM subscription cost of about $100.

Based on fast progress, low cost, and the simple setup available to everyone, autoformalization may become quite easy and ubiquitous in 2026, regardless of which proof assistant is used.

## Broader Context on Formal Reasoning

Recent advances sparked a surge of interest in applying AI to formal mathematical reasoning, with AlphaProof becoming the first AI to achieve silver-medal level in the IMO in 2024, followed by strong results from ByteDance and Harmonic in IMO 2025.

The search results suggest that 2025-2026 marks a significant turning point where formalizability prediction and classification of which mathematical steps can be formalized has become increasingly practical and accessible through LLM-based approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "735d31a9-d409-4337-beba-931dc2b1ae20",
  "isSidechain": false,
  "promptId": "a00e7258-e784-41c0-94ed-69e950d263d7",
  "type": "user",
  "uuid": "5764854f-7c7d-4330-9221-f87202a4ea39",
  "toolUseResult": {
    "query": "formalizability prediction classification which math steps can be formalized 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RKV2W4qrrKGWLwknR9r2BB",
        "content": [
          {
            "title": "Waldemar Lis, HoTT-RO v2 A Mathematical Instrument for Relational Ontology - PhilArchive",
            "url": "https://philarchive.org/rec/LISHVA"
          },
          {
            "title": "FM: Formal Methods 2027 2026 2025 .. ...",
            "url": "http://www.wikicfp.com/cfp/program?id=1050&s=FM&f=Formal+Methods"
          },
          {
            "title": "StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion",
            "url": "https://arxiv.org/pdf/2508.04440"
          },
          {
            "title": "May 2026 Prediction Exam - IB Mathematics AI SL | RV",
            "url": "https://www.revisionvillage.com/ib-math/applications-and-interpretation-sl/practice-exams/prediction-exams/"
          },
          {
            "title": "Formal Reasoning Meets LLMs: Toward AI for Mathematics and Verification – Communications of the ACM",
            "url": "https://cacm.acm.org/research/formal-reasoning-meets-llms-toward-ai-for-mathematics-and-verification/"
          },
          {
            "title": "Frontiers | Formal methods for safety-critical machine learning: a systematic literature review",
            "url": "https://www.frontiersin.org/articles/10.3389/frai.2026.1749956/full"
          },
          {
            "title": "On the Relation between Realizable and Nonrealizable Cases of the   Sequence Prediction Problem",
            "url": "https://arxiv.org/pdf/1005.5603"
          },
          {
            "title": "130k Lines of Formal Topology in Two Weeks: Simple and Cheap Autoformalization for Everyone?",
            "url": "https://arxiv.org/pdf/2601.03298"
          },
          {
            "title": "Explainable AI needs formalization | npj Artificial Intelligence",
            "url": "https://www.nature.com/articles/s44387-026-00095-1"
          }
        ]
      },
      "Based on the web search results, here are the most relevant findings about formalizability and mathematical reasoning in 2025-2026:\n\n## Autoformalization of Mathematical Steps\n\nAutoformalization aims to translate natural-language mathematical statements into formally verifiable statements in formal languages such as Lean, Coq, and Isabelle. StepFun-Formalizer-32B achieves state-of-the-art scores of 40.5% on FormalMATH-Lite and 26.7% on ProverBench.\n\n## Recent Progress in AI-Assisted Formalization\n\nA project running since November 21, 2025 has autoformalized a large portion of general topology from the Munkres textbook, producing 160k lines of formalized topology as of January 4, 2026, with about 130k lines completed in two weeks for an LLM subscription cost of about $100.\n\nBased on fast progress, low cost, and the simple setup available to everyone, autoformalization may become quite easy and ubiquitous in 2026, regardless of which proof assistant is used.\n\n## Broader Context on Formal Reasoning\n\nRecent advances sparked a surge of interest in applying AI to formal mathematical reasoning, with AlphaProof becoming the first AI to achieve silver-medal level in the IMO in 2024, followed by strong results from ByteDance and Harmonic in IMO 2025.\n\nThe search results suggest that 2025-2026 marks a significant turning point where formalizability prediction and classification of which mathematical steps can be formalized has become increasingly practical and accessible through LLM-based approaches."
    ],
    "durationSeconds": 7.812944605000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "735d31a9-d409-4337-beba-931dc2b1ae20",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "fe782bfd-21b4-4edc-993e-2743bfd061a7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-29T06:22:23.633Z_

<details><summary>↩ Tool result · `toolu_011Rb2EeTwELoSY3kDyUyr5h`</summary>

```text
Web search results for query: "LogicReward ICLR 2026 Isabelle step verification token probability fallback arXiv 2512.18196"

Links: [{"title":"GitHub - Aiden0526/Logic-Reward: Codes and Data for ICLR 2026 paper \"LogicReward: Incentivizing LLM Reasoning via Step-Wise Logical Supervision\" · GitHub","url":"https://github.com/Aiden0526/Logic-Reward"},{"title":"[2512.18196] LogicReward: Incentivizing LLM Reasoning via Step-Wise Logical Supervision","url":"https://arxiv.org/abs/2512.18196"},{"title":"Published as a conference paper at ICLR 2026","url":"https://www.arxiv.org/pdf/2601.21969"},{"title":"Published as a conference paper at ICLR 2026 PARALLEL TOKEN PREDICTION","url":"https://arxiv.org/pdf/2512.21323"},{"title":"Pushing the Boundaries of Natural Reasoning: Interleaved Bonus from Formal-Logic Verification","url":"https://arxiv.org/pdf/2601.22642"},{"title":"LogicReward: Incentivizing LLM Reasoning via Step-Wise Logical Supervision","url":"https://arxiv.org/html/2512.18196"},{"title":"Formally Verified Solution Methods for Infinite-Horizon Markov Decision   Processes","url":"https://arxiv.org/pdf/2206.02169"},{"title":"Efficient PRM Training Data Synthesis via Formal Verification","url":"https://arxiv.org/pdf/2505.15960"},{"title":"Learning to Generate Formally Verifiable Step-by-Step Logic Reasoning via Structured Formal Intermediaries","url":"https://arxiv.org/pdf/2603.29500"}]

I found information about the paper you searched for. Here are the results:

LogicReward is an ICLR 2026 paper titled "LogicReward: Incentivizing LLM Reasoning via Step-Wise Logical Supervision" by Jundong Xu, Hao Fei, Huichi Zhou, Xin Quan, Qijun Huang, Shengqiong Wu, William Yang Wang, Mong-Li Lee, and Wynne Hsu, with the arXiv identifier 2512.18196.

The paper proposes LogicReward, a novel reward system that guides model training by enforcing step-level logical correctness with a theorem prover. The authors further introduce Autoformalization with Soft Unification, which reduces natural language ambiguity and improves formalization quality, enabling more effective use of the theorem prover.

An 8B model trained on data constructed with LogicReward surpasses GPT-4o and o4-mini by 11.6% and 2% on natural language inference and logical reasoning tasks.

The search results also show that Isabelle is used as a formal verification tool for creating training data, with some frameworks using both Z3 and Isabelle for annotating step-level error labels on LLM responses to formal logic and theorem proving tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9b81b578-3df0-4f87-947d-c762496b7a20",
  "isSidechain": false,
  "promptId": "a00e7258-e784-41c0-94ed-69e950d263d7",
  "type": "user",
  "uuid": "767b4658-8564-4489-9f3c-10907c19e17b",
  "toolUseResult": {
    "query": "LogicReward ICLR 2026 Isabelle step verification token probability fallback arXiv 2512.18196",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Ftopc2pny7yaoc6y5AUTBC",
        "content": [
          {
            "title": "GitHub - Aiden0526/Logic-Reward: Codes and Data for ICLR 2026 paper \"LogicReward: Incentivizing LLM Reasoning via Step-Wise Logical Supervision\" · GitHub",
            "url": "https://github.com/Aiden0526/Logic-Reward"
          },
          {
            "title": "[2512.18196] LogicReward: Incentivizing LLM Reasoning via Step-Wise Logical Supervision",
            "url": "https://arxiv.org/abs/2512.18196"
          },
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://www.arxiv.org/pdf/2601.21969"
          },
          {
            "title": "Published as a conference paper at ICLR 2026 PARALLEL TOKEN PREDICTION",
            "url": "https://arxiv.org/pdf/2512.21323"
          },
          {
            "title": "Pushing the Boundaries of Natural Reasoning: Interleaved Bonus from Formal-Logic Verification",
            "url": "https://arxiv.org/pdf/2601.22642"
          },
          {
            "title": "LogicReward: Incentivizing LLM Reasoning via Step-Wise Logical Supervision",
            "url": "https://arxiv.org/html/2512.18196"
          },
          {
            "title": "Formally Verified Solution Methods for Infinite-Horizon Markov Decision   Processes",
            "url": "https://arxiv.org/pdf/2206.02169"
          },
          {
            "title": "Efficient PRM Training Data Synthesis via Formal Verification",
            "url": "https://arxiv.org/pdf/2505.15960"
          },
          {
            "title": "Learning to Generate Formally Verifiable Step-by-Step Logic Reasoning via Structured Formal Intermediaries",
            "url": "https://arxiv.org/pdf/2603.29500"
          }
        ]
      },
      "I found information about the paper you searched for. Here are the results:\n\nLogicReward is an ICLR 2026 paper titled \"LogicReward: Incentivizing LLM Reasoning via Step-Wise Logical Supervision\" by Jundong Xu, Hao Fei, Huichi Zhou, Xin Quan, Qijun Huang, Shengqiong Wu, William Yang Wang, Mong-Li Lee, and Wynne Hsu, with the arXiv identifier 2512.18196.\n\nThe paper proposes LogicReward, a novel reward system that guides model training by enforcing step-level logical correctness with a theorem prover. The authors further introduce Autoformalization with Soft Unification, which reduces natural language ambiguity and improves formalization quality, enabling more effective use of the theorem prover.\n\nAn 8B model trained on data constructed with LogicReward surpasses GPT-4o and o4-mini by 11.6% and 2% on natural language inference and logical reasoning tasks.\n\nThe search results also show that Isabelle is used as a formal verification tool for creating training data, with some frameworks using both Z3 and Isabelle for annotating step-level error labels on LLM responses to formal logic and theorem proving tasks."
    ],
    "durationSeconds": 9.948981096999995,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "9b81b578-3df0-4f87-947d-c762496b7a20",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "fe782bfd-21b4-4edc-993e-2743bfd061a7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-29T06:22:30.509Z_

<details><summary>Logged reasoning block</summary>

```text
Let me do one more search to understand the landscape better, specifically looking for any work that directly competes with the "learned formalizability routing for verification" idea:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "767b4658-8564-4489-9f3c-10907c19e17b",
  "isSidechain": false,
  "requestId": "req_011CbWNvwxk6L1T7Cm1883ZG",
  "type": "assistant",
  "uuid": "21a31612-30b0-4c87-ba3d-f45d7a2cd958",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "fe782bfd-21b4-4edc-993e-2743bfd061a7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CAejZZqYm5U7E8bcbBYoCQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 917,
      "cache_creation_input_tokens": 2652,
      "cache_read_input_tokens": 22820,
      "output_tokens": 179,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2652,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 917,
          "output_tokens": 179,
          "cache_read_input_tokens": 22820,
          "cache_creation_input_tokens": 2652,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2652
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-29T06:22:31.512Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GhrTm3pPCchcK82M7Fdp49`</summary>

```json
{
  "query": "FIRMA bidirectional formal informal mathematical alignment complexity router MathNLP 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "21a31612-30b0-4c87-ba3d-f45d7a2cd958",
  "isSidechain": false,
  "requestId": "req_011CbWNvwxk6L1T7Cm1883ZG",
  "type": "assistant",
  "uuid": "0dc9ae2f-34cc-489f-8e14-5d9d8c4cfd32",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "fe782bfd-21b4-4edc-993e-2743bfd061a7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CAejZZqYm5U7E8bcbBYoCQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 917,
      "cache_creation_input_tokens": 2652,
      "cache_read_input_tokens": 22820,
      "output_tokens": 179,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2652,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 917,
          "output_tokens": 179,
          "cache_read_input_tokens": 22820,
          "cache_creation_input_tokens": 2652,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2652
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-29T06:22:32.624Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JTgfj9zj6VKgjo9iVDkAYH`</summary>

```json
{
  "query": "FoVer process reward model Z3 Isabelle overly strict behavior formal verification PRM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0dc9ae2f-34cc-489f-8e14-5d9d8c4cfd32",
  "isSidechain": false,
  "requestId": "req_011CbWNvwxk6L1T7Cm1883ZG",
  "type": "assistant",
  "uuid": "812bb4a1-cee1-4248-8d6b-b6bff0ded7e9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "fe782bfd-21b4-4edc-993e-2743bfd061a7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CAejZZqYm5U7E8bcbBYoCQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 917,
      "cache_creation_input_tokens": 2652,
      "cache_read_input_tokens": 22820,
      "output_tokens": 179,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2652,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 917,
          "output_tokens": 179,
          "cache_read_input_tokens": 22820,
          "cache_creation_input_tokens": 2652,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2652
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-29T06:22:38.549Z_

<details><summary>↩ Tool result · `toolu_01JTgfj9zj6VKgjo9iVDkAYH`</summary>

```text
Web search results for query: "FoVer process reward model Z3 Isabelle overly strict behavior formal verification PRM 2025 2026"

Links: [{"title":"[2505.15960] Efficient PRM Training Data Synthesis via Formal Verification","url":"https://arxiv.org/abs/2505.15960"},{"title":"Efficient PRM Training Data Synthesis via Formal Verification","url":"https://arxiv.org/html/2505.15960v3"},{"title":"Generalizable Process Reward Models via Formally Verified Training Data | OpenReview","url":"https://openreview.net/forum?id=LAejsDitr3"},{"title":"FOVER: Training Verifiers with Formal Tools","url":"https://www.emergentmind.com/papers/2505.15960"},{"title":"[2505.15960] Training Step-Level Reasoning Verifiers with Formal Verification Tools","url":"https://ar5iv.labs.arxiv.org/html/2505.15960"},{"title":"Paper page - Training Step-Level Reasoning Verifiers with Formal Verification Tools","url":"https://huggingface.co/papers/2505.15960"},{"title":"(PDF) Training Step-Level Reasoning Verifiers with Formal Verification Tools","url":"https://www.researchgate.net/publication/391990893_Training_Step-Level_Reasoning_Verifiers_with_Formal_Verification_Tools"},{"title":"FoVer: Efficient PRM Training Data Synthesis via Formal Verification","url":"https://fover-prm.github.io/"},{"title":"Generalizable Process Reward Models via Formally Verified Training Data","url":"https://arxiv.org/pdf/2505.15960"},{"title":"GitHub - psunlpgroup/FoVer: This repository includes code and materials for the paper \"Efficient PRM Training Data Synthesis via Formal Verification\" (ACL 2026 Findings). · GitHub","url":"https://github.com/psunlpgroup/FoVer"}]

I found comprehensive information about FoVer. Here are the search results:

## Overview

FoVer is a framework that synthesizes PRM (Process Reward Model) training data from formal reasoning tasks by annotating step-level error labels using formal verification tools such as Z3 and Isabelle.

## Purpose and Benefits

Process Reward Models have emerged as a promising approach for improving LLM reasoning capabilities by providing process supervision over reasoning traces. However, existing approaches for constructing PRM training data remain costly and noisy, as they typically rely on human annotation or sampling-based labeling methods that require repeated LLM calls.

By leveraging formal verification, FoVer enables efficient and accurate PRM data construction without requiring human annotation or additional LLM calls.

## Implementation

Using FoVer, a PRM training dataset named FoVer-40K was created by annotating step-level error labels on LLM responses to formal logic and theorem proving tasks using Z3 and Isabelle. Llama 3.1 8B and Qwen 2.5 7B were then fine-tuned on FoVer-40K to be used as PRMs.

## Generalization

PRMs trained with FoVer improve performance on diverse reasoning tasks, including MATH, AIME, and MMLU. Experiments on 12 reasoning benchmarks show that fine-tuning on the training data improves PRMs not only on math and logic reasoning tasks, but also on NLI and BBH benchmarks, which differ substantially from the tasks used to construct the training data.

The research was published in April 2026 and is part of ACL 2026 Findings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "812bb4a1-cee1-4248-8d6b-b6bff0ded7e9",
  "isSidechain": false,
  "promptId": "a00e7258-e784-41c0-94ed-69e950d263d7",
  "type": "user",
  "uuid": "1482abff-3082-44c1-9cce-6a52795a02cd",
  "toolUseResult": {
    "query": "FoVer process reward model Z3 Isabelle overly strict behavior formal verification PRM 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QmePSaBzNvMascU9iLjmBi",
        "content": [
          {
            "title": "[2505.15960] Efficient PRM Training Data Synthesis via Formal Verification",
            "url": "https://arxiv.org/abs/2505.15960"
          },
          {
            "title": "Efficient PRM Training Data Synthesis via Formal Verification",
            "url": "https://arxiv.org/html/2505.15960v3"
          },
          {
            "title": "Generalizable Process Reward Models via Formally Verified Training Data | OpenReview",
            "url": "https://openreview.net/forum?id=LAejsDitr3"
          },
          {
            "title": "FOVER: Training Verifiers with Formal Tools",
            "url": "https://www.emergentmind.com/papers/2505.15960"
          },
          {
            "title": "[2505.15960] Training Step-Level Reasoning Verifiers with Formal Verification Tools",
            "url": "https://ar5iv.labs.arxiv.org/html/2505.15960"
          },
          {
            "title": "Paper page - Training Step-Level Reasoning Verifiers with Formal Verification Tools",
            "url": "https://huggingface.co/papers/2505.15960"
          },
          {
            "title": "(PDF) Training Step-Level Reasoning Verifiers with Formal Verification Tools",
            "url": "https://www.researchgate.net/publication/391990893_Training_Step-Level_Reasoning_Verifiers_with_Formal_Verification_Tools"
          },
          {
            "title": "FoVer: Efficient PRM Training Data Synthesis via Formal Verification",
            "url": "https://fover-prm.github.io/"
          },
          {
            "title": "Generalizable Process Reward Models via Formally Verified Training Data",
            "url": "https://arxiv.org/pdf/2505.15960"
          },
          {
            "title": "GitHub - psunlpgroup/FoVer: This repository includes code and materials for the paper \"Efficient PRM Training Data Synthesis via Formal Verification\" (ACL 2026 Findings). · GitHub",
            "url": "https://github.com/psunlpgroup/FoVer"
          }
        ]
      },
      "I found comprehensive information about FoVer. Here are the search results:\n\n## Overview\n\nFoVer is a framework that synthesizes PRM (Process Reward Model) training data from formal reasoning tasks by annotating step-level error labels using formal verification tools such as Z3 and Isabelle.\n\n## Purpose and Benefits\n\nProcess Reward Models have emerged as a promising approach for improving LLM reasoning capabilities by providing process supervision over reasoning traces. However, existing approaches for constructing PRM training data remain costly and noisy, as they typically rely on human annotation or sampling-based labeling methods that require repeated LLM calls.\n\nBy leveraging formal verification, FoVer enables efficient and accurate PRM data construction without requiring human annotation or additional LLM calls.\n\n## Implementation\n\nUsing FoVer, a PRM training dataset named FoVer-40K was created by annotating step-level error labels on LLM responses to formal logic and theorem proving tasks using Z3 and Isabelle. Llama 3.1 8B and Qwen 2.5 7B were then fine-tuned on FoVer-40K to be used as PRMs.\n\n## Generalization\n\nPRMs trained with FoVer improve performance on diverse reasoning tasks, including MATH, AIME, and MMLU. Experiments on 12 reasoning benchmarks show that fine-tuning on the training data improves PRMs not only on math and logic reasoning tasks, but also on NLI and BBH benchmarks, which differ substantially from the tasks used to construct the training data.\n\nThe research was published in April 2026 and is part of ACL 2026 Findings."
    ],
    "durationSeconds": 5.919170413,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "812bb4a1-cee1-4248-8d6b-b6bff0ded7e9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "fe782bfd-21b4-4edc-993e-2743bfd061a7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 33_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Formally-Routed Process Reward Models for Sound Miracle Step Detection  ## Core Problem  No existing PRM exploits the formalizability structure of reasoning steps. Formal-only PRMs (FoVer, PRoSFI) p…",
  "leafUuid": "1482abff-3082-44c1-9cce-6a52795a02cd",
  "sessionId": "fe782bfd-21b4-4edc-993e-2743bfd061a7"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Learned routing for formal process reward models",
  "sessionId": "fe782bfd-21b4-4edc-993e-2743bfd061a7"
}
```

---

### Tool result

_source line 35 · 2026-05-29T06:22:39.712Z_

<details><summary>↩ Tool result · `toolu_01GhrTm3pPCchcK82M7Fdp49`</summary>

```text
Web search results for query: "FIRMA bidirectional formal informal mathematical alignment complexity router MathNLP 2025"

Links: [{"title":"FIRMA: Bidirectional Formal-Informal Mathematical Language Alignment with Proof-Theoretic Grounding - ACL Anthology","url":"https://aclanthology.org/2025.mathnlp-main.5/"},{"title":"Proceedings of The 3rd Workshop on Mathematical Natural Language Processing (MathNLP 2025) - ACL Anthology","url":"https://aclanthology.org/volumes/2025.mathnlp-main/"},{"title":"Workshop on Mathematical Natural Language Processing (2025) - ACL Anthology","url":"https://aclanthology.org/events/mathnlp-2025/"},{"title":"MathNLP 2025 MathNLP 2025: The 3rd Workshop on Mathematical Natural","url":"https://aclanthology.org/2025.mathnlp-main.pdf"},{"title":"FIRMA: Bidirectional Formal-Informal Mathematical ...","url":"https://aclanthology.org/2025.mathnlp-main.5.pdf"},{"title":"GitHub - smfatima3/FIRMA: The official codebase of the paper \"FIRMA: Bidirectional Formal-Informal Mathematical Language Alignment with Proof-Theoretic Grounding\"","url":"https://github.com/smfatima3/FIRMA"},{"title":"Alignment Methods for Formal Logical Reasoning","url":"https://aclanthology.org/2025.mathnlp-main.8.pdf"}]

Based on the search results, here's what I found about FIRMA:

## FIRMA Overview

FIRMA (Formal-Informal Reasoning in Mathematical Alignment) is a bidirectional translation system between formal and informal mathematical language that leverages proof-theoretic interpretability hierarchies and specialized architectural components for proof preservation.

## Problem It Addresses

While large language models excel at generating plausible mathematical text, they often produce subtly incorrect formal translations that violate proof-theoretic constraints.

## Architecture

Unlike existing approaches that treat this as pure sequence-to-sequence translation, FIRMA introduces a hierarchical architecture with complexity-aware routing, proof-preserving attention mechanisms, and multi-objective training that balances formal correctness with natural readability. More specifically, the model processes formal or informal mathematical statements through a hierarchical encoder (symbol, syntax, and semantic layers), followed by a complexity router and proof-preserving attention.

## Performance Results

Through progressive complexity training on curated datasets from Lean 4 and formal mathematics repositories, FIRMA was evaluated on 200 translation samples across complexity levels. The analysis shows statistically significant improvements of 277.8% over BFS-Prover-V1-7B and 6307.5% over REAL-Prover on overall translation quality metrics. Additionally, ablation studies on 50 samples demonstrate that each architectural component contributes substantially to performance, with removal of any component resulting in 83-85% performance degradation.

## Publication

FIRMA was presented at the 3rd Workshop on Mathematical Natural Language Processing (MathNLP 2025) in Suzhou, China, with code released on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0dc9ae2f-34cc-489f-8e14-5d9d8c4cfd32",
  "isSidechain": false,
  "promptId": "a00e7258-e784-41c0-94ed-69e950d263d7",
  "type": "user",
  "uuid": "6e1ce41b-db1f-47cf-a204-d6414f16816a",
  "toolUseResult": {
    "query": "FIRMA bidirectional formal informal mathematical alignment complexity router MathNLP 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MidBhZuzrxRipq71JNdsXu",
        "content": [
          {
            "title": "FIRMA: Bidirectional Formal-Informal Mathematical Language Alignment with Proof-Theoretic Grounding - ACL Anthology",
            "url": "https://aclanthology.org/2025.mathnlp-main.5/"
          },
          {
            "title": "Proceedings of The 3rd Workshop on Mathematical Natural Language Processing (MathNLP 2025) - ACL Anthology",
            "url": "https://aclanthology.org/volumes/2025.mathnlp-main/"
          },
          {
            "title": "Workshop on Mathematical Natural Language Processing (2025) - ACL Anthology",
            "url": "https://aclanthology.org/events/mathnlp-2025/"
          },
          {
            "title": "MathNLP 2025 MathNLP 2025: The 3rd Workshop on Mathematical Natural",
            "url": "https://aclanthology.org/2025.mathnlp-main.pdf"
          },
          {
            "title": "FIRMA: Bidirectional Formal-Informal Mathematical ...",
            "url": "https://aclanthology.org/2025.mathnlp-main.5.pdf"
          },
          {
            "title": "GitHub - smfatima3/FIRMA: The official codebase of the paper \"FIRMA: Bidirectional Formal-Informal Mathematical Language Alignment with Proof-Theoretic Grounding\"",
            "url": "https://github.com/smfatima3/FIRMA"
          },
          {
            "title": "Alignment Methods for Formal Logical Reasoning",
            "url": "https://aclanthology.org/2025.mathnlp-main.8.pdf"
          }
        ]
      },
      "Based on the search results, here's what I found about FIRMA:\n\n## FIRMA Overview\n\nFIRMA (Formal-Informal Reasoning in Mathematical Alignment) is a bidirectional translation system between formal and informal mathematical language that leverages proof-theoretic interpretability hierarchies and specialized architectural components for proof preservation.\n\n## Problem It Addresses\n\nWhile large language models excel at generating plausible mathematical text, they often produce subtly incorrect formal translations that violate proof-theoretic constraints.\n\n## Architecture\n\nUnlike existing approaches that treat this as pure sequence-to-sequence translation, FIRMA introduces a hierarchical architecture with complexity-aware routing, proof-preserving attention mechanisms, and multi-objective training that balances formal correctness with natural readability. More specifically, the model processes formal or informal mathematical statements through a hierarchical encoder (symbol, syntax, and semantic layers), followed by a complexity router and proof-preserving attention.\n\n## Performance Results\n\nThrough progressive complexity training on curated datasets from Lean 4 and formal mathematics repositories, FIRMA was evaluated on 200 translation samples across complexity levels. The analysis shows statistically significant improvements of 277.8% over BFS-Prover-V1-7B and 6307.5% over REAL-Prover on overall translation quality metrics. Additionally, ablation studies on 50 samples demonstrate that each architectural component contributes substantially to performance, with removal of any component resulting in 83-85% performance degradation.\n\n## Publication\n\nFIRMA was presented at the 3rd Workshop on Mathematical Natural Language Processing (MathNLP 2025) in Suzhou, China, with code released on GitHub."
    ],
    "durationSeconds": 8.195758420000006,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "0dc9ae2f-34cc-489f-8e14-5d9d8c4cfd32",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "fe782bfd-21b4-4edc-993e-2743bfd061a7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 36 · 2026-05-29T06:22:39.719Z_

```json
{
  "parentUuid": "6e1ce41b-db1f-47cf-a204-d6414f16816a",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "7c457f35-25ef-40a5-900a-472878b616de",
  "timestamp": "2026-05-29T06:22:39.719Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "fe782bfd-21b4-4edc-993e-2743bfd061a7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 37 · 2026-05-29T06:23:57.455Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me synthesize my research and provide a thorough assessment. Let me think about the key aspects:

**What I've learned from research:**

1. **FoVer** (ACL 2026 Findings): Uses Z3/Isabelle to create PRM training labels. Achieves strong generalization. The proposal mentions "overly strict" behavior but I should verify whether FoVer explicitly documents this.

2. **VERGE** (arXiv 2601.20055): Rule-based semantic routing to Z3 or LLM ensemble. 18.7% uplift. Static routing, not learned. The proposal correctly identifies this as context-free.
   
3. **LogicReward** (ICLR 2026): Uses Isabelle for step verification with fallback, operating as an RL framework.

4. **RRM** (arXiv 2510.07774): Identifies miracle steps and reduces them by 71% through rubric rewards, though it was withdrawn from ICLR 2026.

5. **Risk-Controlled Lean-as-Judge** (arXiv 2605.28365): A recent approach from May 2026 showing 43% faithfulness and 28% coverage for 7B autoformalizers, proposing COVCAL for risk-controlled decisions.

6. **FIRMA** (MathNLP 2025): Incorporates a complexity router.

The autoformalization landscape is advancing quickly—recent work has produced 130k lines of topology in just two weeks with various formalizers improving—though faithfulness remains a significant challenge. Looking at the proposal itself, the three-layer architecture combining routing, roundtrip verification, and dual formal/neural checking is clean and well-motivated. The core insight about bridging the gap between overly strict formal-only approaches and unreliable neural-only methods is compelling, and the conditional soundness framing is honest about what the system actually guarantees. The evaluation design and related work coverage are thorough, though I'm wondering whether there's a simpler baseline being overlooked—what if we just tried formal verification directly without the added complexity?

The real question is whether a learned router meaningfully outperforms a straightforward try-formal-first-then-fallback approach. The proposal argues it prevents systematic false alarms from formal verification on non-formalizable steps, but if the roundtrip verification layer already catches most unfaithful formalizations, does the router contribute much beyond computational savings? The router's value hinges on whether it catches false alarms that roundtrip verification misses, or if it's primarily just an efficiency optimization. But there's a deeper issue: attempting formal verification on everything will generate Z3 failures on non-formalizable steps, and the question becomes whether those failures actually cause problems downstream or if they're handled gracefully by the fallback mechanism.

Actually, the try-and-fallback approach has a critical failure mode I'm realizing. If an informal step gets autoformalized somewhat faithfully but Z3 can't prove it because the step relies on implicit knowledge the formal system doesn't capture, it gets flagged as a "miracle step" when it's actually valid informal reasoning. The learned router would prevent sending such steps to Z3 in the first place, which is a more fundamental contribution than just computational efficiency.

Now I'm questioning whether "formalizability" is even a learnable, well-defined property at the individual step level.  It's not intrinsic to the step itself—it depends on the autoformalization model's capabilities, which formal system you're using, what lemmas are available, and the context of preceding steps. The proposal acknowledges these dependencies but ties the label definition to a specific autoformalization model, which raises concerns about whether the router would generalize beyond that particular setup.

The learned formalizability router itself is genuinely novel—no prior work has explicitly tackled learning to classify steps as formalizable versus not. The conditional soundness framing is also intellectually honest and novel, and the miracle step detection mechanism is a clever way to identify where the formal system breaks down.

However, the overall architecture is fairly straightforward: it's essentially combining known autoformalization, known roundtrip verification, known Z3 checking, and known neural PRM with a classifier in front. The real question is whether this actually delivers on its promise. With autoformalization coverage around 28% and faithfulness at 43%, the formal branch might only cover roughly 12% of steps in practice, and that's before accounting for router errors. The conditional soundness guarantee could end up applying to so few steps that it's practically negligible, and while the proposal acknowledges this through honest coverage reporting, there's no clear strategy for what to do if coverage becomes too low to be useful.

The coverage bottleneck is really the critical issue here. If we're looking at 28% coverage times 43% faithfulness times maybe 80% router accuracy, we're down to roughly 19% of steps getting formal guarantees, with the rest relying on neural scores. That's a meaningful question: is a hybrid system that provides formal guarantees on ~19% of steps actually significantly better than a pure neural PRM? And the novelty of "conditional soundness" is technically interesting but might need sharper framing—it's sound miracle detection on a formally-verified subset, which is novel but could feel incremental.

The real question is why learned routing beats naive try-and-fallback for achieving this conditional soundness in practice. There's also a gap between miracle steps and formal derivability that deserves more attention. A step could be formally derivable but still a "miracle" if the model just recalled the answer rather than reasoning through it, or conversely, it might not be formally derivable due to Z3's theory limitations but still be sound. On the novelty front, while nobody's explicitly trained a "formalizability classifier," the autoformalization literature has implicitly tackled this through success rates, so I need to clarify what's genuinely novel here.

The asymmetric cost-aware routing threshold feels like a design detail rather than a standalone contribution—asymmetric thresholds are standard in cost-sensitive classification. But there's something worth exploring: the claim that the router is context-dependent because formalizability depends on the predecessor chain. Is that actually true in practice, or is formalizability mostly determined by step type rather than context?

I should also check whether there's existing work on complexity-aware routing in verification. FIRMA does something similar with its complexity router, though it targets translation quality rather than verification correctness. That's a useful comparison point.

Now I can structure my assessment. The proposal is well-crafted with a genuine gap, technically sound, and probably borderline accept territory at AAAI. But there are critical weaknesses: the effective formal coverage might be too low for the conditional soundness guarantee to matter in practice, and the proposal needs a stronger argument for why even low coverage is valuable.

The key insight is that even 15-20% formal coverage could disproportionately catch the most error-prone steps—the ones where miracle steps are most egregious and detectable. The learned routing also needs sharper positioning against simple try-and-fallback approaches. The real advantage is that learned routing avoids conflating "autoformalization failed" with "step is non-formalizable," which has downstream consequences for PRM quality. Finally, the conditional soundness framing risks feeling tautological—the actual challenge is building a system that correctly identifies which steps to formally verify, not just proving that formal verification itself is sound.

The router could also be reframed as solving a meta-learning problem: it learns the boundary of the autoformalization tool's capabilities. The core logic is sound, the novelty is real—no prior work combines learned routing with roundtrip verification and a formal/neural hybrid PRM—and try-and-fallback is the main ablation to worry about, but the proposal still holds up against it.

The real weakness is whether the coverage will be sufficient in practice, but the idea has room to strengthen rather than fundamental flaws. Time to write this up.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c457f35-25ef-40a5-900a-472878b616de",
  "isSidechain": false,
  "requestId": "req_011CbWNx8ntZFLdodbh5d7rN",
  "type": "assistant",
  "uuid": "3c7ca17b-b480-4453-b7a5-55fb897d27fb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "fe782bfd-21b4-4edc-993e-2743bfd061a7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XiK6Sare8aABeWHJMAASQw",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 924,
      "cache_creation_input_tokens": 1993,
      "cache_read_input_tokens": 25472,
      "output_tokens": 6793,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1993,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 924,
          "output_tokens": 6793,
          "cache_read_input_tokens": 25472,
          "cache_creation_input_tokens": 1993,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1993
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-29T06:25:28.496Z_

Now I have sufficient research to provide a thorough assessment. Let me synthesize my findings.

---

【状态】: 有发掘空间

【前置调研发现】
- **Risk-Controlled Lean-as-Judge (arXiv:2605.28365, May 2026)**: Reports 28% problem coverage and only 43% proof faithfulness for a 7B autoformalizer on MATH-500. Proposes COVCAL for risk-controlled selective verification. This paper is the most critical calibration reference — it quantifies exactly how thin the "formal guarantee" layer can be in practice.
- **FoVer (arXiv:2505.15960, ACL 2026 Findings)**: Uses Z3/Isabelle to synthesize PRM training labels. Generalizes well across 12 benchmarks including non-formal tasks. The "overly strict" claim from the proposal needs to be verified against FoVer's actual reporting — FoVer frames its limitation as limited formal coverage, not necessarily false alarms on informal steps.
- **VERGE (arXiv:2601.20055)**: Rule-based semantic routing (logical vs. commonsense claims) to Z3 or LLM ensemble. 18.7% uplift. Explicitly identifies "learned routing" as future work. Validates the routing-matters hypothesis.
- **LogicReward (arXiv:2512.18196, ICLR 2026)**: Isabelle-based step verification with fallback. Primarily an RL training framework. Its "try-formal-first" approach is indeed the natural baseline for the routing idea.
- **FIRMA (MathNLP 2025)**: Complexity-aware routing for formal-informal translation. Has a complexity router, but targets translation quality, not verification correctness. The proposal correctly differentiates, but FIRMA's router architecture and training methodology may provide useful technical parallels.
- **RRM (arXiv:2510.07774)**: Defines miracle step taxonomy. Reduces miracle steps 71% via rubric rewards. Never attempts formal derivability checking. Withdrawn from ICLR 2026, which may affect its credibility as a foundation for the miracle step concept.
- **Autoformalization landscape (StepFun-Formalizer, FormaRL, etc.)**: Autoformalization is improving rapidly (130k lines of topology in 2 weeks at ~$100 cost), but step-level faithfulness remains a major bottleneck. No prior work explicitly frames "formalizability" as a learnable, context-dependent property for verification routing.
- 调研总结: 领域当前在两个轴上推进——(1) 提升 autoformalization 的覆盖率和忠实度 (Risk-Controlled, roundtrip verification, StepFun)，(2) 构建更强的 neural PRM (GenPRM, ThinkPRM, R-PRM)。将两者通过学习路由桥接的工作尚无人做，但核心瓶颈在于 autoformalization 的有效覆盖率可能太低，导致形式化分支的实际价值存疑。

---

【发掘点 1】
- 维度: significance 提升
- 内容: **有效形式化覆盖率是 significance 的生死线，proposal 必须正面回应而非仅"honest reporting"。** 根据 Risk-Controlled Lean-as-Judge 的数据，7B autoformalizer 在 MATH-500 上 28% coverage × 43% faithfulness ≈ 12% 有效覆盖。即使用 72B autoformalizer 并假设覆盖率翻倍、忠实度提升到 60%，有效覆盖也仅约 56% × 60% ≈ 34%，再乘以 router 准确率（假设 85%），最终约 29% 的 steps 获得形式化保证。一个对 ~29% steps 提供 soundness guarantee、其余 ~71% 只有 neural scoring 的 PRM，审稿人会问：这比 pure neural PRM 好多少？当前 proposal 的策略是"honest coverage reporting"，但这是防守姿态。更有力的 framing 应该是：**argue that formal coverage is disproportionately concentrated on the steps where it matters most**——即 miracle steps 往往发生在明确的逻辑推导环节（代数变换、方程求解、不等式推导），而这些恰好是 autoformalization 最擅长处理的 step 类型。如果能论证"形式化覆盖率虽低，但精准覆盖了 miracle step 高发区"，significance 会大幅提升。建议在 proposal 中增加一个分析维度：formal branch coverage 与 miracle step occurrence 的相关性假设及预实验验证计划。
- 价值: 直接决定审稿人是否认为这个 conditional soundness guarantee 在实践中有意义（Significance 维度）。一个"覆盖 12% 但精准命中高风险 steps"的故事远比"覆盖 12%，剩下全靠 neural"有说服力。
- 调研依据: Risk-Controlled Lean-as-Judge (arXiv:2605.28365) 提供的 43% faithfulness / 28% coverage 数据，以及 RRM (arXiv:2510.07774) 对 miracle step 发生场景的分析（miracle steps 集中在明确的推理跳跃环节）。

【发掘点 2】
- 维度: novelty 锐化
- 内容: **"条件性 soundness"的 framing 有被审稿人视为 tautological 的风险，需要重新定位 novelty 的核心承载点。** 当前 Contribution 1 说"on steps that pass routing AND roundtrip verification, Z3 provides guaranteed miracle detection"——一个严格的审稿人可能反应为"if you can formally verify a step, of course you know whether it's correct; the hard part is getting there reliably, not the guarantee itself." 真正的 novelty 不是"形式验证是 sound 的"（这是 Z3 的固有属性），而是：**构建了一个实用系统，能可靠地识别哪些 steps 可以信赖地送入形式验证管道，并通过 roundtrip verification 确保 formalization 的忠实度**。建议将 Contribution 1 的叙事从"we provide formal soundness guarantees"转向"we solve the practical problem of reliably routing steps to the right verifier, making conditional formal soundness achievable at scale for the first time"。这样 novelty 的重心从 Z3（已知）转移到 routing + roundtrip gating pipeline（新的）。
- 价值: 防止审稿人将核心贡献归因于 Z3 的已有能力而非本文的系统设计（Novelty 维度）。
- 调研依据: FoVer 已经使用 Z3 做 step-level verification；VERGE 已经做了 Z3 routing；本文的真正增量在 routing 的学习化和 roundtrip gating，而非 Z3 验证本身。

【发掘点 3】
- 维度: trivial alternative 威胁
- 内容: **Ablation #6（try-formal-first + neural fallback）是最严重的 trivial alternative 威胁，当前 proposal 对其的回应不够有力。** Proposal 列出三个 learned routing 的优势：(i) 避免 false alarms, (ii) 提供 per-step confidence tier, (iii) 区分 intrinsic formalizability vs extrinsic autoformalization capability。但 (ii) 是 output format 设计，不依赖 learned routing；(iii) 在概念上有趣但不清楚如何在实验中验证。唯一的硬优势是 (i)——避免 non-formalizable steps 被送入 formal pipeline 后产生 false alarms。但如果 Layer 2（roundtrip verification）已经能过滤掉大部分 unfaithful formalizations，那 try-and-fallback + roundtrip verification 可能也能避免大部分 false alarms，只是多花了 autoformalization 的 compute。**建议明确回答：在有 roundtrip verification 作为安全网的情况下，learned router 相比 try-and-fallback 的增量到底在哪里？** 可能的强答案是：(a) roundtrip verification 并非完美——Do LLMs Game Formalization (arXiv:2604.19459) 指出 axiom fabrication 和 premise mistranslation 可以逃过 compilation 检查，也可能逃过 roundtrip verification；learned router 作为第一道防线可以在这些情况下避免错误。(b) compute savings：避免对 ~50-70% non-formalizable steps 做 72B 模型 autoformalization 推理，这是非平凡的 cost reduction。需要在 proposal 中将这两点论证做实。
- 价值: 如果审稿人认为 try-and-fallback 就够了，整个 learned routing 贡献就被消解（Novelty 维度核心威胁）。
- 调研依据: Do LLMs Game Formalization (arXiv:2604.19459) 关于 unfaithfulness 逃过 compilation 检查的发现；LogicReward (arXiv:2512.18196) 的 try-formal-first 设计作为直接 baseline。

【发掘点 4】
- 维度: 前提假设质疑
- 内容: **"Formalizability"作为步骤的内禀属性的假设需要更严谨的论证。** 当前 proposal 将 formalizability label 定义为 "Z3 compilation success AND roundtrip semantic verification pass"——这意味着 formalizability 是相对于特定 autoformalizer（Qwen2.5-Math-72B-Instruct）和特定 formal system（Z3 的 SMT-LIB 片段）的操作性定义，而非步骤的内禀语义属性。随着 autoformalizer 能力提升（2025-2026 autoformalization 进展迅速，如 130k lines of topology in two weeks），今天"non-formalizable"的步骤明天可能变成 formalizable。这产生两个问题：(a) router 的训练标签有时效性，模型可能学到的是当前 autoformalizer 的能力边界而非步骤的内禀属性；(b) 审稿人可能质疑"formalizability"概念的稳定性。**建议在 proposal 中明确区分两个层面：intrinsic formalizability（步骤在原则上是否可以用一阶逻辑/SMT 表达）和 operational formalizability（给定当前 autoformalization 工具链，步骤是否能被可靠地形式化）。Router 学习的是后者，但 contribution 的价值论证应该建立在前者之上——因为 intrinsically formalizable 的步骤恰好是 miracle step 最不应该出现、出现后最值得被形式化检测的地方。** 这个区分不仅让概念更严谨，还能回应"autoformalizer 变好了 router 就没用了"的质疑：即使 autoformalizer 完美了，routing 仍然有价值，因为 intrinsically non-formalizable 的步骤（如直觉判断、heuristic arguments）送入形式验证仍然会产生无意义结果。
- 价值: 概念基础的严谨性直接影响审稿人对整个技术方案的信任度（Novelty + Significance 维度）。
- 调研依据: Autoformalization 快速进展（130k lines of topology, StepFun-Formalizer 等）表明 operational formalizability 边界在快速移动；FIRMA (MathNLP 2025) 的 complexity router 面临类似的"复杂度是相对于什么定义的"问题。

【发掘点 5】
- 维度: 核心 claim 强化
- 内容: **Contribution 3（asymmetric cost-aware routing threshold）不够撑一个独立贡献，建议将其合并或替换。** 非对称代价感知阈值是 cost-sensitive classification 的标准技术（dating back to Elkan 2001），在此场景中应用虽合理，但缺乏技术深度作为独立贡献。建议两种替代方案：(a) 将其降级为 Contribution 2 的实现细节，然后提升一个新贡献——例如"formalizability-guided confidence calibration"：利用 routing decision 和 roundtrip verification 结果，为每个 step 的 PRM score 提供 calibrated uncertainty estimate，formal-verified steps 和 neural-scored steps 的 score 有不同的 reliability interpretation，这对下游 Best-of-N reranking 可能有实际影响（formal-verified positive 的权重应该高于 neural-scored positive）；或 (b) 将重心放在 router 作为"tool competence meta-learner"的角度——router 本质上在学习 autoformalization 工具的能力边界，这是一个更有趣的 framing，可以连接到 tool-use 和 meta-learning 的文献。
- 价值: 三个 contributions 应该每个都有足够的 novelty 承载力。当前 C3 太弱会拉低整体 perceived contribution（Novelty 维度）。
- 调研依据: 基于领域整体趋势判断——asymmetric thresholds 在 ML 中是基础技术；FIRMA 的 complexity router 和 Router-R1 的动态 LLM 选择提供了更有 novelty 的 routing 相关贡献模式。

Sources:
- [Risk-Controlled Lean-as-Judge](https://arxiv.org/abs/2605.28365)
- [FoVer: Efficient PRM Training Data Synthesis via Formal Verification](https://arxiv.org/abs/2505.15960)
- [VERGE: Formal Refinement and Guidance Engine](https://arxiv.org/abs/2601.20055)
- [LogicReward: Step-Wise Logical Supervision](https://arxiv.org/abs/2512.18196)
- [FIRMA: Bidirectional Formal-Informal Mathematical Language Alignment](https://aclanthology.org/2025.mathnlp-main.5/)
- [Curing Miracle Steps with Rubric Rewards](https://arxiv.org/abs/2510.07774)
- [Do LLMs Game Formalization?](https://arxiv.org/html/2604.19459)
- [StepFun-Formalizer](https://arxiv.org/pdf/2508.04440)
- [Router-R1: Multi-Round Routing via RL](https://openreview.net/forum?id=DWf4vroKWJ)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c7ca17b-b480-4453-b7a5-55fb897d27fb",
  "isSidechain": false,
  "requestId": "req_011CbWNx8ntZFLdodbh5d7rN",
  "type": "assistant",
  "uuid": "7055626e-e7c5-40ff-9646-28f90f6d7417",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "fe782bfd-21b4-4edc-993e-2743bfd061a7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XiK6Sare8aABeWHJMAASQw",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 924,
      "cache_creation_input_tokens": 1993,
      "cache_read_input_tokens": 25472,
      "output_tokens": 6793,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1993,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 924,
          "output_tokens": 6793,
          "cache_read_input_tokens": 25472,
          "cache_creation_input_tokens": 1993,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1993
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Runtime record

_source line 39_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Formally-Routed Process Reward Models for Sound Miracle Step Detection  ## Core Problem  No existing PRM exploits the formalizability structure of reasoning steps. Formal-only PRMs (FoVer, PRoSFI) p…",
  "leafUuid": "7055626e-e7c5-40ff-9646-28f90f6d7417",
  "sessionId": "fe782bfd-21b4-4edc-993e-2743bfd061a7"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "ai-title",
  "aiTitle": "Learned routing for formal process reward models",
  "sessionId": "fe782bfd-21b4-4edc-993e-2743bfd061a7"
}
```

---

### Runtime record

_source line 41_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Formally-Routed Process Reward Models for Sound Miracle Step Detection  ## Core Problem  No existing PRM exploits the formalizability structure of reasoning steps. Formal-only PRMs (FoVer, PRoSFI) p…",
  "leafUuid": "7055626e-e7c5-40ff-9646-28f90f6d7417",
  "sessionId": "fe782bfd-21b4-4edc-993e-2743bfd061a7"
}
```

---

### Runtime record

_source line 42_

```json
{
  "type": "ai-title",
  "aiTitle": "Learned routing for formal process reward models",
  "sessionId": "fe782bfd-21b4-4edc-993e-2743bfd061a7"
}
```

---
