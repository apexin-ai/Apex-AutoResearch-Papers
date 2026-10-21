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
