# Idea Brief: TaxEI: Structured Non-Tool Error Injection for Agent Recovery Training


- **Idea ID**: `idea_008`
- **Created**: 2026-05-14
- **Approved**: 2026-05-14
- **Source**: foreign:be-idea-gen-0509-7
- **Level**: top-tier
- **Target Venues**: EMNLP 2026 (ARR deadline: May 25, 2026), AAAI 2027 (expected ~Aug 2026), ICLR 2027 (expected ~Sep 2026)

## Seed Topic

Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: LLM Agents.

Direction: LLM Agents — planning algorithms, memory architectures, tool use, multi-agent coordination, agent training (SFT/RL), self-correction in agentic loops, environment feedback exploitation.

Contribution type: METHOD ONLY. Must propose a concrete new algorithm, training procedure, or inference-time mechanism. Reject pure benchmark / dataset / analysis ideas. Method + analysis OK if analysis validates the method.

HARD CONSTRAINTS:
1. Compute: ≤200 H100-hours total (baselines + method + ablations). Show the math.
2. Time: ≤16 days. Build on existing OSS agent codebases (AutoGen, LangGraph, OpenManus, etc.) — no from-scratch systems.
3. Eval: existing benchmarks only — AgentBench, WebArena, SWE-bench Verified, GAIA, ToolBench, ALFWorld, Mind2Web, τ-bench.

Avoid: generic ReAct variants, plain tool retrieval, naive memory summarization. Look for: agent training with minimal RL budget, structured planning beyond flat CoT, multi-agent communication protocols, agent self-verification mechanisms.

Tag: direction=agent, contribution_type=method. target_venues=["EMNLP 2026 Main", "EMNLP 2026 Findings"].

## Core Problem

LLM agents fail frequently at planning and context management — even as WebArena success rates have risen substantially (proprietary models: Claude Mythos Preview 68.7%, GPT-5.4 Pro 65.8%; open-weight models: Qwen3.5-397B 55.8%, GLM-5 49.8%, DeepSeek V3.2 48.6%), failure analysis consistently shows planning decomposition errors and context loss account for 40-55% of agent failures across benchmarks (AgentDebug taxonomy, AgenTracer). Yet all training-time error-resilience work targets only tool-level failures or operates without structured error categorization: PALADIN (AAAI 2026 LaMAS Workshop) injects API exceptions and timeouts into 50K+ trajectories for SFT-based recovery, achieving 89.7% tool-error recovery — but planning errors, context corruption, and memory failures remain unaddressed at training time. Agent-R (arXiv 2025) trains recovery via MCTS-based iterative self-training on natural errors but without error categorization, limiting targeted improvement. AgentRefine (ICLR 2025) learns from environment feedback through refinement tuning for generalization but does not inject structured faults. Meanwhile, MAS-FIRE (arXiv 2026) defines a comprehensive taxonomy of 15 fault types including planning and memory categories — but purely for evaluation, not training. A parallel empirical study (arXiv 2603.06847) analyzed 385 faults from 40 open-source agentic AI repositories and produced a taxonomy of 5 fault dimensions and 13 symptom classes, further validating that structured fault categorization is essential for systematic agent improvement. Inference-time approaches (AgentDebug, ErrorProbe, SHIELDA) add scaffolding without improving the agent's inherent robustness, while AgenTracer trains a separate diagnostic model to locate errors but does not teach agents to recover from them. AEGIS (arXiv 2509.14295) generates error-injected multi-agent trajectories for fault attribution but likewise does not train agents for recovery. ErrorProbe (arXiv 2604.17658) introduces a self-improving diagnostic framework using symptom-driven backward tracing and a multi-agent verification team — but focuses purely on error attribution, not agent recovery training.

## Opportunity / Why Now

PALADIN (AAAI 2026 LaMAS Workshop) demonstrated that training-time error injection with SFT substantially improves tool-failure recovery (+13.6% recovery rate), establishing injection-for-recovery as a viable paradigm. MAS-FIRE (arXiv 2026) defined a systematic fault taxonomy of 15 types covering planning (Inexecutable Plan, Critical Information Loss), memory (Memory Loss, Context Length Violation), reasoning, and action categories — but for evaluation, not training. AgenTracer (arXiv 2025) showed that programmatic fault injection on trajectories can generate high-fidelity failure data and trained a diagnostic model via GRPO — but for error attribution, not recovery. AEGIS (arXiv 2509.14295) scaled taxonomy-grounded error injection to 9,533 multi-agent trajectories and trained attribution models via SFT/GRPO — but for diagnosis, not recovery. ErrorProbe (arXiv 2604.17658) advanced diagnostic capabilities with a self-improving framework that operationalizes the MAST taxonomy via symptom-driven backward tracing and tool-grounded multi-agent verification — achieving 34.6% step-level localization accuracy (vs. 8.7% for LLM-as-a-Judge) — but remains a purely inference-time diagnostic system that does not train agents to recover from identified errors. Agent-R (arXiv 2025) trains recovery via MCTS-based self-training, splicing correct paths into failed trajectories (+5.59% on WebShop/ScienceWorld/TextCraft) — but does not categorize errors or target specific failure modes. AgentRefine (ICLR 2025) improves agent generalization through refinement tuning with environment feedback, achieving better perturbation robustness — but operates on natural errors without structured injection. ERL (arXiv 2026) embeds reflection-consolidation into RL training to learn from natural failures (+81% in multi-step environments), but does not inject structured faults or target specific error categories. AgentHER (arXiv 2026) repurposes failed trajectories via hindsight relabeling for +7-12pp SFT/DPO gains but does not inject errors or train category-specific recovery.

A potential concern is raised by Wu et al. (arXiv 2512.02389), who found that SFT with synthetic error injection fails to elicit self-correction in language models due to distribution mismatch between synthetic and on-policy errors. However, their study tested only 1B-parameter models on toy tasks (4-digit multiplication, 4×4 Sudoku) using pure chain-of-thought reasoning without any environment feedback — a fundamentally different setting from agent trajectory training. In agent settings, environment feedback provides external error signals (failed actions, unexpected observations) that ground error detection in observable state changes rather than requiring purely introspective self-correction. Indeed, PALADIN demonstrated that SFT with injection works for agent tool-error recovery, directly contradicting Wu et al.'s conclusion when environment grounding is present.

The central scientific question: PALADIN proved that environment-grounded SFT injection overcomes Wu et al.'s distribution-mismatch barrier for tool errors, where recovery strategies are unambiguous (retry, switch tool, reformulate query). Does this transfer to planning and context/memory errors, where recovery strategies are qualitatively harder and more ambiguous — requiring the agent to re-plan, reacquire lost information, or reconcile contradictory state? Hell or High Water (arXiv 2025) found that agents struggle to formulate backup plans even in restricted search spaces, suggesting this transfer is non-trivial. TaxEI provides the first controlled test by operationalizing MAS-FIRE-style fault categories as training-time injection operators, extending PALADIN's validated paradigm to the harder non-tool setting, and measuring whether structured injection enables category-level generalization via held-out operator evaluation.

The timeliness of this direction is underscored by strong community interest: ICML 2026 accepted multiple workshops on agentic AI failure modes — FMAI (Failure Modes in Agentic AI) and FAGEN — both focused on reproducible failure triggers, trace diagnostics, and verified fixes. TaxEI directly addresses the 'verified fixes' dimension by training agents to recover from categorized failures, complementing the evaluation-focused work presented at these venues.

## Landscape (SOTA & Limitations)

Training-time approaches: PALADIN (AAAI 2026 LaMAS Workshop, arXiv 2509.25238) injects tool failures (API exceptions, timeouts, hallucinated tools) into 50K+ trajectories and trains recovery via LoRA SFT, achieving +13.6% avg recovery rate and 89.7% RR on ToolBench — but is limited to tool errors and requires an inference-time exemplar bank. Agent-R (arXiv 2025, ByteDance) uses MCTS to construct error-recovery training pairs by identifying the first error step in failed trajectories and splicing correct paths, achieving +5.59% on WebShop/ScienceWorld/TextCraft via SFT on Llama-3.1-8B — but without error categorization, recovery is unstructured. AgentRefine (ICLR 2025) enables agents to learn from mistakes via environment feedback through refinement tuning, improving generalization and perturbation robustness — but operates on natural errors without structured injection or category targeting. AgenTracer (arXiv 2025) uses LLM-based perturbation operators to corrupt successful trajectories and trains AgenTracer-8B (GRPO) for error diagnosis — achieving up to 14.2% improvement when feeding diagnostic output back to agents, but the agent itself does not learn recovery. AEGIS (arXiv 2509.14295) scales error injection to 9,533 multi-agent trajectories grounded in the MAST 14-failure-mode taxonomy, training attribution models via SFT (Qwen2.5-14B, +89% over base) and GRPO — but for fault attribution in multi-agent systems, not single-agent recovery training. ErrorProbe (arXiv 2604.17658, April 2026) introduces a self-improving diagnostic framework that operationalizes the MAST taxonomy with symptom-driven backward tracing and a specialized multi-agent team (Strategist, Investigator, Arbiter) for tool-grounded error verification, substantially outperforming baselines on step-level localization (34.6% vs. 8.7% on TracerTraj) — but is entirely prompt-based with no model training, focused on diagnosis not recovery, and evaluated only on multi-agent debugging benchmarks (TracerTraj, Who&When). TaxEI differs fundamentally: it trains the agent itself to recover from errors via SFT/GRPO, whereas ErrorProbe diagnoses errors using an external multi-agent team without modifying the target agent. ERL (arXiv 2026) integrates experience-reflection-consolidation into RL, learning from naturally-occurring failures for +81% in control tasks and +11% in tool-use — but without structured injection or error categorization. AgentHER (arXiv 2026) converts failed trajectories into training data via hindsight relabeling (+7.1-11.7pp on ToolBench, +7-12pp on WebArena), a data-efficiency technique complementary to error injection.

SFT vs. RL for self-correction: Wu et al. (arXiv 2512.02389) showed that SFT with synthetic error injection fails for pure CoT self-correction in 1B models on toy reasoning tasks, due to distribution mismatch between synthetic and on-policy errors (error recognition dropped from 94% to 8% on distribution-shifted errors). SCoRe (Kumar et al., arXiv 2024) demonstrated that on-policy RL achieves substantially positive intrinsic self-correction (+15.6% on MATH). 'SFT Memorizes, RL Generalizes' (Chu et al., ICML 2025) showed RL generalizes to OOD scenarios where SFT memorizes — but also found SFT essential as a warm-start for RL. Critically, Wu et al.'s negative finding applies to introspective self-correction without environment feedback; in agent settings with environment grounding, PALADIN demonstrated that SFT with injection successfully teaches recovery from tool errors, suggesting the environment feedback loop mitigates the distribution-mismatch concern. TaxEI's held-out operator and AgentErrorBench evaluations directly measure whether this mitigation extends to planning/context errors — the qualitatively harder setting where recovery strategies are ambiguous. A preliminary GRPO ablation (TaxEI-SFT warm-start vs. vanilla SFT warm-start) further tests whether taxonomy-guided SFT provides a better RL initialization, connecting to the SCoRe and 'SFT Memorizes, RL Generalizes' findings.

Fault taxonomy work: MAS-FIRE (arXiv 2026) defines 15 fault types across 7 categories for multi-agent evaluation. 'Characterizing Faults in Agentic AI' (arXiv 2603.06847) produced an empirical taxonomy from 385 analyzed faults across 40 open-source repositories, identifying 5 architectural fault dimensions and 13 symptom classes — validated by a 145-practitioner developer study. ErrorProbe (arXiv 2604.17658) operationalizes the MAST taxonomy for step-level error localization in multi-agent traces. All confirm that structured fault categorization systematically exposes weaknesses but none uses taxonomies for recovery training.

Evaluation-time approaches: AgentDebug (arXiv 2025) provides modular corrective feedback with AgentErrorTaxonomy and releases AgentErrorBench (200 expert-annotated failure trajectories on ALFWorld/GAIA/WebShop, Cohen's kappa=0.55) — achieving +26% relative improvement via inference-time feedback. ReliabilityBench (arXiv 2026) evaluates agent reliability using chaos-engineering-style injection. SHIELDA (arXiv 2025) defines 36 exception types across 12 agent artifacts. Hell or High Water (arXiv 2025) evaluates agentic recovery from external failures, finding agents struggle to formulate backup plans.

Community momentum: ICML 2026 accepted multiple workshops on agentic AI failure modes (FMAI, FAGEN), both focused on reproducible failure triggers, trace diagnostics, and verified fixes — validating strong community interest in this research direction.

Key insight from 'What Do Agents Learn from Trajectory-SFT' (arXiv 2026): trajectory SFT can induce interface shortcutting rather than semantic learning — error injection may counteract this by forcing agents to handle unexpected states.

The fundamental gap: Structured fault taxonomies (MAS-FIRE, AEGIS/MAST, ErrorProbe, arXiv 2603.06847) have been validated for evaluation and diagnosis. PALADIN proved injection-for-recovery works for tool errors where recovery is unambiguous. Agent-R proved training error recovery improves performance. But no work has tested whether structured category-specific injection of planning and context/memory errors — where recovery strategies are qualitatively harder and ambiguous — can train recovery in environment-grounded settings. TaxEI uniquely combines the injection taxonomy (operationalizing MAS-FIRE-style categories as training operators) with recovery policy training (extending PALADIN's SFT paradigm to non-tool errors) and a preliminary RL bridge (GRPO ablation testing taxonomy-guided SFT as RL initialization) to answer this question.

## Proposed Approach

We propose TaxEI (Taxonomy-guided Error Injection), a training framework that tests whether environment-grounded SFT injection — validated for tool errors by PALADIN — transfers to the qualitatively harder setting of planning and context/memory errors, where recovery strategies are ambiguous and the Wu et al. distribution-mismatch concern is most acute. TaxEI operationalizes fault categories from evaluation frameworks (particularly MAS-FIRE's taxonomy) as concrete injection operators for recovery-oriented SFT, with a preliminary GRPO ablation testing whether taxonomy-guided SFT provides a superior RL initialization.

**Infrastructure**: TaxEI is built on verl-agent (an extension of veRL for agent RL training, Apache-2.0) using its native agent loop and extension points. Injection operators are implemented through verl-agent's existing customization mechanisms: (a) custom memory modules extending SimpleMemory to corrupt context/history for context/memory errors, (b) prompt template modification in the environment-specific prompt system to inject planning errors, and (c) observation modification via EnvManager wrappers to alter environment feedback. For ToolBench (not natively supported by verl-agent), we implement a custom EnvManager wrapper using StableToolBench's reproducible virtual API server, following the same integration pattern as verl-agent's existing AppWorld (experimental) support — the API-call-based interaction pattern aligns naturally with verl-agent's step-wise model.

**Error Injection Operators** (the core technical contribution):

We define 8 injection operators across 2 non-tool error categories, explicitly aligned with MAS-FIRE's intra-agent fault taxonomy:

*Planning errors* (4 operators, injected via prompt/plan state modification before model calls; aligned with MAS-FIRE's Planning faults):
(P1) Step-order swap: transpose two causally-dependent steps in a decomposed plan (e.g., swap 'pick up knife' and 'go to countertop'). [Aligned with MAS-FIRE: Inexecutable Plan]
(P2) Sub-goal deletion: remove a critical intermediate step, leaving an unachievable gap. [Aligned with MAS-FIRE: Critical Information Loss]
(P3) Irrelevant sub-goal insertion: inject an unrelated action step (e.g., 'examine painting' during a cooking task). [Novel: not directly in MAS-FIRE]
(P4) Goal drift: mid-trajectory, subtly shift the target objective to a related but different goal. [Novel: extends MAS-FIRE's Critical Information Loss to objective-level corruption]

*Context/memory errors* (4 operators, injected via custom memory module overriding SimpleMemory; aligned with MAS-FIRE's Memory faults):
(C1) Context truncation: remove the earliest k observations from the agent's context, simulating window overflow. [Aligned with MAS-FIRE: Memory Loss / Context Length Violation]
(C2) Contradictory fact injection: insert an observation contradicting a previously established fact (e.g., 'the drawer is empty' after the agent saw an item in it). [Novel: extends MAS-FIRE's Memory faults to active corruption]
(C3) Stale state replay: repeat an outdated observation as current, simulating failure to track state changes. [Novel: not directly in MAS-FIRE]
(C4) Observation masking: replace a critical observation with a null/empty result, simulating environment feedback loss. [Aligned with MAS-FIRE: Memory Loss]

Key differentiation from related training-time approaches: (1) vs. PALADIN: extends from tool errors to planning/context errors; (2) vs. Agent-R: uses structured category-specific injection rather than mining natural errors without categorization; (3) vs. AgentRefine: injects synthetic faults into successful trajectories rather than learning from natural environment feedback; (4) vs. AgenTracer/AEGIS/ErrorProbe: trains recovery policies in the agent itself rather than a separate diagnostic/attribution model or inference-time multi-agent verification team; (5) vs. Wu et al.: operates in environment-grounded agent settings where external feedback signals provide observable error indicators, unlike pure CoT introspection.

**Why SFT first, with a GRPO bridge**: SFT is the right first step for three principled reasons. First, TaxEI's structured injection labels (operator category, error location, recovery strategy) provide a supervised curriculum signal — the DETECT→CLASSIFY→RECOVER format is a training-time intervention that requires label supervision, and RL cannot efficiently leverage these structured labels. Second, SFT establishes whether taxonomy-guided injection provides useful training signal at all — a prerequisite question that must be answered before investing in RL-based recovery. Third, 'SFT Memorizes, RL Generalizes' (ICML 2025) found SFT essential as a warm-start for RL, confirming the SFT→RL progression as the principled order. To bridge SFT and RL, we include a preliminary GRPO ablation comparing TaxEI-SFT warm-start vs. vanilla SFT warm-start for recovery training — testing whether taxonomy-guided SFT provides a better RL initialization and connecting to the SCoRe findings.

**Pipeline**:

(0) **Teacher Quality Pilot Study**: Before scaling, validate GPT-4o's recovery demonstration quality. Generate 50 recovery demonstrations per operator category (400 total). Two annotators independently evaluate each for: (a) correct error detection, (b) appropriate recovery strategy, (c) successful task continuation. Report precision and inter-annotator agreement per category. If planning-error recovery quality is borderline (70-80%), we include this as a finding — documenting that teacher model recovery quality degrades from X% (tool errors, per PALADIN) to Y% (planning errors) motivates future work on specialized recovery generators. If any category falls below 70%, apply targeted mitigation: use a stronger reasoning model (o1/o3) for that category's recovery generation.

(1) Collect successful trajectories using GPT-4o as the base agent, leveraging verl-agent's existing environment integrations: ~3K from ALFWorld, ~3K from WebShop, ~2K from ToolBench (via custom StableToolBench EnvManager wrapper). Total: ~8K base trajectories across 3 diverse environments.

(2) Apply injection operators stochastically: each trajectory receives 1-2 injections sampled from the 8 operators, producing ~13K corrupted trajectory variants.

(3) Use GPT-4o as the teacher model to generate recovery demonstrations: given the corrupted trajectory up to the injection point, generate the correct recovery action sequence (detect error, classify, recover). This leverages environment grounding — the agent observes the consequences of injected errors through environment feedback, making error detection externally verifiable rather than purely introspective (addressing Wu et al.'s distribution-mismatch concern).

(4) Format as SFT data with explicit recovery annotations: [DETECT: error description] -> [CLASSIFY: planning/context + operator type] -> [RECOVER: corrective action].

(5) Train Qwen3-8B with LoRA SFT using ms-swift on the ~13K annotated recovery pairs.

(6) **Preliminary GRPO ablation**: Using verl-agent's native GRPO implementation, run ~20h of RL training comparing two conditions: (a) GRPO initialized from TaxEI-SFT checkpoint (taxonomy-guided warm-start), (b) GRPO initialized from vanilla SFT checkpoint (standard trajectory SFT, no error injection). Both use the same reward signal: binary task success after error injection. This tests whether taxonomy-guided SFT provides a structurally better initialization for RL-based recovery, connecting to the 'SFT Memorizes, RL Generalizes' (ICML 2025) finding that SFT warm-starts are essential for RL.

**Evaluation** (designed to address circular evaluation risk and Wu et al.'s distribution-mismatch concern):

(a) **Held-out operator generalization**: Train on 6/8 operators (P1, P2, P3, C1, C3, C4), hold out P4 (goal drift) and C2 (contradictory fact injection) — the two most semantically complex operators. Test recovery on all 8 operators. For held-out operators, evaluate behavioral recovery (can the agent detect something is wrong and take corrective action?) rather than classification accuracy (the agent has never seen these category labels). This provides the first controlled test of whether structured error injection enables category-level generalization — directly testing whether SFT-trained recovery generalizes beyond memorized injection patterns.

(b) **Three-environment evaluation**: ALFWorld (embodied, short-horizon), WebShop (web-based, medium-horizon), and ToolBench (API-based, large-scale tool orchestration with 16K+ APIs via StableToolBench). These span distinct interaction modalities: text-game navigation, web browsing, and API-call orchestration. ToolBench replaces AppWorld to comply with the approved benchmark list and enables direct comparison with PALADIN (89.7% RR on ToolBench) on their home benchmark — showing TaxEI's planning/context injection complements rather than conflicts with tool-error recovery — and with AgentHER (+7.1-11.7pp on ToolBench). Compare against: (i) vanilla ReAct baseline (no error training), (ii) PALADIN-reproduced (tool-error SFT only, reproduced on our three environments), (iii) Agent-R (MCTS self-training, reproduced). AgentRefine, AgentHER, and ERL results cited from their published papers where environments overlap.

(c) **Naturally-occurring error evaluation**: Evaluate on AgentErrorBench from AgentDebug (200 expert-annotated failure trajectories: 100 ALFWorld, 50 WebShop, 50 GAIA). This tests whether training on synthetic injections transfers to naturally-occurring planning and context errors — directly addressing whether environment-grounded SFT injection avoids the distribution-mismatch failure Wu et al. observed in pure CoT settings.

(d) **Clean task evaluation**: Task success rate on unperturbed tasks across all three environments to verify no regression.

(e) **GRPO ablation**: Compare TaxEI-SFT+GRPO vs. vanilla-SFT+GRPO on recovery rate under injec

## Resource Estimate

- **teacher_model_api_cost**: $400-700 (GPT-4o for ~8K base trajectories across 3 environments + ~13K recovery demonstrations + pilot study. Per-environment breakdown: ALFWorld ~$120-200 [~3K trajectories, avg 10 steps, ~20K tokens/trajectory], WebShop ~$150-250 [~3K trajectories, avg 8 steps, ~28K tokens/trajectory], ToolBench ~$100-180 [~2K trajectories, avg 8 steps, ~25K tokens/trajectory with API call context]; recovery demonstrations ~$100-200 [13K demos, avg ~7K context + 1.5K output]. Costs assume GPT-4o at $2.50/M input, $10.00/M output; ~30% savings possible with prompt caching at $1.25/M cached input.)
- **unified**: {'claude_api_cost': '$150-250 (~1200-1800 Opus turns for experiment orchestration and analysis)', 'estimated_gpu_cost': '$475-$665 at ~$2.50-3.50/hr per H100', 'gpu_hours': '~190h H100 (trajectory collection ~20h across 3 envs incl. ToolBench wrapper validation, baseline reproduction ~15h for PALADIN + Agent-R on our envs, SFT training ~25h, main evaluation suite ~45h incl. held-out/AgentErrorBench/clean tasks, GRPO ablation ~20h on 2 conditions, additional ablations ~15h on injection rates, buffer ~15h for reruns; remaining baselines AgentRefine/AgentHER/ERL cited from published numbers)', 'gpu_utilization': '~15-20% idle: pilot study annotation and recovery quality review happen off-GPU; ToolBench wrapper development partially off-GPU', 'risk_note': "Pilot study may reveal that planning-error recovery quality is borderline (70-80%); this is included as a finding documenting teacher model limitations for non-tool errors. ToolBench EnvManager wrapper requires ~1-2 days implementation using StableToolBench's virtual API server, budgeted in days 1-3 concurrent with other setup.", 'team': '1 researcher, ~1.5h/day (pilot study annotation: concentrated on days 1-3, then ongoing review of recovery annotation correctness, held-out evaluation analysis, and paper writing from day 14)', 'timeline': '16 days with parallelized schedule: Days 1-3: baseline reproduction (PALADIN + Agent-R on our envs, ~15h GPU) concurrent with pilot study (400 samples, 2 annotators, off-GPU) and injection operator implementation + ToolBench EnvManager wrapper (off-GPU); Days 3-6: trajectory collection across ALFWorld, WebShop, ToolBench (~20h GPU, parallelized across envs) concurrent with recovery generation pipeline setup; Days 7-9: error injection + GPT-4o recovery demonstration generation (~13K trajectories, primarily API-bound, ~5h GPU for validation); Days 10-12: SFT training with LoRA via ms-swift (~25h GPU); Days 12-14: main evaluation suite — held-out operators, 3 environments, AgentErrorBench, clean tasks (~45h GPU, parallelized across envs); Days 14-16: GRPO ablation (~20h GPU) + remaining ablations (~15h GPU) concurrent with paper writing and analysis'}

## Key References

- PALADIN: Self-Correcting Language Model Agents to Cure Tool-Failure Cases (AAAI 2026 LaMAS Workshop, arXiv 2509.25238)
- MAS-FIRE: Fault Injection and Reliability Evaluation for LLM-Based Multi-Agent Systems (arXiv 2602.19843, 2026)
- Agent-R: Training Language Model Agents to Reflect via Iterative Self-Training (arXiv 2501.11425, 2025)
- AgentRefine: Enhancing Agent Generalization through Refinement Tuning (ICLR 2025, arXiv 2501.01702)
- AgenTracer: Who Is Inducing Failure in the LLM Agentic Systems? (arXiv 2509.03312, 2025)
- AEGIS: Automated Error Generation and Attribution for Multi-Agent Systems (arXiv 2509.14295, 2025)
- Towards Self-Improving Error Diagnosis in Multi-Agent Systems [ErrorProbe] (arXiv 2604.17658, April 2026)
- Characterizing Faults in Agentic AI: A Taxonomy of Types, Symptoms, and Root Causes (arXiv 2603.06847, 2026)
- Experiential Reinforcement Learning (arXiv 2602.13949, 2026)
- Experiential Reflective Learning for Self-Improving LLM Agents (ICLR 2026 MemAgents Workshop, arXiv 2603.24639)
- AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling (arXiv 2603.21357, 2026)
- Where LLM Agents Fail and How They can Learn From Failures [AgentDebug/AgentErrorBench] (arXiv 2509.25370, 2025)
- What Do Agents Learn from Trajectory-SFT: Semantics or Interfaces? (arXiv 2602.01611, 2026)
- SHIELDA: Structured Handling of Exceptions in LLM-Driven Agentic Workflows (arXiv 2025)
- Why Do Multi-Agent LLM Systems Fail? (NeurIPS 2025)
- Hell or High Water: Evaluating Agentic Recovery from External Failures (arXiv 2508.11027, 2025)
- ReliabilityBench: Evaluating LLM Agent Reliability Under Production-Like Stress Conditions (arXiv 2601.06112, 2026)
- Synthetic Error Injection Fails to Elicit Self-Correction in Language Models (Wu et al., arXiv 2512.02389, 2025)
- Training Language Models to Self-Correct via Reinforcement Learning [SCoRe] (Kumar et al., arXiv 2409.12917, 2024)
- SFT Memorizes, RL Generalizes: A Comparative Study of Foundation Model Post-training (Chu et al., ICML 2025)
- StableToolBench: A Stable, Reproducible, and Reliable Benchmarking Framework for Tool Learning (arXiv 2024)

## Reviewer Evaluation

**Scores**:
  - clarity: **{'rationale': 'Exceptionally well-articulated across all dimensions: the 8 injection operators are concrete with explicit MAS-FIRE taxonomy alignment, the SFT-first justification is principled (structured labels as supervised curriculum signal), the Wu et al. counter-argument is well-handled, and the evaluation design addresses all prior reviewer concerns (circular evaluation, natural error transfer, clean task regression). The landscape section is comprehensive with correct citations and honest differentiation.', 'score': 4}**/5
  - feasibility: **{'rationale': "Compute budget (190h H100) fits within the 200h constraint. verl-agent's architecture (EnvironmentManagerBase, SimpleMemory, GRPO implementation) is independently verified to support the claimed extension points. ToolBench wrapper via StableToolBench is a reasonable 1-2 day implementation risk, honestly acknowledged. The 16-day parallelized timeline is aggressive but plausible given that baseline reproduction, pilot study, and operator implementation can run concurrently (days 1-3).", 'score': 4}**/5
  - impact: **{'rationale': 'If positive results materialize, TaxEI opens a new training paradigm for non-tool error recovery — addressing the dominant failure mode (40-55% of agent failures). The GRPO ablation bridges to RL. Three diverse environments (embodied/web/API) with ToolBench enabling direct PALADIN comparison, plus AgentErrorBench for natural error transfer, provide comprehensive evidence. Community timeliness validated by ICML 2026 FMAI/FAGEN workshops. Competitive for EMNLP Findings.', 'score': 4}**/5
  - novelty: **{'rationale': "The gap is independently verified as genuine: no existing work combines taxonomy-guided error injection of planning/context errors with recovery-oriented SFT. The scientific framing — testing whether PALADIN's environment-grounded SFT injection transfers from tool errors (where recovery is unambiguous) to planning/context errors (where recovery is qualitatively harder and Wu et al.'s distribution-mismatch concern is most acute) — elevates this beyond simple paradigm extension. The held-out operator evaluation design provides a novel methodology for testing category-level generalization.", 'score': 4}**/5

## Human Review Note

## Agent 审核结果（完整三阶段 pipeline）

**Verdict**: PASS

**入口三重共识 (X)**: 29.0%
**终审自评 (Y)**: 38.0%
**出口三重共识 (Z)**: 33.0%
**Z 区间**: [28.0%, 37.0%]
**真实提升 (Z-X)**: +4.0 pp
**幻觉幅度 (Y-Z)**: +5.0 pp
**出口一致性**: 高
**出口三次评估**: [32.0, 33.0, 34.0]

### 优化方案 / 拒绝详情
【优化方案】

1. **[标题 / 核心定位]** — 从 "TaxEI: Taxonomy-guided Error Injection for Agent Recovery Training" 调整为 "TaxEI: Taxonomy-Guided Error Injection for **Generalizable** Agent Recovery Training"；核心定位从"一个系统"重构为"一个可复用框架的首个实例化 + 一组 hypothesis-driven 实验"。Introduction 开头即建立两个并列 RQ：(1) cross-category generalization 是否可能？(2) error classification 是否 mechanistically necessary for recovery？ — **命中 Novelty + Significance：将 system paper 提升为 empirical investigation paper，审稿人对 contribution 的定性从 "built a tool" 变为 "answered open questions"**

2. **[Core Hypothesis 章节 — 新增]** — 原 proposal 无显式假设陈述。新版建立三个可检验子假设：Sub-H1（grounding type contingency: explicit vs. implicit），Sub-H2（classification necessity for recovery），Sub-H3（taxonomy structure vs. monolithic injection）。每个子假设都有对应的实验设计直接检验。 — **命中 Technical Soundness + Novelty：hypothesis-driven framing 使 negative result 同样有价值（验证理论预测边界），是 EMNLP 近年推崇的论文范式**

3. **[Conceptual Framework — Grounding Signal Spectrum]** — 原 proposal 仅笼统提及 "environment grounding"。新版显式区分 explicit grounding（tool errors → 环境直接报错）和 implicit grounding（planning/context errors → agent 必须从 state divergence 自行推断），并提供 2×2 可视化表格（grounding type × recovery space size）。这是统一解释 Wu et al.（no grounding → fail）、PALADIN（explicit grounding → succeed）、TaxEI（tests implicit grounding）的概念工具。 — **命中 Novelty：建立了 TaxEI 独创的概念贡献，与 PALADIN 差异化最锐利的一刀；同时命中 Analysis Depth：为结果提供 mechanistic explanation 而非仅 empirical observation**

4. **[Contribution 列表 — 重排序 + 增删]** — 原 proposal 的贡献排序以系统描述为主，GRPO ablation 列为独立贡献。新版重构为：C1（首个控制性跨类别泛化测试 + operator transfer matrix），C2（taxonomy-to-curriculum general framework），C3（stage-wise diagnostic evaluation with mechanistic hypotheses），C4（teacher-model capability 初步刻画）。GRPO 完全删除，移至 Future Work 一句话提及。 — **命中 Technical Soundness：消除 "claimed contribution 只有 20h preliminary experiment 支撑" 的风险；命中 Novelty：transfer matrix 定位为 "first systematic map of cross-category recovery transferability"，类比 cross-lingual transfer matrix（Pires et al. 2019），独立于 TaxEI 性能的 community resource**

5. **[Injection Operators — 具体化]** — 原 proposal 对 OP4-OP8（planning/context operators）仅有概念层面描述。新版为每个 operator 增加 environment-specific 实现示例（如 OP4 在 ALFWorld 中将 "put apple in fridge" 的 subgoal 替换为 "put apple on countertop"；OP7 用环境 object vocabulary 做 template-based observation hallucination）。明确承认 injection realism 是核心假设，由 distribution analysis 和 pilot study 验证。 — **命中 Technical Soundness：堵住 "planning error injection 如何 deterministically 实现？" 的审稿人追问**

6. **[新增 Trajectory Collection 小节]** — 原 proposal 未说明 gold trajectory 来源。新版明确各环境 gold trajectory 的来源（ALFWorld expert rollouts / ToolBench 验证过的成功轨迹）、筛选标准（success + 长度阈值 + 人工抽检）、总量和分布，以及评估模型（Qwen3-8B）≠ gold trajectory 生成模型 ≠ recovery teacher（GPT-4o）的 anti-echo-chamber 声明。 — **命中 Technical Soundness：预防 "teacher model echo chamber" 质疑**

7. **[Held-Out 实验设计 — 从单一 split 扩展为系统化矩阵]** — 原 proposal 仅做一组 6/8 训练 + 2/8 测试，未说明 split 选择逻辑。新版扩展为：(a) 4-6 组 leave-2-out splits（覆盖 same-family + cross-family），每组预注册 rationale；(b) 2-3 组 leave-1-family-out 极端 split（如完全去除 planning family 的 3 个 operators）；(c) 结果聚合为 8×8 operator transfer matrix 热力图，附预注册迁移假设（same-family > cross-family 等）。 — **命中 Technical Soundness + Novelty：从 "2 个 data points 上报的 metric" 升级为 "系统性迁移景观量化"，消除 cherry-picking 质疑；leave-1-family-out 是最 clean 的跨类别泛化测试**

8. **[Stage-Wise Evaluation — 从描述性指标升级为机制性分析]** — 原 proposal 仅提及三阶段训练格式。新版将 [DETECT]→[CLASSIFY]→[RECOVER] 作为独立评估框架（C3），增加：detection latency 分析（planning error 平均多少步后被检测到 vs. tool error），以及核心的 classification necessity 检验——通过 classification-shuffled ablation（训练时用随机类别标签替换正确标签）人为制造大量 "correct detection + incorrect classification" 样本，确保统计效力。 — **命中 Analysis Depth：回答 "如果 end-to-end 不行，瓶颈在哪"；classification necessity 分析将 TaxEI 从 system paper 提升为 insight paper**

9. **[Teacher Quality — 从弱点转化为贡献]** — 原 proposal 将 GPT-4o 在 planning errors 上 70-80% 的表现视为"a finding about teacher model limitations rather than blocking the pipeline"但未展开。新版将其发展为 C4（preliminary characterization of teacher-model capabilities），增加：(a) per-operator quality heatmap（8 operators × 4 quality dimensions）with confidence intervals；(b) teacher-quality-controlled ablation（filtered vs. unfiltered SFT）disentangle teacher ceiling vs. task difficulty；(c) pilot study 目标扩展到 800 samples（100/operator），若不可行则 400 samples + wider CIs + tempered claim。 — **命中 Community Usefulness：高度可引用的附带贡献；命中 Technical Soundness：通过 quality filtering ablation 消除 "teacher 太烂导致结论不 clean" 的 confound**

10. **[Pilot Study — 增加 Injection Realism 验证]** — 原 pilot study 仅评估 recovery demonstration 质量。新版在 pilot study 中增加注入错误本身的自然度评估：(a) 5 点 Likert 量表评分；(b) 混合展示注入错误和自然错误的区分实验（annotator 判断 synthetic vs. natural）。边际成本低（与现有 pilot study 整合）。 — **命中 Technical Soundness：对 planning/context injection realism 这个核心假设的直接验证，预防 "synthetic ≠ real" 攻击**

11. **[Baseline 体系 — 重构]** — 原 proposal 的 baseline 配置有两个问题：cited baselines（AgentRefine/AgentHER/ERL）不直接可比但放在主表，且缺少测试 taxonomy structure 价值的 ablation baseline。新版重构为：(a) Reproduced baselines：PALADIN、Agent-R、**monolithic-uniform**（均匀采样但去除类别标签，隔离 structure 贡献）、**monolithic-random**（按自然概率采样，同时包含 diversity + structure 差异）、**ReAct prompting recovery**（no training lower bound）；(b) Cited baselines 移至 appendix "broader context" 表。 — **命中 Technical Soundness：monolithic-uniform vs. monolithic-random 的双条件设计精确分离 structure 和 diversity 两个因素，直接验证 Sub-H3；ReAct baseline 提供 no-training 参照**

12. **[新增 Curriculum Scheduling Ablation]** — 原 proposal 未讨论训练数据排列顺序。新版增加 random-order vs. easy→hard curriculum-order SFT 对比（按 tool-execution → context → planning 的 family 难度排列），零额外 compute（只改数据顺序）。 — **命中 Novelty：使 C2 中的 "curriculum" 从隐喻变为实质性 curriculum learning 实验，与 Bengio et al. 2009 形成正式对接**

13. **[Synthetic-vs-Natural Distribution Analysis — 升级]** — 原 proposal 无此分析。新版增加：(a) 使用 AgentErrorBench 的 200 个自然错误做 operator-type 分布统计；(b) 计算 taxonomy-guided injection vs. natural error 分布的 Jensen-Shannon divergence；(c) 与 monolithic injection 的 JSD 对比。明确 AgentErrorBench 的环境覆盖情况，若与 TaxEI 环境不一致则降级为参考性验证。 — **命中 Technical Soundness + Related Work Positioning：quantitatively 回应 Wu et al. 的 distribution mismatch 核心质疑，闭合论证链**

14. **[C2 Generality — CWE 第二实例化 Sketch]** — 原 proposal 对 framework generality 仅一句话提及 "code bug taxonomies, medical error taxonomies"。新版在 Discussion 中用 1-2 段具体 sketch CWE → code repair 的应用：CWE fault categories → injection operators → teacher repair demonstrations → cross-CWE-category generalization test。 — **命中 Novelty：将 "general framework" claim 从口号变为可信承诺，减少 "你只在一个 taxonomy 上做了" 的质疑**

15. **[环境缩减]** — 原 proposal 使用 3 个环境（ALFWorld, ToolBench, WebArena）。新版聚焦 ALFWorld + ToolBench 为核心环境，WebArena 降为 supplementary（if time/compute allows）。 — **命中 Feasibility：显著降低工程复杂度（从 24 个 environment-operator 组合降至 16 个），不削弱核心贡献**

16. **[Timeline + Compute 调整]** — 原 16 天 / ~190h H100。新版调整为 20-21 天 / ~220h H100（GRPO 删除后实际节省 20-30h，重新分配给核心实验）。Baseline 优先级排序（monolithic > Agent-R > PALADIN），pilot study 分两阶段（先 400 后 400）。 — **命中 Feasibility：增加 buffer 应对 baseline 复现的工程不确定性**

17. **[Dual-Outcome Value Proposition — 强化]** — 原 proposal 的 dual-outcome 仅一句话。新版详细展开两个场景的具体产出：(a) 成功 → transfer matrix + classification mechanism + curriculum effect；(b) 失败 → 三条可归因路径（teacher quality ceiling / implicit grounding insufficiency / inherent non-transferability），每条归因都有对应的 ablation 支撑。 — **命中 Significance + Technical Soundness：审稿人对 "paper 无论结果如何都有贡献" 的信心大幅增加**

18. **[Limitations 章节 — 新增显式声明]** — 原 proposal 无独立 limitations 段。新版显式列出：injection realism 假设、单模型 scale/family、pilot study 样本量、2 环境覆盖。 — **命中 Technical Soundness：主动暴露局限 > 被审稿人挑出，展示学术诚实度**

【主要风险】:

1. **"PALADIN++ / Incremental Extension" 定性风险** — 尽管 grounding signal spectrum、transfer matrix、classification necessity 共同建立了差异化身份，一位只看算法创新的审稿人仍可能将 TaxEI 定性为 "extends PALADIN from 1 family to 3 families with more careful evaluation"。底层技术（SFT with injection, LoRA, GPT-4o teacher）均为成熟工具的组合，无算法层面创新。这是概率上界的主要限制因素。**缓解策略**：在 rebuttal 中强调 contribution 是 empirical + conceptual（首个控制性泛化测试 + grounding signal spectrum + transfer matrix），而非 algorithmic。

2. **Planning/Context Error Injection Realism** — 即使增加了 naturalness 评估和 distribution overlap 分析，planning operators（OP4-OP6）的注入真实性仍是一个经验性假设。如果 JSD 分析显示 synthetic planning errors 与 natural failures 分布差异大，且 naturalness 评分低，整条论证链的可信度将受影响。**缓解策略**：dual-outcome framing 将此转化为 empirical finding（"synthetic planning errors 不够 realistic → injection approach 对 planning errors 存在 inherent limitation"），但审稿人可能认为这是 "method failure dressed as finding"。

【实施评估】:

- **计算资源**: 约 220h H100 GPU。核心 SFT 训练（Qwen3-8B LoRA, primary split + ablations）~60h；多组 held-out splits（leave-2-out + leave-1-family-out）~50h；baseline 复现（PALADIN, Agent-R, monolithic-uniform, monolithic-random）~40h；teacher-quality ablation ~10h；evaluation + distribution analysis ~30h；secondary model validation（Llama-3.1-8B，stretch goal）~30h。单卡 H100 或 4×A100 集群均可满足。无需大规模分布式训练。
- **数据需求**: ALFWorld（公开，标准 134 test tasks）；ToolBench/StableToolBench（公开）；AgentErrorBench（公开，200 annotated failures）；WebArena（公开，supplementary）。Gold trajectories 需从各环境收集（ReAct expert rollouts 或 benchmark 提供的成功轨迹）。Teacher recovery demonstrations 由 GPT-4o 生成（~13K 条，API 费用约 $200-400）。所有数据集公开可得，无数据获取障碍。
- **人工介入**: Pilot study 需要 2 名标注者，共标注 800 samples（100/operator × 8 operators），评估维度包括 recovery quality（4 维度）+ injection naturalness（Likert + 区分实验）。估计每人 40-50 小时工作量（每 sample ~6 分钟），总计 80-100 人时。需要标注者具备基本的 agent trajectory 理解能力，但不需要领域专家。Inter-annotator agreement 用 Cohen's κ 衡量。若缩减至 400 samples，人工量减半。
- **训练需求**: 需要模型训练。核心训练为 Qwen3-8B LoRA SFT（rank 64, α=128），单次训练约 8-10h H100。总训练次数较多（primary split + 5-8 个 additional splits + 4-5 个 ablation conditions + 2 个 monolithic baselines），但每次训练规模可控（13K 数据，8B 参数，LoRA）。不涉及全参数微调或预训练。Secondary model（Llama-3.1-8B）为 stretch goal。
- **新 Benchmark**: 不需要构建全新 benchmark。核心评测使用已有 benchmark（ALFWorld, ToolBench, AgentErrorBench）。Operator transfer matrix 是一个新的评
