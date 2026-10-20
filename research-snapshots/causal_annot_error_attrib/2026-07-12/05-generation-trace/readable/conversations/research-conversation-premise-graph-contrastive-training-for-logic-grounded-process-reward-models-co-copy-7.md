# Research conversation: Premise-Graph Contrastive Training for Logic-Grounded Process Reward Models ## Core Problem Current process reward model

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 43
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-2/6ab36dcb-fa57-4a2b-87cc-9d068208d199.jsonl`
- **Structured JSON:** [`3fa4d106559f1bb60d66.json`](../../sessions/3f/3fa4d106559f1bb60d66.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-27T08:54:31.945Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T08:54:31.945Z",
  "sessionId": "6ab36dcb-fa57-4a2b-87cc-9d068208d199",
  "content": "# Premise-Graph Contrastive Training for Logic-Grounded Process Reward Models\n\n## Core Problem\n\nCurrent process reward models detect consistency rather than causality. \"Reward Models Identify Consistency, Not Causality\" (arXiv:2502.14619, Feb 2025) established that PRMs verify surface-level coherence between steps — not whether each step logically follows from its premises. \"Reward Under Attack\" (arXiv:2603.06621, Feb 2026) quantified the consequences: 43% of PRM reward gains stem from stylistic shortcuts, and RL-trained policies achieve >0.9 PRM scores but <4% actual accuracy. The root cause is that standard PRM training provides only point-wise step-correctness supervision, which is blind to the logical dependency structure connecting reasoning steps. Can we train PRMs whose representations explicitly encode premise-dependency awareness rather than mere surface consistency?\n\n## Research Opportunity and Key Insight\n\nA critical representation-utilization gap exists in current PRMs. \"From Chains to DAGs\" (arXiv:2601.17593, Jan 2026) proved that LLM hidden states already linearly encode DAG reasoning structure — node depth, pairwise distance, and adjacency are recoverable from intermediate layers via lightweight probes. Yet standard PRM training fails to channel this latent structural knowledge into reward prediction (arXiv:2502.14619). PARC/PERL (ICML 2025, arXiv:2502.02362) demonstrated that premise dependency links are extractable at >90% recall (on 70B+ models), improving error detection by 6-16%. DAG-Math (arXiv:2510.19842, 2025) and ProofFlow (arXiv:2510.15981, 2025) further established feasibility of dependency graph extraction at scale.\n\nOur key insight: contrastive training anchored to premise dependency DAGs can bridge this representation-utilization gap. By constructing training pairs that hold surface form constant while varying logical structure (and vice versa), we force the PRM's embedding space to explicitly encode premise-dependency relationships — activating structural representations the model already possesses but that point-wise BCE training leaves dormant. This constitutes a shift from point-wise supervision (each step independently correct/incorrect) to relational supervision (structural relationships between steps encoded in representation space). An alternative approach — using linear probes as auxiliary loss to directly maximize DAG-structure recovery in hidden states — would only optimize local-layer information retention without affecting cross-layer representation flow or end-to-end reward prediction; contrastive training directly constrains the reward-relevant embedding space, providing end-to-end structural injection.\n\n## Research Landscape\n\n**PRM robustness: existing defenses.** \"Reward Under Attack\" (arXiv:2603.06621) established the three-tier diagnostic: static perturbation exploitability, adversarial token-level attacks, and RL-induced reward hacking. Defenses include CRA (Aug 2025, arXiv:2508.04216, post-hoc SAE correction), APRM (Nov 2025, arXiv:2511.22888, adversarial harder negatives, +5.3pp OOD), CRM (ICLR 2026, arXiv:2509.26578, sequential conditioning), and PURE (NeurIPS 2025, arXiv:2504.15275, min-form credit aggregation). None uses explicit logical dependency structure in PRM training. APRM's adversarial negatives improve the single-step classification decision boundary but remain domain-agnostic — the PRM learns to resist specific patterns without understanding why they are wrong, leaving it vulnerable to novel attacks (cat-and-mouse problem). PGCT instead reorganizes the PRM's representation space around premise-dependency topology.\n\n**Representation-level robustness.** Factored Causal Representation Learning (ICML 2026, arXiv:2601.21350) decomposes reward model embeddings into causal/non-causal factors via gradient reversal. \"When Reward Hacking Rebounds\" (arXiv:2604.01476, April 2026) extracts shortcut concept directions from contrastive pairs via representation engineering. Both operate in representation space but use domain-agnostic statistical separation (gradient reversal, concept directions). PGCT differs fundamentally: its structural prior is domain-grounded — premise dependency DAGs extracted from mathematical reasoning chains — rather than learned statistical factors. This provides interpretable, verifiable structural constraints rather than latent factor separation.\n\n**Reasoning-enhanced PRMs.** R-PRM (arXiv:2503.21295, 2025) augments PRMs with reasoning-driven critique (+11.9 F1 on ProcessBench, +8.5 on PRMBench). GenPRM (AAAI 2026, arXiv:2504.00891) uses generative CoT + code verification. ThinkPRM (arXiv:2504.16828, 2025) achieves strong results with only 1% PRM800K labels via generative verification. These enhance inference-time reasoning. PGCT is orthogonal: it improves training-time representation learning, and could serve as a backbone for generative verification methods.\n\n**Graph structure for verification.** CRV (ICLR 2026, arXiv:2510.09312) verifies reasoning via attribution graph structural fingerprints (white-box, inference-time). GoV decomposes reasoning into DAGs for training-free verification. AgentEval (arXiv:2604.23581, 2026) shows DAG-based dependency modeling yields +22pp failure detection recall. Multiple independent lines confirm graph structure carries powerful verification signal. **Existing approaches either reorganize representation space without domain-specific logical structure (Factored Causal RL) or leverage graph structure only at inference time (GoV, CRV). PGCT is the first to inject premise-dependency topology directly into training-time representation learning.**\n\n**Concurrent contrastive/graph approaches.** CPMI (arXiv:2604.10660, April 2026) uses contrastive MI for PRM auto-labeling without dependency graphs. RewardFlow (arXiv:2603.18859, March 2026) propagates rewards over state-transition graphs without contrastive training. Thought-Path Contrastive Learning (AAAI 2025, arXiv:2409.14495) constructs premise-oriented contrastive examples for logical reading comprehension but operates on propositional-level pairs, not multi-step mathematical DAGs, and targets reading accuracy rather than PRM robustness.\n\n**Performance gap.** Best open-source PRM on PRMBench: 67.7 (PathFinder-PRM-7B, arXiv:2505.19706) vs. 83.8 human ceiling.\n\n## Proposed Approach\n\n**DAG extraction.** Extract premise dependency DAGs from mathematical reasoning chains using PARC's method with Qwen2.5-72B-Instruct (targeting >90% recall per PERL results on 70B-class models; ICML 2025, arXiv:2502.02362). Each reasoning step is a node; directed edges encode \"step j uses the result of step i as a premise.\"\n\n**Contrastive pair construction.** Two types of structure-aware pairs: (1) Graph-preserving surface perturbations (rephrased steps, identical DAG topology) as positives; (2) Graph-breaking fluent perturbations (severed premise links, dangling references, logically invalid steps maintaining surface fluency) as hard negatives. Difficulty-aware construction: score all hard negatives with a baseline PRM to ensure sufficient proportion (>30%) of genuinely hard cases (baseline PRM score >0.7). Quality assurance: re-extract DAGs from generated pairs to verify topology preservation/breaking; stratified human audit (~1000 pairs across math subdomains × DAG complexity × difficulty levels) with thresholds (topology preservation ≥90% for positives, premise-link corruption verification ≥85% for negatives) and inter-annotator agreement (2 annotators, Cohen's κ on ~200-pair overlap). Per-difficulty DAG extraction quality audit (easy/medium/hard/competition).\n\n**Dual objective training.** Qwen2.5-Math-7B-Instruct-based PRM with: (a) standard step-correctness BCE loss (point-wise supervision), and (b) graph-contrastive InfoNCE loss over DAG-anchored step embeddings (relational supervision — \"same DAG topology → nearby embeddings, different topology → distant embeddings\"). This complements CRM (ICLR 2026, arXiv:2509.26578), which conditions sequentially on preceding steps but operates in point-wise prediction paradigm without encoding relational structure in embedding space.\n\n**Scope clarification.** PGCT trains two complementary capabilities: (1) structural dependency sensitivity — detecting whether premise links between steps are correctly maintained (via DAG topology contrastive learning), and (2) partial semantic inference validity — detecting logically invalid reasoning preserving surface fluency (via graph-breaking hard negatives). We claim premise-dependency awareness substantially narrows the consistency-causality gap, not full logical causality verification.\n\n**Data.** PRM800K + Math-Shepherd (~300K solutions) + ~600K contrastive pairs via LLM paraphrasing (7B/32B for generation, 72B for quality verification) and targeted premise-link corruption.\n\n## Evaluation Plan\n\n**Benchmarks (5-tier, with ID/OOD split):**\n1. **Step-level error detection**: PRMBench (ACL 2025, arXiv:2501.03124) with per-error-category breakdown (soundness/sensitivity/simplicity; redundancy, circular logic, step inconsistency, domain inconsistency, deceptive logical steps), targeting >70 overall (vs. 67.7 SOTA). ProcessBench (arXiv:2412.06559) with per-difficulty-level F1.\n2. **Downstream best-of-N reranking**: ID: MATH500, GSM8K; OOD: AIME 2024, AMC. N ∈ {8, 16, 64}. Report prm@N accuracy with ID/OOD breakdown.\n3. **Adversarial robustness**: PRM-BiasBench and perturbation suite from \"Reward Under Attack\" (arXiv:2603.06621).\n4. **RL closed-loop reward hacking**: GRPO training of Qwen2.5-Math-7B-Instruct using PGCT-PRM vs. baseline PRMs as reward. 3000-5000 steps, checkpoint every 200 steps, evaluate on MATH and AIME. Metrics: hacking gap = (PRM score improvement) − (accuracy improvement); reward-accuracy Pearson r with 95% CI from 3 seeds; late-stage divergence ratio (final 30% training).\n5. **Representation analysis**: (a) Linear probing (per \"From Chains to DAGs\" methodology, arXiv:2601.17593): compare DAG structure encoding (node depth, pairwise distance, adjacency) in PGCT-PRM vs. standard PRM hidden states, layer by layer. (b) t-SNE/UMAP visualization of step embeddings: graph-preserving pairs should cluster, graph-breaking pairs should separate. (c) Quantitative topology metric: mean cosine similarity of graph-preserving pairs vs. graph-breaking pairs.\n\n**Baselines (6 tiers):**\n1. Standard PRM: Qwen2.5-Math-PRM-7B (same base model)\n2. Robustness-focused: APRM (arXiv:2511.22888), CRA (arXiv:2508.04216)\n3. Architecture-level: CRM (ICLR 2026, arXiv:2509.26578), PURE (NeurIPS 2025, arXiv:2504.15275)\n4. Contrastive/concurrent: CPMI (arXiv:2604.10660)\n5. Error-aware: PathFinder-PRM-7B (arXiv:2505.19706)\n6. Reasoning-enhanced: R-PRM (arXiv:2503.21295), GenPRM-7B (AAAI 2026, arXiv:2504.00891), ThinkPRM-7B (arXiv:2504.16828) — all under fixed inference-compute budget for fair comparison; unrestricted comparison also reported\n- Data-matched control: ~900K total samples, contrastive pairs replaced with step-correctness annotations, standard BCE\n- Compute-matched control: equal total training FLOPs including DAG extraction overhead\n\n**Ablations (8 variants):**\n- A1: Remove InfoNCE loss → isolate contrastive learning contribution\n- A2: Remove step-correctness loss → test contrastive learning standalone\n- A3: Random perturbation replacing DAG-aware perturbation → **critical: isolate DAG structure contribution**\n- A4: Only positives (no graph-breaking negatives)\n- A5: Only negatives (no graph-preserving positives)\n- A6: Loss weighting λ ∈ {0.1, 0.3, 0.5, 0.7, 1.0}\n- A7: DAG noise injection at 5%/10%/15%/20%\n- A8: DAG extraction model scale: 7B / 32B / 72B extractors → practical viability curve\n\n## Key References\n\n- Reward Under Attack (arXiv 2026, arXiv:2603.06621)\n- Reward Models Identify Consistency, Not Causality (arXiv 2025, arXiv:2502.14619)\n- PARC/PERL (ICML 2025, arXiv:2502.02362)\n- From Chains to DAGs (arXiv 2026, arXiv:2601.17593)\n- DAG-Math (arXiv 2025, arXiv:2510.19842)\n- ProofFlow (arXiv 2025, arXiv:2510.15981)\n- CRA (arXiv 2025, arXiv:2508.04216)\n- APRM (arXiv 2025, arXiv:2511.22888)\n- CRM (ICLR 2026, arXiv:2509.26578)\n- PURE (NeurIPS 2025, arXiv:2504.15275)\n- GenPRM (AAAI 2026, arXiv:2504.00891)\n- AgentEval (arXiv 2026, arXiv:2604.23581)\n- PRMBench (ACL 2025, arXiv:2501.03124)\n- ProcessBench (arXiv 2024, arXiv:2412.06559)\n- CPMI (arXiv 2026, arXiv:2604.10660)\n- RewardFlow (arXiv 2026, arXiv:2603.18859)\n- PathFinder-PRM (arXiv 2025, arXiv:2505.19706)\n- Thought-Path Contrastive Learning (AAAI 2025, arXiv:2409.14495)\n- ThinkPRM (arXiv 2025, arXiv:2504.16828)\n- CRV (ICLR 2026, arXiv:2510.09312)\n- R-PRM (arXiv 2025, arXiv:2503.21295)\n- Factored Causal Representation Learning (ICML 2026, arXiv:2601.21350)\n- When Reward Hacking Rebounds (arXiv 2026, arXiv:2604.01476)\n\n## Resource Estimate\n\n- **manual**: gpu_hours: 1600-2200 A100-hours (DAG extraction 72B: ~350h, pair generation 7B/32B + quality verification 72B: ~300h, PRM training + 8 ablations: ~550h, baseline reproduction/evaluation: ~150h, RL closed-loop × 3 seeds: ~250h, best-of-N + adversarial + representation analysis: ~100h), timeline: 18-22 weeks for 2-3 researchers, estimated_gpu_cost: $4,800-$6,600 at $3/hr A100 spot pricing\n- **human_in_loop**: gpu_hours: 1200-1600 A100-hours (~30% reduction from automated quality triage), timeline: 13-17 weeks for 2 researchers, claude_api_cost: $800-$1,200, estimated_gpu_cost: $3,600-$4,800\n- **auto_research**: gpu_hours: 1800-2500 A100-hours (parallel sweeps), timeline: 9-12 weeks automated, claude_api_cost: $1,500-$2,000, estimated_gpu_cost: $5,400-$7,500, speed_bottleneck: DAG extraction quality validation per math subdomain requires serial human spot-checks"
}
```

---

### Runtime record

_source line 2 · 2026-05-27T08:54:31.950Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T08:54:31.950Z",
  "sessionId": "6ab36dcb-fa57-4a2b-87cc-9d068208d199"
}
```

---

## Round 1

41 recorded events

### User

_source line 3 · 2026-05-27T08:54:32.068Z_

# Premise-Graph Contrastive Training for Logic-Grounded Process Reward Models

## Core Problem

Current process reward models detect consistency rather than causality. "Reward Models Identify Consistency, Not Causality" (arXiv:2502.14619, Feb 2025) established that PRMs verify surface-level coherence between steps — not whether each step logically follows from its premises. "Reward Under Attack" (arXiv:2603.06621, Feb 2026) quantified the consequences: 43% of PRM reward gains stem from stylistic shortcuts, and RL-trained policies achieve >0.9 PRM scores but <4% actual accuracy. The root cause is that standard PRM training provides only point-wise step-correctness supervision, which is blind to the logical dependency structure connecting reasoning steps. Can we train PRMs whose representations explicitly encode premise-dependency awareness rather than mere surface consistency?

## Research Opportunity and Key Insight

A critical representation-utilization gap exists in current PRMs. "From Chains to DAGs" (arXiv:2601.17593, Jan 2026) proved that LLM hidden states already linearly encode DAG reasoning structure — node depth, pairwise distance, and adjacency are recoverable from intermediate layers via lightweight probes. Yet standard PRM training fails to channel this latent structural knowledge into reward prediction (arXiv:2502.14619). PARC/PERL (ICML 2025, arXiv:2502.02362) demonstrated that premise dependency links are extractable at >90% recall (on 70B+ models), improving error detection by 6-16%. DAG-Math (arXiv:2510.19842, 2025) and ProofFlow (arXiv:2510.15981, 2025) further established feasibility of dependency graph extraction at scale.

Our key insight: contrastive training anchored to premise dependency DAGs can bridge this representation-utilization gap. By constructing training pairs that hold surface form constant while varying logical structure (and vice versa), we force the PRM's embedding space to explicitly encode premise-dependency relationships — activating structural representations the model already possesses but that point-wise BCE training leaves dormant. This constitutes a shift from point-wise supervision (each step independently correct/incorrect) to relational supervision (structural relationships between steps encoded in representation space). An alternative approach — using linear probes as auxiliary loss to directly maximize DAG-structure recovery in hidden states — would only optimize local-layer information retention without affecting cross-layer representation flow or end-to-end reward prediction; contrastive training directly constrains the reward-relevant embedding space, providing end-to-end structural injection.

## Research Landscape

**PRM robustness: existing defenses.** "Reward Under Attack" (arXiv:2603.06621) established the three-tier diagnostic: static perturbation exploitability, adversarial token-level attacks, and RL-induced reward hacking. Defenses include CRA (Aug 2025, arXiv:2508.04216, post-hoc SAE correction), APRM (Nov 2025, arXiv:2511.22888, adversarial harder negatives, +5.3pp OOD), CRM (ICLR 2026, arXiv:2509.26578, sequential conditioning), and PURE (NeurIPS 2025, arXiv:2504.15275, min-form credit aggregation). None uses explicit logical dependency structure in PRM training. APRM's adversarial negatives improve the single-step classification decision boundary but remain domain-agnostic — the PRM learns to resist specific patterns without understanding why they are wrong, leaving it vulnerable to novel attacks (cat-and-mouse problem). PGCT instead reorganizes the PRM's representation space around premise-dependency topology.

**Representation-level robustness.** Factored Causal Representation Learning (ICML 2026, arXiv:2601.21350) decomposes reward model embeddings into causal/non-causal factors via gradient reversal. "When Reward Hacking Rebounds" (arXiv:2604.01476, April 2026) extracts shortcut concept directions from contrastive pairs via representation engineering. Both operate in representation space but use domain-agnostic statistical separation (gradient reversal, concept directions). PGCT differs fundamentally: its structural prior is domain-grounded — premise dependency DAGs extracted from mathematical reasoning chains — rather than learned statistical factors. This provides interpretable, verifiable structural constraints rather than latent factor separation.

**Reasoning-enhanced PRMs.** R-PRM (arXiv:2503.21295, 2025) augments PRMs with reasoning-driven critique (+11.9 F1 on ProcessBench, +8.5 on PRMBench). GenPRM (AAAI 2026, arXiv:2504.00891) uses generative CoT + code verification. ThinkPRM (arXiv:2504.16828, 2025) achieves strong results with only 1% PRM800K labels via generative verification. These enhance inference-time reasoning. PGCT is orthogonal: it improves training-time representation learning, and could serve as a backbone for generative verification methods.

**Graph structure for verification.** CRV (ICLR 2026, arXiv:2510.09312) verifies reasoning via attribution graph structural fingerprints (white-box, inference-time). GoV decomposes reasoning into DAGs for training-free verification. AgentEval (arXiv:2604.23581, 2026) shows DAG-based dependency modeling yields +22pp failure detection recall. Multiple independent lines confirm graph structure carries powerful verification signal. **Existing approaches either reorganize representation space without domain-specific logical structure (Factored Causal RL) or leverage graph structure only at inference time (GoV, CRV). PGCT is the first to inject premise-dependency topology directly into training-time representation learning.**

**Concurrent contrastive/graph approaches.** CPMI (arXiv:2604.10660, April 2026) uses contrastive MI for PRM auto-labeling without dependency graphs. RewardFlow (arXiv:2603.18859, March 2026) propagates rewards over state-transition graphs without contrastive training. Thought-Path Contrastive Learning (AAAI 2025, arXiv:2409.14495) constructs premise-oriented contrastive examples for logical reading comprehension but operates on propositional-level pairs, not multi-step mathematical DAGs, and targets reading accuracy rather than PRM robustness.

**Performance gap.** Best open-source PRM on PRMBench: 67.7 (PathFinder-PRM-7B, arXiv:2505.19706) vs. 83.8 human ceiling.

## Proposed Approach

**DAG extraction.** Extract premise dependency DAGs from mathematical reasoning chains using PARC's method with Qwen2.5-72B-Instruct (targeting >90% recall per PERL results on 70B-class models; ICML 2025, arXiv:2502.02362). Each reasoning step is a node; directed edges encode "step j uses the result of step i as a premise."

**Contrastive pair construction.** Two types of structure-aware pairs: (1) Graph-preserving surface perturbations (rephrased steps, identical DAG topology) as positives; (2) Graph-breaking fluent perturbations (severed premise links, dangling references, logically invalid steps maintaining surface fluency) as hard negatives. Difficulty-aware construction: score all hard negatives with a baseline PRM to ensure sufficient proportion (>30%) of genuinely hard cases (baseline PRM score >0.7). Quality assurance: re-extract DAGs from generated pairs to verify topology preservation/breaking; stratified human audit (~1000 pairs across math subdomains × DAG complexity × difficulty levels) with thresholds (topology preservation ≥90% for positives, premise-link corruption verification ≥85% for negatives) and inter-annotator agreement (2 annotators, Cohen's κ on ~200-pair overlap). Per-difficulty DAG extraction quality audit (easy/medium/hard/competition).

**Dual objective training.** Qwen2.5-Math-7B-Instruct-based PRM with: (a) standard step-correctness BCE loss (point-wise supervision), and (b) graph-contrastive InfoNCE loss over DAG-anchored step embeddings (relational supervision — "same DAG topology → nearby embeddings, different topology → distant embeddings"). This complements CRM (ICLR 2026, arXiv:2509.26578), which conditions sequentially on preceding steps but operates in point-wise prediction paradigm without encoding relational structure in embedding space.

**Scope clarification.** PGCT trains two complementary capabilities: (1) structural dependency sensitivity — detecting whether premise links between steps are correctly maintained (via DAG topology contrastive learning), and (2) partial semantic inference validity — detecting logically invalid reasoning preserving surface fluency (via graph-breaking hard negatives). We claim premise-dependency awareness substantially narrows the consistency-causality gap, not full logical causality verification.

**Data.** PRM800K + Math-Shepherd (~300K solutions) + ~600K contrastive pairs via LLM paraphrasing (7B/32B for generation, 72B for quality verification) and targeted premise-link corruption.

## Evaluation Plan

**Benchmarks (5-tier, with ID/OOD split):**
1. **Step-level error detection**: PRMBench (ACL 2025, arXiv:2501.03124) with per-error-category breakdown (soundness/sensitivity/simplicity; redundancy, circular logic, step inconsistency, domain inconsistency, deceptive logical steps), targeting >70 overall (vs. 67.7 SOTA). ProcessBench (arXiv:2412.06559) with per-difficulty-level F1.
2. **Downstream best-of-N reranking**: ID: MATH500, GSM8K; OOD: AIME 2024, AMC. N ∈ {8, 16, 64}. Report prm@N accuracy with ID/OOD breakdown.
3. **Adversarial robustness**: PRM-BiasBench and perturbation suite from "Reward Under Attack" (arXiv:2603.06621).
4. **RL closed-loop reward hacking**: GRPO training of Qwen2.5-Math-7B-Instruct using PGCT-PRM vs. baseline PRMs as reward. 3000-5000 steps, checkpoint every 200 steps, evaluate on MATH and AIME. Metrics: hacking gap = (PRM score improvement) − (accuracy improvement); reward-accuracy Pearson r with 95% CI from 3 seeds; late-stage divergence ratio (final 30% training).
5. **Representation analysis**: (a) Linear probing (per "From Chains to DAGs" methodology, arXiv:2601.17593): compare DAG structure encoding (node depth, pairwise distance, adjacency) in PGCT-PRM vs. standard PRM hidden states, layer by layer. (b) t-SNE/UMAP visualization of step embeddings: graph-preserving pairs should cluster, graph-breaking pairs should separate. (c) Quantitative topology metric: mean cosine similarity of graph-preserving pairs vs. graph-breaking pairs.

**Baselines (6 tiers):**
1. Standard PRM: Qwen2.5-Math-PRM-7B (same base model)
2. Robustness-focused: APRM (arXiv:2511.22888), CRA (arXiv:2508.04216)
3. Architecture-level: CRM (ICLR 2026, arXiv:2509.26578), PURE (NeurIPS 2025, arXiv:2504.15275)
4. Contrastive/concurrent: CPMI (arXiv:2604.10660)
5. Error-aware: PathFinder-PRM-7B (arXiv:2505.19706)
6. Reasoning-enhanced: R-PRM (arXiv:2503.21295), GenPRM-7B (AAAI 2026, arXiv:2504.00891), ThinkPRM-7B (arXiv:2504.16828) — all under fixed inference-compute budget for fair comparison; unrestricted comparison also reported
- Data-matched control: ~900K total samples, contrastive pairs replaced with step-correctness annotations, standard BCE
- Compute-matched control: equal total training FLOPs including DAG extraction overhead

**Ablations (8 variants):**
- A1: Remove InfoNCE loss → isolate contrastive learning contribution
- A2: Remove step-correctness loss → test contrastive learning standalone
- A3: Random perturbation replacing DAG-aware perturbation → **critical: isolate DAG structure contribution**
- A4: Only positives (no graph-breaking negatives)
- A5: Only negatives (no graph-preserving positives)
- A6: Loss weighting λ ∈ {0.1, 0.3, 0.5, 0.7, 1.0}
- A7: DAG noise injection at 5%/10%/15%/20%
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
- Factored Causal Representation Learning (ICML 2026, arXiv:2601.21350)
- When Reward Hacking Rebounds (arXiv 2026, arXiv:2604.01476)

## Resource Estimate

- **manual**: gpu_hours: 1600-2200 A100-hours (DAG extraction 72B: ~350h, pair generation 7B/32B + quality verification 72B: ~300h, PRM training + 8 ablations: ~550h, baseline reproduction/evaluation: ~150h, RL closed-loop × 3 seeds: ~250h, best-of-N + adversarial + representation analysis: ~100h), timeline: 18-22 weeks for 2-3 researchers, estimated_gpu_cost: $4,800-$6,600 at $3/hr A100 spot pricing
- **human_in_loop**: gpu_hours: 1200-1600 A100-hours (~30% reduction from automated quality triage), timeline: 13-17 weeks for 2 researchers, claude_api_cost: $800-$1,200, estimated_gpu_cost: $3,600-$4,800
- **auto_research**: gpu_hours: 1800-2500 A100-hours (parallel sweeps), timeline: 9-12 weeks automated, claude_api_cost: $1,500-$2,000, estimated_gpu_cost: $5,400-$7,500, speed_bottleneck: DAG extraction quality validation per math subdomain requires serial human spot-checks

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "d8b72561-4b7c-4874-99b3-296be6c30c18",
  "type": "user",
  "uuid": "eed3a9bc-5ad4-4c93-90e4-655635a2bb7a",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6ab36dcb-fa57-4a2b-87cc-9d068208d199",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-27T08:54:32.067Z_

```json
{
  "parentUuid": "eed3a9bc-5ad4-4c93-90e4-655635a2bb7a",
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
  "uuid": "8c26a24a-5132-4137-b023-57969a3ff689",
  "timestamp": "2026-05-27T08:54:32.067Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6ab36dcb-fa57-4a2b-87cc-9d068208d199",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-27T08:54:32.067Z_

```json
{
  "parentUuid": "8c26a24a-5132-4137-b023-57969a3ff689",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "4a49dac3-648f-4629-8cce-7c43e09dfda3",
  "timestamp": "2026-05-27T08:54:32.067Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6ab36dcb-fa57-4a2b-87cc-9d068208d199",
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
  "lastPrompt": "# Premise-Graph Contrastive Training for Logic-Grounded Process Reward Models  ## Core Problem  Current process reward models detect consistency rather than causality. \"Reward Models Identify Consiste…",
  "leafUuid": "4a49dac3-648f-4629-8cce-7c43e09dfda3",
  "sessionId": "6ab36dcb-fa57-4a2b-87cc-9d068208d199"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Premise-graph contrastive training for process reward models",
  "sessionId": "6ab36dcb-fa57-4a2b-87cc-9d068208d199"
}
```

---

### Assistant

_source line 8 · 2026-05-27T08:54:39.036Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to act as the "补救 agent" (remediation agent) and analyze this proposal's experimental design and technical execution completeness. I need to:

1. First do WebSearch to understand the current experimental standards in this field
2. Then evaluate: baseline coverage, experimental design, evaluation metrics, ablation design, and feasibility
3. Output in the specified format

Let me start by doing the prerequisite research. I need to search for:
1. Recent PRM papers and their experimental setups
2. Current SOTA baselines for process reward models
3. Standard benchmarks for PRM evaluation


4. How contrastive learning is being applied to reasoning verification

Let me search for these topics.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a49dac3-648f-4629-8cce-7c43e09dfda3",
  "isSidechain": false,
  "requestId": "req_011CbSnv1wc7L4KBGP2vcroh",
  "type": "assistant",
  "uuid": "9ab7bd42-cfe2-4ae4-8392-9d3b263d0ad8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6ab36dcb-fa57-4a2b-87cc-9d068208d199",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014mBbkBaaaT8mECQxnetD9R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5455,
      "cache_read_input_tokens": 14080,
      "output_tokens": 280,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5455,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 280,
          "cache_read_input_tokens": 14080,
          "cache_creation_input_tokens": 5455,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5455
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

_source line 9 · 2026-05-27T08:54:39.675Z_

I'll start by doing the required prerequisite research to understand current experimental standards in the PRM field before making any recommendations. Let me search for several key topics in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ab7bd42-cfe2-4ae4-8392-9d3b263d0ad8",
  "isSidechain": false,
  "requestId": "req_011CbSnv1wc7L4KBGP2vcroh",
  "type": "assistant",
  "uuid": "5e87e08a-05db-47b1-b45a-30d112b4b64d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6ab36dcb-fa57-4a2b-87cc-9d068208d199",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014mBbkBaaaT8mECQxnetD9R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5455,
      "cache_read_input_tokens": 14080,
      "output_tokens": 280,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5455,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 280,
          "cache_read_input_tokens": 14080,
          "cache_creation_input_tokens": 5455,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5455
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

_source line 10 · 2026-05-27T08:54:40.120Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01UmhSA8Fz9kbiwMtKsioqpH`</summary>

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
  "parentUuid": "5e87e08a-05db-47b1-b45a-30d112b4b64d",
  "isSidechain": false,
  "requestId": "req_011CbSnv1wc7L4KBGP2vcroh",
  "type": "assistant",
  "uuid": "81bc8fcf-c2a3-4b6f-bee5-4cc19a8b82d1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6ab36dcb-fa57-4a2b-87cc-9d068208d199",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014mBbkBaaaT8mECQxnetD9R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5455,
      "cache_read_input_tokens": 14080,
      "output_tokens": 280,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5455,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 280,
          "cache_read_input_tokens": 14080,
          "cache_creation_input_tokens": 5455,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5455
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

_source line 11 · 2026-05-27T08:54:40.127Z_

<details><summary>↩ Tool result · `toolu_01UmhSA8Fz9kbiwMtKsioqpH`</summary>

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
  "parentUuid": "81bc8fcf-c2a3-4b6f-bee5-4cc19a8b82d1",
  "isSidechain": false,
  "promptId": "d8b72561-4b7c-4874-99b3-296be6c30c18",
  "type": "user",
  "uuid": "3944bab7-67ef-4cc0-bca4-56012ee523ed",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "81bc8fcf-c2a3-4b6f-bee5-4cc19a8b82d1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6ab36dcb-fa57-4a2b-87cc-9d068208d199",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-27T08:54:42.724Z_

Now let me conduct the prerequisite research with multiple targeted searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3944bab7-67ef-4cc0-bca4-56012ee523ed",
  "isSidechain": false,
  "requestId": "req_011CbSnvcVzL59mueXpiN79R",
  "type": "assistant",
  "uuid": "3a6b3d35-b117-4889-a25e-16871b0cc169",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6ab36dcb-fa57-4a2b-87cc-9d068208d199",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QRwFpeJXPKy8Cw7nPw7emF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 808,
      "cache_read_input_tokens": 19535,
      "output_tokens": 91,
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
          "input_tokens": 3,
          "output_tokens": 91,
          "cache_read_input_tokens": 19535,
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

### Tool call

_source line 13 · 2026-05-27T08:54:43.394Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RHLK3Kx3GBwiuTAav9wrFY`</summary>

```json
{
  "query": "PRMBench ProcessBench process reward model evaluation benchmark 2025 2026 experimental setup baselines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a6b3d35-b117-4889-a25e-16871b0cc169",
  "isSidechain": false,
  "requestId": "req_011CbSnvcVzL59mueXpiN79R",
  "type": "assistant",
  "uuid": "c71c3c63-1320-4c0f-959a-8d68ab84d54a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6ab36dcb-fa57-4a2b-87cc-9d068208d199",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QRwFpeJXPKy8Cw7nPw7emF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 808,
      "cache_read_input_tokens": 19535,
      "output_tokens": 91,
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
          "input_tokens": 3,
          "output_tokens": 91,
          "cache_read_input_tokens": 19535,
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

_source line 14 · 2026-05-27T08:54:53.521Z_

<details><summary>↩ Tool result · `toolu_01RHLK3Kx3GBwiuTAav9wrFY`</summary>

```text
Web search results for query: "PRMBench ProcessBench process reward model evaluation benchmark 2025 2026 experimental setup baselines"

Links: [{"title":"[2501.03124] PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models","url":"https://arxiv.org/abs/2501.03124"},{"title":"PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.1230/"},{"title":"[Literature Review] PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models","url":"https://www.themoonlight.io/en/review/prmbench-a-fine-grained-and-challenging-benchmark-for-process-level-reward-models"},{"title":"[2501.03124v2] PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models","url":"https://arxiv.org/abs/2501.03124v2"},{"title":"PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models","url":"https://arxiv.org/pdf/2501.03124"},{"title":"PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models","url":"https://prmbench.github.io/"},{"title":"Paper page - PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models","url":"https://huggingface.co/papers/2501.03124"},{"title":"PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models | Request PDF","url":"https://www.researchgate.net/publication/394270805_PRMBench_A_Fine-grained_and_Challenging_Benchmark_for_Process-Level_Reward_Models"},{"title":"ToolPRMBench: Evaluating and Advancing Process Reward Models for Tool-using Agents","url":"https://arxiv.org/html/2601.12294v1"}]

Based on the search results, here's what I found about PRMBench and ProcessBench:

## PRMBench Overview

PRMBench is a process-level benchmark specifically designed to assess the fine-grained error detection capabilities of Process-Level Reward Models (PRMs).

### Benchmark Composition

PRMBench comprises 6,216 carefully designed problems and 83,456 step-level labels, evaluating models across multiple dimensions, including simplicity, soundness, and sensitivity.

### Experimental Setup & Evaluation Dimensions

Problems are categorized into three primary evaluation subjects: Simplicity, Soundness, and Sensitivity, further divided into nine sub-categories that reflect various types of errors within reasoning processes. Unlike prior benchmarks that used binary labels (correct/incorrect), PRMBench evaluates models' abilities to detect nuanced errors such as redundancy, circular logic, counterfactual errors, and more.

### Baselines & Experimental Results

Experiments on 25 models spanning both open-source PRMs and closed-source large language models prompted as critic models uncovered significant weaknesses in current PRMs. Gemini-2-Thinking achieved the best performance of 68.8, but still significantly fell behind the human performance of 83.8.

### Data Construction Methodology

The authors start with metadata sourced from PRM800K, which contains questions, answers, and correct reasoning processes, with test cases created wherein the correct reasoning steps are modified to introduce specific errors.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c71c3c63-1320-4c0f-959a-8d68ab84d54a",
  "isSidechain": false,
  "promptId": "d8b72561-4b7c-4874-99b3-296be6c30c18",
  "type": "user",
  "uuid": "f6514d78-23b6-4f34-b4bb-959aabd3b761",
  "toolUseResult": {
    "query": "PRMBench ProcessBench process reward model evaluation benchmark 2025 2026 experimental setup baselines",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HZw9UVUtYzRuq4GnQuVhEy",
        "content": [
          {
            "title": "[2501.03124] PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models",
            "url": "https://arxiv.org/abs/2501.03124"
          },
          {
            "title": "PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models - ACL Anthology",
            "url": "https://aclanthology.org/2025.acl-long.1230/"
          },
          {
            "title": "[Literature Review] PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models",
            "url": "https://www.themoonlight.io/en/review/prmbench-a-fine-grained-and-challenging-benchmark-for-process-level-reward-models"
          },
          {
            "title": "[2501.03124v2] PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models",
            "url": "https://arxiv.org/abs/2501.03124v2"
          },
          {
            "title": "PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models",
            "url": "https://arxiv.org/pdf/2501.03124"
          },
          {
            "title": "PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models",
            "url": "https://prmbench.github.io/"
          },
          {
            "title": "Paper page - PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models",
            "url": "https://huggingface.co/papers/2501.03124"
          },
          {
            "title": "PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models | Request PDF",
            "url": "https://www.researchgate.net/publication/394270805_PRMBench_A_Fine-grained_and_Challenging_Benchmark_for_Process-Level_Reward_Models"
          },
          {
            "title": "ToolPRMBench: Evaluating and Advancing Process Reward Models for Tool-using Agents",
            "url": "https://arxiv.org/html/2601.12294v1"
          }
        ]
      },
      "Based on the search results, here's what I found about PRMBench and ProcessBench:\n\n## PRMBench Overview\n\nPRMBench is a process-level benchmark specifically designed to assess the fine-grained error detection capabilities of Process-Level Reward Models (PRMs).\n\n### Benchmark Composition\n\nPRMBench comprises 6,216 carefully designed problems and 83,456 step-level labels, evaluating models across multiple dimensions, including simplicity, soundness, and sensitivity.\n\n### Experimental Setup & Evaluation Dimensions\n\nProblems are categorized into three primary evaluation subjects: Simplicity, Soundness, and Sensitivity, further divided into nine sub-categories that reflect various types of errors within reasoning processes. Unlike prior benchmarks that used binary labels (correct/incorrect), PRMBench evaluates models' abilities to detect nuanced errors such as redundancy, circular logic, counterfactual errors, and more.\n\n### Baselines & Experimental Results\n\nExperiments on 25 models spanning both open-source PRMs and closed-source large language models prompted as critic models uncovered significant weaknesses in current PRMs. Gemini-2-Thinking achieved the best performance of 68.8, but still significantly fell behind the human performance of 83.8.\n\n### Data Construction Methodology\n\nThe authors start with metadata sourced from PRM800K, which contains questions, answers, and correct reasoning processes, with test cases created wherein the correct reasoning steps are modified to introduce specific errors."
    ],
    "durationSeconds": 10.119558896000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c71c3c63-1320-4c0f-959a-8d68ab84d54a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6ab36dcb-fa57-4a2b-87cc-9d068208d199",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-27T08:54:56.235Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01C5dhqaHMsieJgtiCmssfVA`</summary>

```json
{
  "query": "PathFinder-PRM process reward model 2025 arXiv 2505.19706 experimental results baselines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6514d78-23b6-4f34-b4bb-959aabd3b761",
  "isSidechain": false,
  "requestId": "req_011CbSnwbVVdndso3vdbGu3z",
  "type": "assistant",
  "uuid": "f21c3512-67de-46c1-8adb-683ab873b1b1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6ab36dcb-fa57-4a2b-87cc-9d068208d199",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FsReFfjGnHNL4iekTHn9sU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 976,
      "cache_read_input_tokens": 20343,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 976,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 78,
          "cache_read_input_tokens": 20343,
          "cache_creation_input_tokens": 976,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 976
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

_source line 16 · 2026-05-27T08:55:04.250Z_

<details><summary>↩ Tool result · `toolu_01C5dhqaHMsieJgtiCmssfVA`</summary>

```text
Web search results for query: "PathFinder-PRM process reward model 2025 arXiv 2505.19706 experimental results baselines"

Links: [{"title":"[2505.19706] Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision","url":"https://arxiv.org/abs/2505.19706"},{"title":"arXiv:2505.19706v1 [cs.CL] 26 May 2025","url":"https://arxiv.org/pdf/2505.19706"},{"title":"Process-Supervised Reward Model","url":"https://www.emergentmind.com/topics/process-supervised-reward-model-prm"},{"title":"Process-supervised Reward Models (PRMs)","url":"https://www.emergentmind.com/topics/process-supervised-reward-models-prm"},{"title":"GitHub - declare-lab/PathFinder-PRM: This repository contains the official implementation of Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision.","url":"https://github.com/declare-lab/PathFinder-PRM"},{"title":"A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models","url":"https://arxiv.org/html/2510.08049v3"},{"title":"GitHub - RyanLiu112/Awesome-Process-Reward-Models: A comprehensive collection of process reward models. · GitHub","url":"https://github.com/RyanLiu112/Awesome-Process-Reward-Models"},{"title":"A Survey of Process Reward Models: From Outcome Signals to Process","url":"https://arxiv.org/pdf/2510.08049"},{"title":"Awesome-Process-Reward-Models/README.md at main · RyanLiu112/Awesome-Process-Reward-Models","url":"https://github.com/RyanLiu112/Awesome-Process-Reward-Models/blob/main/README.md"}]

Based on the search results, here's information about PathFinder-PRM's experimental results and baselines:

## Overview

PathFinder-PRM is a novel hierarchical, error-aware discriminative PRM that first classifies math and consistency errors at each step, then combines these fine-grained signals to estimate step correctness.

## Experimental Results

On PRMBench, PathFinder-PRM achieves a new state-of-the-art PRMScore of 67.7, outperforming the prior best (65.5) while using 3 times less data. When applied to reward guided greedy search, the model yields prm@8 48.3, a +1.5 point gain over the strongest baseline.

## Training Data

To train PathFinder-PRM, the authors constructed a 400K-sample dataset by enriching the human-annotated PRM800K corpus and RLHFlow Mistral traces with three-dimensional step-level labels.

## Key Findings

The error-aware approach has been empirically shown to improve both benchmark F1 and downstream guided search performance. Hierarchical models such as PathFinder-PRM explicitly decompose errors into math and consistency dimensions before reward assignment, increasing interpretability and data efficiency.

The paper (arXiv:2505.19706) was published on May 26, 2025, and the official implementation is available on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f21c3512-67de-46c1-8adb-683ab873b1b1",
  "isSidechain": false,
  "promptId": "d8b72561-4b7c-4874-99b3-296be6c30c18",
  "type": "user",
  "uuid": "47fbec49-1b83-46ee-93fe-7b5c6bc7c554",
  "toolUseResult": {
    "query": "PathFinder-PRM process reward model 2025 arXiv 2505.19706 experimental results baselines",
    "results": [
      {
        "tool_use_id": "srvtoolu_016TJxfLLmo3CsCAsAsp8QHq",
        "content": [
          {
            "title": "[2505.19706] Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision",
            "url": "https://arxiv.org/abs/2505.19706"
          },
          {
            "title": "arXiv:2505.19706v1 [cs.CL] 26 May 2025",
            "url": "https://arxiv.org/pdf/2505.19706"
          },
          {
            "title": "Process-Supervised Reward Model",
            "url": "https://www.emergentmind.com/topics/process-supervised-reward-model-prm"
          },
          {
            "title": "Process-supervised Reward Models (PRMs)",
            "url": "https://www.emergentmind.com/topics/process-supervised-reward-models-prm"
          },
          {
            "title": "GitHub - declare-lab/PathFinder-PRM: This repository contains the official implementation of Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision.",
            "url": "https://github.com/declare-lab/PathFinder-PRM"
          },
          {
            "title": "A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models",
            "url": "https://arxiv.org/html/2510.08049v3"
          },
          {
            "title": "GitHub - RyanLiu112/Awesome-Process-Reward-Models: A comprehensive collection of process reward models. · GitHub",
            "url": "https://github.com/RyanLiu112/Awesome-Process-Reward-Models"
          },
          {
            "title": "A Survey of Process Reward Models: From Outcome Signals to Process",
            "url": "https://arxiv.org/pdf/2510.08049"
          },
          {
            "title": "Awesome-Process-Reward-Models/README.md at main · RyanLiu112/Awesome-Process-Reward-Models",
            "url": "https://github.com/RyanLiu112/Awesome-Process-Reward-Models/blob/main/README.md"
          }
        ]
      },
      "Based on the search results, here's information about PathFinder-PRM's experimental results and baselines:\n\n## Overview\n\nPathFinder-PRM is a novel hierarchical, error-aware discriminative PRM that first classifies math and consistency errors at each step, then combines these fine-grained signals to estimate step correctness.\n\n## Experimental Results\n\nOn PRMBench, PathFinder-PRM achieves a new state-of-the-art PRMScore of 67.7, outperforming the prior best (65.5) while using 3 times less data. When applied to reward guided greedy search, the model yields prm@8 48.3, a +1.5 point gain over the strongest baseline.\n\n## Training Data\n\nTo train PathFinder-PRM, the authors constructed a 400K-sample dataset by enriching the human-annotated PRM800K corpus and RLHFlow Mistral traces with three-dimensional step-level labels.\n\n## Key Findings\n\nThe error-aware approach has been empirically shown to improve both benchmark F1 and downstream guided search performance. Hierarchical models such as PathFinder-PRM explicitly decompose errors into math and consistency dimensions before reward assignment, increasing interpretability and data efficiency.\n\nThe paper (arXiv:2505.19706) was published on May 26, 2025, and the official implementation is available on GitHub."
    ],
    "durationSeconds": 8.010986124999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f21c3512-67de-46c1-8adb-683ab873b1b1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6ab36dcb-fa57-4a2b-87cc-9d068208d199",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-27T08:55:07.332Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EbDSdqAyCpJ5KE5wotpJ3N`</summary>

```json
{
  "query": "APRM adversarial process reward model CRM conditional reward model experimental design ablation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47fbec49-1b83-46ee-93fe-7b5c6bc7c554",
  "isSidechain": false,
  "requestId": "req_011CbSnxPJYPTRnEGF87r2LS",
  "type": "assistant",
  "uuid": "326927c0-3971-47de-a2bd-32cf994038c7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6ab36dcb-fa57-4a2b-87cc-9d068208d199",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C7itPW4mJMrYZvNb9cSg3o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 918,
      "cache_read_input_tokens": 21319,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 918,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 21319,
          "cache_creation_input_tokens": 918,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 918
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

_source line 18 · 2026-05-27T08:55:14.875Z_

<details><summary>↩ Tool result · `toolu_01EbDSdqAyCpJ5KE5wotpJ3N`</summary>

```text
Web search results for query: "APRM adversarial process reward model CRM conditional reward model experimental design ablation 2025 2026"

Links: [{"title":"Adversarially Trained Reward Models","url":"https://www.emergentmind.com/topics/adversarially-trained-reward-models"},{"title":"Adversarial Training for Process Reward Models","url":"https://arxiv.org/pdf/2511.22888"},{"title":"[2511.22888] Adversarial Training for Process Reward Models","url":"https://arxiv.org/abs/2511.22888"},{"title":"Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning","url":"https://arxiv.org/pdf/2509.26578"},{"title":"Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning","url":"https://arxiv.org/html/2509.26578"},{"title":"Adversarial Training for Process Reward Models","url":"https://arxiv.org/html/2511.22888"}]

I found relevant research on both APRM and CRM. Here's what the recent work shows:

## Adversarial Process Reward Models (APRM)

APRM uses a Generator to produce reasoning errors to deceive a Process Reward Model (PRM), while the PRM learns to detect them, yielding progressively harder negatives that improve robustness and generalization to novel errors without manual step-level labels. Across math and science reasoning benchmarks, APRM yields an average improvement of 3.4 percentage points over state-of-the-art PRM training methods.

The approach employs game-aware optimizers and symmetric policy regularization for stable training, modeling the Generator-PRM interaction as a general-sum game that yields a Nash Equilibrium rather than a mini-max saddle point. Ablations highlight the necessity of entropy regularization and OGDA in avoiding degenerate solutions.

## Conditional Reward Modeling (CRM)

CRM frames LLM reasoning as a temporal process where the reward of each step is conditioned on preceding steps and explicitly linked to the final outcome. By enforcing conditional probability rules, the design captures causal relationships among reasoning steps with precise attribution of each intermediate step. Experiments across Best-of-N sampling, beam search and reinforcement learning demonstrate CRM consistently outperforms existing reward models.

Sample ablation studies confirm the necessity of adversarial data filtering, task-specific loss weighting, and ensemble uncertainty for maximal effect.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "326927c0-3971-47de-a2bd-32cf994038c7",
  "isSidechain": false,
  "promptId": "d8b72561-4b7c-4874-99b3-296be6c30c18",
  "type": "user",
  "uuid": "2d9b2a2a-058f-4ec5-b3be-84997ae15b36",
  "toolUseResult": {
    "query": "APRM adversarial process reward model CRM conditional reward model experimental design ablation 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01M1xvfPDr755Jf9Vm5Q3Xrz",
        "content": [
          {
            "title": "Adversarially Trained Reward Models",
            "url": "https://www.emergentmind.com/topics/adversarially-trained-reward-models"
          },
          {
            "title": "Adversarial Training for Process Reward Models",
            "url": "https://arxiv.org/pdf/2511.22888"
          },
          {
            "title": "[2511.22888] Adversarial Training for Process Reward Models",
            "url": "https://arxiv.org/abs/2511.22888"
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
            "title": "Adversarial Training for Process Reward Models",
            "url": "https://arxiv.org/html/2511.22888"
          }
        ]
      },
      "I found relevant research on both APRM and CRM. Here's what the recent work shows:\n\n## Adversarial Process Reward Models (APRM)\n\nAPRM uses a Generator to produce reasoning errors to deceive a Process Reward Model (PRM), while the PRM learns to detect them, yielding progressively harder negatives that improve robustness and generalization to novel errors without manual step-level labels. Across math and science reasoning benchmarks, APRM yields an average improvement of 3.4 percentage points over state-of-the-art PRM training methods.\n\nThe approach employs game-aware optimizers and symmetric policy regularization for stable training, modeling the Generator-PRM interaction as a general-sum game that yields a Nash Equilibrium rather than a mini-max saddle point. Ablations highlight the necessity of entropy regularization and OGDA in avoiding degenerate solutions.\n\n## Conditional Reward Modeling (CRM)\n\nCRM frames LLM reasoning as a temporal process where the reward of each step is conditioned on preceding steps and explicitly linked to the final outcome. By enforcing conditional probability rules, the design captures causal relationships among reasoning steps with precise attribution of each intermediate step. Experiments across Best-of-N sampling, beam search and reinforcement learning demonstrate CRM consistently outperforms existing reward models.\n\nSample ablation studies confirm the necessity of adversarial data filtering, task-specific loss weighting, and ensemble uncertainty for maximal effect."
    ],
    "durationSeconds": 7.537184672999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "326927c0-3971-47de-a2bd-32cf994038c7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6ab36dcb-fa57-4a2b-87cc-9d068208d199",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-27T08:55:19.498Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019bdZueFwG8QsgKaiMEmMRg`</summary>

```json
{
  "query": "\"reward under attack\" process reward model robustness hacking 2026 arXiv experimental evaluation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d9b2a2a-058f-4ec5-b3be-84997ae15b36",
  "isSidechain": false,
  "requestId": "req_011CbSnyAjGrowJeeabD4693",
  "type": "assistant",
  "uuid": "f7033c90-1da4-4922-babe-aaa1c5613170",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6ab36dcb-fa57-4a2b-87cc-9d068208d199",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GU8e3X4WiorWrG6cVats8F",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 689,
      "cache_read_input_tokens": 22237,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 689,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 22237,
          "cache_creation_input_tokens": 689,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 689
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

_source line 20 · 2026-05-27T08:55:25.858Z_

<details><summary>↩ Tool result · `toolu_019bdZueFwG8QsgKaiMEmMRg`</summary>

```text
Web search results for query: ""reward under attack" process reward model robustness hacking 2026 arXiv experimental evaluation"

Links: [{"title":"[2603.06621] Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models","url":"https://arxiv.org/abs/2603.06621"},{"title":"[2602.10623v1] Mitigating Reward Hacking in RLHF via Bayesian Non-negative Reward Modeling","url":"https://arxiv.org/abs/2602.10623v1"},{"title":"[2602.10623] Mitigating Reward Hacking in RLHF via Bayesian Non-negative Reward Modeling","url":"https://arxiv.org/abs/2602.10623"},{"title":"Reward Under Attack: Analyzing the Robustness and Hackability of","url":"https://arxiv.org/pdf/2603.06621"},{"title":"Reward Hacking as Equilibrium under Finite Evaluation","url":"https://arxiv.org/html/2603.28063v1"},{"title":"[2604.02986] Mitigating Reward Hacking in RLHF via Advantage Sign Robustness","url":"https://arxiv.org/abs/2604.02986"},{"title":"[2604.12086] Robust Optimization for Mitigating Reward Hacking with Correlated Proxies","url":"https://arxiv.org/abs/2604.12086"},{"title":"Mitigating Reward Hacking in RLHF via Advantage Sign Robustness","url":"https://arxiv.org/pdf/2604.02986"},{"title":"Robust Reward Modeling via Causal Rubrics","url":"https://arxiv.org/pdf/2506.16507"}]

Perfect! I found the paper you were searching for. Here's what I found:

## "Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models"

The research reveals a critical failure mode where policies trained on AIME problems achieve near-perfect PRM rewards (>0.9), while ground-truth accuracy remains low (below 4%), with 43% of reward gains attributable to stylistic shortcuts.

The findings show that current PRMs function as fluency detectors rather than reasoning verifiers, creating systematic blind spots that undermine their use as training signals.

The authors release PRM-BiasBench and a diagnostic toolkit to enable robustness evaluation before deployment.

The paper was published on **February 20, 2026** on arXiv as paper **2603.06621**. It appears to employ a three-tiered diagnostic framework to evaluate process reward model robustness under various levels of adversarial pressure, including static perturbations, adversarial optimization, and RL-based attacks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f7033c90-1da4-4922-babe-aaa1c5613170",
  "isSidechain": false,
  "promptId": "d8b72561-4b7c-4874-99b3-296be6c30c18",
  "type": "user",
  "uuid": "e7b5e432-457d-489e-8173-4c0bb86ff44c",
  "toolUseResult": {
    "query": "\"reward under attack\" process reward model robustness hacking 2026 arXiv experimental evaluation",
    "results": [
      {
        "tool_use_id": "srvtoolu_01X1DeCWEHNuaA51CiB2cgqr",
        "content": [
          {
            "title": "[2603.06621] Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models",
            "url": "https://arxiv.org/abs/2603.06621"
          },
          {
            "title": "[2602.10623v1] Mitigating Reward Hacking in RLHF via Bayesian Non-negative Reward Modeling",
            "url": "https://arxiv.org/abs/2602.10623v1"
          },
          {
            "title": "[2602.10623] Mitigating Reward Hacking in RLHF via Bayesian Non-negative Reward Modeling",
            "url": "https://arxiv.org/abs/2602.10623"
          },
          {
            "title": "Reward Under Attack: Analyzing the Robustness and Hackability of",
            "url": "https://arxiv.org/pdf/2603.06621"
          },
          {
            "title": "Reward Hacking as Equilibrium under Finite Evaluation",
            "url": "https://arxiv.org/html/2603.28063v1"
          },
          {
            "title": "[2604.02986] Mitigating Reward Hacking in RLHF via Advantage Sign Robustness",
            "url": "https://arxiv.org/abs/2604.02986"
          },
          {
            "title": "[2604.12086] Robust Optimization for Mitigating Reward Hacking with Correlated Proxies",
            "url": "https://arxiv.org/abs/2604.12086"
          },
          {
            "title": "Mitigating Reward Hacking in RLHF via Advantage Sign Robustness",
            "url": "https://arxiv.org/pdf/2604.02986"
          },
          {
            "title": "Robust Reward Modeling via Causal Rubrics",
            "url": "https://arxiv.org/pdf/2506.16507"
          }
        ]
      },
      "Perfect! I found the paper you were searching for. Here's what I found:\n\n## \"Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models\"\n\nThe research reveals a critical failure mode where policies trained on AIME problems achieve near-perfect PRM rewards (>0.9), while ground-truth accuracy remains low (below 4%), with 43% of reward gains attributable to stylistic shortcuts.\n\nThe findings show that current PRMs function as fluency detectors rather than reasoning verifiers, creating systematic blind spots that undermine their use as training signals.\n\nThe authors release PRM-BiasBench and a diagnostic toolkit to enable robustness evaluation before deployment.\n\nThe paper was published on **February 20, 2026** on arXiv as paper **2603.06621**. It appears to employ a three-tiered diagnostic framework to evaluate process reward model robustness under various levels of adversarial pressure, including static perturbations, adversarial optimization, and RL-based attacks."
    ],
    "durationSeconds": 6.355423814000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f7033c90-1da4-4922-babe-aaa1c5613170",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6ab36dcb-fa57-4a2b-87cc-9d068208d199",
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
  "lastPrompt": "# Premise-Graph Contrastive Training for Logic-Grounded Process Reward Models  ## Core Problem  Current process reward models detect consistency rather than causality. \"Reward Models Identify Consiste…",
  "leafUuid": "e7b5e432-457d-489e-8173-4c0bb86ff44c",
  "sessionId": "6ab36dcb-fa57-4a2b-87cc-9d068208d199"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Premise-graph contrastive training for process reward models",
  "sessionId": "6ab36dcb-fa57-4a2b-87cc-9d068208d199"
}
```

---

### Tool call

_source line 23 · 2026-05-27T08:55:33.929Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KNLtJP4vQSATJjQy3Lu8XE`</summary>

```json
{
  "query": "PARC PERL premise dependency extraction mathematical reasoning DAG 2025 experimental setup recall precision"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7b5e432-457d-489e-8173-4c0bb86ff44c",
  "isSidechain": false,
  "requestId": "req_011CbSnyyiH5uLG2u8FG4qp2",
  "type": "assistant",
  "uuid": "154649be-3d93-445e-b9c6-4f59d1cc4c7e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6ab36dcb-fa57-4a2b-87cc-9d068208d199",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NDL6SQmgNmBqp18v9d36mB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 784,
      "cache_read_input_tokens": 22926,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 784,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 22926,
          "cache_creation_input_tokens": 784,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 784
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

_source line 24 · 2026-05-27T08:55:43.848Z_

<details><summary>↩ Tool result · `toolu_01KNLtJP4vQSATJjQy3Lu8XE`</summary>

```text
Web search results for query: "PARC PERL premise dependency extraction mathematical reasoning DAG 2025 experimental setup recall precision"

Links: [{"title":"Premise-Augmented Reasoning Chains Improve Error Identification in Math Reasoning with LLMs","url":"https://abhinavchinta.com/parc/"},{"title":"Premise-Augmented Reasoning Chains Improve Error Identification in Math reasoning with LLMs","url":"https://arxiv.org/pdf/2502.02362"},{"title":"Premise-Augmented Reasoning Chains Improve Error Identification in Math Reasoning with LLMs","url":"https://arxiv.org/html/2502.02362v4"},{"title":"From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs","url":"https://arxiv.org/html/2601.17593"},{"title":"DAG-Math: Graph-Guided Mathematical Reasoning in LLMs","url":"https://arxiv.org/html/2510.19842v1"},{"title":"DAG-Math: Graph-Guided Mathematical Reasoning in LLMs Yuanhe Zhang1,","url":"https://openreview.net/pdf/da01f6108049382645bcd011dc7b62217fd24965.pdf"}]

Based on the search results, here's what I found about PARC, PERL, premise dependency extraction, and the experimental setup:

## PARC and PERL Overview

PARC (Premise Augmented Reasoning Chains) restructures conventional linear reasoning chains by introducing premise links, resulting in a directed acyclic graph where the nodes are the steps and the edges are the premise links. PERL (Premises and ERrors identification in LLMs) is a PARC-based dataset built to demonstrate that LLMs can reliably identify premises within complex reasoning chains.

## Premise Dependency Extraction Performance

Even open-source LLMs achieve 90% recall in premise identification. More specifically, Llama 3.1 70b, Qwen 2.5 32b and GPT4o are very efficient in this task, all having a recall greater than 90%. PARC's effectiveness is evaluated using precision, recall, F1-score for premise extraction, and accuracy metrics for error identification.

## Mathematical Reasoning and DAG Structure

Depth-First Search (DFS) is employed on the PARC structure to systematically identify dependencies, clearly distinguishing inherent step-level inaccuracies from errors propagated due to faulty premises. The accuracy of error identification improves by 6% to 16% absolute when step-by-step verification is carried out in PARC under the premises.

## Experimental Setup

The experimental setup utilizes both open-source (e.g., Llama, Qwen) and proprietary (e.g., GPT-4o) large language models, comparing the premise-centric verification approach against traditional full-context baseline methods. PERL incorporates reasoning chains from established mathematical reasoning datasets (GSM8K, MATH, Orca-Math, and MetaMathQA), annotated with both premises and error types using OpenAI's GPT-4o.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "154649be-3d93-445e-b9c6-4f59d1cc4c7e",
  "isSidechain": false,
  "promptId": "d8b72561-4b7c-4874-99b3-296be6c30c18",
  "type": "user",
  "uuid": "5efd387c-46bd-460b-a7b2-b2eb4a42136f",
  "toolUseResult": {
    "query": "PARC PERL premise dependency extraction mathematical reasoning DAG 2025 experimental setup recall precision",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HwX6UG8hfgPYMYzBLJ1ugm",
        "content": [
          {
            "title": "Premise-Augmented Reasoning Chains Improve Error Identification in Math Reasoning with LLMs",
            "url": "https://abhinavchinta.com/parc/"
          },
          {
            "title": "Premise-Augmented Reasoning Chains Improve Error Identification in Math reasoning with LLMs",
            "url": "https://arxiv.org/pdf/2502.02362"
          },
          {
            "title": "Premise-Augmented Reasoning Chains Improve Error Identification in Math Reasoning with LLMs",
            "url": "https://arxiv.org/html/2502.02362v4"
          },
          {
            "title": "From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs",
            "url": "https://arxiv.org/html/2601.17593"
          },
          {
            "title": "DAG-Math: Graph-Guided Mathematical Reasoning in LLMs",
            "url": "https://arxiv.org/html/2510.19842v1"
          },
          {
            "title": "DAG-Math: Graph-Guided Mathematical Reasoning in LLMs Yuanhe Zhang1,",
            "url": "https://openreview.net/pdf/da01f6108049382645bcd011dc7b62217fd24965.pdf"
          }
        ]
      },
      "Based on the search results, here's what I found about PARC, PERL, premise dependency extraction, and the experimental setup:\n\n## PARC and PERL Overview\n\nPARC (Premise Augmented Reasoning Chains) restructures conventional linear reasoning chains by introducing premise links, resulting in a directed acyclic graph where the nodes are the steps and the edges are the premise links. PERL (Premises and ERrors identification in LLMs) is a PARC-based dataset built to demonstrate that LLMs can reliably identify premises within complex reasoning chains.\n\n## Premise Dependency Extraction Performance\n\nEven open-source LLMs achieve 90% recall in premise identification. More specifically, Llama 3.1 70b, Qwen 2.5 32b and GPT4o are very efficient in this task, all having a recall greater than 90%. PARC's effectiveness is evaluated using precision, recall, F1-score for premise extraction, and accuracy metrics for error identification.\n\n## Mathematical Reasoning and DAG Structure\n\nDepth-First Search (DFS) is employed on the PARC structure to systematically identify dependencies, clearly distinguishing inherent step-level inaccuracies from errors propagated due to faulty premises. The accuracy of error identification improves by 6% to 16% absolute when step-by-step verification is carried out in PARC under the premises.\n\n## Experimental Setup\n\nThe experimental setup utilizes both open-source (e.g., Llama, Qwen) and proprietary (e.g., GPT-4o) large language models, comparing the premise-centric verification approach against traditional full-context baseline methods. PERL incorporates reasoning chains from established mathematical reasoning datasets (GSM8K, MATH, Orca-Math, and MetaMathQA), annotated with both premises and error types using OpenAI's GPT-4o."
    ],
    "durationSeconds": 9.913163163999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "154649be-3d93-445e-b9c6-4f59d1cc4c7e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6ab36dcb-fa57-4a2b-87cc-9d068208d199",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-27T08:55:52.171Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LhcnzaivWxnmyH76ycAHcn`</summary>

```json
{
  "query": "GenPRM ThinkPRM R-PRM process reward model 2025 2026 inference compute budget experimental comparison"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5efd387c-46bd-460b-a7b2-b2eb4a42136f",
  "isSidechain": false,
  "requestId": "req_011CbSo1KMzZfs9zqMtLKNU3",
  "type": "assistant",
  "uuid": "cb56b623-3da5-4e3a-acc5-f54d818e884d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6ab36dcb-fa57-4a2b-87cc-9d068208d199",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ZfSuHr3Z6hbxSLvVJuHLd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 836,
      "cache_read_input_tokens": 23710,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 836,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 23710,
          "cache_creation_input_tokens": 836,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 836
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

_source line 26 · 2026-05-27T08:55:59.269Z_

<details><summary>↩ Tool result · `toolu_01LhcnzaivWxnmyH76ycAHcn`</summary>

```text
Web search results for query: "GenPRM ThinkPRM R-PRM process reward model 2025 2026 inference compute budget experimental comparison"

Links: [{"title":"GitHub - RyanLiu112/Awesome-Process-Reward-Models: A comprehensive collection of process reward models. · GitHub","url":"https://github.com/RyanLiu112/Awesome-Process-Reward-Models"},{"title":"GitHub - RyanLiu112/GenPRM: [AAAI 2026] Official codebase for \"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning\".","url":"https://github.com/RyanLiu112/GenPRM"},{"title":"Process Reward Models That Think | OpenReview","url":"https://openreview.net/forum?id=V727xqBYIW"},{"title":"GitHub - mukhal/ThinkPRM: Process Reward Models That Think","url":"https://github.com/mukhal/thinkprm"},{"title":"ThinkPRM: A Generative Process Reward Models for Scalable Reasoning Verification - MarkTechPost","url":"https://www.marktechpost.com/2025/04/29/thinkprm-a-generative-process-reward-models-for-scalable-reasoning-verification/"},{"title":"[2504.16828] Process Reward Models That Think","url":"https://arxiv.org/abs/2504.16828"},{"title":"Paper page - Process Reward Models That Think","url":"https://huggingface.co/papers/2504.16828"},{"title":"Process Reward Models That Think","url":"https://arxiv.org/pdf/2504.16828"},{"title":"Process Reward Models: Step-Level Feedback for LLMs","url":"https://www.emergentmind.com/topics/process-reward-models-prm"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=Process+Reward+Models+%28PRMs%29"}]

I've performed a web search on process reward models (PRMs) and found comprehensive information about GenPRM, ThinkPRM, and R-PRM. Here are the key findings:

## Overview of Recent Process Reward Models (2025)

The search revealed several recent PRM models including GenPRM, ThinkPRM, and R-PRM, all from 2025.

### GenPRM

GenPRM is a generative process reward model that performs explicit Chain-of-Thought (CoT) reasoning with code verification before providing judgment for each reasoning step. Through test-time scaling, a 1.5B GenPRM outperforms GPT-4o, and a 7B GenPRM surpasses Qwen2.5-Math-PRM-72B on ProcessBench.

### ThinkPRM

ThinkPRM is a long CoT verifier fine-tuned on orders of magnitude fewer process labels than those required by discriminative PRMs. ThinkPRM outperforms LLM-as-a-Judge and discriminative verifiers using only 1% of the process labels in PRM800K across several challenging benchmarks. Under the same token budget, ThinkPRM scales up verification compute more effectively compared to LLM-as-a-Judge, outperforming it by 7.2% on a subset of ProcessBench.

### R-PRM

R-PRM: Reasoning-Driven Process Reward Modeling was released in arXiv 2025.03.

## Inference Compute & Experimental Comparisons

ThinkPRM enables scaling up verifier compute either in parallel or sequentially by thinking longer. On verifier-guided search with MATH-500, ThinkPRM-1.5B outperforms discriminative PRMs by approximately 5 percentage points.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb56b623-3da5-4e3a-acc5-f54d818e884d",
  "isSidechain": false,
  "promptId": "d8b72561-4b7c-4874-99b3-296be6c30c18",
  "type": "user",
  "uuid": "24027fda-b5ec-4961-902d-a58a26721dbd",
  "toolUseResult": {
    "query": "GenPRM ThinkPRM R-PRM process reward model 2025 2026 inference compute budget experimental comparison",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RRkjFAr8fXLabY84ZrB2LJ",
        "content": [
          {
            "title": "GitHub - RyanLiu112/Awesome-Process-Reward-Models: A comprehensive collection of process reward models. · GitHub",
            "url": "https://github.com/RyanLiu112/Awesome-Process-Reward-Models"
          },
          {
            "title": "GitHub - RyanLiu112/GenPRM: [AAAI 2026] Official codebase for \"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning\".",
            "url": "https://github.com/RyanLiu112/GenPRM"
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
            "title": "ThinkPRM: A Generative Process Reward Models for Scalable Reasoning Verification - MarkTechPost",
            "url": "https://www.marktechpost.com/2025/04/29/thinkprm-a-generative-process-reward-models-for-scalable-reasoning-verification/"
          },
          {
            "title": "[2504.16828] Process Reward Models That Think",
            "url": "https://arxiv.org/abs/2504.16828"
          },
          {
            "title": "Paper page - Process Reward Models That Think",
            "url": "https://huggingface.co/papers/2504.16828"
          },
          {
            "title": "Process Reward Models That Think",
            "url": "https://arxiv.org/pdf/2504.16828"
          },
          {
            "title": "Process Reward Models: Step-Level Feedback for LLMs",
            "url": "https://www.emergentmind.com/topics/process-reward-models-prm"
          },
          {
            "title": "Daily Papers - Hugging Face",
            "url": "https://huggingface.co/papers?q=Process+Reward+Models+%28PRMs%29"
          }
        ]
      },
      "I've performed a web search on process reward models (PRMs) and found comprehensive information about GenPRM, ThinkPRM, and R-PRM. Here are the key findings:\n\n## Overview of Recent Process Reward Models (2025)\n\nThe search revealed several recent PRM models including GenPRM, ThinkPRM, and R-PRM, all from 2025.\n\n### GenPRM\n\nGenPRM is a generative process reward model that performs explicit Chain-of-Thought (CoT) reasoning with code verification before providing judgment for each reasoning step. Through test-time scaling, a 1.5B GenPRM outperforms GPT-4o, and a 7B GenPRM surpasses Qwen2.5-Math-PRM-72B on ProcessBench.\n\n### ThinkPRM\n\nThinkPRM is a long CoT verifier fine-tuned on orders of magnitude fewer process labels than those required by discriminative PRMs. ThinkPRM outperforms LLM-as-a-Judge and discriminative verifiers using only 1% of the process labels in PRM800K across several challenging benchmarks. Under the same token budget, ThinkPRM scales up verification compute more effectively compared to LLM-as-a-Judge, outperforming it by 7.2% on a subset of ProcessBench.\n\n### R-PRM\n\nR-PRM: Reasoning-Driven Process Reward Modeling was released in arXiv 2025.03.\n\n## Inference Compute & Experimental Comparisons\n\nThinkPRM enables scaling up verifier compute either in parallel or sequentially by thinking longer. On verifier-guided search with MATH-500, ThinkPRM-1.5B outperforms discriminative PRMs by approximately 5 percentage points."
    ],
    "durationSeconds": 7.092491580999995,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "cb56b623-3da5-4e3a-acc5-f54d818e884d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6ab36dcb-fa57-4a2b-87cc-9d068208d199",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-27T08:56:02.065Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018tFUDzizC8UY9wxGu62x32`</summary>

```json
{
  "query": "contrastive learning reward model training InfoNCE representation learning 2025 2026 ablation experimental methodology"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24027fda-b5ec-4961-902d-a58a26721dbd",
  "isSidechain": false,
  "requestId": "req_011CbSo2SbbMSV3RsxMgCKa5",
  "type": "assistant",
  "uuid": "5a0f39cf-7caa-4c5c-87d4-0cfd67455814",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6ab36dcb-fa57-4a2b-87cc-9d068208d199",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S8RwRQSeazGqPHxMeA5B96",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1012,
      "cache_read_input_tokens": 24546,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1012,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 24546,
          "cache_creation_input_tokens": 1012,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1012
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

_source line 28 · 2026-05-27T08:56:12.407Z_

<details><summary>↩ Tool result · `toolu_018tFUDzizC8UY9wxGu62x32`</summary>

```text
Web search results for query: "contrastive learning reward model training InfoNCE representation learning 2025 2026 ablation experimental methodology"

Links: [{"title":"GRACE: GENERATIVE REPRESENTATION LEARNING","url":"https://openreview.net/pdf?id=hs9lwjH1bJ"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2602.24012"},{"title":"What is contrastive learning? Meaning, Architecture, Examples, Use Cases, and How to Measure It (2026 Guide) – AiOps School","url":"https://aiopsschool.com/blog/contrastive-learning/"},{"title":"GRACE: GENERATIVE REPRESENTATION LEARNING VIA CONTRASTIVE POLICY OPTIMIZATION","url":"https://arxiv.org/pdf/2510.04506"},{"title":"InfoNCE: Contrastive Loss for Representation Learning","url":"https://www.emergentmind.com/topics/infonce"},{"title":"Understanding InfoNCE: Transition Probability Matrix Induced Feature Clustering","url":"https://arxiv.org/pdf/2511.12180"},{"title":"A Systematic Review of Contrastive Learning in Medical AI: Foundations, Biomedical Modalities, and Future Directions - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12938576/"}]

I found several recent research papers and resources on contrastive learning, reward model training, and InfoNCE representation learning from 2025-2026. Here are the key findings:

## Recent Work on Contrastive Learning & Reward Models

**GRACE: Generative Representation Learning via Contrastive Policy Optimization** is a prominent 2025-2026 paper that directly addresses combining contrastive learning with reward model training. The approach optimizes a contrastive reward within an RL framework, which aligns updates with the generative policy while using relative, advantage-weighted updates that resist representation collapse and the rescaling/drift common in direct InfoNCE-style training.

## InfoNCE Theory & Ablations

The InfoNCE loss is the standard objective in self-supervised representation learning and underlies methods such as SimCLR, MoCo, and CLIP. Recent 2025-2026 research has examined the theoretical properties more deeply. Prior work has studied these effects from geometric and optimization perspectives, identifying phenomena such as hyperspherical uniformity and feature concentration.

## Experimental Methodology (GRACE Paper)

The experimental setup includes: experiments run on a single node with 4× NVIDIA H100 GPUs, with training performed for 2 epochs with a batch size of 64. For supervised training, they use a replication of the public portion of the E5 dataset which contains 1.5M samples.

## Key Challenges

The effectiveness of InfoNCE is contingent on negative sampling, and excessive negatives under label noise produce misleading loss signals, especially when semantically similar negatives are included.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5a0f39cf-7caa-4c5c-87d4-0cfd67455814",
  "isSidechain": false,
  "promptId": "d8b72561-4b7c-4874-99b3-296be6c30c18",
  "type": "user",
  "uuid": "a8716e15-c157-4275-b975-047ef7dea2ea",
  "toolUseResult": {
    "query": "contrastive learning reward model training InfoNCE representation learning 2025 2026 ablation experimental methodology",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RHRNoJMBxn11fBjdcVs11v",
        "content": [
          {
            "title": "GRACE: GENERATIVE REPRESENTATION LEARNING",
            "url": "https://openreview.net/pdf?id=hs9lwjH1bJ"
          },
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://arxiv.org/pdf/2602.24012"
          },
          {
            "title": "What is contrastive learning? Meaning, Architecture, Examples, Use Cases, and How to Measure It (2026 Guide) – AiOps School",
            "url": "https://aiopsschool.com/blog/contrastive-learning/"
          },
          {
            "title": "GRACE: GENERATIVE REPRESENTATION LEARNING VIA CONTRASTIVE POLICY OPTIMIZATION",
            "url": "https://arxiv.org/pdf/2510.04506"
          },
          {
            "title": "InfoNCE: Contrastive Loss for Representation Learning",
            "url": "https://www.emergentmind.com/topics/infonce"
          },
          {
            "title": "Understanding InfoNCE: Transition Probability Matrix Induced Feature Clustering",
            "url": "https://arxiv.org/pdf/2511.12180"
          },
          {
            "title": "A Systematic Review of Contrastive Learning in Medical AI: Foundations, Biomedical Modalities, and Future Directions - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12938576/"
          }
        ]
      },
      "I found several recent research papers and resources on contrastive learning, reward model training, and InfoNCE representation learning from 2025-2026. Here are the key findings:\n\n## Recent Work on Contrastive Learning & Reward Models\n\n**GRACE: Generative Representation Learning via Contrastive Policy Optimization** is a prominent 2025-2026 paper that directly addresses combining contrastive learning with reward model training. The approach optimizes a contrastive reward within an RL framework, which aligns updates with the generative policy while using relative, advantage-weighted updates that resist representation collapse and the rescaling/drift common in direct InfoNCE-style training.\n\n## InfoNCE Theory & Ablations\n\nThe InfoNCE loss is the standard objective in self-supervised representation learning and underlies methods such as SimCLR, MoCo, and CLIP. Recent 2025-2026 research has examined the theoretical properties more deeply. Prior work has studied these effects from geometric and optimization perspectives, identifying phenomena such as hyperspherical uniformity and feature concentration.\n\n## Experimental Methodology (GRACE Paper)\n\nThe experimental setup includes: experiments run on a single node with 4× NVIDIA H100 GPUs, with training performed for 2 epochs with a batch size of 64. For supervised training, they use a replication of the public portion of the E5 dataset which contains 1.5M samples.\n\n## Key Challenges\n\nThe effectiveness of InfoNCE is contingent on negative sampling, and excessive negatives under label noise produce misleading loss signals, especially when semantically similar negatives are included."
    ],
    "durationSeconds": 10.337354707000006,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "5a0f39cf-7caa-4c5c-87d4-0cfd67455814",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6ab36dcb-fa57-4a2b-87cc-9d068208d199",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-27T08:56:12.410Z_

```json
{
  "parentUuid": "a8716e15-c157-4275-b975-047ef7dea2ea",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "5dfe67c4-7cd4-49b5-bb8e-5b522df21229",
  "timestamp": "2026-05-27T08:56:12.410Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6ab36dcb-fa57-4a2b-87cc-9d068208d199",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 30 · 2026-05-27T08:56:17.016Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019sV2Snx6Nuk8v5HzVu6S3h`</summary>

```json
{
  "query": "GRPO reinforcement learning reward hacking process reward model closed-loop evaluation 2025 2026 experimental setup"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5dfe67c4-7cd4-49b5-bb8e-5b522df21229",
  "isSidechain": false,
  "requestId": "req_011CbSo3QimGBc8wtJGzKQje",
  "type": "assistant",
  "uuid": "b9daab46-58b2-43db-a863-732f7ee4e7c7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6ab36dcb-fa57-4a2b-87cc-9d068208d199",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SmhphRL8yvUJWYgjQzqJ9m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 906,
      "cache_read_input_tokens": 25558,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 906,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 25558,
          "cache_creation_input_tokens": 906,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 906
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

_source line 31 · 2026-05-27T08:56:24.569Z_

<details><summary>↩ Tool result · `toolu_019sV2Snx6Nuk8v5HzVu6S3h`</summary>

```text
Web search results for query: "GRPO reinforcement learning reward hacking process reward model closed-loop evaluation 2025 2026 experimental setup"

Links: [{"title":"[2509.21154] GRPO is Secretly a Process Reward Model","url":"https://arxiv.org/abs/2509.21154"},{"title":"[2509.22047] MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems","url":"https://arxiv.org/abs/2509.22047"},{"title":"Reinforcement Learning with Verifiable Rewards: GRPO’s Effective Loss, Dynamics, and Success Amplification","url":"https://arxiv.org/html/2503.06639v1"},{"title":"GRPO is Secretly a Process Reward Model","url":"https://arxiv.org/html/2509.21154"},{"title":"GRPO is Secretly a Process Reward Model","url":"https://arxiv.org/pdf/2509.21154"},{"title":"MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems","url":"https://arxiv.org/pdf/2509.22047"},{"title":"Post-Training in 2026: GRPO, DAPO, RLVR & Beyond","url":"https://llm-stats.com/blog/research/post-training-techniques-2026"}]

Based on the web search results, here's what I found regarding GRPO, reinforcement learning, reward hacking, and process reward models in 2025-2026:

## GRPO as a Process Reward Model

The Group Relative Policy Optimization (GRPO) RL algorithm equipped with an ORM is equivalent to a PRM-aware RL objective equipped with a non-trivial, Monte-Carlo-based PRM. A modification called λ-GRPO was proposed to address defects in the standard algorithm, with LLMs tuned with λ-GRPO outperforming those trained with standard GRPO on downstream reasoning tasks.

## Reward Hacking Issues

GRPO is vulnerable to reward hacking in multi-objective settings, optimizing only one of the objectives at the cost of the others. MO-GRPO was proposed as an extension of GRPO with a normalization method to reweight reward functions automatically according to the variances of their values.

Additionally, verifiable rewards balance simplicity and bias and are thought to be less prone to reward hacking than reward models learned from preference data, while reward hacking is a common issue in reinforcement learning where the policy learns to over-optimize a reward leading to lower model quality.

## Experimental Setup and Methods

GRPO samples multiple responses per prompt, scores them, then normalizes rewards within the group, without needing a critic model. Recent work has evaluated GRPO in scenarios with multiple reward models, including practical applications like machine translation tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b9daab46-58b2-43db-a863-732f7ee4e7c7",
  "isSidechain": false,
  "promptId": "d8b72561-4b7c-4874-99b3-296be6c30c18",
  "type": "user",
  "uuid": "ad06f4c1-f13e-4c09-bf6b-1cf04d4020a7",
  "toolUseResult": {
    "query": "GRPO reinforcement learning reward hacking process reward model closed-loop evaluation 2025 2026 experimental setup",
    "results": [
      {
        "tool_use_id": "srvtoolu_013WAFpaYC32ULBQ6jUb4Trk",
        "content": [
          {
            "title": "[2509.21154] GRPO is Secretly a Process Reward Model",
            "url": "https://arxiv.org/abs/2509.21154"
          },
          {
            "title": "[2509.22047] MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems",
            "url": "https://arxiv.org/abs/2509.22047"
          },
          {
            "title": "Reinforcement Learning with Verifiable Rewards: GRPO’s Effective Loss, Dynamics, and Success Amplification",
            "url": "https://arxiv.org/html/2503.06639v1"
          },
          {
            "title": "GRPO is Secretly a Process Reward Model",
            "url": "https://arxiv.org/html/2509.21154"
          },
          {
            "title": "GRPO is Secretly a Process Reward Model",
            "url": "https://arxiv.org/pdf/2509.21154"
          },
          {
            "title": "MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems",
            "url": "https://arxiv.org/pdf/2509.22047"
          },
          {
            "title": "Post-Training in 2026: GRPO, DAPO, RLVR & Beyond",
            "url": "https://llm-stats.com/blog/research/post-training-techniques-2026"
          }
        ]
      },
      "Based on the web search results, here's what I found regarding GRPO, reinforcement learning, reward hacking, and process reward models in 2025-2026:\n\n## GRPO as a Process Reward Model\n\nThe Group Relative Policy Optimization (GRPO) RL algorithm equipped with an ORM is equivalent to a PRM-aware RL objective equipped with a non-trivial, Monte-Carlo-based PRM. A modification called λ-GRPO was proposed to address defects in the standard algorithm, with LLMs tuned with λ-GRPO outperforming those trained with standard GRPO on downstream reasoning tasks.\n\n## Reward Hacking Issues\n\nGRPO is vulnerable to reward hacking in multi-objective settings, optimizing only one of the objectives at the cost of the others. MO-GRPO was proposed as an extension of GRPO with a normalization method to reweight reward functions automatically according to the variances of their values.\n\nAdditionally, verifiable rewards balance simplicity and bias and are thought to be less prone to reward hacking than reward models learned from preference data, while reward hacking is a common issue in reinforcement learning where the policy learns to over-optimize a reward leading to lower model quality.\n\n## Experimental Setup and Methods\n\nGRPO samples multiple responses per prompt, scores them, then normalizes rewards within the group, without needing a critic model. Recent work has evaluated GRPO in scenarios with multiple reward models, including practical applications like machine translation tasks."
    ],
    "durationSeconds": 7.5487704709999965,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "b9daab46-58b2-43db-a863-732f7ee4e7c7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6ab36dcb-fa57-4a2b-87cc-9d068208d199",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-27T08:56:27.558Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EFxXytigkdMoVC7PuxrqnQ`</summary>

```json
{
  "query": "CPMI contrastive mutual information PRM auto-labeling 2026 arXiv 2604.10660"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad06f4c1-f13e-4c09-bf6b-1cf04d4020a7",
  "isSidechain": false,
  "requestId": "req_011CbSo4JjsW8aKNryRGpwFQ",
  "type": "assistant",
  "uuid": "a8672fb9-f4b9-4a6a-b8d7-52dde707e50a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6ab36dcb-fa57-4a2b-87cc-9d068208d199",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J3q7Jca4rS9HUDQQ3ovqgZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 792,
      "cache_read_input_tokens": 26464,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 792,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 78,
          "cache_read_input_tokens": 26464,
          "cache_creation_input_tokens": 792,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 792
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

_source line 33_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Premise-Graph Contrastive Training for Logic-Grounded Process Reward Models  ## Core Problem  Current process reward models detect consistency rather than causality. \"Reward Models Identify Consiste…",
  "leafUuid": "a8672fb9-f4b9-4a6a-b8d7-52dde707e50a",
  "sessionId": "6ab36dcb-fa57-4a2b-87cc-9d068208d199"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Premise-graph contrastive training for process reward models",
  "sessionId": "6ab36dcb-fa57-4a2b-87cc-9d068208d199"
}
```

---

### Tool result

_source line 35 · 2026-05-27T08:56:36.520Z_

<details><summary>↩ Tool result · `toolu_01EFxXytigkdMoVC7PuxrqnQ`</summary>

```text
Web search results for query: "CPMI contrastive mutual information PRM auto-labeling 2026 arXiv 2604.10660"

Links: [{"title":"[2604.10660] Efficient Process Reward Modeling via Contrastive Mutual Information","url":"https://arxiv.org/abs/2604.10660"},{"title":"Efficient Process Reward Modeling via Contrastive Mutual Information","url":"https://arxiv.org/html/2604.10660"},{"title":"Self-Supervised Contrastive Learning of Protein Representations By Mutual Information Maximization","url":"https://www.biorxiv.org/content/10.1101/2020.09.04.283929.full.pdf"},{"title":"Contrastive Mutual Information Learning: Toward Robust Representations without Positive-Pair Augmentations","url":"https://arxiv.org/html/2509.21511"},{"title":"Contrastive MIM: A Contrastive Mutual Information Framework for Unified Generative and Discriminative Representation Learning","url":"https://arxiv.org/html/2411.10548v4"},{"title":"Contrastive Mutual Information Learning: Toward Robust Representations without Positive-Pair Augmentations","url":"https://arxiv.org/pdf/2509.21511"}]

Based on the search results, I found the paper you're looking for:

The arXiv paper 2604.10660 is titled "Efficient Process Reward Modeling via Contrastive Mutual Information", published on April 12, 2026.

**Key Overview:**

The paper addresses the challenge of verifying intermediate reasoning steps in chain-of-thought trajectories using process reward models, which typically requires human annotators to assign reward scores to each reasoning step—a costly and time-consuming process.

**The CPMI Method:**

The authors propose contrastive pointwise mutual information (CPMI), a novel automatic reward labeling method that leverages the model's internal probability to infer step-level supervision while significantly reducing the computational burden of annotating datasets. CPMI quantifies how much a reasoning step increases the mutual information between the step and the correct target answer relative to hard-negative alternatives.

**Results:**

The experimental results show that CPMI-based labeling reduces dataset construction time by 84% and token generation by 98% compared to MC estimation, while achieving higher accuracy on process-level evaluations and mathematical reasoning benchmarks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a8672fb9-f4b9-4a6a-b8d7-52dde707e50a",
  "isSidechain": false,
  "promptId": "d8b72561-4b7c-4874-99b3-296be6c30c18",
  "type": "user",
  "uuid": "0f296aee-9da9-484e-839e-b60bceb2d369",
  "toolUseResult": {
    "query": "CPMI contrastive mutual information PRM auto-labeling 2026 arXiv 2604.10660",
    "results": [
      {
        "tool_use_id": "srvtoolu_014Wpo5T8kMyLfdR7fcfpHRw",
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
            "title": "Contrastive Mutual Information Learning: Toward Robust Representations without Positive-Pair Augmentations",
            "url": "https://arxiv.org/html/2509.21511"
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
      "Based on the search results, I found the paper you're looking for:\n\nThe arXiv paper 2604.10660 is titled \"Efficient Process Reward Modeling via Contrastive Mutual Information\", published on April 12, 2026.\n\n**Key Overview:**\n\nThe paper addresses the challenge of verifying intermediate reasoning steps in chain-of-thought trajectories using process reward models, which typically requires human annotators to assign reward scores to each reasoning step—a costly and time-consuming process.\n\n**The CPMI Method:**\n\nThe authors propose contrastive pointwise mutual information (CPMI), a novel automatic reward labeling method that leverages the model's internal probability to infer step-level supervision while significantly reducing the computational burden of annotating datasets. CPMI quantifies how much a reasoning step increases the mutual information between the step and the correct target answer relative to hard-negative alternatives.\n\n**Results:**\n\nThe experimental results show that CPMI-based labeling reduces dataset construction time by 84% and token generation by 98% compared to MC estimation, while achieving higher accuracy on process-level evaluations and mathematical reasoning benchmarks."
    ],
    "durationSeconds": 8.956161311000004,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "a8672fb9-f4b9-4a6a-b8d7-52dde707e50a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6ab36dcb-fa57-4a2b-87cc-9d068208d199",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-27T08:56:41.793Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012gMZXx8BvsdwLGZmoipnuJ`</summary>

```json
{
  "query": "Qwen2.5-Math-7B PRM training compute cost GPU hours A100 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f296aee-9da9-484e-839e-b60bceb2d369",
  "isSidechain": false,
  "requestId": "req_011CbSo5BsehywbX5JtFEsZa",
  "type": "assistant",
  "uuid": "136f8b7e-6631-4913-a5a1-6ae4a36ed526",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6ab36dcb-fa57-4a2b-87cc-9d068208d199",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qeu3FTHS43TyrTMr2hDJV7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 683,
      "cache_read_input_tokens": 27256,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 683,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 27256,
          "cache_creation_input_tokens": 683,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 683
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

_source line 37 · 2026-05-27T08:56:47.640Z_

<details><summary>↩ Tool result · `toolu_012gMZXx8BvsdwLGZmoipnuJ`</summary>

```text
Web search results for query: "Qwen2.5-Math-7B PRM training compute cost GPU hours A100 2025"

Links: [{"title":"Qwen/Qwen2.5-Math-7B-PRM800K · Hugging Face","url":"https://huggingface.co/Qwen/Qwen2.5-Math-7B-PRM800K"},{"title":"Improving Data Efficiency for LLM Reinforcement Fine- ...","url":"https://arxiv.org/pdf/2506.05316"},{"title":"Qwen/Qwen2.5-Math-PRM-7B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen2.5-Math-PRM-7B"},{"title":"Fine-Tune and Deploy Qwen2.5 - Coder with SFT & DPO on PAI - Alibaba Cloud","url":"https://www.alibabacloud.com/help/en/pai/use-cases/training-evaluation-compression-and-deployment-of-qwen2-5-coder-model"},{"title":"README.md · Qwen/Qwen2.5-Math-PRM-7B at main","url":"https://huggingface.co/Qwen/Qwen2.5-Math-PRM-7B/blob/main/README.md"},{"title":"Small LLMs Can Master Math Reasoning with Self-Evolved ...","url":"https://thenaai.org/uploads/admin/article_thumb/20250210/94b8994058899cefa8eeddddb5865651.pdf"},{"title":"Qwen2.5-Math-PRM: Advanced Math LLM Framework","url":"https://www.emergentmind.com/topics/qwen2-5-math-prm"},{"title":"Fine-Tuning Qwen 2.5 for Advanced Reasoning Tasks on RunPod","url":"https://www.runpod.io/articles/guides/fine-tuning-qwen-2-5-for-advanced-reasoning-tasks"},{"title":"qwen2.5-7b-instruct Model by Qwen","url":"https://build.nvidia.com/qwen/qwen2_5-7b-instruct/modelcard"},{"title":"Qwen 2.5: A Comprehensive Review of the Leading ...","url":"https://www.techrxiv.org/users/638823/articles/1270667/master/file/data/Qwen_2_5/Qwen_2_5.pdf"}]

Based on the search results, I found relevant information about training compute costs for models related to Qwen2.5-Math-7B with PRM (Process Reward Model):

Training samples required over 3,800 A100 GPU hours—equivalent to approximately $4,500 in compute cost, according to a research paper on improving data efficiency for LLM reinforcement fine-tuning that discusses Qwen2.5 models.

Additionally, the search results indicate that the 7B model is trained on 8 A100 GPUs in the context of reinforcement learning fine-tuning experiments for Qwen2.5-Math models.

However, the search results don't contain detailed specifications specifically about the Qwen2.5-Math-7B PRM's original training compute cost. The information found relates to downstream fine-tuning and RL training experiments rather than the initial PRM model training. For the most specific details about the original PRM training compute requirements, you may need to consult the official technical reports or papers referenced in the Hugging Face model card, particularly "The Lessons of Developing Process Reward Models in Mathematical Reasoning" (arXiv:2501.07301, 2025).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "136f8b7e-6631-4913-a5a1-6ae4a36ed526",
  "isSidechain": false,
  "promptId": "d8b72561-4b7c-4874-99b3-296be6c30c18",
  "type": "user",
  "uuid": "d701af74-9859-4913-b75a-941f7499c4c0",
  "toolUseResult": {
    "query": "Qwen2.5-Math-7B PRM training compute cost GPU hours A100 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Fco7Dv7jM3HYNmWnoVEAhs",
        "content": [
          {
            "title": "Qwen/Qwen2.5-Math-7B-PRM800K · Hugging Face",
            "url": "https://huggingface.co/Qwen/Qwen2.5-Math-7B-PRM800K"
          },
          {
            "title": "Improving Data Efficiency for LLM Reinforcement Fine- ...",
            "url": "https://arxiv.org/pdf/2506.05316"
          },
          {
            "title": "Qwen/Qwen2.5-Math-PRM-7B · Hugging Face",
            "url": "https://huggingface.co/Qwen/Qwen2.5-Math-PRM-7B"
          },
          {
            "title": "Fine-Tune and Deploy Qwen2.5 - Coder with SFT & DPO on PAI - Alibaba Cloud",
            "url": "https://www.alibabacloud.com/help/en/pai/use-cases/training-evaluation-compression-and-deployment-of-qwen2-5-coder-model"
          },
          {
            "title": "README.md · Qwen/Qwen2.5-Math-PRM-7B at main",
            "url": "https://huggingface.co/Qwen/Qwen2.5-Math-PRM-7B/blob/main/README.md"
          },
          {
            "title": "Small LLMs Can Master Math Reasoning with Self-Evolved ...",
            "url": "https://thenaai.org/uploads/admin/article_thumb/20250210/94b8994058899cefa8eeddddb5865651.pdf"
          },
          {
            "title": "Qwen2.5-Math-PRM: Advanced Math LLM Framework",
            "url": "https://www.emergentmind.com/topics/qwen2-5-math-prm"
          },
          {
            "title": "Fine-Tuning Qwen 2.5 for Advanced Reasoning Tasks on RunPod",
            "url": "https://www.runpod.io/articles/guides/fine-tuning-qwen-2-5-for-advanced-reasoning-tasks"
          },
          {
            "title": "qwen2.5-7b-instruct Model by Qwen",
            "url": "https://build.nvidia.com/qwen/qwen2_5-7b-instruct/modelcard"
          },
          {
            "title": "Qwen 2.5: A Comprehensive Review of the Leading ...",
            "url": "https://www.techrxiv.org/users/638823/articles/1270667/master/file/data/Qwen_2_5/Qwen_2_5.pdf"
          }
        ]
      },
      "Based on the search results, I found relevant information about training compute costs for models related to Qwen2.5-Math-7B with PRM (Process Reward Model):\n\nTraining samples required over 3,800 A100 GPU hours—equivalent to approximately $4,500 in compute cost, according to a research paper on improving data efficiency for LLM reinforcement fine-tuning that discusses Qwen2.5 models.\n\nAdditionally, the search results indicate that the 7B model is trained on 8 A100 GPUs in the context of reinforcement learning fine-tuning experiments for Qwen2.5-Math models.\n\nHowever, the search results don't contain detailed specifications specifically about the Qwen2.5-Math-7B PRM's original training compute cost. The information found relates to downstream fine-tuning and RL training experiments rather than the initial PRM model training. For the most specific details about the original PRM training compute requirements, you may need to consult the official technical reports or papers referenced in the Hugging Face model card, particularly \"The Lessons of Developing Process Reward Models in Mathematical Reasoning\" (arXiv:2501.07301, 2025)."
    ],
    "durationSeconds": 5.842877995000017,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "136f8b7e-6631-4913-a5a1-6ae4a36ed526",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6ab36dcb-fa57-4a2b-87cc-9d068208d199",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-27T08:58:21.613Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough information from my research. Let me compile my analysis as the 补救 agent, focusing on experimental design and technical execution completeness.

Let me assess the proposal's experimental design:

1. **Baselines**: The proposal lists 6 tiers of baselines which is quite comprehensive:
   - Standard PRM: Qwen2.5-Math-PRM-7B
   - Robustness-focused: APRM, CRA
   - Architecture-level: CRM, PURE
   - Contrastive/concurrent: CPMI
   - Error-aware: PathFinder-PRM-7B
   - Reasoning-enhanced: R-PRM, GenPRM-7B, ThinkPRM-7B
   - Data-matched and compute-matched controls

The baseline selection is thorough, covering both discriminative and generative approaches across different optimization targets. However, I notice that "Factored Causal Representation Learning" and "When Reward Hacking Rebounds" appear in the related work but aren't included as baselines—since PGCT also operates at the representation level, these would be valuable comparisons to include.

Though those papers might be too recent or different in scope to work as direct baselines, RewardFlow could be a stronger candidate since it also leverages graph structure through reward propagation over state transitions. The benchmark suite itself is solid: step-level detection on PRMBench and ProcessBench, downstream performance on MATH500 and competition math datasets, adversarial robustness testing, closed-loop RL evaluation, and representation analysis through probing and similarity metrics.

The ablation plan covers the key components—loss terms, DAG structure contribution, pair selection strategies, weighting schemes, noise robustness, and model scale—which should isolate where the gains come from. The resource requirements look reasonable at 1600-2200 A100 hours for the full pipeline with an 18-22 week timeline, using Qwen2.5-72B for DAG extraction. Now I'm checking what might be missing from the evaluation setup.

RewardFlow keeps coming up in the related work as a concurrent graph-based approach, so it really should be included as a baseline rather than just mentioned in context. That's a notable gap for fair comparison.

The contrastive pair generation and quality assurance is concerning—generating 600K pairs but only auditing 1000 of them across multiple stratification dimensions (math subdomains, DAG complexity, difficulty levels) seems like it could leave blind spots. The human audit might be too sparse to catch systematic quality issues at scale.

There's also the question of whether the comparisons with R-PRM, GenPRM, and ThinkPRM are truly compute-normalized, since inference costs can vary significantly between approaches.

On the DAG extraction side, PARC's >90% recall was validated on GSM8K and MATH, but it's unclear how well that holds up on out-of-distribution problems like AIME and AMC where the math is significantly harder. The proposal doesn't really address potential degradation on competition-level problems.

The statistical rigor is also a bit loose—the RL experiments mention 3 seeds, but other experiments don't specify how many runs or whether significance testing was done, and best-of-N results can have high variance without proper statistical treatment.

I'm also noticing they don't compare against outcome reward models, which are a standard baseline in recent PRM work, though I suppose since this is specifically about improving PRMs that might be less critical than the PRM-to-PRM comparisons they already have.

The negative pair construction through "graph-breaking fluent perturbations" needs more clarity on the mechanics—how exactly are premise links being severed, and if it's LLM-based paraphrasing, how do we guarantee the perturbation is subtle enough to be a challenging negative while remaining logically invalid? The difficulty-aware threshold they mention (baseline PRM score >0.7 for >30% of negatives) feels somewhat arbitrary without justification.

And then there's the scope issue—the entire evaluation is limited to mathematical reasoning tasks.

Since they're explicitly positioning this as a mathematical reasoning paper, that's probably acceptable, though it does constrain generalizability claims. I'm also noticing the InfoNCE loss doesn't discuss temperature tuning, which is typically crucial for contrastive learning and should at least be ablated. The representation analysis could be strengthened with CKA comparisons across layers beyond just the linear probing and t-SNE visualizations they mention.

Ranking these by impact: DAG extraction quality on harder problems is the most serious since it affects reliability, followed by whether the contrastive pair audit is thorough enough, then the statistical significance details, missing baselines like RewardFlow, and finally the InfoNCE temperature sensitivity.

Actually, stepping back—this proposal is genuinely comprehensive. The baseline coverage is extensive with over 10 methods plus matched controls, the ablations span 8 variants, and the evaluation is multi-layered. Most of my concerns are actually minor and fixable. I should calibrate my assessment accordingly.

On RewardFlow specifically, I'm reconsidering whether it even belongs as a baseline since it operates fundamentally differently—it propagates rewards over graphs at inference time rather than using contrastive training during training like PGCT does, so they're solving somewhat different problems.

But looking at the full baseline set, they already have solid coverage. The real test is whether any baseline directly challenges PGCT's core claim about premise-dependency awareness improving robustness. The A3 ablation—comparing DAG-aware perturbation against random perturbation—already isolates this contribution and is marked critical, which is the right design choice.

Overall the experimental design holds up well. There are specific improvements worth making, but nothing fundamental is broken here.

Actually, I need to think more carefully about the contrastive pair construction itself. The quality of those ~600K pairs is crucial—if the graph-preserving pairs accidentally alter logical structure or the graph-breaking pairs are too obvious, the whole contrastive training fails. Looking at their quality assurance: they re-extract DAGs to verify topology, run stratified human audits on ~1000 pairs, enforce thresholds of ≥90% topology preservation for positives and ≥85% premise-link corruption for negatives, and measure inter-annotator agreement. This is actually quite rigorous—the automated verification alone is a solid safeguard.

The human audit sample of 1000 is reasonable for a proposal, though the stratification across math subdomains, DAG complexity, and difficulty levels could create sparse coverage in some strata. If there are 45 strata, that's only ~22 pairs per stratum, which might be tight depending on what they're trying to validate. That said, it's a detail they can refine during execution.

Now looking at the RL closed-loop experiment—they're doing GRPO training on Qwen2.5-Math-7B-Instruct with 3000-5000 steps and checkpointing every 200 steps.

They'll evaluate on MATH and AIME using hacking gap, reward-accuracy correlation, and late-stage divergence ratio across 3 seeds. This directly tests the core claim, and while 3 seeds is minimal, it's acceptable. The checkpoint evaluation gives good visibility into training dynamics. The main question is whether 3000-5000 steps is sufficient for reward hacking to emerge—prior work suggests it can happen quickly, but the exact threshold depends on their specific setup.

I think ORM could be mentioned as a baseline since it's standard in PRM literature, but it's not critical here since they're already comparing against a standard PRM and PGCT is specifically about improving PRMs.

Now looking at feasibility: the compute breakdown spans DAG extraction, pair generation with quality checks, PRM training with ablations, baseline reproduction, and RL experiments across seeds—totaling around 1600-2200 A100-hours. For a group with a modest cluster, that's roughly 2-3 months of compute time, which fits their 18-22 week timeline reasonably well.

The cost estimate of $4,800-$6,600 at spot pricing seems realistic, though I'm realizing the baseline reproduction budget might be tight. Some methods like Qwen2.5-Math-PRM and PathFinder-PRM are publicly available, which helps, but others like APRM, CRA, CRM, PURE, CPMI, R-PRM, and ThinkPRM might require retraining—and 150 A100-hours might not be sufficient if multiple baselines need to be reproduced from scratch.

The timeline is also concerning. With AAAI 2026 submissions likely due in August and only about 12-14 weeks from now, the "manual" approach feels risky, though the "human_in_loop" timeline of 13-17 weeks might just barely fit depending on the exact deadline.

But I should focus on the experimental design itself rather than speculating about dates. The main issues I'm seeing are that the RL experiment specifies 3 seeds for statistical rigor, but the other experiments like best-of-N and step-level detection don't have clear statistical testing protocols—that's going to be a reviewer concern. And the 150 A100-hours budget for reproducing 10+ baselines might not be enough, especially if some aren't readily available.

There are also some missing ablations on critical hyperparameters like InfoNCE temperature and embedding dimension, which are known to matter a lot for contrastive learning. The DAG extraction results look strong on PARC with >90% recall, but those are relatively easier datasets—I'm wondering how it'll hold up on harder competition-level math problems like AIME. The human audit sample sizes could be problematic too if they're stratifying finely and end up with too few examples in some strata. And RewardFlow seems like an obvious baseline to include since it also leverages graph structure for process reward modeling.

These are all fixable issues though, and overall the experimental design is solid. Let me put together my feedback.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d701af74-9859-4913-b75a-941f7499c4c0",
  "isSidechain": false,
  "requestId": "req_011CbSo61LvR6GnLiuVdGR9q",
  "type": "assistant",
  "uuid": "b4cadc8a-7617-42ec-8659-14673a80c2b7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6ab36dcb-fa57-4a2b-87cc-9d068208d199",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NihV6MKuFwLBWcyRZqhNUo",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1001,
      "cache_read_input_tokens": 27939,
      "output_tokens": 9216,
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
          "output_tokens": 9216,
          "cache_read_input_tokens": 27939,
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

### Assistant

_source line 39 · 2026-05-27T09:00:20.328Z_

Now I have sufficient research to provide a thorough assessment. Let me compile my analysis.

---

【状态】: 有缺陷待补救

【前置调研发现】
- **PathFinder-PRM (arXiv:2505.19706, 2025)**: 实验设计要点：在 PRMBench 和 ProcessBench 上评测，baselines 包括 Qwen2.5-Math-PRM、Math-Shepherd-PRM 等标准 PRM，以及 GPT-4o 等 LLM-as-Judge；报告了 prm@N 指标；用 400K 样本训练，强调数据效率。关键：该论文将误差分解为 math error 和 consistency error 两个维度，实验中用 per-error-category breakdown 证明各类别贡献。
- **APRM (arXiv:2511.22888, 2025)**: 实验设计要点：adversarial generator-PRM 博弈训练；ablation 包括 entropy regularization 和 OGDA optimizer 的必要性验证；评测 ID 和 OOD 泛化（+5.3pp OOD）；使用多种 math benchmark。
- **CRM (arXiv:2509.26578, ICLR 2026)**: 实验设计要点：在 Best-of-N、beam search 和 RL 三种下游任务上评测；ablation 包括 adversarial data filtering、task-specific loss weighting、ensemble uncertainty；强调 step-level reward 与 outcome 的条件概率关系。
- **GenPRM (arXiv:2504.00891, AAAI 2026)**: 实验设计要点：1.5B GenPRM 超越 GPT-4o，7B GenPRM 超越 Qwen2.5-Math-PRM-72B on ProcessBench；关键对比维度是 inference compute scaling（thinking longer vs. more samples）。
- **ThinkPRM (arXiv:2504.16828, 2025)**: 实验设计要点：仅用 1% PRM800K 标签训练，在 fixed token budget 下与 LLM-as-Judge 和 discriminative verifiers 对比；强调 compute-performance tradeoff curve。
- **CPMI (arXiv:2604.10660, 2026)**: 实验设计要点：contrastive MI 用于 PRM auto-labeling，减少 84% dataset construction time 和 98% token generation；在 ProcessBench 和数学推理 benchmark 上评测。
- **PARC/PERL (arXiv:2502.02362, ICML 2025)**: 实验设计要点：70B+ 模型 premise extraction recall >90%；评测数据集包括 GSM8K、MATH、Orca-Math、MetaMathQA；error identification accuracy 提升 6-16%。
- **GRACE (ICLR 2026, arXiv:2510.04506)**: contrastive reward optimization 中强调 InfoNCE 温度参数和 negative sampling 策略的关键性，实验中包含 temperature sensitivity 分析。

- **调研总结**: 该领域当前实验设计标准要求：(1) 至少在 PRMBench + ProcessBench 上做 step-level 评测并报告 per-category breakdown；(2) downstream best-of-N 必须覆盖 ID/OOD split；(3) RL closed-loop 实验需要多 seed + reward-accuracy correlation 分析；(4) 对 generative PRM (GenPRM/ThinkPRM) 的对比需要明确 inference compute normalization 方法；(5) contrastive learning 方法需要包含 temperature sensitivity 分析。审稿人普遍期望 ablation 能隔离每个组件的贡献，并要求 statistical significance reporting。

---

【缺陷 1】
- 类别: 实验设计不足（统计显著性协议不完整）
- 问题: Proposal 的 RL closed-loop 实验明确指定了 3 seeds 和 95% CI，但其他关键实验——特别是 step-level error detection（PRMBench/ProcessBench）和 best-of-N reranking（MATH500/GSM8K/AIME/AMC）——没有指定种子数量、置信区间或统计显著性检验方法。Best-of-N 实验因 sampling variance 天然方差较大，单次实验结果不足以支撑 claim。这是 AAAI 审稿人几乎必问的问题。
- 严重度: 可补救
- 补救方案: (1) 所有 best-of-N 实验统一使用 ≥3 seeds（不同 candidate solution 采样），报告 mean ± std 和 95% CI；(2) PRMBench/ProcessBench 的 step-level detection 虽然是确定性推理（给定模型输出是确定的），但应报告 bootstrap 置信区间（对测试样本重采样）来量化评估的可靠性；(3) 关键对比使用 paired t-test 或 Wilcoxon signed-rank test 报告 p-value。建议在 Evaluation Plan 中增加一个统一的「Statistical Protocol」段落。
- 调研依据: PathFinder-PRM 和 ThinkPRM 论文均在 best-of-N 实验中报告多次采样结果的统计量；CRM 论文在 RL 实验中使用多 seed 并报告方差。

【缺陷 2】
- 类别: baseline 不足或过时
- 问题: Proposal 在 Research Landscape 中讨论了 **RewardFlow (arXiv:2603.18859)** 作为 concurrent work（"propagates rewards over state-transition graphs without contrastive training"），但未将其纳入 baseline 对比。RewardFlow 同样使用图结构进行 PRM reward 计算，与 PGCT 共享"利用推理步骤间依赖关系"这一核心思路，差异仅在于方法路径（inference-time propagation vs. training-time contrastive learning）。审稿人很可能要求这一对比来验证 PGCT 的 training-time structural injection 相比 inference-time graph propagation 的优势。
- 严重度: 可补救
- 补救方案: 将 RewardFlow 加入 Baselines 第 4 tier（Contrastive/concurrent），或单独创建一个 "Graph-based" tier。如果 RewardFlow 没有公开代码/模型，至少需要 (a) 在实验中说明为什么无法直接对比，(b) 基于论文报告的数字在共同 benchmark 上做间接比较。如果有代码可用，则在 PRMBench 和 best-of-N 上直接对比。
- 调研依据: 基于领域实验规范判断——当 related work 中讨论了功能高度相关的方法而不做实验对比时，审稿人通常会要求补充。

【缺陷 3】
- 类别: ablation 不完整（InfoNCE 关键超参数敏感性缺失）
- 问题: 当前 8 个 ablation 涵盖了 loss 组件、DAG 结构贡献、正负样本贡献、loss weighting、DAG 噪声鲁棒性和提取模型规模，覆盖面很广。但遗漏了 **InfoNCE 温度参数 τ 的敏感性分析**。InfoNCE 的温度参数是 contrastive learning 中公认的最关键超参数之一，直接影响 hard negative 的梯度权重分配和表示空间的均匀性。A6 虽然测试了 BCE/InfoNCE 的 loss weighting λ，但这与温度参数 τ 的效果是正交的。
- 严重度: 可补救
- 补救方案: 增加 **A9: InfoNCE temperature τ ∈ {0.01, 0.05, 0.1, 0.2, 0.5}**。此外可选增加 **A10: negative sample batch size（InfoNCE 的 negative 数量）** 的影响，因为 proposal 没有明确 InfoNCE 的 batch/negative 采样策略。这两个实验计算开销很小（共增加约 5-7 个 training run），但能大幅加强 contrastive learning 方法论的可信度。
- 调研依据: GRACE (ICLR 2026) 明确在实验中包含 temperature sensitivity 分析；SimCLR/MoCo 等经典 contrastive learning 论文均将温度视为核心超参数。InfoNCE 相关综述 (emergentmind) 也强调 negative sampling 和温度的关键性。

【缺陷 4】
- 类别: 可行性问题（DAG 提取在 OOD 高难度问题上的质量未验证）
- 问题: Proposal 引用 PARC/PERL 的 >90% recall 作为 DAG 提取可行性依据，但 PARC 的评测数据集为 GSM8K、MATH、Orca-Math、MetaMathQA——均为训练分布内或中等难度问题。Proposal 的 OOD 评测包括 AIME 2024 和 AMC，这些竞赛级问题的推理链更长、逻辑结构更复杂、前提依赖更隐含。Proposal 在 Ablation A8 中测试了 DAG 提取模型规模（7B/32B/72B），但这是在训练数据上的测试，未明确验证在 OOD 竞赛级问题上的提取质量。如果 OOD 上 DAG 提取质量显著下降，PGCT 在 OOD 评测上的结果将不可靠——因为不清楚性能差异来自方法本身还是 DAG 提取质量。
- 严重度: 可补救
- 补救方案: (1) 在实验中增加一个 "DAG Extraction Quality Audit" 实验：随机采样 100-200 条 AIME/AMC 推理链，人工标注 ground-truth premise dependencies，然后测量 PARC+Qwen2.5-72B 在这些数据上的 precision/recall/F1。这是一个一次性成本（~20-30 人工小时），但对结果可信度至关重要。(2) 在 A7（DAG noise injection）的分析中，明确讨论如果 OOD DAG extraction recall 降到 X% 时，PGCT 的性能如何退化——这样 A7 可以同时回答"DAG 提取在 OOD 上如果不完美，方法是否 robust"的问题。(3) Proposal 提到 "Per-difficulty DAG extraction quality audit (easy/medium/hard/competition)" 但仅出现在 pair construction 的 QA 环节，建议将其提升为一个独立的实验分析点，并报告具体数字。
- 调研依据: PARC (arXiv:2502.02362) 实验中的 recall 数据来源于 GSM8K/MATH 等中等难度数据集，论文本身未验证竞赛级问题上的提取质量。

【缺陷 5】
- 类别: 评估方案缺陷（inference compute normalization 不够具体）
- 问题: Proposal 在 baselines 中提到 R-PRM、GenPRM-7B、ThinkPRM-7B "all under fixed inference-compute budget for fair comparison; unrestricted comparison also reported"。但没有具体定义 inference compute 的度量方式。GenPRM 和 ThinkPRM 是 generative PRMs，推理时生成 CoT reasoning，其计算开销与 PGCT（discriminative PRM，单次前向传播）有数量级差异。如果 compute budget 定义不清晰，审稿人可能质疑对比的公平性——特别是如果 PGCT 在 unrestricted 对比中输给 generative PRM，但在 compute-matched 对比中胜出，读者需要理解这个 tradeoff。
- 严重度: 可补救
- 补救方案: 明确定义 inference compute budget 的度量标准：建议采用 **total generated tokens per problem**（而非 wall-clock time 或 FLOPs，因为前者更可复现且不依赖硬件）。具体做法：(a) 对 PGCT 统计 inference 时的 input tokens × forward passes；(b) 对 GenPRM/ThinkPRM 统计 generated CoT tokens + verification tokens；(c) 绘制 **compute-performance Pareto curve**（x 轴：inference tokens/problem，y 轴：accuracy），这是 ThinkPRM 论文中已有的做法，审稿人对此格式很熟悉。(d) 选取 2-3 个 fixed compute levels 做 snapshot 对比。
- 调研依据: ThinkPRM (arXiv:2504.16828) 在 fixed token budget 下对比 LLM-as-Judge 和 discriminative verifiers，已建立这一对比范式；GenPRM 的实验也强调 test-time compute scaling。

【缺陷 6】
- 类别: 可行性问题（baseline 复现预算偏紧）
- 问题: Resource Estimate 中为 "baseline reproduction/evaluation" 分配 ~150 A100-hours。但 baseline 列表包含 10+ 方法（APRM、CRA、CRM、PURE、CPMI、PathFinder-PRM、R-PRM、GenPRM、ThinkPRM + 2 个 controls）。部分 baseline（如 PathFinder-PRM、GenPRM、ThinkPRM）有公开权重和代码，仅需 evaluation；但 APRM、CRA、CRM、PURE、CPMI 可能需要部分或完全复现（取决于是否有公开 checkpoint、是否在相同 base model 上训练、是否在相同 benchmark 上有报告数字）。此外，Data-matched control 和 Compute-matched control 明确需要从头训练。如果有 3-4 个 baseline 需要复现（每个 7B 模型训练约 30-50 A100-hours），加上两个 control 训练，150 hours 可能不够。
- 严重度: 可补救
- 补救方案: (1) 在 proposal 中明确区分 "需要复现训练" vs. "直接使用公开 checkpoint 评测" 的 baselines，按此分别估算预算；(2) 对无公开 checkpoint 的 baseline（如 APRM、CPMI），检查其代码和数据可用性——如果代码公开但需要在 Qwen2.5-Math-7B 上 retrain（以确保 base model 一致），预留足够时间；(3) 如果某些 baseline 确实无法复现，可在论文中引用其论文报告的数字做 "reported results" 对比（标注清楚），同时在可复现的 baseline 上做 "reproduced results" 对比。建议将 baseline reproduction 预算上调至 250-350 A100-hours。(4) 两个 controls (data-matched, compute-matched) 的训练预算应单独列出，目前似乎被归入 "PRM training + 8 ablations" 的 ~550h 中，如是则问题不大，但需确认。
- 调研依据: 基于领域实验规范判断——AAAI 审稿人重视 controlled comparison（same base model, same data scale），直接使用不同 base model 的公开 checkpoint 会被质疑公平性。

【缺陷 7】
- 类别: 实验设计不足（contrastive pair 构造的 difficulty-aware 阈值缺乏理论/实证依据）
- 问题: Proposal 中指定 "score all hard negatives with a baseline PRM to ensure sufficient proportion (>30%) of genuinely hard cases (baseline PRM score >0.7)"。这两个数字（30% 和 0.7）看似合理但缺乏依据——为什么不是 20% 或 40%？为什么 PRM score 阈值是 0.7 而不是 0.6 或 0.8？在 contrastive learning 中，hard negative ratio 和 difficulty level 直接影响训练动态和最终性能。如果这些是 pilot experiment 的结果，应说明；如果是超参数，应纳入消融实验。
- 严重度: 可补救
- 补救方案: (1) 最简方案：承认这些是需要调优的超参数，在 A6（loss weighting）旁边增加一个 **hard negative ratio sensitivity 消融**（如 >20%、>30%、>40% hard negatives at threshold 0.7）和 **difficulty threshold 消融**（如 threshold 0.5、0.6、0.7、0.8）。计算开销极小（可在训练数据的 subset 上做 pilot experiment）。(2) 更好的方案：在论文中引用 curriculum learning 或 hard negative mining 文献（如 HN-Mine, ANCE 等）来 justify 这些选择，或报告 pilot experiment 的结果说明选择依据。
- 调研依据: 基于 contrastive learning 领域实验规范——SimCLR、MoCo、ANCE 等工作均将 hard negative 策略视为关键设计选择并做了充分消融。

---

**整体评估**: 这份 proposal 的实验设计已经非常扎实——6 tier baselines（含 data/compute-matched controls）、5 tier evaluation、8 ablation variants，在 proposal 阶段已远超多数投稿。上述 7 个缺陷均为**可补救**的技术细节层面问题，无方向性致命缺陷。其中**缺陷 1（统计显著性）和缺陷 4（OOD DAG 提取质量）**对审稿人说服力影响最大，建议优先处理。其余缺陷补救成本较低（主要是增加少量实验 run 或在写作中明确定义），均可在实验执行阶段解决。

Sources:
- [PRMBench (arXiv:2501.03124)](https://arxiv.org/abs/2501.03124)
- [PathFinder-PRM (arXiv:2505.19706)](https://arxiv.org/abs/2505.19706)
- [APRM (arXiv:2511.22888)](https://arxiv.org/abs/2511.22888)
- [CRM (arXiv:2509.26578)](https://arxiv.org/abs/2509.26578)
- [Reward Under Attack (arXiv:2603.06621)](https://arxiv.org/abs/2603.06621)
- [PARC/PERL (arXiv:2502.02362)](https://arxiv.org/abs/2502.02362)
- [GenPRM GitHub](https://github.com/RyanLiu112/GenPRM)
- [ThinkPRM (arXiv:2504.16828)](https://arxiv.org/abs/2504.16828)
- [CPMI (arXiv:2604.10660)](https://arxiv.org/abs/2604.10660)
- [GRACE (ICLR 2026)](https://arxiv.org/pdf/2510.04506)
- [Awesome-Process-Reward-Models](https://github.com/RyanLiu112/Awesome-Process-Reward-Models)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4cadc8a-7617-42ec-8659-14673a80c2b7",
  "isSidechain": false,
  "requestId": "req_011CbSo61LvR6GnLiuVdGR9q",
  "type": "assistant",
  "uuid": "7d0887ec-5d32-48cf-81ff-34becd6e50df",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6ab36dcb-fa57-4a2b-87cc-9d068208d199",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NihV6MKuFwLBWcyRZqhNUo",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1001,
      "cache_read_input_tokens": 27939,
      "output_tokens": 9216,
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
          "output_tokens": 9216,
          "cache_read_input_tokens": 27939,
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

### Runtime record

_source line 40_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Premise-Graph Contrastive Training for Logic-Grounded Process Reward Models  ## Core Problem  Current process reward models detect consistency rather than causality. \"Reward Models Identify Consiste…",
  "leafUuid": "7d0887ec-5d32-48cf-81ff-34becd6e50df",
  "sessionId": "6ab36dcb-fa57-4a2b-87cc-9d068208d199"
}
```

---

### Runtime record

_source line 41_

```json
{
  "type": "ai-title",
  "aiTitle": "Premise-graph contrastive training for process reward models",
  "sessionId": "6ab36dcb-fa57-4a2b-87cc-9d068208d199"
}
```

---

### Runtime record

_source line 42_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Premise-Graph Contrastive Training for Logic-Grounded Process Reward Models  ## Core Problem  Current process reward models detect consistency rather than causality. \"Reward Models Identify Consiste…",
  "leafUuid": "7d0887ec-5d32-48cf-81ff-34becd6e50df",
  "sessionId": "6ab36dcb-fa57-4a2b-87cc-9d068208d199"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "ai-title",
  "aiTitle": "Premise-graph contrastive training for process reward models",
  "sessionId": "6ab36dcb-fa57-4a2b-87cc-9d068208d199"
}
```

---
