# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：Episode-level 训练有效但 performance 中等，双机制理论部分验证，selective verification 未完成或效果

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/3f91a417-7d76-4bf5-9691-eb7dd278d753.jsonl`
- **Structured JSON:** [`3b9648410a7cadbf2fb1.json`](../../sessions/3b/3b9648410a7cadbf2fb1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-17T13:39:25.749Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-17T13:39:25.749Z",
  "sessionId": "3f91a417-7d76-4bf5-9691-eb7dd278d753",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：Episode-level 训练有效但 performance 中等，双机制理论部分验证，selective verification 未完成或效果弱，paper 收缩为 diagnostic contribution\n核心假设：['Episode-level GRPO 收敛至 30-40% val success，足以证明优于 step-independent 但不足以支撑 cost-efficiency story', 'h-sweep cliff 存在但 sharpness 因 seed 而异（2/3 seeds 清晰，1 seed 模糊）', 'Sign misattribution 实证部分验证：sign-vs-outcome correlation 0.80-0.95（存在但非完美）', 'GAE baseline 优于 episode-level GRPO 5-12pp，削弱 contrarian positioning（finer credit 确实有价值）', 'Multi-seed std 5-8pp，reproducibility 可接受但不完美', 'Selective verification 未完成（时间/资源不足）或效果弱（verification reduction <30%）', 'ScienceWorld transfer 未执行或结果不明确']\n关键指标范围：{'episode_level_val_success_converged': [0.3, 0.44], 'step_independent_h2_val_success': [0.0, 0.08], 'h_sweep_cliff_threshold': [5, 10], 'sign_vs_outcome_correlation': [0.8, 0.94], 'sign_vs_local_quality_correlation': [0.05, 0.2], 'gamma_k_magnitude_decay_r2': [0.6, 0.84], 'multi_seed_mean_success': [0.28, 0.42], 'multi_seed_std': [0.05, 0.08], 'gae_vs_episode_level_delta_pp': [5, 12], 'selective_verification_rate_reduction': [0.15, 0.35], 'selective_success_delta_vs_always_on_pp': [3, 8], 'scienceworld_episode_vs_step_ratio': [1.2, 2.0]}\n叙事方向：Paper 收缩为 Plan A 方向：diagnostic + analysis contribution。标题变为 \"Why Step-Independent RL Fails for LLM Multi-Turn Agents: Dual Mechanism Analysis\"。 Claim 1 保留但调整措辞：sign misattribution 是 \"dominant factor\" 而非 \"complete explanation\"， 因为 correlation 未达 0.95。GAE 优势需正面讨论：承认 finer credit 在 performance 上有额外价值， 但 reframe 为 \"episode-level 是 necessary minimum（消除 sign misattribution）， GAE 是 sufficient improvement（加 per-token credit）\"，不再强推 contrarian \"更粗就够了\"。 Selective verification（Claim 2/3）降为 preliminary results 或 future work。 h-sweep 和多 seed 机制分析需做得更深（community practice survey, 更多 ablation）来补偿 selective verification 贡献的缺失。仍可投同 venue 但作为 analysis paper track。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: cost-verify-agent-rl\nfocus: Post-novelty-check framing with updated competitive positioning: sign misattribution as deeper mechanistic characterization (not just \"uniform advantage\"), P(correct|update) quantification, dual mechanism separation, contrarian episode-level solution. Evaluate with updated experiment plan including γ-sweep, K-sweep, ScienceWorld transfer. Key question: does the contrarian positioning hold against Turn-PPO/GAGPO/HiPER competitors?\n\n## paper_framing.md\n\n# Paper Framing — Learning When to Verify: RL-Trained Selective Self-Verification for Interactive Agents\n\n> Post-MVP 重写 (2026-05-17) | D054 framing pivot + Dream Review feedback (weak reject → 修正理论)\n\n## Core Insight\n\nMulti-turn interactive agents 的 self-verification 大部分是 confirmatory（不改变行为）而非 corrective。训练 agent 学 selective verification 的前提是 RL 训练本身能 work。我们发现 LLM agent 社区默认的 step-independent training 在长 horizon 任务中灾难性崩溃，根因是**双机制失效**：\n\n1. **Policy Information Loss**: 短窗口（h 步）的 policy 无法学习跨步策略（如 \"先探索 drawer 再去 countertop\"）\n2. **Advantage Sign Misattribution**: step_independent 中，per-window advantage 的**符号**由 episode 成败决定，而非 window-local action quality：\n   - 失败 episode 中的好 action → 获得负 advantage（被错误惩罚）\n   - 成功 episode 中的差 action → 获得正 advantage（被错误强化）\n   - 梯度方向（reinforce/suppress）反映 episode outcome 而非 local decision quality\n   - 附加：γ^k magnitude decay 使早期 window 信号更弱（γ^24 ≈ 29%, where 24 = ⌈T/h⌉-1 windows），但方向错误比幅度衰减更致命\n\nEpisode-level training 同时解决两者：policy 看全历史（解决 1），整条 trajectory 作为一个 GRPO 样本，所有 tokens 共享同一 advantage — 虽然仍是 episode-level credit（非 per-token），但消除了 window 间的 sign misattribution，因为不再需要将 episode reward 分配到独立优化的子窗口（解决 2）。\n\n**技术澄清**：GRPO 算法本身是 bandit-style（advantage = (R-μ)/σ，无显式 γ），但 RAGEN 的 step_independent 实现在 `compute_step_discounted_returns()` 中引入 γ 计算每个 window 的 return（代码：`agent_trainer.py:271-340`）。γ^(T-t) decay 对 step_independent 模式是代码事实，不是类比。Episode-level 模式下无此问题：整条 trajectory 只有一个 return = episode_reward。\n\n## Story Arc\n\n**Dual contribution**: Training methodology diagnosis + Selective verification system\n\n叙事线：\n1. Self-verification 对 interactive agents 有用，但 always-on 成本高\n2. 训练 agent 学 WHEN to verify 需要 RL → 但 LLM agent 社区默认的 step-independent training 在多轮任务上灾难性崩溃（0% at step 10）\n3. 我们诊断双机制根因（information loss + advantage sign misattribution），提出 episode-level GRPO 解决\n4. 分析 \"为什么社区默认走向 step-independent\"（context window 限制 + token-level training 惯性 + framework design accident）\n5. 在 episode-level 基础上，用 action-change 作为 verification informativeness 的 reward，训练 selective policy\n6. 结果：near-always-on performance + 显著降低 verification cost\n\n**定位**：不 claim \"发明了 episode-level RL\"（trivial），而是 \"诊断了 LLM agent RL 训练中被忽视的 step-independent 隐性代价 + 系统分析崩溃机制 + 提出实用修复方案 + 在此基础上实现 selective verification\"\n\n## Target Venue\n\n待定（NeurIPS 2026 / EMNLP 2026 / ICLR 2026），取决于实验进度和最终效果。\n\n## Core Claims\n\n### Claim 1 (strength: strong): Step-independent GRPO catastrophically fails for multi-turn agents due to dual mechanism\n- 所需证据：episode-level vs step-independent 对比（多 seed），h-sweep ablation（3 seeds each），mechanistic analysis（gradient signal measurement），GAE baseline comparison\n- 当前证据状态：**ESTABLISHED** (exp029 step5 val=25% vs exp028c step10 val=0%)\n- 机制：(1) policy information loss (h-step context insufficient), (2) advantage sign misattribution (gradient direction reflects episode outcome, not window-local action quality; additionally γ^k magnitude decay for early windows)\n- 技术细节：GRPO 算法无固有 γ，但 RAGEN step_independent 的 `compute_step_discounted_returns()` 引入 γ-discounted per-window returns → advantage 符号由 episode 成败决定。代码验证：`agent_trainer.py:271-340` + `core_algos.py:194-246`\n\n### Claim 2 (strength: moderate): Action-change is an effective intrinsic reward for verification informativeness\n- 所需证据：selective verification 训练收敛 + action-change vs random/confidence baselines\n- 当前证据状态：**not yet established**，依赖 Phase B 实验\n- 前提：episode-level 训练的 agent 需达到 ≥40% success 才有意义\n\n### Claim 3 (strength: moderate): Learned selective policy matches always-on performance at reduced verification cost\n- 所需证据：B-IAVR verification ↓40%+ 且 success delta < 3pp vs always-on\n- 当前证据状态：**not yet established**，依赖 Phase B + C\n- 前提：Claim 1 的 agent 需足够强\n\n## Contingency Plan\n\n如果 episode-level 训练收敛后 success 仍 < 40%（不足以支撑 cost-efficiency story）：\n- **Plan A**：paper 变为 diagnostic + analysis contribution — \"Why Step-Independent RL Fails for LLM Multi-Turn Agents: Dual Mechanism Analysis\" (需更深 ablation + GAE comparison + community practice survey)\n- **Plan B**：加 Self-Guide reward 到 episode-level（从 binary→dense reward），推高 performance 后再做 selective verification\n- 不考虑 downgrade venue\n- **注意**：Dream review 已证明 Plan A 纯 methodology paper 需要比预期更深的分析才能通过审稿（\"诊断社区默认实践的隐性代价\" > \"episode-level RL works\"）\n\n## Reviewer Attack Surface + Defense\n\n| # | Concern | Severity | Defense |\n|---|---------|----------|---------|\n| 1 | \"Episode-level RL is obvious / well-known\" | HIGH | h-sweep (3 seeds) 展示 non-trivial cliff + 双机制理论 + \"为什么社区默认 step-independent\" 分析 |\n| 2 | \"Theory 与 GRPO 不匹配\" | HIGH | 精确区分：GRPO 算法无 γ，但 step_independent 实现引入 γ-discounted returns（代码引用）→ per-window advantage logging 实证 + 伪代码 |\n| 3 | \"缺 GAE/标准 RL baselines\" | HIGH | 加 GAE(λ=0.95) + GAE(λ=1,γ=1) baseline，证明 episode-level GRPO 与 GAE 的差异 |\n| 4 | \"Self-Guide 3x performance gap\" | HIGH | 正面回应：不同 paradigm (expert-guided vs from-scratch RL)，不同问题（Self-Guide 回避了训练问题） |\n| 5 | Single environment (ALFWorld) | MEDIUM | ScienceWorld transfer (if resources permit) |\n| 6 | Small model (1.7B) | MEDIUM | 定位 resource-constrained; 7B 验证 (conditional) |\n| 7 | Action-change = noise vs signal | MEDIUM | Entropy-controlled analysis + causal intervention (Phase B) |\n| 8 | 与 ARES 差异化不足 | LOW | Head-to-head 对比 + 方法论差异表 |\n| 9 | \"Turn-PPO 已解决相同问题\" | HIGH | 精确区分：Turn-PPO 发现 uniform advantage (subset)，我们发现 sign misattribution (superset + 量化 γ^24≈29%)；解法相反 (finer vs coarser) |\n\n## Evidence Status Matrix\n\n| Claim | MVP Evidence | Research Evidence Needed | Priority |\n|-------|-------------|--------------------------|----------|\n| Claim 1 | exp029 vs exp028c (25% vs 0%) | h-value ablation, multi-seed, mechanism paper figure | P0 |\n| Claim 2 | N/A | Phase B full implementation | P1 |\n| Claim 3 | N/A | Phase B + C comparison suite | P1 |\n\n## Competitive Positioning\n\n| System | Method | Benchmark | Key Difference from Us |\n|--------|--------|-----------|----------------------|\n| Self-Guide (2026) | Always-on verification | ALFWorld 72.7% (1.7B) | We add selectivity via RL |\n| ARES (2603.07915) | SFT router, continuous effort | 52.7% token reduction | SFT vs RL, continuous vs binary |\n| Thinkless (NeurIPS'25) | RL control token | reasoning domain | Same RL philosophy, different domain |\n| ReflAct (EMNLP'25) | Prompting GPT-4 | ALFWorld 93.3% | Different scale/approach |\n| RAGEN (2025) | GRPO for agents | varies | Step-independent default, our baseline |\n| **Turn-PPO (2512.17008)** | Turn-level MDP + value fn | reasoning tasks | \"Uniform advantage\" vs our \"sign misattribution\"; finer credit vs coarser |\n| **GAGPO (2605.13217)** | Grouped value proxy, step-aligned | ALFWorld 93.5% (1.5B) | Finer-grained credit for performance; we diagnose mechanism failure |\n| **MT-GRPO (2505.11821)** | Turn-level reward design | QA search tasks | Turn-level credit; we show coarser suffices |\n| **iStar (ICLR'26)** | Implicit PRM + dual advantage | WebShop 86.5% | Learns step rewards; we show episode-level eliminates misattribution |\n| **ArCHer (ICML'24)** | Hierarchical multi-turn RL | multi-turn agents | Foundational framework; establishes need for hierarchical structure |\n| **HiPER (2602.16165)** | Hierarchical Plan-Execute RL | ALFWorld 97.4% (7B) | SOTA performance pursuit; we do mechanism diagnosis |\n\n### Positioning Strategy\n\n**核心差异化：Contrarian Solution。** 竞品（Turn-PPO, GAGPO, MT-GRPO, iStar, HiPER）一致认为 multi-turn RL 需要更细粒度的 credit assignment（turn-level, step-level, hierarchical），并用此提升性能。我们的贡献是诊断性的：\n\n1. **问题定义更精确**：Turn-PPO 发现 \"uniform advantage\" 问题（所有 turn 获得相同 advantage），我们发现更本质的 \"Advantage Sign Misattribution\"（advantage 符号由 episode outcome 决定而非 local action quality），并量化 γ^24 ≈ 29% 的 return 衰减。Sign misattribution 是 uniform advantage 的超集。\n\n2. **Contrarian solution**：所有竞品的解法都是引入更细的 credit（turn-level value, step-level PRM, hierarchical planner）。我们展示更粗的 episode-level credit 反而消除 sign misattribution，因为它避免了将 episode reward 错误分配到独立优化的子窗口。这挑战了 \"越细越好\" 的社区默认假设。\n\n3. **不同 contribution 维度**：GAGPO/HiPER 追求 ALFWorld 93-97% 的 SOTA performance（通过更好的 credit + 更复杂的架构）。我们不 compete on performance axis，而是回答 \"为什么社区默认的 step-independent 灾难性失败\" 这个诊断问题。两个 contribution 维度正交互补。\n\n4. **与 CA Survey 的关系**：Zhang (2604.09459) 系统化了 47 种 CA 方法，但未分析 CA 方法本身的 failure modes（何时更细粒度反而有害）。我们填补这一空白。\n\n## Research Phases\n\n1. **Phase A (DONE)**: Episode-level GRPO training — MVP passed, demonstrates Claim 1\n2. **Phase A+**: Continue training to convergence (target ≥40% success), deploy tatsu parallel patch, multi-seed\n3. **Phase B**: Implement selective verification with action-change reward — Claim 2 & 3\n4. **Phase C**: Ablation suite — context window sweep, reward ablations, baseline comparisons\n5. **Phase D**: (Conditional on resources) Multi-env / multi-model scaling\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  title: Episode-level GRPO convergence (exp029 continuation)\n  claim: Claim 1\n  phase: A+\n  priority: P0\n  depends_on: []\n  registry_id: exp029_episode_level\n  status: DONE\n  description: 'Episode-level GRPO (context_window_mode: full) on Qwen3-1.7B + ALFWorld.\n    50 steps, dual-GPU. MVP passed at step 5 (val=25%, 2x baseline 12.5%). Continue\n    to convergence (step 20+) with tatsu parallel patch for 4x val speedup.\n\n    '\n  hypothesis: 'Episode-level training enables stable RL for multi-turn agents, reaching\n    ≥40% success by convergence.\n\n    '\n  metrics:\n    current_step: 15\n    total_steps: 100\n    progress_pct: 15\n    step5_val_success: 0.25\n    step10_val_success: 0.25\n    step15_val_success: 0.28125\n    step15_val_pass_at_1: 0.28125\n    step15_val_pass_at_2: 0.469\n    step15_val_pass_at_4: 0.726\n    step15_val_pass_at_8: 0.929\n    step15_val_pass_at_16: 0.996\n    step15_val_action_is_valid: 0.5452\n    step15_val_action_is_effective: 0.7672\n    step15_val_manager_invalid_action: 0.2328\n    step15_train_success: 0.4375\n    step15_train_pass_at_8: 0.75\n    elapsed_hours: 7.35\n    eta_completion: '2026-05-19T03:00:00Z'\n  gpu_hours_estimate: 48\n  framing_ref: claim_1\n  conclusion: success\n- id: plan_002\n  title: Context window h-sweep ablation (3 seeds each)\n  claim: Claim 1\n  phase: A+\n  priority: P0\n  depends_on:\n  - plan_001\n  registry_id: null\n  status: planned\n  description: 'Sweep context_window h={2, 5, 10, 20, full} on same GRPO config. Config:\n    context_window_mode=step_independent + step_independent_history_length={h} (h=full\n    uses context_window_mode=full). 15 steps per run, 3 seeds each. KEY paper figure:\n    shows credit assignment cliff is robust across seeds. Addresses Reviewer Concern\n    #1 + Dream C3 (statistical power).\n\n    '\n  hypothesis: 'Performance degrades monotonically with smaller h, with sharp cliff\n    below h=10. Cliff is robust across seeds (not single-run artifact).\n\n    '\n  metrics:\n  - success_rate_per_h\n  - convergence_speed\n  - collapse_rate\n  gpu_hours_estimate: 90\n  notes: 5 h-values × 15 steps × 3 seeds. h=2 已有 exp028c 作 1 seed。\n- id: plan_003\n  title: Multi-seed replication (5 seeds total)\n  claim: Claim 1\n  phase: A+\n  priority: P0\n  depends_on:\n  - plan_001\n  registry_id: null\n  status: planned\n  description: '4 additional seeds for exp029 episode-level config (5 total incl original).\n    Report mean ± std. Dream C3 要求 5-8 seeds for credible CI.\n\n    '\n  hypothesis: 'Episode-level success rate is reproducible (std < 5pp across 5 seeds).\n\n    '\n  metrics:\n  - success_rate_mean\n  - success_rate_std\n  gpu_hours_estimate: 192\n- id: plan_003b\n  title: GAE baseline comparison\n  claim: Claim 1\n  phase: A+\n  priority: P0\n  depends_on:\n  - plan_001\n  registry_id: null\n  status: planned\n  description: 'Dream C4 要求标准 RL baselines。实现 GAE(lambda=0.95, gamma=1.0) 和 GAE(lambda=1.0,\n    gamma=1.0) 在 RAGEN 中。需要 value function (critic head)。 15 steps × 3 seeds each。如果\n    GAE >> episode-level GRPO → per-token credit assignment 额外有价值。如果持平 → episode-level\n    信息是关键。 GRPO episode-level ≠ GAE(1,1)：GRPO 无 critic，所有 token 同一 advantage。\n\n    '\n  hypothesis: 'GAE provides modest improvement over episode-level GRPO due to finer\n    credit assignment, but both far exceed step-independent.\n\n    '\n  metrics:\n  - success_rate\n  - per_token_advantage_variance\n  gpu_hours_estimate: 60\n  notes: 需实现 critic head。如果实现成本过高，可用 REINFORCE baseline 替代。\n- id: plan_003c\n  title: Episode-level + valid_action_bonus (plateau-breaker, D056)\n  claim: Claim 1\n  phase: A+\n  priority: P0\n  depends_on:\n  - plan_001\n  registry_id: null\n  status: planned\n  description: 'Derived from exp013f negative (D056): dense reward gaming is step_independent-specific.\n    Episode-level training prevents per-step reward gaming because model optimizes\n    full trajectory total reward. Add valid_action_bonus=0.05 to episode-level config.\n    Test if this safely improves action_is_valid (currently 55.9%) without gaming,\n    and whether it breaks the 23-25% success plateau. Run during h-sweep batch as\n    h=full variant.\n\n    '\n  hypothesis: 'Episode-level + small valid_action_bonus safely improves action_is_valid\n    (target ≥80%) without reward gaming, and success rate exceeds 30% (breaking exp029\n    plateau). Gaming only occurs under step_independent.\n\n    '\n  metrics:\n  - success_rate\n  - action_is_valid\n  - valid_bonus_vs_task_reward_ratio\n  gpu_hours_estimate: 24\n  parent: exp013f\n  notes: 'Parent derivation: exp013f gaming → D056 insight → episode-level safety\n    hypothesis'\n- id: plan_004\n  title: Credit assignment mechanism empirical verification (paper Figure 2)\n  claim: Claim 1\n  phase: A+\n  priority: P0\n  depends_on:\n  - plan_002\n  registry_id: null\n  status: planned\n  description: \"Empirically verify \\\"Advantage Sign Misattribution\\\" mechanism (D058,\\\n    \\ Reviewer-refined): (a) Per-window advantage logging from h=2 seed 2: record\\\n    \\ (episode_id, window_position,\\n    raw_return, advantage_sign, advantage_magnitude,\\\n    \\ episode_outcome, local_action_quality_proxy)\\n(b) Key analysis: advantage sign\\\n    \\ vs episode outcome correlation (should be ~1.0),\\n    advantage sign vs local\\\n    \\ action quality correlation (should be ~0, proving misattribution)\\n(c) Contrast\\\n    \\ success vs failure episodes: success → all positive (including bad windows),\\n\\\n    \\    failure → all negative (including good windows)\\n(d) γ^k magnitude decay:\\\n    \\ advantage magnitude vs position in success episodes (e) Episode-level control:\\\n    \\ all tokens share one advantage (no position/sign variance) Data source: LOG_PER_SAMPLE_ADV=1\\\n    \\ on h=2 seed 2 (10 lines logging code, zero GPU overhead). Code reference: agent_trainer.py:271-340,\\\n    \\ core_algos.py:194-246.\\n\"\n  hypothesis: 'Per-window advantage in step_independent shows: (1) advantage sign\n    is determined by episode success/failure (correlation > 0.95), (2) advantage sign\n    is NOT correlated with window-local action quality (r < 0.1), proving sign misattribution,\n    (3) magnitude decays as γ^k from terminal position, (4) episode-level shows uniform\n    advantage with no sign/magnitude position effects.\n\n    '\n  metrics:\n  - sign_vs_outcome_correlation\n  - sign_vs_local_quality_correlation\n  - magnitude_position_decay_r2\n  - episode_level_variance\n  gpu_hours_estimate: 4\n  notes: 'D058+Reviewer: ''sign misattribution'' is the core mechanism (direction\n    error > magnitude error). γ^k decay is secondary.'\n- id: plan_005\n  title: Action-change statistics from always-on runs\n  claim: Claim 2\n  phase: B\n  priority: P1\n  depends_on:\n  - plan_001\n  registry_id: null\n  status: planned\n  description: 'Collect action-change statistics from exp029 trained checkpoints:\n    (1) fraction of verifications triggering action change, (2) correlation between\n    action change and episode success, (3) per-task-type breakdown. Informs reward\n    design and provides empirical grounding.\n\n    '\n  hypothesis: 'Most verifications are confirmatory (>60% no action change). Action\n    change positively correlates with episode success (r > 0.2).\n\n    '\n  metrics:\n  - action_change_rate\n  - correlation\n  - confirmatory_rate\n  gpu_hours_estimate: 4\n- id: plan_006\n  title: Selective verification implementation\n  claim: Claim 2\n  phase: B\n  priority: P1\n  depends_on:\n  - plan_005\n  registry_id: null\n  status: planned\n  description: 'Implement binary verify/skip decision in RAGEN framework. Agent outputs\n    special token (verify/skip) before each step. Reward = task_success + alpha *\n    action_change_when_verified - beta * verification_cost. Code-only, no GPU.\n\n    '\n  hypothesis: null\n  metrics: []\n  gpu_hours_estimate: 0\n- id: plan_007\n  title: B-IAVR selective verification training\n  claim: Claim 2, Claim 3\n  phase: B\n  priority: P1\n  depends_on:\n  - plan_006\n  - plan_001\n  registry_id: null\n  status: planned\n  description: 'Train selective verification policy via episode-level GRPO. Initialize\n    from best exp029 checkpoint. Action-change reward encourages verification only\n    when informative.\n\n    '\n  hypothesis: 'B-IAVR achieves verification rate ↓40%+ vs always-on while maintaining\n    success within 5pp of baseline.\n\n    '\n  metrics:\n  - success_rate\n  - verification_rate\n  - cost_reduction\n  gpu_hours_estimate: 96\n- id: plan_008\n  title: Selective verification full comparison\n  claim: Claim 3\n  phase: B\n  priority: P1\n  depends_on:\n  - plan_007\n  registry_id: null\n  status: planned\n  description: 'Compare on same val set: always-on / B-IAVR / no-verify / random-p\n    / confidence-threshold. Report success rate, verification rate, total inference\n    tokens, per-task breakdown.\n\n    '\n  hypothesis: 'B-IAVR dominates Pareto frontier (best success-to-cost ratio).\n\n    '\n  metrics:\n  - success_rate\n  - verification_rate\n  - cost_reduction\n  - total_tokens\n  gpu_hours_estimate: 8\n- id: plan_009\n  title: No-verify ablation\n  claim: Claim 3\n  phase: C\n  priority: P1\n  depends_on:\n  - plan_001\n  registry_id: null\n  status: planned\n  description: 'Episode-level GRPO without any self-verification. Lower bound: demonstrates\n    verification value.\n\n    '\n  hypothesis: 'Removing verification drops success by ≥10pp vs always-on.\n\n    '\n  metrics:\n  - success_rate\n  - action_is_valid\n  gpu_hours_estimate: 48\n- id: plan_010\n  title: Entropy-controlled action-change analysis\n  claim: Claim 2\n  phase: C\n  priority: P1\n  depends_on:\n  - plan_005\n  registry_id: null\n  status: planned\n  description: 'Defense for \"action change = noise\" concern. Stratify by policy entropy;\n    test if action-change-success correlation holds within each stratum.\n\n    '\n  hypothesis: 'Partial correlation remains significant (p < 0.05) after controlling\n    entropy.\n\n    '\n  metrics:\n  - partial_correlation\n  - p_value\n  gpu_hours_estimate: 4\n- id: plan_011\n  title: 'Causal intervention: random vs verification-triggered changes'\n  claim: Claim 2\n  phase: C\n  priority: P1\n  depends_on:\n  - plan_001\n  registry_id: null\n  status: planned\n  description: 'Inject random action changes at same rate as verification-triggered.\n    Compare task success. If verification-triggered >> random, causal evidence.\n\n    '\n  hypothesis: 'Verification-triggered changes yield ≥10pp higher success than random.\n\n    '\n  metrics:\n  - success_rate_triggered\n  - success_rate_random\n  - delta\n  gpu_hours_estimate: 8\n- id: plan_012\n  title: Reward signal ablation (action-change vs alternatives)\n  claim: Claim 2\n  phase: C\n  priority: P1\n  depends_on:\n  - plan_007\n  registry_id: null\n  status: planned\n  description: 'Train B-IAVR with alternative rewards: (a) action-change (ours), (b)\n    random trigger reward, (c) confidence-based reward. Demonstrates action-change\n    is the best signal.\n\n    '\n  hypothesis: 'Action-change reward produces best cost-performance tradeoff.\n\n    '\n  metrics:\n  - success_rate\n  - verification_rate\n  - cost_reduction\n  gpu_hours_estimate: 192\n- id: plan_013\n  title: ARES reproduction + comparison\n  claim: Claim 3\n  phase: C\n  priority: P1\n  depends_on:\n  - plan_007\n  registry_id: null\n  status: planned\n  description: 'Reproduce ARES SFT router on ALFWorld (same model). Head-to-head with\n    B-IAVR on identical eval episodes. Addresses \"ARES differentiation\" concern.\n\n    '\n  hypothesis: 'B-IAVR achieves ≥10pp better cost reduction than ARES at matched success.\n\n    '\n  metrics:\n  - success_rate\n  - verification_rate\n  - cost_reduction\n  gpu_hours_estimate: 24\n- id: plan_014\n  title: ScienceWorld transfer (episode-level advantage)\n  claim: Claim 1\n  phase: D\n  priority: P2\n  depends_on:\n  - plan_001\n  registry_id: null\n  status: planned\n  description: 'Validate episode-level vs step-independent on ScienceWorld. Different\n    env, similar multi-turn structure. Addresses single-env concern.\n\n    '\n  hypothesis: 'Episode-level advantage generalizes: ≥2x improvement over step-independent.\n\n    '\n  metrics:\n  - success_rate_episode\n  - success_rate_step_independent\n  gpu_hours_estimate: 72\n- id: plan_015\n  title: 7B model scaling verification\n  claim: Claim 1\n  phase: D\n  priority: P2\n  depends_on:\n  - plan_002\n  registry_id: null\n  status: planned\n  description: 'Episode-level vs step-independent on Qwen3-7B. Addresses model size\n    concern. May need cloud GPU.\n\n    '\n  hypothesis: 'Episode-level advantage holds at 7B scale.\n\n    '\n  metrics:\n  - success_rate_episode_7B\n  - success_rate_step_independent_7B\n  gpu_hours_estimate: 192\n  notes: May require cloud GPU rental (4x A100 or 2x H100)\n- id: plan_016\n  title: Per-task-type breakdown analysis\n  claim: Claim 1\n  phase: D\n  priority: P2\n  depends_on:\n  - plan_001\n  registry_id: null\n  status: planned\n  description: 'Breakdown by ALFWorld task type (pick, clean, heat, cool, examine,\n    pick_two). Shows within-environment diversity.\n\n    '\n  hypothesis: 'Episode-level advantage varies by task complexity; longer tasks benefit\n    more.\n\n    '\n  metrics:\n  - per_task_success\n  - episode_length_correlation\n  gpu_hours_estimate: 2\n\n\n## registry (completed experiments)\n\n- exp_id: exp_001\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001b\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_002\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_003\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_003_dryrun\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_003_dryrun2\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp003_dryrun3\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_003_dryrun3\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp003\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp005\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp007\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    steps_completed: 10\n    steps_planned: 30\n    crash_reason: 'OSError: No space left on device (/tmp)'\n    final_success_rate: 0.0625\n    final_action_is_valid: 0.0835\n    final_manager_invalid_action: 0.0156\n    final_pass_at_8: 0.375\n    final_pg_loss: 0.00117\n    final_ppo_kl: 0.00127\n    final_entropy: 0.057\n    final_score_mean: 0.578\n    dryrun_action_is_valid: 0.054\n    dryrun_invalid_action: 0.065\n    training_time_s: 6739\n- exp_id: exp007_dryrun\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp008\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp008_sft\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    action_is_valid: 0.9\n    format_ok: 1\n    success_rate: 0\n    final_loss: 0.069\n    final_token_accuracy: 0.973\n    data_count: 1200\n    epochs: 3\n    total_steps: 225\n    training_time_s: 576\n- exp_id: exp009\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp010\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    step: 11\n    total_steps: 30\n    crash_reason: /tmp disk full (fast_downward libdownward.so)\n    initial_val_action_is_valid: 0.652\n    initial_val_success: 0\n    step1_success: 0.047\n    step1_pass_at_8: 0.375\n    step1_action_is_valid: 0.588\n    step10_success: 0\n    step10_pass_at_8: 0\n    step10_action_is_valid: 0.683\n    step5_ppo_kl: 0.00158\n    step5_entropy: 0.1\n    trend: action_is_valid improving (58.8%→68.3%) but success collapsing (4.7%→0%)\n    checkpoint_saved: global_step_10\n- exp_id: exp011\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp012\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp012b\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    step: 8\n    total_steps: 30\n    step6_success: 0.0859\n    step6_action_is_valid: 0.613\n    step6_pass_at_16: 0.5\n    step6_ppo_kl: 0.0039\n    step6_entropy: 0.1006\n    step6_grad_norm: 1.477\n    step7_success: 0\n    step7_action_is_valid: 0.685\n    step7_pass_at_16: 0\n    step7_pg_loss: 0\n    step7_ppo_kl: 0.00439\n    step7_entropy: 0.0904\n    step7_grad_norm: 0.094\n    trend: success 8.6%→0% collapse at step 7 (same pattern as exp010, delayed 1 step).\n      grad_norm 1.477→0.094, pg_loss→0. Reward fix delayed but did not prevent collapse.\n- exp_id: exp013\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp013b\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp013c\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp013d\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp013e\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp013f\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    step: 30\n    total_steps: 30\n    completed: true\n    exit_code: 0\n    training_time_s: 10683\n    step6_success: 0.0156\n    step7_success: 0.0781\n    step10_success: 0\n    step17_success: 0.0156\n    final_val_success: 0\n    final_val_action_is_valid: 0.975\n    final_val_action_is_effective: 1\n    final_val_reward_mean_at4: 4.388\n    final_val_reward_std_at4: 0.195\n    final_val_reward_best_at4: 4.499\n    final_val_pass_at1: 0\n    action_is_valid_trend: 60%→65.9%→77.1%→97.5%\n    success_trend: 0%→1.56%→7.81%→0%→1.56%→0%\n    grad_norm_range: 1.7-2.9 (no collapse)\n    conclusion_reason: 'Dense reward gaming: model optimized valid_action_bonus (action_is_valid\n      60%→97.5%) but success stayed 0%. Reward ratio 1:67 too weak — cumulative valid_action_bonus\n      (4.5) dominated learning signal vs sparse success_reward (10.0). GRPO collapse\n      prevented but task completion not learned.'\n- exp_id: exp014c\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp014a\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp014b\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp015\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    step: 1\n    total_steps: 30\n    val_step0_success: 0\n    val_step0_action_is_valid: 0.858\n    val_step0_pass_at1: 0\n    val_step0_episodic_return: 0\n    val_step0_response_length: 2797.5\n    val_train_transition: passed\n    estimated_total_time_min: 163\n    time_per_step_min: 5.6\n- exp_id: exp016\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    step: 12\n    total_steps: 30\n    elapsed_min: 51\n    step6_success: 0\n    step6_action_is_valid: 0.521\n    step6_pg_loss: 0\n    step6_grad_norm: 0.841\n    step7_success: 0.047\n    step7_pass_at16: 0.5\n    step7_action_is_valid: 0.655\n    step10_success: 0\n    step10_action_is_valid: 0.664\n    step10_pg_loss: 0\n    step10_grad_norm: 0.856\n    step10_entropy: 0.1046\n    step10_ppo_kl: -9.1e-05\n    all_raw_rewards: 0\n    all_advantages: 0\n    all_returns: 0\n    reward_signal: BROKEN — success episodes get reward=0\n    action_is_valid_trend: 52.1%→65.5%→66.4%\n    manager_invalid_action_trend: 13.5%→11.2%→9.6%\n- exp_id: exp017_expert_sft\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_train_loss: 0.1434\n    final_step_loss: 0.04\n    final_token_accuracy: 0.983\n    epochs: 3\n    total_steps: 462\n    training_time_min: 26\n    data_count_train: 2460\n    data_count_val: 129\n    checkpoint_size_gb: 3.44\n    eval_success_rate: 0.05\n    eval_success: 1/20\n    eval_action_is_valid: 0.638\n    eval_format_ok: 0.75\n    eval_avg_steps: 22\n    eval_time_s: 149.6\n    eval_per_task:\n      put: 0/10\n      clean: 0/4\n      cool: 1/3\n      heat: 0/2\n      examine: 0/1\n    eval_parse_failures: 5/20 episodes (EP 7/12/16/17/18)\n- exp_id: exp018_sft_grpo\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp019_expert_sft_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp019b_expert_sft_v2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp019b_expert_sft_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.0718\n    eval_loss: 0.0428\n    eval_mean_token_accuracy: 0.9869\n    train_runtime_seconds: 2869.8\n    steps: 320\n    epochs: 2\n    eval_success_rate: 0.2\n    eval_format_ok: 1\n    eval_action_is_valid: 0.8533\n    eval_episodes: 20\n    eval_avg_steps: 25.4\n    eval_time_seconds: 146\n- exp_id: exp019c_expert_sft_v3\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp020_grpo_from_sft\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp020b_grpo_from_sft\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    steps_completed: 22\n    steps_planned: 30\n    hung_at_step: 23\n    step1_train_success: 0.1875\n    step10_train_success: 0.1875\n    step20_train_success: 0.125\n    step22_train_success: 0.0469\n    val_success_step0: 0\n    val_success_step20: 0\n    entropy_initial: 0.107\n    entropy_final: 0.042\n    grad_norm_initial: 2.78\n    grad_norm_step20: 5.58\n    ppo_kl_final: 0.00918\n    pass_at_16_step1: 0.75\n    pass_at_16_step22: 0.25\n    checkpoint_latest: global_step_20\n    training_status: hung_at_step23_rollout\n- exp_id: exp020c_grpo_from_sft\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp020d_grpo_from_sft\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp021_sft_ragen_format\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp021_ragen_sft_v4\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    train_loss_final: 0.038\n    train_token_accuracy: 0.988\n    train_steps: 320\n    train_epochs: 2\n    train_time_min: 47.8\n    ragen_val_success: 0.25\n    ragen_val_action_is_valid: 0.875\n    eval_sft_fast_success: 0\n    eval_sft_fast_format_ok: 1\n    eval_sft_fast_action_is_valid: 0.71\n    checkpoint_size_gb: 3.3\n    ragen_val_success_16ep: 0.0625\n    ragen_val_action_is_valid_16ep: 0.6875\n- exp_id: exp022_grpo_from_sft_v4\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    steps_completed: 1\n    steps_planned: 30\n    val_step0_success: 0.125\n    val_step0_action_is_valid: 0.4875\n    val_step0_action_is_effective: 1\n    val_step0_reward_mean: 1.25\n    val_step0_reward_best: 6.61\n    val_step0_episodes: 8\n    step_time_seconds: 208\n- exp_id: exp023_grpo_parallel\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp023c_grpo_serial\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    val_step0_success: 0.0625\n    val_step0_action_is_valid: 0.6875\n    val_step0_episodes: 16\n    train_step1_success: 0.297\n    train_step1_action_is_valid: 0.791\n    train_step1_entropy: 0.0652\n    train_step1_pass16: 0.75\n    train_step1_kl: 0.000156\n    train_step8_success: 0.234\n    train_step8_action_is_valid: 0.779\n    train_step8_entropy: 0.0555\n    train_step8_pass16: 0.5\n    train_step8_kl: 0.000475\n    steps_completed: 8\n    steps_planned: 30\n    step_time_seconds_start: 240\n    step_time_seconds_end: 365\n- exp_id: exp024_success_gated_grpo\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp025\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp025b\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp025c\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp026_step_independent_grpo\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    val_before_train_success: 0.0625\n    val_before_train_action_is_valid: 0.631\n    val_before_train_episodes: 16\n    train_step1_success: 0.2188\n    train_step1_action_is_valid: 0.686\n    train_step1_entropy: 0.2672\n    train_step1_kl_loss: 0.1797\n    train_step1_grad_norm: 14.43\n    train_step1_reward_mean: 1.218\n    train_step1_pass_at_16: 1\n    train_step2_success: 0.3281\n    train_step2_action_is_valid: 0.603\n    train_step2_entropy: 0.317\n    train_step2_kl_loss: 0.0974\n    train_step2_grad_norm: 15.62\n    train_step2_reward_mean: 1.62\n    train_step2_pass_at_16: 1\n    train_step3_success: 0.1719\n    train_step3_action_is_valid: 0.641\n    train_step3_entropy: 0.387\n    train_step3_kl_loss: 0.2617\n    train_step3_grad_norm: 15.65\n    train_step3_reward_mean: 1.079\n    train_step3_pass_at_16: 0.75\n    train_step4_success: 0\n    train_step4_action_is_valid: 0.717\n    train_step4_entropy: 0.387\n    train_step4_kl_loss: 0.054\n    train_step4_grad_norm: 13.81\n    train_step4_pass_at_16: 0\n- exp_id: exp027_stable_grpo\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    step_0_val_before_train:\n      success: 6.25\n      action_is_valid: 63.125\n      action_is_effective: 87.875\n      num_actions: 42.375\n      response_length: 114.67\n      reward_mean: 0.3226\n      val_generation_time_s: 502.57\n    step_1_train:\n      success: 35.94\n      kl_loss: 0.058\n      batch_size: 5152\n      training_time_s: 4342\n    step_2_train:\n      success: 10.16\n      kl_loss: 0.413\n      batch_size: 6144\n      training_time_s: 5886\n    step_3_train:\n      success: 10.16\n      kl_loss: 0.248\n      entropy: 0.385\n      pass_at_16: 0.5\n      grad_norm: 21.31\n      reward_mean: 0.483\n      batch_size: 6048\n      training_time_s: 4689\n    step_4_train:\n      success: 13.28\n      pass_at_16: 0.375\n      note: 'Director判定: 趋势确认, MVP未通过'\n- exp_id: exp028_prereq_zeroshot_instruct\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp028a_recipe_fix\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp028_prereq_zeroshot\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    success: 0\n    action_is_valid: 0.75\n    num_actions: 50\n    pass_at_1: 0\n    response_length: 75.07\n- exp_id: exp028c_selfguide_recipe\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    step_0_val:\n      success: 6.25\n      pass_at_1: 6.25\n      action_is_valid: 74.5\n      score_mean: 0.119\n    step_1_train:\n      success: 13.28\n      pass_at_8: 37.5\n      action_is_valid: 76.4\n      action_is_effective: 96.37\n      entropy: 0.2634\n      kl_loss: 0.0128\n      ppo_kl: 0.019\n      grad_norm: 16.88\n      score_mean: 0.843\n      time_s: 3252\n      note: 三方交叉验证通过\n    step_2_train:\n      success: 6.25\n      pass_at_8: 25\n      action_is_valid: 83.2\n      entropy: 0.247\n      kl_loss: 0.1706\n      pg_loss: 0.007\n      grad_norm: 17.3\n      score_mean: 0.274\n      time_s: 3120\n    step_3_train:\n      success: 15.63\n      pass_at_8: 68.75\n      action_is_valid: 85.9\n      entropy: 0.2488\n      kl_loss: 0.1118\n      grad_norm: 12.57\n      score_mean: 0.661\n      time_s: 2760\n    step_4_train:\n      success: 18.75\n      pass_at_8: 62.5\n      action_is_valid: 87.94\n      entropy: 0.234\n      kl_loss: 0.031\n      ppo_kl: 0.015\n    step_5_train:\n      success: 9.4\n      pass_at_8: 37.5\n      action_is_valid: 89.6\n      entropy: 0.236\n      kl_loss: 0.824\n      grad_norm: 13.1\n    step_5_val:\n      success: 6.25\n      pass_at_1: 6.25\n      action_is_valid: 96.5\n      action_is_effective: 100\n      num_actions: 49.4\n      score_mean: 0.518\n    step_6_train:\n      success: 10.94\n      action_is_valid: 90.4\n      entropy: 0.234\n      kl_loss: 0.098\n      grad_norm: 12.54\n    step_7_train:\n      success: 21.88\n      pass_at_8: 56.25\n      action_is_valid: 91.8\n      entropy: 0.224\n      kl_loss: 0.046\n    step_8_train:\n      success: 15.6\n      pass_at_8: 50\n      action_is_valid: 92.7\n      kl_loss: 0.039\n      entropy: 0.204\n    step_9_train:\n      success: 18\n      pass_at_8: 56.3\n      action_is_valid: 93.6\n      kl_loss: 0.047\n      entropy: 0.204\n    step_10_train:\n      success: 18.75\n      action_is_valid: 90.7\n      kl_loss: 0.197\n    step_10_val:\n      success: 0\n      pass_at_1: 0\n      best_at_128: 0\n      best_at_800: 0\n      action_is_valid: 93.6\n      num_actions: 49.8\n      reward_mean: 0\n      note: 灾难性崩溃，模型完全遗忘\n- exp_id: exp029_episode_level\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    current_step: 15\n    total_steps: 100\n    progress_pct: 15\n    step5_val_success: 0.25\n    step10_val_success: 0.25\n    step15_val_success: 0.28125\n    step15_val_pass_at_1: 0.28125\n    step15_val_pass_at_2: 0.469\n    step15_val_pass_at_4: 0.726\n    step15_val_pass_at_8: 0.929\n    step15_val_pass_at_16: 0.996\n    step15_val_action_is_valid: 0.5452\n    step15_val_action_is_effective: 0.7672\n    step15_val_manager_invalid_action: 0.2328\n    step15_train_success: 0.4375\n    step15_train_pass_at_8: 0.75\n    elapsed_hours: 7.35\n    eta_completion: '2026-05-19T03:00:00Z'\n- exp_id: hsweep_h2_seed1\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics:\n    train_step: 9\n    total_steps: 15\n    wandb_run_id: 7o9bjszm\n    step1:\n      success: 0.1875\n      pass_at_8: 0.4375\n      invalid_action: 0.027\n    step2:\n      success: 0.1484\n      pass_at_8: 0.5\n      invalid_action: 0.02\n    step3:\n      success: 0.1875\n      pass_at_8: 0.625\n      invalid_action: 0.028\n    step4:\n      success: 0.0547\n      pass_at_8: 0.25\n      invalid_action: 0.264\n    step5:\n      success: 0.0156\n      pass_at_8: 0.0625\n      invalid_action: 0.369\n    step6:\n      success: 0.0313\n      pass_at_8: 0.25\n      invalid_action: 0.471\n    step7:\n      success: 0.0469\n      pass_at_8: 0.1875\n      invalid_action: 0.502\n    step8:\n      success: 0.0156\n      pass_at_8: 0.125\n      invalid_action: 0.542\n    step9:\n      success: 0\n      pass_at_8: 0\n      invalid_action: 0.641\n    val_step0:\n      success: 0\n      reward_mean: 0\n    val_step5:\n      success: 0.0313\n      invalid_action: 0.781\n    checkpoint: global_step_5\n    gpu_util: 95-96%\n    collapse_onset: step3→step4\n    pid: 920380\n    elapsed_hours: 7.1\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-17T13:39:25.753Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-17T13:39:25.753Z",
  "sessionId": "3f91a417-7d76-4bf5-9691-eb7dd278d753"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-17T13:39:25.773Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：Episode-level 训练有效但 performance 中等，双机制理论部分验证，selective verification 未完成或效果弱，paper 收缩为 diagnostic contribution
核心假设：['Episode-level GRPO 收敛至 30-40% val success，足以证明优于 step-independent 但不足以支撑 cost-efficiency story', 'h-sweep cliff 存在但 sharpness 因 seed 而异（2/3 seeds 清晰，1 seed 模糊）', 'Sign misattribution 实证部分验证：sign-vs-outcome correlation 0.80-0.95（存在但非完美）', 'GAE baseline 优于 episode-level GRPO 5-12pp，削弱 contrarian positioning（finer credit 确实有价值）', 'Multi-seed std 5-8pp，reproducibility 可接受但不完美', 'Selective verification 未完成（时间/资源不足）或效果弱（verification reduction <30%）', 'ScienceWorld transfer 未执行或结果不明确']
关键指标范围：{'episode_level_val_success_converged': [0.3, 0.44], 'step_independent_h2_val_success': [0.0, 0.08], 'h_sweep_cliff_threshold': [5, 10], 'sign_vs_outcome_correlation': [0.8, 0.94], 'sign_vs_local_quality_correlation': [0.05, 0.2], 'gamma_k_magnitude_decay_r2': [0.6, 0.84], 'multi_seed_mean_success': [0.28, 0.42], 'multi_seed_std': [0.05, 0.08], 'gae_vs_episode_level_delta_pp': [5, 12], 'selective_verification_rate_reduction': [0.15, 0.35], 'selective_success_delta_vs_always_on_pp': [3, 8], 'scienceworld_episode_vs_step_ratio': [1.2, 2.0]}
叙事方向：Paper 收缩为 Plan A 方向：diagnostic + analysis contribution。标题变为 "Why Step-Independent RL Fails for LLM Multi-Turn Agents: Dual Mechanism Analysis"。 Claim 1 保留但调整措辞：sign misattribution 是 "dominant factor" 而非 "complete explanation"， 因为 correlation 未达 0.95。GAE 优势需正面讨论：承认 finer credit 在 performance 上有额外价值， 但 reframe 为 "episode-level 是 necessary minimum（消除 sign misattribution）， GAE 是 sufficient improvement（加 per-token credit）"，不再强推 contrarian "更粗就够了"。 Selective verification（Claim 2/3）降为 preliminary results 或 future work。 h-sweep 和多 seed 机制分析需做得更深（community practice survey, 更多 ablation）来补偿 selective verification 贡献的缺失。仍可投同 venue 但作为 analysis paper track。


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
tier: median
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
  "promptId": "a9413000-4003-4f0c-bf77-7ea9365ffb3d",
  "type": "user",
  "uuid": "6108daa9-bb41-4f55-ba81-6d530ff53d53",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1",
  "sessionId": "3f91a417-7d76-4bf5-9691-eb7dd278d753",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-17T13:39:25.772Z_

```json
{
  "parentUuid": "6108daa9-bb41-4f55-ba81-6d530ff53d53",
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
  "uuid": "8f38795c-1665-4518-acb4-b3c08f4b22f7",
  "timestamp": "2026-05-17T13:39:25.772Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1",
  "sessionId": "3f91a417-7d76-4bf5-9691-eb7dd278d753",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-17T13:39:25.772Z_

```json
{
  "parentUuid": "8f38795c-1665-4518-acb4-b3c08f4b22f7",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "cce4e375-48ad-4de8-8f53-b32488da6918",
  "timestamp": "2026-05-17T13:39:25.772Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1",
  "sessionId": "3f91a417-7d76-4bf5-9691-eb7dd278d753",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Episode-level 训练有效但 performance 中等，双机制理论部分验证，selective verification 未完成或效果弱，paper 收缩为 diagnostic contribution 核心假设：['Episode-level GRPO 收敛至 30-40% val su…",
  "leafUuid": "cce4e375-48ad-4de8-8f53-b32488da6918",
  "sessionId": "3f91a417-7d76-4bf5-9691-eb7dd278d753"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier outcome: episode-level RL with diagnostic framing",
  "sessionId": "3f91a417-7d76-4bf5-9691-eb7dd278d753"
}
```

---

### Assistant

_source line 8 · 2026-05-17T13:39:49.005Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed imagined experimental data for the "median" tier across all planned experiments in the experiment_plan. Each prediction needs a result_rationale explaining why this tier would produce these specific results.

Let me go through each planned experiment and generate median-tier predictions.

Let me read the experiment plan carefully and understand what median means:

Median tier:
- Episode-level GRPO converges to 30-40% val success
- h-sweep cliff exists but sharpness varies by seed (2/3 seeds clear, 1 seed fuzzy)
- Sign misattribution partially verified: sign-vs-outcome correlation 0.80-0.95


- GAE baseline outperforms episode-level GRPO by 5-12pp with multi-seed std of 5-8pp
- Selective verification shows incomplete or weak results (<30% reduction)
- ScienceWorld transfer either doesn't happen or remains unclear

Now I'm mapping each of the planned experiments to their median-tier outcomes: the h-sweep ablation, multi-seed replication, GAE baseline comparison, episode-level with valid_action_bonus, credit assignment verification, action-change statistics, and selective verification implementation.

I also need to account for plan_001, which is already done—it converged at step 15 with 28.125%, and in the median tier I'd expect that to land in the 30-40% range. Then I'm working through the remaining experiments: B-IAVR training, selective verification comparison, no-verify ablation, entropy-controlled analysis, causal intervention, reward signal ablation, ARES comparison, ScienceWorld transfer, 7B scaling, and per-task-type breakdown. I should flesh out detailed predictions for each one since the user wants thorough coverage.

For the h-sweep, the median tier suggests a cliff exists but 2 out of 3 seeds clear it while 1 stays fuzzy, with the threshold somewhere between 5-10. Multi-seed results show standard deviation of 5-8 percentage points with means spanning 28-42%. GAE appears to outperform episode-level by 5-12 percentage points, and the valid_action_bonus might provide modest gains. The mechanism verification correlations look strong for sign-vs-outcome (0.80-0.95) but weak for sign-vs-local-quality (0.05-0.2). Beyond that, the Phase B and C experiments—selective verification and beyond—are either incomplete or show weak signals.

I'll organize all these predictions into a structured format.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cce4e375-48ad-4de8-8f53-b32488da6918",
  "isSidechain": false,
  "requestId": "req_011Cb8EYugwLYhMJkBLgJXBc",
  "type": "assistant",
  "uuid": "1ea8df95-ab98-4656-9feb-1263be2ad4b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1",
  "sessionId": "3f91a417-7d76-4bf5-9691-eb7dd278d753",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HXXwVhidBzbbsz7Bgo2G1J",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 21355,
      "cache_read_input_tokens": 11841,
      "output_tokens": 14505,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21355,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 14505,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 21355,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21355
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

_source line 9 · 2026-05-17T13:43:55.539Z_

```yaml
tier: median
narrative_guidance: >
  Paper 收缩为 Plan A 方向：diagnostic + analysis contribution。
  标题变为 "Why Step-Independent RL Fails for LLM Multi-Turn Agents: Dual Mechanism Analysis"。
  Claim 1 保留但措辞调整：sign misattribution 是 "dominant factor" 而非 "complete explanation"（correlation 未达 0.95）。
  GAE 优势需正面讨论：承认 finer credit 有额外 performance 价值，reframe 为 "episode-level 是 necessary minimum，GAE 是 sufficient improvement"，
  不再强推 contrarian "更粗就够了"。Selective verification（Claim 2/3）降为 preliminary results 或 future work。
  h-sweep 和多 seed 机制分析需做得更深来补偿 selective verification 贡献的缺失。仍可投同 venue 但作为 analysis paper track。

imagined_experiments:
  - name: "Episode-level GRPO convergence (exp029 continuation)"
    plan_id: "plan_001"
    description: >
      Episode-level GRPO 继续训练至 step 50+。基于已有 step 15 数据（val=28.125%）外推收敛曲线。
      Median 档下模型持续缓慢进步但遭遇 plateau，最终稳定在 35% 附近。
    expected_results:
      step20_val_success: 0.3125
      step25_val_success: 0.34375
      step30_val_success: 0.34375
      step35_val_success: 0.375
      step40_val_success: 0.375
      step50_val_success: 0.375
      converged_val_success: 0.375
      converged_train_success: 0.5625
      converged_pass_at_1: 0.375
      converged_pass_at_4: 0.78
      converged_pass_at_8: 0.94
      converged_pass_at_16: 0.998
      converged_action_is_valid: 0.62
      converged_action_is_effective: 0.81
      converged_entropy: 0.18
      converged_ppo_kl: 0.008
      plateau_onset_step: 30
      total_training_hours: 24
    result_rationale: >
      Step 15 已达 28.125%，训练曲线减速明显（step 5→10 无进步，step 10→15 仅 +3pp）。
      Median 档下 episode-level GRPO 的 bandit-style credit（所有 token 共享同一 advantage）
      足以消除 sign misattribution，但缺乏 per-token credit 使得模型难以学习精细的 action-level 策略。
      37.5% 的 plateau 反映了 GRPO episode-level 的 credit assignment 天花板：模型学会了
      "哪类 trajectory 好"但无法精确归因 "哪个 action 关键"。Pass@8=0.94 说明 policy 覆盖了
      正确策略但 greedy sampling 时选择不够精准。这个 success rate 足以证明 episode-level 显著优于
      step-independent（0%），但不足以支撑 cost-efficiency story（需 ≥40%）。
    tables:
      - title: "Episode-level GRPO convergence trajectory"
        columns: ["step", "val_success", "train_success", "pass_at_8", "action_is_valid", "entropy"]
        rows:
          - [5, 0.25, 0.3125, 0.875, 0.50, 0.22]
          - [10, 0.25, 0.375, 0.8125, 0.52, 0.20]
          - [15, 0.28125, 0.4375, 0.75, 0.545, 0.19]
          - [20, 0.3125, 0.5, 0.8125, 0.57, 0.19]
          - [25, 0.34375, 0.5313, 0.875, 0.60, 0.18]
          - [30, 0.34375, 0.5625, 0.875, 0.61, 0.18]
          - [40, 0.375, 0.5625, 0.9375, 0.62, 0.18]
          - [50, 0.375, 0.5625, 0.9375, 0.62, 0.18]
    figures_description:
      - "Learning curve (val_success vs step): 缓慢上升至 step 30 后 plateau 于 37.5%，与 step-independent exp028c 的 0%@step10 形成鲜明对比。"
    analysis: >
      收敛于 37.5% 落入 median 指标范围 [30%, 44%]。足以作为 diagnostic paper 的核心证据：
      episode-level 训练有效（vs step-independent 灾难性崩溃），但 performance 不够强以支撑
      selective verification 的 cost-efficiency 叙事。Paper pivot 到 Plan A。

  - name: "Context window h-sweep ablation (3 seeds each)"
    plan_id: "plan_002"
    description: >
      Sweep h={2, 5, 10, 20, full}，每个 h 值 3 个 seed，每 seed 训练 15 steps。
      Median 档下 cliff 存在但 sharpness 因 seed 而异。
    expected_results:
      h2_seed1_step15_success: 0.0
      h2_seed2_step15_success: 0.0
      h2_seed3_step15_success: 0.0313
      h2_mean: 0.0104
      h2_std: 0.018
      h5_seed1_step15_success: 0.0625
      h5_seed2_step15_success: 0.0313
      h5_seed3_step15_success: 0.125
      h5_mean: 0.0729
      h5_std: 0.047
      h10_seed1_step15_success: 0.1563
      h10_seed2_step15_success: 0.125
      h10_seed3_step15_success: 0.2188
      h10_mean: 0.1667
      h10_std: 0.047
      h20_seed1_step15_success: 0.25
      h20_seed2_step15_success: 0.2188
      h20_seed3_step15_success: 0.2813
      h20_mean: 0.25
      h20_std: 0.031
      full_seed1_step15_success: 0.3125
      full_seed2_step15_success: 0.25
      full_seed3_step15_success: 0.2813
      full_mean: 0.2813
      full_std: 0.031
      cliff_threshold_h: 10
      cliff_clear_seeds: 2
      cliff_fuzzy_seeds: 1
    result_rationale: >
      h=2 一致崩溃（3/3 seeds → ~0%）：2-step window 对 ALFWorld 完全不够，policy information loss
      和 sign misattribution 同时严重。h=5 有 1 个 seed 勉强存活（12.5%）但另 2 个很弱，因为
      5-step 窗口偶尔能捕捉到短 task 的完整策略但多数时候不行。h=10 是转折区域但 seed 间方差大：
      seed 3 达 21.9% 说明 10-step 窗口在某些 seed 初始化下能部分解决 information loss，
      但 sign misattribution 仍导致梯度噪声。h=20 和 full 接近但有 gap（25% vs 28%），
      说明即使 20-step 窗口也会因 sign misattribution 损失一些信号。
      Cliff 的 "fuzzy seed" 出现在 h=10 区间——seed 3 的 21.9% 模糊了 cliff 的清晰度，
      而 seed 1/2 的 15.6%/12.5% 明确显示 h<10 区域的 degradation。2/3 seeds 清晰对应
      median 定义。
    tables:
      - title: "h-sweep results (15 steps, 3 seeds each)"
        columns: ["h", "seed1", "seed2", "seed3", "mean", "std", "collapse_at_step"]
        rows:
          - ["h=2", "0%", "0%", "3.1%", "1.0%", "1.8%", "step 3-4"]
          - ["h=5", "6.3%", "3.1%", "12.5%", "7.3%", "4.7%", "step 5-7"]
          - ["h=10", "15.6%", "12.5%", "21.9%", "16.7%", "4.7%", "none"]
          - ["h=20", "25.0%", "21.9%", "28.1%", "25.0%", "3.1%", "none"]
          - ["full", "31.3%", "25.0%", "28.1%", "28.1%", "3.1%", "none"]
      - title: "h-sweep action_is_valid at step 15"
        columns: ["h", "mean_action_is_valid", "mean_invalid_action"]
        rows:
          - ["h=2", 0.31, 0.69]
          - ["h=5", 0.48, 0.52]
          - ["h=10", 0.55, 0.45]
          - ["h=20", 0.58, 0.42]
          - ["full", 0.60, 0.40]
    figures_description:
      - "Bar chart: mean success rate per h-value with error bars (3 seeds)。清晰 cliff 在 h=5→h=2 区间，h=10 区间 seed 方差较大。"
      - "Individual seed trajectories (5 panels, one per h)：h=2 三条线一致下降，h=10 三条线有明显 spread。"
    analysis: >
      Cliff 存在于 h≈5-10 区间，但非单一 sharp threshold。h=2 → 0% 是 robust 的（3/3 seeds），
      h=5 → h=10 是 transition zone 且 seed-dependent。这支持 Claim 1 但 cliff sharpness
      弱于 ideal：无法画出一条漂亮的 "step function"，只能描述 "monotonic degradation with
      high-variance transition zone"。Paper 需要更多讨论来解释 seed 依赖性。

  - name: "Multi-seed replication (5 seeds total)"
    plan_id: "plan_003"
    description: >
      4 个额外 seed 运行 exp029 episode-level 配置（共 5 seeds），训练至 step 30+，报告 mean ± std。
    expected_results:
      seed1_converged_success: 0.375
      seed2_converged_success: 0.3125
      seed3_converged_success: 0.28125
      seed4_converged_success: 0.4063
      seed5_converged_success: 0.34375
      multi_seed_mean_success: 0.3438
      multi_seed_std: 0.048
      multi_seed_ci95_lower: 0.284
      multi_seed_ci95_upper: 0.404
      multi_seed_mean_action_is_valid: 0.59
      multi_seed_std_action_is_valid: 0.04
      multi_seed_mean_pass_at_8: 0.90
      multi_seed_std_pass_at_8: 0.03
    result_rationale: >
      5 个 seed 的 spread 反映了 GRPO 训练的固有随机性：初始化 + rollout sampling + ALFWorld
      环境随机性。Std = 4.8pp 落入 median 范围 [5%, 8%] 的下端。Mean = 34.4% 落入 [28%, 42%]。
      Seed 3 最弱（28.1%）可能因为初始 rollout 运气差导致 early advantage estimates 偏差，
      seed 4 最强（40.6%）可能恰好 early rollout 探索到了高效策略。
      这个 std 水平意味着 "episode-level 有效" 的 claim 是 robust 的（CI 下界 28.4% >> step-independent 0%），
      但具体 success rate 有不可忽略的 seed 依赖性。Reproducibility 可接受但不完美。
    tables:
      - title: "Multi-seed episode-level GRPO results (converged)"
        columns: ["seed", "val_success", "train_success", "pass_at_8", "action_is_valid", "converge_step"]
        rows:
          - [1, "37.5%", "56.3%", "93.8%", 0.62, 30]
          - [2, "31.3%", "50.0%", "87.5%", 0.58, 35]
          - [3, "28.1%", "46.9%", "87.5%", 0.55, 25]
          - [4, "40.6%", "59.4%", "93.8%", 0.63, 30]
          - [5, "34.4%", "53.1%", "87.5%", 0.59, 30]
          - ["mean±std", "34.4±4.8%", "53.1±4.9%", "90.0±3.4%", "0.59±0.04", "30±3.5"]
    figures_description:
      - "Box plot: 5-seed distribution of converged val_success，mean 34.4%，quartiles 可见。与 step-independent 的 0±0% 并排。"
      - "5 条 learning curve 叠加图：convergence speed 和 final performance 的 seed-to-seed variation。"
    analysis: >
      Std 4.8pp 意味着 paper 需要报告 CI 而非单点。CI [28.4%, 40.4%] 宽度 12pp 说明单 seed
      结果不够可信——这也是为什么 dream review 要求多 seed。好消息是 CI 下界仍远超 step-independent。

  - name: "GAE baseline comparison"
    plan_id: "plan_003b"
    description: >
      实现 GAE(λ=0.95, γ=1.0) 和 GAE(λ=1.0, γ=1.0) 作为标准 RL baseline，需要 critic head。
      15 steps × 3 seeds each。
    expected_results:
      gae_095_seed1_step15_success: 0.375
      gae_095_seed2_step15_success: 0.4063
      gae_095_seed3_step15_success: 0.4375
      gae_095_mean: 0.4063
      gae_095_std: 0.031
      gae_10_seed1_step15_success: 0.34375
      gae_10_seed2_step15_success: 0.375
      gae_10_seed3_step15_success: 0.3125
      gae_10_mean: 0.3438
      gae_10_std: 0.031
      episode_grpo_mean_at_step15: 0.2813
      gae_095_vs_episode_grpo_delta_pp: 12.5
      gae_10_vs_episode_grpo_delta_pp: 6.25
      gae_095_per_token_advantage_variance: 0.42
      gae_10_per_token_advantage_variance: 0.28
      episode_grpo_per_token_advantage_variance: 0.0
    result_rationale: >
      GAE(0.95) 的 12.5pp 优势落入 median 范围 [5, 12] 的上端。这直接挑战 contrarian positioning：
      finer credit assignment（per-token advantage via value function）确实比 episode-level
      bandit credit 提供额外信息。GAE(1.0, 1.0) 相当于 MC return + baseline，优势较小（6.25pp），
      因为 λ=1.0 等效于不做 bootstrapping，信息量接近 episode-level。
      GAE(0.95) 的优势来源于 critic 提供的 per-token baseline 减少了 variance，使得有效 action
      能更快被强化。但关键是 GAE 也远超 step-independent（40.6% vs 0%），说明问题的主要因素
      确实是 step-independent 的 sign misattribution，而非 credit granularity 不够。
      这迫使 paper 调整叙事：episode-level 是 "necessary minimum"，GAE 是 "sufficient improvement"。
    tables:
      - title: "GAE vs Episode-level GRPO comparison (step 15, 3 seeds)"
        columns: ["method", "mean_success", "std", "adv_variance", "training_cost_ratio"]
        rows:
          - ["Step-independent (h=2)", "1.0%", "1.8%", 0.85, "1.0x"]
          - ["Episode-level GRPO", "28.1%", "3.1%", 0.0, "1.2x"]
          - ["GAE(λ=1.0, γ=1.0)", "34.4%", "3.1%", 0.28, "1.8x"]
          - ["GAE(λ=0.95, γ=1.0)", "40.6%", "3.1%", 0.42, "1.8x"]
    figures_description:
      - "Bar chart: 4 methods 对比，error bars from 3 seeds。清晰展示 step-independent → episode-level 的巨大 jump，以及 episode-level → GAE 的 modest improvement。"
    analysis: >
      GAE 优势削弱 contrarian "更粗就够了" 的 positioning。Paper 需改为：step-independent 的问题
      是 sign misattribution（episode-level 解决），但 performance 最优需要 finer credit（GAE 解决）。
      两个 contribution 维度分离：诊断问题（我们的主要贡献）vs 最大化性能（GAE/竞品的贡献）。
      GAE 额外 50% 训练成本（critic head）是 trade-off，可以讨论但不改变主论点。

  - name: "Episode-level + valid_action_bonus (plateau-breaker)"
    plan_id: "plan_003c"
    description: >
      在 episode-level 配置上加 valid_action_bonus=0.05。测试是否安全提升 action_is_valid 且打破 plateau。
    expected_results:
      step15_val_success: 0.3125
      step15_val_action_is_valid: 0.72
      step15_val_action_is_effective: 0.85
      step15_train_success: 0.4688
      valid_bonus_vs_task_reward_ratio: 0.22
      gaming_detected: false
      plateau_broken: false
      success_delta_vs_no_bonus_pp: 3.1
    result_rationale: >
      Episode-level 训练下 valid_action_bonus 不会被 game（与 exp013f step-independent 不同），
      因为模型优化的是整条 trajectory 的 total reward，而非单个 window 的 return。
      Action_is_valid 从 55% 提升至 72%（有效但非 dramatic），因为 bonus 信号相对 task reward
      仍然弱（ratio 0.22 vs exp013f 的 67）。Success 仅提升 3pp（31.3% vs 28.1%），
      因为 valid action 和 task success 的 correlation 虽为正但不强——模型可以执行 valid 但
      strategically wrong 的 action。Plateau 未被打破：根本瓶颈是 credit assignment granularity，
      不是 action validity。这个实验更多是 negative control：证明 dense reward gaming 是
      step-independent 特有的问题。
    tables:
      - title: "Episode-level ± valid_action_bonus comparison (step 15)"
        columns: ["config", "val_success", "action_is_valid", "gaming", "bonus_ratio"]
        rows:
          - ["Episode-level (no bonus)", "28.1%", "54.5%", "N/A", "N/A"]
          - ["Episode-level + bonus=0.05", "31.3%", "72.0%", "No", 0.22]
          - ["Step-independent + bonus=0.05 (exp013f)", "0%", "97.5%", "Yes", 67.0]
    figures_description:
      - "对比三种配置的 action_is_valid 和 success 趋势：step-independent gaming（valid↑ success→0）vs episode-level safe（valid↑ success 持平/微升）。"
    analysis: >
      结果验证 D056 insight：dense reward gaming 是 step-independent 特有的。但 bonus 对
      打破 success plateau 帮助有限。可作为 paper 的 supplementary ablation。

  - name: "Credit assignment mechanism empirical verification (paper Figure 2)"
    plan_id: "plan_004"
    description: >
      对 h=2 seed 2 运行添加 per-window advantage logging，验证 sign misattribution 机制。
      分析 advantage sign 与 episode outcome / local action quality 的 correlation。
    expected_results:
      sign_vs_outcome_correlation: 0.87
      sign_vs_local_quality_correlation: 0.14
      gamma_k_magnitude_decay_r2: 0.72
      episode_level_advantage_variance_across_positions: 0.0
      success_episodes_all_positive_pct: 0.92
      failure_episodes_all_negative_pct: 0.89
      mixed_sign_episodes_pct: 0.11
      total_episodes_analyzed: 256
      total_windows_analyzed: 3200
    result_rationale: >
      Sign-vs-outcome correlation 0.87 而非理论预测的 ~1.0，因为 GRPO 的 group normalization
      引入噪声：当一个 group 内所有 trajectory 都失败时，GRPO 的 (R-μ)/σ 会将 "least bad"
      的 trajectory 赋予正 advantage，即使 episode 失败。这导致约 11% 的 episode 出现 "mixed sign"
      （失败 episode 中部分 window 获得正 advantage）。
      Sign-vs-local-quality correlation 0.14（非零但弱）因为 local action quality proxy
      （action_is_valid × action_is_effective）与 episode outcome 有弱正相关——好的 local action
      确实微弱增加 success 概率。但 0.14 远低于 0.87，足以证明 advantage sign 主要由 episode outcome
      决定而非 local quality。
      γ^k decay R²=0.72 说明 magnitude decay 存在但拟合不完美：实际 magnitude 受 GRPO
      normalization 和 token-level variance 影响，不是纯粹的 γ^k 指数衰减。
    tables:
      - title: "Advantage sign attribution analysis (h=2, 256 episodes)"
        columns: ["metric", "value", "interpretation"]
        rows:
          - ["sign-vs-outcome corr", 0.87, "strong but not perfect — GRPO normalization noise"]
          - ["sign-vs-local-quality corr", 0.14, "weak — sign NOT determined by local action quality"]
          - ["γ^k decay R²", 0.72, "moderate fit — magnitude decays with position but noisy"]
          - ["success eps all-positive %", "92%", "most success episodes have uniformly positive advantages"]
          - ["failure eps all-negative %", "89%", "most failure episodes have uniformly negative advantages"]
          - ["mixed-sign episodes %", "11%", "GRPO normalization creates exceptions"]
      - title: "Per-window advantage statistics (success vs failure episodes)"
        columns: ["episode_type", "mean_advantage", "std_advantage", "pct_positive", "pct_negative"]
        rows:
          - ["success (n=72)", "+0.43", "0.12", "92%", "8%"]
          - ["failure (n=184)", "-0.31", "0.15", "11%", "89%"]
      - title: "Episode-level control: advantage uniformity"
        columns: ["mode", "within_episode_sign_variance", "within_episode_magnitude_cv"]
        rows:
          - ["step-independent (h=2)", 0.18, 0.45]
          - ["episode-level", 0.0, 0.0]
    figures_description:
      - "Figure 2a: Scatter plot of per-window advantage sign (+1/-1) vs episode outcome (success/failure)，clear clustering but with ~11% exceptions in off-diagonal quadrants。"
      - "Figure 2b: Per-window advantage magnitude vs window position (from terminal)，γ^k decay 趋势线 R²=0.72。"
      - "Figure 2c: Same analysis for episode-level — all positions have identical advantage（完美水平线）。"
    analysis: >
      Sign misattribution 实证为 "dominant factor" 而非 "complete explanation"。0.87 correlation
      足够强以支撑核心 claim，但 GRPO normalization 导致的 exceptions 需要诚实讨论。
      Paper 措辞从 "advantage sign is determined by episode outcome" 改为 "advantage sign
      is predominantly determined by episode outcome (r=0.87), with exceptions arising from
      GRPO's within-group normalization"。γ^k decay 作为 secondary mechanism 报告但不过度强调。

  - name: "Action-change statistics from always-on runs"
    plan_id: "plan_005"
    description: >
      从 exp029 训练好的 checkpoint 收集 verification 后的 action change 统计。
    expected_results:
      overall_action_change_rate: 0.32
      confirmatory_rate: 0.68
      action_change_when_success: 0.28
      action_change_when_failure: 0.34
      action_change_success_correlation: 0.12
      per_task_breakdown:
        pick: {action_change_rate: 0.25, n_episodes: 40}
        clean: {action_change_rate: 0.38, n_episodes: 25}
        heat: {action_change_rate: 0.35, n_episodes: 20}
        cool: {action_change_rate: 0.30, n_episodes: 15}
        examine: {action_change_rate: 0.42, n_episodes: 10}
        pick_two: {action_change_rate: 0.40, n_episodes: 18}
      total_verification_events: 512
    result_rationale: >
      68% confirmatory rate 符合 "大部分 verification 是 confirmatory" 的 hypothesis。
      但 action_change-success correlation 仅 0.12（弱正相关），低于 hypothesis 的 0.2。
      原因：在 37.5% success rate 下，模型经常在 "confused" 状态下 change action（改了但改错了），
      导致 change ≠ improvement。高 confirmatory rate 说明 always-on verification 有大量浪费，
      支持 selective verification 的动机。但弱 correlation 意味着 action-change 作为 reward signal
      的信噪比可能不够好——这预示了 Phase B 的挑战。
    tables:
      - title: "Verification action-change statistics"
        columns: ["category", "action_change_rate", "n_events"]
        rows:
          - ["Overall", "32%", 512]
          - ["Success episodes", "28%", 192]
          - ["Failure episodes", "34%", 320]
          - ["Early turns (1-3)", "38%", 180]
          - ["Mid turns (4-6)", "30%", 170]
          - ["Late turns (7+)", "28%", 162]
    figures_description:
      - "Histogram: action change rate per turn position，early turns 更高（模型初期更不确定）。"
      - "Confusion matrix: verification outcome (change/confirm) × episode outcome (success/failure)。"
    analysis: >
      Confirmatory rate 高是好消息（支持 selective verification 动机），但 correlation 弱是坏消息
      （action-change 作为 reward 的有效性存疑）。这为 plan_007 的弱结果埋下伏笔。

  - name: "Selective verification implementation"
    plan_id: "plan_006"
    description: >
      实现 binary verify/skip decision，纯代码工作无 GPU。
    expected_results:
      implementation_complete: true
      code_changes_files: 5
      test_coverage: "unit tests passing"
      integration_verified: true
    result_rationale: >
      纯工程任务，无不确定性。实现 verify/skip token + reward 计算逻辑。
    tables: []
    figures_description: []
    analysis: >
      实现本身不影响 tier，为 plan_007 做准备。

  - name: "B-IAVR selective verification training"
    plan_id: "plan_007"
    description: >
      用 episode-level GRPO 训练 selective verification policy，从 exp029 best checkpoint 初始化。
      Action-change reward 驱动 verification 选择。
    expected_results:
      converged_success: 0.34375
      converged_verification_rate: 0.72
      verification_rate_reduction_vs_always_on: 0.28
      success_delta_vs_always_on_pp: -3.1
      training_steps_to_converge: 20
      reward_components:
        task_success_mean: 0.34
        action_change_reward_mean: 0.08
        verification_cost_penalty_mean: -0.05
      training_stability: "moderate oscillation in verification_rate"
    result_rationale: >
      Verification rate reduction 仅 28%，落入 median 范围 [15%, 35%] 但未达 target 40%。
      原因是 action-change reward 的信噪比弱（plan_005 显示 correlation 仅 0.12）：模型
      难以学到 "何时 verify 有信息量"，倾向于保守地 verify（因为 skip-and-fail 的惩罚
      高于 unnecessary-verify 的成本）。Success 下降 3.1pp 因为偶尔 skip 了本该 verify 的 turn。
      训练过程中 verification_rate 振荡反映了 reward signal 的噪声——模型在 "verify everything"
      和 "skip too much" 之间摆动。
    tables:
      - title: "B-IAVR training trajectory"
        columns: ["step", "success", "verification_rate", "cost_reduction"]
        rows:
          - [0, "37.5%", "100%", "0%"]
          - [5, "34.4%", "85%", "15%"]
          - [10, "31.3%", "68%", "32%"]
          - [15, "34.4%", "75%", "25%"]
          - [20, "34.4%", "72%", "28%"]
    figures_description:
      - "Dual-axis plot: success rate (left) and verification rate (right) vs training step，显示 verification rate 的 oscillation。"
    analysis: >
      28% verification reduction 不足以讲 compelling cost-efficiency story。Selective
      verification 降为 paper 的 preliminary results / future work section。

  - name: "Selective verification full comparison"
    plan_id: "plan_008"
    description: >
      在相同 val set 上比较 always-on / B-IAVR / no-verify / random-p / confidence-threshold。
    expected_results:
      always_on_success: 0.375
      always_on_verification_rate: 1.0
      always_on_total_tokens: 45000
      biavr_success: 0.34375
      biavr_verification_rate: 0.72
      biavr_total_tokens: 38000
      no_verify_success: 0.25
      no_verify_verification_rate: 0.0
      no_verify_total_tokens: 28000
      random_p05_success: 0.3125
      random_p05_verification_rate: 0.50
      random_p05_total_tokens: 35000
      confidence_threshold_success: 0.3125
      confidence_threshold_verification_rate: 0.65
      confidence_threshold_total_tokens: 37000
    result_rationale: >
      B-IAVR 的 Pareto 优势不明显：它与 confidence-threshold 在 success-cost space 中位置接近。
      Random-p=0.5 也达到了 31.3% success，仅比 B-IAVR 低 3pp，但 verification cost 更低。
      这说明 learned selective policy 相对 simple heuristics 的优势微弱——在 37.5% 的 base
      success rate 下，verification 的 marginal value 本身就不大（只有 +12.5pp vs no-verify），
      所以 "选择性 verify" 的空间有限。
    tables:
      - title: "Selective verification comparison"
        columns: ["method", "success", "verif_rate", "tokens", "cost_saving"]
        rows:
          - ["Always-on", "37.5%", "100%", 45000, "0%"]
          - ["B-IAVR (ours)", "34.4%", "72%", 38000, "15.6%"]
          - ["Confidence-threshold", "31.3%", "65%", 37000, "17.8%"]
          - ["Random p=0.5", "31.3%", "50%", 35000, "22.2%"]
          - ["No-verify", "25.0%", "0%", 28000, "37.8%"]
    figures_description:
      - "Pareto frontier plot: success rate vs verification cost。B-IAVR 在 frontier 上但与 confidence-threshold 重叠。"
    analysis: >
      B-IAVR 未能 dominate Pareto frontier。这进一步支持 selective verification 降为
      preliminary result。Paper 的核心 contribution 只能是 Claim 1（diagnostic）。

  - name: "No-verify ablation"
    plan_id: "plan_009"
    description: >
      Episode-level GRPO 完全不做 self-verification，作为 lower bound。
    expected_results:
      converged_val_success: 0.25
      converged_action_is_valid: 0.52
      success_delta_vs_always_on_pp: -12.5
    result_rationale: >
      无 verification 时 success 降 12.5pp（25% vs 37.5%），符合 hypothesis（≥10pp）。
      这证明 verification 本身有价值（模型确实受益于 self-check），但 12.5pp 的 gap 也意味着
      verification 的 marginal value 在 medium-performance regime 并非 overwhelming。
      对 pick 类简单任务影响小（5pp），对 clean/heat 类复杂任务影响大（15-20pp）。
    tables:
      - title: "Verification ablation"
        columns: ["config", "val_success", "delta_vs_always_on"]
        rows:
          - ["Always-on verification", "37.5%", "baseline"]
          - ["No verification", "25.0%", "-12.5pp"]
    figures_description:
      - "Per-task-type breakdown bar chart: verification 对复杂任务影响更大。"
    analysis: >
      12.5pp gap 支持 "verification 有价值" 的前提。但在 selective verification 效果弱的情况下，
      这个数据更多用于 motivation section 而非 main result。

  - name: "Entropy-controlled action-change analysis"
    plan_id: "plan_010"
    description: >
      按 policy entropy 分层，检验 action-change-success correlation 在控制 entropy 后是否保持。
    expected_results:
      raw_correlation: 0.12
      partial_correlation_controlling_entropy: 0.08
      p_value: 0.12
      low_entropy_stratum_correlation: 0.05
      high_entropy_stratum_correlation: 0.15
      n_observations: 512
    result_rationale: >
      控制 entropy 后 partial correlation 降至 0.08（p=0.12，not significant at 0.05）。
      高 entropy stratum 的 correlation（0.15）比低 entropy（0.05）高，说明 action-change
      在 uncertain states 中更 informative，但在 confident states 中接近 noise。
      这意味着 action-change 作为 reward signal 有 confounding：部分 correlation 来自
      "uncertain states → both more changes and more failures"，不是 "change → improvement"。
    tables:
      - title: "Entropy-stratified action-change analysis"
        columns: ["stratum", "n", "action_change_rate", "success_rate", "correlation"]
        rows:
          - ["Low entropy (<0.1)", 180, "22%", "42%", 0.05]
          - ["Medium entropy (0.1-0.3)", 200, "32%", "35%", 0.10]
          - ["High entropy (>0.3)", 132, "45%", "25%", 0.15]
          - ["All (raw)", 512, "32%", "34%", 0.12]
          - ["All (partial, controlling entropy)", 512, "-", "-", 0.08]
    figures_description:
      - "Scatter plot with entropy-colored points: action_change vs success，高 entropy 点（红色）集中在高 change / 低 success 区域。"
    analysis: >
      p=0.12 无法拒绝 null hypothesis。这弱化了 action-change 作为 intrinsic reward 的理论基础。
      Paper 需诚实报告：action-change signal 有 entropy confounding，但 selective verification
      已降为 future work，所以这个 negative 结果的影响可控。

  - name: "Causal intervention: random vs verification-triggered changes"
    plan_id: "plan_011"
    description: >
      随机注入 action changes（与 verification-triggered 同频率），比较 task success。
    expected_results:
      verification_triggered_success: 0.375
      random_change_success: 0.28125
      delta_pp: 9.4
      p_value: 0.04
      n_episodes_per_condition: 128
    result_rationale: >
      Verification-triggered changes 比 random 高 9.4pp，接近但略低于 hypothesis 的 10pp。
      P=0.04 勉强 significant。这提供了弱 causal evidence：verification 确实能在 marginal 上
      选择更好的 change point。但 effect size 不大，因为在 37.5% base success 下，很多 episode
      的命运在 verification 之前就已决定（选错了第一步物品 → 后续 verify 无法挽救）。
    tables:
      - title: "Causal intervention results"
        columns: ["condition", "success", "n_episodes", "p_value"]
        rows:
          - ["Verification-triggered", "37.5%", 128, "-"]
          - ["Random (same rate)", "28.1%", 128, "0.04"]
          - ["No changes", "25.0%", 128, "ref"]
    figures_description:
      - "Bar chart with significance stars: 三种 condition 的 success rate。"
    analysis: >
      弱 causal evidence。可作为 supplementary result 但不足以成为 main claim。

  - name: "Reward signal ablation (action-change vs alternatives)"
    plan_id: "plan_012"
    description: >
      用不同 reward signal 训练 B-IAVR：action-change / random trigger / confidence-based。
    expected_results:
      action_change_success: 0.34375
      action_change_verification_rate: 0.72
      random_trigger_success: 0.3125
      random_trigger_verification_rate: 0.55
      confidence_based_success: 0.3125
      confidence_based_verification_rate: 0.68
    result_rationale: >
      Action-change reward 略优于 alternatives（+3pp success, 高 verification rate），
      但差距不大。Random trigger 的 success 仅低 3pp 说明 learned policy 的 value add 有限。
      Confidence-based 与 action-change 接近因为两者都 proxy 了 "uncertainty"。
      在 median 档下，三种 reward 的差异不够大以 claim "action-change is the best signal"。
    tables:
      - title: "Reward signal comparison"
        columns: ["reward", "success", "verif_rate", "cost_reduction"]
        rows:
          - ["Action-change (ours)", "34.4%", "72%", "28%"]
          - ["Confidence-based", "31.3%", "68%", "32%"]
          - ["Random trigger", "31.3%", "55%", "45%"]
    figures_description:
      - "Grouped bar chart: 三种 reward 的 success / verification rate / cost reduction。"
    analysis: >
      差异不显著，进一步支持 selective verification 降为 future work。

  - name: "ARES reproduction + comparison"
    plan_id: "plan_013"
    description: >
      复现 ARES SFT router 在 ALFWorld 上的表现，与 B-IAVR head-to-head 比较。
    expected_results:
      ares_repro_success: 0.3125
      ares_repro_verification_rate: 0.55
      ares_repro_cost_reduction: 0.45
      biavr_success: 0.34375
      biavr_verification_rate: 0.72
      biavr_cost_reduction: 0.28
      biavr_vs_ares_success_delta_pp: 3.1
      biavr_vs_ares_cost_reduction_delta_pp: -17
    result_rationale: >
      ARES 的 SFT router 更 aggressive 地 skip verification（55% rate），cost reduction 更高（45%）
      但 success 更低（31.3%）。B-IAVR success 略高（+3pp）但 cost 更高（只省 28% vs 45%）。
      两者在 Pareto frontier 上各有优势而非 domination。
      原因：ARES 用 SFT 从 expert demonstrations 学习 skip pattern，more data-efficient；
      B-IAVR 用 RL 但 reward signal 弱导致 policy 不够 aggressive。
    tables:
      - title: "B-IAVR vs ARES comparison"
        columns: ["method", "success", "verif_rate", "cost_reduction", "training_paradigm"]
        rows:
          - ["B-IAVR (ours)", "34.4%", "72%", "28%", "RL (GRPO)"]
          - ["ARES (repro)", "31.3%", "55%", "45%", "SFT router"]
          - ["Always-on", "37.5%", "100%", "0%", "N/A"]
    figures_description:
      - "Pareto plot: B-IAVR 和 ARES 在 success-cost space 中的位置。"
    analysis: >
      无法 claim B-IAVR dominates ARES。但在 Plan A (diagnostic paper) 下，这个比较降为
      supplementary material。

  - name: "ScienceWorld transfer (episode-level advantage)"
    plan_id: "plan_014"
    description: >
      在 ScienceWorld 上验证 episode-level vs step-independent。
    expected_results:
      not_executed: true
      reason: "资源/时间不足，ScienceWorld 集成复杂度高于预期"
    result_rationale: >
      Median 档定义明确指出 "ScienceWorld transfer 未执行或结果不明确"。
      ScienceWorld 需要不同的 environment wrapper 和 action space adapter，集成工作量
      在 Phase D 时间线内难以完成，尤其在 Phase A+ 已消耗大量 GPU hours 的情况下。
      Paper 将其列为 limitation / future work，承认 single-environment 是弱点。
    tables: []
    figures_description: []
    analysis: >
      Single-environment limitation 需在 paper 中正面讨论。通过 h-sweep 的 within-ALFWorld
      多样性和 per-task-type breakdown 来部分缓解，但 reviewer concern #5 无法完全回应。

  - name: "7B model scaling verification"
    plan_id: "plan_015"
    description: >
      在 Qwen3-7B 上验证 episode-level vs step-independent。
    expected_results:
      not_executed: true
      reason: "需要 4xA100 或 2xH100 云 GPU，预算/时间约束"
    result_rationale: >
      7B 模型需要至少 4xA100 80GB（episode-level full context 下 7B 的 memory footprint 约 60GB+），
      现有双 GPU 设置无法支撑。在 median 档下 budget 不足以租用云 GPU。
      Paper 将 "small model" 列为 limitation，定位为 resource-constrained research。
    tables: []
    figures_description: []
    analysis: >
      Reviewer concern #6 只能通过 framing 缓解（"resource-constrained research setting"），
      无硬 evidence。Analysis paper track 对 model scale 的要求比 SOTA paper 更宽容。

  - name: "Per-task-type breakdown analysis"
    plan_id: "plan_016"
    description: >
      按 ALFWorld 6 种 task type 分解 episode-level 和 step-independent 的 success。
    expected_results:
      episode_level_per_task:
        pick: {success: 0.50, n_episodes: 40, avg_episode_length: 18}
        clean: {success: 0.36, n_episodes: 25, avg_episode_length: 28}
        heat: {success: 0.30, n_episodes: 20, avg_episode_length: 32}
        cool: {success: 0.33, n_episodes: 15, avg_episode_length: 25}
        examine: {success: 0.20, n_episodes: 10, avg_episode_length: 35}
        pick_two: {success: 0.22, n_episodes: 18, avg_episode_length: 40}
      step_independent_per_task:
        pick: {success: 0.05, n_episodes: 40, avg_episode_length: 18}
        clean: {success: 0.0, n_episodes: 25, avg_episode_length: 28}
        heat: {success: 0.0, n_episodes: 20, avg_episode_length: 32}
        cool: {success: 0.0, n_episodes: 15, avg_episode_length: 25}
        examine: {success: 0.0, n_episodes: 10, avg_episode_length: 35}
        pick_two: {success: 0.0, n_episodes: 18, avg_episode_length: 40}
      episode_length_vs_episode_level_advantage_correlation: -0.82
    result_rationale: >
      Episode-level 优势在长 episode 任务上更大：pick（最短，18 steps）episode-level 也只有 50%，
      但 step-independent 还有 5%；examine 和 pick_two（35-40 steps）episode-level 20-22%
      而 step-independent 0%。Correlation -0.82 说明 episode length 越长，step-independent
      的 sign misattribution 越严重（更多 window 的 advantage sign 被 episode outcome 污染）。
      Pick 任务 step-independent 残存 5% success 因为有些 pick 任务 trajectory 短到 1-2 个 window，
      sign misattribution 的伤害较小。
    tables:
      - title: "Per-task-type breakdown"
        columns: ["task_type", "n", "avg_steps", "episode_level", "step_independent", "delta"]
        rows:
          - ["pick", 40, 18, "50.0%", "5.0%", "+45.0pp"]
          - ["clean", 25, 28, "36.0%", "0.0%", "+36.0pp"]
          - ["cool", 15, 25, "33.3%", "0.0%", "+33.3pp"]
          - ["heat", 20, 32, "30.0%", "0.0%", "+30.0pp"]
          - ["pick_two", 18, 40, "22.2%", "0.0%", "+22.2pp"]
          - ["examine", 10, 35, "20.0%", "0.0%", "+20.0pp"]
    figures_description:
      - "Grouped bar chart: 每种 task type 的 episode-level vs step-independent success，按 avg_steps 排序。清晰展示长任务的 advantage 更大但 absolute success 更低。"
      - "Scatter plot: avg_episode_length vs episode-level success，负相关 r=-0.82。"
    analysis: >
      Per-task breakdown 是 diagnostic paper 的重要 figure：展示了 step-independent 崩溃
      在长 horizon 任务上尤为严重，与 sign misattribution 机制预测一致（更多 windows → 更多
      misattributed gradients）。短任务（pick）的残存 success 提供了额外 mechanistic evidence。
      这部分分析在 Plan A 下变得更重要，作为 h-sweep 的补充。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ea8df95-ab98-4656-9feb-1263be2ad4b7",
  "isSidechain": false,
  "requestId": "req_011Cb8EYugwLYhMJkBLgJXBc",
  "type": "assistant",
  "uuid": "2363ddf2-1900-4416-99f4-777cb9a180ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1",
  "sessionId": "3f91a417-7d76-4bf5-9691-eb7dd278d753",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HXXwVhidBzbbsz7Bgo2G1J",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 21355,
      "cache_read_input_tokens": 11841,
      "output_tokens": 14505,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21355,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 14505,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 21355,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21355
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Episode-level 训练有效但 performance 中等，双机制理论部分验证，selective verification 未完成或效果弱，paper 收缩为 diagnostic contribution 核心假设：['Episode-level GRPO 收敛至 30-40% val su…",
  "leafUuid": "2363ddf2-1900-4416-99f4-777cb9a180ca",
  "sessionId": "3f91a417-7d76-4bf5-9691-eb7dd278d753"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier outcome: episode-level RL with diagnostic framing",
  "sessionId": "3f91a417-7d76-4bf5-9691-eb7dd278d753"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Episode-level 训练有效但 performance 中等，双机制理论部分验证，selective verification 未完成或效果弱，paper 收缩为 diagnostic contribution 核心假设：['Episode-level GRPO 收敛至 30-40% val su…",
  "leafUuid": "2363ddf2-1900-4416-99f4-777cb9a180ca",
  "sessionId": "3f91a417-7d76-4bf5-9691-eb7dd278d753"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier outcome: episode-level RL with diagnostic framing",
  "sessionId": "3f91a417-7d76-4bf5-9691-eb7dd278d753"
}
```

---
