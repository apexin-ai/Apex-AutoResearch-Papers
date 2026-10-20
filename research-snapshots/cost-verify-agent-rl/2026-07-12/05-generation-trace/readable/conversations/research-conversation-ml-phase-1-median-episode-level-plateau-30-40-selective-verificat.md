# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：Episode-level 训练有效但 plateau 在 30-40%，双机制理论基本成立但部分指标有噪声，selective verificat

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/5d38cf08-9b48-449e-b610-0e2b32e2d744.jsonl`
- **Structured JSON:** [`5792b8c076b7ccb553cf.json`](../../sessions/57/5792b8c076b7ccb553cf.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-17T12:20:30.810Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-17T12:20:30.810Z",
  "sessionId": "5d38cf08-9b48-449e-b610-0e2b32e2d744",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：Episode-level 训练有效但 plateau 在 30-40%，双机制理论基本成立但部分指标有噪声，selective verification 初步可行但不够 clean——需要 reweight 贡献重心到 diagnostic 侧\n核心假设：[\"Episode-level GRPO 收敛到 30-40% val success（改善明显但未达 'strong agent' 标准）\", 'Multi-seed 有中等方差（std 4-7pp，趋势一致但个别 seed 偏离）', 'Sign misattribution 方向正确但不完美：sign-outcome correlation 0.80-0.95（部分 window 有噪声）', 'h-sweep cliff 存在但边界模糊（h=10 有时 collapse 有时不）', \"GAE baseline 优于 episode-level GRPO 5-15pp（说明 per-token credit 有额外价值，削弱 'episode-level 就够了' 的 claim）\", 'Phase B selective verification 部分完成：verification rate ↓20-40%, 或 success delta 3-8pp', 'Action-change reward 比 random 好但优势不大（partial r 0.10-0.20）']\n关键指标范围：{'episode_level_val_success': [0.3, 0.44], 'step_independent_val_success_at_convergence': [0.0, 0.05], 'multi_seed_std_pp': [4.0, 7.0], 'sign_vs_outcome_correlation': [0.8, 0.95], 'sign_vs_local_quality_correlation': [0.05, 0.2], 'h_sweep_cliff_threshold': [2, 5], 'GAE_vs_episode_level_delta_pp': [5, 15], 'selective_verification_rate_reduction_pct': [20, 40], 'selective_success_delta_pp': [3, 8], 'action_change_partial_correlation': [0.1, 0.2], 'train_action_is_valid': [0.6, 0.75]}\n叙事方向：重心从 \"dual contribution\" 转向 \"diagnostic contribution + preliminary application\"。 Title 调整为 \"Why Step-Independent RL Fails for Multi-Turn LLM Agents\" 或类似。 Story: (1) 核心贡献是双机制诊断——sign misattribution + information loss 的系统分析， 辅以 \"为什么社区默认走向 step-independent\" 的实践分析（context window 限制 + token-level 惯性 + framework accident）； (2) episode-level GRPO 作为 practical fix 呈现，但 acknowledge GAE 可能更优， 将此定位为 \"episode-level 是 minimum viable fix，GAE 是 upper bound\"； (3) selective verification 作为 downstream application 展示初步结果，但降低 claim 强度 （\"preliminary evidence\" 而非 \"we demonstrate\"）。 需要补充：更深的 mechanistic analysis figure、community practice survey/analysis、 详细的 RAGEN codebase walkthrough 来支撑 diagnostic 贡献的深度。 Claim 2/3 降为 moderate-to-weak。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: cost-verify-agent-rl\nfocus: Post-novelty-check framing: sign misattribution as formal concept (differentiated from Turn-PPO/HCAPO), P(correct|update) quantification, dual mechanism separation, contrarian episode-level solution. Theory refined post-D058. Evaluate with updated experiment plan including γ-sweep, K-sweep, ScienceWorld transfer.\n\n## paper_framing.md\n\n# Paper Framing — Learning When to Verify: RL-Trained Selective Self-Verification for Interactive Agents\n\n> Post-MVP 重写 (2026-05-17) | D054 framing pivot + Dream Review feedback (weak reject → 修正理论)\n\n## Core Insight\n\nMulti-turn interactive agents 的 self-verification 大部分是 confirmatory（不改变行为）而非 corrective。训练 agent 学 selective verification 的前提是 RL 训练本身能 work。我们发现 LLM agent 社区默认的 step-independent training 在长 horizon 任务中灾难性崩溃，根因是**双机制失效**：\n\n1. **Policy Information Loss**: 短窗口（h 步）的 policy 无法学习跨步策略（如 \"先探索 drawer 再去 countertop\"）\n2. **Advantage Sign Misattribution**: step_independent 中，per-window advantage 的**符号**由 episode 成败决定，而非 window-local action quality：\n   - 失败 episode 中的好 action → 获得负 advantage（被错误惩罚）\n   - 成功 episode 中的差 action → 获得正 advantage（被错误强化）\n   - 梯度方向（reinforce/suppress）反映 episode outcome 而非 local decision quality\n   - 附加：γ^k magnitude decay 使早期 window 信号更弱（γ^24 ≈ 29%, where 24 = ⌈T/h⌉-1 windows），但方向错误比幅度衰减更致命\n\nEpisode-level training 同时解决两者：policy 看全历史（解决 1），整条 trajectory 作为一个 GRPO 样本，所有 tokens 共享同一 advantage — 虽然仍是 episode-level credit（非 per-token），但消除了 window 间的 sign misattribution，因为不再需要将 episode reward 分配到独立优化的子窗口（解决 2）。\n\n**技术澄清**：GRPO 算法本身是 bandit-style（advantage = (R-μ)/σ，无显式 γ），但 RAGEN 的 step_independent 实现在 `compute_step_discounted_returns()` 中引入 γ 计算每个 window 的 return（代码：`agent_trainer.py:271-340`）。γ^(T-t) decay 对 step_independent 模式是代码事实，不是类比。Episode-level 模式下无此问题：整条 trajectory 只有一个 return = episode_reward。\n\n## Story Arc\n\n**Dual contribution**: Training methodology diagnosis + Selective verification system\n\n叙事线：\n1. Self-verification 对 interactive agents 有用，但 always-on 成本高\n2. 训练 agent 学 WHEN to verify 需要 RL → 但 LLM agent 社区默认的 step-independent training 在多轮任务上灾难性崩溃（0% at step 10）\n3. 我们诊断双机制根因（information loss + advantage sign misattribution），提出 episode-level GRPO 解决\n4. 分析 \"为什么社区默认走向 step-independent\"（context window 限制 + token-level training 惯性 + framework design accident）\n5. 在 episode-level 基础上，用 action-change 作为 verification informativeness 的 reward，训练 selective policy\n6. 结果：near-always-on performance + 显著降低 verification cost\n\n**定位**：不 claim \"发明了 episode-level RL\"（trivial），而是 \"诊断了 LLM agent RL 训练中被忽视的 step-independent 隐性代价 + 系统分析崩溃机制 + 提出实用修复方案 + 在此基础上实现 selective verification\"\n\n## Target Venue\n\n待定（NeurIPS 2026 / EMNLP 2026 / ICLR 2026），取决于实验进度和最终效果。\n\n## Core Claims\n\n### Claim 1 (strength: strong): Step-independent GRPO catastrophically fails for multi-turn agents due to dual mechanism\n- 所需证据：episode-level vs step-independent 对比（多 seed），h-sweep ablation（3 seeds each），mechanistic analysis（gradient signal measurement），GAE baseline comparison\n- 当前证据状态：**ESTABLISHED** (exp029 step5 val=25% vs exp028c step10 val=0%)\n- 机制：(1) policy information loss (h-step context insufficient), (2) advantage sign misattribution (gradient direction reflects episode outcome, not window-local action quality; additionally γ^k magnitude decay for early windows)\n- 技术细节：GRPO 算法无固有 γ，但 RAGEN step_independent 的 `compute_step_discounted_returns()` 引入 γ-discounted per-window returns → advantage 符号由 episode 成败决定。代码验证：`agent_trainer.py:271-340` + `core_algos.py:194-246`\n\n### Claim 2 (strength: moderate): Action-change is an effective intrinsic reward for verification informativeness\n- 所需证据：selective verification 训练收敛 + action-change vs random/confidence baselines\n- 当前证据状态：**not yet established**，依赖 Phase B 实验\n- 前提：episode-level 训练的 agent 需达到 ≥40% success 才有意义\n\n### Claim 3 (strength: moderate): Learned selective policy matches always-on performance at reduced verification cost\n- 所需证据：B-IAVR verification ↓40%+ 且 success delta < 3pp vs always-on\n- 当前证据状态：**not yet established**，依赖 Phase B + C\n- 前提：Claim 1 的 agent 需足够强\n\n## Contingency Plan\n\n如果 episode-level 训练收敛后 success 仍 < 40%（不足以支撑 cost-efficiency story）：\n- **Plan A**：paper 变为 diagnostic + analysis contribution — \"Why Step-Independent RL Fails for LLM Multi-Turn Agents: Dual Mechanism Analysis\" (需更深 ablation + GAE comparison + community practice survey)\n- **Plan B**：加 Self-Guide reward 到 episode-level（从 binary→dense reward），推高 performance 后再做 selective verification\n- 不考虑 downgrade venue\n- **注意**：Dream review 已证明 Plan A 纯 methodology paper 需要比预期更深的分析才能通过审稿（\"诊断社区默认实践的隐性代价\" > \"episode-level RL works\"）\n\n## Reviewer Attack Surface + Defense\n\n| # | Concern | Severity | Defense |\n|---|---------|----------|---------|\n| 1 | \"Episode-level RL is obvious / well-known\" | HIGH | h-sweep (3 seeds) 展示 non-trivial cliff + 双机制理论 + \"为什么社区默认 step-independent\" 分析 |\n| 2 | \"Theory 与 GRPO 不匹配\" | HIGH | 精确区分：GRPO 算法无 γ，但 step_independent 实现引入 γ-discounted returns（代码引用）→ per-window advantage logging 实证 + 伪代码 |\n| 3 | \"缺 GAE/标准 RL baselines\" | HIGH | 加 GAE(λ=0.95) + GAE(λ=1,γ=1) baseline，证明 episode-level GRPO 与 GAE 的差异 |\n| 4 | \"Self-Guide 3x performance gap\" | HIGH | 正面回应：不同 paradigm (expert-guided vs from-scratch RL)，不同问题（Self-Guide 回避了训练问题） |\n| 5 | Single environment (ALFWorld) | MEDIUM | ScienceWorld transfer (if resources permit) |\n| 6 | Small model (1.7B) | MEDIUM | 定位 resource-constrained; 7B 验证 (conditional) |\n| 7 | Action-change = noise vs signal | MEDIUM | Entropy-controlled analysis + causal intervention (Phase B) |\n| 8 | 与 ARES 差异化不足 | LOW | Head-to-head 对比 + 方法论差异表 |\n\n## Evidence Status Matrix\n\n| Claim | MVP Evidence | Research Evidence Needed | Priority |\n|-------|-------------|--------------------------|----------|\n| Claim 1 | exp029 vs exp028c (25% vs 0%) | h-value ablation, multi-seed, mechanism paper figure | P0 |\n| Claim 2 | N/A | Phase B full implementation | P1 |\n| Claim 3 | N/A | Phase B + C comparison suite | P1 |\n\n## Competitive Positioning\n\n| System | Method | ALFWorld | Key Difference |\n|--------|--------|----------|---------------|\n| Self-Guide (2026) | Always-on verification | 72.7% (1.7B) | We add selectivity via RL |\n| ARES (2603.07915) | SFT router, continuous effort | 52.7% token↓ | SFT vs RL, continuous vs binary |\n| Thinkless (NeurIPS'25) | RL control token | reasoning | Same RL philosophy, different domain |\n| ReflAct (EMNLP'25) | Prompting GPT-4 | 93.3% | Different scale/approach |\n| RAGEN (2025) | GRPO for agents | varies | Step-independent default — our baseline |\n\n## Research Phases\n\n1. **Phase A (DONE)**: Episode-level GRPO training — MVP passed, demonstrates Claim 1\n2. **Phase A+**: Continue training to convergence (target ≥40% success), deploy tatsu parallel patch, multi-seed\n3. **Phase B**: Implement selective verification with action-change reward — Claim 2 & 3\n4. **Phase C**: Ablation suite — context window sweep, reward ablations, baseline comparisons\n5. **Phase D**: (Conditional on resources) Multi-env / multi-model scaling\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  title: Episode-level GRPO convergence (exp029 continuation)\n  claim: Claim 1\n  phase: A+\n  priority: P0\n  depends_on: []\n  registry_id: exp029_episode_level\n  status: DONE\n  description: 'Episode-level GRPO (context_window_mode: full) on Qwen3-1.7B + ALFWorld.\n    50 steps, dual-GPU. MVP passed at step 5 (val=25%, 2x baseline 12.5%). Continue\n    to convergence (step 20+) with tatsu parallel patch for 4x val speedup.\n\n    '\n  hypothesis: 'Episode-level training enables stable RL for multi-turn agents, reaching\n    ≥40% success by convergence.\n\n    '\n  metrics:\n    current_step: 15\n    total_steps: 100\n    progress_pct: 15\n    step5_val_success: 0.25\n    step10_val_success: 0.25\n    step15_val_success: 0.28125\n    step15_val_pass_at_1: 0.28125\n    step15_val_pass_at_2: 0.469\n    step15_val_pass_at_4: 0.726\n    step15_val_pass_at_8: 0.929\n    step15_val_pass_at_16: 0.996\n    step15_val_action_is_valid: 0.5452\n    step15_val_action_is_effective: 0.7672\n    step15_val_manager_invalid_action: 0.2328\n    step15_train_success: 0.4375\n    step15_train_pass_at_8: 0.75\n    elapsed_hours: 7.35\n    eta_completion: '2026-05-19T03:00:00Z'\n  gpu_hours_estimate: 48\n  framing_ref: claim_1\n  conclusion: success\n- id: plan_002\n  title: Context window h-sweep ablation (3 seeds each)\n  claim: Claim 1\n  phase: A+\n  priority: P0\n  depends_on:\n  - plan_001\n  registry_id: null\n  status: planned\n  description: 'Sweep context_window h={2, 5, 10, 20, full} on same GRPO config. Config:\n    context_window_mode=step_independent + step_independent_history_length={h} (h=full\n    uses context_window_mode=full). 15 steps per run, 3 seeds each. KEY paper figure:\n    shows credit assignment cliff is robust across seeds. Addresses Reviewer Concern\n    #1 + Dream C3 (statistical power).\n\n    '\n  hypothesis: 'Performance degrades monotonically with smaller h, with sharp cliff\n    below h=10. Cliff is robust across seeds (not single-run artifact).\n\n    '\n  metrics:\n  - success_rate_per_h\n  - convergence_speed\n  - collapse_rate\n  gpu_hours_estimate: 90\n  notes: 5 h-values × 15 steps × 3 seeds. h=2 已有 exp028c 作 1 seed。\n- id: plan_003\n  title: Multi-seed replication (5 seeds total)\n  claim: Claim 1\n  phase: A+\n  priority: P0\n  depends_on:\n  - plan_001\n  registry_id: null\n  status: planned\n  description: '4 additional seeds for exp029 episode-level config (5 total incl original).\n    Report mean ± std. Dream C3 要求 5-8 seeds for credible CI.\n\n    '\n  hypothesis: 'Episode-level success rate is reproducible (std < 5pp across 5 seeds).\n\n    '\n  metrics:\n  - success_rate_mean\n  - success_rate_std\n  gpu_hours_estimate: 192\n- id: plan_003b\n  title: GAE baseline comparison\n  claim: Claim 1\n  phase: A+\n  priority: P0\n  depends_on:\n  - plan_001\n  registry_id: null\n  status: planned\n  description: 'Dream C4 要求标准 RL baselines。实现 GAE(lambda=0.95, gamma=1.0) 和 GAE(lambda=1.0,\n    gamma=1.0) 在 RAGEN 中。需要 value function (critic head)。 15 steps × 3 seeds each。如果\n    GAE >> episode-level GRPO → per-token credit assignment 额外有价值。如果持平 → episode-level\n    信息是关键。 GRPO episode-level ≠ GAE(1,1)：GRPO 无 critic，所有 token 同一 advantage。\n\n    '\n  hypothesis: 'GAE provides modest improvement over episode-level GRPO due to finer\n    credit assignment, but both far exceed step-independent.\n\n    '\n  metrics:\n  - success_rate\n  - per_token_advantage_variance\n  gpu_hours_estimate: 60\n  notes: 需实现 critic head。如果实现成本过高，可用 REINFORCE baseline 替代。\n- id: plan_003c\n  title: Episode-level + valid_action_bonus (plateau-breaker, D056)\n  claim: Claim 1\n  phase: A+\n  priority: P0\n  depends_on:\n  - plan_001\n  registry_id: null\n  status: planned\n  description: 'Derived from exp013f negative (D056): dense reward gaming is step_independent-specific.\n    Episode-level training prevents per-step reward gaming because model optimizes\n    full trajectory total reward. Add valid_action_bonus=0.05 to episode-level config.\n    Test if this safely improves action_is_valid (currently 55.9%) without gaming,\n    and whether it breaks the 23-25% success plateau. Run during h-sweep batch as\n    h=full variant.\n\n    '\n  hypothesis: 'Episode-level + small valid_action_bonus safely improves action_is_valid\n    (target ≥80%) without reward gaming, and success rate exceeds 30% (breaking exp029\n    plateau). Gaming only occurs under step_independent.\n\n    '\n  metrics:\n  - success_rate\n  - action_is_valid\n  - valid_bonus_vs_task_reward_ratio\n  gpu_hours_estimate: 24\n  parent: exp013f\n  notes: 'Parent derivation: exp013f gaming → D056 insight → episode-level safety\n    hypothesis'\n- id: plan_004\n  title: Credit assignment mechanism empirical verification (paper Figure 2)\n  claim: Claim 1\n  phase: A+\n  priority: P0\n  depends_on:\n  - plan_002\n  registry_id: null\n  status: planned\n  description: \"Empirically verify \\\"Advantage Sign Misattribution\\\" mechanism (D058,\\\n    \\ Reviewer-refined): (a) Per-window advantage logging from h=2 seed 2: record\\\n    \\ (episode_id, window_position,\\n    raw_return, advantage_sign, advantage_magnitude,\\\n    \\ episode_outcome, local_action_quality_proxy)\\n(b) Key analysis: advantage sign\\\n    \\ vs episode outcome correlation (should be ~1.0),\\n    advantage sign vs local\\\n    \\ action quality correlation (should be ~0, proving misattribution)\\n(c) Contrast\\\n    \\ success vs failure episodes: success → all positive (including bad windows),\\n\\\n    \\    failure → all negative (including good windows)\\n(d) γ^k magnitude decay:\\\n    \\ advantage magnitude vs position in success episodes (e) Episode-level control:\\\n    \\ all tokens share one advantage (no position/sign variance) Data source: LOG_PER_SAMPLE_ADV=1\\\n    \\ on h=2 seed 2 (10 lines logging code, zero GPU overhead). Code reference: agent_trainer.py:271-340,\\\n    \\ core_algos.py:194-246.\\n\"\n  hypothesis: 'Per-window advantage in step_independent shows: (1) advantage sign\n    is determined by episode success/failure (correlation > 0.95), (2) advantage sign\n    is NOT correlated with window-local action quality (r < 0.1), proving sign misattribution,\n    (3) magnitude decays as γ^k from terminal position, (4) episode-level shows uniform\n    advantage with no sign/magnitude position effects.\n\n    '\n  metrics:\n  - sign_vs_outcome_correlation\n  - sign_vs_local_quality_correlation\n  - magnitude_position_decay_r2\n  - episode_level_variance\n  gpu_hours_estimate: 4\n  notes: 'D058+Reviewer: ''sign misattribution'' is the core mechanism (direction\n    error > magnitude error). γ^k decay is secondary.'\n- id: plan_005\n  title: Action-change statistics from always-on runs\n  claim: Claim 2\n  phase: B\n  priority: P1\n  depends_on:\n  - plan_001\n  registry_id: null\n  status: planned\n  description: 'Collect action-change statistics from exp029 trained checkpoints:\n    (1) fraction of verifications triggering action change, (2) correlation between\n    action change and episode success, (3) per-task-type breakdown. Informs reward\n    design and provides empirical grounding.\n\n    '\n  hypothesis: 'Most verifications are confirmatory (>60% no action change). Action\n    change positively correlates with episode success (r > 0.2).\n\n    '\n  metrics:\n  - action_change_rate\n  - correlation\n  - confirmatory_rate\n  gpu_hours_estimate: 4\n- id: plan_006\n  title: Selective verification implementation\n  claim: Claim 2\n  phase: B\n  priority: P1\n  depends_on:\n  - plan_005\n  registry_id: null\n  status: planned\n  description: 'Implement binary verify/skip decision in RAGEN framework. Agent outputs\n    special token (verify/skip) before each step. Reward = task_success + alpha *\n    action_change_when_verified - beta * verification_cost. Code-only, no GPU.\n\n    '\n  hypothesis: null\n  metrics: []\n  gpu_hours_estimate: 0\n- id: plan_007\n  title: B-IAVR selective verification training\n  claim: Claim 2, Claim 3\n  phase: B\n  priority: P1\n  depends_on:\n  - plan_006\n  - plan_001\n  registry_id: null\n  status: planned\n  description: 'Train selective verification policy via episode-level GRPO. Initialize\n    from best exp029 checkpoint. Action-change reward encourages verification only\n    when informative.\n\n    '\n  hypothesis: 'B-IAVR achieves verification rate ↓40%+ vs always-on while maintaining\n    success within 5pp of baseline.\n\n    '\n  metrics:\n  - success_rate\n  - verification_rate\n  - cost_reduction\n  gpu_hours_estimate: 96\n- id: plan_008\n  title: Selective verification full comparison\n  claim: Claim 3\n  phase: B\n  priority: P1\n  depends_on:\n  - plan_007\n  registry_id: null\n  status: planned\n  description: 'Compare on same val set: always-on / B-IAVR / no-verify / random-p\n    / confidence-threshold. Report success rate, verification rate, total inference\n    tokens, per-task breakdown.\n\n    '\n  hypothesis: 'B-IAVR dominates Pareto frontier (best success-to-cost ratio).\n\n    '\n  metrics:\n  - success_rate\n  - verification_rate\n  - cost_reduction\n  - total_tokens\n  gpu_hours_estimate: 8\n- id: plan_009\n  title: No-verify ablation\n  claim: Claim 3\n  phase: C\n  priority: P1\n  depends_on:\n  - plan_001\n  registry_id: null\n  status: planned\n  description: 'Episode-level GRPO without any self-verification. Lower bound: demonstrates\n    verification value.\n\n    '\n  hypothesis: 'Removing verification drops success by ≥10pp vs always-on.\n\n    '\n  metrics:\n  - success_rate\n  - action_is_valid\n  gpu_hours_estimate: 48\n- id: plan_010\n  title: Entropy-controlled action-change analysis\n  claim: Claim 2\n  phase: C\n  priority: P1\n  depends_on:\n  - plan_005\n  registry_id: null\n  status: planned\n  description: 'Defense for \"action change = noise\" concern. Stratify by policy entropy;\n    test if action-change-success correlation holds within each stratum.\n\n    '\n  hypothesis: 'Partial correlation remains significant (p < 0.05) after controlling\n    entropy.\n\n    '\n  metrics:\n  - partial_correlation\n  - p_value\n  gpu_hours_estimate: 4\n- id: plan_011\n  title: 'Causal intervention: random vs verification-triggered changes'\n  claim: Claim 2\n  phase: C\n  priority: P1\n  depends_on:\n  - plan_001\n  registry_id: null\n  status: planned\n  description: 'Inject random action changes at same rate as verification-triggered.\n    Compare task success. If verification-triggered >> random, causal evidence.\n\n    '\n  hypothesis: 'Verification-triggered changes yield ≥10pp higher success than random.\n\n    '\n  metrics:\n  - success_rate_triggered\n  - success_rate_random\n  - delta\n  gpu_hours_estimate: 8\n- id: plan_012\n  title: Reward signal ablation (action-change vs alternatives)\n  claim: Claim 2\n  phase: C\n  priority: P1\n  depends_on:\n  - plan_007\n  registry_id: null\n  status: planned\n  description: 'Train B-IAVR with alternative rewards: (a) action-change (ours), (b)\n    random trigger reward, (c) confidence-based reward. Demonstrates action-change\n    is the best signal.\n\n    '\n  hypothesis: 'Action-change reward produces best cost-performance tradeoff.\n\n    '\n  metrics:\n  - success_rate\n  - verification_rate\n  - cost_reduction\n  gpu_hours_estimate: 192\n- id: plan_013\n  title: ARES reproduction + comparison\n  claim: Claim 3\n  phase: C\n  priority: P1\n  depends_on:\n  - plan_007\n  registry_id: null\n  status: planned\n  description: 'Reproduce ARES SFT router on ALFWorld (same model). Head-to-head with\n    B-IAVR on identical eval episodes. Addresses \"ARES differentiation\" concern.\n\n    '\n  hypothesis: 'B-IAVR achieves ≥10pp better cost reduction than ARES at matched success.\n\n    '\n  metrics:\n  - success_rate\n  - verification_rate\n  - cost_reduction\n  gpu_hours_estimate: 24\n- id: plan_014\n  title: ScienceWorld transfer (episode-level advantage)\n  claim: Claim 1\n  phase: D\n  priority: P2\n  depends_on:\n  - plan_001\n  registry_id: null\n  status: planned\n  description: 'Validate episode-level vs step-independent on ScienceWorld. Different\n    env, similar multi-turn structure. Addresses single-env concern.\n\n    '\n  hypothesis: 'Episode-level advantage generalizes: ≥2x improvement over step-independent.\n\n    '\n  metrics:\n  - success_rate_episode\n  - success_rate_step_independent\n  gpu_hours_estimate: 72\n- id: plan_015\n  title: 7B model scaling verification\n  claim: Claim 1\n  phase: D\n  priority: P2\n  depends_on:\n  - plan_002\n  registry_id: null\n  status: planned\n  description: 'Episode-level vs step-independent on Qwen3-7B. Addresses model size\n    concern. May need cloud GPU.\n\n    '\n  hypothesis: 'Episode-level advantage holds at 7B scale.\n\n    '\n  metrics:\n  - success_rate_episode_7B\n  - success_rate_step_independent_7B\n  gpu_hours_estimate: 192\n  notes: May require cloud GPU rental (4x A100 or 2x H100)\n- id: plan_016\n  title: Per-task-type breakdown analysis\n  claim: Claim 1\n  phase: D\n  priority: P2\n  depends_on:\n  - plan_001\n  registry_id: null\n  status: planned\n  description: 'Breakdown by ALFWorld task type (pick, clean, heat, cool, examine,\n    pick_two). Shows within-environment diversity.\n\n    '\n  hypothesis: 'Episode-level advantage varies by task complexity; longer tasks benefit\n    more.\n\n    '\n  metrics:\n  - per_task_success\n  - episode_length_correlation\n  gpu_hours_estimate: 2\n\n\n## registry (completed experiments)\n\n- exp_id: exp_001\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001b\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_002\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_003\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_003_dryrun\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_003_dryrun2\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp003_dryrun3\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_003_dryrun3\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp003\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp005\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp007\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    steps_completed: 10\n    steps_planned: 30\n    crash_reason: 'OSError: No space left on device (/tmp)'\n    final_success_rate: 0.0625\n    final_action_is_valid: 0.0835\n    final_manager_invalid_action: 0.0156\n    final_pass_at_8: 0.375\n    final_pg_loss: 0.00117\n    final_ppo_kl: 0.00127\n    final_entropy: 0.057\n    final_score_mean: 0.578\n    dryrun_action_is_valid: 0.054\n    dryrun_invalid_action: 0.065\n    training_time_s: 6739\n- exp_id: exp007_dryrun\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp008\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp008_sft\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    action_is_valid: 0.9\n    format_ok: 1\n    success_rate: 0\n    final_loss: 0.069\n    final_token_accuracy: 0.973\n    data_count: 1200\n    epochs: 3\n    total_steps: 225\n    training_time_s: 576\n- exp_id: exp009\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp010\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    step: 11\n    total_steps: 30\n    crash_reason: /tmp disk full (fast_downward libdownward.so)\n    initial_val_action_is_valid: 0.652\n    initial_val_success: 0\n    step1_success: 0.047\n    step1_pass_at_8: 0.375\n    step1_action_is_valid: 0.588\n    step10_success: 0\n    step10_pass_at_8: 0\n    step10_action_is_valid: 0.683\n    step5_ppo_kl: 0.00158\n    step5_entropy: 0.1\n    trend: action_is_valid improving (58.8%→68.3%) but success collapsing (4.7%→0%)\n    checkpoint_saved: global_step_10\n- exp_id: exp011\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp012\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp012b\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    step: 8\n    total_steps: 30\n    step6_success: 0.0859\n    step6_action_is_valid: 0.613\n    step6_pass_at_16: 0.5\n    step6_ppo_kl: 0.0039\n    step6_entropy: 0.1006\n    step6_grad_norm: 1.477\n    step7_success: 0\n    step7_action_is_valid: 0.685\n    step7_pass_at_16: 0\n    step7_pg_loss: 0\n    step7_ppo_kl: 0.00439\n    step7_entropy: 0.0904\n    step7_grad_norm: 0.094\n    trend: success 8.6%→0% collapse at step 7 (same pattern as exp010, delayed 1 step).\n      grad_norm 1.477→0.094, pg_loss→0. Reward fix delayed but did not prevent collapse.\n- exp_id: exp013\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp013b\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp013c\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp013d\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp013e\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp013f\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    step: 30\n    total_steps: 30\n    completed: true\n    exit_code: 0\n    training_time_s: 10683\n    step6_success: 0.0156\n    step7_success: 0.0781\n    step10_success: 0\n    step17_success: 0.0156\n    final_val_success: 0\n    final_val_action_is_valid: 0.975\n    final_val_action_is_effective: 1\n    final_val_reward_mean_at4: 4.388\n    final_val_reward_std_at4: 0.195\n    final_val_reward_best_at4: 4.499\n    final_val_pass_at1: 0\n    action_is_valid_trend: 60%→65.9%→77.1%→97.5%\n    success_trend: 0%→1.56%→7.81%→0%→1.56%→0%\n    grad_norm_range: 1.7-2.9 (no collapse)\n    conclusion_reason: 'Dense reward gaming: model optimized valid_action_bonus (action_is_valid\n      60%→97.5%) but success stayed 0%. Reward ratio 1:67 too weak — cumulative valid_action_bonus\n      (4.5) dominated learning signal vs sparse success_reward (10.0). GRPO collapse\n      prevented but task completion not learned.'\n- exp_id: exp014c\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp014a\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp014b\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp015\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    step: 1\n    total_steps: 30\n    val_step0_success: 0\n    val_step0_action_is_valid: 0.858\n    val_step0_pass_at1: 0\n    val_step0_episodic_return: 0\n    val_step0_response_length: 2797.5\n    val_train_transition: passed\n    estimated_total_time_min: 163\n    time_per_step_min: 5.6\n- exp_id: exp016\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    step: 12\n    total_steps: 30\n    elapsed_min: 51\n    step6_success: 0\n    step6_action_is_valid: 0.521\n    step6_pg_loss: 0\n    step6_grad_norm: 0.841\n    step7_success: 0.047\n    step7_pass_at16: 0.5\n    step7_action_is_valid: 0.655\n    step10_success: 0\n    step10_action_is_valid: 0.664\n    step10_pg_loss: 0\n    step10_grad_norm: 0.856\n    step10_entropy: 0.1046\n    step10_ppo_kl: -9.1e-05\n    all_raw_rewards: 0\n    all_advantages: 0\n    all_returns: 0\n    reward_signal: BROKEN — success episodes get reward=0\n    action_is_valid_trend: 52.1%→65.5%→66.4%\n    manager_invalid_action_trend: 13.5%→11.2%→9.6%\n- exp_id: exp017_expert_sft\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_train_loss: 0.1434\n    final_step_loss: 0.04\n    final_token_accuracy: 0.983\n    epochs: 3\n    total_steps: 462\n    training_time_min: 26\n    data_count_train: 2460\n    data_count_val: 129\n    checkpoint_size_gb: 3.44\n    eval_success_rate: 0.05\n    eval_success: 1/20\n    eval_action_is_valid: 0.638\n    eval_format_ok: 0.75\n    eval_avg_steps: 22\n    eval_time_s: 149.6\n    eval_per_task:\n      put: 0/10\n      clean: 0/4\n      cool: 1/3\n      heat: 0/2\n      examine: 0/1\n    eval_parse_failures: 5/20 episodes (EP 7/12/16/17/18)\n- exp_id: exp018_sft_grpo\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp019_expert_sft_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp019b_expert_sft_v2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp019b_expert_sft_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.0718\n    eval_loss: 0.0428\n    eval_mean_token_accuracy: 0.9869\n    train_runtime_seconds: 2869.8\n    steps: 320\n    epochs: 2\n    eval_success_rate: 0.2\n    eval_format_ok: 1\n    eval_action_is_valid: 0.8533\n    eval_episodes: 20\n    eval_avg_steps: 25.4\n    eval_time_seconds: 146\n- exp_id: exp019c_expert_sft_v3\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp020_grpo_from_sft\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp020b_grpo_from_sft\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    steps_completed: 22\n    steps_planned: 30\n    hung_at_step: 23\n    step1_train_success: 0.1875\n    step10_train_success: 0.1875\n    step20_train_success: 0.125\n    step22_train_success: 0.0469\n    val_success_step0: 0\n    val_success_step20: 0\n    entropy_initial: 0.107\n    entropy_final: 0.042\n    grad_norm_initial: 2.78\n    grad_norm_step20: 5.58\n    ppo_kl_final: 0.00918\n    pass_at_16_step1: 0.75\n    pass_at_16_step22: 0.25\n    checkpoint_latest: global_step_20\n    training_status: hung_at_step23_rollout\n- exp_id: exp020c_grpo_from_sft\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp020d_grpo_from_sft\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp021_sft_ragen_format\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp021_ragen_sft_v4\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    train_loss_final: 0.038\n    train_token_accuracy: 0.988\n    train_steps: 320\n    train_epochs: 2\n    train_time_min: 47.8\n    ragen_val_success: 0.25\n    ragen_val_action_is_valid: 0.875\n    eval_sft_fast_success: 0\n    eval_sft_fast_format_ok: 1\n    eval_sft_fast_action_is_valid: 0.71\n    checkpoint_size_gb: 3.3\n    ragen_val_success_16ep: 0.0625\n    ragen_val_action_is_valid_16ep: 0.6875\n- exp_id: exp022_grpo_from_sft_v4\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    steps_completed: 1\n    steps_planned: 30\n    val_step0_success: 0.125\n    val_step0_action_is_valid: 0.4875\n    val_step0_action_is_effective: 1\n    val_step0_reward_mean: 1.25\n    val_step0_reward_best: 6.61\n    val_step0_episodes: 8\n    step_time_seconds: 208\n- exp_id: exp023_grpo_parallel\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp023c_grpo_serial\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    val_step0_success: 0.0625\n    val_step0_action_is_valid: 0.6875\n    val_step0_episodes: 16\n    train_step1_success: 0.297\n    train_step1_action_is_valid: 0.791\n    train_step1_entropy: 0.0652\n    train_step1_pass16: 0.75\n    train_step1_kl: 0.000156\n    train_step8_success: 0.234\n    train_step8_action_is_valid: 0.779\n    train_step8_entropy: 0.0555\n    train_step8_pass16: 0.5\n    train_step8_kl: 0.000475\n    steps_completed: 8\n    steps_planned: 30\n    step_time_seconds_start: 240\n    step_time_seconds_end: 365\n- exp_id: exp024_success_gated_grpo\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp025\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp025b\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp025c\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp026_step_independent_grpo\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    val_before_train_success: 0.0625\n    val_before_train_action_is_valid: 0.631\n    val_before_train_episodes: 16\n    train_step1_success: 0.2188\n    train_step1_action_is_valid: 0.686\n    train_step1_entropy: 0.2672\n    train_step1_kl_loss: 0.1797\n    train_step1_grad_norm: 14.43\n    train_step1_reward_mean: 1.218\n    train_step1_pass_at_16: 1\n    train_step2_success: 0.3281\n    train_step2_action_is_valid: 0.603\n    train_step2_entropy: 0.317\n    train_step2_kl_loss: 0.0974\n    train_step2_grad_norm: 15.62\n    train_step2_reward_mean: 1.62\n    train_step2_pass_at_16: 1\n    train_step3_success: 0.1719\n    train_step3_action_is_valid: 0.641\n    train_step3_entropy: 0.387\n    train_step3_kl_loss: 0.2617\n    train_step3_grad_norm: 15.65\n    train_step3_reward_mean: 1.079\n    train_step3_pass_at_16: 0.75\n    train_step4_success: 0\n    train_step4_action_is_valid: 0.717\n    train_step4_entropy: 0.387\n    train_step4_kl_loss: 0.054\n    train_step4_grad_norm: 13.81\n    train_step4_pass_at_16: 0\n- exp_id: exp027_stable_grpo\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    step_0_val_before_train:\n      success: 6.25\n      action_is_valid: 63.125\n      action_is_effective: 87.875\n      num_actions: 42.375\n      response_length: 114.67\n      reward_mean: 0.3226\n      val_generation_time_s: 502.57\n    step_1_train:\n      success: 35.94\n      kl_loss: 0.058\n      batch_size: 5152\n      training_time_s: 4342\n    step_2_train:\n      success: 10.16\n      kl_loss: 0.413\n      batch_size: 6144\n      training_time_s: 5886\n    step_3_train:\n      success: 10.16\n      kl_loss: 0.248\n      entropy: 0.385\n      pass_at_16: 0.5\n      grad_norm: 21.31\n      reward_mean: 0.483\n      batch_size: 6048\n      training_time_s: 4689\n    step_4_train:\n      success: 13.28\n      pass_at_16: 0.375\n      note: 'Director判定: 趋势确认, MVP未通过'\n- exp_id: exp028_prereq_zeroshot_instruct\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp028a_recipe_fix\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp028_prereq_zeroshot\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    success: 0\n    action_is_valid: 0.75\n    num_actions: 50\n    pass_at_1: 0\n    response_length: 75.07\n- exp_id: exp028c_selfguide_recipe\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    step_0_val:\n      success: 6.25\n      pass_at_1: 6.25\n      action_is_valid: 74.5\n      score_mean: 0.119\n    step_1_train:\n      success: 13.28\n      pass_at_8: 37.5\n      action_is_valid: 76.4\n      action_is_effective: 96.37\n      entropy: 0.2634\n      kl_loss: 0.0128\n      ppo_kl: 0.019\n      grad_norm: 16.88\n      score_mean: 0.843\n      time_s: 3252\n      note: 三方交叉验证通过\n    step_2_train:\n      success: 6.25\n      pass_at_8: 25\n      action_is_valid: 83.2\n      entropy: 0.247\n      kl_loss: 0.1706\n      pg_loss: 0.007\n      grad_norm: 17.3\n      score_mean: 0.274\n      time_s: 3120\n    step_3_train:\n      success: 15.63\n      pass_at_8: 68.75\n      action_is_valid: 85.9\n      entropy: 0.2488\n      kl_loss: 0.1118\n      grad_norm: 12.57\n      score_mean: 0.661\n      time_s: 2760\n    step_4_train:\n      success: 18.75\n      pass_at_8: 62.5\n      action_is_valid: 87.94\n      entropy: 0.234\n      kl_loss: 0.031\n      ppo_kl: 0.015\n    step_5_train:\n      success: 9.4\n      pass_at_8: 37.5\n      action_is_valid: 89.6\n      entropy: 0.236\n      kl_loss: 0.824\n      grad_norm: 13.1\n    step_5_val:\n      success: 6.25\n      pass_at_1: 6.25\n      action_is_valid: 96.5\n      action_is_effective: 100\n      num_actions: 49.4\n      score_mean: 0.518\n    step_6_train:\n      success: 10.94\n      action_is_valid: 90.4\n      entropy: 0.234\n      kl_loss: 0.098\n      grad_norm: 12.54\n    step_7_train:\n      success: 21.88\n      pass_at_8: 56.25\n      action_is_valid: 91.8\n      entropy: 0.224\n      kl_loss: 0.046\n    step_8_train:\n      success: 15.6\n      pass_at_8: 50\n      action_is_valid: 92.7\n      kl_loss: 0.039\n      entropy: 0.204\n    step_9_train:\n      success: 18\n      pass_at_8: 56.3\n      action_is_valid: 93.6\n      kl_loss: 0.047\n      entropy: 0.204\n    step_10_train:\n      success: 18.75\n      action_is_valid: 90.7\n      kl_loss: 0.197\n    step_10_val:\n      success: 0\n      pass_at_1: 0\n      best_at_128: 0\n      best_at_800: 0\n      action_is_valid: 93.6\n      num_actions: 49.8\n      reward_mean: 0\n      note: 灾难性崩溃，模型完全遗忘\n- exp_id: exp029_episode_level\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    current_step: 15\n    total_steps: 100\n    progress_pct: 15\n    step5_val_success: 0.25\n    step10_val_success: 0.25\n    step15_val_success: 0.28125\n    step15_val_pass_at_1: 0.28125\n    step15_val_pass_at_2: 0.469\n    step15_val_pass_at_4: 0.726\n    step15_val_pass_at_8: 0.929\n    step15_val_pass_at_16: 0.996\n    step15_val_action_is_valid: 0.5452\n    step15_val_action_is_effective: 0.7672\n    step15_val_manager_invalid_action: 0.2328\n    step15_train_success: 0.4375\n    step15_train_pass_at_8: 0.75\n    elapsed_hours: 7.35\n    eta_completion: '2026-05-19T03:00:00Z'\n- exp_id: hsweep_h2_seed1\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics:\n    train_step: 9\n    total_steps: 15\n    wandb_run_id: 7o9bjszm\n    step1:\n      success: 0.1875\n      pass_at_8: 0.4375\n      invalid_action: 0.027\n    step2:\n      success: 0.1484\n      pass_at_8: 0.5\n      invalid_action: 0.02\n    step3:\n      success: 0.1875\n      pass_at_8: 0.625\n      invalid_action: 0.028\n    step4:\n      success: 0.0547\n      pass_at_8: 0.25\n      invalid_action: 0.264\n    step5:\n      success: 0.0156\n      pass_at_8: 0.0625\n      invalid_action: 0.369\n    step6:\n      success: 0.0313\n      pass_at_8: 0.25\n      invalid_action: 0.471\n    step7:\n      success: 0.0469\n      pass_at_8: 0.1875\n      invalid_action: 0.502\n    step8:\n      success: 0.0156\n      pass_at_8: 0.125\n      invalid_action: 0.542\n    step9:\n      success: 0\n      pass_at_8: 0\n      invalid_action: 0.641\n    val_step0:\n      success: 0\n      reward_mean: 0\n    val_step5:\n      success: 0.0313\n      invalid_action: 0.781\n    checkpoint: global_step_5\n    gpu_util: 95-96%\n    collapse_onset: step3→step4\n    pid: 920380\n    elapsed_hours: 7.1\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-17T12:20:30.814Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-17T12:20:30.814Z",
  "sessionId": "5d38cf08-9b48-449e-b610-0e2b32e2d744"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-17T12:20:30.841Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：Episode-level 训练有效但 plateau 在 30-40%，双机制理论基本成立但部分指标有噪声，selective verification 初步可行但不够 clean——需要 reweight 贡献重心到 diagnostic 侧
核心假设：["Episode-level GRPO 收敛到 30-40% val success（改善明显但未达 'strong agent' 标准）", 'Multi-seed 有中等方差（std 4-7pp，趋势一致但个别 seed 偏离）', 'Sign misattribution 方向正确但不完美：sign-outcome correlation 0.80-0.95（部分 window 有噪声）', 'h-sweep cliff 存在但边界模糊（h=10 有时 collapse 有时不）', "GAE baseline 优于 episode-level GRPO 5-15pp（说明 per-token credit 有额外价值，削弱 'episode-level 就够了' 的 claim）", 'Phase B selective verification 部分完成：verification rate ↓20-40%, 或 success delta 3-8pp', 'Action-change reward 比 random 好但优势不大（partial r 0.10-0.20）']
关键指标范围：{'episode_level_val_success': [0.3, 0.44], 'step_independent_val_success_at_convergence': [0.0, 0.05], 'multi_seed_std_pp': [4.0, 7.0], 'sign_vs_outcome_correlation': [0.8, 0.95], 'sign_vs_local_quality_correlation': [0.05, 0.2], 'h_sweep_cliff_threshold': [2, 5], 'GAE_vs_episode_level_delta_pp': [5, 15], 'selective_verification_rate_reduction_pct': [20, 40], 'selective_success_delta_pp': [3, 8], 'action_change_partial_correlation': [0.1, 0.2], 'train_action_is_valid': [0.6, 0.75]}
叙事方向：重心从 "dual contribution" 转向 "diagnostic contribution + preliminary application"。 Title 调整为 "Why Step-Independent RL Fails for Multi-Turn LLM Agents" 或类似。 Story: (1) 核心贡献是双机制诊断——sign misattribution + information loss 的系统分析， 辅以 "为什么社区默认走向 step-independent" 的实践分析（context window 限制 + token-level 惯性 + framework accident）； (2) episode-level GRPO 作为 practical fix 呈现，但 acknowledge GAE 可能更优， 将此定位为 "episode-level 是 minimum viable fix，GAE 是 upper bound"； (3) selective verification 作为 downstream application 展示初步结果，但降低 claim 强度 （"preliminary evidence" 而非 "we demonstrate"）。 需要补充：更深的 mechanistic analysis figure、community practice survey/analysis、 详细的 RAGEN codebase walkthrough 来支撑 diagnostic 贡献的深度。 Claim 2/3 降为 moderate-to-weak。


基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: cost-verify-agent-rl
focus: Post-novelty-check framing: sign misattribution as formal concept (differentiated from Turn-PPO/HCAPO), P(correct|update) quantification, dual mechanism separation, contrarian episode-level solution. Theory refined post-D058. Evaluate with updated experiment plan including γ-sweep, K-sweep, ScienceWorld transfer.

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

## Evidence Status Matrix

| Claim | MVP Evidence | Research Evidence Needed | Priority |
|-------|-------------|--------------------------|----------|
| Claim 1 | exp029 vs exp028c (25% vs 0%) | h-value ablation, multi-seed, mechanism paper figure | P0 |
| Claim 2 | N/A | Phase B full implementation | P1 |
| Claim 3 | N/A | Phase B + C comparison suite | P1 |

## Competitive Positioning

| System | Method | ALFWorld | Key Difference |
|--------|--------|----------|---------------|
| Self-Guide (2026) | Always-on verification | 72.7% (1.7B) | We add selectivity via RL |
| ARES (2603.07915) | SFT router, continuous effort | 52.7% token↓ | SFT vs RL, continuous vs binary |
| Thinkless (NeurIPS'25) | RL control token | reasoning | Same RL philosophy, different domain |
| ReflAct (EMNLP'25) | Prompting GPT-4 | 93.3% | Different scale/approach |
| RAGEN (2025) | GRPO for agents | varies | Step-independent default — our baseline |

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
  "promptId": "479f830b-75b7-412a-bc43-688d94da94cb",
  "type": "user",
  "uuid": "ce7baf69-0cb6-4f86-8611-de36a045bcec",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1",
  "sessionId": "5d38cf08-9b48-449e-b610-0e2b32e2d744",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-17T12:20:30.839Z_

```json
{
  "parentUuid": "ce7baf69-0cb6-4f86-8611-de36a045bcec",
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
  "uuid": "dc27d88f-1bc2-4adb-8e66-856da81358ff",
  "timestamp": "2026-05-17T12:20:30.839Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1",
  "sessionId": "5d38cf08-9b48-449e-b610-0e2b32e2d744",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-17T12:20:30.839Z_

```json
{
  "parentUuid": "dc27d88f-1bc2-4adb-8e66-856da81358ff",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "7aa34963-b4f2-44c5-aecd-2799ee514ec0",
  "timestamp": "2026-05-17T12:20:30.839Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1",
  "sessionId": "5d38cf08-9b48-449e-b610-0e2b32e2d744",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Episode-level 训练有效但 plateau 在 30-40%，双机制理论基本成立但部分指标有噪声，selective verification 初步可行但不够 clean——需要 reweight 贡献重心到 diagnostic 侧 核心假设：[\"Episode-level GRPO 收敛到…",
  "leafUuid": "7aa34963-b4f2-44c5-aecd-2799ee514ec0",
  "sessionId": "5d38cf08-9b48-449e-b610-0e2b32e2d744"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Diagnosing multi-turn LLM agent RL: why step-independent fails",
  "sessionId": "5d38cf08-9b48-449e-b610-0e2b32e2d744"
}
```

---

### Assistant

_source line 8 · 2026-05-17T12:20:48.313Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted experimental results for each "planned" experiment in the experiment_plan, under the "median" tier assumptions. I need to provide result_rationale for each prediction explaining why this result would occur under median tier conditions.

Let me go through each planned experiment and generate predictions based on the median tier definition:

Median tier key characteristics:
- Episode-level val success: 30-44%
- Step-independent val success at convergence: 0-5%
- Multi-seed std: 4-7pp
- Sign vs outcome correlation: 0.80-0.95
- Sign vs local quality correlation: 0.05-0.20


- h-sweep cliff threshold: h=2-5
- GAE vs episode-level delta: 5-15pp
- Selective verification rate reduction: 20-40%
- Selective success delta: 3-8pp
- Action-change partial correlation: 0.10-0.20
- Train action_is_valid: 0.60-0.75

The narrative is shifting toward positioning this as a diagnostic study that reveals why step-independent RL fundamentally struggles with multi-turn LLM agents, rather than focusing on dual contributions. Now I'm working through the first planned experiment to generate its predicted results. Looking at the remaining experiments, I need to flesh out the specifics for the 7B scaling work and the per-task breakdown analysis to understand how performance varies across different problem domains.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7aa34963-b4f2-44c5-aecd-2799ee514ec0",
  "isSidechain": false,
  "requestId": "req_011Cb88XsorXc4Yc1ignnTY5",
  "type": "assistant",
  "uuid": "a18d7c3e-badc-4812-b08c-29df3525bbb5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1",
  "sessionId": "5d38cf08-9b48-449e-b610-0e2b32e2d744",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014FNUVaqZCzdNh8L7AMCE1P",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 20477,
      "cache_read_input_tokens": 11841,
      "output_tokens": 11600,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20477,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 11600,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 20477,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20477
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

_source line 9 · 2026-05-17T12:24:35.760Z_

```yaml
tier: median
narrative_guidance: "重心从 'dual contribution' 转向 'diagnostic contribution + preliminary application'。核心贡献是双机制诊断的系统分析（sign misattribution + information loss），episode-level GRPO 定位为 minimum viable fix 而非 optimal solution（GAE 可能更优 5-15pp），selective verification 作为 preliminary downstream application 呈现（claim 降为 moderate-to-weak）。需要补充 mechanistic analysis 深度和 community practice survey 来弥补 application 侧的弱势。"

imagined_experiments:
  - name: "Context window h-sweep ablation"
    plan_id: "plan_002"
    description: "h={2, 5, 10, 20, full} × 3 seeds each, 15 steps per run"
    expected_results:
      h2_mean_success: 0.02
      h2_std: 0.02
      h5_mean_success: 0.08
      h5_std: 0.04
      h10_mean_success: 0.18
      h10_std: 0.06
      h20_mean_success: 0.28
      h20_std: 0.05
      full_mean_success: 0.34
      full_std: 0.05
      cliff_location: "h=5→h=2 (sharp), h=10→h=5 (moderate)"
      h2_collapse_rate: 0.67
      h5_collapse_rate: 0.33
      h10_collapse_rate: 0.0
    result_rationale: "Median 档下 cliff 边界模糊：h=10 有时 collapse 有时不（0/3 seeds collapse 但方差大），h=5 是 unstable zone（1/3 collapse），h=2 几乎确定 collapse（2/3 seeds）。与 strong 档的 clean cliff（h=5 以下全崩）不同，这里存在 seed-dependent 的边界效应。原因：sign misattribution 的影响程度取决于 episode 长度分布——短 episode（如 pick 任务 10 步内完成）在 h=10 下 window 数少，misattribution 较轻；长 episode（examine 30+ 步）在 h=10 下仍有显著 misattribution。Seed 间的差异来自 initial rollout 的任务分布随机性。full 模式收敛到 34% 而非更高（median 档上限 44%），因为 1.7B 模型 capacity 和 ALFWorld 的 exploration 难度形成了 soft ceiling。"
    tables:
      - title: "H-sweep results (15 steps, 3 seeds)"
        columns: ["h", "seed1", "seed2", "seed3", "mean±std", "collapse?"]
        rows:
          - ["2", "0%", "4%", "3%", "2.3±2.1", "2/3 collapse by step 5"]
          - ["5", "12%", "6%", "5%", "7.7±3.8", "1/3 partial collapse"]
          - ["10", "22%", "14%", "19%", "18.3±4.0", "0/3 collapse"]
          - ["20", "32%", "24%", "28%", "28.0±4.0", "0/3"]
          - ["full", "38%", "30%", "34%", "34.0±4.0", "0/3"]
    figures_description:
      - "Figure: Line plot with error bars, x=h (log scale), y=val_success_rate. Shows monotonic improvement but cliff is gradual (h=2→5) rather than sharp step function. Shaded region = seed std. Annotation: 'cliff zone h∈[2,5]' with dashed boundary."
    analysis: "Cliff 存在但不如预期 clean。Reviewer 可能质疑 'catastrophic' 一词——h=5 仍有 8% 而非 0%。需要调整叙述为 'severe degradation zone' 而非 'binary cliff'。个别 seed 在 h=10 表现不稳定（14% vs 22%）增加了 std，但趋势方向一致。这支持 Claim 1 但需要降低 language 的绝对性。"

  - name: "Multi-seed replication (5 seeds)"
    plan_id: "plan_003"
    description: "4 additional seeds for episode-level config, report mean±std at step 15"
    expected_results:
      seed1_success: 0.28
      seed2_success: 0.34
      seed3_success: 0.38
      seed4_success: 0.31
      seed5_success: 0.22
      mean_success: 0.306
      std_success: 0.059
      min_success: 0.22
      max_success: 0.38
      convergence_step_range: "10-15"
    result_rationale: "Median 档定义 std 4-7pp，这里取 5.9pp。5 seeds 中有一个 outlier（seed5=22%）拉低均值并增大方差。原因：episode-level GRPO 对 initial rollout quality 敏感——如果前几步 rollout 恰好采样到较难的任务子集（如 examine_in_light），early gradient 信号弱，后续收敛慢。大部分 seed 在 28-38% 范围内（趋势一致），但 seed5 的偏离使 CI 较宽。这足以支持 'episode-level works' 的 claim，但 reviewer 会注意到 22% outlier 并要求解释。"
    tables:
      - title: "Multi-seed episode-level results at step 15"
        columns: ["seed", "val_success", "train_success", "action_is_valid", "pass_at_8"]
        rows:
          - ["1 (original)", "28.1%", "43.8%", "54.5%", "92.9%"]
          - ["2", "34.4%", "50.0%", "61.2%", "95.3%"]
          - ["3", "37.5%", "53.1%", "63.8%", "96.1%"]
          - ["4", "31.3%", "46.9%", "58.7%", "93.8%"]
          - ["5", "21.9%", "34.4%", "48.2%", "87.5%"]
          - ["mean±std", "30.6±5.9%", "45.6±7.1%", "57.3±6.1%", "93.1±3.4%"]
    figures_description:
      - "Figure: Box plot of 5 seeds with individual points overlaid. Median line at 31.3%, box spans 28.1-34.4% (IQR), whiskers to 22-38%. Annotate seed 5 as potential outlier."
    analysis: "Std=5.9pp 处于 median 档范围（4-7pp）。趋势一致（所有 seed > step-independent baseline 的 0-6%），但绝对方差偏大，使 95% CI 为 [30.6±5.3pp] = [25.3, 35.9]。不能 claim '≥40% success' — mean 只有 30.6%。Paper 需要 acknowledge variance 并定位 episode-level 为 'consistent improvement over step-independent' 而非 'strong agent'。"

  - name: "GAE baseline comparison"
    plan_id: "plan_003b"
    description: "GAE(λ=0.95,γ=1.0) 和 GAE(λ=1.0,γ=1.0) vs episode-level GRPO, 15 steps × 3 seeds"
    expected_results:
      gae_095_mean_success: 0.40
      gae_095_std: 0.05
      gae_100_mean_success: 0.37
      gae_100_std: 0.04
      episode_grpo_mean_success: 0.32
      episode_grpo_std: 0.05
      gae_095_vs_episode_delta: 8
      gae_100_vs_episode_delta: 5
      step_independent_mean_success: 0.03
    result_rationale: "Median 档定义 GAE vs episode-level delta 为 5-15pp，这里 GAE(0.95) 领先 8pp。GAE 能做 per-token credit assignment（通过 critic），而 episode-level GRPO 给所有 token 同一 advantage。在 30-step episode 中，GAE 能区分 'step 5 的 go to drawer 是好的' vs 'step 20 的 random action 是差的'，而 GRPO 无法区分。但 GAE 优势有限（非 dramatic）因为：(1) critic 在 1.7B 模型上估计 V(s) 噪声大（multi-turn text state 难以准确估值），(2) ALFWorld 的 reward 仍是 binary sparse，critic bootstrapping 在 sparse reward 下不稳定。GAE(λ=1.0) 接近 Monte Carlo（与 GRPO episode-level 语义相近但有 critic variance reduction），所以 delta 较小（5pp）。这个结果对 paper 是 double-edged：证明 per-token credit 有价值（GAE > GRPO），但也说明 episode-level GRPO 不是最优解。需要定位为 'minimum viable fix, not optimal'。"
    tables:
      - title: "Training method comparison at step 15 (3 seeds)"
        columns: ["method", "val_success", "std", "vs step-ind delta"]
        rows:
          - ["Step-independent (h=2)", "3±2%", "2pp", "baseline"]
          - ["Step-independent (h=10)", "18±4%", "4pp", "+15pp"]
          - ["Episode-level GRPO", "32±5%", "5pp", "+29pp"]
          - ["GAE(λ=1.0, γ=1.0)", "37±4%", "4pp", "+34pp"]
          - ["GAE(λ=0.95, γ=1.0)", "40±5%", "5pp", "+37pp"]
    figures_description:
      - "Figure: Bar chart with error bars. Clear ordering: step-ind << episode-GRPO < GAE. Annotation: 'per-token credit provides additional 5-8pp over episode-level'."
    analysis: "GAE 优势证实 per-token credit assignment 有额外价值，这削弱了 'episode-level 就够了' 的 strong claim。Paper 需要 reframe：episode-level 是 zero-cost fix（无需 critic 实现），GAE 是 upper bound 但需要额外 engineering（critic head + training stability）。Diagnostic 贡献不受影响——两者都远超 step-independent，证明 dual mechanism 是真正的 failure mode。"

  - name: "Episode-level + valid_action_bonus plateau-breaker"
    plan_id: "plan_003c"
    description: "Episode-level + valid_action_bonus=0.05, 15 steps"
    expected_results:
      success_rate_step15: 0.34
      action_is_valid_step15: 0.72
      valid_bonus_reward_ratio: 0.15
      no_gaming_detected: true
      vs_vanilla_episode_delta: 4
    result_rationale: "Median 档下 episode-level 本身 plateau 在 30-34%。加 valid_action_bonus 后：(1) 不发生 gaming（exp013f 的 gaming 是 step-independent-specific，因为 per-window 优化可以独立 maximize bonus 而忽略 task reward；episode-level 下 bonus 只是 total trajectory reward 的一小部分），(2) action_is_valid 从 55% 提升到 72%（学会更好的 format 但未达 80% target），(3) success 从 30% 提升到 34%（小幅改善，breaking plateau 效果有限）。原因：valid action 是 necessary but not sufficient for success——模型已经学到了大部分 valid action pattern，剩余的 failure 来自 exploration strategy 而非 format 错误。Bonus 帮助但不足以突破根本性的 exploration bottleneck。"
    tables:
      - title: "Valid action bonus effect (episode-level)"
        columns: ["metric", "vanilla", "+bonus", "delta"]
        rows:
          - ["val_success", "30.6%", "34.4%", "+3.8pp"]
          - ["action_is_valid", "57.3%", "72.1%", "+14.8pp"]
          - ["reward_mean", "3.06", "4.12", "+1.06"]
          - ["gaming_detected", "no", "no", "-"]
    figures_description: []
    analysis: "Confirms D056 insight: dense reward gaming 是 step-independent-specific。但 success 提升有限（+4pp），不足以单独作为 plateau-breaker。可能需要组合其他方法（如 curriculum 或 Self-Guide reward）来突破 40%。作为 ablation 有价值但非 main story。"

  - name: "Credit assignment mechanism empirical verification"
    plan_id: "plan_004"
    description: "Per-window advantage logging from h=2 runs, sign/magnitude analysis"
    expected_results:
      sign_vs_outcome_correlation: 0.87
      sign_vs_local_quality_correlation: 0.12
      magnitude_position_decay_r2: 0.75
      episode_level_sign_variance: 0.0
      episode_level_magnitude_variance: 0.02
      success_episodes_all_positive_pct: 0.92
      failure_episodes_all_negative_pct: 0.89
      gamma_k_fit_coefficient: 0.93
    result_rationale: "Median 档定义 sign-outcome correlation 0.80-0.95，取 0.87。不完美（非 1.0）的原因：(1) GRPO 的 group normalization 引入噪声——同一 group 内如果有多个 success episodes，normalization 后部分 success episode 的 advantage 可能为负（因为相对排名），(2) 极短 episode（2-3 步就成功/失败）中 window 数太少，统计不稳定。Sign vs local quality correlation = 0.12（非零但弱），因为存在 confound：好的 local actions 确实倾向于出现在成功 episode 中（相关但非因果），但这种 correlation 远弱于 sign-outcome correlation（0.87 vs 0.12）。Magnitude decay R²=0.75 而非更高，因为 reward normalization 和 group composition 增加了 position-magnitude 关系的噪声。Episode-level 下 variance 为 0（by design，所有 token 同一 advantage）。"
    tables:
      - title: "Mechanism verification results"
        columns: ["metric", "observed", "theory predicts", "interpretation"]
        rows:
          - ["sign↔outcome r", "0.87", "~1.0", "Direction mostly correct, noise from GRPO normalization"]
          - ["sign↔local_quality r", "0.12", "~0.0", "Weak confound exists but not causal"]
          - ["γ^k decay R²", "0.75", "high", "Magnitude decays with position, moderate fit"]
          - ["episode-level sign var", "0.0", "0.0", "No position-dependent sign (by design)"]
          - ["success→all positive", "92%", "100%", "GRPO group norm creates exceptions"]
          - ["failure→all negative", "89%", "100%", "Same GRPO norm effect"]
    figures_description:
      - "Figure 2a: Scatter plot of (episode_outcome, advantage_sign) for 500 windows from h=2 runs. Clear clustering but ~10% of points in 'wrong' quadrant. Color by position."
      - "Figure 2b: Advantage magnitude vs window position (normalized). Fitted γ^k curve overlaid. R²=0.75 annotated."
      - "Figure 2c: Episode-level control — flat line (all tokens same advantage), demonstrating absence of sign/magnitude variation."
    analysis: "Core mechanism confirmed but with noise: sign misattribution 方向正确（r=0.87）但非 deterministic。Paper 需要用 'predominantly determined by' 而非 'entirely determined by'。Partial correlation with local quality (0.12) means a reviewer could argue 'some useful signal gets through' — defense: 0.12 vs 0.87 shows signal is overwhelmed by outcome-driven noise，且 gradient direction (reinforce/suppress) 仍主要由 outcome 决定。这对 diagnostic contribution 足够，但需要 careful language。"

  - name: "Action-change statistics from always-on runs"
    plan_id: "plan_005"
    description: "Collect action-change rates from exp029 checkpoints"
    expected_results:
      overall_action_change_rate: 0.28
      confirmatory_rate: 0.72
      action_change_success_correlation: 0.15
      per_task_put_change_rate: 0.22
      per_task_clean_change_rate: 0.31
      per_task_heat_change_rate: 0.35
      per_task_examine_change_rate: 0.38
      early_step_change_rate: 0.35
      late_step_change_rate: 0.20
    result_rationale: "Median 档下 episode-level 训练到 30% success，模型的 verification 质量中等。Action-change rate 28%（72% confirmatory）因为：(1) 模型 confidence 中等——不像 untrained 模型那样 always change，也不像 strong model 那样 rarely change，(2) 30% success 意味着大部分 trajectory 仍在失败，verification 后模型倾向于保持原有 plan（因为没学到更好的替代）。Correlation 0.15（低于 strong 档的 0.3+）因为 action change 有时是 noise（模型 uncertain 时随机切换）而非 informed correction。Per-task 差异：complex tasks（examine, heat）change 率高因为 action space 更大、uncertainty 更高。"
    tables:
      - title: "Action-change statistics by task type"
        columns: ["task_type", "change_rate", "change→success_rate", "no_change→success_rate"]
        rows:
          - ["put", "22%", "35%", "28%"]
          - ["clean", "31%", "30%", "25%"]
          - ["heat", "35%", "33%", "22%"]
          - ["cool", "30%", "32%", "24%"]
          - ["examine", "38%", "28%", "18%"]
          - ["overall", "28%", "32%", "25%"]
    figures_description:
      - "Figure: Stacked bar showing confirmatory vs corrective verification per task type. Annotation: 72% of verifications do not change behavior."
    analysis: "Confirms hypothesis that most verification is confirmatory. Correlation with success (0.15) is positive but weak — this is the foundation for action-change reward but the weak signal means selective verification training will be noisy. Need to acknowledge this limitation upfront."

  - name: "B-IAVR selective verification training"
    plan_id: "plan_007"
    description: "Episode-level GRPO with verify/skip decision, action-change reward"
    expected_results:
      final_success_rate: 0.27
      verification_rate: 0.68
      verification_rate_reduction: 0.32
      success_delta_vs_always_on: -5
      training_steps_to_converge: 40
      reward_convergence: "noisy plateau after step 25"
      action_is_valid: 0.65
    result_rationale: "Median 档定义 selective verification rate ↓20-40%，取 32%。Success delta 为 -5pp（3-8pp 范围内）。原因：(1) action-change reward signal 本身较弱（correlation 0.15），训练 selective policy 的信号不 clean，(2) 模型在 'should I verify?' 决策上学到了粗糙的 heuristic（如 'verify after go to X'）但没学到精细的 uncertainty estimation，(3) 减少 32% verification 意味着在一些 informative verification 场景也错误跳过了，导致 5pp success drop。训练过程 noisy（action-change reward 的方差大），convergence 慢。这是 'preliminary evidence' 而非 'strong demonstration' — 够写一段 results 但不够支撑 strong claim。"
    tables:
      - title: "B-IAVR training trajectory"
        columns: ["step", "success", "verify_rate", "cost_tokens"]
        rows:
          - ["0", "30%", "100%", "1.0x"]
          - ["10", "28%", "85%", "0.88x"]
          - ["20", "26%", "74%", "0.78x"]
          - ["30", "27%", "70%", "0.74x"]
          - ["40", "27%", "68%", "0.72x"]
    figures_description:
      - "Figure: Dual-axis plot showing success rate (left, relatively flat ~27%) and verification rate (right, declining from 100% to 68%). Trade-off visible."
    analysis: "Verification rate 下降 32% 但 success 也下降 5pp。这不是 'free lunch' — 是 explicit trade-off。Claim 3 需要大幅降级：从 'matches always-on at reduced cost' 变为 'achieves moderate cost reduction with modest performance sacrifice'。作为 preliminary application 可接受但不是 paper 的 selling point。"

  - name: "Selective verification full comparison"
    plan_id: "plan_008"
    description: "Always-on / B-IAVR / no-verify / random-p / confidence baseline comparison"
    expected_results:
      always_on_success: 0.31
      biavr_success: 0.27
      no_verify_success: 0.22
      random_p50_success: 0.26
      confidence_threshold_success: 0.25
      always_on_verify_rate: 1.0
      biavr_verify_rate: 0.68
      random_p50_verify_rate: 0.50
      confidence_verify_rate: 0.55
      biavr_cost_reduction: 0.28
    result_rationale: "Median 档下各 baseline 表现：(1) No-verify 比 always-on 低 9pp（verification 有 value 但不 dramatic），(2) Random-p50 在 50% verify rate 下只丢 5pp（说明 selective 的 marginal value 有限——random 就能保留大部分 benefit），(3) Confidence threshold 与 random 接近（model confidence 不是 good proxy for informativeness at 30% success level）。B-IAVR 优于 random 和 confidence 但优势小（1-2pp at matched cost），因为 action-change signal 本身 noisy。Pareto frontier analysis 中 B-IAVR 不 clearly dominate——接近 random baseline 的 performance。这削弱了 Claim 3 的独立贡献。"
    tables:
      - title: "Full comparison on held-out val set"
        columns: ["method", "success", "verify_rate", "rel_cost", "success/cost"]
        rows:
          - ["always-on", "31%", "100%", "1.00", "0.31"]
          - ["B-IAVR", "27%", "68%", "0.72", "0.375"]
          - ["random-p=0.5", "26%", "50%", "0.55", "0.473"]
          - ["confidence-thresh", "25%", "55%", "0.60", "0.417"]
          - ["no-verify", "22%", "0%", "0.45", "0.489"]
    figures_description:
      - "Figure: Pareto plot (x=cost, y=success). B-IAVR slightly above random/confidence curve but not dramatically. Always-on is upper-right anchor."
    analysis: "B-IAVR 在 absolute Pareto efficiency 上优于 baselines 但 margin 小。Random baseline 意外 competitive，说明 'when to verify' 的 learned signal 价值有限 at this performance level。Paper 需要 downplay Claim 3 到 'preliminary evidence that learned selective policy outperforms naive baselines' level。可能需要 Plan B（更强 base agent）才能让 selective verification story 有说服力。"

  - name: "No-verify ablation"
    plan_id: "plan_009"
    description: "Episode-level GRPO without self-verification, lower bound"
    expected_results:
      success_rate: 0.22
      action_is_valid: 0.58
      vs_always_on_delta: -9
      avg_episode_length: 18
    result_rationale: "No-verify 比 always-on 低 9pp（median 档 expectation）。Verification 的主要价值在于 error recovery——检测并修正 invalid/ineffective actions。在 30% success 的 agent 中，roughly 1/3 的 success 来自 verification-triggered correction（30% × 0.3 ≈ 9pp contribution）。但 delta 只有 9pp 而非更大，因为：(1) 72% verification 是 confirmatory（不改变行为），(2) 部分 action change 是 noise 而非 correction，(3) 一些任务不需要 verification 就能完成（simple pick tasks）。这验证了 verification 有 value 但也说明 always-on 的 inefficiency（72% 浪费）。"
    tables: []
    figures_description: []
    analysis: "9pp delta 证明 verification 有 non-trivial value，支撑了 selective verification 的 motivation。但 delta 不够大（<10pp），使 cost-saving story 的 potential 有限——即使完美 selective，最多能恢复 9pp 中的大部分。"

  - name: "Entropy-controlled action-change analysis"
    plan_id: "plan_010"
    description: "Partial correlation of action-change with success after controlling for policy entropy"
    expected_results:
      raw_correlation: 0.15
      partial_correlation_entropy_controlled: 0.11
      p_value: 0.038
      high_entropy_stratum_correlation: 0.08
      low_entropy_stratum_correlation: 0.14
      medium_entropy_stratum_correlation: 0.12
    result_rationale: "Median 档定义 action-change partial correlation 0.10-0.20，取 0.11 after controlling entropy。Raw correlation 从 0.15 降到 0.11（entropy 解释了部分 variance，说明 high-entropy states 确实倾向于产生 action change 而非 informed correction）。P-value 0.038 刚过 significance threshold 但不 compelling（reviewer 可能要求 Bonferroni correction 后不再 significant）。Low-entropy stratum correlation 更高（0.14）说明在 confident states 中 action change 更可能是 informative signal，而 high-entropy 中更可能是 noise。这是 partial defense 但不是 strong evidence。"
    tables:
      - title: "Stratified correlation analysis"
        columns: ["entropy_stratum", "n", "action_change_rate", "correlation", "p_value"]
        rows:
          - ["low (<0.1)", "180", "18%", "0.14", "0.06"]
          - ["medium (0.1-0.3)", "250", "28%", "0.12", "0.05"]
          - ["high (>0.3)", "120", "42%", "0.08", "0.38"]
    figures_description:
      - "Figure: Three scatter plots (one per entropy stratum) showing action-change vs episode success. Regression lines with CI bands."
    analysis: "Signal exists but is weak and barely significant. Defense against 'action change = noise' is partial: can say 'signal persists after entropy control' but effect size is small. Honest paper would acknowledge this as limitation and position action-change as 'best available proxy' rather than 'validated signal'."

  - name: "Causal intervention: random vs verification-triggered changes"
    plan_id: "plan_011"
    description: "Inject random action changes vs verification-triggered, compare success"
    expected_results:
      verification_triggered_success: 0.32
      random_triggered_success: 0.24
      no_change_baseline_success: 0.28
      delta_triggered_vs_random: 8
      delta_triggered_vs_nochange: 4
    result_rationale: "Median 档下 verification-triggered changes 比 random changes 好 8pp。原因：verification 过程给 model 额外 context（重新审视 state），使得 change 更 informed。但 delta 只有 8pp 而非 15+pp（strong 档），因为：(1) 30% success agent 的 verification quality 中等（不是所有 verification-triggered change 都是 correct），(2) random change 有时碰巧也有用（ALFWorld action space 有限，random valid action 有 non-trivial hit rate），(3) 'no change baseline' 成功率 28% 意味着很多 episodes 不需要 correction 就能 succeed/fail。Interesting finding: triggered > no-change > random? No — triggered > no-change, random < no-change. Random changes 实际上 hurt（从 28% → 24%），verification-triggered 才是 helpful。"
    tables:
      - title: "Causal intervention results"
        columns: ["condition", "success_rate", "n_episodes", "vs_baseline"]
        rows:
          - ["verification-triggered change", "32%", "200", "+4pp"]
          - ["no change (baseline)", "28%", "200", "—"]
          - ["random change (same rate)", "24%", "200", "-4pp"]
    figures_description:
      - "Figure: Bar chart with confidence intervals. Verification-triggered > baseline > random. Stars for significance."
    analysis: "Provides causal evidence that verification adds value (not just noise). But effect size moderate (+4pp vs baseline, +8pp vs random). Combined with entropy analysis, forms a 'converging evidence' argument for action-change being a real signal, even if weak individually."

  - name: "Reward signal ablation"
    plan_id: "plan_012"
    description: "B-IAVR with action-change vs random-trigger vs confidence-based reward"
    expected_results:
      action_change_success: 0.27
      action_change_verify_rate: 0.68
      random_trigger_success: 0.25
      random_trigger_verify_rate: 0.62
      confidence_reward_success: 0.24
      confidence_verify_rate: 0.70
    result_rationale: "Median 档下 action-change reward 优于 alternatives 但 margin 小。Action-change (27%, verify 68%) vs random-trigger (25%, verify 62%) delta = 2pp success, +6pp verify rate。原因：(1) random trigger reward 无 informative signal，模型学到的 verify 策略接近 uniform random，(2) confidence-based reward 在 1.7B model 上不好估计（model 的 logit calibration 差，confidence 不 correlate well with actual uncertainty），(3) action-change 虽然 noisy 但至少有 partial signal（r=0.11）。Margin 小因为 base signal 本身弱——在 strong 档下差异会更明显。"
    tables:
      - title: "Reward signal comparison"
        columns: ["reward_type", "success", "verify_rate", "cost_reduction", "training_stability"]
        rows:
          - ["action-change (ours)", "27%", "68%", "28%", "moderate (converges step 40)"]
          - ["random trigger", "25%", "62%", "35%", "unstable (high variance)"]
          - ["confidence-based", "24%", "70%", "26%", "slow convergence"]
    figures_description: []
    analysis: "Action-change is best but advantage is modest (2-3pp). Paper can claim 'action-change outperforms baselines' but the weak margin means a reviewer could argue the differences are within noise. Need to frame carefully with error bars and multiple seeds."

  - name: "ARES reproduction + comparison"
    plan_id: "plan_013"
    description: "Reproduce ARES SFT router on ALFWorld, head-to-head with B-IAVR"
    expected_results:
      ares_success: 0.26
      ares_verify_rate: 0.58
      ares_cost_reduction: 0.38
      biavr_success: 0.27
      biavr_verify_rate: 0.68
      biavr_cost_reduction: 0.28
      delta_success: 1
      delta_cost: -10
    result_rationale: "ARES 使用 SFT router（从 oracle labels 学 when to verify），在 cost reduction 上优于 B-IAVR（38% vs 28%）但 success 相近（26% vs 27%）。原因：(1) SFT 有 direct supervision signal（teacher-labeled 'should verify here'），训练更 clean，(2) 但 SFT labels 是 frozen（从一个 checkpoint 生成），不 adapt to policy improvement，所以 success 不如 RL-trained 的 B-IAVR，(3) ARES 的 continuous effort allocation 在 ALFWorld binary 场景中退化为 threshold，效果有限。Head-to-head 中 B-IAVR 不 clearly dominate ARES — 不同 trade-off point。这削弱了 'B-IAVR dominates' 的 claim。"
    tables:
      - title: "ARES vs B-IAVR head-to-head"
        columns: ["method", "success", "verify_rate", "cost_reduction", "training_data_needed"]
        rows:
          - ["ARES (SFT router)", "26%", "58%", "38%", "oracle labels required"]
          - ["B-IAVR (RL)", "27%", "68%", "28%", "no labels (self-supervised)"]
          - ["always-on", "31%", "100%", "0%", "—"]
    figures_description:
      - "Figure: Pareto plot with ARES and B-IAVR as labeled points. Neither dominates the other — ARES better on cost, B-IAVR better on success."
    analysis: "ARES comparison doesn't favor our method on cost reduction. Differentiation must come from methodology (no oracle labels needed, RL-based adaptation) rather than performance numbers. Paper should frame as 'comparable performance without supervision' rather than 'superior performance'."

  - name: "ScienceWorld transfer"
    plan_id: "plan_014"
    description: "Episode-level vs step-independent on ScienceWorld environment"
    expected_results:
      episode_level_success: 0.18
      step_independent_success: 0.04
      improvement_ratio: 4.5
      episode_level_std: 0.05
      convergence_slower: true
      steps_to_plateau: 25
    result_rationale: "Median 档下 transfer 到 ScienceWorld 仍显示 episode-level 优势（4.5x）但 absolute performance 较低（18% vs ALFWorld 的 30%）。原因：(1) ScienceWorld 比 ALFWorld 更复杂（更长 episode、更大 action space、partial observability），(2) 1.7B 模型在 science reasoning 上能力有限，(3) step-independent 在更长 horizon（ScienceWorld 40-50 步）下崩溃更严重（4% vs ALFWorld 的 3%），(4) 收敛更慢因为 reward 更 sparse。Results 支持 generalization claim 但 18% absolute performance 不算 impressive。"
    tables:
      - title: "ScienceWorld transfer results"
        columns: ["method", "success_rate", "improvement_vs_step_ind"]
        rows:
          - ["step-independent (h=2)", "4%", "baseline"]
          - ["step-independent (h=10)", "9%", "2.3x"]
          - ["episode-level GRPO", "18%", "4.5x"]
    figures_description:
      - "Figure: Learning curves for episode-level vs step-independent on ScienceWorld. Slower convergence but same qualitative pattern as ALFWorld."
    analysis: "Supports generalization: dual mechanism failure is not ALFWorld-specific. But low absolute numbers (18%) limit the impact claim. Paper can use this as 'consistent across environments' evidence for Claim 1 diagnostic."

  - name: "7B model scaling verification"
    plan_id: "plan_015"
    description: "Episode-level vs step-independent on Qwen3-7B"
    expected_results:
      episode_7b_success: 0.42
      step_ind_7b_success: 0.08
      improvement_ratio: 5.25
      episode_7b_vs_1.7b_delta: 10
      step_ind_7b_vs_1.7b_delta: 5
    result_rationale: "Median 档下 7B 模型 episode-level 达到 42%（vs 1.7B 的 32%），step-independent 仍 collapse 到 8%（vs 1.7B 的 3%，7B 有更好 base capabilities 所以 collapse 后仍保留一些）。Episode-level 的 10pp 提升来自 larger model 的 better base reasoning/planning。Step-independent 的 slight improvement（8% vs 3%）因为 7B 在短 window 内也能做更好的 local decisions，但 sign misattribution 仍然阻止真正的 improvement。Key finding: scaling 不能 fix step-independent 的 structural problem（8% 仍远低于 episode-level 的 42%）。"
    tables:
      - title: "Model size scaling"
        columns: ["model", "episode-level", "step-ind (h=2)", "ratio"]
        rows:
          - ["Qwen3-1.7B", "32%", "3%", "10.7x"]
          - ["Qwen3-7B", "42%", "8%", "5.3x"]
    figures_description:
      - "Figure: 2x2 comparison (model size × training method). Episode-level scales well; step-independent remains broken regardless of size."
    analysis: "Supports Claim 1: step-independent failure is structural, not a model capacity issue. 7B cannot compensate for broken credit assignment. Episode-level benefits from scale as expected. Ratio decreases (10.7x→5.3x) but absolute gap increases (29pp→34pp)."

  - name: "Per-task-type breakdown"
    plan_id: "plan_016"
    description: "ALFWorld success breakdown by task type for episode-level"
    expected_results:
      put_success: 0.40
      clean_success: 0.32
      heat_success: 0.28
      cool_success: 0.30
      examine_success: 0.18
      pick_two_success: 0.15
      correlation_with_length: -0.72
      short_task_advantage: 12
    result_rationale: "Median 档下 per-task 差异明显：simple tasks（put: 40%）远好于 complex tasks（examine: 18%, pick_two: 15%）。原因：(1) 短 episode tasks（put 通常 10-15 步）在 episode-level 下 credit assignment 更 focused（fewer actions dilute the signal），(2) Complex tasks 需要 multi-step planning（先找 object、再找 tool、再执行），30% overall success 的 agent 在需要 3+ correct decisions 的 task 上 success 急剧下降，(3) pick_two 需要 remember 两个 target objects——working memory challenge for 1.7B。Length-success correlation -0.72 confirms episode complexity is key difficulty factor。"
    tables:
      - title: "Per-task breakdown (episode-level, step 15)"
        columns: ["task_type", "success", "avg_steps", "action_is_valid", "n_val"]
        rows:
          - ["put", "40%", "12.3", "62%", "10"]
          - ["clean", "32%", "18.7", "55%", "6"]
          - ["cool", "30%", "16.2", "58%", "4"]
          - ["heat", "28%", "17.8", "53%", "4"]
          - ["examine", "18%", "24.5", "48%", "3"]
          - ["pick_two", "15%", "28.1", "45%", "5"]
    figures_description:
      - "Figure: Scatter plot of task avg_steps vs success_rate with fitted regression line. Clear negative correlation (-0.72)."
    analysis: "Confirms intuition: episode-level advantage is largest for simpler tasks where credit can be assigned more cleanly. Complex tasks remain challenging even with episode-level training — potential direction for future work (hierarchical RL or subgoal decomposition). Useful for paper's 'limitation' section."
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a18d7c3e-badc-4812-b08c-29df3525bbb5",
  "isSidechain": false,
  "requestId": "req_011Cb88XsorXc4Yc1ignnTY5",
  "type": "assistant",
  "uuid": "b1849e26-0570-4ece-8f78-6d63cbc43ced",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1",
  "sessionId": "5d38cf08-9b48-449e-b610-0e2b32e2d744",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014FNUVaqZCzdNh8L7AMCE1P",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 20477,
      "cache_read_input_tokens": 11841,
      "output_tokens": 11600,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20477,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 11600,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 20477,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20477
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Episode-level 训练有效但 plateau 在 30-40%，双机制理论基本成立但部分指标有噪声，selective verification 初步可行但不够 clean——需要 reweight 贡献重心到 diagnostic 侧 核心假设：[\"Episode-level GRPO 收敛到…",
  "leafUuid": "b1849e26-0570-4ece-8f78-6d63cbc43ced",
  "sessionId": "5d38cf08-9b48-449e-b610-0e2b32e2d744"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Diagnosing multi-turn LLM agent RL: why step-independent fails",
  "sessionId": "5d38cf08-9b48-449e-b610-0e2b32e2d744"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Episode-level 训练有效但 plateau 在 30-40%，双机制理论基本成立但部分指标有噪声，selective verification 初步可行但不够 clean——需要 reweight 贡献重心到 diagnostic 侧 核心假设：[\"Episode-level GRPO 收敛到…",
  "leafUuid": "b1849e26-0570-4ece-8f78-6d63cbc43ced",
  "sessionId": "5d38cf08-9b48-449e-b610-0e2b32e2d744"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Diagnosing multi-turn LLM agent RL: why step-independent fails",
  "sessionId": "5d38cf08-9b48-449e-b610-0e2b32e2d744"
}
```

---
