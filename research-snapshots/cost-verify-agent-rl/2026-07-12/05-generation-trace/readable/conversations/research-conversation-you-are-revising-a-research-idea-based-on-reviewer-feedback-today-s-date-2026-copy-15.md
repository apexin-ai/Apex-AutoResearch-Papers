# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-09 (UTC).** ## Original idea { "tit

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-2/273dc98c-8ab8-4fa8-9d51-65cb993ef786.jsonl`
- **Structured JSON:** [`7c73db9da0156d66a826.json`](../../sessions/7c/7c73db9da0156d66a826.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-09T18:40:49.888Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-09T18:40:49.888Z",
  "sessionId": "273dc98c-8ab8-4fa8-9d51-65cb993ef786",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-09 (UTC).**\n\n## Original idea\n{\n  \"title\": \"CascadeWatch: Cascade-Onset Detection with Targeted Rollback for Long-Horizon Agent Tasks\",\n  \"core_problem\": \"In long-horizon agent tasks, individual early-step errors produce cascading downstream failures that grow exponentially more costly to correct with each additional step. The core question is whether a lightweight trained monitor can prospectively detect cascade onset—predicting failure propagation before it fully manifests—to trigger targeted rollback rather than reactive reflection or full replanning. The challenge is not simply detecting failure: the Intervention Paradox (arXiv 2602.03338) establishes that generic critics with AUROC 0.94 cause up to 26 percentage point performance degradation by triggering on non-cascade failures that the agent would have self-corrected. The disruption-recovery tradeoff (Δ Success = p·r − (1−p)·d) only favors intervention on high-failure benchmarks like ALFWorld; it degrades GAIA and HotPotQA even with accurate critics. The solution is not a better generic critic but a cascade-specific one: targeting only the recoverability-degrading prefix patterns that precede confirmed cascades—detectable via recoverability proxy signals—to achieve the high precision (low d) and focused recall (high p conditional on cascade-onset) that shifts the threshold in favor of intervention. A natural alternative early-warning signal is canonical path deviation (arXiv 2602.19008): measuring Jaccard similarity of tool invocations against the convergent set shared across successful runs. This signal is empirically validated but requires aggregating tool invocation sequences from multiple successful runs per task, making it unavailable for novel tasks or low-success-rate settings. CascadeWatch uses ERR Efficiency Score recoverability deltas (arXiv 2601.22352) computable from single trajectories without reference to other runs, enabling cascade detection in the absence of precomputed canonical paths. The rollback mechanism varies by environment affordance: for text-game environments (ALFWorld), full environment-state rollback is achieved via command-replay from env.reset(); for tool-augmented environments (WebShop, GAIA), context-only rollback rewinds the agent's context window. Neither mechanism requires a non-existent API; both are acknowledged to have environment-specific costs and limitations.\",\n  \"opportunity\": \"The cascade failure pattern is now well-characterized and trainable. AgentErrorBench (arXiv 2509.25370) provides the first systematically annotated failure taxonomy across ALFWorld, WebShop, and GAIA, with root-cause step annotations identifying where cascades originate; memory and reflection errors at steps 5–15 are the most common initiators, crucially occurring mid-trajectory rather than at the earliest steps where the Intervention Paradox shows all regressions occur. The ERR paper (arXiv 2601.22352) formalizes recoverability as Expected Recovery Regret and derives a measurable Efficiency Score proxy, empirically validated across five benchmarks to within δ ≤ 0.05 of observed post-failure regret—establishing that step-level recoverability is observable from trajectory prefixes and thus learnable as a predictive signal. This signal applies directly to tool-augmented agents (WebShop, GAIA) where structured tool-call/result pairs provide natural Efficiency Score observables; for text-game environments (ALFWorld), where failures are cognitive planning errors rather than tool execution failures, a domain-adapted proxy (step-level game score delta) is used instead, acknowledged as a heuristic extension. Canonical Path Deviation (arXiv 2602.19008) provides independent corroboration of the self-reinforcing cascade mechanism in long-horizon tool-use tasks: each off-canonical tool invocation raises the probability that the next invocation is also off-canonical by 22.7 percentage points, confirming that cascade propagation is empirically measurable and compounding. CascadeWatch uses recoverability signals rather than canonical path adherence specifically because recoverability deltas are computable from a single trajectory, enabling deployment where canonical paths from multiple successful runs are unavailable. BacktrackAgent (arXiv 2505.20660, EMNLP 2025) demonstrates that backtracking triggers improve GUI agent task completion on Mobile3M and Auto-UI benchmarks, but requires constructing a task-specific training dataset and fine-tuning the agent components—leaving a clear gap for an external, training-free cascade monitor that operates on any frozen agent in cognitive long-horizon tasks. The proactive detection landscape now includes ProMAS (arXiv 2603.20260) for multi-agent error attribution, ProbGuard (arXiv 2508.00500) for physical safety monitoring, and Trajectory Guard (arXiv 2601.00516) for general structural anomaly detection in agentic trajectories, but none targets cognitive-task cascade failure in single-agent long-horizon settings nor closes the detection-to-rollback loop. The labeled failure datasets, recoverability signals, and the Intervention Paradox's threshold formula together make a specific, testable hypothesis: a cascade-specific monitor using recoverability signals will achieve sufficiently higher precision than generic critics to make rollback net-positive on benchmarks where generic critics fail, for the first time.\",\n  \"landscape\": \"Proactive monitoring is an active and crowded area that must be navigated carefully. ProMAS (arXiv 2603.20260, March 2026) uses Causal Delta Features mapped to a 30-prototype Vector Markov Space with a frozen Meta-Llama-3.1-8B extractor to predict failure onset in multi-agent collaborative reasoning systems, achieving 22.97% step-level accuracy on the Who&When benchmark (annotated multi-agent dialogues of math and logic puzzles) while processing only 27% of reasoning logs. Critically, ProMAS raises an alert but provides no corrective action—it is a detector only and evaluates exclusively on the Who&When multi-agent attribution benchmark, not on single-agent long-horizon tasks. ProbGuard (arXiv 2508.00500) learns a Discrete-Time Markov Chain from symbolic agent-state abstractions with PAC-style guarantees and triggers prompt-injection interventions when P(unsafe state) exceeds a threshold; it predicts traffic violations up to 38.66 seconds ahead and reduces unsafe behavior by 65.37% in embodied agents, but operates on physical safety constraints using symbolic abstractions rather than frozen neural representations or recoverability signals. Trajectory Guard (arXiv 2601.00516, AAAI TrustAgent Workshop 2026) proposes a Siamese Recurrent Autoencoder with hybrid contrastive-reconstruction loss for real-time anomaly detection in agentic AI trajectories, achieving F1 0.88–0.94 on balanced sets and recall 0.86–0.92 on imbalanced external benchmarks while running 17–27× faster than LLM Judge baselines at 32ms inference. Three distinctions separate this from CascadeWatch: (1) Trajectory Guard detects general structural anomalies—contextual misalignment and sequential incoherence—via reconstruction error, not cascade-specific onset via recoverability-delta signals; (2) it evaluates on synthetic perturbations, security audit failures (RAS-Eval), and multi-agent attribution (Who&When), not on single-agent long-horizon cognitive tasks (ALFWorld, GAIA); (3) it provides no rollback or correction mechanism—detection only. The lightweight framing ('inference-time monitoring of agentic trajectories') directly overlaps with CascadeWatch's positioning, but the two systems target structurally different failure modes: Trajectory Guard's reconstruction error is task-agnostic and catches any structural deviation, while CascadeWatch's recoverability-delta specifically targets the compounding-cost prefix patterns that confirm cascade onset in long-horizon cognitive tasks. The ORC auditing paper (ICLR Workshop 2026, arXiv 2603.13325) detects cascading risks in multi-agent systems via Ollivier-Ricci Curvature on completed interaction graphs—post-hoc auditing, not inference-time intervention. Canonical Path Deviation (arXiv 2602.19008, Feb 2026) is the closest theoretical neighbor to CascadeWatch's cascade-onset framing. Analyzing 515 model-task combinations on the Toolathlon benchmark (22 frontier models, 108 real-world tool-use tasks across 3 independent runs each), Wilson Y. Lee identifies stochastic drift from canonical solution paths—the convergent set of tool invocations shared across successful runs—as a causal mechanism of long-horizon failure. Path adherence is measured as Jaccard similarity between actual and canonical tool invocation sequences; adherence gaps are statistically indistinguishable from zero through the first half of trajectories but become significant and self-reinforcing thereafter, with each off-canonical tool call raising the probability that the next call is also off-canonical by 22.7 percentage points. An intervention restarting the bottom tercile of runs by mid-trajectory canonical adherence achieves +8.8pp success rate improvement. Three distinctions separate this from CascadeWatch: (1) Canonical path adherence requires aggregating tool invocation sequences across multiple successful runs per task—unavailable for novel tasks or low-success-rate settings; CascadeWatch's ERR Efficiency Score recoverability proxy is computable from a single trajectory without reference to other runs. (2) Canonical path deviation detects drift retrospectively via trajectory statistics that become significant only in the second half of execution; CascadeWatch proactively intervenes at steps 5–15 using a trained probe on prefix embeddings, before adherence divergence solidifies. (3) The CPD intervention is a full task restart of lowest-adherence runs; CascadeWatch performs targeted rollback to the pre-cascade checkpoint, preserving valid completed steps and avoiding full re-execution cost. From Spark to Fire (arXiv 2603.04474, March 2026) models cascade error propagation in LLM-based multi-agent collaboration using an individual-based mean-field framework over inter-agent communication graphs, and proposes a genealogy-graph governance layer that tracks atomic claim provenance via NLI-based verification (Green/Red/Yellow status using DeBERTa-v3-small) and blocks transmission of error-carrying messages; the Benign Infection Control Rate (complement of attack success rate) improves from 0.32 to 0.89 across Chain, Mesh, and Star multi-agent topologies on data-analysis, logic, and MMLU tasks. The cascade mechanism is specifically inter-agent: atomic factuality errors injected at one agent propagate through recursive message reuse across rounds of collaboration—a phenomenon requiring multiple communicating agents. CascadeWatch addresses a structurally different failure mode—cognitive cascade failure within a single agent's sequential trajectory (ALFWorld's planning errors, GAIA's tool-call compounding)—where there are no inter-agent message dependencies and no genealogy graph can be constructed. The per-message NLI verification in From Spark to Fire also introduces latency proportional to message volume; CascadeWatch adds only a single 2-layer MLP forward pass per step. The Intervention Paradox (arXiv 2602.03338) is the most important negative result in the space: ROLLBACK and APPEND interventions triggered by a generic LLM critic (AUROC 0.94) degrade performance on HotPotQA by −2.3 to −25.5pp and on GAIA by −4.4 to −30pp; only ALFWorld (high baseline failure rate: 5.8–14.7%) shows improvement (+0.5 to +2.8pp). All observed regressions occur with early-step (step ≤ 2) interventions. BacktrackAgent (arXiv 2505.20660, EMNLP 2025) trains a verifier-judger-reflector pipeline for GUI agents (Mobile3M, Auto-UI benchmarks) to detect individual action errors and trigger backtracking. Unlike CascadeWatch, BacktrackAgent requires constructing a task-specific training dataset and fine-tuning the agent's backtracking components; it targets GUI action-level errors (click/type correctness) rather than recoverability-degrading cascade onset in cognitive long-horizon tasks, and provides no recoverability signal. Self-Backtracking (arXiv 2502.04404) trains the base LLM to internalize when and where to backtrack during training and inference, achieving over 40% performance gains over optimal-path SFT baselines in general reasoning. This approach requires model retraining and modifies the agent's internal reasoning; CascadeWatch operates as a frozen external probe on any pre-trained agent, requiring no modification to the agent and no access to model weights or training infrastructure. Deploying CascadeWatch with a different LLM backbone requires retraining only the lightweight MLP probe (~3–5 H100-hours) against that backbone's embedding space—not retraining the backbone itself. Prior work probes LLM hidden states for single-step answer correctness in mathematical reasoning (arXiv 2504.05419), achieving 24% token reduction via early exit by detecting when intermediate reasoning steps are correct. The mechanism is structurally similar to CascadeWatch's frozen embedding + MLP probe, but targets single-step step-level correctness rather than multi-step cascade onset in agent trajectories; crucially, it adds no recoverability signal channel and does not address long-horizon failure propagation. Reactive self-correction methods share the same fundamental limitation: ExpeL and Contextual Experience Replay distill past trajectories for future improvement; self-verification (arXiv 2602.03485) confirms rechecks rarely identify errors; T-STAR (arXiv 2604.07165) achieves training-time divergence detection via Cognitive Trees but adds no inference-time mechanism. No existing system combines cascade-specific detection using recoverability signals with targeted rollback and a false-positive circuit-breaker, nor validates that cascade-specific precision avoids the Intervention Paradox's disruption-recovery tradeoff.\",\n  \"approach\": \"We train CascadeWatch to address the Intervention Paradox by targeting only the recoverability-degrading mid-trajectory patterns that precede confirmed cascades. Training data: AgentErrorBench's 200 expert-annotated trajectories (davide221/agenterrorbench on HuggingFace, spanning ALFWorld, WebShop, and GAIA) augmented with ~5,000 synthetic rollouts from Qwen/Qwen3-32B (HuggingFace: Qwen/Qwen3-32B; 32B dense model; 64GB BF16; fits in 1× H100-80GB without quantization—the Qwen3-72B designation referenced in earlier drafts corresponds to unofficial community merges and lacks an authoritative reproducible checkpoint) sampled at three temperatures (0.7, 1.0, 1.3) to increase failure-mode diversity. Cascade labels use a confirmed-cascade criterion: a step k is labeled cascade-onset only if (1) the trajectory ultimately fails, (2) step k is at or after the earliest annotated root-cause error, AND (3) the root-cause error occurs before the trajectory midpoint (step ≤ ⌊total_steps / 2⌋)—this filters out partially-recovered trajectories and prevents false cascade labels from error-tolerant agents. A minimum intervention threshold of step ≥ 5 is imposed at inference time, consistent with AgentErrorBench's finding that cascade-initiating errors occur at steps 5–15 and with the Intervention Paradox's finding that all observed regressions involve step ≤ 2 interventions. Each trajectory prefix at step k is represented by concatenating (a) frozen Qwen/Qwen3-32B hidden-state embeddings (mean-pooled last 4 transformer layers over the action–observation sequence) with (b) recoverability delta signals. For WebShop and GAIA (tool-augmented benchmarks with structured tool-call/result pairs), these are ERR Efficiency Score deltas as defined in arXiv 2601.22352. For ALFWorld (a text-based game where failures are cognitive planning errors rather than tool execution failures, and which lacks structured tool-call pairs), ERR Efficiency Score is not directly applicable; we substitute a domain-adapted proxy: step-level delta in the normalized ALFWorld game score (Δ(info['score'] / info['max_score']) at each step), which tracks incremental subgoal-completion rate. This is an acknowledged heuristic extension of the ERR framework; whether the recoverability motivation holds for this proxy is explicitly tested in the ablation. A 2-layer MLP probe (with L2 weight decay 1e-4) outputs P(cascade | prefix_k), with Platt scaling applied on a stratified held-out validation split. Training data sparsity (200 labeled trajectories) is addressed by (i) 5-fold cross-validation stratified by benchmark (ALFWorld / WebShop / GAIA) to estimate generalization without benchmark leakage, and (ii) a parallel logistic probe baseline to assess whether MLP complexity is justified over this small labeled set. The AgentErrorBench annotations are distributed unevenly across benchmarks: GAIA contributes approximately 50 of the 200 labeled trajectories, yielding roughly 27 training samples per fold in 3-fold CV (the compressed HIL mode), placing the GAIA cascade probe near the minimum viable supervised learning regime; GAIA results are consequently treated as preliminary evidence, with ALFWorld (approximately 100 trajectories, ~67 per fold) providing the primary evidence base for the main cascade-avoidance claim. CascadeWatch requires no modification to the base agent and does not require retraining the agent backbone; deploying CascadeWatch with a different LLM backbone requires retraining only the lightweight MLP probe (~3–5 H100-hours) against that backbone's embedding space, not retraining the agent itself. This is a meaningful practical advantage over BacktrackAgent, which requires constructing a task-specific training dataset and fine-tuning agent components. The rollback mechanism is specified per benchmark: For ALFWorld, environment-state rollback is performed via command-replay from env.reset(): the TextWorld gym environment is reset to the initial observation, then the k−1 accepted actions from the checkpoint buffer are re-executed sequentially to reconstruct game state at step k−1. The ALFWorld game engine processes each text command in approximately 1–2ms; for typical episodes capped at 50 steps, rollback at step k incurs roughly 25–100ms wall-clock overhead—negligible relative to LLM inference time. A checkpoint buffer stores accepted action sequences at each step to enable replay without re-querying the LLM. Note that TextWorld's Python API does not expose a save/restore mechanism for Glulx-format (.ulx) games used in ALFWorld competition settings, so command-replay is the correct mechanism; the O(k) replay cost is in game-engine steps, not LLM compute. The Crab sandbox (arXiv 2604.28138) provides semantics-aware container-level checkpoint/restore that could in principle support ALFWorld game-state snapshots regardless of the underlying game engine; CascadeWatch uses command-replay to maintain compatibility with standard ALFWorld evaluation setups that do not use containerized sandboxes, and to avoid container-spinup overhead that would dominate the ~25–100ms rollback budget. For WebShop and GAIA, context-only rollback rewinds the agent context window to step k_checkpoint, masks all subsequent actions and observations, and re-samples an alternative action with temperature +0.3. Context-only rollback does not undo irreversible WebShop web-state changes (e.g., submitted searches), which is explicitly noted as a limitation. A false-positive circuit-breaker limits rollback to a maximum of 2 triggers per episode; after the second trigger, monitoring is suspended for the remainder of the episode to prevent compounding disruption. Before full evaluation, we run the Intervention Paradox's 50-task pilot test on each benchmark to empirically verify that CascadeWatch's cascade-specific intervention is net-positive (p > d/(r+d)) on that benchmark; benchmarks where the pilot test fails are reported as negative results, not omitted. We include a pre-registered 3-way ablation: (a) frozen embeddings only → logistic probe, (b) recoverability-delta features only → logistic regression (no embeddings), (c) full CascadeWatch (embeddings + recoverability-delta) → 2-layer MLP. The primary empirical claim is that CascadeWatch achieves task success rate improvement over no-correction baselines on ALFWorld and GAIA while avoiding the performance degradation caused by generic critics observed in the Intervention Paradox—demonstrating for the first time that cascade-specific precision is sufficient to make rollback net-positive on benchmarks where generic critics fail. The recoverability-delta ablation serves as an internal validation gate: if recoverability-delta provides ≥3% F1 lift over frozen embeddings alone, the ERR-motivated feature design is empirically confirmed; if the lift is <3%, the theoretical ERR motivation weakens substantially and this is reported honestly as a negative result on the recoverability signal hypothesis. We evaluate task success rate, steps saved per episode, and false-positive intervention rate against no-correction, ExpeL-style reflection, self-verification, T-STAR offline, and ProMAS-style detection-only baselines on ALFWorld, WebShop, and GAIA (subject to pilot test results).\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~100-140 H100-hours total: rollout generation ~45 H100-hours (Qwen/Qwen3-32B runs in BF16 on 1× H100-80GB without quantization—32B × 2 bytes ≈ 64GB, within the 80GB VRAM budget; inference throughput roughly doubles relative to a 72B model; ~45h covers ~5K synthetic rollouts across three benchmarks at three temperatures, including environment interaction overhead and tool-call latency for GAIA tasks); probe training ~10 H100-hours (5-fold CV × 3-way ablation × logistic/MLP variants; these are small models, <1h each); evaluation runs ~45–85 H100-hours across three benchmarks + pilot tests (50 tasks × 3 benchmarks × 2 conditions per test). ALFWorld command-replay rollback adds <1 H100-hour overhead across all evaluation episodes.\",\n      \"gpu_utilization\": \"~30–40% effective utilization; high idle between human coding, debugging, and analysis cycles\",\n      \"timeline\": \"4–6 months\",\n      \"team\": \"2 researchers\",\n      \"estimated_gpu_cost\": \"~$200–$280 at ~$2/H100-hour\"\n    },\n    \"human_in_loop\": {\n      \"scope_note\": \"Compressed to satisfy the joint ≤16-day calendar / ≤200 H100-hour constraint. Primary benchmarks reduced to ALFWorld + GAIA (2 of 3); WebShop deferred to optional extension after primary evaluation completes. Synthetic rollouts reduced to 2,000 total at 2 temperatures (T=0.7, T=1.0); 3-fold CV replaces 5-fold. Human gates: cascade label validation, pilot test pass/fail judgment per benchmark, ablation design review, threshold decisions. Human engagement: 2–3 hours/day (not 30 min/day).\",\n      \"compute_breakdown\": \"Rollout generation (2K rollouts × 2 temperatures = 4K trajectories; ~1K ALFWorld + 1K GAIA per temperature): ~10–15 H100-hours (ALFWorld ~2–3h; GAIA ~8–12h including tool-call overhead; Qwen/Qwen3-32B BF16 on 1× H100-80GB without quantization). Probe training (3-fold CV × 3-way ablation × logistic/MLP): ~3–5 H100-hours. Pilot tests (50 tasks × 2 benchmarks × 2 conditions × 2 seeds = 400 episodes): ~7–10 H100-hours. Full evaluation (post-pilot, 2 benchmarks × 4 baselines + CascadeWatch): ~25–35 H100-hours. Buffer/debugging: ~5–10 H100-hours. Total: ~50–75 H100-hours.\",\n      \"gpu_hours\": \"~50–75 H100-hours (well within ≤200 H100-hour constraint)\",\n      \"gpu_utilization\": \"~60–70% utilization; human approval gates reduce compute waste on dead-end ablations\",\n      \"timeline\": \"12–14 calendar days (achievable within 16-day constraint with efficient pipeline execution: rollout generation days 1–2, labeling + probe training days 2–4, pilot tests with human review days 4–8, full evaluation days 8–12, analysis and write-up days 10–14)\",\n      \"team\": \"1 researcher, ~2–3 hours/day check-in\",\n      \"claude_api_cost\": \"$150–$250\",\n      \"estimated_gpu_cost\": \"~$100–$150 at ~$2/H100-hour\",\n      \"risk_note\": \"Small labeled training set (200 trajectories) risks MLP overfitting; confirmed-cascade criterion and temperature augmentation strategy are critical human-gate decisions. GAIA contributes approximately 50 of those 200 labeled trajectories (~27 training samples per fold in 3-fold CV), placing the GAIA probe near the minimum viable supervised learning regime—GAIA evaluation results should be treated as preliminary evidence pending replication on a larger annotated set. ALFWorld ERR proxy (game score delta) is a domain adaptation—its F1 contribution must be validated in ablation before committing to full evaluation on ALFWorld. Pilot test (50 tasks × 2 benchmarks) must be reviewed by human before committing to full evaluation on each benchmark. WebShop extension requires an additional ~15–25 H100-hours beyond the primary constraint if pursued.\"\n    },\n    \"auto_research\": {\n      \"note\": \"This mode exceeds the primary ≤200 H100-hour constraint and is presented as an extended evaluation scenario for teams with unrestricted compute, not a valid path within the joint 16-day/200 H100-hour constraint. Included for completeness only.\",\n      \"gpu_hours\": \"~300–450 H100-hours (3–5× more ablations across probe architectures, threshold strategies, feature combinations, augmentation volumes, rollback trigger policies, and minimum-step thresholds; reduced from prior estimates due to Qwen/Qwen3-32B being more compute-efficient than the previously specified 72B model)\",\n      \"gpu_utilization\": \"~85–95%; near-zero idle as agent continuously queues and launches experiments\",\n      \"timeline\": \"3–10 days with 4+ H100s in parallel\",\n      \"team\": \"0 (initial setup only)\",\n      \"claude_api_cost\": \"$350–$600\",\n      \"estimated_gpu_cost\": \"~$600–$900\",\n      \"speed_bottleneck\": \"Number of H100s available; rollout generation dominates throughput\",\n      \"risk_note\": \"Automated cascade label derivation may skip the confirmed-cascade midpoint filter, generating false positive labels; no human oversight to detect always-predict-cascade degenerate solutions. Pilot test pass/fail judgment and Intervention Paradox threshold calculation require human review—an agent may proceed to full evaluation on benchmarks where intervention is net-negative. ALFWorld ERR proxy domain adaptation requires human judgment to validate before scaling.\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 (ARR deadline May 25, 2026)\",\n    \"AAAI 2027 (abstract deadline expected ~August 2026)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"Where LLM Agents Fail and How They can Learn From Failures (arXiv 2509.25370, 2025)\",\n    \"Recoverability Has a Law: The ERR Measure for Tool-Augmented Agents (arXiv 2601.22352, 2026)\",\n    \"The Intervention Paradox: Accurate Failure Prediction in Agents Does Not Imply Effective Failure Prevention (arXiv 2602.03338, 2026)\",\n    \"Capable but Unreliable: Canonical Path Deviation as a Causal Mechanism of Agent Failure in Long-Horizon Tasks (arXiv 2602.19008, 2026)\",\n    \"Trajectory Guard: A Lightweight, Sequence-Aware Model for Real-Time Anomaly Detection in Agentic AI (AAAI TrustAgent Workshop 2026, arXiv 2601.00516)\",\n    \"ProMAS: Proactive Error Forecasting for Multi-Agent Systems Using Markov Transition Dynamics (arXiv 2603.20260, 2026)\",\n    \"From Spark to Fire: Modeling and Mitigating Error Cascades in LLM-Based Multi-Agent Collaboration (arXiv 2603.04474, 2026)\",\n    \"ProbGuard: Probabilistic Runtime Monitoring for LLM Agent Safety (arXiv 2508.00500, 2025)\",\n    \"Auditing Cascading Risks in Multi-Agent Systems via Semantic–Geometric Co-evolution (ICLR Workshop 2026, arXiv 2603.13325)\",\n    \"Crab: A Semantics-Aware Checkpoint/Restore Runtime for Agent Sandboxes (arXiv 2604.28138, 2026)\",\n    \"Reason in Chains, Learn in Trees: Self-Rectification and Grafting for Multi-turn Agent Policy Optimization (arXiv 2604.07165, 2026)\",\n    \"Self-Verification Dilemma: Experience-Driven Suppression of Overused Checking in LLM Reasoning (arXiv 2602.03485, 2026)\",\n    \"Beyond Fluency: Toward Reliable Trajectories in Agentic IR — position paper on failure modes, not empirical cascade measurement (arXiv 2604.04269, 2026)\",\n    \"BacktrackAgent: Enhancing GUI Agent with Error Detection and Backtracking Mechanism (EMNLP 2025, arXiv 2505.20660)\",\n    \"Step Back to Leap Forward: Self-Backtracking for Boosting Reasoning of Language Models (arXiv 2502.04404, 2025)\",\n    \"Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification (arXiv 2504.05419, 2025)\"\n  ],\n  \"description\": \"Long-horizon agent tasks suffer from cascade failures: a single early error propagates across subsequent steps, compounding recovery cost. The critical challenge is the Intervention Paradox (arXiv 2602.03338): a generic critic with AUROC 0.94 causes up to 26 percentage point degradation by disrupting self-correcting trajectories, with all observed regressions occurring at early intervention steps. The solution requires cascade-specific, high-precision detection rather than general failure prediction. We propose CascadeWatch, an inference-time monitor that targets cascade onset specifically using frozen Qwen/Qwen3-32B hidden-state embeddings (HuggingFace: Qwen/Qwen3-32B; 32B dense model; 64GB BF16; fits in 1× H100-80GB without quantization) combined with recoverability delta signals to estimate P(cascade_failure | prefix_k) at each step, with a minimum trigger threshold of step ≥ 5 to avoid the early-step intervention regime where generic critics cause harm. For WebShop and GAIA (tool-augmented benchmarks), recoverability deltas are ERR Efficiency Score deltas (arXiv 2601.22352). For ALFWorld (text-based game with cognitive planning errors, not tool execution failures), ERR Efficiency Score is inapplicable; we use a domain-adapted proxy: step-level delta in the normalized ALFWorld game score, which tracks subgoal completion rate. This domain adaptation is acknowledged as a heuristic extension and is explicitly isolated in the ablation. CascadeWatch is positioned precisely among five distinct neighboring systems. (1) Canonical Path Deviation (arXiv 2602.19008) identifies stochastic drift from canonical solution paths—aggregated from multiple successful runs per task—as a long-horizon failure mechanism, achieving +8.8pp improvement via restart of lowest-adherence runs; CascadeWatch uses single-trajectory recoverability signals (no canonical paths required) and performs targeted rollback rather than full restarts. (2) From Spark to Fire (arXiv 2603.04474) proposes a genealogy-graph governance layer for cascade mitigation in multi-agent collaboration, improving Benign Infection Control Rate from 0.32 to 0.89; CascadeWatch addresses a structurally different failure mode—cognitive cascade failure within a single agent's sequential trajectory—where there are no inter-agent message dependencies. (3) ProMAS (arXiv 2603.20260) raises alerts in multi-agent reasoning but provides no corrective action and evaluates only on the Who&When attribution benchmark. (4) ProbGuard (arXiv 2508.00500) softly intervenes on physical safety constraints via symbolic DTMC. (5) Trajectory Guard (arXiv 2601.00516) uses a Siamese Recurrent Autoencoder with hybrid contrastive-reconstruction loss to detect trajectory anomalies in agentic AI at 32ms, but targets general structural anomalies rather than cascade-specific onset via recoverability signals, evaluates on security audit and multi-agent benchmarks (not ALFWorld/GAIA), and provides no rollback mechanism. Unlike BacktrackAgent (arXiv 2505.20660, EMNLP 2025), which trains a verifier-judger-reflector pipeline for GUI action errors using a task-specific backtracking dataset, CascadeWatch requires no modification to the base agent and does not require retraining the agent backbone; deploying CascadeWatch with a different LLM backbone requires retraining only the lightweight MLP probe (~3–5 H100-hours) against that backbone's embedding space, not retraining the agent itself. Unlike Self-Backtracking (arXiv 2502.04404), which trains the LLM itself to internalize backtracking decisions, CascadeWatch operates as a frozen external probe deployable without model retraining. Prior hidden-state probing work (arXiv 2504.05419) probes single-step reasoning correctness to reduce tokens by 24%; CascadeWatch probes multi-step trajectory prefixes for cascade onset and adds recoverability signals as a second feature channel. CascadeWatch closes the loop on cognitive-task cascades in single-agent long-horizon settings by triggering targeted rollback with a false-positive circuit-breaker (max 2 rollbacks per episode). Rollback mechanism: for ALFWorld, environment-state rollback via command-replay from env.reset() (O(k) game-engine steps; ~25–100ms wall-clock for 50-step episodes; TextWorld's Python API does not expose save/restore for Glulx-format .ulx games; the Crab sandbox, arXiv 2604.28138, provides container-level checkpoint/restore that could support ALFWorld in principle but requires containerization overhead incompatible with standard evaluation setups). For WebShop and GAIA, context-only rollback (agent context rewound to checkpoint; does not undo irreversible web-state changes, acknowledged as a limitation). Cascade labels use a confirmed-cascade criterion (trajectory fails AND root-cause error occurs before the trajectory midpoint) to prevent false labels from partially-recovered trajectories. The GAIA cascade probe operates near the minimum viable supervised learning regime (~27 training samples per fold in 3-fold CV across approximately 50 GAIA-labeled trajectories from AgentErrorBench); GAIA results are treated as preliminary evidence, with ALFWorld (approximately 100 trajectories, ~67 per fold) providing the primary evidence base for the main cascade-avoidance claim. The primary empirical claim is that CascadeWatch achieves task success rate improvement over no-correction baselines on ALFWorld and GAIA while avoiding the performance degradation caused by generic critics (the Intervention Paradox)—demonstrating that cascade-specific precision is sufficient to make rollback net-positive on benchmarks where generic critics fail. The recoverability-delta ablation (embeddings-only vs. recoverability-delta-only vs. combined) serves as an internal validation gate: ≥3% F1 lift from recoverability-delta confirms the ERR-motivated feature design; <3% lift is reported as a negative result. Evaluated on ALFWorld and GAIA as primary benchmarks (WebShop as optional extension), each preceded by the Intervention Paradox's 50-task pilot test to verify net-positive intervention before full evaluation. The compressed HIL execution mode (2 benchmarks, 2K rollouts, 3-fold CV, 2–3 hours/day human engagement) fits within ~50–75 H100-hours and 12–14 calendar days, comfortably within the ≤200 H100-hour and ≤16-day constraints.\",\n  \"project_name\": \"cascade_monitor\",\n  \"source\": \"web_research\"\n}\n\n## Reviewer feedback (round 5)\nIssues: [\"MODERATE — InferAct (arXiv 2407.11843, EMNLP 2025 main track, pages 222–244) is uncited despite being published at the exact target venue and explicitly framing its contribution as 'preemptive detection and correction of misaligned actions in LLM agents.' It uses Theory-of-Mind reasoning (Task Inference Unit + Task Verification Unit) to detect misaligned agent actions before execution and achieves up to 20% Marco-F1 improvement over baselines. EMNLP 2026 reviewers will know this paper and its absence will be a red flag. The distinction from CascadeWatch is real — InferAct targets single-step action misalignment with user intent (e.g., executing a buy action without user authorization) via ToM belief reasoning and requires human-in-loop correction via user alerts; CascadeWatch targets multi-step cascade propagation onset via trajectory-prefix ERR recoverability signals and triggers automated rollback — but these distinctions must be stated explicitly in related work.\", \"MINOR — MASC (arXiv 2510.14319, October 2025, revised January 2026) — 'Metacognitive Self-Correction for Multi-Agent System via Prototype-Guided Next-Execution Reconstruction' — explicitly targets cascading errors in agent systems using history-conditioned embedding anomaly scoring (Next-Execution Reconstruction + Prototype-Guided Enhancement) to trigger step-level correction, achieving +8.47% AUC-ROC on the Who&When benchmark. Though MASC is multi-agent (not single-agent), it uses an embedding-based cascade-targeting mechanism structurally related to CascadeWatch's frozen embedding probe, and its explicit 'cascading errors' framing partially occupies CascadeWatch's conceptual space. A 1–2 sentence mention with differentiation (multi-agent vs. single-agent; unsupervised reconstruction vs. supervised ERR-motivated cascade labels; Who&When vs. ALFWorld/GAIA) is needed to complete the landscape coverage.\"]\nFeedback: All three Round 4 fixes are cleanly implemented. The paper is close to pass-ready. Two targeted additions will close the remaining reviewer exposure:\n\n1. **Add InferAct to §Related Work (required):** 'InferAct [arXiv 2407.11843, EMNLP 2025] uses Theory-of-Mind reasoning to detect actions misaligned with user intent before execution and alerts users for correction, achieving up to 20% Marco-F1 improvement. InferAct addresses single-step action misalignment — whether a specific upcoming action matches user authorization — and relies on human-in-loop correction via user alerts. CascadeWatch addresses a structurally different failure mode: multi-step cascade propagation, where an early-step error compounds across subsequent trajectory steps regardless of user intent; our detection uses trajectory-prefix ERR recoverability signals rather than ToM belief inference, and our intervention is automated rollback rather than human alerting.' This distinction is accurate and defensible; the citation is necessary.\n\n2. **Add MASC to §Related Work (recommended, 1–2 sentences):** 'MASC [arXiv 2510.14319] proposes metacognitive self-correction for multi-agent systems via Prototype-Guided Next-Execution Reconstruction, detecting cascading errors at step level via history-conditioned embedding anomaly scoring and triggering correction agents; CascadeWatch differs in targeting single-agent long-horizon cognitive cascades using supervised ERR-motivated recoverability labels (not unsupervised reconstruction) and evaluating on ALFWorld/GAIA rather than the Who&When multi-agent benchmark.'\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method (approach / resource_estimate / key_references). Do not jump straight to fixing the method if the underlying problem framing needs correction.\n- Address each issue specifically.\n\n## 深度调研要求（每一轮修订都必须执行）\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化这个 idea 的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，建议用 2-3 种不同的搜索查询调研。\n   - 搜索最新的相关论文（arXiv, conference proceedings）\n   - 搜索 benchmark/leaderboard 确认当前 SOTA\n   - 搜索可能遗漏的相关工作和 concurrent work\n\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文的 abstract 和方法部分，\n   不要只依赖搜索摘要。形成你自己对领域现状的独立判断。\n\n3. **深度思考**：在修订之前，先独立思考以下问题：\n   - 这个 idea 的核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach 来解决同一个核心问题？\n   - 修订后的 idea 相比上一版有什么本质性的改进？\n\n4. **避免表面修订**：如果你发现自己只是在换措辞或补充细节而没有实质改进，\n   考虑是否需要 major revision 或 pivot。反复的 minor fix 不会拯救一个根基有问题的 idea。\n\n## 针对 Review 意见的定向搜索\n\n对 reviewer 指出的每个问题，执行以下搜索流程：\n\n1. **如果 reviewer 说'已有类似工作'**：\n   - 搜索 reviewer 提到的论文，用 WebFetch 实际阅读\n   - 搜索该论文的 cited-by，找到后续跟进工作\n   - 明确你的 idea 与这些工作的差异化点——如果差异化不够，必须 pivot\n\n2. **如果 reviewer 说'SOTA 过时'**：\n   - 用 Papers With Code 查看当前排行榜\n   - 搜索过去 6 个月的最新方法\n   - 更新你的 landscape 和 baseline\n\n3. **如果 reviewer 说'可行性有问题'**：\n   - 搜索类似规模实验的实际成本和时间线\n   - 搜索 GitHub 上是否有可复用的实现\n   - 搜索相关数据集/模型的可获取性\n\n4. **如果 reviewer 说'novelty 不足'**：\n   - 对核心方法尽量做 3-5 种不同关键词组合的搜索\n   - 搜索相邻领域是否有类似思路\n   - 如果确实 novelty 不足，考虑 major revision 或 pivot\n\n- Use WebSearch to find updated information if the reviewer flagged outdated claims.\n- You have full freedom in how much to change:\n  - Minor fix: if only specific details are wrong, correct them and keep everything else.\n  - Major revision: if the approach is fundamentally flawed but the core problem is valid, you may redesign the approach entirely.\n  - Pivot: if the reviewer's feedback reveals that the core problem itself is invalid (e.g., the gap no longer exists), you may propose a RELATED but substantially different idea that builds on the same research area. This is preferred over forcing a doomed idea to pass review.\n- The output replaces the original idea (same tracking ID). Whether you make a small tweak or a full pivot, output a COMPLETE JSON object with ALL fields filled.\n- In the output JSON, include a \"change_type\" field with one of: \"minor\", \"major\", or \"pivot\" to indicate the scope of your changes.\n- Output the revised idea as a COMPLETE JSON object (same schema as original, plus \"change_type\").\n\n## 停滞提醒\n这个 idea 已经经过 5 轮修订，近 3 轮的平均分从 3.8 到 3.8，没有明显改善。\n\n请认真思考：\n- 当前方向是否存在根本性的瓶颈？反复的 minor fix 是否在回避核心问题？\n- 如果你认为问题出在 approach 而非 framing，可以做 major revision。\n- 如果你认为 core problem 本身就有问题（gap 不存在、问题不够重要），pivot 到同一研究领域下的新方向可能是更好的选择。\n- 当然，如果你有信心这一轮修订能实现突破，继续改进也完全可以。\n\n最终由你判断——做你认为最能提升 idea 质量的选择。"
}
```

---

### Runtime record

_source line 2 · 2026-05-09T18:40:49.893Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-09T18:40:49.893Z",
  "sessionId": "273dc98c-8ab8-4fa8-9d51-65cb993ef786"
}
```

---

## Round 1

29 recorded events

### User

_source line 3 · 2026-05-09T18:40:49.937Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-09 (UTC).**

## Original idea
{
  "title": "CascadeWatch: Cascade-Onset Detection with Targeted Rollback for Long-Horizon Agent Tasks",
  "core_problem": "In long-horizon agent tasks, individual early-step errors produce cascading downstream failures that grow exponentially more costly to correct with each additional step. The core question is whether a lightweight trained monitor can prospectively detect cascade onset—predicting failure propagation before it fully manifests—to trigger targeted rollback rather than reactive reflection or full replanning. The challenge is not simply detecting failure: the Intervention Paradox (arXiv 2602.03338) establishes that generic critics with AUROC 0.94 cause up to 26 percentage point performance degradation by triggering on non-cascade failures that the agent would have self-corrected. The disruption-recovery tradeoff (Δ Success = p·r − (1−p)·d) only favors intervention on high-failure benchmarks like ALFWorld; it degrades GAIA and HotPotQA even with accurate critics. The solution is not a better generic critic but a cascade-specific one: targeting only the recoverability-degrading prefix patterns that precede confirmed cascades—detectable via recoverability proxy signals—to achieve the high precision (low d) and focused recall (high p conditional on cascade-onset) that shifts the threshold in favor of intervention. A natural alternative early-warning signal is canonical path deviation (arXiv 2602.19008): measuring Jaccard similarity of tool invocations against the convergent set shared across successful runs. This signal is empirically validated but requires aggregating tool invocation sequences from multiple successful runs per task, making it unavailable for novel tasks or low-success-rate settings. CascadeWatch uses ERR Efficiency Score recoverability deltas (arXiv 2601.22352) computable from single trajectories without reference to other runs, enabling cascade detection in the absence of precomputed canonical paths. The rollback mechanism varies by environment affordance: for text-game environments (ALFWorld), full environment-state rollback is achieved via command-replay from env.reset(); for tool-augmented environments (WebShop, GAIA), context-only rollback rewinds the agent's context window. Neither mechanism requires a non-existent API; both are acknowledged to have environment-specific costs and limitations.",
  "opportunity": "The cascade failure pattern is now well-characterized and trainable. AgentErrorBench (arXiv 2509.25370) provides the first systematically annotated failure taxonomy across ALFWorld, WebShop, and GAIA, with root-cause step annotations identifying where cascades originate; memory and reflection errors at steps 5–15 are the most common initiators, crucially occurring mid-trajectory rather than at the earliest steps where the Intervention Paradox shows all regressions occur. The ERR paper (arXiv 2601.22352) formalizes recoverability as Expected Recovery Regret and derives a measurable Efficiency Score proxy, empirically validated across five benchmarks to within δ ≤ 0.05 of observed post-failure regret—establishing that step-level recoverability is observable from trajectory prefixes and thus learnable as a predictive signal. This signal applies directly to tool-augmented agents (WebShop, GAIA) where structured tool-call/result pairs provide natural Efficiency Score observables; for text-game environments (ALFWorld), where failures are cognitive planning errors rather than tool execution failures, a domain-adapted proxy (step-level game score delta) is used instead, acknowledged as a heuristic extension. Canonical Path Deviation (arXiv 2602.19008) provides independent corroboration of the self-reinforcing cascade mechanism in long-horizon tool-use tasks: each off-canonical tool invocation raises the probability that the next invocation is also off-canonical by 22.7 percentage points, confirming that cascade propagation is empirically measurable and compounding. CascadeWatch uses recoverability signals rather than canonical path adherence specifically because recoverability deltas are computable from a single trajectory, enabling deployment where canonical paths from multiple successful runs are unavailable. BacktrackAgent (arXiv 2505.20660, EMNLP 2025) demonstrates that backtracking triggers improve GUI agent task completion on Mobile3M and Auto-UI benchmarks, but requires constructing a task-specific training dataset and fine-tuning the agent components—leaving a clear gap for an external, training-free cascade monitor that operates on any frozen agent in cognitive long-horizon tasks. The proactive detection landscape now includes ProMAS (arXiv 2603.20260) for multi-agent error attribution, ProbGuard (arXiv 2508.00500) for physical safety monitoring, and Trajectory Guard (arXiv 2601.00516) for general structural anomaly detection in agentic trajectories, but none targets cognitive-task cascade failure in single-agent long-horizon settings nor closes the detection-to-rollback loop. The labeled failure datasets, recoverability signals, and the Intervention Paradox's threshold formula together make a specific, testable hypothesis: a cascade-specific monitor using recoverability signals will achieve sufficiently higher precision than generic critics to make rollback net-positive on benchmarks where generic critics fail, for the first time.",
  "landscape": "Proactive monitoring is an active and crowded area that must be navigated carefully. ProMAS (arXiv 2603.20260, March 2026) uses Causal Delta Features mapped to a 30-prototype Vector Markov Space with a frozen Meta-Llama-3.1-8B extractor to predict failure onset in multi-agent collaborative reasoning systems, achieving 22.97% step-level accuracy on the Who&When benchmark (annotated multi-agent dialogues of math and logic puzzles) while processing only 27% of reasoning logs. Critically, ProMAS raises an alert but provides no corrective action—it is a detector only and evaluates exclusively on the Who&When multi-agent attribution benchmark, not on single-agent long-horizon tasks. ProbGuard (arXiv 2508.00500) learns a Discrete-Time Markov Chain from symbolic agent-state abstractions with PAC-style guarantees and triggers prompt-injection interventions when P(unsafe state) exceeds a threshold; it predicts traffic violations up to 38.66 seconds ahead and reduces unsafe behavior by 65.37% in embodied agents, but operates on physical safety constraints using symbolic abstractions rather than frozen neural representations or recoverability signals. Trajectory Guard (arXiv 2601.00516, AAAI TrustAgent Workshop 2026) proposes a Siamese Recurrent Autoencoder with hybrid contrastive-reconstruction loss for real-time anomaly detection in agentic AI trajectories, achieving F1 0.88–0.94 on balanced sets and recall 0.86–0.92 on imbalanced external benchmarks while running 17–27× faster than LLM Judge baselines at 32ms inference. Three distinctions separate this from CascadeWatch: (1) Trajectory Guard detects general structural anomalies—contextual misalignment and sequential incoherence—via reconstruction error, not cascade-specific onset via recoverability-delta signals; (2) it evaluates on synthetic perturbations, security audit failures (RAS-Eval), and multi-agent attribution (Who&When), not on single-agent long-horizon cognitive tasks (ALFWorld, GAIA); (3) it provides no rollback or correction mechanism—detection only. The lightweight framing ('inference-time monitoring of agentic trajectories') directly overlaps with CascadeWatch's positioning, but the two systems target structurally different failure modes: Trajectory Guard's reconstruction error is task-agnostic and catches any structural deviation, while CascadeWatch's recoverability-delta specifically targets the compounding-cost prefix patterns that confirm cascade onset in long-horizon cognitive tasks. The ORC auditing paper (ICLR Workshop 2026, arXiv 2603.13325) detects cascading risks in multi-agent systems via Ollivier-Ricci Curvature on completed interaction graphs—post-hoc auditing, not inference-time intervention. Canonical Path Deviation (arXiv 2602.19008, Feb 2026) is the closest theoretical neighbor to CascadeWatch's cascade-onset framing. Analyzing 515 model-task combinations on the Toolathlon benchmark (22 frontier models, 108 real-world tool-use tasks across 3 independent runs each), Wilson Y. Lee identifies stochastic drift from canonical solution paths—the convergent set of tool invocations shared across successful runs—as a causal mechanism of long-horizon failure. Path adherence is measured as Jaccard similarity between actual and canonical tool invocation sequences; adherence gaps are statistically indistinguishable from zero through the first half of trajectories but become significant and self-reinforcing thereafter, with each off-canonical tool call raising the probability that the next call is also off-canonical by 22.7 percentage points. An intervention restarting the bottom tercile of runs by mid-trajectory canonical adherence achieves +8.8pp success rate improvement. Three distinctions separate this from CascadeWatch: (1) Canonical path adherence requires aggregating tool invocation sequences across multiple successful runs per task—unavailable for novel tasks or low-success-rate settings; CascadeWatch's ERR Efficiency Score recoverability proxy is computable from a single trajectory without reference to other runs. (2) Canonical path deviation detects drift retrospectively via trajectory statistics that become significant only in the second half of execution; CascadeWatch proactively intervenes at steps 5–15 using a trained probe on prefix embeddings, before adherence divergence solidifies. (3) The CPD intervention is a full task restart of lowest-adherence runs; CascadeWatch performs targeted rollback to the pre-cascade checkpoint, preserving valid completed steps and avoiding full re-execution cost. From Spark to Fire (arXiv 2603.04474, March 2026) models cascade error propagation in LLM-based multi-agent collaboration using an individual-based mean-field framework over inter-agent communication graphs, and proposes a genealogy-graph governance layer that tracks atomic claim provenance via NLI-based verification (Green/Red/Yellow status using DeBERTa-v3-small) and blocks transmission of error-carrying messages; the Benign Infection Control Rate (complement of attack success rate) improves from 0.32 to 0.89 across Chain, Mesh, and Star multi-agent topologies on data-analysis, logic, and MMLU tasks. The cascade mechanism is specifically inter-agent: atomic factuality errors injected at one agent propagate through recursive message reuse across rounds of collaboration—a phenomenon requiring multiple communicating agents. CascadeWatch addresses a structurally different failure mode—cognitive cascade failure within a single agent's sequential trajectory (ALFWorld's planning errors, GAIA's tool-call compounding)—where there are no inter-agent message dependencies and no genealogy graph can be constructed. The per-message NLI verification in From Spark to Fire also introduces latency proportional to message volume; CascadeWatch adds only a single 2-layer MLP forward pass per step. The Intervention Paradox (arXiv 2602.03338) is the most important negative result in the space: ROLLBACK and APPEND interventions triggered by a generic LLM critic (AUROC 0.94) degrade performance on HotPotQA by −2.3 to −25.5pp and on GAIA by −4.4 to −30pp; only ALFWorld (high baseline failure rate: 5.8–14.7%) shows improvement (+0.5 to +2.8pp). All observed regressions occur with early-step (step ≤ 2) interventions. BacktrackAgent (arXiv 2505.20660, EMNLP 2025) trains a verifier-judger-reflector pipeline for GUI agents (Mobile3M, Auto-UI benchmarks) to detect individual action errors and trigger backtracking. Unlike CascadeWatch, BacktrackAgent requires constructing a task-specific training dataset and fine-tuning the agent's backtracking components; it targets GUI action-level errors (click/type correctness) rather than recoverability-degrading cascade onset in cognitive long-horizon tasks, and provides no recoverability signal. Self-Backtracking (arXiv 2502.04404) trains the base LLM to internalize when and where to backtrack during training and inference, achieving over 40% performance gains over optimal-path SFT baselines in general reasoning. This approach requires model retraining and modifies the agent's internal reasoning; CascadeWatch operates as a frozen external probe on any pre-trained agent, requiring no modification to the agent and no access to model weights or training infrastructure. Deploying CascadeWatch with a different LLM backbone requires retraining only the lightweight MLP probe (~3–5 H100-hours) against that backbone's embedding space—not retraining the backbone itself. Prior work probes LLM hidden states for single-step answer correctness in mathematical reasoning (arXiv 2504.05419), achieving 24% token reduction via early exit by detecting when intermediate reasoning steps are correct. The mechanism is structurally similar to CascadeWatch's frozen embedding + MLP probe, but targets single-step step-level correctness rather than multi-step cascade onset in agent trajectories; crucially, it adds no recoverability signal channel and does not address long-horizon failure propagation. Reactive self-correction methods share the same fundamental limitation: ExpeL and Contextual Experience Replay distill past trajectories for future improvement; self-verification (arXiv 2602.03485) confirms rechecks rarely identify errors; T-STAR (arXiv 2604.07165) achieves training-time divergence detection via Cognitive Trees but adds no inference-time mechanism. No existing system combines cascade-specific detection using recoverability signals with targeted rollback and a false-positive circuit-breaker, nor validates that cascade-specific precision avoids the Intervention Paradox's disruption-recovery tradeoff.",
  "approach": "We train CascadeWatch to address the Intervention Paradox by targeting only the recoverability-degrading mid-trajectory patterns that precede confirmed cascades. Training data: AgentErrorBench's 200 expert-annotated trajectories (davide221/agenterrorbench on HuggingFace, spanning ALFWorld, WebShop, and GAIA) augmented with ~5,000 synthetic rollouts from Qwen/Qwen3-32B (HuggingFace: Qwen/Qwen3-32B; 32B dense model; 64GB BF16; fits in 1× H100-80GB without quantization—the Qwen3-72B designation referenced in earlier drafts corresponds to unofficial community merges and lacks an authoritative reproducible checkpoint) sampled at three temperatures (0.7, 1.0, 1.3) to increase failure-mode diversity. Cascade labels use a confirmed-cascade criterion: a step k is labeled cascade-onset only if (1) the trajectory ultimately fails, (2) step k is at or after the earliest annotated root-cause error, AND (3) the root-cause error occurs before the trajectory midpoint (step ≤ ⌊total_steps / 2⌋)—this filters out partially-recovered trajectories and prevents false cascade labels from error-tolerant agents. A minimum intervention threshold of step ≥ 5 is imposed at inference time, consistent with AgentErrorBench's finding that cascade-initiating errors occur at steps 5–15 and with the Intervention Paradox's finding that all observed regressions involve step ≤ 2 interventions. Each trajectory prefix at step k is represented by concatenating (a) frozen Qwen/Qwen3-32B hidden-state embeddings (mean-pooled last 4 transformer layers over the action–observation sequence) with (b) recoverability delta signals. For WebShop and GAIA (tool-augmented benchmarks with structured tool-call/result pairs), these are ERR Efficiency Score deltas as defined in arXiv 2601.22352. For ALFWorld (a text-based game where failures are cognitive planning errors rather than tool execution failures, and which lacks structured tool-call pairs), ERR Efficiency Score is not directly applicable; we substitute a domain-adapted proxy: step-level delta in the normalized ALFWorld game score (Δ(info['score'] / info['max_score']) at each step), which tracks incremental subgoal-completion rate. This is an acknowledged heuristic extension of the ERR framework; whether the recoverability motivation holds for this proxy is explicitly tested in the ablation. A 2-layer MLP probe (with L2 weight decay 1e-4) outputs P(cascade | prefix_k), with Platt scaling applied on a stratified held-out validation split. Training data sparsity (200 labeled trajectories) is addressed by (i) 5-fold cross-validation stratified by benchmark (ALFWorld / WebShop / GAIA) to estimate generalization without benchmark leakage, and (ii) a parallel logistic probe baseline to assess whether MLP complexity is justified over this small labeled set. The AgentErrorBench annotations are distributed unevenly across benchmarks: GAIA contributes approximately 50 of the 200 labeled trajectories, yielding roughly 27 training samples per fold in 3-fold CV (the compressed HIL mode), placing the GAIA cascade probe near the minimum viable supervised learning regime; GAIA results are consequently treated as preliminary evidence, with ALFWorld (approximately 100 trajectories, ~67 per fold) providing the primary evidence base for the main cascade-avoidance claim. CascadeWatch requires no modification to the base agent and does not require retraining the agent backbone; deploying CascadeWatch with a different LLM backbone requires retraining only the lightweight MLP probe (~3–5 H100-hours) against that backbone's embedding space, not retraining the agent itself. This is a meaningful practical advantage over BacktrackAgent, which requires constructing a task-specific training dataset and fine-tuning agent components. The rollback mechanism is specified per benchmark: For ALFWorld, environment-state rollback is performed via command-replay from env.reset(): the TextWorld gym environment is reset to the initial observation, then the k−1 accepted actions from the checkpoint buffer are re-executed sequentially to reconstruct game state at step k−1. The ALFWorld game engine processes each text command in approximately 1–2ms; for typical episodes capped at 50 steps, rollback at step k incurs roughly 25–100ms wall-clock overhead—negligible relative to LLM inference time. A checkpoint buffer stores accepted action sequences at each step to enable replay without re-querying the LLM. Note that TextWorld's Python API does not expose a save/restore mechanism for Glulx-format (.ulx) games used in ALFWorld competition settings, so command-replay is the correct mechanism; the O(k) replay cost is in game-engine steps, not LLM compute. The Crab sandbox (arXiv 2604.28138) provides semantics-aware container-level checkpoint/restore that could in principle support ALFWorld game-state snapshots regardless of the underlying game engine; CascadeWatch uses command-replay to maintain compatibility with standard ALFWorld evaluation setups that do not use containerized sandboxes, and to avoid container-spinup overhead that would dominate the ~25–100ms rollback budget. For WebShop and GAIA, context-only rollback rewinds the agent context window to step k_checkpoint, masks all subsequent actions and observations, and re-samples an alternative action with temperature +0.3. Context-only rollback does not undo irreversible WebShop web-state changes (e.g., submitted searches), which is explicitly noted as a limitation. A false-positive circuit-breaker limits rollback to a maximum of 2 triggers per episode; after the second trigger, monitoring is suspended for the remainder of the episode to prevent compounding disruption. Before full evaluation, we run the Intervention Paradox's 50-task pilot test on each benchmark to empirically verify that CascadeWatch's cascade-specific intervention is net-positive (p > d/(r+d)) on that benchmark; benchmarks where the pilot test fails are reported as negative results, not omitted. We include a pre-registered 3-way ablation: (a) frozen embeddings only → logistic probe, (b) recoverability-delta features only → logistic regression (no embeddings), (c) full CascadeWatch (embeddings + recoverability-delta) → 2-layer MLP. The primary empirical claim is that CascadeWatch achieves task success rate improvement over no-correction baselines on ALFWorld and GAIA while avoiding the performance degradation caused by generic critics observed in the Intervention Paradox—demonstrating for the first time that cascade-specific precision is sufficient to make rollback net-positive on benchmarks where generic critics fail. The recoverability-delta ablation serves as an internal validation gate: if recoverability-delta provides ≥3% F1 lift over frozen embeddings alone, the ERR-motivated feature design is empirically confirmed; if the lift is <3%, the theoretical ERR motivation weakens substantially and this is reported honestly as a negative result on the recoverability signal hypothesis. We evaluate task success rate, steps saved per episode, and false-positive intervention rate against no-correction, ExpeL-style reflection, self-verification, T-STAR offline, and ProMAS-style detection-only baselines on ALFWorld, WebShop, and GAIA (subject to pilot test results).",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~100-140 H100-hours total: rollout generation ~45 H100-hours (Qwen/Qwen3-32B runs in BF16 on 1× H100-80GB without quantization—32B × 2 bytes ≈ 64GB, within the 80GB VRAM budget; inference throughput roughly doubles relative to a 72B model; ~45h covers ~5K synthetic rollouts across three benchmarks at three temperatures, including environment interaction overhead and tool-call latency for GAIA tasks); probe training ~10 H100-hours (5-fold CV × 3-way ablation × logistic/MLP variants; these are small models, <1h each); evaluation runs ~45–85 H100-hours across three benchmarks + pilot tests (50 tasks × 3 benchmarks × 2 conditions per test). ALFWorld command-replay rollback adds <1 H100-hour overhead across all evaluation episodes.",
      "gpu_utilization": "~30–40% effective utilization; high idle between human coding, debugging, and analysis cycles",
      "timeline": "4–6 months",
      "team": "2 researchers",
      "estimated_gpu_cost": "~$200–$280 at ~$2/H100-hour"
    },
    "human_in_loop": {
      "scope_note": "Compressed to satisfy the joint ≤16-day calendar / ≤200 H100-hour constraint. Primary benchmarks reduced to ALFWorld + GAIA (2 of 3); WebShop deferred to optional extension after primary evaluation completes. Synthetic rollouts reduced to 2,000 total at 2 temperatures (T=0.7, T=1.0); 3-fold CV replaces 5-fold. Human gates: cascade label validation, pilot test pass/fail judgment per benchmark, ablation design review, threshold decisions. Human engagement: 2–3 hours/day (not 30 min/day).",
      "compute_breakdown": "Rollout generation (2K rollouts × 2 temperatures = 4K trajectories; ~1K ALFWorld + 1K GAIA per temperature): ~10–15 H100-hours (ALFWorld ~2–3h; GAIA ~8–12h including tool-call overhead; Qwen/Qwen3-32B BF16 on 1× H100-80GB without quantization). Probe training (3-fold CV × 3-way ablation × logistic/MLP): ~3–5 H100-hours. Pilot tests (50 tasks × 2 benchmarks × 2 conditions × 2 seeds = 400 episodes): ~7–10 H100-hours. Full evaluation (post-pilot, 2 benchmarks × 4 baselines + CascadeWatch): ~25–35 H100-hours. Buffer/debugging: ~5–10 H100-hours. Total: ~50–75 H100-hours.",
      "gpu_hours": "~50–75 H100-hours (well within ≤200 H100-hour constraint)",
      "gpu_utilization": "~60–70% utilization; human approval gates reduce compute waste on dead-end ablations",
      "timeline": "12–14 calendar days (achievable within 16-day constraint with efficient pipeline execution: rollout generation days 1–2, labeling + probe training days 2–4, pilot tests with human review days 4–8, full evaluation days 8–12, analysis and write-up days 10–14)",
      "team": "1 researcher, ~2–3 hours/day check-in",
      "claude_api_cost": "$150–$250",
      "estimated_gpu_cost": "~$100–$150 at ~$2/H100-hour",
      "risk_note": "Small labeled training set (200 trajectories) risks MLP overfitting; confirmed-cascade criterion and temperature augmentation strategy are critical human-gate decisions. GAIA contributes approximately 50 of those 200 labeled trajectories (~27 training samples per fold in 3-fold CV), placing the GAIA probe near the minimum viable supervised learning regime—GAIA evaluation results should be treated as preliminary evidence pending replication on a larger annotated set. ALFWorld ERR proxy (game score delta) is a domain adaptation—its F1 contribution must be validated in ablation before committing to full evaluation on ALFWorld. Pilot test (50 tasks × 2 benchmarks) must be reviewed by human before committing to full evaluation on each benchmark. WebShop extension requires an additional ~15–25 H100-hours beyond the primary constraint if pursued."
    },
    "auto_research": {
      "note": "This mode exceeds the primary ≤200 H100-hour constraint and is presented as an extended evaluation scenario for teams with unrestricted compute, not a valid path within the joint 16-day/200 H100-hour constraint. Included for completeness only.",
      "gpu_hours": "~300–450 H100-hours (3–5× more ablations across probe architectures, threshold strategies, feature combinations, augmentation volumes, rollback trigger policies, and minimum-step thresholds; reduced from prior estimates due to Qwen/Qwen3-32B being more compute-efficient than the previously specified 72B model)",
      "gpu_utilization": "~85–95%; near-zero idle as agent continuously queues and launches experiments",
      "timeline": "3–10 days with 4+ H100s in parallel",
      "team": "0 (initial setup only)",
      "claude_api_cost": "$350–$600",
      "estimated_gpu_cost": "~$600–$900",
      "speed_bottleneck": "Number of H100s available; rollout generation dominates throughput",
      "risk_note": "Automated cascade label derivation may skip the confirmed-cascade midpoint filter, generating false positive labels; no human oversight to detect always-predict-cascade degenerate solutions. Pilot test pass/fail judgment and Intervention Paradox threshold calculation require human review—an agent may proceed to full evaluation on benchmarks where intervention is net-negative. ALFWorld ERR proxy domain adaptation requires human judgment to validate before scaling."
    }
  },
  "target_venues": [
    "EMNLP 2026 (ARR deadline May 25, 2026)",
    "AAAI 2027 (abstract deadline expected ~August 2026)"
  ],
  "level": "solid",
  "key_references": [
    "Where LLM Agents Fail and How They can Learn From Failures (arXiv 2509.25370, 2025)",
    "Recoverability Has a Law: The ERR Measure for Tool-Augmented Agents (arXiv 2601.22352, 2026)",
    "The Intervention Paradox: Accurate Failure Prediction in Agents Does Not Imply Effective Failure Prevention (arXiv 2602.03338, 2026)",
    "Capable but Unreliable: Canonical Path Deviation as a Causal Mechanism of Agent Failure in Long-Horizon Tasks (arXiv 2602.19008, 2026)",
    "Trajectory Guard: A Lightweight, Sequence-Aware Model for Real-Time Anomaly Detection in Agentic AI (AAAI TrustAgent Workshop 2026, arXiv 2601.00516)",
    "ProMAS: Proactive Error Forecasting for Multi-Agent Systems Using Markov Transition Dynamics (arXiv 2603.20260, 2026)",
    "From Spark to Fire: Modeling and Mitigating Error Cascades in LLM-Based Multi-Agent Collaboration (arXiv 2603.04474, 2026)",
    "ProbGuard: Probabilistic Runtime Monitoring for LLM Agent Safety (arXiv 2508.00500, 2025)",
    "Auditing Cascading Risks in Multi-Agent Systems via Semantic–Geometric Co-evolution (ICLR Workshop 2026, arXiv 2603.13325)",
    "Crab: A Semantics-Aware Checkpoint/Restore Runtime for Agent Sandboxes (arXiv 2604.28138, 2026)",
    "Reason in Chains, Learn in Trees: Self-Rectification and Grafting for Multi-turn Agent Policy Optimization (arXiv 2604.07165, 2026)",
    "Self-Verification Dilemma: Experience-Driven Suppression of Overused Checking in LLM Reasoning (arXiv 2602.03485, 2026)",
    "Beyond Fluency: Toward Reliable Trajectories in Agentic IR — position paper on failure modes, not empirical cascade measurement (arXiv 2604.04269, 2026)",
    "BacktrackAgent: Enhancing GUI Agent with Error Detection and Backtracking Mechanism (EMNLP 2025, arXiv 2505.20660)",
    "Step Back to Leap Forward: Self-Backtracking for Boosting Reasoning of Language Models (arXiv 2502.04404, 2025)",
    "Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification (arXiv 2504.05419, 2025)"
  ],
  "description": "Long-horizon agent tasks suffer from cascade failures: a single early error propagates across subsequent steps, compounding recovery cost. The critical challenge is the Intervention Paradox (arXiv 2602.03338): a generic critic with AUROC 0.94 causes up to 26 percentage point degradation by disrupting self-correcting trajectories, with all observed regressions occurring at early intervention steps. The solution requires cascade-specific, high-precision detection rather than general failure prediction. We propose CascadeWatch, an inference-time monitor that targets cascade onset specifically using frozen Qwen/Qwen3-32B hidden-state embeddings (HuggingFace: Qwen/Qwen3-32B; 32B dense model; 64GB BF16; fits in 1× H100-80GB without quantization) combined with recoverability delta signals to estimate P(cascade_failure | prefix_k) at each step, with a minimum trigger threshold of step ≥ 5 to avoid the early-step intervention regime where generic critics cause harm. For WebShop and GAIA (tool-augmented benchmarks), recoverability deltas are ERR Efficiency Score deltas (arXiv 2601.22352). For ALFWorld (text-based game with cognitive planning errors, not tool execution failures), ERR Efficiency Score is inapplicable; we use a domain-adapted proxy: step-level delta in the normalized ALFWorld game score, which tracks subgoal completion rate. This domain adaptation is acknowledged as a heuristic extension and is explicitly isolated in the ablation. CascadeWatch is positioned precisely among five distinct neighboring systems. (1) Canonical Path Deviation (arXiv 2602.19008) identifies stochastic drift from canonical solution paths—aggregated from multiple successful runs per task—as a long-horizon failure mechanism, achieving +8.8pp improvement via restart of lowest-adherence runs; CascadeWatch uses single-trajectory recoverability signals (no canonical paths required) and performs targeted rollback rather than full restarts. (2) From Spark to Fire (arXiv 2603.04474) proposes a genealogy-graph governance layer for cascade mitigation in multi-agent collaboration, improving Benign Infection Control Rate from 0.32 to 0.89; CascadeWatch addresses a structurally different failure mode—cognitive cascade failure within a single agent's sequential trajectory—where there are no inter-agent message dependencies. (3) ProMAS (arXiv 2603.20260) raises alerts in multi-agent reasoning but provides no corrective action and evaluates only on the Who&When attribution benchmark. (4) ProbGuard (arXiv 2508.00500) softly intervenes on physical safety constraints via symbolic DTMC. (5) Trajectory Guard (arXiv 2601.00516) uses a Siamese Recurrent Autoencoder with hybrid contrastive-reconstruction loss to detect trajectory anomalies in agentic AI at 32ms, but targets general structural anomalies rather than cascade-specific onset via recoverability signals, evaluates on security audit and multi-agent benchmarks (not ALFWorld/GAIA), and provides no rollback mechanism. Unlike BacktrackAgent (arXiv 2505.20660, EMNLP 2025), which trains a verifier-judger-reflector pipeline for GUI action errors using a task-specific backtracking dataset, CascadeWatch requires no modification to the base agent and does not require retraining the agent backbone; deploying CascadeWatch with a different LLM backbone requires retraining only the lightweight MLP probe (~3–5 H100-hours) against that backbone's embedding space, not retraining the agent itself. Unlike Self-Backtracking (arXiv 2502.04404), which trains the LLM itself to internalize backtracking decisions, CascadeWatch operates as a frozen external probe deployable without model retraining. Prior hidden-state probing work (arXiv 2504.05419) probes single-step reasoning correctness to reduce tokens by 24%; CascadeWatch probes multi-step trajectory prefixes for cascade onset and adds recoverability signals as a second feature channel. CascadeWatch closes the loop on cognitive-task cascades in single-agent long-horizon settings by triggering targeted rollback with a false-positive circuit-breaker (max 2 rollbacks per episode). Rollback mechanism: for ALFWorld, environment-state rollback via command-replay from env.reset() (O(k) game-engine steps; ~25–100ms wall-clock for 50-step episodes; TextWorld's Python API does not expose save/restore for Glulx-format .ulx games; the Crab sandbox, arXiv 2604.28138, provides container-level checkpoint/restore that could support ALFWorld in principle but requires containerization overhead incompatible with standard evaluation setups). For WebShop and GAIA, context-only rollback (agent context rewound to checkpoint; does not undo irreversible web-state changes, acknowledged as a limitation). Cascade labels use a confirmed-cascade criterion (trajectory fails AND root-cause error occurs before the trajectory midpoint) to prevent false labels from partially-recovered trajectories. The GAIA cascade probe operates near the minimum viable supervised learning regime (~27 training samples per fold in 3-fold CV across approximately 50 GAIA-labeled trajectories from AgentErrorBench); GAIA results are treated as preliminary evidence, with ALFWorld (approximately 100 trajectories, ~67 per fold) providing the primary evidence base for the main cascade-avoidance claim. The primary empirical claim is that CascadeWatch achieves task success rate improvement over no-correction baselines on ALFWorld and GAIA while avoiding the performance degradation caused by generic critics (the Intervention Paradox)—demonstrating that cascade-specific precision is sufficient to make rollback net-positive on benchmarks where generic critics fail. The recoverability-delta ablation (embeddings-only vs. recoverability-delta-only vs. combined) serves as an internal validation gate: ≥3% F1 lift from recoverability-delta confirms the ERR-motivated feature design; <3% lift is reported as a negative result. Evaluated on ALFWorld and GAIA as primary benchmarks (WebShop as optional extension), each preceded by the Intervention Paradox's 50-task pilot test to verify net-positive intervention before full evaluation. The compressed HIL execution mode (2 benchmarks, 2K rollouts, 3-fold CV, 2–3 hours/day human engagement) fits within ~50–75 H100-hours and 12–14 calendar days, comfortably within the ≤200 H100-hour and ≤16-day constraints.",
  "project_name": "cascade_monitor",
  "source": "web_research"
}

## Reviewer feedback (round 5)
Issues: ["MODERATE — InferAct (arXiv 2407.11843, EMNLP 2025 main track, pages 222–244) is uncited despite being published at the exact target venue and explicitly framing its contribution as 'preemptive detection and correction of misaligned actions in LLM agents.' It uses Theory-of-Mind reasoning (Task Inference Unit + Task Verification Unit) to detect misaligned agent actions before execution and achieves up to 20% Marco-F1 improvement over baselines. EMNLP 2026 reviewers will know this paper and its absence will be a red flag. The distinction from CascadeWatch is real — InferAct targets single-step action misalignment with user intent (e.g., executing a buy action without user authorization) via ToM belief reasoning and requires human-in-loop correction via user alerts; CascadeWatch targets multi-step cascade propagation onset via trajectory-prefix ERR recoverability signals and triggers automated rollback — but these distinctions must be stated explicitly in related work.", "MINOR — MASC (arXiv 2510.14319, October 2025, revised January 2026) — 'Metacognitive Self-Correction for Multi-Agent System via Prototype-Guided Next-Execution Reconstruction' — explicitly targets cascading errors in agent systems using history-conditioned embedding anomaly scoring (Next-Execution Reconstruction + Prototype-Guided Enhancement) to trigger step-level correction, achieving +8.47% AUC-ROC on the Who&When benchmark. Though MASC is multi-agent (not single-agent), it uses an embedding-based cascade-targeting mechanism structurally related to CascadeWatch's frozen embedding probe, and its explicit 'cascading errors' framing partially occupies CascadeWatch's conceptual space. A 1–2 sentence mention with differentiation (multi-agent vs. single-agent; unsupervised reconstruction vs. supervised ERR-motivated cascade labels; Who&When vs. ALFWorld/GAIA) is needed to complete the landscape coverage."]
Feedback: All three Round 4 fixes are cleanly implemented. The paper is close to pass-ready. Two targeted additions will close the remaining reviewer exposure:

1. **Add InferAct to §Related Work (required):** 'InferAct [arXiv 2407.11843, EMNLP 2025] uses Theory-of-Mind reasoning to detect actions misaligned with user intent before execution and alerts users for correction, achieving up to 20% Marco-F1 improvement. InferAct addresses single-step action misalignment — whether a specific upcoming action matches user authorization — and relies on human-in-loop correction via user alerts. CascadeWatch addresses a structurally different failure mode: multi-step cascade propagation, where an early-step error compounds across subsequent trajectory steps regardless of user intent; our detection uses trajectory-prefix ERR recoverability signals rather than ToM belief inference, and our intervention is automated rollback rather than human alerting.' This distinction is accurate and defensible; the citation is necessary.

2. **Add MASC to §Related Work (recommended, 1–2 sentences):** 'MASC [arXiv 2510.14319] proposes metacognitive self-correction for multi-agent systems via Prototype-Guided Next-Execution Reconstruction, detecting cascading errors at step level via history-conditioned embedding anomaly scoring and triggering correction agents; CascadeWatch differs in targeting single-agent long-horizon cognitive cascades using supervised ERR-motivated recoverability labels (not unsupervised reconstruction) and evaluating on ALFWorld/GAIA rather than the Who&When multi-agent benchmark.'

## Instructions
- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method (approach / resource_estimate / key_references). Do not jump straight to fixing the method if the underlying problem framing needs correction.
- Address each issue specifically.

## 深度调研要求（每一轮修订都必须执行）

不要简单地'打补丁'——每一轮修订都是重新审视和深化这个 idea 的机会。

1. **深度搜索**：针对 reviewer 指出的每个问题，建议用 2-3 种不同的搜索查询调研。
   - 搜索最新的相关论文（arXiv, conference proceedings）
   - 搜索 benchmark/leaderboard 确认当前 SOTA
   - 搜索可能遗漏的相关工作和 concurrent work

2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文的 abstract 和方法部分，
   不要只依赖搜索摘要。形成你自己对领域现状的独立判断。

3. **深度思考**：在修订之前，先独立思考以下问题：
   - 这个 idea 的核心假设是否仍然成立？
   - reviewer 的批评是否揭示了更深层的问题？
   - 有没有更好的 framing 或 approach 来解决同一个核心问题？
   - 修订后的 idea 相比上一版有什么本质性的改进？

4. **避免表面修订**：如果你发现自己只是在换措辞或补充细节而没有实质改进，
   考虑是否需要 major revision 或 pivot。反复的 minor fix 不会拯救一个根基有问题的 idea。

## 针对 Review 意见的定向搜索

对 reviewer 指出的每个问题，执行以下搜索流程：

1. **如果 reviewer 说'已有类似工作'**：
   - 搜索 reviewer 提到的论文，用 WebFetch 实际阅读
   - 搜索该论文的 cited-by，找到后续跟进工作
   - 明确你的 idea 与这些工作的差异化点——如果差异化不够，必须 pivot

2. **如果 reviewer 说'SOTA 过时'**：
   - 用 Papers With Code 查看当前排行榜
   - 搜索过去 6 个月的最新方法
   - 更新你的 landscape 和 baseline

3. **如果 reviewer 说'可行性有问题'**：
   - 搜索类似规模实验的实际成本和时间线
   - 搜索 GitHub 上是否有可复用的实现
   - 搜索相关数据集/模型的可获取性

4. **如果 reviewer 说'novelty 不足'**：
   - 对核心方法尽量做 3-5 种不同关键词组合的搜索
   - 搜索相邻领域是否有类似思路
   - 如果确实 novelty 不足，考虑 major revision 或 pivot

- Use WebSearch to find updated information if the reviewer flagged outdated claims.
- You have full freedom in how much to change:
  - Minor fix: if only specific details are wrong, correct them and keep everything else.
  - Major revision: if the approach is fundamentally flawed but the core problem is valid, you may redesign the approach entirely.
  - Pivot: if the reviewer's feedback reveals that the core problem itself is invalid (e.g., the gap no longer exists), you may propose a RELATED but substantially different idea that builds on the same research area. This is preferred over forcing a doomed idea to pass review.
- The output replaces the original idea (same tracking ID). Whether you make a small tweak or a full pivot, output a COMPLETE JSON object with ALL fields filled.
- In the output JSON, include a "change_type" field with one of: "minor", "major", or "pivot" to indicate the scope of your changes.
- Output the revised idea as a COMPLETE JSON object (same schema as original, plus "change_type").

## 停滞提醒
这个 idea 已经经过 5 轮修订，近 3 轮的平均分从 3.8 到 3.8，没有明显改善。

请认真思考：
- 当前方向是否存在根本性的瓶颈？反复的 minor fix 是否在回避核心问题？
- 如果你认为问题出在 approach 而非 framing，可以做 major revision。
- 如果你认为 core problem 本身就有问题（gap 不存在、问题不够重要），pivot 到同一研究领域下的新方向可能是更好的选择。
- 当然，如果你有信心这一轮修订能实现突破，继续改进也完全可以。

最终由你判断——做你认为最能提升 idea 质量的选择。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "438b2a64-25e3-4fd7-bd11-ea7d73d2ec1f",
  "type": "user",
  "uuid": "722d73d6-2852-414d-870f-310d7997267c",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "273dc98c-8ab8-4fa8-9d51-65cb993ef786",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-09T18:40:49.934Z_

```json
{
  "parentUuid": "722d73d6-2852-414d-870f-310d7997267c",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "AskUserQuestion",
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
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "AskUserQuestion",
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
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "ed6c92d5-8a8c-4fc8-9bb1-de34c0f9ccc4",
  "timestamp": "2026-05-09T18:40:49.934Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "273dc98c-8ab8-4fa8-9d51-65cb993ef786",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-09T18:40:49.934Z_

```json
{
  "parentUuid": "ed6c92d5-8a8c-4fc8-9bb1-de34c0f9ccc4",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "3f33d4d2-9966-4279-a3c5-a3924335b41e",
  "timestamp": "2026-05-09T18:40:49.934Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "273dc98c-8ab8-4fa8-9d51-65cb993ef786",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-09 (UTC).**  ## Original idea {   \"title\": \"CascadeWatch: Cascade-Onset Detection with Targeted Rollback for Long-…",
  "leafUuid": "3f33d4d2-9966-4279-a3c5-a3924335b41e",
  "sessionId": "273dc98c-8ab8-4fa8-9d51-65cb993ef786"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Cascade-aware agent rollback with recoverability signals",
  "sessionId": "273dc98c-8ab8-4fa8-9d51-65cb993ef786"
}
```

---

### Assistant

_source line 8 · 2026-05-09T18:41:07.240Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the situation carefully before deciding on the best course of action.

**Current state:**
- This is round 5 of revisions
- The paper has been stuck at ~3.8 average score for ~3 rounds
- The reviewer feedback this round is relatively minor (two missing citations - one moderate, one minor)
- The feedback is actionable: add InferAct and MASC to related work

**Key question: Should I do a minor fix, major revision, or pivot?**

The reviewer feedback this round is specifically about two missing citations:
1. InferAct (arXiv 2407.11843, EMNLP 2025) - MODERATE issue, same target venue


2. MASC (arXiv 2510.14319) - MINOR issue

Both are citation gaps rather than fundamental flaws with the approach. The reviewer explicitly notes that the Round 4 fixes are well-implemented and the paper is "close to pass-ready," which suggests the core idea is solid. However, the fact that the score has plateaued at 3.8 for three rounds makes me wonder if there are deeper issues the reviewer isn't directly addressing. I could take the straightforward path of just adding these two citations to the related work section, which directly addresses what the reviewer flagged.

But I should also consider whether the stagnation points to something more substantial—maybe the novelty isn't compelling enough or there's a subtle flaw in the approach that keeps the score from moving. Given that the reviewer says it's close to pass-ready and the issues are specific and actionable, I think the minor fix approach makes the most sense. I'll research both InferAct and MASC to understand them properly, then integrate them into the landscape with clear differentiation from my work.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f33d4d2-9966-4279-a3c5-a3924335b41e",
  "isSidechain": false,
  "requestId": "req_011CasV4eWYHkPsfYvebt4hd",
  "type": "assistant",
  "uuid": "97010655-0fb4-4e5b-84b4-0a4a11b9248c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "273dc98c-8ab8-4fa8-9d51-65cb993ef786",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_012VSdGb2dhc2328tXMeNgbr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16279,
      "cache_read_input_tokens": 11631,
      "output_tokens": 814,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16279,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 814,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 16279,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16279
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-09T18:41:07.260Z_

Let me research both papers before making any revisions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "97010655-0fb4-4e5b-84b4-0a4a11b9248c",
  "isSidechain": false,
  "requestId": "req_011CasV4eWYHkPsfYvebt4hd",
  "type": "assistant",
  "uuid": "d8f947fa-c85d-468e-9cbe-c1e9fcd6dcc2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "273dc98c-8ab8-4fa8-9d51-65cb993ef786",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_012VSdGb2dhc2328tXMeNgbr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16279,
      "cache_read_input_tokens": 11631,
      "output_tokens": 814,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16279,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 814,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 16279,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16279
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-09T18:41:08.029Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Rgy98WiktLwchTwc2fdUJr`</summary>

```json
{
  "query": "select:WebFetch,WebSearch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8f947fa-c85d-468e-9cbe-c1e9fcd6dcc2",
  "isSidechain": false,
  "requestId": "req_011CasV4eWYHkPsfYvebt4hd",
  "type": "assistant",
  "uuid": "6be4d6d9-4d2e-44ce-a494-8b33936b2ef3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "273dc98c-8ab8-4fa8-9d51-65cb993ef786",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_012VSdGb2dhc2328tXMeNgbr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16279,
      "cache_read_input_tokens": 11631,
      "output_tokens": 814,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16279,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 814,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 16279,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16279
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-09T18:41:08.035Z_

<details><summary>↩ Tool result · `toolu_01Rgy98WiktLwchTwc2fdUJr`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```

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
  "parentUuid": "6be4d6d9-4d2e-44ce-a494-8b33936b2ef3",
  "isSidechain": false,
  "promptId": "438b2a64-25e3-4fd7-bd11-ea7d73d2ec1f",
  "type": "user",
  "uuid": "acab61da-7926-4e52-b4c8-3c0e9bea596c",
  "toolUseResult": {
    "matches": [
      "WebFetch",
      "WebSearch"
    ],
    "query": "select:WebFetch,WebSearch",
    "total_deferred_tools": 17
  },
  "sourceToolAssistantUUID": "6be4d6d9-4d2e-44ce-a494-8b33936b2ef3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "273dc98c-8ab8-4fa8-9d51-65cb993ef786",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-09T18:41:10.487Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me research both papers concurrently.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "acab61da-7926-4e52-b4c8-3c0e9bea596c",
  "isSidechain": false,
  "requestId": "req_011CasV5yseSqFU3qCuMpKTM",
  "type": "assistant",
  "uuid": "eaa9cfc3-2de4-46d4-b3d6-a9dd2817487b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "273dc98c-8ab8-4fa8-9d51-65cb993ef786",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0183MRZxfgwHfqbKuxZFKKzT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1836,
      "cache_read_input_tokens": 27910,
      "output_tokens": 348,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1836,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 348,
          "cache_read_input_tokens": 27910,
          "cache_creation_input_tokens": 1836,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1836
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-09T18:41:10.488Z_

Fetching both papers concurrently before revising.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eaa9cfc3-2de4-46d4-b3d6-a9dd2817487b",
  "isSidechain": false,
  "requestId": "req_011CasV5yseSqFU3qCuMpKTM",
  "type": "assistant",
  "uuid": "4b6c2248-68e4-4647-934e-be5de48752d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "273dc98c-8ab8-4fa8-9d51-65cb993ef786",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0183MRZxfgwHfqbKuxZFKKzT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1836,
      "cache_read_input_tokens": 27910,
      "output_tokens": 348,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1836,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 348,
          "cache_read_input_tokens": 27910,
          "cache_creation_input_tokens": 1836,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1836
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-09T18:41:13.011Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01LMkMa3Axo1AmLi2qYbwbTE`</summary>

```json
{
  "url": "https://arxiv.org/abs/2407.11843",
  "prompt": "Extract: (1) full title, (2) abstract, (3) key method details (Task Inference Unit, Task Verification Unit, Theory-of-Mind reasoning), (4) evaluation benchmarks and metrics, (5) main results, (6) how it handles correction/intervention, (7) what kinds of errors/failures it targets"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b6c2248-68e4-4647-934e-be5de48752d0",
  "isSidechain": false,
  "requestId": "req_011CasV5yseSqFU3qCuMpKTM",
  "type": "assistant",
  "uuid": "204c0cbd-0c7f-47f8-861d-eeaa2b57ac63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "273dc98c-8ab8-4fa8-9d51-65cb993ef786",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0183MRZxfgwHfqbKuxZFKKzT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1836,
      "cache_read_input_tokens": 27910,
      "output_tokens": 348,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1836,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 348,
          "cache_read_input_tokens": 27910,
          "cache_creation_input_tokens": 1836,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1836
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-09T18:41:14.811Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01AHMCoZQA4bVCjm4xYaUYAP`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.14319",
  "prompt": "Extract: (1) full title, (2) abstract, (3) key method details (Next-Execution Reconstruction, Prototype-Guided Enhancement, embedding anomaly scoring), (4) evaluation benchmarks and metrics, (5) main results, (6) how it handles correction/intervention, (7) what kinds of errors/failures it targets, (8) whether it targets single-agent or multi-agent settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "204c0cbd-0c7f-47f8-861d-eeaa2b57ac63",
  "isSidechain": false,
  "requestId": "req_011CasV5yseSqFU3qCuMpKTM",
  "type": "assistant",
  "uuid": "2bff4719-df65-4191-bf06-a97aa73d210c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "273dc98c-8ab8-4fa8-9d51-65cb993ef786",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0183MRZxfgwHfqbKuxZFKKzT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1836,
      "cache_read_input_tokens": 27910,
      "output_tokens": 348,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1836,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 348,
          "cache_read_input_tokens": 27910,
          "cache_creation_input_tokens": 1836,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1836
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-09T18:41:18.517Z_

<details><summary>↩ Tool result · `toolu_01LMkMa3Axo1AmLi2qYbwbTE`</summary>

```text
# InferAct: Preemptive Detection and Correction of Misaligned Actions in LLM Agents

## 1. Full Title
"Preemptive Detection and Correction of Misaligned Actions in LLM Agents"

## 2. Abstract
The paper addresses a critical challenge in deploying LLM-based agents: misalignment between agent behavior and user intent. The authors introduce InferAct, which "leverages the belief reasoning ability of LLMs, grounded in Theory-of-Mind, to detect misaligned actions before execution." Upon detection, the system alerts users for timely correction.

## 3. Key Method Details
The document indicates three core components:
- **Task Inference Unit**: Not explicitly detailed in the provided content
- **Task Verification Unit**: Not explicitly detailed in the provided content
- **Theory-of-Mind Reasoning**: The approach grounds its detection mechanism in Theory-of-Mind principles to identify when agent actions diverge from user intent

## 4. Evaluation Benchmarks and Metrics
The paper evaluated on "three widely used tasks" using Marco-F1 as the primary metric for assessing detection accuracy.

## 5. Main Results
InferAct demonstrated "up to 20% improvements on Marco-F1 against baselines in misaligned action detection." The evaluation also highlighted effectiveness in improving agent alignment through correction mechanisms.

## 6. Correction/Intervention Handling
Upon detecting misalignment, the system "alerts users for timely correction, preventing adverse outcomes" before critical actions execute.

## 7. Error/Failure Types Targeted
The approach targets unintended execution of critical actions—such as "accidentally triggering a 'buy-now' in web shopping"—that could produce irreversible negative consequences.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "204c0cbd-0c7f-47f8-861d-eeaa2b57ac63",
  "isSidechain": false,
  "promptId": "438b2a64-25e3-4fd7-bd11-ea7d73d2ec1f",
  "type": "user",
  "uuid": "93c996a7-9d9d-4a92-829f-55317627963d",
  "toolUseResult": {
    "bytes": 46507,
    "code": 200,
    "codeText": "OK",
    "result": "# InferAct: Preemptive Detection and Correction of Misaligned Actions in LLM Agents\n\n## 1. Full Title\n\"Preemptive Detection and Correction of Misaligned Actions in LLM Agents\"\n\n## 2. Abstract\nThe paper addresses a critical challenge in deploying LLM-based agents: misalignment between agent behavior and user intent. The authors introduce InferAct, which \"leverages the belief reasoning ability of LLMs, grounded in Theory-of-Mind, to detect misaligned actions before execution.\" Upon detection, the system alerts users for timely correction.\n\n## 3. Key Method Details\nThe document indicates three core components:\n- **Task Inference Unit**: Not explicitly detailed in the provided content\n- **Task Verification Unit**: Not explicitly detailed in the provided content\n- **Theory-of-Mind Reasoning**: The approach grounds its detection mechanism in Theory-of-Mind principles to identify when agent actions diverge from user intent\n\n## 4. Evaluation Benchmarks and Metrics\nThe paper evaluated on \"three widely used tasks\" using Marco-F1 as the primary metric for assessing detection accuracy.\n\n## 5. Main Results\nInferAct demonstrated \"up to 20% improvements on Marco-F1 against baselines in misaligned action detection.\" The evaluation also highlighted effectiveness in improving agent alignment through correction mechanisms.\n\n## 6. Correction/Intervention Handling\nUpon detecting misalignment, the system \"alerts users for timely correction, preventing adverse outcomes\" before critical actions execute.\n\n## 7. Error/Failure Types Targeted\nThe approach targets unintended execution of critical actions—such as \"accidentally triggering a 'buy-now' in web shopping\"—that could produce irreversible negative consequences.",
    "durationMs": 5502,
    "url": "https://arxiv.org/abs/2407.11843"
  },
  "sourceToolAssistantUUID": "204c0cbd-0c7f-47f8-861d-eeaa2b57ac63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "273dc98c-8ab8-4fa8-9d51-65cb993ef786",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-09T18:41:20.258Z_

<details><summary>↩ Tool result · `toolu_01AHMCoZQA4bVCjm4xYaUYAP`</summary>

```text
# MASC: Metacognitive Self-Correction for Multi-Agent Systems

## (1) Full Title
"Metacognitive Self-Correction for Multi-Agent System via Prototype-Guided Next-Execution Reconstruction"

## (2) Abstract
The framework addresses brittleness in LLM-based multi-agent systems caused by cascading errors. It provides "real-time, unsupervised, step-level error detection and self-correction" by treating detection as anomaly scoring conditioned on interaction history.

## (3) Key Method Details

**Next-Execution Reconstruction:** Predicts embeddings of upcoming steps from query and interaction history to identify causal inconsistencies.

**Prototype-Guided Enhancement:** Learns a prototype prior representing normal-step embeddings to stabilize reconstruction and anomaly scoring, particularly when context is sparse (early execution steps).

**Anomaly Scoring:** History-conditioned approach combining both mechanisms for step-level error flagging.

## (4) Evaluation Benchmarks and Metrics
- **Benchmark:** Who&When dataset
- **Primary metric:** Step-level error detection measured via AUC-ROC

## (5) Main Results
- Achieves "up to 8.47% AUC-ROC" improvement in step-level error detection over baselines
- Delivers consistent end-to-end gains across diverse MAS frameworks with minimal computational overhead

## (6) Correction/Intervention Mechanism
When an anomaly is detected, the framework "triggers a correction agent to revise the acting agent's output before information flows downstream," preventing error propagation.

## (7) Target Error Types
Cascading errors where "a single faulty step can propagate across agents and disrupt the trajectory."

## (8) Application Setting
**Multi-agent systems** explicitly designed for collaborative problem-solving architectures.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2bff4719-df65-4191-bf06-a97aa73d210c",
  "isSidechain": false,
  "promptId": "438b2a64-25e3-4fd7-bd11-ea7d73d2ec1f",
  "type": "user",
  "uuid": "5473d129-b3e9-4bd4-b0f7-90bb4d49306f",
  "toolUseResult": {
    "bytes": 47693,
    "code": 200,
    "codeText": "OK",
    "result": "# MASC: Metacognitive Self-Correction for Multi-Agent Systems\n\n## (1) Full Title\n\"Metacognitive Self-Correction for Multi-Agent System via Prototype-Guided Next-Execution Reconstruction\"\n\n## (2) Abstract\nThe framework addresses brittleness in LLM-based multi-agent systems caused by cascading errors. It provides \"real-time, unsupervised, step-level error detection and self-correction\" by treating detection as anomaly scoring conditioned on interaction history.\n\n## (3) Key Method Details\n\n**Next-Execution Reconstruction:** Predicts embeddings of upcoming steps from query and interaction history to identify causal inconsistencies.\n\n**Prototype-Guided Enhancement:** Learns a prototype prior representing normal-step embeddings to stabilize reconstruction and anomaly scoring, particularly when context is sparse (early execution steps).\n\n**Anomaly Scoring:** History-conditioned approach combining both mechanisms for step-level error flagging.\n\n## (4) Evaluation Benchmarks and Metrics\n- **Benchmark:** Who&When dataset\n- **Primary metric:** Step-level error detection measured via AUC-ROC\n\n## (5) Main Results\n- Achieves \"up to 8.47% AUC-ROC\" improvement in step-level error detection over baselines\n- Delivers consistent end-to-end gains across diverse MAS frameworks with minimal computational overhead\n\n## (6) Correction/Intervention Mechanism\nWhen an anomaly is detected, the framework \"triggers a correction agent to revise the acting agent's output before information flows downstream,\" preventing error propagation.\n\n## (7) Target Error Types\nCascading errors where \"a single faulty step can propagate across agents and disrupt the trajectory.\"\n\n## (8) Application Setting\n**Multi-agent systems** explicitly designed for collaborative problem-solving architectures.",
    "durationMs": 5443,
    "url": "https://arxiv.org/abs/2510.14319"
  },
  "sourceToolAssistantUUID": "2bff4719-df65-4191-bf06-a97aa73d210c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "273dc98c-8ab8-4fa8-9d51-65cb993ef786",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-09T18:42:10.401Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I now have solid information on both papers. Let me now think carefully about how to integrate them.

**InferAct (arXiv 2407.11843, EMNLP 2025):**
- Full title: "Preemptive Detection and Correction of Misaligned Actions in LLM Agents"
- Uses Theory-of-Mind reasoning to detect actions misaligned with user intent before execution
- Alerts users for correction (human-in-loop)
- Targets single-step misalignment (e.g., buy-now without authorization)
- Up to 20% Marco-F1 improvement


- Evaluated on 3 widely-used tasks

**CascadeWatch distinction from InferAct:**
- InferAct catches single-step action misalignment through ToM belief reasoning and requires human intervention, while CascadeWatch addresses multi-step cascade propagation from early errors using trajectory-prefix ERR signals and performs fully automated rollback
- These represent different failure modes: user-intent misalignment versus cascade propagation

**MASC (arXiv 2510.14319):**
- Full title: "

Metacognitive Self-Correction for Multi-Agent System via Prototype-Guided Next-Execution Reconstruction"
- Uses unsupervised step-level error detection via embedding anomaly scoring, triggering a correction agent when anomalies appear, achieving +8.47% AUC-ROC improvement on Who&When
- CascadeWatch differs by operating on single-agent systems with supervised ERR-motivated labels on ALFWorld/GAIA, specifically targeting cascade onset rather than general anomalies, and performing targeted rollback instead of output revision

Now I'm thinking about why the paper's been stuck at 3.8 for three rounds—the reviewer flagged missing citations for InferAct and MASC, which are genuine gaps that should be straightforward to address. But I want to dig deeper and see if there's something fundamentally limiting the approach that these citation issues might be obscuring. The core method relies on a relatively small dataset of 200 annotated trajectories from AgentErrorBench, uses Qwen embeddings with ERR signals fed into a simple 2-layer MLP, and targets cascade onset starting at step 5 or later. The GAIA evaluation is particularly concerning with only 27 training samples per task.

Looking at the acknowledged limitations though—the small GAIA sample size is already noted, the ALFWorld ERR proxy is already flagged as heuristic, and the Intervention Paradox constraint is carefully handled. The reviewer's explicit "close to pass-ready" comment suggests the foundation is solid, so I don't think there's a hidden flaw requiring a major pivot. My approach is to make the targeted citation additions exactly as the reviewer specified, integrate them into the landscape and description sections, and update the references. The reviewer essentially provided the text I need to incorporate, so it's a matter of placing it naturally within the existing structure.

Now I'm mapping where these papers fit in the current landscape. InferAct focuses on preemptive detection of action misalignment at inference time, so it belongs in that cluster alongside Trajectory Guard and the other single-step correction methods. MASC handles multi-agent cascade error detection through embeddings, which aligns it with the other multi-agent systems like ProMAS and From Spark to Fire. I'll slot them into those respective sections and then update the JSON with the new references and description mentions. uses Theory-of-Mind reasoning to preemptively detect actions misaligned with user intent before execution, achieving up to 20% Marco-F1 improvement in misaligned-action detection across three evaluation tasks. Two distinctions separate InferAct from CascadeWatch: (1) InferAct targets single-step action misalignment—whether a specific upcoming action (e.g., a buy-now command) matches user authorization—via ToM belief inference about user intent; CascadeWatch targets multi-step cascade propagation, where an early-step error compounds across subsequent trajectory steps regardless of user intent, and uses trajectory-prefix ERR recoverability signals rather than ToM belief reasoning. (2) InferAct's intervention is human-in-loop: it alerts the user for correction before the misaligned action executes; CascadeWatch's intervention is automated rollback to a pre-cascade checkpoint, requiring no human availability. The two systems are complementary: InferAct prevents user-unauthorized actions, CascadeWatch prevents self-compounding cascade failures.

For MASC, I'm comparing it against CascadeWatch across three key dimensions: MASC operates on multi-agent systems where errors propagate through message passing between agents, while CascadeWatch focuses on single-agent trajectories where mistakes accumulate within one agent's reasoning chain. Their anomaly detection approaches also differ—MASC uses history-conditioned embedding anomaly scoring, whereas CascadeWatch relies on trajectory-prefix ERR recoverability signals. MASC achieves +8.47% AUC-ROC improvement on the Who&When benchmark through its Prototype-Guided Next-Execution Reconstruction method, which detects cascading errors at the step level and triggers a correction agent to revise outputs before they propagate. InferAct fits best near Trajectory Guard since it's also doing inference-time monitoring, while MASC belongs in the multi-agent cluster alongside ProMAS and From Spark to Fire given its focus on cascade detection across agent interactions.

Now I need to update the JSON carefully, preserving all existing content while integrating these two new papers into the description and positioning them appropriately in the related work section.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5473d129-b3e9-4bd4-b0f7-90bb4d49306f",
  "isSidechain": false,
  "requestId": "req_011CasV6st1ReicXR93YzKn7",
  "type": "assistant",
  "uuid": "751c8586-9cc6-4154-946a-d53a5616920e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "273dc98c-8ab8-4fa8-9d51-65cb993ef786",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01S6pAxNj3tvUGK7fUwSyUpJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1226,
      "cache_read_input_tokens": 29746,
      "output_tokens": 2521,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1226,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2521,
          "cache_read_input_tokens": 29746,
          "cache_creation_input_tokens": 1226,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1226
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-09T18:42:10.548Z_

Good, I have solid information on both papers. Now let me compose the complete revised JSON with targeted additions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "751c8586-9cc6-4154-946a-d53a5616920e",
  "isSidechain": false,
  "requestId": "req_011CasV6st1ReicXR93YzKn7",
  "type": "assistant",
  "uuid": "d3f92230-8292-4981-80d1-92d23f24f2ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "273dc98c-8ab8-4fa8-9d51-65cb993ef786",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01S6pAxNj3tvUGK7fUwSyUpJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1226,
      "cache_read_input_tokens": 29746,
      "output_tokens": 2521,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1226,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2521,
          "cache_read_input_tokens": 29746,
          "cache_creation_input_tokens": 1226,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1226
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-09T18:42:11.562Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01DRsTaHyTDznCn6Ss6nMxtU`</summary>

```json
{
  "description": "Verify InferAct publication details at EMNLP 2025",
  "subagent_type": "Explore",
  "prompt": "Use WebFetch to retrieve https://arxiv.org/abs/2407.11843 and extract: (1) exact paper title, (2) author list, (3) venue confirmation (EMNLP 2025 main track, pages 222–244 or similar), (4) the three evaluation tasks/benchmarks used, (5) what \"Marco-F1\" measures in this context, (6) whether the correction mechanism specifically requires a human-in-the-loop or can be automated. Report in under 200 words."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3f92230-8292-4981-80d1-92d23f24f2ad",
  "isSidechain": false,
  "requestId": "req_011CasV6st1ReicXR93YzKn7",
  "type": "assistant",
  "uuid": "8cb363be-3fa6-417b-b576-f6480c179ae3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "273dc98c-8ab8-4fa8-9d51-65cb993ef786",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01S6pAxNj3tvUGK7fUwSyUpJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1226,
      "cache_read_input_tokens": 29746,
      "output_tokens": 2521,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1226,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2521,
          "cache_read_input_tokens": 29746,
          "cache_creation_input_tokens": 1226,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1226
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Runtime record

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-09 (UTC).**  ## Original idea {   \"title\": \"CascadeWatch: Cascade-Onset Detection with Targeted Rollback for Long-…",
  "leafUuid": "8cb363be-3fa6-417b-b576-f6480c179ae3",
  "sessionId": "273dc98c-8ab8-4fa8-9d51-65cb993ef786"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Cascade-aware agent rollback with recoverability signals",
  "sessionId": "273dc98c-8ab8-4fa8-9d51-65cb993ef786"
}
```

---

### Tool result

_source line 23 · 2026-05-09T18:42:19.759Z_

<details><summary>↩ Tool result · `toolu_01DRsTaHyTDznCn6Ss6nMxtU`</summary>

```text
**Summary of Paper "Preemptive Detection and Correction of Misaligned Actions in LLM Agents":**

**(1) Title:** Preemptive Detection and Correction of Misaligned Actions in LLM Agents

**(2) Authors:** Haishuo Fang, Xiaodan Zhu, Iryna Gurevych

**(3) Venue:** Accepted by EMNLP 2025 (specific page range not available on abstract page)

**(4) Evaluation Tasks:** The paper evaluated on three widely-used tasks, but specific names are not detailed in the abstract content retrieved.

**(5) Marco-F1:** Measures detection accuracy for misaligned actions; the paper reports up to 20% improvements on this metric against baselines.

**(6) Correction Mechanism:** Requires **human-in-the-loop intervention**—InferAct alerts users for timely correction. The abstract does not specify if fully automated correction is also supported.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8cb363be-3fa6-417b-b576-f6480c179ae3",
  "isSidechain": false,
  "promptId": "438b2a64-25e3-4fd7-bd11-ea7d73d2ec1f",
  "type": "user",
  "uuid": "fbfc57de-74c5-47ab-a073-ca6cb42a0f8b",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Use WebFetch to retrieve https://arxiv.org/abs/2407.11843 and extract: (1) exact paper title, (2) author list, (3) venue confirmation (EMNLP 2025 main track, pages 222–244 or similar), (4) the three evaluation tasks/benchmarks used, (5) what \"Marco-F1\" measures in this context, (6) whether the correction mechanism specifically requires a human-in-the-loop or can be automated. Report in under 200 words.",
    "agentId": "ac6401e34dcf51a92",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "**Summary of Paper \"Preemptive Detection and Correction of Misaligned Actions in LLM Agents\":**\n\n**(1) Title:** Preemptive Detection and Correction of Misaligned Actions in LLM Agents\n\n**(2) Authors:** Haishuo Fang, Xiaodan Zhu, Iryna Gurevych\n\n**(3) Venue:** Accepted by EMNLP 2025 (specific page range not available on abstract page)\n\n**(4) Evaluation Tasks:** The paper evaluated on three widely-used tasks, but specific names are not detailed in the abstract content retrieved.\n\n**(5) Marco-F1:** Measures detection accuracy for misaligned actions; the paper reports up to 20% improvements on this metric against baselines.\n\n**(6) Correction Mechanism:** Requires **human-in-the-loop intervention**—InferAct alerts users for timely correction. The abstract does not specify if fully automated correction is also supported."
      }
    ],
    "totalDurationMs": 8191,
    "totalTokens": 18167,
    "totalToolUseCount": 1,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1229,
      "cache_read_input_tokens": 16700,
      "output_tokens": 233,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1229
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 233,
          "cache_read_input_tokens": 16700,
          "cache_creation_input_tokens": 1229,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1229,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 1
    }
  },
  "sourceToolAssistantUUID": "8cb363be-3fa6-417b-b576-f6480c179ae3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "273dc98c-8ab8-4fa8-9d51-65cb993ef786",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-09T18:42:36.569Z_

<details><summary>Logged reasoning block</summary>

```text
Good. Let me now compose the complete revised JSON. The key additions are:

1. In `landscape`: Add InferAct paragraph (after Trajectory Guard section, as it's an inference-time monitoring paper) and MASC paragraph (after ProMAS section, as it's multi-agent cascade detection)

2. In `description`: Add InferAct and MASC to the positioning list (expand from "five distinct neighboring systems" to "seven distinct neighboring systems")

3. In `key_references`: Add InferAct and MASC entries

Let me now compose the complete JSON carefully.

The change_type is "minor" since we're just adding two citation blocks to related work.


Now I'm carefully integrating the two new papers into the landscape section. I need to insert InferAct after Trajectory Guard since it's also about inference-time monitoring, and place MASC after ProMAS given its focus on multi-agent cascade detection. Let me map out the full ordering to ensure the insertions flow naturally with the existing related work.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fbfc57de-74c5-47ab-a073-ca6cb42a0f8b",
  "isSidechain": false,
  "requestId": "req_011CasVBGVQtCsTtdR276jti",
  "type": "assistant",
  "uuid": "c59cf715-ad14-4533-9d15-a5938a792a0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "273dc98c-8ab8-4fa8-9d51-65cb993ef786",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01TE5qPcLMompuZXFNTcJ735",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2759,
      "cache_read_input_tokens": 30972,
      "output_tokens": 11163,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2759,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11163,
          "cache_read_input_tokens": 30972,
          "cache_creation_input_tokens": 2759,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2759
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-09T18:42:36.626Z_

I have everything I need. The fix is clearly minor — add InferAct and MASC to the landscape and references with the reviewer-specified differentiation. Let me now produce the complete revised JSON.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c59cf715-ad14-4533-9d15-a5938a792a0a",
  "isSidechain": false,
  "requestId": "req_011CasVBGVQtCsTtdR276jti",
  "type": "assistant",
  "uuid": "e7ee7d74-9f6e-4af8-9ec8-3d2b9359072e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "273dc98c-8ab8-4fa8-9d51-65cb993ef786",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01TE5qPcLMompuZXFNTcJ735",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2759,
      "cache_read_input_tokens": 30972,
      "output_tokens": 11163,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2759,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11163,
          "cache_read_input_tokens": 30972,
          "cache_creation_input_tokens": 2759,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2759
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-09T18:47:01.478Z_

<details open><summary>🔧 Tool call — Agent · `toolu_012kELr42pKWn4WjwFeqJj2p`</summary>

````json
{
  "description": "Compose complete revised idea JSON",
  "prompt": "You are a research-idea editor. Your job is to produce a COMPLETE revised JSON for a research idea called \"CascadeWatch.\" I will give you the full original JSON and precise instructions. Output ONLY the JSON — no prose before or after.\n\n## What to change\n\n**Change type: minor**\n\nAdd exactly two new citation blocks to the `landscape` field and integrate both papers into `description` and `key_references`. Do NOT change anything else.\n\n### Insertion 1 — MASC — insert immediately after the ProMAS paragraph in `landscape`\n\nThe ProMAS paragraph ends with: \"...it is a detector only and evaluates exclusively on the Who&When multi-agent attribution benchmark, not on single-agent long-horizon tasks.\"\n\nInsert this new paragraph after it:\n\n\"MASC (arXiv 2510.14319, October 2025) proposes metacognitive self-correction for multi-agent systems via Prototype-Guided Next-Execution Reconstruction: it predicts embeddings of upcoming execution steps from interaction history (Next-Execution Reconstruction) and stabilizes anomaly scoring against a learned prototype of normal-step embeddings (Prototype-Guided Enhancement), triggering a correction agent to revise the acting agent's output before error propagation; it achieves +8.47% AUC-ROC in step-level error detection on the Who&When benchmark. Three distinctions separate MASC from CascadeWatch: (1) MASC targets multi-agent systems where errors propagate across agent boundaries via message passing; CascadeWatch targets single-agent long-horizon cognitive cascades where errors compound within a single sequential trajectory. (2) MASC's anomaly scoring is unsupervised—reconstruction error against a learned normal-step prototype detects any deviation, regardless of whether it constitutes a cascade-initiating event; CascadeWatch's cascade detection is supervised using ERR Efficiency Score recoverability-delta labels derived from confirmed-cascade annotations (trajectory fails AND root-cause error before midpoint), specifically distinguishing cascade-onset patterns from recoverable deviations that the Intervention Paradox shows should not be interrupted. (3) MASC evaluates on the Who&When multi-agent attribution benchmark; CascadeWatch evaluates on ALFWorld and GAIA single-agent long-horizon task benchmarks, where the failure mode is cognitive planning error propagation rather than inter-agent message corruption.\"\n\n### Insertion 2 — InferAct — insert immediately after the Trajectory Guard paragraph in `landscape`\n\nThe Trajectory Guard paragraph ends with: \"...The lightweight framing ('inference-time monitoring of agentic trajectories') directly overlaps with CascadeWatch's positioning, but the two systems target structurally different failure modes: Trajectory Guard's reconstruction error is task-agnostic and catches any structural deviation, while CascadeWatch's recoverability-delta specifically targets the compounding-cost prefix patterns that confirm cascade onset in long-horizon cognitive tasks.\"\n\nInsert this new paragraph after it:\n\n\"InferAct (arXiv 2407.11843, EMNLP 2025 main track) uses Theory-of-Mind reasoning—grounded in LLM belief inference about user intent—to preemptively detect actions misaligned with user authorization before execution and alert users for timely correction, achieving up to 20% Marco-F1 improvement in misaligned-action detection across three evaluation tasks. Two distinctions separate InferAct from CascadeWatch: (1) InferAct targets single-step action misalignment—whether a specific upcoming action (e.g., executing a buy-now command without user authorization) matches user intent—using ToM belief inference; CascadeWatch targets multi-step cascade propagation, where an early-step error (cognitive planning error, tool-call compounding) compounds across subsequent trajectory steps regardless of user intent, using trajectory-prefix ERR recoverability signals rather than belief reasoning about user authorization. (2) InferAct's intervention is human-in-loop: it raises an alert and waits for user correction before the misaligned action executes, making it unsuitable for fully autonomous long-horizon operation; CascadeWatch's intervention is automated rollback to a pre-cascade checkpoint with no human availability requirement, and is gated by a false-positive circuit-breaker (max 2 rollbacks per episode) rather than human judgment. InferAct and CascadeWatch address complementary failure modes—unauthorized action execution versus self-compounding cascade failure—in agent safety.\"\n\n### Insertion 3 — description field\n\nIn the `description` field, find the sentence: \"CascadeWatch is positioned precisely among five distinct neighboring systems.\"\n\nReplace \"five\" with \"seven\" and add, at the end of that positioning list (after the Trajectory Guard entry which ends \"...provides no rollback mechanism\"), two new entries:\n\n\"(6) InferAct (arXiv 2407.11843, EMNLP 2025) uses Theory-of-Mind reasoning to detect actions misaligned with user intent before execution and alerts users for human-in-loop correction, achieving up to 20% Marco-F1 improvement; CascadeWatch targets multi-step cascade propagation rather than single-step user-intent misalignment, uses ERR recoverability signals rather than ToM belief inference, and intervenes via automated rollback rather than human alerting. (7) MASC (arXiv 2510.14319) detects cascading errors in multi-agent systems via unsupervised Prototype-Guided Next-Execution Reconstruction embedding anomaly scoring, achieving +8.47% AUC-ROC on the Who&When benchmark; CascadeWatch targets single-agent long-horizon cognitive cascades using supervised ERR-motivated recoverability labels and evaluates on ALFWorld/GAIA rather than multi-agent attribution tasks.\"\n\n### Insertion 4 — key_references field\n\nAdd two new entries to the key_references list:\n- \"InferAct: Preemptive Detection and Correction of Misaligned Actions in LLM Agents (EMNLP 2025 main track, arXiv 2407.11843)\"\n- \"MASC: Metacognitive Self-Correction for Multi-Agent System via Prototype-Guided Next-Execution Reconstruction (arXiv 2510.14319, 2025)\"\n\n### Add field\nAdd `\"change_type\": \"minor\"` to the top-level JSON object.\n\n## Original JSON\n\n```json\n{\n  \"title\": \"CascadeWatch: Cascade-Onset Detection with Targeted Rollback for Long-Horizon Agent Tasks\",\n  \"core_problem\": \"In long-horizon agent tasks, individual early-step errors produce cascading downstream failures that grow exponentially more costly to correct with each additional step. The core question is whether a lightweight trained monitor can prospectively detect cascade onset—predicting failure propagation before it fully manifests—to trigger targeted rollback rather than reactive reflection or full replanning. The challenge is not simply detecting failure: the Intervention Paradox (arXiv 2602.03338) establishes that generic critics with AUROC 0.94 cause up to 26 percentage point performance degradation by triggering on non-cascade failures that the agent would have self-corrected. The disruption-recovery tradeoff (Δ Success = p·r − (1−p)·d) only favors intervention on high-failure benchmarks like ALFWorld; it degrades GAIA and HotPotQA even with accurate critics. The solution is not a better generic critic but a cascade-specific one: targeting only the recoverability-degrading prefix patterns that precede confirmed cascades—detectable via recoverability proxy signals—to achieve the high precision (low d) and focused recall (high p conditional on cascade-onset) that shifts the threshold in favor of intervention. A natural alternative early-warning signal is canonical path deviation (arXiv 2602.19008): measuring Jaccard similarity of tool invocations against the convergent set shared across successful runs. This signal is empirically validated but requires aggregating tool invocation sequences from multiple successful runs per task, making it unavailable for novel tasks or low-success-rate settings. CascadeWatch uses ERR Efficiency Score recoverability deltas (arXiv 2601.22352) computable from single trajectories without reference to other runs, enabling cascade detection in the absence of precomputed canonical paths. The rollback mechanism varies by environment affordance: for text-game environments (ALFWorld), full environment-state rollback is achieved via command-replay from env.reset(); for tool-augmented environments (WebShop, GAIA), context-only rollback rewinds the agent's context window. Neither mechanism requires a non-existent API; both are acknowledged to have environment-specific costs and limitations.\",\n  \"opportunity\": \"The cascade failure pattern is now well-characterized and trainable. AgentErrorBench (arXiv 2509.25370) provides the first systematically annotated failure taxonomy across ALFWorld, WebShop, and GAIA, with root-cause step annotations identifying where cascades originate; memory and reflection errors at steps 5–15 are the most common initiators, crucially occurring mid-trajectory rather than at the earliest steps where the Intervention Paradox shows all regressions occur. The ERR paper (arXiv 2601.22352) formalizes recoverability as Expected Recovery Regret and derives a measurable Efficiency Score proxy, empirically validated across five benchmarks to within δ ≤ 0.05 of observed post-failure regret—establishing that step-level recoverability is observable from trajectory prefixes and thus learnable as a predictive signal. This signal applies directly to tool-augmented agents (WebShop, GAIA) where structured tool-call/result pairs provide natural Efficiency Score observables; for text-game environments (ALFWorld), where failures are cognitive planning errors rather than tool execution failures, a domain-adapted proxy (step-level game score delta) is used instead, acknowledged as a heuristic extension. Canonical Path Deviation (arXiv 2602.19008) provides independent corroboration of the self-reinforcing cascade mechanism in long-horizon tool-use tasks: each off-canonical tool invocation raises the probability that the next invocation is also off-canonical by 22.7 percentage points, confirming that cascade propagation is empirically measurable and compounding. CascadeWatch uses recoverability signals rather than canonical path adherence specifically because recoverability deltas are computable from a single trajectory, enabling deployment where canonical paths from multiple successful runs are unavailable. BacktrackAgent (arXiv 2505.20660, EMNLP 2025) demonstrates that backtracking triggers improve GUI agent task completion on Mobile3M and Auto-UI benchmarks, but requires constructing a task-specific training dataset and fine-tuning the agent components—leaving a clear gap for an external, training-free cascade monitor that operates on any frozen agent in cognitive long-horizon tasks. The proactive detection landscape now includes ProMAS (arXiv 2603.20260) for multi-agent error attribution, ProbGuard (arXiv 2508.00500) for physical safety monitoring, and Trajectory Guard (arXiv 2601.00516) for general structural anomaly detection in agentic trajectories, but none targets cognitive-task cascade failure in single-agent long-horizon settings nor closes the detection-to-rollback loop. The labeled failure datasets, recoverability signals, and the Intervention Paradox's threshold formula together make a specific, testable hypothesis: a cascade-specific monitor using recoverability signals will achieve sufficiently higher precision than generic critics to make rollback net-positive on benchmarks where generic critics fail, for the first time.\",\n  \"landscape\": \"Proactive monitoring is an active and crowded area that must be navigated carefully. ProMAS (arXiv 2603.20260, March 2026) uses Causal Delta Features mapped to a 30-prototype Vector Markov Space with a frozen Meta-Llama-3.1-8B extractor to predict failure onset in multi-agent collaborative reasoning systems, achieving 22.97% step-level accuracy on the Who&When benchmark (annotated multi-agent dialogues of math and logic puzzles) while processing only 27% of reasoning logs. Critically, ProMAS raises an alert but provides no corrective action—it is a detector only and evaluates exclusively on the Who&When multi-agent attribution benchmark, not on single-agent long-horizon tasks. ProbGuard (arXiv 2508.00500) learns a Discrete-Time Markov Chain from symbolic agent-state abstractions with PAC-style guarantees and triggers prompt-injection interventions when P(unsafe state) exceeds a threshold; it predicts traffic violations up to 38.66 seconds ahead and reduces unsafe behavior by 65.37% in embodied agents, but operates on physical safety constraints using symbolic abstractions rather than frozen neural representations or recoverability signals. Trajectory Guard (arXiv 2601.00516, AAAI TrustAgent Workshop 2026) proposes a Siamese Recurrent Autoencoder with hybrid contrastive-reconstruction loss for real-time anomaly detection in agentic AI trajectories, achieving F1 0.88–0.94 on balanced sets and recall 0.86–0.92 on imbalanced external benchmarks while running 17–27× faster than LLM Judge baselines at 32ms inference. Three distinctions separate this from CascadeWatch: (1) Trajectory Guard detects general structural anomalies—contextual misalignment and sequential incoherence—via reconstruction error, not cascade-specific onset via recoverability-delta signals; (2) it evaluates on synthetic perturbations, security audit failures (RAS-Eval), and multi-agent attribution (Who&When), not on single-agent long-horizon cognitive tasks (ALFWorld, GAIA); (3) it provides no rollback or correction mechanism—detection only. The lightweight framing ('inference-time monitoring of agentic trajectories') directly overlaps with CascadeWatch's positioning, but the two systems target structurally different failure modes: Trajectory Guard's reconstruction error is task-agnostic and catches any structural deviation, while CascadeWatch's recoverability-delta specifically targets the compounding-cost prefix patterns that confirm cascade onset in long-horizon cognitive tasks. The ORC auditing paper (ICLR Workshop 2026, arXiv 2603.13325) detects cascading risks in multi-agent systems via Ollivier-Ricci Curvature on completed interaction graphs—post-hoc auditing, not inference-time intervention. Canonical Path Deviation (arXiv 2602.19008, Feb 2026) is the closest theoretical neighbor to CascadeWatch's cascade-onset framing. Analyzing 515 model-task combinations on the Toolathlon benchmark (22 frontier models, 108 real-world tool-use tasks across 3 independent runs each), Wilson Y. Lee identifies stochastic drift from canonical solution paths—the convergent set of tool invocations shared across successful runs—as a causal mechanism of long-horizon failure. Path adherence is measured as Jaccard similarity between actual and canonical tool invocation sequences; adherence gaps are statistically indistinguishable from zero through the first half of trajectories but become significant and self-reinforcing thereafter, with each off-canonical tool call raising the probability that the next call is also off-canonical by 22.7 percentage points. An intervention restarting the bottom tercile of runs by mid-trajectory canonical adherence achieves +8.8pp success rate improvement. Three distinctions separate this from CascadeWatch: (1) Canonical path adherence requires aggregating tool invocation sequences across multiple successful runs per task—unavailable for novel tasks or low-success-rate settings; CascadeWatch's ERR Efficiency Score recoverability proxy is computable from a single trajectory without reference to other runs. (2) Canonical path deviation detects drift retrospectively via trajectory statistics that become significant only in the second half of execution; CascadeWatch proactively intervenes at steps 5–15 using a trained probe on prefix embeddings, before adherence divergence solidifies. (3) The CPD intervention is a full task restart of lowest-adherence runs; CascadeWatch performs targeted rollback to the pre-cascade checkpoint, preserving valid completed steps and avoiding full re-execution cost. From Spark to Fire (arXiv 2603.04474, March 2026) models cascade error propagation in LLM-based multi-agent collaboration using an individual-based mean-field framework over inter-agent communication graphs, and proposes a genealogy-graph governance layer that tracks atomic claim provenance via NLI-based verification (Green/Red/Yellow status using DeBERTa-v3-small) and blocks transmission of error-carrying messages; the Benign Infection Control Rate (complement of attack success rate) improves from 0.32 to 0.89 across Chain, Mesh, and Star multi-agent topologies on data-analysis, logic, and MMLU tasks. The cascade mechanism is specifically inter-agent: atomic factuality errors injected at one agent propagate through recursive message reuse across rounds of collaboration—a phenomenon requiring multiple communicating agents. CascadeWatch addresses a structurally different failure mode—cognitive cascade failure within a single agent's sequential trajectory (ALFWorld's planning errors, GAIA's tool-call compounding)—where there are no inter-agent message dependencies and no genealogy graph can be constructed. The per-message NLI verification in From Spark to Fire also introduces latency proportional to message volume; CascadeWatch adds only a single 2-layer MLP forward pass per step. The Intervention Paradox (arXiv 2602.03338) is the most important negative result in the space: ROLLBACK and APPEND interventions triggered by a generic LLM critic (AUROC 0.94) degrade performance on HotPotQA by −2.3 to −25.5pp and on GAIA by −4.4 to −30pp; only ALFWorld (high baseline failure rate: 5.8–14.7%) shows improvement (+0.5 to +2.8pp). All observed regressions occur with early-step (step ≤ 2) interventions. BacktrackAgent (arXiv 2505.20660, EMNLP 2025) trains a verifier-judger-reflector pipeline for GUI agents (Mobile3M, Auto-UI benchmarks) to detect individual action errors and trigger backtracking. Unlike CascadeWatch, BacktrackAgent requires constructing a task-specific training dataset and fine-tuning the agent's backtracking components; it targets GUI action-level errors (click/type correctness) rather than recoverability-degrading cascade onset in cognitive long-horizon tasks, and provides no recoverability signal. Self-Backtracking (arXiv 2502.04404) trains the base LLM to internalize when and where to backtrack during training and inference, achieving over 40% performance gains over optimal-path SFT baselines in general reasoning. This approach requires model retraining and modifies the agent's internal reasoning; CascadeWatch operates as a frozen external probe on any pre-trained agent, requiring no modification to the agent and no access to model weights or training infrastructure. Deploying CascadeWatch with a different LLM backbone requires retraining only the lightweight MLP probe (~3–5 H100-hours) against that backbone's embedding space—not retraining the backbone itself. Prior work probes LLM hidden states for single-step answer correctness in mathematical reasoning (arXiv 2504.05419), achieving 24% token reduction via early exit by detecting when intermediate reasoning steps are correct. The mechanism is structurally similar to CascadeWatch's frozen embedding + MLP probe, but targets single-step step-level correctness rather than multi-step cascade onset in agent trajectories; crucially, it adds no recoverability signal channel and does not address long-horizon failure propagation. Reactive self-correction methods share the same fundamental limitation: ExpeL and Contextual Experience Replay distill past trajectories for future improvement; self-verification (arXiv 2602.03485) confirms rechecks rarely identify errors; T-STAR (arXiv 2604.07165) achieves training-time divergence detection via Cognitive Trees but adds no inference-time mechanism. No existing system combines cascade-specific detection using recoverability signals with targeted rollback and a false-positive circuit-breaker, nor validates that cascade-specific precision avoids the Intervention Paradox's disruption-recovery tradeoff.\",\n  \"approach\": \"We train CascadeWatch to address the Intervention Paradox by targeting only the recoverability-degrading mid-trajectory patterns that precede confirmed cascades. Training data: AgentErrorBench's 200 expert-annotated trajectories (davide221/agenterrorbench on HuggingFace, spanning ALFWorld, WebShop, and GAIA) augmented with ~5,000 synthetic rollouts from Qwen/Qwen3-32B (HuggingFace: Qwen/Qwen3-32B; 32B dense model; 64GB BF16; fits in 1× H100-80GB without quantization—the Qwen3-72B designation referenced in earlier drafts corresponds to unofficial community merges and lacks an authoritative reproducible checkpoint) sampled at three temperatures (0.7, 1.0, 1.3) to increase failure-mode diversity. Cascade labels use a confirmed-cascade criterion: a step k is labeled cascade-onset only if (1) the trajectory ultimately fails, (2) step k is at or after the earliest annotated root-cause error, AND (3) the root-cause error occurs before the trajectory midpoint (step ≤ ⌊total_steps / 2⌋)—this filters out partially-recovered trajectories and prevents false cascade labels from error-tolerant agents. A minimum intervention threshold of step ≥ 5 is imposed at inference time, consistent with AgentErrorBench's finding that cascade-initiating errors occur at steps 5–15 and with the Intervention Paradox's finding that all observed regressions involve step ≤ 2 interventions. Each trajectory prefix at step k is represented by concatenating (a) frozen Qwen/Qwen3-32B hidden-state embeddings (mean-pooled last 4 transformer layers over the action–observation sequence) with (b) recoverability delta signals. For WebShop and GAIA (tool-augmented benchmarks with structured tool-call/result pairs), these are ERR Efficiency Score deltas as defined in arXiv 2601.22352. For ALFWorld (a text-based game where failures are cognitive planning errors rather than tool execution failures, and which lacks structured tool-call pairs), ERR Efficiency Score is not directly applicable; we substitute a domain-adapted proxy: step-level delta in the normalized ALFWorld game score (Δ(info['score'] / info['max_score']) at each step), which tracks incremental subgoal-completion rate. This is an acknowledged heuristic extension of the ERR framework; whether the recoverability motivation holds for this proxy is explicitly tested in the ablation. A 2-layer MLP probe (with L2 weight decay 1e-4) outputs P(cascade | prefix_k), with Platt scaling applied on a stratified held-out validation split. Training data sparsity (200 labeled trajectories) is addressed by (i) 5-fold cross-validation stratified by benchmark (ALFWorld / WebShop / GAIA) to estimate generalization without benchmark leakage, and (ii) a parallel logistic probe baseline to assess whether MLP complexity is justified over this small labeled set. The AgentErrorBench annotations are distributed unevenly across benchmarks: GAIA contributes approximately 50 of the 200 labeled trajectories, yielding roughly 27 training samples per fold in 3-fold CV (the compressed HIL mode), placing the GAIA cascade probe near the minimum viable supervised learning regime; GAIA results are consequently treated as preliminary evidence, with ALFWorld (approximately 100 trajectories, ~67 per fold) providing the primary evidence base for the main cascade-avoidance claim. CascadeWatch requires no modification to the base agent and does not require retraining the agent backbone; deploying CascadeWatch with a different LLM backbone requires retraining only the lightweight MLP probe (~3–5 H100-hours) against that backbone's embedding space, not retraining the agent itself. This is a meaningful practical advantage over BacktrackAgent, which requires constructing a task-specific training dataset and fine-tuning agent components. The rollback mechanism is specified per benchmark: For ALFWorld, environment-state rollback is performed via command-replay from env.reset(): the TextWorld gym environment is reset to the initial observation, then the k−1 accepted actions from the checkpoint buffer are re-executed sequentially to reconstruct game state at step k−1. The ALFWorld game engine processes each text command in approximately 1–2ms; for typical episodes capped at 50 steps, rollback at step k incurs roughly 25–100ms wall-clock overhead—negligible relative to LLM inference time. A checkpoint buffer stores accepted action sequences at each step to enable replay without re-querying the LLM. Note that TextWorld's Python API does not expose a save/restore mechanism for Glulx-format (.ulx) games used in ALFWorld competition settings, so command-replay is the correct mechanism; the O(k) replay cost is in game-engine steps, not LLM compute. The Crab sandbox (arXiv 2604.28138) provides semantics-aware container-level checkpoint/restore that could in principle support ALFWorld game-state snapshots regardless of the underlying game engine; CascadeWatch uses command-replay to maintain compatibility with standard ALFWorld evaluation setups that do not use containerized sandboxes, and to avoid container-spinup overhead that would dominate the ~25–100ms rollback budget. For WebShop and GAIA, context-only rollback rewinds the agent context window to step k_checkpoint, masks all subsequent actions and observations, and re-samples an alternative action with temperature +0.3. Context-only rollback does not undo irreversible WebShop web-state changes (e.g., submitted searches), which is explicitly noted as a limitation. A false-positive circuit-breaker limits rollback to a maximum of 2 triggers per episode; after the second trigger, monitoring is suspended for the remainder of the episode to prevent compounding disruption. Before full evaluation, we run the Intervention Paradox's 50-task pilot test on each benchmark to empirically verify that CascadeWatch's cascade-specific intervention is net-positive (p > d/(r+d)) on that benchmark; benchmarks where the pilot test fails are reported as negative results, not omitted. We include a pre-registered 3-way ablation: (a) frozen embeddings only → logistic probe, (b) recoverability-delta features only → logistic regression (no embeddings), (c) full CascadeWatch (embeddings + recoverability-delta) → 2-layer MLP. The primary empirical claim is that CascadeWatch achieves task success rate improvement over no-correction baselines on ALFWorld and GAIA while avoiding the performance degradation caused by generic critics observed in the Intervention Paradox—demonstrating for the first time that cascade-specific precision is sufficient to make rollback net-positive on benchmarks where generic critics fail. The recoverability-delta ablation serves as an internal validation gate: if recoverability-delta provides ≥3% F1 lift over frozen embeddings alone, the ERR-motivated feature design is empirically confirmed; if the lift is <3%, the theoretical ERR motivation weakens substantially and this is reported honestly as a negative result on the recoverability signal hypothesis. We evaluate task success rate, steps saved per episode, and false-positive intervention rate against no-correction, ExpeL-style reflection, self-verification, T-STAR offline, and ProMAS-style detection-only baselines on ALFWorld, WebShop, and GAIA (subject to pilot test results).\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~100-140 H100-hours total: rollout generation ~45 H100-hours (Qwen/Qwen3-32B runs in BF16 on 1× H100-80GB without quantization—32B × 2 bytes ≈ 64GB, within the 80GB VRAM budget; inference throughput roughly doubles relative to a 72B model; ~45h covers ~5K synthetic rollouts across three benchmarks at three temperatures, including environment interaction overhead and tool-call latency for GAIA tasks); probe training ~10 H100-hours (5-fold CV × 3-way ablation × logistic/MLP variants; these are small models, <1h each); evaluation runs ~45–85 H100-hours across three benchmarks + pilot tests (50 tasks × 3 benchmarks × 2 conditions per test). ALFWorld command-replay rollback adds <1 H100-hour overhead across all evaluation episodes.\",\n      \"gpu_utilization\": \"~30–40% effective utilization; high idle between human coding, debugging, and analysis cycles\",\n      \"timeline\": \"4–6 months\",\n      \"team\": \"2 researchers\",\n      \"estimated_gpu_cost\": \"~$200–$280 at ~$2/H100-hour\"\n    },\n    \"human_in_loop\": {\n      \"scope_note\": \"Compressed to satisfy the joint ≤16-day calendar / ≤200 H100-hour constraint. Primary benchmarks reduced to ALFWorld + GAIA (2 of 3); WebShop deferred to optional extension after primary evaluation completes. Synthetic rollouts reduced to 2,000 total at 2 temperatures (T=0.7, T=1.0); 3-fold CV replaces 5-fold. Human gates: cascade label validation, pilot test pass/fail judgment per benchmark, ablation design review, threshold decisions. Human engagement: 2–3 hours/day (not 30 min/day).\",\n      \"compute_breakdown\": \"Rollout generation (2K rollouts × 2 temperatures = 4K trajectories; ~1K ALFWorld + 1K GAIA per temperature): ~10–15 H100-hours (ALFWorld ~2–3h; GAIA ~8–12h including tool-call overhead; Qwen/Qwen3-32B BF16 on 1× H100-80GB without quantization). Probe training (3-fold CV × 3-way ablation × logistic/MLP): ~3–5 H100-hours. Pilot tests (50 tasks × 2 benchmarks × 2 conditions × 2 seeds = 400 episodes): ~7–10 H100-hours. Full evaluation (post-pilot, 2 benchmarks × 4 baselines + CascadeWatch): ~25–35 H100-hours. Buffer/debugging: ~5–10 H100-hours. Total: ~50–75 H100-hours.\",\n      \"gpu_hours\": \"~50–75 H100-hours (well within ≤200 H100-hour constraint)\",\n      \"gpu_utilization\": \"~60–70% utilization; human approval gates reduce compute waste on dead-end ablations\",\n      \"timeline\": \"12–14 calendar days (achievable within 16-day constraint with efficient pipeline execution: rollout generation days 1–2, labeling + probe training days 2–4, pilot tests with human review days 4–8, full evaluation days 8–12, analysis and write-up days 10–14)\",\n      \"team\": \"1 researcher, ~2–3 hours/day check-in\",\n      \"claude_api_cost\": \"$150–$250\",\n      \"estimated_gpu_cost\": \"~$100–$150 at ~$2/H100-hour\",\n      \"risk_note\": \"Small labeled training set (200 trajectories) risks MLP overfitting; confirmed-cascade criterion and temperature augmentation strategy are critical human-gate decisions. GAIA contributes approximately 50 of those 200 labeled trajectories (~27 training samples per fold in 3-fold CV), placing the GAIA probe near the minimum viable supervised learning regime—GAIA evaluation results should be treated as preliminary evidence pending replication on a larger annotated set. ALFWorld ERR proxy (game score delta) is a domain adaptation—its F1 contribution must be validated in ablation before committing to full evaluation on ALFWorld. Pilot test (50 tasks × 2 benchmarks) must be reviewed by human before committing to full evaluation on each benchmark. WebShop extension requires an additional ~15–25 H100-hours beyond the primary constraint if pursued.\"\n    },\n    \"auto_research\": {\n      \"note\": \"This mode exceeds the primary ≤200 H100-hour constraint and is presented as an extended evaluation scenario for teams with unrestricted compute, not a valid path within the joint 16-day/200 H100-hour constraint. Included for completeness only.\",\n      \"gpu_hours\": \"~300–450 H100-hours (3–5× more ablations across probe architectures, threshold strategies, feature combinations, augmentation volumes, rollback trigger policies, and minimum-step thresholds; reduced from prior estimates due to Qwen/Qwen3-32B being more compute-efficient than the previously specified 72B model)\",\n      \"gpu_utilization\": \"~85–95%; near-zero idle as agent continuously queues and launches experiments\",\n      \"timeline\": \"3–10 days with 4+ H100s in parallel\",\n      \"team\": \"0 (initial setup only)\",\n      \"claude_api_cost\": \"$350–$600\",\n      \"estimated_gpu_cost\": \"~$600–$900\",\n      \"speed_bottleneck\": \"Number of H100s available; rollout generation dominates throughput\",\n      \"risk_note\": \"Automated cascade label derivation may skip the confirmed-cascade midpoint filter, generating false positive labels; no human oversight to detect always-predict-cascade degenerate solutions. Pilot test pass/fail judgment and Intervention Paradox threshold calculation require human review—an agent may proceed to full evaluation on benchmarks where intervention is net-negative. ALFWorld ERR proxy domain adaptation requires human judgment to validate before scaling.\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 (ARR deadline May 25, 2026)\",\n    \"AAAI 2027 (abstract deadline expected ~August 2026)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"Where LLM Agents Fail and How They can Learn From Failures (arXiv 2509.25370, 2025)\",\n    \"Recoverability Has a Law: The ERR Measure for Tool-Augmented Agents (arXiv 2601.22352, 2026)\",\n    \"The Intervention Paradox: Accurate Failure Prediction in Agents Does Not Imply Effective Failure Prevention (arXiv 2602.03338, 2026)\",\n    \"Capable but Unreliable: Canonical Path Deviation as a Causal Mechanism of Agent Failure in Long-Horizon Tasks (arXiv 2602.19008, 2026)\",\n    \"Trajectory Guard: A Lightweight, Sequence-Aware Model for Real-Time Anomaly Detection in Agentic AI (AAAI TrustAgent Workshop 2026, arXiv 2601.00516)\",\n    \"ProMAS: Proactive Error Forecasting for Multi-Agent Systems Using Markov Transition Dynamics (arXiv 2603.20260, 2026)\",\n    \"From Spark to Fire: Modeling and Mitigating Error Cascades in LLM-Based Multi-Agent Collaboration (arXiv 2603.04474, 2026)\",\n    \"ProbGuard: Probabilistic Runtime Monitoring for LLM Agent Safety (arXiv 2508.00500, 2025)\",\n    \"Auditing Cascading Risks in Multi-Agent Systems via Semantic–Geometric Co-evolution (ICLR Workshop 2026, arXiv 2603.13325)\",\n    \"Crab: A Semantics-Aware Checkpoint/Restore Runtime for Agent Sandboxes (arXiv 2604.28138, 2026)\",\n    \"Reason in Chains, Learn in Trees: Self-Rectification and Grafting for Multi-turn Agent Policy Optimization (arXiv 2604.07165, 2026)\",\n    \"Self-Verification Dilemma: Experience-Driven Suppression of Overused Checking in LLM Reasoning (arXiv 2602.03485, 2026)\",\n    \"Beyond Fluency: Toward Reliable Trajectories in Agentic IR — position paper on failure modes, not empirical cascade measurement (arXiv 2604.04269, 2026)\",\n    \"BacktrackAgent: Enhancing GUI Agent with Error Detection and Backtracking Mechanism (EMNLP 2025, arXiv 2505.20660)\",\n    \"Step Back to Leap Forward: Self-Backtracking for Boosting Reasoning of Language Models (arXiv 2502.04404, 2025)\",\n    \"Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification (arXiv 2504.05419, 2025)\"\n  ],\n  \"description\": \"Long-horizon agent tasks suffer from cascade failures: a single early error propagates across subsequent steps, compounding recovery cost. The critical challenge is the Intervention Paradox (arXiv 2602.03338): a generic critic with AUROC 0.94 causes up to 26 percentage point degradation by disrupting self-correcting trajectories, with all observed regressions occurring at early intervention steps. The solution requires cascade-specific, high-precision detection rather than general failure prediction. We propose CascadeWatch, an inference-time monitor that targets cascade onset specifically using frozen Qwen/Qwen3-32B hidden-state embeddings (HuggingFace: Qwen/Qwen3-32B; 32B dense model; 64GB BF16; fits in 1× H100-80GB without quantization) combined with recoverability delta signals to estimate P(cascade_failure | prefix_k) at each step, with a minimum trigger threshold of step ≥ 5 to avoid the early-step intervention regime where generic critics cause harm. For WebShop and GAIA (tool-augmented benchmarks), recoverability deltas are ERR Efficiency Score deltas (arXiv 2601.22352). For ALFWorld (text-based game with cognitive planning errors, not tool execution failures), ERR Efficiency Score is inapplicable; we use a domain-adapted proxy: step-level delta in the normalized ALFWorld game score, which tracks subgoal completion rate. This domain adaptation is acknowledged as a heuristic extension and is explicitly isolated in the ablation. CascadeWatch is positioned precisely among five distinct neighboring systems. (1) Canonical Path Deviation (arXiv 2602.19008) identifies stochastic drift from canonical solution paths—aggregated from multiple successful runs per task—as a long-horizon failure mechanism, achieving +8.8pp improvement via restart of lowest-adherence runs; CascadeWatch uses single-trajectory recoverability signals (no canonical paths required) and performs targeted rollback rather than full restarts. (2) From Spark to Fire (arXiv 2603.04474) proposes a genealogy-graph governance layer for cascade mitigation in multi-agent collaboration, improving Benign Infection Control Rate from 0.32 to 0.89; CascadeWatch addresses a structurally different failure mode—cognitive cascade failure within a single agent's sequential trajectory—where there are no inter-agent message dependencies. (3) ProMAS (arXiv 2603.20260) raises alerts in multi-agent reasoning but provides no corrective action and evaluates only on the Who&When attribution benchmark. (4) ProbGuard (arXiv 2508.00500) softly intervenes on physical safety constraints via symbolic DTMC. (5) Trajectory Guard (arXiv 2601.00516) uses a Siamese Recurrent Autoencoder with hybrid contrastive-reconstruction loss to detect trajectory anomalies in agentic AI at 32ms, but targets general structural anomalies rather than cascade-specific onset via recoverability signals, evaluates on security audit and multi-agent benchmarks (not ALFWorld/GAIA), and provides no rollback mechanism. Unlike BacktrackAgent (arXiv 2505.20660, EMNLP 2025), which trains a verifier-judger-reflector pipeline for GUI action errors using a task-specific backtracking dataset, CascadeWatch requires no modification to the base agent and does not require retraining the agent backbone; deploying CascadeWatch with a different LLM backbone requires retraining only the lightweight MLP probe (~3–5 H100-hours) against that backbone's embedding space, not retraining the agent itself. Unlike Self-Backtracking (arXiv 2502.04404), which trains the LLM itself to internalize backtracking decisions, CascadeWatch operates as a frozen external probe deployable without model retraining. Prior hidden-state probing work (arXiv 2504.05419) probes single-step reasoning correctness to reduce tokens by 24%; CascadeWatch probes multi-step trajectory prefixes for cascade onset and adds recoverability signals as a second feature channel. CascadeWatch closes the loop on cognitive-task cascades in single-agent long-horizon settings by triggering targeted rollback with a false-positive circuit-breaker (max 2 rollbacks per episode). Rollback mechanism: for ALFWorld, environment-state rollback via command-replay from env.reset() (O(k) game-engine steps; ~25–100ms wall-clock for 50-step episodes; TextWorld's Python API does not expose save/restore for Glulx-format .ulx games; the Crab sandbox, arXiv 2604.28138, provides container-level checkpoint/restore that could support ALFWorld in principle but requires containerization overhead incompatible with standard evaluation setups). For WebShop and GAIA, context-only rollback (agent context rewound to checkpoint; does not undo irreversible web-state changes, acknowledged as a limitation). Cascade labels use a confirmed-cascade criterion (trajectory fails AND root-cause error occurs before the trajectory midpoint) to prevent false labels from partially-recovered trajectories. The GAIA cascade probe operates near the minimum viable supervised learning regime (~27 training samples per fold in 3-fold CV across approximately 50 GAIA-labeled trajectories from AgentErrorBench); GAIA results are treated as preliminary evidence, with ALFWorld (approximately 100 trajectories, ~67 per fold) providing the primary evidence base for the main cascade-avoidance claim. The primary empirical claim is that CascadeWatch achieves task success rate improvement over no-correction baselines on ALFWorld and GAIA while avoiding the performance degradation caused by generic critics (the Intervention Paradox)—demonstrating that cascade-specific precision is sufficient to make rollback net-positive on benchmarks where generic critics fail. The recoverability-delta ablation (embeddings-only vs. recoverability-delta-only vs. combined) serves as an internal validation gate: ≥3% F1 lift from recoverability-delta confirms the ERR-motivated feature design; <3% lift is reported as a negative result. Evaluated on ALFWorld and GAIA as primary benchmarks (WebShop as optional extension), each preceded by the Intervention Paradox's 50-task pilot test to verify net-positive intervention before full evaluation. The compressed HIL execution mode (2 benchmarks, 2K rollouts, 3-fold CV, 2–3 hours/day human engagement) fits within ~50–75 H100-hours and 12–14 calendar days, comfortably within the ≤200 H100-hour and ≤16-day constraints.\",\n  \"project_name\": \"cascade_monitor\",\n  \"source\": \"web_research\"\n}\n```\n\nNow produce the complete revised JSON applying exactly the four insertions described above. Output ONLY valid JSON, no markdown fences, no prose."
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7ee7d74-9f6e-4af8-9ec8-3d2b9359072e",
  "isSidechain": false,
  "requestId": "req_011CasVBGVQtCsTtdR276jti",
  "type": "assistant",
  "uuid": "11efee4e-0a09-48a1-a46b-f7eb3c049f6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "273dc98c-8ab8-4fa8-9d51-65cb993ef786",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01TE5qPcLMompuZXFNTcJ735",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2759,
      "cache_read_input_tokens": 30972,
      "output_tokens": 11163,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2759,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11163,
          "cache_read_input_tokens": 30972,
          "cache_creation_input_tokens": 2759,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2759
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Runtime record

_source line 27_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-09 (UTC).**  ## Original idea {   \"title\": \"CascadeWatch: Cascade-Onset Detection with Targeted Rollback for Long-…",
  "leafUuid": "11efee4e-0a09-48a1-a46b-f7eb3c049f6b",
  "sessionId": "273dc98c-8ab8-4fa8-9d51-65cb993ef786"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "ai-title",
  "aiTitle": "Cascade-aware agent rollback with recoverability signals",
  "sessionId": "273dc98c-8ab8-4fa8-9d51-65cb993ef786"
}
```

---

### Tool result

_source line 29 · 2026-05-09T19:12:30.572Z_

<details><summary>↩ Tool result · `toolu_012kELr42pKWn4WjwFeqJj2p`</summary>

```text
I'll output the complete revised JSON directly in my response:

{"change_type":"minor","title":"CascadeWatch: Cascade-Onset Detection with Targeted Rollback for Long-Horizon Agent Tasks","core_problem":"In long-horizon agent tasks, individual early-step errors produce cascading downstream failures that grow exponentially more costly to correct with each additional step. The core question is whether a lightweight trained monitor can prospectively detect cascade onset—predicting failure propagation before it fully manifests—to trigger targeted rollback rather than reactive reflection or full replanning. The challenge is not simply detecting failure: the Intervention Paradox (arXiv 2602.03338) establishes that generic critics with AUROC 0.94 cause up to 26 percentage point performance degradation by triggering on non-cascade failures that the agent would have self-corrected. The disruption-recovery tradeoff (Δ Success = p·r − (1−p)·d) only favors intervention on high-failure benchmarks like ALFWorld; it degrades GAIA and HotPotQA even with accurate critics. The solution is not a better generic critic but a cascade-specific one: targeting only the recoverability-degrading prefix patterns that precede confirmed cascades—detectable via recoverability proxy signals—to achieve the high precision (low d) and focused recall (high p conditional on cascade-onset) that shifts the threshold in favor of intervention. A natural alternative early-warning signal is canonical path deviation (arXiv 2602.19008): measuring Jaccard similarity of tool invocations against the convergent set shared across successful runs. This signal is empirically validated but requires aggregating tool invocation sequences from multiple successful runs per task, making it unavailable for novel tasks or low-success-rate settings. CascadeWatch uses ERR Efficiency Score recoverability deltas (arXiv 2601.22352) computable from single trajectories without reference to other runs, enabling cascade detection in the absence of precomputed canonical paths. The rollback mechanism varies by environment affordance: for text-game environments (ALFWorld), full environment-state rollback is achieved via command-replay from env.reset(); for tool-augmented environments (WebShop, GAIA), context-only rollback rewinds the agent's context window. Neither mechanism requires a non-existent API; both are acknowledged to have environment-specific costs and limitations.","opportunity":"The cascade failure pattern is now well-characterized and trainable. AgentErrorBench (arXiv 2509.25370) provides the first systematically annotated failure taxonomy across ALFWorld, WebShop, and GAIA, with root-cause step annotations identifying where cascades originate; memory and reflection errors at steps 5–15 are the most common initiators, crucially occurring mid-trajectory rather than at the earliest steps where the Intervention Paradox shows all regressions occur. The ERR paper (arXiv 2601.22352) formalizes recoverability as Expected Recovery Regret and derives a measurable Efficiency Score proxy, empirically validated across five benchmarks to within δ ≤ 0.05 of observed post-failure regret—establishing that step-level recoverability is observable from trajectory prefixes and thus learnable as a predictive signal. This signal applies directly to tool-augmented agents (WebShop, GAIA) where structured tool-call/result pairs provide natural Efficiency Score observables; for text-game environments (ALFWorld), where failures are cognitive planning errors rather than tool execution failures, a domain-adapted proxy (step-level game score delta) is used instead, acknowledged as a heuristic extension. Canonical Path Deviation (arXiv 2602.19008) provides independent corroboration of the self-reinforcing cascade mechanism in long-horizon tool-use tasks: each off-canonical tool invocation raises the probability that the next invocation is also off-canonical by 22.7 percentage points, confirming that cascade propagation is empirically measurable and compounding. CascadeWatch uses recoverability signals rather than canonical path adherence specifically because recoverability deltas are computable from a single trajectory, enabling deployment where canonical paths from multiple successful runs are unavailable. BacktrackAgent (arXiv 2505.20660, EMNLP 2025) demonstrates that backtracking triggers improve GUI agent task completion on Mobile3M and Auto-UI benchmarks, but requires constructing a task-specific training dataset and fine-tuning the agent components—leaving a clear gap for an external, training-free cascade monitor that operates on any frozen agent in cognitive long-horizon tasks. The proactive detection landscape now includes ProMAS (arXiv 2603.20260) for multi-agent error attribution, ProbGuard (arXiv 2508.00500) for physical safety monitoring, and Trajectory Guard (arXiv 2601.00516) for general structural anomaly detection in agentic trajectories, but none targets cognitive-task cascade failure in single-agent long-horizon settings nor closes the detection-to-rollback loop. The labeled failure datasets, recoverability signals, and the Intervention Paradox's threshold formula together make a specific, testable hypothesis: a cascade-specific monitor using recoverability signals will achieve sufficiently higher precision than generic critics to make rollback net-positive on benchmarks where generic critics fail, for the first time.","landscape":"Proactive monitoring is an active and crowded area that must be navigated carefully. ProMAS (arXiv 2603.20260, March 2026) uses Causal Delta Features mapped to a 30-prototype Vector Markov Space with a frozen Meta-Llama-3.1-8B extractor to predict failure onset in multi-agent collaborative reasoning systems, achieving 22.97% step-level accuracy on the Who&When benchmark (annotated multi-agent dialogues of math and logic puzzles) while processing only 27% of reasoning logs. Critically, ProMAS raises an alert but provides no corrective action—it is a detector only and evaluates exclusively on the Who&When multi-agent attribution benchmark, not on single-agent long-horizon tasks. MASC (arXiv 2510.14319, October 2025) proposes metacognitive self-correction for multi-agent systems via Prototype-Guided Next-Execution Reconstruction: it predicts embeddings of upcoming execution steps from interaction history (Next-Execution Reconstruction) and stabilizes anomaly scoring against a learned prototype of normal-step embeddings (Prototype-Guided Enhancement), triggering a correction agent to revise the acting agent's output before error propagation; it achieves +8.47% AUC-ROC in step-level error detection on the Who&When benchmark. Three distinctions separate MASC from CascadeWatch: (1) MASC targets multi-agent systems where errors propagate across agent boundaries via message passing; CascadeWatch targets single-agent long-horizon cognitive cascades where errors compound within a single sequential trajectory. (2) MASC's anomaly scoring is unsupervised—reconstruction error against a learned normal-step prototype detects any deviation, regardless of whether it constitutes a cascade-initiating event; CascadeWatch's cascade detection is supervised using ERR Efficiency Score recoverability-delta labels derived from confirmed-cascade annotations (trajectory fails AND root-cause error before midpoint), specifically distinguishing cascade-onset patterns from recoverable deviations that the Intervention Paradox shows should not be interrupted. (3) MASC evaluates on the Who&When multi-agent attribution benchmark; CascadeWatch evaluates on ALFWorld and GAIA single-agent long-horizon task benchmarks, where the failure mode is cognitive planning error propagation rather than inter-agent message corruption. ProbGuard (arXiv 2508.00500) learns a Discrete-Time Markov Chain from symbolic agent-state abstractions with PAC-style guarantees and triggers prompt-injection interventions when P(unsafe state) exceeds a threshold; it predicts traffic violations up to 38.66 seconds ahead and reduces unsafe behavior by 65.37% in embodied agents, but operates on physical safety constraints using symbolic abstractions rather than frozen neural representations or recoverability signals. Trajectory Guard (arXiv 2601.00516, AAAI TrustAgent Workshop 2026) proposes a Siamese Recurrent Autoencoder with hybrid contrastive-reconstruction loss for real-time anomaly detection in agentic AI trajectories, achieving F1 0.88–0.94 on balanced sets and recall 0.86–0.92 on imbalanced external benchmarks while running 17–27× faster than LLM Judge baselines at 32ms inference. Three distinctions separate this from CascadeWatch: (1) Trajectory Guard detects general structural anomalies—contextual misalignment and sequential incoherence—via reconstruction error, not cascade-specific onset via recoverability-delta signals; (2) it evaluates on synthetic perturbations, security audit failures (RAS-Eval), and multi-agent attribution (Who&When), not on single-agent long-horizon cognitive tasks (ALFWorld, GAIA); (3) it provides no rollback or correction mechanism—detection only. The lightweight framing ('inference-time monitoring of agentic trajectories') directly overlaps with CascadeWatch's positioning, but the two systems target structurally different failure modes: Trajectory Guard's reconstruction error is task-agnostic and catches any structural deviation, while CascadeWatch's recoverability-delta specifically targets the compounding-cost prefix patterns that confirm cascade onset in long-horizon cognitive tasks. InferAct (arXiv 2407.11843, EMNLP 2025 main track) uses Theory-of-Mind reasoning—grounded in LLM belief inference about user intent—to preemptively detect actions misaligned with user authorization before execution and alert users for timely correction, achieving up to 20% Marco-F1 improvement in misaligned-action detection across three evaluation tasks. Two distinctions separate InferAct from CascadeWatch: (1) InferAct targets single-step action misalignment—whether a specific upcoming action (e.g., executing a buy-now command without user authorization) matches user intent—using ToM belief inference; CascadeWatch targets multi-step cascade propagation, where an early-step error (cognitive planning error, tool-call compounding) compounds across subsequent trajectory steps regardless of user intent, using trajectory-prefix ERR recoverability signals rather than belief reasoning about user authorization. (2) InferAct's intervention is human-in-loop: it raises an alert and waits for user correction before the misaligned action executes, making it unsuitable for fully autonomous long-horizon operation; CascadeWatch's intervention is automated rollback to a pre-cascade checkpoint with no human availability requirement, and is gated by a false-positive circuit-breaker (max 2 rollbacks per episode) rather than human judgment. InferAct and CascadeWatch address complementary failure modes—unauthorized action execution versus self-compounding cascade failure—in agent safety. The ORC auditing paper (ICLR Workshop 2026, arXiv 2603.13325) detects cascading risks in multi-agent systems via Ollivier-Ricci Curvature on completed interaction graphs—post-hoc auditing, not inference-time intervention. Canonical Path Deviation (arXiv 2602.19008, Feb 2026) is the closest theoretical neighbor to CascadeWatch's cascade-onset framing. Analyzing 515 model-task combinations on the Toolathlon benchmark (22 frontier models, 108 real-world tool-use tasks across 3 independent runs each), Wilson Y. Lee identifies stochastic drift from canonical solution paths—the convergent set of tool invocations shared across successful runs—as a causal mechanism of long-horizon failure. Path adherence is measured as Jaccard similarity between actual and canonical tool invocation sequences; adherence gaps are statistically indistinguishable from zero through the first half of trajectories but become significant and self-reinforcing thereafter, with each off-canonical tool call raising the probability that the next call is also off-canonical by 22.7 percentage points. An intervention restarting the bottom tercile of runs by mid-trajectory canonical adherence achieves +8.8pp success rate improvement. Three distinctions separate this from CascadeWatch: (1) Canonical path adherence requires aggregating tool invocation sequences across multiple successful runs per task—unavailable for novel tasks or low-success-rate settings; CascadeWatch's ERR Efficiency Score recoverability proxy is computable from a single trajectory without reference to other runs. (2) Canonical path deviation detects drift retrospectively via trajectory statistics that become significant only in the second half of execution; CascadeWatch proactively intervenes at steps 5–15 using a trained probe on prefix embeddings, before adherence divergence solidifies. (3) The CPD intervention is a full task restart of lowest-adherence runs; CascadeWatch performs targeted rollback to the pre-cascade checkpoint, preserving valid completed steps and avoiding full re-execution cost. From Spark to Fire (arXiv 2603.04474, March 2026) models cascade error propagation in LLM-based multi-agent collaboration using an individual-based mean-field framework over inter-agent communication graphs, and proposes a genealogy-graph governance layer that tracks atomic claim provenance via NLI-based verification (Green/Red/Yellow status using DeBERTa-v3-small) and blocks transmission of error-carrying messages; the Benign Infection Control Rate (complement of attack success rate) improves from 0.32 to 0.89 across Chain, Mesh, and Star multi-agent topologies on data-analysis, logic, and MMLU tasks. The cascade mechanism is specifically inter-agent: atomic factuality errors injected at one agent propagate through recursive message reuse across rounds of collaboration—a phenomenon requiring multiple communicating agents. CascadeWatch addresses a structurally different failure mode—cognitive cascade failure within a single agent's sequential trajectory (ALFWorld's planning errors, GAIA's tool-call compounding)—where there are no inter-agent message dependencies and no genealogy graph can be constructed. The per-message NLI verification in From Spark to Fire also introduces latency proportional to message volume; CascadeWatch adds only a single 2-layer MLP forward pass per step. The Intervention Paradox (arXiv 2602.03338) is the most important negative result in the space: ROLLBACK and APPEND interventions triggered by a generic LLM critic (AUROC 0.94) degrade performance on HotPotQA by −2.3 to −25.5pp and on GAIA by −4.4 to −30pp; only ALFWorld (high baseline failure rate: 5.8–14.7%) shows improvement (+0.5 to +2.8pp). All observed regressions occur with early-step (step ≤ 2) interventions. BacktrackAgent (arXiv 2505.20660, EMNLP 2025) trains a verifier-judger-reflector pipeline for GUI agents (Mobile3M, Auto-UI benchmarks) to detect individual action errors and trigger backtracking. Unlike CascadeWatch, BacktrackAgent requires constructing a task-specific training dataset and fine-tuning the agent's backtracking components; it targets GUI action-level errors (click/type correctness) rather than recoverability-degrading cascade onset in cognitive long-horizon tasks, and provides no recoverability signal. Self-Backtracking (arXiv 2502.04404) trains the base LLM to internalize when and where to backtrack during training and inference, achieving over 40% performance gains over optimal-path SFT baselines in general reasoning. This approach requires model retraining and modifies the agent's internal reasoning; CascadeWatch operates as a frozen external probe on any pre-trained agent, requiring no modification to the agent and no access to model weights or training infrastructure. Deploying CascadeWatch with a different LLM backbone requires retraining only the lightweight MLP probe (~3–5 H100-hours) against that backbone's embedding space—not retraining the backbone itself. Prior work probes LLM hidden states for single-step answer correctness in mathematical reasoning (arXiv 2504.05419), achieving 24% token reduction via early exit by detecting when intermediate reasoning steps are correct. The mechanism is structurally similar to CascadeWatch's frozen embedding + MLP probe, but targets single-step step-level correctness rather than multi-step cascade onset in agent trajectories; crucially, it adds no recoverability signal channel and does not address long-horizon failure propagation. Reactive self-correction methods share the same fundamental limitation: ExpeL and Contextual Experience Replay distill past trajectories for future improvement; self-verification (arXiv 2602.03485) confirms rechecks rarely identify errors; T-STAR (arXiv 2604.07165) achieves training-time divergence detection via Cognitive Trees but adds no inference-time mechanism. No existing system combines cascade-specific detection using recoverability signals with targeted rollback and a false-positive circuit-breaker, nor validates that cascade-specific precision avoids the Intervention Paradox's disruption-recovery tradeoff.","approach":"We train CascadeWatch to address the Intervention Paradox by targeting only the recoverability-degrading mid-trajectory patterns that precede confirmed cascades. Training data: AgentErrorBench's 200 expert-annotated trajectories (davide221/agenterrorbench on HuggingFace, spanning ALFWorld, WebShop, and GAIA) augmented with ~5,000 synthetic rollouts from Qwen/Qwen3-32B (HuggingFace: Qwen/Qwen3-32B; 32B dense model; 64GB BF16; fits in 1× H100-80GB without quantization—the Qwen3-72B designation referenced in earlier drafts corresponds to unofficial community merges and lacks an authoritative reproducible checkpoint) sampled at three temperatures (0.7, 1.0, 1.3) to increase failure-mode diversity. Cascade labels use a confirmed-cascade criterion: a step k is labeled cascade-onset only if (1) the trajectory ultimately fails, (2) step k is at or after the earliest annotated root-cause error, AND (3) the root-cause error occurs before the trajectory midpoint (step ≤ ⌊total_steps / 2⌋)—this filters out partially-recovered trajectories and prevents false cascade labels from error-tolerant agents. A minimum intervention threshold of step ≥ 5 is imposed at inference time, consistent with AgentErrorBench's finding that cascade-initiating errors occur at steps 5–15 and with the Intervention Paradox's finding that all observed regressions involve step ≤ 2 interventions. Each trajectory prefix at step k is represented by concatenating (a) frozen Qwen/Qwen3-32B hidden-state embeddings (mean-pooled last 4 transformer layers over the action–observation sequence) with (b) recoverability delta signals. For WebShop and GAIA (tool-augmented benchmarks with structured tool-call/result pairs), these are ERR Efficiency Score deltas as defined in arXiv 2601.22352. For ALFWorld (a text-based game where failures are cognitive planning errors rather than tool execution failures, and which lacks structured tool-call pairs), ERR Efficiency Score is not directly applicable; we substitute a domain-adapted proxy: step-level delta in the normalized ALFWorld game score (Δ(info['score'] / info['max_score']) at each step), which tracks incremental subgoal-completion rate. This is an acknowledged heuristic extension of the ERR framework; whether the recoverability motivation holds for this proxy is explicitly tested in the ablation. A 2-layer MLP probe (with L2 weight decay 1e-4) outputs P(cascade | prefix_k), with Platt scaling applied on a stratified held-out validation split. Training data sparsity (200 labeled trajectories) is addressed by (i) 5-fold cross-validation stratified by benchmark (ALFWorld / WebShop / GAIA) to estimate generalization without benchmark leakage, and (ii) a parallel logistic probe baseline to assess whether MLP complexity is justified over this small labeled set. The AgentErrorBench annotations are distributed unevenly across benchmarks: GAIA contributes approximately 50 of the 200 labeled trajectories, yielding roughly 27 training samples per fold in 3-fold CV (the compressed HIL mode), placing the GAIA cascade probe near the minimum viable supervised learning regime; GAIA results are consequently treated as preliminary evidence, with ALFWorld (approximately 100 trajectories, ~67 per fold) providing the primary evidence base for the main cascade-avoidance claim. CascadeWatch requires no modification to the base agent and does not require retraining the agent backbone; deploying CascadeWatch with a different LLM backbone requires retraining only the lightweight MLP probe (~3–5 H100-hours) against that backbone's embedding space, not retraining the agent itself. This is a meaningful practical advantage over BacktrackAgent, which requires constructing a task-specific training dataset and fine-tuning agent components. The rollback mechanism is specified per benchmark: For ALFWorld, environment-state rollback is performed via command-replay from env.reset(): the TextWorld gym environment is reset to the initial observation, then the k−1 accepted actions from the checkpoint buffer are re-executed sequentially to reconstruct game state at step k−1. The ALFWorld game engine processes each text command in approximately 1–2ms; for typical episodes capped at 50 steps, rollback at step k incurs roughly 25–100ms wall-clock overhead—negligible relative to LLM inference time. A checkpoint buffer stores accepted action sequences at each step to enable replay without re-querying the LLM. Note that TextWorld's Python API does not expose a save/restore mechanism for Glulx-format (.ulx) games used in ALFWorld competition settings, so command-replay is the correct mechanism; the O(k) replay cost is in game-engine steps, not LLM compute. The Crab sandbox (arXiv 2604.28138) provides semantics-aware container-level checkpoint/restore that could in principle support ALFWorld game-state snapshots regardless of the underlying game engine; CascadeWatch uses command-replay to maintain compatibility with standard ALFWorld evaluation setups that do not use containerized sandboxes, and to avoid container-spinup overhead that would dominate the ~25–100ms rollback budget. For WebShop and GAIA, context-only rollback rewinds the agent context window to step k_checkpoint, masks all subsequent actions and observations, and re-samples an alternative action with temperature +0.3. Context-only rollback does not undo irreversible WebShop web-state changes (e.g., submitted searches), which is explicitly noted as a limitation. A false-positive circuit-breaker limits rollback to a maximum of 2 triggers per episode; after the second trigger, monitoring is suspended for the remainder of the episode to prevent compounding disruption. Before full evaluation, we run the Intervention Paradox's 50-task pilot test on each benchmark to empirically verify that CascadeWatch's cascade-specific intervention is net-positive (p > d/(r+d)) on that benchmark; benchmarks where the pilot test fails are reported as negative results, not omitted. We include a pre-registered 3-way ablation: (a) frozen embeddings only → logistic probe, (b) recoverability-delta features only → logistic regression (no embeddings), (c) full CascadeWatch (embeddings + recoverability-delta) → 2-layer MLP. The primary empirical claim is that CascadeWatch achieves task success rate improvement over no-correction baselines on ALFWorld and GAIA while avoiding the performance degradation caused by generic critics observed in the Intervention Paradox—demonstrating for the first time that cascade-specific precision is sufficient to make rollback net-positive on benchmarks where generic critics fail. The recoverability-delta ablation serves as an internal validation gate: if recoverability-delta provides ≥3% F1 lift over frozen embeddings alone, the ERR-motivated feature design is empirically confirmed; if the lift is <3%, the theoretical ERR motivation weakens substantially and this is reported honestly as a negative result on the recoverability signal hypothesis. We evaluate task success rate, steps saved per episode, and false-positive intervention rate against no-correction, ExpeL-style reflection, self-verification, T-STAR offline, and ProMAS-style detection-only baselines on ALFWorld, WebShop, and GAIA (subject to pilot test results).","resource_estimate":{"manual":{"gpu_hours":"~100-140 H100-hours total: rollout generation ~45 H100-hours (Qwen/Qwen3-32B runs in BF16 on 1× H100-80GB without quantization—32B × 2 bytes ≈ 64GB, within the 80GB VRAM budget; inference throughput roughly doubles relative to a 72B model; ~45h covers ~5K synthetic rollouts across three benchmarks at three temperatures, including environment interaction overhead and tool-call latency for GAIA tasks); probe training ~10 H100-hours (5-fold CV × 3-way ablation × logistic/MLP variants; these are small models, <1h each); evaluation runs ~45–85 H100-hours across three benchmarks + pilot tests (50 tasks × 3 benchmarks × 2 conditions per test). ALFWorld command-replay rollback adds <1 H100-hour overhead across all evaluation episodes.","gpu_utilization":"~30–40% effective utilization; high idle between human coding, debugging, and analysis cycles","timeline":"4–6 months","team":"2 researchers","estimated_gpu_cost":"~$200–$280 at ~$2/H100-hour"},"human_in_loop":{"scope_note":"Compressed to satisfy the joint ≤16-day calendar / ≤200 H100-hour constraint. Primary benchmarks reduced to ALFWorld + GAIA (2 of 3); WebShop deferred to optional extension after primary evaluation completes. Synthetic rollouts reduced to 2,000 total at 2 temperatures (T=0.7, T=1.0); 3-fold CV replaces 5-fold. Human gates: cascade label validation, pilot test pass/fail judgment per benchmark, ablation design review, threshold decisions. Human engagement: 2–3 hours/day (not 30 min/day).","compute_breakdown":"Rollout generation (2K rollouts × 2 temperatures = 4K trajectories; ~1K ALFWorld + 1K GAIA per temperature): ~10–15 H100-hours (ALFWorld ~2–3h; GAIA ~8–12h including tool-call overhead; Qwen/Qwen3-32B BF16 on 1× H100-80GB without quantization). Probe training (3-fold CV × 3-way ablation × logistic/MLP): ~3–5 H100-hours. Pilot tests (50 tasks × 2 benchmarks × 2 conditions × 2 seeds = 400 episodes): ~7–10 H100-hours. Full evaluation (post-pilot, 2 benchmarks × 4 baselines + CascadeWatch): ~25–35 H100-hours. Buffer/debugging: ~5–10 H100-hours. Total: ~50–75 H100-hours.","gpu_hours":"~50–75 H100-hours (well within ≤200 H100-hour constraint)","gpu_utilization":"~60–70% utilization; human approval gates reduce compute waste on dead-end ablations","timeline":"12–14 calendar days (achievable within 16-day constraint with efficient pipeline execution: rollout generation days 1–2, labeling + probe training days 2–4, pilot tests with human review days 4–8, full evaluation days 8–12, analysis and write-up days 10–14)","team":"1 researcher, ~2–3 hours/day check-in","claude_api_cost":"$150–$250","estimated_gpu_cost":"~$100–$150 at ~$2/H100-hour","risk_note":"Small labeled training set (200 trajectories) risks MLP overfitting; confirmed-cascade criterion and temperature augmentation strategy are critical human-gate decisions. GAIA contributes approximately 50 of those 200 labeled trajectories (~27 training samples per fold in 3-fold CV), placing the GAIA probe near the minimum viable supervised learning regime—GAIA evaluation results should be treated as preliminary evidence pending replication on a larger annotated set. ALFWorld ERR proxy (game score delta) is a domain adaptation—its F1 contribution must be validated in ablation before committing to full evaluation on ALFWorld. Pilot test (50 tasks × 2 benchmarks) must be reviewed by human before committing to full evaluation on each benchmark. WebShop extension requires an additional ~15–25 H100-hours beyond the primary constraint if pursued."},"auto_research":{"note":"This mode exceeds the primary ≤200 H100-hour constraint and is presented as an extended evaluation scenario for teams with unrestricted compute, not a valid path within the joint 16-day/200 H100-hour constraint. Included for completeness only.","gpu_hours":"~300–450 H100-hours (3–5× more ablations across probe architectures, threshold strategies, feature combinations, augmentation volumes, rollback trigger policies, and minimum-step thresholds; reduced from prior estimates due to Qwen/Qwen3-32B being more compute-efficient than the previously specified 72B model)","gpu_utilization":"~85–95%; near-zero idle as agent continuously queues and launches experiments","timeline":"3–10 days with 4+ H100s in parallel","team":"0 (initial setup only)","claude_api_cost":"$350–$600","estimated_gpu_cost":"~$600–$900","speed_bottleneck":"Number of H100s available; rollout generation dominates throughput","risk_note":"Automated cascade label derivation may skip the confirmed-cascade midpoint filter, generating false positive labels; no human oversight to detect always-predict-cascade degenerate solutions. Pilot test pass/fail judgment and Intervention Paradox threshold calculation require human review—an agent may proceed to full evaluation on benchmarks where intervention is net-negative. ALFWorld ERR proxy domain adaptation requires human judgment to validate before scaling."}},"target_venues":["EMNLP 2026 (ARR deadline May 25, 2026)","AAAI 2027 (abstract deadline expected ~August 2026)"],"level":"solid","key_references":["Where LLM Agents Fail and How They can Learn From Failures (arXiv 2509.25370, 2025)","Recoverability Has a Law: The ERR Measure for Tool-Augmented Agents (arXiv 2601.22352, 2026)","The Intervention Paradox: Accurate Failure Prediction in Agents Does Not Imply Effective Failure Prevention (arXiv 2602.03338, 2026)","Capable but Unreliable: Canonical Path Deviation as a Causal Mechanism of Agent Failure in Long-Horizon Tasks (arXiv 2602.19008, 2026)","Trajectory Guard: A Lightweight, Sequence-Aware Model for Real-Time Anomaly Detection in Agentic AI (AAAI TrustAgent Workshop 2026, arXiv 2601.00516)","ProMAS: Proactive Error Forecasting for Multi-Agent Systems Using Markov Transition Dynamics (arXiv 2603.20260, 2026)","From Spark to Fire: Modeling and Mitigating Error Cascades in LLM-Based Multi-Agent Collaboration (arXiv 2603.04474, 2026)","ProbGuard: Probabilistic Runtime Monitoring for LLM Agent Safety (arXiv 2508.00500, 2025)","Auditing Cascading Risks in Multi-Agent Systems via Semantic–Geometric Co-evolution (ICLR Workshop 2026, arXiv 2603.13325)","Crab: A Semantics-Aware Checkpoint/Restore Runtime for Agent Sandboxes (arXiv 2604.28138, 2026)","Reason in Chains, Learn in Trees: Self-Rectification and Grafting for Multi-turn Agent Policy Optimization (arXiv 2604.07165, 2026)","Self-Verification Dilemma: Experience-Driven Suppression of Overused Checking in LLM Reasoning (arXiv 2602.03485, 2026)","Beyond Fluency: Toward Reliable Trajectories in Agentic IR — position paper on failure modes, not empirical cascade measurement (arXiv 2604.04269, 2026)","BacktrackAgent: Enhancing GUI Agent with Error Detection and Backtracking Mechanism (EMNLP 2025, arXiv 2505.20660)","Step Back to Leap Forward: Self-Backtracking for Boosting Reasoning of Language Models (arXiv 2502.04404, 2025)","Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification (arXiv 2504.05419, 2025)","InferAct: Preemptive Detection and Correction of Misaligned Actions in LLM Agents (EMNLP 2025 main track, arXiv 2407.11843)","MASC: Metacognitive Self-Correction for Multi-Agent System via Prototype-Guided Next-Execution Reconstruction (arXiv 2510.14319, 2025)"],"description":"Long-horizon agent tasks suffer from cascade failures: a single early error propagates across subsequent steps, compounding recovery cost. The critical challenge is the Intervention Paradox (arXiv 2602.03338): a generic critic with AUROC 0.94 causes up to 26 percentage point degradation by disrupting self-correcting trajectories, with all observed regressions occurring at early intervention steps. The solution requires cascade-specific, high-precision detection rather than general failure prediction. We propose CascadeWatch, an inference-time monitor that targets cascade onset specifically using frozen Qwen/Qwen3-32B hidden-state embeddings (HuggingFace: Qwen/Qwen3-32B; 32B dense model; 64GB BF16; fits in 1× H100-80GB without quantization) combined with recoverability delta signals to estimate P(cascade_failure | prefix_k) at each step, with a minimum trigger threshold of step ≥ 5 to avoid the early-step intervention regime where generic critics cause harm. For WebShop and GAIA (tool-augmented benchmarks), recoverability deltas are ERR Efficiency Score deltas (arXiv 2601.22352). For ALFWorld (text-based game with cognitive planning errors, not tool execution failures), ERR Efficiency Score is inapplicable; we use a domain-adapted proxy: step-level delta in the normalized ALFWorld game score, which tracks subgoal completion rate. This domain adaptation is acknowledged as a heuristic extension and is explicitly isolated in the ablation. CascadeWatch is positioned precisely among seven distinct neighboring systems. (1) Canonical Path Deviation (arXiv 2602.19008) identifies stochastic drift from canonical solution paths—aggregated from multiple successful runs per task—as a long-horizon failure mechanism, achieving +8.8pp improvement via restart of lowest-adherence runs; CascadeWatch uses single-trajectory recoverability signals (no canonical paths required) and performs targeted rollback rather than full restarts. (2) From Spark to Fire (arXiv 2603.04474) proposes a genealogy-graph governance layer for cascade mitigation in multi-agent collaboration, improving Benign Infection Control Rate from 0.32 to 0.89; CascadeWatch addresses a structurally different failure mode—cognitive cascade failure within a single agent's sequential trajectory—where there are no inter-agent message dependencies. (3) ProMAS (arXiv 2603.20260) raises alerts in multi-agent reasoning but provides no corrective action and evaluates only on the Who&When attribution benchmark. (4) ProbGuard (arXiv 2508.00500) softly intervenes on physical safety constraints via symbolic DTMC. (5) Trajectory Guard (arXiv 2601.00516) uses a Siamese Recurrent Autoencoder with hybrid contrastive-reconstruction loss to detect trajectory anomalies in agentic AI at 32ms, but targets general structural anomalies rather than cascade-specific onset via recoverability signals, evaluates on security audit and multi-agent benchmarks (not ALFWorld/GAIA), and provides no rollback mechanism. (6) InferAct (arXiv 2407.11843, EMNLP 2025) uses Theory-of-Mind reasoning to detect actions misaligned with user intent before execution and alerts users for human-in-loop correction, achieving up to 20% Marco-F1 improvement; CascadeWatch targets multi-step cascade propagation rather than single-step user-intent misalignment, uses ERR recoverability signals rather than ToM belief inference, and intervenes via automated rollback rather than human alerting. (7) MASC (arXiv 2510.14319) detects cascading errors in multi-agent systems via unsupervised Prototype-Guided Next-Execution Reconstruction embedding anomaly scoring, achieving +8.47% AUC-ROC on the Who&When benchmark; CascadeWatch targets single-agent long-horizon cognitive cascades using supervised ERR-motivated recoverability labels and evaluates on ALFWorld/GAIA rather than multi-agent attribution tasks. Unlike BacktrackAgent (arXiv 2505.20660, EMNLP 2025), which trains a verifier-judger-reflector pipeline for GUI action errors using a task-specific backtracking dataset, CascadeWatch requires no modification to the base agent and does not require retraining the agent backbone; deploying CascadeWatch with a different LLM backbone requires retraining only the lightweight MLP probe (~3–5 H100-hours) against that backbone's embedding space, not retraining the agent itself. Unlike Self-Backtracking (arXiv 2502.04404), which trains the LLM itself to internalize backtracking decisions, CascadeWatch operates as a frozen external probe deployable without model retraining. Prior hidden-state probing work (arXiv 2504.05419) probes single-step reasoning correctness to reduce tokens by 24%; CascadeWatch probes multi-step trajectory prefixes for cascade onset and adds recoverability signals as a second feature channel. CascadeWatch closes the loop on cognitive-task cascades in single-agent long-horizon settings by triggering targeted rollback with a false-positive circuit-breaker (max 2 rollbacks per episode). Rollback mechanism: for ALFWorld, environment-state rollback via command-replay from env.reset() (O(k) game-engine steps; ~25–100ms wall-clock for 50-step episodes; TextWorld's Python API does not expose save/restore for Glulx-format .ulx games; the Crab sandbox, arXiv 2604.28138, provides container-level checkpoint/restore that could support ALFWorld in principle but requires containerization overhead incompatible with standard evaluation setups). For WebShop and GAIA, context-only rollback (agent context rewound to checkpoint; does not undo irreversible web-state changes, acknowledged as a limitation). Cascade labels use a confirmed-cascade criterion (trajectory fails AND root-cause error occurs before the trajectory midpoint) to prevent false labels from partially-recovered trajectories. The GAIA cascade probe operates near the minimum viable supervised learning regime (~27 training samples per fold in 3-fold CV across approximately 50 GAIA-labeled trajectories from AgentErrorBench); GAIA results are treated as preliminary evidence, with ALFWorld (approximately 100 trajectories, ~67 per fold) providing the primary evidence base for the main cascade-avoidance claim. The primary empirical claim is that CascadeWatch achieves task success rate improvement over no-correction baselines on ALFWorld and GAIA while avoiding the performance degradation caused by generic critics (the Intervention Paradox)—demonstrating that cascade-specific precision is sufficient to make rollback net-positive on benchmarks where generic critics fail. The recoverability-delta ablation (embeddings-only vs. recoverability-delta-only vs. combined) serves as an internal validation gate: ≥3% F1 lift from recoverability-delta confirms the ERR-motivated feature design; <3% lift is reported as a negative result. Evaluated on ALFWorld and GAIA as primary benchmarks (WebShop as optional extension), each preceded by the Intervention Paradox's 50-task pilot test to verify net-positive intervention before full evaluation. The compressed HIL execution mode (2 benchmarks, 2K rollouts, 3-fold CV, 2–3 hours/day human engagement) fits within ~50–75 H100-hours and 12–14 calendar days, comfortably within the ≤200 H100-hour and ≤16-day constraints.","project_name":"cascade_monitor","source":"web_research"}

agentId: aa4740e3b5507b77e (use SendMessage with to: 'aa4740e3b5507b77e' to continue this agent)
&lt;usage>total_tokens: 80541
tool_uses: 7
duration_ms: 1529087&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "11efee4e-0a09-48a1-a46b-f7eb3c049f6b",
  "isSidechain": false,
  "promptId": "438b2a64-25e3-4fd7-bd11-ea7d73d2ec1f",
  "type": "user",
  "uuid": "a79e0de5-8d13-4ff1-9a8c-7b5c65e5eab3",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are a research-idea editor. Your job is to produce a COMPLETE revised JSON for a research idea called \"CascadeWatch.\" I will give you the full original JSON and precise instructions. Output ONLY the JSON — no prose before or after.\n\n## What to change\n\n**Change type: minor**\n\nAdd exactly two new citation blocks to the `landscape` field and integrate both papers into `description` and `key_references`. Do NOT change anything else.\n\n### Insertion 1 — MASC — insert immediately after the ProMAS paragraph in `landscape`\n\nThe ProMAS paragraph ends with: \"...it is a detector only and evaluates exclusively on the Who&When multi-agent attribution benchmark, not on single-agent long-horizon tasks.\"\n\nInsert this new paragraph after it:\n\n\"MASC (arXiv 2510.14319, October 2025) proposes metacognitive self-correction for multi-agent systems via Prototype-Guided Next-Execution Reconstruction: it predicts embeddings of upcoming execution steps from interaction history (Next-Execution Reconstruction) and stabilizes anomaly scoring against a learned prototype of normal-step embeddings (Prototype-Guided Enhancement), triggering a correction agent to revise the acting agent's output before error propagation; it achieves +8.47% AUC-ROC in step-level error detection on the Who&When benchmark. Three distinctions separate MASC from CascadeWatch: (1) MASC targets multi-agent systems where errors propagate across agent boundaries via message passing; CascadeWatch targets single-agent long-horizon cognitive cascades where errors compound within a single sequential trajectory. (2) MASC's anomaly scoring is unsupervised—reconstruction error against a learned normal-step prototype detects any deviation, regardless of whether it constitutes a cascade-initiating event; CascadeWatch's cascade detection is supervised using ERR Efficiency Score recoverability-delta labels derived from confirmed-cascade annotations (trajectory fails AND root-cause error before midpoint), specifically distinguishing cascade-onset patterns from recoverable deviations that the Intervention Paradox shows should not be interrupted. (3) MASC evaluates on the Who&When multi-agent attribution benchmark; CascadeWatch evaluates on ALFWorld and GAIA single-agent long-horizon task benchmarks, where the failure mode is cognitive planning error propagation rather than inter-agent message corruption.\"\n\n### Insertion 2 — InferAct — insert immediately after the Trajectory Guard paragraph in `landscape`\n\nThe Trajectory Guard paragraph ends with: \"...The lightweight framing ('inference-time monitoring of agentic trajectories') directly overlaps with CascadeWatch's positioning, but the two systems target structurally different failure modes: Trajectory Guard's reconstruction error is task-agnostic and catches any structural deviation, while CascadeWatch's recoverability-delta specifically targets the compounding-cost prefix patterns that confirm cascade onset in long-horizon cognitive tasks.\"\n\nInsert this new paragraph after it:\n\n\"InferAct (arXiv 2407.11843, EMNLP 2025 main track) uses Theory-of-Mind reasoning—grounded in LLM belief inference about user intent—to preemptively detect actions misaligned with user authorization before execution and alert users for timely correction, achieving up to 20% Marco-F1 improvement in misaligned-action detection across three evaluation tasks. Two distinctions separate InferAct from CascadeWatch: (1) InferAct targets single-step action misalignment—whether a specific upcoming action (e.g., executing a buy-now command without user authorization) matches user intent—using ToM belief inference; CascadeWatch targets multi-step cascade propagation, where an early-step error (cognitive planning error, tool-call compounding) compounds across subsequent trajectory steps regardless of user intent, using trajectory-prefix ERR recoverability signals rather than belief reasoning about user authorization. (2) InferAct's intervention is human-in-loop: it raises an alert and waits for user correction before the misaligned action executes, making it unsuitable for fully autonomous long-horizon operation; CascadeWatch's intervention is automated rollback to a pre-cascade checkpoint with no human availability requirement, and is gated by a false-positive circuit-breaker (max 2 rollbacks per episode) rather than human judgment. InferAct and CascadeWatch address complementary failure modes—unauthorized action execution versus self-compounding cascade failure—in agent safety.\"\n\n### Insertion 3 — description field\n\nIn the `description` field, find the sentence: \"CascadeWatch is positioned precisely among five distinct neighboring systems.\"\n\nReplace \"five\" with \"seven\" and add, at the end of that positioning list (after the Trajectory Guard entry which ends \"...provides no rollback mechanism\"), two new entries:\n\n\"(6) InferAct (arXiv 2407.11843, EMNLP 2025) uses Theory-of-Mind reasoning to detect actions misaligned with user intent before execution and alerts users for human-in-loop correction, achieving up to 20% Marco-F1 improvement; CascadeWatch targets multi-step cascade propagation rather than single-step user-intent misalignment, uses ERR recoverability signals rather than ToM belief inference, and intervenes via automated rollback rather than human alerting. (7) MASC (arXiv 2510.14319) detects cascading errors in multi-agent systems via unsupervised Prototype-Guided Next-Execution Reconstruction embedding anomaly scoring, achieving +8.47% AUC-ROC on the Who&When benchmark; CascadeWatch targets single-agent long-horizon cognitive cascades using supervised ERR-motivated recoverability labels and evaluates on ALFWorld/GAIA rather than multi-agent attribution tasks.\"\n\n### Insertion 4 — key_references field\n\nAdd two new entries to the key_references list:\n- \"InferAct: Preemptive Detection and Correction of Misaligned Actions in LLM Agents (EMNLP 2025 main track, arXiv 2407.11843)\"\n- \"MASC: Metacognitive Self-Correction for Multi-Agent System via Prototype-Guided Next-Execution Reconstruction (arXiv 2510.14319, 2025)\"\n\n### Add field\nAdd `\"change_type\": \"minor\"` to the top-level JSON object.\n\n## Original JSON\n\n```json\n{\n  \"title\": \"CascadeWatch: Cascade-Onset Detection with Targeted Rollback for Long-Horizon Agent Tasks\",\n  \"core_problem\": \"In long-horizon agent tasks, individual early-step errors produce cascading downstream failures that grow exponentially more costly to correct with each additional step. The core question is whether a lightweight trained monitor can prospectively detect cascade onset—predicting failure propagation before it fully manifests—to trigger targeted rollback rather than reactive reflection or full replanning. The challenge is not simply detecting failure: the Intervention Paradox (arXiv 2602.03338) establishes that generic critics with AUROC 0.94 cause up to 26 percentage point performance degradation by triggering on non-cascade failures that the agent would have self-corrected. The disruption-recovery tradeoff (Δ Success = p·r − (1−p)·d) only favors intervention on high-failure benchmarks like ALFWorld; it degrades GAIA and HotPotQA even with accurate critics. The solution is not a better generic critic but a cascade-specific one: targeting only the recoverability-degrading prefix patterns that precede confirmed cascades—detectable via recoverability proxy signals—to achieve the high precision (low d) and focused recall (high p conditional on cascade-onset) that shifts the threshold in favor of intervention. A natural alternative early-warning signal is canonical path deviation (arXiv 2602.19008): measuring Jaccard similarity of tool invocations against the convergent set shared across successful runs. This signal is empirically validated but requires aggregating tool invocation sequences from multiple successful runs per task, making it unavailable for novel tasks or low-success-rate settings. CascadeWatch uses ERR Efficiency Score recoverability deltas (arXiv 2601.22352) computable from single trajectories without reference to other runs, enabling cascade detection in the absence of precomputed canonical paths. The rollback mechanism varies by environment affordance: for text-game environments (ALFWorld), full environment-state rollback is achieved via command-replay from env.reset(); for tool-augmented environments (WebShop, GAIA), context-only rollback rewinds the agent's context window. Neither mechanism requires a non-existent API; both are acknowledged to have environment-specific costs and limitations.\",\n  \"opportunity\": \"The cascade failure pattern is now well-characterized and trainable. AgentErrorBench (arXiv 2509.25370) provides the first systematically annotated failure taxonomy across ALFWorld, WebShop, and GAIA, with root-cause step annotations identifying where cascades originate; memory and reflection errors at steps 5–15 are the most common initiators, crucially occurring mid-trajectory rather than at the earliest steps where the Intervention Paradox shows all regressions occur. The ERR paper (arXiv 2601.22352) formalizes recoverability as Expected Recovery Regret and derives a measurable Efficiency Score proxy, empirically validated across five benchmarks to within δ ≤ 0.05 of observed post-failure regret—establishing that step-level recoverability is observable from trajectory prefixes and thus learnable as a predictive signal. This signal applies directly to tool-augmented agents (WebShop, GAIA) where structured tool-call/result pairs provide natural Efficiency Score observables; for text-game environments (ALFWorld), where failures are cognitive planning errors rather than tool execution failures, a domain-adapted proxy (step-level game score delta) is used instead, acknowledged as a heuristic extension. Canonical Path Deviation (arXiv 2602.19008) provides independent corroboration of the self-reinforcing cascade mechanism in long-horizon tool-use tasks: each off-canonical tool invocation raises the probability that the next invocation is also off-canonical by 22.7 percentage points, confirming that cascade propagation is empirically measurable and compounding. CascadeWatch uses recoverability signals rather than canonical path adherence specifically because recoverability deltas are computable from a single trajectory, enabling deployment where canonical paths from multiple successful runs are unavailable. BacktrackAgent (arXiv 2505.20660, EMNLP 2025) demonstrates that backtracking triggers improve GUI agent task completion on Mobile3M and Auto-UI benchmarks, but requires constructing a task-specific training dataset and fine-tuning the agent components—leaving a clear gap for an external, training-free cascade monitor that operates on any frozen agent in cognitive long-horizon tasks. The proactive detection landscape now includes ProMAS (arXiv 2603.20260) for multi-agent error attribution, ProbGuard (arXiv 2508.00500) for physical safety monitoring, and Trajectory Guard (arXiv 2601.00516) for general structural anomaly detection in agentic trajectories, but none targets cognitive-task cascade failure in single-agent long-horizon settings nor closes the detection-to-rollback loop. The labeled failure datasets, recoverability signals, and the Intervention Paradox's threshold formula together make a specific, testable hypothesis: a cascade-specific monitor using recoverability signals will achieve sufficiently higher precision than generic critics to make rollback net-positive on benchmarks where generic critics fail, for the first time.\",\n  \"landscape\": \"Proactive monitoring is an active and crowded area that must be navigated carefully. ProMAS (arXiv 2603.20260, March 2026) uses Causal Delta Features mapped to a 30-prototype Vector Markov Space with a frozen Meta-Llama-3.1-8B extractor to predict failure onset in multi-agent collaborative reasoning systems, achieving 22.97% step-level accuracy on the Who&When benchmark (annotated multi-agent dialogues of math and logic puzzles) while processing only 27% of reasoning logs. Critically, ProMAS raises an alert but provides no corrective action—it is a detector only and evaluates exclusively on the Who&When multi-agent attribution benchmark, not on single-agent long-horizon tasks. ProbGuard (arXiv 2508.00500) learns a Discrete-Time Markov Chain from symbolic agent-state abstractions with PAC-style guarantees and triggers prompt-injection interventions when P(unsafe state) exceeds a threshold; it predicts traffic violations up to 38.66 seconds ahead and reduces unsafe behavior by 65.37% in embodied agents, but operates on physical safety constraints using symbolic abstractions rather than frozen neural representations or recoverability signals. Trajectory Guard (arXiv 2601.00516, AAAI TrustAgent Workshop 2026) proposes a Siamese Recurrent Autoencoder with hybrid contrastive-reconstruction loss for real-time anomaly detection in agentic AI trajectories, achieving F1 0.88–0.94 on balanced sets and recall 0.86–0.92 on imbalanced external benchmarks while running 17–27× faster than LLM Judge baselines at 32ms inference. Three distinctions separate this from CascadeWatch: (1) Trajectory Guard detects general structural anomalies—contextual misalignment and sequential incoherence—via reconstruction error, not cascade-specific onset via recoverability-delta signals; (2) it evaluates on synthetic perturbations, security audit failures (RAS-Eval), and multi-agent attribution (Who&When), not on single-agent long-horizon cognitive tasks (ALFWorld, GAIA); (3) it provides no rollback or correction mechanism—detection only. The lightweight framing ('inference-time monitoring of agentic trajectories') directly overlaps with CascadeWatch's positioning, but the two systems target structurally different failure modes: Trajectory Guard's reconstruction error is task-agnostic and catches any structural deviation, while CascadeWatch's recoverability-delta specifically targets the compounding-cost prefix patterns that confirm cascade onset in long-horizon cognitive tasks. The ORC auditing paper (ICLR Workshop 2026, arXiv 2603.13325) detects cascading risks in multi-agent systems via Ollivier-Ricci Curvature on completed interaction graphs—post-hoc auditing, not inference-time intervention. Canonical Path Deviation (arXiv 2602.19008, Feb 2026) is the closest theoretical neighbor to CascadeWatch's cascade-onset framing. Analyzing 515 model-task combinations on the Toolathlon benchmark (22 frontier models, 108 real-world tool-use tasks across 3 independent runs each), Wilson Y. Lee identifies stochastic drift from canonical solution paths—the convergent set of tool invocations shared across successful runs—as a causal mechanism of long-horizon failure. Path adherence is measured as Jaccard similarity between actual and canonical tool invocation sequences; adherence gaps are statistically indistinguishable from zero through the first half of trajectories but become significant and self-reinforcing thereafter, with each off-canonical tool call raising the probability that the next call is also off-canonical by 22.7 percentage points. An intervention restarting the bottom tercile of runs by mid-trajectory canonical adherence achieves +8.8pp success rate improvement. Three distinctions separate this from CascadeWatch: (1) Canonical path adherence requires aggregating tool invocation sequences across multiple successful runs per task—unavailable for novel tasks or low-success-rate settings; CascadeWatch's ERR Efficiency Score recoverability proxy is computable from a single trajectory without reference to other runs. (2) Canonical path deviation detects drift retrospectively via trajectory statistics that become significant only in the second half of execution; CascadeWatch proactively intervenes at steps 5–15 using a trained probe on prefix embeddings, before adherence divergence solidifies. (3) The CPD intervention is a full task restart of lowest-adherence runs; CascadeWatch performs targeted rollback to the pre-cascade checkpoint, preserving valid completed steps and avoiding full re-execution cost. From Spark to Fire (arXiv 2603.04474, March 2026) models cascade error propagation in LLM-based multi-agent collaboration using an individual-based mean-field framework over inter-agent communication graphs, and proposes a genealogy-graph governance layer that tracks atomic claim provenance via NLI-based verification (Green/Red/Yellow status using DeBERTa-v3-small) and blocks transmission of error-carrying messages; the Benign Infection Control Rate (complement of attack success rate) improves from 0.32 to 0.89 across Chain, Mesh, and Star multi-agent topologies on data-analysis, logic, and MMLU tasks. The cascade mechanism is specifically inter-agent: atomic factuality errors injected at one agent propagate through recursive message reuse across rounds of collaboration—a phenomenon requiring multiple communicating agents. CascadeWatch addresses a structurally different failure mode—cognitive cascade failure within a single agent's sequential trajectory (ALFWorld's planning errors, GAIA's tool-call compounding)—where there are no inter-agent message dependencies and no genealogy graph can be constructed. The per-message NLI verification in From Spark to Fire also introduces latency proportional to message volume; CascadeWatch adds only a single 2-layer MLP forward pass per step. The Intervention Paradox (arXiv 2602.03338) is the most important negative result in the space: ROLLBACK and APPEND interventions triggered by a generic LLM critic (AUROC 0.94) degrade performance on HotPotQA by −2.3 to −25.5pp and on GAIA by −4.4 to −30pp; only ALFWorld (high baseline failure rate: 5.8–14.7%) shows improvement (+0.5 to +2.8pp). All observed regressions occur with early-step (step ≤ 2) interventions. BacktrackAgent (arXiv 2505.20660, EMNLP 2025) trains a verifier-judger-reflector pipeline for GUI agents (Mobile3M, Auto-UI benchmarks) to detect individual action errors and trigger backtracking. Unlike CascadeWatch, BacktrackAgent requires constructing a task-specific training dataset and fine-tuning the agent's backtracking components; it targets GUI action-level errors (click/type correctness) rather than recoverability-degrading cascade onset in cognitive long-horizon tasks, and provides no recoverability signal. Self-Backtracking (arXiv 2502.04404) trains the base LLM to internalize when and where to backtrack during training and inference, achieving over 40% performance gains over optimal-path SFT baselines in general reasoning. This approach requires model retraining and modifies the agent's internal reasoning; CascadeWatch operates as a frozen external probe on any pre-trained agent, requiring no modification to the agent and no access to model weights or training infrastructure. Deploying CascadeWatch with a different LLM backbone requires retraining only the lightweight MLP probe (~3–5 H100-hours) against that backbone's embedding space—not retraining the backbone itself. Prior work probes LLM hidden states for single-step answer correctness in mathematical reasoning (arXiv 2504.05419), achieving 24% token reduction via early exit by detecting when intermediate reasoning steps are correct. The mechanism is structurally similar to CascadeWatch's frozen embedding + MLP probe, but targets single-step step-level correctness rather than multi-step cascade onset in agent trajectories; crucially, it adds no recoverability signal channel and does not address long-horizon failure propagation. Reactive self-correction methods share the same fundamental limitation: ExpeL and Contextual Experience Replay distill past trajectories for future improvement; self-verification (arXiv 2602.03485) confirms rechecks rarely identify errors; T-STAR (arXiv 2604.07165) achieves training-time divergence detection via Cognitive Trees but adds no inference-time mechanism. No existing system combines cascade-specific detection using recoverability signals with targeted rollback and a false-positive circuit-breaker, nor validates that cascade-specific precision avoids the Intervention Paradox's disruption-recovery tradeoff.\",\n  \"approach\": \"We train CascadeWatch to address the Intervention Paradox by targeting only the recoverability-degrading mid-trajectory patterns that precede confirmed cascades. Training data: AgentErrorBench's 200 expert-annotated trajectories (davide221/agenterrorbench on HuggingFace, spanning ALFWorld, WebShop, and GAIA) augmented with ~5,000 synthetic rollouts from Qwen/Qwen3-32B (HuggingFace: Qwen/Qwen3-32B; 32B dense model; 64GB BF16; fits in 1× H100-80GB without quantization—the Qwen3-72B designation referenced in earlier drafts corresponds to unofficial community merges and lacks an authoritative reproducible checkpoint) sampled at three temperatures (0.7, 1.0, 1.3) to increase failure-mode diversity. Cascade labels use a confirmed-cascade criterion: a step k is labeled cascade-onset only if (1) the trajectory ultimately fails, (2) step k is at or after the earliest annotated root-cause error, AND (3) the root-cause error occurs before the trajectory midpoint (step ≤ ⌊total_steps / 2⌋)—this filters out partially-recovered trajectories and prevents false cascade labels from error-tolerant agents. A minimum intervention threshold of step ≥ 5 is imposed at inference time, consistent with AgentErrorBench's finding that cascade-initiating errors occur at steps 5–15 and with the Intervention Paradox's finding that all observed regressions involve step ≤ 2 interventions. Each trajectory prefix at step k is represented by concatenating (a) frozen Qwen/Qwen3-32B hidden-state embeddings (mean-pooled last 4 transformer layers over the action–observation sequence) with (b) recoverability delta signals. For WebShop and GAIA (tool-augmented benchmarks with structured tool-call/result pairs), these are ERR Efficiency Score deltas as defined in arXiv 2601.22352. For ALFWorld (a text-based game where failures are cognitive planning errors rather than tool execution failures, and which lacks structured tool-call pairs), ERR Efficiency Score is not directly applicable; we substitute a domain-adapted proxy: step-level delta in the normalized ALFWorld game score (Δ(info['score'] / info['max_score']) at each step), which tracks incremental subgoal-completion rate. This is an acknowledged heuristic extension of the ERR framework; whether the recoverability motivation holds for this proxy is explicitly tested in the ablation. A 2-layer MLP probe (with L2 weight decay 1e-4) outputs P(cascade | prefix_k), with Platt scaling applied on a stratified held-out validation split. Training data sparsity (200 labeled trajectories) is addressed by (i) 5-fold cross-validation stratified by benchmark (ALFWorld / WebShop / GAIA) to estimate generalization without benchmark leakage, and (ii) a parallel logistic probe baseline to assess whether MLP complexity is justified over this small labeled set. The AgentErrorBench annotations are distributed unevenly across benchmarks: GAIA contributes approximately 50 of the 200 labeled trajectories, yielding roughly 27 training samples per fold in 3-fold CV (the compressed HIL mode), placing the GAIA cascade probe near the minimum viable supervised learning regime; GAIA results are consequently treated as preliminary evidence, with ALFWorld (approximately 100 trajectories, ~67 per fold) providing the primary evidence base for the main cascade-avoidance claim. CascadeWatch requires no modification to the base agent and does not require retraining the agent backbone; deploying CascadeWatch with a different LLM backbone requires retraining only the lightweight MLP probe (~3–5 H100-hours) against that backbone's embedding space, not retraining the agent itself. This is a meaningful practical advantage over BacktrackAgent, which requires constructing a task-specific training dataset and fine-tuning agent components. The rollback mechanism is specified per benchmark: For ALFWorld, environment-state rollback is performed via command-replay from env.reset(): the TextWorld gym environment is reset to the initial observation, then the k−1 accepted actions from the checkpoint buffer are re-executed sequentially to reconstruct game state at step k−1. The ALFWorld game engine processes each text command in approximately 1–2ms; for typical episodes capped at 50 steps, rollback at step k incurs roughly 25–100ms wall-clock overhead—negligible relative to LLM inference time. A checkpoint buffer stores accepted action sequences at each step to enable replay without re-querying the LLM. Note that TextWorld's Python API does not expose a save/restore mechanism for Glulx-format (.ulx) games used in ALFWorld competition settings, so command-replay is the correct mechanism; the O(k) replay cost is in game-engine steps, not LLM compute. The Crab sandbox (arXiv 2604.28138) provides semantics-aware container-level checkpoint/restore that could in principle support ALFWorld game-state snapshots regardless of the underlying game engine; CascadeWatch uses command-replay to maintain compatibility with standard ALFWorld evaluation setups that do not use containerized sandboxes, and to avoid container-spinup overhead that would dominate the ~25–100ms rollback budget. For WebShop and GAIA, context-only rollback rewinds the agent context window to step k_checkpoint, masks all subsequent actions and observations, and re-samples an alternative action with temperature +0.3. Context-only rollback does not undo irreversible WebShop web-state changes (e.g., submitted searches), which is explicitly noted as a limitation. A false-positive circuit-breaker limits rollback to a maximum of 2 triggers per episode; after the second trigger, monitoring is suspended for the remainder of the episode to prevent compounding disruption. Before full evaluation, we run the Intervention Paradox's 50-task pilot test on each benchmark to empirically verify that CascadeWatch's cascade-specific intervention is net-positive (p > d/(r+d)) on that benchmark; benchmarks where the pilot test fails are reported as negative results, not omitted. We include a pre-registered 3-way ablation: (a) frozen embeddings only → logistic probe, (b) recoverability-delta features only → logistic regression (no embeddings), (c) full CascadeWatch (embeddings + recoverability-delta) → 2-layer MLP. The primary empirical claim is that CascadeWatch achieves task success rate improvement over no-correction baselines on ALFWorld and GAIA while avoiding the performance degradation caused by generic critics observed in the Intervention Paradox—demonstrating for the first time that cascade-specific precision is sufficient to make rollback net-positive on benchmarks where generic critics fail. The recoverability-delta ablation serves as an internal validation gate: if recoverability-delta provides ≥3% F1 lift over frozen embeddings alone, the ERR-motivated feature design is empirically confirmed; if the lift is <3%, the theoretical ERR motivation weakens substantially and this is reported honestly as a negative result on the recoverability signal hypothesis. We evaluate task success rate, steps saved per episode, and false-positive intervention rate against no-correction, ExpeL-style reflection, self-verification, T-STAR offline, and ProMAS-style detection-only baselines on ALFWorld, WebShop, and GAIA (subject to pilot test results).\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~100-140 H100-hours total: rollout generation ~45 H100-hours (Qwen/Qwen3-32B runs in BF16 on 1× H100-80GB without quantization—32B × 2 bytes ≈ 64GB, within the 80GB VRAM budget; inference throughput roughly doubles relative to a 72B model; ~45h covers ~5K synthetic rollouts across three benchmarks at three temperatures, including environment interaction overhead and tool-call latency for GAIA tasks); probe training ~10 H100-hours (5-fold CV × 3-way ablation × logistic/MLP variants; these are small models, <1h each); evaluation runs ~45–85 H100-hours across three benchmarks + pilot tests (50 tasks × 3 benchmarks × 2 conditions per test). ALFWorld command-replay rollback adds <1 H100-hour overhead across all evaluation episodes.\",\n      \"gpu_utilization\": \"~30–40% effective utilization; high idle between human coding, debugging, and analysis cycles\",\n      \"timeline\": \"4–6 months\",\n      \"team\": \"2 researchers\",\n      \"estimated_gpu_cost\": \"~$200–$280 at ~$2/H100-hour\"\n    },\n    \"human_in_loop\": {\n      \"scope_note\": \"Compressed to satisfy the joint ≤16-day calendar / ≤200 H100-hour constraint. Primary benchmarks reduced to ALFWorld + GAIA (2 of 3); WebShop deferred to optional extension after primary evaluation completes. Synthetic rollouts reduced to 2,000 total at 2 temperatures (T=0.7, T=1.0); 3-fold CV replaces 5-fold. Human gates: cascade label validation, pilot test pass/fail judgment per benchmark, ablation design review, threshold decisions. Human engagement: 2–3 hours/day (not 30 min/day).\",\n      \"compute_breakdown\": \"Rollout generation (2K rollouts × 2 temperatures = 4K trajectories; ~1K ALFWorld + 1K GAIA per temperature): ~10–15 H100-hours (ALFWorld ~2–3h; GAIA ~8–12h including tool-call overhead; Qwen/Qwen3-32B BF16 on 1× H100-80GB without quantization). Probe training (3-fold CV × 3-way ablation × logistic/MLP): ~3–5 H100-hours. Pilot tests (50 tasks × 2 benchmarks × 2 conditions × 2 seeds = 400 episodes): ~7–10 H100-hours. Full evaluation (post-pilot, 2 benchmarks × 4 baselines + CascadeWatch): ~25–35 H100-hours. Buffer/debugging: ~5–10 H100-hours. Total: ~50–75 H100-hours.\",\n      \"gpu_hours\": \"~50–75 H100-hours (well within ≤200 H100-hour constraint)\",\n      \"gpu_utilization\": \"~60–70% utilization; human approval gates reduce compute waste on dead-end ablations\",\n      \"timeline\": \"12–14 calendar days (achievable within 16-day constraint with efficient pipeline execution: rollout generation days 1–2, labeling + probe training days 2–4, pilot tests with human review days 4–8, full evaluation days 8–12, analysis and write-up days 10–14)\",\n      \"team\": \"1 researcher, ~2–3 hours/day check-in\",\n      \"claude_api_cost\": \"$150–$250\",\n      \"estimated_gpu_cost\": \"~$100–$150 at ~$2/H100-hour\",\n      \"risk_note\": \"Small labeled training set (200 trajectories) risks MLP overfitting; confirmed-cascade criterion and temperature augmentation strategy are critical human-gate decisions. GAIA contributes approximately 50 of those 200 labeled trajectories (~27 training samples per fold in 3-fold CV), placing the GAIA probe near the minimum viable supervised learning regime—GAIA evaluation results should be treated as preliminary evidence pending replication on a larger annotated set. ALFWorld ERR proxy (game score delta) is a domain adaptation—its F1 contribution must be validated in ablation before committing to full evaluation on ALFWorld. Pilot test (50 tasks × 2 benchmarks) must be reviewed by human before committing to full evaluation on each benchmark. WebShop extension requires an additional ~15–25 H100-hours beyond the primary constraint if pursued.\"\n    },\n    \"auto_research\": {\n      \"note\": \"This mode exceeds the primary ≤200 H100-hour constraint and is presented as an extended evaluation scenario for teams with unrestricted compute, not a valid path within the joint 16-day/200 H100-hour constraint. Included for completeness only.\",\n      \"gpu_hours\": \"~300–450 H100-hours (3–5× more ablations across probe architectures, threshold strategies, feature combinations, augmentation volumes, rollback trigger policies, and minimum-step thresholds; reduced from prior estimates due to Qwen/Qwen3-32B being more compute-efficient than the previously specified 72B model)\",\n      \"gpu_utilization\": \"~85–95%; near-zero idle as agent continuously queues and launches experiments\",\n      \"timeline\": \"3–10 days with 4+ H100s in parallel\",\n      \"team\": \"0 (initial setup only)\",\n      \"claude_api_cost\": \"$350–$600\",\n      \"estimated_gpu_cost\": \"~$600–$900\",\n      \"speed_bottleneck\": \"Number of H100s available; rollout generation dominates throughput\",\n      \"risk_note\": \"Automated cascade label derivation may skip the confirmed-cascade midpoint filter, generating false positive labels; no human oversight to detect always-predict-cascade degenerate solutions. Pilot test pass/fail judgment and Intervention Paradox threshold calculation require human review—an agent may proceed to full evaluation on benchmarks where intervention is net-negative. ALFWorld ERR proxy domain adaptation requires human judgment to validate before scaling.\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 (ARR deadline May 25, 2026)\",\n    \"AAAI 2027 (abstract deadline expected ~August 2026)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"Where LLM Agents Fail and How They can Learn From Failures (arXiv 2509.25370, 2025)\",\n    \"Recoverability Has a Law: The ERR Measure for Tool-Augmented Agents (arXiv 2601.22352, 2026)\",\n    \"The Intervention Paradox: Accurate Failure Prediction in Agents Does Not Imply Effective Failure Prevention (arXiv 2602.03338, 2026)\",\n    \"Capable but Unreliable: Canonical Path Deviation as a Causal Mechanism of Agent Failure in Long-Horizon Tasks (arXiv 2602.19008, 2026)\",\n    \"Trajectory Guard: A Lightweight, Sequence-Aware Model for Real-Time Anomaly Detection in Agentic AI (AAAI TrustAgent Workshop 2026, arXiv 2601.00516)\",\n    \"ProMAS: Proactive Error Forecasting for Multi-Agent Systems Using Markov Transition Dynamics (arXiv 2603.20260, 2026)\",\n    \"From Spark to Fire: Modeling and Mitigating Error Cascades in LLM-Based Multi-Agent Collaboration (arXiv 2603.04474, 2026)\",\n    \"ProbGuard: Probabilistic Runtime Monitoring for LLM Agent Safety (arXiv 2508.00500, 2025)\",\n    \"Auditing Cascading Risks in Multi-Agent Systems via Semantic–Geometric Co-evolution (ICLR Workshop 2026, arXiv 2603.13325)\",\n    \"Crab: A Semantics-Aware Checkpoint/Restore Runtime for Agent Sandboxes (arXiv 2604.28138, 2026)\",\n    \"Reason in Chains, Learn in Trees: Self-Rectification and Grafting for Multi-turn Agent Policy Optimization (arXiv 2604.07165, 2026)\",\n    \"Self-Verification Dilemma: Experience-Driven Suppression of Overused Checking in LLM Reasoning (arXiv 2602.03485, 2026)\",\n    \"Beyond Fluency: Toward Reliable Trajectories in Agentic IR — position paper on failure modes, not empirical cascade measurement (arXiv 2604.04269, 2026)\",\n    \"BacktrackAgent: Enhancing GUI Agent with Error Detection and Backtracking Mechanism (EMNLP 2025, arXiv 2505.20660)\",\n    \"Step Back to Leap Forward: Self-Backtracking for Boosting Reasoning of Language Models (arXiv 2502.04404, 2025)\",\n    \"Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification (arXiv 2504.05419, 2025)\"\n  ],\n  \"description\": \"Long-horizon agent tasks suffer from cascade failures: a single early error propagates across subsequent steps, compounding recovery cost. The critical challenge is the Intervention Paradox (arXiv 2602.03338): a generic critic with AUROC 0.94 causes up to 26 percentage point degradation by disrupting self-correcting trajectories, with all observed regressions occurring at early intervention steps. The solution requires cascade-specific, high-precision detection rather than general failure prediction. We propose CascadeWatch, an inference-time monitor that targets cascade onset specifically using frozen Qwen/Qwen3-32B hidden-state embeddings (HuggingFace: Qwen/Qwen3-32B; 32B dense model; 64GB BF16; fits in 1× H100-80GB without quantization) combined with recoverability delta signals to estimate P(cascade_failure | prefix_k) at each step, with a minimum trigger threshold of step ≥ 5 to avoid the early-step intervention regime where generic critics cause harm. For WebShop and GAIA (tool-augmented benchmarks), recoverability deltas are ERR Efficiency Score deltas (arXiv 2601.22352). For ALFWorld (text-based game with cognitive planning errors, not tool execution failures), ERR Efficiency Score is inapplicable; we use a domain-adapted proxy: step-level delta in the normalized ALFWorld game score, which tracks subgoal completion rate. This domain adaptation is acknowledged as a heuristic extension and is explicitly isolated in the ablation. CascadeWatch is positioned precisely among five distinct neighboring systems. (1) Canonical Path Deviation (arXiv 2602.19008) identifies stochastic drift from canonical solution paths—aggregated from multiple successful runs per task—as a long-horizon failure mechanism, achieving +8.8pp improvement via restart of lowest-adherence runs; CascadeWatch uses single-trajectory recoverability signals (no canonical paths required) and performs targeted rollback rather than full restarts. (2) From Spark to Fire (arXiv 2603.04474) proposes a genealogy-graph governance layer for cascade mitigation in multi-agent collaboration, improving Benign Infection Control Rate from 0.32 to 0.89; CascadeWatch addresses a structurally different failure mode—cognitive cascade failure within a single agent's sequential trajectory—where there are no inter-agent message dependencies. (3) ProMAS (arXiv 2603.20260) raises alerts in multi-agent reasoning but provides no corrective action and evaluates only on the Who&When attribution benchmark. (4) ProbGuard (arXiv 2508.00500) softly intervenes on physical safety constraints via symbolic DTMC. (5) Trajectory Guard (arXiv 2601.00516) uses a Siamese Recurrent Autoencoder with hybrid contrastive-reconstruction loss to detect trajectory anomalies in agentic AI at 32ms, but targets general structural anomalies rather than cascade-specific onset via recoverability signals, evaluates on security audit and multi-agent benchmarks (not ALFWorld/GAIA), and provides no rollback mechanism. Unlike BacktrackAgent (arXiv 2505.20660, EMNLP 2025), which trains a verifier-judger-reflector pipeline for GUI action errors using a task-specific backtracking dataset, CascadeWatch requires no modification to the base agent and does not require retraining the agent backbone; deploying CascadeWatch with a different LLM backbone requires retraining only the lightweight MLP probe (~3–5 H100-hours) against that backbone's embedding space, not retraining the agent itself. Unlike Self-Backtracking (arXiv 2502.04404), which trains the LLM itself to internalize backtracking decisions, CascadeWatch operates as a frozen external probe deployable without model retraining. Prior hidden-state probing work (arXiv 2504.05419) probes single-step reasoning correctness to reduce tokens by 24%; CascadeWatch probes multi-step trajectory prefixes for cascade onset and adds recoverability signals as a second feature channel. CascadeWatch closes the loop on cognitive-task cascades in single-agent long-horizon settings by triggering targeted rollback with a false-positive circuit-breaker (max 2 rollbacks per episode). Rollback mechanism: for ALFWorld, environment-state rollback via command-replay from env.reset() (O(k) game-engine steps; ~25–100ms wall-clock for 50-step episodes; TextWorld's Python API does not expose save/restore for Glulx-format .ulx games; the Crab sandbox, arXiv 2604.28138, provides container-level checkpoint/restore that could support ALFWorld in principle but requires containerization overhead incompatible with standard evaluation setups). For WebShop and GAIA, context-only rollback (agent context rewound to checkpoint; does not undo irreversible web-state changes, acknowledged as a limitation). Cascade labels use a confirmed-cascade criterion (trajectory fails AND root-cause error occurs before the trajectory midpoint) to prevent false labels from partially-recovered trajectories. The GAIA cascade probe operates near the minimum viable supervised learning regime (~27 training samples per fold in 3-fold CV across approximately 50 GAIA-labeled trajectories from AgentErrorBench); GAIA results are treated as preliminary evidence, with ALFWorld (approximately 100 trajectories, ~67 per fold) providing the primary evidence base for the main cascade-avoidance claim. The primary empirical claim is that CascadeWatch achieves task success rate improvement over no-correction baselines on ALFWorld and GAIA while avoiding the performance degradation caused by generic critics (the Intervention Paradox)—demonstrating that cascade-specific precision is sufficient to make rollback net-positive on benchmarks where generic critics fail. The recoverability-delta ablation (embeddings-only vs. recoverability-delta-only vs. combined) serves as an internal validation gate: ≥3% F1 lift from recoverability-delta confirms the ERR-motivated feature design; <3% lift is reported as a negative result. Evaluated on ALFWorld and GAIA as primary benchmarks (WebShop as optional extension), each preceded by the Intervention Paradox's 50-task pilot test to verify net-positive intervention before full evaluation. The compressed HIL execution mode (2 benchmarks, 2K rollouts, 3-fold CV, 2–3 hours/day human engagement) fits within ~50–75 H100-hours and 12–14 calendar days, comfortably within the ≤200 H100-hour and ≤16-day constraints.\",\n  \"project_name\": \"cascade_monitor\",\n  \"source\": \"web_research\"\n}\n```\n\nNow produce the complete revised JSON applying exactly the four insertions described above. Output ONLY valid JSON, no markdown fences, no prose.",
    "agentId": "aa4740e3b5507b77e",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I'll output the complete revised JSON directly in my response:\n\n{\"change_type\":\"minor\",\"title\":\"CascadeWatch: Cascade-Onset Detection with Targeted Rollback for Long-Horizon Agent Tasks\",\"core_problem\":\"In long-horizon agent tasks, individual early-step errors produce cascading downstream failures that grow exponentially more costly to correct with each additional step. The core question is whether a lightweight trained monitor can prospectively detect cascade onset—predicting failure propagation before it fully manifests—to trigger targeted rollback rather than reactive reflection or full replanning. The challenge is not simply detecting failure: the Intervention Paradox (arXiv 2602.03338) establishes that generic critics with AUROC 0.94 cause up to 26 percentage point performance degradation by triggering on non-cascade failures that the agent would have self-corrected. The disruption-recovery tradeoff (Δ Success = p·r − (1−p)·d) only favors intervention on high-failure benchmarks like ALFWorld; it degrades GAIA and HotPotQA even with accurate critics. The solution is not a better generic critic but a cascade-specific one: targeting only the recoverability-degrading prefix patterns that precede confirmed cascades—detectable via recoverability proxy signals—to achieve the high precision (low d) and focused recall (high p conditional on cascade-onset) that shifts the threshold in favor of intervention. A natural alternative early-warning signal is canonical path deviation (arXiv 2602.19008): measuring Jaccard similarity of tool invocations against the convergent set shared across successful runs. This signal is empirically validated but requires aggregating tool invocation sequences from multiple successful runs per task, making it unavailable for novel tasks or low-success-rate settings. CascadeWatch uses ERR Efficiency Score recoverability deltas (arXiv 2601.22352) computable from single trajectories without reference to other runs, enabling cascade detection in the absence of precomputed canonical paths. The rollback mechanism varies by environment affordance: for text-game environments (ALFWorld), full environment-state rollback is achieved via command-replay from env.reset(); for tool-augmented environments (WebShop, GAIA), context-only rollback rewinds the agent's context window. Neither mechanism requires a non-existent API; both are acknowledged to have environment-specific costs and limitations.\",\"opportunity\":\"The cascade failure pattern is now well-characterized and trainable. AgentErrorBench (arXiv 2509.25370) provides the first systematically annotated failure taxonomy across ALFWorld, WebShop, and GAIA, with root-cause step annotations identifying where cascades originate; memory and reflection errors at steps 5–15 are the most common initiators, crucially occurring mid-trajectory rather than at the earliest steps where the Intervention Paradox shows all regressions occur. The ERR paper (arXiv 2601.22352) formalizes recoverability as Expected Recovery Regret and derives a measurable Efficiency Score proxy, empirically validated across five benchmarks to within δ ≤ 0.05 of observed post-failure regret—establishing that step-level recoverability is observable from trajectory prefixes and thus learnable as a predictive signal. This signal applies directly to tool-augmented agents (WebShop, GAIA) where structured tool-call/result pairs provide natural Efficiency Score observables; for text-game environments (ALFWorld), where failures are cognitive planning errors rather than tool execution failures, a domain-adapted proxy (step-level game score delta) is used instead, acknowledged as a heuristic extension. Canonical Path Deviation (arXiv 2602.19008) provides independent corroboration of the self-reinforcing cascade mechanism in long-horizon tool-use tasks: each off-canonical tool invocation raises the probability that the next invocation is also off-canonical by 22.7 percentage points, confirming that cascade propagation is empirically measurable and compounding. CascadeWatch uses recoverability signals rather than canonical path adherence specifically because recoverability deltas are computable from a single trajectory, enabling deployment where canonical paths from multiple successful runs are unavailable. BacktrackAgent (arXiv 2505.20660, EMNLP 2025) demonstrates that backtracking triggers improve GUI agent task completion on Mobile3M and Auto-UI benchmarks, but requires constructing a task-specific training dataset and fine-tuning the agent components—leaving a clear gap for an external, training-free cascade monitor that operates on any frozen agent in cognitive long-horizon tasks. The proactive detection landscape now includes ProMAS (arXiv 2603.20260) for multi-agent error attribution, ProbGuard (arXiv 2508.00500) for physical safety monitoring, and Trajectory Guard (arXiv 2601.00516) for general structural anomaly detection in agentic trajectories, but none targets cognitive-task cascade failure in single-agent long-horizon settings nor closes the detection-to-rollback loop. The labeled failure datasets, recoverability signals, and the Intervention Paradox's threshold formula together make a specific, testable hypothesis: a cascade-specific monitor using recoverability signals will achieve sufficiently higher precision than generic critics to make rollback net-positive on benchmarks where generic critics fail, for the first time.\",\"landscape\":\"Proactive monitoring is an active and crowded area that must be navigated carefully. ProMAS (arXiv 2603.20260, March 2026) uses Causal Delta Features mapped to a 30-prototype Vector Markov Space with a frozen Meta-Llama-3.1-8B extractor to predict failure onset in multi-agent collaborative reasoning systems, achieving 22.97% step-level accuracy on the Who&When benchmark (annotated multi-agent dialogues of math and logic puzzles) while processing only 27% of reasoning logs. Critically, ProMAS raises an alert but provides no corrective action—it is a detector only and evaluates exclusively on the Who&When multi-agent attribution benchmark, not on single-agent long-horizon tasks. MASC (arXiv 2510.14319, October 2025) proposes metacognitive self-correction for multi-agent systems via Prototype-Guided Next-Execution Reconstruction: it predicts embeddings of upcoming execution steps from interaction history (Next-Execution Reconstruction) and stabilizes anomaly scoring against a learned prototype of normal-step embeddings (Prototype-Guided Enhancement), triggering a correction agent to revise the acting agent's output before error propagation; it achieves +8.47% AUC-ROC in step-level error detection on the Who&When benchmark. Three distinctions separate MASC from CascadeWatch: (1) MASC targets multi-agent systems where errors propagate across agent boundaries via message passing; CascadeWatch targets single-agent long-horizon cognitive cascades where errors compound within a single sequential trajectory. (2) MASC's anomaly scoring is unsupervised—reconstruction error against a learned normal-step prototype detects any deviation, regardless of whether it constitutes a cascade-initiating event; CascadeWatch's cascade detection is supervised using ERR Efficiency Score recoverability-delta labels derived from confirmed-cascade annotations (trajectory fails AND root-cause error before midpoint), specifically distinguishing cascade-onset patterns from recoverable deviations that the Intervention Paradox shows should not be interrupted. (3) MASC evaluates on the Who&When multi-agent attribution benchmark; CascadeWatch evaluates on ALFWorld and GAIA single-agent long-horizon task benchmarks, where the failure mode is cognitive planning error propagation rather than inter-agent message corruption. ProbGuard (arXiv 2508.00500) learns a Discrete-Time Markov Chain from symbolic agent-state abstractions with PAC-style guarantees and triggers prompt-injection interventions when P(unsafe state) exceeds a threshold; it predicts traffic violations up to 38.66 seconds ahead and reduces unsafe behavior by 65.37% in embodied agents, but operates on physical safety constraints using symbolic abstractions rather than frozen neural representations or recoverability signals. Trajectory Guard (arXiv 2601.00516, AAAI TrustAgent Workshop 2026) proposes a Siamese Recurrent Autoencoder with hybrid contrastive-reconstruction loss for real-time anomaly detection in agentic AI trajectories, achieving F1 0.88–0.94 on balanced sets and recall 0.86–0.92 on imbalanced external benchmarks while running 17–27× faster than LLM Judge baselines at 32ms inference. Three distinctions separate this from CascadeWatch: (1) Trajectory Guard detects general structural anomalies—contextual misalignment and sequential incoherence—via reconstruction error, not cascade-specific onset via recoverability-delta signals; (2) it evaluates on synthetic perturbations, security audit failures (RAS-Eval), and multi-agent attribution (Who&When), not on single-agent long-horizon cognitive tasks (ALFWorld, GAIA); (3) it provides no rollback or correction mechanism—detection only. The lightweight framing ('inference-time monitoring of agentic trajectories') directly overlaps with CascadeWatch's positioning, but the two systems target structurally different failure modes: Trajectory Guard's reconstruction error is task-agnostic and catches any structural deviation, while CascadeWatch's recoverability-delta specifically targets the compounding-cost prefix patterns that confirm cascade onset in long-horizon cognitive tasks. InferAct (arXiv 2407.11843, EMNLP 2025 main track) uses Theory-of-Mind reasoning—grounded in LLM belief inference about user intent—to preemptively detect actions misaligned with user authorization before execution and alert users for timely correction, achieving up to 20% Marco-F1 improvement in misaligned-action detection across three evaluation tasks. Two distinctions separate InferAct from CascadeWatch: (1) InferAct targets single-step action misalignment—whether a specific upcoming action (e.g., executing a buy-now command without user authorization) matches user intent—using ToM belief inference; CascadeWatch targets multi-step cascade propagation, where an early-step error (cognitive planning error, tool-call compounding) compounds across subsequent trajectory steps regardless of user intent, using trajectory-prefix ERR recoverability signals rather than belief reasoning about user authorization. (2) InferAct's intervention is human-in-loop: it raises an alert and waits for user correction before the misaligned action executes, making it unsuitable for fully autonomous long-horizon operation; CascadeWatch's intervention is automated rollback to a pre-cascade checkpoint with no human availability requirement, and is gated by a false-positive circuit-breaker (max 2 rollbacks per episode) rather than human judgment. InferAct and CascadeWatch address complementary failure modes—unauthorized action execution versus self-compounding cascade failure—in agent safety. The ORC auditing paper (ICLR Workshop 2026, arXiv 2603.13325) detects cascading risks in multi-agent systems via Ollivier-Ricci Curvature on completed interaction graphs—post-hoc auditing, not inference-time intervention. Canonical Path Deviation (arXiv 2602.19008, Feb 2026) is the closest theoretical neighbor to CascadeWatch's cascade-onset framing. Analyzing 515 model-task combinations on the Toolathlon benchmark (22 frontier models, 108 real-world tool-use tasks across 3 independent runs each), Wilson Y. Lee identifies stochastic drift from canonical solution paths—the convergent set of tool invocations shared across successful runs—as a causal mechanism of long-horizon failure. Path adherence is measured as Jaccard similarity between actual and canonical tool invocation sequences; adherence gaps are statistically indistinguishable from zero through the first half of trajectories but become significant and self-reinforcing thereafter, with each off-canonical tool call raising the probability that the next call is also off-canonical by 22.7 percentage points. An intervention restarting the bottom tercile of runs by mid-trajectory canonical adherence achieves +8.8pp success rate improvement. Three distinctions separate this from CascadeWatch: (1) Canonical path adherence requires aggregating tool invocation sequences across multiple successful runs per task—unavailable for novel tasks or low-success-rate settings; CascadeWatch's ERR Efficiency Score recoverability proxy is computable from a single trajectory without reference to other runs. (2) Canonical path deviation detects drift retrospectively via trajectory statistics that become significant only in the second half of execution; CascadeWatch proactively intervenes at steps 5–15 using a trained probe on prefix embeddings, before adherence divergence solidifies. (3) The CPD intervention is a full task restart of lowest-adherence runs; CascadeWatch performs targeted rollback to the pre-cascade checkpoint, preserving valid completed steps and avoiding full re-execution cost. From Spark to Fire (arXiv 2603.04474, March 2026) models cascade error propagation in LLM-based multi-agent collaboration using an individual-based mean-field framework over inter-agent communication graphs, and proposes a genealogy-graph governance layer that tracks atomic claim provenance via NLI-based verification (Green/Red/Yellow status using DeBERTa-v3-small) and blocks transmission of error-carrying messages; the Benign Infection Control Rate (complement of attack success rate) improves from 0.32 to 0.89 across Chain, Mesh, and Star multi-agent topologies on data-analysis, logic, and MMLU tasks. The cascade mechanism is specifically inter-agent: atomic factuality errors injected at one agent propagate through recursive message reuse across rounds of collaboration—a phenomenon requiring multiple communicating agents. CascadeWatch addresses a structurally different failure mode—cognitive cascade failure within a single agent's sequential trajectory (ALFWorld's planning errors, GAIA's tool-call compounding)—where there are no inter-agent message dependencies and no genealogy graph can be constructed. The per-message NLI verification in From Spark to Fire also introduces latency proportional to message volume; CascadeWatch adds only a single 2-layer MLP forward pass per step. The Intervention Paradox (arXiv 2602.03338) is the most important negative result in the space: ROLLBACK and APPEND interventions triggered by a generic LLM critic (AUROC 0.94) degrade performance on HotPotQA by −2.3 to −25.5pp and on GAIA by −4.4 to −30pp; only ALFWorld (high baseline failure rate: 5.8–14.7%) shows improvement (+0.5 to +2.8pp). All observed regressions occur with early-step (step ≤ 2) interventions. BacktrackAgent (arXiv 2505.20660, EMNLP 2025) trains a verifier-judger-reflector pipeline for GUI agents (Mobile3M, Auto-UI benchmarks) to detect individual action errors and trigger backtracking. Unlike CascadeWatch, BacktrackAgent requires constructing a task-specific training dataset and fine-tuning the agent's backtracking components; it targets GUI action-level errors (click/type correctness) rather than recoverability-degrading cascade onset in cognitive long-horizon tasks, and provides no recoverability signal. Self-Backtracking (arXiv 2502.04404) trains the base LLM to internalize when and where to backtrack during training and inference, achieving over 40% performance gains over optimal-path SFT baselines in general reasoning. This approach requires model retraining and modifies the agent's internal reasoning; CascadeWatch operates as a frozen external probe on any pre-trained agent, requiring no modification to the agent and no access to model weights or training infrastructure. Deploying CascadeWatch with a different LLM backbone requires retraining only the lightweight MLP probe (~3–5 H100-hours) against that backbone's embedding space—not retraining the backbone itself. Prior work probes LLM hidden states for single-step answer correctness in mathematical reasoning (arXiv 2504.05419), achieving 24% token reduction via early exit by detecting when intermediate reasoning steps are correct. The mechanism is structurally similar to CascadeWatch's frozen embedding + MLP probe, but targets single-step step-level correctness rather than multi-step cascade onset in agent trajectories; crucially, it adds no recoverability signal channel and does not address long-horizon failure propagation. Reactive self-correction methods share the same fundamental limitation: ExpeL and Contextual Experience Replay distill past trajectories for future improvement; self-verification (arXiv 2602.03485) confirms rechecks rarely identify errors; T-STAR (arXiv 2604.07165) achieves training-time divergence detection via Cognitive Trees but adds no inference-time mechanism. No existing system combines cascade-specific detection using recoverability signals with targeted rollback and a false-positive circuit-breaker, nor validates that cascade-specific precision avoids the Intervention Paradox's disruption-recovery tradeoff.\",\"approach\":\"We train CascadeWatch to address the Intervention Paradox by targeting only the recoverability-degrading mid-trajectory patterns that precede confirmed cascades. Training data: AgentErrorBench's 200 expert-annotated trajectories (davide221/agenterrorbench on HuggingFace, spanning ALFWorld, WebShop, and GAIA) augmented with ~5,000 synthetic rollouts from Qwen/Qwen3-32B (HuggingFace: Qwen/Qwen3-32B; 32B dense model; 64GB BF16; fits in 1× H100-80GB without quantization—the Qwen3-72B designation referenced in earlier drafts corresponds to unofficial community merges and lacks an authoritative reproducible checkpoint) sampled at three temperatures (0.7, 1.0, 1.3) to increase failure-mode diversity. Cascade labels use a confirmed-cascade criterion: a step k is labeled cascade-onset only if (1) the trajectory ultimately fails, (2) step k is at or after the earliest annotated root-cause error, AND (3) the root-cause error occurs before the trajectory midpoint (step ≤ ⌊total_steps / 2⌋)—this filters out partially-recovered trajectories and prevents false cascade labels from error-tolerant agents. A minimum intervention threshold of step ≥ 5 is imposed at inference time, consistent with AgentErrorBench's finding that cascade-initiating errors occur at steps 5–15 and with the Intervention Paradox's finding that all observed regressions involve step ≤ 2 interventions. Each trajectory prefix at step k is represented by concatenating (a) frozen Qwen/Qwen3-32B hidden-state embeddings (mean-pooled last 4 transformer layers over the action–observation sequence) with (b) recoverability delta signals. For WebShop and GAIA (tool-augmented benchmarks with structured tool-call/result pairs), these are ERR Efficiency Score deltas as defined in arXiv 2601.22352. For ALFWorld (a text-based game where failures are cognitive planning errors rather than tool execution failures, and which lacks structured tool-call pairs), ERR Efficiency Score is not directly applicable; we substitute a domain-adapted proxy: step-level delta in the normalized ALFWorld game score (Δ(info['score'] / info['max_score']) at each step), which tracks incremental subgoal-completion rate. This is an acknowledged heuristic extension of the ERR framework; whether the recoverability motivation holds for this proxy is explicitly tested in the ablation. A 2-layer MLP probe (with L2 weight decay 1e-4) outputs P(cascade | prefix_k), with Platt scaling applied on a stratified held-out validation split. Training data sparsity (200 labeled trajectories) is addressed by (i) 5-fold cross-validation stratified by benchmark (ALFWorld / WebShop / GAIA) to estimate generalization without benchmark leakage, and (ii) a parallel logistic probe baseline to assess whether MLP complexity is justified over this small labeled set. The AgentErrorBench annotations are distributed unevenly across benchmarks: GAIA contributes approximately 50 of the 200 labeled trajectories, yielding roughly 27 training samples per fold in 3-fold CV (the compressed HIL mode), placing the GAIA cascade probe near the minimum viable supervised learning regime; GAIA results are consequently treated as preliminary evidence, with ALFWorld (approximately 100 trajectories, ~67 per fold) providing the primary evidence base for the main cascade-avoidance claim. CascadeWatch requires no modification to the base agent and does not require retraining the agent backbone; deploying CascadeWatch with a different LLM backbone requires retraining only the lightweight MLP probe (~3–5 H100-hours) against that backbone's embedding space, not retraining the agent itself. This is a meaningful practical advantage over BacktrackAgent, which requires constructing a task-specific training dataset and fine-tuning agent components. The rollback mechanism is specified per benchmark: For ALFWorld, environment-state rollback is performed via command-replay from env.reset(): the TextWorld gym environment is reset to the initial observation, then the k−1 accepted actions from the checkpoint buffer are re-executed sequentially to reconstruct game state at step k−1. The ALFWorld game engine processes each text command in approximately 1–2ms; for typical episodes capped at 50 steps, rollback at step k incurs roughly 25–100ms wall-clock overhead—negligible relative to LLM inference time. A checkpoint buffer stores accepted action sequences at each step to enable replay without re-querying the LLM. Note that TextWorld's Python API does not expose a save/restore mechanism for Glulx-format (.ulx) games used in ALFWorld competition settings, so command-replay is the correct mechanism; the O(k) replay cost is in game-engine steps, not LLM compute. The Crab sandbox (arXiv 2604.28138) provides semantics-aware container-level checkpoint/restore that could in principle support ALFWorld game-state snapshots regardless of the underlying game engine; CascadeWatch uses command-replay to maintain compatibility with standard ALFWorld evaluation setups that do not use containerized sandboxes, and to avoid container-spinup overhead that would dominate the ~25–100ms rollback budget. For WebShop and GAIA, context-only rollback rewinds the agent context window to step k_checkpoint, masks all subsequent actions and observations, and re-samples an alternative action with temperature +0.3. Context-only rollback does not undo irreversible WebShop web-state changes (e.g., submitted searches), which is explicitly noted as a limitation. A false-positive circuit-breaker limits rollback to a maximum of 2 triggers per episode; after the second trigger, monitoring is suspended for the remainder of the episode to prevent compounding disruption. Before full evaluation, we run the Intervention Paradox's 50-task pilot test on each benchmark to empirically verify that CascadeWatch's cascade-specific intervention is net-positive (p > d/(r+d)) on that benchmark; benchmarks where the pilot test fails are reported as negative results, not omitted. We include a pre-registered 3-way ablation: (a) frozen embeddings only → logistic probe, (b) recoverability-delta features only → logistic regression (no embeddings), (c) full CascadeWatch (embeddings + recoverability-delta) → 2-layer MLP. The primary empirical claim is that CascadeWatch achieves task success rate improvement over no-correction baselines on ALFWorld and GAIA while avoiding the performance degradation caused by generic critics observed in the Intervention Paradox—demonstrating for the first time that cascade-specific precision is sufficient to make rollback net-positive on benchmarks where generic critics fail. The recoverability-delta ablation serves as an internal validation gate: if recoverability-delta provides ≥3% F1 lift over frozen embeddings alone, the ERR-motivated feature design is empirically confirmed; if the lift is <3%, the theoretical ERR motivation weakens substantially and this is reported honestly as a negative result on the recoverability signal hypothesis. We evaluate task success rate, steps saved per episode, and false-positive intervention rate against no-correction, ExpeL-style reflection, self-verification, T-STAR offline, and ProMAS-style detection-only baselines on ALFWorld, WebShop, and GAIA (subject to pilot test results).\",\"resource_estimate\":{\"manual\":{\"gpu_hours\":\"~100-140 H100-hours total: rollout generation ~45 H100-hours (Qwen/Qwen3-32B runs in BF16 on 1× H100-80GB without quantization—32B × 2 bytes ≈ 64GB, within the 80GB VRAM budget; inference throughput roughly doubles relative to a 72B model; ~45h covers ~5K synthetic rollouts across three benchmarks at three temperatures, including environment interaction overhead and tool-call latency for GAIA tasks); probe training ~10 H100-hours (5-fold CV × 3-way ablation × logistic/MLP variants; these are small models, <1h each); evaluation runs ~45–85 H100-hours across three benchmarks + pilot tests (50 tasks × 3 benchmarks × 2 conditions per test). ALFWorld command-replay rollback adds <1 H100-hour overhead across all evaluation episodes.\",\"gpu_utilization\":\"~30–40% effective utilization; high idle between human coding, debugging, and analysis cycles\",\"timeline\":\"4–6 months\",\"team\":\"2 researchers\",\"estimated_gpu_cost\":\"~$200–$280 at ~$2/H100-hour\"},\"human_in_loop\":{\"scope_note\":\"Compressed to satisfy the joint ≤16-day calendar / ≤200 H100-hour constraint. Primary benchmarks reduced to ALFWorld + GAIA (2 of 3); WebShop deferred to optional extension after primary evaluation completes. Synthetic rollouts reduced to 2,000 total at 2 temperatures (T=0.7, T=1.0); 3-fold CV replaces 5-fold. Human gates: cascade label validation, pilot test pass/fail judgment per benchmark, ablation design review, threshold decisions. Human engagement: 2–3 hours/day (not 30 min/day).\",\"compute_breakdown\":\"Rollout generation (2K rollouts × 2 temperatures = 4K trajectories; ~1K ALFWorld + 1K GAIA per temperature): ~10–15 H100-hours (ALFWorld ~2–3h; GAIA ~8–12h including tool-call overhead; Qwen/Qwen3-32B BF16 on 1× H100-80GB without quantization). Probe training (3-fold CV × 3-way ablation × logistic/MLP): ~3–5 H100-hours. Pilot tests (50 tasks × 2 benchmarks × 2 conditions × 2 seeds = 400 episodes): ~7–10 H100-hours. Full evaluation (post-pilot, 2 benchmarks × 4 baselines + CascadeWatch): ~25–35 H100-hours. Buffer/debugging: ~5–10 H100-hours. Total: ~50–75 H100-hours.\",\"gpu_hours\":\"~50–75 H100-hours (well within ≤200 H100-hour constraint)\",\"gpu_utilization\":\"~60–70% utilization; human approval gates reduce compute waste on dead-end ablations\",\"timeline\":\"12–14 calendar days (achievable within 16-day constraint with efficient pipeline execution: rollout generation days 1–2, labeling + probe training days 2–4, pilot tests with human review days 4–8, full evaluation days 8–12, analysis and write-up days 10–14)\",\"team\":\"1 researcher, ~2–3 hours/day check-in\",\"claude_api_cost\":\"$150–$250\",\"estimated_gpu_cost\":\"~$100–$150 at ~$2/H100-hour\",\"risk_note\":\"Small labeled training set (200 trajectories) risks MLP overfitting; confirmed-cascade criterion and temperature augmentation strategy are critical human-gate decisions. GAIA contributes approximately 50 of those 200 labeled trajectories (~27 training samples per fold in 3-fold CV), placing the GAIA probe near the minimum viable supervised learning regime—GAIA evaluation results should be treated as preliminary evidence pending replication on a larger annotated set. ALFWorld ERR proxy (game score delta) is a domain adaptation—its F1 contribution must be validated in ablation before committing to full evaluation on ALFWorld. Pilot test (50 tasks × 2 benchmarks) must be reviewed by human before committing to full evaluation on each benchmark. WebShop extension requires an additional ~15–25 H100-hours beyond the primary constraint if pursued.\"},\"auto_research\":{\"note\":\"This mode exceeds the primary ≤200 H100-hour constraint and is presented as an extended evaluation scenario for teams with unrestricted compute, not a valid path within the joint 16-day/200 H100-hour constraint. Included for completeness only.\",\"gpu_hours\":\"~300–450 H100-hours (3–5× more ablations across probe architectures, threshold strategies, feature combinations, augmentation volumes, rollback trigger policies, and minimum-step thresholds; reduced from prior estimates due to Qwen/Qwen3-32B being more compute-efficient than the previously specified 72B model)\",\"gpu_utilization\":\"~85–95%; near-zero idle as agent continuously queues and launches experiments\",\"timeline\":\"3–10 days with 4+ H100s in parallel\",\"team\":\"0 (initial setup only)\",\"claude_api_cost\":\"$350–$600\",\"estimated_gpu_cost\":\"~$600–$900\",\"speed_bottleneck\":\"Number of H100s available; rollout generation dominates throughput\",\"risk_note\":\"Automated cascade label derivation may skip the confirmed-cascade midpoint filter, generating false positive labels; no human oversight to detect always-predict-cascade degenerate solutions. Pilot test pass/fail judgment and Intervention Paradox threshold calculation require human review—an agent may proceed to full evaluation on benchmarks where intervention is net-negative. ALFWorld ERR proxy domain adaptation requires human judgment to validate before scaling.\"}},\"target_venues\":[\"EMNLP 2026 (ARR deadline May 25, 2026)\",\"AAAI 2027 (abstract deadline expected ~August 2026)\"],\"level\":\"solid\",\"key_references\":[\"Where LLM Agents Fail and How They can Learn From Failures (arXiv 2509.25370, 2025)\",\"Recoverability Has a Law: The ERR Measure for Tool-Augmented Agents (arXiv 2601.22352, 2026)\",\"The Intervention Paradox: Accurate Failure Prediction in Agents Does Not Imply Effective Failure Prevention (arXiv 2602.03338, 2026)\",\"Capable but Unreliable: Canonical Path Deviation as a Causal Mechanism of Agent Failure in Long-Horizon Tasks (arXiv 2602.19008, 2026)\",\"Trajectory Guard: A Lightweight, Sequence-Aware Model for Real-Time Anomaly Detection in Agentic AI (AAAI TrustAgent Workshop 2026, arXiv 2601.00516)\",\"ProMAS: Proactive Error Forecasting for Multi-Agent Systems Using Markov Transition Dynamics (arXiv 2603.20260, 2026)\",\"From Spark to Fire: Modeling and Mitigating Error Cascades in LLM-Based Multi-Agent Collaboration (arXiv 2603.04474, 2026)\",\"ProbGuard: Probabilistic Runtime Monitoring for LLM Agent Safety (arXiv 2508.00500, 2025)\",\"Auditing Cascading Risks in Multi-Agent Systems via Semantic–Geometric Co-evolution (ICLR Workshop 2026, arXiv 2603.13325)\",\"Crab: A Semantics-Aware Checkpoint/Restore Runtime for Agent Sandboxes (arXiv 2604.28138, 2026)\",\"Reason in Chains, Learn in Trees: Self-Rectification and Grafting for Multi-turn Agent Policy Optimization (arXiv 2604.07165, 2026)\",\"Self-Verification Dilemma: Experience-Driven Suppression of Overused Checking in LLM Reasoning (arXiv 2602.03485, 2026)\",\"Beyond Fluency: Toward Reliable Trajectories in Agentic IR — position paper on failure modes, not empirical cascade measurement (arXiv 2604.04269, 2026)\",\"BacktrackAgent: Enhancing GUI Agent with Error Detection and Backtracking Mechanism (EMNLP 2025, arXiv 2505.20660)\",\"Step Back to Leap Forward: Self-Backtracking for Boosting Reasoning of Language Models (arXiv 2502.04404, 2025)\",\"Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification (arXiv 2504.05419, 2025)\",\"InferAct: Preemptive Detection and Correction of Misaligned Actions in LLM Agents (EMNLP 2025 main track, arXiv 2407.11843)\",\"MASC: Metacognitive Self-Correction for Multi-Agent System via Prototype-Guided Next-Execution Reconstruction (arXiv 2510.14319, 2025)\"],\"description\":\"Long-horizon agent tasks suffer from cascade failures: a single early error propagates across subsequent steps, compounding recovery cost. The critical challenge is the Intervention Paradox (arXiv 2602.03338): a generic critic with AUROC 0.94 causes up to 26 percentage point degradation by disrupting self-correcting trajectories, with all observed regressions occurring at early intervention steps. The solution requires cascade-specific, high-precision detection rather than general failure prediction. We propose CascadeWatch, an inference-time monitor that targets cascade onset specifically using frozen Qwen/Qwen3-32B hidden-state embeddings (HuggingFace: Qwen/Qwen3-32B; 32B dense model; 64GB BF16; fits in 1× H100-80GB without quantization) combined with recoverability delta signals to estimate P(cascade_failure | prefix_k) at each step, with a minimum trigger threshold of step ≥ 5 to avoid the early-step intervention regime where generic critics cause harm. For WebShop and GAIA (tool-augmented benchmarks), recoverability deltas are ERR Efficiency Score deltas (arXiv 2601.22352). For ALFWorld (text-based game with cognitive planning errors, not tool execution failures), ERR Efficiency Score is inapplicable; we use a domain-adapted proxy: step-level delta in the normalized ALFWorld game score, which tracks subgoal completion rate. This domain adaptation is acknowledged as a heuristic extension and is explicitly isolated in the ablation. CascadeWatch is positioned precisely among seven distinct neighboring systems. (1) Canonical Path Deviation (arXiv 2602.19008) identifies stochastic drift from canonical solution paths—aggregated from multiple successful runs per task—as a long-horizon failure mechanism, achieving +8.8pp improvement via restart of lowest-adherence runs; CascadeWatch uses single-trajectory recoverability signals (no canonical paths required) and performs targeted rollback rather than full restarts. (2) From Spark to Fire (arXiv 2603.04474) proposes a genealogy-graph governance layer for cascade mitigation in multi-agent collaboration, improving Benign Infection Control Rate from 0.32 to 0.89; CascadeWatch addresses a structurally different failure mode—cognitive cascade failure within a single agent's sequential trajectory—where there are no inter-agent message dependencies. (3) ProMAS (arXiv 2603.20260) raises alerts in multi-agent reasoning but provides no corrective action and evaluates only on the Who&When attribution benchmark. (4) ProbGuard (arXiv 2508.00500) softly intervenes on physical safety constraints via symbolic DTMC. (5) Trajectory Guard (arXiv 2601.00516) uses a Siamese Recurrent Autoencoder with hybrid contrastive-reconstruction loss to detect trajectory anomalies in agentic AI at 32ms, but targets general structural anomalies rather than cascade-specific onset via recoverability signals, evaluates on security audit and multi-agent benchmarks (not ALFWorld/GAIA), and provides no rollback mechanism. (6) InferAct (arXiv 2407.11843, EMNLP 2025) uses Theory-of-Mind reasoning to detect actions misaligned with user intent before execution and alerts users for human-in-loop correction, achieving up to 20% Marco-F1 improvement; CascadeWatch targets multi-step cascade propagation rather than single-step user-intent misalignment, uses ERR recoverability signals rather than ToM belief inference, and intervenes via automated rollback rather than human alerting. (7) MASC (arXiv 2510.14319) detects cascading errors in multi-agent systems via unsupervised Prototype-Guided Next-Execution Reconstruction embedding anomaly scoring, achieving +8.47% AUC-ROC on the Who&When benchmark; CascadeWatch targets single-agent long-horizon cognitive cascades using supervised ERR-motivated recoverability labels and evaluates on ALFWorld/GAIA rather than multi-agent attribution tasks. Unlike BacktrackAgent (arXiv 2505.20660, EMNLP 2025), which trains a verifier-judger-reflector pipeline for GUI action errors using a task-specific backtracking dataset, CascadeWatch requires no modification to the base agent and does not require retraining the agent backbone; deploying CascadeWatch with a different LLM backbone requires retraining only the lightweight MLP probe (~3–5 H100-hours) against that backbone's embedding space, not retraining the agent itself. Unlike Self-Backtracking (arXiv 2502.04404), which trains the LLM itself to internalize backtracking decisions, CascadeWatch operates as a frozen external probe deployable without model retraining. Prior hidden-state probing work (arXiv 2504.05419) probes single-step reasoning correctness to reduce tokens by 24%; CascadeWatch probes multi-step trajectory prefixes for cascade onset and adds recoverability signals as a second feature channel. CascadeWatch closes the loop on cognitive-task cascades in single-agent long-horizon settings by triggering targeted rollback with a false-positive circuit-breaker (max 2 rollbacks per episode). Rollback mechanism: for ALFWorld, environment-state rollback via command-replay from env.reset() (O(k) game-engine steps; ~25–100ms wall-clock for 50-step episodes; TextWorld's Python API does not expose save/restore for Glulx-format .ulx games; the Crab sandbox, arXiv 2604.28138, provides container-level checkpoint/restore that could support ALFWorld in principle but requires containerization overhead incompatible with standard evaluation setups). For WebShop and GAIA, context-only rollback (agent context rewound to checkpoint; does not undo irreversible web-state changes, acknowledged as a limitation). Cascade labels use a confirmed-cascade criterion (trajectory fails AND root-cause error occurs before the trajectory midpoint) to prevent false labels from partially-recovered trajectories. The GAIA cascade probe operates near the minimum viable supervised learning regime (~27 training samples per fold in 3-fold CV across approximately 50 GAIA-labeled trajectories from AgentErrorBench); GAIA results are treated as preliminary evidence, with ALFWorld (approximately 100 trajectories, ~67 per fold) providing the primary evidence base for the main cascade-avoidance claim. The primary empirical claim is that CascadeWatch achieves task success rate improvement over no-correction baselines on ALFWorld and GAIA while avoiding the performance degradation caused by generic critics (the Intervention Paradox)—demonstrating that cascade-specific precision is sufficient to make rollback net-positive on benchmarks where generic critics fail. The recoverability-delta ablation (embeddings-only vs. recoverability-delta-only vs. combined) serves as an internal validation gate: ≥3% F1 lift from recoverability-delta confirms the ERR-motivated feature design; <3% lift is reported as a negative result. Evaluated on ALFWorld and GAIA as primary benchmarks (WebShop as optional extension), each preceded by the Intervention Paradox's 50-task pilot test to verify net-positive intervention before full evaluation. The compressed HIL execution mode (2 benchmarks, 2K rollouts, 3-fold CV, 2–3 hours/day human engagement) fits within ~50–75 H100-hours and 12–14 calendar days, comfortably within the ≤200 H100-hour and ≤16-day constraints.\",\"project_name\":\"cascade_monitor\",\"source\":\"web_research\"}"
      }
    ],
    "totalDurationMs": 1529087,
    "totalTokens": 80541,
    "totalToolUseCount": 7,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 111,
      "cache_read_input_tokens": 70692,
      "output_tokens": 9737,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 111
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9737,
          "cache_read_input_tokens": 70692,
          "cache_creation_input_tokens": 111,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 111,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 6,
      "editFileCount": 1,
      "linesAdded": 68,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "11efee4e-0a09-48a1-a46b-f7eb3c049f6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "273dc98c-8ab8-4fa8-9d51-65cb993ef786",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Runtime record

_source line 30_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-09 (UTC).**  ## Original idea {   \"title\": \"CascadeWatch: Cascade-Onset Detection with Targeted Rollback for Long-…",
  "leafUuid": "a79e0de5-8d13-4ff1-9a8c-7b5c65e5eab3",
  "sessionId": "273dc98c-8ab8-4fa8-9d51-65cb993ef786"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "ai-title",
  "aiTitle": "Cascade-aware agent rollback with recoverability signals",
  "sessionId": "273dc98c-8ab8-4fa8-9d51-65cb993ef786"
}
```

---
