# Research conversation: Axiom-Grounded Self-Verified Perception for Visual Math Reasoning ## Core Problem and Thesis Current multimodal math rea

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 63
- **Recorded user turns:** 1
- **Tool calls:** 19
- **Original source:** `logs/chats/exported-trajectories/account-2/e8953efc-455a-4cba-89cd-695fc452845c.jsonl`
- **Structured JSON:** [`7cdba82ad9d2408e05a7.json`](../../sessions/7c/7cdba82ad9d2408e05a7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-27T08:43:57.456Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T08:43:57.456Z",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c",
  "content": "# Axiom-Grounded Self-Verified Perception for Visual Math Reasoning\n\n## Core Problem and Thesis\n\nCurrent multimodal math reasoning systems verify perceived visual facts independently—checking each claim against the image in isolation—but never verify whether perceived facts are mutually consistent under known mathematical constraints. This causes individually plausible but collectively impossible perceptions to cascade into reasoning failures. We argue that mathematical perception correctness is fundamentally a joint constraint satisfaction problem, not an independent fact-checking problem: even when each perceived fact has high marginal confidence, the joint set may violate mathematical axioms (e.g., three individually plausible angle estimates that do not sum to 180°). All existing per-claim verification approaches—whether using LLM judges (Perception-R1, arXiv 2025), ground-truth checklists (PEARL, arXiv 2025), or image-extracted constraints (EVPV, arXiv 2026)—are structurally blind to such inter-claim inconsistencies, regardless of their per-claim accuracy.\n\n## Research Opportunity\n\nMathematical diagrams encode structural invariants (geometric theorems like angle sums, Pythagorean constraints, parallel-line properties, circle theorems; chart constraints like sum-to-total; function constraints like monotonicity) that perceived facts must jointly satisfy. These invariants provide a free, dense, automatically verifiable reward signal for RL-based perception training—requiring no ground truth annotations. This is newly feasible because (1) diagram formalization methods (DFE-GPS (AAAI 2025), Geoparsing (arXiv 2026)) now reliably extract structured representations, (2) solver-in-the-loop RL has been proven effective for reasoning (FGeo-DRL achieves 86.4% on formalgeo7k via RL in formal geometry environments (arXiv 2024); sub-goal verifiable rewards unlock geometric reasoning gains (Milestones over Outcome, arXiv 2025)), and (3) the perception bottleneck is definitively established (61% of multimodal math errors are perception errors per MM-MATH (arXiv 2024)).\n\nThe principle that domain-specific structural invariants serve as free self-supervised perception rewards extends beyond mathematics—Kirchhoff's laws for circuit diagrams, valence constraints for chemical structures, dimensional consistency for engineering drawings all exhibit the same \"axioms provide free verification\" structure—though this paper demonstrates the paradigm on mathematical diagrams.\n\n## Research Landscape\n\nPerception is the confirmed bottleneck: Qwen3-VL leads MathVista (ICLR 2024) at 85.8% but models still fail systematically on vision-dense problems (MathVerse vision-only subsets). The current landscape of perception-focused methods can be categorized by their reward signal source:\n\n**Annotation-dependent rewards.** Perception-R1 (arXiv 2025) introduces an LLM-judged visual perception reward but requires pre-collected textual annotations and checks individual claims, not inter-claim consistency. PEARL (arXiv 2025) uses ground-truth perception checklists as gating rewards (+9.7% on MathVerse) but needs annotated sub-question answers.\n\n**Image-level per-claim verification.** EVPV (arXiv 2026) matches per-claim visual checklists against image-extracted constraints but checks each claim independently against image-level perceptual features (e.g., \"this angle appears to be ~60°\")—it does not verify whether the set of perceived values jointly satisfies domain-level mathematical axioms (e.g., \"these three angles must sum to 180°\"). This distinction—image-level perceptual constraints vs. domain-level mathematical axioms—is the precise gap our work fills.\n\n**Translation-fidelity rewards.** GeoDPO (arXiv 2026) uses NL-to-DSL translator-guided RL for geometric perception (+26.5% in-domain, +39% downstream) but rewards DSL translation accuracy, not axiom-level consistency of perceived quantitative values.\n\n**Structural/topological parsing.** SymHPR (arXiv 2025) enforces structural parsing consistency (point-on-line, shape-on-relation) for diagram reconstruction at the topological level. Our approach operates at the quantitative level and implicitly depends on reasonable topological parsing—we address this dependency through curriculum design (see Approach).\n\n**Utility-based and generic self-supervised rewards.** PRCO (arXiv 2026) introduces Observer/Solver role separation with utility-based perception rewards but does not exploit mathematical structure for verification. SSL-R1 (arXiv 2026) derives self-supervised visual RL rewards from generic SSL puzzles (rotation prediction, patch ordering) rather than domain-specific mathematical invariants. V-Zero (arXiv 2026) uses Questioner-Solver co-evolutionary loop for zero-annotation training but is domain-agnostic. Our approach's advantage over domain-agnostic methods is that mathematical invariants provide stronger, more targeted supervision than generic visual puzzles.\n\n**Confidence-based and inference-time methods.** PDCR (arXiv 2026) decomposes perception and reasoning rewards via model-internal confidence scores but does not use formal mathematical constraints. M3-ACE (arXiv 2026) uses multi-agentic context engineering to rectify perception at inference time but does not train perception via RL rewards. PFlowNet (arXiv 2026) applies variational RL with geometric reward shaping where 'geometric' refers to reward landscape geometry, not mathematical theorem constraints.\n\n**Why training-time internalization, not inference-time correction.** A natural question is whether axiom checking at inference time alone (without RL training) suffices. We argue training-time internalization via RL offers three advantages over inference-time-only correction: (1) computational efficiency—a trained model produces axiom-consistent perceptions in a single forward pass, while inference-time correction requires iterative re-perception loops with axiom checking at each step; (2) representation-level learning—RL shapes the model's internal visual representations to favor axiom-consistent percepts, rather than patching inconsistencies at the output level; (3) generalization—trained axiom-consistency transfers to novel diagram configurations and axiom combinations not seen during training. We validate this through ablation comparing training-time RL vs. inference-time-only axiom correction.\n\nNo existing work uses mathematical invariant consistency of perceived quantitative facts as a self-supervised perception reward signal.\n\n## Proposed Approach\n\nWe train a VLM (Qwen3-VL-8B as primary base, with Qwen3-VL-3B for scale-transfer validation) to perceive mathematical diagrams accurately using axiom-consistency as a self-supervised RLVR reward, requiring zero ground-truth perception annotations.\n\n**Stage 0: Formal Extraction Warm-Start.** Since axiom rewards require parseable formal descriptions, and VLMs cannot produce these from scratch, we first SFT the base model on FormalGeo/Geoparsing (arXiv 2026) data (a subset of GDP-29K) to bootstrap syntactically valid diagram-to-formal-language extraction. This addresses the bootstrapping challenge: axiom reward quality depends on reasonable formal extraction, which itself requires training. Geoparsing's own SFT+RLVR paradigm confirms this warm-start is necessary.\n\n**Stage 1: Perception-Only Axiom RL.** The model extracts structured perception claims (angles, lengths, coordinates, ratios) from diagrams into a formal constraint description language built on FormalGeo (arXiv 2023)/Geoparsing primitives. A lightweight axiom checker—implementing 40+ geometric theorems (angle sums, Pythagorean constraints, parallel-line properties, circle theorems) plus chart and function invariants—evaluates whether the perceived facts jointly satisfy all applicable mathematical constraints, producing a soft consistency score: for each applicable axiom, the violation magnitude is computed (e.g., |angle_sum − 180°|/180°) and the axiom-consistency reward is the mean of (1 − normalized_violation) across all applicable axioms. This continuous scoring provides gradient-rich reward signal for near-correct perceptions, avoiding the sparsity of binary pass/fail. An auxiliary parsability reward (whether the formal description is syntactically valid and parseable by the axiom checker) supplements the consistency reward in early training. Training uses GRPO via the veRL framework. The curriculum begins with structurally simple diagrams (single triangles, basic charts) where topological parsing is easy, progressively increasing to complex multi-shape configurations, mitigating the dependency on correct structural parsing noted in SymHPR (arXiv 2025).\n\n**Stage 2: Joint Perception-Reasoning.** Combines axiom-consistency reward with outcome-based answer correctness in GRPO training, jointly optimizing perception and reasoning.\n\n**Inference-Time Self-Verification.** Perceived facts violating axioms trigger iterative re-perception (up to 3 iterations), providing built-in self-verification without external judges. We report inference latency with and without re-perception.\n\n## Experimental Design\n\n**Benchmarks.** MathVista (ICLR 2024), MathVerse (with vision-only / vision-dominant / vision-intensive subset breakdown), MathVision (NeurIPS 2024), GeoQA, formalgeo7k. WeMath as optional extension.\n\n**Baselines (4 categories).**\n- *Base VLM:* Qwen3-VL-8B zero-shot; Qwen3-VL-8B + SFT (same data as Stage 0, no RL)\n- *Perception RL methods:* Perception-R1 (arXiv 2025, LLM-judged reward); GeoDPO (arXiv 2026, DSL-translation reward)\n- *Self-supervised RL:* SSL-R1 (arXiv 2026, generic visual puzzle reward) if code available; answer-only GRPO (answer correctness reward only, no perception reward)\n- *Reference numbers:* PEARL (arXiv 2025), EVPV (arXiv 2026), PRCO (arXiv 2026) reported results where available\n\n**Ablation Studies (5 groups).**\n1. *Reward components:* axiom reward only / answer reward only / axiom + answer (full) / random reward (sanity check)\n2. *Training curriculum:* three-stage (proposed) / skip Stage 0 (no warm-start) / skip Stage 1 (joint from scratch) / Stage 1 only (perception-only)\n3. *Axiom set:* full 40+ axioms / basic axioms only (angle sum, Pythagorean) / chart+function invariants only\n4. *Scoring strategy:* soft continuous / hard binary (ε = 0.5°, 1°, 2°) / weighted combination\n5. *Inference-time re-perception:* 0 / 1 / 2 / 3 iterations—performance vs. latency tradeoff\n\n**Additional Analyses.**\n- *Reward signal quality:* On a GT-annotated subset, compute Pearson/Spearman correlation between axiom-consistency score and true perception accuracy; report false positive (axiom-consistent but perception-incorrect) and false negative rates; visualize representative success and failure cases\n- *Compute fairness:* Report training wall-clock time and per-step overhead for each method; plot performance vs. training FLOPs curves; quantify axiom checker per-sample latency\n- *Scale transfer:* Replicate main experiments on Qwen3-VL-3B (MathVista, MathVerse) to validate method generality across model scales\n- *Training-time RL vs. inference-time-only:* Compare full ASVP against \"Stage 0 SFT + axiom-based re-perception at inference without RL training\" to validate the necessity of RL-based internalization\n\n## Key References\n\n- Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward (arXiv 2025)\n- PEARL: Perceptual-Evidence Anchored Reinforced Learning for Multimodal Reasoning (arXiv 2025)\n- Grounding the Score: Explicit Visual Premise Verification for Reliable VLM Process Reward Models [EVPV] (arXiv 2026)\n- Hierarchical Process Reward Models are Symbolic Vision Learners [SymHPR] (arXiv 2025)\n- MM-MATH: Advancing Multimodal Math Evaluation with Process Evaluation and Fine-grained Classification (arXiv 2024)\n- Diagram Formalization Enhanced Multi-Modal Geometry Problem Solver [DFE-GPS] (AAAI 2025)\n- Geoparsing: Diagram Parsing for Plane and Solid Geometry with a Unified Formal Language (arXiv 2026)\n- TrustGeoGen: Formal-Verified Data Engine for Trustworthy Multi-modal Geometric Problem Solving (arXiv 2025)\n- FormalGeo: An Extensible Formalized Framework for Olympiad Geometric Problem Solving (arXiv 2023)\n- GeoPQA: Bridging the Visual Perception Gap in MLLMs for Geometric Reasoning (EMNLP 2025)\n- Enhancing Geometric Perception in VLMs via Translator-Guided Reinforcement Learning [GeoDPO] (arXiv 2026)\n- M3-ACE: Rectifying Visual Perception in Multimodal Math Reasoning via Multi-Agentic Context Engineering (arXiv 2026)\n- PDCR: Perception-Decomposed Confidence Reward for Vision-Language Reasoning (arXiv 2026)\n- SSL-R1: Self-Supervised Visual Reinforcement Post-Training for MLLMs (arXiv 2026)\n- Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning [PRCO] (arXiv 2026)\n- MathVista: Evaluating Mathematical Reasoning of Foundation Models in Visual Contexts (ICLR 2024)\n- FGeo-DRL: Deductive Reasoning for Geometric Problems through Deep Reinforcement Learning (arXiv 2024)\n- A Survey of Multimodal Mathematical Reasoning: From Perception, Alignment to Reasoning (arXiv 2026)\n- Figure It Out: Improve the Frontier of Reasoning with Executable Visual States [FIGR] (arXiv 2025)\n- Milestones over Outcome: Unlocking Geometric Reasoning with Sub-Goal Verifiable Reward (arXiv 2025)\n- PFlowNet: Perceptual Flow Network for Visually Grounded Reasoning (arXiv 2026)\n- Measuring Multimodal Mathematical Reasoning with MATH-Vision Dataset [MathVision] (NeurIPS 2024)\n- V-Zero: Zero-Shot Multimodal Reasoning via Cross-Modal Self-Play (arXiv 2026)\n\n## Resource Estimate\n\n- **manual**: gpu_hours: 1500-1800 (8×H100: axiom checker development, Stage 0 SFT, 4-5 GRPO training runs at ~30h each, ablation studies, multi-benchmark evaluation, Qwen3-VL-3B replication), timeline: 9-11 weeks (2 wks axiom checker + data pipeline + Stage 0 SFT, 3-4 wks RL training iterations, 2-3 wks evaluation + ablation + paper writing), estimated_gpu_cost: $3,750-$4,500\n- **human_in_loop**: gpu_hours: 1000-1400 (Claude accelerates axiom checker coding, reward function design, and ablation analysis), timeline: 6-8 weeks, claude_api_cost: $400-$700, estimated_gpu_cost: $2,500-$3,500\n- **auto_research**: gpu_hours: 1800-2400 (broader axiom-weight tuning, architecture search over reward combinations, automated multi-seed runs, scale-transfer experiments), timeline: 4-6 weeks, claude_api_cost: $900-$1,400, estimated_gpu_cost: $4,500-$6,000, speed_bottleneck: RL convergence under potentially sparse axiom-violation signals; constraint checker robustness on degenerate/ambiguous diagram parses"
}
```

---

### Runtime record

_source line 2 · 2026-05-27T08:43:57.462Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T08:43:57.462Z",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c"
}
```

---

## Round 1

61 recorded events

### User

_source line 3 · 2026-05-27T08:43:57.483Z_

# Axiom-Grounded Self-Verified Perception for Visual Math Reasoning

## Core Problem and Thesis

Current multimodal math reasoning systems verify perceived visual facts independently—checking each claim against the image in isolation—but never verify whether perceived facts are mutually consistent under known mathematical constraints. This causes individually plausible but collectively impossible perceptions to cascade into reasoning failures. We argue that mathematical perception correctness is fundamentally a joint constraint satisfaction problem, not an independent fact-checking problem: even when each perceived fact has high marginal confidence, the joint set may violate mathematical axioms (e.g., three individually plausible angle estimates that do not sum to 180°). All existing per-claim verification approaches—whether using LLM judges (Perception-R1, arXiv 2025), ground-truth checklists (PEARL, arXiv 2025), or image-extracted constraints (EVPV, arXiv 2026)—are structurally blind to such inter-claim inconsistencies, regardless of their per-claim accuracy.

## Research Opportunity

Mathematical diagrams encode structural invariants (geometric theorems like angle sums, Pythagorean constraints, parallel-line properties, circle theorems; chart constraints like sum-to-total; function constraints like monotonicity) that perceived facts must jointly satisfy. These invariants provide a free, dense, automatically verifiable reward signal for RL-based perception training—requiring no ground truth annotations. This is newly feasible because (1) diagram formalization methods (DFE-GPS (AAAI 2025), Geoparsing (arXiv 2026)) now reliably extract structured representations, (2) solver-in-the-loop RL has been proven effective for reasoning (FGeo-DRL achieves 86.4% on formalgeo7k via RL in formal geometry environments (arXiv 2024); sub-goal verifiable rewards unlock geometric reasoning gains (Milestones over Outcome, arXiv 2025)), and (3) the perception bottleneck is definitively established (61% of multimodal math errors are perception errors per MM-MATH (arXiv 2024)).

The principle that domain-specific structural invariants serve as free self-supervised perception rewards extends beyond mathematics—Kirchhoff's laws for circuit diagrams, valence constraints for chemical structures, dimensional consistency for engineering drawings all exhibit the same "axioms provide free verification" structure—though this paper demonstrates the paradigm on mathematical diagrams.

## Research Landscape

Perception is the confirmed bottleneck: Qwen3-VL leads MathVista (ICLR 2024) at 85.8% but models still fail systematically on vision-dense problems (MathVerse vision-only subsets). The current landscape of perception-focused methods can be categorized by their reward signal source:

**Annotation-dependent rewards.** Perception-R1 (arXiv 2025) introduces an LLM-judged visual perception reward but requires pre-collected textual annotations and checks individual claims, not inter-claim consistency. PEARL (arXiv 2025) uses ground-truth perception checklists as gating rewards (+9.7% on MathVerse) but needs annotated sub-question answers.

**Image-level per-claim verification.** EVPV (arXiv 2026) matches per-claim visual checklists against image-extracted constraints but checks each claim independently against image-level perceptual features (e.g., "this angle appears to be ~60°")—it does not verify whether the set of perceived values jointly satisfies domain-level mathematical axioms (e.g., "these three angles must sum to 180°"). This distinction—image-level perceptual constraints vs. domain-level mathematical axioms—is the precise gap our work fills.

**Translation-fidelity rewards.** GeoDPO (arXiv 2026) uses NL-to-DSL translator-guided RL for geometric perception (+26.5% in-domain, +39% downstream) but rewards DSL translation accuracy, not axiom-level consistency of perceived quantitative values.

**Structural/topological parsing.** SymHPR (arXiv 2025) enforces structural parsing consistency (point-on-line, shape-on-relation) for diagram reconstruction at the topological level. Our approach operates at the quantitative level and implicitly depends on reasonable topological parsing—we address this dependency through curriculum design (see Approach).

**Utility-based and generic self-supervised rewards.** PRCO (arXiv 2026) introduces Observer/Solver role separation with utility-based perception rewards but does not exploit mathematical structure for verification. SSL-R1 (arXiv 2026) derives self-supervised visual RL rewards from generic SSL puzzles (rotation prediction, patch ordering) rather than domain-specific mathematical invariants. V-Zero (arXiv 2026) uses Questioner-Solver co-evolutionary loop for zero-annotation training but is domain-agnostic. Our approach's advantage over domain-agnostic methods is that mathematical invariants provide stronger, more targeted supervision than generic visual puzzles.

**Confidence-based and inference-time methods.** PDCR (arXiv 2026) decomposes perception and reasoning rewards via model-internal confidence scores but does not use formal mathematical constraints. M3-ACE (arXiv 2026) uses multi-agentic context engineering to rectify perception at inference time but does not train perception via RL rewards. PFlowNet (arXiv 2026) applies variational RL with geometric reward shaping where 'geometric' refers to reward landscape geometry, not mathematical theorem constraints.

**Why training-time internalization, not inference-time correction.** A natural question is whether axiom checking at inference time alone (without RL training) suffices. We argue training-time internalization via RL offers three advantages over inference-time-only correction: (1) computational efficiency—a trained model produces axiom-consistent perceptions in a single forward pass, while inference-time correction requires iterative re-perception loops with axiom checking at each step; (2) representation-level learning—RL shapes the model's internal visual representations to favor axiom-consistent percepts, rather than patching inconsistencies at the output level; (3) generalization—trained axiom-consistency transfers to novel diagram configurations and axiom combinations not seen during training. We validate this through ablation comparing training-time RL vs. inference-time-only axiom correction.

No existing work uses mathematical invariant consistency of perceived quantitative facts as a self-supervised perception reward signal.

## Proposed Approach

We train a VLM (Qwen3-VL-8B as primary base, with Qwen3-VL-3B for scale-transfer validation) to perceive mathematical diagrams accurately using axiom-consistency as a self-supervised RLVR reward, requiring zero ground-truth perception annotations.

**Stage 0: Formal Extraction Warm-Start.** Since axiom rewards require parseable formal descriptions, and VLMs cannot produce these from scratch, we first SFT the base model on FormalGeo/Geoparsing (arXiv 2026) data (a subset of GDP-29K) to bootstrap syntactically valid diagram-to-formal-language extraction. This addresses the bootstrapping challenge: axiom reward quality depends on reasonable formal extraction, which itself requires training. Geoparsing's own SFT+RLVR paradigm confirms this warm-start is necessary.

**Stage 1: Perception-Only Axiom RL.** The model extracts structured perception claims (angles, lengths, coordinates, ratios) from diagrams into a formal constraint description language built on FormalGeo (arXiv 2023)/Geoparsing primitives. A lightweight axiom checker—implementing 40+ geometric theorems (angle sums, Pythagorean constraints, parallel-line properties, circle theorems) plus chart and function invariants—evaluates whether the perceived facts jointly satisfy all applicable mathematical constraints, producing a soft consistency score: for each applicable axiom, the violation magnitude is computed (e.g., |angle_sum − 180°|/180°) and the axiom-consistency reward is the mean of (1 − normalized_violation) across all applicable axioms. This continuous scoring provides gradient-rich reward signal for near-correct perceptions, avoiding the sparsity of binary pass/fail. An auxiliary parsability reward (whether the formal description is syntactically valid and parseable by the axiom checker) supplements the consistency reward in early training. Training uses GRPO via the veRL framework. The curriculum begins with structurally simple diagrams (single triangles, basic charts) where topological parsing is easy, progressively increasing to complex multi-shape configurations, mitigating the dependency on correct structural parsing noted in SymHPR (arXiv 2025).

**Stage 2: Joint Perception-Reasoning.** Combines axiom-consistency reward with outcome-based answer correctness in GRPO training, jointly optimizing perception and reasoning.

**Inference-Time Self-Verification.** Perceived facts violating axioms trigger iterative re-perception (up to 3 iterations), providing built-in self-verification without external judges. We report inference latency with and without re-perception.

## Experimental Design

**Benchmarks.** MathVista (ICLR 2024), MathVerse (with vision-only / vision-dominant / vision-intensive subset breakdown), MathVision (NeurIPS 2024), GeoQA, formalgeo7k. WeMath as optional extension.

**Baselines (4 categories).**
- *Base VLM:* Qwen3-VL-8B zero-shot; Qwen3-VL-8B + SFT (same data as Stage 0, no RL)
- *Perception RL methods:* Perception-R1 (arXiv 2025, LLM-judged reward); GeoDPO (arXiv 2026, DSL-translation reward)
- *Self-supervised RL:* SSL-R1 (arXiv 2026, generic visual puzzle reward) if code available; answer-only GRPO (answer correctness reward only, no perception reward)
- *Reference numbers:* PEARL (arXiv 2025), EVPV (arXiv 2026), PRCO (arXiv 2026) reported results where available

**Ablation Studies (5 groups).**
1. *Reward components:* axiom reward only / answer reward only / axiom + answer (full) / random reward (sanity check)
2. *Training curriculum:* three-stage (proposed) / skip Stage 0 (no warm-start) / skip Stage 1 (joint from scratch) / Stage 1 only (perception-only)
3. *Axiom set:* full 40+ axioms / basic axioms only (angle sum, Pythagorean) / chart+function invariants only
4. *Scoring strategy:* soft continuous / hard binary (ε = 0.5°, 1°, 2°) / weighted combination
5. *Inference-time re-perception:* 0 / 1 / 2 / 3 iterations—performance vs. latency tradeoff

**Additional Analyses.**
- *Reward signal quality:* On a GT-annotated subset, compute Pearson/Spearman correlation between axiom-consistency score and true perception accuracy; report false positive (axiom-consistent but perception-incorrect) and false negative rates; visualize representative success and failure cases
- *Compute fairness:* Report training wall-clock time and per-step overhead for each method; plot performance vs. training FLOPs curves; quantify axiom checker per-sample latency
- *Scale transfer:* Replicate main experiments on Qwen3-VL-3B (MathVista, MathVerse) to validate method generality across model scales
- *Training-time RL vs. inference-time-only:* Compare full ASVP against "Stage 0 SFT + axiom-based re-perception at inference without RL training" to validate the necessity of RL-based internalization

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
- Milestones over Outcome: Unlocking Geometric Reasoning with Sub-Goal Verifiable Reward (arXiv 2025)
- PFlowNet: Perceptual Flow Network for Visually Grounded Reasoning (arXiv 2026)
- Measuring Multimodal Mathematical Reasoning with MATH-Vision Dataset [MathVision] (NeurIPS 2024)
- V-Zero: Zero-Shot Multimodal Reasoning via Cross-Modal Self-Play (arXiv 2026)

## Resource Estimate

- **manual**: gpu_hours: 1500-1800 (8×H100: axiom checker development, Stage 0 SFT, 4-5 GRPO training runs at ~30h each, ablation studies, multi-benchmark evaluation, Qwen3-VL-3B replication), timeline: 9-11 weeks (2 wks axiom checker + data pipeline + Stage 0 SFT, 3-4 wks RL training iterations, 2-3 wks evaluation + ablation + paper writing), estimated_gpu_cost: $3,750-$4,500
- **human_in_loop**: gpu_hours: 1000-1400 (Claude accelerates axiom checker coding, reward function design, and ablation analysis), timeline: 6-8 weeks, claude_api_cost: $400-$700, estimated_gpu_cost: $2,500-$3,500
- **auto_research**: gpu_hours: 1800-2400 (broader axiom-weight tuning, architecture search over reward combinations, automated multi-seed runs, scale-transfer experiments), timeline: 4-6 weeks, claude_api_cost: $900-$1,400, estimated_gpu_cost: $4,500-$6,000, speed_bottleneck: RL convergence under potentially sparse axiom-violation signals; constraint checker robustness on degenerate/ambiguous diagram parses

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "fbf4376b-8631-4eaa-a9bd-ce1f560c8253",
  "type": "user",
  "uuid": "587554f2-44e6-4d6a-b275-428b82275e62",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-27T08:43:57.482Z_

```json
{
  "parentUuid": "587554f2-44e6-4d6a-b275-428b82275e62",
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
  "uuid": "9789f785-732d-4068-8d9c-fdb68dfc5f59",
  "timestamp": "2026-05-27T08:43:57.482Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-27T08:43:57.482Z_

```json
{
  "parentUuid": "9789f785-732d-4068-8d9c-fdb68dfc5f59",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "5098be86-6fea-44a8-93b1-405e70af3975",
  "timestamp": "2026-05-27T08:43:57.482Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c",
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
  "lastPrompt": "# Axiom-Grounded Self-Verified Perception for Visual Math Reasoning  ## Core Problem and Thesis  Current multimodal math reasoning systems verify perceived visual facts independently—checking each cla…",
  "leafUuid": "5098be86-6fea-44a8-93b1-405e70af3975",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Axiom-grounded self-verified visual math reasoning",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c"
}
```

---

### Assistant

_source line 8 · 2026-05-27T08:44:00.898Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze this proposal carefully. It's about "Axiom-Grounded Self-Verified Perception for Visual Math Reasoning" - using mathematical invariants (like angle sums, Pythagorean constraints) as self-supervised reward signals for RL-based perception training in VLMs.

Let me first do thorough web searches to understand the current landscape before giving any suggestions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5098be86-6fea-44a8-93b1-405e70af3975",
  "isSidechain": false,
  "requestId": "req_011CbSn7EmiocZxX38c8Bpcy",
  "type": "assistant",
  "uuid": "a9bf49dd-0f8d-4c6b-a77a-be3fd1f7c987",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CHcULTC9Bh4MwVQUvLEvzt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5274,
      "cache_read_input_tokens": 14184,
      "output_tokens": 202,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5274,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 202,
          "cache_read_input_tokens": 14184,
          "cache_creation_input_tokens": 5274,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5274
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

_source line 9 · 2026-05-27T08:44:01.340Z_

I need to do thorough literature research before evaluating this proposal. Let me start with targeted searches on the key topics.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9bf49dd-0f8d-4c6b-a77a-be3fd1f7c987",
  "isSidechain": false,
  "requestId": "req_011CbSn7EmiocZxX38c8Bpcy",
  "type": "assistant",
  "uuid": "1f20173c-ae36-46e6-9aa8-3d89321502db",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CHcULTC9Bh4MwVQUvLEvzt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5274,
      "cache_read_input_tokens": 14184,
      "output_tokens": 202,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5274,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 202,
          "cache_read_input_tokens": 14184,
          "cache_creation_input_tokens": 5274,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5274
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

_source line 10 · 2026-05-27T08:44:01.563Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01DAt52GtDuYLsbXBcnw2YKj`</summary>

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
  "parentUuid": "1f20173c-ae36-46e6-9aa8-3d89321502db",
  "isSidechain": false,
  "requestId": "req_011CbSn7EmiocZxX38c8Bpcy",
  "type": "assistant",
  "uuid": "4743f26f-9c38-47e8-8705-34d2066f99a0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CHcULTC9Bh4MwVQUvLEvzt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5274,
      "cache_read_input_tokens": 14184,
      "output_tokens": 202,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5274,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 202,
          "cache_read_input_tokens": 14184,
          "cache_creation_input_tokens": 5274,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5274
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

_source line 11 · 2026-05-27T08:44:01.572Z_

<details><summary>↩ Tool result · `toolu_01DAt52GtDuYLsbXBcnw2YKj`</summary>

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
  "parentUuid": "4743f26f-9c38-47e8-8705-34d2066f99a0",
  "isSidechain": false,
  "promptId": "fbf4376b-8631-4eaa-a9bd-ce1f560c8253",
  "type": "user",
  "uuid": "8c07ba42-e2ee-4a5e-8ac8-5bb5d338e720",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "4743f26f-9c38-47e8-8705-34d2066f99a0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-27T08:44:04.461Z_

Now let me conduct the prerequisite literature research with multiple targeted searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c07ba42-e2ee-4a5e-8ac8-5bb5d338e720",
  "isSidechain": false,
  "requestId": "req_011CbSn7YL9f1LUxDJtzXZUw",
  "type": "assistant",
  "uuid": "3bddd27b-43b7-4216-ac3e-1a40f1346ef0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017nn3W9SCjWoYKBkTiGint6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 730,
      "cache_read_input_tokens": 19458,
      "output_tokens": 85,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 730,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 85,
          "cache_read_input_tokens": 19458,
          "cache_creation_input_tokens": 730,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 730
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

_source line 13 · 2026-05-27T08:44:04.826Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RPsx3i5kb9xdjHeKgb7FWX`</summary>

```json
{
  "query": "EVPV visual premise verification VLM process reward 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3bddd27b-43b7-4216-ac3e-1a40f1346ef0",
  "isSidechain": false,
  "requestId": "req_011CbSn7YL9f1LUxDJtzXZUw",
  "type": "assistant",
  "uuid": "608fd250-d7ea-4c53-8a07-cd4153534eb9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017nn3W9SCjWoYKBkTiGint6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 730,
      "cache_read_input_tokens": 19458,
      "output_tokens": 85,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 730,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 85,
          "cache_read_input_tokens": 19458,
          "cache_creation_input_tokens": 730,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 730
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

_source line 14 · 2026-05-27T08:44:12.557Z_

<details><summary>↩ Tool result · `toolu_01RPsx3i5kb9xdjHeKgb7FWX`</summary>

```text
Web search results for query: "EVPV visual premise verification VLM process reward 2026 arxiv"

Links: [{"title":"[2603.16253] Grounding the Score: Explicit Visual Premise Verification for Reliable Vision-Language Process Reward Models","url":"https://arxiv.org/abs/2603.16253"},{"title":"Grounding the Score: Explicit Visual Premise Verification for Reliable VLM Process Reward Models","url":"https://arxiv.org/html/2603.16253"},{"title":"Grounding the Score: Explicit Visual Premise Verification for Reliable Vision-Language Process Reward Models","url":"https://arxiv.org/pdf/2603.16253"},{"title":"GitHub - Qwen-Applications/EVPV-PRM · GitHub","url":"https://github.com/Qwen-Applications/EVPV-PRM"},{"title":"[2604.24583] Improving Vision-language Models with Perception-centric Process Reward Models","url":"https://arxiv.org/abs/2604.24583"}]

I found relevant results for your search. Here's what I discovered:

## EVPV: Explicit Visual Premise Verification

EVPV (Explicit Visual Premise Verification) is a lightweight verification interface that conditions step scoring on the reliability of the visual premises a step depends on.

**The Problem It Addresses:**
Vision-language process reward models often function as black-box judges where a low step score may reflect either a genuine reasoning mistake or the verifier's misperception of the image. This entanglement between perception and reasoning leads to systematic false positives (rewarding hallucinated visual premises) and false negatives (penalizing correct grounded statements).

**How It Works:**
The policy is prompted to produce a step-wise visual checklist that makes required visual facts explicit, while a constraint extractor independently derives structured visual constraints from the input image. EVPV matches checklist claims against these constraints to compute a scalar visual reliability signal, and calibrates PRM step rewards via reliability gating.

**Results:**
Experiments on VisualProcessBench and six multimodal reasoning benchmarks show that EVPV improves step-level verification and consistently boosts Best-of-N reranking accuracy over strong baselines.

The paper was published on arXiv on March 17, 2026 (arxiv ID: 2603.16253), and the code is available on GitHub through the Qwen-Applications/EVPV-PRM repository.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "608fd250-d7ea-4c53-8a07-cd4153534eb9",
  "isSidechain": false,
  "promptId": "fbf4376b-8631-4eaa-a9bd-ce1f560c8253",
  "type": "user",
  "uuid": "f32ef7cb-6431-49e1-b21d-38a5c7741a9d",
  "toolUseResult": {
    "query": "EVPV visual premise verification VLM process reward 2026 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_0116NHfF6iTsXAH8hdDyK95N",
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
            "title": "[2604.24583] Improving Vision-language Models with Perception-centric Process Reward Models",
            "url": "https://arxiv.org/abs/2604.24583"
          }
        ]
      },
      "I found relevant results for your search. Here's what I discovered:\n\n## EVPV: Explicit Visual Premise Verification\n\nEVPV (Explicit Visual Premise Verification) is a lightweight verification interface that conditions step scoring on the reliability of the visual premises a step depends on.\n\n**The Problem It Addresses:**\nVision-language process reward models often function as black-box judges where a low step score may reflect either a genuine reasoning mistake or the verifier's misperception of the image. This entanglement between perception and reasoning leads to systematic false positives (rewarding hallucinated visual premises) and false negatives (penalizing correct grounded statements).\n\n**How It Works:**\nThe policy is prompted to produce a step-wise visual checklist that makes required visual facts explicit, while a constraint extractor independently derives structured visual constraints from the input image. EVPV matches checklist claims against these constraints to compute a scalar visual reliability signal, and calibrates PRM step rewards via reliability gating.\n\n**Results:**\nExperiments on VisualProcessBench and six multimodal reasoning benchmarks show that EVPV improves step-level verification and consistently boosts Best-of-N reranking accuracy over strong baselines.\n\nThe paper was published on arXiv on March 17, 2026 (arxiv ID: 2603.16253), and the code is available on GitHub through the Qwen-Applications/EVPV-PRM repository."
    ],
    "durationSeconds": 7.727349813000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "608fd250-d7ea-4c53-8a07-cd4153534eb9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-27T08:44:15.407Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NXaMSeEed66wVsjWko9rpu`</summary>

```json
{
  "query": "Perception-R1 visual perception reward multimodal reasoning RL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f32ef7cb-6431-49e1-b21d-38a5c7741a9d",
  "isSidechain": false,
  "requestId": "req_011CbSn8M3mn8Nnkn2Es4sBq",
  "type": "assistant",
  "uuid": "9470079c-0ee8-49ef-930a-76a80cbe6ac7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016fXBYH5gmGbbbzoh8ojJu2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 701,
      "cache_read_input_tokens": 20188,
      "output_tokens": 172,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 701,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 172,
          "cache_read_input_tokens": 20188,
          "cache_creation_input_tokens": 701,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 701
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

_source line 16 · 2026-05-27T08:44:15.874Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EoT6JQMcKF1Xpza5ndcji7`</summary>

```json
{
  "query": "GeoDPO geometric perception VLM translator-guided reinforcement learning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9470079c-0ee8-49ef-930a-76a80cbe6ac7",
  "isSidechain": false,
  "requestId": "req_011CbSn8M3mn8Nnkn2Es4sBq",
  "type": "assistant",
  "uuid": "297092a6-bafe-427d-be0b-6d2619066c3d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016fXBYH5gmGbbbzoh8ojJu2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 701,
      "cache_read_input_tokens": 20188,
      "output_tokens": 172,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 701,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 172,
          "cache_read_input_tokens": 20188,
          "cache_creation_input_tokens": 701,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 701
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

_source line 17 · 2026-05-27T08:44:16.348Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KBai3vQ5XvjDVCU7pSP86a`</summary>

```json
{
  "query": "axiom consistency constraint satisfaction visual perception multimodal math 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "297092a6-bafe-427d-be0b-6d2619066c3d",
  "isSidechain": false,
  "requestId": "req_011CbSn8M3mn8Nnkn2Es4sBq",
  "type": "assistant",
  "uuid": "d9a88f9e-ff9f-46ce-b185-59e87a89d20f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016fXBYH5gmGbbbzoh8ojJu2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 701,
      "cache_read_input_tokens": 20188,
      "output_tokens": 172,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 701,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 172,
          "cache_read_input_tokens": 20188,
          "cache_creation_input_tokens": 701,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 701
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

_source line 18 · 2026-05-27T08:44:23.857Z_

<details><summary>↩ Tool result · `toolu_01KBai3vQ5XvjDVCU7pSP86a`</summary>

```text
Web search results for query: "axiom consistency constraint satisfaction visual perception multimodal math 2025 2026"

Links: [{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2506.06727"},{"title":"Perception-Consistency Multimodal Large Language Models Reasoning via Caption-Regularized Policy Optimization","url":"https://arxiv.org/pdf/2509.21854"},{"title":"Multi-task Visual Grounding with Coarse-to-Fine Consistency Constraints","url":"https://arxiv.org/pdf/2501.06710"},{"title":"Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward","url":"https://arxiv.org/pdf/2506.07218"},{"title":"Published at ICLR 2026 Workshop on Multimodal Intelligence","url":"https://openreview.net/pdf/ead1f59114888d4ea20e03b359a1d103493438ff.pdf"}]

I found several relevant research papers from 2025-2026 related to your search query. Here are the key results:

**Recent Research on Multimodal Math and Visual Perception (2025-2026):**

1. **Multimodal Math Benchmarks**: Recent studies like MMSciBench and SeePhys introduce the concept of "Vision-Essential" problems to reveal models' reliance on textual shortcuts, while VisAidMath explores active visual reasoning.

2. **Perception-Consistency in Multimodal Models**: A KL-based regularization explicitly aligns responses conditioned on images with those conditioned on captions, thereby enforcing perceptual consistency. Analysis indicates that perceptual errors constitute a primary source of reasoning failures in MLLMs.

3. **Visual Perception Rewards**: Perception-R1 introduces a novel visual perception reward that explicitly encourages MLLMs to perceive visual content accurately, thereby effectively incentivizing both their multimodal perception and reasoning capabilities.

4. **Consistency Constraints in Visual Grounding**: The C³VG architecture integrates implicit and explicit modeling approaches, with coarse predictions refined through a novel explicit bidirectional consistency constraint loss to ensure consistent representations across tasks.

5. **Unified Multimodal Models**: Hybrid MLLMs represent visual tokens with continuous embeddings and incorporate generative objectives such as diffusion or flow matching.

These papers represent cutting-edge work in combining visual perception, constraint satisfaction, and mathematical reasoning in multimodal AI systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d9a88f9e-ff9f-46ce-b185-59e87a89d20f",
  "isSidechain": false,
  "promptId": "fbf4376b-8631-4eaa-a9bd-ce1f560c8253",
  "type": "user",
  "uuid": "07f0de6c-b928-472f-abb4-cfd84ba1e57f",
  "toolUseResult": {
    "query": "axiom consistency constraint satisfaction visual perception multimodal math 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01STqxGNrRd9RebC47EgSXRr",
        "content": [
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://arxiv.org/pdf/2506.06727"
          },
          {
            "title": "Perception-Consistency Multimodal Large Language Models Reasoning via Caption-Regularized Policy Optimization",
            "url": "https://arxiv.org/pdf/2509.21854"
          },
          {
            "title": "Multi-task Visual Grounding with Coarse-to-Fine Consistency Constraints",
            "url": "https://arxiv.org/pdf/2501.06710"
          },
          {
            "title": "Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward",
            "url": "https://arxiv.org/pdf/2506.07218"
          },
          {
            "title": "Published at ICLR 2026 Workshop on Multimodal Intelligence",
            "url": "https://openreview.net/pdf/ead1f59114888d4ea20e03b359a1d103493438ff.pdf"
          }
        ]
      },
      "I found several relevant research papers from 2025-2026 related to your search query. Here are the key results:\n\n**Recent Research on Multimodal Math and Visual Perception (2025-2026):**\n\n1. **Multimodal Math Benchmarks**: Recent studies like MMSciBench and SeePhys introduce the concept of \"Vision-Essential\" problems to reveal models' reliance on textual shortcuts, while VisAidMath explores active visual reasoning.\n\n2. **Perception-Consistency in Multimodal Models**: A KL-based regularization explicitly aligns responses conditioned on images with those conditioned on captions, thereby enforcing perceptual consistency. Analysis indicates that perceptual errors constitute a primary source of reasoning failures in MLLMs.\n\n3. **Visual Perception Rewards**: Perception-R1 introduces a novel visual perception reward that explicitly encourages MLLMs to perceive visual content accurately, thereby effectively incentivizing both their multimodal perception and reasoning capabilities.\n\n4. **Consistency Constraints in Visual Grounding**: The C³VG architecture integrates implicit and explicit modeling approaches, with coarse predictions refined through a novel explicit bidirectional consistency constraint loss to ensure consistent representations across tasks.\n\n5. **Unified Multimodal Models**: Hybrid MLLMs represent visual tokens with continuous embeddings and incorporate generative objectives such as diffusion or flow matching.\n\nThese papers represent cutting-edge work in combining visual perception, constraint satisfaction, and mathematical reasoning in multimodal AI systems."
    ],
    "durationSeconds": 7.503723600999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d9a88f9e-ff9f-46ce-b185-59e87a89d20f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-27T08:44:24.711Z_

<details><summary>↩ Tool result · `toolu_01NXaMSeEed66wVsjWko9rpu`</summary>

```text
Web search results for query: "Perception-R1 visual perception reward multimodal reasoning RL 2025"

Links: [{"title":"[2506.07218] Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward","url":"https://arxiv.org/abs/2506.07218"},{"title":"Enhancing MLLM Reasoning with Visual Rewards","url":"https://www.emergentmind.com/papers/2506.07218"},{"title":"Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward","url":"https://arxiv.org/pdf/2506.07218"},{"title":"Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward","url":"https://arxiv.org/html/2506.07218v2"},{"title":"Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward [Quick Review]","url":"https://liner.com/review/perceptionr1-advancing-multimodal-reasoning-capabilities-of-mllms-via-visual-perception"},{"title":"Vision-SR1: Self-Rewarding Vision-Language Model via Reasoning Decomposition and Multi-Reward Policy Optimization","url":"https://arxiv.org/html/2508.19652"},{"title":"VTPERCEPTION-R1: ENHANCING MULTIMODAL ...","url":"https://openreview.net/pdf?id=UyAJQQPU4W"}]

Based on the search results, here's what I found about Perception-R1:

## Overview

Perception-R1 introduces a novel visual perception reward that explicitly encourages MLLMs to perceive the visual content accurately, thereby effectively incentivizing both their multimodal perception and reasoning capabilities.

## The Problem It Addresses

Existing RLVR methods largely overlook the enhancement of multimodal perception capabilities in MLLMs, which serve as a core prerequisite and foundational component of complex multimodal reasoning, and research shows that existing RLVR methods fail to effectively enhance the multimodal perception capabilities of MLLMs.

## How It Works

The method first collects textual visual annotations from the CoT trajectories of multimodal problems, which serve as visual references for reward assignment. During RLVR training, a judging LLM assesses the consistency between the visual annotations and the responses generated by MLLMs, and assigns the visual perception reward based on these consistency judgments.

## Results

Extensive experiments on several multimodal reasoning benchmarks demonstrate the effectiveness of Perception-R1, which achieves state-of-the-art performance on most benchmarks using only 1,442 training data.

The research was published in June 2025 and represents an advancement in applying reinforcement learning with verifiable rewards (RLVR) to multimodal reasoning tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9470079c-0ee8-49ef-930a-76a80cbe6ac7",
  "isSidechain": false,
  "promptId": "fbf4376b-8631-4eaa-a9bd-ce1f560c8253",
  "type": "user",
  "uuid": "83d26bca-f7be-434c-b862-30e03ec03a31",
  "toolUseResult": {
    "query": "Perception-R1 visual perception reward multimodal reasoning RL 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_011J6EuVwPfrvSUGqRBH4d6i",
        "content": [
          {
            "title": "[2506.07218] Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward",
            "url": "https://arxiv.org/abs/2506.07218"
          },
          {
            "title": "Enhancing MLLM Reasoning with Visual Rewards",
            "url": "https://www.emergentmind.com/papers/2506.07218"
          },
          {
            "title": "Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward",
            "url": "https://arxiv.org/pdf/2506.07218"
          },
          {
            "title": "Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward",
            "url": "https://arxiv.org/html/2506.07218v2"
          },
          {
            "title": "Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward [Quick Review]",
            "url": "https://liner.com/review/perceptionr1-advancing-multimodal-reasoning-capabilities-of-mllms-via-visual-perception"
          },
          {
            "title": "Vision-SR1: Self-Rewarding Vision-Language Model via Reasoning Decomposition and Multi-Reward Policy Optimization",
            "url": "https://arxiv.org/html/2508.19652"
          },
          {
            "title": "VTPERCEPTION-R1: ENHANCING MULTIMODAL ...",
            "url": "https://openreview.net/pdf?id=UyAJQQPU4W"
          }
        ]
      },
      "Based on the search results, here's what I found about Perception-R1:\n\n## Overview\n\nPerception-R1 introduces a novel visual perception reward that explicitly encourages MLLMs to perceive the visual content accurately, thereby effectively incentivizing both their multimodal perception and reasoning capabilities.\n\n## The Problem It Addresses\n\nExisting RLVR methods largely overlook the enhancement of multimodal perception capabilities in MLLMs, which serve as a core prerequisite and foundational component of complex multimodal reasoning, and research shows that existing RLVR methods fail to effectively enhance the multimodal perception capabilities of MLLMs.\n\n## How It Works\n\nThe method first collects textual visual annotations from the CoT trajectories of multimodal problems, which serve as visual references for reward assignment. During RLVR training, a judging LLM assesses the consistency between the visual annotations and the responses generated by MLLMs, and assigns the visual perception reward based on these consistency judgments.\n\n## Results\n\nExtensive experiments on several multimodal reasoning benchmarks demonstrate the effectiveness of Perception-R1, which achieves state-of-the-art performance on most benchmarks using only 1,442 training data.\n\nThe research was published in June 2025 and represents an advancement in applying reinforcement learning with verifiable rewards (RLVR) to multimodal reasoning tasks."
    ],
    "durationSeconds": 9.301189059999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "9470079c-0ee8-49ef-930a-76a80cbe6ac7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-27T08:44:26.351Z_

<details><summary>↩ Tool result · `toolu_01EoT6JQMcKF1Xpza5ndcji7`</summary>

```text
Web search results for query: "GeoDPO geometric perception VLM translator-guided reinforcement learning 2026"

Links: [{"title":"[2602.22703] Enhancing Geometric Perception in VLMs via Translator-Guided Reinforcement Learning","url":"https://arxiv.org/abs/2602.22703"},{"title":"Enhancing Geometric Perception in VLMs via Translator-Guided Reinforcement Learning","url":"https://arxiv.org/pdf/2602.22703"},{"title":"Enhancing Geometric Perception in VLMs via Translator-Guided Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=O70LkLl3gW"},{"title":"GitHub - majianz/dl4gps: [ACL 2026 Main Conference] Paper list for the survey \"A Survey of Deep Learning for Geometry Problem Solving\" · GitHub","url":"https://github.com/majianz/dl4gps"},{"title":"Geo-R1: Unlocking VLM Geospatial Reasoning with Cross-View Reinforcement Learning","url":"https://arxiv.org/pdf/2510.00072"}]

I found relevant information about GeoDPO. Here are the search results:

## GeoDPO: Enhancing Geometric Perception in VLMs

Vision-language models (VLMs) often struggle with geometric reasoning due to their limited perception of fundamental diagram elements. To address this, researchers introduced GeoPerceive, a benchmark comprising diagram instances paired with domain-specific language (DSL) representations, along with an efficient automatic data generation pipeline.

GeoDPO is a translator-guided reinforcement learning (RL) framework designed to enhance the geometric perception capabilities of VLMs. GeoDPO employs an NL-to-DSL translator, which is trained on synthetic pairs generated by the data engine of GeoPerceive, to bridge natural language and DSL. This translator facilitates the computation of fine-grained, DSL-level scores, which serve as reward signals in reinforcement learning.

## Key Results

Experimental results demonstrate that GeoDPO achieves substantial gains: +26.5% on in-domain data, +8.0% on out-of-domain data, and +39.0% on downstream reasoning tasks. These findings underscore the superior performance and generalization ability of GeoDPO over supervised fine-tuning (SFT).

The paper was published on February 26, 2026, and the code has been made publicly available on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "297092a6-bafe-427d-be0b-6d2619066c3d",
  "isSidechain": false,
  "promptId": "fbf4376b-8631-4eaa-a9bd-ce1f560c8253",
  "type": "user",
  "uuid": "424b0fa0-175c-42c8-be18-8d47d4537076",
  "toolUseResult": {
    "query": "GeoDPO geometric perception VLM translator-guided reinforcement learning 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_017pEm6oGkzKhJo1kSXhjEba",
        "content": [
          {
            "title": "[2602.22703] Enhancing Geometric Perception in VLMs via Translator-Guided Reinforcement Learning",
            "url": "https://arxiv.org/abs/2602.22703"
          },
          {
            "title": "Enhancing Geometric Perception in VLMs via Translator-Guided Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2602.22703"
          },
          {
            "title": "Enhancing Geometric Perception in VLMs via Translator-Guided Reinforcement Learning | OpenReview",
            "url": "https://openreview.net/forum?id=O70LkLl3gW"
          },
          {
            "title": "GitHub - majianz/dl4gps: [ACL 2026 Main Conference] Paper list for the survey \"A Survey of Deep Learning for Geometry Problem Solving\" · GitHub",
            "url": "https://github.com/majianz/dl4gps"
          },
          {
            "title": "Geo-R1: Unlocking VLM Geospatial Reasoning with Cross-View Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2510.00072"
          }
        ]
      },
      "I found relevant information about GeoDPO. Here are the search results:\n\n## GeoDPO: Enhancing Geometric Perception in VLMs\n\nVision-language models (VLMs) often struggle with geometric reasoning due to their limited perception of fundamental diagram elements. To address this, researchers introduced GeoPerceive, a benchmark comprising diagram instances paired with domain-specific language (DSL) representations, along with an efficient automatic data generation pipeline.\n\nGeoDPO is a translator-guided reinforcement learning (RL) framework designed to enhance the geometric perception capabilities of VLMs. GeoDPO employs an NL-to-DSL translator, which is trained on synthetic pairs generated by the data engine of GeoPerceive, to bridge natural language and DSL. This translator facilitates the computation of fine-grained, DSL-level scores, which serve as reward signals in reinforcement learning.\n\n## Key Results\n\nExperimental results demonstrate that GeoDPO achieves substantial gains: +26.5% on in-domain data, +8.0% on out-of-domain data, and +39.0% on downstream reasoning tasks. These findings underscore the superior performance and generalization ability of GeoDPO over supervised fine-tuning (SFT).\n\nThe paper was published on February 26, 2026, and the code has been made publicly available on GitHub."
    ],
    "durationSeconds": 10.474010181999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "297092a6-bafe-427d-be0b-6d2619066c3d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c",
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
  "lastPrompt": "# Axiom-Grounded Self-Verified Perception for Visual Math Reasoning  ## Core Problem and Thesis  Current multimodal math reasoning systems verify perceived visual facts independently—checking each cla…",
  "leafUuid": "424b0fa0-175c-42c8-be18-8d47d4537076",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Axiom-grounded self-verified visual math reasoning",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c"
}
```

---

### Tool call

_source line 23 · 2026-05-27T08:44:29.343Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FM94XeT7bAdL1YcYb8xcKs`</summary>

```json
{
  "query": "PEARL perceptual evidence anchored reinforced learning multimodal reasoning 2025 MathVerse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "424b0fa0-175c-42c8-be18-8d47d4537076",
  "isSidechain": false,
  "requestId": "req_011CbSn9NLCQca4rEnY5ux1x",
  "type": "assistant",
  "uuid": "5f67b952-d07b-49d5-a567-93c3429b5684",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JvzSSA8YMmJg3u4dbbVjbe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 642,
      "cache_creation_input_tokens": 1551,
      "cache_read_input_tokens": 20889,
      "output_tokens": 179,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1551,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 642,
          "output_tokens": 179,
          "cache_read_input_tokens": 20889,
          "cache_creation_input_tokens": 1551,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1551
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

_source line 24 · 2026-05-27T08:44:30.275Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01X1CUvzkrrDAdkmbKFDC4d5`</summary>

```json
{
  "query": "Geoparsing diagram parsing formal language geometry 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f67b952-d07b-49d5-a567-93c3429b5684",
  "isSidechain": false,
  "requestId": "req_011CbSn9NLCQca4rEnY5ux1x",
  "type": "assistant",
  "uuid": "fd845073-2877-45e0-be43-0f3071a90884",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JvzSSA8YMmJg3u4dbbVjbe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 642,
      "cache_creation_input_tokens": 1551,
      "cache_read_input_tokens": 20889,
      "output_tokens": 179,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1551,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 642,
          "output_tokens": 179,
          "cache_read_input_tokens": 20889,
          "cache_creation_input_tokens": 1551,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1551
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

_source line 25 · 2026-05-27T08:44:31.037Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GDee7v31CGgeMNZJB7mERa`</summary>

```json
{
  "query": "self-supervised reward signal RL VLM perception training mathematical constraint verification 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd845073-2877-45e0-be43-0f3071a90884",
  "isSidechain": false,
  "requestId": "req_011CbSn9NLCQca4rEnY5ux1x",
  "type": "assistant",
  "uuid": "6cb8f39c-1461-4261-9b78-663f8dd4b7a8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JvzSSA8YMmJg3u4dbbVjbe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 642,
      "cache_creation_input_tokens": 1551,
      "cache_read_input_tokens": 20889,
      "output_tokens": 179,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1551,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 642,
          "output_tokens": 179,
          "cache_read_input_tokens": 20889,
          "cache_creation_input_tokens": 1551,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1551
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

_source line 26 · 2026-05-27T08:44:39.111Z_

<details><summary>↩ Tool result · `toolu_01X1CUvzkrrDAdkmbKFDC4d5`</summary>

```text
Web search results for query: "Geoparsing diagram parsing formal language geometry 2026 arxiv"

Links: [{"title":"[2604.11600] Geoparsing: Diagram Parsing for Plane and Solid Geometry with a Unified Formal Language","url":"https://arxiv.org/abs/2604.11600"},{"title":"Geoparsing: Diagram Parsing for Plane and Solid Geometry with a Unified Formal Language","url":"https://arxiv.org/html/2604.11600"},{"title":"GeoLoom: High-quality Geometric Diagram Generation from Textual Input","url":"https://arxiv.org/html/2512.08180v1"},{"title":"A Survey of Deep Learning for Geometry Problem Solving","url":"https://arxiv.org/html/2507.11936v5"},{"title":"GitHub - majianz/dl4gps: [ACL 2026 Main Conference] Paper list for the survey \"A Survey of Deep Learning for Geometry Problem Solving\" · GitHub","url":"https://github.com/majianz/dl4gps"},{"title":"GeoLoom: High-quality Geometric Diagram Generation from Textual Input","url":"https://arxiv.org/pdf/2512.08180"},{"title":"[2512.08180] GeoLoom: High-quality Geometric Diagram Generation from Textual Input","url":"https://arxiv.org/abs/2512.08180"},{"title":"Inter-GPS: Interpretable Geometry Problem Solving with Formal Language   and Symbolic Reasoning","url":"https://arxiv.org/pdf/2105.04165"}]

I found relevant search results for your query. Here's what I discovered:

The most directly relevant result is a paper that designs a unified formal language integrating plane and solid geometry, comprehensively covering geometric structures and semantic relations. 

The researchers constructed GDP-29K, a large-scale dataset comprising 20k plane and 9k solid geometry samples collected from diverse real-world sources, each paired with its ground-truth formal description. To ensure syntactic correctness and geometric consistency, they propose a training paradigm that combines Supervised Fine-Tuning with Reinforcement Learning via Verifiable Rewards.

The parsed formal descriptions serve as a critical cognitive scaffold, significantly boosting MLLMs' capabilities for downstream geometry reasoning tasks.

This paper was published on arXiv on April 13, 2026 (arXiv:2604.11600), and addresses the challenge of Multimodal Large Language Models struggling with geometric reasoning due to perception issues with fine-grained visual elements, particularly in solid geometry which requires spatial understanding.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fd845073-2877-45e0-be43-0f3071a90884",
  "isSidechain": false,
  "promptId": "fbf4376b-8631-4eaa-a9bd-ce1f560c8253",
  "type": "user",
  "uuid": "86e08cc0-512e-45df-bdb0-21ca94ef8b35",
  "toolUseResult": {
    "query": "Geoparsing diagram parsing formal language geometry 2026 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_019cSFyanod6KLL5H81bfh7P",
        "content": [
          {
            "title": "[2604.11600] Geoparsing: Diagram Parsing for Plane and Solid Geometry with a Unified Formal Language",
            "url": "https://arxiv.org/abs/2604.11600"
          },
          {
            "title": "Geoparsing: Diagram Parsing for Plane and Solid Geometry with a Unified Formal Language",
            "url": "https://arxiv.org/html/2604.11600"
          },
          {
            "title": "GeoLoom: High-quality Geometric Diagram Generation from Textual Input",
            "url": "https://arxiv.org/html/2512.08180v1"
          },
          {
            "title": "A Survey of Deep Learning for Geometry Problem Solving",
            "url": "https://arxiv.org/html/2507.11936v5"
          },
          {
            "title": "GitHub - majianz/dl4gps: [ACL 2026 Main Conference] Paper list for the survey \"A Survey of Deep Learning for Geometry Problem Solving\" · GitHub",
            "url": "https://github.com/majianz/dl4gps"
          },
          {
            "title": "GeoLoom: High-quality Geometric Diagram Generation from Textual Input",
            "url": "https://arxiv.org/pdf/2512.08180"
          },
          {
            "title": "[2512.08180] GeoLoom: High-quality Geometric Diagram Generation from Textual Input",
            "url": "https://arxiv.org/abs/2512.08180"
          },
          {
            "title": "Inter-GPS: Interpretable Geometry Problem Solving with Formal Language   and Symbolic Reasoning",
            "url": "https://arxiv.org/pdf/2105.04165"
          }
        ]
      },
      "I found relevant search results for your query. Here's what I discovered:\n\nThe most directly relevant result is a paper that designs a unified formal language integrating plane and solid geometry, comprehensively covering geometric structures and semantic relations. \n\nThe researchers constructed GDP-29K, a large-scale dataset comprising 20k plane and 9k solid geometry samples collected from diverse real-world sources, each paired with its ground-truth formal description. To ensure syntactic correctness and geometric consistency, they propose a training paradigm that combines Supervised Fine-Tuning with Reinforcement Learning via Verifiable Rewards.\n\nThe parsed formal descriptions serve as a critical cognitive scaffold, significantly boosting MLLMs' capabilities for downstream geometry reasoning tasks.\n\nThis paper was published on arXiv on April 13, 2026 (arXiv:2604.11600), and addresses the challenge of Multimodal Large Language Models struggling with geometric reasoning due to perception issues with fine-grained visual elements, particularly in solid geometry which requires spatial understanding."
    ],
    "durationSeconds": 8.832365977000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "fd845073-2877-45e0-be43-0f3071a90884",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-27T08:44:39.182Z_

<details><summary>↩ Tool result · `toolu_01FM94XeT7bAdL1YcYb8xcKs`</summary>

```text
Web search results for query: "PEARL perceptual evidence anchored reinforced learning multimodal reasoning 2025 MathVerse"

Links: [{"title":"[2511.18437] Perceptual-Evidence Anchored Reinforced Learning for Multimodal Reasoning","url":"https://arxiv.org/abs/2511.18437"},{"title":"Perceptual-Evidence Anchored Reinforced Learning for Multimodal Reasoning","url":"https://arxiv.org/pdf/2511.18437"},{"title":"Perceptual-Evidence Anchored Reinforced Learning for Multimodal Reasoning","url":"https://arxiv.org/html/2511.18437"},{"title":"Seeing with You: Perception–Reasoning Coevolution for Multimodal Reasoning","url":"https://arxiv.org/html/2603.28618v1"},{"title":"GitHub - MiliLab/PEARL: Official repository for [CVPR 2026] \"Perceptual-Evidence Anchored Reinforced Learning for Multimodal Reasoning\" · GitHub","url":"https://github.com/MiliLab/PEARL"}]

I found relevant results for your search. Here's what I found:

PEARL (Perceptual-Evidence Anchored Reinforced Learning) is a dual-branch, perception-reasoning synergistic approach that strengthens multimodal reasoning by explicitly anchoring it to verified visual evidence.

**Key Features:**

For each reasoning-oriented QA instance, PEARL derives a perception checklist—a set of perception-oriented sub-questions with verifiable answers that probe the model's understanding of key visual evidence. During training, auxiliary rollouts on this checklist yield a perceptual reward that both directly reinforces the model's perception ability and acts as a fidelity gate for reasoning.

If the model passes the perception check, its policy update is biased towards evidence-anchored reasoning. Otherwise, the process is halted to prevent reasoning from flawed premises.

**Performance:**

PEARL achieves substantial gains on multimodal reasoning benchmarks, e.g., a +9.7% improvement over the baseline and +6.6% over GRPO on MathVerse.

PEARL can be seamlessly integrated with popular RL methods like GRPO and DAPO.

The paper was posted on arXiv on November 23, 2025, and is from researchers at Wuhan University, Meituan Inc, and The University of Sydney.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5f67b952-d07b-49d5-a567-93c3429b5684",
  "isSidechain": false,
  "promptId": "fbf4376b-8631-4eaa-a9bd-ce1f560c8253",
  "type": "user",
  "uuid": "184ad531-7c54-49b5-aa15-b238ac2f8996",
  "toolUseResult": {
    "query": "PEARL perceptual evidence anchored reinforced learning multimodal reasoning 2025 MathVerse",
    "results": [
      {
        "tool_use_id": "srvtoolu_01E2KTqBRFjhRfUukELsytyx",
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
      "I found relevant results for your search. Here's what I found:\n\nPEARL (Perceptual-Evidence Anchored Reinforced Learning) is a dual-branch, perception-reasoning synergistic approach that strengthens multimodal reasoning by explicitly anchoring it to verified visual evidence.\n\n**Key Features:**\n\nFor each reasoning-oriented QA instance, PEARL derives a perception checklist—a set of perception-oriented sub-questions with verifiable answers that probe the model's understanding of key visual evidence. During training, auxiliary rollouts on this checklist yield a perceptual reward that both directly reinforces the model's perception ability and acts as a fidelity gate for reasoning.\n\nIf the model passes the perception check, its policy update is biased towards evidence-anchored reasoning. Otherwise, the process is halted to prevent reasoning from flawed premises.\n\n**Performance:**\n\nPEARL achieves substantial gains on multimodal reasoning benchmarks, e.g., a +9.7% improvement over the baseline and +6.6% over GRPO on MathVerse.\n\nPEARL can be seamlessly integrated with popular RL methods like GRPO and DAPO.\n\nThe paper was posted on arXiv on November 23, 2025, and is from researchers at Wuhan University, Meituan Inc, and The University of Sydney."
    ],
    "durationSeconds": 9.833974876000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "5f67b952-d07b-49d5-a567-93c3429b5684",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-27T08:44:39.832Z_

<details><summary>↩ Tool result · `toolu_01GDee7v31CGgeMNZJB7mERa`</summary>

```text
Web search results for query: "self-supervised reward signal RL VLM perception training mathematical constraint verification 2025 2026"

Links: [{"title":"Self-Rewarding Vision-Language Model via Reasoning Decomposition","url":"https://arxiv.org/html/2508.19652v1"},{"title":"Self-Supervised RL with Verifiable Rewards","url":"https://www.emergentmind.com/topics/self-supervised-reinforcement-learning-with-verifiable-rewards-rlvr"},{"title":"One RL to See Them All","url":"https://arxiv.org/pdf/2505.18129"},{"title":"Reinforcement Learning with Verified Rewards (RLVR)","url":"https://www.emergentmind.com/topics/reinforcement-learning-with-verified-rewards-rlvr"},{"title":"Self-Rewarding Vision-Language Model via Reasoning Decomposition","url":"https://arxiv.org/pdf/2508.19652"},{"title":"Masked-and-Reordered Self-Supervision for Reinforcement Learning from Verifiable Rewards","url":"https://arxiv.org/pdf/2511.17473"},{"title":"Aha Moment Revisited: Are VLMs Truly Capable of Self Verification in Inference-time Scaling?","url":"https://arxiv.org/pdf/2506.17417"}]

I found several relevant research papers and resources on this topic. Here are the key findings from the web search:

## Self-Supervised Reward Signals in VLM-Based RL

Recent RL methods have been shown to improve the reasoning abilities of VLMs across diverse tasks, though there are notable challenges. These methods often encourage "thinking over seeing" that lean heavily on language reasoning while underutilize visual perception, and this imbalance makes VLMs susceptible to reward hacking and spurious effects.

## Mathematical Constraint Verification

Verifiable rewards obtained by programmatically checking final answers or executing unit tests offer a practical solution, where whether a model output satisfies predefined symbolic or numeric constraints can often be determined automatically. Recent work proposes MR-RLVR (Masked-and-Reordered RLVR), which constructs process-level self-supervised rewards via "masked-then-fill" and "step reordering" to extract learnable signals from intermediate reasoning.

## Vision-Language Domain Applications

In remote sensing, few-shot RLVR using only lightweight rule-based rewards enables specialist VLMs to learn from as little as a single example, and in robotic manipulation, dense geometric and format-based RLVR rewards enable spatial generalization and out-of-domain transfer.

## Broader Multimodal RL Efforts

A stable methodology for scaling RL across heterogeneous visual tasks remains an important open problem for VLMs, with challenges lying in handling both capability heterogeneity and verification heterogeneity, covering both reasoning-heavy and perception-heavy tasks while their outcomes may require symbolic checking or continuous spatial feedback.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6cb8f39c-1461-4261-9b78-663f8dd4b7a8",
  "isSidechain": false,
  "promptId": "fbf4376b-8631-4eaa-a9bd-ce1f560c8253",
  "type": "user",
  "uuid": "5e41e298-226e-4e1c-a7a1-66a9241300db",
  "toolUseResult": {
    "query": "self-supervised reward signal RL VLM perception training mathematical constraint verification 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_013BLoHUR46LKz1GbDHZAZHt",
        "content": [
          {
            "title": "Self-Rewarding Vision-Language Model via Reasoning Decomposition",
            "url": "https://arxiv.org/html/2508.19652v1"
          },
          {
            "title": "Self-Supervised RL with Verifiable Rewards",
            "url": "https://www.emergentmind.com/topics/self-supervised-reinforcement-learning-with-verifiable-rewards-rlvr"
          },
          {
            "title": "One RL to See Them All",
            "url": "https://arxiv.org/pdf/2505.18129"
          },
          {
            "title": "Reinforcement Learning with Verified Rewards (RLVR)",
            "url": "https://www.emergentmind.com/topics/reinforcement-learning-with-verified-rewards-rlvr"
          },
          {
            "title": "Self-Rewarding Vision-Language Model via Reasoning Decomposition",
            "url": "https://arxiv.org/pdf/2508.19652"
          },
          {
            "title": "Masked-and-Reordered Self-Supervision for Reinforcement Learning from Verifiable Rewards",
            "url": "https://arxiv.org/pdf/2511.17473"
          },
          {
            "title": "Aha Moment Revisited: Are VLMs Truly Capable of Self Verification in Inference-time Scaling?",
            "url": "https://arxiv.org/pdf/2506.17417"
          }
        ]
      },
      "I found several relevant research papers and resources on this topic. Here are the key findings from the web search:\n\n## Self-Supervised Reward Signals in VLM-Based RL\n\nRecent RL methods have been shown to improve the reasoning abilities of VLMs across diverse tasks, though there are notable challenges. These methods often encourage \"thinking over seeing\" that lean heavily on language reasoning while underutilize visual perception, and this imbalance makes VLMs susceptible to reward hacking and spurious effects.\n\n## Mathematical Constraint Verification\n\nVerifiable rewards obtained by programmatically checking final answers or executing unit tests offer a practical solution, where whether a model output satisfies predefined symbolic or numeric constraints can often be determined automatically. Recent work proposes MR-RLVR (Masked-and-Reordered RLVR), which constructs process-level self-supervised rewards via \"masked-then-fill\" and \"step reordering\" to extract learnable signals from intermediate reasoning.\n\n## Vision-Language Domain Applications\n\nIn remote sensing, few-shot RLVR using only lightweight rule-based rewards enables specialist VLMs to learn from as little as a single example, and in robotic manipulation, dense geometric and format-based RLVR rewards enable spatial generalization and out-of-domain transfer.\n\n## Broader Multimodal RL Efforts\n\nA stable methodology for scaling RL across heterogeneous visual tasks remains an important open problem for VLMs, with challenges lying in handling both capability heterogeneity and verification heterogeneity, covering both reasoning-heavy and perception-heavy tasks while their outcomes may require symbolic checking or continuous spatial feedback."
    ],
    "durationSeconds": 8.792327674000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "6cb8f39c-1461-4261-9b78-663f8dd4b7a8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-27T08:44:39.842Z_

```json
{
  "parentUuid": "5e41e298-226e-4e1c-a7a1-66a9241300db",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "7f1eeada-6660-4cb9-94ba-406d08a4b130",
  "timestamp": "2026-05-27T08:44:39.842Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 30 · 2026-05-27T08:44:42.514Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CMd1iKsnHjygrJRNzEf3zo`</summary>

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
  "parentUuid": "7f1eeada-6660-4cb9-94ba-406d08a4b130",
  "isSidechain": false,
  "requestId": "req_011CbSnAMi27UEmu6xWZB3nR",
  "type": "assistant",
  "uuid": "e6da15f2-36a8-4507-812e-8938df6ac69f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EtvT4PovfhqXQCtTWuAjPp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2956,
      "cache_read_input_tokens": 22440,
      "output_tokens": 180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2956,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 180,
          "cache_read_input_tokens": 22440,
          "cache_creation_input_tokens": 2956,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2956
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

_source line 31 · 2026-05-27T08:44:43.447Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011cCbdssUnVRaAoGHnuu6jB`</summary>

```json
{
  "query": "PRCO perception reasoning coevolution observer solver multimodal reasoning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e6da15f2-36a8-4507-812e-8938df6ac69f",
  "isSidechain": false,
  "requestId": "req_011CbSnAMi27UEmu6xWZB3nR",
  "type": "assistant",
  "uuid": "ffc279cd-8174-48fa-aeb7-93c993b00f93",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EtvT4PovfhqXQCtTWuAjPp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2956,
      "cache_read_input_tokens": 22440,
      "output_tokens": 180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2956,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 180,
          "cache_read_input_tokens": 22440,
          "cache_creation_input_tokens": 2956,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2956
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

_source line 32 · 2026-05-27T08:44:44.501Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TZNuxu7n1FS3qSwSYhPi6p`</summary>

```json
{
  "query": "formal geometry constraint solver reward RL training FGeo-DRL formalgeo 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ffc279cd-8174-48fa-aeb7-93c993b00f93",
  "isSidechain": false,
  "requestId": "req_011CbSnAMi27UEmu6xWZB3nR",
  "type": "assistant",
  "uuid": "79f07f53-b53b-4717-9613-a5b5f0abb54b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EtvT4PovfhqXQCtTWuAjPp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2956,
      "cache_read_input_tokens": 22440,
      "output_tokens": 180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2956,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 180,
          "cache_read_input_tokens": 22440,
          "cache_creation_input_tokens": 2956,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2956
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

_source line 33 · 2026-05-27T08:44:48.636Z_

<details><summary>↩ Tool result · `toolu_01CMd1iKsnHjygrJRNzEf3zo`</summary>

```text
Web search results for query: "SSL-R1 self-supervised visual reinforcement post-training MLLM 2026"

Links: [{"title":"[2604.20705] SSL-R1: Self-Supervised Visual Reinforcement Post-Training for Multimodal Large Language Models","url":"https://arxiv.org/abs/2604.20705"},{"title":"SSL-R1: Self-Supervised Visual Reinforcement Post-Training for Multimodal Large Language Models","url":"https://arxiv.org/html/2604.20705"},{"title":"GitHub - smiles724/Awesome-LLM-RLVR: Collection of latest papers and materials in the area of RLVR! · GitHub","url":"https://github.com/smiles724/Awesome-LLM-RLVR"},{"title":"ViSS-R1: Self-Supervised Reinforcement Video Reasoning","url":"https://arxiv.org/html/2511.13054"},{"title":"Visual Jigsaw Post-Training Improves MLLMs","url":"https://arxiv.org/pdf/2509.25190"},{"title":"ViSS-R1: Self-Supervised Reinforcement Video Reasoning","url":"https://arxiv.org/pdf/2511.13054"}]

Based on the search results, here's what I found about SSL-R1:

## SSL-R1: Self-Supervised Visual Reinforcement Post-Training for Multimodal Large Language Models

SSL-R1 is a generic self-supervised RL framework that derives verifiable rewards directly from images. It addresses the limitation that the reliance on language-centric priors and expensive manual annotations prevents MLLMs' intrinsic visual understanding and scalable reward designs.

**Key Features:**

The framework revisits self-supervised learning in visual domains and reformulates widely-used SSL tasks into a set of verifiable visual puzzles for RL post-training, requiring neither human nor external model supervision. SSL-R1 is vision-centric, cost-effective, scalable, and consistently improves Qwen2.5-VL on 13 vision-centric multimodal benchmarks, spanning fine-grained perception, spatial understanding, and compositional understanding.

**Results:**

Training MLLMs on these tasks substantially improves their performance on multimodal understanding and reasoning benchmarks, highlighting the potential of leveraging vision-centric self-supervised tasks for MLLM post-training.

The paper was published on April 22, 2026, on arXiv and represents recent work in the field of reinforcement learning with verifiable rewards (RLVR) for multimodal large language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e6da15f2-36a8-4507-812e-8938df6ac69f",
  "isSidechain": false,
  "promptId": "fbf4376b-8631-4eaa-a9bd-ce1f560c8253",
  "type": "user",
  "uuid": "b1cdd420-59f8-4dee-a232-451a9ee95521",
  "toolUseResult": {
    "query": "SSL-R1 self-supervised visual reinforcement post-training MLLM 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01ApQabtE5piZy8SpJGhmksP",
        "content": [
          {
            "title": "[2604.20705] SSL-R1: Self-Supervised Visual Reinforcement Post-Training for Multimodal Large Language Models",
            "url": "https://arxiv.org/abs/2604.20705"
          },
          {
            "title": "SSL-R1: Self-Supervised Visual Reinforcement Post-Training for Multimodal Large Language Models",
            "url": "https://arxiv.org/html/2604.20705"
          },
          {
            "title": "GitHub - smiles724/Awesome-LLM-RLVR: Collection of latest papers and materials in the area of RLVR! · GitHub",
            "url": "https://github.com/smiles724/Awesome-LLM-RLVR"
          },
          {
            "title": "ViSS-R1: Self-Supervised Reinforcement Video Reasoning",
            "url": "https://arxiv.org/html/2511.13054"
          },
          {
            "title": "Visual Jigsaw Post-Training Improves MLLMs",
            "url": "https://arxiv.org/pdf/2509.25190"
          },
          {
            "title": "ViSS-R1: Self-Supervised Reinforcement Video Reasoning",
            "url": "https://arxiv.org/pdf/2511.13054"
          }
        ]
      },
      "Based on the search results, here's what I found about SSL-R1:\n\n## SSL-R1: Self-Supervised Visual Reinforcement Post-Training for Multimodal Large Language Models\n\nSSL-R1 is a generic self-supervised RL framework that derives verifiable rewards directly from images. It addresses the limitation that the reliance on language-centric priors and expensive manual annotations prevents MLLMs' intrinsic visual understanding and scalable reward designs.\n\n**Key Features:**\n\nThe framework revisits self-supervised learning in visual domains and reformulates widely-used SSL tasks into a set of verifiable visual puzzles for RL post-training, requiring neither human nor external model supervision. SSL-R1 is vision-centric, cost-effective, scalable, and consistently improves Qwen2.5-VL on 13 vision-centric multimodal benchmarks, spanning fine-grained perception, spatial understanding, and compositional understanding.\n\n**Results:**\n\nTraining MLLMs on these tasks substantially improves their performance on multimodal understanding and reasoning benchmarks, highlighting the potential of leveraging vision-centric self-supervised tasks for MLLM post-training.\n\nThe paper was published on April 22, 2026, on arXiv and represents recent work in the field of reinforcement learning with verifiable rewards (RLVR) for multimodal large language models."
    ],
    "durationSeconds": 6.1178544069999985,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e6da15f2-36a8-4507-812e-8938df6ac69f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-27T08:44:49.822Z_

<details><summary>↩ Tool result · `toolu_011cCbdssUnVRaAoGHnuu6jB`</summary>

```text
Web search results for query: "PRCO perception reasoning coevolution observer solver multimodal reasoning 2026"

Links: [{"title":"[2603.28618] Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning","url":"https://arxiv.org/abs/2603.28618"},{"title":"Seeing with You: Perception–Reasoning Coevolution for Multimodal Reasoning","url":"https://arxiv.org/html/2603.28618v1"},{"title":"Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning","url":"https://chatpaper.com/paper/262369"},{"title":"Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning","url":"https://arxiv.org/pdf/2603.28618"},{"title":"Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning | Takara TLDR","url":"https://tldr.takara.ai/p/2603.28618"},{"title":"Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning | Request PDF","url":"https://www.researchgate.net/publication/403307388_Seeing_with_You_Perception-Reasoning_Coevolution_for_Multimodal_Reasoning"}]

I found relevant results for your search query. Here's what I found:

## PRCO: Perception-Reasoning Coevolution for Multimodal Reasoning

PRCO (Perception-Reasoning Coevolution) is a dual-role reinforcement learning with verifiable rewards (RLVR) framework with a shared policy.

**Framework Components:**

PRCO consists of two cooperative roles: an Observer that generates an evidence caption tailored to the question and a Solver that predicts the final answer based on this caption.

**Reward Signals:**

The Solver is optimized using verifiable outcome rewards on the final answer, while the Observer receives a utility reward derived from the Solver's downstream success.

**Problem It Addresses:**

Existing RLVR approaches typically rely on outcome-driven optimization that updates both perception and reasoning using a shared reward based solely on the final answer, which blurs credit assignment and frequently improves reasoning patterns while failing to reliably enhance the accuracy of upstream visual evidence extraction.

**Performance Results:**

Extensive experiments across eight challenging multimodal reasoning benchmarks demonstrate that PRCO yields consistent improvements across model scales by over 7 points on average accuracy compared to the base model, outperforming prior open-source RL-tuned baselines.

The research paper was published on arXiv in March/April 2026 with the title "Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning."


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ffc279cd-8174-48fa-aeb7-93c993b00f93",
  "isSidechain": false,
  "promptId": "fbf4376b-8631-4eaa-a9bd-ce1f560c8253",
  "type": "user",
  "uuid": "e608826d-89db-406c-a5ae-108635d26126",
  "toolUseResult": {
    "query": "PRCO perception reasoning coevolution observer solver multimodal reasoning 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Uwv9qsaARda1R23WkzHd9X",
        "content": [
          {
            "title": "[2603.28618] Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning",
            "url": "https://arxiv.org/abs/2603.28618"
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
      "I found relevant results for your search query. Here's what I found:\n\n## PRCO: Perception-Reasoning Coevolution for Multimodal Reasoning\n\nPRCO (Perception-Reasoning Coevolution) is a dual-role reinforcement learning with verifiable rewards (RLVR) framework with a shared policy.\n\n**Framework Components:**\n\nPRCO consists of two cooperative roles: an Observer that generates an evidence caption tailored to the question and a Solver that predicts the final answer based on this caption.\n\n**Reward Signals:**\n\nThe Solver is optimized using verifiable outcome rewards on the final answer, while the Observer receives a utility reward derived from the Solver's downstream success.\n\n**Problem It Addresses:**\n\nExisting RLVR approaches typically rely on outcome-driven optimization that updates both perception and reasoning using a shared reward based solely on the final answer, which blurs credit assignment and frequently improves reasoning patterns while failing to reliably enhance the accuracy of upstream visual evidence extraction.\n\n**Performance Results:**\n\nExtensive experiments across eight challenging multimodal reasoning benchmarks demonstrate that PRCO yields consistent improvements across model scales by over 7 points on average accuracy compared to the base model, outperforming prior open-source RL-tuned baselines.\n\nThe research paper was published on arXiv in March/April 2026 with the title \"Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning.\""
    ],
    "durationSeconds": 6.372180185999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "ffc279cd-8174-48fa-aeb7-93c993b00f93",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 35_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Axiom-Grounded Self-Verified Perception for Visual Math Reasoning  ## Core Problem and Thesis  Current multimodal math reasoning systems verify perceived visual facts independently—checking each cla…",
  "leafUuid": "e608826d-89db-406c-a5ae-108635d26126",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Axiom-grounded self-verified visual math reasoning",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c"
}
```

---

### Tool result

_source line 37 · 2026-05-27T08:44:51.981Z_

<details><summary>↩ Tool result · `toolu_01TZNuxu7n1FS3qSwSYhPi6p`</summary>

```text
Web search results for query: "formal geometry constraint solver reward RL training FGeo-DRL formalgeo 2024 2025"

Links: [{"title":"[2402.09051] FGeo-DRL: Deductive Reasoning for Geometric Problems through Deep Reinforcement Learning","url":"https://arxiv.org/abs/2402.09051"},{"title":"(PDF) FGeo-DRL: Deductive Reasoning for Geometric Problems through Deep Reinforcement Learning","url":"https://www.researchgate.net/publication/379613284_FGeo-DRL_Deductive_Reasoning_for_Geometric_Problems_through_Deep_Reinforcement_Learning"},{"title":"FGeo-DRL: Deductive Reasoning for Geometric Problems through Deep Reinforcement Learning","url":"https://www.mdpi.com/2073-8994/16/4/437"},{"title":"FormalGeo: Formal representation and solving for Euclidean plane geometry problems","url":"https://formalgeo.github.io/"},{"title":"FormalGeo: An Extensible Formalized Framework for Olympiad Geometric Problem Solving | alphaXiv","url":"https://www.alphaxiv.org/abs/2310.18021"},{"title":"GitHub - BitSecret/FGPS: Formal geometric problem solver based on FormalGeo. · GitHub","url":"https://github.com/BitSecret/FGPS"},{"title":"FGeo-DRL: Deductive Reasoning for Geometric Problems through Deep   Reinforcement Learning","url":"https://arxiv.org/pdf/2402.09051"},{"title":"FGeo-DRL:Deductive Reasoning for Geometric Problems through Deep Reinforcement Learning","url":"https://arxiv.org/html/2402.09051v1"},{"title":"GitHub - majianz/dl4gps: [ACL 2026 Main Conference] Paper list for the survey \"A Survey of Deep Learning for Geometry Problem Solving\" · GitHub","url":"https://github.com/majianz/dl4gps"}]

Based on the search results, here's what I found about FGeo-DRL and related formal geometry constraint solving work:

## FGeo-DRL: Deductive Reasoning for Geometric Problems

FGeo-DRL is a neural-symbolic system built to automatically perform human-like geometric deductive reasoning. It leverages a pre-trained natural language model to establish a policy network for theorem selection and employ Monte Carlo Tree Search for heuristic exploration.

### System Architecture

The symbolic part is a reinforcement learning environment based on geometry formalization theory and FormalGeo, which models geometric problem solving (GPS) as a Markov Decision Process (MDP). The known conditions and objectives of the problem form the state space, while the set of theorems forms the action space.

### Reward Function

The reward is determined by the success of theorem solving in the Monte Carlo Tree Search process, similar to AlphaGo, allowing reward feedback to shorten the length of theorem sequences and achieve optimal sequences.

### Performance Results

Experiments conducted on the formalgeo7k dataset have achieved a problem-solving success rate of 86.40%. FGeo-DRL provides readable and verifiable automated solutions to geometric problems.

The paper was published in April 2024 in the Symmetry journal and represents part of a broader series of formal geometry problem-solving approaches within the FormalGeo framework.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "79f07f53-b53b-4717-9613-a5b5f0abb54b",
  "isSidechain": false,
  "promptId": "fbf4376b-8631-4eaa-a9bd-ce1f560c8253",
  "type": "user",
  "uuid": "2915b051-dc25-4839-9796-2b6a2ca0e138",
  "toolUseResult": {
    "query": "formal geometry constraint solver reward RL training FGeo-DRL formalgeo 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01S6uYAHMuze5CHU7958Cr9X",
        "content": [
          {
            "title": "[2402.09051] FGeo-DRL: Deductive Reasoning for Geometric Problems through Deep Reinforcement Learning",
            "url": "https://arxiv.org/abs/2402.09051"
          },
          {
            "title": "(PDF) FGeo-DRL: Deductive Reasoning for Geometric Problems through Deep Reinforcement Learning",
            "url": "https://www.researchgate.net/publication/379613284_FGeo-DRL_Deductive_Reasoning_for_Geometric_Problems_through_Deep_Reinforcement_Learning"
          },
          {
            "title": "FGeo-DRL: Deductive Reasoning for Geometric Problems through Deep Reinforcement Learning",
            "url": "https://www.mdpi.com/2073-8994/16/4/437"
          },
          {
            "title": "FormalGeo: Formal representation and solving for Euclidean plane geometry problems",
            "url": "https://formalgeo.github.io/"
          },
          {
            "title": "FormalGeo: An Extensible Formalized Framework for Olympiad Geometric Problem Solving | alphaXiv",
            "url": "https://www.alphaxiv.org/abs/2310.18021"
          },
          {
            "title": "GitHub - BitSecret/FGPS: Formal geometric problem solver based on FormalGeo. · GitHub",
            "url": "https://github.com/BitSecret/FGPS"
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
          }
        ]
      },
      "Based on the search results, here's what I found about FGeo-DRL and related formal geometry constraint solving work:\n\n## FGeo-DRL: Deductive Reasoning for Geometric Problems\n\nFGeo-DRL is a neural-symbolic system built to automatically perform human-like geometric deductive reasoning. It leverages a pre-trained natural language model to establish a policy network for theorem selection and employ Monte Carlo Tree Search for heuristic exploration.\n\n### System Architecture\n\nThe symbolic part is a reinforcement learning environment based on geometry formalization theory and FormalGeo, which models geometric problem solving (GPS) as a Markov Decision Process (MDP). The known conditions and objectives of the problem form the state space, while the set of theorems forms the action space.\n\n### Reward Function\n\nThe reward is determined by the success of theorem solving in the Monte Carlo Tree Search process, similar to AlphaGo, allowing reward feedback to shorten the length of theorem sequences and achieve optimal sequences.\n\n### Performance Results\n\nExperiments conducted on the formalgeo7k dataset have achieved a problem-solving success rate of 86.40%. FGeo-DRL provides readable and verifiable automated solutions to geometric problems.\n\nThe paper was published in April 2024 in the Symmetry journal and represents part of a broader series of formal geometry problem-solving approaches within the FormalGeo framework."
    ],
    "durationSeconds": 7.477457108000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "79f07f53-b53b-4717-9613-a5b5f0abb54b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-27T08:44:54.977Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NKu941kKcdhYEUofFfmgzV`</summary>

```json
{
  "query": "SymHPR hierarchical process reward symbolic vision learner geometry diagram 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2915b051-dc25-4839-9796-2b6a2ca0e138",
  "isSidechain": false,
  "requestId": "req_011CbSnBFdB5XGeBHCv1khTw",
  "type": "assistant",
  "uuid": "f5668329-b586-4d7b-88a6-6fddda3802a7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QSqZTuk8PQj1ee8HscFeR5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2405,
      "cache_read_input_tokens": 25396,
      "output_tokens": 122,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2405,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 122,
          "cache_read_input_tokens": 25396,
          "cache_creation_input_tokens": 2405,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2405
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

_source line 39 · 2026-05-27T08:44:55.388Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ByQmFQcaNz7DJUBmqzqkUJ`</summary>

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
  "parentUuid": "f5668329-b586-4d7b-88a6-6fddda3802a7",
  "isSidechain": false,
  "requestId": "req_011CbSnBFdB5XGeBHCv1khTw",
  "type": "assistant",
  "uuid": "a8e58ebd-0fe5-4c7c-91d6-318c03197c61",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QSqZTuk8PQj1ee8HscFeR5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2405,
      "cache_read_input_tokens": 25396,
      "output_tokens": 122,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2405,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 122,
          "cache_read_input_tokens": 25396,
          "cache_creation_input_tokens": 2405,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2405
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

_source line 40 · 2026-05-27T08:45:02.183Z_

<details><summary>↩ Tool result · `toolu_01NKu941kKcdhYEUofFfmgzV`</summary>

```text
Web search results for query: "SymHPR hierarchical process reward symbolic vision learner geometry diagram 2025"

Links: [{"title":"[2512.03126] Hierarchical Process Reward Models are Symbolic Vision Learners","url":"https://arxiv.org/abs/2512.03126"},{"title":"Hierarchical Process Reward Models are Symbolic Vision Learners","url":"https://arxiv.org/html/2512.03126v1"},{"title":"Hierarchical Process Reward Models are Symbolic Vision Learners","url":"https://arxiv.org/pdf/2512.03126"},{"title":"A Hierarchical Bayesian Approach to Inverse Reinforcement Learning with   Symbolic Reward Machines","url":"https://arxiv.org/pdf/2204.09772"},{"title":"Light Cones For Vision: Simple Causal Priors For Visual Hierarchy","url":"https://arxiv.org/pdf/2603.24753"}]

Based on the search results, I found relevant information about SymHPR:

SymHPR (Symbolic Hierarchical Process Reward Modeling) applies hierarchical step-level parsing rewards to enforce point-on-line, line-on-shape, and shape-on-relation consistency.

SymHPR (Symbolic Hierarchical Process Reward Modeling) adapts Process Reward Models (PRMs) to provide fine-grained supervision for hierarchical multi-step parsing.

The approach introduces several key innovations: cost-free training data via a synthetic logic-form engine that constructs structured parsing paths paired with rendered diagrams, eliminating manual annotation; rule-based rewards computed via verifiable metrics such as F1 scores and L2 distances, removing hallucinated supervision; and hierarchical dependency modeling that enforces step-level constraints.

The approach achieved 98.2% reduction in MSE for geometric diagram reconstruction, surpassed GPT-4o by 0.6% with a 7B model on chart reconstruction, and improved by +13% on the MathGlance perception benchmark, and by +3% on MathVerse and GeoQA reasoning benchmarks.

This research was published on December 2, 2025, and represents a novel application of hierarchical process reward modeling specifically designed for symbolic vision learning with geometric diagrams.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f5668329-b586-4d7b-88a6-6fddda3802a7",
  "isSidechain": false,
  "promptId": "fbf4376b-8631-4eaa-a9bd-ce1f560c8253",
  "type": "user",
  "uuid": "c85d64ba-d68c-45bf-940d-c1faeb57d0bd",
  "toolUseResult": {
    "query": "SymHPR hierarchical process reward symbolic vision learner geometry diagram 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01ALEf389pCYhJCFr2NAqypr",
        "content": [
          {
            "title": "[2512.03126] Hierarchical Process Reward Models are Symbolic Vision Learners",
            "url": "https://arxiv.org/abs/2512.03126"
          },
          {
            "title": "Hierarchical Process Reward Models are Symbolic Vision Learners",
            "url": "https://arxiv.org/html/2512.03126v1"
          },
          {
            "title": "Hierarchical Process Reward Models are Symbolic Vision Learners",
            "url": "https://arxiv.org/pdf/2512.03126"
          },
          {
            "title": "A Hierarchical Bayesian Approach to Inverse Reinforcement Learning with   Symbolic Reward Machines",
            "url": "https://arxiv.org/pdf/2204.09772"
          },
          {
            "title": "Light Cones For Vision: Simple Causal Priors For Visual Hierarchy",
            "url": "https://arxiv.org/pdf/2603.24753"
          }
        ]
      },
      "Based on the search results, I found relevant information about SymHPR:\n\nSymHPR (Symbolic Hierarchical Process Reward Modeling) applies hierarchical step-level parsing rewards to enforce point-on-line, line-on-shape, and shape-on-relation consistency.\n\nSymHPR (Symbolic Hierarchical Process Reward Modeling) adapts Process Reward Models (PRMs) to provide fine-grained supervision for hierarchical multi-step parsing.\n\nThe approach introduces several key innovations: cost-free training data via a synthetic logic-form engine that constructs structured parsing paths paired with rendered diagrams, eliminating manual annotation; rule-based rewards computed via verifiable metrics such as F1 scores and L2 distances, removing hallucinated supervision; and hierarchical dependency modeling that enforces step-level constraints.\n\nThe approach achieved 98.2% reduction in MSE for geometric diagram reconstruction, surpassed GPT-4o by 0.6% with a 7B model on chart reconstruction, and improved by +13% on the MathGlance perception benchmark, and by +3% on MathVerse and GeoQA reasoning benchmarks.\n\nThis research was published on December 2, 2025, and represents a novel application of hierarchical process reward modeling specifically designed for symbolic vision learning with geometric diagrams."
    ],
    "durationSeconds": 7.202117472999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f5668329-b586-4d7b-88a6-6fddda3802a7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-27T08:45:02.302Z_

<details><summary>↩ Tool result · `toolu_01ByQmFQcaNz7DJUBmqzqkUJ`</summary>

```text
Web search results for query: "V-Zero zero-shot multimodal reasoning cross-modal self-play 2026"

Links: [{"title":"V-Zero: Self-Improving Multimodal Reasoning with Zero Annotation","url":"https://arxiv.org/pdf/2601.10094"},{"title":"[2601.10094] V-Zero: Self-Improving Multimodal Reasoning with Zero Annotation","url":"https://arxiv.org/abs/2601.10094"},{"title":"MM-Zero: Self-Evolving Multi-Model Vision Language Models From Zero Data","url":"https://arxiv.org/pdf/2603.09206"},{"title":"Vision-Zero: Scalable VLM Self-Improvement via Strategic Gamified Self-Play","url":"https://arxiv.org/pdf/2509.25541"},{"title":"CogGuide: Human-Like Guidance for Zero-Shot Omni-Modal Reasoning","url":"https://arxiv.org/pdf/2509.06641"},{"title":"Zero-Shot Multimodal Reasoning","url":"https://www.emergentmind.com/topics/zero-shot-multimodal-reasoning"}]

I found relevant information about V-Zero and related multimodal reasoning research. Here are the key findings:

## V-Zero: Self-Improving Multimodal Reasoning

V-Zero is a general post-training framework that facilitates self-improvement using exclusively unlabeled images. V-Zero establishes a co-evolutionary loop by instantiating two distinct roles: a Questioner and a Solver.

**How it works:**
The Questioner learns to synthesize high-quality, challenging questions by leveraging a dual-track reasoning reward that contrasts intuitive guesses with reasoned results. The Solver is optimized using pseudo-labels derived from majority voting over its own sampled responses, and both roles are trained iteratively via Group Relative Policy Optimization (GRPO), driving a cycle of mutual enhancement.

**Key advantage:**
State-of-the-art multimodal approaches rely heavily on large-scale human-annotated datasets, which are costly and time-consuming to acquire, but V-Zero overcomes this limitation.

## Related Research

The search also revealed other recent related approaches in this space, including Vision-Zero (a gamified self-play framework for VLMs) and MM-Zero (extending self-evolution to multi-model systems). These represent an emerging trend in 2026 toward self-improving multimodal models that leverage zero-annotation paradigms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a8e58ebd-0fe5-4c7c-91d6-318c03197c61",
  "isSidechain": false,
  "promptId": "fbf4376b-8631-4eaa-a9bd-ce1f560c8253",
  "type": "user",
  "uuid": "c1b3e8d7-d0d3-433b-8a0f-dcdb8b8e8fa8",
  "toolUseResult": {
    "query": "V-Zero zero-shot multimodal reasoning cross-modal self-play 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01R64UFi6Tpxti9qDzWk9f7q",
        "content": [
          {
            "title": "V-Zero: Self-Improving Multimodal Reasoning with Zero Annotation",
            "url": "https://arxiv.org/pdf/2601.10094"
          },
          {
            "title": "[2601.10094] V-Zero: Self-Improving Multimodal Reasoning with Zero Annotation",
            "url": "https://arxiv.org/abs/2601.10094"
          },
          {
            "title": "MM-Zero: Self-Evolving Multi-Model Vision Language Models From Zero Data",
            "url": "https://arxiv.org/pdf/2603.09206"
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
      "I found relevant information about V-Zero and related multimodal reasoning research. Here are the key findings:\n\n## V-Zero: Self-Improving Multimodal Reasoning\n\nV-Zero is a general post-training framework that facilitates self-improvement using exclusively unlabeled images. V-Zero establishes a co-evolutionary loop by instantiating two distinct roles: a Questioner and a Solver.\n\n**How it works:**\nThe Questioner learns to synthesize high-quality, challenging questions by leveraging a dual-track reasoning reward that contrasts intuitive guesses with reasoned results. The Solver is optimized using pseudo-labels derived from majority voting over its own sampled responses, and both roles are trained iteratively via Group Relative Policy Optimization (GRPO), driving a cycle of mutual enhancement.\n\n**Key advantage:**\nState-of-the-art multimodal approaches rely heavily on large-scale human-annotated datasets, which are costly and time-consuming to acquire, but V-Zero overcomes this limitation.\n\n## Related Research\n\nThe search also revealed other recent related approaches in this space, including Vision-Zero (a gamified self-play framework for VLMs) and MM-Zero (extending self-evolution to multi-model systems). These represent an emerging trend in 2026 toward self-improving multimodal models that leverage zero-annotation paradigms."
    ],
    "durationSeconds": 6.910671880000009,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "a8e58ebd-0fe5-4c7c-91d6-318c03197c61",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-27T08:45:05.281Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TFRkGh2Hfu1rgqUi9ZP4oL`</summary>

```json
{
  "query": "\"joint constraint\" \"mutual consistency\" perceived facts visual reasoning mathematical axiom reward 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1b3e8d7-d0d3-433b-8a0f-dcdb8b8e8fa8",
  "isSidechain": false,
  "requestId": "req_011CbSnC1m258eQA3kWjawWi",
  "type": "assistant",
  "uuid": "5f399e82-da5c-4b46-9ced-3780c1b36e50",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0181nwzr9aikseS6mpCsqGbM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1334,
      "cache_read_input_tokens": 27801,
      "output_tokens": 122,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1334,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 122,
          "cache_read_input_tokens": 27801,
          "cache_creation_input_tokens": 1334,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1334
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

_source line 43 · 2026-05-27T08:45:05.689Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LSaD6iWnNe9GEYwvj5L58b`</summary>

```json
{
  "query": "FIGR executable visual states figure reasoning multimodal math 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f399e82-da5c-4b46-9ced-3780c1b36e50",
  "isSidechain": false,
  "requestId": "req_011CbSnC1m258eQA3kWjawWi",
  "type": "assistant",
  "uuid": "5bcd74ed-0d30-466d-8b53-6f5a55dff63a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0181nwzr9aikseS6mpCsqGbM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1334,
      "cache_read_input_tokens": 27801,
      "output_tokens": 122,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1334,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 122,
          "cache_read_input_tokens": 27801,
          "cache_creation_input_tokens": 1334,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1334
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

_source line 44 · 2026-05-27T08:45:11.731Z_

<details><summary>↩ Tool result · `toolu_01LSaD6iWnNe9GEYwvj5L58b`</summary>

```text
Web search results for query: "FIGR executable visual states figure reasoning multimodal math 2025"

Links: [{"title":"[2512.24297] Figure It Out: Improve the Frontier of Reasoning with Executable Visual States","url":"https://arxiv.org/abs/2512.24297"},{"title":"Figure It Out: Improve the Frontier of Reasoning with Active Visual Thinking","url":"https://arxiv.org/html/2512.24297v1"},{"title":"Figure It Out: Improve the Frontier of Reasoning with Executable Visual States","url":"https://arxiv.org/pdf/2512.24297"},{"title":"EXECUTABLE VISUAL REASONING","url":"https://openreview.net/pdf/55c405c1346131d8fb27731a78d468a0c950e118.pdf"},{"title":"Multimodal Reasoning for Science: Technical Report and 1st Place Solution to the ICML 2025 SeePhys Challenge","url":"https://arxiv.org/pdf/2509.06079"},{"title":"CVPR 2025 Tutorial: Multimodal Mathematical Reasoning","url":"https://cvpr2025mutimodalmathreasoning.github.io/MM_math_reasoning/"},{"title":"VisioMath: Benchmarking Figure-based Mathematical Reasoning in LMMs","url":"https://arxiv.org/html/2506.06727v2"}]

Based on the search results, here's what I found about FIGR:

FIGR integrates executable visual construction into multi-turn reasoning via end-to-end reinforcement learning. Rather than relying solely on textual chains of thought, FIGR externalizes intermediate hypotheses by generating executable code that constructs diagrams within the reasoning loop.

The approach addresses a fundamental limitation in current reasoning models. Purely text-based reasoning struggles to capture structural constraints in complex settings. An adaptive reward mechanism selectively regulates when visual construction is invoked, enabling more consistent reasoning over latent global properties that are difficult to infer from text alone.

In terms of performance, experiments on eight challenging mathematical benchmarks demonstrate that FIGR outperforms strong text-only chain-of-thought baselines, improving the base model by 13.12% on AIME 2025.

The research represents an interesting development in multimodal AI, combining vision and language capabilities for improved mathematical reasoning by allowing models to construct and revise visual diagrams as part of their reasoning process.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5bcd74ed-0d30-466d-8b53-6f5a55dff63a",
  "isSidechain": false,
  "promptId": "fbf4376b-8631-4eaa-a9bd-ce1f560c8253",
  "type": "user",
  "uuid": "ab9690d9-1531-4bfa-9ddb-72132d8713dd",
  "toolUseResult": {
    "query": "FIGR executable visual states figure reasoning multimodal math 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QZmYjriMrYqAETjxXJiyNA",
        "content": [
          {
            "title": "[2512.24297] Figure It Out: Improve the Frontier of Reasoning with Executable Visual States",
            "url": "https://arxiv.org/abs/2512.24297"
          },
          {
            "title": "Figure It Out: Improve the Frontier of Reasoning with Active Visual Thinking",
            "url": "https://arxiv.org/html/2512.24297v1"
          },
          {
            "title": "Figure It Out: Improve the Frontier of Reasoning with Executable Visual States",
            "url": "https://arxiv.org/pdf/2512.24297"
          },
          {
            "title": "EXECUTABLE VISUAL REASONING",
            "url": "https://openreview.net/pdf/55c405c1346131d8fb27731a78d468a0c950e118.pdf"
          },
          {
            "title": "Multimodal Reasoning for Science: Technical Report and 1st Place Solution to the ICML 2025 SeePhys Challenge",
            "url": "https://arxiv.org/pdf/2509.06079"
          },
          {
            "title": "CVPR 2025 Tutorial: Multimodal Mathematical Reasoning",
            "url": "https://cvpr2025mutimodalmathreasoning.github.io/MM_math_reasoning/"
          },
          {
            "title": "VisioMath: Benchmarking Figure-based Mathematical Reasoning in LMMs",
            "url": "https://arxiv.org/html/2506.06727v2"
          }
        ]
      },
      "Based on the search results, here's what I found about FIGR:\n\nFIGR integrates executable visual construction into multi-turn reasoning via end-to-end reinforcement learning. Rather than relying solely on textual chains of thought, FIGR externalizes intermediate hypotheses by generating executable code that constructs diagrams within the reasoning loop.\n\nThe approach addresses a fundamental limitation in current reasoning models. Purely text-based reasoning struggles to capture structural constraints in complex settings. An adaptive reward mechanism selectively regulates when visual construction is invoked, enabling more consistent reasoning over latent global properties that are difficult to infer from text alone.\n\nIn terms of performance, experiments on eight challenging mathematical benchmarks demonstrate that FIGR outperforms strong text-only chain-of-thought baselines, improving the base model by 13.12% on AIME 2025.\n\nThe research represents an interesting development in multimodal AI, combining vision and language capabilities for improved mathematical reasoning by allowing models to construct and revise visual diagrams as part of their reasoning process."
    ],
    "durationSeconds": 6.038587131000008,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "5bcd74ed-0d30-466d-8b53-6f5a55dff63a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-27T08:45:15.491Z_

<details><summary>↩ Tool result · `toolu_01TFRkGh2Hfu1rgqUi9ZP4oL`</summary>

```text
Web search results for query: ""joint constraint" "mutual consistency" perceived facts visual reasoning mathematical axiom reward 2025 2026"

Links: [{"title":"Joint Reward Modeling: Internalizing Chain-of-Thought for Efficient Visual Reward Models","url":"https://arxiv.org/pdf/2602.07533"},{"title":"CogFlow: Bridging Perception and Reasoning through Knowledge Internalization for Visual Mathematical Problem Solving","url":"https://arxiv.org/pdf/2601.01874"},{"title":"Figure It Out: Improve the Frontier of Reasoning with Executable Visual States","url":"https://arxiv.org/pdf/2512.24297"},{"title":"PaLMR: Towards Faithful Visual Reasoning via Multimodal Process Alignment","url":"https://arxiv.org/pdf/2603.06652"},{"title":"Grounding the Score: Explicit Visual Premise Verification for Reliable Vision-Language Process Reward Models","url":"https://arxiv.org/pdf/2603.16253"}]

I found relevant research from 2025-2026 on related topics. Here are the search results:

**Key Papers Found:**

1. **Joint Reward Modeling for Visual Reward Models** - A comparison of generative, discriminative, and joint reward modeling paradigms, with joint reward modeling achieving state-of-the-art accuracy on benchmarks and significantly boosting downstream RL performance.

2. **CogFlow: Bridging Perception and Reasoning** - A cognitive-inspired three-stage framework designed to mitigate reasoning drift in mathematical problem solving.

3. **FIGR: Executable Visual States for Reasoning** - Integrates executable visual construction into multi-turn reasoning via reinforcement learning, with an adaptive reward mechanism that selectively regulates when visual construction is invoked to enable more consistent reasoning.

4. **PaLMR: Multimodal Process Alignment** - Constructs reasoning samples grounded in verifiable visual facts through data filtering and visual statement extraction, with a process-aligned optimization layer that reinforces reasoning trajectories according to visual faithfulness and logical coherence.

5. **Grounding the Score: Visual Premise Verification** - Addresses how multimodal mathematical reasoning requires jointly solving visual perception and symbolic reasoning, as a single perceptual mistake may redirect the entire derivation while keeping later steps locally coherent.

These papers appear to address the intersection of visual reasoning, mathematical problem-solving, and reward modeling that your search query targeted.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5f399e82-da5c-4b46-9ced-3780c1b36e50",
  "isSidechain": false,
  "promptId": "fbf4376b-8631-4eaa-a9bd-ce1f560c8253",
  "type": "user",
  "uuid": "57c75dc9-d2e0-49c2-b0fb-ac1a1d8dd447",
  "toolUseResult": {
    "query": "\"joint constraint\" \"mutual consistency\" perceived facts visual reasoning mathematical axiom reward 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Nw7NzWmo1ubnMaD3QJ6S1G",
        "content": [
          {
            "title": "Joint Reward Modeling: Internalizing Chain-of-Thought for Efficient Visual Reward Models",
            "url": "https://arxiv.org/pdf/2602.07533"
          },
          {
            "title": "CogFlow: Bridging Perception and Reasoning through Knowledge Internalization for Visual Mathematical Problem Solving",
            "url": "https://arxiv.org/pdf/2601.01874"
          },
          {
            "title": "Figure It Out: Improve the Frontier of Reasoning with Executable Visual States",
            "url": "https://arxiv.org/pdf/2512.24297"
          },
          {
            "title": "PaLMR: Towards Faithful Visual Reasoning via Multimodal Process Alignment",
            "url": "https://arxiv.org/pdf/2603.06652"
          },
          {
            "title": "Grounding the Score: Explicit Visual Premise Verification for Reliable Vision-Language Process Reward Models",
            "url": "https://arxiv.org/pdf/2603.16253"
          }
        ]
      },
      "I found relevant research from 2025-2026 on related topics. Here are the search results:\n\n**Key Papers Found:**\n\n1. **Joint Reward Modeling for Visual Reward Models** - A comparison of generative, discriminative, and joint reward modeling paradigms, with joint reward modeling achieving state-of-the-art accuracy on benchmarks and significantly boosting downstream RL performance.\n\n2. **CogFlow: Bridging Perception and Reasoning** - A cognitive-inspired three-stage framework designed to mitigate reasoning drift in mathematical problem solving.\n\n3. **FIGR: Executable Visual States for Reasoning** - Integrates executable visual construction into multi-turn reasoning via reinforcement learning, with an adaptive reward mechanism that selectively regulates when visual construction is invoked to enable more consistent reasoning.\n\n4. **PaLMR: Multimodal Process Alignment** - Constructs reasoning samples grounded in verifiable visual facts through data filtering and visual statement extraction, with a process-aligned optimization layer that reinforces reasoning trajectories according to visual faithfulness and logical coherence.\n\n5. **Grounding the Score: Visual Premise Verification** - Addresses how multimodal mathematical reasoning requires jointly solving visual perception and symbolic reasoning, as a single perceptual mistake may redirect the entire derivation while keeping later steps locally coherent.\n\nThese papers appear to address the intersection of visual reasoning, mathematical problem-solving, and reward modeling that your search query targeted."
    ],
    "durationSeconds": 10.207186688000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "5f399e82-da5c-4b46-9ced-3780c1b36e50",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c",
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
  "lastPrompt": "# Axiom-Grounded Self-Verified Perception for Visual Math Reasoning  ## Core Problem and Thesis  Current multimodal math reasoning systems verify perceived visual facts independently—checking each cla…",
  "leafUuid": "57c75dc9-d2e0-49c2-b0fb-ac1a1d8dd447",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "ai-title",
  "aiTitle": "Axiom-grounded self-verified visual math reasoning",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c"
}
```

---

### Tool call

_source line 48 · 2026-05-27T08:45:18.616Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AC2iRcRjhpKZJud3dfcE6C`</summary>

```json
{
  "query": "TrustGeoGen formal verified data engine geometric problem solving 2025 constraint consistency"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "57c75dc9-d2e0-49c2-b0fb-ac1a1d8dd447",
  "isSidechain": false,
  "requestId": "req_011CbSnCz94qgV6jzbtLBxoz",
  "type": "assistant",
  "uuid": "ccef455d-4e92-4d2d-a58a-f836e5936a7a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hk49DGRsonojpdkZLaJhhS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 621,
      "cache_creation_input_tokens": 742,
      "cache_read_input_tokens": 29135,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 742,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 621,
          "output_tokens": 125,
          "cache_read_input_tokens": 29135,
          "cache_creation_input_tokens": 742,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 742
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

_source line 49 · 2026-05-27T08:45:19.104Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KfBNzWW3kNhvkRofEEHYX2`</summary>

```json
{
  "query": "multimodal math perception error bottleneck MM-MATH 2024 vision language model geometry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ccef455d-4e92-4d2d-a58a-f836e5936a7a",
  "isSidechain": false,
  "requestId": "req_011CbSnCz94qgV6jzbtLBxoz",
  "type": "assistant",
  "uuid": "24719f58-2fb1-4bf7-88b8-75d8bd736217",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hk49DGRsonojpdkZLaJhhS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 621,
      "cache_creation_input_tokens": 742,
      "cache_read_input_tokens": 29135,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 742,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 621,
          "output_tokens": 125,
          "cache_read_input_tokens": 29135,
          "cache_creation_input_tokens": 742,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 742
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

_source line 50 · 2026-05-27T08:45:26.516Z_

<details><summary>↩ Tool result · `toolu_01KfBNzWW3kNhvkRofEEHYX2`</summary>

```text
Web search results for query: "multimodal math perception error bottleneck MM-MATH 2024 vision language model geometry"

Links: [{"title":"Multimodal Math Reasoning: Insights and Advances","url":"https://www.emergentmind.com/topics/multimodal-mathematical-reasoning"},{"title":"Open Eyes, Then Reason: Fine-grained Visual Mathematical Understanding in MLLMs | OpenReview","url":"https://openreview.net/forum?id=6zAIFLgayn"},{"title":"MV-MATH: Evaluating Multimodal Math Reasoning in Multi-Visual Contexts","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_MV-MATH_Evaluating_Multimodal_Math_Reasoning_in_Multi-Visual_Contexts_CVPR_2025_paper.pdf"},{"title":"Visual Reasoning Benchmark: Evaluating Multimodal LLMs on Classroom-Authentic Visual Problems from Primary Education","url":"https://arxiv.org/html/2602.12196v1"},{"title":"MathVerse: Visual Math Reasoning Benchmark","url":"https://www.emergentmind.com/topics/mathverse"},{"title":"MM-MATH: Advancing Multimodal Math Evaluation with Process Evaluation   and Fine-grained Classification","url":"https://arxiv.org/pdf/2404.05091"},{"title":"GeoPQA: Bridging the Visual Perception Gap in MLLMs for Geometric Reasoning","url":"https://arxiv.org/pdf/2509.17437"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=MATH-VISION"},{"title":"GeoCoder: Solving Geometry Problems by Generating Modular Code through   Vision-Language Models","url":"https://arxiv.org/pdf/2410.13510"}]

I found relevant search results about multimodal math perception errors and the MM-MATH benchmark. Here are the key findings:

## MM-MATH Benchmark and Perception Error Bottleneck

The MM-MATH benchmark provides fine-grained assessment of large multimodal models' multimodal math capabilities, comprising 5,793 open-ended multimodal math problems from middle school.

## Diagram Misinterpretation as Primary Error

Diagram misinterpretation is the most common error, accounting for more than half of the total error cases, underscoring the need for improved image comprehension in multimodal reasoning. More specifically, the dominant first-step error in open-ended geometry problems (over 60% in MM-MATH) is incorrect reading of spatial relationships, ignored auxiliary lines, or mistaken object identities.

## Fine-grained Visual Understanding as a Bottleneck

Advanced models like GPT-4o demonstrate a significant error rate (70%) when identifying geometric entities, highlighting that fine-grained visual understanding remains a crucial bottleneck in visual mathematical reasoning. There is a negative correlation between visual grounding accuracy and problem-solving performance.

## Performance Gap

The best-performing model achieves only 31% accuracy on MM-MATH, compared to 82% for humans, highlighting the challenging nature of the benchmark and the significant gap between multimodal reasoning capabilities of current models and humans.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "24719f58-2fb1-4bf7-88b8-75d8bd736217",
  "isSidechain": false,
  "promptId": "fbf4376b-8631-4eaa-a9bd-ce1f560c8253",
  "type": "user",
  "uuid": "7a110a5b-b8b1-4848-afef-f9da803c1b09",
  "toolUseResult": {
    "query": "multimodal math perception error bottleneck MM-MATH 2024 vision language model geometry",
    "results": [
      {
        "tool_use_id": "srvtoolu_0144hZWL9uRope6XCfXJ8LhS",
        "content": [
          {
            "title": "Multimodal Math Reasoning: Insights and Advances",
            "url": "https://www.emergentmind.com/topics/multimodal-mathematical-reasoning"
          },
          {
            "title": "Open Eyes, Then Reason: Fine-grained Visual Mathematical Understanding in MLLMs | OpenReview",
            "url": "https://openreview.net/forum?id=6zAIFLgayn"
          },
          {
            "title": "MV-MATH: Evaluating Multimodal Math Reasoning in Multi-Visual Contexts",
            "url": "https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_MV-MATH_Evaluating_Multimodal_Math_Reasoning_in_Multi-Visual_Contexts_CVPR_2025_paper.pdf"
          },
          {
            "title": "Visual Reasoning Benchmark: Evaluating Multimodal LLMs on Classroom-Authentic Visual Problems from Primary Education",
            "url": "https://arxiv.org/html/2602.12196v1"
          },
          {
            "title": "MathVerse: Visual Math Reasoning Benchmark",
            "url": "https://www.emergentmind.com/topics/mathverse"
          },
          {
            "title": "MM-MATH: Advancing Multimodal Math Evaluation with Process Evaluation   and Fine-grained Classification",
            "url": "https://arxiv.org/pdf/2404.05091"
          },
          {
            "title": "GeoPQA: Bridging the Visual Perception Gap in MLLMs for Geometric Reasoning",
            "url": "https://arxiv.org/pdf/2509.17437"
          },
          {
            "title": "Daily Papers - Hugging Face",
            "url": "https://huggingface.co/papers?q=MATH-VISION"
          },
          {
            "title": "GeoCoder: Solving Geometry Problems by Generating Modular Code through   Vision-Language Models",
            "url": "https://arxiv.org/pdf/2410.13510"
          }
        ]
      },
      "I found relevant search results about multimodal math perception errors and the MM-MATH benchmark. Here are the key findings:\n\n## MM-MATH Benchmark and Perception Error Bottleneck\n\nThe MM-MATH benchmark provides fine-grained assessment of large multimodal models' multimodal math capabilities, comprising 5,793 open-ended multimodal math problems from middle school.\n\n## Diagram Misinterpretation as Primary Error\n\nDiagram misinterpretation is the most common error, accounting for more than half of the total error cases, underscoring the need for improved image comprehension in multimodal reasoning. More specifically, the dominant first-step error in open-ended geometry problems (over 60% in MM-MATH) is incorrect reading of spatial relationships, ignored auxiliary lines, or mistaken object identities.\n\n## Fine-grained Visual Understanding as a Bottleneck\n\nAdvanced models like GPT-4o demonstrate a significant error rate (70%) when identifying geometric entities, highlighting that fine-grained visual understanding remains a crucial bottleneck in visual mathematical reasoning. There is a negative correlation between visual grounding accuracy and problem-solving performance.\n\n## Performance Gap\n\nThe best-performing model achieves only 31% accuracy on MM-MATH, compared to 82% for humans, highlighting the challenging nature of the benchmark and the significant gap between multimodal reasoning capabilities of current models and humans."
    ],
    "durationSeconds": 7.408121098999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "24719f58-2fb1-4bf7-88b8-75d8bd736217",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-27T08:45:26.990Z_

<details><summary>↩ Tool result · `toolu_01AC2iRcRjhpKZJud3dfcE6C`</summary>

```text
Web search results for query: "TrustGeoGen formal verified data engine geometric problem solving 2025 constraint consistency"

Links: [{"title":"TrustGeoGen: Formal-Verified Data Engine for Trustworthy Multi-modal Geometric Problem Solving","url":"https://arxiv.org/html/2504.15780"},{"title":"[2504.15780] TrustGeoGen: Formal-Verified Data Engine for Trustworthy Multi-modal Geometric Problem Solving","url":"https://arxiv.org/abs/2504.15780"},{"title":"Paper page - TrustGeoGen: Scalable and Formal-Verified Data Engine for Trustworthy Multi-modal Geometric Problem Solving","url":"https://huggingface.co/papers/2504.15780"},{"title":"[PDF] TrustGeoGen: Formal-Verified Data Engine for Trustworthy Multi-modal Geometric Problem Solving | Semantic Scholar","url":"https://www.semanticscholar.org/paper/TrustGeoGen:-Formal-Verified-Data-Engine-for-Fu-Chen/1ee64628a20890cd08c9bff7832dbbe0e8c6cce6"},{"title":"TrustGeoGen: Formal-Verified Data Engine for Trustworthy ...","url":"https://arxiv.org/pdf/2504.15780"},{"title":"GeoBench: Rethinking Multimodal Geometric Problem-Solving via Hierarchical Evaluation","url":"https://arxiv.org/html/2512.24119v1"},{"title":"GitHub - majianz/dl4gps: [ACL 2026 Main Conference] Paper list for the survey \"A Survey of Deep Learning for Geometry Problem Solving\" · GitHub","url":"https://github.com/majianz/dl4gps"}]

Based on the web search results, here's what I found about TrustGeoGen:

## Overview

TrustGeoGen is an autonomous and formalized geometric data generation engine that strictly guarantees reasoning trustworthiness through formal verification while generating multimodally integrated data, including premises, visual diagrams, and solutions.

## Problem It Addresses

Developing capable Multimodal Large Language Models (MLLMs) for geometric problem solving is heavily bottlenecked by the scarcity of high-quality, verifiable data, as existing data acquisition paradigms either suffer from modality incompleteness and unverified logical gaps ("leaps-of-faith"), or rely on formal engines that generate rigid, structurally homogeneous data, failing to produce high-difficulty problems or foster genuine natural-language reasoning.

## Key Features

The system introduces "connection thinking," which bridges the semantic gap between rigid formal logic and fluent human-like reasoning, ensuring coherent logical transitions, and uses the GeoExplore family of sampling algorithms to extract diverse problem-solving trajectories based on various thinking templates.

TrustGeoGen is a scalable, rule-driven formal engine that integrates three core components: constructions (defining geometric elements and premises), states (logical propositions about geometric relationships), and rules (deductive operations like triangle congruence or parallelism properties).

## Results

By formal logical verification, TrustGeoGen produces GeoTrust-200K dataset with guaranteed modality integrity, along with GeoTrust-test testset. Models trained on the synthesized dataset achieve substantial gains on out-of-distribution benchmarks, including GeoQA, Geometry3K, and OlympiadBench, demonstrating strong generalization to unseen geometry problems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ccef455d-4e92-4d2d-a58a-f836e5936a7a",
  "isSidechain": false,
  "promptId": "fbf4376b-8631-4eaa-a9bd-ce1f560c8253",
  "type": "user",
  "uuid": "f1ef87d4-60bc-4773-840a-28a710380503",
  "toolUseResult": {
    "query": "TrustGeoGen formal verified data engine geometric problem solving 2025 constraint consistency",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FBUsiiqhtSPPcNLLiQqMmG",
        "content": [
          {
            "title": "TrustGeoGen: Formal-Verified Data Engine for Trustworthy Multi-modal Geometric Problem Solving",
            "url": "https://arxiv.org/html/2504.15780"
          },
          {
            "title": "[2504.15780] TrustGeoGen: Formal-Verified Data Engine for Trustworthy Multi-modal Geometric Problem Solving",
            "url": "https://arxiv.org/abs/2504.15780"
          },
          {
            "title": "Paper page - TrustGeoGen: Scalable and Formal-Verified Data Engine for Trustworthy Multi-modal Geometric Problem Solving",
            "url": "https://huggingface.co/papers/2504.15780"
          },
          {
            "title": "[PDF] TrustGeoGen: Formal-Verified Data Engine for Trustworthy Multi-modal Geometric Problem Solving | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/TrustGeoGen:-Formal-Verified-Data-Engine-for-Fu-Chen/1ee64628a20890cd08c9bff7832dbbe0e8c6cce6"
          },
          {
            "title": "TrustGeoGen: Formal-Verified Data Engine for Trustworthy ...",
            "url": "https://arxiv.org/pdf/2504.15780"
          },
          {
            "title": "GeoBench: Rethinking Multimodal Geometric Problem-Solving via Hierarchical Evaluation",
            "url": "https://arxiv.org/html/2512.24119v1"
          },
          {
            "title": "GitHub - majianz/dl4gps: [ACL 2026 Main Conference] Paper list for the survey \"A Survey of Deep Learning for Geometry Problem Solving\" · GitHub",
            "url": "https://github.com/majianz/dl4gps"
          }
        ]
      },
      "Based on the web search results, here's what I found about TrustGeoGen:\n\n## Overview\n\nTrustGeoGen is an autonomous and formalized geometric data generation engine that strictly guarantees reasoning trustworthiness through formal verification while generating multimodally integrated data, including premises, visual diagrams, and solutions.\n\n## Problem It Addresses\n\nDeveloping capable Multimodal Large Language Models (MLLMs) for geometric problem solving is heavily bottlenecked by the scarcity of high-quality, verifiable data, as existing data acquisition paradigms either suffer from modality incompleteness and unverified logical gaps (\"leaps-of-faith\"), or rely on formal engines that generate rigid, structurally homogeneous data, failing to produce high-difficulty problems or foster genuine natural-language reasoning.\n\n## Key Features\n\nThe system introduces \"connection thinking,\" which bridges the semantic gap between rigid formal logic and fluent human-like reasoning, ensuring coherent logical transitions, and uses the GeoExplore family of sampling algorithms to extract diverse problem-solving trajectories based on various thinking templates.\n\nTrustGeoGen is a scalable, rule-driven formal engine that integrates three core components: constructions (defining geometric elements and premises), states (logical propositions about geometric relationships), and rules (deductive operations like triangle congruence or parallelism properties).\n\n## Results\n\nBy formal logical verification, TrustGeoGen produces GeoTrust-200K dataset with guaranteed modality integrity, along with GeoTrust-test testset. Models trained on the synthesized dataset achieve substantial gains on out-of-distribution benchmarks, including GeoQA, Geometry3K, and OlympiadBench, demonstrating strong generalization to unseen geometry problems."
    ],
    "durationSeconds": 8.370555924999993,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "ccef455d-4e92-4d2d-a58a-f836e5936a7a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 52 · 2026-05-27T08:45:30.921Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of the landscape. Let me do one more search to check if there's any work that directly uses mathematical axiom/theorem consistency as a reward signal for perception training, which is the core claim of this proposal.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1ef87d4-60bc-4773-840a-28a710380503",
  "isSidechain": false,
  "requestId": "req_011CbSnDqJnFNBwTQLcqXWJQ",
  "type": "assistant",
  "uuid": "b7ceb2c5-a207-47d2-bcef-0a444628aca5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HSYZw9JtjNYFS8YwHcHhLv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 826,
      "cache_creation_input_tokens": 1628,
      "cache_read_input_tokens": 29877,
      "output_tokens": 184,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1628,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 826,
          "output_tokens": 184,
          "cache_read_input_tokens": 29877,
          "cache_creation_input_tokens": 1628,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1628
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

_source line 53 · 2026-05-27T08:45:31.875Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01D8dtCdjQMTgMFFALHmSbYQ`</summary>

```json
{
  "query": "geometric theorem consistency check reward signal perception VLM angle sum constraint verification training 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7ceb2c5-a207-47d2-bcef-0a444628aca5",
  "isSidechain": false,
  "requestId": "req_011CbSnDqJnFNBwTQLcqXWJQ",
  "type": "assistant",
  "uuid": "6a9ef8df-f40b-4ca2-9884-db364b15b39b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HSYZw9JtjNYFS8YwHcHhLv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 826,
      "cache_creation_input_tokens": 1628,
      "cache_read_input_tokens": 29877,
      "output_tokens": 184,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1628,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 826,
          "output_tokens": 184,
          "cache_read_input_tokens": 29877,
          "cache_creation_input_tokens": 1628,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1628
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

_source line 54 · 2026-05-27T08:45:32.138Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SNzy86A3aWwneu7xakxuvq`</summary>

```json
{
  "query": "CogFlow perception reasoning knowledge internalization visual mathematical problem 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a9ef8df-f40b-4ca2-9884-db364b15b39b",
  "isSidechain": false,
  "requestId": "req_011CbSnDqJnFNBwTQLcqXWJQ",
  "type": "assistant",
  "uuid": "5733c97d-c5d6-4018-b336-a3af72406edc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HSYZw9JtjNYFS8YwHcHhLv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 826,
      "cache_creation_input_tokens": 1628,
      "cache_read_input_tokens": 29877,
      "output_tokens": 184,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1628,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 826,
          "output_tokens": 184,
          "cache_read_input_tokens": 29877,
          "cache_creation_input_tokens": 1628,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1628
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

_source line 55 · 2026-05-27T08:45:39.224Z_

<details><summary>↩ Tool result · `toolu_01SNzy86A3aWwneu7xakxuvq`</summary>

```text
Web search results for query: "CogFlow perception reasoning knowledge internalization visual mathematical problem 2026"

Links: [{"title":"\\textsc{CogFlow}: Bridging Perception and Reasoning through Knowledge Internalization for Visual Mathematical Problem Solving","url":"https://shchen233.github.io/cogflow/"},{"title":"[Quick Review] CogFlow: Bridging Perception and Reasoning through Knowledge Internalization for Visual Mathematical Problem Solving","url":"https://liner.com/review/cogflow-bridging-perception-and-reasoning-through-knowledge-internalization-for-visual"},{"title":"[2601.01874] CogFlow: Bridging Perception and Reasoning through Knowledge Internalization for Visual Mathematical Problem Solving","url":"https://arxiv.org/abs/2601.01874"},{"title":"CogFlow: Bridging Perception and Reasoning through Knowledge Internalization for Visual Mathematical Problem Solving | OpenReview","url":"https://openreview.net/forum?id=sZ0DsaRsd4"},{"title":"CogFlow: Bridging Perception and Reasoning through Knowledge Internalization for Visual Mathematical Problem Solving","url":"https://arxiv.org/html/2601.01874"},{"title":"[Literature Review] CogFlow: Bridging Perception and Reasoning through Knowledge Internalization for Visual Mathematical Problem Solving","url":"https://www.themoonlight.io/en/review/cogflow-bridging-perception-and-reasoning-through-knowledge-internalization-for-visual-mathematical-problem-solving"},{"title":"Preprint COGFLOW: BRIDGING PERCEPTION AND REASONING","url":"https://arxiv.org/pdf/2601.01874"}]

I found comprehensive information about CogFlow. Here's what the search results reveal:

## Overview

CogFlow is a novel cognitive-inspired three-stage framework that incorporates a knowledge internalization stage, explicitly simulating the hierarchical flow of human reasoning: perception → internalization → reasoning. The work was presented at The Fourteenth International Conference on Learning Representations in 2026.

## Problem Address

Despite significant progress, multimodal large language models continue to struggle with visual mathematical problem solving. Recent works recognize that visual perception is a bottleneck in visual mathematical reasoning, but their solutions are limited to improving the extraction and interpretation of visual inputs, while ignoring the key issue of whether the extracted visual cues are faithfully integrated and properly utilized in subsequent reasoning.

## Key Components

The framework includes three main enhancements:

1. **Perception Stage**: Synergistic Visual Rewards boost perception capabilities in parametric and semantic spaces, jointly improving visual information extraction from symbols and diagrams.

2. **Internalization Stage**: A Knowledge Internalization Reward model in the internalization stage bridges perception and reasoning.

3. **Reasoning Stage**: A Visual-Gated Policy Optimization algorithm enforces that reasoning is grounded with visual knowledge, preventing models from seeking shortcuts that appear coherent but are visually ungrounded reasoning chains.

## Dataset and Validation

CogFlow contributes a new dataset MathCog for model training, which contains samples with over 120K high-quality perception-reasoning aligned annotations. Comprehensive experiments and analysis on commonly used visual mathematical reasoning benchmarks validate the superiority of the proposed CogFlow.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5733c97d-c5d6-4018-b336-a3af72406edc",
  "isSidechain": false,
  "promptId": "fbf4376b-8631-4eaa-a9bd-ce1f560c8253",
  "type": "user",
  "uuid": "b2653604-5cd6-4f2c-b13a-3a6615c5c7f6",
  "toolUseResult": {
    "query": "CogFlow perception reasoning knowledge internalization visual mathematical problem 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_015CaMHAopP8AvHZnKGHA826",
        "content": [
          {
            "title": "\\textsc{CogFlow}: Bridging Perception and Reasoning through Knowledge Internalization for Visual Mathematical Problem Solving",
            "url": "https://shchen233.github.io/cogflow/"
          },
          {
            "title": "[Quick Review] CogFlow: Bridging Perception and Reasoning through Knowledge Internalization for Visual Mathematical Problem Solving",
            "url": "https://liner.com/review/cogflow-bridging-perception-and-reasoning-through-knowledge-internalization-for-visual"
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
            "title": "CogFlow: Bridging Perception and Reasoning through Knowledge Internalization for Visual Mathematical Problem Solving",
            "url": "https://arxiv.org/html/2601.01874"
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
      "I found comprehensive information about CogFlow. Here's what the search results reveal:\n\n## Overview\n\nCogFlow is a novel cognitive-inspired three-stage framework that incorporates a knowledge internalization stage, explicitly simulating the hierarchical flow of human reasoning: perception → internalization → reasoning. The work was presented at The Fourteenth International Conference on Learning Representations in 2026.\n\n## Problem Address\n\nDespite significant progress, multimodal large language models continue to struggle with visual mathematical problem solving. Recent works recognize that visual perception is a bottleneck in visual mathematical reasoning, but their solutions are limited to improving the extraction and interpretation of visual inputs, while ignoring the key issue of whether the extracted visual cues are faithfully integrated and properly utilized in subsequent reasoning.\n\n## Key Components\n\nThe framework includes three main enhancements:\n\n1. **Perception Stage**: Synergistic Visual Rewards boost perception capabilities in parametric and semantic spaces, jointly improving visual information extraction from symbols and diagrams.\n\n2. **Internalization Stage**: A Knowledge Internalization Reward model in the internalization stage bridges perception and reasoning.\n\n3. **Reasoning Stage**: A Visual-Gated Policy Optimization algorithm enforces that reasoning is grounded with visual knowledge, preventing models from seeking shortcuts that appear coherent but are visually ungrounded reasoning chains.\n\n## Dataset and Validation\n\nCogFlow contributes a new dataset MathCog for model training, which contains samples with over 120K high-quality perception-reasoning aligned annotations. Comprehensive experiments and analysis on commonly used visual mathematical reasoning benchmarks validate the superiority of the proposed CogFlow."
    ],
    "durationSeconds": 7.080758155000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "5733c97d-c5d6-4018-b336-a3af72406edc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-27T08:45:40.005Z_

<details><summary>↩ Tool result · `toolu_01D8dtCdjQMTgMFFALHmSbYQ`</summary>

```text
Web search results for query: "geometric theorem consistency check reward signal perception VLM angle sum constraint verification training 2025 2026"

Links: [{"title":"Grounding the Score: Explicit Visual Premise Verification for Reliable VLM Process Reward Models","url":"https://arxiv.org/html/2603.16253"},{"title":"Enhancing Geometric Perception in VLMs via Translator-Guided Reinforcement Learning","url":"https://arxiv.org/pdf/2602.22703"},{"title":"Grounding the Score: Explicit Visual Premise Verification for Reliable Vision-Language Process Reward Models","url":"https://arxiv.org/pdf/2603.16253"},{"title":"TangramSR: Can Vision-Language Models Reason in Continuous Geometric Space?","url":"https://arxiv.org/pdf/2602.05570"},{"title":"GeoPQA: Bridging the Visual Perception Gap in MLLMs for Geometric Reasoning","url":"https://arxiv.org/pdf/2509.17437"},{"title":"Geometrically-Constrained Agent for Spatial Reasoning","url":"https://arxiv.org/html/2511.22659v1"},{"title":"Smooth Operator: Smooth Verifiable Reward Activates Spatial Reasoning Ability of Vision-Language Model","url":"https://arxiv.org/pdf/2601.07695"}]

Based on the web search results, I found several highly relevant recent papers (2025-2026) on this topic:

## Key Findings:

**EVPV-PRM (Grounding the Score)** - EVPV makes a PRM "qualified" to judge: it explicitly represents what visual facts a step relies on, checks those facts against independent visual evidence, and uses the resulting reliability to calibrate step rewards. Rewards for visually dependent steps are attenuated when reliability is low and preserved when reliability is high, decoupling perceptual uncertainty from logical evaluation.

**GEODPO (Enhancing Geometric Perception)** - GEODPO employs an NL-to-DSL translator trained on synthetic pairs, which facilitates the computation of fine-grained, DSL-level scores, which serve as reward signals in reinforcement learning. GEODPO achieves substantial gains: +26.5% on in-domain data, +8.0% on out-of-domain data, and +39.0% on downstream reasoning tasks.

**GeoPQA (Bridging the Visual Perception Gap)** - A two-stage RL training framework that first enhances the visual perception of geometric structures, then fosters reasoning capabilities, improving geometric reasoning by 9.7% and geometric problem solving by 9.1%.

**TangramSR (Continuous Geometric Space)** - A lightweight, recursive self-improvement framework that combines in-context learning with reward-guided refinement loops to progressively enhance geometric alignment, achieving substantial IoU improvements at test time.

These papers directly address constraint verification, reward signal design for geometric perception in VLMs, and recent training approaches from 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6a9ef8df-f40b-4ca2-9884-db364b15b39b",
  "isSidechain": false,
  "promptId": "fbf4376b-8631-4eaa-a9bd-ce1f560c8253",
  "type": "user",
  "uuid": "f9f9b998-f789-4b34-abef-1a61c75dc75c",
  "toolUseResult": {
    "query": "geometric theorem consistency check reward signal perception VLM angle sum constraint verification training 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Pr6zhp2uYATFB6XBNaTRW9",
        "content": [
          {
            "title": "Grounding the Score: Explicit Visual Premise Verification for Reliable VLM Process Reward Models",
            "url": "https://arxiv.org/html/2603.16253"
          },
          {
            "title": "Enhancing Geometric Perception in VLMs via Translator-Guided Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2602.22703"
          },
          {
            "title": "Grounding the Score: Explicit Visual Premise Verification for Reliable Vision-Language Process Reward Models",
            "url": "https://arxiv.org/pdf/2603.16253"
          },
          {
            "title": "TangramSR: Can Vision-Language Models Reason in Continuous Geometric Space?",
            "url": "https://arxiv.org/pdf/2602.05570"
          },
          {
            "title": "GeoPQA: Bridging the Visual Perception Gap in MLLMs for Geometric Reasoning",
            "url": "https://arxiv.org/pdf/2509.17437"
          },
          {
            "title": "Geometrically-Constrained Agent for Spatial Reasoning",
            "url": "https://arxiv.org/html/2511.22659v1"
          },
          {
            "title": "Smooth Operator: Smooth Verifiable Reward Activates Spatial Reasoning Ability of Vision-Language Model",
            "url": "https://arxiv.org/pdf/2601.07695"
          }
        ]
      },
      "Based on the web search results, I found several highly relevant recent papers (2025-2026) on this topic:\n\n## Key Findings:\n\n**EVPV-PRM (Grounding the Score)** - EVPV makes a PRM \"qualified\" to judge: it explicitly represents what visual facts a step relies on, checks those facts against independent visual evidence, and uses the resulting reliability to calibrate step rewards. Rewards for visually dependent steps are attenuated when reliability is low and preserved when reliability is high, decoupling perceptual uncertainty from logical evaluation.\n\n**GEODPO (Enhancing Geometric Perception)** - GEODPO employs an NL-to-DSL translator trained on synthetic pairs, which facilitates the computation of fine-grained, DSL-level scores, which serve as reward signals in reinforcement learning. GEODPO achieves substantial gains: +26.5% on in-domain data, +8.0% on out-of-domain data, and +39.0% on downstream reasoning tasks.\n\n**GeoPQA (Bridging the Visual Perception Gap)** - A two-stage RL training framework that first enhances the visual perception of geometric structures, then fosters reasoning capabilities, improving geometric reasoning by 9.7% and geometric problem solving by 9.1%.\n\n**TangramSR (Continuous Geometric Space)** - A lightweight, recursive self-improvement framework that combines in-context learning with reward-guided refinement loops to progressively enhance geometric alignment, achieving substantial IoU improvements at test time.\n\nThese papers directly address constraint verification, reward signal design for geometric perception in VLMs, and recent training approaches from 2025-2026."
    ],
    "durationSeconds": 8.126779899,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "6a9ef8df-f40b-4ca2-9884-db364b15b39b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 57 · 2026-05-27T08:45:40.013Z_

```json
{
  "parentUuid": "f9f9b998-f789-4b34-abef-1a61c75dc75c",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "bd517639-bec6-4137-9c86-7ee672daf92e",
  "timestamp": "2026-05-27T08:45:40.013Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 58_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Axiom-Grounded Self-Verified Perception for Visual Math Reasoning  ## Core Problem and Thesis  Current multimodal math reasoning systems verify perceived visual facts independently—checking each cla…",
  "leafUuid": "bd517639-bec6-4137-9c86-7ee672daf92e",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c"
}
```

---

### Runtime record

_source line 59_

```json
{
  "type": "ai-title",
  "aiTitle": "Axiom-grounded self-verified visual math reasoning",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c"
}
```

---

### Assistant

_source line 60 · 2026-05-27T08:46:15.414Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a very comprehensive picture of the landscape. Let me synthesize my findings and evaluate this proposal as the "发掘 agent."

Key observations from my research:

1. **The core claim is genuinely novel**: No existing work uses mathematical axiom/invariant consistency of the *joint set* of perceived quantitative facts as a self-supervised perception reward. The closest works are:
   - EVPV: checks per-claim visual premises against image-extracted constraints, but independently
   - Perception-R1: LLM-judged per-claim perception reward
   - PEARL: per-claim perception checklist gating
   - GeoDPO, SymHPR, SSL-R1, PRCO, and CogFlow all approach the problem differently—through DSL translation accuracy, structural properties, generic visual reasoning, utility-based rewards, or knowledge internalization—but none directly leverage quantitative axiom consistency across multiple facts.

2. **The "joint constraint satisfaction vs independent fact-checking" framing is genuinely sharp and novel**. This is a real conceptual contribution.

3. **However, there are some things I need to think about critically:**

a) **Trivial alternative question**: Could you simply do inference-time axiom checking without the training-time reward signal?

—The proposal addresses this explicitly with the "training-time internalization vs inference-time correction" argument and plans an ablation. Good.

b) **Premise assumption question**: The core assumption is that the axiom checker and formal extraction pipeline are reliable enough to provide useful reward signals. If the formal extraction is noisy at the SFT stage, the axiom rewards could be misleading. The proposal partially addresses this through curriculum design and parsability rewards.

c) **False positive/negative concern**: The proposal acknowledges this and plans to measure it. But there's a fundamental limitation: how often do perceived facts satisfy the axioms but are actually incorrect? For instance, if all three angles in a triangle are wrong but still sum to 180°, the axiom reward gives a false positive.

d) **Related work coverage**: The proposal has extremely thorough related work coverage. CogFlow (ICLR 2026) is a notable gap—it also uses a three-stage framework with perception, internalization, and reasoning stages, addressing the same perception bottleneck problem. The key distinction is that CogFlow relies on ground-truth annotations for its rewards, whereas this proposal's axiom-based rewards are annotation-free.

e) **The "beyond mathematics" generalization claim**: The proposal frames this nicely with examples like Kirchhoff's laws and valence constraints, elevating the significance, but it's somewhat speculative since the actual demonstrations are limited to mathematics.

Looking at potential discovery points, the core novelty really centers on shifting from verifying individual claims to satisfying joint constraints—this is a conceptual reframing of what perception verification means in domains with structural invariants. The false positive problem is actually revealing: when perceived facts are individually incorrect but jointly consistent with axioms (like angles all shifted by the same amount but still summing to 180°), it exposes a fundamental limitation. This also hints at a stronger argument: denser axiom coverage should constrain the solution space more tightly, making the reward signal more informative.

I should also flag CogFlow as a missing related work that needs differentiation, and the false positive rate deserves better theoretical framing as a limitation rather than just an empirical observation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd517639-bec6-4137-9c86-7ee672daf92e",
  "isSidechain": false,
  "requestId": "req_011CbSnEnyAR37CQrbXTRDLW",
  "type": "assistant",
  "uuid": "fb235392-71cf-469f-9515-c4be5c57dd25",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PHXGBQ5xtKEWMNyTW9QuUx",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 802,
      "cache_creation_input_tokens": 1870,
      "cache_read_input_tokens": 31505,
      "output_tokens": 5585,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1870,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 802,
          "output_tokens": 5585,
          "cache_read_input_tokens": 31505,
          "cache_creation_input_tokens": 1870,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1870
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

_source line 61 · 2026-05-27T08:47:43.652Z_

Now I have a thorough understanding of the landscape. Let me compile my analysis.

---

【状态】: 有发掘空间

【前置调研发现】

- **EVPV (arXiv 2603.16253, 2026)**: 最直接相关的对比对象。EVPV 将 per-claim visual checklist 与 image-extracted constraints 匹配，用于校准 PRM step reward。关键区别：EVPV 逐条检查每个 visual premise 的可靠性，然后用可靠性分数 gate reward——它不检查多个 perceived facts 之间的联合一致性。这是本 proposal 声称要填的 gap，从调研来看这个 gap 确实存在。

- **Perception-R1 (arXiv 2506.07218, 2025)**: 用 LLM judge 评估 VLM response 与预收集 textual annotations 的一致性作为 perception reward。仅需 1,442 训练样本即达 SOTA。局限：需要预收集 annotations，且逐条判断，不涉及跨 claim 一致性。

- **PEARL (arXiv 2511.18437, CVPR 2026)**: 双分支框架，用 perception checklist 作为 gating reward，MathVerse +9.7%。局限：需要标注的 sub-question answers，每个 checklist item 独立验证。

- **GeoDPO (arXiv 2602.22703, 2026)**: NL-to-DSL translator 引导的 RL，reward 基于 DSL 翻译准确度。in-domain +26.5%, downstream +39%。关键区别：reward 信号来自 DSL 翻译保真度，不是 perceived quantitative values 的 axiom-level 一致性。

- **CogFlow (arXiv 2601.01874, ICLR 2026)**: **高度相关但 proposal 未引用**。三阶段框架 perception → internalization → reasoning，用 Synergistic Visual Rewards + Knowledge Internalization Reward + Visual-Gated Policy Optimization。构建了 MathCog 数据集（120K+ perception-reasoning aligned annotations）。关键区别：CogFlow 依赖大量标注数据，而本 proposal 用 axiom consistency 实现 annotation-free reward。

- **SymHPR (arXiv 2512.03126, 2025)**: 在 topological/structural 层面用 rule-based reward（F1, L2 距离）训练 hierarchical PRM。关键区别：操作在结构层（point-on-line, shape-on-relation），不是 quantitative 层（角度值、长度值的 axiom 一致性）。

- **SSL-R1 (arXiv 2604.20705, 2026)**: 用 generic visual puzzles（rotation prediction, patch ordering）作为 self-supervised RL reward，domain-agnostic。本 proposal 用 domain-specific mathematical axioms，supervision 信号更强更有针对性。

- **PRCO (arXiv 2603.28618, 2026)**: Observer/Solver 双角色框架，Observer 获得基于 Solver 下游成功的 utility reward。不利用数学结构做验证。

- **TrustGeoGen (arXiv 2504.15780, 2025)**: 形式化验证的几何数据生成引擎，保证 reasoning trustworthiness。生成 GeoTrust-200K。关键：该工作证明了形式化几何约束验证在数据生成中的可行性，间接支持了本 proposal 将形式化约束用于 reward signal 的技术路线。

- **FIGR (arXiv 2512.24297, 2025)**: 将 executable visual construction 集成到 multi-turn reasoning，用 RL + adaptive reward。思路不同但都在用 executable/formal 手段增强 visual math reasoning。

- **PaLMR (arXiv 2603.06652, 2026)**: 用 verifiable visual facts 构建 reasoning samples，process-aligned optimization 强化 visual faithfulness 和 logical coherence。相关但更偏 process alignment 而非 perception training。

- **调研总结**: 当前领域研究者在两个方向上活跃突破：(1) 如何设计更好的 perception-specific reward signal（从 GT-dependent → LLM-judged → DSL-translation → self-supervised），(2) 如何解耦 perception 和 reasoning 的 credit assignment。本 proposal 在方向(1)上提出了一个确实未被探索的 reward 设计——基于 domain-specific mathematical invariants 的 joint consistency。这个 gap 在调研中得到了确认。

---

【发掘点 1】
- 维度: related work 差异化
- 内容: **CogFlow (ICLR 2026) 是一个高度相关但被遗漏的工作，必须在 related work 中定位并差异化。** CogFlow 同样提出三阶段框架（perception → internalization → reasoning）解决同一个 perception bottleneck 问题，且已被 ICLR 2026 接收。若审稿人发现这一遗漏，会严重质疑 novelty claim 的完整性。差异化要点：CogFlow 的 Synergistic Visual Rewards 和 Knowledge Internalization Reward 都依赖 120K+ 人工标注的 perception-reasoning aligned annotations（MathCog 数据集），本 proposal 的 axiom-consistency reward 完全不需要 GT perception annotations——这恰恰是核心差异，应作为 "annotation-free vs. annotation-dependent" 的对比轴明确提出。此外，CogFlow 的 reward 仍然是 per-claim level（Synergistic Visual Rewards 分别在 parametric 和 semantic space 优化），而本 proposal 的 reward 天然是 joint level（axiom 约束的是 claims 之间的关系），这是一个更深层的差异。
- 价值: 补全 related work 覆盖面，防止审稿人以 "missed highly relevant work" 为由质疑 novelty claim 的严肃性。同时，与 CogFlow 的显式对比实际上强化了本 proposal 的独特性（annotation-free + joint-level verification）。命中 Related Work 维度。
- 调研依据: CogFlow (arXiv 2601.01874, ICLR 2026) 调研发现其依赖大规模标注数据且 reward 仍为 per-claim level。

【发掘点 2】
- 维度: 核心 claim 强化
- 内容: **"joint constraint satisfaction vs. independent fact-checking" 这一核心概念贡献的理论深度可以进一步强化。** 当前 proposal 停留在直觉层面（"三个角度分别看起来合理但不求和到 180°"）。可以构建一个更严谨的论证：(1) 形式化定义"perception configuration"为一个 value vector，"axiom set"为该 vector 必须满足的约束集合；(2) 论证当 axiom 数量增加时，满足所有 axiom 的 feasible set 收缩，false positive（axiom-consistent 但 factually incorrect）的概率下降——即 axiom density 与 reward informativeness 正相关；(3) 给出一个简单的几何示例：单个三角形有 1 个 axiom（角度和=180°），自由度为 2；加上 Pythagorean constraint 后自由度降为 1；再加上外角定理后 feasible set 进一步收缩。这种 "axiom density → constraint tightness → reward informativeness" 的论证会让 core claim 从 "intuitive observation" 升级为 "principled framework"，显著提升 novelty 的可信度。
- 价值: 将核心贡献从 "methodological trick"（用 axiom 做 reward）提升为 "conceptual framework"（joint constraint satisfaction 作为 perception verification 的正确范式），提升 Novelty 和 Significance 两个维度的天花板。
- 调研依据: 基于领域整体趋势判断——调研发现所有现有工作（EVPV, Perception-R1, PEARL, CogFlow）都在 per-claim level 操作，没有任何工作讨论过 joint consistency 的信息论/约束论性质。这意味着提出这一理论框架有真正的新颖性。

【发掘点 3】
- 维度: 前提假设质疑
- 内容: **Axiom-consistency reward 的 false positive 问题比 proposal 目前承认的更根本，需要在 claim 层面正面应对而非仅作为 empirical measurement。** 核心问题：当多个 perceived values 同时偏离 GT 但恰好满足 axiom 约束时（例如三角形三个角均偏移 +5° 但仍求和 180°——这不可能，但更一般地：等腰三角形中两底角均被感知为 50° 而非 GT 的 45°，顶角被感知为 80° 而非 90°，求和仍为 180°），axiom reward 给出 false positive。这不是 edge case——系统性感知偏差（如 VLM 对锐角的系统性高估）恰恰会产生这种 "collectively consistent but individually wrong" 的模式。Proposal 需要在 claim 层面承认这一理论限制，并论证为什么这仍然优于 status quo：(1) 即使存在 false positive，axiom reward 排除了 "collectively impossible" 的感知（当前方法连这一步都做不到），这已是净改进；(2) 多个不同类型的 axioms 联合约束大幅压缩 false positive 空间（回到发掘点 2 的 axiom density 论证）；(3) 与 answer-level reward 联合使用（Stage 2）进一步补偿。这样 proposal 就把一个潜在弱点转化为了展示方法论成熟度的机会。
- 价值: 审稿人几乎必然会追问 false positive 率问题。提前在 claim 层面系统性回应，比仅在实验中测量更有说服力，命中 Novelty（核心 claim 的 robustness）维度。
- 调研依据: 基于 EVPV 和 PEARL 的设计——它们虽然只做 per-claim 检查，但不存在 "jointly consistent but individually wrong" 的 false positive 模式，因此从某种意义上比 joint approach 更不容易被系统性偏差欺骗。这是一个需要正面讨论的 tradeoff。

【发掘点 4】
- 维度: significance 提升
- 内容: **"Axioms provide free verification" 的 paradigm claim 是 proposal 的最大 significance lever，但当前 framing 过于轻描淡写。** Proposal 在第二段简短提到 Kirchhoff's laws、valence constraints、dimensional consistency 等，但仅作为一句附带说明。建议将此提升为 paper 的核心 significance 论述之一：在任何有 formal domain knowledge 可表达为 constraint system 的领域，domain invariants 都可以作为 annotation-free self-supervised perception reward。这不仅是 visual math 的一个方法，而是 "structured-domain perception training" 的一个通用范式。具体可以：(1) 在 introduction 明确提出这一 paradigm，将 visual math 定位为第一个 instantiation；(2) 在 discussion 中给出至少 2 个其他领域的 concrete instantiation sketch（例如：电路图中 Kirchhoff's current law 要求节点电流之和为零，化学结构图中 valence 约束要求原子价键数匹配），让审稿人看到 generalization potential 而非仅仅是 geometry trick。
- 价值: 将 contribution 从 "a better reward for visual math" 提升为 "a paradigm for structured-domain self-supervised perception training"，显著扩大 paper 的受众面和 citation potential。命中 Significance 维度。
- 调研依据: 基于领域整体趋势判断——调研发现 SSL-R1 和 V-Zero 代表的 "domain-agnostic self-supervised reward" 方向正在兴起，但没有工作系统性地提出 "domain-specific invariants as perception reward" 这一互补范式。这个定位空白是真实的。

【发掘点 5】
- 维度: novelty 锐化
- 内容: **Proposal 的 novelty 叙述可以更锐利地区分 "what to verify"（verification target）和 "how to verify"（verification mechanism）两个维度。** 当前 proposal 在 related work 中有时将这两个维度混在一起讨论。建议构建一个 2×2 定位矩阵：(1) per-claim × image-based = EVPV, Perception-R1; (2) per-claim × annotation-based = PEARL; (3) per-claim × DSL-translation = GeoDPO; (4) **joint × axiom-based = 本工作（唯一占据此象限）**。这种矩阵式定位让 novelty 的位置一目了然，审稿人无需自己提炼。额外的锐化点：强调 joint verification 不仅是一种 "更好的" verification，而是捕捉了一类 per-claim methods 在结构上（structurally）无法检测的错误——这不是程度差异，而是能力边界差异。
- 价值: 让 novelty claim 从散文式叙述变为结构化定位，降低审稿人误判 novelty 的风险。命中 Novelty 维度。
- 调研依据: 综合 EVPV、Perception-R1、PEARL、GeoDPO 的调研发现——这四个工作分别代表了 per-claim verification 的不同 mechanism，但都共享 "per-claim" 这一 verification target。本 proposal 在 "what to verify" 维度上的创新是确实的。

Sources:
- [EVPV - Grounding the Score](https://arxiv.org/abs/2603.16253)
- [Perception-R1](https://arxiv.org/abs/2506.07218)
- [PEARL](https://arxiv.org/abs/2511.18437)
- [GeoDPO](https://arxiv.org/abs/2602.22703)
- [CogFlow](https://arxiv.org/abs/2601.01874)
- [SymHPR](https://arxiv.org/abs/2512.03126)
- [SSL-R1](https://arxiv.org/abs/2604.20705)
- [PRCO](https://arxiv.org/abs/2603.28618)
- [TrustGeoGen](https://arxiv.org/abs/2504.15780)
- [FIGR](https://arxiv.org/abs/2512.24297)
- [V-Zero](https://arxiv.org/abs/2601.10094)
- [FGeo-DRL](https://arxiv.org/abs/2402.09051)
- [Geoparsing](https://arxiv.org/abs/2604.11600)
- [MM-MATH](https://arxiv.org/abs/2404.05091)
- [PaLMR](https://arxiv.org/abs/2603.06652)
- [GeoPQA](https://arxiv.org/abs/2509.17437)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb235392-71cf-469f-9515-c4be5c57dd25",
  "isSidechain": false,
  "requestId": "req_011CbSnEnyAR37CQrbXTRDLW",
  "type": "assistant",
  "uuid": "49c5528a-428d-4a14-ab68-cc023dea8041",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PHXGBQ5xtKEWMNyTW9QuUx",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 802,
      "cache_creation_input_tokens": 1870,
      "cache_read_input_tokens": 31505,
      "output_tokens": 5585,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1870,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 802,
          "output_tokens": 5585,
          "cache_read_input_tokens": 31505,
          "cache_creation_input_tokens": 1870,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1870
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

_source line 62_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Axiom-Grounded Self-Verified Perception for Visual Math Reasoning  ## Core Problem and Thesis  Current multimodal math reasoning systems verify perceived visual facts independently—checking each cla…",
  "leafUuid": "49c5528a-428d-4a14-ab68-cc023dea8041",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c"
}
```

---

### Runtime record

_source line 63_

```json
{
  "type": "ai-title",
  "aiTitle": "Axiom-grounded self-verified visual math reasoning",
  "sessionId": "e8953efc-455a-4cba-89cd-695fc452845c"
}
```

---
