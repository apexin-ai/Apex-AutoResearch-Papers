# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-11 (UTC).** ## Original idea { "tit

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-2/3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c.jsonl`
- **Structured JSON:** [`3dd062e022a0b3d0432c.json`](../../sessions/3d/3dd062e022a0b3d0432c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-11T23:28:34.475Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-11T23:28:34.475Z",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-11 (UTC).**\n\n## Original idea\n{\n  \"title\": \"Error-Type-Conditioned Branching GRPO for Self-Supervised Agent Recovery\",\n  \"core_problem\": \"When tool-use agents encounter environment errors (API failures, timeouts, parameter mismatches, format violations), they must adapt mid-trajectory to recover. Two active research lines address related problems but leave a gap at their intersection. Error recovery training (PALADIN, ICLR 2026; 'Failure Makes Agent Stronger', arXiv:2509.18847) has demonstrated that recovery is learnable, but both require expensive annotation: PALADIN uses GPT-5 API calls across 50K+ trajectories, while 'Failure Makes Agent Stronger' relies on synthetic error perturbations with ~18 person-days of human annotation and explicit reflection supervision via DAPO+GSPO. Branching-augmented agentic RL (ARPO, Tree-GRPO, AT²PO, InfoTree) has shown that branching at critical decision points with GRPO improves general agent performance, but none target recovery behavior, measure recovery metrics, or condition branching budgets on error semantics. Can error-type-conditioned branching GRPO, where the branching trigger and budget allocation are both determined by the error taxonomy, train effective recovery behavior without curated demonstrations—and does error-type conditioning provide meaningful improvement over type-agnostic branching?\",\n  \"opportunity\": \"A clear methodological gap exists: no existing method combines error-type-aware branching with GRPO for self-supervised recovery training. This gap bridges three dimensions simultaneously. (1) Annotation cost: PALADIN requires GPT-5 demonstrations; 'Failure Makes Agent Stronger' requires synthetic error generation plus human annotation (~18 person-days for 5K trajectories); our approach uses naturally-occurring environment errors (zero annotation cost). (2) Branching trigger design: ARPO uses entropy (may indicate lexical uncertainty without behavioral significance), AT²PO uses turn-level entropy (better but still not recovery-aligned), InfoTree uses submodular entropy-based budget allocation (principled but domain-agnostic), Tree-GRPO uses uniform expansion (no selectivity); our approach uses error observation points, which are free (environment-emitted), unambiguous (the agent must change strategy), and directly aligned with the recovery objective. (3) Error-type conditioning: no prior branching method conditions budget allocation on the semantic type of the decision point. Different error types (API timeout vs. parameter mismatch vs. format error) have different recovery difficulty profiles and require different amounts of exploration. Error-type-conditioned budget allocation—allocating more branches to harder-to-recover error categories—is a principled extension that none of ARPO, Tree-GRPO, AT²PO, or InfoTree implement, because their branching triggers (entropy, uniform) lack the discrete categorical structure that error types provide.\",\n  \"landscape\": \"PALADIN (ICLR 2026, arXiv:2509.25238) trains recovery via SFT on 50K+ trajectories with GPT-5-generated recovery demonstrations across 7 error categories from ToolScan's taxonomy, achieving 89.68% recovery rate—but depends on expensive API-based annotation. 'Failure Makes Agent Stronger' (arXiv:2509.18847) proposes structured reflection (Reflect→Call→Final) with DAPO+GSPO training on synthetic error perturbations (call-order swap, redundant call, missing call, argument error), achieving large gains on BFCL v3 multi-turn and Tool-Reflection-Bench—but requires synthetic error generation, human annotation (~18 person-days), and explicit reflection supervision, rather than self-supervised RL from real environment errors. ARPO (ICLR 2026, arXiv:2507.19849) introduces entropy-triggered adaptive branching at tool-call steps for general agent training across 13 benchmarks—but does not target error recovery or measure recovery metrics. Tree-GRPO (ICLR 2026, arXiv:2509.21240) establishes that intra-tree GRPO is equivalent to step-level DPO, using uniform tree expansion for sample-efficient agentic RL—but uses uniform expansion without recovery-specific triggers. AT²PO (arXiv:2601.04767) introduces entropy-guided turn-level tree expansion with turn-wise credit assignment, evaluated on 7 search benchmarks (HotpotQA, MuSiQue, etc.) with Qwen3-8B/4B—conceptually close to our branching approach but uses entropy triggers and targets search, not recovery. A²TGPO (arXiv:2605.06200, concurrent) improves on AT²PO with turn-group normalization and variance-rescaled advantage accumulation—addresses turn-level optimization challenges but remains in the general search domain. InfoTree (arXiv:2605.05262, concurrent) formalizes rollout budget allocation via submodular optimization with learned Adaptive Budget Allocator across 9 benchmarks—principled budget allocation but entropy-based and domain-agnostic, not error-type-conditioned. HiPER (arXiv:2602.16165) achieves 97.4% on ALFWorld and 83.3% on WebShop via hierarchical plan-execute RL with hierarchical advantage estimation—near-saturates ALFWorld, motivating our focus on StableToolBench where recovery metrics are less saturated. AgentHER (arXiv:2603.21357) converts failed trajectories into training data via hindsight relabeling, achieving +7-12pp over success-only SFT on WebArena and ToolBench—a natural SFT baseline for comparison with our RL approach. Agent-RLVR (arXiv:2506.11425) uses environment test-pass/fail signals for RL training of SWE agents (22.4% pass@1 on SWE-Bench Verified)—validates the paradigm of environment-signal-driven RL but targets code, not tool-use recovery. iStar (ICLR 2026, arXiv:2509.19199) derives implicit step rewards via trajectory-based DPO—occupies the step-level DPO space without error-specific focus. EPO (EMNLP 2024, arXiv:2408.16090) generates trajectory-level preference pairs via a trained reward model—differs by operating at trajectory-level with a separate reward model. ERR Measure (arXiv:2601.22352) formalizes recoverability via Expected Recovery Regret, providing a quantitative law of recovery dynamics—we adopt their recovery metrics framework. SIGHT (arXiv:2602.11551) uses information-gain branching for search agents. Spark (arXiv:2601.20209) applies policy-aware dynamic branching for embodied planning. StepPO (arXiv:2604.18401) and RTMC (arXiv:2604.11037) propose step-level credit assignment for agentic RL. Agent-R (arXiv:2501.11425) uses MCTS for revision. BranPO (arXiv:2602.03719) applies contrastive dynamic branch sampling. CLEANER (arXiv:2601.15141) replaces failed tool calls with self-corrections but discards error context. Co-Evolving Agents (arXiv:2511.22254) trains auxiliary failure agents for hard negatives. RLAnything/DemyAgent (ICML 2026) provides general agentic RL recipes with GRPO-TCR. The specific intersection of error-type-conditioned branching with GRPO for self-supervised recovery training—combining error-type-aware budget allocation (absent from all branching methods), environment-error triggers (absent from entropy-based methods), and self-supervised RL (absent from annotation-dependent recovery methods)—remains unoccupied.\",\n  \"approach\": \"We propose Error-Type-Conditioned Branching GRPO (ETC-GRPO), which bridges the gap between recovery training and branching RL with a methodologically deeper contribution than branching trigger selection alone. The method has three components:\\n\\n(1) Error-Triggered Branching with Type-Conditioned Budget Allocation: Given a policy model (Qwen3-8B), we collect trajectories on StableToolBench, automatically detect error observation points where the environment emits failure signals, and classify each error into one of ToolScan's categories (API timeout, parameter mismatch, format error, authentication failure, missing function, etc.) using rule-based parsing of environment return codes and error messages. Crucially, we allocate the branching budget K_τ per error type τ proportional to recovery difficulty: K_τ = round(K_base · (1 - RR_pilot(τ)) / Z), where RR_pilot(τ) is the recovery rate for error type τ estimated from a small pilot run (500 trajectories), and Z is a normalization constant ensuring total budget remains within bounds. Harder-to-recover error types receive more alternative continuations, concentrating exploration where it is most needed. This error-type conditioning is the key methodological contribution absent from all prior branching methods (ARPO, Tree-GRPO, AT²PO, InfoTree), which use domain-agnostic triggers (entropy, uniform, submodular) that lack the categorical structure to support type-conditioned allocation.\\n\\n(2) Error-Type-Stratified GRPO: Within each error point's rollout group, we compute group-relative advantages using downstream task success as the binary reward signal. However, unlike standard GRPO which normalizes advantages within each branching group independently, we introduce error-type stratification: advantages are z-score normalized within (error_type, task_difficulty) strata before aggregation. This prevents easy-to-recover error types (e.g., simple format errors) from dominating the advantage signal over hard-to-recover types (e.g., multi-step API failures), ensuring balanced gradient contributions across the error taxonomy. We fine-tune with LoRA-GRPO for 1 iterative round.\\n\\n(3) Systematic Branching Trigger and Budget Comparison: As a central empirical contribution, we compare: (a) error-triggered branching with type-conditioned budget (ETC-GRPO, ours), (b) error-triggered branching with uniform budget (ETB-GRPO, ablation), (c) entropy-triggered branching (AT²PO-style, branching at high-entropy post-tool-call turns), (d) random branching (uniform random turn selection), (e) no branching baseline (standard GRPO on full trajectories), and (f) AgentHER (SFT on hindsight-relabeled failed trajectories, representing the SFT paradigm). All methods are evaluated on recovery-specific metrics: Recovery Rate (RR), Post-Error Task Success Rate (PE-TSR), and Recovery Efficiency (steps-to-recover), following the ERR measure framework. Error-type-stratified analysis reveals which recovery behaviors benefit most from RL-based branching vs. SFT-based relabeling, providing actionable guidance.\\n\\nThis is distinguished from 'Failure Makes Agent Stronger' (synthetic errors + DAPO/GSPO + explicit reflection supervision + human annotation) by using real environment errors with self-supervised GRPO and no annotation; from AT²PO/InfoTree (entropy-based, search-focused, domain-agnostic budget) by error-type-conditioned, recovery-focused design; from PALADIN (SFT with GPT-5) by self-supervised RL; from AgentHER (SFT with hindsight relabeling) by RL-based recovery training.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~130h H100-80GB (trajectory collection on StableToolBench ~15h, pilot run for recovery difficulty estimation ~5h, error-triggered branching rollouts with type-conditioned K ~20h, baseline rollouts: entropy+random+no-branch ~20h, AgentHER SFT baseline ~5h, GRPO LoRA training: ETC-GRPO + ETB-GRPO ablation ~15h, evaluation on recovery metrics ~10h, error-type analysis ~5h, debugging buffer ~35h)\",\n      \"gpu_utilization\": \"~55% — GPUs wait while researchers validate error detection rules and analyze pilot recovery difficulty estimates\",\n      \"timeline\": \"14 days (extremely tight, feasible only with pre-existing infrastructure and full-time execution)\",\n      \"team\": \"1-2 researchers working full-time\",\n      \"estimated_gpu_cost\": \"$390 (at ~$3.00/hr H100)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~120h H100-80GB (same breakdown but ~10h saved via automated pilot analysis and error detection validation)\",\n      \"gpu_utilization\": \"~70% — agent handles rollout orchestration, pilot analysis, and training loops; human reviews error classification accuracy and validates recovery difficulty estimates\",\n      \"timeline\": \"12-14 days\",\n      \"team\": \"1 researcher, ~2hr/day for error taxonomy review, pilot analysis validation, and paper writing\",\n      \"claude_api_cost\": \"$80-120 (~600-900 turns for pipeline orchestration and analysis)\",\n      \"estimated_gpu_cost\": \"$360 (at ~$3.00/hr H100)\",\n      \"risk_note\": \"Error detection heuristics need validation against StableToolBench's virtual API server error patterns; some rare error types may produce too few branching opportunities for stable per-type GRPO signal\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~150h H100-80GB (adds second GRPO iteration ~15h, extended error-type analysis with bootstrap confidence intervals ~10h, on top of base ~125h)\",\n      \"gpu_utilization\": \"~85% — continuous job submission across trajectory collection, branching rollouts, and training\",\n      \"timeline\": \"10-12 days with 2-4 parallel H100 GPUs\",\n      \"team\": \"0 (1-2 hour initial setup for StableToolBench environment deployment and error detection rule configuration)\",\n      \"claude_api_cost\": \"$120-200 (~1200-2000 turns for full pipeline orchestration and paper drafting)\",\n      \"estimated_gpu_cost\": \"$450 (at ~$3.00/hr H100)\",\n      \"speed_bottleneck\": \"StableToolBench virtual API server throughput limits concurrent rollouts; error-type-conditioned branching requires sequential pilot→allocation→rollout stages\",\n      \"risk_note\": \"Automated error classification may produce noisy type assignments without human quality gates; rare error types may lack statistical power for per-type analysis\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 (ARR May 25, 2026 — primary and only target, 14 days available, short paper 4 pages + unlimited references; binding conference selection at submission)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"PALADIN: Self-Correcting Language Model Agents to Cure Tool-Failure Cases (ICLR 2026, arXiv:2509.25238)\",\n    \"Failure Makes the Agent Stronger: Structured Reflection for Reliable Tool Interactions (arXiv:2509.18847)\",\n    \"Agentic Reinforced Policy Optimization / ARPO (ICLR 2026, arXiv:2507.19849)\",\n    \"Tree Search for LLM Agent Reinforcement Learning / Tree-GRPO (ICLR 2026, arXiv:2509.21240)\",\n    \"AT²PO: Agentic Turn-based Policy Optimization via Tree Search (arXiv:2601.04767)\",\n    \"A²TGPO: Agentic Turn-Group Policy Optimization with Adaptive Turn-level Clipping (arXiv:2605.06200)\",\n    \"InfoTree: Maximizing Rollout Informativeness under a Fixed Budget via Submodular Tree Search (arXiv:2605.05262)\",\n    \"HiPER: Hierarchical RL with Explicit Credit Assignment for LLM Agents (arXiv:2602.16165)\",\n    \"AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling (arXiv:2603.21357)\",\n    \"Agent-RLVR: Training Software Engineering Agents via Guidance and Environment Rewards (arXiv:2506.11425)\",\n    \"Recoverability Has a Law: The ERR Measure for Tool-Augmented Agents (arXiv:2601.22352)\",\n    \"Agentic Reinforcement Learning with Implicit Step Rewards / iStar (ICLR 2026, arXiv:2509.19199)\",\n    \"EPO: Hierarchical LLM Agents with Environment Preference Optimization (EMNLP 2024, arXiv:2408.16090)\",\n    \"SIGHT: RL with Self-Evidence and Information-Gain Diverse Branching for Search Agent (arXiv:2602.11551)\",\n    \"Spark: Strategic Policy-Aware Exploration via Dynamic Branching (arXiv:2601.20209)\",\n    \"StepPO: Step-Aligned Policy Optimization for Agentic RL (arXiv:2604.18401)\",\n    \"RTMC: Step-Level Credit Assignment via Rollout Trees (arXiv:2604.11037)\",\n    \"Verified Critical Step Optimization for LLM Agents / CSO (arXiv:2602.03412)\",\n    \"Agent-R: Training Language Model Agents to Reflect via Iterative Self-Training (arXiv:2501.11425)\",\n    \"Training Multi-Turn Search Agent via Contrastive Dynamic Branch Sampling / BranPO (arXiv:2602.03719)\",\n    \"CLEANER: Self-Purified Trajectories Boost Agentic RL (arXiv:2601.15141)\",\n    \"Co-Evolving Agents: Learning from Failures as Hard Negatives (arXiv:2511.22254)\",\n    \"AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling (arXiv:2603.21357)\",\n    \"Where LLM Agents Fail: Error Taxonomy across Modules / ToolScan (arXiv:2509.25370)\",\n    \"RLAnything & DemyAgent: General Agentic RL Algorithms (ICML 2026)\",\n    \"StableToolBench: Towards Stable Large-Scale Benchmarking on Tool Learning (ACL Findings 2024, arXiv:2403.07714)\"\n  ],\n  \"description\": \"Error-Type-Conditioned Branching GRPO (ETC-GRPO) bridges three unconnected threads: error recovery training (PALADIN, 'Failure Makes Agent Stronger'), branching-augmented agentic RL (ARPO, Tree-GRPO, AT²PO, InfoTree), and error-type-aware optimization (absent from all prior work). PALADIN achieves 89.68% recovery via SFT on GPT-5-annotated trajectories; 'Failure Makes Agent Stronger' trains recovery via DAPO+GSPO on synthetic errors with human annotation. Both are effective but expensive. Branching RL methods (ARPO, AT²PO, InfoTree) improve general agent performance via entropy-based branching but none target recovery or condition on error semantics. ETC-GRPO fills this gap with two methodological contributions beyond trigger selection: (1) Error-type-conditioned branching budget allocation, where harder-to-recover error categories receive more alternative continuations (K_τ proportional to 1-RR_pilot(τ)), concentrating exploration where it yields the most recovery learning signal—a categorical conditioning mechanism absent from entropy-based methods (ARPO, AT²PO, InfoTree); (2) Error-type-stratified advantage normalization, preventing easy-to-recover errors from dominating GRPO gradients. At environment error observation points on StableToolBench, the policy (Qwen3-8B) generates type-conditioned alternative continuations via self-rollout, and stratified group-relative advantages form the training signal—entirely self-supervised with zero annotation cost. We systematically compare error-triggered (type-conditioned and uniform) vs. entropy-triggered (AT²PO-style) vs. random branching, and RL-based recovery (ours) vs. SFT-based recovery (AgentHER), evaluated on Recovery Rate, Post-Error Task Success Rate, and Recovery Efficiency following the ERR measure framework. Error-type-stratified analysis reveals which recovery behaviors benefit from RL vs. SFT. ALFWorld is excluded due to near-saturation by HiPER (97.4%). Total compute: ≤150 H100 hours with ~50h margin from 200h budget. Target: EMNLP 2026 short paper (ARR May 25, 2026).\",\n  \"project_name\": \"etb_grpo_recovery\",\n  \"source\": \"web_research\"\n}\n\n## Reviewer feedback (round 3)\nIssues: [\"CRITICAL MISSING WORK — Fission-GRPO (ACL 2026, arXiv:2601.15625): 'Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors' by Zhiwei Zhang et al. This paper DIRECTLY addresses error recovery in tool-use agents via GRPO. It fissions each failed trajectory into new training instances by augmenting with diagnostic feedback from a trained Error Simulator, then resamples G' parallel recovery attempts on-policy — this IS error-triggered branching with GRPO for recovery training. On BFCL v4 Multi-Turn, it improves Qwen3-8B error recovery rate by +5.7% absolute. It distinguishes format errors vs. semantic errors. This was published Jan 2026 and accepted at ACL 2026. ETC-GRPO's core claim of being the first to combine error-triggered branching with GRPO for self-supervised recovery is invalidated by this paper. The generator MUST cite, compare, and differentiate.\", \"CRITICAL MISSING WORK — Stratified GRPO (arXiv:2510.06214, Oct 2025): 'Stratified GRPO: Handling Structural Heterogeneity in Reinforcement Learning of LLM Search Agents' proposes Stratified Advantage Normalization (SAN), which partitions trajectories into homogeneous strata and computes advantages locally within each stratum. While it uses search-structure-based strata (not error-type-based), the conceptual innovation of stratified advantage normalization within GRPO is NOT novel to ETC-GRPO. The generator claims 'error-type-stratified advantage normalization' as a contribution, but the general mechanism of stratifying GRPO advantages by categorical structure already exists.\", \"STABLETOOLBENCH ERROR DIVERSITY CONCERN: StableToolBench's virtual API server was designed to improve stability by caching responses and using GPT-4-turbo simulation when real APIs fail. Only 44.4% of API calls were successful in original ToolBench — but StableToolBench specifically addresses this. The generator assumes abundant naturally-occurring errors across ToolScan's categories, but the virtual server may produce fewer and less diverse errors than assumed. The pilot run (500 trajectories) to estimate per-type recovery difficulty may yield insufficient samples for rare error types (e.g., authentication failures), making the budget allocation K_τ estimates unstable.\", \"NOVELTY NARROWING AFTER FISSION-GRPO: With Fission-GRPO already occupying 'error-triggered GRPO for recovery,' and Stratified GRPO occupying 'stratified advantage normalization,' ETC-GRPO's unique contribution reduces to: (a) error-TYPE-conditioned budget allocation (K_τ ∝ 1-RR_pilot(τ)), and (b) applying this in a recovery-training context with ToolScan's taxonomy. This is a valid but narrow contribution — essentially an adaptive budget scheduling heuristic conditioned on error category difficulty. For EMNLP short paper it may suffice, but the paper must honestly position itself as building on Fission-GRPO's foundation rather than claiming the entire error-triggered-branching-GRPO intersection.\", \"MISSING WORK — CoBA-RL (arXiv:2602.03048): Capability-Oriented Budget Allocation for RL in LLMs proposes adaptive rollout budget allocation based on task difficulty, using a Beta distribution to self-calibrate exploration vs. exploitation. While targeting reasoning rather than agent recovery, the budget allocation mechanism (more compute for harder tasks) is conceptually parallel to ETC-GRPO's K_τ ∝ 1-RR_pilot(τ). Should be cited.\", \"MISSING WORK — RC-GRPO (arXiv:2602.03025): Reward-Conditioned GRPO for Multi-Turn Tool Calling addresses the problem of low reward variation within GRPO groups via reward-conditioned trajectory generation — relevant to the GRPO training dynamics ETC-GRPO must handle.\", \"TIMELINE RISK: 14 days for: (1) StableToolBench environment setup, (2) pilot run (500 trajectories), (3) error classification rule development and validation, (4) type-conditioned branching rollouts, (5) 4 comparison methods (entropy/random/uniform/no-branch), (6) AgentHER SFT baseline, (7) GRPO training for ETC-GRPO + ETB-GRPO ablation, (8) evaluation on 3 recovery metrics, (9) error-type-stratified analysis, (10) paper writing (4 pages short). This is feasible only if StableToolBench infrastructure is already deployed and error detection rules work on first attempt.\"]\nFeedback: Round 3 shows significant improvement in scope (single benchmark, short paper target, systematic comparison), but the discovery of Fission-GRPO (ACL 2026) fundamentally changes the novelty landscape. To salvage this idea:\n\n1. **MANDATORY: Cite and position against Fission-GRPO**: This is non-negotiable. Fission-GRPO does error-triggered GRPO resampling for recovery. ETC-GRPO must be positioned as an extension that adds (a) error-TYPE conditioning on branching budget and (b) error-type-stratified advantage normalization. Acknowledge that Fission-GRPO establishes the error-triggered-GRPO-for-recovery paradigm; your contribution is principled error-type conditioning.\n\n2. **MANDATORY: Cite Stratified GRPO**: Acknowledge that stratified advantage normalization exists for search agents (structure-based strata) and position your error-type strata as a domain-specific instantiation with theoretical motivation (different error types have different recovery difficulty distributions).\n\n3. **Sharpen the contribution around error-type conditioning**: The unique value after accounting for Fission-GRPO + Stratified GRPO is: (a) error-type-conditioned budget allocation (K_τ formula), (b) error-type-stratified advantages in recovery context, (c) systematic analysis showing WHICH error types benefit from RL branching vs. SFT relabeling. Lean heavily into (c) — the per-type analysis is the most novel empirical contribution.\n\n4. **Add Fission-GRPO as a baseline**: Replace one of the weaker baselines (random branching) with Fission-GRPO, or at minimum discuss it as concurrent work you cannot reproduce. If you can reproduce it (code may be available given ACL 2026 acceptance), it becomes the strongest baseline.\n\n5. **Address StableToolBench error diversity**: Run a quick feasibility check: how many distinct error types actually occur with Qwen3-8B on StableToolBench? If fewer than 3 types occur with >100 instances each, the per-type analysis lacks statistical power. Consider augmenting with deliberate API server configuration to increase error diversity, or switch to a benchmark with richer natural error distributions.\n\n6. **Cite CoBA-RL for budget allocation precedent**: The difficulty-proportional budget allocation idea (more resources for harder problems) already exists in CoBA-RL and Knapsack RL (ICLR 2026). Position K_τ as applying this principle to error-type-level difficulty rather than instance-level difficulty.\n\n7. **Reframe as 'Error-Type-Aware Agentic RL' study**: The strongest version of this paper is a short empirical study asking: 'Does error-type conditioning improve branching RL for agent recovery?' with Fission-GRPO as the unconditioned baseline. This is honest, novel enough for a short paper, and avoids overclaiming.\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method (approach / resource_estimate / key_references). Do not jump straight to fixing the method if the underlying problem framing needs correction.\n- Address each issue specifically.\n\n## 深度调研要求（每一轮修订都必须执行）\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化这个 idea 的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，建议用 2-3 种不同的搜索查询调研。\n   - 搜索最新的相关论文（arXiv, conference proceedings）\n   - 搜索 benchmark/leaderboard 确认当前 SOTA\n   - 搜索可能遗漏的相关工作和 concurrent work\n\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文的 abstract 和方法部分，\n   不要只依赖搜索摘要。形成你自己对领域现状的独立判断。\n\n3. **深度思考**：在修订之前，先独立思考以下问题：\n   - 这个 idea 的核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach 来解决同一个核心问题？\n   - 修订后的 idea 相比上一版有什么本质性的改进？\n\n4. **避免表面修订**：如果你发现自己只是在换措辞或补充细节而没有实质改进，\n   考虑是否需要 major revision 或 pivot。反复的 minor fix 不会拯救一个根基有问题的 idea。\n\n## 针对 Review 意见的定向搜索\n\n对 reviewer 指出的每个问题，执行以下搜索流程：\n\n1. **如果 reviewer 说'已有类似工作'**：\n   - 搜索 reviewer 提到的论文，用 WebFetch 实际阅读\n   - 搜索该论文的 cited-by，找到后续跟进工作\n   - 明确你的 idea 与这些工作的差异化点——如果差异化不够，必须 pivot\n\n2. **如果 reviewer 说'SOTA 过时'**：\n   - 用 Papers With Code 查看当前排行榜\n   - 搜索过去 6 个月的最新方法\n   - 更新你的 landscape 和 baseline\n\n3. **如果 reviewer 说'可行性有问题'**：\n   - 搜索类似规模实验的实际成本和时间线\n   - 搜索 GitHub 上是否有可复用的实现\n   - 搜索相关数据集/模型的可获取性\n\n4. **如果 reviewer 说'novelty 不足'**：\n   - 对核心方法尽量做 3-5 种不同关键词组合的搜索\n   - 搜索相邻领域是否有类似思路\n   - 如果确实 novelty 不足，考虑 major revision 或 pivot\n\n- Use WebSearch to find updated information if the reviewer flagged outdated claims.\n- You have full freedom in how much to change:\n  - Minor fix: if only specific details are wrong, correct them and keep everything else.\n  - Major revision: if the approach is fundamentally flawed but the core problem is valid, you may redesign the approach entirely.\n  - Pivot: if the reviewer's feedback reveals that the core problem itself is invalid (e.g., the gap no longer exists), you may propose a RELATED but substantially different idea that builds on the same research area. This is preferred over forcing a doomed idea to pass review.\n- The output replaces the original idea (same tracking ID). Whether you make a small tweak or a full pivot, output a COMPLETE JSON object with ALL fields filled.\n- In the output JSON, include a \"change_type\" field with one of: \"minor\", \"major\", or \"pivot\" to indicate the scope of your changes.\n- Output the revised idea as a COMPLETE JSON object (same schema as original, plus \"change_type\")."
}
```

---

### Runtime record

_source line 2 · 2026-05-11T23:28:34.479Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-11T23:28:34.479Z",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c"
}
```

---

## Round 1

35 recorded events

### User

_source line 3 · 2026-05-11T23:28:34.514Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-11 (UTC).**

## Original idea
{
  "title": "Error-Type-Conditioned Branching GRPO for Self-Supervised Agent Recovery",
  "core_problem": "When tool-use agents encounter environment errors (API failures, timeouts, parameter mismatches, format violations), they must adapt mid-trajectory to recover. Two active research lines address related problems but leave a gap at their intersection. Error recovery training (PALADIN, ICLR 2026; 'Failure Makes Agent Stronger', arXiv:2509.18847) has demonstrated that recovery is learnable, but both require expensive annotation: PALADIN uses GPT-5 API calls across 50K+ trajectories, while 'Failure Makes Agent Stronger' relies on synthetic error perturbations with ~18 person-days of human annotation and explicit reflection supervision via DAPO+GSPO. Branching-augmented agentic RL (ARPO, Tree-GRPO, AT²PO, InfoTree) has shown that branching at critical decision points with GRPO improves general agent performance, but none target recovery behavior, measure recovery metrics, or condition branching budgets on error semantics. Can error-type-conditioned branching GRPO, where the branching trigger and budget allocation are both determined by the error taxonomy, train effective recovery behavior without curated demonstrations—and does error-type conditioning provide meaningful improvement over type-agnostic branching?",
  "opportunity": "A clear methodological gap exists: no existing method combines error-type-aware branching with GRPO for self-supervised recovery training. This gap bridges three dimensions simultaneously. (1) Annotation cost: PALADIN requires GPT-5 demonstrations; 'Failure Makes Agent Stronger' requires synthetic error generation plus human annotation (~18 person-days for 5K trajectories); our approach uses naturally-occurring environment errors (zero annotation cost). (2) Branching trigger design: ARPO uses entropy (may indicate lexical uncertainty without behavioral significance), AT²PO uses turn-level entropy (better but still not recovery-aligned), InfoTree uses submodular entropy-based budget allocation (principled but domain-agnostic), Tree-GRPO uses uniform expansion (no selectivity); our approach uses error observation points, which are free (environment-emitted), unambiguous (the agent must change strategy), and directly aligned with the recovery objective. (3) Error-type conditioning: no prior branching method conditions budget allocation on the semantic type of the decision point. Different error types (API timeout vs. parameter mismatch vs. format error) have different recovery difficulty profiles and require different amounts of exploration. Error-type-conditioned budget allocation—allocating more branches to harder-to-recover error categories—is a principled extension that none of ARPO, Tree-GRPO, AT²PO, or InfoTree implement, because their branching triggers (entropy, uniform) lack the discrete categorical structure that error types provide.",
  "landscape": "PALADIN (ICLR 2026, arXiv:2509.25238) trains recovery via SFT on 50K+ trajectories with GPT-5-generated recovery demonstrations across 7 error categories from ToolScan's taxonomy, achieving 89.68% recovery rate—but depends on expensive API-based annotation. 'Failure Makes Agent Stronger' (arXiv:2509.18847) proposes structured reflection (Reflect→Call→Final) with DAPO+GSPO training on synthetic error perturbations (call-order swap, redundant call, missing call, argument error), achieving large gains on BFCL v3 multi-turn and Tool-Reflection-Bench—but requires synthetic error generation, human annotation (~18 person-days), and explicit reflection supervision, rather than self-supervised RL from real environment errors. ARPO (ICLR 2026, arXiv:2507.19849) introduces entropy-triggered adaptive branching at tool-call steps for general agent training across 13 benchmarks—but does not target error recovery or measure recovery metrics. Tree-GRPO (ICLR 2026, arXiv:2509.21240) establishes that intra-tree GRPO is equivalent to step-level DPO, using uniform tree expansion for sample-efficient agentic RL—but uses uniform expansion without recovery-specific triggers. AT²PO (arXiv:2601.04767) introduces entropy-guided turn-level tree expansion with turn-wise credit assignment, evaluated on 7 search benchmarks (HotpotQA, MuSiQue, etc.) with Qwen3-8B/4B—conceptually close to our branching approach but uses entropy triggers and targets search, not recovery. A²TGPO (arXiv:2605.06200, concurrent) improves on AT²PO with turn-group normalization and variance-rescaled advantage accumulation—addresses turn-level optimization challenges but remains in the general search domain. InfoTree (arXiv:2605.05262, concurrent) formalizes rollout budget allocation via submodular optimization with learned Adaptive Budget Allocator across 9 benchmarks—principled budget allocation but entropy-based and domain-agnostic, not error-type-conditioned. HiPER (arXiv:2602.16165) achieves 97.4% on ALFWorld and 83.3% on WebShop via hierarchical plan-execute RL with hierarchical advantage estimation—near-saturates ALFWorld, motivating our focus on StableToolBench where recovery metrics are less saturated. AgentHER (arXiv:2603.21357) converts failed trajectories into training data via hindsight relabeling, achieving +7-12pp over success-only SFT on WebArena and ToolBench—a natural SFT baseline for comparison with our RL approach. Agent-RLVR (arXiv:2506.11425) uses environment test-pass/fail signals for RL training of SWE agents (22.4% pass@1 on SWE-Bench Verified)—validates the paradigm of environment-signal-driven RL but targets code, not tool-use recovery. iStar (ICLR 2026, arXiv:2509.19199) derives implicit step rewards via trajectory-based DPO—occupies the step-level DPO space without error-specific focus. EPO (EMNLP 2024, arXiv:2408.16090) generates trajectory-level preference pairs via a trained reward model—differs by operating at trajectory-level with a separate reward model. ERR Measure (arXiv:2601.22352) formalizes recoverability via Expected Recovery Regret, providing a quantitative law of recovery dynamics—we adopt their recovery metrics framework. SIGHT (arXiv:2602.11551) uses information-gain branching for search agents. Spark (arXiv:2601.20209) applies policy-aware dynamic branching for embodied planning. StepPO (arXiv:2604.18401) and RTMC (arXiv:2604.11037) propose step-level credit assignment for agentic RL. Agent-R (arXiv:2501.11425) uses MCTS for revision. BranPO (arXiv:2602.03719) applies contrastive dynamic branch sampling. CLEANER (arXiv:2601.15141) replaces failed tool calls with self-corrections but discards error context. Co-Evolving Agents (arXiv:2511.22254) trains auxiliary failure agents for hard negatives. RLAnything/DemyAgent (ICML 2026) provides general agentic RL recipes with GRPO-TCR. The specific intersection of error-type-conditioned branching with GRPO for self-supervised recovery training—combining error-type-aware budget allocation (absent from all branching methods), environment-error triggers (absent from entropy-based methods), and self-supervised RL (absent from annotation-dependent recovery methods)—remains unoccupied.",
  "approach": "We propose Error-Type-Conditioned Branching GRPO (ETC-GRPO), which bridges the gap between recovery training and branching RL with a methodologically deeper contribution than branching trigger selection alone. The method has three components:\n\n(1) Error-Triggered Branching with Type-Conditioned Budget Allocation: Given a policy model (Qwen3-8B), we collect trajectories on StableToolBench, automatically detect error observation points where the environment emits failure signals, and classify each error into one of ToolScan's categories (API timeout, parameter mismatch, format error, authentication failure, missing function, etc.) using rule-based parsing of environment return codes and error messages. Crucially, we allocate the branching budget K_τ per error type τ proportional to recovery difficulty: K_τ = round(K_base · (1 - RR_pilot(τ)) / Z), where RR_pilot(τ) is the recovery rate for error type τ estimated from a small pilot run (500 trajectories), and Z is a normalization constant ensuring total budget remains within bounds. Harder-to-recover error types receive more alternative continuations, concentrating exploration where it is most needed. This error-type conditioning is the key methodological contribution absent from all prior branching methods (ARPO, Tree-GRPO, AT²PO, InfoTree), which use domain-agnostic triggers (entropy, uniform, submodular) that lack the categorical structure to support type-conditioned allocation.\n\n(2) Error-Type-Stratified GRPO: Within each error point's rollout group, we compute group-relative advantages using downstream task success as the binary reward signal. However, unlike standard GRPO which normalizes advantages within each branching group independently, we introduce error-type stratification: advantages are z-score normalized within (error_type, task_difficulty) strata before aggregation. This prevents easy-to-recover error types (e.g., simple format errors) from dominating the advantage signal over hard-to-recover types (e.g., multi-step API failures), ensuring balanced gradient contributions across the error taxonomy. We fine-tune with LoRA-GRPO for 1 iterative round.\n\n(3) Systematic Branching Trigger and Budget Comparison: As a central empirical contribution, we compare: (a) error-triggered branching with type-conditioned budget (ETC-GRPO, ours), (b) error-triggered branching with uniform budget (ETB-GRPO, ablation), (c) entropy-triggered branching (AT²PO-style, branching at high-entropy post-tool-call turns), (d) random branching (uniform random turn selection), (e) no branching baseline (standard GRPO on full trajectories), and (f) AgentHER (SFT on hindsight-relabeled failed trajectories, representing the SFT paradigm). All methods are evaluated on recovery-specific metrics: Recovery Rate (RR), Post-Error Task Success Rate (PE-TSR), and Recovery Efficiency (steps-to-recover), following the ERR measure framework. Error-type-stratified analysis reveals which recovery behaviors benefit most from RL-based branching vs. SFT-based relabeling, providing actionable guidance.\n\nThis is distinguished from 'Failure Makes Agent Stronger' (synthetic errors + DAPO/GSPO + explicit reflection supervision + human annotation) by using real environment errors with self-supervised GRPO and no annotation; from AT²PO/InfoTree (entropy-based, search-focused, domain-agnostic budget) by error-type-conditioned, recovery-focused design; from PALADIN (SFT with GPT-5) by self-supervised RL; from AgentHER (SFT with hindsight relabeling) by RL-based recovery training.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~130h H100-80GB (trajectory collection on StableToolBench ~15h, pilot run for recovery difficulty estimation ~5h, error-triggered branching rollouts with type-conditioned K ~20h, baseline rollouts: entropy+random+no-branch ~20h, AgentHER SFT baseline ~5h, GRPO LoRA training: ETC-GRPO + ETB-GRPO ablation ~15h, evaluation on recovery metrics ~10h, error-type analysis ~5h, debugging buffer ~35h)",
      "gpu_utilization": "~55% — GPUs wait while researchers validate error detection rules and analyze pilot recovery difficulty estimates",
      "timeline": "14 days (extremely tight, feasible only with pre-existing infrastructure and full-time execution)",
      "team": "1-2 researchers working full-time",
      "estimated_gpu_cost": "$390 (at ~$3.00/hr H100)"
    },
    "human_in_loop": {
      "gpu_hours": "~120h H100-80GB (same breakdown but ~10h saved via automated pilot analysis and error detection validation)",
      "gpu_utilization": "~70% — agent handles rollout orchestration, pilot analysis, and training loops; human reviews error classification accuracy and validates recovery difficulty estimates",
      "timeline": "12-14 days",
      "team": "1 researcher, ~2hr/day for error taxonomy review, pilot analysis validation, and paper writing",
      "claude_api_cost": "$80-120 (~600-900 turns for pipeline orchestration and analysis)",
      "estimated_gpu_cost": "$360 (at ~$3.00/hr H100)",
      "risk_note": "Error detection heuristics need validation against StableToolBench's virtual API server error patterns; some rare error types may produce too few branching opportunities for stable per-type GRPO signal"
    },
    "auto_research": {
      "gpu_hours": "~150h H100-80GB (adds second GRPO iteration ~15h, extended error-type analysis with bootstrap confidence intervals ~10h, on top of base ~125h)",
      "gpu_utilization": "~85% — continuous job submission across trajectory collection, branching rollouts, and training",
      "timeline": "10-12 days with 2-4 parallel H100 GPUs",
      "team": "0 (1-2 hour initial setup for StableToolBench environment deployment and error detection rule configuration)",
      "claude_api_cost": "$120-200 (~1200-2000 turns for full pipeline orchestration and paper drafting)",
      "estimated_gpu_cost": "$450 (at ~$3.00/hr H100)",
      "speed_bottleneck": "StableToolBench virtual API server throughput limits concurrent rollouts; error-type-conditioned branching requires sequential pilot→allocation→rollout stages",
      "risk_note": "Automated error classification may produce noisy type assignments without human quality gates; rare error types may lack statistical power for per-type analysis"
    }
  },
  "target_venues": [
    "EMNLP 2026 (ARR May 25, 2026 — primary and only target, 14 days available, short paper 4 pages + unlimited references; binding conference selection at submission)"
  ],
  "level": "solid",
  "key_references": [
    "PALADIN: Self-Correcting Language Model Agents to Cure Tool-Failure Cases (ICLR 2026, arXiv:2509.25238)",
    "Failure Makes the Agent Stronger: Structured Reflection for Reliable Tool Interactions (arXiv:2509.18847)",
    "Agentic Reinforced Policy Optimization / ARPO (ICLR 2026, arXiv:2507.19849)",
    "Tree Search for LLM Agent Reinforcement Learning / Tree-GRPO (ICLR 2026, arXiv:2509.21240)",
    "AT²PO: Agentic Turn-based Policy Optimization via Tree Search (arXiv:2601.04767)",
    "A²TGPO: Agentic Turn-Group Policy Optimization with Adaptive Turn-level Clipping (arXiv:2605.06200)",
    "InfoTree: Maximizing Rollout Informativeness under a Fixed Budget via Submodular Tree Search (arXiv:2605.05262)",
    "HiPER: Hierarchical RL with Explicit Credit Assignment for LLM Agents (arXiv:2602.16165)",
    "AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling (arXiv:2603.21357)",
    "Agent-RLVR: Training Software Engineering Agents via Guidance and Environment Rewards (arXiv:2506.11425)",
    "Recoverability Has a Law: The ERR Measure for Tool-Augmented Agents (arXiv:2601.22352)",
    "Agentic Reinforcement Learning with Implicit Step Rewards / iStar (ICLR 2026, arXiv:2509.19199)",
    "EPO: Hierarchical LLM Agents with Environment Preference Optimization (EMNLP 2024, arXiv:2408.16090)",
    "SIGHT: RL with Self-Evidence and Information-Gain Diverse Branching for Search Agent (arXiv:2602.11551)",
    "Spark: Strategic Policy-Aware Exploration via Dynamic Branching (arXiv:2601.20209)",
    "StepPO: Step-Aligned Policy Optimization for Agentic RL (arXiv:2604.18401)",
    "RTMC: Step-Level Credit Assignment via Rollout Trees (arXiv:2604.11037)",
    "Verified Critical Step Optimization for LLM Agents / CSO (arXiv:2602.03412)",
    "Agent-R: Training Language Model Agents to Reflect via Iterative Self-Training (arXiv:2501.11425)",
    "Training Multi-Turn Search Agent via Contrastive Dynamic Branch Sampling / BranPO (arXiv:2602.03719)",
    "CLEANER: Self-Purified Trajectories Boost Agentic RL (arXiv:2601.15141)",
    "Co-Evolving Agents: Learning from Failures as Hard Negatives (arXiv:2511.22254)",
    "AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling (arXiv:2603.21357)",
    "Where LLM Agents Fail: Error Taxonomy across Modules / ToolScan (arXiv:2509.25370)",
    "RLAnything & DemyAgent: General Agentic RL Algorithms (ICML 2026)",
    "StableToolBench: Towards Stable Large-Scale Benchmarking on Tool Learning (ACL Findings 2024, arXiv:2403.07714)"
  ],
  "description": "Error-Type-Conditioned Branching GRPO (ETC-GRPO) bridges three unconnected threads: error recovery training (PALADIN, 'Failure Makes Agent Stronger'), branching-augmented agentic RL (ARPO, Tree-GRPO, AT²PO, InfoTree), and error-type-aware optimization (absent from all prior work). PALADIN achieves 89.68% recovery via SFT on GPT-5-annotated trajectories; 'Failure Makes Agent Stronger' trains recovery via DAPO+GSPO on synthetic errors with human annotation. Both are effective but expensive. Branching RL methods (ARPO, AT²PO, InfoTree) improve general agent performance via entropy-based branching but none target recovery or condition on error semantics. ETC-GRPO fills this gap with two methodological contributions beyond trigger selection: (1) Error-type-conditioned branching budget allocation, where harder-to-recover error categories receive more alternative continuations (K_τ proportional to 1-RR_pilot(τ)), concentrating exploration where it yields the most recovery learning signal—a categorical conditioning mechanism absent from entropy-based methods (ARPO, AT²PO, InfoTree); (2) Error-type-stratified advantage normalization, preventing easy-to-recover errors from dominating GRPO gradients. At environment error observation points on StableToolBench, the policy (Qwen3-8B) generates type-conditioned alternative continuations via self-rollout, and stratified group-relative advantages form the training signal—entirely self-supervised with zero annotation cost. We systematically compare error-triggered (type-conditioned and uniform) vs. entropy-triggered (AT²PO-style) vs. random branching, and RL-based recovery (ours) vs. SFT-based recovery (AgentHER), evaluated on Recovery Rate, Post-Error Task Success Rate, and Recovery Efficiency following the ERR measure framework. Error-type-stratified analysis reveals which recovery behaviors benefit from RL vs. SFT. ALFWorld is excluded due to near-saturation by HiPER (97.4%). Total compute: ≤150 H100 hours with ~50h margin from 200h budget. Target: EMNLP 2026 short paper (ARR May 25, 2026).",
  "project_name": "etb_grpo_recovery",
  "source": "web_research"
}

## Reviewer feedback (round 3)
Issues: ["CRITICAL MISSING WORK — Fission-GRPO (ACL 2026, arXiv:2601.15625): 'Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors' by Zhiwei Zhang et al. This paper DIRECTLY addresses error recovery in tool-use agents via GRPO. It fissions each failed trajectory into new training instances by augmenting with diagnostic feedback from a trained Error Simulator, then resamples G' parallel recovery attempts on-policy — this IS error-triggered branching with GRPO for recovery training. On BFCL v4 Multi-Turn, it improves Qwen3-8B error recovery rate by +5.7% absolute. It distinguishes format errors vs. semantic errors. This was published Jan 2026 and accepted at ACL 2026. ETC-GRPO's core claim of being the first to combine error-triggered branching with GRPO for self-supervised recovery is invalidated by this paper. The generator MUST cite, compare, and differentiate.", "CRITICAL MISSING WORK — Stratified GRPO (arXiv:2510.06214, Oct 2025): 'Stratified GRPO: Handling Structural Heterogeneity in Reinforcement Learning of LLM Search Agents' proposes Stratified Advantage Normalization (SAN), which partitions trajectories into homogeneous strata and computes advantages locally within each stratum. While it uses search-structure-based strata (not error-type-based), the conceptual innovation of stratified advantage normalization within GRPO is NOT novel to ETC-GRPO. The generator claims 'error-type-stratified advantage normalization' as a contribution, but the general mechanism of stratifying GRPO advantages by categorical structure already exists.", "STABLETOOLBENCH ERROR DIVERSITY CONCERN: StableToolBench's virtual API server was designed to improve stability by caching responses and using GPT-4-turbo simulation when real APIs fail. Only 44.4% of API calls were successful in original ToolBench — but StableToolBench specifically addresses this. The generator assumes abundant naturally-occurring errors across ToolScan's categories, but the virtual server may produce fewer and less diverse errors than assumed. The pilot run (500 trajectories) to estimate per-type recovery difficulty may yield insufficient samples for rare error types (e.g., authentication failures), making the budget allocation K_τ estimates unstable.", "NOVELTY NARROWING AFTER FISSION-GRPO: With Fission-GRPO already occupying 'error-triggered GRPO for recovery,' and Stratified GRPO occupying 'stratified advantage normalization,' ETC-GRPO's unique contribution reduces to: (a) error-TYPE-conditioned budget allocation (K_τ ∝ 1-RR_pilot(τ)), and (b) applying this in a recovery-training context with ToolScan's taxonomy. This is a valid but narrow contribution — essentially an adaptive budget scheduling heuristic conditioned on error category difficulty. For EMNLP short paper it may suffice, but the paper must honestly position itself as building on Fission-GRPO's foundation rather than claiming the entire error-triggered-branching-GRPO intersection.", "MISSING WORK — CoBA-RL (arXiv:2602.03048): Capability-Oriented Budget Allocation for RL in LLMs proposes adaptive rollout budget allocation based on task difficulty, using a Beta distribution to self-calibrate exploration vs. exploitation. While targeting reasoning rather than agent recovery, the budget allocation mechanism (more compute for harder tasks) is conceptually parallel to ETC-GRPO's K_τ ∝ 1-RR_pilot(τ). Should be cited.", "MISSING WORK — RC-GRPO (arXiv:2602.03025): Reward-Conditioned GRPO for Multi-Turn Tool Calling addresses the problem of low reward variation within GRPO groups via reward-conditioned trajectory generation — relevant to the GRPO training dynamics ETC-GRPO must handle.", "TIMELINE RISK: 14 days for: (1) StableToolBench environment setup, (2) pilot run (500 trajectories), (3) error classification rule development and validation, (4) type-conditioned branching rollouts, (5) 4 comparison methods (entropy/random/uniform/no-branch), (6) AgentHER SFT baseline, (7) GRPO training for ETC-GRPO + ETB-GRPO ablation, (8) evaluation on 3 recovery metrics, (9) error-type-stratified analysis, (10) paper writing (4 pages short). This is feasible only if StableToolBench infrastructure is already deployed and error detection rules work on first attempt."]
Feedback: Round 3 shows significant improvement in scope (single benchmark, short paper target, systematic comparison), but the discovery of Fission-GRPO (ACL 2026) fundamentally changes the novelty landscape. To salvage this idea:

1. **MANDATORY: Cite and position against Fission-GRPO**: This is non-negotiable. Fission-GRPO does error-triggered GRPO resampling for recovery. ETC-GRPO must be positioned as an extension that adds (a) error-TYPE conditioning on branching budget and (b) error-type-stratified advantage normalization. Acknowledge that Fission-GRPO establishes the error-triggered-GRPO-for-recovery paradigm; your contribution is principled error-type conditioning.

2. **MANDATORY: Cite Stratified GRPO**: Acknowledge that stratified advantage normalization exists for search agents (structure-based strata) and position your error-type strata as a domain-specific instantiation with theoretical motivation (different error types have different recovery difficulty distributions).

3. **Sharpen the contribution around error-type conditioning**: The unique value after accounting for Fission-GRPO + Stratified GRPO is: (a) error-type-conditioned budget allocation (K_τ formula), (b) error-type-stratified advantages in recovery context, (c) systematic analysis showing WHICH error types benefit from RL branching vs. SFT relabeling. Lean heavily into (c) — the per-type analysis is the most novel empirical contribution.

4. **Add Fission-GRPO as a baseline**: Replace one of the weaker baselines (random branching) with Fission-GRPO, or at minimum discuss it as concurrent work you cannot reproduce. If you can reproduce it (code may be available given ACL 2026 acceptance), it becomes the strongest baseline.

5. **Address StableToolBench error diversity**: Run a quick feasibility check: how many distinct error types actually occur with Qwen3-8B on StableToolBench? If fewer than 3 types occur with >100 instances each, the per-type analysis lacks statistical power. Consider augmenting with deliberate API server configuration to increase error diversity, or switch to a benchmark with richer natural error distributions.

6. **Cite CoBA-RL for budget allocation precedent**: The difficulty-proportional budget allocation idea (more resources for harder problems) already exists in CoBA-RL and Knapsack RL (ICLR 2026). Position K_τ as applying this principle to error-type-level difficulty rather than instance-level difficulty.

7. **Reframe as 'Error-Type-Aware Agentic RL' study**: The strongest version of this paper is a short empirical study asking: 'Does error-type conditioning improve branching RL for agent recovery?' with Fission-GRPO as the unconditioned baseline. This is honest, novel enough for a short paper, and avoids overclaiming.

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

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "type": "user",
  "uuid": "fd8d67af-4400-4bf2-8767-38cf11a6d19e",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-11T23:28:34.512Z_

```json
{
  "parentUuid": "fd8d67af-4400-4bf2-8767-38cf11a6d19e",
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
  "uuid": "c10b3cab-14e2-4748-ba99-8d37d9e9185d",
  "timestamp": "2026-05-11T23:28:34.512Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-11T23:28:34.512Z_

```json
{
  "parentUuid": "c10b3cab-14e2-4748-ba99-8d37d9e9185d",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "c1276e7b-c4cd-466e-af6e-f0704397f7e0",
  "timestamp": "2026-05-11T23:28:34.512Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-11 (UTC).**  ## Original idea {   \"title\": \"Error-Type-Conditioned Branching GRPO for Self-Supervised Agent Recove…",
  "leafUuid": "c1276e7b-c4cd-466e-af6e-f0704397f7e0",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Error-type-aware branching for agent recovery beyond Fission-GRPO",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c"
}
```

---

### Assistant

_source line 8 · 2026-05-11T23:28:44.207Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the reviewer feedback carefully before diving into research. The key issues are:

1. **Fission-GRPO (ACL 2026)** - directly addresses error recovery via GRPO, invalidating our "first to combine" claim
2. **Stratified GRPO** - stratified advantage normalization already exists
3. **StableToolBench error diversity** - may not have enough natural errors
4. **Novelty narrowing** - after accounting for Fission-GRPO + Stratified GRPO
5. **CoBA-RL** - budget allocation precedent


6. **RC-GRPO** - reward-conditioned GRPO for tool calling
7. **Timeline risk**

I need to search for and read these papers to understand what's already been done, then assess whether the core idea can survive these challenges or if we need to pivot the approach entirely. Let me start with deep research on each of these works.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1276e7b-c4cd-466e-af6e-f0704397f7e0",
  "isSidechain": false,
  "requestId": "req_011Cawed8BdfvtfrLPUeZpYK",
  "type": "assistant",
  "uuid": "6037df6b-0f6c-4072-baa5-f1fdb2a48f92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M8vsWhYsH5Zg57YZKmV7A4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13175,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1849,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13175,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1849,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13175,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13175
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

_source line 9 · 2026-05-11T23:28:44.650Z_

I'll start by researching each paper the reviewer flagged, then reassess the idea's viability before revising. Let me search for all critical missing works in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6037df6b-0f6c-4072-baa5-f1fdb2a48f92",
  "isSidechain": false,
  "requestId": "req_011Cawed8BdfvtfrLPUeZpYK",
  "type": "assistant",
  "uuid": "4fa59af7-8208-42c0-9447-618a61868180",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M8vsWhYsH5Zg57YZKmV7A4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13175,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1849,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13175,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1849,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13175,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13175
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

_source line 10 · 2026-05-11T23:28:53.598Z_

<details open><summary>🔧 Tool call — Agent · `toolu_011fm4rR7nyqy5r5z1p25HX2`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Research Fission-GRPO paper",
  "prompt": "I need to deeply research the paper \"Fission-GRPO\" (arXiv:2601.15625). This is claimed to be an ACL 2026 paper titled \"Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors\" by Zhiwei Zhang et al.\n\nPlease:\n1. Use WebSearch to find this paper with queries like \"Fission-GRPO arXiv 2601.15625\", \"Fission-GRPO error recovery tool use GRPO\", and \"Fission GRPO ACL 2026\"\n2. Use WebFetch to read the actual paper abstract and method sections from arxiv.org\n3. Search for any follow-up work citing Fission-GRPO\n\nI need to understand:\n- What exactly is the \"fission\" mechanism? How does it create new training instances from failed trajectories?\n- What is the \"Error Simulator\" they train?\n- How do they resample G' parallel recovery attempts?\n- What benchmarks do they use? What are their main results?\n- Do they condition on error TYPE? Or just error occurrence?\n- How does their branching differ from tree-based branching (ARPO, Tree-GRPO)?\n- Is their code publicly available?\n\nReport all findings in detail. If the paper doesn't exist at that arXiv ID, report that clearly."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4fa59af7-8208-42c0-9447-618a61868180",
  "isSidechain": false,
  "requestId": "req_011Cawed8BdfvtfrLPUeZpYK",
  "type": "assistant",
  "uuid": "8c0c2de8-fbe8-414c-9e2b-c3ac1c4b153a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M8vsWhYsH5Zg57YZKmV7A4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13175,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1849,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13175,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1849,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13175,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13175
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

_source line 11 · 2026-05-11T23:28:59.348Z_

<details open><summary>🔧 Tool call — Agent · `toolu_0167yVdgUzjjLLASeWMyicvU`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Research Stratified GRPO paper",
  "prompt": "I need to deeply research the paper \"Stratified GRPO\" (arXiv:2510.06214). This is claimed to be titled \"Stratified GRPO: Handling Structural Heterogeneity in Reinforcement Learning of LLM Search Agents\" proposing Stratified Advantage Normalization (SAN).\n\nPlease:\n1. Use WebSearch to find this paper with queries like \"Stratified GRPO arXiv 2510.06214\", \"stratified advantage normalization GRPO\", \"structural heterogeneity reinforcement learning LLM\"\n2. Use WebFetch to read the actual paper abstract and method sections from arxiv.org\n3. Search for follow-up work or related papers on stratified normalization in GRPO\n\nI need to understand:\n- What are the \"strata\" they use? How do they partition trajectories?\n- What is SAN (Stratified Advantage Normalization) exactly?\n- What problem does it solve? Why is within-group normalization insufficient?\n- What benchmarks/tasks do they evaluate on?\n- How is this different from standard GRPO group normalization?\n- Is this published at a venue or just arXiv?\n\nReport all findings in detail. If the paper doesn't exist at that arXiv ID, report that clearly."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c0c2de8-fbe8-414c-9e2b-c3ac1c4b153a",
  "isSidechain": false,
  "requestId": "req_011Cawed8BdfvtfrLPUeZpYK",
  "type": "assistant",
  "uuid": "4bb90586-abf2-4205-977c-dcddc128e16c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M8vsWhYsH5Zg57YZKmV7A4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13175,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1849,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13175,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1849,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13175,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13175
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

_source line 12 · 2026-05-11T23:29:06.639Z_

<details open><summary>🔧 Tool call — Agent · `toolu_019ZJJBUoPg5LQkjmP3fQDXp`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Research CoBA-RL and RC-GRPO",
  "prompt": "I need to research two papers:\n\n1. **CoBA-RL** (arXiv:2602.03048): \"Capability-Oriented Budget Allocation for RL in LLMs\" - proposes adaptive rollout budget allocation based on task difficulty using Beta distribution.\n\n2. **RC-GRPO** (arXiv:2602.03025): \"Reward-Conditioned GRPO for Multi-Turn Tool Calling\" - addresses low reward variation within GRPO groups via reward-conditioned trajectory generation.\n\nFor each paper:\n1. Use WebSearch to find the paper with the arXiv ID and title keywords\n2. Use WebFetch to read the actual abstract and method from arxiv.org\n3. Search for related work on adaptive budget allocation in RL for LLMs\n\nI need to understand:\n- For CoBA-RL: How does the Beta distribution-based budget allocation work? What is \"capability-oriented\"? How does difficulty estimation work? What benchmarks?\n- For RC-GRPO: What is \"reward-conditioned\" trajectory generation? How does it address low reward variation? What benchmarks? Is it specific to tool calling?\n\nAlso search for \"Knapsack RL ICLR 2026\" which is mentioned as another budget allocation method.\n\nReport all findings in detail. If papers don't exist at those IDs, report that clearly."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4bb90586-abf2-4205-977c-dcddc128e16c",
  "isSidechain": false,
  "requestId": "req_011Cawed8BdfvtfrLPUeZpYK",
  "type": "assistant",
  "uuid": "89322e70-78ce-4efc-bf97-4a8ef6c17073",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M8vsWhYsH5Zg57YZKmV7A4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13175,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1849,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13175,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1849,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13175,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13175
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

_source line 13 · 2026-05-11T23:29:13.587Z_

<details open><summary>🔧 Tool call — Agent · `toolu_014WkDQZ8VmPCKLHsU487cAs`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Research StableToolBench error patterns",
  "prompt": "I need to research the actual error patterns and diversity in StableToolBench to assess feasibility of error-type-conditioned training.\n\nPlease:\n1. Use WebSearch with queries like \"StableToolBench error analysis\", \"StableToolBench virtual API server errors\", \"StableToolBench Qwen error types\"\n2. Search for \"StableToolBench GitHub\" to find the actual codebase and check error handling\n3. Use WebFetch to read the StableToolBench paper (arXiv:2403.07714) focusing on their virtual API server design and what kinds of errors occur\n4. Search for papers that evaluate on StableToolBench and report error statistics\n5. Search for \"ToolBench error analysis\" or \"tool-use LLM error distribution\"\n\nI need to understand:\n- What fraction of API calls fail on StableToolBench vs original ToolBench?\n- What types of errors does the virtual API server produce?\n- Does StableToolBench's caching/simulation actually reduce error diversity compared to real APIs?\n- Are there papers reporting per-error-type statistics on StableToolBench?\n- What alternative benchmarks have richer natural error distributions for tool-use agents?\n\nReport all findings in detail."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "89322e70-78ce-4efc-bf97-4a8ef6c17073",
  "isSidechain": false,
  "requestId": "req_011Cawed8BdfvtfrLPUeZpYK",
  "type": "assistant",
  "uuid": "f9cb14f3-f161-40fb-bf78-4d552b1330ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M8vsWhYsH5Zg57YZKmV7A4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13175,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1849,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13175,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1849,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13175,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13175
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

_source line 14 · 2026-05-11T23:31:55.844Z_

<details><summary>↩ Tool result · `toolu_019ZJJBUoPg5LQkjmP3fQDXp`</summary>

```text
I have collected extensive information on all three papers. Here is my comprehensive report.

---

## Detailed Research Report

### 1. CoBA-RL (arXiv:2602.03048)

**Title:** CoBA-RL: Capability-Oriented Budget Allocation for Reinforcement Learning in LLMs

**Authors:** Zhiyuan Yao, Yi-Kai Zhang, Yuxin Chen, Yueqing Sun, Zishan Xu, Yu Yang, Tianhao Hu, Qi Gu, Hui Su, Xunliang Cai

**Submitted:** February 3, 2026 (revised February 6, 2026)

**GitHub:** https://github.com/Within-yao/CoBA-RL

#### Problem
Standard GRPO uses a uniform rollout budget across all tasks, which is wasteful: easy tasks always succeed and hard tasks always fail, both producing zero gradients. Existing adaptive methods rely on instance-level metrics like pass rates, failing to capture the model's dynamic learning state.

#### How the Beta Distribution-Based Budget Allocation Works
CoBA-RL models task preferences using a Beta distribution with dynamically adjusted parameters. The density function is:

`Density(p_i; alpha_t, beta_t) = p_i^(alpha_t - 1) * (1 - p_i)^(beta_t - 1) / B(alpha_t, beta_t)`

The parameters shift based on a "Global Failure Rate" (F_t), which is the complementary probability of the average success rate across the training batch. As the model's capability evolves, the Beta distribution parameters change, re-weighting which difficulty levels of tasks are prioritized for budget allocation.

#### What "Capability-Oriented" Means
Rather than using static, pre-determined difficulty labels, CoBA-RL uses a "Capability-Oriented Value function" that dynamically maps each task to its potential training gain given the model's *current* ability level. The value function combines two components:

- **Budget Saturation Factor:** `eta(B_i, p_i) = 1 - exp(-B_i / (tau * p_i * (1-p_i)))` -- captures diminishing returns from additional rollouts. Tasks with pass rates near 0.5 (moderate difficulty relative to current capability) get the most benefit.
- **Complete Value Function:** `V(B_i, pi_theta, p_i) = eta(B_i, p_i) * Density(p_i; alpha_t, beta_t)` -- synthesizes budget constraints with the capability-weighted preference density.

The Global Success Rate `S_t = (1/M) * sum(p_i)` serves as the capability metric, with a sigmoid scaling transformation when failure rates fall below 0.5 to maintain sensitivity during later training stages.

#### Heap-Based Greedy Strategy
Instead of expensive dynamic programming (O(M * B_total * (B_up - B_low))), CoBA-RL uses a max-heap of marginal gains. It iteratively: (1) extracts the task with highest marginal gain, (2) allocates one rollout unit, (3) recalculates the marginal gain, (4) reinserts into the heap. This achieves O(B_total * log M) complexity -- approximately 928x speedup over DP in tested configurations.

#### Benchmarks and Results
- **Training data:** DAPO-Math-17K
- **Evaluation:** AIME24, AIME25, AMC23, MATH500, OlympiadBench
- **Models:** Qwen2.5-7B-Instruct, Qwen2.5-7B-Base, Qwen3-4B-Base, Qwen3-1.7B-Base (16-rollout group sizes)
- **Key results (Qwen2.5-7B-Instruct):**
  - AIME25: 18.33% (vs. GRPO 12.71%, Knapsack-RL 15.21%)
  - Average: 46.78% (vs. GRPO 42.24%, Knapsack-RL 45.39%)
  - CoBA-RL outperforms both uniform allocation (+4.54% avg) and static Beta configurations (44.22%-45.21%)

---

### 2. RC-GRPO (arXiv:2602.03025)

**Title:** RC-GRPO: Reward-Conditioned Group Relative Policy Optimization for Multi-Turn Tool Calling Agents

**Authors:** Haitian Zhong, Jixiu Zhai, Lei Song, Jiang Bian, Qiang Liu, Tieniu Tan

**Submitted:** February 3, 2026

#### Problem
Multi-turn tool calling has sparse rewards and expensive exploration. When SFT produces a strong initial policy, GRPO stalls due to the "paradox of perfection": within a group, rollouts tend to all succeed or all fail, collapsing within-group reward variance. The group-normalized advantage becomes uninformative, yielding vanishing gradient updates.

#### What "Reward-Conditioned" Trajectory Generation Means
RC-GRPO treats exploration as a **controllable steering problem** using discrete reward tokens. Two special tokens are defined:
- `<|high_reward|>` -- steers the model toward optimal trajectories
- `<|low_reward|>` -- steers toward failure trajectories

These tokens are prepended to the input, enabling the model to generate systematically different-quality trajectories on demand based on the conditioning signal.

#### How It Addresses Low Reward Variation
The algorithm has two stages:

**Stage 1 -- RCTP Training:** A Reward-Conditioned Trajectory Policy is fine-tuned via supervised learning on 1,600 mixed-quality trajectories (800 expert/success, 800 failure). Each trajectory is paired with the appropriate reward token. The model learns to correlate reward tokens with trajectory quality through maximum likelihood training.

**Stage 2 -- RC-GRPO Training:** During RL, for each member j in a GRPO group, a reward token r_j is sampled from a distribution P_sample(r) (with p=0.5 in their experiments, matching the success/failure ratio in training data). Each rollout is conditioned on its sampled token. This explicitly injects diversity within each group -- some rollouts are steered toward success, others toward failure -- ensuring that within-group reward variance remains high and advantages are informative.

The RL objective uses PPO-style clipped updates with group-relative advantage normalization and KL divergence penalty against the reference policy.

#### Benchmarks and Results
- **Benchmark:** Berkeley Function Calling Leaderboard v4 (BFCLv4), multi-turn subset (200 evaluation trajectories)
- **Models:** Qwen2.5-7B-Instruct, LLaMA-3.1-8B-Instruct
- **Key results:**
  - Qwen2.5-7B: 85.00% (vs. 48.75% for SFT+GRPO baseline)
  - LLaMA-3.1-8B: 48.75% (vs. 35.00% SFT+GRPO baseline)
  - Outperforms even the best API baseline (Opus-4.5 at 61.25%)

#### Scope
The method is specifically designed for and evaluated on **multi-turn tool-calling agents**, but the authors note it addresses a general pathology in group-based policy optimization (within-group variance collapse), suggesting broader applicability to any RL setting with similar issues.

---

### 3. Knapsack RL (arXiv:2509.25849)

**Title:** Knapsack RL: Unlocking Exploration of LLMs via Optimizing Budget Allocation

**Authors:** Ziniu Li, Congliang Chen, Tianyun Yang, Tian Ding, Ruoyu Sun, Ge Zhang, Wenhao Huang, Zhi-Quan Luo

**Submitted:** September 2025 (revised February 2026)

**ICLR 2026 status:** Submitted to ICLR 2026 per OpenReview (https://openreview.net/forum?id=uqxNmKw7DI). I could not confirm acceptance from the sources I checked, though it was listed among ICLR 2026 submissions.

#### Knapsack Formulation
Each task's exploration is treated as an "item" with:
- **Value:** `Value(N_i, p_i) = ProbNonZeroGradient(N_i, p_i) * InfoGain(p_i)` where:
  - `ProbNonZeroGradient = 1 - p_i^N_i - (1-p_i)^N_i` (probability of getting mixed success/failure outcomes, which is needed for non-zero GRPO gradients)
  - `InfoGain ~ p_i * (1-p_i)^2` (approximated via Taylor expansion of one-step policy improvement -- tasks near the learning frontier have highest information gain)
- **Cost:** Number of rollouts N_i allocated to the task
- **Constraints:** Total budget B_total, minimum allocation N_low=2, maximum N_up=128

#### Optimal Assignment Rule
The optimization maximizes total value subject to the fixed total budget. The authors show this can be solved in polynomial time using standard dynamic programming, taking only 1-2 seconds with Numba acceleration.

#### Learning Status Estimation
Simple lag-based heuristic: success rates from the previous epoch estimate current rates. A fallback strategy reallocates unused budget from fully-solved tasks to unsolved tasks.

#### Benchmarks and Results
- **Training:** DAPO-MATH-17K (17,917 prompts)
- **In-domain evaluation:** AIME, AMC, MATH, MINERVA, OLYMPIAD
- **Out-of-domain:** GPQA (scientific reasoning)
- **Key results:**
  - 20-40% improvement in effective (non-zero) gradient ratio
  - Average gains of 2-4 points on math reasoning benchmarks
  - Peak gains: 9.1 points on AMC (Qwen3-4B-Base), 6.8 on AMC (Qwen2.5-Math-7B)
  - Achieves same performance as uniform GRPO with ~2x fewer compute resources
  - Can allocate up to 93 rollouts for challenging problems (impossible under uniform allocation)

---

### Comparison and Relationship Between Papers

| Aspect | CoBA-RL | Knapsack RL | RC-GRPO |
|--------|---------|-------------|---------|
| **Core problem** | Uniform budget is wasteful | Uniform budget causes zero gradients | Low within-group variance kills learning |
| **Solution type** | Adaptive budget allocation via Beta distribution | Adaptive budget via knapsack optimization | Diversity injection via reward conditioning |
| **Key mechanism** | Capability-oriented value + heap-based greedy | Value/cost knapsack DP | Reward token steering of rollouts |
| **What adapts** | Budget per task based on model capability | Budget per task based on gradient informativeness | Trajectory quality distribution within groups |
| **Domain** | Math reasoning | Math reasoning | Multi-turn tool calling |
| **Base models** | Qwen2.5-7B, Qwen3-1.7B/4B | Qwen2.5-Math-7B, Qwen3-4B | Qwen2.5-7B, LLaMA-3.1-8B |

CoBA-RL explicitly compares against Knapsack RL and outperforms it (46.78% vs. 45.39% average), attributing the improvement to dynamic capability-aware recalibration versus Knapsack RL's simpler lag-based estimation. Both operate on the budget allocation axis, while RC-GRPO tackles a complementary problem (within-group diversity) that persists even with optimal budget allocation.

A related concurrent work is **GRESO** (arXiv:2506.02177), "Act Only When It Pays," which uses pre-rollout filtering to skip uninformative prompts entirely based on reward training dynamics, representing another approach to efficient RL compute allocation.

Sources:
- [CoBA-RL (arXiv:2602.03048)](https://arxiv.org/abs/2602.03048)
- [CoBA-RL Full Paper HTML](https://arxiv.org/html/2602.03048)
- [CoBA-RL GitHub](https://github.com/Within-yao/CoBA-RL)
- [RC-GRPO (arXiv:2602.03025)](https://arxiv.org/abs/2602.03025)
- [RC-GRPO Full Paper HTML](https://arxiv.org/html/2602.03025)
- [Knapsack RL (arXiv:2509.25849)](https://arxiv.org/abs/2509.25849)
- [Knapsack RL Full Paper HTML](https://arxiv.org/html/2509.25849v1)
- [Knapsack RL OpenReview](https://openreview.net/forum?id=uqxNmKw7DI)
- [GRESO (arXiv:2506.02177)](https://arxiv.org/abs/2506.02177)

agentId: a11d1541bbbc8a5e8 (use SendMessage with to: 'a11d1541bbbc8a5e8' to continue this agent)
&lt;usage>total_tokens: 25038
tool_uses: 15
duration_ms: 169201&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "89322e70-78ce-4efc-bf97-4a8ef6c17073",
  "isSidechain": false,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "type": "user",
  "uuid": "eb9b6fd7-8b63-4e07-89e9-51af7332d8cd",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to research two papers:\n\n1. **CoBA-RL** (arXiv:2602.03048): \"Capability-Oriented Budget Allocation for RL in LLMs\" - proposes adaptive rollout budget allocation based on task difficulty using Beta distribution.\n\n2. **RC-GRPO** (arXiv:2602.03025): \"Reward-Conditioned GRPO for Multi-Turn Tool Calling\" - addresses low reward variation within GRPO groups via reward-conditioned trajectory generation.\n\nFor each paper:\n1. Use WebSearch to find the paper with the arXiv ID and title keywords\n2. Use WebFetch to read the actual abstract and method from arxiv.org\n3. Search for related work on adaptive budget allocation in RL for LLMs\n\nI need to understand:\n- For CoBA-RL: How does the Beta distribution-based budget allocation work? What is \"capability-oriented\"? How does difficulty estimation work? What benchmarks?\n- For RC-GRPO: What is \"reward-conditioned\" trajectory generation? How does it address low reward variation? What benchmarks? Is it specific to tool calling?\n\nAlso search for \"Knapsack RL ICLR 2026\" which is mentioned as another budget allocation method.\n\nReport all findings in detail. If papers don't exist at those IDs, report that clearly.",
    "agentId": "a11d1541bbbc8a5e8",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I have collected extensive information on all three papers. Here is my comprehensive report.\n\n---\n\n## Detailed Research Report\n\n### 1. CoBA-RL (arXiv:2602.03048)\n\n**Title:** CoBA-RL: Capability-Oriented Budget Allocation for Reinforcement Learning in LLMs\n\n**Authors:** Zhiyuan Yao, Yi-Kai Zhang, Yuxin Chen, Yueqing Sun, Zishan Xu, Yu Yang, Tianhao Hu, Qi Gu, Hui Su, Xunliang Cai\n\n**Submitted:** February 3, 2026 (revised February 6, 2026)\n\n**GitHub:** https://github.com/Within-yao/CoBA-RL\n\n#### Problem\nStandard GRPO uses a uniform rollout budget across all tasks, which is wasteful: easy tasks always succeed and hard tasks always fail, both producing zero gradients. Existing adaptive methods rely on instance-level metrics like pass rates, failing to capture the model's dynamic learning state.\n\n#### How the Beta Distribution-Based Budget Allocation Works\nCoBA-RL models task preferences using a Beta distribution with dynamically adjusted parameters. The density function is:\n\n`Density(p_i; alpha_t, beta_t) = p_i^(alpha_t - 1) * (1 - p_i)^(beta_t - 1) / B(alpha_t, beta_t)`\n\nThe parameters shift based on a \"Global Failure Rate\" (F_t), which is the complementary probability of the average success rate across the training batch. As the model's capability evolves, the Beta distribution parameters change, re-weighting which difficulty levels of tasks are prioritized for budget allocation.\n\n#### What \"Capability-Oriented\" Means\nRather than using static, pre-determined difficulty labels, CoBA-RL uses a \"Capability-Oriented Value function\" that dynamically maps each task to its potential training gain given the model's *current* ability level. The value function combines two components:\n\n- **Budget Saturation Factor:** `eta(B_i, p_i) = 1 - exp(-B_i / (tau * p_i * (1-p_i)))` -- captures diminishing returns from additional rollouts. Tasks with pass rates near 0.5 (moderate difficulty relative to current capability) get the most benefit.\n- **Complete Value Function:** `V(B_i, pi_theta, p_i) = eta(B_i, p_i) * Density(p_i; alpha_t, beta_t)` -- synthesizes budget constraints with the capability-weighted preference density.\n\nThe Global Success Rate `S_t = (1/M) * sum(p_i)` serves as the capability metric, with a sigmoid scaling transformation when failure rates fall below 0.5 to maintain sensitivity during later training stages.\n\n#### Heap-Based Greedy Strategy\nInstead of expensive dynamic programming (O(M * B_total * (B_up - B_low))), CoBA-RL uses a max-heap of marginal gains. It iteratively: (1) extracts the task with highest marginal gain, (2) allocates one rollout unit, (3) recalculates the marginal gain, (4) reinserts into the heap. This achieves O(B_total * log M) complexity -- approximately 928x speedup over DP in tested configurations.\n\n#### Benchmarks and Results\n- **Training data:** DAPO-Math-17K\n- **Evaluation:** AIME24, AIME25, AMC23, MATH500, OlympiadBench\n- **Models:** Qwen2.5-7B-Instruct, Qwen2.5-7B-Base, Qwen3-4B-Base, Qwen3-1.7B-Base (16-rollout group sizes)\n- **Key results (Qwen2.5-7B-Instruct):**\n  - AIME25: 18.33% (vs. GRPO 12.71%, Knapsack-RL 15.21%)\n  - Average: 46.78% (vs. GRPO 42.24%, Knapsack-RL 45.39%)\n  - CoBA-RL outperforms both uniform allocation (+4.54% avg) and static Beta configurations (44.22%-45.21%)\n\n---\n\n### 2. RC-GRPO (arXiv:2602.03025)\n\n**Title:** RC-GRPO: Reward-Conditioned Group Relative Policy Optimization for Multi-Turn Tool Calling Agents\n\n**Authors:** Haitian Zhong, Jixiu Zhai, Lei Song, Jiang Bian, Qiang Liu, Tieniu Tan\n\n**Submitted:** February 3, 2026\n\n#### Problem\nMulti-turn tool calling has sparse rewards and expensive exploration. When SFT produces a strong initial policy, GRPO stalls due to the \"paradox of perfection\": within a group, rollouts tend to all succeed or all fail, collapsing within-group reward variance. The group-normalized advantage becomes uninformative, yielding vanishing gradient updates.\n\n#### What \"Reward-Conditioned\" Trajectory Generation Means\nRC-GRPO treats exploration as a **controllable steering problem** using discrete reward tokens. Two special tokens are defined:\n- `<|high_reward|>` -- steers the model toward optimal trajectories\n- `<|low_reward|>` -- steers toward failure trajectories\n\nThese tokens are prepended to the input, enabling the model to generate systematically different-quality trajectories on demand based on the conditioning signal.\n\n#### How It Addresses Low Reward Variation\nThe algorithm has two stages:\n\n**Stage 1 -- RCTP Training:** A Reward-Conditioned Trajectory Policy is fine-tuned via supervised learning on 1,600 mixed-quality trajectories (800 expert/success, 800 failure). Each trajectory is paired with the appropriate reward token. The model learns to correlate reward tokens with trajectory quality through maximum likelihood training.\n\n**Stage 2 -- RC-GRPO Training:** During RL, for each member j in a GRPO group, a reward token r_j is sampled from a distribution P_sample(r) (with p=0.5 in their experiments, matching the success/failure ratio in training data). Each rollout is conditioned on its sampled token. This explicitly injects diversity within each group -- some rollouts are steered toward success, others toward failure -- ensuring that within-group reward variance remains high and advantages are informative.\n\nThe RL objective uses PPO-style clipped updates with group-relative advantage normalization and KL divergence penalty against the reference policy.\n\n#### Benchmarks and Results\n- **Benchmark:** Berkeley Function Calling Leaderboard v4 (BFCLv4), multi-turn subset (200 evaluation trajectories)\n- **Models:** Qwen2.5-7B-Instruct, LLaMA-3.1-8B-Instruct\n- **Key results:**\n  - Qwen2.5-7B: 85.00% (vs. 48.75% for SFT+GRPO baseline)\n  - LLaMA-3.1-8B: 48.75% (vs. 35.00% SFT+GRPO baseline)\n  - Outperforms even the best API baseline (Opus-4.5 at 61.25%)\n\n#### Scope\nThe method is specifically designed for and evaluated on **multi-turn tool-calling agents**, but the authors note it addresses a general pathology in group-based policy optimization (within-group variance collapse), suggesting broader applicability to any RL setting with similar issues.\n\n---\n\n### 3. Knapsack RL (arXiv:2509.25849)\n\n**Title:** Knapsack RL: Unlocking Exploration of LLMs via Optimizing Budget Allocation\n\n**Authors:** Ziniu Li, Congliang Chen, Tianyun Yang, Tian Ding, Ruoyu Sun, Ge Zhang, Wenhao Huang, Zhi-Quan Luo\n\n**Submitted:** September 2025 (revised February 2026)\n\n**ICLR 2026 status:** Submitted to ICLR 2026 per OpenReview (https://openreview.net/forum?id=uqxNmKw7DI). I could not confirm acceptance from the sources I checked, though it was listed among ICLR 2026 submissions.\n\n#### Knapsack Formulation\nEach task's exploration is treated as an \"item\" with:\n- **Value:** `Value(N_i, p_i) = ProbNonZeroGradient(N_i, p_i) * InfoGain(p_i)` where:\n  - `ProbNonZeroGradient = 1 - p_i^N_i - (1-p_i)^N_i` (probability of getting mixed success/failure outcomes, which is needed for non-zero GRPO gradients)\n  - `InfoGain ~ p_i * (1-p_i)^2` (approximated via Taylor expansion of one-step policy improvement -- tasks near the learning frontier have highest information gain)\n- **Cost:** Number of rollouts N_i allocated to the task\n- **Constraints:** Total budget B_total, minimum allocation N_low=2, maximum N_up=128\n\n#### Optimal Assignment Rule\nThe optimization maximizes total value subject to the fixed total budget. The authors show this can be solved in polynomial time using standard dynamic programming, taking only 1-2 seconds with Numba acceleration.\n\n#### Learning Status Estimation\nSimple lag-based heuristic: success rates from the previous epoch estimate current rates. A fallback strategy reallocates unused budget from fully-solved tasks to unsolved tasks.\n\n#### Benchmarks and Results\n- **Training:** DAPO-MATH-17K (17,917 prompts)\n- **In-domain evaluation:** AIME, AMC, MATH, MINERVA, OLYMPIAD\n- **Out-of-domain:** GPQA (scientific reasoning)\n- **Key results:**\n  - 20-40% improvement in effective (non-zero) gradient ratio\n  - Average gains of 2-4 points on math reasoning benchmarks\n  - Peak gains: 9.1 points on AMC (Qwen3-4B-Base), 6.8 on AMC (Qwen2.5-Math-7B)\n  - Achieves same performance as uniform GRPO with ~2x fewer compute resources\n  - Can allocate up to 93 rollouts for challenging problems (impossible under uniform allocation)\n\n---\n\n### Comparison and Relationship Between Papers\n\n| Aspect | CoBA-RL | Knapsack RL | RC-GRPO |\n|--------|---------|-------------|---------|\n| **Core problem** | Uniform budget is wasteful | Uniform budget causes zero gradients | Low within-group variance kills learning |\n| **Solution type** | Adaptive budget allocation via Beta distribution | Adaptive budget via knapsack optimization | Diversity injection via reward conditioning |\n| **Key mechanism** | Capability-oriented value + heap-based greedy | Value/cost knapsack DP | Reward token steering of rollouts |\n| **What adapts** | Budget per task based on model capability | Budget per task based on gradient informativeness | Trajectory quality distribution within groups |\n| **Domain** | Math reasoning | Math reasoning | Multi-turn tool calling |\n| **Base models** | Qwen2.5-7B, Qwen3-1.7B/4B | Qwen2.5-Math-7B, Qwen3-4B | Qwen2.5-7B, LLaMA-3.1-8B |\n\nCoBA-RL explicitly compares against Knapsack RL and outperforms it (46.78% vs. 45.39% average), attributing the improvement to dynamic capability-aware recalibration versus Knapsack RL's simpler lag-based estimation. Both operate on the budget allocation axis, while RC-GRPO tackles a complementary problem (within-group diversity) that persists even with optimal budget allocation.\n\nA related concurrent work is **GRESO** (arXiv:2506.02177), \"Act Only When It Pays,\" which uses pre-rollout filtering to skip uninformative prompts entirely based on reward training dynamics, representing another approach to efficient RL compute allocation.\n\nSources:\n- [CoBA-RL (arXiv:2602.03048)](https://arxiv.org/abs/2602.03048)\n- [CoBA-RL Full Paper HTML](https://arxiv.org/html/2602.03048)\n- [CoBA-RL GitHub](https://github.com/Within-yao/CoBA-RL)\n- [RC-GRPO (arXiv:2602.03025)](https://arxiv.org/abs/2602.03025)\n- [RC-GRPO Full Paper HTML](https://arxiv.org/html/2602.03025)\n- [Knapsack RL (arXiv:2509.25849)](https://arxiv.org/abs/2509.25849)\n- [Knapsack RL Full Paper HTML](https://arxiv.org/html/2509.25849v1)\n- [Knapsack RL OpenReview](https://openreview.net/forum?id=uqxNmKw7DI)\n- [GRESO (arXiv:2506.02177)](https://arxiv.org/abs/2506.02177)"
      }
    ],
    "totalDurationMs": 169201,
    "totalTokens": 25038,
    "totalToolUseCount": 15,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 286,
      "cache_read_input_tokens": 21522,
      "output_tokens": 3229,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 286
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3229,
          "cache_read_input_tokens": 21522,
          "cache_creation_input_tokens": 286,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 286,
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
      "otherToolCount": 15
    }
  },
  "sourceToolAssistantUUID": "89322e70-78ce-4efc-bf97-4a8ef6c17073",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 15_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-11 (UTC).**  ## Original idea {   \"title\": \"Error-Type-Conditioned Branching GRPO for Self-Supervised Agent Recove…",
  "leafUuid": "eb9b6fd7-8b63-4e07-89e9-51af7332d8cd",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "Error-type-aware branching for agent recovery beyond Fission-GRPO",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c"
}
```

---

### Tool result

_source line 17 · 2026-05-11T23:32:09.109Z_

<details><summary>↩ Tool result · `toolu_0167yVdgUzjjLLASeWMyicvU`</summary>

````text
I now have comprehensive information. Here is the full research report.

---

## Research Report: Stratified GRPO (arXiv:2510.06214)

### Confirmation

The paper **does exist** at arXiv:2510.06214. It is real and substantive.

**Full Title:** "Stratified GRPO: Handling Structural Heterogeneity in Reinforcement Learning of LLM Search Agents"

**Authors:** Mingkang Zhu, Xi Chen, Bei Yu, Hengshuang Zhao, Jiaya Jia

**Submitted:** October 7, 2025

**Categories:** cs.LG, cs.AI, cs.CL

---

### Publication Venue Status

The paper was **submitted to ICLR 2026** (OpenReview ID: `hqnGfzQQfa`, submission #431, primary area: "Foundation or frontier models, including LLMs"). The submission was dated September 1, 2025 and last modified February 11, 2026. As of my research, **no public decision (accept/reject) is visible on the OpenReview page**, and the paper does not appear to be findable on the ICLR 2026 virtual site. The arXiv version is labeled "Preprint." The decision status remains unclear -- it may still be under review, or the decision may not be publicly visible yet.

---

### What Problem Does It Solve?

When training LLM search agents (models that call external search/retrieval tools), the generated trajectories are **structurally heterogeneous**: some trajectories use zero search calls, some use one, some use two or more. These different trajectory structures lead to fundamentally different reward distributions -- a trajectory that uses no search operates in a different "regime" than one that performs multi-hop retrieval.

Standard GRPO computes a **single global baseline** (mean and standard deviation across all trajectories in a group) and normalizes advantages against it. The authors identify that this creates **cross-stratum bias** -- an "apples-to-oranges" comparison where trajectories from different structural categories are compared against a shared baseline that is appropriate for none of them.

Concretely, this bias:
- Uniformly penalizes trajectories from low-reward strata while favoring high-reward ones, regardless of the quality of individual trajectories within their stratum
- Distorts credit assignment
- Hinders exploration of complex multi-step search strategies (the model learns to avoid multi-hop search because it is penalized relative to simpler strategies)

---

### What Are the "Strata"?

Strata are defined by a **partitioning function** S(tau; theta) that assigns each trajectory to a discrete stratum k in {0, ..., I-1}. The primary partitioning variable used in the paper is the **number of search calls** in a trajectory:

- **Stratum 0:** Trajectories with zero search calls (direct answer)
- **Stratum 1:** Trajectories with one search call
- **Stratum 2:** Trajectories with two search calls
- And so on...

The paper frames this generally -- "a chosen partitioning function (e.g., the search count for search agents)" -- so the strata definition is domain-dependent. For search agents, search count is the natural choice because it determines the trajectory's structural character.

---

### What Is SAN (Stratified Advantage Normalization) Exactly?

**Standard GRPO (Global Normalization):**
```
A_GN(tau_i) = (R(tau_i) - R_global_mean) / (sigma_global + epsilon)
```

**SAN:**
```
A_SAN(tau_i) = (R(tau_i) - mu_k(x)) / (sigma_k(x) + epsilon)
```

Where mu_k and sigma_k are the empirical mean and standard deviation computed **only within stratum k** -- the stratum to which trajectory tau_i belongs.

The key decomposition (Proposition 1) shows:
```
A_GN = (scaled A_SAN) + cross-stratum offset
```
where the cross-stratum offset = (stratum_mean - global_mean) / global_std. This offset is the bias term: it uniformly shifts all trajectories in a stratum up or down regardless of their individual quality.

**Blended Advantage** (for finite-sample stability):
```
A_blend(tau) = alpha * A_SAN(tau) + (1 - alpha) * A_GN(tau),    alpha in [0, 1]
```

This convex blend handles edge cases where some strata contain very few trajectories (making within-stratum statistics noisy) by borrowing signal from the global estimate.

---

### Why Is Within-Group (Standard GRPO) Normalization Insufficient?

Standard GRPO's "group" is all trajectories for a given prompt -- it is **not** stratified by structural properties. The paper proves several formal results:

1. **Theorem 1:** The cross-stratum offset is precisely the source of excess variance in global normalization.

2. **Theorem 4 (Conditional Properties):** In the population limit:
   - SAN is conditionally unbiased: E[A_SAN | stratum k] = 0 for every k
   - SAN has unit conditional variance: Var(A_SAN | stratum k) = 1
   - Global Normalization is **conditionally biased**: E[A_GN | k] = (stratum_mean - global_mean) / global_std (nonzero whenever strata have different reward distributions)

3. **Theorem 5 (Global Properties):** Both SAN and GN are globally unbiased (mean zero) and have identical unit global variance when epsilon = 0 -- so SAN gives you strictly better conditional properties without sacrificing anything globally.

4. **Theorem 3 (Gradient):** SAN's population gradient exactly targets a weighted sum of within-stratum policy gradients, with weights proportional to stratum probabilities scaled by inverse standard deviations. This means exploration of multi-step strategies is not suppressed.

In short: standard GRPO's normalization across all trajectories **conflates signal from structurally different trajectory types**, injecting systematic bias that specifically punishes complex multi-hop strategies (which tend to have lower average reward) and rewards simple strategies, regardless of whether an individual complex trajectory was actually good.

---

### How Is This Different from Standard GRPO Group Normalization?

| Property | Standard GRPO | Stratified GRPO (SAN) |
|---|---|---|
| Advantage baseline | Single global mean/std across all trajectories for a prompt | Per-stratum mean/std within each structural category |
| Cross-stratum bias | Present -- conflates different trajectory types | Eliminated by construction |
| Conditional unbiasedness | No (biased within each stratum) | Yes (zero-mean within each stratum) |
| Conditional variance | Inconsistent across strata | Unit variance within each stratum |
| Global unbiasedness | Yes | Yes (preserved) |
| Effect on exploration | Suppresses multi-step strategies | Encourages exploration of complex strategies |
| Training stability | Subject to training collapse (especially on Instruct models) | Stable, monotonically increasing rewards |

---

### Benchmarks and Evaluation

**Base Models:** Qwen-2.5-3B (both Base and Instruct variants)

**Training Data:** Merged training splits from Natural Questions (NQ) and HotpotQA. Reward: Exact Match.

**Retrieval Setup:** Wikipedia 2018 dump with E5 retriever, top-3 passages per query.

**Evaluation Benchmarks (7 QA datasets):**
- **Single-hop:** Natural Questions (NQ), TriviaQA, PopQA
- **Multi-hop:** HotpotQA, 2WikiMultiHopQA, MuSiQue, Bamboogle

**Baselines:**
- Non-RL: Direct Generation, SFT, RAG, Search-o1, IRCoT
- RL methods: GRPO, Search-R1, R1, ReSearch

**Key Results:**
- Stratified GRPO improves over GRPO by **up to 11.3 points** averaged across benchmarks
- Up to **14.5 points** improvement over the strongest baseline on multi-hop tasks
- Outperforms best baseline by up to **8.3 points** overall
- Standard GRPO suffers training collapse on Instruct models; Stratified GRPO remains stable
- Stratified GRPO learns policies that converge to ~2.5 search calls (effective multi-hop reasoning), while GRPO stagnates at ~1 search call

---

### Follow-up and Related Work

The paper is relatively recent (October 2025), but the broader GRPO ecosystem has been active:

- **Blockwise Advantage Estimation** (arXiv:2602.10231, Pavlenko et al.) independently uses stratification in advantage estimation for multi-objective RL, stratifying by prefix-derived intermediate outcomes -- a conceptually related approach though not directly citing Stratified GRPO.
- **S-GRPO** (arXiv:2604.16557) is a different paper (unified post-training for vision-language models) that does **not** cite or build on Stratified GRPO.
- **Demystifying GRPO** (arXiv:2603.01162) analyzes GRPO's policy gradient as a U-statistic, providing complementary theoretical understanding.
- The Emergent Mind topic page on "Stratified Normalization" lists the paper as a key reference for stratified normalization in RL.

---

### Limitations (Implicit -- No Dedicated Section)

- Requires **domain knowledge** to define strata (search count is specific to search agents; other agent types would need different partitioning functions)
- When strata contain **very few trajectories**, SAN estimates become noisy (addressed via blending)
- The small regularization constant epsilon technically breaks the perfect affine invariance property
- Only evaluated on **Qwen-2.5-3B** -- unknown how well it scales to larger models
- Only tested on **QA tasks with search** -- generalization to other agentic settings (code, tool use, etc.) is unverified
- **Applicability to continuous action spaces** is unclear

Sources:
- [Stratified GRPO - arXiv Abstract](https://arxiv.org/abs/2510.06214)
- [Stratified GRPO - Full HTML Paper](https://arxiv.org/html/2510.06214)
- [Stratified GRPO - OpenReview (ICLR 2026 Submission)](https://openreview.net/forum?id=hqnGfzQQfa)
- [Stratified GRPO - ResearchGate](https://www.researchgate.net/publication/396292051_Stratified_GRPO_Handling_Structural_Heterogeneity_in_Reinforcement_Learning_of_LLM_Search_Agents)
- [Blockwise Advantage Estimation (related work)](https://arxiv.org/abs/2602.10231)
- [S-GRPO (unrelated despite similar name)](https://arxiv.org/html/2604.16557v1)
- [Demystifying GRPO as U-Statistic](https://arxiv.org/abs/2603.01162)
- [Emergent Mind - Stratified Normalization Methods](https://www.emergentmind.com/topics/stratified-normalization)
- [ICLR 2026 Accepted Paper List (Paper Copilot)](https://papercopilot.com/paper-list/iclr-paper-list/iclr-2026-paper-list/)

agentId: a9e76bf4de50fb468 (use SendMessage with to: 'a9e76bf4de50fb468' to continue this agent)
&lt;usage>total_tokens: 27389
tool_uses: 18
duration_ms: 189759&lt;/usage>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "4bb90586-abf2-4205-977c-dcddc128e16c",
  "isSidechain": false,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "type": "user",
  "uuid": "9e5fb5e2-ce25-48e1-8be7-fb9cad1d5286",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to deeply research the paper \"Stratified GRPO\" (arXiv:2510.06214). This is claimed to be titled \"Stratified GRPO: Handling Structural Heterogeneity in Reinforcement Learning of LLM Search Agents\" proposing Stratified Advantage Normalization (SAN).\n\nPlease:\n1. Use WebSearch to find this paper with queries like \"Stratified GRPO arXiv 2510.06214\", \"stratified advantage normalization GRPO\", \"structural heterogeneity reinforcement learning LLM\"\n2. Use WebFetch to read the actual paper abstract and method sections from arxiv.org\n3. Search for follow-up work or related papers on stratified normalization in GRPO\n\nI need to understand:\n- What are the \"strata\" they use? How do they partition trajectories?\n- What is SAN (Stratified Advantage Normalization) exactly?\n- What problem does it solve? Why is within-group normalization insufficient?\n- What benchmarks/tasks do they evaluate on?\n- How is this different from standard GRPO group normalization?\n- Is this published at a venue or just arXiv?\n\nReport all findings in detail. If the paper doesn't exist at that arXiv ID, report that clearly.",
    "agentId": "a9e76bf4de50fb468",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive information. Here is the full research report.\n\n---\n\n## Research Report: Stratified GRPO (arXiv:2510.06214)\n\n### Confirmation\n\nThe paper **does exist** at arXiv:2510.06214. It is real and substantive.\n\n**Full Title:** \"Stratified GRPO: Handling Structural Heterogeneity in Reinforcement Learning of LLM Search Agents\"\n\n**Authors:** Mingkang Zhu, Xi Chen, Bei Yu, Hengshuang Zhao, Jiaya Jia\n\n**Submitted:** October 7, 2025\n\n**Categories:** cs.LG, cs.AI, cs.CL\n\n---\n\n### Publication Venue Status\n\nThe paper was **submitted to ICLR 2026** (OpenReview ID: `hqnGfzQQfa`, submission #431, primary area: \"Foundation or frontier models, including LLMs\"). The submission was dated September 1, 2025 and last modified February 11, 2026. As of my research, **no public decision (accept/reject) is visible on the OpenReview page**, and the paper does not appear to be findable on the ICLR 2026 virtual site. The arXiv version is labeled \"Preprint.\" The decision status remains unclear -- it may still be under review, or the decision may not be publicly visible yet.\n\n---\n\n### What Problem Does It Solve?\n\nWhen training LLM search agents (models that call external search/retrieval tools), the generated trajectories are **structurally heterogeneous**: some trajectories use zero search calls, some use one, some use two or more. These different trajectory structures lead to fundamentally different reward distributions -- a trajectory that uses no search operates in a different \"regime\" than one that performs multi-hop retrieval.\n\nStandard GRPO computes a **single global baseline** (mean and standard deviation across all trajectories in a group) and normalizes advantages against it. The authors identify that this creates **cross-stratum bias** -- an \"apples-to-oranges\" comparison where trajectories from different structural categories are compared against a shared baseline that is appropriate for none of them.\n\nConcretely, this bias:\n- Uniformly penalizes trajectories from low-reward strata while favoring high-reward ones, regardless of the quality of individual trajectories within their stratum\n- Distorts credit assignment\n- Hinders exploration of complex multi-step search strategies (the model learns to avoid multi-hop search because it is penalized relative to simpler strategies)\n\n---\n\n### What Are the \"Strata\"?\n\nStrata are defined by a **partitioning function** S(tau; theta) that assigns each trajectory to a discrete stratum k in {0, ..., I-1}. The primary partitioning variable used in the paper is the **number of search calls** in a trajectory:\n\n- **Stratum 0:** Trajectories with zero search calls (direct answer)\n- **Stratum 1:** Trajectories with one search call\n- **Stratum 2:** Trajectories with two search calls\n- And so on...\n\nThe paper frames this generally -- \"a chosen partitioning function (e.g., the search count for search agents)\" -- so the strata definition is domain-dependent. For search agents, search count is the natural choice because it determines the trajectory's structural character.\n\n---\n\n### What Is SAN (Stratified Advantage Normalization) Exactly?\n\n**Standard GRPO (Global Normalization):**\n```\nA_GN(tau_i) = (R(tau_i) - R_global_mean) / (sigma_global + epsilon)\n```\n\n**SAN:**\n```\nA_SAN(tau_i) = (R(tau_i) - mu_k(x)) / (sigma_k(x) + epsilon)\n```\n\nWhere mu_k and sigma_k are the empirical mean and standard deviation computed **only within stratum k** -- the stratum to which trajectory tau_i belongs.\n\nThe key decomposition (Proposition 1) shows:\n```\nA_GN = (scaled A_SAN) + cross-stratum offset\n```\nwhere the cross-stratum offset = (stratum_mean - global_mean) / global_std. This offset is the bias term: it uniformly shifts all trajectories in a stratum up or down regardless of their individual quality.\n\n**Blended Advantage** (for finite-sample stability):\n```\nA_blend(tau) = alpha * A_SAN(tau) + (1 - alpha) * A_GN(tau),    alpha in [0, 1]\n```\n\nThis convex blend handles edge cases where some strata contain very few trajectories (making within-stratum statistics noisy) by borrowing signal from the global estimate.\n\n---\n\n### Why Is Within-Group (Standard GRPO) Normalization Insufficient?\n\nStandard GRPO's \"group\" is all trajectories for a given prompt -- it is **not** stratified by structural properties. The paper proves several formal results:\n\n1. **Theorem 1:** The cross-stratum offset is precisely the source of excess variance in global normalization.\n\n2. **Theorem 4 (Conditional Properties):** In the population limit:\n   - SAN is conditionally unbiased: E[A_SAN | stratum k] = 0 for every k\n   - SAN has unit conditional variance: Var(A_SAN | stratum k) = 1\n   - Global Normalization is **conditionally biased**: E[A_GN | k] = (stratum_mean - global_mean) / global_std (nonzero whenever strata have different reward distributions)\n\n3. **Theorem 5 (Global Properties):** Both SAN and GN are globally unbiased (mean zero) and have identical unit global variance when epsilon = 0 -- so SAN gives you strictly better conditional properties without sacrificing anything globally.\n\n4. **Theorem 3 (Gradient):** SAN's population gradient exactly targets a weighted sum of within-stratum policy gradients, with weights proportional to stratum probabilities scaled by inverse standard deviations. This means exploration of multi-step strategies is not suppressed.\n\nIn short: standard GRPO's normalization across all trajectories **conflates signal from structurally different trajectory types**, injecting systematic bias that specifically punishes complex multi-hop strategies (which tend to have lower average reward) and rewards simple strategies, regardless of whether an individual complex trajectory was actually good.\n\n---\n\n### How Is This Different from Standard GRPO Group Normalization?\n\n| Property | Standard GRPO | Stratified GRPO (SAN) |\n|---|---|---|\n| Advantage baseline | Single global mean/std across all trajectories for a prompt | Per-stratum mean/std within each structural category |\n| Cross-stratum bias | Present -- conflates different trajectory types | Eliminated by construction |\n| Conditional unbiasedness | No (biased within each stratum) | Yes (zero-mean within each stratum) |\n| Conditional variance | Inconsistent across strata | Unit variance within each stratum |\n| Global unbiasedness | Yes | Yes (preserved) |\n| Effect on exploration | Suppresses multi-step strategies | Encourages exploration of complex strategies |\n| Training stability | Subject to training collapse (especially on Instruct models) | Stable, monotonically increasing rewards |\n\n---\n\n### Benchmarks and Evaluation\n\n**Base Models:** Qwen-2.5-3B (both Base and Instruct variants)\n\n**Training Data:** Merged training splits from Natural Questions (NQ) and HotpotQA. Reward: Exact Match.\n\n**Retrieval Setup:** Wikipedia 2018 dump with E5 retriever, top-3 passages per query.\n\n**Evaluation Benchmarks (7 QA datasets):**\n- **Single-hop:** Natural Questions (NQ), TriviaQA, PopQA\n- **Multi-hop:** HotpotQA, 2WikiMultiHopQA, MuSiQue, Bamboogle\n\n**Baselines:**\n- Non-RL: Direct Generation, SFT, RAG, Search-o1, IRCoT\n- RL methods: GRPO, Search-R1, R1, ReSearch\n\n**Key Results:**\n- Stratified GRPO improves over GRPO by **up to 11.3 points** averaged across benchmarks\n- Up to **14.5 points** improvement over the strongest baseline on multi-hop tasks\n- Outperforms best baseline by up to **8.3 points** overall\n- Standard GRPO suffers training collapse on Instruct models; Stratified GRPO remains stable\n- Stratified GRPO learns policies that converge to ~2.5 search calls (effective multi-hop reasoning), while GRPO stagnates at ~1 search call\n\n---\n\n### Follow-up and Related Work\n\nThe paper is relatively recent (October 2025), but the broader GRPO ecosystem has been active:\n\n- **Blockwise Advantage Estimation** (arXiv:2602.10231, Pavlenko et al.) independently uses stratification in advantage estimation for multi-objective RL, stratifying by prefix-derived intermediate outcomes -- a conceptually related approach though not directly citing Stratified GRPO.\n- **S-GRPO** (arXiv:2604.16557) is a different paper (unified post-training for vision-language models) that does **not** cite or build on Stratified GRPO.\n- **Demystifying GRPO** (arXiv:2603.01162) analyzes GRPO's policy gradient as a U-statistic, providing complementary theoretical understanding.\n- The Emergent Mind topic page on \"Stratified Normalization\" lists the paper as a key reference for stratified normalization in RL.\n\n---\n\n### Limitations (Implicit -- No Dedicated Section)\n\n- Requires **domain knowledge** to define strata (search count is specific to search agents; other agent types would need different partitioning functions)\n- When strata contain **very few trajectories**, SAN estimates become noisy (addressed via blending)\n- The small regularization constant epsilon technically breaks the perfect affine invariance property\n- Only evaluated on **Qwen-2.5-3B** -- unknown how well it scales to larger models\n- Only tested on **QA tasks with search** -- generalization to other agentic settings (code, tool use, etc.) is unverified\n- **Applicability to continuous action spaces** is unclear\n\nSources:\n- [Stratified GRPO - arXiv Abstract](https://arxiv.org/abs/2510.06214)\n- [Stratified GRPO - Full HTML Paper](https://arxiv.org/html/2510.06214)\n- [Stratified GRPO - OpenReview (ICLR 2026 Submission)](https://openreview.net/forum?id=hqnGfzQQfa)\n- [Stratified GRPO - ResearchGate](https://www.researchgate.net/publication/396292051_Stratified_GRPO_Handling_Structural_Heterogeneity_in_Reinforcement_Learning_of_LLM_Search_Agents)\n- [Blockwise Advantage Estimation (related work)](https://arxiv.org/abs/2602.10231)\n- [S-GRPO (unrelated despite similar name)](https://arxiv.org/html/2604.16557v1)\n- [Demystifying GRPO as U-Statistic](https://arxiv.org/abs/2603.01162)\n- [Emergent Mind - Stratified Normalization Methods](https://www.emergentmind.com/topics/stratified-normalization)\n- [ICLR 2026 Accepted Paper List (Paper Copilot)](https://papercopilot.com/paper-list/iclr-paper-list/iclr-2026-paper-list/)"
      }
    ],
    "totalDurationMs": 189759,
    "totalTokens": 27389,
    "totalToolUseCount": 18,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 328,
      "cache_read_input_tokens": 24239,
      "output_tokens": 2821,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 328
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2821,
          "cache_read_input_tokens": 24239,
          "cache_creation_input_tokens": 328,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 328,
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
      "otherToolCount": 18
    }
  },
  "sourceToolAssistantUUID": "4bb90586-abf2-4205-977c-dcddc128e16c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Tool result

_source line 18 · 2026-05-11T23:32:36.770Z_

<details><summary>↩ Tool result · `toolu_011fm4rR7nyqy5r5z1p25HX2`</summary>

```text
Now I have comprehensive information. Here is the detailed research report.

---

## Detailed Research Report: Fission-GRPO (arXiv:2601.15625)

### Paper Verification

The paper **does exist** at arXiv:2601.15625. It is confirmed as:

- **Title:** "Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors"
- **Authors:** Zhiwei Zhang, Fei Zhao, Rui Wang, Zezhong Wang, Bin Liang, Jiakang Wang, Yao Hu, Shaosheng Cao, Kam-Fai Wong
- **Affiliations:** The Chinese University of Hong Kong (1) and Xiaohongshu Inc. (2)
- **Submitted:** January 22, 2026 (v1); revised April 20, 2026 (v2)
- **Conference:** **Accepted to ACL 2026 Main Conference** (confirmed on the arXiv abstract page)

---

### 1. What Exactly Is the "Fission" Mechanism?

The "fission" metaphor refers to splitting a single failed trajectory into multiple new training instances. The process operates in three stages within the GRPO training loop:

**Stage 1 -- Standard GRPO Exploration:** For each query x, the model samples G rollouts (G=8 in their setup). Each rollout is scored by a composite reward function. Trajectories failing the error filter (R_corr < delta_corr OR R_fmt = 0) are flagged.

**Stage 2 -- Error Augmentation:** Each failed trajectory tau_err is intercepted and augmented with diagnostic feedback f from the Error Simulator S_phi. The augmented context is constructed as: `x_corr = [x; tau_err; f]` (original query + failed tool call + simulated diagnostic feedback).

**Stage 3 -- Fission Update:** Each augmented error context is "fissioned" -- expanded into G' parallel recovery attempts by resampling new rollouts on-policy from the current model conditioned on x_corr. So a single error becomes G' new training trajectories, each attempting recovery from that specific error state with the benefit of the diagnostic feedback.

All corrective samples are stored in a **LIFO (Last-In-First-Out) buffer** (B_corr), ensuring that the most recent errors (closest to the current policy) are consumed first during corrective updates. Deduplication is applied via hashing (x, tau_err) pairs to avoid redundant training on identical error patterns.

The fission update is triggered when the buffer accumulates sufficient samples (|B| >= B_trig). The paper investigates trigger frequency sensitivity in Section 4.5 and finds performance is stable for small-to-moderate intervals but degrades with overly sparse triggering.

---

### 2. The Error Simulator

The Error Simulator (S_phi) is a critical component that generates realistic, context-aware error feedback resembling actual runtime error traces.

**Training data:** Approximately 2,000 instances distilled from error logs. Each instance contains:
1. System prompt + tool specifications + dialogue state
2. The model's failed tool call (tau_err)
3. The ground-truth correct call (tau_gt)
4. A teacher-written diagnostic message generated by Claude Sonnet 4, filtered for quality

**Architecture:** Qwen3-32B fine-tuned via supervised fine-tuning (SFT).

**Critical constraint -- No target leakage:** The simulator's outputs are explicitly restricted to "non-revealing error descriptions" (e.g., "parameter status expects value OPEN") rather than exposing the full correct tool call. This is essential -- if the simulator revealed the answer, the model would learn to pattern-match rather than reason about recovery.

**Inference:** `f <- S_phi(x, tau_err, tau_gt)` -- it consumes the system prompt, tools, dialogue history, ground truth, and the failed attempt to produce concise diagnostic feedback.

**Missing details:** The paper does not disclose the number of training epochs, learning rate, specific loss function, or validation metrics for the simulator training.

---

### 3. How G' Parallel Recovery Attempts Are Resampled

The resampling procedure (from Algorithm 1, lines 37-42) works as follows:

1. Construct the augmented corrective context: `x_corr = [x; tau_err; f]`
2. Sample G' new rollouts from the current policy: `{tau'_j}_{j=1}^{G'} ~ pi_theta(.|x_corr)`
3. Compute rewards for each recovery trajectory
4. Calculate corrective advantages using **within-group normalization**:
   - mu'_R = (1/G') * sum(r'_j)
   - sigma'_R = Std(r'_j)
   - A'_j = (r'_j - mu'_R) / (sigma'_R + epsilon)
5. Apply the corrective objective (Eq. 6): `J_corr(theta) = E_xcorr[(1/G') * sum_j A'(tau'_j) * grad log pi_theta(tau'_j|x_corr)]`

This is a standard GRPO-style clipped objective with KL penalty, applied over the corrective distribution. The innovation is not a novel loss function but rather the **contextual conditioning** (on error + feedback) and **multiplicative resampling** (one error becomes G' training signals).

The authors note that conditioning on explicit feedback f "typically increases outcome diversity within the fission group, improving the usefulness of advantage estimates for recovery updates."

---

### 4. Benchmarks and Main Results

**Benchmark:** Evaluation is **exclusively on BFCL v4 Multi-Turn**. The authors chose this because it features an "interactive error feedback mechanism: upon execution error, the environment provides explicit error traces and permits the agent up to 20 retries." The limitations section explicitly acknowledges this narrow evaluation scope.

**Primary Results (Table 1):**

| Model | Method | Overall Accuracy |
|---|---|---|
| Qwen3-8B | GRPO | 42.75% |
| Qwen3-8B | DAPO | ~41-42% |
| Qwen3-8B | Dr.GRPO | ~42-43% |
| Qwen3-8B | **Fission-GRPO** | **46.75%** |
| ToolACE-2-8B | Specialized | 37.00% |
| BitAgent-8B | Specialized | 37.75% |

Results are consistent across the Qwen3 family (1.7B, 4B, 8B), with Fission-GRPO outperforming all baselines at every scale.

**Error Recovery Analysis (Figure 3):**
- Average error recovery rate improvement: **+5.7%** across categories
- Long Context category: **+11.8%** improvement (most dramatic)
- One-shot success (getting it right on the first try) is also preserved/improved: **+1.75%** average

The abstract mentions "gains up to 17.4% on additional benchmarks" but the paper body evaluates only BFCL v4 Multi-Turn; this 17.4% figure likely refers to a specific error-category sub-split rather than a separate benchmark.

---

### 5. Error Type Conditioning

Fission-GRPO conditions on **error occurrence + diagnostic feedback content**, **not** on explicit error type categories. The error filter uses a two-level check:
- **Format validity** (R_fmt): Binary {0,1} -- is the output a well-formed tool call?
- **Functional correctness** (R_corr): Scalar threshold (delta_corr = 1) -- did the call do the right thing?

However, the resampling uses a **unified augmented context** `[x; tau_err; f]` without any explicit error-type labeling or categorization. The diagnostic feedback f implicitly encodes information about what went wrong, but there is no taxonomy of error types that conditions different recovery strategies.

---

### 6. How Branching Differs from Tree-Based Approaches (ARPO, Tree-GRPO)

This is a notable gap in the paper. The Related Work section (Section 2) **does not discuss tree-based methods, MCTS approaches, ARPO, or Tree-GRPO at all**. The authors position their work against:
- Standard RL baselines (GRPO, DAPO, Dr.GRPO)
- Static error-correction datasets (ToolACE, LoopTool)

Based on the technical details, the key architectural distinctions from tree-based approaches are:

1. **Targeted vs. exhaustive branching:** Tree-based methods (like MCTS or Tree-GRPO) branch at decision points to explore the full action space. Fission-GRPO branches **only at error points**, focusing computational budget specifically on diagnosed failure states.

2. **Simulator-augmented context:** Tree-based methods typically branch with the same context. Fission-GRPO augments the context with diagnostic feedback before branching, providing the model additional information about what went wrong.

3. **On-policy error alignment:** The LIFO buffer ensures the model trains on errors from its current policy distribution, not from a static exploration tree. As the policy improves, the error distribution shifts, and the fission targets shift with it.

4. **No backtracking:** Unlike tree search which explores alternative paths from earlier states, Fission-GRPO always conditions on the full failed trajectory plus feedback -- it's forward-looking recovery, not backward-looking exploration.

5. **Flat structure:** There is no tree data structure or recursive branching. Each error produces exactly one "fission group" of G' parallel attempts at the same level.

---

### 7. Reward Function Design

The composite reward R(tau, t) has three components with time-annealing weights:

1. **Format Compliance (R_fmt):** Binary {0,1}. Weight w_fmt(t) decays from 2 to 1 over training.
2. **Functional Correctness (R_corr):** Range [0,2]. Computed as `R_corr = alpha * I(N=N*) + (1-alpha) * (1/|M|) * sum F1(a, a*)` where I(N=N*) checks correct function selection and F1 measures token-level overlap on matched parameters. Weight w_corr(t) increases from 2 to 3.
3. **Efficiency Regularization (R_len):** Range [0,1] via piecewise Gaussian with time-annealing.

The dynamic weighting shifts focus "from syntax to semantics as training progresses."

---

### 8. Ablation Studies

**Table 2 -- Feedback Quality Ablation (Qwen3-8B):**

| Configuration | Overall Accuracy | Delta |
|---|---|---|
| GRPO baseline | 42.75% | -- |
| Fission-Static (generic error message) | 44.00% | +1.25% |
| Fission-Dynamic (learned Error Simulator) | 46.75% | +4.00% |

The +2.75% gap between Static and Dynamic demonstrates that the Error Simulator's precise, context-aware diagnostics are substantially more useful than generic "error occurred" messages. However, even generic feedback provides some benefit (+1.25%).

**Section 4.5 -- Trigger Frequency:** Performance is stable for small N (frequent fission triggers) but degrades with sparse updates (large N). The Miss Param and Long Context error categories are most sensitive to trigger frequency.

---

### 9. Code Availability

**No code has been released.** The paper contains no mention of a GitHub repository, code release, or open-source plans. No repository was found through GitHub searches. The authors do provide detailed hyperparameters (learning rate 1e-6, batch size 8, G=8, max prompt 12,800 tokens, max response 4,096 tokens) and Algorithm 1 pseudocode.

---

### 10. Follow-Up Work and Citations

Given the paper was posted in January 2026 (approximately 4 months ago), I was unable to find a specific citation count. Related concurrent work in the same space includes:

- **RC-GRPO** (arXiv:2602.03025) -- "Reward-Conditioned GRPO for Multi-Turn Tool Calling Agents" -- addresses a similar problem (vanishing updates in multi-turn GRPO) but via reward-conditioned trajectory generation rather than error-augmented fission. It does not appear to cite Fission-GRPO directly.
- **CLEANER** (arXiv:2601.15141) -- "Self-Purified Trajectories Boost Agentic Reinforcement Learning" -- a concurrent paper addressing error-contaminated trajectories via retrospective replacement rather than forward recovery.
- **SeeUPO** (arXiv:2602.06554) -- "Sequence-Level Agentic-RL with Convergence Guarantees" -- also evaluated on BFCL v4, focuses on training stability via sequential updates rather than error recovery specifically.

---

### Known Limitations and Criticisms

From the literature review and the paper's own discussion:

1. **Simulator dependency:** Requires ~2K teacher-written error instances (generated via Claude Sonnet 4); scalability to new tool domains is unclear.
2. **Threshold sensitivity:** Error identification depends on tunable delta_corr; sensitivity analysis is limited.
3. **Single benchmark:** Evaluated only on BFCL v4 Multi-Turn; generalization to other tool-use benchmarks, code execution, or web interaction is untested.
4. **Computational overhead:** Multiplicative resampling (G' extra rollouts per error) increases training cost, though the paper does not quantify this overhead.
5. **No tree-based comparison:** The paper does not engage with the tree-search/branching literature, leaving an important comparison gap.

---

Sources:
- [arXiv Abstract: Fission-GRPO](https://arxiv.org/abs/2601.15625)
- [arXiv HTML Full Paper](https://arxiv.org/html/2601.15625v1)
- [HuggingFace Paper Page](https://huggingface.co/papers/2601.15625)
- [Literature Review - Moonlight](https://www.themoonlight.io/en/review/robust-tool-use-via-fission-grpo-learning-to-recover-from-execution-errors)
- [Paper Notes by AkihikoWatanabe](https://github.com/AkihikoWatanabe/paper_notes/issues/4277)
- [RC-GRPO (related work)](https://arxiv.org/abs/2602.03025)
- [CLEANER (concurrent work)](https://arxiv.org/abs/2601.15141)
- [SeeUPO (concurrent work)](https://arxiv.org/abs/2602.06554)

agentId: a878e485d3c9127b8 (use SendMessage with to: 'a878e485d3c9127b8' to continue this agent)
&lt;usage>total_tokens: 30939
tool_uses: 19
duration_ms: 223166&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8c0c2de8-fbe8-414c-9e2b-c3ac1c4b153a",
  "isSidechain": false,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "type": "user",
  "uuid": "310bcee1-16c3-4e42-a6f9-b735fca75b77",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to deeply research the paper \"Fission-GRPO\" (arXiv:2601.15625). This is claimed to be an ACL 2026 paper titled \"Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors\" by Zhiwei Zhang et al.\n\nPlease:\n1. Use WebSearch to find this paper with queries like \"Fission-GRPO arXiv 2601.15625\", \"Fission-GRPO error recovery tool use GRPO\", and \"Fission GRPO ACL 2026\"\n2. Use WebFetch to read the actual paper abstract and method sections from arxiv.org\n3. Search for any follow-up work citing Fission-GRPO\n\nI need to understand:\n- What exactly is the \"fission\" mechanism? How does it create new training instances from failed trajectories?\n- What is the \"Error Simulator\" they train?\n- How do they resample G' parallel recovery attempts?\n- What benchmarks do they use? What are their main results?\n- Do they condition on error TYPE? Or just error occurrence?\n- How does their branching differ from tree-based branching (ARPO, Tree-GRPO)?\n- Is their code publicly available?\n\nReport all findings in detail. If the paper doesn't exist at that arXiv ID, report that clearly.",
    "agentId": "a878e485d3c9127b8",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive information. Here is the detailed research report.\n\n---\n\n## Detailed Research Report: Fission-GRPO (arXiv:2601.15625)\n\n### Paper Verification\n\nThe paper **does exist** at arXiv:2601.15625. It is confirmed as:\n\n- **Title:** \"Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors\"\n- **Authors:** Zhiwei Zhang, Fei Zhao, Rui Wang, Zezhong Wang, Bin Liang, Jiakang Wang, Yao Hu, Shaosheng Cao, Kam-Fai Wong\n- **Affiliations:** The Chinese University of Hong Kong (1) and Xiaohongshu Inc. (2)\n- **Submitted:** January 22, 2026 (v1); revised April 20, 2026 (v2)\n- **Conference:** **Accepted to ACL 2026 Main Conference** (confirmed on the arXiv abstract page)\n\n---\n\n### 1. What Exactly Is the \"Fission\" Mechanism?\n\nThe \"fission\" metaphor refers to splitting a single failed trajectory into multiple new training instances. The process operates in three stages within the GRPO training loop:\n\n**Stage 1 -- Standard GRPO Exploration:** For each query x, the model samples G rollouts (G=8 in their setup). Each rollout is scored by a composite reward function. Trajectories failing the error filter (R_corr < delta_corr OR R_fmt = 0) are flagged.\n\n**Stage 2 -- Error Augmentation:** Each failed trajectory tau_err is intercepted and augmented with diagnostic feedback f from the Error Simulator S_phi. The augmented context is constructed as: `x_corr = [x; tau_err; f]` (original query + failed tool call + simulated diagnostic feedback).\n\n**Stage 3 -- Fission Update:** Each augmented error context is \"fissioned\" -- expanded into G' parallel recovery attempts by resampling new rollouts on-policy from the current model conditioned on x_corr. So a single error becomes G' new training trajectories, each attempting recovery from that specific error state with the benefit of the diagnostic feedback.\n\nAll corrective samples are stored in a **LIFO (Last-In-First-Out) buffer** (B_corr), ensuring that the most recent errors (closest to the current policy) are consumed first during corrective updates. Deduplication is applied via hashing (x, tau_err) pairs to avoid redundant training on identical error patterns.\n\nThe fission update is triggered when the buffer accumulates sufficient samples (|B| >= B_trig). The paper investigates trigger frequency sensitivity in Section 4.5 and finds performance is stable for small-to-moderate intervals but degrades with overly sparse triggering.\n\n---\n\n### 2. The Error Simulator\n\nThe Error Simulator (S_phi) is a critical component that generates realistic, context-aware error feedback resembling actual runtime error traces.\n\n**Training data:** Approximately 2,000 instances distilled from error logs. Each instance contains:\n1. System prompt + tool specifications + dialogue state\n2. The model's failed tool call (tau_err)\n3. The ground-truth correct call (tau_gt)\n4. A teacher-written diagnostic message generated by Claude Sonnet 4, filtered for quality\n\n**Architecture:** Qwen3-32B fine-tuned via supervised fine-tuning (SFT).\n\n**Critical constraint -- No target leakage:** The simulator's outputs are explicitly restricted to \"non-revealing error descriptions\" (e.g., \"parameter status expects value OPEN\") rather than exposing the full correct tool call. This is essential -- if the simulator revealed the answer, the model would learn to pattern-match rather than reason about recovery.\n\n**Inference:** `f <- S_phi(x, tau_err, tau_gt)` -- it consumes the system prompt, tools, dialogue history, ground truth, and the failed attempt to produce concise diagnostic feedback.\n\n**Missing details:** The paper does not disclose the number of training epochs, learning rate, specific loss function, or validation metrics for the simulator training.\n\n---\n\n### 3. How G' Parallel Recovery Attempts Are Resampled\n\nThe resampling procedure (from Algorithm 1, lines 37-42) works as follows:\n\n1. Construct the augmented corrective context: `x_corr = [x; tau_err; f]`\n2. Sample G' new rollouts from the current policy: `{tau'_j}_{j=1}^{G'} ~ pi_theta(.|x_corr)`\n3. Compute rewards for each recovery trajectory\n4. Calculate corrective advantages using **within-group normalization**:\n   - mu'_R = (1/G') * sum(r'_j)\n   - sigma'_R = Std(r'_j)\n   - A'_j = (r'_j - mu'_R) / (sigma'_R + epsilon)\n5. Apply the corrective objective (Eq. 6): `J_corr(theta) = E_xcorr[(1/G') * sum_j A'(tau'_j) * grad log pi_theta(tau'_j|x_corr)]`\n\nThis is a standard GRPO-style clipped objective with KL penalty, applied over the corrective distribution. The innovation is not a novel loss function but rather the **contextual conditioning** (on error + feedback) and **multiplicative resampling** (one error becomes G' training signals).\n\nThe authors note that conditioning on explicit feedback f \"typically increases outcome diversity within the fission group, improving the usefulness of advantage estimates for recovery updates.\"\n\n---\n\n### 4. Benchmarks and Main Results\n\n**Benchmark:** Evaluation is **exclusively on BFCL v4 Multi-Turn**. The authors chose this because it features an \"interactive error feedback mechanism: upon execution error, the environment provides explicit error traces and permits the agent up to 20 retries.\" The limitations section explicitly acknowledges this narrow evaluation scope.\n\n**Primary Results (Table 1):**\n\n| Model | Method | Overall Accuracy |\n|---|---|---|\n| Qwen3-8B | GRPO | 42.75% |\n| Qwen3-8B | DAPO | ~41-42% |\n| Qwen3-8B | Dr.GRPO | ~42-43% |\n| Qwen3-8B | **Fission-GRPO** | **46.75%** |\n| ToolACE-2-8B | Specialized | 37.00% |\n| BitAgent-8B | Specialized | 37.75% |\n\nResults are consistent across the Qwen3 family (1.7B, 4B, 8B), with Fission-GRPO outperforming all baselines at every scale.\n\n**Error Recovery Analysis (Figure 3):**\n- Average error recovery rate improvement: **+5.7%** across categories\n- Long Context category: **+11.8%** improvement (most dramatic)\n- One-shot success (getting it right on the first try) is also preserved/improved: **+1.75%** average\n\nThe abstract mentions \"gains up to 17.4% on additional benchmarks\" but the paper body evaluates only BFCL v4 Multi-Turn; this 17.4% figure likely refers to a specific error-category sub-split rather than a separate benchmark.\n\n---\n\n### 5. Error Type Conditioning\n\nFission-GRPO conditions on **error occurrence + diagnostic feedback content**, **not** on explicit error type categories. The error filter uses a two-level check:\n- **Format validity** (R_fmt): Binary {0,1} -- is the output a well-formed tool call?\n- **Functional correctness** (R_corr): Scalar threshold (delta_corr = 1) -- did the call do the right thing?\n\nHowever, the resampling uses a **unified augmented context** `[x; tau_err; f]` without any explicit error-type labeling or categorization. The diagnostic feedback f implicitly encodes information about what went wrong, but there is no taxonomy of error types that conditions different recovery strategies.\n\n---\n\n### 6. How Branching Differs from Tree-Based Approaches (ARPO, Tree-GRPO)\n\nThis is a notable gap in the paper. The Related Work section (Section 2) **does not discuss tree-based methods, MCTS approaches, ARPO, or Tree-GRPO at all**. The authors position their work against:\n- Standard RL baselines (GRPO, DAPO, Dr.GRPO)\n- Static error-correction datasets (ToolACE, LoopTool)\n\nBased on the technical details, the key architectural distinctions from tree-based approaches are:\n\n1. **Targeted vs. exhaustive branching:** Tree-based methods (like MCTS or Tree-GRPO) branch at decision points to explore the full action space. Fission-GRPO branches **only at error points**, focusing computational budget specifically on diagnosed failure states.\n\n2. **Simulator-augmented context:** Tree-based methods typically branch with the same context. Fission-GRPO augments the context with diagnostic feedback before branching, providing the model additional information about what went wrong.\n\n3. **On-policy error alignment:** The LIFO buffer ensures the model trains on errors from its current policy distribution, not from a static exploration tree. As the policy improves, the error distribution shifts, and the fission targets shift with it.\n\n4. **No backtracking:** Unlike tree search which explores alternative paths from earlier states, Fission-GRPO always conditions on the full failed trajectory plus feedback -- it's forward-looking recovery, not backward-looking exploration.\n\n5. **Flat structure:** There is no tree data structure or recursive branching. Each error produces exactly one \"fission group\" of G' parallel attempts at the same level.\n\n---\n\n### 7. Reward Function Design\n\nThe composite reward R(tau, t) has three components with time-annealing weights:\n\n1. **Format Compliance (R_fmt):** Binary {0,1}. Weight w_fmt(t) decays from 2 to 1 over training.\n2. **Functional Correctness (R_corr):** Range [0,2]. Computed as `R_corr = alpha * I(N=N*) + (1-alpha) * (1/|M|) * sum F1(a, a*)` where I(N=N*) checks correct function selection and F1 measures token-level overlap on matched parameters. Weight w_corr(t) increases from 2 to 3.\n3. **Efficiency Regularization (R_len):** Range [0,1] via piecewise Gaussian with time-annealing.\n\nThe dynamic weighting shifts focus \"from syntax to semantics as training progresses.\"\n\n---\n\n### 8. Ablation Studies\n\n**Table 2 -- Feedback Quality Ablation (Qwen3-8B):**\n\n| Configuration | Overall Accuracy | Delta |\n|---|---|---|\n| GRPO baseline | 42.75% | -- |\n| Fission-Static (generic error message) | 44.00% | +1.25% |\n| Fission-Dynamic (learned Error Simulator) | 46.75% | +4.00% |\n\nThe +2.75% gap between Static and Dynamic demonstrates that the Error Simulator's precise, context-aware diagnostics are substantially more useful than generic \"error occurred\" messages. However, even generic feedback provides some benefit (+1.25%).\n\n**Section 4.5 -- Trigger Frequency:** Performance is stable for small N (frequent fission triggers) but degrades with sparse updates (large N). The Miss Param and Long Context error categories are most sensitive to trigger frequency.\n\n---\n\n### 9. Code Availability\n\n**No code has been released.** The paper contains no mention of a GitHub repository, code release, or open-source plans. No repository was found through GitHub searches. The authors do provide detailed hyperparameters (learning rate 1e-6, batch size 8, G=8, max prompt 12,800 tokens, max response 4,096 tokens) and Algorithm 1 pseudocode.\n\n---\n\n### 10. Follow-Up Work and Citations\n\nGiven the paper was posted in January 2026 (approximately 4 months ago), I was unable to find a specific citation count. Related concurrent work in the same space includes:\n\n- **RC-GRPO** (arXiv:2602.03025) -- \"Reward-Conditioned GRPO for Multi-Turn Tool Calling Agents\" -- addresses a similar problem (vanishing updates in multi-turn GRPO) but via reward-conditioned trajectory generation rather than error-augmented fission. It does not appear to cite Fission-GRPO directly.\n- **CLEANER** (arXiv:2601.15141) -- \"Self-Purified Trajectories Boost Agentic Reinforcement Learning\" -- a concurrent paper addressing error-contaminated trajectories via retrospective replacement rather than forward recovery.\n- **SeeUPO** (arXiv:2602.06554) -- \"Sequence-Level Agentic-RL with Convergence Guarantees\" -- also evaluated on BFCL v4, focuses on training stability via sequential updates rather than error recovery specifically.\n\n---\n\n### Known Limitations and Criticisms\n\nFrom the literature review and the paper's own discussion:\n\n1. **Simulator dependency:** Requires ~2K teacher-written error instances (generated via Claude Sonnet 4); scalability to new tool domains is unclear.\n2. **Threshold sensitivity:** Error identification depends on tunable delta_corr; sensitivity analysis is limited.\n3. **Single benchmark:** Evaluated only on BFCL v4 Multi-Turn; generalization to other tool-use benchmarks, code execution, or web interaction is untested.\n4. **Computational overhead:** Multiplicative resampling (G' extra rollouts per error) increases training cost, though the paper does not quantify this overhead.\n5. **No tree-based comparison:** The paper does not engage with the tree-search/branching literature, leaving an important comparison gap.\n\n---\n\nSources:\n- [arXiv Abstract: Fission-GRPO](https://arxiv.org/abs/2601.15625)\n- [arXiv HTML Full Paper](https://arxiv.org/html/2601.15625v1)\n- [HuggingFace Paper Page](https://huggingface.co/papers/2601.15625)\n- [Literature Review - Moonlight](https://www.themoonlight.io/en/review/robust-tool-use-via-fission-grpo-learning-to-recover-from-execution-errors)\n- [Paper Notes by AkihikoWatanabe](https://github.com/AkihikoWatanabe/paper_notes/issues/4277)\n- [RC-GRPO (related work)](https://arxiv.org/abs/2602.03025)\n- [CLEANER (concurrent work)](https://arxiv.org/abs/2601.15141)\n- [SeeUPO (concurrent work)](https://arxiv.org/abs/2602.06554)"
      }
    ],
    "totalDurationMs": 223166,
    "totalTokens": 30939,
    "totalToolUseCount": 19,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2276,
      "cache_read_input_tokens": 25058,
      "output_tokens": 3604,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2276
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3604,
          "cache_read_input_tokens": 25058,
          "cache_creation_input_tokens": 2276,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2276,
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
      "otherToolCount": 19
    }
  },
  "sourceToolAssistantUUID": "8c0c2de8-fbe8-414c-9e2b-c3ac1c4b153a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 19_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-11 (UTC).**  ## Original idea {   \"title\": \"Error-Type-Conditioned Branching GRPO for Self-Supervised Agent Recove…",
  "leafUuid": "310bcee1-16c3-4e42-a6f9-b735fca75b77",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "Error-type-aware branching for agent recovery beyond Fission-GRPO",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c"
}
```

---

### Tool result

_source line 21 · 2026-05-11T23:32:43.855Z_

<details><summary>↩ Tool result · `toolu_014WkDQZ8VmPCKLHsU487cAs`</summary>

```text
Now I have comprehensive data. Let me compile the full research report.

---

# StableToolBench Error Patterns and Diversity: Detailed Research Findings

## 1. API Failure Rates: Original ToolBench vs. StableToolBench

### Original ToolBench Failure Rate
The original ToolBench suffers from severe instability. A systematic evaluation found that **55.6% of APIs are unstable**, with only **44.4% of API calls succeeding consistently** (7,311 out of 16,464 APIs). The breakdown of the 55.6% unstable APIs:

- **Not Available: 49.2%** (8,095 APIs), further subdivided:
  - Parsing Error: 52.6% of unavailable APIs
  - Not Connectable: 30.0%
  - Parameter Change: 7.3%
  - Not Found: 7.2%
  - Other: 3.1%
- **Not Authorized: 6.4%** (1,058 APIs)

When researchers attempted to reproduce ToolBench results months after original publication, ChatGPT+CoT showed a **32.5% drop in pass rate** and ToolLLaMA v2+DFS showed a **40.4% decline**, demonstrating the severity of the instability problem.

### StableToolBench's Virtual API Server
StableToolBench dramatically reduces failures through a hierarchical fallback system:

1. **Cache lookup** (composite key: category + tool + API name + arguments) -- 164,980 cached items after filtering
2. **Real API call** (if cache miss)
3. **API simulator** (GPT-4-turbo powered, if real API fails) using documentation + up to 5 real call examples as few-shot prompts
4. **All responses cached** regardless of source

**Cache hit rates**: For in-domain methods (e.g., GPT-3.5 Turbo 0613 + CoT/DFS), the cache hit rate is **96.7-97.0%**, meaning the simulator is rarely invoked. For out-of-domain methods, cache hit rates drop to ~75.8% (cache miss rate ~24.2%).

The paper demonstrated that even when **50% of real APIs are manually disabled**, model performance changes remain "within the range of variance" -- confirming the virtual server absorbs failures effectively.

## 2. Error Types the Virtual API Server Produces

The virtual API server produces responses in the format `{"error": "", "response": "..."}`. The error landscape is fundamentally transformed compared to real APIs:

**Errors that are preserved/simulated:**
- Parameter-related failures (incorrect/missing arguments)
- Documentation-violating requests

**Errors that are eliminated or suppressed:**
- Connection timeouts and DNS failures
- HTTP 5xx server errors
- Authentication/authorization failures (401/403)
- Rate limiting (429)
- API deprecation/removal errors
- Transient network errors

The simulator response format means the agent always gets a well-formed JSON response, even when the "real" API would have returned a raw HTTP error, a connection timeout, or no response at all.

## 3. Does StableToolBench's Caching/Simulation Reduce Error Diversity?

**Yes, substantially.** The evidence is clear from multiple angles:

**a) Cache dominance eliminates most error encounters.** With 96.7-97% cache hit rates for in-domain methods, agents almost never encounter real API failures. They receive the same cached response each time, which ensures reproducibility but eliminates the stochastic error landscape of real APIs.

**b) The simulator does not reproduce operational failures.** The MirrorAPI paper (the successor to GPT-4-turbo as simulator) explicitly acknowledges: *"Real API requests often fail in practical environments due to issues such as connectivity problems. While it is crucial for a tool-using model to effectively handle such failures, this aspect is not addressed in our project."* MirrorAPI's training data intentionally includes ~10,000 unsuccessful calls, but these are limited to **parameter-related issues** -- not connectivity, timeout, rate-limit, or server errors.

**c) Diversity testing showed limited variation.** The StableToolBench paper tested whether simulated outputs were diverse enough: only 2 of 60 sampled APIs returned identical responses across multiple calls. While this suggests some output diversity, it does not measure error-type diversity.

**d) The error taxonomy is narrowed.** In the real ToolBench, agents encounter a rich (if chaotic) distribution: connection errors, auth errors, parsing errors, parameter changes, 404s, timeouts, rate limits, malformed responses. In StableToolBench, the agent essentially sees either: (1) a cached successful response, (2) a cached error response, or (3) a simulator-generated response that follows documentation constraints. The entire class of infrastructure/operational errors is absent.

## 4. Papers Reporting Per-Error-Type Statistics on StableToolBench

**No paper was found that reports per-error-type statistics specifically on StableToolBench's virtual API server outputs.** The StableToolBench paper itself reports error statistics only for the **original ToolBench** (the 44.4%/49.2%/6.4% breakdown). It does not break down what types of errors the virtual server produces during evaluation, because the virtual server's design goal is to minimize/eliminate errors, not to characterize them.

However, several related works provide relevant error taxonomies:

### ToolScan (arXiv:2411.13547)
Defines **7 error patterns** in LLM tool-use (focused on agent-side errors, not API-side):
1. **Insufficient API Calls (IAC)** -- most prevalent failure
2. **Incorrect Argument Value (IAV)**
3. **Incorrect Argument Name (IAN)** -- hallucination
4. **Incorrect Argument Type (IAT)**
5. **Repeated API Calls (RAC)** -- especially in smaller models
6. **Incorrect Function Name (IFN)** -- hallucination
7. **Invalid Format Error (IFE)**

GPT-4 achieves 0.73 success rate; weaker models like Vicuna-13B drop to 0.16. Error profiles differ significantly across models even at similar overall performance.

### PALADIN (arXiv:2509.25238)
Catalogs tool failure types aligned with ToolScan's taxonomy plus **HTTP/API errors**: 400/422 (malformed), 401/403/407 (auth), 404 (not found), 500/503 (server), timeouts, DNS failures, rate limiting (429), JSON parsing failures. Trains on 50,000+ recovery-annotated trajectories with systematic failure injection. Improves recovery rate from 32.76% to 89.68% on ToolBench.

### API-Bank
Reports 6 error types with distribution: No API Call (36.77%), False API Format (23.65%), API Hallucination (15.93%), Invalid Input Parameters (7.96%), Miss Input Parameters (1.17%).

### AgentProcessBench (arXiv:2603.14465)
Reports error step ratios varying by dataset: HotPotQA 64.6%, GAIA 62.6%, BFCL 31.9%, tau-bench 48.0%. Identifies that QA tasks fail from initial reasoning errors while tool-heavy tasks fail later from policy violations.

## 5. Alternative Benchmarks with Richer Natural Error Distributions

Based on the research, several benchmarks offer richer or more realistic error landscapes:

### BFCL V4 Agentic (Berkeley Function Calling Leaderboard)
The strongest candidate for natural error diversity. BFCL V4 **injects six common programmatic access errors** (503 Server Error, 429 Too Many Requests, 403 Forbidden, etc.) randomly into multi-turn tool-calling scenarios. It explicitly evaluates **error recovery** as a core capability. 665 test cases across web search and memory tasks.

### tau-bench / tau2-bench
Emulates dynamic customer-service conversations (retail and airline domains) with domain-specific API tools and policy guidelines. Even GPT-4o succeeds on <50% of tasks; pass^8 reliability <25% in retail. Failures emerge naturally from complex reasoning over databases, ad-hoc policy compliance, and compound request handling. While not focused on API infrastructure errors, it produces rich agent-level failures.

### PALADIN's Failure Injection Framework
Not a benchmark per se, but a **systematic failure injection pipeline** that deterministically injects error type, manifestation mechanism (malformed output, silent failure), and turn index into ToolBench trajectories. Uses a GPT-5 "Teacher" to generate recovery demonstrations. The 55+ failure exemplar bank aligned to ToolScan's taxonomy represents the most structured error-conditioning resource found.

### ToolReflection
Self-generates error trajectories and corrections for training. Shows 25.4% improvement on GPT4Tools-OOD, 56.2% on GPT4Tools-OOD-Hard, and 10.5% on ToolAlpaca Real-world. Specifically targets recovery from incorrect tool calls with incomplete or erroneous API documentation.

### Original ToolBench (with real APIs)
Paradoxically, the original ToolBench with live RapidAPI calls provides the **richest natural error distribution** -- 55.6% of APIs produce diverse, unpredictable failures including timeouts, auth failures, deprecation, parameter drift, and rate limits. The problem is that this distribution is non-reproducible and changes daily.

## 6. Feasibility Assessment for Error-Type-Conditioned Training

Based on these findings, here are the key considerations:

**Challenges with StableToolBench:**
- The virtual API server **deliberately suppresses error diversity** -- that is its core design goal
- Cache hit rates of 96-97% mean agents almost never encounter real errors during evaluation
- The simulator does not produce connectivity, timeout, auth, or server errors
- No existing paper reports per-error-type statistics from StableToolBench evaluations
- MirrorAPI explicitly acknowledges it does not handle operational/connectivity failures

**More promising approaches:**
- **PALADIN's failure injection + ToolScan taxonomy** provides the most structured framework for error-type-conditioned training, with 7 well-defined error categories and 55+ exemplars
- **BFCL V4's randomized error injection** (6 HTTP error types) provides a controlled but realistic error landscape
- **ToolReflection's self-generated error data** demonstrates that training on error-correction pairs improves robustness significantly
- **Hybrid approach**: Use StableToolBench for the base tool-use task structure, but overlay PALADIN-style systematic failure injection to create controlled error-type-conditioned training data with known error distributions

**Key gap:** No existing work systematically conditions training on a full taxonomy of both agent-side errors (ToolScan's 7 types) AND API-side errors (HTTP errors, timeouts, malformed responses, auth failures) simultaneously. This represents an open opportunity.

Sources:
- [StableToolBench Paper (arXiv:2403.07714)](https://arxiv.org/abs/2403.07714)
- [StableToolBench HTML](https://arxiv.org/html/2403.07714v1)
- [StableToolBench GitHub](https://github.com/THUNLP-MT/StableToolBench)
- [StableToolBench Project Page](https://zhichengg.github.io/stb.github.io/)
- [StableToolBench-MirrorAPI (arXiv:2503.20527)](https://arxiv.org/abs/2503.20527)
- [ToolScan (arXiv:2411.13547)](https://arxiv.org/abs/2411.13547)
- [PALADIN (arXiv:2509.25238)](https://arxiv.org/abs/2509.25238)
- [AgentProcessBench (arXiv:2603.14465)](https://arxiv.org/html/2603.14465v1)
- [Where LLM Agents Fail (arXiv:2509.25370)](https://arxiv.org/abs/2509.25370)
- [ToolReflection (ACL Anthology)](https://aclanthology.org/2025.realm-1.14/)
- [API-Bank (EMNLP 2023)](https://aclanthology.org/2023.emnlp-main.187/)
- [BFCL V4 Agentic](https://gorilla.cs.berkeley.edu/leaderboard.html)
- [tau-bench (arXiv:2406.12045)](https://arxiv.org/abs/2406.12045)
- [ToolBench / ToolLLM (ICLR 2024)](https://openreview.net/forum?id=dHng2O0Jjr)
- [ToolBench Evaluation Overview](https://www.emergentmind.com/topics/toolbench-evaluation)

agentId: ac49be575f1d4259f (use SendMessage with to: 'ac49be575f1d4259f' to continue this agent)
&lt;usage>total_tokens: 38852
tool_uses: 27
duration_ms: 210264&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f9cb14f3-f161-40fb-bf78-4d552b1330ab",
  "isSidechain": false,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "type": "user",
  "uuid": "aa477e23-95ea-4193-b86d-53572a4d8fa5",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to research the actual error patterns and diversity in StableToolBench to assess feasibility of error-type-conditioned training.\n\nPlease:\n1. Use WebSearch with queries like \"StableToolBench error analysis\", \"StableToolBench virtual API server errors\", \"StableToolBench Qwen error types\"\n2. Search for \"StableToolBench GitHub\" to find the actual codebase and check error handling\n3. Use WebFetch to read the StableToolBench paper (arXiv:2403.07714) focusing on their virtual API server design and what kinds of errors occur\n4. Search for papers that evaluate on StableToolBench and report error statistics\n5. Search for \"ToolBench error analysis\" or \"tool-use LLM error distribution\"\n\nI need to understand:\n- What fraction of API calls fail on StableToolBench vs original ToolBench?\n- What types of errors does the virtual API server produce?\n- Does StableToolBench's caching/simulation actually reduce error diversity compared to real APIs?\n- Are there papers reporting per-error-type statistics on StableToolBench?\n- What alternative benchmarks have richer natural error distributions for tool-use agents?\n\nReport all findings in detail.",
    "agentId": "ac49be575f1d4259f",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive data. Let me compile the full research report.\n\n---\n\n# StableToolBench Error Patterns and Diversity: Detailed Research Findings\n\n## 1. API Failure Rates: Original ToolBench vs. StableToolBench\n\n### Original ToolBench Failure Rate\nThe original ToolBench suffers from severe instability. A systematic evaluation found that **55.6% of APIs are unstable**, with only **44.4% of API calls succeeding consistently** (7,311 out of 16,464 APIs). The breakdown of the 55.6% unstable APIs:\n\n- **Not Available: 49.2%** (8,095 APIs), further subdivided:\n  - Parsing Error: 52.6% of unavailable APIs\n  - Not Connectable: 30.0%\n  - Parameter Change: 7.3%\n  - Not Found: 7.2%\n  - Other: 3.1%\n- **Not Authorized: 6.4%** (1,058 APIs)\n\nWhen researchers attempted to reproduce ToolBench results months after original publication, ChatGPT+CoT showed a **32.5% drop in pass rate** and ToolLLaMA v2+DFS showed a **40.4% decline**, demonstrating the severity of the instability problem.\n\n### StableToolBench's Virtual API Server\nStableToolBench dramatically reduces failures through a hierarchical fallback system:\n\n1. **Cache lookup** (composite key: category + tool + API name + arguments) -- 164,980 cached items after filtering\n2. **Real API call** (if cache miss)\n3. **API simulator** (GPT-4-turbo powered, if real API fails) using documentation + up to 5 real call examples as few-shot prompts\n4. **All responses cached** regardless of source\n\n**Cache hit rates**: For in-domain methods (e.g., GPT-3.5 Turbo 0613 + CoT/DFS), the cache hit rate is **96.7-97.0%**, meaning the simulator is rarely invoked. For out-of-domain methods, cache hit rates drop to ~75.8% (cache miss rate ~24.2%).\n\nThe paper demonstrated that even when **50% of real APIs are manually disabled**, model performance changes remain \"within the range of variance\" -- confirming the virtual server absorbs failures effectively.\n\n## 2. Error Types the Virtual API Server Produces\n\nThe virtual API server produces responses in the format `{\"error\": \"\", \"response\": \"...\"}`. The error landscape is fundamentally transformed compared to real APIs:\n\n**Errors that are preserved/simulated:**\n- Parameter-related failures (incorrect/missing arguments)\n- Documentation-violating requests\n\n**Errors that are eliminated or suppressed:**\n- Connection timeouts and DNS failures\n- HTTP 5xx server errors\n- Authentication/authorization failures (401/403)\n- Rate limiting (429)\n- API deprecation/removal errors\n- Transient network errors\n\nThe simulator response format means the agent always gets a well-formed JSON response, even when the \"real\" API would have returned a raw HTTP error, a connection timeout, or no response at all.\n\n## 3. Does StableToolBench's Caching/Simulation Reduce Error Diversity?\n\n**Yes, substantially.** The evidence is clear from multiple angles:\n\n**a) Cache dominance eliminates most error encounters.** With 96.7-97% cache hit rates for in-domain methods, agents almost never encounter real API failures. They receive the same cached response each time, which ensures reproducibility but eliminates the stochastic error landscape of real APIs.\n\n**b) The simulator does not reproduce operational failures.** The MirrorAPI paper (the successor to GPT-4-turbo as simulator) explicitly acknowledges: *\"Real API requests often fail in practical environments due to issues such as connectivity problems. While it is crucial for a tool-using model to effectively handle such failures, this aspect is not addressed in our project.\"* MirrorAPI's training data intentionally includes ~10,000 unsuccessful calls, but these are limited to **parameter-related issues** -- not connectivity, timeout, rate-limit, or server errors.\n\n**c) Diversity testing showed limited variation.** The StableToolBench paper tested whether simulated outputs were diverse enough: only 2 of 60 sampled APIs returned identical responses across multiple calls. While this suggests some output diversity, it does not measure error-type diversity.\n\n**d) The error taxonomy is narrowed.** In the real ToolBench, agents encounter a rich (if chaotic) distribution: connection errors, auth errors, parsing errors, parameter changes, 404s, timeouts, rate limits, malformed responses. In StableToolBench, the agent essentially sees either: (1) a cached successful response, (2) a cached error response, or (3) a simulator-generated response that follows documentation constraints. The entire class of infrastructure/operational errors is absent.\n\n## 4. Papers Reporting Per-Error-Type Statistics on StableToolBench\n\n**No paper was found that reports per-error-type statistics specifically on StableToolBench's virtual API server outputs.** The StableToolBench paper itself reports error statistics only for the **original ToolBench** (the 44.4%/49.2%/6.4% breakdown). It does not break down what types of errors the virtual server produces during evaluation, because the virtual server's design goal is to minimize/eliminate errors, not to characterize them.\n\nHowever, several related works provide relevant error taxonomies:\n\n### ToolScan (arXiv:2411.13547)\nDefines **7 error patterns** in LLM tool-use (focused on agent-side errors, not API-side):\n1. **Insufficient API Calls (IAC)** -- most prevalent failure\n2. **Incorrect Argument Value (IAV)**\n3. **Incorrect Argument Name (IAN)** -- hallucination\n4. **Incorrect Argument Type (IAT)**\n5. **Repeated API Calls (RAC)** -- especially in smaller models\n6. **Incorrect Function Name (IFN)** -- hallucination\n7. **Invalid Format Error (IFE)**\n\nGPT-4 achieves 0.73 success rate; weaker models like Vicuna-13B drop to 0.16. Error profiles differ significantly across models even at similar overall performance.\n\n### PALADIN (arXiv:2509.25238)\nCatalogs tool failure types aligned with ToolScan's taxonomy plus **HTTP/API errors**: 400/422 (malformed), 401/403/407 (auth), 404 (not found), 500/503 (server), timeouts, DNS failures, rate limiting (429), JSON parsing failures. Trains on 50,000+ recovery-annotated trajectories with systematic failure injection. Improves recovery rate from 32.76% to 89.68% on ToolBench.\n\n### API-Bank\nReports 6 error types with distribution: No API Call (36.77%), False API Format (23.65%), API Hallucination (15.93%), Invalid Input Parameters (7.96%), Miss Input Parameters (1.17%).\n\n### AgentProcessBench (arXiv:2603.14465)\nReports error step ratios varying by dataset: HotPotQA 64.6%, GAIA 62.6%, BFCL 31.9%, tau-bench 48.0%. Identifies that QA tasks fail from initial reasoning errors while tool-heavy tasks fail later from policy violations.\n\n## 5. Alternative Benchmarks with Richer Natural Error Distributions\n\nBased on the research, several benchmarks offer richer or more realistic error landscapes:\n\n### BFCL V4 Agentic (Berkeley Function Calling Leaderboard)\nThe strongest candidate for natural error diversity. BFCL V4 **injects six common programmatic access errors** (503 Server Error, 429 Too Many Requests, 403 Forbidden, etc.) randomly into multi-turn tool-calling scenarios. It explicitly evaluates **error recovery** as a core capability. 665 test cases across web search and memory tasks.\n\n### tau-bench / tau2-bench\nEmulates dynamic customer-service conversations (retail and airline domains) with domain-specific API tools and policy guidelines. Even GPT-4o succeeds on <50% of tasks; pass^8 reliability <25% in retail. Failures emerge naturally from complex reasoning over databases, ad-hoc policy compliance, and compound request handling. While not focused on API infrastructure errors, it produces rich agent-level failures.\n\n### PALADIN's Failure Injection Framework\nNot a benchmark per se, but a **systematic failure injection pipeline** that deterministically injects error type, manifestation mechanism (malformed output, silent failure), and turn index into ToolBench trajectories. Uses a GPT-5 \"Teacher\" to generate recovery demonstrations. The 55+ failure exemplar bank aligned to ToolScan's taxonomy represents the most structured error-conditioning resource found.\n\n### ToolReflection\nSelf-generates error trajectories and corrections for training. Shows 25.4% improvement on GPT4Tools-OOD, 56.2% on GPT4Tools-OOD-Hard, and 10.5% on ToolAlpaca Real-world. Specifically targets recovery from incorrect tool calls with incomplete or erroneous API documentation.\n\n### Original ToolBench (with real APIs)\nParadoxically, the original ToolBench with live RapidAPI calls provides the **richest natural error distribution** -- 55.6% of APIs produce diverse, unpredictable failures including timeouts, auth failures, deprecation, parameter drift, and rate limits. The problem is that this distribution is non-reproducible and changes daily.\n\n## 6. Feasibility Assessment for Error-Type-Conditioned Training\n\nBased on these findings, here are the key considerations:\n\n**Challenges with StableToolBench:**\n- The virtual API server **deliberately suppresses error diversity** -- that is its core design goal\n- Cache hit rates of 96-97% mean agents almost never encounter real errors during evaluation\n- The simulator does not produce connectivity, timeout, auth, or server errors\n- No existing paper reports per-error-type statistics from StableToolBench evaluations\n- MirrorAPI explicitly acknowledges it does not handle operational/connectivity failures\n\n**More promising approaches:**\n- **PALADIN's failure injection + ToolScan taxonomy** provides the most structured framework for error-type-conditioned training, with 7 well-defined error categories and 55+ exemplars\n- **BFCL V4's randomized error injection** (6 HTTP error types) provides a controlled but realistic error landscape\n- **ToolReflection's self-generated error data** demonstrates that training on error-correction pairs improves robustness significantly\n- **Hybrid approach**: Use StableToolBench for the base tool-use task structure, but overlay PALADIN-style systematic failure injection to create controlled error-type-conditioned training data with known error distributions\n\n**Key gap:** No existing work systematically conditions training on a full taxonomy of both agent-side errors (ToolScan's 7 types) AND API-side errors (HTTP errors, timeouts, malformed responses, auth failures) simultaneously. This represents an open opportunity.\n\nSources:\n- [StableToolBench Paper (arXiv:2403.07714)](https://arxiv.org/abs/2403.07714)\n- [StableToolBench HTML](https://arxiv.org/html/2403.07714v1)\n- [StableToolBench GitHub](https://github.com/THUNLP-MT/StableToolBench)\n- [StableToolBench Project Page](https://zhichengg.github.io/stb.github.io/)\n- [StableToolBench-MirrorAPI (arXiv:2503.20527)](https://arxiv.org/abs/2503.20527)\n- [ToolScan (arXiv:2411.13547)](https://arxiv.org/abs/2411.13547)\n- [PALADIN (arXiv:2509.25238)](https://arxiv.org/abs/2509.25238)\n- [AgentProcessBench (arXiv:2603.14465)](https://arxiv.org/html/2603.14465v1)\n- [Where LLM Agents Fail (arXiv:2509.25370)](https://arxiv.org/abs/2509.25370)\n- [ToolReflection (ACL Anthology)](https://aclanthology.org/2025.realm-1.14/)\n- [API-Bank (EMNLP 2023)](https://aclanthology.org/2023.emnlp-main.187/)\n- [BFCL V4 Agentic](https://gorilla.cs.berkeley.edu/leaderboard.html)\n- [tau-bench (arXiv:2406.12045)](https://arxiv.org/abs/2406.12045)\n- [ToolBench / ToolLLM (ICLR 2024)](https://openreview.net/forum?id=dHng2O0Jjr)\n- [ToolBench Evaluation Overview](https://www.emergentmind.com/topics/toolbench-evaluation)"
      }
    ],
    "totalDurationMs": 210264,
    "totalTokens": 38852,
    "totalToolUseCount": 27,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5016,
      "cache_read_input_tokens": 30711,
      "output_tokens": 3124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5016
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3124,
          "cache_read_input_tokens": 30711,
          "cache_creation_input_tokens": 5016,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5016,
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
      "otherToolCount": 27
    }
  },
  "sourceToolAssistantUUID": "f9cb14f3-f161-40fb-bf78-4d552b1330ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-11T23:34:21.024Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have comprehensive information on all the key papers. Let me synthesize and think deeply about the situation:

## Key Findings

### Fission-GRPO (ACL 2026)
- **Does exist** and is accepted at ACL 2026
- Fissions failed trajectories by augmenting with diagnostic feedback from a trained Error Simulator, then resamples G' recovery attempts
- Uses Qwen3-8B on BFCL v4 Multi-Turn
- +5.7% error recovery rate improvement
- **Does NOT condition on error TYPE** — uses a unified augmented context without error taxonomy


- Requires training an Error Simulator on ~2K teacher-written examples from Claude Sonnet 4, with no code released, and doesn't explore tree-based branching approaches like ARPO or Tree-GRPO

### Stratified GRPO (arXiv, ICLR 2026 submission — status unclear)
- **Does exist** and partitions trajectories by structural strata (number of search calls) while normalizing advantages within each stratum
- Applied to search agents on QA tasks rather than tool-use or recovery scenarios, tested only on Qwen-2.5-3B
- Provides formal theoretical analysis of cross-stratum bias and establishes a general mechanism for stratified normalization, though it targets search-structure strata rather than error-type strata

### CoBA-RL
- **Does exist** as a beta distribution-based adaptive budget allocation method for GRPO
- Applied to math reasoning with DAPO-Math-17K, outperforming Knapsack RL by allocating budgets based on task difficulty rather than error types

### RC-GRPO
- **Does exist** and uses reward-conditioned trajectory generation to maintain within-group variance in GRPO
- Applied to multi-turn tool calling on BFCL v4, achieving 85% on Qwen2.5-7B compared to 48.75% for SFT+GRPO, addressing the complementary problem of variance collapse

### StableToolBench Error Diversity
- **Critically suppresses error diversity** with 96-97% cache hit rates, since the virtual API server doesn't produce connectivity, timeout, auth, or server errors, and MirrorAPI explicitly doesn't handle operational failures
- This is a fundamental feasibility concern for the original idea, making BFCL v4 a much better fit since it deliberately injects 6 error types

## Deep Thinking: Does the Idea Survive?

Now I'm checking the core assumptions against what I've found. The original idea assumed no existing method combines error-triggered branching with GRPO for recovery, but Fission-GRPO invalidates that. The assumption about error-type-stratified advantage normalization being novel is partially invalidated by Stratified GRPO, which has the general mechanism even if not applied to error types specifically. I need to assess whether the core idea still holds up.

Looking at what actually remains novel: error-type-conditioned budget allocation where K_τ scales inversely with pilot recovery rates is something Fission-GRPO doesn't do with their uniform resampling approach. The systematic per-type analysis of recovery behaviors is still empirically novel, even if the stratification mechanism itself isn't entirely new.

But there's a fundamental problem with the StableToolBench foundation — it's explicitly designed to suppress errors, so the pilot run won't generate the diverse error types needed for meaningful conditioning. This undermines the whole premise. BFCL v4 would be much better since it deliberately injects six error types with built-in recovery evaluation, though that's what Fission-GRPO already uses. The core research question about whether error-type conditioning improves GRPO for recovery is still valid and unanswered, so this feels like a major revision rather than a complete pivot.

The repositioning is significant though: I need to build directly on Fission-GRPO's foundation instead of claiming to work at the intersection of two approaches. The key insight is that Fission-GRPO uses uniform resampling budgets across all error types, but harder errors might benefit from more recovery branches. So the contribution becomes error-type-conditioned budget allocation paired with stratified advantage normalization applied to error categories, evaluated on BFCL v4 or a version of StableToolBench with deliberate error injection.

But there's a real tension here—if I remove the Error Simulator that Fission-GRPO relies on, I lose the diagnostic feedback that showed a +2.75% improvement over static feedback, which could actually make the method worse despite the type conditioning. So instead of cutting the error feedback entirely, I should keep it but add error-type conditioning on top. The story then is: Fission-GRPO works with uniform budgets, but different error types have different recovery difficulty, so conditioning the budget allocation and advantage normalization by error type should improve performance. This is narrower than my original framing, but it's more defensible.

For a short EMNLP paper, I could position this as a systematic empirical study combining error-type-conditioned budget allocation with stratified advantages for recovery training. The key is showing that type conditioning actually matters—that's where the contribution lies.

Looking at the methodological differences, I'm realizing the zero-annotation angle is actually stronger than I initially thought. Fission-GRPO requires thousands of teacher-written error instances, whereas our approach works directly with raw error signals, making it more practical even if we lose some of the simulator's benefits. The real story is comparing type-conditioned versus uniform versus entropy-triggered branching strategies and demonstrating which error types benefit most from RL-based recovery versus SFT-based relabeling.

For the benchmark, BFCL v4 makes sense for direct comparison with Fission-GRPO since it's the same evaluation setup, but there's a fundamental mismatch—BFCL injects HTTP-level environment errors while ToolScan's taxonomy focuses on agent-side errors, so I need to think through whether that distinction matters for what we're trying to measure.

Actually, BFCL v4 gives us both types naturally: agent errors like incorrect function calls and parameter mistakes, plus the injected HTTP errors. That's actually useful for testing a more complete error taxonomy.

So the plan is to shift from StableToolBench to BFCL v4, position this as building on Fission-GRPO's work rather than claiming novelty at the intersection, ground the error-type stratification in Stratified GRPO, cite CoBA-RL for the budget allocation precedent, and include Fission-GRPO as a baseline for comparison.

Now I'm considering whether a full pivot makes more sense instead. The reviewer's suggestion about framing this as an error-type-aware agentic RL study is interesting—maybe the stronger contribution is a focused empirical paper that takes Fission-GRPO as the foundation, adds error-type-conditioned budget allocation and stratified advantages, then systematically compares against the baseline and other variants like entropy-triggered approaches.

But there's a practical constraint: Fission-GRPO has no released code, so I'd need to either reimplement from the paper's pseudocode, build a simplified version, or cite it as concurrent work. Given the 14-day timeline, I'm weighing whether reimplementing Fission-GRPO plus running the full comparison study is feasible.

The Error Simulator component alone is expensive—it requires 2K teacher examples and SFT training on a large model. Rather than attempt the full reimplementation, I should implement a stripped-down version that uses raw error messages instead of simulated ones, then note that the complete Fission-GRPO would likely perform better. This lets me test whether error-type conditioning recovers some of the performance gap without the overhead.

Actually, stepping back on the timeline: 14 days is really tight, especially with the BFCL v4 setup overhead. I think the most realistic path is to stick with BFCL v4 since it's well-established, implement a simplified error-triggered resampling baseline, and focus the effort on the core comparison study rather than trying to fully replicate Fission-GRPO.

Now I'm noticing the RC-GRPO results—they hit 85% on BFCL v4 with Qwen2.5-7B, which is substantially higher than Fission-GRPO's 46.75% on the same benchmark. I need to check whether they're using different evaluation subsets or if there's something else explaining that gap. The RC-GRPO result might be using the full BFCL v4 score rather than just the multi-turn subset, or the evaluation setups differ in ways I can't pin down. Either way, for this revision what really matters is ensuring we're comparing our own implementations consistently.

Now I'm structuring the major revision: reframing the core problem from "combining error-triggered branching with GRPO" to "whether error-type conditioning improves recovery-focused GRPO," updating the landscape with the recent papers, switching to BFCL v4 as the benchmark, simplifying the approach to build on Fission-GRPO with type conditioning added, and sharpening the contribution around error-type conditioning as the key innovation.

I should do one more check on whether there's recent work specifically on error-type-conditioned RL or error-taxonomy-aware training I might have missed, and verify that BFCL v4 has enough error diversity for this study. Actually, I think I have what I need. For the title, something like "Does Error-Type Conditioning Matter? Adaptive Budget Allocation for Recovery-Focused Agentic RL" or "Error-Type-Conditioned Budget Allocation for Agent" captures the positioning better.

Let me verify the error types available in BFCL v4 before I finalize the JSON.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa477e23-95ea-4193-b86d-53572a4d8fa5",
  "isSidechain": false,
  "requestId": "req_011CawewW3n5KJDjVH4wDd2c",
  "type": "assistant",
  "uuid": "ade8c152-b33f-47fc-beca-d8e020f81bd2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013X8WrJ1JCufdzz3C8nSpUE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15023,
      "cache_read_input_tokens": 25016,
      "output_tokens": 4631,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15023,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4631,
          "cache_read_input_tokens": 25016,
          "cache_creation_input_tokens": 15023,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15023
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

_source line 23 · 2026-05-11T23:34:21.378Z_

Now let me do one more targeted search about BFCL v4's error injection mechanism to confirm it's suitable as a replacement benchmark.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ade8c152-b33f-47fc-beca-d8e020f81bd2",
  "isSidechain": false,
  "requestId": "req_011CawewW3n5KJDjVH4wDd2c",
  "type": "assistant",
  "uuid": "a454469f-365d-4cae-adb0-94028934d113",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013X8WrJ1JCufdzz3C8nSpUE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15023,
      "cache_read_input_tokens": 25016,
      "output_tokens": 4631,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15023,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4631,
          "cache_read_input_tokens": 25016,
          "cache_creation_input_tokens": 15023,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15023
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

_source line 24 · 2026-05-11T23:34:28.305Z_

<details open><summary>🔧 Tool call — Agent · `toolu_0175KjJe2YsLWV8FqQixefjS`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Research BFCL v4 error types",
  "prompt": "I need detailed information about the Berkeley Function Calling Leaderboard v4 (BFCL v4), specifically its error injection mechanism and error types.\n\nPlease:\n1. WebSearch for \"BFCL v4 agentic error injection\", \"Berkeley function calling leaderboard v4 error types\", \"BFCL v4 multi-turn error recovery\"\n2. WebFetch the BFCL v4 documentation or blog post from gorilla.cs.berkeley.edu if available\n3. Search for \"BFCL v4 503 429 403 error recovery evaluation\"\n\nI need to understand:\n- What specific error types does BFCL v4 inject? (e.g., 503, 429, 403, etc.)\n- How many distinct error categories are there?\n- How are errors injected — randomly? At what rate?\n- What is the evaluation protocol for error recovery?\n- How many test cases are there total, and how many involve error recovery?\n- What models have been evaluated on it and what are their scores?\n- Is this benchmark suitable for training (i.e., can we get training trajectories with errors)?\n\nReport all findings in detail."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a454469f-365d-4cae-adb0-94028934d113",
  "isSidechain": false,
  "requestId": "req_011CawewW3n5KJDjVH4wDd2c",
  "type": "assistant",
  "uuid": "48b26ef6-996b-476e-b87a-b2e062f7d1f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013X8WrJ1JCufdzz3C8nSpUE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15023,
      "cache_read_input_tokens": 25016,
      "output_tokens": 4631,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15023,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4631,
          "cache_read_input_tokens": 25016,
          "cache_creation_input_tokens": 15023,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15023
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

_source line 25 · 2026-05-11T23:34:33.932Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01BKgEqFV3dU3tVPgXNpaSH1`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search recent error-type-aware RL",
  "prompt": "Search for any recent work (2025-2026) on error-type-aware or error-taxonomy-conditioned reinforcement learning for LLM agents. I want to make sure we haven't missed any work that specifically conditions RL training on error categories/types.\n\nPlease search with these queries:\n1. \"error type conditioned reinforcement learning LLM agent\"\n2. \"error taxonomy aware training tool use agent\"  \n3. \"error category adaptive GRPO\"\n4. \"failure type conditioned policy optimization\"\n5. \"error-aware budget allocation agent RL\"\n\nAlso search for any very recent papers (April-May 2026) that might be concurrent work:\n6. \"error recovery GRPO 2026\"\n7. \"adaptive branching error recovery agent\"\n\nReport any relevant findings. If nothing is found for a query, say so explicitly — that confirms the gap."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "48b26ef6-996b-476e-b87a-b2e062f7d1f5",
  "isSidechain": false,
  "requestId": "req_011CawewW3n5KJDjVH4wDd2c",
  "type": "assistant",
  "uuid": "26557558-a118-4a79-a041-c93ba02e3f24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013X8WrJ1JCufdzz3C8nSpUE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15023,
      "cache_read_input_tokens": 25016,
      "output_tokens": 4631,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15023,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4631,
          "cache_read_input_tokens": 25016,
          "cache_creation_input_tokens": 15023,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15023
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

_source line 26_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-11 (UTC).**  ## Original idea {   \"title\": \"Error-Type-Conditioned Branching GRPO for Self-Supervised Agent Recove…",
  "leafUuid": "26557558-a118-4a79-a041-c93ba02e3f24",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Error-type-aware branching for agent recovery beyond Fission-GRPO",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c"
}
```

---

### Tool result

_source line 28 · 2026-05-11T23:36:42.257Z_

<details><summary>↩ Tool result · `toolu_01BKgEqFV3dU3tVPgXNpaSH1`</summary>

```text
Here is a comprehensive report of my findings across all seven search queries.

---

## Results by Query

### Query 1: "error type conditioned reinforcement learning LLM agent"

**No direct match found.** No paper explicitly frames RL training as "conditioned on error types" in the sense of varying the policy optimization objective or reward function based on a classified error category. The closest work found is general agentic RL surveys (e.g., [The Landscape of Agentic RL for LLMs](https://arxiv.org/abs/2509.02547)) that discuss learning from failure trajectories via contrastive preference pairs, but none explicitly condition the RL loss on an error taxonomy.

### Query 2: "error taxonomy aware training tool use agent"

**Partial match -- error taxonomies exist, but are not used to condition RL training.**

- **"Where LLM Agents Fail and How They can Learn From Failures"** (arXiv:2509.25370, Sep 2025) introduces **AgentErrorTaxonomy**, a modular classification of failure modes (memory, reflection, planning, action, system-level), and **AgentDebug**, a debugging framework that isolates root-cause failures and provides corrective feedback. It achieves 24% higher all-correct accuracy. However, this is an inference-time debugging/recovery framework -- it does not use the taxonomy to condition RL training.

- **"A Taxonomy of Failures in Tool-Augmented LLMs"** (AST 2025, UW) defines failure categories for tool-augmented LLMs but again focuses on evaluation/diagnosis, not on feeding error types back into training.

**Gap confirmed**: error taxonomies exist in the literature, but no one uses them to modulate the RL training signal itself.

### Query 3: "error category adaptive GRPO"

**No direct match found.** Several adaptive GRPO variants exist, but none condition on error categories:

- **GHPO** (arXiv:2507.10628) addresses reward sparsity by extracting partial ground-truth solutions -- adaptive to difficulty, not error type.
- **Ada-GRPO** adapts to task difficulty to prevent format collapse -- not error-type-aware.
- **AGGC** (arXiv:2601.11864) uses group-wise adaptive gradient clipping for training stability.
- **GRPO++** collects practical tricks for making GRPO work but does not classify errors.

**Gap confirmed**: GRPO adaptations address reward sparsity, difficulty, and stability, but none differentiate by error category.

### Query 4: "failure type conditioned policy optimization"

**No direct match found.** Related work exists on failure-aware training:

- **AgentHER** (arXiv:2603.21357, Mar 2026) adapts Hindsight Experience Replay for LLM agent trajectories. It includes **failure-severity weighting** (downweighting trajectories with major reasoning flaws, inspired by MQM-style error analysis) and a four-stage pipeline (failure classification, outcome extraction, LLM-guided relabeling, data packaging). This is the closest to "failure-type-conditioned" training found -- it classifies failures and weights them differently -- but it applies to SFT/DPO data generation, not to RL policy optimization directly.

- **EPO** (arXiv:2509.22576) uses entropy regularization to address exploration-exploitation cascade failure in multi-turn settings, but does not classify failure types.

- **ARPO** uses entropy-based adaptive rollouts for step-level exploration but is not error-type-aware.

### Query 5: "error-aware budget allocation agent RL"

**No match found.** Searches returned work on multi-agent resource allocation (network slicing, manufacturing) and cost-performance trade-offs in multi-LLM systems (arXiv:2511.02755), but nothing on allocating compute/retry budgets based on error type classification during RL training.

**Gap confirmed**: no work on error-type-aware budget allocation for agent RL training.

### Query 6: "error recovery GRPO 2026"

**Significant match found.**

- **Fission-GRPO: Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors** (arXiv:2601.15625, Jan 2026, Zhiwei Zhang et al.). This is the most relevant paper found. Standard RL treats errors as sparse negative rewards with no guidance on recovery. Fission-GRPO "fissions" each failed trajectory into a new training instance, augments it with diagnostic feedback from a finetuned Error Simulator, and resamples recovery rollouts on-policy. On BFCL v4 Multi-Turn, it improves Qwen3-8B error recovery rate by 5.7% absolute and overall accuracy by 4% over GRPO. **However**, it does not classify errors into a taxonomy and condition training differently per error type -- it treats all execution errors uniformly by converting them into recovery training instances.

- **GVPO: Group Verification-based Policy Optimization** (OpenReview, 2026) integrates process-verifiable signals (syntax errors, runtime exceptions) as step-level corrective shaping terms alongside outcome-verifiable signals. A 32B agent trained with GVPO outperforms o1 by 12.7% on AppWorld Test-C. **But** it uses execution feedback as a generic process reward signal, not as an error-type-conditioned objective.

- **CLEANER: Self-Purified Trajectories Boost Agentic RL** (arXiv:2601.15141, Jan 2026) uses a Similarity-Aware Adaptive Rollback mechanism to replace failures with self-corrections in trajectories, addressing credit assignment issues from noisy trajectories. It classifies replacement granularity (shallow execution repairs vs. deep reasoning substitutions) but this is a trajectory cleaning method, not error-type-conditioned RL.

- **GRPO-VPS** (arXiv:2604.20659, Apr 2026) uses segment-wise confidence gains on ground-truth answers as dense process rewards but does not classify error types.

### Query 7: "adaptive branching error recovery agent 2026"

**No direct match for "adaptive branching" as a training method.** Related work:

- **ErrorProbe** (arXiv:2604.17658, Apr 2026) performs symptom-driven backward tracing using the MAST failure taxonomy for failure attribution in multi-agent systems. It localizes responsible agents and error steps. This is a diagnostic/evaluation tool, not a training method.

- **ReFlect** (2026) is a training-free error recovery method for long-horizon LLM reasoning using deterministic validators, not RL-based.

- LangGraph-style frameworks offer built-in adaptive branching and error recovery at the infrastructure level, not at the training level.

**Gap confirmed**: no work on adaptive branching as an error-recovery-aware RL training strategy.

---

## Summary of the Landscape

| Concept | Papers Found | Conditions RL on Error Types? |
|---|---|---|
| Error taxonomies for agents | AgentErrorTaxonomy, MAST taxonomy, Tool-Augmented LLM failures | No -- used for diagnosis/evaluation only |
| Failure-aware data generation | AgentHER (failure-severity weighting for SFT/DPO) | Partially -- weights by severity for data generation, not RL |
| Error recovery in GRPO | Fission-GRPO (fissions failed trajectories + error simulator) | No -- treats all errors uniformly |
| Process-level error signals in RL | GVPO (syntax/runtime errors as step rewards) | No -- uses errors as generic process reward, no taxonomy |
| Trajectory cleaning from errors | CLEANER (adaptive rollback of failures) | No -- classifies repair granularity, not error types |
| Adaptive GRPO variants | GHPO, Ada-GRPO, AGGC, GRPO++ | No -- adapt to difficulty/stability, not error categories |
| Error-type-aware budget allocation | None found | N/A |
| Error-type-conditioned RL objective | **None found** | **N/A -- this is the gap** |

## Conclusion

**The gap is confirmed.** No existing work (2025-2026) explicitly conditions the RL training objective, reward function, or policy optimization on a classified error taxonomy. The closest neighbors are:

1. **Fission-GRPO** (Jan 2026) -- converts execution errors into recovery training, but does not differentiate by error type.
2. **AgentHER** (Mar 2026) -- uses failure-severity weighting for data generation, but applies to SFT/DPO, not RL policy optimization.
3. **GVPO** (2026) -- uses process-verifiable error signals (syntax/runtime) as step-level rewards, but treats them as a generic signal without taxonomy-based conditioning.
4. **AgentErrorTaxonomy** (Sep 2025) -- defines the taxonomy, but uses it only for inference-time debugging.

No paper combines (a) a structured error taxonomy with (b) error-type-conditioned RL training (e.g., varying rewards, advantages, or exploration budgets based on classified error categories). This represents a genuine research gap.

---

Sources:
- [The Landscape of Agentic RL for LLMs: A Survey](https://arxiv.org/abs/2509.02547)
- [Where LLM Agents Fail and How They can Learn From Failures](https://arxiv.org/abs/2509.25370)
- [Fission-GRPO: Robust Tool Use via Learning to Recover from Execution Errors](https://arxiv.org/abs/2601.15625)
- [AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling](https://arxiv.org/abs/2603.21357)
- [GVPO: Group Verification-based Policy Optimization](https://openreview.net/forum?id=RY47Tq0VsV)
- [CLEANER: Self-Purified Trajectories Boost Agentic RL](https://arxiv.org/abs/2601.15141)
- [GRPO-VPS: Enhancing GRPO with Verifiable Process Supervision](https://arxiv.org/abs/2604.20659)
- [GHPO: Adaptive Guidance for Stable and Efficient LLM RL](https://arxiv.org/pdf/2507.10628)
- [ErrorProbe: Towards Self-Improving Error Diagnosis in Multi-Agent Systems](https://arxiv.org/html/2604.17658v1)
- [EPO: Entropy-regularized Policy Optimization for LLM Agents](https://arxiv.org/abs/2509.22576)
- [Progressive Reward Shaping for Agentic RL](https://arxiv.org/abs/2512.07478)
- [Credit Assignment in RL for LLMs](https://arxiv.org/html/2604.09459v1)
- [Training Recipes for Agentic RL in LLMs](https://github.com/blacksnail789521/Agentic-RL-Training-Recipes)
- [A Taxonomy of RL Environments for LLM Agents](https://leehanchung.github.io/blogs/2026/03/21/rl-environments-for-llm-agents/)
- [A Taxonomy of Failures in Tool-Augmented LLMs](https://homes.cs.washington.edu/~rjust/publ/tallm_testing_ast_2025.pdf)
- [Automated Failure Attribution of LLM Multi-Agent Systems](https://arxiv.org/abs/2505.00212)

agentId: a8a588998dc430654 (use SendMessage with to: 'a8a588998dc430654' to continue this agent)
&lt;usage>total_tokens: 28634
tool_uses: 16
duration_ms: 128323&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "26557558-a118-4a79-a041-c93ba02e3f24",
  "isSidechain": false,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "type": "user",
  "uuid": "cdec3d88-e4d8-4b07-ac72-cacff7df829f",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for any recent work (2025-2026) on error-type-aware or error-taxonomy-conditioned reinforcement learning for LLM agents. I want to make sure we haven't missed any work that specifically conditions RL training on error categories/types.\n\nPlease search with these queries:\n1. \"error type conditioned reinforcement learning LLM agent\"\n2. \"error taxonomy aware training tool use agent\"  \n3. \"error category adaptive GRPO\"\n4. \"failure type conditioned policy optimization\"\n5. \"error-aware budget allocation agent RL\"\n\nAlso search for any very recent papers (April-May 2026) that might be concurrent work:\n6. \"error recovery GRPO 2026\"\n7. \"adaptive branching error recovery agent\"\n\nReport any relevant findings. If nothing is found for a query, say so explicitly — that confirms the gap.",
    "agentId": "a8a588998dc430654",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is a comprehensive report of my findings across all seven search queries.\n\n---\n\n## Results by Query\n\n### Query 1: \"error type conditioned reinforcement learning LLM agent\"\n\n**No direct match found.** No paper explicitly frames RL training as \"conditioned on error types\" in the sense of varying the policy optimization objective or reward function based on a classified error category. The closest work found is general agentic RL surveys (e.g., [The Landscape of Agentic RL for LLMs](https://arxiv.org/abs/2509.02547)) that discuss learning from failure trajectories via contrastive preference pairs, but none explicitly condition the RL loss on an error taxonomy.\n\n### Query 2: \"error taxonomy aware training tool use agent\"\n\n**Partial match -- error taxonomies exist, but are not used to condition RL training.**\n\n- **\"Where LLM Agents Fail and How They can Learn From Failures\"** (arXiv:2509.25370, Sep 2025) introduces **AgentErrorTaxonomy**, a modular classification of failure modes (memory, reflection, planning, action, system-level), and **AgentDebug**, a debugging framework that isolates root-cause failures and provides corrective feedback. It achieves 24% higher all-correct accuracy. However, this is an inference-time debugging/recovery framework -- it does not use the taxonomy to condition RL training.\n\n- **\"A Taxonomy of Failures in Tool-Augmented LLMs\"** (AST 2025, UW) defines failure categories for tool-augmented LLMs but again focuses on evaluation/diagnosis, not on feeding error types back into training.\n\n**Gap confirmed**: error taxonomies exist in the literature, but no one uses them to modulate the RL training signal itself.\n\n### Query 3: \"error category adaptive GRPO\"\n\n**No direct match found.** Several adaptive GRPO variants exist, but none condition on error categories:\n\n- **GHPO** (arXiv:2507.10628) addresses reward sparsity by extracting partial ground-truth solutions -- adaptive to difficulty, not error type.\n- **Ada-GRPO** adapts to task difficulty to prevent format collapse -- not error-type-aware.\n- **AGGC** (arXiv:2601.11864) uses group-wise adaptive gradient clipping for training stability.\n- **GRPO++** collects practical tricks for making GRPO work but does not classify errors.\n\n**Gap confirmed**: GRPO adaptations address reward sparsity, difficulty, and stability, but none differentiate by error category.\n\n### Query 4: \"failure type conditioned policy optimization\"\n\n**No direct match found.** Related work exists on failure-aware training:\n\n- **AgentHER** (arXiv:2603.21357, Mar 2026) adapts Hindsight Experience Replay for LLM agent trajectories. It includes **failure-severity weighting** (downweighting trajectories with major reasoning flaws, inspired by MQM-style error analysis) and a four-stage pipeline (failure classification, outcome extraction, LLM-guided relabeling, data packaging). This is the closest to \"failure-type-conditioned\" training found -- it classifies failures and weights them differently -- but it applies to SFT/DPO data generation, not to RL policy optimization directly.\n\n- **EPO** (arXiv:2509.22576) uses entropy regularization to address exploration-exploitation cascade failure in multi-turn settings, but does not classify failure types.\n\n- **ARPO** uses entropy-based adaptive rollouts for step-level exploration but is not error-type-aware.\n\n### Query 5: \"error-aware budget allocation agent RL\"\n\n**No match found.** Searches returned work on multi-agent resource allocation (network slicing, manufacturing) and cost-performance trade-offs in multi-LLM systems (arXiv:2511.02755), but nothing on allocating compute/retry budgets based on error type classification during RL training.\n\n**Gap confirmed**: no work on error-type-aware budget allocation for agent RL training.\n\n### Query 6: \"error recovery GRPO 2026\"\n\n**Significant match found.**\n\n- **Fission-GRPO: Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors** (arXiv:2601.15625, Jan 2026, Zhiwei Zhang et al.). This is the most relevant paper found. Standard RL treats errors as sparse negative rewards with no guidance on recovery. Fission-GRPO \"fissions\" each failed trajectory into a new training instance, augments it with diagnostic feedback from a finetuned Error Simulator, and resamples recovery rollouts on-policy. On BFCL v4 Multi-Turn, it improves Qwen3-8B error recovery rate by 5.7% absolute and overall accuracy by 4% over GRPO. **However**, it does not classify errors into a taxonomy and condition training differently per error type -- it treats all execution errors uniformly by converting them into recovery training instances.\n\n- **GVPO: Group Verification-based Policy Optimization** (OpenReview, 2026) integrates process-verifiable signals (syntax errors, runtime exceptions) as step-level corrective shaping terms alongside outcome-verifiable signals. A 32B agent trained with GVPO outperforms o1 by 12.7% on AppWorld Test-C. **But** it uses execution feedback as a generic process reward signal, not as an error-type-conditioned objective.\n\n- **CLEANER: Self-Purified Trajectories Boost Agentic RL** (arXiv:2601.15141, Jan 2026) uses a Similarity-Aware Adaptive Rollback mechanism to replace failures with self-corrections in trajectories, addressing credit assignment issues from noisy trajectories. It classifies replacement granularity (shallow execution repairs vs. deep reasoning substitutions) but this is a trajectory cleaning method, not error-type-conditioned RL.\n\n- **GRPO-VPS** (arXiv:2604.20659, Apr 2026) uses segment-wise confidence gains on ground-truth answers as dense process rewards but does not classify error types.\n\n### Query 7: \"adaptive branching error recovery agent 2026\"\n\n**No direct match for \"adaptive branching\" as a training method.** Related work:\n\n- **ErrorProbe** (arXiv:2604.17658, Apr 2026) performs symptom-driven backward tracing using the MAST failure taxonomy for failure attribution in multi-agent systems. It localizes responsible agents and error steps. This is a diagnostic/evaluation tool, not a training method.\n\n- **ReFlect** (2026) is a training-free error recovery method for long-horizon LLM reasoning using deterministic validators, not RL-based.\n\n- LangGraph-style frameworks offer built-in adaptive branching and error recovery at the infrastructure level, not at the training level.\n\n**Gap confirmed**: no work on adaptive branching as an error-recovery-aware RL training strategy.\n\n---\n\n## Summary of the Landscape\n\n| Concept | Papers Found | Conditions RL on Error Types? |\n|---|---|---|\n| Error taxonomies for agents | AgentErrorTaxonomy, MAST taxonomy, Tool-Augmented LLM failures | No -- used for diagnosis/evaluation only |\n| Failure-aware data generation | AgentHER (failure-severity weighting for SFT/DPO) | Partially -- weights by severity for data generation, not RL |\n| Error recovery in GRPO | Fission-GRPO (fissions failed trajectories + error simulator) | No -- treats all errors uniformly |\n| Process-level error signals in RL | GVPO (syntax/runtime errors as step rewards) | No -- uses errors as generic process reward, no taxonomy |\n| Trajectory cleaning from errors | CLEANER (adaptive rollback of failures) | No -- classifies repair granularity, not error types |\n| Adaptive GRPO variants | GHPO, Ada-GRPO, AGGC, GRPO++ | No -- adapt to difficulty/stability, not error categories |\n| Error-type-aware budget allocation | None found | N/A |\n| Error-type-conditioned RL objective | **None found** | **N/A -- this is the gap** |\n\n## Conclusion\n\n**The gap is confirmed.** No existing work (2025-2026) explicitly conditions the RL training objective, reward function, or policy optimization on a classified error taxonomy. The closest neighbors are:\n\n1. **Fission-GRPO** (Jan 2026) -- converts execution errors into recovery training, but does not differentiate by error type.\n2. **AgentHER** (Mar 2026) -- uses failure-severity weighting for data generation, but applies to SFT/DPO, not RL policy optimization.\n3. **GVPO** (2026) -- uses process-verifiable error signals (syntax/runtime) as step-level rewards, but treats them as a generic signal without taxonomy-based conditioning.\n4. **AgentErrorTaxonomy** (Sep 2025) -- defines the taxonomy, but uses it only for inference-time debugging.\n\nNo paper combines (a) a structured error taxonomy with (b) error-type-conditioned RL training (e.g., varying rewards, advantages, or exploration budgets based on classified error categories). This represents a genuine research gap.\n\n---\n\nSources:\n- [The Landscape of Agentic RL for LLMs: A Survey](https://arxiv.org/abs/2509.02547)\n- [Where LLM Agents Fail and How They can Learn From Failures](https://arxiv.org/abs/2509.25370)\n- [Fission-GRPO: Robust Tool Use via Learning to Recover from Execution Errors](https://arxiv.org/abs/2601.15625)\n- [AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling](https://arxiv.org/abs/2603.21357)\n- [GVPO: Group Verification-based Policy Optimization](https://openreview.net/forum?id=RY47Tq0VsV)\n- [CLEANER: Self-Purified Trajectories Boost Agentic RL](https://arxiv.org/abs/2601.15141)\n- [GRPO-VPS: Enhancing GRPO with Verifiable Process Supervision](https://arxiv.org/abs/2604.20659)\n- [GHPO: Adaptive Guidance for Stable and Efficient LLM RL](https://arxiv.org/pdf/2507.10628)\n- [ErrorProbe: Towards Self-Improving Error Diagnosis in Multi-Agent Systems](https://arxiv.org/html/2604.17658v1)\n- [EPO: Entropy-regularized Policy Optimization for LLM Agents](https://arxiv.org/abs/2509.22576)\n- [Progressive Reward Shaping for Agentic RL](https://arxiv.org/abs/2512.07478)\n- [Credit Assignment in RL for LLMs](https://arxiv.org/html/2604.09459v1)\n- [Training Recipes for Agentic RL in LLMs](https://github.com/blacksnail789521/Agentic-RL-Training-Recipes)\n- [A Taxonomy of RL Environments for LLM Agents](https://leehanchung.github.io/blogs/2026/03/21/rl-environments-for-llm-agents/)\n- [A Taxonomy of Failures in Tool-Augmented LLMs](https://homes.cs.washington.edu/~rjust/publ/tallm_testing_ast_2025.pdf)\n- [Automated Failure Attribution of LLM Multi-Agent Systems](https://arxiv.org/abs/2505.00212)"
      }
    ],
    "totalDurationMs": 128323,
    "totalTokens": 28634,
    "totalToolUseCount": 16,
    "usage": {
      "input_tokens": 1736,
      "cache_creation_input_tokens": 1369,
      "cache_read_input_tokens": 22704,
      "output_tokens": 2825,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1369
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1736,
          "output_tokens": 2825,
          "cache_read_input_tokens": 22704,
          "cache_creation_input_tokens": 1369,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1369,
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
      "otherToolCount": 16
    }
  },
  "sourceToolAssistantUUID": "26557558-a118-4a79-a041-c93ba02e3f24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-11T23:39:24.682Z_

<details><summary>↩ Tool result · `toolu_0175KjJe2YsLWV8FqQixefjS`</summary>

````text
Now I have enough information to provide a comprehensive report. Here is the detailed summary:

---

## BFCL V4 Error Injection Mechanism and Benchmark Details

### 1. Error Types Injected

BFCL v4 injects **six distinct error types** during web search evaluation, covering both HTTP status-code failures and network-level disruptions:

| # | Error Type | Category |
|---|-----------|----------|
| 1 | **503 Server Error** (Service Unavailable) | HTTP status code |
| 2 | **429 Too Many Requests** | HTTP status code |
| 3 | **403 Forbidden** | HTTP status code |
| 4 | **ConnectTimeout** (connect timeout=5) | Network disruption |
| 5 | **ReadTimeout** (read timeout=5) | Network disruption |
| 6 | **ConnectionError** (connection establishment failure) | Network disruption |

These are defined as templates in `ERROR_TEMPLATES` in the source file at:
`berkeley-function-call-leaderboard/bfcl_eval/eval_checker/multi_turn_eval/func_source_code/web_search.py`

### 2. How Many Distinct Error Categories

There are **six error types** in the web search error injection, but BFCL v4 also tests for **five broader error/adversarial mechanisms** across the full benchmark:

1. **HTTP/Network errors** (the 6 types above) -- in web search tasks
2. **Missing function documentation** (`miss_func`) -- tools are withheld at certain turns, model must request documentation or recover
3. **Missing parameters** (`miss_param`) -- required arguments are withheld, model must detect and negotiate with user
4. **Context pollution / long context** (`long_context`) -- distractor narratives injected into the initial config
5. **Irrelevance / hallucination traps** (`irrelevance`, `live_irrelevance`) -- misleading tool descriptions where the model should refuse to call any function

### 3. Error Injection Rate and Mechanism

- **Implementation**: Each `fetch_url_content()` call has a randomized chance of returning one of the six error templates instead of actual content.
- **Injection probability**: The source code reveals a threshold of `self._random.random() < 0.95`, meaning there is a **~5% chance of error injection per fetch request** (the code was designed with this rate but appears to have been toggled during development).
- **Reproducibility**: A seeded random number generator (`random.Random(1053)`) is used so that error injection is deterministic across runs.
- **Error selection**: When an error triggers, the specific type is chosen uniformly at random via `self._rng.choice(ERROR_TEMPLATES)`.
- **URL Blocker ablation**: Separately from probabilistic injection, the benchmark tested models at **0%, 50%, and 100% URL fetch failure rates** to measure degradation. At 100% failure, some models still answered correctly (likely from internal knowledge or hallucination).

### 4. Evaluation Protocol for Error Recovery

**Web search evaluation:**
- **Metric**: Exact match. An answer is marked correct if the normalized ground-truth phrase exactly matches the model's response. Normalization includes lowercasing and removing punctuation.
- **Response format**: Models must output `{'answer': [response], 'context': [explanation]}`.
- **Recovery options**: When a fetch fails, the model can either (a) retry the same URL or (b) select an alternative URL from search results.
- **Retry logic**: For 429 errors specifically, the framework implements exponential backoff (initial 2 seconds, capped at 120 seconds) with an infinite retry loop. Non-429 errors propagate immediately.
- **Available tools**: Models are given exactly two functions: `duckduckgo_search()` and `fetch_url_content(url, mode)` where mode can be "raw", "markdown", or "truncate".

**Multi-turn evaluation:**
- **State-based evaluation**: The evaluator checks the actual backend system state after model actions (not just the model's text output).
- **Up to 20 retries**: Upon execution error, the environment provides explicit error traces and permits the agent up to 20 retries to correct its action.
- **AST-based verification**: For function call correctness, Abstract Syntax Tree evaluation is used for deterministic, reproducible scoring.

### 5. Test Case Counts

**Total: approximately 4,680 primary test cases across all categories.**

| Category | Subcategory | Test Cases |
|----------|-------------|------------|
| **Non-Live Single-Turn** | simple_python | 399 |
| | simple_java | 99 |
| | simple_javascript | 49 |
| | multiple | 199 |
| | parallel | 199 |
| | parallel_multiple | 199 |
| | irrelevance | 239 |
| **Live API** | live_simple | 257 |
| | live_multiple | 1,052 |
| | live_parallel | 15 |
| | live_parallel_multiple | 23 |
| | live_relevance | 16 |
| | live_irrelevance | 884 |
| **Multi-Turn** | base | 199 |
| | miss_func | 199 |
| | miss_param | 199 |
| | long_context | 199 |
| **Agentic - Web Search** | web_search_base (with snippet) | ~99 |
| | web_search_no_snippet | ~99 |
| **Agentic - Memory** | memory_kv / memory_vector / memory_rec_sum | 155 |
| **Format Sensitivity** | 200 base entries x 26 prompt variations | 200 (base) |

**Cases explicitly involving error recovery: ~443+** (199 miss_func + 199 miss_param + the web search error injection across ~99-100 questions).

### 6. Scoring Formula

```
Overall Score = (Agentic x 40%) + (Multi-Turn x 30%) + (Live x 10%) + (Non-Live x 10%) + (Hallucination x 10%)
```

The Agentic category (web search + memory) now carries the heaviest weight at 40%, reflecting the shift toward evaluating real-world agentic capabilities. This was a major rebalancing from previous versions where Live, Non-Live, and Multi-Turn each had 33%.

### 7. Model Scores

| Rank | Model | Overall Score |
|------|-------|---------------|
| 1 | GLM-4.5 (FC) | 70.85% |
| 2 | Claude Opus 4.1 | 70.36% |
| 3 | Claude Sonnet 4 | 70.29% |
| 4 | xLAM-2-8b-fc-r | (not reported) |
| 5 | GPT-5 | 59.22% |

**Critical finding**: Memory task performance is extremely low -- even the best models score as low as ~12% in the agentic memory sub-category. Format sensitivity scores range from ~47% (ToolACE-2-Llama-3.1-8B) to ~65% (GLM-4.5). Qwen3.5-397B-A17B scored 72.9% overall on a separate evaluation run. The leaderboard notes that not all models have been evaluated under identical conditions.

### 8. Suitability for Training

**The benchmark data is released under Apache 2.0 license**, and the README explicitly states: "All the leaderboard statistics, and data used to train the models are released under Apache 2.0."

**What is available for constructing training trajectories:**
- Ground truth answers in the `possible_answer/` directory
- Memory prerequisite conversations in `memory_prereq_conversation/` (32 items)
- Complete tool documentation in `multi_turn_func_doc/` (162 JSONL items)
- Full test case definitions with initial configurations and canonical tool call sequences (`path` field)
- Archived/unused dataset splits in `unused_datasets/` that could supplement training

**What is NOT directly available:**
- Pre-recorded model interaction trajectories (you would need to generate these via self-play)
- Explicit error-recovery trajectories (the error injection happens at runtime, so you would need to run models through the benchmark and record the interactions)

**To create training trajectories with errors**, you would need to:
1. Run models through the web search evaluation with error injection enabled
2. Record the full multi-turn interaction including error responses and recovery attempts
3. Use the ground truth to label successful vs. failed recovery strategies
4. The seeded RNG (seed 1053) ensures reproducible error injection, which is useful for consistent training data generation

The 22 evaluation tasks, the `initial_config` state definitions, the `path` (canonical tool sequence), and the `missed_function`/`missed_param` annotations provide a rich scaffold for generating synthetic training data with realistic error scenarios.

Sources:
- [BFCL V4 Agentic Part 1: Web Search](https://gorilla.cs.berkeley.edu/blogs/15_bfcl_v4_web_search.html)
- [BFCL V4 Memory](https://gorilla.cs.berkeley.edu/blogs/16_bfcl_v4_memory.html)
- [BFCL V4 Format Sensitivity](https://gorilla.cs.berkeley.edu/blogs/17_bfcl_v4_prompt_variation.html)
- [BFCL V4 Leaderboard](https://gorilla.cs.berkeley.edu/leaderboard.html)
- [BFCL GitHub Repository](https://github.com/ShishirPatil/gorilla/tree/main/berkeley-function-call-leaderboard)
- [BFCL ICML 2025 Paper](https://proceedings.mlr.press/v267/patil25a.html)
- [BFCL V4 Dataset Guide (HuggingFace)](https://huggingface.co/datasets/tuandunghcmut/BFCL_v4_information/blob/main/BFCL_v4_dataset_guide.md)
- [BFCL V4 Analysis (HuggingFace)](https://huggingface.co/datasets/tuandunghcmut/BFCL_v4_information/blob/main/From%20Tool%20Use%20to%20Holistic%20Agent%20Evaluation_%20An%20In-Depth%20Analysis%20of%20the%20Berkeley%20Function%20Calling%20Leaderboard%20(BFCL).md)
- [EvalScope BFCL-v4 Documentation](https://evalscope.readthedocs.io/en/v1.2.0/third_party/bfcl_v4.html)
- [BFCL-V4 Leaderboard (llm-stats.com)](https://llm-stats.com/benchmarks/bfcl-v4)
- [Agentic AI Benchmarks Leaderboard](https://awesomeagents.ai/leaderboards/agentic-ai-benchmarks-leaderboard/)
- [Error injection source code (web_search.py)](https://github.com/ShishirPatil/gorilla/blob/main/berkeley-function-call-leaderboard/bfcl_eval/eval_checker/multi_turn_eval/func_source_code/web_search.py)
- [BFCL Changelog](https://github.com/ShishirPatil/gorilla/blob/main/berkeley-function-call-leaderboard/CHANGELOG.md)
- [Klavis AI Blog - Function Calling Benchmarks 2025](https://www.klavis.ai/blog/function-calling-and-agentic-ai-in-2025-what-the-latest-benchmarks-tell-us-about-model-performance)

agentId: a259042257267d8a9 (use SendMessage with to: 'a259042257267d8a9' to continue this agent)
&lt;usage>total_tokens: 42379
tool_uses: 34
duration_ms: 296370&lt;/usage>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "48b26ef6-996b-476e-b87a-b2e062f7d1f5",
  "isSidechain": false,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "type": "user",
  "uuid": "2daf67e9-983b-4b55-8bd6-6e5a23fc39ee",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need detailed information about the Berkeley Function Calling Leaderboard v4 (BFCL v4), specifically its error injection mechanism and error types.\n\nPlease:\n1. WebSearch for \"BFCL v4 agentic error injection\", \"Berkeley function calling leaderboard v4 error types\", \"BFCL v4 multi-turn error recovery\"\n2. WebFetch the BFCL v4 documentation or blog post from gorilla.cs.berkeley.edu if available\n3. Search for \"BFCL v4 503 429 403 error recovery evaluation\"\n\nI need to understand:\n- What specific error types does BFCL v4 inject? (e.g., 503, 429, 403, etc.)\n- How many distinct error categories are there?\n- How are errors injected — randomly? At what rate?\n- What is the evaluation protocol for error recovery?\n- How many test cases are there total, and how many involve error recovery?\n- What models have been evaluated on it and what are their scores?\n- Is this benchmark suitable for training (i.e., can we get training trajectories with errors)?\n\nReport all findings in detail.",
    "agentId": "a259042257267d8a9",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have enough information to provide a comprehensive report. Here is the detailed summary:\n\n---\n\n## BFCL V4 Error Injection Mechanism and Benchmark Details\n\n### 1. Error Types Injected\n\nBFCL v4 injects **six distinct error types** during web search evaluation, covering both HTTP status-code failures and network-level disruptions:\n\n| # | Error Type | Category |\n|---|-----------|----------|\n| 1 | **503 Server Error** (Service Unavailable) | HTTP status code |\n| 2 | **429 Too Many Requests** | HTTP status code |\n| 3 | **403 Forbidden** | HTTP status code |\n| 4 | **ConnectTimeout** (connect timeout=5) | Network disruption |\n| 5 | **ReadTimeout** (read timeout=5) | Network disruption |\n| 6 | **ConnectionError** (connection establishment failure) | Network disruption |\n\nThese are defined as templates in `ERROR_TEMPLATES` in the source file at:\n`berkeley-function-call-leaderboard/bfcl_eval/eval_checker/multi_turn_eval/func_source_code/web_search.py`\n\n### 2. How Many Distinct Error Categories\n\nThere are **six error types** in the web search error injection, but BFCL v4 also tests for **five broader error/adversarial mechanisms** across the full benchmark:\n\n1. **HTTP/Network errors** (the 6 types above) -- in web search tasks\n2. **Missing function documentation** (`miss_func`) -- tools are withheld at certain turns, model must request documentation or recover\n3. **Missing parameters** (`miss_param`) -- required arguments are withheld, model must detect and negotiate with user\n4. **Context pollution / long context** (`long_context`) -- distractor narratives injected into the initial config\n5. **Irrelevance / hallucination traps** (`irrelevance`, `live_irrelevance`) -- misleading tool descriptions where the model should refuse to call any function\n\n### 3. Error Injection Rate and Mechanism\n\n- **Implementation**: Each `fetch_url_content()` call has a randomized chance of returning one of the six error templates instead of actual content.\n- **Injection probability**: The source code reveals a threshold of `self._random.random() < 0.95`, meaning there is a **~5% chance of error injection per fetch request** (the code was designed with this rate but appears to have been toggled during development).\n- **Reproducibility**: A seeded random number generator (`random.Random(1053)`) is used so that error injection is deterministic across runs.\n- **Error selection**: When an error triggers, the specific type is chosen uniformly at random via `self._rng.choice(ERROR_TEMPLATES)`.\n- **URL Blocker ablation**: Separately from probabilistic injection, the benchmark tested models at **0%, 50%, and 100% URL fetch failure rates** to measure degradation. At 100% failure, some models still answered correctly (likely from internal knowledge or hallucination).\n\n### 4. Evaluation Protocol for Error Recovery\n\n**Web search evaluation:**\n- **Metric**: Exact match. An answer is marked correct if the normalized ground-truth phrase exactly matches the model's response. Normalization includes lowercasing and removing punctuation.\n- **Response format**: Models must output `{'answer': [response], 'context': [explanation]}`.\n- **Recovery options**: When a fetch fails, the model can either (a) retry the same URL or (b) select an alternative URL from search results.\n- **Retry logic**: For 429 errors specifically, the framework implements exponential backoff (initial 2 seconds, capped at 120 seconds) with an infinite retry loop. Non-429 errors propagate immediately.\n- **Available tools**: Models are given exactly two functions: `duckduckgo_search()` and `fetch_url_content(url, mode)` where mode can be \"raw\", \"markdown\", or \"truncate\".\n\n**Multi-turn evaluation:**\n- **State-based evaluation**: The evaluator checks the actual backend system state after model actions (not just the model's text output).\n- **Up to 20 retries**: Upon execution error, the environment provides explicit error traces and permits the agent up to 20 retries to correct its action.\n- **AST-based verification**: For function call correctness, Abstract Syntax Tree evaluation is used for deterministic, reproducible scoring.\n\n### 5. Test Case Counts\n\n**Total: approximately 4,680 primary test cases across all categories.**\n\n| Category | Subcategory | Test Cases |\n|----------|-------------|------------|\n| **Non-Live Single-Turn** | simple_python | 399 |\n| | simple_java | 99 |\n| | simple_javascript | 49 |\n| | multiple | 199 |\n| | parallel | 199 |\n| | parallel_multiple | 199 |\n| | irrelevance | 239 |\n| **Live API** | live_simple | 257 |\n| | live_multiple | 1,052 |\n| | live_parallel | 15 |\n| | live_parallel_multiple | 23 |\n| | live_relevance | 16 |\n| | live_irrelevance | 884 |\n| **Multi-Turn** | base | 199 |\n| | miss_func | 199 |\n| | miss_param | 199 |\n| | long_context | 199 |\n| **Agentic - Web Search** | web_search_base (with snippet) | ~99 |\n| | web_search_no_snippet | ~99 |\n| **Agentic - Memory** | memory_kv / memory_vector / memory_rec_sum | 155 |\n| **Format Sensitivity** | 200 base entries x 26 prompt variations | 200 (base) |\n\n**Cases explicitly involving error recovery: ~443+** (199 miss_func + 199 miss_param + the web search error injection across ~99-100 questions).\n\n### 6. Scoring Formula\n\n```\nOverall Score = (Agentic x 40%) + (Multi-Turn x 30%) + (Live x 10%) + (Non-Live x 10%) + (Hallucination x 10%)\n```\n\nThe Agentic category (web search + memory) now carries the heaviest weight at 40%, reflecting the shift toward evaluating real-world agentic capabilities. This was a major rebalancing from previous versions where Live, Non-Live, and Multi-Turn each had 33%.\n\n### 7. Model Scores\n\n| Rank | Model | Overall Score |\n|------|-------|---------------|\n| 1 | GLM-4.5 (FC) | 70.85% |\n| 2 | Claude Opus 4.1 | 70.36% |\n| 3 | Claude Sonnet 4 | 70.29% |\n| 4 | xLAM-2-8b-fc-r | (not reported) |\n| 5 | GPT-5 | 59.22% |\n\n**Critical finding**: Memory task performance is extremely low -- even the best models score as low as ~12% in the agentic memory sub-category. Format sensitivity scores range from ~47% (ToolACE-2-Llama-3.1-8B) to ~65% (GLM-4.5). Qwen3.5-397B-A17B scored 72.9% overall on a separate evaluation run. The leaderboard notes that not all models have been evaluated under identical conditions.\n\n### 8. Suitability for Training\n\n**The benchmark data is released under Apache 2.0 license**, and the README explicitly states: \"All the leaderboard statistics, and data used to train the models are released under Apache 2.0.\"\n\n**What is available for constructing training trajectories:**\n- Ground truth answers in the `possible_answer/` directory\n- Memory prerequisite conversations in `memory_prereq_conversation/` (32 items)\n- Complete tool documentation in `multi_turn_func_doc/` (162 JSONL items)\n- Full test case definitions with initial configurations and canonical tool call sequences (`path` field)\n- Archived/unused dataset splits in `unused_datasets/` that could supplement training\n\n**What is NOT directly available:**\n- Pre-recorded model interaction trajectories (you would need to generate these via self-play)\n- Explicit error-recovery trajectories (the error injection happens at runtime, so you would need to run models through the benchmark and record the interactions)\n\n**To create training trajectories with errors**, you would need to:\n1. Run models through the web search evaluation with error injection enabled\n2. Record the full multi-turn interaction including error responses and recovery attempts\n3. Use the ground truth to label successful vs. failed recovery strategies\n4. The seeded RNG (seed 1053) ensures reproducible error injection, which is useful for consistent training data generation\n\nThe 22 evaluation tasks, the `initial_config` state definitions, the `path` (canonical tool sequence), and the `missed_function`/`missed_param` annotations provide a rich scaffold for generating synthetic training data with realistic error scenarios.\n\nSources:\n- [BFCL V4 Agentic Part 1: Web Search](https://gorilla.cs.berkeley.edu/blogs/15_bfcl_v4_web_search.html)\n- [BFCL V4 Memory](https://gorilla.cs.berkeley.edu/blogs/16_bfcl_v4_memory.html)\n- [BFCL V4 Format Sensitivity](https://gorilla.cs.berkeley.edu/blogs/17_bfcl_v4_prompt_variation.html)\n- [BFCL V4 Leaderboard](https://gorilla.cs.berkeley.edu/leaderboard.html)\n- [BFCL GitHub Repository](https://github.com/ShishirPatil/gorilla/tree/main/berkeley-function-call-leaderboard)\n- [BFCL ICML 2025 Paper](https://proceedings.mlr.press/v267/patil25a.html)\n- [BFCL V4 Dataset Guide (HuggingFace)](https://huggingface.co/datasets/tuandunghcmut/BFCL_v4_information/blob/main/BFCL_v4_dataset_guide.md)\n- [BFCL V4 Analysis (HuggingFace)](https://huggingface.co/datasets/tuandunghcmut/BFCL_v4_information/blob/main/From%20Tool%20Use%20to%20Holistic%20Agent%20Evaluation_%20An%20In-Depth%20Analysis%20of%20the%20Berkeley%20Function%20Calling%20Leaderboard%20(BFCL).md)\n- [EvalScope BFCL-v4 Documentation](https://evalscope.readthedocs.io/en/v1.2.0/third_party/bfcl_v4.html)\n- [BFCL-V4 Leaderboard (llm-stats.com)](https://llm-stats.com/benchmarks/bfcl-v4)\n- [Agentic AI Benchmarks Leaderboard](https://awesomeagents.ai/leaderboards/agentic-ai-benchmarks-leaderboard/)\n- [Error injection source code (web_search.py)](https://github.com/ShishirPatil/gorilla/blob/main/berkeley-function-call-leaderboard/bfcl_eval/eval_checker/multi_turn_eval/func_source_code/web_search.py)\n- [BFCL Changelog](https://github.com/ShishirPatil/gorilla/blob/main/berkeley-function-call-leaderboard/CHANGELOG.md)\n- [Klavis AI Blog - Function Calling Benchmarks 2025](https://www.klavis.ai/blog/function-calling-and-agentic-ai-in-2025-what-the-latest-benchmarks-tell-us-about-model-performance)"
      }
    ],
    "totalDurationMs": 296370,
    "totalTokens": 42379,
    "totalToolUseCount": 34,
    "usage": {
      "input_tokens": 290,
      "cache_creation_input_tokens": 1804,
      "cache_read_input_tokens": 37355,
      "output_tokens": 2930,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1804
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 290,
          "output_tokens": 2930,
          "cache_read_input_tokens": 37355,
          "cache_creation_input_tokens": 1804,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1804,
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
      "otherToolCount": 34
    }
  },
  "sourceToolAssistantUUID": "48b26ef6-996b-476e-b87a-b2e062f7d1f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-11 (UTC).**  ## Original idea {   \"title\": \"Error-Type-Conditioned Branching GRPO for Self-Supervised Agent Recove…",
  "leafUuid": "2daf67e9-983b-4b55-8bd6-6e5a23fc39ee",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "ai-title",
  "aiTitle": "Error-type-aware branching for agent recovery beyond Fission-GRPO",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c"
}
```

---

### Assistant

_source line 32 · 2026-05-11T23:41:43.352Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have comprehensive information. Let me synthesize everything and think deeply about the revision.

## Synthesis of All Research

### The Novelty Landscape After Accounting for All Prior Work:

1. **Fission-GRPO (ACL 2026)**: Does error-triggered GRPO resampling for recovery, but:
   - Does NOT condition on error type (treats all errors uniformly)
   - Requires a trained Error Simulator (2K examples from Claude Sonnet 4, SFT on Qwen3-32B)
   - Evaluated only on BFCL v4 Multi-Turn
   - No code released

2. **Stratified GRPO**: Proposes stratified advantage normalization, but:
   - Uses search-structure-based strata (number of search calls), NOT error types
   - Applied to search agents, not recovery
   - Evaluated on QA tasks only

3. **CoBA-RL / Knapsack RL**: Adaptive budget allocation, but:
   - Based on task difficulty, NOT error types
   - Applied to math reasoning
   - No connection to error recovery

4. **RC-GRPO**: Reward-conditioned trajectory generation, but:
   - Solves variance collapse, not error recovery
   - Addresses a complementary problem

5. **The gap is confirmed**: No paper combines error taxonomy with error-type-conditioned RL training (varying budgets, advantages, or rewards by error category).

### StableToolBench vs BFCL v4:

StableToolBench suppresses error diversity with its high cache hit rate, making it unsuitable. BFCL v4 is the better choice—it includes six injected HTTP/network error types plus three adversarial categories, uses the same benchmark as Fission-GRPO for direct comparison, and has an Apache 2.0 license. The main concern is the low error injection rate for web search and whether the error type diversity is sufficient, but I should reconsider this more carefully.

Looking at BFCL v4's structure, the HTTP/network errors are concentrated in the web search subtask (~99 questions), while the multi-turn error types like miss_func and miss_param represent situations where the agent needs to adapt rather than traditional API failures. From the agent's perspective, these still constitute distinct error types with different recovery profiles, giving us a workable taxonomy for error-type conditioning.

The real constraint is data scarcity — with only ~5-10 instances per HTTP/network error type across the entire benchmark, there's not enough volume for effective GRPO training. This pushes me toward either injecting errors synthetically into StableToolBench to control the distribution and scale, or focusing on BFCL v4's multi-turn errors where we have sufficient instances but they're agent-side rather than environment-side failures. -side errors (incorrect function name, wrong parameters, format errors) DO occur naturally when Qwen3-8B interacts with BFCL v4. These are ToolScan-style errors. Combined with the environment-injected errors, we might have a richer taxonomy.

Let me think about what actually happens when Qwen3-8B runs BFCL v4 multi-turn:
- The model might call a function that doesn't exist → incorrect function name error
- The model might pass wrong parameter types → parameter error  
- The model might produce malformed JSON → format error
- The environment might inject HTTP errors → environment errors
- The model might miss required parameters → missing parameter error

So there ARE multiple error types, but they come from two sources:
1. Agent-side errors (naturally occurring from model mistakes)
2. Environment-side errors (injected by BFCL v4)

This combination could give us a decent taxonomy for error-type conditioning. I'm thinking the best approach is to study whether conditioning recovery training on error types actually helps—using Fission-GRPO as the baseline. The hypothesis is that different error types require different recovery strategies, so allocating training budget and normalizing advantages by error type could improve efficiency. I'd use BFCL v4 Multi-Turn as the benchmark, combining the environment-injected errors with the naturally occurring agent-side errors plus the benchmark's built-in challenges. Though I'm realizing Fission-GRPO itself only evaluates on BFCL v4 Multi-Turn, so I need to think about whether that's the right scope. The error categories align well with ToolScan's taxonomy, and they have varying difficulty levels—format errors are straightforward to fix while incorrect function names require deeper reasoning. This suggests that uniform resampling might not be optimal, and allocating retry budget based on error type could improve efficiency. My approach is to start with Fission-GRPO's error-triggered resampling framework, then layer in type-conditioned budget allocation and additional refinements.

But I'm realizing that removing the Error Simulator would actually hurt our baseline—Fission-GRPO showed a +2.75% improvement with it. Instead of dropping it, I should keep the simulator and add type conditioning on top, though that means training the simulator becomes part of the cost.

Actually, there's a better angle: BFCL v4 Multi-Turn already provides explicit error traces from the environment itself (up to 20 retries), so we don't need a trained simulator at all. The environment gives us diagnostic feedback naturally. This is our real differentiation from Fission-GRPO—they need a simulator because their environments don't provide detailed error feedback, but ours does. We can leverage those raw error traces and add error-type conditioning on top instead.

Though I need to check whether Fission-GRPO also evaluates on BFCL v4...

they do, which means the environment already has error traces. So what's the simulator actually adding? It must be generating more pedagogical error descriptions—hints that don't reveal the answer but guide the agent better than raw "function not found" messages. We're skipping that layer and compensating with type-conditioned budget allocation that focuses exploration on harder error types.

This gives me a clearer direction: stay with Fission-GRPO's error-triggered GRPO resampling paradigm but differentiate through error-type conditioning and raw environment feedback instead of a trained simulator.

The key empirical question becomes whether error-type conditioning beats uniform resampling, which would show us how to do error recovery training more efficiently. Switching to BFCL v4 cuts setup overhead and removing the Error Simulator saves about 20 GPU hours, though reimplementing Fission-GRPO takes time—so we're roughly even on compute with a tighter timeline.

Now I need to check if BFCL v4's error diversity is sufficient for type conditioning.

Looking at the numbers: Fission-GRPO gets 42.75% base accuracy on BFCL v4 Multi-Turn, leaving about 458 failed trajectories. These failures distribute across error types—incorrect function names, wrong arguments, format errors, and the benchmark-designed missing function/parameter cases. A pilot run would show the exact breakdown, but with ~458 failures spread across 4-6 types, I'd expect roughly 75-115 instances per type, which gives enough data for GRPO training.

That's workable. But I'm realizing BFCL v4 Multi-Turn actually has 199 base cases plus 199 each for miss_func, miss_param, and long_context variants—I need to think through how those split.

The issue is that miss_func and miss_param are deliberately designed test scenarios, not naturally occurring errors. So I'm conflating two different things: errors that emerge organically from the base category versus errors that are engineered into the benchmark. For error-type conditioning, I could either focus only on base (too small), or classify errors by their actual mistake pattern rather than the BFCL category. That second approach makes more sense—within each BFCL category, the model still makes different kinds of mistakes that I can identify from the error traces, and the category itself tells me the context of the failure.

So I'd define error types like format errors, incorrect function names, wrong argument types or values, missing arguments, and function unavailability. That gives me enough diversity to work with. Now I'm wondering whether to include BFCL v4 Multi-Turn only or the full dataset including web search tasks, since web search adds HTTP errors like timeouts and rate limits that would expand the error taxonomy further.

Given the tight timeline for a short paper, sticking with Multi-Turn makes more sense—it's the pragmatic choice and aligns with what Fission-GRPO used. I can always mention web search error types as future work.

Now I need to finalize the approach and settle on a title. The reviewer suggested focusing on error-type awareness, so I'm weighing a few options that emphasize either the conditioning aspect or the adaptive budget allocation for recovery training.

I'm leaning toward something direct that clearly states the hypothesis without borrowing Fission-GRPO's terminology. "Error-Type Conditioning Improves GRPO-Based Agent Recovery Training" feels like the strongest choice—it's straightforward and positions the contribution clearly.

Actually, a question-style title might work better for a shorter paper since it frames this as an empirical investigation rather than claiming a definitive result. "Does Error-Type Conditioning Improve GRPO-Based Agent Recovery?" is more honest about the scope and reads as a genuine research question.

Now I'm ready to build out the JSON structure. I'll reframe the core problem around what Fission-GRPO does uniformly versus what error-type conditioning could offer, narrow the opportunity to the specific gap in budget allocation and stratified advantages, update the landscape with the new papers, and simplify the approach section.

For the approach, I need to be precise about how I'll extract error types from BFCL v4 traces, compute the type-specific budget allocation, implement error-type-stratified advantages while acknowledging Stratified GRPO's existing work, define which baselines to compare against, and specify the metrics. Switching to BFCL v4 simplifies the resource requirements since there's no virtual API server or Error Simulator training needed, though I'll still need to generate rollout trajectories.

Looking at the timeline, I'm estimating around 90 hours total—trajectory collection and pilot runs taking roughly 10-15 hours, error-type-conditioned rollouts and baselines each around 15 hours, GRPO training with ablations another 15 hours, plus evaluation and buffer time. That's much more feasible than the original 130 hours. With 14 days being tight, I should map out what can run in parallel: setting up BFCL v4 and initial trajectories on days 1-2, then pilot runs and error classification while baseline rollouts start.

I can parallelize all the rollout variants across multiple GPUs during days 5-7, run GRPO training for all variants on days 8-9, then evaluation and analysis on days 10-11, leaving days 12-14 for writing. This works with 2-4 GPUs running simultaneously.

Now I'm thinking through the possible outcomes—whether error-type conditioning actually helps, whether it's a negative result showing uniform resampling is sufficient, or whether it helps selectively for certain error types. Any of these would make a solid contribution for an EMNLP short paper.

I'm also considering whether to include RC-GRPO as a baseline since it addresses variance collapse and could complement type conditioning, but that would add complexity to an already tight schedule. I'll mention it as future work instead and keep the baselines focused.

Drafting the final JSON structure...

Now I'm writing out each field carefully, starting with the core problem. The key insight is that Fission-GRPO treats all errors the same way, but recent work on stratified advantage normalization and difficulty-proportional budget allocation suggests that error-type-specific resampling could be more effective. The key insight is that error types have fundamentally different recovery difficulty profiles—format errors are straightforward fixes, while function selection errors require tool understanding and argument errors demand domain reasoning—yet existing methods treat all errors uniformly. I'm laying out the concrete approach: extracting error classifications from BFCL v4 traces, allocating recovery budgets proportionally to error difficulty, normalizing advantages within error-type strata rather than just trajectory structure, and building a streamlined system without the Error Simulator to enable direct comparison of whether type-conditioned allocation outperforms Fission-GRPO's uniform resampling strategy.

Now I'm mapping the related work landscape, positioning this against Fission-GRPO as the primary baseline, drawing on stratified normalization from prior work and budget allocation precedents like CoBA-RL and Knapsack RL, while also accounting for complementary GRPO improvements and noting where GVPO's process-verifiable error signals differ from my conditioning approach—it shapes rewards directly rather than allocating exploration budget.

I'm also considering AgentHER's failure-severity weighting as the closest parallel in SFT, then settling on the project name and contribution level before writing out the full reference JSON carefully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2daf67e9-983b-4b55-8bd6-6e5a23fc39ee",
  "isSidechain": false,
  "requestId": "req_011CawfT3k5P4L4ZerP5Edwo",
  "type": "assistant",
  "uuid": "de367d88-86df-4868-8eff-0128bd87685e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TcdAqiQVXqtZtejmKU5xMd",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2922,
      "cache_creation_input_tokens": 7649,
      "cache_read_input_tokens": 40039,
      "output_tokens": 12159,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7649,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2922,
          "output_tokens": 12159,
          "cache_read_input_tokens": 40039,
          "cache_creation_input_tokens": 7649,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7649
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

_source line 33 · 2026-05-11T23:43:57.760Z_

Excellent research. Now I have a complete picture. Let me synthesize the findings and think through the revision before writing.

**Key findings from research:**

1. **Fission-GRPO is real (ACL 2026)** — does error-triggered GRPO resampling but treats all errors uniformly (no type conditioning). Requires trained Error Simulator (2K Claude Sonnet 4 examples + Qwen3-32B SFT). No code released.

2. **Stratified GRPO is real** — proposes SAN (stratified advantage normalization) for search agents using trajectory-structure strata (search count), not error types. Under review at ICLR 2026.

3. **CoBA-RL is real** — Beta distribution-based adaptive budget allocation for math reasoning GRPO. Task-difficulty-based, not error-type-based.

4. **RC-GRPO is real** — reward-conditioned trajectory generation for BFCL v4 tool calling. Complementary problem (variance collapse).

5. **StableToolBench is a bad fit** — 96-97% cache hit rate, virtual server deliberately suppresses error diversity. No infrastructure/operational errors.

6. **BFCL v4 is the right benchmark** — 6 injected error types, up to 20 retries with error traces, same as Fission-GRPO (enables direct comparison).

7. **The gap is confirmed** — no paper conditions RL training on error TYPE taxonomy. The specific combination of type-conditioned budget + type-stratified advantages for recovery is unoccupied.

This calls for a **major revision**: keep the core hypothesis (error-type conditioning improves recovery training) but completely reposition against Fission-GRPO, switch benchmark, and sharpen the contribution.

```json
{
  "title": "Does Error-Type Conditioning Improve GRPO-Based Agent Recovery?",
  "core_problem": "Fission-GRPO (ACL 2026) established that error-triggered GRPO resampling—fissioning each failed tool-call trajectory into G' parallel recovery attempts—improves agent recovery on BFCL v4 Multi-Turn by +5.7% absolute recovery rate. However, Fission-GRPO treats all errors uniformly: every fission event receives the same resampling budget G' regardless of error type, and advantages are normalized within each fission group without regard to error category. Two concurrent lines of work suggest this uniformity is suboptimal. Stratified GRPO (arXiv:2510.06214) demonstrates that structurally heterogeneous GRPO groups (varying numbers of search calls) suffer cross-stratum advantage bias, corrected by stratified advantage normalization (SAN). CoBA-RL (arXiv:2602.03048) and Knapsack RL (arXiv:2509.25849) show that difficulty-proportional rollout budget allocation consistently outperforms uniform allocation in GRPO training for math reasoning. Tool-use errors have demonstrably different recovery difficulty profiles: format errors (malformed JSON) are typically recoverable via simple reformatting, while incorrect function selection requires understanding the tool space, and wrong argument values demand domain-specific reasoning. Yet no method conditions recovery training budget or advantage computation on error category. Does error-type-conditioned budget allocation and advantage stratification improve over Fission-GRPO's uniform error-triggered resampling, and if so, for which error types does conditioning matter most?",
  "opportunity": "A specific methodological gap exists at the intersection of three established ideas, each validated independently but never combined. (1) Error-triggered resampling for recovery (Fission-GRPO, ACL 2026): fissions failed trajectories into G' recovery attempts with uniform budget—effective but type-agnostic. (2) Stratified advantage normalization (Stratified GRPO, arXiv:2510.06214): eliminates cross-stratum bias by normalizing advantages within structural strata—but uses trajectory structure (search call count), not error categories. (3) Difficulty-proportional budget allocation (CoBA-RL, arXiv:2602.03048; Knapsack RL, arXiv:2509.25849): allocates more rollouts to harder tasks—but operates at task level, not error-type level. The specific combination—error-type-conditioned budget for recovery resampling (K_τ ∝ 1-RR_pilot(τ), more fission branches for harder-to-recover error types) plus error-type-stratified advantage normalization (preventing easy-to-recover format errors from dominating gradients over hard-to-recover function selection errors)—is absent from all prior work. This matters because: (a) uniform budget wastes exploration on easy recoveries (format fixes) while under-exploring hard ones (function hallucination), and (b) cross-type advantage bias systematically penalizes recovery attempts for hard error types when normalized against easy ones. Additionally, error-type conditioning enables per-type empirical analysis—revealing which error categories benefit from RL-based branching vs. SFT-based relabeling—a novel diagnostic contribution absent from both Fission-GRPO and AgentHER. A further practical advantage: by using raw environment error traces (which BFCL v4 provides natively with up to 20 retries) instead of Fission-GRPO's trained Error Simulator (requiring 2K Claude-annotated examples + Qwen3-32B SFT), our approach is annotation-free and simpler to deploy.",
  "landscape": "Fission-GRPO (ACL 2026, arXiv:2601.15625) is the most directly related work: it fissions each failed trajectory into G' parallel recovery attempts augmented with diagnostic feedback from a trained Error Simulator (Qwen3-32B SFT on 2K Claude Sonnet 4-written examples), achieving +4.0% overall accuracy and +5.7% recovery rate on BFCL v4 Multi-Turn with Qwen3-8B. Critically, it uses uniform resampling budget G' for all error types and does not condition on error category—the Error Simulator generates context-aware feedback but does not classify errors. No code released. Stratified GRPO (arXiv:2510.06214, ICLR 2026 submission) proposes Stratified Advantage Normalization (SAN), which partitions GRPO trajectories into strata by structural properties (number of search calls) and normalizes advantages within each stratum, eliminating cross-stratum bias. Applied to search agents on QA benchmarks (NQ, HotpotQA, MuSiQue, etc.) with Qwen-2.5-3B, achieving up to +11.3 points over standard GRPO. The general mechanism of stratified normalization is established, but its application to error-type strata in recovery training is novel. CoBA-RL (arXiv:2602.03048) models task preferences via a Beta distribution with capability-aware parameters, allocating more rollout budget to tasks at the model's learning frontier—outperforms Knapsack RL (arXiv:2509.25849) on math reasoning. Both operate at task difficulty level, not error-type level. RC-GRPO (arXiv:2602.03025) addresses the complementary problem of within-group reward variance collapse in multi-turn tool calling via reward-conditioned trajectory generation, achieving 85.0% on BFCL v4 with Qwen2.5-7B—a strong result but on a different axis (variance vs. type conditioning). PALADIN (ICLR 2026, arXiv:2509.25238) trains recovery via SFT on 50K+ GPT-5-annotated trajectories across ToolScan's 7 error categories, achieving 89.68% recovery rate—expensive annotation-based approach. 'Failure Makes Agent Stronger' (arXiv:2509.18847) uses DAPO+GSPO on synthetic errors with ~18 person-days human annotation. AgentHER (arXiv:2603.21357) uses hindsight experience replay with failure-severity weighting for SFT-based recovery—the closest SFT approach to type-aware training, but not RL. GVPO (OpenReview 2026) uses process-verifiable signals (syntax errors, runtime exceptions) as step-level reward shaping but treats errors as generic process rewards without taxonomy. AT²PO (arXiv:2601.04767) and A²TGPO (arXiv:2605.06200) use entropy-based turn-level branching for search agents. InfoTree (arXiv:2605.05262) uses submodular budget allocation—principled but domain-agnostic. ARPO (ICLR 2026, arXiv:2507.19849) and Tree-GRPO (ICLR 2026, arXiv:2509.21240) establish entropy-triggered and uniform branching respectively. ToolScan (arXiv:2509.25370) defines 7 error patterns (IAC, IAV, IAN, IAT, RAC, IFN, IFE) used for evaluation but not for conditioning RL training. ERR Measure (arXiv:2601.22352) formalizes recovery metrics. HiPER (arXiv:2602.16165) near-saturates ALFWorld (97.4%). CLEANER (arXiv:2601.15141) purifies trajectories via adaptive rollback but does not condition on error type. The specific intersection—error-type-conditioned budget allocation + error-type-stratified advantage normalization within error-triggered GRPO resampling for recovery—remains unoccupied.",
  "approach": "We propose Error-Type-Conditioned Fission (ETC-Fission), an extension of Fission-GRPO that adds error-type conditioning to error-triggered GRPO resampling for recovery training, evaluated on BFCL v4 Multi-Turn. The method has three components:\n\n(1) Error-Type Classification and Type-Conditioned Budget Allocation: When the policy model (Qwen3-8B) encounters execution errors during rollout on BFCL v4 Multi-Turn, we classify each error into one of 5 categories using rule-based parsing of BFCL v4's structured error traces: (a) format error (malformed JSON/function call syntax), (b) incorrect function name (calling non-existent or wrong function), (c) argument type/value error (correct function but wrong parameters), (d) missing argument error, (e) function unavailable (for miss_func scenarios). Unlike Fission-GRPO which uses uniform G' for all fission events, we allocate the fission budget K_τ per error type τ proportional to recovery difficulty: K_τ = round(K_base · (1 - RR_pilot(τ)) / Z), where RR_pilot(τ) is the recovery rate for error type τ from a pilot run (500 trajectories), and Z is a normalization constant. This applies CoBA-RL's principle of difficulty-proportional allocation at the error-type granularity rather than task granularity. Harder-to-recover error types receive more recovery branches, concentrating exploration budget where uniform allocation under-explores.\n\n(2) Error-Type-Stratified Advantage Normalization: Following Stratified GRPO's insight that cross-stratum advantage bias distorts gradient contributions, we stratify GRPO advantages by error type. Within each fission group, advantages are z-score normalized within the error-type stratum rather than globally across all fission groups: A_stratified(τ_i) = (R(τ_i) - μ_k) / (σ_k + ε), where k is the error type of the fission event producing τ_i. This prevents easy-to-recover error types (format errors, which often recover on first retry) from dominating the advantage signal over hard-to-recover types (function hallucination, requiring tool-space exploration). We use Stratified GRPO's blended formulation (α-weighted combination of stratified and global advantages) for finite-sample stability when some error types have few instances. This is a domain-specific instantiation of SAN: Stratified GRPO uses trajectory structure (search count) as the stratification variable; we use error category.\n\n(3) Annotation-Free Error Feedback via Native Error Traces: Unlike Fission-GRPO which trains an Error Simulator (Qwen3-32B SFT on 2K Claude Sonnet 4-annotated examples) to generate diagnostic feedback, we use BFCL v4's native error traces directly as the recovery context. BFCL v4 provides structured error messages (function not found, type mismatch, missing required parameter, etc.) with up to 20 retries per error. These traces are informative enough for recovery (Fission-GRPO's ablation shows even generic error messages yield +1.25% over no feedback) and eliminate the annotation cost entirely. The fission context is constructed as [query; failed_trajectory; environment_error_trace] without synthetic augmentation.\n\nSystematic Comparison: We compare six conditions: (a) ETC-Fission (ours: type-conditioned budget + type-stratified advantages + native error traces), (b) Uniform-Fission (uniform budget G' + global advantages + native error traces—our reimplementation of Fission-GRPO without the Error Simulator), (c) Uniform-Fission+Simulator (if feasible: adds Error Simulator to (b), reproducing full Fission-GRPO), (d) entropy-triggered branching (AT²PO-style, branching at high-entropy post-tool-call turns), (e) standard GRPO (no fission), (f) AgentHER (SFT on hindsight-relabeled failed trajectories). All methods use Qwen3-8B with LoRA, 1 iterative round.\n\nEvaluation: Overall accuracy, Recovery Rate (RR), Post-Error Task Success Rate (PE-TSR), and Recovery Efficiency (steps-to-recover) following ERR measure framework. The central empirical contribution is error-type-stratified analysis: per-type RR/PE-TSR/efficiency breakdown revealing which error types benefit most from type-conditioned RL branching vs. uniform branching vs. SFT relabeling. This analysis is absent from all prior work and provides actionable guidance for recovery training.\n\nPositioning: We build explicitly on Fission-GRPO's paradigm of error-triggered GRPO resampling, extending it with type-conditioned budget allocation (from CoBA-RL's difficulty-proportional principle) and type-stratified advantage normalization (from Stratified GRPO's SAN). The contribution is the combination and the per-type empirical analysis, not the individual components.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~95h H100-80GB (trajectory collection on BFCL v4 Multi-Turn ~10h, pilot run for per-type recovery difficulty estimation ~4h, type-conditioned fission rollouts ~15h, baseline rollouts: uniform-fission+entropy+standard-GRPO ~15h, AgentHER SFT baseline ~5h, GRPO LoRA training: ETC-Fission + Uniform-Fission ~12h, evaluation on recovery metrics ~5h, per-type analysis ~3h, debugging buffer ~26h)",
      "gpu_utilization": "~55% — GPUs wait while researchers validate error classification rules and review pilot per-type statistics",
      "timeline": "14 days (tight but feasible: BFCL v4 is simpler to deploy than StableToolBench, no Error Simulator training needed)",
      "team": "1-2 researchers working full-time",
      "estimated_gpu_cost": "$285 (at ~$3.00/hr H100)"
    },
    "human_in_loop": {
      "gpu_hours": "~85h H100-80GB (same breakdown minus ~10h from automated pilot analysis and error classification validation)",
      "gpu_utilization": "~70% — agent handles rollout orchestration and training loops; human reviews error classification accuracy and per-type statistics",
      "timeline": "12-14 days",
      "team": "1 researcher, ~2hr/day for error taxonomy review, per-type analysis validation, and paper writing",
      "claude_api_cost": "$70-100 (~500-700 turns for pipeline orchestration and analysis)",
      "estimated_gpu_cost": "$255 (at ~$3.00/hr H100)",
      "risk_note": "Error classification from BFCL v4 error traces is straightforward (structured error messages), reducing risk vs. StableToolBench. Main risk: if 1-2 error types dominate (>80% of errors), per-type analysis lacks statistical power for rare types; mitigation is to merge rare types into an 'other' category and focus analysis on the 3-4 most frequent types."
    },
    "auto_research": {
      "gpu_hours": "~110h H100-80GB (adds Error Simulator reproduction attempt ~15h, second GRPO iteration ~10h, bootstrap confidence intervals for per-type analysis ~5h)",
      "gpu_utilization": "~85% — continuous job submission across trajectory collection, fission rollouts, and training",
      "timeline": "10-12 days with 2-4 parallel H100 GPUs",
      "team": "0 (1-2 hour initial setup for BFCL v4 environment and error classification rules)",
      "claude_api_cost": "$100-160 (~1000-1600 turns for full pipeline orchestration and paper drafting)",
      "estimated_gpu_cost": "$330 (at ~$3.00/hr H100)",
      "speed_bottleneck": "Sequential dependency: pilot run → K_τ estimation → type-conditioned rollouts; BFCL v4 evaluation is faster than StableToolBench (no external API calls)",
      "risk_note": "Automated error classification should be reliable given BFCL v4's structured error traces; rare error types may need merging for statistical validity"
    }
  },
  "target_venues": [
    "EMNLP 2026 (ARR May 25, 2026 — primary and only target, 14 days available, short paper 4 pages + unlimited references)"
  ],
  "level": "solid",
  "key_references": [
    "Fission-GRPO: Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors (ACL 2026, arXiv:2601.15625)",
    "Stratified GRPO: Handling Structural Heterogeneity in RL of LLM Search Agents (arXiv:2510.06214)",
    "CoBA-RL: Capability-Oriented Budget Allocation for RL in LLMs (arXiv:2602.03048)",
    "Knapsack RL: Unlocking Exploration of LLMs via Optimizing Budget Allocation (arXiv:2509.25849)",
    "RC-GRPO: Reward-Conditioned GRPO for Multi-Turn Tool Calling Agents (arXiv:2602.03025)",
    "PALADIN: Self-Correcting Language Model Agents to Cure Tool-Failure Cases (ICLR 2026, arXiv:2509.25238)",
    "Failure Makes the Agent Stronger: Structured Reflection for Reliable Tool Interactions (arXiv:2509.18847)",
    "AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling (arXiv:2603.21357)",
    "Agentic Reinforced Policy Optimization / ARPO (ICLR 2026, arXiv:2507.19849)",
    "Tree Search for LLM Agent Reinforcement Learning / Tree-GRPO (ICLR 2026, arXiv:2509.21240)",
    "AT²PO: Agentic Turn-based Policy Optimization via Tree Search (arXiv:2601.04767)",
    "A²TGPO: Agentic Turn-Group Policy Optimization with Adaptive Turn-level Clipping (arXiv:2605.06200)",
    "InfoTree: Maximizing Rollout Informativeness under a Fixed Budget via Submodular Tree Search (arXiv:2605.05262)",
    "GVPO: Group Verification-based Policy Optimization (OpenReview 2026)",
    "HiPER: Hierarchical RL with Explicit Credit Assignment for LLM Agents (arXiv:2602.16165)",
    "Where LLM Agents Fail: Error Taxonomy across Modules / ToolScan (arXiv:2509.25370)",
    "Recoverability Has a Law: The ERR Measure for Tool-Augmented Agents (arXiv:2601.22352)",
    "CLEANER: Self-Purified Trajectories Boost Agentic RL (arXiv:2601.15141)",
    "BFCL V4: Berkeley Function Calling Leaderboard (ICML 2025, gorilla.cs.berkeley.edu)",
    "StableToolBench: Towards Stable Large-Scale Benchmarking on Tool Learning (ACL Findings 2024, arXiv:2403.07714)",
    "Agentic Reinforcement Learning with Implicit Step Rewards / iStar (ICLR 2026, arXiv:2509.19199)",
    "Agent-RLVR: Training Software Engineering Agents via Guidance and Environment Rewards (arXiv:2506.11425)",
    "Co-Evolving Agents: Learning from Failures as Hard Negatives (arXiv:2511.22254)",
    "RLAnything & DemyAgent: General Agentic RL Algorithms (ICML 2026)"
  ],
  "description": "An empirical short paper asking: does error-type conditioning improve GRPO-based agent recovery training? Fission-GRPO (ACL 2026) established error-triggered GRPO resampling for recovery, achieving +5.7% recovery rate on BFCL v4 Multi-Turn—but treats all errors uniformly. Stratified GRPO shows that stratified advantage normalization eliminates cross-stratum bias in heterogeneous GRPO groups. CoBA-RL/Knapsack RL show difficulty-proportional budget allocation outperforms uniform allocation. We combine these insights in Error-Type-Conditioned Fission (ETC-Fission): (1) error-type-conditioned fission budget K_τ ∝ 1-RR_pilot(τ), allocating more recovery branches to harder-to-recover error categories; (2) error-type-stratified advantage normalization, preventing easy-to-recover types (format errors) from dominating gradients over hard-to-recover types (function hallucination); (3) annotation-free recovery using BFCL v4's native error traces instead of Fission-GRPO's trained Error Simulator. We systematically compare ETC-Fission vs. uniform fission (Fission-GRPO reimplementation), entropy-triggered branching (AT²PO-style), standard GRPO, and AgentHER (SFT), all with Qwen3-8B on BFCL v4 Multi-Turn. The central contribution beyond method is error-type-stratified empirical analysis: per-type recovery rate, post-error success rate, and recovery efficiency breakdown revealing which error categories benefit from type-conditioned RL branching vs. uniform branching vs. SFT relabeling—a diagnostic absent from all prior work. We position honestly as extending Fission-GRPO with type conditioning (from CoBA-RL's difficulty-proportional principle) and type-stratified normalization (from Stratified GRPO's SAN), not claiming the error-triggered-GRPO intersection. Total compute: ≤110 H100 hours. Target: EMNLP 2026 short paper (ARR May 25, 2026).",
  "project_name": "etb_grpo_recovery",
  "source": "web_research",
  "change_type": "major"
}
```

**Summary of changes (major revision):**

1. **Repositioned against Fission-GRPO** — no longer claims "first to combine error-triggered branching with GRPO." Instead honestly builds on Fission-GRPO's paradigm, extending it with type conditioning.

2. **Cited Stratified GRPO** — acknowledged that stratified advantage normalization exists for search agents; positioned error-type strata as a domain-specific instantiation with recovery-specific motivation.

3. **Cited CoBA-RL and Knapsack RL** — acknowledged difficulty-proportional budget allocation exists for math reasoning; positioned K_τ as applying this principle at error-type granularity rather than task granularity.

4. **Switched benchmark from StableToolBench to BFCL v4** — StableToolBench's virtual API server suppresses error diversity (96-97% cache hit rate, no infrastructure errors). BFCL v4 provides structured error traces, up to 20 retries, and is the same benchmark as Fission-GRPO enabling direct comparison.

5. **Removed Error Simulator dependency** — BFCL v4 natively provides structured error traces. Fission-GRPO's ablation shows even generic messages help (+1.25%). Our approach is annotation-free.

6. **Added Fission-GRPO reimplementation as baseline** — "Uniform-Fission" without Error Simulator, plus optional Uniform-Fission+Simulator if feasible.

7. **Sharpened contribution to per-type empirical analysis** — the strongest novel contribution is the error-type-stratified analysis showing which error categories benefit from type-conditioned RL vs. uniform branching vs. SFT relabeling.

8. **Added RC-GRPO and GVPO to landscape** — RC-GRPO addresses complementary variance collapse problem; GVPO uses errors as generic process rewards without taxonomy.

9. **Reduced GPU estimate** — from ~130-150h to ~85-110h, since no Error Simulator training and BFCL v4 is simpler than StableToolBench.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de367d88-86df-4868-8eff-0128bd87685e",
  "isSidechain": false,
  "requestId": "req_011CawfT3k5P4L4ZerP5Edwo",
  "type": "assistant",
  "uuid": "e22cbf87-c969-42bb-b610-33197318297f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TcdAqiQVXqtZtejmKU5xMd",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2922,
      "cache_creation_input_tokens": 7649,
      "cache_read_input_tokens": 40039,
      "output_tokens": 12159,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7649,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2922,
          "output_tokens": 12159,
          "cache_read_input_tokens": 40039,
          "cache_creation_input_tokens": 7649,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7649
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

_source line 34_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-11 (UTC).**  ## Original idea {   \"title\": \"Error-Type-Conditioned Branching GRPO for Self-Supervised Agent Recove…",
  "leafUuid": "e22cbf87-c969-42bb-b610-33197318297f",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Error-type-aware branching for agent recovery beyond Fission-GRPO",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-11 (UTC).**  ## Original idea {   \"title\": \"Error-Type-Conditioned Branching GRPO for Self-Supervised Agent Recove…",
  "leafUuid": "e22cbf87-c969-42bb-b610-33197318297f",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c"
}
```

---

### Runtime record

_source line 37_

```json
{
  "type": "ai-title",
  "aiTitle": "Error-type-aware branching for agent recovery beyond Fission-GRPO",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c"
}
```

---
