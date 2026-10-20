# Idea Brief: ProgressProbe: Learned Window-Level Progress Estimation for Detecting Semantic Stagnation in LLM Agent Loops


- **Idea ID**: `idea_012`
- **Created**: 2026-05-14
- **Approved**: 2026-05-14
- **Source**: foreign:be-idea-gen-0509-1
- **Level**: top-tier
- **Target Venues**: EMNLP 2026 (ARR submission deadline: May 25, 2026; commitment deadline: August 2, 2026) — primary target, 14-day timeline feasible for short paper (4 pages + references), ACL 2026 (ARR August 2026 cycle, ~August 15 deadline) — fallback if EMNLP timeline proves too tight; allows extended evaluation with stagnation typing (human-annotated) and intervention selector as long paper, NAACL 2027 (ARR ~October 2026) — backup for long paper version with full detection + intervention pipeline, multi-domain evaluation, and stagnation type taxonomy

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

LLM agents frequently stagnate during long-horizon tasks—executing individually reasonable but collectively unproductive actions without advancing toward the goal. Current trajectory monitoring systems treat this as an anomaly detection problem (TrajAD, TRACER, Trajectory Guard, IBM Cycle Detection) or a step-level value estimation problem (AgentPRM, SPA-RL, SWE-TRACE). But semantic stagnation is fundamentally neither anomalous nor step-level: each action may be well-formed, non-repetitive, and locally plausible, while step-level scores remain high because individual actions appear promising. The real issue is the absence of goal-directed progress across a *window* of actions—requiring a window-level progress estimation framing distinct from both action-level anomaly detection and step-level scoring. Moreover, no existing system provides interpretability into *what* distinguishes stagnating windows from progressing ones—whether stagnation onset has characteristic temporal signatures that static aggregation misses. Meanwhile, the Intervention Paradox (arXiv:2602.03338) demonstrates that even accurate failure detectors can cause severe performance degradation (-25.5 pp) when coupled with naive interventions, and The Verifier Tax (arXiv:2603.19328) quantifies the overhead of runtime verification at 2.0–2.8× token inflation, underscoring that high-quality, low-overhead detection must be empirically validated before any intervention system can be safely deployed.

## Opportunity / Why Now

The trajectory monitoring landscape has expanded rapidly along two orthogonal axes—anomaly/cycle detection and value estimation—yet a critical gap persists at their intersection, compounded by the absence of interpretable progress signals. Cycle and anomaly detectors (TrajAD, TRACER, Trajectory Guard, IBM Cycle Detection's CDCS+CDSA hybrid, SpecRA's FFT autocorrelation) flag structurally wrong, repetitive, or periodic actions but miss semantically diverse stagnation where the agent reads different files, tries different strategies, and runs different tests without progress. IBM Cycle Detection (arXiv:2511.10650) achieves F1=0.72 by combining call-stack structural analysis (CDCS) with semantic embedding cosine similarity (CDSA), but their semantic component reduces to pairwise cosine similarity—the same approach that DSAP (arXiv:2512.20660) shows fails on 85.9% of stagnation instances that produce sufficiently different failing outputs. SpecRA (OpenReview:xVO4BqmzVD, submitted to ICLR 2026) detects periodic repetition via FFT autocorrelation over token sequences, effective for degenerative repetition but not semantic stagnation where actions are diverse. Step-level value estimators (AgentPRM, SWE-TRACE's rubric-based PRM, Process Reward Agents) score individual steps but operate at step granularity—one could threshold step scores averaged over a window, but this imposes a uniform aggregation that cannot capture the sequential dynamics of stagnation onset. Self-reflection-based approaches (AgentCollab, arXiv:2603.26034) use intrinsic LLM self-evaluation for progress detection, but rely on the stagnating model's own assessment rather than a separately trained external detector—problematic precisely when the agent is stuck in a confident but unproductive loop. Recovery-oriented systems (PALADIN, BacktrackAgent, BEAP-Agent, DSAP) implement backtracking but rely on detecting tool-level failures or structural loops rather than progress deficits. Early-termination systems (EET, CaRT) reduce compute waste but use experience retrieval or counterfactual reasoning rather than learned progress signals. The remaining gap is a learned, interpretable, window-level progress estimator trained on domain-specific progress signals that can serve as a high-precision stagnation detector with low overhead (cf. The Verifier Tax's 2.0–2.8× inflation for full verification), providing the reliable detection signal that must precede safe downstream intervention.

## Landscape (SOTA & Limitations)

**Cycle and anomaly detection (detect wrong/repetitive actions):** TrajAD (arXiv:2602.06443, Feb 2026) trains a LoRA-finetuned Qwen3-4B verifier on TrajBench (63K trajectories, 5 domains) detecting task failures, process inefficiency (structural loops, redundant steps), and unwarranted continuation, achieving 81.81% F1 with step-level error localization. Its 'process inefficiency' targets observable structural patterns, not semantic stagnation where actions appear diverse and correct. IBM Cycle Detection (arXiv:2511.10650, Oct 2025) combines structural call-stack analysis (CDCS) with semantic embedding cosine similarity (CDSA) for unsupervised cycle detection, achieving F1=0.72 (precision 0.62, recall 0.86) on 1,575 LangGraph stock-market agent trajectories. Their CDSA component—cosine similarity of span embeddings—is essentially our baseline #3, and their hybrid CDCS+CDSA (F1=0.72) provides a natural comparison point for testing whether learned progress estimation outperforms heuristic semantic cycle detection. SpecRA (OpenReview:xVO4BqmzVD, submitted to ICLR 2026) applies FFT autocorrelation via randomized projection to detect degenerative repetition in LLM agents, building a taxonomy of repetition modes from 813 samples in 1.13M agent outputs—effective for periodic repetition but not semantic stagnation where actions are diverse. TRACER (arXiv:2602.11409, Feb 2026) aggregates content-aware surprisal, repetition patterns, and tool coherence gaps into a trajectory-level uncertainty metric. Trajectory Guard (arXiv:2601.00516, Jan 2026) applies a Siamese Recurrent Autoencoder for real-time plan-level anomaly detection (F1 0.88–0.94). MASC (arXiv:2510.14319, Oct 2025) learns trajectory embeddings for unsupervised error detection. Detecting Silent Failures (arXiv:2511.04032, Nov 2025) trains XGBoost/SVDD on trajectory features post-hoc (98% accuracy on drift/cycles) but provides no online detection. ProbGuard (arXiv:2508.00500) builds a DTMC from execution traces for probabilistic safety monitoring. Near-Miss (arXiv:2603.29665, March 2026) detects latent policy failures where agents bypass required checks yet reach correct outcomes, finding 8–17% of trajectories contain such failures—complementary to stagnation detection but focused on policy adherence rather than progress. **Progress/value estimation (step-level, not window-level):** AgentPRM (arXiv:2511.08325, ACM Web 2026) trains a TD-based process reward model scoring step-level 'promise' and 'progress'—could be thresholded for stagnation detection by averaging scores over k steps, but this uniform aggregation cannot capture sequential dynamics of stagnation onset. SWE-TRACE (arXiv:2604.14820, April 2026) uses a rubric-based PRM with an auxiliary Rubric-Agent for dense step-level feedback, designed for test-time scaling, not online monitoring. SPA-RL (arXiv:2505.20732, May 2025) trains a progress estimator for training-time reward redistribution only. Process Reward Agents (PRA, arXiv:2604.09482, April 2026) provides online step-wise rewards via search-based decoding for knowledge-intensive QA (MedQA), achieving 80.8% accuracy with Qwen3-4B—operates at step level for domain-grounded verification during generation, not window-level progress estimation for online trajectory monitoring. AgentProcessBench (arXiv:2603.14465, March 2026) provides 8,509 ternary step-level annotations across 1,000 trajectories at step granularity without window-level aggregation. **Self-reflection-based progress detection:** AgentCollab (arXiv:2603.26034, March 2026) uses the agent's own self-reflection to produce a binary progress signal (TRUE/FALSE) at each step, triggering model escalation from a cheaper to a stronger model upon stagnation. Their self-evaluation is intrinsic ('generated by the model itself based solely on the current reasoning context, without any training process or auxiliary routing model')—fundamentally different from ProgressProbe's external trained detector. The intrinsic approach is problematic for semantic stagnation precisely because a model stuck in a confident but unproductive loop may self-evaluate as making progress. **Runtime verification overhead:** The Verifier Tax (arXiv:2603.19328, March 2026) quantifies the cost of runtime safety enforcement in tool-using LLM agents: 2.0–2.8× token inflation from planning and verification messages, with recovery rates from 21% to near-zero after blocked actions. This motivates ProgressProbe's lightweight (<5ms) probe approach as an alternative to full LLM-based verification—an external trained detector imposes negligible overhead compared to intrinsic self-reflection or full verification architectures. **Recovery and early-termination systems:** PALADIN (arXiv:2509.25238, Sep 2025) learns self-correction from 50K+ recovery trajectories targeting tool-level failures. BacktrackAgent (EMNLP 2025, arXiv:2505.20660) trains verifier/judger/reflector modules for error detection and backtracking based on action correctness. BEAP-Agent (arXiv:2601.21352, Jan 2026) models GUI task execution as DFS with structural backtracking. DSAP (arXiv:2512.20660, Dec 2025) implements a three-level recovery hierarchy—critically, their finding that 85.9% of stagnation instances produce sufficiently different failing outputs demonstrates that similarity-based approaches fail on semantic stagnation. EET (arXiv:2601.05777, Jan 2026) achieves 32% average cost reduction on SWE-bench Verified via experience-driven early termination with ≤0.2% resolution loss—using retrieval from past successful executions rather than learned progress signals. CaRT (arXiv:2510.08517, Oct 2025) teaches agents when to stop via counterfactual trajectory pairs, applied in medical diagnosis and math domains. **The Intervention Paradox:** Vasudev et al. (arXiv:2602.03338, Feb 2026) show that a binary LLM critic with AUROC 0.94 caused -25.5 pp degradation, formalizing the disruption-recovery tradeoff: intervention helps only when baseline failure rate p > d/(r+d). **Geometric/diagnostic approaches:** Geometric Dynamics of Agentic Loops (arXiv:2512.10350) formalizes drift/dispersion metrics in embedding space. Exploration-Exploitation Errors (arXiv:2604.13151, April 2026) quantifies exploration vs. exploitation errors across 13 LMs. Understanding Code Agent Behaviour (arXiv:2511.00197, Nov 2025) compares OpenHands, SWE-agent, and Prometheus trajectories on SWE-bench, finding failure patterns differ significantly across agents—motivating our cross-agent generalization evaluation. The Long-Horizon Task Mirage (arXiv:2604.11978), Beyond pass@1 (arXiv:2603.29231), and Where LLM Agents Fail (arXiv:2509.25370) diagnose agent failure modes but propose no learned detector. **The remaining gap:** No system provides learned, interpretable, window-level progress estimation for online stagnation detection—operating between action-level cycle/anomaly detection (misses diverse stagnation) and step-level scoring (loses sequential dynamics under uniform aggregation). ProgressProbe fills this gap with a detection-focused contribution that goes beyond 'it works better' to reveal what temporal signatures distinguish stagnation from progress via representation analysis, empirically demonstrating the value of learned window-level estimation over both heuristic approaches and step-level score averaging, including simulated early-termination evaluation grounded in the Intervention Paradox framework.

## Proposed Approach

Train a lightweight progress probe with learned positional encoding and attention-based window aggregation that estimates goal-directed progress within sliding trajectory windows, evaluate as a high-precision binary stagnation detector on SWE-bench trajectories with cross-agent generalization, simulated early termination, and interpretability analysis revealing what temporal signals the probe captures that static aggregation misses. This is a detection-focused short paper contribution. **Phase 1 — Domain-Specific Progress Labeling (Days 1–4):** Download 80K+ trajectories from nebius/SWE-agent-trajectories (HuggingFace) with resolved/unresolved outcome labels. Additionally download nebius/SWE-rebench-openhands-trajectories (67K OpenHands trajectories) for cross-agent evaluation. Define progress within sliding windows (k=5 agent steps) using four domain-specific labeling functions: (a) file diff delta—net bytes of meaningful code change between window start and end; (b) test pass rate transition—change in number of passing tests after 'run tests' actions; (c) linter output delta—change in warning/error count; (d) outcome backpropagation—windows in resolved trajectories near the resolution point labeled progressing; sustained flat-signal windows in unresolved trajectories labeled stuck. **Labeling function analysis:** Report the fraction of ~200K labeled windows attributed to each labeling function; quantify agreement/disagreement between functions on overlapping windows; identify a 'high-confidence' subset where ≥2 functions agree. **Labeling coverage analysis:** Quantify what fraction of trajectory windows receive NO signal from any labeling function (e.g., windows containing only file reads, documentation browsing, or planning actions with no code changes or test runs). Report this coverage gap explicitly, exclude no-signal windows from training, and analyze whether the probe's test-time predictions on no-signal windows correlate with eventual trajectory outcomes. Human calibration: spot-check 500 labels to measure agreement with automated labeling functions (targeting >90% agreement). **Phase 2 — Progress Probe Training (Days 4–7):** Encode each trajectory window as a sequence of step embeddings using frozen Qwen3-Embedding-0.6B. Each step serialized as (action_type, tool_name, key_parameters, truncated_observation_256_tokens). Train a binary progress head on a GRU encoder (hidden_dim=256, 2-layer) with **learned positional encoding** for step positions within the window (positions 1..k) and **attention-based aggregation with position-aware attention weights**, outputting calibrated P(progressing) via temperature scaling. The learned positional encoding allows the model to capture position-dependent stagnation onset dynamics—e.g., learning that the transition from progress to stagnation has characteristic signatures at specific positions within the window, which uniform aggregation (mean-pooling) provably cannot capture. **Contrastive auxiliary objective:** In addition to binary cross-entropy, add a supervised contrastive loss (SupCon) over GRU final hidden states that pulls progressing window representations together and pushes stuck window representations apart in embedding space. This serves dual purposes: (1) improved separation yields better detection, and (2) the resulting embedding structure directly supports the interpretability analysis in Phase 5 by producing well-clustered representations. We focus on binary progress/stuck classification rather than stagnation typing to avoid circularity in evaluation (see below). Target: <5ms inference per step (cf. The Verifier Tax's 2.0–2.8× token inflation for full LLM verification), >85% F1 on held-out windows. **Phase 3 — Detection Evaluation (Days 7–10):** Evaluate on two test sets: (A) held-out SWE-agent trajectories (20% held-out split stratified by outcome and repository)—same-distribution; (B) OpenHands trajectories from nebius/SWE-rebench-openhands-trajectories—cross-agent generalization, using the same labeling functions applied to a different agent's action format, tool usage patterns, and observation style. This directly tests whether the probe learns general progress signals or overfits to SWE-agent-specific patterns, addressing the concern from arXiv:2511.00197 that failure patterns differ significantly across agents. **Baselines:** (1) No detection (iteration cap at agent's default step limit); (2) Repeat-3 heuristic (flag when 3 consecutive actions share >80% token overlap); (3) Embedding cosine similarity threshold (flag when mean pairwise cosim within window > 0.9); (4) Geometric dynamics metrics (local drift + dispersion thresholding from arXiv:2512.10350); (5) Windowed AgentPRM (repurpose step-level progress score by averaging over k steps—directly tests whether step-level signals suffice or learned window-level aggregation adds value); (6) IBM CDCS+CDSA hybrid (re-implement call-stack structural analysis + semantic cosine similarity from arXiv:2511.10650—tests whether learned estimation outperforms their heuristic hybrid approach, F1=0.72 on their domain). **Metrics:** (a) Detection precision/recall/F1 on held-out labeled windows for both test sets A and B; (b) Cross-agent generalization gap (F1 on test set B vs. A); (c) False positive rate on progressing episodes; (d) Per-labeling-function analysis (see ablations). **Key ablations:** (i) Window size (k=3,5,7); (ii) Architecture (GRU+attention vs. GRU+mean-pooling vs. MLP vs. mean-pooling-only—the mean-pooling ablation directly tests whether sequential modeling and learned positional encoding add value beyond uniform aggregation); (iii) Embedding model (Qwen3-Embedding-0.6B vs. 4B for quality-cost tradeoff); (iv) **Labeling function hold-one-out ablation:** Train four probe variants, each with one labeling function removed, to quantify each function's marginal contribution and specifically assess outcome backpropagation noise—if removing outcome backpropagation improves cross-agent F1, this reveals label noise; if it degrades performance, the signal is genuinely informative despite the correlation/causation concern. Report the fraction of labels sourced from each function; (v) **Contrastive loss ablation:** Train with and without SupCon auxiliary loss to measure its contribution to both F1 and embedding separability. **Phase 4 — Simulated Early-Termination Evaluation (Days 10–11):** Move beyond analytical Intervention Paradox computation to empirical early-termination simulation. For each detected-stuck episode in held-out trajectories: (a) check whether the trajectory would have eventually succeeded (i.e., is this a false positive that would kill a succeeding trajectory?); (b) compute tokens/steps saved by terminating at the detection point; (c) aggregate into compute savings vs. lost-success tradeoff curves at varying detection thresholds. This yields: empirical disruption rate d (fraction of eventually-successful trajectories incorrectly terminated), empirical recovery rate r (fraction of stuck trajectories correctly identified for early termination), and the failure-rate threshold p* = d/(r+d) from the Intervention Paradox framework. Compare p* against observed SWE-bench baseline failure rates to determine feasibility. Also compare against EET's (arXiv:2601.05777) reported 32% cost reduction as a reference point for compute savings. Also compare against The Verifier Tax's overhead: ProgressProbe aims for significant cost savings at negligible inference cost (<5ms per step), unlike full verification architectures that inflate token costs 2.0–2.8×. This converts the Intervention Paradox analysis from a thought experiment into an empirical result at near-zero additional compute cost—all computation uses existing held-out trajectories. **Phase 5 — Interpretability Analysis (Days 11–12, 0 additional compute):** This phase requires no new model training or inference—only analysis of existing model outputs from Phases 2–3. **(a) Representation analysis:** t-SNE visualization of GRU final hidden states for progressing vs. stuck windows, compared against t-SNE of raw mean-pooled step embeddings (without GRU processing). This directly tests whether the GRU learns a clear separation in representation space that raw embeddings do not exhibit—i.e., whether the sequential processing creates discriminative structure. Plot cluster purity and silhouette scores for both representations. The contrastive auxiliary loss is expected to produce tighter clusters, quantified by comparing silhouette scores with and without SupCon. **(b) Attention weight analysis at stagnation onset:** For windows that span the transition from progressing to stuck behavior (identified via labeling function signals), visualize attention weights across the k=5 positions. Hypothesis: the model learns to attend disproportionately to the 'turning point' steps where progress signals cease—e.g., the last test run that still passed, or the last file edit that produced meaningful diff. If positional attention patterns are consistent across stagnation instances, this reveals a learnable temporal signature of stagnation onset that uniform aggregation provably misses. **(c) Error analysis:** Categorize false positives (progressing windows flagged as stuck) and false negatives (stuck windows missed) by action type, labeling function source, and trajectory outcome. Key questions: Do false positives cluster in windows with low-signal actions (file reads, planning)? Do false negatives occur in early-stage stagnation where the probe hasn't accumulated enough evidence? This analysis converts the contribution from 'we trained a classifier and it beat baselines' to 'we show that sequential dynamics in trajectory windows carry learnable stagnation signals with characteristic temporal structure that static aggregation misses, and we characterize what those signals look like.' **Contingency framing (windowed-AgentPRM competitive scenario):** If baselin

## Resource Estimate

- **auto_research**: {'claude_api_cost': '$100–200 (~1000–2000 Opus turns)', 'estimated_gpu_cost': '$190', 'gpu_hours': '~75h H100 (2x ablation grid: window sizes, architectures incl. contrastive variants, embedding models, threshold sweeps, labeling function ablations, cross-agent evaluation)', 'gpu_utilization': 'High (~80%)', 'risk_note': 'Well within 200h H100 hard constraint. No live agent evaluation runs needed—all evaluation is on existing trajectory data. Cross-agent evaluation depends on OpenHands trajectory format being parseable into our step serialization schema.', 'speed_bottleneck': 'Trajectory embedding is the main sequential bottleneck (~12h for SWE-agent + ~8h for OpenHands); all other steps parallelize well. Early-termination simulation and interpretability analysis add negligible compute—purely trajectory replay and post-hoc visualization.', 'team': '0 (initial setup and final review only)', 'timeline': '10–12 days with 2 H100 GPUs'}
- **human_in_loop**: {'claude_api_cost': '$50–100 (~500–1000 Opus turns for experiment orchestration and writing assistance)', 'estimated_gpu_cost': '$95', 'gpu_hours': '~37h H100 (overlapping embedding/training with human label review)', 'gpu_utilization': 'Moderate (~50%)', 'risk_note': 'Primary risk is the 14-day timeline for ARR submission. Adding OpenHands cross-agent evaluation increases embedding time by ~40% but is parallelizable. Labeling function hold-one-out ablation adds 4 additional training runs (~8h total). Contrastive loss ablation adds 1 training run (~1h). Interpretability analysis (Phase 5) requires zero additional compute—only post-hoc analysis of existing outputs. The IBM CDCS+CDSA baseline requires re-implementing call-stack analysis for SWE-agent action format—estimated 4–6 hours of engineering.', 'team': '1 researcher, ~1hr/day for label spot-checks, interpretability review, and analysis review', 'timeline': '14 days'}
- **manual**: {'estimated_gpu_cost': '$80 (at ~$2.50/hr H100 spot, May 2026)', 'gpu_hours': '~32h H100 (trajectory embedding ~12h including OpenHands trajectories, probe training ~3h including contrastive loss variants, baseline evaluation + ablations ~17h)', 'gpu_utilization': 'Low (~25%); GPUs idle during labeling function design, label spot-checking, interpretability analysis, and writing', 'team': '1 researcher', 'timeline': '14 days (May 11–25, 2026)'}

## Key References

- The Intervention Paradox: Accurate Failure Prediction Does Not Imply Effective Prevention (arXiv:2602.03338, Feb 2026)
- Unsupervised Cycle Detection in Agentic Applications (arXiv:2511.10650, Oct 2025) — IBM; hybrid CDCS+CDSA F1=0.72; CDSA component is our baseline #3, hybrid is baseline #6
- SpecRA: Monitor Degenerative Repetition in LLM Agents using Randomized FFT (OpenReview:xVO4BqmzVD, submitted to ICLR 2026) — FFT autocorrelation for periodic repetition detection
- TrajAD: Trajectory Anomaly Detection for Trustworthy LLM Agents (arXiv:2602.06443, Feb 2026)
- DSAP: Dual-State Action Pair Framework with Stagnation Detection and Informed Backtracking (arXiv:2512.20660, Dec 2025)
- BacktrackAgent: Error Detection and Backtracking for GUI Agents (EMNLP 2025, arXiv:2505.20660)
- BEAP-Agent: DFS-Based GUI Automation with Long-Range Backtracking (arXiv:2601.21352, Jan 2026)
- SWE-TRACE: Rubric-Based Process Reward Model for SWE Agents (arXiv:2604.14820, April 2026)
- AgentProcessBench: Ternary Step-Level Evaluation for Tool-Using Agents (arXiv:2603.14465, March 2026)
- ProbGuard: Probabilistic Runtime Monitoring for LLM Agent Safety (arXiv:2508.00500)
- MASC: Metacognitive Self-Correction via Next-Execution Reconstruction (arXiv:2510.14319, Oct 2025)
- Detecting Silent Failures in Multi-Agentic AI Trajectories (arXiv:2511.04032, Nov 2025)
- SPA-RL: Stepwise Progress Attribution for RL-Trained LLM Agents (arXiv:2505.20732, May 2025)
- AgentPRM: Process Reward Models via Step-Wise Promise and Progress (arXiv:2511.08325, ACM Web 2026)
- TRACER: Trajectory Risk Aggregation for Critical Episodes (arXiv:2602.11409, Feb 2026)
- Trajectory Guard: Lightweight Sequence-Aware Anomaly Detection (arXiv:2601.00516, Jan 2026)
- PALADIN: Self-Correcting Language Model Agents (arXiv:2509.25238, Sep 2025)
- EET: Experience-Driven Early Termination for Cost-Efficient Software Engineering Agents (arXiv:2601.05777, Jan 2026)
- CaRT: Teaching LLM Agents to Know When They Know Enough (arXiv:2510.08517, Oct 2025)
- Geometric Dynamics of Agentic Loops (arXiv:2512.10350, Dec 2025)
- Exploration and Exploitation Errors Are Measurable (arXiv:2604.13151, April 2026)
- Understanding Code Agent Behaviour: An Empirical Study (arXiv:2511.00197, Nov 2025) — cross-agent trajectory analysis motivating generalization evaluation
- Beyond pass@1: A Reliability Science Framework for Long-Horizon LLM Agents (arXiv:2603.29231, 2026)
- Where LLM Agents Fail and How They Can Learn From Failures (arXiv:2509.25370, Sep 2025)
- The Long-Horizon Task Mirage (arXiv:2604.11978, April 2026)
- AgentBoard: An Analytical Evaluation Board of Multi-turn LLM Agents (NeurIPS 2024)
- AgentCollab: A Self-Evaluation-Driven Collaboration Paradigm for Efficient LLM Agents (arXiv:2603.26034, March 2026) — intrinsic self-reflection-based progress detection triggering model escalation; different mechanism (intrinsic vs. external trained detector)
- The Verifier Tax: Horizon Dependent Safety-Success Tradeoffs in Tool Using LLM Agents (arXiv:2603.19328, March 2026) — quantifies 2.0–2.8× token inflation from runtime verification, motivating lightweight probe approach
- Process Reward Agents for Steering Knowledge-Intensive Reasoning (arXiv:2604.09482, April 2026) — online step-wise rewards via search-based decoding for QA, not window-level progress estimation for coding agent stagnation
- Near-Miss: Latent Policy Failure Detection in Agentic Workflows (arXiv:2603.29665, March 2026) — complementary work on latent failure detection in agent traces

## Reviewer Evaluation

**Scores**:
  - clarity: **{'rationale': "Exceptionally thorough proposal with explicit contingency planning (windowed-AgentPRM scenario), clear evaluation protocol (6 baselines, 2 test sets, 5 ablations), well-defined phases, and careful differentiation from 28+ related works. The landscape analysis is one of the most comprehensive I've reviewed.", 'score': 4.5}**/5
  - feasibility: **{'rationale': 'All data sources verified (nebius 80K + 67K trajectories), embedding model available (Qwen3-Embedding-0.6B), compute budget realistic (~32-75h H100, well within 200h cap). Timeline is tight at 14 days but feasible for a short paper with pre-existing trajectory data and no live agent evaluation. Primary risk is cross-agent trajectory format compatibility between SWE-agent and OpenHands action schemas.', 'score': 4.5}**/5
  - impact: **{'rationale': 'Limited to SWE-bench domain and detection-only (no intervention), but the practical contribution — stagnation detection for cost reduction with empirical early-termination profiles — is directly actionable for the SWE-bench agent community. The interpretability findings about temporal signatures of stagnation and the labeling function methodology could generalize beyond SWE-bench.', 'score': 3.5}**/5
  - novelty: **{'rationale': 'The core architecture (frozen embeddings → GRU → binary classifier) is standard, but the problem framing (window-level progress estimation as distinct from both anomaly detection and step-level scoring) is genuinely novel. The labeling function methodology, cross-agent generalization evaluation, contrastive auxiliary objective, attention-based positional aggregation, and interpretability analysis collectively elevate the contribution beyond a straightforward classifier — though this targets EMNLP Findings rather than Main.', 'score': 3.5}**/5

## Human Review Note

## Agent 审核结果（完整三阶段 pipeline）

**Verdict**: PASS

**入口三重共识 (X)**: 23.0%
**终审自评 (Y)**: 33.0%
**出口三重共识 (Z)**: 31.0%
**Z 区间**: [26.0%, 36.0%]
**真实提升 (Z-X)**: +8.0 pp
**幻觉幅度 (Y-Z)**: +2.0 pp
**出口一致性**: 高
**出口三次评估**: [33.0, 32.0, 30.0]

### 优化方案 / 拒绝详情
【优化方案】

1. [标题 / 核心术语] — 将 "Semantic Stagnation" 修正为 "Progress Stagnation"，标题改为 *ProgressProbe: Learned Window-Level Progress Estimation for Detecting Progress Stagnation in Software Engineering Agent Loops* — [命中 Technical Soundness：消除"语义"名不副实的概念错位攻击面；命中 Related Work：明确限定 SE domain，避免 over-claim]
   原始标题中 "Semantic Stagnation" 暗示 LFs 在做语义分析，但四个 LF（file diff、test pass-rate、linter output、outcome backprop）实际度量的是功能进展。修正后将 "semantic diversity" 保留为描述检测挑战的属性（表面形式多样但功能进展为零），而非检测目标本身。同时标题增加 "Software Engineering" 限定词，与实验范围对齐。

2. [投稿格式] — 从 short paper（4 页）改为 long paper（8 页正文 + appendix） — [命中 Technical Soundness + Significance：释放分析深度空间，分析深度是本文真正的卖点]
   原始 proposal 的内容量（6 baseline 对比、多项 ablation、t-SNE、attention 分析、early-termination 模拟、error analysis）远超 4 页承载能力。改为 long paper 后，每个实验/分析可获得充分展开空间。明确规划 core vs. appendix：正文聚焦 method + main results + human validation + cross-implementation transfer + LF temporal dynamics；appendix 放 per-LF 详细分析、data scaling、attention visualization、error taxonomy、architecture variants、domain adaptation discussion。

3. [贡献叙事 / 核心重构] — 从"单贡献（检测器）+ contingency fallback"重构为"双贡献：弱监督标注框架 + 系统性实证研究"，删除 contingency framing — [命中 Novelty + Significance：将 novelty 锚点从标准架构转移到方法论层面；命中 Technical Soundness：消除 narrative 自毁]
   - **贡献一**定位为 "Agent Trajectory Labeling via Data Programming"——从 Snorkel 范式到 agent trajectory 的非平凡迁移，强调两个 non-trivial adaptation：(a) LFs 产生时序信号而非 i.i.d. 标签；(b) outcome backpropagation 引入全局-局部冲突，需 temporal discounting + confidence-based gating。含 LF 冲突解决策略对比（majority vote vs. learned label model）。
   - **贡献二**定位为系统性实证研究，含跨实现迁移分析 + SupCon 对迁移性的因果作用调查。
   - "问题形式化"降格为 framing/motivation 的一部分，不作为独立贡献列出（对 EMNLP reviewer 太轻）。
   - **彻底删除** contingency framing（"if windowed AgentPRM is competitive, contributions shift to..."）——这在论文中会被解读为作者对自身贡献缺乏信心，是 narrative poison pill。

4. [架构叙事降权] — 将 GRU + positional encoding + attention aggregation 从"核心贡献"降格为"deliberately simple and effective technical choice" — [命中 Novelty：将 reviewer 的 novelty 期望锚定在方法论层面而非架构层面]
   原始 proposal 过度强调架构细节（"position-aware attention aggregation"、"GRU-based probe with learned positional encoding"），给人包装已知技术的印象。新叙事中架构只需 "work well"，配合架构变体消融（Transformer encoder, Mamba, MLP on pooled features），若 GRU 胜出则产出 "lightweight temporal modeling suffices" 的 actionable insight。

5. [NLP venue fit 加固] — 增加与经典 NLP 问题的结构类比 + non-NLP baseline 对比实验 — [命中 Significance + Related Work：直接回应"为什么投 EMNLP 而不是 ICSE/NeurIPS"]
   - 在 intro 中建立结构类比：progress stagnation detection ≈ trajectory-level semantic equivalence judgment under surface diversity，与 NLI/paraphrase detection 有结构相似性但操作单元从 sentence pair 扩展到 action-observation window sequence。
   - 增加 non-NLP baseline：仅用纯结构/数值特征（行数改动量、AST diff size、test pass/fail counts、linter warning counts）做分类，不使用任何自然语言处理。若 NL embedding probe 显著胜出，直接证明理解自然语言内容的必要性。
   - 在 related work 中说明选择外部 encoder embedding 而非 agent-internal representations 的理由（agent-agnostic 监控需求）。

6. [Baseline 大幅扩展与重组] — 从 6 个 baseline 扩展到 10 个，分为 analytical 和 competitive 两组 — [命中 Technical Soundness + Related Work]
   新增 baseline：
   - **LLM-as-judge**（GPT-4o / Claude，zero-shot + few-shot）——预防 "为什么不直接用 LLM" 质疑，最关键的新增 baseline
   - **LF ensemble oracle**——直接用 LF 实时输出做窗口级判定，论证 probe 相对于 LF 的增量价值
   - **Mean-pooling + logistic regression**——参数匹配的下界，证明 GRU temporal modeling 的增量来自时序建模而非参数量
   - **Embedding cosine similarity 滑动窗口**——最简单的语义重复检测器
   
   Baseline 分为两组在 results table 中视觉区分：Analytical baselines（cycle detectors，回答"多少 stagnation 是 cyclic 的"）vs. Competitive baselines（直接与 ProgressProbe 竞争）。消除 straw man comparison 质疑。
   
   所有 baseline 标注出处（会议/期刊/arXiv + 年份），确保 ≥3-4 个 peer-reviewed；软化 "first" claim 为 "systematic comparison"。

7. [人工验证设计] — 新增 400 window 人工标注评估，破解 circular evaluation — [命中 Technical Soundness：堵住最大攻击面]
   原始 proposal 完全没有人工验证，训练和评估均在自动标签上形成闭环。新增：3 annotators × 400 windows（分层抽样：class balance + task difficulty + LF conflict level），pilot 校准轮，Fleiss' κ + 预设可解释性阈值，ambiguous 处理协议（primary: 排除 ambiguous 评估；secondary: ambiguous→stuck）。Per-LF precision/recall 矩阵量化每个 LF 的标注质量。所有方法在人工标签上重新评估。

8. [Outcome Backpropagation 补强] — 从"承认假设"升级为"实质性改进 + 实证量化" — [命中 Technical Soundness]
   原始 proposal 仅提到这个 LF 存在且推迟人工标注到 long paper。新版：(a) 实现 temporal discounting（线性 + 指数衰减两种）并报告结果；(b) confidence-based gating（仅在 ≥2 个 LF 一致时采纳 outcome backprop）；(c) conflict rate 分析（outcome=success 但 diff/test/linter 显示无进展的 step 占比）；(d) hold-one-out 细分分析（成功轨迹中的探索阶段、失败轨迹中的早期正确步骤）；(e) 报告 Snorkel label model 学到的权重。

9. [Cross-agent claim 精确化] — "agent-invariant" → "cross-implementation transferability"，明确 scope — [命中 Technical Soundness：消除 over-claim 攻击面]
   SWE-agent → OpenHands 做同一类任务、操作同一环境，表征对齐是 weaker finding。措辞修正 + limitations 中讨论真正 cross-domain transfer 的条件和预期 failure mode。CKA + t-SNE 仍保留，SupCon 对迁移性的因果作用显式消融。

10. [数据溯源 + Scaling] — 明确 80K 轨迹来源 + data scaling 实验 + 开源承诺 — [命中 Technical Soundness + Feasibility]
    原始 proposal 未说明 80K 轨迹如何获得（SWE-bench 原始仅 ~2294 instances）。新版明确标注公开 dataset URL/版本/agent 版本/LLM backend，加入 10%/25%/50%/100% scaling 曲线，承诺代码和数据开源。

11. [实用价值量化] — 增加 cost-accuracy Pareto 图 + 具体 token/dollar savings — [命中 Significance]
    新增显式 Pareto frontier 可视化（x: per-window cost, y: F1/AUROC），覆盖从 cosine similarity（近零成本）到 ProgressProbe（<5ms）到 LLM-as-judge（昂贵）全谱。报告 stagnation 占总 token 预算百分比、各 recall 点位的 token 节省量、按当前 API pricing 的美元估算。Oracle intervention upper bound 估计最大可达 pass-rate 提升。

12. [PRM 定位 + Agent Training 连接] — 在 intro 建立 PRM 关联，discussion 连接 agent training loop — [命中 Significance：与当前热点（PRMs for agents）对接]
    ProgressProbe 作为 weakly-supervised domain-specific PRM for agentic trajectories，与 Math-Shepherd/OmegaPRM 的区别：(a) 针对 action-observation sequences 而非 reasoning chains；(b) 用 programmatic weak supervision 替代 outcome supervision。Discussion 指出 calibrated probability 可作为 RL fine-tuning 的 process reward signal 或 DPO/KTO 的 rejection signal。

13. [LF temporal dynamics 分析] — 新增 LF 先后关系分析 — [命中 Analysis Depth]
    在 hold-one-out 分析中增加时间维度：哪个 LF 在 stagnation onset 最先亮灯（leading indicator），哪个是 lagging indicator。为实践者提供 actionable guidance。

【主要风险】:

1. **Probe vs. LF ensemble 的增量价值是否成立**：如果直接用 LF 实时输出（majority vote / learned label model）做窗口级判定的效果与 probe 相当或更好，则 probe 的核心价值仅剩"离线/无 sandbox 场景下的替代方案"，这会显著削弱第二贡献的说服力。Reviewer 会直接问"why train a model when rules work?"。这是实验结果层面的最大不确定性。

2. **EMNLP venue fit 仍存不确定性**：尽管增加了 NLI 类比、non-NLP baseline 对比、NLP 必要性论证，核心 LFs 和数据仍 100% 来自 SE 领域。遇到 SE-skeptical 的 NLP reviewer 时，可能被判 "more suitable for ICSE/FSE"。这是 reviewer lottery 层面的风险，无法通过论文内容完全消除。

【实施评估】:

- **计算资源**: 
  - Embedding 生成：Qwen3-Embedding-0.6B（frozen）处理 80K+ trajectories，单 GPU（A100/H100）约 1-2 天
  - GRU probe 训练：轻量模型，单 GPU 数小时级别；含架构变体消融（GRU/Transformer/Mamba/MLP）约 1-2 天
  - LLM-as-judge baseline：GPT-4o/Claude API 调用，估计测试集 ~2000-5000 windows × 4 配置（2 model × zero/few-shot），按 $0.01-0.03/window 计约 $80-600
  - 总计算需求：1× A100/H100 GPU 约 1 周 + API 预算 $200-800

- **数据需求**: 
  - 80K+ SWE-bench agent trajectories：需确认公开 dataset（如 nebius/SWE-rebench 或类似），若需自行生成则成本大幅增加（需多次运行 SWE-agent，API 成本可达数千美元）
  - 67K OpenHands trajectories：nebius/SWE-rebench-openhands-trajectories（已公开）
  - 所有数据均为代码/SE 领域，公开可得性是关键前提

- **人工介入**: 
  - 人工标注：3 annotators × 400 windows（含 pilot 校准轮），每人约 4-6 小时
  - 标注者资质：需具备基本的软件工程背景以理解 agent trajectory 内容
  - 标注协议设计 + 培训 + 质量审核：额外 1-2 天
  - 总人工成本估算：12-20 人时

- **训练需求**: 
  - 需要模型训练，但规模很小——GRU probe 是轻量序列模型（非 LLM 训练）
  - 含 SupCon 辅助目标的多任务训练，单次训练数小时
  - 需训练多个变体（架构消融、LF 组合消融、data scaling），总训练次数约 20-30 次
  - 无需微调或预训练任何大语言模型

- **新 Benchmark**: 
  - 不需要构建全新 benchmark
  - 需要构建人工标注的 gold-standard 测试子集（400 windows），这是对现有数据的标注而非新数据集
  - LF ensemble oracle baseline 需要在测试集上运行所有 4 个 LF 的实时版本

- **预估周期**: 
  - 数据获取与预处理：1-2 周（取决于 80K 轨迹是否公开可直接下载）
  - Embedding 生成 + probe 训练 + 全部消融：2-3 周
  - Baseline 实现与运行（含 LLM-as-judge API 调用）：1-2 周
  - 人工标注设计 + 执行 + 分析：1-2 周
  - 分析章节（t-SNE, CKA, temporal dynamics, Pareto 图, error analysis）：1-2 周
  - 论文写作：2-3 周
  - **总计：约 8-12 周**（部分阶段可并行），ARR May 2025 deadline 需倒推启动时间



## MVP Validation Results

- **Date**: 2026-05-14
- **Hypothesis Supported**: Yes

### Key Metrics

Probe macro-F1: 0.9055 | Repeat-3 baseline: 0.8432 | Gap: 6.24pp | Stagnation F1: 0.8593 vs 0.7532 | Train windows: 10,634 | Val: 2,943 | Test: 1,824 | Best epoch: 3/8 | GPU time: ~5 min

### Summary

GRU probe（2-layer, hidden=256）在 SWE-bench agent 轨迹的弱监督标签上训练，test set macro-F1=0.9055。比最佳 baseline Repeat-3（0.8432）高 6.24pp。训练数据：15,401 高置信度窗口（conf≥2，3 个 LF 中至少 2 个一致）。Probe 在 stagnation 检测上优势尤为显著（F1 0.8593 vs 0.7532）。核心假设"弱监督标注+GRU probe 能有效检测 progress stagnation"得到验证。

### Recommendation

GO — 进入 research 阶段。后续重点：(1) 全量数据（conf≥1）泛化性验证，(2) 跨 agent model 迁移实验，(3) Probe 错误分析（是否只学了 LF 启发式），(4) 与 Repeat-3 的消融（命令重复信号 vs embedding 语义信号），(5) paper framing 围绕弱监督框架+系统性实证展开。
