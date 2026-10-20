# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：Episode-level 训练收敛到强 performance，双机制理论完整验证，selective verification 可行，contrar

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-2/76d61b9e-2e1c-4565-b8a8-d68d26d41235.jsonl`
- **Structured JSON:** [`2e0a9cfce8c24b441c77.json`](../../sessions/2e/2e0a9cfce8c24b441c77.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-17T13:32:52.970Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-17T13:32:52.970Z",
  "sessionId": "76d61b9e-2e1c-4565-b8a8-d68d26d41235",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：Episode-level 训练收敛到强 performance，双机制理论完整验证，selective verification 可行，contrarian positioning 成立\n核心假设：['Episode-level GRPO 收敛至 ≥45% val success（pass@1），打破当前 28% plateau', 'h-sweep 在 3 seeds 上均展示 h<10 的 sharp cliff（无 seed 是 outlier）', 'Sign misattribution 实证：sign-vs-outcome correlation ≥0.95，sign-vs-local-quality correlation <0.1', 'GAE baseline 与 episode-level GRPO 持平或仅略优（delta <5pp），证明 episode-level 信息是关键而非 per-token credit', 'Multi-seed std <5pp（5 seeds），结果 robust', 'Selective verification（B-IAVR）训练收敛，action-change reward 有效', 'ScienceWorld transfer 成功（episode-level ≥2x step-independent）']\n关键指标范围：{'episode_level_val_success_converged': [0.45, 0.6], 'step_independent_h2_val_success': [0.0, 0.05], 'h_sweep_cliff_threshold': [8, 12], 'sign_vs_outcome_correlation': [0.95, 1.0], 'sign_vs_local_quality_correlation': [0.0, 0.1], 'gamma_k_magnitude_decay_r2': [0.85, 0.99], 'multi_seed_mean_success': [0.42, 0.58], 'multi_seed_std': [0.02, 0.05], 'gae_vs_episode_level_delta_pp': [-3, 5], 'selective_verification_rate_reduction': [0.4, 0.65], 'selective_success_delta_vs_always_on_pp': [0, 3], 'scienceworld_episode_vs_step_ratio': [2.0, 4.0]}\n叙事方向：原始 framing 完全成立。Dual contribution paper：(1) 诊断 step-independent 灾难性失败的双机制 （sign misattribution + information loss），实证量化，contrarian solution（更粗的 episode-level 反而优于 finer credit）直接挑战社区 \"越细越好\" 假设；(2) 在此基础上实现 selective verification， B-IAVR 以 40-65% cost reduction 匹配 always-on performance。三个 claims 全部成立， 不需要调整强度。GAE baseline 验证了 episode-level 信息是核心而非 per-token credit。 ScienceWorld transfer 回应 single-env 审稿攻击。可投 NeurIPS/ICLR 主会。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: cost-verify-agent-rl\nfocus: Post-novelty-check framing with updated competitive positioning: sign misattribution as deeper mechanistic characterization (not just \"uniform advantage\"), P(correct|update) quantification, dual mechanism separation, contrarian episode-level solution. Evaluate with updated experiment plan including γ-sweep, K-sweep, ScienceWorld transfer. Key question: does the contrarian positioning hold against Turn-PPO/GAGPO/HiPER competitors?\n\n## paper_framing.md\n\n# Paper Framing — Learning When to Verify: RL-Trained Selective Self-Verification for Interactive Agents\n\n> Post-MVP 重写 (2026-05-17) | D054 framing pivot + Dream Review feedback (weak reject → 修正理论)\n\n## Core Insight\n\nMulti-turn interactive agents 的 self-verification 大部分是 confirmatory（不改变行为）而非 corrective。训练 agent 学 selective verification 的前提是 RL 训练本身能 work。我们发现 LLM agent 社区默认的 step-independent training 在长 horizon 任务中灾难性崩溃，根因是**双机制失效**：\n\n1. **Policy Information Loss**: 短窗口（h 步）的 policy 无法学习跨步策略（如 \"先探索 drawer 再去 countertop\"）\n2. **Advantage Sign Misattribution**: step_independent 中，per-window advantage 的**符号**由 episode 成败决定，而非 window-local action quality：\n   - 失败 episode 中的好 action → 获得负 advantage（被错误惩罚）\n   - 成功 episode 中的差 action → 获得正 advantage（被错误强化）\n   - 梯度方向（reinforce/suppress）反映 episode outcome 而非 local decision quality\n   - 附加：γ^k magnitude decay 使早期 window 信号更弱（γ^24 ≈ 29%, where 24 = ⌈T/h⌉-1 windows），但方向错误比幅度衰减更致命\n\nEpisode-level training 同时解决两者：policy 看全历史（解决 1），整条 trajectory 作为一个 GRPO 样本，所有 tokens 共享同一 advantage — 虽然仍是 episode-level credit（非 per-token），但消除了 window 间的 sign misattribution，因为不再需要将 episode reward 分配到独立优化的子窗口（解决 2）。\n\n**技术澄清**：GRPO 算法本身是 bandit-style（advantage = (R-μ)/σ，无显式 γ），但 RAGEN 的 step_independent 实现在 `compute_step_discounted_returns()` 中引入 γ 计算每个 window 的 return（代码：`agent_trainer.py:271-340`）。γ^(T-t) decay 对 step_independent 模式是代码事实，不是类比。Episode-level 模式下无此问题：整条 trajectory 只有一个 return = episode_reward。\n\n## Story Arc\n\n**Dual contribution**: Training methodology diagnosis + Selective verification system\n\n叙事线：\n1. Self-verification 对 interactive agents 有用，但 always-on 成本高\n2. 训练 agent 学 WHEN to verify 需要 RL → 但 LLM agent 社区默认的 step-independent training 在多轮任务上灾难性崩溃（0% at step 10）\n3. 我们诊断双机制根因（information loss + advantage sign misattribution），提出 episode-level GRPO 解决\n4. 分析 \"为什么社区默认走向 step-independent\"（context window 限制 + token-level training 惯性 + framework design accident）\n5. 在 episode-level 基础上，用 action-change 作为 verification informativeness 的 reward，训练 selective policy\n6. 结果：near-always-on performance + 显著降低 verification cost\n\n**定位**：不 claim \"发明了 episode-level RL\"（trivial），而是 \"诊断了 LLM agent RL 训练中被忽视的 step-independent 隐性代价 + 系统分析崩溃机制 + 提出实用修复方案 + 在此基础上实现 selective verification\"\n\n## Target Venue\n\n待定（NeurIPS 2026 / EMNLP 2026 / ICLR 2026），取决于实验进度和最终效果。\n\n## Core Claims\n\n### Claim 1 (strength: strong): Step-independent GRPO catastrophically fails for multi-turn agents due to dual mechanism\n- 所需证据：episode-level vs step-independent 对比（多 seed），h-sweep ablation（3 seeds each），mechanistic analysis（gradient signal measurement），GAE baseline comparison\n- 当前证据状态：**ESTABLISHED** (exp029 step5 val=25% vs exp028c step10 val=0%)\n- 机制：(1) policy information loss (h-step context insufficient), (2) advantage sign misattribution (gradient direction reflects episode outcome, not window-local action quality; additionally γ^k magnitude decay for early windows)\n- 技术细节：GRPO 算法无固有 γ，但 RAGEN step_independent 的 `compute_step_discounted_returns()` 引入 γ-discounted per-window returns → advantage 符号由 episode 成败决定。代码验证：`agent_trainer.py:271-340` + `core_algos.py:194-246`\n\n### Claim 2 (strength: moderate): Action-change is an effective intrinsic reward for verification informativeness\n- 所需证据：selective verification 训练收敛 + action-change vs random/confidence baselines\n- 当前证据状态：**not yet established**，依赖 Phase B 实验\n- 前提：episode-level 训练的 agent 需达到 ≥40% success 才有意义\n\n### Claim 3 (strength: moderate): Learned selective policy matches always-on performance at reduced verification cost\n- 所需证据：B-IAVR verification ↓40%+ 且 success delta < 3pp vs always-on\n- 当前证据状态：**not yet established**，依赖 Phase B + C\n- 前提：Claim 1 的 agent 需足够强\n\n## Contingency Plan\n\n如果 episode-level 训练收敛后 success 仍 < 40%（不足以支撑 cost-efficiency story）：\n- **Plan A**：paper 变为 diagnostic + analysis contribution — \"Why Step-Independent RL Fails for LLM Multi-Turn Agents: Dual Mechanism Analysis\" (需更深 ablation + GAE comparison + community practice survey)\n- **Plan B**：加 Self-Guide reward 到 episode-level（从 binary→dense reward），推高 performance 后再做 selective verification\n- 不考虑 downgrade venue\n- **注意**：Dream review 已证明 Plan A 纯 methodology paper 需要比预期更深的分析才能通过审稿（\"诊断社区默认实践的隐性代价\" > \"episode-level RL works\"）\n\n## Reviewer Attack Surface + Defense\n\n| # | Concern | Severity | Defense |\n|---|---------|----------|---------|\n| 1 | \"Episode-level RL is obvious / well-known\" | HIGH | h-sweep (3 seeds) 展示 non-trivial cliff + 双机制理论 + \"为什么社区默认 step-independent\" 分析 |\n| 2 | \"Theory 与 GRPO 不匹配\" | HIGH | 精确区分：GRPO 算法无 γ，但 step_independent 实现引入 γ-discounted returns（代码引用）→ per-window advantage logging 实证 + 伪代码 |\n| 3 | \"缺 GAE/标准 RL baselines\" | HIGH | 加 GAE(λ=0.95) + GAE(λ=1,γ=1) baseline，证明 episode-level GRPO 与 GAE 的差异 |\n| 4 | \"Self-Guide 3x performance gap\" | HIGH | 正面回应：不同 paradigm (expert-guided vs from-scratch RL)，不同问题（Self-Guide 回避了训练问题） |\n| 5 | Single environment (ALFWorld) | MEDIUM | ScienceWorld transfer (if resources permit) |\n| 6 | Small model (1.7B) | MEDIUM | 定位 resource-constrained; 7B 验证 (conditional) |\n| 7 | Action-change = noise vs signal | MEDIUM | Entropy-controlled analysis + causal intervention (Phase B) |\n| 8 | 与 ARES 差异化不足 | LOW | Head-to-head 对比 + 方法论差异表 |\n| 9 | \"Turn-PPO 已解决相同问题\" | HIGH | 精确区分：Turn-PPO 发现 uniform advantage (subset)，我们发现 sign misattribution (superset + 量化 γ^24≈29%)；解法相反 (finer vs coarser) |\n\n## Evidence Status Matrix\n\n| Claim | MVP Evidence | Research Evidence Needed | Priority |\n|-------|-------------|--------------------------|----------|\n| Claim 1 | exp029 vs exp028c (25% vs 0%) | h-value ablation, multi-seed, mechanism paper figure | P0 |\n| Claim 2 | N/A | Phase B full implementation | P1 |\n| Claim 3 | N/A | Phase B + C comparison suite | P1 |\n\n## Competitive Positioning\n\n| System | Method | Benchmark | Key Difference from Us |\n|--------|--------|-----------|----------------------|\n| Self-Guide (2026) | Always-on verification | ALFWorld 72.7% (1.7B) | We add selectivity via RL |\n| ARES (2603.07915) | SFT router, continuous effort | 52.7% token reduction | SFT vs RL, continuous vs binary |\n| Thinkless (NeurIPS'25) | RL control token | reasoning domain | Same RL philosophy, different domain |\n| ReflAct (EMNLP'25) | Prompting GPT-4 | ALFWorld 93.3% | Different scale/approach |\n| RAGEN (2025) | GRPO for agents | varies | Step-independent default, our baseline |\n| **Turn-PPO (2512.17008)** | Turn-level MDP + value fn | reasoning tasks | \"Uniform advantage\" vs our \"sign misattribution\"; finer credit vs coarser |\n| **GAGPO (2605.13217)** | Grouped value proxy, step-aligned | ALFWorld 93.5% (1.5B) | Finer-grained credit for performance; we diagnose mechanism failure |\n| **MT-GRPO (2505.11821)** | Turn-level reward design | QA search tasks | Turn-level credit; we show coarser suffices |\n| **iStar (ICLR'26)** | Implicit PRM + dual advantage | WebShop 86.5% | Learns step rewards; we show episode-level eliminates misattribution |\n| **ArCHer (ICML'24)** | Hierarchical multi-turn RL | multi-turn agents | Foundational framework; establishes need for hierarchical structure |\n| **HiPER (2602.16165)** | Hierarchical Plan-Execute RL | ALFWorld 97.4% (7B) | SOTA performance pursuit; we do mechanism diagnosis |\n\n### Positioning Strategy\n\n**核心差异化：Contrarian Solution。** 竞品（Turn-PPO, GAGPO, MT-GRPO, iStar, HiPER）一致认为 multi-turn RL 需要更细粒度的 credit assignment（turn-level, step-level, hierarchical），并用此提升性能。我们的贡献是诊断性的：\n\n1. **问题定义更精确**：Turn-PPO 发现 \"uniform advantage\" 问题（所有 turn 获得相同 advantage），我们发现更本质的 \"Advantage Sign Misattribution\"（advantage 符号由 episode outcome 决定而非 local action quality），并量化 γ^24 ≈ 29% 的 return 衰减。Sign misattribution 是 uniform advantage 的超集。\n\n2. **Contrarian solution**：所有竞品的解法都是引入更细的 credit（turn-level value, step-level PRM, hierarchical planner）。我们展示更粗的 episode-level credit 反而消除 sign misattribution，因为它避免了将 episode reward 错误分配到独立优化的子窗口。这挑战了 \"越细越好\" 的社区默认假设。\n\n3. **不同 contribution 维度**：GAGPO/HiPER 追求 ALFWorld 93-97% 的 SOTA performance（通过更好的 credit + 更复杂的架构）。我们不 compete on performance axis，而是回答 \"为什么社区默认的 step-independent 灾难性失败\" 这个诊断问题。两个 contribution 维度正交互补。\n\n4. **与 CA Survey 的关系**：Zhang (2604.09459) 系统化了 47 种 CA 方法，但未分析 CA 方法本身的 failure modes（何时更细粒度反而有害）。我们填补这一空白。\n\n## Research Phases\n\n1. **Phase A (DONE)**: Episode-level GRPO training — MVP passed, demonstrates Claim 1\n2. **Phase A+**: Continue training to convergence (target ≥40% success), deploy tatsu parallel patch, multi-seed\n3. **Phase B**: Implement selective verification with action-change reward — Claim 2 & 3\n4. **Phase C**: Ablation suite — context window sweep, reward ablations, baseline comparisons\n5. **Phase D**: (Conditional on resources) Multi-env / multi-model scaling\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  title: Episode-level GRPO convergence (exp029 continuation)\n  claim: Claim 1\n  phase: A+\n  priority: P0\n  depends_on: []\n  registry_id: exp029_episode_level\n  status: DONE\n  description: 'Episode-level GRPO (context_window_mode: full) on Qwen3-1.7B + ALFWorld.\n    50 steps, dual-GPU. MVP passed at step 5 (val=25%, 2x baseline 12.5%). Continue\n    to convergence (step 20+) with tatsu parallel patch for 4x val speedup.\n\n    '\n  hypothesis: 'Episode-level training enables stable RL for multi-turn agents, reaching\n    ≥40% success by convergence.\n\n    '\n  metrics:\n    current_step: 15\n    total_steps: 100\n    progress_pct: 15\n    step5_val_success: 0.25\n    step10_val_success: 0.25\n    step15_val_success: 0.28125\n    step15_val_pass_at_1: 0.28125\n    step15_val_pass_at_2: 0.469\n    step15_val_pass_at_4: 0.726\n    step15_val_pass_at_8: 0.929\n    step15_val_pass_at_16: 0.996\n    step15_val_action_is_valid: 0.5452\n    step15_val_action_is_effective: 0.7672\n    step15_val_manager_invalid_action: 0.2328\n    step15_train_success: 0.4375\n    step15_train_pass_at_8: 0.75\n    elapsed_hours: 7.35\n    eta_completion: '2026-05-19T03:00:00Z'\n  gpu_hours_estimate: 48\n  framing_ref: claim_1\n  conclusion: success\n- id: plan_002\n  title: Context window h-sweep ablation (3 seeds each)\n  claim: Claim 1\n  phase: A+\n  priority: P0\n  depends_on:\n  - plan_001\n  registry_id: null\n  status: planned\n  description: 'Sweep context_window h={2, 5, 10, 20, full} on same GRPO config. Config:\n    context_window_mode=step_independent + step_independent_history_length={h} (h=full\n    uses context_window_mode=full). 15 steps per run, 3 seeds each. KEY paper figure:\n    shows credit assignment cliff is robust across seeds. Addresses Reviewer Concern\n    #1 + Dream C3 (statistical power).\n\n    '\n  hypothesis: 'Performance degrades monotonically with smaller h, with sharp cliff\n    below h=10. Cliff is robust across seeds (not single-run artifact).\n\n    '\n  metrics:\n  - success_rate_per_h\n  - convergence_speed\n  - collapse_rate\n  gpu_hours_estimate: 90\n  notes: 5 h-values × 15 steps × 3 seeds. h=2 已有 exp028c 作 1 seed。\n- id: plan_003\n  title: Multi-seed replication (5 seeds total)\n  claim: Claim 1\n  phase: A+\n  priority: P0\n  depends_on:\n  - plan_001\n  registry_id: null\n  status: planned\n  description: '4 additional seeds for exp029 episode-level config (5 total incl original).\n    Report mean ± std. Dream C3 要求 5-8 seeds for credible CI.\n\n    '\n  hypothesis: 'Episode-level success rate is reproducible (std < 5pp across 5 seeds).\n\n    '\n  metrics:\n  - success_rate_mean\n  - success_rate_std\n  gpu_hours_estimate: 192\n- id: plan_003b\n  title: GAE baseline comparison\n  claim: Claim 1\n  phase: A+\n  priority: P0\n  depends_on:\n  - plan_001\n  registry_id: null\n  status: planned\n  description: 'Dream C4 要求标准 RL baselines。实现 GAE(lambda=0.95, gamma=1.0) 和 GAE(lambda=1.0,\n    gamma=1.0) 在 RAGEN 中。需要 value function (critic head)。 15 steps × 3 seeds each。如果\n    GAE >> episode-level GRPO → per-token credit assignment 额外有价值。如果持平 → episode-level\n    信息是关键。 GRPO episode-level ≠ GAE(1,1)：GRPO 无 critic，所有 token 同一 advantage。\n\n    '\n  hypothesis: 'GAE provides modest improvement over episode-level GRPO due to finer\n    credit assignment, but both far exceed step-independent.\n\n    '\n  metrics:\n  - success_rate\n  - per_token_advantage_variance\n  gpu_hours_estimate: 60\n  notes: 需实现 critic head。如果实现成本过高，可用 REINFORCE baseline 替代。\n- id: plan_003c\n  title: Episode-level + valid_action_bonus (plateau-breaker, D056)\n  claim: Claim 1\n  phase: A+\n  priority: P0\n  depends_on:\n  - plan_001\n  registry_id: null\n  status: planned\n  description: 'Derived from exp013f negative (D056): dense reward gaming is step_independent-specific.\n    Episode-level training prevents per-step reward gaming because model optimizes\n    full trajectory total reward. Add valid_action_bonus=0.05 to episode-level config.\n    Test if this safely improves action_is_valid (currently 55.9%) without gaming,\n    and whether it breaks the 23-25% success plateau. Run during h-sweep batch as\n    h=full variant.\n\n    '\n  hypothesis: 'Episode-level + small valid_action_bonus safely improves action_is_valid\n    (target ≥80%) without reward gaming, and success rate exceeds 30% (breaking exp029\n    plateau). Gaming only occurs under step_independent.\n\n    '\n  metrics:\n  - success_rate\n  - action_is_valid\n  - valid_bonus_vs_task_reward_ratio\n  gpu_hours_estimate: 24\n  parent: exp013f\n  notes: 'Parent derivation: exp013f gaming → D056 insight → episode-level safety\n    hypothesis'\n- id: plan_004\n  title: Credit assignment mechanism empirical verification (paper Figure 2)\n  claim: Claim 1\n  phase: A+\n  priority: P0\n  depends_on:\n  - plan_002\n  registry_id: null\n  status: planned\n  description: \"Empirically verify \\\"Advantage Sign Misattribution\\\" mechanism (D058,\\\n    \\ Reviewer-refined): (a) Per-window advantage logging from h=2 seed 2: record\\\n    \\ (episode_id, window_position,\\n    raw_return, advantage_sign, advantage_magnitude,\\\n    \\ episode_outcome, local_action_quality_proxy)\\n(b) Key analysis: advantage sign\\\n    \\ vs episode outcome correlation (should be ~1.0),\\n    advantage sign vs local\\\n    \\ action quality correlation (should be ~0, proving misattribution)\\n(c) Contrast\\\n    \\ success vs failure episodes: success → all positive (including bad windows),\\n\\\n    \\    failure → all negative (including good windows)\\n(d) γ^k magnitude decay:\\\n    \\ advantage magnitude vs position in success episodes (e) Episode-level control:\\\n    \\ all tokens share one advantage (no position/sign variance) Data source: LOG_PER_SAMPLE_ADV=1\\\n    \\ on h=2 seed 2 (10 lines logging code, zero GPU overhead). Code reference: agent_trainer.py:271-340,\\\n    \\ core_algos.py:194-246.\\n\"\n  hypothesis: 'Per-window advantage in step_independent shows: (1) advantage sign\n    is determined by episode success/failure (correlation > 0.95), (2) advantage sign\n    is NOT correlated with window-local action quality (r < 0.1), proving sign misattribution,\n    (3) magnitude decays as γ^k from terminal position, (4) episode-level shows uniform\n    advantage with no sign/magnitude position effects.\n\n    '\n  metrics:\n  - sign_vs_outcome_correlation\n  - sign_vs_local_quality_correlation\n  - magnitude_position_decay_r2\n  - episode_level_variance\n  gpu_hours_estimate: 4\n  notes: 'D058+Reviewer: ''sign misattribution'' is the core mechanism (direction\n    error > magnitude error). γ^k decay is secondary.'\n- id: plan_005\n  title: Action-change statistics from always-on runs\n  claim: Claim 2\n  phase: B\n  priority: P1\n  depends_on:\n  - plan_001\n  registry_id: null\n  status: planned\n  description: 'Collect action-change statistics from exp029 trained checkpoints:\n    (1) fraction of verifications triggering action change, (2) correlation between\n    action change and episode success, (3) per-task-type breakdown. Informs reward\n    design and provides empirical grounding.\n\n    '\n  hypothesis: 'Most verifications are confirmatory (>60% no action change). Action\n    change positively correlates with episode success (r > 0.2).\n\n    '\n  metrics:\n  - action_change_rate\n  - correlation\n  - confirmatory_rate\n  gpu_hours_estimate: 4\n- id: plan_006\n  title: Selective verification implementation\n  claim: Claim 2\n  phase: B\n  priority: P1\n  depends_on:\n  - plan_005\n  registry_id: null\n  status: planned\n  description: 'Implement binary verify/skip decision in RAGEN framework. Agent outputs\n    special token (verify/skip) before each step. Reward = task_success + alpha *\n    action_change_when_verified - beta * verification_cost. Code-only, no GPU.\n\n    '\n  hypothesis: null\n  metrics: []\n  gpu_hours_estimate: 0\n- id: plan_007\n  title: B-IAVR selective verification training\n  claim: Claim 2, Claim 3\n  phase: B\n  priority: P1\n  depends_on:\n  - plan_006\n  - plan_001\n  registry_id: null\n  status: planned\n  description: 'Train selective verification policy via episode-level GRPO. Initialize\n    from best exp029 checkpoint. Action-change reward encourages verification only\n    when informative.\n\n    '\n  hypothesis: 'B-IAVR achieves verification rate ↓40%+ vs always-on while maintaining\n    success within 5pp of baseline.\n\n    '\n  metrics:\n  - success_rate\n  - verification_rate\n  - cost_reduction\n  gpu_hours_estimate: 96\n- id: plan_008\n  title: Selective verification full comparison\n  claim: Claim 3\n  phase: B\n  priority: P1\n  depends_on:\n  - plan_007\n  registry_id: null\n  status: planned\n  description: 'Compare on same val set: always-on / B-IAVR / no-verify / random-p\n    / confidence-threshold. Report success rate, verification rate, total inference\n    tokens, per-task breakdown.\n\n    '\n  hypothesis: 'B-IAVR dominates Pareto frontier (best success-to-cost ratio).\n\n    '\n  metrics:\n  - success_rate\n  - verification_rate\n  - cost_reduction\n  - total_tokens\n  gpu_hours_estimate: 8\n- id: plan_009\n  title: No-verify ablation\n  claim: Claim 3\n  phase: C\n  priority: P1\n  depends_on:\n  - plan_001\n  registry_id: null\n  status: planned\n  description: 'Episode-level GRPO without any self-verification. Lower bound: demonstrates\n    verification value.\n\n    '\n  hypothesis: 'Removing verification drops success by ≥10pp vs always-on.\n\n    '\n  metrics:\n  - success_rate\n  - action_is_valid\n  gpu_hours_estimate: 48\n- id: plan_010\n  title: Entropy-controlled action-change analysis\n  claim: Claim 2\n  phase: C\n  priority: P1\n  depends_on:\n  - plan_005\n  registry_id: null\n  status: planned\n  description: 'Defense for \"action change = noise\" concern. Stratify by policy entropy;\n    test if action-change-success correlation holds within each stratum.\n\n    '\n  hypothesis: 'Partial correlation remains significant (p < 0.05) after controlling\n    entropy.\n\n    '\n  metrics:\n  - partial_correlation\n  - p_value\n  gpu_hours_estimate: 4\n- id: plan_011\n  title: 'Causal intervention: random vs verification-triggered changes'\n  claim: Claim 2\n  phase: C\n  priority: P1\n  depends_on:\n  - plan_001\n  registry_id: null\n  status: planned\n  description: 'Inject random action changes at same rate as verification-triggered.\n    Compare task success. If verification-triggered >> random, causal evidence.\n\n    '\n  hypothesis: 'Verification-triggered changes yield ≥10pp higher success than random.\n\n    '\n  metrics:\n  - success_rate_triggered\n  - success_rate_random\n  - delta\n  gpu_hours_estimate: 8\n- id: plan_012\n  title: Reward signal ablation (action-change vs alternatives)\n  claim: Claim 2\n  phase: C\n  priority: P1\n  depends_on:\n  - plan_007\n  registry_id: null\n  status: planned\n  description: 'Train B-IAVR with alternative rewards: (a) action-change (ours), (b)\n    random trigger reward, (c) confidence-based reward. Demonstrates action-change\n    is the best signal.\n\n    '\n  hypothesis: 'Action-change reward produces best cost-performance tradeoff.\n\n    '\n  metrics:\n  - success_rate\n  - verification_rate\n  - cost_reduction\n  gpu_hours_estimate: 192\n- id: plan_013\n  title: ARES reproduction + comparison\n  claim: Claim 3\n  phase: C\n  priority: P1\n  depends_on:\n  - plan_007\n  registry_id: null\n  status: planned\n  description: 'Reproduce ARES SFT router on ALFWorld (same model). Head-to-head with\n    B-IAVR on identical eval episodes. Addresses \"ARES differentiation\" concern.\n\n    '\n  hypothesis: 'B-IAVR achieves ≥10pp better cost reduction than ARES at matched success.\n\n    '\n  metrics:\n  - success_rate\n  - verification_rate\n  - cost_reduction\n  gpu_hours_estimate: 24\n- id: plan_014\n  title: ScienceWorld transfer (episode-level advantage)\n  claim: Claim 1\n  phase: D\n  priority: P2\n  depends_on:\n  - plan_001\n  registry_id: null\n  status: planned\n  description: 'Validate episode-level vs step-independent on ScienceWorld. Different\n    env, similar multi-turn structure. Addresses single-env concern.\n\n    '\n  hypothesis: 'Episode-level advantage generalizes: ≥2x improvement over step-independent.\n\n    '\n  metrics:\n  - success_rate_episode\n  - success_rate_step_independent\n  gpu_hours_estimate: 72\n- id: plan_015\n  title: 7B model scaling verification\n  claim: Claim 1\n  phase: D\n  priority: P2\n  depends_on:\n  - plan_002\n  registry_id: null\n  status: planned\n  description: 'Episode-level vs step-independent on Qwen3-7B. Addresses model size\n    concern. May need cloud GPU.\n\n    '\n  hypothesis: 'Episode-level advantage holds at 7B scale.\n\n    '\n  metrics:\n  - success_rate_episode_7B\n  - success_rate_step_independent_7B\n  gpu_hours_estimate: 192\n  notes: May require cloud GPU rental (4x A100 or 2x H100)\n- id: plan_016\n  title: Per-task-type breakdown analysis\n  claim: Claim 1\n  phase: D\n  priority: P2\n  depends_on:\n  - plan_001\n  registry_id: null\n  status: planned\n  description: 'Breakdown by ALFWorld task type (pick, clean, heat, cool, examine,\n    pick_two). Shows within-environment diversity.\n\n    '\n  hypothesis: 'Episode-level advantage varies by task complexity; longer tasks benefit\n    more.\n\n    '\n  metrics:\n  - per_task_success\n  - episode_length_correlation\n  gpu_hours_estimate: 2\n\n\n## registry (completed experiments)\n\n- exp_id: exp_001\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001b\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_002\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_003\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_003_dryrun\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_003_dryrun2\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp003_dryrun3\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_003_dryrun3\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp003\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp005\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp007\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    steps_completed: 10\n    steps_planned: 30\n    crash_reason: 'OSError: No space left on device (/tmp)'\n    final_success_rate: 0.0625\n    final_action_is_valid: 0.0835\n    final_manager_invalid_action: 0.0156\n    final_pass_at_8: 0.375\n    final_pg_loss: 0.00117\n    final_ppo_kl: 0.00127\n    final_entropy: 0.057\n    final_score_mean: 0.578\n    dryrun_action_is_valid: 0.054\n    dryrun_invalid_action: 0.065\n    training_time_s: 6739\n- exp_id: exp007_dryrun\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp008\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp008_sft\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    action_is_valid: 0.9\n    format_ok: 1\n    success_rate: 0\n    final_loss: 0.069\n    final_token_accuracy: 0.973\n    data_count: 1200\n    epochs: 3\n    total_steps: 225\n    training_time_s: 576\n- exp_id: exp009\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp010\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    step: 11\n    total_steps: 30\n    crash_reason: /tmp disk full (fast_downward libdownward.so)\n    initial_val_action_is_valid: 0.652\n    initial_val_success: 0\n    step1_success: 0.047\n    step1_pass_at_8: 0.375\n    step1_action_is_valid: 0.588\n    step10_success: 0\n    step10_pass_at_8: 0\n    step10_action_is_valid: 0.683\n    step5_ppo_kl: 0.00158\n    step5_entropy: 0.1\n    trend: action_is_valid improving (58.8%→68.3%) but success collapsing (4.7%→0%)\n    checkpoint_saved: global_step_10\n- exp_id: exp011\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp012\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp012b\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    step: 8\n    total_steps: 30\n    step6_success: 0.0859\n    step6_action_is_valid: 0.613\n    step6_pass_at_16: 0.5\n    step6_ppo_kl: 0.0039\n    step6_entropy: 0.1006\n    step6_grad_norm: 1.477\n    step7_success: 0\n    step7_action_is_valid: 0.685\n    step7_pass_at_16: 0\n    step7_pg_loss: 0\n    step7_ppo_kl: 0.00439\n    step7_entropy: 0.0904\n    step7_grad_norm: 0.094\n    trend: success 8.6%→0% collapse at step 7 (same pattern as exp010, delayed 1 step).\n      grad_norm 1.477→0.094, pg_loss→0. Reward fix delayed but did not prevent collapse.\n- exp_id: exp013\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp013b\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp013c\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp013d\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp013e\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp013f\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    step: 30\n    total_steps: 30\n    completed: true\n    exit_code: 0\n    training_time_s: 10683\n    step6_success: 0.0156\n    step7_success: 0.0781\n    step10_success: 0\n    step17_success: 0.0156\n    final_val_success: 0\n    final_val_action_is_valid: 0.975\n    final_val_action_is_effective: 1\n    final_val_reward_mean_at4: 4.388\n    final_val_reward_std_at4: 0.195\n    final_val_reward_best_at4: 4.499\n    final_val_pass_at1: 0\n    action_is_valid_trend: 60%→65.9%→77.1%→97.5%\n    success_trend: 0%→1.56%→7.81%→0%→1.56%→0%\n    grad_norm_range: 1.7-2.9 (no collapse)\n    conclusion_reason: 'Dense reward gaming: model optimized valid_action_bonus (action_is_valid\n      60%→97.5%) but success stayed 0%. Reward ratio 1:67 too weak — cumulative valid_action_bonus\n      (4.5) dominated learning signal vs sparse success_reward (10.0). GRPO collapse\n      prevented but task completion not learned.'\n- exp_id: exp014c\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp014a\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp014b\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp015\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    step: 1\n    total_steps: 30\n    val_step0_success: 0\n    val_step0_action_is_valid: 0.858\n    val_step0_pass_at1: 0\n    val_step0_episodic_return: 0\n    val_step0_response_length: 2797.5\n    val_train_transition: passed\n    estimated_total_time_min: 163\n    time_per_step_min: 5.6\n- exp_id: exp016\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    step: 12\n    total_steps: 30\n    elapsed_min: 51\n    step6_success: 0\n    step6_action_is_valid: 0.521\n    step6_pg_loss: 0\n    step6_grad_norm: 0.841\n    step7_success: 0.047\n    step7_pass_at16: 0.5\n    step7_action_is_valid: 0.655\n    step10_success: 0\n    step10_action_is_valid: 0.664\n    step10_pg_loss: 0\n    step10_grad_norm: 0.856\n    step10_entropy: 0.1046\n    step10_ppo_kl: -9.1e-05\n    all_raw_rewards: 0\n    all_advantages: 0\n    all_returns: 0\n    reward_signal: BROKEN — success episodes get reward=0\n    action_is_valid_trend: 52.1%→65.5%→66.4%\n    manager_invalid_action_trend: 13.5%→11.2%→9.6%\n- exp_id: exp017_expert_sft\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_train_loss: 0.1434\n    final_step_loss: 0.04\n    final_token_accuracy: 0.983\n    epochs: 3\n    total_steps: 462\n    training_time_min: 26\n    data_count_train: 2460\n    data_count_val: 129\n    checkpoint_size_gb: 3.44\n    eval_success_rate: 0.05\n    eval_success: 1/20\n    eval_action_is_valid: 0.638\n    eval_format_ok: 0.75\n    eval_avg_steps: 22\n    eval_time_s: 149.6\n    eval_per_task:\n      put: 0/10\n      clean: 0/4\n      cool: 1/3\n      heat: 0/2\n      examine: 0/1\n    eval_parse_failures: 5/20 episodes (EP 7/12/16/17/18)\n- exp_id: exp018_sft_grpo\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp019_expert_sft_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp019b_expert_sft_v2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp019b_expert_sft_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.0718\n    eval_loss: 0.0428\n    eval_mean_token_accuracy: 0.9869\n    train_runtime_seconds: 2869.8\n    steps: 320\n    epochs: 2\n    eval_success_rate: 0.2\n    eval_format_ok: 1\n    eval_action_is_valid: 0.8533\n    eval_episodes: 20\n    eval_avg_steps: 25.4\n    eval_time_seconds: 146\n- exp_id: exp019c_expert_sft_v3\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp020_grpo_from_sft\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp020b_grpo_from_sft\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    steps_completed: 22\n    steps_planned: 30\n    hung_at_step: 23\n    step1_train_success: 0.1875\n    step10_train_success: 0.1875\n    step20_train_success: 0.125\n    step22_train_success: 0.0469\n    val_success_step0: 0\n    val_success_step20: 0\n    entropy_initial: 0.107\n    entropy_final: 0.042\n    grad_norm_initial: 2.78\n    grad_norm_step20: 5.58\n    ppo_kl_final: 0.00918\n    pass_at_16_step1: 0.75\n    pass_at_16_step22: 0.25\n    checkpoint_latest: global_step_20\n    training_status: hung_at_step23_rollout\n- exp_id: exp020c_grpo_from_sft\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp020d_grpo_from_sft\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp021_sft_ragen_format\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp021_ragen_sft_v4\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    train_loss_final: 0.038\n    train_token_accuracy: 0.988\n    train_steps: 320\n    train_epochs: 2\n    train_time_min: 47.8\n    ragen_val_success: 0.25\n    ragen_val_action_is_valid: 0.875\n    eval_sft_fast_success: 0\n    eval_sft_fast_format_ok: 1\n    eval_sft_fast_action_is_valid: 0.71\n    checkpoint_size_gb: 3.3\n    ragen_val_success_16ep: 0.0625\n    ragen_val_action_is_valid_16ep: 0.6875\n- exp_id: exp022_grpo_from_sft_v4\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    steps_completed: 1\n    steps_planned: 30\n    val_step0_success: 0.125\n    val_step0_action_is_valid: 0.4875\n    val_step0_action_is_effective: 1\n    val_step0_reward_mean: 1.25\n    val_step0_reward_best: 6.61\n    val_step0_episodes: 8\n    step_time_seconds: 208\n- exp_id: exp023_grpo_parallel\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp023c_grpo_serial\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    val_step0_success: 0.0625\n    val_step0_action_is_valid: 0.6875\n    val_step0_episodes: 16\n    train_step1_success: 0.297\n    train_step1_action_is_valid: 0.791\n    train_step1_entropy: 0.0652\n    train_step1_pass16: 0.75\n    train_step1_kl: 0.000156\n    train_step8_success: 0.234\n    train_step8_action_is_valid: 0.779\n    train_step8_entropy: 0.0555\n    train_step8_pass16: 0.5\n    train_step8_kl: 0.000475\n    steps_completed: 8\n    steps_planned: 30\n    step_time_seconds_start: 240\n    step_time_seconds_end: 365\n- exp_id: exp024_success_gated_grpo\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp025\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp025b\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp025c\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp026_step_independent_grpo\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    val_before_train_success: 0.0625\n    val_before_train_action_is_valid: 0.631\n    val_before_train_episodes: 16\n    train_step1_success: 0.2188\n    train_step1_action_is_valid: 0.686\n    train_step1_entropy: 0.2672\n    train_step1_kl_loss: 0.1797\n    train_step1_grad_norm: 14.43\n    train_step1_reward_mean: 1.218\n    train_step1_pass_at_16: 1\n    train_step2_success: 0.3281\n    train_step2_action_is_valid: 0.603\n    train_step2_entropy: 0.317\n    train_step2_kl_loss: 0.0974\n    train_step2_grad_norm: 15.62\n    train_step2_reward_mean: 1.62\n    train_step2_pass_at_16: 1\n    train_step3_success: 0.1719\n    train_step3_action_is_valid: 0.641\n    train_step3_entropy: 0.387\n    train_step3_kl_loss: 0.2617\n    train_step3_grad_norm: 15.65\n    train_step3_reward_mean: 1.079\n    train_step3_pass_at_16: 0.75\n    train_step4_success: 0\n    train_step4_action_is_valid: 0.717\n    train_step4_entropy: 0.387\n    train_step4_kl_loss: 0.054\n    train_step4_grad_norm: 13.81\n    train_step4_pass_at_16: 0\n- exp_id: exp027_stable_grpo\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    step_0_val_before_train:\n      success: 6.25\n      action_is_valid: 63.125\n      action_is_effective: 87.875\n      num_actions: 42.375\n      response_length: 114.67\n      reward_mean: 0.3226\n      val_generation_time_s: 502.57\n    step_1_train:\n      success: 35.94\n      kl_loss: 0.058\n      batch_size: 5152\n      training_time_s: 4342\n    step_2_train:\n      success: 10.16\n      kl_loss: 0.413\n      batch_size: 6144\n      training_time_s: 5886\n    step_3_train:\n      success: 10.16\n      kl_loss: 0.248\n      entropy: 0.385\n      pass_at_16: 0.5\n      grad_norm: 21.31\n      reward_mean: 0.483\n      batch_size: 6048\n      training_time_s: 4689\n    step_4_train:\n      success: 13.28\n      pass_at_16: 0.375\n      note: 'Director判定: 趋势确认, MVP未通过'\n- exp_id: exp028_prereq_zeroshot_instruct\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp028a_recipe_fix\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp028_prereq_zeroshot\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    success: 0\n    action_is_valid: 0.75\n    num_actions: 50\n    pass_at_1: 0\n    response_length: 75.07\n- exp_id: exp028c_selfguide_recipe\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    step_0_val:\n      success: 6.25\n      pass_at_1: 6.25\n      action_is_valid: 74.5\n      score_mean: 0.119\n    step_1_train:\n      success: 13.28\n      pass_at_8: 37.5\n      action_is_valid: 76.4\n      action_is_effective: 96.37\n      entropy: 0.2634\n      kl_loss: 0.0128\n      ppo_kl: 0.019\n      grad_norm: 16.88\n      score_mean: 0.843\n      time_s: 3252\n      note: 三方交叉验证通过\n    step_2_train:\n      success: 6.25\n      pass_at_8: 25\n      action_is_valid: 83.2\n      entropy: 0.247\n      kl_loss: 0.1706\n      pg_loss: 0.007\n      grad_norm: 17.3\n      score_mean: 0.274\n      time_s: 3120\n    step_3_train:\n      success: 15.63\n      pass_at_8: 68.75\n      action_is_valid: 85.9\n      entropy: 0.2488\n      kl_loss: 0.1118\n      grad_norm: 12.57\n      score_mean: 0.661\n      time_s: 2760\n    step_4_train:\n      success: 18.75\n      pass_at_8: 62.5\n      action_is_valid: 87.94\n      entropy: 0.234\n      kl_loss: 0.031\n      ppo_kl: 0.015\n    step_5_train:\n      success: 9.4\n      pass_at_8: 37.5\n      action_is_valid: 89.6\n      entropy: 0.236\n      kl_loss: 0.824\n      grad_norm: 13.1\n    step_5_val:\n      success: 6.25\n      pass_at_1: 6.25\n      action_is_valid: 96.5\n      action_is_effective: 100\n      num_actions: 49.4\n      score_mean: 0.518\n    step_6_train:\n      success: 10.94\n      action_is_valid: 90.4\n      entropy: 0.234\n      kl_loss: 0.098\n      grad_norm: 12.54\n    step_7_train:\n      success: 21.88\n      pass_at_8: 56.25\n      action_is_valid: 91.8\n      entropy: 0.224\n      kl_loss: 0.046\n    step_8_train:\n      success: 15.6\n      pass_at_8: 50\n      action_is_valid: 92.7\n      kl_loss: 0.039\n      entropy: 0.204\n    step_9_train:\n      success: 18\n      pass_at_8: 56.3\n      action_is_valid: 93.6\n      kl_loss: 0.047\n      entropy: 0.204\n    step_10_train:\n      success: 18.75\n      action_is_valid: 90.7\n      kl_loss: 0.197\n    step_10_val:\n      success: 0\n      pass_at_1: 0\n      best_at_128: 0\n      best_at_800: 0\n      action_is_valid: 93.6\n      num_actions: 49.8\n      reward_mean: 0\n      note: 灾难性崩溃，模型完全遗忘\n- exp_id: exp029_episode_level\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    current_step: 15\n    total_steps: 100\n    progress_pct: 15\n    step5_val_success: 0.25\n    step10_val_success: 0.25\n    step15_val_success: 0.28125\n    step15_val_pass_at_1: 0.28125\n    step15_val_pass_at_2: 0.469\n    step15_val_pass_at_4: 0.726\n    step15_val_pass_at_8: 0.929\n    step15_val_pass_at_16: 0.996\n    step15_val_action_is_valid: 0.5452\n    step15_val_action_is_effective: 0.7672\n    step15_val_manager_invalid_action: 0.2328\n    step15_train_success: 0.4375\n    step15_train_pass_at_8: 0.75\n    elapsed_hours: 7.35\n    eta_completion: '2026-05-19T03:00:00Z'\n- exp_id: hsweep_h2_seed1\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics:\n    train_step: 9\n    total_steps: 15\n    wandb_run_id: 7o9bjszm\n    step1:\n      success: 0.1875\n      pass_at_8: 0.4375\n      invalid_action: 0.027\n    step2:\n      success: 0.1484\n      pass_at_8: 0.5\n      invalid_action: 0.02\n    step3:\n      success: 0.1875\n      pass_at_8: 0.625\n      invalid_action: 0.028\n    step4:\n      success: 0.0547\n      pass_at_8: 0.25\n      invalid_action: 0.264\n    step5:\n      success: 0.0156\n      pass_at_8: 0.0625\n      invalid_action: 0.369\n    step6:\n      success: 0.0313\n      pass_at_8: 0.25\n      invalid_action: 0.471\n    step7:\n      success: 0.0469\n      pass_at_8: 0.1875\n      invalid_action: 0.502\n    step8:\n      success: 0.0156\n      pass_at_8: 0.125\n      invalid_action: 0.542\n    step9:\n      success: 0\n      pass_at_8: 0\n      invalid_action: 0.641\n    val_step0:\n      success: 0\n      reward_mean: 0\n    val_step5:\n      success: 0.0313\n      invalid_action: 0.781\n    checkpoint: global_step_5\n    gpu_util: 95-96%\n    collapse_onset: step3→step4\n    pid: 920380\n    elapsed_hours: 7.1\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-17T13:32:52.975Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-17T13:32:52.975Z",
  "sessionId": "76d61b9e-2e1c-4565-b8a8-d68d26d41235"
}
```

---

## Round 1

23 recorded events

### User

_source line 3 · 2026-05-17T13:32:52.995Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：Episode-level 训练收敛到强 performance，双机制理论完整验证，selective verification 可行，contrarian positioning 成立
核心假设：['Episode-level GRPO 收敛至 ≥45% val success（pass@1），打破当前 28% plateau', 'h-sweep 在 3 seeds 上均展示 h<10 的 sharp cliff（无 seed 是 outlier）', 'Sign misattribution 实证：sign-vs-outcome correlation ≥0.95，sign-vs-local-quality correlation <0.1', 'GAE baseline 与 episode-level GRPO 持平或仅略优（delta <5pp），证明 episode-level 信息是关键而非 per-token credit', 'Multi-seed std <5pp（5 seeds），结果 robust', 'Selective verification（B-IAVR）训练收敛，action-change reward 有效', 'ScienceWorld transfer 成功（episode-level ≥2x step-independent）']
关键指标范围：{'episode_level_val_success_converged': [0.45, 0.6], 'step_independent_h2_val_success': [0.0, 0.05], 'h_sweep_cliff_threshold': [8, 12], 'sign_vs_outcome_correlation': [0.95, 1.0], 'sign_vs_local_quality_correlation': [0.0, 0.1], 'gamma_k_magnitude_decay_r2': [0.85, 0.99], 'multi_seed_mean_success': [0.42, 0.58], 'multi_seed_std': [0.02, 0.05], 'gae_vs_episode_level_delta_pp': [-3, 5], 'selective_verification_rate_reduction': [0.4, 0.65], 'selective_success_delta_vs_always_on_pp': [0, 3], 'scienceworld_episode_vs_step_ratio': [2.0, 4.0]}
叙事方向：原始 framing 完全成立。Dual contribution paper：(1) 诊断 step-independent 灾难性失败的双机制 （sign misattribution + information loss），实证量化，contrarian solution（更粗的 episode-level 反而优于 finer credit）直接挑战社区 "越细越好" 假设；(2) 在此基础上实现 selective verification， B-IAVR 以 40-65% cost reduction 匹配 always-on performance。三个 claims 全部成立， 不需要调整强度。GAE baseline 验证了 episode-level 信息是核心而非 per-token credit。 ScienceWorld transfer 回应 single-env 审稿攻击。可投 NeurIPS/ICLR 主会。


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
tier: best
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
  "promptId": "be49ce8a-0797-4b90-bc7b-9e8303358289",
  "type": "user",
  "uuid": "d636ca72-7841-4b9d-a243-f7811cc07292",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1",
  "sessionId": "76d61b9e-2e1c-4565-b8a8-d68d26d41235",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-17T13:32:52.993Z_

```json
{
  "parentUuid": "d636ca72-7841-4b9d-a243-f7811cc07292",
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
  "uuid": "ff7ab0e4-3019-417c-8db4-18322f794f51",
  "timestamp": "2026-05-17T13:32:52.993Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1",
  "sessionId": "76d61b9e-2e1c-4565-b8a8-d68d26d41235",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-17T13:32:52.993Z_

```json
{
  "parentUuid": "ff7ab0e4-3019-417c-8db4-18322f794f51",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "5f29282c-fbc6-45bb-9f14-3cb927874b59",
  "timestamp": "2026-05-17T13:32:52.993Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1",
  "sessionId": "76d61b9e-2e1c-4565-b8a8-d68d26d41235",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Episode-level 训练收敛到强 performance，双机制理论完整验证，selective verification 可行，contrarian positioning 成立 核心假设：['Episode-level GRPO 收敛至 ≥45% val success（pass@1），打破当前…",
  "leafUuid": "5f29282c-fbc6-45bb-9f14-3cb927874b59",
  "sessionId": "76d61b9e-2e1c-4565-b8a8-d68d26d41235"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Episode-level RL for multi-turn agent training",
  "sessionId": "76d61b9e-2e1c-4565-b8a8-d68d26d41235"
}
```

---

### Assistant

_source line 8 · 2026-05-17T13:32:56.098Z_

I'll generate the detailed best-tier predictions for all planned experiments. Let me first review the experiment plan and current metrics carefully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f29282c-fbc6-45bb-9f14-3cb927874b59",
  "isSidechain": false,
  "requestId": "req_011Cb8E3xPMLaMVd8SdsL7KS",
  "type": "assistant",
  "uuid": "4af68db9-5508-49af-b295-c4f033e9d01d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1",
  "sessionId": "76d61b9e-2e1c-4565-b8a8-d68d26d41235",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QYM1ZeW4qL6u1xwRX4Uvzi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 21276,
      "cache_read_input_tokens": 11841,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21276,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 119,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 21276,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21276
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

_source line 9 · 2026-05-17T13:32:57.459Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01EWg4fhCAwBMRh5zFXDQiaP`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_1/",
  "description": "List project files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4af68db9-5508-49af-b295-c4f033e9d01d",
  "isSidechain": false,
  "requestId": "req_011Cb8E3xPMLaMVd8SdsL7KS",
  "type": "assistant",
  "uuid": "eb75b401-2d11-4402-981d-61a9a2779aa5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1",
  "sessionId": "76d61b9e-2e1c-4565-b8a8-d68d26d41235",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QYM1ZeW4qL6u1xwRX4Uvzi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 21276,
      "cache_read_input_tokens": 11841,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21276,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 119,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 21276,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21276
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

_source line 10 · 2026-05-17T13:32:57.631Z_

<details><summary>↩ Tool result · `toolu_01EWg4fhCAwBMRh5zFXDQiaP`</summary>

```text
AGENTS.md
config
global
idea_generator
projects
skills
state
workspace.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eb75b401-2d11-4402-981d-61a9a2779aa5",
  "isSidechain": false,
  "promptId": "be49ce8a-0797-4b90-bc7b-9e8303358289",
  "type": "user",
  "uuid": "3e154990-eb71-4884-aa86-465379baf47e",
  "toolUseResult": {
    "stdout": "AGENTS.md\nconfig\nglobal\nidea_generator\nprojects\nskills\nstate\nworkspace.yaml",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "eb75b401-2d11-4402-981d-61a9a2779aa5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1",
  "sessionId": "76d61b9e-2e1c-4565-b8a8-d68d26d41235",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T13:33:00.391Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01JuuEuPsL36qgrxBgNNGVaf`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/ 2>/dev/null; ls /home/ubuntu/.agent-ml-research-idea_gen_0509_1/state/ 2>/dev/null",
  "description": "Check project and state directories"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e154990-eb71-4884-aa86-465379baf47e",
  "isSidechain": false,
  "requestId": "req_011Cb8E4J62E6HK2yTwxzek1",
  "type": "assistant",
  "uuid": "08e86ea3-deae-4615-a3e3-782be0374a5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1",
  "sessionId": "76d61b9e-2e1c-4565-b8a8-d68d26d41235",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SX7d5iaapnF1uGEnX7FtAU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 153,
      "cache_read_input_tokens": 33117,
      "output_tokens": 131,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 153,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 131,
          "cache_read_input_tokens": 33117,
          "cache_creation_input_tokens": 153,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 153
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

_source line 12 · 2026-05-17T13:33:00.452Z_

<details><summary>↩ Tool result · `toolu_01JuuEuPsL36qgrxBgNNGVaf`</summary>

```text
__setup__
cost-verify-agent-rl
error_diag_dpo_recovery
pool_state_last.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "08e86ea3-deae-4615-a3e3-782be0374a5f",
  "isSidechain": false,
  "promptId": "be49ce8a-0797-4b90-bc7b-9e8303358289",
  "type": "user",
  "uuid": "6c985869-9085-4b2b-b673-aaaef43234da",
  "toolUseResult": {
    "stdout": "__setup__\ncost-verify-agent-rl\nerror_diag_dpo_recovery\npool_state_last.json",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "08e86ea3-deae-4615-a3e3-782be0374a5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1",
  "sessionId": "76d61b9e-2e1c-4565-b8a8-d68d26d41235",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T13:33:03.236Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01EJyorAv7qzCad4NFdDe1LN`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/",
  "description": "List project directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c985869-9085-4b2b-b673-aaaef43234da",
  "isSidechain": false,
  "requestId": "req_011Cb8E4W9osfLGajsvzTXRs",
  "type": "assistant",
  "uuid": "b679eea4-0d41-400f-b403-52224dadb4ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1",
  "sessionId": "76d61b9e-2e1c-4565-b8a8-d68d26d41235",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XFtNjUb4k98Qd5ebZZgKgb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 173,
      "cache_read_input_tokens": 33270,
      "output_tokens": 102,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 173,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 102,
          "cache_read_input_tokens": 33270,
          "cache_creation_input_tokens": 173,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 173
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

_source line 14 · 2026-05-17T13:33:03.288Z_

<details><summary>↩ Tool result · `toolu_01EJyorAv7qzCad4NFdDe1LN`</summary>

```text
AGENTS.md
RAGEN
ROADMAP.lock
ROADMAP.md
artifacts
checkpoints
constraints.lock
constraints.yaml
decisions.lock
decisions.yaml
docs
dream_registry.lock
dream_registry.yaml
dream_registry.yaml.bak
dream_registry.yaml.bak.130710
experiment_plan.yaml
literature_map.yaml
logs
memory.md
paper_framing.md
paper_provenance.lock
paper_provenance.yaml
registry.lock
registry.yaml
report.md
scripts
study_status.lock
task_context
writing_plan.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b679eea4-0d41-400f-b403-52224dadb4ee",
  "isSidechain": false,
  "promptId": "be49ce8a-0797-4b90-bc7b-9e8303358289",
  "type": "user",
  "uuid": "8d1f74c5-b004-45b2-b0ce-4d766637e0f0",
  "toolUseResult": {
    "stdout": "AGENTS.md\nRAGEN\nROADMAP.lock\nROADMAP.md\nartifacts\ncheckpoints\nconstraints.lock\nconstraints.yaml\ndecisions.lock\ndecisions.yaml\ndocs\ndream_registry.lock\ndream_registry.yaml\ndream_registry.yaml.bak\ndream_registry.yaml.bak.130710\nexperiment_plan.yaml\nliterature_map.yaml\nlogs\nmemory.md\npaper_framing.md\npaper_provenance.lock\npaper_provenance.yaml\nregistry.lock\nregistry.yaml\nreport.md\nscripts\nstudy_status.lock\ntask_context\nwriting_plan.yaml",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "b679eea4-0d41-400f-b403-52224dadb4ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1",
  "sessionId": "76d61b9e-2e1c-4565-b8a8-d68d26d41235",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T13:33:05.133Z_

<details open><summary>🔧 Tool call — Read · `toolu_01W5CeVFhvt1xP1KcRLGWzhc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d1f74c5-b004-45b2-b0ce-4d766637e0f0",
  "isSidechain": false,
  "requestId": "req_011Cb8E4iLHoMiEVNK8U68yC",
  "type": "assistant",
  "uuid": "39d038d5-e599-4f2b-af05-693e5290504f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1",
  "sessionId": "76d61b9e-2e1c-4565-b8a8-d68d26d41235",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PD6GiWSZzfQdY5XJUTHg8m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 259,
      "cache_read_input_tokens": 33443,
      "output_tokens": 88,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 259,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 88,
          "cache_read_input_tokens": 33443,
          "cache_creation_input_tokens": 259,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 259
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

_source line 16 · 2026-05-17T13:33:05.147Z_

<details><summary>↩ Tool result · `toolu_01W5CeVFhvt1xP1KcRLGWzhc`</summary>

```text
1	# Experiment Plan — Learning When to Verify
2	# Post-MVP rewrite: 2026-05-17 (Dream Review feedback integrated)
3	# Based on: paper_framing.md (dual mechanism theory + dual contribution)
4	#
5	# Claims:
6	#   claim_1: Step-independent GRPO catastrophically fails for multi-turn agents (dual mechanism)
7	#   claim_2: Action-change is effective intrinsic reward for verification informativeness
8	#   claim_3: Learned selective policy matches always-on at reduced cost
9	#
10	# Phases:
11	#   A+  — Episode-level training to convergence + consolidation (Claim 1)
12	#   B   — Selective verification implementation + training (Claims 2 & 3)
13	#   C   — Ablations & baselines (all claims, includes GAE)
14	#   D   — Scaling & generalization (reviewer defense)
15	#
16	# GPU budget: 2x RTX PRO 6000 96GB (cuda:0, cuda:1) @ bjb1-17606
17	# Key: h-sweep/GAE only 15 steps (sufficient to observe collapse pattern)
18	# Timeline at full utilization: P0 ~8 days, P0+P1 ~14 days, all ~20 days
19	
20	experiments:
21	
22	  # ============================================================
23	  # Phase A+: Episode-Level Training to Convergence
24	  # ============================================================
25	
26	  - id: "plan_001"
27	    title: "Episode-level GRPO convergence (exp029 continuation)"
28	    claim: "Claim 1"
29	    phase: "A+"
30	    priority: "P0"
31	    depends_on: []
32	    registry_id: "exp029_episode_level"
33	    status: "done"
34	    description: >
35	      Episode-level GRPO (context_window_mode: full) on Qwen3-1.7B + ALFWorld.
36	      50 steps, dual-GPU. MVP passed at step 5 (val=25%, 2x baseline 12.5%).
37	      Continue to convergence (step 20+) with tatsu parallel patch for 4x val speedup.
38	    hypothesis: >
39	      Episode-level training enables stable RL for multi-turn agents,
40	      reaching ≥40% success by convergence.
41	    metrics: ["success_rate", "action_is_valid", "kl_divergence", "entropy"]
42	    gpu_hours_estimate: 48
43	    framing_ref: "claim_1"
44	
45	  - id: "plan_002"
46	    title: "Context window h-sweep ablation (3 seeds each)"
47	    claim: "Claim 1"
48	    phase: "A+"
49	    priority: "P0"
50	    depends_on: ["plan_001"]
51	    registry_id: null
52	    status: "planned"
53	    description: >
54	      Sweep context_window h={2, 5, 10, 20, full} on same GRPO config.
55	      Config: context_window_mode=step_independent + step_independent_history_length={h}
56	      (h=full uses context_window_mode=full). 15 steps per run, 3 seeds each.
57	      KEY paper figure: shows credit assignment cliff is robust across seeds.
58	      Addresses Reviewer Concern #1 + Dream C3 (statistical power).
59	    hypothesis: >
60	      Performance degrades monotonically with smaller h, with sharp cliff
61	      below h=10. Cliff is robust across seeds (not single-run artifact).
62	    metrics: ["success_rate_per_h", "convergence_speed", "collapse_rate"]
63	    gpu_hours_estimate: 90
64	    notes: "5 h-values × 15 steps × 3 seeds. h=2 已有 exp028c 作 1 seed。"
65	
66	  - id: "plan_003"
67	    title: "Multi-seed replication (5 seeds total)"
68	    claim: "Claim 1"
69	    phase: "A+"
70	    priority: "P0"
71	    depends_on: ["plan_001"]
72	    registry_id: null
73	    status: "planned"
74	    description: >
75	      4 additional seeds for exp029 episode-level config (5 total incl original).
76	      Report mean ± std. Dream C3 要求 5-8 seeds for credible CI.
77	    hypothesis: >
78	      Episode-level success rate is reproducible (std < 5pp across 5 seeds).
79	    metrics: ["success_rate_mean", "success_rate_std"]
80	    gpu_hours_estimate: 192
81	
82	  - id: "plan_003b"
83	    title: "GAE baseline comparison"
84	    claim: "Claim 1"
85	    phase: "A+"
86	    priority: "P0"
87	    depends_on: ["plan_001"]
88	    registry_id: null
89	    status: "planned"
90	    description: >
91	      Dream C4 要求标准 RL baselines。实现 GAE(lambda=0.95, gamma=1.0) 和
92	      GAE(lambda=1.0, gamma=1.0) 在 RAGEN 中。需要 value function (critic head)。
93	      15 steps × 3 seeds each。如果 GAE >> episode-level GRPO → per-token credit
94	      assignment 额外有价值。如果持平 → episode-level 信息是关键。
95	      GRPO episode-level ≠ GAE(1,1)：GRPO 无 critic，所有 token 同一 advantage。
96	    hypothesis: >
97	      GAE provides modest improvement over episode-level GRPO due to
98	      finer credit assignment, but both far exceed step-independent.
99	    metrics: ["success_rate", "per_token_advantage_variance"]
100	    gpu_hours_estimate: 60
101	    notes: "需实现 critic head。如果实现成本过高，可用 REINFORCE baseline 替代。"
102	
103	  - id: "plan_003c"
104	    title: "Episode-level + valid_action_bonus (plateau-breaker, D056)"
105	    claim: "Claim 1"
106	    phase: "A+"
107	    priority: "P0"
108	    depends_on: ["plan_001"]
109	    registry_id: null
110	    status: "planned"
111	    description: >
112	      Derived from exp013f negative (D056): dense reward gaming is step_independent-specific.
113	      Episode-level training prevents per-step reward gaming because model optimizes
114	      full trajectory total reward. Add valid_action_bonus=0.05 to episode-level config.
115	      Test if this safely improves action_is_valid (currently 55.9%) without gaming,
116	      and whether it breaks the 23-25% success plateau.
117	      Run during h-sweep batch as h=full variant.
118	    hypothesis: >
119	      Episode-level + small valid_action_bonus safely improves action_is_valid
120	      (target ≥80%) without reward gaming, and success rate exceeds 30%
121	      (breaking exp029 plateau). Gaming only occurs under step_independent.
122	    metrics: ["success_rate", "action_is_valid", "valid_bonus_vs_task_reward_ratio"]
123	    gpu_hours_estimate: 24
124	    parent: "exp013f"
125	    notes: "Parent derivation: exp013f gaming → D056 insight → episode-level safety hypothesis"
126	
127	  - id: "plan_004"
128	    title: "Credit assignment mechanism empirical verification (paper Figure 2)"
129	    claim: "Claim 1"
130	    phase: "A+"
131	    priority: "P0"
132	    depends_on: ["plan_002"]
133	    registry_id: null
134	    status: "planned"
135	    description: >
136	      Empirically verify "Advantage Sign Misattribution" mechanism (D058, Reviewer-refined):
137	      (a) Per-window advantage logging from h=2 seed 2: record (episode_id, window_position,
138	          raw_return, advantage_sign, advantage_magnitude, episode_outcome, local_action_quality_proxy)
139	      (b) Key analysis: advantage sign vs episode outcome correlation (should be ~1.0),
140	          advantage sign vs local action quality correlation (should be ~0, proving misattribution)
141	      (c) Contrast success vs failure episodes: success → all positive (including bad windows),
142	          failure → all negative (including good windows)
143	      (d) γ^k magnitude decay: advantage magnitude vs position in success episodes
144	      (e) Episode-level control: all tokens share one advantage (no position/sign variance)
145	      Data source: LOG_PER_SAMPLE_ADV=1 on h=2 seed 2 (10 lines logging code, zero GPU overhead).
146	      Code reference: agent_trainer.py:271-340, core_algos.py:194-246.
147	    hypothesis: >
148	      Per-window advantage in step_independent shows: (1) advantage sign is determined
149	      by episode success/failure (correlation > 0.95), (2) advantage sign is NOT correlated
150	      with window-local action quality (r < 0.1), proving sign misattribution,
151	      (3) magnitude decays as γ^k from terminal position, (4) episode-level shows
152	      uniform advantage with no sign/magnitude position effects.
153	    metrics: ["sign_vs_outcome_correlation", "sign_vs_local_quality_correlation", "magnitude_position_decay_r2", "episode_level_variance"]
154	    gpu_hours_estimate: 4
155	    notes: "D058+Reviewer: 'sign misattribution' is the core mechanism (direction error > magnitude error). γ^k decay is secondary."
156	
157	  # ============================================================
158	  # Phase B: Selective Verification (Claims 2 & 3)
159	  # ============================================================
160	
161	  - id: "plan_005"
162	    title: "Action-change statistics from always-on runs"
163	    claim: "Claim 2"
164	    phase: "B"
165	    priority: "P1"
166	    depends_on: ["plan_001"]
167	    registry_id: null
168	    status: "planned"
169	    description: >
170	      Collect action-change statistics from exp029 trained checkpoints:
171	      (1) fraction of verifications triggering action change,
172	      (2) correlation between action change and episode success,
173	      (3) per-task-type breakdown.
174	      Informs reward design and provides empirical grounding.
175	    hypothesis: >
176	      Most verifications are confirmatory (>60% no action change).
177	      Action change positively correlates with episode success (r > 0.2).
178	    metrics: ["action_change_rate", "correlation", "confirmatory_rate"]
179	    gpu_hours_estimate: 4
180	
181	  - id: "plan_006"
182	    title: "Selective verification implementation"
183	    claim: "Claim 2"
184	    phase: "B"
185	    priority: "P1"
186	    depends_on: ["plan_005"]
187	    registry_id: null
188	    status: "planned"
189	    description: >
190	      Implement binary verify/skip decision in RAGEN framework.
191	      Agent outputs special token (verify/skip) before each step.
192	      Reward = task_success + alpha * action_change_when_verified - beta * verification_cost.
193	      Code-only, no GPU.
194	    hypothesis: null
195	    metrics: []
196	    gpu_hours_estimate: 0
197	
198	  - id: "plan_007"
199	    title: "B-IAVR selective verification training"
200	    claim: "Claim 2, Claim 3"
201	    phase: "B"
202	    priority: "P1"
203	    depends_on: ["plan_006", "plan_001"]
204	    registry_id: null
205	    status: "planned"
206	    description: >
207	      Train selective verification policy via episode-level GRPO.
208	      Initialize from best exp029 checkpoint. Action-change reward
209	      encourages verification only when informative.
210	    hypothesis: >
211	      B-IAVR achieves verification rate ↓40%+ vs always-on
212	      while maintaining success within 5pp of baseline.
213	    metrics: ["success_rate", "verification_rate", "cost_reduction"]
214	    gpu_hours_estimate: 96
215	
216	  - id: "plan_008"
217	    title: "Selective verification full comparison"
218	    claim: "Claim 3"
219	    phase: "B"
220	    priority: "P1"
221	    depends_on: ["plan_007"]
222	    registry_id: null
223	    status: "planned"
224	    description: >
225	      Compare on same val set: always-on / B-IAVR / no-verify / random-p / confidence-threshold.
226	      Report success rate, verification rate, total inference tokens, per-task breakdown.
227	    hypothesis: >
228	      B-IAVR dominates Pareto frontier (best success-to-cost ratio).
229	    metrics: ["success_rate", "verification_rate", "cost_reduction", "total_tokens"]
230	    gpu_hours_estimate: 8
231	
232	  # ============================================================
233	  # Phase C: Ablations & Causal Analysis
234	  # ============================================================
235	
236	  - id: "plan_009"
237	    title: "No-verify ablation"
238	    claim: "Claim 3"
239	    phase: "C"
240	    priority: "P1"
241	    depends_on: ["plan_001"]
242	    registry_id: null
243	    status: "planned"
244	    description: >
245	      Episode-level GRPO without any self-verification.
246	      Lower bound: demonstrates verification value.
247	    hypothesis: >
248	      Removing verification drops success by ≥10pp vs always-on.
249	    metrics: ["success_rate", "action_is_valid"]
250	    gpu_hours_estimate: 48
251	
252	  - id: "plan_010"
253	    title: "Entropy-controlled action-change analysis"
254	    claim: "Claim 2"
255	    phase: "C"
256	    priority: "P1"
257	    depends_on: ["plan_005"]
258	    registry_id: null
259	    status: "planned"
260	    description: >
261	      Defense for "action change = noise" concern.
262	      Stratify by policy entropy; test if action-change-success
263	      correlation holds within each stratum.
264	    hypothesis: >
265	      Partial correlation remains significant (p < 0.05) after controlling entropy.
266	    metrics: ["partial_correlation", "p_value"]
267	    gpu_hours_estimate: 4
268	
269	  - id: "plan_011"
270	    title: "Causal intervention: random vs verification-triggered changes"
271	    claim: "Claim 2"
272	    phase: "C"
273	    priority: "P1"
274	    depends_on: ["plan_001"]
275	    registry_id: null
276	    status: "planned"
277	    description: >
278	      Inject random action changes at same rate as verification-triggered.
279	      Compare task success. If verification-triggered >> random, causal evidence.
280	    hypothesis: >
281	      Verification-triggered changes yield ≥10pp higher success than random.
282	    metrics: ["success_rate_triggered", "success_rate_random", "delta"]
283	    gpu_hours_estimate: 8
284	
285	  - id: "plan_012"
286	    title: "Reward signal ablation (action-change vs alternatives)"
287	    claim: "Claim 2"
288	    phase: "C"
289	    priority: "P1"
290	    depends_on: ["plan_007"]
291	    registry_id: null
292	    status: "planned"
293	    description: >
294	      Train B-IAVR with alternative rewards: (a) action-change (ours),
295	      (b) random trigger reward, (c) confidence-based reward.
296	      Demonstrates action-change is the best signal.
297	    hypothesis: >
298	      Action-change reward produces best cost-performance tradeoff.
299	    metrics: ["success_rate", "verification_rate", "cost_reduction"]
300	    gpu_hours_estimate: 192
301	
302	  - id: "plan_013"
303	    title: "ARES reproduction + comparison"
304	    claim: "Claim 3"
305	    phase: "C"
306	    priority: "P1"
307	    depends_on: ["plan_007"]
308	    registry_id: null
309	    status: "planned"
310	    description: >
311	      Reproduce ARES SFT router on ALFWorld (same model).
312	      Head-to-head with B-IAVR on identical eval episodes.
313	      Addresses "ARES differentiation" concern.
314	    hypothesis: >
315	      B-IAVR achieves ≥10pp better cost reduction than ARES at matched success.
316	    metrics: ["success_rate", "verification_rate", "cost_reduction"]
317	    gpu_hours_estimate: 24
318	
319	  # ============================================================
320	  # Phase D: Scaling & Generalization (conditional)
321	  # ============================================================
322	
323	  - id: "plan_014"
324	    title: "ScienceWorld transfer (episode-level advantage)"
325	    claim: "Claim 1"
326	    phase: "D"
327	    priority: "P2"
328	    depends_on: ["plan_001"]
329	    registry_id: null
330	    status: "planned"
331	    description: >
332	      Validate episode-level vs step-independent on ScienceWorld.
333	      Different env, similar multi-turn structure. Addresses single-env concern.
334	    hypothesis: >
335	      Episode-level advantage generalizes: ≥2x improvement over step-independent.
336	    metrics: ["success_rate_episode", "success_rate_step_independent"]
337	    gpu_hours_estimate: 72
338	
339	  - id: "plan_015"
340	    title: "7B model scaling verification"
341	    claim: "Claim 1"
342	    phase: "D"
343	    priority: "P2"
344	    depends_on: ["plan_002"]
345	    registry_id: null
346	    status: "planned"
347	    description: >
348	      Episode-level vs step-independent on Qwen3-7B.
349	      Addresses model size concern. May need cloud GPU.
350	    hypothesis: >
351	      Episode-level advantage holds at 7B scale.
352	    metrics: ["success_rate_episode_7B", "success_rate_step_independent_7B"]
353	    gpu_hours_estimate: 192
354	    notes: "May require cloud GPU rental (4x A100 or 2x H100)"
355	
356	  - id: "plan_016"
357	    title: "Per-task-type breakdown analysis"
358	    claim: "Claim 1"
359	    phase: "D"
360	    priority: "P2"
361	    depends_on: ["plan_001"]
362	    registry_id: null
363	    status: "planned"
364	    description: >
365	      Breakdown by ALFWorld task type (pick, clean, heat, cool, examine, pick_two).
366	      Shows within-environment diversity.
367	    hypothesis: >
368	      Episode-level advantage varies by task complexity; longer tasks benefit more.
369	    metrics: ["per_task_success", "episode_length_correlation"]
370	    gpu_hours_estimate: 2
371	
372	# ============================================================
373	# Summary (updated 2026-05-17, Dream Review feedback)
374	# ============================================================
375	# Total experiments: 17
376	# Phase A+: 5 (plan_001-004, 003b) — ~438 GPU-h [P0, Claim 1]
377	#   - plan_001: 48h (exp029 convergence, running)
378	#   - plan_002: 90h (h-sweep, 5 values × 15 steps × 3 seeds)
379	#   - plan_003: 192h (multi-seed, 4 additional × full 50 steps)
380	#   - plan_003b: 60h (GAE baseline, 2 configs × 15 steps × 3 seeds)
381	#   - plan_004: 4h (mechanism analysis, CPU)
382	# Phase B:  4 (plan_005-008) — 108 GPU-h [P1, Claims 2&3]
383	# Phase C:  5 (plan_009-013) — 276 GPU-h [P1, all claims]
384	# Phase D:  3 (plan_014-016) — 266 GPU-h [P2, reviewer defense]
385	# Total: ~1088 GPU-h
386	#
387	# Critical path: plan_001 → plan_002/003/003b (parallel) → plan_004 → plan_005 → plan_006 → plan_007 → plan_008
388	# At 2 GPUs (48 GPU-h/day): P0 ~9 days, P0+P1 ~14 days, all ~22 days
389	#
390	# Minimum viable paper (P0 only): plan_001-004+003b = 394 GPU-h ≈ 8 days
391	# Full paper (P0+P1): 546 GPU-h ≈ 11 days (h-sweep/GAE 15-step optimization saves ~200h)
392	#
393	# Claim coverage:
394	#   Claim 1: plan_001, 002, 003, 003b, 004, 009, 014, 015, 016 (9 experiments)
395	#   Claim 2: plan_005, 006, 007, 010, 011, 012 (6 experiments)
396	#   Claim 3: plan_007, 008, 009, 013 (4 experiments)
397	#
398	# Dream Review responses:
399	#   C1 (theory mismatch): plan_004 reframed as dual-mechanism analysis (not γ decay)
400	#   C2 (novelty): dual contribution framing + "why community defaults to step-independent" analysis
401	#   C3 (statistics): plan_003 upgraded to 5 seeds; plan_002 to 3 seeds per h
402	#   C4 (baselines): plan_003b added (GAE)
403	#   C5 (references): Paper Agent task, not experiment
404	#   C6 (Self-Guide gap): positioning in paper_framing.md (different paradigm)
405	#
406	# Reviewer concern coverage:
407	#   RC1 (episode-level is obvious): plan_002, 004 (h-sweep + dual mechanism)
408	#   RC2 (single environment): plan_014, 016
409	#   RC3 (model size): plan_015
410	#   RC4 (action-change noise): plan_005, 010, 011, 012
411	#   RC5 (ARES differentiation): plan_013
412	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "39d038d5-e599-4f2b-af05-693e5290504f",
  "isSidechain": false,
  "promptId": "be49ce8a-0797-4b90-bc7b-9e8303358289",
  "type": "user",
  "uuid": "0436d053-0cab-4b20-ae4c-40909a7bec8c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/experiment_plan.yaml",
      "content": "# Experiment Plan — Learning When to Verify\n# Post-MVP rewrite: 2026-05-17 (Dream Review feedback integrated)\n# Based on: paper_framing.md (dual mechanism theory + dual contribution)\n#\n# Claims:\n#   claim_1: Step-independent GRPO catastrophically fails for multi-turn agents (dual mechanism)\n#   claim_2: Action-change is effective intrinsic reward for verification informativeness\n#   claim_3: Learned selective policy matches always-on at reduced cost\n#\n# Phases:\n#   A+  — Episode-level training to convergence + consolidation (Claim 1)\n#   B   — Selective verification implementation + training (Claims 2 & 3)\n#   C   — Ablations & baselines (all claims, includes GAE)\n#   D   — Scaling & generalization (reviewer defense)\n#\n# GPU budget: 2x RTX PRO 6000 96GB (cuda:0, cuda:1) @ bjb1-17606\n# Key: h-sweep/GAE only 15 steps (sufficient to observe collapse pattern)\n# Timeline at full utilization: P0 ~8 days, P0+P1 ~14 days, all ~20 days\n\nexperiments:\n\n  # ============================================================\n  # Phase A+: Episode-Level Training to Convergence\n  # ============================================================\n\n  - id: \"plan_001\"\n    title: \"Episode-level GRPO convergence (exp029 continuation)\"\n    claim: \"Claim 1\"\n    phase: \"A+\"\n    priority: \"P0\"\n    depends_on: []\n    registry_id: \"exp029_episode_level\"\n    status: \"done\"\n    description: >\n      Episode-level GRPO (context_window_mode: full) on Qwen3-1.7B + ALFWorld.\n      50 steps, dual-GPU. MVP passed at step 5 (val=25%, 2x baseline 12.5%).\n      Continue to convergence (step 20+) with tatsu parallel patch for 4x val speedup.\n    hypothesis: >\n      Episode-level training enables stable RL for multi-turn agents,\n      reaching ≥40% success by convergence.\n    metrics: [\"success_rate\", \"action_is_valid\", \"kl_divergence\", \"entropy\"]\n    gpu_hours_estimate: 48\n    framing_ref: \"claim_1\"\n\n  - id: \"plan_002\"\n    title: \"Context window h-sweep ablation (3 seeds each)\"\n    claim: \"Claim 1\"\n    phase: \"A+\"\n    priority: \"P0\"\n    depends_on: [\"plan_001\"]\n    registry_id: null\n    status: \"planned\"\n    description: >\n      Sweep context_window h={2, 5, 10, 20, full} on same GRPO config.\n      Config: context_window_mode=step_independent + step_independent_history_length={h}\n      (h=full uses context_window_mode=full). 15 steps per run, 3 seeds each.\n      KEY paper figure: shows credit assignment cliff is robust across seeds.\n      Addresses Reviewer Concern #1 + Dream C3 (statistical power).\n    hypothesis: >\n      Performance degrades monotonically with smaller h, with sharp cliff\n      below h=10. Cliff is robust across seeds (not single-run artifact).\n    metrics: [\"success_rate_per_h\", \"convergence_speed\", \"collapse_rate\"]\n    gpu_hours_estimate: 90\n    notes: \"5 h-values × 15 steps × 3 seeds. h=2 已有 exp028c 作 1 seed。\"\n\n  - id: \"plan_003\"\n    title: \"Multi-seed replication (5 seeds total)\"\n    claim: \"Claim 1\"\n    phase: \"A+\"\n    priority: \"P0\"\n    depends_on: [\"plan_001\"]\n    registry_id: null\n    status: \"planned\"\n    description: >\n      4 additional seeds for exp029 episode-level config (5 total incl original).\n      Report mean ± std. Dream C3 要求 5-8 seeds for credible CI.\n    hypothesis: >\n      Episode-level success rate is reproducible (std < 5pp across 5 seeds).\n    metrics: [\"success_rate_mean\", \"success_rate_std\"]\n    gpu_hours_estimate: 192\n\n  - id: \"plan_003b\"\n    title: \"GAE baseline comparison\"\n    claim: \"Claim 1\"\n    phase: \"A+\"\n    priority: \"P0\"\n    depends_on: [\"plan_001\"]\n    registry_id: null\n    status: \"planned\"\n    description: >\n      Dream C4 要求标准 RL baselines。实现 GAE(lambda=0.95, gamma=1.0) 和\n      GAE(lambda=1.0, gamma=1.0) 在 RAGEN 中。需要 value function (critic head)。\n      15 steps × 3 seeds each。如果 GAE >> episode-level GRPO → per-token credit\n      assignment 额外有价值。如果持平 → episode-level 信息是关键。\n      GRPO episode-level ≠ GAE(1,1)：GRPO 无 critic，所有 token 同一 advantage。\n    hypothesis: >\n      GAE provides modest improvement over episode-level GRPO due to\n      finer credit assignment, but both far exceed step-independent.\n    metrics: [\"success_rate\", \"per_token_advantage_variance\"]\n    gpu_hours_estimate: 60\n    notes: \"需实现 critic head。如果实现成本过高，可用 REINFORCE baseline 替代。\"\n\n  - id: \"plan_003c\"\n    title: \"Episode-level + valid_action_bonus (plateau-breaker, D056)\"\n    claim: \"Claim 1\"\n    phase: \"A+\"\n    priority: \"P0\"\n    depends_on: [\"plan_001\"]\n    registry_id: null\n    status: \"planned\"\n    description: >\n      Derived from exp013f negative (D056): dense reward gaming is step_independent-specific.\n      Episode-level training prevents per-step reward gaming because model optimizes\n      full trajectory total reward. Add valid_action_bonus=0.05 to episode-level config.\n      Test if this safely improves action_is_valid (currently 55.9%) without gaming,\n      and whether it breaks the 23-25% success plateau.\n      Run during h-sweep batch as h=full variant.\n    hypothesis: >\n      Episode-level + small valid_action_bonus safely improves action_is_valid\n      (target ≥80%) without reward gaming, and success rate exceeds 30%\n      (breaking exp029 plateau). Gaming only occurs under step_independent.\n    metrics: [\"success_rate\", \"action_is_valid\", \"valid_bonus_vs_task_reward_ratio\"]\n    gpu_hours_estimate: 24\n    parent: \"exp013f\"\n    notes: \"Parent derivation: exp013f gaming → D056 insight → episode-level safety hypothesis\"\n\n  - id: \"plan_004\"\n    title: \"Credit assignment mechanism empirical verification (paper Figure 2)\"\n    claim: \"Claim 1\"\n    phase: \"A+\"\n    priority: \"P0\"\n    depends_on: [\"plan_002\"]\n    registry_id: null\n    status: \"planned\"\n    description: >\n      Empirically verify \"Advantage Sign Misattribution\" mechanism (D058, Reviewer-refined):\n      (a) Per-window advantage logging from h=2 seed 2: record (episode_id, window_position,\n          raw_return, advantage_sign, advantage_magnitude, episode_outcome, local_action_quality_proxy)\n      (b) Key analysis: advantage sign vs episode outcome correlation (should be ~1.0),\n          advantage sign vs local action quality correlation (should be ~0, proving misattribution)\n      (c) Contrast success vs failure episodes: success → all positive (including bad windows),\n          failure → all negative (including good windows)\n      (d) γ^k magnitude decay: advantage magnitude vs position in success episodes\n      (e) Episode-level control: all tokens share one advantage (no position/sign variance)\n      Data source: LOG_PER_SAMPLE_ADV=1 on h=2 seed 2 (10 lines logging code, zero GPU overhead).\n      Code reference: agent_trainer.py:271-340, core_algos.py:194-246.\n    hypothesis: >\n      Per-window advantage in step_independent shows: (1) advantage sign is determined\n      by episode success/failure (correlation > 0.95), (2) advantage sign is NOT correlated\n      with window-local action quality (r < 0.1), proving sign misattribution,\n      (3) magnitude decays as γ^k from terminal position, (4) episode-level shows\n      uniform advantage with no sign/magnitude position effects.\n    metrics: [\"sign_vs_outcome_correlation\", \"sign_vs_local_quality_correlation\", \"magnitude_position_decay_r2\", \"episode_level_variance\"]\n    gpu_hours_estimate: 4\n    notes: \"D058+Reviewer: 'sign misattribution' is the core mechanism (direction error > magnitude error). γ^k decay is secondary.\"\n\n  # ============================================================\n  # Phase B: Selective Verification (Claims 2 & 3)\n  # ============================================================\n\n  - id: \"plan_005\"\n    title: \"Action-change statistics from always-on runs\"\n    claim: \"Claim 2\"\n    phase: \"B\"\n    priority: \"P1\"\n    depends_on: [\"plan_001\"]\n    registry_id: null\n    status: \"planned\"\n    description: >\n      Collect action-change statistics from exp029 trained checkpoints:\n      (1) fraction of verifications triggering action change,\n      (2) correlation between action change and episode success,\n      (3) per-task-type breakdown.\n      Informs reward design and provides empirical grounding.\n    hypothesis: >\n      Most verifications are confirmatory (>60% no action change).\n      Action change positively correlates with episode success (r > 0.2).\n    metrics: [\"action_change_rate\", \"correlation\", \"confirmatory_rate\"]\n    gpu_hours_estimate: 4\n\n  - id: \"plan_006\"\n    title: \"Selective verification implementation\"\n    claim: \"Claim 2\"\n    phase: \"B\"\n    priority: \"P1\"\n    depends_on: [\"plan_005\"]\n    registry_id: null\n    status: \"planned\"\n    description: >\n      Implement binary verify/skip decision in RAGEN framework.\n      Agent outputs special token (verify/skip) before each step.\n      Reward = task_success + alpha * action_change_when_verified - beta * verification_cost.\n      Code-only, no GPU.\n    hypothesis: null\n    metrics: []\n    gpu_hours_estimate: 0\n\n  - id: \"plan_007\"\n    title: \"B-IAVR selective verification training\"\n    claim: \"Claim 2, Claim 3\"\n    phase: \"B\"\n    priority: \"P1\"\n    depends_on: [\"plan_006\", \"plan_001\"]\n    registry_id: null\n    status: \"planned\"\n    description: >\n      Train selective verification policy via episode-level GRPO.\n      Initialize from best exp029 checkpoint. Action-change reward\n      encourages verification only when informative.\n    hypothesis: >\n      B-IAVR achieves verification rate ↓40%+ vs always-on\n      while maintaining success within 5pp of baseline.\n    metrics: [\"success_rate\", \"verification_rate\", \"cost_reduction\"]\n    gpu_hours_estimate: 96\n\n  - id: \"plan_008\"\n    title: \"Selective verification full comparison\"\n    claim: \"Claim 3\"\n    phase: \"B\"\n    priority: \"P1\"\n    depends_on: [\"plan_007\"]\n    registry_id: null\n    status: \"planned\"\n    description: >\n      Compare on same val set: always-on / B-IAVR / no-verify / random-p / confidence-threshold.\n      Report success rate, verification rate, total inference tokens, per-task breakdown.\n    hypothesis: >\n      B-IAVR dominates Pareto frontier (best success-to-cost ratio).\n    metrics: [\"success_rate\", \"verification_rate\", \"cost_reduction\", \"total_tokens\"]\n    gpu_hours_estimate: 8\n\n  # ============================================================\n  # Phase C: Ablations & Causal Analysis\n  # ============================================================\n\n  - id: \"plan_009\"\n    title: \"No-verify ablation\"\n    claim: \"Claim 3\"\n    phase: \"C\"\n    priority: \"P1\"\n    depends_on: [\"plan_001\"]\n    registry_id: null\n    status: \"planned\"\n    description: >\n      Episode-level GRPO without any self-verification.\n      Lower bound: demonstrates verification value.\n    hypothesis: >\n      Removing verification drops success by ≥10pp vs always-on.\n    metrics: [\"success_rate\", \"action_is_valid\"]\n    gpu_hours_estimate: 48\n\n  - id: \"plan_010\"\n    title: \"Entropy-controlled action-change analysis\"\n    claim: \"Claim 2\"\n    phase: \"C\"\n    priority: \"P1\"\n    depends_on: [\"plan_005\"]\n    registry_id: null\n    status: \"planned\"\n    description: >\n      Defense for \"action change = noise\" concern.\n      Stratify by policy entropy; test if action-change-success\n      correlation holds within each stratum.\n    hypothesis: >\n      Partial correlation remains significant (p < 0.05) after controlling entropy.\n    metrics: [\"partial_correlation\", \"p_value\"]\n    gpu_hours_estimate: 4\n\n  - id: \"plan_011\"\n    title: \"Causal intervention: random vs verification-triggered changes\"\n    claim: \"Claim 2\"\n    phase: \"C\"\n    priority: \"P1\"\n    depends_on: [\"plan_001\"]\n    registry_id: null\n    status: \"planned\"\n    description: >\n      Inject random action changes at same rate as verification-triggered.\n      Compare task success. If verification-triggered >> random, causal evidence.\n    hypothesis: >\n      Verification-triggered changes yield ≥10pp higher success than random.\n    metrics: [\"success_rate_triggered\", \"success_rate_random\", \"delta\"]\n    gpu_hours_estimate: 8\n\n  - id: \"plan_012\"\n    title: \"Reward signal ablation (action-change vs alternatives)\"\n    claim: \"Claim 2\"\n    phase: \"C\"\n    priority: \"P1\"\n    depends_on: [\"plan_007\"]\n    registry_id: null\n    status: \"planned\"\n    description: >\n      Train B-IAVR with alternative rewards: (a) action-change (ours),\n      (b) random trigger reward, (c) confidence-based reward.\n      Demonstrates action-change is the best signal.\n    hypothesis: >\n      Action-change reward produces best cost-performance tradeoff.\n    metrics: [\"success_rate\", \"verification_rate\", \"cost_reduction\"]\n    gpu_hours_estimate: 192\n\n  - id: \"plan_013\"\n    title: \"ARES reproduction + comparison\"\n    claim: \"Claim 3\"\n    phase: \"C\"\n    priority: \"P1\"\n    depends_on: [\"plan_007\"]\n    registry_id: null\n    status: \"planned\"\n    description: >\n      Reproduce ARES SFT router on ALFWorld (same model).\n      Head-to-head with B-IAVR on identical eval episodes.\n      Addresses \"ARES differentiation\" concern.\n    hypothesis: >\n      B-IAVR achieves ≥10pp better cost reduction than ARES at matched success.\n    metrics: [\"success_rate\", \"verification_rate\", \"cost_reduction\"]\n    gpu_hours_estimate: 24\n\n  # ============================================================\n  # Phase D: Scaling & Generalization (conditional)\n  # ============================================================\n\n  - id: \"plan_014\"\n    title: \"ScienceWorld transfer (episode-level advantage)\"\n    claim: \"Claim 1\"\n    phase: \"D\"\n    priority: \"P2\"\n    depends_on: [\"plan_001\"]\n    registry_id: null\n    status: \"planned\"\n    description: >\n      Validate episode-level vs step-independent on ScienceWorld.\n      Different env, similar multi-turn structure. Addresses single-env concern.\n    hypothesis: >\n      Episode-level advantage generalizes: ≥2x improvement over step-independent.\n    metrics: [\"success_rate_episode\", \"success_rate_step_independent\"]\n    gpu_hours_estimate: 72\n\n  - id: \"plan_015\"\n    title: \"7B model scaling verification\"\n    claim: \"Claim 1\"\n    phase: \"D\"\n    priority: \"P2\"\n    depends_on: [\"plan_002\"]\n    registry_id: null\n    status: \"planned\"\n    description: >\n      Episode-level vs step-independent on Qwen3-7B.\n      Addresses model size concern. May need cloud GPU.\n    hypothesis: >\n      Episode-level advantage holds at 7B scale.\n    metrics: [\"success_rate_episode_7B\", \"success_rate_step_independent_7B\"]\n    gpu_hours_estimate: 192\n    notes: \"May require cloud GPU rental (4x A100 or 2x H100)\"\n\n  - id: \"plan_016\"\n    title: \"Per-task-type breakdown analysis\"\n    claim: \"Claim 1\"\n    phase: \"D\"\n    priority: \"P2\"\n    depends_on: [\"plan_001\"]\n    registry_id: null\n    status: \"planned\"\n    description: >\n      Breakdown by ALFWorld task type (pick, clean, heat, cool, examine, pick_two).\n      Shows within-environment diversity.\n    hypothesis: >\n      Episode-level advantage varies by task complexity; longer tasks benefit more.\n    metrics: [\"per_task_success\", \"episode_length_correlation\"]\n    gpu_hours_estimate: 2\n\n# ============================================================\n# Summary (updated 2026-05-17, Dream Review feedback)\n# ============================================================\n# Total experiments: 17\n# Phase A+: 5 (plan_001-004, 003b) — ~438 GPU-h [P0, Claim 1]\n#   - plan_001: 48h (exp029 convergence, running)\n#   - plan_002: 90h (h-sweep, 5 values × 15 steps × 3 seeds)\n#   - plan_003: 192h (multi-seed, 4 additional × full 50 steps)\n#   - plan_003b: 60h (GAE baseline, 2 configs × 15 steps × 3 seeds)\n#   - plan_004: 4h (mechanism analysis, CPU)\n# Phase B:  4 (plan_005-008) — 108 GPU-h [P1, Claims 2&3]\n# Phase C:  5 (plan_009-013) — 276 GPU-h [P1, all claims]\n# Phase D:  3 (plan_014-016) — 266 GPU-h [P2, reviewer defense]\n# Total: ~1088 GPU-h\n#\n# Critical path: plan_001 → plan_002/003/003b (parallel) → plan_004 → plan_005 → plan_006 → plan_007 → plan_008\n# At 2 GPUs (48 GPU-h/day): P0 ~9 days, P0+P1 ~14 days, all ~22 days\n#\n# Minimum viable paper (P0 only): plan_001-004+003b = 394 GPU-h ≈ 8 days\n# Full paper (P0+P1): 546 GPU-h ≈ 11 days (h-sweep/GAE 15-step optimization saves ~200h)\n#\n# Claim coverage:\n#   Claim 1: plan_001, 002, 003, 003b, 004, 009, 014, 015, 016 (9 experiments)\n#   Claim 2: plan_005, 006, 007, 010, 011, 012 (6 experiments)\n#   Claim 3: plan_007, 008, 009, 013 (4 experiments)\n#\n# Dream Review responses:\n#   C1 (theory mismatch): plan_004 reframed as dual-mechanism analysis (not γ decay)\n#   C2 (novelty): dual contribution framing + \"why community defaults to step-independent\" analysis\n#   C3 (statistics): plan_003 upgraded to 5 seeds; plan_002 to 3 seeds per h\n#   C4 (baselines): plan_003b added (GAE)\n#   C5 (references): Paper Agent task, not experiment\n#   C6 (Self-Guide gap): positioning in paper_framing.md (different paradigm)\n#\n# Reviewer concern coverage:\n#   RC1 (episode-level is obvious): plan_002, 004 (h-sweep + dual mechanism)\n#   RC2 (single environment): plan_014, 016\n#   RC3 (model size): plan_015\n#   RC4 (action-change noise): plan_005, 010, 011, 012\n#   RC5 (ARES differentiation): plan_013\n",
      "numLines": 412,
      "startLine": 1,
      "totalLines": 412
    }
  },
  "sourceToolAssistantUUID": "39d038d5-e599-4f2b-af05-693e5290504f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1",
  "sessionId": "76d61b9e-2e1c-4565-b8a8-d68d26d41235",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 17 · 2026-05-17T13:33:05.217Z_

````json
{
  "parentUuid": "0436d053-0cab-4b20-ae4c-40909a7bec8c",
  "isSidechain": false,
  "attachment": {
    "type": "nested_memory",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/.claude/CLAUDE.md",
    "content": {
      "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/.claude/CLAUDE.md",
      "type": "Project",
      "content": "## 当前项目\n当前绑定项目：**cost-verify-agent-rl**\n\n## 按需查阅\n- 项目配置：`load_project_config(\"cost-verify-agent-rl\")` 或 `load_project_config(\"cost-verify-agent-rl\", section=\"execution\")`\n- 知识文件：`read_project_file(file=...)` 读取项目文件（ROADMAP.md/memory.md/ideas.md/report.md 等）\n- 路线图：`read_roadmap()` 读取研究方向和短期任务\n- 产出目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/`（写文件后用 `register_artifact` 注册）\n\n## Worker 操作规范\n\n### paper-writing-norms\n\n# 论文写作风格规范\n\n> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。\n\n---\n\n## 一、总体写作哲学\n\n### 1.1 故事驱动，不是数据堆砌\n\n- 论文必须以\"故事线\"为核心展开：问题 → 洞察 → 方法 → 验证\n- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进\n- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌\n- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing\n\n### 1.2 主线统一性\n\n- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**\n- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C\n- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机\n- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线\n\n### 1.3 专有名词必须有定义\n\n- 首次出现的专有名词/缩写必须给出完整定义和解释\n- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）\n- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用\n- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug\n\n### 1.4 写作前必读同类优秀论文\n\n- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可\n- 重点学：\n  - Abstract 怎么用最少篇幅讲完故事\n  - Introduction 怎么从大问题切入到具体贡献\n  - Related Work 怎么 positioning 自己（不是 survey）\n  - Table/Figure 怎么压缩信息密度\n- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大\n- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文\n\n---\n\n## 二、Abstract 写作规范\n\n### 2.1 四个必答问题（150-250 words）\n\nAbstract 必须在很短的篇幅内清楚回答：\n1. **研究什么问题** — 1-2 句话交代背景和痛点\n2. **为什么重要** — 现有方法的不足（不用写太多）\n3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）\n4. **结果说明什么** — 用具体实验结论支撑贡献\n\n### 2.2 禁忌\n\n- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim\n- **禁止过度宣传**：不说 \"revolutionary\"、\"groundbreaking\"\n- **禁止写成 Introduction 的缩写**：Abstract 是独立阅读单元\n- **禁止术语堆积**：如果审稿人几十秒内判断不出价值，就失败了\n- **缩写必须定义**：Abstract 中首次出现的缩写必须展开\n\n### 2.3 审稿人视角检验\n\n写完后用这个标准自检：审稿人能否在 30 秒内判断——\n- 问题是否重要？\n- 方法是否清楚？\n- 贡献是否可信？\n- 结果是否有说服力？\n\n---\n\n## 三、Introduction 写作规范\n\n### 3.1 完整叙事线（5 段结构）\n\nIntroduction 需要从一个清晰、重要的问题切入，逐步把读者带到核心贡献：\n\n1. **研究背景**（1-2 段）：大模型在某类能力/应用中已取得进展，但仍存在一个关键瓶颈\n2. **问题重要性**（1 段）：结合真实应用、已有方法局限或当前趋势，说明这不是小问题\n3. **现有方法不足**（1 段）：系统梳理为什么不够（依赖更大模型/更多数据/更复杂推理/更高成本，或只在特定 benchmark 有效）\n4. **本文核心想法**（1 段）：我们观察到什么、提出了什么方法、为什么能解决上述问题\n5. **贡献总结**（列表）：清楚列出方法贡献、实验贡献和分析贡献\n\n### 3.2 整体叙事结构\n\n```\n现有进展 → 关键缺口 → 本文洞察 → 方法概述 → 实验证据 → 贡献总结\n```\n\n### 3.3 禁忌\n\n- **禁止泛泛介绍**：不要开头就写 \"LLMs have shown remarkable capabilities...\"，要从具体问题切入\n- **禁止缺少过渡**：每段之间必须有逻辑连接\n- **禁止实验报告风格**：Introduction 不是 \"我们做了 X 实验得到了 Y 结果\" 的罗列\n- 每条 Contribution 必须有对应的 section/table 支撑\n- Contribution 列表中不能出现未在前文铺垫过的概念\n\n---\n\n## 四、Related Work 写作规范\n\n### 4.1 目标\n\n让审稿人相信：作者理解这个领域，知道自己的方法站在什么位置，清楚相对已有工作的真实增量在哪里。\n\n### 4.2 结构要求\n\n- 把已有工作分成几个清晰的主题（如模型训练、推理增强、工具调用、数据构建、评测等）\n- 每类简要说明：已有方法做了什么、解决了哪些问题、和本文的关系\n- 帮助读者理解：哪些是本文直接继承的，哪些方法不同但解决相似问题，哪些留下了本文要解决的缺口\n\n### 4.3 禁忌\n\n- **禁止论文堆砌**：不要写成 \"A proposed X. B proposed Y. C proposed Z.\" 的列表\n- **目标不是展示读了多少论文**，而是做归纳和比较\n- Contribution claim（\"To our knowledge, no prior work...\"）应放在 Introduction，不在 Related Work\n\n### 4.4 引用充足度\n\n- 引用必须覆盖：**直接相关方法、baseline 论文、评测 benchmark 论文、理论基础**\n- 任何一类缺失，审稿人会立刻看出来调研不充分\n- 引用密度参照目标会议近年录用论文的量级——明显偏少意味着 Related Work 调研不足\n\n---\n\n## 五、去 AI 写作风格（硬规则）\n\n以下模式是 AI 生成文本的典型标志，审稿人一眼能看出。**必须全部消除。**\n\n### 5.1 严禁破折号（最显著的 AI 痕迹）\n\n**这是 AI 写作最容易被识别的标志，审稿人最敏感。单列为最高优先级硬规则。**\n\n- 解释性 em-dash（—，U+2014）和 en-dash（–，U+2013）必须**全部删除**\n- 替代方式：用逗号、括号或拆分为两个句子\n- 强制检查命令：\n  ```bash\n  grep -n \"—\" paper/*.tex     # em-dash，每处人工判断是否必要\n  grep -n \" – \" paper/*.tex   # 解释性 en-dash，几乎都应删除\n  ```\n- 例外（允许保留）：表格分隔符、数字范围（`2020–2024`、`pp. 12–18`）、专有名词（`Newton–Raphson`）\n\n### 5.2 段落与句式\n\n- **禁止过度分段**：不需要每 2-3 句就换段，自然段 5-8 句是正常的\n- **减少关系从句**（which, that, who）：能用简洁直接的句子就不用从句\n- **禁止 -ing 短语结尾**：如 \"..., highlighting the applicability of...\" / \"..., demonstrating the effectiveness of...\"。这是 AI 写作最典型的标志之一\n- **禁止连续使用 \"Furthermore\" / \"Moreover\" / \"Additionally\"**：一段内最多用一个过渡词\n- **避免 \"It is worth noting that...\" / \"Notably, ...\"**：直接写要说的内容\n\n### 5.3 用词黑名单\n\n- 避免 \"delve into\" / \"leverage\" / \"utilize\" / \"facilitate\" — 用 \"explore\" / \"use\" / \"enable\"\n- 避免 \"a myriad of\" / \"a plethora of\" — 用 \"many\" / \"various\"\n- 避免 \"in the realm of\" / \"in the context of\" — 直接说\n- 避免 \"paradigm shift\" / \"novel\" 过度使用\n\n### 5.4 校对清单（4 步）\n\n1. 全文 proofread 语法和拼写\n2. 检查所有代词/指示词（this, that, it）是否指代明确\n3. **`grep \"—\"` + `grep \" – \"` 全文清零**（删除所有解释性 dash，§5.1）\n4. `grep \"ing,\"` 模式——大部分 -ing 分词短语需要改写\n\n---\n\n## 六、图表与视觉规范\n\n### 6.1 知识密度原则\n\n- **图表的信息必须紧凑**——不能为了美观而留大量白空间\n- 一张图如果只传达一个简单信息，要么缩小要么合并到其他图中\n- 能用 inline text 说清的不要占一整个 Figure\n\n### 6.2 表格规范\n\n- 表格和正文文字不能视觉重叠（检查 column 宽度和 alignment）\n- 小数精度全表统一\n- 最优加粗、次优下划线\n- Caption 必须自包含\n\n### 6.3 图片规范\n\n- 数值标签不能被线、bar、点遮住——用白色背景或偏移标签\n- 图中字体 >= 7pt（打印后仍可读）\n- 栏宽约束需匹配目标 venue 模板要求\n- 概念图/流程图要有信息量，不要画一个 trivial 的 pipeline 然后占半页\n\n### 6.4 空间效率\n\n- 顶会正文页数严格受限（具体页数查目标会议官网），每 cm² 都是宝贵资源\n- 优先使用 `\\subfigure` 合并相关图\n- Table 能 inline 就不要单独浮动\n- 图表占比与其对叙事的贡献成正比\n\n---\n\n## 七、投稿前通用准备\n\n### 7.1 模板必须官方（硬规则）\n\n- LaTeX 模板**必须从目标会议官网下载**（CallForPapers / Author Instructions 页面）\n- **不要用**：\n  - 网上他人转载的复制版本（可能被改过 margin / 行号设置）\n  - 上一年的模板（参数可能变：字体、margin、行号、anonymous 选项等）\n  - 组里学长留的旧版本（来源不明、无法追溯）\n- 风险：\n  - 样式不符合 → desk reject\n  - margin 不对 → 被审稿人质疑诚信\n  - reference 格式错 → 被认为不规范\n- 流程：先查会议官网 templates → 找不到再 `WebSearch \"{venue} {year} latex template official\"` → 仍找不到汇报 Director（不要用就近年版本顶替）\n- `\\documentclass[]{}` 选项必须与目标 venue + 阶段（review / camera-ready）一致\n\n### 7.2 投稿要求逐项核对\n\n- 目标会议如要求 Checklist / Ethical Statement / Broader Impact Statement / Reproducibility Statement，必须**认真填每一项**，不要全写 N/A\n- 页数限制：查目标会议官网\n- 匿名化要求：review 版 vs camera-ready 版本设置不同\n- 行号开启（review 版常需）\n- 字体大小、margin 不得修改 sty 文件\n\n### 7.3 最终修改 10 项检查流程\n\n提交前必须逐一检查：\n1. 所有最新实验结果已全部录入\n2. 根据实验结果将叙事调至最优状态\n3. 附录所有内容在正文中被引用且融入叙事\n4. 无数据堆砌（每个数字服务于叙事推进）\n5. Abstract 和 Introduction 具有吸引力（不是实验报告风格）\n6. 全文主线统一（idea 变化后各章节逻辑一致）\n7. 所有专有名词有定义\n8. 无 AI 风格标志（dash、-ing phrases、过度分段）\n9. 图表知识密度高、无视觉遮挡\n10. Reference 覆盖直接相关方法、baseline、benchmark、理论基础\n\n## 更多 Skills（按需加载）\n\n执行相关任务前，先 Read 对应 skill 获取环境配置和最佳实践。\n\n- **ssh-env-setup** — 远程服务器 Python/CUDA 环境搭建规范——discovery-first 流程、PEP 668 处理、PyTorch 版本选择。当需要在远程服务器搭建训练环境时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/ssh-env-setup.skill.md`\n- **check-training-status** — 当用户问训练进度/实验状态/查状态时使用。用专用工具查看训练状态，禁止 ssh_execute。  →  `/home/ubuntu/agent-ml-research/skills/global/check-training-status.skill.md`\n- **rebuttal** — 撰写和优化学术 rebuttal——逐条回应审稿意见，生成 response letter。当收到审稿意见、需要写 rebuttal、回复 reviewer 评论时使用。关键词：rebuttal、审稿意见、reviewer response、author response、meta-review、AC 意见。  →  `/home/ubuntu/agent-ml-research/skills/global/rebuttal.skill.md`\n- **review-reviewer-session-start** — Review Reviewer session 启动初始化——检查论文格式、编译状态、材料清单。Review Reviewer 角色 session 启动时自动使用。  →  `/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md`\n- **reference-audit** — 引用验证与审计——检查 bib 条目完整性、引用真实性、格式一致性。写论文、审查论文、提交前检查引用时使用。关键词：citation verification、引用检查、bib 审计、fake citation、引用格式。  →  `/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md`\n- **accelerate-distributed** — HuggingFace Accelerate 分布式训练指南——4行代码实现多GPU/DeepSpeed/FSDP/混合精度。多GPU训练时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/accelerate-distributed.skill.md`\n- **draw-paper-figure** — 生成学术论文级 matplotlib 图表——reliability diagrams、ECE heatmap、T* scatter plot、模型对比图，直接在 A6000 服务器上执行，输出 PDF/PNG  →  `/home/ubuntu/agent-ml-research/skills/global/draw-paper-figure.skill.md`\n- **experiment-analysis** — 实验结果分析框架——统计显著性检验、消融分析、baseline 对比、可视化建议。分析实验结果或撰写论文 Results 部分时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/experiment-analysis.skill.md`\n- **hf-hub** — HuggingFace Hub CLI (hf) — 下载/上传模型和数据集、管理缓存、搜索论文和模型。涉及 HuggingFace 资源操作时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/hf-hub.skill.md`\n- **latex-paper** — ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md`\n- **lm-eval-harness** — lm-evaluation-harness 模型评估指南——MMLU/GSM8K/HumanEval 等 60+ 学术基准测试。评估模型质量、对比实验时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/lm-eval-harness.skill.md`\n- **ml-experiment-guide** — 跨项目 ML 实验避坑指南——从多个项目沉淀的通用踩坑经验与最佳实践。当 Worker 准备写实验代码、或排查实验问题时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/ml-experiment-guide.skill.md`\n- **paper-banana** — 用 PaperBanana 生成发表级学术统计图——LLM 写 matplotlib 代码 + Critic 迭代 3 轮，输入 CSV/JSON 数据 + 意图描述即可。需要 GOOGLE_API_KEY。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-banana.skill.md`\n- **paper-image-extractor** — 从论文 PDF 或 arXiv 源码包提取图表——优先 arXiv 原始图片，回退 PDF 解析。用户说\"提取图\"/\"抽图\"/\"extract figures\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-image-extractor.skill.md`\n- **peft-lora** — PEFT/LoRA/QLoRA 参数高效微调指南——LoRA 配置选择、QLoRA 量化训练、Adapter 管理与合并。微调大模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/peft-lora.skill.md`\n- **research-news** — 每日论文推荐——搜索 arXiv 最新论文，按相关性/新颖性/影响力评分，生成推荐列表。Director 说\"有什么新论文\"/\"最近进展\"/\"research news\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/research-news.skill.md`\n- **trl-training** — TRL (Transformer Reinforcement Learning) 训练指南——SFT/DPO/GRPO/KTO 配置与最佳实践。训练或对齐语言模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/trl-training.skill.md`\n- **wandb-guide** — W&B 查询最佳实践——如何高效使用 fetch_wandb_metrics / compare_wandb_runs / get_best_wandb_run 分析实验结果。分析实验指标时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/wandb-guide.skill.md`\n",
      "contentDiffersFromDisk": false
    },
    "displayPath": "projects/cost-verify-agent-rl/.claude/CLAUDE.md"
  },
  "type": "attachment",
  "uuid": "6d6ce617-4c0f-44d9-8592-5cc36f3d0f60",
  "timestamp": "2026-05-17T13:33:05.217Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1",
  "sessionId": "76d61b9e-2e1c-4565-b8a8-d68d26d41235",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

---

### Runtime record

_source line 18_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Episode-level 训练收敛到强 performance，双机制理论完整验证，selective verification 可行，contrarian positioning 成立 核心假设：['Episode-level GRPO 收敛至 ≥45% val success（pass@1），打破当前…",
  "leafUuid": "6d6ce617-4c0f-44d9-8592-5cc36f3d0f60",
  "sessionId": "76d61b9e-2e1c-4565-b8a8-d68d26d41235"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Episode-level RL for multi-turn agent training",
  "sessionId": "76d61b9e-2e1c-4565-b8a8-d68d26d41235"
}
```

---

### Assistant

_source line 20 · 2026-05-17T13:33:53.889Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed best-tier predictions for all planned experiments in the experiment plan. Let me carefully analyze each experiment and produce the expected results with rationales.

Let me understand the "best" tier definition:
- Episode-level training converges to strong performance
- Dual mechanism theory fully verified
- Selective verification feasible
- Contrarian positioning holds

Key metric ranges for best tier:
- episode_level_val_success_converged: [0.45, 0.6]
- step_independent_h2_val_success: [0.0, 0.05]
- h_sweep_cliff_threshold: [8, 12]


- sign_vs_outcome_correlation: [0.95, 1.0]
- sign_vs_local_quality_correlation: [0.0, 0.1]
- gamma_k_magnitude_decay_r2: [0.85, 0.99]
- multi_seed_mean_success: [0.42, 0.58]
- multi_seed_std: [0.02, 0.05]
- gae_vs_episode_level_delta_pp: [-3, 5]
- selective_verification_rate_reduction: [0.4, 0.65]
- selective_success_delta: (continuing to review the remaining metric ranges)

Now I need to work through each of the 16 plans and generate their expected results. Looking at the current exp029 data, I'm seeing step 15 with validation success at 28.1% and pass_at_8 reaching 92.9%, while training success is at 43.75% with 15 of 100 steps completed. The hsweep_h2_seed1 run is showing concerning behavior—there's a sharp collapse between steps 3 and 4 where success plummets from 18.75% to 5.47%, eventually bottoming out near zero by step 9, with invalid actions spiking dramatically to 64.1%.

For the best-tier plans, I need plan_001 to eventually converge above 45% validation success—currently it's tracking at 28.125% at step 15, so I'm looking for it to reach the 45-60% range by convergence. Plan_002 shows a clear performance cliff below h=8-12 that holds consistently across seeds. Plans_003 through 003c involve multi-seed validation with tighter variance bounds and comparisons between GAE and episode-level approaches. Plans_004 through 016 focus on empirical verification of sign misattribution and selective validation strategies.

Now I'm drafting the specifics. For plan_001, the validation trajectory is climbing slowly from 25% at step 5 to 28.125% at step 15, while training's already at 43.75%—that gap suggests the model is learning task-specific patterns that haven't generalized yet. With continued training, I expect validation to accelerate and reach around 48% by step 40-50 as the policy explores more diverse strategies and generalization catches up. For plan_002, I'm examining the h-sweep results to confirm the sharp performance boundary. We already have h=2 data (hsweep_h2_seed1 showing collapse at step 3-4, going to 0% by step 9). Best tier needs sharp cliff at h<10. Expected:
- h=2: ~0-3% success by step 15 (collapse confirmed by seed 1)
- h=5: ~5-10% success (partial information, still collapses but slower)
- h=10: ~15-25% success (cliff threshold zone, may survive partially)
- h=20: ~30-40% success (enough context for some multi-step strategies)
- h=full: ~45-50% (full episode-level, reference from plan_001)

For plan_003, I'm running multi-seed experiments with 5 seeds at episode-level, expecting 45-55% mean success with 2-5pp standard deviation since the consistent gradient signal minimizes sign misattribution issues. Plan_003b tests GAE baseline against episode-level GRPO, anticipating similar performance within 3-5pp since both solve the core sign problem, though GAE's per-token credit might be offset by critic noise. Plan_003c adds a small valid_action_bonus to episode-level training, targeting ≥35% success and ≥80% action validity without gaming, since the trajectory-level optimization prevents the per-step bonus accumulation that caused gaming in earlier experiments. Now I'm moving to plan_004 to empirically verify the underlying mechanisms.

Looking at the mechanism verification data: sign-outcome correlation is very strong at 0.97, but sign-local quality correlation is nearly zero at 0.05, confirming that the gradient signal tracks episode outcomes rather than step-level quality. The gamma decay shows good fit (R²=0.92) and episode-level variance is essentially zero since all tokens share the same advantage. For plan_005, I'm examining action-change statistics where verification happens about 72% of the time without changing the action, with actual changes occurring 28% of the time and correlating moderately with success (r≈0.35). Plan_006 is implementation without results yet. Plan_007 tests B-IAVR training with selective verification, achieving roughly 45% verification rate (55% reduction from always-on) while maintaining ~46% success within 2pp of the baseline, cutting computational cost by about 50%. Plan_008 shows B-IAVR dominates the Pareto frontier in the efficiency-performance tradeoff. Plan_009 tests the no-verify baseline.

Now examining the ablation studies: removing verification entirely drops success by about 12pp compared to always-on. Entropy-controlled analysis reveals the partial correlation becomes significant after controlling for entropy. Causal intervention shows verification-triggered action changes outperform random changes by roughly 15pp. The reward signal ablation indicates that action-change rewards work best among the alternatives tested. Comparing to ARES, B-IAVR achieves about 15pp better cost reduction. Transfer to ScienceWorld shows episode-level advantages are at least 2.5x larger than step-independent effects. The 7B scaling experiments confirm the episode-level advantage persists at larger model sizes. Finally, the per-task breakdown reveals longer tasks benefit more from the episode-level approach.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d6ce617-4c0f-44d9-8592-5cc36f3d0f60",
  "isSidechain": false,
  "requestId": "req_011Cb8E4rXey2yosgsPvb6uM",
  "type": "assistant",
  "uuid": "48c34c69-072a-4ccc-a5ed-3ad4cfce6b2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1",
  "sessionId": "76d61b9e-2e1c-4565-b8a8-d68d26d41235",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014j9MsGdMguX6UpRxZZyacL",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12520,
      "cache_read_input_tokens": 33702,
      "output_tokens": 18558,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12520,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 18558,
          "cache_read_input_tokens": 33702,
          "cache_creation_input_tokens": 12520,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12520
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

_source line 21 · 2026-05-17T13:39:23.571Z_

```yaml
tier: best
narrative_guidance: >
  原始 framing 完全成立。Episode-level GRPO 突破 28% plateau 收敛至 ~48% val success，
  双机制理论（sign misattribution + information loss）通过 h-sweep cliff 和 per-window
  advantage logging 完整实证验证。Contrarian positioning 成立：更粗的 episode-level credit
  优于社区默认的 finer credit（GAE 仅持平，不优于 episode-level GRPO，证明 episode-level 信息
  是关键而非 per-token credit assignment）。Selective verification（B-IAVR）以 ~55%
  verification reduction 匹配 always-on performance，action-change reward 有效。
  ScienceWorld transfer 成功回应 single-env 攻击。五 seed 复现 std<4pp。
  三个 claim 全部成立，不需要降级，可投 NeurIPS/ICLR 主会。

imagined_experiments:

  # ============================================================
  # Phase A+: Episode-Level Training to Convergence
  # ============================================================

  - name: "Episode-level GRPO convergence (exp029 continuation)"
    plan_id: "plan_001"
    description: >
      Episode-level GRPO 继续训练至 step 50+。当前 step15 val=28.125%，
      train=43.75%。观察 val success 是否突破 plateau 并收敛至 ≥45%。
    expected_results:
      step20_val_success: 0.34
      step30_val_success: 0.42
      step40_val_success: 0.47
      step50_val_success: 0.48
      converged_val_pass_at_1: 0.48
      converged_val_pass_at_8: 0.96
      converged_train_success: 0.56
      converged_action_is_valid: 0.72
      converged_action_is_effective: 0.85
      converged_entropy: 0.15
      converged_ppo_kl: 0.008
      convergence_step: 45
      total_training_hours: 22
    result_rationale: >
      当前 train success（43.75%）大幅领先 val success（28.125%），说明模型已学到有效策略
      但尚未充分泛化。这个 train-val gap 的缩小是 RL 训练的典型模式：早期策略过拟合训练任务
      分布，随着 entropy 逐渐降低和 policy 稳定，模型学到更通用的行动模式（如 "先探索容器再
      去目标位置" 的跨任务策略）。Step 15→30 是加速期（policy 从探索转向利用），step 30→50
      进入收敛区。Val success 从 28%→48% 的跃升源于 episode-level 训练消除了 sign
      misattribution——正确的梯度方向保证了训练信号持续积累而非在好坏 window 间相互抵消。
      Action_is_valid 从 55%→72% 的改善是 success 提升的副产品（成功 trajectory 自然包含
      更多有效动作）。最终 48% 而非更高，因为 Qwen3-1.7B 的基础能力限制了 ceiling
      （pass@8=0.96 说明潜力在 ~50% 左右）。
    tables:
      - title: "Episode-level GRPO training trajectory"
        columns: ["step", "val_success", "train_success", "action_is_valid", "entropy", "pass_at_8"]
        rows:
          - [5, 0.250, 0.31, 0.48, 0.22, 0.82]
          - [10, 0.250, 0.38, 0.51, 0.19, 0.88]
          - [15, 0.281, 0.438, 0.545, 0.17, 0.93]
          - [20, 0.340, 0.48, 0.60, 0.16, 0.94]
          - [30, 0.420, 0.53, 0.67, 0.15, 0.95]
          - [40, 0.470, 0.55, 0.71, 0.15, 0.96]
          - [50, 0.480, 0.56, 0.72, 0.15, 0.96]
    figures_description:
      - "Fig: Val success vs training step，显示 step 15-30 加速区和 step 40+ 收敛 plateau。附 train success 作为 upper envelope 参考。"
    analysis: >
      收敛值 48% 是 best 档的核心支撑点。关键观察：(1) train-val gap 从 15pp (step15) 缩小到
      8pp (step50)，表明 policy 泛化逐步改善；(2) pass@8 从 0.93→0.96 表明多数任务在 8 次采样
      内可解，constraint 是 greedy decoding 下的 deterministic 策略选择；(3) 48% 对比
      exp028c 的 0% (step10 val)，episode-level 优势倍率 >10x，为 Claim 1 提供最直接证据。

  - name: "Context window h-sweep ablation (3 seeds each)"
    plan_id: "plan_002"
    description: >
      h={2, 5, 10, 20, full}，每值 3 seeds，各 15 steps。展示 credit assignment cliff
      的位置和 robustness。Paper 核心 Figure。
    expected_results:
      h2_mean_step15_success: 0.02
      h2_std: 0.02
      h2_collapse_onset_step_mean: 4.0
      h5_mean_step15_success: 0.06
      h5_std: 0.03
      h5_collapse_onset_step_mean: 6.5
      h10_mean_step15_success: 0.18
      h10_std: 0.04
      h10_collapse_onset_step_mean: null
      h20_mean_step15_success: 0.31
      h20_std: 0.04
      h20_collapse_onset_step_mean: null
      full_mean_step15_success: 0.38
      full_std: 0.03
      cliff_threshold: 10
      all_seeds_show_cliff_below_h10: true
    result_rationale: >
      h-sweep 结果由双机制共同决定：(1) Information loss — h=2 的 2-step context 窗口完全无法
      编码跨步策略（如 "先开冰箱再放东西"），模型只能做 reactive single-step 决策。h=5 稍好但
      仍不足以覆盖 ALFWorld 平均 ~25 步的关键策略跨度。h=10 开始捕获部分多步依赖。h=20 覆盖
      大部分策略所需上下文。(2) Sign misattribution — h 越小，独立优化的 window 越多
      （T/h 个），sign misattribution 影响越大。h=2 产生 ~12 个独立 window，每个 window 的
      advantage 符号完全由 episode outcome 决定而非 window-local action quality。h=10 产生
      ~2-3 个 window，misattribution 仍存在但影响较小。h=full 完全消除 window 间 sign
      问题。Cliff 在 h=10 附近是因为这是两个机制 jointly 从 "勉强可学" 转为 "不可学" 的
      临界点。已有 hsweep_h2_seed1 数据验证 h=2 collapse 模式（step3→4 onset，step9 归零），
      3-seed 复现确认非 outlier。
    tables:
      - title: "h-sweep performance summary (step 15, 3 seeds)"
        columns: ["h", "mean_success", "std", "seed1", "seed2", "seed3", "collapse?"]
        rows:
          - [2, 0.02, 0.02, 0.00, 0.03, 0.02, "Yes (step 3-5)"]
          - [5, 0.06, 0.03, 0.04, 0.09, 0.05, "Yes (step 6-8)"]
          - [10, 0.18, 0.04, 0.22, 0.16, 0.15, "No (slow decline)"]
          - [20, 0.31, 0.04, 0.34, 0.28, 0.31, "No"]
          - ["full", 0.38, 0.03, 0.40, 0.36, 0.38, "No"]
      - title: "Collapse onset step (mean across seeds)"
        columns: ["h", "collapse_onset_step", "success_at_onset", "final_success"]
        rows:
          - [2, 4.0, 0.15, 0.02]
          - [5, 6.5, 0.12, 0.06]
          - [10, "N/A", "N/A", 0.18]
          - [20, "N/A", "N/A", 0.31]
          - ["full", "N/A", "N/A", 0.38]
    figures_description:
      - "Fig 1 (paper Figure 1): h vs mean success rate (step 15) with error bars (±1 std across 3 seeds)。清晰展示 h=10 处 sharp cliff。所有 3 seeds 在 h<10 区域一致 collapse。"
      - "Fig 1b: Training curves per h value (success vs step)，以 shaded region 表示 seed 间 std。h=2 和 h=5 的 collapse 轨迹清晰可见。"
    analysis: >
      Cliff 位于 h=10 处（从 18%→6%→2% 的两级跌落），且 3 seeds 无 outlier（所有 seed 在
      h<10 时均展示 collapse）。这是 paper 最关键的 figure 之一：(1) 证明 step-independent
      失败不是 hyperparameter 敏感性问题而是结构性缺陷；(2) cliff 的存在证明问题不是
      "逐渐退化" 而是 "相变式崩溃"；(3) h=20 vs full 的 gap (31% vs 38%) 说明即使
      较大的 h 仍有 information loss，episode-level 是最优的。

  - name: "Multi-seed replication (5 seeds total)"
    plan_id: "plan_003"
    description: >
      4 additional seeds for episode-level config，加原始 seed 共 5 个。
      Full training to convergence (~50 steps each)。Report mean ± std。
    expected_results:
      seed1_converged_success: 0.48
      seed2_converged_success: 0.45
      seed3_converged_success: 0.50
      seed4_converged_success: 0.44
      seed5_converged_success: 0.52
      mean_success: 0.478
      std_success: 0.031
      ci_95_lower: 0.44
      ci_95_upper: 0.52
      all_seeds_above_40pct: true
      convergence_step_range: [40, 55]
    result_rationale: >
      Episode-level GRPO 的 seed 间 variance 低（std ~3pp）有三个原因：(1) 消除 sign
      misattribution 后，所有 seed 收到一致的正确梯度方向——不像 step-independent 中
      不同 seed 可能在不同 step 发生 collapse（hsweep_h2_seed1 在 step4 开始 collapse，
      而 exp028c 是不同模式）；(2) GRPO 的 group-based advantage normalization 提供了
      自然的 variance reduction（相比 REINFORCE）；(3) ALFWorld 任务分布相对 structured
      （6 个 task type，每类有清晰的最优策略模式），policy 收敛目标较为 deterministic。
      Mean 47.8% 在 best 档指标范围 [42%, 58%] 内偏中。各 seed 的差异主要来自早期
      exploration 随机性决定的策略发现顺序（某些 seed 先学会 clean task 的策略，另一些
      先学会 pick task）。
    tables:
      - title: "Multi-seed episode-level GRPO results"
        columns: ["seed", "converged_success", "convergence_step", "final_action_is_valid", "final_pass_at_8"]
        rows:
          - [1, 0.48, 45, 0.72, 0.96]
          - [2, 0.45, 50, 0.69, 0.94]
          - [3, 0.50, 42, 0.74, 0.97]
          - [4, 0.44, 55, 0.68, 0.93]
          - [5, 0.52, 40, 0.76, 0.97]
          - ["mean±std", "0.478±0.031", "46.4±5.9", "0.718±0.032", "0.954±0.017"]
    figures_description:
      - "Fig: 5 seeds training curves (val success vs step) overlay plot with individual thin lines + bold mean line + shaded std band。"
    analysis: >
      Std=3.1pp 满足 <5pp 要求。95% CI [0.44, 0.52] 不包含 step-independent 的任何
      positive result（exp028c step10=0%），差异显著（p<0.001, Welch t-test）。
      所有 5 seeds 均超过 40%，无 seed 是 failure case。

  - name: "GAE baseline comparison"
    plan_id: "plan_003b"
    description: >
      GAE(λ=0.95, γ=1.0) 和 GAE(λ=1.0, γ=1.0) 在 RAGEN 中实现。
      15 steps × 3 seeds each。与 episode-level GRPO 对比。
    expected_results:
      gae_095_mean_step15_success: 0.36
      gae_095_std: 0.04
      gae_100_mean_step15_success: 0.39
      gae_100_std: 0.04
      episode_grpo_mean_step15_success: 0.38
      episode_grpo_std: 0.03
      gae_095_vs_episode_delta_pp: -2.0
      gae_100_vs_episode_delta_pp: 1.0
      both_far_exceed_step_independent: true
      step_independent_h2_step15_success: 0.02
    result_rationale: >
      GAE 与 episode-level GRPO 持平（delta < 5pp）是 best 档的关键预测，因为它直接
      支持 contrarian positioning：更精细的 per-token credit assignment（GAE 提供）
      并不比更粗的 episode-level credit（GRPO 提供）更好。机制解释：(1) GAE(λ=1,γ=1)
      在极限下等价于 Monte Carlo return + baseline subtraction，与 episode-level GRPO
      的 group-normalized advantage 在信息量上相近——两者都使用完整 episode return，
      差异仅在 advantage 计算方式（GAE 用 learned value function, GRPO 用 group statistics）。
      (2) GAE(λ=0.95) 引入了 temporal discounting 的 bias（偏向近期 reward），
      在 sparse binary reward（只有 episode end 有 reward）下这个 bias 没有帮助反而
      略微损害性能。(3) Critic head 的 estimation error（尤其是训练早期 value function
      不准确时）引入 noise，抵消了 per-token credit 的理论优势。(4) 关键是：GAE 和
      episode-level GRPO 都解决了 sign misattribution（因为都使用 episode-level return），
      所以两者都远超 step-independent。性能差异只反映 credit assignment granularity 的
      边际价值，在 sparse reward 设定下这个边际很小。
    tables:
      - title: "GAE vs Episode-level GRPO comparison (step 15, 3 seeds)"
        columns: ["method", "mean_success", "std", "vs_step_independent_ratio"]
        rows:
          - ["GAE(λ=0.95, γ=1.0)", 0.36, 0.04, "18x"]
          - ["GAE(λ=1.0, γ=1.0)", 0.39, 0.04, "19.5x"]
          - ["Episode-level GRPO", 0.38, 0.03, "19x"]
          - ["Step-independent (h=2)", 0.02, 0.02, "1x (baseline)"]
    figures_description:
      - "Fig: Bar chart comparing 4 methods, 显示 GAE 与 episode-level GRPO 持平，两者均远超 step-independent。Error bars for std across seeds。"
    analysis: >
      GAE 与 episode-level GRPO 的 delta < 5pp 是 paper 的关键论据：证明 episode-level
      信息（而非 per-token credit assignment）是多轮 agent RL 成功的核心要素。
      这直接挑战 "越细越好" 的社区假设——Turn-PPO、GAGPO、iStar 都投入复杂机制做
      finer credit，但我们的证据表明在 sparse reward 多轮设定下，这些复杂性是不必要的。
      GRPO 的简洁性（无 critic、无 value function）反而是优势。

  - name: "Episode-level + valid_action_bonus (plateau-breaker, D056)"
    plan_id: "plan_003c"
    description: >
      在 episode-level config 上加 valid_action_bonus=0.05。测试是否安全提升
      action_is_valid 且突破 exp029 的 23-28% success plateau。
    expected_results:
      step15_val_success: 0.36
      step15_val_action_is_valid: 0.82
      step15_val_action_is_effective: 0.90
      valid_bonus_vs_task_reward_ratio: 0.18
      gaming_detected: false
      success_vs_baseline_delta_pp: 8.0
      action_is_valid_improvement_pp: 27.0
    result_rationale: >
      Episode-level 训练下 valid_action_bonus 安全有效，原因与 step-independent 下的
      gaming 机制截然不同。在 exp013f（step-independent）中，model 优化的是每个独立
      window 的 per-step reward，所以累积的 valid_action_bonus（~4.5 over 50 steps）
      主导了 learning signal，model 学会 "总是输出有效但无用的动作" 来最大化 bonus。
      在 episode-level 下，model 优化的是整条 trajectory 的 total reward（success=10
      + Σvalid_bonus）。关键差异：GRPO 的 advantage 是 group-normalized 的，所以所有
      trajectory 都有相似的 valid_bonus 总量（因为 action count 大致相同），advantage
      的区分度主要来自 success reward（有/无 10 分的差异远大于 valid_bonus 的微小变化）。
      因此 model 被引导向 success 方向学习，同时 valid_action_bonus 作为 exploration
      shaping 帮助 model 避免输出无效动作（从 55%→82%），间接提升 success（有效动作
      是成功的前提）。36% 的 success（vs baseline 28%）表明打破了 plateau。
    tables:
      - title: "Episode-level + valid_action_bonus vs baseline (step 15)"
        columns: ["config", "success", "action_is_valid", "gaming_indicator"]
        rows:
          - ["episode-level baseline", 0.281, 0.545, "N/A"]
          - ["episode-level + bonus", 0.360, 0.820, "No"]
          - ["step-independent + bonus (exp013f)", 0.000, 0.975, "Yes (reward ratio 1:67)"]
    figures_description:
      - "Fig: action_is_valid 和 success 的双轴 training curves 对比（baseline vs +bonus vs exp013f）。exp013f 展示 gaming pattern（valid↑ success↓），episode-level +bonus 展示 safe co-improvement。"
    analysis: >
      这个实验同时服务于两个目的：(1) 作为 plateau-breaker 提升 episode-level 基线
      performance；(2) 作为 dense reward gaming 是 step-independent-specific 的
      因果证据（same bonus, different training mode → gaming vs no-gaming）。

  - name: "Credit assignment mechanism empirical verification (paper Figure 2)"
    plan_id: "plan_004"
    description: >
      Per-window advantage logging 实证验证 sign misattribution 机制。
      从 h=2 seed 2 收集 advantage 数据并分析 sign-outcome correlation。
    expected_results:
      sign_vs_outcome_correlation: 0.97
      sign_vs_local_quality_correlation: 0.04
      gamma_k_magnitude_decay_r2: 0.92
      episode_level_advantage_sign_variance: 0.0
      episode_level_advantage_magnitude_cv: 0.0
      success_episodes_all_positive_pct: 0.98
      failure_episodes_all_negative_pct: 0.96
      good_window_in_failure_negative_pct: 0.94
      bad_window_in_success_positive_pct: 0.95
      n_episodes_analyzed: 128
      n_windows_analyzed: 1536
    result_rationale: >
      Sign misattribution 的 correlation 结构由 RAGEN 的 step_independent 实现直接决定。
      代码路径 agent_trainer.py:271-340 中，每个 window 的 return 由
      compute_step_discounted_returns() 计算：return_w = Σ_{t=w}^{T} γ^(t-w) * r_t。
      由于 ALFWorld 是 sparse binary reward（只有 episode 最后一步有 +10 或 0），
      所有 window 的 return 只取决于 episode 是否成功。成功 episode：return_w = γ^(T-w) * 10
      > 0（所有 window 正），失败 episode：return_w = 0（经 GRPO group normalization 后
      变为负 advantage）。因此 advantage sign 与 episode outcome 的 correlation 接近 1.0
      （0.97 而非 1.0 是因为 GRPO normalization 中偶有 group 全成功或全失败的 edge case）。
      Sign 与 local action quality 的 correlation 接近 0（0.04）是因为 advantage sign
      完全由 episode outcome 决定，与 window 内 action 质量无关——好 window 坏 window
      在同一 episode 内获得相同符号的 advantage。γ^k decay 的 R²=0.92 反映 magnitude
      随 window 位置的指数衰减（早期 window 信号更弱）。Episode-level 模式下所有 token
      共享一个 advantage（sign variance = 0, magnitude CV = 0），没有 position-dependent
      distortion。
    tables:
      - title: "Advantage sign analysis: step-independent (h=2) vs episode-level"
        columns: ["metric", "step_independent_h2", "episode_level"]
        rows:
          - ["sign-outcome correlation", 0.97, "N/A (single advantage)"]
          - ["sign-local_quality correlation", 0.04, "N/A"]
          - ["γ^k magnitude decay R²", 0.92, "N/A (no decay)"]
          - ["advantage sign variance (within episode)", 0.0, 0.0]
          - ["% success eps with all-positive windows", "98%", "100%"]
          - ["% failure eps with all-negative windows", "96%", "100%"]
      - title: "Window-level advantage examples (2 success + 2 failure episodes)"
        columns: ["episode", "outcome", "window", "advantage", "local_quality_proxy"]
        rows:
          - ["ep_001", "success", "w1 (earliest)", "+0.31", "low (exploration)"]
          - ["ep_001", "success", "w6 (goal action)", "+2.47", "high"]
          - ["ep_001", "success", "w12 (terminal)", "+7.89", "medium"]
          - ["ep_042", "failure", "w1", "-0.28", "high (good start)"]
          - ["ep_042", "failure", "w5", "-1.93", "low (wrong room)"]
          - ["ep_042", "failure", "w10", "-6.52", "medium"]
    figures_description:
      - "Fig 2a (paper Figure 2 left): Scatter plot — advantage sign (y=+1/-1) vs episode outcome (x=success/failure)，颜色编码 local action quality。几乎完美的 sign-outcome alignment，且 high/low quality points 混合分布在每侧（证明 sign 与 quality 无关）。"
      - "Fig 2b (paper Figure 2 right): Advantage magnitude vs window position (in success episodes)，展示 γ^k 指数衰减拟合线（R²=0.92）。"
      - "Fig 2c: Episode-level control — 所有 token 的 advantage 值相同（水平线），无 position/sign variation。"
    analysis: >
      这是 paper 的理论核心 figure。三个 panel 分别证明：(a) advantage sign 由 episode
      outcome 决定（sign misattribution，r=0.97），(b) magnitude 按 γ^k 衰减
      （information loss 的辅助效应，R²=0.92），(c) episode-level 完全消除两者。
      Sign misattribution 是 "方向错误"（好 action 被惩罚、坏 action 被奖励），
      比 magnitude decay（"信号弱"）更致命——这解释了为什么 h=2 catastrophically
      collapses 而非只是 "学得慢"。

  # ============================================================
  # Phase B: Selective Verification
  # ============================================================

  - name: "Action-change statistics from always-on runs"
    plan_id: "plan_005"
    description: >
      从 exp029 converged checkpoint 收集 always-on verification 的 action-change 统计。
    expected_results:
      confirmatory_rate: 0.72
      action_change_rate: 0.28
      action_change_success_correlation: 0.35
      per_task_action_change_rate_pick: 0.22
      per_task_action_change_rate_clean: 0.31
      per_task_action_change_rate_heat: 0.30
      per_task_action_change_rate_cool: 0.27
      per_task_action_change_rate_examine: 0.25
      per_task_action_change_rate_pick_two: 0.35
      mean_verifications_per_episode: 18.5
      mean_action_changes_per_episode: 5.2
      action_change_at_critical_steps_rate: 0.48
      n_episodes: 256
    result_rationale: >
      72% confirmatory rate 反映 trained agent 的 policy 已经较为 deterministic——大部分
      时候 verification 后 agent 选择相同动作，说明 verification 并未提供新信息。28% 的
      action change 集中在两类 step：(1) 关键决策点（如选择去哪个房间、选择哪个容器），
      这些 step 的 policy entropy 较高；(2) 纠错点（前一步执行了无效动作后需要修正策略）。
      Action change 与 success 的正相关（r=0.35）表明 verification 触发的改变倾向于
      改善决策——成功 episode 中更多的 action change 意味着 agent 在关键点做出了修正。
      pick_two 任务的 action_change_rate 最高（0.35）因为它需要更多分支决策（选两个物品
      的顺序和位置），每个决策点的 uncertainty 更高。
    tables:
      - title: "Action-change statistics breakdown"
        columns: ["task_type", "episodes", "confirmatory_rate", "action_change_rate", "success_with_change", "success_without_change"]
        rows:
          - ["pick", 85, 0.78, 0.22, 0.52, 0.45]
          - ["clean", 52, 0.69, 0.31, 0.50, 0.38]
          - ["heat", 38, 0.70, 0.30, 0.48, 0.40]
          - ["cool", 30, 0.73, 0.27, 0.53, 0.43]
          - ["examine", 21, 0.75, 0.25, 0.47, 0.42]
          - ["pick_two", 30, 0.65, 0.35, 0.44, 0.33]
          - ["overall", 256, 0.72, 0.28, 0.49, 0.41]
    figures_description:
      - "Fig: Per-step action-change probability heatmap across episode progression (x=normalized step position 0-1, y=task type)。显示 action change 集中在 episode 中期（探索→执行转折点）。"
    analysis: >
      72% confirmatory rate 直接支持 selective verification 的 motivation：大部分
      verification 是浪费计算资源的。同时 r=0.35 的 positive correlation 说明 action
      change 不是随机噪声——它携带关于 episode 成功的预测信息，为 action-change-based
      reward 提供了 grounding。

  - name: "Selective verification implementation"
    plan_id: "plan_006"
    description: >
      RAGEN 框架中实现 binary verify/skip decision。纯代码实现，无 GPU 结果。
    expected_results:
      implementation_complete: true
      special_tokens_added: ["&lt;verify>", "&lt;skip>"]
      reward_formula: "R = task_success + α * action_change_when_verified - β * verification_cost"
      alpha: 0.5
      beta: 0.1
      code_changes_files: 4
      unit_tests_passing: true
    result_rationale: >
      实现层面是 engineering work，best 档下顺利完成。关键设计决策：(1) 在每个 step 的
      action output 前插入 verify/skip special token（最小化对现有 pipeline 的侵入）；
      (2) α=0.5 和 β=0.1 的初始值基于 plan_005 的 action-change statistics（action
      change 约 28% 的时间发生，verification cost 需要足够低以允许 ~40-60% verification
      rate）；(3) 当 agent 选择 verify 但未 change action 时，reward 减少 β（惩罚
      无信息的 verification）；当 agent 选择 verify 且 changed action 时，reward 增加
      α（奖励信息性 verification）。
    tables: []
    figures_description: []
    analysis: >
      纯实现步骤，为 plan_007 训练做准备。

  - name: "B-IAVR selective verification training"
    plan_id: "plan_007"
    description: >
      从 exp029 best checkpoint 初始化，用 action-change reward 训练 selective
      verification policy。Episode-level GRPO。
    expected_results:
      converged_val_success: 0.46
      converged_verification_rate: 0.42
      verification_rate_reduction_vs_always_on: 0.58
      success_delta_vs_always_on_pp: -2.0
      converged_action_change_when_verified: 0.52
      converged_skip_accuracy: 0.88
      convergence_step: 30
      training_hours: 36
      cost_reduction_total_tokens: 0.52
    result_rationale: >
      B-IAVR 收敛到 42% verification rate（58% reduction）且 success 仅降 2pp（46% vs
      48% always-on），原因：(1) 从 converged checkpoint 初始化意味着 agent 已有强 policy
      base，只需学习 verify/skip 决策（低维问题，收敛快）；(2) Action-change reward 有效
      引导 agent 识别 "高 uncertainty 步骤" 和 "低 uncertainty 步骤"——agent 学会在
      policy entropy 高的 decision point（如选择房间）verify，在 routine step（如
      "go to countertop"）skip；(3) 42% verification rate 意味着 agent 平均每 episode
      verify ~7.8 次 (18.5 * 0.42)，跳过 ~10.7 次。被跳过的 step 中 88% 确实是
      confirmatory 的（skip_accuracy=0.88），说明 agent 精确识别了不需要 verification 的
      step；(4) 2pp 的 success drop 来自少数 false skip——agent 在个别关键 decision point
      错误地 skip 了 verification，导致错误决策未被纠正。这个 trade-off 在 cost-efficiency
      角度是有利的。
    tables:
      - title: "B-IAVR training trajectory"
        columns: ["step", "success", "verification_rate", "action_change_when_verified", "skip_accuracy"]
        rows:
          - [0, 0.48, 1.00, 0.28, "N/A"]
          - [5, 0.47, 0.72, 0.35, 0.75]
          - [10, 0.46, 0.58, 0.42, 0.82]
          - [20, 0.46, 0.45, 0.50, 0.86]
          - [30, 0.46, 0.42, 0.52, 0.88]
    figures_description:
      - "Fig: Dual-axis training curve — success rate (left y) 基本水平，verification rate (right y) 从 100%→42% 逐步下降。"
    analysis: >
      58% verification reduction 在 best 档指标范围 [40%, 65%] 的上部。关键：agent 学会了
      选择性 verify——action_change_when_verified 从 0.28 (always-on) 提升到 0.52
      （selective），说明 agent 确实在选择 informative step 做 verify。

  - name: "Selective verification full comparison"
    plan_id: "plan_008"
    description: >
      同一 val set 上对比 always-on / B-IAVR / no-verify / random-p / confidence-threshold。
    expected_results:
      always_on_success: 0.48
      always_on_verification_rate: 1.00
      always_on_total_tokens: 1.00
      biavr_success: 0.46
      biavr_verification_rate: 0.42
      biavr_total_tokens: 0.52
      no_verify_success: 0.36
      no_verify_verification_rate: 0.00
      no_verify_total_tokens: 0.38
      random_p40_success: 0.41
      random_p40_verification_rate: 0.40
      random_p40_total_tokens: 0.55
      confidence_threshold_success: 0.43
      confidence_threshold_verification_rate: 0.45
      confidence_threshold_total_tokens: 0.58
      biavr_pareto_dominant: true
    result_rationale: >
      B-IAVR 在 Pareto frontier 上 dominant 的原因：(1) vs always-on：仅 -2pp success
      但节省 48% tokens，efficiency 远高；(2) vs no-verify：+10pp success 因为 selective
      verification 在关键 step 纠正了错误；(3) vs random-p（以 40% probability 随机
      verify）：+5pp success at comparable verification rate，因为 random 浪费 verify 在
      不需要的 step 且错过关键 step；(4) vs confidence-threshold（基于 logit entropy
      决定是否 verify）：+3pp success at lower verification rate，因为 model 的 token-level
      confidence 不完全反映 decision-level uncertainty（一个 confident-looking action
      可能在 trajectory-level 是错误的，confidence 无法捕捉这种 temporal credit structure，
      而 B-IAVR 通过 RL 学到了 trajectory-aware 的 verify 策略）。
    tables:
      - title: "Selective verification comparison (same val set, 128 episodes)"
        columns: ["method", "success_rate", "verification_rate", "relative_tokens", "success_per_token"]
        rows:
          - ["always-on", 0.48, 1.00, 1.00, 0.48]
          - ["B-IAVR (ours)", 0.46, 0.42, 0.52, 0.88]
          - ["confidence-threshold", 0.43, 0.45, 0.58, 0.74]
          - ["random-p=0.4", 0.41, 0.40, 0.55, 0.75]
          - ["no-verify", 0.36, 0.00, 0.38, 0.95]
    figures_description:
      - "Fig (paper Figure 4): Pareto frontier plot — x=relative inference cost, y=success rate。B-IAVR 在 frontier 的最优位置（highest success at given cost）。"
      - "Fig: Per-task breakdown bar chart — 6 task types × 5 methods。"
    analysis: >
      B-IAVR 的 success-per-token ratio (0.88) 是所有方法中最高的（always-on=0.48，
      说明 always-on 一半以上的 verification 是浪费的）。这是 Claim 3 的核心证据。

  # ============================================================
  # Phase C: Ablations & Causal Analysis
  # ============================================================

  - name: "No-verify ablation"
    plan_id: "plan_009"
    description: >
      Episode-level GRPO 训练但完全移除 self-verification。Verification 价值的 lower bound。
    expected_results:
      converged_val_success: 0.36
      converged_action_is_valid: 0.65
      success_drop_vs_always_on_pp: 12.0
      convergence_step: 40
    result_rationale: >
      移除 verification 后 success 降 12pp（48%→36%）反映了 verification 在 ALFWorld 中
      的两个作用：(1) 错误纠正——agent 在某些 step 选择了错误动作（如 go to wrong room），
      verification 提供了 second chance 来修正。没有 verification，这些错误直接导致 episode
      失败。(2) 信息获取——verification 过程中 agent 重新审视 observation，有时发现之前
      忽略的信息（如 "there is a cup on the shelf" 被遗漏）。12pp 的 drop 在 best 档
      预期内（≥10pp），足以证明 verification 有价值。同时 36% 的 success 说明 episode-level
      policy 本身已经很强——verification 是 incremental improvement 而非必需品。
      Action_is_valid 下降（72%→65%）因为 verification 提供的 error feedback 在某些 case
      帮助 model 避免后续的 invalid action。
    tables:
      - title: "Verification ablation impact"
        columns: ["config", "success", "action_is_valid", "avg_steps_to_success"]
        rows:
          - ["always-on verification", 0.48, 0.72, 18.3]
          - ["no verification", 0.36, 0.65, 16.8]
          - ["delta", "-12pp", "-7pp", "-1.5 steps"]
    figures_description: []
    analysis: >
      12pp gap 证明 verification 有价值，但 36% 无验证的 success 也说明 episode-level
      training 本身学到了 strong policy。这支持 "verification 是 optional optimization,
      not critical requirement" 的定位，让 selective verification 的 framing 更合理——
      我们不是 "必须 verify 才能 work"，而是 "verify 有帮助，如何只在有帮助时 verify"。

  - name: "Entropy-controlled action-change analysis"
    plan_id: "plan_010"
    description: >
      控制 policy entropy 后检验 action-change 与 success 的偏相关。
      回应 "action change = noise" 审稿攻击。
    expected_results:
      raw_correlation: 0.35
      partial_correlation_controlling_entropy: 0.28
      partial_correlation_p_value: 0.003
      n_episodes: 256
      entropy_strata: 4
      correlation_by_stratum_low: 0.25
      correlation_by_stratum_mid_low: 0.30
      correlation_by_stratum_mid_high: 0.29
      correlation_by_stratum_high: 0.26
    result_rationale: >
      控制 entropy 后 partial correlation 仍显著（0.28, p=0.003）证明 action change 不仅仅
      是 policy uncertainty 的 proxy。机制：高 entropy step 确实更可能 change action（因为
      policy 不确定），但 action change 的信息价值超越了 uncertainty 本身——verification
      触发的 change 反映了 agent 在 re-examination 后发现了 initial decision 的错误，
      这种 "informed correction" 与 success 的相关性在所有 entropy 层级中都存在。
      四个 entropy stratum 的 correlation 相对稳定（0.25-0.30），说明 action-change-success
      relationship 是 robust 的，不是被高 entropy bin 驱动的 artifact。
    tables:
      - title: "Entropy-stratified action-change analysis"
        columns: ["entropy_stratum", "n_steps", "action_change_rate", "correlation_with_success", "p_value"]
        rows:
          - ["low (0-0.1)", 420, 0.15, 0.25, 0.02]
          - ["mid-low (0.1-0.3)", 380, 0.25, 0.30, 0.008]
          - ["mid-high (0.3-0.6)", 410, 0.35, 0.29, 0.005]
          - ["high (0.6+)", 326, 0.45, 0.26, 0.01]
          - ["overall (partial)", 1536, 0.28, 0.28, 0.003]
    figures_description:
      - "Fig: 4-panel scatter plots (one per entropy stratum) showing action-change rate vs episode success，with partial correlation annotation。"
    analysis: >
      Partial correlation 0.28 (p=0.003) 在 best 档下充分回应 "action change = noise"
      攻击。Stratum-level stability 是额外的 robustness 证据。

  - name: "Causal intervention: random vs verification-triggered changes"
    plan_id: "plan_011"
    description: >
      以相同 rate 注入 random action changes，对比 verification-triggered changes 的
      task success。因果推断证据。
    expected_results:
      success_rate_verification_triggered: 0.48
      success_rate_random_change: 0.33
      success_rate_no_change: 0.36
      delta_triggered_vs_random_pp: 15.0
      delta_triggered_vs_no_change_pp: 12.0
      n_episodes_per_condition: 128
      p_value_triggered_vs_random: 0.001
    result_rationale: >
      Verification-triggered changes 显著优于 random changes（+15pp），证明 verification
      过程 genuinely 帮助 agent 做出更好的决策（因果效应），而不仅仅是 "任何 change 都有
      帮助"。Random changes 反而比 no-change 略差（33% vs 36%），因为随机改变一个已经
      合理的决策会导致更多错误。Verification-triggered changes 只在 agent 认为当前决策
      有误时才发生（28% 的 step），且这些改变指向更正确的方向——这是 trained policy 的
      verification 过程提供了 informed error correction，而非 random perturbation。
      15pp 的 delta 是强因果证据，p<0.001。
    tables:
      - title: "Causal intervention comparison"
        columns: ["condition", "success", "action_change_rate", "p_value_vs_triggered"]
        rows:
          - ["verification-triggered", 0.48, 0.28, "—"]
          - ["random (matched rate)", 0.33, 0.28, 0.001]
          - ["no change baseline", 0.36, 0.00, "<0.001"]
    figures_description:
      - "Fig: Bar chart with significance markers (***, p<0.001) 展示三个条件的 success rate。"
    analysis: >
      15pp delta 是 Claim 2 的因果证据支柱。Verification-triggered > no-change > random
      的排序说明 (a) verification 有值，(b) informed change 远优于 uninformed change。

  - name: "Reward signal ablation (action-change vs alternatives)"
    plan_id: "plan_012"
    description: >
      B-IAVR 用三种 reward 训练对比：action-change / random-trigger / confidence-based。
    expected_results:
      action_change_success: 0.46
      action_change_verification_rate: 0.42
      action_change_cost_reduction: 0.52
      random_trigger_success: 0.40
      random_trigger_verification_rate: 0.55
      random_trigger_cost_reduction: 0.38
      confidence_success: 0.43
      confidence_verification_rate: 0.50
      confidence_cost_reduction: 0.42
    result_rationale: >
      Action-change reward 最优因为它直接衡量 verification 的 informativeness（是否改变了
      决策）。Random-trigger reward（随机时机给 reward）无法引导 agent 学习 when to verify
      的有用 pattern，导致 verification rate 高（55%，不知道何时 skip）且 success 低
      （40%，浪费 verification 在无用 step）。Confidence-based reward（基于 logit entropy
      决定 verify 价值）性能居中——它能捕捉 token-level uncertainty 但错过 trajectory-level
      的 verification 需求（如一个 confident 但在 trajectory context 中错误的 action）。
      Action-change 的优势在于它是 outcome-informed 的 signal（verification 是否 actually
      改变了行为），而非 proxy signal（uncertainty/randomness）。
    tables:
      - title: "Reward signal ablation"
        columns: ["reward_type", "success", "verif_rate", "cost_reduction", "pareto_efficient"]
        rows:
          - ["action-change (ours)", 0.46, 0.42, 0.52, "Yes"]
          - ["confidence-based", 0.43, 0.50, 0.42, "No"]
          - ["random-trigger", 0.40, 0.55, 0.38, "No"]
    figures_description:
      - "Fig: Pareto frontier plot comparing 3 reward variants, action-change dominates。"
    analysis: >
      Action-change reward 在 success 和 cost reduction 两个维度上都最优，
      验证了 action change 作为 verification informativeness signal 的有效性。

  - name: "ARES reproduction + comparison"
    plan_id: "plan_013"
    description: >
      复现 ARES SFT router on ALFWorld（same model），与 B-IAVR head-to-head 对比。
    expected_results:
      ares_success: 0.44
      ares_verification_rate: 0.55
      ares_cost_reduction: 0.38
      biavr_success: 0.46
      biavr_verification_rate: 0.42
      biavr_cost_reduction: 0.52
      biavr_vs_ares_cost_reduction_delta_pp: 14.0
      biavr_vs_ares_success_delta_pp: 2.0
    result_rationale: >
      B-IAVR 在 cost reduction 上超越 ARES 14pp（52% vs 38%）且 success 略高（+2pp）。
      ARES 使用 SFT-trained router（supervision 来自 heuristic labels），存在两个限制：
      (1) SFT label quality ceiling——heuristic 标注的 verify/skip decision 不一定最优，
      router 只能学到 heuristic 的水平；(2) 无 exploration——SFT 是 imitation learning，
      router 无法发现 heuristic 未覆盖的 verification pattern。B-IAVR 用 RL 训练
      （action-change reward），agent 通过 exploration 发现比 heuristic 更精准的
      verification timing。另外 ARES 的 continuous effort 设计（连续 effort 值而非 binary
      verify/skip）在 ALFWorld 的 binary decision 结构下未必优于简洁的 binary approach。
      ARES 的 verification_rate=55% 高于 B-IAVR 的 42%，说明 ARES router 更保守（不确定
      时倾向 verify），这牺牲了 cost efficiency。
    tables:
      - title: "B-IAVR vs ARES comparison (same model, same val set)"
        columns: ["method", "success", "verif_rate", "cost_reduction", "training_method"]
        rows:
          - ["B-IAVR (ours)", 0.46, 0.42, 0.52, "RL (action-change reward)"]
          - ["ARES (reproduced)", 0.44, 0.55, 0.38, "SFT (heuristic labels)"]
          - ["delta", "+2pp", "-13pp", "+14pp", "—"]
    figures_description:
      - "Fig: Head-to-head Pareto plot with ARES and B-IAVR on same axes。"
    analysis: >
      14pp cost reduction 优势直接回应 "ARES differentiation" 审稿攻击。核心差异化：
      RL > SFT for learning verification policy（RL 可 explore optimal timing, SFT 被
      heuristic label quality 限制）。

  # ============================================================
  # Phase D: Scaling & Generalization
  # ============================================================

  - name: "ScienceWorld transfer (episode-level advantage)"
    plan_id: "plan_014"
    description: >
      ScienceWorld 环境上验证 episode-level vs step-independent。不同环境，类似多轮结构。
    expected_results:
      episode_level_success: 0.32
      step_independent_h2_success: 0.04
      step_independent_h10_success: 0.11
      episode_vs_step_h2_ratio: 8.0
      episode_vs_step_h10_ratio: 2.9
      episode_vs_step_independent_mean_ratio: 3.2
      scienceworld_task_diversity: 10
      episode_convergence_step: 20
    result_rationale: >
      ScienceWorld 的 episode-level 优势比率 3.2x（32% vs 10% step-independent 均值）在
      best 档范围 [2x, 4x] 内。ScienceWorld 与 ALFWorld 共享关键结构特征：(1) 多轮交互
      （平均 ~30 steps），(2) sparse binary reward（任务完成/未完成），(3) 需要跨步策略
      规划（如 science 实验需要按顺序操作多个 object）。这些结构特征正是 sign misattribution
      和 information loss 的触发条件。因此 episode-level 的优势可以 transfer。
      绝对 success 低于 ALFWorld（32% vs 48%）因为 ScienceWorld 任务更复杂（需要
      domain-specific knowledge，如化学反应、物理实验步骤），但 relative advantage
      （3.2x ratio）甚至高于 ALFWorld，因为 ScienceWorld 的 longer horizon（~30 steps
      vs ~25 steps）使 sign misattribution 更严重（更多 window，每个 window 的 sign
      偏差对训练的干扰更大）。Step-independent h=2 几乎完全 collapse（4%），h=10 也仅
      11%，验证了 cliff 现象在新环境中的 generalizability。
    tables:
      - title: "ScienceWorld: Episode-level vs Step-independent"
        columns: ["method", "success", "convergence_step", "collapse?"]
        rows:
          - ["episode-level", 0.32, 20, "No"]
          - ["step-independent (h=2)", 0.04, "N/A", "Yes (step 5)"]
          - ["step-independent (h=10)", 0.11, "N/A", "Partial"]
    figures_description:
      - "Fig: ALFWorld vs ScienceWorld side-by-side bar charts，展示 episode-level advantage 在两个环境中的一致性。"
    analysis: >
      Cross-environment transfer 是回应 "single environment" 审稿攻击的关键证据。
      3.2x ratio 证明 dual mechanism 不是 ALFWorld-specific artifact，而是 sparse-reward
      multi-turn 任务的通用问题。

  - name: "7B model scaling verification"
    plan_id: "plan_015"
    description: >
      Qwen3-7B 上验证 episode-level vs step-independent。回应 model size concern。
    expected_results:
      episode_level_7B_success: 0.58
      step_independent_h2_7B_success: 0.08
      step_independent_h10_7B_success: 0.22
      episode_vs_step_ratio_7B: 3.6
      episode_7B_vs_1_7B_improvement_pp: 10.0
      step_independent_7B_vs_1_7B_improvement_pp: 6.0
      convergence_step_7B: 30
    result_rationale: >
      7B model 在两个 regime 下都更强（episode-level 58% vs 1.7B 48%；step-independent
      h=10 22% vs 1.7B 18%），但 episode-level 的 relative advantage 更大（3.6x vs 3.0x
      at 1.7B, comparing h=10）。原因：(1) 7B 的更强 base capability 意味着 policy 有更多
      "正确策略" 可学，但 sign misattribution 仍然阻止 step-independent 学到它们——
      更强的 model 反而让 misattribution 的 "浪费" 更显著；(2) 7B 的更长 context window
      利用能力使 episode-level training 的优势更大（1.7B 可能在 full context 下也有信息
      处理限制，7B 更充分利用全 episode 信息）。Step-independent 在 7B 下表现略好于 1.7B
      但仍远不及 episode-level，说明 model scaling alone 不能解决 sign misattribution——
      这支持 "问题在 training methodology 而非 model capacity" 的 framing。
    tables:
      - title: "7B vs 1.7B scaling comparison"
        columns: ["method", "1.7B success", "7B success", "scaling gain"]
        rows:
          - ["episode-level", 0.48, 0.58, "+10pp"]
          - ["step-independent (h=10)", 0.18, 0.22, "+4pp"]
          - ["step-independent (h=2)", 0.02, 0.08, "+6pp"]
          - ["episode/step ratio", "2.7x", "3.6x", "ratio increases"]
    figures_description:
      - "Fig: Grouped bar chart — 1.7B vs 7B × episode/step-independent。"
    analysis: >
      7B 实验的核心贡献不是追求 SOTA performance（58% 仍低于 GAGPO 93.5%），而是证明
      episode-level advantage 随 model scale 增大而增强——larger model 更需要正确的
      training methodology。这预测了在更大 model（70B+）上 episode-level 的优势会更明显。

  - name: "Per-task-type breakdown analysis"
    plan_id: "plan_016"
    description: >
      ALFWorld 6 种 task type 的分类 success 分析。展示 within-environment diversity。
    expected_results:
      pick_episode_success: 0.55
      pick_step_indep_success: 0.08
      clean_episode_success: 0.48
      clean_step_indep_success: 0.03
      heat_episode_success: 0.52
      heat_step_indep_success: 0.05
      cool_episode_success: 0.50
      cool_step_indep_success: 0.04
      examine_episode_success: 0.42
      examine_step_indep_success: 0.02
      pick_two_episode_success: 0.38
      pick_two_step_indep_success: 0.01
      episode_length_success_correlation: -0.82
      longer_tasks_benefit_more: true
    result_rationale: >
      Episode-level advantage 在所有 task type 上一致存在，但更长、更复杂的任务获益更多。
      Pick（最简单，~15 步）的 episode-level success 最高（55%）因为策略最直接（find
      object → pick → put），step-independent 也能偶尔成功（8%）。Pick_two（最复杂，
      ~35 步）的 episode-level success 最低（38%）因为需要两轮 find-pick-put 的跨步
      协调，但 step-independent 几乎完全 collapse（1%）。Episode-length 与 success 的
      负相关（r=-0.82）反映了 ALFWorld 的 task complexity gradient。关键观察：
      episode-level 的 advantage ratio（episode/step-independent）随 task length 增加：
      pick=6.9x, clean=16x, heat=10.4x, cool=12.5x, examine=21x, pick_two=38x。
      这是因为更长的 task 有更多的 sign-misattributed window，累积的梯度方向错误更严重。
    tables:
      - title: "Per-task-type breakdown"
        columns: ["task", "avg_steps", "episode_success", "step_indep_success", "advantage_ratio"]
        rows:
          - ["pick", 15, 0.55, 0.08, "6.9x"]
          - ["clean", 22, 0.48, 0.03, "16x"]
          - ["heat", 20, 0.52, 0.05, "10.4x"]
          - ["cool", 20, 0.50, 0.04, "12.5x"]
          - ["examine", 28, 0.42, 0.02, "21x"]
          - ["pick_two", 35, 0.38, 0.01, "38x"]
    figures_description:
      - "Fig: Grouped bar chart per task type (episode vs step-independent)，按 task length 排序。"
      - "Fig: Scatter plot — average episode length vs advantage ratio，展示 length-advantage 正相关。"
    analysis: >
      Per-task breakdown 提供了 dual mechanism theory 的 additional support：advantage
      ratio 随 task length monotonically 增加，consistent with 更多 window → 更多
      sign misattribution → 更大的 catastrophic effect。这也回应了 "ALFWorld 多样性
      不足" 的 concern——6 个 task type 在 complexity 和 strategy 上有显著差异，
      episode-level advantage 在全部 type 上都成立。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "48c34c69-072a-4ccc-a5ed-3ad4cfce6b2b",
  "isSidechain": false,
  "requestId": "req_011Cb8E4rXey2yosgsPvb6uM",
  "type": "assistant",
  "uuid": "67a29934-38cb-42c7-817a-9f635d7ca1ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1",
  "sessionId": "76d61b9e-2e1c-4565-b8a8-d68d26d41235",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014j9MsGdMguX6UpRxZZyacL",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12520,
      "cache_read_input_tokens": 33702,
      "output_tokens": 18558,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12520,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 18558,
          "cache_read_input_tokens": 33702,
          "cache_creation_input_tokens": 12520,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12520
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

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Episode-level 训练收敛到强 performance，双机制理论完整验证，selective verification 可行，contrarian positioning 成立 核心假设：['Episode-level GRPO 收敛至 ≥45% val success（pass@1），打破当前…",
  "leafUuid": "67a29934-38cb-42c7-817a-9f635d7ca1ca",
  "sessionId": "76d61b9e-2e1c-4565-b8a8-d68d26d41235"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Episode-level RL for multi-turn agent training",
  "sessionId": "76d61b9e-2e1c-4565-b8a8-d68d26d41235"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Episode-level 训练收敛到强 performance，双机制理论完整验证，selective verification 可行，contrarian positioning 成立 核心假设：['Episode-level GRPO 收敛至 ≥45% val success（pass@1），打破当前…",
  "leafUuid": "67a29934-38cb-42c7-817a-9f635d7ca1ca",
  "sessionId": "76d61b9e-2e1c-4565-b8a8-d68d26d41235"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Episode-level RL for multi-turn agent training",
  "sessionId": "76d61b9e-2e1c-4565-b8a8-d68d26d41235"
}
```

---
