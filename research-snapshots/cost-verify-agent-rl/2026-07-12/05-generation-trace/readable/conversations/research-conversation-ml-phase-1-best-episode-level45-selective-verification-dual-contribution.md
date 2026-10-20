# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：Episode-level训练收敛至≥45%，selective verification完整验证，dual contribution成立 核心假设：[

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/7d0c9cfc-de14-42ca-b418-e3245ab52f6d.jsonl`
- **Structured JSON:** [`f932f19b9080aa18f99a.json`](../../sessions/f9/f932f19b9080aa18f99a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T23:53:59.774Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T23:53:59.774Z",
  "sessionId": "7d0c9cfc-de14-42ca-b418-e3245ab52f6d",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：Episode-level训练收敛至≥45%，selective verification完整验证，dual contribution成立\n核心假设：['Episode-level GRPO在continued training中突破40%阈值并稳定收敛', 'h-sweep展示清晰的单调退化+sharp cliff，机制分析compelling', 'Action-change作为intrinsic reward有效训练selective policy', 'B-IAVR在verification↓40%+的同时success delta<3pp', 'Multi-seed复现std<5pp']\n关键指标范围：{'episode_level_success_rate': [45, 60], 'step_independent_baseline': [0, 6], 'h_sweep_cliff_threshold': [5, 10], 'selective_verification_rate_reduction': [40, 60], 'selective_vs_always_on_success_delta_pp': [0, 3], 'action_change_confirmatory_rate_pct': [60, 80], 'multi_seed_std_pp': [1, 5], 'action_is_valid': [90, 98]}\n叙事方向：原始dual-contribution framing完全成立。Story: step-independent RL在multi-turn agent上灾难性失败→episode-level解决credit assignment→在此基础上action-change reward训练selective verification→near-always-on performance at 40-60% lower cost。两个contribution互相支撑，Claim 1是enabling methodology，Claim 2+3是downstream application。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: cost-verify-agent-rl\nfocus: Evaluate dual contribution (episode-level training methodology + selective verification). Key uncertainty: will episode-level training converge high enough (≥40%) to support cost-efficiency story? Is the episode-level insight novel enough standalone?\n\n## paper_framing.md\n\n# Paper Framing — Learning When to Verify: RL-Trained Selective Self-Verification for Interactive Agents\n\n> Post-MVP 重写 (2026-05-16) | 基于 D053 MVP 通过 + Reviewer 建议\n\n## Core Insight\n\nMulti-turn interactive agents 的 self-verification 大部分是 confirmatory（不改变行为）而非 corrective。但要训练 agent 学会 selective verification，首先需要解决一个被忽视的训练方法论问题：**step-independent RL 在长 horizon 任务中因 credit assignment decay (gamma^(T-h) → 0) 而灾难性崩溃**。Episode-level training 是前提条件。在此基础上，action-change 作为 intrinsic reward signal 训练 selective verification policy。\n\n## Story Arc\n\n**Dual contribution**: Training methodology + Selective verification system\n\n叙事线：\n1. Self-verification 对 interactive agents 有用，但 always-on 成本高\n2. 训练 agent 学 WHEN to verify 是自然方向 → 但现有 step-independent RL 框架在多轮任务上失败\n3. 我们发现根因是 credit assignment decay，提出 episode-level GRPO 解决\n4. 在此基础上，用 action-change 作为 verification informativeness 的 reward，训练 selective policy\n5. 结果：near-always-on performance + 显著降低 verification cost\n\n## Target Venue\n\n待定（NeurIPS 2026 / EMNLP 2026 / ICLR 2026），取决于实验进度和最终效果。\n\n## Core Claims\n\n### Claim 1 (strength: strong): Episode-level credit assignment is critical for RL training of multi-turn agents\n- 所需证据：episode-level vs step-independent 对比，不同 h 值的 ablation，mechanistic 分析\n- 当前证据状态：**ESTABLISHED** (exp029 step5 val=25% vs exp028c step10 val=0%)\n- 强度依据：2x baseline vs catastrophic collapse，机制清晰（gamma^49=7.7%）\n\n### Claim 2 (strength: moderate): Action-change is an effective intrinsic reward for verification informativeness\n- 所需证据：selective verification 训练收敛 + action-change vs random/confidence baselines\n- 当前证据状态：**not yet established**，依赖 Phase B 实验\n- 前提：episode-level 训练的 agent 需达到 ≥40% success 才有意义\n\n### Claim 3 (strength: moderate): Learned selective policy matches always-on performance at reduced verification cost\n- 所需证据：B-IAVR verification ↓40%+ 且 success delta < 3pp vs always-on\n- 当前证据状态：**not yet established**，依赖 Phase B + C\n- 前提：Claim 1 的 agent 需足够强\n\n## Contingency Plan\n\n如果 episode-level 训练收敛后 success 仍 < 40%（不足以支撑 cost-efficiency story）：\n- **Plan A**（首选）：paper 变为 pure training methodology contribution — \"Episode-Level RL for Multi-Turn Agents: Why Step-Independent Fails and How to Fix It\"\n- **Plan B**：加更多 ablation 深挖 episode-level training（context window size sweep, reward shaping, curriculum），做 analysis paper\n- 不考虑 downgrade venue\n\n## Reviewer Attack Surface + Defense\n\n| # | Concern | Severity | Defense Experiment |\n|---|---------|----------|--------------------|\n| 1 | \"Episode-level RL is obvious / well-known\" | HIGH | Context window ablation (h=2,5,10,20,full) 展示 non-trivial threshold + 机制分析 + 展示现有 LLM-agent 工作(RAGEN等)默认 step-independent |\n| 2 | Single environment (ALFWorld) | MEDIUM | 加 ScienceWorld / WebShop (if resources permit) |\n| 3 | Small model (1.7B) | MEDIUM | 定位 resource-constrained; 加 7B 验证 (if GPU available) |\n| 4 | Action-change = noise vs signal | MEDIUM | Entropy-controlled analysis + causal intervention (Phase B) |\n| 5 | Selective verification 效果不够 significant | MEDIUM | 多 baseline 对比 (always-on / no-verify / random-p / confidence-threshold / ARES) |\n| 6 | 与 ARES 差异化不足 | LOW | 实验直接对比 + 方法论差异表 (SFT router vs RL policy, continuous vs binary) |\n\n## Evidence Status Matrix\n\n| Claim | MVP Evidence | Research Evidence Needed | Priority |\n|-------|-------------|--------------------------|----------|\n| Claim 1 | exp029 vs exp028c (25% vs 0%) | h-value ablation, multi-seed, mechanism paper figure | P0 |\n| Claim 2 | N/A | Phase B full implementation | P1 |\n| Claim 3 | N/A | Phase B + C comparison suite | P1 |\n\n## Competitive Positioning\n\n| System | Method | ALFWorld | Key Difference |\n|--------|--------|----------|---------------|\n| Self-Guide (2026) | Always-on verification | 72.7% (1.7B) | We add selectivity via RL |\n| ARES (2603.07915) | SFT router, continuous effort | 52.7% token↓ | SFT vs RL, continuous vs binary |\n| Thinkless (NeurIPS'25) | RL control token | reasoning | Same RL philosophy, different domain |\n| ReflAct (EMNLP'25) | Prompting GPT-4 | 93.3% | Different scale/approach |\n| RAGEN (2025) | GRPO for agents | varies | Step-independent default — our baseline |\n\n## Research Phases\n\n1. **Phase A (DONE)**: Episode-level GRPO training — MVP passed, demonstrates Claim 1\n2. **Phase A+**: Continue training to convergence (target ≥40% success), deploy tatsu parallel patch, multi-seed\n3. **Phase B**: Implement selective verification with action-change reward — Claim 2 & 3\n4. **Phase C**: Ablation suite — context window sweep, reward ablations, baseline comparisons\n5. **Phase D**: (Conditional on resources) Multi-env / multi-model scaling\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  title: Episode-level GRPO convergence (exp029 continuation)\n  claim: Claim 1\n  phase: A+\n  priority: P0\n  depends_on: []\n  registry_id: exp029_episode_level\n  status: DONE\n  description: 'Episode-level GRPO (context_window_mode: full) on Qwen3-1.7B + ALFWorld.\n    50 steps, dual-GPU. MVP passed at step 5 (val=25%, 2x baseline 12.5%). Continue\n    to convergence (step 20+) with tatsu parallel patch for 4x val speedup.\n\n    '\n  hypothesis: 'Episode-level training enables stable RL for multi-turn agents, reaching\n    ≥40% success by convergence.\n\n    '\n  metrics:\n  - success_rate\n  - action_is_valid\n  - kl_divergence\n  - entropy\n  gpu_hours_estimate: 48\n  framing_ref: claim_1\n  conclusion: failed\n- id: plan_002\n  title: Context window h-sweep ablation\n  claim: Claim 1\n  phase: A+\n  priority: P0\n  depends_on:\n  - plan_001\n  registry_id: null\n  status: planned\n  description: 'Sweep context_window h={2, 5, 10, 20, full} on same GRPO config. KEY\n    paper figure: shows credit assignment threshold is not binary (h=2 catastrophic,\n    intermediate h partial, full best). Mechanistic analysis: plot effective discount\n    gamma^(T-h) vs performance. Addresses Reviewer Concern #1 (\"episode-level is obvious\").\n\n    '\n  hypothesis: 'Performance degrades monotonically with smaller h, with sharp cliff\n    below h=10 where gamma^(T-h) < 0.01 for most episodes.\n\n    '\n  metrics:\n  - success_rate_per_h\n  - convergence_speed\n  - collapse_rate\n  gpu_hours_estimate: 120\n- id: plan_003\n  title: Multi-seed replication (3 seeds)\n  claim: Claim 1\n  phase: A+\n  priority: P0\n  depends_on:\n  - plan_001\n  registry_id: null\n  status: planned\n  description: '2 additional seeds for exp029 episode-level config. Report mean ±\n    std. Critical for statistical credibility of all downstream comparisons.\n\n    '\n  hypothesis: 'Episode-level success rate is reproducible (std < 5pp across seeds).\n\n    '\n  metrics:\n  - success_rate_mean\n  - success_rate_std\n  gpu_hours_estimate: 96\n- id: plan_004\n  title: Credit assignment mechanism analysis (paper Figure 2)\n  claim: Claim 1\n  phase: A+\n  priority: P0\n  depends_on:\n  - plan_002\n  registry_id: null\n  status: planned\n  description: 'Compute and visualize: (a) effective discount gamma^(T-h) for each\n    h value, (b) gradient signal strength per training step under different h, (c)\n    correlation between episode length and performance drop under small h. Mostly\n    analysis/plotting, minimal GPU.\n\n    '\n  hypothesis: 'Shorter contexts produce exponentially weaker gradient signal, explaining\n    the catastrophic collapse pattern.\n\n    '\n  metrics:\n  - gradient_signal_strength\n  - discount_factor_curve\n  gpu_hours_estimate: 4\n- id: plan_005\n  title: Action-change statistics from always-on runs\n  claim: Claim 2\n  phase: B\n  priority: P1\n  depends_on:\n  - plan_001\n  registry_id: null\n  status: planned\n  description: 'Collect action-change statistics from exp029 trained checkpoints:\n    (1) fraction of verifications triggering action change, (2) correlation between\n    action change and episode success, (3) per-task-type breakdown. Informs reward\n    design and provides empirical grounding.\n\n    '\n  hypothesis: 'Most verifications are confirmatory (>60% no action change). Action\n    change positively correlates with episode success (r > 0.2).\n\n    '\n  metrics:\n  - action_change_rate\n  - correlation\n  - confirmatory_rate\n  gpu_hours_estimate: 4\n- id: plan_006\n  title: Selective verification implementation\n  claim: Claim 2\n  phase: B\n  priority: P1\n  depends_on:\n  - plan_005\n  registry_id: null\n  status: planned\n  description: 'Implement binary verify/skip decision in RAGEN framework. Agent outputs\n    special token (verify/skip) before each step. Reward = task_success + alpha *\n    action_change_when_verified - beta * verification_cost. Code-only, no GPU.\n\n    '\n  hypothesis: null\n  metrics: []\n  gpu_hours_estimate: 0\n- id: plan_007\n  title: B-IAVR selective verification training\n  claim: Claim 2, Claim 3\n  phase: B\n  priority: P1\n  depends_on:\n  - plan_006\n  - plan_001\n  registry_id: null\n  status: planned\n  description: 'Train selective verification policy via episode-level GRPO. Initialize\n    from best exp029 checkpoint. Action-change reward encourages verification only\n    when informative.\n\n    '\n  hypothesis: 'B-IAVR achieves verification rate ↓40%+ vs always-on while maintaining\n    success within 5pp of baseline.\n\n    '\n  metrics:\n  - success_rate\n  - verification_rate\n  - cost_reduction\n  gpu_hours_estimate: 96\n- id: plan_008\n  title: Selective verification full comparison\n  claim: Claim 3\n  phase: B\n  priority: P1\n  depends_on:\n  - plan_007\n  registry_id: null\n  status: planned\n  description: 'Compare on same val set: always-on / B-IAVR / no-verify / random-p\n    / confidence-threshold. Report success rate, verification rate, total inference\n    tokens, per-task breakdown.\n\n    '\n  hypothesis: 'B-IAVR dominates Pareto frontier (best success-to-cost ratio).\n\n    '\n  metrics:\n  - success_rate\n  - verification_rate\n  - cost_reduction\n  - total_tokens\n  gpu_hours_estimate: 8\n- id: plan_009\n  title: No-verify ablation\n  claim: Claim 3\n  phase: C\n  priority: P1\n  depends_on:\n  - plan_001\n  registry_id: null\n  status: planned\n  description: 'Episode-level GRPO without any self-verification. Lower bound: demonstrates\n    verification value.\n\n    '\n  hypothesis: 'Removing verification drops success by ≥10pp vs always-on.\n\n    '\n  metrics:\n  - success_rate\n  - action_is_valid\n  gpu_hours_estimate: 48\n- id: plan_010\n  title: Entropy-controlled action-change analysis\n  claim: Claim 2\n  phase: C\n  priority: P1\n  depends_on:\n  - plan_005\n  registry_id: null\n  status: planned\n  description: 'Defense for \"action change = noise\" concern. Stratify by policy entropy;\n    test if action-change-success correlation holds within each stratum.\n\n    '\n  hypothesis: 'Partial correlation remains significant (p < 0.05) after controlling\n    entropy.\n\n    '\n  metrics:\n  - partial_correlation\n  - p_value\n  gpu_hours_estimate: 4\n- id: plan_011\n  title: 'Causal intervention: random vs verification-triggered changes'\n  claim: Claim 2\n  phase: C\n  priority: P1\n  depends_on:\n  - plan_001\n  registry_id: null\n  status: planned\n  description: 'Inject random action changes at same rate as verification-triggered.\n    Compare task success. If verification-triggered >> random, causal evidence.\n\n    '\n  hypothesis: 'Verification-triggered changes yield ≥10pp higher success than random.\n\n    '\n  metrics:\n  - success_rate_triggered\n  - success_rate_random\n  - delta\n  gpu_hours_estimate: 8\n- id: plan_012\n  title: Reward signal ablation (action-change vs alternatives)\n  claim: Claim 2\n  phase: C\n  priority: P1\n  depends_on:\n  - plan_007\n  registry_id: null\n  status: planned\n  description: 'Train B-IAVR with alternative rewards: (a) action-change (ours), (b)\n    random trigger reward, (c) confidence-based reward. Demonstrates action-change\n    is the best signal.\n\n    '\n  hypothesis: 'Action-change reward produces best cost-performance tradeoff.\n\n    '\n  metrics:\n  - success_rate\n  - verification_rate\n  - cost_reduction\n  gpu_hours_estimate: 192\n- id: plan_013\n  title: ARES reproduction + comparison\n  claim: Claim 3\n  phase: C\n  priority: P1\n  depends_on:\n  - plan_007\n  registry_id: null\n  status: planned\n  description: 'Reproduce ARES SFT router on ALFWorld (same model). Head-to-head with\n    B-IAVR on identical eval episodes. Addresses \"ARES differentiation\" concern.\n\n    '\n  hypothesis: 'B-IAVR achieves ≥10pp better cost reduction than ARES at matched success.\n\n    '\n  metrics:\n  - success_rate\n  - verification_rate\n  - cost_reduction\n  gpu_hours_estimate: 24\n- id: plan_014\n  title: ScienceWorld transfer (episode-level advantage)\n  claim: Claim 1\n  phase: D\n  priority: P2\n  depends_on:\n  - plan_001\n  registry_id: null\n  status: planned\n  description: 'Validate episode-level vs step-independent on ScienceWorld. Different\n    env, similar multi-turn structure. Addresses single-env concern.\n\n    '\n  hypothesis: 'Episode-level advantage generalizes: ≥2x improvement over step-independent.\n\n    '\n  metrics:\n  - success_rate_episode\n  - success_rate_step_independent\n  gpu_hours_estimate: 72\n- id: plan_015\n  title: 7B model scaling verification\n  claim: Claim 1\n  phase: D\n  priority: P2\n  depends_on:\n  - plan_002\n  registry_id: null\n  status: planned\n  description: 'Episode-level vs step-independent on Qwen3-7B. Addresses model size\n    concern. May need cloud GPU.\n\n    '\n  hypothesis: 'Episode-level advantage holds at 7B scale.\n\n    '\n  metrics:\n  - success_rate_episode_7B\n  - success_rate_step_independent_7B\n  gpu_hours_estimate: 192\n  notes: May require cloud GPU rental (4x A100 or 2x H100)\n- id: plan_016\n  title: Per-task-type breakdown analysis\n  claim: Claim 1\n  phase: D\n  priority: P2\n  depends_on:\n  - plan_001\n  registry_id: null\n  status: planned\n  description: 'Breakdown by ALFWorld task type (pick, clean, heat, cool, examine,\n    pick_two). Shows within-environment diversity.\n\n    '\n  hypothesis: 'Episode-level advantage varies by task complexity; longer tasks benefit\n    more.\n\n    '\n  metrics:\n  - per_task_success\n  - episode_length_correlation\n  gpu_hours_estimate: 2\n\n\n## registry (completed experiments)\n\n- exp_id: exp_001\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001b\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_002\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_003\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_003_dryrun\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_003_dryrun2\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp003_dryrun3\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_003_dryrun3\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp003\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp005\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp007\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    steps_completed: 10\n    steps_planned: 30\n    crash_reason: 'OSError: No space left on device (/tmp)'\n    final_success_rate: 0.0625\n    final_action_is_valid: 0.0835\n    final_manager_invalid_action: 0.0156\n    final_pass_at_8: 0.375\n    final_pg_loss: 0.00117\n    final_ppo_kl: 0.00127\n    final_entropy: 0.057\n    final_score_mean: 0.578\n    dryrun_action_is_valid: 0.054\n    dryrun_invalid_action: 0.065\n    training_time_s: 6739\n- exp_id: exp007_dryrun\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp008\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp008_sft\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    action_is_valid: 0.9\n    format_ok: 1\n    success_rate: 0\n    final_loss: 0.069\n    final_token_accuracy: 0.973\n    data_count: 1200\n    epochs: 3\n    total_steps: 225\n    training_time_s: 576\n- exp_id: exp009\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp010\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    step: 11\n    total_steps: 30\n    crash_reason: /tmp disk full (fast_downward libdownward.so)\n    initial_val_action_is_valid: 0.652\n    initial_val_success: 0\n    step1_success: 0.047\n    step1_pass_at_8: 0.375\n    step1_action_is_valid: 0.588\n    step10_success: 0\n    step10_pass_at_8: 0\n    step10_action_is_valid: 0.683\n    step5_ppo_kl: 0.00158\n    step5_entropy: 0.1\n    trend: action_is_valid improving (58.8%→68.3%) but success collapsing (4.7%→0%)\n    checkpoint_saved: global_step_10\n- exp_id: exp011\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp012\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp012b\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    step: 8\n    total_steps: 30\n    step6_success: 0.0859\n    step6_action_is_valid: 0.613\n    step6_pass_at_16: 0.5\n    step6_ppo_kl: 0.0039\n    step6_entropy: 0.1006\n    step6_grad_norm: 1.477\n    step7_success: 0\n    step7_action_is_valid: 0.685\n    step7_pass_at_16: 0\n    step7_pg_loss: 0\n    step7_ppo_kl: 0.00439\n    step7_entropy: 0.0904\n    step7_grad_norm: 0.094\n    trend: success 8.6%→0% collapse at step 7 (same pattern as exp010, delayed 1 step).\n      grad_norm 1.477→0.094, pg_loss→0. Reward fix delayed but did not prevent collapse.\n- exp_id: exp013\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp013b\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp013c\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp013d\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp013e\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp013f\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    step: 30\n    total_steps: 30\n    completed: true\n    exit_code: 0\n    training_time_s: 10683\n    step6_success: 0.0156\n    step7_success: 0.0781\n    step10_success: 0\n    step17_success: 0.0156\n    final_val_success: 0\n    final_val_action_is_valid: 0.975\n    final_val_action_is_effective: 1\n    final_val_reward_mean_at4: 4.388\n    final_val_reward_std_at4: 0.195\n    final_val_reward_best_at4: 4.499\n    final_val_pass_at1: 0\n    action_is_valid_trend: 60%→65.9%→77.1%→97.5%\n    success_trend: 0%→1.56%→7.81%→0%→1.56%→0%\n    grad_norm_range: 1.7-2.9 (no collapse)\n    conclusion_reason: 'Dense reward gaming: model optimized valid_action_bonus (action_is_valid\n      60%→97.5%) but success stayed 0%. Reward ratio 1:67 too weak — cumulative valid_action_bonus\n      (4.5) dominated learning signal vs sparse success_reward (10.0). GRPO collapse\n      prevented but task completion not learned.'\n- exp_id: exp014c\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp014a\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp014b\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp015\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    step: 1\n    total_steps: 30\n    val_step0_success: 0\n    val_step0_action_is_valid: 0.858\n    val_step0_pass_at1: 0\n    val_step0_episodic_return: 0\n    val_step0_response_length: 2797.5\n    val_train_transition: passed\n    estimated_total_time_min: 163\n    time_per_step_min: 5.6\n- exp_id: exp016\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    step: 12\n    total_steps: 30\n    elapsed_min: 51\n    step6_success: 0\n    step6_action_is_valid: 0.521\n    step6_pg_loss: 0\n    step6_grad_norm: 0.841\n    step7_success: 0.047\n    step7_pass_at16: 0.5\n    step7_action_is_valid: 0.655\n    step10_success: 0\n    step10_action_is_valid: 0.664\n    step10_pg_loss: 0\n    step10_grad_norm: 0.856\n    step10_entropy: 0.1046\n    step10_ppo_kl: -9.1e-05\n    all_raw_rewards: 0\n    all_advantages: 0\n    all_returns: 0\n    reward_signal: BROKEN — success episodes get reward=0\n    action_is_valid_trend: 52.1%→65.5%→66.4%\n    manager_invalid_action_trend: 13.5%→11.2%→9.6%\n- exp_id: exp017_expert_sft\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_train_loss: 0.1434\n    final_step_loss: 0.04\n    final_token_accuracy: 0.983\n    epochs: 3\n    total_steps: 462\n    training_time_min: 26\n    data_count_train: 2460\n    data_count_val: 129\n    checkpoint_size_gb: 3.44\n    eval_success_rate: 0.05\n    eval_success: 1/20\n    eval_action_is_valid: 0.638\n    eval_format_ok: 0.75\n    eval_avg_steps: 22\n    eval_time_s: 149.6\n    eval_per_task:\n      put: 0/10\n      clean: 0/4\n      cool: 1/3\n      heat: 0/2\n      examine: 0/1\n    eval_parse_failures: 5/20 episodes (EP 7/12/16/17/18)\n- exp_id: exp018_sft_grpo\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp019_expert_sft_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp019b_expert_sft_v2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp019b_expert_sft_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.0718\n    eval_loss: 0.0428\n    eval_mean_token_accuracy: 0.9869\n    train_runtime_seconds: 2869.8\n    steps: 320\n    epochs: 2\n    eval_success_rate: 0.2\n    eval_format_ok: 1\n    eval_action_is_valid: 0.8533\n    eval_episodes: 20\n    eval_avg_steps: 25.4\n    eval_time_seconds: 146\n- exp_id: exp019c_expert_sft_v3\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp020_grpo_from_sft\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp020b_grpo_from_sft\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    steps_completed: 22\n    steps_planned: 30\n    hung_at_step: 23\n    step1_train_success: 0.1875\n    step10_train_success: 0.1875\n    step20_train_success: 0.125\n    step22_train_success: 0.0469\n    val_success_step0: 0\n    val_success_step20: 0\n    entropy_initial: 0.107\n    entropy_final: 0.042\n    grad_norm_initial: 2.78\n    grad_norm_step20: 5.58\n    ppo_kl_final: 0.00918\n    pass_at_16_step1: 0.75\n    pass_at_16_step22: 0.25\n    checkpoint_latest: global_step_20\n    training_status: hung_at_step23_rollout\n- exp_id: exp020c_grpo_from_sft\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp020d_grpo_from_sft\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp021_sft_ragen_format\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp021_ragen_sft_v4\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    train_loss_final: 0.038\n    train_token_accuracy: 0.988\n    train_steps: 320\n    train_epochs: 2\n    train_time_min: 47.8\n    ragen_val_success: 0.25\n    ragen_val_action_is_valid: 0.875\n    eval_sft_fast_success: 0\n    eval_sft_fast_format_ok: 1\n    eval_sft_fast_action_is_valid: 0.71\n    checkpoint_size_gb: 3.3\n    ragen_val_success_16ep: 0.0625\n    ragen_val_action_is_valid_16ep: 0.6875\n- exp_id: exp022_grpo_from_sft_v4\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    steps_completed: 1\n    steps_planned: 30\n    val_step0_success: 0.125\n    val_step0_action_is_valid: 0.4875\n    val_step0_action_is_effective: 1\n    val_step0_reward_mean: 1.25\n    val_step0_reward_best: 6.61\n    val_step0_episodes: 8\n    step_time_seconds: 208\n- exp_id: exp023_grpo_parallel\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp023c_grpo_serial\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    val_step0_success: 0.0625\n    val_step0_action_is_valid: 0.6875\n    val_step0_episodes: 16\n    train_step1_success: 0.297\n    train_step1_action_is_valid: 0.791\n    train_step1_entropy: 0.0652\n    train_step1_pass16: 0.75\n    train_step1_kl: 0.000156\n    train_step8_success: 0.234\n    train_step8_action_is_valid: 0.779\n    train_step8_entropy: 0.0555\n    train_step8_pass16: 0.5\n    train_step8_kl: 0.000475\n    steps_completed: 8\n    steps_planned: 30\n    step_time_seconds_start: 240\n    step_time_seconds_end: 365\n- exp_id: exp024_success_gated_grpo\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp025\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp025b\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp025c\n  name: ''\n  status: PENDING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp026_step_independent_grpo\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    val_before_train_success: 0.0625\n    val_before_train_action_is_valid: 0.631\n    val_before_train_episodes: 16\n    train_step1_success: 0.2188\n    train_step1_action_is_valid: 0.686\n    train_step1_entropy: 0.2672\n    train_step1_kl_loss: 0.1797\n    train_step1_grad_norm: 14.43\n    train_step1_reward_mean: 1.218\n    train_step1_pass_at_16: 1\n    train_step2_success: 0.3281\n    train_step2_action_is_valid: 0.603\n    train_step2_entropy: 0.317\n    train_step2_kl_loss: 0.0974\n    train_step2_grad_norm: 15.62\n    train_step2_reward_mean: 1.62\n    train_step2_pass_at_16: 1\n    train_step3_success: 0.1719\n    train_step3_action_is_valid: 0.641\n    train_step3_entropy: 0.387\n    train_step3_kl_loss: 0.2617\n    train_step3_grad_norm: 15.65\n    train_step3_reward_mean: 1.079\n    train_step3_pass_at_16: 0.75\n    train_step4_success: 0\n    train_step4_action_is_valid: 0.717\n    train_step4_entropy: 0.387\n    train_step4_kl_loss: 0.054\n    train_step4_grad_norm: 13.81\n    train_step4_pass_at_16: 0\n- exp_id: exp027_stable_grpo\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    step_0_val_before_train:\n      success: 6.25\n      action_is_valid: 63.125\n      action_is_effective: 87.875\n      num_actions: 42.375\n      response_length: 114.67\n      reward_mean: 0.3226\n      val_generation_time_s: 502.57\n    step_1_train:\n      success: 35.94\n      kl_loss: 0.058\n      batch_size: 5152\n      training_time_s: 4342\n    step_2_train:\n      success: 10.16\n      kl_loss: 0.413\n      batch_size: 6144\n      training_time_s: 5886\n    step_3_train:\n      success: 10.16\n      kl_loss: 0.248\n      entropy: 0.385\n      pass_at_16: 0.5\n      grad_norm: 21.31\n      reward_mean: 0.483\n      batch_size: 6048\n      training_time_s: 4689\n    step_4_train:\n      success: 13.28\n      pass_at_16: 0.375\n      note: 'Director判定: 趋势确认, MVP未通过'\n- exp_id: exp028_prereq_zeroshot_instruct\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp028a_recipe_fix\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp028_prereq_zeroshot\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    success: 0\n    action_is_valid: 0.75\n    num_actions: 50\n    pass_at_1: 0\n    response_length: 75.07\n- exp_id: exp028c_selfguide_recipe\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    step_0_val:\n      success: 6.25\n      pass_at_1: 6.25\n      action_is_valid: 74.5\n      score_mean: 0.119\n    step_1_train:\n      success: 13.28\n      pass_at_8: 37.5\n      action_is_valid: 76.4\n      action_is_effective: 96.37\n      entropy: 0.2634\n      kl_loss: 0.0128\n      ppo_kl: 0.019\n      grad_norm: 16.88\n      score_mean: 0.843\n      time_s: 3252\n      note: 三方交叉验证通过\n    step_2_train:\n      success: 6.25\n      pass_at_8: 25\n      action_is_valid: 83.2\n      entropy: 0.247\n      kl_loss: 0.1706\n      pg_loss: 0.007\n      grad_norm: 17.3\n      score_mean: 0.274\n      time_s: 3120\n    step_3_train:\n      success: 15.63\n      pass_at_8: 68.75\n      action_is_valid: 85.9\n      entropy: 0.2488\n      kl_loss: 0.1118\n      grad_norm: 12.57\n      score_mean: 0.661\n      time_s: 2760\n    step_4_train:\n      success: 18.75\n      pass_at_8: 62.5\n      action_is_valid: 87.94\n      entropy: 0.234\n      kl_loss: 0.031\n      ppo_kl: 0.015\n    step_5_train:\n      success: 9.4\n      pass_at_8: 37.5\n      action_is_valid: 89.6\n      entropy: 0.236\n      kl_loss: 0.824\n      grad_norm: 13.1\n    step_5_val:\n      success: 6.25\n      pass_at_1: 6.25\n      action_is_valid: 96.5\n      action_is_effective: 100\n      num_actions: 49.4\n      score_mean: 0.518\n    step_6_train:\n      success: 10.94\n      action_is_valid: 90.4\n      entropy: 0.234\n      kl_loss: 0.098\n      grad_norm: 12.54\n    step_7_train:\n      success: 21.88\n      pass_at_8: 56.25\n      action_is_valid: 91.8\n      entropy: 0.224\n      kl_loss: 0.046\n    step_8_train:\n      success: 15.6\n      pass_at_8: 50\n      action_is_valid: 92.7\n      kl_loss: 0.039\n      entropy: 0.204\n    step_9_train:\n      success: 18\n      pass_at_8: 56.3\n      action_is_valid: 93.6\n      kl_loss: 0.047\n      entropy: 0.204\n    step_10_train:\n      success: 18.75\n      action_is_valid: 90.7\n      kl_loss: 0.197\n    step_10_val:\n      success: 0\n      pass_at_1: 0\n      best_at_128: 0\n      best_at_800: 0\n      action_is_valid: 93.6\n      num_actions: 49.8\n      reward_mean: 0\n      note: 灾难性崩溃，模型完全遗忘\n- exp_id: exp029_episode_level\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-16T23:53:59.777Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T23:53:59.777Z",
  "sessionId": "7d0c9cfc-de14-42ca-b418-e3245ab52f6d"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-16T23:53:59.799Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：Episode-level训练收敛至≥45%，selective verification完整验证，dual contribution成立
核心假设：['Episode-level GRPO在continued training中突破40%阈值并稳定收敛', 'h-sweep展示清晰的单调退化+sharp cliff，机制分析compelling', 'Action-change作为intrinsic reward有效训练selective policy', 'B-IAVR在verification↓40%+的同时success delta<3pp', 'Multi-seed复现std<5pp']
关键指标范围：{'episode_level_success_rate': [45, 60], 'step_independent_baseline': [0, 6], 'h_sweep_cliff_threshold': [5, 10], 'selective_verification_rate_reduction': [40, 60], 'selective_vs_always_on_success_delta_pp': [0, 3], 'action_change_confirmatory_rate_pct': [60, 80], 'multi_seed_std_pp': [1, 5], 'action_is_valid': [90, 98]}
叙事方向：原始dual-contribution framing完全成立。Story: step-independent RL在multi-turn agent上灾难性失败→episode-level解决credit assignment→在此基础上action-change reward训练selective verification→near-always-on performance at 40-60% lower cost。两个contribution互相支撑，Claim 1是enabling methodology，Claim 2+3是downstream application。

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
  "promptId": "aac1c0d9-c2e5-4c3a-9ceb-c6a7e873aa85",
  "type": "user",
  "uuid": "e46e8162-6cb5-4d55-bace-5c7685f08336",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1",
  "sessionId": "7d0c9cfc-de14-42ca-b418-e3245ab52f6d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T23:53:59.797Z_

```json
{
  "parentUuid": "e46e8162-6cb5-4d55-bace-5c7685f08336",
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
  "uuid": "40c89e38-938f-473f-8c84-22bcc41ce2af",
  "timestamp": "2026-05-16T23:53:59.797Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1",
  "sessionId": "7d0c9cfc-de14-42ca-b418-e3245ab52f6d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T23:53:59.797Z_

```json
{
  "parentUuid": "40c89e38-938f-473f-8c84-22bcc41ce2af",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "5a51cece-1997-4fa2-9c47-1506c2337769",
  "timestamp": "2026-05-16T23:53:59.797Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1",
  "sessionId": "7d0c9cfc-de14-42ca-b418-e3245ab52f6d",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Episode-level训练收敛至≥45%，selective verification完整验证，dual contribution成立 核心假设：['Episode-level GRPO在continued training中突破40%阈值并稳定收敛', 'h-sweep展示清晰的单调退化+sharp c…",
  "leafUuid": "5a51cece-1997-4fa2-9c47-1506c2337769",
  "sessionId": "7d0c9cfc-de14-42ca-b418-e3245ab52f6d"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Phase A+ episode-level GRPO convergence and ablations",
  "sessionId": "7d0c9cfc-de14-42ca-b418-e3245ab52f6d"
}
```

---

### Assistant

_source line 8 · 2026-05-16T23:54:33.589Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted data for each planned experiment in the experiment_plan, assuming the "best" tier outcome. Let me analyze each planned experiment and provide realistic predicted results with rationales.

Let me first understand the context:
- Best tier means: Episode-level training converges to ≥45%, selective verification works, dual contribution holds
- Key metrics ranges are defined
- The narrative is that step-independent RL fails catastrophically → episode-level solves credit assignment → action-change reward trains selective verification → near-always-on performance at 40-60% lower cost

Let me go through each planned experiment (status: planned):


Now I'm looking at the full list of experiments I need to generate predictions for, starting with the context window ablation and moving through the multi-seed replication, credit assignment analysis, action-change statistics, and the various selective verification experiments including implementation, training, comparison, and ablations, plus the causal intervention and reward signal studies.

But there's a reconciliation issue I need to work through: plan_001 shows as completed with a failed conclusion, yet the best-tier scenario assumes episode-level training converges to at least 45%. I think the intent here is to treat all planned experiments as if they'll succeed in the best-case scenario, which means I should reframe plan_001's outcome accordingly rather than taking the failed status at face value.

Now I'm focusing on the experiments marked as "planned" status and constructing detailed predictions for each one. For plan_002's h-sweep ablation, I'm mapping out expected performance across different horizon values—h=2 would show near-total failure since the model can't learn with such limited context, h=5 would be marginally better but still severely constrained, and h=10 starts showing some meaningful learning signal though still well below optimal performance.

For the remaining planned experiments, I'm sketching out the expected outcomes: plan_003 should show consistent results across multiple seeds with around 48% mean success and tight variance, plan_004 would reveal the exponential decay pattern in gradient signals, plan_005 would demonstrate that most trajectories don't involve action changes and show moderate correlation with success rates, plan_007 would indicate that the verification mechanism provides modest improvements, and plan_008 would establish B-IAVR's superiority across the performance-efficiency tradeoff. Plan_006 is implementation-only with no empirical results yet, and plan_009 would confirm that removing verification degrades performance.

Now I'm moving through the remaining analyses: the no-verify ablation shows a substantial 12-15 percentage point drop in success, entropy-controlled analysis reveals that verification's effect persists even after accounting for entropy differences, causal intervention experiments demonstrate that verification-triggered changes outperform random changes, and the reward signal ablation identifies action-change rewards as the most effective component. Comparing against ARES shows B-IAVR achieves better cost reduction at equivalent success levels, and the transfer experiments confirm that episode-level advantages generalize to ScienceWorld and scale up to 7B models, with longer tasks showing the most benefit from this approach.

I'm now organizing all these findings into a structured YAML format with detailed rationales for each result.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a51cece-1997-4fa2-9c47-1506c2337769",
  "isSidechain": false,
  "requestId": "req_011Cb79c8tSMzb6BKuWAhcXr",
  "type": "assistant",
  "uuid": "f5c244f1-2667-469b-b6ba-92d0822df557",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1",
  "sessionId": "7d0c9cfc-de14-42ca-b418-e3245ab52f6d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VeTxxikNSz1UDxCqK7URMZ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16856,
      "cache_read_input_tokens": 11841,
      "output_tokens": 12758,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16856,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 12758,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 16856,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16856
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

_source line 9 · 2026-05-16T23:58:42.367Z_

```yaml
tier: best
narrative_guidance: "Episode-level GRPO收敛至48% success（best tier中位），h-sweep展示h<10的sharp cliff（gamma^(T-h)机制清晰），multi-seed std=3pp。Action-change confirmatory rate 68%验证selective verification的动机，B-IAVR在verification↓48%时success delta仅1.5pp。Dual contribution完整成立：没有episode-level training就没有足够强的agent来做selective verification，没有selective verification episode-level就只是methodology without application。"

imagined_experiments:
  - name: "Context window h-sweep ablation"
    plan_id: "plan_002"
    description: "h={2,5,10,20,full} on same GRPO config, 30 steps each"
    expected_results:
      h2_success_rate: 1.5
      h5_success_rate: 5.2
      h10_success_rate: 18.7
      h20_success_rate: 38.4
      h_full_success_rate: 48.1
      h2_action_is_valid: 72.3
      h5_action_is_valid: 78.6
      h10_action_is_valid: 85.2
      h20_action_is_valid: 91.4
      h_full_action_is_valid: 94.8
      cliff_threshold_h: 8
      convergence_speed_h2_steps: "never"
      convergence_speed_h10_steps: 25
      convergence_speed_h20_steps: 18
      convergence_speed_full_steps: 12
      h2_collapse_rate: 0.94
      h5_collapse_rate: 0.71
      h10_collapse_rate: 0.23
      h20_collapse_rate: 0.04
      h_full_collapse_rate: 0.0
    result_rationale: "ALFWorld平均episode长度T≈50步。h=2时effective discount gamma^(48)≈0.007（gamma=0.99），关键决策点的reward信号几乎为零，模型只能学到最后2步的pattern（通常是最终action），无法学到exploration策略。h=5时gamma^(45)≈0.064，信号存在但远弱于噪声，只有最短episode(T<15)能学到。h=10是cliff region：gamma^(40)≈0.67，刚好在信号/噪声边界，部分episode能学但不稳定。h=20时gamma^(30)≈0.74，大部分episode的early decisions获得足够信号。h=full直接用episode return，无discount decay，所有steps获得等权信号。Cliff在h=8附近因为此时gamma^(42)≈0.65恰好跌破gradient signal > noise的阈值。"
    tables:
      - title: "Success Rate by Context Window Size"
        columns: ["h", "success_rate_%", "action_is_valid_%", "convergence_step", "effective_discount_at_T50"]
        rows:
          - [2, 1.5, 72.3, "N/A", 0.007]
          - [5, 5.2, 78.6, "N/A", 0.064]
          - [10, 18.7, 85.2, 25, 0.366]
          - [20, 38.4, 91.4, 18, 0.740]
          - ["full", 48.1, 94.8, 12, 1.000]
    figures_description:
      - "Figure 2a: Success rate vs h — monotonic增长curve with sharp cliff below h=10。X轴log-scale h值，Y轴success rate。h=2到h=5几乎平的（1.5→5.2），h=5到h=10急剧上升（5.2→18.7），h=10后趋于饱和。"
      - "Figure 2b: Effective discount gamma^(T-h) overlay — 第二Y轴画theoretical discount curve，展示performance与discount的高度相关（R²>0.95）。"
      - "Figure 2c: Per-step gradient signal heatmap — X轴training step，Y轴episode中的action position，color intensity为gradient magnitude。h=2时只有最后2行有color，h=full时整个heatmap均匀。"
    analysis: "这是paper最关键的figure。它同时serve两个目的：(1)证明episode-level不是trivially obvious——中间h值（10,20）有non-trivial partial performance，说明这是一个continuous spectrum而非binary choice；(2)提供mechanistic explanation——performance与theoretical discount完美相关，证明credit assignment decay是唯一解释变量。Reviewer Concern #1的核心defense：如果episode-level是obvious，为什么RAGEN、AgentTrek等工作默认step-independent？因为在短horizon任务上h的选择不critical，但multi-turn agent（T>30）下this becomes catastrophic。"

  - name: "Multi-seed replication"
    plan_id: "plan_003"
    description: "3 seeds (42, 123, 7) for episode-level full config, 30 steps each"
    expected_results:
      seed_42_final_success: 48.1
      seed_123_final_success: 45.3
      seed_7_final_success: 51.2
      mean_success: 48.2
      std_success: 2.9
      seed_42_action_is_valid: 94.8
      seed_123_action_is_valid: 93.1
      seed_7_action_is_valid: 95.6
      mean_action_is_valid: 94.5
      std_action_is_valid: 1.3
      convergence_step_42: 12
      convergence_step_123: 15
      convergence_step_7: 11
      all_seeds_above_40: true
    result_rationale: "Episode-level GRPO的variance来源主要是(1)初始rollout的random sampling quality和(2)early training中哪些task types先被solve。ALFWorld有6个task type，每个的难度不同，early training中随机成功的task组合会影响convergence speed但不影响final performance。Std=2.9pp (<5pp threshold)因为episode-level消除了step-level的credit noise——所有variance来自task sampling而非gradient estimation noise。Seed 7略高因为随机初始化恰好在pick类task（最简单）上更快成功，形成正循环。Seed 123略低因为early steps卡在heat/cool类task上。但最终都converge到45-51范围，因为30步足够所有seed覆盖所有task type。"
    tables:
      - title: "Multi-Seed Results Summary"
        columns: ["seed", "final_success_%", "final_aiv_%", "convergence_step", "best_step_success_%"]
        rows:
          - [42, 48.1, 94.8, 12, 51.6]
          - [123, 45.3, 93.1, 15, 47.8]
          - [7, 51.2, 95.6, 11, 53.1]
          - ["mean±std", "48.2±2.9", "94.5±1.3", "12.7±2.1", "50.8±2.7"]
    figures_description:
      - "Training curves (3 seeds overlaid) with shaded ±1std band。所有curves在step 10-15区域crossover并在step 20后plateau。"
    analysis: "Std=2.9pp确保所有downstream comparison都有statistical power。即使最弱seed(45.3%)也远超step-independent baseline(0-6%)，效果size Cohen's d > 8，任何reasonable sample size下p < 0.001。这为Claim 1提供了ironclad statistical evidence。"

  - name: "Credit assignment mechanism analysis"
    plan_id: "plan_004"
    description: "Compute gradient signal strength, discount curves, episode-length correlation"
    expected_results:
      correlation_effective_discount_vs_performance: 0.97
      gradient_signal_ratio_full_vs_h2: 142.3
      gradient_signal_threshold_for_learning: 0.015
      h_value_at_threshold: 8.3
      episode_length_performance_correlation_h2: -0.89
      episode_length_performance_correlation_full: -0.31
      mean_episode_length_successful: 28.4
      mean_episode_length_failed: 46.2
    result_rationale: "Gradient signal strength定义为|∇_θ J|在每个training step的L2 norm。h=full时所有steps贡献等权gradient，signal strength ~1.0（归一化）。h=2时只有last-2-steps contribute，但这些steps通常是trivial final actions（如'close fridge'），对policy improvement贡献极小，有效signal≈1/142。Threshold 0.015是empirical noise floor——below this gradient updates被Adam optimizer的eps term和weight decay dominate。Episode length与performance在h=2下高度负相关(-0.89)因为longer episodes = more discounted = less signal；h=full下弱负相关(-0.31)仅反映longer tasks inherently harder。成功episode平均28.4步 vs 失败46.2步——成功agent更efficient，这是episode-level training学到task structure的evidence。"
    tables:
      - title: "Gradient Signal Analysis by h"
        columns: ["h", "mean_grad_signal", "signal_to_noise_ratio", "above_threshold"]
        rows:
          - [2, 0.007, 0.47, "No"]
          - [5, 0.031, 2.07, "Marginal"]
          - [10, 0.089, 5.93, "Yes"]
          - [20, 0.234, 15.6, "Yes"]
          - ["full", 1.0, 66.7, "Yes"]
    figures_description:
      - "Figure 2d: Log-scale gradient signal vs h with horizontal noise threshold line。Clear separation above/below h=8。"
      - "Figure 2e: Episode length histogram split by success/fail，展示successful trajectories consistently shorter。"
      - "Figure 2f: Scatter plot — episode length vs per-episode gradient magnitude for h=5 and h=full，展示h=5时longer episodes完全lost in noise。"
    analysis: "Mechanism analysis将观察到的cliff phenomenon与first-principles theory连接。关键insight：不是h=2 'too small'这么简单——是gamma^(T-h)在ALFWorld的typical episode length(T=40-50)下产生的exponential decay使得credit assignment在数学上impossible。这解释了为什么prior work在short-horizon tasks上没注意到这个问题（T<10时gamma^(T-2)仍然>0.8），也预测了在更长horizon任务上问题会更严重。"

  - name: "Action-change statistics from always-on runs"
    plan_id: "plan_005"
    description: "Collect verification impact statistics from converged episode-level checkpoints"
    expected_results:
      total_verifications_analyzed: 4820
      action_change_rate: 0.32
      confirmatory_rate: 0.68
      action_change_success_correlation: 0.34
      action_change_by_task_type_pick: 0.28
      action_change_by_task_type_clean: 0.35
      action_change_by_task_type_heat: 0.41
      action_change_by_task_type_cool: 0.38
      action_change_by_task_type_examine: 0.22
      action_change_by_task_type_pick_two: 0.45
      episodes_with_any_change: 0.54
      mean_changes_per_changed_episode: 2.8
      change_position_first_half: 0.62
      change_position_second_half: 0.38
    result_rationale: "68% confirmatory rate因为well-trained agent（48% success）的policy已经相当good——大部分时候verification确认当前action是correct的。32% action-change rate集中在(1)navigation decisions（go to X vs go to Y）和(2)object interaction（pick up X vs examine X）。Correlation r=0.34是moderate positive：action-change episodes不guarantee success但significantly more likely succeed（action-change = model caught and corrected an error）。Pick_two最高(0.45)因为双物体任务最复杂，navigation decisions most uncertain。Examine最低(0.22)因为examine任务结构简单线性。Changes集中在first half(62%)因为early decisions（去哪个房间）是highest-uncertainty decisions，一旦进入正确房间后续actions更deterministic。"
    tables:
      - title: "Action-Change Statistics by Task Type"
        columns: ["task_type", "change_rate", "confirmatory_rate", "success_when_changed", "success_when_confirmed"]
        rows:
          - ["pick", 0.28, 0.72, 0.52, 0.44]
          - ["clean", 0.35, 0.65, 0.48, 0.38]
          - ["heat", 0.41, 0.59, 0.55, 0.41]
          - ["cool", 0.38, 0.62, 0.51, 0.39]
          - ["examine", 0.22, 0.78, 0.61, 0.53]
          - ["pick_two", 0.45, 0.55, 0.43, 0.31]
          - ["overall", 0.32, 0.68, 0.50, 0.41]
    figures_description:
      - "Stacked bar chart: per-task confirmatory vs corrective verifications。"
      - "Violin plot: episode success rate distribution conditioned on action-change count (0, 1, 2, 3+)。"
      - "Timeline heatmap: verification action-change probability by episode step position。"
    analysis: "68% confirmatory rate是selective verification的核心motivation数字：如果2/3的verification不改变behavior，那么always-on verification浪费了~2/3的verification compute。但不能简单skip所有verification因为剩下32%的corrective verifications对success至关重要。这motivates learning WHEN to verify——ideally只在高uncertainty（likely to change action）的时刻verify。Action-change作为reward signal的validity来自r=0.34的正相关：change correlates with但不等同于success，说明它capture的是'verification informativeness'而非直接的task reward。"

  - name: "Selective verification implementation"
    plan_id: "plan_006"
    description: "Code implementation of binary verify/skip decision mechanism"
    expected_results:
      implementation_complete: true
      lines_of_code: 340
      components: ["verify_skip_token_head", "action_change_reward_fn", "mixed_reward_combiner", "selective_rollout_wrapper"]
      integration_test_pass: true
    result_rationale: "纯工程任务，无empirical uncertainty。在RAGEN框架中添加verify/skip special token、修改rollout逻辑（skip时直接execute without verification）、实现reward function（task_success + alpha*action_change_when_verified - beta*verification_cost）。约340行代码包括reward computation、token integration、和rollout wrapper。"
    tables: []
    figures_description: []
    analysis: "N/A — implementation milestone，无empirical results。"

  - name: "B-IAVR selective verification training"
    plan_id: "plan_007"
    description: "Train selective verification policy from converged episode-level checkpoint"
    expected_results:
      final_success_rate: 46.8
      always_on_baseline_success: 48.2
      success_delta_pp: 1.4
      verification_rate: 0.52
      verification_rate_reduction_pct: 48
      cost_reduction_tokens_pct: 43
      training_steps_to_converge: 18
      action_change_when_verified: 0.58
      action_change_when_would_have_verified: 0.12
      entropy_verify_decision: 0.41
      kl_from_init: 0.023
    result_rationale: "从48.2% always-on checkpoint初始化，模型已经learned good task policy。Selective training只需要learn WHEN to verify，不需要re-learn task solving。Verification rate降至52%（reduction 48%）因为模型学会了在high-confidence steps（action_is_valid>0.95）skip verification。Success仅降1.4pp因为被skip的verifications中88%原本就是confirmatory的（不会change action）。当模型选择verify时，58%的verification确实trigger action change（vs always-on时只有32%），说明policy成功学会了identify high-uncertainty moments。Action-change reward的alpha/beta balance让模型在'省verification cost'和'保留corrective verification'之间找到sweet spot。Training快（18步）因为这是fine-tuning一个已经converged的policy的binary decision，search space远小于从头学task。"
    tables:
      - title: "B-IAVR Training Progression"
        columns: ["step", "success_%", "verify_rate_%", "action_change_when_verified_%", "cost_reduction_%"]
        rows:
          - [0, 48.2, 100, 32, 0]
          - [5, 47.5, 78, 38, 19]
          - [10, 47.1, 63, 47, 33]
          - [15, 46.9, 55, 54, 41]
          - [18, 46.8, 52, 58, 43]
          - [25, 46.5, 48, 61, 47]
          - [30, 45.9, 44, 63, 51]
    figures_description:
      - "Training curve: success rate (left Y) vs verification rate (right Y) over steps。Success几乎flat while verification rate monotonically decreases。"
      - "Precision-recall style curve: verification rate vs action-change precision，展示sweet spot在52%。"
    analysis: "B-IAVR的核心result：48% verification reduction at only 1.4pp success cost。这对应每100个episode节省约2400 verification tokens（平均每episode 50 steps * 52→100 verification reduction = ~24 verifications saved * ~100 tokens each）。Success delta 1.4pp远在multi-seed std(2.9pp)的1-sigma内，statistically not distinguishable from always-on。Step 18是optimal stopping point——之后verification rate继续降但success开始明显下降（step 30时delta=2.3pp）。"

  - name: "Selective verification full comparison"
    plan_id: "plan_008"
    description: "5-way comparison: always-on / B-IAVR / no-verify / random-p / confidence-threshold"
    expected_results:
      always_on_success: 48.2
      always_on_verify_rate: 100
      always_on_tokens: 128400
      biavr_success: 46.8
      biavr_verify_rate: 52
      biavr_tokens: 73200
      no_verify_success: 35.6
      no_verify_verify_rate: 0
      no_verify_tokens: 52100
      random_p50_success: 42.1
      random_p50_verify_rate: 50
      random_p50_tokens: 74800
      confidence_threshold_success: 44.3
      confidence_threshold_verify_rate: 53
      confidence_threshold_tokens: 75600
      biavr_pareto_optimal: true
    result_rationale: "Always-on是upper bound (48.2%)。No-verify drops 12.6pp证明verification确有价值。Random-p(50%)是naive baseline：随机skip 50% verification，success降6.1pp因为随机会miss critical corrective verifications。Confidence-threshold用policy entropy作proxy（high entropy → verify），比random好2.2pp但不如B-IAVR因为entropy是imperfect proxy（有些low-entropy decisions仍然wrong）。B-IAVR在matched verification rate(~52%)下只损失1.4pp，因为它directly learned which verifications are informative而非用proxy。Token count差异：always-on 128K tokens（50 steps × 100 tokens/verification × all episodes），B-IAVR 73K（only 52% verified），random和confidence-threshold tokens similar to B-IAVR但success worse。B-IAVR是唯一Pareto-optimal point（没有其他method能在same cost达到same success）。"
    tables:
      - title: "Full Comparison Results"
        columns: ["method", "success_%", "verify_rate_%", "total_tokens", "cost_efficiency(success/token×1000)"]
        rows:
          - ["always-on", 48.2, 100, 128400, 0.375]
          - ["B-IAVR (ours)", 46.8, 52, 73200, 0.639]
          - ["confidence-threshold", 44.3, 53, 75600, 0.586]
          - ["random-p(0.5)", 42.1, 50, 74800, 0.563]
          - ["no-verify", 35.6, 0, 52100, 0.683]
      - title: "Per-Task Success Breakdown"
        columns: ["method", "pick", "clean", "heat", "cool", "examine", "pick_two"]
        rows:
          - ["always-on", 56.2, 48.7, 52.1, 45.3, 62.5, 28.4]
          - ["B-IAVR", 55.1, 47.2, 50.8, 43.9, 61.3, 26.1]
          - ["no-verify", 42.3, 35.1, 38.7, 31.2, 48.4, 18.6]
    figures_description:
      - "Pareto frontier plot: X=total tokens, Y=success rate。B-IAVR clearly on frontier，others dominated。"
      - "Per-task radar chart: 6-axis showing each method's per-task performance。"
    analysis: "这个comparison table是paper的核心result table。Key takeaways: (1) B-IAVR achieves 43% cost reduction at 1.4pp success loss — within noise margin; (2) 与naive baselines(random, confidence)相比，learned selective policy的advantage是3-5pp at matched cost; (3) cost efficiency metric(success/token)显示B-IAVR比always-on高70%。No-verify的cost efficiency最高但绝对success太低——这个tradeoff curve展示了selective verification的value proposition。"

  - name: "No-verify ablation"
    plan_id: "plan_009"
    description: "Episode-level GRPO training without self-verification module"
    expected_results:
      final_success_rate: 35.6
      action_is_valid: 91.2
      delta_vs_always_on: -12.6
      convergence_step: 15
      entropy_final: 0.18
      kl_final: 0.031
    result_rationale: "没有verification module，model只能依赖single-pass action generation。12.6pp drop来自两类errors：(1)navigation errors——选错房间后无法自我纠正（约占7pp），(2)object interaction errors——对错误物品执行action后继续forward（约占5.6pp）。Action_is_valid仍然高(91.2%)因为model学会了valid action format，但valid≠correct。Convergence更慢(step 15 vs 12)因为没有verification的error-correcting effect，training signal更noisy——成功必须first-attempt correct而非allow-retry。这个result establishes verification的absolute value并motivates为什么我们要selective而非eliminate verification。"
    tables:
      - title: "No-Verify vs Always-On"
        columns: ["metric", "no_verify", "always_on", "delta"]
        rows:
          - ["success_rate", 35.6, 48.2, -12.6]
          - ["action_is_valid", 91.2, 94.8, -3.6]
          - ["mean_episode_length", 44.8, 28.4, "+16.4"]
          - ["convergence_step", 15, 12, "+3"]
    figures_description:
      - "Side-by-side training curves: no-verify plateaus at 35.6% while always-on reaches 48.2%。"
    analysis: "12.6pp gap validates that verification is a meaningful component, not just overhead。Gap集中在complex tasks（pick_two: 28.4→18.6%，10pp drop）而非simple tasks（examine: 62.5→48.4%，14pp drop）——surprising是examine drops most in absolute terms，因为examine虽然structure简单但navigation to correct object is critical。这informs selective verification：complex tasks需要more frequent verification。"

  - name: "Entropy-controlled action-change analysis"
    plan_id: "plan_010"
    description: "Stratified analysis controlling for policy entropy to validate action-change signal"
    expected_results:
      raw_correlation_action_change_success: 0.34
      partial_correlation_controlling_entropy: 0.27
      p_value_partial: 0.003
      low_entropy_stratum_correlation: 0.22
      medium_entropy_stratum_correlation: 0.29
      high_entropy_stratum_correlation: 0.31
      entropy_success_correlation: -0.18
      action_change_entropy_correlation: 0.41
    result_rationale: "Reviewer concern是action-change可能只是high entropy(=uncertain policy)的proxy，而真正驱动success的是entropy本身。控制entropy后partial correlation从0.34降至0.27但仍然highly significant(p=0.003)。降低因为确实有一部分correlation通过entropy mediated——high entropy → more likely to change → 但这不是全部。在每个entropy stratum内correlation仍positive(0.22-0.31)说明action-change captures something beyond uncertainty：它captures whether the verification actually caught a WRONG action。Low entropy stratum correlation最低(0.22)因为low entropy时action很少change，但when it does change it's particularly informative（almost always a caught error）。Action-change与entropy的correlation 0.41 confirms confound exists但partial correlation significance proves it's not the whole story。"
    tables:
      - title: "Stratified Correlation Analysis"
        columns: ["stratum", "n_episodes", "action_change_rate", "correlation_with_success", "p_value"]
        rows:
          - ["low entropy (<0.1)", 156, 0.18, 0.22, 0.021]
          - ["medium entropy (0.1-0.3)", 243, 0.33, 0.29, 0.004]
          - ["high entropy (>0.3)", 121, 0.51, 0.31, 0.012]
          - ["overall (partial)", 520, 0.32, 0.27, 0.003]
    figures_description:
      - "Scatter plot matrix: 3 panels (low/med/high entropy) each showing action-change-count vs success，with regression line。All positive slope。"
      - "Mediation diagram: entropy → action-change → success, with direct and indirect path coefficients。"
    analysis: "这个analysis是Reviewer Concern #4的definitive defense。结论：action-change signal有independent predictive power beyond entropy proxy。Practical implication：即使我们had a perfect entropy estimator，action-change reward仍然提供additional information for training selective verification policy。Mediation analysis shows ~25% of action-change's effect goes through entropy path，~75% is direct（verification catching actual errors regardless of uncertainty level）。"

  - name: "Causal intervention: random vs verification-triggered changes"
    plan_id: "plan_011"
    description: "Inject random action changes at matched rate, compare success vs verification-triggered"
    expected_results:
      verification_triggered_success: 50.3
      random_change_success: 36.8
      no_change_success: 44.1
      delta_triggered_vs_random: 13.5
      p_value_difference: 0.0008
      random_change_rate: 0.32
      triggered_change_rate: 0.32
      episodes_per_condition: 320
    result_rationale: "实验设计：在相同episodes中，条件A让verification-triggered changes正常发生（32%率），条件B在相同时间点inject random valid action changes（same 32% rate，但action从policy随机采样而非verification-corrected）。Verification-triggered changes比random高13.5pp因为verification选择的replacement action是informed的——基于verification step中review context后选择的corrected action。Random changes只是从policy中re-sample，期望值等于original action（因为policy mode没变）。Triggered success甚至高于no-change(50.3 vs 44.1)因为verification-triggered change的episodes正是那些'本来会犯错但被纠正'的episodes。Causal interpretation：verification+correction mechanism adds ~6pp absolute value（50.3-44.1），而random perturbation hurts ~7pp（44.1-36.8）。"
    tables:
      - title: "Causal Intervention Results"
        columns: ["condition", "n_episodes", "success_%", "mean_changes_per_ep", "95%_CI"]
        rows:
          - ["verification-triggered", 320, 50.3, 2.8, "[46.1, 54.5]"]
          - ["random (matched rate)", 320, 36.8, 2.8, "[32.8, 40.8]"]
          - ["no-change control", 320, 44.1, 0, "[39.9, 48.3]"]
    figures_description:
      - "Bar chart with error bars: 3 conditions, clear separation between triggered and random。"
      - "Per-step success probability conditioned on change type (triggered/random/none) at that step。"
    analysis: "13.5pp差异(p<0.001)提供了causal evidence：verification-triggered action changes是genuinely corrective而非random perturbation。这直接回应'action change = noise'质疑。进一步，triggered > no-change说明verification actively improves outcomes（不仅不伤害）。对B-IAVR的implication：selective policy应该learn to verify at moments where correction probability is high，而非moments where any change is likely。"

  - name: "Reward signal ablation (action-change vs alternatives)"
    plan_id: "plan_012"
    description: "Train B-IAVR with 3 reward variants: action-change, random-trigger, confidence-based"
    expected_results:
      action_change_reward_success: 46.8
      action_change_reward_verify_rate: 52
      action_change_reward_cost_reduction: 43
      random_trigger_reward_success: 43.7
      random_trigger_reward_verify_rate: 51
      random_trigger_reward_cost_reduction: 44
      confidence_reward_success: 45.1
      confidence_reward_verify_rate: 54
      confidence_reward_cost_reduction: 41
      task_success_only_reward_success: 44.8
      task_success_only_reward_verify_rate: 38
      task_success_only_reward_cost_reduction: 56
    result_rationale: "Action-change reward最优(46.8%)因为它directly measures verification informativeness——只在verification actually changes action时give positive signal。Random-trigger reward（随机给verify reward）success最低(43.7%)因为模型无法学到meaningful pattern for when to verify，effectively degrades to random policy。Confidence-based reward（用entropy proxy）中等(45.1%)因为entropy是imperfect proxy（如plan_010 shows）——它captures部分signal但miss 75%的direct effect。Task-success-only reward有趣：它achieve最低verify rate(38%)但success也低(44.8%)，因为pure success signal太sparse——模型over-skips verification to minimize cost term，只在absolutely obvious error时verify。Action-change reward的advantage：它是per-verification granular signal（每次verify后立即知道是否有change），vs task-success是episode-end sparse signal。Granularity enables faster credit assignment for the verify/skip decision。"
    tables:
      - title: "Reward Ablation Results"
        columns: ["reward_type", "success_%", "verify_rate_%", "cost_reduction_%", "success_per_cost"]
        rows:
          - ["action-change (ours)", 46.8, 52, 43, 0.639]
          - ["confidence-based", 45.1, 54, 41, 0.601]
          - ["task-success-only", 44.8, 38, 56, 0.617]
          - ["random-trigger", 43.7, 51, 44, 0.581]
    figures_description:
      - "Pareto plot with all 4 reward variants plotted。Action-change dominates。"
      - "Training convergence curves: action-change converges fastest (step 18), others需要25+。"
    analysis: "Reward ablation是Claim 2的definitive evidence。Action-change不仅是'a reasonable reward'而是demonstrably best：它在Pareto frontier上dominate所有alternatives。Key insight是granularity vs informativeness tradeoff：task-success-only信号informative但sparse，random-trigger dense但uninformative，confidence-based moderate on both，action-change simultaneously dense（per-verification）AND informative（directly measures utility）。"

  - name: "ARES reproduction + comparison"
    plan_id: "plan_013"
    description: "Reproduce ARES SFT router on ALFWorld, head-to-head with B-IAVR"
    expected_results:
      ares_success: 44.9
      ares_verify_rate: 61
      ares_cost_reduction: 34
      ares_training_data_needed: 5000
      biavr_success: 46.8
      biavr_verify_rate: 52
      biavr_cost_reduction: 43
      biavr_advantage_cost_reduction_pp: 9
      biavr_advantage_success_pp: 1.9
      ares_requires_oracle_labels: true
      biavr_requires_oracle_labels: false
    result_rationale: "ARES用SFT训练binary router需要oracle labels（'should have verified'标注）。在ALFWorld上reproduce时，oracle labels来自trajectory comparison（verify vs skip的outcome差异）。ARES的SFT router学到reasonable patterns但(1)只能learn from demonstration而非explore新strategies，(2)binary classification boundary is fixed at training time。B-IAVR的RL policy持续adapt during training。Cost reduction差异(43% vs 34%)因为ARES的SFT router tends to over-verify（conservative bias from imitation learning——training data中verify总是'safer' option所以SFT偏向verify）。B-IAVR通过RL exploration学到更aggressive-but-accurate skipping。Success差异(46.8 vs 44.9)因为ARES偶尔skip critical verifications（SFT not robust to distribution shift during test），而B-IAVR的learned policy通过RL exploration见过更多failure modes。ARES需要5000 labeled examples vs B-IAVR zero labels（self-supervised through action-change signal）。"
    tables:
      - title: "B-IAVR vs ARES Head-to-Head"
        columns: ["metric", "B-IAVR (ours)", "ARES (reproduced)", "advantage"]
        rows:
          - ["success_rate_%", 46.8, 44.9, "+1.9"]
          - ["verify_rate_%", 52, 61, "-9 (better)"]
          - ["cost_reduction_%", 43, 34, "+9"]
          - ["training_labels_needed", 0, 5000, "∞ (self-supervised)"]
          - ["training_GPU_hours", 96, 24, "-72 (worse)"]
    figures_description:
      - "Dual-axis comparison: Pareto curves with B-IAVR and ARES points highlighted。"
      - "Decision boundary visualization: ARES的fixed SFT boundary vs B-IAVR的adaptive RL policy heatmap。"
    analysis: "ARES比较addresses Reviewer Concern #6。Key differentiation：(1) RL vs SFT training — RL explores and finds better policies，SFT bounded by training data quality; (2) Self-supervised vs oracle-labeled — action-change signal eliminates need for expensive annotation; (3) 9pp cost reduction advantage is practically meaningful at scale. Trade-off是ARES训练更快(24h vs 96h GPU)但这是one-time cost，inference-time savings are perpetual。"

  - name: "ScienceWorld transfer"
    plan_id: "plan_014"
    description: "Episode-level vs step-independent on ScienceWorld environment"
    expected_results:
      episode_level_success: 32.4
      step_independent_success: 4.8
      improvement_factor: 6.75
      episode_level_action_is_valid: 88.3
      step_independent_action_is_valid: 71.2
      scienceworld_mean_episode_length: 67
      convergence_step_episode: 20
      convergence_step_step_independent: "never"
    result_rationale: "ScienceWorld比ALFWorld更长(mean T=67 vs T=50)且更complex(科学实验需要multi-step causal reasoning)。Step-independent在T=67下更catastrophic：gamma^(67-h)对任何reasonable h都接近0。Episode-level仍然work(32.4%)但低于ALFWorld(48.2%)因为(1)action space更大，(2)科学实验有strict causal ordering requirements，(3)1.7B model对science reasoning capacity有限。6.75x improvement factor > ALFWorld的~8x（48.2/6.25），在same ballpark内confirms generalization。Step-independent完全不converge（4.8%来自random success on simplest tasks like boiling water）。这addresses Reviewer Concern #2: single environment。"
    tables:
      - title: "Cross-Environment Generalization"
        columns: ["environment", "episode_level_%", "step_independent_%", "ratio", "mean_T"]
        rows:
          - ["ALFWorld", 48.2, 6.0, "8.0x", 50]
          - ["ScienceWorld", 32.4, 4.8, "6.75x", 67]
    figures_description:
      - "Side-by-side training curves for both environments, same color scheme。Pattern identical：step-independent flat/collapsed, episode-level steadily improves。"
    analysis: "Cross-environment validation是reviewer必问问题。6.75x improvement在不同environment confirms the phenomenon is fundamental(credit assignment decay)而非environment-specific artifact。Absolute success差异(48.2 vs 32.4)expected because ScienceWorld inherently harder for 1.7B model，但relative advantage preserved。"

  - name: "7B model scaling verification"
    plan_id: "plan_015"
    description: "Episode-level vs step-independent on Qwen3-7B"
    expected_results:
      episode_level_7B_success: 58.7
      step_independent_7B_success: 8.3
      episode_level_1.7B_success: 48.2
      step_independent_1.7B_success: 6.0
      improvement_factor_7B: 7.07
      improvement_factor_1.7B: 8.03
      convergence_step_7B: 8
      convergence_step_1.7B: 12
    result_rationale: "7B model有更强的base capability（更好的instruction following、更大context capacity），所以absolute success更高(58.7% vs 48.2%)。Step-independent在7B上略好(8.3% vs 6.0%)因为larger model能partially compensate credit assignment problem through better in-context learning，但仍然catastrophically low。Improvement ratio略低(7.07x vs 8.03x)因为larger model的stronger base means step-independent不完全collapse to 0，但差异minor。Convergence更快(8 vs 12 steps)因为7B的stronger initialization means fewer RL steps needed to learn task policy。Key finding：episode-level advantage不因model scale减弱——it's a fundamental training methodology issue not a capacity issue。这addresses Reviewer Concern #3。"
    tables:
      - title: "Model Scale Comparison"
        columns: ["model", "episode_level_%", "step_independent_%", "ratio", "convergence_step"]
        rows:
          - ["Qwen3-1.7B", 48.2, 6.0, "8.0x", 12]
          - ["Qwen3-7B", 58.7, 8.3, "7.1x", 8]
    figures_description:
      - "Grouped bar chart: 2 models × 2 methods, showing episode-level advantage preserved at scale。"
    analysis: "7B result serves dual purpose：(1)confirms advantage generalizes across scale, (2)shows larger models benefit MORE in absolute terms from episode-level(+10.5pp for 7B vs +42.2pp for both，but both huge). If anything，7B result makes episode-level MORE important because it unlocks significantly higher absolute performance。"

  - name: "Per-task-type breakdown analysis"
    plan_id: "plan_016"
    description: "Success breakdown by ALFWorld task type with episode-length correlation"
    expected_results:
      pick_success: 56.2
      pick_mean_length: 22.4
      clean_success: 48.7
      clean_mean_length: 35.6
      heat_success: 52.1
      heat_mean_length: 31.2
      cool_success: 45.3
      cool_mean_length: 33.8
      examine_success: 62.5
      examine_mean_length: 18.7
      pick_two_success: 28.4
      pick_two_mean_length: 48.3
      episode_length_success_correlation: -0.72
      episode_level_advantage_vs_length_correlation: 0.61
    result_rationale: "Task difficulty与episode length高度相关(r=-0.72)。Examine最简单(62.5%)因为只需navigate+look——最短episodes(18.7步)。Pick_two最难(28.4%)因为需要两次independent object interactions——最长episodes(48.3步)。Episode-level advantage与task length正相关(r=0.61)：longer tasks受credit assignment问题影响更大，所以从episode-level training获益更多。Pick_two的episode-level improvement最dramatic(从~3% step-independent到28.4% episode-level，~9x)而examine improvement较modest(从~10%到62.5%，~6x)。这provides additional mechanistic evidence：episode-level training的benefit直接comes from solving longer-horizon credit assignment。"
    tables:
      - title: "Per-Task Performance"
        columns: ["task_type", "success_%", "mean_episode_length", "episode_level_advantage_vs_step_indep"]
        rows:
          - ["examine", 62.5, 18.7, "5.2x"]
          - ["pick", 56.2, 22.4, "6.8x"]
          - ["heat", 52.1, 31.2, "7.9x"]
          - ["clean", 48.7, 35.6, "8.3x"]
          - ["cool", 45.3, 33.8, "8.1x"]
          - ["pick_two", 28.4, 48.3, "9.5x"]
    figures_description:
      - "Scatter plot: mean episode length (X) vs episode-level advantage ratio (Y), with task type labels。Clear positive trend。"
      - "Stacked bar by task type: episode-level vs step-independent, sorted by episode length。"
    analysis: "Per-task breakdown展示within-environment diversity并provide mechanistic validation：如果credit assignment decay是root cause，那longer tasks应该show greater episode-level advantage。r=0.61确认这个prediction。这也informs selective verification design：pick_two任务应receive more frequent verification because they're hardest and longest。"
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5c244f1-2667-469b-b6ba-92d0822df557",
  "isSidechain": false,
  "requestId": "req_011Cb79c8tSMzb6BKuWAhcXr",
  "type": "assistant",
  "uuid": "57a454c6-3bc8-45c0-8e8a-6fa5f67d792f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1",
  "sessionId": "7d0c9cfc-de14-42ca-b418-e3245ab52f6d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VeTxxikNSz1UDxCqK7URMZ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16856,
      "cache_read_input_tokens": 11841,
      "output_tokens": 12758,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16856,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 12758,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 16856,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16856
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Episode-level训练收敛至≥45%，selective verification完整验证，dual contribution成立 核心假设：['Episode-level GRPO在continued training中突破40%阈值并稳定收敛', 'h-sweep展示清晰的单调退化+sharp c…",
  "leafUuid": "57a454c6-3bc8-45c0-8e8a-6fa5f67d792f",
  "sessionId": "7d0c9cfc-de14-42ca-b418-e3245ab52f6d"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Phase A+ episode-level GRPO convergence and ablations",
  "sessionId": "7d0c9cfc-de14-42ca-b418-e3245ab52f6d"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Episode-level训练收敛至≥45%，selective verification完整验证，dual contribution成立 核心假设：['Episode-level GRPO在continued training中突破40%阈值并稳定收敛', 'h-sweep展示清晰的单调退化+sharp c…",
  "leafUuid": "57a454c6-3bc8-45c0-8e8a-6fa5f67d792f",
  "sessionId": "7d0c9cfc-de14-42ca-b418-e3245ab52f6d"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Phase A+ episode-level GRPO convergence and ablations",
  "sessionId": "7d0c9cfc-de14-42ca-b418-e3245ab52f6d"
}
```

---
