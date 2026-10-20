# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Formally-Routed Process Reward Mo

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 39
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-3/644ee0d4-56af-4ee5-8097-233dab1a01f6.jsonl`
- **Structured JSON:** [`d947de5614191477cd2e.json`](../../sessions/d9/d947de5614191477cd2e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-29T06:38:24.066Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-29T06:38:24.066Z",
  "sessionId": "644ee0d4-56af-4ee5-8097-233dab1a01f6",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Formally-Routed Process Reward Models for Sound Miracle Step Detection\n\n## Core Problem\n\nNo existing PRM exploits the formalizability structure of reasoning steps. Formal-only PRMs (FoVer, PRoSFI) provide high precision but suffer documented overly-strict behavior on informal steps. Neural-only PRMs (GenPRM, ThinkPRM, R-PRM, ARES) provide broad coverage but no formal derivability guarantees. Hybrid systems use either hand-crafted routing (VERGE) or unlearned try-and-fallback (LogicReward). The critical gap: a learned, context-dependent formalizability router that dispatches each step to the appropriate verifier—with roundtrip-verified formal checking providing sound miracle step detection on formalizable steps while neural verification covers the rest.\n\n## Research Opportunity\n\nThree converging gaps create a unique opening:\n\n(1) VERGE (arXiv:2601.20055) demonstrates 18.7% uplift from routing between Z3 and neural verifiers but uses rule-based routing over static claim types (logical vs. commonsense)—context-free and not learned. The paper explicitly identifies learned routing as the open next step.\n\n(2) LogicReward (ICLR 2026, arXiv:2512.18196) implements Isabelle step verification with token-probability fallback—a \"try-formal-first\" strategy. This cannot distinguish \"step is intrinsically non-formalizable\" from \"autoformalization failed on a formalizable step,\" producing systematic false alarms on non-formalizable steps (the same overly-strict behavior documented in FoVer).\n\n(3) RRM (arXiv:2510.07774, withdrawn from ICLR 2026) defines the miracle step taxonomy and reduces miracle steps by 71% via rubric rewards, but never tested formal derivability from predecessors. FoVer's public codebase (arXiv:2505.15960), GenPRM's open weights (arXiv:2504.00891), and Risk-Controlled Lean-as-Judge (arXiv:2605.28365) with its honest quantification of autoformalization limits (43% faithfulness, 28% coverage for 7B autoformalizer on MATH-500) provide infrastructure and calibration data for a hybrid system at academic compute budgets.\n\n## Key Insight: Conditional Formal Soundness for Miracle Detection\n\nA miracle step is an unjustified logical leap—step S_i that does not follow from predecessors {S_1,...,S_{i-1}}. When a step is faithfully formalized and submitted to Z3 for predecessor-derivability checking, miracle steps produce Z3 UNSAT (not derivable). This is near-definitional: on the faithfully-formalized subset, miracle step detection reduces to Z3 derivability failure.\n\nThe critical qualifier is \"faithfully formalized.\" Autoformalization is unreliable: Risk-Controlled Lean-as-Judge (arXiv:2605.28365) reports only 43% faithfulness, and Do LLMs Game Formalization? (arXiv:2604.19459) identifies two unfaithfulness modes—axiom fabrication and premise mistranslation—that evade compilation-based detection. Therefore, the soundness guarantee is conditional: it holds only for steps that pass both formalizability routing AND roundtrip verification of autoformalization faithfulness (arXiv:2604.25031).\n\nFormalRoute-PRM makes this conditionality explicit and operationalizable through a three-layer pipeline: learned formalizability routing → roundtrip faithfulness verification → formal or neural verification.\n\n## Contributions\n\n1. **Conditional sound miracle detection.** On steps that the router identifies as formalizable AND that pass roundtrip faithfulness verification, Z3 predecessor-derivability checking provides guaranteed miracle step detection. This is the first PRM offering formal soundness guarantees for any subset of reasoning steps, with honest coverage reporting following Risk-Controlled methodology.\n\n2. **Learned context-dependent formalizability routing.** Unlike VERGE's static claim-type routing (context-free) and LogicReward's unlearned try-and-fallback, our Qwen3-8B router predicts formalizability conditioned on the full predecessor chain {S_1,...,S_{i-1}}. Context-dependent formalizability prediction is a non-trivial learning problem because a step's formalizability depends on: (a) the formal context established by predecessors (which definitions and variables are already formalized), (b) the autoformalization tool's capability boundary for this step type, and (c) the step's position in the proof (early declarative steps are more formalizable than later heuristic steps). Rule-based approaches cannot capture these context dependencies. Compared to try-and-fallback, learned routing provides three advantages: (i) avoids systematic false alarms from formal verification on non-formalizable steps (FoVer's documented overly-strict behavior), (ii) produces per-step verification confidence signals distinguishing formally guaranteed vs. neurally estimated scores, and (iii) distinguishes intrinsic step formalizability from extrinsic autoformalization capability.\n\n3. **Asymmetric cost-aware routing threshold.** Router errors have asymmetric costs: routing non-formalizable steps to Z3 produces false alarms (overly strict); routing formalizable steps to neural verification risks missing miracle steps. The router threshold is optimized to favor recall (prefer sending to Z3), with explicit cost-asymmetry analysis. This design is informed by FoVer's documented overly-strict behavior and Risk-Controlled Lean-as-Judge's faithfulness quantification.\n\n## Research Landscape\n\n**Formal-only PRMs.** FoVer (ACL 2026, arXiv:2505.15960) achieves 85.8 AUROC on ProcessBench via Z3/Isabelle-verified training labels, but produces overly-strict scores on informal reasoning steps. PRoSFI (arXiv:2603.29500) generates structured formal intermediaries for prover verification on the generation side.\n\n**Neural PRMs.** GenPRM (AAAI 2026, arXiv:2504.00891): 7B surpasses Qwen2.5-Math-PRM-72B on ProcessBench via generative CoT and code verification. ThinkPRM (arXiv:2504.16828): 14B trained on only 8K process labels outperforms discriminative PRMs trained on 100× more data; establishes token-budget-normalized comparison paradigm (+7.2% over LLM-as-Judge at same budget). R-PRM (EMNLP 2025, arXiv:2503.21295): +13.9 F1 on ProcessBench and +8.5 F1 on PRMBench via three-stage cold-start, DPO, inference-time scaling. ARES (2025): 72.1% Macro-F1 on PRMBench via autoregressive entailment, entirely dependent on LLM calibration.\n\n**Hybrid systems.** VERGE (arXiv:2601.20055): rule-based semantic routing (logical vs. commonsense claim types) to Z3 or LLM ensemble, 18.7% uplift—routing is static, context-free, not learned. LogicReward (ICLR 2026, arXiv:2512.18196): Isabelle step verification with token-probability fallback; 8B model surpasses GPT-4o by 11.6% on logical reasoning but is an RL training framework, not a standalone PRM. FIRMA (MathNLP 2025, ACL Anthology 2025.mathnlp-main.5): bidirectional formal-informal mathematical language alignment with a complexity router—but this routes for translation quality, not verification correctness; the target function and training signal are fundamentally different from formalizability routing for verification.\n\n**Miracle step detection.** RRM (arXiv:2510.07774, withdrawn from ICLR 2026) defines the miracle step taxonomy and reduces miracle steps by 71% via rubric rewards, without formal derivability checking.\n\n**Autoformalization limits.** Risk-Controlled Lean-as-Judge (arXiv:2605.28365): 43% faithfulness, 28% coverage for 7B autoformalizer. Do LLMs Game Formalization? (arXiv:2604.19459): identifies axiom fabrication and premise mistranslation as unfaithfulness modes evading compilation checks. Faithful Autoformalization via Roundtrip Verification (arXiv:2604.25031): provides roundtrip verification methodology for detecting unfaithful formalizations.\n\n## Proposed Approach\n\n**Three-layer pipeline:**\n\n**Layer 1: Formalizability Router.** Qwen3-8B classifier trained on FoVer Z3 verification labels + autoformalization success signals. Labels defined as: formalizable = Z3 compilation success AND roundtrip semantic verification pass; non-formalizable = autoformalization failure OR roundtrip failure OR Z3 timeout. Input: step S_i + predecessor context {S_1,...,S_{i-1}}. Output: formalizability probability. Threshold set via asymmetric cost-aware optimization favoring recall.\n\n**Layer 2: Roundtrip Faithfulness Verification.** Steps routed to formal branch undergo autoformalization (via Qwen2.5-Math-72B-Instruct) → roundtrip verification (arXiv:2604.25031): back-translate the formal statement to natural language and check semantic equivalence with the original step. Steps failing roundtrip verification are redirected to neural branch. This layer gates the soundness guarantee.\n\n**Layer 3: Verification.**\n- Formal branch (roundtrip-verified): Z3 predecessor-derivability checking. Z3 UNSAT → miracle step detected (sound). Z3 SAT → step verified with formal guarantee.\n- Neural branch (non-formalizable or roundtrip-failed): GenPRM-7B scoring with ARES-style calibrated entailment (Platt scaling on held-out validation set). Best-effort verification without formal guarantees.\n\n**Output.** Per-step score with verification confidence tier: (a) roundtrip-verified + Z3-verified (highest confidence), (b) roundtrip-failed but router-formalizable (medium—formal attempt inconclusive), (c) router-non-formalizable + neurally scored (neural confidence), (d) router uncertain (lowest confidence).\n\n## Evaluation Design\n\n**Benchmarks and metrics.**\n- ProcessBench: F1 (aligned with GenPRM, R-PRM) + AUROC (aligned with FoVer)\n- PRMBench (ACL 2025, arXiv:2501.03124): PRMScore + error-type breakdown\n- Best-of-N reranking: MATH-500, AIME24 using Qwen2.5-Math-7B-Instruct as generator; report Pass@1, majority voting, PRM reranking (N=8,16,64)\n- OOD generalization: GPQA-Diamond (scientific reasoning, following ThinkPRM)\n- Miracle step detection: precision/recall/F1 on (a) RRM miracle taxonomy annotations (Yuan et al., 2025) if publicly available, (b) PRMBench error-type categories as primary proxy if RRM data unavailable, (c) self-constructed human-annotated set (200–300 steps, 2–3 annotators, inter-annotator agreement via Cohen's kappa)\n\n**Baseline matrix.**\n- Pure neural: GenPRM-7B, ThinkPRM-14B, R-PRM-7B, Qwen2.5-Math-PRM-72B\n- Pure formal: FoVer-7B\n- Hybrid: VERGE (hand-crafted routing), Naive Hybrid (FoVer Z3 try-and-fallback to GenPRM, no learned router)\n- LLM-as-Judge: GPT-4o, QwQ-32B\n- Compute-matched: GenPRM majority voting under equivalent total token budget (including autoformalization cost)\n- LogicReward (ICLR 2026): conceptual comparison on method design; quantitative comparison where applicable with methodology differences noted (RL framework vs. standalone PRM)\n\n**Ablation studies.**\n1. Formal-only: all steps → Z3 (low coverage penalty)\n2. Neural-only: all steps → GenPRM (miracle step leakage)\n3. Random routing: 50/50 formal/neural (isolates routing from ensemble)\n4. Oracle routing: ground-truth formalizability labels (performance ceiling)\n5. Router threshold sweep: coverage-accuracy trade-off across formalizability thresholds, visualizing asymmetric cost impact\n6. Try-formal-first + neural fallback: no router, attempt Z3 on all steps, fallback on failure (trivial alternative baseline—directly tests whether learned routing outperforms unlearned try-and-fallback)\n7. Router label noise analysis: compare router trained on noisy auto-labels vs. router trained on human-cleaned labels (500–1000 examples); report label precision via human audit of 200–300 \"non-formalizable\" training labels\n\n**Compute fairness.** Report per-step average inference time and total FLOPs for all systems, explicitly including autoformalization cost (Qwen2.5-Math-72B-Instruct inference) in FormalRoute-PRM's compute. Plot accuracy vs. compute Pareto curve. Compute-matched GenPRM majority voting as explicit comparison following ThinkPRM's token-budget-normalized paradigm.\n\n**Router analysis.** Classification accuracy, precision, recall on in-domain (formal reasoning) and out-of-domain (general math, GPQA-Diamond) splits. Few-shot domain adaptation ablation with ProcessBench/PRMBench samples. Oracle formalizability labels (human-annotated, 100–200 examples) to quantify router quality ceiling. Formalizability positive rate, formal branch coverage, roundtrip verification pass rate per benchmark.\n\n**Honest coverage reporting.** Following Risk-Controlled Lean-as-Judge (arXiv:2605.28365) methodology: report autoformalization coverage, roundtrip faithfulness rate, formal branch activation rate, and effective soundness coverage (= steps receiving formal guarantee / total steps) per benchmark.\n\n## Compute Budget\n\n- Router training: Qwen3-8B LoRA fine-tuning on ~80K FoVer-derived labels, ≈4–8 GPU-hours on single H100\n- Autoformalization: Qwen2.5-Math-72B-Instruct inference for formalizable steps (est. 30–50% of total); dominant compute cost\n- Z3 solving: millisecond-scale per formula, negligible\n- GenPRM-7B inference: standard 7B inference for neural branch steps\n- Roundtrip verification: one additional LLM call per formal-branch step for back-translation + semantic equivalence check\n- Total: training <1 day, full evaluation pipeline <5 days on single-node 8×H100 (dominated by autoformalization inference)\n\n## Key References\n\n- FoVer: PRM Data Synthesis via Formal Verification (ACL 2026, arXiv:2505.15960)\n- GenPRM: Scaling Test-Time Compute of PRMs (AAAI 2026, arXiv:2504.00891)\n- LogicReward: Step-Wise Logical Supervision (ICLR 2026, arXiv:2512.18196)\n- VERGE: Formal Refinement and Guidance Engine (arXiv 2026, arXiv:2601.20055)\n- Curing Miracle Steps with Rubric Rewards (arXiv 2025, arXiv:2510.07774)\n- Risk-Controlled Lean-as-Judge (arXiv 2026, arXiv:2605.28365)\n- ARES: Autoregressive Entailment Scoring (2025)\n- ThinkPRM: Process Reward Models That Think (arXiv:2504.16828)\n- R-PRM: Reasoning-Driven Process Reward Modeling (EMNLP 2025, arXiv:2503.21295)\n- PRMBench: Fine-grained PRM Benchmark (ACL 2025, arXiv:2501.03124)\n- PRoSFI: Structured Formal Intermediaries (arXiv:2603.29500)\n- Faithful Autoformalization via Roundtrip Verification (arXiv:2604.25031)\n- FIRMA: Formal-Informal Mathematical Language Alignment (MathNLP 2025, ACL Anthology 2025.mathnlp-main.5)\n- Do LLMs Game Formalization? (arXiv:2604.19459)"
}
```

---

### Runtime record

_source line 2 · 2026-05-29T06:38:24.072Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-29T06:38:24.072Z",
  "sessionId": "644ee0d4-56af-4ee5-8097-233dab1a01f6"
}
```

---

## Round 1

37 recorded events

### User

_source line 3 · 2026-05-29T06:38:24.140Z_

【任务】: 请评估以下 proposal 的客观中稿概率。
必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。

【proposal】:
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
  "promptId": "02da38a2-c80a-4990-b6e8-13012729d6f2",
  "type": "user",
  "uuid": "0ea74062-f08c-4c1d-90c1-83ca941c797e",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "644ee0d4-56af-4ee5-8097-233dab1a01f6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-29T06:38:24.138Z_

```json
{
  "parentUuid": "0ea74062-f08c-4c1d-90c1-83ca941c797e",
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
  "uuid": "b2679bbd-0b6e-42cf-bb52-44e56fe2dbb2",
  "timestamp": "2026-05-29T06:38:24.138Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "644ee0d4-56af-4ee5-8097-233dab1a01f6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-29T06:38:24.138Z_

```json
{
  "parentUuid": "b2679bbd-0b6e-42cf-bb52-44e56fe2dbb2",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "a3f71219-8236-4427-a645-e3678d8325e9",
  "timestamp": "2026-05-29T06:38:24.138Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "644ee0d4-56af-4ee5-8097-233dab1a01f6",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Formally-Routed Process Reward Models for Sound Miracle Step Detection  ## Core Problem  No existing PRM exploit…",
  "leafUuid": "a3f71219-8236-4427-a645-e3678d8325e9",
  "sessionId": "644ee0d4-56af-4ee5-8097-233dab1a01f6"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Learned routing for hybrid formal-neural process reward models",
  "sessionId": "644ee0d4-56af-4ee5-8097-233dab1a01f6"
}
```

---

### Assistant

_source line 8 · 2026-05-29T06:38:27.831Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to evaluate a research proposal for AAAI 2026 submission. I need to first conduct thorough web searches to understand the current landscape, then provide a comprehensive evaluation following the specified format.

Let me start by searching for the key related works and the current state of the field.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a3f71219-8236-4427-a645-e3678d8325e9",
  "isSidechain": false,
  "requestId": "req_011CbWQ9khJs3dQacRGMLajg",
  "type": "assistant",
  "uuid": "8e0f8186-4037-4f86-a3d6-cc7788c4c334",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "644ee0d4-56af-4ee5-8097-233dab1a01f6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FzkqNG3mDcC9pQZrPaNCRp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 18958,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 189,
          "cache_read_input_tokens": 18958,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 0
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

_source line 9 · 2026-05-29T06:38:28.388Z_

I'll start by conducting thorough web searches to understand the current research landscape before evaluating this proposal. Let me search for the key related works and field status.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e0f8186-4037-4f86-a3d6-cc7788c4c334",
  "isSidechain": false,
  "requestId": "req_011CbWQ9khJs3dQacRGMLajg",
  "type": "assistant",
  "uuid": "c1114a68-d5c7-4744-8d56-49d1a286290d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "644ee0d4-56af-4ee5-8097-233dab1a01f6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FzkqNG3mDcC9pQZrPaNCRp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 18958,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 189,
          "cache_read_input_tokens": 18958,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 0
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

_source line 10 · 2026-05-29T06:38:28.731Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01XsJbPsCQmjZs39s1xxkwm6`</summary>

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
  "parentUuid": "c1114a68-d5c7-4744-8d56-49d1a286290d",
  "isSidechain": false,
  "requestId": "req_011CbWQ9khJs3dQacRGMLajg",
  "type": "assistant",
  "uuid": "2d705dde-e180-40f9-8d36-905070ccba7b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "644ee0d4-56af-4ee5-8097-233dab1a01f6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FzkqNG3mDcC9pQZrPaNCRp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 18958,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 189,
          "cache_read_input_tokens": 18958,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 0
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

_source line 11 · 2026-05-29T06:38:28.774Z_

<details><summary>↩ Tool result · `toolu_01XsJbPsCQmjZs39s1xxkwm6`</summary>

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
  "parentUuid": "2d705dde-e180-40f9-8d36-905070ccba7b",
  "isSidechain": false,
  "promptId": "02da38a2-c80a-4990-b6e8-13012729d6f2",
  "type": "user",
  "uuid": "3945661b-ae11-4e4e-9887-d0f536ae7b2f",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "2d705dde-e180-40f9-8d36-905070ccba7b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "644ee0d4-56af-4ee5-8097-233dab1a01f6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-29T06:38:31.422Z_

Now let me conduct the required research searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3945661b-ae11-4e4e-9887-d0f536ae7b2f",
  "isSidechain": false,
  "requestId": "req_011CbWQA6XAa9KKh7BMGJECx",
  "type": "assistant",
  "uuid": "2e32db0d-ea0d-4011-859d-7dcd228ab471",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "644ee0d4-56af-4ee5-8097-233dab1a01f6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019SSBSFX8MpFHjFmVu33D7R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 717,
      "cache_read_input_tokens": 18958,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 717,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 79,
          "cache_read_input_tokens": 18958,
          "cache_creation_input_tokens": 717,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 717
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

_source line 13 · 2026-05-29T06:38:31.426Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TVh7JEXfmctAyVJFuB93Qr`</summary>

```json
{
  "query": "Process Reward Model PRM formal verification hybrid 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e32db0d-ea0d-4011-859d-7dcd228ab471",
  "isSidechain": false,
  "requestId": "req_011CbWQA6XAa9KKh7BMGJECx",
  "type": "assistant",
  "uuid": "d4fbddbe-8c4f-45cc-975e-cf08cbb367cf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "644ee0d4-56af-4ee5-8097-233dab1a01f6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019SSBSFX8MpFHjFmVu33D7R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 717,
      "cache_read_input_tokens": 18958,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 717,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 79,
          "cache_read_input_tokens": 18958,
          "cache_creation_input_tokens": 717,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 717
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

_source line 14 · 2026-05-29T06:38:38.773Z_

<details><summary>↩ Tool result · `toolu_01TVh7JEXfmctAyVJFuB93Qr`</summary>

```text
Web search results for query: "Process Reward Model PRM formal verification hybrid 2025 2026"

Links: [{"title":"[2505.15960] Efficient PRM Training Data Synthesis via Formal Verification","url":"https://arxiv.org/abs/2505.15960"},{"title":"Generalizable Process Reward Models via Formally Verified Training Data | OpenReview","url":"https://openreview.net/forum?id=LAejsDitr3"},{"title":"Generalizable Process Reward Models via Formally Verified Training Data","url":"https://arxiv.org/pdf/2505.15960"},{"title":"Process Reward Models That Think | OpenReview","url":"https://openreview.net/forum?id=V727xqBYIW"},{"title":"A Survey of Process Reward Models: From Outcome Signals to Process","url":"https://arxiv.org/pdf/2510.08049"},{"title":"Process-supervised Reward Models (PRMs)","url":"https://www.emergentmind.com/topics/process-supervised-reward-models-prm"},{"title":"A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models","url":"https://arxiv.org/html/2510.08049v3"},{"title":"GitHub - RyanLiu112/Awesome-Process-Reward-Models: A comprehensive collection of process reward models. · GitHub","url":"https://github.com/RyanLiu112/Awesome-Process-Reward-Models"}]

Based on the web search results, here are the key findings on Process Reward Models (PRMs) with formal verification approaches in 2025-2026:

## Key Research on PRM with Formal Verification

Process Reward Models (PRMs) have emerged as a promising approach for improving LLM reasoning capabilities by providing process supervision over reasoning traces. However, existing approaches for constructing PRM training data remain costly and noisy, as they typically rely on human annotation or sampling-based labeling methods that require repeated LLM calls.

### FoVer Framework

A significant recent development is FoVer, a framework that synthesizes PRM training data from formal reasoning tasks by annotating step-level error labels using formal verification tools such as Z3 and Isabelle. By leveraging formal verification, FoVer enables efficient and accurate PRM data construction without requiring human annotation or additional LLM calls.

PRMs trained with FoVer improve performance on diverse reasoning tasks, including MATH, AIME, and MMLU.

## Hybrid and Alternative Approaches

Beyond formal verification, hybrid approaches like Web-Shepherd and ActPRM combine human oversight with automatic checks or use active learning to selectively query annotators, reducing labeling costs while maintaining supervision quality.

Additionally, ThinkPRM builds data-efficient PRMs as verbalized step-wise reward models that verify every step by generating a verification chain-of-thought, requiring orders of magnitude fewer process labels than discriminative PRMs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d4fbddbe-8c4f-45cc-975e-cf08cbb367cf",
  "isSidechain": false,
  "promptId": "02da38a2-c80a-4990-b6e8-13012729d6f2",
  "type": "user",
  "uuid": "d4dc0217-66f1-475d-b174-5d4982b4eb89",
  "toolUseResult": {
    "query": "Process Reward Model PRM formal verification hybrid 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01U7REiKR8vipvPtGjcvfC9z",
        "content": [
          {
            "title": "[2505.15960] Efficient PRM Training Data Synthesis via Formal Verification",
            "url": "https://arxiv.org/abs/2505.15960"
          },
          {
            "title": "Generalizable Process Reward Models via Formally Verified Training Data | OpenReview",
            "url": "https://openreview.net/forum?id=LAejsDitr3"
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
            "title": "A Survey of Process Reward Models: From Outcome Signals to Process",
            "url": "https://arxiv.org/pdf/2510.08049"
          },
          {
            "title": "Process-supervised Reward Models (PRMs)",
            "url": "https://www.emergentmind.com/topics/process-supervised-reward-models-prm"
          },
          {
            "title": "A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models",
            "url": "https://arxiv.org/html/2510.08049v3"
          },
          {
            "title": "GitHub - RyanLiu112/Awesome-Process-Reward-Models: A comprehensive collection of process reward models. · GitHub",
            "url": "https://github.com/RyanLiu112/Awesome-Process-Reward-Models"
          }
        ]
      },
      "Based on the web search results, here are the key findings on Process Reward Models (PRMs) with formal verification approaches in 2025-2026:\n\n## Key Research on PRM with Formal Verification\n\nProcess Reward Models (PRMs) have emerged as a promising approach for improving LLM reasoning capabilities by providing process supervision over reasoning traces. However, existing approaches for constructing PRM training data remain costly and noisy, as they typically rely on human annotation or sampling-based labeling methods that require repeated LLM calls.\n\n### FoVer Framework\n\nA significant recent development is FoVer, a framework that synthesizes PRM training data from formal reasoning tasks by annotating step-level error labels using formal verification tools such as Z3 and Isabelle. By leveraging formal verification, FoVer enables efficient and accurate PRM data construction without requiring human annotation or additional LLM calls.\n\nPRMs trained with FoVer improve performance on diverse reasoning tasks, including MATH, AIME, and MMLU.\n\n## Hybrid and Alternative Approaches\n\nBeyond formal verification, hybrid approaches like Web-Shepherd and ActPRM combine human oversight with automatic checks or use active learning to selectively query annotators, reducing labeling costs while maintaining supervision quality.\n\nAdditionally, ThinkPRM builds data-efficient PRMs as verbalized step-wise reward models that verify every step by generating a verification chain-of-thought, requiring orders of magnitude fewer process labels than discriminative PRMs."
    ],
    "durationSeconds": 7.339669740000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d4fbddbe-8c4f-45cc-975e-cf08cbb367cf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "644ee0d4-56af-4ee5-8097-233dab1a01f6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-29T06:38:41.134Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Uatt5zp9kcLx2Htzn82hj1`</summary>

```json
{
  "query": "VERGE formal refinement guidance engine Z3 routing verification arXiv 2601.20055"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4dc0217-66f1-475d-b174-5d4982b4eb89",
  "isSidechain": false,
  "requestId": "req_011CbWQAq7Es99ZNtARqXVzN",
  "type": "assistant",
  "uuid": "9fddb39b-79a0-45ca-a157-2ee5b9386671",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "644ee0d4-56af-4ee5-8097-233dab1a01f6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F2Cbbk7tjeuCtKt2PJDXsR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 798,
      "cache_read_input_tokens": 19675,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 798,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 19675,
          "cache_creation_input_tokens": 798,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 798
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

_source line 16 · 2026-05-29T06:38:53.732Z_

<details><summary>↩ Tool result · `toolu_01Uatt5zp9kcLx2Htzn82hj1`</summary>

```text
Web search results for query: "VERGE formal refinement guidance engine Z3 routing verification arXiv 2601.20055"

Links: [{"title":"Paper page - VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning","url":"https://huggingface.co/papers/2601.20055"},{"title":"[2601.20055] VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning","url":"https://arxiv.org/abs/2601.20055"},{"title":"[Literature Review] VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning","url":"https://www.themoonlight.io/en/review/verge-formal-refinement-and-guidance-engine-for-verifiable-llm-reasoning"},{"title":"VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning","url":"https://arxiv.org/html/2601.20055v1"},{"title":"dblp: VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning.","url":"https://dblp.uni-trier.de/rec/journals/corr/abs-2601-20055.html"},{"title":"VERGE: Formal Refinement and Guidance Engine for Verifiable ...","url":"https://ubos.tech/verge-formal-refinement-and-guidance-engine-for-verifiable-llm-reasoning-2/"},{"title":"Verge: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning | Hacker News","url":"https://news.ycombinator.com/item?id=46813257"},{"title":"Formal Refinement and Guidance Engine for Verifiable ...","url":"https://www.researchgate.net/publication/400178327_VERGE_Formal_Refinement_and_Guidance_Engine_for_Verifiable_LLM_Reasoning"},{"title":"Emergent Formal Verification: How an Autonomous AI Ecosystem Independently Discovered SMT-Based Safety Across Six Domains","url":"https://arxiv.org/pdf/2603.21149"}]

Based on the search results, here's what I found about the paper arXiv 2601.20055:

## VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning

VERGE is a neuro-symbolic framework designed to bridge the semantic gap between LLM fluency and formal correctness by addressing the "all-or-nothing" limitation of traditional solvers.

### Key Innovation: Semantic Routing

A key innovation is Semantic Routing, which dynamically classifies atomic claims to handle non-formalizable natural language; verifiable logic is sent to SMT solvers (Z3) for proof, while ambiguous or commonsense claims are routed to a consensus-based "soft verifier," preventing the system from breaking on vague predicates.

### Three Main Contributions

The framework introduces three key innovations: (1) multi-model consensus via formal semantic equivalence checking to ensure logic-level alignment between candidates, (2) semantic routing that directs different claim types to appropriate verification strategies: symbolic solvers for logical claims and LLM ensembles for commonsense reasoning, and (3) precise logical error localization via Minimal Correction Subsets (MCS), which pinpoint the exact subset of claims to revise.

### Verification Process

For formalizable claims, a Z3 solver checks satisfiability. Claims are categorized as Contradictory, Entailed, Possible, or Unknown. For non-formalizable claims, an ensemble of LLM judges assigns confidence-weighted verdicts.

### Performance

The system enables the model to iteratively refine its reasoning from "probabilistic" to "provable" with an 18.7% performance uplift.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9fddb39b-79a0-45ca-a157-2ee5b9386671",
  "isSidechain": false,
  "promptId": "02da38a2-c80a-4990-b6e8-13012729d6f2",
  "type": "user",
  "uuid": "bc1acf4f-4195-46b1-962b-d09199a2898c",
  "toolUseResult": {
    "query": "VERGE formal refinement guidance engine Z3 routing verification arXiv 2601.20055",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NGWKWeAqq3zBAjyDoQognT",
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
            "title": "[Literature Review] VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning",
            "url": "https://www.themoonlight.io/en/review/verge-formal-refinement-and-guidance-engine-for-verifiable-llm-reasoning"
          },
          {
            "title": "VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning",
            "url": "https://arxiv.org/html/2601.20055v1"
          },
          {
            "title": "dblp: VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning.",
            "url": "https://dblp.uni-trier.de/rec/journals/corr/abs-2601-20055.html"
          },
          {
            "title": "VERGE: Formal Refinement and Guidance Engine for Verifiable ...",
            "url": "https://ubos.tech/verge-formal-refinement-and-guidance-engine-for-verifiable-llm-reasoning-2/"
          },
          {
            "title": "Verge: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning | Hacker News",
            "url": "https://news.ycombinator.com/item?id=46813257"
          },
          {
            "title": "Formal Refinement and Guidance Engine for Verifiable ...",
            "url": "https://www.researchgate.net/publication/400178327_VERGE_Formal_Refinement_and_Guidance_Engine_for_Verifiable_LLM_Reasoning"
          },
          {
            "title": "Emergent Formal Verification: How an Autonomous AI Ecosystem Independently Discovered SMT-Based Safety Across Six Domains",
            "url": "https://arxiv.org/pdf/2603.21149"
          }
        ]
      },
      "Based on the search results, here's what I found about the paper arXiv 2601.20055:\n\n## VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning\n\nVERGE is a neuro-symbolic framework designed to bridge the semantic gap between LLM fluency and formal correctness by addressing the \"all-or-nothing\" limitation of traditional solvers.\n\n### Key Innovation: Semantic Routing\n\nA key innovation is Semantic Routing, which dynamically classifies atomic claims to handle non-formalizable natural language; verifiable logic is sent to SMT solvers (Z3) for proof, while ambiguous or commonsense claims are routed to a consensus-based \"soft verifier,\" preventing the system from breaking on vague predicates.\n\n### Three Main Contributions\n\nThe framework introduces three key innovations: (1) multi-model consensus via formal semantic equivalence checking to ensure logic-level alignment between candidates, (2) semantic routing that directs different claim types to appropriate verification strategies: symbolic solvers for logical claims and LLM ensembles for commonsense reasoning, and (3) precise logical error localization via Minimal Correction Subsets (MCS), which pinpoint the exact subset of claims to revise.\n\n### Verification Process\n\nFor formalizable claims, a Z3 solver checks satisfiability. Claims are categorized as Contradictory, Entailed, Possible, or Unknown. For non-formalizable claims, an ensemble of LLM judges assigns confidence-weighted verdicts.\n\n### Performance\n\nThe system enables the model to iteratively refine its reasoning from \"probabilistic\" to \"provable\" with an 18.7% performance uplift."
    ],
    "durationSeconds": 12.591364117999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "9fddb39b-79a0-45ca-a157-2ee5b9386671",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "644ee0d4-56af-4ee5-8097-233dab1a01f6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-29T06:38:56.590Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QsoauV8gpreXhbfACXvyaM`</summary>

```json
{
  "query": "LogicReward ICLR 2026 Isabelle step verification token probability arXiv 2512.18196"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc1acf4f-4195-46b1-962b-d09199a2898c",
  "isSidechain": false,
  "requestId": "req_011CbWQBw2iTyr5gkJGoEWrZ",
  "type": "assistant",
  "uuid": "fb929d9b-ef76-456d-8085-999a7052443f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "644ee0d4-56af-4ee5-8097-233dab1a01f6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J9Heqat8QjT1n7tcJuETJA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1026,
      "cache_read_input_tokens": 20473,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1026,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 20473,
          "cache_creation_input_tokens": 1026,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1026
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

_source line 18 · 2026-05-29T06:39:05.288Z_

<details><summary>↩ Tool result · `toolu_01QsoauV8gpreXhbfACXvyaM`</summary>

```text
Web search results for query: "LogicReward ICLR 2026 Isabelle step verification token probability arXiv 2512.18196"

Links: [{"title":"LogicReward: Incentivizing LLM Reasoning via Step-Wise Logical Supervision [Quick Review]","url":"https://liner.com/review/logicreward-incentivizing-llm-reasoning-via-stepwise-logical-supervision"},{"title":"GitHub - Aiden0526/Logic-Reward: Codes and Data for ICLR 2026 paper \"LogicReward: Incentivizing LLM Reasoning via Step-Wise Logical Supervision\" · GitHub","url":"https://github.com/Aiden0526/Logic-Reward"},{"title":"LogicReward: Incentivizing LLM Reasoning via Step-Wise Logical Supervision","url":"https://arxiv.org/html/2512.18196"},{"title":"[2512.18196] LogicReward: Incentivizing LLM Reasoning via Step-Wise Logical Supervision","url":"https://arxiv.org/abs/2512.18196"},{"title":"Stepwise: Neuro-Symbolic Proof Search for Automated Systems Verification","url":"https://arxiv.org/pdf/2603.19715"},{"title":"Publiced as a conference paper at ICLR 2026 LOGICREWARD:","url":"https://openreview.net/pdf/de9ac22503a1fd3b541e09e4ff9021f87fc357c3.pdf"},{"title":"Efficient verification of imperative programs using auto2","url":"https://arxiv.org/pdf/1610.06996"},{"title":"Reconstructing veriT Proofs in Isabelle/HOL","url":"https://arxiv.org/pdf/1908.09480"}]

I found relevant information about the LogicReward paper. Here are the search results:

## LogicReward Paper Details

LogicReward is an ICLR 2026 paper that presents a novel system enforcing step-level logical correctness and reasoning faithfulness.

### Key Information

**Paper Title:** LogicReward: Incentivizing LLM Reasoning via Step-Wise Logical Supervision

**arXiv ID:** 2512.18196

**Authors:** Jundong Xu, Hao Fei, Huichi Zhou, Xin Quan, Qijun Huang, Shengqiong Wu, William Yang Wang, Mong-Li Lee, and Wynne Hsu

### Main Contribution

LogicReward is a novel reward system that guides model training by enforcing step-level logical correctness with a theorem prover. The approach introduces Autoformalization with Soft Unification, which reduces natural language ambiguity and improves formalization quality.

### Performance Results

An 8B model trained on data constructed with LogicReward surpasses GPT-4o and o4-mini by 11.6% and 2% on natural language inference and logical reasoning tasks.

The paper addresses the problem that although LLMs exhibit strong reasoning capabilities, existing training methods largely depend on outcome-based feedback which can produce correct answers with flawed reasoning, and prior work still lacks guarantees of logical soundness.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fb929d9b-ef76-456d-8085-999a7052443f",
  "isSidechain": false,
  "promptId": "02da38a2-c80a-4990-b6e8-13012729d6f2",
  "type": "user",
  "uuid": "3dc51da4-92df-4091-ac44-7b98ea73f336",
  "toolUseResult": {
    "query": "LogicReward ICLR 2026 Isabelle step verification token probability arXiv 2512.18196",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TXrAv2VKyhXAm3PPpDsuyR",
        "content": [
          {
            "title": "LogicReward: Incentivizing LLM Reasoning via Step-Wise Logical Supervision [Quick Review]",
            "url": "https://liner.com/review/logicreward-incentivizing-llm-reasoning-via-stepwise-logical-supervision"
          },
          {
            "title": "GitHub - Aiden0526/Logic-Reward: Codes and Data for ICLR 2026 paper \"LogicReward: Incentivizing LLM Reasoning via Step-Wise Logical Supervision\" · GitHub",
            "url": "https://github.com/Aiden0526/Logic-Reward"
          },
          {
            "title": "LogicReward: Incentivizing LLM Reasoning via Step-Wise Logical Supervision",
            "url": "https://arxiv.org/html/2512.18196"
          },
          {
            "title": "[2512.18196] LogicReward: Incentivizing LLM Reasoning via Step-Wise Logical Supervision",
            "url": "https://arxiv.org/abs/2512.18196"
          },
          {
            "title": "Stepwise: Neuro-Symbolic Proof Search for Automated Systems Verification",
            "url": "https://arxiv.org/pdf/2603.19715"
          },
          {
            "title": "Publiced as a conference paper at ICLR 2026 LOGICREWARD:",
            "url": "https://openreview.net/pdf/de9ac22503a1fd3b541e09e4ff9021f87fc357c3.pdf"
          },
          {
            "title": "Efficient verification of imperative programs using auto2",
            "url": "https://arxiv.org/pdf/1610.06996"
          },
          {
            "title": "Reconstructing veriT Proofs in Isabelle/HOL",
            "url": "https://arxiv.org/pdf/1908.09480"
          }
        ]
      },
      "I found relevant information about the LogicReward paper. Here are the search results:\n\n## LogicReward Paper Details\n\nLogicReward is an ICLR 2026 paper that presents a novel system enforcing step-level logical correctness and reasoning faithfulness.\n\n### Key Information\n\n**Paper Title:** LogicReward: Incentivizing LLM Reasoning via Step-Wise Logical Supervision\n\n**arXiv ID:** 2512.18196\n\n**Authors:** Jundong Xu, Hao Fei, Huichi Zhou, Xin Quan, Qijun Huang, Shengqiong Wu, William Yang Wang, Mong-Li Lee, and Wynne Hsu\n\n### Main Contribution\n\nLogicReward is a novel reward system that guides model training by enforcing step-level logical correctness with a theorem prover. The approach introduces Autoformalization with Soft Unification, which reduces natural language ambiguity and improves formalization quality.\n\n### Performance Results\n\nAn 8B model trained on data constructed with LogicReward surpasses GPT-4o and o4-mini by 11.6% and 2% on natural language inference and logical reasoning tasks.\n\nThe paper addresses the problem that although LLMs exhibit strong reasoning capabilities, existing training methods largely depend on outcome-based feedback which can produce correct answers with flawed reasoning, and prior work still lacks guarantees of logical soundness."
    ],
    "durationSeconds": 8.692237519000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "fb929d9b-ef76-456d-8085-999a7052443f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "644ee0d4-56af-4ee5-8097-233dab1a01f6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-29T06:39:08.569Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014ZerV9bEHMQ1vJcfDCmpP6`</summary>

```json
{
  "query": "GenPRM process reward model 2025 miracle step detection RRM rubric rewards arXiv 2510.07774"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3dc51da4-92df-4091-ac44-7b98ea73f336",
  "isSidechain": false,
  "requestId": "req_011CbWQCnT4RcVyDCDLuTe4k",
  "type": "assistant",
  "uuid": "42a8e2d9-4fdb-4f0d-876f-e70ffe2df4ff",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "644ee0d4-56af-4ee5-8097-233dab1a01f6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012EbiRjkSCDAKBNuM8f1XxZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 891,
      "cache_read_input_tokens": 21499,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 891,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 78,
          "cache_read_input_tokens": 21499,
          "cache_creation_input_tokens": 891,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 891
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

_source line 20 · 2026-05-29T06:39:17.306Z_

<details><summary>↩ Tool result · `toolu_014ZerV9bEHMQ1vJcfDCmpP6`</summary>

```text
Web search results for query: "GenPRM process reward model 2025 miracle step detection RRM rubric rewards arXiv 2510.07774"

Links: [{"title":"[2510.07774] Curing Miracle Steps in LLM Mathematical Reasoning with Rubric Rewards","url":"https://arxiv.org/abs/2510.07774"},{"title":"Curing Miracle Steps in LLM Mathematical Reasoning with ...","url":"https://arxiv.org/pdf/2510.07774"},{"title":"Curing “Miracle Steps” in LLM Mathematical Reasoning with Rubric Rewards","url":"https://arxiv.org/html/2510.07774"},{"title":"(PDF) Curing Miracle Steps in LLM Mathematical Reasoning with Rubric Rewards","url":"https://www.researchgate.net/publication/396372877_Curing_Miracle_Steps_in_LLM_Mathematical_Reasoning_with_Rubric_Rewards"},{"title":"[2504.00891] GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning","url":"https://arxiv.org/abs/2504.00891"},{"title":"A Survey of Process Reward Models: From Outcome Signals to Process","url":"https://arxiv.org/pdf/2510.08049"},{"title":"GM-PRM: A Generative Multimodal Process Reward Model for Multimodal Mathematical Reasoning","url":"https://arxiv.org/pdf/2508.04088"},{"title":"GitHub - RyanLiu112/GenPRM: [AAAI 2026] Official codebase for \"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning\".","url":"https://github.com/RyanLiu112/GenPRM"}]

Based on the search results, I found detailed information about the papers and concepts you're asking about:

## arXiv 2510.07774: "Curing Miracle Steps in LLM Mathematical Reasoning with Rubric Rewards"

The paper addresses "Miracle Steps" which are linked to answer-recall shortcuts, including memorization from pretraining, where the model accesses the correct answer independently of its reasoning chain.

**Rubric Reward Model (RRM):**
The RRM is a process-oriented reward function that evaluates the entire reasoning trajectory against problem-specific rubrics. The RRM explicitly penalizes logical flaws and encourages rigorous deduction.

**Key Results:**
When integrated into an RL pipeline, RRM-based training consistently outperforms outcome-only supervision across four math benchmarks, notably boosting Verified Pass@1024 on AIME2024 from 26.7% to 62.6% and reducing the incidence of Miracle Steps by 71%.

**Technical Features:**
Unlike the binary Verifier and saturation-prone PRM, RRM yields fine-grained, interpretable 0–10 scores that correlate strongly with false-positive rates, providing more informative gradients for training.

## GenPRM (arXiv 2504.00891): "Scaling Test-Time Compute of Process Reward Models via Generative Reasoning"

Through test-time scaling, a 1.5B GenPRM outperforms GPT-4o, and a 7B GenPRM surpasses Qwen2.5-Math-PRM-72B on ProcessBench. GenPRM significantly outperforms prior PRMs with only 23K training data from MATH dataset.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "42a8e2d9-4fdb-4f0d-876f-e70ffe2df4ff",
  "isSidechain": false,
  "promptId": "02da38a2-c80a-4990-b6e8-13012729d6f2",
  "type": "user",
  "uuid": "434c2bc8-d87e-49b7-a0a5-b09038ff0154",
  "toolUseResult": {
    "query": "GenPRM process reward model 2025 miracle step detection RRM rubric rewards arXiv 2510.07774",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MUSJvQt9BBAN57KA8ZiRES",
        "content": [
          {
            "title": "[2510.07774] Curing Miracle Steps in LLM Mathematical Reasoning with Rubric Rewards",
            "url": "https://arxiv.org/abs/2510.07774"
          },
          {
            "title": "Curing Miracle Steps in LLM Mathematical Reasoning with ...",
            "url": "https://arxiv.org/pdf/2510.07774"
          },
          {
            "title": "Curing “Miracle Steps” in LLM Mathematical Reasoning with Rubric Rewards",
            "url": "https://arxiv.org/html/2510.07774"
          },
          {
            "title": "(PDF) Curing Miracle Steps in LLM Mathematical Reasoning with Rubric Rewards",
            "url": "https://www.researchgate.net/publication/396372877_Curing_Miracle_Steps_in_LLM_Mathematical_Reasoning_with_Rubric_Rewards"
          },
          {
            "title": "[2504.00891] GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning",
            "url": "https://arxiv.org/abs/2504.00891"
          },
          {
            "title": "A Survey of Process Reward Models: From Outcome Signals to Process",
            "url": "https://arxiv.org/pdf/2510.08049"
          },
          {
            "title": "GM-PRM: A Generative Multimodal Process Reward Model for Multimodal Mathematical Reasoning",
            "url": "https://arxiv.org/pdf/2508.04088"
          },
          {
            "title": "GitHub - RyanLiu112/GenPRM: [AAAI 2026] Official codebase for \"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning\".",
            "url": "https://github.com/RyanLiu112/GenPRM"
          }
        ]
      },
      "Based on the search results, I found detailed information about the papers and concepts you're asking about:\n\n## arXiv 2510.07774: \"Curing Miracle Steps in LLM Mathematical Reasoning with Rubric Rewards\"\n\nThe paper addresses \"Miracle Steps\" which are linked to answer-recall shortcuts, including memorization from pretraining, where the model accesses the correct answer independently of its reasoning chain.\n\n**Rubric Reward Model (RRM):**\nThe RRM is a process-oriented reward function that evaluates the entire reasoning trajectory against problem-specific rubrics. The RRM explicitly penalizes logical flaws and encourages rigorous deduction.\n\n**Key Results:**\nWhen integrated into an RL pipeline, RRM-based training consistently outperforms outcome-only supervision across four math benchmarks, notably boosting Verified Pass@1024 on AIME2024 from 26.7% to 62.6% and reducing the incidence of Miracle Steps by 71%.\n\n**Technical Features:**\nUnlike the binary Verifier and saturation-prone PRM, RRM yields fine-grained, interpretable 0–10 scores that correlate strongly with false-positive rates, providing more informative gradients for training.\n\n## GenPRM (arXiv 2504.00891): \"Scaling Test-Time Compute of Process Reward Models via Generative Reasoning\"\n\nThrough test-time scaling, a 1.5B GenPRM outperforms GPT-4o, and a 7B GenPRM surpasses Qwen2.5-Math-PRM-72B on ProcessBench. GenPRM significantly outperforms prior PRMs with only 23K training data from MATH dataset."
    ],
    "durationSeconds": 8.727526829000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "42a8e2d9-4fdb-4f0d-876f-e70ffe2df4ff",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "644ee0d4-56af-4ee5-8097-233dab1a01f6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Formally-Routed Process Reward Models for Sound Miracle Step Detection  ## Core Problem  No existing PRM exploit…",
  "leafUuid": "434c2bc8-d87e-49b7-a0a5-b09038ff0154",
  "sessionId": "644ee0d4-56af-4ee5-8097-233dab1a01f6"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Learned routing for hybrid formal-neural process reward models",
  "sessionId": "644ee0d4-56af-4ee5-8097-233dab1a01f6"
}
```

---

### Tool call

_source line 23 · 2026-05-29T06:39:20.804Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TZiUtwaGdqbGqG5RpibXC9`</summary>

```json
{
  "query": "Risk-Controlled Lean-as-Judge autoformalization faithfulness coverage 2026 arXiv 2605.28365"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "434c2bc8-d87e-49b7-a0a5-b09038ff0154",
  "isSidechain": false,
  "requestId": "req_011CbWQDgSBc6oM2TcVaohPF",
  "type": "assistant",
  "uuid": "b8c827e2-4913-48bb-8ca1-dc8345319468",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "644ee0d4-56af-4ee5-8097-233dab1a01f6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UmcuR5WAHuTfmr2gutRL2b",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 947,
      "cache_read_input_tokens": 22390,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 947,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 80,
          "cache_read_input_tokens": 22390,
          "cache_creation_input_tokens": 947,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 947
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

_source line 24 · 2026-05-29T06:39:28.927Z_

<details><summary>↩ Tool result · `toolu_01TZiUtwaGdqbGqG5RpibXC9`</summary>

```text
Web search results for query: "Risk-Controlled Lean-as-Judge autoformalization faithfulness coverage 2026 arXiv 2605.28365"

Links: [{"title":"[2605.28365] Risk-Controlled Lean-as-Judge for Natural-Language Mathematical Reasoning","url":"https://arxiv.org/abs/2605.28365"},{"title":"Risk-Controlled Lean-as-Judge for Natural-Language Mathematical Reasoning","url":"https://arxiv.org/html/2605.28365"},{"title":"Autoformalizer with Tool Feedback","url":"https://arxiv.org/html/2510.06857v1"},{"title":"Autoformalizer with Tool Feedback","url":"https://arxiv.org/pdf/2510.06857"},{"title":"A New Approach Towards Autoformalization","url":"https://arxiv.org/pdf/2310.07957"},{"title":"An Evaluation Benchmark for Autoformalization in Lean4","url":"https://arxiv.org/pdf/2406.06555"},{"title":"Process-Driven Autoformalization in Lean 4","url":"https://arxiv.org/pdf/2406.01940"}]

I found the paper! Here's what I can tell you about arXiv:2605.28365:

## Paper Summary

The paper is titled "Risk-Controlled Lean-as-Judge for Natural-Language Mathematical Reasoning" by Pauline Bourigault, Xiaotong Ji, Matthieu Zimmer, Rasul Tutunov, and Haitham Bou Ammar.

## Key Findings on Faithfulness and Coverage

The research found that on MATH-500, the Lean proof signal is sharply coverage-dependent: the proof-winning answer is correct 96% of the time at high proved coverage but only 20% at low coverage. Additionally, a 7B autoformalizer proves a class for only 28% of problems, and a manual audit finds only approximately 43% of those proofs faithful.

## Proposed Solution

The authors propose COVCAL, a selector over Lean-trace diagnostics that certifies a finite-sample selective-risk bound on accepted answers or abstains, under two regimes (a conservative Bonferroni bound and a tighter dev-then-cal rule).

The paper was submitted on May 27, 2026, and addresses the fundamental challenge that while Lean is increasingly used to verify mathematical answers, many answers never formalize, and a failed proof may not indicate a wrong answer but rather an ill-typed statement or missing library fact.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b8c827e2-4913-48bb-8ca1-dc8345319468",
  "isSidechain": false,
  "promptId": "02da38a2-c80a-4990-b6e8-13012729d6f2",
  "type": "user",
  "uuid": "56ba9f72-d755-4223-8829-22704c5b4d3e",
  "toolUseResult": {
    "query": "Risk-Controlled Lean-as-Judge autoformalization faithfulness coverage 2026 arXiv 2605.28365",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DC1x7FYMwgEHkmAwWYobkV",
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
            "title": "Autoformalizer with Tool Feedback",
            "url": "https://arxiv.org/html/2510.06857v1"
          },
          {
            "title": "Autoformalizer with Tool Feedback",
            "url": "https://arxiv.org/pdf/2510.06857"
          },
          {
            "title": "A New Approach Towards Autoformalization",
            "url": "https://arxiv.org/pdf/2310.07957"
          },
          {
            "title": "An Evaluation Benchmark for Autoformalization in Lean4",
            "url": "https://arxiv.org/pdf/2406.06555"
          },
          {
            "title": "Process-Driven Autoformalization in Lean 4",
            "url": "https://arxiv.org/pdf/2406.01940"
          }
        ]
      },
      "I found the paper! Here's what I can tell you about arXiv:2605.28365:\n\n## Paper Summary\n\nThe paper is titled \"Risk-Controlled Lean-as-Judge for Natural-Language Mathematical Reasoning\" by Pauline Bourigault, Xiaotong Ji, Matthieu Zimmer, Rasul Tutunov, and Haitham Bou Ammar.\n\n## Key Findings on Faithfulness and Coverage\n\nThe research found that on MATH-500, the Lean proof signal is sharply coverage-dependent: the proof-winning answer is correct 96% of the time at high proved coverage but only 20% at low coverage. Additionally, a 7B autoformalizer proves a class for only 28% of problems, and a manual audit finds only approximately 43% of those proofs faithful.\n\n## Proposed Solution\n\nThe authors propose COVCAL, a selector over Lean-trace diagnostics that certifies a finite-sample selective-risk bound on accepted answers or abstains, under two regimes (a conservative Bonferroni bound and a tighter dev-then-cal rule).\n\nThe paper was submitted on May 27, 2026, and addresses the fundamental challenge that while Lean is increasingly used to verify mathematical answers, many answers never formalize, and a failed proof may not indicate a wrong answer but rather an ill-typed statement or missing library fact."
    ],
    "durationSeconds": 8.116689643999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "b8c827e2-4913-48bb-8ca1-dc8345319468",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "644ee0d4-56af-4ee5-8097-233dab1a01f6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-29T06:39:31.559Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VX146EvP8b5oBAqsw83h46`</summary>

```json
{
  "query": "ThinkPRM R-PRM ARES process reward model ProcessBench PRMBench 2025 2026 state of the art"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56ba9f72-d755-4223-8829-22704c5b4d3e",
  "isSidechain": false,
  "requestId": "req_011CbWQEXXvceDFCunzhXwbE",
  "type": "assistant",
  "uuid": "bc349bb0-d612-461a-86ee-8accc41fce91",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "644ee0d4-56af-4ee5-8097-233dab1a01f6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MxVR5zb54sMeWrGefzD2FY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 715,
      "cache_read_input_tokens": 23337,
      "output_tokens": 83,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 715,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 83,
          "cache_read_input_tokens": 23337,
          "cache_creation_input_tokens": 715,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 715
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

_source line 26 · 2026-05-29T06:39:40.862Z_

<details><summary>↩ Tool result · `toolu_01VX146EvP8b5oBAqsw83h46`</summary>

```text
Web search results for query: "ThinkPRM R-PRM ARES process reward model ProcessBench PRMBench 2025 2026 state of the art"

Links: [{"title":"[2504.16828] Process Reward Models That Think","url":"https://arxiv.org/abs/2504.16828"},{"title":"Paper page - Process Reward Models That Think","url":"https://huggingface.co/papers/2504.16828"},{"title":"ThinkPRM: A Generative Process Reward Models for Scalable Reasoning Verification - MarkTechPost","url":"https://www.marktechpost.com/2025/04/29/thinkprm-a-generative-process-reward-models-for-scalable-reasoning-verification/"},{"title":"Process Reward Models That Think","url":"https://arxiv.org/pdf/2504.16828"},{"title":"Process Reward Models That Think | OpenReview","url":"https://openreview.net/forum?id=V727xqBYIW"},{"title":"GitHub - mukhal/ThinkPRM: Process Reward Models That Think","url":"https://github.com/mukhal/thinkprm"},{"title":"PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models","url":"https://prmbench.github.io/"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=Process+Reward+Models+%28PRMs%29"},{"title":"GitHub - RyanLiu112/Awesome-Process-Reward-Models: A comprehensive collection of process reward models. · GitHub","url":"https://github.com/RyanLiu112/Awesome-Process-Reward-Models"},{"title":"Process Reward Models: Step-Level Feedback for LLMs","url":"https://www.emergentmind.com/topics/process-reward-models-prm"}]

Based on the search results, here's what I found about these process reward model approaches and benchmarks:

## ThinkPRM

ThinkPRM is a data-efficient PRM built as a verbalized step-wise reward model that verifies every step in the solution by generating a verification chain-of-thought (CoT). ThinkPRM is a long CoT verifier fine-tuned on orders of magnitude fewer process labels than those required by discriminative PRMs, and outperforms LLM-as-a-Judge and discriminative verifiers using only 1% of the process labels in PRM800K across several challenging benchmarks.

## R-PRM (Reasoning-Driven Process Reward Modeling)

R-PRM (Reasoning-Driven Process Reward Modeling) leverages stronger LLMs to generate seed data from limited annotations to bootstrap reasoning capabilities, enhances performance through preference optimization without requiring additional annotated data, and introduces inference-time scaling to harness the model's reasoning potential. On ProcessBench and PRMBench, R-PRM surpasses strong baselines by 11.9 and 8.5 points in F1 scores, respectively.

## ProcessBench and PRMBench

PRMBench comprises 6,216 carefully designed problems and 83,456 step-level labels, evaluating models across multiple dimensions including simplicity, soundness, and sensitivity. ThinkPRM beats baselines on ProcessBench, MATH-500, and AIME '24 under best-of-N selection and reward-guided search.

## Current State-of-the-Art

A new state-of-the-art PRM on ProcessBench (75.0%) and PRMBench (65.5%) compared with same sized models was achieved through active learning and filtering approaches. Recent generative, chain-of-thought PRMs like ThinkPRM and GenPRM provide long-form verification chains, representing a shift in the field toward more interpretable, generative approaches to process reward modeling.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bc349bb0-d612-461a-86ee-8accc41fce91",
  "isSidechain": false,
  "promptId": "02da38a2-c80a-4990-b6e8-13012729d6f2",
  "type": "user",
  "uuid": "d91ba8ae-31ea-46cf-bf35-c3b287047c34",
  "toolUseResult": {
    "query": "ThinkPRM R-PRM ARES process reward model ProcessBench PRMBench 2025 2026 state of the art",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RGQXDP5w6apxAREwKuC3qV",
        "content": [
          {
            "title": "[2504.16828] Process Reward Models That Think",
            "url": "https://arxiv.org/abs/2504.16828"
          },
          {
            "title": "Paper page - Process Reward Models That Think",
            "url": "https://huggingface.co/papers/2504.16828"
          },
          {
            "title": "ThinkPRM: A Generative Process Reward Models for Scalable Reasoning Verification - MarkTechPost",
            "url": "https://www.marktechpost.com/2025/04/29/thinkprm-a-generative-process-reward-models-for-scalable-reasoning-verification/"
          },
          {
            "title": "Process Reward Models That Think",
            "url": "https://arxiv.org/pdf/2504.16828"
          },
          {
            "title": "Process Reward Models That Think | OpenReview",
            "url": "https://openreview.net/forum?id=V727xqBYIW"
          },
          {
            "title": "GitHub - mukhal/ThinkPRM: Process Reward Models That Think",
            "url": "https://github.com/mukhal/thinkprm"
          },
          {
            "title": "PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models",
            "url": "https://prmbench.github.io/"
          },
          {
            "title": "Daily Papers - Hugging Face",
            "url": "https://huggingface.co/papers?q=Process+Reward+Models+%28PRMs%29"
          },
          {
            "title": "GitHub - RyanLiu112/Awesome-Process-Reward-Models: A comprehensive collection of process reward models. · GitHub",
            "url": "https://github.com/RyanLiu112/Awesome-Process-Reward-Models"
          },
          {
            "title": "Process Reward Models: Step-Level Feedback for LLMs",
            "url": "https://www.emergentmind.com/topics/process-reward-models-prm"
          }
        ]
      },
      "Based on the search results, here's what I found about these process reward model approaches and benchmarks:\n\n## ThinkPRM\n\nThinkPRM is a data-efficient PRM built as a verbalized step-wise reward model that verifies every step in the solution by generating a verification chain-of-thought (CoT). ThinkPRM is a long CoT verifier fine-tuned on orders of magnitude fewer process labels than those required by discriminative PRMs, and outperforms LLM-as-a-Judge and discriminative verifiers using only 1% of the process labels in PRM800K across several challenging benchmarks.\n\n## R-PRM (Reasoning-Driven Process Reward Modeling)\n\nR-PRM (Reasoning-Driven Process Reward Modeling) leverages stronger LLMs to generate seed data from limited annotations to bootstrap reasoning capabilities, enhances performance through preference optimization without requiring additional annotated data, and introduces inference-time scaling to harness the model's reasoning potential. On ProcessBench and PRMBench, R-PRM surpasses strong baselines by 11.9 and 8.5 points in F1 scores, respectively.\n\n## ProcessBench and PRMBench\n\nPRMBench comprises 6,216 carefully designed problems and 83,456 step-level labels, evaluating models across multiple dimensions including simplicity, soundness, and sensitivity. ThinkPRM beats baselines on ProcessBench, MATH-500, and AIME '24 under best-of-N selection and reward-guided search.\n\n## Current State-of-the-Art\n\nA new state-of-the-art PRM on ProcessBench (75.0%) and PRMBench (65.5%) compared with same sized models was achieved through active learning and filtering approaches. Recent generative, chain-of-thought PRMs like ThinkPRM and GenPRM provide long-form verification chains, representing a shift in the field toward more interpretable, generative approaches to process reward modeling."
    ],
    "durationSeconds": 9.296627112000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "bc349bb0-d612-461a-86ee-8accc41fce91",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "644ee0d4-56af-4ee5-8097-233dab1a01f6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-29T06:39:44.537Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VmciWApzBt69AxW2ZAY7SN`</summary>

```json
{
  "query": "autoformalization roundtrip verification faithfulness arXiv 2604.25031 \"Do LLMs Game Formalization\" 2604.19459"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d91ba8ae-31ea-46cf-bf35-c3b287047c34",
  "isSidechain": false,
  "requestId": "req_011CbWQFQbz8HXzyCgx9RTTr",
  "type": "assistant",
  "uuid": "e3342d75-69e7-4085-8c34-cef5dc923108",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "644ee0d4-56af-4ee5-8097-233dab1a01f6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KX1T5BnpkxUU8rGxFFgtkE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1032,
      "cache_read_input_tokens": 24052,
      "output_tokens": 86,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1032,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 86,
          "cache_read_input_tokens": 24052,
          "cache_creation_input_tokens": 1032,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1032
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

_source line 28 · 2026-05-29T06:39:52.421Z_

<details><summary>↩ Tool result · `toolu_01VmciWApzBt69AxW2ZAY7SN`</summary>

```text
Web search results for query: "autoformalization roundtrip verification faithfulness arXiv 2604.25031 "Do LLMs Game Formalization" 2604.19459"

Links: [{"title":"[2604.25031] Faithful Autoformalization via Roundtrip Verification and Repair","url":"https://arxiv.org/abs/2604.25031"},{"title":"Faithful Autoformalization via Roundtrip Verification and Repair","url":"https://arxiv.org/html/2604.25031"},{"title":"[2604.19459] Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning","url":"https://arxiv.org/abs/2604.19459"},{"title":"Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning","url":"https://arxiv.org/html/2604.19459"},{"title":"Formal Reasoning Meets LLMs: Toward AI for Mathematics and Verification – Communications of the ACM","url":"https://cacm.acm.org/research/formal-reasoning-meets-llms-toward-ai-for-mathematics-and-verification/"},{"title":"MerLean: An Agentic Framework For Autoformalization in Quantum Computation","url":"https://arxiv.org/html/2602.16554v1"}]

I found both papers you're interested in. Here's what they cover:

**Paper 2604.25031: "Faithful Autoformalization via Roundtrip Verification and Repair"**

This paper proposes a roundtrip verification approach that doesn't require ground-truth annotations: formalize a statement, translate the result back to natural language, re-formalize, and use a formal tool to check logical equivalence. When the two formalizations agree, this provides evidence of a faithful formalization. When they disagree, a diagnosis step identifies which translation stage failed, and a targeted repair operator attempts to correct that stage. The authors evaluate their approach on 150 traffic rules using Claude Opus 4.6 and GPT-5.2, finding that diagnosis-guided repair raises formal equivalence from 45–61% to 83–85% for both models.

**Paper 2604.19459: "Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning"**

This paper addresses how formal verification guarantees proof validity but not formalization faithfulness. The authors investigate whether frontier models exploit this gap when generating Lean 4 proofs, a behavior they term formalization gaming. They evaluate GPT-5 and DeepSeek-R1 on 303 first-order logic problems. The two-stage pipeline reveals two distinct modes of unfaithfulness: GPT-5 fabricates axioms during proof generation, while DeepSeek-R1 mistranslates premises during formalization.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e3342d75-69e7-4085-8c34-cef5dc923108",
  "isSidechain": false,
  "promptId": "02da38a2-c80a-4990-b6e8-13012729d6f2",
  "type": "user",
  "uuid": "9e897c91-2464-4be7-93c5-2408465ea0cf",
  "toolUseResult": {
    "query": "autoformalization roundtrip verification faithfulness arXiv 2604.25031 \"Do LLMs Game Formalization\" 2604.19459",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MGTeqzzbRtyJEBG3tj6xo1",
        "content": [
          {
            "title": "[2604.25031] Faithful Autoformalization via Roundtrip Verification and Repair",
            "url": "https://arxiv.org/abs/2604.25031"
          },
          {
            "title": "Faithful Autoformalization via Roundtrip Verification and Repair",
            "url": "https://arxiv.org/html/2604.25031"
          },
          {
            "title": "[2604.19459] Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning",
            "url": "https://arxiv.org/abs/2604.19459"
          },
          {
            "title": "Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning",
            "url": "https://arxiv.org/html/2604.19459"
          },
          {
            "title": "Formal Reasoning Meets LLMs: Toward AI for Mathematics and Verification – Communications of the ACM",
            "url": "https://cacm.acm.org/research/formal-reasoning-meets-llms-toward-ai-for-mathematics-and-verification/"
          },
          {
            "title": "MerLean: An Agentic Framework For Autoformalization in Quantum Computation",
            "url": "https://arxiv.org/html/2602.16554v1"
          }
        ]
      },
      "I found both papers you're interested in. Here's what they cover:\n\n**Paper 2604.25031: \"Faithful Autoformalization via Roundtrip Verification and Repair\"**\n\nThis paper proposes a roundtrip verification approach that doesn't require ground-truth annotations: formalize a statement, translate the result back to natural language, re-formalize, and use a formal tool to check logical equivalence. When the two formalizations agree, this provides evidence of a faithful formalization. When they disagree, a diagnosis step identifies which translation stage failed, and a targeted repair operator attempts to correct that stage. The authors evaluate their approach on 150 traffic rules using Claude Opus 4.6 and GPT-5.2, finding that diagnosis-guided repair raises formal equivalence from 45–61% to 83–85% for both models.\n\n**Paper 2604.19459: \"Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning\"**\n\nThis paper addresses how formal verification guarantees proof validity but not formalization faithfulness. The authors investigate whether frontier models exploit this gap when generating Lean 4 proofs, a behavior they term formalization gaming. They evaluate GPT-5 and DeepSeek-R1 on 303 first-order logic problems. The two-stage pipeline reveals two distinct modes of unfaithfulness: GPT-5 fabricates axioms during proof generation, while DeepSeek-R1 mistranslates premises during formalization."
    ],
    "durationSeconds": 7.877846997999994,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e3342d75-69e7-4085-8c34-cef5dc923108",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "644ee0d4-56af-4ee5-8097-233dab1a01f6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-29T06:39:52.432Z_

```json
{
  "parentUuid": "9e897c91-2464-4be7-93c5-2408465ea0cf",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "99d879c2-35e4-496e-8db3-ce28ee05ba9d",
  "timestamp": "2026-05-29T06:39:52.432Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "644ee0d4-56af-4ee5-8097-233dab1a01f6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 30 · 2026-05-29T06:39:56.187Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YaRkvbC2crurcddqYW2TV7`</summary>

```json
{
  "query": "learned formalizability routing classifier reasoning steps neural formal verification 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "99d879c2-35e4-496e-8db3-ce28ee05ba9d",
  "isSidechain": false,
  "requestId": "req_011CbWQGG3aEVPJxbqidBHjA",
  "type": "assistant",
  "uuid": "4221e3dd-49f3-458a-9daf-2976bda2857e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "644ee0d4-56af-4ee5-8097-233dab1a01f6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LN6XiVKhEdD7ZDcTVLegfj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 884,
      "cache_read_input_tokens": 25084,
      "output_tokens": 68,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 884,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 68,
          "cache_read_input_tokens": 25084,
          "cache_creation_input_tokens": 884,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 884
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

_source line 31 · 2026-05-29T06:40:03.499Z_

<details><summary>↩ Tool result · `toolu_01YaRkvbC2crurcddqYW2TV7`</summary>

```text
Web search results for query: "learned formalizability routing classifier reasoning steps neural formal verification 2025 2026"

Links: [{"title":"Learning to Generate Formally Verifiable Step-by-Step Logic Reasoning via Structured Formal Intermediaries","url":"https://arxiv.org/pdf/2603.29500"},{"title":"Generating and Structuring Proofs for Formal Verification","url":"https://arxiv.org/pdf/2504.17017"},{"title":"Pushing the Boundaries of Natural Reasoning: Interleaved Bonus from Formal-Logic Verification","url":"https://arxiv.org/pdf/2601.22642"},{"title":"Neural Theorem Proving: Generating and Structuring Proofs for Formal Verification","url":"https://arxiv.org/html/2504.17017v1"},{"title":"Incremental Certificate Learning for Hybrid Neural Network Verification . A Solver Architecture for Piecewise-Linear Safety Queries","url":"https://arxiv.org/pdf/2512.24379"},{"title":"Efficient PRM Training Data Synthesis via Formal Verification","url":"https://arxiv.org/pdf/2505.15960"}]

Based on the web search results, here are the key findings related to your query about learned formalizability routing, classifier reasoning steps, and neural formal verification:

## Recent Research (2025-2026)

PRoSFI (Process Reward over Structured Formal Intermediates) is a novel reward method that generates structured intermediate steps aligned with natural language reasoning, which are then verified by a formal prover, with only fully validated reasoning chains receiving high rewards to guide models toward generating step-by-step machine-checkable proofs.

A two-stage training pipeline synergizes formal logic verification-guided supervised fine-tuning and policy optimization, with 7B and 14B models outperforming state-of-the-art baselines by average margins of 10.4% and 14.2%, respectively.

## Process Reward Models (PRMs)

PRMs are created by fine-tuning LLMs to classify the correctness of individual reasoning steps, using training datasets annotated with step-level error labels on LLM-generated reasoning traces. FoVER-40K is a formal logic and theorem proving task dataset, and FoVER-PRMs outperform baseline PRMs based on LLMs without additional fine-tuning when evaluated on benchmarks like LogicNLI, AQuA-RAT, and AIME.

## General Theorem Proving

Two main paradigms towards automated theorem proving have emerged: one that generates the whole proof and the other that generates only the next proof step.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4221e3dd-49f3-458a-9daf-2976bda2857e",
  "isSidechain": false,
  "promptId": "02da38a2-c80a-4990-b6e8-13012729d6f2",
  "type": "user",
  "uuid": "ccc5735b-15c6-47e6-99c5-a2074f5bccee",
  "toolUseResult": {
    "query": "learned formalizability routing classifier reasoning steps neural formal verification 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_019vmmb9fKXjMVSQDXDLykEY",
        "content": [
          {
            "title": "Learning to Generate Formally Verifiable Step-by-Step Logic Reasoning via Structured Formal Intermediaries",
            "url": "https://arxiv.org/pdf/2603.29500"
          },
          {
            "title": "Generating and Structuring Proofs for Formal Verification",
            "url": "https://arxiv.org/pdf/2504.17017"
          },
          {
            "title": "Pushing the Boundaries of Natural Reasoning: Interleaved Bonus from Formal-Logic Verification",
            "url": "https://arxiv.org/pdf/2601.22642"
          },
          {
            "title": "Neural Theorem Proving: Generating and Structuring Proofs for Formal Verification",
            "url": "https://arxiv.org/html/2504.17017v1"
          },
          {
            "title": "Incremental Certificate Learning for Hybrid Neural Network Verification . A Solver Architecture for Piecewise-Linear Safety Queries",
            "url": "https://arxiv.org/pdf/2512.24379"
          },
          {
            "title": "Efficient PRM Training Data Synthesis via Formal Verification",
            "url": "https://arxiv.org/pdf/2505.15960"
          }
        ]
      },
      "Based on the web search results, here are the key findings related to your query about learned formalizability routing, classifier reasoning steps, and neural formal verification:\n\n## Recent Research (2025-2026)\n\nPRoSFI (Process Reward over Structured Formal Intermediates) is a novel reward method that generates structured intermediate steps aligned with natural language reasoning, which are then verified by a formal prover, with only fully validated reasoning chains receiving high rewards to guide models toward generating step-by-step machine-checkable proofs.\n\nA two-stage training pipeline synergizes formal logic verification-guided supervised fine-tuning and policy optimization, with 7B and 14B models outperforming state-of-the-art baselines by average margins of 10.4% and 14.2%, respectively.\n\n## Process Reward Models (PRMs)\n\nPRMs are created by fine-tuning LLMs to classify the correctness of individual reasoning steps, using training datasets annotated with step-level error labels on LLM-generated reasoning traces. FoVER-40K is a formal logic and theorem proving task dataset, and FoVER-PRMs outperform baseline PRMs based on LLMs without additional fine-tuning when evaluated on benchmarks like LogicNLI, AQuA-RAT, and AIME.\n\n## General Theorem Proving\n\nTwo main paradigms towards automated theorem proving have emerged: one that generates the whole proof and the other that generates only the next proof step."
    ],
    "durationSeconds": 7.3063987060000075,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "4221e3dd-49f3-458a-9daf-2976bda2857e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "644ee0d4-56af-4ee5-8097-233dab1a01f6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-29T06:40:06.483Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01C7skyRF8ShSnfWPsj59BX2`</summary>

```json
{
  "query": "FIRMA bidirectional formal informal mathematical language alignment complexity router MathNLP 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ccc5735b-15c6-47e6-99c5-a2074f5bccee",
  "isSidechain": false,
  "requestId": "req_011CbWQH5Jgrkg6gtzyFqUa3",
  "type": "assistant",
  "uuid": "bd9e23a6-c445-42a6-b9a0-ec86158f3e26",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "644ee0d4-56af-4ee5-8097-233dab1a01f6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TZ8Nd8EvWK2iEQfmxE4gkZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 713,
      "cache_read_input_tokens": 25968,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 713,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 25968,
          "cache_creation_input_tokens": 713,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 713
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

_source line 33 · 2026-05-29T06:40:15.171Z_

<details><summary>↩ Tool result · `toolu_01C7skyRF8ShSnfWPsj59BX2`</summary>

```text
Web search results for query: "FIRMA bidirectional formal informal mathematical language alignment complexity router MathNLP 2025"

Links: [{"title":"FIRMA: Bidirectional Formal-Informal Mathematical Language Alignment with Proof-Theoretic Grounding - ACL Anthology","url":"https://aclanthology.org/2025.mathnlp-main.5/"},{"title":"Proceedings of The 3rd Workshop on Mathematical Natural Language Processing (MathNLP 2025) - ACL Anthology","url":"https://aclanthology.org/volumes/2025.mathnlp-main/"},{"title":"Workshop on Mathematical Natural Language Processing (2025) - ACL Anthology","url":"https://aclanthology.org/events/mathnlp-2025/"},{"title":"MathNLP 2025 MathNLP 2025: The 3rd Workshop on Mathematical Natural","url":"https://aclanthology.org/2025.mathnlp-main.pdf"},{"title":"FIRMA: Bidirectional Formal-Informal Mathematical ...","url":"https://aclanthology.org/2025.mathnlp-main.5.pdf"},{"title":"GitHub - smfatima3/FIRMA: The official codebase of the paper \"FIRMA: Bidirectional Formal-Informal Mathematical Language Alignment with Proof-Theoretic Grounding\"","url":"https://github.com/smfatima3/FIRMA"},{"title":"Alignment Methods for Formal Logical Reasoning","url":"https://aclanthology.org/2025.mathnlp-main.8.pdf"}]

Based on the search results, here's what I found about FIRMA:

## Overview

FIRMA (Formal-Informal Reasoning in Mathematical Alignment) is a bidirectional translation system between formal and informal mathematical language that leverages proof-theoretic interpretability hierarchies and specialized architectural components for proof preservation.

## Problem It Addresses

While large language models excel at generating plausible mathematical text, they often produce subtly incorrect formal translations that violate proof-theoretic constraints.

## Architecture

Unlike existing approaches that treat this as pure sequence-to-sequence translation, FIRMA introduces a hierarchical architecture with complexity-aware routing, proof-preserving attention mechanisms, and multi-objective training that balances formal correctness with natural readability. More specifically, the model processes formal or informal mathematical statements through a hierarchical encoder (symbol, syntax, and semantic layers), followed by a complexity router and proof-preserving attention.

## Performance Results

Through progressive complexity training on curated datasets from Lean 4 and formal mathematics repositories, FIRMA was evaluated on 200 translation samples across complexity levels and compared against two baseline systems. The analysis shows statistically significant improvements of 277.8% over BFS-Prover-V1-7B and 6307.5% over REAL-Prover on overall translation quality metrics. Additionally, ablation studies on 50 samples demonstrate that each architectural component contributes substantially to performance, with removal of any component resulting in 83-85% performance degradation.

## Publication

FIRMA was presented at The 3rd Workshop on Mathematical Natural Language Processing (MathNLP 2025) in Suzhou, China.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd9e23a6-c445-42a6-b9a0-ec86158f3e26",
  "isSidechain": false,
  "promptId": "02da38a2-c80a-4990-b6e8-13012729d6f2",
  "type": "user",
  "uuid": "45504cd1-1456-4827-8338-02f499301507",
  "toolUseResult": {
    "query": "FIRMA bidirectional formal informal mathematical language alignment complexity router MathNLP 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GXuTcNCqm32W6udVs7Pwdn",
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
      "Based on the search results, here's what I found about FIRMA:\n\n## Overview\n\nFIRMA (Formal-Informal Reasoning in Mathematical Alignment) is a bidirectional translation system between formal and informal mathematical language that leverages proof-theoretic interpretability hierarchies and specialized architectural components for proof preservation.\n\n## Problem It Addresses\n\nWhile large language models excel at generating plausible mathematical text, they often produce subtly incorrect formal translations that violate proof-theoretic constraints.\n\n## Architecture\n\nUnlike existing approaches that treat this as pure sequence-to-sequence translation, FIRMA introduces a hierarchical architecture with complexity-aware routing, proof-preserving attention mechanisms, and multi-objective training that balances formal correctness with natural readability. More specifically, the model processes formal or informal mathematical statements through a hierarchical encoder (symbol, syntax, and semantic layers), followed by a complexity router and proof-preserving attention.\n\n## Performance Results\n\nThrough progressive complexity training on curated datasets from Lean 4 and formal mathematics repositories, FIRMA was evaluated on 200 translation samples across complexity levels and compared against two baseline systems. The analysis shows statistically significant improvements of 277.8% over BFS-Prover-V1-7B and 6307.5% over REAL-Prover on overall translation quality metrics. Additionally, ablation studies on 50 samples demonstrate that each architectural component contributes substantially to performance, with removal of any component resulting in 83-85% performance degradation.\n\n## Publication\n\nFIRMA was presented at The 3rd Workshop on Mathematical Natural Language Processing (MathNLP 2025) in Suzhou, China."
    ],
    "durationSeconds": 8.682574179000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "bd9e23a6-c445-42a6-b9a0-ec86158f3e26",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "644ee0d4-56af-4ee5-8097-233dab1a01f6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 34_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Formally-Routed Process Reward Models for Sound Miracle Step Detection  ## Core Problem  No existing PRM exploit…",
  "leafUuid": "45504cd1-1456-4827-8338-02f499301507",
  "sessionId": "644ee0d4-56af-4ee5-8097-233dab1a01f6"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Learned routing for hybrid formal-neural process reward models",
  "sessionId": "644ee0d4-56af-4ee5-8097-233dab1a01f6"
}
```

---

### Assistant

_source line 36 · 2026-05-29T06:41:00.169Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have gathered comprehensive research on the related works. Let me synthesize all findings and provide a thorough evaluation of this proposal.

Let me analyze this proposal carefully:

## Summary of Key Research Landscape Findings

1. **FoVer** (ACL 2026): Uses Z3/Isabelle to synthesize PRM training labels. Achieves 85.8 AUROC on ProcessBench. Known overly-strict behavior on informal steps.

2. **VERGE** (arXiv 2026): Rule-based routing between Z3 and LLM ensemble. 18.7% uplift. Static routing by claim type (logical vs. 

3. **LogicReward** (ICLR 2026): Isabelle step verification with token-probability fallback. 8B model surpasses GPT-4o by 11.6% on logical reasoning. RL training framework.

4. **GenPRM** (AAAI 2026): Generative PRM, 7B surpasses 72B discriminative PRM on ProcessBench. Open weights.

5. **ThinkPRM**: Generative verification CoT, data-efficient, outperforms LLM-as-Judge.

6. **R-PRM** (EMN): Continuing through the remaining approaches in this research landscape. The proposal addresses a genuine gap between formal-only and neural-only approaches by introducing learned context-dependent routing, and the three-layer pipeline with formalizability assessment, faithfulness verification, and dual verification paths is well-architected. What's compelling is the intellectual honesty about autoformalization's real limitations—acknowledging 43% faithfulness and offering conditional soundness rather than false guarantees—which aligns with the Risk-Controlled framework. The experimental design looks thorough with detailed baselines and ablation studies planned.

However, the core novelty feels somewhat incremental: the main contribution boils down to training a binary classifier on FoVer labels to decide between formal and neural verification, which is a straightforward application of supervised learning. The real bottleneck appears to be the autoformalization step itself, which relies on Qwen2.5-Math-72B and its inherent limitations.

The autoformalization tool's 43% faithfulness and 28% coverage means the formal branch likely covers only a small fraction of steps—potentially 10-15% of all steps when accounting for routing accuracy and verification success. This raises questions about whether the formal soundness guarantee is practically meaningful at scale. Additionally, the router's training labels are tied to the specific autoformalization tool used, so if a better tool emerges, those labels become outdated and the router would need retraining.

The "conditional sound miracle step detection" claim also seems overstated since it requires steps to be routed correctly, pass roundtrip verification, and be faithfully formalized—a chain of conditions that compounds the limitations of each component.

A critical concern is whether the learned router actually outperforms a simpler try-and-fallback baseline that just attempts formalization first and falls back to neural methods. If preliminary results show comparable performance, the core contribution dissolves. The proposal also lacks experimental results entirely, so the risk hinges entirely on execution. Finally, even if the technical approach works, reviewers may not find "formal guarantees for 10-20% of steps" compelling enough to constitute a meaningful contribution, depending on their view of what practical impact requires. The core question is whether learned routing actually outperforms simpler fallback strategies enough to justify the added complexity. For AAAI 2026, I'm settling on around 35% — the problem and experimental rigor are strong, but the methodological novelty is moderate and the practical gains from conditional soundness remain uncertain.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45504cd1-1456-4827-8338-02f499301507",
  "isSidechain": false,
  "requestId": "req_011CbWQHwE3AiDFyqMQZfknR",
  "type": "assistant",
  "uuid": "77fb17d8-f180-4c65-85d4-8d0e1884915b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "644ee0d4-56af-4ee5-8097-233dab1a01f6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LgfQxEvMvGTGGfYqoERnFP",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 849,
      "cache_read_input_tokens": 26681,
      "output_tokens": 7196,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 849,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7196,
          "cache_read_input_tokens": 26681,
          "cache_creation_input_tokens": 849,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 849
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

_source line 37 · 2026-05-29T06:42:46.631Z_

Now I have sufficient research to provide a thorough evaluation. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:
- [FoVer: Efficient PRM Training Data Synthesis via Formal Verification](https://arxiv.org/abs/2505.15960) (ACL 2026): 直接前序工作。使用 Z3/Isabelle 合成 PRM 训练标签，ProcessBench 上 85.8 AUROC。文档化了在非形式化推理步骤上的"过于严格"行为——这正是本 proposal 试图解决的问题。提供公开代码和数据集。
- [VERGE: Formal Refinement and Guidance Engine](https://arxiv.org/abs/2601.20055) (arXiv 2026): 最直接竞争者。规则化语义路由（逻辑 vs. 常识 claim type）到 Z3 或 LLM ensemble，18.7% 性能提升。路由是静态的、基于 claim type 的、非学习的。论文明确指出 learned routing 是开放的下一步——本 proposal 正是回应这一 gap。
- [LogicReward](https://arxiv.org/abs/2512.18196) (ICLR 2026): Isabelle step verification + token-probability fallback。8B 模型超越 GPT-4o 11.6%。但其"先尝试形式化、失败则回退"策略无法区分"步骤本质上不可形式化"与"自动形式化在可形式化步骤上失败"——正是 proposal 所批评的缺陷。
- [GenPRM](https://arxiv.org/abs/2504.00891) (AAAI 2026): 生成式 PRM，7B 超越 Qwen2.5-Math-PRM-72B。开源权重。本 proposal 将其用作 neural branch 的 backbone。
- [ThinkPRM](https://arxiv.org/abs/2504.16828) (arXiv 2025): 14B 模型仅用 8K 过程标签即超越 100× 数据训练的判别式 PRM。建立了 token-budget-normalized 比较范式——proposal 引用此范式做 compute fairness 分析。
- [R-PRM](https://arxiv.org/abs/2503.21295) (EMNLP 2025): ProcessBench +13.9 F1，PRMBench +8.5 F1，三阶段训练。本 proposal 将其列为 baseline。
- [RRM: Curing Miracle Steps](https://arxiv.org/abs/2510.07774) (arXiv 2025, withdrawn from ICLR 2026): 定义 miracle step 分类法，通过 rubric rewards 减少 71% miracle steps。未测试形式化可推导性——proposal 的 miracle detection 贡献直接建立在此基础之上。
- [Risk-Controlled Lean-as-Judge](https://arxiv.org/abs/2605.28365) (arXiv 2026): 7B autoformalizer 仅 43% faithfulness、28% coverage。该论文提供了量化 autoformalization 局限的校准数据和 honest coverage reporting 方法论——proposal 的"条件性形式化保证"直接受此启发。
- [Faithful Autoformalization via Roundtrip Verification](https://arxiv.org/abs/2604.25031) (arXiv 2026): Roundtrip verification 将 formal equivalence 从 45-61% 提升到 83-85%。本 proposal 的 Layer 2 直接采用此方法。
- [Do LLMs Game Formalization?](https://arxiv.org/abs/2604.19459) (arXiv 2026): 识别出 axiom fabrication 和 premise mistranslation 两种 unfaithfulness 模式。为 proposal 的 roundtrip verification 层提供了理论动机。
- [FIRMA](https://aclanthology.org/2025.mathnlp-main.5/) (MathNLP 2025): 复杂度感知路由做 formal-informal 翻译。Proposal 正确指出其目标函数（翻译质量）与 formalizability routing for verification 根本不同。
- [PRoSFI](https://arxiv.org/abs/2603.29500) (arXiv 2026): 结构化形式中间体用于 prover verification，偏向 generation side。

- **调研总结**: PRM 领域正处于从纯判别式向生成式/混合式快速演进的阶段。形式化验证（FoVer, VERGE, LogicReward）已被证明有效但受限于覆盖率和过度严格问题。"学习化路由"是 VERGE 明确指出的开放问题，目前确实没有工作实现了 learned context-dependent formalizability routing。但 autoformalization 的低可靠性（43% faithfulness）构成了系统性瓶颈。Proposal 在这一 landscape 中定位清晰，但其条件性保证的实际覆盖范围可能受限。

【整体印象】:
如果我是审稿人，第一反应是：这是一篇 **定位精准、技术叙事清晰、实验设计异常完备** 的 proposal。作者对领域的掌握非常深入，VERGE 的 static routing → learned routing 的 gap 真实存在且被原论文明确指出。三层 pipeline（routing → roundtrip verification → formal/neural dispatch）逻辑自洽，honest coverage reporting 的设计哲学也令人欣赏。

然而，我的倾向会是 **borderline（偏向 weak accept / borderline reject）**。原因如下：
1. 核心贡献——learned formalizability routing——在技术上是一个相对直接的二分类器（Qwen3-8B LoRA fine-tuned on FoVer labels），novelty 天花板有限。
2. 受制于 autoformalization 的低可靠性（43% faithfulness, 28% coverage），formal branch 的"effective soundness coverage"可能仅覆盖 10-20% 的步骤，条件性保证的实际影响力存疑。
3. 如果 ablation 6（try-formal-first + neural fallback）表现接近 learned router，整个贡献基础将被削弱。

【核心贡献】:
1. **Conditional sound miracle detection**: 在 router 判定为 formalizable 且 roundtrip verification 通过的步骤子集上，Z3 predecessor-derivability 检查提供有保证的 miracle step 检测。这是第一个对推理步骤子集提供形式化正确性保证的 PRM。
2. **Learned context-dependent formalizability routing**: 不同于 VERGE 的静态 claim type routing 和 LogicReward 的 try-and-fallback，使用 Qwen3-8B 预测依赖前驱链上下文的 formalizability。
3. **Asymmetric cost-aware routing threshold**: 显式建模路由错误的不对称代价。

**贡献价值评估**: 贡献 1 在理论上有吸引力，但受 autoformalization 瓶颈限制，实际覆盖范围可能很窄。贡献 2 是核心 novelty，但二分类器的技术复杂度有限。贡献 3 更像是工程设计选择而非独立贡献。整体来看，这是一个 **方向正确、gap 清晰、但 novelty 量级中等** 的贡献。

【方法合理性】:
方法整体合理，三层 pipeline 的 cascading 设计逻辑自洽。但需关注以下问题：

1. **更简单的替代方案**: Ablation 6（try-formal-first + neural fallback，即 LogicReward 的策略）是一个非常自然的 trivial baseline。如果 Z3 编译失败即回退到 neural，无需训练 router，只需付出额外的 Z3 尝试开销（millisecond-scale）。Proposal 虽然将其列为 ablation，但未提供任何初步证据表明 learned routing 显著优于此简单策略。这是最大的方法论风险——如果 learned routing 的优势不显著，论文的核心贡献将大打折扣。

2. **Router 训练数据的 circularity**: Router 在 FoVer Z3 verification labels 上训练，但这些 labels 编码的是当前 autoformalization 工具的能力边界，而非步骤的内在 formalizability。换工具后 labels 需要重新生成，router 需要重新训练。这削弱了"学习 formalizability"的叙事。

3. **Roundtrip verification 的额外开销**: Layer 2 需要 72B 模型做 autoformalization + back-translation + semantic equivalence check，计算代价不低。在 effective coverage 可能只有 10-20% 的情况下，cost-effectiveness 值得质疑。

4. **神经分支缺乏创新**: Neural branch 直接使用 GenPRM-7B + Platt scaling，没有任何修改。这意味着对于大部分（~80-90%）步骤，系统退化为标准 GenPRM。

【5 维度打分】:

  1. **研究问题: 强** — 
     形式化-only PRM 过于严格 vs. 神经-only PRM 无形式化保证的 gap 在 FoVer、VERGE、LogicReward 的文献中都有明确记载。"Learned formalizability routing" 是 VERGE 论文明确指出的 open next step。Miracle step 的形式化检测连接了 RRM 的分类法和 FoVer 的验证能力，是一个有理论价值的组合。研究问题定义清晰，有充分的文献支撑。

  2. **方法与创新: 中** — 
     三层 pipeline 设计合理，但核心 novelty（learned routing classifier）在技术上是标准的 LoRA fine-tuning + binary classification。与 VERGE 相比，从 rule-based → learned 的跨越是真实的，但并非意料之外。与 FIRMA 的 complexity router 相比（虽然目标不同），learned routing 的概念并非全新。条件性形式化保证是好的理论贡献，但 honest coverage reporting 的方法论直接借自 Risk-Controlled Lean-as-Judge，原创成分有限。没有提出新的 autoformalization 方法或新的形式验证技术，主要贡献在于组合和系统设计。Asymmetric threshold 是标准的 cost-sensitive classification，不构成独立贡献。

  3. **实验设计: 强** — 
     这是 proposal 最突出的亮点。7 个 ablation（formal-only, neural-only, random routing, oracle routing, threshold sweep, try-formal-first fallback, label noise analysis）非常全面，特别是 ablation 6 直接测试了最自然的 trivial alternative，ablation 4 给出了性能上限。Baseline 矩阵包括 pure neural (GenPRM, ThinkPRM, R-PRM), pure formal (FoVer), hybrid (VERGE, Naive Hybrid), LLM-as-Judge, compute-matched comparison，覆盖全面。Compute fairness 分析（包含 autoformalization 成本）和 honest coverage reporting 遵循了领域最佳实践（ThinkPRM 的 token-budget paradigm, Risk-Controlled 方法论）。Miracle step detection 的评估有 primary data source (RRM) + proxy (PRMBench) + self-constructed human annotation 的三级方案。唯一的小遗憾是没有对 OOD 场景（如 code reasoning, scientific reasoning beyond GPQA）做更多规划。

  4. **可行性: 强** — 
     计算预算合理：Qwen3-8B LoRA 训练 4-8 H100 GPU-hours，全流程评估 <5 天 on 8×H100。所有核心组件（FoVer 代码、GenPRM 权重、Qwen 系列模型、Z3 solver）均已公开可用。最大的不确定性是 roundtrip verification 的实际通过率和 formal branch 的 effective coverage——但 proposal 已将这些作为实验指标来报告，而非作为必须成功的前提条件。

  5. **写作与呈现: 强** — 
     Proposal 结构清晰、逻辑连贯。Research opportunity 的三条 converging gaps 叙事有说服力。对 autoformalization 局限性的诚实讨论（引用 Risk-Controlled 的具体数据）和对 conditional soundness 的明确界定显示了学术诚实。Related work 覆盖 14+ 篇论文并精确标注了与本工作的区别。技术细节（pipeline 三层、输出 confidence tier 分级）描述精确。一个改进点是：可以更早、更显著地讨论 "learned routing vs. try-and-fallback 的预期优势"，以预防最明显的审稿人质疑。

【概率估计】: [28% - 42%] 中位 34%

【估计理由】:
向上因素：
- 研究问题定位精准，填补了 VERGE 明确指出的 learned routing gap（+）
- 实验设计异常完备，ablation 设计直接回应最自然的质疑（+）
- 对 autoformalization 局限性的诚实处理遵循领域最佳实践（+）
- 计算预算合理，可行性高（+）
- 领域热度高，PRM 是当前 reasoning 研究的焦点（+）

向下因素：
- 核心 novelty（learned binary classifier for routing）技术复杂度有限，可能被视为"incremental over VERGE"（-）
- Formal branch 的 effective soundness coverage 可能仅 10-20%，实际影响力有限（-）
- 如果 ablation 6（try-formal-first fallback）表现接近 learned router，核心贡献将被严重质疑（-）
- Neural branch 对大部分步骤直接退化为 GenPRM，系统的实际增量价值可能有限（-）
- 没有初步实验结果支撑 learned routing 优于 try-and-fallback 的假设（-）

综合判断：这是一篇 solid 但 novelty 中等的工作。在 AAAI 的激烈竞争中，方向正确 + 实验完备但 novelty 不够突出的论文通常处于 borderline 区间。中位 34% 反映了"质量高于平均投稿但不足以进入上半区"的定位。

【主要风险】:
1. **Ablation 6 风险（致命）**: Try-formal-first + neural fallback 是零训练成本的 trivial alternative。如果其性能接近 learned router（差距 <2-3% F1），审稿人将直接判定 learned routing 没有足够的价值，论文的核心贡献不成立。这是最大的单点风险。
2. **Effective coverage 过低风险（严重）**: 如果 formal branch 最终只覆盖 10-15% 的步骤且这些步骤本身错误率低（形式化步骤通常较简单、错误率较低），那么"conditional sound miracle detection" 在最需要检测 miracle steps 的困难步骤上恰恰无能为力——审稿人会质疑条件性保证的实际价值。

【实施评估】:
  - 计算资源: 单节点 8×H100，训练 <1 天，评估 <5 天。主要成本在 Qwen2.5-Math-72B-Instruct 的 autoformalization 推理（dominant cost）。学术实验室可行。
  - 数据需求: FoVer ~80K 标签（已公开），ProcessBench/PRMBench（已公开），MATH-500/AIME24（已公开），人工标注 200-300 步骤用于 miracle step 评估 + 100-200 formalizability oracle labels + 200-300 router label noise audit。总人工标注量约 500-800 个样本。
  - 人工介入: 中等。需要 2-3 名标注员进行 miracle step 标注、formalizability oracle 标注、router label audit，并计算 inter-annotator agreement (Cohen's kappa)。
  - 训练需求: Qwen3-8B LoRA fine-tuning（轻量）。不需要从头训练大模型。GenPRM-7B 使用预训练权重，不需要额外训练。
  - 新 Benchmark: 不需要构建全新 benchmark。使用已有 ProcessBench, PRMBench, MATH-500, AIME24, GPQA-Diamond。自建 miracle step 标注集 (200-300 steps) 规模较小。
  - 预估周期: 6-10 周。Router 训练 1-2 周（含数据准备），Pipeline 集成 1-2 周，全面评估 2-3 周，人工标注并行进行 2-3 周，写作 2 周。AAAI 2026 deadline 前可完成。
```

Sources:
- [FoVer: Efficient PRM Training Data Synthesis via Formal Verification](https://arxiv.org/abs/2505.15960)
- [VERGE: Formal Refinement and Guidance Engine](https://arxiv.org/abs/2601.20055)
- [LogicReward: Step-Wise Logical Supervision](https://arxiv.org/abs/2512.18196)
- [GenPRM: Scaling Test-Time Compute of PRMs](https://arxiv.org/abs/2504.00891)
- [ThinkPRM: Process Reward Models That Think](https://arxiv.org/abs/2504.16828)
- [R-PRM: Reasoning-Driven Process Reward Modeling](https://arxiv.org/abs/2503.21295)
- [RRM: Curing Miracle Steps](https://arxiv.org/abs/2510.07774)
- [Risk-Controlled Lean-as-Judge](https://arxiv.org/abs/2605.28365)
- [Faithful Autoformalization via Roundtrip Verification](https://arxiv.org/abs/2604.25031)
- [Do LLMs Game Formalization?](https://arxiv.org/abs/2604.19459)
- [FIRMA: Bidirectional Formal-Informal Mathematical Language Alignment](https://aclanthology.org/2025.mathnlp-main.5/)
- [PRoSFI: Structured Formal Intermediaries](https://arxiv.org/abs/2603.29500)
- [PRMBench: Fine-grained PRM Benchmark](https://prmbench.github.io/)
- [Awesome Process Reward Models](https://github.com/RyanLiu112/Awesome-Process-Reward-Models)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77fb17d8-f180-4c65-85d4-8d0e1884915b",
  "isSidechain": false,
  "requestId": "req_011CbWQHwE3AiDFyqMQZfknR",
  "type": "assistant",
  "uuid": "afd1104d-624f-4a83-85c1-9040f42cf579",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "644ee0d4-56af-4ee5-8097-233dab1a01f6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LgfQxEvMvGTGGfYqoERnFP",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 849,
      "cache_read_input_tokens": 26681,
      "output_tokens": 7196,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 849,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7196,
          "cache_read_input_tokens": 26681,
          "cache_creation_input_tokens": 849,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 849
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

_source line 38_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Formally-Routed Process Reward Models for Sound Miracle Step Detection  ## Core Problem  No existing PRM exploit…",
  "leafUuid": "afd1104d-624f-4a83-85c1-9040f42cf579",
  "sessionId": "644ee0d4-56af-4ee5-8097-233dab1a01f6"
}
```

---

### Runtime record

_source line 39_

```json
{
  "type": "ai-title",
  "aiTitle": "Learned routing for hybrid formal-neural process reward models",
  "sessionId": "644ee0d4-56af-4ee5-8097-233dab1a01f6"
}
```

---
