# 文献调研：Step-Independent RL 训练失败的跨领域证据

> 目标：为我们的 sign misattribution 发现（step-independent GRPO 中 advantage 与 episode outcome 的 agreement 仅 52%≈随机）提供泛化性佐证。
> 调研时间：2026-05-18

---

## 一、核心发现总览

搜索覆盖 5 个方向（RAGEN 系列、Agent RL 框架、多轮对话 RL、经典 credit assignment、2024-2026 最新 arXiv），深入阅读 40+ 篇论文。

**结论：step-independent episode-level advantage 在 multi-step agent RL 中导致 catastrophic collapse 是被广泛报告、多角度验证的普遍问题，不是特定环境/模型的个例。**

---

## 二、Tier 1：直接佐证 Sign Misattribution / Advantage 方向错误

### 2.1 IRC: Iterative Reward Calibration (2026)
- **论文：** Multi-Turn Reinforcement Learning for Tool-Calling Agents with Iterative Reward Calibration
- **arXiv:** https://arxiv.org/abs/2604.02869
- **关键发现：** **明确报告 advantage sign disagreement。** Table 1 显示 per-turn intermediate advantage (A^I) 与 outcome advantage (A^O) 方向不一致："read-only and soft match show misalignment: A^I reinforces but A^I+A^O suppresses"。Dense per-turn reward 导致性能下降 6.5-14 pp（Qwen3.5-4B: 63.8%→57.3%）。提出 point-biserial correlation 校准方法。
- **佐证强度：** 直接佐证（唯一明确报告 advantage direction mismatch 的工作）
- **引用价值：** 可直接引用

### 2.2 MC-GRPO: Median-Centered GRPO (2025)
- **论文：** MC-GRPO: Median-Centered Group Relative Policy Optimization for Small-Rollout RL
- **arXiv:** https://arxiv.org/abs/2601.22582
- **关键发现：** 直接研究 **advantage sign flip** 问题。小 rollout budget 下 GRPO 的 mean baseline 被 outlier 扰动，导致 advantage 符号翻转。**5% sign-flip rate 即导致 GSM8K accuracy 下降约 4%。** Figure 2 显示 sign-flip rates 在 G∈{2,4} 时最高。提出 median-centering 替代 mean-centering。
- **佐证强度：** 直接佐证（sign flip 的定量分析）
- **引用价值：** 可直接引用

### 2.3 G-RA: Gated Rewards for Agent RL (2025)
- **论文：** Stabilizing Long-term Multi-turn Reinforcement Learning with Gated Rewards
- **arXiv:** https://arxiv.org/abs/2508.10548
- **关键发现：** **Figure 3 展示 accumulated reward 与 outcome reward 的 sign divergence**："accumulated reward keeps increasing while the outcome reward decreases during RL process"。不使用 gating 时 catastrophic policy degradation：completion rate 从 47.6% 降至 1.4%（100步后）。D-RA (direct accumulation) 导致 intermediate reward 与 outcome reward 负相关。
- **佐证强度：** 直接佐证（step reward 与 episode outcome 方向反转的直接证据）
- **引用价值：** 可直接引用

### 2.4 GRPO-λ: Credit Assignment via Eligibility Traces (2025)
- **论文：** GRPO-λ: Credit Assignment improves LLM Reasoning
- **arXiv:** https://arxiv.org/abs/2510.00194
- **关键发现：** **Lemma 1 证明 GRPO 的 normalized advantage estimation 对后续 tokens 越来越有偏。** 因为所有 rollouts 从同一 s₀ 开始，baseline μₜ 只在 t=0 时准确，对下游 tokens 产生 systematic misattribution。训练效率提升 30-40%。
- **佐证强度：** 直接佐证（数学证明 uniform advantage → systematic misattribution）
- **引用价值：** 可直接引用

### 2.5 Outcome-Grounded Advantage Reshaping (2026)
- **论文：** Outcome-Grounded Advantage Reshaping for Fine-Grained Credit Assignment in Mathematical Reasoning
- **arXiv:** https://arxiv.org/abs/2601.07408
- **关键发现：** 明确指出标准 policy gradient 将 uniform advantage 分配给所有 tokens，无法区分哪些步骤贡献了正确/错误结果。**将此问题命名为 "advantage misattribution"**。通过 outcome-grounded reshaping 识别 critical tokens，修正 sign errors。
- **佐证强度：** 直接佐证（术语和问题定义最接近我们的发现）
- **引用价值：** 可直接引用

### 2.6 Decoupled Credit Assignment (ICLR 2026)
- **论文：** Both Local Validity and Global Effectiveness Matter: Decoupled Credit Assignment for Long-Horizon Agentic Learning
- **链接：** https://openreview.net/forum?id=Suja4AQ9Fo
- **关键发现：** 识别 additive credit assignment 的关键缺陷：**invalid actions 在 positive trajectories 中被分配 positive credit。** 提出 multiplicative gated rewards (MGR)："the action's validity strictly governs the reward's polarity (sign), preventing credit misassignment"。
- **佐证强度：** 直接佐证（直接论述 sign/polarity 误分配问题）
- **引用价值：** 可直接引用

---

## 三、Tier 2：GRPO Catastrophic Collapse 的系统性证据

### 3.1 RAGEN (2025)
- **论文：** RAGEN: Understanding Self-Evolution in LLM Agents via Multi-Turn Reinforcement Learning
- **arXiv:** https://arxiv.org/abs/2504.20073
- **关键发现：** GRPO 在 Bandit/Sokoban 上分别在 20/10 步即 collapse（远早于 PPO 的 100/50 步）。识别 **Echo Trap**：reward std 骤降 → entropy 下降 → gradient norm spike → 不可逆 collapse。"Sparse delayed reward fails to differentiate coherent reasoning from trial-and-error success"。StarPO 使用 trajectory-level reward，所有 token 共享相同 normalized advantage。
- **佐证强度：** 直接佐证
- **引用价值：** 可直接引用

### 3.2 RAGEN-2 (2026)
- **论文：** RAGEN-2: Reasoning Collapse in Agentic RL
- **arXiv:** https://arxiv.org/abs/2604.06268
- **关键发现：** **Advantage collapse 的数学证明：** `|g_task(x)| ≤ √(Var(R|X=x)) · C`。当 within-prompt reward variance → 0 时，task gradient 几乎消失，regularization gradient 主导 → 更新方向被 input-agnostic noise 主导。**这与我们的 52% agreement rate 高度一致：当 advantage ≈ 0 时 sign 基本随机。** Collapse 跨所有算法（PPO, DAPO, GRPO, Dr. GRPO）。推理长度在所有 8 个环境中单调下降。
- **佐证强度：** 直接佐证（更强，提供数学证明）
- **引用价值：** 可直接引用

### 3.3 Turn-PPO (EACL Findings 2026)
- **论文：** Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL
- **arXiv:** https://arxiv.org/abs/2512.17008
- **关键发现：** **GRPO 在 WebShop 和 Sokoban 上直接 crash（reward=0）。** 尝试了 3 种 GRPO 修复策略（去 std normalization、去 KL、增加 batch diversity），**"all modifications still fail to prevent training collapse"。** 数据：Sokoban-3B GRPO=Crash, Turn-PPO=2.29; Sokoban-7B GRPO=Crash, Turn-PPO=3.74。
- **佐证强度：** 直接佐证
- **引用价值：** 可直接引用

### 3.4 GRPO Collapse / Search-R1 (2025)
- **论文：** On GRPO Collapse in Search-R1: The Lazy Likelihood-Displacement Death Spiral
- **arXiv:** https://arxiv.org/abs/2512.04220
- **关键发现：** Lazy Likelihood Displacement (LLD) death spiral：correct 和 incorrect responses 的 likelihood 同时下降 → low-confidence → inflated gradients → collapse。所有 4 个测试模型（Qwen 3B/7B, Base/Instruct）在 **300 steps 内全部 collapse**。~60% incorrect responses 初始搜索查询正确 → 共享 action 产生冲突 gradient signals。
- **佐证强度：** 直接佐证
- **引用价值：** 可直接引用

### 3.5 Gradient Coupling (2025)
- **论文：** Gradient Coupling: The Hidden Barrier to Generalization in Agentic RL
- **arXiv:** https://arxiv.org/abs/2509.23870
- **关键发现：** 挑战 "reward miscalibration" 假说。Lemma 3.1 证明 flawed actions 的 expected advantage 天然为负。真正根因是 **gradient coupling**：agent 任务中连续 steps 的 input 高度相似，优化一个 sample 的梯度会增加相似 bad action 的概率。识别 **Danger Zone (q>0.5)**。明确指出 step-level reward 单独不能根治。ALFWorld: 85.1%→89.8%。
- **佐证强度：** 直接佐证（互补视角）
- **引用价值：** 可直接引用（需 acknowledge 其反面观点：expected advantage 天然正确，但这与我们的 per-sample sign analysis 不矛盾）

---

## 四、Tier 3：Step vs Episode Ablation 证据

### 4.1 GiGPO (NeurIPS 2025)
- **论文：** GiGPO: Group-in-Group Policy Optimization for LLM Agent Training
- **arXiv:** https://arxiv.org/abs/2505.10978
- **关键发现：** 双层结构：episode-level macro + step-level micro advantage。**关键 ablation：** 去掉 step advantage 性能大幅下降，去掉 episode advantage 同样下降，证明两个层级都不可或缺。ALFWorld: 86.1% vs GRPO 72.8% (+13.3pp); WebShop: 83.5 vs 75.8 (+10.6%)。
- **佐证强度：** 直接佐证
- **引用价值：** 可直接引用

### 4.2 GAGPO (2026)
- **论文：** GAGPO: Generalized Advantage Grouped Policy Optimization
- **arXiv:** https://arxiv.org/abs/2605.13217
- **关键发现：** 用 TD/GAE 风格递推替代 MC step advantage。批评 GiGPO "assigns the same episode-level offset to every step"。GiGPO step 120 时 43.1% advantage 超过 magnitude 1，GAGPO 仅 17.2%。ALFWorld 1.5B: 93.5 vs GiGPO 88.1 (+5.4)。
- **佐证强度：** 直接佐证
- **引用价值：** 可直接引用

### 4.3 iStar (NeurIPS 2025)
- **论文：** Agentic Reinforcement Learning with Implicit Step Rewards
- **arXiv:** https://arxiv.org/abs/2509.19199
- **关键发现：** A(a_t^i) = A_E(τ^i) + α·A_S(a_t^i) 合并 episode + step advantage。**Ablation：** vanilla RLOO 76.6% → merged rewards 81.3% → full iStar 89.1% (WebShop)。Token-level（PRIME）出现 sharp fluctuations，过细粒度反而不稳定。
- **佐证强度：** 直接佐证
- **引用价值：** 可直接引用

### 4.4 SWEET-RL (Meta, 2025)
- **论文：** SWEET-RL: Training Multi-Turn LLM Agents on Collaborative Reasoning Tasks
- **arXiv:** https://arxiv.org/abs/2503.15478
- **关键发现：** "Existing multi-turn RL algorithms fail to perform effective credit assignment over multiple turns"。Episode-level agents **在 10+ turns 后性能急剧下降**，step-wise reward agents 保持稳定。Llama-3.1-8B + SWEET-RL 达到 GPT-4o 水平。
- **佐证强度：** 直接佐证
- **引用价值：** 可直接引用

### 4.5 MT-GRPO (ICML 2025)
- **论文：** Reinforcing Multi-Turn Reasoning in LLM Agents via Turn-Level Credit Assignment
- **arXiv:** https://arxiv.org/abs/2505.11821
- **关键发现：** GRPO-OR (outcome reward only) exact match 仅 **0.04**，MT-GRPO 达到 **0.50** (12x)。GRPO-OR 训练中 **agent 完全放弃 tool use**（tool execution reward 降为 0）。
- **佐证强度：** 直接佐证
- **引用价值：** 可直接引用

---

## 五、Tier 4：理论基础

### 5.1 RUDDER (NeurIPS 2019)
- **论文：** RUDDER: Return Decomposition for Delayed Rewards
- **arXiv:** https://arxiv.org/abs/1806.07857
- **关键发现：** **核心定理：TD 的 bias 修正速度随 delay 长度指数级减慢。** MC 的 variance 随 delay steps 指数级增长。提出 return-equivalent MDP。RUDDER 比 MC/TD(λ)/MCTS **指数级更快**。
- **佐证强度：** 理论支持（均匀分配 reward 在 long-horizon 下失败的数学证明）
- **引用价值：** 可直接引用

### 5.2 COCOA (NeurIPS 2023 Spotlight)
- **论文：** Would I have gotten that reward? Long-term credit assignment by counterfactual contribution analysis
- **arXiv:** https://arxiv.org/abs/2306.16803
- **关键发现：** HCA 在很多环境中产生 **spurious estimates of contributions**，导致退化为高方差 REINFORCE。通过反事实分析实现精确 credit assignment。
- **佐证强度：** 直接佐证（spurious contribution estimates 与 sign misattribution 直接对应）
- **引用价值：** 可直接引用

### 5.3 Credit Assignment Survey (2026)
- **论文：** From Reasoning to Agentic: Credit Assignment in RL for LLMs
- **arXiv:** https://arxiv.org/abs/2604.09459
- **关键发现：** 47 种方法综述。"GRPO assigns identical advantage to a pivotal tool selection and a trivial formatting action"。梯度方差 O(T·Var[R])，从 10 到 100 个决策点方差增 10x。Agentic CA 仍是 open problem。
- **佐证强度：** 理论支持
- **引用价值：** 可直接引用

### 5.4 Credit Assignment Survey (经典 RL, 2023)
- **论文：** A Survey of Temporal Credit Assignment in Deep Reinforcement Learning
- **arXiv:** https://arxiv.org/abs/2312.01072
- **关键发现：** 统一框架：delayed effects、transpositions、lack of action influence 三大挑战。Sparse delayed reward 下无法区分 lucky outcomes 与 genuinely informed decisions。
- **佐证强度：** 理论支持
- **引用价值：** 背景引用

---

## 六、Tier 5：补充证据

| 论文 | arXiv | 关键点 | 佐证 |
|------|-------|--------|------|
| CARL (2025) | 2512.04949 | GRPO assumes equal contribution → noisy CA; 72% action 更新被跳过 | 间接 |
| HiPER (2026) | 2602.16165 | Flat RL → unstable optimization; ALFWorld 97.4% SOTA | 间接 |
| ArCHer (NeurIPS 2024) | 2402.19446 | Single-turn RL cannot do CA in multi-turn; 100x efficiency | 间接 |
| DAPO (ByteDance, 2025) | 2503.14476 | GRPO entropy collapse; Clip-Higher fix | 间接 |
| HCAPO (2026) | 2603.08754 | Hindsight CA for GRPO; ALFWorld +13.8% | 间接 |
| SPA-RL (2025) | 2505.20732 | Stepwise progress attribution; PPO advantage 在长 horizon 指数衰减 | 间接 |
| GTPO (2025) | 2511.14846 | Turn-level decomposition; "arbitrary and noisy reward feedback" | 间接 |
| REFUEL (2024) | 2410.04612 | Covariate shift 随 turn 数累积 | 间接 |
| Agent Lightning (Microsoft, 2025) | 2508.03680 | Episode→step CA + step-level RL 两步解耦 | 间接 |
| Planner-R1 (2025) | 2509.25779 | Dense process signals 让 8B 达 32B sparse-reward 性能 | 间接 |
| Bespoke Labs Blog (2025) | bespokelabs.ai | ~300步 GRPO collapse + gibberish blowup 工业案例 | 间接 |

---

## 七、与我们发现的对应关系

| 我们的发现 | 文献佐证 |
|---|---|
| **Step-independent GRPO → catastrophic collapse** | RAGEN (10-20步collapse), Turn-PPO (GRPO crash, 3种fix均失败), GRPO Collapse (300步内4模型全collapse), Bespoke Labs (工业案例) |
| **Advantage-outcome agreement ≈ 52% (≈随机)** | **IRC: 明确报告 A^I 与 A^O 方向不一致**; MC-GRPO: 5% sign-flip → 4% accuracy drop; G-RA: step reward 与 outcome 负相关; RAGEN-2: advantage≈0时方向随机 |
| **Sign misattribution 是根因** | Outcome-Grounded Reshaping: 使用 "advantage misattribution" 术语; ICLR 2026 Decoupled CA: sign/polarity misassignment; GRPO-λ Lemma 1: systematic misattribution |
| **Episode-level reward 无法 credit assign** | GiGPO ablation (+13.3pp), MT-GRPO (12x improvement), SWEET-RL (10+ turns 后 episode-level 崩溃), Credit Assignment Survey (variance 增 10x) |
| **需要 step-level 信号** | GiGPO, iStar, Turn-PPO, HiPER, ArCHer, SWEET-RL 等 10+ 篇提出不同粒度方案 |
| **但纯 step-level 也有问题** | Gradient Coupling (step reward alone 不够), iStar (token-level → fluctuations), GAGPO (MC step advantage 高方差) |

---

## 八、建议引用方案

### 核心引用（论文中必须出现，5-7 篇）

1. **RAGEN** (arXiv:2504.20073) + **RAGEN-2** (arXiv:2604.06268) — multi-turn agent RL collapse 的系统性研究，Echo Trap + advantage collapse 数学证明
2. **IRC** (arXiv:2604.02869) — 唯一明确报告 advantage sign disagreement 的工作，与我们的 52% 发现最直接对应
3. **GiGPO** (NeurIPS 2025, arXiv:2505.10978) — 顶会论文，clean step vs episode ablation
4. **RUDDER** (NeurIPS 2019, arXiv:1806.07857) — 理论基础：delay → bias 指数增长
5. **Credit Assignment Survey** (arXiv:2604.09459) — "identical advantage to pivotal and trivial actions"

### 强化引用（Related Work 中出现，3-5 篇）

6. **Turn-PPO** (arXiv:2512.17008) — GRPO crash 数据 + 3种fix均失败
7. **Gradient Coupling** (arXiv:2509.23870) — 互补视角，需 acknowledge 其反面观点
8. **MC-GRPO** (arXiv:2601.22582) — sign flip 定量分析
9. **GRPO-λ** (arXiv:2510.00194) — Lemma 1 证明 systematic misattribution
10. **SWEET-RL** (arXiv:2503.15478) — Meta 的工作，10+ turns 后 episode-level 失败

### 背景引用（按需）

11. G-RA (2508.10548) — sign divergence 可视化
12. GAGPO (2605.13217) — MC step advantage 方差问题
13. ArCHer (NeurIPS 2024) — hierarchical agent RL 先驱
14. Decoupled CA (ICLR 2026) — multiplicative gating for sign correction
15. COCOA (NeurIPS 2023) — counterfactual credit assignment

---

## 九、关键 Takeaway

1. **Sign misattribution 不是个例**——至少 6 篇独立工作从不同角度报告了 advantage/reward 方向错误问题
2. **GRPO collapse 在 agent 任务中是公认问题**——RAGEN, Turn-PPO, GiGPO, GRPO Collapse 等 10+ 篇论文报告了 collapse
3. **Episode-level → step-level 是领域共识方向**——2024-2026 年涌现 15+ 篇提出 step/turn-level CA 方案
4. **我们的独特贡献**——直接测量 advantage-outcome sign agreement rate (52%) 并将其与 catastrophic collapse 建立因果关系，这是其他工作没有做的定量分析
5. **反面观点需 acknowledge**——Gradient Coupling 论文认为 expected advantage 天然正确，问题在 gradient coupling 而非 sign error。但两者不矛盾：expected value 可以正确（大量样本平均），per-sample sign 仍可近乎随机（高 variance）
