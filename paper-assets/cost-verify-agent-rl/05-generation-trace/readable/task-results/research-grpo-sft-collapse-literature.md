# research grpo sft collapse literature

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_grpo-sft-collapse-literature_20260515T005806_result.json`
- **Structured JSON:** [`066ea86fdd4873b91786.json`](../../sessions/06/066ea86fdd4873b91786.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 调研结果

---

### 问题 1: SFT → GRPO/PPO 的 Catastrophic Forgetting

**关键发现**：SFT 学到的 task knowledge 在 RL 阶段被遗忘是已知问题。研究表明遗忘主要源于"function activation bias 偏移"而非知识真正被覆盖——RL 改变了模型对 prompt 的响应模式，使原有 task processing pathway 无法正确激活。

**相关论文**：
- **Robust Policy Optimization to Prevent Catastrophic Forgetting** — 提出在 KL 邻域内优化 reward-flatness，找到适应后仍保持高 reward 的 flat region policy
- **LUFFY** (ICLR 2025) — 将 expert demonstrations 集成到 GRPO rollout group 中，使 SFT 知识持续作为 baseline 参与梯度计算
- **SASR** — 概率性交替执行 SFT step 和 RL step，防止 RL 梯度完全主导

**缓解方案**：
1. **SFT replay mixing**：每个 GRPO batch 中混入 10-20% 的 SFT 数据作为 replay buffer（类似 LUFFY 方法），在 GRPO advantage 计算中将 expert trajectory 作为 group 成员
2. **增大 KL penalty**：当前 KL=0.0092 太小，说明 KL 约束形同虚设。将 `kl_coef` 从当前值提升 5-10x
3. **Warm reference update**：每 N 步用 EMA 更新 reference model（而非固定 SFT checkpoint），减少 RL policy 与 reference 的 distribution shift

---

### 问题 2: Entropy Collapse in GRPO

**关键发现**：entropy 0.107→0.045 是典型的策略坍缩。GRPO 原生没有 entropy bonus，clip 机制对低概率 token 的抑制效应会加速 entropy 下降。DAPO 和 EPO 分别从 clip 策略和 regularization 角度解决此问题。

**相关论文**：
- **DAPO** (arXiv:2503.14476) — Clip-Higher：不对称 clipping（ε_low=0.2, ε_high=0.28），允许低概率 token 的 ratio 突破上界，增加 entropy。Qwen2.5-32B 在 AIME 上达到 50 分
- **EPO** (arXiv:2509.22576) — Entropy-regularized Policy Optimization，专为 multi-turn agent 设计。在 ALFWorld 上提升 19.8%。核心：entropy smoothing regularizer 将 entropy 约束在历史均值附近 + adaptive phase-based 权重
- **GTPO** (arXiv:2508.03772) — Gradient-preserving clipping + entropy control，解决 GRPO 梯度冲突
- **T2PO** (arXiv:2605.02178) — Uncertainty-guided exploration control for multi-turn agent RL

**缓解方案**：
1. **Clip-Higher**（最易实现）：将 GRPO 的 upper clip 从 1+ε 改为 1+ε_high（ε_high=0.28），下界保持 1-ε_low（ε_low=0.2）
2. **显式 entropy bonus**：在 loss 中加 `-β * H(π)`，β 初始 0.01-0.05，随训练 anneal
3. **Token-level temperature scaling**：训练时 temperature=1.2-1.5 采样，greedy 推理时 temperature=1.0

---

### 问题 3: Sparse Reward + GRPO 冷启动

**关键发现**：~20% base success 在 sparse binary GRPO 中处于"危险区"。当 group 内 16 个 sample 全部失败时（概率 (0.8)^16 ≈ 3%），reward variance=0，梯度为零。但更致命的是：大部分 group 可能只有 1-3 个成功 sample，advantage 估计方差极大。S-GRPO 论文明确指出这是 "optimization collapse" 的根因。

**相关论文**：
- **S-GRPO** (arXiv:2604.16557) — Conditional Ground-Truth Trajectory Injection (CGI)：当 group 内成功数低于阈值时，注入 ground-truth trajectory，保证正向学习信号
- **RAGEN** (arXiv:2504.20073) — 发现 Echo Trap：reward variance collapse → entropy drop → gradient spike 的恶性循环。StarPO-S 通过 variability-based trajectory filtering 丢弃低信息量 rollout
- **E-GRPO** (arXiv:2601.00423) — 识别 high-entropy step 贡献有效探索，low-entropy step 产生无区分度 rollout

**缓解方案**：
1. **Dense intermediate reward**（最重要）：不要只给终局 won=10.0。加入中间 reward：
   - action validity reward: +0.5/valid action
   - progress reward: 每完成一个 subgoal +1.0
   - format compliance: +0.2
2. **CGI 注入**：当 group 内 success < 2 时，将 SFT 期间的成功 trajectory 注入 group 参与 advantage 计算
3. **Increase group size**：从 16 提到 32 或 64，增加采到成功 sample 的概率（20% success → group=32 时期望 6.4 个成功 sample）

---

### 问题 4: pass@K 高但 Greedy 差

**关键发现**：这是经典的 "exploration-exploitation 解耦" 现象。模型的 probability mass 分散在多个合理策略上，pass@16=1.0 说明正确策略在 support 中，但 mode（greedy）不在正确策略上。这表明模型倾向于在错误但高概率的 pattern 上 exploit。

**相关论文**：
- **Pass@k Training** (arXiv:2508.10751) — 用 pass@k 作为 reward（而非 pass@1），直接优化模型的 coverage ability，发现 exploration 和 exploitation 可以互增强
- **Token Hidden Reward (THR)** (arXiv:2510.03669) — token-level advantage reweighting，positive THR 增强正确输出的 confidence，negative THR 保留 alternative 概率
- **SimKO** (arXiv:2510.14807) — Simple Pass@K Policy Optimization，直接将 pass@k 集成到 policy gradient

**缓解方案**：
1. **Best-of-N filtering for GRPO**：在 advantage 计算时，对成功 trajectory 给予额外 bonus weight，使 mode 向成功策略移动
2. **降低采样温度训练**：当前可能 temperature 过高导致 probability mass 过于分散。训练时使用 temperature=0.8-1.0 而非更高值
3. **Majority voting reward**：用 pass@1 而非 pass@16 作为 reward signal，或用 `reward = success * (1/rank)` 给 greedy-consistent 的成功 trajectory 更高权重

---

## 推荐下一步实验方案（Top 3）

### 方案 1: Dense Reward + Entropy Control（最推荐）
- **改动**：将 sparse binary reward 改为 dense reward：`R = 0.3*format + 0.3*valid_action + 0.4*subgoal_progress + 10.0*won`
- **同时**：加 entropy bonus β=0.02，或实现 DAPO Clip-Higher（ε_high=0.28）
- **预期**：解决冷启动 + 防止 entropy collapse 的双重问题
- **复杂度**：中等（需要定义 intermediate reward function）

### 方案 2: SFT Replay + KL 约束增强（最简单）
- **改动**：每个 GRPO batch 混入 20% SFT 成功 trajectory；将 `kl_coef` 提升至 0.05-0.1
- **预期**：直接解决 catastrophic forgetting，保持 SFT 学到的 task knowledge
- **复杂度**：低（只改 data sampling 和一个超参）

### 方案 3: EPO 式 Entropy Smoothing + CGI 注入
- **改动**：实现 EPO 的 entropy smoothing regularizer（约束 entropy 在历史 MA±δ 范围内）；当 group 内 success<2 时注入 expert trajectory
- **预期**：同时解决 entropy collapse 和 sparse reward 信号不足
- **复杂度**：中高（需要实现 EPO loss + trajectory injection 逻辑）

---

**核心判断**：你的场景（20% base success + sparse reward + entropy collapse）几乎完美匹配 RAGEN 论文描述的 Echo Trap 和 EPO 论文描述的 exploration-exploitation cascade failure。最大的杠杆是 **加入 intermediate reward**——纯 sparse binary reward 在 20% success rate 下学习信号严重不足，这是根因。

Sources:
- [EPO: Entropy-regularized Policy Optimization](https://arxiv.org/abs/2509.22576)
- [RAGEN: Multi-Turn Reinforcement Learning](https://arxiv.org/abs/2504.20073)
- [DAPO: Open-Source LLM RL at Scale](https://arxiv.org/html/2503.14476v1)
- [S-GRPO: Unified Post-Training for VLMs](https://arxiv.org/abs/2604.16557)
- [Pass@k Training](https://arxiv.org/abs/2508.10751)
- [GTPO: Gradient and Entropy Control](https://arxiv.org/html/2508.03772v4)
- [Token Hidden Reward](https://arxiv.org/html/2510.03669v4)
- [Post-Training in 2026: GRPO, DAPO, RLVR & Beyond](https://llm-stats.com/blog/research/post-training-techniques-2026)
- [Reinforcing Multi-Turn Reasoning via Turn-Level Reward](https://arxiv.org/html/2505.11821v2)
- [Enhancing Agentic RL with Progressive Reward Shaping](https://arxiv.org/abs/2512.07478)
- [Robust Policy Optimization to Prevent Catastrophic Forgetting](https://arxiv.org/html/2602.08813)
- [T2PO: Uncertainty-Guided Exploration Control](https://arxiv.org/html/2605.02178v1)

---
