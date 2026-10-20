# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Axiom-Grounded Self-Verified Perc

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 51
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-2/5facff83-0af4-48a3-a612-caaf81c1db1b.jsonl`
- **Structured JSON:** [`f278b70cec56532dfb33.json`](../../sessions/f2/f278b70cec56532dfb33.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-27T09:09:11.914Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T09:09:11.914Z",
  "sessionId": "5facff83-0af4-48a3-a612-caaf81c1db1b",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Axiom-Grounded Self-Verified Perception for Visual Math Reasoning\n\n## Core Problem and Thesis\n\nCurrent multimodal math reasoning systems verify perceived visual facts independently—checking each claim against the image in isolation—but never verify whether perceived facts are mutually consistent under known mathematical constraints. This causes individually plausible but collectively impossible perceptions to cascade into reasoning failures (61% of multimodal math errors are perception errors per MM-MATH (arXiv 2024)).\n\nWe argue that mathematical perception correctness is fundamentally a joint constraint satisfaction problem, not an independent fact-checking problem: even when each perceived fact has high marginal confidence, the joint set may violate mathematical axioms (e.g., three individually plausible angle estimates that do not sum to 180°). All existing per-claim verification approaches—whether using LLM judges (Perception-R1, arXiv 2025), ground-truth checklists (PEARL, arXiv 2025), image-extracted constraints (EVPV, arXiv 2026), or annotation-dependent synergistic rewards (CogFlow, arXiv 2026)—are structurally blind to such inter-claim inconsistencies.\n\n## Research Opportunity\n\nMathematical diagrams encode structural invariants (geometric theorems like angle sums, Pythagorean constraints, parallel-line properties, circle theorems; chart constraints like sum-to-total; function constraints like monotonicity) that perceived facts must jointly satisfy. These invariants provide a free, dense, automatically verifiable reward signal for RL-based perception training—requiring no ground truth annotations. This is newly feasible because (1) diagram formalization methods (DFE-GPS (AAAI 2025), Geoparsing (arXiv 2026)) now reliably extract structured representations, (2) solver-in-the-loop RL has been proven effective for reasoning (FGeo-DRL achieves 86.4% on formalgeo7k via RL in formal geometry environments (arXiv 2024); sub-goal verifiable rewards unlock geometric reasoning gains (Milestones over Outcome / SGVR, arXiv 2025)), and (3) the perception bottleneck is definitively established (MM-MATH (arXiv 2024); GeoPQA (EMNLP 2025)).\n\nCritically, as more axioms apply to a given diagram, the feasible set of value combinations that satisfy all constraints simultaneously shrinks—making the axiom-consistency reward increasingly informative and reducing the false positive rate (axiom-consistent but factually incorrect perceptions). This \"constraint density\" property means the reward signal quality improves precisely for complex diagrams where perception errors are most damaging.\n\nThe principle that domain-specific structural invariants serve as free self-supervised perception rewards extends beyond mathematics—Kirchhoff's laws for circuit diagrams, valence constraints for chemical structures, dimensional consistency for engineering drawings all exhibit the same structure—though this paper demonstrates the paradigm on mathematical diagrams.\n\n## Research Landscape and Novelty Positioning\n\nWe position our work along two orthogonal dimensions: **what is verified** (per-claim vs. joint consistency) and **how verification is sourced** (annotation-dependent vs. annotation-free). This yields a clear novelty map:\n\n| | Per-claim verification | Joint consistency verification |\n|---|---|---|\n| Annotation-dependent | Perception-R1 (LLM judge + text annotations), PEARL (GT checklists), CogFlow (120K+ annotated MathCog) | — |\n| Translation-fidelity | GeoDPO (DSL translation accuracy) | — |\n| Image-level self-supervised | EVPV (image-extracted per-claim constraints) | — |\n| Domain-agnostic self-supervised | SSL-R1 (visual puzzles), V-Zero (cross-modal self-play) | — |\n| Domain-axiom self-supervised | — | **ASVP (ours)** |\n\n**Annotation-dependent per-claim methods.** Perception-R1 (arXiv 2025) uses LLM-judged visual perception reward with pre-collected textual annotations; only 1,442 training samples but per-claim only. PEARL (arXiv 2025) uses ground-truth perception checklists as gating rewards (+9.7% on MathVerse) but needs annotated sub-question answers. CogFlow (arXiv 2026) proposes a three-stage perception→internalization→reasoning framework with Synergistic Visual Rewards and Knowledge Internalization Reward, achieving strong results but requiring 120K+ perception-reasoning aligned annotations (MathCog dataset); its rewards operate at per-claim level in parametric and semantic spaces without checking inter-claim mathematical consistency.\n\n**Image-level per-claim verification.** EVPV (arXiv 2026) matches per-claim visual checklists against image-extracted constraints—checking each claim independently against image-level perceptual features (e.g., \"this angle appears to be ~60°\")—but does not verify whether the set of perceived values jointly satisfies domain-level mathematical axioms (e.g., \"these three angles must sum to 180°\"). This distinction between image-level perceptual constraints and domain-level mathematical axioms is the precise gap our work fills.\n\n**Translation-fidelity rewards.** GeoDPO (arXiv 2026) uses NL-to-DSL translator-guided RL for geometric perception (+26.5% in-domain, +39% downstream) but rewards DSL translation accuracy, not axiom-level consistency.\n\n**Structural/topological parsing.** SymHPR (arXiv 2025) enforces structural parsing consistency (point-on-line, shape-on-relation) at the topological level. Our approach operates at the quantitative level and depends on reasonable topological parsing—addressed through curriculum design.\n\n**Utility-based and generic self-supervised rewards.** PRCO (arXiv 2026) introduces Observer/Solver role separation with utility-based perception rewards (+7 points average across 8 benchmarks) but does not exploit mathematical structure. SSL-R1 (arXiv 2026) derives rewards from generic SSL puzzles. V-Zero (arXiv 2026) uses Questioner-Solver co-evolution for zero-annotation training. Our advantage over domain-agnostic methods: mathematical invariants provide stronger, more targeted supervision.\n\n**Confidence-based and inference-time methods.** PDCR (arXiv 2026) decomposes rewards via model-internal confidence scores without formal constraints. M3-ACE (arXiv 2026) rectifies perception at inference time via multi-agentic context engineering but does not train perception via RL. PFlowNet (arXiv 2026) applies variational RL with geometric reward shaping where 'geometric' refers to reward landscape geometry, not mathematical theorems.\n\n**Why training-time internalization, not inference-time correction alone.** A natural alternative is axiom checking at inference time without RL training. Training-time internalization offers three advantages: (1) efficiency—trained model produces axiom-consistent perceptions in a single forward pass vs. iterative re-perception loops; (2) representation-level learning—RL shapes internal visual representations to favor axiom-consistent percepts, not just patching outputs; (3) generalization—trained consistency transfers to novel diagram configurations. We validate this through direct ablation.\n\n**Theoretical limitation: false positives.** Axiom-consistency admits false positives—perceived values that are individually incorrect but collectively satisfy axioms (e.g., all angles systematically biased but still summing to 180°). We acknowledge this limitation and argue it is acceptable: (1) axiom verification excludes collectively impossible perceptions, which per-claim methods cannot detect—a net improvement over the status quo; (2) as constraint density increases (more applicable axioms per diagram), the false positive space shrinks dramatically; (3) Stage 2 answer-correctness reward further compensates. We empirically characterize false positive rates across diagram types (see Experimental Design).\n\nNo existing work uses mathematical invariant consistency of perceived quantitative facts as a self-supervised perception reward signal.\n\n## Proposed Approach\n\nWe train a VLM (Qwen3-VL-8B as primary base, Qwen3-VL-3B for scale-transfer validation) to perceive mathematical diagrams accurately using axiom-consistency as a self-supervised RLVR reward, requiring zero ground-truth perception annotations.\n\n**Stage 0: Formal Extraction Warm-Start.** VLMs cannot produce parseable formal descriptions from scratch (Geoparsing (arXiv 2026) itself requires SFT before RLVR). We SFT the base model on a subset of GDP-29K (Geoparsing) and FormalGeo (arXiv 2023) data to bootstrap syntactically valid diagram-to-formal-language extraction. To ensure compute fairness, all RL baselines are also trained from this same Stage 0 checkpoint.\n\n**Stage 1: Perception-Only Axiom RL.** The model extracts structured perception claims (angles, lengths, coordinates, ratios) into a formal constraint description language built on FormalGeo/Geoparsing primitives. A lightweight axiom checker—leveraging FormalGeo's existing theorem verification infrastructure and implementing 40+ geometric theorems plus chart and function invariants in a phased rollout (core 15 direct-check axioms first, extended set second)—evaluates joint satisfaction. The axiom-consistency reward uses soft continuous scoring: for each applicable axiom, violation magnitude is computed (e.g., |angle_sum − 180°|/180°), and the reward is the mean of (1 − normalized_violation) across all applicable axioms. This avoids the sparsity of binary pass/fail. An auxiliary parsability reward (whether the formal description is syntactically valid) supplements consistency reward in early training. For unparseable or partial outputs, the checker evaluates only the parseable subset (graceful degradation). Training uses GRPO via veRL. Curriculum starts with structurally simple diagrams (single triangles, basic charts) and progressively increases complexity.\n\n**Stage 2: Joint Perception-Reasoning.** Combines axiom-consistency reward with outcome-based answer correctness in GRPO training.\n\n**Inference-Time Self-Verification.** Perceived facts violating axioms trigger iterative re-perception (up to 3 iterations).\n\n## Experimental Design\n\n**Benchmarks.** MathVista (ICLR 2024), MathVerse (with vision-only / vision-dominant / vision-intensive subset breakdown), MathVision (NeurIPS 2024), GeoQA, formalgeo7k, WeMath. GeoPerceive (from GeoDPO, arXiv 2026) for perception-only evaluation.\n\n**Baselines (4 categories, all RL baselines run from both raw Qwen3-VL-8B and Stage 0 checkpoint to isolate SFT warm-start contribution).**\n- *Base VLM:* Qwen3-VL-8B zero-shot; Qwen3-VL-8B + SFT only (Stage 0 data, no RL)\n- *Perception RL (controlled, same GRPO framework):* Perception-R1 reward (LLM-judged); GeoDPO reward (DSL-translation accuracy); PRCO reward (utility-based Observer/Solver); SGVR reward (skeleton rate, Milestones over Outcome (arXiv 2025)); answer-only GRPO (answer correctness only, no perception reward)\n- *Self-supervised RL:* SSL-R1 (generic visual puzzle reward) if code available\n- *Oracle:* GT perception reward (using ground-truth formal annotations from formalgeo7k/GeoTrust (TrustGeoGen, arXiv 2025) as reward signal)—quantifies the gap between free axiom reward and oracle GT supervision\n- *Reference numbers:* PEARL (arXiv 2025), EVPV (arXiv 2026), CogFlow (arXiv 2026), M3-ACE (arXiv 2026) reported results where available\n\n**Ablation Studies (6 groups).**\n1. *Reward components:* axiom reward only / answer reward only / axiom + answer (full) / random reward\n2. *Training curriculum:* three-stage (proposed) / skip Stage 0 / skip Stage 1 (joint from scratch) / Stage 1 only\n3. *Axiom set:* full 40+ axioms / basic axioms only (angle sum, Pythagorean) / chart+function invariants only\n4. *Scoring strategy:* soft continuous / hard binary (ε = 0.5°, 1°, 2°) / weighted combination\n5. *Inference-time re-perception:* 0 / 1 / 2 / 3 iterations (performance vs. latency tradeoff)\n6. *Training-time RL vs inference-time-only:* Full ASVP vs. \"Stage 0 SFT + axiom re-perception at inference without RL\"\n\n**Reward Signal Quality Analysis.**\n- On GT-annotated subset: Pearson/Spearman correlation between axiom-consistency score and true perception accuracy\n- False positive / false negative rate analysis\n- **Per-diagram-type discriminability**: separately report axiom reward false positive rates for triangles (strong constraints), quadrilaterals (moderate), circles (moderate-strong), compound figures (weak constraints)\n- **Adversarial perturbation test**: add calibrated noise (σ = 1°, 2°, 5°, 10°) to GT values, measure axiom checker detection rate across constraint densities—quantifies the \"detection frontier\"\n\n**Additional Analyses.**\n- *Perception isolation:* On GeoPerceive benchmark, report perception-level accuracy (element extraction precision/recall, perceived value MAE vs GT); on MathVerse, classify errors as perception vs. reasoning (following MM-MATH taxonomy) pre/post training\n- *Compute fairness:* Training wall-clock time and per-step overhead per method; performance vs. FLOPs curves; axiom checker per-sample latency\n- *Scale transfer:* Qwen3-VL-3B on MathVista, MathVerse\n- *Chart proof-of-concept (optional):* Demonstrate axiom checker effectiveness on MathVista chart questions using sum-to-total constraints\n\n## Key References\n\n- Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward (arXiv 2025)\n- PEARL: Perceptual-Evidence Anchored Reinforced Learning for Multimodal Reasoning (arXiv 2025)\n- Grounding the Score: Explicit Visual Premise Verification for Reliable VLM Process Reward Models [EVPV] (arXiv 2026)\n- Hierarchical Process Reward Models are Symbolic Vision Learners [SymHPR] (arXiv 2025)\n- MM-MATH: Advancing Multimodal Math Evaluation with Process Evaluation and Fine-grained Classification (arXiv 2024)\n- Diagram Formalization Enhanced Multi-Modal Geometry Problem Solver [DFE-GPS] (AAAI 2025)\n- Geoparsing: Diagram Parsing for Plane and Solid Geometry with a Unified Formal Language (arXiv 2026)\n- TrustGeoGen: Formal-Verified Data Engine for Trustworthy Multi-modal Geometric Problem Solving (arXiv 2025)\n- FormalGeo: An Extensible Formalized Framework for Olympiad Geometric Problem Solving (arXiv 2023)\n- GeoPQA: Bridging the Visual Perception Gap in MLLMs for Geometric Reasoning (EMNLP 2025)\n- Enhancing Geometric Perception in VLMs via Translator-Guided Reinforcement Learning [GeoDPO] (arXiv 2026)\n- M3-ACE: Rectifying Visual Perception in Multimodal Math Reasoning via Multi-Agentic Context Engineering (arXiv 2026)\n- PDCR: Perception-Decomposed Confidence Reward for Vision-Language Reasoning (arXiv 2026)\n- SSL-R1: Self-Supervised Visual Reinforcement Post-Training for MLLMs (arXiv 2026)\n- Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning [PRCO] (arXiv 2026)\n- MathVista: Evaluating Mathematical Reasoning of Foundation Models in Visual Contexts (ICLR 2024)\n- FGeo-DRL: Deductive Reasoning for Geometric Problems through Deep Reinforcement Learning (arXiv 2024)\n- A Survey of Multimodal Mathematical Reasoning: From Perception, Alignment to Reasoning (arXiv 2026)\n- Figure It Out: Improve the Frontier of Reasoning with Executable Visual States [FIGR] (arXiv 2025)\n- Milestones over Outcome: Unlocking Geometric Reasoning with Sub-Goal Verifiable Reward [SGVR] (arXiv 2025)\n- PFlowNet: Perceptual Flow Network for Visually Grounded Reasoning (arXiv 2026)\n- Measuring Multimodal Mathematical Reasoning with MATH-Vision Dataset [MathVision] (NeurIPS 2024)\n- V-Zero: Zero-Shot Multimodal Reasoning via Cross-Modal Self-Play (arXiv 2026)\n- CogFlow: Bridging Perception and Reasoning through Knowledge Internalization for Visual Mathematical Problem Solving (arXiv 2026)\n\n## Resource Estimate\n\n- **manual**: gpu_hours: 1800-2200 (8×H100: axiom checker on FormalGeo infrastructure 3 wks, Stage 0 SFT, 6-7 GRPO training runs including PRCO/SGVR baselines at ~30h each, dual-checkpoint baselines, ablation studies, 7-benchmark evaluation, GeoPerceive + adversarial analysis, Qwen3-VL-3B replication), timeline: 10-12 weeks (3 wks axiom checker + data pipeline + Stage 0, 3-4 wks RL training iterations including baselines, 3 wks evaluation + ablation + adversarial analysis + paper writing), estimated_gpu_cost: $4,500-$5,500\n- **human_in_loop**: gpu_hours: 1300-1700, timeline: 7-9 weeks, claude_api_cost: $500-$800, estimated_gpu_cost: $3,250-$4,250\n- **auto_research**: gpu_hours: 2200-2800, timeline: 5-7 weeks, claude_api_cost: $1,000-$1,500, estimated_gpu_cost: $5,500-$7,000, speed_bottleneck: RL convergence under potentially sparse axiom-violation signals; axiom checker robustness on degenerate diagram parses; dual-checkpoint experiment matrix size"
}
```

---

### Runtime record

_source line 2 · 2026-05-27T09:09:11.920Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T09:09:11.920Z",
  "sessionId": "5facff83-0af4-48a3-a612-caaf81c1db1b"
}
```

---

## Round 1

49 recorded events

### User

_source line 3 · 2026-05-27T09:09:11.941Z_

【任务】: 请评估以下 proposal 的客观中稿概率。
必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。

【proposal】:
# Axiom-Grounded Self-Verified Perception for Visual Math Reasoning

## Core Problem and Thesis

Current multimodal math reasoning systems verify perceived visual facts independently—checking each claim against the image in isolation—but never verify whether perceived facts are mutually consistent under known mathematical constraints. This causes individually plausible but collectively impossible perceptions to cascade into reasoning failures (61% of multimodal math errors are perception errors per MM-MATH (arXiv 2024)).

We argue that mathematical perception correctness is fundamentally a joint constraint satisfaction problem, not an independent fact-checking problem: even when each perceived fact has high marginal confidence, the joint set may violate mathematical axioms (e.g., three individually plausible angle estimates that do not sum to 180°). All existing per-claim verification approaches—whether using LLM judges (Perception-R1, arXiv 2025), ground-truth checklists (PEARL, arXiv 2025), image-extracted constraints (EVPV, arXiv 2026), or annotation-dependent synergistic rewards (CogFlow, arXiv 2026)—are structurally blind to such inter-claim inconsistencies.

## Research Opportunity

Mathematical diagrams encode structural invariants (geometric theorems like angle sums, Pythagorean constraints, parallel-line properties, circle theorems; chart constraints like sum-to-total; function constraints like monotonicity) that perceived facts must jointly satisfy. These invariants provide a free, dense, automatically verifiable reward signal for RL-based perception training—requiring no ground truth annotations. This is newly feasible because (1) diagram formalization methods (DFE-GPS (AAAI 2025), Geoparsing (arXiv 2026)) now reliably extract structured representations, (2) solver-in-the-loop RL has been proven effective for reasoning (FGeo-DRL achieves 86.4% on formalgeo7k via RL in formal geometry environments (arXiv 2024); sub-goal verifiable rewards unlock geometric reasoning gains (Milestones over Outcome / SGVR, arXiv 2025)), and (3) the perception bottleneck is definitively established (MM-MATH (arXiv 2024); GeoPQA (EMNLP 2025)).

Critically, as more axioms apply to a given diagram, the feasible set of value combinations that satisfy all constraints simultaneously shrinks—making the axiom-consistency reward increasingly informative and reducing the false positive rate (axiom-consistent but factually incorrect perceptions). This "constraint density" property means the reward signal quality improves precisely for complex diagrams where perception errors are most damaging.

The principle that domain-specific structural invariants serve as free self-supervised perception rewards extends beyond mathematics—Kirchhoff's laws for circuit diagrams, valence constraints for chemical structures, dimensional consistency for engineering drawings all exhibit the same structure—though this paper demonstrates the paradigm on mathematical diagrams.

## Research Landscape and Novelty Positioning

We position our work along two orthogonal dimensions: **what is verified** (per-claim vs. joint consistency) and **how verification is sourced** (annotation-dependent vs. annotation-free). This yields a clear novelty map:

| | Per-claim verification | Joint consistency verification |
|---|---|---|
| Annotation-dependent | Perception-R1 (LLM judge + text annotations), PEARL (GT checklists), CogFlow (120K+ annotated MathCog) | — |
| Translation-fidelity | GeoDPO (DSL translation accuracy) | — |
| Image-level self-supervised | EVPV (image-extracted per-claim constraints) | — |
| Domain-agnostic self-supervised | SSL-R1 (visual puzzles), V-Zero (cross-modal self-play) | — |
| Domain-axiom self-supervised | — | **ASVP (ours)** |

**Annotation-dependent per-claim methods.** Perception-R1 (arXiv 2025) uses LLM-judged visual perception reward with pre-collected textual annotations; only 1,442 training samples but per-claim only. PEARL (arXiv 2025) uses ground-truth perception checklists as gating rewards (+9.7% on MathVerse) but needs annotated sub-question answers. CogFlow (arXiv 2026) proposes a three-stage perception→internalization→reasoning framework with Synergistic Visual Rewards and Knowledge Internalization Reward, achieving strong results but requiring 120K+ perception-reasoning aligned annotations (MathCog dataset); its rewards operate at per-claim level in parametric and semantic spaces without checking inter-claim mathematical consistency.

**Image-level per-claim verification.** EVPV (arXiv 2026) matches per-claim visual checklists against image-extracted constraints—checking each claim independently against image-level perceptual features (e.g., "this angle appears to be ~60°")—but does not verify whether the set of perceived values jointly satisfies domain-level mathematical axioms (e.g., "these three angles must sum to 180°"). This distinction between image-level perceptual constraints and domain-level mathematical axioms is the precise gap our work fills.

**Translation-fidelity rewards.** GeoDPO (arXiv 2026) uses NL-to-DSL translator-guided RL for geometric perception (+26.5% in-domain, +39% downstream) but rewards DSL translation accuracy, not axiom-level consistency.

**Structural/topological parsing.** SymHPR (arXiv 2025) enforces structural parsing consistency (point-on-line, shape-on-relation) at the topological level. Our approach operates at the quantitative level and depends on reasonable topological parsing—addressed through curriculum design.

**Utility-based and generic self-supervised rewards.** PRCO (arXiv 2026) introduces Observer/Solver role separation with utility-based perception rewards (+7 points average across 8 benchmarks) but does not exploit mathematical structure. SSL-R1 (arXiv 2026) derives rewards from generic SSL puzzles. V-Zero (arXiv 2026) uses Questioner-Solver co-evolution for zero-annotation training. Our advantage over domain-agnostic methods: mathematical invariants provide stronger, more targeted supervision.

**Confidence-based and inference-time methods.** PDCR (arXiv 2026) decomposes rewards via model-internal confidence scores without formal constraints. M3-ACE (arXiv 2026) rectifies perception at inference time via multi-agentic context engineering but does not train perception via RL. PFlowNet (arXiv 2026) applies variational RL with geometric reward shaping where 'geometric' refers to reward landscape geometry, not mathematical theorems.

**Why training-time internalization, not inference-time correction alone.** A natural alternative is axiom checking at inference time without RL training. Training-time internalization offers three advantages: (1) efficiency—trained model produces axiom-consistent perceptions in a single forward pass vs. iterative re-perception loops; (2) representation-level learning—RL shapes internal visual representations to favor axiom-consistent percepts, not just patching outputs; (3) generalization—trained consistency transfers to novel diagram configurations. We validate this through direct ablation.

**Theoretical limitation: false positives.** Axiom-consistency admits false positives—perceived values that are individually incorrect but collectively satisfy axioms (e.g., all angles systematically biased but still summing to 180°). We acknowledge this limitation and argue it is acceptable: (1) axiom verification excludes collectively impossible perceptions, which per-claim methods cannot detect—a net improvement over the status quo; (2) as constraint density increases (more applicable axioms per diagram), the false positive space shrinks dramatically; (3) Stage 2 answer-correctness reward further compensates. We empirically characterize false positive rates across diagram types (see Experimental Design).

No existing work uses mathematical invariant consistency of perceived quantitative facts as a self-supervised perception reward signal.

## Proposed Approach

We train a VLM (Qwen3-VL-8B as primary base, Qwen3-VL-3B for scale-transfer validation) to perceive mathematical diagrams accurately using axiom-consistency as a self-supervised RLVR reward, requiring zero ground-truth perception annotations.

**Stage 0: Formal Extraction Warm-Start.** VLMs cannot produce parseable formal descriptions from scratch (Geoparsing (arXiv 2026) itself requires SFT before RLVR). We SFT the base model on a subset of GDP-29K (Geoparsing) and FormalGeo (arXiv 2023) data to bootstrap syntactically valid diagram-to-formal-language extraction. To ensure compute fairness, all RL baselines are also trained from this same Stage 0 checkpoint.

**Stage 1: Perception-Only Axiom RL.** The model extracts structured perception claims (angles, lengths, coordinates, ratios) into a formal constraint description language built on FormalGeo/Geoparsing primitives. A lightweight axiom checker—leveraging FormalGeo's existing theorem verification infrastructure and implementing 40+ geometric theorems plus chart and function invariants in a phased rollout (core 15 direct-check axioms first, extended set second)—evaluates joint satisfaction. The axiom-consistency reward uses soft continuous scoring: for each applicable axiom, violation magnitude is computed (e.g., |angle_sum − 180°|/180°), and the reward is the mean of (1 − normalized_violation) across all applicable axioms. This avoids the sparsity of binary pass/fail. An auxiliary parsability reward (whether the formal description is syntactically valid) supplements consistency reward in early training. For unparseable or partial outputs, the checker evaluates only the parseable subset (graceful degradation). Training uses GRPO via veRL. Curriculum starts with structurally simple diagrams (single triangles, basic charts) and progressively increases complexity.

**Stage 2: Joint Perception-Reasoning.** Combines axiom-consistency reward with outcome-based answer correctness in GRPO training.

**Inference-Time Self-Verification.** Perceived facts violating axioms trigger iterative re-perception (up to 3 iterations).

## Experimental Design

**Benchmarks.** MathVista (ICLR 2024), MathVerse (with vision-only / vision-dominant / vision-intensive subset breakdown), MathVision (NeurIPS 2024), GeoQA, formalgeo7k, WeMath. GeoPerceive (from GeoDPO, arXiv 2026) for perception-only evaluation.

**Baselines (4 categories, all RL baselines run from both raw Qwen3-VL-8B and Stage 0 checkpoint to isolate SFT warm-start contribution).**
- *Base VLM:* Qwen3-VL-8B zero-shot; Qwen3-VL-8B + SFT only (Stage 0 data, no RL)
- *Perception RL (controlled, same GRPO framework):* Perception-R1 reward (LLM-judged); GeoDPO reward (DSL-translation accuracy); PRCO reward (utility-based Observer/Solver); SGVR reward (skeleton rate, Milestones over Outcome (arXiv 2025)); answer-only GRPO (answer correctness only, no perception reward)
- *Self-supervised RL:* SSL-R1 (generic visual puzzle reward) if code available
- *Oracle:* GT perception reward (using ground-truth formal annotations from formalgeo7k/GeoTrust (TrustGeoGen, arXiv 2025) as reward signal)—quantifies the gap between free axiom reward and oracle GT supervision
- *Reference numbers:* PEARL (arXiv 2025), EVPV (arXiv 2026), CogFlow (arXiv 2026), M3-ACE (arXiv 2026) reported results where available

**Ablation Studies (6 groups).**
1. *Reward components:* axiom reward only / answer reward only / axiom + answer (full) / random reward
2. *Training curriculum:* three-stage (proposed) / skip Stage 0 / skip Stage 1 (joint from scratch) / Stage 1 only
3. *Axiom set:* full 40+ axioms / basic axioms only (angle sum, Pythagorean) / chart+function invariants only
4. *Scoring strategy:* soft continuous / hard binary (ε = 0.5°, 1°, 2°) / weighted combination
5. *Inference-time re-perception:* 0 / 1 / 2 / 3 iterations (performance vs. latency tradeoff)
6. *Training-time RL vs inference-time-only:* Full ASVP vs. "Stage 0 SFT + axiom re-perception at inference without RL"

**Reward Signal Quality Analysis.**
- On GT-annotated subset: Pearson/Spearman correlation between axiom-consistency score and true perception accuracy
- False positive / false negative rate analysis
- **Per-diagram-type discriminability**: separately report axiom reward false positive rates for triangles (strong constraints), quadrilaterals (moderate), circles (moderate-strong), compound figures (weak constraints)
- **Adversarial perturbation test**: add calibrated noise (σ = 1°, 2°, 5°, 10°) to GT values, measure axiom checker detection rate across constraint densities—quantifies the "detection frontier"

**Additional Analyses.**
- *Perception isolation:* On GeoPerceive benchmark, report perception-level accuracy (element extraction precision/recall, perceived value MAE vs GT); on MathVerse, classify errors as perception vs. reasoning (following MM-MATH taxonomy) pre/post training
- *Compute fairness:* Training wall-clock time and per-step overhead per method; performance vs. FLOPs curves; axiom checker per-sample latency
- *Scale transfer:* Qwen3-VL-3B on MathVista, MathVerse
- *Chart proof-of-concept (optional):* Demonstrate axiom checker effectiveness on MathVista chart questions using sum-to-total constraints

## Key References

- Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward (arXiv 2025)
- PEARL: Perceptual-Evidence Anchored Reinforced Learning for Multimodal Reasoning (arXiv 2025)
- Grounding the Score: Explicit Visual Premise Verification for Reliable VLM Process Reward Models [EVPV] (arXiv 2026)
- Hierarchical Process Reward Models are Symbolic Vision Learners [SymHPR] (arXiv 2025)
- MM-MATH: Advancing Multimodal Math Evaluation with Process Evaluation and Fine-grained Classification (arXiv 2024)
- Diagram Formalization Enhanced Multi-Modal Geometry Problem Solver [DFE-GPS] (AAAI 2025)
- Geoparsing: Diagram Parsing for Plane and Solid Geometry with a Unified Formal Language (arXiv 2026)
- TrustGeoGen: Formal-Verified Data Engine for Trustworthy Multi-modal Geometric Problem Solving (arXiv 2025)
- FormalGeo: An Extensible Formalized Framework for Olympiad Geometric Problem Solving (arXiv 2023)
- GeoPQA: Bridging the Visual Perception Gap in MLLMs for Geometric Reasoning (EMNLP 2025)
- Enhancing Geometric Perception in VLMs via Translator-Guided Reinforcement Learning [GeoDPO] (arXiv 2026)
- M3-ACE: Rectifying Visual Perception in Multimodal Math Reasoning via Multi-Agentic Context Engineering (arXiv 2026)
- PDCR: Perception-Decomposed Confidence Reward for Vision-Language Reasoning (arXiv 2026)
- SSL-R1: Self-Supervised Visual Reinforcement Post-Training for MLLMs (arXiv 2026)
- Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning [PRCO] (arXiv 2026)
- MathVista: Evaluating Mathematical Reasoning of Foundation Models in Visual Contexts (ICLR 2024)
- FGeo-DRL: Deductive Reasoning for Geometric Problems through Deep Reinforcement Learning (arXiv 2024)
- A Survey of Multimodal Mathematical Reasoning: From Perception, Alignment to Reasoning (arXiv 2026)
- Figure It Out: Improve the Frontier of Reasoning with Executable Visual States [FIGR] (arXiv 2025)
- Milestones over Outcome: Unlocking Geometric Reasoning with Sub-Goal Verifiable Reward [SGVR] (arXiv 2025)
- PFlowNet: Perceptual Flow Network for Visually Grounded Reasoning (arXiv 2026)
- Measuring Multimodal Mathematical Reasoning with MATH-Vision Dataset [MathVision] (NeurIPS 2024)
- V-Zero: Zero-Shot Multimodal Reasoning via Cross-Modal Self-Play (arXiv 2026)
- CogFlow: Bridging Perception and Reasoning through Knowledge Internalization for Visual Mathematical Problem Solving (arXiv 2026)

## Resource Estimate

- **manual**: gpu_hours: 1800-2200 (8×H100: axiom checker on FormalGeo infrastructure 3 wks, Stage 0 SFT, 6-7 GRPO training runs including PRCO/SGVR baselines at ~30h each, dual-checkpoint baselines, ablation studies, 7-benchmark evaluation, GeoPerceive + adversarial analysis, Qwen3-VL-3B replication), timeline: 10-12 weeks (3 wks axiom checker + data pipeline + Stage 0, 3-4 wks RL training iterations including baselines, 3 wks evaluation + ablation + adversarial analysis + paper writing), estimated_gpu_cost: $4,500-$5,500
- **human_in_loop**: gpu_hours: 1300-1700, timeline: 7-9 weeks, claude_api_cost: $500-$800, estimated_gpu_cost: $3,250-$4,250
- **auto_research**: gpu_hours: 2200-2800, timeline: 5-7 weeks, claude_api_cost: $1,000-$1,500, estimated_gpu_cost: $5,500-$7,000, speed_bottleneck: RL convergence under potentially sparse axiom-violation signals; axiom checker robustness on degenerate diagram parses; dual-checkpoint experiment matrix size

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "d0596239-f589-4752-b6af-bbf7d6ed140d",
  "type": "user",
  "uuid": "f0eea63c-1315-493e-b8fb-8c32355514b9",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5facff83-0af4-48a3-a612-caaf81c1db1b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-27T09:09:11.939Z_

```json
{
  "parentUuid": "f0eea63c-1315-493e-b8fb-8c32355514b9",
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
  "uuid": "f5dc0e7c-8ba7-4f6b-bb61-d43e9470c717",
  "timestamp": "2026-05-27T09:09:11.939Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5facff83-0af4-48a3-a612-caaf81c1db1b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-27T09:09:11.939Z_

```json
{
  "parentUuid": "f5dc0e7c-8ba7-4f6b-bb61-d43e9470c717",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "e6232a82-02d2-4e9b-b45e-2a69e594ba9f",
  "timestamp": "2026-05-27T09:09:11.939Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5facff83-0af4-48a3-a612-caaf81c1db1b",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Axiom-Grounded Self-Verified Perception for Visual Math Reasoning  ## Core Problem and Thesis  Current multimoda…",
  "leafUuid": "e6232a82-02d2-4e9b-b45e-2a69e594ba9f",
  "sessionId": "5facff83-0af4-48a3-a612-caaf81c1db1b"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Axiom-grounded self-verified perception for math reasoning",
  "sessionId": "5facff83-0af4-48a3-a612-caaf81c1db1b"
}
```

---

### Assistant

_source line 8 · 2026-05-27T09:09:17.057Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to evaluate a research proposal for AAAI 2026 submission. I need to first do thorough web searches to understand the current landscape, then provide an objective assessment following the specified rubric.

Let me start by searching for the key related works and the current state of the field.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e6232a82-02d2-4e9b-b45e-2a69e594ba9f",
  "isSidechain": false,
  "requestId": "req_011CbSp2so2maXFcadGjAput",
  "type": "assistant",
  "uuid": "ce7bb3cf-0700-4c8d-a787-32e63b6acafc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5facff83-0af4-48a3-a612-caaf81c1db1b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UkqAN7EpgQznKAaQMemFPz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5963,
      "cache_read_input_tokens": 13968,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5963,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 189,
          "cache_read_input_tokens": 13968,
          "cache_creation_input_tokens": 5963,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5963
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

_source line 9 · 2026-05-27T09:09:18.029Z_

I'll start by conducting thorough web searches to understand the current research landscape before making any assessments. Let me search for the key topics and competing works.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce7bb3cf-0700-4c8d-a787-32e63b6acafc",
  "isSidechain": false,
  "requestId": "req_011CbSp2so2maXFcadGjAput",
  "type": "assistant",
  "uuid": "499b217a-9737-418e-a774-81105501ea64",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5facff83-0af4-48a3-a612-caaf81c1db1b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UkqAN7EpgQznKAaQMemFPz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5963,
      "cache_read_input_tokens": 13968,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5963,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 189,
          "cache_read_input_tokens": 13968,
          "cache_creation_input_tokens": 5963,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5963
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

_source line 10 · 2026-05-27T09:09:18.290Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01XS3Qawq2WgJQ6HMvZGEnix`</summary>

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
  "parentUuid": "499b217a-9737-418e-a774-81105501ea64",
  "isSidechain": false,
  "requestId": "req_011CbSp2so2maXFcadGjAput",
  "type": "assistant",
  "uuid": "e79d1d86-b8da-4ea8-8b83-29f422397810",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5facff83-0af4-48a3-a612-caaf81c1db1b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UkqAN7EpgQznKAaQMemFPz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5963,
      "cache_read_input_tokens": 13968,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5963,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 189,
          "cache_read_input_tokens": 13968,
          "cache_creation_input_tokens": 5963,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5963
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

_source line 11 · 2026-05-27T09:09:18.297Z_

<details><summary>↩ Tool result · `toolu_01XS3Qawq2WgJQ6HMvZGEnix`</summary>

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
  "parentUuid": "e79d1d86-b8da-4ea8-8b83-29f422397810",
  "isSidechain": false,
  "promptId": "d0596239-f589-4752-b6af-bbf7d6ed140d",
  "type": "user",
  "uuid": "3dea7b67-6d99-4464-87df-be67f7ce5654",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "e79d1d86-b8da-4ea8-8b83-29f422397810",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5facff83-0af4-48a3-a612-caaf81c1db1b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-27T09:09:25.813Z_

Now let me conduct multiple targeted searches to understand the research landscape.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3dea7b67-6d99-4464-87df-be67f7ce5654",
  "isSidechain": false,
  "requestId": "req_011CbSp3M1PK3G13PqP1GyGt",
  "type": "assistant",
  "uuid": "ce7a5fad-bbe3-4d8c-827e-9e2b049628c8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5facff83-0af4-48a3-a612-caaf81c1db1b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Bo22DiDSnexTWuwHJkxT2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 717,
      "cache_read_input_tokens": 19931,
      "output_tokens": 277,
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
          "output_tokens": 277,
          "cache_read_input_tokens": 19931,
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

_source line 13 · 2026-05-27T09:09:26.330Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013PULpuYD2fsFcPzKpdJVcY`</summary>

```json
{
  "query": "Perception-R1 visual perception reward multimodal math reasoning 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce7a5fad-bbe3-4d8c-827e-9e2b049628c8",
  "isSidechain": false,
  "requestId": "req_011CbSp3M1PK3G13PqP1GyGt",
  "type": "assistant",
  "uuid": "ce810311-9f24-4bcd-b31d-df0662c1aae0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5facff83-0af4-48a3-a612-caaf81c1db1b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Bo22DiDSnexTWuwHJkxT2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 717,
      "cache_read_input_tokens": 19931,
      "output_tokens": 277,
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
          "output_tokens": 277,
          "cache_read_input_tokens": 19931,
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

_source line 14 · 2026-05-27T09:09:27.249Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01K61RwH6DVQo5tgxH4nVbwv`</summary>

```json
{
  "query": "EVPV visual premise verification VLM reward model 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce810311-9f24-4bcd-b31d-df0662c1aae0",
  "isSidechain": false,
  "requestId": "req_011CbSp3M1PK3G13PqP1GyGt",
  "type": "assistant",
  "uuid": "727c6f53-318b-4481-9e58-b96150c7d1f5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5facff83-0af4-48a3-a612-caaf81c1db1b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Bo22DiDSnexTWuwHJkxT2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 717,
      "cache_read_input_tokens": 19931,
      "output_tokens": 277,
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
          "output_tokens": 277,
          "cache_read_input_tokens": 19931,
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

_source line 15 · 2026-05-27T09:09:27.757Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DkgaAcpiYecCPsxKG4qkZE`</summary>

```json
{
  "query": "CogFlow perception reasoning knowledge internalization visual math 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "727c6f53-318b-4481-9e58-b96150c7d1f5",
  "isSidechain": false,
  "requestId": "req_011CbSp3M1PK3G13PqP1GyGt",
  "type": "assistant",
  "uuid": "4b75a1b6-e49e-411c-800b-bd706eddbe62",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5facff83-0af4-48a3-a612-caaf81c1db1b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Bo22DiDSnexTWuwHJkxT2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 717,
      "cache_read_input_tokens": 19931,
      "output_tokens": 277,
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
          "output_tokens": 277,
          "cache_read_input_tokens": 19931,
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

_source line 16 · 2026-05-27T09:09:28.285Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01V8DLVrYGhWimUNre7TVVKA`</summary>

```json
{
  "query": "GeoDPO translator guided reinforcement learning geometric perception 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b75a1b6-e49e-411c-800b-bd706eddbe62",
  "isSidechain": false,
  "requestId": "req_011CbSp3M1PK3G13PqP1GyGt",
  "type": "assistant",
  "uuid": "2bc718d6-22f7-48eb-b518-4bc6a9598371",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5facff83-0af4-48a3-a612-caaf81c1db1b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Bo22DiDSnexTWuwHJkxT2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 717,
      "cache_read_input_tokens": 19931,
      "output_tokens": 277,
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
          "output_tokens": 277,
          "cache_read_input_tokens": 19931,
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

_source line 17 · 2026-05-27T09:09:28.837Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HSfM4vSWQtvyNR6XTGfcpU`</summary>

```json
{
  "query": "axiom consistency constraint satisfaction visual perception math diagram reasoning 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2bc718d6-22f7-48eb-b518-4bc6a9598371",
  "isSidechain": false,
  "requestId": "req_011CbSp3M1PK3G13PqP1GyGt",
  "type": "assistant",
  "uuid": "d37dcc43-3eaf-4acf-a6ac-0e66594a2d70",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5facff83-0af4-48a3-a612-caaf81c1db1b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Bo22DiDSnexTWuwHJkxT2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 717,
      "cache_read_input_tokens": 19931,
      "output_tokens": 277,
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
          "output_tokens": 277,
          "cache_read_input_tokens": 19931,
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

_source line 18 · 2026-05-27T09:09:33.087Z_

<details><summary>↩ Tool result · `toolu_01V8DLVrYGhWimUNre7TVVKA`</summary>

```text
Web search results for query: "GeoDPO translator guided reinforcement learning geometric perception 2026"

Links: [{"title":"[2602.22703] Enhancing Geometric Perception in VLMs via Translator-Guided Reinforcement Learning","url":"https://arxiv.org/abs/2602.22703"},{"title":"ENHANCING GEOMETRIC PERCEPTION IN VLMS VIA ...","url":"https://openreview.net/pdf/1d34e77e69e361bec95c3bd9bc4687f25c4a670d.pdf"},{"title":"Enhancing Geometric Perception in VLMs via Translator-Guided Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=O70LkLl3gW"},{"title":"Enhancing Geometric Perception in VLMs via Translator-Guided Reinforcement Learning","url":"https://arxiv.org/pdf/2602.22703"},{"title":"GeoPQA: Bridging the Visual Perception Gap in MLLMs for Geometric Reasoning","url":"https://arxiv.org/pdf/2509.17437"}]

Based on the search results, here's what I found:

GeoDPO is a translator-guided reinforcement learning framework that employs an NL-to-DSL (natural language to domain-specific language) translator trained on synthetic pairs to bridge natural language and domain-specific language. 

Vision-language models (VLMs) often struggle with geometric reasoning due to their limited perception of fundamental diagram elements. To address this, the researchers introduced GeoPerceive, a benchmark comprising diagram instances paired with domain-specific language representations and an efficient automatic data generation pipeline.

The translator in GeoDPO facilitates the computation of fine-grained, DSL-level scores, which serve as reward signals in reinforcement learning.

**Performance Results:**

GeoDPO achieved substantial gains of +26.5% on in-domain data, +8.0% on out-of-domain data, and +39.0% on downstream reasoning tasks, significantly outperforming supervised fine-tuning approaches.

The research appears to have been recently published, with the paper posted on arXiv in February 2026. Code and data are released at https://github.com/Longin-Yu/GeoPerceive.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2bc718d6-22f7-48eb-b518-4bc6a9598371",
  "isSidechain": false,
  "promptId": "d0596239-f589-4752-b6af-bbf7d6ed140d",
  "type": "user",
  "uuid": "eca061a4-ab55-4abb-ae4d-14638ae0b93b",
  "toolUseResult": {
    "query": "GeoDPO translator guided reinforcement learning geometric perception 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01AZJRXutbrXZtmxn7dfLWAn",
        "content": [
          {
            "title": "[2602.22703] Enhancing Geometric Perception in VLMs via Translator-Guided Reinforcement Learning",
            "url": "https://arxiv.org/abs/2602.22703"
          },
          {
            "title": "ENHANCING GEOMETRIC PERCEPTION IN VLMS VIA ...",
            "url": "https://openreview.net/pdf/1d34e77e69e361bec95c3bd9bc4687f25c4a670d.pdf"
          },
          {
            "title": "Enhancing Geometric Perception in VLMs via Translator-Guided Reinforcement Learning | OpenReview",
            "url": "https://openreview.net/forum?id=O70LkLl3gW"
          },
          {
            "title": "Enhancing Geometric Perception in VLMs via Translator-Guided Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2602.22703"
          },
          {
            "title": "GeoPQA: Bridging the Visual Perception Gap in MLLMs for Geometric Reasoning",
            "url": "https://arxiv.org/pdf/2509.17437"
          }
        ]
      },
      "Based on the search results, here's what I found:\n\nGeoDPO is a translator-guided reinforcement learning framework that employs an NL-to-DSL (natural language to domain-specific language) translator trained on synthetic pairs to bridge natural language and domain-specific language. \n\nVision-language models (VLMs) often struggle with geometric reasoning due to their limited perception of fundamental diagram elements. To address this, the researchers introduced GeoPerceive, a benchmark comprising diagram instances paired with domain-specific language representations and an efficient automatic data generation pipeline.\n\nThe translator in GeoDPO facilitates the computation of fine-grained, DSL-level scores, which serve as reward signals in reinforcement learning.\n\n**Performance Results:**\n\nGeoDPO achieved substantial gains of +26.5% on in-domain data, +8.0% on out-of-domain data, and +39.0% on downstream reasoning tasks, significantly outperforming supervised fine-tuning approaches.\n\nThe research appears to have been recently published, with the paper posted on arXiv in February 2026. Code and data are released at https://github.com/Longin-Yu/GeoPerceive."
    ],
    "durationSeconds": 4.795097644999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "2bc718d6-22f7-48eb-b518-4bc6a9598371",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5facff83-0af4-48a3-a612-caaf81c1db1b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-27T09:09:34.319Z_

<details><summary>↩ Tool result · `toolu_013PULpuYD2fsFcPzKpdJVcY`</summary>

```text
Web search results for query: "Perception-R1 visual perception reward multimodal math reasoning 2025"

Links: [{"title":"Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward","url":"https://arxiv.org/html/2506.07218v2"},{"title":"Enhancing MLLM Reasoning with Visual Rewards","url":"https://www.emergentmind.com/papers/2506.07218"},{"title":"Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward [Quick Review]","url":"https://liner.com/review/perceptionr1-advancing-multimodal-reasoning-capabilities-of-mllms-via-visual-perception"},{"title":"GitHub - tongxiao2002/Perception-R1: The official repo of paper: \"Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward\"","url":"https://github.com/tongxiao2002/Perception-R1"},{"title":"Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward | OpenReview","url":"https://openreview.net/forum?id=KttCXdjj4w"},{"title":"[2506.07218] Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward","url":"https://arxiv.org/abs/2506.07218"},{"title":"Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward","url":"https://arxiv.org/pdf/2506.07218"}]

Based on the search results, here's what I found about Perception-R1:

## Overview

Perception-R1 introduces a novel visual perception reward that explicitly encourages MLLMs to perceive the visual content accurately, thereby effectively incentivizing both their multimodal perception and reasoning capabilities.

## Key Problem Addressed

Previous works largely overlook the enhancement of multimodal perception capabilities in MLLMs, which serve as a core prerequisite and foundational component of complex multimodal reasoning, and existing RLVR methods fail to effectively enhance the multimodal perception capabilities of MLLMs.

## Methodology

The approach collects textual visual annotations from CoT trajectories of multimodal problems as visual references for reward assignment, and during RLVR training, employs a judging LLM to assess the consistency between visual annotations and MLLM responses, assigning the visual perception reward based on consistency judgments.

## Performance Results

Perception-R1-7B achieves 74.2 on MathVista testmini, 54.3 on MathVerse testmini, and 72.0 on WeMath testmini, which are generally higher than the best open-source reasoning MLLMs like SophiaVL-R1-7B and Vision-R1-7B.

Extensive experiments on several multimodal math and general benchmarks demonstrate the effectiveness of Perception-R1, which achieves superior performance on all benchmarks using only 1,442 training data.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ce810311-9f24-4bcd-b31d-df0662c1aae0",
  "isSidechain": false,
  "promptId": "d0596239-f589-4752-b6af-bbf7d6ed140d",
  "type": "user",
  "uuid": "9a4b5ee5-c670-4f43-8250-e81b4f3b40ef",
  "toolUseResult": {
    "query": "Perception-R1 visual perception reward multimodal math reasoning 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01G5ZmGywmZ84AT4LvnpoE1B",
        "content": [
          {
            "title": "Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward",
            "url": "https://arxiv.org/html/2506.07218v2"
          },
          {
            "title": "Enhancing MLLM Reasoning with Visual Rewards",
            "url": "https://www.emergentmind.com/papers/2506.07218"
          },
          {
            "title": "Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward [Quick Review]",
            "url": "https://liner.com/review/perceptionr1-advancing-multimodal-reasoning-capabilities-of-mllms-via-visual-perception"
          },
          {
            "title": "GitHub - tongxiao2002/Perception-R1: The official repo of paper: \"Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward\"",
            "url": "https://github.com/tongxiao2002/Perception-R1"
          },
          {
            "title": "Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward | OpenReview",
            "url": "https://openreview.net/forum?id=KttCXdjj4w"
          },
          {
            "title": "[2506.07218] Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward",
            "url": "https://arxiv.org/abs/2506.07218"
          },
          {
            "title": "Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward",
            "url": "https://arxiv.org/pdf/2506.07218"
          }
        ]
      },
      "Based on the search results, here's what I found about Perception-R1:\n\n## Overview\n\nPerception-R1 introduces a novel visual perception reward that explicitly encourages MLLMs to perceive the visual content accurately, thereby effectively incentivizing both their multimodal perception and reasoning capabilities.\n\n## Key Problem Addressed\n\nPrevious works largely overlook the enhancement of multimodal perception capabilities in MLLMs, which serve as a core prerequisite and foundational component of complex multimodal reasoning, and existing RLVR methods fail to effectively enhance the multimodal perception capabilities of MLLMs.\n\n## Methodology\n\nThe approach collects textual visual annotations from CoT trajectories of multimodal problems as visual references for reward assignment, and during RLVR training, employs a judging LLM to assess the consistency between visual annotations and MLLM responses, assigning the visual perception reward based on consistency judgments.\n\n## Performance Results\n\nPerception-R1-7B achieves 74.2 on MathVista testmini, 54.3 on MathVerse testmini, and 72.0 on WeMath testmini, which are generally higher than the best open-source reasoning MLLMs like SophiaVL-R1-7B and Vision-R1-7B.\n\nExtensive experiments on several multimodal math and general benchmarks demonstrate the effectiveness of Perception-R1, which achieves superior performance on all benchmarks using only 1,442 training data."
    ],
    "durationSeconds": 7.984018945,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "ce810311-9f24-4bcd-b31d-df0662c1aae0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5facff83-0af4-48a3-a612-caaf81c1db1b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-27T09:09:34.776Z_

<details><summary>↩ Tool result · `toolu_01DkgaAcpiYecCPsxKG4qkZE`</summary>

```text
Web search results for query: "CogFlow perception reasoning knowledge internalization visual math 2026"

Links: [{"title":"\\textsc{CogFlow}: Bridging Perception and Reasoning through Knowledge Internalization for Visual Mathematical Problem Solving","url":"https://shchen233.github.io/cogflow/"},{"title":"[2601.01874] CogFlow: Bridging Perception and Reasoning through Knowledge Internalization for Visual Mathematical Problem Solving","url":"https://arxiv.org/abs/2601.01874"},{"title":"CogFlow: Bridging Perception and Reasoning through Knowledge Internalization for Visual Mathematical Problem Solving | OpenReview","url":"https://openreview.net/forum?id=sZ0DsaRsd4"},{"title":"[Quick Review] CogFlow: Bridging Perception and Reasoning through Knowledge Internalization for Visual Mathematical Problem Solving","url":"https://liner.com/review/cogflow-bridging-perception-and-reasoning-through-knowledge-internalization-for-visual"},{"title":"COGFLOW: BRIDGING PERCEPTION AND REASONING","url":"https://openreview.net/pdf/5fb3a4bf11affd8ee673222cabb77c59e0ab0491.pdf"},{"title":"CogFlow: Bridging Perception and Reasoning through Knowledge Internalization for Visual Mathematical Problem Solving","url":"https://arxiv.org/html/2601.01874"},{"title":"CogFlow: Bridging Perception and Reasoning through Knowledge Internalization for Visual Mathematical Problem Solving","url":"https://www.researchgate.net/publication/399478031_CogFlow_Bridging_Perception_and_Reasoning_through_Knowledge_Internalization_for_Visual_Mathematical_Problem_Solving"},{"title":"[Literature Review] CogFlow: Bridging Perception and Reasoning through Knowledge Internalization for Visual Mathematical Problem Solving","url":"https://www.themoonlight.io/en/review/cogflow-bridging-perception-and-reasoning-through-knowledge-internalization-for-visual-mathematical-problem-solving"},{"title":"Preprint COGFLOW: BRIDGING PERCEPTION AND REASONING","url":"https://arxiv.org/pdf/2601.01874"}]

Based on the search results, here's information about CogFlow:

## Overview

CogFlow is a novel cognitive-inspired three-stage framework that incorporates a knowledge internalization stage, explicitly simulating the hierarchical flow of human reasoning: perception→internalization→reasoning. The paper was published at The Fourteenth International Conference on Learning Representations in 2026.

## Problem It Addresses

Despite significant progress, multimodal large language models continue to struggle with visual mathematical problem solving. Some recent works recognize that visual perception is a bottleneck in visual mathematical reasoning, but their solutions are limited to improving the extraction and interpretation of visual inputs. Notably, they all ignore the key issue of whether the extracted visual cues are faithfully integrated and properly utilized in subsequent reasoning.

## Key Components

The framework devises Synergistic Visual Rewards to boost perception capabilities in parametric and semantic spaces, jointly improving visual information extraction from symbols and diagrams. To guarantee faithful integration of extracted visual cues into subsequent reasoning, it introduces a Knowledge Internalization Reward model in the internalization stage, bridging perception and reasoning. It also designs a Visual-Gated Policy Optimization algorithm to further enforce the reasoning is grounded with the visual knowledge, preventing models seeking shortcuts that appear coherent but are visually ungrounded reasoning chains.

## Dataset and Validation

The authors contribute a new dataset MathCog for model training, which contains samples with over 120K high-quality perception-reasoning aligned annotations. Comprehensive experiments and analysis on commonly used visual mathematical reasoning benchmarks validate the superiority of the proposed CogFlow.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4b75a1b6-e49e-411c-800b-bd706eddbe62",
  "isSidechain": false,
  "promptId": "d0596239-f589-4752-b6af-bbf7d6ed140d",
  "type": "user",
  "uuid": "a3974724-a0b1-4e23-b3c5-69bb52bfcf64",
  "toolUseResult": {
    "query": "CogFlow perception reasoning knowledge internalization visual math 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_0194PrHBtxJdCoDeBAZAWndw",
        "content": [
          {
            "title": "\\textsc{CogFlow}: Bridging Perception and Reasoning through Knowledge Internalization for Visual Mathematical Problem Solving",
            "url": "https://shchen233.github.io/cogflow/"
          },
          {
            "title": "[2601.01874] CogFlow: Bridging Perception and Reasoning through Knowledge Internalization for Visual Mathematical Problem Solving",
            "url": "https://arxiv.org/abs/2601.01874"
          },
          {
            "title": "CogFlow: Bridging Perception and Reasoning through Knowledge Internalization for Visual Mathematical Problem Solving | OpenReview",
            "url": "https://openreview.net/forum?id=sZ0DsaRsd4"
          },
          {
            "title": "[Quick Review] CogFlow: Bridging Perception and Reasoning through Knowledge Internalization for Visual Mathematical Problem Solving",
            "url": "https://liner.com/review/cogflow-bridging-perception-and-reasoning-through-knowledge-internalization-for-visual"
          },
          {
            "title": "COGFLOW: BRIDGING PERCEPTION AND REASONING",
            "url": "https://openreview.net/pdf/5fb3a4bf11affd8ee673222cabb77c59e0ab0491.pdf"
          },
          {
            "title": "CogFlow: Bridging Perception and Reasoning through Knowledge Internalization for Visual Mathematical Problem Solving",
            "url": "https://arxiv.org/html/2601.01874"
          },
          {
            "title": "CogFlow: Bridging Perception and Reasoning through Knowledge Internalization for Visual Mathematical Problem Solving",
            "url": "https://www.researchgate.net/publication/399478031_CogFlow_Bridging_Perception_and_Reasoning_through_Knowledge_Internalization_for_Visual_Mathematical_Problem_Solving"
          },
          {
            "title": "[Literature Review] CogFlow: Bridging Perception and Reasoning through Knowledge Internalization for Visual Mathematical Problem Solving",
            "url": "https://www.themoonlight.io/en/review/cogflow-bridging-perception-and-reasoning-through-knowledge-internalization-for-visual-mathematical-problem-solving"
          },
          {
            "title": "Preprint COGFLOW: BRIDGING PERCEPTION AND REASONING",
            "url": "https://arxiv.org/pdf/2601.01874"
          }
        ]
      },
      "Based on the search results, here's information about CogFlow:\n\n## Overview\n\nCogFlow is a novel cognitive-inspired three-stage framework that incorporates a knowledge internalization stage, explicitly simulating the hierarchical flow of human reasoning: perception→internalization→reasoning. The paper was published at The Fourteenth International Conference on Learning Representations in 2026.\n\n## Problem It Addresses\n\nDespite significant progress, multimodal large language models continue to struggle with visual mathematical problem solving. Some recent works recognize that visual perception is a bottleneck in visual mathematical reasoning, but their solutions are limited to improving the extraction and interpretation of visual inputs. Notably, they all ignore the key issue of whether the extracted visual cues are faithfully integrated and properly utilized in subsequent reasoning.\n\n## Key Components\n\nThe framework devises Synergistic Visual Rewards to boost perception capabilities in parametric and semantic spaces, jointly improving visual information extraction from symbols and diagrams. To guarantee faithful integration of extracted visual cues into subsequent reasoning, it introduces a Knowledge Internalization Reward model in the internalization stage, bridging perception and reasoning. It also designs a Visual-Gated Policy Optimization algorithm to further enforce the reasoning is grounded with the visual knowledge, preventing models seeking shortcuts that appear coherent but are visually ungrounded reasoning chains.\n\n## Dataset and Validation\n\nThe authors contribute a new dataset MathCog for model training, which contains samples with over 120K high-quality perception-reasoning aligned annotations. Comprehensive experiments and analysis on commonly used visual mathematical reasoning benchmarks validate the superiority of the proposed CogFlow."
    ],
    "durationSeconds": 7.016728329000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "4b75a1b6-e49e-411c-800b-bd706eddbe62",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5facff83-0af4-48a3-a612-caaf81c1db1b",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Axiom-Grounded Self-Verified Perception for Visual Math Reasoning  ## Core Problem and Thesis  Current multimoda…",
  "leafUuid": "a3974724-a0b1-4e23-b3c5-69bb52bfcf64",
  "sessionId": "5facff83-0af4-48a3-a612-caaf81c1db1b"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Axiom-grounded self-verified perception for math reasoning",
  "sessionId": "5facff83-0af4-48a3-a612-caaf81c1db1b"
}
```

---

### Tool result

_source line 23 · 2026-05-27T09:09:35.033Z_

<details><summary>↩ Tool result · `toolu_01K61RwH6DVQo5tgxH4nVbwv`</summary>

```text
Web search results for query: "EVPV visual premise verification VLM reward model 2026"

Links: [{"title":"[2603.16253] Grounding the Score: Explicit Visual Premise Verification for Reliable Vision-Language Process Reward Models","url":"https://arxiv.org/abs/2603.16253"},{"title":"Grounding the Score: Explicit Visual Premise Verification for Reliable VLM Process Reward Models","url":"https://arxiv.org/html/2603.16253"},{"title":"Grounding the Score: Explicit Visual Premise Verification for Reliable Vision-Language Process Reward Models","url":"https://arxiv.org/pdf/2603.16253"},{"title":"GitHub - Qwen-Applications/EVPV-PRM · GitHub","url":"https://github.com/Qwen-Applications/EVPV-PRM"},{"title":"Self-Rewarding Vision-Language Model via Reasoning Decomposition","url":"https://arxiv.org/pdf/2508.19652"}]

Based on the search results, here's what I found about EVPV:

EVPV (Explicit Visual Premise Verification) is a lightweight verification interface that conditions step scoring on the reliability of the visual premises a step depends on.

The policy is prompted to produce a step-wise visual checklist that makes required visual facts explicit, while a constraint extractor independently derives structured visual constraints from the input image. EVPV matches checklist claims against these constraints to compute a scalar visual reliability signal, and calibrates PRM step rewards via reliability gating: rewards for visually dependent steps are attenuated when reliability is low and preserved when reliability is high.

The approach addresses systematic false positives (rewarding hallucinated visual premises) and false negatives (penalizing correct grounded statements) that undermine both reranking and error localization.

Experiments on VisualProcessBench and six multimodal reasoning benchmarks show that EVPV improves step-level verification and consistently boosts Best-of-N reranking accuracy over strong baselines.

The paper was published on arXiv in March 2026 and is authored by researchers from Alibaba's Qwen Large Model Application Team and other institutions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "727c6f53-318b-4481-9e58-b96150c7d1f5",
  "isSidechain": false,
  "promptId": "d0596239-f589-4752-b6af-bbf7d6ed140d",
  "type": "user",
  "uuid": "64c80593-adcb-4844-a387-2e74ca0fe7b3",
  "toolUseResult": {
    "query": "EVPV visual premise verification VLM reward model 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01177gkWyZnJoWiAczMReJAS",
        "content": [
          {
            "title": "[2603.16253] Grounding the Score: Explicit Visual Premise Verification for Reliable Vision-Language Process Reward Models",
            "url": "https://arxiv.org/abs/2603.16253"
          },
          {
            "title": "Grounding the Score: Explicit Visual Premise Verification for Reliable VLM Process Reward Models",
            "url": "https://arxiv.org/html/2603.16253"
          },
          {
            "title": "Grounding the Score: Explicit Visual Premise Verification for Reliable Vision-Language Process Reward Models",
            "url": "https://arxiv.org/pdf/2603.16253"
          },
          {
            "title": "GitHub - Qwen-Applications/EVPV-PRM · GitHub",
            "url": "https://github.com/Qwen-Applications/EVPV-PRM"
          },
          {
            "title": "Self-Rewarding Vision-Language Model via Reasoning Decomposition",
            "url": "https://arxiv.org/pdf/2508.19652"
          }
        ]
      },
      "Based on the search results, here's what I found about EVPV:\n\nEVPV (Explicit Visual Premise Verification) is a lightweight verification interface that conditions step scoring on the reliability of the visual premises a step depends on.\n\nThe policy is prompted to produce a step-wise visual checklist that makes required visual facts explicit, while a constraint extractor independently derives structured visual constraints from the input image. EVPV matches checklist claims against these constraints to compute a scalar visual reliability signal, and calibrates PRM step rewards via reliability gating: rewards for visually dependent steps are attenuated when reliability is low and preserved when reliability is high.\n\nThe approach addresses systematic false positives (rewarding hallucinated visual premises) and false negatives (penalizing correct grounded statements) that undermine both reranking and error localization.\n\nExperiments on VisualProcessBench and six multimodal reasoning benchmarks show that EVPV improves step-level verification and consistently boosts Best-of-N reranking accuracy over strong baselines.\n\nThe paper was published on arXiv in March 2026 and is authored by researchers from Alibaba's Qwen Large Model Application Team and other institutions."
    ],
    "durationSeconds": 7.781056833999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "727c6f53-318b-4481-9e58-b96150c7d1f5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5facff83-0af4-48a3-a612-caaf81c1db1b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-27T09:09:38.031Z_

<details><summary>↩ Tool result · `toolu_01HSfM4vSWQtvyNR6XTGfcpU`</summary>

```text
Web search results for query: "axiom consistency constraint satisfaction visual perception math diagram reasoning 2025 2026"

Links: [{"title":"A Constraint Satisfaction Framework for Executing Perceptions and   Actions in Diagrammatic Reasoning","url":"https://arxiv.org/pdf/1401.3854"},{"title":"Math Blind: Failures in Diagram Understanding Undermine Reasoning in MLLMs","url":"https://arxiv.org/pdf/2503.20745"},{"title":"Figure It Out: Improve the Frontier of Reasoning with Executable Visual States","url":"https://arxiv.org/pdf/2512.24297"},{"title":"MathSticks: A Benchmark for Visual Symbolic Compositional Reasoning with Matchstick Puzzles","url":"https://arxiv.org/pdf/2510.00483"},{"title":"Learning to Solve Constraint Satisfaction Problems with Recurrent   Transformer","url":"https://arxiv.org/pdf/2307.04895"}]

I found relevant research on the intersection of these topics. Here are the key findings:

## Recent Research (2025-2026)

FIGR is a recent approach that integrates executable visual construction into multi-turn reasoning, generating executable code that constructs diagrams within the reasoning loop rather than relying solely on textual chains of thought. This method improved the base model by 13.12% on AIME 2025 and 11.00% on BeyondAIME.

While text-based reasoning struggles to capture structural constraints in complex settings, adaptive reward mechanisms can selectively regulate when visual construction is invoked, enabling more consistent reasoning over latent global properties that are difficult to infer from text alone.

## Visual Perception and Math Diagram Understanding

Current multimodal language models face considerable challenges in accurately interpreting mathematical diagrams, which are abstract visual representations with precise geometric structures and symbolic notations that require genuine visual interpretation rather than pattern recognition.

## Constraint-Based Approaches

Visual Symbolic Compositional Reasoning (VSCR) unifies visual perception with symbolic manipulation, requiring models to recognize structured elements, plan transformations under explicit constraints, and verify arithmetic consistency.

Recurrent Transformers can be applied to visual constraint reasoning problems while successfully addressing symbol grounding, achieving 93.5% test accuracy on visual Sudoku problems.

The research shows an emerging focus on combining visual perception, constraint satisfaction, and formal reasoning for improved mathematical problem-solving.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d37dcc43-3eaf-4acf-a6ac-0e66594a2d70",
  "isSidechain": false,
  "promptId": "d0596239-f589-4752-b6af-bbf7d6ed140d",
  "type": "user",
  "uuid": "b3a85442-b124-44cd-9515-6bd0849393c3",
  "toolUseResult": {
    "query": "axiom consistency constraint satisfaction visual perception math diagram reasoning 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_012mXw99bzQ3eSq97bSzevVU",
        "content": [
          {
            "title": "A Constraint Satisfaction Framework for Executing Perceptions and   Actions in Diagrammatic Reasoning",
            "url": "https://arxiv.org/pdf/1401.3854"
          },
          {
            "title": "Math Blind: Failures in Diagram Understanding Undermine Reasoning in MLLMs",
            "url": "https://arxiv.org/pdf/2503.20745"
          },
          {
            "title": "Figure It Out: Improve the Frontier of Reasoning with Executable Visual States",
            "url": "https://arxiv.org/pdf/2512.24297"
          },
          {
            "title": "MathSticks: A Benchmark for Visual Symbolic Compositional Reasoning with Matchstick Puzzles",
            "url": "https://arxiv.org/pdf/2510.00483"
          },
          {
            "title": "Learning to Solve Constraint Satisfaction Problems with Recurrent   Transformer",
            "url": "https://arxiv.org/pdf/2307.04895"
          }
        ]
      },
      "I found relevant research on the intersection of these topics. Here are the key findings:\n\n## Recent Research (2025-2026)\n\nFIGR is a recent approach that integrates executable visual construction into multi-turn reasoning, generating executable code that constructs diagrams within the reasoning loop rather than relying solely on textual chains of thought. This method improved the base model by 13.12% on AIME 2025 and 11.00% on BeyondAIME.\n\nWhile text-based reasoning struggles to capture structural constraints in complex settings, adaptive reward mechanisms can selectively regulate when visual construction is invoked, enabling more consistent reasoning over latent global properties that are difficult to infer from text alone.\n\n## Visual Perception and Math Diagram Understanding\n\nCurrent multimodal language models face considerable challenges in accurately interpreting mathematical diagrams, which are abstract visual representations with precise geometric structures and symbolic notations that require genuine visual interpretation rather than pattern recognition.\n\n## Constraint-Based Approaches\n\nVisual Symbolic Compositional Reasoning (VSCR) unifies visual perception with symbolic manipulation, requiring models to recognize structured elements, plan transformations under explicit constraints, and verify arithmetic consistency.\n\nRecurrent Transformers can be applied to visual constraint reasoning problems while successfully addressing symbol grounding, achieving 93.5% test accuracy on visual Sudoku problems.\n\nThe research shows an emerging focus on combining visual perception, constraint satisfaction, and formal reasoning for improved mathematical problem-solving."
    ],
    "durationSeconds": 9.190218229000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d37dcc43-3eaf-4acf-a6ac-0e66594a2d70",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5facff83-0af4-48a3-a612-caaf81c1db1b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-27T09:09:40.651Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I've gathered initial information. Let me do a few more targeted searches to understand the specific landscape better.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3a85442-b124-44cd-9515-6bd0849393c3",
  "isSidechain": false,
  "requestId": "req_011CbSp4o7JYQtzVJZ8Dekzq",
  "type": "assistant",
  "uuid": "f87a6f24-70db-4573-98c7-2f5ebfeb1e80",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5facff83-0af4-48a3-a612-caaf81c1db1b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QGdtDPEoXpw3tx8g2yTehG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3750,
      "cache_read_input_tokens": 20648,
      "output_tokens": 294,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3750,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 294,
          "cache_read_input_tokens": 20648,
          "cache_creation_input_tokens": 3750,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3750
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

_source line 26 · 2026-05-27T09:09:41.547Z_

Let me do additional targeted searches to fill in gaps on key competing works and the specific novelty claim.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f87a6f24-70db-4573-98c7-2f5ebfeb1e80",
  "isSidechain": false,
  "requestId": "req_011CbSp4o7JYQtzVJZ8Dekzq",
  "type": "assistant",
  "uuid": "694bc565-c4ab-413a-8a81-e821a82a4839",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5facff83-0af4-48a3-a612-caaf81c1db1b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QGdtDPEoXpw3tx8g2yTehG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3750,
      "cache_read_input_tokens": 20648,
      "output_tokens": 294,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3750,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 294,
          "cache_read_input_tokens": 20648,
          "cache_creation_input_tokens": 3750,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3750
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

_source line 27 · 2026-05-27T09:09:42.479Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011cLyeizrcEXeQMfuH9mtS1`</summary>

```json
{
  "query": "PRCO observer solver perception reasoning coevolution multimodal reasoning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "694bc565-c4ab-413a-8a81-e821a82a4839",
  "isSidechain": false,
  "requestId": "req_011CbSp4o7JYQtzVJZ8Dekzq",
  "type": "assistant",
  "uuid": "5103cff7-fda1-4d4a-b88b-bcc6a7cc9a6d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5facff83-0af4-48a3-a612-caaf81c1db1b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QGdtDPEoXpw3tx8g2yTehG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3750,
      "cache_read_input_tokens": 20648,
      "output_tokens": 294,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3750,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 294,
          "cache_read_input_tokens": 20648,
          "cache_creation_input_tokens": 3750,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3750
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

_source line 28 · 2026-05-27T09:09:43.413Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UJoev6uv8cPEbzcPrb5sDa`</summary>

```json
{
  "query": "FormalGeo geometric theorem verification solver reinforcement learning FGeo-DRL 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5103cff7-fda1-4d4a-b88b-bcc6a7cc9a6d",
  "isSidechain": false,
  "requestId": "req_011CbSp4o7JYQtzVJZ8Dekzq",
  "type": "assistant",
  "uuid": "8b4c12f7-4cae-452c-95a5-08888acdf898",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5facff83-0af4-48a3-a612-caaf81c1db1b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QGdtDPEoXpw3tx8g2yTehG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3750,
      "cache_read_input_tokens": 20648,
      "output_tokens": 294,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3750,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 294,
          "cache_read_input_tokens": 20648,
          "cache_creation_input_tokens": 3750,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3750
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

_source line 29 · 2026-05-27T09:09:44.365Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Pc6nRs3TTDAS3a4kdoDruV`</summary>

```json
{
  "query": "self-supervised reward signal visual math reasoning RLVR annotation-free 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b4c12f7-4cae-452c-95a5-08888acdf898",
  "isSidechain": false,
  "requestId": "req_011CbSp4o7JYQtzVJZ8Dekzq",
  "type": "assistant",
  "uuid": "4b0c6b4a-f6b8-49e5-94af-85a14ed7e713",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5facff83-0af4-48a3-a612-caaf81c1db1b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QGdtDPEoXpw3tx8g2yTehG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3750,
      "cache_read_input_tokens": 20648,
      "output_tokens": 294,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3750,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 294,
          "cache_read_input_tokens": 20648,
          "cache_creation_input_tokens": 3750,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3750
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

_source line 30 · 2026-05-27T09:09:45.056Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01R5EczcJuVNmwhaZLcmkTGe`</summary>

```json
{
  "query": "PEARL perceptual evidence anchored reinforced learning multimodal reasoning MathVerse 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b0c6b4a-f6b8-49e5-94af-85a14ed7e713",
  "isSidechain": false,
  "requestId": "req_011CbSp4o7JYQtzVJZ8Dekzq",
  "type": "assistant",
  "uuid": "2cfed78e-412e-44ce-9cbb-a6d4fb6d8dbf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5facff83-0af4-48a3-a612-caaf81c1db1b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QGdtDPEoXpw3tx8g2yTehG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3750,
      "cache_read_input_tokens": 20648,
      "output_tokens": 294,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3750,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 294,
          "cache_read_input_tokens": 20648,
          "cache_creation_input_tokens": 3750,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3750
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

_source line 31 · 2026-05-27T09:09:49.352Z_

<details><summary>↩ Tool result · `toolu_011cLyeizrcEXeQMfuH9mtS1`</summary>

```text
Web search results for query: "PRCO observer solver perception reasoning coevolution multimodal reasoning 2026"

Links: [{"title":"[2603.28618] Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning","url":"https://arxiv.org/abs/2603.28618"},{"title":"GitHub - Dtc7w3PQ/PRCO: Official implementation of Seeing with You: Perception-Reasoning Co-evolution for Multimodal Reasoning. · GitHub","url":"https://github.com/Dtc7w3PQ/PRCO"},{"title":"Seeing with You: Perception–Reasoning Coevolution for Multimodal Reasoning","url":"https://arxiv.org/html/2603.28618v1"},{"title":"Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning","url":"https://chatpaper.com/paper/262369"},{"title":"Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning","url":"https://arxiv.org/pdf/2603.28618"},{"title":"Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning | Takara TLDR","url":"https://tldr.takara.ai/p/2603.28618"},{"title":"Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning | Request PDF","url":"https://www.researchgate.net/publication/403307388_Seeing_with_You_Perception-Reasoning_Coevolution_for_Multimodal_Reasoning"}]

Based on the search results, here's what I found about PRCO:

## Overview

PRCO (Perception-Reasoning Coevolution) is a dual-role RLVR (reinforcement learning with verifiable rewards) framework with a shared policy that consists of two cooperative roles: an Observer that generates an evidence caption tailored to the question and a Solver that predicts the final answer based on this caption.

## Key Innovation

Existing RLVR approaches typically rely on outcome-driven optimization that updates both perception and reasoning using a shared reward based solely on the final answer, which blurs credit assignment and frequently improves reasoning patterns while failing to reliably enhance the accuracy of upstream visual evidence extraction. PRCO addresses this by employing role-specific reward signals: the Solver is optimized using verifiable outcome rewards on the final answer, while the Observer receives a utility reward derived from the Solver's downstream success.

## Results

Extensive experiments across eight challenging multimodal reasoning benchmarks demonstrate that PRCO yields consistent improvements across model scales by over 7 points on average accuracy compared to the base model, outperforming prior open-source RL-tuned baselines.

## CoEvolution Process

PRCO drives coevolution, in which the Observer progressively improves question-grounded visual perception by extracting and articulating question-relevant evidence, while the Solver learns to reason more reliably under explicit evidence guidance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5103cff7-fda1-4d4a-b88b-bcc6a7cc9a6d",
  "isSidechain": false,
  "promptId": "d0596239-f589-4752-b6af-bbf7d6ed140d",
  "type": "user",
  "uuid": "7503e964-38e1-479c-8ce0-3332289d1cd7",
  "toolUseResult": {
    "query": "PRCO observer solver perception reasoning coevolution multimodal reasoning 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_018w9FPStkpuUcAd3vQ24age",
        "content": [
          {
            "title": "[2603.28618] Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning",
            "url": "https://arxiv.org/abs/2603.28618"
          },
          {
            "title": "GitHub - Dtc7w3PQ/PRCO: Official implementation of Seeing with You: Perception-Reasoning Co-evolution for Multimodal Reasoning. · GitHub",
            "url": "https://github.com/Dtc7w3PQ/PRCO"
          },
          {
            "title": "Seeing with You: Perception–Reasoning Coevolution for Multimodal Reasoning",
            "url": "https://arxiv.org/html/2603.28618v1"
          },
          {
            "title": "Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning",
            "url": "https://chatpaper.com/paper/262369"
          },
          {
            "title": "Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning",
            "url": "https://arxiv.org/pdf/2603.28618"
          },
          {
            "title": "Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning | Takara TLDR",
            "url": "https://tldr.takara.ai/p/2603.28618"
          },
          {
            "title": "Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning | Request PDF",
            "url": "https://www.researchgate.net/publication/403307388_Seeing_with_You_Perception-Reasoning_Coevolution_for_Multimodal_Reasoning"
          }
        ]
      },
      "Based on the search results, here's what I found about PRCO:\n\n## Overview\n\nPRCO (Perception-Reasoning Coevolution) is a dual-role RLVR (reinforcement learning with verifiable rewards) framework with a shared policy that consists of two cooperative roles: an Observer that generates an evidence caption tailored to the question and a Solver that predicts the final answer based on this caption.\n\n## Key Innovation\n\nExisting RLVR approaches typically rely on outcome-driven optimization that updates both perception and reasoning using a shared reward based solely on the final answer, which blurs credit assignment and frequently improves reasoning patterns while failing to reliably enhance the accuracy of upstream visual evidence extraction. PRCO addresses this by employing role-specific reward signals: the Solver is optimized using verifiable outcome rewards on the final answer, while the Observer receives a utility reward derived from the Solver's downstream success.\n\n## Results\n\nExtensive experiments across eight challenging multimodal reasoning benchmarks demonstrate that PRCO yields consistent improvements across model scales by over 7 points on average accuracy compared to the base model, outperforming prior open-source RL-tuned baselines.\n\n## CoEvolution Process\n\nPRCO drives coevolution, in which the Observer progressively improves question-grounded visual perception by extracting and articulating question-relevant evidence, while the Solver learns to reason more reliably under explicit evidence guidance."
    ],
    "durationSeconds": 6.867695597000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "5103cff7-fda1-4d4a-b88b-bcc6a7cc9a6d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5facff83-0af4-48a3-a612-caaf81c1db1b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-27T09:09:51.286Z_

<details><summary>↩ Tool result · `toolu_01UJoev6uv8cPEbzcPrb5sDa`</summary>

```text
Web search results for query: "FormalGeo geometric theorem verification solver reinforcement learning FGeo-DRL 2024"

Links: [{"title":"FGeo-DRL: Deductive Reasoning for Geometric Problems through Deep Reinforcement Learning","url":"https://www.mdpi.com/2073-8994/16/4/437"},{"title":"(PDF) FGeo-DRL: Deductive Reasoning for Geometric Problems through Deep Reinforcement Learning","url":"https://www.researchgate.net/publication/379613284_FGeo-DRL_Deductive_Reasoning_for_Geometric_Problems_through_Deep_Reinforcement_Learning"},{"title":"[2402.09051] FGeo-DRL: Deductive Reasoning for Geometric Problems through Deep Reinforcement Learning","url":"https://arxiv.org/abs/2402.09051"},{"title":"FormalGeo: Formal representation and solving for Euclidean plane geometry problems","url":"https://formalgeo.github.io/"},{"title":"(PDF) FGeo-TP: A Language Model-Enhanced Solver for Euclidean Geometry Problems","url":"https://www.researchgate.net/publication/379563827_FGeo-TP_A_Language_Model-Enhanced_Solver_for_Euclidean_Geometry_Problems"},{"title":"FGeo-HyperGNet: Geometric Problem Solving Integrating FormalGeo Symbolic System and Hypergraph Neural Network","url":"https://arxiv.org/html/2402.11461"},{"title":"FGeo-DRL: Deductive Reasoning for Geometric Problems through Deep   Reinforcement Learning","url":"https://arxiv.org/pdf/2402.09051"},{"title":"FGeo-DRL:Deductive Reasoning for Geometric Problems through Deep Reinforcement Learning","url":"https://arxiv.org/html/2402.09051v1"},{"title":"GitHub - majianz/dl4gps: [ACL 2026 Main Conference] Paper list for the survey \"A Survey of Deep Learning for Geometry Problem Solving\" · GitHub","url":"https://github.com/majianz/dl4gps"},{"title":"FGeo-TP: A Language Model-Enhanced Solver for Euclidean Geometry Problems","url":"https://www.mdpi.com/2073-8994/16/4/421"}]

I found comprehensive information about FGeo-DRL and related research. Here's what the search reveals:

## FGeo-DRL Overview

FGeo-DRL is a neural-symbolic system built to automatically perform human-like geometric deductive reasoning. The paper was published on April 5, 2024 in the journal Symmetry.

## System Architecture

The neural part is an AI agent based on deep reinforcement learning, capable of autonomously learning problem-solving methods from the feedback of a formalized environment, leveraging a pre-trained natural language model to establish a policy network for theorem selection and employing Monte Carlo Tree Search for heuristic exploration.

The symbolic part is a reinforcement learning environment based on geometry formalization theory and FormalGeo, which models geometric problem solving as a Markov Decision Process. The known conditions and objectives of the problem form the state space, while the set of theorems forms the action space.

## Performance Results

Experiments conducted on the formalgeo7k dataset achieved a problem-solving success rate of 86.40%.

## Related Work

The researchers established a geometric formalized system known as FormalGeo and annotated approximately 7000 geometric problems, forming the FormalGeo7k dataset. This system enables readable and verifiable automated solutions to geometric problems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8b4c12f7-4cae-452c-95a5-08888acdf898",
  "isSidechain": false,
  "promptId": "d0596239-f589-4752-b6af-bbf7d6ed140d",
  "type": "user",
  "uuid": "82d31284-0bfe-412a-9359-3f5fd9734a1d",
  "toolUseResult": {
    "query": "FormalGeo geometric theorem verification solver reinforcement learning FGeo-DRL 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_01AAZ2naZptknisidpTmGQ3D",
        "content": [
          {
            "title": "FGeo-DRL: Deductive Reasoning for Geometric Problems through Deep Reinforcement Learning",
            "url": "https://www.mdpi.com/2073-8994/16/4/437"
          },
          {
            "title": "(PDF) FGeo-DRL: Deductive Reasoning for Geometric Problems through Deep Reinforcement Learning",
            "url": "https://www.researchgate.net/publication/379613284_FGeo-DRL_Deductive_Reasoning_for_Geometric_Problems_through_Deep_Reinforcement_Learning"
          },
          {
            "title": "[2402.09051] FGeo-DRL: Deductive Reasoning for Geometric Problems through Deep Reinforcement Learning",
            "url": "https://arxiv.org/abs/2402.09051"
          },
          {
            "title": "FormalGeo: Formal representation and solving for Euclidean plane geometry problems",
            "url": "https://formalgeo.github.io/"
          },
          {
            "title": "(PDF) FGeo-TP: A Language Model-Enhanced Solver for Euclidean Geometry Problems",
            "url": "https://www.researchgate.net/publication/379563827_FGeo-TP_A_Language_Model-Enhanced_Solver_for_Euclidean_Geometry_Problems"
          },
          {
            "title": "FGeo-HyperGNet: Geometric Problem Solving Integrating FormalGeo Symbolic System and Hypergraph Neural Network",
            "url": "https://arxiv.org/html/2402.11461"
          },
          {
            "title": "FGeo-DRL: Deductive Reasoning for Geometric Problems through Deep   Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2402.09051"
          },
          {
            "title": "FGeo-DRL:Deductive Reasoning for Geometric Problems through Deep Reinforcement Learning",
            "url": "https://arxiv.org/html/2402.09051v1"
          },
          {
            "title": "GitHub - majianz/dl4gps: [ACL 2026 Main Conference] Paper list for the survey \"A Survey of Deep Learning for Geometry Problem Solving\" · GitHub",
            "url": "https://github.com/majianz/dl4gps"
          },
          {
            "title": "FGeo-TP: A Language Model-Enhanced Solver for Euclidean Geometry Problems",
            "url": "https://www.mdpi.com/2073-8994/16/4/421"
          }
        ]
      },
      "I found comprehensive information about FGeo-DRL and related research. Here's what the search reveals:\n\n## FGeo-DRL Overview\n\nFGeo-DRL is a neural-symbolic system built to automatically perform human-like geometric deductive reasoning. The paper was published on April 5, 2024 in the journal Symmetry.\n\n## System Architecture\n\nThe neural part is an AI agent based on deep reinforcement learning, capable of autonomously learning problem-solving methods from the feedback of a formalized environment, leveraging a pre-trained natural language model to establish a policy network for theorem selection and employing Monte Carlo Tree Search for heuristic exploration.\n\nThe symbolic part is a reinforcement learning environment based on geometry formalization theory and FormalGeo, which models geometric problem solving as a Markov Decision Process. The known conditions and objectives of the problem form the state space, while the set of theorems forms the action space.\n\n## Performance Results\n\nExperiments conducted on the formalgeo7k dataset achieved a problem-solving success rate of 86.40%.\n\n## Related Work\n\nThe researchers established a geometric formalized system known as FormalGeo and annotated approximately 7000 geometric problems, forming the FormalGeo7k dataset. This system enables readable and verifiable automated solutions to geometric problems."
    ],
    "durationSeconds": 7.8691732870000015,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "8b4c12f7-4cae-452c-95a5-08888acdf898",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5facff83-0af4-48a3-a612-caaf81c1db1b",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Axiom-Grounded Self-Verified Perception for Visual Math Reasoning  ## Core Problem and Thesis  Current multimoda…",
  "leafUuid": "82d31284-0bfe-412a-9359-3f5fd9734a1d",
  "sessionId": "5facff83-0af4-48a3-a612-caaf81c1db1b"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Axiom-grounded self-verified perception for math reasoning",
  "sessionId": "5facff83-0af4-48a3-a612-caaf81c1db1b"
}
```

---

### Tool result

_source line 35 · 2026-05-27T09:09:52.110Z_

<details><summary>↩ Tool result · `toolu_01R5EczcJuVNmwhaZLcmkTGe`</summary>

```text
Web search results for query: "PEARL perceptual evidence anchored reinforced learning multimodal reasoning MathVerse 2025"

Links: [{"title":"[2511.18437] Perceptual-Evidence Anchored Reinforced Learning for Multimodal Reasoning","url":"https://arxiv.org/abs/2511.18437"},{"title":"Perceptual-Evidence Anchored Reinforced Learning for Multimodal Reasoning","url":"https://arxiv.org/pdf/2511.18437"},{"title":"Perceptual-Evidence Anchored Reinforced Learning for Multimodal Reasoning","url":"https://arxiv.org/html/2511.18437"},{"title":"Seeing with You: Perception–Reasoning Coevolution for Multimodal Reasoning","url":"https://arxiv.org/html/2603.28618v1"},{"title":"GitHub - MiliLab/PEARL: Official repository for [CVPR 2026] \"Perceptual-Evidence Anchored Reinforced Learning for Multimodal Reasoning\" · GitHub","url":"https://github.com/MiliLab/PEARL"}]

Based on the search results, here's what I found:

## PEARL: Perceptual-Evidence Anchored Reinforced Learning

PEARL (Perceptual-Evidence Anchored Reinforced Learning) is a dual-branch, perception-reasoning synergistic that strengthens multimodal reasoning by explicitly anchoring it to verified visual evidence.

### How It Works

For each reasoning-oriented QA instance, PEARL derives a perception checklist—a set of perception-oriented sub-questions with verifiable answers that probe the model's understanding of key visual evidence. During training, auxiliary rollouts on this checklist yield a perceptual reward that both directly reinforces the model's perception ability and acts as a fidelity gate for reasoning. If the model passes the perception check, its policy update is biased towards evidence-anchored reasoning. Otherwise, the process is halted to prevent reasoning from flawed premises.

### Performance Results

PEARL achieves substantial gains on multimodal reasoning benchmarks, with a +9.7% improvement over the baseline and +6.6% over GRPO on MathVerse.

### Integration

PEARL can be seamlessly integrated with popular RL methods like GRPO and DAPO.

The research paper was published in November 2025 and is available on arXiv, with an official repository on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2cfed78e-412e-44ce-9cbb-a6d4fb6d8dbf",
  "isSidechain": false,
  "promptId": "d0596239-f589-4752-b6af-bbf7d6ed140d",
  "type": "user",
  "uuid": "ebe428ad-b410-469e-854f-1e7f726fb927",
  "toolUseResult": {
    "query": "PEARL perceptual evidence anchored reinforced learning multimodal reasoning MathVerse 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SvwtjwKe7M72x5hgbMpm8n",
        "content": [
          {
            "title": "[2511.18437] Perceptual-Evidence Anchored Reinforced Learning for Multimodal Reasoning",
            "url": "https://arxiv.org/abs/2511.18437"
          },
          {
            "title": "Perceptual-Evidence Anchored Reinforced Learning for Multimodal Reasoning",
            "url": "https://arxiv.org/pdf/2511.18437"
          },
          {
            "title": "Perceptual-Evidence Anchored Reinforced Learning for Multimodal Reasoning",
            "url": "https://arxiv.org/html/2511.18437"
          },
          {
            "title": "Seeing with You: Perception–Reasoning Coevolution for Multimodal Reasoning",
            "url": "https://arxiv.org/html/2603.28618v1"
          },
          {
            "title": "GitHub - MiliLab/PEARL: Official repository for [CVPR 2026] \"Perceptual-Evidence Anchored Reinforced Learning for Multimodal Reasoning\" · GitHub",
            "url": "https://github.com/MiliLab/PEARL"
          }
        ]
      },
      "Based on the search results, here's what I found:\n\n## PEARL: Perceptual-Evidence Anchored Reinforced Learning\n\nPEARL (Perceptual-Evidence Anchored Reinforced Learning) is a dual-branch, perception-reasoning synergistic that strengthens multimodal reasoning by explicitly anchoring it to verified visual evidence.\n\n### How It Works\n\nFor each reasoning-oriented QA instance, PEARL derives a perception checklist—a set of perception-oriented sub-questions with verifiable answers that probe the model's understanding of key visual evidence. During training, auxiliary rollouts on this checklist yield a perceptual reward that both directly reinforces the model's perception ability and acts as a fidelity gate for reasoning. If the model passes the perception check, its policy update is biased towards evidence-anchored reasoning. Otherwise, the process is halted to prevent reasoning from flawed premises.\n\n### Performance Results\n\nPEARL achieves substantial gains on multimodal reasoning benchmarks, with a +9.7% improvement over the baseline and +6.6% over GRPO on MathVerse.\n\n### Integration\n\nPEARL can be seamlessly integrated with popular RL methods like GRPO and DAPO.\n\nThe research paper was published in November 2025 and is available on arXiv, with an official repository on GitHub."
    ],
    "durationSeconds": 7.051402170000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "2cfed78e-412e-44ce-9cbb-a6d4fb6d8dbf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5facff83-0af4-48a3-a612-caaf81c1db1b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-27T09:09:52.679Z_

<details><summary>↩ Tool result · `toolu_01Pc6nRs3TTDAS3a4kdoDruV`</summary>

```text
Web search results for query: "self-supervised reward signal visual math reasoning RLVR annotation-free 2025 2026"

Links: [{"title":"TRAPO: A SEMI-SUPERVISED REINFORCEMENT LEARN","url":"https://openreview.net/pdf/5384951c5b51ad5525766f9dc9e5402535eb876b.pdf"},{"title":"Reinforcement Learning from Verifier Rewards","url":"https://www.emergentmind.com/topics/reinforcement-learning-from-verifier-rewards-rlvr"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2505.19590"},{"title":"RLVR Beyond Math and Code: The Verifier Problem Nobody Has Solved | Subhadip Mitra","url":"https://subhadipmitra.com/blog/2026/rlvr-beyond-math-code/"},{"title":"Masked-and-Reordered Self-Supervision for Reinforcement Learning from Verifiable Rewards","url":"https://arxiv.org/pdf/2511.17473"},{"title":"Co-rewarding: Stable Self-supervised RL for Eliciting Reasoning in Large Language Models","url":"https://arxiv.org/pdf/2508.00410"}]

Based on the search results, here's what I found regarding self-supervised reward signals, visual math reasoning, RLVR, and annotation-free approaches in 2025-2026:

## Key Findings:

**Self-Supervised Reward Signals for RLVR:**
INTUITOR guides learning through self-generated signals, eliminating the need for external supervision or handcrafted rewards. The method uses self-certainty—the average KL divergence between the model's output distribution and a uniform distribution—as a confidence measure that has proven useful for distinguishing high-quality responses from flawed ones.

**Annotation-Free Training Approaches:**
Self-rewarding methods with unlabeled data have emerged to address the bottleneck of reliance on high-quality ground-truth labels in RLVR. One prominent line of label-free methods leverages internal signals like entropy and self-certainty to strengthen model confidence in reasoning, while another seeks answer-level consensus to construct pseudo labels as reward basis.

**RLVR Performance in Math:**
RLVR demonstrates strong performance in math, with verifiable reward alone being sufficient to surface complex reasoning without explicit annotation.

**Process-Level Self-Supervision:**
MR-RLVR (Masked-and-Reordered RLVR) constructs process-level self-supervised rewards via "masked-then-fill" and "step reordering" to extract learnable signals from intermediate reasoning.

These approaches represent significant progress in developing annotation-free training methods for reasoning tasks in 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4b0c6b4a-f6b8-49e5-94af-85a14ed7e713",
  "isSidechain": false,
  "promptId": "d0596239-f589-4752-b6af-bbf7d6ed140d",
  "type": "user",
  "uuid": "4a9c6666-dbcc-4c6f-8b0d-b08ba785d96b",
  "toolUseResult": {
    "query": "self-supervised reward signal visual math reasoning RLVR annotation-free 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_016EFN9XUpHA35PyHVmfQxmG",
        "content": [
          {
            "title": "TRAPO: A SEMI-SUPERVISED REINFORCEMENT LEARN",
            "url": "https://openreview.net/pdf/5384951c5b51ad5525766f9dc9e5402535eb876b.pdf"
          },
          {
            "title": "Reinforcement Learning from Verifier Rewards",
            "url": "https://www.emergentmind.com/topics/reinforcement-learning-from-verifier-rewards-rlvr"
          },
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://arxiv.org/pdf/2505.19590"
          },
          {
            "title": "RLVR Beyond Math and Code: The Verifier Problem Nobody Has Solved | Subhadip Mitra",
            "url": "https://subhadipmitra.com/blog/2026/rlvr-beyond-math-code/"
          },
          {
            "title": "Masked-and-Reordered Self-Supervision for Reinforcement Learning from Verifiable Rewards",
            "url": "https://arxiv.org/pdf/2511.17473"
          },
          {
            "title": "Co-rewarding: Stable Self-supervised RL for Eliciting Reasoning in Large Language Models",
            "url": "https://arxiv.org/pdf/2508.00410"
          }
        ]
      },
      "Based on the search results, here's what I found regarding self-supervised reward signals, visual math reasoning, RLVR, and annotation-free approaches in 2025-2026:\n\n## Key Findings:\n\n**Self-Supervised Reward Signals for RLVR:**\nINTUITOR guides learning through self-generated signals, eliminating the need for external supervision or handcrafted rewards. The method uses self-certainty—the average KL divergence between the model's output distribution and a uniform distribution—as a confidence measure that has proven useful for distinguishing high-quality responses from flawed ones.\n\n**Annotation-Free Training Approaches:**\nSelf-rewarding methods with unlabeled data have emerged to address the bottleneck of reliance on high-quality ground-truth labels in RLVR. One prominent line of label-free methods leverages internal signals like entropy and self-certainty to strengthen model confidence in reasoning, while another seeks answer-level consensus to construct pseudo labels as reward basis.\n\n**RLVR Performance in Math:**\nRLVR demonstrates strong performance in math, with verifiable reward alone being sufficient to surface complex reasoning without explicit annotation.\n\n**Process-Level Self-Supervision:**\nMR-RLVR (Masked-and-Reordered RLVR) constructs process-level self-supervised rewards via \"masked-then-fill\" and \"step reordering\" to extract learnable signals from intermediate reasoning.\n\nThese approaches represent significant progress in developing annotation-free training methods for reasoning tasks in 2025-2026."
    ],
    "durationSeconds": 8.312106718999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "4b0c6b4a-f6b8-49e5-94af-85a14ed7e713",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5facff83-0af4-48a3-a612-caaf81c1db1b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 37 · 2026-05-27T09:09:52.683Z_

```json
{
  "parentUuid": "4a9c6666-dbcc-4c6f-8b0d-b08ba785d96b",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "57816fc5-fcaa-4f30-912a-ff967827ac84",
  "timestamp": "2026-05-27T09:09:52.683Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5facff83-0af4-48a3-a612-caaf81c1db1b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 38 · 2026-05-27T09:09:56.057Z_

<details><summary>Logged reasoning block</summary>

```text
Let me do a few more searches to check for more directly competing work — specifically on joint constraint satisfaction for perception, and on the Geoparsing work mentioned in the proposal.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "57816fc5-fcaa-4f30-912a-ff967827ac84",
  "isSidechain": false,
  "requestId": "req_011CbSp5skPDtA3cwVTYYNk1",
  "type": "assistant",
  "uuid": "bf961a16-d7cf-4317-bb52-8458efbfb757",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5facff83-0af4-48a3-a612-caaf81c1db1b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014DGGoTsa9wGcTMhchRFAe5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 622,
      "cache_creation_input_tokens": 2780,
      "cache_read_input_tokens": 24398,
      "output_tokens": 245,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2780,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 622,
          "output_tokens": 245,
          "cache_read_input_tokens": 24398,
          "cache_creation_input_tokens": 2780,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2780
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

_source line 39 · 2026-05-27T09:09:56.603Z_

Let me do a few more targeted searches to check for the most directly competing approaches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf961a16-d7cf-4317-bb52-8458efbfb757",
  "isSidechain": false,
  "requestId": "req_011CbSp5skPDtA3cwVTYYNk1",
  "type": "assistant",
  "uuid": "060fe251-4c1e-417a-bebd-e8aa2a5b9836",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5facff83-0af4-48a3-a612-caaf81c1db1b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014DGGoTsa9wGcTMhchRFAe5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 622,
      "cache_creation_input_tokens": 2780,
      "cache_read_input_tokens": 24398,
      "output_tokens": 245,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2780,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 622,
          "output_tokens": 245,
          "cache_read_input_tokens": 24398,
          "cache_creation_input_tokens": 2780,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2780
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

_source line 40 · 2026-05-27T09:09:57.546Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Y7ApwZXperZFzcxV8ioCQR`</summary>

```json
{
  "query": "Geoparsing diagram parsing plane solid geometry unified formal language 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "060fe251-4c1e-417a-bebd-e8aa2a5b9836",
  "isSidechain": false,
  "requestId": "req_011CbSp5skPDtA3cwVTYYNk1",
  "type": "assistant",
  "uuid": "988b96a3-2703-43be-b0af-c1787201af36",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5facff83-0af4-48a3-a612-caaf81c1db1b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014DGGoTsa9wGcTMhchRFAe5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 622,
      "cache_creation_input_tokens": 2780,
      "cache_read_input_tokens": 24398,
      "output_tokens": 245,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2780,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 622,
          "output_tokens": 245,
          "cache_read_input_tokens": 24398,
          "cache_creation_input_tokens": 2780,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2780
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

_source line 41 · 2026-05-27T09:09:58.088Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MWTv9F5a1cn2GLJFYq17mL`</summary>

```json
{
  "query": "SSL-R1 self-supervised visual reinforcement post-training MLLM 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "988b96a3-2703-43be-b0af-c1787201af36",
  "isSidechain": false,
  "requestId": "req_011CbSp5skPDtA3cwVTYYNk1",
  "type": "assistant",
  "uuid": "f6bf1819-7c3f-4468-849a-12b6027e7839",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5facff83-0af4-48a3-a612-caaf81c1db1b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014DGGoTsa9wGcTMhchRFAe5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 622,
      "cache_creation_input_tokens": 2780,
      "cache_read_input_tokens": 24398,
      "output_tokens": 245,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2780,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 622,
          "output_tokens": 245,
          "cache_read_input_tokens": 24398,
          "cache_creation_input_tokens": 2780,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2780
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

_source line 42 · 2026-05-27T09:09:58.780Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WRcPzmCJJziJMyyJnHBnx3`</summary>

```json
{
  "query": "V-Zero zero-shot multimodal reasoning cross-modal self-play 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6bf1819-7c3f-4468-849a-12b6027e7839",
  "isSidechain": false,
  "requestId": "req_011CbSp5skPDtA3cwVTYYNk1",
  "type": "assistant",
  "uuid": "f25e9d71-1e45-459a-9a90-773f6938169f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5facff83-0af4-48a3-a612-caaf81c1db1b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014DGGoTsa9wGcTMhchRFAe5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 622,
      "cache_creation_input_tokens": 2780,
      "cache_read_input_tokens": 24398,
      "output_tokens": 245,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2780,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 622,
          "output_tokens": 245,
          "cache_read_input_tokens": 24398,
          "cache_creation_input_tokens": 2780,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2780
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

_source line 43 · 2026-05-27T09:10:04.589Z_

<details><summary>↩ Tool result · `toolu_01Y7ApwZXperZFzcxV8ioCQR`</summary>

```text
Web search results for query: "Geoparsing diagram parsing plane solid geometry unified formal language 2026"

Links: [{"title":"[2604.11600] Geoparsing: Diagram Parsing for Plane and Solid Geometry with a Unified Formal Language","url":"https://arxiv.org/abs/2604.11600"},{"title":"Geoparsing: Diagram Parsing for Plane and Solid Geometry with a Unified Formal Language","url":"https://arxiv.org/html/2604.11600v1"},{"title":"Diagram Parsing for Plane and Solid Geometry with a Unified Formal Language | OpenReview","url":"https://openreview.net/forum?id=Jivgo2qRGI"},{"title":"FGeo-Parser: Autoformalization and Solution of Plane Geometric Problems | MDPI","url":"https://www.mdpi.com/2073-8994/17/1/8"},{"title":"The architecture of diagram parser. | Download Scientific Diagram","url":"https://www.researchgate.net/figure/The-architecture-of-diagram-parser_fig4_387376974"},{"title":"Plane Geometry Diagram Parsing","url":"https://arxiv.org/pdf/2205.09363"},{"title":"GeoSDF: Plane Geometry Diagram Synthesis via Signed Distance Field","url":"https://arxiv.org/pdf/2506.13492"}]

Based on the search results, I found information about the "Geoparsing" paper you're looking for.

## Overview

The paper addresses the challenge of geometric reasoning by designing a unified formal language that integrates plane and solid geometry, comprehensively covering geometric structures and semantic relations.

## Key Contributions

The researchers constructed GDP-29K, a large-scale dataset comprising 20k plane and 9k solid geometry samples collected from diverse real-world sources, each paired with its ground-truth formal description.

## Training Approach

To ensure syntactic correctness and geometric consistency, they propose a training paradigm that combines Supervised Fine-Tuning with Reinforcement Learning via Verifiable Rewards.

## Results and Applications

Experiments show that their approach achieves state-of-the-art parsing performance, and the parsed formal descriptions serve as a critical cognitive scaffold, significantly boosting MLLMs' capabilities for downstream geometry reasoning tasks.

The paper was authored by researchers from the Institute of Automation of the Chinese Academy of Sciences and Alibaba, and was published to arXiv in April 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "988b96a3-2703-43be-b0af-c1787201af36",
  "isSidechain": false,
  "promptId": "d0596239-f589-4752-b6af-bbf7d6ed140d",
  "type": "user",
  "uuid": "e7d34e5d-7b36-44a4-b1a1-29e249504d38",
  "toolUseResult": {
    "query": "Geoparsing diagram parsing plane solid geometry unified formal language 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01P86B4wWb24Th1a5rqFVUXU",
        "content": [
          {
            "title": "[2604.11600] Geoparsing: Diagram Parsing for Plane and Solid Geometry with a Unified Formal Language",
            "url": "https://arxiv.org/abs/2604.11600"
          },
          {
            "title": "Geoparsing: Diagram Parsing for Plane and Solid Geometry with a Unified Formal Language",
            "url": "https://arxiv.org/html/2604.11600v1"
          },
          {
            "title": "Diagram Parsing for Plane and Solid Geometry with a Unified Formal Language | OpenReview",
            "url": "https://openreview.net/forum?id=Jivgo2qRGI"
          },
          {
            "title": "FGeo-Parser: Autoformalization and Solution of Plane Geometric Problems | MDPI",
            "url": "https://www.mdpi.com/2073-8994/17/1/8"
          },
          {
            "title": "The architecture of diagram parser. | Download Scientific Diagram",
            "url": "https://www.researchgate.net/figure/The-architecture-of-diagram-parser_fig4_387376974"
          },
          {
            "title": "Plane Geometry Diagram Parsing",
            "url": "https://arxiv.org/pdf/2205.09363"
          },
          {
            "title": "GeoSDF: Plane Geometry Diagram Synthesis via Signed Distance Field",
            "url": "https://arxiv.org/pdf/2506.13492"
          }
        ]
      },
      "Based on the search results, I found information about the \"Geoparsing\" paper you're looking for.\n\n## Overview\n\nThe paper addresses the challenge of geometric reasoning by designing a unified formal language that integrates plane and solid geometry, comprehensively covering geometric structures and semantic relations.\n\n## Key Contributions\n\nThe researchers constructed GDP-29K, a large-scale dataset comprising 20k plane and 9k solid geometry samples collected from diverse real-world sources, each paired with its ground-truth formal description.\n\n## Training Approach\n\nTo ensure syntactic correctness and geometric consistency, they propose a training paradigm that combines Supervised Fine-Tuning with Reinforcement Learning via Verifiable Rewards.\n\n## Results and Applications\n\nExperiments show that their approach achieves state-of-the-art parsing performance, and the parsed formal descriptions serve as a critical cognitive scaffold, significantly boosting MLLMs' capabilities for downstream geometry reasoning tasks.\n\nThe paper was authored by researchers from the Institute of Automation of the Chinese Academy of Sciences and Alibaba, and was published to arXiv in April 2026."
    ],
    "durationSeconds": 7.037661152000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "988b96a3-2703-43be-b0af-c1787201af36",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5facff83-0af4-48a3-a612-caaf81c1db1b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-27T09:10:04.706Z_

<details><summary>↩ Tool result · `toolu_01MWTv9F5a1cn2GLJFYq17mL`</summary>

```text
Web search results for query: "SSL-R1 self-supervised visual reinforcement post-training MLLM 2026"

Links: [{"title":"SSL-R1: Self-Supervised Visual Reinforcement Post-Training for Multimodal Large Language Models","url":"https://arxiv.org/html/2604.20705"},{"title":"[2604.20705] SSL-R1: Self-Supervised Visual Reinforcement Post-Training for Multimodal Large Language Models","url":"https://arxiv.org/abs/2604.20705"},{"title":"(PDF) ViSS-R1: Self-Supervised Reinforcement Video Reasoning","url":"https://www.researchgate.net/publication/397701383_ViSS-R1_Self-Supervised_Reinforcement_Video_Reasoning"},{"title":"Visual Jigsaw Post-Training Improves MLLMs","url":"https://arxiv.org/pdf/2509.25190"},{"title":"ViSS-R1: Self-Supervised Reinforcement Video Reasoning","url":"https://arxiv.org/pdf/2511.13054"},{"title":"Visual Jigsaw Post-Training Improves MLLMs’ Visual Understanding Via Self-Supervised Ordering","url":"https://quantumzeitgeist.com/supervised-training-visual-jigsaw-post-improves-mllms-understanding-self/"},{"title":"Visual Jigsaw Post-Training Improves MLLMs","url":"https://arxiv.org/html/2509.25190"}]

Based on the search results, here's what I found about SSL-R1:

## SSL-R1: Self-Supervised Visual Reinforcement Post-Training for Multimodal Large Language Models

SSL-R1 is a generic self-supervised RL framework that derives verifiable rewards directly from images. The framework reformulates widely-used SSL tasks into a set of verifiable visual puzzles for RL post-training, requiring neither human nor external model supervision.

### Key Characteristics:

- **Problem it addresses**: The reliance on language-centric priors and expensive manual annotations prevents MLLMs' intrinsic visual understanding and scalable reward designs.

- **Approach**: SSL-R1 is a self-supervised RLVR-based post-training framework that derives intrinsically verifiable rewards from input images, requiring neither human nor external model supervision.

- **Performance**: Training MLLMs on these tasks substantially improves their performance on multimodal understanding and reasoning benchmarks, highlighting the potential of leveraging vision-centric self-supervised tasks for MLLM post-training.

SSL-R1 is vision-centric, cost-effective, scalable, and consistently improves Qwen2.5-VL on 13 vision-centric multimodal benchmarks.

The research was published in April 2026 on arXiv, with the project code available on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f6bf1819-7c3f-4468-849a-12b6027e7839",
  "isSidechain": false,
  "promptId": "d0596239-f589-4752-b6af-bbf7d6ed140d",
  "type": "user",
  "uuid": "b789031d-42b5-49f1-a76c-453db4f8cf67",
  "toolUseResult": {
    "query": "SSL-R1 self-supervised visual reinforcement post-training MLLM 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_019y8KZR2jxUwkEmAKA5h9zK",
        "content": [
          {
            "title": "SSL-R1: Self-Supervised Visual Reinforcement Post-Training for Multimodal Large Language Models",
            "url": "https://arxiv.org/html/2604.20705"
          },
          {
            "title": "[2604.20705] SSL-R1: Self-Supervised Visual Reinforcement Post-Training for Multimodal Large Language Models",
            "url": "https://arxiv.org/abs/2604.20705"
          },
          {
            "title": "(PDF) ViSS-R1: Self-Supervised Reinforcement Video Reasoning",
            "url": "https://www.researchgate.net/publication/397701383_ViSS-R1_Self-Supervised_Reinforcement_Video_Reasoning"
          },
          {
            "title": "Visual Jigsaw Post-Training Improves MLLMs",
            "url": "https://arxiv.org/pdf/2509.25190"
          },
          {
            "title": "ViSS-R1: Self-Supervised Reinforcement Video Reasoning",
            "url": "https://arxiv.org/pdf/2511.13054"
          },
          {
            "title": "Visual Jigsaw Post-Training Improves MLLMs’ Visual Understanding Via Self-Supervised Ordering",
            "url": "https://quantumzeitgeist.com/supervised-training-visual-jigsaw-post-improves-mllms-understanding-self/"
          },
          {
            "title": "Visual Jigsaw Post-Training Improves MLLMs",
            "url": "https://arxiv.org/html/2509.25190"
          }
        ]
      },
      "Based on the search results, here's what I found about SSL-R1:\n\n## SSL-R1: Self-Supervised Visual Reinforcement Post-Training for Multimodal Large Language Models\n\nSSL-R1 is a generic self-supervised RL framework that derives verifiable rewards directly from images. The framework reformulates widely-used SSL tasks into a set of verifiable visual puzzles for RL post-training, requiring neither human nor external model supervision.\n\n### Key Characteristics:\n\n- **Problem it addresses**: The reliance on language-centric priors and expensive manual annotations prevents MLLMs' intrinsic visual understanding and scalable reward designs.\n\n- **Approach**: SSL-R1 is a self-supervised RLVR-based post-training framework that derives intrinsically verifiable rewards from input images, requiring neither human nor external model supervision.\n\n- **Performance**: Training MLLMs on these tasks substantially improves their performance on multimodal understanding and reasoning benchmarks, highlighting the potential of leveraging vision-centric self-supervised tasks for MLLM post-training.\n\nSSL-R1 is vision-centric, cost-effective, scalable, and consistently improves Qwen2.5-VL on 13 vision-centric multimodal benchmarks.\n\nThe research was published in April 2026 on arXiv, with the project code available on GitHub."
    ],
    "durationSeconds": 6.612828806000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f6bf1819-7c3f-4468-849a-12b6027e7839",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5facff83-0af4-48a3-a612-caaf81c1db1b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-27T09:10:07.063Z_

<details><summary>↩ Tool result · `toolu_01WRcPzmCJJziJMyyJnHBnx3`</summary>

```text
Web search results for query: "V-Zero zero-shot multimodal reasoning cross-modal self-play 2026"

Links: [{"title":"[Literature Review] V-Zero: Self-Improving Multimodal Reasoning with Zero Annotation","url":"https://www.themoonlight.io/en/review/v-zero-self-improving-multimodal-reasoning-with-zero-annotation"},{"title":"[2601.10094] V-Zero: Self-Improving Multimodal Reasoning with Zero Annotation","url":"https://arxiv.org/abs/2601.10094"},{"title":"V-Zero: Self-Improving Multimodal Reasoning with Zero Annotation","url":"https://arxiv.org/pdf/2601.10094"},{"title":"GitHub - wangqinsi1/Vision-Zero: [ICLR 2026] Vision-Zero: Scalable VLM Self-Improvement via Strategic Gamified Self-Play. · GitHub","url":"https://github.com/wangqinsi1/Vision-Zero"},{"title":"Plug-and-Play Clarifier: A Zero-Shot Multimodal Framework for Egocentric Intent Disambiguation","url":"https://arxiv.org/html/2511.08971"},{"title":"Vision-Zero: Scalable VLM Self-Improvement via Strategic Gamified Self-Play","url":"https://arxiv.org/pdf/2509.25541"},{"title":"CogGuide: Human-Like Guidance for Zero-Shot Omni-Modal Reasoning","url":"https://arxiv.org/pdf/2509.06641"},{"title":"Zero-Shot Multimodal Reasoning","url":"https://www.emergentmind.com/topics/zero-shot-multimodal-reasoning"}]

Based on the search results, here's what I found about V-Zero:

## V-Zero: Self-Improving Multimodal Reasoning

V-Zero is a research paper released in January 2026 that focuses on self-improving multimodal reasoning for vision-language models.

### Key Features

V-Zero achieves self-improvement from unlabeled images via a dynamic co-evolutionary loop, where reward signals are internally generated through the interaction between a Questioner and a Solver. Both roles are trained iteratively via Group Relative Policy Optimization (GRPO), driving a cycle of mutual enhancement.

### Performance Results

Without a single human annotation, V-Zero achieves consistent performance gains on Qwen2.5-VL-7B-Instruct, improving visual mathematical reasoning by +1.7 and general vision-centric by +2.6.

### Significance

V-Zero demonstrates a promising path for self-improving vision-language models without human annotation by establishing a dynamic co-evolutionary loop and leveraging a novel dual-track reasoning reward, which effectively generates a curriculum of increasing difficulty.

The research represents an important development in enabling multimodal models to improve themselves through cross-modal interaction and self-play without requiring labeled training data.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f25e9d71-1e45-459a-9a90-773f6938169f",
  "isSidechain": false,
  "promptId": "d0596239-f589-4752-b6af-bbf7d6ed140d",
  "type": "user",
  "uuid": "37646166-641c-42b9-8092-638da18c4da8",
  "toolUseResult": {
    "query": "V-Zero zero-shot multimodal reasoning cross-modal self-play 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Ju2H1WSLhWtpn1gtUbtJh9",
        "content": [
          {
            "title": "[Literature Review] V-Zero: Self-Improving Multimodal Reasoning with Zero Annotation",
            "url": "https://www.themoonlight.io/en/review/v-zero-self-improving-multimodal-reasoning-with-zero-annotation"
          },
          {
            "title": "[2601.10094] V-Zero: Self-Improving Multimodal Reasoning with Zero Annotation",
            "url": "https://arxiv.org/abs/2601.10094"
          },
          {
            "title": "V-Zero: Self-Improving Multimodal Reasoning with Zero Annotation",
            "url": "https://arxiv.org/pdf/2601.10094"
          },
          {
            "title": "GitHub - wangqinsi1/Vision-Zero: [ICLR 2026] Vision-Zero: Scalable VLM Self-Improvement via Strategic Gamified Self-Play. · GitHub",
            "url": "https://github.com/wangqinsi1/Vision-Zero"
          },
          {
            "title": "Plug-and-Play Clarifier: A Zero-Shot Multimodal Framework for Egocentric Intent Disambiguation",
            "url": "https://arxiv.org/html/2511.08971"
          },
          {
            "title": "Vision-Zero: Scalable VLM Self-Improvement via Strategic Gamified Self-Play",
            "url": "https://arxiv.org/pdf/2509.25541"
          },
          {
            "title": "CogGuide: Human-Like Guidance for Zero-Shot Omni-Modal Reasoning",
            "url": "https://arxiv.org/pdf/2509.06641"
          },
          {
            "title": "Zero-Shot Multimodal Reasoning",
            "url": "https://www.emergentmind.com/topics/zero-shot-multimodal-reasoning"
          }
        ]
      },
      "Based on the search results, here's what I found about V-Zero:\n\n## V-Zero: Self-Improving Multimodal Reasoning\n\nV-Zero is a research paper released in January 2026 that focuses on self-improving multimodal reasoning for vision-language models.\n\n### Key Features\n\nV-Zero achieves self-improvement from unlabeled images via a dynamic co-evolutionary loop, where reward signals are internally generated through the interaction between a Questioner and a Solver. Both roles are trained iteratively via Group Relative Policy Optimization (GRPO), driving a cycle of mutual enhancement.\n\n### Performance Results\n\nWithout a single human annotation, V-Zero achieves consistent performance gains on Qwen2.5-VL-7B-Instruct, improving visual mathematical reasoning by +1.7 and general vision-centric by +2.6.\n\n### Significance\n\nV-Zero demonstrates a promising path for self-improving vision-language models without human annotation by establishing a dynamic co-evolutionary loop and leveraging a novel dual-track reasoning reward, which effectively generates a curriculum of increasing difficulty.\n\nThe research represents an important development in enabling multimodal models to improve themselves through cross-modal interaction and self-play without requiring labeled training data."
    ],
    "durationSeconds": 8.279461079,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f25e9d71-1e45-459a-9a90-773f6938169f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5facff83-0af4-48a3-a612-caaf81c1db1b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 46_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Axiom-Grounded Self-Verified Perception for Visual Math Reasoning  ## Core Problem and Thesis  Current multimoda…",
  "leafUuid": "37646166-641c-42b9-8092-638da18c4da8",
  "sessionId": "5facff83-0af4-48a3-a612-caaf81c1db1b"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "ai-title",
  "aiTitle": "Axiom-grounded self-verified perception for math reasoning",
  "sessionId": "5facff83-0af4-48a3-a612-caaf81c1db1b"
}
```

---

### Assistant

_source line 48 · 2026-05-27T09:10:57.393Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive picture of the research landscape. Let me synthesize my findings and provide the evaluation.

Let me think through the key questions:

**1. Novelty Assessment:**

The core claim is: "mathematical perception correctness is a joint constraint satisfaction problem, not an independent fact-checking problem." The proposal wants to use mathematical axioms (e.g., angle sum = 180°, Pythagorean theorem) as self-supervised reward signals for RL-based perception training.

Let me check what already exists:
- Perception-R1: per-claim verification using LLM judge, annotation-dependent


- PEARL: per-claim checklist with GT answers, annotation-dependent
- EVPV: per-claim visual premise verification, image-level constraints
- CogFlow: per-claim synergistic rewards, annotation-dependent (120K+ annotations)
- GeoDPO: DSL translation accuracy reward, not axiom-level consistency
- PRCO: utility-based Observer/Solver, domain-agnostic
- SSL-R1: generic visual puzzle rewards, domain-agnostic
- V-Zero: cross-modal self-play, zero annotation
- SymHPR: structural/topological parsing consistency
- FIGR: executable visual states

The existing work focuses on per-claim verification or domain-agnostic rewards, but none directly leverage mathematical axioms as self-supervised constraints for geometry-specific perception training. This axiom-based constraint satisfaction approach appears genuinely novel. The novelty is real but somewhat incremental — it's a natural combination of formal geometry extraction, constraint checking, and RL rewards rather than a fundamentally new paradigm, though the constraint density argument does offer some theoretical value. I'm also considering whether axiom checking at inference time could work as a simpler alternative: just extract the formal representation and resample if axioms are violated, which would be test-time compute scaling without needing RL training at all.

The perception bottleneck is well-established and the problem genuinely matters for multimodal math reasoning, with the appeal of getting reward signals for free without annotations. That said, the scope is fairly narrow — mostly geometry with some extensions to charts and functions — and while the principle of using domain invariants as supervision is interesting, it's only demonstrated on math diagrams so far. The related work section is thorough with a clear novelty positioning table, though I'm flagging a key assumption: whether formal extraction from Geoparsing is reliable enough to actually provide useful axioms.

The constraint density property needs to hold in practice for this to work, and the axiom checker has to be robustly implementable across 40+ theorems on top of FormalGeo. These are testable assumptions, which is encouraging, but they're fundamental to whether the approach succeeds. The core idea is genuinely novel — no one else is doing joint axiom consistency checking as an RL reward signal — and it's well-motivated by the established perception bottleneck. The "free reward signal" framing is elegant, and the constraint density argument adds a nice theoretical layer. The practical approach of leveraging existing infrastructure is solid, though I'm still evaluating the weaknesses.

The method itself feels somewhat predictable once you have formal extraction, RL, and the joint consistency framing in place — the combination flows naturally from those pieces. The scope is limited to geometry with optional extensions to charts and functions. The false positive concern could be more serious than acknowledged, and everything hinges on Geoparsing and FormalGeo quality. Now I'm reconsidering the novelty score. The specific combination is genuinely new and the joint consistency framing hasn't been done before, but the individual components already exist. I'd place it between medium and strong novelty, leaning slightly toward medium. Actually, the positioning is quite clear — using mathematical invariant consistency of perceived quantitative facts as a self-supervised perception signal is genuinely novel.

The 2×2 table comparing per-claim versus joint consistency and annotation-dependent versus annotation-free approaches is compelling and fills a real gap. The constraint density argument adds theoretical weight. I'm settling on medium novelty — real contribution but not paradigm-shifting. Significance lands between medium and strong since the perception bottleneck is a genuine problem and the annotation-free aspect matters, though the scope remains somewhat narrow. The related work coverage is exceptionally thorough. For probability, the core idea has real novelty and addresses an important problem, but there's a risk the positive findings might feel somewhat expected. The execution depends heavily on infrastructure quality. I'm estimating around 30-40%, with a median closer to 33-35%.

Recalibrating for AAAI 2026: the novelty is genuine in its specific formulation with clean framing and excellent related work coverage, but the surprise factor is moderate — reviewers might reasonably expect consistency checking to help. The narrow scope and infrastructure dependency are concerns. I'm settling on 28-38% with a median of 33%. This is a solid paper that needs strong execution but isn't paradigm-shifting.

Looking more carefully at what's working: the novelty gap between joint and per-claim consistency is clear, the annotation-free reward signal is elegant, the mathematical axioms connecting to perception training is well-motivated, the constraint density argument provides theoretical grounding, and it uses practical existing infrastructure. Against it: moderate surprise factor and narrow scope.

For a top venue like AAAI, this is competitive — the novelty is real, related work is thorough, and the approach is well-motivated. I'm revising to 30-38% with median 34%.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37646166-641c-42b9-8092-638da18c4da8",
  "isSidechain": false,
  "requestId": "req_011CbSp6wFFekuTdY2py8iUn",
  "type": "assistant",
  "uuid": "b7eb0414-1b76-49e1-9c93-9fa0b5caa711",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5facff83-0af4-48a3-a612-caaf81c1db1b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sx5f2GgQH5iGqFEDGnKft6",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2974,
      "cache_read_input_tokens": 27178,
      "output_tokens": 6113,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2974,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6113,
          "cache_read_input_tokens": 27178,
          "cache_creation_input_tokens": 2974,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2974
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

_source line 49 · 2026-05-27T09:12:25.449Z_

Now I have sufficient information to conduct a thorough evaluation. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:
- Perception-R1 (arXiv 2506.07218, 2025): 使用 LLM judge 对 VLM 输出的视觉描述进行 per-claim 验证，基于文本注释的一致性打分作为 RL reward。仅需 1,442 训练样本，MathVista 74.2。与本 proposal 的关系：annotation-dependent + per-claim，正是本 proposal 定义的 gap 的代表性方法。
- PEARL (arXiv 2511.18437, CVPR 2026): 为每个推理 QA 生成感知 checklist，用 GT sub-question answers 作为 gating reward，MathVerse +9.7%。与本 proposal 的关系：annotation-dependent + per-claim，需要标注的子问题答案。
- CogFlow (arXiv 2601.01874, ICLR 2026): 三阶段 perception→internalization→reasoning 框架，Synergistic Visual Rewards + Knowledge Internalization Reward，需要 120K+ MathCog 标注。与本 proposal 的关系：annotation-dependent + per-claim，reward 在参数和语义空间而非数学公理空间。
- EVPV (arXiv 2603.16253, 2026): Explicit Visual Premise Verification，从图像提取结构化约束，per-claim 匹配 checklist。与本 proposal 的关系：最接近的竞争者——也是自监督的，但仍然是 per-claim image-level 验证，不检查 claims 之间的数学公理一致性。这是本 proposal 主要需要区分的对手。
- GeoDPO (arXiv 2602.22703, 2026): NL-to-DSL 翻译准确度作为 RL reward，GeoPerceive benchmark，in-domain +26.5%, downstream +39%。与本 proposal 的关系：reward 基于翻译保真度而非公理一致性，提供了 perception-only 评估基准。
- PRCO (arXiv 2603.28618, 2026): Observer/Solver 双角色 RLVR 框架，utility-based reward，8 个 benchmark 平均 +7 分。与本 proposal 的关系：domain-agnostic 自监督，不利用数学结构。
- SSL-R1 (arXiv 2604.20705, 2026): 通用视觉 SSL 拼图任务作为 RLVR reward，13 个 benchmark 上持续提升。与本 proposal 的关系：generic 自监督，不利用领域知识。
- V-Zero (arXiv 2601.10094, 2026): Questioner-Solver 共进化，零标注，+1.7 数学推理。与本 proposal 的关系：零标注自监督，但通用方法，增益较小。
- FGeo-DRL (arXiv 2402.09051, 2024): 基于 FormalGeo 的几何 RL solver，formalgeo7k 上 86.4%。与本 proposal 的关系：验证了 solver-in-the-loop RL 在形式几何中的有效性，但用于推理而非感知。
- Geoparsing (arXiv 2604.11600, 2026): GDP-29K 数据集，SFT+RLVR 训练范式，平面和立体几何的统一形式语言。与本 proposal 的关系：提供了 Stage 0 所依赖的形式化提取基础设施。
- FIGR (arXiv 2512.24297, 2025): 将可执行视觉构建嵌入推理循环，AIME 2025 +13.12%。与本 proposal 的关系：不同路线——通过执行代码验证而非公理约束。
- SGVR/Milestones over Outcome (arXiv 2025): 子目标可验证奖励用于几何推理。与本 proposal 的关系：基线之一。

- 调研总结: 2025-2026年，multimodal math perception 已成为活跃研究方向，多个并行工作从不同角度提出 perception reward（LLM judge、GT checklist、DSL 翻译、通用 SSL、utility-based）。但所有现有方法的 reward 都在 per-claim 层面运作。尚无工作将"感知 claims 之间的数学公理联合一致性"作为自监督 reward 信号。本 proposal 填补的是一个 genuine gap，但这个 gap 的"显而易见程度"是审稿争议点。

【Trivial Alternative 检验】:
最直接的 trivial alternative: 在推理时（inference-time）执行公理一致性检查 + 重采样，无需 RL 训练。具体操作是：在任意现有模型（如 GeoDPO 或 Geoparsing 微调模型）上，提取形式化描述 → 公理检查器验证 → 如果不一致就重新生成。这本质上是 test-time compute scaling 的一种形式。

Proposal 确实预见并回应了这一点（"Why training-time internalization"），给出了三个论点：(1) 效率——单次 forward pass vs 迭代循环；(2) 表征学习——RL 塑造内部视觉表征；(3) 泛化——训练的一致性能力迁移到新配置。但这三个论点目前都是假说，没有实证支撑（虽然 proposal 设计了消融实验来验证）。

增量价值判断：如果消融实验证明 training-time RL 显著优于 inference-time-only（消融组 6），则增量价值成立。但如果差距很小，这个 idea 的核心贡献就大打折扣——因为公理检查本身是 engineering contribution，而非 learning contribution。这是一个 high-variance 的赌注。

【前提假设检验】:
核心逻辑链条中有以下未验证假设：

1. **形式化提取质量假设**: 公理一致性 reward 的有效性完全依赖于 Geoparsing/FormalGeo 能可靠地将图表转化为结构化描述。如果提取本身有大量噪声（漏提元素、错误识别关系），公理检查器的输入就已经不可靠，reward 信号也会失真。Geoparsing 论文本身就指出需要 SFT+RLVR 才能获得合理质量——而本 proposal 的 Stage 0 只用了其数据子集做 SFT。

2. **约束密度-错误检出率关系假设**: Proposal 的核心理论论点是"更多公理 → 更紧的可行域 → 更低的 false positive rate"。这在数学上是正确的（更多约束确实缩小可行域），但实际效果取决于 (a) 每个图表平均能应用多少公理（如果大部分图表只能应用 1-2 个公理，约束密度就很低），(b) 公理之间的冗余程度。这个假设需要在真实数据上验证。

3. **Soft reward 信息量假设**: 提出了连续打分（1 - |violation|/scale）替代二值 pass/fail。但这隐含假设 violation magnitude 是 perception 错误的单调函数——而实际上，一个"差一点"的值可能是噪声而非系统性错误，而一个"差很多"的值可能是提取器的彻底失败（不可修复）。

4. **RL reward → 内部表征改善假设**: 假设公理一致性 reward 能通过 GRPO 有效地改善 VLM 的内部视觉表征，使其"倾向于生成公理一致的感知"。但 GRPO 主要在输出空间操作，能否有效改变视觉编码器的表征是一个开放问题（尤其是对 frozen visual encoder 的 VLM）。

以上假设均非致命，但构成了论文成功的关键前提。

【3 维度打分】:
1. Novelty: 中（偏强） — "per-claim vs joint consistency"这一区分是 genuine insight，填补了现有工作的真实空白。调研显示所有现有 perception reward 方法（Perception-R1、PEARL、EVPV、CogFlow、GeoDPO、PRCO）确实都在 per-claim 层面运作，没有工作检查 perceived facts 之间的数学公理一致性。"数学不变量作为自监督 reward"的 framing 是清晰且新颖的。但降低 novelty 评分的因素：(a) 一旦有了 Geoparsing 的形式化提取和 FormalGeo 的公理验证基础设施，将两者组合为 RL reward 是一个相对自然的想法——属于"well-motivated combination"而非"paradigm shift"；(b) EVPV 已经走到了"自监督视觉约束作为 reward"这一步，从 per-claim image-level 到 joint axiom-level 的跳跃是渐进式的。

2. Significance: 中 — 问题本身重要（MM-MATH 的 61% perception error 确立了瓶颈），annotation-free 属性有吸引力。但 significance 受限于：(a) 应用范围主要是几何图形，chart 和 function 扩展标记为 optional，实际论文可能只覆盖几何；(b) 如果核心发现是 positive（公理一致性 reward 帮助提升 perception accuracy），审稿人可能会说 "this makes sense, I would have guessed consistency checking helps"——属于 confirmatory 而非 surprising 的结果；(c) 更广泛的"领域不变量作为自监督信号"的 principle 虽然被提及（Kirchhoff 定律、化学价约束），但不会在论文中验证，只是 future direction。

3. Related Work: 强 — 这是本 proposal 最出色的维度。覆盖了 2024-2026 几乎所有直接相关的工作（Perception-R1、PEARL、EVPV、CogFlow、GeoDPO、PRCO、SSL-R1、V-Zero、SymHPR、PDCR、M3-ACE、PFlowNet、SGVR），并用清晰的 2×2 表格（per-claim vs joint × annotation-dependent vs annotation-free）进行定位。与每个竞争者的差异化分析具体而准确。对 EVPV 的区分（image-level perceptual constraints vs domain-level mathematical axioms）是最关键的差异化论点，表述清晰。唯一小风险：引用的部分论文是 2026 年的 arXiv 预印本，可能在 AAAI 投稿截止前有更新或更多竞争者出现。

【概率估计】: 28% - 38%，中位 33%

【估计理由】:
Novelty 是中偏强（填补了 genuine gap，但组合性质较强），这决定了概率上界不会很高——如果核心发现是 positive，它更可能是 confirmatory（"一致性检查确实有用"）而非 surprising。Significance 受限于较窄的应用范围（主要是几何）和可能的"I would have guessed this"反应。Related Work 是强项，降低了因 positioning 不清而被拒的风险。

上界（38%）对应的场景：公理一致性 reward 显著优于所有 per-claim baseline 和 inference-time-only 的 trivial alternative，"constraint density"假说在实验中得到验证，产生一个 clean story。
下界（28%）对应的场景：Geoparsing 提取质量不足导致 reward 信号噪声大，或 training-time RL 相比 inference-time 公理检查的增量很小，使得核心贡献变成 engineering contribution。

上界的限制因素主要是 Novelty 的天花板——即使实验完美执行，idea 本身的"组合自然性"限制了它的 surprise factor。

【主要风险】:
1. **Trivial alternative 威胁**: 如果 inference-time 公理检查 + 重采样（无需 RL 训练）就能获得大部分收益，则 training-time RL 的贡献被大幅稀释，论文核心 claim 从"需要 RL 内化公理一致性"退化为"公理检查器本身有用"（engineering contribution）。
2. **形式化提取瓶颈**: 公理一致性 reward 的上游完全依赖 Geoparsing/FormalGeo 的提取质量。如果提取错误率高，reward 信号本身就不可靠，可能导致 RL 训练失败或效果平庸——而审稿人会质疑"你的 reward 信号质量本身就有问题，怎么证明是 joint consistency 帮了忙而不是碰巧？"
```

Sources:
- [Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward](https://arxiv.org/abs/2506.07218)
- [PEARL: Perceptual-Evidence Anchored Reinforced Learning for Multimodal Reasoning](https://arxiv.org/abs/2511.18437)
- [CogFlow: Bridging Perception and Reasoning through Knowledge Internalization](https://arxiv.org/abs/2601.01874)
- [EVPV: Grounding the Score: Explicit Visual Premise Verification](https://arxiv.org/abs/2603.16253)
- [GeoDPO: Enhancing Geometric Perception in VLMs via Translator-Guided RL](https://arxiv.org/abs/2602.22703)
- [PRCO: Seeing with You: Perception-Reasoning Coevolution](https://arxiv.org/abs/2603.28618)
- [SSL-R1: Self-Supervised Visual Reinforcement Post-Training](https://arxiv.org/abs/2604.20705)
- [V-Zero: Self-Improving Multimodal Reasoning with Zero Annotation](https://arxiv.org/abs/2601.10094)
- [FGeo-DRL: Deductive Reasoning for Geometric Problems through Deep RL](https://arxiv.org/abs/2402.09051)
- [Geoparsing: Diagram Parsing with Unified Formal Language](https://arxiv.org/abs/2604.11600)
- [FIGR: Figure It Out: Improve Reasoning with Executable Visual States](https://arxiv.org/abs/2512.24297)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7eb0414-1b76-49e1-9c93-9fa0b5caa711",
  "isSidechain": false,
  "requestId": "req_011CbSp6wFFekuTdY2py8iUn",
  "type": "assistant",
  "uuid": "d84489e2-68a7-4cfb-a1f4-112ba8440fdf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5facff83-0af4-48a3-a612-caaf81c1db1b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sx5f2GgQH5iGqFEDGnKft6",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2974,
      "cache_read_input_tokens": 27178,
      "output_tokens": 6113,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2974,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6113,
          "cache_read_input_tokens": 27178,
          "cache_creation_input_tokens": 2974,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2974
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

_source line 50_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Axiom-Grounded Self-Verified Perception for Visual Math Reasoning  ## Core Problem and Thesis  Current multimoda…",
  "leafUuid": "d84489e2-68a7-4cfb-a1f4-112ba8440fdf",
  "sessionId": "5facff83-0af4-48a3-a612-caaf81c1db1b"
}
```

---

### Runtime record

_source line 51_

```json
{
  "type": "ai-title",
  "aiTitle": "Axiom-grounded self-verified perception for math reasoning",
  "sessionId": "5facff83-0af4-48a3-a612-caaf81c1db1b"
}
```

---
