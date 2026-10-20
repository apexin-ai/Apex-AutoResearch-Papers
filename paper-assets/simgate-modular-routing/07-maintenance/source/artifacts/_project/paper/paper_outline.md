# EMNLP 2026 Short Paper Outline

## Title Candidates

1. **Death Avoidance Dominates Routing Signal: A Counterfactual Analysis of LLM Agent Tool Use in Interactive Environments**
2. **When Does Deterministic Computation Help LLM Agents? Episode-Level Counterfactual Analysis Reveals Death Avoidance Dominance**
3. **90% Death Avoidance: Decomposing the Routing Signal Between LLM Reasoning and Deterministic Simulation**

Recommended: **Title 1** (clear claim + methodology in title; fits short paper convention of stating the finding)

---

## Abstract Skeleton (~150 words)

Key points to cover:

- **Problem**: LLM agents hallucinate state transitions in rule-governed environments, causing catastrophic failures (deaths). Routing between internal LLM reasoning and deterministic computation (simulators) can mitigate this, but what exactly does routing learn?
- **Methodological gap**: Per-step oracle labeling degenerates in sparse-reward settings (98% tie rate on ScienceWorld). We propose episode-level counterfactual analysis.
- **Core finding**: Death avoidance accounts for ~90% of routing signal (Δ_full=+29.60, Δ_no_death=+2.84, DAF=90.41%; Pearson r=0.97, p<1e-6 across 11 task types / 245 episodes) [A: plan-012-full, 245eps/11tasks]. Non-death performance is approximately equal between modalities.
- **Supporting finding**: Keyword heuristics structurally fail (match rates degenerate to ≈always-det or ≈always-internal); episode-level counterfactual labels can train a lightweight router (internal_recall=51.5%).
- **Implication**: The value of deterministic computation in interactive environments is concentrated in catastrophic failure prevention, not positive task guidance.

---

## Section Structure

### 1. Introduction (0.8 pages)

**Key points:**
- LLM agents on rule-governed environments (physics, chemistry) suffer catastrophic failures from hallucinated state transitions → motivate the routing question
- Existing work: tool-use learning (Toolformer, ART, Chameleon) learns *when* to invoke tools but doesn't analyze *what* routing learns; ITP-R routes to approximate world models but underperforms pure internal reasoning; ReTool/AgentMath use implicit routing entangled with backbone
- Per-step oracle labeling degenerates in sparse-reward environments (98% tie rate) → need episode-level analysis
- **Contributions** (bulleted):
  1. Episode-level counterfactual methodology that overcomes per-step oracle degeneracy
  2. Empirical finding: death avoidance accounts for ≥90% of routing signal on ScienceWorld (11 tasks, 245 episodes) [A: plan-012-full, 245eps/11tasks]
  3. Structural failure analysis of keyword heuristics; demonstration that counterfactual labels can train a lightweight diagnostic router

### 2. Method (1.0 pages)

**Key points:**
- **2.1 Problem Setup**: ScienceWorld environment; two computation modalities (internal LLM reasoning vs. deterministic simulation via environment forking); per-step routing decision
- **2.2 Episode-Level Counterfactual Labeling**: Why per-step oracle fails (98% tie rate in sparse rewards) → run complete episodes under pure-internal and pure-deterministic strategies → compare episode-level scores → label: det-preferred / internal-preferred / no-preference. Distribution: 86 det-pref / 9 int-pref / 150 no-pref (245 episodes) [A: plan-012-full, 245eps/11tasks]
- **2.3 Death Decomposition Framework**: Decompose Δ_full into death-avoidance component (Δ_death) and non-death component (Δ_nd). Death avoidance fraction = (Δ_full - Δ_nd) / Δ_full. Cross-task correlation: Pearson r between per-task death rate difference and Δ_full

### 3. Experiments (1.5 pages)

**Key points:**
- **3.1 Setup**: Qwen3-1.7B backbone; ScienceWorld 11 task types × 20-40 episodes; evaluation: always-internal, always-deterministic, oracle, random, keyword heuristic, learned router
- **3.2 Death Decomposition Results** (core result):
  - Δ_full=+29.60, Δ_nd=+2.84, death fraction=90.41% [A: plan-012-full, 245eps/11tasks]
  - 10/11 death-prone tasks: death-dominated gaps
  - 1 exception: find-non-living-thing (n=40, 0 deaths, Δ=+9.58 from non-death mechanisms) [A: plan-012-full, 245eps/11tasks]
  - Pearson r=0.9698 (p=8.12e-07) [A: plan-012-full, 245eps/11tasks]
- **3.3 Baseline Comparison**:
  - always-internal: -39.07, always-det: -9.47, oracle: -6.58, random: -22.38 [A: plan-003-baseline-245eps]
  - Keyword heuristic: structural failure (v1 85.8% match → ≈always-det; v2 4.9% → ≈always-internal)
  - Learned router (ablation-b): internal_recall=51.5%, first non-degenerate; classification head variants all degenerate
- **3.4 Analysis**: Death rate: internal 42.9% vs. deterministic 16.3%; alive-episode scores nearly equal across modalities [A: plan-012-full, 245eps/11tasks]

### 4. Related Work (0.5 pages, integrated or separate)

**Key points:**
- **Tool-use learning**: Toolformer (self-supervised API insertion), ART (LLM-as-router), Chameleon (LLM-as-planner), ToolkenGPT (token-level triggers). Differentiation: episode-level counterfactual labeling, safety-aware framing, explicit modular router
- **Adaptive computation / routing**: CogRouter (RL-based), ARES, Mixture-of-Depths. Our focus: empirical analysis of *what* routing learns, not a new routing architecture
- **World model routing**: ITP-R, Dyna-Think. Our deterministic computation is exact (simulator), not approximate (LLM world model)
- **Agent frameworks**: ReAct, Reflexion. Orthogonal — we analyze the routing decision within an agent loop

### 5. Conclusion (0.3 pages)

**Key points:**
- Summary: death avoidance ≥90% of routing signal; episode-level counterfactual analysis as diagnostic methodology
- **Limitations**: single benchmark (ScienceWorld), episode-level granularity (not step-level), DAgger distribution shift (train on pure strategies, deploy on mixed)
- **Future work**: step-level labeling with denser reward signals, extension to MATH/code interpretation domains, DAgger-style iterative relabeling

---

## Figure/Table Plan

### Table 1: Baseline Comparison
| Method | Score | 90% CI | Success Rate | Death Rate | Sim Ratio |
|--------|-------|--------|-------------|------------|-----------|
| Always-Internal | -39.07 [A: plan-003-baseline-245eps] | TBD | TBD | TBD | 0.00 |
| Always-Deterministic | -9.47 [A: plan-003-baseline-245eps] | TBD | TBD | TBD | 1.00 |
| Oracle | -6.58 [A: plan-003-baseline-245eps] | TBD | TBD | TBD | 0.96 |
| Random | -22.38 [A: plan-003-baseline-245eps] | TBD | TBD | TBD | 0.50 |
| Keyword Heuristic (v1) | ≈ Always-Det | — | — | — | 0.86 |
| Keyword Heuristic (v2) | ≈ Always-Int | — | — | — | 0.05 |
| Learned Router (implicit) | TBD | — | — | — | TBD |

*Source: plan-003-baseline-245eps, plan-011-rule-based*

### Figure 1: Death Decomposition (core figure)
- **Type**: Grouped bar chart or stacked bar
- **X-axis**: 11 task types (sorted by death fraction)
- **Y-axis**: Score delta (deterministic − internal)
- **Bars**: Δ_full decomposed into Δ_death (death-avoidance component, dark) and Δ_nd (non-death component, light)
- **Highlight**: find-non-living-thing as sole exception (Δ_nd = Δ_full = 9.58, zero deaths)
- **Annotation**: Overall death fraction = 90.41%

*Source: plan-012-full*

### Figure 2: Cross-task Correlation (if space permits)
- **Type**: Scatter plot with regression line
- **X-axis**: Per-task death rate difference (internal − deterministic)
- **Y-axis**: Δ_full per task
- **Regression line**: r=0.9698, p=8.12e-07
- **11 points**, labeled by task type
- **Purpose**: Visually demonstrates near-perfect linear relationship

*Source: plan-012-full, plan-012-decomposition*

**Space strategy**: Figure 1 is mandatory. Figure 2 can be merged as an inset in Figure 1, or moved to appendix if space is tight. Table 1 is mandatory. Per-task breakdown table → appendix.

---

## Key References

### Tool-Use Learning
- Schick et al. (2024). Toolformer: Language Models Can Teach Themselves to Use Tools. *NeurIPS*
- Paranjape et al. (2023). ART: Automatic Multi-step Reasoning and Tool-Use. *arXiv*
- Lu et al. (2024). Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models. *NeurIPS*
- Hao et al. (2024). ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings. *NeurIPS*

### Agent Routing / Adaptive Computation
- CogRouter — RL-based cognitive routing (ScienceWorld SOTA)
- ITP-R — imagination-based routing to LLM world model
- ARES — adaptive routing for efficient serving
- Raposo et al. (2024). Mixture-of-Depths. *ICML*

### Agent Frameworks
- Yao et al. (2023). ReAct: Synergizing Reasoning and Acting in Language Models. *ICLR*
- Shinn et al. (2023). Reflexion: Language Agents with Verbal Reinforcement Learning. *NeurIPS*

### Methodology
- Ross et al. (2011). A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning. *AISTATS* (DAgger)

### Environment
- Wang et al. (2022). ScienceWorld: Is your Agent Smarter than a 5th Grader? *EMNLP*

### Code Execution Routing
- Gou et al. (2024). ReTool / ToRA — tool-integrated reasoning for math
- Chen et al. (2023). AgentMath — code-augmented mathematical reasoning

---

## Provenance: Claims → Experiments

| Claim | Source Experiment | Key Metric |
|-------|------------------|------------|
| Δ_full=+29.60, death fraction=90.41% | plan-012-full | delta_full, death_avoidance_fraction |
| r=0.9698, p=8.12e-07 | plan-012-full | pearson_r, pearson_p |
| Baseline scores (Table 1) | plan-003-baseline-245eps | metrics per condition |
| Keyword heuristic failure | plan-011-rule-based | v1_match_rate, v2_match_rate |
| Learned router internal_recall=51.5% | plan-004-ablation-b | per_class.internal.recall |
| find-non-living-thing Δ=9.58 | plan-012-decomposition | key_tasks.find_non_living_thing |
| Episode label distribution 86/9/150 | plan-012-full | label_dist |
| Death rates: int 42.9%, det 16.3% | plan-012-full | death_rate_int, death_rate_det |
| Per-step oracle 98% tie rate | plan-012-decomposition | (derived from label_dist) |
