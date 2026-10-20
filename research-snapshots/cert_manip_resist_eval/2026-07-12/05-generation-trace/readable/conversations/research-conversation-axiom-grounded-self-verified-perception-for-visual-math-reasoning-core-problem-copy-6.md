# Research conversation: Axiom-Grounded Self-Verified Perception for Visual Math Reasoning ## Core Problem and Thesis Current multimodal math rea

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 63
- **Recorded user turns:** 1
- **Tool calls:** 20
- **Original source:** `logs/chats/exported-trajectories/account-2/52f19b28-98e1-4c6f-ab76-67a25e50a164.jsonl`
- **Structured JSON:** [`0ef6a20468593362f34c.json`](../../sessions/0e/0ef6a20468593362f34c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-27T08:43:57.491Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T08:43:57.491Z",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164",
  "content": "# Axiom-Grounded Self-Verified Perception for Visual Math Reasoning\n\n## Core Problem and Thesis\n\nCurrent multimodal math reasoning systems verify perceived visual facts independently—checking each claim against the image in isolation—but never verify whether perceived facts are mutually consistent under known mathematical constraints. This causes individually plausible but collectively impossible perceptions to cascade into reasoning failures. We argue that mathematical perception correctness is fundamentally a joint constraint satisfaction problem, not an independent fact-checking problem: even when each perceived fact has high marginal confidence, the joint set may violate mathematical axioms (e.g., three individually plausible angle estimates that do not sum to 180°). All existing per-claim verification approaches—whether using LLM judges (Perception-R1, arXiv 2025), ground-truth checklists (PEARL, arXiv 2025), or image-extracted constraints (EVPV, arXiv 2026)—are structurally blind to such inter-claim inconsistencies, regardless of their per-claim accuracy.\n\n## Research Opportunity\n\nMathematical diagrams encode structural invariants (geometric theorems like angle sums, Pythagorean constraints, parallel-line properties, circle theorems; chart constraints like sum-to-total; function constraints like monotonicity) that perceived facts must jointly satisfy. These invariants provide a free, dense, automatically verifiable reward signal for RL-based perception training—requiring no ground truth annotations. This is newly feasible because (1) diagram formalization methods (DFE-GPS (AAAI 2025), Geoparsing (arXiv 2026)) now reliably extract structured representations, (2) solver-in-the-loop RL has been proven effective for reasoning (FGeo-DRL achieves 86.4% on formalgeo7k via RL in formal geometry environments (arXiv 2024); sub-goal verifiable rewards unlock geometric reasoning gains (Milestones over Outcome, arXiv 2025)), and (3) the perception bottleneck is definitively established (61% of multimodal math errors are perception errors per MM-MATH (arXiv 2024)).\n\nThe principle that domain-specific structural invariants serve as free self-supervised perception rewards extends beyond mathematics—Kirchhoff's laws for circuit diagrams, valence constraints for chemical structures, dimensional consistency for engineering drawings all exhibit the same \"axioms provide free verification\" structure—though this paper demonstrates the paradigm on mathematical diagrams.\n\n## Research Landscape\n\nPerception is the confirmed bottleneck: Qwen3-VL leads MathVista (ICLR 2024) at 85.8% but models still fail systematically on vision-dense problems (MathVerse vision-only subsets). The current landscape of perception-focused methods can be categorized by their reward signal source:\n\n**Annotation-dependent rewards.** Perception-R1 (arXiv 2025) introduces an LLM-judged visual perception reward but requires pre-collected textual annotations and checks individual claims, not inter-claim consistency. PEARL (arXiv 2025) uses ground-truth perception checklists as gating rewards (+9.7% on MathVerse) but needs annotated sub-question answers.\n\n**Image-level per-claim verification.** EVPV (arXiv 2026) matches per-claim visual checklists against image-extracted constraints but checks each claim independently against image-level perceptual features (e.g., \"this angle appears to be ~60°\")—it does not verify whether the set of perceived values jointly satisfies domain-level mathematical axioms (e.g., \"these three angles must sum to 180°\"). This distinction—image-level perceptual constraints vs. domain-level mathematical axioms—is the precise gap our work fills.\n\n**Translation-fidelity rewards.** GeoDPO (arXiv 2026) uses NL-to-DSL translator-guided RL for geometric perception (+26.5% in-domain, +39% downstream) but rewards DSL translation accuracy, not axiom-level consistency of perceived quantitative values.\n\n**Structural/topological parsing.** SymHPR (arXiv 2025) enforces structural parsing consistency (point-on-line, shape-on-relation) for diagram reconstruction at the topological level. Our approach operates at the quantitative level and implicitly depends on reasonable topological parsing—we address this dependency through curriculum design (see Approach).\n\n**Utility-based and generic self-supervised rewards.** PRCO (arXiv 2026) introduces Observer/Solver role separation with utility-based perception rewards but does not exploit mathematical structure for verification. SSL-R1 (arXiv 2026) derives self-supervised visual RL rewards from generic SSL puzzles (rotation prediction, patch ordering) rather than domain-specific mathematical invariants. V-Zero (arXiv 2026) uses Questioner-Solver co-evolutionary loop for zero-annotation training but is domain-agnostic. Our approach's advantage over domain-agnostic methods is that mathematical invariants provide stronger, more targeted supervision than generic visual puzzles.\n\n**Confidence-based and inference-time methods.** PDCR (arXiv 2026) decomposes perception and reasoning rewards via model-internal confidence scores but does not use formal mathematical constraints. M3-ACE (arXiv 2026) uses multi-agentic context engineering to rectify perception at inference time but does not train perception via RL rewards. PFlowNet (arXiv 2026) applies variational RL with geometric reward shaping where 'geometric' refers to reward landscape geometry, not mathematical theorem constraints.\n\n**Why training-time internalization, not inference-time correction.** A natural question is whether axiom checking at inference time alone (without RL training) suffices. We argue training-time internalization via RL offers three advantages over inference-time-only correction: (1) computational efficiency—a trained model produces axiom-consistent perceptions in a single forward pass, while inference-time correction requires iterative re-perception loops with axiom checking at each step; (2) representation-level learning—RL shapes the model's internal visual representations to favor axiom-consistent percepts, rather than patching inconsistencies at the output level; (3) generalization—trained axiom-consistency transfers to novel diagram configurations and axiom combinations not seen during training. We validate this through ablation comparing training-time RL vs. inference-time-only axiom correction.\n\nNo existing work uses mathematical invariant consistency of perceived quantitative facts as a self-supervised perception reward signal.\n\n## Proposed Approach\n\nWe train a VLM (Qwen3-VL-8B as primary base, with Qwen3-VL-3B for scale-transfer validation) to perceive mathematical diagrams accurately using axiom-consistency as a self-supervised RLVR reward, requiring zero ground-truth perception annotations.\n\n**Stage 0: Formal Extraction Warm-Start.** Since axiom rewards require parseable formal descriptions, and VLMs cannot produce these from scratch, we first SFT the base model on FormalGeo/Geoparsing (arXiv 2026) data (a subset of GDP-29K) to bootstrap syntactically valid diagram-to-formal-language extraction. This addresses the bootstrapping challenge: axiom reward quality depends on reasonable formal extraction, which itself requires training. Geoparsing's own SFT+RLVR paradigm confirms this warm-start is necessary.\n\n**Stage 1: Perception-Only Axiom RL.** The model extracts structured perception claims (angles, lengths, coordinates, ratios) from diagrams into a formal constraint description language built on FormalGeo (arXiv 2023)/Geoparsing primitives. A lightweight axiom checker—implementing 40+ geometric theorems (angle sums, Pythagorean constraints, parallel-line properties, circle theorems) plus chart and function invariants—evaluates whether the perceived facts jointly satisfy all applicable mathematical constraints, producing a soft consistency score: for each applicable axiom, the violation magnitude is computed (e.g., |angle_sum − 180°|/180°) and the axiom-consistency reward is the mean of (1 − normalized_violation) across all applicable axioms. This continuous scoring provides gradient-rich reward signal for near-correct perceptions, avoiding the sparsity of binary pass/fail. An auxiliary parsability reward (whether the formal description is syntactically valid and parseable by the axiom checker) supplements the consistency reward in early training. Training uses GRPO via the veRL framework. The curriculum begins with structurally simple diagrams (single triangles, basic charts) where topological parsing is easy, progressively increasing to complex multi-shape configurations, mitigating the dependency on correct structural parsing noted in SymHPR (arXiv 2025).\n\n**Stage 2: Joint Perception-Reasoning.** Combines axiom-consistency reward with outcome-based answer correctness in GRPO training, jointly optimizing perception and reasoning.\n\n**Inference-Time Self-Verification.** Perceived facts violating axioms trigger iterative re-perception (up to 3 iterations), providing built-in self-verification without external judges. We report inference latency with and without re-perception.\n\n## Experimental Design\n\n**Benchmarks.** MathVista (ICLR 2024), MathVerse (with vision-only / vision-dominant / vision-intensive subset breakdown), MathVision (NeurIPS 2024), GeoQA, formalgeo7k. WeMath as optional extension.\n\n**Baselines (4 categories).**\n- *Base VLM:* Qwen3-VL-8B zero-shot; Qwen3-VL-8B + SFT (same data as Stage 0, no RL)\n- *Perception RL methods:* Perception-R1 (arXiv 2025, LLM-judged reward); GeoDPO (arXiv 2026, DSL-translation reward)\n- *Self-supervised RL:* SSL-R1 (arXiv 2026, generic visual puzzle reward) if code available; answer-only GRPO (answer correctness reward only, no perception reward)\n- *Reference numbers:* PEARL (arXiv 2025), EVPV (arXiv 2026), PRCO (arXiv 2026) reported results where available\n\n**Ablation Studies (5 groups).**\n1. *Reward components:* axiom reward only / answer reward only / axiom + answer (full) / random reward (sanity check)\n2. *Training curriculum:* three-stage (proposed) / skip Stage 0 (no warm-start) / skip Stage 1 (joint from scratch) / Stage 1 only (perception-only)\n3. *Axiom set:* full 40+ axioms / basic axioms only (angle sum, Pythagorean) / chart+function invariants only\n4. *Scoring strategy:* soft continuous / hard binary (ε = 0.5°, 1°, 2°) / weighted combination\n5. *Inference-time re-perception:* 0 / 1 / 2 / 3 iterations—performance vs. latency tradeoff\n\n**Additional Analyses.**\n- *Reward signal quality:* On a GT-annotated subset, compute Pearson/Spearman correlation between axiom-consistency score and true perception accuracy; report false positive (axiom-consistent but perception-incorrect) and false negative rates; visualize representative success and failure cases\n- *Compute fairness:* Report training wall-clock time and per-step overhead for each method; plot performance vs. training FLOPs curves; quantify axiom checker per-sample latency\n- *Scale transfer:* Replicate main experiments on Qwen3-VL-3B (MathVista, MathVerse) to validate method generality across model scales\n- *Training-time RL vs. inference-time-only:* Compare full ASVP against \"Stage 0 SFT + axiom-based re-perception at inference without RL training\" to validate the necessity of RL-based internalization\n\n## Key References\n\n- Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward (arXiv 2025)\n- PEARL: Perceptual-Evidence Anchored Reinforced Learning for Multimodal Reasoning (arXiv 2025)\n- Grounding the Score: Explicit Visual Premise Verification for Reliable VLM Process Reward Models [EVPV] (arXiv 2026)\n- Hierarchical Process Reward Models are Symbolic Vision Learners [SymHPR] (arXiv 2025)\n- MM-MATH: Advancing Multimodal Math Evaluation with Process Evaluation and Fine-grained Classification (arXiv 2024)\n- Diagram Formalization Enhanced Multi-Modal Geometry Problem Solver [DFE-GPS] (AAAI 2025)\n- Geoparsing: Diagram Parsing for Plane and Solid Geometry with a Unified Formal Language (arXiv 2026)\n- TrustGeoGen: Formal-Verified Data Engine for Trustworthy Multi-modal Geometric Problem Solving (arXiv 2025)\n- FormalGeo: An Extensible Formalized Framework for Olympiad Geometric Problem Solving (arXiv 2023)\n- GeoPQA: Bridging the Visual Perception Gap in MLLMs for Geometric Reasoning (EMNLP 2025)\n- Enhancing Geometric Perception in VLMs via Translator-Guided Reinforcement Learning [GeoDPO] (arXiv 2026)\n- M3-ACE: Rectifying Visual Perception in Multimodal Math Reasoning via Multi-Agentic Context Engineering (arXiv 2026)\n- PDCR: Perception-Decomposed Confidence Reward for Vision-Language Reasoning (arXiv 2026)\n- SSL-R1: Self-Supervised Visual Reinforcement Post-Training for MLLMs (arXiv 2026)\n- Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning [PRCO] (arXiv 2026)\n- MathVista: Evaluating Mathematical Reasoning of Foundation Models in Visual Contexts (ICLR 2024)\n- FGeo-DRL: Deductive Reasoning for Geometric Problems through Deep Reinforcement Learning (arXiv 2024)\n- A Survey of Multimodal Mathematical Reasoning: From Perception, Alignment to Reasoning (arXiv 2026)\n- Figure It Out: Improve the Frontier of Reasoning with Executable Visual States [FIGR] (arXiv 2025)\n- Milestones over Outcome: Unlocking Geometric Reasoning with Sub-Goal Verifiable Reward (arXiv 2025)\n- PFlowNet: Perceptual Flow Network for Visually Grounded Reasoning (arXiv 2026)\n- Measuring Multimodal Mathematical Reasoning with MATH-Vision Dataset [MathVision] (NeurIPS 2024)\n- V-Zero: Zero-Shot Multimodal Reasoning via Cross-Modal Self-Play (arXiv 2026)\n\n## Resource Estimate\n\n- **manual**: gpu_hours: 1500-1800 (8×H100: axiom checker development, Stage 0 SFT, 4-5 GRPO training runs at ~30h each, ablation studies, multi-benchmark evaluation, Qwen3-VL-3B replication), timeline: 9-11 weeks (2 wks axiom checker + data pipeline + Stage 0 SFT, 3-4 wks RL training iterations, 2-3 wks evaluation + ablation + paper writing), estimated_gpu_cost: $3,750-$4,500\n- **human_in_loop**: gpu_hours: 1000-1400 (Claude accelerates axiom checker coding, reward function design, and ablation analysis), timeline: 6-8 weeks, claude_api_cost: $400-$700, estimated_gpu_cost: $2,500-$3,500\n- **auto_research**: gpu_hours: 1800-2400 (broader axiom-weight tuning, architecture search over reward combinations, automated multi-seed runs, scale-transfer experiments), timeline: 4-6 weeks, claude_api_cost: $900-$1,400, estimated_gpu_cost: $4,500-$6,000, speed_bottleneck: RL convergence under potentially sparse axiom-violation signals; constraint checker robustness on degenerate/ambiguous diagram parses"
}
```

---

### Runtime record

_source line 2 · 2026-05-27T08:43:57.496Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T08:43:57.496Z",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164"
}
```

---

## Round 1

61 recorded events

### User

_source line 3 · 2026-05-27T08:43:57.563Z_

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
  "promptId": "d4c50c87-a492-4ccd-ad5a-7cc9da96dc22",
  "type": "user",
  "uuid": "037bf19f-a3f6-4a2f-b0d4-cbd9d3649ad2",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-27T08:43:57.562Z_

```json
{
  "parentUuid": "037bf19f-a3f6-4a2f-b0d4-cbd9d3649ad2",
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
  "uuid": "78cd595c-b0d5-4520-a60d-6ccf48dda63f",
  "timestamp": "2026-05-27T08:43:57.562Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-27T08:43:57.562Z_

```json
{
  "parentUuid": "78cd595c-b0d5-4520-a60d-6ccf48dda63f",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "872a13a3-1a04-4080-bae9-ad659d2843ef",
  "timestamp": "2026-05-27T08:43:57.562Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164",
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
  "leafUuid": "872a13a3-1a04-4080-bae9-ad659d2843ef",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Axiom-grounded self-verified perception for math reasoning",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164"
}
```

---

### Assistant

_source line 8 · 2026-05-27T08:44:02.234Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze this proposal as the 补救 agent (remediation agent), focusing exclusively on experimental design and technical execution completeness. I need to first do thorough literature research to understand the current experimental standards in this field before making any recommendations.

Let me start by searching for the key papers mentioned and understanding the experimental landscape.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "872a13a3-1a04-4080-bae9-ad659d2843ef",
  "isSidechain": false,
  "requestId": "req_011CbSn7F2MEwXP2x6Be7u5m",
  "type": "assistant",
  "uuid": "53d98ef7-b2fb-424d-84ad-5b3f9f20ddee",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017jzNTnKDnwvFePS9VsVcHr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5274,
      "cache_read_input_tokens": 14080,
      "output_tokens": 192,
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
          "output_tokens": 192,
          "cache_read_input_tokens": 14080,
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

_source line 9 · 2026-05-27T08:44:03.288Z_

I need to do thorough pre-research before making any experimental design recommendations. Let me search for the key papers and understand current experimental standards in this field.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53d98ef7-b2fb-424d-84ad-5b3f9f20ddee",
  "isSidechain": false,
  "requestId": "req_011CbSn7F2MEwXP2x6Be7u5m",
  "type": "assistant",
  "uuid": "df71fc08-6e8d-4a01-b0df-f5dfe6da2146",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017jzNTnKDnwvFePS9VsVcHr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5274,
      "cache_read_input_tokens": 14080,
      "output_tokens": 192,
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
          "output_tokens": 192,
          "cache_read_input_tokens": 14080,
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

_source line 10 · 2026-05-27T08:44:03.602Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_017BbgqHk91898kt2CCWLJgb`</summary>

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
  "parentUuid": "df71fc08-6e8d-4a01-b0df-f5dfe6da2146",
  "isSidechain": false,
  "requestId": "req_011CbSn7F2MEwXP2x6Be7u5m",
  "type": "assistant",
  "uuid": "84b843a7-340b-421b-90c9-c9e18fd72049",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017jzNTnKDnwvFePS9VsVcHr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5274,
      "cache_read_input_tokens": 14080,
      "output_tokens": 192,
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
          "output_tokens": 192,
          "cache_read_input_tokens": 14080,
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

_source line 11 · 2026-05-27T08:44:03.609Z_

<details><summary>↩ Tool result · `toolu_017BbgqHk91898kt2CCWLJgb`</summary>

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
  "parentUuid": "84b843a7-340b-421b-90c9-c9e18fd72049",
  "isSidechain": false,
  "promptId": "d4c50c87-a492-4ccd-ad5a-7cc9da96dc22",
  "type": "user",
  "uuid": "5678a6cf-4e76-4eab-a4cb-02316f2d1032",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "84b843a7-340b-421b-90c9-c9e18fd72049",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-27T08:44:06.502Z_

Now let me conduct my pre-research. I'll search for the key papers and experimental standards in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5678a6cf-4e76-4eab-a4cb-02316f2d1032",
  "isSidechain": false,
  "requestId": "req_011CbSn7h3mnJCyCZ5EkEPxT",
  "type": "assistant",
  "uuid": "d2795eeb-53b0-447f-aedc-fa129c9c4190",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FBdPsbm2eFUBmybCj5amKn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 720,
      "cache_read_input_tokens": 19354,
      "output_tokens": 95,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 720,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 95,
          "cache_read_input_tokens": 19354,
          "cache_creation_input_tokens": 720,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 720
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

_source line 13 · 2026-05-27T08:44:06.732Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017vxxCvt4qETTCJFP3hNmNM`</summary>

```json
{
  "query": "Perception-R1 visual perception reward multimodal math reasoning experiments baselines 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2795eeb-53b0-447f-aedc-fa129c9c4190",
  "isSidechain": false,
  "requestId": "req_011CbSn7h3mnJCyCZ5EkEPxT",
  "type": "assistant",
  "uuid": "fda55fa9-dfcb-4648-9f35-575087f33445",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FBdPsbm2eFUBmybCj5amKn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 720,
      "cache_read_input_tokens": 19354,
      "output_tokens": 95,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 720,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 95,
          "cache_read_input_tokens": 19354,
          "cache_creation_input_tokens": 720,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 720
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

_source line 14 · 2026-05-27T08:44:14.389Z_

<details><summary>↩ Tool result · `toolu_017vxxCvt4qETTCJFP3hNmNM`</summary>

```text
Web search results for query: "Perception-R1 visual perception reward multimodal math reasoning experiments baselines 2025"

Links: [{"title":"GitHub - tongxiao2002/Perception-R1: The official repo of paper: \"Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward\"","url":"https://github.com/tongxiao2002/Perception-R1"},{"title":"Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward","url":"https://arxiv.org/html/2506.07218v2"},{"title":"[2506.07218] Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward","url":"https://arxiv.org/abs/2506.07218"},{"title":"Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward [Quick Review]","url":"https://liner.com/review/perceptionr1-advancing-multimodal-reasoning-capabilities-of-mllms-via-visual-perception"},{"title":"VTPerception-R1: Enhancing Multimodal Reasoning via ...","url":"https://www.arxiv.org/pdf/2509.24776"},{"title":"Enhancing MLLM Reasoning with Visual Rewards","url":"https://www.emergentmind.com/papers/2506.07218"},{"title":"Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward","url":"https://arxiv.org/pdf/2506.07218"},{"title":"VTPerception-R1: Enhancing Multimodal Reasoning via Explicit Visual and Textual Perceptual Grounding","url":"https://arxiv.org/html/2509.24776"}]

Based on the search results, here's what I found about Perception-R1:

## Overview

Perception-R1 introduces a novel visual perception reward that explicitly encourages MLLMs to perceive visual content accurately, thereby effectively incentivizing both their multimodal perception and reasoning capabilities.

## Methodology

The approach collects textual visual annotations from Chain-of-Thought (CoT) trajectories of multimodal problems as visual references for reward assignment, and during RLVR training, a judging LLM assesses consistency between visual annotations and MLLM responses to assign visual perception rewards.

## Experimental Results

Perception-R1 demonstrates strong multimodal reasoning capabilities across several challenging and widely-used multimodal math benchmarks, outperforming baselines trained on 10–100× more data. The evaluation covers challenging multimodal benchmarks including math benchmarks (MathVista, MathVerse, MathVision, and WeMath) and general benchmarks (MMMU, MMMU-Pro, MMStar, and EMMA).

## Training Efficiency

The method achieves superior performance on all benchmarks using only 1,442 training data. For example, Perception-R1-7B scores 60.8 on MMMU val overall and 64.5 on MMStar val full, surpassing most baselines.

The code and dataset are available at the GitHub repository: https://github.com/tongxiao2002/Perception-R1


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fda55fa9-dfcb-4648-9f35-575087f33445",
  "isSidechain": false,
  "promptId": "d4c50c87-a492-4ccd-ad5a-7cc9da96dc22",
  "type": "user",
  "uuid": "962b9983-eedc-47ca-93de-14c94020e238",
  "toolUseResult": {
    "query": "Perception-R1 visual perception reward multimodal math reasoning experiments baselines 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01ABNmYpYYRnAGUmDDp7pHVu",
        "content": [
          {
            "title": "GitHub - tongxiao2002/Perception-R1: The official repo of paper: \"Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward\"",
            "url": "https://github.com/tongxiao2002/Perception-R1"
          },
          {
            "title": "Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward",
            "url": "https://arxiv.org/html/2506.07218v2"
          },
          {
            "title": "[2506.07218] Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward",
            "url": "https://arxiv.org/abs/2506.07218"
          },
          {
            "title": "Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward [Quick Review]",
            "url": "https://liner.com/review/perceptionr1-advancing-multimodal-reasoning-capabilities-of-mllms-via-visual-perception"
          },
          {
            "title": "VTPerception-R1: Enhancing Multimodal Reasoning via ...",
            "url": "https://www.arxiv.org/pdf/2509.24776"
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
            "title": "VTPerception-R1: Enhancing Multimodal Reasoning via Explicit Visual and Textual Perceptual Grounding",
            "url": "https://arxiv.org/html/2509.24776"
          }
        ]
      },
      "Based on the search results, here's what I found about Perception-R1:\n\n## Overview\n\nPerception-R1 introduces a novel visual perception reward that explicitly encourages MLLMs to perceive visual content accurately, thereby effectively incentivizing both their multimodal perception and reasoning capabilities.\n\n## Methodology\n\nThe approach collects textual visual annotations from Chain-of-Thought (CoT) trajectories of multimodal problems as visual references for reward assignment, and during RLVR training, a judging LLM assesses consistency between visual annotations and MLLM responses to assign visual perception rewards.\n\n## Experimental Results\n\nPerception-R1 demonstrates strong multimodal reasoning capabilities across several challenging and widely-used multimodal math benchmarks, outperforming baselines trained on 10–100× more data. The evaluation covers challenging multimodal benchmarks including math benchmarks (MathVista, MathVerse, MathVision, and WeMath) and general benchmarks (MMMU, MMMU-Pro, MMStar, and EMMA).\n\n## Training Efficiency\n\nThe method achieves superior performance on all benchmarks using only 1,442 training data. For example, Perception-R1-7B scores 60.8 on MMMU val overall and 64.5 on MMStar val full, surpassing most baselines.\n\nThe code and dataset are available at the GitHub repository: https://github.com/tongxiao2002/Perception-R1"
    ],
    "durationSeconds": 7.6485513350000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "fda55fa9-dfcb-4648-9f35-575087f33445",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-27T08:44:17.393Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012XEzcnPDdCDr1vPrNxnyWK`</summary>

```json
{
  "query": "PEARL perceptual evidence anchored reinforcement learning MathVerse experiments ablation 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "962b9983-eedc-47ca-93de-14c94020e238",
  "isSidechain": false,
  "requestId": "req_011CbSn8Uv3pde5LB2QJSt6k",
  "type": "assistant",
  "uuid": "c82a1640-e8ab-4b47-ac3a-7b4c5c59ca54",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Efqe8R1ULX9Z4kNfdpvGEV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 927,
      "cache_read_input_tokens": 20074,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 927,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 20074,
          "cache_creation_input_tokens": 927,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 927
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

_source line 16 · 2026-05-27T08:44:30.420Z_

<details><summary>↩ Tool result · `toolu_012XEzcnPDdCDr1vPrNxnyWK`</summary>

```text
Web search results for query: "PEARL perceptual evidence anchored reinforcement learning MathVerse experiments ablation 2025"

Links: [{"title":"Perceptual-Evidence Anchored Reinforced Learning for Multimodal Reasoning","url":"https://arxiv.org/html/2511.18437"},{"title":"Perceptual-Evidence Anchored Reinforced Learning for Multimodal Reasoning","url":"https://arxiv.org/pdf/2511.18437"},{"title":"000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019","url":"https://openreview.net/pdf?id=UyAJQQPU4W"},{"title":"Enhancing MLLM Reasoning with Visual Rewards","url":"https://www.emergentmind.com/papers/2506.07218"},{"title":"Credit Where It is Due: Cross-Modality Connectivity Drives Precise Reinforcement Learning for MLLM Reasoning","url":"https://arxiv.org/pdf/2602.11455"}]

Based on the search results, here's what I found about PEARL and its experiments:

## PEARL Overview

PEARL (Perceptual-Evidence Anchored Reinforced Learning) is a dual-branch, perception-reasoning synergistic that strengthens multimodal reasoning by explicitly anchoring it to verified visual evidence.

## How PEARL Works

For each reasoning-oriented QA instance, PEARL first derives a perception checklist—a set of perception-oriented sub-questions with verifiable answers that probe the model's understanding of key visual evidence. During training, auxiliary rollouts on this checklist yield a perceptual reward that both directly reinforces the model's perception ability and acts as a fidelity gate for reasoning. If the model passes the perception check, its policy update is biased towards evidence-anchored reasoning.

## MathVerse Experiments Results

PEARL manages to identify room for improvement, boosting performance by +3% on MathVerse and +5.1% on WeMath. This indicates that explicitly guiding models to answer basic perception probes can still enhance performance, even for highly capable models.

The research paper was published on arXiv in November 2025 with contributions from researchers at Wuhan University, Meituan Inc, and The University of Sydney.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c82a1640-e8ab-4b47-ac3a-7b4c5c59ca54",
  "isSidechain": false,
  "promptId": "d4c50c87-a492-4ccd-ad5a-7cc9da96dc22",
  "type": "user",
  "uuid": "261e95fb-66c1-4978-96db-783125bb2235",
  "toolUseResult": {
    "query": "PEARL perceptual evidence anchored reinforcement learning MathVerse experiments ablation 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_016Vh9hMFNxnYXzBKPNLVK4n",
        "content": [
          {
            "title": "Perceptual-Evidence Anchored Reinforced Learning for Multimodal Reasoning",
            "url": "https://arxiv.org/html/2511.18437"
          },
          {
            "title": "Perceptual-Evidence Anchored Reinforced Learning for Multimodal Reasoning",
            "url": "https://arxiv.org/pdf/2511.18437"
          },
          {
            "title": "000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019",
            "url": "https://openreview.net/pdf?id=UyAJQQPU4W"
          },
          {
            "title": "Enhancing MLLM Reasoning with Visual Rewards",
            "url": "https://www.emergentmind.com/papers/2506.07218"
          },
          {
            "title": "Credit Where It is Due: Cross-Modality Connectivity Drives Precise Reinforcement Learning for MLLM Reasoning",
            "url": "https://arxiv.org/pdf/2602.11455"
          }
        ]
      },
      "Based on the search results, here's what I found about PEARL and its experiments:\n\n## PEARL Overview\n\nPEARL (Perceptual-Evidence Anchored Reinforced Learning) is a dual-branch, perception-reasoning synergistic that strengthens multimodal reasoning by explicitly anchoring it to verified visual evidence.\n\n## How PEARL Works\n\nFor each reasoning-oriented QA instance, PEARL first derives a perception checklist—a set of perception-oriented sub-questions with verifiable answers that probe the model's understanding of key visual evidence. During training, auxiliary rollouts on this checklist yield a perceptual reward that both directly reinforces the model's perception ability and acts as a fidelity gate for reasoning. If the model passes the perception check, its policy update is biased towards evidence-anchored reasoning.\n\n## MathVerse Experiments Results\n\nPEARL manages to identify room for improvement, boosting performance by +3% on MathVerse and +5.1% on WeMath. This indicates that explicitly guiding models to answer basic perception probes can still enhance performance, even for highly capable models.\n\nThe research paper was published on arXiv in November 2025 with contributions from researchers at Wuhan University, Meituan Inc, and The University of Sydney."
    ],
    "durationSeconds": 13.020180733999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c82a1640-e8ab-4b47-ac3a-7b4c5c59ca54",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-27T08:44:33.265Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JXmQLgvADbgVmAgqL3XNUN`</summary>

```json
{
  "query": "GeoDPO geometric perception VLM translator-guided reinforcement learning experiments evaluation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "261e95fb-66c1-4978-96db-783125bb2235",
  "isSidechain": false,
  "requestId": "req_011CbSn9fR6obz2VmCdyyQ82",
  "type": "assistant",
  "uuid": "8825738b-c256-4f13-8aa6-bafa195ba904",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LRd7YnbrRiHu2ZuRtXwFS4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 658,
      "cache_read_input_tokens": 21001,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 658,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 21001,
          "cache_creation_input_tokens": 658,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 658
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

_source line 18 · 2026-05-27T08:44:40.476Z_

<details><summary>↩ Tool result · `toolu_01JXmQLgvADbgVmAgqL3XNUN`</summary>

```text
Web search results for query: "GeoDPO geometric perception VLM translator-guided reinforcement learning experiments evaluation 2026"

Links: [{"title":"Enhancing Geometric Perception in VLMs via Translator-Guided Reinforcement Learning","url":"https://arxiv.org/pdf/2602.22703"},{"title":"Enhancing Geometric Perception in VLMs via Translator-Guided Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=O70LkLl3gW"},{"title":"[2602.22703] Enhancing Geometric Perception in VLMs via Translator-Guided Reinforcement Learning","url":"https://arxiv.org/abs/2602.22703"},{"title":"Does VLM Always Fail in Solving Geometry Problems? GEODPO: Starting from \"Seeing\", Using Structured Representation + DPO Optimization to Enable Model Understanding before Reasoning","url":"https://eu.36kr.com/en/p/3745344269893891"},{"title":"Geo-R1: Unlocking VLM Geospatial Reasoning with Cross-View Reinforcement Learning","url":"https://arxiv.org/pdf/2510.00072"}]

I found research on GeoDPO! Here are the key findings:

## GeoDPO: Enhancing Geometric Perception in VLMs

Vision-language models (VLMs) often struggle with geometric reasoning due to their limited perception of fundamental diagram elements. 

**The Proposed Solution:**

Researchers introduced GeoPerceive, a benchmark comprising diagram instances paired with domain-specific language (DSL) representations, along with an efficient automatic data generation pipeline that enables isolated evaluation of geometric perception independently from reasoning.

GeoDPO is a translator-guided reinforcement learning framework that employs an NL-to-DSL translator trained on synthetic pairs to bridge natural language and DSL, facilitating the computation of fine-grained, DSL-level scores which serve as reward signals in reinforcement learning.

**Experimental Results:**

The framework was assessed on both in-domain and out-of-domain datasets, spanning tasks in geometric perception as well as downstream reasoning, achieving substantial gains of +26.5% on in-domain data, +8.0% on out-of-domain data, and +39.0% on downstream reasoning tasks. These findings underscore the superior performance and generalization ability of GeoDPO over supervised fine-tuning (SFT).

The research was published on arxiv in February 2026, and the code is available on GitHub for reproducibility.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8825738b-c256-4f13-8aa6-bafa195ba904",
  "isSidechain": false,
  "promptId": "d4c50c87-a492-4ccd-ad5a-7cc9da96dc22",
  "type": "user",
  "uuid": "44f5bc87-a635-4d5a-ad75-35de875f6beb",
  "toolUseResult": {
    "query": "GeoDPO geometric perception VLM translator-guided reinforcement learning experiments evaluation 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VpAA5KqVVAG3GQWmDqmu6A",
        "content": [
          {
            "title": "Enhancing Geometric Perception in VLMs via Translator-Guided Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2602.22703"
          },
          {
            "title": "Enhancing Geometric Perception in VLMs via Translator-Guided Reinforcement Learning | OpenReview",
            "url": "https://openreview.net/forum?id=O70LkLl3gW"
          },
          {
            "title": "[2602.22703] Enhancing Geometric Perception in VLMs via Translator-Guided Reinforcement Learning",
            "url": "https://arxiv.org/abs/2602.22703"
          },
          {
            "title": "Does VLM Always Fail in Solving Geometry Problems? GEODPO: Starting from \"Seeing\", Using Structured Representation + DPO Optimization to Enable Model Understanding before Reasoning",
            "url": "https://eu.36kr.com/en/p/3745344269893891"
          },
          {
            "title": "Geo-R1: Unlocking VLM Geospatial Reasoning with Cross-View Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2510.00072"
          }
        ]
      },
      "I found research on GeoDPO! Here are the key findings:\n\n## GeoDPO: Enhancing Geometric Perception in VLMs\n\nVision-language models (VLMs) often struggle with geometric reasoning due to their limited perception of fundamental diagram elements. \n\n**The Proposed Solution:**\n\nResearchers introduced GeoPerceive, a benchmark comprising diagram instances paired with domain-specific language (DSL) representations, along with an efficient automatic data generation pipeline that enables isolated evaluation of geometric perception independently from reasoning.\n\nGeoDPO is a translator-guided reinforcement learning framework that employs an NL-to-DSL translator trained on synthetic pairs to bridge natural language and DSL, facilitating the computation of fine-grained, DSL-level scores which serve as reward signals in reinforcement learning.\n\n**Experimental Results:**\n\nThe framework was assessed on both in-domain and out-of-domain datasets, spanning tasks in geometric perception as well as downstream reasoning, achieving substantial gains of +26.5% on in-domain data, +8.0% on out-of-domain data, and +39.0% on downstream reasoning tasks. These findings underscore the superior performance and generalization ability of GeoDPO over supervised fine-tuning (SFT).\n\nThe research was published on arxiv in February 2026, and the code is available on GitHub for reproducibility."
    ],
    "durationSeconds": 7.206689661000004,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "8825738b-c256-4f13-8aa6-bafa195ba904",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-27T08:44:42.915Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WW3YXxsnZNCZpYjNUK7e66`</summary>

```json
{
  "query": "EVPV \"explicit visual premise verification\" VLM process reward model experiments baselines 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "44f5bc87-a635-4d5a-ad75-35de875f6beb",
  "isSidechain": false,
  "requestId": "req_011CbSnAQQVJTxYXoydrQodV",
  "type": "assistant",
  "uuid": "1665637f-ff0a-4908-93f7-47a243590d10",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U5Uh3qzVkTqYipqYT4zVqF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 700,
      "cache_read_input_tokens": 21659,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 700,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 21659,
          "cache_creation_input_tokens": 700,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 700
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

_source line 20 · 2026-05-27T08:44:50.831Z_

<details><summary>↩ Tool result · `toolu_01WW3YXxsnZNCZpYjNUK7e66`</summary>

```text
Web search results for query: "EVPV "explicit visual premise verification" VLM process reward model experiments baselines 2026"

Links: [{"title":"Grounding the Score: Explicit Visual Premise Verification for Reliable VLM Process Reward Models","url":"https://arxiv.org/html/2603.16253"},{"title":"[2603.16253] Grounding the Score: Explicit Visual Premise Verification for Reliable Vision-Language Process Reward Models","url":"https://arxiv.org/abs/2603.16253"},{"title":"Grounding the Score: Explicit Visual Premise Verification for Reliable Vision-Language Process Reward Models","url":"https://arxiv.org/pdf/2603.16253"},{"title":"GitHub - Qwen-Applications/EVPV-PRM · GitHub","url":"https://github.com/Qwen-Applications/EVPV-PRM"},{"title":"Self-Rewarding Vision-Language Model via Reasoning Decomposition","url":"https://arxiv.org/html/2508.19652v1"}]

I found relevant information about EVPV (Explicit Visual Premise Verification) and the VLM process reward model research. Here's what the search revealed:

## EVPV Overview

EVPV is a lightweight verification interface that conditions step scoring on the reliability of the visual premises a step depends on. Vision-language process reward models (VL-PRMs) are increasingly used to score intermediate reasoning steps and rerank candidates under test-time scaling, but they often function as black-box judges where a low step score may reflect either a genuine reasoning mistake or simply the verifier's misperception of the image, leading to systematic false positives and false negatives.

## Methodology

The policy is prompted to produce a step-wise visual checklist that makes required visual facts explicit, while a constraint extractor independently derives structured visual constraints from the input image. EVPV matches checklist claims against these constraints to compute a scalar visual reliability signal, and calibrates PRM step rewards via reliability gating, decoupling perceptual uncertainty from logical evaluation without per-step tool calls.

## Experimental Results

Experiments on VisualProcessBench and six multimodal reasoning benchmarks show that EVPV improves step-level verification and consistently boosts Best-of-N reranking accuracy over strong baselines. The research was published on March 17, 2026, and is available on arXiv (2603.16253) with code available on GitHub through the Qwen Applications repository.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1665637f-ff0a-4908-93f7-47a243590d10",
  "isSidechain": false,
  "promptId": "d4c50c87-a492-4ccd-ad5a-7cc9da96dc22",
  "type": "user",
  "uuid": "33079c3c-2e77-4bc6-9648-eb653a109808",
  "toolUseResult": {
    "query": "EVPV \"explicit visual premise verification\" VLM process reward model experiments baselines 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VGYQaoYLqHK1z5Jjq9nS9h",
        "content": [
          {
            "title": "Grounding the Score: Explicit Visual Premise Verification for Reliable VLM Process Reward Models",
            "url": "https://arxiv.org/html/2603.16253"
          },
          {
            "title": "[2603.16253] Grounding the Score: Explicit Visual Premise Verification for Reliable Vision-Language Process Reward Models",
            "url": "https://arxiv.org/abs/2603.16253"
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
            "url": "https://arxiv.org/html/2508.19652v1"
          }
        ]
      },
      "I found relevant information about EVPV (Explicit Visual Premise Verification) and the VLM process reward model research. Here's what the search revealed:\n\n## EVPV Overview\n\nEVPV is a lightweight verification interface that conditions step scoring on the reliability of the visual premises a step depends on. Vision-language process reward models (VL-PRMs) are increasingly used to score intermediate reasoning steps and rerank candidates under test-time scaling, but they often function as black-box judges where a low step score may reflect either a genuine reasoning mistake or simply the verifier's misperception of the image, leading to systematic false positives and false negatives.\n\n## Methodology\n\nThe policy is prompted to produce a step-wise visual checklist that makes required visual facts explicit, while a constraint extractor independently derives structured visual constraints from the input image. EVPV matches checklist claims against these constraints to compute a scalar visual reliability signal, and calibrates PRM step rewards via reliability gating, decoupling perceptual uncertainty from logical evaluation without per-step tool calls.\n\n## Experimental Results\n\nExperiments on VisualProcessBench and six multimodal reasoning benchmarks show that EVPV improves step-level verification and consistently boosts Best-of-N reranking accuracy over strong baselines. The research was published on March 17, 2026, and is available on arXiv (2603.16253) with code available on GitHub through the Qwen Applications repository."
    ],
    "durationSeconds": 7.911859490000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "1665637f-ff0a-4908-93f7-47a243590d10",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164",
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
  "leafUuid": "33079c3c-2e77-4bc6-9648-eb653a109808",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Axiom-grounded self-verified perception for math reasoning",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164"
}
```

---

### Tool call

_source line 23 · 2026-05-27T08:44:53.553Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Qy9g9K6suX4Jz1x9F8etYV`</summary>

```json
{
  "query": "SSL-R1 self-supervised visual reinforcement learning MLLM experiments benchmarks evaluation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33079c3c-2e77-4bc6-9648-eb653a109808",
  "isSidechain": false,
  "requestId": "req_011CbSnBAydePEZa6mEJKZ6k",
  "type": "assistant",
  "uuid": "b31098ee-7736-4f8c-aa1b-53759b416d88",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BKkvB8Gp4YQwTaMLLJnnfu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 687,
      "cache_read_input_tokens": 22359,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 687,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 22359,
          "cache_creation_input_tokens": 687,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 687
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

_source line 24 · 2026-05-27T08:45:03.680Z_

<details><summary>↩ Tool result · `toolu_01Qy9g9K6suX4Jz1x9F8etYV`</summary>

```text
Web search results for query: "SSL-R1 self-supervised visual reinforcement learning MLLM experiments benchmarks evaluation 2026"

Links: [{"title":"SSL-R1: Self-Supervised Visual Reinforcement Post-Training for Multimodal Large Language Models","url":"https://arxiv.org/html/2604.20705"},{"title":"[2604.20705] SSL-R1: Self-Supervised Visual Reinforcement Post-Training for Multimodal Large Language Models","url":"https://arxiv.org/abs/2604.20705"},{"title":"ViSS-R1: Self-Supervised Reinforcement Video Reasoning","url":"https://arxiv.org/html/2511.13054"},{"title":"Awesome-LLM-RLVR/README.md at main · smiles724/Awesome-LLM-RLVR","url":"https://github.com/smiles724/Awesome-LLM-RLVR/blob/main/README.md"},{"title":"GitHub - smiles724/Awesome-LLM-RLVR: Collection of latest papers and materials in the area of RLVR! · GitHub","url":"https://github.com/smiles724/Awesome-LLM-RLVR"},{"title":"Visual Jigsaw Post-Training Improves MLLMs","url":"https://arxiv.org/pdf/2509.25190"},{"title":"ViSS-R1: Self-Supervised Reinforcement Video Reasoning","url":"https://arxiv.org/pdf/2511.13054"}]

Based on the search results, here's what I found about SSL-R1:

## Overview

SSL-R1 is a generic self-supervised RL post-training framework that derives verifiable rewards intrinsically from images, requiring neither human nor model supervision. It derives verifiable rewards directly from images by reformulating widely-used self-supervised learning tasks into a set of verifiable visual puzzles for RL post-training.

## Experiments and Benchmarks

The method was evaluated on a wide range of multimodal understanding benchmarks, including fine-grained perception, spatial understanding, and compositional understanding. The experiments used Qwen2.5-VL-3B-Instruct as the base MLLM.

## Key Findings

In single-task post-training experiments, the greatest gains came from Geometric Correspondence, achieving an average gain of +2.13% across 13 benchmarks compared to the baseline, followed by Patch Ordering (+1.92%), Rotation Prediction (+1.80%), and Visual Similarity (+1.60%).

Extensive experimental results demonstrate that the method substantially improves the vision-centric capabilities of MLLMs.

The paper was published on April 22, 2026, and represents recent work in the area of self-supervised reinforcement learning for multimodal understanding.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b31098ee-7736-4f8c-aa1b-53759b416d88",
  "isSidechain": false,
  "promptId": "d4c50c87-a492-4ccd-ad5a-7cc9da96dc22",
  "type": "user",
  "uuid": "8d037489-2d61-4afd-a27a-17f1b4fb32b9",
  "toolUseResult": {
    "query": "SSL-R1 self-supervised visual reinforcement learning MLLM experiments benchmarks evaluation 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01ANJUuijkMvLSgc2YKBViZp",
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
            "title": "ViSS-R1: Self-Supervised Reinforcement Video Reasoning",
            "url": "https://arxiv.org/html/2511.13054"
          },
          {
            "title": "Awesome-LLM-RLVR/README.md at main · smiles724/Awesome-LLM-RLVR",
            "url": "https://github.com/smiles724/Awesome-LLM-RLVR/blob/main/README.md"
          },
          {
            "title": "GitHub - smiles724/Awesome-LLM-RLVR: Collection of latest papers and materials in the area of RLVR! · GitHub",
            "url": "https://github.com/smiles724/Awesome-LLM-RLVR"
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
      "Based on the search results, here's what I found about SSL-R1:\n\n## Overview\n\nSSL-R1 is a generic self-supervised RL post-training framework that derives verifiable rewards intrinsically from images, requiring neither human nor model supervision. It derives verifiable rewards directly from images by reformulating widely-used self-supervised learning tasks into a set of verifiable visual puzzles for RL post-training.\n\n## Experiments and Benchmarks\n\nThe method was evaluated on a wide range of multimodal understanding benchmarks, including fine-grained perception, spatial understanding, and compositional understanding. The experiments used Qwen2.5-VL-3B-Instruct as the base MLLM.\n\n## Key Findings\n\nIn single-task post-training experiments, the greatest gains came from Geometric Correspondence, achieving an average gain of +2.13% across 13 benchmarks compared to the baseline, followed by Patch Ordering (+1.92%), Rotation Prediction (+1.80%), and Visual Similarity (+1.60%).\n\nExtensive experimental results demonstrate that the method substantially improves the vision-centric capabilities of MLLMs.\n\nThe paper was published on April 22, 2026, and represents recent work in the area of self-supervised reinforcement learning for multimodal understanding."
    ],
    "durationSeconds": 10.123121091000009,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "b31098ee-7736-4f8c-aa1b-53759b416d88",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-27T08:45:06.653Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VnYiDCZ8Tr5UGhGnRcZ7bu`</summary>

```json
{
  "query": "Geoparsing diagram parsing plane solid geometry unified formal language experiments evaluation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d037489-2d61-4afd-a27a-17f1b4fb32b9",
  "isSidechain": false,
  "requestId": "req_011CbSnC7ckGvGywZJERThWt",
  "type": "assistant",
  "uuid": "f9ad6eac-11af-466b-9f3a-69ffd75a28bc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018vxSjKWsft3vXpRrAshhYz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 782,
      "cache_read_input_tokens": 23046,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 782,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 23046,
          "cache_creation_input_tokens": 782,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 782
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

_source line 26 · 2026-05-27T08:45:13.967Z_

<details><summary>↩ Tool result · `toolu_01VnYiDCZ8Tr5UGhGnRcZ7bu`</summary>

```text
Web search results for query: "Geoparsing diagram parsing plane solid geometry unified formal language experiments evaluation 2026"

Links: [{"title":"[2604.11600] Geoparsing: Diagram Parsing for Plane and Solid Geometry with a Unified Formal Language","url":"https://arxiv.org/abs/2604.11600"},{"title":"Geoparsing: Diagram Parsing for Plane and Solid Geometry with a Unified Formal Language","url":"https://arxiv.org/html/2604.11600"},{"title":"Diagram Parsing for Plane and Solid Geometry with a Unified Formal Language | OpenReview","url":"https://openreview.net/forum?id=Jivgo2qRGI"},{"title":"Plane Geometry Diagram Parsing","url":"https://arxiv.org/pdf/2205.09363"},{"title":"PGDP5K: A Diagram Parsing Dataset for Plane Geometry Problems | Request PDF","url":"https://www.researchgate.net/publication/365865613_PGDP5K_A_Diagram_Parsing_Dataset_for_Plane_Geometry_Problems"},{"title":"GeoX: Geometric Problem Solving Through Unified Formalized Vision-Language Pre-training","url":"https://arxiv.org/html/2412.11863v1"}]

I found comprehensive information about the Geoparsing research. Here are the key findings:

## Geoparsing: Diagram Parsing for Plane and Solid Geometry

The research addresses the challenge by designing a unified formal language that integrates plane and solid geometry, comprehensively covering geometric structures and semantic relations.

### Dataset and Methodology

The researchers constructed GDP-29K, a large-scale dataset comprising 20k plane and 9k solid geometry samples collected from diverse real-world sources, each paired with its ground-truth formal description. To ensure syntactic correctness and geometric consistency, they propose a training paradigm that combines Supervised Fine-Tuning with Reinforcement Learning via Verifiable Rewards.

### Experimental Results

Experiments show that the approach achieves state-of-the-art parsing performance. The parsed formal descriptions serve as a critical cognitive scaffold, significantly boosting MLLMs' capabilities for downstream geometry reasoning tasks.

### Problem Addressed

Multimodal Large Language Models (MLLMs) continue to struggle with geometric reasoning, primarily due to the perception bottleneck regarding fine-grained visual elements. While formal languages have aided plane geometry understanding, solid geometry which requires spatial understanding remains largely unexplored.

The paper was published on arXiv on April 16, 2026 (arxiv.org/abs/2604.11600).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f9ad6eac-11af-466b-9f3a-69ffd75a28bc",
  "isSidechain": false,
  "promptId": "d4c50c87-a492-4ccd-ad5a-7cc9da96dc22",
  "type": "user",
  "uuid": "18f68a3c-cad3-47fd-8dff-ee55be5c3313",
  "toolUseResult": {
    "query": "Geoparsing diagram parsing plane solid geometry unified formal language experiments evaluation 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_017HJVgjuDSJyxVf6zsttBC1",
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
            "title": "Diagram Parsing for Plane and Solid Geometry with a Unified Formal Language | OpenReview",
            "url": "https://openreview.net/forum?id=Jivgo2qRGI"
          },
          {
            "title": "Plane Geometry Diagram Parsing",
            "url": "https://arxiv.org/pdf/2205.09363"
          },
          {
            "title": "PGDP5K: A Diagram Parsing Dataset for Plane Geometry Problems | Request PDF",
            "url": "https://www.researchgate.net/publication/365865613_PGDP5K_A_Diagram_Parsing_Dataset_for_Plane_Geometry_Problems"
          },
          {
            "title": "GeoX: Geometric Problem Solving Through Unified Formalized Vision-Language Pre-training",
            "url": "https://arxiv.org/html/2412.11863v1"
          }
        ]
      },
      "I found comprehensive information about the Geoparsing research. Here are the key findings:\n\n## Geoparsing: Diagram Parsing for Plane and Solid Geometry\n\nThe research addresses the challenge by designing a unified formal language that integrates plane and solid geometry, comprehensively covering geometric structures and semantic relations.\n\n### Dataset and Methodology\n\nThe researchers constructed GDP-29K, a large-scale dataset comprising 20k plane and 9k solid geometry samples collected from diverse real-world sources, each paired with its ground-truth formal description. To ensure syntactic correctness and geometric consistency, they propose a training paradigm that combines Supervised Fine-Tuning with Reinforcement Learning via Verifiable Rewards.\n\n### Experimental Results\n\nExperiments show that the approach achieves state-of-the-art parsing performance. The parsed formal descriptions serve as a critical cognitive scaffold, significantly boosting MLLMs' capabilities for downstream geometry reasoning tasks.\n\n### Problem Addressed\n\nMultimodal Large Language Models (MLLMs) continue to struggle with geometric reasoning, primarily due to the perception bottleneck regarding fine-grained visual elements. While formal languages have aided plane geometry understanding, solid geometry which requires spatial understanding remains largely unexplored.\n\nThe paper was published on arXiv on April 16, 2026 (arxiv.org/abs/2604.11600)."
    ],
    "durationSeconds": 7.309137680999993,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f9ad6eac-11af-466b-9f3a-69ffd75a28bc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-27T08:45:16.901Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QHZGL5XnSJtmtKmLRQTGMQ`</summary>

```json
{
  "query": "multimodal math reasoning RL training perception reward GRPO veRL experiments 2025 2026 state-of-the-art benchmarks"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "18f68a3c-cad3-47fd-8dff-ee55be5c3313",
  "isSidechain": false,
  "requestId": "req_011CbSnCsdQAgWEi6jnJAudR",
  "type": "assistant",
  "uuid": "402ad4d4-dba2-4216-be73-0932e334d0e9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AC9Av3ybiDx4Fdf3eq9G4Z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 727,
      "cache_read_input_tokens": 23828,
      "output_tokens": 83,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 727,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 83,
          "cache_read_input_tokens": 23828,
          "cache_creation_input_tokens": 727,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 727
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

_source line 28 · 2026-05-27T08:45:24.754Z_

<details><summary>↩ Tool result · `toolu_01QHZGL5XnSJtmtKmLRQTGMQ`</summary>

```text
Web search results for query: "multimodal math reasoning RL training perception reward GRPO veRL experiments 2025 2026 state-of-the-art benchmarks"

Links: [{"title":"[2501.04686] Unlocking Multimodal Mathematical Reasoning via Process Reward Model","url":"https://arxiv.org/abs/2501.04686"},{"title":"Unlocking Multimodal Mathematical Reasoning via Process Reward Model | OpenReview","url":"https://openreview.net/forum?id=96I8PGPALv"},{"title":"Multimodal Mathematical Reasoning with Diverse Solving Perspective","url":"https://arxiv.org/pdf/2507.02804"},{"title":"Seeing with You: Perception–Reasoning Coevolution for Multimodal Reasoning","url":"https://arxiv.org/html/2603.28618v1"},{"title":"Multi-modal Reasoning with LLMs for Visual Semantic Arithmetic","url":"https://arxiv.org/html/2604.19567"},{"title":"Unlocking Multimodal Mathematical Reasoning via Process Reward Model","url":"https://arxiv.org/pdf/2501.04686"},{"title":"Perceptual-Evidence Anchored Reinforced Learning for Multimodal Reasoning","url":"https://arxiv.org/pdf/2511.18437"},{"title":"Vision-R1: Incentivizing Reasoning Capability in Multimodal Large Language Models","url":"https://arxiv.org/pdf/2503.06749"}]

Based on the search results, here's what I found regarding multimodal math reasoning with RL training, perception rewards, GRPO, and related techniques from 2025-2026:

## Key Recent Work

**Process-Supervised GRPO (PS-GRPO):** Process-Supervised Group-Relative-Policy-Optimization (PS-GRPO) pioneering a multimodal PRM-aided online RL method outperforms vanilla GRPO. URSA-8B-PS-GRPO outperforms Gemma3-12B and GPT-4o by 8.4% and 2.7% on average across 6 benchmarks.

**Multimodal Reasoning with Diverse Solutions:** Researchers trained models through supervised fine-tuning and group relative policy optimization (GRPO) as rule-based reinforcement learning using diverse solutions for mathematical problems.

**Perception-Reasoning Coevolution:** A critical finding is that effective reasoning relies on accurate perception which provides necessary grounding for logical deduction, but RLVR is often applied in an outcome-driven manner, verifying only the final textual answer while largely neglecting the accuracy of upstream visual perception.

**Perceptual-Evidence Anchored Learning (PEARL):** PEARL can be seamlessly integrated with popular RL methods like GRPO and DAPO, achieving substantial gains like +9.7% improvement over baseline and +6.6% over GRPO on MathVerse.

**Vision-R1:** Following the DeepSeek-R1 training pipeline, Group Relative Policy Optimization (GRPO) is applied on multimodal math datasets to enhance model reasoning capability.

The research indicates a shift toward integrating process rewards and perception-aware training into multimodal RL frameworks, moving beyond simple outcome-based verification.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "402ad4d4-dba2-4216-be73-0932e334d0e9",
  "isSidechain": false,
  "promptId": "d4c50c87-a492-4ccd-ad5a-7cc9da96dc22",
  "type": "user",
  "uuid": "ea2d85fd-e4c3-4970-b123-29b1d2b2f95f",
  "toolUseResult": {
    "query": "multimodal math reasoning RL training perception reward GRPO veRL experiments 2025 2026 state-of-the-art benchmarks",
    "results": [
      {
        "tool_use_id": "srvtoolu_011F5t3o9V4FfyKFEUDAqHxt",
        "content": [
          {
            "title": "[2501.04686] Unlocking Multimodal Mathematical Reasoning via Process Reward Model",
            "url": "https://arxiv.org/abs/2501.04686"
          },
          {
            "title": "Unlocking Multimodal Mathematical Reasoning via Process Reward Model | OpenReview",
            "url": "https://openreview.net/forum?id=96I8PGPALv"
          },
          {
            "title": "Multimodal Mathematical Reasoning with Diverse Solving Perspective",
            "url": "https://arxiv.org/pdf/2507.02804"
          },
          {
            "title": "Seeing with You: Perception–Reasoning Coevolution for Multimodal Reasoning",
            "url": "https://arxiv.org/html/2603.28618v1"
          },
          {
            "title": "Multi-modal Reasoning with LLMs for Visual Semantic Arithmetic",
            "url": "https://arxiv.org/html/2604.19567"
          },
          {
            "title": "Unlocking Multimodal Mathematical Reasoning via Process Reward Model",
            "url": "https://arxiv.org/pdf/2501.04686"
          },
          {
            "title": "Perceptual-Evidence Anchored Reinforced Learning for Multimodal Reasoning",
            "url": "https://arxiv.org/pdf/2511.18437"
          },
          {
            "title": "Vision-R1: Incentivizing Reasoning Capability in Multimodal Large Language Models",
            "url": "https://arxiv.org/pdf/2503.06749"
          }
        ]
      },
      "Based on the search results, here's what I found regarding multimodal math reasoning with RL training, perception rewards, GRPO, and related techniques from 2025-2026:\n\n## Key Recent Work\n\n**Process-Supervised GRPO (PS-GRPO):** Process-Supervised Group-Relative-Policy-Optimization (PS-GRPO) pioneering a multimodal PRM-aided online RL method outperforms vanilla GRPO. URSA-8B-PS-GRPO outperforms Gemma3-12B and GPT-4o by 8.4% and 2.7% on average across 6 benchmarks.\n\n**Multimodal Reasoning with Diverse Solutions:** Researchers trained models through supervised fine-tuning and group relative policy optimization (GRPO) as rule-based reinforcement learning using diverse solutions for mathematical problems.\n\n**Perception-Reasoning Coevolution:** A critical finding is that effective reasoning relies on accurate perception which provides necessary grounding for logical deduction, but RLVR is often applied in an outcome-driven manner, verifying only the final textual answer while largely neglecting the accuracy of upstream visual perception.\n\n**Perceptual-Evidence Anchored Learning (PEARL):** PEARL can be seamlessly integrated with popular RL methods like GRPO and DAPO, achieving substantial gains like +9.7% improvement over baseline and +6.6% over GRPO on MathVerse.\n\n**Vision-R1:** Following the DeepSeek-R1 training pipeline, Group Relative Policy Optimization (GRPO) is applied on multimodal math datasets to enhance model reasoning capability.\n\nThe research indicates a shift toward integrating process rewards and perception-aware training into multimodal RL frameworks, moving beyond simple outcome-based verification."
    ],
    "durationSeconds": 7.846932839999994,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "402ad4d4-dba2-4216-be73-0932e334d0e9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-27T08:45:24.758Z_

```json
{
  "parentUuid": "ea2d85fd-e4c3-4970-b123-29b1d2b2f95f",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "9bc0a28c-b4d8-4bd0-bfb0-8782a01c35cf",
  "timestamp": "2026-05-27T08:45:24.758Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 30 · 2026-05-27T08:45:27.882Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AGtukR9kVBA6cmgxeLv7bT`</summary>

```json
{
  "query": "PRCO \"perception reasoning coevolution\" observer solver multimodal reasoning experiments ablation benchmarks 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9bc0a28c-b4d8-4bd0-bfb0-8782a01c35cf",
  "isSidechain": false,
  "requestId": "req_011CbSnDfiZsmxwYE2Pwg6oj",
  "type": "assistant",
  "uuid": "e105fcef-2e5f-4e2c-a3ac-27cb2aa9ed82",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fi2WmtmAt2ZsdjhHgKMSZA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 996,
      "cache_read_input_tokens": 24555,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 996,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 24555,
          "cache_creation_input_tokens": 996,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 996
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

_source line 31 · 2026-05-27T08:45:33.540Z_

<details><summary>↩ Tool result · `toolu_01AGtukR9kVBA6cmgxeLv7bT`</summary>

```text
Web search results for query: "PRCO "perception reasoning coevolution" observer solver multimodal reasoning experiments ablation benchmarks 2026"

Links: [{"title":"[2603.28618] Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning","url":"https://arxiv.org/abs/2603.28618"},{"title":"Seeing with You: Perception–Reasoning Coevolution for Multimodal Reasoning","url":"https://arxiv.org/html/2603.28618v1"},{"title":"GitHub - Dtc7w3PQ/PRCO: Official implementation of Seeing with You: Perception-Reasoning Co-evolution for Multimodal Reasoning. · GitHub","url":"https://github.com/Dtc7w3PQ/PRCO"},{"title":"Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning | Takara TLDR","url":"https://tldr.takara.ai/p/2603.28618"},{"title":"Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning","url":"https://arxiv.org/pdf/2603.28618"},{"title":"Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning","url":"https://chatpaper.com/paper/262369"},{"title":"Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning | Request PDF","url":"https://www.researchgate.net/publication/403307388_Seeing_with_You_Perception-Reasoning_Coevolution_for_Multimodal_Reasoning"}]

I found relevant information about PRCO. Here's what the search reveals:

## Overview

PRCO (Perception-Reasoning Coevolution) is a dual-role RLVR framework with a shared policy consisting of two cooperative roles: an Observer that generates an evidence caption tailored to the question and a Solver that predicts the final answer based on this caption.

## Framework Design

PRCO employs role-specific reward signals: the Solver is optimized using verifiable outcome rewards on the final answer, while the Observer receives a utility reward derived from the Solver's downstream success. Existing RLVR approaches typically rely on outcome-driven optimization that updates both perception and reasoning using a shared reward based solely on the final answer, which blurs credit assignment and frequently fails to reliably enhance the accuracy of upstream visual evidence extraction.

## Experimental Results

Extensive experiments across eight challenging multimodal reasoning benchmarks demonstrate that PRCO yields consistent improvements across model scales by over 7 points on average accuracy compared to the base model. On the 3B and 7B backbones, PRCO achieves average accuracy improvements of 7.65 and 7.18 points, respectively, setting a new performance standard among open-source MLLMs.

## Ablation Studies

Ablation studies validate the importance of PRCO's core design choices, showing that removing the Solver's updates leads to substantial performance drop and removing the Observer's updates results in even larger performance degradation, demonstrating that the utility reward provides critical complementary benefits by strengthening the intermediate evidence signal.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e105fcef-2e5f-4e2c-a3ac-27cb2aa9ed82",
  "isSidechain": false,
  "promptId": "d4c50c87-a492-4ccd-ad5a-7cc9da96dc22",
  "type": "user",
  "uuid": "6825f690-328e-43bd-979d-f60fc1f85623",
  "toolUseResult": {
    "query": "PRCO \"perception reasoning coevolution\" observer solver multimodal reasoning experiments ablation benchmarks 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_013qZzNvGafRes5qcRHHGdNQ",
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
            "title": "GitHub - Dtc7w3PQ/PRCO: Official implementation of Seeing with You: Perception-Reasoning Co-evolution for Multimodal Reasoning. · GitHub",
            "url": "https://github.com/Dtc7w3PQ/PRCO"
          },
          {
            "title": "Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning | Takara TLDR",
            "url": "https://tldr.takara.ai/p/2603.28618"
          },
          {
            "title": "Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning",
            "url": "https://arxiv.org/pdf/2603.28618"
          },
          {
            "title": "Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning",
            "url": "https://chatpaper.com/paper/262369"
          },
          {
            "title": "Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning | Request PDF",
            "url": "https://www.researchgate.net/publication/403307388_Seeing_with_You_Perception-Reasoning_Coevolution_for_Multimodal_Reasoning"
          }
        ]
      },
      "I found relevant information about PRCO. Here's what the search reveals:\n\n## Overview\n\nPRCO (Perception-Reasoning Coevolution) is a dual-role RLVR framework with a shared policy consisting of two cooperative roles: an Observer that generates an evidence caption tailored to the question and a Solver that predicts the final answer based on this caption.\n\n## Framework Design\n\nPRCO employs role-specific reward signals: the Solver is optimized using verifiable outcome rewards on the final answer, while the Observer receives a utility reward derived from the Solver's downstream success. Existing RLVR approaches typically rely on outcome-driven optimization that updates both perception and reasoning using a shared reward based solely on the final answer, which blurs credit assignment and frequently fails to reliably enhance the accuracy of upstream visual evidence extraction.\n\n## Experimental Results\n\nExtensive experiments across eight challenging multimodal reasoning benchmarks demonstrate that PRCO yields consistent improvements across model scales by over 7 points on average accuracy compared to the base model. On the 3B and 7B backbones, PRCO achieves average accuracy improvements of 7.65 and 7.18 points, respectively, setting a new performance standard among open-source MLLMs.\n\n## Ablation Studies\n\nAblation studies validate the importance of PRCO's core design choices, showing that removing the Solver's updates leads to substantial performance drop and removing the Observer's updates results in even larger performance degradation, demonstrating that the utility reward provides critical complementary benefits by strengthening the intermediate evidence signal."
    ],
    "durationSeconds": 5.654104594999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e105fcef-2e5f-4e2c-a3ac-27cb2aa9ed82",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-27T08:45:37.296Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01P1s32vGsdFaXouh2h3iZoN`</summary>

```json
{
  "query": "MathVista MathVerse GeoQA state-of-the-art results 2026 Qwen3 VL multimodal math leaderboard"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6825f690-328e-43bd-979d-f60fc1f85623",
  "isSidechain": false,
  "requestId": "req_011CbSnEKFYHXRNVzqcXr7zD",
  "type": "assistant",
  "uuid": "2f34cdf5-f591-4ee2-bf0f-9054bfe4a5aa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N2QeCMGJfs31wgq6XD1Xdt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 858,
      "cache_read_input_tokens": 25551,
      "output_tokens": 89,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 858,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 89,
          "cache_read_input_tokens": 25551,
          "cache_creation_input_tokens": 858,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 858
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

_source line 33 · 2026-05-27T08:45:45.640Z_

<details><summary>↩ Tool result · `toolu_01P1s32vGsdFaXouh2h3iZoN`</summary>

```text
Web search results for query: "MathVista MathVerse GeoQA state-of-the-art results 2026 Qwen3 VL multimodal math leaderboard"

Links: [{"title":"[2511.21631] Qwen3-VL Technical Report","url":"https://arxiv.org/abs/2511.21631"},{"title":"qwen3-vl","url":"https://ollama.com/library/qwen3-vl"},{"title":"Qwen3-VL Technical Report","url":"https://www.researchgate.net/publication/398026379_Qwen3-VL_Technical_Report"},{"title":"qwen3-vl:32b-thinking","url":"https://ollama.com/library/qwen3-vl:32b-thinking"},{"title":"CapGeo: A Caption-Assisted Approach to Geometric Reasoning","url":"https://arxiv.org/html/2510.09302"},{"title":"M3-ACE: Rectifying Visual Perception in Multimodal Math Reasoning via Multi-Agentic Context Engineering","url":"https://arxiv.org/html/2603.08369"},{"title":"MathSE: Improving Multimodal Mathematical Reasoning via Self-Evolving Iterative Reflection and Reward-Guided Fine-Tuning","url":"https://arxiv.org/html/2511.06805"},{"title":"MathVerse: Visual Math Reasoning Benchmark","url":"https://www.emergentmind.com/topics/mathverse"},{"title":"When to Think and When to Look: Uncertainty-Guided Lookback","url":"https://arxiv.org/html/2511.15613v2"}]

Based on the search results, here's what I found about state-of-the-art results on multimodal math reasoning benchmarks involving Qwen3-VL and related models:

## Qwen3-VL Performance

Qwen3-VL demonstrates advanced multimodal reasoning across single-image, multi-image, and video tasks, with leading performance on comprehensive evaluations such as MMMU and visual-math benchmarks (e.g., MathVista and MathVision). The Qwen3-VL Thinking model achieves strong performance on reasoning benchmarks like MathVision, MMMU, and MathVista.

## Recent SOTA Results (2026)

The Qwen3.5 series achieves 85.7% on MathVista and 78.9% on MathVision, substantially surpassing human baselines of 60.3% and 68.82% respectively.

## Related Benchmark Performance

The search results also document performance across these three key benchmarks:

- On MathVista, MathVerse, and MathVision, various models show significant performance improvements with average score increases ranging from 8.04% to 15.91% through optimization approaches.

- On MathVista, caption-assisted reasoning enables Qwen2.5-VL-72B-Instruct to improve from 75.9% to 92.6%, closing the gap with SOTA closed model GPT-o3 (94.9%).

The results demonstrate ongoing advancement in multimodal mathematical reasoning, with vision-language models showing increasingly strong performance on geometry and visual math problem-solving benchmarks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2f34cdf5-f591-4ee2-bf0f-9054bfe4a5aa",
  "isSidechain": false,
  "promptId": "d4c50c87-a492-4ccd-ad5a-7cc9da96dc22",
  "type": "user",
  "uuid": "3388adc4-cc8e-40ac-8e5c-af22c182a9d4",
  "toolUseResult": {
    "query": "MathVista MathVerse GeoQA state-of-the-art results 2026 Qwen3 VL multimodal math leaderboard",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Ke6z8pH3Wz2stCR1ADsuRU",
        "content": [
          {
            "title": "[2511.21631] Qwen3-VL Technical Report",
            "url": "https://arxiv.org/abs/2511.21631"
          },
          {
            "title": "qwen3-vl",
            "url": "https://ollama.com/library/qwen3-vl"
          },
          {
            "title": "Qwen3-VL Technical Report",
            "url": "https://www.researchgate.net/publication/398026379_Qwen3-VL_Technical_Report"
          },
          {
            "title": "qwen3-vl:32b-thinking",
            "url": "https://ollama.com/library/qwen3-vl:32b-thinking"
          },
          {
            "title": "CapGeo: A Caption-Assisted Approach to Geometric Reasoning",
            "url": "https://arxiv.org/html/2510.09302"
          },
          {
            "title": "M3-ACE: Rectifying Visual Perception in Multimodal Math Reasoning via Multi-Agentic Context Engineering",
            "url": "https://arxiv.org/html/2603.08369"
          },
          {
            "title": "MathSE: Improving Multimodal Mathematical Reasoning via Self-Evolving Iterative Reflection and Reward-Guided Fine-Tuning",
            "url": "https://arxiv.org/html/2511.06805"
          },
          {
            "title": "MathVerse: Visual Math Reasoning Benchmark",
            "url": "https://www.emergentmind.com/topics/mathverse"
          },
          {
            "title": "When to Think and When to Look: Uncertainty-Guided Lookback",
            "url": "https://arxiv.org/html/2511.15613v2"
          }
        ]
      },
      "Based on the search results, here's what I found about state-of-the-art results on multimodal math reasoning benchmarks involving Qwen3-VL and related models:\n\n## Qwen3-VL Performance\n\nQwen3-VL demonstrates advanced multimodal reasoning across single-image, multi-image, and video tasks, with leading performance on comprehensive evaluations such as MMMU and visual-math benchmarks (e.g., MathVista and MathVision). The Qwen3-VL Thinking model achieves strong performance on reasoning benchmarks like MathVision, MMMU, and MathVista.\n\n## Recent SOTA Results (2026)\n\nThe Qwen3.5 series achieves 85.7% on MathVista and 78.9% on MathVision, substantially surpassing human baselines of 60.3% and 68.82% respectively.\n\n## Related Benchmark Performance\n\nThe search results also document performance across these three key benchmarks:\n\n- On MathVista, MathVerse, and MathVision, various models show significant performance improvements with average score increases ranging from 8.04% to 15.91% through optimization approaches.\n\n- On MathVista, caption-assisted reasoning enables Qwen2.5-VL-72B-Instruct to improve from 75.9% to 92.6%, closing the gap with SOTA closed model GPT-o3 (94.9%).\n\nThe results demonstrate ongoing advancement in multimodal mathematical reasoning, with vision-language models showing increasingly strong performance on geometry and visual math problem-solving benchmarks."
    ],
    "durationSeconds": 8.340087563000008,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "2f34cdf5-f591-4ee2-bf0f-9054bfe4a5aa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164",
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
  "lastPrompt": "# Axiom-Grounded Self-Verified Perception for Visual Math Reasoning  ## Core Problem and Thesis  Current multimodal math reasoning systems verify perceived visual facts independently—checking each cla…",
  "leafUuid": "3388adc4-cc8e-40ac-8e5c-af22c182a9d4",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Axiom-grounded self-verified perception for math reasoning",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164"
}
```

---

### Tool call

_source line 36 · 2026-05-27T08:45:48.814Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JmsV16mDqD5ejnkybtX5Zd`</summary>

```json
{
  "query": "FormalGeo FGeo-DRL deductive reasoning geometric problems reinforcement learning formalgeo7k experiments 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3388adc4-cc8e-40ac-8e5c-af22c182a9d4",
  "isSidechain": false,
  "requestId": "req_011CbSnFD1XgtSy3GdtnVrAo",
  "type": "assistant",
  "uuid": "4fcbe52d-e5d5-4aea-acd4-b3d8ef9a1f10",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WWUtzRBd3sR8tWCEJQ21xE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 908,
      "cache_read_input_tokens": 26409,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 908,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 78,
          "cache_read_input_tokens": 26409,
          "cache_creation_input_tokens": 908,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 908
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

_source line 37 · 2026-05-27T08:45:54.135Z_

<details><summary>↩ Tool result · `toolu_01JmsV16mDqD5ejnkybtX5Zd`</summary>

```text
Web search results for query: "FormalGeo FGeo-DRL deductive reasoning geometric problems reinforcement learning formalgeo7k experiments 2024"

Links: [{"title":"[2402.09051] FGeo-DRL: Deductive Reasoning for Geometric Problems through Deep Reinforcement Learning","url":"https://arxiv.org/abs/2402.09051"},{"title":"(PDF) FGeo-DRL: Deductive Reasoning for Geometric Problems through Deep Reinforcement Learning","url":"https://www.researchgate.net/publication/379613284_FGeo-DRL_Deductive_Reasoning_for_Geometric_Problems_through_Deep_Reinforcement_Learning"},{"title":"FGeo-DRL: Deductive Reasoning for Geometric Problems through Deep Reinforcement Learning","url":"https://www.mdpi.com/2073-8994/16/4/437"},{"title":"FGeo-DRL: Deductive Reasoning for Geometric Problems through Deep   Reinforcement Learning","url":"https://arxiv.org/pdf/2402.09051"},{"title":"FGeo-DRL:Deductive Reasoning for Geometric Problems through Deep Reinforcement Learning","url":"https://arxiv.org/html/2402.09051v1"},{"title":"FormalGeo: Formal representation and solving for Euclidean plane geometry problems","url":"https://formalgeo.github.io/"},{"title":"FGeo-HyperGNet: Geometric Problem Solving Integrating FormalGeo Symbolic System and Hypergraph Neural Network","url":"https://arxiv.org/html/2402.11461"},{"title":"Papers with Code - FGeo-DRL: Deductive Reasoning for Geometric Problems through Deep Reinforcement Learning","url":"https://paperswithcode.com/paper/fgeo-drl-deductive-reasoning-for-geometric"},{"title":"AutoGPS: Automated Geometry Problem Solving","url":"https://www.emergentmind.com/papers/2505.23381"}]

Based on the search results, here's what I found about FGeo-DRL and the related research:

## Overview

FGeo-DRL is a neural-symbolic system built to automatically perform human-like geometric deductive reasoning. The paper was published in February 2024, and represents part of a broader research initiative on formal geometry problem solving.

## System Architecture

The FGeo-DRL system consists of two main components:

**Neural Component:** The neural part is an AI agent based on reinforcement learning, capable of autonomously learning problem-solving methods from the feedback of a formalized environment, without the need for human supervision. It leverages a pre-trained natural language model to establish a policy network for theorem selection and employ Monte Carlo Tree Search for heuristic exploration.

**Symbolic Component:** The symbolic part is a reinforcement learning environment based on geometry formalization theory and FormalGeo, which models GPS as a Markov Decision Process. In this formal symbolic system, the known conditions and objectives of the problem form the state space, while the set of theorems forms the action space.

## Experimental Results

Experiments conducted on the formalgeo7k dataset have achieved a problem-solving success rate of 86.40%. Leveraging FGeoDRL, they achieved readable and verifiable automated solutions to geometric problems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4fcbe52d-e5d5-4aea-acd4-b3d8ef9a1f10",
  "isSidechain": false,
  "promptId": "d4c50c87-a492-4ccd-ad5a-7cc9da96dc22",
  "type": "user",
  "uuid": "fe7b4336-fa56-4563-b279-5800fe339f96",
  "toolUseResult": {
    "query": "FormalGeo FGeo-DRL deductive reasoning geometric problems reinforcement learning formalgeo7k experiments 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_015WFACdbGzDXdR1DAv7bGtd",
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
            "title": "FGeo-DRL: Deductive Reasoning for Geometric Problems through Deep   Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2402.09051"
          },
          {
            "title": "FGeo-DRL:Deductive Reasoning for Geometric Problems through Deep Reinforcement Learning",
            "url": "https://arxiv.org/html/2402.09051v1"
          },
          {
            "title": "FormalGeo: Formal representation and solving for Euclidean plane geometry problems",
            "url": "https://formalgeo.github.io/"
          },
          {
            "title": "FGeo-HyperGNet: Geometric Problem Solving Integrating FormalGeo Symbolic System and Hypergraph Neural Network",
            "url": "https://arxiv.org/html/2402.11461"
          },
          {
            "title": "Papers with Code - FGeo-DRL: Deductive Reasoning for Geometric Problems through Deep Reinforcement Learning",
            "url": "https://paperswithcode.com/paper/fgeo-drl-deductive-reasoning-for-geometric"
          },
          {
            "title": "AutoGPS: Automated Geometry Problem Solving",
            "url": "https://www.emergentmind.com/papers/2505.23381"
          }
        ]
      },
      "Based on the search results, here's what I found about FGeo-DRL and the related research:\n\n## Overview\n\nFGeo-DRL is a neural-symbolic system built to automatically perform human-like geometric deductive reasoning. The paper was published in February 2024, and represents part of a broader research initiative on formal geometry problem solving.\n\n## System Architecture\n\nThe FGeo-DRL system consists of two main components:\n\n**Neural Component:** The neural part is an AI agent based on reinforcement learning, capable of autonomously learning problem-solving methods from the feedback of a formalized environment, without the need for human supervision. It leverages a pre-trained natural language model to establish a policy network for theorem selection and employ Monte Carlo Tree Search for heuristic exploration.\n\n**Symbolic Component:** The symbolic part is a reinforcement learning environment based on geometry formalization theory and FormalGeo, which models GPS as a Markov Decision Process. In this formal symbolic system, the known conditions and objectives of the problem form the state space, while the set of theorems forms the action space.\n\n## Experimental Results\n\nExperiments conducted on the formalgeo7k dataset have achieved a problem-solving success rate of 86.40%. Leveraging FGeoDRL, they achieved readable and verifiable automated solutions to geometric problems."
    ],
    "durationSeconds": 5.31552347700001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "4fcbe52d-e5d5-4aea-acd4-b3d8ef9a1f10",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-27T08:45:57.797Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01L9cDKtmvLX1bnLAbJE3dKH`</summary>

```json
{
  "query": "axiom checker geometric constraint verification computational overhead implementation feasibility VLM training 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe7b4336-fa56-4563-b279-5800fe339f96",
  "isSidechain": false,
  "requestId": "req_011CbSnFqNJdJRRHfBN9yzvw",
  "type": "assistant",
  "uuid": "5675c74d-c209-4add-9bff-8be12f77a8ff",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D76BQFpdyK8Kban1aHk2sq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 887,
      "cache_read_input_tokens": 27317,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 887,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 27317,
          "cache_creation_input_tokens": 887,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 887
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

_source line 39 · 2026-05-27T08:46:06.475Z_

<details><summary>↩ Tool result · `toolu_01L9cDKtmvLX1bnLAbJE3dKH`</summary>

```text
Web search results for query: "axiom checker geometric constraint verification computational overhead implementation feasibility VLM training 2025 2026"

Links: [{"title":"Vision-Language Model Training - 2026 Embedded Vision Summit","url":"https://embeddedvisionsummit.com/vlm-training/"},{"title":"GitHub - InternRobotics/G2VLM: [CVPR 2026] G2VLM: Geometry Grounded Vision Language Model with Unified 3D Reconstruction and Spatial Reasoning · GitHub","url":"https://github.com/InternRobotics/G2VLM"},{"title":"Geometrically-Constrained Agent for Spatial Reasoning","url":"https://arxiv.org/pdf/2511.22659"},{"title":"VLM: How Vision-Language Models Work (2026 Guide) | Label Your Data","url":"https://labelyourdata.com/articles/machine-learning/vision-language-models"},{"title":"Predicting When to Trust Vision-Language Models for Spatial Reasoning","url":"https://arxiv.org/pdf/2601.11644"}]

Based on the web search results, here's what I found relevant to your query about axiom checker geometric constraint verification and VLM training in 2025-2026:

## Geometric Constraint Verification for VLMs

Recent work shows that tool-integrated methods constrain final computation but leave the VLM's planning process unconstrained, resulting in geometrically flawed plans—motivating approaches like Geometrically-Constrained Agent (GCA), a training-free paradigm that introduces formal task constraints.

One approach proposes vision-based confidence estimation that validates VLM predictions through independent geometric verification, using object detection to verify spatial relationships and extract confidence features.

## Computational Overhead and Implementation Feasibility

Full pretraining for VLMs requires prohibitive compute budgets, so most teams fine-tune pretrained VLMs instead, adapting existing models to their domain at a fraction of the cost. LoRA (Low-Rank Adaptation) cuts training costs by freezing pretrained weights and adding small trainable matrices to attention layers, enabling 70B model fine-tuning on single A100 GPUs.

## 2025-2026 Developments

Recent work like G2VLM (accepted to CVPR 2026) presents a unified model integrating geometric perception for 3D reconstruction and semantic perception for multimodal understanding and spatial reasoning tasks.

The search results suggest a focus on balancing geometric constraints with practical computational feasibility in VLM training during this period.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5675c74d-c209-4add-9bff-8be12f77a8ff",
  "isSidechain": false,
  "promptId": "d4c50c87-a492-4ccd-ad5a-7cc9da96dc22",
  "type": "user",
  "uuid": "474e1a43-1e4e-478e-b436-43c4a87c9dee",
  "toolUseResult": {
    "query": "axiom checker geometric constraint verification computational overhead implementation feasibility VLM training 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01St79C4tD3HPjDHgCZFKQ4u",
        "content": [
          {
            "title": "Vision-Language Model Training - 2026 Embedded Vision Summit",
            "url": "https://embeddedvisionsummit.com/vlm-training/"
          },
          {
            "title": "GitHub - InternRobotics/G2VLM: [CVPR 2026] G2VLM: Geometry Grounded Vision Language Model with Unified 3D Reconstruction and Spatial Reasoning · GitHub",
            "url": "https://github.com/InternRobotics/G2VLM"
          },
          {
            "title": "Geometrically-Constrained Agent for Spatial Reasoning",
            "url": "https://arxiv.org/pdf/2511.22659"
          },
          {
            "title": "VLM: How Vision-Language Models Work (2026 Guide) | Label Your Data",
            "url": "https://labelyourdata.com/articles/machine-learning/vision-language-models"
          },
          {
            "title": "Predicting When to Trust Vision-Language Models for Spatial Reasoning",
            "url": "https://arxiv.org/pdf/2601.11644"
          }
        ]
      },
      "Based on the web search results, here's what I found relevant to your query about axiom checker geometric constraint verification and VLM training in 2025-2026:\n\n## Geometric Constraint Verification for VLMs\n\nRecent work shows that tool-integrated methods constrain final computation but leave the VLM's planning process unconstrained, resulting in geometrically flawed plans—motivating approaches like Geometrically-Constrained Agent (GCA), a training-free paradigm that introduces formal task constraints.\n\nOne approach proposes vision-based confidence estimation that validates VLM predictions through independent geometric verification, using object detection to verify spatial relationships and extract confidence features.\n\n## Computational Overhead and Implementation Feasibility\n\nFull pretraining for VLMs requires prohibitive compute budgets, so most teams fine-tune pretrained VLMs instead, adapting existing models to their domain at a fraction of the cost. LoRA (Low-Rank Adaptation) cuts training costs by freezing pretrained weights and adding small trainable matrices to attention layers, enabling 70B model fine-tuning on single A100 GPUs.\n\n## 2025-2026 Developments\n\nRecent work like G2VLM (accepted to CVPR 2026) presents a unified model integrating geometric perception for 3D reconstruction and semantic perception for multimodal understanding and spatial reasoning tasks.\n\nThe search results suggest a focus on balancing geometric constraints with practical computational feasibility in VLM training during this period."
    ],
    "durationSeconds": 8.673731975999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "5675c74d-c209-4add-9bff-8be12f77a8ff",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-27T08:46:09.169Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014mTtA7QTJeyQQA9m2xGYds`</summary>

```json
{
  "query": "V-Zero zero-shot multimodal reasoning cross-modal self-play questioner solver experiments 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "474e1a43-1e4e-478e-b436-43c4a87c9dee",
  "isSidechain": false,
  "requestId": "req_011CbSnGk4qrmPuLhT1rvUhN",
  "type": "assistant",
  "uuid": "661dfc23-881c-4817-a50d-b9990f4af153",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CsivuxLGbEF2ZJSG8VtegR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 701,
      "cache_read_input_tokens": 28204,
      "output_tokens": 74,
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
          "output_tokens": 74,
          "cache_read_input_tokens": 28204,
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

_source line 41 · 2026-05-27T08:46:18.188Z_

<details><summary>↩ Tool result · `toolu_014mTtA7QTJeyQQA9m2xGYds`</summary>

```text
Web search results for query: "V-Zero zero-shot multimodal reasoning cross-modal self-play questioner solver experiments 2026"

Links: [{"title":"V-Zero: Self-Improving Multimodal Reasoning with Zero Annotation","url":"https://arxiv.org/pdf/2601.10094"},{"title":"[2601.10094] V-Zero: Self-Improving Multimodal Reasoning with Zero Annotation","url":"https://arxiv.org/abs/2601.10094"},{"title":"[Literature Review] V-Zero: Self-Improving Multimodal Reasoning with Zero Annotation","url":"https://www.themoonlight.io/en/review/v-zero-self-improving-multimodal-reasoning-with-zero-annotation"},{"title":"Jingyuan Hu's research works","url":"https://www.researchgate.net/scientific-contributions/Jingyuan-Hu-2337177897"},{"title":"Han Wang","url":"https://www.catalyzex.com/author/Han%20Wang"},{"title":"MM-Zero: Self-Evolving Multi-Model Vision Language Models From Zero Data","url":"https://arxiv.org/pdf/2603.09206"},{"title":"Improving Zero-shot Visual Question Answering via Large Language Models   with Reasoning Question Prompts","url":"https://arxiv.org/pdf/2311.09050"},{"title":"CogGuide: Human-Like Guidance for Zero-Shot Omni-Modal Reasoning","url":"https://arxiv.org/pdf/2509.06641"}]

Based on the web search results, I found comprehensive information about V-Zero:

## V-Zero: Self-Improving Multimodal Reasoning with Zero Annotation

V-Zero is a general post-training framework that facilitates self-improvement using exclusively unlabeled images.

### Core Framework

V-Zero establishes a co-evolutionary loop by instantiating two distinct roles: a Questioner and a Solver. The Questioner learns to synthesize high-quality, challenging questions by leveraging a dual-track reasoning reward that contrasts intuitive guesses with reasoned results. The Solver is optimized using pseudo-labels derived from majority voting over its own sampled responses, with both roles trained iteratively via Group Relative Policy Optimization (GRPO).

### Experimental Results

The Questioner's format validity improved from 64.9% (Base) to 99.8% (Iter 2), while question difficulty increased from an average score of 0.52 (Base) to 0.60 (Iter 2).

### Key Features

By establishing a dynamic co-evolutionary loop and leveraging a novel dual-track reasoning reward, V-Zero effectively generates a curriculum of increasing difficulty, leading to significant and generalized performance gains in multimodal reasoning.

The research paper was published in January 2026 on arXiv (paper 2601.10094).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "661dfc23-881c-4817-a50d-b9990f4af153",
  "isSidechain": false,
  "promptId": "d4c50c87-a492-4ccd-ad5a-7cc9da96dc22",
  "type": "user",
  "uuid": "2f308e7f-d71b-4ee3-bf78-f12f78e07008",
  "toolUseResult": {
    "query": "V-Zero zero-shot multimodal reasoning cross-modal self-play questioner solver experiments 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PobAbnA6MkoK3uHmswmF8Q",
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
            "title": "[Literature Review] V-Zero: Self-Improving Multimodal Reasoning with Zero Annotation",
            "url": "https://www.themoonlight.io/en/review/v-zero-self-improving-multimodal-reasoning-with-zero-annotation"
          },
          {
            "title": "Jingyuan Hu's research works",
            "url": "https://www.researchgate.net/scientific-contributions/Jingyuan-Hu-2337177897"
          },
          {
            "title": "Han Wang",
            "url": "https://www.catalyzex.com/author/Han%20Wang"
          },
          {
            "title": "MM-Zero: Self-Evolving Multi-Model Vision Language Models From Zero Data",
            "url": "https://arxiv.org/pdf/2603.09206"
          },
          {
            "title": "Improving Zero-shot Visual Question Answering via Large Language Models   with Reasoning Question Prompts",
            "url": "https://arxiv.org/pdf/2311.09050"
          },
          {
            "title": "CogGuide: Human-Like Guidance for Zero-Shot Omni-Modal Reasoning",
            "url": "https://arxiv.org/pdf/2509.06641"
          }
        ]
      },
      "Based on the web search results, I found comprehensive information about V-Zero:\n\n## V-Zero: Self-Improving Multimodal Reasoning with Zero Annotation\n\nV-Zero is a general post-training framework that facilitates self-improvement using exclusively unlabeled images.\n\n### Core Framework\n\nV-Zero establishes a co-evolutionary loop by instantiating two distinct roles: a Questioner and a Solver. The Questioner learns to synthesize high-quality, challenging questions by leveraging a dual-track reasoning reward that contrasts intuitive guesses with reasoned results. The Solver is optimized using pseudo-labels derived from majority voting over its own sampled responses, with both roles trained iteratively via Group Relative Policy Optimization (GRPO).\n\n### Experimental Results\n\nThe Questioner's format validity improved from 64.9% (Base) to 99.8% (Iter 2), while question difficulty increased from an average score of 0.52 (Base) to 0.60 (Iter 2).\n\n### Key Features\n\nBy establishing a dynamic co-evolutionary loop and leveraging a novel dual-track reasoning reward, V-Zero effectively generates a curriculum of increasing difficulty, leading to significant and generalized performance gains in multimodal reasoning.\n\nThe research paper was published in January 2026 on arXiv (paper 2601.10094)."
    ],
    "durationSeconds": 9.013790267000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "661dfc23-881c-4817-a50d-b9990f4af153",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-27T08:46:21.258Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UGN8YNc7KozmWckkuP29XX`</summary>

```json
{
  "query": "SymHPR \"hierarchical process reward\" symbolic vision learner diagram parsing structural consistency 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f308e7f-d71b-4ee3-bf78-f12f78e07008",
  "isSidechain": false,
  "requestId": "req_011CbSnHcC7882e9ezHoAz4u",
  "type": "assistant",
  "uuid": "eee4d03f-5f34-4327-84a7-d90430b84647",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K3REhx6DkMiqQjnTHPbBvJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 786,
      "cache_read_input_tokens": 28905,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 786,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 28905,
          "cache_creation_input_tokens": 786,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 786
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

_source line 43 · 2026-05-27T08:46:29.043Z_

<details><summary>↩ Tool result · `toolu_01UGN8YNc7KozmWckkuP29XX`</summary>

```text
Web search results for query: "SymHPR "hierarchical process reward" symbolic vision learner diagram parsing structural consistency 2025"

Links: [{"title":"Hierarchical Process Reward Models are Symbolic Vision Learners","url":"https://arxiv.org/html/2512.03126v1"},{"title":"[2512.03126] Hierarchical Process Reward Models are Symbolic Vision Learners","url":"https://arxiv.org/abs/2512.03126"},{"title":"Hierarchical Process Reward Models are Symbolic Vision Learners","url":"https://arxiv.org/pdf/2512.03126"},{"title":"Interpretable Imitation Learning with Symbolic Rewards | ACM Transactions on Intelligent Systems and Technology","url":"https://dl.acm.org/doi/10.1145/3627822"},{"title":"A Hierarchical Bayesian Approach to Inverse Reinforcement Learning with   Symbolic Reward Machines","url":"https://arxiv.org/pdf/2204.09772"}]

Based on the search results, I found comprehensive information about SymHPR:

## SymHPR: Hierarchical Process Reward Models for Symbolic Vision Learning

SymHPR is a research work from Adelaide AIML, Ohio State University, NetMind.ai, University of Oxford, and Data61/CSIRO that focuses on symbolic computer vision representing diagrams through explicit logical rules and structured representations.

### Key Innovations

SymHPR introduces three key innovations: cost-free training data using a synthetic logic-form engine that constructs structured parsing paths paired with rendered diagrams; rule-based rewards computed via verifiable metrics like F1 scores and L2 distances; and hierarchical dependency modeling that enforces step-level constraints such as point-on-line, line-on-shape, and shape-on-relation.

### Core Architecture

The approach proposes a novel self-supervised symbolic auto-encoder that encodes diagrams into structured primitives and their interrelationships, with SymHPR applying hierarchical step-level parsing rewards to enforce point-on-line, line-on-shape, and shape-on-relation consistency. After hierarchical reward training, it instantiates a symbolic auto-encoder with an executable rendering engine that reconstructs diagrams from structured primitives.

### Performance

Evaluations demonstrate the effectiveness of the approach: achieving a 98.2% reduction in MSE for geometric diagram reconstruction, surpassing GPT-4O by 0.6% with a 7B model on chart reconstruction, and improving by +13% on the MathGlance perception task.

The paper was published in December 2025 on arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eee4d03f-5f34-4327-84a7-d90430b84647",
  "isSidechain": false,
  "promptId": "d4c50c87-a492-4ccd-ad5a-7cc9da96dc22",
  "type": "user",
  "uuid": "cd6c7781-4761-4120-9b33-2028efe11f4f",
  "toolUseResult": {
    "query": "SymHPR \"hierarchical process reward\" symbolic vision learner diagram parsing structural consistency 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CqJRoaqfnj1SEPexCTES94",
        "content": [
          {
            "title": "Hierarchical Process Reward Models are Symbolic Vision Learners",
            "url": "https://arxiv.org/html/2512.03126v1"
          },
          {
            "title": "[2512.03126] Hierarchical Process Reward Models are Symbolic Vision Learners",
            "url": "https://arxiv.org/abs/2512.03126"
          },
          {
            "title": "Hierarchical Process Reward Models are Symbolic Vision Learners",
            "url": "https://arxiv.org/pdf/2512.03126"
          },
          {
            "title": "Interpretable Imitation Learning with Symbolic Rewards | ACM Transactions on Intelligent Systems and Technology",
            "url": "https://dl.acm.org/doi/10.1145/3627822"
          },
          {
            "title": "A Hierarchical Bayesian Approach to Inverse Reinforcement Learning with   Symbolic Reward Machines",
            "url": "https://arxiv.org/pdf/2204.09772"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about SymHPR:\n\n## SymHPR: Hierarchical Process Reward Models for Symbolic Vision Learning\n\nSymHPR is a research work from Adelaide AIML, Ohio State University, NetMind.ai, University of Oxford, and Data61/CSIRO that focuses on symbolic computer vision representing diagrams through explicit logical rules and structured representations.\n\n### Key Innovations\n\nSymHPR introduces three key innovations: cost-free training data using a synthetic logic-form engine that constructs structured parsing paths paired with rendered diagrams; rule-based rewards computed via verifiable metrics like F1 scores and L2 distances; and hierarchical dependency modeling that enforces step-level constraints such as point-on-line, line-on-shape, and shape-on-relation.\n\n### Core Architecture\n\nThe approach proposes a novel self-supervised symbolic auto-encoder that encodes diagrams into structured primitives and their interrelationships, with SymHPR applying hierarchical step-level parsing rewards to enforce point-on-line, line-on-shape, and shape-on-relation consistency. After hierarchical reward training, it instantiates a symbolic auto-encoder with an executable rendering engine that reconstructs diagrams from structured primitives.\n\n### Performance\n\nEvaluations demonstrate the effectiveness of the approach: achieving a 98.2% reduction in MSE for geometric diagram reconstruction, surpassing GPT-4O by 0.6% with a 7B model on chart reconstruction, and improving by +13% on the MathGlance perception task.\n\nThe paper was published in December 2025 on arXiv."
    ],
    "durationSeconds": 7.7815465449999905,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "eee4d03f-5f34-4327-84a7-d90430b84647",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-27T08:46:35.507Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NqChjzAqu93scxnEqr7PNE`</summary>

```json
{
  "query": "\"Milestones over Outcome\" sub-goal verifiable reward geometric reasoning experiments results 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd6c7781-4761-4120-9b33-2028efe11f4f",
  "isSidechain": false,
  "requestId": "req_011CbSnJQioy3pPJb7rFo7jT",
  "type": "assistant",
  "uuid": "aa3c6e27-c01e-4ef5-9e82-6533aa41b7d1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015HJGqBwGG6E88vyCLJDc8V",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 720,
      "cache_read_input_tokens": 29691,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 720,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 29691,
          "cache_creation_input_tokens": 720,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 720
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

_source line 45 · 2026-05-27T08:46:45.297Z_

<details><summary>↩ Tool result · `toolu_01NqChjzAqu93scxnEqr7PNE`</summary>

```text
Web search results for query: ""Milestones over Outcome" sub-goal verifiable reward geometric reasoning experiments results 2025"

Links: [{"title":"Milestones over Outcome: Unlocking Geometric Reasoning with Sub-Goal Verifiable Reward","url":"https://arxiv.org/html/2601.05073v1"},{"title":"Milestones over Outcome: Unlocking Geometric Reasoning with Sub-Goal Verifiable Reward | alphaXiv","url":"https://www.alphaxiv.org/es/overview/2601.05073v1"},{"title":"Paper page - Milestones over Outcome: Unlocking Geometric Reasoning with Sub-Goal Verifiable Reward","url":"https://huggingface.co/papers/2601.05073"},{"title":"Milestones over Outcome: Unlocking Geometric Reasoning with Sub-Goal Verifiable Reward - ADS","url":"https://ui.adsabs.harvard.edu/abs/2026arXiv260105073C/abstract"},{"title":"[2601.05073] Milestones over Outcome: Unlocking Geometric Reasoning with Sub-Goal Verifiable Reward","url":"https://arxiv.org/abs/2601.05073"},{"title":"GitHub - FrontierX-Lab/SGVR","url":"https://github.com/FrontierX-Lab/SGVR"},{"title":"CUHKSZ & SJTU January 9, 2026 Milestones over Outcome: Unlocking Geometric","url":"https://arxiv.org/pdf/2601.05073"}]

Based on the search results, here's what I found about the "Milestones over Outcome: Unlocking Geometric Reasoning with Sub-Goal Verifiable Reward" research:

## Overview

The research addresses how Multimodal Large Language Models (MLLMs) struggle with complex geometric reasoning, largely because "black box" outcome-based supervision fails to distinguish between lucky guesses and rigorous deduction.

## Key Contributions

The researchers constructed GeoGoal, a benchmark synthesized via a rigorous formal verification data engine, which converts abstract proofs into verifiable numeric subgoals. They proposed the Sub-Goal Verifiable Reward (SGVR) framework, which replaces sparse signals with dense rewards based on the Skeleton Rate.

## Experimental Results

The results show that the proposed SGVR improves both final-answer performance and intermediate reasoning quality, with gains transferring beyond geometry by achieving average improvements of +9.7% on geometric reasoning, +8.0% on general mathematics, and +2.8% on general reasoning tasks.

## Training Method

The researchers used Group Relative Policy Optimization (GRPO) DeepSeek-AI (2025) to maximize the Skeleton Rate, the ratio of successfully verified sub-goals.

The paper was published on January 8, 2026, and represents a significant advancement in enabling more rigorous reasoning processes in multimodal AI models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa3c6e27-c01e-4ef5-9e82-6533aa41b7d1",
  "isSidechain": false,
  "promptId": "d4c50c87-a492-4ccd-ad5a-7cc9da96dc22",
  "type": "user",
  "uuid": "89de1476-da41-4b56-a72b-114e7b0abda4",
  "toolUseResult": {
    "query": "\"Milestones over Outcome\" sub-goal verifiable reward geometric reasoning experiments results 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Q8jQyLuU4taNNDtrjKqy98",
        "content": [
          {
            "title": "Milestones over Outcome: Unlocking Geometric Reasoning with Sub-Goal Verifiable Reward",
            "url": "https://arxiv.org/html/2601.05073v1"
          },
          {
            "title": "Milestones over Outcome: Unlocking Geometric Reasoning with Sub-Goal Verifiable Reward | alphaXiv",
            "url": "https://www.alphaxiv.org/es/overview/2601.05073v1"
          },
          {
            "title": "Paper page - Milestones over Outcome: Unlocking Geometric Reasoning with Sub-Goal Verifiable Reward",
            "url": "https://huggingface.co/papers/2601.05073"
          },
          {
            "title": "Milestones over Outcome: Unlocking Geometric Reasoning with Sub-Goal Verifiable Reward - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2026arXiv260105073C/abstract"
          },
          {
            "title": "[2601.05073] Milestones over Outcome: Unlocking Geometric Reasoning with Sub-Goal Verifiable Reward",
            "url": "https://arxiv.org/abs/2601.05073"
          },
          {
            "title": "GitHub - FrontierX-Lab/SGVR",
            "url": "https://github.com/FrontierX-Lab/SGVR"
          },
          {
            "title": "CUHKSZ & SJTU January 9, 2026 Milestones over Outcome: Unlocking Geometric",
            "url": "https://arxiv.org/pdf/2601.05073"
          }
        ]
      },
      "Based on the search results, here's what I found about the \"Milestones over Outcome: Unlocking Geometric Reasoning with Sub-Goal Verifiable Reward\" research:\n\n## Overview\n\nThe research addresses how Multimodal Large Language Models (MLLMs) struggle with complex geometric reasoning, largely because \"black box\" outcome-based supervision fails to distinguish between lucky guesses and rigorous deduction.\n\n## Key Contributions\n\nThe researchers constructed GeoGoal, a benchmark synthesized via a rigorous formal verification data engine, which converts abstract proofs into verifiable numeric subgoals. They proposed the Sub-Goal Verifiable Reward (SGVR) framework, which replaces sparse signals with dense rewards based on the Skeleton Rate.\n\n## Experimental Results\n\nThe results show that the proposed SGVR improves both final-answer performance and intermediate reasoning quality, with gains transferring beyond geometry by achieving average improvements of +9.7% on geometric reasoning, +8.0% on general mathematics, and +2.8% on general reasoning tasks.\n\n## Training Method\n\nThe researchers used Group Relative Policy Optimization (GRPO) DeepSeek-AI (2025) to maximize the Skeleton Rate, the ratio of successfully verified sub-goals.\n\nThe paper was published on January 8, 2026, and represents a significant advancement in enabling more rigorous reasoning processes in multimodal AI models."
    ],
    "durationSeconds": 9.783168468999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "aa3c6e27-c01e-4ef5-9e82-6533aa41b7d1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164",
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
  "leafUuid": "89de1476-da41-4b56-a72b-114e7b0abda4",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "ai-title",
  "aiTitle": "Axiom-grounded self-verified perception for math reasoning",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164"
}
```

---

### Tool call

_source line 48 · 2026-05-27T08:46:49.005Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DVmakWXn9kTPjXLQbVdRXB`</summary>

```json
{
  "query": "M3-ACE multi-agentic context engineering rectify visual perception multimodal math experiments 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "89de1476-da41-4b56-a72b-114e7b0abda4",
  "isSidechain": false,
  "requestId": "req_011CbSnKc8gq85wCJJ3Ak3XJ",
  "type": "assistant",
  "uuid": "b62aab2d-882f-48df-ab30-c1a0f91cc4d7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014JHfc1PqMK7bJdVJiswAPP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 804,
      "cache_read_input_tokens": 30411,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 804,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 30411,
          "cache_creation_input_tokens": 804,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 804
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

_source line 49 · 2026-05-27T08:46:55.007Z_

<details><summary>↩ Tool result · `toolu_01DVmakWXn9kTPjXLQbVdRXB`</summary>

```text
Web search results for query: "M3-ACE multi-agentic context engineering rectify visual perception multimodal math experiments 2026"

Links: [{"title":"[2603.08369] M$^3$-ACE: Rectifying Visual Perception in Multimodal Math Reasoning via Multi-Agentic Context Engineering","url":"https://arxiv.org/abs/2603.08369"},{"title":"M3-ACE: Rectifying Visual Perception in Multimodal Math Reasoning via Multi-Agentic Context Engineering","url":"https://arxiv.org/html/2603.08369"},{"title":"M3-ACE: Rectifying Visual Perception in Multimodal Math ...","url":"https://arxiv.org/pdf/2603.08369"},{"title":"M3-Agent: Multimodal Cognitive Framework","url":"https://www.emergentmind.com/topics/m3-agent"},{"title":"The Role of Visual Modality in Multimodal Mathematical Reasoning: Challenges and Insights","url":"https://arxiv.org/pdf/2503.04167"},{"title":"Mitigating Visual Context Degradation in Large Multimodal Models: A Training-Free Decoupled Agentic Framework","url":"https://arxiv.org/html/2509.23322v2"}]

Based on the search results, I found information about M3-ACE:

M3-ACE is a multi-agentic context engineering framework designed to rectify visual perception in multimodal math reasoning. 

The research addresses a key problem in multimodal large language models: their performance is often limited by inaccurate visual perception, with most failures originating from incorrect or incomplete visual evidence extraction rather than deficiencies in reasoning capability.

The approach decouples perception and reasoning by dynamically maintaining a shared context centered on visual evidence lists. More specifically, the approach introduces structured multi-agent interactions over a shared visual evidence context, enabling cross-validation through consistent, complementary, and conflicting evidence categorization, disagreement resolution via lightweight summary and refinement tools, and iterative refinement of perceptual facts until convergence.

Extensive experiments demonstrate that M3-ACE substantially improves visual mathematical reasoning performance across multiple benchmarks. The paper was published in March 2026 on arXiv (2603.08369).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b62aab2d-882f-48df-ab30-c1a0f91cc4d7",
  "isSidechain": false,
  "promptId": "d4c50c87-a492-4ccd-ad5a-7cc9da96dc22",
  "type": "user",
  "uuid": "0a439a03-2b24-44b7-8da0-83b1b20c5d55",
  "toolUseResult": {
    "query": "M3-ACE multi-agentic context engineering rectify visual perception multimodal math experiments 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Ujh9GZZRit2EvYDzwUKQfX",
        "content": [
          {
            "title": "[2603.08369] M$^3$-ACE: Rectifying Visual Perception in Multimodal Math Reasoning via Multi-Agentic Context Engineering",
            "url": "https://arxiv.org/abs/2603.08369"
          },
          {
            "title": "M3-ACE: Rectifying Visual Perception in Multimodal Math Reasoning via Multi-Agentic Context Engineering",
            "url": "https://arxiv.org/html/2603.08369"
          },
          {
            "title": "M3-ACE: Rectifying Visual Perception in Multimodal Math ...",
            "url": "https://arxiv.org/pdf/2603.08369"
          },
          {
            "title": "M3-Agent: Multimodal Cognitive Framework",
            "url": "https://www.emergentmind.com/topics/m3-agent"
          },
          {
            "title": "The Role of Visual Modality in Multimodal Mathematical Reasoning: Challenges and Insights",
            "url": "https://arxiv.org/pdf/2503.04167"
          },
          {
            "title": "Mitigating Visual Context Degradation in Large Multimodal Models: A Training-Free Decoupled Agentic Framework",
            "url": "https://arxiv.org/html/2509.23322v2"
          }
        ]
      },
      "Based on the search results, I found information about M3-ACE:\n\nM3-ACE is a multi-agentic context engineering framework designed to rectify visual perception in multimodal math reasoning. \n\nThe research addresses a key problem in multimodal large language models: their performance is often limited by inaccurate visual perception, with most failures originating from incorrect or incomplete visual evidence extraction rather than deficiencies in reasoning capability.\n\nThe approach decouples perception and reasoning by dynamically maintaining a shared context centered on visual evidence lists. More specifically, the approach introduces structured multi-agent interactions over a shared visual evidence context, enabling cross-validation through consistent, complementary, and conflicting evidence categorization, disagreement resolution via lightweight summary and refinement tools, and iterative refinement of perceptual facts until convergence.\n\nExtensive experiments demonstrate that M3-ACE substantially improves visual mathematical reasoning performance across multiple benchmarks. The paper was published in March 2026 on arXiv (2603.08369)."
    ],
    "durationSeconds": 5.997632973,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "b62aab2d-882f-48df-ab30-c1a0f91cc4d7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-27T08:46:58.049Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GRZno2PjZniuBhiGpkpF8b`</summary>

```json
{
  "query": "Qwen3 VL 8B GRPO training compute GPU hours RL fine-tuning multimodal 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a439a03-2b24-44b7-8da0-83b1b20c5d55",
  "isSidechain": false,
  "requestId": "req_011CbSnLKbo4Wsrtw7HETQQL",
  "type": "assistant",
  "uuid": "0de438d2-8b99-4690-8687-5a04a7583cae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XMiWG9RztmbExqLBMWXDcw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 648,
      "cache_read_input_tokens": 31215,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 648,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 80,
          "cache_read_input_tokens": 31215,
          "cache_creation_input_tokens": 648,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 648
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

_source line 51 · 2026-05-27T08:47:05.643Z_

<details><summary>↩ Tool result · `toolu_01GRZno2PjZniuBhiGpkpF8b`</summary>

```text
Web search results for query: "Qwen3 VL 8B GRPO training compute GPU hours RL fine-tuning multimodal 2026"

Links: [{"title":"Fine-Tuning Qwen3-VL 8B: A Step-by-Step Guide | DataCamp","url":"https://www.datacamp.com/tutorial/fine-tuning-qwen3-vl-8b"},{"title":"Qwen3-VL: How to Run Guide | Unsloth Documentation","url":"https://unsloth.ai/docs/models/tutorials/qwen3-how-to-run-and-fine-tune/qwen3-vl-how-to-run-and-fine-tune"},{"title":"Predictive Scaling Laws for Efficient GRPO Training of Large Reasoning Models","url":"https://arxiv.org/pdf/2507.18014"},{"title":"Qwen3-VL Technical Report","url":"https://arxiv.org/pdf/2511.21631"},{"title":"🚀[Fine-tuning] Qwen3-MoE Megatron Training Implementation and Best Practices👋 · QwenLM/Qwen3 · Discussion #1301","url":"https://github.com/QwenLM/Qwen3/discussions/1301"},{"title":"Qwen3-VL-Embedding and Qwen3-VL-Reranker: A Unified Framework for State-of-the-Art Multimodal Retrieval and Ranking","url":"https://arxiv.org/pdf/2601.04720"},{"title":"Unsloth - Qwen - Read the Docs","url":"https://qwen.readthedocs.io/en/latest/training/unsloth.html"},{"title":"Open-Qwen2VL: Compute-Efficient Pre-Training of Fully-Open Multimodal   LLMs on Academic Resources","url":"https://arxiv.org/pdf/2504.00595"},{"title":"Qwen3-VL-8B-Instruct VRAM Requirement + Unsloth Fine-Tuning (Patch Size, trust_remote_code)","url":"https://kaitchup.substack.com/p/qwen3-vl-fine-tuning-on-your-computer"}]

Based on the search results, I found relevant information about Qwen3-VL 8B GRPO training, though specific GPU hours aren't extensively detailed in these sources. Here's what I found:

## Qwen3-VL 8B and GRPO Training

Unsloth supports fine-tuning and reinforcement learning (RL) Qwen3-VL including the larger 32B and 235B models. Specifically for the 8B variant, the goal of the GRPO notebook is to make a vision language model solve maths problems via RL given an image input.

### Training Approach and Multimodal Support

Post-training comprises three phases: (i) supervised fine-tuning on long chain-of-thought data, (ii) knowledge distillation from stronger teacher models, and (iii) reinforcement learning.

### Efficiency and GPU Requirements

Unsloth makes Qwen3-VL models train 1.7x faster with 60% less VRAM, and for the 8B model specifically, VRAM requirement notes: 4B ~16GB, 8B ~24GB.

The search results don't contain specific GPU hour requirements for GRPO training of Qwen3-VL 8B. While there is research on GRPO scaling laws for other models, the exact compute requirements for the Qwen3-VL 8B GRPO training aren't detailed in the available sources.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0de438d2-8b99-4690-8687-5a04a7583cae",
  "isSidechain": false,
  "promptId": "d4c50c87-a492-4ccd-ad5a-7cc9da96dc22",
  "type": "user",
  "uuid": "00a1ebcd-5ae8-48dd-812f-be1b64a3699d",
  "toolUseResult": {
    "query": "Qwen3 VL 8B GRPO training compute GPU hours RL fine-tuning multimodal 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01UP4CXRRx4PoBpUBUyAEmRz",
        "content": [
          {
            "title": "Fine-Tuning Qwen3-VL 8B: A Step-by-Step Guide | DataCamp",
            "url": "https://www.datacamp.com/tutorial/fine-tuning-qwen3-vl-8b"
          },
          {
            "title": "Qwen3-VL: How to Run Guide | Unsloth Documentation",
            "url": "https://unsloth.ai/docs/models/tutorials/qwen3-how-to-run-and-fine-tune/qwen3-vl-how-to-run-and-fine-tune"
          },
          {
            "title": "Predictive Scaling Laws for Efficient GRPO Training of Large Reasoning Models",
            "url": "https://arxiv.org/pdf/2507.18014"
          },
          {
            "title": "Qwen3-VL Technical Report",
            "url": "https://arxiv.org/pdf/2511.21631"
          },
          {
            "title": "🚀[Fine-tuning] Qwen3-MoE Megatron Training Implementation and Best Practices👋 · QwenLM/Qwen3 · Discussion #1301",
            "url": "https://github.com/QwenLM/Qwen3/discussions/1301"
          },
          {
            "title": "Qwen3-VL-Embedding and Qwen3-VL-Reranker: A Unified Framework for State-of-the-Art Multimodal Retrieval and Ranking",
            "url": "https://arxiv.org/pdf/2601.04720"
          },
          {
            "title": "Unsloth - Qwen - Read the Docs",
            "url": "https://qwen.readthedocs.io/en/latest/training/unsloth.html"
          },
          {
            "title": "Open-Qwen2VL: Compute-Efficient Pre-Training of Fully-Open Multimodal   LLMs on Academic Resources",
            "url": "https://arxiv.org/pdf/2504.00595"
          },
          {
            "title": "Qwen3-VL-8B-Instruct VRAM Requirement + Unsloth Fine-Tuning (Patch Size, trust_remote_code)",
            "url": "https://kaitchup.substack.com/p/qwen3-vl-fine-tuning-on-your-computer"
          }
        ]
      },
      "Based on the search results, I found relevant information about Qwen3-VL 8B GRPO training, though specific GPU hours aren't extensively detailed in these sources. Here's what I found:\n\n## Qwen3-VL 8B and GRPO Training\n\nUnsloth supports fine-tuning and reinforcement learning (RL) Qwen3-VL including the larger 32B and 235B models. Specifically for the 8B variant, the goal of the GRPO notebook is to make a vision language model solve maths problems via RL given an image input.\n\n### Training Approach and Multimodal Support\n\nPost-training comprises three phases: (i) supervised fine-tuning on long chain-of-thought data, (ii) knowledge distillation from stronger teacher models, and (iii) reinforcement learning.\n\n### Efficiency and GPU Requirements\n\nUnsloth makes Qwen3-VL models train 1.7x faster with 60% less VRAM, and for the 8B model specifically, VRAM requirement notes: 4B ~16GB, 8B ~24GB.\n\nThe search results don't contain specific GPU hour requirements for GRPO training of Qwen3-VL 8B. While there is research on GRPO scaling laws for other models, the exact compute requirements for the Qwen3-VL 8B GRPO training aren't detailed in the available sources."
    ],
    "durationSeconds": 7.590366153999988,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "0de438d2-8b99-4690-8687-5a04a7583cae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-27T08:47:10.474Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01461Ft15gw9H18VFWPY1Jjz`</summary>

```json
{
  "query": "multimodal math VLM RLVR training reviewer criticism common issues experiment design ablation AAAI 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00a1ebcd-5ae8-48dd-812f-be1b64a3699d",
  "isSidechain": false,
  "requestId": "req_011CbSnM74m3gSh5afga5DkF",
  "type": "assistant",
  "uuid": "4bb47c65-6e74-4a99-8fe9-75c0d12f0db4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sy9Mcgj9vrEXN9vYDbu57r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1001,
      "cache_read_input_tokens": 31863,
      "output_tokens": 82,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1001,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 82,
          "cache_read_input_tokens": 31863,
          "cache_creation_input_tokens": 1001,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1001
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

_source line 53 · 2026-05-27T08:47:17.420Z_

<details><summary>↩ Tool result · `toolu_01461Ft15gw9H18VFWPY1Jjz`</summary>

```text
Web search results for query: "multimodal math VLM RLVR training reviewer criticism common issues experiment design ablation AAAI 2025 2026"

Links: [{"title":"GitHub - smiles724/Awesome-LLM-RLVR: Collection of latest papers and materials in the area of RLVR! · GitHub","url":"https://github.com/smiles724/Awesome-LLM-RLVR"},{"title":"Spotlight on Token Perception for Multimodal Reinforcement Learning","url":"https://arxiv.org/pdf/2510.09285"},{"title":"Critic-V: VLM Critics Help Catch VLM Errors in Multimodal Reasoning","url":"https://arxiv.org/pdf/2411.18203"},{"title":"Reinforced MLLM: A Survey on RL-Based Reasoning in Multimodal Large Language Models","url":"https://arxiv.org/html/2504.21277v1"},{"title":"Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward","url":"https://arxiv.org/pdf/2506.07218"}]

Based on my search results, here's what I found regarding multimodal math VLM, RLVR training, and related research:

## Recent Research on Multimodal RLVR

Reinforcement learning from verifiable rewards (RLVR) with online algorithms like Group Relative Policy Optimization (GRPO) has dramatically advanced the reasoning capabilities of Large Language Models in text-centric domains such as math and code, and the success of reasoning models such as OpenAI-o1, DeepSeek-R1, and Kimi-k1.5 has demonstrated the efficacy of large-scale reinforcement learning, particularly RLVR, in enhancing advanced reasoning capabilities of LLMs and MLLMs.

## Key Challenges Identified

Research has identified several issues with current multimodal RLVR approaches:

1. **Visual Perception Issues**: Prevailing RLVR frameworks for LVLMs largely neglect the critical role of visual perception in the optimization process. Both standard models and their RLVR-trained variants can make severe perception errors but manage to guess the answer.

2. **Training Approaches**: Research efforts primarily focus on three directions: data-centric enhancements, reward-centric engineering, and other algorithmic adjustments.

## Recent Solutions

Recent works like MM-Eureka and R1-VL successfully stabilized RLVR training in the multimodal domain by incorporating additional training tricks, while R1-OneVision and Vision-R1 constructed large-scale high-quality multimodal datasets by addressing the modality gap issue before applying RLVR.

I did not find specific information about AAAI 2025/2026 papers with reviewer criticisms or detailed ablation studies in these results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4bb47c65-6e74-4a99-8fe9-75c0d12f0db4",
  "isSidechain": false,
  "promptId": "d4c50c87-a492-4ccd-ad5a-7cc9da96dc22",
  "type": "user",
  "uuid": "69b9fb3a-ceb1-4408-8973-bae601073fc4",
  "toolUseResult": {
    "query": "multimodal math VLM RLVR training reviewer criticism common issues experiment design ablation AAAI 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EaCQ7YuhxQ5r1J3NwM1CKW",
        "content": [
          {
            "title": "GitHub - smiles724/Awesome-LLM-RLVR: Collection of latest papers and materials in the area of RLVR! · GitHub",
            "url": "https://github.com/smiles724/Awesome-LLM-RLVR"
          },
          {
            "title": "Spotlight on Token Perception for Multimodal Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2510.09285"
          },
          {
            "title": "Critic-V: VLM Critics Help Catch VLM Errors in Multimodal Reasoning",
            "url": "https://arxiv.org/pdf/2411.18203"
          },
          {
            "title": "Reinforced MLLM: A Survey on RL-Based Reasoning in Multimodal Large Language Models",
            "url": "https://arxiv.org/html/2504.21277v1"
          },
          {
            "title": "Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward",
            "url": "https://arxiv.org/pdf/2506.07218"
          }
        ]
      },
      "Based on my search results, here's what I found regarding multimodal math VLM, RLVR training, and related research:\n\n## Recent Research on Multimodal RLVR\n\nReinforcement learning from verifiable rewards (RLVR) with online algorithms like Group Relative Policy Optimization (GRPO) has dramatically advanced the reasoning capabilities of Large Language Models in text-centric domains such as math and code, and the success of reasoning models such as OpenAI-o1, DeepSeek-R1, and Kimi-k1.5 has demonstrated the efficacy of large-scale reinforcement learning, particularly RLVR, in enhancing advanced reasoning capabilities of LLMs and MLLMs.\n\n## Key Challenges Identified\n\nResearch has identified several issues with current multimodal RLVR approaches:\n\n1. **Visual Perception Issues**: Prevailing RLVR frameworks for LVLMs largely neglect the critical role of visual perception in the optimization process. Both standard models and their RLVR-trained variants can make severe perception errors but manage to guess the answer.\n\n2. **Training Approaches**: Research efforts primarily focus on three directions: data-centric enhancements, reward-centric engineering, and other algorithmic adjustments.\n\n## Recent Solutions\n\nRecent works like MM-Eureka and R1-VL successfully stabilized RLVR training in the multimodal domain by incorporating additional training tricks, while R1-OneVision and Vision-R1 constructed large-scale high-quality multimodal datasets by addressing the modality gap issue before applying RLVR.\n\nI did not find specific information about AAAI 2025/2026 papers with reviewer criticisms or detailed ablation studies in these results."
    ],
    "durationSeconds": 6.939897319000011,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "4bb47c65-6e74-4a99-8fe9-75c0d12f0db4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 54 · 2026-05-27T08:47:17.428Z_

```json
{
  "parentUuid": "69b9fb3a-ceb1-4408-8973-bae601073fc4",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "84e86ffe-6da5-49c8-9ceb-e9e999c58dce",
  "timestamp": "2026-05-27T08:47:17.428Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 55 · 2026-05-27T08:47:20.164Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01T8GVx6pVXYmmEWeRgRwTs1`</summary>

```json
{
  "query": "FIGR \"figure it out\" executable visual states reasoning experiments evaluation baselines 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84e86ffe-6da5-49c8-9ceb-e9e999c58dce",
  "isSidechain": false,
  "requestId": "req_011CbSnMyUPSKugShzdAcSQp",
  "type": "assistant",
  "uuid": "d5e03ab3-ccf4-4382-b464-4e4326311b0a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KqEW4xXF3BcZtUzRY9ddF4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 903,
      "cache_read_input_tokens": 32864,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 903,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 32864,
          "cache_creation_input_tokens": 903,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 903
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

_source line 56 · 2026-05-27T08:47:26.909Z_

<details><summary>↩ Tool result · `toolu_01T8GVx6pVXYmmEWeRgRwTs1`</summary>

```text
Web search results for query: "FIGR "figure it out" executable visual states reasoning experiments evaluation baselines 2025"

Links: [{"title":"[2512.24297] Figure It Out: Improve the Frontier of Reasoning with Executable Visual States","url":"https://arxiv.org/abs/2512.24297"},{"title":"Figure It Out: Improve the Frontier of Reasoning with Executable Visual States","url":"https://arxiv.org/pdf/2512.24297"},{"title":"Figure It Out: Improve the Frontier of Reasoning with Executable Visual States","url":"https://arxiv.org/html/2512.24297"},{"title":"Paper page - Figure It Out: Improving the Frontier of Reasoning with Active Visual Thinking","url":"https://huggingface.co/papers/2512.24297"},{"title":"Figure It Out: Improve the Frontier of Reasoning with Active Visual Thinking","url":"https://arxiv.org/html/2512.24297v1"},{"title":"FigureQA: An Annotated Figure Dataset for Visual Reasoning | Request PDF","url":"https://www.researchgate.net/publication/320564686_FigureQA_An_Annotated_Figure_Dataset_for_Visual_Reasoning"}]

Based on the search results, I found information about FIGR:

## Overview

FIGR integrates executable visual construction into multi-turn reasoning via end-to-end reinforcement learning. Rather than relying solely on textual chains of thought, FIGR externalizes intermediate hypotheses by generating executable code that constructs diagrams within the reasoning loop.

## Key Innovation

Complex reasoning problems often involve implicit spatial and geometric relationships that are not explicitly encoded in text, and purely text-based reasoning struggles to capture structural constraints in complex settings. An adaptive reward mechanism selectively regulates when visual construction is invoked, enabling more consistent reasoning over latent global properties that are difficult to infer from text alone.

## Experimental Results

Experiments on eight challenging mathematical benchmarks demonstrate that FIGR outperforms strong text-only chain-of-thought baselines, improving the base model by 13.12% on AIME 2025 and 11.00% on BeyondAIME.

The paper was published in January 2026 on arXiv and represents a significant advance in combining visual reasoning with executable code generation for solving complex mathematical problems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d5e03ab3-ccf4-4382-b464-4e4326311b0a",
  "isSidechain": false,
  "promptId": "d4c50c87-a492-4ccd-ad5a-7cc9da96dc22",
  "type": "user",
  "uuid": "aed7fcbc-8fe4-4b0f-bc3a-d51391cae466",
  "toolUseResult": {
    "query": "FIGR \"figure it out\" executable visual states reasoning experiments evaluation baselines 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_0149NZXbxsSVcPskKyvJtA6U",
        "content": [
          {
            "title": "[2512.24297] Figure It Out: Improve the Frontier of Reasoning with Executable Visual States",
            "url": "https://arxiv.org/abs/2512.24297"
          },
          {
            "title": "Figure It Out: Improve the Frontier of Reasoning with Executable Visual States",
            "url": "https://arxiv.org/pdf/2512.24297"
          },
          {
            "title": "Figure It Out: Improve the Frontier of Reasoning with Executable Visual States",
            "url": "https://arxiv.org/html/2512.24297"
          },
          {
            "title": "Paper page - Figure It Out: Improving the Frontier of Reasoning with Active Visual Thinking",
            "url": "https://huggingface.co/papers/2512.24297"
          },
          {
            "title": "Figure It Out: Improve the Frontier of Reasoning with Active Visual Thinking",
            "url": "https://arxiv.org/html/2512.24297v1"
          },
          {
            "title": "FigureQA: An Annotated Figure Dataset for Visual Reasoning | Request PDF",
            "url": "https://www.researchgate.net/publication/320564686_FigureQA_An_Annotated_Figure_Dataset_for_Visual_Reasoning"
          }
        ]
      },
      "Based on the search results, I found information about FIGR:\n\n## Overview\n\nFIGR integrates executable visual construction into multi-turn reasoning via end-to-end reinforcement learning. Rather than relying solely on textual chains of thought, FIGR externalizes intermediate hypotheses by generating executable code that constructs diagrams within the reasoning loop.\n\n## Key Innovation\n\nComplex reasoning problems often involve implicit spatial and geometric relationships that are not explicitly encoded in text, and purely text-based reasoning struggles to capture structural constraints in complex settings. An adaptive reward mechanism selectively regulates when visual construction is invoked, enabling more consistent reasoning over latent global properties that are difficult to infer from text alone.\n\n## Experimental Results\n\nExperiments on eight challenging mathematical benchmarks demonstrate that FIGR outperforms strong text-only chain-of-thought baselines, improving the base model by 13.12% on AIME 2025 and 11.00% on BeyondAIME.\n\nThe paper was published in January 2026 on arXiv and represents a significant advance in combining visual reasoning with executable code generation for solving complex mathematical problems."
    ],
    "durationSeconds": 6.740644793000014,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d5e03ab3-ccf4-4382-b464-4e4326311b0a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-27T08:47:30.210Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Dunom3yTiGdsbkMeXsYs24`</summary>

```json
{
  "query": "TrustGeoGen formal-verified data engine geometric problem solving data quality axiom consistency 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aed7fcbc-8fe4-4b0f-bc3a-d51391cae466",
  "isSidechain": false,
  "requestId": "req_011CbSnNfyhYuosb5DeyN6py",
  "type": "assistant",
  "uuid": "bbc4de56-4ab1-473b-9782-a842171893a2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019vP8iASXsdx9JVRFcimwmk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 652,
      "cache_read_input_tokens": 33767,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 652,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 33767,
          "cache_creation_input_tokens": 652,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 652
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

_source line 58 · 2026-05-27T08:47:38.219Z_

<details><summary>↩ Tool result · `toolu_01Dunom3yTiGdsbkMeXsYs24`</summary>

```text
Web search results for query: "TrustGeoGen formal-verified data engine geometric problem solving data quality axiom consistency 2025"

Links: [{"title":"[PDF] TrustGeoGen: Formal-Verified Data Engine for Trustworthy Multi-modal Geometric Problem Solving | Semantic Scholar","url":"https://www.semanticscholar.org/paper/TrustGeoGen:-Formal-Verified-Data-Engine-for-Fu-Chen/1ee64628a20890cd08c9bff7832dbbe0e8c6cce6"},{"title":"TrustGeoGen: Formal-Verified Data Engine for Trustworthy ...","url":"https://arxiv.org/pdf/2504.15780"},{"title":"[2504.15780] TrustGeoGen: Formal-Verified Data Engine for Trustworthy Multi-modal Geometric Problem Solving","url":"https://arxiv.org/abs/2504.15780"},{"title":"TrustGeoGen: Formal-Verified Data Engine for Trustworthy Multi-modal Geometric Problem Solving","url":"https://arxiv.org/html/2504.15780"},{"title":"Paper page - TrustGeoGen: Scalable and Formal-Verified Data Engine for Trustworthy Multi-modal Geometric Problem Solving","url":"https://huggingface.co/papers/2504.15780"},{"title":"GitHub - majianz/dl4gps: [ACL 2026 Main Conference] Paper list for the survey \"A Survey of Deep Learning for Geometry Problem Solving\" · GitHub","url":"https://github.com/majianz/dl4gps"}]

I've found information about TrustGeoGen from the search results. Here's what I found:

## TrustGeoGen Overview

TrustGeoGen is a data engine that generates formally verified geometric problems to establish a principled and trustworthy benchmark, and creates the GeoTrust-200K dataset and the corresponding GeoTrust-test benchmark, both with guaranteed cross-modal integrity.

## Problem It Addresses

Developing capable Multimodal Large Language Models (MLLMs) for geometric problem solving is heavily bottlenecked by the scarcity of high-quality, verifiable data, with existing data acquisition paradigms suffering from modality incompleteness and unverified logical gaps, or relying on formal engines that generate rigid, structurally homogeneous data.

## Architecture and Components

TrustGeoGen consists of four components: (1) a Constructor that generates geometric premises and corresponding diagrams under explicit constraints; (2) a Reasoner that expands formally valid reasoning graphs through rule-based verification; (3) a Sampler that uses GeoExplore to extract high-quality reasoning paths and formulate problem-solution pairs; and (4) a Translator that converts formal derivations into fluent natural-language explanations.

## Key Features

TrustGeoGen strictly guarantees reasoning trustworthiness through formal verification while generating multimodally integrated data, including premises, visual diagrams, and solutions.

The paper was submitted to arXiv in April 2025 and represents a significant advancement in creating trustworthy benchmarks for geometric problem solving.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bbc4de56-4ab1-473b-9782-a842171893a2",
  "isSidechain": false,
  "promptId": "d4c50c87-a492-4ccd-ad5a-7cc9da96dc22",
  "type": "user",
  "uuid": "f71db36c-e562-4bb2-86e9-1683bb7ca4bc",
  "toolUseResult": {
    "query": "TrustGeoGen formal-verified data engine geometric problem solving data quality axiom consistency 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LNpydTtScF3XB6vuQ6kJEG",
        "content": [
          {
            "title": "[PDF] TrustGeoGen: Formal-Verified Data Engine for Trustworthy Multi-modal Geometric Problem Solving | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/TrustGeoGen:-Formal-Verified-Data-Engine-for-Fu-Chen/1ee64628a20890cd08c9bff7832dbbe0e8c6cce6"
          },
          {
            "title": "TrustGeoGen: Formal-Verified Data Engine for Trustworthy ...",
            "url": "https://arxiv.org/pdf/2504.15780"
          },
          {
            "title": "[2504.15780] TrustGeoGen: Formal-Verified Data Engine for Trustworthy Multi-modal Geometric Problem Solving",
            "url": "https://arxiv.org/abs/2504.15780"
          },
          {
            "title": "TrustGeoGen: Formal-Verified Data Engine for Trustworthy Multi-modal Geometric Problem Solving",
            "url": "https://arxiv.org/html/2504.15780"
          },
          {
            "title": "Paper page - TrustGeoGen: Scalable and Formal-Verified Data Engine for Trustworthy Multi-modal Geometric Problem Solving",
            "url": "https://huggingface.co/papers/2504.15780"
          },
          {
            "title": "GitHub - majianz/dl4gps: [ACL 2026 Main Conference] Paper list for the survey \"A Survey of Deep Learning for Geometry Problem Solving\" · GitHub",
            "url": "https://github.com/majianz/dl4gps"
          }
        ]
      },
      "I've found information about TrustGeoGen from the search results. Here's what I found:\n\n## TrustGeoGen Overview\n\nTrustGeoGen is a data engine that generates formally verified geometric problems to establish a principled and trustworthy benchmark, and creates the GeoTrust-200K dataset and the corresponding GeoTrust-test benchmark, both with guaranteed cross-modal integrity.\n\n## Problem It Addresses\n\nDeveloping capable Multimodal Large Language Models (MLLMs) for geometric problem solving is heavily bottlenecked by the scarcity of high-quality, verifiable data, with existing data acquisition paradigms suffering from modality incompleteness and unverified logical gaps, or relying on formal engines that generate rigid, structurally homogeneous data.\n\n## Architecture and Components\n\nTrustGeoGen consists of four components: (1) a Constructor that generates geometric premises and corresponding diagrams under explicit constraints; (2) a Reasoner that expands formally valid reasoning graphs through rule-based verification; (3) a Sampler that uses GeoExplore to extract high-quality reasoning paths and formulate problem-solution pairs; and (4) a Translator that converts formal derivations into fluent natural-language explanations.\n\n## Key Features\n\nTrustGeoGen strictly guarantees reasoning trustworthiness through formal verification while generating multimodally integrated data, including premises, visual diagrams, and solutions.\n\nThe paper was submitted to arXiv in April 2025 and represents a significant advancement in creating trustworthy benchmarks for geometric problem solving."
    ],
    "durationSeconds": 8.005221350000006,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "bbc4de56-4ab1-473b-9782-a842171893a2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 59_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Axiom-Grounded Self-Verified Perception for Visual Math Reasoning  ## Core Problem and Thesis  Current multimodal math reasoning systems verify perceived visual facts independently—checking each cla…",
  "leafUuid": "f71db36c-e562-4bb2-86e9-1683bb7ca4bc",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164"
}
```

---

### Runtime record

_source line 60_

```json
{
  "type": "ai-title",
  "aiTitle": "Axiom-grounded self-verified perception for math reasoning",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164"
}
```

---

### Assistant

_source line 61 · 2026-05-27T08:50:15.449Z_

Now I have comprehensive pre-research. Let me synthesize my findings and produce the formal assessment.

---

【状态】: 有缺陷待补救

【前置调研发现】
- **Perception-R1** (arXiv 2025): 实验使用 Qwen2.5-VL-7B 为 base，在 MathVista/MathVerse/MathVision/WeMath/MMMU/MMStar 上评测；baseline 包含 base model zero-shot、SFT、answer-only GRPO、以及多个同规模开源 VLM；ablation 拆解了 perception reward 与 outcome reward 的独立贡献；仅用 1,442 条训练数据即超越 10-100× 数据量的 baseline。
- **PEARL** (arXiv 2025): 在 MathVerse/WeMath/MathVista 上评测；baseline 含 GRPO/DAPO 及多种 RL 方法；ablation 验证 perception checklist gating 的作用；+9.7% on MathVerse, +6.6% over GRPO。
- **GeoDPO** (arXiv 2026): 构建 GeoPerceive benchmark 独立评测 perception；in-domain +26.5%, out-of-domain +8.0%, downstream +39%；baseline 含 SFT 和 direct RL；关键实验是 perception-only 和 downstream reasoning 的分离评测。
- **PRCO** (arXiv 2026): Observer/Solver 双角色框架；在 8 个 multimodal reasoning benchmark 上评测，含 3B 和 7B 两种规模；ablation 分别移除 Observer 更新和 Solver 更新，证明 utility reward 的关键性；+7.65 (3B) 和 +7.18 (7B) 平均提升。
- **SSL-R1** (arXiv 2026): 基于 Qwen2.5-VL-3B，在 13 个 benchmark 上评测；ablation 比较不同 SSL 任务（rotation prediction, patch ordering, geometric correspondence, visual similarity）的独立贡献。
- **SymHPR** (arXiv 2025): 用合成数据+规则奖励训练，hierarchical step-level parsing reward；评测含 diagram reconstruction MSE、chart reconstruction、MathGlance perception 任务。
- **Milestones over Outcome (SGVR)** (arXiv 2025): 使用 GRPO + skeleton rate reward；在 geometric/general math/general reasoning 三类 benchmark 上评测；用 TrustGeoGen/GeoGoal 的形式化验证 sub-goal。
- **Geoparsing** (arXiv 2026): GDP-29K 数据集 (20k plane + 9k solid)；SFT+RLVR 训练范式；评测 parsing 准确率和 downstream reasoning 提升。
- **TrustGeoGen** (arXiv 2025): 形式化验证数据引擎；4组件架构 (Constructor/Reasoner/Sampler/Translator)；产出 GeoTrust-200K 数据集。
- **FIGR** (arXiv 2025): executable visual states + RL；评测 8 个数学 benchmark，AIME 2025 +13.12%。
- **M3-ACE** (arXiv 2026): 多智能体推理时 perception 矫正；在多个 multimodal math benchmark 上评测。
- **V-Zero** (arXiv 2026): Questioner-Solver GRPO co-evolution；zero annotation；在 multimodal reasoning benchmark 上评测。

- **调研总结**: 该领域当前实验设计标准要求：(1) 在 MathVista/MathVerse/MathVision 三大 benchmark + 至少一个几何专用 benchmark (GeoQA/formalgeo7k) 上全面评测；(2) baseline 必须覆盖 base model zero-shot、SFT-only、answer-only RL 以及至少 2-3 个同期 perception-focused RL 方法进行公平对比；(3) ablation 必须拆解 reward 各组件的独立贡献并做 scale transfer 验证；(4) 审稿人高度关注 compute fairness (FLOPs-matched comparison)、reward signal 质量的实证验证、以及 training-time vs inference-time 方法的消融。该 proposal 的实验方案已经相当接近领域标准，但有若干可补强之处。

---

【缺陷 1】
- 类别: baseline 不足或过时
- 问题: Proposal 在 baselines 的 "Perception RL methods" 类别中仅列出 Perception-R1 和 GeoDPO，但遗漏了 **PRCO (arXiv 2026)**——该方法是当前 perception-reasoning 联合训练的 SOTA 之一（3B +7.65, 7B +7.18 平均提升），且其 Observer/Solver 双角色设计与本 proposal 的 "perception 先行 → reasoning 跟进" 训练范式有直接可比性。PRCO 虽然被列在 "Reference numbers (reported results where available)" 中，但仅引用报告数值而不做可控对比实验，审稿人极可能质疑：你的 axiom-based reward 相比 PRCO 的 utility-based perception reward 到底好在哪里？此外，**SGVR (Milestones over Outcome, arXiv 2025)** 在几何推理上实现了 +9.7% 提升，且同样使用 GRPO + sub-goal verifiable reward，与本 proposal 的 axiom-consistency reward 在 reward 信号设计上高度可比，却完全未出现在 baseline 列表中。
- 严重度: 可补救
- 补救方案: (1) 将 PRCO 从 "reference numbers" 提升为**可控复现 baseline**——使用相同 base model (Qwen3-VL-8B)、相同训练数据量、相同 GRPO 框架，替换 reward signal 为 PRCO 的 utility reward，进行 head-to-head 对比。PRCO 已开源代码 (GitHub)，复现成本较低。(2) 新增 SGVR 作为 baseline——同样使用 GRPO，将 reward 替换为 SGVR 的 skeleton rate reward。此对比可直接回答 "axiom-consistency reward vs sub-goal verifiable reward" 的核心问题。(3) 这两个 baseline 的训练开销约增加 2×30h = 60h GPU time (H100)，在资源预算内可消化。
- 调研依据: PRCO (arXiv 2603.28618) 在 8 个 benchmark 上均优于 GRPO baseline；SGVR (arXiv 2601.05073) 在 GeoQA 等几何 benchmark 上使用相同 GRPO 框架的 sub-goal reward 取得显著提升。两者均已开源且使用 GRPO 训练，与本 proposal 在技术框架上直接可比。

【缺陷 2】
- 类别: 评估方案缺陷
- 问题: Proposal 的 benchmark 选择中缺少对 **perception 本身的独立评测**。当前方案仅用端到端 QA accuracy (MathVista/MathVerse/MathVision/GeoQA/formalgeo7k) 评测，但本 proposal 的核心 claim 是 "改善 perception"，而端到端 accuracy 同时受 perception 和 reasoning 双重因素影响，无法隔离 perception 的改善。GeoDPO 论文专门构建了 **GeoPerceive benchmark** 来独立评测 perception accuracy（与 reasoning 解耦），PRCO 在 ablation 中也分别报告了 Observer 和 Solver 的独立表现。如果不独立评测 perception quality，审稿人会质疑：accuracy 提升是否真的来自 perception 改善，还是 RL 训练间接改善了推理？
- 严重度: 可补救
- 补救方案: (1) 引入 **GeoPerceive** (GeoDPO 提出) 作为 perception-only 评测 benchmark，直接报告 diagram element extraction accuracy（点、线、角度、长度识别精度），与 GeoDPO 和 SFT baseline 进行 perception-level 对比。(2) 在 MathVerse 的 **vision-only subset** 上做更细粒度的 error analysis——将错误分类为 perception error vs reasoning error（参考 MM-MATH 的 error taxonomy），量化 perception error 比例在训练前后的变化。(3) 在已标注 ground-truth 的子集上，报告 perceived value 与 ground-truth 的 **平均绝对误差 (MAE)**（如角度 MAE、长度比 MAE），直接衡量 perception 精度而非间接通过 QA accuracy 推断。
- 调研依据: GeoDPO (arXiv 2602.22703) 专门构建 GeoPerceive 来隔离评测 perception；MM-MATH (arXiv 2024) 提出 61% 错误为 perception error 的分类方法论；PRCO 分别报告 Observer/Solver 表现以隔离 perception 贡献。

【缺陷 3】
- 类别: ablation 不完整
- 问题: Proposal 在 ablation 中缺少一个关键对照实验：**axiom-consistency reward vs. ground-truth perception reward 的 oracle comparison**。本 proposal 的核心 selling point 是 "无需标注的自监督 axiom reward 可以替代需要标注的 perception reward"，但如果不在有标注的子集上比较 axiom reward 与 ground-truth perception reward (如 PEARL 的 checklist reward 或直接用 GT 角度/长度值计算 reward) 的训练效果差异，审稿人无法判断 axiom reward 相对于 oracle supervision 的 gap 有多大——这个 gap 决定了 "free reward signal" 这个优势到底值不值。
- 严重度: 可补救
- 补救方案: 在 formalgeo7k 或 GeoTrust (TrustGeoGen 产出) 等有 ground-truth formal annotation 的子集上，额外做一组 ablation：(a) GT perception reward（直接用 ground-truth 值计算 perception accuracy 作为 reward），(b) axiom-consistency reward (proposed)，(c) combined GT + axiom reward。训练相同 steps，对比最终 performance。这能量化 "axiom reward 作为 free proxy" 相对于 oracle GT reward 的性能差距，明确 annotation-free 的代价有多大。如果 gap 小，则有力支撑 proposal 的核心优势；如果 gap 大，至少诚实报告。此 ablation 仅需 2-3 次额外 training run（在小数据集上），GPU 开销约 40-60h。
- 调研依据: PEARL (arXiv 2511.18437) 使用 GT-annotated perception checklist 作为 reward 达到 +9.7%，Perception-R1 使用 LLM-judged reward 也需要 textual annotations；本 proposal 声称 axiom reward 是 "free" 的替代，但缺少与 GT-supervised reward 的直接对比来量化 gap。

【缺陷 4】
- 类别: 实验设计不足
- 问题: Proposal 在 "Reward signal quality" 分析中提到会计算 axiom-consistency score 与 true perception accuracy 的 correlation，以及 false positive / false negative rate，这很好。但缺少对一个关键 failure mode 的分析：**axiom-satisfying but perceptually wrong 的系统性漏洞**。例如，一个等边三角形的三个角都被感知为 70°，满足 70+70+70 ≠ 180 所以会被检测到；但如果被感知为 58°, 62°, 60°，角度和为 180° 满足 axiom 但值全部不精确。更严重的是，对于约束不充分的图形（如一般四边形），axiom 提供的约束很弱（内角和 360° 只约束 4 个角的和），大量 individually incorrect 的感知可以满足这一约束。Proposal 需要系统分析：**不同图形类型/复杂度下 axiom reward 的鉴别力 (discriminability) 如何变化**，以及 axiom 约束不充分时会出现什么退化。
- 严重度: 可补救
- 补救方案: (1) 在 "Reward signal quality" 分析中增加 **按图形类型分层的 false positive rate 分析**：分别报告三角形 (强约束: 3 angles sum to 180, Pythagorean, etc.)、四边形 (中等约束)、圆相关 (圆周角定理等，中强约束)、复合图形 (弱约束) 的 axiom reward false positive rate。(2) 设计 **adversarial perception test**：在 GT 值上添加不同幅度的随机扰动 (σ=1°,2°,5°,10°)，观察 axiom checker 在不同约束密度下的检测率曲线——这可以量化 axiom reward 的 "detection frontier"。(3) 对于约束稀疏的图形类型，探索是否可以通过推导更多隐含约束 (e.g., 利用辅助线推导的额外角度关系) 来增加约束密度，并在 ablation 中报告 "基础 axiom set" vs "增强 axiom set" 的 false positive rate 差异。
- 调研依据: 基于领域实验规范判断。FormalGeo 的 axiom 系统包含 40+ 定理但其覆盖密度因图形类型而异；TrustGeoGen 的形式化验证引擎提供了量化约束充分性的工具参考。

【缺陷 5】
- 类别: compute 公平性问题
- 问题: Proposal 提到会 "report training wall-clock time and per-step overhead" 以及 "plot performance vs. training FLOPs curves"，这些是必要的。但存在一个微妙的 compute fairness 问题：**Stage 0 SFT warm-start 为本方法提供了额外的训练信号**（Geoparsing/FormalGeo 数据上的 SFT），而 Perception-R1、SSL-R1 等 baseline 不使用此类 SFT warm-start。如果不控制这个变量，审稿人可能质疑：performance gain 是来自 axiom reward，还是来自 Stage 0 的额外 SFT 数据？Proposal 的 ablation 中有 "skip Stage 0 (no warm-start)"，但这只测试了本方法去掉 Stage 0 的效果，没有为 baseline 方法加上同等 Stage 0 的效果。
- 严重度: 可补救
- 补救方案: 为所有 RL baseline（Perception-R1, GeoDPO, SSL-R1, answer-only GRPO）提供 **两种起点**: (a) 从 Qwen3-VL-8B raw 出发，(b) 从 Stage 0 SFT checkpoint 出发。这样可以隔离 "Stage 0 SFT 带来的增益" 和 "各自 RL reward 带来的增益"。具体而言，如果本方法 "Stage 0 + axiom RL" 优于 "Stage 0 + answer-only GRPO"，则证明 axiom reward 的独立贡献。这额外需要 3-4 次 training runs（在 Stage 0 checkpoint 上用不同 reward 训练），约 100-120h GPU time。这可能稍微超出原始预算但对论文说服力至关重要。
- 调研依据: GeoDPO (arXiv 2602.22703) 的实验中明确对比了 SFT 和 RL 的独立贡献；PEARL 在 ablation 中也控制了 base training 的一致性；Geoparsing 本身使用 SFT+RLVR 范式，Stage 0 使用其数据等于引入了额外 supervision。

【缺陷 6】
- 类别: 可行性问题
- 问题: Proposal 的 axiom checker 需要实现 **40+ geometric theorems** 的自动化验证，加上 chart 和 function invariants。这个工程量不小且有两个可行性风险：(1) **axiom checker 的鲁棒性**——real-world diagram 的 VLM 输出可能含 parsing error（标签错误、元素遗漏、坐标系不一致），axiom checker 需要在 noisy input 下仍然给出有意义的 reward，而非大量 parse failure 导致 reward signal 极其稀疏。(2) **axiom 覆盖率**——40+ 定理听起来多，但对于复杂的组合几何图形（e.g., 圆内接四边形 + 切线 + 辅助线），很多约束关系需要先推导出隐含关系才能应用（类似于 FGeo-DRL 中的 theorem application chain），这不是简单的 "check if angle_sum == 180°"，而需要几何推理。Resource estimate 中为 axiom checker 开发只预留了 2 周时间。
- 严重度: 可补救
- 补救方案: (1) **分层实现策略**: 第一版 axiom checker 仅实现最高频、最直接的 ~15 条 axiom（三角形角和/边关系、平行线性质、圆心角/圆周角关系、勾股定理），这些是 "直接可检查" 的无需推理链的约束，可在 2 周内完成。第二版再扩展需要 1-step 推导的 axiom。在 ablation 中本身已有 "full 40+ axioms vs basic axioms only" 的对比，因此即使只实现基础 axiom set 也能作为可报告的结果。(2) **利用 FormalGeo 已有基础设施**: FormalGeo 框架本身已实现了大量几何定理的形式化验证（FGeo-DRL 基于此达到 86.4%），可直接调用 FormalGeo 的 theorem checker 而非从零实现。Geoparsing 的 formal language 也与 FormalGeo 兼容。这大幅降低工程量。(3) **为 noisy input 设计 fallback**: 当 VLM 输出无法完整 parse 时（e.g., 缺少某些元素），axiom checker 应只检查 parseable 的子集约束，而非返回 0 reward。Proposal 已提到 "parsability reward" 作为辅助，但应明确描述 graceful degradation 策略。(4) 时间线建议调整为 3 周 (axiom checker) + 3-4 周 (RL training) + 3 周 (evaluation + writing)，总时间线略有延长但更现实。
- 调研依据: FormalGeo (arXiv 2023) 和 FGeo-DRL (arXiv 2024) 已提供 theorem verification 基础设施；Geoparsing (arXiv 2604.11600) 确认与 FormalGeo formal language 的兼容性；TrustGeoGen 的 Reasoner 组件实现了 rule-based verification 可作为参考。

【缺陷 7】
- 类别: 实验设计不足
- 问题: Proposal 声称 axiom-consistency 原则可推广到非数学领域（电路图的 Kirchhoff 定律、化学结构的 valence 约束等），但实验设计完全局限于数学 diagram。虽然 generalization claim 的实验验证不是必须的（论文可以留为 future work），但如果只字不提任何初步验证，审稿人可能认为这只是空口承诺。然而此条需要权衡——增加额外 domain 的实验会大幅增加工作量和资源需求。
- 严重度: 可补救（低优先级）
- 补救方案: **不建议为此增加完整实验**，但建议：(1) 在论文 discussion 中明确将此定位为 "conceptual contribution + future work"，而非 paper 的主要 claim。(2) 如果时间允许，可做一个 **最小 proof-of-concept**：在一个 chart-type 子任务上（MathVista 含大量 chart 题目，sum-to-total 是简单可实现的 axiom），展示 axiom checker 在 chart 数据上也能提供有效 reward signal，以最小成本增加一个 generalization 数据点。这无需额外数据集，只需 axiom checker 的 chart module（Proposal 的 axiom checker 本身就计划包含 "chart and function invariants"）。
- 调研依据: 基于领域实验规范判断。AAAI 审稿人通常对 over-claim 很敏感，但对 clearly-scoped future work 接受度高。

【缺陷 8】
- 类别: 评估方案缺陷
- 问题: Proposal 列出了 MathVista / MathVerse / MathVision / GeoQA / formalgeo7k 五个 benchmark，但缺少一个在该领域近期被广泛采用的 benchmark：**WeMath**。Proposal 将 WeMath 标注为 "optional extension"，但调研发现 Perception-R1 和 PEARL 都在 WeMath 上报告了结果，PRCO 也在类似规模的 benchmark suite 上评测。如果主要 baseline 方法（Perception-R1, PEARL）都报告了 WeMath 结果但本 proposal 不报告，审稿人可能要求补实验。此外，**MathGlance** (SymHPR 使用的 perception-focused benchmark) 也值得考虑。
- 严重度: 可补救（低优先级）
- 补救方案: 将 WeMath 从 "optional" 提升为 **主要评测 benchmark**，与 MathVista/MathVerse/MathVision 并列。WeMath 的评测成本很低（inference only），不增加训练开销。MathGlance 可保持 optional。
- 调研依据: Perception-R1 和 PEARL 均在 WeMath 上报告结果；不在相同 benchmark 上对比会给审稿人留下 "cherry-picking benchmark" 的印象。

---

**整体评估**: 该 proposal 的实验设计已经达到中等偏上水平，展示了对领域实验规范的良好理解——5 组 ablation、compute fairness 分析、scale transfer 验证、training-time vs inference-time 对比等设计均为加分项。上述 8 条缺陷中，**缺陷 1（baseline 补充 PRCO/SGVR）、缺陷 2（独立 perception 评测）、缺陷 3（axiom reward vs GT reward oracle comparison）** 为高优先级，直接关系到核心 claim 的可信度；**缺陷 5（compute fairness for Stage 0）** 为中高优先级，审稿人大概率会提到；其余为中低优先级的加固措施。所有缺陷均可补救，未发现方向性致命问题。补救后预计增加 200-300h GPU time，需相应调整资源预算。

Sources:
- [Perception-R1](https://arxiv.org/abs/2506.07218)
- [PEARL](https://arxiv.org/abs/2511.18437)
- [GeoDPO](https://arxiv.org/abs/2602.22703)
- [EVPV](https://arxiv.org/abs/2603.16253)
- [PRCO](https://arxiv.org/abs/2603.28618)
- [SSL-R1](https://arxiv.org/abs/2604.20705)
- [SymHPR](https://arxiv.org/abs/2512.03126)
- [Milestones over Outcome (SGVR)](https://arxiv.org/abs/2601.05073)
- [Geoparsing](https://arxiv.org/abs/2604.11600)
- [TrustGeoGen](https://arxiv.org/abs/2504.15780)
- [FGeo-DRL](https://arxiv.org/abs/2402.09051)
- [FIGR](https://arxiv.org/abs/2512.24297)
- [M3-ACE](https://arxiv.org/abs/2603.08369)
- [V-Zero](https://arxiv.org/abs/2601.10094)
- [Qwen3-VL Technical Report](https://arxiv.org/abs/2511.21631)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f71db36c-e562-4bb2-86e9-1683bb7ca4bc",
  "isSidechain": false,
  "requestId": "req_011CbSnPWKJXfR8ZCAuyKQPX",
  "type": "assistant",
  "uuid": "e5f32e40-3adf-493a-a6e9-07397e94291a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DoC7cRaArHtX3ze8taFAfs",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 856,
      "cache_read_input_tokens": 34419,
      "output_tokens": 7149,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 856,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7149,
          "cache_read_input_tokens": 34419,
          "cache_creation_input_tokens": 856,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 856
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
  "leafUuid": "e5f32e40-3adf-493a-a6e9-07397e94291a",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164"
}
```

---

### Runtime record

_source line 63_

```json
{
  "type": "ai-title",
  "aiTitle": "Axiom-grounded self-verified perception for math reasoning",
  "sessionId": "52f19b28-98e1-4c6f-ab76-67a25e50a164"
}
```

---
