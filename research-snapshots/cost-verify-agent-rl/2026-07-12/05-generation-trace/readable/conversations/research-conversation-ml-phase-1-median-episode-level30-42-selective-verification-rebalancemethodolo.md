# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：Episode-level收敛至30-42%，selective verification效果有限，需rebalance为methodology-h

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/79f9012f-eb35-4e80-8e55-564c1bc1b0c2.jsonl`
- **Structured JSON:** [`4d56b1cb931bcd4df746.json`](../../sessions/4d/4d56b1cb931bcd4df746.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T23:58:44.668Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T23:58:44.668Z",
  "sessionId": "79f9012f-eb35-4e80-8e55-564c1bc1b0c2",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：Episode-level收敛至30-42%，selective verification效果有限，需rebalance为methodology-heavy paper\n核心假设：['Episode-level训练收敛但未大幅超过40%阈值（borderline区间）', 'h-sweep大体展示预期趋势但存在噪声（某些h值不完全单调）', 'Selective verification可训练但cost-performance tradeoff不dramatic', 'Action-change signal存在但correlation moderate（r=0.15-0.25）', 'Multi-seed有一定variance（std 5-8pp）']\n关键指标范围：{'episode_level_success_rate': [30, 42], 'step_independent_baseline': [0, 6], 'h_sweep_cliff_threshold': [3, 8], 'selective_verification_rate_reduction': [15, 35], 'selective_vs_always_on_success_delta_pp': [3, 8], 'action_change_confirmatory_rate_pct': [55, 75], 'multi_seed_std_pp': [5, 8], 'action_is_valid': [85, 93]}\n叙事方向：Rebalance为70% training methodology + 30% selective verification。Claim 1保持strong（episode vs step-independent的gap仍然dramatic），但Claim 2+3降级为'preliminary evidence'或'proof-of-concept'。Paper主打：episode-level training是被忽视的关键设计选择，selective verification作为downstream application demo而非co-equal contribution。需要加厚Phase C ablation（h-sweep做得更细、mechanism analysis更深）来补偿Phase B的弱结果。Title可能调整为更强调methodology。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: cost-verify-agent-rl\nfocus: Evaluate dual contribution (episode-level training methodology + selective verification). Key uncertainty: will episode-level training converge high enough (≥40%) to support cost-efficiency story? Is the episode-level insight novel enough standalone?\n\n## paper_framing.md\n\n# Paper Framing — Learning When to Verify: RL-Trained Selective Self-Verification for Interactive Agents\n\n> Post-MVP 重写 (2026-05-16) | 基于 D053 MVP 通过 + Reviewer 建议\n\n## Core Insight\n\nMulti-turn interactive agents 的 self-verification 大部分是 confirmatory（不改变行为）而非 corrective。但要训练 agent 学会 selective verification，首先需要解决一个被忽视的训练方法论问题：**step-independent RL 在长 horizon 任务中因 credit assignment decay (gamma^(T-h) → 0) 而灾难性崩溃**。Episode-level training 是前提条件。在此基础上，action-change 作为 intrinsic reward signal 训练 selective verification policy。\n\n## Story Arc\n\n**Dual contribution**: Training methodology + Selective verification system\n\n叙事线：\n1. Self-verification 对 interactive agents 有用，但 always-on 成本高\n2. 训练 agent 学 WHEN to verify 是自然方向 → 但现有 step-independent RL 框架在多轮任务上失败\n3. 我们发现根因是 credit assignment decay，提出 episode-level GRPO 解决\n4. 在此基础上，用 action-change 作为 verification informativeness 的 reward，训练 selective policy\n5. 结果：near-always-on performance + 显著降低 verification cost\n\n## Target Venue\n\n待定（NeurIPS 2026 / EMNLP 2026 / ICLR 2026），取决于实验进度和最终效果。\n\n## Core Claims\n\n### Claim 1 (strength: strong): Episode-level credit assignment is critical for RL training of multi-turn agents\n- 所需证据：episode-level vs step-independent 对比，不同 h 值的 ablation，mechanistic 分析\n- 当前证据状态：**ESTABLISHED** (exp029 step5 val=25% vs exp028c step10 val=0%)\n- 强度依据：2x baseline vs catastrophic collapse，机制清晰（gamma^49=7.7%）\n\n### Claim 2 (strength: moderate): Action-change is an effective intrinsic reward for verification informativeness\n- 所需证据：selective verification 训练收敛 + action-change vs random/confidence baselines\n- 当前证据状态：**not yet established**，依赖 Phase B 实验\n- 前提：episode-level 训练的 agent 需达到 ≥40% success 才有意义\n\n### Claim 3 (strength: moderate): Learned selective policy matches always-on performance at reduced verification cost\n- 所需证据：B-IAVR verification ↓40%+ 且 success delta < 3pp vs always-on\n- 当前证据状态：**not yet established**，依赖 Phase B + C\n- 前提：Claim 1 的 agent 需足够强\n\n## Contingency Plan\n\n如果 episode-level 训练收敛后 success 仍 < 40%（不足以支撑 cost-efficiency story）：\n- **Plan A**（首选）：paper 变为 pure training methodology contribution — \"Episode-Level RL for Multi-Turn Agents: Why Step-Independent Fails and How to Fix It\"\n- **Plan B**：加更多 ablation 深挖 episode-level training（context window size sweep, reward shaping, curriculum），做 analysis paper\n- 不考虑 downgrade venue\n\n## Reviewer Attack Surface + Defense\n\n| # | Concern | Severity | Defense Experiment |\n|---|---------|----------|--------------------|\n| 1 | \"Episode-level RL is obvious / well-known\" | HIGH | Context window ablation (h=2,5,10,20,full) 展示 non-trivial threshold + 机制分析 + 展示现有 LLM-agent 工作(RAGEN等)默认 step-independent |\n| 2 | Single environment (ALFWorld) | MEDIUM | 加 ScienceWorld / WebShop (if resources permit) |\n| 3 | Small model (1.7B) | MEDIUM | 定位 resource-constrained; 加 7B 验证 (if GPU available) |\n| 4 | Action-change = noise vs signal | MEDIUM | Entropy-controlled analysis + causal intervention (Phase B) |\n| 5 | Selective verification 效果不够 significant | MEDIUM | 多 baseline 对比 (always-on / no-verify / random-p / confidence-threshold / ARES) |\n| 6 | 与 ARES 差异化不足 | LOW | 实验直接对比 + 方法论差异表 (SFT router vs RL policy, continuous vs binary) |\n\n## Evidence Status Matrix\n\n| Claim | MVP Evidence | Research Evidence Needed | Priority |\n|-------|-------------|--------------------------|----------|\n| Claim 1 | exp029 vs exp028c (25% vs 0%) | h-value ablation, multi-seed, mechanism paper figure | P0 |\n| Claim 2 | N/A | Phase B full implementation | P1 |\n| Claim 3 | N/A | Phase B + C comparison suite | P1 |\n\n## Competitive Positioning\n\n| System | Method | ALFWorld | Key Difference |\n|--------|--------|----------|---------------|\n| Self-Guide (2026) | Always-on verification | 72.7% (1.7B) | We add selectivity via RL |\n| ARES (2603.07915) | SFT router, continuous effort | 52.7% token↓ | SFT vs RL, continuous vs binary |\n| Thinkless (NeurIPS'25) | RL control token | reasoning | Same RL philosophy, different domain |\n| ReflAct (EMNLP'25) | Prompting GPT-4 | 93.3% | Different scale/approach |\n| RAGEN (2025) | GRPO for agents | varies | Step-independent default — our baseline |\n\n## Research Phases\n\n1. **Phase A (DONE)**: Episode-level GRPO training — MVP passed, demonstrates Claim 1\n2. **Phase A+**: Continue training to convergence (target ≥40% success), deploy tatsu parallel patch, multi-seed\n3. **Phase B**: Implement selective verification with action-change reward — Claim 2 & 3\n4. **Phase C**: Ablation suite — context window sweep, reward ablations, baseline comparisons\n5. **Phase D**: (Conditional on resources) Multi-env / multi-model scaling\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  title: Episode-level GRPO convergence (exp029 continuation)\n  claim: Claim 1\n  phase: A+\n  priority: P0\n  depends_on: []\n  registry_id: exp029_episode_level\n  status: DONE\n  description: 'Episode-level GRPO (context_window_mode: full) on Qwen3-1.7B + ALFWorld.\n    50 steps, dual-GPU. MVP passed at step 5 (val=25%, 2x baseline 12.5%). Continue\n    to convergence (step 20+) with tatsu parallel patch for 4x val speedup.\n\n    '\n  hypothesis: 'Episode-level training enables stable RL for multi-turn agents, reaching\n    ≥40% success by convergence.\n\n    '\n  metrics:\n  - success_rate\n  - action_is_valid\n  - kl_divergence\n  - entropy\n  gpu_hours_estimate: 48\n  framing_ref: claim_1\n  conclusion: failed\n- id: plan_002\n  title: Context window h-sweep ablation\n  claim: Claim 1\n  phase: A+\n  priority: P0\n  depends_on:\n  - plan_001\n  registry_id: null\n  status: planned\n  description: 'Sweep context_window h={2, 5, 10, 20, full} on same GRPO config. KEY\n    paper figure: shows credit assignment threshold is not binary (h=2 catastrophic,\n    intermediate h partial, full best). Mechanistic analysis: plot effective discount\n    gamma^(T-h) vs performance. Addresses Reviewer Concern #1 (\"episode-level is obvious\").\n\n    '\n  hypothesis: 'Performance degrades monotonically with smaller h, with sharp cliff\n    below h=10 where gamma^(T-h) < 0.01 for most episodes.\n\n    '\n  metrics:\n  - success_rate_per_h\n  - convergence_speed\n  - collapse_rate\n  gpu_hours_estimate: 120\n- id: plan_003\n  title: Multi-seed replication (3 seeds)\n  claim: Claim 1\n  phase: A+\n  priority: P0\n  depends_on:\n  - plan_001\n  registry_id: null\n  status: planned\n  description: '2 additional seeds for exp029 episode-level config. Report mean ±\n    std. Critical for statistical credibility of all downstream comparisons.\n\n    '\n  hypothesis: 'Episode-level success rate is reproducible (std < 5pp across seeds).\n\n    '\n  metrics:\n  - success_rate_mean\n  - success_rate_std\n  gpu_hours_estimate: 96\n- id: plan_004\n  title: Credit assignment mechanism analysis (paper Figure 2)\n  claim: Claim 1\n  phase: A+\n  priority: P0\n  depends_on:\n  - plan_002\n  registry_id: null\n  status: planned\n  description: 'Compute and visualize: (a) effective discount gamma^(T-h) for each\n    h value, (b) gradient signal strength per training step under different h, (c)\n    correlation between episode length and performance drop under small h. Mostly\n    analysis/plotting, minimal GPU.\n\n    '\n  hypothesis: 'Shorter contexts produce exponentially weaker gradient signal, explaining\n    the catastrophic collapse pattern.\n\n    '\n  metrics:\n  - gradient_signal_strength\n  - discount_factor_curve\n  gpu_hours_estimate: 4\n- id: plan_005\n  title: Action-change statistics from always-on runs\n  claim: Claim 2\n  phase: B\n  priority: P1\n  depends_on:\n  - plan_001\n  registry_id: null\n  status: planned\n  description: 'Collect action-change statistics from exp029 trained checkpoints:\n    (1) fraction of verifications triggering action change, (2) correlation between\n    action change and episode success, (3) per-task-type breakdown. Informs reward\n    design and provides empirical grounding.\n\n    '\n  hypothesis: 'Most verifications are confirmatory (>60% no action change). Action\n    change positively correlates with episode success (r > 0.2).\n\n    '\n  metrics:\n  - action_change_rate\n  - correlation\n  - confirmatory_rate\n  gpu_hours_estimate: 4\n- id: plan_006\n  title: Selective verification implementation\n  claim: Claim 2\n  phase: B\n  priority: P1\n  depends_on:\n  - plan_005\n  registry_id: null\n  status: planned\n  description: 'Implement binary verify/skip decision in RAGEN framework. Agent outputs\n    special token (verify/skip) before each step. Reward = task_success + alpha *\n    action_change_when_verified - beta * verification_cost. Code-only, no GPU.\n\n    '\n  hypothesis: null\n  metrics: []\n  gpu_hours_estimate: 0\n- id: plan_007\n  title: B-IAVR selective verification training\n  claim: Claim 2, Claim 3\n  phase: B\n  priority: P1\n  depends_on:\n  - plan_006\n  - plan_001\n  registry_id: null\n  status: planned\n  description: 'Train selective verification policy via episode-level GRPO. Initialize\n    from best exp029 checkpoint. Action-change reward encourages verification only\n    when informative.\n\n    '\n  hypothesis: 'B-IAVR achieves verification rate ↓40%+ vs always-on while maintaining\n    success within 5pp of baseline.\n\n    '\n  metrics:\n  - success_rate\n  - verification_rate\n  - cost_reduction\n  gpu_hours_estimate: 96\n- id: plan_008\n  title: Selective verification full comparison\n  claim: Claim 3\n  phase: B\n  priority: P1\n  depends_on:\n  - plan_007\n  registry_id: null\n  status: planned\n  description: 'Compare on same val set: always-on / B-IAVR / no-verify / random-p\n    / confidence-threshold. Report success rate, verification rate, total inference\n    tokens, per-task breakdown.\n\n    '\n  hypothesis: 'B-IAVR dominates Pareto frontier (best success-to-cost ratio).\n\n    '\n  metrics:\n  - success_rate\n  - verification_rate\n  - cost_reduction\n  - total_tokens\n  gpu_hours_estimate: 8\n- id: plan_009\n  title: No-verify ablation\n  claim: Claim 3\n  phase: C\n  priority: P1\n  depends_on:\n  - plan_001\n  registry_id: null\n  status: planned\n  description: 'Episode-level GRPO without any self-verification. Lower bound: demonstrates\n    verification value.\n\n    '\n  hypothesis: 'Removing verification drops success by ≥10pp vs always-on.\n\n    '\n  metrics:\n  - success_rate\n  - action_is_valid\n  gpu_hours_estimate: 48\n- id: plan_010\n  title: Entropy-controlled action-change analysis\n  claim: Claim 2\n  phase: C\n  priority: P1\n  depends_on:\n  - plan_005\n  registry_id: null\n  status: planned\n  description: 'Defense for \"action change = noise\" concern. Stratify by policy entropy;\n    test if action-change-success correlation holds within each stratum.\n\n    '\n  hypothesis: 'Partial correlation remains significant (p < 0.05) after controlling\n    entropy.\n\n    '\n  metrics:\n  - partial_correlation\n  - p_value\n  gpu_hours_estimate: 4\n- id: plan_011\n  title: 'Causal intervention: random vs verification-triggered changes'\n  claim: Claim 2\n  phase: C\n  priority: P1\n  depends_on:\n  - plan_001\n  registry_id: null\n  status: planned\n  description: 'Inject random action changes at same rate as verification-triggered.\n    Compare task success. If verification-triggered >> random, causal evidence.\n\n    '\n  hypothesis: 'Verification-triggered changes yield ≥10pp higher success than random.\n\n    '\n  metrics:\n  - success_rate_triggered\n  - success_rate_random\n  - delta\n  gpu_hours_estimate: 8\n- id: plan_012\n  title: Reward signal ablation (action-change vs alternatives)\n  claim: Claim 2\n  phase: C\n  priority: P1\n  depends_on:\n  - plan_007\n  registry_id: null\n  status: planned\n  description: 'Train B-IAVR with alternative rewards: (a) action-change (ours), (b)\n    random trigger reward, (c) confidence-based reward. Demonstrates action-change\n    is the best signal.\n\n    '\n  hypothesis: 'Action-change reward produces best cost-performance tradeoff.\n\n    '\n  metrics:\n  - success_rate\n  - verification_rate\n  - cost_reduction\n  gpu_hours_estimate: 192\n- id: plan_013\n  title: ARES reproduction + comparison\n  claim: Claim 3\n  phase: C\n  priority: P1\n  depends_on:\n  - plan_007\n  registry_id: null\n  status: planned\n  description: 'Reproduce ARES SFT router on ALFWorld (same model). Head-to-head with\n    B-IAVR on identical eval episodes. Addresses \"ARES differentiation\" concern.\n\n    '\n  hypothesis: 'B-IAVR achieves ≥10pp better cost reduction than ARES at matched success.\n\n    '\n  metrics:\n  - success_rate\n  - verification_rate\n  - cost_reduction\n  gpu_hours_estimate: 24\n- id: plan_014\n  title: ScienceWorld transfer (episode-level advantage)\n  claim: Claim 1\n  phase: D\n  priority: P2\n  depends_on:\n  - plan_001\n  registry_id: null\n  status: planned\n  description: 'Validate episode-level vs step-independent on ScienceWorld. Different\n    env, similar multi-turn structure. Addresses single-env concern.\n\n    '\n  hypothesis: 'Episode-level advantage generalizes: ≥2x improvement over step-independent.\n\n    '\n  metrics:\n  - success_rate_episode\n  - success_rate_step_independent\n  gpu_hours_estimate: 72\n- id: plan_015\n  title: 7B model scaling verification\n  claim: Claim 1\n  phase: D\n  priority: P2\n  depends_on:\n  - plan_002\n  registry_id: null\n  status: planned\n  description: 'Episode-level vs step-independent on Qwen3-7B. Addresses model size\n    concern. May need cloud GPU.\n\n    '\n  hypothesis: 'Episode-level advantage holds at 7B scale.\n\n    '\n  metrics:\n  - success_rate_episode_7B\n  - success_rate_step_independent_7B\n  gpu_hours_estimate: 192\n  notes: May require cloud GPU rental (4x A100 or 2x H100)\n- id: plan_016\n  title: Per-task-type breakdown analysis\n  claim: Claim 1\n  phase: D\n  priority: P2\n  depends_on:\n  - plan_001\n  registry_id: null\n  status: planned\n  description: 'Breakdown by ALFWorld task type (pick, clean, heat, cool, examine,\n    pick_two). Shows within-environment diversity.\n\n    '\n  hypothesis: 'Episode-level advantage varies by task complexity; longer tasks benefit\n    more.\n\n    '\n  metrics:\n  - per_task_success\n  - episode_length_correlation\n  gpu_hours_estimate: 2\n\n\n## registry (completed experiments)\n\n- exp_id: exp_001\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001b\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_002\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_003\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_003_dryrun\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_003_dryrun2\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp003_dryrun3\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_003_dryrun3\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp003\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp005\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp007\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    steps_completed: 10\n    steps_planned: 30\n    crash_reason: 'OSError: No space left on device (/tmp)'\n    final_success_rate: 0.0625\n    final_action_is_valid: 0.0835\n    final_manager_invalid_action: 0.0156\n    final_pass_at_8: 0.375\n    final_pg_loss: 0.00117\n    final_ppo_kl: 0.00127\n    final_entropy: 0.057\n    final_score_mean: 0.578\n    dryrun_action_is_valid: 0.054\n    dryrun_invalid_action: 0.065\n    training_time_s: 6739\n- exp_id: exp007_dryrun\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp008\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp008_sft\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    action_is_valid: 0.9\n    format_ok: 1\n    success_rate: 0\n    final_loss: 0.069\n    final_token_accuracy: 0.973\n    data_count: 1200\n    epochs: 3\n    total_steps: 225\n    training_time_s: 576\n- exp_id: exp009\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp010\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    step: 11\n    total_steps: 30\n    crash_reason: /tmp disk full (fast_downward libdownward.so)\n    initial_val_action_is_valid: 0.652\n    initial_val_success: 0\n    step1_success: 0.047\n    step1_pass_at_8: 0.375\n    step1_action_is_valid: 0.588\n    step10_success: 0\n    step10_pass_at_8: 0\n    step10_action_is_valid: 0.683\n    step5_ppo_kl: 0.00158\n    step5_entropy: 0.1\n    trend: action_is_valid improving (58.8%→68.3%) but success collapsing (4.7%→0%)\n    checkpoint_saved: global_step_10\n- exp_id: exp011\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp012\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp012b\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    step: 8\n    total_steps: 30\n    step6_success: 0.0859\n    step6_action_is_valid: 0.613\n    step6_pass_at_16: 0.5\n    step6_ppo_kl: 0.0039\n    step6_entropy: 0.1006\n    step6_grad_norm: 1.477\n    step7_success: 0\n    step7_action_is_valid: 0.685\n    step7_pass_at_16: 0\n    step7_pg_loss: 0\n    step7_ppo_kl: 0.00439\n    step7_entropy: 0.0904\n    step7_grad_norm: 0.094\n    trend: success 8.6%→0% collapse at step 7 (same pattern as exp010, delayed 1 step).\n      grad_norm 1.477→0.094, pg_loss→0. Reward fix delayed but did not prevent collapse.\n- exp_id: exp013\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp013b\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp013c\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp013d\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp013e\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp013f\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    step: 30\n    total_steps: 30\n    completed: true\n    exit_code: 0\n    training_time_s: 10683\n    step6_success: 0.0156\n    step7_success: 0.0781\n    step10_success: 0\n    step17_success: 0.0156\n    final_val_success: 0\n    final_val_action_is_valid: 0.975\n    final_val_action_is_effective: 1\n    final_val_reward_mean_at4: 4.388\n    final_val_reward_std_at4: 0.195\n    final_val_reward_best_at4: 4.499\n    final_val_pass_at1: 0\n    action_is_valid_trend: 60%→65.9%→77.1%→97.5%\n    success_trend: 0%→1.56%→7.81%→0%→1.56%→0%\n    grad_norm_range: 1.7-2.9 (no collapse)\n    conclusion_reason: 'Dense reward gaming: model optimized valid_action_bonus (action_is_valid\n      60%→97.5%) but success stayed 0%. Reward ratio 1:67 too weak — cumulative valid_action_bonus\n      (4.5) dominated learning signal vs sparse success_reward (10.0). GRPO collapse\n      prevented but task completion not learned.'\n- exp_id: exp014c\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp014a\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp014b\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp015\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    step: 1\n    total_steps: 30\n    val_step0_success: 0\n    val_step0_action_is_valid: 0.858\n    val_step0_pass_at1: 0\n    val_step0_episodic_return: 0\n    val_step0_response_length: 2797.5\n    val_train_transition: passed\n    estimated_total_time_min: 163\n    time_per_step_min: 5.6\n- exp_id: exp016\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    step: 12\n    total_steps: 30\n    elapsed_min: 51\n    step6_success: 0\n    step6_action_is_valid: 0.521\n    step6_pg_loss: 0\n    step6_grad_norm: 0.841\n    step7_success: 0.047\n    step7_pass_at16: 0.5\n    step7_action_is_valid: 0.655\n    step10_success: 0\n    step10_action_is_valid: 0.664\n    step10_pg_loss: 0\n    step10_grad_norm: 0.856\n    step10_entropy: 0.1046\n    step10_ppo_kl: -9.1e-05\n    all_raw_rewards: 0\n    all_advantages: 0\n    all_returns: 0\n    reward_signal: BROKEN — success episodes get reward=0\n    action_is_valid_trend: 52.1%→65.5%→66.4%\n    manager_invalid_action_trend: 13.5%→11.2%→9.6%\n- exp_id: exp017_expert_sft\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_train_loss: 0.1434\n    final_step_loss: 0.04\n    final_token_accuracy: 0.983\n    epochs: 3\n    total_steps: 462\n    training_time_min: 26\n    data_count_train: 2460\n    data_count_val: 129\n    checkpoint_size_gb: 3.44\n    eval_success_rate: 0.05\n    eval_success: 1/20\n    eval_action_is_valid: 0.638\n    eval_format_ok: 0.75\n    eval_avg_steps: 22\n    eval_time_s: 149.6\n    eval_per_task:\n      put: 0/10\n      clean: 0/4\n      cool: 1/3\n      heat: 0/2\n      examine: 0/1\n    eval_parse_failures: 5/20 episodes (EP 7/12/16/17/18)\n- exp_id: exp018_sft_grpo\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp019_expert_sft_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp019b_expert_sft_v2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp019b_expert_sft_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.0718\n    eval_loss: 0.0428\n    eval_mean_token_accuracy: 0.9869\n    train_runtime_seconds: 2869.8\n    steps: 320\n    epochs: 2\n    eval_success_rate: 0.2\n    eval_format_ok: 1\n    eval_action_is_valid: 0.8533\n    eval_episodes: 20\n    eval_avg_steps: 25.4\n    eval_time_seconds: 146\n- exp_id: exp019c_expert_sft_v3\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp020_grpo_from_sft\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp020b_grpo_from_sft\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    steps_completed: 22\n    steps_planned: 30\n    hung_at_step: 23\n    step1_train_success: 0.1875\n    step10_train_success: 0.1875\n    step20_train_success: 0.125\n    step22_train_success: 0.0469\n    val_success_step0: 0\n    val_success_step20: 0\n    entropy_initial: 0.107\n    entropy_final: 0.042\n    grad_norm_initial: 2.78\n    grad_norm_step20: 5.58\n    ppo_kl_final: 0.00918\n    pass_at_16_step1: 0.75\n    pass_at_16_step22: 0.25\n    checkpoint_latest: global_step_20\n    training_status: hung_at_step23_rollout\n- exp_id: exp020c_grpo_from_sft\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp020d_grpo_from_sft\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp021_sft_ragen_format\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp021_ragen_sft_v4\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    train_loss_final: 0.038\n    train_token_accuracy: 0.988\n    train_steps: 320\n    train_epochs: 2\n    train_time_min: 47.8\n    ragen_val_success: 0.25\n    ragen_val_action_is_valid: 0.875\n    eval_sft_fast_success: 0\n    eval_sft_fast_format_ok: 1\n    eval_sft_fast_action_is_valid: 0.71\n    checkpoint_size_gb: 3.3\n    ragen_val_success_16ep: 0.0625\n    ragen_val_action_is_valid_16ep: 0.6875\n- exp_id: exp022_grpo_from_sft_v4\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    steps_completed: 1\n    steps_planned: 30\n    val_step0_success: 0.125\n    val_step0_action_is_valid: 0.4875\n    val_step0_action_is_effective: 1\n    val_step0_reward_mean: 1.25\n    val_step0_reward_best: 6.61\n    val_step0_episodes: 8\n    step_time_seconds: 208\n- exp_id: exp023_grpo_parallel\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp023c_grpo_serial\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    val_step0_success: 0.0625\n    val_step0_action_is_valid: 0.6875\n    val_step0_episodes: 16\n    train_step1_success: 0.297\n    train_step1_action_is_valid: 0.791\n    train_step1_entropy: 0.0652\n    train_step1_pass16: 0.75\n    train_step1_kl: 0.000156\n    train_step8_success: 0.234\n    train_step8_action_is_valid: 0.779\n    train_step8_entropy: 0.0555\n    train_step8_pass16: 0.5\n    train_step8_kl: 0.000475\n    steps_completed: 8\n    steps_planned: 30\n    step_time_seconds_start: 240\n    step_time_seconds_end: 365\n- exp_id: exp024_success_gated_grpo\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp025\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp025b\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp025c\n  name: ''\n  status: PENDING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp026_step_independent_grpo\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    val_before_train_success: 0.0625\n    val_before_train_action_is_valid: 0.631\n    val_before_train_episodes: 16\n    train_step1_success: 0.2188\n    train_step1_action_is_valid: 0.686\n    train_step1_entropy: 0.2672\n    train_step1_kl_loss: 0.1797\n    train_step1_grad_norm: 14.43\n    train_step1_reward_mean: 1.218\n    train_step1_pass_at_16: 1\n    train_step2_success: 0.3281\n    train_step2_action_is_valid: 0.603\n    train_step2_entropy: 0.317\n    train_step2_kl_loss: 0.0974\n    train_step2_grad_norm: 15.62\n    train_step2_reward_mean: 1.62\n    train_step2_pass_at_16: 1\n    train_step3_success: 0.1719\n    train_step3_action_is_valid: 0.641\n    train_step3_entropy: 0.387\n    train_step3_kl_loss: 0.2617\n    train_step3_grad_norm: 15.65\n    train_step3_reward_mean: 1.079\n    train_step3_pass_at_16: 0.75\n    train_step4_success: 0\n    train_step4_action_is_valid: 0.717\n    train_step4_entropy: 0.387\n    train_step4_kl_loss: 0.054\n    train_step4_grad_norm: 13.81\n    train_step4_pass_at_16: 0\n- exp_id: exp027_stable_grpo\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    step_0_val_before_train:\n      success: 6.25\n      action_is_valid: 63.125\n      action_is_effective: 87.875\n      num_actions: 42.375\n      response_length: 114.67\n      reward_mean: 0.3226\n      val_generation_time_s: 502.57\n    step_1_train:\n      success: 35.94\n      kl_loss: 0.058\n      batch_size: 5152\n      training_time_s: 4342\n    step_2_train:\n      success: 10.16\n      kl_loss: 0.413\n      batch_size: 6144\n      training_time_s: 5886\n    step_3_train:\n      success: 10.16\n      kl_loss: 0.248\n      entropy: 0.385\n      pass_at_16: 0.5\n      grad_norm: 21.31\n      reward_mean: 0.483\n      batch_size: 6048\n      training_time_s: 4689\n    step_4_train:\n      success: 13.28\n      pass_at_16: 0.375\n      note: 'Director判定: 趋势确认, MVP未通过'\n- exp_id: exp028_prereq_zeroshot_instruct\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp028a_recipe_fix\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp028_prereq_zeroshot\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    success: 0\n    action_is_valid: 0.75\n    num_actions: 50\n    pass_at_1: 0\n    response_length: 75.07\n- exp_id: exp028c_selfguide_recipe\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    step_0_val:\n      success: 6.25\n      pass_at_1: 6.25\n      action_is_valid: 74.5\n      score_mean: 0.119\n    step_1_train:\n      success: 13.28\n      pass_at_8: 37.5\n      action_is_valid: 76.4\n      action_is_effective: 96.37\n      entropy: 0.2634\n      kl_loss: 0.0128\n      ppo_kl: 0.019\n      grad_norm: 16.88\n      score_mean: 0.843\n      time_s: 3252\n      note: 三方交叉验证通过\n    step_2_train:\n      success: 6.25\n      pass_at_8: 25\n      action_is_valid: 83.2\n      entropy: 0.247\n      kl_loss: 0.1706\n      pg_loss: 0.007\n      grad_norm: 17.3\n      score_mean: 0.274\n      time_s: 3120\n    step_3_train:\n      success: 15.63\n      pass_at_8: 68.75\n      action_is_valid: 85.9\n      entropy: 0.2488\n      kl_loss: 0.1118\n      grad_norm: 12.57\n      score_mean: 0.661\n      time_s: 2760\n    step_4_train:\n      success: 18.75\n      pass_at_8: 62.5\n      action_is_valid: 87.94\n      entropy: 0.234\n      kl_loss: 0.031\n      ppo_kl: 0.015\n    step_5_train:\n      success: 9.4\n      pass_at_8: 37.5\n      action_is_valid: 89.6\n      entropy: 0.236\n      kl_loss: 0.824\n      grad_norm: 13.1\n    step_5_val:\n      success: 6.25\n      pass_at_1: 6.25\n      action_is_valid: 96.5\n      action_is_effective: 100\n      num_actions: 49.4\n      score_mean: 0.518\n    step_6_train:\n      success: 10.94\n      action_is_valid: 90.4\n      entropy: 0.234\n      kl_loss: 0.098\n      grad_norm: 12.54\n    step_7_train:\n      success: 21.88\n      pass_at_8: 56.25\n      action_is_valid: 91.8\n      entropy: 0.224\n      kl_loss: 0.046\n    step_8_train:\n      success: 15.6\n      pass_at_8: 50\n      action_is_valid: 92.7\n      kl_loss: 0.039\n      entropy: 0.204\n    step_9_train:\n      success: 18\n      pass_at_8: 56.3\n      action_is_valid: 93.6\n      kl_loss: 0.047\n      entropy: 0.204\n    step_10_train:\n      success: 18.75\n      action_is_valid: 90.7\n      kl_loss: 0.197\n    step_10_val:\n      success: 0\n      pass_at_1: 0\n      best_at_128: 0\n      best_at_800: 0\n      action_is_valid: 93.6\n      num_actions: 49.8\n      reward_mean: 0\n      note: 灾难性崩溃，模型完全遗忘\n- exp_id: exp029_episode_level\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-16T23:58:44.671Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T23:58:44.671Z",
  "sessionId": "79f9012f-eb35-4e80-8e55-564c1bc1b0c2"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-16T23:58:44.692Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：Episode-level收敛至30-42%，selective verification效果有限，需rebalance为methodology-heavy paper
核心假设：['Episode-level训练收敛但未大幅超过40%阈值（borderline区间）', 'h-sweep大体展示预期趋势但存在噪声（某些h值不完全单调）', 'Selective verification可训练但cost-performance tradeoff不dramatic', 'Action-change signal存在但correlation moderate（r=0.15-0.25）', 'Multi-seed有一定variance（std 5-8pp）']
关键指标范围：{'episode_level_success_rate': [30, 42], 'step_independent_baseline': [0, 6], 'h_sweep_cliff_threshold': [3, 8], 'selective_verification_rate_reduction': [15, 35], 'selective_vs_always_on_success_delta_pp': [3, 8], 'action_change_confirmatory_rate_pct': [55, 75], 'multi_seed_std_pp': [5, 8], 'action_is_valid': [85, 93]}
叙事方向：Rebalance为70% training methodology + 30% selective verification。Claim 1保持strong（episode vs step-independent的gap仍然dramatic），但Claim 2+3降级为'preliminary evidence'或'proof-of-concept'。Paper主打：episode-level training是被忽视的关键设计选择，selective verification作为downstream application demo而非co-equal contribution。需要加厚Phase C ablation（h-sweep做得更细、mechanism analysis更深）来补偿Phase B的弱结果。Title可能调整为更强调methodology。

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: cost-verify-agent-rl
focus: Evaluate dual contribution (episode-level training methodology + selective verification). Key uncertainty: will episode-level training converge high enough (≥40%) to support cost-efficiency story? Is the episode-level insight novel enough standalone?

## paper_framing.md

# Paper Framing — Learning When to Verify: RL-Trained Selective Self-Verification for Interactive Agents

> Post-MVP 重写 (2026-05-16) | 基于 D053 MVP 通过 + Reviewer 建议

## Core Insight

Multi-turn interactive agents 的 self-verification 大部分是 confirmatory（不改变行为）而非 corrective。但要训练 agent 学会 selective verification，首先需要解决一个被忽视的训练方法论问题：**step-independent RL 在长 horizon 任务中因 credit assignment decay (gamma^(T-h) → 0) 而灾难性崩溃**。Episode-level training 是前提条件。在此基础上，action-change 作为 intrinsic reward signal 训练 selective verification policy。

## Story Arc

**Dual contribution**: Training methodology + Selective verification system

叙事线：
1. Self-verification 对 interactive agents 有用，但 always-on 成本高
2. 训练 agent 学 WHEN to verify 是自然方向 → 但现有 step-independent RL 框架在多轮任务上失败
3. 我们发现根因是 credit assignment decay，提出 episode-level GRPO 解决
4. 在此基础上，用 action-change 作为 verification informativeness 的 reward，训练 selective policy
5. 结果：near-always-on performance + 显著降低 verification cost

## Target Venue

待定（NeurIPS 2026 / EMNLP 2026 / ICLR 2026），取决于实验进度和最终效果。

## Core Claims

### Claim 1 (strength: strong): Episode-level credit assignment is critical for RL training of multi-turn agents
- 所需证据：episode-level vs step-independent 对比，不同 h 值的 ablation，mechanistic 分析
- 当前证据状态：**ESTABLISHED** (exp029 step5 val=25% vs exp028c step10 val=0%)
- 强度依据：2x baseline vs catastrophic collapse，机制清晰（gamma^49=7.7%）

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
- **Plan A**（首选）：paper 变为 pure training methodology contribution — "Episode-Level RL for Multi-Turn Agents: Why Step-Independent Fails and How to Fix It"
- **Plan B**：加更多 ablation 深挖 episode-level training（context window size sweep, reward shaping, curriculum），做 analysis paper
- 不考虑 downgrade venue

## Reviewer Attack Surface + Defense

| # | Concern | Severity | Defense Experiment |
|---|---------|----------|--------------------|
| 1 | "Episode-level RL is obvious / well-known" | HIGH | Context window ablation (h=2,5,10,20,full) 展示 non-trivial threshold + 机制分析 + 展示现有 LLM-agent 工作(RAGEN等)默认 step-independent |
| 2 | Single environment (ALFWorld) | MEDIUM | 加 ScienceWorld / WebShop (if resources permit) |
| 3 | Small model (1.7B) | MEDIUM | 定位 resource-constrained; 加 7B 验证 (if GPU available) |
| 4 | Action-change = noise vs signal | MEDIUM | Entropy-controlled analysis + causal intervention (Phase B) |
| 5 | Selective verification 效果不够 significant | MEDIUM | 多 baseline 对比 (always-on / no-verify / random-p / confidence-threshold / ARES) |
| 6 | 与 ARES 差异化不足 | LOW | 实验直接对比 + 方法论差异表 (SFT router vs RL policy, continuous vs binary) |

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
  - success_rate
  - action_is_valid
  - kl_divergence
  - entropy
  gpu_hours_estimate: 48
  framing_ref: claim_1
  conclusion: failed
- id: plan_002
  title: Context window h-sweep ablation
  claim: Claim 1
  phase: A+
  priority: P0
  depends_on:
  - plan_001
  registry_id: null
  status: planned
  description: 'Sweep context_window h={2, 5, 10, 20, full} on same GRPO config. KEY
    paper figure: shows credit assignment threshold is not binary (h=2 catastrophic,
    intermediate h partial, full best). Mechanistic analysis: plot effective discount
    gamma^(T-h) vs performance. Addresses Reviewer Concern #1 ("episode-level is obvious").

    '
  hypothesis: 'Performance degrades monotonically with smaller h, with sharp cliff
    below h=10 where gamma^(T-h) < 0.01 for most episodes.

    '
  metrics:
  - success_rate_per_h
  - convergence_speed
  - collapse_rate
  gpu_hours_estimate: 120
- id: plan_003
  title: Multi-seed replication (3 seeds)
  claim: Claim 1
  phase: A+
  priority: P0
  depends_on:
  - plan_001
  registry_id: null
  status: planned
  description: '2 additional seeds for exp029 episode-level config. Report mean ±
    std. Critical for statistical credibility of all downstream comparisons.

    '
  hypothesis: 'Episode-level success rate is reproducible (std < 5pp across seeds).

    '
  metrics:
  - success_rate_mean
  - success_rate_std
  gpu_hours_estimate: 96
- id: plan_004
  title: Credit assignment mechanism analysis (paper Figure 2)
  claim: Claim 1
  phase: A+
  priority: P0
  depends_on:
  - plan_002
  registry_id: null
  status: planned
  description: 'Compute and visualize: (a) effective discount gamma^(T-h) for each
    h value, (b) gradient signal strength per training step under different h, (c)
    correlation between episode length and performance drop under small h. Mostly
    analysis/plotting, minimal GPU.

    '
  hypothesis: 'Shorter contexts produce exponentially weaker gradient signal, explaining
    the catastrophic collapse pattern.

    '
  metrics:
  - gradient_signal_strength
  - discount_factor_curve
  gpu_hours_estimate: 4
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
  status: PENDING
  conclusion: failed
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
  conclusion: failed
  metrics: {}

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
  "promptId": "1535ae77-11b5-4533-bf0c-6bcbdd7dc59f",
  "type": "user",
  "uuid": "7fc829a8-024a-4861-8179-29374d6d1afa",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1",
  "sessionId": "79f9012f-eb35-4e80-8e55-564c1bc1b0c2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T23:58:44.691Z_

```json
{
  "parentUuid": "7fc829a8-024a-4861-8179-29374d6d1afa",
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
  "uuid": "9424e2d0-b790-4fa7-9d13-d0636e56ac50",
  "timestamp": "2026-05-16T23:58:44.691Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1",
  "sessionId": "79f9012f-eb35-4e80-8e55-564c1bc1b0c2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T23:58:44.691Z_

```json
{
  "parentUuid": "9424e2d0-b790-4fa7-9d13-d0636e56ac50",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "e89085a8-5e98-4de4-85c4-fe4922bbee1d",
  "timestamp": "2026-05-16T23:58:44.691Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1",
  "sessionId": "79f9012f-eb35-4e80-8e55-564c1bc1b0c2",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Episode-level收敛至30-42%，selective verification效果有限，需rebalance为methodology-heavy paper 核心假设：['Episode-level训练收敛但未大幅超过40%阈值（borderline区间）', 'h-sweep大体展示预期趋势…",
  "leafUuid": "e89085a8-5e98-4de4-85c4-fe4922bbee1d",
  "sessionId": "79f9012f-eb35-4e80-8e55-564c1bc1b0c2"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Episode-level training for selective verification: Detailed median-tier projections",
  "sessionId": "79f9012f-eb35-4e80-8e55-564c1bc1b0c2"
}
```

---

### Assistant

_source line 8 · 2026-05-16T23:59:09.182Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed imagined experimental data for all "planned" experiments in the experiment_plan, based on the "median" tier definition they provided. Let me carefully go through each planned experiment and generate realistic data that fits within the median tier parameters.

Key median tier parameters:
- Episode-level success rate: 30-42%
- Step-independent baseline: 0-6%
- h-sweep cliff threshold: h=3-8
- Selective verification rate reduction: 15-35%
- Selective vs always-on success delta: 3-8pp
- Action-change confirmatory rate: 55-75%


- Multi-seed std: 5-8pp
- Action is valid: 85-93%

Narrative direction: 70% training methodology + 30% selective verification. Claim 1 strong, Claims 2+3 downgraded to "preliminary evidence."

Now I'm working through each of the planned experiments systematically: the h-sweep ablation across different h values, the multi-seed robustness check, the credit assignment mechanism analysis, action-change statistics, the selective verification implementation, and the remaining experiments to ensure all data points align with the median tier constraints.

I'm noticing something odd with plan_001 though—it's marked as failed in the registry, but the median tier definition suggests episode-level convergence should hit 30-42%, which seems to contradict that conclusion. Let me reconcile what the actual expected performance should be versus what was observed.

The user is asking for detailed data specifically on the planned experiments, not the completed ones. Looking through the registry, all experiments except plan_001 have "planned" status, so I need to generate synthetic data for plans 002 through 016 based on the median tier expectations.

Since plan_001 actually failed but the median tier scenario assumes a ~36% success baseline, I'll treat that as the foundation and build the planned experiments' data around it, constructing the YAML output with realistic metrics for each planned run.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e89085a8-5e98-4de4-85c4-fe4922bbee1d",
  "isSidechain": false,
  "requestId": "req_011Cb79y8poTs9p5LpCHtxD5",
  "type": "assistant",
  "uuid": "ff90c539-16d3-411b-8807-99e0bd8c336e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1",
  "sessionId": "79f9012f-eb35-4e80-8e55-564c1bc1b0c2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016fRzX6ZeixWb6LBhvdhpjh",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16917,
      "cache_read_input_tokens": 11841,
      "output_tokens": 11377,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16917,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 11377,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 16917,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16917
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

_source line 9 · 2026-05-17T00:02:35.860Z_

```yaml
tier: median
narrative_guidance: "Rebalance为70% training methodology + 30% selective verification。Episode-level训练收敛至~36%，与step-independent的0%形成dramatic gap（Claim 1 strong）。h-sweep展示预期趋势但有噪声，multi-seed variance偏大(std~6pp)。Selective verification可工作但cost-performance tradeoff不够dramatic（Claim 2+3降级为preliminary evidence）。Paper主打episode-level training methodology，selective verification作为downstream demo。需加厚Phase C ablation弥补Phase B弱结果。"

imagined_experiments:
  - name: "Context window h-sweep ablation"
    plan_id: "plan_002"
    description: "Sweep h={2,5,10,20,full}，展示credit assignment threshold非binary"
    expected_results:
      h2_success_rate: 0.0
      h5_success_rate: 4.7
      h10_success_rate: 18.8
      h20_success_rate: 29.7
      h_full_success_rate: 35.9
      h2_action_is_valid: 72.3
      h5_action_is_valid: 78.6
      h10_action_is_valid: 85.1
      h20_action_is_valid: 88.4
      h_full_action_is_valid: 90.6
      h2_convergence_steps: "collapsed_step4"
      h5_convergence_steps: 25
      h10_convergence_steps: 18
      h20_convergence_steps: 15
      h_full_convergence_steps: 12
      cliff_threshold_h: 5
    result_rationale: "Median档下h-sweep大体展示预期趋势但存在噪声。h=2完全崩溃（gamma^(50-2)≈0），h=5勉强有信号但仅4.7%（cliff位于h=5-10之间，符合median指标h_cliff=3-8）。h=10到h=20的跳跃(18.8→29.7)不完全单调——某些seed下h=10偶尔超过h=20的个别eval batch，造成noise。h=full达到35.9%但未突破40%阈值。整体趋势清晰但不像理想情况那样perfectly monotonic，存在reviewer可以质疑的边界case。"
    tables:
      - name: "Table 2: h-sweep results"
        columns: ["h", "success_rate(%)", "action_is_valid(%)", "converge_step", "effective_discount"]
        rows:
          - [2, 0.0, 72.3, "collapse", "7.7e-25"]
          - [5, 4.7, 78.6, 25, "7.7e-14"]
          - [10, 18.8, 85.1, 18, "2.8e-7"]
          - [20, 29.7, 88.4, 15, "5.2e-4"]
          - ["full", 35.9, 90.6, 12, "1.0"]
    figures_description:
      - "Figure 2a: h vs success_rate曲线，sigmoid-like但h=10处有轻微非单调（某batch h=10略高于趋势线），error bar较大"
      - "Figure 2b: effective discount gamma^(T-h) vs performance，log-scale，展示exponential decay关系但散点有噪声"
    analysis: "h-sweep确认credit assignment decay hypothesis但curve不够clean。h=5是cliff区域（从4.7%到h=10的18.8%有4x跳跃）。关键发现：intermediate h值(10,20)部分有效，说明threshold不是binary而是gradual degradation。但h=10和h=20之间的gap(11pp)小于h=20和full之间的gap(6pp)，暗示diminishing returns。Reviewer可能argue h=20已经'good enough'——需要在paper中强调full context的额外6pp在deployment中的cumulative价值。"

  - name: "Multi-seed replication (3 seeds)"
    plan_id: "plan_003"
    description: "2 additional seeds复现episode-level config，报告mean±std"
    expected_results:
      seed1_success_rate: 35.9
      seed2_success_rate: 29.7
      seed3_success_rate: 39.1
      mean_success_rate: 34.9
      std_success_rate: 4.7
      seed1_action_is_valid: 90.6
      seed2_action_is_valid: 86.3
      seed3_action_is_valid: 91.8
      mean_action_is_valid: 89.6
      std_action_is_valid: 2.9
      seed1_convergence_step: 12
      seed2_convergence_step: 16
      seed3_convergence_step: 11
    result_rationale: "Median档下multi-seed std在5-8pp范围。三个seed分别为35.9/29.7/39.1%，std≈4.7pp——略低于median范围下限(5pp)但接近。Seed2表现较差(29.7%)拉低mean至34.9%，刚好落在median指标[30,42]内。Variance主要来自early training的exploration randomness——不同seed在step 3-5的trajectory divergence决定了最终收敛点。action_is_valid更稳定(std 2.9pp)因为它是easier sub-task。"
    tables:
      - name: "Table 3: Multi-seed episode-level results"
        columns: ["seed", "success_rate(%)", "action_is_valid(%)", "converge_step", "final_entropy"]
        rows:
          - [42, 35.9, 90.6, 12, 0.18]
          - [123, 29.7, 86.3, 16, 0.21]
          - [7, 39.1, 91.8, 11, 0.16]
          - ["mean±std", "34.9±4.7", "89.6±2.9", "13.0±2.6", "0.18±0.03"]
    figures_description:
      - "Figure S1: 三条learning curve叠加，shaded area表示min-max范围，展示convergence trajectory variance"
    analysis: "Std=4.7pp在可接受范围但不够tight。Seed2的29.7%是potential weakness——reviewer可能argue这接近step-independent上界。Defense：即使worst seed(29.7%)仍远超step-independent(0-6%)，gap仍然dramatic(24-30pp)。但无法claim '≥40% convergence'——需要更多seeds或更长training来tighten confidence interval。Paper措辞需调整为'converges to 30-39% range'而非固定数字。"

  - name: "Credit assignment mechanism analysis"
    plan_id: "plan_004"
    description: "可视化effective discount、gradient signal strength、episode length correlation"
    expected_results:
      gradient_signal_h2_relative: 0.003
      gradient_signal_h5_relative: 0.041
      gradient_signal_h10_relative: 0.287
      gradient_signal_h20_relative: 0.714
      gradient_signal_full_relative: 1.0
      episode_length_performance_correlation: -0.43
      episode_length_performance_p_value: 0.008
      mean_episode_length: 38.7
      gradient_variance_h2: 0.89
      gradient_variance_full: 0.12
    result_rationale: "Mechanism analysis主要是对h-sweep数据的post-hoc分析。Gradient signal strength与effective discount高度相关(r>0.95)——这是数学必然。Episode length与performance负相关(r=-0.43, p=0.008)说明longer episodes在small-h下受害更严重——这支撑mechanism story。但correlation是moderate(-0.43)而非strong，因为episode success还受task difficulty影响。Gradient variance在h=2时极高(0.89)说明信号几乎是noise。"
    tables:
      - name: "Table 4: Gradient signal analysis"
        columns: ["h", "effective_discount", "relative_gradient_signal", "gradient_variance", "collapsed(%)"]
        rows:
          - [2, "7.7e-25", 0.003, 0.89, 100]
          - [5, "7.7e-14", 0.041, 0.67, 75]
          - [10, "2.8e-7", 0.287, 0.34, 25]
          - [20, "5.2e-4", 0.714, 0.18, 0]
          - ["full", 1.0, 1.0, 0.12, 0]
    figures_description:
      - "Figure 2c: gradient signal strength vs h (log-scale x-axis)，展示exponential relationship"
      - "Figure 2d: episode length histogram colored by success/failure，stratified by h value"
      - "Figure 2e: per-step gradient magnitude heatmap across training steps for each h"
    analysis: "Mechanism analysis清晰支撑narrative：credit assignment decay是exponential的，gradient signal在small h下是noise-dominated。Key insight for paper：不仅是signal弱，而且variance高——small-h模型实际在做random walk而非learning。Episode length correlation提供additional evidence但不是smoking gun(r=-0.43)。整体sufficient for methodology paper的Figure 2，但需要careful framing避免over-claim因果关系。"

  - name: "Action-change statistics from always-on runs"
    plan_id: "plan_005"
    description: "收集always-on verification的action-change统计"
    expected_results:
      total_verification_episodes: 240
      total_verification_steps: 9360
      action_change_rate_overall: 31.2
      confirmatory_rate_pct: 68.8
      action_change_success_correlation_r: 0.19
      action_change_success_correlation_p: 0.003
      per_task_action_change_rate_pick: 26.4
      per_task_action_change_rate_clean: 33.7
      per_task_action_change_rate_heat: 35.2
      per_task_action_change_rate_cool: 29.8
      per_task_action_change_rate_examine: 38.1
      per_task_action_change_rate_pick_two: 28.9
      action_change_at_early_steps_pct: 22.1
      action_change_at_mid_steps_pct: 34.6
      action_change_at_late_steps_pct: 41.3
    result_rationale: "Median档下confirmatory rate在55-75%范围——这里68.8%。意味着接近70%的verification没有改变agent行为，支撑'most verification is wasted'的narrative。但action-change与success的correlation仅r=0.19(在median的0.15-0.25范围内)——这是moderate信号，sufficient for motivation但不够强到支撑action-change作为standalone reward的strong claim。Late steps的action-change率更高(41.3%)因为agent在episode后期更likely偏离正轨，需要correction。"
    tables:
      - name: "Table 5: Action-change statistics"
        columns: ["metric", "value"]
        rows:
          - ["Confirmatory rate (no action change)", "68.8%"]
          - ["Action-change rate", "31.2%"]
          - ["Correlation with episode success (r)", 0.19]
          - ["p-value", 0.003]
          - ["Action-change at early steps (1-15)", "22.1%"]
          - ["Action-change at mid steps (16-35)", "34.6%"]
          - ["Action-change at late steps (36-50)", "41.3%"]
    figures_description:
      - "Figure 3a: action-change rate per step position (bar chart)，展示increasing trend"
      - "Figure 3b: scatter plot of per-episode action-change count vs episode success (binary)，展示weak positive trend"
    analysis: "Confirmatory rate 68.8%确认核心motivation——大多数verification是浪费。但r=0.19的correlation偏弱，需要careful framing。不能claim 'action-change strongly predicts success'，只能说'action-change is a meaningful but noisy signal for verification informativeness'。Per-task breakdown显示examine类task最高(38.1%)——可能因为这类task需要更多exploration/correction。Paper应强调这是'proof-of-concept evidence'而非conclusive。"

  - name: "Selective verification implementation"
    plan_id: "plan_006"
    description: "Code implementation of binary verify/skip mechanism (no GPU needed)"
    expected_results:
      implementation_complete: true
      verify_token_added: true
      reward_function_implemented: true
      alpha_default: 0.5
      beta_default: 0.1
      integration_test_passed: true
    result_rationale: "纯code实现，无实验数据。实现binary verify/skip decision token，reward = task_success + alpha * action_change_when_verified - beta * verification_cost。Alpha=0.5和beta=0.1是initial hyperparameters，后续plan_007中调优。"
    tables: []
    figures_description: []
    analysis: "Implementation milestone，无experimental findings。关键设计决策：(1) verify/skip作为special token在每步action前输出，(2) reward中action_change仅在verify时计算(skip时为0)，(3) verification_cost是constant penalty per verify。这些design choices在plan_012的ablation中会被验证。"

  - name: "B-IAVR selective verification training"
    plan_id: "plan_007"
    description: "从best episode-level checkpoint初始化，训练selective verification policy"
    expected_results:
      final_success_rate: 31.3
      always_on_baseline_success: 35.9
      success_delta_pp: -4.6
      verification_rate: 71.2
      verification_rate_reduction_vs_always_on: 28.8
      action_is_valid: 87.4
      training_steps_to_converge: 18
      final_entropy: 0.24
      final_kl: 0.034
      cost_tokens_reduction_pct: 22.1
    result_rationale: "Median档下selective verification效果有限：verification rate仅降低28.8%(未达40%目标)，且success delta为-4.6pp(在median的3-8pp范围内但偏大)。这是因为：(1) base model仅35.9% success，headroom本就有限——从weak model上训练selectivity更难，因为model本身就不确定何时verification有帮助；(2) action-change signal仅r=0.19的correlation，reward信号noisy导致policy学到的是conservative strategy(倾向verify)而非optimal selective；(3) 28.8%的verification reduction虽然存在但cost-performance tradeoff不dramatic——需要几乎always verify才能维持本就不高的success rate。"
    tables:
      - name: "Table 6: B-IAVR training trajectory"
        columns: ["step", "success(%)", "verify_rate(%)", "entropy", "kl"]
        rows:
          - [0, 35.9, 100, 0.18, 0]
          - [5, 33.6, 85.3, 0.26, 0.012]
          - [10, 32.0, 76.8, 0.28, 0.021]
          - [15, 31.8, 73.1, 0.25, 0.029]
          - [18, 31.3, 71.2, 0.24, 0.034]
    figures_description:
      - "Figure 4a: success rate vs verification rate Pareto curve during training"
      - "Figure 4b: per-step verify probability heatmap across episode positions"
    analysis: "B-IAVR学到了一些selectivity但效果不够dramatic。Policy趋向于在early steps skip(因为early steps action-change率低)但在late steps几乎always verify。验证率从100%降到71.2%——仅~29%reduction。Success loss 4.6pp在可接受范围但combined with modest cost saving使得overall story偏弱。Paper中需要frame为'proof-of-concept that selective verification is learnable via RL'而非'a system that dramatically reduces cost'。"

  - name: "Selective verification full comparison"
    plan_id: "plan_008"
    description: "Always-on/B-IAVR/no-verify/random-p/confidence-threshold全面对比"
    expected_results:
      always_on_success: 35.9
      always_on_verify_rate: 100
      always_on_tokens: 47200
      biavr_success: 31.3
      biavr_verify_rate: 71.2
      biavr_tokens: 38100
      no_verify_success: 23.4
      no_verify_verify_rate: 0
      no_verify_tokens: 24800
      random_50_success: 28.1
      random_50_verify_rate: 50
      random_50_tokens: 35600
      confidence_threshold_success: 30.5
      confidence_threshold_verify_rate: 62.4
      confidence_threshold_tokens: 39700
    result_rationale: "Median档下B-IAVR在Pareto frontier上marginally优于baselines但差距不大。与random-50%相比：B-IAVR用更多verification(71.2% vs 50%)获得更多success(31.3% vs 28.1%)——说明B-IAVR的selectivity有signal但不dramatic。与confidence-threshold相比几乎持平(31.3% vs 30.5% success, 71.2% vs 62.4% verify)——confidence-threshold更aggressive(verify少10pp)但success仅差0.8pp，暗示学到的policy和simple heuristic差别有限。Key finding：verification本身有价值(always-on 35.9% vs no-verify 23.4%=12.5pp gap)，但SELECTIVE verification的额外价值(vs random/confidence)是marginal的。"
    tables:
      - name: "Table 7: Full verification comparison"
        columns: ["method", "success(%)", "verify_rate(%)", "tokens", "cost_relative"]
        rows:
          - ["Always-on", 35.9, 100, 47200, "1.00"]
          - ["B-IAVR (ours)", 31.3, 71.2, 38100, "0.81"]
          - ["Confidence-threshold", 30.5, 62.4, 39700, "0.84"]
          - ["Random-50%", 28.1, 50.0, 35600, "0.75"]
          - ["No-verify", 23.4, 0, 24800, "0.53"]
    figures_description:
      - "Figure 5: Pareto frontier plot (success vs cost)，5 methods marked，B-IAVR slightly above convex hull of baselines"
    analysis: "Full comparison确认verification有价值(12.5pp gap)但selective的marginal benefit有限。B-IAVR在Pareto frontier上but仅marginally优于confidence-threshold。这意味着Claim 3无法以strong形式成立——paper需调整为：'B-IAVR demonstrates that RL can learn selectivity, but the current action-change signal provides limited advantage over simpler heuristics at this model capacity'。Framing应转向'the gap between always-on and no-verify motivates future work on better verification signals'。"

  - name: "No-verify ablation"
    plan_id: "plan_009"
    description: "Episode-level GRPO无self-verification，作为lower bound"
    expected_results:
      success_rate: 23.4
      action_is_valid: 85.7
      success_delta_vs_always_on: -12.5
      convergence_step: 14
      final_entropy: 0.19
      final_kl: 0.028
    result_rationale: "No-verify在median档下收敛至23.4%——比always-on(35.9%)低12.5pp。这证明verification有实质价值。差距来源：without verification，agent在错误action后无法self-correct，导致episode在early mistake后cascading failure。12.5pp gap对于paper是strong evidence that verification matters——即使selective verification效果不dramatic，always-on verification的价值已被establish。action_is_valid略低(85.7% vs 90.6%)因为without verification feedback，model less aware of action validity constraints。"
    tables:
      - name: "Table 8: No-verify vs always-on"
        columns: ["config", "success(%)", "action_is_valid(%)", "avg_episode_length"]
        rows:
          - ["Episode-level + always-on verify", 35.9, 90.6, 38.7]
          - ["Episode-level + no verify", 23.4, 85.7, 42.1]
          - ["Delta", -12.5, -4.9, "+3.4"]
    figures_description:
      - "Figure S2: learning curves对比(with/without verification)，展示gap在training中持续存在"
    analysis: "12.5pp gap是paper中supporting verification value的关键数据点。Without verification, episodes倾向于更长(42.1 vs 38.7 steps)因为agent wandering而非converging。这支撑Section 2的motivation ('verification helps but is costly → selective is needed')。即使B-IAVR最终效果modest，no-verify ablation确认了research direction的合理性。"

  - name: "Entropy-controlled action-change analysis"
    plan_id: "plan_010"
    description: "控制policy entropy后检验action-change-success partial correlation"
    expected_results:
      raw_correlation_r: 0.19
      partial_correlation_after_entropy_control: 0.14
      partial_correlation_p_value: 0.031
      entropy_action_change_correlation: 0.34
      entropy_strata_low_correlation: 0.11
      entropy_strata_mid_correlation: 0.16
      entropy_strata_high_correlation: 0.13
      significant_at_005: true
    result_rationale: "Median档下partial correlation从0.19降至0.14——entropy确实解释了部分action-change variance(r=0.34 between entropy and action-change)，但控制后correlation仍然significant(p=0.031)。这意味着action-change不完全是entropy/randomness的artifact，但signal偏弱(r=0.14)。各entropy stratum内的correlation基本一致(0.11-0.16)，说明relationship不依赖于specific entropy regime。对于paper够用作defense('action-change signal survives entropy control')但不够强到claim causal relationship。"
    tables:
      - name: "Table 9: Entropy-controlled analysis"
        columns: ["stratum", "n_episodes", "action_change_rate(%)", "success_rate(%)", "correlation_r"]
        rows:
          - ["Low entropy (<0.15)", 78, 24.3, 38.5, 0.11]
          - ["Mid entropy (0.15-0.25)", 96, 32.1, 34.2, 0.16]
          - ["High entropy (>0.25)", 66, 38.7, 30.1, 0.13]
          - ["Partial (entropy-controlled)", "240 total", "-", "-", "0.14 (p=0.031)"]
    figures_description:
      - "Figure S3: partial correlation forest plot，展示raw vs controlled vs per-stratum"
    analysis: "Defense成立但marginal——action-change不是pure noise(p<0.05)但信号弱。High entropy episodes有更多action-change(38.7% vs 24.3%)但更低success(30.1% vs 38.5%)——说明部分action-change确实是exploration noise而非informative correction。Paper应acknowledge this nuance:'while action-change survives entropy control, the modest partial correlation (r=0.14) suggests that stronger reward signals for verification informativeness remain an open problem'。"

  - name: "Causal intervention: random vs verification-triggered changes"
    plan_id: "plan_011"
    description: "注入random action changes对比verification-triggered changes的success rate"
    expected_results:
      verification_triggered_success_rate: 39.2
      random_triggered_success_rate: 31.8
      no_change_baseline_success_rate: 34.1
      delta_triggered_vs_random: 7.4
      delta_triggered_vs_no_change: 5.1
      n_episodes_per_condition: 80
      p_value_triggered_vs_random: 0.042
    result_rationale: "Median档下verification-triggered changes优于random但delta仅7.4pp(未达hypothesis的≥10pp)。关键insight：verification-triggered在成功率上(39.2%)高于no-change baseline(34.1%)说明verification有selective correction能力；但random changes也并非灾难性(31.8%)——有时random perturbation碰巧correct。7.4pp差距p=0.042，barely significant。这是'存在causal signal但不strong'的典型median档结果——够写进paper作为supporting evidence但不够作为standalone claim。"
    tables:
      - name: "Table 10: Causal intervention results"
        columns: ["condition", "success(%)", "n", "vs_random_p"]
        rows:
          - ["Verification-triggered change", 39.2, 80, "-"]
          - ["Random change (matched rate)", 31.8, 80, "0.042"]
          - ["No change (baseline)", 34.1, 80, "0.18"]
    figures_description:
      - "Figure S4: bar chart with error bars showing three conditions"
    analysis: "Causal evidence存在但偏弱。7.4pp delta不够large(hypothesis was ≥10pp)且p=0.042 barely passes threshold。有趣的是no-change baseline(34.1%)高于random(31.8%)——说明random changes有时harmful。Paper应frame为'preliminary causal evidence that verification-triggered corrections are non-random, though the effect size is modest'。Combined with entropy analysis, 构成Claim 2的supporting evidence bundle，单独每个都不够strong但together形成coherent picture。"

  - name: "Reward signal ablation (action-change vs alternatives)"
    plan_id: "plan_012"
    description: "对比action-change/random trigger/confidence-based三种reward训练B-IAVR"
    expected_results:
      action_change_reward_success: 31.3
      action_change_reward_verify_rate: 71.2
      action_change_reward_cost_reduction: 22.1
      random_reward_success: 27.8
      random_reward_verify_rate: 54.3
      random_reward_cost_reduction: 31.4
      confidence_reward_success: 30.1
      confidence_reward_verify_rate: 68.7
      confidence_reward_cost_reduction: 24.8
    result_rationale: "Median档下action-change reward略优但差距不dramatic。Action-change(31.3% success)优于random(27.8%)3.5pp和confidence(30.1%)1.2pp。但random reward的verification rate更低(54.3%)导致更大cost reduction(31.4%)——trade-off不clear-cut。Confidence-based与action-change几乎持平，暗示在这个model capacity下两种信号效果类似。这confirm了'action-change is a reasonable reward signal'但不能claim it's dramatically better——consistent with median tier的'selective verification效果有限'。"
    tables:
      - name: "Table 11: Reward signal comparison"
        columns: ["reward_type", "success(%)", "verify_rate(%)", "cost_reduction(%)", "pareto_optimal"]
        rows:
          - ["Action-change (ours)", 31.3, 71.2, 22.1, "yes"]
          - ["Confidence-based", 30.1, 68.7, 24.8, "~tied"]
          - ["Random trigger", 27.8, 54.3, 31.4, "no"]
    figures_description:
      - "Figure S5: Pareto frontier with three reward variants marked"
    analysis: "Action-change marginally best但优势不compelling。Paper应honest acknowledge：'action-change reward achieves the best success-to-cost ratio, but the margin over confidence-based baseline is modest (1.2pp success, 2.7pp cost difference). This suggests that at current model capacity, the choice of verification reward signal is less critical than the training methodology itself—reinforcing our focus on episode-level training as the primary contribution.'这naturally转向70% methodology narrative。"

  - name: "ARES reproduction + comparison"
    plan_id: "plan_013"
    description: "复现ARES SFT router，与B-IAVR head-to-head对比"
    expected_results:
      ares_reproduction_success: 29.7
      ares_reproduction_verify_rate: 58.3
      ares_reproduction_cost_reduction: 33.8
      biavr_success: 31.3
      biavr_verify_rate: 71.2
      biavr_cost_reduction: 22.1
      ares_original_paper_token_reduction: 52.7
      delta_success_biavr_vs_ares: 1.6
      delta_cost_ares_vs_biavr: 11.7
    result_rationale: "Median档下B-IAVR与ARES对比结果mixed：B-IAVR success略高(31.3 vs 29.7, +1.6pp)但cost reduction更差(22.1% vs 33.8%)。ARES的SFT router更aggressive(58.3% verify)因为supervised signal更直接；B-IAVR的RL policy更conservative。ARES reproduction未达原paper的52.7% token reduction——可能因为我们的setup(ALFWorld+1.7B model)与原paper不同。整体不能claim 'B-IAVR dominates ARES'(原hypothesis ≥10pp better cost reduction at matched success未达成)。需要frame为'different trade-off points: RL-based B-IAVR prioritizes success preservation while SFT-based ARES is more cost-aggressive'。"
    tables:
      - name: "Table 12: B-IAVR vs ARES comparison"
        columns: ["method", "success(%)", "verify_rate(%)", "cost_reduction(%)", "training_signal"]
        rows:
          - ["B-IAVR (ours, RL)", 31.3, 71.2, 22.1, "action-change reward"]
          - ["ARES (SFT router)", 29.7, 58.3, 33.8, "supervised labels"]
          - ["Always-on baseline", 35.9, 100, 0, "-"]
    figures_description:
      - "Figure 6: head-to-head Pareto plot with ARES and B-IAVR, annotated with training methodology differences"
    analysis: "ARES对比结果要求paper做careful positioning。不能claim domination——而是frame差异：(1) B-IAVR不需要human-labeled verification relevance data(ARES SFT需要)，(2) B-IAVR自动适应action-change statistics，(3) tradeoff：RL更conservative但SFT更直接有效。Paper table should highlight methodological differences(RL vs SFT, online vs offline, binary vs continuous)而非只看numbers。Competitive positioning变为'complementary approaches'而非'we beat ARES'。"

  - name: "ScienceWorld transfer"
    plan_id: "plan_014"
    description: "在ScienceWorld上验证episode-level vs step-independent优势"
    expected_results:
      scienceworld_episode_level_success: 22.8
      scienceworld_step_independent_success: 3.1
      scienceworld_episode_level_action_is_valid: 81.4
      scienceworld_step_independent_action_is_valid: 68.2
      advantage_ratio: 7.4
      convergence_steps_episode: 20
      convergence_steps_step_independent: "collapsed_step6"
    result_rationale: "Median档下ScienceWorld上episode-level优势依然dramatic(22.8% vs 3.1%, 7.4x)但absolute success偏低(22.8% vs ALFWorld的35.9%)。ScienceWorld harder because：(1) larger action space，(2) more complex state tracking，(3) longer episodes on average。Step-independent再次catastrophically collapse(3.1%接近random)。7.4x ratio(虽然不到ALFWorld的无穷大因为ALFWorld step-ind=0%)仍然是strong evidence for generalization。但absolute 22.8%意味着model在此env上capacity不足——不能做meaningful selective verification experiment on ScienceWorld。"
    tables:
      - name: "Table 13: ScienceWorld transfer results"
        columns: ["method", "success(%)", "action_is_valid(%)", "converge/collapse"]
        rows:
          - ["Episode-level (ScienceWorld)", 22.8, 81.4, "step 20"]
          - ["Step-independent (ScienceWorld)", 3.1, 68.2, "collapse step 6"]
          - ["Episode-level (ALFWorld, ref)", 35.9, 90.6, "step 12"]
          - ["Step-independent (ALFWorld, ref)", 0, 93.6, "collapse step 4"]
    figures_description:
      - "Figure 7: cross-environment comparison bar chart with ALFWorld and ScienceWorld side-by-side"
    analysis: "Transfer成功addresses single-env concern。Episode-level advantage在ScienceWorld上reproduce(7.4x ratio)。不同env的absolute performance差异可归因于task difficulty而非method failure。Paper可argue：'episode-level training methodology generalizes across interactive environments with different action spaces and episode structures'。This strengthens Claim 1 (methodology contribution) independent of Claim 2/3's weakness。"

  - name: "7B model scaling verification"
    plan_id: "plan_015"
    description: "Qwen3-7B上episode-level vs step-independent对比"
    expected_results:
      episode_level_7b_success: 48.4
      step_independent_7b_success: 5.3
      episode_level_7b_action_is_valid: 93.2
      step_independent_7b_action_is_valid: 74.8
      advantage_ratio_7b: 9.1
      convergence_steps_7b: 8
      advantage_ratio_1_7b: "inf (0% baseline)"
    result_rationale: "Median档下7B model在episode-level上达到48.4%——超过1.7B的35.9%约12.5pp，符合scaling expectation。Step-independent仍catastrophically低(5.3%)但不完全为0(比1.7B的0%略好——larger model有更多capacity做limited credit assignment)。Convergence更快(8 steps vs 12)因为7B model初始capability更强。Key implication：7B结果暗示method scales——如果have更多compute，更大model可能达到60%+，使selective verification story更compelling。但这在当前resource constraint下是future work。"
    tables:
      - name: "Table 14: Model scaling results"
        columns: ["model", "method", "success(%)", "action_is_valid(%)", "converge_step"]
        rows:
          - ["Qwen3-1.7B", "episode-level", 35.9, 90.6, 12]
          - ["Qwen3-1.7B", "step-independent", 0, 93.6, "collapse"]
          - ["Qwen3-7B", "episode-level", 48.4, 93.2, 8]
          - ["Qwen3-7B", "step-independent", 5.3, 74.8, "collapse step 8"]
    figures_description:
      - "Figure 8: scaling plot (model size vs success rate) for both methods, showing diverging trajectories"
    analysis: "7B结果是paper的strong supplementary evidence。Episode-level advantage不仅holds而且在absolute terms更impressive at scale(48.4%)。Step-independent即使在7B上仍collapse——refutes potential reviewer argument 'just use bigger model to compensate for credit assignment issues'。This result could motivate reframing paper conclusion：'episode-level training is prerequisite at ALL scales for multi-turn RL, and its benefit grows with model capacity'。如果paper space permits，这是compelling argument for methodology contribution。"

  - name: "Per-task-type breakdown analysis"
    plan_id: "plan_016"
    description: "按ALFWorld 6个task type分解episode-level结果"
    expected_results:
      pick_success: 42.1
      clean_success: 31.6
      heat_success: 38.9
      cool_success: 36.4
      examine_success: 22.7
      pick_two_success: 18.2
      pick_avg_episode_length: 28.3
      clean_avg_episode_length: 35.7
      heat_avg_episode_length: 32.1
      cool_avg_episode_length: 33.8
      examine_avg_episode_length: 41.2
      pick_two_avg_episode_length: 44.6
      episode_length_success_correlation: -0.87
    result_rationale: "Median档下task breakdown展示within-environment diversity：shorter/simpler tasks(pick:42.1%, length 28.3)表现最好，longer/complex tasks(pick_two:18.2%, length 44.6; examine:22.7%, length 41.2)表现较差。Episode length与per-task success高度负相关(r=-0.87)——longer tasks suffer more from credit assignment(即使用full context，longer episodes仍有higher variance)。This supports mechanism story：credit assignment difficulty与episode length直接相关。Pick_two最差因为需要sequential two-object manipulation——更长trajectory且更多potential failure points。"
    tables:
      - name: "Table 15: Per-task breakdown"
        columns: ["task_type", "success(%)", "n_episodes", "avg_length", "action_is_valid(%)"]
        rows:
          - ["pick", 42.1, 38, 28.3, 92.4]
          - ["heat", 38.9, 18, 32.1, 91.7]
          - ["cool", 36.4, 22, 33.8, 90.3]
          - ["clean", 31.6, 38, 35.7, 89.8]
          - ["examine", 22.7, 22, 41.2, 88.1]
          - ["pick_two", 18.2, 22, 44.6, 87.9]
    figures_description:
      - "Figure S6: per-task success bar chart ordered by avg episode length"
      - "Figure S7: scatter plot of task avg_length vs success_rate with regression line (r=-0.87)"
    analysis: "Per-task breakdown提供两个paper contributions：(1) demonstrates within-environment diversity(addresses single-env concern partially)，(2) strong correlation between episode length and difficulty supports credit assignment mechanism story。Reviewer defense：即使single env(ALFWorld)，task types span substantial complexity range(18-42% success, 28-45 steps)。Pick_two和examine的低success(18-23%)也暗示1.7B model capacity limit——selective verification在这些hard tasks上可能更有价值但base performance太低无法meaningful测试。"
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff90c539-16d3-411b-8807-99e0bd8c336e",
  "isSidechain": false,
  "requestId": "req_011Cb79y8poTs9p5LpCHtxD5",
  "type": "assistant",
  "uuid": "dc929bc0-4f07-40cc-a667-4fc00480c21f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1",
  "sessionId": "79f9012f-eb35-4e80-8e55-564c1bc1b0c2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016fRzX6ZeixWb6LBhvdhpjh",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16917,
      "cache_read_input_tokens": 11841,
      "output_tokens": 11377,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16917,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 11377,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 16917,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16917
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Episode-level收敛至30-42%，selective verification效果有限，需rebalance为methodology-heavy paper 核心假设：['Episode-level训练收敛但未大幅超过40%阈值（borderline区间）', 'h-sweep大体展示预期趋势…",
  "leafUuid": "dc929bc0-4f07-40cc-a667-4fc00480c21f",
  "sessionId": "79f9012f-eb35-4e80-8e55-564c1bc1b0c2"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Episode-level training for selective verification: Detailed median-tier projections",
  "sessionId": "79f9012f-eb35-4e80-8e55-564c1bc1b0c2"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Episode-level收敛至30-42%，selective verification效果有限，需rebalance为methodology-heavy paper 核心假设：['Episode-level训练收敛但未大幅超过40%阈值（borderline区间）', 'h-sweep大体展示预期趋势…",
  "leafUuid": "dc929bc0-4f07-40cc-a667-4fc00480c21f",
  "sessionId": "79f9012f-eb35-4e80-8e55-564c1bc1b0c2"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Episode-level training for selective verification: Detailed median-tier projections",
  "sessionId": "79f9012f-eb35-4e80-8e55-564c1bc1b0c2"
}
```

---
