# Research conversation: Skill-DAG-Guided Frontier Synthesis for Mathematical Compositional Generalization ## Core Problem LLMs exhibit a persist

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 62
- **Recorded user turns:** 1
- **Tool calls:** 19
- **Original source:** `logs/chats/exported-trajectories/account-3/63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1.jsonl`
- **Structured JSON:** [`8cc4fb7fa79958f2accc.json`](../../sessions/8c/8cc4fb7fa79958f2accc.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-29T12:26:02.139Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-29T12:26:02.139Z",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1",
  "content": "# Skill-DAG-Guided Frontier Synthesis for Mathematical Compositional Generalization\n\n## Core Problem\n\nLLMs exhibit a persistent compositional ceiling in mathematical reasoning: OMEGA (NeurIPS 2025, arXiv:2506.18880) demonstrates that RL fine-tuning (GRPO) improves exploratory generalization by +38pp but fails to improve compositional performance — combining distinct skills such as GCD computation with polynomial factoring. This ceiling persists across model scales and training paradigms.\n\nTwo theoretical results establish that **coverage of the compositional task space** is the prerequisite for breaking this ceiling: Redhardt et al. (NeurIPS 2025 Spotlight, arXiv:2507.07207) prove that standard MLPs can approximate compositional task families with linear neuron scaling, provided the training distribution sufficiently covers the task space; Chang et al. (ICLR 2026, arXiv:2505.20278) formalize how pattern matching on compositional task structures requires coverage of functional equivalence classes. Empirically, FLAMES (arXiv:2508.16514) confirms that in math data synthesis, maintaining higher problem coverage matters more than filtering for reliable solutions only. CHIMERA (arXiv:2603.00889) shows that 9K problems covering 1,179 fine-grained topics across 8 disciplines can match frontier-level reasoning performance, demonstrating the power of compact but high-coverage data — though its coverage is over topic diversity, not compositional skill-pair structure.\n\nThese results tell us **that** coverage matters, but not **where** to cover. Current synthesis methods either ignore compositional structure entirely or optimize proxies (difficulty, entropy, scarcity) rather than directly targeting coverage gaps. This paper tests two linked hypotheses: (1) that compositional coverage causally enables generalization even without RL, and more sharply, (2) that **DAG-guided gap-filling of the compositional skill space is more sample-efficient than random broad coverage**.\n\n## Hypothesis Structure\n\n- **H1 (Coverage → Generalization):** Increasing coverage of skill compositions in training data causally improves compositional generalization, even without RL. This extends Redhardt et al.'s theoretical result to the empirical math reasoning setting.\n- **H2 (Targeted > Random):** DAG-guided coverage-gap targeting achieves the same or better compositional gains with fewer training samples than random broad coverage of the skill-pair space. This is our primary novel contribution — tested by comparing coverage-guided synthesis against random-synthesis under fixed data budgets.\n- **H2+ (Structure Provides Signal):** Prerequisite DAG structure specifically predicts where coverage gaps are most harmful — i.e., DAG-connected gap-filling outperforms arbitrary-graph-connected gap-filling. This mechanistic hypothesis is tested by ablation A1 (DAG vs. random graph vs. no graph). If confirmed, it establishes that skill dependencies causally constrain compositional learning; if not, H2 still holds as a coverage-targeting contribution.\n\n## Research Landscape\n\n**Coverage-agnostic composition methods.** MathFusion (ACL 2025, arXiv:2503.16212) fuses problems via sequential/parallel/conditional strategies (+18pp) without skill-graph guidance — compositions are random. Agentic Proposing (arXiv:2602.03279, Feb 2026) achieves 91.6% AIME25 via difficulty-adaptive multi-granularity composition but optimizes difficulty, not coverage. MindLoom (arXiv:2605.21630, May 2026) composes atomic thought modes with a scarcity reward to encourage rare combinations — conceptually related to our coverage gap identification, but uses implicit RL-driven scarcity signals rather than explicit DAG-guided gap targeting, and applies thought modes sequentially without prerequisite structure.\n\n**Coverage-aware methods not applied to math composition.** STAT (ICLR 2026, arXiv:2510.10023) identifies atomic skill gaps via teacher-student profiling and synthesizes single-skill remediation — targeting individual skill deficiencies rather than skill combinations. STEPS (arXiv:2601.03676, Jan 2026) maximizes structural entropy over hierarchical skill taxonomies but validates only on instruction-following benchmarks (not math reasoning), uses flat taxonomy rather than prerequisite DAGs, and optimizes entropy rather than explicit coverage gaps. \"Less is More\" (arXiv:2504.14508) uses maximum coverage problem formulations for subset selection from existing synthetic data, demonstrating that coverage-based selection outperforms training on full datasets — but addresses data selection, not synthesis of missing compositions.\n\n**Skill graphs for data operations.** MASS (ICML 2025, arXiv:2503.14917) builds a 46K-skill, 1.18M-edge co-occurrence graph for scoring and selecting existing pretraining data (50–70% token efficiency gains). Its adjacency matrix has not been repurposed to identify missing compositions — the unexploited move our work takes.\n\n**DAG structures in math reasoning (disambiguation).** DAG-Math (arXiv:2510.19842) uses directed acyclic graphs to model the logical structure of Chain-of-Thought reasoning trajectories, measuring \"logical closeness\" of derivation paths. This is orthogonal to our use: we model skill prerequisite relationships to guide data synthesis, not reasoning path structure.\n\n**Gap summary.** No published method combines explicit coverage-gap identification over a skill-prerequisite DAG with targeted compositional synthesis, formal verification, and evaluation on a benchmark that isolates compositional generalization.\n\n## Proposed Approach: SkillDAG-Synth\n\n### Step 1: Skill-Prerequisite DAG Construction (Hierarchical Design)\n\n- **Coarse layer:** Extract OMEGA's 40 programmatic template generators as top-level skill categories spanning arithmetic, algebra, combinatorics, number theory, geometry, and logic/puzzles. Encode prerequisite relationships (e.g., GCD computation is prerequisite for modular arithmetic) as directed edges, forming a well-defined DAG.\n- **Fine layer (supplementary):** Map each OMEGA template category to MASS's co-occurrence skill graph clusters via embedding similarity, obtaining intra-category co-occurrence patterns for enriching within-pair diversity during synthesis.\n\n### Step 2: Coverage-Gap Identification\n\nCompute a 40×40 compositional coverage matrix over existing training corpora, where entry (i,j) counts co-occurrence of skills i and j in the same training problem. Identify DAG-connected skill pairs with zero or near-zero coverage. Note: while the coarse-layer matrix is 40×40, each template contains parameterized sub-dimensions (difficulty levels, sub-types, parameter ranges), so the effective compositional space is substantially larger than C(40,2)=780.\n\n**Pilot coverage analysis (pre-experiment, also a diagnostic contribution):** Compute the actual coverage matrix on OMEGA's training set and report: (a) number of zero-coverage DAG-connected pairs; (b) distribution of low-coverage pairs (bottom 10th percentile); (c) coverage patterns — whether cross-domain pairs (e.g., geometry×number_theory) are systematically under-covered vs. within-domain pairs; (d) relationship between prerequisite chain depth and coverage sparsity. If zero-coverage pairs are scarce, adjust targeting threshold to low-coverage. This analysis also characterizes the compositional coverage landscape of existing math training data, providing reusable diagnostic insights.\n\n### Step 3: Gap-Filling Synthesis with Verification\n\nFor each identified gap, synthesize multi-skill problems via constrained LLM generation (GPT-4o-mini) with OMEGA's symbolic solution verifiers ensuring correctness. MASS fine-grained co-occurrence patterns inform within-pair difficulty and diversity sampling.\n\n**Verification coverage analysis:** In pilot study, catalog OMEGA's 40 templates' verifier types (symbolic/numerical/graphical) and assess which skill-pair combinations can be verified via final-answer equivalence checking (e.g., SymPy). Report verification coverage rate (proportion of target pairs with automatic verification). For pairs without automatic verification, apply LLM-as-judge with human spot-check calibration.\n\n### Step 4: Fine-Tuning and Evaluation\n\nFine-tune DeepSeek-R1-Distill-Qwen3-8B (8B) and Qwen3-32B on coverage-targeted data via QLoRA.\n\n## Experimental Design\n\n### Baselines (all on the same base model for fair comparison)\n\n- **Vanilla SFT:** SFT on OMEGA's original 1K single-skill training problems, no synthetic data — isolates the effect of compositional augmentation from training paradigm\n- **GRPO (re-run):** GRPO on the same base model (DeepSeek-R1-Distill-Qwen3-8B) using OMEGA's training protocol — ensures base model consistency with SFT experiments\n- **Random-synthesis:** Random skill-pair selection with equal total samples — the critical H2 control\n- **STAT-Syn:** STAT's synthesis pipeline (arXiv:2510.10023) applied to OMEGA skills — representing atomic-skill remediation\n- **MathFusion:** Three fusion strategies (arXiv:2503.16212) applied to OMEGA training problems — representing coverage-agnostic composition\n- **STEPS-adapted (P2):** STEPS entropy-based selection (arXiv:2601.03676) applied to OMEGA's skill taxonomy — closest concurrent approach; implementation details and any adaptation limitations explicitly documented; labeled \"best-effort adaptation\"\n- **Agentic Proposing (reference, P2):** Using publicly available data/code (arXiv:2602.03279) as a difficulty-optimized composition reference point\n\n### Compute Normalization\n\nAll synthesis methods produce a fixed number of training samples. Data scales: **5K, 25K, 50K** — the 5K point is designed to maximize discriminative power for H2 (at low budgets, targeted coverage should show clearest advantage over random). Data efficiency curves (performance vs. #samples) are reported for all methods.\n\n### Evaluation\n\n- **Primary:** OMEGA compositional axis (main claim)\n- **Regression check:** OMEGA exploratory + transformative axes (confirm no degradation)\n- **Transfer benchmarks:** MATH-500, GSM8K, AIME24/25\n- **Per-skill-pair breakdown:** (a) OMEGA compositional test results grouped by skill-pair; (b) targeted vs. non-targeted pairs compared for improvement magnitude; (c) scatter plot of original coverage (from coverage matrix) vs. performance change; (d) comparison of random-synthesis vs. DAG-guided coverage of the same pairs. This is the primary mechanistic evidence for H2.\n- **Exploratory:** Correlation between prerequisite chain depth in DAG and compositional difficulty (base model failure rate), testing whether DAG structure predicts difficulty patterns.\n\n### Ablation Studies\n\n- **(A1) Graph structure:** DAG-guided → random graph → no graph (random pair selection), fixed data budget — tests H2+ (whether prerequisite structure specifically matters)\n- **(A2) Coverage strategy:** Gap-based targeting → entropy-based (STEPS-style) → uniform sampling — isolates coverage optimization value\n- **(A3) Verification (P1):** With symbolic verification → without — quantifies verification filtering impact\n- **(A4) Graph source (P2):** OMEGA DAG + MASS co-occurrence → OMEGA-only → MASS-only — validates fusion value\n\n### Synthesis Quality Analysis\n\n- Generation pass rate (candidates vs. passing symbolic verification)\n- Compositional fidelity: LLM judge or rule-based checker verifying target skill-pair presence (vs. degeneration to single-skill)\n- Verification coverage rate: proportion of target pairs with automatic verification capability\n- Difficulty distribution via base model pass@1\n- Human spot-check on 50–100 samples\n\n### Statistical Rigor\n\n- 8B model: 3 runs with different random seeds, report mean ± std\n- 32B model: 2 runs minimum\n- Paired significance tests (bootstrap or McNemar) on H2 comparisons\n\n### Compute Priority Tiering\n\n- **P0 (core):** Proposed + Random-synthesis + GRPO + Vanilla SFT, on 8B, 3 seeds, at 5K and 25K scales. Per-pair breakdown. Pilot coverage + verification coverage analysis.\n- **P1 (strong baselines + key ablations):** MathFusion + STAT-Syn baselines. A1 + A2 ablations on 8B at 25K. DAG-Synth + GRPO combination (testing SFT-RL complementarity, following STAT's demonstrated paradigm). OMEGA full 3-axis + transfer benchmarks. A3 ablation. 50K data scale for all P0 methods.\n- **P2 (extensions):** STEPS-adapted + Agentic Proposing baselines. A4 ablation. 32B experiments (proposed + random + GRPO at 25K). AIME24/25.\n\n### SFT-RL Complementarity\n\nFollowing STAT's finding that SFT and GRPO are complementary, we test a sequential \"DAG-Synth SFT → GRPO\" pipeline as a P1 experiment. Training FLOPs for all methods are reported for compute-normalized discussion.\n\n## Scalability Note\n\nOMEGA's 40 templates serve as a controlled proof-of-concept platform with symbolic verification capability. The SkillDAG-Synth methodology is designed for larger skill ontologies: MASS's 46K-skill graph demonstrates that structured skill spaces at this scale exist, where exhaustive coverage becomes infeasible and targeted gap-filling becomes essential. The coverage-guided synthesis framework is transferable to domains with structured skill dependencies (code generation, scientific reasoning, agent tool-chain composition), though non-math instantiation is left to future work.\n\n## Key References\n\n- OMEGA: Can LLMs Reason Outside the Box in Math? (NeurIPS 2025, arXiv:2506.18880)\n- MASS: Mathematical Data Selection via Skill Graphs for Pretraining LLMs (ICML 2025, arXiv:2503.14917)\n- STAT: Skill-Targeted Adaptive Training (ICLR 2026, arXiv:2510.10023)\n- MathFusion: Enhancing Math Problem-solving via Instruction Fusion (ACL 2025, arXiv:2503.16212)\n- Scaling Can Lead to Compositional Generalization — Redhardt et al. (NeurIPS 2025 Spotlight, arXiv:2507.07207)\n- Characterizing Pattern Matching on Compositional Task Structures — Chang et al. (ICLR 2026, arXiv:2505.20278)\n- STEPS: Skill Taxonomy Guided Data Synthesis (arXiv:2601.03676, Jan 2026)\n- Agentic Proposing: Compositional Skill Synthesis (arXiv:2602.03279, Feb 2026)\n- MindLoom: Composing Thought Modes for Frontier-Level Reasoning Data Synthesis (arXiv:2605.21630, May 2026)\n- FLAMES: Improving LLM Math Reasoning via Fine-Grained Analysis of Data Synthesis (arXiv:2508.16514, Aug 2025)\n- DAG-Math: Graph-of-Thought Guided Mathematical Reasoning in LLMs (arXiv:2510.19842, Oct 2025)\n- CHIMERA: Compact Synthetic Data for Generalizable LLM Reasoning (arXiv:2603.00889, Mar 2026)\n- Less is More: Adaptive Coverage for Synthetic Training Data (arXiv:2504.14508, Apr 2025)"
}
```

---

### Runtime record

_source line 2 · 2026-05-29T12:26:02.145Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-29T12:26:02.145Z",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1"
}
```

---

## Round 1

60 recorded events

### User

_source line 3 · 2026-05-29T12:26:02.216Z_

# Skill-DAG-Guided Frontier Synthesis for Mathematical Compositional Generalization

## Core Problem

LLMs exhibit a persistent compositional ceiling in mathematical reasoning: OMEGA (NeurIPS 2025, arXiv:2506.18880) demonstrates that RL fine-tuning (GRPO) improves exploratory generalization by +38pp but fails to improve compositional performance — combining distinct skills such as GCD computation with polynomial factoring. This ceiling persists across model scales and training paradigms.

Two theoretical results establish that **coverage of the compositional task space** is the prerequisite for breaking this ceiling: Redhardt et al. (NeurIPS 2025 Spotlight, arXiv:2507.07207) prove that standard MLPs can approximate compositional task families with linear neuron scaling, provided the training distribution sufficiently covers the task space; Chang et al. (ICLR 2026, arXiv:2505.20278) formalize how pattern matching on compositional task structures requires coverage of functional equivalence classes. Empirically, FLAMES (arXiv:2508.16514) confirms that in math data synthesis, maintaining higher problem coverage matters more than filtering for reliable solutions only. CHIMERA (arXiv:2603.00889) shows that 9K problems covering 1,179 fine-grained topics across 8 disciplines can match frontier-level reasoning performance, demonstrating the power of compact but high-coverage data — though its coverage is over topic diversity, not compositional skill-pair structure.

These results tell us **that** coverage matters, but not **where** to cover. Current synthesis methods either ignore compositional structure entirely or optimize proxies (difficulty, entropy, scarcity) rather than directly targeting coverage gaps. This paper tests two linked hypotheses: (1) that compositional coverage causally enables generalization even without RL, and more sharply, (2) that **DAG-guided gap-filling of the compositional skill space is more sample-efficient than random broad coverage**.

## Hypothesis Structure

- **H1 (Coverage → Generalization):** Increasing coverage of skill compositions in training data causally improves compositional generalization, even without RL. This extends Redhardt et al.'s theoretical result to the empirical math reasoning setting.
- **H2 (Targeted > Random):** DAG-guided coverage-gap targeting achieves the same or better compositional gains with fewer training samples than random broad coverage of the skill-pair space. This is our primary novel contribution — tested by comparing coverage-guided synthesis against random-synthesis under fixed data budgets.
- **H2+ (Structure Provides Signal):** Prerequisite DAG structure specifically predicts where coverage gaps are most harmful — i.e., DAG-connected gap-filling outperforms arbitrary-graph-connected gap-filling. This mechanistic hypothesis is tested by ablation A1 (DAG vs. random graph vs. no graph). If confirmed, it establishes that skill dependencies causally constrain compositional learning; if not, H2 still holds as a coverage-targeting contribution.

## Research Landscape

**Coverage-agnostic composition methods.** MathFusion (ACL 2025, arXiv:2503.16212) fuses problems via sequential/parallel/conditional strategies (+18pp) without skill-graph guidance — compositions are random. Agentic Proposing (arXiv:2602.03279, Feb 2026) achieves 91.6% AIME25 via difficulty-adaptive multi-granularity composition but optimizes difficulty, not coverage. MindLoom (arXiv:2605.21630, May 2026) composes atomic thought modes with a scarcity reward to encourage rare combinations — conceptually related to our coverage gap identification, but uses implicit RL-driven scarcity signals rather than explicit DAG-guided gap targeting, and applies thought modes sequentially without prerequisite structure.

**Coverage-aware methods not applied to math composition.** STAT (ICLR 2026, arXiv:2510.10023) identifies atomic skill gaps via teacher-student profiling and synthesizes single-skill remediation — targeting individual skill deficiencies rather than skill combinations. STEPS (arXiv:2601.03676, Jan 2026) maximizes structural entropy over hierarchical skill taxonomies but validates only on instruction-following benchmarks (not math reasoning), uses flat taxonomy rather than prerequisite DAGs, and optimizes entropy rather than explicit coverage gaps. "Less is More" (arXiv:2504.14508) uses maximum coverage problem formulations for subset selection from existing synthetic data, demonstrating that coverage-based selection outperforms training on full datasets — but addresses data selection, not synthesis of missing compositions.

**Skill graphs for data operations.** MASS (ICML 2025, arXiv:2503.14917) builds a 46K-skill, 1.18M-edge co-occurrence graph for scoring and selecting existing pretraining data (50–70% token efficiency gains). Its adjacency matrix has not been repurposed to identify missing compositions — the unexploited move our work takes.

**DAG structures in math reasoning (disambiguation).** DAG-Math (arXiv:2510.19842) uses directed acyclic graphs to model the logical structure of Chain-of-Thought reasoning trajectories, measuring "logical closeness" of derivation paths. This is orthogonal to our use: we model skill prerequisite relationships to guide data synthesis, not reasoning path structure.

**Gap summary.** No published method combines explicit coverage-gap identification over a skill-prerequisite DAG with targeted compositional synthesis, formal verification, and evaluation on a benchmark that isolates compositional generalization.

## Proposed Approach: SkillDAG-Synth

### Step 1: Skill-Prerequisite DAG Construction (Hierarchical Design)

- **Coarse layer:** Extract OMEGA's 40 programmatic template generators as top-level skill categories spanning arithmetic, algebra, combinatorics, number theory, geometry, and logic/puzzles. Encode prerequisite relationships (e.g., GCD computation is prerequisite for modular arithmetic) as directed edges, forming a well-defined DAG.
- **Fine layer (supplementary):** Map each OMEGA template category to MASS's co-occurrence skill graph clusters via embedding similarity, obtaining intra-category co-occurrence patterns for enriching within-pair diversity during synthesis.

### Step 2: Coverage-Gap Identification

Compute a 40×40 compositional coverage matrix over existing training corpora, where entry (i,j) counts co-occurrence of skills i and j in the same training problem. Identify DAG-connected skill pairs with zero or near-zero coverage. Note: while the coarse-layer matrix is 40×40, each template contains parameterized sub-dimensions (difficulty levels, sub-types, parameter ranges), so the effective compositional space is substantially larger than C(40,2)=780.

**Pilot coverage analysis (pre-experiment, also a diagnostic contribution):** Compute the actual coverage matrix on OMEGA's training set and report: (a) number of zero-coverage DAG-connected pairs; (b) distribution of low-coverage pairs (bottom 10th percentile); (c) coverage patterns — whether cross-domain pairs (e.g., geometry×number_theory) are systematically under-covered vs. within-domain pairs; (d) relationship between prerequisite chain depth and coverage sparsity. If zero-coverage pairs are scarce, adjust targeting threshold to low-coverage. This analysis also characterizes the compositional coverage landscape of existing math training data, providing reusable diagnostic insights.

### Step 3: Gap-Filling Synthesis with Verification

For each identified gap, synthesize multi-skill problems via constrained LLM generation (GPT-4o-mini) with OMEGA's symbolic solution verifiers ensuring correctness. MASS fine-grained co-occurrence patterns inform within-pair difficulty and diversity sampling.

**Verification coverage analysis:** In pilot study, catalog OMEGA's 40 templates' verifier types (symbolic/numerical/graphical) and assess which skill-pair combinations can be verified via final-answer equivalence checking (e.g., SymPy). Report verification coverage rate (proportion of target pairs with automatic verification). For pairs without automatic verification, apply LLM-as-judge with human spot-check calibration.

### Step 4: Fine-Tuning and Evaluation

Fine-tune DeepSeek-R1-Distill-Qwen3-8B (8B) and Qwen3-32B on coverage-targeted data via QLoRA.

## Experimental Design

### Baselines (all on the same base model for fair comparison)

- **Vanilla SFT:** SFT on OMEGA's original 1K single-skill training problems, no synthetic data — isolates the effect of compositional augmentation from training paradigm
- **GRPO (re-run):** GRPO on the same base model (DeepSeek-R1-Distill-Qwen3-8B) using OMEGA's training protocol — ensures base model consistency with SFT experiments
- **Random-synthesis:** Random skill-pair selection with equal total samples — the critical H2 control
- **STAT-Syn:** STAT's synthesis pipeline (arXiv:2510.10023) applied to OMEGA skills — representing atomic-skill remediation
- **MathFusion:** Three fusion strategies (arXiv:2503.16212) applied to OMEGA training problems — representing coverage-agnostic composition
- **STEPS-adapted (P2):** STEPS entropy-based selection (arXiv:2601.03676) applied to OMEGA's skill taxonomy — closest concurrent approach; implementation details and any adaptation limitations explicitly documented; labeled "best-effort adaptation"
- **Agentic Proposing (reference, P2):** Using publicly available data/code (arXiv:2602.03279) as a difficulty-optimized composition reference point

### Compute Normalization

All synthesis methods produce a fixed number of training samples. Data scales: **5K, 25K, 50K** — the 5K point is designed to maximize discriminative power for H2 (at low budgets, targeted coverage should show clearest advantage over random). Data efficiency curves (performance vs. #samples) are reported for all methods.

### Evaluation

- **Primary:** OMEGA compositional axis (main claim)
- **Regression check:** OMEGA exploratory + transformative axes (confirm no degradation)
- **Transfer benchmarks:** MATH-500, GSM8K, AIME24/25
- **Per-skill-pair breakdown:** (a) OMEGA compositional test results grouped by skill-pair; (b) targeted vs. non-targeted pairs compared for improvement magnitude; (c) scatter plot of original coverage (from coverage matrix) vs. performance change; (d) comparison of random-synthesis vs. DAG-guided coverage of the same pairs. This is the primary mechanistic evidence for H2.
- **Exploratory:** Correlation between prerequisite chain depth in DAG and compositional difficulty (base model failure rate), testing whether DAG structure predicts difficulty patterns.

### Ablation Studies

- **(A1) Graph structure:** DAG-guided → random graph → no graph (random pair selection), fixed data budget — tests H2+ (whether prerequisite structure specifically matters)
- **(A2) Coverage strategy:** Gap-based targeting → entropy-based (STEPS-style) → uniform sampling — isolates coverage optimization value
- **(A3) Verification (P1):** With symbolic verification → without — quantifies verification filtering impact
- **(A4) Graph source (P2):** OMEGA DAG + MASS co-occurrence → OMEGA-only → MASS-only — validates fusion value

### Synthesis Quality Analysis

- Generation pass rate (candidates vs. passing symbolic verification)
- Compositional fidelity: LLM judge or rule-based checker verifying target skill-pair presence (vs. degeneration to single-skill)
- Verification coverage rate: proportion of target pairs with automatic verification capability
- Difficulty distribution via base model pass@1
- Human spot-check on 50–100 samples

### Statistical Rigor

- 8B model: 3 runs with different random seeds, report mean ± std
- 32B model: 2 runs minimum
- Paired significance tests (bootstrap or McNemar) on H2 comparisons

### Compute Priority Tiering

- **P0 (core):** Proposed + Random-synthesis + GRPO + Vanilla SFT, on 8B, 3 seeds, at 5K and 25K scales. Per-pair breakdown. Pilot coverage + verification coverage analysis.
- **P1 (strong baselines + key ablations):** MathFusion + STAT-Syn baselines. A1 + A2 ablations on 8B at 25K. DAG-Synth + GRPO combination (testing SFT-RL complementarity, following STAT's demonstrated paradigm). OMEGA full 3-axis + transfer benchmarks. A3 ablation. 50K data scale for all P0 methods.
- **P2 (extensions):** STEPS-adapted + Agentic Proposing baselines. A4 ablation. 32B experiments (proposed + random + GRPO at 25K). AIME24/25.

### SFT-RL Complementarity

Following STAT's finding that SFT and GRPO are complementary, we test a sequential "DAG-Synth SFT → GRPO" pipeline as a P1 experiment. Training FLOPs for all methods are reported for compute-normalized discussion.

## Scalability Note

OMEGA's 40 templates serve as a controlled proof-of-concept platform with symbolic verification capability. The SkillDAG-Synth methodology is designed for larger skill ontologies: MASS's 46K-skill graph demonstrates that structured skill spaces at this scale exist, where exhaustive coverage becomes infeasible and targeted gap-filling becomes essential. The coverage-guided synthesis framework is transferable to domains with structured skill dependencies (code generation, scientific reasoning, agent tool-chain composition), though non-math instantiation is left to future work.

## Key References

- OMEGA: Can LLMs Reason Outside the Box in Math? (NeurIPS 2025, arXiv:2506.18880)
- MASS: Mathematical Data Selection via Skill Graphs for Pretraining LLMs (ICML 2025, arXiv:2503.14917)
- STAT: Skill-Targeted Adaptive Training (ICLR 2026, arXiv:2510.10023)
- MathFusion: Enhancing Math Problem-solving via Instruction Fusion (ACL 2025, arXiv:2503.16212)
- Scaling Can Lead to Compositional Generalization — Redhardt et al. (NeurIPS 2025 Spotlight, arXiv:2507.07207)
- Characterizing Pattern Matching on Compositional Task Structures — Chang et al. (ICLR 2026, arXiv:2505.20278)
- STEPS: Skill Taxonomy Guided Data Synthesis (arXiv:2601.03676, Jan 2026)
- Agentic Proposing: Compositional Skill Synthesis (arXiv:2602.03279, Feb 2026)
- MindLoom: Composing Thought Modes for Frontier-Level Reasoning Data Synthesis (arXiv:2605.21630, May 2026)
- FLAMES: Improving LLM Math Reasoning via Fine-Grained Analysis of Data Synthesis (arXiv:2508.16514, Aug 2025)
- DAG-Math: Graph-of-Thought Guided Mathematical Reasoning in LLMs (arXiv:2510.19842, Oct 2025)
- CHIMERA: Compact Synthetic Data for Generalizable LLM Reasoning (arXiv:2603.00889, Mar 2026)
- Less is More: Adaptive Coverage for Synthetic Training Data (arXiv:2504.14508, Apr 2025)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "e367c23d-5456-4f70-a5b3-3d1f58831111",
  "type": "user",
  "uuid": "49477a69-da01-45d9-b5aa-2a5668c86ad3",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-29T12:26:02.215Z_

```json
{
  "parentUuid": "49477a69-da01-45d9-b5aa-2a5668c86ad3",
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
  "uuid": "2ecd3f1a-a049-481b-88e8-3754b7ca4333",
  "timestamp": "2026-05-29T12:26:02.215Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-29T12:26:02.215Z_

```json
{
  "parentUuid": "2ecd3f1a-a049-481b-88e8-3754b7ca4333",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "564b77b9-0e78-4933-83d7-f761593fff92",
  "timestamp": "2026-05-29T12:26:02.215Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1",
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
  "lastPrompt": "# Skill-DAG-Guided Frontier Synthesis for Mathematical Compositional Generalization  ## Core Problem  LLMs exhibit a persistent compositional ceiling in mathematical reasoning: OMEGA (NeurIPS 2025, ar…",
  "leafUuid": "564b77b9-0e78-4933-83d7-f761593fff92",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Skill-DAG-guided synthesis for math compositional generalization",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1"
}
```

---

### Assistant

_source line 8 · 2026-05-29T12:26:10.119Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully analyze this proposal as the "发掘 agent" (Discovery Agent). I need to first do thorough literature research before making any suggestions. Let me read the proposal carefully and then conduct targeted searches.

The proposal is about "Skill-DAG-Guided Frontier Synthesis for Mathematical Compositional Generalization" - essentially using a skill prerequisite DAG to identify coverage gaps in compositional skill pairs and synthesize targeted training data to improve LLMs' compositional math reasoning.

Let me first understand the core claims:
1. H1: Coverage of skill compositions causally enables compositional generalization


2. H2: DAG-guided gap-filling is more sample-efficient than random broad coverage
3. H2+: DAG structure specifically predicts where coverage gaps are most harmful

Now I need to search for the most relevant recent work to assess novelty and significance.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "564b77b9-0e78-4933-83d7-f761593fff92",
  "isSidechain": false,
  "requestId": "req_011CbWrfHrdcRxkve1VZ9Cbw",
  "type": "assistant",
  "uuid": "1551ed2f-8ee6-42bb-9124-5cd8a3e5803b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014umU5Uu9iC5XMhwk7yG5Zx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5087,
      "cache_read_input_tokens": 14184,
      "output_tokens": 313,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5087,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 313,
          "cache_read_input_tokens": 14184,
          "cache_creation_input_tokens": 5087,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5087
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

_source line 9 · 2026-05-29T12:26:11.040Z_

I'll start by reading the proposal carefully and then conducting thorough literature searches before making any assessments. Let me do the prerequisite research first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1551ed2f-8ee6-42bb-9124-5cd8a3e5803b",
  "isSidechain": false,
  "requestId": "req_011CbWrfHrdcRxkve1VZ9Cbw",
  "type": "assistant",
  "uuid": "1edc386a-0a50-4d47-89c5-5a17efafbc2d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014umU5Uu9iC5XMhwk7yG5Zx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5087,
      "cache_read_input_tokens": 14184,
      "output_tokens": 313,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5087,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 313,
          "cache_read_input_tokens": 14184,
          "cache_creation_input_tokens": 5087,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5087
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

_source line 10 · 2026-05-29T12:26:11.204Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_014CTDtfhtuxwkGRd1apVj8T`</summary>

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
  "parentUuid": "1edc386a-0a50-4d47-89c5-5a17efafbc2d",
  "isSidechain": false,
  "requestId": "req_011CbWrfHrdcRxkve1VZ9Cbw",
  "type": "assistant",
  "uuid": "516ce2db-764e-4b9b-bba1-6a3fb4363490",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014umU5Uu9iC5XMhwk7yG5Zx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5087,
      "cache_read_input_tokens": 14184,
      "output_tokens": 313,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5087,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 313,
          "cache_read_input_tokens": 14184,
          "cache_creation_input_tokens": 5087,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5087
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

_source line 11 · 2026-05-29T12:26:11.211Z_

<details><summary>↩ Tool result · `toolu_014CTDtfhtuxwkGRd1apVj8T`</summary>

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
  "parentUuid": "516ce2db-764e-4b9b-bba1-6a3fb4363490",
  "isSidechain": false,
  "promptId": "e367c23d-5456-4f70-a5b3-3d1f58831111",
  "type": "user",
  "uuid": "5372a620-a4f9-4c25-80d7-1c39704fed3b",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "516ce2db-764e-4b9b-bba1-6a3fb4363490",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-29T12:26:13.430Z_

Now let me conduct my prerequisite research. I'll run multiple searches in parallel to cover different angles of the proposal.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5372a620-a4f9-4c25-80d7-1c39704fed3b",
  "isSidechain": false,
  "requestId": "req_011CbWrfxWKjeSgUaQtH8wf4",
  "type": "assistant",
  "uuid": "fdde269d-f0d8-4bfc-b3af-631ffd030034",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CbzU4HNtNHcTtFPxnAa1JG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 841,
      "cache_read_input_tokens": 19271,
      "output_tokens": 95,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 841,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 95,
          "cache_read_input_tokens": 19271,
          "cache_creation_input_tokens": 841,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 841
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

_source line 13 · 2026-05-29T12:26:14.054Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AQPUFtbcj9usSySkFjoeUj`</summary>

```json
{
  "query": "compositional generalization mathematical reasoning LLM 2025 2026 skill coverage"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fdde269d-f0d8-4bfc-b3af-631ffd030034",
  "isSidechain": false,
  "requestId": "req_011CbWrfxWKjeSgUaQtH8wf4",
  "type": "assistant",
  "uuid": "c9babca1-547f-43e7-92f9-597336abce4f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CbzU4HNtNHcTtFPxnAa1JG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 841,
      "cache_read_input_tokens": 19271,
      "output_tokens": 95,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 841,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 95,
          "cache_read_input_tokens": 19271,
          "cache_creation_input_tokens": 841,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 841
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

_source line 14 · 2026-05-29T12:26:21.643Z_

<details><summary>↩ Tool result · `toolu_01AQPUFtbcj9usSySkFjoeUj`</summary>

```text
Web search results for query: "compositional generalization mathematical reasoning LLM 2025 2026 skill coverage"

Links: [{"title":"Iterative In-Context Learning to Enhance LLMs Abstract Reasoning: The Case-Study of Algebraic Tasks","url":"https://arxiv.org/html/2509.01267"},{"title":"Out-of-distribution generalization via composition: A lens through induction heads in Transformers - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11831214/"},{"title":"Exploring the Compositional Deficiency of Large Language Models in   Mathematical Reasoning","url":"https://arxiv.org/pdf/2405.06680"},{"title":"The Mystery of Compositional Generalization in Graph-based Generative   Commonsense Reasoning","url":"https://arxiv.org/pdf/2410.06272"},{"title":"Out-of-distribution generalization via composition: A lens through induction heads in Transformers | PNAS","url":"https://www.pnas.org/doi/10.1073/pnas.2417182122"},{"title":"Mathematical Reasoning in Large Language Models: Benchmarks, Architectures, Evaluation, and Open Challenges","url":"https://arxiv.org/html/2605.19723v1"},{"title":"Accepted Findings Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/find_papers/"}]

Based on the search results, here's what I found regarding compositional generalization in mathematical reasoning for LLMs in 2025-2026:

## Key Findings

**Compositional Generalization Challenges:**
LLMs perform well when test data resembles training examples but fail to generalize to patterns beyond their observed data, highlighting inherent limitations of LLMs in compositional tasks and extrapolating beyond training data. Systematic compositionality remains an open challenge for current LLMs.

**Recent Research Developments:**

A few-shot in-context learning methodology aims to improve generalization capabilities of LLMs in solving algorithmic tasks by iteratively querying LLMs and adding wrongly computed examples to prompts, employing approaches like chain-of-thoughts.

Research has investigated the compositional generalization of LLMs on mathematical reasoning and demonstrated their stark underperformance compared to humans. The human-like 'slow thinking' demonstrated by OpenAI's o1 helps improve the compositionality of LLMs.

**Out-of-Distribution Generalization:**
While LLMs appear to solve certain novel tasks with appropriately formatted prompts through out-of-distribution generalization, the underlying mechanisms remain poorly understood.

**Future Directions:**
Future research should prioritize human-curated datasets that capture diverse reasoning strategies and explicitly test out-of-distribution generalization, emphasizing complex multi-step reasoning processes that cannot be easily memorized.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c9babca1-547f-43e7-92f9-597336abce4f",
  "isSidechain": false,
  "promptId": "e367c23d-5456-4f70-a5b3-3d1f58831111",
  "type": "user",
  "uuid": "37e592ce-2807-4a51-aa0c-efb3d95dd2fb",
  "toolUseResult": {
    "query": "compositional generalization mathematical reasoning LLM 2025 2026 skill coverage",
    "results": [
      {
        "tool_use_id": "srvtoolu_01B5quYNTNQpJ3b7Sah27HvT",
        "content": [
          {
            "title": "Iterative In-Context Learning to Enhance LLMs Abstract Reasoning: The Case-Study of Algebraic Tasks",
            "url": "https://arxiv.org/html/2509.01267"
          },
          {
            "title": "Out-of-distribution generalization via composition: A lens through induction heads in Transformers - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11831214/"
          },
          {
            "title": "Exploring the Compositional Deficiency of Large Language Models in   Mathematical Reasoning",
            "url": "https://arxiv.org/pdf/2405.06680"
          },
          {
            "title": "The Mystery of Compositional Generalization in Graph-based Generative   Commonsense Reasoning",
            "url": "https://arxiv.org/pdf/2410.06272"
          },
          {
            "title": "Out-of-distribution generalization via composition: A lens through induction heads in Transformers | PNAS",
            "url": "https://www.pnas.org/doi/10.1073/pnas.2417182122"
          },
          {
            "title": "Mathematical Reasoning in Large Language Models: Benchmarks, Architectures, Evaluation, and Open Challenges",
            "url": "https://arxiv.org/html/2605.19723v1"
          },
          {
            "title": "Accepted Findings Papers - EMNLP 2025",
            "url": "https://2025.emnlp.org/program/find_papers/"
          }
        ]
      },
      "Based on the search results, here's what I found regarding compositional generalization in mathematical reasoning for LLMs in 2025-2026:\n\n## Key Findings\n\n**Compositional Generalization Challenges:**\nLLMs perform well when test data resembles training examples but fail to generalize to patterns beyond their observed data, highlighting inherent limitations of LLMs in compositional tasks and extrapolating beyond training data. Systematic compositionality remains an open challenge for current LLMs.\n\n**Recent Research Developments:**\n\nA few-shot in-context learning methodology aims to improve generalization capabilities of LLMs in solving algorithmic tasks by iteratively querying LLMs and adding wrongly computed examples to prompts, employing approaches like chain-of-thoughts.\n\nResearch has investigated the compositional generalization of LLMs on mathematical reasoning and demonstrated their stark underperformance compared to humans. The human-like 'slow thinking' demonstrated by OpenAI's o1 helps improve the compositionality of LLMs.\n\n**Out-of-Distribution Generalization:**\nWhile LLMs appear to solve certain novel tasks with appropriately formatted prompts through out-of-distribution generalization, the underlying mechanisms remain poorly understood.\n\n**Future Directions:**\nFuture research should prioritize human-curated datasets that capture diverse reasoning strategies and explicitly test out-of-distribution generalization, emphasizing complex multi-step reasoning processes that cannot be easily memorized."
    ],
    "durationSeconds": 7.5817181640000015,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c9babca1-547f-43e7-92f9-597336abce4f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-29T12:26:24.372Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017HPXA9FpwGwUj2UbZgNsj7`</summary>

```json
{
  "query": "OMEGA benchmark NeurIPS 2025 arXiv 2506.18880 compositional math reasoning GRPO"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37e592ce-2807-4a51-aa0c-efb3d95dd2fb",
  "isSidechain": false,
  "requestId": "req_011CbWrgirKhXNr1PQ85C58b",
  "type": "assistant",
  "uuid": "52865d38-6ebb-465e-a99d-408c5db46ae0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WUzv9t6WJRSK7EV7VfFeyh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 800,
      "cache_read_input_tokens": 20112,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 800,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 20112,
          "cache_creation_input_tokens": 800,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 800
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

_source line 16 · 2026-05-29T12:26:31.540Z_

<details><summary>↩ Tool result · `toolu_017HPXA9FpwGwUj2UbZgNsj7`</summary>

```text
Web search results for query: "OMEGA benchmark NeurIPS 2025 arXiv 2506.18880 compositional math reasoning GRPO"

Links: [{"title":"OMEGA: LLMs in Math Reasoning","url":"https://www.emergentmind.com/papers/2506.18880"},{"title":"[2506.18880] OMEGA: Can LLMs Reason Outside the Box in Math? Evaluating Exploratory, Compositional, and Transformative Generalization","url":"https://arxiv.org/abs/2506.18880"},{"title":"Transform-Augmented GRPO Improves Pass@k","url":"https://arxiv.org/pdf/2601.22478"},{"title":"Prompt Augmentation Scales up GRPO Training on Mathematical Reasoning","url":"https://arxiv.org/pdf/2602.03190"},{"title":"GRPO and Reflection Reward for Mathematical Reasoning in Large Language Models","url":"https://arxiv.org/pdf/2603.14041"},{"title":"GRPO-LEAD: A Difficulty-Aware Reinforcement Learning Approach for Concise Mathematical Reasoning in Language Models","url":"https://arxiv.org/pdf/2504.09696"},{"title":"DRA-GRPO: Your GRPO Needs to Know Diverse Reasoning Paths for Mathematical Reasoning","url":"https://arxiv.org/pdf/2505.09655"}]

Based on the search results, here's what I found about the OMEGA benchmark and related work:

## OMEGA Benchmark Overview

OMEGA (Out-of-distribution Math Problems Evaluation with 3 Generalization Axes) is a controlled yet diverse benchmark designed to evaluate three axes of out-of-distribution generalization: (1) Exploratory—applying known problem solving skills to more complex instances within the same problem domain; (2) Compositional—combining distinct reasoning skills, previously learned in isolation, to solve novel problems that require integrating these skills in new and coherent ways; and (3) Transformative—adopting novel, often unconventional strategies.

## Key Findings

The OMEGA benchmark provides a systematic framework for evaluating the out-of-distribution (OOD) generalization capabilities of LLMs in mathematical reasoning. 

Fine-tuning of the Qwen-series models across all generalization settings shows notable improvements in exploratory generalization, while compositional generalization remains limited and transformative reasoning shows little to no improvement. Empirical findings reveal sharp accuracy declines with complexity and limited reinforcement learning gains on compositional and transformative generalization tasks.

## Connection to GRPO

The search results also contain several papers discussing GRPO (Group Relative Policy Optimization) as a reinforcement learning approach for mathematical reasoning, including variants and improvements to the method. However, the specific connection between OMEGA and GRPO in the arXiv paper 2506.18880 is not detailed in these results. You can access the full paper at https://arxiv.org/abs/2506.18880 for more complete information about how GRPO was used in the OMEGA research.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "52865d38-6ebb-465e-a99d-408c5db46ae0",
  "isSidechain": false,
  "promptId": "e367c23d-5456-4f70-a5b3-3d1f58831111",
  "type": "user",
  "uuid": "3c4eda74-906d-4b63-9903-2942e956d0a0",
  "toolUseResult": {
    "query": "OMEGA benchmark NeurIPS 2025 arXiv 2506.18880 compositional math reasoning GRPO",
    "results": [
      {
        "tool_use_id": "srvtoolu_018t28HTSchKzdX9kbrYa31M",
        "content": [
          {
            "title": "OMEGA: LLMs in Math Reasoning",
            "url": "https://www.emergentmind.com/papers/2506.18880"
          },
          {
            "title": "[2506.18880] OMEGA: Can LLMs Reason Outside the Box in Math? Evaluating Exploratory, Compositional, and Transformative Generalization",
            "url": "https://arxiv.org/abs/2506.18880"
          },
          {
            "title": "Transform-Augmented GRPO Improves Pass@k",
            "url": "https://arxiv.org/pdf/2601.22478"
          },
          {
            "title": "Prompt Augmentation Scales up GRPO Training on Mathematical Reasoning",
            "url": "https://arxiv.org/pdf/2602.03190"
          },
          {
            "title": "GRPO and Reflection Reward for Mathematical Reasoning in Large Language Models",
            "url": "https://arxiv.org/pdf/2603.14041"
          },
          {
            "title": "GRPO-LEAD: A Difficulty-Aware Reinforcement Learning Approach for Concise Mathematical Reasoning in Language Models",
            "url": "https://arxiv.org/pdf/2504.09696"
          },
          {
            "title": "DRA-GRPO: Your GRPO Needs to Know Diverse Reasoning Paths for Mathematical Reasoning",
            "url": "https://arxiv.org/pdf/2505.09655"
          }
        ]
      },
      "Based on the search results, here's what I found about the OMEGA benchmark and related work:\n\n## OMEGA Benchmark Overview\n\nOMEGA (Out-of-distribution Math Problems Evaluation with 3 Generalization Axes) is a controlled yet diverse benchmark designed to evaluate three axes of out-of-distribution generalization: (1) Exploratory—applying known problem solving skills to more complex instances within the same problem domain; (2) Compositional—combining distinct reasoning skills, previously learned in isolation, to solve novel problems that require integrating these skills in new and coherent ways; and (3) Transformative—adopting novel, often unconventional strategies.\n\n## Key Findings\n\nThe OMEGA benchmark provides a systematic framework for evaluating the out-of-distribution (OOD) generalization capabilities of LLMs in mathematical reasoning. \n\nFine-tuning of the Qwen-series models across all generalization settings shows notable improvements in exploratory generalization, while compositional generalization remains limited and transformative reasoning shows little to no improvement. Empirical findings reveal sharp accuracy declines with complexity and limited reinforcement learning gains on compositional and transformative generalization tasks.\n\n## Connection to GRPO\n\nThe search results also contain several papers discussing GRPO (Group Relative Policy Optimization) as a reinforcement learning approach for mathematical reasoning, including variants and improvements to the method. However, the specific connection between OMEGA and GRPO in the arXiv paper 2506.18880 is not detailed in these results. You can access the full paper at https://arxiv.org/abs/2506.18880 for more complete information about how GRPO was used in the OMEGA research."
    ],
    "durationSeconds": 7.163927595000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "52865d38-6ebb-465e-a99d-408c5db46ae0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-29T12:26:33.894Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01U7KFqUyQcGt12H1MVdqBpb`</summary>

```json
{
  "query": "MindLoom arXiv 2605.21630 thought modes reasoning data synthesis scarcity reward 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c4eda74-906d-4b63-9903-2942e956d0a0",
  "isSidechain": false,
  "requestId": "req_011CbWrhTFythDQv4aQ6Mtty",
  "type": "assistant",
  "uuid": "fd392f0b-60a3-4bef-beb9-d683f3abea5b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012v2Fd7AfuNGDuvABtpGRjb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 826,
      "cache_read_input_tokens": 20912,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 826,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 20912,
          "cache_creation_input_tokens": 826,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 826
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

_source line 18 · 2026-05-29T12:26:39.906Z_

<details><summary>↩ Tool result · `toolu_01U7KFqUyQcGt12H1MVdqBpb`</summary>

```text
Web search results for query: "MindLoom arXiv 2605.21630 thought modes reasoning data synthesis scarcity reward 2026"

Links: [{"title":"[2605.21630] MindLoom: Composing Thought Modes for Frontier-Level Reasoning Data Synthesis","url":"https://arxiv.org/abs/2605.21630"},{"title":"MindLoom: Composing Thought Modes for Frontier-Level Reasoning Data Synthesis","url":"https://arxiv.org/html/2605.21630"},{"title":"Long Grounded Thoughts: Synthesizing Visual Problems and Reasoning Chains at Scale","url":"https://arxiv.org/pdf/2511.05705"},{"title":"ImageNet-Think-250K: A Large-Scale Synthetic Dataset for Multimodal Reasoning for Vision Language Models","url":"https://arxiv.org/pdf/2510.01582"},{"title":"AgentFrontier: Expanding the Capability Frontier of LLM Agents with ZPD-Guided Data Synthesis","url":"https://arxiv.org/pdf/2510.24695"}]

Based on the search results, here's what I found about MindLoom (arXiv 2605.21630):

## Overview

MindLoom is a framework for synthesizing frontier-level reasoning data through compositional thought mode engineering. The paper was submitted on May 20, 2026 and is authored by researchers from Peking University and Tsinghua University.

## Key Problem and Approach

Although LLMs have made substantial progress in reasoning, systematically producing frontier-level reasoning data remains difficult, with existing synthesis methods often having limited visibility into the structural factors that govern problem difficulty.

The work views the difficulty of a reasoning problem as arising from the accumulation of atomic knowledge-reasoning transformations, which are termed thought modes.

## Methodology

Given a collection of hard problems with verified solutions, MindLoom decomposes those solutions into thought mode chains that reveal each problem's construction logic, and then trains a retrieval model that matches problem states to compatible thought modes.

The project materials are available at: https://github.com/EachSheep/MindLoom


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fd392f0b-60a3-4bef-beb9-d683f3abea5b",
  "isSidechain": false,
  "promptId": "e367c23d-5456-4f70-a5b3-3d1f58831111",
  "type": "user",
  "uuid": "e6aed3fa-816d-49ef-980a-f645803545c1",
  "toolUseResult": {
    "query": "MindLoom arXiv 2605.21630 thought modes reasoning data synthesis scarcity reward 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_012nHTyazzgMJ8MiKDN884yr",
        "content": [
          {
            "title": "[2605.21630] MindLoom: Composing Thought Modes for Frontier-Level Reasoning Data Synthesis",
            "url": "https://arxiv.org/abs/2605.21630"
          },
          {
            "title": "MindLoom: Composing Thought Modes for Frontier-Level Reasoning Data Synthesis",
            "url": "https://arxiv.org/html/2605.21630"
          },
          {
            "title": "Long Grounded Thoughts: Synthesizing Visual Problems and Reasoning Chains at Scale",
            "url": "https://arxiv.org/pdf/2511.05705"
          },
          {
            "title": "ImageNet-Think-250K: A Large-Scale Synthetic Dataset for Multimodal Reasoning for Vision Language Models",
            "url": "https://arxiv.org/pdf/2510.01582"
          },
          {
            "title": "AgentFrontier: Expanding the Capability Frontier of LLM Agents with ZPD-Guided Data Synthesis",
            "url": "https://arxiv.org/pdf/2510.24695"
          }
        ]
      },
      "Based on the search results, here's what I found about MindLoom (arXiv 2605.21630):\n\n## Overview\n\nMindLoom is a framework for synthesizing frontier-level reasoning data through compositional thought mode engineering. The paper was submitted on May 20, 2026 and is authored by researchers from Peking University and Tsinghua University.\n\n## Key Problem and Approach\n\nAlthough LLMs have made substantial progress in reasoning, systematically producing frontier-level reasoning data remains difficult, with existing synthesis methods often having limited visibility into the structural factors that govern problem difficulty.\n\nThe work views the difficulty of a reasoning problem as arising from the accumulation of atomic knowledge-reasoning transformations, which are termed thought modes.\n\n## Methodology\n\nGiven a collection of hard problems with verified solutions, MindLoom decomposes those solutions into thought mode chains that reveal each problem's construction logic, and then trains a retrieval model that matches problem states to compatible thought modes.\n\nThe project materials are available at: https://github.com/EachSheep/MindLoom"
    ],
    "durationSeconds": 6.007338574000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "fd392f0b-60a3-4bef-beb9-d683f3abea5b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-29T12:26:42.539Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GLyLTP3jiddBst3dtQnvMF`</summary>

```json
{
  "query": "STAT skill-targeted adaptive training arXiv 2510.10023 ICLR 2026 SFT GRPO complementary"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e6aed3fa-816d-49ef-980a-f645803545c1",
  "isSidechain": false,
  "requestId": "req_011CbWri4wq9BP2Bitv2HBhx",
  "type": "assistant",
  "uuid": "ba97f450-63f8-472b-ba19-18bc7a35385e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XDeCtdbNPcLTSujAucd3vV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 616,
      "cache_read_input_tokens": 21738,
      "output_tokens": 84,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 616,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 84,
          "cache_read_input_tokens": 21738,
          "cache_creation_input_tokens": 616,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 616
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

_source line 20 · 2026-05-29T12:26:49.833Z_

<details><summary>↩ Tool result · `toolu_01GLyLTP3jiddBst3dtQnvMF`</summary>

```text
Web search results for query: "STAT skill-targeted adaptive training arXiv 2510.10023 ICLR 2026 SFT GRPO complementary"

Links: [{"title":"[2510.10023] Skill-Targeted Adaptive Training","url":"https://arxiv.org/abs/2510.10023"},{"title":"ICLR Poster STAT: Skill-Targeted Adaptive Training","url":"https://iclr.cc/virtual/2026/poster/10007620"},{"title":"Skill-Targeted Adaptive Training","url":"https://arxiv.org/html/2510.10023"},{"title":"Preprint. Under review. Skill-Targeted Adaptive Training","url":"https://arxiv.org/pdf/2510.10023"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2601.21251"},{"title":"Enhancing Team Science by Training Collaborative Biostatisticians to have a Strong Statistical Voice","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12705724/"},{"title":"Machine Learning Oct 2025","url":"https://arxiv.org/list/cs.LG/2025-10?skip=1175&show=50"},{"title":"Method for training an adaptive statistical classifier with improved learning of difficult samples","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5805730"}]

Based on the search results, I found information about the paper you're looking for:

STAT (Skill-Targeted Adaptive Training) is a new fine-tuning strategy to train a student model by using the metacognition ability of a stronger large language model (LLM) as the teacher.

The teacher uses the task dataset to create a list of skills needed for the task and labels each data point with its required skills, then monitors the student's answers to create a Missing-Skill-Profile for the student, tracking how often they failed to apply each skill in their responses.

In STAT-Sel, the teacher uses an existing set of training examples but adaptively reweights them according to the Missing-Skill-Profile.

The paper (arXiv 2510.10023) has been accepted to ICLR 2026. The research focuses on addressing the problem that language models often show little to no improvement when trained via vanilla supervised fine-tuning (SFT) on data similar to what they saw in their training set.

The search results don't contain specific information about the relationship between STAT and GRPO, or details about how they are complementary, so I cannot provide details on that aspect from the available search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ba97f450-63f8-472b-ba19-18bc7a35385e",
  "isSidechain": false,
  "promptId": "e367c23d-5456-4f70-a5b3-3d1f58831111",
  "type": "user",
  "uuid": "0f6a0ae5-bc39-44cf-a15c-1988af61cd83",
  "toolUseResult": {
    "query": "STAT skill-targeted adaptive training arXiv 2510.10023 ICLR 2026 SFT GRPO complementary",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WhDL4zKYgJJEuS7iSZszkN",
        "content": [
          {
            "title": "[2510.10023] Skill-Targeted Adaptive Training",
            "url": "https://arxiv.org/abs/2510.10023"
          },
          {
            "title": "ICLR Poster STAT: Skill-Targeted Adaptive Training",
            "url": "https://iclr.cc/virtual/2026/poster/10007620"
          },
          {
            "title": "Skill-Targeted Adaptive Training",
            "url": "https://arxiv.org/html/2510.10023"
          },
          {
            "title": "Preprint. Under review. Skill-Targeted Adaptive Training",
            "url": "https://arxiv.org/pdf/2510.10023"
          },
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://arxiv.org/pdf/2601.21251"
          },
          {
            "title": "Enhancing Team Science by Training Collaborative Biostatisticians to have a Strong Statistical Voice",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12705724/"
          },
          {
            "title": "Machine Learning Oct 2025",
            "url": "https://arxiv.org/list/cs.LG/2025-10?skip=1175&show=50"
          },
          {
            "title": "Method for training an adaptive statistical classifier with improved learning of difficult samples",
            "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5805730"
          }
        ]
      },
      "Based on the search results, I found information about the paper you're looking for:\n\nSTAT (Skill-Targeted Adaptive Training) is a new fine-tuning strategy to train a student model by using the metacognition ability of a stronger large language model (LLM) as the teacher.\n\nThe teacher uses the task dataset to create a list of skills needed for the task and labels each data point with its required skills, then monitors the student's answers to create a Missing-Skill-Profile for the student, tracking how often they failed to apply each skill in their responses.\n\nIn STAT-Sel, the teacher uses an existing set of training examples but adaptively reweights them according to the Missing-Skill-Profile.\n\nThe paper (arXiv 2510.10023) has been accepted to ICLR 2026. The research focuses on addressing the problem that language models often show little to no improvement when trained via vanilla supervised fine-tuning (SFT) on data similar to what they saw in their training set.\n\nThe search results don't contain specific information about the relationship between STAT and GRPO, or details about how they are complementary, so I cannot provide details on that aspect from the available search results."
    ],
    "durationSeconds": 7.2902155809999964,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "ba97f450-63f8-472b-ba19-18bc7a35385e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1",
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
  "lastPrompt": "# Skill-DAG-Guided Frontier Synthesis for Mathematical Compositional Generalization  ## Core Problem  LLMs exhibit a persistent compositional ceiling in mathematical reasoning: OMEGA (NeurIPS 2025, ar…",
  "leafUuid": "0f6a0ae5-bc39-44cf-a15c-1988af61cd83",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Skill-DAG-guided synthesis for math compositional generalization",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1"
}
```

---

### Tool call

_source line 23 · 2026-05-29T12:26:52.051Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019GTMxyHqnqeZLkpjgzLs13`</summary>

```json
{
  "query": "MASS mathematical skill graph pretraining data selection ICML 2025 arXiv 2503.14917 coverage synthesis"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f6a0ae5-bc39-44cf-a15c-1988af61cd83",
  "isSidechain": false,
  "requestId": "req_011CbWrioLkKhiHH8Y8J31ME",
  "type": "assistant",
  "uuid": "db1543fa-c9a8-45c0-b96f-523ffef53dec",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GH6LhLfYguqYyy5LGRy5T8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 749,
      "cache_read_input_tokens": 22354,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 749,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 80,
          "cache_read_input_tokens": 22354,
          "cache_creation_input_tokens": 749,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 749
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

_source line 24 · 2026-05-29T12:26:57.864Z_

<details><summary>↩ Tool result · `toolu_019GTMxyHqnqeZLkpjgzLs13`</summary>

```text
Web search results for query: "MASS mathematical skill graph pretraining data selection ICML 2025 arXiv 2503.14917 coverage synthesis"

Links: [{"title":"ICML Poster MASS: Mathematical Data Selection via Skill Graphs for Pretraining Large Language Models","url":"https://icml.cc/virtual/2025/poster/45257"},{"title":"[2503.14917] MASS: Mathematical Data Selection via Skill Graphs for Pretraining Large Language Models","url":"https://arxiv.org/abs/2503.14917"},{"title":"MASS: Mathematical Data Selection via Skill Graphs for Pretraining Large Language Models | OpenReview","url":"https://openreview.net/forum?id=RvYO10B5ss&noteId=MnfKLTuWvA"},{"title":"[Literature Review] MASS: Mathematical Data Selection via Skill Graphs for Pretraining Large Language Models","url":"https://www.themoonlight.io/en/review/mass-mathematical-data-selection-via-skill-graphs-for-pretraining-large-language-models"},{"title":"MASS: MAthematical Data Selection via Skill Graphs for Pretraining Large Language Models","url":"https://arxiv.org/html/2503.14917"},{"title":"(PDF) MASS: Mathematical Data Selection via Skill Graphs for Pretraining Large Language Models","url":"https://www.researchgate.net/publication/390019391_MASS_Mathematical_Data_Selection_via_Skill_Graphs_for_Pretraining_Large_Language_Models"},{"title":"MASS: Mathematical Data Selection via Skill Graphs for ...","url":"https://arxiv.org/pdf/2503.14917"}]

I found the paper you're looking for! Here's what I found about MASS:

## Overview

MASS is a Mathematical data Selection framework using the Skill graph for pretraining LLMs in the mathematical reasoning domain. While most data selection methods focus on general data selection, they tend to overlook the specific nuances of domain-related data.

## Key Approach

The framework constructs a skill graph that captures the mathematical skills and their interrelations from a reference dataset, which guides the assignment of quality scores to the target dataset, enabling selection of the top-ranked subset used to pretrain LLMs.

## Results

The selected datasets achieve the same results as the original dataset, but with 43%-71% fewer trained tokens. The approach was tested on TinyLlama-1.1B and Mistral-7B using OpenWebMath, OpenWebMath-pro, and Jiuzhang3.0 datasets.

The paper (arXiv:2503.14917) was presented at ICML 2025 and represents a novel approach to improving LLM performance in mathematical reasoning through intelligent data selection based on skill graphs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "db1543fa-c9a8-45c0-b96f-523ffef53dec",
  "isSidechain": false,
  "promptId": "e367c23d-5456-4f70-a5b3-3d1f58831111",
  "type": "user",
  "uuid": "08df581d-11eb-46fd-903a-d9f59eb79194",
  "toolUseResult": {
    "query": "MASS mathematical skill graph pretraining data selection ICML 2025 arXiv 2503.14917 coverage synthesis",
    "results": [
      {
        "tool_use_id": "srvtoolu_011sLRLF4JNmBNeEoqT7XyXh",
        "content": [
          {
            "title": "ICML Poster MASS: Mathematical Data Selection via Skill Graphs for Pretraining Large Language Models",
            "url": "https://icml.cc/virtual/2025/poster/45257"
          },
          {
            "title": "[2503.14917] MASS: Mathematical Data Selection via Skill Graphs for Pretraining Large Language Models",
            "url": "https://arxiv.org/abs/2503.14917"
          },
          {
            "title": "MASS: Mathematical Data Selection via Skill Graphs for Pretraining Large Language Models | OpenReview",
            "url": "https://openreview.net/forum?id=RvYO10B5ss&noteId=MnfKLTuWvA"
          },
          {
            "title": "[Literature Review] MASS: Mathematical Data Selection via Skill Graphs for Pretraining Large Language Models",
            "url": "https://www.themoonlight.io/en/review/mass-mathematical-data-selection-via-skill-graphs-for-pretraining-large-language-models"
          },
          {
            "title": "MASS: MAthematical Data Selection via Skill Graphs for Pretraining Large Language Models",
            "url": "https://arxiv.org/html/2503.14917"
          },
          {
            "title": "(PDF) MASS: Mathematical Data Selection via Skill Graphs for Pretraining Large Language Models",
            "url": "https://www.researchgate.net/publication/390019391_MASS_Mathematical_Data_Selection_via_Skill_Graphs_for_Pretraining_Large_Language_Models"
          },
          {
            "title": "MASS: Mathematical Data Selection via Skill Graphs for ...",
            "url": "https://arxiv.org/pdf/2503.14917"
          }
        ]
      },
      "I found the paper you're looking for! Here's what I found about MASS:\n\n## Overview\n\nMASS is a Mathematical data Selection framework using the Skill graph for pretraining LLMs in the mathematical reasoning domain. While most data selection methods focus on general data selection, they tend to overlook the specific nuances of domain-related data.\n\n## Key Approach\n\nThe framework constructs a skill graph that captures the mathematical skills and their interrelations from a reference dataset, which guides the assignment of quality scores to the target dataset, enabling selection of the top-ranked subset used to pretrain LLMs.\n\n## Results\n\nThe selected datasets achieve the same results as the original dataset, but with 43%-71% fewer trained tokens. The approach was tested on TinyLlama-1.1B and Mistral-7B using OpenWebMath, OpenWebMath-pro, and Jiuzhang3.0 datasets.\n\nThe paper (arXiv:2503.14917) was presented at ICML 2025 and represents a novel approach to improving LLM performance in mathematical reasoning through intelligent data selection based on skill graphs."
    ],
    "durationSeconds": 5.808203061999993,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "db1543fa-c9a8-45c0-b96f-523ffef53dec",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-29T12:27:00.257Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Sjr2E5HPwZgi3rJu3TXSKb`</summary>

```json
{
  "query": "curriculum learning skill composition data synthesis math reasoning 2026 DAG prerequisite structure training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08df581d-11eb-46fd-903a-d9f59eb79194",
  "isSidechain": false,
  "requestId": "req_011CbWrjPmCTNpujsDVtyvFE",
  "type": "assistant",
  "uuid": "e5a794f3-f0d2-46d3-9fc8-726af52aa81a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hfpua8iJF7MPaCm3ZdLeFJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 785,
      "cache_read_input_tokens": 23103,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 785,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 23103,
          "cache_creation_input_tokens": 785,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 785
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

_source line 26 · 2026-05-29T12:27:06.645Z_

<details><summary>↩ Tool result · `toolu_01Sjr2E5HPwZgi3rJu3TXSKb`</summary>

```text
Web search results for query: "curriculum learning skill composition data synthesis math reasoning 2026 DAG prerequisite structure training"

Links: [{"title":"Introducing ReasonLite-0.6B: Curriculum Distillation for Lightweight High-Accuracy Math Reasoning","url":"https://www.amd.com/en/developer/resources/technical-articles/2026/introducing-reasonlite-0-6b.html"},{"title":"[2601.17006] MathMixup: Boosting LLM Mathematical Reasoning with Difficulty-Controllable Data Synthesis and Curriculum Learning","url":"https://arxiv.org/abs/2601.17006"},{"title":"MathMixup: Boosting LLM Mathematical Reasoning with Difficulty-Controllable Data Synthesis and Curriculum Learning","url":"https://arxiv.org/html/2601.17006"},{"title":"MathMixup: Boosting LLM Mathematical Reasoning with Difficulty-Controllable Data Synthesis and Curriculum Learning","url":"https://arxiv.org/pdf/2601.17006"},{"title":"Reasoning Curriculum: Bootstrapping Broad LLM Reasoning from Math","url":"https://arxiv.org/pdf/2510.26143"}]

I found several relevant results about curriculum learning, data synthesis, and math reasoning from 2026. Here's what I discovered:

## Key Research Findings

MathMixup is a novel data synthesis paradigm that systematically generates high-quality, difficulty-controllable mathematical reasoning problems through hybrid and decomposed strategies. Automated self-checking and manual screening are incorporated to ensure semantic clarity and a well-structured difficulty gradient in the synthesized data.

The curriculum learning framework exploits explicit difficulty gradation where synthesized questions are organized into several levels (decomposed, original, hybrid) according to their difficulty, and the model is trained progressively from easier to harder problems. This staged process enables the model to build foundational reasoning skills before tackling more complex concepts, providing a data-driven and controllable curriculum learning strategy.

## Performance Results

Fine-tuned Qwen2.5-7B achieves an average score of 52.6% across seven mathematical benchmarks, surpassing previous state-of-the-art methods.

## Additional Work

A powerful teacher model is leveraged to synthesize a large number of high-quality reasoning examples—an approach commonly referred to as data distillation.

The search results emphasize how curriculum learning strategies combined with difficulty-controllable data synthesis significantly improve LLM mathematical reasoning performance in 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e5a794f3-f0d2-46d3-9fc8-726af52aa81a",
  "isSidechain": false,
  "promptId": "e367c23d-5456-4f70-a5b3-3d1f58831111",
  "type": "user",
  "uuid": "cac1759c-cd2b-4b5a-8d0d-59e17fbc89ae",
  "toolUseResult": {
    "query": "curriculum learning skill composition data synthesis math reasoning 2026 DAG prerequisite structure training",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JHUufmKZFGKPwvXo3tAQhN",
        "content": [
          {
            "title": "Introducing ReasonLite-0.6B: Curriculum Distillation for Lightweight High-Accuracy Math Reasoning",
            "url": "https://www.amd.com/en/developer/resources/technical-articles/2026/introducing-reasonlite-0-6b.html"
          },
          {
            "title": "[2601.17006] MathMixup: Boosting LLM Mathematical Reasoning with Difficulty-Controllable Data Synthesis and Curriculum Learning",
            "url": "https://arxiv.org/abs/2601.17006"
          },
          {
            "title": "MathMixup: Boosting LLM Mathematical Reasoning with Difficulty-Controllable Data Synthesis and Curriculum Learning",
            "url": "https://arxiv.org/html/2601.17006"
          },
          {
            "title": "MathMixup: Boosting LLM Mathematical Reasoning with Difficulty-Controllable Data Synthesis and Curriculum Learning",
            "url": "https://arxiv.org/pdf/2601.17006"
          },
          {
            "title": "Reasoning Curriculum: Bootstrapping Broad LLM Reasoning from Math",
            "url": "https://arxiv.org/pdf/2510.26143"
          }
        ]
      },
      "I found several relevant results about curriculum learning, data synthesis, and math reasoning from 2026. Here's what I discovered:\n\n## Key Research Findings\n\nMathMixup is a novel data synthesis paradigm that systematically generates high-quality, difficulty-controllable mathematical reasoning problems through hybrid and decomposed strategies. Automated self-checking and manual screening are incorporated to ensure semantic clarity and a well-structured difficulty gradient in the synthesized data.\n\nThe curriculum learning framework exploits explicit difficulty gradation where synthesized questions are organized into several levels (decomposed, original, hybrid) according to their difficulty, and the model is trained progressively from easier to harder problems. This staged process enables the model to build foundational reasoning skills before tackling more complex concepts, providing a data-driven and controllable curriculum learning strategy.\n\n## Performance Results\n\nFine-tuned Qwen2.5-7B achieves an average score of 52.6% across seven mathematical benchmarks, surpassing previous state-of-the-art methods.\n\n## Additional Work\n\nA powerful teacher model is leveraged to synthesize a large number of high-quality reasoning examples—an approach commonly referred to as data distillation.\n\nThe search results emphasize how curriculum learning strategies combined with difficulty-controllable data synthesis significantly improve LLM mathematical reasoning performance in 2026."
    ],
    "durationSeconds": 6.383456699000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e5a794f3-f0d2-46d3-9fc8-726af52aa81a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-29T12:27:08.832Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QsHbR5KxNAuxPcZWf1YULx`</summary>

```json
{
  "query": "compositional skill pair coverage gap targeted data synthesis LLM training efficiency 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cac1759c-cd2b-4b5a-8d0d-59e17fbc89ae",
  "isSidechain": false,
  "requestId": "req_011CbWrk3Hfinyd1nXGYBax9",
  "type": "assistant",
  "uuid": "06db584b-5b3b-4b03-aaa8-2c066b193227",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015FdfpRE7ggDCQJQCfNDqG4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 684,
      "cache_read_input_tokens": 23888,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 684,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 23888,
          "cache_creation_input_tokens": 684,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 684
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

_source line 28 · 2026-05-29T12:27:18.235Z_

<details><summary>↩ Tool result · `toolu_01QsHbR5KxNAuxPcZWf1YULx`</summary>

```text
Web search results for query: "compositional skill pair coverage gap targeted data synthesis LLM training efficiency 2025 2026"

Links: [{"title":"Towards Compositional Generalization of LLMs via Skill Taxonomy Guided Data Synthesis","url":"https://arxiv.org/html/2601.03676"},{"title":"Towards Compositional Generalization of LLMs via Skill Taxonomy Guided Data Synthesis","url":"https://arxiv.org/pdf/2601.03676"},{"title":"GitHub - weiyifan1023/STEPS: Code and Data for Paper \"Towards Compositional Generalization of LLMs via Skill Taxonomy Guided Data Synthesis\"","url":"https://github.com/weiyifan1023/STEPS"},{"title":"[2601.03676] Towards Compositional Generalization of LLMs via Skill Taxonomy Guided Data Synthesis","url":"https://arxiv.org/abs/2601.03676"},{"title":"Towards a Theoretical Understanding of Synthetic Data in LLM Post-Training: A Reverse-Bottleneck Perspective","url":"https://arxiv.org/html/2410.01720v2"},{"title":"Compositional Skill Acquisition in LLMs","url":"https://www.emergentmind.com/topics/compositional-skill-acquisition-in-llms"}]

The search results reveal significant recent research (2025-2026) on compositional skill pair coverage gaps and targeted data synthesis for LLM training efficiency:

## Key Findings

LLMs and agent-based systems struggle with compositional generalization due to a data bottleneck where complex skill combinations follow a long-tailed, power-law distribution, limiting instruction-following performance and generalization in agent-centric tasks.

### STEPS Framework

STEPS is a Skill Taxonomy guided Entropy-based Post-training data Synthesis framework that addresses this by uncovering latent relationships among skills and organizing them into an interpretable, hierarchical skill taxonomy using structural information theory. The framework formulates data synthesis as a constrained information maximization problem, selecting skill combinations that maximize marginal structural information within the hierarchy while preserving semantic coherence.

### Training Efficiency Improvements

Recent efforts utilize data synthesis via stochastic skill pairing to bridge compositional data gaps, though heuristic methods often ignore latent hierarchical dependencies, which may result in semantically incoherent compositions and inefficient exploration of the combinatorial space.

### Performance Impact

Experiments on challenging instruction-following benchmarks show that STEPS outperforms existing data synthesis baselines, while also yielding improved compositional generalization in downstream agent-based evaluations.

These advances represent a systematic shift from random skill pairing to theoretically-grounded approaches that target specific compositional coverage gaps.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "06db584b-5b3b-4b03-aaa8-2c066b193227",
  "isSidechain": false,
  "promptId": "e367c23d-5456-4f70-a5b3-3d1f58831111",
  "type": "user",
  "uuid": "578a2690-42ef-401c-bf79-32f13e41beb0",
  "toolUseResult": {
    "query": "compositional skill pair coverage gap targeted data synthesis LLM training efficiency 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_013Ko9BMMtCTPZwsEH4UggtK",
        "content": [
          {
            "title": "Towards Compositional Generalization of LLMs via Skill Taxonomy Guided Data Synthesis",
            "url": "https://arxiv.org/html/2601.03676"
          },
          {
            "title": "Towards Compositional Generalization of LLMs via Skill Taxonomy Guided Data Synthesis",
            "url": "https://arxiv.org/pdf/2601.03676"
          },
          {
            "title": "GitHub - weiyifan1023/STEPS: Code and Data for Paper \"Towards Compositional Generalization of LLMs via Skill Taxonomy Guided Data Synthesis\"",
            "url": "https://github.com/weiyifan1023/STEPS"
          },
          {
            "title": "[2601.03676] Towards Compositional Generalization of LLMs via Skill Taxonomy Guided Data Synthesis",
            "url": "https://arxiv.org/abs/2601.03676"
          },
          {
            "title": "Towards a Theoretical Understanding of Synthetic Data in LLM Post-Training: A Reverse-Bottleneck Perspective",
            "url": "https://arxiv.org/html/2410.01720v2"
          },
          {
            "title": "Compositional Skill Acquisition in LLMs",
            "url": "https://www.emergentmind.com/topics/compositional-skill-acquisition-in-llms"
          }
        ]
      },
      "The search results reveal significant recent research (2025-2026) on compositional skill pair coverage gaps and targeted data synthesis for LLM training efficiency:\n\n## Key Findings\n\nLLMs and agent-based systems struggle with compositional generalization due to a data bottleneck where complex skill combinations follow a long-tailed, power-law distribution, limiting instruction-following performance and generalization in agent-centric tasks.\n\n### STEPS Framework\n\nSTEPS is a Skill Taxonomy guided Entropy-based Post-training data Synthesis framework that addresses this by uncovering latent relationships among skills and organizing them into an interpretable, hierarchical skill taxonomy using structural information theory. The framework formulates data synthesis as a constrained information maximization problem, selecting skill combinations that maximize marginal structural information within the hierarchy while preserving semantic coherence.\n\n### Training Efficiency Improvements\n\nRecent efforts utilize data synthesis via stochastic skill pairing to bridge compositional data gaps, though heuristic methods often ignore latent hierarchical dependencies, which may result in semantically incoherent compositions and inefficient exploration of the combinatorial space.\n\n### Performance Impact\n\nExperiments on challenging instruction-following benchmarks show that STEPS outperforms existing data synthesis baselines, while also yielding improved compositional generalization in downstream agent-based evaluations.\n\nThese advances represent a systematic shift from random skill pairing to theoretically-grounded approaches that target specific compositional coverage gaps."
    ],
    "durationSeconds": 9.398644704999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "06db584b-5b3b-4b03-aaa8-2c066b193227",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-29T12:27:18.238Z_

```json
{
  "parentUuid": "578a2690-42ef-401c-bf79-32f13e41beb0",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "001ed2fe-fd4d-41b1-8f66-2244830c7b1c",
  "timestamp": "2026-05-29T12:27:18.238Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 30 · 2026-05-29T12:27:20.027Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017i3SnTYKQdSX61ZQPtDpBx`</summary>

```json
{
  "query": "STEPS arXiv 2601.03676 skill taxonomy entropy structural information theory compositional generalization limitations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "001ed2fe-fd4d-41b1-8f66-2244830c7b1c",
  "isSidechain": false,
  "requestId": "req_011CbWrktmEspqVMdg9Mr9pD",
  "type": "assistant",
  "uuid": "ab884c44-f14b-4554-8745-95ef14bf65e5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CMtS6GbMXzZos61ShWr5Ee",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 840,
      "cache_read_input_tokens": 24572,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 840,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 24572,
          "cache_creation_input_tokens": 840,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 840
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

_source line 31 · 2026-05-29T12:27:26.774Z_

<details><summary>↩ Tool result · `toolu_017i3SnTYKQdSX61ZQPtDpBx`</summary>

```text
Web search results for query: "STEPS arXiv 2601.03676 skill taxonomy entropy structural information theory compositional generalization limitations"

Links: [{"title":"[2601.03676] Towards Compositional Generalization of LLMs via Skill Taxonomy Guided Data Synthesis","url":"https://arxiv.org/abs/2601.03676"},{"title":"Towards Compositional Generalization of LLMs via Skill Taxonomy Guided Data Synthesis","url":"https://arxiv.org/pdf/2601.03676"},{"title":"Paper page - Towards Compositional Generalization of LLMs via Skill Taxonomy Guided Data Synthesis","url":"https://huggingface.co/papers/2601.03676"},{"title":"Towards Compositional Generalization of LLMs via Skill Taxonomy Guided Data Synthesis","url":"https://arxiv.org/html/2601.03676v1"},{"title":"GitHub - weiyifan1023/STEPS: Code and Data for Paper \"Towards Compositional Generalization of LLMs via Skill Taxonomy Guided Data Synthesis\"","url":"https://github.com/weiyifan1023/STEPS"}]

Based on the search results, here's what I found about arXiv paper 2601.03676:

## Overview

STEPS is a Skill Taxonomy guided Entropy-based Post-training data Synthesis framework for generating compositionally challenging data.

## Problem Addressed

Large Language Models (LLMs) and agent-based systems often struggle with compositional generalization due to a data bottleneck in which complex skill combinations follow a long-tailed, power-law distribution, limiting both instruction-following performance and generalization in agent-centric tasks.

## Key Technical Approach

STEPS explicitly targets compositional generalization by uncovering latent relationships among skills and organizing them into an interpretable, hierarchical skill taxonomy using structural information theory.

The method has two main components:

1. **Skill Taxonomy Construction**: STEPS first induces a hierarchical skill dependency taxonomy by constructing a skill co-occurrence graph and recursively merging groups of skill nodes with dense intra-group connections and sparse inter-group connections. This process is guided by minimizing structural entropy, which favors hierarchies in which high-weight co-occurrence edges are largely explained within local groups rather than across unrelated ones, yielding a compact and interpretable dependency structure over skills.

2. **Data Synthesis**: Building on this taxonomy, data synthesis is formulated as a constrained information maximization problem, selecting skill combinations that maximize marginal structural information within the hierarchy while preserving semantic coherence.

## Results

Experiments on challenging instruction-following benchmarks show that STEPS outperforms existing data synthesis baselines, while also yielding improved compositional generalization in downstream agent-based evaluations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ab884c44-f14b-4554-8745-95ef14bf65e5",
  "isSidechain": false,
  "promptId": "e367c23d-5456-4f70-a5b3-3d1f58831111",
  "type": "user",
  "uuid": "6421406d-7b5a-4363-ada1-1660b8048ab6",
  "toolUseResult": {
    "query": "STEPS arXiv 2601.03676 skill taxonomy entropy structural information theory compositional generalization limitations",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FmVvX5K5hWzEKGfwYFTKUy",
        "content": [
          {
            "title": "[2601.03676] Towards Compositional Generalization of LLMs via Skill Taxonomy Guided Data Synthesis",
            "url": "https://arxiv.org/abs/2601.03676"
          },
          {
            "title": "Towards Compositional Generalization of LLMs via Skill Taxonomy Guided Data Synthesis",
            "url": "https://arxiv.org/pdf/2601.03676"
          },
          {
            "title": "Paper page - Towards Compositional Generalization of LLMs via Skill Taxonomy Guided Data Synthesis",
            "url": "https://huggingface.co/papers/2601.03676"
          },
          {
            "title": "Towards Compositional Generalization of LLMs via Skill Taxonomy Guided Data Synthesis",
            "url": "https://arxiv.org/html/2601.03676v1"
          },
          {
            "title": "GitHub - weiyifan1023/STEPS: Code and Data for Paper \"Towards Compositional Generalization of LLMs via Skill Taxonomy Guided Data Synthesis\"",
            "url": "https://github.com/weiyifan1023/STEPS"
          }
        ]
      },
      "Based on the search results, here's what I found about arXiv paper 2601.03676:\n\n## Overview\n\nSTEPS is a Skill Taxonomy guided Entropy-based Post-training data Synthesis framework for generating compositionally challenging data.\n\n## Problem Addressed\n\nLarge Language Models (LLMs) and agent-based systems often struggle with compositional generalization due to a data bottleneck in which complex skill combinations follow a long-tailed, power-law distribution, limiting both instruction-following performance and generalization in agent-centric tasks.\n\n## Key Technical Approach\n\nSTEPS explicitly targets compositional generalization by uncovering latent relationships among skills and organizing them into an interpretable, hierarchical skill taxonomy using structural information theory.\n\nThe method has two main components:\n\n1. **Skill Taxonomy Construction**: STEPS first induces a hierarchical skill dependency taxonomy by constructing a skill co-occurrence graph and recursively merging groups of skill nodes with dense intra-group connections and sparse inter-group connections. This process is guided by minimizing structural entropy, which favors hierarchies in which high-weight co-occurrence edges are largely explained within local groups rather than across unrelated ones, yielding a compact and interpretable dependency structure over skills.\n\n2. **Data Synthesis**: Building on this taxonomy, data synthesis is formulated as a constrained information maximization problem, selecting skill combinations that maximize marginal structural information within the hierarchy while preserving semantic coherence.\n\n## Results\n\nExperiments on challenging instruction-following benchmarks show that STEPS outperforms existing data synthesis baselines, while also yielding improved compositional generalization in downstream agent-based evaluations."
    ],
    "durationSeconds": 6.741691262000008,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "ab884c44-f14b-4554-8745-95ef14bf65e5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-29T12:27:29.623Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01M7JB3m2ox1aNjVVH4moPf1`</summary>

```json
{
  "query": "\"Agentic Proposing\" arXiv 2602.03279 compositional skill synthesis difficulty adaptive multi-granularity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6421406d-7b5a-4363-ada1-1660b8048ab6",
  "isSidechain": false,
  "requestId": "req_011CbWrmXHSJz5kMUcHrTNs4",
  "type": "assistant",
  "uuid": "b903fbb9-f922-41b9-a49d-a78924369927",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ajXu9NbFREZwD6r1GyAwQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 753,
      "cache_read_input_tokens": 25412,
      "output_tokens": 81,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 753,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 81,
          "cache_read_input_tokens": 25412,
          "cache_creation_input_tokens": 753,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 753
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

_source line 33 · 2026-05-29T12:27:36.752Z_

<details><summary>↩ Tool result · `toolu_01M7JB3m2ox1aNjVVH4moPf1`</summary>

```text
Web search results for query: ""Agentic Proposing" arXiv 2602.03279 compositional skill synthesis difficulty adaptive multi-granularity"

Links: [{"title":"[2602.03279] Agentic Proposing: Enhancing Large Language Model Reasoning via Compositional Skill Synthesis","url":"https://arxiv.org/abs/2602.03279"},{"title":"Agentic Proposing: Enhancing Large Language Model Reasoning via Compositional Skill Synthesis | alphaXiv","url":"https://www.alphaxiv.org/overview/2602.03279"},{"title":"Agentic Proposing: Enhancing Large Language Model Reasoning via Compositional Skill Synthesis","url":"https://arxiv.org/html/2602.03279"},{"title":"(PDF) Agentic Proposing: Enhancing Large Language Model Reasoning via Compositional Skill Synthesis","url":"https://www.researchgate.net/publication/400414852_Agentic_Proposing_Enhancing_Large_Language_Model_Reasoning_via_Compositional_Skill_Synthesis"},{"title":"Agentic Proposing: Enhancing Large Language Model ...","url":"https://arxiv.org/pdf/2602.03279"},{"title":"Agent Skills for Large Language Models: Architecture, ...","url":"https://arxiv.org/pdf/2602.12430"},{"title":"(PDF) Agent Skills for Large Language Models: Architecture, Acquisition, Security, and the Path Forward","url":"https://www.researchgate.net/publication/400812095_Agent_Skills_for_Large_Language_Models_Architecture_Acquisition_Security_and_the_Path_Forward"}]

Based on the search results, here's what I found about the paper:

## Overview

Agentic Proposing is a framework that models problem synthesis as a goal-driven sequential decision process where a specialized agent dynamically selects and composes modular reasoning skills.

## Problem and Motivation

Current synthesis paradigms often face a recurring trade-off: maintaining structural validity typically restricts problem complexity, while relaxing constraints to increase difficulty frequently leads to inconsistent or unsolvable instances.

## Approach

The framework develops the Agentic-Proposer-4B using Multi-Granularity Policy Optimization (MGPO) to generate high-precision, verifiable training trajectories across mathematics, coding, and science. Agentic proposing is a closed-loop process that composes modular skills and uses tool-assisted verification to produce stable, verifiable, and well-calibrated problems.

## Results

A 30B solver trained on only 11,000 synthesized trajectories achieves a state-of-the-art 91.6% accuracy on AIME25, rivaling frontier-scale proprietary models such as GPT-5 and proving that a small volume of high-quality synthetic signals can effectively substitute for massive datasets.

The paper was submitted to arXiv on February 3, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b903fbb9-f922-41b9-a49d-a78924369927",
  "isSidechain": false,
  "promptId": "e367c23d-5456-4f70-a5b3-3d1f58831111",
  "type": "user",
  "uuid": "5f1d94c0-de5b-433e-b9d3-725ebf797801",
  "toolUseResult": {
    "query": "\"Agentic Proposing\" arXiv 2602.03279 compositional skill synthesis difficulty adaptive multi-granularity",
    "results": [
      {
        "tool_use_id": "srvtoolu_0175BQjWPM7u2QpcKJQ9QgqH",
        "content": [
          {
            "title": "[2602.03279] Agentic Proposing: Enhancing Large Language Model Reasoning via Compositional Skill Synthesis",
            "url": "https://arxiv.org/abs/2602.03279"
          },
          {
            "title": "Agentic Proposing: Enhancing Large Language Model Reasoning via Compositional Skill Synthesis | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2602.03279"
          },
          {
            "title": "Agentic Proposing: Enhancing Large Language Model Reasoning via Compositional Skill Synthesis",
            "url": "https://arxiv.org/html/2602.03279"
          },
          {
            "title": "(PDF) Agentic Proposing: Enhancing Large Language Model Reasoning via Compositional Skill Synthesis",
            "url": "https://www.researchgate.net/publication/400414852_Agentic_Proposing_Enhancing_Large_Language_Model_Reasoning_via_Compositional_Skill_Synthesis"
          },
          {
            "title": "Agentic Proposing: Enhancing Large Language Model ...",
            "url": "https://arxiv.org/pdf/2602.03279"
          },
          {
            "title": "Agent Skills for Large Language Models: Architecture, ...",
            "url": "https://arxiv.org/pdf/2602.12430"
          },
          {
            "title": "(PDF) Agent Skills for Large Language Models: Architecture, Acquisition, Security, and the Path Forward",
            "url": "https://www.researchgate.net/publication/400812095_Agent_Skills_for_Large_Language_Models_Architecture_Acquisition_Security_and_the_Path_Forward"
          }
        ]
      },
      "Based on the search results, here's what I found about the paper:\n\n## Overview\n\nAgentic Proposing is a framework that models problem synthesis as a goal-driven sequential decision process where a specialized agent dynamically selects and composes modular reasoning skills.\n\n## Problem and Motivation\n\nCurrent synthesis paradigms often face a recurring trade-off: maintaining structural validity typically restricts problem complexity, while relaxing constraints to increase difficulty frequently leads to inconsistent or unsolvable instances.\n\n## Approach\n\nThe framework develops the Agentic-Proposer-4B using Multi-Granularity Policy Optimization (MGPO) to generate high-precision, verifiable training trajectories across mathematics, coding, and science. Agentic proposing is a closed-loop process that composes modular skills and uses tool-assisted verification to produce stable, verifiable, and well-calibrated problems.\n\n## Results\n\nA 30B solver trained on only 11,000 synthesized trajectories achieves a state-of-the-art 91.6% accuracy on AIME25, rivaling frontier-scale proprietary models such as GPT-5 and proving that a small volume of high-quality synthetic signals can effectively substitute for massive datasets.\n\nThe paper was submitted to arXiv on February 3, 2026."
    ],
    "durationSeconds": 7.124934036999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "b903fbb9-f922-41b9-a49d-a78924369927",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1",
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
  "lastPrompt": "# Skill-DAG-Guided Frontier Synthesis for Mathematical Compositional Generalization  ## Core Problem  LLMs exhibit a persistent compositional ceiling in mathematical reasoning: OMEGA (NeurIPS 2025, ar…",
  "leafUuid": "5f1d94c0-de5b-433e-b9d3-725ebf797801",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Skill-DAG-guided synthesis for math compositional generalization",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1"
}
```

---

### Tool call

_source line 36 · 2026-05-29T12:27:39.750Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FpJn6VP9iU1SzppjQwBJAX`</summary>

```json
{
  "query": "MathFusion arXiv 2503.16212 ACL 2025 problem fusion sequential parallel conditional composition strategy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f1d94c0-de5b-433e-b9d3-725ebf797801",
  "isSidechain": false,
  "requestId": "req_011CbWrnFwjQSquyuxX44Zuc",
  "type": "assistant",
  "uuid": "b1669872-50cb-495b-9145-d5c79978a860",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011nBxy5xLkwxyw4J5Lw2B6Y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 817,
      "cache_read_input_tokens": 26165,
      "output_tokens": 78,
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
          "output_tokens": 78,
          "cache_read_input_tokens": 26165,
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

_source line 37 · 2026-05-29T12:27:48.328Z_

<details><summary>↩ Tool result · `toolu_01FpJn6VP9iU1SzppjQwBJAX`</summary>

```text
Web search results for query: "MathFusion arXiv 2503.16212 ACL 2025 problem fusion sequential parallel conditional composition strategy"

Links: [{"title":"[2503.16212] MathFusion: Enhancing Mathematical Problem-solving of LLM through Instruction Fusion","url":"https://arxiv.org/abs/2503.16212"},{"title":"GitHub - QizhiPei/MathFusion: MathFusion: Enhancing Mathematical Problem-solving of LLM through Instruction Fusion (ACL 2025)","url":"https://github.com/QizhiPei/MathFusion"},{"title":"[Quick Review] MathFusion: Enhancing Mathematic Problem-solving of LLM through Instruction Fusion","url":"https://liner.com/review/mathfusion-enhancing-mathematic-problemsolving-llm-through-instruction-fusion"},{"title":"arXiv:2503.16212v2 [cs.CL] 16 Jun 2025","url":"https://arxiv.org/pdf/2503.16212"},{"title":"MathFusion: Enhancing Mathematical Problem-solving of LLM through Instruction Fusion - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.367/"},{"title":"Computation and Language Mar 2025","url":"https://arxiv.org/list/cs.CL/2025-03?skip=950&show=250"},{"title":"MathFusion: Enhancing Mathematical Problem-solving of ...","url":"https://aclanthology.org/2025.acl-long.367.pdf"},{"title":"MathFusion: Enhancing Mathematical Problem-solving of LLM through Instruction Fusion","url":"https://arxiv.org/html/2503.16212"}]

Based on the search results, I found comprehensive information about MathFusion:

## MathFusion Overview

MathFusion is a novel framework that enhances mathematical reasoning through cross-problem instruction synthesis, inspired by human learning processes where mathematical proficiency develops through systematic exposure to interconnected concepts.

## Three Fusion Strategies

The framework implements Sequential Fusion, which chains related problems to model solution dependencies. Parallel Fusion combines analogous problems to reinforce conceptual understanding, while Conditional Fusion creates context-aware selective problems to enhance reasoning flexibility.

## Motivation and Approach

While data augmentation is promising to enhance mathematical problem-solving ability, current approaches are predominantly limited to instance-level modifications—such as rephrasing or generating syntactic variations—which fail to capture and leverage the intrinsic relational structures inherent in mathematical knowledge.

## Results and Performance

The researchers generated a new dataset called MathFusionQA and fine-tuned models (DeepSeekMath-7B, Mistral-7B, Llama3-8B) on it. Experimental results demonstrate that MathFusion achieves substantial improvements in mathematical reasoning while maintaining high data efficiency, boosting performance by 18.0 points in accuracy across diverse benchmarks while requiring only 45K additional synthetic instructions.

## Publication

The paper has been accepted by ACL 2025 (main conference) and is available as arXiv preprint 2503.16212.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b1669872-50cb-495b-9145-d5c79978a860",
  "isSidechain": false,
  "promptId": "e367c23d-5456-4f70-a5b3-3d1f58831111",
  "type": "user",
  "uuid": "017fc6ed-5397-464a-977c-81e876ae04c8",
  "toolUseResult": {
    "query": "MathFusion arXiv 2503.16212 ACL 2025 problem fusion sequential parallel conditional composition strategy",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BExiXjkhtBkKYa7TukjK2D",
        "content": [
          {
            "title": "[2503.16212] MathFusion: Enhancing Mathematical Problem-solving of LLM through Instruction Fusion",
            "url": "https://arxiv.org/abs/2503.16212"
          },
          {
            "title": "GitHub - QizhiPei/MathFusion: MathFusion: Enhancing Mathematical Problem-solving of LLM through Instruction Fusion (ACL 2025)",
            "url": "https://github.com/QizhiPei/MathFusion"
          },
          {
            "title": "[Quick Review] MathFusion: Enhancing Mathematic Problem-solving of LLM through Instruction Fusion",
            "url": "https://liner.com/review/mathfusion-enhancing-mathematic-problemsolving-llm-through-instruction-fusion"
          },
          {
            "title": "arXiv:2503.16212v2 [cs.CL] 16 Jun 2025",
            "url": "https://arxiv.org/pdf/2503.16212"
          },
          {
            "title": "MathFusion: Enhancing Mathematical Problem-solving of LLM through Instruction Fusion - ACL Anthology",
            "url": "https://aclanthology.org/2025.acl-long.367/"
          },
          {
            "title": "Computation and Language Mar 2025",
            "url": "https://arxiv.org/list/cs.CL/2025-03?skip=950&show=250"
          },
          {
            "title": "MathFusion: Enhancing Mathematical Problem-solving of ...",
            "url": "https://aclanthology.org/2025.acl-long.367.pdf"
          },
          {
            "title": "MathFusion: Enhancing Mathematical Problem-solving of LLM through Instruction Fusion",
            "url": "https://arxiv.org/html/2503.16212"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about MathFusion:\n\n## MathFusion Overview\n\nMathFusion is a novel framework that enhances mathematical reasoning through cross-problem instruction synthesis, inspired by human learning processes where mathematical proficiency develops through systematic exposure to interconnected concepts.\n\n## Three Fusion Strategies\n\nThe framework implements Sequential Fusion, which chains related problems to model solution dependencies. Parallel Fusion combines analogous problems to reinforce conceptual understanding, while Conditional Fusion creates context-aware selective problems to enhance reasoning flexibility.\n\n## Motivation and Approach\n\nWhile data augmentation is promising to enhance mathematical problem-solving ability, current approaches are predominantly limited to instance-level modifications—such as rephrasing or generating syntactic variations—which fail to capture and leverage the intrinsic relational structures inherent in mathematical knowledge.\n\n## Results and Performance\n\nThe researchers generated a new dataset called MathFusionQA and fine-tuned models (DeepSeekMath-7B, Mistral-7B, Llama3-8B) on it. Experimental results demonstrate that MathFusion achieves substantial improvements in mathematical reasoning while maintaining high data efficiency, boosting performance by 18.0 points in accuracy across diverse benchmarks while requiring only 45K additional synthetic instructions.\n\n## Publication\n\nThe paper has been accepted by ACL 2025 (main conference) and is available as arXiv preprint 2503.16212."
    ],
    "durationSeconds": 8.574359077999993,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "b1669872-50cb-495b-9145-d5c79978a860",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-29T12:27:52.098Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WA1Jyu2upb4FgtGaaPtY74`</summary>

```json
{
  "query": "knowledge prerequisite graph skill dependency structure compositional training data generation LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "017fc6ed-5397-464a-977c-81e876ae04c8",
  "isSidechain": false,
  "requestId": "req_011CbWro7YjwZjPucR8ZCCp2",
  "type": "assistant",
  "uuid": "06ee3512-02a1-432c-abce-208fc79f5dab",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KnMVPBt5gz8fTrZc2rCgQg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 872,
      "cache_read_input_tokens": 26982,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 872,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 26982,
          "cache_creation_input_tokens": 872,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 872
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

_source line 39 · 2026-05-29T12:27:59.185Z_

<details><summary>↩ Tool result · `toolu_01WA1Jyu2upb4FgtGaaPtY74`</summary>

```text
Web search results for query: "knowledge prerequisite graph skill dependency structure compositional training data generation LLM 2025 2026"

Links: [{"title":"Towards Compositional Generalization of LLMs via Skill Taxonomy Guided Data Synthesis","url":"https://arxiv.org/pdf/2601.03676"},{"title":"Towards Compositional Generalization of LLMs via Skill Taxonomy Guided Data Synthesis","url":"https://arxiv.org/html/2601.03676v1"},{"title":"Not All Features Deserve Attention: Graph-Guided Dependency Learning for Tabular Data Generation with Language Models","url":"https://arxiv.org/pdf/2507.18504"},{"title":"Enhancing LLM Tool Use with High-quality Instruction Data from Knowledge Graph","url":"https://arxiv.org/pdf/2506.21071"},{"title":"Graph of Skills: Dependency-Aware Structural Retrieval for Massive Agent Skills","url":"https://arxiv.org/pdf/2604.05333"},{"title":"What do Language Models Learn and When? The Implicit Curriculum Hypothesis","url":"https://arxiv.org/pdf/2604.08510"}]

The search results reveal several recent developments in 2025-2026 related to knowledge prerequisite graphs, skill dependency structures, and compositional training data generation for large language models:

## Key Findings:

**Skill Taxonomy-Guided Data Synthesis (STEPS)**
A recent approach uses structural entropy minimization to create compact dependency structures over skills, then synthesizes data by recursively composing skill nodes to maximize structural entropy gain. This strategy prioritizes skill compositions that introduce the largest amount of new structural information while remaining coherent with the induced hierarchy, efficiently exploring the combinatorial skill space.

**Graph-Based Skill Retrieval (Graph of Skills)**
Graph of Skills (GoS) is an inference-time structural retrieval layer that constructs a directed multi-relational graph over skill packages, where nodes are executable skills and edges encode prerequisite and workflow structure.

**Compositional Skill Structures**
Skills can be represented as directed acyclic graphs (DAGs), where an edge from skill A to skill B indicates that training on data associated with A reduces the amount of data needed to learn B.

**Addressing Compositional Data Scarcity**
While data-centric strategies exist for individual skills, approaches that synthesize compositional data through skill mixing typically ignore underlying structural and hierarchical relationships among skills, resulting in semantically incoherent compositions.

These developments represent an emerging focus on leveraging skill dependency structures to improve compositional generalization in LLMs through structured data generation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "06ee3512-02a1-432c-abce-208fc79f5dab",
  "isSidechain": false,
  "promptId": "e367c23d-5456-4f70-a5b3-3d1f58831111",
  "type": "user",
  "uuid": "06a62745-bb4b-4d40-94ff-f54195f5ce20",
  "toolUseResult": {
    "query": "knowledge prerequisite graph skill dependency structure compositional training data generation LLM 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01N56ujBc2bnnFSogr3Yquk8",
        "content": [
          {
            "title": "Towards Compositional Generalization of LLMs via Skill Taxonomy Guided Data Synthesis",
            "url": "https://arxiv.org/pdf/2601.03676"
          },
          {
            "title": "Towards Compositional Generalization of LLMs via Skill Taxonomy Guided Data Synthesis",
            "url": "https://arxiv.org/html/2601.03676v1"
          },
          {
            "title": "Not All Features Deserve Attention: Graph-Guided Dependency Learning for Tabular Data Generation with Language Models",
            "url": "https://arxiv.org/pdf/2507.18504"
          },
          {
            "title": "Enhancing LLM Tool Use with High-quality Instruction Data from Knowledge Graph",
            "url": "https://arxiv.org/pdf/2506.21071"
          },
          {
            "title": "Graph of Skills: Dependency-Aware Structural Retrieval for Massive Agent Skills",
            "url": "https://arxiv.org/pdf/2604.05333"
          },
          {
            "title": "What do Language Models Learn and When? The Implicit Curriculum Hypothesis",
            "url": "https://arxiv.org/pdf/2604.08510"
          }
        ]
      },
      "The search results reveal several recent developments in 2025-2026 related to knowledge prerequisite graphs, skill dependency structures, and compositional training data generation for large language models:\n\n## Key Findings:\n\n**Skill Taxonomy-Guided Data Synthesis (STEPS)**\nA recent approach uses structural entropy minimization to create compact dependency structures over skills, then synthesizes data by recursively composing skill nodes to maximize structural entropy gain. This strategy prioritizes skill compositions that introduce the largest amount of new structural information while remaining coherent with the induced hierarchy, efficiently exploring the combinatorial skill space.\n\n**Graph-Based Skill Retrieval (Graph of Skills)**\nGraph of Skills (GoS) is an inference-time structural retrieval layer that constructs a directed multi-relational graph over skill packages, where nodes are executable skills and edges encode prerequisite and workflow structure.\n\n**Compositional Skill Structures**\nSkills can be represented as directed acyclic graphs (DAGs), where an edge from skill A to skill B indicates that training on data associated with A reduces the amount of data needed to learn B.\n\n**Addressing Compositional Data Scarcity**\nWhile data-centric strategies exist for individual skills, approaches that synthesize compositional data through skill mixing typically ignore underlying structural and hierarchical relationships among skills, resulting in semantically incoherent compositions.\n\nThese developments represent an emerging focus on leveraging skill dependency structures to improve compositional generalization in LLMs through structured data generation."
    ],
    "durationSeconds": 7.083009073999987,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "06ee3512-02a1-432c-abce-208fc79f5dab",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-29T12:28:01.462Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BePtwhMB6nJk7qDE2X8jay`</summary>

```json
{
  "query": "\"coverage gap\" \"skill graph\" OR \"prerequisite DAG\" math reasoning training data targeted synthesis 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06a62745-bb4b-4d40-94ff-f54195f5ce20",
  "isSidechain": false,
  "requestId": "req_011CbWrour4DoDKGSyz1ny9Z",
  "type": "assistant",
  "uuid": "59f27d1c-0a00-479b-ae7c-e70ba99e4940",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015wDU6vt2fJa37nm4eVfokK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 709,
      "cache_read_input_tokens": 27854,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 709,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 27854,
          "cache_creation_input_tokens": 709,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 709
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

_source line 41 · 2026-05-29T12:28:08.946Z_

<details><summary>↩ Tool result · `toolu_01BePtwhMB6nJk7qDE2X8jay`</summary>

```text
Web search results for query: ""coverage gap" "skill graph" OR "prerequisite DAG" math reasoning training data targeted synthesis 2026"

Links: [{"title":"DAG-Math: Graph-Guided Mathematical Reasoning in LLMs","url":"https://arxiv.org/html/2510.19842v1"},{"title":"Enhanced Data Synthesis for LLM through Reasoning ...","url":"https://aclanthology.org/2025.findings-acl.821.pdf"},{"title":"The New Math Skills Every Data Scientist Must Master in 2026 | by Sahin Ahmed(Data Scientist/MLE) | Medium","url":"https://medium.com/@sahin.samia/the-new-math-skills-every-data-scientist-must-master-in-2026-355f6a577ab8"},{"title":"Skill-Targeted Adaptive Training","url":"https://arxiv.org/pdf/2510.10023"},{"title":"Agentic Proposing: Enhancing Large Language Model Reasoning via Compositional Skill Synthesis","url":"https://arxiv.org/pdf/2602.03279"},{"title":"Improving LLMs' Generalized Reasoning Abilities by Graph ...","url":"https://arxiv.org/pdf/2507.17168"},{"title":"MASS: Mathematical Data Selection via Skill Graphs for Pretraining Large Language Models","url":"https://arxiv.org/pdf/2503.14917"}]

Based on the search results, here are the relevant findings related to your query about coverage gaps, skill graphs, prerequisite DAGs, and math reasoning training data:

## Key Research Areas

**Skill-Targeted Adaptive Training (STAT):**
STAT is a three-stage skill-based data selection/generation method that identifies difficult questions for each model, uses frontier LLMs to build a model-specific Missing-Skill-Profile, and then uses a pre-constructed Skill-Map to guide training question distribution, with synthesis of new questions targeted to missing skills. The method yields improvements of up to 7.5% on MATH benchmarks.

**Skill Graphs for Data Selection:**
MASS constructs a skill graph that captures mathematical skills and their interrelations from a reference dataset, which guides quality score assignment to target datasets for selection. Models trained on subsets selected by MASS achieve similar performance with 50-70% fewer tokens, and when trained on equal tokens, outperform baseline models by 3.3% to 5.9%.

**Agentic Synthesis:**
Agentic Proposing models problem synthesis as a goal-driven sequential decision process where agents dynamically select and compose modular reasoning skills to generate high-precision, verifiable training trajectories. A 30B solver trained on 11,000 synthesized trajectories achieves 91.6% accuracy on AIME25.

**DAG-Based Reasoning:**
DAG-Math provides a framework balancing free-form CoT and formal proof systems, offering actionable diagnostics for LLM reasoning evaluation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "59f27d1c-0a00-479b-ae7c-e70ba99e4940",
  "isSidechain": false,
  "promptId": "e367c23d-5456-4f70-a5b3-3d1f58831111",
  "type": "user",
  "uuid": "bf243482-3706-4d7a-9cb7-13669dfe6f7f",
  "toolUseResult": {
    "query": "\"coverage gap\" \"skill graph\" OR \"prerequisite DAG\" math reasoning training data targeted synthesis 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DHawrxMXvhW5d9zhTi7jgA",
        "content": [
          {
            "title": "DAG-Math: Graph-Guided Mathematical Reasoning in LLMs",
            "url": "https://arxiv.org/html/2510.19842v1"
          },
          {
            "title": "Enhanced Data Synthesis for LLM through Reasoning ...",
            "url": "https://aclanthology.org/2025.findings-acl.821.pdf"
          },
          {
            "title": "The New Math Skills Every Data Scientist Must Master in 2026 | by Sahin Ahmed(Data Scientist/MLE) | Medium",
            "url": "https://medium.com/@sahin.samia/the-new-math-skills-every-data-scientist-must-master-in-2026-355f6a577ab8"
          },
          {
            "title": "Skill-Targeted Adaptive Training",
            "url": "https://arxiv.org/pdf/2510.10023"
          },
          {
            "title": "Agentic Proposing: Enhancing Large Language Model Reasoning via Compositional Skill Synthesis",
            "url": "https://arxiv.org/pdf/2602.03279"
          },
          {
            "title": "Improving LLMs' Generalized Reasoning Abilities by Graph ...",
            "url": "https://arxiv.org/pdf/2507.17168"
          },
          {
            "title": "MASS: Mathematical Data Selection via Skill Graphs for Pretraining Large Language Models",
            "url": "https://arxiv.org/pdf/2503.14917"
          }
        ]
      },
      "Based on the search results, here are the relevant findings related to your query about coverage gaps, skill graphs, prerequisite DAGs, and math reasoning training data:\n\n## Key Research Areas\n\n**Skill-Targeted Adaptive Training (STAT):**\nSTAT is a three-stage skill-based data selection/generation method that identifies difficult questions for each model, uses frontier LLMs to build a model-specific Missing-Skill-Profile, and then uses a pre-constructed Skill-Map to guide training question distribution, with synthesis of new questions targeted to missing skills. The method yields improvements of up to 7.5% on MATH benchmarks.\n\n**Skill Graphs for Data Selection:**\nMASS constructs a skill graph that captures mathematical skills and their interrelations from a reference dataset, which guides quality score assignment to target datasets for selection. Models trained on subsets selected by MASS achieve similar performance with 50-70% fewer tokens, and when trained on equal tokens, outperform baseline models by 3.3% to 5.9%.\n\n**Agentic Synthesis:**\nAgentic Proposing models problem synthesis as a goal-driven sequential decision process where agents dynamically select and compose modular reasoning skills to generate high-precision, verifiable training trajectories. A 30B solver trained on 11,000 synthesized trajectories achieves 91.6% accuracy on AIME25.\n\n**DAG-Based Reasoning:**\nDAG-Math provides a framework balancing free-form CoT and formal proof systems, offering actionable diagnostics for LLM reasoning evaluation."
    ],
    "durationSeconds": 7.480317093999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "59f27d1c-0a00-479b-ae7c-e70ba99e4940",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-29T12:28:11.253Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019KeRpM9C8q6ffSvfY7JG5b`</summary>

```json
{
  "query": "Redhardt NeurIPS 2025 spotlight arXiv 2507.07207 compositional generalization MLP linear scaling coverage"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf243482-3706-4d7a-9cb7-13669dfe6f7f",
  "isSidechain": false,
  "requestId": "req_011CbWrpdcmsAL16MEVXfUPG",
  "type": "assistant",
  "uuid": "5ec7868f-4f99-4c90-81d0-2545b25b8a46",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015KAwh35XnH3nwgKxzKNw9f",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 804,
      "cache_read_input_tokens": 28563,
      "output_tokens": 82,
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
          "output_tokens": 82,
          "cache_read_input_tokens": 28563,
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

_source line 43 · 2026-05-29T12:28:16.898Z_

<details><summary>↩ Tool result · `toolu_019KeRpM9C8q6ffSvfY7JG5b`</summary>

```text
Web search results for query: "Redhardt NeurIPS 2025 spotlight arXiv 2507.07207 compositional generalization MLP linear scaling coverage"

Links: [{"title":"Computer Science Jul 2025","url":"https://www.arxiv.org/list/cs/2025-07?skip=3125&show=2000"},{"title":"Machine Learning Jul 2025","url":"https://arxiv.org/list/cs.LG/2025-07?skip=600&show=100"},{"title":"[2507.07207] Scaling can lead to compositional generalization","url":"https://arxiv.org/abs/2507.07207"},{"title":"Scaling can lead to compositional generalization Florian Redhardt∗ ETH Zurich","url":"https://arxiv.org/pdf/2507.07207"},{"title":"[2507.07207] Scale leads to compositional generalization","url":"https://ar5iv.labs.arxiv.org/html/2507.07207"},{"title":"Scaling can lead to compositional generalization","url":"https://proceedings.neurips.cc/paper_files/paper/2025/hash/5047b64366bc0dbf5047de85f1e0c7be-Abstract-Conference.html"},{"title":"Scaling can lead to compositional generalization","url":"https://arxiv.org/html/2507.07207"}]

Based on the search results, here's what I found about this paper:

The paper "Scaling can lead to compositional generalization" by Florian Redhardt, Yassir Akram, and Simon Schug (arXiv:2507.07207) is a NeurIPS 2025 Spotlight paper.

**Key Findings:**

The paper finds that simply scaling data and model size leads to compositional generalization, and shows that this holds across different task encodings as long as the training distribution sufficiently covers the task space.

**Theoretical Contribution:**

The authors prove that standard multilayer perceptrons can approximate a general class of compositional task families to arbitrary precision using only a linear number of neurons with respect to the number of task modules. This directly addresses the linear scaling aspect mentioned in your query.

The paper investigates how standard neural networks can capture discrete, compositional task structure and achieve compositional generalization through scaling, with empirical validation supporting the theoretical finding about linear scaling of MLPs in relation to task modules.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5ec7868f-4f99-4c90-81d0-2545b25b8a46",
  "isSidechain": false,
  "promptId": "e367c23d-5456-4f70-a5b3-3d1f58831111",
  "type": "user",
  "uuid": "c4f2041c-8b95-4c13-89ed-3b0482a54523",
  "toolUseResult": {
    "query": "Redhardt NeurIPS 2025 spotlight arXiv 2507.07207 compositional generalization MLP linear scaling coverage",
    "results": [
      {
        "tool_use_id": "srvtoolu_013FaUX1uhqHGFjDiDgUWJvq",
        "content": [
          {
            "title": "Computer Science Jul 2025",
            "url": "https://www.arxiv.org/list/cs/2025-07?skip=3125&show=2000"
          },
          {
            "title": "Machine Learning Jul 2025",
            "url": "https://arxiv.org/list/cs.LG/2025-07?skip=600&show=100"
          },
          {
            "title": "[2507.07207] Scaling can lead to compositional generalization",
            "url": "https://arxiv.org/abs/2507.07207"
          },
          {
            "title": "Scaling can lead to compositional generalization Florian Redhardt∗ ETH Zurich",
            "url": "https://arxiv.org/pdf/2507.07207"
          },
          {
            "title": "[2507.07207] Scale leads to compositional generalization",
            "url": "https://ar5iv.labs.arxiv.org/html/2507.07207"
          },
          {
            "title": "Scaling can lead to compositional generalization",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2025/hash/5047b64366bc0dbf5047de85f1e0c7be-Abstract-Conference.html"
          },
          {
            "title": "Scaling can lead to compositional generalization",
            "url": "https://arxiv.org/html/2507.07207"
          }
        ]
      },
      "Based on the search results, here's what I found about this paper:\n\nThe paper \"Scaling can lead to compositional generalization\" by Florian Redhardt, Yassir Akram, and Simon Schug (arXiv:2507.07207) is a NeurIPS 2025 Spotlight paper.\n\n**Key Findings:**\n\nThe paper finds that simply scaling data and model size leads to compositional generalization, and shows that this holds across different task encodings as long as the training distribution sufficiently covers the task space.\n\n**Theoretical Contribution:**\n\nThe authors prove that standard multilayer perceptrons can approximate a general class of compositional task families to arbitrary precision using only a linear number of neurons with respect to the number of task modules. This directly addresses the linear scaling aspect mentioned in your query.\n\nThe paper investigates how standard neural networks can capture discrete, compositional task structure and achieve compositional generalization through scaling, with empirical validation supporting the theoretical finding about linear scaling of MLPs in relation to task modules."
    ],
    "durationSeconds": 5.640644501999995,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "5ec7868f-4f99-4c90-81d0-2545b25b8a46",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-29T12:28:19.883Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HYQy3v8XcHQriUpybrbsse`</summary>

```json
{
  "query": "CHIMERA compact synthetic data arXiv 2603.00889 topic coverage reasoning performance 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4f2041c-8b95-4c13-89ed-3b0482a54523",
  "isSidechain": false,
  "requestId": "req_011CbWrqDwGFZwF7ffSqM9XJ",
  "type": "assistant",
  "uuid": "1f25b103-7f51-42e7-ab6c-bffef3dcab5d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R9pLe8Rw1CTf7Zdp7A6NFZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 680,
      "cache_read_input_tokens": 29367,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 680,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 29367,
          "cache_creation_input_tokens": 680,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 680
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

_source line 45 · 2026-05-29T12:28:27.090Z_

<details><summary>↩ Tool result · `toolu_01HYQy3v8XcHQriUpybrbsse`</summary>

```text
Web search results for query: "CHIMERA compact synthetic data arXiv 2603.00889 topic coverage reasoning performance 2026"

Links: [{"title":"[2603.00889] CHIMERA: Compact Synthetic Data for Generalizable LLM Reasoning","url":"https://arxiv.org/abs/2603.00889"},{"title":"[2603.00889v1] CHIMERA: Compact Synthetic Data for Generalizable LLM Reasoning","url":"https://arxiv.org/abs/2603.00889v1"},{"title":"Paper page - CHIMERA: Compact Synthetic Data for Generalizable LLM Reasoning","url":"https://huggingface.co/papers/2603.00889"},{"title":"Papers Explained 548: CHIMERA. CHIMERA is a compact synthetic… | by Ritvik Rastogi | Mar, 2026 | Medium","url":"https://ritvik19.medium.com/papers-explained-548-chimera-e3a368a1830c"},{"title":"CHIMERA: Compact Synthetic Data for Generalizable LLM Reasoning","url":"https://arxiv.org/pdf/2603.00889"},{"title":"CHIMERA: Compact Synthetic Data for Generalizable LLM Reasoning | Papers | HyperAI","url":"https://beta.hyper.ai/en/papers/2603.00889"},{"title":"Magnitude and Impact of Hallucinations in Tabular Synthetic Health Data on Prognostic Machine Learning Models: Validation Study","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12402739/"}]

Based on the search results, here's what I found about CHIMERA (arXiv 2603.00889):

## Overview

CHIMERA is a compact but high-difficulty synthetic reasoning dataset with long Chain-of-Thought trajectories and broad multi-disciplinary coverage, designed for reasoning post-training of large language models.

## Dataset Composition

CHIMERA contains 9,225 expert-level problems spanning 8 subjects (Mathematics, Computer Science, Chemistry, Physics, Literature, History, Biology, Linguistics) and 1,179 fine-grained topics, all synthesized by GPT-5.

## Problem Being Addressed

The research addresses three fundamental data-centric challenges: (1) the cold-start problem, arising from the lack of seed datasets with detailed, long Chain-of-Thought (CoT) trajectories needed to initialize reasoning policies; (2) limited domain coverage, as most existing open-source reasoning datasets are concentrated in mathematics, with limited coverage of broader scientific disciplines; and (3) the annotation bottleneck, where the difficulty of frontier-level reasoning tasks makes reliable human annotation prohibitively expensive or infeasible.

## Data Synthesis Pipeline

The data synthesis pipeline has three stages: stage 1 expands a small set of seed subjects into thousands of fine-grained topics; stage 2 creates well-defined problems with concise, verifiable answers based on these topics; stage 3 generates detailed reasoning trajectories.

The paper was submitted to arXiv on March 1, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1f25b103-7f51-42e7-ab6c-bffef3dcab5d",
  "isSidechain": false,
  "promptId": "e367c23d-5456-4f70-a5b3-3d1f58831111",
  "type": "user",
  "uuid": "00f2260b-ce88-4e39-9bca-d6957f626252",
  "toolUseResult": {
    "query": "CHIMERA compact synthetic data arXiv 2603.00889 topic coverage reasoning performance 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_015gCZhBuVV4e6yk74yADKS2",
        "content": [
          {
            "title": "[2603.00889] CHIMERA: Compact Synthetic Data for Generalizable LLM Reasoning",
            "url": "https://arxiv.org/abs/2603.00889"
          },
          {
            "title": "[2603.00889v1] CHIMERA: Compact Synthetic Data for Generalizable LLM Reasoning",
            "url": "https://arxiv.org/abs/2603.00889v1"
          },
          {
            "title": "Paper page - CHIMERA: Compact Synthetic Data for Generalizable LLM Reasoning",
            "url": "https://huggingface.co/papers/2603.00889"
          },
          {
            "title": "Papers Explained 548: CHIMERA. CHIMERA is a compact synthetic… | by Ritvik Rastogi | Mar, 2026 | Medium",
            "url": "https://ritvik19.medium.com/papers-explained-548-chimera-e3a368a1830c"
          },
          {
            "title": "CHIMERA: Compact Synthetic Data for Generalizable LLM Reasoning",
            "url": "https://arxiv.org/pdf/2603.00889"
          },
          {
            "title": "CHIMERA: Compact Synthetic Data for Generalizable LLM Reasoning | Papers | HyperAI",
            "url": "https://beta.hyper.ai/en/papers/2603.00889"
          },
          {
            "title": "Magnitude and Impact of Hallucinations in Tabular Synthetic Health Data on Prognostic Machine Learning Models: Validation Study",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12402739/"
          }
        ]
      },
      "Based on the search results, here's what I found about CHIMERA (arXiv 2603.00889):\n\n## Overview\n\nCHIMERA is a compact but high-difficulty synthetic reasoning dataset with long Chain-of-Thought trajectories and broad multi-disciplinary coverage, designed for reasoning post-training of large language models.\n\n## Dataset Composition\n\nCHIMERA contains 9,225 expert-level problems spanning 8 subjects (Mathematics, Computer Science, Chemistry, Physics, Literature, History, Biology, Linguistics) and 1,179 fine-grained topics, all synthesized by GPT-5.\n\n## Problem Being Addressed\n\nThe research addresses three fundamental data-centric challenges: (1) the cold-start problem, arising from the lack of seed datasets with detailed, long Chain-of-Thought (CoT) trajectories needed to initialize reasoning policies; (2) limited domain coverage, as most existing open-source reasoning datasets are concentrated in mathematics, with limited coverage of broader scientific disciplines; and (3) the annotation bottleneck, where the difficulty of frontier-level reasoning tasks makes reliable human annotation prohibitively expensive or infeasible.\n\n## Data Synthesis Pipeline\n\nThe data synthesis pipeline has three stages: stage 1 expands a small set of seed subjects into thousands of fine-grained topics; stage 2 creates well-defined problems with concise, verifiable answers based on these topics; stage 3 generates detailed reasoning trajectories.\n\nThe paper was submitted to arXiv on March 1, 2026."
    ],
    "durationSeconds": 7.203358825000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "1f25b103-7f51-42e7-ab6c-bffef3dcab5d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1",
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
  "lastPrompt": "# Skill-DAG-Guided Frontier Synthesis for Mathematical Compositional Generalization  ## Core Problem  LLMs exhibit a persistent compositional ceiling in mathematical reasoning: OMEGA (NeurIPS 2025, ar…",
  "leafUuid": "00f2260b-ce88-4e39-9bca-d6957f626252",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "ai-title",
  "aiTitle": "Skill-DAG-guided synthesis for math compositional generalization",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1"
}
```

---

### Tool call

_source line 48 · 2026-05-29T12:28:29.184Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016NcSLKeDjNJQzhZe9gmYAr`</summary>

```json
{
  "query": "FLAMES arXiv 2508.16514 math data synthesis fine-grained analysis coverage reliability tradeoff 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00f2260b-ce88-4e39-9bca-d6957f626252",
  "isSidechain": false,
  "requestId": "req_011CbWrqyBY4BW6h4BR6QgTu",
  "type": "assistant",
  "uuid": "7ae72313-061a-43ac-b6c9-b1025d8f680b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lrr6mhU9tGG3rmLfC5i685",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 842,
      "cache_read_input_tokens": 30047,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 842,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 30047,
          "cache_creation_input_tokens": 842,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 842
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

_source line 49 · 2026-05-29T12:28:36.764Z_

<details><summary>↩ Tool result · `toolu_016NcSLKeDjNJQzhZe9gmYAr`</summary>

```text
Web search results for query: "FLAMES arXiv 2508.16514 math data synthesis fine-grained analysis coverage reliability tradeoff 2025"

Links: [{"title":"[2508.16514] FLAMES: Improving LLM Math Reasoning via a Fine-Grained Analysis of the Data Synthesis Pipeline","url":"https://arxiv.org/abs/2508.16514"},{"title":"[2508.16514v1] FLAMES: Improving LLM Math Reasoning via a Fine-Grained Analysis of the Data Synthesis Pipeline","url":"https://arxiv.org/abs/2508.16514v1"},{"title":"[PDF] FLAMES: Improving LLM Math Reasoning via a Fine-Grained Analysis of the Data Synthesis Pipeline | Semantic Scholar","url":"https://www.semanticscholar.org/paper/FLAMES:-Improving-LLM-Math-Reasoning-via-a-Analysis-Seegmiller-Mehta/4a6fde5cc04a1dc9e2815c42bf0372ae36e1db45"},{"title":"FLAMES: Improving LLM Math Reasoning via a Fine-Grained Analysis of the Data Synthesis Pipeline - Paper Detail","url":"https://deeplearn.org/arxiv/632100/flames:-improving-llm-math-reasoning-via-a-fine-grained-analysis-of-the-data-synthesis-pipeline"},{"title":"FLAMES: Improving LLM Math Reasoning via a Fine- ...","url":"https://arxiv.org/pdf/2508.16514"},{"title":"(PDF) FLAMES: Improving LLM Math Reasoning via a Fine-Grained Analysis of the Data Synthesis Pipeline","url":"https://www.researchgate.net/publication/394921058_FLAMES_Improving_LLM_Math_Reasoning_via_a_Fine-Grained_Analysis_of_the_Data_Synthesis_Pipeline"},{"title":"dblp: FLAMES: Improving LLM Math Reasoning via a Fine-Grained Analysis of the Data Synthesis Pipeline.","url":"https://dblp.org/rec/journals/corr/abs-2508-16514.html"},{"title":"FLAMES: Improving LLM Math Reasoning via a Fine-Grained Analysis of the Data Synthesis Pipeline | Article Information | J-GLOBAL","url":"http://jglobal.jst.go.jp/en/public/202502214943193998"}]

I found the paper! Here are the key findings from the FLAMES research:

## Overview

FLAMES is a Framework for LLM Assessment of Math rEasoning Data Synthesis that performs a systematic study of 10 existing data synthesis strategies and multiple other factors impacting the performance of synthetic math reasoning data.

## Key Insights

The FLAMES experiments provide several valuable insights about the optimal balance of difficulty and diversity of synthetic data.

### Coverage vs. Reliability Tradeoff

The paper directly addresses the coverage-reliability tradeoff you mentioned: With a fixed data generation budget, keeping higher problem coverage is more important than keeping only problems with reliable solutions.

### Problem Complexity

Data agents designed to increase problem complexity lead to best improvements on most math metrics.

## Background

Recent works improving LLM math reasoning with synthetic data have used unique setups, making comparison of data synthesis strategies impractical, leaving many unanswered questions about the roles of different factors in the synthetic data pipeline, such as the impact of filtering low-quality problems.

The paper was submitted on August 22, 2025, and is authored by Parker Seegmiller, Kartik Mehta, Soumya Saha, Chenyang Tao, Shereen Oraby, Arpit Gupta, Tagyoung Chung, Mohit Bansal, and Nanyun Peng.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7ae72313-061a-43ac-b6c9-b1025d8f680b",
  "isSidechain": false,
  "promptId": "e367c23d-5456-4f70-a5b3-3d1f58831111",
  "type": "user",
  "uuid": "f7cd1acb-3256-4633-a958-895091dd061a",
  "toolUseResult": {
    "query": "FLAMES arXiv 2508.16514 math data synthesis fine-grained analysis coverage reliability tradeoff 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QtW77j3iutSdBbrdhDEUA6",
        "content": [
          {
            "title": "[2508.16514] FLAMES: Improving LLM Math Reasoning via a Fine-Grained Analysis of the Data Synthesis Pipeline",
            "url": "https://arxiv.org/abs/2508.16514"
          },
          {
            "title": "[2508.16514v1] FLAMES: Improving LLM Math Reasoning via a Fine-Grained Analysis of the Data Synthesis Pipeline",
            "url": "https://arxiv.org/abs/2508.16514v1"
          },
          {
            "title": "[PDF] FLAMES: Improving LLM Math Reasoning via a Fine-Grained Analysis of the Data Synthesis Pipeline | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/FLAMES:-Improving-LLM-Math-Reasoning-via-a-Analysis-Seegmiller-Mehta/4a6fde5cc04a1dc9e2815c42bf0372ae36e1db45"
          },
          {
            "title": "FLAMES: Improving LLM Math Reasoning via a Fine-Grained Analysis of the Data Synthesis Pipeline - Paper Detail",
            "url": "https://deeplearn.org/arxiv/632100/flames:-improving-llm-math-reasoning-via-a-fine-grained-analysis-of-the-data-synthesis-pipeline"
          },
          {
            "title": "FLAMES: Improving LLM Math Reasoning via a Fine- ...",
            "url": "https://arxiv.org/pdf/2508.16514"
          },
          {
            "title": "(PDF) FLAMES: Improving LLM Math Reasoning via a Fine-Grained Analysis of the Data Synthesis Pipeline",
            "url": "https://www.researchgate.net/publication/394921058_FLAMES_Improving_LLM_Math_Reasoning_via_a_Fine-Grained_Analysis_of_the_Data_Synthesis_Pipeline"
          },
          {
            "title": "dblp: FLAMES: Improving LLM Math Reasoning via a Fine-Grained Analysis of the Data Synthesis Pipeline.",
            "url": "https://dblp.org/rec/journals/corr/abs-2508-16514.html"
          },
          {
            "title": "FLAMES: Improving LLM Math Reasoning via a Fine-Grained Analysis of the Data Synthesis Pipeline | Article Information | J-GLOBAL",
            "url": "http://jglobal.jst.go.jp/en/public/202502214943193998"
          }
        ]
      },
      "I found the paper! Here are the key findings from the FLAMES research:\n\n## Overview\n\nFLAMES is a Framework for LLM Assessment of Math rEasoning Data Synthesis that performs a systematic study of 10 existing data synthesis strategies and multiple other factors impacting the performance of synthetic math reasoning data.\n\n## Key Insights\n\nThe FLAMES experiments provide several valuable insights about the optimal balance of difficulty and diversity of synthetic data.\n\n### Coverage vs. Reliability Tradeoff\n\nThe paper directly addresses the coverage-reliability tradeoff you mentioned: With a fixed data generation budget, keeping higher problem coverage is more important than keeping only problems with reliable solutions.\n\n### Problem Complexity\n\nData agents designed to increase problem complexity lead to best improvements on most math metrics.\n\n## Background\n\nRecent works improving LLM math reasoning with synthetic data have used unique setups, making comparison of data synthesis strategies impractical, leaving many unanswered questions about the roles of different factors in the synthetic data pipeline, such as the impact of filtering low-quality problems.\n\nThe paper was submitted on August 22, 2025, and is authored by Parker Seegmiller, Kartik Mehta, Soumya Saha, Chenyang Tao, Shereen Oraby, Arpit Gupta, Tagyoung Chung, Mohit Bansal, and Nanyun Peng."
    ],
    "durationSeconds": 7.575043318000011,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "7ae72313-061a-43ac-b6c9-b1025d8f680b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-29T12:28:39.151Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011DUzAy8fp4h6y96u4bMxK5`</summary>

```json
{
  "query": "\"Less is More\" arXiv 2504.14508 adaptive coverage synthetic training data maximum coverage subset selection 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7cd1acb-3256-4633-a958-895091dd061a",
  "isSidechain": false,
  "requestId": "req_011CbWrrgXCrEcgiiEY28dzq",
  "type": "assistant",
  "uuid": "7958301c-9304-489f-b3c8-55839449848f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XUH17fDZnfT6YdobqCcYdC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1011,
      "cache_read_input_tokens": 30889,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1011,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 78,
          "cache_read_input_tokens": 30889,
          "cache_creation_input_tokens": 1011,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1011
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

_source line 51 · 2026-05-29T12:28:45.753Z_

<details><summary>↩ Tool result · `toolu_011DUzAy8fp4h6y96u4bMxK5`</summary>

```text
Web search results for query: ""Less is More" arXiv 2504.14508 adaptive coverage synthetic training data maximum coverage subset selection 2025"

Links: [{"title":"[2504.14508] Less is More: Adaptive Coverage for Synthetic Training Data","url":"https://arxiv.org/abs/2504.14508"},{"title":"Less is More: Adaptive Coverage for Synthetic Training Data","url":"https://arxiv.org/html/2504.14508v2"},{"title":"Less is More: Adaptive Coverage for Synthetic Training Data Sasan Tavakkol","url":"https://arxiv.org/pdf/2504.14508"},{"title":"Machine Learning Apr 2025","url":"https://arxiv.org/list/cs.LG/2025-04?skip=1050&show=1000"},{"title":"Computer Science Apr 2025","url":"https://arxiv.org/list/cs/2025-04?skip=6850&show=50"},{"title":"SYNAPSE-G: Bridging Large Language Models and Graph Learning for Rare Event Classification","url":"https://arxiv.org/html/2508.09544v1"},{"title":"Less Is More: Adaptive Trainable Gradient Dropout for Deep Neural Networks","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9921448/"},{"title":"Ensembles of GANs for synthetic training data generation","url":"https://arxiv.org/pdf/2104.11797"},{"title":"Smaller, Weaker, Yet Better: Training LLM Reasoners via Compute-Optimal   Sampling","url":"https://arxiv.org/pdf/2408.16737"}]

Based on the search results, I found the paper "Less is More: Adaptive Coverage for Synthetic Training Data" (arXiv 2504.14508). Here's what I found:

## Overview

The paper addresses synthetic training data generation with Large Language Models (LLMs) like Google's Gemma and OpenAI's GPT as a solution for obtaining large, labeled datasets for training classifiers.

## Core Contribution

The study introduces a novel sampling algorithm, based on the maximum coverage problem, to select a representative subset from a synthetically generated dataset. Training a classifier on this contextually sampled subset achieves superior performance compared to training on the entire dataset.

## Key Results

This "less is more" approach not only improves model accuracy but also reduces the volume of data required, leading to potentially more efficient model fine-tuning.

## Authors

The authors are Sasan Tavakkol, Max Springer, Mohammadhossein Bateni, Neslihan Bulut, Vincent Cohen-Addad, and MohammadTaghi Hajiaghayi.

The paper was updated on July 24, 2025, and falls under the Machine Learning (cs.LG) category on arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7958301c-9304-489f-b3c8-55839449848f",
  "isSidechain": false,
  "promptId": "e367c23d-5456-4f70-a5b3-3d1f58831111",
  "type": "user",
  "uuid": "abb04f34-5546-442b-965a-327db789eef7",
  "toolUseResult": {
    "query": "\"Less is More\" arXiv 2504.14508 adaptive coverage synthetic training data maximum coverage subset selection 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_014S1rtLBmQjVMQWuUK6Tevo",
        "content": [
          {
            "title": "[2504.14508] Less is More: Adaptive Coverage for Synthetic Training Data",
            "url": "https://arxiv.org/abs/2504.14508"
          },
          {
            "title": "Less is More: Adaptive Coverage for Synthetic Training Data",
            "url": "https://arxiv.org/html/2504.14508v2"
          },
          {
            "title": "Less is More: Adaptive Coverage for Synthetic Training Data Sasan Tavakkol",
            "url": "https://arxiv.org/pdf/2504.14508"
          },
          {
            "title": "Machine Learning Apr 2025",
            "url": "https://arxiv.org/list/cs.LG/2025-04?skip=1050&show=1000"
          },
          {
            "title": "Computer Science Apr 2025",
            "url": "https://arxiv.org/list/cs/2025-04?skip=6850&show=50"
          },
          {
            "title": "SYNAPSE-G: Bridging Large Language Models and Graph Learning for Rare Event Classification",
            "url": "https://arxiv.org/html/2508.09544v1"
          },
          {
            "title": "Less Is More: Adaptive Trainable Gradient Dropout for Deep Neural Networks",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9921448/"
          },
          {
            "title": "Ensembles of GANs for synthetic training data generation",
            "url": "https://arxiv.org/pdf/2104.11797"
          },
          {
            "title": "Smaller, Weaker, Yet Better: Training LLM Reasoners via Compute-Optimal   Sampling",
            "url": "https://arxiv.org/pdf/2408.16737"
          }
        ]
      },
      "Based on the search results, I found the paper \"Less is More: Adaptive Coverage for Synthetic Training Data\" (arXiv 2504.14508). Here's what I found:\n\n## Overview\n\nThe paper addresses synthetic training data generation with Large Language Models (LLMs) like Google's Gemma and OpenAI's GPT as a solution for obtaining large, labeled datasets for training classifiers.\n\n## Core Contribution\n\nThe study introduces a novel sampling algorithm, based on the maximum coverage problem, to select a representative subset from a synthetically generated dataset. Training a classifier on this contextually sampled subset achieves superior performance compared to training on the entire dataset.\n\n## Key Results\n\nThis \"less is more\" approach not only improves model accuracy but also reduces the volume of data required, leading to potentially more efficient model fine-tuning.\n\n## Authors\n\nThe authors are Sasan Tavakkol, Max Springer, Mohammadhossein Bateni, Neslihan Bulut, Vincent Cohen-Addad, and MohammadTaghi Hajiaghayi.\n\nThe paper was updated on July 24, 2025, and falls under the Machine Learning (cs.LG) category on arXiv."
    ],
    "durationSeconds": 6.598381850000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "7958301c-9304-489f-b3c8-55839449848f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-29T12:28:48.068Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01U6sCRYshALg4UCi1y19Mf2`</summary>

```json
{
  "query": "compositional generalization math LLM 2026 new method skill combination structured synthesis beyond STEPS MathFusion"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "abb04f34-5546-442b-965a-327db789eef7",
  "isSidechain": false,
  "requestId": "req_011CbWrsLzjR7modMtHso74G",
  "type": "assistant",
  "uuid": "a3c2ae21-5747-4164-bad2-01f15ca50148",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RoAxjj5b6iA3kkUgFdsoUu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 790,
      "cache_read_input_tokens": 31900,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 790,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 31900,
          "cache_creation_input_tokens": 790,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 790
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

_source line 53 · 2026-05-29T12:28:55.721Z_

<details><summary>↩ Tool result · `toolu_01U6sCRYshALg4UCi1y19Mf2`</summary>

```text
Web search results for query: "compositional generalization math LLM 2026 new method skill combination structured synthesis beyond STEPS MathFusion"

Links: [{"title":"Towards Compositional Generalization of LLMs via Skill Taxonomy Guided Data Synthesis","url":"https://arxiv.org/pdf/2601.03676"},{"title":"Towards Compositional Generalization of LLMs via Skill Taxonomy Guided Data Synthesis","url":"https://arxiv.org/html/2601.03676"},{"title":"MathFusion: Enhancing Mathematical Problem-solving of LLM through Instruction Fusion","url":"https://arxiv.org/html/2503.16212v2"},{"title":"MathFusion: Enhancing Mathematic Problem-solving of LLM through Instruction Fusion","url":"https://arxiv.org/html/2503.16212v1"},{"title":"MathMixup: Boosting LLM Mathematical Reasoning with Difficulty-Controllable Data Synthesis and Curriculum Learning","url":"https://arxiv.org/html/2601.17006v1"}]

I found several relevant recent research papers on compositional generalization in math LLMs from 2025-2026. Here's what I discovered:

## STEPS Framework (January 2026)

STEPS is a Skill Taxonomy-guided Entropy-based Posttraining data Synthesis framework that addresses compositional generalization by uncovering latent relationships among skills and organizing them into an interpretable, hierarchical skill taxonomy using structural information theory. The framework formulates data synthesis as a constrained information maximization problem, selecting skill combinations that maximize marginal structural information within the hierarchy while preserving semantic coherence.

## MathFusion Framework (June 2025)

MathFusion is a novel framework that enhances mathematical reasoning by fusing different mathematical problems. The key insight is that strategic combination of complementary mathematical instructions can unlock deeper reasoning capabilities, with MathFusion synthesizing a new math problem that encapsulates the relational and compositional aspects of the original two problems. The framework uses three distinct fusion strategies: sequential, parallel, and conditional.

## MathMixup (January 2026)

MathMixup employs curriculum learning to improve performance, with Qwen2.5-7B reaching 47.60% accuracy and notable gains on challenging benchmarks such as OlympiadBench.

These methods represent recent advances in addressing compositional generalization in mathematical reasoning for LLMs through structured data synthesis and skill combination techniques.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a3c2ae21-5747-4164-bad2-01f15ca50148",
  "isSidechain": false,
  "promptId": "e367c23d-5456-4f70-a5b3-3d1f58831111",
  "type": "user",
  "uuid": "267cbe4f-7e97-43fb-8791-408da0f414a5",
  "toolUseResult": {
    "query": "compositional generalization math LLM 2026 new method skill combination structured synthesis beyond STEPS MathFusion",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GewBKL7Zx8UQWDfQpn2dy7",
        "content": [
          {
            "title": "Towards Compositional Generalization of LLMs via Skill Taxonomy Guided Data Synthesis",
            "url": "https://arxiv.org/pdf/2601.03676"
          },
          {
            "title": "Towards Compositional Generalization of LLMs via Skill Taxonomy Guided Data Synthesis",
            "url": "https://arxiv.org/html/2601.03676"
          },
          {
            "title": "MathFusion: Enhancing Mathematical Problem-solving of LLM through Instruction Fusion",
            "url": "https://arxiv.org/html/2503.16212v2"
          },
          {
            "title": "MathFusion: Enhancing Mathematic Problem-solving of LLM through Instruction Fusion",
            "url": "https://arxiv.org/html/2503.16212v1"
          },
          {
            "title": "MathMixup: Boosting LLM Mathematical Reasoning with Difficulty-Controllable Data Synthesis and Curriculum Learning",
            "url": "https://arxiv.org/html/2601.17006v1"
          }
        ]
      },
      "I found several relevant recent research papers on compositional generalization in math LLMs from 2025-2026. Here's what I discovered:\n\n## STEPS Framework (January 2026)\n\nSTEPS is a Skill Taxonomy-guided Entropy-based Posttraining data Synthesis framework that addresses compositional generalization by uncovering latent relationships among skills and organizing them into an interpretable, hierarchical skill taxonomy using structural information theory. The framework formulates data synthesis as a constrained information maximization problem, selecting skill combinations that maximize marginal structural information within the hierarchy while preserving semantic coherence.\n\n## MathFusion Framework (June 2025)\n\nMathFusion is a novel framework that enhances mathematical reasoning by fusing different mathematical problems. The key insight is that strategic combination of complementary mathematical instructions can unlock deeper reasoning capabilities, with MathFusion synthesizing a new math problem that encapsulates the relational and compositional aspects of the original two problems. The framework uses three distinct fusion strategies: sequential, parallel, and conditional.\n\n## MathMixup (January 2026)\n\nMathMixup employs curriculum learning to improve performance, with Qwen2.5-7B reaching 47.60% accuracy and notable gains on challenging benchmarks such as OlympiadBench.\n\nThese methods represent recent advances in addressing compositional generalization in mathematical reasoning for LLMs through structured data synthesis and skill combination techniques."
    ],
    "durationSeconds": 7.648371114000009,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "a3c2ae21-5747-4164-bad2-01f15ca50148",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 54 · 2026-05-29T12:28:55.724Z_

```json
{
  "parentUuid": "267cbe4f-7e97-43fb-8791-408da0f414a5",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "f6d8c54c-d214-4364-9b19-0ee6b396d080",
  "timestamp": "2026-05-29T12:28:55.724Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 55 · 2026-05-29T12:28:58.599Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012qLPfEaK3L5Mudju9EpnS9`</summary>

```json
{
  "query": "Graph of Skills arXiv 2604.05333 dependency-aware structural retrieval skill DAG prerequisite 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6d8c54c-d214-4364-9b19-0ee6b396d080",
  "isSidechain": false,
  "requestId": "req_011CbWrt5aokNALtdTJ594gj",
  "type": "assistant",
  "uuid": "20951af3-7a11-4538-89c0-2d53d332b81b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dktca2xGw9KvtYHn2Tecu7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 789,
      "cache_read_input_tokens": 32690,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 789,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 78,
          "cache_read_input_tokens": 32690,
          "cache_creation_input_tokens": 789,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 789
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

_source line 56 · 2026-05-29T12:29:06.862Z_

<details><summary>↩ Tool result · `toolu_012qLPfEaK3L5Mudju9EpnS9`</summary>

```text
Web search results for query: "Graph of Skills arXiv 2604.05333 dependency-aware structural retrieval skill DAG prerequisite 2026"

Links: [{"title":"[2604.05333] Graph-of-Skills: Dependency-Aware Structural Retrieval for Massive Agent Skills","url":"https://arxiv.org/abs/2604.05333"},{"title":"Paper page - Graph of Skills: Dependency-Aware Structural Retrieval for Massive Agent Skills","url":"https://huggingface.co/papers/2604.05333"},{"title":"GitHub - davidliuk/graph-of-skills: Dependency-Aware Structural Retrieval for Massive Agent Skills · GitHub","url":"https://github.com/davidliuk/graph-of-skills"},{"title":"Graph-of-Skills: Dependency-Aware Structural Retrieval for Massive Agent Skills","url":"https://arxiv.org/html/2604.05333"},{"title":"graph-of-skills - AI Agents","url":"https://skillsllm.com/skill/graph-of-skills"},{"title":"Graph of Skills: Dependency-Aware Structural Retrieval for Massive Agent Skills","url":"https://arxiv.org/pdf/2604.05333"},{"title":"From Skill Text to Skill Structure: The Scheduling-Structural-Logical Representation for Agent Skills","url":"https://arxiv.org/html/2604.24026v1"}]

Based on the search results, I found comprehensive information about the paper you're looking for:

## Graph-of-Skills: Dependency-Aware Structural Retrieval

Graph-of-Skills (GoS) is an inference-time structural retrieval layer for large skill libraries that constructs an executable skill graph offline from skill packages, then at inference time retrieves a bounded, dependency-aware skill bundle through hybrid semantic-lexical seeding, reverse-aware Personalized PageRank, and context-budgeted hydration.

### Problem Being Solved

Scaling to larger skill sets introduces two key challenges: first, loading the full skill set saturates the context window, driving up token costs, hallucination, and latency; second, semantic retrieval surfaces topically relevant skills but misses their prerequisite chain of upstream and downstream skills, creating a prerequisite gap that leaves the retrieved bundle execution-incomplete.

### Performance Results

On SkillsBench and ALFWorld, GoS improves average reward by 43.6% over the vanilla full skill-loading baseline while reducing input tokens by 37.8%, and generalizes across three model families: Claude Sonnet, GPT-5.2 Codex, and MiniMax.

### Paper Details

The paper (arXiv:2604.05333) was submitted on April 7, 2026, with the latest version (v3) revised on May 27, 2026. The authors are Dawei Liu, Zongxia Li, Hongyang Du, Xiyang Wu, Shihang Gui, Yongbei Kuang, and Lichao Sun from the University of Pennsylvania, University of Maryland, Brown University, Carnegie Mellon University, and Lehigh University.

You can find the code on [GitHub](https://github.com/davidliuk/graph-of-skills) and the full paper on [arXiv](https://arxiv.org/abs/2604.05333).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "20951af3-7a11-4538-89c0-2d53d332b81b",
  "isSidechain": false,
  "promptId": "e367c23d-5456-4f70-a5b3-3d1f58831111",
  "type": "user",
  "uuid": "27060aab-5330-492e-8d57-fd6f16a31518",
  "toolUseResult": {
    "query": "Graph of Skills arXiv 2604.05333 dependency-aware structural retrieval skill DAG prerequisite 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EoJj56f3rgNDYYNh7YjAo4",
        "content": [
          {
            "title": "[2604.05333] Graph-of-Skills: Dependency-Aware Structural Retrieval for Massive Agent Skills",
            "url": "https://arxiv.org/abs/2604.05333"
          },
          {
            "title": "Paper page - Graph of Skills: Dependency-Aware Structural Retrieval for Massive Agent Skills",
            "url": "https://huggingface.co/papers/2604.05333"
          },
          {
            "title": "GitHub - davidliuk/graph-of-skills: Dependency-Aware Structural Retrieval for Massive Agent Skills · GitHub",
            "url": "https://github.com/davidliuk/graph-of-skills"
          },
          {
            "title": "Graph-of-Skills: Dependency-Aware Structural Retrieval for Massive Agent Skills",
            "url": "https://arxiv.org/html/2604.05333"
          },
          {
            "title": "graph-of-skills - AI Agents",
            "url": "https://skillsllm.com/skill/graph-of-skills"
          },
          {
            "title": "Graph of Skills: Dependency-Aware Structural Retrieval for Massive Agent Skills",
            "url": "https://arxiv.org/pdf/2604.05333"
          },
          {
            "title": "From Skill Text to Skill Structure: The Scheduling-Structural-Logical Representation for Agent Skills",
            "url": "https://arxiv.org/html/2604.24026v1"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about the paper you're looking for:\n\n## Graph-of-Skills: Dependency-Aware Structural Retrieval\n\nGraph-of-Skills (GoS) is an inference-time structural retrieval layer for large skill libraries that constructs an executable skill graph offline from skill packages, then at inference time retrieves a bounded, dependency-aware skill bundle through hybrid semantic-lexical seeding, reverse-aware Personalized PageRank, and context-budgeted hydration.\n\n### Problem Being Solved\n\nScaling to larger skill sets introduces two key challenges: first, loading the full skill set saturates the context window, driving up token costs, hallucination, and latency; second, semantic retrieval surfaces topically relevant skills but misses their prerequisite chain of upstream and downstream skills, creating a prerequisite gap that leaves the retrieved bundle execution-incomplete.\n\n### Performance Results\n\nOn SkillsBench and ALFWorld, GoS improves average reward by 43.6% over the vanilla full skill-loading baseline while reducing input tokens by 37.8%, and generalizes across three model families: Claude Sonnet, GPT-5.2 Codex, and MiniMax.\n\n### Paper Details\n\nThe paper (arXiv:2604.05333) was submitted on April 7, 2026, with the latest version (v3) revised on May 27, 2026. The authors are Dawei Liu, Zongxia Li, Hongyang Du, Xiyang Wu, Shihang Gui, Yongbei Kuang, and Lichao Sun from the University of Pennsylvania, University of Maryland, Brown University, Carnegie Mellon University, and Lehigh University.\n\nYou can find the code on [GitHub](https://github.com/davidliuk/graph-of-skills) and the full paper on [arXiv](https://arxiv.org/abs/2604.05333)."
    ],
    "durationSeconds": 8.258755225000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "20951af3-7a11-4538-89c0-2d53d332b81b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 57 · 2026-05-29T12:29:53.164Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive picture of the research landscape. Let me synthesize my findings and assess this proposal.

Key findings from my research:

1. **OMEGA** (NeurIPS 2025): Establishes the compositional ceiling problem - GRPO helps exploratory but not compositional generalization. This is the key benchmark the proposal targets.

2. **STEPS** (Jan 2026): The most directly comparable work - uses skill taxonomy with structural entropy for compositional generalization. Key differences from the proposal: (a) uses co-occurrence graph, not prerequisite DAG; (b) optimizes entropy, not explicit coverage gaps; (c) validated on instruction-following benchmarks, not math reasoning.


3. **MathFusion** (ACL 2025) composes math problems without skill-graph guidance using random strategies, while **STAT** (ICLR 2026) addresses individual skill deficiencies rather than compositions. **Agentic Proposing** (Feb 2026) achieves strong results on AIME25 but optimizes difficulty rather than coverage. **MindLoom** (May 2026) is conceptually similar with its thought-mode composition and scarcity rewards, though it relies on implicit RL signals instead of explicit DAG-guided gap targeting.

**MASS** (ICML 2025) uses skill graphs for data selection rather than synthesis, while **Redhardt et al.** (NeurIPS 2025 Spotlight) provides theoretical grounding that coverage enables compositional generalization. **CHIMERA** (Mar 2026) shows compact high-coverage data can match frontier performance, but its coverage focuses on topic diversity rather than compositional skill pairs. **FLAMES** (Aug 2025) confirms coverage matters more than reliability in math synthesis, and **Graph-of-Skills** (Apr 2026) validates that prerequisite DAGs are valuable for agent skill retrieval, though not for training data synthesis. **"Less is More"** (Apr 2025) uses coverage-based subset selection rather than synthesis.

Now I'm assessing the novelty of the proposal itself.

The core innovation is using a prerequisite DAG to explicitly identify coverage gaps and guide compositional synthesis. Checking against prior work: STEPS uses entropy-based optimization over co-occurrence taxonomies rather than explicit gap targeting on a DAG, MathFusion relies on random composition without graph guidance, STAT targets individual skills not pairs, MindLoom uses implicit scarcity rewards, and Graph-of-Skills applies DAGs at inference time for retrieval rather than training data synthesis. The specific combination of prerequisite DAG structure plus explicit coverage-gap identification plus targeted compositional synthesis plus evaluation on compositional generalization benchmarks appears genuinely novel—no existing work combines all these elements.

That said, I need to evaluate how much this represents true novelty versus incremental progress over existing approaches. STEPS, since STEPS is the closest concurrent work. The key differences:
1. DAG vs. co-occurrence taxonomy: The proposal uses prerequisite relationships (directed, causal), while STEPS uses co-occurrence patterns (undirected, statistical).
2. Coverage gap targeting vs. entropy maximization: Different optimization objectives.
3. Math reasoning vs. instruction following: Different domains.
4. Symbolic verification: The proposal leverages OMEGA's verifiers.

**Significance Assessment:**
The compositional ceiling is a real and well-documented problem. Breaking it would be significant. The proposal is well-motivated by OMEGA's empirical findings and Redhardt et al.'s theoretical results.

**Potential Issues:**
The proposal is somewhat incremental — it's essentially "use prerequisite DAG to identify gaps and fill them" which, while novel in specifics, is conceptually predictable given MASS + OMEGA + STEPS exist. With only 40 templates, the compositional space is relatively small (780 pairs), so the real question is whether targeted gap-filling actually outperforms random coverage at this scale. H2+ about DAG structure providing signal is the sharpest contribution, but it hinges on ablation A1 confirming that prerequisite relationships genuinely matter more than random graph connectivity.

The most promising angle is reframing the core claim: instead of emphasizing coverage-gap targeting broadly, the real novelty lies in using prerequisite structure as a predictive signal for where coverage matters most. That's H2+, and if it holds, it becomes the centerpiece rather than a secondary hypothesis. The question is whether there's still real discovery space here or if the proposal has already converged. Looking at the structure and depth, it feels fairly mature, but I can see a few angles that could push it further — particularly elevating H2+ as the core finding, sharpening the connection to prerequisite structure as a predictive signal, and making sure the coverage analysis itself reads as a standalone contribution rather than just scaffolding for the method.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27060aab-5330-492e-8d57-fd6f16a31518",
  "isSidechain": false,
  "requestId": "req_011CbWrtuDk7i3mYpcwYq5zD",
  "type": "assistant",
  "uuid": "c0d12e21-cd1a-4332-ab0c-c287421ea26d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017u4Y4k624H8byaXtPpdCaH",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 895,
      "cache_read_input_tokens": 33479,
      "output_tokens": 6382,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 895,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6382,
          "cache_read_input_tokens": 33479,
          "cache_creation_input_tokens": 895,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 895
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

_source line 58 · 2026-05-29T12:31:38.854Z_

Now I have sufficient research to make my assessment. Let me compile my analysis.

---

【状态】: 有发掘空间

【前置调研发现】
- [OMEGA: Can LLMs Reason Outside the Box in Math?](https://arxiv.org/abs/2506.18880) (NeurIPS 2025): 建立了 compositional ceiling 的实证基线——GRPO 提升 exploratory +38pp 但 compositional 零增益。这是本 proposal 的核心出发点，定义了目标基准。
- [STEPS: Skill Taxonomy Guided Data Synthesis](https://arxiv.org/abs/2601.03676) (arXiv Jan 2026): 最直接的竞争者。用 structural information theory 构建 co-occurrence taxonomy，通过 entropy maximization 选择 skill 组合。关键区别：(1) co-occurrence graph（无向、统计）vs. prerequisite DAG（有向、因果）；(2) 优化 entropy vs. 显式 coverage gap；(3) 验证在 instruction-following benchmark 而非 math reasoning。
- [MindLoom: Composing Thought Modes](https://arxiv.org/abs/2605.21630) (arXiv May 2026): 将 thought modes 视为 atomic 组件并通过 scarcity reward 鼓励 rare combinations。概念上与 coverage gap 相关，但使用隐式 RL 信号而非显式 DAG 引导，且不建模 prerequisite 结构。
- [Graph-of-Skills: Dependency-Aware Structural Retrieval](https://arxiv.org/abs/2604.05333) (arXiv Apr 2026): 在 agent skill retrieval 场景中构建 prerequisite DAG，证明 prerequisite structure 对 skill composition 有实际价值（reward +43.6%）。但用于 inference-time retrieval，非 training data synthesis。这为"prerequisite 结构是 informative signal"提供了独立的跨域验证。
- [Agentic Proposing](https://arxiv.org/abs/2602.03279) (arXiv Feb 2026): 91.6% AIME25，但核心优化轴是 difficulty 而非 coverage，不建模 skill 间依赖关系。
- [Scaling can lead to compositional generalization](https://arxiv.org/abs/2507.07207) (NeurIPS 2025 Spotlight): 理论证明 MLP 可在 linear neuron scaling 下逼近 compositional task families，**前提是训练分布充分覆盖 task space**。这是 H1 的理论锚点。
- [CHIMERA](https://arxiv.org/abs/2603.00889) (arXiv Mar 2026): 9K problems 覆盖 1,179 topics 匹配 frontier 性能，但其 coverage 是 topic diversity 而非 compositional skill-pair structure。
- [FLAMES](https://arxiv.org/abs/2508.16514) (arXiv Aug 2025): 系统研究发现"coverage > reliability"在 math data synthesis 中成立。
- [MASS](https://arxiv.org/abs/2503.14917) (ICML 2025): 46K-skill co-occurrence graph 用于 data selection（50-70% token 效率增益），但未用于 synthesis 或 gap identification。
- 调研总结：这个领域当前的研究者在两条线上推进——一是结构化 skill representation 用于 data 操作（MASS 选择、STEPS entropy、GoS 检索），二是 compositional synthesis 用于 reasoning 增强（MathFusion 融合、Agentic Proposing 难度、MindLoom 稀缺性）。**本 proposal 的独特位置在于将"结构化 skill graph"线与"compositional synthesis"线在 prerequisite DAG + coverage gap 这个交汇点连接**，这个连接尚未被任何已有工作实现。

---

【发掘点 1】
- 维度: 核心 claim 强化 / novelty 锐化
- 内容: **H2+ 应提升为 primary hypothesis，而非 secondary。** 当前 proposal 将 H2+（"DAG structure specifically predicts where coverage gaps are most harmful"）定位为 mechanistic sub-hypothesis，在叙事中低于 H2（"targeted > random"）。但从 novelty 角度分析：H2 本身——"targeted coverage beats random coverage"——虽然有价值但 surprise value 不高，审稿人的直觉反应很可能是 "I would have guessed this"；而 H2+——"prerequisite DAG structure causally constrains compositional learning, making DAG-connected gap-filling superior to arbitrary-graph-connected gap-filling"——才是真正 surprising 且 non-obvious 的 claim。如果 H2+ 成立，其理论含义远大于 H2：它意味着 skill 间的因果依赖关系不仅存在于认知层面，还直接约束了 neural network 的 compositional learning dynamics，这连接到 Redhardt et al. 的理论但添加了一个全新的结构性维度（他们证明 coverage 够就行，但没有说哪种 coverage pattern 更高效）。

  **具体建议：** 将论文的 primary contribution 重新定位为"prerequisite structure as a predictive signal for compositional learning efficiency"，H2 降为 supporting evidence（targeted > random 自然成立），H2+ 升为 primary novel claim。标题也可以考虑更多体现 prerequisite structure 的中心地位，而非仅仅 "DAG-guided"。
- 价值: 直接提升 Novelty 天花板。当前 framing 下核心贡献是"用 DAG 填 gap 比 random 好"（incremental），重新 framing 后核心贡献是"prerequisite structure 是 compositional learning 的因果约束因素"（mechanistic insight），后者的学术影响力和 surprise value 显著更高。
- 调研依据: 参考 Graph-of-Skills (arXiv:2604.05333) 提供的独立证据——prerequisite structure 在 inference-time skill retrieval 中已被证明有价值（+43.6% reward），本 proposal 若能证明它在 training-time compositional learning 中同样有因果作用，则构成一个跨 inference/training 的统一发现，impact 显著扩大。

【发掘点 2】
- 维度: significance 提升 / related work 差异化
- 内容: **与 Graph-of-Skills 建立显式的 training-inference 对称性叙事。** GoS (arXiv:2604.05333, Apr 2026) 证明了 prerequisite DAG 在 inference-time 的 skill retrieval 中有重要作用——missing prerequisites 导致 execution-incomplete 的 skill bundle。本 proposal 的核心 claim 可以被框架为对称命题：如果 prerequisite structure 在 inference 时决定了 skill composition 的成功率，那么在 training 时它也应该决定 compositional learning 的效率。这不是简单类比——GoS 的发现为本 proposal 的假设提供了独立的 motivation 和 plausibility argument。

  **具体建议：** 在 Introduction 或 Research Landscape 中加入一段论述："Recently, Graph-of-Skills (2026) demonstrated that prerequisite structure is critical for composing skills at inference time—missing prerequisites lead to execution-incomplete skill bundles. We hypothesize the training-time analogue: coverage gaps along prerequisite edges are disproportionately harmful for compositional learning. If confirmed, this establishes prerequisite structure as a domain-general organizing principle for compositional AI, spanning both data curation and runtime orchestration."
- 价值: 提升 Significance。当前 proposal 的 impact story 局限于"math reasoning 的 SFT data curation"。引入 GoS 的 training-inference 对称性后，impact story 扩展为"prerequisite structure as a general principle for compositional AI"，这对审稿人的说服力显著不同。同时加强了 Related Work 差异化——明确 GoS 是互补验证而非竞争者。
- 调研依据: 直接参考 Graph-of-Skills (arXiv:2604.05333)——其核心发现是 "prerequisite gap leads to execution-incomplete bundles"，这与本 proposal 的 "coverage gap along DAG edges leads to compositional learning failure" 形成精确对称。

【发掘点 3】
- 维度: trivial alternative 威胁
- 内容: **需要正面回应一个 trivial alternative：如果 OMEGA 只有 40 个 template，全量覆盖 C(40,2)=780 个 pair 的成本是否已经足够低，使得"targeted gap-filling"失去必要性？** 这是审稿人最可能提出的第一个质疑：在一个只有 780 个 pair 的空间里，"targeted"相对于"exhaustive"的优势不明显——直接生成覆盖所有 780 个 pair 的数据，每个 pair 生成 5-10 个样本，总量也就 4K-8K，成本极低。proposal 提到了"each template contains parameterized sub-dimensions"来论证 effective space 更大，但这个论点在当前文本中不够有力。

  **具体建议：** (a) 在 Step 2 中定量展示 effective compositional space 的实际大小——不仅仅提到 sub-dimensions 存在，而是给出估算。例如，如果每个 template 有 5 个难度级别和 3 个子类型，effective space 就是 C(40×5×3, 2) = C(600, 2) ≈ 180K，这个规模下 targeted 才有真正的 value proposition。(b) 更根本地，将 OMEGA 40-template 明确定位为 **controlled testbed**——方法论的 scalability 价值在于当 skill ontology 扩展到 MASS 的 46K-skill 规模时，exhaustive coverage 不再可行，targeted gap-filling 成为必须。在 Scalability Note 中已经提到，但应该在 motivation 部分更前置地强调。(c) 设计实验时，可以在 5K budget 下对比 "targeted 5K vs. exhaustive 780-pair × ~6 samples ≈ 5K"，直接回应这个 trivial alternative。
- 价值: 消除 Novelty 的最大威胁。如果审稿人认为"在 780-pair 空间里直接全覆盖就行了"，H2 的 value proposition 直接瓦解。正面回应这个问题是保护核心 claim 的必要步骤。
- 调研依据: 基于领域整体趋势判断——CHIMERA (arXiv:2603.00889) 用 9K samples 覆盖 1,179 topics 达到 frontier 性能，这暗示在 compact skill space 里 exhaustive coverage 可能已经够用；MASS 的 46K-skill graph 则代表了真正需要 targeted approach 的规模。proposal 需要在这两个极端之间清晰定位。

【发掘点 4】
- 维度: novelty 锐化 / 前提假设质疑
- 内容: **Pilot coverage analysis 的贡献被严重低估——它可能是论文最有影响力的 empirical contribution 之一，但当前只被当作 pre-experiment 附属品。** 具体来说，如果 pilot analysis 揭示了以下任何 pattern，它本身就是一个重要发现：(a) existing math training data 的 compositional coverage 呈现系统性偏差（cross-domain pairs 被严重欠覆盖）；(b) coverage sparsity 与 prerequisite chain depth 存在相关性（更长的依赖链导致更稀疏的覆盖）；(c) 覆盖率与模型的 compositional failure rate 存在 strong correlation。这些发现独立于 SkillDAG-Synth 方法本身的成功与否都有价值，因为它们回答了一个之前没有人定量回答过的问题："existing math training data 的 compositional coverage landscape 长什么样？"

  **同时需要审视一个前提假设：** proposal 假设 OMEGA 的 40 template 之间存在足够多的 meaningful prerequisite relationships 来构建一个 non-trivial DAG。如果大部分 template 之间是平行的（没有 prerequisite 关系），DAG 就退化为一个很稀疏的图，"DAG-guided" 的信号就很弱。建议在 pilot study 中报告 DAG 的 density（|edges| / |possible edges|）和 structure metrics（longest path, average in-degree）来验证这个前提。

  **具体建议：** 将 pilot coverage analysis 升格为论文的一个 standalone contribution（例如在 contribution list 中单独列出"the first quantitative characterization of the compositional coverage landscape in math training data"），而不仅仅是 method pipeline 的一个步骤。
- 价值: 提升 Significance。即使主方法的效果 marginal，coverage landscape characterization 本身也为领域提供了可引用的诊断工具和实证基准。这等于给论文增加了一个"保底贡献"维度——降低了论文价值对主实验 effect size 的依赖。同时，验证 DAG density 的前提假设也保护了核心 claim 的逻辑完整性。
- 调研依据: 参考 FLAMES (arXiv:2508.16514) 的研究范式——它通过系统性诊断 data synthesis pipeline 中的各因素贡献，即使没有提出新方法，本身的分析发现也具有高引用价值。本 proposal 的 pilot coverage analysis 可以类似定位。

【发掘点 5】
- 维度: 核心 claim 强化
- 内容: **当前理论 grounding 有一个 gap：Redhardt et al. 证明了 coverage 足够就能 generalize，但没有证明 targeted coverage 比 random coverage 更 efficient。proposal 的 H2 是纯 empirical claim，缺乏理论 argument 解释 why targeted should beat random。** 可以补强这个逻辑链：

  **可能的理论 argument（informal）：** 如果 skill i 是 skill j 的 prerequisite，那么 composition (i, j) 的学习难度可能低于 composition (i, k) where k 与 i 无 prerequisite 关系——因为 prerequisite 意味着存在 shared computational subroutine，模型只需要学习如何 compose 而非同时学习两个 independent skills。因此，DAG-connected pairs 的 learning curve 应该更 steep（每 sample 带来的 generalization gain 更大），这解释了为什么优先覆盖 DAG-connected gaps 更 efficient。

  这不需要 formal proof，但如果在 motivation 中提供这种 informal theoretical argument，它会显著加强 H2+ claim 的 plausibility，让审稿人在看到实验结果之前就认为"这 makes sense"。
- 价值: 加强 Novelty 和 Significance。将核心 claim 从"pure empirical finding"升级为"theoretically motivated empirical finding"，提高审稿人对结果的预期和信任度。
- 调研依据: 参考 Redhardt et al. (arXiv:2507.07207) 的理论框架——其证明依赖于 training distribution 覆盖 task space，但未区分 structured coverage 和 uniform coverage。本建议是在其理论框架上做自然延伸，提出 structured coverage 更高效的 informal argument。

Sources:
- [OMEGA: Can LLMs Reason Outside the Box in Math?](https://arxiv.org/abs/2506.18880)
- [STEPS: Towards Compositional Generalization of LLMs via Skill Taxonomy Guided Data Synthesis](https://arxiv.org/abs/2601.03676)
- [MindLoom: Composing Thought Modes for Frontier-Level Reasoning Data Synthesis](https://arxiv.org/abs/2605.21630)
- [Graph-of-Skills: Dependency-Aware Structural Retrieval for Massive Agent Skills](https://arxiv.org/abs/2604.05333)
- [Agentic Proposing: Enhancing Large Language Model Reasoning via Compositional Skill Synthesis](https://arxiv.org/abs/2602.03279)
- [Scaling can lead to compositional generalization](https://arxiv.org/abs/2507.07207)
- [CHIMERA: Compact Synthetic Data for Generalizable LLM Reasoning](https://arxiv.org/abs/2603.00889)
- [FLAMES: Improving LLM Math Reasoning via a Fine-Grained Analysis of the Data Synthesis Pipeline](https://arxiv.org/abs/2508.16514)
- [MASS: Mathematical Data Selection via Skill Graphs for Pretraining LLMs](https://arxiv.org/abs/2503.14917)
- [MathFusion: Enhancing Mathematical Problem-solving of LLM through Instruction Fusion](https://arxiv.org/abs/2503.16212)
- [Less is More: Adaptive Coverage for Synthetic Training Data](https://arxiv.org/abs/2504.14508)
- [STAT: Skill-Targeted Adaptive Training](https://arxiv.org/abs/2510.10023)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0d12e21-cd1a-4332-ab0c-c287421ea26d",
  "isSidechain": false,
  "requestId": "req_011CbWrtuDk7i3mYpcwYq5zD",
  "type": "assistant",
  "uuid": "995ec918-b29f-4c3e-82af-fd56b6c81588",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017u4Y4k624H8byaXtPpdCaH",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 895,
      "cache_read_input_tokens": 33479,
      "output_tokens": 6382,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 895,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6382,
          "cache_read_input_tokens": 33479,
          "cache_creation_input_tokens": 895,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 895
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

_source line 59_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Skill-DAG-Guided Frontier Synthesis for Mathematical Compositional Generalization  ## Core Problem  LLMs exhibit a persistent compositional ceiling in mathematical reasoning: OMEGA (NeurIPS 2025, ar…",
  "leafUuid": "995ec918-b29f-4c3e-82af-fd56b6c81588",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1"
}
```

---

### Runtime record

_source line 60_

```json
{
  "type": "ai-title",
  "aiTitle": "Skill-DAG-guided synthesis for math compositional generalization",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1"
}
```

---

### Runtime record

_source line 61_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Skill-DAG-Guided Frontier Synthesis for Mathematical Compositional Generalization  ## Core Problem  LLMs exhibit a persistent compositional ceiling in mathematical reasoning: OMEGA (NeurIPS 2025, ar…",
  "leafUuid": "995ec918-b29f-4c3e-82af-fd56b6c81588",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1"
}
```

---

### Runtime record

_source line 62_

```json
{
  "type": "ai-title",
  "aiTitle": "Skill-DAG-guided synthesis for math compositional generalization",
  "sessionId": "63c5bdd6-ccb7-41cc-9fed-0d4186b6b9a1"
}
```

---
