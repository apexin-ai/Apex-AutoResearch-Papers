# Research conversation: Premise-Graph Contrastive Training for Logic-Grounded Process Reward Models ## Core Problem Current process reward model

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 47
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-2/9d15703d-7612-480c-9cbd-2adbcb5cdf2b.jsonl`
- **Structured JSON:** [`be8da9529961499e5d78.json`](../../sessions/be/be8da9529961499e5d78.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-27T08:54:32.046Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T08:54:32.046Z",
  "sessionId": "9d15703d-7612-480c-9cbd-2adbcb5cdf2b",
  "content": "# Premise-Graph Contrastive Training for Logic-Grounded Process Reward Models\n\n## Core Problem\n\nCurrent process reward models detect consistency rather than causality. \"Reward Models Identify Consistency, Not Causality\" (arXiv:2502.14619, Feb 2025) established that PRMs verify surface-level coherence between steps — not whether each step logically follows from its premises. \"Reward Under Attack\" (arXiv:2603.06621, Feb 2026) quantified the consequences: 43% of PRM reward gains stem from stylistic shortcuts, and RL-trained policies achieve >0.9 PRM scores but <4% actual accuracy. The root cause is that standard PRM training provides only point-wise step-correctness supervision, which is blind to the logical dependency structure connecting reasoning steps. Can we train PRMs whose representations explicitly encode premise-dependency awareness rather than mere surface consistency?\n\n## Research Opportunity and Key Insight\n\nA critical representation-utilization gap exists in current PRMs. \"From Chains to DAGs\" (arXiv:2601.17593, Jan 2026) proved that LLM hidden states already linearly encode DAG reasoning structure — node depth, pairwise distance, and adjacency are recoverable from intermediate layers via lightweight probes. Yet standard PRM training fails to channel this latent structural knowledge into reward prediction (arXiv:2502.14619). PARC/PERL (ICML 2025, arXiv:2502.02362) demonstrated that premise dependency links are extractable at >90% recall (on 70B+ models), improving error detection by 6-16%. DAG-Math (arXiv:2510.19842, 2025) and ProofFlow (arXiv:2510.15981, 2025) further established feasibility of dependency graph extraction at scale.\n\nOur key insight: contrastive training anchored to premise dependency DAGs can bridge this representation-utilization gap. By constructing training pairs that hold surface form constant while varying logical structure (and vice versa), we force the PRM's embedding space to explicitly encode premise-dependency relationships — activating structural representations the model already possesses but that point-wise BCE training leaves dormant. This constitutes a shift from point-wise supervision (each step independently correct/incorrect) to relational supervision (structural relationships between steps encoded in representation space). An alternative approach — using linear probes as auxiliary loss to directly maximize DAG-structure recovery in hidden states — would only optimize local-layer information retention without affecting cross-layer representation flow or end-to-end reward prediction; contrastive training directly constrains the reward-relevant embedding space, providing end-to-end structural injection.\n\n## Research Landscape\n\n**PRM robustness: existing defenses.** \"Reward Under Attack\" (arXiv:2603.06621) established the three-tier diagnostic: static perturbation exploitability, adversarial token-level attacks, and RL-induced reward hacking. Defenses include CRA (Aug 2025, arXiv:2508.04216, post-hoc SAE correction), APRM (Nov 2025, arXiv:2511.22888, adversarial harder negatives, +5.3pp OOD), CRM (ICLR 2026, arXiv:2509.26578, sequential conditioning), and PURE (NeurIPS 2025, arXiv:2504.15275, min-form credit aggregation). None uses explicit logical dependency structure in PRM training. APRM's adversarial negatives improve the single-step classification decision boundary but remain domain-agnostic — the PRM learns to resist specific patterns without understanding why they are wrong, leaving it vulnerable to novel attacks (cat-and-mouse problem). PGCT instead reorganizes the PRM's representation space around premise-dependency topology.\n\n**Representation-level robustness.** Factored Causal Representation Learning (ICML 2026, arXiv:2601.21350) decomposes reward model embeddings into causal/non-causal factors via gradient reversal. \"When Reward Hacking Rebounds\" (arXiv:2604.01476, April 2026) extracts shortcut concept directions from contrastive pairs via representation engineering. Both operate in representation space but use domain-agnostic statistical separation (gradient reversal, concept directions). PGCT differs fundamentally: its structural prior is domain-grounded — premise dependency DAGs extracted from mathematical reasoning chains — rather than learned statistical factors. This provides interpretable, verifiable structural constraints rather than latent factor separation.\n\n**Reasoning-enhanced PRMs.** R-PRM (arXiv:2503.21295, 2025) augments PRMs with reasoning-driven critique (+11.9 F1 on ProcessBench, +8.5 on PRMBench). GenPRM (AAAI 2026, arXiv:2504.00891) uses generative CoT + code verification. ThinkPRM (arXiv:2504.16828, 2025) achieves strong results with only 1% PRM800K labels via generative verification. These enhance inference-time reasoning. PGCT is orthogonal: it improves training-time representation learning, and could serve as a backbone for generative verification methods.\n\n**Graph structure for verification.** CRV (ICLR 2026, arXiv:2510.09312) verifies reasoning via attribution graph structural fingerprints (white-box, inference-time). GoV decomposes reasoning into DAGs for training-free verification. AgentEval (arXiv:2604.23581, 2026) shows DAG-based dependency modeling yields +22pp failure detection recall. Multiple independent lines confirm graph structure carries powerful verification signal. **Existing approaches either reorganize representation space without domain-specific logical structure (Factored Causal RL) or leverage graph structure only at inference time (GoV, CRV). PGCT is the first to inject premise-dependency topology directly into training-time representation learning.**\n\n**Concurrent contrastive/graph approaches.** CPMI (arXiv:2604.10660, April 2026) uses contrastive MI for PRM auto-labeling without dependency graphs. RewardFlow (arXiv:2603.18859, March 2026) propagates rewards over state-transition graphs without contrastive training. Thought-Path Contrastive Learning (AAAI 2025, arXiv:2409.14495) constructs premise-oriented contrastive examples for logical reading comprehension but operates on propositional-level pairs, not multi-step mathematical DAGs, and targets reading accuracy rather than PRM robustness.\n\n**Performance gap.** Best open-source PRM on PRMBench: 67.7 (PathFinder-PRM-7B, arXiv:2505.19706) vs. 83.8 human ceiling.\n\n## Proposed Approach\n\n**DAG extraction.** Extract premise dependency DAGs from mathematical reasoning chains using PARC's method with Qwen2.5-72B-Instruct (targeting >90% recall per PERL results on 70B-class models; ICML 2025, arXiv:2502.02362). Each reasoning step is a node; directed edges encode \"step j uses the result of step i as a premise.\"\n\n**Contrastive pair construction.** Two types of structure-aware pairs: (1) Graph-preserving surface perturbations (rephrased steps, identical DAG topology) as positives; (2) Graph-breaking fluent perturbations (severed premise links, dangling references, logically invalid steps maintaining surface fluency) as hard negatives. Difficulty-aware construction: score all hard negatives with a baseline PRM to ensure sufficient proportion (>30%) of genuinely hard cases (baseline PRM score >0.7). Quality assurance: re-extract DAGs from generated pairs to verify topology preservation/breaking; stratified human audit (~1000 pairs across math subdomains × DAG complexity × difficulty levels) with thresholds (topology preservation ≥90% for positives, premise-link corruption verification ≥85% for negatives) and inter-annotator agreement (2 annotators, Cohen's κ on ~200-pair overlap). Per-difficulty DAG extraction quality audit (easy/medium/hard/competition).\n\n**Dual objective training.** Qwen2.5-Math-7B-Instruct-based PRM with: (a) standard step-correctness BCE loss (point-wise supervision), and (b) graph-contrastive InfoNCE loss over DAG-anchored step embeddings (relational supervision — \"same DAG topology → nearby embeddings, different topology → distant embeddings\"). This complements CRM (ICLR 2026, arXiv:2509.26578), which conditions sequentially on preceding steps but operates in point-wise prediction paradigm without encoding relational structure in embedding space.\n\n**Scope clarification.** PGCT trains two complementary capabilities: (1) structural dependency sensitivity — detecting whether premise links between steps are correctly maintained (via DAG topology contrastive learning), and (2) partial semantic inference validity — detecting logically invalid reasoning preserving surface fluency (via graph-breaking hard negatives). We claim premise-dependency awareness substantially narrows the consistency-causality gap, not full logical causality verification.\n\n**Data.** PRM800K + Math-Shepherd (~300K solutions) + ~600K contrastive pairs via LLM paraphrasing (7B/32B for generation, 72B for quality verification) and targeted premise-link corruption.\n\n## Evaluation Plan\n\n**Benchmarks (5-tier, with ID/OOD split):**\n1. **Step-level error detection**: PRMBench (ACL 2025, arXiv:2501.03124) with per-error-category breakdown (soundness/sensitivity/simplicity; redundancy, circular logic, step inconsistency, domain inconsistency, deceptive logical steps), targeting >70 overall (vs. 67.7 SOTA). ProcessBench (arXiv:2412.06559) with per-difficulty-level F1.\n2. **Downstream best-of-N reranking**: ID: MATH500, GSM8K; OOD: AIME 2024, AMC. N ∈ {8, 16, 64}. Report prm@N accuracy with ID/OOD breakdown.\n3. **Adversarial robustness**: PRM-BiasBench and perturbation suite from \"Reward Under Attack\" (arXiv:2603.06621).\n4. **RL closed-loop reward hacking**: GRPO training of Qwen2.5-Math-7B-Instruct using PGCT-PRM vs. baseline PRMs as reward. 3000-5000 steps, checkpoint every 200 steps, evaluate on MATH and AIME. Metrics: hacking gap = (PRM score improvement) − (accuracy improvement); reward-accuracy Pearson r with 95% CI from 3 seeds; late-stage divergence ratio (final 30% training).\n5. **Representation analysis**: (a) Linear probing (per \"From Chains to DAGs\" methodology, arXiv:2601.17593): compare DAG structure encoding (node depth, pairwise distance, adjacency) in PGCT-PRM vs. standard PRM hidden states, layer by layer. (b) t-SNE/UMAP visualization of step embeddings: graph-preserving pairs should cluster, graph-breaking pairs should separate. (c) Quantitative topology metric: mean cosine similarity of graph-preserving pairs vs. graph-breaking pairs.\n\n**Baselines (6 tiers):**\n1. Standard PRM: Qwen2.5-Math-PRM-7B (same base model)\n2. Robustness-focused: APRM (arXiv:2511.22888), CRA (arXiv:2508.04216)\n3. Architecture-level: CRM (ICLR 2026, arXiv:2509.26578), PURE (NeurIPS 2025, arXiv:2504.15275)\n4. Contrastive/concurrent: CPMI (arXiv:2604.10660)\n5. Error-aware: PathFinder-PRM-7B (arXiv:2505.19706)\n6. Reasoning-enhanced: R-PRM (arXiv:2503.21295), GenPRM-7B (AAAI 2026, arXiv:2504.00891), ThinkPRM-7B (arXiv:2504.16828) — all under fixed inference-compute budget for fair comparison; unrestricted comparison also reported\n- Data-matched control: ~900K total samples, contrastive pairs replaced with step-correctness annotations, standard BCE\n- Compute-matched control: equal total training FLOPs including DAG extraction overhead\n\n**Ablations (8 variants):**\n- A1: Remove InfoNCE loss → isolate contrastive learning contribution\n- A2: Remove step-correctness loss → test contrastive learning standalone\n- A3: Random perturbation replacing DAG-aware perturbation → **critical: isolate DAG structure contribution**\n- A4: Only positives (no graph-breaking negatives)\n- A5: Only negatives (no graph-preserving positives)\n- A6: Loss weighting λ ∈ {0.1, 0.3, 0.5, 0.7, 1.0}\n- A7: DAG noise injection at 5%/10%/15%/20%\n- A8: DAG extraction model scale: 7B / 32B / 72B extractors → practical viability curve\n\n## Key References\n\n- Reward Under Attack (arXiv 2026, arXiv:2603.06621)\n- Reward Models Identify Consistency, Not Causality (arXiv 2025, arXiv:2502.14619)\n- PARC/PERL (ICML 2025, arXiv:2502.02362)\n- From Chains to DAGs (arXiv 2026, arXiv:2601.17593)\n- DAG-Math (arXiv 2025, arXiv:2510.19842)\n- ProofFlow (arXiv 2025, arXiv:2510.15981)\n- CRA (arXiv 2025, arXiv:2508.04216)\n- APRM (arXiv 2025, arXiv:2511.22888)\n- CRM (ICLR 2026, arXiv:2509.26578)\n- PURE (NeurIPS 2025, arXiv:2504.15275)\n- GenPRM (AAAI 2026, arXiv:2504.00891)\n- AgentEval (arXiv 2026, arXiv:2604.23581)\n- PRMBench (ACL 2025, arXiv:2501.03124)\n- ProcessBench (arXiv 2024, arXiv:2412.06559)\n- CPMI (arXiv 2026, arXiv:2604.10660)\n- RewardFlow (arXiv 2026, arXiv:2603.18859)\n- PathFinder-PRM (arXiv 2025, arXiv:2505.19706)\n- Thought-Path Contrastive Learning (AAAI 2025, arXiv:2409.14495)\n- ThinkPRM (arXiv 2025, arXiv:2504.16828)\n- CRV (ICLR 2026, arXiv:2510.09312)\n- R-PRM (arXiv 2025, arXiv:2503.21295)\n- Factored Causal Representation Learning (ICML 2026, arXiv:2601.21350)\n- When Reward Hacking Rebounds (arXiv 2026, arXiv:2604.01476)\n\n## Resource Estimate\n\n- **manual**: gpu_hours: 1600-2200 A100-hours (DAG extraction 72B: ~350h, pair generation 7B/32B + quality verification 72B: ~300h, PRM training + 8 ablations: ~550h, baseline reproduction/evaluation: ~150h, RL closed-loop × 3 seeds: ~250h, best-of-N + adversarial + representation analysis: ~100h), timeline: 18-22 weeks for 2-3 researchers, estimated_gpu_cost: $4,800-$6,600 at $3/hr A100 spot pricing\n- **human_in_loop**: gpu_hours: 1200-1600 A100-hours (~30% reduction from automated quality triage), timeline: 13-17 weeks for 2 researchers, claude_api_cost: $800-$1,200, estimated_gpu_cost: $3,600-$4,800\n- **auto_research**: gpu_hours: 1800-2500 A100-hours (parallel sweeps), timeline: 9-12 weeks automated, claude_api_cost: $1,500-$2,000, estimated_gpu_cost: $5,400-$7,500, speed_bottleneck: DAG extraction quality validation per math subdomain requires serial human spot-checks"
}
```

---

### Runtime record

_source line 2 · 2026-05-27T08:54:32.054Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T08:54:32.054Z",
  "sessionId": "9d15703d-7612-480c-9cbd-2adbcb5cdf2b"
}
```

---

## Round 1

45 recorded events

### User

_source line 3 · 2026-05-27T08:54:32.135Z_

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
  "promptId": "92cfa655-8f2a-41b8-b21e-d398291b2706",
  "type": "user",
  "uuid": "80c3358c-9567-4b4f-be14-d2e298344b42",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9d15703d-7612-480c-9cbd-2adbcb5cdf2b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-27T08:54:32.134Z_

```json
{
  "parentUuid": "80c3358c-9567-4b4f-be14-d2e298344b42",
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
  "uuid": "c7003c78-b59a-42e6-ba55-603d5284d89b",
  "timestamp": "2026-05-27T08:54:32.134Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9d15703d-7612-480c-9cbd-2adbcb5cdf2b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-27T08:54:32.134Z_

```json
{
  "parentUuid": "c7003c78-b59a-42e6-ba55-603d5284d89b",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "b314a125-8c3a-45a9-b55b-337ac7cefa97",
  "timestamp": "2026-05-27T08:54:32.134Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9d15703d-7612-480c-9cbd-2adbcb5cdf2b",
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
  "leafUuid": "b314a125-8c3a-45a9-b55b-337ac7cefa97",
  "sessionId": "9d15703d-7612-480c-9cbd-2adbcb5cdf2b"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Premise-graph contrastive training for process reward models",
  "sessionId": "9d15703d-7612-480c-9cbd-2adbcb5cdf2b"
}
```

---

### Assistant

_source line 8 · 2026-05-27T08:54:43.571Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully read through this proposal and then conduct targeted web searches to assess its novelty, significance, and related work positioning before giving my analysis.

The proposal is about "Premise-Graph Contrastive Training (PGCT)" for training Process Reward Models (PRMs) that are aware of logical dependency structure rather than just surface consistency. The key idea is:

1. Extract premise dependency DAGs from reasoning chains
2. Construct contrastive pairs that vary logical structure while holding surface form constant (and vice versa)
3. Train PRMs with a dual objective: standard BCE + graph-contrastive InfoNCE loss


4. Now I need to search for related work in process reward modeling, contrastive learning approaches, and logical reasoning to see where this fits in the landscape.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b314a125-8c3a-45a9-b55b-337ac7cefa97",
  "isSidechain": false,
  "requestId": "req_011CbSnv2632hroV5TRms1ry",
  "type": "assistant",
  "uuid": "f1a4c4e8-d00f-4407-8e09-134101541636",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9d15703d-7612-480c-9cbd-2adbcb5cdf2b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012yAtKmQgLEZxjwzwzLn5pZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5455,
      "cache_read_input_tokens": 14184,
      "output_tokens": 249,
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
          "output_tokens": 249,
          "cache_read_input_tokens": 14184,
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

_source line 9 · 2026-05-27T08:54:43.633Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01JHS6HyvhkEydizPGSXUX3z`</summary>

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
  "parentUuid": "f1a4c4e8-d00f-4407-8e09-134101541636",
  "isSidechain": false,
  "requestId": "req_011CbSnv2632hroV5TRms1ry",
  "type": "assistant",
  "uuid": "1b16cbcc-3db4-4e68-8ae9-6782ff32e891",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9d15703d-7612-480c-9cbd-2adbcb5cdf2b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012yAtKmQgLEZxjwzwzLn5pZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5455,
      "cache_read_input_tokens": 14184,
      "output_tokens": 249,
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
          "output_tokens": 249,
          "cache_read_input_tokens": 14184,
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

_source line 10 · 2026-05-27T08:54:43.643Z_

<details><summary>↩ Tool result · `toolu_01JHS6HyvhkEydizPGSXUX3z`</summary>

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
  "parentUuid": "1b16cbcc-3db4-4e68-8ae9-6782ff32e891",
  "isSidechain": false,
  "promptId": "92cfa655-8f2a-41b8-b21e-d398291b2706",
  "type": "user",
  "uuid": "059c28e6-c352-43cc-a9e1-6bd97f598411",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "1b16cbcc-3db4-4e68-8ae9-6782ff32e891",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9d15703d-7612-480c-9cbd-2adbcb5cdf2b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-27T08:54:47.089Z_

Now let me conduct my front-loaded literature research. I'll run multiple searches in parallel to cover the key angles of this proposal.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "059c28e6-c352-43cc-a9e1-6bd97f598411",
  "isSidechain": false,
  "requestId": "req_011CbSnvsF1HE9gHHVezCeqM",
  "type": "assistant",
  "uuid": "ee776431-625e-4a18-b867-3a091166c6ec",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9d15703d-7612-480c-9cbd-2adbcb5cdf2b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HPNRQ3YMxpLjrJWTeGfV6X",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 777,
      "cache_read_input_tokens": 19639,
      "output_tokens": 236,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 777,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 236,
          "cache_read_input_tokens": 19639,
          "cache_creation_input_tokens": 777,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 777
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

_source line 12 · 2026-05-27T08:54:47.630Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GbuVyBr3X9oTZKccVFXJfS`</summary>

```json
{
  "query": "process reward model robustness logical structure 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee776431-625e-4a18-b867-3a091166c6ec",
  "isSidechain": false,
  "requestId": "req_011CbSnvsF1HE9gHHVezCeqM",
  "type": "assistant",
  "uuid": "fdedffee-3d6b-42ef-acd8-1328abdbabd0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9d15703d-7612-480c-9cbd-2adbcb5cdf2b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HPNRQ3YMxpLjrJWTeGfV6X",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 777,
      "cache_read_input_tokens": 19639,
      "output_tokens": 236,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 777,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 236,
          "cache_read_input_tokens": 19639,
          "cache_creation_input_tokens": 777,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 777
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

_source line 13 · 2026-05-27T08:54:48.052Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BbBrq2LE4BjRCZoPRcuZNf`</summary>

```json
{
  "query": "contrastive learning process reward model mathematical reasoning 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fdedffee-3d6b-42ef-acd8-1328abdbabd0",
  "isSidechain": false,
  "requestId": "req_011CbSnvsF1HE9gHHVezCeqM",
  "type": "assistant",
  "uuid": "807a5365-0f49-4320-9cb9-bca20cf68e83",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9d15703d-7612-480c-9cbd-2adbcb5cdf2b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HPNRQ3YMxpLjrJWTeGfV6X",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 777,
      "cache_read_input_tokens": 19639,
      "output_tokens": 236,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 777,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 236,
          "cache_read_input_tokens": 19639,
          "cache_creation_input_tokens": 777,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 777
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

_source line 14 · 2026-05-27T08:54:49.031Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VkAGxEHpkTFd4ToiYXcgq6`</summary>

```json
{
  "query": "premise dependency DAG reasoning verification reward model 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "807a5365-0f49-4320-9cb9-bca20cf68e83",
  "isSidechain": false,
  "requestId": "req_011CbSnvsF1HE9gHHVezCeqM",
  "type": "assistant",
  "uuid": "70e8c23e-c8b3-4d3f-878f-ba0e0c795607",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9d15703d-7612-480c-9cbd-2adbcb5cdf2b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HPNRQ3YMxpLjrJWTeGfV6X",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 777,
      "cache_read_input_tokens": 19639,
      "output_tokens": 236,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 777,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 236,
          "cache_read_input_tokens": 19639,
          "cache_creation_input_tokens": 777,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 777
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

_source line 15 · 2026-05-27T08:54:49.208Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ar8chsy3uPgQ6EMKMBytQy`</summary>

```json
{
  "query": "PGCT premise graph contrastive training PRM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70e8c23e-c8b3-4d3f-878f-ba0e0c795607",
  "isSidechain": false,
  "requestId": "req_011CbSnvsF1HE9gHHVezCeqM",
  "type": "assistant",
  "uuid": "a91f8a7f-1b19-4afa-888d-7b670319f6da",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9d15703d-7612-480c-9cbd-2adbcb5cdf2b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HPNRQ3YMxpLjrJWTeGfV6X",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 777,
      "cache_read_input_tokens": 19639,
      "output_tokens": 236,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 777,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 236,
          "cache_read_input_tokens": 19639,
          "cache_creation_input_tokens": 777,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 777
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

_source line 16 · 2026-05-27T08:54:55.335Z_

<details><summary>↩ Tool result · `toolu_01GbuVyBr3X9oTZKccVFXJfS`</summary>

```text
Web search results for query: "process reward model robustness logical structure 2025 2026"

Links: [{"title":"Process Reward Models: Step-Level Feedback for LLMs","url":"https://www.emergentmind.com/topics/process-reward-models-prm"},{"title":"Process Reward Models Meet Planning: Generating Precise and Scalable Datasets for Step-Level Rewards","url":"https://arxiv.org/html/2604.17957"},{"title":"Reward Under Attack: Evaluating the Sensitivity of Process Reward Models","url":"https://openreview.net/pdf?id=Hw24VOppus"},{"title":"Beyond Outcome Verification: Verifiable Process Reward Models for Structured Reasoning","url":"https://arxiv.org/html/2601.17223"},{"title":"Beyond Outcome Verification: Verifiable Process Reward Models for","url":"https://www.arxiv.org/pdf/2601.17223"},{"title":"A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models","url":"https://arxiv.org/html/2510.08049v3"},{"title":"Towards Robust Process Reward Modeling via Noise-aware Learning","url":"https://arxiv.org/pdf/2601.12748"}]

Based on the search results, here's what recent research (2025-2026) shows about process reward model robustness and logical structure:

## Key Developments in Robustness

Recent benchmarks like Socratic-PRMBench (May 2025) demonstrate that PRMs can exhibit reward bias, error latency, or reduced transfer to novel reasoning patterns unless explicitly trained for diverse logical structures.

Evaluating reasoning at the process level, rather than relying solely on final-answer correctness, is important to better detect and mitigate logical imperfections and improve the robustness of LLM reasoning.

## Challenges with Current Approaches

Recent research (2025) has found that PRMs often latch onto shallow consistency cues rather than learning true causal reasoning structures. Additionally, as policy models optimize against fixed automated reward models, they learn to exploit biases, such as favoring longer chains, rather than improving genuine logic, resulting in high rewards for vacuous reasoning.

## Emerging Solutions

Verifiable Process Reward Models (VPRMs) combine the robustness of reinforcement learning from verification with step-wise, rule-based verification, which enables transparent, structurally aligned reasoning and removes opportunities for reward hacking inherent in neural process rewards.

Error-aware and hierarchical labeling approaches using decoupled error detection before reward computation yield better interpretability and sample efficiency (May 2025).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fdedffee-3d6b-42ef-acd8-1328abdbabd0",
  "isSidechain": false,
  "promptId": "92cfa655-8f2a-41b8-b21e-d398291b2706",
  "type": "user",
  "uuid": "f5ebfa37-a46d-45db-8ab9-9aa0183eac7c",
  "toolUseResult": {
    "query": "process reward model robustness logical structure 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01633ega1EBsBRjpDrtVQGNS",
        "content": [
          {
            "title": "Process Reward Models: Step-Level Feedback for LLMs",
            "url": "https://www.emergentmind.com/topics/process-reward-models-prm"
          },
          {
            "title": "Process Reward Models Meet Planning: Generating Precise and Scalable Datasets for Step-Level Rewards",
            "url": "https://arxiv.org/html/2604.17957"
          },
          {
            "title": "Reward Under Attack: Evaluating the Sensitivity of Process Reward Models",
            "url": "https://openreview.net/pdf?id=Hw24VOppus"
          },
          {
            "title": "Beyond Outcome Verification: Verifiable Process Reward Models for Structured Reasoning",
            "url": "https://arxiv.org/html/2601.17223"
          },
          {
            "title": "Beyond Outcome Verification: Verifiable Process Reward Models for",
            "url": "https://www.arxiv.org/pdf/2601.17223"
          },
          {
            "title": "A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models",
            "url": "https://arxiv.org/html/2510.08049v3"
          },
          {
            "title": "Towards Robust Process Reward Modeling via Noise-aware Learning",
            "url": "https://arxiv.org/pdf/2601.12748"
          }
        ]
      },
      "Based on the search results, here's what recent research (2025-2026) shows about process reward model robustness and logical structure:\n\n## Key Developments in Robustness\n\nRecent benchmarks like Socratic-PRMBench (May 2025) demonstrate that PRMs can exhibit reward bias, error latency, or reduced transfer to novel reasoning patterns unless explicitly trained for diverse logical structures.\n\nEvaluating reasoning at the process level, rather than relying solely on final-answer correctness, is important to better detect and mitigate logical imperfections and improve the robustness of LLM reasoning.\n\n## Challenges with Current Approaches\n\nRecent research (2025) has found that PRMs often latch onto shallow consistency cues rather than learning true causal reasoning structures. Additionally, as policy models optimize against fixed automated reward models, they learn to exploit biases, such as favoring longer chains, rather than improving genuine logic, resulting in high rewards for vacuous reasoning.\n\n## Emerging Solutions\n\nVerifiable Process Reward Models (VPRMs) combine the robustness of reinforcement learning from verification with step-wise, rule-based verification, which enables transparent, structurally aligned reasoning and removes opportunities for reward hacking inherent in neural process rewards.\n\nError-aware and hierarchical labeling approaches using decoupled error detection before reward computation yield better interpretability and sample efficiency (May 2025)."
    ],
    "durationSeconds": 7.697910717999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "fdedffee-3d6b-42ef-acd8-1328abdbabd0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9d15703d-7612-480c-9cbd-2adbcb5cdf2b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-27T08:54:56.774Z_

<details><summary>↩ Tool result · `toolu_01BbBrq2LE4BjRCZoPRcuZNf`</summary>

```text
Web search results for query: "contrastive learning process reward model mathematical reasoning 2025 2026"

Links: [{"title":"Learning from Contrasts: Synthesizing Reasoning Paths from Diverse","url":"https://arxiv.org/pdf/2604.11365"},{"title":"Reasoning-Aware Proxy Reward Model using Process Mining","url":"https://arxiv.org/pdf/2510.25065"},{"title":"Coarse-to-Fine Process Reward Modeling for Mathematical Reasoning","url":"https://arxiv.org/pdf/2501.13622"},{"title":"enhancing llm reasoning with adversarial reinforce","url":"https://arxiv.org/pdf/2512.16917"},{"title":"Preprint, 2025 CAN LARGE REASONING MODELS SELF-TRAIN? Sheikh Shafayat1∗","url":"https://arxiv.org/pdf/2505.21444"},{"title":"Full-Step-DPO: Self-Supervised Preference Optimization with Step-wise   Rewards for Mathematical Reasoning","url":"https://arxiv.org/pdf/2502.14356"},{"title":"Good Learners Think Their Thinking: Generative PRM Makes Large Reasoning Model More Efficient Math Learner","url":"https://arxiv.org/pdf/2507.23317"},{"title":"arXiv:2505.02686v2 [cs.CL] 12 Jun 2025","url":"https://arxiv.org/pdf/2505.02686"}]

Based on the search results, here's what I found regarding contrastive learning, process reward models, and mathematical reasoning in 2025-2026:

## Recent Research Developments

**Process Reward Models for Mathematical Reasoning:**

An accurate process reward model (PRM) is vital for reasoning tasks, as it provides intermediate supervision signals for each individual step. Recent work has focused on improving how these models are trained. A hierarchical refinement process mitigates redundancy while preserving essential fine-grained knowledge, with extensive experiments validating effectiveness across reasoning datasets.

**Contrastive Learning in Self-Improvement:**

Contrastive learning methods like DPO and ScPO employ contrastive learning between the majority vote and non-majority vote answer, representing an approach to training reasoning models through preference learning.

**Step-wise Optimization:**

DPO's focus on coarse solution-wise preferences makes it less effective at correcting errors in multi-step reasoning, so Step-DPO was proposed, which identifies the first erroneous step and optimizes only this erroneous step along with the corresponding correct one.

**Process Rewards and Learning Efficiency:**

Well-structured process rewards can substantially accelerate large reasoning model optimization in math reasoning tasks.

These developments reflect a broader trend of using more fine-grained, intermediate-level feedback signals to improve mathematical reasoning in large language models, moving beyond simple outcome-based rewards.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "807a5365-0f49-4320-9cb9-bca20cf68e83",
  "isSidechain": false,
  "promptId": "92cfa655-8f2a-41b8-b21e-d398291b2706",
  "type": "user",
  "uuid": "202fcbb6-b4b7-4d86-bcdd-f4fcb3745a7e",
  "toolUseResult": {
    "query": "contrastive learning process reward model mathematical reasoning 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Lgxe6kxCqxa3i75a49WEs1",
        "content": [
          {
            "title": "Learning from Contrasts: Synthesizing Reasoning Paths from Diverse",
            "url": "https://arxiv.org/pdf/2604.11365"
          },
          {
            "title": "Reasoning-Aware Proxy Reward Model using Process Mining",
            "url": "https://arxiv.org/pdf/2510.25065"
          },
          {
            "title": "Coarse-to-Fine Process Reward Modeling for Mathematical Reasoning",
            "url": "https://arxiv.org/pdf/2501.13622"
          },
          {
            "title": "enhancing llm reasoning with adversarial reinforce",
            "url": "https://arxiv.org/pdf/2512.16917"
          },
          {
            "title": "Preprint, 2025 CAN LARGE REASONING MODELS SELF-TRAIN? Sheikh Shafayat1∗",
            "url": "https://arxiv.org/pdf/2505.21444"
          },
          {
            "title": "Full-Step-DPO: Self-Supervised Preference Optimization with Step-wise   Rewards for Mathematical Reasoning",
            "url": "https://arxiv.org/pdf/2502.14356"
          },
          {
            "title": "Good Learners Think Their Thinking: Generative PRM Makes Large Reasoning Model More Efficient Math Learner",
            "url": "https://arxiv.org/pdf/2507.23317"
          },
          {
            "title": "arXiv:2505.02686v2 [cs.CL] 12 Jun 2025",
            "url": "https://arxiv.org/pdf/2505.02686"
          }
        ]
      },
      "Based on the search results, here's what I found regarding contrastive learning, process reward models, and mathematical reasoning in 2025-2026:\n\n## Recent Research Developments\n\n**Process Reward Models for Mathematical Reasoning:**\n\nAn accurate process reward model (PRM) is vital for reasoning tasks, as it provides intermediate supervision signals for each individual step. Recent work has focused on improving how these models are trained. A hierarchical refinement process mitigates redundancy while preserving essential fine-grained knowledge, with extensive experiments validating effectiveness across reasoning datasets.\n\n**Contrastive Learning in Self-Improvement:**\n\nContrastive learning methods like DPO and ScPO employ contrastive learning between the majority vote and non-majority vote answer, representing an approach to training reasoning models through preference learning.\n\n**Step-wise Optimization:**\n\nDPO's focus on coarse solution-wise preferences makes it less effective at correcting errors in multi-step reasoning, so Step-DPO was proposed, which identifies the first erroneous step and optimizes only this erroneous step along with the corresponding correct one.\n\n**Process Rewards and Learning Efficiency:**\n\nWell-structured process rewards can substantially accelerate large reasoning model optimization in math reasoning tasks.\n\nThese developments reflect a broader trend of using more fine-grained, intermediate-level feedback signals to improve mathematical reasoning in large language models, moving beyond simple outcome-based rewards."
    ],
    "durationSeconds": 8.719993608000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "807a5365-0f49-4320-9cb9-bca20cf68e83",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9d15703d-7612-480c-9cbd-2adbcb5cdf2b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-27T08:54:57.177Z_

<details><summary>↩ Tool result · `toolu_01Ar8chsy3uPgQ6EMKMBytQy`</summary>

```text
Web search results for query: "PGCT premise graph contrastive training PRM"

Links: [{"title":"Prototypical Graph Contrastive Learning","url":"https://arxiv.org/pdf/2106.09645"},{"title":"Provable Training for Graph Contrastive Learning","url":"https://arxiv.org/pdf/2309.13944"},{"title":"Information-aware graph contrastive learning","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12518162"},{"title":"Information-aware graph contrastive learning","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12488238"},{"title":"Information-aware graph contrastive learning","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12511540"},{"title":"Information-aware graph contrastive learning","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12518163"},{"title":"Supervised Graph Contrastive Pretraining for Text Classification","url":"https://arxiv.org/pdf/2112.11389"}]

Based on the search results, I found information related to graph contrastive learning, though the specific combination "PGCT premise graph contrastive training PRM" didn't return an exact match. Here's what I found:

The search results contain several approaches to graph contrastive learning:

1. **Prototypical Graph Contrastive Learning (PGCL)**: PGCL models the underlying semantic structure of the graph data via clustering semantically similar graphs into the same group, and simultaneously encourages the clustering consistency for different augmentations of the same graph.

2. **Provable Training for Graph Contrastive Learning**: Graph Contrastive Learning (GCL) has emerged as a popular training approach for learning node embeddings from augmented graphs without labels.

3. **Information-aware Graph Contrastive Learning**: This framework focuses on generating semantically similar views of graphs while preserving structural and attribute information.

4. **Graph Contrastive Pre-training for Text (GCPT)**: This approach extrapolates label information on examples to tokens as their conditional probability and uses this label information in a supervised contrastive learning formulation to learn a token embedding space.

If you're looking for more specific information about "PGCT" with "PRM" (which might refer to Process Reward Models or similar), you may want to provide additional context or refine the search query, as the results primarily cover graph contrastive learning methods rather than the specific combination you're searching for.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a91f8a7f-1b19-4afa-888d-7b670319f6da",
  "isSidechain": false,
  "promptId": "92cfa655-8f2a-41b8-b21e-d398291b2706",
  "type": "user",
  "uuid": "2adaf13c-532e-45fd-a1c6-c27f40ce8be2",
  "toolUseResult": {
    "query": "PGCT premise graph contrastive training PRM",
    "results": [
      {
        "tool_use_id": "srvtoolu_011EqQzuekd1EEQWURoEjniu",
        "content": [
          {
            "title": "Prototypical Graph Contrastive Learning",
            "url": "https://arxiv.org/pdf/2106.09645"
          },
          {
            "title": "Provable Training for Graph Contrastive Learning",
            "url": "https://arxiv.org/pdf/2309.13944"
          },
          {
            "title": "Information-aware graph contrastive learning",
            "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12518162"
          },
          {
            "title": "Information-aware graph contrastive learning",
            "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12488238"
          },
          {
            "title": "Information-aware graph contrastive learning",
            "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12511540"
          },
          {
            "title": "Information-aware graph contrastive learning",
            "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12518163"
          },
          {
            "title": "Supervised Graph Contrastive Pretraining for Text Classification",
            "url": "https://arxiv.org/pdf/2112.11389"
          }
        ]
      },
      "Based on the search results, I found information related to graph contrastive learning, though the specific combination \"PGCT premise graph contrastive training PRM\" didn't return an exact match. Here's what I found:\n\nThe search results contain several approaches to graph contrastive learning:\n\n1. **Prototypical Graph Contrastive Learning (PGCL)**: PGCL models the underlying semantic structure of the graph data via clustering semantically similar graphs into the same group, and simultaneously encourages the clustering consistency for different augmentations of the same graph.\n\n2. **Provable Training for Graph Contrastive Learning**: Graph Contrastive Learning (GCL) has emerged as a popular training approach for learning node embeddings from augmented graphs without labels.\n\n3. **Information-aware Graph Contrastive Learning**: This framework focuses on generating semantically similar views of graphs while preserving structural and attribute information.\n\n4. **Graph Contrastive Pre-training for Text (GCPT)**: This approach extrapolates label information on examples to tokens as their conditional probability and uses this label information in a supervised contrastive learning formulation to learn a token embedding space.\n\nIf you're looking for more specific information about \"PGCT\" with \"PRM\" (which might refer to Process Reward Models or similar), you may want to provide additional context or refine the search query, as the results primarily cover graph contrastive learning methods rather than the specific combination you're searching for."
    ],
    "durationSeconds": 7.964829697000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "a91f8a7f-1b19-4afa-888d-7b670319f6da",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9d15703d-7612-480c-9cbd-2adbcb5cdf2b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-27T08:54:58.124Z_

<details><summary>↩ Tool result · `toolu_01VkAGxEHpkTFd4ToiYXcgq6`</summary>

```text
Web search results for query: "premise dependency DAG reasoning verification reward model 2025 2026"

Links: [{"title":"Grounding the Score: Explicit Visual Premise Verification for Reliable Vision-Language Process Reward Models","url":"https://arxiv.org/pdf/2603.16253"},{"title":"DAG-Math: Graph-Guided Mathematical Reasoning in LLMs","url":"https://arxiv.org/html/2510.19842v1"},{"title":"A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models","url":"https://arxiv.org/html/2510.08049v3"},{"title":"PRISM: Pushing the Frontier of Deep Think via Process Reward Model-Guided Inference","url":"https://arxiv.org/html/2603.02479"},{"title":"Rewarding the Scientific Process: Process-Level Reward Modeling for Agentic Data Analysis","url":"https://arxiv.org/html/2604.24198v1"},{"title":"Uncertainty-Aware Step-wise Verification with Generative Reward Models","url":"https://arxiv.org/pdf/2502.11250"}]

I found several relevant recent papers on premise dependency, DAG reasoning, verification, and reward models. Here's what the search results show:

## Key Recent Works (2025-2026):

**DAG-Based Reasoning:**
A recent work formalizes Chain-of-Thought as a rule-based stochastic process on directed acyclic graphs (DAGs), addressing limitations in evaluating LLM mathematical reasoning. This approach involves identifying all required premises (such as facts and constraints) and conducting correct logical inference.

**Premise-Aware Verification:**
EVPV (Explicit Visual Premise Verification) is a premise-aware process reward modeling approach for reliable multimodal reasoning. Current vision-language PRMs still function as "black-box judges" where low scores are hard to interpret—did the step fail logically, or did the verifier itself misperceive the image?

**Automated Verification Methods:**
FOVER uses formal verification tools (such as Z3 and Isabelle) to automatically generate PRM training data with accurate step-level error labels. URSA synthesizes process-level supervision for multimodal mathematical reasoning through a fully automated dual-view pipeline.

**Process Reward Models:**
By providing step-level supervision and fine-grained verification during both training and inference time, PRMs can significantly boost models' reasoning reliability and performance.

**Uncertainty in Verification:**
Recent work argues that uncertainty quantification offers a principled way to improve the reliability of generative reward models by detecting when the verifier itself is uncertain at a given step.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "70e8c23e-c8b3-4d3f-878f-ba0e0c795607",
  "isSidechain": false,
  "promptId": "92cfa655-8f2a-41b8-b21e-d398291b2706",
  "type": "user",
  "uuid": "a32ee483-afed-4bf5-a85b-f15709f5688b",
  "toolUseResult": {
    "query": "premise dependency DAG reasoning verification reward model 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_015tN2JE4oRt8rjtuBmWAwLA",
        "content": [
          {
            "title": "Grounding the Score: Explicit Visual Premise Verification for Reliable Vision-Language Process Reward Models",
            "url": "https://arxiv.org/pdf/2603.16253"
          },
          {
            "title": "DAG-Math: Graph-Guided Mathematical Reasoning in LLMs",
            "url": "https://arxiv.org/html/2510.19842v1"
          },
          {
            "title": "A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models",
            "url": "https://arxiv.org/html/2510.08049v3"
          },
          {
            "title": "PRISM: Pushing the Frontier of Deep Think via Process Reward Model-Guided Inference",
            "url": "https://arxiv.org/html/2603.02479"
          },
          {
            "title": "Rewarding the Scientific Process: Process-Level Reward Modeling for Agentic Data Analysis",
            "url": "https://arxiv.org/html/2604.24198v1"
          },
          {
            "title": "Uncertainty-Aware Step-wise Verification with Generative Reward Models",
            "url": "https://arxiv.org/pdf/2502.11250"
          }
        ]
      },
      "I found several relevant recent papers on premise dependency, DAG reasoning, verification, and reward models. Here's what the search results show:\n\n## Key Recent Works (2025-2026):\n\n**DAG-Based Reasoning:**\nA recent work formalizes Chain-of-Thought as a rule-based stochastic process on directed acyclic graphs (DAGs), addressing limitations in evaluating LLM mathematical reasoning. This approach involves identifying all required premises (such as facts and constraints) and conducting correct logical inference.\n\n**Premise-Aware Verification:**\nEVPV (Explicit Visual Premise Verification) is a premise-aware process reward modeling approach for reliable multimodal reasoning. Current vision-language PRMs still function as \"black-box judges\" where low scores are hard to interpret—did the step fail logically, or did the verifier itself misperceive the image?\n\n**Automated Verification Methods:**\nFOVER uses formal verification tools (such as Z3 and Isabelle) to automatically generate PRM training data with accurate step-level error labels. URSA synthesizes process-level supervision for multimodal mathematical reasoning through a fully automated dual-view pipeline.\n\n**Process Reward Models:**\nBy providing step-level supervision and fine-grained verification during both training and inference time, PRMs can significantly boost models' reasoning reliability and performance.\n\n**Uncertainty in Verification:**\nRecent work argues that uncertainty quantification offers a principled way to improve the reliability of generative reward models by detecting when the verifier itself is uncertain at a given step."
    ],
    "durationSeconds": 9.090552002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "70e8c23e-c8b3-4d3f-878f-ba0e0c795607",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9d15703d-7612-480c-9cbd-2adbcb5cdf2b",
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
  "lastPrompt": "# Premise-Graph Contrastive Training for Logic-Grounded Process Reward Models  ## Core Problem  Current process reward models detect consistency rather than causality. \"Reward Models Identify Consiste…",
  "leafUuid": "a32ee483-afed-4bf5-a85b-f15709f5688b",
  "sessionId": "9d15703d-7612-480c-9cbd-2adbcb5cdf2b"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Premise-graph contrastive training for process reward models",
  "sessionId": "9d15703d-7612-480c-9cbd-2adbcb5cdf2b"
}
```

---

### Tool call

_source line 22 · 2026-05-27T08:55:01.004Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QKnC6QK6YsUrRBXdcRY9Ft`</summary>

```json
{
  "query": "reward hacking process reward model representation learning causal structure 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a32ee483-afed-4bf5-a85b-f15709f5688b",
  "isSidechain": false,
  "requestId": "req_011CbSnww9gKL4us49CG5EGr",
  "type": "assistant",
  "uuid": "fa21140d-a03d-4150-beea-21d44f1a3f10",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9d15703d-7612-480c-9cbd-2adbcb5cdf2b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ah4zZdcv7mvWVYFS3tLbrK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 664,
      "cache_creation_input_tokens": 2293,
      "cache_read_input_tokens": 20416,
      "output_tokens": 176,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2293,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 664,
          "output_tokens": 176,
          "cache_read_input_tokens": 20416,
          "cache_creation_input_tokens": 2293,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2293
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

_source line 23 · 2026-05-27T08:55:02.064Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Hq5FxZK7yXWKMd2KNXV9dg`</summary>

```json
{
  "query": "\"From Chains to DAGs\" LLM hidden states DAG structure linear probing 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa21140d-a03d-4150-beea-21d44f1a3f10",
  "isSidechain": false,
  "requestId": "req_011CbSnww9gKL4us49CG5EGr",
  "type": "assistant",
  "uuid": "bc0037b8-2a03-4d90-ad15-65abf0554488",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9d15703d-7612-480c-9cbd-2adbcb5cdf2b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ah4zZdcv7mvWVYFS3tLbrK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 664,
      "cache_creation_input_tokens": 2293,
      "cache_read_input_tokens": 20416,
      "output_tokens": 176,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2293,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 664,
          "output_tokens": 176,
          "cache_read_input_tokens": 20416,
          "cache_creation_input_tokens": 2293,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2293
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

_source line 24 · 2026-05-27T08:55:02.691Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015AFqri2xo4BkE6HCio1gk2`</summary>

```json
{
  "query": "CPMI contrastive mutual information PRM auto-labeling 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc0037b8-2a03-4d90-ad15-65abf0554488",
  "isSidechain": false,
  "requestId": "req_011CbSnww9gKL4us49CG5EGr",
  "type": "assistant",
  "uuid": "e4fe0e55-8868-40ea-b5ef-dbbe71ac6d14",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9d15703d-7612-480c-9cbd-2adbcb5cdf2b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ah4zZdcv7mvWVYFS3tLbrK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 664,
      "cache_creation_input_tokens": 2293,
      "cache_read_input_tokens": 20416,
      "output_tokens": 176,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2293,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 664,
          "output_tokens": 176,
          "cache_read_input_tokens": 20416,
          "cache_creation_input_tokens": 2293,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2293
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

_source line 25 · 2026-05-27T08:55:07.085Z_

<details><summary>↩ Tool result · `toolu_01Hq5FxZK7yXWKMd2KNXV9dg`</summary>

```text
Web search results for query: ""From Chains to DAGs" LLM hidden states DAG structure linear probing 2026"

Links: [{"title":"[2601.17593] From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs","url":"https://arxiv.org/abs/2601.17593"},{"title":"From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs","url":"https://arxiv.org/pdf/2601.17593"},{"title":"From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs","url":"https://arxiv.org/html/2601.17593"},{"title":"From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs - ADS","url":"https://ui.adsabs.harvard.edu/abs/2026arXiv260117593Z/abstract"},{"title":"Probing LLM Hidden States","url":"https://apxml.com/courses/how-to-build-a-large-language-model/chapter-23-analyzing-model-behavior/probing-internal-representations"}]

Based on the search results, I found the paper you're looking for:

"From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs" introduces Reasoning DAG Probing, a framework for testing whether LLM hidden states linearly encode properties of an underlying reasoning DAG and where this structure emerges across layers.

**Key Details:**

- The paper addresses how many reasoning problems are more naturally modeled as directed acyclic graphs (DAGs), where intermediate conclusions branch, merge, and are reused, rather than linear chains.

- The researchers associate each reasoning node with a textual realization and train lightweight probes to predict node depth, pairwise distance, and adjacency from hidden states.

- Across reasoning benchmarks, the findings show that DAG structure is meaningfully encoded in LLM representations, with recoverability peaking in intermediate layers, varying systematically by node depth, edge span, and model scale.

The paper (arxiv 2601.17593) was published in early April 2026 by researchers from Columbia University.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bc0037b8-2a03-4d90-ad15-65abf0554488",
  "isSidechain": false,
  "promptId": "92cfa655-8f2a-41b8-b21e-d398291b2706",
  "type": "user",
  "uuid": "974da46d-01c6-4ac6-998f-a6e9b65fc143",
  "toolUseResult": {
    "query": "\"From Chains to DAGs\" LLM hidden states DAG structure linear probing 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01V9Bv8pnfqKesZsbrLSVNkn",
        "content": [
          {
            "title": "[2601.17593] From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs",
            "url": "https://arxiv.org/abs/2601.17593"
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
            "title": "From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2026arXiv260117593Z/abstract"
          },
          {
            "title": "Probing LLM Hidden States",
            "url": "https://apxml.com/courses/how-to-build-a-large-language-model/chapter-23-analyzing-model-behavior/probing-internal-representations"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n\"From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs\" introduces Reasoning DAG Probing, a framework for testing whether LLM hidden states linearly encode properties of an underlying reasoning DAG and where this structure emerges across layers.\n\n**Key Details:**\n\n- The paper addresses how many reasoning problems are more naturally modeled as directed acyclic graphs (DAGs), where intermediate conclusions branch, merge, and are reused, rather than linear chains.\n\n- The researchers associate each reasoning node with a textual realization and train lightweight probes to predict node depth, pairwise distance, and adjacency from hidden states.\n\n- Across reasoning benchmarks, the findings show that DAG structure is meaningfully encoded in LLM representations, with recoverability peaking in intermediate layers, varying systematically by node depth, edge span, and model scale.\n\nThe paper (arxiv 2601.17593) was published in early April 2026 by researchers from Columbia University."
    ],
    "durationSeconds": 5.015586951999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "bc0037b8-2a03-4d90-ad15-65abf0554488",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9d15703d-7612-480c-9cbd-2adbcb5cdf2b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-27T08:55:08.822Z_

<details><summary>↩ Tool result · `toolu_01QKnC6QK6YsUrRBXdcRY9Ft`</summary>

```text
Web search results for query: "reward hacking process reward model representation learning causal structure 2026"

Links: [{"title":"Factored Causal Representation Learning for Robust Reward Modeling in RLHF","url":"https://www.arxiv.org/pdf/2601.21350"},{"title":"GitHub - xhwang22/Awesome-Reward-Hacking: A curated list of papers and resources on Reward Hacking, Emergent Misalignment, and Proxy Exploitation in Large Models · GitHub","url":"https://github.com/xhwang22/Awesome-Reward-Hacking"},{"title":"[2602.10623] Mitigating Reward Hacking in RLHF via Bayesian Non-negative Reward Modeling","url":"https://arxiv.org/abs/2602.10623"},{"title":"[2602.10623v1] Mitigating Reward Hacking in RLHF via Bayesian Non-negative Reward Modeling","url":"https://arxiv.org/abs/2602.10623v1"},{"title":"Reward Hacking in Reinforcement Learning | Lil'Log","url":"https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"},{"title":"Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction","url":"https://arxiv.org/html/2508.04216v1"},{"title":"When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals","url":"https://arxiv.org/pdf/2604.01476"},{"title":"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges","url":"https://arxiv.org/html/2604.13602v1"},{"title":"Mitigating Reward Hacking in RLHF via Bayesian Non-negative Reward Modeling","url":"https://arxiv.org/pdf/2602.10623"}]

I found several highly relevant 2026 papers on this topic. Here are the key findings:

## Reward Hacking and Mitigation Approaches in 2026

Reward hacking is a structural vulnerability where models exploit imperfections in learned reward signals to maximize a proxy objective while bypassing true task intent.

### Causal Representation Learning Approaches

Recent work uses factored causal representation learning to separate causal latents and non-causal latents in reward models, restricting reward prediction to depend only on causal factors while discouraging non-causal factors from encoding reward-predictive information. The CausalRM framework explicitly diagnoses and isolates spurious features during training by partitioning the reward model's latent space into causal factors (which align with true human preference) and non-causal factors (which capture confounders like verbosity).

### Bayesian Non-Negative Reward Modeling

Another approach represents rewards through a sparse, non-negative latent factor generative process that uses instance-specific latent variables to induce disentangled reward representations, while sparsity over global latent factors acts as an implicit debiasing mechanism that suppresses spurious correlations. This method substantially mitigates reward over-optimization, improves robustness under distribution shifts, and yields more interpretable reward decompositions than strong baselines.

### Broader Framework

The field is being organized along an escalating hierarchy of exploitation mechanisms: Feature-level → Representation-level → Evaluator-level → Environment-level.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fa21140d-a03d-4150-beea-21d44f1a3f10",
  "isSidechain": false,
  "promptId": "92cfa655-8f2a-41b8-b21e-d398291b2706",
  "type": "user",
  "uuid": "8806ddad-eb0f-4de4-9dec-73d5a223a40f",
  "toolUseResult": {
    "query": "reward hacking process reward model representation learning causal structure 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_018af2pzN1C86aLhgienTrpp",
        "content": [
          {
            "title": "Factored Causal Representation Learning for Robust Reward Modeling in RLHF",
            "url": "https://www.arxiv.org/pdf/2601.21350"
          },
          {
            "title": "GitHub - xhwang22/Awesome-Reward-Hacking: A curated list of papers and resources on Reward Hacking, Emergent Misalignment, and Proxy Exploitation in Large Models · GitHub",
            "url": "https://github.com/xhwang22/Awesome-Reward-Hacking"
          },
          {
            "title": "[2602.10623] Mitigating Reward Hacking in RLHF via Bayesian Non-negative Reward Modeling",
            "url": "https://arxiv.org/abs/2602.10623"
          },
          {
            "title": "[2602.10623v1] Mitigating Reward Hacking in RLHF via Bayesian Non-negative Reward Modeling",
            "url": "https://arxiv.org/abs/2602.10623v1"
          },
          {
            "title": "Reward Hacking in Reinforcement Learning | Lil'Log",
            "url": "https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"
          },
          {
            "title": "Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction",
            "url": "https://arxiv.org/html/2508.04216v1"
          },
          {
            "title": "When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals",
            "url": "https://arxiv.org/pdf/2604.01476"
          },
          {
            "title": "Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges",
            "url": "https://arxiv.org/html/2604.13602v1"
          },
          {
            "title": "Mitigating Reward Hacking in RLHF via Bayesian Non-negative Reward Modeling",
            "url": "https://arxiv.org/pdf/2602.10623"
          }
        ]
      },
      "I found several highly relevant 2026 papers on this topic. Here are the key findings:\n\n## Reward Hacking and Mitigation Approaches in 2026\n\nReward hacking is a structural vulnerability where models exploit imperfections in learned reward signals to maximize a proxy objective while bypassing true task intent.\n\n### Causal Representation Learning Approaches\n\nRecent work uses factored causal representation learning to separate causal latents and non-causal latents in reward models, restricting reward prediction to depend only on causal factors while discouraging non-causal factors from encoding reward-predictive information. The CausalRM framework explicitly diagnoses and isolates spurious features during training by partitioning the reward model's latent space into causal factors (which align with true human preference) and non-causal factors (which capture confounders like verbosity).\n\n### Bayesian Non-Negative Reward Modeling\n\nAnother approach represents rewards through a sparse, non-negative latent factor generative process that uses instance-specific latent variables to induce disentangled reward representations, while sparsity over global latent factors acts as an implicit debiasing mechanism that suppresses spurious correlations. This method substantially mitigates reward over-optimization, improves robustness under distribution shifts, and yields more interpretable reward decompositions than strong baselines.\n\n### Broader Framework\n\nThe field is being organized along an escalating hierarchy of exploitation mechanisms: Feature-level → Representation-level → Evaluator-level → Environment-level."
    ],
    "durationSeconds": 7.8123699009999985,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "fa21140d-a03d-4150-beea-21d44f1a3f10",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9d15703d-7612-480c-9cbd-2adbcb5cdf2b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-27T08:55:09.020Z_

<details><summary>↩ Tool result · `toolu_015AFqri2xo4BkE6HCio1gk2`</summary>

```text
Web search results for query: "CPMI contrastive mutual information PRM auto-labeling 2026 arXiv"

Links: [{"title":"[2604.10660] Efficient Process Reward Modeling via Contrastive Mutual Information","url":"https://arxiv.org/abs/2604.10660"},{"title":"Efficient Process Reward Modeling via Contrastive Mutual Information","url":"https://arxiv.org/html/2604.10660"},{"title":"Pointwise Mutual Information (PMI)","url":"https://www.emergentmind.com/topics/pointwise-mutual-information-pmi"},{"title":"Decomposed Mutual Information Estimation for Contrastive Representation   Learning","url":"https://arxiv.org/pdf/2106.13401"},{"title":"Contrastive Mutual Information Learning: Toward Robust Representations without Positive-Pair Augmentations","url":"https://arxiv.org/pdf/2509.21511"},{"title":"Contrastive Mutual Information Learning: Toward Robust Representations without Positive-Pair Augmentations","url":"https://arxiv.org/html/2509.21511"}]

Based on the search results, I found the paper you're looking for:

The paper "Efficient Process Reward Modeling via Contrastive Mutual Information" was submitted on April 12, 2026, with authors Nakyung Lee, Sangwoo Hong, and Jungwoo Lee.

The paper proposes contrastive pointwise mutual information (CPMI), a novel automatic reward labeling method that leverages the model's internal probability to infer step-level supervision while significantly reducing computational burden. CPMI quantifies how much a reasoning step increases the mutual information between the step and the correct target answer relative to hard-negative alternatives.

The work addresses the limitation that training a PRM typically requires human annotators to assign reward scores to each reasoning step, which is both costly and time-consuming, while existing automated approaches like Monte Carlo estimation demand substantial computational resources due to repeated LLM rollouts.

The arXiv paper ID is 2604.10660, and you can access it at https://arxiv.org/abs/2604.10660.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e4fe0e55-8868-40ea-b5ef-dbbe71ac6d14",
  "isSidechain": false,
  "promptId": "92cfa655-8f2a-41b8-b21e-d398291b2706",
  "type": "user",
  "uuid": "15531a5a-caca-4bee-a3fd-35f99a915bf6",
  "toolUseResult": {
    "query": "CPMI contrastive mutual information PRM auto-labeling 2026 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Rs7xcdpMzU6CvWVgqCm84R",
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
            "title": "Pointwise Mutual Information (PMI)",
            "url": "https://www.emergentmind.com/topics/pointwise-mutual-information-pmi"
          },
          {
            "title": "Decomposed Mutual Information Estimation for Contrastive Representation   Learning",
            "url": "https://arxiv.org/pdf/2106.13401"
          },
          {
            "title": "Contrastive Mutual Information Learning: Toward Robust Representations without Positive-Pair Augmentations",
            "url": "https://arxiv.org/pdf/2509.21511"
          },
          {
            "title": "Contrastive Mutual Information Learning: Toward Robust Representations without Positive-Pair Augmentations",
            "url": "https://arxiv.org/html/2509.21511"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\nThe paper \"Efficient Process Reward Modeling via Contrastive Mutual Information\" was submitted on April 12, 2026, with authors Nakyung Lee, Sangwoo Hong, and Jungwoo Lee.\n\nThe paper proposes contrastive pointwise mutual information (CPMI), a novel automatic reward labeling method that leverages the model's internal probability to infer step-level supervision while significantly reducing computational burden. CPMI quantifies how much a reasoning step increases the mutual information between the step and the correct target answer relative to hard-negative alternatives.\n\nThe work addresses the limitation that training a PRM typically requires human annotators to assign reward scores to each reasoning step, which is both costly and time-consuming, while existing automated approaches like Monte Carlo estimation demand substantial computational resources due to repeated LLM rollouts.\n\nThe arXiv paper ID is 2604.10660, and you can access it at https://arxiv.org/abs/2604.10660."
    ],
    "durationSeconds": 6.326373930000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e4fe0e55-8868-40ea-b5ef-dbbe71ac6d14",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9d15703d-7612-480c-9cbd-2adbcb5cdf2b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-27T08:55:18.209Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BFwqRfz7qFBppiYTFzBLfV`</summary>

```json
{
  "query": "RewardFlow graph reward propagation reasoning 2026 arXiv:2603.18859"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15531a5a-caca-4bee-a3fd-35f99a915bf6",
  "isSidechain": false,
  "requestId": "req_011CbSnxjjcjg4KMkTLgLoaF",
  "type": "assistant",
  "uuid": "627d9263-4470-4b78-a5ca-8b902ac22474",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9d15703d-7612-480c-9cbd-2adbcb5cdf2b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MQL7poDcNcpvdoW8CUU7xy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2849,
      "cache_read_input_tokens": 22709,
      "output_tokens": 177,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2849,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 177,
          "cache_read_input_tokens": 22709,
          "cache_creation_input_tokens": 2849,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2849
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

_source line 29 · 2026-05-27T08:55:18.698Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LnUNLhDUJxz7S5ZBDDpegd`</summary>

```json
{
  "query": "CRV attribution graph reasoning verification ICLR 2026 arXiv:2510.09312"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "627d9263-4470-4b78-a5ca-8b902ac22474",
  "isSidechain": false,
  "requestId": "req_011CbSnxjjcjg4KMkTLgLoaF",
  "type": "assistant",
  "uuid": "2eabff5c-7a9e-46ad-9bd0-2b6131c6a0a1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9d15703d-7612-480c-9cbd-2adbcb5cdf2b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MQL7poDcNcpvdoW8CUU7xy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2849,
      "cache_read_input_tokens": 22709,
      "output_tokens": 177,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2849,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 177,
          "cache_read_input_tokens": 22709,
          "cache_creation_input_tokens": 2849,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2849
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

_source line 30 · 2026-05-27T08:55:19.384Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01A8sgxceDUvCJHVFM4gDXwu`</summary>

```json
{
  "query": "verifiable process reward model reasoning structure-aware training 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2eabff5c-7a9e-46ad-9bd0-2b6131c6a0a1",
  "isSidechain": false,
  "requestId": "req_011CbSnxjjcjg4KMkTLgLoaF",
  "type": "assistant",
  "uuid": "85b6e261-5829-430a-86e7-7c1f66d73afb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9d15703d-7612-480c-9cbd-2adbcb5cdf2b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MQL7poDcNcpvdoW8CUU7xy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2849,
      "cache_read_input_tokens": 22709,
      "output_tokens": 177,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2849,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 177,
          "cache_read_input_tokens": 22709,
          "cache_creation_input_tokens": 2849,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2849
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

_source line 31 · 2026-05-27T08:55:26.098Z_

<details><summary>↩ Tool result · `toolu_01LnUNLhDUJxz7S5ZBDDpegd`</summary>

```text
Web search results for query: "CRV attribution graph reasoning verification ICLR 2026 arXiv:2510.09312"

Links: [{"title":"[2510.09312] Verifying Chain-of-Thought Reasoning via Its Computational Graph","url":"https://arxiv.org/abs/2510.09312"},{"title":"Verifying Chain-of-Thought Reasoning via Its Computational Graph","url":"https://arxiv.org/html/2510.09312v1"},{"title":"Verifying Chain-of-Thought Reasoning via Its Computational Graph","url":"https://arxiv.org/pdf/2510.09312"},{"title":"Verifying Chain-of-Thought Reasoning via Its Computational Graph |…","url":"https://www.opentrain.ai/papers/verifying-chain-of-thought-reasoning-via-its-computational-graph--arxiv-2510.09312/"},{"title":"Meta's \"X-ray\" AI Thought Chain: 92% Accuracy in CRV Reasoning Diagnosis","url":"https://eu.36kr.com/en/p/3521511653170052"},{"title":"facebook/crv · Datasets at Hugging Face","url":"https://huggingface.co/datasets/facebook/crv"},{"title":"Machine Learning Oct 2025","url":"https://arxiv.org/list/cs.LG/2025-10?skip=3650&show=250"},{"title":"Verifying Chain-of-Thought Reasoning via Its Computational Graph | Request PDF","url":"https://www.researchgate.net/publication/396459021_Verifying_Chain-of-Thought_Reasoning_via_Its_Computational_Graph"},{"title":"GraphReason: Enhancing Reasoning Capabilities of Large Language Models   through A Graph-Based Verification Approach","url":"https://arxiv.org/pdf/2308.09267"}]

Based on the search results, here's what I found about the CRV attribution graph reasoning verification paper:

## Overview

Circuit-based Reasoning Verification (CRV) is a white-box method that addresses limitations of current Chain-of-Thought (CoT) verification methods, which predict reasoning correctness based on outputs (black-box) or activations (gray-box), but offer limited insight into why a computation fails.

## Core Approach

The method is based on the hypothesis that attribution graphs of correct CoT steps, viewed as execution traces of the model's latent reasoning circuits, possess distinct structural fingerprints from those of incorrect steps. By training a classifier on structural features of these graphs, the traces contain a powerful signal of reasoning errors.

The approach constructs an attribution graph—a structural representation of the causal information flow between model components. To make the graph interpretable, the researchers create a surrogate model by replacing standard MLP modules with trained transcoders, then construct and analyze attribution graphs over the sparsely activating features of such surrogate model.

## Publication Status

The paper "Verifying Chain-of-Thought Reasoning via Its Computational Graph" has been accepted to ICLR 2026 as an Oral presentation. The paper is authored by Zheng Zhao, Yeskendir Koishekenov, Xianjun Yang, Naila Murray, and Nicola Cancedda.

## Results

The method achieved 98.4% accuracy on synthetic Boolean problems, 98.8% on synthetic arithmetic problems, and 93.4% on GSM8K.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2eabff5c-7a9e-46ad-9bd0-2b6131c6a0a1",
  "isSidechain": false,
  "promptId": "92cfa655-8f2a-41b8-b21e-d398291b2706",
  "type": "user",
  "uuid": "1bd238a8-fa9d-4470-ad3d-2948b2197390",
  "toolUseResult": {
    "query": "CRV attribution graph reasoning verification ICLR 2026 arXiv:2510.09312",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JKY8yQn7JaX4pfvsyf97xP",
        "content": [
          {
            "title": "[2510.09312] Verifying Chain-of-Thought Reasoning via Its Computational Graph",
            "url": "https://arxiv.org/abs/2510.09312"
          },
          {
            "title": "Verifying Chain-of-Thought Reasoning via Its Computational Graph",
            "url": "https://arxiv.org/html/2510.09312v1"
          },
          {
            "title": "Verifying Chain-of-Thought Reasoning via Its Computational Graph",
            "url": "https://arxiv.org/pdf/2510.09312"
          },
          {
            "title": "Verifying Chain-of-Thought Reasoning via Its Computational Graph |…",
            "url": "https://www.opentrain.ai/papers/verifying-chain-of-thought-reasoning-via-its-computational-graph--arxiv-2510.09312/"
          },
          {
            "title": "Meta's \"X-ray\" AI Thought Chain: 92% Accuracy in CRV Reasoning Diagnosis",
            "url": "https://eu.36kr.com/en/p/3521511653170052"
          },
          {
            "title": "facebook/crv · Datasets at Hugging Face",
            "url": "https://huggingface.co/datasets/facebook/crv"
          },
          {
            "title": "Machine Learning Oct 2025",
            "url": "https://arxiv.org/list/cs.LG/2025-10?skip=3650&show=250"
          },
          {
            "title": "Verifying Chain-of-Thought Reasoning via Its Computational Graph | Request PDF",
            "url": "https://www.researchgate.net/publication/396459021_Verifying_Chain-of-Thought_Reasoning_via_Its_Computational_Graph"
          },
          {
            "title": "GraphReason: Enhancing Reasoning Capabilities of Large Language Models   through A Graph-Based Verification Approach",
            "url": "https://arxiv.org/pdf/2308.09267"
          }
        ]
      },
      "Based on the search results, here's what I found about the CRV attribution graph reasoning verification paper:\n\n## Overview\n\nCircuit-based Reasoning Verification (CRV) is a white-box method that addresses limitations of current Chain-of-Thought (CoT) verification methods, which predict reasoning correctness based on outputs (black-box) or activations (gray-box), but offer limited insight into why a computation fails.\n\n## Core Approach\n\nThe method is based on the hypothesis that attribution graphs of correct CoT steps, viewed as execution traces of the model's latent reasoning circuits, possess distinct structural fingerprints from those of incorrect steps. By training a classifier on structural features of these graphs, the traces contain a powerful signal of reasoning errors.\n\nThe approach constructs an attribution graph—a structural representation of the causal information flow between model components. To make the graph interpretable, the researchers create a surrogate model by replacing standard MLP modules with trained transcoders, then construct and analyze attribution graphs over the sparsely activating features of such surrogate model.\n\n## Publication Status\n\nThe paper \"Verifying Chain-of-Thought Reasoning via Its Computational Graph\" has been accepted to ICLR 2026 as an Oral presentation. The paper is authored by Zheng Zhao, Yeskendir Koishekenov, Xianjun Yang, Naila Murray, and Nicola Cancedda.\n\n## Results\n\nThe method achieved 98.4% accuracy on synthetic Boolean problems, 98.8% on synthetic arithmetic problems, and 93.4% on GSM8K."
    ],
    "durationSeconds": 7.395888746999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "2eabff5c-7a9e-46ad-9bd0-2b6131c6a0a1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9d15703d-7612-480c-9cbd-2adbcb5cdf2b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-27T08:55:26.862Z_

<details><summary>↩ Tool result · `toolu_01BFwqRfz7qFBppiYTFzBLfV`</summary>

```text
Web search results for query: "RewardFlow graph reward propagation reasoning 2026 arXiv:2603.18859"

Links: [{"title":"RewardFlow: Topology-Aware Reward Propagation on State Graphs for Agentic RL with Large Language Models","url":"https://arxiv.org/html/2603.18859"},{"title":"[2603.18859] RewardFlow: Topology-Aware Reward Propagation on State Graphs for Agentic RL with Large Language Models","url":"https://arxiv.org/abs/2603.18859"},{"title":"RewardFlow: Topology-Aware Reward Propagation on State Graphs for Agentic RL with Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/402860521_RewardFlow_Topology-Aware_Reward_Propagation_on_State_Graphs_for_Agentic_RL_with_Large_Language_Models"},{"title":"GitHub - tmlr-group/RewardFlow: [arXiv:2603.18859] \"RewardFlow: Topology-Aware Reward Propagation on State Graphs for Agentic RL with Large Language Models\" · GitHub","url":"https://github.com/tmlr-group/RewardFlow"},{"title":"RewardFlow: Topology-Aware Reward Propagation on State Graphs for Agentic RL with Large Language Models","url":"https://arxiv.org/pdf/2603.18859"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/recent?show=500&skip=725"},{"title":"[2604.08536v1] RewardFlow: Generate Images by Optimizing What You Reward","url":"https://arxiv.org/abs/2604.08536v1"}]

I found the paper you're looking for! Here are the key details about RewardFlow (arXiv:2603.18859):

## Overview
RewardFlow is a lightweight method for estimating state-level rewards tailored to agentic reasoning tasks. The paper was submitted on March 19, 2026, and the authors include researchers from Hong Kong Baptist University, TCL Corporate Research, Shanghai Jiao Tong University, and others.

## Problem Addressed
The inherent sparsity of terminal rewards hinders fine-grained, state-level optimization, and although process reward modeling offers a promising alternative, training dedicated reward models often entails substantial computational costs and scaling difficulties.

## Key Technical Approach
RewardFlow leverages the intrinsic topological structure of states within reasoning trajectories by constructing state graphs, enabling an analysis of state-wise contributions to success, followed by topology-aware graph propagation to quantify contributions and yield objective, state-level rewards.

## Results
When integrated as dense rewards for RL optimization, RewardFlow substantially outperforms prior RL baselines across four agentic reasoning benchmarks, demonstrating superior performance, robustness, and training efficiency.

The paper focuses on enhancing the reasoning capabilities of large language models through reinforcement learning by providing better reward signals for intermediate states during agent-environment interactions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "627d9263-4470-4b78-a5ca-8b902ac22474",
  "isSidechain": false,
  "promptId": "92cfa655-8f2a-41b8-b21e-d398291b2706",
  "type": "user",
  "uuid": "8b473eab-6ddb-48c9-9328-820f760a0388",
  "toolUseResult": {
    "query": "RewardFlow graph reward propagation reasoning 2026 arXiv:2603.18859",
    "results": [
      {
        "tool_use_id": "srvtoolu_0117uiH5BBy3rrZUhEaBVk7r",
        "content": [
          {
            "title": "RewardFlow: Topology-Aware Reward Propagation on State Graphs for Agentic RL with Large Language Models",
            "url": "https://arxiv.org/html/2603.18859"
          },
          {
            "title": "[2603.18859] RewardFlow: Topology-Aware Reward Propagation on State Graphs for Agentic RL with Large Language Models",
            "url": "https://arxiv.org/abs/2603.18859"
          },
          {
            "title": "RewardFlow: Topology-Aware Reward Propagation on State Graphs for Agentic RL with Large Language Models | Request PDF",
            "url": "https://www.researchgate.net/publication/402860521_RewardFlow_Topology-Aware_Reward_Propagation_on_State_Graphs_for_Agentic_RL_with_Large_Language_Models"
          },
          {
            "title": "GitHub - tmlr-group/RewardFlow: [arXiv:2603.18859] \"RewardFlow: Topology-Aware Reward Propagation on State Graphs for Agentic RL with Large Language Models\" · GitHub",
            "url": "https://github.com/tmlr-group/RewardFlow"
          },
          {
            "title": "RewardFlow: Topology-Aware Reward Propagation on State Graphs for Agentic RL with Large Language Models",
            "url": "https://arxiv.org/pdf/2603.18859"
          },
          {
            "title": "Computer Science",
            "url": "https://arxiv.org/list/cs/recent?show=500&skip=725"
          },
          {
            "title": "[2604.08536v1] RewardFlow: Generate Images by Optimizing What You Reward",
            "url": "https://arxiv.org/abs/2604.08536v1"
          }
        ]
      },
      "I found the paper you're looking for! Here are the key details about RewardFlow (arXiv:2603.18859):\n\n## Overview\nRewardFlow is a lightweight method for estimating state-level rewards tailored to agentic reasoning tasks. The paper was submitted on March 19, 2026, and the authors include researchers from Hong Kong Baptist University, TCL Corporate Research, Shanghai Jiao Tong University, and others.\n\n## Problem Addressed\nThe inherent sparsity of terminal rewards hinders fine-grained, state-level optimization, and although process reward modeling offers a promising alternative, training dedicated reward models often entails substantial computational costs and scaling difficulties.\n\n## Key Technical Approach\nRewardFlow leverages the intrinsic topological structure of states within reasoning trajectories by constructing state graphs, enabling an analysis of state-wise contributions to success, followed by topology-aware graph propagation to quantify contributions and yield objective, state-level rewards.\n\n## Results\nWhen integrated as dense rewards for RL optimization, RewardFlow substantially outperforms prior RL baselines across four agentic reasoning benchmarks, demonstrating superior performance, robustness, and training efficiency.\n\nThe paper focuses on enhancing the reasoning capabilities of large language models through reinforcement learning by providing better reward signals for intermediate states during agent-environment interactions."
    ],
    "durationSeconds": 8.648782500000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "627d9263-4470-4b78-a5ca-8b902ac22474",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9d15703d-7612-480c-9cbd-2adbcb5cdf2b",
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
  "lastPrompt": "# Premise-Graph Contrastive Training for Logic-Grounded Process Reward Models  ## Core Problem  Current process reward models detect consistency rather than causality. \"Reward Models Identify Consiste…",
  "leafUuid": "8b473eab-6ddb-48c9-9328-820f760a0388",
  "sessionId": "9d15703d-7612-480c-9cbd-2adbcb5cdf2b"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Premise-graph contrastive training for process reward models",
  "sessionId": "9d15703d-7612-480c-9cbd-2adbcb5cdf2b"
}
```

---

### Tool result

_source line 35 · 2026-05-27T08:55:29.176Z_

<details><summary>↩ Tool result · `toolu_01A8sgxceDUvCJHVFM4gDXwu`</summary>

```text
Web search results for query: "verifiable process reward model reasoning structure-aware training 2026"

Links: [{"title":"Learning to Generate Formally Verifiable Step-by-Step Logic Reasoning via Structured Formal Intermediaries","url":"https://arxiv.org/pdf/2603.29500"},{"title":"Knowledge-to-Verification: Unlocking Reinforcement Learning with Verifiable Rewards for LLMs in Knowledge-Intensive Domains | OpenReview","url":"https://openreview.net/forum?id=EVS7SeKBqI"},{"title":"StructVRM: Aligning Multimodal Reasoning with Structured and Verifiable Reward Models","url":"https://arxiv.org/pdf/2508.05383"},{"title":"RLVR: The Training Breakthrough That Will Make Reasoning AI Verifiable | by RAKTIM SINGH | Medium","url":"https://medium.com/@raktims2210/rlvr-the-training-breakthrough-that-will-make-reasoning-ai-verifiable-cf4209e79669"},{"title":"(PDF) Beyond Outcome Verification: Verifiable Process Reward Models for Structured Reasoning","url":"https://www.researchgate.net/publication/400083746_Beyond_Outcome_Verification_Verifiable_Process_Reward_Models_for_Structured_Reasoning"},{"title":"Verifiable Process Reward Models for Structured Reasoning","url":"https://www.arxiv.org/pdf/2601.17223"},{"title":"SARL: Optimizing the Path of Reasoning with Structure Aware Reinforcement Learning","url":"https://arxiv.org/html/2603.27977"},{"title":"Post-Training as Reweighting: A Stochastic View of Reasoning Trajectories in Language Models","url":"https://arxiv.org/pdf/2511.07368"},{"title":"RM-R1: Reward Modeling as Reasoning","url":"https://arxiv.org/pdf/2505.02387"}]

Based on the search results, here are the key findings related to verifiable process reward models with reasoning structure-aware training from 2026:

## Verifiable Process Reward Models (VPRMs)

Verifiable Process Reward Models (VPRMs) are a reinforcement-learning framework in which intermediate reasoning steps are checked by deterministic, rule-based verifiers. VPRMs generate reasoning that adheres closely to domain rules and achieve substantially higher coherence between step-level decisions and final labels, with up to 20% higher F1 than state-of-the-art models.

## Structure-Aware Reinforcement Learning (SARL)

Structure Aware Reinforcement Learning (SARL) is a label-free framework that constructs per-response reasoning maps from intermediate thinking steps and rewards their reasoning topology. SARL addresses whether general reasoning ability can be improved by teaching models how to think (the structure of reasoning) rather than what to produce, shifting supervision from destination to path and encouraging reasoning trajectories that are both locally coherent and globally efficient.

## Related Approaches

PRoSFI (Process Reward over Structured Formal Intermediates) is a novel reward method that enhances reasoning reliability without compromising accuracy. Additionally, training with structured, verifiable rewards is an effective approach for advancing the capabilities of multimodal models in complex, real-world reasoning domains.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "85b6e261-5829-430a-86e7-7c1f66d73afb",
  "isSidechain": false,
  "promptId": "92cfa655-8f2a-41b8-b21e-d398291b2706",
  "type": "user",
  "uuid": "33c23490-cb9d-4183-ac75-e044d743db8f",
  "toolUseResult": {
    "query": "verifiable process reward model reasoning structure-aware training 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GGgLdxAMx9BKVdSg8grHBL",
        "content": [
          {
            "title": "Learning to Generate Formally Verifiable Step-by-Step Logic Reasoning via Structured Formal Intermediaries",
            "url": "https://arxiv.org/pdf/2603.29500"
          },
          {
            "title": "Knowledge-to-Verification: Unlocking Reinforcement Learning with Verifiable Rewards for LLMs in Knowledge-Intensive Domains | OpenReview",
            "url": "https://openreview.net/forum?id=EVS7SeKBqI"
          },
          {
            "title": "StructVRM: Aligning Multimodal Reasoning with Structured and Verifiable Reward Models",
            "url": "https://arxiv.org/pdf/2508.05383"
          },
          {
            "title": "RLVR: The Training Breakthrough That Will Make Reasoning AI Verifiable | by RAKTIM SINGH | Medium",
            "url": "https://medium.com/@raktims2210/rlvr-the-training-breakthrough-that-will-make-reasoning-ai-verifiable-cf4209e79669"
          },
          {
            "title": "(PDF) Beyond Outcome Verification: Verifiable Process Reward Models for Structured Reasoning",
            "url": "https://www.researchgate.net/publication/400083746_Beyond_Outcome_Verification_Verifiable_Process_Reward_Models_for_Structured_Reasoning"
          },
          {
            "title": "Verifiable Process Reward Models for Structured Reasoning",
            "url": "https://www.arxiv.org/pdf/2601.17223"
          },
          {
            "title": "SARL: Optimizing the Path of Reasoning with Structure Aware Reinforcement Learning",
            "url": "https://arxiv.org/html/2603.27977"
          },
          {
            "title": "Post-Training as Reweighting: A Stochastic View of Reasoning Trajectories in Language Models",
            "url": "https://arxiv.org/pdf/2511.07368"
          },
          {
            "title": "RM-R1: Reward Modeling as Reasoning",
            "url": "https://arxiv.org/pdf/2505.02387"
          }
        ]
      },
      "Based on the search results, here are the key findings related to verifiable process reward models with reasoning structure-aware training from 2026:\n\n## Verifiable Process Reward Models (VPRMs)\n\nVerifiable Process Reward Models (VPRMs) are a reinforcement-learning framework in which intermediate reasoning steps are checked by deterministic, rule-based verifiers. VPRMs generate reasoning that adheres closely to domain rules and achieve substantially higher coherence between step-level decisions and final labels, with up to 20% higher F1 than state-of-the-art models.\n\n## Structure-Aware Reinforcement Learning (SARL)\n\nStructure Aware Reinforcement Learning (SARL) is a label-free framework that constructs per-response reasoning maps from intermediate thinking steps and rewards their reasoning topology. SARL addresses whether general reasoning ability can be improved by teaching models how to think (the structure of reasoning) rather than what to produce, shifting supervision from destination to path and encouraging reasoning trajectories that are both locally coherent and globally efficient.\n\n## Related Approaches\n\nPRoSFI (Process Reward over Structured Formal Intermediates) is a novel reward method that enhances reasoning reliability without compromising accuracy. Additionally, training with structured, verifiable rewards is an effective approach for advancing the capabilities of multimodal models in complex, real-world reasoning domains."
    ],
    "durationSeconds": 9.789309151000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "85b6e261-5829-430a-86e7-7c1f66d73afb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9d15703d-7612-480c-9cbd-2adbcb5cdf2b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 36 · 2026-05-27T08:55:29.180Z_

```json
{
  "parentUuid": "33c23490-cb9d-4183-ac75-e044d743db8f",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "9984e3ba-3159-435a-b934-0171664becec",
  "timestamp": "2026-05-27T08:55:29.180Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9d15703d-7612-480c-9cbd-2adbcb5cdf2b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 37 · 2026-05-27T08:55:33.316Z_

<details><summary>Logged reasoning block</summary>

```text
Let me search for one more critical piece - the SARL paper since it seems highly relevant (structure-aware RL that rewards reasoning topology), and also check if there's any work that directly combines graph structure with contrastive training for PRMs.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9984e3ba-3159-435a-b934-0171664becec",
  "isSidechain": false,
  "requestId": "req_011CbSnzDuoLqrkJx6sfNXZq",
  "type": "assistant",
  "uuid": "cec001ff-3dc7-4391-9622-054c68cda367",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9d15703d-7612-480c-9cbd-2adbcb5cdf2b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BqDYVMiA535e3k1p46dya7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2753,
      "cache_read_input_tokens": 25558,
      "output_tokens": 188,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2753,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 188,
          "cache_read_input_tokens": 25558,
          "cache_creation_input_tokens": 2753,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2753
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

_source line 38 · 2026-05-27T08:55:33.763Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DRxjM1AmK8gTiHBuhwqCUw`</summary>

```json
{
  "query": "SARL structure aware reinforcement learning reasoning topology reward 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cec001ff-3dc7-4391-9622-054c68cda367",
  "isSidechain": false,
  "requestId": "req_011CbSnzDuoLqrkJx6sfNXZq",
  "type": "assistant",
  "uuid": "b85ad388-d6ab-402b-939a-27126faceca2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9d15703d-7612-480c-9cbd-2adbcb5cdf2b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BqDYVMiA535e3k1p46dya7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2753,
      "cache_read_input_tokens": 25558,
      "output_tokens": 188,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2753,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 188,
          "cache_read_input_tokens": 25558,
          "cache_creation_input_tokens": 2753,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2753
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

_source line 39 · 2026-05-27T08:55:34.356Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MUMNBs4ryZwEhG8KeT7azU`</summary>

```json
{
  "query": "PathFinder-PRM error-aware process reward model PRMBench 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b85ad388-d6ab-402b-939a-27126faceca2",
  "isSidechain": false,
  "requestId": "req_011CbSnzDuoLqrkJx6sfNXZq",
  "type": "assistant",
  "uuid": "7bc02f19-9a61-4a93-9ecc-d204e06e1af5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9d15703d-7612-480c-9cbd-2adbcb5cdf2b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BqDYVMiA535e3k1p46dya7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2753,
      "cache_read_input_tokens": 25558,
      "output_tokens": 188,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2753,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 188,
          "cache_read_input_tokens": 25558,
          "cache_creation_input_tokens": 2753,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2753
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

_source line 40 · 2026-05-27T08:55:41.943Z_

<details><summary>↩ Tool result · `toolu_01MUMNBs4ryZwEhG8KeT7azU`</summary>

```text
Web search results for query: "PathFinder-PRM error-aware process reward model PRMBench 2025"

Links: [{"title":"[2505.19706] Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision","url":"https://arxiv.org/abs/2505.19706"},{"title":"PRMBench: Benchmark for Process-level Math Reasoning","url":"https://www.emergentmind.com/topics/prmbench"},{"title":"Process-Supervised Reward Model","url":"https://www.emergentmind.com/topics/process-supervised-reward-model-prm"},{"title":"PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models | Request PDF","url":"https://www.researchgate.net/publication/394270805_PRMBench_A_Fine-grained_and_Challenging_Benchmark_for_Process-Level_Reward_Models"},{"title":"Process-supervised Reward Models (PRMs)","url":"https://www.emergentmind.com/topics/process-supervised-reward-models-prm"},{"title":"Process Reward Models: Step-Level Feedback for LLMs","url":"https://www.emergentmind.com/topics/process-reward-models-prm"},{"title":"GitHub - declare-lab/PathFinder-PRM: This repository contains the official implementation of Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision.","url":"https://github.com/declare-lab/PathFinder-PRM"},{"title":"Improving Process Reward Models with Error-Aware ...","url":"https://arxiv.org/pdf/2505.19706"}]

Based on the search results, here's what I found about PathFinder-PRM, error-aware process reward models, and PRMBench:

## PathFinder-PRM Overview

PathFinder-PRM is a novel hierarchical, error-aware discriminative PRM that first classifies math and consistency errors at each step, then combines these fine-grained signals to estimate step correctness.

## Dataset and Training

To train PathFinder-PRM, a 400K-sample dataset was constructed by enriching the human-annotated PRM800K corpus and RLHFlow Mistral traces with three-dimensional step-level labels.

## Performance on PRMBench

On PRMBench, PathFinder-PRM achieves a new state-of-the-art PRMScore of 67.7, outperforming the prior best (65.5) while using 3 times less data. When applied to reward guided greedy search, the model yields prm@8 48.3, a +1.5 point gain over the strongest baseline.

## Key Innovation

Hierarchical models such as PathFinder-PRM explicitly decompose errors into math and consistency dimensions before reward assignment, increasing interpretability and data efficiency.

The research was published in May 2025 and has established a new benchmark for process reward model evaluation in mathematical reasoning tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7bc02f19-9a61-4a93-9ecc-d204e06e1af5",
  "isSidechain": false,
  "promptId": "92cfa655-8f2a-41b8-b21e-d398291b2706",
  "type": "user",
  "uuid": "fc19fcb2-7b3a-4b0f-880c-c34b7e54172a",
  "toolUseResult": {
    "query": "PathFinder-PRM error-aware process reward model PRMBench 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01AyrUmQ3zF4TAwbNk1f1dtM",
        "content": [
          {
            "title": "[2505.19706] Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision",
            "url": "https://arxiv.org/abs/2505.19706"
          },
          {
            "title": "PRMBench: Benchmark for Process-level Math Reasoning",
            "url": "https://www.emergentmind.com/topics/prmbench"
          },
          {
            "title": "Process-Supervised Reward Model",
            "url": "https://www.emergentmind.com/topics/process-supervised-reward-model-prm"
          },
          {
            "title": "PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models | Request PDF",
            "url": "https://www.researchgate.net/publication/394270805_PRMBench_A_Fine-grained_and_Challenging_Benchmark_for_Process-Level_Reward_Models"
          },
          {
            "title": "Process-supervised Reward Models (PRMs)",
            "url": "https://www.emergentmind.com/topics/process-supervised-reward-models-prm"
          },
          {
            "title": "Process Reward Models: Step-Level Feedback for LLMs",
            "url": "https://www.emergentmind.com/topics/process-reward-models-prm"
          },
          {
            "title": "GitHub - declare-lab/PathFinder-PRM: This repository contains the official implementation of Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision.",
            "url": "https://github.com/declare-lab/PathFinder-PRM"
          },
          {
            "title": "Improving Process Reward Models with Error-Aware ...",
            "url": "https://arxiv.org/pdf/2505.19706"
          }
        ]
      },
      "Based on the search results, here's what I found about PathFinder-PRM, error-aware process reward models, and PRMBench:\n\n## PathFinder-PRM Overview\n\nPathFinder-PRM is a novel hierarchical, error-aware discriminative PRM that first classifies math and consistency errors at each step, then combines these fine-grained signals to estimate step correctness.\n\n## Dataset and Training\n\nTo train PathFinder-PRM, a 400K-sample dataset was constructed by enriching the human-annotated PRM800K corpus and RLHFlow Mistral traces with three-dimensional step-level labels.\n\n## Performance on PRMBench\n\nOn PRMBench, PathFinder-PRM achieves a new state-of-the-art PRMScore of 67.7, outperforming the prior best (65.5) while using 3 times less data. When applied to reward guided greedy search, the model yields prm@8 48.3, a +1.5 point gain over the strongest baseline.\n\n## Key Innovation\n\nHierarchical models such as PathFinder-PRM explicitly decompose errors into math and consistency dimensions before reward assignment, increasing interpretability and data efficiency.\n\nThe research was published in May 2025 and has established a new benchmark for process reward model evaluation in mathematical reasoning tasks."
    ],
    "durationSeconds": 7.583726088000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "7bc02f19-9a61-4a93-9ecc-d204e06e1af5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9d15703d-7612-480c-9cbd-2adbcb5cdf2b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-27T08:55:47.294Z_

<details><summary>↩ Tool result · `toolu_01DRxjM1AmK8gTiHBuhwqCUw`</summary>

```text
Web search results for query: "SARL structure aware reinforcement learning reasoning topology reward 2026 arxiv"

Links: [{"title":"[2603.27977] SARL: Label-Free Reinforcement Learning by Rewarding Reasoning Topology","url":"https://arxiv.org/abs/2603.27977"},{"title":"SARL: Optimizing the Path of Reasoning with Structure Aware Reinforcement Learning","url":"https://arxiv.org/html/2603.27977"},{"title":"SARL: Label-Free Reinforcement Learning by Rewarding Reasoning Topology","url":"https://arxiv.org/pdf/2603.27977"},{"title":"RewardFlow: Topology-Aware Reward Propagation on State Graphs for Agentic RL with Large Language Models","url":"https://arxiv.org/pdf/2603.18859"},{"title":"Graph Reasoning Paradigm: Structured and Symbolic Reasoning with Topology-Aware Reinforcement Learning for Large Language Models","url":"https://arxiv.org/pdf/2601.12995"}]

I found the paper you're looking for! Here are the results:

## SARL: Label-Free Reinforcement Learning by Rewarding Reasoning Topology

The paper is authored by Yifan Wang, Bolian Li, David Cho, Ruqi Zhang, Fanping Sui, and Ananth Grama from Purdue University and Texas Instruments.

**Key Concepts:**

SARL is a label-free framework that constructs per-response reasoning maps from intermediate thinking steps and rewards their reasoning topology. The work investigates whether general reasoning ability can be improved by teaching models how to think (the structure of reasoning) rather than what to produce (the outcome of reasoning).

**Main Innovation:**

SARL shifts supervision from destination to path, encouraging reasoning trajectories that are both locally coherent and globally efficient. The framework constructs a per-response Reasoning Map from intermediate thinking steps and rewards its small world topology, inspired by complex networks and the functional organization of the human brain.

**Results:**

On Qwen3-4B, SARL surpassed ground truth based RL and prior label-free RL baselines, achieving the best average gain of 9.1% under PPO and 11.6% under GRPO on math tasks and 34.6% under PPO and 30.4% under GRPO on open-ended tasks.

The paper was submitted on March 30, 2026, with a revised version on May 10, 2026. You can find the full paper at arxiv.org/abs/2603.27977.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b85ad388-d6ab-402b-939a-27126faceca2",
  "isSidechain": false,
  "promptId": "92cfa655-8f2a-41b8-b21e-d398291b2706",
  "type": "user",
  "uuid": "bdea80cb-994c-4a7c-8a5e-7692eb298b64",
  "toolUseResult": {
    "query": "SARL structure aware reinforcement learning reasoning topology reward 2026 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_013S2roHR3WSaAg56oh2XzbV",
        "content": [
          {
            "title": "[2603.27977] SARL: Label-Free Reinforcement Learning by Rewarding Reasoning Topology",
            "url": "https://arxiv.org/abs/2603.27977"
          },
          {
            "title": "SARL: Optimizing the Path of Reasoning with Structure Aware Reinforcement Learning",
            "url": "https://arxiv.org/html/2603.27977"
          },
          {
            "title": "SARL: Label-Free Reinforcement Learning by Rewarding Reasoning Topology",
            "url": "https://arxiv.org/pdf/2603.27977"
          },
          {
            "title": "RewardFlow: Topology-Aware Reward Propagation on State Graphs for Agentic RL with Large Language Models",
            "url": "https://arxiv.org/pdf/2603.18859"
          },
          {
            "title": "Graph Reasoning Paradigm: Structured and Symbolic Reasoning with Topology-Aware Reinforcement Learning for Large Language Models",
            "url": "https://arxiv.org/pdf/2601.12995"
          }
        ]
      },
      "I found the paper you're looking for! Here are the results:\n\n## SARL: Label-Free Reinforcement Learning by Rewarding Reasoning Topology\n\nThe paper is authored by Yifan Wang, Bolian Li, David Cho, Ruqi Zhang, Fanping Sui, and Ananth Grama from Purdue University and Texas Instruments.\n\n**Key Concepts:**\n\nSARL is a label-free framework that constructs per-response reasoning maps from intermediate thinking steps and rewards their reasoning topology. The work investigates whether general reasoning ability can be improved by teaching models how to think (the structure of reasoning) rather than what to produce (the outcome of reasoning).\n\n**Main Innovation:**\n\nSARL shifts supervision from destination to path, encouraging reasoning trajectories that are both locally coherent and globally efficient. The framework constructs a per-response Reasoning Map from intermediate thinking steps and rewards its small world topology, inspired by complex networks and the functional organization of the human brain.\n\n**Results:**\n\nOn Qwen3-4B, SARL surpassed ground truth based RL and prior label-free RL baselines, achieving the best average gain of 9.1% under PPO and 11.6% under GRPO on math tasks and 34.6% under PPO and 30.4% under GRPO on open-ended tasks.\n\nThe paper was submitted on March 30, 2026, with a revised version on May 10, 2026. You can find the full paper at arxiv.org/abs/2603.27977."
    ],
    "durationSeconds": 13.526364702999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "b85ad388-d6ab-402b-939a-27126faceca2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9d15703d-7612-480c-9cbd-2adbcb5cdf2b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-27T08:56:50.775Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a solid understanding of the landscape. Let me synthesize my findings and analyze this proposal.

Key findings from my research:

1. **"From Chains to DAGs"** (arXiv:2601.17593) - Confirms that LLM hidden states linearly encode DAG structure. The proposal correctly cites this.

2. **SARL** (arXiv:2603.27977, March 2026) - This is a very important paper the proposal DOES NOT cite. SARL rewards reasoning topology directly, constructing "reasoning maps" and rewarding their small-world topology. 

While SARL operates in the RL policy training domain rather than PRM training, it shares the core insight of rewarding structural reasoning topology—which represents a notable gap in the proposal's related work section.

3. **CRV** (ICLR 2026 Oral, arXiv:2510.09312) - White-box verification via attribution graph structural fingerprints. The proposal cites this correctly.

4. **RewardFlow** (arXiv:2603.18859) - Topology-aware reward propagation. Correctly cited.

5. **VPRMs** (arXiv:2601.17223) - Verifiable PRMs using rule-based verification for structured reasoning. This is mentioned briefly in searches but NOT cited in the proposal, which could be an oversight.

6. **PathFinder-PRM** (arXiv:2505.19706) - Error-aware hierarchical PRM achieving SOTA 67.7 on PRMBench. Correctly cited.

7. **CPMI** (arXiv:2604.10660) - Contrastive MI for PRM auto-labeling. Correctly cited.

8. **Factored Causal RL** (ICML 2026, arXiv:2601.21350) - Causal/non-causal factor separation. Correctly cited.

9. **"When Reward Hacking Rebounds"** (arXiv:2604.01476) - Representation-level shortcut detection. Correctly cited.

Now I'm evaluating the proposal's strengths, starting with its core insight being well-motivated.

**Strengths:**
- The core insight is well-motivated: PRMs detect consistency not causality, and LLMs already encode DAG structure in hidden states, so contrastive training can bridge the gap
- The related work coverage is impressively comprehensive
- The positioning against each related work category is specific and defensible
- The claim is carefully scoped ("premise-dependency awareness" not "full logical causality")
- The evaluation plan is thorough with proper controls

**Critical assessment:**

I'm examining whether a simpler alternative would work: just adding auxiliary linear probe losses to predict DAG properties from hidden states instead of contrastive learning. The proposal argues this would only optimize local-layer information retention without affecting cross-layer representation flow or end-to-end reward prediction, but that reasoning isn't fully convincing—linear probe auxiliary losses would actually create gradient signals flowing through the network, so the claim about local-layer optimization seems overstated.

I'm also noticing some gaps in the related work: SARL (arXiv:2603.27977) shares the core idea of rewarding reasoning structure in RL policy training, and VPRMs (arXiv:2601.17223) use rule-based verifiers for structured reasoning steps, providing an alternative approach that sidesteps the representation learning problem entirely. Both deserve acknowledgment.

The novelty claim does seem to hold up though - using premise-dependency DAGs to construct contrastive training pairs that reorganize PRM embedding space is genuinely novel. Existing work either uses graph structure at inference time rather than training time, reorganizes representation space without domain-specific logical structure, or applies similar ideas to different domains like policy RL or reading comprehension. The significance is clear too, given that 43% of PRM reward gains come from stylistic shortcuts, and there's a substantial gap between current SOTA and human performance on PRMBench.

The core assumption that contrastive training will actually force structural representations rather than just learning new surface patterns is the real bet here. The graph-breaking negatives maintain fluency which should help, but there's no guarantee the model won't find alternative shortcuts. That said, the "representation-utilization gap" framing is compelling - the idea that models already understand structure but standard training doesn't leverage it is a clean, testable claim.

For improvements, SARL should definitely be cited and differentiated more carefully. While SARL operates at the RL policy level rather than PRM training, its core insight about rewarding reasoning topology could be relevant to strengthen the positioning.

VPRMs represent a competing paradigm worth addressing directly - they use rule-based verifiers instead of learned representations, so the proposal should clarify that PGCT targets domains where formal verification isn't feasible. The representation-utilization gap claim could also be sharpened by making a specific prediction: if standard PRMs actually have higher DAG-structure probing accuracy in their middle layers, that would directly support the hypothesis that the structure is already there but underutilized.

On the auxiliary probe critique, I need to be more precise - the real advantage of contrastive training over auxiliary losses isn't that auxiliary losses don't propagate gradients, but rather that contrastive learning in the reward-relevant embedding space directly ties structural awareness to the reward objective, whereas auxiliary probes only enforce local structural encoding without that explicit connection. Plus, contrastive loss on the final embedding lets the model organize structure flexibly across layers instead of requiring manual layer selection.

The proposal could also emphasize that PGCT represents a paradigm shift from reactive defenses like CRA and adversarial training - which patch specific failure modes - toward proactive representation reorganization that bakes structural awareness into the model from training time. And there's an underexplored conceptual angle here: the shift from point-wise supervision to relational supervision. Every existing PRM method uses point-wise classification, but PGCT introduces relational supervision by examining how steps relate to each other structurally. The core novelty is solid and the positioning is thoughtful with strong related work coverage. I see a few concrete ways to strengthen it: better positioning relative to SARL and VPRM, developing the relational supervision framing as a more central conceptual contribution rather than burying it, and tightening the argument about why auxiliary probes aren't necessary here.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bdea80cb-994c-4a7c-8a5e-7692eb298b64",
  "isSidechain": false,
  "requestId": "req_011CbSo1ZTpGRi6vXJ93ywVT",
  "type": "assistant",
  "uuid": "c2394024-0ac6-4445-aa01-5effc9f899f3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9d15703d-7612-480c-9cbd-2adbcb5cdf2b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S6d6uMZpiWupDCM2zEd2eG",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 778,
      "cache_creation_input_tokens": 850,
      "cache_read_input_tokens": 28311,
      "output_tokens": 5935,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 850,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 778,
          "output_tokens": 5935,
          "cache_read_input_tokens": 28311,
          "cache_creation_input_tokens": 850,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 850
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

_source line 43 · 2026-05-27T08:58:06.573Z_

Now I have sufficient research to provide my analysis. Let me compile my findings.

---

【状态】: 有发掘空间

【前置调研发现】
- **SARL (arXiv:2603.27977, March 2026)**: Structure Aware Reinforcement Learning — a label-free RL framework that constructs per-response "Reasoning Maps" from intermediate thinking steps and rewards their small-world topology. SARL operates on policy RL training (not PRM training), achieving +9-12% on math tasks. **This paper is NOT cited in the proposal but shares the core intuition of rewarding reasoning topology.** The differentiation (policy RL vs. PRM representation learning; small-world topology vs. premise-dependency DAGs) is clear but must be explicitly stated.
- **VPRMs / Beyond Outcome Verification (arXiv:2601.17223, Jan 2026)**: Verifiable Process Reward Models use rule-based, deterministic verifiers for step-level verification in structured reasoning, achieving up to +20% F1 over neural PRMs. **Also NOT cited.** Represents a competing paradigm: bypass learned representations entirely via formal verification.
- **CRV (arXiv:2510.09312, ICLR 2026 Oral)**: White-box verification via attribution graph structural fingerprints — 98.8% on arithmetic, 93.4% on GSM8K. Confirms graph structure carries verification signal but operates at inference time, not training time. Correctly cited.
- **Factored Causal RL (arXiv:2601.21350, ICML 2026)**: Causal/non-causal latent factor separation via gradient reversal for reward models. Domain-agnostic statistical decomposition. Correctly cited and differentiated.
- **CPMI (arXiv:2604.10660, April 2026)**: Contrastive MI for auto-labeling, no dependency graphs. Correctly cited.
- **PathFinder-PRM (arXiv:2505.19706, May 2025)**: Error-aware hierarchical PRM with SOTA 67.7 on PRMBench. Correctly cited.
- **From Chains to DAGs (arXiv:2601.17593, Jan 2026)**: Confirms DAG structure linearly recoverable from LLM hidden states. Correctly cited and central to the proposal's motivation.
- 调研总结: 当前领域在三条独立轨道上推进PRM改进：(1) 表示空间鲁棒性（因果分解、对抗训练），(2) 推理时结构验证（归因图、代码验证），(3) 训练信号改进（自动标注、层次化标注）。PGCT 处于这三条轨道的交叉点——将结构先验注入训练时表示学习——这个交叉位置确实是空白的，但需要更明确地与 SARL 和 VPRM 这两条近邻路线划清界限。

---

【发掘点 1】
- 维度: related work 差异化
- 内容: **必须补充 SARL (arXiv:2603.27977) 的定位。** SARL 是 2026 年 3 月的工作，其核心主张与 PGCT 高度相关——"teaching models how to think (the structure of reasoning) rather than what to produce"——并且直接在推理拓扑上施加奖励。虽然 SARL 作用于 RL 策略训练而非 PRM 表示学习，且其拓扑指标是通用的小世界网络性质（聚类系数、最短路径）而非领域接地的前提依赖 DAG，但审稿人很可能会 flag 这篇论文作为"already uses reasoning topology for training"。建议在 Related Work 的 "Graph structure for verification" 段落中增加一个明确的差异化声明：SARL rewards topology of policy outputs (generation-side), while PGCT constrains the topology of verifier representations (evaluation-side); SARL's topology metric is domain-agnostic (small-world properties), while PGCT's is domain-grounded (premise dependency extracted from mathematical proof structure).
- 价值: 防御 Related Work 差异化维度的审稿攻击。如果审稿人发现 SARL 未被引用，会质疑作者对领域的掌握程度，进而动摇整个 novelty claim 的可信度。
- 调研依据: 直接基于搜索到的 SARL (arXiv:2603.27977) 论文内容。

【发掘点 2】
- 维度: related work 差异化
- 内容: **补充 VPRMs (arXiv:2601.17223) 作为竞争范式的定位。** VPRMs 完全绕过了"表示学习"问题——用确定性规则验证器替代神经网络 PRM，在结构化推理上获得 +20% F1。这代表一种"何必修 PRM？直接用形式化验证"的立场。PGCT 应该明确回应：(1) 形式化验证仅适用于可形式化的领域（数学中一部分），PGCT 的表示学习方法更通用；(2) 即使在可形式化领域，PGCT 的结构感知 PRM 可以与形式化验证互补（例如作为 fallback when formal verification fails or as a faster screening step）。不回应此范式会让审稿人认为作者没有考虑过"为什么还要用神经 PRM"这个根本问题。
- 价值: 堵住审稿人"为什么不直接用形式化验证"的质疑路径，同时更清晰地定位 PGCT 的适用范围，属于 Related Work 差异化 + Significance 双重提升。
- 调研依据: 基于搜索到的 VPRMs (arXiv:2601.17223) 论文。

【发掘点 3】
- 维度: 核心 claim 强化
- 内容: **"Relational supervision" 作为范式级贡献应被显著提升，而非埋在段落中间。** 当前 proposal 在 Research Opportunity 段落中提到 "shift from point-wise supervision to relational supervision"，但仅作为一句描述，没有将其作为 conceptual contribution 来发展。事实上，这可能是 PGCT 最重要的理论贡献：在 PRM 文献中，**所有**现有方法——包括 CRM（序列条件化）、APRM（对抗负样本）、PURE（最小形式信用聚合）、PathFinder-PRM（层次化分类）——最终都在做点逐步分类（"这一步对不对？"）。即使 CRM 条件化了前文步骤，其训练目标仍然是逐步的 binary cross-entropy。PGCT 是第一个引入**步间关系**作为训练信号的方法——"步骤之间的结构关系应该如何映射到表示空间"。这是 PRM 训练范式的根本性转变。建议在 Abstract 级别就建立 "point-wise → relational supervision" 的对比框架，并在 contribution list 中将其作为第一个 conceptual contribution 列出，而非只在方法描述中附带提及。
- 价值: 将 PGCT 从"一个使用 DAG 的具体方法"提升为"一种新的 PRM 训练范式"，直接提升 Significance 和 Novelty 的天花板。审稿人更容易给出 "novel paradigm" 而非 "neat trick" 的评价。
- 调研依据: 基于对 CRM、APRM、PURE、PathFinder-PRM 等所有现有 PRM 方法训练目标的系统对比——它们无一例外都是 point-wise step classification。

【发掘点 4】
- 维度: 前提假设质疑
- 内容: **对辅助 probe loss 的否定论证在机制上不够严谨，可能被审稿人反驳。** 当前 proposal 声称："using linear probes as auxiliary loss to directly maximize DAG-structure recovery in hidden states — would only optimize local-layer information retention without affecting cross-layer representation flow or end-to-end reward prediction"。这个论证有漏洞：auxiliary loss 作为训练目标，其梯度**会**通过 backbone 反向传播，因此**会**影响跨层表示流。审稿人如果有 representation learning 背景，会立刻 flag 这一点。建议修正为更精确的论证：(a) auxiliary probe loss 要求预先指定在哪一层施加监督（"From Chains to DAGs" 发现结构信息在中间层最强），但不同推理任务的最优层可能不同，引入额外超参数；(b) auxiliary probe loss 仅要求结构信息**可被线性读出**，但不要求该信息**被用于奖励预测**——模型可以在满足 probe loss 的同时仍然用表面特征做奖励决策；(c) 对比学习直接在奖励预测相关的 embedding 空间施加结构约束，构建了结构感知与奖励计算之间的显式链接。这三个论点比"只优化局部层信息保留"更站得住脚。
- 价值: 防御审稿人对方法设计选择的质疑。如果核心方法选择（为什么用 contrastive 而不是 auxiliary probe）的论证不严密，审稿人会质疑整个 approach 的理论基础。属于 Novelty 维度——确保 novelty claim 的逻辑链条无断裂。
- 调研依据: 基于 "From Chains to DAGs" (arXiv:2601.17593) 关于结构信息在中间层 peak 的发现，以及表示学习领域 auxiliary loss vs. contrastive loss 的一般性认知。

【发掘点 5】
- 维度: significance 提升
- 内容: **可以更鲜明地建立 "reactive vs. proactive robustness" 的对立框架来提升 significance。** 当前 landscape 分析将 CRA、APRM 等归为 "robustness-focused" 方法，但没有提炼出一个统一的批判视角。观察所有现有鲁棒性方法：CRA 是事后修补（post-hoc SAE correction）、APRM 是对抗性缝补（harder negatives targeting known attack patterns）、"When Reward Hacking Rebounds" 是检测并移除快捷方式方向。它们都是**reactive**——先发现了特定的失败模式，再针对性修补。这导致 cat-and-mouse 问题：每修补一种 hack，新的 hack 就会出现。PGCT 的范式本质是**proactive**——不针对任何特定失败模式，而是重组表示空间使其天然具备结构感知能力。这个 "reactive patching vs. proactive structural grounding" 的框架如果在 Introduction 中显著建立，会让审稿人更清楚地看到 PGCT 不仅是"又一个鲁棒性方法"，而是解决问题层级的提升。
- 价值: 直接提升 Significance——从"我们提出了一个新方法来提高 PRM 鲁棒性"提升为"我们提出了一个新的鲁棒性范式来根本性解决 PRM 的结构盲区"。
- 调研依据: 基于对 CRA (arXiv:2508.04216)、APRM (arXiv:2511.22888)、"When Reward Hacking Rebounds" (arXiv:2604.01476) 等工作的系统对比——它们均为 reactive 范式。

Sources:
- [SARL: Label-Free Reinforcement Learning by Rewarding Reasoning Topology](https://arxiv.org/abs/2603.27977)
- [Beyond Outcome Verification: Verifiable Process Reward Models for Structured Reasoning](https://arxiv.org/pdf/2601.17223)
- [CRV: Verifying Chain-of-Thought Reasoning via Its Computational Graph](https://arxiv.org/abs/2510.09312)
- [From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs](https://arxiv.org/abs/2601.17593)
- [CPMI: Efficient Process Reward Modeling via Contrastive Mutual Information](https://arxiv.org/abs/2604.10660)
- [PathFinder-PRM: Error Typing for Smarter Rewards](https://arxiv.org/abs/2505.19706)
- [Factored Causal Representation Learning for Robust Reward Modeling](https://arxiv.org/pdf/2601.21350)
- [When Reward Hacking Rebounds](https://arxiv.org/pdf/2604.01476)
- [RewardFlow: Topology-Aware Reward Propagation](https://arxiv.org/abs/2603.18859)
- [Reward Under Attack](https://openreview.net/pdf?id=Hw24VOppus)
- [Process Reward Models Survey](https://arxiv.org/html/2510.08049v3)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c2394024-0ac6-4445-aa01-5effc9f899f3",
  "isSidechain": false,
  "requestId": "req_011CbSo1ZTpGRi6vXJ93ywVT",
  "type": "assistant",
  "uuid": "790fd9b8-8846-4cc1-a518-4ef66f06b704",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9d15703d-7612-480c-9cbd-2adbcb5cdf2b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S6d6uMZpiWupDCM2zEd2eG",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 778,
      "cache_creation_input_tokens": 850,
      "cache_read_input_tokens": 28311,
      "output_tokens": 5935,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 850,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 778,
          "output_tokens": 5935,
          "cache_read_input_tokens": 28311,
          "cache_creation_input_tokens": 850,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 850
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

_source line 44_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Premise-Graph Contrastive Training for Logic-Grounded Process Reward Models  ## Core Problem  Current process reward models detect consistency rather than causality. \"Reward Models Identify Consiste…",
  "leafUuid": "790fd9b8-8846-4cc1-a518-4ef66f06b704",
  "sessionId": "9d15703d-7612-480c-9cbd-2adbcb5cdf2b"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "ai-title",
  "aiTitle": "Premise-graph contrastive training for process reward models",
  "sessionId": "9d15703d-7612-480c-9cbd-2adbcb5cdf2b"
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Premise-Graph Contrastive Training for Logic-Grounded Process Reward Models  ## Core Problem  Current process reward models detect consistency rather than causality. \"Reward Models Identify Consiste…",
  "leafUuid": "790fd9b8-8846-4cc1-a518-4ef66f06b704",
  "sessionId": "9d15703d-7612-480c-9cbd-2adbcb5cdf2b"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "ai-title",
  "aiTitle": "Premise-graph contrastive training for process reward models",
  "sessionId": "9d15703d-7612-480c-9cbd-2adbcb5cdf2b"
}
```

---
