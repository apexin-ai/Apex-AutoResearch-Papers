# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：Episode-level plateau 未突破或回退，双机制理论被 GAE 结果反驳，contrarian positioning 不成立，需要全

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/5dabea73-6dd0-4af0-be38-86df39e878a5.jsonl`
- **Structured JSON:** [`43cb352f66978b0f6cb1.json`](../../sessions/43/43cb352f66978b0f6cb1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-17T13:43:58.026Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-17T13:43:58.026Z",
  "sessionId": "5dabea73-6dd0-4af0-be38-86df39e878a5",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：Episode-level plateau 未突破或回退，双机制理论被 GAE 结果反驳，contrarian positioning 不成立，需要全新 angle\n核心假设：['Episode-level GRPO plateau 在 25-30%，未显著超过当前 step 15 的 28.125%', \"h-sweep cliff 不一致：部分 seed 无崩溃（h=5 也能学到 15-20%），削弱 'catastrophic failure' narrative\", 'Sign misattribution 实证模糊：sign-vs-outcome correlation 0.60-0.80，存在但非主因', 'GAE baseline 大幅优于 episode-level GRPO（>15pp），证明 per-token credit 是关键，episode-level 信息不够', 'Multi-seed std >8pp，部分 seed 成功部分 seed 失败，不 reproducible', 'Selective verification 不可行（base agent 太弱，无法做 cost-efficiency）', 'exp029 的 action_is_valid 持续低（~55%），模型未真正学到有效策略，只是 memorize 少量 pattern']\n关键指标范围：{'episode_level_val_success_converged': [0.22, 0.3], 'step_independent_h2_val_success': [0.0, 0.1], 'h_sweep_cliff_threshold': [3, 8], 'sign_vs_outcome_correlation': [0.6, 0.8], 'sign_vs_local_quality_correlation': [0.15, 0.35], 'gamma_k_magnitude_decay_r2': [0.3, 0.6], 'multi_seed_mean_success': [0.2, 0.3], 'multi_seed_std': [0.08, 0.15], 'gae_vs_episode_level_delta_pp': [12, 25], 'selective_verification_rate_reduction': [0.0, 0.15], 'selective_success_delta_vs_always_on_pp': [8, 20], 'scienceworld_episode_vs_step_ratio': [0.8, 1.5]}\n叙事方向：原始 framing 的两个支柱均不成立：(1) \"episode-level 就够了\" 被 GAE 反驳（finer credit 确实必要）， (2) \"catastrophic failure\" 被不一致的 h-sweep 削弱。需要完全 reframe。 新 angle 选项：(A) \"Empirical Taxonomy of Credit Assignment Failure Modes in LLM Agent RL\"—— 不再 claim 单一解法，而是系统分类不同 CA 方法（step-independent, episode-level, GAE, turn-level） 在不同条件下的 failure modes，填补 CA Survey (Zhang 2604.09459) 的实验空白。 h-sweep 的不一致性反而变成 contribution（\"failure mode 是 context-dependent，非 universal\"）。 (B) \"When Does Coarse Credit Assignment Suffice? Conditions for Episode-Level RL in Multi-Turn Agents\"—— 承认 episode-level 不是 universal solution，但找到它 work 的 sufficient conditions （task length, reward sparsity, action space size），变成 prescriptive guideline paper。 两个 angle 均需额外 2-3 个实验但不降 venue。Selective verification 完全放弃。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: cost-verify-agent-rl\nfocus: Post-novelty-check framing with updated competitive positioning: sign misattribution as deeper mechanistic characterization (not just \"uniform advantage\"), P(correct|update) quantification, dual mechanism separation, contrarian episode-level solution. Evaluate with updated experiment plan including γ-sweep, K-sweep, ScienceWorld transfer. Key question: does the contrarian positioning hold against Turn-PPO/GAGPO/HiPER competitors?\n\n## paper_framing.md\n\n# Paper Framing — Learning When to Verify: RL-Trained Selective Self-Verification for Interactive Agents\n\n> Post-MVP 重写 (2026-05-17) | D054 framing pivot + Dream Review feedback (weak reject → 修正理论)\n\n## Core Insight\n\nMulti-turn interactive agents 的 self-verification 大部分是 confirmatory（不改变行为）而非 corrective。训练 agent 学 selective verification 的前提是 RL 训练本身能 work。我们发现 LLM agent 社区默认的 step-independent training 在长 horizon 任务中灾难性崩溃，根因是**双机制失效**：\n\n1. **Policy Information Loss**: 短窗口（h 步）的 policy 无法学习跨步策略（如 \"先探索 drawer 再去 countertop\"）\n2. **Advantage Sign Misattribution**: step_independent 中，per-window advantage 的**符号**由 episode 成败决定，而非 window-local action quality：\n   - 失败 episode 中的好 action → 获得负 advantage（被错误惩罚）\n   - 成功 episode 中的差 action → 获得正 advantage（被错误强化）\n   - 梯度方向（reinforce/suppress）反映 episode outcome 而非 local decision quality\n   - 附加：γ^k magnitude decay 使早期 window 信号更弱（γ^24 ≈ 29%, where 24 = ⌈T/h⌉-1 windows），但方向错误比幅度衰减更致命\n\nEpisode-level training 同时解决两者：policy 看全历史（解决 1），整条 trajectory 作为一个 GRPO 样本，所有 tokens 共享同一 advantage — 虽然仍是 episode-level credit（非 per-token），但消除了 window 间的 sign misattribution，因为不再需要将 episode reward 分配到独立优化的子窗口（解决 2）。\n\n**技术澄清**：GRPO 算法本身是 bandit-style（advantage = (R-μ)/σ，无显式 γ），但 RAGEN 的 step_independent 实现在 `compute_step_discounted_returns()` 中引入 γ 计算每个 window 的 return（代码：`agent_trainer.py:271-340`）。γ^(T-t) decay 对 step_independent 模式是代码事实，不是类比。Episode-level 模式下无此问题：整条 trajectory 只有一个 return = episode_reward。\n\n## Story Arc\n\n**Dual contribution**: Training methodology diagnosis + Selective verification system\n\n叙事线：\n1. Self-verification 对 interactive agents 有用，但 always-on 成本高\n2. 训练 agent 学 WHEN to verify 需要 RL → 但 LLM agent 社区默认的 step-independent training 在多轮任务上灾难性崩溃（0% at step 10）\n3. 我们诊断双机制根因（information loss + advantage sign misattribution），提出 episode-level GRPO 解决\n4. 分析 \"为什么社区默认走向 step-independent\"（context window 限制 + token-level training 惯性 + framework design accident）\n5. 在 episode-level 基础上，用 action-change 作为 verification informativeness 的 reward，训练 selective policy\n6. 结果：near-always-on performance + 显著降低 verification cost\n\n**定位**：不 claim \"发明了 episode-level RL\"（trivial），而是 \"诊断了 LLM agent RL 训练中被忽视的 step-independent 隐性代价 + 系统分析崩溃机制 + 提出实用修复方案 + 在此基础上实现 selective verification\"\n\n## Target Venue\n\n待定（NeurIPS 2026 / EMNLP 2026 / ICLR 2026），取决于实验进度和最终效果。\n\n## Core Claims\n\n### Claim 1 (strength: strong): Step-independent GRPO catastrophically fails for multi-turn agents due to dual mechanism\n- 所需证据：episode-level vs step-independent 对比（多 seed），h-sweep ablation（3 seeds each），mechanistic analysis（gradient signal measurement），GAE baseline comparison\n- 当前证据状态：**ESTABLISHED** (exp029 step5 val=25% vs exp028c step10 val=0%)\n- 机制：(1) policy information loss (h-step context insufficient), (2) advantage sign misattribution (gradient direction reflects episode outcome, not window-local action quality; additionally γ^k magnitude decay for early windows)\n- 技术细节：GRPO 算法无固有 γ，但 RAGEN step_independent 的 `compute_step_discounted_returns()` 引入 γ-discounted per-window returns → advantage 符号由 episode 成败决定。代码验证：`agent_trainer.py:271-340` + `core_algos.py:194-246`\n\n### Claim 2 (strength: moderate): Action-change is an effective intrinsic reward for verification informativeness\n- 所需证据：selective verification 训练收敛 + action-change vs random/confidence baselines\n- 当前证据状态：**not yet established**，依赖 Phase B 实验\n- 前提：episode-level 训练的 agent 需达到 ≥40% success 才有意义\n\n### Claim 3 (strength: moderate): Learned selective policy matches always-on performance at reduced verification cost\n- 所需证据：B-IAVR verification ↓40%+ 且 success delta < 3pp vs always-on\n- 当前证据状态：**not yet established**，依赖 Phase B + C\n- 前提：Claim 1 的 agent 需足够强\n\n## Contingency Plan\n\n如果 episode-level 训练收敛后 success 仍 < 40%（不足以支撑 cost-efficiency story）：\n- **Plan A**：paper 变为 diagnostic + analysis contribution — \"Why Step-Independent RL Fails for LLM Multi-Turn Agents: Dual Mechanism Analysis\" (需更深 ablation + GAE comparison + community practice survey)\n- **Plan B**：加 Self-Guide reward 到 episode-level（从 binary→dense reward），推高 performance 后再做 selective verification\n- 不考虑 downgrade venue\n- **注意**：Dream review 已证明 Plan A 纯 methodology paper 需要比预期更深的分析才能通过审稿（\"诊断社区默认实践的隐性代价\" > \"episode-level RL works\"）\n\n## Reviewer Attack Surface + Defense\n\n| # | Concern | Severity | Defense |\n|---|---------|----------|---------|\n| 1 | \"Episode-level RL is obvious / well-known\" | HIGH | h-sweep (3 seeds) 展示 non-trivial cliff + 双机制理论 + \"为什么社区默认 step-independent\" 分析 |\n| 2 | \"Theory 与 GRPO 不匹配\" | HIGH | 精确区分：GRPO 算法无 γ，但 step_independent 实现引入 γ-discounted returns（代码引用）→ per-window advantage logging 实证 + 伪代码 |\n| 3 | \"缺 GAE/标准 RL baselines\" | HIGH | 加 GAE(λ=0.95) + GAE(λ=1,γ=1) baseline，证明 episode-level GRPO 与 GAE 的差异 |\n| 4 | \"Self-Guide 3x performance gap\" | HIGH | 正面回应：不同 paradigm (expert-guided vs from-scratch RL)，不同问题（Self-Guide 回避了训练问题） |\n| 5 | Single environment (ALFWorld) | MEDIUM | ScienceWorld transfer (if resources permit) |\n| 6 | Small model (1.7B) | MEDIUM | 定位 resource-constrained; 7B 验证 (conditional) |\n| 7 | Action-change = noise vs signal | MEDIUM | Entropy-controlled analysis + causal intervention (Phase B) |\n| 8 | 与 ARES 差异化不足 | LOW | Head-to-head 对比 + 方法论差异表 |\n| 9 | \"Turn-PPO 已解决相同问题\" | HIGH | 精确区分：Turn-PPO 发现 uniform advantage (subset)，我们发现 sign misattribution (superset + 量化 γ^24≈29%)；解法相反 (finer vs coarser) |\n\n## Evidence Status Matrix\n\n| Claim | MVP Evidence | Research Evidence Needed | Priority |\n|-------|-------------|--------------------------|----------|\n| Claim 1 | exp029 vs exp028c (25% vs 0%) | h-value ablation, multi-seed, mechanism paper figure | P0 |\n| Claim 2 | N/A | Phase B full implementation | P1 |\n| Claim 3 | N/A | Phase B + C comparison suite | P1 |\n\n## Competitive Positioning\n\n| System | Method | Benchmark | Key Difference from Us |\n|--------|--------|-----------|----------------------|\n| Self-Guide (2026) | Always-on verification | ALFWorld 72.7% (1.7B) | We add selectivity via RL |\n| ARES (2603.07915) | SFT router, continuous effort | 52.7% token reduction | SFT vs RL, continuous vs binary |\n| Thinkless (NeurIPS'25) | RL control token | reasoning domain | Same RL philosophy, different domain |\n| ReflAct (EMNLP'25) | Prompting GPT-4 | ALFWorld 93.3% | Different scale/approach |\n| RAGEN (2025) | GRPO for agents | varies | Step-independent default, our baseline |\n| **Turn-PPO (2512.17008)** | Turn-level MDP + value fn | reasoning tasks | \"Uniform advantage\" vs our \"sign misattribution\"; finer credit vs coarser |\n| **GAGPO (2605.13217)** | Grouped value proxy, step-aligned | ALFWorld 93.5% (1.5B) | Finer-grained credit for performance; we diagnose mechanism failure |\n| **MT-GRPO (2505.11821)** | Turn-level reward design | QA search tasks | Turn-level credit; we show coarser suffices |\n| **iStar (ICLR'26)** | Implicit PRM + dual advantage | WebShop 86.5% | Learns step rewards; we show episode-level eliminates misattribution |\n| **ArCHer (ICML'24)** | Hierarchical multi-turn RL | multi-turn agents | Foundational framework; establishes need for hierarchical structure |\n| **HiPER (2602.16165)** | Hierarchical Plan-Execute RL | ALFWorld 97.4% (7B) | SOTA performance pursuit; we do mechanism diagnosis |\n\n### Positioning Strategy\n\n**核心差异化：Contrarian Solution。** 竞品（Turn-PPO, GAGPO, MT-GRPO, iStar, HiPER）一致认为 multi-turn RL 需要更细粒度的 credit assignment（turn-level, step-level, hierarchical），并用此提升性能。我们的贡献是诊断性的：\n\n1. **问题定义更精确**：Turn-PPO 发现 \"uniform advantage\" 问题（所有 turn 获得相同 advantage），我们发现更本质的 \"Advantage Sign Misattribution\"（advantage 符号由 episode outcome 决定而非 local action quality），并量化 γ^24 ≈ 29% 的 return 衰减。Sign misattribution 是 uniform advantage 的超集。\n\n2. **Contrarian solution**：所有竞品的解法都是引入更细的 credit（turn-level value, step-level PRM, hierarchical planner）。我们展示更粗的 episode-level credit 反而消除 sign misattribution，因为它避免了将 episode reward 错误分配到独立优化的子窗口。这挑战了 \"越细越好\" 的社区默认假设。\n\n3. **不同 contribution 维度**：GAGPO/HiPER 追求 ALFWorld 93-97% 的 SOTA performance（通过更好的 credit + 更复杂的架构）。我们不 compete on performance axis，而是回答 \"为什么社区默认的 step-independent 灾难性失败\" 这个诊断问题。两个 contribution 维度正交互补。\n\n4. **与 CA Survey 的关系**：Zhang (2604.09459) 系统化了 47 种 CA 方法，但未分析 CA 方法本身的 failure modes（何时更细粒度反而有害）。我们填补这一空白。\n\n## Research Phases\n\n1. **Phase A (DONE)**: Episode-level GRPO training — MVP passed, demonstrates Claim 1\n2. **Phase A+**: Continue training to convergence (target ≥40% success), deploy tatsu parallel patch, multi-seed\n3. **Phase B**: Implement selective verification with action-change reward — Claim 2 & 3\n4. **Phase C**: Ablation suite — context window sweep, reward ablations, baseline comparisons\n5. **Phase D**: (Conditional on resources) Multi-env / multi-model scaling\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  title: Episode-level GRPO convergence (exp029 continuation)\n  claim: Claim 1\n  phase: A+\n  priority: P0\n  depends_on: []\n  registry_id: exp029_episode_level\n  status: DONE\n  description: 'Episode-level GRPO (context_window_mode: full) on Qwen3-1.7B + ALFWorld.\n    50 steps, dual-GPU. MVP passed at step 5 (val=25%, 2x baseline 12.5%). Continue\n    to convergence (step 20+) with tatsu parallel patch for 4x val speedup.\n\n    '\n  hypothesis: 'Episode-level training enables stable RL for multi-turn agents, reaching\n    ≥40% success by convergence.\n\n    '\n  metrics:\n    current_step: 15\n    total_steps: 100\n    progress_pct: 15\n    step5_val_success: 0.25\n    step10_val_success: 0.25\n    step15_val_success: 0.28125\n    step15_val_pass_at_1: 0.28125\n    step15_val_pass_at_2: 0.469\n    step15_val_pass_at_4: 0.726\n    step15_val_pass_at_8: 0.929\n    step15_val_pass_at_16: 0.996\n    step15_val_action_is_valid: 0.5452\n    step15_val_action_is_effective: 0.7672\n    step15_val_manager_invalid_action: 0.2328\n    step15_train_success: 0.4375\n    step15_train_pass_at_8: 0.75\n    elapsed_hours: 7.35\n    eta_completion: '2026-05-19T03:00:00Z'\n  gpu_hours_estimate: 48\n  framing_ref: claim_1\n  conclusion: success\n- id: plan_002\n  title: Context window h-sweep ablation (3 seeds each)\n  claim: Claim 1\n  phase: A+\n  priority: P0\n  depends_on:\n  - plan_001\n  registry_id: null\n  status: planned\n  description: 'Sweep context_window h={2, 5, 10, 20, full} on same GRPO config. Config:\n    context_window_mode=step_independent + step_independent_history_length={h} (h=full\n    uses context_window_mode=full). 15 steps per run, 3 seeds each. KEY paper figure:\n    shows credit assignment cliff is robust across seeds. Addresses Reviewer Concern\n    #1 + Dream C3 (statistical power).\n\n    '\n  hypothesis: 'Performance degrades monotonically with smaller h, with sharp cliff\n    below h=10. Cliff is robust across seeds (not single-run artifact).\n\n    '\n  metrics:\n  - success_rate_per_h\n  - convergence_speed\n  - collapse_rate\n  gpu_hours_estimate: 90\n  notes: 5 h-values × 15 steps × 3 seeds. h=2 已有 exp028c 作 1 seed。\n- id: plan_003\n  title: Multi-seed replication (5 seeds total)\n  claim: Claim 1\n  phase: A+\n  priority: P0\n  depends_on:\n  - plan_001\n  registry_id: null\n  status: planned\n  description: '4 additional seeds for exp029 episode-level config (5 total incl original).\n    Report mean ± std. Dream C3 要求 5-8 seeds for credible CI.\n\n    '\n  hypothesis: 'Episode-level success rate is reproducible (std < 5pp across 5 seeds).\n\n    '\n  metrics:\n  - success_rate_mean\n  - success_rate_std\n  gpu_hours_estimate: 192\n- id: plan_003b\n  title: GAE baseline comparison\n  claim: Claim 1\n  phase: A+\n  priority: P0\n  depends_on:\n  - plan_001\n  registry_id: null\n  status: planned\n  description: 'Dream C4 要求标准 RL baselines。实现 GAE(lambda=0.95, gamma=1.0) 和 GAE(lambda=1.0,\n    gamma=1.0) 在 RAGEN 中。需要 value function (critic head)。 15 steps × 3 seeds each。如果\n    GAE >> episode-level GRPO → per-token credit assignment 额外有价值。如果持平 → episode-level\n    信息是关键。 GRPO episode-level ≠ GAE(1,1)：GRPO 无 critic，所有 token 同一 advantage。\n\n    '\n  hypothesis: 'GAE provides modest improvement over episode-level GRPO due to finer\n    credit assignment, but both far exceed step-independent.\n\n    '\n  metrics:\n  - success_rate\n  - per_token_advantage_variance\n  gpu_hours_estimate: 60\n  notes: 需实现 critic head。如果实现成本过高，可用 REINFORCE baseline 替代。\n- id: plan_003c\n  title: Episode-level + valid_action_bonus (plateau-breaker, D056)\n  claim: Claim 1\n  phase: A+\n  priority: P0\n  depends_on:\n  - plan_001\n  registry_id: null\n  status: planned\n  description: 'Derived from exp013f negative (D056): dense reward gaming is step_independent-specific.\n    Episode-level training prevents per-step reward gaming because model optimizes\n    full trajectory total reward. Add valid_action_bonus=0.05 to episode-level config.\n    Test if this safely improves action_is_valid (currently 55.9%) without gaming,\n    and whether it breaks the 23-25% success plateau. Run during h-sweep batch as\n    h=full variant.\n\n    '\n  hypothesis: 'Episode-level + small valid_action_bonus safely improves action_is_valid\n    (target ≥80%) without reward gaming, and success rate exceeds 30% (breaking exp029\n    plateau). Gaming only occurs under step_independent.\n\n    '\n  metrics:\n  - success_rate\n  - action_is_valid\n  - valid_bonus_vs_task_reward_ratio\n  gpu_hours_estimate: 24\n  parent: exp013f\n  notes: 'Parent derivation: exp013f gaming → D056 insight → episode-level safety\n    hypothesis'\n- id: plan_004\n  title: Credit assignment mechanism empirical verification (paper Figure 2)\n  claim: Claim 1\n  phase: A+\n  priority: P0\n  depends_on:\n  - plan_002\n  registry_id: null\n  status: planned\n  description: \"Empirically verify \\\"Advantage Sign Misattribution\\\" mechanism (D058,\\\n    \\ Reviewer-refined): (a) Per-window advantage logging from h=2 seed 2: record\\\n    \\ (episode_id, window_position,\\n    raw_return, advantage_sign, advantage_magnitude,\\\n    \\ episode_outcome, local_action_quality_proxy)\\n(b) Key analysis: advantage sign\\\n    \\ vs episode outcome correlation (should be ~1.0),\\n    advantage sign vs local\\\n    \\ action quality correlation (should be ~0, proving misattribution)\\n(c) Contrast\\\n    \\ success vs failure episodes: success → all positive (including bad windows),\\n\\\n    \\    failure → all negative (including good windows)\\n(d) γ^k magnitude decay:\\\n    \\ advantage magnitude vs position in success episodes (e) Episode-level control:\\\n    \\ all tokens share one advantage (no position/sign variance) Data source: LOG_PER_SAMPLE_ADV=1\\\n    \\ on h=2 seed 2 (10 lines logging code, zero GPU overhead). Code reference: agent_trainer.py:271-340,\\\n    \\ core_algos.py:194-246.\\n\"\n  hypothesis: 'Per-window advantage in step_independent shows: (1) advantage sign\n    is determined by episode success/failure (correlation > 0.95), (2) advantage sign\n    is NOT correlated with window-local action quality (r < 0.1), proving sign misattribution,\n    (3) magnitude decays as γ^k from terminal position, (4) episode-level shows uniform\n    advantage with no sign/magnitude position effects.\n\n    '\n  metrics:\n  - sign_vs_outcome_correlation\n  - sign_vs_local_quality_correlation\n  - magnitude_position_decay_r2\n  - episode_level_variance\n  gpu_hours_estimate: 4\n  notes: 'D058+Reviewer: ''sign misattribution'' is the core mechanism (direction\n    error > magnitude error). γ^k decay is secondary.'\n- id: plan_005\n  title: Action-change statistics from always-on runs\n  claim: Claim 2\n  phase: B\n  priority: P1\n  depends_on:\n  - plan_001\n  registry_id: null\n  status: planned\n  description: 'Collect action-change statistics from exp029 trained checkpoints:\n    (1) fraction of verifications triggering action change, (2) correlation between\n    action change and episode success, (3) per-task-type breakdown. Informs reward\n    design and provides empirical grounding.\n\n    '\n  hypothesis: 'Most verifications are confirmatory (>60% no action change). Action\n    change positively correlates with episode success (r > 0.2).\n\n    '\n  metrics:\n  - action_change_rate\n  - correlation\n  - confirmatory_rate\n  gpu_hours_estimate: 4\n- id: plan_006\n  title: Selective verification implementation\n  claim: Claim 2\n  phase: B\n  priority: P1\n  depends_on:\n  - plan_005\n  registry_id: null\n  status: planned\n  description: 'Implement binary verify/skip decision in RAGEN framework. Agent outputs\n    special token (verify/skip) before each step. Reward = task_success + alpha *\n    action_change_when_verified - beta * verification_cost. Code-only, no GPU.\n\n    '\n  hypothesis: null\n  metrics: []\n  gpu_hours_estimate: 0\n- id: plan_007\n  title: B-IAVR selective verification training\n  claim: Claim 2, Claim 3\n  phase: B\n  priority: P1\n  depends_on:\n  - plan_006\n  - plan_001\n  registry_id: null\n  status: planned\n  description: 'Train selective verification policy via episode-level GRPO. Initialize\n    from best exp029 checkpoint. Action-change reward encourages verification only\n    when informative.\n\n    '\n  hypothesis: 'B-IAVR achieves verification rate ↓40%+ vs always-on while maintaining\n    success within 5pp of baseline.\n\n    '\n  metrics:\n  - success_rate\n  - verification_rate\n  - cost_reduction\n  gpu_hours_estimate: 96\n- id: plan_008\n  title: Selective verification full comparison\n  claim: Claim 3\n  phase: B\n  priority: P1\n  depends_on:\n  - plan_007\n  registry_id: null\n  status: planned\n  description: 'Compare on same val set: always-on / B-IAVR / no-verify / random-p\n    / confidence-threshold. Report success rate, verification rate, total inference\n    tokens, per-task breakdown.\n\n    '\n  hypothesis: 'B-IAVR dominates Pareto frontier (best success-to-cost ratio).\n\n    '\n  metrics:\n  - success_rate\n  - verification_rate\n  - cost_reduction\n  - total_tokens\n  gpu_hours_estimate: 8\n- id: plan_009\n  title: No-verify ablation\n  claim: Claim 3\n  phase: C\n  priority: P1\n  depends_on:\n  - plan_001\n  registry_id: null\n  status: planned\n  description: 'Episode-level GRPO without any self-verification. Lower bound: demonstrates\n    verification value.\n\n    '\n  hypothesis: 'Removing verification drops success by ≥10pp vs always-on.\n\n    '\n  metrics:\n  - success_rate\n  - action_is_valid\n  gpu_hours_estimate: 48\n- id: plan_010\n  title: Entropy-controlled action-change analysis\n  claim: Claim 2\n  phase: C\n  priority: P1\n  depends_on:\n  - plan_005\n  registry_id: null\n  status: planned\n  description: 'Defense for \"action change = noise\" concern. Stratify by policy entropy;\n    test if action-change-success correlation holds within each stratum.\n\n    '\n  hypothesis: 'Partial correlation remains significant (p < 0.05) after controlling\n    entropy.\n\n    '\n  metrics:\n  - partial_correlation\n  - p_value\n  gpu_hours_estimate: 4\n- id: plan_011\n  title: 'Causal intervention: random vs verification-triggered changes'\n  claim: Claim 2\n  phase: C\n  priority: P1\n  depends_on:\n  - plan_001\n  registry_id: null\n  status: planned\n  description: 'Inject random action changes at same rate as verification-triggered.\n    Compare task success. If verification-triggered >> random, causal evidence.\n\n    '\n  hypothesis: 'Verification-triggered changes yield ≥10pp higher success than random.\n\n    '\n  metrics:\n  - success_rate_triggered\n  - success_rate_random\n  - delta\n  gpu_hours_estimate: 8\n- id: plan_012\n  title: Reward signal ablation (action-change vs alternatives)\n  claim: Claim 2\n  phase: C\n  priority: P1\n  depends_on:\n  - plan_007\n  registry_id: null\n  status: planned\n  description: 'Train B-IAVR with alternative rewards: (a) action-change (ours), (b)\n    random trigger reward, (c) confidence-based reward. Demonstrates action-change\n    is the best signal.\n\n    '\n  hypothesis: 'Action-change reward produces best cost-performance tradeoff.\n\n    '\n  metrics:\n  - success_rate\n  - verification_rate\n  - cost_reduction\n  gpu_hours_estimate: 192\n- id: plan_013\n  title: ARES reproduction + comparison\n  claim: Claim 3\n  phase: C\n  priority: P1\n  depends_on:\n  - plan_007\n  registry_id: null\n  status: planned\n  description: 'Reproduce ARES SFT router on ALFWorld (same model). Head-to-head with\n    B-IAVR on identical eval episodes. Addresses \"ARES differentiation\" concern.\n\n    '\n  hypothesis: 'B-IAVR achieves ≥10pp better cost reduction than ARES at matched success.\n\n    '\n  metrics:\n  - success_rate\n  - verification_rate\n  - cost_reduction\n  gpu_hours_estimate: 24\n- id: plan_014\n  title: ScienceWorld transfer (episode-level advantage)\n  claim: Claim 1\n  phase: D\n  priority: P2\n  depends_on:\n  - plan_001\n  registry_id: null\n  status: planned\n  description: 'Validate episode-level vs step-independent on ScienceWorld. Different\n    env, similar multi-turn structure. Addresses single-env concern.\n\n    '\n  hypothesis: 'Episode-level advantage generalizes: ≥2x improvement over step-independent.\n\n    '\n  metrics:\n  - success_rate_episode\n  - success_rate_step_independent\n  gpu_hours_estimate: 72\n- id: plan_015\n  title: 7B model scaling verification\n  claim: Claim 1\n  phase: D\n  priority: P2\n  depends_on:\n  - plan_002\n  registry_id: null\n  status: planned\n  description: 'Episode-level vs step-independent on Qwen3-7B. Addresses model size\n    concern. May need cloud GPU.\n\n    '\n  hypothesis: 'Episode-level advantage holds at 7B scale.\n\n    '\n  metrics:\n  - success_rate_episode_7B\n  - success_rate_step_independent_7B\n  gpu_hours_estimate: 192\n  notes: May require cloud GPU rental (4x A100 or 2x H100)\n- id: plan_016\n  title: Per-task-type breakdown analysis\n  claim: Claim 1\n  phase: D\n  priority: P2\n  depends_on:\n  - plan_001\n  registry_id: null\n  status: planned\n  description: 'Breakdown by ALFWorld task type (pick, clean, heat, cool, examine,\n    pick_two). Shows within-environment diversity.\n\n    '\n  hypothesis: 'Episode-level advantage varies by task complexity; longer tasks benefit\n    more.\n\n    '\n  metrics:\n  - per_task_success\n  - episode_length_correlation\n  gpu_hours_estimate: 2\n\n\n## registry (completed experiments)\n\n- exp_id: exp_001\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001b\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_002\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_003\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_003_dryrun\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_003_dryrun2\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp003_dryrun3\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_003_dryrun3\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp003\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp005\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp007\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    steps_completed: 10\n    steps_planned: 30\n    crash_reason: 'OSError: No space left on device (/tmp)'\n    final_success_rate: 0.0625\n    final_action_is_valid: 0.0835\n    final_manager_invalid_action: 0.0156\n    final_pass_at_8: 0.375\n    final_pg_loss: 0.00117\n    final_ppo_kl: 0.00127\n    final_entropy: 0.057\n    final_score_mean: 0.578\n    dryrun_action_is_valid: 0.054\n    dryrun_invalid_action: 0.065\n    training_time_s: 6739\n- exp_id: exp007_dryrun\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp008\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp008_sft\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    action_is_valid: 0.9\n    format_ok: 1\n    success_rate: 0\n    final_loss: 0.069\n    final_token_accuracy: 0.973\n    data_count: 1200\n    epochs: 3\n    total_steps: 225\n    training_time_s: 576\n- exp_id: exp009\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp010\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    step: 11\n    total_steps: 30\n    crash_reason: /tmp disk full (fast_downward libdownward.so)\n    initial_val_action_is_valid: 0.652\n    initial_val_success: 0\n    step1_success: 0.047\n    step1_pass_at_8: 0.375\n    step1_action_is_valid: 0.588\n    step10_success: 0\n    step10_pass_at_8: 0\n    step10_action_is_valid: 0.683\n    step5_ppo_kl: 0.00158\n    step5_entropy: 0.1\n    trend: action_is_valid improving (58.8%→68.3%) but success collapsing (4.7%→0%)\n    checkpoint_saved: global_step_10\n- exp_id: exp011\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp012\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp012b\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    step: 8\n    total_steps: 30\n    step6_success: 0.0859\n    step6_action_is_valid: 0.613\n    step6_pass_at_16: 0.5\n    step6_ppo_kl: 0.0039\n    step6_entropy: 0.1006\n    step6_grad_norm: 1.477\n    step7_success: 0\n    step7_action_is_valid: 0.685\n    step7_pass_at_16: 0\n    step7_pg_loss: 0\n    step7_ppo_kl: 0.00439\n    step7_entropy: 0.0904\n    step7_grad_norm: 0.094\n    trend: success 8.6%→0% collapse at step 7 (same pattern as exp010, delayed 1 step).\n      grad_norm 1.477→0.094, pg_loss→0. Reward fix delayed but did not prevent collapse.\n- exp_id: exp013\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp013b\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp013c\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp013d\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp013e\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp013f\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    step: 30\n    total_steps: 30\n    completed: true\n    exit_code: 0\n    training_time_s: 10683\n    step6_success: 0.0156\n    step7_success: 0.0781\n    step10_success: 0\n    step17_success: 0.0156\n    final_val_success: 0\n    final_val_action_is_valid: 0.975\n    final_val_action_is_effective: 1\n    final_val_reward_mean_at4: 4.388\n    final_val_reward_std_at4: 0.195\n    final_val_reward_best_at4: 4.499\n    final_val_pass_at1: 0\n    action_is_valid_trend: 60%→65.9%→77.1%→97.5%\n    success_trend: 0%→1.56%→7.81%→0%→1.56%→0%\n    grad_norm_range: 1.7-2.9 (no collapse)\n    conclusion_reason: 'Dense reward gaming: model optimized valid_action_bonus (action_is_valid\n      60%→97.5%) but success stayed 0%. Reward ratio 1:67 too weak — cumulative valid_action_bonus\n      (4.5) dominated learning signal vs sparse success_reward (10.0). GRPO collapse\n      prevented but task completion not learned.'\n- exp_id: exp014c\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp014a\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp014b\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp015\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    step: 1\n    total_steps: 30\n    val_step0_success: 0\n    val_step0_action_is_valid: 0.858\n    val_step0_pass_at1: 0\n    val_step0_episodic_return: 0\n    val_step0_response_length: 2797.5\n    val_train_transition: passed\n    estimated_total_time_min: 163\n    time_per_step_min: 5.6\n- exp_id: exp016\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    step: 12\n    total_steps: 30\n    elapsed_min: 51\n    step6_success: 0\n    step6_action_is_valid: 0.521\n    step6_pg_loss: 0\n    step6_grad_norm: 0.841\n    step7_success: 0.047\n    step7_pass_at16: 0.5\n    step7_action_is_valid: 0.655\n    step10_success: 0\n    step10_action_is_valid: 0.664\n    step10_pg_loss: 0\n    step10_grad_norm: 0.856\n    step10_entropy: 0.1046\n    step10_ppo_kl: -9.1e-05\n    all_raw_rewards: 0\n    all_advantages: 0\n    all_returns: 0\n    reward_signal: BROKEN — success episodes get reward=0\n    action_is_valid_trend: 52.1%→65.5%→66.4%\n    manager_invalid_action_trend: 13.5%→11.2%→9.6%\n- exp_id: exp017_expert_sft\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_train_loss: 0.1434\n    final_step_loss: 0.04\n    final_token_accuracy: 0.983\n    epochs: 3\n    total_steps: 462\n    training_time_min: 26\n    data_count_train: 2460\n    data_count_val: 129\n    checkpoint_size_gb: 3.44\n    eval_success_rate: 0.05\n    eval_success: 1/20\n    eval_action_is_valid: 0.638\n    eval_format_ok: 0.75\n    eval_avg_steps: 22\n    eval_time_s: 149.6\n    eval_per_task:\n      put: 0/10\n      clean: 0/4\n      cool: 1/3\n      heat: 0/2\n      examine: 0/1\n    eval_parse_failures: 5/20 episodes (EP 7/12/16/17/18)\n- exp_id: exp018_sft_grpo\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp019_expert_sft_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp019b_expert_sft_v2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp019b_expert_sft_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.0718\n    eval_loss: 0.0428\n    eval_mean_token_accuracy: 0.9869\n    train_runtime_seconds: 2869.8\n    steps: 320\n    epochs: 2\n    eval_success_rate: 0.2\n    eval_format_ok: 1\n    eval_action_is_valid: 0.8533\n    eval_episodes: 20\n    eval_avg_steps: 25.4\n    eval_time_seconds: 146\n- exp_id: exp019c_expert_sft_v3\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp020_grpo_from_sft\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp020b_grpo_from_sft\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    steps_completed: 22\n    steps_planned: 30\n    hung_at_step: 23\n    step1_train_success: 0.1875\n    step10_train_success: 0.1875\n    step20_train_success: 0.125\n    step22_train_success: 0.0469\n    val_success_step0: 0\n    val_success_step20: 0\n    entropy_initial: 0.107\n    entropy_final: 0.042\n    grad_norm_initial: 2.78\n    grad_norm_step20: 5.58\n    ppo_kl_final: 0.00918\n    pass_at_16_step1: 0.75\n    pass_at_16_step22: 0.25\n    checkpoint_latest: global_step_20\n    training_status: hung_at_step23_rollout\n- exp_id: exp020c_grpo_from_sft\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp020d_grpo_from_sft\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp021_sft_ragen_format\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp021_ragen_sft_v4\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    train_loss_final: 0.038\n    train_token_accuracy: 0.988\n    train_steps: 320\n    train_epochs: 2\n    train_time_min: 47.8\n    ragen_val_success: 0.25\n    ragen_val_action_is_valid: 0.875\n    eval_sft_fast_success: 0\n    eval_sft_fast_format_ok: 1\n    eval_sft_fast_action_is_valid: 0.71\n    checkpoint_size_gb: 3.3\n    ragen_val_success_16ep: 0.0625\n    ragen_val_action_is_valid_16ep: 0.6875\n- exp_id: exp022_grpo_from_sft_v4\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    steps_completed: 1\n    steps_planned: 30\n    val_step0_success: 0.125\n    val_step0_action_is_valid: 0.4875\n    val_step0_action_is_effective: 1\n    val_step0_reward_mean: 1.25\n    val_step0_reward_best: 6.61\n    val_step0_episodes: 8\n    step_time_seconds: 208\n- exp_id: exp023_grpo_parallel\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp023c_grpo_serial\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    val_step0_success: 0.0625\n    val_step0_action_is_valid: 0.6875\n    val_step0_episodes: 16\n    train_step1_success: 0.297\n    train_step1_action_is_valid: 0.791\n    train_step1_entropy: 0.0652\n    train_step1_pass16: 0.75\n    train_step1_kl: 0.000156\n    train_step8_success: 0.234\n    train_step8_action_is_valid: 0.779\n    train_step8_entropy: 0.0555\n    train_step8_pass16: 0.5\n    train_step8_kl: 0.000475\n    steps_completed: 8\n    steps_planned: 30\n    step_time_seconds_start: 240\n    step_time_seconds_end: 365\n- exp_id: exp024_success_gated_grpo\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp025\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp025b\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp025c\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp026_step_independent_grpo\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    val_before_train_success: 0.0625\n    val_before_train_action_is_valid: 0.631\n    val_before_train_episodes: 16\n    train_step1_success: 0.2188\n    train_step1_action_is_valid: 0.686\n    train_step1_entropy: 0.2672\n    train_step1_kl_loss: 0.1797\n    train_step1_grad_norm: 14.43\n    train_step1_reward_mean: 1.218\n    train_step1_pass_at_16: 1\n    train_step2_success: 0.3281\n    train_step2_action_is_valid: 0.603\n    train_step2_entropy: 0.317\n    train_step2_kl_loss: 0.0974\n    train_step2_grad_norm: 15.62\n    train_step2_reward_mean: 1.62\n    train_step2_pass_at_16: 1\n    train_step3_success: 0.1719\n    train_step3_action_is_valid: 0.641\n    train_step3_entropy: 0.387\n    train_step3_kl_loss: 0.2617\n    train_step3_grad_norm: 15.65\n    train_step3_reward_mean: 1.079\n    train_step3_pass_at_16: 0.75\n    train_step4_success: 0\n    train_step4_action_is_valid: 0.717\n    train_step4_entropy: 0.387\n    train_step4_kl_loss: 0.054\n    train_step4_grad_norm: 13.81\n    train_step4_pass_at_16: 0\n- exp_id: exp027_stable_grpo\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    step_0_val_before_train:\n      success: 6.25\n      action_is_valid: 63.125\n      action_is_effective: 87.875\n      num_actions: 42.375\n      response_length: 114.67\n      reward_mean: 0.3226\n      val_generation_time_s: 502.57\n    step_1_train:\n      success: 35.94\n      kl_loss: 0.058\n      batch_size: 5152\n      training_time_s: 4342\n    step_2_train:\n      success: 10.16\n      kl_loss: 0.413\n      batch_size: 6144\n      training_time_s: 5886\n    step_3_train:\n      success: 10.16\n      kl_loss: 0.248\n      entropy: 0.385\n      pass_at_16: 0.5\n      grad_norm: 21.31\n      reward_mean: 0.483\n      batch_size: 6048\n      training_time_s: 4689\n    step_4_train:\n      success: 13.28\n      pass_at_16: 0.375\n      note: 'Director判定: 趋势确认, MVP未通过'\n- exp_id: exp028_prereq_zeroshot_instruct\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp028a_recipe_fix\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp028_prereq_zeroshot\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    success: 0\n    action_is_valid: 0.75\n    num_actions: 50\n    pass_at_1: 0\n    response_length: 75.07\n- exp_id: exp028c_selfguide_recipe\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    step_0_val:\n      success: 6.25\n      pass_at_1: 6.25\n      action_is_valid: 74.5\n      score_mean: 0.119\n    step_1_train:\n      success: 13.28\n      pass_at_8: 37.5\n      action_is_valid: 76.4\n      action_is_effective: 96.37\n      entropy: 0.2634\n      kl_loss: 0.0128\n      ppo_kl: 0.019\n      grad_norm: 16.88\n      score_mean: 0.843\n      time_s: 3252\n      note: 三方交叉验证通过\n    step_2_train:\n      success: 6.25\n      pass_at_8: 25\n      action_is_valid: 83.2\n      entropy: 0.247\n      kl_loss: 0.1706\n      pg_loss: 0.007\n      grad_norm: 17.3\n      score_mean: 0.274\n      time_s: 3120\n    step_3_train:\n      success: 15.63\n      pass_at_8: 68.75\n      action_is_valid: 85.9\n      entropy: 0.2488\n      kl_loss: 0.1118\n      grad_norm: 12.57\n      score_mean: 0.661\n      time_s: 2760\n    step_4_train:\n      success: 18.75\n      pass_at_8: 62.5\n      action_is_valid: 87.94\n      entropy: 0.234\n      kl_loss: 0.031\n      ppo_kl: 0.015\n    step_5_train:\n      success: 9.4\n      pass_at_8: 37.5\n      action_is_valid: 89.6\n      entropy: 0.236\n      kl_loss: 0.824\n      grad_norm: 13.1\n    step_5_val:\n      success: 6.25\n      pass_at_1: 6.25\n      action_is_valid: 96.5\n      action_is_effective: 100\n      num_actions: 49.4\n      score_mean: 0.518\n    step_6_train:\n      success: 10.94\n      action_is_valid: 90.4\n      entropy: 0.234\n      kl_loss: 0.098\n      grad_norm: 12.54\n    step_7_train:\n      success: 21.88\n      pass_at_8: 56.25\n      action_is_valid: 91.8\n      entropy: 0.224\n      kl_loss: 0.046\n    step_8_train:\n      success: 15.6\n      pass_at_8: 50\n      action_is_valid: 92.7\n      kl_loss: 0.039\n      entropy: 0.204\n    step_9_train:\n      success: 18\n      pass_at_8: 56.3\n      action_is_valid: 93.6\n      kl_loss: 0.047\n      entropy: 0.204\n    step_10_train:\n      success: 18.75\n      action_is_valid: 90.7\n      kl_loss: 0.197\n    step_10_val:\n      success: 0\n      pass_at_1: 0\n      best_at_128: 0\n      best_at_800: 0\n      action_is_valid: 93.6\n      num_actions: 49.8\n      reward_mean: 0\n      note: 灾难性崩溃，模型完全遗忘\n- exp_id: exp029_episode_level\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    current_step: 15\n    total_steps: 100\n    progress_pct: 15\n    step5_val_success: 0.25\n    step10_val_success: 0.25\n    step15_val_success: 0.28125\n    step15_val_pass_at_1: 0.28125\n    step15_val_pass_at_2: 0.469\n    step15_val_pass_at_4: 0.726\n    step15_val_pass_at_8: 0.929\n    step15_val_pass_at_16: 0.996\n    step15_val_action_is_valid: 0.5452\n    step15_val_action_is_effective: 0.7672\n    step15_val_manager_invalid_action: 0.2328\n    step15_train_success: 0.4375\n    step15_train_pass_at_8: 0.75\n    elapsed_hours: 7.35\n    eta_completion: '2026-05-19T03:00:00Z'\n- exp_id: hsweep_h2_seed1\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics:\n    train_step: 9\n    total_steps: 15\n    wandb_run_id: 7o9bjszm\n    step1:\n      success: 0.1875\n      pass_at_8: 0.4375\n      invalid_action: 0.027\n    step2:\n      success: 0.1484\n      pass_at_8: 0.5\n      invalid_action: 0.02\n    step3:\n      success: 0.1875\n      pass_at_8: 0.625\n      invalid_action: 0.028\n    step4:\n      success: 0.0547\n      pass_at_8: 0.25\n      invalid_action: 0.264\n    step5:\n      success: 0.0156\n      pass_at_8: 0.0625\n      invalid_action: 0.369\n    step6:\n      success: 0.0313\n      pass_at_8: 0.25\n      invalid_action: 0.471\n    step7:\n      success: 0.0469\n      pass_at_8: 0.1875\n      invalid_action: 0.502\n    step8:\n      success: 0.0156\n      pass_at_8: 0.125\n      invalid_action: 0.542\n    step9:\n      success: 0\n      pass_at_8: 0\n      invalid_action: 0.641\n    val_step0:\n      success: 0\n      reward_mean: 0\n    val_step5:\n      success: 0.0313\n      invalid_action: 0.781\n    checkpoint: global_step_5\n    gpu_util: 95-96%\n    collapse_onset: step3→step4\n    pid: 920380\n    elapsed_hours: 7.1\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-17T13:43:58.029Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-17T13:43:58.029Z",
  "sessionId": "5dabea73-6dd0-4af0-be38-86df39e878a5"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-17T13:43:58.054Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：Episode-level plateau 未突破或回退，双机制理论被 GAE 结果反驳，contrarian positioning 不成立，需要全新 angle
核心假设：['Episode-level GRPO plateau 在 25-30%，未显著超过当前 step 15 的 28.125%', "h-sweep cliff 不一致：部分 seed 无崩溃（h=5 也能学到 15-20%），削弱 'catastrophic failure' narrative", 'Sign misattribution 实证模糊：sign-vs-outcome correlation 0.60-0.80，存在但非主因', 'GAE baseline 大幅优于 episode-level GRPO（>15pp），证明 per-token credit 是关键，episode-level 信息不够', 'Multi-seed std >8pp，部分 seed 成功部分 seed 失败，不 reproducible', 'Selective verification 不可行（base agent 太弱，无法做 cost-efficiency）', 'exp029 的 action_is_valid 持续低（~55%），模型未真正学到有效策略，只是 memorize 少量 pattern']
关键指标范围：{'episode_level_val_success_converged': [0.22, 0.3], 'step_independent_h2_val_success': [0.0, 0.1], 'h_sweep_cliff_threshold': [3, 8], 'sign_vs_outcome_correlation': [0.6, 0.8], 'sign_vs_local_quality_correlation': [0.15, 0.35], 'gamma_k_magnitude_decay_r2': [0.3, 0.6], 'multi_seed_mean_success': [0.2, 0.3], 'multi_seed_std': [0.08, 0.15], 'gae_vs_episode_level_delta_pp': [12, 25], 'selective_verification_rate_reduction': [0.0, 0.15], 'selective_success_delta_vs_always_on_pp': [8, 20], 'scienceworld_episode_vs_step_ratio': [0.8, 1.5]}
叙事方向：原始 framing 的两个支柱均不成立：(1) "episode-level 就够了" 被 GAE 反驳（finer credit 确实必要）， (2) "catastrophic failure" 被不一致的 h-sweep 削弱。需要完全 reframe。 新 angle 选项：(A) "Empirical Taxonomy of Credit Assignment Failure Modes in LLM Agent RL"—— 不再 claim 单一解法，而是系统分类不同 CA 方法（step-independent, episode-level, GAE, turn-level） 在不同条件下的 failure modes，填补 CA Survey (Zhang 2604.09459) 的实验空白。 h-sweep 的不一致性反而变成 contribution（"failure mode 是 context-dependent，非 universal"）。 (B) "When Does Coarse Credit Assignment Suffice? Conditions for Episode-Level RL in Multi-Turn Agents"—— 承认 episode-level 不是 universal solution，但找到它 work 的 sufficient conditions （task length, reward sparsity, action space size），变成 prescriptive guideline paper。 两个 angle 均需额外 2-3 个实验但不降 venue。Selective verification 完全放弃。

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: cost-verify-agent-rl
focus: Post-novelty-check framing with updated competitive positioning: sign misattribution as deeper mechanistic characterization (not just "uniform advantage"), P(correct|update) quantification, dual mechanism separation, contrarian episode-level solution. Evaluate with updated experiment plan including γ-sweep, K-sweep, ScienceWorld transfer. Key question: does the contrarian positioning hold against Turn-PPO/GAGPO/HiPER competitors?

## paper_framing.md

# Paper Framing — Learning When to Verify: RL-Trained Selective Self-Verification for Interactive Agents

> Post-MVP 重写 (2026-05-17) | D054 framing pivot + Dream Review feedback (weak reject → 修正理论)

## Core Insight

Multi-turn interactive agents 的 self-verification 大部分是 confirmatory（不改变行为）而非 corrective。训练 agent 学 selective verification 的前提是 RL 训练本身能 work。我们发现 LLM agent 社区默认的 step-independent training 在长 horizon 任务中灾难性崩溃，根因是**双机制失效**：

1. **Policy Information Loss**: 短窗口（h 步）的 policy 无法学习跨步策略（如 "先探索 drawer 再去 countertop"）
2. **Advantage Sign Misattribution**: step_independent 中，per-window advantage 的**符号**由 episode 成败决定，而非 window-local action quality：
   - 失败 episode 中的好 action → 获得负 advantage（被错误惩罚）
   - 成功 episode 中的差 action → 获得正 advantage（被错误强化）
   - 梯度方向（reinforce/suppress）反映 episode outcome 而非 local decision quality
   - 附加：γ^k magnitude decay 使早期 window 信号更弱（γ^24 ≈ 29%, where 24 = ⌈T/h⌉-1 windows），但方向错误比幅度衰减更致命

Episode-level training 同时解决两者：policy 看全历史（解决 1），整条 trajectory 作为一个 GRPO 样本，所有 tokens 共享同一 advantage — 虽然仍是 episode-level credit（非 per-token），但消除了 window 间的 sign misattribution，因为不再需要将 episode reward 分配到独立优化的子窗口（解决 2）。

**技术澄清**：GRPO 算法本身是 bandit-style（advantage = (R-μ)/σ，无显式 γ），但 RAGEN 的 step_independent 实现在 `compute_step_discounted_returns()` 中引入 γ 计算每个 window 的 return（代码：`agent_trainer.py:271-340`）。γ^(T-t) decay 对 step_independent 模式是代码事实，不是类比。Episode-level 模式下无此问题：整条 trajectory 只有一个 return = episode_reward。

## Story Arc

**Dual contribution**: Training methodology diagnosis + Selective verification system

叙事线：
1. Self-verification 对 interactive agents 有用，但 always-on 成本高
2. 训练 agent 学 WHEN to verify 需要 RL → 但 LLM agent 社区默认的 step-independent training 在多轮任务上灾难性崩溃（0% at step 10）
3. 我们诊断双机制根因（information loss + advantage sign misattribution），提出 episode-level GRPO 解决
4. 分析 "为什么社区默认走向 step-independent"（context window 限制 + token-level training 惯性 + framework design accident）
5. 在 episode-level 基础上，用 action-change 作为 verification informativeness 的 reward，训练 selective policy
6. 结果：near-always-on performance + 显著降低 verification cost

**定位**：不 claim "发明了 episode-level RL"（trivial），而是 "诊断了 LLM agent RL 训练中被忽视的 step-independent 隐性代价 + 系统分析崩溃机制 + 提出实用修复方案 + 在此基础上实现 selective verification"

## Target Venue

待定（NeurIPS 2026 / EMNLP 2026 / ICLR 2026），取决于实验进度和最终效果。

## Core Claims

### Claim 1 (strength: strong): Step-independent GRPO catastrophically fails for multi-turn agents due to dual mechanism
- 所需证据：episode-level vs step-independent 对比（多 seed），h-sweep ablation（3 seeds each），mechanistic analysis（gradient signal measurement），GAE baseline comparison
- 当前证据状态：**ESTABLISHED** (exp029 step5 val=25% vs exp028c step10 val=0%)
- 机制：(1) policy information loss (h-step context insufficient), (2) advantage sign misattribution (gradient direction reflects episode outcome, not window-local action quality; additionally γ^k magnitude decay for early windows)
- 技术细节：GRPO 算法无固有 γ，但 RAGEN step_independent 的 `compute_step_discounted_returns()` 引入 γ-discounted per-window returns → advantage 符号由 episode 成败决定。代码验证：`agent_trainer.py:271-340` + `core_algos.py:194-246`

### Claim 2 (strength: moderate): Action-change is an effective intrinsic reward for verification informativeness
- 所需证据：selective verification 训练收敛 + action-change vs random/confidence baselines
- 当前证据状态：**not yet established**，依赖 Phase B 实验
- 前提：episode-level 训练的 agent 需达到 ≥40% success 才有意义

### Claim 3 (strength: moderate): Learned selective policy matches always-on performance at reduced verification cost
- 所需证据：B-IAVR verification ↓40%+ 且 success delta < 3pp vs always-on
- 当前证据状态：**not yet established**，依赖 Phase B + C
- 前提：Claim 1 的 agent 需足够强

## Contingency Plan

如果 episode-level 训练收敛后 success 仍 < 40%（不足以支撑 cost-efficiency story）：
- **Plan A**：paper 变为 diagnostic + analysis contribution — "Why Step-Independent RL Fails for LLM Multi-Turn Agents: Dual Mechanism Analysis" (需更深 ablation + GAE comparison + community practice survey)
- **Plan B**：加 Self-Guide reward 到 episode-level（从 binary→dense reward），推高 performance 后再做 selective verification
- 不考虑 downgrade venue
- **注意**：Dream review 已证明 Plan A 纯 methodology paper 需要比预期更深的分析才能通过审稿（"诊断社区默认实践的隐性代价" > "episode-level RL works"）

## Reviewer Attack Surface + Defense

| # | Concern | Severity | Defense |
|---|---------|----------|---------|
| 1 | "Episode-level RL is obvious / well-known" | HIGH | h-sweep (3 seeds) 展示 non-trivial cliff + 双机制理论 + "为什么社区默认 step-independent" 分析 |
| 2 | "Theory 与 GRPO 不匹配" | HIGH | 精确区分：GRPO 算法无 γ，但 step_independent 实现引入 γ-discounted returns（代码引用）→ per-window advantage logging 实证 + 伪代码 |
| 3 | "缺 GAE/标准 RL baselines" | HIGH | 加 GAE(λ=0.95) + GAE(λ=1,γ=1) baseline，证明 episode-level GRPO 与 GAE 的差异 |
| 4 | "Self-Guide 3x performance gap" | HIGH | 正面回应：不同 paradigm (expert-guided vs from-scratch RL)，不同问题（Self-Guide 回避了训练问题） |
| 5 | Single environment (ALFWorld) | MEDIUM | ScienceWorld transfer (if resources permit) |
| 6 | Small model (1.7B) | MEDIUM | 定位 resource-constrained; 7B 验证 (conditional) |
| 7 | Action-change = noise vs signal | MEDIUM | Entropy-controlled analysis + causal intervention (Phase B) |
| 8 | 与 ARES 差异化不足 | LOW | Head-to-head 对比 + 方法论差异表 |
| 9 | "Turn-PPO 已解决相同问题" | HIGH | 精确区分：Turn-PPO 发现 uniform advantage (subset)，我们发现 sign misattribution (superset + 量化 γ^24≈29%)；解法相反 (finer vs coarser) |

## Evidence Status Matrix

| Claim | MVP Evidence | Research Evidence Needed | Priority |
|-------|-------------|--------------------------|----------|
| Claim 1 | exp029 vs exp028c (25% vs 0%) | h-value ablation, multi-seed, mechanism paper figure | P0 |
| Claim 2 | N/A | Phase B full implementation | P1 |
| Claim 3 | N/A | Phase B + C comparison suite | P1 |

## Competitive Positioning

| System | Method | Benchmark | Key Difference from Us |
|--------|--------|-----------|----------------------|
| Self-Guide (2026) | Always-on verification | ALFWorld 72.7% (1.7B) | We add selectivity via RL |
| ARES (2603.07915) | SFT router, continuous effort | 52.7% token reduction | SFT vs RL, continuous vs binary |
| Thinkless (NeurIPS'25) | RL control token | reasoning domain | Same RL philosophy, different domain |
| ReflAct (EMNLP'25) | Prompting GPT-4 | ALFWorld 93.3% | Different scale/approach |
| RAGEN (2025) | GRPO for agents | varies | Step-independent default, our baseline |
| **Turn-PPO (2512.17008)** | Turn-level MDP + value fn | reasoning tasks | "Uniform advantage" vs our "sign misattribution"; finer credit vs coarser |
| **GAGPO (2605.13217)** | Grouped value proxy, step-aligned | ALFWorld 93.5% (1.5B) | Finer-grained credit for performance; we diagnose mechanism failure |
| **MT-GRPO (2505.11821)** | Turn-level reward design | QA search tasks | Turn-level credit; we show coarser suffices |
| **iStar (ICLR'26)** | Implicit PRM + dual advantage | WebShop 86.5% | Learns step rewards; we show episode-level eliminates misattribution |
| **ArCHer (ICML'24)** | Hierarchical multi-turn RL | multi-turn agents | Foundational framework; establishes need for hierarchical structure |
| **HiPER (2602.16165)** | Hierarchical Plan-Execute RL | ALFWorld 97.4% (7B) | SOTA performance pursuit; we do mechanism diagnosis |

### Positioning Strategy

**核心差异化：Contrarian Solution。** 竞品（Turn-PPO, GAGPO, MT-GRPO, iStar, HiPER）一致认为 multi-turn RL 需要更细粒度的 credit assignment（turn-level, step-level, hierarchical），并用此提升性能。我们的贡献是诊断性的：

1. **问题定义更精确**：Turn-PPO 发现 "uniform advantage" 问题（所有 turn 获得相同 advantage），我们发现更本质的 "Advantage Sign Misattribution"（advantage 符号由 episode outcome 决定而非 local action quality），并量化 γ^24 ≈ 29% 的 return 衰减。Sign misattribution 是 uniform advantage 的超集。

2. **Contrarian solution**：所有竞品的解法都是引入更细的 credit（turn-level value, step-level PRM, hierarchical planner）。我们展示更粗的 episode-level credit 反而消除 sign misattribution，因为它避免了将 episode reward 错误分配到独立优化的子窗口。这挑战了 "越细越好" 的社区默认假设。

3. **不同 contribution 维度**：GAGPO/HiPER 追求 ALFWorld 93-97% 的 SOTA performance（通过更好的 credit + 更复杂的架构）。我们不 compete on performance axis，而是回答 "为什么社区默认的 step-independent 灾难性失败" 这个诊断问题。两个 contribution 维度正交互补。

4. **与 CA Survey 的关系**：Zhang (2604.09459) 系统化了 47 种 CA 方法，但未分析 CA 方法本身的 failure modes（何时更细粒度反而有害）。我们填补这一空白。

## Research Phases

1. **Phase A (DONE)**: Episode-level GRPO training — MVP passed, demonstrates Claim 1
2. **Phase A+**: Continue training to convergence (target ≥40% success), deploy tatsu parallel patch, multi-seed
3. **Phase B**: Implement selective verification with action-change reward — Claim 2 & 3
4. **Phase C**: Ablation suite — context window sweep, reward ablations, baseline comparisons
5. **Phase D**: (Conditional on resources) Multi-env / multi-model scaling


## experiment_plan (with registry status)

- id: plan_001
  title: Episode-level GRPO convergence (exp029 continuation)
  claim: Claim 1
  phase: A+
  priority: P0
  depends_on: []
  registry_id: exp029_episode_level
  status: DONE
  description: 'Episode-level GRPO (context_window_mode: full) on Qwen3-1.7B + ALFWorld.
    50 steps, dual-GPU. MVP passed at step 5 (val=25%, 2x baseline 12.5%). Continue
    to convergence (step 20+) with tatsu parallel patch for 4x val speedup.

    '
  hypothesis: 'Episode-level training enables stable RL for multi-turn agents, reaching
    ≥40% success by convergence.

    '
  metrics:
    current_step: 15
    total_steps: 100
    progress_pct: 15
    step5_val_success: 0.25
    step10_val_success: 0.25
    step15_val_success: 0.28125
    step15_val_pass_at_1: 0.28125
    step15_val_pass_at_2: 0.469
    step15_val_pass_at_4: 0.726
    step15_val_pass_at_8: 0.929
    step15_val_pass_at_16: 0.996
    step15_val_action_is_valid: 0.5452
    step15_val_action_is_effective: 0.7672
    step15_val_manager_invalid_action: 0.2328
    step15_train_success: 0.4375
    step15_train_pass_at_8: 0.75
    elapsed_hours: 7.35
    eta_completion: '2026-05-19T03:00:00Z'
  gpu_hours_estimate: 48
  framing_ref: claim_1
  conclusion: success
- id: plan_002
  title: Context window h-sweep ablation (3 seeds each)
  claim: Claim 1
  phase: A+
  priority: P0
  depends_on:
  - plan_001
  registry_id: null
  status: planned
  description: 'Sweep context_window h={2, 5, 10, 20, full} on same GRPO config. Config:
    context_window_mode=step_independent + step_independent_history_length={h} (h=full
    uses context_window_mode=full). 15 steps per run, 3 seeds each. KEY paper figure:
    shows credit assignment cliff is robust across seeds. Addresses Reviewer Concern
    #1 + Dream C3 (statistical power).

    '
  hypothesis: 'Performance degrades monotonically with smaller h, with sharp cliff
    below h=10. Cliff is robust across seeds (not single-run artifact).

    '
  metrics:
  - success_rate_per_h
  - convergence_speed
  - collapse_rate
  gpu_hours_estimate: 90
  notes: 5 h-values × 15 steps × 3 seeds. h=2 已有 exp028c 作 1 seed。
- id: plan_003
  title: Multi-seed replication (5 seeds total)
  claim: Claim 1
  phase: A+
  priority: P0
  depends_on:
  - plan_001
  registry_id: null
  status: planned
  description: '4 additional seeds for exp029 episode-level config (5 total incl original).
    Report mean ± std. Dream C3 要求 5-8 seeds for credible CI.

    '
  hypothesis: 'Episode-level success rate is reproducible (std < 5pp across 5 seeds).

    '
  metrics:
  - success_rate_mean
  - success_rate_std
  gpu_hours_estimate: 192
- id: plan_003b
  title: GAE baseline comparison
  claim: Claim 1
  phase: A+
  priority: P0
  depends_on:
  - plan_001
  registry_id: null
  status: planned
  description: 'Dream C4 要求标准 RL baselines。实现 GAE(lambda=0.95, gamma=1.0) 和 GAE(lambda=1.0,
    gamma=1.0) 在 RAGEN 中。需要 value function (critic head)。 15 steps × 3 seeds each。如果
    GAE >> episode-level GRPO → per-token credit assignment 额外有价值。如果持平 → episode-level
    信息是关键。 GRPO episode-level ≠ GAE(1,1)：GRPO 无 critic，所有 token 同一 advantage。

    '
  hypothesis: 'GAE provides modest improvement over episode-level GRPO due to finer
    credit assignment, but both far exceed step-independent.

    '
  metrics:
  - success_rate
  - per_token_advantage_variance
  gpu_hours_estimate: 60
  notes: 需实现 critic head。如果实现成本过高，可用 REINFORCE baseline 替代。
- id: plan_003c
  title: Episode-level + valid_action_bonus (plateau-breaker, D056)
  claim: Claim 1
  phase: A+
  priority: P0
  depends_on:
  - plan_001
  registry_id: null
  status: planned
  description: 'Derived from exp013f negative (D056): dense reward gaming is step_independent-specific.
    Episode-level training prevents per-step reward gaming because model optimizes
    full trajectory total reward. Add valid_action_bonus=0.05 to episode-level config.
    Test if this safely improves action_is_valid (currently 55.9%) without gaming,
    and whether it breaks the 23-25% success plateau. Run during h-sweep batch as
    h=full variant.

    '
  hypothesis: 'Episode-level + small valid_action_bonus safely improves action_is_valid
    (target ≥80%) without reward gaming, and success rate exceeds 30% (breaking exp029
    plateau). Gaming only occurs under step_independent.

    '
  metrics:
  - success_rate
  - action_is_valid
  - valid_bonus_vs_task_reward_ratio
  gpu_hours_estimate: 24
  parent: exp013f
  notes: 'Parent derivation: exp013f gaming → D056 insight → episode-level safety
    hypothesis'
- id: plan_004
  title: Credit assignment mechanism empirical verification (paper Figure 2)
  claim: Claim 1
  phase: A+
  priority: P0
  depends_on:
  - plan_002
  registry_id: null
  status: planned
  description: "Empirically verify \"Advantage Sign Misattribution\" mechanism (D058,\
    \ Reviewer-refined): (a) Per-window advantage logging from h=2 seed 2: record\
    \ (episode_id, window_position,\n    raw_return, advantage_sign, advantage_magnitude,\
    \ episode_outcome, local_action_quality_proxy)\n(b) Key analysis: advantage sign\
    \ vs episode outcome correlation (should be ~1.0),\n    advantage sign vs local\
    \ action quality correlation (should be ~0, proving misattribution)\n(c) Contrast\
    \ success vs failure episodes: success → all positive (including bad windows),\n\
    \    failure → all negative (including good windows)\n(d) γ^k magnitude decay:\
    \ advantage magnitude vs position in success episodes (e) Episode-level control:\
    \ all tokens share one advantage (no position/sign variance) Data source: LOG_PER_SAMPLE_ADV=1\
    \ on h=2 seed 2 (10 lines logging code, zero GPU overhead). Code reference: agent_trainer.py:271-340,\
    \ core_algos.py:194-246.\n"
  hypothesis: 'Per-window advantage in step_independent shows: (1) advantage sign
    is determined by episode success/failure (correlation > 0.95), (2) advantage sign
    is NOT correlated with window-local action quality (r < 0.1), proving sign misattribution,
    (3) magnitude decays as γ^k from terminal position, (4) episode-level shows uniform
    advantage with no sign/magnitude position effects.

    '
  metrics:
  - sign_vs_outcome_correlation
  - sign_vs_local_quality_correlation
  - magnitude_position_decay_r2
  - episode_level_variance
  gpu_hours_estimate: 4
  notes: 'D058+Reviewer: ''sign misattribution'' is the core mechanism (direction
    error > magnitude error). γ^k decay is secondary.'
- id: plan_005
  title: Action-change statistics from always-on runs
  claim: Claim 2
  phase: B
  priority: P1
  depends_on:
  - plan_001
  registry_id: null
  status: planned
  description: 'Collect action-change statistics from exp029 trained checkpoints:
    (1) fraction of verifications triggering action change, (2) correlation between
    action change and episode success, (3) per-task-type breakdown. Informs reward
    design and provides empirical grounding.

    '
  hypothesis: 'Most verifications are confirmatory (>60% no action change). Action
    change positively correlates with episode success (r > 0.2).

    '
  metrics:
  - action_change_rate
  - correlation
  - confirmatory_rate
  gpu_hours_estimate: 4
- id: plan_006
  title: Selective verification implementation
  claim: Claim 2
  phase: B
  priority: P1
  depends_on:
  - plan_005
  registry_id: null
  status: planned
  description: 'Implement binary verify/skip decision in RAGEN framework. Agent outputs
    special token (verify/skip) before each step. Reward = task_success + alpha *
    action_change_when_verified - beta * verification_cost. Code-only, no GPU.

    '
  hypothesis: null
  metrics: []
  gpu_hours_estimate: 0
- id: plan_007
  title: B-IAVR selective verification training
  claim: Claim 2, Claim 3
  phase: B
  priority: P1
  depends_on:
  - plan_006
  - plan_001
  registry_id: null
  status: planned
  description: 'Train selective verification policy via episode-level GRPO. Initialize
    from best exp029 checkpoint. Action-change reward encourages verification only
    when informative.

    '
  hypothesis: 'B-IAVR achieves verification rate ↓40%+ vs always-on while maintaining
    success within 5pp of baseline.

    '
  metrics:
  - success_rate
  - verification_rate
  - cost_reduction
  gpu_hours_estimate: 96
- id: plan_008
  title: Selective verification full comparison
  claim: Claim 3
  phase: B
  priority: P1
  depends_on:
  - plan_007
  registry_id: null
  status: planned
  description: 'Compare on same val set: always-on / B-IAVR / no-verify / random-p
    / confidence-threshold. Report success rate, verification rate, total inference
    tokens, per-task breakdown.

    '
  hypothesis: 'B-IAVR dominates Pareto frontier (best success-to-cost ratio).

    '
  metrics:
  - success_rate
  - verification_rate
  - cost_reduction
  - total_tokens
  gpu_hours_estimate: 8
- id: plan_009
  title: No-verify ablation
  claim: Claim 3
  phase: C
  priority: P1
  depends_on:
  - plan_001
  registry_id: null
  status: planned
  description: 'Episode-level GRPO without any self-verification. Lower bound: demonstrates
    verification value.

    '
  hypothesis: 'Removing verification drops success by ≥10pp vs always-on.

    '
  metrics:
  - success_rate
  - action_is_valid
  gpu_hours_estimate: 48
- id: plan_010
  title: Entropy-controlled action-change analysis
  claim: Claim 2
  phase: C
  priority: P1
  depends_on:
  - plan_005
  registry_id: null
  status: planned
  description: 'Defense for "action change = noise" concern. Stratify by policy entropy;
    test if action-change-success correlation holds within each stratum.

    '
  hypothesis: 'Partial correlation remains significant (p < 0.05) after controlling
    entropy.

    '
  metrics:
  - partial_correlation
  - p_value
  gpu_hours_estimate: 4
- id: plan_011
  title: 'Causal intervention: random vs verification-triggered changes'
  claim: Claim 2
  phase: C
  priority: P1
  depends_on:
  - plan_001
  registry_id: null
  status: planned
  description: 'Inject random action changes at same rate as verification-triggered.
    Compare task success. If verification-triggered >> random, causal evidence.

    '
  hypothesis: 'Verification-triggered changes yield ≥10pp higher success than random.

    '
  metrics:
  - success_rate_triggered
  - success_rate_random
  - delta
  gpu_hours_estimate: 8
- id: plan_012
  title: Reward signal ablation (action-change vs alternatives)
  claim: Claim 2
  phase: C
  priority: P1
  depends_on:
  - plan_007
  registry_id: null
  status: planned
  description: 'Train B-IAVR with alternative rewards: (a) action-change (ours), (b)
    random trigger reward, (c) confidence-based reward. Demonstrates action-change
    is the best signal.

    '
  hypothesis: 'Action-change reward produces best cost-performance tradeoff.

    '
  metrics:
  - success_rate
  - verification_rate
  - cost_reduction
  gpu_hours_estimate: 192
- id: plan_013
  title: ARES reproduction + comparison
  claim: Claim 3
  phase: C
  priority: P1
  depends_on:
  - plan_007
  registry_id: null
  status: planned
  description: 'Reproduce ARES SFT router on ALFWorld (same model). Head-to-head with
    B-IAVR on identical eval episodes. Addresses "ARES differentiation" concern.

    '
  hypothesis: 'B-IAVR achieves ≥10pp better cost reduction than ARES at matched success.

    '
  metrics:
  - success_rate
  - verification_rate
  - cost_reduction
  gpu_hours_estimate: 24
- id: plan_014
  title: ScienceWorld transfer (episode-level advantage)
  claim: Claim 1
  phase: D
  priority: P2
  depends_on:
  - plan_001
  registry_id: null
  status: planned
  description: 'Validate episode-level vs step-independent on ScienceWorld. Different
    env, similar multi-turn structure. Addresses single-env concern.

    '
  hypothesis: 'Episode-level advantage generalizes: ≥2x improvement over step-independent.

    '
  metrics:
  - success_rate_episode
  - success_rate_step_independent
  gpu_hours_estimate: 72
- id: plan_015
  title: 7B model scaling verification
  claim: Claim 1
  phase: D
  priority: P2
  depends_on:
  - plan_002
  registry_id: null
  status: planned
  description: 'Episode-level vs step-independent on Qwen3-7B. Addresses model size
    concern. May need cloud GPU.

    '
  hypothesis: 'Episode-level advantage holds at 7B scale.

    '
  metrics:
  - success_rate_episode_7B
  - success_rate_step_independent_7B
  gpu_hours_estimate: 192
  notes: May require cloud GPU rental (4x A100 or 2x H100)
- id: plan_016
  title: Per-task-type breakdown analysis
  claim: Claim 1
  phase: D
  priority: P2
  depends_on:
  - plan_001
  registry_id: null
  status: planned
  description: 'Breakdown by ALFWorld task type (pick, clean, heat, cool, examine,
    pick_two). Shows within-environment diversity.

    '
  hypothesis: 'Episode-level advantage varies by task complexity; longer tasks benefit
    more.

    '
  metrics:
  - per_task_success
  - episode_length_correlation
  gpu_hours_estimate: 2


## registry (completed experiments)

- exp_id: exp_001
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp_001b
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp_002
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp_003
  name: ''
  status: PREPARING
  conclusion: failed
  metrics: {}
- exp_id: exp_003_dryrun
  name: ''
  status: PREPARING
  conclusion: failed
  metrics: {}
- exp_id: exp_003_dryrun2
  name: ''
  status: PREPARING
  conclusion: failed
  metrics: {}
- exp_id: exp003_dryrun3
  name: ''
  status: PREPARING
  conclusion: failed
  metrics: {}
- exp_id: exp_003_dryrun3
  name: ''
  status: PREPARING
  conclusion: failed
  metrics: {}
- exp_id: exp003
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp005
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: exp007
  name: ''
  status: DONE
  conclusion: failed
  metrics:
    steps_completed: 10
    steps_planned: 30
    crash_reason: 'OSError: No space left on device (/tmp)'
    final_success_rate: 0.0625
    final_action_is_valid: 0.0835
    final_manager_invalid_action: 0.0156
    final_pass_at_8: 0.375
    final_pg_loss: 0.00117
    final_ppo_kl: 0.00127
    final_entropy: 0.057
    final_score_mean: 0.578
    dryrun_action_is_valid: 0.054
    dryrun_invalid_action: 0.065
    training_time_s: 6739
- exp_id: exp007_dryrun
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: exp008
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: exp008_sft
  name: ''
  status: DONE
  conclusion: success
  metrics:
    action_is_valid: 0.9
    format_ok: 1
    success_rate: 0
    final_loss: 0.069
    final_token_accuracy: 0.973
    data_count: 1200
    epochs: 3
    total_steps: 225
    training_time_s: 576
- exp_id: exp009
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp010
  name: ''
  status: DONE
  conclusion: failed
  metrics:
    step: 11
    total_steps: 30
    crash_reason: /tmp disk full (fast_downward libdownward.so)
    initial_val_action_is_valid: 0.652
    initial_val_success: 0
    step1_success: 0.047
    step1_pass_at_8: 0.375
    step1_action_is_valid: 0.588
    step10_success: 0
    step10_pass_at_8: 0
    step10_action_is_valid: 0.683
    step5_ppo_kl: 0.00158
    step5_entropy: 0.1
    trend: action_is_valid improving (58.8%→68.3%) but success collapsing (4.7%→0%)
    checkpoint_saved: global_step_10
- exp_id: exp011
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: exp012
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp012b
  name: ''
  status: DONE
  conclusion: killed
  metrics:
    step: 8
    total_steps: 30
    step6_success: 0.0859
    step6_action_is_valid: 0.613
    step6_pass_at_16: 0.5
    step6_ppo_kl: 0.0039
    step6_entropy: 0.1006
    step6_grad_norm: 1.477
    step7_success: 0
    step7_action_is_valid: 0.685
    step7_pass_at_16: 0
    step7_pg_loss: 0
    step7_ppo_kl: 0.00439
    step7_entropy: 0.0904
    step7_grad_norm: 0.094
    trend: success 8.6%→0% collapse at step 7 (same pattern as exp010, delayed 1 step).
      grad_norm 1.477→0.094, pg_loss→0. Reward fix delayed but did not prevent collapse.
- exp_id: exp013
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: exp013b
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp013c
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: exp013d
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp013e
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp013f
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    step: 30
    total_steps: 30
    completed: true
    exit_code: 0
    training_time_s: 10683
    step6_success: 0.0156
    step7_success: 0.0781
    step10_success: 0
    step17_success: 0.0156
    final_val_success: 0
    final_val_action_is_valid: 0.975
    final_val_action_is_effective: 1
    final_val_reward_mean_at4: 4.388
    final_val_reward_std_at4: 0.195
    final_val_reward_best_at4: 4.499
    final_val_pass_at1: 0
    action_is_valid_trend: 60%→65.9%→77.1%→97.5%
    success_trend: 0%→1.56%→7.81%→0%→1.56%→0%
    grad_norm_range: 1.7-2.9 (no collapse)
    conclusion_reason: 'Dense reward gaming: model optimized valid_action_bonus (action_is_valid
      60%→97.5%) but success stayed 0%. Reward ratio 1:67 too weak — cumulative valid_action_bonus
      (4.5) dominated learning signal vs sparse success_reward (10.0). GRPO collapse
      prevented but task completion not learned.'
- exp_id: exp014c
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: exp014a
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: exp014b
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: exp015
  name: ''
  status: DONE
  conclusion: killed
  metrics:
    step: 1
    total_steps: 30
    val_step0_success: 0
    val_step0_action_is_valid: 0.858
    val_step0_pass_at1: 0
    val_step0_episodic_return: 0
    val_step0_response_length: 2797.5
    val_train_transition: passed
    estimated_total_time_min: 163
    time_per_step_min: 5.6
- exp_id: exp016
  name: ''
  status: DONE
  conclusion: failed
  metrics:
    step: 12
    total_steps: 30
    elapsed_min: 51
    step6_success: 0
    step6_action_is_valid: 0.521
    step6_pg_loss: 0
    step6_grad_norm: 0.841
    step7_success: 0.047
    step7_pass_at16: 0.5
    step7_action_is_valid: 0.655
    step10_success: 0
    step10_action_is_valid: 0.664
    step10_pg_loss: 0
    step10_grad_norm: 0.856
    step10_entropy: 0.1046
    step10_ppo_kl: -9.1e-05
    all_raw_rewards: 0
    all_advantages: 0
    all_returns: 0
    reward_signal: BROKEN — success episodes get reward=0
    action_is_valid_trend: 52.1%→65.5%→66.4%
    manager_invalid_action_trend: 13.5%→11.2%→9.6%
- exp_id: exp017_expert_sft
  name: ''
  status: DONE
  conclusion: success
  metrics:
    final_train_loss: 0.1434
    final_step_loss: 0.04
    final_token_accuracy: 0.983
    epochs: 3
    total_steps: 462
    training_time_min: 26
    data_count_train: 2460
    data_count_val: 129
    checkpoint_size_gb: 3.44
    eval_success_rate: 0.05
    eval_success: 1/20
    eval_action_is_valid: 0.638
    eval_format_ok: 0.75
    eval_avg_steps: 22
    eval_time_s: 149.6
    eval_per_task:
      put: 0/10
      clean: 0/4
      cool: 1/3
      heat: 0/2
      examine: 0/1
    eval_parse_failures: 5/20 episodes (EP 7/12/16/17/18)
- exp_id: exp018_sft_grpo
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: exp019_expert_sft_v2
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: exp019b_expert_sft_v2
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: exp019b_expert_sft_v3
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_loss: 0.0718
    eval_loss: 0.0428
    eval_mean_token_accuracy: 0.9869
    train_runtime_seconds: 2869.8
    steps: 320
    epochs: 2
    eval_success_rate: 0.2
    eval_format_ok: 1
    eval_action_is_valid: 0.8533
    eval_episodes: 20
    eval_avg_steps: 25.4
    eval_time_seconds: 146
- exp_id: exp019c_expert_sft_v3
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: exp020_grpo_from_sft
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp020b_grpo_from_sft
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    steps_completed: 22
    steps_planned: 30
    hung_at_step: 23
    step1_train_success: 0.1875
    step10_train_success: 0.1875
    step20_train_success: 0.125
    step22_train_success: 0.0469
    val_success_step0: 0
    val_success_step20: 0
    entropy_initial: 0.107
    entropy_final: 0.042
    grad_norm_initial: 2.78
    grad_norm_step20: 5.58
    ppo_kl_final: 0.00918
    pass_at_16_step1: 0.75
    pass_at_16_step22: 0.25
    checkpoint_latest: global_step_20
    training_status: hung_at_step23_rollout
- exp_id: exp020c_grpo_from_sft
  name: ''
  status: PREPARING
  conclusion: failed
  metrics: {}
- exp_id: exp020d_grpo_from_sft
  name: ''
  status: PREPARING
  conclusion: failed
  metrics: {}
- exp_id: exp021_sft_ragen_format
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: exp021_ragen_sft_v4
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    train_loss_final: 0.038
    train_token_accuracy: 0.988
    train_steps: 320
    train_epochs: 2
    train_time_min: 47.8
    ragen_val_success: 0.25
    ragen_val_action_is_valid: 0.875
    eval_sft_fast_success: 0
    eval_sft_fast_format_ok: 1
    eval_sft_fast_action_is_valid: 0.71
    checkpoint_size_gb: 3.3
    ragen_val_success_16ep: 0.0625
    ragen_val_action_is_valid_16ep: 0.6875
- exp_id: exp022_grpo_from_sft_v4
  name: ''
  status: DONE
  conclusion: killed
  metrics:
    steps_completed: 1
    steps_planned: 30
    val_step0_success: 0.125
    val_step0_action_is_valid: 0.4875
    val_step0_action_is_effective: 1
    val_step0_reward_mean: 1.25
    val_step0_reward_best: 6.61
    val_step0_episodes: 8
    step_time_seconds: 208
- exp_id: exp023_grpo_parallel
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp023c_grpo_serial
  name: ''
  status: DONE
  conclusion: failed
  metrics:
    val_step0_success: 0.0625
    val_step0_action_is_valid: 0.6875
    val_step0_episodes: 16
    train_step1_success: 0.297
    train_step1_action_is_valid: 0.791
    train_step1_entropy: 0.0652
    train_step1_pass16: 0.75
    train_step1_kl: 0.000156
    train_step8_success: 0.234
    train_step8_action_is_valid: 0.779
    train_step8_entropy: 0.0555
    train_step8_pass16: 0.5
    train_step8_kl: 0.000475
    steps_completed: 8
    steps_planned: 30
    step_time_seconds_start: 240
    step_time_seconds_end: 365
- exp_id: exp024_success_gated_grpo
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: exp025
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp025b
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp025c
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: exp026_step_independent_grpo
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    val_before_train_success: 0.0625
    val_before_train_action_is_valid: 0.631
    val_before_train_episodes: 16
    train_step1_success: 0.2188
    train_step1_action_is_valid: 0.686
    train_step1_entropy: 0.2672
    train_step1_kl_loss: 0.1797
    train_step1_grad_norm: 14.43
    train_step1_reward_mean: 1.218
    train_step1_pass_at_16: 1
    train_step2_success: 0.3281
    train_step2_action_is_valid: 0.603
    train_step2_entropy: 0.317
    train_step2_kl_loss: 0.0974
    train_step2_grad_norm: 15.62
    train_step2_reward_mean: 1.62
    train_step2_pass_at_16: 1
    train_step3_success: 0.1719
    train_step3_action_is_valid: 0.641
    train_step3_entropy: 0.387
    train_step3_kl_loss: 0.2617
    train_step3_grad_norm: 15.65
    train_step3_reward_mean: 1.079
    train_step3_pass_at_16: 0.75
    train_step4_success: 0
    train_step4_action_is_valid: 0.717
    train_step4_entropy: 0.387
    train_step4_kl_loss: 0.054
    train_step4_grad_norm: 13.81
    train_step4_pass_at_16: 0
- exp_id: exp027_stable_grpo
  name: ''
  status: DONE
  conclusion: failed
  metrics:
    step_0_val_before_train:
      success: 6.25
      action_is_valid: 63.125
      action_is_effective: 87.875
      num_actions: 42.375
      response_length: 114.67
      reward_mean: 0.3226
      val_generation_time_s: 502.57
    step_1_train:
      success: 35.94
      kl_loss: 0.058
      batch_size: 5152
      training_time_s: 4342
    step_2_train:
      success: 10.16
      kl_loss: 0.413
      batch_size: 6144
      training_time_s: 5886
    step_3_train:
      success: 10.16
      kl_loss: 0.248
      entropy: 0.385
      pass_at_16: 0.5
      grad_norm: 21.31
      reward_mean: 0.483
      batch_size: 6048
      training_time_s: 4689
    step_4_train:
      success: 13.28
      pass_at_16: 0.375
      note: 'Director判定: 趋势确认, MVP未通过'
- exp_id: exp028_prereq_zeroshot_instruct
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: exp028a_recipe_fix
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: exp028_prereq_zeroshot
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    success: 0
    action_is_valid: 0.75
    num_actions: 50
    pass_at_1: 0
    response_length: 75.07
- exp_id: exp028c_selfguide_recipe
  name: ''
  status: DONE
  conclusion: failed
  metrics:
    step_0_val:
      success: 6.25
      pass_at_1: 6.25
      action_is_valid: 74.5
      score_mean: 0.119
    step_1_train:
      success: 13.28
      pass_at_8: 37.5
      action_is_valid: 76.4
      action_is_effective: 96.37
      entropy: 0.2634
      kl_loss: 0.0128
      ppo_kl: 0.019
      grad_norm: 16.88
      score_mean: 0.843
      time_s: 3252
      note: 三方交叉验证通过
    step_2_train:
      success: 6.25
      pass_at_8: 25
      action_is_valid: 83.2
      entropy: 0.247
      kl_loss: 0.1706
      pg_loss: 0.007
      grad_norm: 17.3
      score_mean: 0.274
      time_s: 3120
    step_3_train:
      success: 15.63
      pass_at_8: 68.75
      action_is_valid: 85.9
      entropy: 0.2488
      kl_loss: 0.1118
      grad_norm: 12.57
      score_mean: 0.661
      time_s: 2760
    step_4_train:
      success: 18.75
      pass_at_8: 62.5
      action_is_valid: 87.94
      entropy: 0.234
      kl_loss: 0.031
      ppo_kl: 0.015
    step_5_train:
      success: 9.4
      pass_at_8: 37.5
      action_is_valid: 89.6
      entropy: 0.236
      kl_loss: 0.824
      grad_norm: 13.1
    step_5_val:
      success: 6.25
      pass_at_1: 6.25
      action_is_valid: 96.5
      action_is_effective: 100
      num_actions: 49.4
      score_mean: 0.518
    step_6_train:
      success: 10.94
      action_is_valid: 90.4
      entropy: 0.234
      kl_loss: 0.098
      grad_norm: 12.54
    step_7_train:
      success: 21.88
      pass_at_8: 56.25
      action_is_valid: 91.8
      entropy: 0.224
      kl_loss: 0.046
    step_8_train:
      success: 15.6
      pass_at_8: 50
      action_is_valid: 92.7
      kl_loss: 0.039
      entropy: 0.204
    step_9_train:
      success: 18
      pass_at_8: 56.3
      action_is_valid: 93.6
      kl_loss: 0.047
      entropy: 0.204
    step_10_train:
      success: 18.75
      action_is_valid: 90.7
      kl_loss: 0.197
    step_10_val:
      success: 0
      pass_at_1: 0
      best_at_128: 0
      best_at_800: 0
      action_is_valid: 93.6
      num_actions: 49.8
      reward_mean: 0
      note: 灾难性崩溃，模型完全遗忘
- exp_id: exp029_episode_level
  name: ''
  status: DONE
  conclusion: success
  metrics:
    current_step: 15
    total_steps: 100
    progress_pct: 15
    step5_val_success: 0.25
    step10_val_success: 0.25
    step15_val_success: 0.28125
    step15_val_pass_at_1: 0.28125
    step15_val_pass_at_2: 0.469
    step15_val_pass_at_4: 0.726
    step15_val_pass_at_8: 0.929
    step15_val_pass_at_16: 0.996
    step15_val_action_is_valid: 0.5452
    step15_val_action_is_effective: 0.7672
    step15_val_manager_invalid_action: 0.2328
    step15_train_success: 0.4375
    step15_train_pass_at_8: 0.75
    elapsed_hours: 7.35
    eta_completion: '2026-05-19T03:00:00Z'
- exp_id: hsweep_h2_seed1
  name: ''
  status: RUNNING
  conclusion: ''
  metrics:
    train_step: 9
    total_steps: 15
    wandb_run_id: 7o9bjszm
    step1:
      success: 0.1875
      pass_at_8: 0.4375
      invalid_action: 0.027
    step2:
      success: 0.1484
      pass_at_8: 0.5
      invalid_action: 0.02
    step3:
      success: 0.1875
      pass_at_8: 0.625
      invalid_action: 0.028
    step4:
      success: 0.0547
      pass_at_8: 0.25
      invalid_action: 0.264
    step5:
      success: 0.0156
      pass_at_8: 0.0625
      invalid_action: 0.369
    step6:
      success: 0.0313
      pass_at_8: 0.25
      invalid_action: 0.471
    step7:
      success: 0.0469
      pass_at_8: 0.1875
      invalid_action: 0.502
    step8:
      success: 0.0156
      pass_at_8: 0.125
      invalid_action: 0.542
    step9:
      success: 0
      pass_at_8: 0
      invalid_action: 0.641
    val_step0:
      success: 0
      reward_mean: 0
    val_step5:
      success: 0.0313
      invalid_action: 0.781
    checkpoint: global_step_5
    gpu_util: 95-96%
    collapse_onset: step3→step4
    pid: 920380
    elapsed_hours: 7.1

# 输出格式（YAML，仅输出一个 ```yaml 块）

```yaml
tier: worst
narrative_guidance: "..."
imagined_experiments:
  - name: "..."
    plan_id: "..."
    description: "..."
    expected_results: {metric: value, ...}
    result_rationale: "..."
    tables: []
    figures_description: []
    analysis: "..."
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "a7e5f957-fcc1-419b-af4b-a120df19be49",
  "type": "user",
  "uuid": "715cd111-176d-439a-8f0a-6d361cced4ca",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1",
  "sessionId": "5dabea73-6dd0-4af0-be38-86df39e878a5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-17T13:43:58.052Z_

```json
{
  "parentUuid": "715cd111-176d-439a-8f0a-6d361cced4ca",
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
  "uuid": "e8dd0128-8db6-40f7-9939-2116f89fc4c0",
  "timestamp": "2026-05-17T13:43:58.052Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1",
  "sessionId": "5dabea73-6dd0-4af0-be38-86df39e878a5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-17T13:43:58.052Z_

```json
{
  "parentUuid": "e8dd0128-8db6-40f7-9939-2116f89fc4c0",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "e8b56332-35ef-42fe-966a-f9cb207151ab",
  "timestamp": "2026-05-17T13:43:58.052Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1",
  "sessionId": "5dabea73-6dd0-4af0-be38-86df39e878a5",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Episode-level plateau 未突破或回退，双机制理论被 GAE 结果反驳，contrarian positioning 不成立，需要全新 angle 核心假设：['Episode-level GRPO plateau 在 25-30%，未显著超过当前 step 15 的 28.125%',…",
  "leafUuid": "e8b56332-35ef-42fe-966a-f9cb207151ab",
  "sessionId": "5dabea73-6dd0-4af0-be38-86df39e878a5"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Empirical taxonomy of credit assignment failure modes in LLM agent RL",
  "sessionId": "5dabea73-6dd0-4af0-be38-86df39e878a5"
}
```

---

### Assistant

_source line 8 · 2026-05-17T13:44:16.623Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted results for each planned experiment in the experiment_plan, assuming the "worst" tier scenario. Let me go through each planned experiment and predict what would happen under the worst case scenario.

The worst tier means:
- Episode-level plateau NOT broken (stays at 25-30%, not significantly beyond step 15's 28.125%)
- h-sweep cliff is inconsistent (some seeds don't collapse, h=5 can still learn 15-20%)
- Sign misattribution is empirically ambiguous (correlation 0.60-0.80, exists but not dominant)
- GAE baseline significantly outperforms episode-level GRPO (>15pp), proving per-token credit is key


- Multi-seed results show high variance (>8pp std), making reproducibility difficult
- Selective verification becomes impractical since the base agent lacks sufficient capability
- The action_is_valid metric remains low around 55%, indicating the model hasn't developed genuinely effective strategies

I'm now looking at the expected metric ranges across these worst-case scenarios to establish the bounds for each experiment's predicted outcomes.

The narrative is becoming clearer: both my initial assumptions are breaking down. Episode-level success alone isn't sufficient given the GAE discrepancies, and the inconsistent h-sweep results undermine the catastrophic failure hypothesis. I need to fundamentally reconsider the experimental framework.

Now I'm generating predictions for each planned experiment...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8b56332-35ef-42fe-966a-f9cb207151ab",
  "isSidechain": false,
  "requestId": "req_011Cb8EtykpWtGFMF5pVYJq3",
  "type": "assistant",
  "uuid": "956129a4-04f9-4c0d-8287-94b88aa829b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1",
  "sessionId": "5dabea73-6dd0-4af0-be38-86df39e878a5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FarcaXCuHWXjAxmoMnBP8W",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 21439,
      "cache_read_input_tokens": 11841,
      "output_tokens": 10401,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21439,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 10401,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 21439,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21439
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

_source line 9 · 2026-05-17T13:47:35.198Z_

```yaml
tier: worst
narrative_guidance: "原始 framing 的两个支柱均不成立：(1) 'episode-level 就够了' 被 GAE 大幅超越反驳（finer credit 确实必要），(2) 'catastrophic failure at small h' 被不一致的 h-sweep 削弱（部分 seed h=5 也能学到 15-20%）。Contrarian positioning 崩塌。需要完全 reframe 为 empirical taxonomy 或 sufficient conditions 研究。Selective verification 因 base agent 太弱（<30%）完全不可行。"

imagined_experiments:
  - name: "Context window h-sweep ablation (3 seeds each)"
    plan_id: "plan_002"
    description: "Sweep h={2, 5, 10, 20, full}, 15 steps, 3 seeds each. 测试 credit assignment cliff 是否 robust。"
    expected_results:
      h2_seed1_val_success_step15: 0.0
      h2_seed2_val_success_step15: 0.031
      h2_seed3_val_success_step15: 0.0
      h5_seed1_val_success_step15: 0.156
      h5_seed2_val_success_step15: 0.0
      h5_seed3_val_success_step15: 0.188
      h10_seed1_val_success_step15: 0.094
      h10_seed2_val_success_step15: 0.219
      h10_seed3_val_success_step15: 0.125
      h20_seed1_val_success_step15: 0.188
      h20_seed2_val_success_step15: 0.25
      h20_seed3_val_success_step15: 0.156
      full_seed1_val_success_step15: 0.25
      full_seed2_val_success_step15: 0.281
      full_seed3_val_success_step15: 0.219
      collapse_rate_h2: 0.67
      collapse_rate_h5: 0.33
      collapse_rate_h10: 0.0
      cliff_threshold_range: "3-8 (seed-dependent)"
    result_rationale: "Worst 档下 h-sweep cliff 不一致。h=2 多数 seed 崩溃但非全部（seed2 靠运气学到少量 pattern）。h=5 更关键：seed1/3 没有崩溃且学到 15-19%，只有 seed2 崩溃。这直接削弱 'catastrophic failure below threshold' narrative——cliff 位置是 stochastic 的，不是 deterministic 的。h=10/20/full 之间差异不大（均在 10-25% 区间），说明即使给了足够 context，episode-level 本身也有天花板。Monotonic degradation 假设不成立：h=5 的某些 seed 可以接近 h=full。"
    tables:
      - name: "Table 1: h-sweep results (mean ± std across 3 seeds)"
        columns: ["h", "val_success_mean", "val_success_std", "collapse_rate", "convergence_step"]
        rows:
          - [2, "1.0%", "1.8%", "67%", "3-4"]
          - [5, "11.5%", "10.4%", "33%", "4-6"]
          - [10, "14.6%", "6.3%", "0%", "N/A"]
          - [20, "19.8%", "4.8%", "0%", "N/A"]
          - ["full", "25.0%", "3.1%", "0%", "N/A"]
    figures_description:
      - "Fig: h-value vs val_success with per-seed lines. 无 clean cliff——h=5 区间有巨大 variance band（0-19%），与 h=10 overlap。Error bars 在 h=5 处最宽。"
    analysis: "Cliff 不 robust。h=5 std=10.4pp 意味着 cliff 位置是 random variable 而非 structural property。无法 claim 'h&lt;X catastrophically fails' 因为 X 取决于 seed。这削弱了 paper 的核心 figure 说服力——reviewer 会问 'with more seeds would the cliff disappear entirely?'"

  - name: "Multi-seed replication (5 seeds total)"
    plan_id: "plan_003"
    description: "4 additional seeds for exp029 episode-level config, report mean ± std。"
    expected_results:
      seed1_val_success_step15: 0.281
      seed2_val_success_step15: 0.188
      seed3_val_success_step15: 0.313
      seed4_val_success_step15: 0.156
      seed5_val_success_step15: 0.25
      mean_val_success: 0.238
      std_val_success: 0.062
      max_val_success_any_seed: 0.313
      min_val_success_any_seed: 0.156
      seeds_above_30pct: 1
      seeds_below_20pct: 1
      convergence_step_range: "10-15 (all plateau)"
      step50_mean_val_success: 0.26
      step50_std: 0.071
    result_rationale: "Worst 档要求 multi_seed_std > 8pp。5 seeds 中 std=6.2pp（接近但略低于阈值），但如果看 step 50（训练更久），seed 4 可能进一步恶化（plateau 后缓慢下降到 12-15%），使得 late-stage std 达到 8-10pp。关键问题：seed 4 只有 15.6%，与 step-independent h=10 的 best seed（21.9%）重叠——episode-level 的 advantage over step-independent 在 per-seed 层面不 universal。reproducibility 不够 strong（CI 太宽），reviewer 会 flag 'your method might just be getting lucky on some seeds'。"
    tables:
      - name: "Table 2: Multi-seed episode-level GRPO results"
        columns: ["seed", "step5_val", "step10_val", "step15_val", "step50_val", "plateau_onset"]
        rows:
          - [1, "25.0%", "25.0%", "28.1%", "28.1%", "step 10"]
          - [2, "18.8%", "18.8%", "18.8%", "21.9%", "step 5"]
          - [3, "25.0%", "31.3%", "31.3%", "31.3%", "step 10"]
          - [4, "12.5%", "15.6%", "15.6%", "15.6%", "step 5"]
          - [5, "18.8%", "25.0%", "25.0%", "28.1%", "step 10"]
    figures_description:
      - "Fig: Training curves (5 seeds) with shaded std band. Band 宽度在 step 5 后稳定但 wide（±6pp），所有 seed 在 step 10-15 plateau，无 seed 突破 32%。"
    analysis: "Mean 23.8% ± 6.2pp。95% CI = [11.3%, 36.3%]。这个 CI 与 step-independent h=10 mean（14.6%）有 overlap，削弱 episode-level 的统计 significance。更致命的是 plateau 现象——所有 seed 在 step 10-15 停滞，额外训练 35 步几乎无改善，说明 episode-level GRPO 本身有信息瓶颈（无 per-token credit）。"

  - name: "GAE baseline comparison"
    plan_id: "plan_003b"
    description: "GAE(λ=0.95, γ=1.0) 和 GAE(λ=1.0, γ=1.0) vs episode-level GRPO, 15 steps × 3 seeds。"
    expected_results:
      gae_095_mean_val_success_step15: 0.438
      gae_095_std: 0.047
      gae_100_mean_val_success_step15: 0.375
      gae_100_std: 0.055
      episode_grpo_mean_val_success_step15: 0.238
      gae_095_vs_episode_delta_pp: 20.0
      gae_100_vs_episode_delta_pp: 13.7
      gae_095_action_is_valid: 0.78
      gae_095_convergence_step: 12
      gae_still_improving_at_step15: true
    result_rationale: "Worst 档核心假设：GAE >> episode-level GRPO（delta > 15pp）。GAE(0.95) 有 value function 做 per-token credit assignment，能区分 trajectory 中好/坏 action 并精确更新。Episode-level GRPO 所有 token 共享一个 advantage（相当于 REINFORCE），缺乏 temporal difference 信息。20pp gap 证明 per-token credit 是关键——episode-level 'just knowing the outcome' 不够，你需要知道 which tokens contributed。这直接反驳 paper 的 contrarian claim 'coarser is better'。GAE(1.0,1.0) 稍弱因为 high variance（相当于 Monte Carlo），但仍优于 GRPO 因为 critic 提供 baseline。"
    tables:
      - name: "Table 3: GAE vs Episode-level GRPO"
        columns: ["method", "val_success_mean", "std", "delta_vs_episode_grpo", "action_is_valid", "still_improving"]
        rows:
          - ["Episode GRPO", "23.8%", "6.2pp", "—", "55%", "No (plateau)"]
          - ["GAE(λ=1.0,γ=1.0)", "37.5%", "5.5pp", "+13.7pp", "72%", "Marginal"]
          - ["GAE(λ=0.95,γ=1.0)", "43.8%", "4.7pp", "+20.0pp", "78%", "Yes"]
    figures_description:
      - "Fig: Learning curves — GAE(0.95) clearly dominates from step 5 onward, with episode GRPO plateauing while GAE continues climbing. The gap widens over training."
    analysis: "GAE 大幅超越 episode-level GRPO 证明 per-token temporal difference credit 是关键。Episode-level 的 'advantage sign is correct' 不够——你还需要 magnitude differentiation across tokens。这反驳了 contrarian positioning：社区追求 finer credit 是对的。Episode-level 只是 '方向不错但信息太粗' 的 solution。Paper 的核心 contribution（'coarser suffices'）被实验数据否定。"

  - name: "Episode-level + valid_action_bonus (plateau-breaker)"
    plan_id: "plan_003c"
    description: "Episode-level + valid_action_bonus=0.05, 测试能否打破 plateau 且不 game。"
    expected_results:
      val_success_step15: 0.25
      val_action_is_valid_step15: 0.72
      val_action_is_valid_step30: 0.85
      success_plateau_broken: false
      reward_gaming_detected: false
      valid_bonus_vs_task_ratio: "4.2:10 (per episode)"
      action_is_valid_improvement: "+17pp vs vanilla"
    result_rationale: "Episode-level 下 dense reward gaming 不发生（与 exp013f 对比，D056 insight 正确）。action_is_valid 从 55% 提升到 72-85%，模型确实学到了更多合法 action format。但 success rate 仍 plateau 在 25%——更多 valid actions ≠ 更好的 task strategy。模型能输出合法格式但不知道 WHICH valid action 能推进 task。Valid action bonus 解决的是 syntax 问题而非 semantics 问题。Plateau 未突破因为瓶颈不在 action validity 而在 credit assignment granularity（GAE 结果已证明）。"
    tables: []
    figures_description:
      - "Fig: action_is_valid 稳步上升（55%→85%），success_rate 保持 flat（25%±3pp）。两条线 decouple 证明 valid format ≠ task success。"
    analysis: "D056 insight 部分正确（episode-level 不 game dense reward），但 plateau 不是 action_is_valid 造成的。Base agent 学会了 'speak the right language' 但不知道 'say the right thing'。Plateau 本质是 episode-level credit 太粗——all valid actions 获得相同 reinforcement signal，模型无法区分哪个 valid action 更好。"

  - name: "Credit assignment mechanism empirical verification"
    plan_id: "plan_004"
    description: "Per-window advantage logging 验证 sign misattribution 机制。"
    expected_results:
      sign_vs_outcome_correlation: 0.72
      sign_vs_local_quality_correlation: 0.28
      gamma_k_magnitude_decay_r2: 0.45
      episode_level_advantage_variance: 0.0
      success_episodes_all_positive: 0.85
      failure_episodes_all_negative: 0.78
      mixed_sign_episodes_pct: 0.18
    result_rationale: "Worst 档下 sign misattribution 存在但非 dominant。sign_vs_outcome_correlation=0.72 说明 advantage sign 确实偏向 episode outcome，但 0.72 远非 'near 1.0' 的理论预测。28% 的 local quality correlation 说明 advantage 中有 non-trivial 的 local signal（GRPO 的 group normalization 引入了组内相对排序信息）。18% 的 episodes 出现 mixed signs（部分 window positive 部分 negative in same episode），这不符合 'pure sign misattribution' 理论（理论预测应为 0%）。γ^k decay R²=0.45 说明 magnitude 确实随 position 衰减但 fit 不好（noise 大）。总结：mechanism 存在但不 clean，empirical evidence 是 'moderate support' 而非 'strong confirmation'。"
    tables:
      - name: "Table 4: Advantage sign analysis"
        columns: ["metric", "theoretical_prediction", "observed", "interpretation"]
        rows:
          - ["sign-outcome corr", ">0.95", "0.72", "Exists but not dominant"]
          - ["sign-local_quality corr", "<0.1", "0.28", "Non-trivial local signal present"]
          - ["γ^k decay R²", ">0.8", "0.45", "Weak fit"]
          - ["mixed-sign episodes", "0%", "18%", "Theory violation"]
          - ["episode-level variance", "0", "0", "Confirmed (trivially)"]
    figures_description:
      - "Fig 2 draft: scatter plot of per-window advantage sign vs episode outcome. 明显 trend 但大量 noise。不像理论预测的 clean two-cluster separation。"
    analysis: "Sign misattribution 是 real phenomenon 但 paper 需要大幅 soften claims。不能写 'advantage sign is entirely determined by episode outcome'——实际只有 72% correlation。Mixed-sign episodes 的存在说明 GRPO group normalization 引入了组内 local ranking 信号（当 group 中有 partial success 时）。Reviewer 会 attack：'your mechanism is one factor among several, not THE explanation'。这把论文从 'mechanistic explanation paper' 降级为 'we observed a contributing factor'。"

  - name: "Action-change statistics from always-on runs"
    plan_id: "plan_005"
    description: "从 exp029 checkpoints 收集 verification 后 action change 统计。"
    expected_results:
      action_change_rate: 0.35
      confirmatory_rate: 0.65
      action_change_success_correlation: 0.08
      action_change_rate_success_episodes: 0.38
      action_change_rate_failure_episodes: 0.34
      per_task_variance: "high (pick: 0.25, clean: 0.45, heat: 0.30)"
    result_rationale: "Base agent 只有 28% success rate，大部分 verification 是在失败 trajectory 中进行的。Action change rate 35%（不是 >60% confirmatory 的预期？ 其实是——65% confirmatory 符合假设）。但关键问题：action_change_success_correlation 极低（0.08），说明 action change 与 episode success 几乎无关。在成功 episodes 中 change rate=38%，失败中=34%——差异 negligible。这意味着 action-change 作为 reward signal 没有 information content：改变 action 并不 predictive of 成功。原因：base agent 太弱（28% success），它的 verification 大多是 random perturbation 而非 informed correction。"
    tables: []
    figures_description:
      - "Fig: action_change_rate 按 task type 分解。High variance across types 但 none 显示 strong change-success correlation。"
    analysis: "Action-change reward 的前提假设（'change = informative verification'）在这个 agent 能力水平下不成立。28% success 的 agent 做 verification 更像是 random re-sampling 而非 informed decision revision。Selective verification 的整个 Phase B 建立在沙子上——你需要一个足够强的 agent（≥50% success?）才能让 verification 成为 meaningful signal 而非 noise。"

  - name: "Selective verification implementation"
    plan_id: "plan_006"
    description: "实现 binary verify/skip decision。Code-only。"
    expected_results:
      implementation_complete: true
      code_lines_added: 280
      integration_test_pass: true
      gpu_hours: 0
    result_rationale: "纯代码实现，无 ML 依赖。能完成但实际 training（plan_007）会 fail 因为 base agent 太弱。"
    tables: []
    figures_description: []
    analysis: "Implementation 本身 trivial。问题不在代码而在 downstream training signal quality。"

  - name: "B-IAVR selective verification training"
    plan_id: "plan_007"
    description: "从 exp029 best checkpoint 训练 selective verification policy。"
    expected_results:
      verification_rate: 0.88
      success_rate: 0.219
      success_delta_vs_always_on_pp: -6.2
      cost_reduction: 0.12
      training_converged: false
      policy_behavior: "near-always-verify (degenerate)"
    result_rationale: "Base agent 只有 28% success。Selective policy 面临两个问题：(1) action-change reward 无 information content（plan_005 证明 change 与 success 无关），所以 reward signal is noise；(2) skip verification 有 immediate cost（performance drop），而 base agent 已经很弱，任何 skip 都大幅降低本就脆弱的 success rate。Policy 学到 degenerate solution：几乎 always verify（88% rate），偶尔 skip 是 random noise 而非 learned strategy。12% cost reduction 远未达到 40% target。Success 还 drop 了 6pp 因为那 12% skip 确实 hurt。"
    tables:
      - name: "Table 5: B-IAVR training results"
        columns: ["metric", "target", "achieved", "gap"]
        rows:
          - ["verification_rate_reduction", "≥40%", "12%", "-28pp"]
          - ["success_delta_vs_always_on", "<5pp", "-6.2pp", "Fail"]
          - ["cost_reduction_pct", "≥40%", "12%", "-28pp"]
          - ["policy_entropy_final", ">0.3", "0.08", "Collapsed to always-verify"]
    figures_description:
      - "Fig: verification rate 从 100% 缓慢下降到 88% 然后 plateau。Policy entropy → 0 表明 degenerate convergence。"
    analysis: "Selective verification 在 base agent success < 30% 时完全不可行。Policy 无法学到 meaningful skip pattern 因为：(1) reward signal (action-change) 是 noise，(2) skipping has guaranteed downside with no upside at this performance level。整个 Phase B contribution 不成立。"

  - name: "Selective verification full comparison"
    plan_id: "plan_008"
    description: "Always-on / B-IAVR / no-verify / random-p / confidence-threshold 对比。"
    expected_results:
      always_on_success: 0.281
      biavr_success: 0.219
      biavr_verification_rate: 0.88
      no_verify_success: 0.188
      random_p05_success: 0.234
      random_p05_verification_rate: 0.50
      confidence_threshold_success: 0.25
      confidence_threshold_verification_rate: 0.62
    result_rationale: "B-IAVR 不 dominate Pareto frontier。Random-p=0.5 在 success/cost tradeoff 上 comparable to B-IAVR（random: 23.4% success at 50% cost vs B-IAVR: 21.9% at 88% cost）——random 更 cost-efficient。Confidence threshold 也优于 B-IAVR。这证明 learned policy 不优于 naive baselines，因为 base agent 太弱导致所有 verification 策略 degenerate。No-verify 只 drop 9pp（远低于预期的 ≥10pp），说明 verification 本身 value 也有限。"
    tables:
      - name: "Table 6: Verification strategy comparison"
        columns: ["method", "success", "verify_rate", "cost_tokens", "success_per_token"]
        rows:
          - ["always-on", "28.1%", "100%", "1.00x", "0.281"]
          - ["B-IAVR (ours)", "21.9%", "88%", "0.92x", "0.238"]
          - ["random-p=0.5", "23.4%", "50%", "0.67x", "0.349"]
          - ["confidence", "25.0%", "62%", "0.74x", "0.338"]
          - ["no-verify", "18.8%", "0%", "0.45x", "0.418"]
    figures_description:
      - "Fig: Pareto frontier (success vs cost). B-IAVR 位于 frontier 内部（dominated by random-p and confidence）。No-verify 有最好的 tokens-per-success efficiency。"
    analysis: "Paper Claim 3 完全 fail。B-IAVR 被 naive baselines dominate。讽刺的是 no-verify 的 efficiency 最高（per-token success ratio），说明在 28% success 水平下，verification 本身就是 pure overhead——agent 改变 action 不提升 success。"

  - name: "No-verify ablation"
    plan_id: "plan_009"
    description: "Episode-level GRPO without self-verification。"
    expected_results:
      success_rate: 0.188
      action_is_valid: 0.52
      delta_vs_always_on: -9.3
    result_rationale: "No-verify 只 drop ~9pp（28.1% → 18.8%），低于预期的 ≥10pp。原因：在 28% success level，verification 的 marginal value 有限——agent 的 success 主要来自偶然走对 path，verification 只是小幅增加 correction 机会但不 fundamentally 改变 strategy。如果 base agent 更强（如 GAE 的 44%），verification drop 可能更大，但我们无法测试因为 episode-level 训练不出更强的 agent。"
    tables: []
    figures_description: []
    analysis: "Verification value 存在但 modest（9pp）。不足以支撑 'selective verification 是重要 research problem' 的 motivation——reviewer 会说 'if verification only adds 9pp, why not just skip it entirely and save tokens?'"

  - name: "Entropy-controlled action-change analysis"
    plan_id: "plan_010"
    description: "Stratify by policy entropy，测试 action-change-success correlation 是否 holds。"
    expected_results:
      partial_correlation_after_entropy_control: 0.03
      p_value: 0.42
      low_entropy_stratum_correlation: 0.05
      high_entropy_stratum_correlation: 0.11
      entropy_success_correlation: -0.15
    result_rationale: "Controlling for entropy 后 action-change-success correlation 从 0.08 降至 0.03（p=0.42，not significant）。这证明 plan_005 中观察到的微弱 correlation 完全由 entropy confound 解释：高 entropy → 更多 random action change + 更低 success。Action change 本身无 causal relationship with success。Reviewer concern 'action change = noise' 被证实。"
    tables: []
    figures_description:
      - "Fig: partial correlation heatmap across entropy strata. All cells near zero after controlling."
    analysis: "Action-change 作为 verification informativeness proxy 的理论基础被否定。Change 只是 high entropy 的 side effect，不是 'verification found better action'。Claim 2 的 reward design 无 empirical grounding。"

  - name: "Causal intervention: random vs verification-triggered changes"
    plan_id: "plan_011"
    description: "Inject random action changes at same rate，对比 verification-triggered。"
    expected_results:
      success_rate_verification_triggered: 0.22
      success_rate_random_change: 0.19
      delta_pp: 3.0
      p_value: 0.31
      effect_size_cohens_d: 0.12
    result_rationale: "Verification-triggered changes 只比 random changes 好 3pp（not significant, p=0.31）。Effect size tiny (d=0.12)。原因：28% success 的 agent 做 verification 时，其 'correction' 几乎等价于 random re-sampling from policy——agent 没有真正的 'second opinion' 能力，verification output 和 original output 来自同一个 weak policy distribution。Causal evidence for verification value 不成立。"
    tables: []
    figures_description:
      - "Fig: success rate comparison with 95% CI error bars. Bars overlap heavily."
    analysis: "Verification 在 weak agent 上 ≈ random perturbation。这是 Claim 2 的 death blow——不仅 action-change 不是好 reward（plan_010），verification 本身在当前 agent 能力下就没有 causal value（它的 correction 不比 random good）。"

  - name: "Reward signal ablation (action-change vs alternatives)"
    plan_id: "plan_012"
    description: "比较不同 reward signals 训练 selective policy。"
    expected_results:
      action_change_success: 0.219
      action_change_verify_rate: 0.88
      random_trigger_success: 0.234
      random_trigger_verify_rate: 0.52
      confidence_reward_success: 0.25
      confidence_reward_verify_rate: 0.65
    result_rationale: "所有 reward variants 都 fail 达到 target，但 action-change 是最差的——它训出 near-always-verify 因为 reward signal 是 noise（plan_010 已证明）。Random trigger 反而学到 reasonable skip rate 因为 random reward 至少不 mislead（均匀分布）。Confidence 略好因为 confidence 与 success 有 weak correlation。讽刺：learned reward (action-change) 输给了 uninformed baselines。"
    tables:
      - name: "Table 7: Reward signal comparison"
        columns: ["reward_type", "success", "verify_rate", "pareto_dominated"]
        rows:
          - ["action-change (ours)", "21.9%", "88%", "Yes (by all others)"]
          - ["random trigger", "23.4%", "52%", "No"]
          - ["confidence-based", "25.0%", "65%", "No"]
    figures_description: []
    analysis: "Action-change reward 是 worst performer。Claim 2 ('action-change is effective intrinsic reward') 被彻底 falsified。Paper 失去了 selective verification 的 technical contribution。"

  - name: "ARES reproduction + comparison"
    plan_id: "plan_013"
    description: "Reproduce ARES SFT router, head-to-head 对比。"
    expected_results:
      ares_success: 0.25
      ares_verification_rate: 0.55
      ares_cost_reduction: 0.38
      biavr_success: 0.219
      biavr_verification_rate: 0.88
      biavr_cost_reduction: 0.12
      ares_dominates_biavr: true
    result_rationale: "ARES 用 SFT 从 oracle decisions 学 router，不需要 RL reward signal quality。在 same base agent 上 ARES 能学到 55% verification rate 且保持 success（因为它直接学 'when did verification change outcome' from data），而 B-IAVR 依赖 noisy RL reward 学不到 meaningful policy。ARES 在 Pareto frontier 上 dominate B-IAVR。我们不仅没有 '≥10pp better cost reduction'，反而被 dominated。"
    tables: []
    figures_description:
      - "Fig: Pareto frontier with ARES point clearly dominating B-IAVR point."
    analysis: "SFT approach (ARES) 优于 RL approach (B-IAVR) 在这个 setting 下。原因：SFT 有 oracle supervision（从 data 直接学 when to verify），不受 reward noise 影响。RL 需要 good reward signal 但我们没有。Paper 的 'RL > SFT for selective verification' implicit claim 被反驳。"

  - name: "ScienceWorld transfer"
    plan_id: "plan_014"
    description: "Episode-level vs step-independent on ScienceWorld。"
    expected_results:
      episode_level_success: 0.15
      step_independent_success: 0.12
      ratio: 1.25
      episode_level_std: 0.06
      step_independent_std: 0.08
      difference_significant: false
      p_value: 0.38
    result_rationale: "Worst 档下 scienceworld_episode_vs_step_ratio 在 [0.8, 1.5]。Ratio=1.25 意味着 episode-level 只是 marginally better（15% vs 12%，差异 3pp not significant p=0.38）。ScienceWorld 有更短的 episodes（~10-15 steps vs ALFWorld 30-50），所以 step-independent 的 information loss 没那么严重——shorter episodes = fewer windows = less sign misattribution。这反驳了 'episode-level universally superior' claim，支持 'advantage depends on episode length' 的 nuanced view，但也意味着我们的 contribution 是 domain-specific 而非 general。"
    tables:
      - name: "Table 8: ScienceWorld transfer"
        columns: ["method", "success", "std", "avg_episode_length"]
        rows:
          - ["episode-level", "15.0%", "6pp", "12.3 steps"]
          - ["step-independent (h=5)", "12.0%", "8pp", "12.3 steps"]
    figures_description: []
    analysis: "Episode-level advantage 不 generalize to shorter-horizon tasks。ScienceWorld 的短 episode 使 step-independent 的缺陷不 manifest。Reviewer concern #5 (single environment) 被证实——our finding is ALFWorld-specific (long horizon)，不是 general principle。"

  - name: "7B model scaling verification"
    plan_id: "plan_015"
    description: "Qwen3-7B 上验证 episode-level vs step-independent。"
    expected_results:
      episode_level_7b_success: 0.35
      step_independent_7b_success: 0.22
      delta_pp: 13
      relative_improvement: 1.59
      step_independent_collapse: false
      step_independent_7b_h5_success: 0.18
    result_rationale: "7B 模型更强，step-independent 不完全崩溃（22% vs 1.7B 的 0%）。原因：更大模型有更好的 in-context learning，即使 h=5 窗口也能从有限 context 推断 partial strategy。Episode-level 仍优（35% vs 22%）但 gap 缩小（13pp vs 1.7B 的 28pp）。这进一步削弱 'catastrophic failure' narrative——在 stronger model 上 step-independent 只是 suboptimal 而非 catastrophic。Reviewer 会问 'at what model size does the gap disappear entirely?'"
    tables:
      - name: "Table 9: 7B scaling"
        columns: ["method", "1.7B", "7B", "gap_reduction"]
        rows:
          - ["episode-level", "28.1%", "35%", "—"]
          - ["step-independent (h=5)", "0%", "22%", "Gap: 28pp→13pp"]
    figures_description: []
    analysis: "Episode-level advantage diminishes with model scale。7B step-independent 不崩溃（22%），gap 缩小到 13pp。暗示 'catastrophic failure' 是 small model + long horizon 的特定 interaction，更大模型的 in-context learning 能部分补偿 credit assignment 缺陷。Paper 的 alarm ('step-independent catastrophically fails!') 变成了 'step-independent is suboptimal for small models on long tasks'——much weaker claim。"

  - name: "Per-task-type breakdown analysis"
    plan_id: "plan_016"
    description: "按 ALFWorld task type 分解 success。"
    expected_results:
      pick_success: 0.35
      clean_success: 0.25
      heat_success: 0.30
      cool_success: 0.20
      examine_success: 0.15
      pick_two_success: 0.10
      episode_length_correlation: 0.45
      longest_task_success: 0.10
      shortest_task_success: 0.35
    result_rationale: "较短 task（pick: ~15 steps）success 较高（35%），较长 task（pick_two: ~45 steps, examine: ~40 steps）success 最低（10-15%）。Episode length correlation=0.45 (moderate)。这 partially 支持 'longer tasks benefit more from episode-level'，但 correlation 不够 strong——其他 factors（task complexity, number of required objects）也 matter。Not a clean story。"
    tables:
      - name: "Table 10: Per-task breakdown"
        columns: ["task_type", "success", "avg_episode_length", "step_indep_success"]
        rows:
          - ["pick", "35%", "15", "8%"]
          - ["heat", "30%", "22", "3%"]
          - ["clean", "25%", "28", "0%"]
          - ["cool", "20%", "25", "2%"]
          - ["examine", "15%", "38", "0%"]
          - ["pick_two", "10%", "45", "0%"]
    figures_description:
      - "Fig: scatter plot success vs episode_length, with moderate negative trend (r=-0.45)."
    analysis: "Task length 是 contributing factor 但非唯一因素。Paper 可以 claim 'longer tasks benefit more' 但不能 claim 'length is the mechanism'。Adds nuance but not a strong independent contribution。"
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "956129a4-04f9-4c0d-8287-94b88aa829b0",
  "isSidechain": false,
  "requestId": "req_011Cb8EtykpWtGFMF5pVYJq3",
  "type": "assistant",
  "uuid": "e639d6e3-279b-4688-81f0-c9505148b7e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1",
  "sessionId": "5dabea73-6dd0-4af0-be38-86df39e878a5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FarcaXCuHWXjAxmoMnBP8W",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 21439,
      "cache_read_input_tokens": 11841,
      "output_tokens": 10401,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21439,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 10401,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 21439,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21439
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

_source line 10_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Episode-level plateau 未突破或回退，双机制理论被 GAE 结果反驳，contrarian positioning 不成立，需要全新 angle 核心假设：['Episode-level GRPO plateau 在 25-30%，未显著超过当前 step 15 的 28.125%',…",
  "leafUuid": "e639d6e3-279b-4688-81f0-c9505148b7e8",
  "sessionId": "5dabea73-6dd0-4af0-be38-86df39e878a5"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Empirical taxonomy of credit assignment failure modes in LLM agent RL",
  "sessionId": "5dabea73-6dd0-4af0-be38-86df39e878a5"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Episode-level plateau 未突破或回退，双机制理论被 GAE 结果反驳，contrarian positioning 不成立，需要全新 angle 核心假设：['Episode-level GRPO plateau 在 25-30%，未显著超过当前 step 15 的 28.125%',…",
  "leafUuid": "e639d6e3-279b-4688-81f0-c9505148b7e8",
  "sessionId": "5dabea73-6dd0-4af0-be38-86df39e878a5"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Empirical taxonomy of credit assignment failure modes in LLM agent RL",
  "sessionId": "5dabea73-6dd0-4af0-be38-86df39e878a5"
}
```

---
