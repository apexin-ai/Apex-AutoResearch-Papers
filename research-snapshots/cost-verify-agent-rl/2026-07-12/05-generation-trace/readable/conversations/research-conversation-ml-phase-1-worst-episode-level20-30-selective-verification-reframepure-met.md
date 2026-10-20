# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：Episode-level收敛停滞在20-30%，selective verification无法有意义地执行，需完全reframe为pure met

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/d5bcf265-d8f9-4ed6-8d80-4426d3780ff6.jsonl`
- **Structured JSON:** [`f783ba9e8030b508bfcd.json`](../../sessions/f7/f783ba9e8030b508bfcd.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-17T00:02:38.205Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-17T00:02:38.205Z",
  "sessionId": "d5bcf265-d8f9-4ed6-8d80-4426d3780ff6",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：Episode-level收敛停滞在20-30%，selective verification无法有意义地执行，需完全reframe为pure methodology paper\n核心假设：['Episode-level训练plateau在20-30%（高于baseline但远不够支撑cost story）', 'Success rate不足以让selective verification有统计意义上的对比空间', 'h-sweep仍能展示episode-level vs step-independent的gap，但绝对性能不impressive', 'Multi-seed variance较大（std>8pp），削弱统计credibility', '1.7B model可能是性能瓶颈而非方法问题（reviewer会attack）']\n关键指标范围：{'episode_level_success_rate': [20, 30], 'step_independent_baseline': [0, 6], 'h_sweep_cliff_threshold': [2, 6], 'selective_verification_rate_reduction': [0, 15], 'selective_vs_always_on_success_delta_pp': [8, 15], 'action_change_confirmatory_rate_pct': [50, 70], 'multi_seed_std_pp': [8, 12], 'action_is_valid': [80, 90]}\n叙事方向：完全放弃selective verification contribution，执行Contingency Plan A：pure training methodology paper 'Episode-Level RL for Multi-Turn Agents: Why Step-Independent Fails and How to Fix It'。Core argument转为：(1)揭示现有LLM-agent RL工作（RAGEN等）的隐性failure mode，(2)提供mechanistic explanation（gamma^(T-h) decay），(3)提出fix并在multiple h values上验证。需要大量invest在：h-sweep做极细粒度（h=1,2,3,5,8,10,15,20,full）、mechanism visualization（Figure 2成为paper核心）、与RAGEN/existing work的explicit对比展示他们默认step-independent。可能需要ScienceWorld第二环境来弥补single-env weakness。不降venue——methodology insight本身sufficiently novel for top venue，但需要更深的analysis depth。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: cost-verify-agent-rl\nfocus: Evaluate dual contribution (episode-level training methodology + selective verification). Key uncertainty: will episode-level training converge high enough (≥40%) to support cost-efficiency story? Is the episode-level insight novel enough standalone?\n\n## paper_framing.md\n\n# Paper Framing — Learning When to Verify: RL-Trained Selective Self-Verification for Interactive Agents\n\n> Post-MVP 重写 (2026-05-16) | 基于 D053 MVP 通过 + Reviewer 建议\n\n## Core Insight\n\nMulti-turn interactive agents 的 self-verification 大部分是 confirmatory（不改变行为）而非 corrective。但要训练 agent 学会 selective verification，首先需要解决一个被忽视的训练方法论问题：**step-independent RL 在长 horizon 任务中因 credit assignment decay (gamma^(T-h) → 0) 而灾难性崩溃**。Episode-level training 是前提条件。在此基础上，action-change 作为 intrinsic reward signal 训练 selective verification policy。\n\n## Story Arc\n\n**Dual contribution**: Training methodology + Selective verification system\n\n叙事线：\n1. Self-verification 对 interactive agents 有用，但 always-on 成本高\n2. 训练 agent 学 WHEN to verify 是自然方向 → 但现有 step-independent RL 框架在多轮任务上失败\n3. 我们发现根因是 credit assignment decay，提出 episode-level GRPO 解决\n4. 在此基础上，用 action-change 作为 verification informativeness 的 reward，训练 selective policy\n5. 结果：near-always-on performance + 显著降低 verification cost\n\n## Target Venue\n\n待定（NeurIPS 2026 / EMNLP 2026 / ICLR 2026），取决于实验进度和最终效果。\n\n## Core Claims\n\n### Claim 1 (strength: strong): Episode-level credit assignment is critical for RL training of multi-turn agents\n- 所需证据：episode-level vs step-independent 对比，不同 h 值的 ablation，mechanistic 分析\n- 当前证据状态：**ESTABLISHED** (exp029 step5 val=25% vs exp028c step10 val=0%)\n- 强度依据：2x baseline vs catastrophic collapse，机制清晰（gamma^49=7.7%）\n\n### Claim 2 (strength: moderate): Action-change is an effective intrinsic reward for verification informativeness\n- 所需证据：selective verification 训练收敛 + action-change vs random/confidence baselines\n- 当前证据状态：**not yet established**，依赖 Phase B 实验\n- 前提：episode-level 训练的 agent 需达到 ≥40% success 才有意义\n\n### Claim 3 (strength: moderate): Learned selective policy matches always-on performance at reduced verification cost\n- 所需证据：B-IAVR verification ↓40%+ 且 success delta < 3pp vs always-on\n- 当前证据状态：**not yet established**，依赖 Phase B + C\n- 前提：Claim 1 的 agent 需足够强\n\n## Contingency Plan\n\n如果 episode-level 训练收敛后 success 仍 < 40%（不足以支撑 cost-efficiency story）：\n- **Plan A**（首选）：paper 变为 pure training methodology contribution — \"Episode-Level RL for Multi-Turn Agents: Why Step-Independent Fails and How to Fix It\"\n- **Plan B**：加更多 ablation 深挖 episode-level training（context window size sweep, reward shaping, curriculum），做 analysis paper\n- 不考虑 downgrade venue\n\n## Reviewer Attack Surface + Defense\n\n| # | Concern | Severity | Defense Experiment |\n|---|---------|----------|--------------------|\n| 1 | \"Episode-level RL is obvious / well-known\" | HIGH | Context window ablation (h=2,5,10,20,full) 展示 non-trivial threshold + 机制分析 + 展示现有 LLM-agent 工作(RAGEN等)默认 step-independent |\n| 2 | Single environment (ALFWorld) | MEDIUM | 加 ScienceWorld / WebShop (if resources permit) |\n| 3 | Small model (1.7B) | MEDIUM | 定位 resource-constrained; 加 7B 验证 (if GPU available) |\n| 4 | Action-change = noise vs signal | MEDIUM | Entropy-controlled analysis + causal intervention (Phase B) |\n| 5 | Selective verification 效果不够 significant | MEDIUM | 多 baseline 对比 (always-on / no-verify / random-p / confidence-threshold / ARES) |\n| 6 | 与 ARES 差异化不足 | LOW | 实验直接对比 + 方法论差异表 (SFT router vs RL policy, continuous vs binary) |\n\n## Evidence Status Matrix\n\n| Claim | MVP Evidence | Research Evidence Needed | Priority |\n|-------|-------------|--------------------------|----------|\n| Claim 1 | exp029 vs exp028c (25% vs 0%) | h-value ablation, multi-seed, mechanism paper figure | P0 |\n| Claim 2 | N/A | Phase B full implementation | P1 |\n| Claim 3 | N/A | Phase B + C comparison suite | P1 |\n\n## Competitive Positioning\n\n| System | Method | ALFWorld | Key Difference |\n|--------|--------|----------|---------------|\n| Self-Guide (2026) | Always-on verification | 72.7% (1.7B) | We add selectivity via RL |\n| ARES (2603.07915) | SFT router, continuous effort | 52.7% token↓ | SFT vs RL, continuous vs binary |\n| Thinkless (NeurIPS'25) | RL control token | reasoning | Same RL philosophy, different domain |\n| ReflAct (EMNLP'25) | Prompting GPT-4 | 93.3% | Different scale/approach |\n| RAGEN (2025) | GRPO for agents | varies | Step-independent default — our baseline |\n\n## Research Phases\n\n1. **Phase A (DONE)**: Episode-level GRPO training — MVP passed, demonstrates Claim 1\n2. **Phase A+**: Continue training to convergence (target ≥40% success), deploy tatsu parallel patch, multi-seed\n3. **Phase B**: Implement selective verification with action-change reward — Claim 2 & 3\n4. **Phase C**: Ablation suite — context window sweep, reward ablations, baseline comparisons\n5. **Phase D**: (Conditional on resources) Multi-env / multi-model scaling\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  title: Episode-level GRPO convergence (exp029 continuation)\n  claim: Claim 1\n  phase: A+\n  priority: P0\n  depends_on: []\n  registry_id: exp029_episode_level\n  status: DONE\n  description: 'Episode-level GRPO (context_window_mode: full) on Qwen3-1.7B + ALFWorld.\n    50 steps, dual-GPU. MVP passed at step 5 (val=25%, 2x baseline 12.5%). Continue\n    to convergence (step 20+) with tatsu parallel patch for 4x val speedup.\n\n    '\n  hypothesis: 'Episode-level training enables stable RL for multi-turn agents, reaching\n    ≥40% success by convergence.\n\n    '\n  metrics:\n  - success_rate\n  - action_is_valid\n  - kl_divergence\n  - entropy\n  gpu_hours_estimate: 48\n  framing_ref: claim_1\n  conclusion: failed\n- id: plan_002\n  title: Context window h-sweep ablation\n  claim: Claim 1\n  phase: A+\n  priority: P0\n  depends_on:\n  - plan_001\n  registry_id: null\n  status: planned\n  description: 'Sweep context_window h={2, 5, 10, 20, full} on same GRPO config. KEY\n    paper figure: shows credit assignment threshold is not binary (h=2 catastrophic,\n    intermediate h partial, full best). Mechanistic analysis: plot effective discount\n    gamma^(T-h) vs performance. Addresses Reviewer Concern #1 (\"episode-level is obvious\").\n\n    '\n  hypothesis: 'Performance degrades monotonically with smaller h, with sharp cliff\n    below h=10 where gamma^(T-h) < 0.01 for most episodes.\n\n    '\n  metrics:\n  - success_rate_per_h\n  - convergence_speed\n  - collapse_rate\n  gpu_hours_estimate: 120\n- id: plan_003\n  title: Multi-seed replication (3 seeds)\n  claim: Claim 1\n  phase: A+\n  priority: P0\n  depends_on:\n  - plan_001\n  registry_id: null\n  status: planned\n  description: '2 additional seeds for exp029 episode-level config. Report mean ±\n    std. Critical for statistical credibility of all downstream comparisons.\n\n    '\n  hypothesis: 'Episode-level success rate is reproducible (std < 5pp across seeds).\n\n    '\n  metrics:\n  - success_rate_mean\n  - success_rate_std\n  gpu_hours_estimate: 96\n- id: plan_004\n  title: Credit assignment mechanism analysis (paper Figure 2)\n  claim: Claim 1\n  phase: A+\n  priority: P0\n  depends_on:\n  - plan_002\n  registry_id: null\n  status: planned\n  description: 'Compute and visualize: (a) effective discount gamma^(T-h) for each\n    h value, (b) gradient signal strength per training step under different h, (c)\n    correlation between episode length and performance drop under small h. Mostly\n    analysis/plotting, minimal GPU.\n\n    '\n  hypothesis: 'Shorter contexts produce exponentially weaker gradient signal, explaining\n    the catastrophic collapse pattern.\n\n    '\n  metrics:\n  - gradient_signal_strength\n  - discount_factor_curve\n  gpu_hours_estimate: 4\n- id: plan_005\n  title: Action-change statistics from always-on runs\n  claim: Claim 2\n  phase: B\n  priority: P1\n  depends_on:\n  - plan_001\n  registry_id: null\n  status: planned\n  description: 'Collect action-change statistics from exp029 trained checkpoints:\n    (1) fraction of verifications triggering action change, (2) correlation between\n    action change and episode success, (3) per-task-type breakdown. Informs reward\n    design and provides empirical grounding.\n\n    '\n  hypothesis: 'Most verifications are confirmatory (>60% no action change). Action\n    change positively correlates with episode success (r > 0.2).\n\n    '\n  metrics:\n  - action_change_rate\n  - correlation\n  - confirmatory_rate\n  gpu_hours_estimate: 4\n- id: plan_006\n  title: Selective verification implementation\n  claim: Claim 2\n  phase: B\n  priority: P1\n  depends_on:\n  - plan_005\n  registry_id: null\n  status: planned\n  description: 'Implement binary verify/skip decision in RAGEN framework. Agent outputs\n    special token (verify/skip) before each step. Reward = task_success + alpha *\n    action_change_when_verified - beta * verification_cost. Code-only, no GPU.\n\n    '\n  hypothesis: null\n  metrics: []\n  gpu_hours_estimate: 0\n- id: plan_007\n  title: B-IAVR selective verification training\n  claim: Claim 2, Claim 3\n  phase: B\n  priority: P1\n  depends_on:\n  - plan_006\n  - plan_001\n  registry_id: null\n  status: planned\n  description: 'Train selective verification policy via episode-level GRPO. Initialize\n    from best exp029 checkpoint. Action-change reward encourages verification only\n    when informative.\n\n    '\n  hypothesis: 'B-IAVR achieves verification rate ↓40%+ vs always-on while maintaining\n    success within 5pp of baseline.\n\n    '\n  metrics:\n  - success_rate\n  - verification_rate\n  - cost_reduction\n  gpu_hours_estimate: 96\n- id: plan_008\n  title: Selective verification full comparison\n  claim: Claim 3\n  phase: B\n  priority: P1\n  depends_on:\n  - plan_007\n  registry_id: null\n  status: planned\n  description: 'Compare on same val set: always-on / B-IAVR / no-verify / random-p\n    / confidence-threshold. Report success rate, verification rate, total inference\n    tokens, per-task breakdown.\n\n    '\n  hypothesis: 'B-IAVR dominates Pareto frontier (best success-to-cost ratio).\n\n    '\n  metrics:\n  - success_rate\n  - verification_rate\n  - cost_reduction\n  - total_tokens\n  gpu_hours_estimate: 8\n- id: plan_009\n  title: No-verify ablation\n  claim: Claim 3\n  phase: C\n  priority: P1\n  depends_on:\n  - plan_001\n  registry_id: null\n  status: planned\n  description: 'Episode-level GRPO without any self-verification. Lower bound: demonstrates\n    verification value.\n\n    '\n  hypothesis: 'Removing verification drops success by ≥10pp vs always-on.\n\n    '\n  metrics:\n  - success_rate\n  - action_is_valid\n  gpu_hours_estimate: 48\n- id: plan_010\n  title: Entropy-controlled action-change analysis\n  claim: Claim 2\n  phase: C\n  priority: P1\n  depends_on:\n  - plan_005\n  registry_id: null\n  status: planned\n  description: 'Defense for \"action change = noise\" concern. Stratify by policy entropy;\n    test if action-change-success correlation holds within each stratum.\n\n    '\n  hypothesis: 'Partial correlation remains significant (p < 0.05) after controlling\n    entropy.\n\n    '\n  metrics:\n  - partial_correlation\n  - p_value\n  gpu_hours_estimate: 4\n- id: plan_011\n  title: 'Causal intervention: random vs verification-triggered changes'\n  claim: Claim 2\n  phase: C\n  priority: P1\n  depends_on:\n  - plan_001\n  registry_id: null\n  status: planned\n  description: 'Inject random action changes at same rate as verification-triggered.\n    Compare task success. If verification-triggered >> random, causal evidence.\n\n    '\n  hypothesis: 'Verification-triggered changes yield ≥10pp higher success than random.\n\n    '\n  metrics:\n  - success_rate_triggered\n  - success_rate_random\n  - delta\n  gpu_hours_estimate: 8\n- id: plan_012\n  title: Reward signal ablation (action-change vs alternatives)\n  claim: Claim 2\n  phase: C\n  priority: P1\n  depends_on:\n  - plan_007\n  registry_id: null\n  status: planned\n  description: 'Train B-IAVR with alternative rewards: (a) action-change (ours), (b)\n    random trigger reward, (c) confidence-based reward. Demonstrates action-change\n    is the best signal.\n\n    '\n  hypothesis: 'Action-change reward produces best cost-performance tradeoff.\n\n    '\n  metrics:\n  - success_rate\n  - verification_rate\n  - cost_reduction\n  gpu_hours_estimate: 192\n- id: plan_013\n  title: ARES reproduction + comparison\n  claim: Claim 3\n  phase: C\n  priority: P1\n  depends_on:\n  - plan_007\n  registry_id: null\n  status: planned\n  description: 'Reproduce ARES SFT router on ALFWorld (same model). Head-to-head with\n    B-IAVR on identical eval episodes. Addresses \"ARES differentiation\" concern.\n\n    '\n  hypothesis: 'B-IAVR achieves ≥10pp better cost reduction than ARES at matched success.\n\n    '\n  metrics:\n  - success_rate\n  - verification_rate\n  - cost_reduction\n  gpu_hours_estimate: 24\n- id: plan_014\n  title: ScienceWorld transfer (episode-level advantage)\n  claim: Claim 1\n  phase: D\n  priority: P2\n  depends_on:\n  - plan_001\n  registry_id: null\n  status: planned\n  description: 'Validate episode-level vs step-independent on ScienceWorld. Different\n    env, similar multi-turn structure. Addresses single-env concern.\n\n    '\n  hypothesis: 'Episode-level advantage generalizes: ≥2x improvement over step-independent.\n\n    '\n  metrics:\n  - success_rate_episode\n  - success_rate_step_independent\n  gpu_hours_estimate: 72\n- id: plan_015\n  title: 7B model scaling verification\n  claim: Claim 1\n  phase: D\n  priority: P2\n  depends_on:\n  - plan_002\n  registry_id: null\n  status: planned\n  description: 'Episode-level vs step-independent on Qwen3-7B. Addresses model size\n    concern. May need cloud GPU.\n\n    '\n  hypothesis: 'Episode-level advantage holds at 7B scale.\n\n    '\n  metrics:\n  - success_rate_episode_7B\n  - success_rate_step_independent_7B\n  gpu_hours_estimate: 192\n  notes: May require cloud GPU rental (4x A100 or 2x H100)\n- id: plan_016\n  title: Per-task-type breakdown analysis\n  claim: Claim 1\n  phase: D\n  priority: P2\n  depends_on:\n  - plan_001\n  registry_id: null\n  status: planned\n  description: 'Breakdown by ALFWorld task type (pick, clean, heat, cool, examine,\n    pick_two). Shows within-environment diversity.\n\n    '\n  hypothesis: 'Episode-level advantage varies by task complexity; longer tasks benefit\n    more.\n\n    '\n  metrics:\n  - per_task_success\n  - episode_length_correlation\n  gpu_hours_estimate: 2\n\n\n## registry (completed experiments)\n\n- exp_id: exp_001\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001b\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_002\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_003\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_003_dryrun\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_003_dryrun2\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp003_dryrun3\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_003_dryrun3\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp003\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp005\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp007\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    steps_completed: 10\n    steps_planned: 30\n    crash_reason: 'OSError: No space left on device (/tmp)'\n    final_success_rate: 0.0625\n    final_action_is_valid: 0.0835\n    final_manager_invalid_action: 0.0156\n    final_pass_at_8: 0.375\n    final_pg_loss: 0.00117\n    final_ppo_kl: 0.00127\n    final_entropy: 0.057\n    final_score_mean: 0.578\n    dryrun_action_is_valid: 0.054\n    dryrun_invalid_action: 0.065\n    training_time_s: 6739\n- exp_id: exp007_dryrun\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp008\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp008_sft\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    action_is_valid: 0.9\n    format_ok: 1\n    success_rate: 0\n    final_loss: 0.069\n    final_token_accuracy: 0.973\n    data_count: 1200\n    epochs: 3\n    total_steps: 225\n    training_time_s: 576\n- exp_id: exp009\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp010\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    step: 11\n    total_steps: 30\n    crash_reason: /tmp disk full (fast_downward libdownward.so)\n    initial_val_action_is_valid: 0.652\n    initial_val_success: 0\n    step1_success: 0.047\n    step1_pass_at_8: 0.375\n    step1_action_is_valid: 0.588\n    step10_success: 0\n    step10_pass_at_8: 0\n    step10_action_is_valid: 0.683\n    step5_ppo_kl: 0.00158\n    step5_entropy: 0.1\n    trend: action_is_valid improving (58.8%→68.3%) but success collapsing (4.7%→0%)\n    checkpoint_saved: global_step_10\n- exp_id: exp011\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp012\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp012b\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    step: 8\n    total_steps: 30\n    step6_success: 0.0859\n    step6_action_is_valid: 0.613\n    step6_pass_at_16: 0.5\n    step6_ppo_kl: 0.0039\n    step6_entropy: 0.1006\n    step6_grad_norm: 1.477\n    step7_success: 0\n    step7_action_is_valid: 0.685\n    step7_pass_at_16: 0\n    step7_pg_loss: 0\n    step7_ppo_kl: 0.00439\n    step7_entropy: 0.0904\n    step7_grad_norm: 0.094\n    trend: success 8.6%→0% collapse at step 7 (same pattern as exp010, delayed 1 step).\n      grad_norm 1.477→0.094, pg_loss→0. Reward fix delayed but did not prevent collapse.\n- exp_id: exp013\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp013b\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp013c\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp013d\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp013e\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp013f\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    step: 30\n    total_steps: 30\n    completed: true\n    exit_code: 0\n    training_time_s: 10683\n    step6_success: 0.0156\n    step7_success: 0.0781\n    step10_success: 0\n    step17_success: 0.0156\n    final_val_success: 0\n    final_val_action_is_valid: 0.975\n    final_val_action_is_effective: 1\n    final_val_reward_mean_at4: 4.388\n    final_val_reward_std_at4: 0.195\n    final_val_reward_best_at4: 4.499\n    final_val_pass_at1: 0\n    action_is_valid_trend: 60%→65.9%→77.1%→97.5%\n    success_trend: 0%→1.56%→7.81%→0%→1.56%→0%\n    grad_norm_range: 1.7-2.9 (no collapse)\n    conclusion_reason: 'Dense reward gaming: model optimized valid_action_bonus (action_is_valid\n      60%→97.5%) but success stayed 0%. Reward ratio 1:67 too weak — cumulative valid_action_bonus\n      (4.5) dominated learning signal vs sparse success_reward (10.0). GRPO collapse\n      prevented but task completion not learned.'\n- exp_id: exp014c\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp014a\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp014b\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp015\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    step: 1\n    total_steps: 30\n    val_step0_success: 0\n    val_step0_action_is_valid: 0.858\n    val_step0_pass_at1: 0\n    val_step0_episodic_return: 0\n    val_step0_response_length: 2797.5\n    val_train_transition: passed\n    estimated_total_time_min: 163\n    time_per_step_min: 5.6\n- exp_id: exp016\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    step: 12\n    total_steps: 30\n    elapsed_min: 51\n    step6_success: 0\n    step6_action_is_valid: 0.521\n    step6_pg_loss: 0\n    step6_grad_norm: 0.841\n    step7_success: 0.047\n    step7_pass_at16: 0.5\n    step7_action_is_valid: 0.655\n    step10_success: 0\n    step10_action_is_valid: 0.664\n    step10_pg_loss: 0\n    step10_grad_norm: 0.856\n    step10_entropy: 0.1046\n    step10_ppo_kl: -9.1e-05\n    all_raw_rewards: 0\n    all_advantages: 0\n    all_returns: 0\n    reward_signal: BROKEN — success episodes get reward=0\n    action_is_valid_trend: 52.1%→65.5%→66.4%\n    manager_invalid_action_trend: 13.5%→11.2%→9.6%\n- exp_id: exp017_expert_sft\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_train_loss: 0.1434\n    final_step_loss: 0.04\n    final_token_accuracy: 0.983\n    epochs: 3\n    total_steps: 462\n    training_time_min: 26\n    data_count_train: 2460\n    data_count_val: 129\n    checkpoint_size_gb: 3.44\n    eval_success_rate: 0.05\n    eval_success: 1/20\n    eval_action_is_valid: 0.638\n    eval_format_ok: 0.75\n    eval_avg_steps: 22\n    eval_time_s: 149.6\n    eval_per_task:\n      put: 0/10\n      clean: 0/4\n      cool: 1/3\n      heat: 0/2\n      examine: 0/1\n    eval_parse_failures: 5/20 episodes (EP 7/12/16/17/18)\n- exp_id: exp018_sft_grpo\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp019_expert_sft_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp019b_expert_sft_v2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp019b_expert_sft_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.0718\n    eval_loss: 0.0428\n    eval_mean_token_accuracy: 0.9869\n    train_runtime_seconds: 2869.8\n    steps: 320\n    epochs: 2\n    eval_success_rate: 0.2\n    eval_format_ok: 1\n    eval_action_is_valid: 0.8533\n    eval_episodes: 20\n    eval_avg_steps: 25.4\n    eval_time_seconds: 146\n- exp_id: exp019c_expert_sft_v3\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp020_grpo_from_sft\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp020b_grpo_from_sft\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    steps_completed: 22\n    steps_planned: 30\n    hung_at_step: 23\n    step1_train_success: 0.1875\n    step10_train_success: 0.1875\n    step20_train_success: 0.125\n    step22_train_success: 0.0469\n    val_success_step0: 0\n    val_success_step20: 0\n    entropy_initial: 0.107\n    entropy_final: 0.042\n    grad_norm_initial: 2.78\n    grad_norm_step20: 5.58\n    ppo_kl_final: 0.00918\n    pass_at_16_step1: 0.75\n    pass_at_16_step22: 0.25\n    checkpoint_latest: global_step_20\n    training_status: hung_at_step23_rollout\n- exp_id: exp020c_grpo_from_sft\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp020d_grpo_from_sft\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp021_sft_ragen_format\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp021_ragen_sft_v4\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    train_loss_final: 0.038\n    train_token_accuracy: 0.988\n    train_steps: 320\n    train_epochs: 2\n    train_time_min: 47.8\n    ragen_val_success: 0.25\n    ragen_val_action_is_valid: 0.875\n    eval_sft_fast_success: 0\n    eval_sft_fast_format_ok: 1\n    eval_sft_fast_action_is_valid: 0.71\n    checkpoint_size_gb: 3.3\n    ragen_val_success_16ep: 0.0625\n    ragen_val_action_is_valid_16ep: 0.6875\n- exp_id: exp022_grpo_from_sft_v4\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    steps_completed: 1\n    steps_planned: 30\n    val_step0_success: 0.125\n    val_step0_action_is_valid: 0.4875\n    val_step0_action_is_effective: 1\n    val_step0_reward_mean: 1.25\n    val_step0_reward_best: 6.61\n    val_step0_episodes: 8\n    step_time_seconds: 208\n- exp_id: exp023_grpo_parallel\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp023c_grpo_serial\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    val_step0_success: 0.0625\n    val_step0_action_is_valid: 0.6875\n    val_step0_episodes: 16\n    train_step1_success: 0.297\n    train_step1_action_is_valid: 0.791\n    train_step1_entropy: 0.0652\n    train_step1_pass16: 0.75\n    train_step1_kl: 0.000156\n    train_step8_success: 0.234\n    train_step8_action_is_valid: 0.779\n    train_step8_entropy: 0.0555\n    train_step8_pass16: 0.5\n    train_step8_kl: 0.000475\n    steps_completed: 8\n    steps_planned: 30\n    step_time_seconds_start: 240\n    step_time_seconds_end: 365\n- exp_id: exp024_success_gated_grpo\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp025\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp025b\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp025c\n  name: ''\n  status: PENDING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp026_step_independent_grpo\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    val_before_train_success: 0.0625\n    val_before_train_action_is_valid: 0.631\n    val_before_train_episodes: 16\n    train_step1_success: 0.2188\n    train_step1_action_is_valid: 0.686\n    train_step1_entropy: 0.2672\n    train_step1_kl_loss: 0.1797\n    train_step1_grad_norm: 14.43\n    train_step1_reward_mean: 1.218\n    train_step1_pass_at_16: 1\n    train_step2_success: 0.3281\n    train_step2_action_is_valid: 0.603\n    train_step2_entropy: 0.317\n    train_step2_kl_loss: 0.0974\n    train_step2_grad_norm: 15.62\n    train_step2_reward_mean: 1.62\n    train_step2_pass_at_16: 1\n    train_step3_success: 0.1719\n    train_step3_action_is_valid: 0.641\n    train_step3_entropy: 0.387\n    train_step3_kl_loss: 0.2617\n    train_step3_grad_norm: 15.65\n    train_step3_reward_mean: 1.079\n    train_step3_pass_at_16: 0.75\n    train_step4_success: 0\n    train_step4_action_is_valid: 0.717\n    train_step4_entropy: 0.387\n    train_step4_kl_loss: 0.054\n    train_step4_grad_norm: 13.81\n    train_step4_pass_at_16: 0\n- exp_id: exp027_stable_grpo\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    step_0_val_before_train:\n      success: 6.25\n      action_is_valid: 63.125\n      action_is_effective: 87.875\n      num_actions: 42.375\n      response_length: 114.67\n      reward_mean: 0.3226\n      val_generation_time_s: 502.57\n    step_1_train:\n      success: 35.94\n      kl_loss: 0.058\n      batch_size: 5152\n      training_time_s: 4342\n    step_2_train:\n      success: 10.16\n      kl_loss: 0.413\n      batch_size: 6144\n      training_time_s: 5886\n    step_3_train:\n      success: 10.16\n      kl_loss: 0.248\n      entropy: 0.385\n      pass_at_16: 0.5\n      grad_norm: 21.31\n      reward_mean: 0.483\n      batch_size: 6048\n      training_time_s: 4689\n    step_4_train:\n      success: 13.28\n      pass_at_16: 0.375\n      note: 'Director判定: 趋势确认, MVP未通过'\n- exp_id: exp028_prereq_zeroshot_instruct\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp028a_recipe_fix\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp028_prereq_zeroshot\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    success: 0\n    action_is_valid: 0.75\n    num_actions: 50\n    pass_at_1: 0\n    response_length: 75.07\n- exp_id: exp028c_selfguide_recipe\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    step_0_val:\n      success: 6.25\n      pass_at_1: 6.25\n      action_is_valid: 74.5\n      score_mean: 0.119\n    step_1_train:\n      success: 13.28\n      pass_at_8: 37.5\n      action_is_valid: 76.4\n      action_is_effective: 96.37\n      entropy: 0.2634\n      kl_loss: 0.0128\n      ppo_kl: 0.019\n      grad_norm: 16.88\n      score_mean: 0.843\n      time_s: 3252\n      note: 三方交叉验证通过\n    step_2_train:\n      success: 6.25\n      pass_at_8: 25\n      action_is_valid: 83.2\n      entropy: 0.247\n      kl_loss: 0.1706\n      pg_loss: 0.007\n      grad_norm: 17.3\n      score_mean: 0.274\n      time_s: 3120\n    step_3_train:\n      success: 15.63\n      pass_at_8: 68.75\n      action_is_valid: 85.9\n      entropy: 0.2488\n      kl_loss: 0.1118\n      grad_norm: 12.57\n      score_mean: 0.661\n      time_s: 2760\n    step_4_train:\n      success: 18.75\n      pass_at_8: 62.5\n      action_is_valid: 87.94\n      entropy: 0.234\n      kl_loss: 0.031\n      ppo_kl: 0.015\n    step_5_train:\n      success: 9.4\n      pass_at_8: 37.5\n      action_is_valid: 89.6\n      entropy: 0.236\n      kl_loss: 0.824\n      grad_norm: 13.1\n    step_5_val:\n      success: 6.25\n      pass_at_1: 6.25\n      action_is_valid: 96.5\n      action_is_effective: 100\n      num_actions: 49.4\n      score_mean: 0.518\n    step_6_train:\n      success: 10.94\n      action_is_valid: 90.4\n      entropy: 0.234\n      kl_loss: 0.098\n      grad_norm: 12.54\n    step_7_train:\n      success: 21.88\n      pass_at_8: 56.25\n      action_is_valid: 91.8\n      entropy: 0.224\n      kl_loss: 0.046\n    step_8_train:\n      success: 15.6\n      pass_at_8: 50\n      action_is_valid: 92.7\n      kl_loss: 0.039\n      entropy: 0.204\n    step_9_train:\n      success: 18\n      pass_at_8: 56.3\n      action_is_valid: 93.6\n      kl_loss: 0.047\n      entropy: 0.204\n    step_10_train:\n      success: 18.75\n      action_is_valid: 90.7\n      kl_loss: 0.197\n    step_10_val:\n      success: 0\n      pass_at_1: 0\n      best_at_128: 0\n      best_at_800: 0\n      action_is_valid: 93.6\n      num_actions: 49.8\n      reward_mean: 0\n      note: 灾难性崩溃，模型完全遗忘\n- exp_id: exp029_episode_level\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-17T00:02:38.209Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-17T00:02:38.209Z",
  "sessionId": "d5bcf265-d8f9-4ed6-8d80-4426d3780ff6"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-17T00:02:38.234Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：Episode-level收敛停滞在20-30%，selective verification无法有意义地执行，需完全reframe为pure methodology paper
核心假设：['Episode-level训练plateau在20-30%（高于baseline但远不够支撑cost story）', 'Success rate不足以让selective verification有统计意义上的对比空间', 'h-sweep仍能展示episode-level vs step-independent的gap，但绝对性能不impressive', 'Multi-seed variance较大（std>8pp），削弱统计credibility', '1.7B model可能是性能瓶颈而非方法问题（reviewer会attack）']
关键指标范围：{'episode_level_success_rate': [20, 30], 'step_independent_baseline': [0, 6], 'h_sweep_cliff_threshold': [2, 6], 'selective_verification_rate_reduction': [0, 15], 'selective_vs_always_on_success_delta_pp': [8, 15], 'action_change_confirmatory_rate_pct': [50, 70], 'multi_seed_std_pp': [8, 12], 'action_is_valid': [80, 90]}
叙事方向：完全放弃selective verification contribution，执行Contingency Plan A：pure training methodology paper 'Episode-Level RL for Multi-Turn Agents: Why Step-Independent Fails and How to Fix It'。Core argument转为：(1)揭示现有LLM-agent RL工作（RAGEN等）的隐性failure mode，(2)提供mechanistic explanation（gamma^(T-h) decay），(3)提出fix并在multiple h values上验证。需要大量invest在：h-sweep做极细粒度（h=1,2,3,5,8,10,15,20,full）、mechanism visualization（Figure 2成为paper核心）、与RAGEN/existing work的explicit对比展示他们默认step-independent。可能需要ScienceWorld第二环境来弥补single-env weakness。不降venue——methodology insight本身sufficiently novel for top venue，但需要更深的analysis depth。

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
  "promptId": "2cecbdaf-b0e2-417e-b39f-47fb46de5dc6",
  "type": "user",
  "uuid": "7f660c73-451d-4c34-b496-27fdc827ea8d",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1",
  "sessionId": "d5bcf265-d8f9-4ed6-8d80-4426d3780ff6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-17T00:02:38.232Z_

```json
{
  "parentUuid": "7f660c73-451d-4c34-b496-27fdc827ea8d",
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
  "uuid": "4305f122-1663-4b12-ab40-f3e05a8613b8",
  "timestamp": "2026-05-17T00:02:38.232Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1",
  "sessionId": "d5bcf265-d8f9-4ed6-8d80-4426d3780ff6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-17T00:02:38.233Z_

```json
{
  "parentUuid": "4305f122-1663-4b12-ab40-f3e05a8613b8",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "fdc7270e-072b-49e0-9cf1-72acba8a98c0",
  "timestamp": "2026-05-17T00:02:38.233Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1",
  "sessionId": "d5bcf265-d8f9-4ed6-8d80-4426d3780ff6",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Episode-level收敛停滞在20-30%，selective verification无法有意义地执行，需完全reframe为pure methodology paper 核心假设：['Episode-level训练plateau在20-30%（高于baseline但远不够支撑cost story）…",
  "leafUuid": "fdc7270e-072b-49e0-9cf1-72acba8a98c0",
  "sessionId": "d5bcf265-d8f9-4ed6-8d80-4426d3780ff6"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Episode-level RL failure scenario planning",
  "sessionId": "d5bcf265-d8f9-4ed6-8d80-4426d3780ff6"
}
```

---

### Assistant

_source line 8 · 2026-05-17T00:02:59.208Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted experimental results for every "planned" experiment in the experiment_plan, under the "worst" tier scenario they've defined. Let me carefully go through each planned experiment and predict what would happen in the worst case scenario.

The worst tier is defined as:
- Episode-level success rate: 20-30%
- Step-independent baseline: 0-6%
- h-sweep cliff threshold: h=2-6
- Selective verification rate reduction: 0-15%
- Selective vs always-on success delta: 8-15pp


- Action-change confirmatory rate: 50-70%
- Multi-seed std: 8-12pp
- Action is valid: 80-90%

The narrative direction is shifting toward a pure methodology paper that abandons selective verification entirely, focusing instead on the episode-level versus step-independent performance gap as the central story, with the h-sweep serving as the core figure and mechanistic explanation.

Now I'm working through each planned experiment to predict worst-case outcomes, starting with the h-sweep ablation and multi-seed replication studies, then moving into the credit assignment mechanism analysis and action-change statistics.

Plan 001 already failed—episode-level training plateaued at 20-30% instead of reaching the hoped-for 40%+, so I'm skipping that and continuing with the remaining experiments through the 7B model scaling and per-task-type breakdowns.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fdc7270e-072b-49e0-9cf1-72acba8a98c0",
  "isSidechain": false,
  "requestId": "req_011Cb7AGMPpVcgsh3ZzDqgQJ",
  "type": "assistant",
  "uuid": "d719fa3a-4d91-4575-8608-2e006e982680",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1",
  "sessionId": "d5bcf265-d8f9-4ed6-8d80-4426d3780ff6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xe52oKJYnULfYrvHc76QMj",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 17026,
      "cache_read_input_tokens": 11841,
      "output_tokens": 10156,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17026,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 10156,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 17026,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17026
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

_source line 9 · 2026-05-17T00:06:12.889Z_

```yaml
tier: worst
narrative_guidance: "完全放弃selective verification contribution。转型为pure training methodology paper: 'Episode-Level RL for Multi-Turn Agents: Why Step-Independent Fails and How to Fix It'。核心Figure是h-sweep + mechanism visualization。需要极细粒度h-sweep、多seed统计、与RAGEN的explicit对比来补偿绝对性能不impressive的弱点。Paper story变为：(1)揭示failure mode, (2)mechanistic explanation, (3)提出fix并验证。不降venue但需要更深analysis depth。"

imagined_experiments:
  - name: "Context window h-sweep ablation"
    plan_id: "plan_002"
    description: "Sweep h={1,2,3,5,8,10,15,20,full} on same GRPO config. Paper核心Figure。"
    expected_results:
      h1_success_rate: 0.0
      h2_success_rate: 2.0
      h3_success_rate: 4.5
      h5_success_rate: 8.0
      h8_success_rate: 14.0
      h10_success_rate: 18.0
      h15_success_rate: 22.0
      h20_success_rate: 24.0
      h_full_success_rate: 25.0
      cliff_threshold_h: 5
      h1_collapse_rate: 1.0
      h2_collapse_rate: 0.85
      h5_action_is_valid: 72.0
      h10_action_is_valid: 82.0
      h_full_action_is_valid: 88.0
      convergence_speed_h10_steps: 15
      convergence_speed_h_full_steps: 8
    result_rationale: "在worst档位下，h-sweep仍能展示episode-level vs step-independent的gap，但曲线形态偏向gradual degradation而非sharp cliff。h=5以下gamma^(T-h)衰减到<1%导致几乎无学习信号，但h=10到h=full之间差距不大（18%→25%），削弱了'episode-level is critical'的论证力度——reviewer会argue h=10 already sufficient。绝对性能ceiling在25%使得整条曲线都不impressive。cliff在h=5左右，比hypothesis的h=10低，意味着credit assignment threshold比预期更宽松，但也说明即便给了足够context（h≥10），1.7B model的能力ceiling也只有20-25%。"
    tables:
      - name: "Table 1: h-sweep results"
        columns: ["h", "success_rate(%)", "action_is_valid(%)", "convergence_step", "effective_discount_gamma^(T-h)_mean"]
        rows:
          - [1, 0.0, 45.0, "N/A (collapse)", 0.0001]
          - [2, 2.0, 58.0, "N/A (near-collapse)", 0.0008]
          - [3, 4.5, 65.0, 20, 0.005]
          - [5, 8.0, 72.0, 15, 0.03]
          - [8, 14.0, 79.0, 12, 0.12]
          - [10, 18.0, 82.0, 12, 0.22]
          - [15, 22.0, 85.0, 10, 0.48]
          - [20, 24.0, 87.0, 8, 0.67]
          - ["full", 25.0, 88.0, 8, 1.0]
    figures_description:
      - "Figure 2a: x=h value (log scale), y=success rate. 呈S-curve但slope较gentle。h<5区域flat near zero, h=5-10区域linear rise, h>10区域saturate at ~25%。Error bars from single seed较大。"
      - "Figure 2b: x=effective discount gamma^(T-h), y=success rate. Near-linear relationship，但R²约0.85（非perfect fit）表明discount不是唯一因素。"
    analysis: "h-sweep是worst档下paper最有价值的contribution。虽然绝对性能低，但趋势清晰：step-independent（h=1-2）catastrophically fails，episode-level（h=full）works。问题在于h=10已达full性能的72%（18/25），reviewer会argue full episode context非必要。Defense需要：(1)强调h=10在更长episode task上可能不够，(2)展示h=full的convergence speed优势，(3)argue 'full是最简方案，无需tune h'。Single seed数据使得intermediate h values的ordering可能有noise。"

  - name: "Multi-seed replication (3 seeds)"
    plan_id: "plan_003"
    description: "2 additional seeds for episode-level config. Report mean ± std。"
    expected_results:
      seed1_success_rate: 25.0
      seed2_success_rate: 18.0
      seed3_success_rate: 30.0
      mean_success_rate: 24.3
      std_success_rate: 6.0
      seed1_convergence_step: 8
      seed2_convergence_step: 15
      seed3_convergence_step: 6
      seed1_action_is_valid: 88.0
      seed2_action_is_valid: 82.0
      seed3_action_is_valid: 90.0
      mean_action_is_valid: 86.7
      std_action_is_valid: 4.2
    result_rationale: "Worst档定义multi-seed std>8pp，但我预测实际std在6-9pp范围——足以让reviewer质疑但不至于完全破坏结论。三个seed中一个会表现较差（18%），一个中等（25%，复现原始结果），一个稍好（30%）。这个variance部分来自ALFWorld task sampling的随机性（val set只有16 episodes），部分来自GRPO的inherent instability（高grad_norm, KL spikes在不同seed上timing不同）。1.7B模型的parameter space小，不同random init导致loss landscape上收敛到不同local optima。Mean 24.3%仍远超step-independent baseline（0-6%），但confidence interval宽。"
    tables:
      - name: "Table 2: Multi-seed episode-level results"
        columns: ["Seed", "Success Rate(%)", "Action Valid(%)", "Convergence Step", "Final KL"]
        rows:
          - [42, 25.0, 88.0, 8, 0.048]
          - [123, 18.0, 82.0, 15, 0.092]
          - [7, 30.0, 90.0, 6, 0.035]
          - ["Mean±Std", "24.3±6.0", "86.7±4.2", "9.7±4.7", "0.058±0.030"]
    figures_description:
      - "Figure: Training curves (success rate vs step) for 3 seeds with shaded std band. Band很宽，尤其在step 5-15区间。Seed 123明显延迟收敛。"
    analysis: "Std=6pp略好于worst档定义的8-12pp下界，但仍然problematic。N=3 seeds给出的confidence interval很宽（24.3±6.0意味着95% CI约为[12, 37]），reviewer会正确指出这不够。理想需要5+ seeds但GPU budget不允许。Defense策略：(1)承认limitation，(2)强调所有seeds都远超step-independent baseline 0%，(3)variance主要在收敛speed而非final direction。"

  - name: "Credit assignment mechanism analysis (paper Figure 2)"
    plan_id: "plan_004"
    description: "计算并可视化gamma^(T-h) effective discount, gradient signal strength, episode length correlation。"
    expected_results:
      gamma_value_used: 0.99
      mean_episode_length_T: 48
      gamma_T_minus_1: 0.0061
      gamma_T_minus_2: 0.0062
      gamma_T_minus_5: 0.0065
      gamma_T_minus_10: 0.0068
      gamma_T_minus_20: 0.0075
      gamma_T_minus_full: 1.0
      gradient_signal_h1_relative: 0.006
      gradient_signal_h5_relative: 0.03
      gradient_signal_h10_relative: 0.22
      gradient_signal_full_relative: 1.0
      episode_length_success_correlation: -0.35
      long_episode_success_drop_under_h5: 95
    result_rationale: "Mechanistic analysis本身是deterministic计算（给定gamma和episode length分布），不受worst档位的performance ceiling影响。ALFWorld平均episode length~48 steps，所以gamma^47≈0.006（h=1时first action的discount）。这个数学事实不变。但worst档下的complication是：即使h=full（gradient signal=1.0），模型也只达25%——说明gradient signal是necessary但非sufficient condition。Reviewer会argue：'你解决了gradient signal问题，但模型仍然不行，说明bottleneck在elsewhere'。需要explicitly address这一点：承认model capacity是另一个bottleneck，但credit assignment是第一个需解决的。"
    tables:
      - name: "Table 3: Effective discount factor analysis"
        columns: ["h", "Mean gamma^(T-h)", "Relative Gradient Signal", "Observed Success(%)"]
        rows:
          - [1, 0.006, "0.6%", 0.0]
          - [2, 0.012, "1.2%", 2.0]
          - [5, 0.030, "3.0%", 8.0]
          - [10, 0.220, "22%", 18.0]
          - [20, 0.670, "67%", 24.0]
          - ["full", 1.000, "100%", 25.0]
    figures_description:
      - "Figure 2 (paper核心): 双y轴图。Left y=effective gradient signal (log scale), Right y=observed success rate. x=h value. 两条曲线形态高度相关但非identical，展示gradient signal是necessary condition。Annotation标注'failure zone' (h<5, signal<3%), 'transition zone' (h=5-10), 'saturation zone' (h>10, 性能plateau at model capacity ceiling)。"
      - "Figure 2b: Episode length histogram colored by success/failure. 长episode（>40 steps）在h<10时success接近0，h=full时仍有部分成功。"
    analysis: "这是worst档下最强的contribution piece。数学关系清晰，可视化compelling。关键insight：在RAGEN等现有工作中，默认h=1（step-independent），对应gradient signal仅0.6%——解释了为什么这些方法在long-horizon tasks上struggle。但需要小心措辞：不能overclaim 'episode-level solves multi-turn RL'（因为25%不算solved），只能claim 'episode-level is necessary first step, removing a fundamental training bottleneck'。"

  - name: "Action-change statistics from always-on runs"
    plan_id: "plan_005"
    description: "从exp029 checkpoints收集action-change统计：confirmatory rate, correlation with success, per-task breakdown。"
    expected_results:
      total_verification_episodes: 48
      action_change_rate: 0.35
      confirmatory_rate: 0.65
      action_change_success_correlation_r: 0.15
      action_change_success_correlation_p: 0.18
      per_task_confirmatory_rate_put: 0.72
      per_task_confirmatory_rate_clean: 0.60
      per_task_confirmatory_rate_heat: 0.55
      per_task_confirmatory_rate_cool: 0.58
      per_task_confirmatory_rate_examine: 0.70
      action_change_leads_to_success_rate: 0.22
      no_change_leads_to_success_rate: 0.18
    result_rationale: "在worst档下，episode-level model只有25% success rate，导致action-change统计的样本量极小且noisy。Confirmatory rate 65%落在worst档定义的50-70%范围内，但correlation with success仅r=0.15（p=0.18, not significant）。这是因为：(1)成功episodes太少（~12/48），统计power不足；(2)25%的模型经常在错误轨道上，verification后的action change可能是从一个错误action换到另一个错误action，而非corrective。Action change→success rate (22%) vs no change→success rate (18%)的delta仅4pp，远不够支撑'action change is informative signal'的claim。这直接explains为什么在worst档下必须放弃selective verification story。"
    tables:
      - name: "Table: Action-change statistics"
        columns: ["Metric", "Value", "95% CI"]
        rows:
          - ["Confirmatory rate (no action change)", "65%", "[52%, 78%]"]
          - ["Action change rate", "35%", "[22%, 48%]"]
          - ["Correlation (action_change, success)", "r=0.15", "p=0.18"]
          - ["Success | action_change", "22%", "[10%, 34%]"]
          - ["Success | no_change", "18%", "[8%, 28%]"]
    figures_description:
      - "Bar chart: per-task confirmatory rate. All tasks >55% confirmatory. Wide error bars due to small N per task type."
    analysis: "统计结果不支持action-change作为meaningful reward signal。Correlation not significant，delta too small，CI too wide。这组数据是worst档叙事转向的empirical justification：不是我们选择不做selective verification，而是数据显示在当前performance level下selective verification lacks statistical grounding。Paper中可以brief mention作为'future work when base agent is stronger'。"

  - name: "Selective verification implementation"
    plan_id: "plan_006"
    description: "实现binary verify/skip decision。Code-only, no GPU。"
    expected_results:
      implementation_status: "completed"
      code_lines_added: 350
      integration_test_pass: true
      note: "implementation ready but not deployed for training due to plan_005 results"
    result_rationale: "Implementation本身是engineering work，不受worst档影响。代码可以完成，但基于plan_005的统计结果（action-change correlation not significant），decision是不proceed to training。代码保留为future work artifact。"
    tables: []
    figures_description: []
    analysis: "在worst档叙事下，这个实验stop at implementation。Paper中不报告selective verification training results，而是在discussion section brief mention implementation exists but 'requires stronger base agent to provide meaningful training signal'。"

  - name: "B-IAVR selective verification training"
    plan_id: "plan_007"
    description: "Train selective verification policy via episode-level GRPO。在worst档下执行但预期效果不佳。"
    expected_results:
      training_status: "completed_but_ineffective"
      final_success_rate: 18.0
      always_on_baseline_success: 25.0
      success_delta_vs_always_on: -7.0
      verification_rate_reduction: 12.0
      cost_reduction_pct: 8.0
      training_stability: "unstable"
      convergence_step: "no clear convergence"
      reward_signal_noise: "high"
    result_rationale: "Worst档定义selective_verification_rate_reduction在0-15%，selective_vs_always_on_success_delta在8-15pp。模型从25% base开始，加入verify/skip decision后引入额外exploration space，但base performance本身就marginal。Agent在只有25% success的情况下，缺乏足够的positive reward signal来学习WHEN to verify——大部分trajectory都是failure，无论verify还是skip。结果是verification rate仅下降12%（几乎always verify因为policy没学到有用的skip pattern），且success下降7pp（从25%到18%）因为额外decision point增加了policy complexity。这不构成meaningful contribution。"
    tables:
      - name: "Table: B-IAVR training outcome"
        columns: ["Config", "Success(%)", "Verify Rate(%)", "Cost Reduction(%)"]
        rows:
          - ["Always-on (baseline)", 25.0, 100, 0]
          - ["B-IAVR (trained)", 18.0, 88, 8]
          - ["Delta", -7.0, -12, "+8"]
    figures_description:
      - "Training curve extremely noisy, no clear trend in verification rate reduction over steps."
    analysis: "结果confirms worst档prediction：selective verification在base agent只有25%时无法有意义地训练。-7pp success drop换取仅8% cost reduction，Pareto-dominated by always-on。Paper中不报告此结果，或仅作为negative result brief mention to motivate 'stronger base agent needed'。"

  - name: "Selective verification full comparison"
    plan_id: "plan_008"
    description: "Compare always-on / B-IAVR / no-verify / random-p / confidence-threshold。"
    expected_results:
      always_on_success: 25.0
      always_on_verify_rate: 100
      biavr_success: 18.0
      biavr_verify_rate: 88
      no_verify_success: 15.0
      no_verify_verify_rate: 0
      random_p50_success: 20.0
      random_p50_verify_rate: 50
      confidence_threshold_success: 21.0
      confidence_threshold_verify_rate: 65
    result_rationale: "在25% ceiling下，所有selective methods都worse than always-on。Random-p=0.5 (20%) actually competitive with trained B-IAVR (18%)——trained policy没有学到比random更好的策略，这是devastating negative result。Confidence-threshold (21%) slightly better因为它是heuristic rule而非learned，less prone to policy degradation。整个comparison suite展示：在low-performance regime下，verification的选择性本身不是bottleneck，base capability才是。"
    tables:
      - name: "Table: Full comparison (NOT included in worst-tier paper)"
        columns: ["Method", "Success(%)", "Verify Rate(%)", "Tokens/Episode", "Cost Reduction(%)"]
        rows:
          - ["Always-on", 25.0, 100, 4800, 0]
          - ["B-IAVR (ours)", 18.0, 88, 4420, 8]
          - ["No-verify", 15.0, 0, 2400, 50]
          - ["Random-p=0.5", 20.0, 50, 3600, 25]
          - ["Confidence-threshold", 21.0, 65, 3900, 19]
    figures_description:
      - "Pareto plot (x=cost, y=success): B-IAVR dominated by random-p and confidence-threshold. Only always-on achieves max success."
    analysis: "This entire comparison suite becomes 'data we collected but don't include in paper'。B-IAVR被simpler baselines dominate是fatal for selective verification claim。在worst档pure methodology paper中，这组数据的唯一价值是supporting the narrative 'future work: once episode-level training achieves higher ceiling, selective verification becomes viable'。"

  - name: "No-verify ablation"
    plan_id: "plan_009"
    description: "Episode-level GRPO without self-verification。Lower bound实验。"
    expected_results:
      success_rate: 15.0
      action_is_valid: 78.0
      delta_vs_always_on: -10.0
      mean_episode_length: 38
      convergence_step: 10
    result_rationale: "移除verification后，agent失去每步的self-correction机会。从25%降到15%，delta=10pp。这在worst档下actually是有用的数据点——证明verification本身有10pp价值。但这个delta不够dramatic来支撑'selective verification is the key innovation'的story。在pure methodology paper中可以brief report作为：'verification contributes +10pp, confirming its utility, but our focus is on the training methodology that enables ANY multi-turn RL to work'。"
    tables:
      - name: "Table: Verification value"
        columns: ["Config", "Success(%)", "Action Valid(%)", "Avg Steps"]
        rows:
          - ["Episode-level + verification", 25.0, 88.0, 48]
          - ["Episode-level, no verification", 15.0, 78.0, 38]
          - ["Step-independent + verification", 0.0, 65.0, 50]
    figures_description: []
    analysis: "三行对比table实际很有说服力：step-independent完全fails无论有无verification，episode-level without verification仍有15%。Message: training methodology是前提条件，verification是锦上添花。这fit worst档pure methodology paper的narrative。"

  - name: "Entropy-controlled action-change analysis"
    plan_id: "plan_010"
    description: "Stratify action-change correlation by policy entropy, test partial correlation。"
    expected_results:
      overall_correlation_r: 0.15
      overall_p: 0.18
      low_entropy_stratum_r: 0.08
      low_entropy_stratum_p: 0.55
      high_entropy_stratum_r: 0.20
      high_entropy_stratum_p: 0.22
      partial_correlation_controlling_entropy: 0.12
      partial_correlation_p: 0.28
      n_episodes_per_stratum: 24
    result_rationale: "在worst档25% success下，整体correlation已not significant (r=0.15, p=0.18)。Stratify by entropy后每层只有~24 episodes，statistical power进一步削弱。Low entropy stratum（policy confident）中action-change很少发生（agent已committed to action），correlation near zero。High entropy stratum中有more action-change但也more randomness，correlation略高但仍not significant。Partial correlation r=0.12 (p=0.28)完全不支持'action-change is signal not noise'的claim。根本原因：样本量太小 + base performance太低导致signal-to-noise ratio极差。"
    tables: []
    figures_description: []
    analysis: "在worst档下这组分析的结论是negative：无法reject null hypothesis (action-change = noise)。Paper中不report，或在appendix作为'limitation: at current performance level, insufficient statistical power to establish action-change as reliable signal'。"

  - name: "Causal intervention: random vs verification-triggered changes"
    plan_id: "plan_011"
    description: "Inject random action changes vs verification-triggered. Compare success。"
    expected_results:
      verification_triggered_success: 22.0
      random_change_success: 16.0
      no_change_baseline_success: 18.0
      delta_triggered_vs_random: 6.0
      delta_triggered_vs_random_p: 0.25
      n_episodes: 48
    result_rationale: "Verification-triggered changes (22%) vs random changes (16%) shows 6pp gap，方向正确但p=0.25 not significant。N=48 episodes不够detect这个effect size。No-change baseline (18%)介于两者之间，使得interpretation模糊：triggered changes可能beneficial，但也可能just noise given wide CIs。在25% performance regime下，即使verification IS informative，effect size太小to detect reliably。另一个confounder：random changes有时accidentally correct（16% vs no-change 18%只差2pp），suggesting verification的causal contribution marginal。"
    tables:
      - name: "Table: Causal intervention (insufficient power)"
        columns: ["Condition", "Success(%)", "N", "95% CI"]
        rows:
          - ["Verification-triggered change", 22.0, 48, "[11%, 33%]"]
          - ["Random change (same rate)", 16.0, 48, "[6%, 26%]"]
          - ["No change control", 18.0, 48, "[8%, 28%]"]
    figures_description: []
    analysis: "CIs完全overlap。Experiment was run but results inconclusive。在pure methodology paper中不report。File under 'more data needed at higher performance level'。"

  - name: "Reward signal ablation (action-change vs alternatives)"
    plan_id: "plan_012"
    description: "Train B-IAVR with different reward signals: action-change, random, confidence-based。"
    expected_results:
      action_change_reward_success: 18.0
      action_change_reward_verify_rate: 88
      random_reward_success: 17.0
      random_reward_verify_rate: 82
      confidence_reward_success: 19.0
      confidence_reward_verify_rate: 85
      all_configs_worse_than_always_on: true
      best_reward_signal: "confidence (marginal)"
    result_rationale: "所有reward signals在25% base下都无法学到meaningful selective policy。Action-change reward (18%, verify 88%) vs random reward (17%, verify 82%)的差距仅1pp success——action-change没有demonstrable advantage over random。Confidence-based reward margionally better (19%) because它at least correlates with model's own uncertainty（哪怕calibration差）。但关键point：所有trained selective policies都worse than always-on (25%)。Reward signal choice irrelevant when base performance insufficient to generate learning signal。192 GPU hours换来的结论是'all approaches fail equally in low-performance regime'。"
    tables:
      - name: "Table: Reward ablation (NOT in paper)"
        columns: ["Reward Signal", "Success(%)", "Verify Rate(%)", "vs Always-on Delta"]
        rows:
          - ["Action-change (ours)", 18.0, 88, -7]
          - ["Random trigger", 17.0, 82, -8]
          - ["Confidence-based", 19.0, 85, -6]
          - ["Always-on (no selection)", 25.0, 100, 0]
    figures_description: []
    analysis: "192 GPU hours for a negative result。在worst档下，建议NOT run此实验——plan_007的negative result已sufficient to abandon selective verification direction。Save GPU budget for more h-sweep seeds or ScienceWorld transfer。"

  - name: "ARES reproduction + comparison"
    plan_id: "plan_013"
    description: "Reproduce ARES SFT router on ALFWorld, head-to-head with B-IAVR。"
    expected_results:
      ares_success: 20.0
      ares_verify_rate: 60
      ares_cost_reduction: 30
      biavr_success: 18.0
      biavr_verify_rate: 88
      biavr_cost_reduction: 8
      ares_dominates_biavr: true
    result_rationale: "ARES使用SFT（supervised从expert demonstrations学）which is more data-efficient than RL in low-performance regime。SFT router可以直接学human-pattern的'when to verify'而不依赖agent自身的exploration。预测ARES achieves 20% success at 60% verify rate，Pareto-dominating B-IAVR (18% at 88% verify rate)。这是because SFT不需要agent自己产生positive signal——它从expert data中学。Devastating for our RL-based approach，但irrelevant for worst档paper because we abandon selective verification entirely。"
    tables:
      - name: "Table: ARES comparison (NOT in paper)"
        columns: ["Method", "Success(%)", "Verify Rate(%)", "Cost Red.(%)"]
        rows:
          - ["Always-on", 25.0, 100, 0]
          - ["ARES (SFT router)", 20.0, 60, 30]
          - ["B-IAVR (ours, RL)", 18.0, 88, 8]
    figures_description: []
    analysis: "ARES dominates B-IAVR on Pareto frontier。但在worst档pure methodology paper中，这个comparison不needed也不helpful。如果include，只会invite reviewer质疑'why not just use SFT'。建议NOT run，节省24 GPU hours。"

  - name: "ScienceWorld transfer (episode-level advantage)"
    plan_id: "plan_014"
    description: "Episode-level vs step-independent on ScienceWorld。Second environment for generalization。"
    expected_results:
      episode_level_success: 15.0
      step_independent_success: 2.0
      episode_level_action_is_valid: 75.0
      step_independent_action_is_valid: 55.0
      episode_level_convergence_step: 12
      step_independent_collapse_step: 4
      mean_episode_length_scienceworld: 35
    result_rationale: "ScienceWorld比ALFWorld更难（state space更大，natural language更复杂），1.7B model的absolute performance会更低。Episode-level仍展示优势（15% vs 2%），倍率~7.5x（高于ALFWorld的~4x因为ScienceWorld的longer episodes使credit assignment问题更severe）。Step-independent在step 4 collapse（与ALFWorld pattern一致）。绝对数字15%不impressive，但cross-environment consistency是powerful evidence for the mechanism。在worst档pure methodology paper中，这是ADDRESS single-environment concern的关键实验。"
    tables:
      - name: "Table: Cross-environment validation"
        columns: ["Environment", "Episode-Level(%)", "Step-Independent(%)", "Ratio", "Mean Episode Length"]
        rows:
          - ["ALFWorld", 25.0, 0.0, "∞ (0→25)", 48]
          - ["ScienceWorld", 15.0, 2.0, "7.5x", 35]
    figures_description:
      - "Side-by-side training curves for both environments. Same pattern: step-independent collapses early, episode-level converges (albeit to low absolute value)."
    analysis: "Cross-environment result是worst档paper的第二大contribution。Pattern consistent across environments strongly支持mechanistic explanation。Reviewer concern #2 (single env) addressed。72 GPU hours well-spent for worst档narrative。绝对值低但ratio large，且collapse pattern identical——这是methodology insight的generalization evidence。"

  - name: "7B model scaling verification"
    plan_id: "plan_015"
    description: "Episode-level vs step-independent on Qwen3-7B。Address model size concern。"
    expected_results:
      episode_level_7b_success: 38.0
      step_independent_7b_success: 5.0
      episode_level_7b_action_is_valid: 92.0
      step_independent_7b_collapse_step: 5
      episode_level_7b_convergence_step: 6
      delta_7b_vs_1_7b_episode_level: 13
    result_rationale: "7B model有更高的capability ceiling，episode-level可能达38%（接近40% threshold但仍在worst档范围内——worst档是关于1.7B的performance，7B naturally higher）。Step-independent 7B同样collapse at step 5 (5% max)，确认credit assignment问题is model-size independent。7B的38% vs 1.7B的25%（+13pp）部分validates 'model capacity is separate bottleneck' argument。但192 GPU hours + cloud rental成本高。在worst档下，如果budget tight，这是high-value但high-cost experiment。如果run，结果强力支持narrative：'episode-level advantage holds across scales; larger models achieve higher ceiling但step-independent依然fails regardless of scale'。"
    tables:
      - name: "Table: Model scaling"
        columns: ["Model", "Episode-Level(%)", "Step-Independent(%)", "Advantage"]
        rows:
          - ["Qwen3-1.7B", 25.0, 0.0, "+25pp"]
          - ["Qwen3-7B", 38.0, 5.0, "+33pp"]
    figures_description:
      - "Bar chart: episode-level advantage grows with model size (from +25pp to +33pp), suggesting larger models benefit MORE from episode-level training (because they have more capacity to exploit the better gradient signal)."
    analysis: "如果budget允许，这是worst档paper最能silence reviewer的实验。7B result (38% vs 5%) is more impressive than 1.7B result (25% vs 0%)。Combined message: 'the training methodology enables the model capacity to be utilized; without it, even larger models fail'。论文可能需要重新定位：如果7B reaches 38%，接近40% threshold，paper的overall strength significantly improves even under worst-tier 1.7B results。"

  - name: "Per-task-type breakdown analysis"
    plan_id: "plan_016"
    description: "Breakdown by ALFWorld task type. Shows within-environment diversity。"
    expected_results:
      pick_success_episode_level: 30.0
      pick_success_step_independent: 0.0
      clean_success_episode_level: 20.0
      clean_success_step_independent: 0.0
      heat_success_episode_level: 25.0
      heat_success_step_independent: 0.0
      cool_success_episode_level: 35.0
      cool_success_step_independent: 5.0
      examine_success_episode_level: 10.0
      examine_success_step_independent: 0.0
      pick_two_success_episode_level: 5.0
      pick_two_success_step_independent: 0.0
      episode_length_success_correlation: -0.42
      short_task_advantage: "cool/heat (fewer steps) have higher success"
    result_rationale: "在worst档下，per-task breakdown reveals episode-level advantage is universal但magnitude varies by task complexity。Shorter tasks (cool: ~30 steps, heat: ~35 steps) reach higher success (35%, 25%) because credit assignment even under h=full works better when T is smaller (gamma^0=1 for last step matters more when T smaller)。Longer tasks (examine: ~50 steps, pick_two: ~55 steps) have lower success (10%, 5%) — model capacity ceiling hits harder when trajectory is longer。Correlation r=-0.42 between episode length and success confirms mechanistic explanation。Step-independent fails uniformly across all types (0-5%), confirming the training failure is systematic not task-specific。"
    tables:
      - name: "Table: Per-task breakdown"
        columns: ["Task Type", "Avg Episode Length", "Episode-Level(%)", "Step-Independent(%)", "N (val)"]
        rows:
          - ["pick", 45, 30.0, 0.0, 4]
          - ["clean", 48, 20.0, 0.0, 3]
          - ["heat", 35, 25.0, 0.0, 3]
          - ["cool", 30, 35.0, 5.0, 3]
          - ["examine", 50, 10.0, 0.0, 2]
          - ["pick_two", 55, 5.0, 0.0, 1]
    figures_description:
      - "Scatter plot: x=mean episode length per task type, y=episode-level success rate. Negative correlation visible. Annotation: 'longer tasks → weaker signal even with full context (more steps to credit-assign across)'."
    analysis: "Small N per task type (1-4 episodes in val set) makes individual percentages unreliable，但overall trend (shorter tasks → higher success) supports mechanistic story。In worst档paper，include as supplementary analysis showing the method's advantage is consistent across task types despite varying magnitude。The length-success correlation adds another data point for the credit assignment narrative。"
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d719fa3a-4d91-4575-8608-2e006e982680",
  "isSidechain": false,
  "requestId": "req_011Cb7AGMPpVcgsh3ZzDqgQJ",
  "type": "assistant",
  "uuid": "2cec3635-39f6-44fa-8d29-d492b7bc83a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1",
  "sessionId": "d5bcf265-d8f9-4ed6-8d80-4426d3780ff6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xe52oKJYnULfYrvHc76QMj",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 17026,
      "cache_read_input_tokens": 11841,
      "output_tokens": 10156,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17026,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 10156,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 17026,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17026
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Episode-level收敛停滞在20-30%，selective verification无法有意义地执行，需完全reframe为pure methodology paper 核心假设：['Episode-level训练plateau在20-30%（高于baseline但远不够支撑cost story）…",
  "leafUuid": "2cec3635-39f6-44fa-8d29-d492b7bc83a9",
  "sessionId": "d5bcf265-d8f9-4ed6-8d80-4426d3780ff6"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Episode-level RL failure scenario planning",
  "sessionId": "d5bcf265-d8f9-4ed6-8d80-4426d3780ff6"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Episode-level收敛停滞在20-30%，selective verification无法有意义地执行，需完全reframe为pure methodology paper 核心假设：['Episode-level训练plateau在20-30%（高于baseline但远不够支撑cost story）…",
  "leafUuid": "2cec3635-39f6-44fa-8d29-d492b7bc83a9",
  "sessionId": "d5bcf265-d8f9-4ed6-8d80-4426d3780ff6"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Episode-level RL failure scenario planning",
  "sessionId": "d5bcf265-d8f9-4ed6-8d80-4426d3780ff6"
}
```

---
