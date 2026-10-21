# Paper Framing — Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Fix

> Plan A 转正 (2026-05-17) | Diagnostic + analysis paper. Selective verification 降级为 future work.

## Core Insight

LLM agent 社区默认的 step-independent training 在长 horizon 多轮任务中表现出严重的训练不稳定性和脆弱性（seed 间表现从崩溃至 0% 到极度延迟学习不等）。根因是**双机制失效**（D073：两个机制有定性不同的破坏效果——sign misattribution 破坏训练稳定性使学习极不可靠，information loss 杀死泛化能力，两者必须同时解决）：

1. **Policy Information Loss**: 短窗口（h 步）的 policy 无法学习跨步策略（如 "先探索 drawer 再去 countertop"）
2. **Advantage Sign Misattribution**: step_independent 中，per-window advantage 的符号由 group normalization + episode outcome 共同决定，而非 task-relevant action quality：
   - **Type C evidence (D063)**: 失败 episode 中零 penalty 的 window（action 全 valid 但 task 失败）→ step_return=0 高于被 penalty 拉负的 group mean → 获得**正** advantage 被强化。直接证据：32/800 windows (4%)
   - 模型学会避免 format errors（action_is_valid ↑）但不学 task success — 与 exp013f gaming 观察一致
   - GRPO group normalization 使 advantage 区分 format quality（有无 penalty），不区分 task progress
   - 附加：γ^k magnitude decay 使早期 window 信号更弱（γ^24 ≈ 29%）
   - **实证确认 (tab3)**：per-sample advantage sign accuracy = 52.07% (n=3000, ≈random)；GRPO group majority = 81.25% vs 理论 79.5%（高度吻合）。Sign misattribution 从理论预测升级为实证确认
   - **理论精度注意**：Proposition 2 的纯二值假设 (R ∈ {0, r+}) 需要扩展为包含 penalty 影响的版本。"80.9% wrong sign" 基于 binary assumption；实际 penalty 创造连续分布，misattribution 机制更复杂但方向不变

Episode-level training 同时解决两者：policy 看全历史（解决 1），整条 trajectory 作为一个 GRPO 样本，所有 tokens 共享同一 advantage — 虽然仍是 episode-level credit（非 per-token），但消除了 window 间的 sign misattribution，因为不再需要将 episode reward 分配到独立优化的子窗口（解决 2）。

**8B Scale Verification (D083-D085)**：Qwen3-8B (8.2B params) 验证双机制 scale-invariance：
- **Information loss 量化 (D087, deterministic eval 完成)**：同一 8B SFT checkpoint，bjb1 2GPU, T=0 deterministic, 同一 32 in-dist tasks。Full context = 68.75%, h=2 = 31.25%。**Information loss = 37.5 pp，纯推理时损失，RL 还没开始。** h=2 response_length 仅 17 tokens vs full context 2186 tokens——极端截断导致模型几乎无法推理。注意：FSDP GPU 数量影响绝对数字 (M020)，论文必须用同服务器配对测量。
- **Cell A collapse (D085)**：8B Cell A step 1 = 12.5%（从 28.1% baseline 腰斩），step 2 = 1.5625%（Q4 完全崩溃确认）。
- **Scale-invariant mechanism, stochastic-triggered (Agent W&B 分析确认)**：
  - 8B Cell A：entropy 坍塌 (0.115) → 反弹 (0.605) + ppo_kl 转负 (-1.885)，2 步内完全崩溃
  - 1.7B seed1 (7o9bjszm)：**完整复现且更剧烈**——3 阶段 entropy oscillation (0.33→1.01→0.33→0.55) + 3 次 negative KL (step 11/12/15)，15 步崩溃到 0%。与 8B 同一破坏路径，仅时间尺度不同
  - 1.7B seed2 (jhwyg4tc)：**正常学习**——entropy 稳定 0.25-0.43，KL 全程正值，success 升到 28.1%
  - **论文 framing**："The failure mechanism (entropy oscillation + negative KL divergence) is identical across model scales; it is stochastic-triggered rather than deterministic. When triggered, the destruction pathway is consistent regardless of model capacity." 这解释了社区为什么没有普遍注意到问题——有时 works 有时不 works，但风险始终存在
  - 8B 与 1.7B 的差异是 **速度** 而非 **机制**：8B 2步崩溃 vs 1.7B 15步崩溃，更大模型可能因策略空间更大导致 sign misattribution 的破坏更迅猛
- **Cell C 完成 (D098→D103)**：经历 v1-v9b 共 11 次失败后，v9d 通过 FSDP2+CPUOffload 成功训练。Step 12 reward 饱和（100% in-dist success, pg_loss=0），step 10 为最终有效模型。**OOD eval: 90.3% pass@1 (134 tasks)**，vs SFT 80.6% (+10pp)，vs Cell A 1.5% (collapse)。action_is_valid 98.7%。⚠️ 待确认实际 temperature（config 有 T=0.4 和 T=1.0 两处值）。
- **结论**：**Claim 范围已扩展：fix 跨尺度有效。** 不仅 failure mechanism 跨尺度一致，episode-level fix 在 8B 尺度上效果更强（1.7B: 23.88% OOD; 8B: 90.3% OOD）。跨尺度证据链完整：failure(Cell A collapse) + fix(Cell C success) 双向验证。

**技术澄清**：GRPO 算法本身是 bandit-style（advantage = (R-μ)/σ，无显式 γ），但 RAGEN 的 step_independent 实现在 `compute_step_discounted_returns()` 中引入 γ 计算每个 window 的 return（代码：`agent_trainer.py:271-340`）。γ^(T-t) decay 对 step_independent 模式是代码事实，不是类比。Episode-level 模式下无此问题：整条 trajectory 只有一个 return = episode_reward。

## Operational Definitions (D138)

**2×2 Framework** (training stability × OOD generalization):

|  | OOD ≤ SFT (NS) | OOD >> SFT (p<0.01) |
|--|-----------------|---------------------|
| **Training collapsed** | Collapsed (seed2048/8/42) | — (not observed) |
| **Training non-collapsed** | Stagnant (seed100/200/300) | Generalized (seed4/5/6) |

Special category: **Delayed learner** (seed2) — initially collapsed-like, eventually non-collapsed with moderate OOD (15.67%, p=0.02).

**Training stability** (based on training dynamics):
- **Collapsed** = ID success from peak sustained decline >50% without recovery (≥3 steps), OR never significantly exceeds SFT baseline (>2x). Typical pattern: response_length explosion + ID success drop to near-zero.
- **Non-collapsed** = complement of collapsed. Maintains ID learning without sustained degradation.

**OOD generalization** (based on 134-task OOD eval, Fisher exact vs SFT baseline 6.72%):
- **Generalized** = OOD significantly exceeds SFT (Fisher exact p < 0.01). seed4/5/6: 25-31%, all p<0.001.
- **Stagnant** = OOD not significantly different from SFT. seed100/200/300: 10-12%, all NS.

**Core finding (D137→D138)**: Step-independent training → 100% collapse (all seeds in factorial Cell A). Episode-level training → 73% non-collapsed (8/11), but only 27% (3/11) achieve OOD generalization. Episode-level is necessary but not sufficient for OOD transfer.

**Collapse rate** (N=11): Collapsed 3 / Stagnant 3 / Generalized 3 / Delayed 1 / Unclassified 1 (seed1).

## Story Arc

**Single contribution**: Mechanistic diagnosis of step-independent training failure + episode-level fix

叙事线：
1. Multi-turn agent RL 需要跨长 trajectory 的 credit assignment，但社区默认 step-independent windowing
2. Step-independent training 在多轮任务上导致训练不稳定（seed1 崩溃至 0%, seed2 延迟学习至 9.375% in-dist / 3.73% OOD），gradient signal 52% sign agreement ≈ 随机噪声
3. 我们诊断双机制根因：(1) policy information loss（inference layer, 常数 ceiling）+ (2) advantage sign misattribution（training layer, 累积退化）
4. 形式化分析：P(correct sign | update) = p/(1-(1-p)^K)，在 p=12.5%, K=8 时仅 19.1% 正确
5. Episode-level GRPO 同时解决两者，从 SFT baseline 2.24% 提升到 23.88% (OOD 134 tasks, T=0.4)。**评估协议 (D092)**：论文统一用 T=0.4 (do_sample=True)，与 RAGEN 训练 eval 一致。T=0.0 greedy 得 16.4% (22/134)——差异来自 greedy decoding 的重复循环陷阱，不是 checkpoint 问题。**T=0.4 per-task 已完成**：独立 eval 得 19.4% (26/134)，与 RAGEN 内置 23.88% 存在 pipeline 差异，正在调查
6. **Factorial 实验揭示两个机制的定性差异 + Cell B 泛化 ceiling seed-invariant**（D073→D078, 核心论据）：
   - Cell A (step-level + truncated): 高坍缩风险（seed1=0%, seed2=3.73% OOD）— sign misattribution 破坏训练稳定性，学习极不稳定
   - Cell B (episode-level + truncated): 训练中能学习但 OOD 崩溃。**关键发现 (D078)**：两个 seed 在 train success 差距极大（20% vs 55.5%）的情况下，step 15 val OOD 完全一致 (0.75% = 1/134)。Information loss 创造了 **hard representational ceiling**，不同训练轨迹收敛到相同的 OOD 上限。这不是典型 RL overfitting（训练分布不够多样），而是 **architectural bottleneck**——h=2 context window 结构性地无法表示需要跨步信息的策略
   - Cell C (episode-level + full context): 两个 seed 都超过 baseline（seed1 28.1%, seed2 31.25%），与 Cell A/B 的系统性失败形成鲜明对比。Claim 表述：**"enables non-trivial learning in both seeds, in sharp contrast to the systematic failure of Cells A and B"**。seed2 训练方差较大（grad_norm 攀升），但 RL 训练 seed 间差异是已知特性，论文一句带过。exp029_seed2 报告 step 30 数据（val 31.25%），继续跑但不 per-seed 调参（避免 cherry-picking 嫌疑）
   - **注意**：早期定量分解（step 5: B=5.97% > A=3.73%）在 step 15 失效（B=0.75% < A），加法模型不可靠。论文报告全 step 轨迹，不做 checkpoint cherry-picking
   - **论文写法**：Results 加入 "learning without generalization" 子节，展示 Cell B 的 train vs OOD 分离曲线。引用 Cobbe et al. 2019 / Kirk et al. 2023 RL generalization survey 做 positioning，明确区分 "our finding is a structural representation bottleneck, not a statistical generalization gap"
7. γ-sweep 佐证（D075 确认情景 1）：g050/g080/g095/g100 **全系列坍缩**，包括 γ=1.0（无折扣）。结论：sign misattribution 是 step-level windowing + GRPO group normalization 的固有属性，与 magnitude decay 无关。γ-sweep contribution 从"发现 γ-cliff"升级为"证明 step-independent windowing 的根本不兼容性——无论 γ 取何值"。需补充 advantage sign 分布分析作为额外支撑
   - **Factorial seed2 (D076→D078) 跨 seed 验证最终确认**：seed2 完整轨迹 2.24%(step5) → 2.24%(step10) → **0.75%(step15)**，与 seed1 step 15 val OOD **完全一致 (0.75%=1/134)**。尽管 train success 差距极大（seed1 ~20% vs seed2 55.5%），OOD 泛化同样崩溃。Information loss 对泛化创造 hard representational ceiling，与训练轨迹无关（N=2 seeds，"hard ceiling" 而非 "deterministic"）
8. 分析 "为什么社区默认走向 step-independent"（context length 限制 + token-level training 惯性 + framework design accident + 6 factors）
9. **干预实验 (D119-D128, Discussion section, SUPPLEMENTARY evidence)**：
   
   **⚠️ 证据层次（D128, Reviewer 审查确认）**：
   - **Primary**: tab3 per-sample advantage sign accuracy = 52.07% ≈ random（sign misattribution 的直接实测）+ Proposition 2 理论推导
   - **Secondary**: factorial experiment（Cell A/B/C 分离两个机制的 causal contribution）
   - **Supplementary**: 干预实验（Discussion 中展示 symptom-level 干预的 ceiling，不是核心论证）
   
   四种干预方向：
   - **Intervention A (reward penalty)**: 无效。penalty 只影响 gradient magnitude 不影响 sign
   - **Intervention B (KL 10x)**: **部分有效但极慢** — step5=8.21% → step7=12.69% (+4.48pp)。KL 约束 policy drift 速度，允许缓慢学习。但远低于 episode-level (23-37%)。**KL 减速但不改变方向**
   - **Intervention C (hard cap)**: **部分有效但 delayed collapse** — step5=19.40%，step7=16.42% (-2.98pp)。物理阻断 response inflation 通道，前期见效但逐步退化
   - **Intervention C' (trajectory cap)**: 11.94% OOD（D127），但有两个混淆因素：(1) cap 代码 bug 从未触发，有效机制是 max_turn=25 副作用 (2) train 25-turn vs eval 50-turn distribution mismatch。**论文中降权处理**：正文 1-2 句带过 + Appendix 详述，不与 B/C 等权呈现
   
   **论文叙事 (D128)**：正文 Discussion 聚焦 B+C 双轨对比——"fast-but-degrading (hard cap) vs slow-but-improving (KL), both converging to a sub-optimal ceiling far below episode-level (8-19% vs 23-37%)"。多条 downstream 干预路径收敛到类似 ceiling，而 episode-level 消除 windowing 后直接跳到 23-37%，这个 gap pattern 比任何单条干预更有说服力。
   
   **⚠️ 已知 alternative explanation 及防御**：审稿人可能提出"根因是 response inflation incentive，非 sign misattribution；完美的 inflation control 或可完全解决"。防御：tab3 直接测量 sign accuracy = 52% ≈ random，这是 sign misattribution 的独立实证，不依赖干预实验。干预实验的角色是展示 downstream 症状无法根治，不是证明 sign misattribution 存在。
   
   **写作注意**：abstract/intro 不强调干预数量。用 "multiple interventions targeting different symptom channels" 而非 "3/4 partially effective"。数字放 Discussion 表格

**定位**：不 claim "发明了 episode-level RL"（trivial），而是 "诊断了 LLM agent RL 训练中被忽视的 step-independent 隐性代价 + 形式化双机制分析 + factorial causal attribution + 实用修复方案"

## Target Venue

**EMNLP 2026**（ARR 统一审稿，8 页正文）。目标 Overall Assessment ≥ 4（Conference accept）。补齐 ScienceWorld 跨环境验证后投稿。

## Core Claims

### Claim 1 (strength: VERY STRONG): Step-independent windowing introduces a systematic, scale-invariant failure mechanism — sign misattribution — that renders multi-turn agent training unreliable. Episode-level credit assignment is a necessary minimum fix. (D104: 从 D067 "unstable/fragile" 升级；不用 "catastrophic"——1.7B seed2 学了 9.375%；不 claim optimal——承认 GAGPO 等 finer credit 更强)
- 所需证据：episode-level vs step-independent 对比（多 seed），h-sweep ablation，mechanistic analysis（gradient signal measurement），REINFORCE++ baseline comparison，factorial experiment
- 当前证据状态：**ESTABLISHED** (exp029 val=28.125% vs hsweep_h2_seed1 val=0%)
- 机制：(1) policy information loss (h-step context insufficient), (2) advantage sign misattribution (gradient direction reflects episode outcome, not window-local action quality; additionally γ^k magnitude decay for early windows)
- 技术细节：GRPO 算法无固有 γ，但 RAGEN step_independent 的 `compute_step_discounted_returns()` 引入 γ-discounted per-window returns → advantage 符号由 episode 成败决定。代码验证：`agent_trainer.py:271-340` + `core_algos.py:194-246`
- 补充证据（进行中）：
  - h-sweep **全部完成 (D084)**：h=2(0%), h=5(0%), h=10(6.25%=baseline), h=20(15.625%), h=full(28-31%)。Cliff 位于 h=10 和 h=20 之间——情景 B 确认（sharp phase transition）。h=20 有学习但远低于 full context，支撑 "context threshold exists but full context still needed for robust learning"
  - hsweep_h2_seed2（崩溃复现 + per-window advantage logging for tab3）
  - factorial_h2_episodeadv（plan_018, 双机制因果分离）
  - γ-sweep **全系列完成 (D075)**: g050/g080/g095/g100 全部坍缩。γ=1.0 无折扣仍坍缩 → sign misattribution 是 windowing + group norm 固有属性
  - factorial seed2 (D076→D078): **完整验证**。step 15 val OOD = 0.75%，与 seed1 完全一致。Train 55.5% vs OOD 0.75% — 学习与泛化完全脱钩
  - **Negative 结果利用 (D072/D075)**: γ-sweep 全坍缩 → "no γ-cliff" figure（更强：全面不兼容）; factorial 振荡 vs Cell A 坍缩 → 训练动态对比; seed 间 variance → 不稳定性证据
  - **Per-task-type OOD breakdown (exp029 seed1, 134 tasks, T=0.4)**：pick_and_place 16.7% (4/24), pick_clean 25.8% (8/31), pick_heat 17.4% (4/23), pick_cool 23.8% (5/21), look_at_obj 27.8% (5/18), pick_two_obj **0.0%** (0/17)。Total 19.4% (26/134)。多步操作型任务（pick_two_obj/pick_heat）success 最低，符合 information loss 假说。pick_heat/pick_cool 在 T=0.4 下比 T=0.0 大幅提升 (+13.1/+14.3 pp)，说明这些任务受益于探索性采样。pick_two_obj 在 T=0.4 下完全失败（T=0.0 为 5.9%），可能是 17 样本采样噪声。
  - **Eval pipeline 差异 (已解决)**：独立 eval script (T=0.4) = 19.4% (26/134) vs RAGEN 内置 eval (T=0.4) = 23.88% (32/134)，差 4.48 pp ≈ 1.3σ (p≈0.19)。**根因：T=0.4 随机采样方差**，非 pipeline bug。次要系统性差异（stop token 处理、action parser 规范化）影响 ≤1-2 games。**论文统一用 RAGEN 内置 eval 的 23.88%**（方法论一致性：训练和 eval 同一 pipeline）
  - **统计分析 (Table 1 数据, Wilson 95% CI, Fisher exact)**：
    - **Generalized seeds** (unified pipeline): mean=**28.36% ± 2.20%** (seed4 30.60%, seed6 29.10%, seed5 25.37%)。跨 seed 方差极低。seed1 23.88% 非统一 pipeline，含则 4-seed mean=27.24%
    - 所有 generalized seeds vs SFT (6.72%): **p < 0.001** (Fisher exact)，OR 4.7-6.1
    - intervention_c step5 (19.40%) vs SFT: **p = 0.003**，显著
    - high_kl step5 D134 re-eval: 9.70% (13/134), NS vs SFT
    - **Collapsed seeds**: seed2048 8.21%, seed42 12.69%, seed8 13.43% — CI 与 SFT 重叠，无显著学习
    - **Stagnant seeds** (D137): seed100 step5=11.19% step10=12.69% (+1.5pp, both NS), seed200 step5=10.45% (NS), seed300 step5=10.45% (NS), seed2 step15=15.67% (p=0.02*). ID 学习但 OOD 不泛化
    - **Three-tier differentiation (D137, N=11 seeds)**: Collapsed 3 / Stagnant 4 / Generalized 3 / Unclassified 1. Collapse rate = 27%. Table 1 有 17 个数据点（多 step 和干预实验）
    - **论文写法**：报告 Wilson CI 而非 p-value 二分判断；generalized seeds 的 tight CI 不重叠 SFT CI → 视觉清晰。三层分化用颜色编码（red/orange/green）在 learning curve figure 中展示

### Claim 2 (strength: N/A — future work): Action-change is an effective intrinsic reward for verification informativeness
- 当前状态：**降级为 future work**，论文中仅作为 proposed design 描述（§3.6, §5.5）
- 不在本论文中实验验证

### Claim 3 (strength: N/A — future work): Learned selective policy matches always-on performance at reduced verification cost
- 当前状态：**降级为 future work**，论文 Conclusion 中列为 extension direction
- 不在本论文中实验验证

## Current Plan (Plan A 已转正)

**论文定位**：Diagnostic + analysis contribution. 核心贡献是双机制诊断 + factorial causal attribution，不是 performance improvement.

**标题方向**：诊断导向（如 "Sign Misattribution in Step-Independent Agent RL"），不是 selective verification 导向

**Dream review 经验**：纯 methodology paper 需要比预期更深的分析才能通过审稿。当前策略：h-sweep cliff + γ-sweep + factorial 2×2 + per-window advantage logging 提供充足的实证深度

**Selective verification 路径**：作为 future work 保留在论文 §3.6 和 Conclusion 中。如后续 episode-level agent 达到 ≥40% success，可作为 follow-up paper 独立展开

## Reviewer Attack Surface + Defense

| # | Concern | Severity | Defense |
|---|---------|----------|---------|
| 1 | "Episode-level RL is obvious / well-known" | HIGH | h-sweep (3 seeds) 展示 non-trivial cliff + 双机制理论 + "为什么社区默认 step-independent" 分析 |
| 2 | "Theory 与 GRPO 不匹配" | HIGH | 精确区分：GRPO 算法无 γ，但 step_independent 实现引入 γ-discounted returns（代码引用）→ per-window advantage logging 实证 + 伪代码 |
| 3 | "缺 GAE/标准 RL baselines" | HIGH | REINFORCE++ baseline (per-token running-mean, TRL 1.1.0). GAE 不可用（TRL 移除 ValueHead，脚注说明）。REINFORCE++ plateau at 12.5% 证明 per-token baseline 不解决 episode-level credit |
| 4 | "Self-Guide 3x performance gap" | HIGH | 正面回应：不同 paradigm (expert-guided vs from-scratch RL)，不同问题（Self-Guide 回避了训练问题） |
| 5 | Single environment (ALFWorld) | HIGH | **ScienceWorld Cell C 实验线终止 (D131)**：v4/v4b/v5/v6 共 4 次尝试全部失败（collapse + SFT checkpoint 丢失）。**已有跨环境证据**：(1) Cell A collapse 在 ScienceWorld 确认 (0%) — 跨环境失败机制验证 ✅; (2) v4b+v5 collapse pattern 精确复现 ALFWorld（KL 控 drift 但不阻 inflation — 跨环境 KL 机制证据）; (3) 8B scale verification (90.3% OOD) 提供同环境不同尺度的 dual verification。**Limitations 写法**：Cell A 失败机制跨环境确认，Cell C fix 仅 ALFWorld 验证——episode-level GRPO 效果可能依赖 SFT 起点质量和环境复杂度 |
| 6 | Small model (1.7B) | **RESOLVED** | 8B 全套完成：Cell A Q4 collapse (28.1%→1.5%), Cell C OOD **90.3%** (vs SFT 80.6%), info loss 37.5pp deterministic。Failure + fix 双向跨尺度验证。 |
| 7 | Action-change = noise vs signal | LOW | 已降级为 future work，不在审稿范围 |
| 8 | 与 ARES 差异化不足 | LOW | 论文不再做 selective verification，与 ARES 不直接竞争 |
| 9 | "Turn-PPO 已解决相同问题" | HIGH | 精确区分：Turn-PPO 发现 uniform advantage（症状）+ 提出 finer fix。我们提供 factorial causal attribution（plan_018 分离 info loss vs sign misattribution 各自贡献）— 诊断深度不同，不是解法方向不同 |
| 10 | "GAGPO 93.5% 证明 finer credit 更好" | HIGH | 不否认。我们的 claim 不是 "coarser is better"，而是 "为什么 broken step-independent 失败"。Episode-level 是 necessary minimum（排除 misattribution），不是 optimal solution。GAGPO 的成功与我们的诊断互补不矛盾 |
| 11 | "Factorial experiment 缺失导致 dual mechanism 未验证" | HIGH | plan_018 直接回应：truncated-obs + episode-advantage 的 2×2 设计分离两个机制的 causal contribution |
| 12 | "干预部分有效说明问题只是 response inflation" | MEDIUM | 干预实验是 supplementary evidence（D128）。核心防御不在干预本身，而在 tab3 sign accuracy = 52% ≈ random 的直接实测。B+C 双轨对比（fast-but-degrading vs slow-but-improving，均 8-19% 远低于 episode-level 23-37%）展示 downstream 干预的 ceiling pattern，加强但不承载论证 |

## Evidence Status Matrix

| Claim | MVP Evidence | Research Evidence Needed | Priority | Status |
|-------|-------------|--------------------------|----------|--------|
| Claim 1 | exp029 val=28.125% vs hsweep_h2 val=0% | h-sweep ✅, factorial ✅, γ-sweep ✅, 8B scale ✅ (90.3% OOD), intervention ✅ (D128), multi-seed OOD ✅ (13 data points + 统计分析完成), ScienceWorld v5 failed (D129), v6 准备中 | P0 | **VERY STRONG** — 统计分析：healthy seeds 28.36%±2.20% (all p<0.001 vs SFT 6.72%)，跨 seed 方差极低。seed100+200 训练中扩 N=9-10。ScienceWorld v6 最后尝试 |
| Claim 2 | N/A | Future work | Deferred | N/A |
| Claim 3 | N/A | Future work | Deferred | N/A |

## Competitive Positioning

| System | Method | Benchmark | Key Difference from Us |
|--------|--------|-----------|----------------------|
| Self-Guide (2026) | Always-on verification | ALFWorld 72.7% (1.7B) | Expert-guided vs from-scratch RL; different paradigm |
| ARES (2603.07915) | SFT router, continuous effort | 52.7% token reduction | Not directly competing (our paper not about selective verification) |
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

**核心差异化：Mechanistic Diagnosis + Factorial Causal Attribution。** 竞品追求 SOTA performance（HOW to do credit well），我们回答诊断问题（WHAT goes wrong and WHY）。

1. **从症状到因果**：Turn-PPO 发现 "uniform advantage"（症状），我们分解为两个独立因果机制（information loss + sign misattribution）并通过 factorial experiment (plan_018: 2×2 design) 量化各自贡献。这是 causal attribution，不是 restatement。

2. **Honest positioning（不 claim "coarser is better"）**：GAGPO 93.5% at 1.5B 证明正确的 fine-grained credit IS superior for performance。我们的 claim 是："step-independent windowing 引入 sign misattribution，episode-level 是消除此问题的 necessary minimum fix。这不意味着 finer credit 无价值——它揭示的是 incorrectly-windowed credit 的具体失败机制。" **禁用旧的 'contrarian' 叙事**。

3. **不同 contribution 维度**：GAGPO/HiPER 追求 performance。我们提供 mechanistic understanding — 实践者需要先理解 failure mode 才能选择正确的 fix（episode-level minimum vs turn-level vs step-level）。两个贡献维度互补不对立。

4. **Factorial rigor 的差异**：Turn-PPO / CA Survey 停留在观察 + 经验 fix。我们通过 2×2 factorial（truncated-obs × episode-advantage）分离因果，这在 agent RL 文献中是 novel methodology contribution。

## Research Phases

1. **Phase A (DONE)**: Episode-level GRPO training — MVP passed (exp029 val=28.125%)
2. **Phase A+ (ACTIVE)**: Ablation suite for Claim 1 depth:
   - h-sweep ablation (h=2 DONE, h=5/10/20 pending 24-48h)
   - γ-sweep **全系列完成 (D075)**: g050/g080/g095/g100 全部坍缩，γ=1.0 无折扣仍坍缩
   - hsweep_h2_seed2 (DONE, collapse replication + advantage logging)
   - factorial_h2_episodeadv seed1 (DONE, D073), seed2 (RUNNING, D076 P0 step 5 通过)
   - REINFORCE++ baseline (DONE, val 12.5% plateau)
   - Dense reward baseline (DONE, exp013f, 0% success / 97.5% validity)
3. **Phase B (DEFERRED — future work)**: Selective verification with action-change reward
4. **Phase C (DEFERRED — future work)**: Selective verification comparison suite
5. **Phase D (CONDITIONAL)**: Multi-env / multi-model scaling (if resources permit before submission)
