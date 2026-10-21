# GRPO 替代/改进算法调研

**调研背景**：用 GRPO + Qwen3-1.7B 在 ALFWorld 上训练 agent，遇到三个核心问题：
1. Sparse 二值奖励 → 同一 group 内 reward 相同 → advantage=0 → pg_loss=0（零梯度）
2. Dense bonus 引入后 reward gaming（action_valid 60→97.5%，success→0%）
3. 即使出现 success 信号，单步 GRPO 更新过激 → catastrophic collapse

**调研截止**：2026-05（覆盖 ICLR 2026、NeurIPS 2025、arXiv 2024-2026）

注：原 task 要求 save_project_file 写入，但该文件不在白名单（白名单仅 memory.md/paper_framing.md/writing_plan.yaml），转写到 artifacts/。

---

## 1. SPEAR (Self-imitation with Progressive Exploration)
- **论文**："Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning"，Qin et al.（Tencent Youtu），arXiv 2509.22601，**ICLR 2026 接收**
- **核心思想**：课程式自模仿学习（SIL）。早期用辅助 tool-use reward 鼓励技能层面探索，后期逐步把权重切换到成功 trajectory 的 self-imitation；用 replay buffer 存正 advantage 轨迹做 off-policy 更新。
- **与我们场景的相关性**：⭐⭐⭐⭐⭐ **最直接相关**。明确针对 sparse-reward + long-horizon agent，**用同一个 ALFWorld + Qwen2.5-1.5B 设置在 GRPO 基础上 +16.1% success（72.8% → 88.9%）**。同时也跑了 WebShop（+20.7%）。三个核心问题它都覆盖：
  - sparse reward：early-stage 用 tool-call bonus 给信号
  - reward gaming：bonus 用 cosine schedule **衰减到 0**，最终只剩 outcome reward
  - collapse：self-imitation 用历史成功轨迹稳定梯度
- **关键公式**：
  - 复合奖励：`R = R_outcome + μ·R_tool-call + R_format`，`R_tool-call = min(1, 0.1·n_tool_call)`
  - 衰减：`μ = ½(cos(πt/T_decay)+1)`，t > T_decay 后 μ=0
  - SIL warm-up：`γ = ½(1 - cos(πt/T_warmup))`，逐步上升到 1
  - SIL 损失：`J_SIL = Σ J_GRPO_j · 𝟙(Â_j > 0 ∧ Ã_j > 0) · M_j`，Ã_j 是 50 分位 baseline 重新校准的 advantage
- **集成难度**：低-中。代码在 `TencentYoutuResearch/SPEAR`，**基于 GRPO + 修改**（去掉 KL，clip-higher 0.28/0.2，去掉 intra-group 归一化）。如果 RAGEN 已经在 verl/TRL 上跑通 GRPO，加 replay buffer + 双 cosine schedule + SIL loss 项即可。
- **关键超参**：
  - replay buffer size N_D = 2000-4000
  - baseline buffer N_DR = 500
  - T_warmup ≈ T_decay ≈ 200 steps
  - clip ratio λ = 0.0002-0.02（mask 高 covariance token）
  - KL coef = 0
- **风险**：
  - 我们 exp013 试过 valid_action_bonus=0.15 已经 gaming 了，SPEAR 的 `0.1·n_tool_call` 系数类似量级——必须严格遵守 cosine decay，否则同样 gaming
  - 1.7B 模型在 ALFWorld 初期 success≈0%，replay buffer 可能长时间为空 → 退化成 GRPO；可考虑用 SFT warm-up 让 buffer 先有种子轨迹

---

## 2. GiGPO (Group-in-Group Policy Optimization)
- **论文**："Group-in-Group Policy Optimization for LLM Agent Training"，Feng, Xue, Liu, An（NTU），arXiv 2505.10978，**NeurIPS 2025**
- **核心思想**：两层 group 结构做细粒度 credit assignment：episode 级用整条 trajectory 算 macro advantage；step 级用 **anchor state grouping**——把跨 trajectory 出现的相同环境状态聚成一组，在该组内对动作算 micro advantage。
- **与我们场景的相关性**：⭐⭐⭐⭐ 主要解决 sparse outcome reward 下的 credit assignment 问题。同样在 ALFWorld + Qwen2.5-1.5B/3B/7B-Instruct 上验证，**vs GRPO +12% on ALFWorld，+9% on WebShop**。不直接解决 collapse，但通过 step-level 信号让 advantage 更稳定（少一些零梯度 group）。
- **集成难度**：中。代码在 `langfengq/verl-agent`（verl-agent 是 verl 的 agent 扩展）。如果 RAGEN 也基于 verl，迁移成本低；核心改动是 rollout 后做状态 hash + 重新分组。**关键依赖**：环境状态可哈希/可识别相同状态——ALFWorld 部分观测下要小心，可能需要用前 N 步 observation 拼接做 anchor。
- **关键超参**：episode-level 和 step-level advantage 的加权系数（论文需查）。
- **风险**：
  - ALFWorld 状态空间大，"相同 anchor state" 可能很少出现 → step-level group 太小 → 仍是 sparse 信号
  - 实现复杂度比 SPEAR 高一些

---

## 3. EPO (Entropy-regularized Policy Optimization for LLM Agents)
- **论文**："EPO: Entropy-regularized Policy Optimization for LLM Agents Reinforcement Learning"，Wujiang Xu et al.，arXiv 2509.22576（2025-09，2026-02 更新）
- **核心思想**：诊断了 sparse-reward 多轮 agent 训练的 **"exploration-exploitation cascade failure"**——前期 sparse feedback 让 policy 过早收敛到 flawed strategies；后期 vanilla entropy 正则反而引发混乱探索导致 collapse。EPO 三机制：(1) 多轮设置下加 entropy 正则，(2) **entropy smoothing regularizer**——把 policy entropy 约束在历史均值范围内防止突变，(3) 自适应阶段权重，平衡探索/利用。
- **与我们场景的相关性**：⭐⭐⭐⭐ 论文描述的 cascade failure 与我们 exp013→exp015 观察到的「先 gaming 再 collapse」非常相似。ALFWorld +19.8%，ScienceWorld +152%。代码在 `WujiangXu/EPO`。
- **集成难度**：中。需要维护历史 entropy 滑动均值，并把 entropy bound 加进 loss——比 SPEAR 改动小，但比单纯加 entropy coef 复杂。
- **关键超参**：entropy 历史窗口大小、entropy bound 的上下限、阶段切换 schedule。
- **风险**：
  - 我们 exp015 已经用 kl_coef=0.1 + lr=1e-7 做稳定性修复，再叠加 EPO 可能过约束（entropy 完全压死 → 无探索）
  - "保证 entropy variance 单调下降"听起来像主动抑制探索，对 1.7B 这种已经 entropy 偏低的模型可能不利

---

## 4. DAPO (Decoupled Clip and Dynamic sAmpling Policy Optimization)
- **论文**："DAPO: An Open-Source LLM Reinforcement Learning System at Scale"，ByteDance Seed，arXiv 2503.14476（2025-03）
- **核心思想**：在 Qwen2.5-32B 上 50% 步数超过 DeepSeek-R1-Zero-Qwen-32B。四个关键技术：
  1. **Clip-Higher**：解耦上下 clip，把上 clip 从 0.2 扩到 0.28，鼓励低概率 token 上升，**防止 entropy collapse**
  2. **Dynamic Sampling**：丢弃 acc=0 和 acc=1 的 prompt group（这些 group 内 advantage 全相同），保留有梯度的样本
  3. **Token-level Policy Gradient Loss**：长 CoT 场景下不再按序列平均
  4. **Overlong Reward Shaping**：长输出的奖励 shaping，降低噪声
- **与我们场景的相关性**：⭐⭐⭐⭐ **Dynamic Sampling 直接解决我们「group 内 reward 全相同 → 零梯度」的问题**——把这种 group 丢掉、resample 直到 batch 内有有效梯度的样本。Clip-Higher 缓解 entropy collapse。
- **集成难度**：低。已被 verl 原生支持，TRL 也有 PR。改三个参数就能开 Clip-Higher，Dynamic Sampling 需要在 batch 构造时加过滤逻辑。
- **关键超参**：ε_low=0.2, ε_high=0.28（论文默认值）；Dynamic Sampling 的 oversample 倍数
- **风险**：
  - 注意：**有研究发现 Dynamic Sampling 在某些设置下不提升性能甚至有害**（见 arxiv 2512.07611）——需要消融
  - DAPO 是为单轮长 CoT reasoning 设计，agent 多轮场景需要额外验证
  - Dynamic Sampling 在 success≈0% 的初期意味着**一直丢弃所有 group**（全 acc=0），可能完全无法启动训练——需要配合 SPEAR 式 bonus 或 SFT warm-up

---

## 5. GTPO (Stabilizing GRPO via Gradient and Entropy Control)
- **论文**："GTPO: Stabilizing Group Relative Policy Optimization via Gradient and Entropy Control"，arXiv 2508.03772（2025-08）
- **核心思想**：诊断 GRPO 两个本质问题：(1) **同 group 内不同 completion 共享的 token 收到矛盾梯度**（gradient conflict）；(2) negative-reward completion 对 confident token 施加惩罚导致 **policy collapse**。GTPO：跳过这些 token 的 negative update，只放大 positive；按 entropy 阈值过滤高 entropy completion；**完全不依赖 KL**（不需要 reference model）。
- **与我们场景的相关性**：⭐⭐⭐ 直接针对 collapse 现象。但实验集中在数学推理（GSM8K/MATH/AIME），agent 任务上未验证。
- **集成难度**：中。需要在 token 级做 gradient 路由（识别哪些 token 跨 completion 共享）。
- **关键超参**：entropy 阈值；conflict 检测的 token 共现窗口
- **风险**：未在 agent 任务上验证；跨 completion 的共享 token 在 agent 多轮场景定义不同（每轮 prompt 不同）

---

## 6. Dr. GRPO (Length-bias 修正)
- **论文**：来自 "Understanding R1-Zero-Like Training: A Critical Perspective"（2503.20783）等工作
- **核心思想**：GRPO 原版按序列长度归一化导致长的错误回复被欠惩罚。Dr. GRPO 用全局常数归一化，消除长度偏差。
- **与我们场景的相关性**：⭐⭐ 主要解决 length bias，不直接解决 sparse reward / collapse / gaming。但 SPEAR 内部就用了类似策略（去掉 intra-group 归一化）。
- **集成难度**：极低。verl 里改 `loss_agg_mode="seq-mean-token-sum-norm"` 即可。
- **风险**：单独用不解决我们的核心问题；可作为基础设置叠加在其他算法上

---

## 7. GDPO (Group reward-Decoupled Normalization)
- **论文**："GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization"，NVlabs，arXiv 2601.05242
- **核心思想**：注意：GDPO 这里指 "Group reward-Decoupled"，**不是** "Group Distributionally-robust"。专门解决**多奖励**场景下 GRPO 把不同 reward 组合 normalize 到同一 advantage 而丢失分辨率的问题。Key trick：**先 normalize 再聚合**（与原 GRPO 顺序相反）。
- **与我们场景的相关性**：⭐⭐⭐ 如果我们坚持用 sparse outcome + dense bonus 的多奖励组合（exp013 的方向），GDPO 比 GRPO 更合适——能保留 success 信号和 bonus 信号的分辨率，**潜在缓解 reward gaming**（因为不同 reward 维度的相对差异被保留）。代码在 `NVlabs/GDPO`。
- **集成难度**：中。需要把 reward 拆成多维度，分别 normalize。
- **关键超参**：各 reward 维度的相对权重
- **风险**：仍未根本解决 gaming——只是让 success 信号不被 bonus 淹没；如果 success 信号本身缺失（初期），多奖励解耦也救不了

---

## 8. StarPO-S (RAGEN 自带的稳定化变体)
- **论文**：RAGEN 论文（arXiv 2504.20073），"Understanding Self-Evolution in LLM Agents via Multi-Turn RL"
- **核心思想**：三个稳定化机制：(1) **variability-based trajectory filtering**——丢弃 group 内 reward variance 低的 trajectory（默认丢 25%）；(2) critic baselining；(3) decoupled clipping。
- **与我们场景的相关性**：⭐⭐⭐⭐ **我们用的就是 RAGEN，这是开箱即用方案**。trajectory filtering 与 DAPO Dynamic Sampling 思路一致。论文还观察到「GRPO 在 Bandit 上 20 步开始 collapse，PPO 100 步才 collapse；reward std 和 entropy 是 early warning」——和我们看到的现象一致。
- **集成难度**：极低（已在 RAGEN 仓库内）。
- **关键超参**：filtering rate（默认 25%）；decoupled clip 上下限
- **风险**：低。可作为 baseline 设置

---

## 9. VAPO (Value-Augmented Proximal PO)
- **论文**："VAPO: Efficient and Reliable Reinforcement Learning for Advanced Reasoning Tasks"，ByteDance，arXiv 2504.05118（2025-04）
- **核心思想**：value-based 方法（保留 critic，与 GRPO 路线相反）。解决 value model bias、长序列异质性、reward sparsity 三大问题。**value-pretraining**：用 fixed policy 的 Monte Carlo return 预训练 value network，避免 value 初始 bias。
- **与我们场景的相关性**：⭐⭐⭐ 直接讨论 sparse reward。但属于 PPO 路线，要恢复 critic，对 1.7B 显存不大友好（不过 1.7B 还好）。AIME 上 60.4，**无训练 crash**。
- **集成难度**：中-高。需要切换回 PPO + critic，多出 value 预训练阶段。
- **关键超参**：value pretraining 步数；GAE λ
- **风险**：PPO 路线整体收敛比 GRPO 慢；agent 场景未验证

---

## 10. ARPO (Agentic Reinforced PO)
- **论文**："Agentic Reinforced Policy Optimization"，RUC-NLPIR，arXiv 2507.19849，**ICLR 2026 接收**
- **核心思想**：观察到 LLM 在 tool-call 后 entropy 升高（不确定性增大）→ **entropy-based adaptive rollout**：在高 entropy 的 tool-call 轮次自适应分支采样。advantage attribution estimation 让 LLM 内化 stepwise 工具使用的 advantage 差异。
- **与我们场景的相关性**：⭐⭐⭐ ALFWorld 是工具/动作型 agent，思路适用但论文重点是 search/tool-use。
- **集成难度**：中。需要 rollout 阶段做自适应分支，与 verl 现有同步 rollout 不太一样。
- **关键超参**：entropy 触发阈值；分支因子
- **风险**：rollout 改造工程量；agent 任务 entropy 信号是否可靠未知

---

## 11. AgentHER / ECHO (Hindsight Trajectory Relabeling)
- **论文**：
  - AgentHER：arXiv 2603.21357
  - ECHO（Sample-Efficient Online Learning via Hindsight Trajectory Rewriting）：arXiv 2510.10304
- **核心思想**：把失败 trajectory 用 LLM 改写成「针对 goal B 的成功 trajectory」——失败一次仍能产生学习信号。AgentHER 报告 WebArena/ToolBench 上 +7.1~11.7pp。
- **与我们场景的相关性**：⭐⭐⭐ 针对 sparse reward 下 "0% success → 0 信号" 的根本问题。但当前主要用于 **offline SFT 数据增强**，online RL 集成方案尚不成熟。
- **集成难度**：中-高。需要 LLM 改写 trajectory（额外推理成本），且要确认 ALFWorld 任务 goal 可以重新标注（ALFWorld 是文本游戏，goal 是"在 X 中放 Y"，理论上可改写）。
- **关键超参**：relabel 的 trajectory 占比；改写温度
- **风险**：可能引入 reward hacking（改写后的"成功"与原任务无关）；多一个推理 pipeline

---

## 12. i-MENTOR / LLM 驱动内在动机
- **论文**："Navigate the Unknown: Enhancing LLM Reasoning with Intrinsic Motivation Guided Exploration"（arXiv 2505.17621）；"LLM-Driven Intrinsic Motivation for Sparse Reward RL"（arXiv 2508.18420）
- **核心思想**：用 VAE state novelty 或 LLM 评估 state novelty 给 intrinsic reward。
- **与我们场景的相关性**：⭐⭐ 思路通用，但偏经典 RL，没在 ALFWorld LLM agent 上验证。
- **集成难度**：高（需要训 VAE 或加 LLM 评估 callback）
- **风险**：与 SPEAR 的 tool-call bonus 类似 → 仍有 gaming 风险；额外训练成本

---

## 13. MT-GRPO (Turn-Level Reward Design)
- **论文**："Reinforcing Multi-Turn Reasoning in LLM Agents via Turn-Level Reward Design"，arXiv 2505.11821，**NeurIPS 2025**
- **核心思想**：把 outcome reward 拆到 turn 级——每一轮给一个中间奖励。GRPO/PPO 扩展为 MT-GRPO/MT-PPO。
- **与我们场景的相关性**：⭐⭐ 思路合理，但 ALFWorld 的「每轮是否合法/有进展」难以自动给出 turn 级奖励（需要 process reward model 或环境信号）。
- **集成难度**：中。如果 ALFWorld 能给 turn 级 progress 信号（如目标距离），直接接入。
- **风险**：与 dense bonus 同一类问题——turn 级奖励容易被 game

---

## 总结推荐表

| 算法 | 解决问题 | 集成难度 | 推荐优先级 | 备注 |
|------|---------|---------|----------|------|
| **SPEAR** | sparse + gaming + collapse 全覆盖 | 低-中 | **★★★★★ P0** | 同设置 ALFWorld 实测 +16.1%；ICLR 2026；课程 + SIL 优雅解决 gaming |
| **GiGPO** | sparse credit assignment | 中 | **★★★★ P1** | ALFWorld +12%；verl-agent 已实现；可与 SPEAR 叠加（SPEAR 论文也对比了 GiGPO） |
| **DAPO 组件** | 零梯度 group + entropy collapse | 低 | **★★★★ P1** | Dynamic Sampling 直接解决「group 全相同」；Clip-Higher 防 collapse；可单独抽取组件叠加 |
| **EPO** | cascade failure（gaming→collapse） | 中 | ★★★ P2 | ALFWorld +19.8%；与 exp015 已有的稳定性修复方向重合，需消融 |
| **StarPO-S** | 一般稳定化 | 极低 | ★★★ P2 | RAGEN 自带，立即可用；与 DAPO Dynamic Sampling 思路重叠 |
| **GDPO** | 多奖励解耦（缓解 gaming） | 中 | ★★ P3 | 仅在保留 dense bonus 时有意义；不解决 sparse 启动问题 |
| **GTPO** | gradient conflict + collapse | 中 | ★★ P3 | 仅推理任务验证；agent 场景未知 |
| **VAPO** | 切回 critic 路线 | 中-高 | ★★ P3 | 改动大；显存/速度劣于 GRPO 系 |
| **ARPO** | tool-call 自适应 rollout | 中 | ★★ P3 | rollout 改造工程量 |
| **AgentHER/ECHO** | 失败轨迹重标 | 中-高 | ★★ P3 | 当前 online RL 集成不成熟，更适合 SFT 阶段 |
| **MT-GRPO** | turn-level credit | 中 | ★ P4 | 需要外部 progress 信号 |
| **Dr. GRPO** | length bias | 极低 | ★ basic | 作为基础设置叠加 |

---

## 行动建议

**短期（1-2 周）**：
- 落地 **SPEAR**，直接复用其 ALFWorld + Qwen2.5-1.5B 配置作为强 baseline（我们用 Qwen3-1.7B 接近）：复合 reward + cosine decay + SIL replay buffer
- 同时叠加 **DAPO 的 Clip-Higher (0.2/0.28) + Dynamic Sampling 过滤 all-same-reward group**，几乎零成本
- 设置 **StarPO-S filtering** 作为额外保险

**消融**：
- SPEAR 复合 reward 单独 vs SPEAR + SIL → 确认 SIL 贡献
- 关掉 cosine decay 看是否 gaming（验证 decay 的必要性）
- 用 SPEAR 默认 KL=0 vs 我们 exp015 的 KL=0.1 → 哪个更稳

**中期备选**：
- 如果 SPEAR + DAPO 组件仍不够稳，叠加 **GiGPO step-level advantage**
- 如果 1.7B 初期 replay buffer 长期为空，先做 **expert trajectory SFT warm-up**（ALFWorld 有 ground-truth solver 可生成专家轨迹）

**不推荐近期尝试**：
- VAPO（切 PPO 路线工程量过大）
- AgentHER online 集成（不成熟）
- 单独的 GDPO/GTPO（缺 agent 任务验证）

---

## 关于原 task 提到的算法的纠正

- **"GDPO = Group Distributionally-robust PO"**：搜不到完全对应该名称的工作。最接近的是 NVlabs 的 "Group reward-Decoupled" GDPO，**作用完全不同**（多奖励解耦，不是 distributional robustness）。"Distributionally Robust DPO" 有相关工作（OpenReview D19hc2XPeZ），但那是 alignment 场景，不是 RL agent。
- **"DAPO = Decoupled Alignment PO"**：原始 DAPO 全称是 "**Decoupled Clip and Dynamic sAmpling Policy Optimization**"（ByteDance），不是 "Alignment"。Clip-higher + Dynamic Sampling 部分原 task 描述正确。
- **SPEAR**：与原 task 描述一致，确为 sparse-reward agent 训练方法。

---

## 参考资源

- SPEAR 代码：https://github.com/TencentYoutuResearch/SPEAR
- GiGPO 代码：https://github.com/langfengq/verl-agent
- DAPO 项目页：https://dapo-sia.github.io/
- EPO 代码：https://github.com/WujiangXu/EPO
- RAGEN/StarPO-S：https://github.com/mll-lab-nu/RAGEN
- ARPO 代码：https://github.com/RUC-NLPIR/ARPO
- 综述：blacksnail789521/Agentic-RL-Training-Recipes（持续更新）
