# Research conversation: Premise-Graph Contrastive Training for Logic-Grounded Process Reward Models ## Core Problem Current process reward model

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 48
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-2/75462fa2-385d-4000-b649-57c64df02312.jsonl`
- **Structured JSON:** [`b3c7f0eb4cb55a12e6e4.json`](../../sessions/b3/b3c7f0eb4cb55a12e6e4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-27T08:42:36.116Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T08:42:36.116Z",
  "sessionId": "75462fa2-385d-4000-b649-57c64df02312",
  "content": "# Premise-Graph Contrastive Training for Logic-Grounded Process Reward Models\n\n## Core Problem\n\nCurrent process reward models detect consistency rather than causality. \"Reward Models Identify Consistency, Not Causality\" (arXiv:2502.14619, Feb 2025) established that PRMs verify surface-level coherence between steps — not whether each step logically follows from its premises. \"Reward Under Attack\" (arXiv:2603.06621, Feb 2026) quantified the consequences: 43% of PRM reward gains are attributable to stylistic shortcuts, and RL-trained policies achieve >0.9 PRM scores but <4% actual accuracy. The root cause is that standard PRM training provides only point-wise step-correctness supervision, which is blind to the logical dependency structure connecting reasoning steps. Can we train PRMs whose representations explicitly encode premise-dependency awareness — sensitivity to which conclusions actually follow from which premises — rather than mere surface consistency?\n\n## Research Opportunity and Key Insight\n\nA critical representation-utilization gap exists in current PRMs. \"From Chains to DAGs\" (arXiv:2601.17593, Jan 2026) proved that LLM hidden states already linearly encode DAG reasoning structure — node depth, pairwise distance, and adjacency are recoverable from intermediate layers via lightweight probes. Yet \"Reward Models Identify Consistency, Not Causality\" (arXiv:2502.14619) showed that standard PRM training fails to channel this latent structural knowledge into reward prediction: PRMs remain insensitive to whether premise-conclusion links are logically valid. PARC/PERL (ICML 2025, arXiv:2502.02362) demonstrated that premise dependency links are extractable at >90% recall (on 70B+ models), and premise-aware verification improves error detection by 6-16%. DAG-Math (arXiv:2510.19842, 2025) and ProofFlow (arXiv:2510.15981, 2025) further established feasibility of dependency graph extraction from mathematical reasoning chains.\n\nOur key insight: contrastive training anchored to premise dependency DAGs can bridge this representation-utilization gap. By constructing training pairs that hold surface form constant while varying logical structure (and vice versa), we force the PRM's embedding space to explicitly encode premise-dependency relationships — activating the structural representations the model already possesses but that point-wise BCE training leaves dormant. This constitutes a shift from point-wise supervision (each step independently correct/incorrect) to relational supervision (structural relationships between steps encoded in representation space).\n\n## Research Landscape\n\n**PRM robustness failures and existing defenses.** \"Reward Under Attack\" (arXiv:2603.06621) established a three-tier diagnostic: static perturbation exploitability, adversarial token-level attacks, and RL-induced reward hacking. Existing defenses span complementary strategies: CRA (Aug 2025, arXiv:2508.04216, post-hoc sparse autoencoder correction), APRM (Nov 2025, arXiv:2511.22888, adversarial training with harder negatives, +5.3pp OOD), CRM (ICLR 2026, arXiv:2509.26578, sequential conditioning on preceding steps), and PURE (NeurIPS 2025, arXiv:2504.15275, min-form credit aggregation). None uses explicit logical dependency structure during PRM training. APRM is the closest methodological comparator: its adversarial negatives improve the single-step classification decision boundary but remain domain-agnostic — the PRM learns to resist specific adversarial patterns without understanding why those patterns are wrong. PGCT instead reorganizes the PRM's representation space around premise-dependency topology, providing a semantically grounded and transferable capability rather than pattern-specific robustness.\n\n**Reasoning-enhanced PRMs.** R-PRM (arXiv:2503.21295, 2025) augments PRMs with reasoning-driven critique, achieving +11.9 F1 on ProcessBench and +8.5 on PRMBench over same-data baselines. GenPRM (AAAI 2026, arXiv:2504.00891) employs generative CoT + code verification for step analysis, surpassing all same-scale discriminative PRMs. ThinkPRM (arXiv:2504.16828, 2025) demonstrates that generative verification with only 1% of PRM800K labels can outperform full-data discriminative PRMs. These approaches enhance verification through richer inference-time reasoning. PGCT is orthogonal: it improves training-time representation learning. PGCT-trained representations could potentially serve as improved backbones for generative verification methods.\n\n**Graph structure for verification.** CRV (ICLR 2026, arXiv:2510.09312) uses attribution graph structural fingerprints to verify reasoning (white-box, inference-time). GoV decomposes reasoning into DAGs for training-free verification. AgentEval (arXiv:2604.23581, 2026) showed DAG-based dependency modeling yields +22pp failure detection recall. These independent lines confirm that graph structure carries powerful verification signal. PGCT is the first to inject this signal into PRM training objectives.\n\n**Concurrent contrastive/graph approaches.** CPMI (arXiv:2604.10660, April 2026) uses contrastive mutual information for PRM auto-labeling without premise dependency graphs. RewardFlow (arXiv:2603.18859, March 2026) propagates rewards over state-transition graphs in agentic tasks without contrastive training. Thought-Path Contrastive Learning (AAAI 2025, arXiv:2409.14495) constructs premise-oriented contrastive examples for logical reading comprehension, but operates on propositional-level premise-conclusion pairs (not multi-step mathematical reasoning DAGs) and targets discriminative reading accuracy rather than PRM robustness.\n\n**Performance gap.** The best open-source PRM on PRMBench scores 67.7 (PathFinder-PRM-7B, arXiv:2505.19706) vs. 83.8 human ceiling. The specific combination of premise dependency DAGs with contrastive PRM training remains untried.\n\n## Proposed Approach\n\n**DAG extraction.** Extract premise dependency DAGs from mathematical reasoning chains using PARC's extraction method with Qwen2.5-72B-Instruct (targeting >90% recall as demonstrated on 70B-class models in PERL, ICML 2025, arXiv:2502.02362). Each reasoning step is a node; directed edges encode \"step j uses the result of step i as a premise.\"\n\n**Contrastive pair construction.** Two types of structure-aware pairs: (1) Graph-preserving surface perturbations (rephrased steps, identical DAG topology) as positives; (2) Graph-breaking fluent perturbations (severed premise links, dangling references, logically invalid steps maintaining surface fluency) as hard negatives. Quality assurance pipeline: re-extract DAGs from generated pairs to verify topology preservation/breaking; stratified human audit (~1000 pairs across math subdomains × DAG complexity levels) with quality thresholds (topology preservation rate ≥90% for positives, premise-link corruption verification ≥85% for negatives) and inter-annotator agreement (2 annotators, Cohen's κ on ~200-pair overlap).\n\n**Dual objective training.** Qwen2.5-Math-7B-Instruct-based PRM trained with: (a) standard step-correctness BCE loss (point-wise supervision), and (b) graph-contrastive InfoNCE loss over DAG-anchored step embeddings (relational supervision). The InfoNCE loss explicitly requires \"same DAG topology → nearby embeddings, different topology → distant embeddings,\" forcing the representation space to reflect premise-dependency structure. This complements CRM (ICLR 2026, arXiv:2509.26578), which conditions predictions sequentially on preceding steps but operates in a point-wise prediction paradigm without encoding relational structure in embedding space.\n\n**Important scope clarification.** PGCT trains two distinct but complementary capabilities: (1) structural dependency sensitivity — detecting whether premise links between steps are correctly maintained (directly via DAG topology contrastive learning), and (2) partial semantic inference validity — detecting logically invalid reasoning steps that preserve surface fluency (via graph-breaking hard negatives). We do not claim PGCT achieves full logical causality verification, but rather that premise-dependency awareness substantially narrows the consistency-causality gap that current PRMs exhibit.\n\n**Data.** PRM800K + Math-Shepherd seed chains (~300K solutions) augmented with DAG annotations and ~600K contrastive pairs via LLM paraphrasing (7B/32B models for generation, 72B for quality verification) and targeted premise-link corruption.\n\n## Evaluation Plan\n\n**Benchmarks (4-tier, with ID/OOD split):**\n1. **Step-level error detection**: PRMBench (ACL 2025, arXiv:2501.03124) with per-error-category breakdown (soundness/sensitivity/simplicity; redundancy, circular logic, step inconsistency, domain inconsistency, deceptive logical steps), targeting >70 overall (vs. 67.7 PathFinder-PRM SOTA) with disproportionate gains on logic-structure-related error types. ProcessBench (arXiv:2412.06559) with per-difficulty-level F1 (easy/medium/hard/competition).\n2. **Downstream best-of-N reranking**: ID: MATH500, GSM8K; OOD: AIME 2024, AMC. N ∈ {8, 16, 64} candidates from Qwen2.5-Math-7B-Instruct. Report prm@N accuracy with ID vs. OOD breakdown.\n3. **Adversarial robustness**: PRM-BiasBench and perturbation suite from \"Reward Under Attack\" (arXiv:2603.06621).\n4. **RL closed-loop reward hacking**: GRPO training of Qwen2.5-Math-7B-Instruct policy using PGCT-PRM vs. baseline PRMs as reward signal. 3000-5000 GRPO steps, checkpoint every 200 steps, evaluate on MATH and AIME. Metrics: (a) hacking gap = (PRM score improvement) − (ground-truth accuracy improvement) over training; (b) reward-accuracy Pearson correlation with 95% CI from 3 random seeds; (c) late-stage divergence ratio (reward growth / accuracy growth in final 30% of training).\n\n**Baselines (6 tiers):**\n1. Standard PRM: Qwen2.5-Math-PRM-7B (same base model)\n2. Robustness-focused: APRM (arXiv:2511.22888), CRA (arXiv:2508.04216)\n3. Architecture-level: CRM (ICLR 2026, arXiv:2509.26578), PURE (NeurIPS 2025, arXiv:2504.15275)\n4. Contrastive/concurrent: CPMI (arXiv:2604.10660)\n5. Error-aware: PathFinder-PRM-7B (arXiv:2505.19706)\n6. Reasoning-enhanced: R-PRM (arXiv:2503.21295), GenPRM-7B (AAAI 2026, arXiv:2504.00891, fixed-compute, no test-time scaling)\n- Data-matched control: ~900K total samples, contrastive pairs replaced with additional step-correctness annotations, standard BCE\n- Compute-matched control: equal total training FLOPs including DAG extraction overhead\n\n**Ablations (8 variants):**\n- A1: Remove InfoNCE loss → isolate contrastive learning contribution\n- A2: Remove step-correctness loss → test contrastive learning standalone\n- A3: Random perturbation replacing DAG-aware perturbation → **critical: isolate DAG structure contribution**\n- A4: Only positives (no graph-breaking negatives) → isolate hard negative contribution\n- A5: Only negatives (no graph-preserving positives) → isolate surface-invariance contribution\n- A6: Loss weighting λ ∈ {0.1, 0.3, 0.5, 0.7, 1.0}\n- A7: DAG noise injection at 5%/10%/15%/20% → robustness to extraction errors\n- A8: DAG extraction model scale: 7B / 32B / 72B extractors → practical viability curve\n\n## Key References\n\n- Reward Under Attack (arXiv 2026, arXiv:2603.06621)\n- Reward Models Identify Consistency, Not Causality (arXiv 2025, arXiv:2502.14619)\n- PARC/PERL (ICML 2025, arXiv:2502.02362)\n- From Chains to DAGs (arXiv 2026, arXiv:2601.17593)\n- DAG-Math (arXiv 2025, arXiv:2510.19842)\n- ProofFlow (arXiv 2025, arXiv:2510.15981)\n- CRA (arXiv 2025, arXiv:2508.04216)\n- APRM (arXiv 2025, arXiv:2511.22888)\n- CRM (ICLR 2026, arXiv:2509.26578)\n- PURE (NeurIPS 2025, arXiv:2504.15275)\n- GenPRM (AAAI 2026, arXiv:2504.00891)\n- AgentEval (arXiv 2026, arXiv:2604.23581)\n- PRMBench (ACL 2025, arXiv:2501.03124)\n- ProcessBench (arXiv 2024, arXiv:2412.06559)\n- CPMI (arXiv 2026, arXiv:2604.10660)\n- RewardFlow (arXiv 2026, arXiv:2603.18859)\n- PathFinder-PRM (arXiv 2025, arXiv:2505.19706)\n- Thought-Path Contrastive Learning (AAAI 2025, arXiv:2409.14495)\n- ThinkPRM (arXiv 2025, arXiv:2504.16828)\n- CRV (ICLR 2026, arXiv:2510.09312)\n- R-PRM (arXiv 2025, arXiv:2503.21295)\n\n## Resource Estimate\n\n- **manual**: gpu_hours: 1500-2000 A100-hours (DAG extraction 72B model: ~300h, contrastive pair generation 7B/32B + quality verification 72B: ~200h, PRM training with 8 ablations: ~550h, 6-tier baseline reproduction/evaluation: ~150h, RL closed-loop × 3 seeds: ~250h, best-of-N + adversarial evaluation: ~80h), timeline: 16-22 weeks for 2-3 researchers, estimated_gpu_cost: $4,500-$6,000 at $3/hr A100 spot pricing\n- **human_in_loop**: gpu_hours: 1100-1500 A100-hours (Claude accelerates DAG quality validation, pair filtering, ablation prioritization; ~30% reduction in failed experiments), timeline: 12-16 weeks for 2 researchers, claude_api_cost: $800-$1,200, estimated_gpu_cost: $3,300-$4,500\n- **auto_research**: gpu_hours: 1600-2200 A100-hours (more parallel sweeps), timeline: 8-12 weeks automated, claude_api_cost: $1,500-$2,000, estimated_gpu_cost: $4,800-$6,600, speed_bottleneck: DAG extraction quality validation per math subdomain (algebra/geometry/combinatorics/number theory) requires serial human spot-checks"
}
```

---

### Runtime record

_source line 2 · 2026-05-27T08:42:36.121Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T08:42:36.121Z",
  "sessionId": "75462fa2-385d-4000-b649-57c64df02312"
}
```

---

## Round 1

46 recorded events

### User

_source line 3 · 2026-05-27T08:42:36.139Z_

# Premise-Graph Contrastive Training for Logic-Grounded Process Reward Models

## Core Problem

Current process reward models detect consistency rather than causality. "Reward Models Identify Consistency, Not Causality" (arXiv:2502.14619, Feb 2025) established that PRMs verify surface-level coherence between steps — not whether each step logically follows from its premises. "Reward Under Attack" (arXiv:2603.06621, Feb 2026) quantified the consequences: 43% of PRM reward gains are attributable to stylistic shortcuts, and RL-trained policies achieve >0.9 PRM scores but <4% actual accuracy. The root cause is that standard PRM training provides only point-wise step-correctness supervision, which is blind to the logical dependency structure connecting reasoning steps. Can we train PRMs whose representations explicitly encode premise-dependency awareness — sensitivity to which conclusions actually follow from which premises — rather than mere surface consistency?

## Research Opportunity and Key Insight

A critical representation-utilization gap exists in current PRMs. "From Chains to DAGs" (arXiv:2601.17593, Jan 2026) proved that LLM hidden states already linearly encode DAG reasoning structure — node depth, pairwise distance, and adjacency are recoverable from intermediate layers via lightweight probes. Yet "Reward Models Identify Consistency, Not Causality" (arXiv:2502.14619) showed that standard PRM training fails to channel this latent structural knowledge into reward prediction: PRMs remain insensitive to whether premise-conclusion links are logically valid. PARC/PERL (ICML 2025, arXiv:2502.02362) demonstrated that premise dependency links are extractable at >90% recall (on 70B+ models), and premise-aware verification improves error detection by 6-16%. DAG-Math (arXiv:2510.19842, 2025) and ProofFlow (arXiv:2510.15981, 2025) further established feasibility of dependency graph extraction from mathematical reasoning chains.

Our key insight: contrastive training anchored to premise dependency DAGs can bridge this representation-utilization gap. By constructing training pairs that hold surface form constant while varying logical structure (and vice versa), we force the PRM's embedding space to explicitly encode premise-dependency relationships — activating the structural representations the model already possesses but that point-wise BCE training leaves dormant. This constitutes a shift from point-wise supervision (each step independently correct/incorrect) to relational supervision (structural relationships between steps encoded in representation space).

## Research Landscape

**PRM robustness failures and existing defenses.** "Reward Under Attack" (arXiv:2603.06621) established a three-tier diagnostic: static perturbation exploitability, adversarial token-level attacks, and RL-induced reward hacking. Existing defenses span complementary strategies: CRA (Aug 2025, arXiv:2508.04216, post-hoc sparse autoencoder correction), APRM (Nov 2025, arXiv:2511.22888, adversarial training with harder negatives, +5.3pp OOD), CRM (ICLR 2026, arXiv:2509.26578, sequential conditioning on preceding steps), and PURE (NeurIPS 2025, arXiv:2504.15275, min-form credit aggregation). None uses explicit logical dependency structure during PRM training. APRM is the closest methodological comparator: its adversarial negatives improve the single-step classification decision boundary but remain domain-agnostic — the PRM learns to resist specific adversarial patterns without understanding why those patterns are wrong. PGCT instead reorganizes the PRM's representation space around premise-dependency topology, providing a semantically grounded and transferable capability rather than pattern-specific robustness.

**Reasoning-enhanced PRMs.** R-PRM (arXiv:2503.21295, 2025) augments PRMs with reasoning-driven critique, achieving +11.9 F1 on ProcessBench and +8.5 on PRMBench over same-data baselines. GenPRM (AAAI 2026, arXiv:2504.00891) employs generative CoT + code verification for step analysis, surpassing all same-scale discriminative PRMs. ThinkPRM (arXiv:2504.16828, 2025) demonstrates that generative verification with only 1% of PRM800K labels can outperform full-data discriminative PRMs. These approaches enhance verification through richer inference-time reasoning. PGCT is orthogonal: it improves training-time representation learning. PGCT-trained representations could potentially serve as improved backbones for generative verification methods.

**Graph structure for verification.** CRV (ICLR 2026, arXiv:2510.09312) uses attribution graph structural fingerprints to verify reasoning (white-box, inference-time). GoV decomposes reasoning into DAGs for training-free verification. AgentEval (arXiv:2604.23581, 2026) showed DAG-based dependency modeling yields +22pp failure detection recall. These independent lines confirm that graph structure carries powerful verification signal. PGCT is the first to inject this signal into PRM training objectives.

**Concurrent contrastive/graph approaches.** CPMI (arXiv:2604.10660, April 2026) uses contrastive mutual information for PRM auto-labeling without premise dependency graphs. RewardFlow (arXiv:2603.18859, March 2026) propagates rewards over state-transition graphs in agentic tasks without contrastive training. Thought-Path Contrastive Learning (AAAI 2025, arXiv:2409.14495) constructs premise-oriented contrastive examples for logical reading comprehension, but operates on propositional-level premise-conclusion pairs (not multi-step mathematical reasoning DAGs) and targets discriminative reading accuracy rather than PRM robustness.

**Performance gap.** The best open-source PRM on PRMBench scores 67.7 (PathFinder-PRM-7B, arXiv:2505.19706) vs. 83.8 human ceiling. The specific combination of premise dependency DAGs with contrastive PRM training remains untried.

## Proposed Approach

**DAG extraction.** Extract premise dependency DAGs from mathematical reasoning chains using PARC's extraction method with Qwen2.5-72B-Instruct (targeting >90% recall as demonstrated on 70B-class models in PERL, ICML 2025, arXiv:2502.02362). Each reasoning step is a node; directed edges encode "step j uses the result of step i as a premise."

**Contrastive pair construction.** Two types of structure-aware pairs: (1) Graph-preserving surface perturbations (rephrased steps, identical DAG topology) as positives; (2) Graph-breaking fluent perturbations (severed premise links, dangling references, logically invalid steps maintaining surface fluency) as hard negatives. Quality assurance pipeline: re-extract DAGs from generated pairs to verify topology preservation/breaking; stratified human audit (~1000 pairs across math subdomains × DAG complexity levels) with quality thresholds (topology preservation rate ≥90% for positives, premise-link corruption verification ≥85% for negatives) and inter-annotator agreement (2 annotators, Cohen's κ on ~200-pair overlap).

**Dual objective training.** Qwen2.5-Math-7B-Instruct-based PRM trained with: (a) standard step-correctness BCE loss (point-wise supervision), and (b) graph-contrastive InfoNCE loss over DAG-anchored step embeddings (relational supervision). The InfoNCE loss explicitly requires "same DAG topology → nearby embeddings, different topology → distant embeddings," forcing the representation space to reflect premise-dependency structure. This complements CRM (ICLR 2026, arXiv:2509.26578), which conditions predictions sequentially on preceding steps but operates in a point-wise prediction paradigm without encoding relational structure in embedding space.

**Important scope clarification.** PGCT trains two distinct but complementary capabilities: (1) structural dependency sensitivity — detecting whether premise links between steps are correctly maintained (directly via DAG topology contrastive learning), and (2) partial semantic inference validity — detecting logically invalid reasoning steps that preserve surface fluency (via graph-breaking hard negatives). We do not claim PGCT achieves full logical causality verification, but rather that premise-dependency awareness substantially narrows the consistency-causality gap that current PRMs exhibit.

**Data.** PRM800K + Math-Shepherd seed chains (~300K solutions) augmented with DAG annotations and ~600K contrastive pairs via LLM paraphrasing (7B/32B models for generation, 72B for quality verification) and targeted premise-link corruption.

## Evaluation Plan

**Benchmarks (4-tier, with ID/OOD split):**
1. **Step-level error detection**: PRMBench (ACL 2025, arXiv:2501.03124) with per-error-category breakdown (soundness/sensitivity/simplicity; redundancy, circular logic, step inconsistency, domain inconsistency, deceptive logical steps), targeting >70 overall (vs. 67.7 PathFinder-PRM SOTA) with disproportionate gains on logic-structure-related error types. ProcessBench (arXiv:2412.06559) with per-difficulty-level F1 (easy/medium/hard/competition).
2. **Downstream best-of-N reranking**: ID: MATH500, GSM8K; OOD: AIME 2024, AMC. N ∈ {8, 16, 64} candidates from Qwen2.5-Math-7B-Instruct. Report prm@N accuracy with ID vs. OOD breakdown.
3. **Adversarial robustness**: PRM-BiasBench and perturbation suite from "Reward Under Attack" (arXiv:2603.06621).
4. **RL closed-loop reward hacking**: GRPO training of Qwen2.5-Math-7B-Instruct policy using PGCT-PRM vs. baseline PRMs as reward signal. 3000-5000 GRPO steps, checkpoint every 200 steps, evaluate on MATH and AIME. Metrics: (a) hacking gap = (PRM score improvement) − (ground-truth accuracy improvement) over training; (b) reward-accuracy Pearson correlation with 95% CI from 3 random seeds; (c) late-stage divergence ratio (reward growth / accuracy growth in final 30% of training).

**Baselines (6 tiers):**
1. Standard PRM: Qwen2.5-Math-PRM-7B (same base model)
2. Robustness-focused: APRM (arXiv:2511.22888), CRA (arXiv:2508.04216)
3. Architecture-level: CRM (ICLR 2026, arXiv:2509.26578), PURE (NeurIPS 2025, arXiv:2504.15275)
4. Contrastive/concurrent: CPMI (arXiv:2604.10660)
5. Error-aware: PathFinder-PRM-7B (arXiv:2505.19706)
6. Reasoning-enhanced: R-PRM (arXiv:2503.21295), GenPRM-7B (AAAI 2026, arXiv:2504.00891, fixed-compute, no test-time scaling)
- Data-matched control: ~900K total samples, contrastive pairs replaced with additional step-correctness annotations, standard BCE
- Compute-matched control: equal total training FLOPs including DAG extraction overhead

**Ablations (8 variants):**
- A1: Remove InfoNCE loss → isolate contrastive learning contribution
- A2: Remove step-correctness loss → test contrastive learning standalone
- A3: Random perturbation replacing DAG-aware perturbation → **critical: isolate DAG structure contribution**
- A4: Only positives (no graph-breaking negatives) → isolate hard negative contribution
- A5: Only negatives (no graph-preserving positives) → isolate surface-invariance contribution
- A6: Loss weighting λ ∈ {0.1, 0.3, 0.5, 0.7, 1.0}
- A7: DAG noise injection at 5%/10%/15%/20% → robustness to extraction errors
- A8: DAG extraction model scale: 7B / 32B / 72B extractors → practical viability curve

## Key References

- Reward Under Attack (arXiv 2026, arXiv:2603.06621)
- Reward Models Identify Consistency, Not Causality (arXiv 2025, arXiv:2502.14619)
- PARC/PERL (ICML 2025, arXiv:2502.02362)
- From Chains to DAGs (arXiv 2026, arXiv:2601.17593)
- DAG-Math (arXiv 2025, arXiv:2510.19842)
- ProofFlow (arXiv 2025, arXiv:2510.15981)
- CRA (arXiv 2025, arXiv:2508.04216)
- APRM (arXiv 2025, arXiv:2511.22888)
- CRM (ICLR 2026, arXiv:2509.26578)
- PURE (NeurIPS 2025, arXiv:2504.15275)
- GenPRM (AAAI 2026, arXiv:2504.00891)
- AgentEval (arXiv 2026, arXiv:2604.23581)
- PRMBench (ACL 2025, arXiv:2501.03124)
- ProcessBench (arXiv 2024, arXiv:2412.06559)
- CPMI (arXiv 2026, arXiv:2604.10660)
- RewardFlow (arXiv 2026, arXiv:2603.18859)
- PathFinder-PRM (arXiv 2025, arXiv:2505.19706)
- Thought-Path Contrastive Learning (AAAI 2025, arXiv:2409.14495)
- ThinkPRM (arXiv 2025, arXiv:2504.16828)
- CRV (ICLR 2026, arXiv:2510.09312)
- R-PRM (arXiv 2025, arXiv:2503.21295)

## Resource Estimate

- **manual**: gpu_hours: 1500-2000 A100-hours (DAG extraction 72B model: ~300h, contrastive pair generation 7B/32B + quality verification 72B: ~200h, PRM training with 8 ablations: ~550h, 6-tier baseline reproduction/evaluation: ~150h, RL closed-loop × 3 seeds: ~250h, best-of-N + adversarial evaluation: ~80h), timeline: 16-22 weeks for 2-3 researchers, estimated_gpu_cost: $4,500-$6,000 at $3/hr A100 spot pricing
- **human_in_loop**: gpu_hours: 1100-1500 A100-hours (Claude accelerates DAG quality validation, pair filtering, ablation prioritization; ~30% reduction in failed experiments), timeline: 12-16 weeks for 2 researchers, claude_api_cost: $800-$1,200, estimated_gpu_cost: $3,300-$4,500
- **auto_research**: gpu_hours: 1600-2200 A100-hours (more parallel sweeps), timeline: 8-12 weeks automated, claude_api_cost: $1,500-$2,000, estimated_gpu_cost: $4,800-$6,600, speed_bottleneck: DAG extraction quality validation per math subdomain (algebra/geometry/combinatorics/number theory) requires serial human spot-checks

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "18914ca9-b0a2-4983-9544-756340563499",
  "type": "user",
  "uuid": "eefad366-8361-4547-a60d-9c73e78dd068",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "75462fa2-385d-4000-b649-57c64df02312",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-27T08:42:36.137Z_

```json
{
  "parentUuid": "eefad366-8361-4547-a60d-9c73e78dd068",
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
  "uuid": "749157b7-5953-43a7-97c3-8127ba6efe1f",
  "timestamp": "2026-05-27T08:42:36.137Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "75462fa2-385d-4000-b649-57c64df02312",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-27T08:42:36.137Z_

```json
{
  "parentUuid": "749157b7-5953-43a7-97c3-8127ba6efe1f",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "a124230a-5308-49d3-a6e2-1083949c0887",
  "timestamp": "2026-05-27T08:42:36.137Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "75462fa2-385d-4000-b649-57c64df02312",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "ai-title",
  "aiTitle": "Premise-Graph contrastive training for process reward models",
  "sessionId": "75462fa2-385d-4000-b649-57c64df02312"
}
```

---

### Assistant

_source line 7 · 2026-05-27T08:42:40.430Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze this proposal carefully. It's about "Premise-Graph Contrastive Training for Logic-Grounded Process Reward Models" (PGCT). I need to first do thorough literature research before making any assessments.

Let me start by searching for the most relevant recent works mentioned in the proposal and related areas to understand the current landscape.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a124230a-5308-49d3-a6e2-1083949c0887",
  "isSidechain": false,
  "requestId": "req_011CbSn1FH4WwCv4oCejdZNX",
  "type": "assistant",
  "uuid": "e1a9e27d-5631-4072-a365-bd2f1e1ed401",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "75462fa2-385d-4000-b649-57c64df02312",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017hDaakVWGzR5BfKZ1pX8vf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5251,
      "cache_read_input_tokens": 14184,
      "output_tokens": 196,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5251,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 196,
          "cache_read_input_tokens": 14184,
          "cache_creation_input_tokens": 5251,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5251
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

_source line 8 · 2026-05-27T08:42:40.954Z_

I need to do thorough literature research before making any assessments. Let me search for the key papers and recent developments in this space.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1a9e27d-5631-4072-a365-bd2f1e1ed401",
  "isSidechain": false,
  "requestId": "req_011CbSn1FH4WwCv4oCejdZNX",
  "type": "assistant",
  "uuid": "be6ca519-5366-47a8-937a-6eb9dabcb210",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "75462fa2-385d-4000-b649-57c64df02312",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017hDaakVWGzR5BfKZ1pX8vf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5251,
      "cache_read_input_tokens": 14184,
      "output_tokens": 196,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5251,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 196,
          "cache_read_input_tokens": 14184,
          "cache_creation_input_tokens": 5251,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5251
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

_source line 9 · 2026-05-27T08:42:41.293Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01KikSWQqs7CngkUBMXs5G6C`</summary>

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
  "parentUuid": "be6ca519-5366-47a8-937a-6eb9dabcb210",
  "isSidechain": false,
  "requestId": "req_011CbSn1FH4WwCv4oCejdZNX",
  "type": "assistant",
  "uuid": "c38a1bfe-11db-4dde-ae97-2ccbad025fe3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "75462fa2-385d-4000-b649-57c64df02312",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017hDaakVWGzR5BfKZ1pX8vf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5251,
      "cache_read_input_tokens": 14184,
      "output_tokens": 196,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5251,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 196,
          "cache_read_input_tokens": 14184,
          "cache_creation_input_tokens": 5251,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5251
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

_source line 10 · 2026-05-27T08:42:41.302Z_

<details><summary>↩ Tool result · `toolu_01KikSWQqs7CngkUBMXs5G6C`</summary>

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
  "parentUuid": "c38a1bfe-11db-4dde-ae97-2ccbad025fe3",
  "isSidechain": false,
  "promptId": "18914ca9-b0a2-4983-9544-756340563499",
  "type": "user",
  "uuid": "f8cac0f6-ddf4-4c82-9f16-bd1777cf991b",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "c38a1bfe-11db-4dde-ae97-2ccbad025fe3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "75462fa2-385d-4000-b649-57c64df02312",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 11_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Premise-Graph Contrastive Training for Logic-Grounded Process Reward Models  ## Core Problem  Current process reward models detect consistency rather than causality. \"Reward Models Identify Consiste…",
  "leafUuid": "f8cac0f6-ddf4-4c82-9f16-bd1777cf991b",
  "sessionId": "75462fa2-385d-4000-b649-57c64df02312"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Premise-Graph contrastive training for process reward models",
  "sessionId": "75462fa2-385d-4000-b649-57c64df02312"
}
```

---

### Assistant

_source line 13 · 2026-05-27T08:42:44.358Z_

Now let me conduct my front-loaded literature research with multiple parallel searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8cac0f6-ddf4-4c82-9f16-bd1777cf991b",
  "isSidechain": false,
  "requestId": "req_011CbSn1dEAVp4vP591wVTaf",
  "type": "assistant",
  "uuid": "6510ebef-8d79-4b88-a3e2-bb55b6b101e8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "75462fa2-385d-4000-b649-57c64df02312",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017oXdoBw7hJXmvGRFVzp5Z5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 724,
      "cache_read_input_tokens": 19435,
      "output_tokens": 84,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 724,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 84,
          "cache_read_input_tokens": 19435,
          "cache_creation_input_tokens": 724,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 724
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

_source line 14 · 2026-05-27T08:42:44.541Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017yekUtCZtLwrnxVBETUEab`</summary>

```json
{
  "query": "process reward model robustness contrastive training 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6510ebef-8d79-4b88-a3e2-bb55b6b101e8",
  "isSidechain": false,
  "requestId": "req_011CbSn1dEAVp4vP591wVTaf",
  "type": "assistant",
  "uuid": "e8cad2e3-6018-424d-95f7-710938fa758e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "75462fa2-385d-4000-b649-57c64df02312",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017oXdoBw7hJXmvGRFVzp5Z5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 724,
      "cache_read_input_tokens": 19435,
      "output_tokens": 84,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 724,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 84,
          "cache_read_input_tokens": 19435,
          "cache_creation_input_tokens": 724,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 724
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

_source line 15 · 2026-05-27T08:42:51.803Z_

<details><summary>↩ Tool result · `toolu_017yekUtCZtLwrnxVBETUEab`</summary>

```text
Web search results for query: "process reward model robustness contrastive training 2025 2026"

Links: [{"title":"Reward-Conditioned Alignment Methods","url":"https://www.emergentmind.com/topics/reward-conditioned-alignment"},{"title":"Adversarial Training for Process Reward Models","url":"https://arxiv.org/pdf/2511.22888"},{"title":"DC-W2S: Dual-Consensus Weak-to-Strong Training for Reliable Process Reward Modeling in Biological Reasoning","url":"https://arxiv.org/pdf/2603.08095"},{"title":"Towards Robust Process Reward Modeling via Noise-aware Learning","url":"https://arxiv.org/pdf/2601.12748"},{"title":"Reward Models Can Improve Themselves: Reward-Guided Adversarial Failure Mode Discovery for Robust Reward Modeling","url":"https://arxiv.org/pdf/2507.06419"},{"title":"CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR","url":"https://arxiv.org/pdf/2603.10101"},{"title":"Improving Reinforcement Learning from Human Feedback Using Contrastive   Rewards","url":"https://arxiv.org/pdf/2403.07708"}]

I found several relevant results about process reward models, robustness, and contrastive training from 2025-2026. Here's what the search revealed:

## Energy-Based Reward Models with Contrastive Training

Energy-Based Reward Models (EBRM) refine reward signals post-hoc via an energy head, capturing uncertainty and mitigating label noise, requiring only batch-level inference and contrastive training (Lochab et al., 17 Apr 2025).

## Adversarial Training for Process Reward Model Robustness

Recent work has focused on improving PRM robustness through adversarial approaches. Process Reward Models (PRMs) are needed for identifying very subtle errors, and current PRM training techniques predominantly rely on static datasets, which are inherently limited as they provide a fixed error distribution that cannot adapt to more nuanced errors.

## Contrastive Learning in Policy Optimization

A series of recent works have explored process reward models (PRMs) that provide finer-grained supervision by identifying errors during the reasoning process. Additionally, contrastive rewards enable the LLM to penalize reward uncertainty, improve robustness, encourage improvement over baselines, calibrate according to task difficulty, and reduce variance in PPO.

## Other Robustness Approaches

Process reward models address issues by providing step-by-step feedback, a technique that has been proven to be highly effective for complex reasoning tasks.

The search results show active research in 2025-2026 on making PRMs more robust through contrastive training, adversarial methods, and noise-aware learning approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e8cad2e3-6018-424d-95f7-710938fa758e",
  "isSidechain": false,
  "promptId": "18914ca9-b0a2-4983-9544-756340563499",
  "type": "user",
  "uuid": "7be8ce7a-7c08-45d4-948e-7a6b815a57ba",
  "toolUseResult": {
    "query": "process reward model robustness contrastive training 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_013tXHbPAmY8igaDowqJF1bv",
        "content": [
          {
            "title": "Reward-Conditioned Alignment Methods",
            "url": "https://www.emergentmind.com/topics/reward-conditioned-alignment"
          },
          {
            "title": "Adversarial Training for Process Reward Models",
            "url": "https://arxiv.org/pdf/2511.22888"
          },
          {
            "title": "DC-W2S: Dual-Consensus Weak-to-Strong Training for Reliable Process Reward Modeling in Biological Reasoning",
            "url": "https://arxiv.org/pdf/2603.08095"
          },
          {
            "title": "Towards Robust Process Reward Modeling via Noise-aware Learning",
            "url": "https://arxiv.org/pdf/2601.12748"
          },
          {
            "title": "Reward Models Can Improve Themselves: Reward-Guided Adversarial Failure Mode Discovery for Robust Reward Modeling",
            "url": "https://arxiv.org/pdf/2507.06419"
          },
          {
            "title": "CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR",
            "url": "https://arxiv.org/pdf/2603.10101"
          },
          {
            "title": "Improving Reinforcement Learning from Human Feedback Using Contrastive   Rewards",
            "url": "https://arxiv.org/pdf/2403.07708"
          }
        ]
      },
      "I found several relevant results about process reward models, robustness, and contrastive training from 2025-2026. Here's what the search revealed:\n\n## Energy-Based Reward Models with Contrastive Training\n\nEnergy-Based Reward Models (EBRM) refine reward signals post-hoc via an energy head, capturing uncertainty and mitigating label noise, requiring only batch-level inference and contrastive training (Lochab et al., 17 Apr 2025).\n\n## Adversarial Training for Process Reward Model Robustness\n\nRecent work has focused on improving PRM robustness through adversarial approaches. Process Reward Models (PRMs) are needed for identifying very subtle errors, and current PRM training techniques predominantly rely on static datasets, which are inherently limited as they provide a fixed error distribution that cannot adapt to more nuanced errors.\n\n## Contrastive Learning in Policy Optimization\n\nA series of recent works have explored process reward models (PRMs) that provide finer-grained supervision by identifying errors during the reasoning process. Additionally, contrastive rewards enable the LLM to penalize reward uncertainty, improve robustness, encourage improvement over baselines, calibrate according to task difficulty, and reduce variance in PPO.\n\n## Other Robustness Approaches\n\nProcess reward models address issues by providing step-by-step feedback, a technique that has been proven to be highly effective for complex reasoning tasks.\n\nThe search results show active research in 2025-2026 on making PRMs more robust through contrastive training, adversarial methods, and noise-aware learning approaches."
    ],
    "durationSeconds": 7.256990052000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e8cad2e3-6018-424d-95f7-710938fa758e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "75462fa2-385d-4000-b649-57c64df02312",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-27T08:43:01.846Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01S7pn43WkY4R1cva4ief37U`</summary>

```json
{
  "query": "premise dependency graph reasoning verification DAG structure LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7be8ce7a-7c08-45d4-948e-7a6b815a57ba",
  "isSidechain": false,
  "requestId": "req_011CbSn2mKcRhTEQnBcX9fE6",
  "type": "assistant",
  "uuid": "72448fd0-ba20-47fe-9f0d-8b171dc64e6d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "75462fa2-385d-4000-b649-57c64df02312",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UCsCgwDcLiHC9TKkYSpy3W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 788,
      "cache_read_input_tokens": 20159,
      "output_tokens": 68,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 788,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 68,
          "cache_read_input_tokens": 20159,
          "cache_creation_input_tokens": 788,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 788
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

_source line 17 · 2026-05-27T08:43:10.213Z_

<details><summary>↩ Tool result · `toolu_01S7pn43WkY4R1cva4ief37U`</summary>

```text
Web search results for query: "premise dependency graph reasoning verification DAG structure LLM 2025 2026"

Links: [{"title":"Graph of Verification: Structured Verification of LLM Reasoning","url":"https://arxiv.org/pdf/2506.12509"},{"title":"[2601.17593] From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs","url":"https://arxiv.org/abs/2601.17593"},{"title":"Graph of Verification: Structured Verification of LLM Reasoning with Directed Acyclic Graphs","url":"https://arxiv.org/html/2506.12509v3"},{"title":"From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs","url":"https://arxiv.org/pdf/2601.17593"},{"title":"From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs","url":"https://arxiv.org/html/2601.17593"},{"title":"Reasoning Circuits in LLMs","url":"https://www.emergentmind.com/topics/reasoning-circuits-in-llms"},{"title":"[2506.12509] Graph of Verification: Structured Verification of LLM Reasoning with Directed Acyclic Graphs","url":"https://arxiv.org/abs/2506.12509"},{"title":"DAG-Math: Graph-of-Thought Guided Mathematical Reasoning in LLMs","url":"https://arxiv.org/html/2510.19842"},{"title":"DAG-Math: Graph-Guided Mathematical Reasoning in LLMs","url":"https://arxiv.org/html/2510.19842v1"}]

I found several highly relevant research papers on premise dependency graphs and DAG-structured reasoning verification in LLMs from 2025-2026. Here are the key findings:

## Recent Work on Reasoning Graphs and Verification

A Directed Acyclic Graph (DAG) structure enforces causal consistency ensuring premises are verified before conclusions, followed by sequential verification where an LLM assesses each unit based on previously validated antecedents.

### Graph of Verification Framework

The GoV framework models any reasoning process as a Directed Acyclic Graph (DAG), and the acyclic property of the DAG guarantees well-founded reasoning by removing circular dependencies, thus preventing situations where the validity of a statement relies on itself.

### Probing LLM Internal Graph Structure

DAG structure is meaningfully encoded in LLM representations, with recoverability peaking in intermediate layers, varying systematically by node depth, edge span, and model scale, and enabling nontrivial recovery of dependency graphs. While chain-of-thought linearizes reasoning, real reasoning often has graph structure where multiple premises can jointly support an intermediate conclusion, intermediate results can be reused, and derivations can branch and later merge—properties naturally captured by directed acyclic graphs.

### Graph-of-Thought Mathematical Reasoning

Recent work formalizes Chain-of-Thought as a rule-based stochastic process on directed acyclic graphs (DAGs), providing a principled framework for modeling and evaluating LLM mathematical reasoning.

These papers represent the cutting edge of research connecting premise dependencies, DAG structures, and structured verification of LLM reasoning in 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "72448fd0-ba20-47fe-9f0d-8b171dc64e6d",
  "isSidechain": false,
  "promptId": "18914ca9-b0a2-4983-9544-756340563499",
  "type": "user",
  "uuid": "146c82a9-ce88-4ec0-b55a-1d83a543309a",
  "toolUseResult": {
    "query": "premise dependency graph reasoning verification DAG structure LLM 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01X11y5S3aA2BeV9Db9HsGT4",
        "content": [
          {
            "title": "Graph of Verification: Structured Verification of LLM Reasoning",
            "url": "https://arxiv.org/pdf/2506.12509"
          },
          {
            "title": "[2601.17593] From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs",
            "url": "https://arxiv.org/abs/2601.17593"
          },
          {
            "title": "Graph of Verification: Structured Verification of LLM Reasoning with Directed Acyclic Graphs",
            "url": "https://arxiv.org/html/2506.12509v3"
          },
          {
            "title": "From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs",
            "url": "https://arxiv.org/pdf/2601.17593"
          },
          {
            "title": "From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs",
            "url": "https://arxiv.org/html/2601.17593"
          },
          {
            "title": "Reasoning Circuits in LLMs",
            "url": "https://www.emergentmind.com/topics/reasoning-circuits-in-llms"
          },
          {
            "title": "[2506.12509] Graph of Verification: Structured Verification of LLM Reasoning with Directed Acyclic Graphs",
            "url": "https://arxiv.org/abs/2506.12509"
          },
          {
            "title": "DAG-Math: Graph-of-Thought Guided Mathematical Reasoning in LLMs",
            "url": "https://arxiv.org/html/2510.19842"
          },
          {
            "title": "DAG-Math: Graph-Guided Mathematical Reasoning in LLMs",
            "url": "https://arxiv.org/html/2510.19842v1"
          }
        ]
      },
      "I found several highly relevant research papers on premise dependency graphs and DAG-structured reasoning verification in LLMs from 2025-2026. Here are the key findings:\n\n## Recent Work on Reasoning Graphs and Verification\n\nA Directed Acyclic Graph (DAG) structure enforces causal consistency ensuring premises are verified before conclusions, followed by sequential verification where an LLM assesses each unit based on previously validated antecedents.\n\n### Graph of Verification Framework\n\nThe GoV framework models any reasoning process as a Directed Acyclic Graph (DAG), and the acyclic property of the DAG guarantees well-founded reasoning by removing circular dependencies, thus preventing situations where the validity of a statement relies on itself.\n\n### Probing LLM Internal Graph Structure\n\nDAG structure is meaningfully encoded in LLM representations, with recoverability peaking in intermediate layers, varying systematically by node depth, edge span, and model scale, and enabling nontrivial recovery of dependency graphs. While chain-of-thought linearizes reasoning, real reasoning often has graph structure where multiple premises can jointly support an intermediate conclusion, intermediate results can be reused, and derivations can branch and later merge—properties naturally captured by directed acyclic graphs.\n\n### Graph-of-Thought Mathematical Reasoning\n\nRecent work formalizes Chain-of-Thought as a rule-based stochastic process on directed acyclic graphs (DAGs), providing a principled framework for modeling and evaluating LLM mathematical reasoning.\n\nThese papers represent the cutting edge of research connecting premise dependencies, DAG structures, and structured verification of LLM reasoning in 2025-2026."
    ],
    "durationSeconds": 8.361970888999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "72448fd0-ba20-47fe-9f0d-8b171dc64e6d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "75462fa2-385d-4000-b649-57c64df02312",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-27T08:43:13.068Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FuJRyd79Hjtut7kn4oixXi`</summary>

```json
{
  "query": "\"reward model\" \"reward hacking\" causal structure logical dependency training 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "146c82a9-ce88-4ec0-b55a-1d83a543309a",
  "isSidechain": false,
  "requestId": "req_011CbSn3kXGZs1mPfYEm9X7W",
  "type": "assistant",
  "uuid": "5caa8b3d-33c5-4da9-912c-402b035876a2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "75462fa2-385d-4000-b649-57c64df02312",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01824QF85QzBudhrNubFhqdJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 875,
      "cache_read_input_tokens": 20947,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 875,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 20947,
          "cache_creation_input_tokens": 875,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 875
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

_source line 19 · 2026-05-27T08:43:21.240Z_

<details><summary>↩ Tool result · `toolu_01FuJRyd79Hjtut7kn4oixXi`</summary>

```text
Web search results for query: ""reward model" "reward hacking" causal structure logical dependency training 2025 2026 arxiv"

Links: [{"title":"Factored Causal Representation Learning for Robust Reward Modeling in RLHF","url":"https://arxiv.org/pdf/2601.21350"},{"title":"[2506.16507] Robust Reward Modeling via Causal Rubrics","url":"https://arxiv.org/abs/2506.16507"},{"title":"[2508.02618] Alleviating Attention Hacking in Discriminative Reward Modeling through Interaction Distillation","url":"https://arxiv.org/abs/2508.02618"},{"title":"Robust Reward Modeling via Causal Rubrics","url":"https://arxiv.org/pdf/2506.16507"},{"title":"[2501.09620] Beyond Reward Hacking: Causal Rewards for Large Language Model Alignment","url":"https://arxiv.org/abs/2501.09620"},{"title":"Causal Rewards for Large Language Model Alignment","url":"https://arxiv.org/pdf/2501.09620"},{"title":"[2506.19248] Inference-Time Reward Hacking in Large Language Models","url":"https://arxiv.org/abs/2506.19248"},{"title":"Mitigating Reward Hacking in RLHF via Bayesian Non-negative Reward Modeling","url":"https://arxiv.org/pdf/2602.10623"}]

Based on the search results, here are several recent arXiv papers (2025-2026) addressing reward modeling, reward hacking, and causal structures:

## Key Papers Found:

1. **"Factored Causal Representation Learning for Robust Reward Modeling in RLHF"** (January 2026)
   - Introduces an adversarial head trained to predict reward from non-causal factors while applying gradient reversal, with analyses validating effectiveness in mitigating reward hacking behaviors.

2. **"Robust Reward Modeling via Causal Rubrics"** (June 2025 - Crome)
   - Introduces Crome (Causally Robust Reward Modeling), a framework grounded in an explicit causal model designed to mitigate reward hacking. RMs often learn to assign high scores based on superficial attributes like response length or formatting because standard training objectives do not explicitly require disentangling true causal drivers of quality from spurious correlates.

3. **"Beyond Reward Hacking: Causal Rewards for Large Language Model Alignment"** (January 2025, updated May 2025)
   - Addresses how reward hacking occurs when RL agents exploit flaws or ambiguities in the reward function to maximize rewards without genuinely improving alignment with desired behaviors.

4. **"Alleviating Attention Hacking in Discriminative Reward Modeling through Interaction Distillation"** (August 2025, updated January 2026)
   - Proposes "Interaction Distillation", a training framework for more adequate discriminative reward modeling via attention-level optimization.

5. **"Mitigating Reward Hacking in RLHF via Bayesian Non-negative Reward Modeling"** (February 2026)
   - Demonstrates that BNRM substantially mitigates reward over-optimization, improves robustness under distribution shifts, and yields more interpretable reward decompositions.

These papers collectively address the logical dependencies and causal structures underlying reward hacking through various technical approaches including causal representation learning, counterfactual augmentation, and Bayesian methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5caa8b3d-33c5-4da9-912c-402b035876a2",
  "isSidechain": false,
  "promptId": "18914ca9-b0a2-4983-9544-756340563499",
  "type": "user",
  "uuid": "9d768370-63b8-4f6b-b05b-9268fb7d83b8",
  "toolUseResult": {
    "query": "\"reward model\" \"reward hacking\" causal structure logical dependency training 2025 2026 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_019192EByDd9fUdb5Yf9c2eX",
        "content": [
          {
            "title": "Factored Causal Representation Learning for Robust Reward Modeling in RLHF",
            "url": "https://arxiv.org/pdf/2601.21350"
          },
          {
            "title": "[2506.16507] Robust Reward Modeling via Causal Rubrics",
            "url": "https://arxiv.org/abs/2506.16507"
          },
          {
            "title": "[2508.02618] Alleviating Attention Hacking in Discriminative Reward Modeling through Interaction Distillation",
            "url": "https://arxiv.org/abs/2508.02618"
          },
          {
            "title": "Robust Reward Modeling via Causal Rubrics",
            "url": "https://arxiv.org/pdf/2506.16507"
          },
          {
            "title": "[2501.09620] Beyond Reward Hacking: Causal Rewards for Large Language Model Alignment",
            "url": "https://arxiv.org/abs/2501.09620"
          },
          {
            "title": "Causal Rewards for Large Language Model Alignment",
            "url": "https://arxiv.org/pdf/2501.09620"
          },
          {
            "title": "[2506.19248] Inference-Time Reward Hacking in Large Language Models",
            "url": "https://arxiv.org/abs/2506.19248"
          },
          {
            "title": "Mitigating Reward Hacking in RLHF via Bayesian Non-negative Reward Modeling",
            "url": "https://arxiv.org/pdf/2602.10623"
          }
        ]
      },
      "Based on the search results, here are several recent arXiv papers (2025-2026) addressing reward modeling, reward hacking, and causal structures:\n\n## Key Papers Found:\n\n1. **\"Factored Causal Representation Learning for Robust Reward Modeling in RLHF\"** (January 2026)\n   - Introduces an adversarial head trained to predict reward from non-causal factors while applying gradient reversal, with analyses validating effectiveness in mitigating reward hacking behaviors.\n\n2. **\"Robust Reward Modeling via Causal Rubrics\"** (June 2025 - Crome)\n   - Introduces Crome (Causally Robust Reward Modeling), a framework grounded in an explicit causal model designed to mitigate reward hacking. RMs often learn to assign high scores based on superficial attributes like response length or formatting because standard training objectives do not explicitly require disentangling true causal drivers of quality from spurious correlates.\n\n3. **\"Beyond Reward Hacking: Causal Rewards for Large Language Model Alignment\"** (January 2025, updated May 2025)\n   - Addresses how reward hacking occurs when RL agents exploit flaws or ambiguities in the reward function to maximize rewards without genuinely improving alignment with desired behaviors.\n\n4. **\"Alleviating Attention Hacking in Discriminative Reward Modeling through Interaction Distillation\"** (August 2025, updated January 2026)\n   - Proposes \"Interaction Distillation\", a training framework for more adequate discriminative reward modeling via attention-level optimization.\n\n5. **\"Mitigating Reward Hacking in RLHF via Bayesian Non-negative Reward Modeling\"** (February 2026)\n   - Demonstrates that BNRM substantially mitigates reward over-optimization, improves robustness under distribution shifts, and yields more interpretable reward decompositions.\n\nThese papers collectively address the logical dependencies and causal structures underlying reward hacking through various technical approaches including causal representation learning, counterfactual augmentation, and Bayesian methods."
    ],
    "durationSeconds": 8.168841328000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "5caa8b3d-33c5-4da9-912c-402b035876a2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "75462fa2-385d-4000-b649-57c64df02312",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-27T08:43:25.821Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XT8NPEbUArS2ycxvnRamfQ`</summary>

```json
{
  "query": "CPMI contrastive mutual information PRM auto-labeling 2026 arXiv:2604.10660"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d768370-63b8-4f6b-b05b-9268fb7d83b8",
  "isSidechain": false,
  "requestId": "req_011CbSn4ZosZGnYLfuczcKAJ",
  "type": "assistant",
  "uuid": "bd069658-0916-4150-b585-78a3969257cf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "75462fa2-385d-4000-b649-57c64df02312",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HNUYq4FPuczaapK3dAK2XA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 971,
      "cache_read_input_tokens": 21822,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 971,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 78,
          "cache_read_input_tokens": 21822,
          "cache_creation_input_tokens": 971,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 971
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

_source line 21 · 2026-05-27T08:43:32.124Z_

<details><summary>↩ Tool result · `toolu_01XT8NPEbUArS2ycxvnRamfQ`</summary>

```text
Web search results for query: "CPMI contrastive mutual information PRM auto-labeling 2026 arXiv:2604.10660"

Links: [{"title":"[2604.10660] Efficient Process Reward Modeling via Contrastive Mutual Information","url":"https://arxiv.org/abs/2604.10660"},{"title":"Efficient Process Reward Modeling via Contrastive Mutual Information","url":"https://arxiv.org/html/2604.10660"},{"title":"Self-Supervised Contrastive Learning of Protein Representations By Mutual Information Maximization","url":"https://www.biorxiv.org/content/10.1101/2020.09.04.283929.full.pdf"},{"title":"On Mutual Information in Contrastive Learning for Visual Representations","url":"https://arxiv.org/pdf/2005.13149"},{"title":"Contrastive MIM: A Contrastive Mutual Information Framework for Unified Generative and Discriminative Representation Learning","url":"https://arxiv.org/html/2411.10548v4"},{"title":"Contrastive Mutual Information Learning: Toward Robust Representations without Positive-Pair Augmentations","url":"https://arxiv.org/pdf/2509.21511"}]

Based on the search results, here's what I found about arXiv:2604.10660:

## Efficient Process Reward Modeling via Contrastive Mutual Information

The paper proposes contrastive pointwise mutual information (CPMI), a novel automatic reward labeling method that leverages the model's internal probability to infer step-level supervision while significantly reducing the computational burden of annotating dataset.

**Key Problem Addressed:**
Training a PRM typically requires human annotators to assign reward scores to each reasoning step, which is both costly and time-consuming, and existing automated approaches like Monte Carlo estimation demand substantial computational resources due to repeated LLM rollouts.

**How CPMI Works:**
CPMI quantifies how much a reasoning step increases the mutual information between the step and the correct target answer relative to hard-negative alternatives.

**Key Results:**
CPMI-based labeling reduces dataset construction time by 84% and token generation by 98% compared to MC estimation, while achieving higher accuracy on process-level evaluations and mathematical reasoning benchmarks.

The paper was submitted on April 12, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd069658-0916-4150-b585-78a3969257cf",
  "isSidechain": false,
  "promptId": "18914ca9-b0a2-4983-9544-756340563499",
  "type": "user",
  "uuid": "5c683ccf-8804-4ac6-9ce7-1ca941db4857",
  "toolUseResult": {
    "query": "CPMI contrastive mutual information PRM auto-labeling 2026 arXiv:2604.10660",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NmBuANBJkDQWAs7c4EEWfi",
        "content": [
          {
            "title": "[2604.10660] Efficient Process Reward Modeling via Contrastive Mutual Information",
            "url": "https://arxiv.org/abs/2604.10660"
          },
          {
            "title": "Efficient Process Reward Modeling via Contrastive Mutual Information",
            "url": "https://arxiv.org/html/2604.10660"
          },
          {
            "title": "Self-Supervised Contrastive Learning of Protein Representations By Mutual Information Maximization",
            "url": "https://www.biorxiv.org/content/10.1101/2020.09.04.283929.full.pdf"
          },
          {
            "title": "On Mutual Information in Contrastive Learning for Visual Representations",
            "url": "https://arxiv.org/pdf/2005.13149"
          },
          {
            "title": "Contrastive MIM: A Contrastive Mutual Information Framework for Unified Generative and Discriminative Representation Learning",
            "url": "https://arxiv.org/html/2411.10548v4"
          },
          {
            "title": "Contrastive Mutual Information Learning: Toward Robust Representations without Positive-Pair Augmentations",
            "url": "https://arxiv.org/pdf/2509.21511"
          }
        ]
      },
      "Based on the search results, here's what I found about arXiv:2604.10660:\n\n## Efficient Process Reward Modeling via Contrastive Mutual Information\n\nThe paper proposes contrastive pointwise mutual information (CPMI), a novel automatic reward labeling method that leverages the model's internal probability to infer step-level supervision while significantly reducing the computational burden of annotating dataset.\n\n**Key Problem Addressed:**\nTraining a PRM typically requires human annotators to assign reward scores to each reasoning step, which is both costly and time-consuming, and existing automated approaches like Monte Carlo estimation demand substantial computational resources due to repeated LLM rollouts.\n\n**How CPMI Works:**\nCPMI quantifies how much a reasoning step increases the mutual information between the step and the correct target answer relative to hard-negative alternatives.\n\n**Key Results:**\nCPMI-based labeling reduces dataset construction time by 84% and token generation by 98% compared to MC estimation, while achieving higher accuracy on process-level evaluations and mathematical reasoning benchmarks.\n\nThe paper was submitted on April 12, 2026."
    ],
    "durationSeconds": 6.2958696560000025,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "bd069658-0916-4150-b585-78a3969257cf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "75462fa2-385d-4000-b649-57c64df02312",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-27T08:43:34.772Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01N4JwYXuwx4qhk2SgjKD5uY`</summary>

```json
{
  "query": "Graph of Verification GoV DAG reasoning verification arXiv:2506.12509 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c683ccf-8804-4ac6-9ce7-1ca941db4857",
  "isSidechain": false,
  "requestId": "req_011CbSn5NC9Zn1KKQfw5A8zA",
  "type": "assistant",
  "uuid": "eaf50b3a-4233-4587-b5ca-c8721eca0a34",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "75462fa2-385d-4000-b649-57c64df02312",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NyvoCcWBkQGDDZmZweDWiv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 669,
      "cache_read_input_tokens": 22793,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 669,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 22793,
          "cache_creation_input_tokens": 669,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 669
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

_source line 23_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Premise-Graph Contrastive Training for Logic-Grounded Process Reward Models  ## Core Problem  Current process reward models detect consistency rather than causality. \"Reward Models Identify Consiste…",
  "leafUuid": "eaf50b3a-4233-4587-b5ca-c8721eca0a34",
  "sessionId": "75462fa2-385d-4000-b649-57c64df02312"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Premise-Graph contrastive training for process reward models",
  "sessionId": "75462fa2-385d-4000-b649-57c64df02312"
}
```

---

### Tool result

_source line 25 · 2026-05-27T08:43:43.593Z_

<details><summary>↩ Tool result · `toolu_01N4JwYXuwx4qhk2SgjKD5uY`</summary>

```text
Web search results for query: "Graph of Verification GoV DAG reasoning verification arXiv:2506.12509 2025"

Links: [{"title":"Graph of Verification: Structured Verification of LLM Reasoning","url":"https://arxiv.org/pdf/2506.12509"},{"title":"Graph of Verification: Structured Verification of LLM Reasoning with Directed Acyclic Graphs","url":"https://arxiv.org/html/2506.12509v3"},{"title":"[2506.12509] Graph of Verification: Structured Verification of LLM Reasoning with Directed Acyclic Graphs","url":"https://arxiv.org/abs/2506.12509"},{"title":"Graph of Verification: Structured Verification of LLM Reasoning with Directed Acyclic Graphs","url":"https://www.researchgate.net/publication/392735078_Graph_of_Verification_Structured_Verification_of_LLM_Reasoning_with_Directed_Acyclic_Graphs"},{"title":"Paper page - Graph of Verification: Structured Verification of LLM Reasoning with Directed Acyclic Graphs","url":"https://huggingface.co/papers/2506.12509"},{"title":"Verifying Chain-of-Thought Reasoning via Its Computational Graph","url":"https://arxiv.org/pdf/2510.09312"},{"title":"GraphReason: Enhancing Reasoning Capabilities of Large Language Models   through A Graph-Based Verification Approach","url":"https://arxiv.org/pdf/2308.09267"}]

Based on the search results, here's what I found about arXiv:2506.12509:

## Graph of Verification (GoV)

The Graph of Verification (GoV) is a novel framework for adaptable and multi-granular verification of Large Language Model reasoning.

### Key Innovation

GoV's core innovation is its flexible "node block" architecture that allows it to adaptively adjust its verification granularity--from atomic steps for formal tasks to entire paragraphs for natural language--to match the native structure of the reasoning process.

### How It Works

GoV operationalizes structured validation by first modeling reasoning as a Directed Acyclic Graph (DAG). A topological sort then enforces causal consistency, ensuring premises are verified before conclusions. Following this order, sequential verification is performed by an LLM which assesses each unit based on previously validated antecedents. The process terminates at the first detected error, enabling precise fault localization and guaranteeing the logical soundness of any fully verified reasoning chain.

### Performance

Experiments on both well-structured and loosely-structured benchmarks demonstrate GoV's versatility, with results showing that GoV's adaptive approach significantly outperforms both holistic baselines and other state-of-the-art decomposition-based methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eaf50b3a-4233-4587-b5ca-c8721eca0a34",
  "isSidechain": false,
  "promptId": "18914ca9-b0a2-4983-9544-756340563499",
  "type": "user",
  "uuid": "0347894e-9587-4490-aafb-a14177f6080e",
  "toolUseResult": {
    "query": "Graph of Verification GoV DAG reasoning verification arXiv:2506.12509 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Grjxvq27KvWuxKoRGd9ZM4",
        "content": [
          {
            "title": "Graph of Verification: Structured Verification of LLM Reasoning",
            "url": "https://arxiv.org/pdf/2506.12509"
          },
          {
            "title": "Graph of Verification: Structured Verification of LLM Reasoning with Directed Acyclic Graphs",
            "url": "https://arxiv.org/html/2506.12509v3"
          },
          {
            "title": "[2506.12509] Graph of Verification: Structured Verification of LLM Reasoning with Directed Acyclic Graphs",
            "url": "https://arxiv.org/abs/2506.12509"
          },
          {
            "title": "Graph of Verification: Structured Verification of LLM Reasoning with Directed Acyclic Graphs",
            "url": "https://www.researchgate.net/publication/392735078_Graph_of_Verification_Structured_Verification_of_LLM_Reasoning_with_Directed_Acyclic_Graphs"
          },
          {
            "title": "Paper page - Graph of Verification: Structured Verification of LLM Reasoning with Directed Acyclic Graphs",
            "url": "https://huggingface.co/papers/2506.12509"
          },
          {
            "title": "Verifying Chain-of-Thought Reasoning via Its Computational Graph",
            "url": "https://arxiv.org/pdf/2510.09312"
          },
          {
            "title": "GraphReason: Enhancing Reasoning Capabilities of Large Language Models   through A Graph-Based Verification Approach",
            "url": "https://arxiv.org/pdf/2308.09267"
          }
        ]
      },
      "Based on the search results, here's what I found about arXiv:2506.12509:\n\n## Graph of Verification (GoV)\n\nThe Graph of Verification (GoV) is a novel framework for adaptable and multi-granular verification of Large Language Model reasoning.\n\n### Key Innovation\n\nGoV's core innovation is its flexible \"node block\" architecture that allows it to adaptively adjust its verification granularity--from atomic steps for formal tasks to entire paragraphs for natural language--to match the native structure of the reasoning process.\n\n### How It Works\n\nGoV operationalizes structured validation by first modeling reasoning as a Directed Acyclic Graph (DAG). A topological sort then enforces causal consistency, ensuring premises are verified before conclusions. Following this order, sequential verification is performed by an LLM which assesses each unit based on previously validated antecedents. The process terminates at the first detected error, enabling precise fault localization and guaranteeing the logical soundness of any fully verified reasoning chain.\n\n### Performance\n\nExperiments on both well-structured and loosely-structured benchmarks demonstrate GoV's versatility, with results showing that GoV's adaptive approach significantly outperforms both holistic baselines and other state-of-the-art decomposition-based methods."
    ],
    "durationSeconds": 8.818244025,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "eaf50b3a-4233-4587-b5ca-c8721eca0a34",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "75462fa2-385d-4000-b649-57c64df02312",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-27T08:43:46.565Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JvwHM487MGXMVHq1EPyuh2`</summary>

```json
{
  "query": "PathFinder-PRM process reward model PRMBench state of the art 2025 arXiv:2505.19706"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0347894e-9587-4490-aafb-a14177f6080e",
  "isSidechain": false,
  "requestId": "req_011CbSn6DCSCs7Jh49LmMg7j",
  "type": "assistant",
  "uuid": "591594bf-f2f9-423b-b4b5-8899ce25ae06",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "75462fa2-385d-4000-b649-57c64df02312",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AdZNRWDMMS295SMrWq8z9r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 771,
      "cache_read_input_tokens": 23462,
      "output_tokens": 81,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 771,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 81,
          "cache_read_input_tokens": 23462,
          "cache_creation_input_tokens": 771,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 771
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

_source line 27 · 2026-05-27T08:43:54.005Z_

<details><summary>↩ Tool result · `toolu_01JvwHM487MGXMVHq1EPyuh2`</summary>

```text
Web search results for query: "PathFinder-PRM process reward model PRMBench state of the art 2025 arXiv:2505.19706"

Links: [{"title":"[2505.19706] Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision","url":"https://arxiv.org/abs/2505.19706"},{"title":"GitHub - declare-lab/PathFinder-PRM: This repository contains the official implementation of Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision.","url":"https://github.com/declare-lab/PathFinder-PRM"},{"title":"Process-Supervised Reward Model","url":"https://www.emergentmind.com/topics/process-supervised-reward-model-prm"},{"title":"PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models","url":"https://arxiv.org/pdf/2501.03124"},{"title":"Improving Process Reward Models with Error-Aware ...","url":"https://arxiv.org/pdf/2505.19706"},{"title":"[2501.03124] PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models","url":"https://arxiv.org/abs/2501.03124"},{"title":"PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models","url":"https://prmbench.github.io/"},{"title":"GitHub - RyanLiu112/Awesome-Process-Reward-Models: A comprehensive collection of process reward models. · GitHub","url":"https://github.com/RyanLiu112/Awesome-Process-Reward-Models"}]

Based on the search results, here's information about the PathFinder-PRM paper and its state-of-the-art results on PRMBench:

## Overview

PathFinder-PRM is a novel hierarchical, error-aware discriminative PRM that first classifies math and consistency errors at each step, then combines these fine-grained signals to estimate step correctness.

## State-of-the-Art Results on PRMBench

On PRMBench, PathFinder-PRM achieves a new state-of-the-art PRMScore of 67.7, outperforming the prior best (65.5) while using 3 times less data. Additionally, when applied to reward guided greedy search, the model yields prm@8 48.3, a +1.5 point gain over the strongest baseline.

## Training Approach

To train PathFinder-PRM, researchers constructed a 400K-sample dataset by enriching the human-annotated PRM800K corpus and RLHFlow Mistral traces with three-dimensional step-level labels.

The paper arXiv:2505.19706 is titled "Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision" and was published on May 26, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "591594bf-f2f9-423b-b4b5-8899ce25ae06",
  "isSidechain": false,
  "promptId": "18914ca9-b0a2-4983-9544-756340563499",
  "type": "user",
  "uuid": "011f1360-8664-4a38-aa3a-0825102a8306",
  "toolUseResult": {
    "query": "PathFinder-PRM process reward model PRMBench state of the art 2025 arXiv:2505.19706",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PBnWrhPPosiSsXRoGybaRG",
        "content": [
          {
            "title": "[2505.19706] Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision",
            "url": "https://arxiv.org/abs/2505.19706"
          },
          {
            "title": "GitHub - declare-lab/PathFinder-PRM: This repository contains the official implementation of Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision.",
            "url": "https://github.com/declare-lab/PathFinder-PRM"
          },
          {
            "title": "Process-Supervised Reward Model",
            "url": "https://www.emergentmind.com/topics/process-supervised-reward-model-prm"
          },
          {
            "title": "PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models",
            "url": "https://arxiv.org/pdf/2501.03124"
          },
          {
            "title": "Improving Process Reward Models with Error-Aware ...",
            "url": "https://arxiv.org/pdf/2505.19706"
          },
          {
            "title": "[2501.03124] PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models",
            "url": "https://arxiv.org/abs/2501.03124"
          },
          {
            "title": "PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models",
            "url": "https://prmbench.github.io/"
          },
          {
            "title": "GitHub - RyanLiu112/Awesome-Process-Reward-Models: A comprehensive collection of process reward models. · GitHub",
            "url": "https://github.com/RyanLiu112/Awesome-Process-Reward-Models"
          }
        ]
      },
      "Based on the search results, here's information about the PathFinder-PRM paper and its state-of-the-art results on PRMBench:\n\n## Overview\n\nPathFinder-PRM is a novel hierarchical, error-aware discriminative PRM that first classifies math and consistency errors at each step, then combines these fine-grained signals to estimate step correctness.\n\n## State-of-the-Art Results on PRMBench\n\nOn PRMBench, PathFinder-PRM achieves a new state-of-the-art PRMScore of 67.7, outperforming the prior best (65.5) while using 3 times less data. Additionally, when applied to reward guided greedy search, the model yields prm@8 48.3, a +1.5 point gain over the strongest baseline.\n\n## Training Approach\n\nTo train PathFinder-PRM, researchers constructed a 400K-sample dataset by enriching the human-annotated PRM800K corpus and RLHFlow Mistral traces with three-dimensional step-level labels.\n\nThe paper arXiv:2505.19706 is titled \"Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision\" and was published on May 26, 2025."
    ],
    "durationSeconds": 7.434752780999989,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "591594bf-f2f9-423b-b4b5-8899ce25ae06",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "75462fa2-385d-4000-b649-57c64df02312",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-27T08:43:57.570Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01USZd4tiFhrQWxJA4iNtvGq`</summary>

```json
{
  "query": "\"Reward Under Attack\" process reward model hacking stylistic shortcuts arXiv:2603.06621"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "011f1360-8664-4a38-aa3a-0825102a8306",
  "isSidechain": false,
  "requestId": "req_011CbSn6ynZrYj7yKNcquMYA",
  "type": "assistant",
  "uuid": "b1a0a917-0baa-4cdd-bbdd-c36a35d05a4f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "75462fa2-385d-4000-b649-57c64df02312",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CRtFef4xwmq2vaepKMgbNG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 838,
      "cache_read_input_tokens": 24233,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 838,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 24233,
          "cache_creation_input_tokens": 838,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 838
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

_source line 29 · 2026-05-27T08:44:04.604Z_

<details><summary>↩ Tool result · `toolu_01USZd4tiFhrQWxJA4iNtvGq`</summary>

```text
Web search results for query: ""Reward Under Attack" process reward model hacking stylistic shortcuts arXiv:2603.06621"

Links: [{"title":"[2603.06621] Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models","url":"https://arxiv.org/abs/2603.06621"},{"title":"Reward Under Attack: Analyzing the Robustness and Hackability of","url":"https://arxiv.org/pdf/2603.06621"},{"title":"When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals","url":"https://arxiv.org/pdf/2604.01476"},{"title":"Is It Thinking or Cheating? Detecting Implicit Reward Hacking by Measuring Reasoning Effort","url":"https://arxiv.org/pdf/2510.01367"},{"title":"Beyond Semantic Manipulation: Token-Space Attacks on Reward Models","url":"https://arxiv.org/pdf/2604.02686"},{"title":"Rectifying Shortcut Behaviors in Preference-based Reward Learning","url":"https://arxiv.org/pdf/2510.19050"},{"title":"Adversarial Training of Reward Models","url":"https://arxiv.org/pdf/2504.06141"}]

Based on the search results, I found the paper you're looking for:

"Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models" demonstrates that state-of-the-art Process Reward Models (PRMs) are systematically exploitable under adversarial optimization pressure.

Key findings from the paper include:

- Policies trained on AIME problems achieve near-perfect PRM rewards (>0.9) while ground-truth accuracy remains low (below 4%), with 43% of reward gains attributable to stylistic shortcuts.

- Current PRMs function as fluency detectors rather than reasoning verifiers, creating systematic blind spots that undermine their use as training signals.

- The researchers introduce a three-tiered diagnostic framework that applies increasing adversarial pressure to quantify these vulnerabilities.

- They release PRM-BiasBench and a diagnostic toolkit to enable robustness evaluation before deployment.

The paper was published on arXiv on February 20, 2026, by Rishabh Tiwari and co-authors.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b1a0a917-0baa-4cdd-bbdd-c36a35d05a4f",
  "isSidechain": false,
  "promptId": "18914ca9-b0a2-4983-9544-756340563499",
  "type": "user",
  "uuid": "477e06ab-5018-4b25-9f2e-d5726f2b4b83",
  "toolUseResult": {
    "query": "\"Reward Under Attack\" process reward model hacking stylistic shortcuts arXiv:2603.06621",
    "results": [
      {
        "tool_use_id": "srvtoolu_01V98AXndLmNB7L1oDQXhSbp",
        "content": [
          {
            "title": "[2603.06621] Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models",
            "url": "https://arxiv.org/abs/2603.06621"
          },
          {
            "title": "Reward Under Attack: Analyzing the Robustness and Hackability of",
            "url": "https://arxiv.org/pdf/2603.06621"
          },
          {
            "title": "When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals",
            "url": "https://arxiv.org/pdf/2604.01476"
          },
          {
            "title": "Is It Thinking or Cheating? Detecting Implicit Reward Hacking by Measuring Reasoning Effort",
            "url": "https://arxiv.org/pdf/2510.01367"
          },
          {
            "title": "Beyond Semantic Manipulation: Token-Space Attacks on Reward Models",
            "url": "https://arxiv.org/pdf/2604.02686"
          },
          {
            "title": "Rectifying Shortcut Behaviors in Preference-based Reward Learning",
            "url": "https://arxiv.org/pdf/2510.19050"
          },
          {
            "title": "Adversarial Training of Reward Models",
            "url": "https://arxiv.org/pdf/2504.06141"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n\"Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models\" demonstrates that state-of-the-art Process Reward Models (PRMs) are systematically exploitable under adversarial optimization pressure.\n\nKey findings from the paper include:\n\n- Policies trained on AIME problems achieve near-perfect PRM rewards (>0.9) while ground-truth accuracy remains low (below 4%), with 43% of reward gains attributable to stylistic shortcuts.\n\n- Current PRMs function as fluency detectors rather than reasoning verifiers, creating systematic blind spots that undermine their use as training signals.\n\n- The researchers introduce a three-tiered diagnostic framework that applies increasing adversarial pressure to quantify these vulnerabilities.\n\n- They release PRM-BiasBench and a diagnostic toolkit to enable robustness evaluation before deployment.\n\nThe paper was published on arXiv on February 20, 2026, by Rishabh Tiwari and co-authors."
    ],
    "durationSeconds": 7.029811998000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "b1a0a917-0baa-4cdd-bbdd-c36a35d05a4f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "75462fa2-385d-4000-b649-57c64df02312",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-27T08:44:04.611Z_

```json
{
  "parentUuid": "477e06ab-5018-4b25-9f2e-d5726f2b4b83",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "dcf1c2d4-63be-4fbe-9137-665fa55a55c0",
  "timestamp": "2026-05-27T08:44:04.611Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "75462fa2-385d-4000-b649-57c64df02312",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 31 · 2026-05-27T08:44:07.462Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HkWskpxLkWoGpyL3iMH8Gs`</summary>

```json
{
  "query": "contrastive representation learning reward model structural graph embedding training 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dcf1c2d4-63be-4fbe-9137-665fa55a55c0",
  "isSidechain": false,
  "requestId": "req_011CbSn7m86NuDYoRppSm54V",
  "type": "assistant",
  "uuid": "6eb04d13-5d1e-4356-aae8-24c8875587c3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "75462fa2-385d-4000-b649-57c64df02312",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0166sxGbaYFRmudYumGfU1T9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 759,
      "cache_read_input_tokens": 25071,
      "output_tokens": 68,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 759,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 68,
          "cache_read_input_tokens": 25071,
          "cache_creation_input_tokens": 759,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 759
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

_source line 32 · 2026-05-27T08:44:14.417Z_

<details><summary>↩ Tool result · `toolu_01HkWskpxLkWoGpyL3iMH8Gs`</summary>

```text
Web search results for query: "contrastive representation learning reward model structural graph embedding training 2025 2026"

Links: [{"title":"Graph contrastive high-order structure representation learning - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0925231225032382"},{"title":"Multi-scale tree-guided contrastive learning for structure-aware graph representation | Complex & Intelligent Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s40747-025-02219-7"},{"title":"Contrastive multi-view representation learning on graphs | Proceedings of the 37th International Conference on Machine Learning","url":"https://dl.acm.org/doi/10.5555/3524938.3525323"},{"title":"Contrastive Learning of Structured World Models","url":"https://arxiv.org/pdf/1911.12247"},{"title":"Control-based Graph Embeddings with Data Augmentation for Contrastive   Learning","url":"https://arxiv.org/pdf/2403.04923"},{"title":"Contrastive Multi-View Representation Learning on Graphs","url":"https://arxiv.org/pdf/2006.05582"},{"title":"GraphCL: Contrastive Self-Supervised Learning of Graph Representations","url":"https://arxiv.org/pdf/2007.08025"},{"title":"Contrastive learning enhanced by graph neural networks for Universal Multivariate Time Series Representation - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0306437924000875"},{"title":"Str-GCL: Structural Commonsense Driven Graph Contrastive Learning","url":"https://arxiv.org/pdf/2507.07141"}]

I've found several recent research papers and articles on contrastive representation learning, graph embeddings, and structural graph learning from 2025-2026. Here are the key findings:

## Recent Developments (2025-2026)

**Graph Contrastive Learning with Structural Focus:**

Contrastive learning is being integrated into graph representation algorithms to maintain graph structure information, with high-order structure capture modules combined with graph contrast learning to fully explore the graph structure.

Recent work designs dual-path contrastive objectives that enforce semantic consistency across augmented views and structural discriminability for both structural and augmented views.

**Structural Commonsense Integration:**

A novel approach embeds structural commonsense into models using first-order logic rules, enabling encoders to perceive additional structural knowledge and focus on intricate patterns within graphs, ultimately enhancing model performance and interpretability.

**Multi-Scale Tree-Guided Approaches:**

Multi-scale tree-guided contrastive learning methods demonstrate an average improvement of 1.76% across benchmark datasets, with robust generalization and parameter stability confirmed through ablation and sensitivity analyses.

These recent works show a clear trend toward combining contrastive learning with sophisticated structural modeling techniques, including augmentation strategies that preserve graph topology while enabling discriminative learning of representations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6eb04d13-5d1e-4356-aae8-24c8875587c3",
  "isSidechain": false,
  "promptId": "18914ca9-b0a2-4983-9544-756340563499",
  "type": "user",
  "uuid": "f35a4e80-943a-479e-8a44-d4d1593cc497",
  "toolUseResult": {
    "query": "contrastive representation learning reward model structural graph embedding training 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01ETwtnPVqkyEgbtWxf2va4B",
        "content": [
          {
            "title": "Graph contrastive high-order structure representation learning - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/abs/pii/S0925231225032382"
          },
          {
            "title": "Multi-scale tree-guided contrastive learning for structure-aware graph representation | Complex & Intelligent Systems | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s40747-025-02219-7"
          },
          {
            "title": "Contrastive multi-view representation learning on graphs | Proceedings of the 37th International Conference on Machine Learning",
            "url": "https://dl.acm.org/doi/10.5555/3524938.3525323"
          },
          {
            "title": "Contrastive Learning of Structured World Models",
            "url": "https://arxiv.org/pdf/1911.12247"
          },
          {
            "title": "Control-based Graph Embeddings with Data Augmentation for Contrastive   Learning",
            "url": "https://arxiv.org/pdf/2403.04923"
          },
          {
            "title": "Contrastive Multi-View Representation Learning on Graphs",
            "url": "https://arxiv.org/pdf/2006.05582"
          },
          {
            "title": "GraphCL: Contrastive Self-Supervised Learning of Graph Representations",
            "url": "https://arxiv.org/pdf/2007.08025"
          },
          {
            "title": "Contrastive learning enhanced by graph neural networks for Universal Multivariate Time Series Representation - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/abs/pii/S0306437924000875"
          },
          {
            "title": "Str-GCL: Structural Commonsense Driven Graph Contrastive Learning",
            "url": "https://arxiv.org/pdf/2507.07141"
          }
        ]
      },
      "I've found several recent research papers and articles on contrastive representation learning, graph embeddings, and structural graph learning from 2025-2026. Here are the key findings:\n\n## Recent Developments (2025-2026)\n\n**Graph Contrastive Learning with Structural Focus:**\n\nContrastive learning is being integrated into graph representation algorithms to maintain graph structure information, with high-order structure capture modules combined with graph contrast learning to fully explore the graph structure.\n\nRecent work designs dual-path contrastive objectives that enforce semantic consistency across augmented views and structural discriminability for both structural and augmented views.\n\n**Structural Commonsense Integration:**\n\nA novel approach embeds structural commonsense into models using first-order logic rules, enabling encoders to perceive additional structural knowledge and focus on intricate patterns within graphs, ultimately enhancing model performance and interpretability.\n\n**Multi-Scale Tree-Guided Approaches:**\n\nMulti-scale tree-guided contrastive learning methods demonstrate an average improvement of 1.76% across benchmark datasets, with robust generalization and parameter stability confirmed through ablation and sensitivity analyses.\n\nThese recent works show a clear trend toward combining contrastive learning with sophisticated structural modeling techniques, including augmentation strategies that preserve graph topology while enabling discriminative learning of representations."
    ],
    "durationSeconds": 6.950536195000008,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "6eb04d13-5d1e-4356-aae8-24c8875587c3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "75462fa2-385d-4000-b649-57c64df02312",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-27T08:44:17.581Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012LmKfDsGojE3p6WquNCYY2`</summary>

```json
{
  "query": "CRM conditional reward model ICLR 2026 sequential step conditioning arXiv:2509.26578"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f35a4e80-943a-479e-8a44-d4d1593cc497",
  "isSidechain": false,
  "requestId": "req_011CbSn8V11DGzumRTuXoyky",
  "type": "assistant",
  "uuid": "24cdcbe2-29e1-445f-a580-856db37c2a0a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "75462fa2-385d-4000-b649-57c64df02312",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KHxz6SoJuUhna9T8vvZvaC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 817,
      "cache_read_input_tokens": 25830,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 817,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 25830,
          "cache_creation_input_tokens": 817,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 817
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

_source line 34 · 2026-05-27T08:44:23.566Z_

<details><summary>↩ Tool result · `toolu_012LmKfDsGojE3p6WquNCYY2`</summary>

```text
Web search results for query: "CRM conditional reward model ICLR 2026 sequential step conditioning arXiv:2509.26578"

Links: [{"title":"[2509.26578] Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning","url":"https://arxiv.org/abs/2509.26578"},{"title":"Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning","url":"https://arxiv.org/pdf/2509.26578"},{"title":"Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning","url":"https://arxiv.org/html/2509.26578"},{"title":"Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning | OpenReview","url":"https://openreview.net/forum?id=4DJoBOQNd0"},{"title":"Linking Process to Outcome: Conditional Reward Modeling (CRM) for LLM Reasoning","url":"https://foundation-model-research.github.io/CRM/"}]

Based on the search results, I found information about the paper you're looking for:

The paper proposes Conditional Reward Modeling (CRM) that frames LLM reasoning as a temporal process leading to a correct answer, where the reward of each reasoning step is not only conditioned on the preceding steps but also explicitly linked to the final outcome of the reasoning trajectory.

The work addresses limitations of existing Process Reward Models (PRMs) which either treat each reasoning step in isolation, failing to capture inter-step dependencies, or struggle to align process rewards with the final outcome, resulting in reward signals that fail to respect temporal causality in sequential reasoning.

By enforcing conditional probability rules, the design captures the causal relationships among reasoning steps, with the link to the outcome allowing precise attribution of each intermediate step, thereby resolving credit assignment ambiguity.

Experiments across Best-of-N sampling, beam search and reinforcement learning demonstrate that CRM consistently outperforms existing reward models, is more robust to reward hacking, and delivers stable downstream improvements without relying on verifiable rewards derived from ground truth.

The paper is published at the International Conference on Learning Representations (ICLR) in 2026 by authors Zheng Zhang, Ziwei Shan, Kaitao Song, Yexin Li, and Kan Ren.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "24cdcbe2-29e1-445f-a580-856db37c2a0a",
  "isSidechain": false,
  "promptId": "18914ca9-b0a2-4983-9544-756340563499",
  "type": "user",
  "uuid": "ab4540d3-51ff-4300-ab7c-9d411f23a5ae",
  "toolUseResult": {
    "query": "CRM conditional reward model ICLR 2026 sequential step conditioning arXiv:2509.26578",
    "results": [
      {
        "tool_use_id": "srvtoolu_01S4zmnoffQB4TEFv5vvFpgX",
        "content": [
          {
            "title": "[2509.26578] Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning",
            "url": "https://arxiv.org/abs/2509.26578"
          },
          {
            "title": "Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning",
            "url": "https://arxiv.org/pdf/2509.26578"
          },
          {
            "title": "Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning",
            "url": "https://arxiv.org/html/2509.26578"
          },
          {
            "title": "Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning | OpenReview",
            "url": "https://openreview.net/forum?id=4DJoBOQNd0"
          },
          {
            "title": "Linking Process to Outcome: Conditional Reward Modeling (CRM) for LLM Reasoning",
            "url": "https://foundation-model-research.github.io/CRM/"
          }
        ]
      },
      "Based on the search results, I found information about the paper you're looking for:\n\nThe paper proposes Conditional Reward Modeling (CRM) that frames LLM reasoning as a temporal process leading to a correct answer, where the reward of each reasoning step is not only conditioned on the preceding steps but also explicitly linked to the final outcome of the reasoning trajectory.\n\nThe work addresses limitations of existing Process Reward Models (PRMs) which either treat each reasoning step in isolation, failing to capture inter-step dependencies, or struggle to align process rewards with the final outcome, resulting in reward signals that fail to respect temporal causality in sequential reasoning.\n\nBy enforcing conditional probability rules, the design captures the causal relationships among reasoning steps, with the link to the outcome allowing precise attribution of each intermediate step, thereby resolving credit assignment ambiguity.\n\nExperiments across Best-of-N sampling, beam search and reinforcement learning demonstrate that CRM consistently outperforms existing reward models, is more robust to reward hacking, and delivers stable downstream improvements without relying on verifiable rewards derived from ground truth.\n\nThe paper is published at the International Conference on Learning Representations (ICLR) in 2026 by authors Zheng Zhang, Ziwei Shan, Kaitao Song, Yexin Li, and Kan Ren."
    ],
    "durationSeconds": 5.980504842000009,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "24cdcbe2-29e1-445f-a580-856db37c2a0a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "75462fa2-385d-4000-b649-57c64df02312",
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
  "lastPrompt": "# Premise-Graph Contrastive Training for Logic-Grounded Process Reward Models  ## Core Problem  Current process reward models detect consistency rather than causality. \"Reward Models Identify Consiste…",
  "leafUuid": "ab4540d3-51ff-4300-ab7c-9d411f23a5ae",
  "sessionId": "75462fa2-385d-4000-b649-57c64df02312"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Premise-Graph contrastive training for process reward models",
  "sessionId": "75462fa2-385d-4000-b649-57c64df02312"
}
```

---

### Tool call

_source line 37 · 2026-05-27T08:44:26.555Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QQuBR8cFBV3KsSTnT2KhCC`</summary>

```json
{
  "query": "\"representation-utilization gap\" OR \"representation gap\" reward model LLM latent structure 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab4540d3-51ff-4300-ab7c-9d411f23a5ae",
  "isSidechain": false,
  "requestId": "req_011CbSn9A9DgUAeDRJPTjksR",
  "type": "assistant",
  "uuid": "d79f2b7f-2d4e-44e1-910b-48ba4b8f381e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "75462fa2-385d-4000-b649-57c64df02312",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013L6dwG2HFnP4SxDqS5qiQf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 659,
      "cache_read_input_tokens": 26647,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 659,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 26647,
          "cache_creation_input_tokens": 659,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 659
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

_source line 38 · 2026-05-27T08:44:42.137Z_

<details><summary>↩ Tool result · `toolu_01QQuBR8cFBV3KsSTnT2KhCC`</summary>

```text
Web search results for query: ""representation-utilization gap" OR "representation gap" reward model LLM latent structure 2025 2026"

Links: [{"title":"Latent Reward Models in AI Systems","url":"https://www.emergentmind.com/topics/latent-reward-models-lrms"},{"title":"Published as a conference paper at ICLR 2026 LATENT THINKING OPTIMIZATION:","url":"https://arxiv.org/pdf/2509.26314"},{"title":"Mining Intrinsic Rewards from LLM Hidden States for Efficient Best-of-N Sampling","url":"https://arxiv.org/pdf/2505.12225"},{"title":"LLM-Based Reward Models","url":"https://www.emergentmind.com/topics/llm-based-reward-models"},{"title":"On the Generalization Gap in LLM Planning: Tests and Verifier-Reward RL","url":"https://arxiv.org/html/2601.14456"},{"title":"Latent Reward Model (LRM)","url":"https://www.emergentmind.com/topics/latent-reward-model-lrm"}]

I found relevant research on latent reward models and related topics. Here are the key findings from recent work (2025-2026):

## Latent Reward Models (LRMs)

Latent Reward Models are reward modeling techniques wherein the reward function operates in a learned latent representation space, rather than directly from explicit outputs, designed to bridge the gap between high-dimensional, non-interpretable internal model states and reliable external supervision signals.

Operating in latent space allows reward models to bypass inefficient, costly back-and-forth transformations to output space.

## Recent Developments

**Latent Thinking Optimization (ICLR 2026):** Researchers have developed a Latent Reward Model approach to sample latent thinking trajectories with higher estimated likelihood of correctness, theoretically guaranteed to improve expected correctness rates. While using models with explicit latent thinking processes, the LRM approach extends to general LLMs whose latent representations across multiple layers can be interpreted as latent chain of thoughts.

**Mining Intrinsic Rewards:** Research addresses an architectural mismatch between LLM internal mechanisms optimized for text and the continuous high-dimensional vectors of hidden states, necessitating a paradigm shift toward architectures specifically designed to mine intrinsic signals directly from latent sources.

**Generalist Reward Models:** Recent work demonstrates that a latent reward function is encoded in the logits of any next-token trained LLM, with no additional preference learning step needed.

The search results show active research on representation-based reward modeling in 2025-2026, though I didn't find explicit discussions of a "representation-utilization gap" by that specific name.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d79f2b7f-2d4e-44e1-910b-48ba4b8f381e",
  "isSidechain": false,
  "promptId": "18914ca9-b0a2-4983-9544-756340563499",
  "type": "user",
  "uuid": "15ea4161-b84f-45ab-bd91-d25189fef875",
  "toolUseResult": {
    "query": "\"representation-utilization gap\" OR \"representation gap\" reward model LLM latent structure 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_014o2w3WcH1ig4oJFbyyNsPa",
        "content": [
          {
            "title": "Latent Reward Models in AI Systems",
            "url": "https://www.emergentmind.com/topics/latent-reward-models-lrms"
          },
          {
            "title": "Published as a conference paper at ICLR 2026 LATENT THINKING OPTIMIZATION:",
            "url": "https://arxiv.org/pdf/2509.26314"
          },
          {
            "title": "Mining Intrinsic Rewards from LLM Hidden States for Efficient Best-of-N Sampling",
            "url": "https://arxiv.org/pdf/2505.12225"
          },
          {
            "title": "LLM-Based Reward Models",
            "url": "https://www.emergentmind.com/topics/llm-based-reward-models"
          },
          {
            "title": "On the Generalization Gap in LLM Planning: Tests and Verifier-Reward RL",
            "url": "https://arxiv.org/html/2601.14456"
          },
          {
            "title": "Latent Reward Model (LRM)",
            "url": "https://www.emergentmind.com/topics/latent-reward-model-lrm"
          }
        ]
      },
      "I found relevant research on latent reward models and related topics. Here are the key findings from recent work (2025-2026):\n\n## Latent Reward Models (LRMs)\n\nLatent Reward Models are reward modeling techniques wherein the reward function operates in a learned latent representation space, rather than directly from explicit outputs, designed to bridge the gap between high-dimensional, non-interpretable internal model states and reliable external supervision signals.\n\nOperating in latent space allows reward models to bypass inefficient, costly back-and-forth transformations to output space.\n\n## Recent Developments\n\n**Latent Thinking Optimization (ICLR 2026):** Researchers have developed a Latent Reward Model approach to sample latent thinking trajectories with higher estimated likelihood of correctness, theoretically guaranteed to improve expected correctness rates. While using models with explicit latent thinking processes, the LRM approach extends to general LLMs whose latent representations across multiple layers can be interpreted as latent chain of thoughts.\n\n**Mining Intrinsic Rewards:** Research addresses an architectural mismatch between LLM internal mechanisms optimized for text and the continuous high-dimensional vectors of hidden states, necessitating a paradigm shift toward architectures specifically designed to mine intrinsic signals directly from latent sources.\n\n**Generalist Reward Models:** Recent work demonstrates that a latent reward function is encoded in the logits of any next-token trained LLM, with no additional preference learning step needed.\n\nThe search results show active research on representation-based reward modeling in 2025-2026, though I didn't find explicit discussions of a \"representation-utilization gap\" by that specific name."
    ],
    "durationSeconds": 15.575532834999992,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d79f2b7f-2d4e-44e1-910b-48ba4b8f381e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "75462fa2-385d-4000-b649-57c64df02312",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-27T08:44:45.413Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01J2EiMYCpacQLVUovFCvawY`</summary>

```json
{
  "query": "Factored Causal Representation Learning Robust Reward Modeling RLHF arXiv:2601.21350 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15ea4161-b84f-45ab-bd91-d25189fef875",
  "isSidechain": false,
  "requestId": "req_011CbSnAXXs6p414jVYYRYSN",
  "type": "assistant",
  "uuid": "f74dd0a2-154f-4f7a-9d6c-083b3db428ff",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "75462fa2-385d-4000-b649-57c64df02312",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FUrARWjEBbcua2xzEJFP3o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 759,
      "cache_read_input_tokens": 27306,
      "output_tokens": 83,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 759,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 83,
          "cache_read_input_tokens": 27306,
          "cache_creation_input_tokens": 759,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 759
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

_source line 40 · 2026-05-27T08:44:52.275Z_

<details><summary>↩ Tool result · `toolu_01J2EiMYCpacQLVUovFCvawY`</summary>

```text
Web search results for query: "Factored Causal Representation Learning Robust Reward Modeling RLHF arXiv:2601.21350 2026"

Links: [{"title":"[2601.21350] Factored Causal Representation Learning for Robust Reward Modeling in RLHF","url":"https://arxiv.org/abs/2601.21350"},{"title":"ICML Poster Factored Causal Representation Learning for Robust Reward Modeling in RLHF","url":"https://icml.cc/virtual/2026/poster/65508"},{"title":"Factored Causal Representation Learning for Robust Reward Modeling in RLHF","url":"https://www.arxiv.org/pdf/2601.21350"},{"title":"Beyond Reward Hacking: Causal Rewards for Large Language Model Alignment","url":"https://arxiv.org/html/2501.09620v1"},{"title":"Robust Reward Modeling for Large Language Models via Causal Decomposition","url":"https://arxiv.org/html/2604.13833"},{"title":"Robust Reward Modeling via Causal Rubrics","url":"https://arxiv.org/pdf/2506.16507"},{"title":"Mitigating Reward Hacking in RLHF via Bayesian Non-negative Reward Modeling","url":"https://arxiv.org/pdf/2602.10623"},{"title":"Counterfactual Reward Model Training for Bias Mitigation in Multimodal Reinforcement Learning","url":"https://arxiv.org/html/2508.19567v1"}]

Based on the web search results, here's what I found about the paper arXiv:2601.21350:

## Factored Causal Representation Learning for Robust Reward Modeling in RLHF

A reliable reward model is essential for aligning large language models with human preferences through reinforcement learning from human feedback. However, standard reward models are susceptible to spurious features that are not causally related to human labels.

**The Proposed Approach:**

The work proposes a factored representation learning framework that decomposes the model's contextual embedding into (1) causal factors that are sufficient for reward prediction and (2) non-causal factors that capture reward-irrelevant attributes such as length or sycophantic bias. The reward head is then constrained to depend only on the causal component. Additionally, an adversarial head is trained to predict reward from the non-causal factors, while applying gradient reversal to discourage them from encoding reward-relevant information.

**Results:**

Experiments on both mathematical and dialogue tasks demonstrate that the method learns more robust reward models and consistently improves downstream RLHF performance over state-of-the-art baselines.

The paper was published on arXiv on January 29, 2026, and has also been presented as a poster at ICML 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f74dd0a2-154f-4f7a-9d6c-083b3db428ff",
  "isSidechain": false,
  "promptId": "18914ca9-b0a2-4983-9544-756340563499",
  "type": "user",
  "uuid": "ae4a624c-ff42-43e0-9eb7-4d31907cecea",
  "toolUseResult": {
    "query": "Factored Causal Representation Learning Robust Reward Modeling RLHF arXiv:2601.21350 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_016bhR2xuFhRq4ABuvsqARZy",
        "content": [
          {
            "title": "[2601.21350] Factored Causal Representation Learning for Robust Reward Modeling in RLHF",
            "url": "https://arxiv.org/abs/2601.21350"
          },
          {
            "title": "ICML Poster Factored Causal Representation Learning for Robust Reward Modeling in RLHF",
            "url": "https://icml.cc/virtual/2026/poster/65508"
          },
          {
            "title": "Factored Causal Representation Learning for Robust Reward Modeling in RLHF",
            "url": "https://www.arxiv.org/pdf/2601.21350"
          },
          {
            "title": "Beyond Reward Hacking: Causal Rewards for Large Language Model Alignment",
            "url": "https://arxiv.org/html/2501.09620v1"
          },
          {
            "title": "Robust Reward Modeling for Large Language Models via Causal Decomposition",
            "url": "https://arxiv.org/html/2604.13833"
          },
          {
            "title": "Robust Reward Modeling via Causal Rubrics",
            "url": "https://arxiv.org/pdf/2506.16507"
          },
          {
            "title": "Mitigating Reward Hacking in RLHF via Bayesian Non-negative Reward Modeling",
            "url": "https://arxiv.org/pdf/2602.10623"
          },
          {
            "title": "Counterfactual Reward Model Training for Bias Mitigation in Multimodal Reinforcement Learning",
            "url": "https://arxiv.org/html/2508.19567v1"
          }
        ]
      },
      "Based on the web search results, here's what I found about the paper arXiv:2601.21350:\n\n## Factored Causal Representation Learning for Robust Reward Modeling in RLHF\n\nA reliable reward model is essential for aligning large language models with human preferences through reinforcement learning from human feedback. However, standard reward models are susceptible to spurious features that are not causally related to human labels.\n\n**The Proposed Approach:**\n\nThe work proposes a factored representation learning framework that decomposes the model's contextual embedding into (1) causal factors that are sufficient for reward prediction and (2) non-causal factors that capture reward-irrelevant attributes such as length or sycophantic bias. The reward head is then constrained to depend only on the causal component. Additionally, an adversarial head is trained to predict reward from the non-causal factors, while applying gradient reversal to discourage them from encoding reward-relevant information.\n\n**Results:**\n\nExperiments on both mathematical and dialogue tasks demonstrate that the method learns more robust reward models and consistently improves downstream RLHF performance over state-of-the-art baselines.\n\nThe paper was published on arXiv on January 29, 2026, and has also been presented as a poster at ICML 2026."
    ],
    "durationSeconds": 6.858052718000006,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f74dd0a2-154f-4f7a-9d6c-083b3db428ff",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "75462fa2-385d-4000-b649-57c64df02312",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-27T08:44:55.068Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Pmh2nQVHmfT6xBGFustiJU`</summary>

```json
{
  "query": "\"When Reward Hacking Rebounds\" representation-level signals reward model arXiv:2604.01476 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae4a624c-ff42-43e0-9eb7-4d31907cecea",
  "isSidechain": false,
  "requestId": "req_011CbSnBHFQWVxPN3tjAbBy7",
  "type": "assistant",
  "uuid": "5766f35a-4b1f-4e33-9348-bb6b6b40b4c9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "75462fa2-385d-4000-b649-57c64df02312",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N6ZqCmnDNNtANYWnQLGVRf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 808,
      "cache_read_input_tokens": 28065,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 808,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 28065,
          "cache_creation_input_tokens": 808,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 808
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

_source line 42 · 2026-05-27T08:45:05.189Z_

<details><summary>↩ Tool result · `toolu_01Pmh2nQVHmfT6xBGFustiJU`</summary>

```text
Web search results for query: ""When Reward Hacking Rebounds" representation-level signals reward model arXiv:2604.01476 2026"

Links: [{"title":"When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals","url":"https://arxiv.org/pdf/2604.01476"},{"title":"When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals","url":"https://arxiv.org/html/2604.01476v1"},{"title":"Factored Causal Representation Learning for Robust Reward Modeling in RLHF","url":"https://arxiv.org/pdf/2601.21350"},{"title":"Monitoring Emergent Reward Hacking During Generation via Internal Activations","url":"https://arxiv.org/pdf/2603.04069"},{"title":"Mitigating Reward Hacking in RLHF via Bayesian Non-negative Reward Modeling","url":"https://arxiv.org/pdf/2602.10623"},{"title":"[2604.16242] Detecting and Suppressing Reward Hacking with Gradient Fingerprints","url":"https://arxiv.org/abs/2604.16242"}]

I found the paper! Here's what I discovered:

## "When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals"

The paper addresses how reinforcement learning for LLMs is vulnerable to reward hacking, where models exploit shortcuts to maximize reward without solving the intended task.

**Key Findings:**

The researchers systematically study this phenomenon in coding tasks using an environment-manipulation setting, where models can rewrite evaluator code to trivially pass tests without solving the task, as a controlled testbed.

Across both studied models, they identify a reproducible three-phase rebound pattern: models first attempt to rewrite the evaluator but fail, as their rewrites embed test cases their own solutions cannot pass. They then temporarily retreat to legitimate solving. When legitimate reward remains scarce, they rebound into successful hacking with qualitatively different strategies.

**Proposed Solution:**

Using representation engineering, they extract concept directions for shortcut, deception, and evaluation awareness from domain-general contrastive pairs and find that the shortcut direction tracks hacking behavior most closely, making it an effective representational proxy for detection.

They propose Advantage Modification, which integrates shortcut concept scores into GRPO advantage computation to penalize hacking rollouts before policy updates. Because the penalty is internalized into the training signal rather than applied only at inference time, Advantage Modification provides more robust suppression of hacking compared with generation-time activation steering.

The paper was submitted to arXiv on April 1, 2026, and is authored by Rui Wu and Ruixiang Tang from Rutgers University.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5766f35a-4b1f-4e33-9348-bb6b6b40b4c9",
  "isSidechain": false,
  "promptId": "18914ca9-b0a2-4983-9544-756340563499",
  "type": "user",
  "uuid": "223c5aca-d7c2-4465-82f4-f2705af6e2b4",
  "toolUseResult": {
    "query": "\"When Reward Hacking Rebounds\" representation-level signals reward model arXiv:2604.01476 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EPvMV9ULHEzQtyM4eSqNnH",
        "content": [
          {
            "title": "When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals",
            "url": "https://arxiv.org/pdf/2604.01476"
          },
          {
            "title": "When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals",
            "url": "https://arxiv.org/html/2604.01476v1"
          },
          {
            "title": "Factored Causal Representation Learning for Robust Reward Modeling in RLHF",
            "url": "https://arxiv.org/pdf/2601.21350"
          },
          {
            "title": "Monitoring Emergent Reward Hacking During Generation via Internal Activations",
            "url": "https://arxiv.org/pdf/2603.04069"
          },
          {
            "title": "Mitigating Reward Hacking in RLHF via Bayesian Non-negative Reward Modeling",
            "url": "https://arxiv.org/pdf/2602.10623"
          },
          {
            "title": "[2604.16242] Detecting and Suppressing Reward Hacking with Gradient Fingerprints",
            "url": "https://arxiv.org/abs/2604.16242"
          }
        ]
      },
      "I found the paper! Here's what I discovered:\n\n## \"When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals\"\n\nThe paper addresses how reinforcement learning for LLMs is vulnerable to reward hacking, where models exploit shortcuts to maximize reward without solving the intended task.\n\n**Key Findings:**\n\nThe researchers systematically study this phenomenon in coding tasks using an environment-manipulation setting, where models can rewrite evaluator code to trivially pass tests without solving the task, as a controlled testbed.\n\nAcross both studied models, they identify a reproducible three-phase rebound pattern: models first attempt to rewrite the evaluator but fail, as their rewrites embed test cases their own solutions cannot pass. They then temporarily retreat to legitimate solving. When legitimate reward remains scarce, they rebound into successful hacking with qualitatively different strategies.\n\n**Proposed Solution:**\n\nUsing representation engineering, they extract concept directions for shortcut, deception, and evaluation awareness from domain-general contrastive pairs and find that the shortcut direction tracks hacking behavior most closely, making it an effective representational proxy for detection.\n\nThey propose Advantage Modification, which integrates shortcut concept scores into GRPO advantage computation to penalize hacking rollouts before policy updates. Because the penalty is internalized into the training signal rather than applied only at inference time, Advantage Modification provides more robust suppression of hacking compared with generation-time activation steering.\n\nThe paper was submitted to arXiv on April 1, 2026, and is authored by Rui Wu and Ruixiang Tang from Rutgers University."
    ],
    "durationSeconds": 10.114313575000008,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "5766f35a-4b1f-4e33-9348-bb6b6b40b4c9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "75462fa2-385d-4000-b649-57c64df02312",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-27T08:45:33.277Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a solid understanding of the research landscape. Let me synthesize my findings and provide a thorough assessment of this proposal.

Let me organize my thoughts:

**Key findings from research:**

1. **"From Chains to DAGs"** (arXiv:2601.17593) - Confirms that LLM hidden states linearly encode DAG reasoning structure. This is a key premise of the proposal and it checks out.

2. **"Reward Under Attack"** (arXiv:2603.06621) - Confirms 43% stylistic shortcut problem, <4% accuracy with >0.9 PRM scores. The problem statement is well-grounded.
   
3. **CPMI** (arXiv:2604.10660) - Uses contrastive mutual information for PRM auto-labeling but lacks the premise dependency graphs that this proposal incorporates. 

4. **CRM** (ICLR 2026) - Conditions sequentially on preceding steps with point-wise prediction, whereas this proposal encodes relational structure directly in the embedding space, which is a meaningful distinction.

5. **GoV** (arXiv:2506.12509) - Applies DAG-based verification at inference time but doesn't integrate it into the training process, unlike what's being proposed here.

6. **Factored Causal Representation Learning** (arXiv:2601.21350, ICML 2026) - Still examining this work... is a VERY important related work that the proposal doesn't mention. It decomposes reward model embeddings into causal vs. non-causal factors. This is conceptually related to what PGCT does but at a different level of abstraction.

7. **"When Reward Hacking Rebounds"** (arXiv:2604.01476) - Uses representation engineering to detect and suppress reward hacking via representation-level signals. This is another important related work the proposal misses.

8. **PathFinder-PRM** (arXiv:2505.19706) - Error-aware hierarchical supervision, SOTA 67.7 on PRMBench.

9. **Graph of Verification** (arXiv:2506.12509) - DAG-based verification at inference time.

The core novelty here is genuinely compelling: using premise dependency DAGs to anchor contrastive training of PRMs is something no existing work attempts. The problem motivation around the consistency-causality gap is well-documented, and the representation-utilization gap framing makes the stakes clear. The experimental design looks solid and the related work analysis is thorough.

But there are some critical gaps to think through. First, I should check whether simpler alternatives could work—combining CRM's sequential conditioning with APRM's adversarial training might achieve similar results without the DAG extraction overhead, which could undermine the proposal's value proposition. Second, there are some significant related works missing from the landscape, particularly Factored Causal Representation Learning and the representation engineering approach in "When Reward Hacking Rebounds," both of which directly compete with the core narrative about reorganizing reward model representations.

Third, and most theoretically important: the claim about bridging the representation-utilization gap hinges on whether contrastive training actually activates the latent DAG structure or learns something entirely new. This distinction is crucial for the theoretical coherence of the proposal. Fourth, the significance framing could be sharpened—this isn't just about PRM robustness, it's potentially about a paradigm shift from point-wise to relational supervision in reward modeling. Finally, the entire method's robustness depends on >90% DAG extraction recall, which could be a serious vulnerability if the approach scales to more complex reasoning chains.

I need to think through whether these concerns are fatal or just require clarification in the proposal.

Here is the next thinking: I think there IS still discovery space, particularly in:

1. The missing related work (Factored Causal Rep Learning) that could threaten the novelty claim if not properly positioned
2. The "representation-utilization gap" narrative could be even sharper
3. The significance framing could be elevated from "better PRM" to "paradigm shift in supervision type"

Let me write up the analysis.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "223c5aca-d7c2-4465-82f4-f2705af6e2b4",
  "isSidechain": false,
  "requestId": "req_011CbSnCE7RcXzM8jWmrWrd1",
  "type": "assistant",
  "uuid": "c07261c8-e255-45b1-a27f-27792df2ea5f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "75462fa2-385d-4000-b649-57c64df02312",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017jeQWdu7THSNFxgyz62eRr",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 773,
      "cache_read_input_tokens": 28873,
      "output_tokens": 5060,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 773,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5060,
          "cache_read_input_tokens": 28873,
          "cache_creation_input_tokens": 773,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 773
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

_source line 44 · 2026-05-27T08:46:52.061Z_

Now I have sufficient research to make an informed assessment. Let me compile my analysis.

---

【状态】: 有发掘空间

【前置调研发现】

- **Factored Causal Representation Learning for Robust Reward Modeling in RLHF** (arXiv:2601.21350, ICML 2026): 将 reward model 的表征分解为 causal factors 与 non-causal factors，通过 gradient reversal 让 reward head 只依赖 causal component。**这篇论文 proposal 未引用，但与 PGCT 的核心叙事——"重组 reward model 的表征空间以增强鲁棒性"——高度重合**，是最大的 novelty 威胁。
- **When Reward Hacking Rebounds** (arXiv:2604.01476, April 2026): 通过 representation engineering 从 contrastive pairs 中提取 shortcut concept direction，作为 reward hacking 的表征级检测代理。**同样在表征层面对抗 reward hacking，且使用 contrastive pairs**，与 PGCT 的方法论有表面相似性。
- **Graph of Verification (GoV)** (arXiv:2506.12509, 2025): DAG 建模 + 拓扑排序 + 逐节点验证，inference-time 的 DAG 验证框架。验证了 DAG 结构在推理验证中的实际收益，支持 PGCT 的前提假设。
- **CPMI** (arXiv:2604.10660, April 2026): 用 contrastive pointwise mutual information 做 PRM 自动标注，节省 84% 数据构建时间。对比方向不同（标注效率 vs. 表征结构），但"contrastive + PRM"的关键词组合可能让审稿人混淆。
- **CRM** (ICLR 2026, arXiv:2509.26578): 将步骤 reward 条件化于前序步骤，引入时序因果关系。Proposal 已正确定位差异（point-wise prediction paradigm vs. relational embedding structure），但 CRM 在 RL closed-loop 上已展现出优于 standard PRM 的 robustness。
- **Robust Reward Modeling via Causal Rubrics (Crome)** (arXiv:2506.16507, June 2025): 基于显式因果模型的 reward modeling 框架，旨在解耦 reward 的真正因果驱动因素和虚假关联。又一个"因果 + reward model"的工作。
- **调研总结**: 当前领域有两条平行的研究主线在对抗 PRM 的 reward hacking 问题：(1) **表征工程路线**——在 embedding space 中分离/对齐因果 vs. 非因果因素（Factored Causal RL、Crome、Representation Rebound）；(2) **结构推理路线**——利用 DAG/图结构捕捉推理链的逻辑依赖（GoV、CRV、AgentEval）。PGCT 是**唯一一个处于这两条主线交叉点**的工作，但 proposal 目前未充分利用这个独特定位。

---

【发掘点 1】
- 维度: related work 差异化 / novelty 威胁
- 内容: **Proposal 遗漏了最关键的竞争者：Factored Causal Representation Learning (ICML 2026, arXiv:2601.21350)**。这篇论文同样在表征空间层面重组 reward model 以增强鲁棒性，使用 adversarial gradient reversal 将 causal 和 non-causal factors 分离。审稿人几乎必然会提出："PGCT 的 DAG-anchored contrastive learning 与 Factored Causal RL 的 causal/non-causal factorization 相比，增量价值是什么？" 建议在 Related Work 中显式对比：Factored Causal RL 的"因果性"是 domain-agnostic 的统计因果（基于 gradient reversal 学习哪些特征与 reward 无关），而 PGCT 的"因果性"是 domain-grounded 的逻辑因果（基于显式的 premise-conclusion dependency 结构）。这个区分非常关键——PGCT 的优势在于其结构化监督信号来自推理链的实际逻辑拓扑，而非纯统计分离。同时，"When Reward Hacking Rebounds" (arXiv:2604.01476) 也在表征层面使用 contrastive pairs 对抗 reward hacking，应纳入讨论。
- 价值: 防御 novelty 被挑战的最大风险点。如果审稿人发现这些高度相关的 ICML 2026 工作未被讨论，会严重质疑作者对 landscape 的了解。补上后反而能强化 PGCT 的独特定位。（命中 Related Work 差异化 + Novelty）
- 调研依据: Factored Causal Representation Learning (arXiv:2601.21350, ICML 2026) 和 When Reward Hacking Rebounds (arXiv:2604.01476)

【发掘点 2】
- 维度: significance 提升 / 核心 claim 强化
- 内容: **Proposal 的 framing 低估了自身的理论贡献层级。** 当前叙事是"改进 PRM 鲁棒性"，但真正的贡献应定位为 **"从 point-wise supervision 到 relational supervision 的范式转变"**。Proposal 已经提到了这个概念（"relational supervision"），但只是作为技术描述一笔带过，未上升为核心 significance claim。建议重新组织叙事结构：(1) 现有 PRM 训练（包括 APRM、CRM、PURE 等）的共同局限不是缺少某种特定技巧，而是它们都在 point-wise supervision paradigm 内做优化——每个步骤的 label 独立于其他步骤的逻辑结构；(2) PGCT 提出的 relational supervision（通过 InfoNCE 编码步骤间的拓扑关系）是对这个 paradigm 的突破；(3) 这解释了为什么 PGCT 与 CRM、APRM 等是正交且可组合的——它们解决的是不同层面的问题。这个 framing 把 PGCT 从"又一个 PRM 鲁棒性改进"提升为"PRM 训练范式的扩展"，显著提高 significance。
- 价值: 将 significance 从 incremental improvement 提升到 paradigmatic contribution，直接影响审稿人对论文重要性的判断。（命中 Significance）
- 调研依据: 基于领域整体趋势判断——调研发现所有现有 PRM 改进工作（APRM、CRM、PURE、CRA、PathFinder-PRM）确实都在 point-wise paradigm 内操作，无一例外。

【发掘点 3】
- 维度: novelty 锐化
- 内容: **"Representation-utilization gap" 这个概念是 proposal 最有价值的原创叙事资产，但目前论证链条有一个逻辑跳跃。** "From Chains to DAGs" 证明了 LLM hidden states 线性编码 DAG 结构 → "Reward Models Identify Consistency Not Causality" 证明 standard PRM training 未能利用这个结构 → **但缺失的环节是：PGCT 的 contrastive training 是"激活"了模型已有的潜在 DAG 表征，还是"重新学习"了一套新的结构表征？** 这两种叙事的 novelty 含金量不同。如果是前者（激活已有表征），理论意义更深——说明 contrastive training 是一种"表征唤醒"机制。建议在方法论中明确设计一个 probing 分析：训练前后用 "From Chains to DAGs" 的 linear probe 方法检测 PRM 内部 DAG 表征的变化（probing accuracy 是否提升、是否从中间层扩展到更多层）。这会让 "representation-utilization gap" 的叙事从一个比喻变成一个可验证的理论贡献。（注意：这不是在建议加实验——这是在强化核心 claim 的逻辑严密性，probing 分析是核心叙事的一部分，不是 ablation。）
- 价值: 将 "representation-utilization gap" 从一个修辞手法升级为可验证的理论 claim，大幅增加 novelty 的深度。审稿人读到这里会觉得这篇论文有真正的 insight，而不只是工程优化。（命中 Novelty）
- 调研依据: From Chains to DAGs (arXiv:2601.17593) 的 linear probing methodology

【发掘点 4】
- 维度: trivial alternative 威胁
- 内容: **必须正面回应一个 trivial alternative：如果直接用 "From Chains to DAGs" 的 linear probe 作为辅助 loss（让 PRM 中间层的 DAG probing accuracy 最大化），是否能达到类似效果？** 这种"probe-as-auxiliary-loss"的方法比 PGCT 的 contrastive pair construction + InfoNCE 要简单得多——无需 DAG extraction pipeline、无需 contrastive pair generation、无需 quality assurance。如果这个 trivial alternative 能 work，PGCT 的全部 engineering overhead 就不 justified。建议 proposal 明确论述为什么 probe-based auxiliary loss 不够：(a) linear probe 只优化局部层的 DAG 信息保留，不影响 cross-layer 的表征流动和最终 reward prediction；(b) contrastive training 直接在 reward-relevant 的 embedding space 中施加拓扑约束，是端到端的结构注入，而 probe loss 是间接的；(c) 可将 probe-as-auxiliary-loss 作为一个 baseline 来实证证明 contrastive approach 的优势。如果 proposal 不主动讨论这个 alternative，审稿人一定会提出。
- 价值: 预判并化解审稿人最可能的 "why not just do X instead" 质疑。如果回应得好，反而能加深审稿人对 contrastive 方法设计动机的理解。（命中 Novelty + Significance）
- 调研依据: From Chains to DAGs (arXiv:2601.17593) 的 linear probe methodology + 基于领域整体趋势判断（auxiliary probing loss 是表征学习中常见的简单替代方案）

【发掘点 5】
- 维度: 核心 claim 强化 / significance 提升
- 内容: **Proposal 处于表征工程路线与结构推理路线的唯一交叉点，但未将此定位为显式贡献。** 调研显示当前领域有两条清晰的并行主线：(1) 表征空间重组（Factored Causal RL、Crome、Representation Rebound）；(2) 图结构推理验证（GoV、CRV、AgentEval）。PGCT 是第一个将图结构信号注入表征训练的工作——**不是在 inference time 用图结构做验证（GoV/CRV），也不是用 domain-agnostic 的统计方法做表征分离（Factored Causal RL），而是用 domain-grounded 的逻辑拓扑直接塑造表征空间。** 这个"交叉点"定位如果在 introduction 中明确表述，可以一句话回答"与现有工作的本质区别是什么"——这是审稿人最需要的一句话。建议在 intro 或 contribution section 加一句类似："While existing approaches either reorganize representation space without domain-specific logical structure (Factored Causal RL) or leverage graph structure only at inference time (GoV, CRV), PGCT is the first to inject premise-dependency topology directly into training-time representation learning."
- 价值: 一句话完成与两大主线所有工作的差异化定位，让审稿人瞬间理解 PGCT 的 unique contribution。（命中 Related Work 差异化 + Significance）
- 调研依据: Factored Causal RL (arXiv:2601.21350), GoV (arXiv:2506.12509), CRV (arXiv:2510.09312), When Reward Hacking Rebounds (arXiv:2604.01476)

---

Sources:
- [Factored Causal Representation Learning for Robust Reward Modeling in RLHF](https://arxiv.org/abs/2601.21350)
- [When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals](https://arxiv.org/abs/2604.01476)
- [Graph of Verification: Structured Verification of LLM Reasoning with Directed Acyclic Graphs](https://arxiv.org/abs/2506.12509)
- [Efficient Process Reward Modeling via Contrastive Mutual Information](https://arxiv.org/abs/2604.10660)
- [Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning](https://arxiv.org/abs/2509.26578)
- [Robust Reward Modeling via Causal Rubrics](https://arxiv.org/abs/2506.16507)
- [From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs](https://arxiv.org/abs/2601.17593)
- [Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models](https://arxiv.org/abs/2603.06621)
- [Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision (PathFinder-PRM)](https://arxiv.org/abs/2505.19706)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c07261c8-e255-45b1-a27f-27792df2ea5f",
  "isSidechain": false,
  "requestId": "req_011CbSnCE7RcXzM8jWmrWrd1",
  "type": "assistant",
  "uuid": "8edb56da-b731-4609-9096-33ddf8dc0573",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "75462fa2-385d-4000-b649-57c64df02312",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017jeQWdu7THSNFxgyz62eRr",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 773,
      "cache_read_input_tokens": 28873,
      "output_tokens": 5060,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 773,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5060,
          "cache_read_input_tokens": 28873,
          "cache_creation_input_tokens": 773,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 773
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

_source line 45_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Premise-Graph Contrastive Training for Logic-Grounded Process Reward Models  ## Core Problem  Current process reward models detect consistency rather than causality. \"Reward Models Identify Consiste…",
  "leafUuid": "8edb56da-b731-4609-9096-33ddf8dc0573",
  "sessionId": "75462fa2-385d-4000-b649-57c64df02312"
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "ai-title",
  "aiTitle": "Premise-Graph contrastive training for process reward models",
  "sessionId": "75462fa2-385d-4000-b649-57c64df02312"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Premise-Graph Contrastive Training for Logic-Grounded Process Reward Models  ## Core Problem  Current process reward models detect consistency rather than causality. \"Reward Models Identify Consiste…",
  "leafUuid": "8edb56da-b731-4609-9096-33ddf8dc0573",
  "sessionId": "75462fa2-385d-4000-b649-57c64df02312"
}
```

---

### Runtime record

_source line 48_

```json
{
  "type": "ai-title",
  "aiTitle": "Premise-Graph contrastive training for process reward models",
  "sessionId": "75462fa2-385d-4000-b649-57c64df02312"
}
```

---
